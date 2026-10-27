---

## C.6 PostScript 字体外部度量规范：AFM、AMFM 与 Windows PFM（Font Metrics Files）

在 PostScript 架构中，字体轮廓程序（`.pfa` 或 `.pfb`）主要由打印机或屏幕 RIP 解释器在光栅化着色阶段执行；而在上层的桌面排版软件（如 PageMaker、QuarkXPress、InDesign）或排版系统（如 $\mathrm{\TeX}$、$\mathrm{Troff}$）中，排版引擎计算行长、折行断字以及字距微调时，**并不需要读取沉重且加密的矢量轮廓字节码，而只需获悉各个字符的纯几何度量数据（Metrics）**。

为此，Adobe 制定了一套完全基于纯 ASCII 文本的工业度量文件标准——**AFM（Adobe Font Metrics）** [22]，以及 Windows 操作系统所专用的二进制派生物 **PFM（Printer Font Metrics）**。

### C.6.1 AFM 文件的全局结构与度量语法

AFM 文件本质上是一份由换行符分隔的键值对与表格流，以 `StartFontMetrics 4.1` 开头，以 `EndFontMetrics` 结尾。其内部结构严格由四大功能段落构成：

#### 1. 全局字体元数据段（Global Font Information）
该段落声明整座字体的宏观物理度量基准与标识字符串：
* **`FontName`**：字体的正式 PostScript 符号名称（如 `Helvetica-Bold`）；
* **`FullName`** 与 **`FamilyName`**：完整人类可读名称与家族族名；
* **`Weight`**：字重（如 `Medium`、`Bold`、`Black`）；
* **`ItalicAngle`**：笔画倾斜角（以度为单位，逆时针方向为负，正体为 `0`，典型斜体为 `-12`）；
* **`IsFixedPitch`**：布尔值，声明是否为等宽字体（`true` 或 `false`）；
* **`FontBBox`**：容纳字体全部字符外边缘的全局外包围盒 `llx lly urx ury`；
* **`UnderlinePosition` 与 `UnderlineThickness`**：下划线的垂直偏移基线深度与笔画粗细；
* **`Version`** 与 **`Notice`**：版本号与版权声明；
* **`EncodingScheme`**：该度量文件所默认绑定的编码方案名称（如 `AdobeStandardEncoding`、`ISOLatin1Encoding` 或 `FontSpecific`）；
* **`CapHeight` 与 `XHeight`**：大写字母字高与小写字母 x 字高；
* **`Ascender` 与 `Descender`**：上升部最高线与下降部最低谷。

#### 2. 单字形微观度量段（Individual Character Metrics）
以 `StartCharMetrics n` 开头（$n$ 为包含的字符总数），以 `EndCharMetrics` 结尾。每一行精确记录一个字形的几何度量，字段之间以分号 `;` 分隔：

```afm
C 65 ; WX 667 ; N A ; B 17 0 650 718 ;
C 102 ; WX 333 ; N f ; B 20 0 382 718 ; L i fi ; L l fl ;
```

关键度量字段的严密物理定义：
* **`C`**：字符在该字体默认编码向量中的十进制编码值（`-1` 代表在默认编码中未被分配码位的字形）；
* **`WX`**（或纵向模式下的 `WY`）：字形的水平排版前进进深宽度（以 1000 设计单位为基准）；
* **`N`**：该字形在 PostScript 字典中的唯一符号名称（如 `A`、`ampersand`）；
* **`B`**：该字形的轴对齐外包围盒 `llx lly urx ury`（左下角点与右上角点坐标）；
* **`L`（连字指令，Ligature Directive）**：声明该字形后继跟随时可自动合成的合字规则（如 `L i fi` 声明当字符 `f` 之后紧跟字符 `i` 时，自动替换为合字 `fi`）。

#### 3. 字距微调对段（Kerning Pairs）
以 `StartKernData` 开头，以 `EndKernData` 结尾。其核心为字偶微调对子表：
```afm
StartKernPairs 350
KPX A V -75
KPX T o -80
KPX W a -60
EndKernPairs
```
每行以 **`KPX`** 关键字引导，声明左侧字形、右侧字形以及沿水平 $x$ 轴施加的度量微调量（以 1000 单位正方形为尺度；负值表示两字靠拢紧缩，正值表示相互推开）。

#### 4. 轨迹字距调整段（Track Kerning）
AFM 规范还支持通过 `StartTrackKern` 声明**轨迹字距（Track Kerning）**，允许排版软件根据文档当前的实际排版字号，线性插值缩放字距松紧度，实现在极小正文字号下自适应放宽字距、在特大标题字号下自适应收紧字距的高级排印物理模型！

### C.6.2 多重母版度量文件：AMFM 与多母版协作

对于多重母版字体（Multiple Master），度量体系由两层架构支撑：
1. **主度量文件（`.amfm`，Adobe Multiple Master Font Metrics）**：声明所有设计轴（Design Axes，如字重轴 Weight、字宽轴 Width、光学尺寸轴 Optical Size）、轴向极值范围、主母版数目、以及用于驱动插值运算的代数混合矩阵（Blend Matrix）；
2. 各个离散极限母版各自附带一份独立的普通 AFM 文件，排版软件根据用户指定的坐标点 $(w_1, w_2, \dots)$ 对所有 AFM 度量执行加权向量线性求和，动态合成当前专属实例的度量数据。

### C.6.3 Windows 二进制打印机度量文件：PFM

在经典的 16 位与 32 位 Windows 操作系统（Windows 3.1/95/98/NT/2000/XP）中，系统内核与 GDI 引擎为了规避解析庞大 ASCII 文本文件的性能惩罚，规定必须将 AFM 文件预先编译为二进制的 **`.pfm`（Printer Font Metrics）** 文件。

一个 PFM 文件由精密的 C 语言二进制结构体打包而成：
- **`dfType`**：字体类型（通常为 `0x0080` 表示 PostScript 栅格驱动）；
- **`dfPoints`** 与 **`dfVertRes` / `dfHorizRes`**：标称点数与设计分辨率；
- **`dfAscent`** 与 **`dfInternalLeading` / `dfExternalLeading`**：Windows 经典的字体上升部与行距前导空白；
- **`dfWeight`**：以 1 到 1000 标定的字重整数（400 为常规 Normal，700 为粗体 Bold）；
- **`dfPitchAndFamily`**：等宽/变宽标志位与 Windows 字体家族族群分类码；
- **`dfWidthTable`**：指向 256 位字符宽度表的 32 位文件偏移指针；
- **`dfPairKernTable`**：指向经过二进制结构化排序的字距微调对数组的文件偏移量指针。
