---
title: 第十章 · Web 网页字体与排版技术
description: 雅尼斯·哈拉兰布斯《Fonts & Encodings》第十章全文深度学术汉译：万维网排版演化史、HTML/CSS 字体模块规范、font-size-adjust 与 x-height 视觉对齐、早期动态网络字体技术（Bitstream TrueDoc、Microsoft WEFT/EOT）、以及 SVG 矢量字体规范。
---

# 第十章 · Web 网页字体与排版技术
### Chapter 10: Fonts and Web Pages
**著者：雅尼斯·哈拉兰布斯 博士（Yannis Haralambous, Ph.D.）**  
*选自《字体与编码》（Fonts & Encodings）原著第 315–366 页*

---

当蒂姆·伯纳斯-李（Tim Berners-Lee）在二十世纪八十年代末构想超文本传输协议（HTTP, Hypertext Transfer Protocol）与超文本标记语言（HTML, Hypertext Markup Language）时，他绝未料到短短二十年后，全世界的文明信息都将依托这套轻量级协议与标签网络流转。万维网的爆发式普及，无疑是二十世纪末全人类信息科学最宏伟的奇迹之一。

然而，在排印学者与图形艺术家的眼中，早期的 Web 却经历了一段近乎野蛮的排版黑暗时代。HTML 最初是作为一种基于 SGML（标准通用标记语言）的**结构化标记系统（Structural Markup System）**诞生的，其初衷是标注文档逻辑角色（如段落 `<p>`、标题 `<h1>`、列表 `<ul>`），刻意抹平物理设备的显示差异。但随着商业世界的涌入，设计师迫切渴望掌控像素级的视觉呈现——字体家族、字号梯队、字距调整与版式色彩。这种结构与样式的撕裂，催生了 HTML 与排版技术的激烈博弈，并最终孕育出层叠样式表（CSS, Cascading Style Sheets）与现代网络字体技术（Web Fonts）。

---

## (X)HTML、CSS 与字体规范的演化

### 1. 早期 HTML 的粗糙尝试与 `<font>` 标签的罪与罚
在 HTML 1.0 至 3.2 时代，W3C 与浏览器厂商（特别是 Netscape 与 Microsoft）为了迎合设计需求，引入了臭名昭著的 `<font>` 标签：
```html
<font face="Verdana, Arial, Helvetica" size="+1" color="#333333">
  Typography on the Web
</font>
```
这种设计带来了灾难性的架构退化：
* **结构与表现极度耦合**：每一个视觉样式的变更都必须直接污染 HTML DOM 节点，导致文档代码极度冗余且无法维护；
* **离散而模糊的字号阶梯**：`size` 属性仅支持 `1` 到 `7` 的相对整数值，无法提供严肃排版所必需的绝对磅值（Points）或精确物理度量；
* **客户端字库依赖困境**：`face` 属性仅仅是向操作系统字体注册表发起的“祈求”；若终端用户的机器上未预装指定的商业字体，浏览器便只能降级回退至粗劣的系统默认字体（如 Times New Roman），导致设计师精雕细琢的版面瞬间坍塌。

### 2. CSS 字体模块的优雅分层
为了将内容语义与视觉呈现彻底解耦，W3C 确立了三层分离架构：**HTML 专精文档结构，JavaScript 专精动态交互，CSS（Cascading Style Sheets）专精排版与视觉样式**。在 CSS 字体规范（CSS Fonts Module）中，排印属性被抽象为一套严谨的继承与层叠系统：

* **`font-family`（字体家族回退机制）**：允许指定优先字体链表，并以泛型通用族（Generic Family：`serif`、`sans-serif`、`monospace`、`cursive`、`fantasy`）作为终极安全兜底；
* **`font-weight`（字重阶梯）**：定义了从 `100`（Thin/Hairline）至 `900`（Black/Heavy）的九级量化刻度；
* **`font-style`（字形姿态）**：严格区分真正的意大利斜体（`italic`，具有独立连笔书写形态的设计）与算法倾斜的伪斜体（`oblique`）；
* **`font-stretch`（字宽伸缩）**：定义从超紧缩（`ultra-condensed`）到超宽展（`ultra-expanded`）的九档宽度变体；
* **`font-size`（字号系统）**：支持绝对度量（`pt`、`px`、`cm`）、相对父级度量（`em`、`%`）以及视口相对度量。

---

