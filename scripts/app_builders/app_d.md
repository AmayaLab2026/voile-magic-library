# 附录 D：TrueType、OpenType 与 AAT 字体底层文件格式全景指南

*译者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

1989 年，苹果公司为了打破 Adobe 在 PostScript 字体解释器授权费用上的垄断，启动了代号为“皇家（Royal）”的秘密项目，由 Sampo Kaasila 等人主导研发了 **TrueType 字体格式**。随后，微软与苹果达成历史性的跨平台技术交换协议：微软向苹果提供 TrueImage 页面渲染技术，苹果向微软全面开放 TrueType 规范。1996 年，微软与 Adobe 宣布握手言和，共同将 TrueType 容器扩展为兼容 PostScript CFF 轮廓与复杂书写系统高级排版特性的 **OpenType**；而苹果则在 TrueType GX 基础上演进出了 **Apple Advanced Typography（AAT）**。

无论是 `.ttf`、`.otf` 还是苹果的 `.dfont` 与 `.ttc`，它们在物理底层均统一归属于 **SFNT（Spline Font / Scaled Font）容器体系**。本附录将对 SFNT 容器总线、TTX XML 表达范式、TrueType 核心表、OpenType 布局表（GSUB/GPOS/GDEF/BASE/JSTF）以及 AAT 有限状态自动机扩展表进行彻底的工业级全景解构。

---

## D.1 SFNT 容器总线拓扑与目录寻址机制

一个 SFNT 字体文件本质上是一个**基于 4 字节 ASCII 标签索引的小型只读文件系统**：

```c
struct TableDirectory {
    uint32 sfntVersion;     /* 格式识别魔数：0x00010000 代表 TrueType 轮廓，0x4F54544F ('OTTO') 代表 CFF OpenType */
    uint16 numTables;       /* 文件中包含的二进制子表总数 */
    uint16 searchRange;     /* 小于等于 numTables 的最大 2 的幂乘以 16：(2^floor(log2(numTables))) * 16 */
    uint16 entrySelector;   /* 二分查找最大幂次迭代步数：floor(log2(numTables)) */
    uint16 rangeShift;      /* numTables * 16 - searchRange */
    /* 紧随其后为 numTables 个子表目录项，严格按 tag 字典序升序排列： */
    struct TableRecord {
        uint32 tag;         /* 4 字节 ASCII 表名标签（如 'head', 'glyf', 'GSUB'） */
        uint32 checkSum;    /* 该子表的 32 位校验和 */
        uint32 offset;      /* 该子表在文件中的起始字节偏移量 */
        uint32 length;      /* 该子表的实际字节长度 */
    } tables[numTables];
};
```

### 1. 32 位校验和计算法则：
排版引擎遍历子表内部的所有 32 位大端整数进行累加（忽略溢出，模 $2^{32}$）：

$$\text{TableCheckSum} = \sum_{i=0}^{\lfloor (\text{length}+3)/4 \rfloor - 1} \text{Word32}_i$$

若子表字节长度不是 4 的倍数，在计算校验和时末尾补零对齐。在全字体中，`head` 表的 `checkSumAdjustment` 字段具有特殊的校验和平衡使命：计算全文件的 32 位总累加和，用神圣常数 `0xB1B0AFBA` 减去该值并存入 `head` 表，使得全字体所有 32 位字相加的最终结果恒等于 `0xB1B0AFBA`！

::: tip SFNT 容器总线目录与子表偏移寻址拓扑（Figure D-1, D-2）
![SFNT 目录拓扑（Figure D-1）](/images/fonts-encodings/fig-app-d1.png)
*SFNT 目录拓扑（Figure D-1）*
:::

*图 D-1：SFNT 顶层目录与各个子表之间的物理指针拓扑。所有子表目录项按 tag 字母顺序排列，支持二分查找。*

::: tip SFNT 子表校验和与内存页对齐（Figure D-2）
![SFNT 校验和对齐（Figure D-2）](/images/fonts-encodings/fig-app-d2.png)
*SFNT 校验和对齐（Figure D-2）*
:::

*图 D-2：子表在文件中的 4 字节边界对齐，便于现代操作系统内核直接发起零拷贝内存映射（Zero-copy mmap）。*

#### Python 工业级 SFNT 目录解析器实现：
```python
import struct

def parse_sfnt_directory(font_data: bytes):
    sfnt_version, num_tables, search_range, entry_selector, range_shift = struct.unpack(">I4H", font_data[:12])
    print(f"SFNT Version: 0x{sfnt_version:08X}, Tables Count: {num_tables}")
    
    tables = {}
    offset = 12
    for _ in range(num_tables):
        tag_bytes, checksum, table_offset, length = struct.unpack(">4s3I", font_data[offset:offset+16])
        tag = tag_bytes.decode('ascii', errors='replace')
        tables[tag] = {
            'checksum': checksum,
            'offset': table_offset,
            'length': length,
            'data': font_data[table_offset:table_offset+length]
        }
        offset += 16
    return tables
```

---

## D.2 TTX：基于 XML 的 TrueType/OpenType 镜像表达体系

与纯文本的 PostScript 字体不同，TrueType 是一门彻底二进制化的字型容器格式。由于内部充斥着密集的 16 位和 32 位相对指针与字节对齐偏移，传统人类开发者若不借助专用的十六进制编辑器，根本无法对其进行阅读、审查或版本控制。

2001 年，荷兰字体设计师尤斯特·范罗苏姆（Just van Rossum，Python 语言创始人吉多·范罗苏姆之弟）推出了革命性的开源工具 **TTX（TrueType XML）**。TTX 能够将任意 SFNT 二进制字库无损解构为一份语义高度明晰的 XML 文档；更重要的是，它能够执行严格对称的逆向编译，将 XML 重新组装为完全一致的二进制字体文件！

在 TTX 的哲学中：
* 整个字体表现为一个 `<ttFont>` 根节点；
* 每一个 SFNT 数据表映射为一个直接子元素（如 `<head>`, `<maxp>`, `<glyf>`, `<GSUB>`）；
* 表内部的字段、标志位与字形坐标映射为 XML 属性或嵌套子元素；
* 所有字形由人机可读的具名符号（Glyph Names，如 `glyph00042`, `A`, `acute`, `uni4E2D`）进行逻辑引用，彻底消除了底层手工维护 GID 指针的痛苦。

---

## D.3 TrueType Collections（TTC）多重字体集合容器

在处理东亚超大型中日韩字库时，同一款字体的不同变体（例如宋体、仿宋、细黑、粗黑，或竖排比例变体）往往需要复用数万个完全相同的汉字字形轮廓。如果为每种样式打包一个独立的 `.ttf` 文件，将造成巨额的磁盘与内存浪费。

为此，微软与苹果联合制定了 **TrueType Collection（TTC，通常文件扩展名为 `.ttc`）** 格式：
* **`ttcf` 集合头**：以魔数 `0x74746366`（'ttcf'）开头；
* **Header 版本**：1.0 版或 2.0 版（2.0 增加了数字签名 DSIG 支持）；
* **`numFonts`**：集合内部封装的逻辑字体总数；
* **`offsetTable[numFonts]`**：指向各个逻辑字体自身 `TableDirectory` 的起始字节偏移数组。

```
+-------------------------------------------------------+
|  TTC 物理文件拓扑 (TrueType Collection Topology)        |
+-------------------------------------------------------+
|  'ttcf' Header (Magic, Version, numFonts, Offsets)    |
|  ├── Font 0 Table Directory ───────────┐              |
|  └── Font 1 Table Directory ─────┐     │              |
|                                  │     │              |
|  [共享物理数据表]                  │     │              |
|  ├── 'glyf' Table (完全共享!) <────┴─────┘              |
|  ├── 'loca' Table (完全共享!) <────┴─────┘              |
|  [独立物理数据表]                                      |
|  ├── Font 0 'name' Table (名称: "MingLiU")            |
|  ├── Font 1 'name' Table (名称: "PMingLiU")           |
|  ├── Font 0 'cmap' Table (等宽映射)                    |
|  └── Font 1 'cmap' Table (比例变宽映射)                |
+-------------------------------------------------------+
```

通过允许多个子字体共享庞大的 `glyf`、`loca` 与 `CFF` 轮廓表，仅在 `name`、`OS/2` 与 `cmap` 表上保留独立差异，TTC 技术使得数万字的 Windows 汉字字库体积骤降了 60% 以上！

---

## D.4 TrueType、OpenType 与 AAT 数据表全景拓扑速查

在 SFNT 体系中，数据表的分类与归属极其严谨：

