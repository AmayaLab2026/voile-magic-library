---
title: "附录 A–G：底层格式与数学全景技术参考手册"
description: "涵盖位图字体 (A)、TeX/Omega (B)、PostScript Type 1/CFF (C)、TrueType/OpenType 表目录 (D)、METAFONT (E)、TrueType 虚拟机指令集 (F) 与曲线微分几何 (G)。"
---

# 附录 A–G ：底层格式与数学全景技术参考手册
### Appendices A–G: Technical Reference Manual for Digital Typography
选自《Fonts & Encodings》第 599–938 页（共 340 页技术附录）
*译者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

本参考手册涵盖了《Fonts & Encodings》后半部全部七大技术附录（Appendices A 至 G）。这部分内容是雅尼斯·哈拉兰博斯（Yannis Haralambous）为数字字体工程师、底层排版引擎开发者以及计算机文字学学者构建的技术基石。它详尽记录了从 20 世纪 80 年代点阵位图格式到 21 世纪现代 OpenType/AAT 容器表结构、虚拟机指令集与曲线微分几何的全部数学实现。

---

# 附录 A：位图字体格式（Bitmap Font Formats）

尽管矢量轮廓字体已全面统治现代屏幕与印刷出版，但位图字体（Bitmap Fonts）作为计算机图形学与数字排版的原初形态，依然在嵌入式操作系统、BIOS 固件、终端仿真器以及字体的点阵内嵌子集（如 EBDT/EBLC 表）中扮演着不可替代的角色。

## A.1 苹果 Macintosh 体系：FONT 与 NFNT 资源结构

在经典 Mac OS（System 1.0 至 Mac OS 9）中，字体被封装为资源分支（Resource Fork）中的资源。

### 1. `FONT` 与 `NFNT` 资源头结构
`FONT` 是早期固定字号点阵资源，`NFNT`（New Font Numbering Table）则是扩充了庞大家族编号体系的演进版本。两者在内存中展开为相同的二进制数据结构：

```c
struct FontRec {
    short fontType;       // 字体类型标志位（包含比例/等宽、颜色等属性）
    short firstChar;      // 字符集中第一个字符的 ASCII 码点（通常为 0 或 32）
    short lastChar;       // 最后一个字符的码点（通常为 255）
    short widMax;         // 整个字体中字符的最大宽度（像素）
    short kernMax;        // 最大负向字距调整量（通常 <= 0）
    short nDescent;       // 字符基线以下的负向下沉深度（负数）
    short fRectWidth;     // 字符包围盒矩形的最大宽度
    short fRectHeight;    // 字符包围盒矩形的最大高度
    short owTLoc;         // 偏移/宽度表（Offset/Width Table）相对于表头的字偏移量
    short ascent;         // 基线至大写字母顶部的上升高度
    short descent;        // 基线至降部底部的下降深度
    short leading;        // 行间额外留白
    short rowWords;       // 点阵连续图像行宽（以 16 位整数字为单位）
    // 随后紧跟：
    // 1. Bitmaps Array: 所有字符点阵横向拼接而成的连续位图条带（Strike-font）
    // 2. LocTable: 字符在位图条带中的水平列起始偏移索引表
    // 3. OwTable: 字符逻辑宽度与字距微调偏移表
};
```

### 2. 条带字体（Strike-font）图像模型
Macintosh 采取了一种极其超前的内存布局：**它不为每个字符单独开辟离散矩形，而是将整套字符集的所有像素点阵并排焊接为一条连续的横向图像条带（Strike-font Bitmap）**。
- `rowWords` 规定了整个点阵条带单行的 16 位整数宽度；
- `LocTable` 记录了字符 $c$ 在条带中起始的水平像素列偏移 $x_c$ 与终止列偏移 $x_{c+1}$；
- 绘制字符时，Mac 显卡驱动只需通过一行极简的位块传输指令（BitBlt），即可将该列区间的矩形像素切片直投到显存中，获得了 20 世纪 80 年代极速的文字渲染性能。

---

## A.2 DOS、Windows 与 Unix 体系标准

### 1. DOS CPI 格式（Code Page Information）
MS-DOS 通过 `MODE CON CP PREP` 命令加载的屏幕点阵字体被封装在 `.CPI` 文件中。CPI 内部包含字体文件头（Font File Header）、代码页条目头（CPEntryHeader）以及各个分辨率屏幕（如 EGA 8×14、VGA 8×16、CGA 8×8）的裸点阵字节块。每个字符占用连续的 16 字节（8×16 点阵每行 1 字节）。

