---
description: 雅尼斯·哈拉兰布斯《Fonts & Encodings》第十四章全文深度学术汉译：高级排版技术体系。从 Adobe OpenType 特性定义语言（AFDKO Feature File Syntax）到微软 VOLT（Visual OpenType Layout Tool）视觉化布局工具，再到 FontForge 中的 OpenType 与 Apple AAT（Apple Advanced Typography）底层状态机管理，涵盖字形替换（GSUB）、精确定位（GPOS）、复杂连字、锚点附着、链式上下文规则、字偶距微调与有限状态自动机重排机制。
---

# 第 14 章 · 丰富字体：高级排版技术体系
### Chapter 14: Enriching Fonts: Advanced Typography
**著者：雅尼斯·哈拉兰布斯 博士（Yannis Haralambous, Ph.D.）**  
**英译与增订：P. 斯科特·霍恩 博士（P. Scott Horne, Ph.D.）**  
*选自《字体与编码》（Fonts & Encodings）原著第 549–598 页*

*译者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

## 14.1 引言（Introduction）

在传统活字排版或基础数字字体中，文本的呈现本质上是一种朴素的一对一映射：输入一个字符编码，排版引擎便在其对应的码位处提取单个固定的字形（Glyph），并按照预设的字身宽度（Advance Width）在基线上向前步进。然而，人类灿烂的文字排印文明绝非如此刻板机械。无论是在拉丁文字中追求极致美感的西文古典排版——例如处理 `fi`、`fl`、`ffi` 等字母碰撞连字（Ligatures）、优雅的小型大写字母（Small Capitals）、随段落上下文自动切换的老式非等高数字（Oldstyle Figures / Medieval Numbers）与上下浮动花体尾缀（Swashes）；还是在阿拉伯文、波斯文、乌尔都文等天然草体书写体系中，字母必须依据其位于词首（Initial）、词中（Medial）、词尾（Final）或孤立（Isolated）状态而发生动态形变与垂直悬挂连接；抑或是南亚诸文字（天城文 Devanagari、孟加拉文、泰米尔文等）中辅音字母簇（Consonant Clusters）重组、半字形态与元音符号在主辅音上方、下方甚至左侧跨字身缠绕附着的复杂音节合成机制——这些高阶视觉诉求都对现代数字字体格式提出了革命性的挑战。

为了在根本上解决这些复杂排版问题，计算机字体工程界演化出了两大顶峰级别的技术架构体系：
1. **OpenType 高级排版体系（OpenType Layout）**：由微软与 Adobe 联合制定，通过在 TrueType 或 PostScript 字体容器中深度内嵌 `GSUB`（字形替换表，Glyph Substitution Table）与 `GPOS`（字形定位表，Glyph Positioning Table）两大二进制状态表，辅以 `GDEF`（字形定义与附加元数据表）和 `BASE`（基准线表），建立起一套基于语言系统（Script / Language System）、排版特性（Feature）以及查找子表（Lookup / Subtable）的声明式规则重写与几何微调框架。
2. **Apple AAT 体系（Apple Advanced Typography）**：由苹果公司在经典 QuickDraw GX 革命性架构基础上提炼而成，核心通过 `morx`（扩展变异变形表，Extended Metamorphosis Table）与 `kerx`（扩展字偶间距调整表，Extended Kerning Table），直接在字体底层植入严谨的**有限状态自动机（Finite State Automaton）**。排版引擎在扫描字符流时，状态机根据当前状态与输入类别驱动动态状态转移，并即时执行字形重排、替换与堆栈回溯动作。

在本章中，我们将深入现代字体设计的实际生产环境，全面剖析在 FontLab Studio、微软 VOLT 以及开源字体工坊 FontForge 中，如何构建、配置与调试这套复杂的高级排版规则。

---

## 14.2 在 FontLab 中管理 OpenType 表（Managing OpenType Tables in FontLab）

FontLab 深度内嵌了基于 Adobe 特性文件定义语言（Feature Definition Language）的纯文本语法编译器。字体设计师无需手写底层的二进制字节偏移，只需在特性编辑窗口中使用人类可读的语法描述替换与定位规则，编译引擎便会自动将其打包为符合 OpenType 规范的 `GSUB` 与 `GPOS` 表。

### 14.2.1 特性定义语言（Feature Definition Language）

Adobe 特性定义语法基于严谨的声明式结构，其顶层逻辑由特性声明块（Feature Block）构成：