## 视觉平衡的核心：字高与 `font-size-adjust`

在跨平台多字体混排与字体回退（Fallback）过程中，网页排印面临着一个致命的视觉痛点：**不同字体在相同标称字号（`font-size`）下，其实际视觉大小与阅读可读性截然不同！**

这一现象的物理根源在于不同西文字体设计的**字心比例（Aspect Value, 即 x 字高与标称字号的比值 $c = \frac{x\text{-height}}{\text{font-size}}$）**存在巨大差异，如 **Figure 10-1** 所示：

![不同西文字体在相同字号下的 x 字高与可读性对比（Figure 10-1）](/images/fonts-encodings/fig10-1-web-x-heights.png)

*图 10-1：六款经典字体在同一 11pt 标称字号下的排印实测（选自原著 Figure 10-1）。自上至下依次为：(1) ITC Berkeley Oldstyle ($c=0.38$)；(2) Times ($c=0.45$)；(3) Minion ($c=0.46$)；(4) Georgia ($c=0.48$)；(5) Myriad ($c=0.48$)；(6) Verdana ($c=0.55$)。各段文本右侧清晰标注了基线（Baseline）、下伸线（Descender line）与 x 字高线（x-height line）。*

### 1. 字心比值（Aspect Value）与阅读可读性
观察图 10-1 可以清楚发现：
* 专门为屏幕低分辨率显示设计的字体（如马修·卡特设计的 **Georgia** 和 **Verdana**），拥有极其宽大的 x 字高（Verdana 的比值高达 $c = 0.55$），因此在小字号下极为清晰醒目；
* 古典书刊排版字体（如 **ITC Berkeley Oldstyle**，$c = 0.38$），其小写字母身材修长，x 字高极低，在屏幕上小字号渲染时会显得孱弱模糊。

如果设计师在样式表中声明：
```css
p {
  font-family: "Berkeley Oldstyle", Verdana, sans-serif;
  font-size: 14px;
}
```
当用户的计算机未安装 Berkeley Oldstyle 时，浏览器回退到 Verdana，整个段落的视觉体量将瞬间暴增近 $45\%$，彻底撑破原有的版面布局！

### 2. `font-size-adjust` 几何归一化算法
为了从根本上消除字体降级回退带来的版面震颤，CSS 规范引入了精妙的 `font-size-adjust` 属性。排印师可以直接指定首选字体的黄金字心比值 $c$：
```css
p {
  font-family: "Berkeley Oldstyle", Verdana, sans-serif;
  font-size: 14px;
  font-size-adjust: 0.38;
}
```
当浏览器被迫降级使用 Verdana 时，它会根据目标字体的固有比值 $c_{\text{actual}} = 0.55$，自动重新计算并缩放实际渲染字号 $z'$：
$$z' = z \times \frac{c_{\text{target}}}{c_{\text{actual}}} = 14\text{px} \times \frac{0.38}{0.55} \approx 9.67\text{px}$$
经过此番动态几何矫正，回退后的 Verdana 小写字母的实际物理 x 字高将与原设计的 Berkeley Oldstyle 严丝合缝完全一致，守住了版面的视觉韵律！

---

## 动态网络字体技术的先驱探索

在当代 WOFF / WOFF2 格式与无限制 `@font-face` 普及之前，业界曾掀起长达十余年的“网络字体格式战争”。核心矛盾在于：**字体设计厂商（Foundries）极度恐惧商业字库文件直接暴露在 Web 上会被任何人随手盗取；而网页开发者与浏览器厂商则迫切需要跨平台的动态下载能力。**

### 1. Bitstream TrueDoc 与 PFR 格式
早在 1996 年，著名的字体铸造厂 Bitstream 便推出了划时代的 **TrueDoc** 体系：
* **核心格式**：便携式字体资源（PFR, Portable Font Resource）；
* **字形捕捉器（Character Shape Recorder, CSR）**：在 Web 开发者机器上运行，从系统安装的 TrueType 或 PostScript Type 1 字体中提取矢量字形曲线，并将其压缩为私有的微型 PFR 轮廓格式；
* **字形渲染器（Character Shape Player, CSP）**：嵌入至浏览器内部（曾被 Netscape Communicator 4.0 原生集成）。当网页加载时，动态下载 `.pfr` 文件并在客户端瞬时绘制高质量字形；
* **防盗链安全机制**：PFR 首次支持将字体绑定到特定的域名（Domain Locking），如果其他网站试图盗用该 `.pfr` 链接，字形播放器将直接拒绝渲染！