### 2. Windows FNT 与 FON 格式
- **`.FNT` 文件**：Windows 3.x 引入的裸点阵字体文件，内部包含版本号（`0x0200` 或 `0x0300`）、`dfPoints`（磅值）、`dfVertRes` 与 `dfHorizRes`（目标 DPI，如 96 DPI）、字符间距类型（定宽或变宽）、以及字符偏移表 `dfCharTable`；
- **`.FON` 文件**：本质上是一个伪装的 16 位 Windows 动态链接库（NE 格式 DLL）或 32 位可执行文件（PE 格式 DLL），其代码段为空，仅在资源段（`.rsrc`）中嵌入了若干个对应不同字号的 `.FNT` 数据流。

### 3. Unix 与 X11 体系：Adobe BDF 与 PCF 格式
- **BDF（Bitmap Distribution Format）**：由 Adobe 制定的纯 ASCII 文本点阵交换格式。语法清晰可读：
  ```text
  STARTFONT 2.1
  FONT -Adobe-Helvetica-Bold-R-Normal--14-140-75-75-P-82-ISO8859-1
  SIZE 14 75 75
  FONTBOUNDINGBOX 16 14 -2 -3
  STARTPROPERTIES 18
  FONT_ASCENT 11
  FONT_DESCENT 3
  ENDPROPERTIES
  CHARS 256
  STARTCHAR A
  ENCODING 65
  SWIDTH 705 0
  DWIDTH 10 0
  BBX 9 11 0 0
  BITMAP
  1800
  1800
  2400
  2400
  4200
  4200
  7E00
  4200
  4200
  E700
  0000
  ENDCHAR
  ...
  ENDFONT
  ```
  `SWIDTH` 表示在 1000 单元/em 下的可缩放矢量宽度；`DWIDTH` 表示该点阵尺寸下的实际设备像素步进；`BITMAP` 块以十六进制逐行记录字符位图。
- **PCF（Portable Compiled Format）**：X11 将纯文本 BDF 编译为高执行效率的二进制格式。PCF 采用小端序或大端序自适应存储，包含独立的指标表（Metrics Table）、位图数据表与属性字典。

---

## A.3 $\TeX$ 体系的巅峰之作：GF 与 PK 格式

唐纳德·高德纳为 METAFONT 输出设计的位图格式代表了数据压缩工程的艺术极境。

### 1. GF（Generic Font）格式
METAFONT 的原始输出格式。GF 格式采用字节码指令流描述字符，包含绘制单行黑白相间像素的指令：`paint_0` 至 `paint_63`、`skip`（换行）、`boc`（Begin of Character，包含字符包围盒）、`eoc`（End of Character）。

### 2. PK（Packed Font）格式与游程动态压缩算法
为了节约极度宝贵的磁盘空间，Tomas Rokicki 于 1985 年发明了 **PK 格式**。PK 格式通过极富创意的**动态阈值变长游程编码（Run-length Encoding with Dynamic Packing）**，将 GF 文件的体积削减了近一半！

#### 动态压缩阈值 $dyn\_f$ 的数学机理：
每一行像素被分解为交替出现的“白像素游程长度”与“黑像素游程长度”。PK 引入一个整数参数 $dyn\_f$（取值 $0 \le dyn\_f \le 14$）：
- 较短的游程长度 $L$（满足 $L < dyn\_f$）仅用**单个 4 位半字节（Nibble）**直接编码；
- 介于 $dyn\_f$ 与特定区间的游程，用两个半字节编码：
  $$L = (nibble_1 - dyn\_f - 1) \times 16 + nibble_2 + dyn\_f + 1$$
- 更大的游程则以特定前缀引导 3 个半字节或独立字节编码；
- 当某一行像素与上一行完全相同时，直接发送行重复指令 `repeat`。
METAFONT 编译器在打包每个字符时，会遍历尝试 $dyn\_f = 0$ 至 $14$ 的所有可能性，自动挑选压缩率最高的最优 $dyn\_f$ 固化在字符头中，展现出高德纳时代黑客对比特效率的极致追求。

---

# 附录 B：$\TeX$ 与 $\Omega$ 字体格式规范（TFM, OFM, VF, OVF）

