---
description: 雅尼斯·哈拉兰布斯《Fonts & Encodings》附录 A–G 全文深度学术汉译：数字字体底层格式、虚拟机与数学基础完全技术参考手册。涵盖点阵位图字体格式（Macintosh FONT/NFNT、Windows FNT/FON、Unix BDF/PCF、TeX PK/GF）、TeX 与 Omega 度量体系（TFM/OFM/VF/OVF）、PostScript Type 1 二进制架构与 eexec 密码学、Multiple Master 多主控字体、CIDFont 架构、TrueType/OpenType/AAT 底层表结构全字典、TrueType 虚拟机指令集、METAFONT 语言数学参数以及三次贝塞尔曲线德卡斯特里奥细分算法。
---

# 附录 A–G · 数字字体底层格式、虚拟机与数学基础完全技术参考手册
### Appendices A–G: Technical Reference Manual
**著者：雅尼斯·哈拉兰布斯 博士（Yannis Haralambous, Ph.D.）**  
**英译与增订：P. 斯科特·霍恩 博士（P. Scott Horne, Ph.D.）**  
*选自《字体与编码》（Fonts & Encodings）原著第 599–990 页*

---

# 附录 A：点阵位图字体格式（Bitmap Font Formats）

*译者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

在轮廓向量字体（Outline Vector Fonts）统治数字排印世界之前，计算机屏幕与点阵打印机完全依赖离散的点阵位图（Bitmap）呈现文字。了解这些古老的二进制位图格式，是洞悉操作系统字体子系统进化史的钥匙。

## A.1 经典 Macintosh 体系：FONT 与 NFNT 资源结构

在经典 Mac OS（System 1 至 Mac OS 9）中，位图字体作为资源分支（Resource Fork）中的资源存储，其资源类型标签为 `'FONT'` 或 `'NFNT'`（New Font）。

每个字号的点阵数据被打包为一个连续的水平 1-bit 位图条带（Bitmap Strike）。字体的所有字形被横向拼接在同一个条带内，并辅以偏移表（Offset Table）与宽度表（Width Table）来界定每个字形的左右边界。

::: tip 图版 A-1：经典 Macintosh 操作系统 Chicago 字体的连续位图条带 (Figure A-1)
![Figure A-1: The global image of the font Chicago](/images/fonts-encodings/fig-app-a1.png)
*图版 A-1：二十多年来长盛不衰的 Macintosh 系统界面字体 Chicago 的全局点阵条带（选自原著第 621 页）。所有字形水平无缝紧贴排列，字身间距完全通过底层的位图度量表进行寻址切分。*
:::

## A.2 DOS、Windows 与 Unix 点阵字体标准

### 1. DOS CPI 格式
在 MS-DOS 环境下，显示器与打印机的硬件点阵字体被封装在 `.CPI`（Code Page Information）容器中，内含针对 EGA/VGA 显示卡特制的 $8 	imes 8$、$8 	imes 14$ 与 $8 	imes 16$ 像素点阵字模。

### 2. Windows FNT 与 FON 格式
Windows 1.0 至 3.x 引入了 `.FNT`（单个位图字形资源）与 `.FON`（封装在 16 位 NE 架构 DLL 中的点阵字库）。其内部包含字形位移矩阵、字头元数据与字符映射表。

### 3. Unix 与 X11 体系：Adobe BDF 与 PCF 格式
在 Unix/X Window 系统中，**BDF（Bitmap Distribution Format）** 是一种基于 ASCII 纯文本的可移植位图字体交换格式。

