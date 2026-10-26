---
title: "第 12 章：字体的设计、编辑与制作技术"
description: "完整无删节 1:1 学术全译：数字字体制作工具演进史（Fontographer、FontStudio、Ikarus、FontLab、FontForge）；矢量轮廓数学机理（PostScript 三次贝塞尔与 TrueType 二次 B-样条、极值点约束、轮廓方向与非零缠绕法则、排印度量网格）；FontLab 工业生产全流程（Names/Pages/Ranges/Index 四大字符视图、Font Info 核心排印度量与 OpenType 元数据、字形绘图与节点拓扑优化、字距调整与 Kerning 类、Multiple Master 多重母版设计空间、原生 Python 脚本自动化编程）；FontForge 开源架构与高级特性（X11 交互环境、垂直排版度量、CID 键控字体与扁平化）；位图自动描摹技术（Potrace 与 ScanFont 参数调优与几何缺陷）。"
---

# 第 12 章：字体的设计、编辑与制作技术

**雅尼斯·哈拉兰博斯（Yannis Haralambous, Ph.D.）著**  
*选自《Fonts & Encodings》第 441–504 页*

*译者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

现在，我们来到了全书最为核心的圣殿：**创造字体**。

我们是否必须成为像赫尔曼·察普夫（Hermann Zapf）或让·弗朗索瓦·波尔谢兹（Jean François Porchez）那样的旷世设计大师，才能有资格踏入字体创作的领域？绝非如此。正如任何人都可以挥毫写下一封书信、绘出一幅素描一样，今天每一个具备基本审美与技术直觉的人，都可以投身于字体的设计与改良。

在计算机排版技术彻底普及的今天，创造一套高品质的数字矢量字体不再是只有大型铸字工坊与跨国软件巨头才能染指的秘术。随着个人图形工作站与专业字体设计软件（Font Editors）的飞速演进，独立字体设计师、排版学者乃至业余爱好者，都能够直接在屏幕上操纵纯粹的几何矢量轮廓，赋予每一个字符以独特的灵魂与生命力。

然而，字体设计是一门在“极致自由的艺术灵感”与“冰冷严苛的数学和工业标准”之间走钢丝的高难度科学。在字形美感背后，隐藏着一整套涉及贝塞尔微积分、轮廓缠绕拓扑学、整型网格离散化、排印度量度量系统以及复杂的跨平台二进制格式包装逻辑。本章将全面解构现代数字字体创作的核心软件生态与底层几何技术机理。

---

# 字体设计与编辑软件全景

在过去二十余年的数字字体演进史上，至少有六套具有里程碑意义的大型系统塑造了现代字体工业的工作流：

## 1. 拓荒时代的先驱：Fontographer 与 FontStudio

* **Macromedia Fontographer**（最早由 Altsys 公司的吉姆·冯·赫尔（Jim von Ehr）于 1986 年开发）：这是人类历史上首个在 Macintosh 图形界面上实现直接用贝塞尔钢笔工具交互绘制 PostScript Type 1 轮廓的革命性字体编辑器。它让千万排印创作者从晦涩的 PostScript 纯代码坐标中彻底解脱出来。尽管后续历经 Altsys 转让给 Macromedia、再转手给 FontLab 的沧桑历程，其界面更新一度陷入停滞，但其直观的“字体字符网格窗口”与“字形编辑画板”奠定了后世所有字体软件的人机交互范式（图 12-1）。
* **Letraset FontStudio**（运行于经典 Mac OS 9 时代）：由著名的干印即贴字字模巨头 Letraset 打造的高端专业级字体工坊软件。它引入了极其先进的自动微调提示（Auto-hinting）、灰度预览与多图层度量网格系统，在 1990 年代初受到各大专业铸字厂商的极高推崇（图 12-2）。
* **URW Ikarus**：由彼得·卡罗（Peter Karow）领导的德国 URW 公司开发的史诗级工业系统。与面向微机的软件不同，Ikarus 诞生于大型机与专业绘图板时代，率先采用了切线点、角点与圆弧极值点的严密数学描述体系，成为全球顶级字体公司数字化历史铅字档案的核心基石。
* **FontToolbox**：一套在专业排印工程师圈子内广泛流传的底层字体操作工具集。

