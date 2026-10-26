---
title: "附录 A–G：底层格式与数学技术参考全景指南"
description: "涵盖位图字体 (A)、TeX/Omega (B)、PostScript Type 1/CFF (C)、TrueType/OpenType 结构与目录 (D)、METAFONT 与画笔几何 (E/F)、TrueType 虚拟机微指令集、以及曲线微分几何学 (G)。"
---

# 附录 A–G：底层格式与数学技术参考全景指南
### Appendices A–G: Technical Reference Manual for Digital Typography
选自《Fonts & Encodings》附录 A 至 G 全 340 页参考手册
*译者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

本参考手册汇集了《Fonts & Encodings》全书后半部全七大技术附录（Appendices A 至 G）。这部分是雅尼斯·哈拉兰博斯（Yannis Haralambous）为字型工程师、底层排版系统开发者以及数学爱好者构筑的坚实基石，详尽记录了从 20 世纪 80 年代点阵位图格式到 21 世纪现代 OpenType/AAT 容器结构、TrueType 虚拟机约 130 条微指令集、以及曲线微分几何学的全套数学实现与工业级规范。

---

# 附录 A：点阵字体格式（Bitmap Font Formats）

点阵字体（Bitmap Fonts，或称光栅字体 Raster Fonts）是数字印艺与计算机图形显示史上的初始形态。在微处理器计算能力与显示内存极其有限的 1970 至 1980 年代，计算机屏幕与点阵打印机无法承受实时计算三次贝塞尔曲线轮廓的庞大浮点运算，文字必须预先在离散的二维点阵像素网格（Pixel Grid）中逐位绘制，并以紧凑的位图切片（Bitmaps）形式固化于存储介质中。

尽管矢量字体在当今桌面出版领域占据了绝对主导地位，但在嵌入式微控制器、BIOS 启动固件、Linux 虚拟终端控制台、低功耗电子墨水屏以及特种排版软件（如 TeX 引擎的高分辨率物理打印驱动）中，点阵字体格式依然发挥着不可替代的高速直读与亚像素纯度优势。本附录对历史上五大主流点阵字库体系进行彻底的底层二进制解构。

---

## A.1 经典苹果 Macintosh 体系点阵字库（FONT 与 NFNT 资源）

在 1984 年发布的经典 Mac OS（System 1.0 至 Mac OS 9）中，苹果开创性地将文件系统划分为**数据分支（Data Fork）**与**资源分支（Resource Fork）**。字库并非存储为普通的平面文件，而是作为具名资源直接封装在资源分支中。

Mac OS 中的点阵字型主要由两类资源承载：
* **`FONT` 资源**：早期系统标准，资源 ID 直接编码了字体家族号（Family ID）与点数磅重（Point Size）：$\text{Resource ID} = \text{Family ID} \times 128 + \text{Point Size}$；
* **`NFNT`（New Font Numbering Table）资源**：由于 `FONT` 架构仅支持最多 256 个字体家族，苹果推出了 `NFNT` 资源，打破了 ID 与字号的直接耦合，支持多达 16,000 个独立字族，并允许携带专有颜色查找表。

### 1. FontRec 核心二进制结构体
无论 `FONT` 还是 `NFNT`，其核心数据载荷均严格遵循由 QuickDraw 图形引擎定义的 `FontRec` 结构体：

```c
struct FontRec {
    uint16 fontType;        /* 字体属性标志位字（见下文位域解析） */
    uint16 firstChar;       /* 字体支持的首个字符 ASCII 码（通常 0x00 或 0x20） */
    uint16 lastChar;        /* 字体支持的末尾字符 ASCII 码（通常 0xFF） */
    uint16 widMax;          /* 全字体字形的最大外形推进宽度（Advance Width） */
    int16  kernMax;         /* 全字体最大负字距（Negative Kerning，通常 <= 0） */
    int16  nDescent;        /* 负向降部高度（Descent，向下为负值） */
    uint16 fRectWidth;      /* 字体包围盒的最大位图宽度（Bounding Box Width） */
    uint16 fRectHeight;     /* 字体包围盒的最大位图高度（Bounding Box Height） */
    uint16 owTLoc;          /* 偏移量/字宽表（Offset/Width Table）距离本结构体首地址的 16 位字偏移 */
    int16  ascent;          /* 正向升部高度（Ascent，从基线到字身顶端） */
    int16  descent;         /* 降部深度绝对值（Descent，从基线到字身底部） */
    int16  leading;         /* 推荐行间空隙（Leading，行距增量） */
    uint16 rowWords;        /* 位图全景图像（Bit Image）每一扫描行所占的 16 位双字节字数（Words） */
    /* 紧随其后为可变长度数组：
       uint16 bitImage[rowWords * fRectHeight]; 位图图像连续扫描行矩阵
       uint16 locTable[lastChar - firstChar + 3]; 字形横向切片列定位表
       uint16 owTable[lastChar - firstChar + 3];  字宽与字距微调偏移表
    */
};
```

#### `fontType` 属性标志位的精细解构
* **Bit 0 (`propFont`)**：为 0 表示等宽字体（Monospaced），为 1 表示比例可变宽字体（Proportional）；
* **Bit 1 (`colorFont`)**：为 1 表示当前资源为彩色多层位图字；
* **Bit 7 (`synthetic`)**：指示当前字库是否为系统通过算法加粗或倾斜合成的派生字；
* **Bits 2–3 (`depth`)**：位图颜色深度，`00` 代表 1-bit 黑白双色，`01` 代表 2-bit 四阶灰度，`10` 代表 4-bit 十六阶灰度，`11` 代表 8-bit 二百五十六阶灰度。

### 2. 位图切片投影：横向撞击图像（Bit Image Strike）
Mac OS 点阵字体最具天才的设计在于其**连贯横向带状图像（Strike Font）**机制。QuickDraw 并没有将 256 个字母分别存储为 256 张零散的小图片，而是将所有字符按照 ASCII 顺序从左向右**一字排开，水平缝合为一张极其狭长的巨幅全景横向位图**！

::: tip Mac OS 点阵字体 FontRec 内存拓扑与 Strike 位图解构（Figure A-1, A-2, A-3）
![Mac OS 点阵字体 FontRec 内存拓扑（Figure A-1）](/images/fonts-encodings/fig-app-a1.png)
*Mac OS 点阵字体 FontRec 内存拓扑（Figure A-1）*
:::

*图 A-1：Mac OS 点阵字体内部内存布局。从头部 FontRec 结构，到底层 Strike 连贯位图条带与 LocTable 列偏移切片。*

::: tip Mac OS Strike 位图横向切片与黑白像素扫描（Figure A-2）
![Mac OS Strike 位图横向切片（Figure A-2）](/images/fonts-encodings/fig-app-a2.png)
*Mac OS Strike 位图横向切片（Figure A-2）*
:::

*图 A-2：Strike 全景横向位图展示。所有字母按顺序排列在同一张高度为 `fRectHeight` 的位图条带中，宽度由 `rowWords * 16` 决定。*

::: tip Mac OS LocTable 与 OWTable 寻址机制（Figure A-3）
![Mac OS LocTable 与 OWTable 寻址（Figure A-3）](/images/fonts-encodings/fig-app-a3.png)
*Mac OS LocTable 与 OWTable 寻址（Figure A-3）*
:::

*图 A-3：字符在 Strike 图像中的提取流程：通过字符 ASCII 码查 `locTable` 得到起始像素列 $x_{start}$ 与结束像素列 $x_{end}$，瞬间切出单个字母的位图矩阵。*

#### 寻址与提取算法：
1. 欲渲染字符 $C$（$\text{firstChar} \le C \le \text{lastChar}$），其在 `locTable` 中的索引为 $i = C - \text{firstChar}$；
2. 读取该字符在全景图像中的像素列起始坐标：$x_{start} = \text{locTable}[i]$；
3. 读取其后一个条目：$x_{end} = \text{locTable}[i+1]$；
4. 若 $x_{start} == x_{end}$，说明该字符在字库中缺失，QuickDraw 自动跳转至末尾绘制默认未定义符号（Missing Symbol）；
5. 若存在，则字符的物理位图宽度即为 $W = x_{end} - x_{start}$，高度恒定为 `fRectHeight`；
6. 接着查阅 `owTable[i]`：高 8 位为该字形渲染时的左侧负间距（Left Kerning offset），低 8 位为绘制后的排版光标前进量（Advance Width）。QuickDraw 仅需一次位块传输（BitBlt）指令，即可将该矩形切片精准印入帧缓冲区！

---

## A.2 PC 与 Windows 体系点阵字库（DOS CPI 与 Windows FNT/FON）

在 IBM PC 兼容机与微软 DOS/Windows 发展史上，点阵字体经历了从 BIOS 硬件 ROM 固化，到 DOS 动态代码页切换，再到 Windows 早期图形环境的演进。

### 1. DOS 代码页信息文件（CPI: Code Page Information）
在 MS-DOS 3.3 引入多语言支持后，系统通过 `CPI` 文件（如 `EGA.CPI`, `LCD.CPI`）动态为显示适配器（EGA/VGA）的显存刷新硬件点阵字体：
* **文件头魔数**：固定前 7 字节为 `0xFF, 'F', 'O', 'N', 'T', ' ', ' '`；
* **指针链表**：包含指向各个代码页块（如 CP437, CP850）的文件偏移指针；
* **点阵载荷**：每个字符通常存储为 8 字节（$8 \times 8$ 点阵）、14 字节（$8 \times 14$ EGA 点阵）或 16 字节（$8 \times 16$ VGA 点阵）的紧凑单色扫描行数组。

### 2. Windows 2.0 / 3.0 光栅字体规范（`.FNT` 与 `.FON`）
在 Windows 3.1 引入 TrueType 之前，Windows 图形设备接口（GDI）完全依赖 `.FNT` 文件。多个尺寸与字重的 `.FNT` 文件最终通过资源链接器被打包为一个动态链接库（DLL）形态的 `.FON` 文件。

`.FNT` 文件由一个庞大的 118 字节（Version 2.0）或 148 字节（Version 3.0）的二进制文件头起始：

```c
#pragma pack(push, 1)
struct WinFNTHeader {
    uint16 dfVersion;            /* 格式版本号：0x0200 (Win 2.x) 或 0x0300 (Win 3.x) */
    uint32 dfSize;               /* .FNT 整个文件的总字节长度 */
    char   dfCopyright[60];      /* ASCII 编码的版权声明字符串 */
    uint16 dfType;               /* 字体类型：0x0000 代表点阵光栅字，0x0001 代表矢量矢量线框字 */
    uint16 dfPoints;             /* 标称设计磅值（Nominal Point Size） */
    uint16 dfVertRes;            /* 设计垂直分辨率（通常 96 DPI） */
    uint16 dfHorizRes;           /* 设计水平分辨率（通常 96 DPI） */
    uint16 dfAscent;             /* 基线至顶端的升部高度（Ascent in pixels） */
    uint16 dfInternalLeading;    /* 内部行距（留给重音符号的空间） */
    uint16 dfExternalLeading;    /* 外部行距（推荐的额外空隙） */
    uint8  dfItalic;             /* 斜体标志位（1 为斜体） */
    uint8  dfUnderline;          /* 下划线标志位 */
    uint8  dfStrikeOut;          /* 删除线标志位 */
    uint16 dfWeight;             /* 字重（100 Thin 至 900 Black，400 为 Regular） */
    uint8  dfCharSet;            /* 字符集代码（0: ANSI, 1: Default, 2: Symbol, 128: Shift-JIS） */
    uint16 dfPixWidth;           /* 等宽字体的像素宽度（若为 0 则为比例变宽字体） */
    uint16 dfPixHeight;          /* 字符全高的像素数（Scanlines） */
    uint8  dfPitchAndFamily;     /* 变宽/等宽标志与字族分类（Serif, Sans-serif 等） */
    uint16 dfAvgWidth;           /* 小写字母平均宽度 */
    uint16 dfMaxWidth;           /* 字体中最大字形宽度 */
    uint8  dfFirstChar;          /* 首个支持的字符码点（通常 32 空格） */
    uint8  dfLastChar;           /* 最后一个字符码点（通常 255） */
    uint8  dfDefaultChar;        /* 替代缺失字符的默认字符偏移量 */
    uint8  dfBreakChar;          /* 用于断行分词的空格字符偏移量 */
    uint16 dfWidthBytes;         /* 每一行扫描线在内存中对齐的单行字节数（必须为双字节偶数倍） */
    uint32 dfDevice;             /* 指向目标设备名称字符串的文件内字节偏移 */
    uint32 dfFace;               /* 指向字体家族名称字符串（如 "System", "Terminal"）的文件内偏移 */
    uint32 dfBitsPointer;        /* 运行时内存中的位图指针（文件中填 0） */
    uint32 dfBitsOffset;         /* 位图数据阵列距离文件头的绝对字节偏移量！ */
    /* Windows 3.0 (dfVersion == 0x0300) 额外包含扩展字段： */
    uint8  dfByteFlags;          /* 位图打包与内存管理标志 */
    uint32 dfColorMapOffset;     /* 颜色表偏移量 */
    uint32 dfReserved[4];        /* 保留字段 */
};
#pragma pack(pop)
```

#### 字符偏移表与位图检索机制
紧随头部之后的是字符表（Char Table）：
* **Version 2.0**：每个字符占用 4 字节：`uint16 width; uint16 offset;`
* **Version 3.0**：为了支持超过 64KB 的超大点阵字库，扩展为 6 字节：`uint16 width; uint32 offset;`

当 Windows GDI 需要绘制字符 $C$ 时：
1. 索引到字符条目，读取字宽 `width` 与绝对文件偏移 `offset`；
2. 定位到 `offset` 处的单色位图数据：数据按照从上至下的光栅行连续排列；
3. **列式优先扫描规则**：与常见水平位图不同，Windows 2.x/3.x 的 FNT 格式在某些变体中采用逐列（Column-major）存储或以 8 像素对齐的垂直步进存储，GDI 通过硬件位移指令将字节流直接解包推送到显示适配器显存。

---

## A.3 X Window System 体系规范（BDF 与 PCF）

在 Unix 与 Linux 桌面图形生态（X11）中，点阵字体拥有高度标准化且极为严谨的开放规范。

### 1. BDF 格式（Bitmap Distribution Format）
BDF 是由 Adobe 与 X 联盟（X Consortium）制定的**纯 ASCII 纯文本点阵字体交换规范**（版本为 2.1 与 2.2）。它不依赖任何特定 CPU 架构的字节序（Endianness），可读性极强，被全人类开源字型设计社区广泛作为点阵字体设计的通用源码格式。

一个正规的 BDF 文件由全局头部声明、X11 逻辑字体描述符（XLFD）属性字典、以及逐个字符的十六进制扫描线块构成：

```bdf
STARTFONT 2.1
FONT -Adobe-Courier-Medium-R-Normal--14-100-100-100-M-90-ISO8859-1
SIZE 10 100 100
FONTBOUNDINGBOX 9 14 -1 -3
STARTPROPERTIES 18
FOUNDRY "Adobe"
FAMILY_NAME "Courier"
WEIGHT_NAME "Medium"
SLANT "R"
SETWIDTH_NAME "Normal"
ADD_STYLE_NAME ""
PIXEL_SIZE 14
POINT_SIZE 100
RESOLUTION_X 100
RESOLUTION_Y 100
SPACING "M"
AVERAGE_WIDTH 90
CHARSET_REGISTRY "ISO8859"
CHARSET_ENCODING "1"
CAP_HEIGHT 10
X_HEIGHT 7
FONT_ASCENT 11
FONT_DESCENT 3
ENDPROPERTIES
CHARS 256
STARTCHAR A
ENCODING 65
SWIDTH 600 0
DWIDTH 9 0
BBX 9 11 0 0
BITMAP
0000
0C00
1E00
3300
3300
6180
7F80
6180
6180
E0C0
0000
ENDCHAR
ENDFONT
```

#### BDF 核心字段数学语义解析：
* `SWIDTH sx sy`：可缩放宽度（Scalable Width）。以 $1/1000$ 磅（Em）为单位。计算公式为：$\text{SWIDTH} = \frac{\text{DWIDTH}}{\text{Point Size} \times \frac{\text{Resolution}}{72.27}} \times 1000$；
* `DWIDTH dx dy`：设备宽度（Device Width）。字符被绘制后，排版光标在屏幕物理像素上的位移增量向量（横排文字时 $dy=0$）；
* `BBX width height x_off y_off`：字符位图的紧包围盒（Bounding Box）：
  * `width`：位图实际具有墨迹像素的横向列数；
  * `height`：位图实际具有墨迹的垂直行数；
  * `x_off`：从逻辑原点（0,0）到包围盒左边缘的水平像素偏移（左侧轴承 LSB）；
  * `y_off`：从逻辑基线到包围盒底边缘的垂直像素偏移（下降为负值）；
* `BITMAP`：每行一个十六进制整数字符串。若 `width` 为 9，则该行需要 2 个十六进制双字节（16 位）表示，多余的低位填充 0。

### 2. PCF 格式（Portable Compiled Format）
BDF 作为文本格式，解析效率低下，体积庞大。X11 在启动加载时，会通过 `bdftopcf` 工具将 BDF 编译为**PCF（Portable Compiled Format）二进制文件**。

PCF 文件由一个**块目录（Table Directory）**管理整个文件的物理分块，具有极高的动态扩展性：
* **文件头魔数**：固定为 4 字节：`0x70, 0x63, 0x66, 0x01`（字符串 `\x01fcp`）；
* **`table_count`**：文件中包含的独立子表总数；
* **子表目录项**：
  ```c
  struct PCFTableEntry {
      uint32 type;        /* 子表类型位域掩码（见下文） */
      uint32 format;      /* 格式控制字：包含字节序（MSB/LSB）、字长（1/2/4字节）、压缩标志 */
      uint32 size;        /* 子表在文件中的原始字节大小 */
      uint32 offset;      /* 子表距离文件头的绝对字节偏移量 */
  };
  ```

#### PCF 核心子表类型掩码：
* `PCF_PROPERTIES (1<<0)`：继承自 BDF 的全部 XLFD 元数据键值对；
* `PCF_ACCELERATORS (1<<1)`：加速器度量（全字体是否有常数宽度、最大最小边界等，允许 X Server 跳过逐字计算）；
* `PCF_METRICS (1<<2)`：每一个字形的 `leftSideBearing`, `rightSideBearing`, `characterWidth`, `ascent`, `descent`, `attributes`；
* `PCF_BITMAPS (1<<3)`：全字体所有字形的纯位图数据载荷阵列；
* `PCF_INK_METRICS (1<<4)`：字符墨迹的真实几何边界；
* `PCF_BDF_ENCODINGS (1<<5)`：字符编码映射表（包含多字节字符集如 GB2312, JISX0208）；
* `PCF_SWIDTHS (1<<6)`：可缩放宽度表；
* `PCF_GLYPH_NAMES (1<<7)`：所有字符的 PostScript 符号名称字符串池。

由于 PCF 在 `format` 字段中显式标明了子表采用大端序（Big-Endian）还是小端序（Little-Endian），X Server 在载入字库时可直接通过 `mmap` 系统调用将字库无缝映射到内存空间，实现接近零开销的瞬时字形索引！

---

## A.4 TeX 体系专用点阵格式（GF 与 PK）

高德纳（Donald Knuth）在研发 TeX 与 METAFONT 系统时，为了使排版结果在不同的操作系统与输出设备上保持**严格不可动摇的数学一致性**，设计了两大标志性的点阵格式：**GF（Generic Font）** 与 **PK（Packed Font）**。

### 1. GF 格式（Generic Font）
GF 是 METAFONT 编译轮廓方程并光栅化输出的初级二进制中间产物。GF 并非简单的位图转储，而是一套**基于一维游程编码（Run-Length Encoding）的微型光栅机虚拟机字节码流**！

GF 拥有多达 256 个操作码（Opcodes），以高度精简的流式状态机控制虚拟画笔：
* `paint_0` 至 `paint_63`（操作码 0–63）：指令操作码本身的值即代表连续绘制黑像素（Black Pixels）的个数（0 到 63 个），画笔自动右移并交替翻转颜色状态；
* `paint1` 至 `paint4`（操作码 64–67）：后接 1 至 4 字节无符号整数，用于绘制超长连续像素段；
* `boc`（操作码 68，Begin of Character）：开启一个全新字符，后接字符码点、前向指针与该字符包围盒的完整浮点度量；
* `boc1`（操作码 69）：精简版字符起始指令（针对普通小字符优化，减少参数字节）；
* `eoc`（操作码 70，End of Character）：终结当前字符；
* `skip0` 至 `skip3`（操作码 71–74）：行末换行指令，将光标跳到下方指定距离的扫描行起始处；
* `new_row_0` 至 `new_row_164`（操作码 75–238）：**超紧凑换行指令**！一条单字节指令同时完成两项工作：换到下一行，并在新行的开头绘制 0 至 164 个白像素；
* `xxx1` 至 `xxx4`（操作码 239–242）：用于在字库中嵌入特殊注释或 METAFONT `special` 扩展指令的透明数据载荷；
* `yyy`（操作码 243）：用于记录字体设计磅重与辅助参数；
* `no_op`（操作码 244）：空操作，用于内存对齐；
* `char_loc`（操作码 245）与 `char_loc0`（操作码 246）：位于文件尾部的字符定位总目录；
* `pre`（操作码 247）：文件前导标识；
* `post`（操作码 248）与 `post_post`（操作码 249）：文件终结签名。

### 2. PK 格式（Packed Font）的高阶动态压缩算法
由于 GF 文件体积相对庞大，Tomas Rokicki 在 1985 年提出了 **PK（Packed Font）格式**。PK 引入了一种革命性的**自适应动态游程压缩算法（Dynamic Run-Length Compression with Parameter $dyn\_f$）**，在保持快速流式解压的同时，将点阵字体体积大幅削减了 50% 以上，成为了全人类 TeX 生态事实上的最终输出标准。

#### PK 字符头（Character Header）结构
每个字符由一个标志字节（Flag Byte）领衔，该字节的高 4 位被赋予了极其关键的数学控制参数：

$$\text{Flag Byte} = (dyn\_f \times 16) + (\text{first\_pixel\_black} \ ? \ 8 : 0) + \text{format\_flag}$$

* $dyn\_f$（取值 0 到 14）：由压缩器计算得出的该字符最优动态截断阈值！若 $dyn\_f == 14$，说明该字符为纯点阵光栅存储（不进行游程压缩）；
* $\text{first\_pixel\_black}$：布尔值，指示当前字符的第一行扫描线的首个像素是黑还是白；
* $\text{format\_flag}$（0 到 7）：指示紧随其后的字符包围盒尺寸采用 1 字节、2 字节还是 4 字节存储。

#### 核心动态半字节（Nybble）解包算法
在解包位图数据时，PK 引擎按 4 位半字节（Nybble，取值 0 到 15）顺序读取字节流。游程长度 $L$（Run-length）的解析完全遵循以下有限状态机：

1. **单半字节情况**：若读到的半字节 $N < dyn\_f$：
   则该游程长度直接等于 $N$：$L = N$；
2. **双半字节情况**：若读到的半字节 $dyn\_f \le N \le 13$：
   则必须紧接着读取下一个半字节 $N_2$，游程长度由两位基数混合计算：
   $$L = (N - dyn\_f - 1) \times 16 + N_2 + dyn\_f + 1$$
3. **三半字节情况**：若读到的半字节 $N == 14$：
   则连续读取后两个半字节 $N_2$ 与 $N_3$：
   $$L = (N_2 - 16) \times 16 + N_3 + dyn\_f + 1$$
4. **多行重复标志（Repeat Count）**：若读到的半字节 $N == 15$：
   **并不产生像素位移**！而是读取随后的游程数据，指示紧随其后的扫描行在垂直方向上重复绘制若干次！这在处理垂直平直笔画（如字母 `'l'`、`'H'` 的坚硬立柱）时，实现了近乎无限大的压缩比！

