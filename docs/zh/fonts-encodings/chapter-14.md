---
title: "第 14 章：高级排版体系：OpenType 与 AAT 特性深度实战"
description: "完整无删节 1:1 学术全译：复杂文字排版困境（天城文连字拆分与元音前置重排、阿拉伯文连笔形态与双向排印、西文历史连字与小型大写字母）；OpenType 架构全景（GSUB 替换表 1–8 类、GPOS 定位表 1–6 类、标准特性标签 Feature Tags）；FontLab 中编写 Adobe 特性定义语言（AFDKO .fea 语法、上下文替换规则、嵌套查找表 Lookup）；微软 VOLT 可视化工程工作流（项目架构、替换与定位视窗、Proofing 实时字形追踪排印测试）；FontForge 中的高级排版管理（锚点类、链式上下文规则）；苹果高级排版（AAT）有限状态自动机（FSM、morx 表、状态转移矩阵、标记与堆栈动作实战）。"
---

# 第 14 章：高级排版体系：OpenType 与 AAT 特性深度实战

**雅尼斯·哈拉兰博斯（Yannis Haralambous, Ph.D.）著**  
*选自《Fonts & Encodings》第 549–598 页*

*译者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

# 导言：复杂排版的世纪挑战

本章的标题直指数字字体技术皇冠上的明珠——**OpenType** 与苹果 **AAT**（Apple Advanced Typography）的“**高级排版特性**”（Advanced Typographic Features）。

在活字印刷与桌面出版的漫长岁月中，排版系统长期被“一个字符对应一个固定字形模具”的简单思维所禁锢。然而，人类文明孕育的文字系统何其广博璀璨，这种单调的机械映射在面对复杂文字系统（Complex Scripts）时迅速陷入破产：

1. **印度次大陆文字（以天城文 Devanagari 为代表）**：在梵文、印地文等语言中，辅音簇之间会融合成结构繁复的组合连字（Conjuncts）；更为奇特的是，短元音符号 “i-matra”（ि）在逻辑编码中输入在辅音之后，但在物理印刷时却必须在视觉上发生“逆序飞跃”，**整齐地跨越前方整个辅音簇并悬挂在词头最左侧！**
2. **阿拉伯文字系**：阿拉伯文是天生的草书连笔文字。每一个字母在词首（Initial）、词中（Medial）、词尾（Final）以及孤立状态（Isolated）下必须呈现截然不同的字形骨架，同时上下变音符号（Tashkeel）必须依据不同字高的字母动态漂移对齐。
3. **希伯来文与东南亚文字**：希伯来文的元音点（Niqqud）与诵读吟诵标记必须精密叠落而不发生墨迹重叠；泰文、缅甸文更具有多层垂直堆叠规则。
4. **西文高阶典籍排版**：哪怕在看似规则的拉丁字母体系中，殿堂级的人文排版同样要求极其精妙的动态变换：自动识别并替换标准连字（如 $\text{fi}, \text{fl}, \text{ffi}, \text{ffl}$）、历史罕见连字（如 $\text{ct}, \text{st}, \text{long-s}$）、真小型大写字母（Small Capitals）、上标与下标数字、比例数字（Proportional Figures）、无衬线表格式等宽数字（Tabular Figures）、旧式复古高低不齐的吊脚数字（Old-Style Figures）以及真分数（Fractions）。

为了在统一的数字字体文件内部完美承载上述复杂的排印智能，现代排版学孕育出了两大工程奇迹：由微软与 Adobe 联合主导的 **OpenType 布局架构**，以及苹果公司独辟蹊径的 **AAT 有限状态自动机架构**。

---

# OpenType 布局架构的宏观全景

OpenType 的高级排版能力主要建立在两大基石表格之上：**GSUB**（Glyph Substitution Table，字形替换表）与 **GPOS**（Glyph Positioning Table，字形定位表）。

## 1. GSUB：字形替换的八大查找类型（Lookups）

字形替换表的使命，是根据上下文语义规则，将文本流中的一个或多个字形代码（Glyph IDs）动态替换为字模库中的另外一个或多个目标字形：