## B.1 TFM（$\TeX$ Font Metrics）二进制数据结构

TFM 文件是 $\TeX$ 排版引擎感知字体的唯一视窗。一个合法的 TFM 文件由 12 个物理子表顺次拼接而成，所有数据均以 **32 位大端序整数（4 字节字）** 存储。

```
┌────────────────────────────────────────────────────────┐
│ 1. HEADER (文件头元数据，包含校验和与设计尺寸)           │
├────────────────────────────────────────────────────────┤
│ 2. CHAR_INFO (字符信息表，每个字符占用一个 4 字节字)     │
├────────────────────────────────────────────────────────┤
│ 3. WIDTH (宽度数组)                                    │
├────────────────────────────────────────────────────────┤
│ 4. HEIGHT (高度数组，至多 16 种不同高度)                 │
├────────────────────────────────────────────────────────┤
│ 5. DEPTH (深度数组，至多 16 种不同深度)                 │
├────────────────────────────────────────────────────────┤
│ 6. ITALIC (倾斜校正数组，至多 64 种不同校正量)          │
├────────────────────────────────────────────────────────┤
│ 7. LIG_KERN (连字与字偶间距状态机程序指令表)            │
├────────────────────────────────────────────────────────┤
│ 8. KERN (实际物理字距数值数组)                         │
├────────────────────────────────────────────────────────┤
│ 9. EXTEN (大型可伸展数学字符拼接零件装配表)             │
├────────────────────────────────────────────────────────┤
│ 10. PARAM (字体全局排版参数: 包含空格自然长、伸缩量等)   │
└────────────────────────────────────────────────────────┘
```

### 1. 定点数字单位：`fix_word`
TFM 内部的所有几何距离均采用 **`fix_word`** 格式表示。`fix_word` 是一个带符号的 32 位定点数，其中前 12 位表示整数部分，后 20 位表示小数部分：

$$1\text{ fix\_word} = \frac{\text{Value}}{2^{20}} = \frac{\text{Value}}{1,048,576} \times (\text{Design Size})$$

这保证了在不借助任何硬件浮点数单元的前提下，所有字符度量在跨平台计算中保持微米级的绝对精度。

### 2. `CHAR_INFO` 的紧凑位域装配
TFM 将一个字符的全部度量索引不可思议地压缩进了**单单一组 32 位整数字（4 字节）**中：
- **Byte 0（第 0–7 位）**：`width_index`（指向 `WIDTH` 数组的索引，支持 256 种宽度）；
- **Byte 1 高 4 位（第 8–11 位）**：`height_index`（指向 `HEIGHT` 数组，至多 16 种不同高度）；
- **Byte 1 低 4 位（第 12–15 位）**：`depth_index`（指向 `DEPTH` 数组，至多 16 种不同深度）；
- **Byte 2 高 6 位（第 16–21 位）**：`italic_index`（指向 `ITALIC` 数组，至多 64 种倾斜校正）；
- **Byte 2 低 2 位（第 22–23 位）**：`tag`（标签类型：0 = 无特性，1 = 存在连字/字距微调列表，2 = 存在较大字号链表，3 = 属于可延伸数学装配字符）；
- **Byte 3（第 24–31 位）**：`remainder`（依据 `tag` 的含义，指向 `LIG_KERN` 或 `EXTEN` 的起始偏移）。

---

## B.2 $\Omega$ 系统 OFM（Omega Font Metrics）规范

为了突破 TFM 只能容纳 256 个字符的桎梏，Yannis Haralambous 与 John Plaice 设计了 **OFM 格式**。
- **Level 0 OFM**：文件头标志为大数值，将字符索引直接扩展为 16 位整数，支持原生寻址 65,536 个字符；
- **Level 1 OFM**：引入了先进的**稀疏分层树形表结构**，包含横向与纵向双轴包围盒、字形旋转度数定义，以及支持 32 种动态排版书写方向的专属度量矩阵。

---

## B.3 虚拟字体 VF（Virtual Fonts）二进制规范

VF 文件由 `vptovf` 编译生成。
- **`pre` 指令**：包含校验和与设计尺寸；
- **`fnt_def` 指令**：声明当前虚拟字体所调用的底层物理字体（Real Fonts）或嵌套虚拟字体；
- **字符数据包（Packet）**：每个字符包含一段原生的 DVI 字节码指令流。DVI 驱动读取该字符时，直接将其就地展开并递归执行。