#### 工业级 Python PK 解包器实现
以下给出遵循 Knuth 标准规范的 PK 游程解析核心算法实现：

```python
def unpack_pk_runs(nybble_stream, dyn_f, first_pixel_black, total_pixels):
    """
    解压 PK 字符点阵游程流
    :param nybble_stream: 生成器，逐个产出 0-15 的 4-bit 整数
    :param dyn_f: 动态阈值 (0-14)
    :param first_pixel_black: 首像素极性
    :param total_pixels: 字符总像素数 (width * height)
    :return: 展开后的 0/1 像素一维数组
    """
    pixels = []
    is_black = first_pixel_black
    repeat_count = 0
    
    while len(pixels) < total_pixels:
        nyb = next(nybble_stream)
        
        # 状态 1: 扫描行重复计数
        if nyb == 15:
            # 读取重复因子
            repeat_count = next(nybble_stream)
            continue
            
        # 状态 2: 单半字节短游程
        if nyb < dyn_f:
            run_length = nyb
        # 状态 3: 双半字节中游程
        elif nyb <= 13:
            nyb2 = next(nybble_stream)
            run_length = (nyb - dyn_f - 1) * 16 + nyb2 + dyn_f + 1
        # 状态 4: 三半字节长游程
        elif nyb == 14:
            nyb2 = next(nybble_stream)
            nyb3 = next(nybble_stream)
            run_length = (nyb2 - 16) * 16 + nyb3 + dyn_f + 1
            
        # 将当前颜色的像素追加到结果流
        pixel_val = 1 if is_black else 0
        pixels.extend([pixel_val] * run_length)
        
        # 处理垂直扫描行重复
        if repeat_count > 0:
            row_data = pixels[-run_length:]
            for _ in range(repeat_count):
                pixels.extend(row_data)
            repeat_count = 0
            
        # 翻转像素颜色状态 (黑 <-> 白)
        is_black = not is_black
        
    return pixels[:total_pixels]
```

通过这一套极其精密且针对字符形态深度优化的数学状态机，高德纳与 Rokicki 将二十世纪点阵字型的压缩理论推向了终极的物理极限。
---

## A.5 Windows 3.0 矢量与光栅字体 `.FNT` 二进制头表全集

在 Windows 3.0 中，微软将 `.FNT` 资源头扩展为 118 字节的庞大结构体，成为了工业界 16 位与 32 位嵌入式设备的标准点阵参考规范：

```c
#pragma pack(push, 1)
struct Win30FontHeader {
    uint16 dfVersion;           /* 0x0300 代表 Windows 3.0 */
    uint32 dfSize;              /* 包含头部的物理文件总字节大小 */
    char   dfCopyright[60];     /* 60 字节定长版权 ASCII 字符串 */
    uint16 dfType;              /* 0 代表点阵位图光栅字，1 代表早期矢量矢量字 */
    uint16 dfPoints;            /* 设计标称点数磅值 (Point Size) */
    uint16 dfVertRes;           /* 垂直标称设计分辨率 (通常 96 DPI) */
    uint16 dfHorizRes;          /* 水平标称设计分辨率 (通常 96 DPI) */
    uint16 dfAscent;            /* 基线到字形包围盒顶部的距离 (升部) */
    uint16 dfInternalLeading;   /* 字身内部预留重音符号间距 */
    uint16 dfExternalLeading;   /* 行与行之间的推荐外部空隙 */
    uint8  dfItalic;            /* 非零代表斜体 */
    uint8  dfUnderline;         /* 非零代表下划线 */
    uint8  dfStrikeOut;         /* 非零代表删除线 */
    uint16 dfWeight;            /* 字重数值 (100..900, 400 为 Normal, 700 为 Bold) */
    uint8  dfCharSet;           /* 字符集 (0: ANSI, 1: Default, 2: Symbol, 128: Shift-JIS) */
    uint16 dfPixWidth;          /* 若为 0 表示比例变宽字；若非 0 表示全字固定点阵宽度 */
    uint16 dfPixHeight;         /* 点阵像素矩阵的物理总高度 */
    uint8  dfPitchAndFamily;    /* 字体族与间距标志 */
    uint16 dfAvgWidth;          /* 小写字母加权平均宽度 */
    uint16 dfMaxWidth;          /* 字体中最大的字符位图宽度 */
    uint8  dfFirstChar;         /* 支持的首个字符 ASCII 编码 */
    uint8  dfLastChar;          /* 支持的末尾字符 ASCII 编码 */
    uint8  dfDefaultChar;       /* 缺失字符替代符偏移 */
    uint8  dfBreakChar;         /* 单词断句空格字符偏移 */
    uint16 dfWidthBytes;        /* 位图扫描行对齐字节数 */
    uint32 dfDevice;            /* 指向目标设备名称字符串的相对文件偏移量 */
    uint32 dfFace;              /* 指向字体家族名称（如 "Arial"）的相对文件偏移量 */
    uint32 dfBitsPointer;       /* 内存中点阵位图矩阵的绝对地址（文件中预留为 0） */
    uint32 dfBitsOffset;        /* 点阵位图位流相对于文件开头的 32 位绝对字节偏移 */
    uint8  dfReserved;          /* 预留字节 */
    uint32 dfFlags;             /* 标志位 */
    uint16 dfAspace;            /* A 空间间隙（左侧负轴承补偿） */
    uint16 dfBspace;            /* B 空间间隙（位图黑体宽度） */
    uint16 dfCspace;            /* C 空间间隙（右侧轴承补偿） */
    uint32 dfColorPointer;      /* 彩色位图调色板偏移 */
    uint32 dfReserved1[4];      /* 预留对齐填充字 */
};
#pragma pack(pop)
```

通过这一结构，Windows GDI 能够以纳秒级的极速在屏幕显存（FrameBuffer）中直接执行 `BitBlt` 块内存拷贝，奠定了早期个人电脑视窗图形界面飞速普及的性能基础。
---

## A.6 DOS 代码页信息文件（`.CPI`）的段落拓扑与显卡固件注入

在微软 MS-DOS 与 IBM PC-DOS 时代，操作系统为了在 EGA 与 VGA 图形显示适配器上切换不同的国家/地区字符集（如代码页 437 美国英语、850 西欧多语言、936 简体中文），采用了专有的 **`.CPI`（Code Page Information）** 点阵字体封装容器。

### 1. CPI 文件的四级二进制树状拓扑：
一个标准的 `.CPI` 文件在物理上由四大层级构成：
1. **Font File Header（字体文件头）**：
   * `0x19` 字节魔数：`\xFF\x46\x4F\x4E\x54\x20\x20`（"FONT  "）；
   * 预留字段与版本号；
   * `pCodePageEntry`：指向首个代码页条目的文件绝对字节偏移。
2. **Code Page Entry Header（代码页条目头）**：
   * `next`：指向下一个代码页条目的指针（为 0 表示链表末尾）；
   * `device_type`：目标硬件设备代码（1: 屏幕显示适配器 Screen; 2: 针式/激光打印机 PRN）；
   * `device_name`：8 字节 ASCII 设备名称（如 `"EGA     "` 或 `"4201    "`）；
   * `codepage_id`：DOS 代码页整数编号（如 437, 850, 852）；
   * `pFontInfo`：指向具体字体信息的偏移量。
3. **Font Info Header（点阵字体信息头）**：
   * `version`：字体格式版本号；
   * `num_fonts`：该代码页下封装的不同像素规格点阵字体总数（通常为 3 种：$8 \times 8$, $8 \times 14$, $8 \times 16$）。
4. **Screen Font Data（屏幕点阵原始字节矩阵）**：
   * 存储每个字符的点阵位图。例如对于标准的 $8 \times 16$ VGA 字体，每个字符占用 16 个连续字节（每行 8 像素占用 1 字节）。256 个字符恰好占用：
     $$256 \times 16 \text{ 字节} = 4096 \text{ 字节} = 4 \text{ KB}$$
   DOS 的 `MODE CON: SELECT=...` 命令正是将这 4KB 数据通过显卡 BIOS 中断（`INT 10h, AX=1100h`）直接写入 VGA 显卡的字符发生器内存平面 2（Plane 2），实现了纯硬件级的即时字符渲染！

---

## A.7 X11 PCF 二进制结构与快速加载优化

在 X Window System 诞生初期，虽然 BDF 纯文本格式极其易读，但每次 X 终端启动或切换字号时，解析数十万行 ASCII 文本并将其转换为二进制点阵极为耗时。

DEC、MIT 与 X 联盟推出了 **PCF（Portable Compiled Format）** 格式：
* PCF 预先在磁盘上完成了大小端字节序重排、4 字节内存页对齐、以及各字符包围盒的微积分计算；
* 操作系统启动 X Server 时，只需发起一次底层的 `mmap` 系统调用，即可将全字体瞬间映射至 X11 核心显存，比 BDF 文本解析提速了整整两百倍！
---

## A.8 TeX 通用字体格式（GF: Generic Font）核心操作码全集

高德纳在设计 METAFONT 时的原始输出格式为 **`.gf`（Generic Font）**。与后续深度压缩的 `.pk` 格式相比，GF 格式更加直接贴近光栅扫描硬件：

| 操作码（Hex/Dec） | 助记符 | 参数形态 | 光栅化绘制与解释器行为 |
| :--- | :--- | :--- | :--- |
| `0..63` | `paint_0..paint_63` | 无额外参数 | 在当前行交替绘制 $0 \dots 63$ 个连续同色像素（黑/白翻转） |
| `64..66` | `paint1..paint3` | $k$ 字节无符号数 | 绘制长达数万像素的连续黑白游程（参数占用 1 到 3 字节） |
| `67` | `boc` (Begin of Char) | 四元包围盒与字符代码 | **字符开启首指令**：初始化字符最小最大 $X, Y$ 坐标与字符码点 |
| `68` | `boc1` | 紧凑型字符开始 | 单字节字符编码且包围盒尺寸极小时的紧凑格式 |
| `69` | `eoc` (End of Char) | 无 | **字符终结指令**：完成当前字符点阵的绘制，将像素提交输出缓存 |
| `70` | `skip0` | 无 | 结束当前扫描行，并将画笔移至下一行起始位置（垂直 $Y$ 减 1） |
| `71..73` | `skip1..skip3` | $k$ 字节整数 | 跨越多行全白空白行（垂直 $Y$ 连续跳跃若干行） |
| `74` | `new_row_0` | 无 | 换行并将当前行横坐标 $X$ 重置为 0 |
| `243` | `post` (Postamble) | 全局元数据指针 | 字体尾部引导表，存储指向各字符 `char_loc` 索引的绝对文件指针 |
| `248` | `post_post` | 魔数字节与识别符 | **全文件收尾标识**：后随 4 字节或更多 `0xDF`（十进制 223）特征对齐字节 |

GF 格式凭借其极度的直观性与严格的时序一致性，成为了 DVI 驱动程序验证点阵字库光栅完整性的第一标准。

---

# 附录 B：TeX 与 Omega 字体度量文件规范（TFM, OFM, VF, OVF）

在计算机排版技术史上，高德纳（Donald Knuth）在设计 TeX 系统时提出了一个彻底超越时代的软硬件解耦范式：**排版排版引擎在计算段落折行、数学公式排版与页面微积分模型时，根本不需要知道字形的长相（轮廓或位图），而仅仅需要知道字符的几何度量盒模型（Metrics Box Model）！**

这一哲学造就了 **TFM（TeX Font Metric）** 格式。在排版过程中，TeX 仅读取极小体积的 `.tfm` 二进制文件（通常仅几千字节），极大地降低了内存消耗并提升了排版速度；字形的实际绘制轮廓则完全延迟到设备驱动程序（DVI 驱动、dvips、pdfTeX）在最终输出纸张或屏幕时才进行绑定。随后，雅尼斯·哈拉兰博斯（Yannis Haralambous）与约翰·普莱斯（John Plaice）在开发多语言多方向排版系统 Omega 时，将 TFM 进一步发展为支持 16 位与 32 位 Unicode 全量字符空间的 **OFM（Omega Font Metrics）** 与 **OVF（Omega Virtual Fonts）**。

---

## B.1 TFM 文件的 12 张核心数据表与二进制拓扑

一个标准的 TFM 文件在磁盘上被组织为严格紧凑的 12 个二进制数组。所有多字节整数一律采用大端序（Big-Endian / Network Byte Order）存储：

```
+-------------------------------------------------------+
|  0: lf (Length of File, 16-bit)                       |
|  1: lh (Length of Header data, 16-bit)                |
|  2: bc (Smallest character code in font, 16-bit)      |
|  3: ec (Largest character code in font, 16-bit)       |
|  4: nw (Number of words in width table, 16-bit)       |
|  5: nh (Number of words in height table, 16-bit)      |
|  6: nd (Number of words in depth table, 16-bit)       |
|  7: ni (Number of words in italic table, 16-bit)      |
|  8: nl (Number of words in lig/kern table, 16-bit)    |
|  9: nk (Number of words in kern table, 16-bit)        |
| 10: ne (Number of words in extensible table, 16-bit)  |
| 11: np (Number of font parameter words, 16-bit)       |
+-------------------------------------------------------+
|  HEADER (lh words): Checksum, Design Size, etc.       |
+-------------------------------------------------------+
|  CHAR_INFO (ec - bc + 1 words): 4 bytes per char      |
+-------------------------------------------------------+
|  WIDTH (nw words): fix_word fractional dimensions     |
+-------------------------------------------------------+
|  HEIGHT (nh words): fix_word fractional dimensions    |
+-------------------------------------------------------+
|  DEPTH (nd words): fix_word fractional dimensions     |
+-------------------------------------------------------+
|  ITALIC (ni words): fix_word fractional dimensions    |
+-------------------------------------------------------+
|  LIG_KERN (nl words): Ligature & Kerning bytecode     |
+-------------------------------------------------------+
|  KERN (nk words): fix_word kerning amounts            |
+-------------------------------------------------------+
|  EXTEN (ne words): Extensible delimiter recipes       |
+-------------------------------------------------------+
|  PARAM (np words): Font-wide design parameters        |
+-------------------------------------------------------+
```

### 1. 定点数数学体系：`fix_word` 的微积分精度
TFM 文件内部所有的尺寸量度（字宽、字高、字深、字距、数学参数）均采用 32 位有符号定点数 **`fix_word`** 存储。其内部结构为一个包含 1 个符号位、11 个整数位与 20 个二进制小数位的定点数：

$$1\text{ fix\_word} = \frac{\text{Value}}{2^{20}} = \frac{\text{Value}}{1,048,576} \times (\text{Design Size})$$

#### `fix_word` 的三大物理法则：
1. `fix_word` 并不是绝对的物理毫米或点数，而是一个**相对于字体标称设计尺寸（Design Size）的无量纲相对缩放因子**！
2. 内部数值 $1,048,576$（即十六进制 `0x00100000`）精确代表相对倍率 $1.0$；
3. 其数值分辨率达到了惊人的 $\frac{1}{1,048,576} \approx 9.5367 \times 10^{-7}$，即便在将字体放大至数千磅的巨幅海报排版中，也能确保累加舍入误差绝对小于一个光栅点阵像素！

### 2. `CHAR_INFO` 四字节位域的极致紧凑打包
在 TFM 中，从 `bc` 到 `ec` 的每一个字符仅占用整整 4 个字节（一个 32 位机器字），高德纳通过极其巧妙的位域切片，将四维信息彻底压缩于其中：

```
+----------------+--------+--------+------------+-----+----------------+
|  width_index   | height | depth  |   italic   | tag |   remainder    |
|    (8 bits)    | (4 bit)| (4 bit)|  (6 bits)  | (2) |    (8 bits)    |
+----------------+--------+--------+------------+-----+----------------+
  Byte 0           Byte 1 (H/D)      Byte 2 (Ital/Tag)   Byte 3
```

* **Byte 0 (`width_index`)**：字宽索引（8 位，0–255）。直接指向 `WIDTH` 数组中该字符的字宽 `fix_word`。注意：`WIDTH[0]` 恒定为 0.0，若字符缺失则索引填 0；
* **Byte 1 高 4 位 (`height_index`)**：字高索引（0–15）。指向 `HEIGHT` 数组中的 16 种字高之一；
* **Byte 1 低 4 位 (`depth_index`)**：字深索引（0–15）。指向 `DEPTH` 数组中的 16 种字深之一；
* **Byte 2 高 6 位 (`italic_index`)**：倾斜校正与数学间距索引（0–63）。指向 `ITALIC` 数组；
* **Byte 2 低 2 位 (`tag`)**：**核心行为标签位（Behavior Tag）**，指示 Byte 3 `remainder` 的解释语义：
  * `tag = 0 (no_tag)`：常规普通字符，`remainder` 字段无意义（填 0）；
  * `tag = 1 (lig_tag)`：**合字与字距链起始**。`remainder` 字段为该字符在 `LIG_KERN` 字节码数组中的第一条指令步长索引；
  * `tag = 2 (list_tag)`：**数学定界符递增链表**。用于数学公式排版，`remainder` 给出比当前字符稍大一号的同形字符 ASCII 码点！例如：小型左括号 '(' 的 `remainder` 指向中型左括号，中型指向大型左括号，大型指向超大型左括号，TeX 据此在行内根据公式高度逐级挑选合适大小的括号；
  * `tag = 3 (ext_tag)`：**无限可伸展定界符配方**。当公式高度超过所有离散预制字符时，`remainder` 指向 `EXTEN` 数组中的一条结构体记录，指示如何使用顶部、中部、底部与重复构件拼装出任意高度的巨型大括号或积分号。

### 3. `LIG_KERN` 虚拟字节码指令集
`LIG_KERN` 表是一个包含了连字融铸与成对字距调整的微型执行引擎。每条指令占用 4 个字节：

```c
struct LigKernStep {
    uint8 skip_byte;    /* 跳跃控制字节：若 >= 128 则为停机指令（Stop Step） */
    uint8 next_char;    /* 预期紧随其后的相邻字符码点 */
    uint8 op_byte;      /* 操作码字节：若 >= 128 则为字距微调；若 < 128 则为合字替换 */
    uint8 remainder;    /* 结果：目标字距在 KERN 表中的索引，或新合成的合字码点 */
};
```

#### 指令执行状态机算法：
1. 欲评估字符对 $(C_1, C_2)$ 是否存在连字或字距调整，首先检查 $C_1$ 的 `tag` 是否等于 1；
2. 若是，令指令指针 $p = \text{remainder}(C_1)$，进入 `LIG_KERN` 数组循环：
   * 读取当前步骤：`skip = LIG_KERN[p].skip_byte`；
   * 若 `LIG_KERN[p].next_char == C2`，说明**规则命中**！
     * 若 `op_byte >= 128`：触发**字距微调（Kern）**！间隙值等于 $\text{KERN}[256 \times (\text{op\_byte} - 128) + \text{remainder}]$；
     * 若 `op_byte < 128`：触发**合字替换（Ligature）**！替换后生成的新字符为 `remainder`，同时 `op_byte` 的位域指示是否继续消耗后续字符；
     * 执行完毕，退出状态机；
   * 若未命中：
     * 若 `skip >= 128`：说明到达链表末端（Stop），规则未匹配，退出；
     * 否则令指针跳跃：$p = p + skip + 1$，继续下一轮匹配。

### 4. `PARAM` 全局参数表与数学字体 22 维物理参数
`PARAM` 表定义了该字体的宏观排印物理常数。对于普通正文字体，包含 7 个标准参数：
1. `slant`：字体倾斜率（垂直每上升 1 单位的水平倾斜位移）；
2. `space`：词间标准空格宽度；
3. `space_stretch`：段落两端对齐时允许空格被拉伸的最大弹性限度；
4. `space_shrink`：允许空格被压缩的最大收缩限度；
5. `x_height`：小写字母 'x' 的标准高度；
6. `quad`：一个全角方（Em）的基准设计宽度；
7. `extra_space`：句号等句末标点后推荐额外追加的间隙。

对于**数学符号字体（Math Symbol Fonts）**与**数学扩展字体（Math Extension Fonts）**，高德纳在此扩展了多达 22 个神圣的排印参数：
* `num1`：行间陈列公式（Display style）中分子基线提升高度；
* `num2`：行内文本公式（Text style）中无分数线时的分子提升高度；
* `num3`：行内文本公式中有常规分数线时的分子提升高度；
* `denom1`：行间公式中分母基线压低深度；
* `denom2`：行内公式中分母压低深度；
* `sup1`：行间公式中上标基线抬升量；
* `sup2`：行内正文公式中上标抬升量；
* `sup3`：无下标伴随时的纯上标额外抬升；
* `sub1`：常规下标压低量；
* `sub2`：上标过大时的下标额外避让压低；
* `supdrop`：上标构件顶部距基字的最小投影下沉；
* `subdrop`：下标底部距基字的投影下沉；
* `delim1`：行间公式中定界符（如左大括号）的最小覆盖高度；
* `delim2`：行内公式中定界符的最小高度；
* `axis_height`：数学符号中轴线高度（分数线与减号的绝对垂直中心）。

每一个参数控制着分子分母基线提升、根号连梁厚度、分数线垂直轴心等微积分几何学常量，成为了全球数学印艺不可逾越的黄金规范。

---

## B.2 Omega 字体度量（OFM: Omega Font Metrics）对多语言的扩展

随着计算机排版走向全球化，TFM 基于 8 位 ASCII（最多 256 字符）的设计成为巨大瓶颈。1994 年，哈拉兰博斯与普莱斯在 Omega 项目中制定了 **OFM（Omega Font Metrics）** 规范。

### 1. OFM Level 0：16 位 Unicode 宽字符扩展
OFM Level 0 将字符寻址空间扩展至 16 位整数（支持 65,536 个字符），完整覆盖了当时的 Unicode 基本多语言平面（BMP）：
* 表头头部魔数扩展为 32 位，引入了对多达数十万字节超大度量表的直接物理寻址；
* `CHAR_INFO` 表中的每一个条目从 4 字节扩展为 12 字节甚至更长，彻底解除了 16 种字高与 64 种倾斜校正的位域限制；
* 支持长合字链与上下文敏感的连字评估。

### 2. OFM Level 1：多方向动态排版支持
在 OFM Level 1 中，Omega 引进了突破性的**四向排印物理坐标系统**：
* 文本不仅支持从左向右（L2R），更原生支持从右向左（R2L，如阿拉伯文、希伯来文）、从上到下（T2B，如传统汉字、满文）与从下到上；
* 每个字符内部包含针对四种流动方向的独立包围盒度量向量；
* 引入了基于上下文模式匹配规则表（Contextual Rule Tables），为早期希腊语古籍多重变音符与阿拉伯文字符变形提供了直接度量支持。

---

## B.3 虚拟字体系统（VF 与 OVF）的指令执行引擎

虚拟字体（Virtual Fonts, `.vf` 与 `.ovf`）是 TeX 生态中最具黑客智慧的发明之一。它允许排版师**凭空创造一个物理上根本不存在的“合成字体”**！

### 1. 虚拟字体的架构哲学
假设我们希望排版希腊文，但手头只有一份缺少重音变体字母的 Adobe Times 商业矢量字体，以及一份由 METAFONT 生成的单色重音点阵字体。通过编写一个 `.vf` 虚拟字体映射文件：
* TeX 引擎在排版时，仅仅将该虚拟字体视为一个普通的单一字体；
* 当遇到带重音的希腊字母时，虚拟字体引擎会在后台将其动态展开为一段**微型的 DVI 字节码渲染脚本**：先从物理字体 A 中取出字母轮廓，接着移动绘图原点，再从物理字体 B 中调出重音符号，最后重合输出！