```fea
feature liga {
    sub f i by f_i;
    sub f l by f_l;
    sub f f i by f_f_i;
} liga;
```

在上述代码中，`feature liga` 声明了标准连字特性（Standard Ligatures）。其内部的 `sub ... by ...` 语句代表字形替换指令。在排版引擎处理文本时，当连续遇到字形 `f` 与 `i`，便会自动将其折叠替换为预先设计好的连字字形 `f_i`。

::: tip 图 14-1：FontLab 中管理与配置 OpenType 样式的面板窗口 (Figure 14-1)
![Figure 14-1: The OpenType window in FontLab](/images/fonts-encodings/fig14-1.png)
*图 14-1：FontLab 中管理与配置 OpenType 样式的面板窗口。左侧窗格罗列当前字体已声明的所有 OpenType 特性；右上方为代码编辑区；右下方为编译日志与错误提示反馈。*
:::

#### 1. 语言系统声明（Language Systems）
OpenType 规则并非全局盲目生效，而是严格锚定在特定的书写系统（Script）与语言体系（Language System）之下。在特性文件的最顶端，必须显式声明所支持的脚本与语言：

```fea
languagesystem DFLT dflt;
languagesystem latn dflt;
languagesystem latn TRK ; /* 土耳其语特殊环境 */
```

在此声明后，排版引擎在为特定语言环境渲染段落时，才会激活该分支下绑定的特性。例如土耳其语中带有小圆点的字母 `i`（点小写 i）对应的大写是带点的 `İ`，而无点小写 `ı` 对应无点大写 `I`；因此在土耳其语环境中，必须禁止将 `fi` 替换为常规连字，否则会导致带点 `i` 的原字形特征丢失，引发拼写语义歧义。

#### 2. 字形类别（Glyph Classes）
为了避免为成百上千个字形逐一编写冗长重复的替换规则，特性语言引入了命名类别（Classes）概念。字形类别以 `@` 符号为前缀声明：

```fea
@UPPERCASE = [A B C D E F G H I J K L M N O P Q R S T U V W X Y Z];
@SMCP = [A.sc B.sc C.sc D.sc E.sc F.sc G.sc H.sc I.sc J.sc K.sc L.sc M.sc N.sc O.sc P.sc Q.sc R.sc S.sc T.sc U.sc V.sc W.sc X.sc Y.sc Z.sc];
@FIGURES_LINING = [zero one two three four five six seven eight nine];
@FIGURES_OLDSTYLE = [zero.oldstyle one.oldstyle two.oldstyle three.oldstyle four.oldstyle five.oldstyle six.oldstyle seven.oldstyle eight.oldstyle nine.oldstyle];
```

利用字形类别，只需一条规则即可完成整套小型大写字母（Small Capitals）的替换定义：

```fea
feature smcp {
    sub @UPPERCASE by @SMCP;
} smcp;
```

#### 3. 字形替换类型全景（Substitution Types）
OpenType `GSUB` 规范支持六种不同维度的字形替换类型：
1. **单字形替换（Single Substitution）**：一个输入字形映射到一个输出字形。例如上述的小写转小型大写字母，或等宽数字（Tabular Figures）切换。
2. **多对一连字替换（Multiple to One / Ligature Substitution）**：多个连续输入字形融合成一个单一的特殊字形（如 `sub f f l by f_f_l;`）。
3. **一对多分解替换（One to Multiple / Multiple Substitution）**：单个字形被分解为若干独立构件（如将特定复合标点拆解为基础字符序列）。
4. **单对多候选交替替换（Alternate Substitution）**：一个输入字形对应多个可选的美术修饰变体，由用户交互选择（例如 `sub ampersand from [ampersand.1 ampersand.2 ampersand.3];`）。
5. **上下文替换（Contextual Substitution）**：仅在特定前驱或后继字形环绕的特定语境下才触发的替换规则。输入字形使用单引号 `'` 标定核心匹配项：
   ```fea
   sub [f long_s]' [b h k l] by [f_alt long_s_alt];
   ```
6. **链式上下文替换（Chained Contextual Substitution）**：分别指定回退前缀上下文（Backtrack）、输入匹配核心（Input）以及前瞻前置上下文（Lookahead）的最高阶替换逻辑：
   ```fea
   sub @BACKTRACK @INPUT' @LOOKAHEAD by @REPLACEMENT;
   ```