| 表分类 | 4 字节标签 (Tag) | 作用与排版使命 | 必选/可选 | 所属体系 |
| :--- | :--- | :--- | :--- | :--- |
| **必需核心表** | `cmap` | 字符编码码点到字形编号 GID 映射表 | 必需 | TrueType / OpenType |
| | `head` | 字体全局头表（设计分辨率、BBox、校验平衡） | 必需 | TrueType / OpenType |
| | `hhea` | 水平度量头表（排版升部、降部、行间距） | 必需 | TrueType / OpenType |
| | `hmtx` | 水平度量字宽与左侧轴承表 | 必需 | TrueType / OpenType |
| | `maxp` | 最大资源配置表（内存堆栈、点数上限宣告） | 必需 | TrueType / OpenType |
| | `name` | 多语言版权、家族名、子样式命名表 | 必需 | TrueType / OpenType |
| | `OS/2` | 跨平台操作系统兼容度量表（Win/Typo 度量） | 必需 | Windows / OpenType |
| | `post` | PostScript 打印机驱动与字形名称表 | 必需 | TrueType / OpenType |
| **轮廓几何表** | `glyf` | TrueType 二次贝塞尔轮廓与微指令表 | TT 必需 | TrueType |
| | `loca` | 字形在 `glyf` 表中的起始偏移索引表 | TT 必需 | TrueType |
| | `CFF ` | PostScript Type 2 / CFF 三次贝塞尔轮廓表 | OTF 必需 | OpenType (CFF) |
| **微指令支持表** | `cvt ` | 控制值表（Control Value Table，像素标准间距） | 可选 | TrueType Hinting |
| | `fpgm` | 字体级程序（全局宏函数定义表） | 可选 | TrueType Hinting |
| | `prep` | 渲染预处理程序（随分辨率执行一次） | 可选 | TrueType Hinting |
| | `gasp` | 网格自适应与 ClearType 平滑模式选择表 | 可选 | TrueType |
| **OpenType 布局表** | `GSUB` | 字形替换表（合字、上下文变体、垂直替换） | 复杂脚本必需 | OpenType Layout |
| | `GPOS` | 字形几何定位表（字距微调、元音标音吸附） | 复杂脚本必需 | OpenType Layout |
| | `GDEF` | 字形分类与附着锚点定义表 | 可选 | OpenType Layout |
| | `BASE` | 多文字基准线对齐表（拉丁/汉字/印度中轴） | 可选 | OpenType Layout |
| | `JSTF` | 复杂草书（阿拉伯文）对齐延伸微调表 | 可选 | OpenType Layout |
| **AAT 扩展表** | `morx` | 扩展字形变态表（有限状态机驱动变形） | AAT 核心 | Apple AAT |
| | `kerx` | 扩展字距微调表（状态机级上下文微调） | AAT 必需 | Apple AAT |
| | `feat` | 排版特性与选择器多语言描述表 | AAT 必需 | Apple AAT |
| | `trak` | 字号跟踪拉伸度量表 | 可选 | Apple AAT |
| | `opbd` | 视觉边缘对齐表（挂起标点） | 可选 | Apple AAT |
| | `bsln` | 苹果原生基准线对齐表 | 可选 | Apple AAT |
| | `lcar` | 合字光标分割线表 | 可选 | Apple AAT |

---

## D.5 TrueType 核心内核表深度解构

### 1. `head`（字体全局头表）
`head` 是操作系统在装载字库时首个读取的元数据表。其固定长度为 54 字节：

```xml
<!-- TTX XML 表达范例 -->
<head>
  <tableVersion value="1.0"/>
  <fontRevision value="1.002"/>
  <checkSumAdjustment value="0x12345678"/>
  <magicNumber value="0x5f0f3cf5"/>
  <flags value="00000000 00001011"/>
  <unitsPerEm value="2048"/>
  <created value="Sun Dec 12 10:00:00 2004"/>
  <modified value="Mon Jan 15 14:30:00 2007"/>
  <xMin value="-350"/>
  <yMin value="-480"/>
  <xMax value="2120"/>
  <yMax value="1950"/>
  <macStyle value="00000000 00000000"/>
  <lowestRecPPEM value="9"/>
  <fontDirectionHint value="2"/>
  <indexToLocFormat value="1"/>
  <glyphDataFormat value="0"/>
</head>
```

#### 关键字段物理语义：
* **`magicNumber`**：恒等于十六进制 `0x5F0F3CF5`。如果该字段不匹配，操作系统字体装载器将立即判定文件损坏并拒绝加载；
* **`unitsPerEm`**：字体设计网格分辨率。TrueType 规范强烈建议将其设置为 2 的幂次方（如 1024, 2048, 4096），以便光栅化底层在做定点数除法时能够直接退化为极速的硬件位移运算（Bit Shift）；
* **`indexToLocFormat`**：**决定 `loca` 表指针宽度的核心开关**！
  * 为 0（Short format）：`loca` 表条目为 16 位无符号整数（`uint16`），实际在 `glyf` 表中的字节偏移量等于存储值乘以 2（最多寻址 128KB）；
  * 为 1（Long format）：`loca` 表条目为 32 位无符号整数（`uint32`），直接存储字节偏移量（支持高达 4GB 的超大型字库）。

---

### 2. `hhea` 与 `hmtx`（水平排印度量体系）
水平度量由头表 `hhea`（36 字节）与连续数组表 `hmtx` 协同完成：

```xml
<hhea>
  <tableVersion value="0x00010000"/>
  <ascent value="1900"/>
  <descent value="-500"/>
  <lineGap value="200"/>
  <advanceWidthMax value="2400"/>
  <minLeftSideBearing value="-120"/>
  <minRightSideBearing value="-80"/>
  <xMaxExtent value="2350"/>
  <caretSlopeRise value="1"/>
  <caretSlopeRun value="0"/>
  <caretOffset value="0"/>
  <reserved0 value="0"/>
  <reserved1 value="0"/>
  <reserved2 value="0"/>
  <reserved3 value="0"/>
  <metricDataFormat value="0"/>
  <numberOfHMetrics value="256"/>
</hhea>
```

#### `hmtx` 表的高效压缩策略：
在包含等宽后缀字符（如全角标点、表格数字、汉字）的字体中，大量字符拥有完全相同的水平前进字宽（`advanceWidth`）。TrueType 引入了 `numberOfHMetrics` 分割线机制：
* 前 `numberOfHMetrics` 个字符，每个条目分配 4 字节：`uint16 advanceWidth` + `int16 lsb`；
* 后续从 `numberOfHMetrics` 到 `numGlyphs - 1` 的所有字符，其前进字宽被强制认定为**与第 `numberOfHMetrics - 1` 号字符完全相同**！每个条目仅需存储 2 字节的 `int16 lsb`，数据体积瞬间减半！

---

### 3. `maxp`（最大资源配置表）
`maxp` 表向光栅化解释器预先宣告字库内部所需的计算内存上限：
* **Version 0.5（CFF OpenType 使用）**：仅包含 `uint32 version` 与 `uint16 numGlyphs`（6 字节）；
* **Version 1.0（TrueType 使用）**：包含整整 14 项极其苛刻的微指令硬件资源上限：
  * `maxPoints`：单个简单字形所包含的最大控制点总数（含轮廓点与幻影点）；
  * `maxContours`：单个简单字形的最大封闭轮廓线条数；
  * `maxCompositePoints` / `maxCompositeContours`：复合字形嵌套展开后的极限点数与轮廓数；
  * `maxZones`：虚拟机寻址区域总数（通常为 2：Zone 0 黄昏区与 Zone 1 字形区）；
  * `maxTwilightPoints`：黄昏区分配的最大临时几何锚点数；
  * `maxStorage`：Storage 暂存区寄存器最大可用槽位数；
  * `maxFunctionDefs`：在 `fpgm` 中通过 `FDEF` 声明的最大全局函数总数；
  * `maxInstructionDefs`：通过 `IDEF` 重载或定义的最大用户指令总数；
  * `maxStackElements`：操作数栈（Operand Stack）的最大深度深度（防止栈溢出）；
  * `maxSizeOfInstructions`：任一单字形所允许包含的最大字节码总长度；
  * `maxComponentElements`：复合字形第一层直接引用的最大构件个数；
  * `maxComponentDepth`：复合字形递归嵌套的最大树深度（防止循环引用死锁）。

---

### 4. `OS/2`（操作系统跨平台度量表）
由微软与 IBM 联合制定的重量级系统集成表：

