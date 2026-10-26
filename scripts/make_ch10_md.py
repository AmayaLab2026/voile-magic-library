---
title: 第十章：Web 网页排版与网络字体技术
description: HTML/CSS 字体模块规范（CSS Fonts 1/2/3）、@font-face 规则与字体匹配算法、动态网络字体历史演进（TrueDoc PFR、WEFT EOT、GlyphGate）与 SVG 矢量字体规范全景技术解析
---

# 第 10 章：Web 网页排版与网络字体技术

*译者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

当蒂姆·伯纳斯-李（Tim Berners-Lee）在 1989 至 1990 年间于欧洲核子研究组织（CERN）发明超文本传输协议（HTTP）与超文本标记语言（HTML）时，他绝不可能预见到二十余年后，“.com”将席卷整个人类文明的每一个角落。万维网（World Wide Web）的爆发式扩张无疑是 20 世纪末人类科技史上的最高光事件之一。

然而，在万维网诞生的前十年里，**网页的排版与字体渲染能力极其简陋贫瘠**。早期互联网主要面向高能物理学家与学术科研人员，网络传输的核心目标是纯学术文本与数据报告的快速共享，视觉美感与高精度印刷级排版从未被纳入核心议程。然而，随着网景浏览器（Netscape Navigator）与微软 Internet Explorer 的激烈商业竞争，数十亿普通用户涌入互联网，数以百万计的商业网站、数字出版物、在线新闻媒体对“在浏览器中呈现与专业印刷纸媒同等优雅的字体”爆发出了前所未有的迫切渴望。

在本章中，我们将系统考察万维网技术演进中字体排版的波澜壮阔历程：
1. **(X)HTML 与级联样式表（CSS）的字体模型**：从简陋的 HTML 物理标签到 CSS Fonts 规范（CSS 1, CSS 2/2.1, CSS 3）、字体匹配算法以及 `@font-face` 跨网络字体装载机制；
2. **早期网络字体下载与嵌入式格式的血泪先驱**：深入剖析 Bitstream 公司的 **TrueDoc（PFR 格式）**、微软公司的 **WEFT 与嵌入式 OpenType（EOT 格式）**，以及 em2 Solutions 公司的 **GlyphGate** 动态字形服务器；
3. **SVG（可缩放矢量图形）与 SVG 字体体系**：从 XML 语法底层到 SVG 字体架构，全面解析 `<font>`、`<font-face>`、`<glyph>`、`<hkern>` 以及字形轮廓路径的几何规范。

---

## 1. (X)HTML、CSS 与字体规范演进

### 1.1 原始 HTML 字体标签的致命困境

在级联样式表（CSS）诞生之前，网页作者控制字体的唯一手段是依靠早期的 HTML 物理标签，其中最具代表性的是网景在 HTML 3.2 时代引入的 `<font>` 标签：
```html
<p>
  <font face="Verdana, Arial, Helvetica" size="3" color="#333333">
    这是一段早期 Web 文本。
  </font>
</p>
```
配合全局的 `<basefont face="..." size="...">`，网页设计者试图以硬编码的方式指定渲染字体。然而，这种早期的原始机制给 Web 生态带来了三项致命的灾难性后果：
1. **语义与表现的彻底混杂**：HTML 应当忠实描述文档的逻辑结构（标题、段落、引用、列表），而 `<font>` 标签将大量纯视觉样式的杂乱代码注入文档正文，导致 HTML 体积膨胀数倍，网页解析极其低效；
2. **本地字体依赖的“囚徒困境”**：`face` 属性所列出的字体名称，必须**完全预先物理安装在终端访问者的本地操作系统中**。如果作者在其豪华的工作站上使用了精美的经典衬线体（如 Garamond 或 Bembo），而访问者的普通家庭电脑上只安装了 Times New Roman，浏览器就会退化为最粗糙的默认字体，导致网页版面瞬间错位崩塌；
3. **印刷度量与像素显示的断层**：HTML 的 `size="1"` 到 `size="7"` 仅为相对标度，完全缺乏排版学中所必需的磅值（pt）、字宽（Set-width）、字重（Weight）以及行距（Leading）的数学定义。

为终结这种混乱局面，万维网联盟（W3C）于 1996 年底正式发布了 CSS 1 规范，随后在 CSS 2 与 CSS 3 中确立了现代 Web 字体的黄金架构。

---

## 2. CSS 字体属性全景规范（CSS Fonts Module）

CSS 将字体属性高度抽象为一组正交、独立的样式描述符（Font Descriptors）。理解每个属性的底层机理与物理单位，是掌握现代 Web 排版的核心前提。

