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
