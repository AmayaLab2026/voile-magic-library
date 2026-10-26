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
