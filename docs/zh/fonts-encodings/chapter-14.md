---
title: "第 14 章：丰富字体：高级排版功能"
description: "深入剖析 OpenType 替换与定位（GSUB/GPOS）、AFDKO 特性文件定义语言全语法规范、微软 VOLT 工程实战、FontForge 排版表与苹果高级排版（AAT）有限状态机（morx/kerx）。"
---

# 第 14 章：丰富字体：高级排版功能
### Chapter 14: Enriching Fonts: Advanced Typography
雅尼斯·哈拉兰博斯（Yannis Haralambous, Ph.D.）著
选自《Fonts & Encodings》第 551–598 页
*译者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

## 1. 排版智能化的演进与范式转移（Introduction）

在传统数字字体技术（如原始的 PostScript Type 1 或未经扩充的经典 TrueType）中，字体文件本质上仅仅是一个**静态的字形轮廓容器**。操作系统在接收到一段文本字符串（如 ASCII 或 Unicode 码位序列）时，所能执行的仅仅是最原始的“查表—提取轮廓—绘制”单向映射。每个字符对应且仅对应一个固定字形，字符之间的排列完全由各自预设的水平前进宽度（Advance Width）累加决定，至多辅以一张简单的平面字距对（Kerning Pair）调整表。

然而，人类悠久的活字排版传统与全球纷繁复杂的书写系统，对计算机排版引擎提出了截然不同的严苛要求：
- **经典西文排版美学**：为了避免字符碰撞并提升阅读韵律，两个或三个特定字母必须融合成精致的连字（如 $\text{f}+\text{i} \to \text{fi}$、$\text{f}+\text{f}+\text{l} \to \text{ffl}$）；正文中的大写字母如果与小写字母混排，需要使用缩放至小写字母高度的小型大写字母（Small Capitals）；在普通段落中应使用错落有致的旧体数字（Oldstyle Figures），而在财务表格中则必须使用等宽的齐线数字（Lining Figures）；分数的呈现需要将斜杠与数字自动转换为对角分数（Diagonal Fractions）或坚式分数（Vertical Fractions）。
- **非拉丁复杂书写系统**：在阿拉伯文、叙利亚文、蒙古文中，文字具有天然的草书连笔特性，同一个字母在单词的词首（Initial）、词中（Medial）、词尾（Final）以及孤立状态（Isolated）下必须呈现完全不同的物理拓扑外形；在南亚与东南亚文字体系（如天城文 Devanagari、孟加拉文 Bengali、泰米尔文 Tamil、高棉文 Khmer）中，辅音与辅音相遇会结合成不可分割的半字连结符，而某些元音符号在逻辑编码上虽然输入在辅音之后，在物理视觉呈现上却必须被“重排”并绘制在辅音簇的最左侧。

如果将这些极其复杂的语言学逻辑、上下文敏感分析和微观几何形变硬编码进操作系统的内核或应用程序内部，不仅会导致字体的可移植性彻底丧失，更使得任何新创文字或特殊排版风格的扩展成为天方夜谭。

因此，20 世纪 90 年代中后期，数字字体工业迎来了一场**划时代的范式转移**：**字体的知性化（Enriching Fonts）**。排版规则的解析与执行逻辑被彻底移入字体文件本身。字体不再是一个被动的轮廓数据库，而变成了一个**拥有自主决策能力、包含微型语法规则与有限状态机的智能执行实体**。当前处于统治地位的高级排版字体标准包括：
1. **OpenType（包含 TrueType 轮廓与 CFF/PostScript 轮廓）**：由微软（Microsoft）与 Adobe 联合制定，基于规则声明与分级查表的架构；
2. **Apple Advanced Typography（AAT）**：由苹果公司（Apple）基于 Mac OS 经典 QuickDraw GX 发展而来，基于纯粹计算理论中的**确定性有限状态自动机（Finite State Machine, FSM）**架构。

### 1.1 从字符到字形：文本整形（Text Shaping）的动态蜕变
在现代高级排版引擎（如开源跨平台的 HarfBuzz、Windows 的 Uniscribe/DirectWrite、macOS 的 CoreText）的工作管线中，排版过程被称为**文本整形（Text Shaping）**。输入引擎的字符流（Unicode 序列）在最终变为显示在屏幕上的像素之前，会经历一系列多维的动态蜕变：

$$\text{Unicode Code Points} \xrightarrow{\quad\text{cmap 映射}\quad} \text{Glyph IDs} \xrightarrow{\quad\text{GSUB 替换}\quad} \text{Glyph IDs} \xrightarrow{\quad\text{GPOS 定位}\quad} \text{Positioned Glyphs}$$

在这一过程中，字符与字形之间的一对一关系被彻底打破，呈现出丰富的映射形态：
- **一对多（One-to-Many）**：单个字符被拆分为多个字形片段（例如南亚文字中被前后分割的环绕型元音）；
- **多对一（Many-to-One）**：多个连续字符融合成单个连字字形；
- **多对多（Many-to-Many）**：一段字符序列被重构为另一组长度不同、外形迥异的字形序列；
- **动态微观位移**：字形不再仅仅沿着基线机械排列，而是可以在二维平面内任意平移，甚至自动根据基字轮廓上的物理锚点实现像素级的磁吸吸附。

### 1.2 高级排版双翼：字形替换（GSUB）与几何定位（GPOS）
在 OpenType 架构中，字体的高级排版能力被清晰地解耦为两大核心表：**GSUB（Glyph Substitution Table，字形替换表）**与 **GPOS（Glyph Positioning Table，字形定位表）**。