* **单字形替换（Single Substitution, Lookup Type 1）**：一对一替换。例如将普通小写字母 ‘a’ 替换为小型大写字母 ‘ᴀ’（`smcp` 特性），或将平直括号替换为大写字母专用的高位括号。
* **多字形替换（Multiple Substitution, Lookup Type 2）**：一对多分解。例如将组合印地文连字拆解为其各自的原始辅音构件，或将单个特殊连字拆分成基础字母序列。
* **择一字形替换（Alternate Substitution, Lookup Type 3）**：一对多交互选择。为同一字符提供多种可选的艺术异体花体（如由设计者精心绘制的多种花体大写字母 Swash），供排版软件弹出视窗由用户手工点选。
* **连字替换（Ligature Substitution, Lookup Type 4）**：多对一融合。将连续输入的一串字符序列合体为一个独一无二的专用连字字模（最经典如 $f + i \to \text{fi}$，$f + f + l \to \text{ffl}$）。
* **上下文替换（Contextual Substitution, Lookup Type 5）**：在特定的前后文字符环绕语境下触发替换。例如：当且仅当小写字母 ‘s’ 出现在词尾且前接元音时，将其替换为终端优雅卷曲形式。
* **链式上下文替换（Chained Contextual Substitution, Lookup Type 6）**：这是排印智能的王牌工具！它将排印环境解构为三大独立区间：**前瞻回溯区（Backtrack）**、**当前匹配区（Input）**与**后顾前瞻区（Lookahead）**。只有当这三个区间的字符同时严丝合缝地命中规则时，才对当前匹配区内的目标字形施加嵌套替换！
* **扩展字形替换（Extension Substitution, Lookup Type 7）**：突破 16 位二进制偏移量（64 KB 限制）的超长距离跳转机制。
* **反向链式上下文单替换（Reverse Chaining Contextual Single Substitution, Lookup Type 8）**：以从右向左的逆序方向评估上下文并进行单字替换，专为某些从中东到南亚的复杂从右至左文字流设计。

## 2. GPOS：字形定位的六大核心查找类型

字形定位表并不改变字形本身的物理 ID，而是通过精确操纵字形的几何坐标偏移量（$X$ 轴位移、$Y$ 轴位移、水平步进增量 $\Delta X$、垂直步进增量 $\Delta Y$），在二维平面上对文字进行纳米级的微调定位：

* **单字形位置微调（Single Adjustment, Lookup Type 1）**：例如当输入全大写文本时，自动将句号、连字符、圆括号整体向上抬升数个像素，使其在视觉上与大写字高居中对齐。
* **字距调整对（Pair Adjustment / Kerning, Lookup Type 2）**：这就是现代排印中不可或缺的 Kerning！消除如 “AV”、“To”、“WA” 等特定字对之间的刺眼空隙。
* **草书连笔锚点定位（Cursive Attachment, Lookup Type 3）**：在每个连续草书字形的“入口点”（Entry Anchor）与“出口点”（Exit Anchor）之间建立刚性吸附，确保手写连笔文本无论如何变形，笔画连接处永远天衣无缝！
* **标点/重音基字符吸附（Mark-to-Base Attachment, Lookup Type 4）**：在基字符（Base Glyph）与变音符（Mark）上分别预设坐标锚点，排版引擎在运行时将两者的锚点强行对齐重合。这一机制彻底解放了字体库——设计者无需再为带有锐音符、钝音符、抑扬符的每个字母单独绘制数百个预制字模，只需绘制一套基字符和一套重音标点，即可通过锚点在屏幕上即时拼合！
* **连字标点吸附（Mark-to-Ligature Attachment, Lookup Type 5）**：将重音符号精密吸附在连字内部的各个独立构件上方。
* **标点叠落吸附（Mark-to-Mark Attachment, Lookup Type 6）**：用于多重变音符叠加（如在阿拉伯文或越南文中，一个元音字母上方同时叠加抑扬符和声调符），后一个标点直接以底层标点的顶部锚点为基准向上吸附。