### 2.1 核心字体属性全览

#### 1. `font-family`（字体家族）
`font-family` 允许声明一个按优先级由高到低排列的字体备选列表（Fallback Font List）：
```css
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
```
浏览器在解析该列表时，会逐字检测当前需要渲染的字符码位是否存在于第一个字体中；如果第一个字体缺失该字符的字形（例如用英文字体渲染中文字符），浏览器会自动跳转至下一个字体继续检索，直到找到可用的字形为止。

为了保证在一切极端情况下页面文字均可正常阅读，W3C 规范强制规定了 **5 种通用字体族名（Generic Font Families）**，作为字体列表的最终兜底保底项：
- `serif`（衬线体）：字形笔画末端带有装饰性衬线（如 Times New Roman, Georgia, 宋体）；
- `sans-serif`（无衬线体）：笔画粗细均匀、末端无装饰平直切口（如 Arial, Helvetica, Verdana, 微软雅黑, 黑体）；
- `monospace`（等宽字体）：所有字符具有完全恒定的固定进深宽度，常用于代码展示（如 Courier New, Consolas, Monaco）；
- `cursive`（手写/草书体）：具有连笔手写风格、模仿墨水毛笔的字形（如 Comic Sans MS, Zapf Chancery）；
- `fantasy`（装饰/花体）：艺术化变体字体，常用于海报标题（如 Impact, Papyrus）。

#### 2. `font-style`（字形姿态）
用于控制字体的直立或倾斜表现：
- `normal`：标准直立正体（Roman）；
- `italic`：专门设计的**意大利斜体（True Italic）**。在西文正统字体学中，Italic 不仅具有倾斜度，其字母结构（尤其是小写字母 `a`, `f`, `g`）往往采用类似手写体的连笔草体形态；
- `oblique`：**算法机械倾斜体（Fake / Slanted Italic）**。排版引擎直接通过对直立正体的轮廓实施仿射剪切矩阵变换（Shearing）生成的假斜体。

#### 3. `font-variant`（字母变体）
- `normal`：默认常规字形；
- `small-caps`：**小型大写字母（Small Capitals）**。排版引擎使用与小写字母 x-高度相当的高度来渲染大写字母形态。在专业 OpenType 字体中，真实的 Small Caps 具备加粗的主茎宽度，以避免机械缩小产生笔画过于细弱的光学缺陷。

#### 4. `font-weight`（字重与黑度）
用于控制笔画的视觉粗细。CSS 引入了九级标准化绝对数值体系：
- 离散整百数值：`100`（Thin / Hairline）、`200`（Extra Light）、`300`（Light）、`400`（Normal / Regular）、`500`（Medium）、`600`（Semi Bold）、`700`（Bold）、`800`（Extra Bold）、`900`（Black / Heavy）；
- 相对关键字：`bolder`（在当前继承值基础上向更重一级跃升）与 `lighter`（向更轻一级衰减）。

#### 5. `font-stretch`（字体展宽比例）
定义字符水平方向的压缩或扩展程度：
- `normal`（100% 原始宽度）；
- 紧缩系列：`ultra-condensed` (50%)、`extra-condensed` (62.5%)、`condensed` (75%)、`semi-condensed` (87.5%)；
- 扩展系列：`semi-expanded` (112.5%)、`expanded` (125%)、`extra-expanded` (150%)、`ultra-expanded` (200%)。

#### 6. `font-size`（字号尺寸与度量单位）
- **绝对关键字**：基于七级比例阶梯构建：`xx-small`, `x-small`, `small`, `medium`（基准默认值，通常为 16px）, `large`, `x-large`, `xx-large`；
- **相对关键字**：`smaller`, `larger`；
- **物理与屏幕长度单位**：
  - `px`（CSS 像素）：屏幕显示最稳定的绝对参考单位；
  - `pt`（印刷磅）：$1 \ pt = 1/72 \ in$，常用于打印样式表（Print Stylesheet）；
  - `em`：相对于当前元素的父级 `font-size` 的比例值（如 `1.5em` 表示当前字号的 1.5 倍）；
  - `rem`（Root EM）：相对于文档根节点 `<html>` 的字号比例，避免了多层嵌套时 `em` 的雪崩式乘法缩放；
  - `ex`：相对于当前字体小写字母 `x` 的实际物理高度（x-height）。

---

### 2.2 `font-size-adjust`：x-高度微调与光学可读性自适应

