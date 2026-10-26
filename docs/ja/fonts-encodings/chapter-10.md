---
title: "第 10 章：字体与万维网页面"
description: "完整无删节中文译本：(X)HTML 与 CSS 字体规范体系、font-size-adjust 与 x-ハイト（x-height）宽高比调节、可下载字体 (@font-face)、网络字体嵌入技术（Bitstream TrueDoc/PFR、微软 WEFT/EOT）、SVG 矢量字体体系与グリフ（Glyph）路径解析。"
---

# 第 10 章：字体与万维网页面
**雅尼斯·哈拉兰博斯（Yannis Haralambous, Ph.D.）著**
*选自『Fonts & Encodings』第 315–366 页*

---

当蒂姆·伯纳斯-李（Tim Berners-Lee）最初定义 HTTP 协议（Hypertext Transfer Protocol）与 HTML 标记系统（Hypertext Markup Language）时，他绝不可能预料到，短短二十年后，全世界都会把“.com”挂在嘴边。万维网（World Wide Web）的爆发性普及，毫无疑问是二十世纪末人类信息科技史上最辉煌的里程碑之一。

HTML 是一种标记系统——一套规定标签结构与语义的规则集合。它脱胎于 SGML（标准通用标记语言，Standard Generalized Markup Language）——这里的“通用”（Generalized）是指它本身不包含固有语义，而只提供一套形式化书写语法。一份 SGML 文档由若干**元素**（Elements）构成。每个元素通常由一对标签表示：起始标签（形如 `<name>`）与闭合标签（形如 `</name>`）。在这对标签之间是元素的内容（Content），其中可以嵌套其他标签或文本。一个元素还可以携带任意数量的元数据，称为**属性**（Attributes）。属性以“键–值”（key–value）对的形式书写在起始标签内部，其数量与排列顺序原则上是任意的。

一份 SGML 文档通常附带一份**文档类型定义**（Document Type Definition, DTD），该定义既可直接嵌入在文档文件内部，也可保存在独立的外部文件中。DTD 包含两类关键数据：其一，是该 SGML 文档中允许出现的所有元素清单，连同它们所能携带的属性以及各属性所允许的数据类型；其二，是规定元素之间嵌套与组合行为的语法规则。例如，我们可以在 DTD 中明确规定：某个特定元素内部只能包含另一特定元素若干次，或者该元素必须为空（Empty Element），或者它可以容纳任意内容等等。

HTML 本质上是一套特定的 SGML DTD，同时也是一套具体的标记语法。这意味着：HTML 文档中可以使用的标签集合是一次性预先严格定义好的；各标签之间的相互嵌套与交互规则也是固定的；并且存在一份详尽的“用户手册”，明确阐述每一个标签在排版呈现与文档语义上的具体含义及适用场景。

然而，与 LATEX 这种每一个命令的底层执行语义都无比清晰严谨的排版语言不同（在 LATEX 中，每个命令都是一道严格的程序指令，我们能够一路追踪其执行流程直至深入 TEX 引擎的底层机理；换言之，LATEX 命令是一种后验定义的“标签”，其语义完全由 TEX 或 $\Omega$ 编译时的实际效果所决定），HTML 为其标签所赋予的往往只是一种极其模糊、近似的语义，甚至放任各大浏览器厂商按照各自的意图进行随意诠释。HTML 在其诞生初期饱受这种围绕标签的“艺术性模糊”（artistic fuzziness）之苦。举例而言，早期的各大主流浏览器厂商都认为自己有权甚至有义务向基础语法系统中随意添加私有专有标签，这导致 HTML 标准频繁经历碎片化混乱更新，且多数更新只是被动迁就那些市场份额最大的浏览器的既成事实。

尽管存在上述缺陷，我们依然必须客观看待历史：在那个 Macintosh、Windows PC 与各类 Unix 工作站之间跨平台通信如同恶梦般的时代，HTML（连同 TEX 以及稍后出现的 Adobe Acrobat PDF）是首个真正实现跨越所有主流操作系统的通用“文档格式”（Document Format）。为了在不彻底撕裂 HTML 标准框架的前提下化解层出不穷的新需求，W3C 与工业界先后在底层标记之上叠加了两层全新的信息维度：其一是 **JavaScript**，这是由网景公司（Netscape）最初开发、随后由 ECMA 组织以 ECMAScript 规范标准化的一种轻量级编程语言，其核心目标是处理 HTML 页面的动态交互逻辑；其二是**级联样式表**（Cascading Style Sheets, CSS，W3C 标准），这是一种专门用于精确解耦并描述 HTML 页面视觉表现与排版外观的样式语言。

这三层信息（HTML 结构、JavaScript 交互、CSS 样式）在同一份文档中彼此协同、和谐共存。不仅如此，得益于被称为**文档对象模型**（Document Object Model, DOM，同为 W3C 标准）的通用对象树接口，JavaScript 脚本能够自如地访问、遍历并动态修改上述三个层面的所有数据节点。

然而，时代的技术演进并未就此止步。若干年前，作为 SGML 的正统现代化继承者，**XML**（可扩展标记语言，Extensible Markup Language，W3C 标准）横空出世并迅速横扫整个计算机软件工业。XML 是对传统 SGML 体系的一种更严格、更干净的裁剪与升华——而在软件工程中，“对人类书写更严格”恰恰意味着“机器解析与自动化处理更加轻量且高效”。事实上，在传统 SGML 时代，全球仅有一两款极其晦涩、庞大且普通开发者根本无法企及的昂贵专用工具才能处理 SGML 文档；而如今，在 XML 领域，工业级、消费级以及开源免费的高性能解析处理工具浩如烟海。通过对 SGML 过于宽泛松散的标记自由度施加适度的语法约束（SGML 与 XML 之间的核心差异实际上可以用五条极其精炼的严格规则予以概括），XML 成功扫清了公众过去对 SGML 所抱有的“迷宫般庞杂”、“笨重迟缓”等负面刻板印象，从而奠定了一套真正能够跨越计算机科学一切应用领域的普适数据交换通用规范。

