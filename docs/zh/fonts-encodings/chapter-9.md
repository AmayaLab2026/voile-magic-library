---
title: "第 9 章：TeX 与 Omega 中的字体及其安装与使用"
description: "详尽解析 TeX 的盒子-胶水物理模型、折行算法、NFSS、DVI 格式、afm2tfm、fontinst 虚拟字体合成与 Omega 16位多向排版。"
---

# 第 9 章：$\TeX$ 与 $\Omega$ 中的字体及其安装与使用
### Chapter 9: Fonts in $\TeX$ and $\Omega$, Their Installation and Use
选自《Fonts & Encodings》第 235–314 页
*译者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

$\TeX$ 及其后继者 $\Omega$（Omega）堪称世界上最精密、最强大的数字排版系统。正因如此，这两个系统中的字体管理机制在初涉者眼中往往显得格外繁复且深奥。在本章中，我们将从三个核心维度对 $\TeX$ 与 $\Omega$ 的字体体系展开全面而严谨的剖析：

1. **字体在 $\TeX$ 与 $\Omega$ 中的使用**：探讨用户如何在普通 $\TeX$ 或 $\LaTeX$ 文档中调用、配置并组织系统中已安装的字体；
2. **字体的基本安装流程**：系统阐述如何将外部轮廓字体（如 PostScript Type 1、TrueType 以及 Multiple Master 字体）转换为 $\TeX$ 与 $\Omega$ 能够识别的底层度量文件与配置文件；
3. **字体的深度定制**：探索如何借助虚拟字体（Virtual Fonts, VF）与变换宏包（如 `fontinst`），构建包含复合重音、特殊连字、伪小型大写字母（Fake Small Capitals）、甚至能够进行上下文连缀分析的高级定制字体族。

最后，我们将深入探索打破传统 8 位束缚的 $\Omega$ 系统——它引入了多字节内部编码、OFM（Omega Font Metrics）、OVF（Omega Virtual Fonts）、动态有限状态流转换器 OTP（Omega Translation Processes）以及支持 32 种正交书写方向的宏大多向排版引擎。

---

## 1. 在 $\TeX$ 中使用字体（Using Fonts in $\TeX$）

### 1.1 $\TeX$ 导论：排版哲学与盒子-胶水模型（Introduction to $\TeX$）

要真正理解 $\TeX$ 是如何对待字体的，我们必须首先摒弃所见即所得（WYSIWYG）桌面排版软件中那种“将字符直接绘制到屏幕画布”的直观思维。在唐纳德·高德纳（Donald E. Knuth）教授构建的 $\TeX$ 宇宙中，排版的核心本质是纯粹的数学抽象与二维装配工程。

#### 盒子（Boxes）与胶水（Glue）

$\TeX$ 将排版构件抽象为两大基本物理实体：**盒子（Box）**与**胶水（Glue）**。

1. **盒子（Box）**：
   在 $\TeX$ 引擎眼中，每一个字符、每一个标点、每一条实线规则甚至每一幅外部插图，都被严格封装在一个刚性的矩形空间内。对于任意字符盒子，$\TeX$ 完全不在意其内部究竟绘制了何种优美的笔画曲线，而仅仅追踪该字符在二维平面上的三个基础几何度量参数：
   - **宽度（Width, $w$）**：字符沿当前基线（Baseline）延伸的水平跨度；
   - **高度（Height, $h$）**：字符从基线向上伸展至最高轮廓边缘的垂直距离；
   - **深度（Depth, $d$）**：字符从基线向下延伸至降部（Descender）最低底部的垂直距离。

   基线是排版的灵魂基准。字符盒子的左下角偏上位置即为参考原点 $(0,0)$。例如，小写字母“x”的高度即为通常所称的 x 高度（x-height），其深度为 0；而带有降部的小写字母“p”与“y”，则具有显著的正向深度；带有升部（Ascender）的字母“d”与“h”，则具有显著的高度。

2. **胶水（Glue）**：
   如果说盒子是构建文档大厦的刚性砖石，那么胶水就是连接砖石的弹性水泥。在西文排版中，词与词之间的空格并非固定宽度的实体，而是一段具有弹性的胶水。胶水具有三个核心数学分量：
   - **自然尺寸（Natural Space）**：胶水在未受任何外力拉伸或压缩时的理想宽度；
   - **可伸展量（Stretchability）**：当整行文本需要被两端对齐（Justified）而字符总宽度不足时，该胶水允许被拉长的最大弹性裕量；
   - **可收缩量（Shrinkability）**：当整行文本稍微超出排版版心宽度时，该胶水允许被压缩挤紧的最大弹性裕量。

#### 水平盒子（hbox）与垂直盒子（vbox）的层级嵌套

$\TeX$ 通过层级递归将微观元素装配为宏观页面：
- 若干个字符盒子与词间胶水在水平方向上依次排列，构成**水平盒子（hbox）**。段落中的单行文本即为一个 hbox；
- 若干个水平盒子再与行间胶水（Baselineskip，即基线行距胶水）在垂直方向上从上至下堆叠排列，构成**垂直盒子（vbox）**。文档中的文本栏、整个页面、甚至带有边注与页脚的完整版面，都是一层层嵌套的 vbox。

#### 折行算法与惩罚机制（Line Breaking and Demerits）

普通文字处理软件通常采用贪心算法（Greedy Algorithm）进行逐行排版：一行只要放得下单词就继续放，放不下就强行断行。这种局部最优策略往往导致段落末尾出现极其丑陋的巨大空白或极度稀疏的字行。

Knuth 为 $\TeX$ 设计了革命性的全局动态规划折行算法：
1. **不良度（Badness, $b$）**：衡量某一行内胶水偏离其自然尺寸的恶劣程度。若一行被拉伸或压缩得过于严重，其不良度将急剧上升；
2. **惩罚值（Penalties, $p$）**：在潜在断行位置（如连字符处、标点后、数学公式间）人为施加的代价权重。例如，在连字符处断行会引入正向惩罚，而在显式禁止断行处惩罚为无穷大（$+10,000$）；
3. **折损值（Demerits, $d$）**：综合单行不良度、断行惩罚值以及相邻两行胶水松紧差异（防止一行极紧、下一行极松的视觉突兀）计算出的段落全局恶劣评分。

$\TeX$ 会构建整个段落所有可能断行方案的有向无环图（DAG），并通过动态规划算法找出全局折损值总和最小的完美断行路径。这使得 $\TeX$ 排出的段落灰度（Typographic Color）极其均匀平稳。

#### 计算机现代字体族（Computer Modern Family）与光学尺寸

伴随 $\TeX$ 系统诞生的基石字体是高德纳亲自使用 METAFONT 编程语言设计的**计算机现代字体族（Computer Modern, CM）**。CM 字体族基于 19 世纪末苏格兰现代体（Modern Face，以 Monotype Modern 8A 为蓝本）精心绘制，具有极高的笔画对比度、几何垂直的轴线与锐利的细衬线。

CM 字体族不仅涵盖了丰富的风格变体：
- `cmr`（Computer Modern Roman，正体）
- `cmbx`（Computer Modern Bold Extended，粗体展宽）
- `cmti`（Computer Modern Text Italic，正文字体意大利斜体）
- `cmsl`（Computer Modern Slanted，伪斜体/机械倾斜体）
- `cmss`（Computer Modern Sans Serif，无衬线体）
- `cmtt`（Computer Modern Typewriter，等宽打字机体）
- `cmmi`（Computer Modern Math Italic，数学斜体）
- `cmsy`（Computer Modern Math Symbols，数学符号）
- `cmex`（Computer Modern Math Extension，数学可变延展符号）

更为关键的是，CM 字体族忠实继承了金属活字时代的**光学尺寸（Optical Sizing）**传统。在金属活字时代，5 磅的活字绝不是 10 磅活字的简单等比例缩小；若机械缩小，小磅数的细笔画将在印刷墨晕或视觉感知中彻底断裂消失，字怀（Counter）也会糊成一片。

高德纳在 METAFONT 代码中为不同的设计尺寸定义了精细的光学修正参数：
- `cmr5`（5pt）：专用于脚注、角标与复杂分式上下标。其字怀格外开阔，笔画对比度显著降低，主干粗细相对加粗，衬线更加厚实，字面率与字间距均经过大幅放宽；
- `cmr7`（7pt）：专用于一级上下标与图表标题；
- `cmr10`（10pt）：标准正文字体；
- `cmr12` 与 `cmr17`（12pt 与 17pt）：用于章节目大标题。其细笔画极其纤细锐利，笔画对比度极高，字距紧凑致密，展现出现代体优雅华贵的光学美感。

---

### 1.2 高层接口：基本 $\LaTeX$ 命令与新字体选择方案 NFSS（The High Level: Basic $\LaTeX$ Commands and NFSS）

在原始 Plain $\TeX$ 中，字体切换是极其原始且僵硬的。用户只能直接通过底层命令加载具体字体，例如 `\font\tenrm=cmr10`，然后调用 `\tenrm`。这种硬编码方式将字体族、尺寸、字重紧密绑定在一起；一旦想要将整篇文档正文由 10pt 改为 12pt，或者将正文由 CM 字体替换为 Times，必须对所有底层命令进行地毯式重写。