在 Web 字体排版中，最令排版设计师感到困惑的问题之一是：**为什么在相同的 `font-size: 16px` 下，不同字体的肉眼可读性与字形大小感会有天壤之别？**

![不同字体的 x-高度比例对比](/images/fonts-encodings/fig10-1.png)
*图 10-1：数款典型字体的 x-高度比例（小写字母高度与字身字号的比率）对比。自上而下：Times New Roman、Verdana、Georgia 等。*

#### 宽高比值（Aspect Value）的数学定义
这一视觉差异的根源在于**字体的 x-高度（x-height）占总字身尺寸（Font Size）的比例**，CSS 规范将其形式化定义为字体的**宽高比值（Aspect Value，记为 $a$）**：

$$a = \frac{\text{x-height}}{\text{font-size}}$$

- **高 Aspect 值字体**：例如微软专门为低分辨率 CRT/LCD 屏幕设计的 Verdana（$a \approx 0.58$）与 Georgia（$a \approx 0.50$）。其小写字母高大丰满，即使在 10px 极小字号下，字母内部的空腔（Counter）依然清晰可见；
- **低 Aspect 值字体**：例如经典金属活字传统的 Times New Roman（$a \approx 0.46$）。其专为高密度印刷纸张设计，小写字母相对低矮，在低分辨率屏幕上小字号渲染时，笔画往往极易粘连成团。

#### 降级替换时的文本崩塌
假设网页主标题设计为 Verdana 字体，字号设定为 12px。如果访问者的系统中没有 Verdana，浏览器自动降级使用备选的 Times New Roman。由于 Times 的 x-高度仅为 0.46，原本在 Verdana 下清晰可读的正文在切换为 Times 后，小写字母尺寸骤降，文本顿时变得模糊难辨，整体段落灰度严重破坏。

#### 补偿修正公式
为解决这一问题，CSS 引入了 `font-size-adjust` 属性：
```css
p {
  font-family: Verdana, "Times New Roman", serif;
  font-size: 14px;
  font-size-adjust: 0.58; /* 锁定目标 Verdana 的宽高比 */
}
```
当浏览器发生字体降级时，它会读取实际调用的备选字体自身的宽高比 $a'$，并根据以下数学公式**动态调整备选字体的实际计算字号 $c$**：