#### 1. 字形替换的六大形态（GSUB）
字形替换负责在不改变字形坐标系统的前提下，根据语法上下文将当前字形替换为更适宜的候选字形：
1. **单字替换（Single Substitution）**：将一个字形直接替换为另一个字形。最典型的应用是将普通小写字母替换为小型大写字母（`a` $\to$ `a.sc`），或者将普通标点替换为特定语言专用标点。
2. **多字替换（Multiple Substitution）**：将单个字形分解为多个连续字形。例如，在解构复合连字或将特定南亚文字连结符还原为独立笔画时使用。
3. **备选字形替换（Alternate Substitution）**：为一个字形提供多个美学对等的变体，供排版软件向用户展示选择菜单。例如赫尔曼·察夫（Hermann Zapf）设计的著名书法字体 **Zapfino** 中，小写字母 `d` 拥有多达 9 种不同挥洒程度的花体变体，排版引擎可以通过备选替换让用户自由挑选。
4. **合字替换（Ligature Substitution）**：排版中最经典的替换形式。将两个或多个连续字形融合成单个专属连字字形（如 `f` + `i` $\to$ `fi`、`c` + `t` $\to$ `ct`）。
5. **上下文替换（Contextual Substitution）**：替换的触发与否完全取决于该字形所处的前后环境（Context）。最经典的案例是阿拉伯文：一个孤立字母仅在后面紧随另一个相连字母时，才转变为词首形（Initial Form）。在这个过程中，字形外形的改变属于单字替换，而紧随其后的字形则构成了“上下文”。
6. **链式上下文替换（Chained Contextual Substitution）**：上下文替换的高级演进形态。在前述阿拉伯文简单上下文中，被充当“上下文”的后随字形由于已被规则捕获，无法立即参与下一轮替换（导致第二个字母无法顺利变为词中形）。链式上下文替换引入了**回溯序列（Backtrack）**、**输入序列（Input）**与**前瞻序列（Lookahead）**的三元划分，使得上下文环境与实际被替换的字形彻底分离，允许规则像多米诺骨牌一样连续链式触发。
7. **逆向链式上下文单替换（Reverse Chaining Contextual Single Substitution）**：专门针对诸如乌尔都语（Urdu）纳斯塔利格体（Nastaliq）等极端书写系统设计的特殊机制。乌尔都语采用从右向左的书写方向，但在排版时，一个字母的垂直悬垂高度和连笔外形取决于其**后续**字母（即视觉左侧的字母）。逆向链式替换以与文本书写相反的物理方向（从左向右）逆流扫描字形流，确保每一处的字形变体都能提前预知未来的上下文形态。

#### 2. 字形微观几何定位的六大形态（GPOS）
字形定位负责在字形外形已确定的基础上，微调字形在二维排版网格上的度量属性：
1. **单字调整（Single Adjustment）**：对单个字形的水平位置、垂直位置、水平前进量或垂直前进量进行微调。例如，全大写排版时，将括号、连字符等标点符号整体向上提升若干距离，使其与大写字母光学中心对齐。
2. **字对调整（Pair Adjustment）**：即现代化的字距调整（Kerning）。当特定的两个字形相遇时（如 `A` 与 `V`、`T` 与 `o`），动态缩短或拉开它们之间的物理间距。OpenType 的字对调整远超传统 1 对 1 字距对，它既支持基于字形类的笛卡尔积批量调整，更允许在 X 轴与 Y 轴两个维度同时进行平移。
3. **草书连笔吸附（Cursive Attachment）**：在阿拉伯文、波斯文或西文花体手写体中，字母之间通过平滑的起伏曲线无缝连接。草书定位允许为每个字形定义一个“入刀点”（Entry Anchor）和一个“出刀点”（Exit Anchor）。排版引擎在渲染时，自动平移后一个字形，使其入刀点与前一个字形的出刀点在二维空间完全重合。
4. **标音符号吸附基字（Mark-to-Base Attachment）**：现代字体实现 Unicode 任意重音组合的核心基石。传统字体不得不为 `á`、`à`、`ä` 等每个带重音字母预先绘制独立字形，导致汉明空间无限膨胀。而在 Mark-to-Base 定位下，基字（如字母 `a`）定义一个或多个吸附锚点（如顶部锚点 `(250, 450)`），重音符号（如尖音符 `acute`）在其基底定义对应的反向锚点。排版引擎动态将两个锚点严丝合缝地对齐，从而理论上可以用一套重音符号为世界上所有字母精准添加声调。
5. **标音符号叠合（Mark-to-Mark Attachment）**：允许在已有标音符号之上继续叠合第二个、第三个标音符号（如越南语中既有扬抑符又有声调符号 `ế`，或国际音标中的复杂上下标）。
6. **合字部件标音吸附（Mark-to-Ligature Attachment）**：当一个连字由多个元音组成（如 `ae` 连字 `æ`），而排版需要单独在 `e` 的上方添加重音符号时，Mark-to-Ligature 允许字体工程师在单个连字内部按照逻辑部件声明多个独立的局部锚点集，使得声调符号能够准确落在目标字母的正上方，彻底免去了为每一种重音组合重复绘制专用合字的繁重劳动。
7. **上下文定位与链式上下文定位（Contextual / Chained Contextual Positioning）**：定位动作的发生受制于上下文。经典范例：在排版缩写词 `V.A.V.` 时，第二个字母 `V` 应当向第二个句点大幅收紧负字距，这是因为该句点前面是一个带有大倾角留白的 `A`；然而，在排版 `V.V.` 时，相同的 `.` 与 `V` 组合就绝对不能收紧字距，否则两个 `V` 的顶部会相互撞击，视觉上严重粘连并形似 `W`。