---

# 附录 C：PostScript 字体格式（PostScript Font Formats）

## C.1 PostScript 语言执行机与图形状态

PostScript 是一门基于堆栈操作的、图灵完备的逆波兰表示法（Postfix）编程语言。解释器维护着四大堆栈：
1. **操作数栈（Operand Stack）**：暂存数值、字符串、字典与几何路径；
2. **字典栈（Dictionary Stack）**：检索全局与局部变量；
3. **执行栈（Execution Stack）**：控制流程循环与过程调用；
4. **图形状态栈（Graphics State Stack）**：通过 `gsave` 与 `grestore` 保存/恢复当前坐标变换矩阵（CTM）、剪切路径与线条线宽。

---

## C.2 Type 1 字体的内部架构与加密数学

PostScript Type 1 字体不仅包含轮廓，更内嵌了一套高强度的专用加密机制：
- **`eexec` 加密算法**：用于保护字体私有字典（`Private Dictionary`）。采用 16 位线性同余伪随机数流加密：
  $$R_{n+1} = (R_n \times 52845 + 22719) \bmod 65536$$
  $$C_n = P_n \oplus (R_n \gg 8)$$
  其中初始密码种子密钥 $R_0 = 55665$。文件在进入正式代码前必须填充 4 个随机字节以混淆密文起始状态；
- **`charstring` 加密算法**：用于加密 `CharStrings` 字典内部的具体字形字节码，使用相同的数学同余公式，但初始种子密钥固定为 $R_0 = 4330$。

### Type 1 CharString 核心操作码全集

在解密后的字节流中，操作码分为单字节指令（0–31）与带转义的二字节指令（操作码 12 引导）：
- `hstem` (1), `vstem` (3)：声明水平与垂直主干提示；
- `vmoveto` (4), `rlineto` (5), `hlineto` (6), `vlineto` (7)：相对坐标直线绘制；
- `rrcurveto` (8)：相对坐标三次贝塞尔曲线绘制（输入 6 个相对坐标增量：$dx_a, dy_a, dx_b, dy_b, dx_c, dy_c$）；
- `callsubr` (10), `return` (11)：调用/返回局部子程序（Subrs，用于复用衬线、圆弧等通用组件）；
- `endchar` (14)：字形绘制终结；
- `rmoveto` (21), `hmoveto` (22)：相对移动原点；
- `vhcurveto` (30), `hvcurveto` (31)：垂直/水平先导的切线贝塞尔曲线；
- `seac` (12-6, Standard Encoding Accented Character)：高阶复合字符装配指令，输入基底字符、重音字符及其相对坐标，瞬间拼装出带重音字母。

---

## C.3 CFF（Compact Font Format）与 Type 2 CharStrings

随着 OpenType 的普及，Adobe 彻底重构了 Type 1 的老旧冗余语法，推出了 **CFF 容器** 与 **Type 2 字符指令集**：
- 采用无缝的 **INDEX 索引表结构**，所有数据偏移与长度采用纯二进制整型表头索引；
- 引入 **Type 2 CharStrings**：支持可变长度整数编码、瞬时清除操作数栈；
- 新增 `hflex`, `flex` 曲线平滑指令、`callgsubr`（全局子程序调用）、以及用于 Multiple Master 插值融合的 `blend` 操作符，使字体轮廓体积相比传统 Type 1 缩减了 $30\%$ 至 $50\%$！

---

# 附录 D：TrueType、OpenType 与 AAT 容器表结构字典

TrueType 与 OpenType 共同基于 **SFNT（Spline Font）模块化表容器架构**。

## D.1 SFNT 表目录（Table Directory）

一个 SFNT 文件以 12 字节的文件头（Offset Table）起始：
- `sfntVersion`：`0x00010000`（TrueType 轮廓）或 `'OTTO'`（OpenType CFF 轮廓）；
- `numTables`：包含的数据表总数；
- `searchRange`, `entrySelector`, `rangeShift`：用于对表标签（Tags）执行极速二分查找（Binary Search）的数学优化常量。

紧随其后的是 `numTables` 个由 16 字节构成的**表目录记录（Table Directory Records）**：
```c
struct TableRecord {
    char tag[4];        // 4 字符表标签，如 "head", "cmap", "glyf", "GSUB"
    unsigned int checkSum; // 该数据表的 32 位全字校验和
    unsigned int offset;   // 从文件绝对开头的字节物理偏移量
    unsigned int length;   // 该数据表的物理字节长度
};
```