为了解决这一工程梦魇，弗兰克·米特尔巴赫（Frank Mittelbach）与赖纳·舍普夫（Rainer Schöpf）于 1989 年为 $\LaTeX$ 设计并引入了**新字体选择方案（New Font Selection Scheme, NFSS）**（并在 $\LaTeX 2_\varepsilon$ 中升级为 NFSS2）。

#### 经典 $\LaTeX$ 字体切换命令与其语义模型

NFSS 将文本层级的样式切换抽象为两套高层接口：
1. **带参数的作用域文本命令**：如 `\textbf{...}`、`\textit{...}`、`\textsf{...}`、`\textsc{...}`。这类命令不仅限制在局部花括号内生效，而且具备智能的字体修正功能（例如在斜体末尾自动插入倾斜校正 `\/`）；
2. **状态声明命令**：如 `\bfseries`、`\itshape`、`\sffamily`。这类命令会修改当前排版环境的全局状态机，直到遇到当前组（Group）的闭合括号。

#### NFSS 的五维正交选择空间

NFSS 的灵魂在于**正交性（Orthogonality）**。它将任何字体的属性彻底解耦为五个彼此独立、互不干扰的离散维度：

| 维度 | 参数命令 | 含义与标准取值范例 |
| :--- | :--- | :--- |
| **编码（Encoding）** | `\fontencoding{...}` | 描述字体槽位映射标准，如 `OT1`, `T1`, `TS1`, `T2A`, `LY1` |
| **字体族（Family）** | `\fontfamily{...}` | 字体家族名称简写，如 `cmr` (Computer Modern Roman), `ptm` (Times), `phv` (Helvetica), `pcr` (Courier) |
| **字重与字宽（Series）** | `\fontseries{...}` | 结合了重量（Weight）与宽度（Width），如 `m` (Medium), `b` (Bold), `bx` (Bold Extended), `c` (Condensed), `bc` (Bold Condensed) |
| **字形（Shape）** | `\fontshape{...}` | 笔画姿态与变体，如 `n` (Normal 直立), `it` (Italic 意大利斜体), `sl` (Slanted 机械倾斜), `sc` (Small Caps 小型大写) |
| **尺寸与行距（Size）** | `\fontsize{s}{b}\selectfont` | 物理字号 $s$ 与基线行距 $b$（如 `\fontsize{10pt}{12pt}\selectfont`） |

在 NFSS 状态机下，若用户当前处于无衬线体（`\sffamily`），此时执行粗体命令 `\bfseries`，NFSS 只会修改字重维度（`series = b`），而严格保留字族维度（`family = sf`），从而得到无衬线粗体，绝不会粗暴地跌回衬线粗体。所有维度的修改必须在调用底层原语 `\selectfont` 时才会被一次性解析为具体字体。

#### 字体定义文件（`.fd`）与自动替换机制

当五维参数确定后，$\LaTeX$ 如何知道去磁盘加载哪一个实际的 `.tfm` 度量文件？这一映射规则被固化在以 `<Encoding><Family>.fd` 命名的**字体定义文件（Font Definition File）**中。

例如，Times 字族在 T1 编码下的定义文件为 `t1ptm.fd`，其内部核心语法结构如下：

```latex
\ProvidesFile{t1ptm.fd}[2001/06/04 font definitions for T1/ptm.]

\DeclareFontFamily{T1}{ptm}{}

\DeclareFontShape{T1}{ptm}{m}{n}{
   <-> ptmr8t
}{}
\DeclareFontShape{T1}{ptm}{m}{it}{
   <-> ptmri8t
}{}
\DeclareFontShape{T1}{ptm}{m}{sl}{
   <-> ptmo8t
}{}
\DeclareFontShape{T1}{ptm}{m}{sc}{
   <-> ptmrc8t
}{}
\DeclareFontShape{T1}{ptm}{bx}{n}{
   <-> ptmb8t
}{}
\DeclareFontShape{T1}{ptm}{bx}{it}{
   <-> ptmbi8t
}{}
\DeclareFontShape{T1}{ptm}{b}{n}{<->ssub * ptm/bx/n}{}
\DeclareFontShape{T1}{ptm}{bx}{sl}{<->ssub * ptm/bx/it}{}
```

在 `\DeclareFontShape` 声明中：
- `<-> ptmr8t` 表示对该字形下的**任意尺寸**，统一映射到底层度量文件 `ptmr8t.tfm`；
- 如果支持光学尺寸（如 Computer Modern），则可使用离散区间语法进行尺寸分段：
  ```latex
  \DeclareFontShape{OT1}{cmr}{m}{n}{
     <-6> cmr5
     <6-7> cmr6
     <7-8> cmr7
     <8-9> cmr8
     <9-10> cmr9
     <10-12> cmr10
     <12-17> cmr12
     <17-> cmr17
  }{}
  ```
- `<-> ssub * ptm/bx/n`：**静默替换（Silent Substitution）**机制。当文档请求普通粗体 `ptm/b/n` 而实际字体只提供了展宽粗体 `ptm/bx/n` 时，NFSS 会自动桥接替换而不会中断排版。

#### NFSS 字体编码体系全景解析

在 NFSS 问世之前，$\TeX$ 世界的字体编码极度混乱。随着国际化排版需求的爆发，$\TeX$ 用户组（TUG）与欧洲 $\TeX$ 组织共同制定了系统化的标准化字体编码规范：

1. **OT1（Old $\TeX$ 1，高德纳原始 7 位编码）**：
   这是 8 位字节诞生前 Knuth 为原始 $\TeX$ 设计的 128 字符编码方案。由于 128 个槽位极其有限，Knuth 做出了若干充满智慧却也带有历史局限性的折中：
   - 0–9 槽位被挪用于存放希腊大写字母（$\Gamma, \Delta, \Theta, \Lambda, \Xi, \Pi, \Sigma, \Upsilon, \Phi, \Psi, \Omega$）；
   - 包含常用的五种经典西文连字：ff (11), fi (12), fl (13), ffi (14), ffl (15)；
   - 包含西班牙语倒问号（¿）与倒叹号（¡）；
   - **痛点**：OT1 中完全没有包含西欧语言所需的重音带符字母（如 é, à, ç, ü）。在 OT1 下，重音字母必须通过 `\accent` 原语在排版运行时动态装配（将独立的重音符号叠加在无重音基底字母上方）。这种动态合成不仅在某些缩放倍率下重音位置容易发生微小偏移，更为致命的是：**$\TeX$ 的自动断字分词引擎在遇到由动态重音拼装而成的单词时会彻底失效**！因为分词算法只能处理单一连续的底层字符槽位序列，一旦遇到 `\accent` 切换，当前单词的断字分析就会在重音处硬生生被掐断。

2. **T1（Cork 编码 / EC 字体）**：
   1990 年在爱尔兰科克（Cork）举行的 TUG 大会上正式确立的 8 位欧洲统一编码标准（256 个槽位）。
   - T1 编码将西欧与东欧主要拉丁语系所需的所有带重音字符（如德语、法语、西班牙语、波兰语、捷克语、匈牙利语、北欧语系的 ð, þ, æ, ø, å, œ, ß 等）全部固化为**独立的单个字符槽位**；
   - 彻底解决了欧洲多语言环境下自动断字与连字符切分的顽疾；
   - 规范了西文引号体系：收录了法式双书名引号 Guillemets（« 与 »）以及基线双低引号（„ 与 “）。

3. **TS1（Text Companion 伴随符号编码）**：
   伴随 T1 编码诞生的补充符号集（又称 TC 字体）。由于 256 个字符依然装不下所有排版辅助符号，TS1 专门用于容纳各类非字母文本符号：
   - 货币符号全家桶：欧元（€）、英镑（£）、日元（¥）、美分（¢）、佛罗林（ƒ）、通用货币符号（¤）；
   - 度量与科学符号：摄氏度（℃）、微度（µ）、公制与角分符号；
   - 预制通用分数（¼, ½, ¾）与上标数字（¹²³）；
   - 标点符号变体：长破折号、双破折号、项目符号圆点（Bullet）等。

4. **T2 系列与 X2（西里尔字母全景体系）**：
   西里尔字母体系涉及俄语、白俄罗斯语、乌克兰语、塞尔维亚语、马其顿语、保加利亚语以及中亚数十种前苏联少数民族语言，字符变体多达百余种，绝无可能塞进单一的 256 字符表中。为此，T2 委员会将其严密拆解为互补的四大子编码：
   - **T2A**：覆盖俄语、白俄罗斯语及大部分斯拉夫西里尔语言；
   - **T2B**：覆盖乌克兰语及若干少数民族西里尔语言；
   - **T2C**：覆盖高加索与西伯利亚地区的非斯拉夫语言西里尔文字；
   - **T2D**：覆盖中亚非斯拉夫语言（如哈萨克语、塔吉克语变体）；
   - **X2**：容纳所有历史古西里尔字母与极罕见变体符号。

5. **其他专用区域编码**：
   - **T3**：国际音标（IPA）专用编码；
   - **T4**：非洲拉丁字母体系（包含加纳语、尼日利亚语等所需的特殊舌根辅音字母）；
   - **T5**：越南语专用编码（越南语拥有多达 5 种声调与独特的触角元音 ơ, ư，声调与触角还会产生复合双重叠置，必须依赖专用编码矩阵）；
   - **LY1（TeX 'n' ANSI / Y&Y 编码）**：商业排版巨头 Y&Y 公司制定的 8 位编码，高度兼容 Windows ANSI (CP1252) 标准，在商业 PostScript 印刷出版中曾广为流行。