面对日新月异、蓬勃发展的 XML 生态与日益显露老态的传统 HTML 规范，W3C 最终推出了历史性的解决方案：将 HTML 彻底置于 XML 语法规范下重构，由此诞生了 **XHTML**。此外，XML 还完整继承了 HTML 时代沉淀的成熟技术资产：JavaScript、CSS，并引入了一项 XML 体系所独有的关键技术——**命名空间**（Namespaces）。命名空间提供了一种优雅的机制，使得多套不同的 DTD（或 XML Schema）能够在一个复合文档中无缝共存。换言之，开发者可以创建由来自五湖四海、各自在独立语境中拥有预定义语义的标签所混编而成的多功能文档。例如，在 XHTML 规范本身中，并未定义任何用于排版高等数学公式的标签；然而，W3C 早已制定了专门用于数学公式表达的 XML 标准——**MathML**。通过将一个命名空间指派给“XHTML”，另一个命名空间指派给“MathML”，我们便能在同一份文档中同时使用这两套标准的标签，而绝不会引发任何名称冲突。通过这种方式，任何新兴的 XML 专业子标准都可以立即融入 XHTML 文档体系，只要客户端具备相应的解析渲染模块即可。

在本章中，我们的核心焦点将完全聚焦于：**如何借助现代万维网的技术体系，实现字体的管理、调用与高保真排版呈现**。

毋庸讳言，字体排印历来是万维网设计中最棘手、矛盾最尖锐的核心领域之一。其根本原因极其质朴：**与文档中的普通文本和插图截然不同，字体是数字文档中唯一一种所有权通常并不属于文档创作者本人的核心资源**。之所以不属于文档创作者，是因为字体受知识产权与商业软件许可协议（License）的严格约束，作者绝无权力将其随意向全球网络公开发布与分发。

在万维网页面上渲染排版文本时，传统做法通常只能局限于使用客户端本地操作系统上已预先安装的现有字体；但如此一来，设计者要么必须提前预知各操作系统的字体命名规则，要么只能退而求其次地使用宽泛的泛用通用字体名称（Generic Family Names）。如果网页设计者出于排版美感、企业品牌视觉识别，或是为了正确显示某些尚未被主流操作系统原生支持的罕见民族文字与古代文字而**必须**使用某款特定字体，那么服务器端就必须具备将字体资源安全推送到客户端的技术通道——而这正是无数棘手技术瓶颈与严苛版权法律纠纷的交汇暴风眼。

纵观万维网字体技术的发展脉络，工业界主要从三个截然不同的技术维度切入探索，这也构成了本章的三大核心主体架构：

1. **结构与样式层面的规范标准**：HTML 标准本身提供了一组基础的文本样式标签；而作为排版中枢的 CSS（级联样式表）规范，则建立了一整套精密的字体属性声明与匹配算法体系，用以详尽描述 (X)HTML 页面中所调用的字体特性——无论这些字体是客户端本地预装的，还是通过网络即时下载的可下载字体（Downloadable Fonts，前提是浏览器宿主具备解析与渲染网络字体的能力）。
2. **商业网络字体嵌入工具与运行时插件**：历史上有两家核心技术巨头针对跨平台字体网络动态分发开发了专有插件系统，使浏览器能够通过网络即时获取渲染网页所需的字体资产。其一是 **Bitstream** 公司的 **TrueDoc** 动态字体技术；其二是**微软公司**（Microsoft）基于 OpenType 架构推出的 **Web 字体嵌入技术**（Font Embedding / EOT）。Bitstream 在早期获得了部分浏览器的支持，如 Netscape Communicator 4.x（但后续的 6.x 与 7.x 放弃了支持）、Windows 平台下的 IE 以及 Mac 平台上的 iCab；而微软的 EOT 字体嵌入技术虽然在相当长一段时间内仅被 Windows 平台下的 Internet Explorer 所独占，但其突出优势在于向全球开发者免费开放了极其完善的专用字体打包嵌入工具集。此外，瑞典的一家名为 em2 Solutions 的软件公司还曾推出过名为 GlyphGate 的服务器端动态グリフ（Glyph）网关中间件，该软件能够根据客户端浏览器的实际渲染能力，动态采用多种混合策略交付高精度的字体グリフ（Glyph）服务。
3. **基于矢量图形标准的自包含字体体系**：**SVG**（可伸缩矢量图形，Scalable Vector Graphics，W3C 标准）。作为一种原生的 XML 矢量图形描述语言，SVG 不仅能够通过常规 CSS 机制调用外部字体，更在标准内部直接开辟了 **SVG 字体规范**（SVG Fonts）——允许将每一个字符的贝塞尔轮廓矢量路径直接以 XML 标签的形式完整内嵌在图形文档内部，从而彻底绕过操作系统底层的字体ラスタライズ（Rasterization）引擎，实现真正意义上跨平台绝对一致的矢宽高保真渲染。

---

## 标准 HTML 标签体系

在 CSS 样式表全面普及之前，早期 HTML 规范为了满足文档起草者的基础视觉诉求，陆续引入了一组直接作用于文字外观的物理与逻辑样式标签：