#### 3. 标准排版特性标签体系（Standard Feature Tags）
为了让世界各地的文字处理软件（InDesign、Word、Web 浏览器）能够以标准化的方式激活这些功能，OpenType 将所有的 GSUB 与 GPOS 操作归类进一组由 **4 个 ASCII 字符组成的特性标签（Feature Tags）**中：

| 特性标签 | 英文全称 | 类别 | 核心功能与应用场景 |
|:---|:---|:---|:---|
| `liga` | Standard Ligatures | GSUB | 标准合字（默认开启）：处理 `fi`, `fl`, `ff` 等基础排版连字，消除字形碰撞 |
| `dlig` | Discretionary Ligatures | GSUB | 自由/美学连字（默认关闭）：特殊历史或装饰性连字，如 `st`, `ct`, `Th` |
| `hist` | Historical Forms | GSUB | 历史异体字：长 `s`（`ſ`）等古典排版字形替换 |
| `smcp` | Lowercase to Small Capitals | GSUB | 将普通小写字母替换为光学设计的小型大写字母 |
| `c2sc` | Capitals to Small Capitals | GSUB | 将普通大写字母替换为小型大写字母（用于全小大写混排） |
| `onum` | Oldstyle Figures | GSUB | 旧体/悬挂数字：具有高低起伏升降部的数字（`0123456789`），融入正文文本流 |
| `lnum` | Lining Figures | GSUB | 齐线数字：高度完全一致的现代西文数字，常用于表格排版 |
| `tnum` | Tabular Figures | GPOS | 表格等宽数字：强制所有数字具有完全相同的水平前进宽度，保证账目纵向对齐 |
| `pnum` | Proportional Figures | GPOS | 比例数字：每个数字具有符合自身形态的自然字宽 |
| `frac` | Diagonal Fractions | GSUB | 对角斜线分数：将 `1/2`, `3/4` 自动替换为单字分数或分子下标/分母上标 |
| `afrc` | Alternative Fractions | GSUB | 竖线水平分数：将分数排版为带水平横线的垂直堆叠结构 |
| `kern` | Kerning | GPOS | 字距调整（默认开启）：微调特定字对之间的水平物理间隙 |
| `mark` | Mark Positioning | GPOS | 标音符号吸附（默认开启）：将音标磁吸至基底字符的物理锚点上 |
| `mkmk` | Mark-to-Mark Positioning | GPOS | 多重标音符号堆叠吸附 |
| `curs` | Cursive Attachment | GPOS | 草书连笔平滑连接 |
| `size` | Optical Size | 杂项 | 光学尺寸参数声明：声明字体专属设计的字号与推荐使用字号区间 |
| `aalt` | Access All Alternates | 元特性 | 汇集字形的所有变体，供排版软件的“字形调色板”全局检视 |

---

## 2. 在 FontLab 中管理 OpenType 表与 AFDKO 特性定义语言

**FontLab Studio**（版本 4.x 与 5.x）是商业字体开发领域的工业级标杆。在 FontLab 中，OpenType 排版表并非通过散乱的表单配置，而是直接采用了由 Adobe 制定并在开源社区广泛通行的标准：**AFDKO（Adobe Font Development Kit for OpenType）特性定义语言（Feature Definition Language）**。

在 FontLab 的主菜单中打开 `Window > Panels > OpenType`，即可唤出 OpenType 面板。该面板顶部列出当前字体中定义的所有 Feature，中部为纯文本代码编辑区，底部则是全局字形类的声明区。如果在编译时代码存在哪怕一个语法错误，FontLab 将直接中断并报错：
`<PalatinoLinotype-Roman> aborting because of errors`
因此，深入掌握 AFDKO 语法是每位专业字体工程师的必修基本功。

### 2.1 AFDKO 特性定义语言的完整语法规范

#### 1. 字形类（Glyph Classes）的定义与集合运算
在字体排版中，许多字形遵循完全相同的上下文行为。AFDKO 允许使用中括号 `[` 和 `]` 将字形组织为**字形类（Glyph Class）**，类名必须以 `@` 符号开头：

```fea
# 1. 显式枚举定义
@VOWELS = [ a e i o u y ];

# 2. ASCII 字典序连续范围定义（使用连字符 -）
@UPPERCASE = [ A-Z ];
@DIGITS = [ zero-nine ];

# 3. 带特定前后缀的字形范围定义
@SC_LETTERS = [ a.sc-z.sc ];
@HIST_FIGURES = [ foo.023-foo.437 ];

# 4. 类的嵌套与组合
@ALL_LETTERS = [ @UPPERCASE @VOWELS agrave eacute ];
```

#### 2. 书写系统、语言与特性的层级结构
AFDKO 代码严格映射 OpenType 内部的四级索引树：**Script（书写系统） $\longrightarrow$ Language（语言系统） $\longrightarrow$ Feature（特性） $\longrightarrow$ Lookup（查找表）**。