## 3. 标准四字符特性标签（Feature Tags）

在 OpenType 架构中，所有上述底层 Lookups 必须被封装在具有特定语义的 4 字符标签（Feature Tag）之内，操作系统与排版软件（如 InDesign、Word、Web 浏览器）正是通过识别这些标签来向用户呈现功能开关：

* `liga`（Standard Ligatures，默认开启）：通用标准连字（$\text{fi}, \text{fl}$）；
* `dlig`（Discretionary Ligatures）：艺术性可选连字（如 $\text{ct}, \text{st}$）；
* `smcp`（Small Capitals from Lowercase）：将小写字母转换为真小型大写字母；
* `c2sc`（Small Capitals from Capitals）：将大写字母转换为小型大写字母；
* `lnum`（Lining Figures）：与大写字母等高的全齐平大写数字；
* `onum`（Oldstyle Figures）：参差不齐的复古高低吊脚数字；
* `pnum` 与 `tnum`：比例间隔数字与表格等宽对齐数字；
* `frac`（Fractions）：斜线分数自动合体（如 $1/2 \to \frac{1}{2}$）；
* `hist`（Historical Forms）：历史变体字形（如长 s，$\text{ſ}$）；
* `salt`（Stylistic Alternates）：风格备用字形；
* `swsh`（Swash）：华丽花体字端；
* `init`, `medi`, `fina`, `isol`：阿拉伯文的词首、词中、词尾与独立字形形态；
* `size`（Optical Size）：字体的光学推荐字号区间与基准设计字号元数据。

---

# 在 FontLab 中掌控 OpenType 表与 AFDKO 语法

FontLab 深度整合了 Adobe 的 **AFDKO**（Adobe Font Development Kit for OpenType）编译器，采用行业通用的**特性定义语言**（**Feature Definition Language**, 扩展名通常为 `.fea`）。

在 FontLab 的 OpenType 面板中（`Window > Panels > OpenType`，图 14-1 与 14-2），设计者可以用极其优雅的人类可读代码来编写整套排印规则：

::: tip 图 14-1：FontLab 中编写与调试 OpenType 特性定义语言（AFDKO .fea 语法）的主编辑视窗
![图 14-1：FontLab 中编写与调试 OpenType 特性定义语言的主编辑视窗](/images/fonts-encodings/fig14-1.png)
*图 14-1：FontLab 中编写与调试 OpenType 特性定义语言的主编辑视窗。*
:::

::: tip 图 14-2：FontLab 中 OpenType 特性编译成功与错误语法诊断面板
![图 14-2：FontLab 中 OpenType 特性编译成功与错误语法诊断面板](/images/fonts-encodings/fig14-2.png)
*图 14-2：FontLab 中 OpenType 特性编译成功与错误语法诊断面板。*
:::

## 1. 核心语法范例与机制

### 字符类（Classes）的定义
使用 `@` 符号声明字形集合，极大地精简后续规则的书写：
```fea
@UPPERCASE = [A-Z];
@FIGURES_LINING = [zero one two three four five six seven eight nine];
@FIGURES_OLDSTYLE = [zero.oldstyle one.oldstyle two.oldstyle three.oldstyle four.oldstyle five.oldstyle six.oldstyle seven.oldstyle eight.oldstyle nine.oldstyle];
```

### 语言系统声明（Languagesystem）
通知排版引擎该特性适用于哪些文字与语言：
```fea
languagesystem DFLT dflt;
languagesystem latn DFLT;
languagesystem latn DEU; /* 德语体系 */
```

### 基础连字与小型大写字母规则
```fea
feature liga {
    sub f i by f_i;
    sub f l by f_l;
    sub f f i by f_f_i;
} liga;

feature smcp {
    sub [a-z] by [a.sc-z.sc];
} smcp;
```

### 上下文与链式排除规则（Contextual & Ignore Rules）
在特性定义语言中，**单引号** `'` 标记了当前规则中实际被执行替换的目标字符！
例如，在排版中我们要将孤立出现的三个字母 “T E X” 自动合体为专有的 $\text{\TeX}$ 标识，但若该词嵌入在更长的单词（如 “TEXAS”）中时则必须严禁合体：
```fea
feature dlig {
    ignore sub [A-Z Eacute] T' E' X' ;
    ignore sub T' E' X' [A-Z Eacute] ;
    sub T' E' X' by T_e_X;
} dlig;
```