* `<b>` 与 `</b>`：将内部文本以**粗体**（Boldface）呈现。
* `<i>` 与 `</i>`：将内部文本以**斜体**（Italics）呈现。
* `<tt>` 与 `</tt>`：将内部文本以**等宽打字机字体**（Teletype / Monospace）呈现。
* `<em>` 与 `</em>`：逻辑强调（Emphasis），在主流浏览器中默认通常渲染为斜体。
* `<strong>` 与 `</strong>`：强逻辑强调（Strong Emphasis），在主流浏览器中默认通常渲染为粗体。
* `<code>` 与 `</code>`：行内计算机程序源代码片段（Code），默认渲染为等宽字体。
* `<samp>` 与 `</samp>`：计算机程序样本输出（Sample Output），默认渲染为等宽字体。
* `<kbd>` 与 `</kbd>`：用户键盘输入（Keyboard Input），默认渲染为等宽字体。
* `<var>` 与 `</var>`：程序变量或数学变量（Variable），默认渲染为斜体。
* `<dfn>` 与 `</dfn>`：术语定义项（Defining Instance），通常渲染为斜体。
* `<cite>` 与 `</cite>`：作品引用或文献出处（Citation），通常渲染为斜体。
* `<small>` 与 `</small>`：缩小一档字号显示（Smaller Font）。
* `<big>` 与 `</big>`：放大一档字号显示（Bigger Font）。
* `<sub>` 与 `</sub>`：下标（Subscript），字号缩小并向ベースライン（Baseline）下方偏移。
* `<sup>` 与 `</sup>`：上标（Superscript），字号缩小并向ベースライン（Baseline）上方偏移。
* `<font>` 与 `</font>`：在 HTML 3.2 中引入、随后在 HTML 4.01 Strict 及 XHTML 1.0 中被彻底废弃的物理排版标签。在它的短暂生命周期中支持的核心属性如下表所示：

| 属性名称（Attribute） | Netscape 支持版本 | Explorer 支持版本 | 典型语法范例 |
| :--- | :--- | :--- | :--- |
| `color` | ≥ 2 | ≥ 3 | `color="#660099"` |
| `face` | ≥ 3 | ≥ 3 | `face="Helvetica, Arial, sans-serif"` |
| `point-size` | 4 | - | `point-size="12"` |
| `size` | 全部版本 | 全部版本 | `size="-2"` |
| `weight` | 4 | - | `weight="300"` |

随着万维网设计哲学的成熟，依靠 `<font>` 等物理表现标签混杂在文档正文中的做法带来了维护成本失控、代码冗余膨胀以及视觉与结构严重耦合等灾难性后果。W3C 确立了“结构（HTML）与表现（CSS）彻底分离”的黄金设计准则，所有涉及字体族选择、ウェイト（Weight）、グリフ（Glyph）倾斜、大小比例等排版控制权，全面移交由 CSS 规范统一接管。

---

## CSS 字体模块规范（CSS Fonts Module）

从 CSS Level 1 到 CSS Level 2，乃至现代的 CSS Fonts Module，样式表语言建立了一套极其完备且符合传统字体排印学规范的属性体系。

### 指定活动字体的 CSS 核心属性声明

在 CSS 中，用于精确描述文本所应采纳的字体视觉特征的核心属性包括以下七个方面：

#### 1. `font-family`（字体族）
该属性用于指定优先采用的字体名称列表。其声明值可以由两类标识符混合构成：
* **具体字体族名称**（Family Names）：如 `"Times New Roman"`, `"Helvetica"`, `"Palatino Linotype"`, `"Georgia"`。当字体名称中包含空格或特殊标点时，必须使用引号包裹。
* **通用泛用字体族**（Generic Font Families）：这是万维网字体体系最后的“安全气囊”，当用户本地系统不存在前面声明的具体字体时，浏览器将自动映射到操作系统内符合该泛用大类的预设字体上。CSS 规定了五种标准通用族：
  * `serif`：带有衬线装饰的グリフ（Glyph）家族（如 Times, Georgia, Minion, Palatino）。
  * `sans-serif`：无衬线グリフ（Glyph）家族，端点平直，具有极佳的屏幕显示清晰度（如 Arial, Helvetica, Verdana, Trebuchet MS）。
  * `monospace`：每个字符具有绝对相同水平步进宽度的等宽字体家族（如 Courier New, Consolas, Monaco, Lucida Console）。
  * `cursive`：模拟手写笔触、连笔或具有书法装饰倾向的书写体家族（如 Comic Sans MS, Zapf Chancery, Brush Script）。
  * `fantasy`：具有高度艺术夸张、剧场舞台风格或特殊视觉图案的奇幻装饰字体家族（如 Impact, Western）。

#### 2. `font-style`（グリフ（Glyph）样式）
控制字体的倾斜状态：
* `normal`：常规直立正体（Roman / Upright）。
* `italic`：真正由字体设计师专为斜体设计的草体/意大利斜体グリフ（Glyph）（True Italic），其字符骨架与衬线结构往往具有手写体特征。
* `oblique`：机械倾斜体（Slanted / Oblique），通常通过将常规正体在几何上向右剪切倾斜一定角度生成。