```xml
<OS_2>
  <version value="4"/>
  <xAvgCharWidth value="1050"/>
  <usWeightClass value="400"/>
  <usWidthClass value="5"/>
  <fsType value="00000000 00000000"/>
  <ySubscriptXSize value="1331"/>
  <ySubscriptYSize value="1228"/>
  <ySubscriptXOffset value="0"/>
  <ySubscriptYOffset value="286"/>
  <ySuperscriptXSize value="1331"/>
  <ySuperscriptYSize value="1228"/>
  <ySuperscriptXOffset value="0"/>
  <ySuperscriptYOffset value="983"/>
  <yStrikeoutSize value="102"/>
  <yStrikeoutPosition value="530"/>
  <sFamilyClass value="257"/>
  <panose>
    <bFamilyType value="2"/>
    <bSerifStyle value="11"/>
    <bWeight value="5"/>
    <bProportion value="3"/>
    <bContrast value="4"/>
    <bStrokeVariation value="3"/>
    <bArmStyle value="2"/>
    <bLetterForm value="2"/>
    <bMidline value="4"/>
    <bXHeight value="4"/>
  </panose>
  <ulUnicodeRange1 value="10000000 00000000 00000000 00000001"/>
  <ulUnicodeRange2 value="00010000 00000000 00000000 00000000"/>
  <ulUnicodeRange3 value="00000000 00000000 00000000 00000000"/>
  <ulUnicodeRange4 value="00000000 00000000 00000000 00000000"/>
  <achVendID value="MSFT"/>
  <fsSelection value="00000000 01000000"/>
  <usFirstCharIndex value="32"/>
  <usLastCharIndex value="65535"/>
  <sTypoAscender value="1490"/>
  <sTypoDescender value="-431"/>
  <sTypoLineGap value="307"/>
  <usWinAscent value="1900"/>
  <usWinDescent value="500"/>
  <ulCodePageRange1 value="00000000 00000000 00000000 00000001"/>
  <ulCodePageRange2 value="00000000 00000000 00000000 00000000"/>
  <sxHeight value="1082"/>
  <sCapHeight value="1456"/>
  <usDefaultChar value="0"/>
  <usBreakChar value="32"/>
  <usMaxContext value="3"/>
</OS_2>
```

#### Windows 与专业排版度量线的冲突与融合：
在现代排印史上，`OS/2` 表中最著名的设计冲突发生在 **Windows GDI 裁剪线** 与 **Typographic 排版行距** 之间：
* **`usWinAscent` 与 `usWinDescent`**：Windows GDI 引擎强制将文本渲染区域严格裁剪在这两条线之间。若字形轮廓（如带重音的大写字母 `Å`, `Ŵ` 或艺术衬线花体）在垂直方向稍微探出 `usWinAscent`，Windows 会在屏幕上将其**直接以像素硬截断**（产生丑陋的削顶现象）！因此字体工程师通常将这两条线拉得极开，以包含全字体极限包围盒；
* **`sTypoAscender`, `sTypoDescender` 与 `sTypoLineGap`**：专业排版软件（如 Adobe InDesign、QuarkXPress 与 LaTeX）遵循正统排版法则，两行连续基线之间的物理行间距严格计算为：
  $$\text{LineSpace} = \text{sTypoAscender} - \text{sTypoDescender} + \text{sTypoLineGap}$$
  若设置不当，会导致 Windows 下与 Mac 下同一文档渲染出完全不同的断行与分页位置！OpenType 规范后续引入了 `fsSelection` 的 Bit 7（`USE_TYPO_METRICS`），指示现代操作系统强制采用 Typo 系列数值作为系统默认行高，彻底平息了长达数十年的跨平台行距灾难。

---

### 5. `cmap`（字符码点到字形 GID 映射表）
操作系统在拿到文本字符串后，首先访问 `cmap` 表检索每个字符对应的字形编号（GID）：

::: tip cmap Format 4 分段连续二分查找算法拓扑（Figure D-3, D-4）
![cmap Format 4 拓扑（Figure D-3）](/images/fonts-encodings/fig-app-d3.png)
*cmap Format 4 拓扑（Figure D-3）*
:::

*图 D-3：cmap Format 4 的分段压缩结构。将 16 位 Unicode 码点划分为多个不相交的连续区间 `[startCode, endCode]`。*

::: tip cmap Format 12 32 位全量扩展表（Figure D-4）
![cmap Format 12 拓扑（Figure D-4）](/images/fonts-encodings/fig-app-d4.png)
*cmap Format 12 拓扑（Figure D-4）*
:::

*图 D-4：针对超大字符集（Emoji、古籍汉字、甲骨文）的 32 位 UCS-4 映射表 Format 12。*

#### Format 4 的二分检索与指针偏移寻址伪代码：
```c
uint16 lookup_gid_format4(uint16 char_code, CmapFormat4* cmap) {
    uint16 segCount = cmap->segCountX2 / 2;
    int left = 0, right = segCount - 1, hit = -1;
    
    /* 二分查找命中的连续段 */
    while (left <= right) {
        int mid = (left + right) / 2;
        if (cmap->endCode[mid] >= char_code) {
            hit = mid;
            right = mid - 1; /* 继续向前探寻最小可能段 */
        } else {
            left = mid + 1;
        }
    }
    
    if (hit == -1 || cmap->startCode[hit] > char_code) {
        return 0; /* 字符不在任何合法段内，返回缺失字形 GID 0 (.notdef) */
    }
    
    /* 核心寻址逻辑 */
    if (cmap->idRangeOffset[hit] == 0) {
        return (char_code + cmap->idDelta[hit]) & 0xFFFF;
    } else {
        /* 基于指针偏移计算在 glyphIdArray 中的位置 */
        uint16* offset_addr = &cmap->idRangeOffset[hit];
        uint16* target_ptr = offset_addr + (cmap->idRangeOffset[hit] / 2) + (char_code - cmap->startCode[hit]);
        uint16 gid = *target_ptr;
        if (gid != 0) {
            gid = (gid + cmap->idDelta[hit]) & 0xFFFF;
        }
        return gid;
    }
}
```

---

### 6. `loca` 与 `glyf`（轮廓几何与微指令）
`loca` 表是一个纯粹的偏移量数组：`offset[numGlyphs + 1]`。若某个字符（如空格字符）的起始偏移等于下一个字符的起始偏移（`offset[i] == offset[i+1]`），说明该字符为**无轮廓字形**，仅具备前进宽度而不占用任何绘图几何内存。

::: tip TrueType 轮廓点阵与二次贝塞尔曲线 On/Off 节点（Figure D-5, D-6）
![TrueType 曲线解构（Figure D-5）](/images/fonts-encodings/fig-app-d5.png)
*TrueType 曲线解构（Figure D-5）*
:::

*图 D-5：TrueType 二次贝塞尔曲线的节点拓扑。实心点为在线控制点（On-curve），空心点为脱线控制点（Off-curve）。连续两个脱线控制点之间，引擎自动在其中点虚构一个隐藏的在线点！*

::: tip glyf 表标志位流（Flags）与差分坐标解包（Figure D-6）
![glyf 标志位流（Figure D-6）](/images/fonts-encodings/fig-app-d6.png)
*glyf 标志位流（Figure D-6）*
:::

*图 D-6：TrueType 坐标流的无损差分压缩：每一个控制点存储的不是绝对坐标，而是相对于前一个点的增量 $\Delta x, \Delta y$。*

::: tip 复合字形矩阵变换与锚点吸附（Figure D-7, D-8）
![复合字形变换矩阵（Figure D-7）](/images/fonts-encodings/fig-app-d7.png)
*复合字形变换矩阵（Figure D-7）*
:::

*图 D-7：复合字形通过 $2 \times 2$ 仿射变换矩阵对引用的子字形进行旋转、缩放与倾斜。*

::: tip 复合字形嵌套与深层组件树（Figure D-8）
![复合字形嵌套树（Figure D-8）](/images/fonts-encodings/fig-app-d8.png)
*复合字形嵌套树（Figure D-8）*
:::

*图 D-8：字形部件允许深层递归嵌套（最多由 `maxComponentDepth` 限制），极大地节约了中日韩多字重字库的存储体积。*

---

### 7. `name` 表（全文字多语言命名与版权信息表）
`name` 表是字库的人事档案库。为了确保同一款字体能够在英语 Windows、繁体中文 Mac OS、日文 X11 等异构操作系统的字体选择菜单中正确显示出本地化名称，`name` 表定义了精密的多语言命名记录结构：