::: tip 图 12-1：Macromedia Fontographer 在 Mac OS X 下的字体字符总览窗口。每个方格内直观呈现字符图形、Unicode 编码与 PostScript 字形名称
![图 12-1：Macromedia Fontographer 在 Mac OS X 下的字体字符总览窗口](/images/fonts-encodings/fig12-1.png)
*图 12-1：Macromedia Fontographer 在 Mac OS X 下的字体字符总览窗口。每个方格内直观呈现字符图形、Unicode 编码与 PostScript 字形名称。*
:::

::: tip 图 12-2：Letraset FontStudio 在经典 Mac OS 9 系统下的单字符字形编辑工作窗口。展示了早期专业字体设计所依赖的参考基准辅助线与贝塞尔节点调控界面
![图 12-2：Letraset FontStudio 在经典 Mac OS 9 系统下的单字符字形编辑工作窗口](/images/fonts-encodings/fig12-2.png)
*图 12-2：Letraset FontStudio 在经典 Mac OS 9 系统下的单字符字形编辑工作窗口。展示了早期专业字体设计所依赖的参考基准辅助线与贝塞尔节点调控界面。*
:::

---

## 2. 现代工业标准霸主：FontLab 与开源传奇 FontForge

在当今字体工业中，占据统治地位的两大旗舰软件分别是商业领域的 **FontLab** 与开源社区的 **FontForge**：

* **FontLab Studio**：由苏联裔天才程序员尤里·亚尔莫拉（Yuri Yarmola）与瓦季姆·苏沃洛夫（Vadim Suvorov）联合倾力打造。自 1990 年代初问世以来，它在长达二十余年的时间里无可争辩地统治着全球各大商业字体厂商（如 Adobe、Linotype、Monotype、Bitstream）的工业生产流水线。它具备无懈可击的跨平台兼容性、工业级 OpenType 特性编译器以及强大的原生 Python 脚本扩展接口。
* **FontForge**（原名 **PfaEdit**）：由传奇黑客**乔治·威廉姆斯**（George Williams）倾注毕生心血独立打造的自由开源软件（FOSS）。它不仅完全支持所有已知的矢量与位图字体格式，更内建了完整的 TrueType 虚拟机单步调试器与深邃的数学几何引擎。

---

# 字体工程的底层几何与通用原则

在真正动笔绘制第一个字符之前，每一个设计者都必须牢牢掌握数字字体在底层几何、数学与空间度量上的严苛通用原则：

## 1. 三次贝塞尔曲线与二次 B-样条的本质分野

数字字体主要由两大对立阵营的矢量数学模型所支配：
* **PostScript / OpenType CFF 阵营**：采用**三次贝塞尔曲线**（Cubic Bézier Curves）。每段曲线由 4 个点决定：2 个端点（On-curve nodes）与 2 个离散控制点（Off-curve control points）。数学公式为：
  $$B(t) = (1-t)^3 P_0 + 3(1-t)^2 t P_1 + 3(1-t)t^2 P_2 + t^3 P_3, \quad t \in [0, 1]$$
  三次贝塞尔曲线具备极高的曲率灵活性与自由度，能够用极少的节点描摹出极其流畅的曲线，是传统字体艺术家的最爱。