::: tip 图 14-2：FontLab 中利用 Adobe Feature 纯代码语法编辑替换与定位规则的编辑器 (Figure 14-2)
![Figure 14-2: The OpenType window in FontLab](/images/fonts-encodings/fig14-2.png)
*图 14-2：FontLab 中利用 Adobe Feature 纯代码语法编辑替换与定位规则的编辑器。在此可以编写复杂的查表规则（Lookups）与多重特性映射。*
:::

### 14.2.2 FontLab 的用户交互界面（FontLab's User Interface）

FontLab 在纯文本编译器的基础上，提供了一套深度的图形化辅助面板。

::: tip 图 14-3：FontLab 中测试 OpenType 语法规则实际渲染效果的交互式演练窗口 (Figure 14-3)
![Figure 14-3: The OpenType testing window in FontLab](/images/fonts-encodings/fig14-3.png)
*图 14-3：FontLab 中测试 OpenType 语法规则实际渲染效果的交互式演练窗口。设计师可以随时键入样例文本，勾选或取消勾选特定 Feature 标签（如 `liga`、`calt`、`onum`），即时观察排版引擎的字形变换反馈。*
:::

在“Classes”（字形分组管理）面板中，设计师可以直接通过鼠标从字体主表格中框选字形拖入类别容器，FontLab 会自动维护类别名称与字形列表的映射同步，防止手写语法时产生由于字形遗漏而导致的类别长度不匹配（Class length mismatch）编译故障。

::: tip 图 14-4：FontLab 中将字形集合聚类为命名类别（Classes）的分组管理面板 (Figure 14-4)
![Figure 14-4: The Classes panel in FontLab](/images/fonts-encodings/fig14-4.png)
*图 14-4：FontLab 中将字形集合聚类为命名类别（Classes）的分组管理面板。*
:::

在动态预览（Preview）窗口中，设计师不仅能审查静态字形轮廓，还能以不同字号实时渲染连字与复杂字偶距调整效果。

::: tip 图 14-5：FontLab 的动态预览（Preview）窗口 (Figure 14-5)
![Figure 14-5: The Preview panel window in FontLab](/images/fonts-encodings/fig14-5.png)
*图 14-5：FontLab 的动态预览（Preview）窗口，用于实机观察特性规则生效后的实际视觉灰度与间距韵律。*
:::

---

## 14.3 在微软 VOLT 中管理 OpenType 表（Managing OpenType Tables in VOLT）

微软开发的 **VOLT（Visual OpenType Layout Tool，视觉化 OpenType 布局工具）** 是数字排印史上的一座丰碑。VOLT 是一款运行在 Windows 环境下的专业级工程软件，其核心设计目标是为世界上最严苛复杂的书写系统（如阿拉伯文、乌尔都文纳斯塔里克体 Nastaliq、天城文、藏文等）提供无可挑剔的高精度交互式布局生产能力。

::: tip 图 14-6：微软 VOLT（Visual OpenType Layout Tool）的项目总览工程面板 (Figure 14-6)
![Figure 14-6: The project window in VOLT](/images/fonts-encodings/fig14-6.png)
*图 14-6：微软 VOLT（Visual OpenType Layout Tool）的项目总览工程面板。自上而下分别展示字体基础度量、脚本与语言系统树、特性绑定列表、独立 Lookup 查表池以及全局字形组（Groups）。*
:::

### VOLT 的工程架构哲学
与 FontLab 依赖代码编译器不同，VOLT 采用高度解耦的数据库模型：
1. **独立查找池（Lookups Pool）**：所有的字形替换与定位逻辑均作为独立的 Lookup 对象存在，拥有唯一的工程名称与行为定义。
2. **多对多特性绑定（Feature Mapping）**：一个排版特性（如 `init`、`medi`、`fina`）仅仅是一个指向一个或多个 Lookup 的指针集合。不同的语言环境可以自由复用已有的 Lookup 链。
3. **视觉化锚点吸附系统（Visual Anchor Positioning）**：在阿拉伯文或印度诸文字中，一个字形上可能包含多个物理附着锚点（例如标音符号附着点 `mark`、连字次级构件附着点 `mkmk`、草体基线进出点 `curs`）。VOLT 允许设计师在交互式画布中通过鼠标拖动十字瞄准线，以亚像素精度将附加符号的附着点与底字锚点严丝合缝地重合锁定。

::: tip 图 14-7：微软 VOLT 中定义复杂字形替换逻辑的工程配置窗口 (Figure 14-7)
![Figure 14-7: The substitution window in VOLT](/images/fonts-encodings/fig14-7.png)
*图 14-7：微软 VOLT 中定义复杂字形替换逻辑的工程配置窗口。直观呈现输入字形队列与匹配替换产物。*
:::