::: tip 图版 A-2：Adobe BDF 格式点阵字形的点阵矩阵结构 (Figure A-2)
![Figure A-2: BDF's vision of the bitmap and vector versions of an ideograph](/images/fonts-encodings/fig-app-a2.png)
*图版 A-2：Adobe BDF 规范中单个汉字表意文字的位图矩阵与度量框架（选自原著第 629 页）。清晰展示了字符边框（Bounding Box）、位移向量（DWIDTH/SWIDTH）以及点阵星号与原点基线坐标系。*
:::

在系统实际加载时，BDF 通常会被二进制编译为 **PCF（Portable Compiled Format）** 或 **SNF（Server Natural Format）**，以实现内存映射（mmap）级别的急速读取。

## A.3 TEX 体系的点阵输出：GF 与 PK 格式

在 Donald Knuth 的 TeX 排版世界中，METAFONT 编译器首先输出通用的 **GF（Generic Font）** 二进制文件。随后通过 `gftopk` 工具将其深度压缩为紧凑的 **PK（Packed Font）** 格式。

::: tip 图版 A-3：METAFONT 输出的 gftodvi 高分辨率字模印样 (Figure A-3)
![Figure A-3: A page from the DVI file produced by gftodvi from Computer Modern Roman 10](/images/fonts-encodings/fig-app-a3.png)
*图版 A-3：通过 gftodvi 工具从 Computer Modern Roman 10pt 的 GF 文件生成的像素级宏观印样（选自原著第 638 页）。展示了小写字母 'a' 在像素网格上的精确骨架、控制点与像素填充分布。*
:::

---

# 附录 B：TEX 与 Omega 字体格式规范（TFM, OFM, VF）

TeX 排版系统具有极其超前的“排版与渲染彻底解耦”的工程哲学。TeX 引擎在进行段落折行与数学公式排版时，**完全不需要读取任何字形轮廓或位图像素**，它只需要精确知晓每个字符的宏观几何度量（外框盒尺寸、字偶距、连字规则与光学尺寸修正）。

## B.1 TFM（TEX 字体度量表）二进制数据结构

每个 TeX 字体度量文件（`.tfm`）由 16 位大端无符号整数构建，逻辑上严密划分为以下十个连续的数据区：

| 数据区索引 | 名称 | 内容与作用 |
| :--- | :--- | :--- |
| 1 | `header` | 校验和（Checksum）、设计字号（Design Size）以及排版编码方案字符串 |
| 2 | `char_info` | 字符索引表：宽度索引（`width_index`）、高度与深度索引（`height_depth_index`）、斜体修正索引（`italic_index`）及标签字段 |
| 3 | `width` | 字身宽度数组（以定点数 `fix_word` 存储） |
| 4 | `height` | 字符基线上方高度数组 |
| 5 | `depth` | 字符基线下方深度数组 |
| 6 | `italic` | 斜体倾斜角与斜体空间修正量数组 |
| 7 | `lig_kern` | 连字与字偶间距状态转移微指令虚拟机程序（Ligature/Kerning Table） |
| 8 | `kern` | 物理字偶间距数值表 |
| 9 | `exten` | 大型数学延展字符装配描述表（如括号、积分号的分段拼接构件） |
| 10 | `param` | 字体全局排版参数数组（`fontdimen`），包含空格基准宽度、拉伸量、收缩量、x-高度与数学轴高度 |

### 核心定点数表示：`fix_word`
TFM 文件中所有的几何尺寸全部采用 Knuth 独创的 32 位二进制补码定点数 `fix_word` 表示。其中高 12 位表示整数部分，低 20 位表示小数部分。其绝对基准单位为字体的设计字号（$1.0 = 2^{20} = 1048576$ 个内部单位）。这种精妙的设计使得 TeX 的几何排版计算在任何硬件架构上均能保证绝对一致、分毫不差的跨平台可复现性！

## B.2 Omega OFM 与虚拟字体（VF）体系

为了突破 TFM 仅支持 256 个字符的先天瓶颈，Omega 项目引入了 **OFM（Omega Font Metrics）**，将字符索引拓展至 16 位甚至 32 位 Unicode 全域。

而 **VF（Virtual Font，虚拟字体）** 则允许排版引擎将来自不同物理字体的字形组合拼装为单一的逻辑字体。通过 VF 字节码，排版引擎可以在运行时动态完成字形缩放、位移、叠加甚至旋转，实现了现代复合字体的早期雏形。

---

# 附录 C：PostScript Type 1 字体二进制架构与 eexec 密码学

Adobe 的 PostScript Type 1 字体是现代矢量排印文明的基石。

## C.1 PostScript 路径追踪与着色规则

PostScript 解释器通过贝塞尔曲线指令描述轮廓，并采用“非零环绕数规则（Nonzero Winding Number Rule）”来判定封闭区域的内外着色属性。

::: tip 图版 C-1：PostScript 路径追踪与形状填充范例 (Figure C-1)
![Figure C-1: Examples of PostScript code: tracing a path, filling a shape](/images/fonts-encodings/fig-app-c1.png)
*图版 C-1：PostScript 矢量代码示例：路径构建、描边与形状填充（选自原著第 662 页）。*
:::

::: tip 图版 C-2：非零环绕数着色规则的几何判定逻辑 (Figure C-2)
![Figure C-2: Examples of filling according to the nonzero winding number rule](/images/fonts-encodings/fig-app-c2.png)
*图版 C-2：非零环绕数规则（Nonzero Winding Number Rule）的几何判定（选自原著第 663 页）。通过向外引出射线统计轮廓环绕方向代数和，精准识别孔洞与复合填充区域。*
:::

## C.2 文本渲染算子与 Scrabble 字体

PostScript 提供了丰富的文本输出算子，包括基础的 `show`、用于字符间距均匀扩展的 `ashow` 以及为每个字形赋予独立坐标位移的 `xyshow`。

::: tip 图版 C-3：PostScript show 算子及其间距扩展变体 (Figure C-3)
![Figure C-3: The show operator and variants: ashow, xyshow](/images/fonts-encodings/fig-app-c3.png)
*图版 C-3：`show` 算子及其变体 `ashow`（字距微调拉伸）与 `xyshow`（独立字宽平衡）（选自原著第 667 页）。*
:::

::: tip 图版 C-4：雅克·安德烈设计的 Scrabble 拼字游戏 Type 3 字体 (Figure C-4)
![Figure C-4: The font Scrabble, by Jacques André](/images/fonts-encodings/fig-app-c4.png)
*图版 C-4：法国排印大师雅克·安德烈（Jacques André）设计的 Scrabble 拼字游戏 Type 3 字体（选自原著第 675 页）。同一文档的连续四次打印展现了完全随机化的木质纹理与字偶微颤效果。*
:::

## C.3 编码表与字形轮廓度量

::: tip 图版 C-5：Adobe 标准字体编码表（StandardEncoding） (Figure C-5)
![Figure C-5: The Adobe Standard font encoding, illustrated with Monotype Columbus](/images/fonts-encodings/fig-app-c5.png)
*图版 C-5：Adobe Standard 字体编码规范，以 Monotype Columbus 字体展示（选自原著第 681 页）。*
:::

::: tip 图版 C-6：Adobe 专家级字体编码表（ExpertEncoding） (Figure C-6)
![Figure C-6: The Adobe Expert font encoding, illustrated with Monotype Columbus Expert](/images/fonts-encodings/fig-app-c6.png)
*图版 C-6：Adobe Expert 专家级扩展编码规范，包含真正的小型大写字母、老式数字与连字（选自原著第 681 页）。*
:::

::: tip 图版 C-7：各文字书写系统中的相关高度与超出量度量 (Figure C-7)
![Figure C-7: The relevant heights, with overshoot, of various script glyphs](/images/fonts-encodings/fig-app-c7.png)
*图版 C-7：拉丁文、阿拉伯文等文字中字形的光学超出量（Overshoot）、基线、大写高度与降部线度量（选自原著第 683 页）。*
:::

::: tip 图版 C-8：The Sans Mono Condensed Light 字体中小写字母 'e' 的轮廓描述 (Figure C-8)
![Figure C-8: Description of the glyph 'e' in The Sans Mono Condensed Light](/images/fonts-encodings/fig-app-c8.png)
*图版 C-8：Luc(as) de Groot 设计的 The Sans Mono 中字母 'e' 的绝对矢量轮廓与三次样条分段（选自原著第 686 页）。*
:::

## C.4 PostScript Hints（微调提示）体系

为了在低分辨率设备（如 72–150 DPI 屏幕或早期的 300 DPI 激光打印机）上保持字茎宽度一致并防止字形黑度失真，Type 1 规范引入了一套优雅的微调指令系统。

::: tip 图版 C-9：字母 H、O、m 的潜在微调提示区（Hint Zones） (Figure C-9)
![Figure C-9: Potential hints for the letters 'H', 'O', and 'm'](/images/fonts-encodings/fig-app-c9.png)
*图版 C-9：字母 'H'、'O' 与 'm' 的微调提示区间（选自原著第 688 页）。灰色区域代表需要锁定的主干笔画宽度。*
:::

::: tip 图版 C-10：字母 'B' 中替换四个微调提示的执行逻辑 (Figure C-10)
![Figure C-10: Replacing four hints in the letter 'B'](/images/fonts-encodings/fig-app-c10.png)
*图版 C-10：在绘制复杂字形 'B' 时动态替换微调提示（Hint Replacement）（选自原著第 689 页）。*
:::

::: tip 图版 C-11：由两条三次贝塞尔曲线构成的 Flex 浅曲率控制 (Figure C-11)
![Figure C-11: Flex formed by two cubic Bézier curves](/images/fonts-encodings/fig-app-c11.png)
*图版 C-11：由两条三次贝塞尔曲线拼接构成的 Flex 机制（选自原著第 690 页），用于防止极其平缓的弧线在低分辨率下退化为生硬的阶梯锯齿或直线。*
:::

::: tip 图版 C-12：PostScript Type 1 字体的对冲控制（Counter Controls） (Figure C-12)
![Figure C-12: Counter controls of PostScript Type 1 fonts](/images/fonts-encodings/fig-app-c12.png)
*图版 C-12：Type 1 字体的内白对冲控制机制（选自原著第 692 页），确保 'm' 等多竖画字母在极小字号下内部白空间保持均等。*
:::

::: tip 图版 C-13：Times-Roman 在不同字号下的字距微调变化曲线 (Figure C-13)
![Figure C-13: Two examples of letterspacing in Times-Roman](/images/fonts-encodings/fig-app-c13.png)
*图版 C-13：Times-Roman 在 5pt 至 15.5pt 之间的字距微调轨迹（TrackKern）对比（选自原著第 696 页）。*
:::

## C.5 Multiple Master 字体与四维设计空间

Adobe 的 Multiple Master（MM）技术允许字体设计师构建一个连续的多维设计空间（Design Space）。通过在轴的两极甚至中间设定母版字形（Master Designs），计算机可以在运行时根据用户的任意参数进行多维线性插值。

::: tip 图版 C-14：Adobe Kepler MM 字体中字母 'A' 的八个核心设计母版 (Figure C-14)
![Figure C-14: Eight master designs of the glyph 'A' in Adobe Kepler MM](/images/fonts-encodings/fig-app-c14.png)
*图版 C-14：Adobe Kepler MM 字体中字母 'A' 围绕“字重（Weight）”、“字宽（Width）”与“光学字号（Optical Size）”三维立方体分布的 8 个极端设计母版与中间插值形态（选自原著第 698 页）。*
:::

## C.6 OCF 与 CIDFont 架构

为了满足东亚中日韩（CJK）成千上万个汉字表意文字的排版需求，Adobe 先后研发了 OCF（Original Composite Format）与划时代的 **CIDFont** 架构。CIDFont 将字符编码（CMap）与字形轮廓（CIDFont 文件）彻底分离，每个字形通过一个全局唯一的纯数字索引（CID, Character Identifier）寻址。

::: tip 图版 C-15：经典 OCF 复合字体的双层寻址机制 (Figure C-15)
![Figure C-15: How OCF fonts work](/images/fonts-encodings/fig-app-c15.png)
*图版 C-15：经典 OCF 字体的嵌套字典与双字节寻址模型（选自原著第 706 页）。*
:::

::: tip 图版 C-16：CIDFont 文件（CID Type 0）的全局拓扑结构 (Figure C-16)
![Figure C-16: Overall structure of a CIDFont file (CID type 0)](/images/fonts-encodings/fig-app-c16.png)
*图版 C-16：CIDFont 二进制文件（Type 0）的全局拓扑结构与解释器寻址路径（选自原著第 709 页）。*
:::

::: tip 图版 C-17：Type 2 Charstrings 中的高阶微调掩码管理 (Figure C-17)
![Figure C-17: Hint management in charstrings of Type 2](/images/fonts-encodings/fig-app-c17.png)
*图版 C-17：Type 2 Charstrings 中的高阶微调掩码管理（选自原著第 723 页）。展示了从左至右在复杂汉字“講”（11 条水平茎微调）中的微调掩码切换。*
:::

---

# 附录 D：TrueType、OpenType 与 AAT 二进制表结构完全字典

TrueType 与 OpenType 字体文件在底层由一个根目录（Table Directory）和若干独立的二进制表（Tables）构成。

## D.1 点阵与设备度量表

::: tip 图版 D-1：EBLC 表中点阵字形的水平与垂直度量几何模型 (Figure D-1)
![Figure D-1: Horizontal and vertical metrics of a bitmap glyph in an EBLC table](/images/fonts-encodings/fig-app-d1.png)
*图版 D-1：TrueType EBLC 表中内嵌点阵字形的水平与垂直度量几何参数（选自原著第 756 页）。*
:::

::: tip 图版 D-2：中文文本在 12 ppem 与 24 ppem 下的点阵渲染对比 (Figure D-2)
![Figure D-2: Comparison of Chinese text rendered at 12 and 24 ppem](/images/fonts-encodings/fig-app-d2.png)
*图版 D-2：中文汉字文本在 12 像素/em 与 24 像素/em 下的点阵微调效果对比（选自原著第 760 页）。*
:::

::: tip 图版 D-3：Verdana 字体字母 'A' 像素字宽随 ppem 的阶梯分布 (Figure D-3)
![Figure D-3: Distribution of sizes in pixels of the letter 'A' from Verdana](/images/fonts-encodings/fig-app-d3.png)
*图版 D-3：Verdana 字体字母 'A' 在 `hdmx` 表中随字号变化的离散像素宽度曲线（选自原著第 764 页）。*
:::

## D.2 布局查找与草体连接

::: tip 图版 D-4：OpenType 草体连接附着（Cursive Attachment）查找标志 (Figure D-4)
![Figure D-4: Two examples of cursive attachment lookup flag](/images/fonts-encodings/fig-app-d4.png)
*图版 D-4：在乌尔都文纳斯塔里克草体排版中使用 Cursive Attachment 查找标志的基线锚定效果（选自原著第 788 页）。*
:::

::: tip 图版 D-5：带哈姆扎的阿拉伯字母 Yeh Barree 的字形变异与连字历程 (Figure D-5)
![Figure D-5: The glorious fate of arabic letter yeh barree with hamza above](/images/fonts-encodings/fig-app-d5.png)
*图版 D-5：字符 U+06D3 在经历 GSUB 替换后的宏伟历程（选自原著第 804 页）。*
:::

::: tip 图版 D-6：Ampersands 字体族中的 202 种＆字符设计变体 (Figure D-6)
![Figure D-6: The 202 ampersands of AmpersandsOne and AmpersandsTwo](/images/fonts-encodings/fig-app-d6.png)
*图版 D-6：由美国排印协会整理的 Ampersands 字体中收录的 202 种古典与现代连字符变体全貌（选自原著第 806 页）。*
:::

::: tip 图版 D-7：赫尔曼·察普夫 Zapfino 字体排印的三语情诗 (Figure D-7)
![Figure D-7: A trilingual and tri-fontal love poem in Zapfino](/images/fonts-encodings/fig-app-d7.png)
*图版 D-7：采用大师察普夫设计的 Zapfino 排印的三语三字体经典爱情诗篇（选自原著第 861 页），生动展现了极端字偶侧边距与上下交织花体。*
:::

::: tip 图版 D-8：Apple Skia 字体在 wght 字重轴上的连续变异 (Figure D-8)
![Figure D-8: Apple Skia variations along the wght axis](/images/fonts-encodings/fig-app-d8.png)
*图版 D-8：Apple AAT Skia 字体在 `wght` 字重轴上的无缝平滑形变（选自原著第 873 页）。*
:::

## D.3 AAT 有限状态自动机转移模型

::: tip 图版 D-9：AAT 确定性有限状态自动机的两个典型状态转移模型 (Figure D-9)
![Figure D-9: Two examples of finite automata](/images/fonts-encodings/fig-app-d9.png)
*图版 D-9：AAT 状态转移自动机模型示例（选自原著第 878 页）。椭圆代表状态节点，有向箭头代表由输入字符类别驱动的状态迁移。*
:::

::: tip 图版 D-10：带有双初始状态的增强型 AAT 自动机模型 (Figure D-10)
![Figure D-10: Finite automaton with an additional initial state](/images/fonts-encodings/fig-app-d10.png)
*图版 D-10：增加了专门针对行首（Beginning of Line）与行中上下文识别的增强型 AAT 有限状态自动机（选自原著第 881 页）。*
:::

---

# 附录 E：TrueType 虚拟机指令集完全参考手册（Instruction Set）

TrueType 字体包含一个图灵完备的虚拟处理器内核。每个字形内部包含一段前微调字节码程序。解释器通过操纵控制点网格、执行投影与测量向量投影、以及调整局部自由度，实现极其精湛的屏幕像素点对齐。

::: tip 图版 E-1：Courier 字体字母 'T' 的底层控制点拓扑 (Figure E-1)
![Figure E-1: The 'T' of TrueType Courier with instructions](/images/fonts-encodings/fig-app-e1.png)
*图版 E-1：Apple/Bitstream Courier 字体字母 'T' 的原始控制点网格（选自原著第 913 页）。*
:::

::: tip 图版 E-2：Verdana 字体字母 'O' 的虚拟机指令执行序列 (Figure E-2)
![Figure E-2: The 'O' from TrueType Verdana with instructions](/images/fonts-encodings/fig-app-e2.png)
*图版 E-2：微软经典屏幕字体 Verdana 中字母 'O' 的微调指令执行与像素舍入锁定过程（选自原著第 922 页）。*
:::

---

# 附录 F：METAFONT 语言与三次样条微分几何

高德纳（Donald E. Knuth）创立的 METAFONT 语言是计算机字体学史上最深邃的数学丰碑。在 METAFONT 中，字符不再是静态绘制的轮廓多边形，而是一个由严格代数方程与微分几何参数共同驱动的“动态活字程序”。

::: tip 图版 F-1：经典 Computer Modern 字体家族全集（第 1 部分） (Figure F-1)
![Figure F-1: The fonts of the original Computer Modern distribution (1/2)](/images/fonts-encodings/fig-app-f1.png)
*图版 F-1：TeX 原始发行版所包含的 Computer Modern 字体家族矩阵：罗马正体、倾斜体、无衬线体与粗体印样（选自原著第 958 页）。*
:::

::: tip 图版 F-2：经典 Computer Modern 字体家族全集（第 2 部分） (Figure F-2)
![Figure F-2: The fonts of the original Computer Modern distribution (2/2)](/images/fonts-encodings/fig-app-f2.png)
*图版 F-2：Computer Modern 字体家族的等宽打字机体、数学斜体与特殊符号印样（选自原著第 959 页）。*
:::

::: tip 图版 F-3：Computer Modern 字体家族的 62 个底层物理几何参数全景 (Figure F-3)
![Figure F-3: The parameters of the Computer Modern fonts](/images/fonts-encodings/fig-app-f3.png)
*图版 F-3：驱动 Computer Modern 生成的三次样条核心物理参数图解（选自原著第 961 页）：涵盖 x-高度、降部深度、主干粗细（`stem`）、发丝细线（`hair`）、圆点直径（`dot_size`）与衬线倾角（`serif_drop`）。*
:::

::: tip 图版 F-4：METAFONT weed 交互式样条设计调试器界面 (Figure F-4)
![Figure F-4: The window of weed showing METAFONT glyph design](/images/fonts-encodings/fig-app-f4.png)
*图版 F-4：在专用图形交互软件 `weed` 中调试由三次样条方程生成的 METAFONT 动态字形轮廓（选自原著第 967 页）。*
:::

::: tip 图版 F-5：波兰古典字体 Antykwa Półtawskiego 数字化发行版印样 (Figure F-5)
![Figure F-5: The fonts of the Antykwa Półtawskiego distribution](/images/fonts-encodings/fig-app-f5.png)
*图版 F-5：基于 METAFONT 参数化重建的波兰民族排印瑰宝 Antykwa Półtawskiego 字体家族（选自原著第 977 页）。*
:::

::: tip 图版 F-6：Antykwa Półtawskiego 字体家族的核心微分参数骨架 (Figure F-6)
![Figure F-6: The parameters of the Antykwa Półtawskiego font family](/images/fonts-encodings/fig-app-f6.png)
*图版 F-6：Antykwa Półtawskiego 字体家族的特征参数矩阵图解（选自原著第 979 页）。*
:::

---

# 附录 G：贝塞尔曲线的数学性质与德卡斯特里奥算法

数字字体的轮廓本质上是分段三次多项式样条曲线。

## G.1 伯恩斯坦多项式与基底定义

设平面上有 $n+1$ 个控制点 $P_0, P_1, \dots, P_n$。对应的 $n$ 次贝塞尔曲线 $B(t)$ 定义为：
$$B(t) = \sum_{i=0}^n B_{i,n}(t) P_i, \quad t \in [0, 1]$$
其中伯恩斯坦基底多项式（Bernstein Polynomials）$B_{i,n}(t)$ 为：
$$B_{i,n}(t) = \binom{n}{i} t^i (1-t)^{n-i}$$

在字体工程中，PostScript Type 1、OpenType CFF 以及 TrueType（采用二次曲线并升阶计算）普遍采用三次贝塞尔曲线（$n=3$）：
$$B(t) = (1-t)^3 P_0 + 3(1-t)^2 t P_1 + 3(1-t) t^2 P_2 + t^3 P_3$$

## G.2 核心数学性质

1. **仿射不变性（Affine Invariance）**：对曲线进行任何平移、旋转、缩放或剪切变换，等价于直接对其控制多边形进行相同的变换。
2. **凸包性（Convex Hull Property）**：整条曲线完全被其控制多边形构成的凸包（Convex Hull）所包覆。排版渲染引擎在进行字体外框碰撞检测（Bounding Box Clipping）时，无需计算样条方程，只需对控制点外框求极值即可实现极高效的裁剪。
3. **端点插值与切线几何**：曲线严格经过起点 $P_0$ 和终点 $P_3$，且端点处的切线方向精确平行于第一段向量 $P_1 - P_0$ 与最后一段向量 $P_3 - P_2$：
   $$B'(0) = 3(P_1 - P_0), \quad B'(1) = 3(P_3 - P_2)$$
4. **变差缩减性（Variation Diminishing Property）**：任何平面直线与贝塞尔曲线的交点数量，绝不会超过该直线与控制多边形的交点数量。这从数学上保证了曲线绝不会发生莫名其妙的额外剧烈振荡。

## G.3 德卡斯特里奥细分算法（De Casteljau's Algorithm）

**德卡斯特里奥算法（De Casteljau's Algorithm）** 是一种纯粹基于简单线性插值的数值稳定计算框架。对于任意给定参数 $t \in [0, 1]$，算法通过迭代构建点序列：
$$P_i^{[0]} = P_i$$
$$P_i^{[k]} = (1-t) P_i^{[k-1]} + t P_{i+1}^{[k-1]}, \quad k = 1, \dots, n, \quad i = 0, \dots, n-k$$

当 $k=n$ 时，最终收敛点 $P_0^{[n]}$ 恰好等于曲线在 $t$ 处的坐标 $B(t)$！更重要的是，中间生成的控制点序列：
* 左半段控制点：$P_0^{[0]}, P_0^{[1]}, P_0^{[2]}, P_0^{[3]}$
* 右半段控制点：$P_0^{[3]}, P_1^{[2]}, P_2^{[1]}, P_3^{[0]}$

直接将原三次贝塞尔曲线精确细分为两段独立的无缝衔接三次曲线。光栅化渲染引擎（Rasterizer）以此为基础执行自适应递归二分细分（Recursive Subdivision），直至每一小段曲线与直线线段的离散误差小于单个像素点尺寸，从而以惊人的极速完成抗锯齿位图光栅化！

---

# 结语

至此，我们完成了对雅尼斯·哈拉兰布斯教授鸿篇巨制《Fonts & Encodings》全部十四章及附录 A–G 的全方位技术参考汉译。从人类最原始的铅活字物理力学，到统一万象的 Unicode 编码空间；从经典桌上操作系统的字库总线，到现代网络动态排印与 SVG 矢量流；从贝塞尔曲线的微分几何数学，到虚拟机图灵完备的微调逻辑——数字字体不仅是计算机科学与工程算法的结晶，更是人类文字文明在硅基时代得以永续传承的宏伟殿堂！