#### 数学字体与微观符号的 NFSS 机制

$\TeX$ 最引以为傲的成就在于其无与伦比的复杂数学公式排版能力。然而，在底层实现上，数学排版与文本排版有着天壤之别：
- 在数学模式下，单个字母代表的是数学变量，它们必须使用具有特殊倾斜角度与侧边留白的数学斜体（Math Italic）；
- 行间数学公式需要无级缩放的大型括号、中括号、花括号、积分号（$\int$）与求和号（$\sum$）；
- 传统 $\TeX$ 引擎内部存在一个**极度严苛的硬件级硬性约束：至多只能同时加载 16 个数学字体家族（Math Families, 编号 0 至 15）**！每一个数学符号在底层被编码为一个三元组 `(family, class, position)`。

NFSS 通过高度抽象的宏命令对这 16 个有限的数学家族进行统一调度：
- `\DeclareMathAlphabet{\mathbf}{OT1}{cmr}{bx}{n}`：声明数学字母表；
- `\DeclareSymbolFont{letters}{OML}{cmm}{m}{it}`：声明符号字体家族；
- `\DeclareMathSymbol{\alpha}{\mathord}{letters}{"0B}`：将数学符号与其具体的家族及槽位精准锚定。

数学公式中的大型变长定界符（Delimiters）则依赖底层的**可延伸字符装配机制**：当定界符需要随公式高度无限伸展时，$\TeX$ 会调用 `cmex10` 字体中的顶部零件（Top）、底部零件（Bottom）、中间连接件（Mid）以及可重复铺设的垂直连接段（Extender），像拼接水管一样拼装出任意高度的完美大括号！

---

### 1.3 底层机制：$\TeX$ 引擎与 DVI 字节码格式（The Low Level: $\TeX$ and DVI）

当用户在命令行执行 `latex document.tex` 时，$\TeX$ 引擎内部究竟发生了什么？$\TeX$ 并不会直接输出 PDF，更不会直接操纵打印机硬件。它的输出是一份精简至极的二进制中间文件——**DVI（Device Independent，设备无关文件）**。

#### DVI 虚拟机的内部结构与寄存器状态机

DVI 文件格式在本质上是一份极其纯粹的**虚拟机字节码指令流**。DVI 虚拟机维护着一个严密的几何状态机，包含六个核心内部寄存器：

$$h, v, w, x, y, z$$

- $h$：当前笔刷在页面上的**水平坐标**（从左侧参考点向右度量）；
- $v$：当前笔刷在页面上的**垂直坐标**（从顶部参考点向下度量）；
- $w, x$：水平方向的当前步长记忆寄存器；
- $y, z$：垂直方向的当前步长记忆寄存器。

此外，DVI 虚拟机配备了一个**坐标堆栈（Coordinate Stack）**，支持通过 `push` 指令将当前 $(h, v, w, x, y, z)$ 完整压入堆栈保存，并在完成局部复杂排版（如上下标或盒子组装）后通过 `pop` 指令瞬间恢复母坐标系。

#### DVI 核心字节码指令全集

DVI 字节码指令极其紧凑，主要分为以下几大类别：

1. **字符设置与打印指令**：
   - `set_char_0` 至 `set_char_127`（单字节操作码 0–127）：打印字符编号 $c$ 并使水平坐标 $h$ 自动向前递增该字符的宽度 $w(c)$；
   - `set1` 至 `set4`：后跟 1 至 4 字节的字符槽位编号，用于打印大字符集的字符并自动前进；
   - `put1` 至 `put4`：打印指定字符，但**不移动水平坐标 $h$**（常用于重音叠加或多字符就地重合）。

2. **几何实线绘制指令**：
   - `set_rule`：后跟规则的高度 $a$ 与宽度 $b$，在当前坐标 $(h, v)$ 处绘制一个实心黑矩形，并将 $h$ 前移 $b$；
   - `put_rule`：绘制矩形但不改变 $h$。

3. **坐标位移指令**：
   - `right1..4`：水平向右移动指定距离（若为负数则向左移）；
   - `down1..4`：垂直向下移动指定距离（若为负数则向上移）；
   - `w0`, `w1..4`, `x0`, `x1..4`：带寄存器记忆的水平相对位移；
   - `y0`, `y1..4`, `z0`, `z1..4`：带寄存器记忆的垂直相对位移。

4. **字体选择与定义指令**：
   - `fnt_num_0` 至 `fnt_num_63`（操作码 171–234）：单字节快速切换当前活动字体编号；
   - `fnt1..4`：切换任意编号的活动字体；
   - `fnt_def1..4`：声明字体元数据，紧随五个关键参数：
     1. 字体内部数字索引；
     2. 字体校验和（Checksum，必须与底层 `.tfm` 文件头严格一致）；
     3. 缩放尺寸（Actual Size，以 `sp` 为单位）；
     4. 光学设计尺寸（Optical Design Size，以 `sp` 为单位）；
     5. 字体名称字符串（不含 `.tfm` 后缀）。

5. **页面结构与文件导言指令**：
   - `bop`（Begin of Page）：页面起始标志，后跟 10 个计数寄存器（用于定位页码）以及指向上一页 `bop` 的反向指针（使得 DVI 阅读器能够闪电般地逆向翻页浏览）；
   - `eop`（End of Page）：当前页面排版终结，强制清空堆栈；
   - `pre`（Preamble）：文件起始导言，记录 DVI 格式版本号及单位缩放比例因子；
   - `post`（Postamble）：后置导言，位于所有排版页面之后，汇总全局页面总数、最大堆栈深度、以及整篇文档所用到的所有 `fnt_def` 字体定义列表；
   - `post_post`：位于文件绝对末尾，记录指向 `post` 的物理偏移指针，并在最后填补至少四个操作码 223（Hex `DF`）字节。

#### 纯整数定点运算机制：缩放点单位 `sp`

Knuth 在设计 DVI 格式时确立了一条铁律：**DVI 文件在任何硬件架构、任何操作系统上必须输出像素级绝对一致的结果**。为了彻底消灭不同 CPU 在浮点数运算（IEEE 754 浮点舍入误差）上的微小精度漂移，$\TeX$ 与 DVI 内部的所有几何距离**全部采用纯 32 位有符号整数进行定点算术运算**！

其最基础的度量单位被称为**缩放点（Scaled Point, `sp`）**：

$$1\text{ pt} = 65,536\text{ sp} = 2^{16}\text{ sp}$$

由于 1 美制印刷磅（pt）约等于 $1/72.27$ 英寸，1 个 `sp` 的物理跨度仅为：

$$1\text{ sp} \approx 5.363 \times 10^{-6}\text{ mm} = 5.363\text{ 纳米 (nm)}$$

这一极度微小的度量粒度远小于可见光的波长，更远超任何高精度工业激光照排机的物理分辨率。在整篇文档排版过程中，所有的字框宽度累加、字距调整与胶水拉伸完全在纯整数空间内进行加减乘除，杜绝了任何累积舍入误差。

#### DVI 字节码的反汇编透视：DVX 格式

为了直观观察 DVI 的字节码流，我们借助 Haralambous 开发的 `dvi2dvx` 工具将一段编译后的二进制 DVI 切片转换为 XML 文本表述（DVX）：

```xml
<fontdef id="18" checksum="20786036" scale="655360" designsize="655360" name="T1lemondemn"/>
<font id="18"/>
<set>the</set>
<right dim="167112"/>
<set>te</set>
<right dim="-14745"/>
<set>xt</set>
<right dim="167112"/>
<set>tha</set>
<right dim="-18350"/>
<set>t</set>
<right dim="167112"/>
<set>y</set>
<right dim="-11141"/>
<set>ou</set>
<right dim="167112"/>
<set>ar</set>
<right dim="-7864"/>
<set>e</set>
<right dim="167112"/>
<set>curr</set>
<right dim="-9830"/>
<set>ently</set>
<right dim="167112"/>
<set>r</set>
<right dim="-13107"/>
<set>eading</set>
```

在这段真实的剖析片段中：
1. `T1lemondemn` 字体（Le Monde Livre 字族的正体，T1 编码）被声明为内部编号 18，缩放尺寸为 655,360 `sp`（即精确的 10pt）；
2. 词间空格通过 `<right dim="167112"/>` 实现（167,112 `sp` 约等于 2.55pt，这是该字体在当前行计算出的词间弹性胶水展开量）；
3. 单词内部的字母组合之间出现了负向的 `<right dim="-..."/>`（例如在 "t" 与 "e" 之间收紧 14,745 `sp`，在 "a" 与 "t" 之间收紧 18,350 `sp`）。这表明：**$\TeX$ 在将段落写入 DVI 时，已经将字偶间距调整（Kerning）全部计算完毕并直接硬编码为物理坐标微调**！

#### 字符盒子与物理墨迹的彻底解耦