::: tip 图 14-8：微软 VOLT 中利用交互式锚点配置字形精确定位（Positioning）的窗口 (Figure 14-8)
![Figure 14-8: The positioning window in VOLT](/images/fonts-encodings/fig14-8.png)
*图 14-8：微软 VOLT 中利用交互式锚点配置字形精确定位（Positioning）的窗口。通过视觉化调整上标、下标与变音符号的物理锚点，实现字符流的动态咬合。*
:::

VOLT 还内置了全球最强大的打样渲染与调试窗口（Proofing Window）。在打样窗口中，设计师可以输入整段复杂经文，单步回放排版引擎执行的每一轮 Lookup 变换，实时捕获定位漂移或连字击穿故障。

::: tip 图 14-9：微软 VOLT 中对整篇复杂排版文本进行实机渲染打样验证（Proofing）的工作窗口 (Figure 14-9)
![Figure 14-9: The proofing window in VOLT](/images/fonts-encodings/fig14-9.png)
*图 14-9：微软 VOLT 中对整篇复杂排版文本进行实机渲染打样验证（Proofing）的工作窗口。*
:::

---

## 14.4 在 FontForge 中管理 OpenType 表（Managing OpenType Tables in FontForge）

作为现代自由软件世界的旗舰字体编辑器，乔治·威廉姆斯（George Williams）开发的 FontForge 提供了全功能且极具学术深度的高级排版管理界面。在 FontForge 中，设计师可以通过直观的树状菜单直接操作 `GSUB` 与 `GPOS` 的每一个层级。

### 14.4.1 物理定位锚点（Anchors）

在字形编辑画布中，设计师可以随时右键执行“Add Anchor”（添加定位锚点）。每一个锚点被赋予一个命名类别（Anchor Class），并被归类为“Base”（基底附着点）、“Mark”（浮动符号附着点）或“Ligature”（连字多构件附着点）。

::: tip 图 14-10：FontForge 中在字形画板中建立物理定位锚点（左）与锚点大类配置面板（右） (Figure 14-10)
![Figure 14-10: Two anchors defined in the glyph window (left) and the anchor-class window (right) in FontForge](/images/fonts-encodings/fig14-10.png)
*图 14-10：FontForge 中在字形画板中建立物理定位锚点（左）与锚点大类配置面板（右）。图左展示了为重音符号与上下标预留的物理坐标十字靶；图右展示了该锚点大类在全局度量系统中的继承与匹配规则。*
:::

### 14.4.2 非上下文替换（Noncontextual Substitutions）

对于单字形变体、非上下文连字以及交替候选字，FontForge 提供了极简的向导式面板。在字形信息窗口的“Substitutions”标签页中，只需点选目标特性（如 `smcp` 或 `liga`），并指定目标字形名称即可完成映射。

::: tip 图 14-11：FontForge 中单字形替换的交互式配置面板 (Figure 14-11)
![Figure 14-11: Left: the glyph window, single substitution tag; Right: the window for a new single substitution in FontForge](/images/fonts-encodings/fig14-11.png)
*图 14-11：FontForge 中单字形替换（Single Substitution）的交互式配置面板。左侧为字形属性窗口标签；右侧为新建单字形替换的参数绑定对话框。*
:::

### 14.4.3 非上下文定位（Noncontextual Positionings）

定位规则用于修正字形的几何位置与进退度量。最常见的定位规则是字偶间距微调（Pairwise Kerning，特性标签 `kern`）。在 FontForge 中，设计师既可以为特定字母对（如 `T` 与 `o`、`A` 与 `V`）单独设置水平位移修正量 $\\Delta x$，也可以建立基于字形分类的类别字偶距矩阵（Class Kerning Matrix），将成百上千个带有重音变体的拉丁字母按轮廓特征归并计算，极大地压缩了最终字体的二进制体积。

::: tip 图 14-12：FontForge 中简单单字定位（左）与字偶间距微调（右）的配置界面 (Figure 14-12)
![Figure 14-12: The windows for simple (left) and pairwise (right) positionings in FontForge](/images/fonts-encodings/fig14-12.png)
*图 14-12：FontForge 中简单单字定位（左，Simple Positioning）与字偶间距微调（右，Pairwise Positioning）的配置界面。*
:::

### 14.4.4 上下文替换与定位（Contextual Substitutions and Positionings）