```fea
# 声明字体支持的全局语言系统
languagesystem DFLT dflt; # 默认缺省语言
languagesystem latn dflt; # 拉丁文默认
languagesystem latn TRK ; # 拉丁文土耳其语（点 i 特殊处理）
languagesystem cyrl dflt; # 西里尔文默认

feature liga {
    script latn;
    language DFLT;
        # 针对拉丁文默认语言应用规则 A
        sub f i by f_i;
    language DEU;
        # 德语继承默认规则，并追加规则 B
        sub c k by c_k;
    language ENG excludeDFLT;
        # 英语显式排除默认规则（excludeDFLT），仅应用专用规则 C
        sub f f l by f_f_l;
} liga;
```
- `languagesystem` 语句必须在整个特性的最外层预先声明；
- `excludeDFLT` 关键字具有极高的工程实用价值：当特定语言不希望继承默认规则时，可以干净利落地将其屏蔽。

#### 3. 命名查找表（Named Lookups）与标记标志位（`lookupflag`）
查找表（Lookup）是组织替换或定位规则的独立原子代码块。在一个特性内部，可以通过 `lookup` 关键字定义命名查找表，从而被其他特性复用或精确控制执行次序：

```fea
lookup MyLigatures {
    sub f i by f_i;
    sub f l by f_l;
} MyLigatures;

feature liga {
    lookup MyLigatures;
} liga;
```

为了防止标音符号或连字破坏上下文匹配，AFDKO 提供了 `lookupflag` 指令，用于指示排版引擎在扫描字符流时忽略特定类型的字形：
- `lookupflag IgnoreBaseGlyphs;`：跳过普通基底字形；
- `lookupflag IgnoreLigatures;`：跳过连字字形；
- `lookupflag IgnoreMarks;`：**跳过所有标音符号**。这是西文和阿拉伯文连字排版的关键指令，确保字母 `f` 与 `i` 之间即使插入了一个重音符号（如声调标音），引擎依然能够识别出 `f` 与 `i` 相邻并顺利触发连字；
- `lookupflag RightToLeft;`：指示该查找表专门服务于从右向左的书写系统。

#### 4. 字形替换规则（GSUB 规则全集）
- **单字替换（Single）**：
  `sub a by a.sc;`
  也可以在两个等长类之间实现全自动平行替换：
  `sub @UPPERCASE by @SC_LETTERS;`
- **合字替换（Ligature）**：
  `sub f i by f_i;`
  `sub f f i by f_f_i;`
- **多字替换（Multiple）**：
  `sub f_f_i by f f i;`
- **备选替换（Alternate）**：
  `sub ampersand from [ ampersand.alt1 ampersand.alt2 ampersand.alt3 ];`
- **上下文替换（Contextual Substitution）与撇号语法（`'`）**：
  在 AFDKO 语法中，**非定向撇号（`'`）**是判定上下文作用域的关键标尺。**带有撇号的字形代表实际要被替换的目标，而未带撇号的字形仅仅构成周围的上下文环境**：
  ```fea
  # 当字母 d 后面紧随元音时，将 d 替换为更舒展的花体 d.prettier
  sub d' @VOWELS by d.prettier;

  # 当字母 i 出现在连字 f 或 ff 之后时，将其替换为无点 i（i.nodot），防止与 f 的出刀端相撞
  sub [ f f_f ] i' by i.nodot;
  ```
- **例外排除规则：`ignore sub` 的语法陷阱**：
  假设我们希望将普通文本中独立出现的单词 “TEX” 替换为专有标志字形 `T_e_X`。如果直接书写 `sub T E X by T_e_X;`，那么包含这三个字母的正常单词（如 `CONTEXTUAL`、`PRETEXTS`、`TEXT`、`CORTEX`）都会遭到误伤，被替换成破碎的标志。
  我们必须使用 `ignore sub` 声明前后如果紧邻英文字母则忽略替换。AFDKO 允许使用逗号将多个忽略条件并联：
  ```fea
  # 必须使用撇号标记上下文作用域
  ignore sub [ A-Z ] T' E' X' , T' E' X' [ A-Z ] ;
  sub T' E' X' by T_e_X ;
  ```
  > [!WARNING] **AFDKO 语法陷阱**
  > 注意上述第二行代码中的 `T' E' X'` 也必须带上撇号！虽然第二行表面上看是一个普通合字替换，但由于第一行的 `ignore sub` 为整个查找表确立了上下文语境，整个代码块被编译器强制提升为上下文查找表，第二行的被替换目标必须严格借用撇号语法，否则编译将直接失败。

#### 5. 字形定位规则（GPOS 规则全集）
排版位移的核心是 **值记录（Value Record）**，它是由尖括号包裹的 4 个整数：
$$\langle xPlacement \quad yPlacement \quad xAdvance \quad yAdvance \rangle$$
- $xPlacement$：字形在 X 轴的物理绘制原点偏移量；
- $yPlacement$：字形在 Y 轴的物理绘制原点偏移量；
- $xAdvance$：字形在 X 轴上的前进宽度增减量；
- $yAdvance$：字形在 Y 轴上的前进高度增减量（用于垂直排版）。

常见物理行为模式：
1. `<0 0 -50 0>`：仅缩减前进宽度 50 单元，字形本身绘制位置不变，使下一个字形向左靠拢 50 单元（最经典的单值字距调整，可简写为 `-50`）；
2. `<30 0 0 0>`：字形向右平移 30 单元，但前进宽度不变；
3. `<0 30 0 0>`：字形向上提升 30 单元，基线保持不变（全大写括号提升）；
4. `<0 -30 0 -30>`：字形向下平移 30 单元，且下一个字形的基线起点也同步下沉 30 单元。