```xml
<!-- TTX XML 表达范例 -->
<name>
  <namerecord nameID="0" platformID="3" platEncID="1" langID="0x409">
    Copyright © 2007 Adobe Systems Incorporated. All Rights Reserved.
  </namerecord>
  <namerecord nameID="1" platformID="3" platEncID="1" langID="0x409">
    Adobe Garamond Pro
  </namerecord>
  <namerecord nameID="2" platformID="3" platEncID="1" langID="0x409">
    Regular
  </namerecord>
  <namerecord nameID="3" platformID="3" platEncID="1" langID="0x409">
    2.000;ADBE;AGaramondPro-Regular;ADOBE
  </namerecord>
  <namerecord nameID="4" platformID="3" platEncID="1" langID="0x409">
    Adobe Garamond Pro Regular
  </namerecord>
  <namerecord nameID="6" platformID="3" platEncID="1" langID="0x409">
    AGaramondPro-Regular
  </namerecord>
</name>
```

#### 关键标准 NameID 权威词典：
* **NameID 0**：版权所有声明（Copyright Notice）；
* **NameID 1**：字体家族名（Font Family Name，如 "Adobe Garamond Pro"）；
* **NameID 2**：字体子样式名称（Font Subfamily Name，如 "Regular", "Bold", "Italic"）；
* **NameID 3**：全字库唯一标识字符串（Unique Font Identifier）；
* **NameID 4**：人机友好的全名字串（Full Font Name，通常为 Family + Subfamily）；
* **NameID 5**：版本号字符串（Version string，如 "Version 2.000;PS 002.000"）；
* **NameID 6**：PostScript 打印机驱动识别名（PostScript Name，**严禁包含空格与非 ASCII 字符**，激光打印机通过该名称在显存中精准挂接字库！）；
* **NameID 7**：注册商标声明（Trademark Notice）；
* **NameID 8**：字体制造商（Manufacturer Name）；
* **NameID 9**：字体设计师（Designer）；
* **NameID 11**：厂商官方网址 URL；
* **NameID 16**：排版首选家族名（Typographic Family Name，解决传统办公软件 4 字重限制的拓展家族名）；
* **NameID 17**：排版首选子样式名（Typographic Subfamily Name，支持 Thin, Light, Semibold, ExtraBold 等丰富层级）；
* **NameID 25**：OpenType 可变字体（Variable Fonts）的 PostScript 命名变化前缀。

---

### 8. `post` 表（PostScript 驱动与字形名称表）
`post` 表最初由苹果设计，用于向 PostScript 打印机转储必要的度量与字形名称：
* **Format 1.0**：恒定包含苹果 Macintosh 操作系统早期标准的 258 个拉丁字形名称（无需在字体中存储任何字符名称字符串，节约内存）；
* **Format 2.0**：最经典的 TrueType 字形命名格式！包含一个 16 位字符编号映射数组与一个连续 Pascal 字符串数组（每个字符串前带 1 字节长度），支持为数万个非标准字形赋予自定义的 ASCII 符号名称；
* **Format 3.0**：**零名称极简格式**！完全不存储任何字形名称字符串。当字体发布用于网页嵌入（Web Fonts / WOFF）或移动端系统固件时，通常采用 Format 3.0 以剥离所有无关字符串，削减数十千字节的文件开销。

```c
struct PostTableFormat2 {
    uint32 format;              /* 0x00020000 */
    int32  italicAngle;         /* 16.16 定点数倾斜角 */
    int16  underlinePosition;   /* 下划线基准线垂直偏移 */
    int16  underlineThickness;  /* 下划线宽度 */
    uint32 isFixedPitch;        /* 是否等宽 */
    uint32 minMemType42;        /* 激光照排机下载 Type 42 所需的最小内存 */
    uint32 maxMemType42;
    uint32 minMemType1;
    uint32 maxMemType1;
    uint16 numGlyphs;           /* 包含的字形总数 */
    uint16 glyphNameIndex[numGlyphs]; /* 指向标准 258 符号或后续自定义字符串的索引数组 */
    /* 紧随其后为 Pascal-string 连续数组: uint8 length + char data[length] */
};
```

---

### 9. `gasp` 表（网格自适应与抗锯齿平滑控制表）
`gasp`（Grid-fitting and Scan-conversion Procedure Table）是 Windows 操作系统在执行屏幕抗锯齿与 ClearType 亚像素渲染时极其关键的决策调度表。

它针对不同的屏幕显示每 Em 像素尺寸（PPEM），精细控制何时启用 TrueType 指令（Grid-fitting）、何时启用灰度平滑（Grayscale Smoothing）、以及何时启用 ClearType 对称平滑：

```xml
<gasp>
  <version value="1"/>
  <gaspRange rangeMaxPPEM="8" rangeGaspBehavior="2"/> <!-- 仅执行灰度平滑，关闭提示 -->
  <gaspRange rangeMaxPPEM="16" rangeGaspBehavior="1"/> <!-- 极小字号：强行开启网格提示对齐 -->
  <gaspRange rangeMaxPPEM="2048" rangeGaspBehavior="15"/> <!-- 正常与大字号：同时开启微指令、灰度与 ClearType 平滑 -->
  <gaspRange rangeMaxPPEM="65535" rangeGaspBehavior="14"/> <!-- 超大海报：关闭微指令，仅执行全平滑 -->
</gasp>
```

#### `rangeGaspBehavior` 四大标志位位域：
* **Bit 0 (`GASP_GRIDFIT`)**：在此分辨率下激活 TrueType 虚拟机执行轮廓对齐；
* **Bit 1 (`GASP_DOGRAY`)**：在此分辨率下启用标准单色灰度抗锯齿；
* **Bit 2 (`GASP_SYMMETRIC_SMOOTHING`)**：针对 ClearType 激活水平亚像素平滑；
* **Bit 3 (`GASP_SYMMETRIC_GRIDFIT`)**：激活 ClearType 对称网格对齐。

---

### 10. `vhea`、`vmtx` 与 `VORG`（垂直排版核心度量体系）
在中文、日文、韩文与传统蒙古文等东亚竖排排版中，字形并非沿着水平基线从左向右推进，而是**沿着垂直中轴线从上向下流动**！

OpenType 为此定义了完整的垂直度量表簇：
* **`vhea`（Vertical Header Table）**：
  * `vertTypoAscender` / `vertTypoDescender`：垂直排版升部与降部；
  * `vertTypoLineGap`：垂直行距；
  * `advanceHeightMax`：全字库最大垂直前进高度；
  * `minTopSideBearing` / `minBottomSideBearing`：全局最小顶部与底部轴承；
  * `numOfLongVerMetrics`：在 `vmtx` 中拥有独立垂直度量的字符数。
* **`vmtx`（Vertical Metrics Table）**：
  * 与 `hmtx` 完全同构，存储每个字符的 `advanceHeight`（垂直前进高，通常为一个全角 Em 高度）与 `topSideBearing`（顶部轴承，即基字顶部距前一字符绘制基线的间隙）；
* **`VORG`（Vertical Origin Table，垂直绘制原点表）**：
  * 在 CFF OpenType 中，由于三次贝塞尔曲线坐标系天然以左下角为设计原点，在垂直排版时需要将原点平移到字符顶部的几何中心。`VORG` 表通过一个紧凑的默认高度与特异字典，为每个字形直接宣告其在垂直排版时的绝对中心原点 Y 坐标（`vertOriginY`），使得排版引擎在进行竖排变换时无需重新解压和计算庞大的 `glyf` 轮廓包围盒！

---

## D.6 OpenType 布局与形态表（GSUB, GPOS, GDEF, BASE, JSTF）

OpenType 彻底超越传统点阵与静态矢量的核心，在于其将排印学提升为一门**上下文敏感的文法重写系统**。排版引擎在加载字库后，首先构建起全局布局查找拓扑：

$$\text{ScriptList} \longrightarrow \text{LangSysRecord} \longrightarrow \text{FeatureList} \longrightarrow \text{LookupList} \longrightarrow \text{SubTables}$$