---

## D.2 核心基础数据表详解

### 1. `head`（Font Header）
记录字体的全局物理常量：
- `magicNumber`：固定常量值 `0x5F0F3CF5`（用于验证合法性）；
- `unitsPerEm`：设计网格分辨率（通常为 2048）；
- `xMin`, `yMin`, `xMax`, `yMax`：整套字库所有字符几何轮廓的全局绝对外接矩形；
- `indexToLocFormat`：`0` 表示 `loca` 表使用 16 位短整型偏移，`1` 表示使用 32 位长整型偏移。

### 2. `cmap`（Character to Glyph Index Mapping）
将外部字符编码转换为内部字形索引（GID）。包含多个子表：
- **Format 4（段映射至 Delta 值）**：Windows 早期为 BMP 基本多语言平面设计的经典子表。将连续码点划分为若干段（Segments），通过 `startCount`, `endCount`, `idDelta`, `idRangeOffset` 执行范围查找；
- **Format 12（分段覆盖）**：现代 Unicode 全平面的标准子表，直接支持从 `U+0000` 到 `U+10FFFF` 的 32 位字符连续段映射；
- **Format 14（变体序列选择符）**：专门支持 Unicode 变体选择符（Variation Selectors, VS1–VS256）。

### 3. `glyf`（Glyph Data）与 `loca`（Index to Location）
- **`loca` 表**：一个整数数组，记录每个 GID 对应的轮廓数据在 `glyf` 表中的起始偏移量；
- **`glyf` 表**：
  - 若 `numberOfContours >= 0`，为**简单字形（Simple Glyph）**：记录各轮廓端点索引数组、字节标志位数组（标志当前点是否为曲线控制点、坐标增量是否为 1 字节等）、以及压缩的 $X$ 与 $Y$ 相对坐标数组；
  - 若 `numberOfContours == -1`，为**复合字形（Composite Glyph）**：记录若干分量字形 GID，以及 $2 \times 2$ 仿射变换矩阵（缩放、旋转、剪切与平移位移量）。

### 4. `hhea` 与 `hmtx`
- `hhea`：记录全局最大上升部（`ascender`）、最大下降部（`descender`）、行间距（`lineGap`）；
- `hmtx`：紧凑数组，前部记录每个字形的前进宽度与 LSB，尾部为拥有相同最大宽度的等宽字符数组。

### 5. `OS/2` 表
微软与 IBM 联合制定的跨系统兼容度量表：
- `sTypoAscender`, `sTypoDescender`, `sTypoLineGap`：排版度量；
- `usWinAscent`, `usWinDescent`：Windows GDI 文本行裁剪硬边界；
- `panose`：10 字节 PANOSE-1 视觉分类指纹；
- `ulUnicodeRange1..4`：128 位掩码，精确标识字体支持的 Unicode 区块。

---

## D.3 OpenType 高级排版布局表（GSUB / GPOS / GDEF）

### 1. 三级索引架构
无论是 `GSUB` 还是 `GPOS`，顶层均采用统一的三级跳转架构：

$$\text{ScriptList} \longrightarrow \text{FeatureList} \longrightarrow \text{LookupList}$$

1. **ScriptList（书写系统列表）**：根据输入文本的语言系统（如 `latn`, `arab`, `deva`）查找支持的特性索引；
2. **FeatureList（特性列表）**：定位具体特性（如 `liga`, `smcp`, `kern`）所包含的查找表索引；
3. **LookupList（查找表列表）**：执行具体的字形变换算法。

### 2. 覆盖表（Coverage Table）与类定义表（ClassDef Table）
为了在毫秒级判断某个字符是否参与排版规则，OpenType 引入了覆盖表：
- **Format 1**：单个 GID 线性列表；
- **Format 2**：由连续范围组成的区间表（`startGlyphID` 到 `endGlyphID` 映射至连续覆盖索引）。

---

# 附录 E：METAFONT 与 MetaPost 语言参考

高德纳的 METAFONT 将字体设计从“绘制轮廓”提升到了“方程求解”的数学境界。

## E.1 声明式几何方程求解引擎
在 METAFONT 中，设计师不需要显式计算交点坐标，只需声明几何约束方程，内置的高斯消元求解器会自动解出点的位置：