### GPOS 位置微调与锚点语法
```fea
# 调整特定字对的 Kerning
pos T -50;
pos A V -100;

# 标点吸附锚点语法（MarkToBase）
markClass [acute] <anchor 150 450> @TOP_MARKS;
pos base [e] <anchor 250 450> mark @TOP_MARKS;
```

在 FontLab 的预览面板中（Preview Panel，图 14-5），设计者可以勾选不同的特性复选框，输入多行长文本，实时测试 OpenType 特性在屏幕上的展开效果。

::: tip 图 14-5：FontLab 的预览面板（Preview Panel）。支持在不同字号与行距下实时测试与校验 OpenType 特性的编译渲染表现
![图 14-5：FontLab 的预览面板](/images/fonts-encodings/fig14-5.png)
*图 14-5：FontLab 的预览面板。支持在不同字号与行距下实时测试与校验 OpenType 特性的编译渲染表现。*
:::

---

# 微软 Visual OpenType Layout Tool（VOLT）工业级实战

如果说 FontLab 代表了程序员所钟爱的纯文本代码编译流，那么微软官方出品的 **VOLT**（**Visual OpenType Layout Tool**）则是大型商业铸字工坊进行极其复杂的阿拉伯文、天城文与东亚字体工程的绝对权威标准。

VOLT 的架构完全摒弃了手写代码，其核心采用高度严密的**图形数据库驱动模式**：

::: tip 图 14-6：微软 VOLT（Visual OpenType Layout Tool）项目全局管理主视窗。左侧展示脚本与语言分层树，右侧列出全部独立的 Lookups 查找表集合
![图 14-6：微软 VOLT 项目全局管理主视窗](/images/fonts-encodings/fig14-6.png)
*图 14-6：微软 VOLT 项目全局管理主视窗。左侧展示脚本与语言分层树，右侧列出全部独立的 Lookups 查找表集合。*
:::

## 1. VOLT 的核心工作流：

* **项目视窗（Project Window，图 14-6）**：以严格的层次结构组织脚本（Scripts）、语言系统（Languages）、特性（Features）以及全局独立的 Lookups 库。
* **字形替换视窗（Substitution Window，图 14-7）**：采用极其直观的视觉表格：
  * **To**（原始字形）与 **By**（替换字形）；
  * **Context**（前置语境）与 **Lookahead**（后置语境）；
  * 勾选 `Reverse Chaining` 可直接一键将查找表编译为罕见的 Lookup Type 8！
* **位置与锚点视窗（Positioning Window，图 14-8）**：设计师可以直接在字形画布上，用鼠标直观地拖拽基字符锚点与标点符号锚点，在极度放大的视窗中实时对拍两者的重合位置，彻底告别盲猜坐标数字的痛苦。
* **打样测试台（Proofing Window，图 14-9）**：VOLT 的测试台堪称排印侦探：当输入一串复杂的天城文或阿拉伯文文本时，测试台不仅呈现最终渲染图像，更能**逐帧回放每一个 Lookup 的执行次序、匹配上下文以及被成功替换或定位的字形步骤轨迹！**

::: tip 图 14-7：VOLT 中的字形替换编辑视窗。展示了前置语境、匹配字形类与目标替换类的图形化配置界面
![图 14-7：VOLT 中的字形替换编辑视窗](/images/fonts-encodings/fig14-7.png)
*图 14-7：VOLT 中的字形替换编辑视窗。展示了前置语境、匹配字形类与目标替换类的图形化配置界面。*
:::

::: tip 图 14-8：VOLT 中的交互式标点吸附（Mark-to-Base）锚点直观配置视窗
![图 14-8：VOLT 中的交互式标点吸附锚点直观配置视窗](/images/fonts-encodings/fig14-8.png)
*图 14-8：VOLT 中的交互式标点吸附锚点直观配置视窗。*
:::