* **TrueType 阵营**：采用**二次 B-样条曲线**（Quadratic Bézier / B-Splines）。每段曲线仅由 3 个点决定：2 个端点与 1 个控制点：
  $$B(t) = (1-t)^2 P_0 + 2(1-t)t P_1 + t^2 P_2, \quad t \in [0, 1]$$
  当两个连续控制点相邻出现时，TrueType 规范规定在其线段中点处隐式插入一个虚拟的端点。二次曲线的计算速度极快，但由于自由度较低，通常需要比三次曲线多出 30% 到 50% 的控制节点才能达到相同的拟合精度。现代字体编辑器必须能够在这两种曲线空间之间进行无损或极低误差的互相转换。

## 2. 整数设计网格与全身身长（Units per em, UPM）

字体内部的几何坐标并非无限精密的实数，而是映射在一个刚性的整数笛卡尔坐标系中：
* 在 PostScript Type 1 / CFF 字体中，全身身长通常固定为 **1000** 个单位；
* 在 TrueType / OpenType TTF 字体中，为了便于二进制快速移位运算，全身身长通常设定为 2 的幂次方，最经典的标准是 **2048** 个单位。
所有的节点坐标必须被量化取整为整数。取整误差若处理不当，极易导致曲线光滑接点处发生肉眼可见的微小折角。

## 3. 轮廓方向与非零缠绕法则（Non-Zero Winding Rule）

一个字符往往由多个闭合子轮廓（Contours）复合而成（例如圆环 ‘O’ 包含一个外轮廓和一个内轮廓）。光栅化填充引擎如何判断哪个区域是黑色实体、哪个区域是白色镂空？这完全依赖于轮廓的走向与缠绕法则：
* **PostScript 铁律**：**外层轮廓必须遵循逆时针方向（Counter-Clockwise），内层镂空轮廓必须遵循顺时针方向（Clockwise）。**
* **TrueType 铁律**：恰好截然相反！**外层轮廓必须遵循顺时针方向，内层镂空轮廓必须遵循逆时针方向。**
若轮廓方向颠倒，现代文本渲染引擎在执行非零缠绕数（Non-zero winding number）判定时，就会发生字符“反白”或内部孔洞被完全填黑的毁灭性错误！字体编辑器均配备了一键反转轮廓方向（Reverse Contour）与自动纠正缠绕向的工具。

## 4. 极值点约束（Extrema Points）

在贝塞尔曲线的数学切线方向平行于 X 轴或 Y 轴的最外侧顶峰与谷底位置，必须严格放置端点（On-curve Extrema Nodes）。**这是数字字体工业的一条铁律！**
若在曲线的极值点处缺乏端点支撑，PostScript 与 TrueType 的微调提示（Hinting）引擎将无法捕获字符的外边界坐标，导致字号缩小时笔画外突量失控、基线颠簸或发生严重的光栅化截断。

## 5. 排印度量：步进宽度与侧边轴承（Side Bearings）

一个字符在水平排版时所占据的空间不仅由其黑体墨迹决定，更由其看不见的虚拟外框决定：
* **字形原点（Origin, (0,0)）**：字符绘制的起始基准点。
* **左侧边距（Left Side Bearing, LSB）**：从原点到字符最左侧几何边缘的水平距离。
* **字符宽度 / 步进宽度（Advance Width / Set-Width）**：字符排印时光标从当前字符原点跳转到下一个字符原点的总距离。
* **右侧边距（Right Side Bearing, RSB）**：从字符最右侧几何边缘到步进宽度终点的水平距离。
$$ \text{Advance Width} = \text{LSB} + \text{Bounding Box Width} + \text{RSB} $$
控制好 LSB 与 RSB，是确保连续文字排版时灰度均匀、间隙和谐的关键所在。

---

# 现代工业标准：FontLab 全景深度实战

FontLab 深度整合了对 Type 1、TrueType、OpenType 以及 Multiple Master 格式的全功能原生支持，其核心工作流构建在高度专业化的“四大字符总览视图模式”之上：

## 1. FontLab 字体总览窗口的四大视图模式

在 FontLab 的主字体管理窗口中，用户可以根据当前工程任务的侧重点，自如切换四种完全不同的字符组织模式：