- **类间字距对调整（Class-based Kerning）**：
  ```fea
  pos @Left_Round @Right_Round -40;
  ```
  如果 `@Left_Round` 包含 7 个字形，`@Right_Round` 包含 3 个字形，该单行语句在编译后将自动在 GPOS 表中展开并生成 $7 \times 3 = 21$ 个高精度的字对调整记录！
- **草书连笔定位（Cursive Attachment）**：
  ```fea
  pos cursive f <anchor -10 0> <anchor 197 105>;
  pos cursive i <anchor -5 0>  <anchor 155 105>;
  ```
  前一个 anchor 声明当前字形的入刀点（Entry），后一个 anchor 声明出刀点（Exit）。
- **合字上的标音符号吸附（Mark-to-Ligature）**：
  以意大利文或法文中带双扬抑符的三部件合字 `e_t_a`（如 `prêtâmes`）为例，合字拥有 3 个逻辑槽位：
  ```fea
  mark circumflex <anchor 151 438>;
  pos ligature e_t_a <anchor 286 432> <anchor NULL> <anchor 832 432> mark circumflex;
  ```
  使用 `<anchor NULL>` 巧妙跳过中间字母 `t`，直接为第一个部件 `e` 和第三个部件 `a` 分别赋予精准的声调吸附坐标。

#### 6. 光学尺寸特性（`size`）与备选汇总（`aalt`）
传统矢量字体彻底遗弃了金属活字时代随字号变化而微调粗细比率的“光学尺寸”传统。OpenType 通过 `size` 特性填补了这一鸿沟：
```fea
feature size {
    parameters 120 1 90 299;
} size;
```
- `120`：字体的标准设计光学尺寸（Design Size），以十分之一点（decipoints）为单位，即 **12.0 pt**；
- `1`：字体在所属家族光学尺寸序列中的编号（从 0 开始计数）；
- `90` 与 `299`：推荐排版软件应用该字体的字号区间：**9.0 pt 至 29.9 pt**。当用户在排版软件中将字号调整至 36 pt 时，引擎将自动调度专为大标题设计的 ITC Bodoni 72。

### 2.2 FontLab Studio 图形化工作流实战
1. **代码编写与即时编译**：在 OpenType 面板中输入上述代码，点击右上角的 **Compile** 按钮。FontLab 将调用内部集成的 AFDKO 编译器进行语法检查并生成二进制表结构。
2. **Preview 预览面板交互**：打开 `Window > Panels > Preview`。在预览窗口中，字体工程师可以勾选需要激活的 Feature（如 `liga`, `smcp`, `onum`），从下拉菜单中指定 `script` 和 `language`，并在文本框中输入测试字符串（支持通过斜杠输入字形名称，如 `/eacute`）。窗口将上下分栏对比展示开启特性前后的实时矢量渲染效果。
3. **位移向量可视化**：点击预览面板中的箭头按钮，FontLab 将直接在屏幕上以高亮线段绘制出每个字形的前进位移向量与锚点重合状态。
4. **字形类型分类（Glyph Typing）**：在字形单元格上右键选择 `Properties`，在弹出窗口中可明确将字形标记为 `Single Glyph`、`Ligature`、`Mark` 或 `Component`。这一分类数据将直接被写入 OpenType 的 `GDEF`（字形定义表）中，作为 `lookupflag IgnoreMarks` 能够准确执行的底层依据。

---

## 3. 在微软 VOLT 中可视化构建 OpenType 排版表（Managing OpenType Tables in VOLT）

由微软官方推出的 **VOLT（Visual OpenType Layout Tool）** 是专门用于为 TrueType/OpenType 字体添加复杂高级排版表的高级专用工具。与 FontLab 的纯文本编译模式不同，VOLT 提供了一套深度绑定 Windows **Uniscribe** 整形引擎的可视化图形工作流。

### 3.1 VOLT 的架构哲学与私有数据表
- **专属工作环境**：VOLT 仅运行在 Windows 平台下。
- **字体无损保留与破坏性打开**：VOLT 采用了一种特殊的内部项目存储方式。当在 VOLT 中保存字体时，它会将全部工程源码、组名、锚点连接网以私有二进制数据表（如 `TSIV` 表）的形式直接嵌入到 TTF 字体文件内部。
  > [!CAUTION] **数据覆盖警告**
  > 当使用 VOLT 打开一个由其他软件（如 FontLab 或 FontForge）生成的 OpenType 字体时，VOLT 会**强制抹除所有现存的标准 GSUB/GPOS 表**，仅保留自身能够识别的私有表！若未备份源码，此前的排版表工作将彻底丢失。
- **PostScript 名称导入**：由于 TrueType 字形在底层仅以 GID（字形编号）标识，VOLT 打开字体后第一步必须执行 `Import > Import PostScript Names`，从字体的 `post` 表或 `name` 表中恢复人类可读的字形名称。
- **全字形类型标记（Glyph Typing）**：在 `Tools > Edit Glyphs` 窗口中，字体工程师必须对字体中所有字形进行严格的类别审核，将每个符号确凿归类为 `base`（基字）、`ligature`（连字，需指定部件数目）、`mark`（标音符号）或 `component`（部件）。

### 3.2 查找表与规则编辑
VOLT 的项目主窗口（Project Window）呈现清晰的三栏架构：
1. **层次树（Hierarchy Area）**：展示 Script、Language、Feature 的树形隶属关系；
2. **查找表库（Lookup List）**：平铺展示字体中所有全局独立的 Lookup；
3. **字形组库（Glyph Classes）**：展示所有预定义的字形分组。