### 2. 虚拟字体的 256 操作码虚拟机指令集
VF 文件内部包含一个完整的微型 DVI 解释器，其核心操作码与 DVI 格式高度同构：
* `set_char_0` 至 `set_char_127`（操作码 0–127）：从当前绑定的物理基字库中绘制指定字符；
* `set_rule`（操作码 132）：直接在页面上绘制一条实心黑矩形连梁或横线（用于分数线与底线）；
* `push`（操作码 141）/ `pop`（操作码 142）：将当前二维绘图坐标 $(x, y)$ 压入硬件栈或从栈中弹出；
* `right1` 至 `right4`（操作码 143–146）：沿水平方向推进指定数量的定点数单位；
* `down1` 至 `down4`（操作码 157–160）：沿垂直方向向下移动；
* `fnt_def1` 至 `fnt_def4`（操作码 243–246）：在虚拟字体内部声明引用的外部真实物理字体（包括字名、校验和与缩放比例）；
* `fnt_num_0` 至 `fnt_num_63`（操作码 171–234）：快速切换当前正在调用的真实底层字体句柄。

### 3. VPL（Virtual Property List）人类可读源码范例
通过 `vptovf` 工具，排版师可将以下人类可读的 `.vpl` 文件直接编译为二进制 `.vf` 与 `.tfm`：

```lisp
(VTITLE An Example Virtual Font for Polytonic Greek)
(DESIGNSIZE R 10.0)
(CHECKSUM O 1234567)
(MAPFONT D 0
   (FONTNAME Times-Roman)
   (FONTCHECKSUM O 1234567)
   (FONTAT R 1.0)
   (FONTDSIZE R 10.0)
   )
(MAPFONT D 1
   (FONTNAME GreekAccents)
   (FONTCHECKSUM O 7654321)
   (FONTAT R 1.0)
   )
(CHARACTER C a
   (CHARWD R 0.5)
   (CHARHT R 0.45)
   (MAP
      (SETCHAR C a)
      )
   )
(CHARACTER O 200 ; Composite alpha with acute accent
   (CHARWD R 0.5)
   (CHARHT R 0.65)
   (MAP
      (PUSH)
      (SETCHAR C a)
      (POP)
      (MOVEUP R 0.2)
      (MOVERIGHT R 0.15)
      (SELECTFONT D 1)
      (SETCHAR C acute)
      )
   )
```

通过这一套极致纯粹的虚拟字体架构，TeX 体系无需重新铸造任何物理字形，即可在排印层实现跨字库的无限无缝熔铸与扩展。
---

## B.4 TeX 数学排版引擎 22 维物理参数的几何代数模型

高德纳在《The TeXbook》附录 G 中，精确公开了 TeX 数学公式排版引擎在二维平面上装配分子、分母、根号连梁与上下标时的微积分几何方程。这些方程直接调用 TFM 中的 `PARAM` 数组参数（在数学符号字体中称为 $\sigma_1 \dots \sigma_{22}$，在数学扩展字体中称为 $\xi_1 \dots \xi_{13}$）：

### 1. 分式（Fractions）分子分母垂直定位方程
对于行间陈列公式（Display Style），分子基线提升量 $u$ 与分母基线下沉量 $v$ 严格按以下不等式组约束：

$$u = \sigma_8 \quad (\text{num1}), \qquad v = \sigma_{11} \quad (\text{denom1})$$

若分子底部与分数线顶部的垂直间隙小于分数线厚度 $\xi_8$（`default_rule_thickness`）的 3 倍，系统强制将分子基线上推：

$$u \longleftarrow \max\left( u, \; \text{depth}(\text{Numerator}) + \frac{3}{2} \xi_8 + \frac{1}{2}\xi_8 + \sigma_{22} \right)$$

其中 $\sigma_{22}$（`axis_height`）是数学公式的中轴线高度。分数线的中心严格锁定在 $y = \sigma_{22}$ 处，彻底保证了无论左右两边的括号、根号多大，分数线永远与等号、减号的水平中轴绝对重合！

### 2. 上标与下标（Superscripts & Subscripts）空间避让算法
设基字高度为 $h$，深度为 $d$：
* 上标初始抬升量：
  * 在行间公式中：$u = \sigma_{13}$（`sup1`）；
  * 在正文行内公式中：$u = \sigma_{14}$（`sup2`）；
  * 若上标为纯紧缩样式（ScriptScript）：$u = \sigma_{15}$（`sup3`）；
* 下标初始下沉量：$v = \sigma_{16}$（`sub1`）；
* **间隙保护不等式**：当上下标同时存在时，上标底部与下标顶部的垂直净距必须满足：
  $$(u - \text{depth}(\text{Sup})) - (-v + \text{height}(\text{Sub})) \ge 4 \xi_8$$
  若不满足，系统强制将下标进一步向下压低，直到间隙等于 $4 \xi_8$，彻底杜绝了复杂数学符号互相粘连的印刷灾难！

---

## B.5 Python 工业级 TFM 二进制解析器实现

```python
import struct

def parse_tfm(data: bytes):
    # 读取 12 个 16 位头表字
    lf, lh, bc, ec, nw, nh, nd, ni, nl, nk, ne, np = struct.unpack(">12H", data[:24])
    print(f"TFM File: {lf} words, Char Range: [{bc}, {ec}]")
    
    offset = 24
    # Header 表 (lh words)
    header = data[offset:offset + lh*4]
    checksum, design_size = struct.unpack(">II", header[:8])
    design_pt = design_size / (1 << 20)
    print(f"Checksum: {checksum:08X}, Design Size: {design_pt:.2f}pt")
    offset += lh * 4
    
    # CHAR_INFO 表 (ec - bc + 1 words)
    num_chars = ec - bc + 1
    char_info = []
    for _ in range(num_chars):
        w_idx, h_d_idx, i_t_idx, rem = struct.unpack(">BBBB", data[offset:offset+4])
        char_info.append({
            'width_index': w_idx,
            'height_index': h_d_idx >> 4,
            'depth_index': h_d_idx & 0x0F,
            'italic_index': i_t_idx >> 2,
            'tag': i_t_idx & 0x03,
            'remainder': rem
        })
        offset += 4
        
    # WIDTH 表 (nw words, 转换为浮点磅值)
    widths = []
    for _ in range(nw):
        val, = struct.unpack(">i", data[offset:offset+4])
        widths.append((val / (1 << 20)) * design_pt)
        offset += 4
        
    return {
        'design_size': design_pt,
        'char_info': char_info,
        'widths': widths
    }
```
---

## B.6 Omega 虚拟字体（OVF）与复杂排版流水线实战

在多语言排版引擎 Omega 中，虚拟字体技术被推向了前所未有的顶峰：
* **多方向字符映射**：针对从右向左书写的阿拉伯字母或自上而下书写的汉字，OVF 内部的 DVI 字节码能够动态调整画笔移动轴向；
* **动态重音合成**：在经典古希腊语多重变音符（Polytonic Greek，包含锐音符、柔音符、强音符、下标角标等多种符号交叠）中，单一物理字体往往缺少组合字形。OVF 在排版时能够自动计算基字包围盒顶部坐标，并动态将变音符吸附在最佳视学位置，消除了传统 TeX 宏包繁琐的纯宏计算。

---

# 附录 C：PostScript 体系字体格式深度参考（Type 1, Type 2/CFF, MM, Type 0, CIDFont）

1984 年，约翰·沃诺克（John Warnock）与查尔斯·格施克（Charles Geschke）创立的 Adobe 公司发布了 **PostScript 页面描述语言**。PostScript 不仅是一套绘图指令，更是一门图灵完备的逆波兰栈式编程语言。随之诞生的 **PostScript Type 1 字体格式**，首次将三次贝塞尔曲线（Cubic Bézier Splines）与高度机密的字体微观渲染提示（Hinting）机制引入数字印刷，彻底催生了人类的桌面出版革命（DTP Revolution）。

在长达十余年的时间里，Adobe 将 Type 1 的核心字节码解释器与加密算法视为最顶级的商业机密，直到 1990 年面对苹果与微软联手推出 TrueType 的巨大竞争压力，才被迫公开出版了著名的黑皮书《Adobe Type 1 Font Format》。本附录基于 PostScript 官方规范，对 Type 1、Type 2（CFF）、Multiple Master、Type 0 复合字体以及当今东亚巨型字库的基石 CID-keyed 字体进行底层的全面技术解密。

---

## C.1 PostScript Type 1 字体的内存拓扑与解密引擎

一个物理上的 Type 1 字体在不同操作系统下有不同的打包载体：
1. **`.PFA`（PostScript Font ASCII）**：纯文本封装格式，常用于 Unix 工作站与通信信道。`eexec` 加密段被编码为两位的十六进制 ASCII 字符串（Hexadecimal-encoded），每行 64 字符；
2. **`.PFB`（PostScript Font Binary）**：二进制封装格式，常用于 IBM PC 与 Windows 系统。文件由若干个带 6 字节二进制头部的记录块（Records）拼接而成；
3. **Mac OS `POST` 资源**：在经典 Mac 操作系统中存储于资源分支（Resource Fork）中的 `POST` 资源段中。

```
+-------------------------------------------------------+
|  .PFB 记录块结构 (Record Header: 6 Bytes)              |
+-------------------------------------------------------+
|  Byte 0:     0x80 (魔数标识符)                          |
|  Byte 1:     记录类型 (0x01: ASCII, 0x02: Binary, 0x03: EOF)
|  Bytes 2-5:  记录长度 (32-bit Little-Endian uint32)    |
|  Bytes 6..N: 载荷数据 (Payload Data)                  |
+-------------------------------------------------------+
```

整个 Type 1 字体由三大逻辑段构成：
1. **ASCII 明文头部段**：包含字体家族声明、版权信息与全局元数据字典；
2. **`eexec` 二进制加密段**：受到伪随机数发生器加密保护的私有核心，包含字体全局微调参数字典 `Private` 与字形轮廓字典 `CharStrings`；
3. **512 字节全零尾部与 `cleartomark` 闭合段**：用于刷新 IBM PC 通信端口与早期激光打印机串口缓冲区。

::: tip PostScript Type 1 字体整体拓扑与 eexec 解密结构（Figure C-1, C-2）
![Type 1 字体整体拓扑（Figure C-1）](/images/fonts-encodings/fig-app-c1.png)
*Type 1 字体整体拓扑（Figure C-1）*
:::

*图 C-1：PostScript Type 1 字体顶层数据字典组织拓扑。从根目录 FontDirectory 到 FontInfo、Encoding、Private 与 CharStrings。*

::: tip Type 1 字体 ASCII 头部与 eexec 加密段（Figure C-2）
![Type 1 字体 eexec 段解构（Figure C-2）](/images/fonts-encodings/fig-app-c2.png)
*Type 1 字体 eexec 段解构（Figure C-2）*
:::

*图 C-2：Type 1 字体物理文件剖分。明文段通过 `currentfile eexec` 关键字瞬间切换为二进制密码流。*

### 1. `eexec` 线性同余解密引擎

进入 `eexec` 关键字后，PostScript 解释器启动一套 16 位线性同余伪随机数发生器（Linear Congruential Generator, LCG）进行实时流式异或解密：

$$R_{n+1} = (R_n \times c_1 + c_2) \bmod M$$

$$P_n = C_n \oplus (R_n \gg 8)$$

* 模数 $M = 65536 = 2^{16}$；
* 乘数 $c_1 = 52845$；
* 增量常数 $c_2 = 22719$；
* **初始密钥 $R_0 = 52845$**（十六进制 `0xCE6D`）；
* $C_n$ 为当前读入的密文字节，$P_n$ 为解密输出的明文字节。

**前 4 个随机字节的丢弃原则**：在 `eexec` 密文的开头，Adobe 强制填充了 4 个完全随机生成的无意义字节。解密引擎在完成前 4 轮循环后，必须将这 4 字节明文直接抛弃，从第 5 个字节开始才是真正的 PostScript 代码。这一设计的目的在于使相同内容的字库在每次导出时呈现完全不同的密文散列，破坏早期密码学者的差分分析！

#### Python 工业级 eexec 解密与加密实现：
```python
def decrypt_type1_cipher(ciphertext: bytes, key: int = 52845, discard: int = 4) -> bytes:
    # PostScript Type 1 线性同余解密算法
    # key = 52845 (eexec) 或 4330 (CharStrings)
    c1 = 52845
    c2 = 22719
    r = key
    plaintext = bytearray()
    for cipher_byte in ciphertext:
        plain_byte = cipher_byte ^ (r >> 8)
        plaintext.append(plain_byte)
        r = ((cipher_byte + r) * c1 + c2) & 0xFFFF
    return bytes(plaintext[discard:])

def encrypt_type1_cipher(plaintext: bytes, key: int = 52845, random_header: bytes = b'\x00\x00\x00\x00') -> bytes:
    # PostScript Type 1 线性同余加密算法
    c1 = 52845
    c2 = 22719
    r = key
    ciphertext = bytearray()
    full_data = random_header + plaintext
    for plain_byte in full_data:
        cipher_byte = plain_byte ^ (r >> 8)
        ciphertext.append(cipher_byte)
        r = ((cipher_byte + r) * c1 + c2) & 0xFFFF
    return bytes(ciphertext)
```

### 2. `FontInfo` 与顶层字典字段全景

在明文段中，`FontDirectory` 注册的顶层字典包含以下核心键值对：
* `FontName`（常字字名符号，如 `/Times-Roman`）；
* `PaintType`（整型：0 为填充笔画，2 为轮廓空心线框）；
* `FontType`（整型：恒为 1）；
* `FontMatrix`（仿射变换矩阵，通常为 `[0.001 0 0 0.001 0 0]`，将 1000 栅格单位归一化为 1 磅）；
* `FontBBox`（四元实数数组：`[llx lly urx ury]`，全字体的左下角与右上角极限包围盒）；
* `UniqueID`（24 位整数，用于激光打印机显存全局光栅缓存索引）；
* `Encoding`（256 元素符号数组，如 `StandardEncoding` 或 `ISOLatin1Encoding`）。

`FontInfo` 子字典则进一步记录了排版与法律元数据：
* `version`：版本号字符串；
* `Notice`：版权所有声明；
* `FullName`：人机可读的完整全名（如 `"Times Roman"`）；
* `FamilyName`：字体家族名（如 `"Times"`）；
* `Weight`：字重描述（`"Regular"`, `"Bold"`, `"Black"` 等）；
* `ItalicAngle`：倾斜角度（正体为 0.0，西文斜体通常为 $-12.0$ 度，负号表示顺时针右倾）；
* `isFixedPitch`：布尔值（等宽字体为 `true`，比例变宽字体为 `false`）；
* `UnderlinePosition`：下划线中心基准线相对于文本基线的垂直偏移（负值）；
* `UnderlineThickness`：下划线的推荐物理宽度。

### 3. `Private` 字典与底层渲染微调中枢

解密后的 `eexec` 内部定义了字体的神经中枢——`Private` 字典。它控制着光栅化渲染器在低分辨率下的所有几何对齐行为：
* **`BlueValues` 与 `OtherBlues`**：基准蓝色对齐带。定义了基线、x 字高、大写字高、升部与降部的平顶吸附区间；
* **`FamilyBlues` 与 `FamilyOtherBlues`**：字体家族全局共享的对齐带，确保同一家族的不同字重在混排时视觉平齐；
* **`BlueScale`, `BlueShift`, `BlueFuzz`**：控制对齐带随显示字号（Point Size）放大时何时解除强行平顶吸附的微调浮点常数；
* **`StdHW` 与 `StdVW`**：全字体的标准主导水平与垂直笔画宽度；
* **`StemSnapH` 与 `StemSnapV`**：允许吸附对齐的多级候选笔画宽度数组；
* **`ForceBold`**：布尔值，在小字号极低分辨率下强行将细笔画加粗一个像素，防止文字笔画断裂消失；
* **`LanguageGroup`**：语言组代码（0 代表拉丁、希腊、西里尔等西文字系；1 代表中日韩繁复汉字字系）；
* **`lenIV`**：指示字形轮廓数据 `CharStrings` 开头包含的随机校验字节数（默认恒为 4；若设为 -1 则表示不加密）。

::: tip Type 1 字体 Private 字典与蓝色对齐带空间分布（Figure C-3, C-4, C-5）
![Private 字典蓝色对齐带（Figure C-3）](/images/fonts-encodings/fig-app-c3.png)
*Private 字典蓝色对齐带（Figure C-3）*
:::

*图 C-3：BlueValues 与 OtherBlues 在基线、x 字高与大写字高周围构筑的垂直吸附禁飞区。*

::: tip StdHW 与 StemSnapH 笔画网格吸附（Figure C-4）
![StdHW 笔画宽度归一化（Figure C-4）](/images/fonts-encodings/fig-app-c4.png)
*StdHW 笔画宽度归一化（Figure C-4）*
:::

*图 C-4：水平主干与垂直主干宽度通过 StemSnap 阵列强行聚类，消除小字号下笔画粗细不均的视觉杂讯。*

::: tip Subrs 子程序池与宏指令复用（Figure C-5）
![Subrs 子程序池（Figure C-5）](/images/fonts-encodings/fig-app-c5.png)
*Subrs 子程序池（Figure C-5）*
:::

*图 C-5：`Subrs` 数组存储了全字体通用的衬线轮廓、弯角弧线与提示替换宏，供所有字形频繁调用。*

---

## C.2 Type 1 CharStrings 虚拟机解释器深度剖析

`CharStrings` 字典内部，每一个字符外观对应一段经过二次加密的二进制字节流。其解密算法与 `eexec` 完全相同，但**初始密钥被替换为 $R_0 = 4330$**。

解密后的字节码在一个深度为 24 的微型数值操作数栈上执行。Type 1 CharStrings 拥有极其精简的操作码体系，划分为单字节基础指令与 `12` 开头的双字节转义指令：

::: tip Type 1 曲线绘制指令与端点切线控制（Figure C-6, C-7, C-8）
![Type 1 曲线绘制指令（Figure C-6）](/images/fonts-encodings/fig-app-c6.png)
*Type 1 曲线绘制指令（Figure C-6）*
:::

*图 C-6：`rrcurveto`、`vhcurveto` 与 `hvcurveto` 指令通过 6 个相对坐标增量定义一段三次贝塞尔曲线。*

::: tip Type 1 闭合路径与内部轮廓填充规则（Figure C-7）
![Type 1 闭合路径（Figure C-7）](/images/fonts-encodings/fig-app-c7.png)
*Type 1 闭合路径（Figure C-7）*
:::

*图 C-7：`closepath` 指令将绘制点连接回当前轮廓的起点，形成封闭区域，并依据非零环绕数规则（Non-zero Winding Rule）进行光栅化填充。*

::: tip Type 1 复合字形 seac 指令构造重音字符（Figure C-8）
![Type 1 seac 指令（Figure C-8）](/images/fonts-encodings/fig-app-c8.png)
*Type 1 seac 指令（Figure C-8）*
:::

*图 C-8：`seac`（Standard Encoding Accented Character）指令通过基字码点与重音码点，瞬间在二维空间将两字合成，大幅节省字体体积。*

### 1. 操作数编码规则（Operand Encoding）
CharStrings 中的每个字节若处于 `32..255` 之间，则被解释为操作数（数值），被直接压入操作数栈：
* `32 <= b0 <= 246`：直接表示整数 $v = b_0 - 139$（范围：$-107 \dots +107$）；
* `247 <= b0 <= 250`：双字节正整数 $v = (b_0 - 247) \times 256 + b_1 + 108$（范围：$+108 \dots +1131$）；
* `251 <= b0 <= 254`：双字节负整数 $v = -(b_0 - 251) \times 256 - b_1 - 108$（范围：$-1131 \dots -108$）；
* `b0 == 255`：随后跟随 4 字节的大端序 32 位有符号整数。

### 2. 核心操作码字典全集

| 操作码（Hex/Dec） | 指令名称 | 参数栈形态 | 几何绘制与虚拟机执行行为 |
| :--- | :--- | :--- | :--- |
| `0x01 (1)` | `hstem` | $y \quad dy$ | 声明一条水平笔画提示（从绝对坐标 $y$ 起，垂直宽度为 $dy$） |
| `0x03 (3)` | `vstem` | $x \quad dx$ | 声明一条垂直笔画提示（从绝对坐标 $x$ 起，水平宽度为 $dx$） |
| `0x04 (4)` | `vmoveto` | $dy$ | 沿垂直轴相对移动当前画笔 $dy$ 距离（水平不移动） |
| `0x05 (5)` | `rlineto` | $dx \quad dy$ | 从当前画笔绘制一条直线至相对坐标 $(dx, dy)$ |
| `0x06 (6)` | `hlineto` | $dx$ | 绘制一条水平直线，距离为 $dx$ |
| `0x07 (7)` | `vlineto` | $dy$ | 绘制一条垂直直线，距离为 $dy$ |
| `0x08 (8)` | `rrcurveto` | $dx_1 dy_1 dx_2 dy_2 dx_3 dy_3$ | 绘制一段三次贝塞尔曲线，三对增量分别为第一控制点、第二控制点与曲线终点 |
| `0x09 (9)` | `closepath` | $\emptyset$ | 闭合当前子路径轮廓 |
| `0x0A (10)` | `callsubr` | $subr\_index$ | 调用 `Subrs` 数组中索引为 $subr\_index$ 的子程序 |
| `0x0B (11)` | `return` | $\emptyset$ | 从当前子程序返回主调用流程 |
| `0x0D (13)` | `hsbw` | $sb_x \quad wx$ | **字形初始化首指令**：设置水平左侧轴承 $sb_x$ 与字符总前进字宽 $wx$ |
| `0x0E (14)` | `endchar` | $\emptyset$ | **字形终结指令**：终结当前字符的绘制，将光栅缓存提交至输出器 |
| `0x15 (21)` | `rmoveto` | $dx \quad dy$ | 二维平面相对移动当前画笔 |
| `0x16 (22)` | `hmoveto` | $dx$ | 沿水平轴相对移动当前画笔 |
| `0x1E (30)` | `vhcurveto` | $dy_1 dx_2 dy_2 dx_3$ | 垂直起刀、水平落刀的简写贝塞尔曲线（首控制点水平位移为 0，终控制点垂直位移为 0） |
| `0x1F (31)` | `hvcurveto` | $dx_1 dx_2 dy_2 dy_3$ | 水平起刀、垂直落刀的简写贝塞尔曲线 |
| `0x0C 0x00` | `dotsection` | $\emptyset$ | 声明进入或退出字符上的点状微小特征（如字母 'i', 'j' 上的圆点） |
| `0x0C 0x01` | `vstem3` | $x_1 dx_1 x_2 dx_2 x_3 dx_3$ | 同时声明三条等距的垂直笔画提示（如字母 'm' 的三根立柱） |
| `0x0C 0x02` | `hstem3` | $y_1 dy_1 y_2 dy_2 y_3 dy_3$ | 同时声明三条等距的水平笔画提示（如字母 'E' 的三根横线） |
| `0x0C 0x06` | `seac` | $asb \quad adx \quad ady \quad bchar \quad achar$ | 标准重音合成：将基字 $bchar$ 与重音 $achar$ 在位移 $(adx, ady)$ 处瞬间拼接 |
| `0x0C 0x07` | `sbw` | $sb_x \quad sb_y \quad wx \quad wy$ | 完整四维轴承设置（包含垂直排版时的垂直轴承与前进高） |
| `0x0C 0x0C` | `div` | $num_1 \quad num_2$ | 整数除法：将栈顶两数弹出并压入商 $num_1 / num_2$ |
| `0x0C 0x10` | `callothersubr` | $arg_1 \dots arg_n \quad n \quad proc$ | 调用解释器底层的驱动级扩展程序（用于 Flex 弧线与动态提示替换） |
| `0x0C 0x11` | `pop` | $\emptyset$ | 将 `callothersubr` 返回的结果从专用暂存器弹出至操作数栈 |

### 3. Flex 弹性微弧算子（Flex Operator）

当字母轮廓中包含极其平缓的浅弧线（例如字母大写 'O' 或加长破折号的微凸弧度）时，在低分辨率屏幕上如果强行光栅化为曲线，往往会因像素阶梯效应产生一个极其丑陋刺眼的孤立凸起像素；而在高分辨率激光照排机上，排版师又必须忠实呈现该优美的弧度。

::: tip Flex 算子几何判据与双轨渲染切换（Figure C-9, C-10）
![Flex 算子几何判据（Figure C-9）](/images/fonts-encodings/fig-app-c9.png)
*Flex 算子几何判据（Figure C-9）*
:::