1. **Names 模式（字形名称模式，图 12-3）**：依据标准 Adobe PostScript 字形命名规范（如 `A`, `acute`, `adieresis`, `hyphen`, `ampersand`）组织排列。这是传统 PostScript 字体工程师最习惯的视角，直观反映字形在排版引擎内部的符号命名树。
2. **Pages 模式（编码代码页模式，图 12-4）**：以经典的 256 字符单字节编码页（Code Page，如 Windows-1252 Latin 1、MacRoman、IBM CP437、ISO 8859 系列）为基准划分。每个代码页被切分为整齐的 16×16 矩阵表格，极大地方便了设计者为特定旧式操作系统或区域市场快速排查字符缺漏。每个编码页在后台直接映射至一个扩展名为 `.cpg` 的配置文件。
3. **Ranges 模式（Unicode 字符块模式，图 12-5）**：完全遵循 Unicode 联盟官方划分的标准字符集区间（Unicode Blocks / Ranges，如 Basic Latin、Latin-1 Supplement、Latin Extended-A、Greek and Coptic、Cyrillic 等）。在开发包含数千字符的大型泛欧或全球化通用 OpenType 字体时，该模式是必不可少的工作中枢。
4. **Index 模式（字形索引模式，图 12-6）**：直接以字体二进制文件内部的物理字形索引（Glyph Index, **GID**）为顺序展示。在底层 TrueType/OpenType 结构中，GID 0 永远固定指派给缺失符号（`.notdef`），随后的各字形按其实际编译进字体数据流中的物理先后次序自左向右严格递增排列。

::: tip 图 12-3：FontLab 字体窗口中的 Names（字形名称）视图模式
![图 12-3：FontLab 字体窗口中的 Names（字形名称）视图模式](/images/fonts-encodings/fig12-3.png)
*图 12-3：FontLab 字体窗口中的 Names（字形名称）视图模式。*
:::

::: tip 图 12-4：FontLab 字体窗口中的 Pages（单字节编码代码页）视图模式
![图 12-4：FontLab 字体窗口中的 Pages（单字节编码代码页）视图模式](/images/fonts-encodings/fig12-4.png)
*图 12-4：FontLab 字体窗口中的 Pages（单字节编码代码页）视图模式。*
:::

::: tip 图 12-5：FontLab 字体窗口中的 Ranges（Unicode 标准字符区间块）视图模式
![图 12-5：FontLab 字体窗口中的 Ranges（Unicode 标准字符区间块）视图模式](/images/fonts-encodings/fig12-5.png)
*图 12-5：FontLab 字体窗口中的 Ranges（Unicode 标准字符区间块）视图模式。*
:::

::: tip 图 12-6：FontLab 字体窗口中的 Index（物理字形索引 GID）视图模式
![图 12-6：FontLab 字体窗口中的 Index（物理字形索引 GID）视图模式](/images/fonts-encodings/fig12-6.png)
*图 12-6：FontLab 字体窗口中的 Index（物理字形索引 GID）视图模式。*
:::

---

## 2. 全面的排印度量与元数据架构（Font Info）

设计字体绝不仅仅是画出好看的矢量外形，更是一项极其繁重的技术元数据配置工程。在 FontLab 的“Font Info”（字体信息属性面板，`File > Font Info`）中，涵盖了决定字体跨平台行为的关键标签页：