这一底层机制揭示了 $\TeX$ 最精妙的架构哲学：**$\TeX$ 内部根本没有字形（Glyphs），只有几何盒子（Boxes）**。
- $\TeX$ 引擎只负责计算盒子在哪里摆放；
- DVI 文件中只记载哪个位置放哪个字符编号；
- 字符究竟长什么样？是由黑白像素构成的位图，还是由三次贝塞尔曲线构成的矢量轮廓？$\TeX$ 完全不知情，也根本不需要知情！
- 真实的物理光栅化与墨迹绘制工作，被彻底推迟到了编译流水线的后处理环节——由专门的**设备驱动程序（DVI Drivers）**来接管并直面物理世界。

---

### 1.4 后 $\TeX$ 时代：直面物理输出与真实世界（“Après-$\TeX$”: Confronting the Real World）

当 DVI 文件离开 $\TeX$ 的象牙塔后，必须直面复杂的物理设备生态。负责将 DVI 解析并转化为印刷品或显示图像的软件被称为 DVI 驱动程序，其中最著名的代表是托马斯·罗基茨基（Tomas Rokicki）开发的 `dvips`，以及后来由韩国学者朝真（Cho Jin-Hwan）与 Hirata 扩展的 `dvipdfmx`。

#### `kpathsea` 文件路径检索子系统与动态位图生成链

在现代 $\TeX$ 发行版（如 TeX Live 与 MacTeX）中，所有命令行工具的底层都集成了卡尔·贝里（Karl Berry）开发的 `kpathsea` 动态路径检索库。

当 `dvips` 读取 DVI 文件并遇到一个名为 `cmr10` 的字体请求时，`kpathsea` 会启动三级自动化文件寻访与生成流水线：
1. **`mktextfm`**：若系统中缺失该字体的度量文件 `cmr10.tfm`，自动在后台触发生成该 TFM；
2. **`mktexmf`**：若缺少对应的 METAFONT 源代码 `cmr10.mf`，自动尝试从通用母版或参数包中动态拼装出源代码；
3. **`mktexpk`**：若需要位图光栅化渲染，`mktexpk` 会根据目标输出设备的具体物理分辨率（如 600 DPI）与驱动模式（如惠普激光打印机模式 `ljfour`），自动调用 METAFONT 编译引擎生成对应的压缩位图字体文件 `cmr10.600pk`。

#### `dvips` 对 PostScript Type 1 字体的解析与映射机制

随着桌面出版彻底倒向矢量时代，基于 METAFONT 的 PK 点阵位图字体已不再适应屏幕缩放与高阶激光照排的需求。印刷工业全面采用了由 Adobe 制定的 PostScript Type 1 矢量字体标准。

由于 DVI 文件中仅记载着 TFM 文件的名称（如 `ptmr8t`），`dvips` 必须依据一套严密的映射数据库——**`psfonts.map`**（或现代的 `pdftex.map`）来决定如何翻译每一个字体条目。

一条典型的 `psfonts.map` 映射条目如下所示：

```text
ptmr8t Times-Roman " T1Encoding ReEncodeFont " <[T1-WGL4.enc <ptmr8a.pfb
```

这条配置包含了驱动程序完成矢量排版所需的全部密码：
- `ptmr8t`：DVI 文件中所引用的 TFM 逻辑名称；
- `Times-Roman`：PostScript 解释器内部识别的标准 PostScript 字体名称（FontName）；
- `" T1Encoding ReEncodeFont "`：一段在 PostScript 解释器中即时执行的 PostScript 代码片段，指示解释器使用随后的编码向量对字体的字符字典进行就地重新索引（Re-encoding）；
- `<[T1-WGL4.enc`：指示 `dvips` 读取外部编码向量文件 `T1-WGL4.enc` 并将其作为数组载入 PostScript 数据流；
- `<ptmr8a.pfb`：指示 `dvips` 打开磁盘上的二进制 Type 1 字体文件 `ptmr8a.pfb`，将其内容完整嵌入（Embed）到最终生成的 `.ps` 打印文件中；如果该字段为空，则表明该字体属于打印机 ROM 中内置的核心字体（Resident Font），驱动程序将只生成调用指令而不内嵌轮廓数据。

#### `pdftex` 的革命性演进与微观排版（Micro-typography）

1996 年，捷克布尔诺马萨里克大学的博士生韩越康（Hàn Thế Thành）推出了改变 $\TeX$ 历史进程的引擎——**`pdftex`**。

`pdftex` 彻底颠覆了“$\TeX \to$ DVI $\to$ PostScript $\to$ Distiller $\to$ PDF”的传统冗长流水线，直接在 $\TeX$ 引擎内部整合了 PDF 矢量生成器与 Type 1 / TrueType 字体解析器。更为震撼的是，Thành 在 `pdftex` 中首次在软件工程层面实现了赫尔曼·察普夫（Hermann Zapf）梦寐以求的现代排版两大顶峰算法：

1. **字符边缘凸出（Character Protrusion / Margin Kerning）**：
   在纯几何排版中，若一行以标点符号（如逗号、句号、引号、连字符）或具有大角度外倾笔画的字母（如大写“A”, “V”, “W”）作为行首或行尾，由于这些字符的空白面积较大，会导致文本块在视觉感知上出现参差不齐的凹陷。`pdftex` 允许根据每个字符的光学权重，将标点符号与特定字母的边缘**微量悬挂凸出到排版边框边界线之外**（通常为字符宽度的 20% 至 70%），从而在人眼视觉感知中塑造出如刀削般笔直完美的段落边缘！

2. **字体横向微伸缩（Font Expansion / hz-algorithm）**：
   传统折行算法仅能调节单词之间的词间胶水（Glue）。当某行单词较长时，仅拉伸词间距往往造成难以容忍的巨大缝隙（视觉“白溪”或“河流”）。察普夫与 Thành 提出的 hz 算法允许 $\TeX$ 在进行全局折行评估时，**对整行中所有字符的字体轮廓进行极微量的横向几何缩放**（通常在 $\pm 1\%$ 至 $\pm 2\%$ 之间微调）。这种极细微的变形在人眼视觉下完全无法察觉任何字形失真，却为动态规划折行算法提供了极其宽广的数学解空间，使断行不良度（Badness）与连字符断字概率断崖式下降，排版灰度达到了空前绝后的均匀与致密。

---

## 2. 为 $\TeX$ 安装新字体（Installing Fonts for $\TeX$）

### 2.1 $\TeX$ 目录结构（TDS）规范

将外部商业字体安装到 $\TeX$ 系统绝非随意将文件扔进某个目录。现代 $\TeX$ 系统遵循严格的**$\TeX$ 目录结构标准（$\TeX$ Directory Structure, TDS）**。对于任意字体包，其内部构件必须精确归位至系统本地树（如 `TEXMFLOCAL`）：

- `fonts/afm/<supplier>/<typeface>/`：存放 Adobe 原始度量文件（`.afm`）；
- `fonts/type1/<supplier>/<typeface>/`：存放 PostScript Type 1 轮廓文件（`.pfb` / `.pfa`）；
- `fonts/truetype/<supplier>/<typeface>/`：存放 TrueType 轮廓文件（`.ttf`）；
- `fonts/opentype/<supplier>/<typeface>/`：存放 OpenType 轮廓文件（`.otf`）；
- `fonts/tfm/<supplier>/<typeface>/`：存放 $\TeX$ 专用底层度量文件（`.tfm`）；
- `fonts/vf/<supplier>/<typeface>/`：存放虚拟字体文件（`.vf`）；
- `fonts/map/dvips/<typeface>/`：存放驱动映射文件（`.map`）；
- `tex/latex/<typeface>/`：存放 $\LaTeX$ 字体定义宏文件（`.fd` 与 `.sty`）。

归档完成后，必须在终端执行 `mktexlsr`（或 `texhash`）以重建 `ls-R` 路径哈希索引数据库，确保 `kpathsea` 能够在毫秒级定位文件。

---

### 2.2 快速工具：`afm2tfm` 深度运用

对于普通西文字体的快速集成，系统提供了一个短小精悍的 C 语言命令行工具——**`afm2tfm`**。

#### 底层几何变换与命令行参数

`afm2tfm` 能够直接解析标准 AFM 文件中的字符包围盒与字偶间距表，并生成 $\TeX$ 核心所需的 TFM 文件：

```bash
afm2tfm CentaurMT.afm -v t1centaurmn.vpl -T EC.enc
```

其关键高级控制参数具有深厚的几何意义：
- **`-s slant`（仿斜体变换）**：
  若某款字体只有正体而缺乏意大利斜体，可通过 `-s` 施加仿斜切变换。其变换矩阵对应于剪切形变：
  $$\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} 1 & \text{slant} \\ 0 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}$$
  通常传入参数如 `-s 0.167`（对应约 $9.5^\circ$ 的向右倾角，$\text{slant} = \tan \theta$）。
- **`-d extend`（展宽/压缩变换）**：
  对字体沿水平 $x$ 轴施加缩放比例因子（如 `-d 0.85` 为紧缩体，`-d 1.15` 为展宽体）。
- **`-T encoding_file`**：
  指定目标重编码向量（如 `EC.enc` 对应 T1 编码，`8r.enc` 对应 TeXBase1 编码）。
- **`-v vpl_file`**：
  指示生成虚拟属性列表（Virtual Property List, `.vpl`）文件，从而允许在更高层级拼装复合虚拟字体。