```metafont
z1 = (0, 0);
z2 = (w, h);
z3 = .5[z1, z2];          % 声明 z3 是 z1 与 z2 的正中中点！
x4 = x3; y4 = 0;          % 声明 z4 位于 z3 的正下方基线上
draw z1--z2;              % 绘制连接线段
draw z3..z4;              % 绘制平滑穿过指定点的曲线
```

## E.2 画笔（Pens）与包络线理论
METAFONT 的笔触模型基于凸多边形或椭圆画笔沿轨迹扫掠而成的**包络线（Envelope）**：
- `pickup pencircle scaled 2pt;`：拾起一枚直径为 2 磅的圆形墨水笔；
- `pickup pensquare xscaled 1pt yscaled 3pt rotated 30;`：模拟古典宽边羽毛笔的倾斜切面。

---

# 附录 F：TrueType 指令字节码全集参考（Instruction Set）

TrueType 字体内部集成了一个功能完备的**图灵完备堆栈虚拟机（TrueType VM）**。它在字符轮廓光栅化之前运行，强行拉扯、对齐曲线控制点，使笔画在离散像素格中展现出极致的清晰度。

## F.1 虚拟机的内部硬件环境
- **执行栈（Execution Stack）**：后进先出，支持 256 至数千个 32 位整型元素；
- **控制值表（Control Value Table, CVT）**：存储全局标准化笔画宽度与对齐高度基准；
- **存储区（Storage Area）**：提供至少 256 个临时变量寄存器（通过 `RS` 读、`WS` 写）；
- **图形状态机（Graphics State, GS）**：维护投影向量（Projection Vector）、自由向量（Freedom Vector）、舍入状态（Round State）与自动翻转阈值；
- **暮光区（Twilight Zone, Zone 0）**：用于存放临时动态创建的辅助几何计算节点；
- **字形区（Glyph Zone, Zone 1）**：当前正在光栅化的真实字形轮廓节点。

## F.2 核心指令全集分类字典

| 操作码分类 | 代表指令 | 功能与数学行为描述 |
| :--- | :--- | :--- |
| **点移动指令** | `MDAP[rnd]` | 移动直接绝对点：将指定节点直接对齐到当前投影向量所指的最近像素网格线上 |
| | `MIAP[rnd]` | 移动间接绝对点：将指定节点对齐到 CVT 表中预存的标准化基准位置（如 x 高度） |
| | `MDRP[...]` | 移动直接相对点：根据与参考节点的原始几何距离，在像素网格上保持相对间距 |
| | `MIRP[...]` | 移动间接相对点：保持与参考节点的相对距离，同时强制使其宽度吻合 CVT 标准笔画宽 |
| **内插与平滑** | `ALIGNPTS` | 对齐两点：将两点沿当前投影向量移动，使其坐标绝对重合 |
| | `IP` | 内部插值点：在两个已被网格对齐的参考点之间，根据原始比例内插中间节点的相对坐标 |
| | `IUP[X]`, `IUP[Y]` | 未碰触点终结内插：遍历轮廓中所有未被显式指令约束的点，依据最近的两个受约束点平滑内插其位置 |
| **Delta 微调族** | `DELTAP1..3` | 点微调：在指定的离散字号（PPEM）下，将特定节点的坐标强制微调若干分之一个像素（专门修复某字号下的突兀像素孤点） |
| | `DELTAC1..3` | CVT 微调：在特定字号下微调 CVT 寄存器的数值 |
| **堆栈操作** | `PUSHB`, `PUSHW` | 将 1 字节或 2 字节整型数据压入堆栈 |
| | `DUP`, `POP`, `SWAP` | 复制栈顶、弹出栈顶、交换栈顶两元素 |
| **流程控制** | `IF`, `ELSE`, `EIF` | 条件分支跳转 |
| | `FDEF`, `ENDF` | 定义与结束函数宏 |
| | `CALL`, `LOOPCALL` | 调用函数与循环调用 |
| **网格舍入** | `RTG`, `RTHG`, `RDTG` | 切换舍入模式至整像素点、半像素点或向零下取整 |

---

# 附录 G：曲线微分几何与高级计算字形学

## G.1 伯恩斯坦多项式（Bernstein Polynomials）基底