* **Names and Copyright（名称与版权信息，图 12-7 [a]）**：遵循严格的 OpenType `name` 记录规范（多达 20 余种预定义字符串标识符），包括字体族名称（Family Name）、样式名称（Style Name）、完整字模名称（Full Font Name）、PostScript 内部名称、独一无二的唯一标识符（Unique Font Identifier）、版本号以及设计者商标与法律版权声明。
* **Key Dimensions（核心排印度量尺寸，图 12-8 [a]）**：精确设定字体的全身身长网格（Units per em，通常 PostScript 设定为 1000，TrueType 设定为 2048）、大写字母高度（Cap-Height）、小写 x-高度（X-Height）、字体上行升幅（Ascender）、下行降幅（Descender）以及行距（Line Gap）。
* **Supported Codepages and Unicode Ranges（支持的代码页与 Unicode 范围标志位，图 12-8 [b]、[c]）**：直接对应 TrueType/OpenType 二进制规范中 `OS/2` 表的 128 位 `ulUnicodeRange` 掩码与 64 位 `ulCodePageRange` 掩码。这些比特位明确通知操作系统与文字渲染管线：本字体经过认证能够完整支持哪些语言与国家标准！
* **TrueType 特定高级度量表**：包括预计算字形水平物理像素宽度的 `hdmx` 表、垂直度量对齐控制的 `VDMX` 表，以及决定在特定低分辨率下是否开启平滑抗锯齿的 `gasp` 表。

::: tip 图 12-7：FontLab 字体属性面板：字体命名规范、版权信息及 OpenType 扩展名称配置标签页：(a) 核心名称与版权；(b) 附加 OpenType 名称字段；(c) 法律说明与版权详录
![图 12-7：FontLab 字体属性面板：字体命名规范、版权信息及 OpenType 扩展名称配置标签页](/images/fonts-encodings/fig12-7.png)
*图 12-7：FontLab 字体属性面板：字体命名规范、版权信息及 OpenType 扩展名称配置标签页：(a) 核心名称与版权；(b) 附加 OpenType 名称字段；(c) 法律说明与版权详录。*
:::

::: tip 图 12-8：FontLab 字体属性面板：核心排印度量尺寸（Key dimensions）、支持代码页与 Unicode 覆盖区间配置标签页：(a) 全身尺寸与基准高度；(b) 支持的代码页与默认字符集；(c) 支持的 Unicode 区间掩码
![图 12-8：FontLab 字体属性面板：核心排印度量尺寸（Key dimensions）、支持代码页与 Unicode 覆盖区间配置标签页](/images/fonts-encodings/fig12-8.png)
*图 12-8：FontLab 字体属性面板：核心排印度量尺寸（Key dimensions）、支持代码页与 Unicode 覆盖区间配置标签页：(a) 全身尺寸与基准高度；(b) 支持的代码页与默认字符集；(c) 支持的 Unicode 区间掩码。*
:::

---

## 3. 字形绘制、节点拓扑与度量微调视窗

在 FontLab 的字形绘制编辑视窗中（图 12-9），设计师拥有极高精度的钢笔工具与变换操纵杆：
* **节点类型系统**：FontLab 将节点分为角节点（Corner nodes，两侧控制杆独立运动）、光滑切线节点（Smooth nodes，两侧控制杆保持共线反向联动）以及对称节点（Symmetric nodes）。
* **背景临摹层（Template Layer）**：可将高分辨率手绘扫描线稿或历史字模位图直接导入背景层，通过半透明高亮辅助矢量勾勒。
* **轮廓极值自动对齐与曲线平滑优化**：具备一键清理冗余多余控制节点（Optimize Curve）功能，在保持极高视觉保真度的同时将文件体积压缩至极致。

在字距度量视窗中（Metrics Window，图 12-10）：
* 支持任意字符串文本的即时排印流预览；
* 设计师可直接用光标拖拽字符两侧的侧边轴承虚线，实时微调 LSB 与 RSB；
* **字距调整对（Kerning Pairs）与基于类的字距（Class-based Kerning）**：对于大写字母组合如 “AV”、“To”、“WA”，常规固定间距会导致字符间出现刺眼的巨大空间缝隙。通过定义特定字符对的负向微调值，可使两字紧密咬合。为了避免 $O(N^2)$ 组合爆炸，FontLab 提供了强大的“字距调整类”功能，将具有相似右侧轮廓的字符归为一组（如 ‘A’, ‘À’, ‘Á’, ‘Â’, ‘Ã’），实现跨字符组的批量联动微调！