::: tip 图 14-9：VOLT 强大的交互式排印打样测试台（Proofing Window）。支持单步单帧追踪复杂排印特性的命中与执行链条
![图 14-9：VOLT 强大的交互式排印打样测试台](/images/fonts-encodings/fig14-9.png)
*图 14-9：VOLT 强大的交互式排印打样测试台。支持单步单帧追踪复杂排印特性的命中与执行链条。*
:::

---

# 在 FontForge 中管理高级排版特性

作为开源旗舰，FontForge 同样提供了极其完整且兼顾图形与底层数据结构的 OpenType 表管理面板（`Element > Font Info > Lookups`）：

* **锚点类系统（Anchor Classes，图 14-10）**：在单个字形内部明确区隔 `Base`、`Mark`、`Ligature` 与 `Cursive` 锚点；
* **单向与成对位置微调（图 14-12）**：提供类似电子表格的 Kerning 表格界面；
* **链式上下文替换配置向导（Chained Contextual Wizard，图 14-13 [a]–[d]）**：将极其复杂的链式查找表拆解为四步引导向导：
  1. 设定前瞻回溯字形类；
  2. 设定当前匹配目标类；
  3. 设定后顾前瞻字形类；
  4. 绑定被调用的嵌套底层 Lookup 规则。

::: tip 图 14-10：FontForge 中的锚点类（Anchor Classes）配置面板。直观定义基字符与变音符号的物理吸附锚点
![图 14-10：FontForge 中的锚点类配置面板](/images/fonts-encodings/fig14-10.png)
*图 14-10：FontForge 中的锚点类配置面板。直观定义基字符与变音符号的物理吸附锚点。*
:::

::: tip 图 14-11：FontForge 中的单字替换配置面板（左：字形标签页；右：新替换规则创建对话框）
![图 14-11：FontForge 中的单字替换配置面板](/images/fonts-encodings/fig14-11.png)
*图 14-11：FontForge 中的单字替换配置面板。*
:::

::: tip 图 14-12：FontForge 中的简单位置调整（左）与成对字距调整 Kerning（右）配置视窗
![图 14-12：FontForge 中的简单位置调整与成对字距调整配置视窗](/images/fonts-encodings/fig14-12.png)
*图 14-12：FontForge 中的简单位置调整与成对字距调整配置视窗。*
:::

::: tip 图 14-13：FontForge 中配置四步链式上下文替换向导的连续交互界面：(a) 查找表类型选择；(b) 格式指定；(c) 规则覆盖范围设定；(d) 语境与替换动作绑定
![图 14-13：FontForge 中配置四步链式上下文替换向导的连续交互界面](/images/fonts-encodings/fig14-13.png)
*图 14-13：FontForge 中配置四步链式上下文替换向导的连续交互界面：(a) 查找表类型选择；(b) 格式指定；(c) 规则覆盖范围设定；(d) 语境与替换动作绑定。*
:::

---

# 苹果高级排版（AAT）与有限状态自动机（FSM）

在排版工程史上，苹果公司走了一条与微软/Adobe 截然不同、在理论计算机科学上极其优美高贵的道路——**基于有限状态自动机（Finite State Automata, FSM）的 AAT 技术**（存储于字体的 `morx`、`kerx` 与 `feat` 表中）。

在 OpenType 中，排版引擎必须在字符串中进行反复的上下文正则回溯匹配，当面对极长或极复杂的文句时，计算复杂度极易退化；而苹果的 AAT 引擎**在底层本质上是一个纯粹的确定性有限状态机（DFA）**！文本流中的字符被当作状态机的一个个输入事件，引擎在常数时间复杂度内即时驱动状态转移，运行速度极快且极具数学确定性。

::: tip 图 14-14：FontForge 中编辑 AAT 特性与选择器（Features and Selectors）名称的三个管理视窗：(a) 特性族名称；(b) 选择器属性与默认激活开关；(c) 多语言本地化字符串
![图 14-14：FontForge 中编辑 AAT 特性与选择器的三个管理视窗](/images/fonts-encodings/fig14-14.png)
*图 14-14：FontForge 中编辑 AAT 特性与选择器的三个管理视窗：(a) 特性族名称；(b) 选择器属性与默认激活开关；(c) 多语言本地化字符串。*
:::