#### 3. `font-variant`（グリフ（Glyph）变体）
控制スモールキャピタル（Small Capitals）（Small Capitals）的呈现：
* `normal`：标准常规大小写グリフ（Glyph）。
* `small-caps`：将小写字母置換（Substitution）为高度近似于小写字母 x-ハイト（x-height）（x-height）的スモールキャピタル（Small Capitals）。如果所选字体本身内置了真正的スモールキャピタル（Small Capitals）グリフ（Glyph），浏览器将优先调用专业设计グリフ（Glyph）；若没有，浏览器可能会通过机械缩放大写字母来合成仿真（Synthetic Small Caps）。

#### 4. `font-weight`（ウェイト（Weight） / 笔画粗细）
控制字体笔画的粗细密度。CSS 支持以下枚举值与九档绝对数值体系：
* `normal`：常规ウェイト（Weight），在数值上等价于 `400`。
* `bold`：粗体ウェイト（Weight），在数值上等价于 `700`。
* `bolder`：相对于父元素的计算ウェイト（Weight），递进提升一级粗细。
* `lighter`：相对于父元素的计算ウェイト（Weight），递减降低一级粗细。
* `100`, `200`, `300`, `400`, `500`, `600`, `700`, `800`, `900`：对应从超细（Thin / Ultralight）到超黑（Black / Ultrabold）的精细等级阶梯。

#### 5. `font-stretch`（グリフ（Glyph）伸缩 / 宽高比）
控制字体的水平冷凝与延展程度。支持以下等级：
* `normal`：常规未伸缩グリフ（Glyph）。
* `ultra-condensed`, `extra-condensed`, `condensed`, `semi-condensed`：四档不同程度的グリフ（Glyph）紧缩。
* `semi-expanded`, `expanded`, `extra-expanded`, `ultra-expanded`：四档不同程度的グリフ（Glyph）扩展拉伸。
* `wider`, `narrower`：相对于父元素当前伸缩状态的相对调整值。

#### 6. `font-size`（字号大小）
决定字体的全身身长尺寸。CSS 提供了极度灵活的取值机制：
* **绝对尺寸关键字**（Absolute Size）：`xx-small`, `x-small`, `small`, `medium`, `large`, `x-large`, `xx-large`。W3C 规范建议各相邻级别之间采用约 1.2 至 1.5 倍的缩放比例阶梯，其中 `medium` 通常默认为用户浏览器的基准阅读字号（通常为 16px）。
* **相对尺寸关键字**（Relative Size）：`larger`, `smaller`。相对于继承自父元素的字号，沿绝对尺寸阶梯向上或向下挪动一档。
* **物理与屏幕长度单位**（Length Units）：
  * `pt`（磅/点，1/72 英寸，排版领域的经典绝对单位）。
  * `px`（像素，在屏幕显示中通常指代参考像素，受屏幕分辨率与设备缩放影响）。
  * `em`（相对于当前元素的计算字号大小；1em 即等于当前字体全身尺寸）。
  * `ex`（相对于当前字体的 x-ハイト（x-height）；若字体未包含该度量，通常按 0.5em 估算）。
* **百分比值**（Percentage）：如 `120%`，其行为与 `em` 单位完全类似，精确基于父元素的计算字号进行缩放。

#### 7. `font-size-adjust`（字号长宽比微调）与 x-ハイト（x-height）的几何定律

在屏幕阅读与排版美学中，一个经常被非专业人士忽视的核心秘密在于：**决定一段文本在屏幕上视觉可读性与明晰度的，并非全身字号（font-size）本身，而是其小写字母的实际高度——即所谓的 x-ハイト（x-height）（x-height）**！

不同字体家族虽然在技术上设定了完全相同的全身字号（例如 100 pt），但由于设计风格与历史流派的迥异，其小写字母的实际高度往往天差地别。我们定义字体的**长宽比值**（Aspect Value，记作 $a$）为：
$$a = \frac{	ext{x-height}}{	ext{font-size}}$$

当设计者在 `font-family` 中指定了一串字体回退候选列表时（例如首选字体为 Verdana，备用字体为 Times New Roman），如果用户的系统缺失首选字体，浏览器被迫切换到备选字体。然而，Verdana 拥有巨大的 x-ハイト（x-height）（其 $a \approx 0.58$），而 Times New Roman 的 x-ハイト（x-height）相对狭小（其 $a \approx 0.45$）。一旦发生回退，同样字号下的 Times New Roman 会在视觉上骤然显得极其微小、暗淡且难以辨识，从而彻底破坏原有的排版平衡与可读性。