`afm2tfm` 在控制台输出的映射字符串，可直接追加到 `psfonts.map` 中：

```text
CentaurMT CentaurMT " ECEncoding ReEncodeFont " <[EC.enc <CentaMT.pfb
```

随后调用 `vptovf` 实用程序将文本格式的 `.vpl` 文件组装为最终的二进制 `.vf` 与 `.tfm` 文件：

```bash
vptovf t1centaurmn.vpl t1centaurmn.vf t1centaurmn.tfm
```

---

### 2.3 工业级字体安装利器：`fontinst` 体系

虽然 `afm2tfm` 足以应对单一字体的简单转换，但在面对庞大的商业专家级字体族时，它就显得力不从心了。

商业专业字体（如 Adobe Garamond Premier Pro、Monotype Dante 等）往往拆分为若干互补的子字体文件：
- 常规文本字体（包含常规大写字母、小写字母与基本标点）；
- 专家集字体（Expert Set, `.sc` / `.exp`，包含真正设计的小型大写字母、全套旧体数字 Oldstyle Figures、分数符、修饰花体）；
- 替换字形字体（包含连字 `ct`, `st`, `ffi`, `ffl`，重音大写字母等）。

$\LaTeX$ 的 NFSS 规范要求：**同一个字形组合（如小型大写字母 `\textsc`）必须在一个统一的编码方案内无缝呈现**。如果使用 `afm2tfm`，用户将无法让大写字母与来自另一个文件的小型大写字母以及来自常规文件的标点符号协同工作。

为了彻底打通这一复杂鸿沟，艾伦·杰弗里（Alan Jeffrey）、罗兰·霍尔茨（Rowland McDonnell）与乌尔里克·迪尔克（Ulrik Vieth）共同研发了 $\TeX$ 历史上最强悍的字体安装基础设施——**`fontinst` 宏包**。

#### `fontinst` 的四步流水线架构

`fontinst` 并非独立编译的二进制程序，而是**完全使用 $\TeX$ 宏语言写成的高阶宏包系统**！它利用 $\TeX$ 自身的巨型计算引擎来操纵度量数据。

其标准处理流水线如下：

```
[原始 AFM 文件] 
      │ (通过 \transformfont 转换)
      ▼
[MTX 度量文件] (包含 \setglyph, \setglyphdim 等纯文本度量指令)
      │
      ├───────────────────────┐
      ▼                       ▼
[ETX 编码目标文件]      [用户自定义规则脚本]
      │                       │
      └───────────┬───────────┘
                  │ (通过 \installfont 编译合成)
                  ▼
         [VPL 虚拟属性列表] + [PL 属性列表]
                  │
      ┌───────────┴───────────┐
      ▼ (调用 vptovf)          ▼ (调用 pltotf)
[VF 虚拟字体文件]        [TFM 度量文件] + [.fd 宏包定义文件]
```

#### 标准安装驱动脚本剖析

用户只需编写一个简短的驱动文件（如 `install-centaur.tex`）：

```latex
\input fontinst.sty

\needsfontinstversion{1.926}

\recordtransforms{centaur-rec.tex}

\transformfont{rcen8r}{\reencodefont{8r}{\fromafm{CentaurMT}}}
\transformfont{rceni8r}{\reencodefont{8r}{\fromafm{CentaurMT-Italic}}}
\transformfont{rcenb8r}{\reencodefont{8r}{\fromafm{CentaurMT-Bold}}}
\transformfont{rcenbi8r}{\reencodefont{8r}{\fromafm{CentaurMT-BoldItalic}}}

\installfonts

\installfamily{T1}{centaur}{}

\installfont{rcen8t}{rcen8r,latin}{t1}{T1}{centaur}{m}{n}{}
\installfont{rceni8t}{rceni8r,latin}{t1}{T1}{centaur}{m}{it}{}
\installfont{rcenb8t}{rcenb8r,latin}{t1}{T1}{centaur}{bx}{n}{}
\installfont{rcenbi8t}{rcenbi8r,latin}{t1}{T1}{centaur}{bx}{it}{}
\installfont{rcenc8t}{rcen8r,latin}{t1c}{T1}{centaur}{m}{sc}{}
\installfont{rceno8t}{rcen8r,latin}{t1j}{T1}{centaur}{m}{ol}{}

\endinstallfonts

\endrecordtransforms
\bye
```

运行 `tex install-centaur.tex` 后：
1. `fontinst` 自动解析 AFM，将字形映射到 TeXBase1 (8r) 基础度量空间；
2. 引入 `latin.mtx` 标准度量变换库，计算所有复合重音字母的装配间距；
3. 根据目标编码 `t1.etx`，自动生成完整的虚拟字体定义；
4. 自动合成并输出规范的 `t1centaur.fd` 宏包，无需人工干预即可在 $\LaTeX$ 中直接通过 `\fontfamily{centaur}\selectfont` 进行排版！

---

### 2.4 多重母版字体（Multiple Master Fonts）在 $\TeX$ 中的实现

在 20 世纪 90 年代，Adobe 推出了划时代的矢量字体格式——**多重母版字体（Multiple Master, MM）**。MM 字体允许在同一个字体文件内部定义多个连续的设计轴（Design Axes），最常见的三大设计轴为：
1. **字重轴（Weight）**：从超细（Extra Light，如数值 300）到极粗（Black，如数值 800）连续渐变；
2. **字宽轴（Width）**：从特紧缩（Condensed，如数值 450）到特展宽（Expanded，如数值 850）连续渐变；
3. **光学尺寸轴（Optical Size）**：从正文字体（6pt）到大标题（72pt）连续渐变。

#### 连续设计轴与 $\TeX$ 离散体系的冲突

理论上，如果 $\TeX$ 能够动态操纵 Multiple Master 字体，排版学者可以实现许多震撼的排版特效：
- 例如依据当前行排版的充盈度，动态微调整行字符的宽度轴，从而消除连字符；
- 或者通过微调字重与光学尺寸，使得一本书的排版版面精准契合 16 页印张（Signature）的整数倍！

然而，$\TeX$ 诞生的哲学是基于不可变离散度量文件（TFM）的确定性排版，无法直接接入运行时的多维参数插值引擎。此外，Adobe 后来全面转向 OpenType，并官方放弃了 MM 格式。

#### 利用 LCDF Typetools 进行切片固化

在 $\TeX$ 或 $\Omega$ 中使用 MM 字体的唯一现实路径是：**预先通过插值工具从连续设计空间中“切片提取”出特定的离散实例（Instances），并将其伪装为标准的 PostScript Type 1 字体交付 $\TeX$ 使用**。

埃迪·科勒（Eddie Kohler）编写的开源工具集 **LCDF Typetools** 中的 `mmafm` 与 `mmpfb` 提供了这一工业级能力：

```bash
mmafm --weight=380 --width=460 --optical-size=6 MinionMM.amfm > minion_380_460_6.afm
mmpfb --weight=380 --width=460 --optical-size=6 MinionMM.pfb  > minion_380_460_6.pfb
```

上述命令指示插值引擎在 Minion MM 字体的三维空间中精确定位坐标点 `(weight=380, width=460, optical_size=6)`，并计算出该点处所有三次贝塞尔控制点与字符度量的物理数值，分别生成对应的单体 `.afm` 与 `.pfb` 文件。

生成的字体在 `dvips` 中的映射配置如下：

```text
minion_380_460_6 Minion_M_380_460_6_ " ECEncoding ReEncodeFont " <EC.enc <minion_380_460_6.pfb
```

从此，该实例便可完全作为一个常规的单体 Type 1 字体，通过标准的 `fontinst` 流程无缝编织进 NFSS 体系。

---

## 3. 按用户需求深度定制 $\TeX$ 字体（Customizing $\TeX$ Fonts for the User's Needs）

### 3.1 虚拟字体（Virtual Fonts）的体系架构与设计哲学

虚拟字体（Virtual Font, VF）是高德纳与戴维·福斯（David Fuchs）在 1989 年引入 $\TeX$ 世界的最具革命性的软件工程创造之一。

#### 虚拟字体与真实字体的本质分野

在底层物理意义上，真实字体（Real Font，如 PK 位图字体、Type 1 PFB、TrueType TTF）是**字形轮廓或像素数据的最终提供者**。

而虚拟字体（`.vf` 文件配合 `.tfm`）在本质上是**一份寄生于 DVI 虚拟机上层的高度结构化的“宏重定向规则库”**：
- 当 $\TeX$ 编译文档时，它读取虚拟字体的 `.tfm`，认为自己在使用一款具有确定高度、宽度与深度的常规字体；
- 当 DVI 驱动程序（如 `dvips`）解析 DVI 文件遇到该虚拟字体的字符设置指令时，驱动程序会拦截该指令，并在其内部展开为一段包含若干条基础 DVI 原语的子指令序列！

#### 虚拟字符展开的无限可能性

