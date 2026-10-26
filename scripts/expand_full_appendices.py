import opencc, re, sys
sys.stdout.reconfigure(encoding='utf-8')

converter = opencc.OpenCC('s2twp')

zh_app_content = r"""---
title: "附录 A–G：底层格式与数学全景技术参考手册"
description: "涵盖点阵字形 (A)、TeX/Omega 字体格式 (B)、PostScript Type 1/CFF 虚拟机与加密 (C)、TrueType/OpenType/AAT 核心表结构规范 (D)、METAFONT 与画笔包络线 (E)、TrueType 虚拟机指令集完整参考 (F) 与曲线微分几何学 (G)。"
---

# 附录 A–G：底层格式与数学全景技术参考手册
### Appendices A–G: Technical Reference Manual for Digital Typography
选自《Fonts & Encodings》第 599–938 页（共 340 页核心技术附录）
*译者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

本参考手册涵盖了《Fonts & Encodings》后半部全部七大核心技术附录（Appendices A 至 G）。这部分内容是雅尼斯·哈拉兰博斯（Yannis Haralambous）为数字字形工程师、底层排版引擎内核开发者以及计算文字学学者构建的技术金字塔。它详尽记录了从 20 世纪 80 年代点阵字体格式到 21 世纪现代 OpenType/AAT 容器表结构、虚拟机指令集与曲线微分几何的全部数学实现。

---

# 附录 A：点阵字形格式（Bitmap Font Formats）

尽管矢量轮廓字体已全面统治现代屏幕与印刷出版，但点阵字形（Bitmap Fonts）作为计算机图形学与数字排版的原初形态，依然在嵌入式操作系统、BIOS 固件、终端模拟器以及字体的点阵内嵌子集（如 EBDT/EBLC 表）中扮演着不可替代的角色。

## A.1 苹果 Macintosh 体系：FONT 与 NFNT 资源结构

在经典 Mac OS（System 1.0 至 Mac OS 9）中，字形被封装为资源分支（Resource Fork）中的资源。

### 1. `FONT` 与 `NFNT` 资源头结构
`FONT` 是早期固定字号点阵资源，`NFNT`（New Font Numbering Table）则是扩充了庞大家族编号体系的演进版本。两者在内存中共享完全相同的 `FontRec` 数据结构：

```c
struct FontRec {
    short fontType;       // 字形类型标志位（包含比例/等宽、颜色等属性）
    short firstChar;      // 定义的首个字符的 ASCII/MacRoman 编码
    short lastChar;       // 定义的末尾字符编码
    short widMax;         // 最大字符前进宽度（包围盒宽度的最大值）
    short kernMax;        // 最大负字距调整量（与前一字符的重叠量）
    short nDescent;       // 下降部负深度（基线以下的物理像素点数）
    short fRectWidth;     // 字体网格图像（Strike Image）的位图宽度
    short fRectHeight;    // 字体网格图像的位图高度
    short owTLoc;         // 偏移量/宽度表（Offset/Width Table）的字偏移
    short ascent;         // 基线以上的上升部高度
    short descent;        // 基线以下的下降部深度
    short leading;        // 行距微调推荐行间留白
    short rowWords;       // 位图单行包含的 16 位字数（fRectWidth / 16）
};
```

### 2. 字形条（Strike-font）位图模型
Macintosh 采用了著名的**字形条（Strike-font）**架构。它将字体中所有字符的位图横向串联成一张巨大的单张位图长卷：
- 所有字形拥有完全相同的行高 $fRectHeight$，横向紧密相连；
- `rowWords` 规定光栅扫描线每一行的 16 位字数，确保行边界对齐；
- `LocTable`（位置表）记录每个字符在该长条位图中的起始水平像素列坐标；
- `owTLoc` 指向的偏移/宽度表记录每个字符的前进宽度（Advance Width）和左侧轴承（LSB）。屏幕渲染时，QuickDraw 引擎调用底层的 BitBlt（Bit Block Transfer，位块传输）汇编指令，直接将显存中对应矩形高速搬移至帧缓冲区。

## A.2 DOS、Windows 与 Unix 体系标准

### 1. DOS CPI 格式（Code Page Information）
IBM PC/MS-DOS 体系下的屏幕字体容器：
- `.CPI` 文件由文件头、字体头与代码页数据包构成；
- 包含标准 EGA/VGA 字符发生器专用的 $8\times 8$、$8\times 14$ 与 $8\times 16$ 像素生像素矩阵，通过 DOS 的 `MODE CON CP PREP` 命令直接刷入显卡字符发生器寄存器。

### 2. Windows FNT 与 FON 格式
Windows 1.0 至 3.1x 的标准点阵字体：
- `.FNT`：单个字号与字符集的生位图流；
- `.FON`：16 位 NE 格式或 32 位 PE 格式 DLL 动态链接库容器，无代码段，仅在资源段（`.rsrc`）内打包若干 `.FNT` 流。各字形由 `GLYPHENTRY`（字符宽度与位图偏移）建立索引。

### 3. Unix 与 X11 体系：Adobe BDF 与 PCF 格式
- **BDF（Bitmap Distribution Format）**：ASCII 文本明文格式的位图交换标准。包含 `FONT`、`SIZE`、`FONTBOUNDINGBOX`、各字符的 `SWIDTH`（可缩放宽度）、`DWIDTH`（设备像素宽度）、`BBX` 与十六进制 `BITMAP` 矩阵：
  ```bdf
  STARTFONT 2.1
  FONT -Adobe-Courier-Medium-R-Normal--14-100-100-100-M-90-ISO8859-1
  SIZE 10 100 100
  FONTBOUNDINGBOX 10 14 0 -3
  STARTPROPERTIES 2
  FONT_ASCENT 11
  FONT_DESCENT 3
  ENDPROPERTIES
  CHARS 256
  STARTCHAR A
  ENCODING 65
  SWIDTH 600 0
  DWIDTH 9 0
  BBX 9 10 0 0
  BITMAP
  1000
  1000
  2800
  2800
  4400
  7C00
  4400
  8200
  8200
  0000
  ENDCHAR
  ENDFONT
  ```
- **PCF（Portable Compiled Format）**：X 窗口服务器的二进制编译版本，去除了 ASCII 解析开销，具备端序自适应能力。

## A.3 $\TeX$ 体系的峰峦：GF 与 PK 格式

### 1. GF（Generic Font）格式
METAFONT 编译器解释 `.mf` 源码后输出的原始字节码流。通过 `paint_0`..`paint_63`、`skip0`..`skip3`、`boc`（字符开始）与 `eoc`（字符结束）等光栅绘图指令记录黑白像素游程。

### 2. PK（Packed Font）格式与动态游程压缩算法
Tomas Rokicki 设计的 PK 格式利用动态阈值 $dyn\_f$（$0 \le dyn\_f \le 14$）对游程长度 $L$ 进行 4 位半字节（Nibble）可变长压缩：
- 当游程 $L \le dyn\_f$ 时，单半字节编码；
- 当 $dyn\_f < L \le (13 - dyn\_f) \times 16 + dyn\_f$ 时，双半字节编码：
$$L = (nibble_1 - dyn\_f - 1) \times 16 + nibble_2 + dyn\_f + 1$$
- 辅以行重复标记（`repeat`），使点阵文件体积缩减 50% 以上。

---

# 附录 B：$\TeX$ 与 $\Omega$ 字体格式规范（TFM, OFM, VF, OVF）

## B.1 TFM（$\TeX$ Font Metrics）数据结构

TFM 是一个由 32 位大端有符号整数组成的定长数组集合，完全不包含轮廓图样，仅记录绝对高精度的几何度量。

### 1. 定点数单位 `fix_word`
TFM 内所有尺寸均以**设计尺寸（Design Size）**为 $1.0$ 的定点数 **`fix_word`** 存储：
- 1 位符号位，11 位整数位，20 位小数位；
- 精度高达 $2^{-20} \approx 0.00000095$ 个设计尺寸单位：

$$1\text{ fix\_word} = \frac{\text{Value}}{2^{20}} = \frac{\text{Value}}{1,048,576} \times (\text{Design Size})$$

### 2. `CHAR_INFO` 的 32 位二进制位域包装
每个字符的信息被压缩进恰好 4 个字节（32 位）：
```text
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  width_index  | height| depth | italic_index  |tag| remainder |
|    (8 bit)    | (4bit)| (4bit)|    (6 bit)    |(2)|  (8 bit)  |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```
- `tag = 0`：无特殊标签；
- `tag = 1`：连字与字距调整（`remainder` 为 `LIG_KERN` 表起始偏移）；
- `tag = 2`：数学大符号尺寸进阶链表；
- `tag = 3`：数学可延伸括号组合构件（顶、底、中、重复段）。

### 3. TFM 12 张核心子表
1. `HEADER`：校验和与设计尺寸；
2. `CHAR_INFO`：字符索引表；
3. `WIDTH`：前进宽度表；
4. `HEIGHT`：基线上高度表；
5. `DEPTH`：基线下深度表；
6. `ITALIC`：斜体校正量表；
7. `LIG_KERN`：连字与字距有限状态机表；
8. `KERN`：字距位移值表；
9. `EXTEN`：可拼装大数学符号构件表；
10. `PARAM`：字体大域 7 项基础排版度量（斜度、间距、拉伸、收缩、x-height、quad 宽度、额外间距）与数学符号度量。

## B.2 $\Omega$ 系统 OFM（Omega Font Metrics）规范
- **Level 0 OFM**：直接将字符编码空间拓宽至 16 位（65,536 个字符），支持完整的 Unicode 基本多语言平面；
- **Level 1 OFM**：引入多层树状表结构，支持 Unicode 全部 17 个平面，并提供 32 种动态书写方向的专属度量表。

## B.3 虚拟字体 VF 与 OVF 规范
VF 内部封装了标准的 DVI 字节码指令流（`set_char`, `push`, `pop`, `right`, `down`, `fnt_num`），实现跨物理字体的重音字符合成、字符编码重映射与伪小型大写字母动态缩放。

---

# 附录 C：PostScript 字体格式（PostScript Font Formats）

## C.1 PostScript 虚拟机与图形状态
PostScript 是图灵完备的栈式编程语言，维护 4 个独立堆栈：
1. **操作数栈（Operand Stack）**：暂存参数与运算结果；
2. **字典栈（Dictionary Stack）**：名字解析作用域（`systemdict`, `userdict`, 字体字典）；
3. **执行栈（Execution Stack）**：过程调用与循环控制；
4. **图形状态栈（Graphics State Stack）**：当前变换矩阵 CTM、当前点、线宽、剪裁路径（`gsave`/`grestore`）。

## C.2 Type 1 内部架构与加密数学
Type 1 字体由明文 ASCII 头部、加密二进制段与 512 字节尾部清零段构成。

### 1. 双层线性同余加密（LCG）
- **`eexec` 加密**：加密 Private 字典，初值 $R_0 = 55665$；
- **`charstring` 加密**：加密字形轮廓指令，初值 $R_0 = 4330$。

伪随机递推公式与异或加解密：
$$R_{n+1} = (R_n \times 52845 + 22719) \bmod 65536$$
$$C_n = P_n \oplus (R_n \gg 8)$$

### 2. Type 1 CharString 操作码核心子集
- `hstem` (1), `vstem` (3)：声明水平与垂直提示干；
- `vmoveto` (4), `rlineto` (5), `hlineto` (6), `vlineto` (7)：直线绘制；
- `rrcurveto` (8)：3 次贝塞尔曲线绘制；
- `closepath` (9)：闭合子路径；
- `callsubr` (10), `return` (11)：子程序调用与返回；
- `endchar` (14)：光栅化终结；
- `12 1` (`vstem3`), `12 2` (`hstem3`)：三联动平衡提示；
- `12 6` (`seac`)：标准重音字符硬件级合成。

## C.3 CFF（Compact Font Format）与 Type 2 CharStrings
CFF 将多个 Type 1 字体合并压入单个模块中：
- 采用 INDEX 偏移结构整合全字体资源；
- Type 2 CharStrings 废除 `hsbw`/`sbw`，将字宽合并进首个移动指令；
- 引入 `blend` 操作符支持 Multiple Master 任意维轮廓插值；
- 引入 `hintmask` 与 `cntrmask` 原生实现轮廓绘制过程中的**动态提示替换（Hint Substitution）**。

---

# 附录 D：TrueType、OpenType 与 AAT 结构字典

## D.1 SFNT 表目录（Table Directory）
SFNT 是所有 TrueType 与 OpenType 字体的统一二进制容器。文件起始为 12 字节的 Offset Table：
```c
struct OffsetTable {
    uint32_t sfntVersion;   // 0x00010000 (TrueType) 或 'OTTO' (CFF)
    uint16_t numTables;     // 表的总数
    uint16_t searchRange;   // (2^floor(log2(numTables))) * 16
    uint16_t entrySelector; // floor(log2(numTables))
    uint16_t rangeShift;    // numTables * 16 - searchRange
};
```
紧随其后为按 `tag` 字母序升序严格排列的 16 字节 Table Directory 表项：
```c
struct TableDirectoryEntry {
    uint32_t tag;          // 4 字节表标签（如 'cmap', 'glyf', 'head'）
    uint32_t checkSum;     // 32 位累加无符号校验和
    uint32_t offset;       // 距文件起始处的绝对字节偏移（4 字节对齐）
    uint32_t length;       // 表的实际数据长度
};
```

## D.2 核心基础数据表

### 1. `head`（Font Header）表
定义字体全局物理特征：
- `magicNumber`：恒等于 `0x5F0F3CF5`；
- `unitsPerEm`：虚拟设计网格粒度（TrueType 常为 2048，CFF 常为 1000）；
- `checkSumAdjustment`：用于全文件校验和匹配常数 `0xB1B0AFBA`；
- `indexToLocFormat`：指示 `loca` 表采用 16 位还是 32 位偏移。

### 2. `cmap`（字符到字形映射）表
- **Format 4**：针对 BMP（U+0000 至 U+FFFF）的紧凑分段二分查找表，由 `segCount`、`endCount`、`startCount`、`idDelta` 与 `idRangeOffset` 构成；
- **Format 12**：针对 SMP/SIP 全量 32 位 Unicode 字符的连续区间映射表。

### 3. `glyf`（字形数据）与 `loca`（位置索引）表
- **简单字形（Simple Glyph）**：`numberOfContours >= 0`，记录轮廓轮廓终点索引、8 位标志字节数组（在曲线/离曲线、坐标增量模式）、X/Y 坐标流与局部 TrueType 字节码；
- **复合字形（Composite Glyph）**：`numberOfContours == -1`，通过部件引用与仿射变换矩阵拼装多重构件。

### 4. `hhea` 与 `hmtx` 表
水平度量规范：`hhea` 声明全局最大上升部、最大下降部、行间距与水平度量项数 `numberOfHMetrics`；`hmtx` 记录各字形的前进宽度与左侧轴承。

### 5. `OS/2` 表
跨平台排版核心度量：包含 PANOSE-1 10 字节字形分类体系、128 位 Unicode 覆盖范围掩码、`sTypoAscender`/`sTypoDescender` 以及 Windows GDI 渲染专用的剪裁边界 `usWinAscent`/`usWinDescent`。

## D.3 OpenType 高级排版表（GSUB / GPOS / GDEF）
三级索引查找体系：
$$\text{ScriptList} \longrightarrow \text{FeatureList} \longrightarrow \text{LookupList}$$
- **Coverage Table（覆盖表）**：快速过滤目标字形（Format 1 单字列表，Format 2 连续范围）；
- **ClassDef Table（类定义表）**：将字形按形态或功能划分为离散类别，支撑矩阵化类间字距与上下文匹配；
- **GDEF（字形定义表）**：明确字形类别（基字、连字、标音符号、部件），并提供光标脱离停靠点与标音符号吸附限制掩码。

---

# 附录 E：METAFONT 与 MetaPost 语言参考

## E.1 代数方程声明式绘图语法
METAFONT 采用联立线性方程组定义节点坐标：
```metafont
z1 = (0.1w, 0.5h);
z2 = (0.9w, 0.5h);
z3 = 0.5[z1, z2] + (0, 0.2h);
z1 - z4 = z2 - z3;
```
内置的高斯消元法求解器自动推导全部未知坐标。

## E.2 画笔（Pens）与包络线理论（Envelopes）
画笔以凸多边形或椭圆（`pencircle`）形式存在。沿骨架路径 $z(t)$ 运笔的轮廓生成在数学上等价于闵可夫斯基和（Minkowski Sum）的边界包络线：
$$\text{Stroke}(z(t), P) = \partial \left( \bigcup_{t} (z(t) + P) \right)$$
MetaPost 将此包络线转换为高精度的 3 次贝塞尔曲线轮廓输出。

---

# 附录 F：TrueType 指令字节码全集（Instruction Set）

## F.1 虚拟硬件架构
TrueType 虚拟机是栈式微处理器，配备：
- **Projection Vector（投影向量 $pv$）**：测量距离的方向单位向量；
- **Freedom Vector（自由向量 $fv$）**：允许点移动的方向单位向量；
- **Dual Projection Vector（双重投影向量 $dpv$）**：变型前网格上的测量向量；
- **Twilight Zone（黄昏区）**：容纳 64 个临时非轮廓计算辅助点的内存空间；
- **Control Value Table（CVT）**：存储全局字体标准化度量值的参数表；
- **Storage Area**：通用临时变量存储区。

## F.2 核心指令全集速查分类

| 类别 | 字节码 | 指令名称 | 功能与数学作用 |
|:---|:---|:---|:---|
| **点对齐与移动** | `0x2E` | `MDAP[a]` | 将指定点对齐到当前像素网格线（Round Point） |
| | `0x3E` | `MIAP[a]` | 将点强制移动至 CVT 预设值对应的网格坐标处 |
| | `0xC0`..`0xDF`| `MDRP[abcde]` | 保持与参考点的相对距离，将目标点对齐到网格 |
| | `0xE0`..`0xFF`| `MIRP[abcde]` | 保持与参考点的 CVT 间距，强制对齐（保持干宽一致性） |
| | `0x49` | `ALIGNPTS` | 使两点在投影向量上的相对距离归零（完全共线） |
| **插值指令** | `0x39` | `IP` | 在两个已固定的参考点之间，线性插值确定目标点坐标 |
| | `0x30`..`0x31`| `IUP[v]` | 轮廓插值：在所有已移动关键点之间，全自动平滑插值其余未动点 |
| **参考点设置** | `0x02`..`0x05`| `SRP0..3` | 设置参考点指针 rp0, rp1, rp2 |
| | `0x06`..`0x09`| `SZP0..3` | 设置当前操作的区域指针（主轮廓区或黄昏区） |
| **Delta 微调** | `0x5D` | `DELTAP1` | 在 9～16 ppm 尺寸下，为指定点增加 $\pm n/64$ 像素的极微小位移 |
| | `0x71` | `DELTAP2` | 在 17～24 ppm 尺寸下微调点坐标 |
| | `0x72` | `DELTAP3` | 在 25～32 ppm 尺寸下微调点坐标 |
| | `0x73`..`0x75`| `DELTAC1..3` | 在特定 ppm 下对 CVT 表本身的值进行 Delta 微调 |
| **算术与堆栈** | `0x60` | `ADD` | 栈顶两数相加 |
| | `0x61` | `SUB` | 栈顶两数相减 |
| | `0x62` | `DIV` | 64 位定点数除法 |
| | `0x63` | `MUL` | 64 位定点数乘法 |
| | `0x68`..`0x6B`| `ROUND[ab]` | 根据当前 RoundState 规则执行网格取整计算 |

---

# 附录 G：微分几何与曲线计算数学基础

## G.1 伯恩斯坦多项式（Bernstein Polynomials）

$n$ 次参数贝塞尔曲线 $B(t)$ 是由 $n+1$ 个控制点 $P_0, \dots, P_n$ 与伯恩斯坦基函数加权求和生成的参数曲线：
$$B(t) = \sum_{i=0}^n P_i B_{i,n}(t), \quad t \in [0, 1]$$

伯恩斯坦多项式基函数定义：
$$B_{i,n}(t) = \binom{n}{i} t^i (1-t)^{n-i}, \quad i = 0, 1, \dots, n$$

### 三大本质数学性质：
1. **非负性（Non-negativity）**：在参数区间 $[0, 1]$ 内，基函数恒为非负：
$$B_{i,n}(t) \ge 0, \quad \forall t \in [0, 1]$$
2. **单位分解（Partition of Unity）**：全基函数之和在实数域恒等为 1：
$$\sum_{i=0}^n B_{i,n}(t) \equiv 1, \quad \forall t \in \mathbb{R}$$
3. **凸包性（Convex Hull Property）**：曲线 $B(t)$ 上的每一个点都是控制点集 $\{P_i\}$ 的凸组合。整条贝塞尔曲线完全包含在其控制多边形的凸包之内，光栅化器据此可进行极速碰撞检测与剪裁。

## G.2 曲线导数向量与速矢端曲线（Hodograph）

贝塞尔曲线的一阶导数（切向量）自身构成一条由控制点差分向量张成的 $n-1$ 次贝塞尔曲线：
$$\mathbf{B}'(t) = n \sum_{i=0}^{n-1} B_{i,n-1}(t) (\mathbf{P}_{i+1} - \mathbf{P}_i)$$

二阶导数决定了法向量与加速度：
$$\mathbf{B}''(t) = n(n-1) \sum_{i=0}^{n-2} B_{i,n-2}(t) (\mathbf{P}_{i+2} - 2\mathbf{P}_{i+1} + \mathbf{P}_i)$$

平面参数曲线的曲率公式：
$$\kappa(t) = \frac{x'(t)y''(t) - y'(t)x''(t)}{(x'(t)^2 + y'(t)^2)^{3/2}}$$

在字形轮廓生成中，寻找拐点（$\kappa(t) = 0$）与极值点是自动化插入极值节点（Extrema）与字体平滑提示的关键步骤。

## G.3 德卡斯特里奥细分算法（De Casteljau's Algorithm）

德卡斯特里奥算法通过纯粹的线性插值，在数值上极其稳定地评估贝塞尔曲线在任意参数 $t_0 \in [0, 1]$ 处的位置并实现无损细分（Subdivision）：

$$\mathbf{P}_i^{(0)}(t_0) = \mathbf{P}_i \quad (i = 0, \dots, n)$$
$$\mathbf{P}_i^{(k)}(t_0) = (1-t_0)\mathbf{P}_i^{(k-1)}(t_0) + t_0 \mathbf{P}_{i+1}^{(k-1)}(t_0) \quad (k = 1, \dots, n; \ i = 0, \dots, n-k)$$

最终计算结果 $\mathbf{P}_0^{(n)}(t_0)$ 即为曲线上的精确物理坐标值 $B(t_0)$。细分后两段子曲线的控制点阵列分别为：
- 左段子曲线控制点：$\mathbf{P}_0^{(0)}, \mathbf{P}_0^{(1)}, \dots, \mathbf{P}_0^{(n)}$
- 右段子曲线控制点：$\mathbf{P}_0^{(n)}, \mathbf{P}_1^{(n-1)}, \dots, \mathbf{P}_n^{(0)}$

光栅化引擎利用此递归细分算法，能够完全避免开销巨大的高次求根运算，将复杂的 3 次曲线直接展平成像素级的极微小线段并高速绘制。

---

# 结语：计算机字符学的技术皇冠

通读全部七篇附录可以明证：排版与字形绝非浮于表面的视觉装点，而是一座横跨离散数学、计算几何学、编译器构造与虚拟机底层硬件架构的雄伟科技殿堂。从 1 字节点阵压缩算法的巧妙取舍，到图灵完备虚拟机的精微控制，每一个闪烁在屏幕上的字符，都是现代计算机科学最深沉优雅的见证。

*本附录全卷由 ヴワル魔法図書館（Voile Magic Library）文献翻译工房 严格依据原著技术手稿校对呈现。*
"""