*图 C-9：Flex 算子的几何控制骨架。包含起点、两个控制点、中途鞍点、以及终点共 7 组二维坐标。*

::: tip Flex 在低分辨率与高分辨率下的不同输出（Figure C-10）
![Flex 双轨渲染（Figure C-10）](/images/fonts-encodings/fig-app-c10.png)
*Flex 双轨渲染（Figure C-10）*
:::

*图 C-10：Flex 动态决策：若该弧度矢高在当前显示设备上折合像素小于等于 0.5 像素（由 `BlueShift` 阈值控制），解释器强制将其退化为一条笔直的水平直线（`rlineto`）；一旦设备分辨率提升使弧度达到 1 像素以上，解释器自动无缝切换为两条平滑拼接的三次贝塞尔曲线！*

### 4. 动态提示替换（Hint Substitution）

在复杂汉字或包含密集笔画的西文符号（如货币符号 '$'、数字 '8'、字母 'B'）中，一个字符从左至右或从上到下存在数十条笔画。由于 Type 1 虚拟机的提示寄存器容量有限，若在字符开头一次性激活所有提示，会导致空间重叠与逻辑死锁。

::: tip 动态提示替换在西文与汉字中的应用（Figure C-11, C-12）
![动态提示替换机制（Figure C-11）](/images/fonts-encodings/fig-app-c11.png)
*动态提示替换机制（Figure C-11）*
:::

*图 C-11：Hint Substitution 通过调用 `callothersubr 3`，在绘制完字符上半部分后，瞬间抹除旧提示并重新声明一套全新的笔画提示集合。*

::: tip 汉字复杂笔画 Hinting 拆解（Figure C-12）
![汉字 Hinting 拆解（Figure C-12）](/images/fonts-encodings/fig-app-c12.png)
*汉字 Hinting 拆解（Figure C-12）*
:::

*图 C-12：在巨型中文字符排版中，Hint Substitution 沿书写笔顺逐笔激活局部提示，彻底消除了笔画粘连。*

---

## C.3 CFF 容器与 Type 2 CharStrings 规范

1996 年，Adobe 在推出 OpenType 架构时，对 Type 1 进行了全方位的现代化重构，推出了 **CFF（Compact Font Format）** 与 **Type 2 CharStrings**：

### 1. CFF 内部索引表（INDEX Table）二进制布局

CFF 彻底废除了 PostScript 文本解释器，采用纯二进制数据布局。其核心是通用的 **INDEX 结构**：
* `uint16 count`：对象总数；
* `uint8 offSize`：偏移数组每个指针占用的字节宽度（1 到 4 字节）；
* `uint<offSize> offset[count + 1]`：累加字节偏移数组；
* `uint8 data[...]`：连续对象二进制载荷。

### 2. CFF 顶层段落拓扑

一个合法的 CFF 表严格按序包含：
1. `Header`：魔数与版本号（通常为 `1.0`，四个字节：`0x01, 0x00, 0x04, 0x04`）；
2. `Name INDEX`：包含的字体家族名称字符串；
3. `Top DICT INDEX`：顶层键值对字典（记录 CharStrings 偏移、编码表偏移、私有字典偏移）；
4. `String INDEX`：全字体共享的字符串池（索引 391 之后自定义字符串）；
5. `Global Subr INDEX`：全局通用子程序池；
6. `Encodings` / `Charsets`：字符编码与字形名称映射；
7. `FDSelect` / `Font DICT INDEX`（针对 CIDFont）：多子字族分类选择表；
8. `CharStrings INDEX`：所有字形的 Type 2 轮廓字节码；
9. `Private DICT`：各字族的局部私有微调字典；
10. `Local Subr INDEX`：局部子程序池。

### 3. Type 2 CharStrings 的颠覆性算子

* **`hintmask` 与 `cntrmask`**：在字形轮廓指令流中间，直接紧随一个根据已声明提示总数决定的位掩码字节数组（例如 24 条提示占用 3 字节）。解释器在 1 字节开销内瞬间激活指定的笔画提示集合，彻底淘汰了 Type 1 繁琐的 `callothersubr 3`！
* **`blend` 算子**：用于支持可变字体（Variable Fonts）与多重母版，在单次计算中完成多个设计母版坐标的线性组合；
* **暂存数组与算术指令**：支持 `put`（将栈顶数存入暂存槽）、`get`（提取暂存数）、`add`, `sub`, `mul`, `div`, `sqrt`, `neg`, `abs`, `random` 等高阶代数运算。

---

## C.4 多重母版字体（Multiple Master Fonts）与连续设计轴

1991 年，Adobe 研发了代表模拟排印巅峰的 **Multiple Master（MM）技术**。MM 允许字体设计师在多维几何空间中建立连续变形轴线：

::: tip Multiple Master 二维与三维设计空间拓扑（Figure C-13, C-14）
![MM 设计空间拓扑（Figure C-13）](/images/fonts-encodings/fig-app-c13.png)
*MM 设计空间拓扑（Figure C-13）*
:::

*图 C-13：由字重轴（Weight: Light to Black）与字宽轴（Width: Condensed to Expanded）构成的二维笛卡尔设计空间。*

::: tip MM 母版轮廓拓扑同构与控制点对应（Figure C-14）
![MM 轮廓拓扑同构（Figure C-14）](/images/fonts-encodings/fig-app-c14.png)
*MM 轮廓拓扑同构（Figure C-14）*
:::

*图 C-14：多重母版插值铁律：参与混配的所有母版字形，其贝塞尔轮廓必须保持**严格绝对的拓扑同构**！即控制点总数、起刀点编号、线段与曲线段的顺序必须逐一精确对应。*

### 多重母版数学插值模型：

设设计空间包含 $k$ 个轴线，空间顶点由 $2^k$ 个极端母版字形 $M_1, M_2, \dots, M_{2^k}$ 锚定。对于用户给定的任意归一化设计坐标 $(w_1, w_2, \dots, w_k) \in [0, 1]^k$，排版引擎通过多线性基函数计算各母版的加权权重 $W_i$：

$$P = \sum_{i=1}^{2^k} W_i M_i, \quad \text{其中 } \sum W_i = 1$$

生成的衍生字形继承了所有母版的优秀基因，在 Adobe Acrobat SuperATM 中实现了对任意未知版面字体的无损克隆！

---

## C.5 Type 0 复合字体（Composite Fonts）

在处理中日韩（CJK）等包含数万汉字的庞大书写系统时，传统 PostScript 字典 256 个字符的上限彻底失效。Adobe 由此设计了 **Type 0 复合字体架构**：

::: tip Type 0 复合字体树状寻址分发体系（Figure C-15）
![Type 0 复合字体分发（Figure C-15）](/images/fonts-encodings/fig-app-c15.png)
*Type 0 复合字体分发（Figure C-15）*
:::

*图 C-15：Type 0 字体的树状解析管线。顶层 Type 0 字体不包含任何轮廓，而是一个路由交换机：通过 `FMapType` 算法将输入的双字节字符编码拆分为高字节与低字节，将高字节作为索引在 `FDepVector`（子字体依赖向量）中查得对应的底层 Type 1 子字库，再用低字节在子字库中提取具体轮廓。*

---

## C.6 CID-keyed 字体体系与 CMap 映射映射学

Type 0 架构虽然解决了字符数量限制，但存在严重的性能缺陷：将汉字硬生生割裂进数十个小字库导致字间距、度量表极度碎片化，且强行绑定了特定的本地化编码（如 Shift-JIS 或 Big5）。

1993 年，Adobe 推出了现代泛东亚字型的终极标准——**CID-keyed 字体（CIDFontType 0 与 CIDFontType 2）**：

::: tip CID-keyed 字符标识符与 CMap 分离架构（Figure C-16, C-17）
![CID 架构图解（Figure C-16）](/images/fonts-encodings/fig-app-c16.png)
*CID 架构图解（Figure C-16）*
:::

*图 C-16：字符集与字形集的彻底解耦。字库内部所有字形按 0 到 65535 的纯数字 CID（Character Identifier）无序线性排列，所有外部编码映射完全交由外挂的 CMap 文件裁决。*

::: tip CMap 文件在多编码环境下的动态映射（Figure C-17）
![CMap 映射机制（Figure C-17）](/images/fonts-encodings/fig-app-c17.png)
*CMap 映射机制（Figure C-17）*
:::

*图 C-17：同一款 CID 字体（如 Adobe-Japan1-6），挂载 `UniJIS-UTF16-H` 即可作为 Unicode 字体使用，挂载 `90ms-RKSJ-H` 即可原生支持日文 Windows Shift-JIS 编码，挂载垂直排版 CMap 即可瞬间激活竖排字形，实现了数字字型史上最伟大的一次架构大一统！*

### 1. CMap 语法规范与映射条目

一个典型的 CMap 文件由以下核心段构成：
```postscript
/CIDInit /ProcSet findresource begin
12 dict begin
begincmap
/CIDSystemInfo 3 dict dup begin
  /Registry (Adobe) def
  /Ordering (Japan1) def
  /Supplement 6 def
end def
/CMapName /UniJIS-UTF16-H def
/CMapVersion 1.018 def
/CMapType 1 def
/UIDOffset 0 def
/XUID [1 10 25330] def
/WMode 0 def % 0 = Horizontal, 1 = Vertical

% 声明编码空间范围 (1 到 4 字节)
1 begincodespacerange
  <0000> <FFFF>
endcodespacerange

% 单字符映射 (Character to CID)
10 beginbfchar
  <0020> 1
  <0021> 2
endbfchar

% 范围连续映射 (Range to CID)
25 begincidrange
  <0022> <005F> 3
  <0060> <007E> 65
endcidrange

endcmap
CMapName currentdict /CMap defineresource pop
end
end
```

通过将字符与字形完全解耦，CMap 文件不仅支持一对一的直接寻址，更通过垂直变体（`V` 系列 CMap）与竖排度量表实现了无缝的纵向书写切换。
---

## C.7 CFF 字典键值与二进制操作码权威词典

在 CFF 容器中，所有的属性字典（Top DICT 与 Private DICT）均采用极其紧凑的**逆波兰键值字节码**存储：操作数（数值）在前，操作符（Operator）在后。单字节操作符占用 `0..21`（除 12 外），双字节操作符以 `12` 开头。

### 1. Top DICT 核心操作符全集：

| 操作符字节（Hex） | 键名（Key Name） | 参数类型 | 默认值 | 语义与排印功能 |
| :--- | :--- | :--- | :--- | :--- |
| `0x00 (0)` | `version` | SID (String ID) | 无 | 字体版本字符串索引 |
| `0x01 (1)` | `Notice` | SID | 无 | 版权声明字符串索引 |
| `0x02 (2)` | `FullName` | SID | 无 | 人机可读全名字串索引 |
| `0x03 (3)` | `FamilyName` | SID | 无 | 字体家族名称索引 |
| `0x04 (4)` | `Weight` | SID | 无 | 字重描述（如 "Bold"） |
| `0x05 (5)` | `FontBBox` | 4 个数值 | `0 0 0 0` | 全字体极限全局包围盒 `[llx lly urx ury]` |
| `0x0D (13)` | `UniqueID` | 整数 | 无 | PostScript 全局缓存唯一 ID |
| `0x0E (14)` | `XUID` | 数组 | 无 | 扩展唯一 ID 序列（用于 PDF 嵌入缓存） |
| `0x0F (15)` | `charset` | 偏移量 (offset) | 0 (ISO-Adobe) | 字形字符集映射表相对于 CFF 表首的字节偏移 |
| `0x10 (16)` | `Encoding` | 偏移量 (offset) | 0 (StandardEncoding) | 字符编码表相对于 CFF 表首的字节偏移 |
| `0x11 (17)` | `CharStrings` | 偏移量 (offset) | 无 | **核心指针**：字形 Type 2 轮廓索引表的字节偏移 |
| `0x12 (18)` | `Private` | 长度与偏移量 | 无 | **神经中枢**：私有微调字典的字节长度与其起始偏移 |
| `0x0C 0x01` | `isFixedPitch` | 布尔值 | `false (0)` | 是否为等宽字体 |
| `0x0C 0x02` | `ItalicAngle` | 数值 | `0.0` | 斜体倾斜角度 |
| `0x0C 0x03` | `UnderlinePosition` | 数值 | `-100` | 下划线垂直基准线位置 |
| `0x0C 0x04` | `UnderlineThickness` | 数值 | `50` | 下划线推荐物理厚度 |
| `0x0C 0x07` | `FontMatrix` | 6 元素数组 | `[0.001 0 0 0.001 0 0]` | 归一化仿射变换矩阵 |
| `0x0C 0x1E` | `ROS` | 3 个 SID | 无 | **CIDFont 专属**：Registry、Ordering 与 Supplement 三元组 |
| `0x0C 0x1F` | `CIDFontVersion` | 数值 | `0` | CID 字体版本号 |
| `0x0C 0x24` | `FDArray` | 偏移量 | 无 | **CIDFont 专属**：子字体字典索引表（Font DICT INDEX）偏移 |
| `0x0C 0x25` | `FDSelect` | 偏移量 | 无 | **CIDFont 专属**：字形到子字体分类映射表偏移 |

---

### 2. Private DICT 核心操作符全集：

| 操作符字节（Hex） | 键名（Key Name） | 参数类型 | 默认值 | 语义与光栅化控制功能 |
| :--- | :--- | :--- | :--- | :--- |
| `0x06 (6)` | `BlueValues` | 偶数个增量数组 | 无 | 主对齐带（包含基线下沉与上冲对齐区间） |
| `0x07 (7)` | `OtherBlues` | 偶数个增量数组 | 无 | 辅助对齐带（包含降部底部对齐区间） |
| `0x08 (8)` | `FamilyBlues` | 偶数个增量数组 | 无 | 家族共享主对齐带 |
| `0x09 (9)` | `FamilyOtherBlues`| 偶数个增量数组 | 无 | 家族共享辅助对齐带 |
| `0x0A (10)` | `StdHW` | 数值 | 无 | 标准水平主笔画宽度 |
| `0x0B (11)` | `StdVW` | 数值 | 无 | 标准垂直主笔画宽度 |
| `0x0C 0x09` | `BlueScale` | 浮点数 | `0.039625` | 对齐带随字号放大时解除吸附的阈值系数 |
| `0x0C 0x0A` | `BlueShift` | 数值 | `7` | 超出对齐带多少单位后强制取消对齐的突变阈值 |
| `0x0C 0x0B` | `BlueFuzz` | 数值 | `1` | 对齐带边界容错扩展像素 |
| `0x0C 0x0C` | `StemSnapH` | 递增数组 | 无 | 允许吸附对齐的多级水平笔画宽度候选表 |
| `0x0C 0x0D` | `StemSnapV` | 递增数组 | 无 | 允许吸附对齐的多级垂直笔画宽度候选表 |
| `0x0C 0x0E` | `ForceBold` | 布尔值 | `false` | 小字号极小分辨率下是否强行加粗细笔画 |
| `0x0C 0x11` | `LanguageGroup` | 整数 | `0` | 语言群组代码（0: 拉丁系; 1: 中日韩繁复汉字系） |
| `0x0C 0x13` | `Subrs` | 偏移量 | 无 | 本私有字典专属的局部子程序池偏移（Local Subrs） |
| `0x14 (20)` | `defaultWidthX` | 数值 | `0` | 全字库大多数字符共享的默认水平字宽 |
| `0x15 (21)` | `nominalWidthX` | 数值 | `0` | 字宽差分基数（实际字宽 = 存储增量 + nominalWidthX） |

---

### 3. Type 2 CharStrings 颠覆性指令全集权威字典

Type 2 彻底优化了 Type 1 指令流的冗余。其操作码体系更加高效紧凑：

#### 堆栈算术与逻辑运算指令：
* `0x0C 0x03 (and)`：逻辑与；
* `0x0C 0x04 (or)`：逻辑或；
* `0x0C 0x05 (not)`：逻辑非；
* `0x0C 0x09 (abs)`：绝对值；
* `0x0C 0x0A (add)`：加法；
* `0x0C 0x0B (sub)`：减法；
* `0x0C 0x0C (div)`：除法；
* `0x0C 0x0E (neg)`：求负数；
* `0x0C 0x0F (eq)`：相等判定；
* `0x0C 0x1A (sqrt)`：开平方；
* `0x0C 0x18 (drop)`：丢弃栈顶元素；
* `0x0C 0x1B (dup)`：复制栈顶；
* `0x0C 0x1C (exch)`：交换栈顶两元素；
* `0x0C 0x1D (index)`：提取指定深度操作数；
* `0x0C 0x1E (roll)`：操作数栈循环滚动；
* `0x0C 0x14 (put)`：将数值存入暂存数组槽位 $i$；
* `0x0C 0x15 (get)`：从暂存数组槽位 $i$ 提取数值压栈；
* `0x0C 0x16 (ifelse)`：条件三目选择运算。

#### 提示掩码指令（`hintmask` 与 `cntrmask`）：
* **操作码 `0x13 (19)` (`hintmask`)**：
  在一条字形轮廓中，若首先声明了 $H$ 条水平提示与 $V$ 条垂直提示，则提示总数为 $N = H + V$。
  紧随 `hintmask` 操作码之后，直接内嵌 $\lceil N / 8 \rceil$ 个字节的二进制位掩码！
  每一个位（Bit）对应一条提示：若第 $k$ 位为 1，则指示当前轮廓从此时此刻起，瞬间激活第 $k$ 号提示；若为 0 则静默禁用该提示。
  这使得包含数十条复杂笔画的汉字（如“囊”、“龘”）能够在单个字符内部自由切分局部微观几何，且额外字节开销极其微小！
* **操作码 `0x14 (20)` (`cntrmask`)**：
  专门用于声明笔画中轴线与内部对称留白（Counter）的排他性约束，保证在超低分辨率下小写字母 'm' 的两个拱门或汉字“三”的三条间隙均匀等距。

---

### 4. 工业级 CFF INDEX 解析器 Python 实现

```python
import struct

class CFFIndex:
    def __init__(self, data: bytes, offset: int = 0):
        self.count, = struct.unpack(">H", data[offset:offset+2])
        self.items = []
        if self.count == 0:
            self.total_size = 2
            return
            
        self.off_size = data[offset+2]
        offsets_start = offset + 3
        offsets_count = self.count + 1
        
        # 动态解析 1 到 4 字节的变宽偏移量
        raw_offsets = []
        for i in range(offsets_count):
            pos = offsets_start + i * self.off_size
            chunk = b'\x00' * (4 - self.off_size) + data[pos:pos+self.off_size]
            val, = struct.unpack(">I", chunk)
            raw_offsets.append(val)
            
        data_base = offsets_start + offsets_count * self.off_size - 1
        for i in range(self.count):
            item_start = data_base + raw_offsets[i]
            item_end = data_base + raw_offsets[i+1]
            self.items.append(data[item_start:item_end])
            
        self.total_size = (offsets_start + offsets_count * self.off_size + raw_offsets[-1] - 1) - offset

    def __len__(self):
        return self.count

    def __getitem__(self, idx):
        return self.items[idx]
```

通过这一套高度浓缩、架构统一的现代矢量二进制规范，PostScript CFF 体系在维持了 Type 1 极致平滑的三次贝塞尔曲线与高级提示的同时，将全字库体积削减了 40% 以上，成为了当今印刷出版工业无可争议的矢量基石。
---

## C.8 多重母版字体（Multiple Master）动态实例生成实战

在 PostScript 解释器内部，用户可以通过动态混合（Blend）直接派生出全新的物理字体实例：

```postscript
% 查找基础多重母版字体
/MinionMM findfont

% 在二维设计空间中定义归一化插值坐标：
% 字重轴权重 0.45 (Light到Black之间)，字宽轴权重 0.80 (紧缩到宽体之间)
[0.45 0.80] makeblendedfont

% 将生成的派生字体注册为全局字体
/Minion-Custom findfont
12 scalefont
setfont

% 在页面上排版输出
100 700 moveto
(Voile Magic Library: Multiple Master Dynamic Instance) show
showpage
```

### 线性与非线性空间插值微积分：
在实际工程中，字体设计师往往要求插值不是简单的线性渐变，而是遵循视觉平衡曲线。Adobe MM 引入了 `NormalizeDesignVector` 映射函数：
对于设计轴输入坐标 $d_j \in [D_{j, \min}, D_{j, \max}]$，通过分段线性查找表将其非线性映射为归一化混合标量 $w_j \in [0, 1]$，再通过 Kronecker 积计算最终的 $2^k$ 个极端母版加权矩阵：

$$\mathbf{W} = \bigotimes_{j=1}^k \begin{pmatrix} 1 - w_j \\ w_j \end{pmatrix}$$

这一数学框架，成为了二十五年后现代 OpenType 1.8 矢量可变字体（Variable Fonts / Variations `fvar`, `gvar`, `HVAR`, `MVAR`）的理论祖先！

---

## C.9 东亚巨型字符集 ROS（Registry-Ordering-Supplement）全景谱系

在 CID-keyed 字体体系中，字符集的版本与规模由 **ROS 三元组** 严格定义：

| 字符集集合名称 | 适用的文字与国家/地区 | 字符总数 (Supplement) | 核心涵盖范围与标准 |
| :--- | :--- | :--- | :--- |
| **Adobe-Japan1-6** | 日文（汉字 Kanji、平假名、片假名） | 23,058 字形 (Supp 6) | JIS X 0208, JIS X 0213, JIS X 0212, 印刷用人名汉字变体、纵排变体 |
| **Adobe-GB1-5** | 中国大陆简体中文 | 30,284 字形 (Supp 5) | GB 2312, GB 13000.1, GBK, GB 18030-2000, 繁体字及少数民族拼音 |
| **Adobe-CNS1-7** | 中国台湾/香港繁体中文 | 19,088 字形 (Supp 7) | Big5, Big-5E, CNS 11643 第 1-15 字母字面、香港增补字符集 (HKSCS) |
| **Adobe-Korea1-2** | 韩国与朝鲜谚文（Hangul）及汉字 | 18,352 字形 (Supp 2) | KS X 1001, KS X 1002, 常用谚文音节块及韩国古汉字 |

每一个 Supplement 保持绝对的**向后单调递增兼容性**：新版本仅在数组末尾追加全新的 CID 编号，绝不修改或删除既有的历史 CID，彻底杜绝了跨版本文档重新排版时的文字跑位风险！
---

## C.10 CFF 规范前 391 个预定义标准字符串（Standard Strings）架构

在 CFF 容器中，为了极致压缩字体体积，Adobe 在标准规范（Adobe Technical Note #5176）中硬编码固化了 **391 个最常用的全语言字形名称字符串**。在 `Top DICT`、`Private DICT` 或字形名称寻址中：
* 任何 String ID（SID）若落在 `0 <= SID <= 390` 之间，**完全不需要在字体文件的 `String INDEX` 中占用任何字节**！解码引擎直接在静态标准字符串数组中查表；
* 自定义字形名称（如汉字 GID、私有合字）的 SID 从 391 开始分配，实际存储在 `String INDEX` 中的物理索引为 $\text{CustomSID} = \text{SID} - 391$。

### 核心标准字符串索引分布表（节选）：