#### 1. 替换规则的可视化与箭头语法
双击一个替换查找表，VOLT 呈现出极其直观的编辑界面。在规则网格中，规则以简单的箭头形式书写：
- **单字替换**：`a -> a.sc`（VOLT 会自动在旁侧列绘制出字形的真实微缩位图）；
- **连字替换**：`f i -> f_i`；
- **多字替换**：`f_f_t -> f f t`；
- **交替字形**：连续书写多条单字映射：
  ```text
  a -> a.old
  a -> a.odd
  a -> a.pretty
  ```
- **上下文替换**：在被替换字形两侧使用管道符 `|` 声明前后上下文环境：
  ```text
  [ zero - nine ] | [ zero - nine ] -> [ slash.fraction ]
  ```
- **逆向链式替换（Reversal）**：在查找表属性中勾选 **Reversal** 选项框。针对乌尔都语的倒序排版，VOLT 将指示 Uniscribe 引擎从右向左逆流扫描，完美解决复杂的斜向垂直悬挂排版问题。

#### 2. 定位规则与交互式锚点吸附（Visual Anchor Attachment）
在定位编辑窗口中，VOLT 彻底展现了可视化交互的巨大威力：
- 窗口右侧为大尺寸的高精度字形工作画布；
- 字体工程师在定义 Mark-to-Base 或 Mark-to-Ligature 时，画布上会同时浮现出基字与标音符号的矢量轮廓；
- 工程师可以直接用鼠标在画布上拖拽标音符号，将其拖动至视觉上最完美的相对位置，VOLT 会在后台自动计算两者的相对距离并精确锁定各自的 Anchor 坐标；
- 支持为合字中的每一个组成部件依次创建名为 `Component 1: Anchor`、`Component 2: Anchor` 的分立吸附点。

### 3.3 VOLT 校对工具（Proofing Tool）与成品发布
VOLT 内置了强大的 **Proofing Tool**（校对工具）。点击该按钮即可打开一个专门的排版测试窗口，该窗口直接调用操作系统底层的 Uniscribe 引擎。工程师可以输入任意长文本测试用例，窗口将一步一步动态高亮展示每条查找表的触发过程、字形替换前后的序列演变以及各锚点的吸附向量。

测试无误后，通过 `File > Ship Font` 命令即可导出最终商用字体。VOLT 在此时会自动编译出纯净的标准 OpenType 表，并彻底剔除庞大的内部 `TSIV` 工程表，生成体积高度优化的最终文件。

---

## 4. 在 FontForge 中管理 OpenType 表（Managing OpenType Tables in FontForge）

与商业软件 FontLab 的代码驱动和 VOLT 的排他性架构完全不同，开源自由软件 **FontForge**（由 George Williams 领衔开发）提供了一种**纯菜单化、原生双向无损**的 OpenType 管理体验。

FontForge 不强迫用户学习任何专有代码语法，一切排版表操作均通过图形窗口、树状列表和向导式对话框完成。更重要的是，FontForge 能够直接解析字体中现有的任何 OpenType 表，并在保存时直接写回标准的二进制表结构。

### 4.1 核心控制台：Element > Font Info > Lookups
在 FontForge 中打开 `Element > Font Info`，切换至 **Lookups** 选项卡。该面板被清晰地划分为两大部分：**GSUB** 选项卡与 **GPOS** 选项卡。

在每个选项卡内部，Lookups 以树状折叠列表的形式呈现。用户可以点击 `Add Lookup` 创建新的查找表，指定其类型（如 Single Substitution、Ligature、Pairwise Positioning 等），并在其下点击 `Add Subtable` 为其挂载具体的规则子表。查找表的执行严格遵循从上到下的几何物理次序，用户可以通过 `Up` 和 `Down` 按钮随时调整其优先级。

### 4.2 锚点体系与类定义（Anchor Classes）
FontForge 将锚点的管理提升到了字形画布的核心交互层：
1. **全局类声明**：在 `Font Info > Anchor Classes` 窗口中点击 `New`，定义锚点类的名称（如 `Top`、`Bottom`、`Entry`、`Exit`），并指定其排版语义：
   - `abvm`：基字上方标音定位（Above-base mark positioning）；
   - `blwm`：基字下方标音定位（Below-base mark positioning）；
   - `mark`：通用标音吸附；
   - `mkmk`：标音叠合标音定位；
   - `curs`：草书连续连笔定位。
2. **画布直观放置**：关闭设置后打开任意字形的编辑窗口，在轮廓上的目标位置右键点击，选择 `Add Anchor Point`。在弹出的下拉菜单中选择此前定义的锚点类（如 `Top`），该锚点即以图形标记的形式钉死在画布上。字形窗口中会实时显示该锚点的名称与绝对坐标，一目了然。

### 4.3 非上下文替换与定位
在字形列表窗口中，右键选中任意字形并点击 `Glyph Info`：
- **单字替换（Single Subs）**：在 `Substitutions` 标签下点击 `New`，指定目标替换字形与关联的 Feature Tag；
- **多字替换（Mult Subs）**：输入拆解后的多个字形名称（以空格分隔）；
- **交替字形（Alt Subs）**：输入多个备选变体列表；
- **合字替换（Ligatures）**：在目标合字（如 `f_i`）的属性窗口中，填入构成它的源字形组件列表（`f i`）。