```xml
<!-- OpenType 顶层布局结构拓扑 (TTX 范例) -->
<GSUB>
  <Version value="0x00010000"/>
  <ScriptList>
    <ScriptRecord index="0">
      <ScriptTag value="latn"/>
      <Script>
        <DefaultLangSys>
          <ReqFeatureIndex value="65535"/>
          <FeatureIndex index="0" value="0"/> <!-- 指向 'liga' -->
          <FeatureIndex index="1" value="1"/> <!-- 指向 'smcp' -->
          <FeatureIndex index="2" value="2"/> <!-- 指向 'cpsp' -->
        </DefaultLangSys>
      </Script>
    </ScriptRecord>
  </ScriptList>
  <FeatureList>
    <FeatureRecord index="0">
      <FeatureTag value="liga"/>
      <Feature>
        <LookupListIndex value="0"/>
      </Feature>
    </FeatureRecord>
    <FeatureRecord index="1">
      <FeatureTag value="smcp"/>
      <Feature>
        <LookupListIndex value="1"/>
      </Feature>
    </FeatureRecord>
  </FeatureList>
  <LookupList>
    <Lookup index="0">
      <LookupType value="4"/> <!-- Ligature Substitution -->
      <LookupFlag value="0"/>
      <!-- 具体子表 -->
    </Lookup>
    <Lookup index="1">
      <LookupType value="1"/> <!-- Single Substitution -->
      <LookupFlag value="0"/>
    </Lookup>
  </LookupList>
</GSUB>
```

---

### 1. 基础构件：Coverage 表与 ClassDef 表
在所有 GSUB 与 GPOS 子表中，两个最基础的筛选构件是 **Coverage 表** 与 **ClassDef 表**：

#### Coverage 表（覆盖字形集合）：
用于快速裁决当前字形是否属于本子表的受控目标，并将 GID 转换为致密的从 0 开始的覆盖索引（Coverage Index）：
* **Format 1（离散字形数组）**：
  ```c
  struct CoverageFormat1 {
      uint16 coverageFormat; /* 恒为 1 */
      uint16 glyphCount;     /* 受控字形总数 */
      uint16 glyphArray[glyphCount]; /* 严格按 GID 字典序升序排列 */
  };
  ```
* **Format 2（连续区间数组）**：
  ```c
  struct CoverageRangeRecord {
      uint16 startGlyphID;   /* 连续区间起始 GID */
      uint16 endGlyphID;     /* 连续区间结束 GID */
      uint16 startCoverageIndex; /* 该区间首个字符分配的连续覆盖索引 */
  };
  struct CoverageFormat2 {
      uint16 coverageFormat; /* 恒为 2 */
      uint16 rangeCount;     /* 区间总数 */
      struct CoverageRangeRecord rangeRecords[rangeCount];
  };
  ```

#### ClassDef 表（字形分类定义表）：
将成百上千个字形划分为若干个等价类（Class ID: 0 到 65535），极大地压缩上下文匹配规则矩阵：
* **Format 1**：指定 `startGlyphID` 与连续数组 `classValueArray`；
* **Format 2**：通过 `ClassRangeRecord` 将连续区间指定为特定的类编号。

---

### 2. `GSUB` 表内部 8 大查找子表规范与 TTX 源码全景

#### Type 1：单字替换（Single Substitution）
* **Format 1（固定增量）**：将输入字形的 GID 加上固定标量 `DeltaGlyphID`；
* **Format 2（一一映射查找表）**：
  ```xml
  <Lookup index="1">
    <LookupType value="1"/>
    <LookupFlag value="0"/>
    <SingleSubst index="0" Format="2">
      <Substitution in="a" out="a.sc"/>
      <Substitution in="b" out="b.sc"/>
      <Substitution in="c" out="c.sc"/>
      <Substitution in="d" out="d.sc"/>
    </SingleSubst>
  </LookupList>
  ```

#### Type 2：多字分解（Multiple Substitution）
将单个输入字形在排版流中原地解构为一个连续的字形序列：
```xml
<Lookup index="2">
  <LookupType value="2"/>
  <LookupFlag value="0"/>
  <MultipleSubst index="0" Format="1">
    <!-- 将连字符 'ffi' 还原分解为独立的三个字形 -->
    <Sequence glyph="f_f_i">
      <Substitute value="f"/>
      <Substitute value="f"/>
      <Substitute value="i"/>
    </Sequence>
  </MultipleSubst>
</Lookup>
```

#### Type 3：备选替换（Alternate Substitution）
为单个字符提供一组等价的美学候选变体，供排版师在交互式菜单中按需挑选：
```xml
<Lookup index="3">
  <LookupType value="3"/>
  <LookupFlag value="0"/>
  <AlternateSubst index="0" Format="1">
    <AlternateSet glyph="ampersand">
      <Alternate glyph="ampersand.italic"/>
      <Alternate glyph="ampersand.swash1"/>
      <Alternate glyph="ampersand.swash2"/>
    </AlternateSet>
  </AlternateSubst>
</Lookup>
```

#### Type 4：合字替换（Ligature Substitution）
包含按首字母聚合的 `LigatureSet` 数组，内部包含各连字组件与生成的目标合字：
```xml
<Lookup index="0">
  <LookupType value="4"/>
  <LookupFlag value="0"/>
  <LigatureSubst index="0" Format="1">
    <LigatureSet glyph="f">
      <!-- 遇到 'f' + 'i' 触发替换为 'fi' (GID 280) -->
      <Ligature components="i" glyph="f_i"/>
      <!-- 遇到 'f' + 'l' 触发替换为 'fl' (GID 281) -->
      <Ligature components="l" glyph="f_l"/>
      <!-- 遇到 'f' + 'f' + 'i' 触发替换为 'ffi' -->
      <Ligature components="f,i" glyph="f_f_i"/>
    </LigatureSet>
  </LigatureSubst>
</Lookup>
```

#### Type 5 与 Type 6：上下文与链式上下文替换（Contextual & Chained Contextual）
Type 6 是 OpenType 文法重写的顶峰。它维护 Backtrack、Input、Lookahead 三重滑动窗口：
```xml
<Lookup index="6">
  <LookupType value="6"/>
  <LookupFlag value="0"/>
  <ChainContextSubst index="0" Format="3">
    <!-- 回溯序列：前面必须有大写字母 -->
    <BacktrackCoverage index="0" Format="1">
      <Glyph value="A"/>
      <Glyph value="E"/>
    </BacktrackCoverage>
    <!-- 输入序列：当前字符小写 'e' -->
    <InputCoverage index="0" Format="1">
      <Glyph value="e"/>
    </InputCoverage>
    <!-- 前瞻序列：后面必须跟随字母 'r' -->
    <LookaheadCoverage index="0" Format="1">
      <Glyph value="r"/>
    </LookaheadCoverage>
    <!-- 动作：在当前输入位置 0 处，调用 Lookup 1 (小型大写替换) -->
    <SubstLookupRecord index="0">
      <SequenceIndex value="0"/>
      <LookupListIndex value="1"/>
    </SubstLookupRecord>
  </ChainContextSubst>
</Lookup>
```

#### Type 7 与 Type 8：
* **Type 7（Extension Substitution）**：打破 16 位 64KB 内部相对偏移限制的 32 位跳转包装器；
* **Type 8（Reverse Chaining Contextual Single）**：专为乌尔都文纳斯塔里克体（Nastaliq）量身定制，排版引擎从后向前逆序求值，确保向下倾斜的级联词尾字符能够正确变形。

---

### 3. `GPOS` 表内部 9 大几何定位子表与 TTX 源码全景

`GPOS` 不修改字形代码，而是通过对字形施加二维矢量偏移与前进宽度修正，完成毫秒级空间装配：

#### Type 1：单字定位调整（Single Adjustment）
```xml
<Lookup index="7">
  <LookupType value="1"/>
  <LookupFlag value="0"/>
  <SinglePos index="0" Format="1">
    <Coverage Format="1">
      <Glyph value="hyphen"/>
      <Glyph value="endash"/>
    </Coverage>
    <!-- 将连字符向上抬高 120 栅格单位以匹配大写字母中心 -->
    <Value YPlacement="120"/>
  </SinglePos>
</Lookup>
```

#### Type 2：基于类的字偶距微调（Class-based PairPos）
```xml
<Lookup index="8">
  <LookupType value="2"/>
  <LookupFlag value="8"/> <!-- 忽略结合音标 -->
  <PairPos index="0" Format="2">
    <Coverage Format="1">
      <Glyph value="T"/>
      <Glyph value="V"/>
      <Glyph value="W"/>
    </Coverage>
    <ClassDef1 Format="1">
      <ClassDefinition glyph="T" class="1"/>
      <ClassDefinition glyph="V" class="2"/>
      <ClassDefinition glyph="W" class="2"/>
    </ClassDef1>
    <ClassDef2 Format="1">
      <ClassDefinition glyph="o" class="1"/>
      <ClassDefinition glyph="c" class="1"/>
      <ClassDefinition glyph="e" class="1"/>
      <ClassDefinition glyph="a" class="2"/>
    </ClassDef2>
    <!-- 类别 1 (T) 与 类别 1 (o, c, e) 相遇时的字距调整 -->
    <Class1Record index="1">
      <Class2Record index="1">
        <Value1 XAdvance="-180"/>
      </Class2Record>
      <!-- 类别 1 (T) 与 类别 2 (a) 相遇时微调 -150 -->
      <Class2Record index="2">
        <Value1 XAdvance="-150"/>
      </Class2Record>
    </Class1Record>
  </PairPos>
</Lookup>
```