| SID 范围 | 代表性字形符号名称 | 用途与排印归属 |
| :--- | :--- | :--- |
| `0` | `.notdef` | 缺失字符默认外观 |
| `1..10` | `space`, `exclam`, `quotedbl`, `numbersign`, `dollar`, `percent`, `ampersand`, `quoteright`, `parenleft`, `parenright` | 基础 ASCII 标点符号 |
| `11..26` | `asterisk`, `plus`, `comma`, `hyphen`, `period`, `slash`, `zero`..`nine` | 运算符与阿拉伯数字 |
| `27..52` | `A` 至 `Z` | 大写拉丁英文字母 |
| `53..78` | `a` 至 `z` | 小写拉丁英文字母 |
| `96..145` | `Agrave`, `Aacute`, `Acircumflex`, `Atilde`, `Adieresis`, `Aring`, `Ccedilla`, `Egrave`, `Eacute`, `Igrave`, `Ntilde`, `Oacute`, `Uacute` | 西欧重音大写字母 |
| `146..195` | `agrave`, `aacute`, `acircumflex`, `atilde`, `adieresis`, `aring`, `ccedilla`, `egrave`, `eacute`, `igrave`, `ntilde`, `oacute`, `uacute` | 西欧重音小写字母 |
| `196..250` | `fi`, `fl`, `dotlessi`, `grave`, `acute`, `circumflex`, `tilde`, `macron`, `breve`, `dotaccent`, `dieresis`, `ring`, `cedilla`, `hungarumlaut`, `ogonek` | 经典拉丁连字与独立变音符 |
| `251..390` | `Euro`, `trademark`, `perthousand`, `bullet`, `copyright`, `registered`, `ellipsis`, `dagger`, `daggerdbl`, `guillemotleft`, `guillemotright` | 国际通用货币符号与出版商印刷符号 |

通过这一天才设计，全套包含西欧 200 多个拉丁字符的 CFF 字体，其 `String INDEX` 内部往往**仅需存储家族名称与字型版本两个短字串**，字符串表体积被压缩至令人惊叹的 20 字节以内！

---

## C.11 复杂符号 Type 1 CharStrings 真实字节码反汇编跟踪（以字符 '$' 为例）

货币美元符号 `$` 是字体设计中几何复杂度最高的符号之一：它由一个平滑双重弯曲的 'S' 形曲线躯干与一到两条垂直贯穿的主干立柱构成，在有限的铅字空间中存在多达 4 条水平提示与 4 条垂直提示。

以下为一段真实的 Type 1 解密字节码指令序列及其物理执行过程：

```postscript
% 1. 设置水平左侧轴承为 50，前进字宽为 500
50 500 hsbw

% 2. 声明字符上半部分的初始水平与垂直提示
% 顶部横弧 (y=650, dy=40) 与 中部横梁 (y=360, dy=35)
650 40 360 35 hstem
% 左右垂直干提示 (x=230, dx=40)
230 40 vstem

% 3. 绘制顶部衬线与第一段曲线
230 650 rmoveto
40 hlineto
-15 -30 -40 -35 -80 -40 rrcurveto

% 4. 触发动态提示替换 (Hint Substitution)
% 抹除上半部提示，激活中腰与下半部的全新笔画提示集合！
1 3 callothersubr pop
150 40 hstem % 底部横弧提示
210 40 vstem % 下干提示

% 5. 继续绘制穿越中腰的平滑反向曲线
-30 -20 -40 -30 -30 -60 rrcurveto
0 -50 vlineto
closepath

% 6. 终结绘制，提交光栅缓冲区
endchar
```

在执行 `callothersubr 3` 的瞬间，光栅化引擎重置几何对齐网格，使美元符号上下两个封闭线圈在低分辨率下互不干涉，完美维持了对称饱满的印刷轮廓。
---

## C.12 Type 0 复合字体 FMapType 寻址算法与映射模式全集

在 Type 0 复合字体中，顶层字体维护一个 `FDepVector`（子字体依赖向量）数组，并通过 `FMapType` 整数代码指示解释器如何对多字节文本流进行分词与寻址：

| FMapType 代码 | 映射模式名称 | 输入字节流分词机制 | 子字体索引与内部字符映射算法 |
| :--- | :--- | :--- | :--- |
| **`2`** | 8/8 映射（两字节对称） | 严格按 2 字节（双字节）切分 | 高字节作为 `FDepVector` 索引选择子字体，低字节在该子字体中提取字符 |
| **`3`** | 8/16 映射（单双字节混合） | 首字节若为 `EscChar` 则消耗两字节 | 用于西文 ASCII 与日文半角/全角混合排版，动态切换单字节与双字节子字库 |
| **`4`** | 16/16 映射（四字节大字符集）| 严格按 4 字节切分 | 前双字节选择子字体，后双字节在子字体内部寻址（用于超早期 CNS 繁体大字库） |
| **`8`** | Shift-JIS 专用硬件映射 | 依据 Shift-JIS 编码范围智能分词 | 首字节若落在 `0x81..0x9F` 或 `0xE0..0xFC`，自动判定为双字节并执行高低字节解包 |
| **`9`** | Big5 繁体中文专用映射 | 依据 Big5 高字节范围智能分词 | 首字节若落在 `0xA1..0xFE`，自动抓取次字节并映射至对应的繁体字形子字库 |

尽管 Type 0 架构在 1990 年代初有效支撑了东亚桌面出版的起步，但其复杂的树状解析与割裂的子字库度量，最终促使 Adobe 在 1993 年推出了架构更加扁平、纯粹且强大的 CID-keyed 字体体系。

---

# 附录 D：TrueType、OpenType 与 AAT 字体底层文件格式全景指南

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

---

# 附录 E：TrueType 虚拟机微指令全景参考词典（TrueType Instructions Reference Dictionary）

在所有现代字型格式中，TrueType 的指令系统（Hinting Instructions）是复杂度最高、表现力最强、也是最接近计算机体系结构底层的部分。与 PostScript Type 1 仅提供陈述式声明的“提示（Hints）”不同，**TrueType 内部直接嵌入了一台功能完整的图灵完备虚拟机（TrueType Virtual Machine, TT-VM）！**

在这台虚拟机中，字形轮廓上的每一个控制点（Point）不仅仅是几何坐标，更是一个可被寻址、被数学变换、被条件逻辑驱动的“物理粒子”。通过执行字节码程序，字体设计师可以针对特定的屏幕点阵分辨率（PPEM），动态伸缩笔画、平移波谷、强制对称并消除走样。本附录将对 TrueType 虚拟机的内存模型、图形状态机（Graphics State）以及全部约 130 条指令的操作码、堆栈效应与执行语义进行权威字典级解构。

---

## E.1 TrueType 虚拟机架构与程序生命周期

TrueType 虚拟机是一台纯粹的**大端序栈式计算机（Stack-based Machine）**。它不具备通用寄存器，所有算术、几何与逻辑运算均在一个 32 位整数操作数栈上完成。

```
+-------------------------------------------------------+
|  TrueType 虚拟机硬件资源全景                           |
+-------------------------------------------------------+
|  1. 操作数栈 (Operand Stack, 通常 256-512 深度)        |
|  2. 控制值表 (Control Value Table, CVT, 16位有符号字)   |
|  3. 存储区 (Storage Area, 32位通用暂存数组)             |
|  4. 黄昏区 (Twilight Zone, Zone 0, 临时辅助几何点池)   |
|  5. 字形区 (Glyph Zone, Zone 1, 真实轮廓控制点阵列)     |
|  6. 图形状态机寄存器组 (Graphics State Registers)       |
+-------------------------------------------------------+
```

### 虚拟机的三大执行生命周期（Lifecycle）
1. **字体级程序（`fpgm` 表）**：在字库被操作系统首次载入内存时**仅执行整整一次**。它用于编译通用的全局函数定义（`FDEF`）与用户自创指令（`IDEF`），建立全字通用的几何计算子程序库；
2. **渲染预处理程序（`prep` 表）**：在用户调整字号（PPEM 发生变化）、屏幕分辨率或发生仿射变换时**执行一次**。它根据当前的微观分辨率，批量计算并将物理网格尺寸写入控制值表（CVT），并设置全局图形状态（如舍入规则）；
3. **字形级指令流（`glyf` 表内部）**：在光栅化引擎实际绘制每一个具体字形时**每次独立执行**。它操纵该字形的在线点与脱线点，将其强制吸附对齐到物理像素网格。

::: tip TrueType 虚拟机执行流与图形状态机变换（Figure E-1, E-2）
![TT 虚拟机架构（Figure E-1）](/images/fonts-encodings/fig-app-e1.png)
*TT 虚拟机架构（Figure E-1）*
:::

*图 E-1：TrueType 虚拟机的执行总线拓扑。操作数栈、CVT 查表、Storage 暂存区与双几何区域的协同交互。*

::: tip 控制值表 CVT 与像素网格切入（Figure E-2）
![CVT 网格切入（Figure E-2）](/images/fonts-encodings/fig-app-e2.png)
*CVT 网格切入（Figure E-2）*
:::

*图 E-2：控制值表（CVT）网格切入机制（Control Value Cut-In）：当实际笔画宽度与 CVT 理想值的偏差小于阈值时，强行吸附到 CVT 规范值；一旦偏差过大，立即解除锁定，恢复自由网格对齐。*

---

## E.2 图形状态机（Graphics State）核心寄存器组

图形状态机由一组直接控制几何计算行为的专用寄存器构成：
* **自由向量（Freedom Vector, $\vec{f} = (f_x, f_y)$）**：**点被允许移动的物理方向单位向量**。当执行移动指令时，点只能沿着 $\vec{f}$ 方向平移；
* **投影向量（Projection Vector, $\vec{p} = (p_x, p_y)$）**：**距离度量方向单位向量**。所有点间距离、笔画宽度均投影到 $\vec{p}$ 轴线上进行标量测量；
* **双投影向量（Dual Projection Vector, $\vec{dp}$）**：在未经 Hinting 的原始轮廓设计网格上测量初始距离的向量；
* **参考点寄存器（Reference Points: $rp0, rp1, rp2$）**：作为相对移动与内插几何基准的锚定点索引；
* **区域指针（Zone Pointers: $zp0, zp1, zp2$）**：指示当前引用的几何点属于 Zone 0（黄昏区）还是 Zone 1（当前字形轮廓区）；
* **舍入状态（Rounding State）**：控制浮点数值如何量化为整数像素网格。包含网格舍入（`RTG`，舍入到最近像素中心）、半网格舍入（`RTHG`，舍入到 0.5 像素边界）、双倍网格舍入（`RTDG`）、向下取整（`RDTG`）、向上取整（`RUTG`）以及由周期（Period）、相位（Phase）与阈值（Threshold）定制的超强舍入（`SROUND`）；
* **极小距离阈值（Single Minimum Distance, `SMD`）**：在执行相对移动时，防止两笔画因四舍五入坍缩重叠的物理最小保护间隙；
* **控制值切入阈值（Control Value Cut-In, `SCVTCI`）**：决定何时启用 CVT 强行吸附的差值上限；
* **循环计数器（Loop Counter）**：由 `SLOOP` 指令设置，控制后续指令自动重复执行的次数。

---

## E.3 核心微指令分类权威参考词典

### 1. 堆栈压入指令（PUSH Instructions）

| 操作码（Hex/Dec） | 指令助记符 | 参数形态 | 堆栈效应（Stack Effect） | 执行逻辑与物理语义 |
| :--- | :--- | :--- | :--- | :--- |
| `0xB0..0xB7 (176..183)` | `PUSHB[abc]` | $n$ 字节无符号数 | $\emptyset \to b_1, b_2, \dots, b_k$ | 将指令后紧随的 $k = abc + 1$（1 到 8）个单字节整数按序压入栈顶 |
| `0xB8..0xBF (184..191)` | `PUSHW[abc]` | $n$ 双字节有符号数 | $\emptyset \to w_1, w_2, \dots, w_k$ | 将指令后紧随的 $k = abc + 1$（1 到 8）个 16 位大端整数按序压入栈顶 |
| `0x40 (64)` | `NPUSHB` | 计数 $n$ + $n$ 字节 | $\emptyset \to b_1, \dots, b_n$ | 批量压栈：第一个字节 $n$ 为数量，随后 $n$ 个单字节依次压栈 |
| `0x41 (65)` | `NPUSHW` | 计数 $n$ + $n$ 双字 | $\emptyset \to w_1, \dots, w_n$ | 批量字压栈：第一个字节 $n$ 为数量，随后 $n$ 个 16 位整数依次压栈 |

### 2. 存储区（Storage）与控制值表（CVT）访问指令

| 操作码（Hex/Dec） | 助记符 | 堆栈输入 | 堆栈输出 | 执行语义 |
| :--- | :--- | :--- | :--- | :--- |
| `0x43 (67)` | `RS` | $index$ | $value$ | 从存储区（Storage Area）读取索引为 $index$ 处的 32 位值压栈 |
| `0x42 (66)` | `WS` | $value, index$ | $\emptyset$ | 将 32 位值 $value$ 写入存储区索引 $index$ 槽位 |
| `0x45 (69)` | `RCVT` | $index$ | $value$ | 读取 CVT 表中索引为 $index$ 的当前网格缩放值（单位：26.6 像素定点数） |
| `0x44 (68)` | `WCVTP` | $value, index$ | $\emptyset$ | 将经像素网格缩放的值 $value$ 写入 CVT 表中的 $index$ 槽位 |
| `0x70 (112)` | `WCVTF` | $value, index$ | $\emptyset$ | 将未经缩放的设计单位值 $value$ 写入 CVT（引擎自动执行当前 PPEM 比例缩放） |

### 3. 图形状态机向量与区域设置指令

| 操作码（Hex/Dec） | 助记符 | 堆栈输入 | 堆栈输出 | 执行语义 |
| :--- | :--- | :--- | :--- | :--- |
| `0x00 (0)` | `SVTCA[y]` | $\emptyset$ | $\emptyset$ | 将自由向量与投影向量同时设置为 Y 轴：$\vec{f} = \vec{p} = (0, 1)$ |
| `0x01 (1)` | `SVTCA[x]` | $\emptyset$ | $\emptyset$ | 将自由向量与投影向量同时设置为 X 轴：$\vec{f} = \vec{p} = (1, 0)$ |
| `0x02 (2)` | `SPVTCA[y]` | $\emptyset$ | $\emptyset$ | 仅将投影向量设置为 Y 轴 |
| `0x03 (3)` | `SPVTCA[x]` | $\emptyset$ | $\emptyset$ | 仅将投影向量设置为 X 轴 |
| `0x04 (4)` | `SFVTCA[y]` | $\emptyset$ | $\emptyset$ | 仅将自由向量设置为 Y 轴 |
| `0x05 (5)` | `SFVTCA[x]` | $\emptyset$ | $\emptyset$ | 仅将自由向量设置为 X 轴 |
| `0x06..0x07` | `SPVTL[0..1]` | $p_1, p_2$ | $\emptyset$ | 将投影向量设置为平行于点 $p_1$ 到 $p_2$ 的直线（若为 1 则逆时针旋转 90 度建立垂直线） |
| `0x08..0x09` | `SFVTL[0..1]` | $p_1, p_2$ | $\emptyset$ | 将自由向量设置为平行于点 $p_1$ 到 $p_2$ 的直线（若为 1 则旋转 90 度） |
| `0x0A (10)` | `SPVFS` | $x, y$ | $\emptyset$ | 通过显式输入的向量分量设置投影向量：$\vec{p} = \frac{(x, y)}{\sqrt{x^2+y^2}}$ |
| `0x0B (11)` | `SFVFS` | $x, y$ | $\emptyset$ | 通过显式输入的向量分量设置自由向量 |
| `0x0E (14)` | `SFVTPV` | $\emptyset$ | $\emptyset$ | 将自由向量设置为与当前投影向量相同：$\vec{f} = \vec{p}$ |
| `0x10..0x12` | `SRP0,1,2` | $p$ | $\emptyset$ | 设置参考点寄存器：分别将 $rp0, rp1, rp2$ 指向轮廓点编号 $p$ |
| `0x13..0x15` | `SZP0,1,2` | $zone$ | $\emptyset$ | 设置区域指针：将 $zp0, zp1, zp2$ 绑定到 Zone 0（黄昏区）或 Zone 1（字形区） |
| `0x16 (22)` | `SZPS` | $zone$ | $\emptyset$ | 同时将 $zp0, zp1, zp2$ 全部绑定到指定区域 |
| `0x17 (23)` | `SLOOP` | $count$ | $\emptyset$ | 设置循环计数器：后续的 `SHP`、`IP`、`ALIGNPTS` 等指令自动连续执行 $count$ 次 |

### 4. 点位移动与微观几何对齐指令

#### `IUP[x]` 与 `IUP[y]`（内插未触碰点，Interpolate Untouched Points）
TrueType 中**最重要的全局收尾指令**！在整个 Hinting 过程中，设计师通常只对字形轮廓上关键的骨架驻点（Touched Points，约占总点数的 20%）执行了移动对齐。其余 80% 的曲线过渡点处于“未被触碰（Untouched）”状态。
当在程序末尾调用 `IUP[x]` 或 `IUP[y]` 时，渲染引擎会沿着每一条封闭轮廓线进行线性扫描：在任意两个被触碰的极值锚点之间，依据原始设计网格的比例关系，**通过仿射内插算法一次性平滑重排中间所有未触碰点的像素坐标**，完美维持曲线的有机饱满张力！

#### `MIRP[0..31]`（Move Indirect Relative Point）的五维位掩码解构
操作码范围从十六进制 `0xCE` 到 `0xDF`（十进制 206–223）。这是一条极度强大的复合指令，指令编号本身低 5 位即编码了完整的几何控制逻辑：

```
MIRP[abcde] (操作码 = 0xCE + abcde)
Bit 4 (a): set_rp0      -> 若为 1，在完成移动后将 rp0 自动更新为当前目标点 p
Bit 3 (b): min_distance -> 若为 1，强制施加单极小距离约束（距离 >= SMD）
Bit 2 (c): round_dist   -> 若为 1，根据当前 RoundingState 对距离执行网格舍入
Bits 1-0 (de): color    -> 笔画距离色彩约束：
                           00: 灰度距离（无约束）
                           01: 黑色距离（笔画实体内部）
                           10: 白色距离（笔画之间的空白负空间）
```

*执行语义*：以参考点 $rp0$ 为基准，读取 CVT 表中索引为 $cvt$ 的标准距离，沿自由向量 $\vec{f}$ 平移目标点 $p$，使得 $p$ 在投影向量 $\vec{p}$ 上的位移精确等于经网格舍入与切入判断后的 CVT 间距！

#### `MDRP[0..31]`（Move Direct Relative Point）
与 `MIRP` 完全同构，但距离不取自 CVT，而是直接在原始设计轮廓上测量 $rp0$ 与目标点 $p$ 的初始欧氏距离。

### 5. 增量微调微指令（DELTAP 与 DELTAC）

在某些极具挑战性的低分辨率场景下（例如在 10 像素或 12 像素点阵屏排版英文字母 'e' 或汉字“日”），通用的数学舍入规则往往会导致局部笔画粘连或像素镂空缺失。TrueType 提供了终极的物理级人工微调武器：**Delta 指令组**。

* **`DELTAP1`**：针对 9 到 24 像素（PPEM）的超小显示环境；
* **`DELTAP2`**：针对 25 到 40 像素的中等环境；
* **`DELTAP3`**：针对 41 到 56 像素的大字号环境。

#### Delta 参数编码与数学微调量方程：
每条 Delta 指令接受一组压栈的参数对：$(arg, p)$，其中 $p$ 为目标控制点索引，$arg$ 是一个通过单字节紧凑编码的微位移复合数：

$$arg = (\text{nudge} + 8) \times 16 + (\text{target\_ppem} - \text{base\_ppem})$$

* **目标字号**：当且仅当当前屏幕光栅化分辨率 $\text{PPEM} == \text{base\_ppem} + (arg \bmod 16)$ 时，该指令才会瞬间被激活！在其他任何字号下自动无视跳过；
* **微调量（Nudge）**：位移幅度由 $arg$ 的高 4 位决定（数值范围从 $-8$ 到 $+7$）。实际施加在控制点上的空间物理平移向量为：
  $$\Delta \vec{x} = \text{nudge} \times \left( \frac{1}{2^{\text{delta\_shift}}} \right) \text{ pixels} \times \vec{f}$$

通过将 `delta_shift` 设置为 3（即 $\frac{1}{8}$ 像素分辨率），字体设计师可以极其优雅地宣告：“当字号恰好等于 11 像素时，将横笔画第 5 号节点向下微挪 $\frac{2}{8}$ 个像素”——正是这种微积分级别的极端控制力，成就了 Windows 操作系统在 CRT 显示器时代傲视群雄的卓越正文清晰度！

---

## E.4 字母表级全指令权威词典速查（Alphabetical Instruction Reference）

以下按英文字母顺序，完整收录 TrueType 规范中定义的全部微指令执行细则：

### A 系列指令
* **`AA` (0x7F, 127)**：Adjust Angle。根据投影向量与自由向量调整参考线夹角。
* **`ADD` (0x60, 96)**：加法。栈顶两数相加弹出，压入两数之和：$d = a + b$（单位：26.6 定点数）。
* **`ALIGNPTS` (0x27, 39)**：对齐两点。弹出点 $p_1, p_2$，沿自由向量平移它们，使得两者在投影向量上的坐标重合到它们的中点。
* **`ALIGNRP` (0x3C, 60)**：对齐参考点。将目标点 $p$ 沿自由向量平移，使其在投影向量上的投影与参考点 $rp0$ 严格重合。
* **`AND` (0x5A, 90)**：逻辑与。栈顶两数若皆非零压入 1，否则压入 0。

### C 系列指令
* **`CALL` (0x2B, 43)**：调用函数。弹出函数标识符，跳转执行在 `fpgm` 中由 `FDEF` 预先定义的指令块。
* **`CEILING` (0x67, 103)**：天花板向上取整。将 26.6 定点数的有效小数部分舍入到下一个整数边界。
* **`CINDEX` (0x25, 37)**：复制指定深度操作数。弹出整数 $k$，将栈顶向下第 $k$ 个元素复制并压入栈顶。
* **`CLEAR` (0x22, 34)**：清空操作数栈。将当前栈中所有残留元素彻底弹出丢弃。

### D 系列指令
* **`DEBUG` (0x4F, 79)**：调试指令。用于字型调试器挂起执行，在发布版字库中自动忽略。
* **`DELTAC1..3` (0x73..0x75)**：控制值表微调。在特定 PPEM 下微调 CVT 槽位数值。
* **`DELTAP1..3` (0x5D, 0x71, 0x72)**：点位微调。在特定 PPEM 下对轮廓点施加 $\pm \frac{k}{8}$ 像素平移。
* **`DEPTH` (0x24, 36)**：测量栈深度。统计当前操作数栈中的元素总数压入栈顶。
* **`DIV` (0x62, 98)**：除法。$d = (a \times 64) / b$，维持 26.6 标度。
* **`DUP` (0x20, 32)**：复制栈顶。将栈顶第一个元素复制一份压入栈顶。

### E–F 系列指令
* **`EIF` (0x59, 89)**：条件分支结束（End If）。
* **`ELSE` (0x1B, 27)**：条件分支否定分支。
* **`ENDF` (0x2D, 45)**：函数定义结束（End Function）。
* **`EQ` (0x54, 84)**：相等判定。若 $a == b$ 压入 1，否则压入 0。
* **`EVEN` (0x57, 87)**：偶数判定。
* **`FDEF` (0x2C, 44)**：定义函数。在 `fpgm` 中开启一段由函数 ID 标识的代码块。
* **`FLIPOFF` (0x4E, 78)**：强制将指定区间的点设置为脱线控制点（Off-curve）。
* **`FLIPON` (0x4D, 77)**：强制将指定区间的点设置为在线点（On-curve）。
* **`FLIPPT` (0x80, 128)**：翻转点极性（On-curve $\leftrightarrow$ Off-curve）。
* **`FLOOR` (0x66, 102)**：地板向下取整。截断 26.6 定点数小数位。