在定位方面，`Glyph Info > Pairwise Pos` 允许为当前字形添加字对定位规则。在弹出的配对窗口中选择第二字形（Second Glyph），即可独立调整第一字形和第二字形的原点偏移与前进量 $\Delta XAdvance$。

### 4.4 链式上下文排版向导（Chained Contextual Lookups）
针对复杂的上下文排版，FontForge 提供了强大的 4 步向导式配置流程（见图 14-13）：
- **步骤 1：格式选择（Format）**：选择规则基于字形覆盖列表（By Coverage）、基于字形类别（By Classes）还是基于独立字形枚举（By Glyphs）。
- **步骤 2：序列划分（List of Classes）**：将目标文本流划分为三大连续区域：
  1. **Backtrack（回溯序列）**：匹配目标之前必须出现的字形环境；
  2. **Match / Input（匹配序列）**：当前正在扫描并即将被改变的目标字形序列；
  3. **Lookahead（前瞻序列）**：匹配目标之后必须紧随的字形环境。
- **步骤 3：嵌套子查找表绑定（Sub-lookup Calls）**：在 Match 序列中，精确指定将第几个字形交由哪一个此前已定义好的非上下文查找表（如某个单字替换或合字替换）进行实际处理。
- **步骤 4：多规则覆盖排序**：为整个上下文特性配置一系列规则的匹配优先级，确保长词优先、特殊模式优先于一般模式。

---

## 5. 在 FontForge 中构建苹果高级排版（AAT）有限状态机（Managing AAT Tables in FontForge）

在整个数字排版世界中，FontForge 是极少数（甚至在很长一段历史时期内是唯一一个）能够完整创建与编辑 **Apple Advanced Typography（AAT）** 表的通用工具。

### 5.1 AAT 与 OpenType 的计算理论对决
深入理解 AAT，必须首先理解其背后由 QuickDraw GX 奠定的计算机科学哲学。AAT 与 OpenType 构成了排版引擎设计上的两条截然不同的路线：

```
OpenType 架构：声明式模式匹配树（Declarative Pattern-Matching Engine）
  [ 扫描输入流 ] ──> [ 全局遍历 Feature 规则 ] ──> [ 递归回溯匹配 ] ──> [ 规则替换 ]
  特征：计算复杂度受上下文深度与规则链嵌套影响，最坏情况下存在回溯与性能抖动。

AAT 架构：确定性有限状态自动机（Deterministic Finite State Automata, FSM）
  [ 字符流输入 ] ──> [ 状态转移：State_i ─(Class_k)─> State_j ] ──> [ 触发瞬时动作 ]
  特征：单向线性扫描，时间复杂度恒定为 O(N)，无回溯，底层执行极度高速稳定。
```

AAT 废弃了庞杂的规则匹配，将排版完全建模为一个带有动作的**有限状态机（Finite State Machine）**。字体文件内部包含四张核心 AAT 表：
1. **`morx`（Extended Glyph Metamorphosis Table）**：形态变换表，包含全部基于状态机的字形替换与重排；
2. **`kerx`（Extended Kerning Table）**：扩展字距表，包含基于状态机的上下文字距微调；
3. **`feat`（Feature Name Table）**：特性与选择器名称表，向操作系统 UI 提供本地化的人类可读菜单名；
4. **`trak`（Tracking Table）**：全局字间距跟踪表，根据实际字号自动拉开或收紧整行文字的字距。

### 5.2 特性与选择器命名体系（Features and Selectors）
在 AAT 中，每一个排版效果由一个**特性（Feature）**和一个具体的**选择器（Selector）**二元组共同标识：
- 在 FontForge 中打开 `Element > Font Info > Mac Features`；
- 每一个 Feature 拥有一个数字标识符 `Feature_Id`（例如 5 代表合字，11 代表数字样式）；
- 每个 Feature 包含若干个可选的 `Setting_Id`（例如设置 0 为开启常用合字，1 为开启罕见合字）；
- 字体工程师可以为特性和选择器输入多种自然语言的本地化字符串（英语、法语、中文等）。当在 Mac OS X 的文本程序（如 TextEdit、Pages）中打开排版面板时，系统将直接根据当前系统语言显示这些优雅的原生菜单。

### 5.3 AAT 状态机四大核心操作（Font Info > Mac SM）
在 `Font Info > Mac SM`（Mac State Machines）面板中，包含了 AAT 的四大核心状态机引擎：

#### 1. 字形重排状态机（Glyph Rearrangement）
**这是 AAT 独步天下、而在 OpenType 中完全没有对应底层表的革命性设计**。在 OpenType 中，字符重排必须依赖操作系统外部驱动（如 Uniscribe）对特定语言的硬编码支持；而 AAT 允许字体本身直接通过内部状态机完成任意复杂的字形物理位置对调。

- **南亚文字天城文重排案例**：
  在天城文中，短元音 `r` 在逻辑编码上输入在辅音簇之后，但在物理显示时必须移至整组辅音的前面。例如，输入字符序列 `KGPTHr`，必须自动蜕变为显示序列 `rKGPTH`。