当排版逻辑需要根据周围环境动态抉择时，FontForge 会启动链式上下文替换引导向导。向导将复杂的链式规则拆解为四个清晰的渐进步骤：
1. **指定匹配格式（Coverage Format）**：选择是以字形列表（Glyph List）、类别列表（Class List）还是覆盖范围表（Coverage Table）组织数据；
2. **定义回退上下文（Backtrack Glyphs）**：录入匹配核心之前必须出现的字形模式序列；
3. **定义前瞻上下文（Lookahead Glyphs）**：录入匹配核心之后必须出现的字形模式序列；
4. **绑定嵌套子查找（Nested Lookups）**：指定当模式完全吻合时，对核心位置字形所执行的次级替换或位移操作。

::: tip 图 14-13：FontForge 中配置链式上下文替换的前四个关键引导步骤 (Figure 14-13)
![Figure 14-13: The first four steps for defining a chained contextual substitution in FontForge](/images/fonts-encodings/fig14-13.png)
*图 14-13：FontForge 中配置链式上下文替换（Chained Contextual Substitution）的前四个关键引导步骤。[a] 选择特性所属格式；[b] 设定上下文序列类别；[c] 构建前后依赖拓扑；[d] 确认并绑定触发动作。*
:::

---

## 14.5 在 FontForge 中管理 AAT 表（Managing AAT Tables in FontForge）

Apple Advanced Typography（AAT）是数字排印史上在技术深度上极富远见的设计。与 OpenType 依赖庞大静态查表的模式截然不同，AAT 将整个文本排版过程抽象为数学上的**确定性有限状态自动机（DFA, Deterministic Finite Automaton）**。

### 14.5.1 特性与选择器（Features and Selectors）

在 AAT 哲学中，每一个排版视觉维度被称为一个“特性类型（Feature Type）”，而在该特性之下包含若干互相排斥或可多选的“选择器（Selector）”。例如在特性类型 1（Ligatures）下，包含“Common Ligatures On/Off”、“Rare Ligatures On/Off”等选择器。

::: tip 图 14-14：在 AAT 规范中编辑与配置特性名称与选择器的面板 (Figure 14-14)
![Figure 14-14: Editing the names of AAT features and selectors](/images/fonts-encodings/fig14-14.png)
*图 14-14：在 AAT 规范中编辑与配置特性名称（Features）与选择器（Selectors）的面板。左侧罗列特性大类（如连字、小型大写字母、分数），右侧配置其默认开启状态与多语言本地化标签。*
:::

### 14.5.2 在 FontForge 中管理 AAT 有限状态自动机（Managing AAT's Finite Automata in FontForge）

AAT 的核心引擎依赖于**状态转移表（State Transition Table）**。其算法运转流程如下：
1. **输入字符流类别划分（Class Table）**：字体将所有字形映射为有限个离散类别（Classes），例如将所有普通小写字母归为 Class 0，特定连字前驱 `f` 归为 Class 1，元音字母归为 Class 2 等。
2. **状态矩阵寻址（State Table）**：当前状态机处于某个具体状态（如初始状态 State 0）。当接收到类别为 $c$ 的字形输入时，算法在二维状态转移矩阵中查询行（State）与列（Class）的交叉点。
3. **执行原子动作（Transition Actions）**：交叉单元格内存储两个核心指令：
   * **下一转移状态（Next State）**：状态机跳转至新的目标状态；
   * **字形堆栈动作（Glyph Actions）**：指示当前字形是否推入暂存堆栈（Mark）、是否与堆栈顶部字形发生重排置换、或者执行特定的字形替换。

::: tip 图 14-15：AAT 状态转移表与字形重排算法的输入配置界面全貌 (Figure 14-15)
![Figure 14-15: Class and state tables for rearrangement of glyphs in AAT](/images/fonts-encodings/fig14-15.png)
*图 14-15：AAT 状态转移表与字形重排算法的输入配置界面全貌：[a] 字符类别划分与状态转移矩阵网格；[b] 与 [c] 上下文字形替换与堆栈动作控制表。*
:::

这种基于状态机的排版范式运算复杂度极低，能够以严格的单遍线性扫描（$O(n)$ 时间复杂度）完成极其复杂的双向文字重排与动态变异渲染。时至今日，AAT 在 macOS 与 iOS 底层文本系统（Core Text）中依然扮演着不可替代的关键角色，与 OpenType 共同构成了现代数字字体技术的璀璨双璧！