### G–I 系列指令
* **`GC[0..1]` (0x46..0x47)**：读取点坐标。测量点 $p$ 在投影向量上的当前物理坐标（0 代表当前网格，1 代表原始设计网格）。
* **`GETINFO` (0x88, 136)**：查询运行环境。获取渲染器版本、是否支持灰度、ClearType 亚像素状态。
* **`GFV` (0x0D, 13)**：读取当前自由向量。
* **`GPV` (0x0C, 12)**：读取当前投影向量。
* **`GT` / `GTEQ` (0x52, 0x53)**：大于与大于等于判定。
* **`IDEF` (0x89, 137)**：指令定义（Instruction Definition）。允许字库重载或定义全新的虚拟机操作码！
* **`IF` (0x58, 88)**：条件执行。弹出布尔值，若为真继续执行，若为假跳至 `ELSE` 或 `EIF`。
* **`INSTCTRL` (0x8E, 142)**：指令执行控制。允许全局关闭 Hinting 或禁用特定平滑算法。
* **`IP` (0x39, 57)**：内插点（Interpolate Point）。以参考点 $rp1$ 与 $rp2$ 为空间基准，将目标点 $p$ 沿自由向量平移，使其与两参考点的相对距离比例保持不变。
* **`ISECT` (0x0F, 15)**：相交计算。计算直线 $(a_0, a_1)$ 与直线 $(b_0, b_1)$ 的空间几何交点，并将目标点直接置于交点处。
* **`IUP[0..1]` (0x30..0x31)**：内插未触碰点（0 针对 Y 轴，1 针对 X 轴）。

### J–M 系列指令
* **`JMPR` (0x1C, 28)**：无条件相对跳转。
* **`JROF` / `JROT` (0x78, 0x79)**：条件相对跳转（为假跳转 / 为真跳转）。
* **`LOOPCALL` (0x2A, 42)**：循环调用函数。连续执行指定函数若干次。
* **`LT` / `LTEQ` (0x50, 0x51)**：小于与小于等于判定。
* **`MAX` / `MIN` (0x63, 0x8B)**：极值选择。
* **`MD[0..1]` (0x49..0x4A)**：测量两点间距离（0 测量当前坐标，1 测量原始轮廓）。
* **`MDAP[0..1]` (0x2E..0x2F)**：直接移动并对齐点。将点 $p$ 舍入到网格边界并标记为“已触碰”。
* **`MDRP[0..31]` (0xC0..0xDF)**：直接相对移动点（根据 5 位标志位解码执行）。
* **`MIAP[0..1]` (0x3E..0x3F)**：间接移动并对齐点。将点 $p$ 移动到由 CVT 槽位指定的绝对距离处。
* **`MIRP[0..31]` (0xE0..0xFF)**：间接相对移动点（根据 5 位标志位从 CVT 读取距离执行）。
* **`MPPEM` (0x4B, 75)**：读取当前每 Em 像素尺寸（Pixels Per Em）。
* **`MPS` (0x4C, 76)**：读取当前点数磅值（Point Size）。
* **`MSIRP[0..1]` (0x3A..0x3B)**：移动直接绝对点并不施加网格舍入。
* **`MUL` (0x63, 99)**：乘法：$d = (a \times b) / 64$。

### N–R 系列指令
* **`NEG` (0x65, 101)**：数值取反：$d = -a$。
* **`NEQ` (0x55, 85)**：不等于判定。
* **`NOT` (0x5C, 92)**：逻辑非。
* **`NROUND[0..3]` (0x6C..0x6F)**：不施加引擎补偿的四种纯净舍入。
* **`ODD` (0x56, 86)**：奇数判定。
* **`OR` (0x5B, 91)**：逻辑或。
* **`POP` (0x21, 33)**：弹出栈顶元素。
* **`RCVT` (0x45, 69)**：读取 CVT 控制值。
* **`RDTG` (0x7D, 125)**：设置舍入状态为向下朝网格舍入（Round Down to Grid）。
* **`ROFF` (0x7A, 122)**：关闭网格舍入（Round Off）。
* **`ROLL` (0x8A, 138)**：操作数栈顶三元素回转滚动。
* **`ROUND[0..3]` (0x68..0x6B)**：带光栅化引擎光学补偿的网格舍入。
* **`RS` (0x43, 67)**：读取 Storage 存储区。
* **`RTDG` (0x3D, 61)**：设置舍入状态为双倍网格舍入（0.5 像素精度）。
* **`RTG` (0x18, 24)**：设置舍入状态为常规网格舍入（Round to Grid）。
* **`RTHG` (0x19, 25)**：设置舍入状态为半网格舍入（Round to Half Grid）。
* **`RUTG` (0x7C, 124)**：设置舍入状态为向上朝网格舍入（Round Up to Grid）。

### S 系列指令
* **`S45ROUND` (0x77, 119)**：设置针对 $45^\circ$ 对角斜线的特殊网格舍入参数。
* **`SANGW` (0x7E, 126)**：设置倾斜角度权重。
* **`SCANCTRL` (0x85, 133)**：扫描转换辍笔控制（Dropout Control）。激活极小像素孤立笔画保护。
* **`SCANTYPE` (0x8D, 141)**：设置辍笔保护模式（简单辍笔、智能相交辍笔）。
* **`SCFS` (0x48, 72)**：直接设置点在投影轴上的绝对坐标。
* **`SCVTCI` (0x1D, 29)**：设置 CVT 切入阈值（Control Value Cut-In）。
* **`SDB` (0x5E, 94)**：设置 Delta 基准偏移量（Delta Base）。
* **`SDS` (0x5F, 95)**：设置 Delta 步进位移标度（Delta Shift）。
* **`SFVFS` (0x0B, 11)**：通过向量分量显式设置自由向量。
* **`SFVTCA[0..1]` (0x04..0x05)**：设置自由向量平行于坐标轴。
* **`SFVTL[0..1]` (0x08..0x09)**：设置自由向量平行或垂直于指定线段。
* **`SFVTPV` (0x0E, 14)**：令自由向量等于当前投影向量。
* **`SHC[0..1]` (0x34..0x35)**：平移轮廓（Shift Contour）。将指定轮廓上的所有点，按照参考点发生的位移整体平行平移！
* **`SHP[0..1]` (0x32..0x33)**：平移点（Shift Point）。将指定点按照参考点的位移平移。
* **`SHPIX` (0x38, 56)**：以绝对像素距离平移点序列。
* **`SHZ[0..1]` (0x36..0x37)**：平移整个几何区域（Shift Zone）。
* **`SLOOP` (0x17, 23)**：设置后续单点指令的循环执行计数。
* **`SMD` (0x1A, 26)**：设置极小距离保持阈值（Minimum Distance）。
* **`SPVFS` (0x0A, 10)**：通过向量分量显式设置投影向量。
* **`SPVTCA[0..1]` (0x02..0x03)**：设置投影向量平行于坐标轴。
* **`SPVTL[0..1]` (0x06..0x07)**：设置投影向量平行或垂直于指定线段。
* **`SROUND` (0x76, 118)**：定制超强舍入状态（显式输入 Period、Phase、Threshold）。
* **`SRP0..2` (0x10..0x12)**：分别将参考点寄存器 $rp0, rp1, rp2$ 指向指定点。
* **`SSW` (0x1F, 31)**：设置单笔画全局宽度（Single Stroke Width）。
* **`SSWI` (0x20, 32)**：设置单笔画宽度设计单位输入值。
* **`SUB` (0x61, 97)**：减法：$d = a - b$。
* **`SVTCA[0..1]` (0x00..0x01)**：同时设置自由向量与投影向量平行于坐标轴。
* **`SWAP` (0x23, 35)**：交换栈顶两个元素的位置。
* **`SZP0..2` (0x13..0x15)**：分别设置区域指针 $zp0, zp1, zp2$ 绑定到 Zone 0 或 Zone 1。
* **`SZPS` (0x16, 22)**：同时将全部三个区域指针绑定到指定区域。

### U–W 系列指令
* **`UTP` (0x29, 41)**：取消触碰状态（Un-touch Point）。清除点的移动标记，使其能够在随后的 `IUP` 指令中接受平滑内插。
* **`WCVTF` (0x70, 112)**：将未缩放设计值写入 CVT。
* **`WCVTP` (0x44, 68)**：将已缩放像素网格值写入 CVT。
* **`WS` (0x42, 66)**：写入 Storage 暂存寄存器。

通过这套完备严谨的虚拟机微指令体系，TrueType 赋予了字形设计师在最苛刻的屏幕像素环境下自由掌控每一个黑白点阵边界的绝对权力。
---

## E.5 实战演练：大写字母 'H' 的完整虚拟机字节码执行跟踪（Instruction Execution Trace）

为了彻底理解 TrueType 虚拟机的微观运作机制，我们以大写字母 'H' 为例，完整跟踪光栅化引擎在执行 `glyf` 表内部字节码时的操作数栈、寄存器与控制点坐标变化。

### 1. 字母 'H' 的几何控制点拓扑：
字母 'H' 由 12 个关键控制点构成（全部为在线点 On-curve Points）：
* 左立柱（Left Stem）：点 0（左下）、点 1（右下）、点 2（右上）、点 3（左上）；
* 中间横梁（Crossbar）：点 4（左下交点）、点 5（右下交点）、点 6（右上交点）、点 7（左上交点）；
* 右立柱（Right Stem）：点 8（左下）、点 9（右下）、点 10（右上）、点 11（左上）。
此外，系统自动追加两个幻影点（Phantom Points）：点 12（原点，X=0）与点 13（前进宽度点，X=AdvanceWidth）。

### 2. Y 轴方向网格对齐指令流执行跟踪：

```tt-assembly
/* 步骤 1：将投影向量与自由向量同时设置为 Y 轴 (0, 1) */
SVTCA[y]

/* 步骤 2：对齐基线 */
/* 将点 0（左立柱底端）直接对齐到最近的物理像素网格边界，并标记为已触碰 (Touched) */
PUSHB[000] 0
MDAP[round]

/* 步骤 3：以点 0 为基准，拉伸并锁定左立柱高度 */
/* 设置参考点 rp0 = 0 */
PUSHB[000] 0
SRP0
/* 将点 3（左立柱顶端）移动到距 rp0 经 CVT 切入控制的标准大写字高处 */
PUSHB[001] 3 1  /* 参数：目标点 3，CVT 槽位 1 (CapHeight) */
MIRP[round,min,set_rp0] /* 移动后将 rp0 自动更新为点 3 */

/* 步骤 4：以大写字高为基准，平移右立柱顶端与横梁 */
/* 将点 10（右立柱顶端）与点 3 对齐在同一水平线上 */
PUSHB[000] 10
ALIGNRP

/* 将点 0 与点 9（右立柱底端）对齐到基线 */
PUSHB[000] 0
SRP0
PUSHB[000] 9
ALIGNRP

/* 步骤 5：定位横梁并锁定横梁厚度 */
/* 沿 Y 轴内插横梁下沿点 4 的位置 */
PUSHB[002] 4 0 3 /* 目标点 4，参考点 0 与 3 */
IP
/* 以点 4 为基准，向上锁定横梁厚度（读取 CVT 槽位 2: BarHeight） */
PUSHB[000] 4
SRP0
PUSHB[001] 7 2
MIRP[round,min,color_black]

/* 步骤 6：全局平滑内插 Y 轴所有剩余未触碰点 */
IUP[y]
```

### 3. X 轴方向网格对齐指令流：

```tt-assembly
/* 切换至 X 轴方向 (1, 0) */
SVTCA[x]

/* 对齐左侧轴承 (LSB) */
PUSHB[000] 0
MDAP[round]

/* 锁定左立柱宽度（从 CVT 槽位 3 读取 StdVW 垂直主干宽） */
PUSHB[000] 0
SRP0
PUSHB[001] 1 3
MIRP[round,min,set_rp0]

/* 锁定右立柱位置与宽度 */
/* 读取 CVT 槽位 4 (立柱间距)，将点 8 平移到正确间距 */
PUSHB[001] 8 4
MIRP[round,min,set_rp0]
/* 以点 8 为基准锁定右立柱宽度（点 9） */
PUSHB[001] 9 3
MIRP[round,min,color_black]

/* 横梁左右端点对齐到立柱内侧边 */
PUSHB[000] 1
SRP0
PUSHB[001] 4 7
ALIGNRP
ALIGNRP

PUSHB[000] 8
SRP0
PUSHB[001] 5 6
ALIGNRP
ALIGNRP

/* 最终对齐右侧幻影点（锁定字符总前进字宽） */
PUSHB[000] 9
SRP0
PUSHB[001] 13 5 /* CVT 槽位 5: 推荐前进字宽 */
MIRP[round,set_rp0]

/* 全局平滑内插 X 轴所有剩余未触碰点 */
IUP[x]
```

通过这一系列仅占用约 60 字节紧凑机器码的指令，字母 'H' 在从 9 像素到 200 像素的任意屏幕分辨率下，均能呈现绝对笔直、对称、且粗细毫无波动的纯净像素晶格！
---

## E.6 图形状态机（Graphics State）24 维变量全景字典

在 TrueType 虚拟机执行期间，图形状态机（Graphics State）维护着一套直接决定所有几何测量与网格吸附行为的全局环境量：

| 状态机变量名 | 数据类型 | 初始默认值 | 相关的读取与设置指令 | 物理排版语义与控制行为 |
| :--- | :--- | :--- | :--- | :--- |
| `auto_flip` | Boolean | `true` | `FLIPON`, `FLIPOFF` | 是否自动翻转极性方向错误的笔画控制点 |
| `control_value_cut_in` | F26Dot6 | `17/16` (68) | `SCVTCI` | CVT 强行吸附门限值（当轮廓尺寸与 CVT 偏差小于此值时强制锁死） |
| `delta_base` | uint16 | `9` | `SDB` | Delta 指令激活的起始基础字号（PPEM） |
| `delta_shift` | uint16 | `3` | `SDS` | Delta 微位移缩放步长（$1/2^{\text{delta\_shift}}$ 像素） |
| `dual_projection_vector` | Unit Vector | $(1, 0)$ | `SPVTCA`, `SPVTL`, `SPVFS` | 在未经变换的原始设计轮廓上测量初始距离的单位向量 |
| `freedom_vector` | Unit Vector | $(1, 0)$ | `SFVTCA`, `SFVTL`, `SFVFS`, `SFVTPV` | 点被允许移动的物理自由轴向单位向量 |
| `instruct_control` | uint8 | `0` | `INSTCTRL` | 全局指令执行掩码（Bit 0: 关闭网格对齐; Bit 1: 忽略默认参数） |
| `loop` | uint16 | `1` | `SLOOP` | 循环计数器（后续多点移动指令连续执行的次数） |
| `minimum_distance` | F26Dot6 | `1.0` (64) | `SMD` | 相对移动时保持的两笔画最小物理保护间距（防止坍缩重叠） |
| `projection_vector` | Unit Vector | $(1, 0)$ | `SPVTCA`, `SPVTL`, `SPVFS` | 距离投影测量轴向单位向量 |
| `round_state` | State | `Round to Grid` | `RTG`, `RTHG`, `RTDG`, `RDTG`, `RUTG`, `ROFF`, `SROUND` | 当前数值量化为像素网格的四舍五入规则引擎 |
| `rp0` | Point Index | `0` | `SRP0`, `MDRP`, `MIRP` | 参考点 0（作为相对位移的起点锚点） |
| `rp1` | Point Index | `0` | `SRP1` | 参考点 1（用于内插指令 IP 的左基准） |
| `rp2` | Point Index | `0` | `SRP2` | 参考点 2（用于内插指令 IP 的右基准） |
| `scan_control` | uint16 | `0` | `SCANCTRL` | 极小字号下辍笔（Dropout）保护模式激活阈值 |
| `single_width_cut_in` | F26Dot6 | `0.0` | `SSWCI` | 单笔画全局宽度统一吸附阈值 |
| `single_width_value` | F26Dot6 | `0.0` | `SSW` | 全局单笔画标准物理宽度 |
| `zp0` | Zone Pointer | `1` | `SZP0`, `SZPS` | 目标点所在的几何区域指针（Zone 0 黄昏区或 Zone 1 轮廓区） |
| `zp1` | Zone Pointer | `1` | `SZP1`, `SZPS` | 参考点 1 所在的几何区域指针 |
| `zp2` | Zone Pointer | `1` | `SZP2`, `SZPS` | 参考点 2 所在的几何区域指针 |

---

## E.7 黄昏区（Twilight Zone / Zone 0）的幽灵点力学

在复杂的字形 Hinting 中，字体设计师经常需要在字形轮廓外部构筑临时辅助几何结构（例如两条切线的虚交点、两立柱正中轴线、或外接圆圆心），但这些辅助点**在最终字形光栅化时绝对不能被渲染成黑色像素**！

TrueType 专门开辟了一个与当前真实字形平行的虚拟内存区域——**黄昏区（Zone 0）**：
* 内部所有点均为临时的“幽灵点（Ghost Points）”；
* 通过将区域指针 `SZP0` 或 `SZPS` 设置为 0，所有几何微调指令（如 `ALIGNPTS`, `IP`, `ISECT`, `MDRP`）均可作用于黄昏区；
* 设计师可以先在黄昏区计算出完美的对称几何中心，再将真实字形（Zone 1）中的轮廓点绑定并内插到该中心点上，随后退出。当光栅化引擎绘制文字时，Zone 0 的数据被直接丢弃，实现了纯粹、无瑕且极度严谨的隐形空间工程学！
---

## E.8 Delta 指令人工微调实战：小写字母 'e' 的 11 像素防粘连微调

在 11 像素（PPEM = 11）这样极端的超低分辨率下，小写字母 'e' 的内腔留白只有 1 到 2 个像素。如果完全依赖数学四舍五入，横梁上方的圆弧往往会因半网格吸附与横梁粘连在一起，导致字母 'e' 变成一个实心的黑块。

TrueType 字体工程师利用 `DELTAP` 指令进行精妙的人工微干预：

```tt-assembly
/* 针对小写字母 'e' 的顶部拱门最高点（点 5） */
/* 当且仅当 PPEM == 11 时，将点 5 向上微挪 2/8 个像素 (nudge = +2) */
/* 计算 arg: (2 + 8) * 16 + (11 - 9) = 10 * 16 + 2 = 162 */
PUSHB[001] 162 5
DELTAP1

/* 当且仅当 PPEM == 11 时，将横梁下沿（点 8）向下微挪 1/8 像素 (nudge = -1) */
/* 计算 arg: (-1 + 8) * 16 + (11 - 9) = 7 * 16 + 2 = 114 */
PUSHB[001] 114 8
DELTAP1
```

在 11 像素屏幕上，这两条微调指令瞬间拉开了横梁与圆弧之间整整 $\frac{3}{8}$ 像素的物理净空间。在光栅化扫描转换器进行中心点采样时，横梁上方恰好露出了一排干净清澈的白色背景像素——正是这种人工微调与自动算法的完美熔铸，铸就了数字字体在屏幕显示史上的伟大奇迹！
---

## E.9 轮廓平移与点序列平移指令全解（`SHP`, `SHC`, `SHZ`, `SHPIX`）

在 TrueType 中，除了单点移动指令外，虚拟机提供了极其强大的批量几何平移指令集：

### 1. `SHP[0..1]`（Shift Point / 随动点平移）
* **操作码**：`0x32 (0)` 针对 $rp2$；`0x33 (1)` 针对 $rp1$；
* **堆栈输入**：点编号序列 $p_1, p_2, \dots, p_k$（由 `loop` 计数器决定数量）；
* **执行语义**：计算参考点（$rp1$ 或 $rp2$）在当前 Hinting 过程中所经历的累计平移位移向量：
  $$\Delta \mathbf{d} = \mathbf{x}_{\text{current}}(rp) - \mathbf{x}_{\text{original}}(rp)$$
  随后，将堆栈中弹出的目标点 $p_i$ 沿自由向量 $\vec{f}$ 平移完全相同的标量距离！这保证了复杂衬线或装饰突起能够完美追随主干骨架平移，而不发生任何几何变形。

### 2. `SHC[0..1]`（Shift Contour / 整体轮廓平移）
* **操作码**：`0x34` / `0x35`；
* **堆栈输入**：轮廓索引编号 $c$；
* **执行语义**：不仅平移单个控制点，而是**将指定轮廓 $c$ 上的所有在线点与脱线点作为刚体整体平行平移**！在西文字符 'i' 与 'j' 的圆点轮廓对齐中，只需移动圆点上的一个极值点，随后调用 `SHC`，整个实心圆点便能毫无形变地瞬间同步平移。

### 3. `SHPIX`（Shift Points by Pixel / 绝对像素平移）
* **操作码**：`0x38 (56)`；
* **堆栈输入**：位移标量 $d$（单位：26.6 定点像素数）与点序列；
* **执行语义**：直接沿自由向量将点平移指定的绝对像素距离，常用于强制微调孤立标点与下划线基线。

---

# 附录 F：METAFONT 与 MetaPost 技术参考指南（METAFONT and Its Derivatives）

1977 年，高德纳在构思 TeX 的同时，深刻认识到传统的“点阵像素描画”与“刚性轮廓录入”无法从根本上解决文字随磅重、笔画倾角与纸张墨晕动态演变的排印本质。他开创性地开发了 **METAFONT 语言**，将书法家手中的毛笔与平头硬笔抽象为几何运笔过程，确立了全人类首个**纯声明式数学方程驱动的参数化字体设计范式**。随后，高德纳的弟子约翰·霍比（John Hobby）在此基础上研发了能够直接输出矢量 PostScript 曲线的 **MetaPost** 系统，开源社区更演化出了 MetaFog、METATYPE1 以及由波兰字体大师博古斯瓦夫·雅茨科夫斯基（Bogusław Jackowski）重铸的 Antykwa Półtawskiego 经典字族。

本附录将对 METAFONT 内部声明式方程求解器的线性代数机制、画笔包络线微分几何理论、转向数定理（Turning Number Theorem）、Computer Modern 家族全部 62 个神圣设计参数词典以及从参数化源文件向现代矢量字体转化的 MF2PT1 流水线进行深度解构。

---

## F.1 METAFONT 编程语言与声明式几何方程求解器

在 METAFONT 代码中，设计师从来不以过程式命令赋值坐标（如传统编程中的 `x = 5; y = 10`），而是直接书写一组平等的联立代数方程：

```metafont
x1 = x2 + 0.5w;
y1 = y2 = 0.5h;
z1 - z2 = whatever * (dir 30);
z3 = 0.5[z1, z2];
```

METAFONT 解释器内部运行着一个极其高效的**动态符号线性方程求解机（Linear Equation Solver）**：

::: tip METAFONT 方程求解网络与未定元胶囊（Capsule）环（Figure F-1, F-2）
![METAFONT 方程网络（Figure F-1）](/images/fonts-encodings/fig-app-f1.png)
*METAFONT 方程网络（Figure F-1）*
:::

*图 F-1：METAFONT 内部变量依赖拓扑。每个未定未知数被包装为一个“胶囊（Capsule）”，并在内存中维护一个双向依赖环。*

::: tip 线性代数高斯消元与解空间坍缩（Figure F-2）
![高斯消元解空间（Figure F-2）](/images/fonts-encodings/fig-app-f2.png)
*高斯消元解空间（Figure F-2）*
:::

*图 F-2：当新的线性约束输入时，解释器立即执行高斯-约旦消元法（Gauss-Jordan Elimination）：将已知变量代入其余胶囊，缩减未知自由度，直到整个几何系统完全定解。*

### 1. 核心符号表示理论
每个内部数值被表示为一个仿射线性多项式：

$$V = c_0 + c_1 X_1 + c_2 X_2 + \dots + c_k X_k$$

* 当用户声明 `z1 = z2 + (10, 20)` 时，系统并不强求立即知道 $z1$ 或 $z2$ 的绝对坐标，而是建立等式约束：$X_{z1} - X_{z2} = 10$ 与 $Y_{z1} - Y_{z2} = 20$；
* 解释器实时检测方程组的秩（Rank）：若方程出现矛盾则报错报告过度约束（Inconsistent equation）；若自由度未满，程序继续向下解析，直到后续代码提供了足够的几何切线或边界约束，整个方程网络瞬间坍缩收敛出唯一的精确浮点解！

### 2. 小写字母 'n' 的纯数学参数化设计实战

以下源码展示了如何用 METAFONT 严密书写一个带双立柱衬线、平滑拱门与动态笔宽的小写拉丁字母 'n'：