#### Type 3：草书连贯吸附（Cursive Attachment）
```xml
<Lookup index="9">
  <LookupType value="3"/>
  <LookupFlag value="1"/> <!-- 从右向左排版 -->
  <CursivePos index="0" Format="1">
    <Coverage Format="1">
      <Glyph value="ar_baa.init"/>
      <Glyph value="ar_noon.medi"/>
    </Coverage>
    <EntryExitRecord index="0">
      <EntryAnchor Format="1">
        <XCoordinate value="0"/>
        <YCoordinate value="150"/>
      </EntryAnchor>
      <ExitAnchor Format="1">
        <XCoordinate value="600"/>
        <YCoordinate value="100"/>
      </ExitAnchor>
    </EntryExitRecord>
  </CursivePos>
</Lookup>
```

#### Type 4：基字标音吸附（MarkToBase Attachment）
定义字母主干上的固定锚点与音标符号上的对齐锚点：
```xml
<Lookup index="10">
  <LookupType value="4"/>
  <LookupFlag value="0"/>
  <MarkBasePos index="0" Format="1">
    <MarkCoverage Format="1">
      <Glyph value="acute"/>
      <Glyph value="grave"/>
    </MarkCoverage>
    <BaseCoverage Format="1">
      <Glyph value="a"/>
      <Glyph value="e"/>
      <Glyph value="o"/>
    </BaseCoverage>
    <BaseArray>
      <BaseRecord index="0">
        <!-- 字母 'a' 顶部的对齐中心锚点 -->
        <BaseAnchor index="0" Format="1">
          <XCoordinate value="260"/>
          <YCoordinate value="680"/>
        </BaseAnchor>
      </BaseRecord>
    </BaseArray>
    <MarkArray>
      <MarkRecord index="0">
        <Class value="0"/>
        <MarkAnchor Format="1">
          <XCoordinate value="0"/>
          <YCoordinate value="0"/>
        </MarkAnchor>
      </MarkRecord>
    </MarkArray>
  </MarkBasePos>
</Lookup>
```

---

### 4. `GDEF`、`BASE` 与 `JSTF` 表深度解构

* **`GDEF`（字形全局属性定义表）**：
  * `GlyphClassDef`：将全字库字形划分为四种神圣类型：
    1. **Base Glyph（单字基字）**：常规文本字符；
    2. **Ligature Glyph（合字字符）**：由多字拼接而成的连字；
    3. **Mark Glyph（结合附着符号）**：无前进宽度的变音符或声调符号；
    4. **Component Glyph（组件字符）**：不可单独显示的内部拼装部件。
  * `AttachList`：在轮廓上显式标明可用于几何组装的锚点编号；
  * `LigCaretList`：定义多字符合字（如 'ffi'）内部的文本光标闪烁分界线（Caret Positions）；
* **`BASE`（跨文字基准线对齐表）**：
  * 在同一段落中混合排版西文拉丁字母、汉字方块字、藏文与印度天城体时，各种文字的历史基准参考线完全不同。`BASE` 表统一定义了 `romn`（罗马基线）、`ideo`（汉字底部基线）、`idcm`（汉字正中轴线）以及 `math`（数学公式中轴），排版引擎依据各文字的基线偏差矩阵自动平移字身，实现跨语系视觉平齐；
* **`JSTF`（两端对齐与段落调整表）**：
  * 专为阿拉伯文等复杂书写系统设计。当需要对段落执行两端对齐（Justification）时，`JSTF` 定义了多级优先级的微调动作：第一级拉长笔画横梁（Kashida 填充）；第二级调用更宽的备选字形；第三级微调字距；第四级允许空格适度拉伸，再现了传统手抄本时代的极致排印美感。

---

## D.7 Apple Advanced Typography（AAT）高级扩展表体系

在苹果公司与微软分别主导字型技术演进的时期，苹果在 macOS（自 Mac OS X 10.0 引入）与 iOS 底层坚持并完善了源自 TrueType GX 的 **AAT（Apple Advanced Typography）** 体系。

与 OpenType 基于静态查找表（Lookups）与多轮模式匹配（Pattern Matching）不同，**AAT 的底层核心是图灵完备的“有限状态自动机（Finite State Machines / State Tables）”！**

::: tip AAT morx 变态表与 kerx 扩展字距表拓扑（Figure D-9, D-10）
![AAT morx 表拓扑（Figure D-9）](/images/fonts-encodings/fig-app-d9.png)
*AAT morx 表拓扑（Figure D-9）*
:::

*图 D-9：AAT `morx`（Extended Glyph Metamorphosis Table）内部由链表链条（Chains）构成，每个链条包含独立的特性掩码与状态机子表。*

::: tip AAT trak 跟踪排印与字间距动态补偿（Figure D-10）
![AAT trak 跟踪表（Figure D-10）](/images/fonts-encodings/fig-app-d10.png)
*AAT trak 跟踪表（Figure D-10）*
:::

*图 D-10：AAT `trak`（Tracking Table）结构。针对不同显示磅数（Point Sizes）定义字间距自动扩展与收缩曲线。*

---

### 1. AAT 扩展状态机（Extended State Table）的代数结构

一个标准的 AAT 状态机子表在二进制内存中由四大连续组件构成：
1. **Header（状态机头）**：记录状态总数、类总数、以及到后续三张表的相对字节偏移量；
2. **ClassTable（字形到类别映射表）**：将输入的 GID 映射为一个 16 位整数类别（Class ID）；
3. **StateArray（二维状态跃迁转移矩阵）**：一个行数为状态数、列数为类别数的稠密二维数组。给定当前状态 $S$ 与输入类别 $C$，查得转移条目索引：
   $$\text{EntryIndex} = \text{StateArray}[S][C]$$
4. **EntryTable（动作条目数组）**：每一个条目占用 4 字节，编码了三大核心排版动作：
   * `newState`：状态机转移到的下一个目标状态；
   * `flags`：执行动作标志位（指示是否将当前字形压入内部回溯硬件栈、是否标记当前位置、是否向前推进画笔）；
   * `actionIndex`：指向字形替换数组或字距微调数组的操作索引。

```
+-------------------------------------------------------+
|  AAT 状态机执行流 (State Machine Execution Pipeline)   |
+-------------------------------------------------------+
|  Input Glyph GID                                      |
|       │                                               |
|       ▼                                               |
|  [ ClassTable ] ──> Class ID (C)                      |
|                           │                           |
|  Current State (S) ───────┼───> [ StateArray[S][C] ]  |
|                                         │             |
|                                         ▼             |
|                                 [ EntryTable ]        |
|                                 ├── Next State (S')   |
|                                 ├── Push/Pop Stack    |
|                                 └── Action (Subst/Kern)
+-------------------------------------------------------+
```

由于状态机在处理连续文本时**仅需向前线性扫描一次（$O(N)$ 单趟时间复杂度）**，AAT 在处理极为繁复的南亚印度系文字（如天城体、泰米尔体、高棉体）与阿拉伯文时，其排版性能与抗死锁能力在历史上长期碾压早期未经硬件优化的 OpenType 引擎！

---

### 2. `morx` 表（扩展字形变态表）的五大子表形态

`morx`（Extended Glyph Metamorphosis）是 AAT 排版体系的心脏。它划分为五种专有子表类型：
1. **Type 0（Rearrangement Subtable / 字形重排状态机）**：
   * 专为印度系文字设计。在印地语中，某些短元音在逻辑字符编码上书写在辅音之后，但视觉呈现上必须被“抛掷”到辅音甚至整个辅音连缀的前方！Type 0 状态机包含一个最多容纳 4 个字符的微型硬件回溯栈，支持从栈中任意重排字符的物理绘制次序；
2. **Type 1（Contextual Glyph Substitution / 上下文替换状态机）**：
   * 在状态转移的同时，根据 `actionIndex` 查表对当前标记的字形进行一对一或基于类的变体替换；
3. **Type 2（Ligature Substitution / 状态机连字替换）**：
   * 支持任意跨度、任意复杂度的多字合字。状态机在扫描连字组件时将它们依次推入内部栈，在遇到连字闭合字符时，一次性将栈中所有组件弹出并整体替换为最终目标合字；