::: tip 图 12-9：FontLab 字形绘制编辑视窗。展示了节点状态、控制杆操纵、坐标读数以及背景参考线
![图 12-9：FontLab 字形绘制编辑视窗](/images/fonts-encodings/fig12-9.png)
*图 12-9：FontLab 字形绘制编辑视窗。展示了节点状态、控制杆操纵、坐标读数以及背景参考线。*
:::

::: tip 图 12-10：FontLab 度量与字距调整视窗（Metrics Window）。支持多字符交互混排、侧边距拖拽与 Kerning 字符对实时校正
![图 12-10：FontLab 度量与字距调整视窗](/images/fonts-encodings/fig12-10.png)
*图 12-10：FontLab 度量与字距调整视窗。支持多字符交互混排、侧边距拖拽与 Kerning 字符对实时校正。*
:::

---

## 4. 多重母版字体（Multiple Master Fonts）设计空间

FontLab 深度内建了对 Adobe **Multiple Master**（**MM**）技术的原生建模支持：
* 设计师可以定义多达 4 个连续设计轴（如字重 Weight 轴：从 Light 到 Black；字宽 Width 轴：从 Condensed 到 Expanded；视觉字号 Optical Size 轴：从 6pt Caption 到 72pt Display）；
* 在设计空间的各个极值角落分别绘制一套几何拓扑完全同构的母版字形（Master Glyphs）；
* **拓扑相容性铁律**：所有母版字形必须具备**绝对完全相同数量的闭合轮廓、完全相同数量的控制节点，以及完全相同类型的控制点序列！**
一旦母版拓扑校验通过，系统便能在多维设计空间中进行全自动多项式线性插值，瞬间演算衍生出成百上千种截然不同的衍生字族样式！

---

## 5. 原生 Python 脚本自动化编程

FontLab 工业价值的巅峰之一，在于其内置了完整的 Python 解释器与极其丰富的原生对象模型（FontLab Python API）。排印工程师可以通过编写纯 Python 脚本，完全绕开耗时的人工鼠标点选，批量自动化操纵海量字库。

### 核心对象模型：
* `fl` 全局应用上下文对象：管理当前活动字体 `fl.font`、当前字形索引 `fl.iglyph`、视窗刷新与重绘；
* `Font` 字体对象：包含了全部字形集合、元数据属性与代码页表；
* `Glyph` 字形对象：包含了轮廓（Contours）、节点（Nodes）、组件（Components）与侧边轴承；
* `Node` 节点对象：包含坐标 `Point`、节点类型标志位（`nLINE`, `nCURVE`, `nMOVE`, `nSMOOTH`, `nFIXED` 等）。

### 经典实战脚本范例：

#### 范例 1：批量筛选所有以字母 ‘f’ 开头的字形并统计其总数

```python
import re

total = 0
r1 = re.compile(r'^f')
fl.Unselect()

for gi in range(len(fl.font)):
    glyph_name = fl.font[gi].name
    if r1.match(glyph_name):
        fl.Select(gi)
        total += 1

print(f"Total matching glyphs found: {total}")
fl.UpdateFont()
```

#### 范例 2：通过纯数学脚本向当前字形动态插入几何矩形轮廓

```python
from fontlab import *

# 获取当前活动字形
g = fl[fl.ifont][fl.iglyph]

# 定义矩形四角坐标
r_ll = Point(100, 0)
r_ur = Point(500, 700)

# 动态构筑轮廓闭合环
n1 = Node(nMOVE, r_ll)
n2 = Node(nLINE, Point(r_ur.x, r_ll.y))
n3 = Node(nLINE, r_ur)
n4 = Node(nLINE, Point(r_ll.x, r_ur.y))

# 压入字形并闭合
g.Add(n1)
g.Add(n2)
g.Add(n3)
g.Add(n4)
g.JoinAll()

# 强制重算边界框并刷新字体
g.SetModified(1)
fl.UpdateFont()
```