在虚拟字体的内部指令块中，排版师拥有操纵 DVI 虚拟机的全部特权：
- **字形替换与跨字体引用**：字符槽位可以直接指向另一个真实字体的特定槽位，甚至从十个不同的字体文件中各借调一部分字符组装成一个虚拟字体；
- **几何移动与重叠合成**：可以发出任意 `right` 与 `down` 移动指令，将一个独立的重音符号精准叠加在某个大写字母的正上方；
- **递归嵌套**：虚拟字体可以透明地调用另一款虚拟字体；
- **绘制复杂规则与外部内嵌代码**：甚至可以在单个字符槽位内注入一段 PostScript 特效代码（如为字符添加阴影、旋转、下划线、绘制花边）。

最为关键的是：**在 DVI 格式规范内，驱动程序完全负责虚拟字体的递归展开，外部宏包与 $\TeX$ 排版引擎完全感受不到虚拟字体的存在**。这使得排版系统在保留绝对确定性的同时，获得了近乎无限的结构扩展能力。

---

### 3.2 ETX 与 MTX 文件的高级语法与数据模型

在 `fontinst` 体系中，虚拟字体被严格解构为两个核心文件：**编码模板文件（`.etx`）**与**度量计算文件（`.mtx`）**。

#### ETX（Encoding $\TeX$）文件的语法架构

`.etx` 文件定义了目标字体中每个槽位的排版语义。其核心语法形式如下：

```latex
\relax
\encoding

\setslot{A}
   \comment{The letter A.}
\endsetslot

\setslot{f_i}
   \comment{The ligature fi.}
\endsetslot

\setslot{f}
   \ligature{LIG}{i}{f_i}
   \ligature{LIG}{f}{f_f}
   \ligature{LIG}{l}{f_l}
\endsetslot
```

在 `\setslot` 块内，最精妙的机制在于**连字控制命令 `\ligature`**。$\TeX$ 内部的连字与字距机在底层支持极其复杂的四种状态转移机制：

1. **`LIG`（经典全替换连字）**：
   $$A + B \to C$$
   吞噬输入字符 $A$ 与 $B$，直接输出复合连字 $C$（如 $f + i \to fi$）；
2. **`/LIG`（后向保留连字 / Post-ligature）**：
   $$A + B \to A + C$$
   保留首个字符 $A$，将后续字符 $B$ 替换为特定形态 $C$；
3. **`LIG/`（前向保留连字 / Pre-ligature）**：
   $$A + B \to C + B$$
   将首个字符 $A$ 替换为变体形态 $C$，但保留后续字符 $B$；
4. **`/LIG/`（双向保留连字 / Contextual ligature）**：
   $$A + B \to A + C + B$$
   保留两端字符，仅在中间动态注入连接构件；
5. **`/LIG/>` 与 `LIG/>`（步进状态机连字）**：
   控制内部指针在完成替换后跳过若干字符，防止状态机陷入死循环。

#### MTX（Metrics $\TeX$）文件的语法架构

`.mtx` 文件则负责具体的字符物理几何与合成工程。其核心原语构架包括：

- **`\setglyph{glyph_name} ... \endsetglyph`**：声明一个新字形；
- **`\glyph{source_name}{scale}`**：从源字体中提取指定字形并按比例缩放（$1000$ 表示 $100\%$）；
- **`\movert{dimension}` 与 `\moveup{dimension}`**：在局部笛卡尔坐标系中相对平移笔刷原点；
- **`\installglyph{glyph_name}{etx_name}{commands}`**：高阶复合字形装配指令；
- **字距微调继承（Kerning Inheritance）**：
  ```latex
  \setleftkerning{Eacute}{E}{1000}
  \setrightkerning{Eacute}{E}{1000}
  \setleftrightkerning{Ecircumflex}{E}{1000}
  ```
  上述指令指示度量引擎：带尖音符的 `Eacute` 在左侧与右侧的字距微调行为，与母体字母 `E` 严格保持 $100\%$（$1000/1000$）一致，排版师无需为数百个带重音字母手动重复定义成千上万个字偶间距！

---

### 3.3 实战应用范例全解

#### 范例一：伪小型大写字母（Fake Small Capitals）的精确合成

小型大写字母（Small Capitals）是西文专业排版中不可或缺的元素，常用于缩写词（如 NASA, UNESCO）、人名以及章节首行。如果一款商用字体未附带专门设计的原生小型大写字母（`Expert Set`），直接使用大写字母缩小往往导致笔画过于纤细弱小，在视觉灰度上产生刺眼的苍白感。

借助 `fontinst`，排版师可以编写高阶算法自动合成高质量的伪小型大写字母：

```latex
\setint{smallcapsscale}{800}
\setint{smallcapskerning}{900}

\installglyph{Asmall}{A}{
   \glyph{A}{\int{smallcapsscale}}
   \movert{\int{smallcapskerning}}
}
```

在合成代码中：
1. 将大写字母 `A` 的轮廓统一等比缩放至 $80\%$（高度接近 x 高度）；
2. 由于等比缩放后字符笔画相对变细，且原大写字母的侧边留白被成比例缩小，导致字符在排版时显得过于拥挤。代码通过 `\movert{\int{smallcapskerning}}` 显式增加额外的侧边字距微调，使伪小型大写字母在文本行中展现出更加均衡稳定的排版灰度。

#### 范例二：为西欧文字增补定制连字（Adding Ligatures to a Font）

法语出版界拥有一批经典的尊称缩写历史习惯，例如：
- 称呼未婚女性的“Mademoiselle”（小姐）在传统法文排版中必须书写为带有下划修饰或紧凑连字的“$\text{M}^{\text{lle}}$”；
- 称呼已婚女士的“Madame”（夫人）书写为“$\text{M}^{\text{me}}$”；
- 荷兰语中的双字母连缀“ij”与“uw”。

若字体中未内嵌这些专用连字，`fontinst` 允许通过连字树进行智能构造：

```latex
\setslot{M}
   \ligature{LIG}{l}{M_l}
\endsetslot

\setslot{M_l}
   \comment{(False) intermediate ligature Ml}
   \ligature{LIG}{l}{M_l_l}
\endsetslot

\setslot{M_l_l}
   \comment{(False) intermediate ligature Mll}
   \ligature{LIG}{e}{M_l_l_e}
\endsetslot

\setslot{M_l_l_e}
   \comment{Real final ligature Mlle}
\endsetslot
```

在 MTX 文件中，复合字形 `M_l_l_e` 的装配逻辑如下：

```latex
\installglyph{M_l_l_e}{M_l_l_e}{
   \glyph{M}{1000}
   \movert{\kerning{M}{l}}
   \moveup{300}
   \glyph{l}{650}
   \movert{-50}
   \glyph{l}{650}
   \movert{-50}
   \glyph{e}{650}
}
\setleftkerning{M_l_l_e}{M}{1000}
\setrightkerning{M_l_l_e}{e}{1000}
```

当排版引擎读取文本流遇到连续的 `M-l-l-e` 四个字符时，$\TeX$ 内部的有限状态机将沿连字树步步推进：$M+l \to M_l$；$M_l+l \to M_{ll}$；$M_{ll}+e \to M^{lle}$！这一连缀变换过程对终端用户完全透明，文档作者只需输入常规字符串 `Mlle`，编译后即可自动呈现出精雕细琢的古典缩写连字！

#### 范例三：基于 8 位虚拟字体实现阿拉伯文上下文连缀分析（Contextual Analysis in Arabic）

阿拉伯文字是典型的草书连缀书写系统。同一个阿拉伯字母在单词的不同位置，其笔画形态会发生颠覆性的剧烈改变：
1. **孤立态（Isolated Form）**：当字符前后均无连缀时；
2. **词首态（Initial Form）**：当字符与后续字母相连时；
3. **词中态（Medial Form）**：当字符同时与前后字母相连时；
4. **词尾态（Final Form）**：当字符仅与前序字母相连时。

在现代系统（如 OpenType 与 HarfBuzz）诞生前，传统 $\TeX$ 引擎被普遍认为绝对不可能排版阿拉伯文，因为 8 位 $\TeX$ 完全缺乏上下文敏感替换机制。

然而，Haralambous 在本章中揭示了一个令世人惊叹的技术创举：**完全利用 $\TeX$ 底层的 `\ligature` 状态机指令网络，在纯 8 位虚拟字体中硬生生模拟出了阿拉伯文的上下文连缀引擎**！

其核心机理是引入虚拟的不可见“前驱探测符”与“后继边界符”：
- 当一个字母遇到左连缀条件时，触发 `/LIG` 连字指令将自身重写为词首态；
- 若后续字符持续连缀，则触发 `/LIG/` 双向连字持续锁定在词中态；
- 一旦遇到空格、标点符号或词尾边界符，立即触发终结连字跌入词尾态或孤立态：

```latex
\setslot{ghayn.init}
   \ligature{/LIG}{ghayn.medi}{ghayn.medi}
   \ligature{/LIG}{dal.fina}{dal.isol}
\endsetslot

\setslot{ghayn.medi}
   \ligature{LIG/}{space}{ghayn.fina}
   \ligature{LIG/}{comma}{ghayn.fina}
   \ligature{LIG/}{period}{ghayn.fina}
\endsetslot
```

这一精妙的有限状态自动机设计，证明了 $\TeX$ 底层虚拟机架构所蕴含的深厚图灵完备潜能。

#### 范例四：窄体字母替换与避头尾碰撞优化