4. **Type 4（Non-contextual Substitution / 非上下文单字替换）**：
   * 无状态机开销，通过单一查找表执行全局单字变体替换；
5. **Type 5（Glyph Insertion / 动态字形插入状态机）**：
   * 允许状态机在当前文本流中凭空插入一个或多个崭新的字形（例如插入方向控制符号、连字符或装饰衬花），而无需上层应用程序修改原始 Unicode 文本缓冲区。

---

### 3. `kerx` 表（扩展字距微调表）

AAT 的 `kerx` 表是对传统 TrueType `kern` 表的革命性升级：
* **Format 0（简单有序字偶对）**：经典 $(Left, Right) \to \text{Value}$ 二分查找数组；
* **Format 1（状态机驱动的上下文多字符微调）**：能够在跨越多个中间字符的复杂语境下，同时对多达 8 个暂存字符施加高精度的相对二维坐标微调！
* **Format 2（基于类的字距矩阵）**：利用稠密矩阵执行全字库大面积字距补偿；
* **Format 4（跨流字距微调 Cross-Stream Kerning）**：**在垂直于文本流动方向的轴线上施加位移**！例如在阿拉伯文草书排版中，当某个字符向下倾斜时，后续字符通过跨流字距在垂直 Y 轴上整体抬高，完美模拟出波斯体书法连绵起伏、层层叠叠的瀑布式美感！

---

### 4. `feat` 表（排版特性多语言定义表）

与 OpenType 采用 4 字节 ASCII 缩写标签（如 `liga`, `smcp`）且未在字体内部定义本地化名称不同，AAT 的 `feat` 表将排版特性定义为两级数字代号：
* **`FeatureType`（特性类别）**：如 1 代表合字（Ligatures），3 代表备选字形（Alternate Pos），22 代表文字变体；
* **`SettingSelector`（设置选择器）**：如对于合字特性，选择器 0 为关闭所有合字，2 为启用标准合字，4 为启用历史连字；
* **多语言本地化支持**：每个特性与选择器直接绑定一个 `nameID`，在 `name` 表中存储英语、法语、中文、日语等原生字符串。使得 macOS 的“字体面板（Font Panel）”能够无需任何外部配置，原生为用户渲染出一个全本地化、支持勾选切换的高级排版功能交互式界面！

---

### 5. `trak`、`opbd`、`bsln` 与 `lcar` 表

* **`trak`（Tracking Table / 字距跟踪表）**：
  * 在传统金属活字排版中，大磅字号（如 72 磅海报标题）需要适度收紧字距，而极小字号（如 6 磅版权小字）必须大幅放宽字间距以保证辨识度。`trak` 表定义了由字体设计师绘制的字号-字距连续非线性补偿样条曲线，操作系统排版器根据当前渲染磅值动态求值并自动施加均匀的微米级字间距平移；
* **`opbd`（Optical Bounds / 视觉边缘对齐表）**：
  * 人眼的视觉心理物理学（Psychophysics）表明：当一段文字左侧包含左双引号 `“` 或小写字母 `o` 时，若将其物理包围盒与下方大写字母 `H` 机械对齐，视觉上会显得左侧凹陷不平。`opbd` 表为每个字符定义了左、上、右、下四个方向的**光学凸出量（Optical Offsets）**，使标点符号在段落边缘能够极其优美地“挂起”探出边框（Hanging Punctuation）；
* **`bsln`（Baseline Table / AAT 基线表）**：
  * 定义了多达 32 种不同文字系统的基线系统，并在同一字库内部存储各文字基线的相对垂直坐标与主控基线（Dominant Baseline）优先权；
* **`lcar`（Ligature Caret Table / 合字光标分割线表）**：
  * 当文本光标在合字（如 'ffi'）内部移动时，`lcar` 为其定义了两个内部逻辑切分点（Caret Coordinates）。光标在合字中间闪烁时能够精确停留在 'f' 与 'i' 之间的虚拟空间，彻底解决了用户在编辑连字时无法定位内部字符的交互噩梦。

通过 SFNT 容器的弹性封装、TrueType 虚拟机的微观粒子控制、OpenType 布局引擎的图灵文法重写、以及 AAT 状态机的毫秒级流式处理，数字字体工程构建起了人类信息文明史上最为精密、优雅且深邃的排印技术巨塔。
---

## D.8 复杂书写系统（Complex Scripts）排版布局实战案例

为了彻底展示 OpenType 与 AAT 处理阿拉伯文、南亚印度系文字（Indic Scripts）以及东亚纵排文字的工业级能力，以下剖析三大高级排版实战结构：

### 1. 阿拉伯文四态上下文替换（Contextual Substitution GSUB Type 5）
在阿拉伯文字体中，每个字母具有四种截然不同的书写形态：
* **孤立态（Isolated）**：字符前后均未连笔；
* **词首态（Initial）**：仅与后一字符连笔；
* **词中态（Medial）**：前后均连笔；
* **词尾态（Final）**：仅与前一字符连笔。

OpenType 引擎首先通过 `init`、`medi`、`fina`、`isol` 四个排版特性，使用 GSUB Type 5（基于类的上下文替换）进行状态匹配：

```xml
<Lookup index="15">
  <LookupType value="5"/> <!-- Contextual Substitution -->
  <LookupFlag value="1"/> <!-- RightToLeft -->
  <ContextSubst index="0" Format="2">
    <!-- 覆盖所有具有连笔能力的阿拉伯文字母 -->
    <Coverage Format="1">
      <Glyph value="ar_baa"/>
      <Glyph value="ar_jeem"/>
      <Glyph value="ar_seen"/>
    </Coverage>
    <ClassDef Format="1">
      <ClassDefinition glyph="ar_baa" class="1"/>
      <ClassDefinition glyph="ar_jeem" class="1"/>
      <ClassDefinition glyph="space" class="2"/>
    </ClassDef>
    <!-- 当 Class 1 (字母) 后紧随 Class 1 (字母) 时，触发替换为词首态 -->
    <SubClassSet index="1">
      <SubClassRule index="0">
        <ClassSequence>
          <Class value="1"/>
        </ClassSequence>
        <SubstLookupRecord index="0">
          <SequenceIndex value="0"/>
          <LookupListIndex value="20"/> <!-- 词首态替换子表 -->
        </SubstLookupRecord>
      </SubClassRule>
    </SubClassSet>
  </ContextSubst>
</Lookup>
```

---

### 2. 多重音标堆叠与碰撞规避（Mark-to-Mark GPOS Type 6）
在阿拉伯文《古兰经》诵读记号或希伯来文圣经多重变音符中，字母上方往往需要垂直堆叠两到三个独立的读音与声调符号。若机械放置，符号必然重叠。

GPOS Type 6 构筑了音标之间的递归相对几何锚点：
```xml
<Lookup index="16">
  <LookupType value="6"/> <!-- MarkToMark Attachment -->
  <LookupFlag value="0"/>
  <MarkMarkPos index="0" Format="1">
    <!-- 顶层音标：开音符 (Fathah) -->
    <Mark1Coverage Format="1">
      <Glyph value="ar_fathah"/>
    </Mark1Coverage>
    <!-- 底层音标：鼻音化轻读符 (Tanwin) -->
    <Mark2Coverage Format="1">
      <Glyph value="ar_tanwin"/>
    </Mark2Coverage>
    <Mark2Array>
      <Mark2Record index="0">
        <!-- 在底层音标顶端定义向上的对接锚点 -->
        <Mark2Anchor index="0" Format="1">
          <XCoordinate value="0"/>
          <YCoordinate value="220"/>
        </Mark2Anchor>
      </Mark2Record>
    </Mark2Array>
    <Mark1Array>
      <Mark1Record index="0">
        <Class value="0"/>
        <Mark1Anchor Format="1">
          <XCoordinate value="0"/>
          <YCoordinate value="0"/>
        </Mark1Anchor>
      </Mark1Record>
    </Mark1Array>
  </MarkMarkPos>
</Lookup>
```

无论下层音标的位置因基字高度发生何种位移，上层音标通过实时锚点对齐，永远浮动在下层音标正上方 220 栅格单位处，彻底消除了文字重叠！

---

### 3. 合字光标分割线（`GDEF` Ligature Caret List）
当用户使用光标键在一个连字合字（如 'ffi'）内部穿行时，文字处理软件查询 `GDEF` 表的 `LigCaretList`：