## 1. 特性与选择器（Features & Selectors）

在 AAT 规范中，排印特性由两个纯整数界定：
* **Feature Type（特性大类编号）**：例如编号 1 代表连字，编号 3 代表大小写转换；
* **Feature Selector（特性选择器编号）**：大类下的具体开关。例如在连字特性下，选择器 0 代表禁用所有连字，选择器 2 代表开启标准连字，选择器 4 代表开启历史连字。
通过在 FontForge 中编辑多语言字典（图 14-14），可以为 macOS 系统的字体调色板提供原生的本地化菜单名称。

## 2. AAT 状态转移矩阵的运作机理

AAT 状态机由以下核心要素咬合运转：
1. **字符分类表（Class Table）**：将字库中数万个字形划分为若干等价类（例如：类 0 = 非数字，类 1 = 数字，类 2 = 斜线 `/`，类 3 = 文本结束符 EOT）；
2. **状态转移矩阵（State Transition Matrix）**：行代表“当前状态”（Current State），列代表“当前读入字形的类别”（Class）。矩阵单元格内严密记录着：
   * **Next State（下一跳状态编号）**；
   * **Mark Current Glyph（是否在当前字形上打上标记标记锚点）**；
   * **Substitute Marked Glyph（将之前被标记的字形替换为指定目标）**；
   * **Substitute Current Glyph（将当前刚读入的字形替换为目标）**；
   * **Push to Stack（是否将当前字形压入内部临时堆栈，最多支持 8 个深度！）**。

::: tip 图 14-15：FontForge 中构建 AAT 有限状态自动机转移矩阵的拓扑视窗。直观展现状态节点、类输入迁移边与字形堆栈操作指令
![图 14-15：FontForge 中构建 AAT 有限状态自动机转移矩阵的拓扑视窗](/images/fonts-encodings/fig14-15.png)
*图 14-15：FontForge 中构建 AAT 有限状态自动机转移矩阵的拓扑视窗。直观展现状态节点、类输入迁移边与字形堆栈操作指令。*
:::

### 经典实战状态机：自动连分数转换器

让我们观察图 14-15 中实现的自动真分数状态机：
* **初始状态（State 1, Start of Text）**：
  * 若输入非数字字符，状态保持在 State 1，无动作；
  * 若读入数字字符（如 ‘3’），状态机在当前数字上打上标记（Mark），并转移至 **State 2（已命中分子候选）**。
* **分子状态（State 2）**：
  * 若继续读入数字，继续标记并保持在 State 2；
  * 若突然读入普通斜杠 `/`，状态机立刻将之前标记的一连串普通数字批量替换为**高位上标分子数字**（Numerators），将当前斜杠替换为优雅的**排印专用分数斜线**（Fraction Slash, `U+2044`），并瞬间跃迁至 **State 3（已命中分数线）**；
  * 若读入其他非数字字符，判定当前非分数语境，静默解除标记并回滚至 State 1。
* **分母状态（State 3）**：
  * 在此状态下读入的任何后续连续数字，一律就地替换为**低位下标分母数字**（Denominators）；
  * 直至遭遇第一个非数字字符，状态机完成闭环，优雅跳回 State 1！

借由这套基于图灵自动机理论的高阶状态引擎，字体的排版逻辑在极度复杂的极端上下文与极端长文本面前，始终坚如磐石、风驰电掣。

---

# 结语

从基础单字替换到链式语境判断，从二维平面浮动锚点到确定性有限状态自动机，高级排版技术为冰冷僵硬的数字矢量字模注入了深邃的语言学智能。

正是这些精妙绝伦的查找表与状态转移矩阵，打破了数百年机械印刷的物理枷锁，让屏幕上跃动的一笔一划能够随着人类思想与语言的节律自由呼吸、顾盼生姿。