在精致的西文正文字体中，小写字母 `f` 的右侧顶部横勾往往向前大幅伸展。当 `f` 后方紧跟带有高耸重音符号的元音字母时（如法语中的 `fè`, `fê`, `fë`），`f` 的笔尖会硬生生地刺入后续重音符号的轮廓内部，造成极度刺眼的物理重叠墨渍。

通过 `fontinst`，排版师可以引入一个专门设计的“窄头 f”（`f.narrow`），并通过 `LIG/` 预连字机制实现自动上下文避让：

```latex
\setslot{f}
   \ligature{LIG/}{egrave}{f.narrow}
   \ligature{LIG/}{ecircumflex}{f.narrow}
   \ligature{LIG/}{edieresis}{f.narrow}
\endsetslot
```

当 $\TeX$ 排版引擎在文本中扫描到 `f` 且探测到后序紧随带有高重音的 `e` 族字母时，会自动将当前的普通 `f` 悄然无声地替换为向后收敛的 `f.narrow`，从而在保留优雅字距的同时彻底消除墨迹碰撞！

#### 范例五：“让字母忘记自己头上有角”——越南语触角与双重重音处理

越南语的拉丁化正字法（Quốc Ngữ）是全世界重音符号系统最为复杂的语言之一。越南语包含两个独特的带触角（Horn）元音：
- `ơ`（带触角的 o）
- `ư`（带触角的 u）

不仅如此，这两个字母还可以叠加上越南语的五种声调符号（锐音、抑音、问音/跌音、重音），从而形成极为复杂的**双重复合重音**（如 `ở`, `ỡ`, `ứ`, `ừ`, `ự`）。

在绝大多数通用的欧美商业西文字体中，不仅完全没有这些复杂的复合字符，甚至连孤立的触角元音都未曾提供。为了解决这一难题，Haralambous 在 `fontinst` 中设计了著名的“让字母忘记触角”算法：

1. **分离基底与触角**：
   从母体字体中提取基础字母 `o` 与 `u`，并从其他符号库（或通过截取逗号、引号）提取微观触角部件 `horn`；
2. **物理装配单触角元音**：
   通过 `\installglyph` 将触角严丝合缝地焊接在元音字母的右上角，生成基础带角字母；
3. **复合声调装配时的“遗忘”机制**：
   当需要为 `ơ` 进一步叠加声调（如锐音符 `acute`）时，若直接将重音按常规位置居中放置，重音符号必然会与右侧的触角挤压碰撞在一起。
   `fontinst` 的处理策略极其优雅：它让装配引擎在逻辑上“暂时抹掉触角的存在”，重新读取母体字母 `o` 的几何中心坐标，将锐音符号向左微移定位，随后再将缩小版触角精密焊接在最右侧边缘，从而完美实现了多重重音在微观几何层面的和谐共存！

#### 范例六：多重重音多调希腊语（Polytonic Greek）排版

在古典希腊语与拜占庭文献排版中，多调希腊文（Polytonic Greek）呈现出同样令人叹为观止的重音堆叠结构：
- **气符（Breathing Marks）**：粗气符（Spiritus Asper / Rough breathing，带有轻微哈气音）与柔气符（Spiritus Lenis / Smooth breathing）；
- **调符（Accents）**：锐音符（Acute / Oxia）、抑音符（Grave / Varia）、扬抑符（Circumflex / Perispomeni）；
- **下加符（Iota Subscript）**：位于长元音下方微型雕刻的下加字母 $\iota$。

这些符号经常两两、甚至三三组合同时出现在同一个元音字母上方（如 $\tilde{\hat{\alpha}}$, $\tilde{\tilde{\omega}}_\iota$）。

在 `fontinst` 代码中，排版师必须建立庞大的笛卡尔偏移补偿矩阵：

```latex
\installglyph{AlphaRoughAcute}{AlphaRoughAcute}{
   \glyph{Alpha}{1000}
   \movert{\neg{\kerning{rough}{Alpha}}}
   \moveup{\height{Alpha}}
   \glyph{roughacute}{1000}
}
```

通过精准计算字符包围盒的真实高度与负向字距补偿量，使得多重重音能够垂直对齐在大写字母的左上方、或居中悬浮在小写字母的顶端，展现出典雅庄严的希腊古典文献排版风貌。

---

## 4. 迈向 16 位与多向排版的新纪元：$\Omega$（Omega）系统

随着计算机全球化浪潮的席卷，传统 $\TeX$ 系统固有的 8 位体系结构遭遇了不可逾越的物理瓶颈。

### 4.1 传统 $\TeX$ 的 8 位技术瓶颈

1. **单字体 256 字符硬上限**：
   传统 $\TeX$ 的底层度量（TFM）与 DVI 虚拟机将字符槽位严格限制在 8 位无符号整数（0–255）。面对包含数万个汉字、日文假名与韩文谚文的东亚 CJK 大字符集，传统 $\TeX$ 只能采用极其笨拙的子集拆分法（将数万字拆分为数百个 256 字符的微型子字体，再通过外部预处理器注入巨量复杂的字体切换指令）；
2. **数学模式 16 个家族上限**：
   在近代前沿数学、理论物理与数理逻辑的学术论文中，排版所涉及的特殊符号与字符变体动辄数百种，16 个数学家族的硬上限常常导致“数学字体已满（Math font exhausted）”的灾难性编译中断；
3. **单向排版管道的固步自封**：
   传统 $\TeX$ 的断行动力学引擎从底层死死绑定在**自左向右（Left-to-Right, LTR）**的单一水平维度上。当面对阿拉伯文、希伯来文等从右向左（RTL）书写的闪米特语系，或者面对东亚传统的自上而下、从右向左推进（Vertical TTB）的纵排文献时，传统 $\TeX$ 彻底束手无策。

为了从根本上砸碎这些枷锁，Yannis Haralambous（本著作作者）与约翰·普莱斯（John Plaice）于 20 世纪 90 年代初联手启动了宏大的项目——**$\Omega$（Omega）**。

---

### 4.2 $\Omega$ 的架构革新与核心构件

$\Omega$ 绝非对 $\TeX$ 的简单补丁修贴，而是一场触及引擎灵魂深处的彻底重构。

```
[多语言输入文本流 (Unicode / 多字节)]
             │
             ▼
┌──────────────────────────────────────────────┐
│  OTP (Omega Translation Processes) 转换流水线  │
│  - 词法解析 / 语系转写 / 上下文形态自动分析      │
└──────────────────────────────────────────────┘
             │
             ▼
┌──────────────────────────────────────────────┐
│  多向排版引擎 (32 种动态正交书写方向系统)         │
│  - 动态段落构建 / 任意轴向胶水拉伸与折行分析   │
└──────────────────────────────────────────────┘
             │
             ▼
┌──────────────────────────────────────────────┐
│  OFM (Omega Font Metrics, 16位分层度量)        │
│  OVF (Omega Virtual Fonts, 多字节虚拟字体)    │
└──────────────────────────────────────────────┘
             │
             ▼
[扩展 DVI 文件 / 矢量 PostScript / PDF 输出]
```

#### 16 位 / 32 位内部字符原生表示

$\Omega$ 彻底废弃了单字节字符结构，内部全部计算变量统一扩展为 **16 位甚至 32 位整数**，完美兼容 ISO/IEC 10646 与 Unicode 标准。单个字体文件中可容纳的字符数量一举飙升至 65,536 个甚至更高，东亚汉字全集得以在一个统一的字体文件内原生寻址。

#### OFM（Omega Font Metrics）分层度量格式

$\Omega$ 针对性扩展了 TFM 规范，设计了 **OFM（Omega Font Metrics）**格式：
- **Level 0 OFM**：平坦扩展结构，直接将字符槽位扩展至 65,536 个；
- **Level 1 OFM**：引入了先进的**分层表结构（Hierarchical Table Structure）**与稀疏存储矩阵。对于存在大面积空白槽位的超大字库，Level 1 OFM 仅为实际存在的字形分配度量内存，极大地节省了系统资源，并引入了对字形旋转度数与多向包围盒的原生支持。

#### OVF（Omega Virtual Fonts）多字节虚拟字体

配合 OFM，$\Omega$ 升级了虚拟字体标准，推出了 **OVF（Omega Virtual Fonts）**。OVF 能够在多字节编码空间内自由编织复杂的跨字库映射、动态复合笔画焊接与多语言字形回退机制。

---

### 4.3 核心引擎：OTP（Omega Translation Processes）有限状态转换流

$\Omega$ 最具划时代意义的独创设计，是其内置的**有限状态流转换器——OTP（Omega Translation Processes）**。

#### OTP 的核心工作原理

在传统排版系统中，文本流直接流入分词断行引擎。而在 $\Omega$ 体系中，用户可以在排版引擎内部构建一条可自由装卸、级联链接的**动态文本流处理管道**。

OTP 本质上是一门专用于字符串模式匹配与流重写的声明式微型编程语言。排版师编写 `.otp` 源代码脚本，随后使用 $\Omega$ 专属编译器 **`otangle`** 将其编译为高执行效率的二进制转换过滤器 **`.ocf`（Omega Compiled Filter）**。

#### OTP 脚本语法实战

以下是一段真实的 OTP 代码片段，用于处理多音希腊文的自动正字法重写：