为了化解这一顽疾，CSS 引入了革命性的 `font-size-adjust` 属性。该属性允许设计者显式声明首选字体的基准长宽比值 $a$。当浏览器由于缺少首选字体而不得不采用某种备选字体时（设该备选字体自身固有的实际长宽比值为 $a'$），浏览器将自动调整实际渲染时的全身字号尺寸（记为调整后字号 $c$），其计算公式为：
$$c = \left(\frac{a}{a'}\right) \times s$$
其中 $s$ 为原始声明的 `font-size`。通过这一动态补偿机制，备选字体在实际屏幕呈现时的小写字母高度将恒定保持在 $c \times a' = a \times s$ 的预设尺寸上，从而奇迹般地维系了跨平台、跨字体回退时的视觉清晰度与阅读舒适感！

::: tip 図 10-1：多种传统经典字体的 x-ハイト（x-height）（短字母高度与全身身长的比率）对比。图中自上而下展示了各主流字体在相同全身尺寸下小写字母实际高度的巨大差异
![図 10-1：多种传统经典字体的 x-ハイト（x-height）（短字母高度与全身身长的比率）对比](/images/fonts-encodings/fig10-1.png)
*図 10-1：多种传统经典字体的 x-ハイト（x-height）（短字母高度与全身身长的比率）对比。图中自上而下展示了各主流字体在相同全身尺寸下小写字母实际高度的巨大差异。*
:::

#### 8. `font` 简写复合属性与系统字体关键字

CSS 提供了强大的单行复合简写属性 `font`，允许按以下严格语法次序一次性声明多个字体属性：
```css
font: [font-style || font-variant || font-weight || font-stretch]? font-size [/ line-height]? font-family;
```
此外，`font` 属性还破例允许使用特定的**系统字体关键字**（System Fonts），以便使 Web 页面中的 UI 元素能够完美融入用户宿主操作系统的原生桌面窗口部件外观：
* `caption`：用于带有标题的控件（如按钮、下拉框）。
* `icon`：用于桌面图标标签。
* `menu`：用于系统下拉菜单。
* `message-box`：用于系统模态对话框与消息提示框。
* `small-caption`：用于小型控件的辅助标头。
* `status-bar`：用于窗口底部系统状态栏。

---

### CSS 字体匹配算法（Font Matching Algorithm）

当一段 HTML 元素被赋予了一套 CSS 字体声明时，浏览器底层绝非盲目尝试，而是必须严格执行一套由 W3C 规范固化的、高度确定的六步匹配算法：

1. **建立本地字体数据库**：用户代理（浏览器）首先遍历当前操作系统及可下载字体资源库，提取所有可用字体的全套排版度量元数据，包括字体族名称、ウェイト（Weight）等级、倾斜状态、伸缩属性以及 Unicode 字符覆盖范围表。
2. **字体族名称匹配**：浏览器沿 `font-family` 声明从左至右依次寻找匹配项。如果在具体名称中未命中，且声明末尾提供了通用泛用族名称（如 `serif`），则从本地数据库中挑选预设的通用族字体替代。
3. **グリフ（Glyph）样式匹配**：优先寻找 `italic` 匹配；若所选字体未提供专用斜体，但在数据库中存在 `oblique`，则采用倾斜体替代；反之亦然。若两者皆无，则由ラスタライズ（Rasterization）引擎对正体施加算法剪切合成仿斜体。
4. **グリフ（Glyph）变体匹配**：优先寻找原生提供スモールキャピタル（Small Capitals）（`small-caps`）的グリフ（Glyph）；若无，则进入仿真合成流程。
5. **ウェイト（Weight）阶梯匹配**：若请求的ウェイト（Weight）数值未完全精准命中，浏览器遵循以下既定启发式阶梯寻找最接近的替代ウェイト（Weight）：
   * 若请求ウェイト（Weight）为 `500`，优先向下寻找 `400`；若无，再向上寻找 `600` 及以上。
   * 若请求ウェイト（Weight）小于 `400`，严格按数值递减方向向下寻找更细的グリフ（Glyph）；若无，再向上寻找。
   * 若请求ウェイト（Weight）大于 `500`，严格按数值递增方向向上寻找更粗的グリフ（Glyph）；若无，再向下寻找。
6. **字号ラスタライズ（Rasterization）缩放**：对于现代可缩放矢量字体（TrueType / OpenType / Type 1），直接按照计算所得的目标字号尺寸缩放贝塞尔轮廓曲线并执行网格对齐微调；对于极少数老旧点阵点阵位图字体，则寻找最接近的预渲染字号点阵，必要时施加二次抽样。

---

### 可下载网络字体规范（@font-face）

早在 CSS Level 2（1998年）规范中，W3C 便极具前瞻性地提出了通过 `@font-face` 规则从网络动态加载专有字体资源的标准化构想。一个标准的 `@font-face` 规则由一系列**字体描述符**（Font Descriptors）构成：

```css
@font-face {
  font-family: "RoboScript";
  src: url("https://example.com/fonts/roboscript.otf") format("opentype"),
       url("https://example.com/fonts/roboscript.woff") format("woff");
  font-weight: normal;
  font-style: normal;
  unicode-range: U+0000-007F, U+0100-017F;
}
```

CSS2 规范中定义的详尽字体描述符清单包括：
* `font-family`：为网络字体在当前样式表作用域内所定义的引用标识符。
* `src`：字体的外部 URI 位置調整（Positioning）符及格式提示（`format(...)`）。
* `font-style`, `font-variant`, `font-weight`, `font-stretch`：定义该网络字体在样式表匹配树中所对应的具体样式槽位。
* `unicode-range`：声明该网络字体中所包含グリフ（Glyph）所覆盖的 Unicode 码点区间。这一机制具有决定性的网络优化意义：浏览器在解析文本时，若发现当前页面完全未出现该区间内的字符，便可智能跳过该大体积字体文件的网络下载！
* `units-per-em`：字体的设计全身身长网格单位（如 1000 或 2048）。
* `panose-1`：该字体的 10 字节 PANOSE 分类编码，用于高级相似性降级替代。
* `stemv`, `stemh`：グリフ（Glyph）主要竖笔划（Vertical Stem）与横笔划（Horizontal Stem）的粗细度量。
* `slope`：斜体グリフ（Glyph）的垂直倾斜偏角角度。
* `cap-height`：大写字母顶部至ベースライン（Baseline）的キャップハイト（Cap Height）。
* `x-height`：小写字母顶部至ベースライン（Baseline）的 x-ハイト（x-height）。
* `ascent`, `descent`：字体的上行部最高升幅与下行部最低降幅。
* `widths`：各グリフ（Glyph）水平步进宽度的紧凑编码表。
* `bbox`：所有グリフ（Glyph）轮廓在设计坐标系下所构成的全局外接边界矩形框（Bounding Box）。
* `definition-src`：指向包含该字体更深层排版元数据的外部定义文件地址。

---

## 网络字体下载与嵌入工具

在万维网字体历史的拓荒阶段，浏览器原生支持直连 TTF/OTF 的时代尚未到来。为了在防范盗版滥用与提供定制排版之间取得商业妥协，两大具有划时代意义的技术解决方案应运而生：

### 1. Bitstream 公司的 TrueDoc 动态字体技术

Bitstream 公司推出的 **TrueDoc** 体系由两个互为表里的核心组件构成：
* **字符轮廓记录器**（Character Shape Recorder, CSR）：安装于服务器端或设计者工作站，负责截获、解析系统中的矢量字体（TrueType 或 PostScript Type 1），将其笔画骨架与轮廓数据经过高强度压缩与加密，封装为极其小巧紧凑的**便携式字体资源**（Portable Font Resource, 扩展名为 `.pfr`）。
* **字符轮廓播放器**（Character Shape Player, CSP）：嵌入在客户端浏览器中的微型渲染引擎。它可以作为原生浏览器模块（如 Netscape 4.x 内置），或作为 ActiveX 控件与 Java Applet 运行于客户端，负责在页面绘制时动态解密 PFR 并在内存中将グリフ（Glyph）ラスタライズ（Rasterization）。

为了方便广大网站设计者制作 PFR 资产，Bitstream 发布了著名的可视化制作套件——**WebFont Wizard**。

::: tip 図 10-2：WebFont Wizard 软件操作界面截图：[a] 字体选择向导；[b] 文字セット子集化选择（英数、西欧拉丁、自定义区间）；[c] 字体グリフ（Glyph）全貌预览表；[d] 目标绑定的万维网 URL 域名安全锁定
![図 10-2：WebFont Wizard 软件操作界面截图](/images/fonts-encodings/fig10-2.png)
*図 10-2：WebFont Wizard 软件操作界面截图：[a] 字体选择向导；[b] 文字セット子集化选择（英数、西欧拉丁、自定义区间）；[c] 字体グリフ（Glyph）全貌预览表；[d] 目标绑定的万维网 URL 域名安全锁定。*
:::

通过 WebFont Wizard，开发者可以对字体实施极其严密的**字符子集化**（Subsetting）——仅提取目标网页所真实用到的字符，从而将数百 KB 甚至数 MB 的字体文件急剧缩减至数 KB 的超微型尺寸。此外，软件强制要求设计者指定该字体允许被调用的 Web 域名地址，任何第三方如果试图跨站盗链该 PFR 文件，播放器在校验当前页面 URL 与授权域名不匹配后将断然拒绝渲染。

::: tip 図 10-6：WebFont Wizard 在服务器端生成的可用字体列表在浏览器中的展示截屏
![図 10-6：WebFont Wizard 在服务器端生成的可用字体列表在浏览器中的展示截屏](/images/fonts-encodings/fig10-6.png)
*図 10-6：WebFont Wizard 在服务器端生成的可用字体列表在浏览器中的展示截屏。*
:::

::: tip 図 10-7：浏览器端展示 Palatino Linotype 字体在 Unicode 基本拉丁字符块（Basic Latin）中的グリフ（Glyph）细节截屏
![図 10-7：浏览器端展示 Palatino Linotype 字体在 Unicode 基本拉丁字符块中的グリフ（Glyph）细节截屏](/images/fonts-encodings/fig10-7.png)
*図 10-7：浏览器端展示 Palatino Linotype 字体在 Unicode 基本拉丁字符块（Basic Latin）中的グリフ（Glyph）细节截屏。*
:::

---

### 2. 微软公司的字体嵌入技术与 WEFT / EOT

微软公司面对网络字体的挑战，采取了深度依托其操作系统技术底蕴的策略：于 1997 年推出了**嵌入式 OpenType**（Embedded OpenType, 扩展名为 `.eot`）格式，并向全球免费推出了**网络嵌入字体工具**（Web Embedding Fonts Tool, **WEFT**）。

EOT 格式本质上是对标准 TrueType / OpenType 字体文件施加深度精简与专有封装的产物：
1. **RootString 根域安全防护**：EOT 在文件头部写入了授权站点的域名字符串列表（RootStrings）。Internet Explorer 在加载 EOT 时，会严格核验发起请求的当前页面 URL 是否属于这些根域或其合法子域。若不匹配，则拒绝装载。这一设计打消了商业字文字体厂商对字体文件被全网无底线随意下载盗用的致命担忧。
2. **微提示与高级グリフ（Glyph）压缩**：WEFT 支持利用 Agfa 公司的 MicroType 压缩算法，对グリフ（Glyph）轮廓数据施加惊人的无损压制，同时完整保留原字体的 TrueType Hinting（ヒンティング（Hinting）），确保在 Windows ClearType 或低分辨率点阵显示下依然保持无可挑剔的清晰刀锋边缘。
3. **严格遵从 OS/2 表的嵌入许可标志**：WEFT 展现出对知识产权的严苛捍卫——在分析字体时，它会严格检查字体内部 `OS/2` 表中的 `fsType` 许可比特位。凡是被标记为“禁止嵌入”（Restricted License Embedding）的商业字体，WEFT 将在界面中直接标记为红色禁用状态，拒绝将其转换为网络字体！

::: tip 図 10-3：WEFT 的系统字体检测与许可数据库界面。清晰列出了系统中各款字体的 Windows 名称、字体族、版本号以及严格的版权许可嵌入级别
![図 10-3：WEFT 的系统字体检测与许可数据库界面](/images/fonts-encodings/fig10-3.png)
*図 10-3：WEFT 的系统字体检测与许可数据库界面。清晰列出了系统中各款字体的 Windows 名称、字体族、版本号以及严格的版权许可嵌入级别。*
:::

WEFT 拥有完备的工作流向导，能够自动化分析目标网站全部 HTML 页面中实际出现的字符频次，自动生成精准剔除冗余グリフ（Glyph）的超轻量级 EOT 字体文件，并自动输出配套的 CSS `@font-face` 声明片段。

::: tip 図 10-4：WEFT 制作 EOT 网络字体的核心步骤界面：[a] 添加目标 Web 页面；[b] 待嵌入字体检测汇总列表；[c] Unicode 字符子集挑选编辑器；[d] 最终生成与 EOT 打包向导
![図 10-4：WEFT 制作 EOT 网络字体的核心步骤界面](/images/fonts-encodings/fig10-4.png)
*図 10-4：WEFT 制作 EOT 网络字体的核心步骤界面：[a] 添加目标 Web 页面；[b] 待嵌入字体检测汇总列表；[c] Unicode 字符子集挑选编辑器；[d] 最终生成与 EOT 打包向导。*
:::

::: tip 図 10-5：WEFT 中生成 EOT 字体与配套 CSS 声明代码的窗口（左侧为待编译字体列表，右侧为自动生成的标准样式代码预览）
![図 10-5：WEFT 中生成 EOT 字体与配套 CSS 声明代码的窗口](/images/fonts-encodings/fig10-5.png)
*図 10-5：WEFT 中生成 EOT 字体与配套 CSS 声明代码的窗口（左侧为待编译字体列表，右侧为自动生成的标准样式代码预览）。*
:::

---

## SVG 格式与原生矢量字体体系

当 W3C 推出 **SVG**（可伸缩矢量图形，Scalable Vector Graphics）时，万维网的视觉表现能力迎来了翻天覆地的技术飞跃。作为一个百分之百基于纯 XML 语法规范的开放矢量图形标准，SVG 彻底打破了位图图像与静态文字之间的传统鸿沟。

### SVG 中的文本与字体选择机制

在 SVG 文档中，文本不再是死板的光栅像素，而是由 `<text>` 元素统领的一等矢量图形对象：
```xml
<svg width="600" height="200" xmlns="http://www.w3.org/2000/svg">
  <text x="50" y="100" 
        font-family="Georgia, serif" 
        font-size="48" 
        fill="#336699" 
        font-style="italic">
    Typography on the Web
  </text>
</svg>
```
SVG 完整继承并支持所有核心 CSS 字体属性。不仅如此，通过 `<tspan>`（实现行内局部的坐标微调与独立样式覆盖）以及 `<textPath>`（允许文本沿着由ベジェ曲線（Bézier Curve）定义的任意数学路径平滑弯曲排列），SVG 赋予了 Web 设计师前所未有的前卫排版自由度。

---

### 原生 SVG 字体架构（SVG Fonts）

然而，SVG 最具开创性乃至令传统排版界为之震撼的特性，莫过于它所建立的**原生 SVG 字体规范**（SVG Fonts）。

在传统计算环境中，文字的渲染高度依赖于底层操作系统复杂的字体子系统（Windows GDI/DirectWrite、Mac Quartz 2D、Linux FreeType）。而在 SVG 规范中，**字体本身可以直接由一套纯 XML 标签完整描述并内嵌于文档之中**！

一个完整的 SVG 字体定义封装在 `<font>` 元素内部，其典型结构如下：

```xml
<font id="MyCustomFont" horiz-adv-x="1000">
  <font-face font-family="MyCustomFont"
             units-per-em="1000"
             ascent="800"
             descent="-200"
             cap-height="700"
             x-height="500" />
  <missing-glyph horiz-adv-x="500" d="M0,0 L500,0 L500,800 L0,800 Z" />
  <glyph unicode="A" horiz-adv-x="650" d="M100,0 L300,700 L350,700 L550,0 ... Z" />
  <hkern u1="A" u2="V" k="-80" />
</font>
```

#### SVG 字体度量与 font-face 属性
在 `<font-face>` 元素中，设计者可以显式精确定义字体的各项排版几何基准度量：

::: tip 図 10-8：SVG font-face 元素的关键几何度量属性示意图。左图展示垂直度量：(1) 上行升幅 ascent；(2) 下行降幅 descent；(3) キャップハイト（Cap Height） cap-height；(4) x-ハイト（x-height） x-height。右图展示基准对齐线：(5) ベースライン（Baseline） baseline；(6) 中心线 center line；(7) 上划线 overline；(8) 删除线 strikethrough；(9) 下划线 underline
![図 10-8：SVG font-face 元素的关键几何度量属性示意图](/images/fonts-encodings/fig10-8.png)
*図 10-8：SVG font-face 元素的关键几何度量属性示意图。左图展示垂直度量：(1) 上行升幅 ascent；(2) 下行降幅 descent；(3) キャップハイト（Cap Height） cap-height；(4) x-ハイト（x-height） x-height。右图展示基准对齐线：(5) ベースライン（Baseline） baseline；(6) 中心线 center line；(7) 上划线 overline；(8) 删除线 strikethrough；(9) 下划线 underline。*
:::

#### 水平与垂直排版原点与进距
SVG 不仅支持西方经典的从左至右水平排版，更原生支持东亚传统的自上而下垂直排版体系：
* 水平排版时，グリフ（Glyph）从**水平原点**（Horizontal Origin，坐标通常为 $(0,0)$）开始绘制，绘制完成后沿 X 轴推进其水平步进宽度（$dx$, 属性为 `horiz-adv-x`）。
* 垂直排版时，グリフ（Glyph）从**垂直原点**（Vertical Origin，由 `vert-origin-x` 与 `vert-origin-y` 指定）开始绘制，绘制完成后沿 Y 轴向下推进其垂直步进高度（$dy$, 属性为 `vert-adv-y`）。

::: tip 図 10-9：水平排版与垂直排版几何原点与前进向量对比示意图：(1) 箭头分别始自“水平原点”（左）与“垂直原点”（右）；(2) 步进位移向量 dx 与 dy
![図 10-9：水平排版与垂直排版几何原点与前进向量对比示意图](/images/fonts-encodings/fig10-9.png)
*図 10-9：水平排版与垂直排版几何原点与前进向量对比示意图：(1) 箭头分别始自“水平原点”（左）与“垂直原点”（右）；(2) 步进位移向量 dx 与 dy。*
:::

---

### 深入剖析：将经典字体グリフ（Glyph）转换为纯 SVG 矢量路径

为了彻底揭开矢量グリフ（Glyph）在 XML 内部的数学运作机理，本书作者以法国当代顶级字体设计大师让·弗朗索瓦·波谢（Jean François Porchez）的名作——《Le Monde Livre》字体中的大写字母 **‘R’** 为例，展开了一场极为详尽的微观解构。

::: tip 図 10-10：来自 Le Monde Livre 字体的字母 ‘R’ 转换为 SVG 贝塞尔矢量轮廓路径的几何剖析。图中清晰标注了字母轮廓每一段三次ベジェ曲線（Bézier Curve）的控制点与起止锚点序列
![図 10-10：来自 Le Monde Livre 字体的字母 ‘R’ 转换为 SVG 贝塞尔矢量轮廓路径的几何剖析](/images/fonts-encodings/fig10-10.png)
*図 10-10：来自 Le Monde Livre 字体的字母 ‘R’ 转换为 SVG 贝塞尔矢量轮廓路径的几何剖析。图中清晰标注了字母轮廓每一段三次ベジェ曲線（Bézier Curve）的控制点与起止锚点序列。*
:::

在 `<glyph>` 元素的 `d` 属性中，グリフ（Glyph）的轮廓通过一套紧凑高效的单字母绘图指令与连续坐标序列加以描述：
* `M x,y`（Move To）：将绘图游标抬起并瞬移至新的起始坐标点 $(x, y)$。
* `L x,y`（Line To）：从当前位置绘制一条至目标点 $(x, y)$ 的直线段。
* `H x`（Horizontal Line To）：绘制水平线至横坐标 $x$。
* `V y`（Vertical Line To）：绘制垂直线至纵坐标 $y$。
* `C x1,y1 x2,y2 x,y`（Cubic Bézier Curve）：以 $(x_1, y_1)$ 与 $(x_2, y_2)$ 为控制点，绘制一条平滑的三次ベジェ曲線（Bézier Curve）至终点 $(x, y)$。
* `Z`（Close Path）：从当前点引出一条直线自动闭合回本轮廓的起始点，形成一个封闭填充环（Contour）。

通过跟随図 10-10 中标注的精细数字坐标轨迹，我们能够清晰看到：
1. 绘图指令首先自大写字母 ‘R’ 主干竖笔的左下角基底开始，利用 `M` 指令确立起点；
2. 随后向上绘制主干竖笔的左侧边缘，平滑过渡至上部衬线（Serif）；
3. 接着借助一连串优美连续的 `C`（三次贝塞尔）曲线绘制出 ‘R’ 上部饱满外凸的圆弧环部（Bowl）；
4. 顺势向下勾勒出该グリフ（Glyph）最为标志性、富于书法张力的优雅右下斜腿（Leg）及其精致的翘尾末端；
5. 最后折返向上闭合外轮廓，并开启第二个内部子路径（Inner Contour）将内腔闭合孔洞（Counter）精确挖空！

这种将高精度曲线完全剥离自专有二进制容器、以明文纯文本形式直接呈现在 Web 标准规范之中的构想，在排版技术史上具有无与伦比的先驱启示意义。尽管 SVG 字体规范由于缺乏专业的全屏栅格微调（Hinting）机制以及解析大体积极端字体时的性能短板，在后来逐渐被更适合全场景的 WOFF/WOFF2（Web Open Font Format）所替代，但它所确立的字符数学矢量化表征逻辑，至今依然是所有现代数字字体与网页图形引擎的灵魂基石。

---

# 结语

回顾万维网早期的字体演进史，我们看到的是一部充满妥协、碰撞与智慧闪光的宏大技术史诗。一方面，网页作者渴望摆脱单调苍白的默认系统字体枷锁，追求具备高度艺术表现力与学术精确度的个性化排版；另一方面，商业字体厂商对版权保护的合法顾虑、操作系统霸主之间的私有标准倾轧，以及带宽极其受限的早期网络基础设施，共同筑起了一道道看似难以逾越的壁垒。

从 Netscape/Bitstream 的 TrueDoc 到微软的 WEFT/EOT，从早期的 CSS 字体描述符探索到自包含的 SVG 原生字体构想，正是这一代先驱者们不懈的技术试错与标准演进，最终为万维网迎向全矢量、全平台无障碍流通的现代通用开放字体时代（WOFF/WOFF2 及现代 CSS Typography），铺平了坚实而宽广的基石！