### 2. 微软 WEFT 与 EOT（Embedded OpenType）
作为对 TrueDoc 的正面反击，微软在 Internet Explorer 4.0 中推出了 **WEFT（Web Embedding Fonts Tool）** 实用工具与 **EOT（Embedded OpenType, `.eot`）** 格式：
* **智能子集化（Subsetting）**：WEFT 能够深度分析网站的所有 HTML 页面，统计出全站实际用到的汉字或特殊标点，从庞大的数兆字节中文字库中剥离出一个仅数十 KB 的微型子集；
* **微型压缩引擎（MicroType Express）**：采用高效的有损/无损自适应几何压缩算法，将 TrueType 表格压缩至原体积的 $30\%$ 以下；
* **根域名加密绑定（Root-String Binding）**：EOT 规范在文件头部严密嵌入了授权网站的完整 URL 签名，若签名与当前加载上下文不符，Windows GDI 引擎将禁止激活该字体。

尽管 TrueDoc 与 EOT 拥有非凡的前瞻性，但由于厂商之间的专利壁垒与浏览器大战（Netscape 押注 TrueDoc，IE 押注 EOT，互不兼容），早期动态网络字体最终遗憾沉沦，直至 W3C 牵头确立开放通用的 WOFF 工业标准。

---

## SVG 字体与矢量排印新范式

在万维网向多媒体与响应式矢量图形跨越的进程中，W3C 制定的 **SVG（Scalable Vector Graphics, 可缩放矢量图形）** 规范为字体排印开辟了一条完全基于 XML 文本描述的全新道路。

### 1. SVG 文本与排印容器
在 SVG 视口中，文本是原生的一等公民矢量对象：
```xml
<svg width="600" height="200" xmlns="http://www.w3.org/2000/svg">
  <text x="50" y="100" font-family="Georgia" font-size="48" fill="#8b0000" letter-spacing="2">
    Voile <tspan fill="#4169e1" font-weight="bold">Magic</tspan> Library
  </text>
</svg>
```
SVG 具备普通 HTML 无法比拟的高级排印控制特性：
* **`text-anchor`**：原生支持 `start`、`middle`、`end` 的几何锚点对齐；
* **`<textPath>`**：允许文本沿着任意复杂的三次贝塞尔样条路径流动弯曲；
* **字形级精确定位**：通过 `dx` 与 `dy` 属性数组，可以对单词内的每一个字符逐一实施二维微移。

### 2. 纯 XML 描述的 SVG Font 规范
在 SVG 1.1 规范中，W3C 甚至直接在 XML 内部定义了完整的字体格式——**SVG Fonts**：
```xml
<svg xmlns="http://www.w3.org/2000/svg">
  <defs>
    <font id="VoileFont" horiz-adv-x="1000">
      <font-face font-family="Voile" units-per-em="1000" ascent="800" descent="-200" />
      <missing-glyph horiz-adv-x="500" d="M0,0 h500 v800 h-500 z" />
      
      <!-- 字符 'A' 的矢量路径定义 -->
      <glyph unicode="A" horiz-adv-x="680" 
             d="M 50,0 L 290,700 L 390,700 L 630,0 L 510,0 L 450,180 L 230,180 L 170,0 Z 
                M 270,300 L 410,300 L 340,510 Z" />
      
      <!-- 字母间字距微调（Kerning Pair） -->
      <hkern u1="A" u2="V" k="-80" />
    </font>
  </defs>
</svg>
```
在 SVG Font 中：
* 每一个字形（`<glyph>`）的轮廓完全由标准的 SVG 路径数据命令（`d="..."`，包含 `M` 移动、`L` 连线、`C` 三次贝塞尔、`Q` 二次样条）直接绘制；
* 原生支持 `<hkern>` 与 `<vkern>` 水平与垂直字距微调对；
* 配合 `<altGlyph>` 标签，排印师甚至可以在特定的语境下指定替换为花体字（Swash）或上下文变体！

尽管 SVG Fonts 由于缺乏类似 TrueType 的字节码 Hinting 渲染优化机制而在主流桌面浏览器中逐渐退役，但它开创的“将字体深度集成进通用图形标记语言”的思想，彻底启发了当代 OpenType-SVG（彩色与表情符号字体）标准的诞生。