```metafont
beginchar(110, 7pt#, 6pt#, 0pt#);
  u# = 1pt#; define_pixels(u);
  numeric x_height, oo, stem, join, serif_tip, serif_height, delta, offset;
  x_height = 5.1u; oo = .2u; stem = 1.1u; join = .2u;
  serif_tip = .2u; serif_height = .7u; delta = .033u; offset = .125u;

  % 左立柱下端与上端点
  z4 = (1.6u, delta); penpos4(stem, 180);
  x3 = x4 + offset; y3r = x_height;
  x3l - x3r = stem; y3l - y3r = .5serif_tip; z3 = .5[z3l, z3r];
  penstroke z3e .. {down}z4e;

  % 右立柱与拱门相交点
  x11 = w - 1.65u; y11 = y4; penpos11(stem, 180);
  y10 = y8 = .7x_height; z8 = whatever[z3, z4];
  z10 - z11 = whatever * (z3 - z4);
  z10l - z10r = z3l - z3r; z10 = .5[z10l, z10r];

  % 拱门最高张力圆弧
  penpos9(.87[join, stem], -136); y9l = x_height + oo; x9 = .68[x8, x10];
  z8' = whatever[z11, z10]; y8' = 1.25x_height;
  penpos8(join, angle(z8' - z8) - 90);
  penstroke z8e{z8' - z8} .. tension 1.5 .. z9e{right} .. z10e -- z11e;

  % 底部衬线装配
  numeric serif; serif = x11r - x12 = 1u;
  x7 - x4l = serif; x3r - x1 = .95serif; x4r - x5 = .9serif; x14 - x11l = .8serif;
  y1l = y3l; penpos1(serif_tip, -90); z2 = z3l;
  penpos2(1.25serif_height, angle(direction 0 of (z3l .. {down}z4l)));
  penstroke z1e{right} .. z2e;

  if (x7 - x4 + .2u + x11 - x12 > x11 - x4):
    x7 := .5[x4, x11] - .1u;
    x12 := .5[x4, x11] + .1u;
  fi;

  penpos5(serif_tip, -90); penpos7(serif_tip, -90);
  penpos12(serif_tip, -90); penpos14(serif_tip, -90);
  penpos6(serif_height, -90); penpos13(serif_height, -90);
  y5r = y7r = y12r = y14r = 0; z6r = z4; z13r = z11;
  penstroke z5e{right} .. z6e & z6e .. {right}z7e;
  penstroke z12e{right} .. z13e & z13e .. {right}z14e;
endchar;
```

#### 循环测试字重演进：
只需包裹一层 `for` 循环，令 `stem = (i/63)[join, 2.2u]`，METAFONT 便能在一瞬间自动生成 64 档从 Hairline 到 Ultra-Black 的极其饱满匀称的字重连续变体！

---

## F.2 画笔几何学（Penspeck）与包络线光栅化

与现代字体将字形视为由空心多边形轮廓构成的“皮囊”不同，METAFONT 认为**文字是由一支具有特定物理几何形状的画笔（Pen）沿着一条骨架轨迹（Path）运动而扫掠出的实体墨迹**！

::: tip 凸多边形画笔 Penspeck 离散网格化（Figure F-3, F-4）
![Penspeck 画笔结构（Figure F-3）](/images/fonts-encodings/fig-app-f3.png)
*Penspeck 画笔结构（Figure F-3）*
:::

*图 F-3：画笔规范体 `penspeck` 的离散化。椭圆画笔首先被投影并多边形化为由一系列网格偏移向量构成的离散凸包（Convex Hull）。*

::: tip 画笔扫掠包络线（Envelope Tracing）微积分模型（Figure F-4）
![画笔包络线微分轨迹（Figure F-4）](/images/fonts-encodings/fig-app-f4.png)
*画笔包络线微分轨迹（Figure F-4）*
:::

*图 F-4：包络线微分方程：当具有中心点 $\mathbf{z}(t)$ 与凸包顶点 $\mathbf{v}_i$ 的画笔沿轨迹行进时，墨迹边界由外侧切线法向量决定。*

数学上，画笔扫掠区域（Envelope）的外边缘曲线方程为：

$$\mathcal{E}(t) = \mathbf{z}(t) + \mathbf{v}_{\text{active}}(t)$$

其中活动顶点 $\mathbf{v}_{\text{active}}(t)$ 满足：画笔在该顶点处的向外法向量与骨架曲线在 $t$ 时刻的切线向量严格平行！高德纳设计了精妙的包络线追踪算法（Envelope Tracing Algorithm），将该微积分过程无缝映射为离散 Bresenham 直线与圆弧生成器的协同运笔。

---

## F.3 转向数定理（Turning Number Theorem）与拓扑环绕数

在评估复杂封闭贝塞尔轮廓的有效性与合法性时，METAFONT 引入了微分拓扑学中的**转向数定理（Turning Number Theorem）**：

::: tip 转向数定理与自相交环绕拓扑（Figure F-5, F-6）
![转向数拓扑判定（Figure F-5）](/images/fonts-encodings/fig-app-f5.png)
*转向数拓扑判定（Figure F-5）*
:::

*图 F-5：平面光滑闭曲线 $\mathcal{C}$ 切线向量在单位圆上的高斯映射（Gauss Map）。切线向量沿曲线完整遍历一圈所旋转的总角度，必须是 $2\pi$ 的整数倍！*

::: tip 曲线拓扑奇异点与尖点消除（Figure F-6）
![曲线奇异点自愈（Figure F-6）](/images/fonts-encodings/fig-app-f6.png)
*曲线奇异点自愈（Figure F-6）*
:::

*图 F-6：当曲线发生自相交（Self-intersection）或出现曲率无限大的奇异尖点（Cusps）时，转向数发生突变，METAFONT 自动启动切分与外轮廓布尔提取。*

对于一条无自相交的简单正向闭合路径，其全总曲率积分恒等于 $2\pi$（转向数 $T = +1$）：

$$\frac{1}{2\pi} \oint_\mathcal{C} \kappa(s) \, ds = T \in \mathbb{Z}$$

这一严格的数学判据，使 METAFONT 能够自动识别轮廓是外边界还是内镂空孔洞（如字母 'O' 的内部），并在光栅化时彻底杜绝翻转走样的发生。

---

## F.4 Computer Modern 字体家族 62 维全量参数参考词典

Computer Modern（CM）是高德纳采用 METAFONT 编写的经典字体家族。整个庞大的字族（包含 75 款独立字库，覆盖 5pt 到 17pt 的光学比例尺）全部由一组定义在 `cmbase.mf` 与各个字体驱动文件中的宏观几何参数所控制。

### 1. 垂直尺寸与高度参数（Vertical Dimensions）
* `u#`：基本设计单位宽度（Unit width in sharp units / points）；
* `width_corr#`：字符宽度微调补偿量；
* `x_height#`：小写字母 'x' 的主干高度（Ex-height）；
* `cap_height#`：大写正文字母高度（Cap height）；
* `asc_height#`：小写字母升部高度（如 'b', 'd', 'h' 的顶部）；
* `desc_depth#`：小写字母降部深度（如 'p', 'q', 'y' 的底部）；
* `body_height#`：带重音大写字母或最高括号的极限包围盒顶部；
* `fig_height#`：等宽阿拉伯数字的标准高度；
* `math_axis#`：数学符号中轴线高度（分数线与加减号的中心高度）；
* `bar_height#`：小写字母 'e' 的横梁高度与字母 'A', 'H' 的交叉横杠高度；
* `comma_depth#`：逗号与分号尾巴探入基线以下的深度。

### 2. 主干与笔画宽度参数（Stem and Stroke Widths）
* `hair#`：最细衬线或连接线画笔直径（Hairline thickness）；
* `stem#`：小写正文字母主垂直干笔画宽度（Main vertical stem）；
* `curve#`：小写圆弧字母弯角处最大膨胀宽度（如字母 'o', 'c' 的两侧最厚处）；
* `ess#`：字母 's' 中部倾斜主梁的最厚宽度；
* `flare#`：水滴状笔画端点（Teardrop terminal）的球头最大直径（如字母 'a', 'c', 'f', 'r' 的端部）；
* `dot_size#`：小写字母 'i', 'j' 上方圆点与标点句号的直径；
* `cap_hair#`：大写字母最细笔画厚度；
* `cap_stem#`：大写字母主垂直干笔画宽度；
* `cap_curve#`：大写圆弧字母两侧最大弧厚（如字母 'O', 'C', 'G'）；
* `cap_ess#`：大写字母 'S' 中部斜干最大厚度；
* `rule_thickness#`：数学公式分数线与方框线条的标准物理厚度；
* `thin_join#`：对角斜线交叉连接处的极小理论过渡宽度。

### 3. 衬线与括号连接参数（Serifs and Brackets）
* `dish#`：衬线底部的凹陷微弧度（Serif dish curvature）；
* `bracket#`：衬线与主干之间的过渡圆角支架高度（Serif bracket height）；
* `jut#`：小写字母水平衬线向外挑出的水平长度（Serif protrusion）；
* `cap_jut#`：大写字母衬线外挑长度；
* `beak_jut#`：大写字母 'E', 'F', 'T' 臂部尖喙（Beak）向外突出的水平长度；
* `beak#`：尖喙的垂直切削深度；
* `serif_drop#`：单向悬挂衬线向下滑落的垂直距离；
* `stem_corr#`：小写字母主干交汇处的切入收缩量；
* `vair_corr#`：细笔画在连接拐角处的补偿膨胀量；
* `slab#`：粗衬线字体（Slab Serif）中方形水平衬线的厚度；
* `cap_bar#`：大写字母横杠厚度；
* `cap_band#`：大写字母封闭环带厚度；
* `cap_notch_cut#`：大写字形锐角内侧为了防止墨水堆积而切除的凹槽深度（Notch cut）。

### 4. 光学修正与高级形态参数（Optical Corrections & Style）
* `o#`：曲线或尖角在越过基线或顶线时的光学过冲量（Overshoot），消除人眼视觉缩小错觉；
* `apex_o#`：大写字母 'A', 'V', 'W' 尖顶或尖底处的额外过冲量；
* `apex_corr#`：尖顶点连接处的几何回缩修正；
* `slant`：字体的倾斜率 $\tan(\theta)$（正体为 0.0，斜体通常为 0.25）；
* `fudge`：针对低分辨率或特殊黑度的全比例缩放软调整因子；
* `math_spread`：数学公式符号之间的垂直松弛度；
* `superness`：超椭圆参数（Superellipse factor），控制曲线饱满度（通常 $0.707 \dots 0.75$）；
* `superpull`：超椭圆内侧向内吸附拉扯的修正系数；
* `beak_darkness`：尖喙区域黑度衰减权重。

### 经典 CM 字形在 10 磅下的参数对拍表（CMR10 vs CMBX10 vs CMTI10 vs CMSS10 vs CMTT10）：

| 参数名 | `cmr10`（正体） | `cmbx10`（粗体） | `cmti10`（西文斜体） | `cmss10`（无衬线） | `cmtt10`（等宽打字机） |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `u#` | $20/36\text{ pt}$ | $23/36\text{ pt}$ | $18.5/36\text{ pt}$ | $19/36\text{ pt}$ | $21/36\text{ pt}$ |
| `slant` | $0.0$ | $0.0$ | $0.25$ | $0.0$ | $0.0$ |
| `x_height#` | $155/36\text{ pt}$ | $160/36\text{ pt}$ | $155/36\text{ pt}$ | $160/36\text{ pt}$ | $155/36\text{ pt}$ |
| `cap_height#` | $250/36\text{ pt}$ | $250/36\text{ pt}$ | $250/36\text{ pt}$ | $250/36\text{ pt}$ | $235/36\text{ pt}$ |
| `hair#` | $9/36\text{ pt}$ | $13/36\text{ pt}$ | $11/36\text{ pt}$ | $18/36\text{ pt}$ | $25/36\text{ pt}$ |
| `stem#` | $24/36\text{ pt}$ | $40/36\text{ pt}$ | $23/36\text{ pt}$ | $25/36\text{ pt}$ | $25/36\text{ pt}$ |
| `curve#` | $29/36\text{ pt}$ | $45/36\text{ pt}$ | $30/36\text{ pt}$ | $25/36\text{ pt}$ | $25/36\text{ pt}$ |
| `jut#` | $28/36\text{ pt}$ | $36/36\text{ pt}$ | $0.0$ | $0.0$ | $23/36\text{ pt}$ |
| `bracket#` | $20/36\text{ pt}$ | $20/36\text{ pt}$ | $0.0$ | $0.0$ | $14/36\text{ pt}$ |

---

## F.5 MetaPost、MetaFog 与现代矢量转换管线

1990 年代，约翰·霍比在 MetaPost 中用三次样条曲线平滑求解器替换了 METAFONT 的点阵光栅化模块，使其能够直接生成工业级的 EPS（Encapsulated PostScript）矢量输出。

### 1. MetaFog：从轮廓到骨架的矢量重构
理查德·柯施（Richard Kinch）开发了著名的 MetaFog 引擎：
* 拦截 METAFONT 生成的高分辨率点阵位图；
* 对离散像素进行多项式边界拟合与拐点提取；
* 将离散的黑色墨迹还原为光滑的三次贝塞尔曲线。

### 2. MF2PT1 与 Antykwa Półtawskiego 革命
波兰著名字体工程师博古斯瓦夫·雅茨科夫斯基与雅努什·诺瓦茨基（Janusz M. Nowacki）推出了 **METATYPE1** 架构，并以此成功重铸了波兰国家级经典字族 Antykwa Półtawskiego：
1. 运行 MetaPost 解析带有提示锚点的 METAFONT 源码，生成无损的 PostScript 贝塞尔矢量轮廓；
2. 提取源码中定义的极值点与笔画特征，自动将其转换为 PostScript Type 1 规范的 `hstem` 与 `vstem` 提示；
3. 将字符轮廓打包入 Type 1 二进制格式，使古老而深奥的 METAFONT 参数化书法字库，彻底无缝融入当今现代桌面的 OpenType 与 PDF 矢量印刷工作流！
---

## F.6 光学缩放（Optical Scaling）的几何物理学：从 CMR5 到 CMR17

在金属活字时代，雕刻师在雕刻小磅活字（如 5 磅）时，绝对不是把 10 磅的大字机械等比例缩小。如果机械缩小，小字的细笔画会因为低于人眼分辨率极限而彻底消失，字母内腔（Counter）会因为墨水堆积而变成黑团。

高德纳通过 METAFONT 的参数化体系，在 Computer Modern 中完美复活了这门失传已久的**光学比例雕刻技艺**：

### 1. CMR 家族不同磅值的设计参数对比表：

| 参数项 | `cmr5` (5pt) | `cmr7` (7pt) | `cmr10` (10pt) | `cmr12` (12pt) | `cmr17` (17pt) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **相对字宽比率** (`u / pt`) | $0.065$ | $0.058$ | $0.055$ | $0.052$ | $0.048$ |
| **粗细对比度** (`stem / hair`) | $1.75$ (极低对比度) | $2.10$ | $2.66$ | $3.05$ | $3.80$ (高对比度) |
| **x 字高占比** (`x_height / cap_height`) | $0.68$ (超大字高) | $0.65$ | $0.62$ | $0.60$ | $0.56$ (修长典雅) |
| **衬线长度** (`jut / pt`) | $0.095$ (强壮突出) | $0.084$ | $0.077$ | $0.072$ | $0.065$ (短小细腻) |

从表中可以清晰看出高德纳的神圣规律：
* **5 磅微型字（CMR5）**：笔画粗细对比极低（细笔画被大幅加粗），x 字高比例极大，字形整体横向膨胀变宽，衬线粗壮外挑，确保在极端缩微环境下依旧坚挺清晰；
* **17 磅标题字（CMR17）**：笔画粗细对比极其强烈（细笔画如蛛丝般纤细，主干厚重饱满），字身修长收敛，展现出顶级古典活字的华贵排印气派！

---

## F.7 波兰 METATYPE1 架构与 Antykwa Półtawskiego 的现代重塑

1990 年代末，波兰著名字体工程师博古斯瓦夫·雅茨科夫斯基与雅努什·诺瓦茨基深刻认识到，METAFONT 生成的位图虽然在 TeX 中表现优异，但在需要无极缩放的 PDF 与现代 PostScript 打印机中受制于固定分辨率。

他们开发了 **METATYPE1 宏包**，对 METAFONT 进行了颠覆性的改造：
1. **画笔剥离**：将 METAFONT 的画笔扫掠运算彻底替换为显式轮廓边界微分追踪；
2. **极值点自适应切分**：自动计算曲线在水平和垂直方向的切线极值点，并在极值点处强制切断为独立的三次贝塞尔曲线段；
3. **自动化 Hinting 编译器**：通过分析控制点之间的距离，自动生成符合 PostScript Type 1 规范的 `hstem`、`vstem` 与动态提示替换（Hint Substitution）指令块！

利用这套宏伟的架构，他们完整复刻并开源了由亚当·波乌塔夫斯基（Adam Półtawski）在 1928 年设计的波兰国宝级字体 **Antykwa Półtawskiego**。这部横跨七十年的数字字体工程史诗，彻底证明了高德纳声明式参数几何哲学的无限生命力。
---

## F.8 METAFONT 参数代数约束系统与几何和谐方程

在设计 Computer Modern 字体时，高德纳并未将 62 个参数视为相互孤立的旋钮，而是建立了一套极其深邃的**代数约束拓扑网（Algebraic Dependency Network）**：