```otp
input: 2;
output: 2;

expressions:

`a'  => @"03AC";
`e'  => @"03AD";
`h'  => @"03AE";
`i'  => @"03AF";
`o'  => @"03CC";
`u'  => @"03CD";
`w'  => @"03CE";

"s" { " " | "." | "," | ";" | "!" | "?" } =>
   @"03C2" \2;
```

在这段简洁的规则中：
1. `input: 2; output: 2;` 声明该转换流处理 16 位双字节字符；
2. 规则将 ASCII 转写序列（如小写字母加单引号）自动映射为标准的 Unicode 希腊语带锐音字符码点（如 `@"03AC"` 为 Greek Small Letter Alpha with Tonos）；
3. 规则 `"s" { ... } => @"03C2" \2;` 实现了精巧的希腊文小写西格玛（Sigma）终结态分析：当字母 `s`（常规 $\sigma$）后方紧跟空格或标点符号时，OTP 状态机在流推进中自动将其重写为词尾专用西格玛字形 $\varsigma$（码点 `U+03C2`），并将匹配的标点符号原样送还输出流！

#### 多级挂载点机制

$\Omega$ 允许排版师将 OTP 过滤器挂载在排版流程的不同关键阶段：
- **输入层挂载（Input OTP）**：在字符流进入 $\TeX$ 词法分析器之前执行，常用于不同字符编码体系之间的实时转码（如将 GB2312 实时转码为 Unicode）；
- **排版前挂载（Pre-typesetting OTP）**：在段落折行之前执行，用于处理复杂的连写分析、重音重排与词法注音；
- **排版后挂载（Post-typesetting OTP）**：在页面装配阶段执行，操纵最终输出的字符槽位与标度。

---

### 4.4 32 种动态排版书写方向系统（Multi-directional Typesetting）

$\Omega$ 对世界数字排版最伟大的贡献，莫过于彻底打破了一维水平排版的束缚，建立了一套数学完备的**32 种正交书写方向系统**。

#### 文本方向的四元轴向矩阵

$\Omega$ 将排版方向拆解为三个彼此独立的正交物理维度：
1. **字符行进方向（Direction of Writing）**：沿基线一个字符接着一个字符推进的方向；
2. **行进推进方向（Direction of Line Progression）**：排满一行之后，下一行相对于前一行的推进方向；
3. **字形旋转朝向（Glyph Orientation）**：字符轮廓自身在局部盒子内的直立或旋转角度（$0^\circ, 90^\circ, 180^\circ, 270^\circ$）。

$\Omega$ 定义了四个基础轴向向量：
- **`L`（Left）**：自右向左，向左推进；
- **`R`（Right）**：自左向右，向右推进；
- **`T`（Top）**：自下而上，向上推进；
- **`B`（Bottom）**：自上而下，向下推进。

通过两两组合字符方向与行推进方向，$\Omega$ 构成了八种主书写模式，每种模式均可搭配四种字形朝向，从而构成了完整的 $8 \times 4 = 32$ 种动态书写系统：

| 模式标识 | 字符行进方向 | 行进推进方向 | 典型应用文明与语言排版场景 |
| :---: | :---: | :---: | :--- |
| **`TL`** | 自上而下（Top to Bottom） | 自右向左（Right to Left） | **东亚古典典籍标准纵排**：中文、日文、韩文传统古籍竖排，行自右向左换行推进 |
| **`TR`** | 自上而下（Top to Bottom） | 自左向右（Left to Right） | **蒙古文（Traditional Mongolian）**与满文竖排：字符从上向下流淌，行自左向右换行推进 |
| **`LT`** | 自左向右（Left to Right） | 自上而下（Top to Bottom） | **现代西文与现代汉语横排**：标准的全球现代通用排版模式 |
| **`RT`** | 自右向左（Right to Left） | 自上而下（Top to Bottom） | **阿拉伯文、希伯来文与波斯文横排**：字符自右向左书写，行自上而下顺次换行 |
| **`BL`** | 自下而上（Bottom to Top） | 自右向左（Right to Left） | 历史碑文、特殊工程绘图与古文字学（如部分爱尔兰欧甘文字变体） |
| **`BR`** | 自下而上（Bottom to Top） | 自左向右（Left to Right） | 古代中美洲玛雅碑铭与特殊学术图表标注 |
| **`LB`** | 自左向右（Left to Right） | 自下而上（Bottom to Top） | 极少数古代地中海牛耕式转折书写（Boustrophedon）过渡行 |
| **`RB`** | 自右向左（Right to Left） | 自下而上（Bottom to Top） | 牛耕式回旋排版与反向拓印文献 |

#### 动态局部嵌套机制

在 $\Omega$ 文档中，排版师可以随时随地通过命令切换书写方向：

```latex
\textdir TL
这里是古典中文竖排文献内容...
\textdir RT
هنا نص عربي (这里是一段阿拉伯文横排内容)
\textdir LT
Return to Western horizontal typography.
```

更为震撼的是：**$\Omega$ 的胶水拉伸动力学与 Knuth 折行算法完全适应这 32 种方向**！在 `TL`（竖排）模式下，垂直方向的行间距变成了水平方向的列间距，字符的宽度变成了高度，垂直列满时的换行惩罚与不良度完全沿轴向无缝旋转。不同书写方向的文本盒子可以像乐高积木一样在一张页面中任意互相嵌套，彻底征服了人类历史上所有已知文明的书写体系排版难题。

---

## 5. 结论与未来展望（Conclusions and Glimpses at the Future）

回顾 $\TeX$ 与 $\Omega$ 走过的壮丽历程，我们不仅目睹了一场技术演进的史诗，更见证了数字排版先驱们为了人类文化的完美传承所付出的无穷智慧。

### 历史架构的技术极限与使命完成

高德纳开创的 TFM、DVI 与虚拟字体（VF）体系，在计算机硬件资源极度匮乏的 20 世纪 70 至 80 年代，以极其有限的内存开销与纯整数算术实现了超越时代的绝美排版。

然而，随着印刷出版全面迈入 21 世纪，这一套建立在“外部度量文件、有限状态连字树与后处理映射”之上的古典架构，其历史局限性已无可回避：
1. **与现代字体标准的割裂**：现实工业界已全面普及 OpenType 字体。OpenType 内部自带了功能强大的高级布局表（Advanced Typographic Tables）：用于上下文连字替换的 **`GSUB`** 表、用于高精度字距微调与光学锚点定位的 **`GPOS`** 表、用于基线对齐的 **`BASE`** 表。在传统 $\TeX$ 或 $\Omega$ 中，排版师不得不编写庞杂的脚本将这些早已原生存在于字体内部的智能数据，千方百计地逆向剥离为 TFM/OFM 与虚拟字体，这无疑构成了巨大的工程内耗；
2. **DVI 格式的时代落幕**：在 PDF 成为全球电子文档事实标准的今天，继续坚持输出中间 DVI 字节码再由后处理驱动转换，已难以满足现代透明度混合、色彩管理系统（ICC Profiles）以及交互式超链接的复杂需求。

### 从 $\Omega$ 到 Aleph、XeTeX 与 LuaTeX 的凤凰涅槃

$\Omega$ 系统的诸多超前探索（尤其是多向排版模型与 16 位字符统一支持），为 $\TeX$ 世界的现代化转型播下了最关键的火种：

1. **Aleph（$\aleph$）**：由热罗姆·劳雷（Jérôme Laurens）等人发起的项目，将 $\Omega$ 的多向排版核心与稳定的 `pdftex` 引擎进行深度杂交，消除了早期 $\Omega$ 的诸多底层 Bug，实现了直接生成高质量 PDF 的壮举；
2. **XeTeX**：由乔纳森·丘（Jonathan Kew）开发，采取了“彻底拥抱现代操作系统”的务实哲学。XeTeX 摒弃了传统的 TFM 与外部映射机制，直接调用操作系统底层的字体光栅化渲染引擎（macOS 上的 Core Text 以及跨平台的 FreeType/HarfBuzz），使得排版师可以在 $\LaTeX$ 文档中直接通过字体名称调用系统安装的任意 OpenType/TrueType 字体，并原生激活其内部的全部高级特性；
3. **LuaTeX**：由哈基姆·霍克沃特（Hartmut Henkel）、塔克·霍克斯（Taco Hoekwater）与汉斯·哈根（Hans Hagen）倾力打造的当代终极 $\TeX$ 引擎。LuaTeX 彻底拆除了 $\TeX$ 固步自封的底层藩篱，将一个现代、高效、轻量级的 **Lua 脚本解释器嵌入到了 $\TeX$ 引擎的心脏深处**！在 LuaTeX 中，不仅 TFM 编译、断行计算、数学公式排版的所有内部数据结构全部以 Lua 表的形式暴露给开发者，排版师甚至可以用 Lua 语言重写 $\TeX$ 的整个段落折行算法与 OpenType 字体解析管线。

从高德纳最初在斯坦福大学黑板上写下的盒子与胶水公式，到 Yannis Haralambous 构筑的 $\Omega$ 宏伟多向世界，再到今天由 LuaTeX 与 HarfBuzz 驱动的现代开源排版文明，$\TeX$ 所代表的追求排版至臻至美的精神内核，历经半个世纪的洗礼，不仅未曾褪色，反而如同陈酿的美酒，在人类知识与文明的数字星河中愈发散发出夺目璀璨的光芒！