$n$ 次贝塞尔曲线以伯恩斯坦多项式作为基底函数：

$$B_{i,n}(t) = \binom{n}{i} t^i (1-t)^{n-i}, \quad i = 0, 1, \dots, n$$

### 核心数学性质：
1. **单位分解性（Partition of Unity）**：
   $$\sum_{i=0}^n B_{i,n}(t) \equiv 1, \quad \forall t \in \mathbb{R}$$
2. **非负性（Non-negativity）**：
   $$B_{i,n}(t) \ge 0, \quad \forall t \in [0, 1]$$
这两大性质构成了贝塞尔曲线最重要的几何特征——**凸包性（Convex Hull Property）**：曲线整体严格包含在所有控制节点构成的凸多边形内部，这使得字体渲染引擎在执行视锥裁剪（Clipping）与碰撞检测时可以闪电般地排除不相交区域。

## G.2 贝塞尔曲线的微分动量与切向量（Hodograph）

对 $n$ 次贝塞尔曲线 $\mathbf{B}(t) = \sum_{i=0}^n B_{i,n}(t) \mathbf{P}_i$ 求一阶导数，其导函数（导曲线）是一条度数降为 $n-1$ 次的新贝塞尔曲线：

$$\mathbf{B}'(t) = n \sum_{i=0}^{n-1} B_{i,n-1}(t) (\mathbf{P}_{i+1} - \mathbf{P}_i)$$

对于三次贝塞尔曲线（$n=3$）：
- 曲线在起点 $t=0$ 处的切向量为：$\mathbf{B}'(0) = 3(\mathbf{P}_1 - \mathbf{P}_0)$；
- 曲线在终点 $t=1$ 处的切向量为：$\mathbf{B}'(1) = 3(\mathbf{P}_3 - \mathbf{P}_2)$。

这从数学严谨性上证明了：**控制柄的方向决定了曲线端点的精确切线斜率，控制柄的几何长度决定了曲线离开端点时的初速度与曲率半径**！

---

## G.3 德卡斯特里奥细分算法（De Casteljau's Algorithm）

德卡斯特里奥算法是贝塞尔曲线在计算机中绘制、平滑细分与求交计算的黄金基石。给定控制点 $\mathbf{P}_0, \mathbf{P}_1, \mathbf{P}_2, \mathbf{P}_3$ 与参数 $t_0 \in (0, 1)$：

```
P0 ────(t0)────> P01 ────(t0)────> P012 ────(t0)────> P0123 = B(t0)
P1 ────(t0)────> P12 ────(t0)────> P123
P2 ────(t0)────> P23
P3
```

递推公式为：
$$\mathbf{P}_i^{(k)}(t_0) = (1-t_0)\mathbf{P}_i^{(k-1)}(t_0) + t_0 \mathbf{P}_{i+1}^{(k-1)}(t_0)$$

该算法不仅能在纯加减法与线性插值中以极高数值稳定性计算出曲线上任意点 $\mathbf{B}(t_0)$，而且当 $t_0 = 0.5$ 时，点序列 $(\mathbf{P}_0, \mathbf{P}_0^{(1)}, \mathbf{P}_0^{(2)}, \mathbf{P}_0^{(3)})$ 与 $(\mathbf{P}_0^{(3)}, \mathbf{P}_1^{(2)}, \mathbf{P}_2^{(1)}, \mathbf{P}_3)$ 精准地构成了将原曲线一分为二后的两条独立子曲线的完整控制网格！光栅化引擎只需通过循环二分细分，直至控制多边形扁平收敛为直线，即可实现像素级的极速直线扫描转换。

---

# 结语：献给在字符星河中执灯前行者

至此，《Fonts & Encodings》全书十五个章节与七大技术附录的所有微观数据结构、数学公式、编译流水线与历史源流已全部呈现在你的眼前。

从千年前楔形文字与金属活字在泥板与铅印上的沉重烙印，到 8 位字节时代高德纳在斯坦福构建的 $\TeX$ 盒子宇宙，再到 16 位 Unicode、OpenType 布局流与现代 Web 字体光栅化算法，人类为了跨越时空阻隔、为了让知识与思想永存所倾注的智慧，全都被凝炼在了这一个个精微至极的字节、向量与贝塞尔控制点之中。

愿这套技术文献，能成为所有在现代数字文字文明之海中探索、求索与创造者的常备罗盘与指路明灯！