```xml
<GDEF>
  <Version value="0x00010002"/>
  <LigCaretList>
    <Coverage Format="1">
      <Glyph value="f_f_i"/>
    </Coverage>
    <LigGlyph index="0">
      <!-- 'f' 与第二个 'f' 之间的光标闪烁 X 坐标 -->
      <CaretValue index="0" Format="1">
        <Coordinate value="320"/>
      </CaretValue>
      <!-- 第二个 'f' 与 'i' 之间的光标闪烁 X 坐标 -->
      <CaretValue index="1" Format="1">
        <Coordinate value="650"/>
      </CaretValue>
    </LigGlyph>
  </LigCaretList>
</GDEF>
```

软件依据这些坐标，在屏幕上绘制闪烁的垂直光标，并在用户按下退格键（Backspace）时，精准将合字拆解还原，提供毫无破绽的原生多字符编辑体验。
---

## D.9 AAT 有限状态自动机状态跃迁矩阵实战推导

为了深刻理解 AAT `morx` 表内部状态转移的数学精髓，我们以印地语天城体（Devanagari）的短元音 'i'（Matra-I）前置重排状态机为例进行推导：

在天城体中，逻辑编码顺序为：$\text{辅音 (Consonant)} + \text{短元音 (Matra-I)}$，但在视觉排版中，短元音必须被“向前翻转”到辅音左侧！

### 状态转移代数模型：
* **状态集合**：$Q = \{ S_0: \text{StartOfLine}, \, S_1: \text{SawConsonant}, \, S_2: \text{SawVirama} \}$；
* **字符类别**：$\Sigma = \{ C_0: \text{Other}, \, C_1: \text{Consonant}, \, C_2: \text{Matra-I}, \, C_3: \text{Virama (死符)} \}$。

#### 跃迁矩阵与动作表（StateArray & EntryTable）：

| 当前状态 | 输入类别：$C_1$ (辅音) | 输入类别：$C_2$ (短元音 Matra-I) | 输入类别：$C_3$ (Virama 死符) | 输入类别：$C_0$ (其余字符) |
| :--- | :--- | :--- | :--- | :--- |
| **$S_0$ (起点)** | 转移到 $S_1$；**动作**：将辅音压栈 (Push) | 保持 $S_0$；无动作 | 保持 $S_0$；无动作 | 保持 $S_0$；推进画笔 |
| **$S_1$ (已见辅音)**| 保持 $S_1$；清空旧栈并压入新辅音 | **触发重排**！转移到 $S_0$；**动作**：从栈中弹出辅音，先绘制短元音，再绘制辅音！ | 转移到 $S_2$；将死符压栈 | 转移到 $S_0$；弹出并清空栈 |
| **$S_2$ (已见死符)**| 转移到 $S_1$；将第二辅音压栈（构筑半辅音连缀群） | **触发连缀重排**！转移到 $S_0$；将元音抛至整个连缀左端！ | 转移到 $S_0$；清空栈 | 转移到 $S_0$；清空栈 |

这种单趟纯线性自动机机制，使得苹果 macOS 的 CoreText 图形框架在处理复杂的梵文经文、藏文千字大藏经时，以极简的查表动作完成了传统排版软件需要数十重正则匹配才能完成的宏伟变换。

---

## D.10 OpenType 与 AAT 排版体系深度技术对照

| 技术维度 | 微软 / Adobe OpenType | 苹果 Apple Advanced Typography (AAT) |
| :--- | :--- | :--- |
| **核心计算模型** | 基于多轮遍历的声明式模式替换查找表（Lookups & Features） | 基于有限状态机（Finite State Machines）的单趟流式自动机 |
| **执行时间复杂度** | 最坏情况下为多次遍历匹配（$O(N \times K)$，依赖查找链长度） | 严格单趟线性时间扫描（$O(N)$，扫描一遍文本即完成排版） |
| **排版逻辑归属** | **外部驱动主导**：字体仅提供数据，排版整形引擎（HarfBuzz, Uniscribe）承担脚本形态逻辑 | **字体内部自治**：字体自身即为完整状态机，上层排版引擎无需知道任何具体语言规则 |
| **跨文字基线支持** | `BASE` 表（罗马基线、汉字底部、中轴、数学轴） | `bsln` 表（32 种脚本原生基线优先级） |
| **字距微调能力** | GPOS Type 2（静态字偶对与分类微调矩阵） | `kerx` 表（支持跨流字距微调与状态机级 8 字符级联微调） |
| **多语言本地化** | 采用 4 字节全局 ASCII 标签（如 'liga'），UI 名称需操作系统单独提供 | `feat` 表将特性代码与 `name` 表多语言字串原生绑定，字体自带本地化菜单 |
| **工业生态与标准** | **全球绝对主导标准**：Windows, Linux, Android, Web 浏览器默认标准 | 苹果生态独占专有标准：macOS, iOS 原生支持，工业跨平台支持较弱 |
---

## D.11 OpenType 1.8 矢量可变字体（Variable Fonts）体系演进

2016 年 9 月，苹果、微软、Adobe 与 Google 在波兰华沙的 ATypI 大会上联合发布了历史性的 **OpenType 1.8 规范**。该规范引入了源自苹果 TrueType GX 与 Adobe Multiple Master 的集大成者——**OpenType 字体可变机制（OpenType Font Variations）**。

### 1. `fvar` 表（字体变化轴与命名实例表）
`fvar`（Font Variations Table）定义了字体在 $k$ 维设计空间中的连续变化轴线：

```xml
<fvar>
  <!-- 声明五大注册标准设计轴之一：字重轴 (wght) -->
  <Axis>
    <AxisTag value="wght"/>
    <Flags value="0x0000"/>
    <MinValue value="100.0"/>
    <DefaultValue value="400.0"/>
    <MaxValue value="900.0"/>
    <AxisNameID value="256"/>
  </Axis>
  <!-- 声明字宽轴 (wdth) -->
  <Axis>
    <AxisTag value="wdth"/>
    <Flags value="0x0000"/>
    <MinValue value="75.0"/>
    <DefaultValue value="100.0"/>
    <MaxValue value="125.0"/>
    <AxisNameID value="257"/>
  </Axis>

  <!-- 预定义命名的静态样式快照 (Named Instances) -->
  <NamedInstance nameID="258"> <!-- "Light Condensed" -->
    <Coordinates>
      <Coord axis="wght" value="300.0"/>
      <Coord axis="wdth" value="75.0"/>
    </Coordinates>
  </NamedInstance>
  <NamedInstance nameID="259"> <!-- "Bold" -->
    <Coordinates>
      <Coord axis="wght" value="700.0"/>
      <Coord axis="wdth" value="100.0"/>
    </Coordinates>
  </NamedInstance>
</fvar>
```

#### 五大国际注册标准轴标签（Standard Registered Axes）：
* **`wght`（Weight / 字重轴）**：取值范围 $1 \dots 1000$（400 为 Regular，700 为 Bold）；
* **`wdth`（Width / 字宽轴）**：以基准设计宽度的百分比衡量（75% Condensed 至 125% Expanded）；
* **`slnt`（Slant / 倾斜角轴）**：文字顺时针倾斜度数（正数为倾斜度，如 $-12$）；
* **`ital`（Italic / 意大利体轴）**：二元或连续轴（0 代表正体 Roman，1 代表真正的手写斜体 Italic）；
* **`opsz`（Optical Size / 视觉字号轴）**：指示字体当前排版使用的物理磅值（如 6pt 至 72pt），引擎据此自动调整笔画粗细对比度与字距。

---

### 2. `gvar` 表（字形变化量数据表 Tuple Variation Store）
在可变字体中，基础轮廓仅存储在 `glyf` 表中（默认母版坐标）。当用户在 CSS 中指定 `font-weight: 550` 时，渲染引擎查询 `gvar` 表：
* 每个轮廓控制点存储的不是绝对坐标，而是一组**变化量差分向量（Delta Vectors: $\Delta x, \Delta y$）**；
* 通过 **元组变化存储器（Tuple Variation Store）** 算法，引擎将用户输入的浮点轴向坐标映射为归一化标量因数；
* 最终物理轮廓点由默认坐标与各轴向 Delta 的标量加权和瞬间线性计算得出：
  $$\mathbf{P}_{\text{rendered}} = \mathbf{P}_{\text{default}} + \sum_{i=1}^m \text{Scalar}_i \times \Delta \mathbf{P}_i$$

不仅轮廓点，OpenType 1.8 更引入了 `HVAR`（水平度量变化表）与 `MVAR`（全局度量变化表），动态联动调整升部、降部与字宽，使原本需要包含数十个独立 `.ttf` 文件（总计数十兆字节）的巨型家族，以**单一紧凑文件（通常仅增加 20% 体积）**的形式完整覆盖了无限连续维度的排印设计空间！