- **状态转移图推演**：
  1. **状态 0（初始状态/行首）**：当遇到非辅音字符时保持状态 0；一旦遇到属于辅音类的字符（`K`, `G`, `P`, `T`, `H`），系统发生转移，跃迁至 **状态 2（辅音收集状态）**，并勾选动作 **Mark Current Glyph As First**（将该辅音标记为重排区间的起始点 A）；
  2. **状态 2（辅音循环状态）**：若继续读入辅音字符，系统停留在状态 2，不改变标记；
  3. **遇到元音触发重排**：当在状态 2 读入字符 `r`（类 5）时，系统立即将当前字符 `r` 标记为区间终点 D，并在下拉菜单中选择执行代号为 `xD => Dx` 的重排指令！
  4. 瞬间，原本位于尾部的终点字形 `r` 被精准移送至起始辅音的前方，随后状态机重置回状态 0，整个过程仅耗费极微小的 CPU 周期。

#### 2. 上下文替换状态机（Contextual Substitution）
在确定性有限状态机中，由于文本流只能向前单向推进，当排版引擎读到后随字符从而确认上下文时，前一个字符在时间线上已经“过去了”。
AAT 巧妙地通过 **标记当前字形（Mark Current Glyph）** 机制解决了这一时空矛盾：
- 状态机在扫描过程中，先为可能发生改变的字形打上临时标记（Mark）；
- 继续前行扫描后置上下文，一旦后置条件满足，立即触发 **Mark Subs** 动作，对早先标记的那个字形执行回溯性替换；
- **斜向分数实战**：输入 `1/2` 自动转换为漂亮的对角分数：
  - 遇到第一个数字 `1` 时，将其标记，状态迁移至“分子状态”；
  - 遇到斜杠 `/` 时，确认分数结构成立，触发对被标记的数字 `1` 执行替换，将其变为分子字形 `1.numerator`，斜杠自身替换为分数斜杠，状态迁移至“分母状态”；
  - 遇到后随的数字 `2` 时，直接替换为分母字形 `2.denominator`。

#### 3. 字形动态插入状态机（Glyph Insertion）
该状态机允许在原始文本流中**凭空动态插入原本不存在的全新字形**，这在处理复杂书写系统时具有无可替代的威力：
- **阿拉伯文 Kashida（拉长线）动态注入**：在两端对齐排版中，阿拉伯文不是通过拉大字间距来对齐，而是在字母连笔处插入一条被称为 Kashida（Tatweel）的水平连接线。AAT 能够根据排版引擎的拉伸信号，在特定的字母连接点状态机中动态插入若干个 Kashida 字形；
- **高棉文裂变元音（Split Vowels）注入**：柬埔寨文字中的部分复合元音需要同时出现在辅音的左侧和右侧。状态机在扫描到该元音时，原地保留右侧部分，同时在辅音左侧动态插入一个新的左侧字形。
- **光标交互属性控制**：状态机专门提供了属性复选框，用于指示插入的字形是作为独立字符响应鼠标光标选择，还是作为依附于相邻字符的“幽灵字形”（不可单独选中文本），完美保障了文字编辑时的交互体验。

#### 4. 上下文扩展字距状态机（Contextual Kerning / `kerx`）
AAT 将字距调整彻底升级为一个**带堆栈的状态机系统**：
- 状态转移单元中提供了一个复选框 **Push Current Glyph**（将当前字形压入内存栈，最多可连续压栈 8 个字形）；
- 状态机一路读取字符并压栈，当识别出终结匹配的字符时，系统触发出栈（Pop）动作；
- 当 $n$ 个字形连续出栈时，系统在底部的参数区同时赋予 $n-1$ 个字距偏移量！
- **应用场景**：完美解决 `A.V.` 缩写词的字距问题。遇到 `A` 压栈，遇到 `.` 压栈，遇到 `V` 出栈，对 `A-.` 赋予 0 偏移，对 `.-V` 赋予 `-400` 强力负字距，而在普通文本流中则绝不误伤。

---

## 6. 结语与现代排版技术图景（Conclusions and Modern Outlook）

回顾从早期数字排版到 OpenType 与 AAT 的辉煌演进，我们可以清晰地看到计算文字学（Computational Typography）的发展脉络：

1. **历史力量的交汇与博弈**：
   20 世纪 90 年代末，微软主导的 Windows Uniscribe 引擎与苹果主导的 Mac OS ATSUI/CoreText 引擎展开了长达十余年的技术竞争。OpenType 凭借 Adobe 的全力支持与 AFDKO 开源工具链的普及，赢得了跨平台桌面出版与商业字体厂商的压倒性青睐；而 AAT 则以其惊世骇俗的有限状态机理论高度和对极端复杂文字的优雅掌控，在苹果生态圈中深深扎根。
2. **现代排版大一统：HarfBuzz 的崛起**：
   进入 21 世纪 10 年代后，由 Behdad Esfahbod 领衔开发的现代开源文本整形引擎 **HarfBuzz** 彻底终结了分裂局面。HarfBuzz 内部完美兼容并原生实现了 OpenType（GSUB/GPOS/GDEF）与 AAT（morx/kerx）的全部规范，被广泛集成到 Google Chrome、Mozilla Firefox、Android 系统、Linux 桌面乃至最新的 Adobe 产品中。
3. **字体的本质跃迁**：
   现代字体已经彻底摆脱了“字符编码翻译表”的原始定义。每一款现代 OpenType/AAT 字体都是一个**兼具几何学、代数学与自动机理论的自洽微型计算机**。正是这些深藏在二进制表结构底层的特性、锚点与状态机，使得数千年人类文明沉淀下来的书法神韵与排版规度，得以在现代数字高精度屏幕与高速印刷机上生生不息、完美重现。

*本章的完整 1:1 全景翻译与专业技术校正由 ヴワル魔法図書館（Voile Magic Library）文献翻译工房 严格依据原著核对呈现。*