$$c = \left(\frac{a}{a'}\right) \times s$$

其中 $s$ 为原始声明的 `font-size`。
- 如果备选字体是 Times New Roman（$a' = 0.46$），其实际渲染字号将自动补偿放大为：
  $$c = \left(\frac{0.58}{0.46}\right) \times 14 \approx 1.26 \times 14 \approx 17.65 \ px$$
- 这一放大完美抵消了字体本身小写字母低矮的缺陷，确保无论备选字体如何切换，页面正文小写字母的绝对视觉高度恒定保持在 $14 \times 0.58 = 8.12 \ px$，极大地捍卫了跨平台跨字体的阅读舒适度。

---

### 2.3 复合属性 `font` 的简写语法法则

CSS 提供了 `font` 简写属性，允许在一行内定义全部核心样式：
```css
/* 语法规范模板 */
font: [font-style || font-variant || font-weight || font-stretch]? font-size [/ line-height]? font-family;
```

**书写规则约束**：
1. `font-size` 与 `font-family` 是**绝对强制必填项**，省略任何一个均会导致整个 `font` 声明完全作废；
2. 如果包含 `line-height`（行高），必须紧跟在 `font-size` 之后，并以正斜杠 `/` 分隔（如 `16px/1.5`）；
3. 前置修饰词（`font-style`, `font-variant`, `font-weight`, `font-stretch`）可以以任意顺序书写，未声明的属性将自动恢复为其初始默认值（`normal`）；
4. `font` 属性还允许直接借用操作系统的系统主题字体关键字：`caption`, `icon`, `menu`, `message-box`, `small-caption`, `status-bar`。

---

### 2.4 CSS 字体匹配算法（Font Matching Algorithm）

当浏览器遍历 DOM 树渲染文本时，它会为每一个字符执行一套高度严密的 **6 步字体匹配算法**：

```
+-------------------------------------------------------------+
| Step 1: 构建本地及网络字体描述数据库 (Font Database)           |
| * 收集系统物理字体、本地安装字体及所有已激活的 @font-face 规则 |
+------------------------------|------------------------------+
                               v
+-------------------------------------------------------------+
| Step 2: 逐元素提取计算样式 (Computed Styles)                 |
| * 确定 font-family 列表、stretch, style, weight, size 等绝对值|
+------------------------------|------------------------------+
                               v
+-------------------------------------------------------------+
| Step 3: 按优先级线性匹配 font-family 家族名称                |
| * 遍历家族名；若完全不命中，回退至 generic font family       |
+------------------------------|------------------------------+
                               v
+-------------------------------------------------------------+
| Step 4: 多维属性模糊度量距离逼近 (Descriptive Matching)     |
| * 优先级顺序: 1. font-stretch -> 2. style -> 3. weight      |
+------------------------------|------------------------------+
                               v
+-------------------------------------------------------------+
| Step 5: 逐字符码位覆盖性验证 (Glyph Coverage Check)          |
| * 检查命中的字体实例是否真正包含目标字符的字形 (Glyph)       |
| * 若包含则调用渲染；若缺失则保持当前属性回跳至 Step 3 下一家族 |
+------------------------------|------------------------------+
                               v
+-------------------------------------------------------------+
| Step 6: 终极系统替补兜底 (Ultimate System Fallback)          |
| * 若整个列表穷尽仍无法渲染，调用系统底层“缺失字符方框”符号   |
+-------------------------------------------------------------+
```

1. **构建数据库（Database Construction）**：浏览器扫描当前系统所有的可用物理字体以及当前样式表中所有通过 `@font-face` 声明的网络字体，构建多维字体索引表；
2. **提取计算属性（Property Extraction）**：确定目标元素在继承与级联计算后的绝对字体属性；
3. **家族名顺序遍历（Family Matching）**：取 `font-family` 列表中的下一个候选字名进行匹配；
4. **多属性距离逼近（Attribute Distance Search）**：
   - 首先匹配 `font-stretch`：如果完全匹配则继续；否则在紧缩/扩展方向寻找最接近的变体；
   - 其次匹配 `font-style`：若请求 `italic`，优先寻找真正的意大利体；次优寻找 `oblique`；若仍无则使用 `normal` 正体；
   - 再次匹配 `font-weight`：若请求 `400`（normal），优先寻找 400，次优寻找 500；若请求 `500`，优先寻找 500，次优寻找 400；若请求大于等于 `600`，优先寻找更重字重，若无则寻找更轻字重；若请求小于等于 `300`，优先寻找更轻字重；
5. **字形覆盖性检验（Glyph Availability Verification）**：这是最核心的特性——**字体匹配是以单个字符为粒度进行的**！即使某款字体被成功选中，但如果它不包含当前正在排版的特定古希腊字母或中文汉字，浏览器**绝不会**显示空白或乱码，而是将该单个字符从当前字体中脱出，退回到 `font-family` 列表中的后续字体继续寻找覆盖该码位的可用字形；
6. **最终回退兜底（System Fallback）**：如果整个列表的所有字体均无法覆盖该字符，浏览器调用操作系统最底层的默认后备字体（如 Windows 上的 Arial / SimSun，Mac 上的 Lucida Grande / PingFang），直至显示著名的“缺失字符替换符号”（通常为一个带问号的黑色菱形或十六进制码位线框）。

---

## 3. `@font-face` 规则与早期网络字体技术先驱

为了打破必须依赖用户本地已装字体的桎梏，CSS 2 正式引入了 `@font-face` 规则，允许网页作者指定从远程服务器动态下载字体文件。

### 3.1 `@font-face` 描述符规范

```css
@font-face {
  font-family: "MyCustomFont";
  src: url("https://example.com/fonts/myfont.woff2") format("woff2"),
       url("https://example.com/fonts/myfont.woff") format("woff"),
       url("https://example.com/fonts/myfont.ttf") format("truetype");
  font-weight: bold;
  font-style: normal;
  font-stretch: normal;
  unicode-range: U+0000-00FF, U+0131, U+0152-0153;
}
```

`@font-face` 内部包含一系列专门的描述符：
- `font-family`：定义该网络字体在后续 CSS 样式中被引用的虚拟名称；
- `src`：定义字体的远程网络 URL 地址以及显式格式提示（`format(...)`）；
- `unicode-range`：**按需分片与子集化下载技术基石**。指定本字体文件所涵盖的 Unicode 码位区间（如 `U+0000-00FF` 仅含 ASCII 与西欧基本字符）。如果当前页面未出现该区间内的任何文字，现代浏览器会自动拦截并**完全放弃下载该字体文件**，从而极大节约了移动网络带宽；
- 字体度量微调描述符：`units-per-em`, `ascent`, `descent`, `cap-height`, `x-height`, `bbox`, `stemv`, `stemh`。

然而，在 1990 年代末至 2000 年代初，由于字体厂商（Monotype, Linotype, Adobe）极度恐惧将价值数千美元的商业字体文件（TrueType/OpenType）裸放在 Web 服务器上会被用户右键直接窃取，字体下载技术经历了一场长达十年的残酷阵营割据与格式战争。

---

### 3.2 先驱之一：Bitstream TrueDoc 与 PFR 格式

1990 年代中叶，著名数字字模开发商 Bitstream 开发了历史上首个成熟的 Web 字体嵌入解决方案——**TrueDoc**。

![WebFont Wizard 转换交互界面](/images/fonts-encodings/fig10-2.png)
*图 10-2：Bitstream TrueDoc 的核心工具 WebFont Wizard 软件操作截图。左侧选择系统已安装字体，右侧配置字符子集与目标生成选项。*

#### 核心工作流与架构
TrueDoc 的核心设计目标是**防范盗版并实现极端压缩**。它由两大模块构成：
1. **Character Shape Recorder（CSR，字符形态记录器）**：这是一个运行在网页作者端的预处理工具（如图 10-2 所示的 WebFont Wizard）。CSR 扫描作者本地安装的任意 PostScript Type 1 或 TrueType 字体，并不完整拷贝字体，而是扫描指定的 HTML 页面，抽取页面实际使用到的字符轮廓，并将这些轮廓编译为一种经过高强度压缩与专有加密的紧凑二进制文件——**PFR（Portable Font Resource，便携式字体资源，文件后缀 `.pfr`）**；
2. **Character Shape Player（CSP，字符形态播放器）**：这是一个内嵌在浏览器中的动态栅格化引擎。网景公司在 Netscape Navigator 4.0 中完整原生集成了 CSP 引擎，用户无需额外安装任何插件，即可在 Netscape 中实时渲染 `.pfr` 字体。而在 Internet Explorer 中，Bitstream 则通过提供 ActiveX 控件来实现跨平台兼容。

虽然 TrueDoc 具有极高的字形还原品质与极小的文件体积，但随着网景在浏览器大战中的溃败，以及微软拒绝在 IE 中原生支持 PFR，TrueDoc 最终在 2000 年代初逐渐淡出了历史舞台。

---

### 3.3 先驱之二：微软 WEFT 与嵌入式 OpenType（EOT）

为了在网络字体领域建立绝对霸权并保护字体知识产权，微软于 1997 年推出了自己的专有 Web 字体解决方案：**WEFT（Web Embedding Fonts Tool）** 与 **EOT（Embedded OpenType，文件后缀 `.eot`）**。

![WEFT 字体数据库界面](/images/fonts-encodings/fig10-3.png)
*图 10-3：微软 WEFT 软件的字体数据库视图。清晰列出系统中各款字体的可嵌入权限等级（Embedding Permissions）。*

![WEFT 创建 EOT 字体的分步向导](/images/fonts-encodings/fig10-4.png)
*图 10-4：WEFT 创建 EOT 嵌入字体的交互式向导流程步骤。*

![WEFT 生成 EOT 字体的主控制窗口](/images/fonts-encodings/fig10-5.png)
*图 10-5：WEFT 最终分析 HTML 站点并批量生成 EOT 压缩字体的配置窗口。*

#### EOT 的核心安全机制与压缩技术
EOT 本质上是基于标准 TrueType/OpenType 字体文件经深度定制与加密后的衍生物，它具备三大核心特征：
1. **严格的操作系统级嵌入授权遵从**：如图 10-3 所示，WEFT 在读取系统字体时，会强制读取字体 `OS/2` 表中的 `fsType` 字段（详见本书附录 D）。如果该字段标注为“禁止嵌入”（Restricted License Embedding），WEFT 会严厉拒绝处理该字体；
2. **根域名绑定加密（Root String URL Binding）**：这是微软设计的核心数字版权管理（DRM）机制。作者在通过 WEFT 生成 EOT 时，必须显式绑定目标网站的顶级域名（如 `https://www.mysite.com`）。EOT 文件内部会将该域名散列并加密签名。当浏览器加载 EOT 文件时，会严格比对当前网页的 URL；如果发现字体被其他盗链网站引用，或者用户试图将 EOT 下载到本地双击安装，EOT 会完全锁死拒绝解码！
3. **MicroType Express 专利压缩算法**：微软收购了 Agfa 公司的 MicroType 压缩技术，对 OpenType 的各个二进制数据表（`glyf`, `hmtx` 等）执行高级 LZ 差分熵编码，平均可将字体体积压缩 50% 到 70%。

EOT 曾一度成为 Internet Explorer 4.0 至 IE 8 在整个 Windows 平台上的事实工业标准。然而，由于 EOT 属于微软私有专有格式且深度捆绑了复杂的 DRM，由 Mozilla、Opera 和苹果组成的开源阵营坚决拒绝接纳该标准，导致整个 Web 字体生态陷入了长达数年的撕裂对抗。

---

### 3.4 动态字形服务器先驱：em2 Solutions 的 GlyphGate

对于包含数万个复杂汉字、日文假名及韩文谚文的东亚大字符集，直接在网络上下载一个包含全量字符的完整字体文件（动辄 10MB 至 30MB）在拨号上网时代是绝对不可承受的灾难。

为了解决大字符集在网页上的实时展示，em2 Solutions 公司开发了突破性的 **GlyphGate** 动态字形服务器系统。

![GlyphGate 发现的服务器字体列表](/images/fonts-encodings/fig10-6.png)
*图 10-6：浏览器中显示的 GlyphGate 服务器端实时扫描并注册的高质量可用字体列表。*

![GlyphGate 动态呈现 Palatino Linotype 扩展字符](/images/fonts-encodings/fig10-7.png)
*图 10-7：浏览器窗口截屏：通过 GlyphGate 动态实时截取并渲染的 Palatino Linotype 字体在 Unicode Latin Extended-1 码位区间的精美字形。*

#### 动态按需切片（On-demand Subsetting）
GlyphGate 彻底重构了传统的数据流：
- 网页客户端并不下载静态字体文件，而是安装一个超轻量级的浏览器前端侦听模块；
- 当客户端打开一个包含生僻汉字或复杂古代文字的页面时，前端自动拦截所有未能在本地渲染的字符码位，并向后端的 GlyphGate 服务器发出异步 HTTP 请求；
- 如图 10-6 与 10-7 所示，后端的 GlyphGate 服务器集群即时加载主干大字体，在内存中毫秒级抽取这几个特定字符的矢量轮廓，动态打包生成一份仅包含几十字节的微型临时 PFR 或动态矢量流即时传回浏览器播放。这一架构成为了今天现代 Web 字体动态云托管（如 Google Fonts API 与 Adobe Fonts）的直接灵感始祖。

---

## 4. SVG（可缩放矢量图形）与 SVG 字体体系

在 W3C 的众多图形标准中，**SVG（Scalable Vector Graphics）** 占据着极其特殊的崇高地位。SVG 不仅是一个二维矢量绘图语言，其规范在历史上曾包含了一套**纯粹基于 XML 语法描述的完整数字字体标准——SVG 字体（SVG Fonts）**。

### 4.1 XML 基础概念速览
SVG 建立在标准 XML 规范之上，必须严格遵循 XML 的语法契约：
- **良构性（Well-formedness）**：所有的标签必须闭合（如 `<path ... />`），标签对大小写极度敏感，属性值必须使用单引号或双引号严密包裹；
- **命名空间（Namespaces）**：通过 `xmlns="http://www.w3.org/2000/svg"` 明确界定标签词汇表的权威归属；
- **DOM 树状层次（Document Object Model）**：文档由根节点 `<svg>` 展开，包含坐标系统、图形图元、样式与滤镜定义。

---

### 4.2 独立 SVG 字体规范与元素语法

SVG 字体将字体的全部物理结构（头信息、度量参数、每一个字符的贝塞尔曲线轮廓、甚至字偶距对调整）完全表达为标准的 XML 文本元素。其核心语法架构如下：

```xml
<svg xmlns="http://www.w3.org/2000/svg">
  <defs>
    <font id="MyWebFont" horiz-adv-x="1000">
      <!-- 1. 字体度量与元数据定义 -->
      <font-face 
        font-family="MyWebFont"
        units-per-em="1000"
        panose-1="2 0 5 3 0 0 0 0 3 2"
        ascent="800"
        descent="-200"
        cap-height="700"
        x-height="500"
        bbox="-100 -250 1100 850"
        underline-thickness="50"
        underline-position="-100" />

      <!-- 2. 缺失字符兜底定义 -->
      <missing-glyph horiz-adv-x="500" d="M 50 0 L 450 0 L 450 700 L 50 700 Z" />

      <!-- 3. 具体字符字形轮廓定义 -->
      <glyph unicode="A" glyph-name="A" horiz-adv-x="720"
        d="M 100 0 L 320 650 L 400 650 L 620 0 L 510 0 L 450 180 L 270 180 L 210 0 Z M 360 480 L 290 260 L 430 260 Z" />

      <!-- 4. 水平字偶距对调整 (Kerning) -->
      <hkern u1="A" u2="V" k="-80" />
      <hkern g1="T" g2="y" k="-50" />
    </font>
  </defs>

  <!-- 引用该内联字体进行排版 -->
  <text font-family="MyWebFont" font-size="48" x="50" y="100">AVANT-GARDE</text>
</svg>
```

---

### 4.3 SVG 字体度量属性与物理坐标系

![SVG font-face 核心度量属性图解](/images/fonts-encodings/fig10-8.png)
*图 10-8：`<font-face>` 元素的各种度量属性在排版空间中的相对位置定义。左侧图示：(1) ascent 上伸高、(2) cap-height 大写字高、(3) x-height 小写字高、(4) 基准线 baseline、(5) descent 下延深；右侧图示：总体包围盒 bbox 与 units-per-em 空间范围。*

如图 10-8 所示，SVG 字体通过 `<font-face>` 元素内嵌的属性集完整确立了字体的数学度量空间：
- `units-per-em`（Em 单位精度）：将字身正方形（Em 方格）细分的高精度网格数，通常为 1000（对应 PostScript 规范）或 2048（对应 TrueType 规范）；
- `ascent`：自水平基准线（Baseline，即 $y=0$）向上延伸至字体最高笔画边缘的设计高度；
- `descent`：自基准线向下延伸至字符最低下延笔画（如小写字母 `p`, `g`, `y` 的底部）的距离。**在 SVG 规范中，descent 明确采用负数表示**（如 `-200`）；
- `cap-height`：大写字母正体（如 `H`, `I`）顶端平直笔画相对于基线的垂直高度；
- `x-height`：小写字母正体（如 `x`, `v`, `z`）顶端相对于基线的垂直高度；
- `bbox`：四个数值构成的全局包围盒空间 `[min-x, min-y, max-x, max-y]`，指示整个字库中一切字符轮廓所可能达到的极值边界。

---

### 4.4 水平与纵向书写模式：进深与原点几何

![SVG 水平与垂直排版进深坐标向量](/images/fonts-encodings/fig10-9.png)
*图 10-9：水平与垂直排版下的字形进深几何坐标图示。(1) 箭头起始于水平原点 (horiz-origin-x, horiz-origin-y)，终结于字符右侧进深位置；(2) 箭头起始于垂直原点并向下延伸指示纵向走字进深。*

SVG 极其出色地原生统一了**横排（Horizontal Typesetting）**与**竖排（Vertical Typesetting）**的双重空间度量，如图 10-9 所示：
1. **水平排版度量（Horizontal Metrics）**：
   - 默认原点坐标位于基线上的字符左侧边界点 $(0, 0)$，由全局属性 `horiz-origin-x` 与 `horiz-origin-y` 定义；
   - `horiz-adv-x`：字符排版后的水平前进位移距离（Advance Width）。当前字符绘制完毕后，排版光标自动在水平方向向右平移 `horiz-adv-x` 个设计单位，作为下一个字符的基准原点。
2. **垂直排版度量（Vertical Metrics，东亚传统竖排）**：
   - 垂直走字的原点通常位于字符顶端的几何中心，通过 `vert-origin-x` 与 `vert-origin-y` 显式设置；
   - `vert-adv-y`：字符排版后的垂直向下前进位移量（Vertical Advance Height）。绘制完毕后，光标向下平移该数值，为下一字提供落脚点。

---

### 4.5 字偶距调整（Kerning）：`<hkern>` 与 `<vkern>`

在排版高品质西文字符串（如 `AV`, `Te`, `WA`）时，由于相邻字符形状互补，若仅依赖固定字符宽度会导致字符间产生刺眼的空洞。SVG 字体为此提供了基于 XML 声明的字偶距微调系统：
- `<hkern>`：水平字偶距调整；
- `<vkern>`：垂直字偶距调整。

#### 语法过滤规则：
- `u1` 与 `u2`：以 Unicode 字符形式指定左/右字符（例如 `u1="A" u2="V"`）；
- `g1` 与 `g2`：以字形名称（Glyph Name）指定匹配字符；
- `k`：字偶距增减值（Kerning Value）。该值通常为**负数**，指示第二个字符的原点相对于第一个字符应当向左回拉靠拢的单位距离。

---

### 4.6 深度剖析：法国经典字体 Le Monde Livre 的大写字母 'R'

为了让读者直观感受真实世界中商业级 SVG 字体的代码风貌，我们以让·弗朗索瓦·波尔谢（Jean François Porchez）大师设计的著名经典正文字体 **Le Monde Livre** 中的大写字母 `R` 为例，分析其经由 FontForge 完整转换出的原生 SVG 代码：

![Le Monde Livre 字体中大写字母 R 的矢量轮廓](/images/fonts-encodings/fig10-10.png)
*图 10-10：法国顶级数字字体 Le Monde Livre 中的大写字母 'R' 的贝塞尔曲线轮廓与控制点网格视图，精确映射至下方的 SVG 路径。*

```xml
<glyph unicode="R" glyph-name="R" horiz-adv-x="689"
  d="M 520 -15
     C 496 29 459 76 382 173
     C 305 270 244 350 200 405
     L 200 480
     C 260 485 315 500 365 525
     C 415 550 455 585 480 625
     C 505 665 515 710 515 760
     C 515 825 490 880 440 925
     C 390 970 310 995 200 1000
     L 50 1000
     L 50 0
     L 130 0
     L 130 440
     L 190 440
     C 245 440 310 350 400 230
     C 490 110 540 30 550 0
     L 660 0
     C 630 30 580 80 520 -15 Z
     M 130 520
     L 130 920
     L 190 920
     C 260 920 310 900 340 870
     C 370 840 385 790 385 730
     C 385 660 365 605 325 565
     C 285 525 220 520 130 520 Z" />
```

#### 路径几何与排版学解码：
1. **外轮廓与内空腔（Sub-paths & Counters）**：
   - 第一个以 `M 520 -15` 开始的子路径勾勒出字母 `R` 的巨大外部主轮廓，包含其标志性优雅弯曲的右下右伸腿（Leg / Tail）；
   - 第二个以 `M 130 520` 开始的子路径勾勒出字母 `R` 头部的内部封闭空腔（Counter）；
2. **三次贝塞尔曲线算子（Cubic Bézier, `C`）**：
   - 路径中的 `C` 指令后严格跟随着 6 个坐标参数：第一控制点 $(x_1, y_1)$、第二控制点 $(x_2, y_2)$ 以及目标锚点 $(x, y)$。这精确对应了 PostScript Type 1 字体格式的平滑曲率方程；
3. **闭合多边形算子（`Z`）**：
   - 确保内外路径各自形成水密闭合区域，供渲染引擎应用**非零缠绕数规则（Non-zero Winding Rule）**实施完美的矢量抗锯齿填充。

---

## 5. Web 字体历史博弈的终局：WOFF 与现代排版纪元

纵观 Web 字体的拓荒史：
- Bitstream TrueDoc 带来了最初的防盗版矢量流，但因浏览器分裂而陨落；
- 微软 EOT 拥有极高压缩率与域名绑定，但因其封闭私有而被其他厂商联合抵制；
- SVG 字体虽然完全公开透明，但由于其纯文本 XML 结构对于西文及 CJK 数万字形而言过于冗长、解析开销巨大且完全缺乏 TrueType/OpenType 指令级 Hinting 支持，最终于 2010 年代初被 W3C 移出 Web 标准推荐规范，仅在移动端极个别旧式 Safari 环境中短暂保留。

直到 2009 至 2010 年，Mozilla 基金会核心工程师弗拉基米尔·武基切维奇（Vladimir Vukićević）联合多家字体厂商，正式提出了 **WOFF（Web Open Font Format）**：
- WOFF 放弃了另起炉灶建立新几何格式的幻象，而是回归常识：**直接将工业标准的 SFNT 字体（TrueType 或 OpenType CFF）进行模块化无损解构**；
- 引入经过深度优化的 zlib（以及 WOFF 2.0 中的 Google Brotli）流压缩算法，将各表数据压缩 30% 到 50%；
- 允许在文件头中注入公开的 XML 格式元数据（包含铸模厂版权、设计师签名与许可声明），既不使用侵入式的 DRM 加密，又充分给予了商业字模厂合法的法律申诉证据。

WOFF 与 WOFF2 迅速被全球所有现代浏览器（Chrome, Firefox, Safari, Edge）全票通过接纳，正式终结了长达十五年的 Web 字体格式乱局。今天，借助 `@font-face`、WOFF2 以及 OpenType 1.8 可变字体技术，人类终于在万维网的每一个屏幕像素上，完整实现了几百年来由古登堡、阿尔杜斯、加拉蒙与察普夫在金属活字上所缔造的高雅排版之梦。
"""

with open('scripts/ch10_content.md', 'w', encoding='utf-8') as f:
    f.write(ch10_zh)

print(f"Created scripts/ch10_content.md ({len(ch10_zh)} characters)")