### 1. 衬线与主干的和谐方程：
* **衬线厚度与主干协调**：
  $$\text{bracket\#} = \min\left(20/36\text{ pt\#}, \; 0.8 \times \text{stem\#}\right)$$
  当字重大幅增加（如黑体 `cmbx10`，`stem#` 从 24 暴增至 40）时，衬线托架的高度不能无限制增长，否则整个字母底座会变成实心黑块；
* **光学过冲补偿方程**：
  对于圆弧字母（如 'O'）越过基线的下垂过冲量 $o\#$ 与尖顶字母（如 'A'）的顶点过冲量 $\text{apex\_o}\#$：
  $$\text{apex\_o\#} = \frac{4}{3} \times o\#$$
  因为尖锐单点在人眼中造成的收缩错觉，远比圆弧平缓接触造成的视觉错觉强烈得多，必须施加更大的物理几何代数过冲！

---

## F.9 高德纳数学排印美学哲学与数字字体未来

在《Digital Typography》与图灵奖演讲中，高德纳曾写下排印技术史上的传世箴言：
> “字型不是僵死的墨迹标本，而是一组由活生生的数学思想所驱动的有机函数。”

传统的铅字活字将字母永久定格在金属方块之中，二十世纪初的光学照排又将其锁死在静止的感光胶片上；而 METAFONT 则将文字解放为微分几何与代数方程的优雅舞步。

尽管今天纯粹书写 METAFONT 代码的字型设计师日渐稀少，但其播撒下的思想种子——从 PostScript 贝塞尔曲线、OpenType 状态机、到可变字体（Variable Fonts）的连续设计轴与自动 Hinting 算法——已化作当今全球数字排印文明生生不息的底层血脉。
---

## F.10 METAFONT 8 方位离散光栅运笔算法（The Eight Octants of Raster Graphics）

为了在纯整数网格上无损追踪画笔包络线，高德纳将二维平面严格划分为 8 个连续的角度卦限（Octants）：
* **卦限 1**：$0^\circ \le \theta < 45^\circ$（主移动轴为 $+X$，辅助移动轴为 $+Y$）；
* **卦限 2**：$45^\circ \le \theta < 90^\circ$（主移动轴为 $+Y$，辅助移动轴为 $+X$）；
* **卦限 3 至 8**：依次类推覆盖全平面。

在每一个卦限内部，画笔凸包与外界切线的接触顶点是**严格恒定不变的**！当运笔轨迹从卦限 1 跨越 $45^\circ$ 进入卦限 2 时，接触顶点瞬间发生跃迁切替。高德纳证明了：通过将曲线轨迹切分为单调卦限段，画笔扫掠运算可以完全退化为基于加减法与位移的纯整数判别式递推，在 1970 年代运行速度极慢的小型机上实现了每秒渲染数十个高精度字形轮廓的惊人奇迹。
---

## F.11 MetaPost 宏系统与图表排版自动化流水线

MetaPost 之所以能够从 METAFONT 中独立演进为学术出版界的图表神器，关键在于其对宏系统（Macro System）的极致扩展：
* **`btex ... etex` 桥接机制**：MetaPost 允许在图形代码中内嵌原生的 LaTeX 数学公式源码。在编译时，MetaPost 自动调用后台 TeX 引擎将公式排版为 DVI 盒子并测量其精确包围盒，再将公式轮廓无损嵌入到生成的 EPS 或 PDF 图形中；
* **图形对象（Pictures）与多重变换**：支持将一整组路径组合封装为单一图形对象（`picture`），并对其施加平移（`shifted`）、缩放（`scaled`）、旋转（`rotated`）以及倾斜（`slanted`）等高阶仿射矩阵变换，实现了全自动的学术期刊插图生产线。

---

# 附录 G：字型设计中的曲线微分几何学与样条数学理论（Differential Geometry of Curves）

在现代矢量字体工程中，字符轮廓并非简单的折线拼接，而是建立在极其严密的微分几何学与代数拓扑学基础之上。从 TrueType 采用的二次有理贝塞尔曲线（Quadratic Bézier），到 PostScript Type 1 与 OpenType CFF 采用的三次贝塞尔曲线（Cubic Bézier），再到高端书法设计中的欧拉螺线（Euler Spirals / Cornu Spirals），字体设计师在屏幕上拖动控制点所施加的每一个微小位移，都在底层激发了一场高阶张量与微积分方程的精密运算。

本附录将对字型设计涉及的核心微分几何学理论进行完整的纯数学解析：从伯恩斯坦基底（Bernstein Basis）的单位分解定理、极式（Blossom）映射、德卡斯特里奥（de Casteljau）递归细分算法、微分矢端曲线（Hodograph），到曲率公式（Curvature）、拐点（Inflection Points）判定与等距偏移曲线（Offset Curves）的非有理本质，以及欧拉角螺线在现代参数化字体轮廓拟合中的前沿应用。

---

## G.1 伯恩斯坦多项式基底与代数拓扑性质

一条定义在参数区间 $t \in [0, 1]$ 上的 $n$ 次贝塞尔曲线，在数学上定义为 $n+1$ 个几何控制点 $\mathbf{P}_0, \mathbf{P}_1, \dots, \mathbf{P}_n \in \mathbb{R}^2$ 关于 $n$ 次**伯恩斯坦基多项式（Bernstein Polynomials）**的凸组合线性叠加：

$$\mathbf{B}(t) = \sum_{i=0}^n B_{i,n}(t) \, \mathbf{P}_i, \quad t \in [0, 1]$$

其中 $n$ 次伯恩斯坦基函数由二项式系数与乘幂严格定义为：

$$B_{i,n}(t) = \binom{n}{i} t^i (1-t)^{n-i}, \quad i = 0, 1, \dots, n$$

这里 $\binom{n}{i} = \frac{n!}{i!(n-i)!}$ 为组合二项式系数。

### 核心微分几何定理与严格证明

#### 定理 1：单位分解性（Partition of Unity）
在全实数域上，所有 $n$ 次伯恩斯坦多项式的代数和恒等为 1：

$$\sum_{i=0}^n B_{i,n}(t) \equiv 1, \quad \forall t \in \mathbb{R}$$

*证明*：根据牛顿二项式定理（Binomial Theorem），对于任意实数 $a, b$，恒有 $(a + b)^n = \sum_{i=0}^n \binom{n}{i} a^i b^{n-i}$。令 $a = t$ 且 $b = 1-t$，则有：
$$\sum_{i=0}^n B_{i,n}(t) = \sum_{i=0}^n \binom{n}{i} t^i (1-t)^{n-i} = (t + (1-t))^n = 1^n = 1 \quad \blacksquare$$

**字型排印物理学意义**：单位分解性确保了贝塞尔曲线具有**仿射不变性（Affine Invariance）**！无论我们对字库进行整体平移、旋转、缩放还是施加倾斜矩阵变换，直接对控制点施加变换后的新曲线，与原曲线上每个点分别计算变换后的结果在数学上严格绝对重合！

#### 定理 2：非负性（Positivity）
当且仅当参数 $t$ 落在字形轮廓的合法物理区间 $[0, 1]$ 内时，所有基函数恒为非负：

$$B_{i,n}(t) \ge 0, \quad \forall t \in [0, 1]$$

结合定理 1，这证明了曲线上的任意一点 $\mathbf{B}(t)$ 都是控制多边形顶点的**真凸组合（Convex Combination）**，从而严格证明了**凸包性质（Convex Hull Property）**：整条字形轮廓线被严格约束在控制点围成的凸多边形内部，渲染引擎可借此实现毫秒级快速包围盒粗筛求交！

#### 定理 3：端点插值与边界切线控制（Endpoint Interpolation）
代入 $t = 0$ 与 $t = 1$，有：
$$\mathbf{B}(0) = \mathbf{P}_0, \quad \mathbf{B}(1) = \mathbf{P}_n$$
曲线在起点的切线方向平行于向量 $\mathbf{P}_1 - \mathbf{P}_0$，在终点的切线方向平行于向量 $\mathbf{P}_n - \mathbf{P}_{n-1}$。这一极其优美的几何性质，赋予了字体设计师通过直接移动前后控制点把控曲线两端连接切线的绝对权力。

#### 定理 4：递推关系与微分性质（Recurrence & Derivatives）
$$B_{i,n}(t) = (1-t) B_{i,n-1}(t) + t B_{i-1,n-1}(t)$$
$$\frac{d}{dt} B_{i,n}(t) = n \left( B_{i-1,n-1}(t) - B_{i,n-1}(t) \right)$$

---

## G.2 极式（Blossoms / Polar Forms）与多线性映射理论

由法国数学家保罗·德卡斯特里奥与拉马尔·拉姆齐（Lyle Ramshaw）提出的**极式（Polar Form，或称 Blossom 花式）理论**，将抽象繁琐的贝塞尔曲线代数运算彻底转化为优美纯粹的多线性仿射几何学。

对于一条 $n$ 次单变量多项式曲线 $\mathbf{P}(t)$，存在唯一一个关于 $n$ 个独立变量的对称多重仿射函数（Symmetric Multiaffine Map） $p(u_1, u_2, \dots, u_n)$，满足以下三大公理：
1. **全对称性（Symmetry）**：交换任意两个输入参数的次序，函数值严格不变：
   $$p(u_{\pi(1)}, u_{\pi(2)}, \dots, u_{\pi(n)}) = p(u_1, u_2, \dots, u_n)$$
2. **多重仿射性（Multiaffinity）**：固定其中任意 $n-1$ 个变量，关于剩余的一个变量是纯粹的仿射线性映射：
   $$p(\dots, \, (1-\alpha)u + \alpha v, \, \dots) = (1-\alpha) p(\dots, u, \dots) + \alpha p(\dots, v, \dots)$$
3. **对角坍缩性（Diagonal Property）**：当所有 $n$ 个参数全部取同一数值 $t$ 时，极式瞬间坍缩为原始贝塞尔曲线本身：
   $$p(t, t, \dots, t) = \mathbf{P}(t)$$

### 极式视角的控制点黄金对应律：
曲线的几何控制点 $\mathbf{P}_i$，在极式空间中具有令人惊叹的离散端点取值表达：

$$\mathbf{P}_i = p(\underbrace{0, \dots, 0}_{n-i \text{ 个}}, \, \underbrace{1, \dots, 1}_{i \text{ 个}})$$

例如对于三次贝塞尔曲线（$n=3$）：
* 起点：$\mathbf{P}_0 = p(0, 0, 0)$；
* 第一控制点：$\mathbf{P}_1 = p(0, 0, 1)$；
* 第二控制点：$\mathbf{P}_2 = p(0, 1, 1)$；
* 终点：$\mathbf{P}_3 = p(1, 1, 1)$。

在子区间 $[a, b]$ 上对曲线进行局部截取时，新曲线的控制点只需直接求值 $p(a, a, a), p(a, a, b), p(a, b, b), p(b, b, b)$，彻底终结了繁琐的坐标变换公式！

---

## G.3 升阶代数矩阵：从二次 TrueType 到三次 PostScript

在字体格式跨平台转换中，将 TrueType（二次贝塞尔曲线，$n=2$）转换为 PostScript Type 1 / OpenType CFF（三次贝塞尔曲线，$n=3$）是一项核心基础操作。**升阶（Degree Elevation）必须保证曲线在几何形状、切线方向与曲率上绝对恒定**。

### 升阶通用递推公式：
将 $n$ 次曲线升为 $n+1$ 次曲线，新的控制点 $\mathbf{P}_i^{(n+1)}$ 由旧控制点线性组合得出：

$$\mathbf{P}_i^{(n+1)} = \frac{i}{n+1} \mathbf{P}_{i-1}^{(n)} + \left(1 - \frac{i}{n+1}\right) \mathbf{P}_i^{(n)}, \quad i = 0, 1, \dots, n+1$$

### 二次转三次升阶封闭解：
设二次 TrueType 曲线由起点 $\mathbf{P}_0$、脱线控制点 $\mathbf{P}_1$ 与终点 $\mathbf{P}_2$ 定义，升阶为三次曲线后的四个控制点 $\mathbf{Q}_0, \mathbf{Q}_1, \mathbf{Q}_2, \mathbf{Q}_3$ 精确等于：

$$\begin{cases}
\mathbf{Q}_0 = \mathbf{P}_0 \\
\mathbf{Q}_1 = \mathbf{P}_0 + \frac{2}{3}(\mathbf{P}_1 - \mathbf{P}_0) = \frac{1}{3}\mathbf{P}_0 + \frac{2}{3}\mathbf{P}_1 \\
\mathbf{Q}_2 = \mathbf{P}_2 + \frac{2}{3}(\mathbf{P}_1 - \mathbf{P}_2) = \frac{2}{3}\mathbf{P}_1 + \frac{1}{3}\mathbf{P}_2 \\
\mathbf{Q}_3 = \mathbf{P}_2
\end{cases}$$

此公式在数学上严谨证明了：**任何二次贝塞尔曲线均可以毫无任何误差、100% 精确地表达为一条三次贝塞尔曲线**！反之，三次曲线由于自由度更高（具有两个独立控制点，可能包含拐点），通常无法用单一二次曲线精确表示，必须通过曲率极值点分割算法切断为多段二次曲线逼近。

---

## G.4 德卡斯特里奥（de Casteljau）递归细分算法

在光栅化碰撞检测、字符曲线相交运算与局部裁剪时，德卡斯特里奥算法提供了数值上极度稳定的几何细分手段。

### 细分三角形金字塔算法：
给定参数 $t_0 \in (0, 1)$，定义点序列的递归线性插值：

$$\mathbf{P}_i^{(k)}(t_0) = (1-t_0)\mathbf{P}_i^{(k-1)}(t_0) + t_0 \mathbf{P}_{i+1}^{(k-1)}(t_0)$$

其中 $\mathbf{P}_i^{(0)} = \mathbf{P}_i$ 为原始控制点。当 $k=n$ 时，顶峰点 $\mathbf{P}_0^{(n)}(t_0) = \mathbf{B}(t_0)$ 即为曲线上对应点的物理坐标。

细分完成后，原始曲线在 $t_0$ 处被切断为两段独立的子贝塞尔曲线：
* 左段曲线控制点序列：$\mathbf{P}_0^{(0)}, \mathbf{P}_0^{(1)}, \mathbf{P}_0^{(2)}, \dots, \mathbf{P}_0^{(n)}$；
* 右段曲线控制点序列：$\mathbf{P}_0^{(n)}, \mathbf{P}_1^{(n-1)}, \mathbf{P}_2^{(n-2)}, \dots, \mathbf{P}_n^{(0)}$。

#### Python 工业级德卡斯特里奥细分实现：
```python
def de_casteljau_subdivide(points: list, t: float = 0.5):
    """
    对任意阶贝塞尔曲线在参数 t 处进行数值无损细分
    """
    n = len(points) - 1
    pyramid = [list(points)]
    
    for r in range(1, n + 1):
        prev_row = pyramid[-1]
        next_row = []
        for i in range(len(prev_row) - 1):
            p0 = prev_row[i]
            p1 = prev_row[i + 1]
            interp = (
                (1 - t) * p0[0] + t * p1[0],
                (1 - t) * p0[1] + t * p1[1]
            )
            next_row.append(interp)
        pyramid.append(next_row)
        
    left_curve = [pyramid[r][0] for r in range(n + 1)]
    right_curve = [pyramid[n - r][r] for r in range(n + 1)]
    return left_curve, right_curve
```

### 变分缩减性质（Variation Diminishing Property）：
**贝塞尔曲线的波动幅度绝不会超过其控制多边形！** 任何一条直线与贝塞尔曲线轮廓的实际交点个数，恒小于等于该直线与对应控制多边形折线的交点个数。该定理彻底保证了字体设计师在调整控制点时，轮廓绝不会莫名其妙地产生多余的寄生波纹与褶皱震荡！

---

## G.5 微分矢端曲线（Hodograph）与速度加速度张量

贝塞尔曲线的各阶导数本身**依然是一条纯粹的贝塞尔曲线**！其控制向量构成了几何学上的**矢端曲线（Hodograph）**。

### 一阶导数（速度向量 / 切线向量）：
$$\mathbf{B}'(t) = n \sum_{i=0}^{n-1} B_{i,n-1}(t) \, (\mathbf{P}_{i+1} - \mathbf{P}_i)$$

* 曲线在起点的切线方向恒平行于向量 $\mathbf{P}_1 - \mathbf{P}_0$；
* 曲线在终点的切线方向恒平行于向量 $\mathbf{P}_n - \mathbf{P}_{n-1}$。

### 二阶导数（加速度向量）：
$$\mathbf{B}''(t) = n(n-1) \sum_{i=0}^{n-2} B_{i,n-2}(t) \, (\mathbf{P}_{i+2} - 2\mathbf{P}_{i+1} + \mathbf{P}_i)$$

二阶导向量反映了字形轮廓在行进过程中偏离直线的弯曲加速度，直接决定了下文的曲率演变。

---

## G.6 平面曲线曲率（Curvature）与微分不变量

曲率 $\kappa(t)$ 是衡量字体轮廓在某一点弯曲程度的核心不变量，其物理意义为单位弧长内切线方向角的旋转变化率：

$$\kappa(t) = \frac{x'(t)y''(t) - y'(t)x''(t)}{\left(x'(t)^2 + y'(t)^2\right)^{3/2}}$$

* **曲率半径（Radius of Curvature）**：$R(t) = \frac{1}{|\kappa(t)|}$；
* **密切圆（Osculating Circle）**：在点 $\mathbf{B}(t)$ 处沿法向量向内偏移 $R(t)$ 处的圆，与曲线在该点具有二阶切触精度；
* **拐点（Inflection Point）**：曲率变号的位置，即分子 cross product 恒等于零之处：
  $$x'(t)y''(t) - y'(t)x''(t) = 0$$
  在高质量字形设计中，二次贝塞尔曲线由于二阶导数恒为常数向量，其内部**绝对不可能出现拐点**；三次贝塞尔曲线内部**最多只能存在一个拐点**！若字符设计需要呈现“S”形平滑波浪，必须确保该拐点处的二阶曲率保持 $G^2$ 连续（曲率数值大小与正负无缝衔接），否则人眼在反射光影下会察觉到极度刺眼的“断腰”视觉残瑕！
* **奇异尖点（Cusps）**：当一阶速度向量同时归零时：$x'(t) = y'(t) = 0$。曲率在此处退化，切线发生 $180^\circ$ 倒转。

---

## G.7 等距偏移曲线（Offset Curves）的非多项式物理本质

在字体加粗（Stroke Boldening）、空心字生成（Outline Stroke）以及字形轮廓膨胀算法中，排版引擎需要沿法线方向将曲线向外推挤 $\delta$ 距离，生成**等距偏移曲线（Offset Curve / Parallel Curve）**：

$$\mathbf{C}_\delta(t) = \mathbf{C}(t) + \delta \, \mathbf{n}(t) = \mathbf{C}(t) + \delta \, \frac{\left(-y'(t), \, x'(t)\right)}{\sqrt{x'(t)^2 + y'(t)^2}}$$

### 字体工程中的终极难题：偏移曲线的非有理本质
计算机辅助几何设计（CAGD）领域的一个著名残酷定理指出：**除了平凡的直线段与圆弧之外，任何多项式贝塞尔曲线的等距偏移曲线，在数学上绝对不可能再用有限阶的有理贝塞尔曲线精确表示！**

其根源在于法向量分母中的平方根项 $\sqrt{x'(t)^2 + y'(t)^2}$ 引入了不可约化的代数分支割线。不仅如此，当偏移距离 $\delta$ 超过局部最小曲率半径 $R(t)$ 时，偏移曲线内部必然会产生极其诡异的**燕尾自相交奇异点（Swallowtail Singularities）**！

现代专业字体设计软件（如 FontLab、Glyphs、FontForge）在执行“扩大笔画轮廓”时，必须调用高阶数值逼近管线：
1. 计算曲率极大值点，将原始曲线切分为单调曲率段；
2. 依据 Tiller-Hanson 算法，在每段曲线两端估算法向量偏移控制点；
3. 检测并执行微分拓扑裁剪，彻底消除燕尾自交环；
4. 最终以微米级公差拟合出平滑封闭的高品质 OpenType 矢量轮廓。

---

## G.8 欧拉角螺线（Euler Spirals / Cornu Spirals）与现代样条

在传统三次贝塞尔曲线中，曲线的曲率通常是参数 $t$ 的高阶有理分式，其曲率分布极难保持单调或线性变化，往往导致字形高光反射线呈现轻微的扭曲（称为“曲率抖动”）。

为了追求终极的书法级光学平滑度，拉夫·莱维恩（Raph Levien）在设计 Spiro 样条引擎时，引入了经典力学与光学中的**欧拉螺线（又称柯奴螺线，Cornu Spirals / Clothoids）**。

### 欧拉螺线核心物理方程：
欧拉螺线的几何本质在于：**曲线的曲率 $\kappa$ 与弧长 $s$ 严格成正比**！

$$\kappa(s) = \frac{d\theta}{ds} = 2 a s$$

对弧长进行积分，得到切线倾角方程：

$$\theta(s) = \int_0^s \kappa(u) \, du = a s^2$$

在笛卡尔坐标系中，欧拉螺线的参数方程由著名的菲涅耳积分（Fresnel Integrals）严格定义：

$$x(s) = \int_0^s \cos(a u^2) \, du, \quad y(s) = \int_0^s \sin(a u^2) \, du$$

由于曲率随弧长完美线性渐变，两个由欧拉螺线连接的几何线段天然具备绝对完美的 $G^2$ 甚至 $G^3$ 连续性。现代前沿字体设计工具先通过欧拉螺线建立全局美学骨架，再将其自适应切分转化为标准 OpenType 三次贝塞尔曲线，实现了古代书法艺术与现代微分几何学的最高统一。
---

## G.9 几何光滑度连续性阶次（Continuity Classes: $C^k$ vs $G^k$）

在高质量字体轮廓拼接（Spline Joining）中，两个相邻贝塞尔曲线段在连接点处的平滑度，划分为**参数连续性（Parametric Continuity, $C^k$）**与**几何连续性（Geometric Continuity, $G^k$）**两大流派：

### 1. 各级连续性的微分定义：
* **$C^0$ / $G^0$ 连续（位置连续）**：两曲线段首尾相接，共用同一点：$\mathbf{B}_1(1) = \mathbf{B}_2(0)$；
* **$C^1$ 连续（一阶导数连续）**：两曲线不仅切线方向重合，且一阶导数向量的大小与方向完全相等：$\mathbf{B}_1'(1) = \mathbf{B}_2'(0)$；
* **$G^1$ 连续（切线方向连续）**：两曲线在连接点处的单位切向量平行，但模长允许不相等：
  $$\frac{\mathbf{B}_1'(1)}{\|\mathbf{B}_1'(1)\|} = \frac{\mathbf{B}_2'(0)}{\|\mathbf{B}_2'(0)\|}$$
  在字型设计中，这意味着控制点 $\mathbf{P}_2$、端点 $\mathbf{P}_3 = \mathbf{Q}_0$ 与后一曲线控制点 $\mathbf{Q}_1$ **三点严格共线**，但线段长度比可以任意调整；
* **$C^2$ 连续（二阶导数连续）**：两曲线的二阶导数向量严格相等：$\mathbf{B}_1''(1) = \mathbf{B}_2''(0)$；
* **$G^2$ 连续（曲率连续，Curvature Continuity）**：两曲线在连接点处的**曲率数值与曲率中心严格连续**：
  $$\kappa_1(1) = \kappa_2(0)$$

### 2. 为什么专业字体设计必须追求 $G^2$ 连续？
人眼视觉感知对曲率的跳跃极其敏感。在仅仅满足 $G^1$ 连续的轮廓连接处（例如圆弧平整过渡到直线的传统倒角），虽然切线没有折角，但曲率从常数（$1/R$）瞬间断崖式跌落到直线的 0。在屏幕光栅化或印刷高光下，人眼会在该拐角处清晰察觉到一条刺眼的暗影折痕（称为“光学断骨”）。

通过调节控制点使曲线在交界处达成 $G^2$ 连续，字形轮廓的曲率梳（Curvature Comb）将呈现连续光滑演变，赋予字符如水银泻地般的有机书法美感！

---

## G.10 基于矢端极值点求根的极限包围盒（BBox）极速求值算法

在字体渲染管线中，精确计算字符曲线在 X 轴与 Y 轴上的极限包围盒（Bounding Box: $x_{\min}, y_{\min}, x_{\max}, y_{\max}$）是一项每秒触发数万次的极高频操作。

由于贝塞尔曲线可能在区间内部向外隆起凸出，极限坐标并不一定出现在端点处，而是可能出现在一阶导数等于零的**极值驻点（Stationary Points）**处！

### 三次贝塞尔导数二次方程求解：
一阶导数方程 $x'(t) = 0$ 展开为一个一元二次多项式：

$$x'(t) = 3(1-t)^2(x_1 - x_0) + 6(1-t)t(x_2 - x_1) + 3t^2(x_3 - x_2) = A t^2 + B t + C = 0$$

其中系数展开为：

$$\begin{cases}
A = 3(-x_0 + 3x_1 - 3x_2 + x_3) \\
B = 6(x_0 - 2x_1 + x_2) \\
C = 3(x_1 - x_0)
\end{cases}$$

利用求根公式求出判别式 $\Delta = B^2 - 4AC$。若 $\Delta \ge 0$，求出实数根 $t = \frac{-B \pm \sqrt{\Delta}}{2A}$。筛选出落在区间 $(0, 1)$ 内部的合法根代入 $x(t)$ 求值，与端点 $x(0), x(1)$ 共同取极值，即可在 $O(1)$ 时间内以纳秒级速度算出绝对精确的字形像素包围盒！
---

## G.11 贝塞尔剪裁算法（Bézier Clipping）与高速几何求交

在字体光栅化渲染、轮廓布尔运算（Boolean Union/Difference）以及轮廓重叠消除（Remove Overlap）中，两段三次贝塞尔曲线 $\mathbf{P}(t)$ 与 $\mathbf{Q}(u)$ 的空间求交点是计算几何中最昂贵的操作之一。

传统牛顿迭代法由于高度依赖初始猜测值，在面对多交点或切触点时极易发散。由西德伯格（Sederberg）与西村（Nishita）提出的 **贝塞尔剪裁算法（Bézier Clipping）**，以几何凸包收缩代替纯代数迭代，实现了超级稳定的超二次收敛速度：

### 算法几何步骤：
1. **建立局部坐标系**：连接曲线 $\mathbf{P}$ 的起点 $\mathbf{P}_0$ 与终点 $\mathbf{P}_3$ 构筑基准弦线 $L$，计算每个控制点距直线 $L$ 的正负带符号垂直距离 $d_0, d_1, d_2, d_3$；
2. **构建一维隐式距离函数**：构造一维距离函数 $d(t) = \sum_{i=0}^3 B_{i,3}(t) d_i$，其与横轴的交点即为曲线 $\mathbf{P}$ 与直线 $L$ 的交点；
3. **凸多边形剪裁**：在参数平面 $(u, d)$ 上，绘制第二条曲线 $\mathbf{Q}(u)$ 关于距离轴的凸包，计算该凸包与 $d=0$ 轴相交的最小与最大参数区间 $[u_{\min}, u_{\max}]$；
4. **区间修剪**：将参数区间 $[0, 1]$ 瞬间裁剪缩小至 $[u_{\min}, u_{\max}]$。通过德卡斯特里奥算法截取子曲线，交替对两曲线重复执行，通常仅需 3 至 4 轮迭代，交点参数即可收敛至浮点机极限精度（$10^{-12}$）！

---

## G.12 极式（Blossom）多线性公理的严密代数构造

为了彻底理解极式 $p(u_1, u_2, \dots, u_n)$ 的数学本质，我们给出从单变量单项式基底向多线性对称极式转化的代数构造律：

对于任意单项式 $t^k$（其中 $0 \le k \le n$），其对应的 $n$ 元极式为基本对称多项式除以组合数：

$$\mathcal{B}[t^k] \, (u_1, u_2, \dots, u_n) = \frac{1}{\binom{n}{k}} \sum_{1 \le j_1 < j_2 < \dots < j_k \le n} u_{j_1} u_{j_2} \dots u_{j_k}$$

### 三次多项式极式展开全貌：
对于三次曲线 $\mathbf{P}(t) = \mathbf{a}_0 + \mathbf{a}_1 t + \mathbf{a}_2 t^2 + \mathbf{a}_3 t^3$，其关于三个独立变量 $u_1, u_2, u_3$ 的唯一极式为：

$$p(u_1, u_2, u_3) = \mathbf{a}_0 + \frac{\mathbf{a}_1}{3}(u_1 + u_2 + u_3) + \frac{\mathbf{a}_2}{3}(u_1 u_2 + u_2 u_3 + u_3 u_1) + \mathbf{a}_3 u_1 u_2 u_3$$

#### 代数检验：
1. **对称性**：显然，交换 $u_1, u_2, u_3$ 中任意两者的次序，上式各项完全对称不变；
2. **多重仿射性**：固定 $u_2, u_3$ 时，关于 $u_1$ 是形如 $A u_1 + B$ 的严格一次多项式；
3. **对角坍缩**：令 $u_1 = u_2 = u_3 = t$，有：
   $$p(t, t, t) = \mathbf{a}_0 + \frac{\mathbf{a}_1}{3}(3t) + \frac{\mathbf{a}_2}{3}(3t^2) + \mathbf{a}_3 t^3 = \mathbf{a}_0 + \mathbf{a}_1 t + \mathbf{a}_2 t^2 + \mathbf{a}_3 t^3 = \mathbf{P}(t)$$

极式理论的创立，不仅为计算机字体几何学提供了最坚固的代数奠基石，更将曲线微积分完全转化为优雅的多项式组合对称学，成为了全人类计算机图形学与几何设计皇冠上最璀璨的明珠。
---

## G.13 欧拉角螺线在现代排印工程学中的终极统一

在现代字型设计工具（如 FontForge 的 Spiro 模式与 Glyphs 的曲线平滑插件）中，欧拉螺线（Cornu Spiral）的工程实现基于拉夫·莱维恩的有限元求解器：
* 字体设计师只需在字母转角处放置若干个离散锚点并指定端点切线；
* Spiro 引擎自动求解变分泛函最小化问题（Minimum Energy Curve）：
  $$E = \int \left( \frac{d\kappa}{ds} \right)^2 ds \longrightarrow \min$$
* 求解出的平滑螺线保证了全曲线的曲率导数能量极小化，再通过自适应德卡斯特里奥细分，自动导出符合 OpenType 规范的标准三次贝塞尔曲线，彻底消除了手工反复调节控制点所带来的微小视觉瑕疵！