---

# 开源世界的传奇旗帜：FontForge 架构与实战

由乔治·威廉姆斯独立打造的 **FontForge**，是自由与开源排印世界的镇国之宝。它基于严谨的 X11 视窗架构运行，底层以 C 语言写就，兼具难以置信的跨平台灵活性与深度技术通透性。

::: tip 图 12-11：FontForge 主字体字符表视窗（Font Table Window）。展示了完备的 Unicode 字符方格阵列、字符编码槽位与状态标记
![图 12-11：FontForge 主字体字符表视窗](/images/fonts-encodings/fig12-11.png)
*图 12-11：FontForge 主字体字符表视窗。展示了完备的 Unicode 字符方格阵列、字符编码槽位与状态标记。*
:::

::: tip 图 12-12：FontForge 字形轮廓编辑绘制视窗。展示了三次/二次混合编辑模式、多图层管理、仿射变换工具箱与精密坐标读数
![图 12-12：FontForge 字形轮廓编辑绘制视窗](/images/fonts-encodings/fig12-12.png)
*图 12-12：FontForge 字形轮廓编辑绘制视窗。展示了三次/二次混合编辑模式、多图层管理、仿射变换工具箱与精密坐标读数。*
:::

## 1. FontForge 的独特架构优势

* **主字体映射视窗（Font Table Window，图 12-11）**：支持从 0 到 1,114,111 全部 Unicode 字符空间乃至自定义私有编码页的无级缩放总览。
* **字形多图层编辑视窗（Glyph Window，图 12-12）**：具有清晰的前景图层（Foreground）、背景临摹层（Background）以及专业数学辅助线层（Guide Layer）。支持在三次贝塞尔与二次 B-样条模式之间随时切换。
* **丰富的导出伴生格式**：生成字体时，可一键协同生成伴生的 AFM（Adobe Font Metrics）、PFM（Printer Font Metrics）、以及专供 TeX/LaTeX 系统的 TFM（TeX Font Metric）与 ENC 编码映射表！
* **仿射变换矩阵（Affine Transformation Matrix）**：内置强大的几何数学工具箱，支持通过设置 $2 \times 3$ 仿射矩阵，对字符轮廓进行精确的平移、旋转、缩放、斜切与镜像操作：
  $$ \begin{bmatrix} x' \\ y' \end{bmatrix} = \begin{bmatrix} a & c \\ b & d \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} + \begin{bmatrix} t_x \\ t_y \end{bmatrix} $$

## 2. 垂直排版（Vertical Typesetting）与 CJK 度量支持

在处理中日韩（CJK）以及传统蒙古文等东亚竖排文本时，字符的排印度量从传统的水平基线转向了垂直中央基线。FontForge 对垂直排版提供了全方位原生支持：
* 在度量视窗中直接启用垂直排版模式（Vertical Metrics）；
* 独立测量并配置每个字符的**上侧边距（Top Side Bearing, TSB）**、**垂直步进高度（Vertical Advance Height）**与底侧边距；
* 自动生成并校验 OpenType/TrueType 二进制规范中的垂直头信息表 `vhea` 与垂直度量表 `vmtx`，并深度配合 OpenType `vert`（垂直书写替代）与 `vrt2` 高级布局特性。

## 3. CID 键控字体（CID-keyed Fonts）与扁平化

面对包含数万汉字的超大型东亚字库，传统的单字节或简单 Unicode 扁平映射往往难以承载复杂的异体字体系。FontForge 原生支持 Adobe 的 **CID 架构**（基于字符集合 Registry-Ordering-Supplement 的 CIDFont）：
* 允许设计者将字体组织为多子字族聚合体；
* 提供极其关键的 `CID > Flatten`（扁平化）指令：能够一键“剥离”晦涩复杂的 CID 结构，将其直接解构降级为普通的全局 Unicode 编码字体，极大地方便了将旧式专业东亚字体向现代跨平台 OpenType 格式的平民化迁移！

