# -*- coding: utf-8 -*-
"""
Expand Chapter 14 to full unabridged depth (Chinese).
"""
import os, sys

target_path = r"docs/zh/fonts-encodings/chapter-14.md"

content = r"""# 第 14 章：赋予字体智慧：高级排版技术
### Chapter 14: Enriching Fonts: Advanced Typography
选自《Fonts & Encodings》第 549–598 页
*译者：[Lycoris <lycorismisaka@gmail.com>](mailto:lycorismisaka@gmail.com)*

---

本章的标题指向了 OpenType 与 AAT 字体中的“高级排版特性”（Advanced Typographic Features）。在技术本质上，这些特性是微软（Microsoft）、Adobe 与苹果（Apple）在基础 TrueType 格式之上扩充的一组专门数据表。我们亲历了两种崭新字体格式的崛起：由 Adobe 与微软联合定义的 **OpenType**（早先称为 TrueType Open），以及由苹果公司研发的 **AAT**（Apple Advanced Typography，早先称为 TrueType GX）。

借助这些数据表，数字字体第一次拥有了直面全球多元文字排版挑战的能力。这类“富媒体”智能字体的核心特质在于：**字形的几何排列、上下文替换与微观定位规则，不再硬编码于操作系统底层，而是被完整打包、固化在字体文件自身内部**——更具体而言，就栖息在 OpenType 与 AAT 的专属数据表中。

这种设计虽然使得文字渲染引擎在加载和解析字体时变得更为精密繁重，但与此同时，它赋予了字体设计师前所未有的自由度与主权：设计师对字体的动态排版行为拥有完全的控制权。她可以继承其他字体的成熟排版规则，可以对其进行肆意修改，甚至可以为新文字发明全新的排版逻辑，而无需乞求操作系统升级渲染器。

---

## 1. 高级排版体系全景导论（Introduction）

### 1.1 从字符到字形：文本塑形（Text Shaping）的动态蜕变

在数字排版中，必须严密区分**字符（Character）**与**字形（Glyph）**：
- **字符**是抽象的文本元素（由 Unicode 唯一赋予数值码点），是文本存储、检索与词法分析的唯一主体；
- **字形**则是具体的视觉图像表达。

在传统西方字母体系中，两者往往呈现简单的一对一关系。然而在东方与中东书写系统中，字符与字形的冲突成为了日常排版的常态：
- 在阿拉伯文中，字母必须草书连写，同一个字符因处于词首、词中、词尾或孤立位置而呈现截然不同的视觉形态；
- 在印度各邦文字与东南亚文字中，多个辅音与元音会互相缠绕融合为结构复杂的复合字母簇；
- 在精致的西文古典排版中，连字（Ligatures）、旧体数字（Oldstyle Figures）、真小型大写字母（Small Caps）以及根据前后字符动态调整的高级变体，使得一个字符在不同环境下呈现完全不同的字形面貌。

在高级排版引擎中，文本必须经历一套被称为**文本塑形（Text Shaping）**的动态转换管线：

```
[原始 Unicode 字符流] 
        │
        ▼ (通过 cmap 表映射)
[标称字形序列 (Nominal Glyphs)] 
        │
        ▼ (GSUB 表 / morx 表：上下文替换引擎)
[定位与替换后的字形序列 (Substituted Glyphs)] 
        │
        ▼ (GPOS 表 / kerx 表：微观几何定位引擎)
[具有精确二维偏移量 (X, Y, Advance) 的最终字形流]
```

### 1.2 高级排版特性的分类全景

OpenType 与 AAT 将字体的排版能力划分为两大类操作：**字形替换（Glyph Substitution）** 与 **字形定位（Glyph Positioning）**。

#### 1. 字形替换的五大核心形态（GSUB）
- **单字形替换（Single Substitution）**：将单一字形无条件或条件替换为另一个字形（如将常规小写字母替换为小型大写字母，或将等宽数字替换为旧体数字）；
- **多对一连字替换（Ligature Substitution）**：将连续输入的若干字形合并为一个复合字形（如将 `f` 与 `i` 合并为 `fi`，将 `c` 与 `t` 合并为 `ct`）；
- **一对多拆分替换（Multiple Substitution）**：将单个输入字形拆分为若干分量字形序列（如将未解开的印度复合连字拆分为独立辅音与半字辅音）；
- **从属集合替换（Alternate Substitution）**：为一个字符提供多个视觉候选形态（例如赫尔曼·察普夫设计的 Zapfino 字体中，同一个字母“d”拥有多达九种飞扬跋扈的变体花体字形），供用户在排版软件的调色板中挑选；
- **上下文替换（Contextual Substitution）**：替换仅在特定字形上下文环境中触发（例如，当小写字母“d”与“s”相邻时，自动消除它们之间突兀的连接笔画）。

#### 2. 微观几何定位的六大操作形态（GPOS）
- **单字形微调（Single Adjustment）**：微调特定字形的几何坐标（例如，在全大写文本环境中，将括号向上微调以匹配大写字母高度）；
- **字偶间距调整（Pair Adjustment / Kerning）**：调整两两相邻字形之间的间距；
- **重音符号基底贴合（Mark-to-Base Attachment）**：通过在基底字母与变音符号上预设的光学锚点（Anchors），将变音符号毫厘不差地吸附对齐在基底字母的正上方或正下方；
- **多重重音堆叠贴合（Mark-to-Mark Attachment）**：实现重音符号之间的垂直级联堆叠（如在国际音标或复杂多调希腊文中，一个变音符号精确叠加在另一个变音符号顶端）；
- **连字重音贴合（Mark-to-Ligature Attachment）**：为复合连字（如 `ffi`）设立多个分量锚点，使重音符号能够分别精准吸附在各个字母母体上方；
- **草书连接贴合（Cursive Attachment）**：在阿拉伯文或手写体中，将前一个字形的出笔点（Exit Anchor）与后一个字形的入笔点（Entry Anchor）精准焊接，确保连写线条如丝般顺滑。

#### 3. 常见标准排版特性标签（Feature Tags）
排版特性由 4 字符标签标识，最常用的包括：
- `smcp`（小型大写字母）、`c2sc`（大写转小型大写）；
- `onum`（旧体数字）、`lnum`（对齐等高大写数字）、`pnum`（比例宽度数字）、`tnum`（表格等宽数字）；
- `zero`（带斜杠的数字 0）；
- `frac`（斜线对角分数，如从 `1/2` 生成 ½）、`afrc`（带水平横杠的垂直分数）；
- `liga`（标准连字）、`dlig`（历史/偶用连字）、`hlig`（历史连字）；
- `hist`（历史字形变体，如长 s：ſ）；
- `calt`（上下文变体替换）、`salt`（风格变体替换）；
- `kern`（字偶间距微调）、`mark`（基底重音定位）、`mkmk`（重音堆叠定位）。

---

## 2. 在 FontLab 中掌控 OpenType 表与 AFDKO 语言（Managing OpenType Tables in FontLab）

在专业数字字体设计领域，FontLab Studio 5 是无可争议的工业标准。FontLab 深度集成了 Adobe 的 **AFDKO（Adobe Font Development Kit for OpenType）** 语法规范，采用声明式的**特性定义语言（Feature Definition Language）**来编写高级排版逻辑。

### 2.1 特性定义语言（AFDKO Feature Definition Language）核心语法

#### 1. 字符类（Glyph Classes）的定义
在 AFDKO 中，排版师应当尽量对字符类而非单个字符编写规则。字符类使用方括号 `[...]` 括起，以 `@` 符号命名前缀：

```fea
# 显式枚举字符
@lowercase_vowels = [a e i o u];

# 范围连字符表示法
@Uppercase = [A-Z];
@Digits = [zero-nine];

# 带有特定后缀的连续范围表示法
@SmallCaps = [A.sc-Z.sc];
@OldstyleDigits = [zero.oldstyle-nine.oldstyle];

# 嵌套字符类
@Vowels = [a e i o u];
@AccentedVowels = [aacute eacute iacute oacute uacute agrave egrave igrave ograve ugrave];
@AllVowels = [@Vowels @AccentedVowels];
```

#### 2. 书写系统、语言与特性结构（Scripts, Languages, Features）
一份特性文件由顶端的全局声明和一系列特性块构成：

```fea
languagesystem DFLT dflt;   # 默认书写系统与语言
languagesystem latn dflt;   # 拉丁文，默认语言
languagesystem latn DEU ;   # 拉丁文，德语
languagesystem latn ROM ;   # 拉丁文，罗马尼亚语
languagesystem latn ENG ;   # 拉丁文，英语
languagesystem arab dflt;   # 阿拉伯文
```

在特性块内部，规则可以针对不同语言分支进行特异化装配：

```fea
feature foo {
    script latn;
    language DFLT;
    # 规则 A：通用默认规则
    sub s cedilla by s.cedilla;

    language DEU;
    # 规则 B：德语专属规则，在德语环境下依次执行规则 A 与规则 B
    sub germandbls by S S;

    language ENG excludeDFLT;
    # 规则 C：英语专属规则。关键语法 excludeDFLT 强制排版引擎
    # 在英语环境下彻底剔除默认的规则 A，仅严格执行规则 C！
    sub a by a.alt;
} foo;
```

#### 3. 命名查找表与查找标志（Named Lookups and Lookupflags）
在 AFDKO 中，`lookup` 充当了类似于编程语言中“宏（Macro）”的角色。排版师可以将一组替换或定位规则打包在一个命名的查找块中，随后在特性内部按名称调用：

```fea
lookup GermanSharpS {
    sub germandbls by S S;
} GermanSharpS;

feature smcp {
    sub @lowercase by @smallcaps;
    lookup GermanSharpS;
} smcp;
```

此外，排版师可以使用 `lookupflag` 指令精确限定查找表的过滤范围：
```fea
lookup CustomLigatures {
    lookupflag IgnoreBaseGlyphs, IgnoreMarks;
    # 此查找表将自动跳过所有的基底字符与重音变音符，仅在连字字形之间执行匹配！
    sub f_i' j by f_i_j;
} CustomLigatures;
```
标准 `lookupflag` 关键字包括：
- `IgnoreBaseGlyphs`：忽略基底字符；
- `IgnoreLigatures`：忽略连字字符；
- `IgnoreMarks`：忽略重音与变音符号；
- `RightToLeft`：指示从右向左的排版方向。

#### 4. 各种替换规则（GSUB 语法）全解

- **单字形一对一替换**：
  ```fea
  feature smcp {
      sub @Uppercase by @SmallCaps;
  } smcp;
  ```
  输入类与输出类的元素数量必须严格相等，引擎将按索引逐一映射。

- **从属候选集合替换（Alternate Substitution）**：
  ```fea
  sub e from [e eacute egrave ecircumflex];
  ```
  该规则告知字处理软件：当遇到字母 `e` 时，向用户弹出一个包含 `e, é, è, ê` 的候选列表供手动选择。

- **多对一连字替换**：
  ```fea
  sub f i by f_i;
  sub f l by f_l;
  sub f f i by f_f_i;
  ```

- **上下文替换与单引号语法（Contextual Substitution）**：
  在上下文规则中，**非定向单引号 `'` 是语法的灵魂**：只有被单引号标注的字形才会成为实际被替换的目标，未加单引号的字符仅充当触发规则的环境背景（Context）：
  ```fea
  # 假设我们有两种字母 'd'：常规 'd' 与终结变体 'd.fina'。
  # 规则：当字母 'd' 紧邻在任何字母之后、且后方紧跟单词边界（空格或标点）时，替换为 'd.fina'：
  sub @letters d' @word_boundaries by d.fina;
  ```

- **多重排除规则（Ignore Rules）的实战绝技**：
  在实际书籍排版中，一个经典难题是如何在普通文本中自动将大写 `TEX` 替换为标志性的复合字形 `T_e_X`，同时绝不破坏形如 `TEXT`、`CONTEXT`、`PRETEXTS`、`CORTEX` 等包含 `TEX` 子串的普通单词！
  AFDKO 的 `ignore` 语法支持同时指定多个用逗号分隔的排除环境：
  ```fea
  feature calt {
      # 排除左侧有大写字母的情况，同时排除右侧有大写字母的情况
      ignore sub [A-Z Eacute] T' E' X', T' E' X' [A-Z Eacute];
      # 在排除了所有干扰后，纯粹独立的 TEX 触发替换
      sub T' E' X' by T_e_X;
  } calt;
  ```
  **语法陷阱警告**：第二行中，虽然 `T' E' X'` 自身看似没有上下文，但由于第一行的 `ignore sub` 已经定义了上下文，导致整个 lookup 变成了上下文查找表！因此，第二行代码必须同样为每个目标字符标注单引号，否则编译器将报错中断！

#### 5. 微观几何定位（GPOS 语法）全解

在 GPOS 中，几何微调被封装为**值记录（Value Record）**。一个完整的值记录包含四个有符号整数：

$$\langle xPlacement \quad yPlacement \quad xAdvance \quad yAdvance \rangle$$

1. $xPlacement$：字形在水平方向相对于原点的偏移量；
2. $yPlacement$：字形在垂直方向相对于基线的偏移量；
3. $xAdvance$：字形绘制完成后，光标在水平方向的前进量（Advance Width 增量）；
4. $yAdvance$：光标在垂直方向的前进量（常用于竖排）。

Haralambous 在本章中总结了五种极具代表性的值记录几何行为：
1. `<x y 0 0>`：将字形原点向左/右平移 $x$，向深/高平移 $y$，但**完全不改变字符的步进宽度**。后续字符将紧接在原定位置绘制；
2. `<0 0 x 0>`：字形自身绘制原点不变，但**将字符的前进宽度增加 $x$**（负值则缩窄间距）；
3. `<x 0 x 0>`：字形原点与前进终点同时平移 $x$；
4. `<0 y 0 0>`：字形原点向下移动 $y$（例如下沉变音符），但前进终点依然停留在基线上；
5. `<0 y 0 y>`：字形原点与前进终点同时向下移动 $y$！这将导致：**随后紧跟的所有字符全部在下沉后的深度上继续排版**，直到特性关闭！

- **简写语法**：若值记录仅书写一个数值（如 `pos period <-50>;`），它等价于 `<0 0 -50 0>`，即单纯调节水平前进宽度。
- **基于类的字距微调（Class-based Kerning）**：
  ```fea
  feature kern {
      # 仅用一行代码即可生成 7 × 3 = 21 对字偶微调数据！
      pos [A Aacute Agrave Acircumflex Atilde Adieresis Aring] [v w y] -50;
  } kern;
  ```
- **草书连接（Cursive Attachment）**：
  在手写体或阿拉伯文中，为每个字符定义入笔点（`entry`）与出笔点（`exit`）锚点：
  ```fea
  pos cursive noon <anchor 200 100> <anchor 0 50>;
  ```
- **连字上的多重变音符号贴合**：
  假定在 Monotype Garamond 斜体中存在复合连字 `pret`，在法语动词变位 *prêtâmes* 中需要为其上方挂载两个扬抑符（Circumflex）。由于连字具有多个分量，AFDKO 采用专门的语法声明各个分量锚点：
  ```fea
  pos ligature p_r_e_t
      <anchor 120 700> mark @TOP_MARKS   # 第一个字母 p 的顶部锚点
      ligComponent
      <anchor 250 700> mark @TOP_MARKS   # 第二个字母 r 的顶部锚点
      ligComponent
      <anchor 380 700> mark @TOP_MARKS   # 第三个字母 e 的顶部锚点
      ligComponent
      <anchor 500 700> mark @TOP_MARKS;  # 第四个字母 t 的顶部锚点
  ```

#### 6. 两个核心特例：`aalt` 与 `size`

- **`aalt`（全部候选变体）**：向排版软件提供备选字形总索引：
  ```fea
  feature aalt {
      feature smcp;
      feature onum;
      feature salt;
  } aalt;
  ```
- **`size`（光学尺寸元数据）**：
  PostScript 与普通 TrueType 字体长期存在一个巨大缺陷：字体名称中可能包含“Times New Roman Seven”、“Times Ten”、“ITC Bodoni Seventy-Two”，但光学尺寸仅存在于名字中，字体内部数据表中毫无记录。OpenType 的 `size` 特性通过四个参数彻底解决了这一问题：
  ```fea
  feature size {
      parameters 10.0 3 80 119;
  } size;
  ```
  - `10.0`：设计尺寸（10 磅）；
  - `3`：尺寸子家族编号（同一家族各尺寸必须相同）；
  - `80`：有效尺寸下限（8.0 磅 × 10）；
  - `119`：有效尺寸上限（11.9 磅 × 10）。

---

### 2.2 FontLab Studio 图形工作流与实战调试

1. **OpenType 面板（Window > Panels > OpenType）**：管理特性列表；
2. **Compile 编译检查**：调用内置 AFDKO 编译器进行词法分析，精准报告语法错误；
3. **交互式预览面板（Preview Panel）**：支持实时勾选开启/关闭特性，并在字符基线上以红色和绿色连线直观显示出每一个字偶间距的位移矢量。

---

## 3. 微软 VOLT（Visual OpenType Layout Tool）专业实战（Managing OpenType Tables in VOLT）

微软推出的 **VOLT** 是解决全世界复杂非拉丁书写系统（阿拉伯文、天城体、泰文、缅甸文等）的终极工业级工具。

### 3.1 VOLT 的架构哲学与独特优势

VOLT 完全脱离字形几何绘制，直接操纵已编译的 TrueType 二进制文件（`.ttf`）。它在字体中开辟专属私有表存储项目元数据，并在编译时直接生成高度压缩优化的二进制 `GSUB`、`GPOS`、`GDEF` 表。

VOLT 的核心组织树为四层严格继承：
$$\text{Scripts} \longrightarrow \text{Languages} \longrightarrow \text{Features} \longrightarrow \text{Lookups}$$

### 3.2 视觉化锚点与连字组件定位

1. **Base 与 Mark 交互式对齐**：在画布上直观拖拽命名锚点（如 `top`），实时查看重音吸附效果；
2. **多重连字分量锚点（Ligature Anchors）**：为复合连字（如 `f_i`）设立 `top_1` 与 `top_2` 分量锚点，确保后续变音符能分别精准吸附在各个字母母体上方；
3. **表格化查找表编辑器**：通过直观的表格定义 Left Context、Input 与 Right Context，编译时自动生成最优化的覆盖子表与类定义表；
4. **校对测试器（Proofing Tool）**：内置与 Windows 底层 Uniscribe 完全一致的文本渲染引擎，以彩色分步阶梯形式追踪每个字符经历的每次替换与位移。

---

## 4. 在 FontForge 中掌控 OpenType 表（Managing OpenType Tables in FontForge）

开源字体编辑器 **FontForge** 采取了纯图形化界面直接映射底层 OpenType 数据结构的路线。

### 4.1 核心控制台：Element > Font Info > Lookups
在 `Lookups` 标签页下，GSUB 与 GPOS 被严格分栏管理。点击 `Add Lookup` 即可指定查找类型并绑定特性标签。

### 4.2 锚点系统与非上下文操作
- **画布直观定锚**：在轮廓编辑窗口右键直接插入命名锚点（Base, Mark, Mark-to-Mark, Cursive）；
- **Anchor Control 统一调校面板**：并排预览所有基底与重音的组合效果；
- **Kern by Classes（类字距微调）**：建立二维字形类交叉矩阵，在单元格中批量录入字距补偿值。

### 4.3 链式上下文查找表（Chained Contextual Lookups）
FontForge 支持三种递进的上下文模式：
1. **基于覆盖（Coverage-based）**；
2. **基于字形类（Class-based）**；
3. **链式嵌套子查找表（Nested Sub-lookups）**：通过定义回溯序列、匹配序列与前瞻序列，在匹配处调用专门的子查找表完成复杂变换。

---

## 5. 苹果高级排版（AAT）与状态机理论实战（Managing AAT Tables in FontForge）

### 5.1 OpenType 与 AAT 的根本哲学分野

| 维度 | OpenType 体系 | Apple Advanced Typography (AAT) 体系 |
| :--- | :--- | :--- |
| **底层核心技术** | 基于模式匹配的声明式静态查找表（GSUB/GPOS） | **基于有限状态自动机（Finite State Automata, FSM）** |
| **排版引擎复杂度** | **极度复杂**：引擎必须为每种复杂语言硬编码专属排版状态机 | **极其通用轻量**：Core Text 仅作为通用虚拟机运行字体内置状态机 |
| **核心数据表** | `GSUB`, `GPOS`, `GDEF`, `BASE`, `JSTF` | **`morx`**（扩展变体表）, **`kerx`**（扩展字距表）, **`feat`**, **`trak`** |
| **新书写系统支持** | 必须等待操作系统排版引擎升级 | **字体内置全部逻辑**：新设计的文字在任何旧版苹果设备上立即可用 |
| **生态版图** | 全球事实工业标准（Windows, Linux, Web, Android） | 苹果生态原生基石（macOS, iOS） |

### 5.2 AAT 的特性与选择器体系（Features and Selectors）
AAT 在 **`feat` 表**中采用两级数字体系：
- 特性类型（Feature Type，如 `19` 对应连字）；
- 特性选择器（Feature Selector，如 `2` 对应常用连字，`4` 对应稀有连字）。macOS 字体面板可直接将其解析为可交互的 UI 控件。

---

### 5.3 AAT 有限状态自动机（FSM）的四大核心应用

FontForge 的 `Element > Font Info > Mac SM` 支持构建 AAT 四大状态机：

#### 1. 字形重排状态机（Glyph Rearrangement）
这是 AAT 独有的杀手级特性（OpenType 必须依赖排版引擎硬编码）。在印度天城体中，元音符号在逻辑字符流中位于辅音之后，但视觉上必须显示在整个辅音组合之前。例如，Unicode 字符序列 `KGPTHr` 必须被重排为 `rKGPTH`。

AAT 状态机通过转移矩阵实现这一重排：
- **State 0（起始状态）**：扫描到非辅音字符保持原状；
- **State 1（辅音收集态）**：一旦扫描到辅音字母（K, G, P, T, H），状态机进入辅音态并持续前进；
- **触发重排**：一旦在辅音态后方扫描到字符 `r`，状态机立即执行内置的重排动作指令，将 `r` 瞬间移动到该辅音簇的最前端！

#### 2. 经典连字上下文替换状态机（Contextual Substitution）

```
                    【AAT 连字状态转移矩阵全景】
──────────────────────────────────────────────────────────────────
当前状态 / 输入类   │ Class 3 (字符 'f') │ Class 4 (字符 'i') │ Class 5 (字符 'l')
───────────────────┼────────────────────┼────────────────────┼────────────────────
State 2 (初始基准) │ 跳转: State 3      │ 跳转: State 2      │ 跳转: State 2
                   │ 动作: 标记 'f', 前进│ 动作: 无, 前进      │ 动作: 无, 前进
───────────────────┼────────────────────┼────────────────────┼────────────────────
State 3 (已见 'f') │ 跳转: State 4      │ 跳转: State 2      │ 跳转: State 2
                   │ 动作: 标记, 前进    │ 动作: 替换为 'fi'  │ 动作: 替换为 'fl'
                   │                    │       清空标记, 前进│       清空标记, 前进
───────────────────┼────────────────────┼────────────────────┼────────────────────
State 4 (已见 'ff')│ 跳转: State 2      │ 跳转: State 2      │ 跳转: State 2
                   │ 动作: 替换为 'ff'  │ 动作: 替换为 'ffi' │ 动作: 替换为 'ffl'
                   │       清空标记, 前进│       清空标记, 前进│       清空标记, 前进
──────────────────────────────────────────────────────────────────
```

#### 3. 字形动态插入状态机（Glyph Insertion）
- **阿拉伯文 Kashida（Tatweel）伸展符插入**：用于两端对齐排版。状态机在适宜连写的字母间自动插入可变长度的连接线，且该构件对用户完全隐形（无法用光标选中）；
- **柬埔寨高棉文（Khmer）分裂元音处理**：将单个逻辑元音在视觉上拆解为前后两半，分别包裹在辅音基底的两侧。

#### 4. 上下文字距微调状态机（Contextual Kerning / `kerx`）
AAT 的 `kerx` 表支持强大的堆栈机制：勾选 `Push Current Glyph` 可将最多 8 个字形压入内部堆栈。当弹出 $n$ 个字形时，系统可同时对其批量施加 $n-1$ 个字距微调值，完美征服了西文斜体手写体与复杂多字母连续干涉的微观对齐难题。

---

## 6. 总结与现代排版引擎展望（Conclusions and Modern Outlook）

高级排版技术的发展，是人类文字文明与数字计算机体系深度交融的结晶。
- **Adobe 与 AFDKO** 确立了现代字体设计的工程代码范式；
- **微软与 VOLT** 树立了工业级复杂书写系统的排版工程标杆；
- **苹果与 AAT** 以计算机科学的纯粹性，证明了内嵌有限状态自动机在多语言渲染中的超前优越性；
- **FontForge** 则作为自由软件的旗帜，让底层二进制排版数据结构向所有人彻底敞开。

在当今现代开源生态中，**HarfBuzz** 文本塑形引擎已成为统一江湖的终极枢纽。HarfBuzz 完美融合了 OpenType 声明式布局与 AAT 自动机算法，驱动着全球数十亿台设备，精准呈现着人类所有文明的书写体系之美！
"""

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully written {target_path}, length: {len(content)} chars.")