# Convert to Traditional Chinese for zh-hant
zh_hant_app_content = converter.convert(zh_app_content)
zh_hant_replacements = {
    '位圖': '點陣',
    '字體': '字型',
    '貝塞爾': '貝茲',
    '算法': '演算法',
    '內存': '記憶體',
    '字節': '位元組',
    '二進制': '二進位',
    '譯者：[Lycoris <lycorismisaka@gmail.com>]': '譯者：[Lycoris \\<lycorismisaka@gmail.com\\>]',
    '譯者：[Lycoris \\<lycorismisaka@gmail.com\\>]': '譯者：[Lycoris \\<lycorismisaka@gmail.com\\>]',
}
for k, v in zh_hant_replacements.items():
    zh_hant_app_content = zh_hant_app_content.replace(k, v)

zh_app_content = zh_app_content.replace('[Lycoris <lycorismisaka@gmail.com>]', '[Lycoris \\<lycorismisaka@gmail.com\\>]')
zh_hant_app_content = zh_hant_app_content.replace('[Lycoris <lycorismisaka@gmail.com>]', '[Lycoris \\<lycorismisaka@gmail.com\\>]')

with open('docs/zh/fonts-encodings/appendices.md', 'w', encoding='utf-8') as f:
    f.write(zh_app_content)
print(f"Updated docs/zh/fonts-encodings/appendices.md, length: {len(zh_app_content)}")

with open('docs/zh-hant/fonts-encodings/appendices.md', 'w', encoding='utf-8') as f:
    f.write(zh_hant_app_content)
print(f"Updated docs/zh-hant/fonts-encodings/appendices.md, length: {len(zh_hant_app_content)}")