---

# 位图自动描摹技术（Autotracing）

对于通过纸张手工绘制或历史扫描获得的字形图像，如果每一个字符都需要人工拉贝塞尔曲线重新勾勒，其劳动量对于数万汉字库而言是无法想象的。为此，图形学界诞生了**自动描摹技术**（**Autotracing** / 矢量化）。

然而，哈拉兰博斯博士在此提出了极其严肃的排印学术警示：**自动描摹绝非灵丹妙药，滥用描摹软件生产的字体往往是排印学上的灾难！**
* 扫描位图中的任何微小墨晕、纸张纤维噪点或光学畸变，都会被算法不加甄别地忠实还原成数十个细碎扭曲的贝塞尔断点；
* 算法无法理解排印学中的“骨骼对齐”概念，导致直笔不直、圆弧扁塌、左右两柱粗细不一。

尽管如此，在掌握严密参数调校的前提下，现代描摹工具依然是字体拓荒的重要武器：

## 1. Peter Selinger 的开源神器：Potrace

作为开源世界无可替代的几何矢量化核心引擎，彼得·塞林格（Peter Selinger）编写的 **potrace** 采用了一套精妙的多边形逼近与三次贝塞尔平滑拟合算法：
1. **轮廓多边形粗分解**：追踪二值化位图的黑白像素边缘；
2. **最优多边形降采样**：基于距离惩罚函数寻找顶点最少的最优闭合多边形；
3. **贝塞尔平滑逼近**：对多边形连续角点进行曲率评估，自动生成极度优美光滑的三次曲线段。
FontForge 深度内嵌了对 potrace 的无缝调用接口（`Element > AutoTrace`）。

## 2. 商业描摹巅峰：ScanFont

由 FontLab 官方出品的配套工具 **ScanFont**（图 12-13），专为将复杂手绘图样转化为专业字模而生。它提供了极其丰富的实时交互参数滑块：
* **Smoothness（平滑度）**：过滤微观像素毛刺的平滑门限；
* **Corner threshold（拐角阈值）**：决定何处强制折叠为锐利尖角、何处圆融过渡；
* **Curve fitting tolerance（曲线拟合容差）**：控制矢量线条偏离原始像素边缘的最大允许误差；
* **Extrema optimization（极值点自动对齐）**：确保生成的节点严格落在水平与垂直极值点切线上。

::: tip 图 12-13：ScanFont 中实时配置与动态预览位图自动描摹参数的交互式面板
![图 12-13：ScanFont 中实时配置与动态预览位图自动描摹参数的交互式面板](/images/fonts-encodings/fig12-13.png)
*图 12-13：ScanFont 中实时配置与动态预览位图自动描摹参数的交互式面板。*
:::

在实际描摹测试中对比发现：ScanFont 在处理字母 ‘A’ 尖锐的内角顶点时偶有轻微形变；而 potrace 则倾向于在平直长主干的中段冗余插入若干微小的控制点。**因此，任何自动描摹产物，都必须经过字体设计师在字形窗口中进行人工审查、删除冗余杂点、对齐极值并重构关键水平/垂直主干，方能真正达到工业级出版质量标准！**

---

# 结语

字体的设计与编辑，是数字人文科学中最具魅力的交汇点。它一方面扎根于数千年书法墨迹与金属活字的经典艺术风骨，另一方面又紧密咬合着离散微分几何、现代计算机图形学与庞大的二进制文件规范。

无论是驾驭商业流水线上的霸主 FontLab，还是驰骋在开源自由的 FontForge 天地中，真正赋予一套字体以不朽生命力的，始终是设计者那双在微观网格与宏观排印节律之间洞悉全局的慧眼，以及对技术规范毫厘不爽的工匠之心。
