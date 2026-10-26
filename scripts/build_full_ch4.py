import os

ch4_zh = r"""---
title: 第四章：编码方式、正规化与东亚文字体系
description: Unicode 字符规范分解与组合（NFC/NFD/NFKC/NFKD）、双向排版算法（UAX #9）、中日韩汉字统一表意文字（CJK Unihan）、字形描述语言（CDL）与谚文（Hangul）数学构造全景技术解析
---

# 第 4 章：编码方式、正规化与东亚文字体系

*译者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

在本章中，我们将深入考察 Unicode 标准中三个高度专业化但对现代排版与文本处理具有决定性意义的核心领域。这三个领域虽然在语言学表面上看似各自独立，但它们共同构成了高精度数字排版引擎的算法基石：
1. **字符的正规化与规范分解（Decompositions and Normalizations）**：解决字符序列在计算机表示中的多对一等价性与标准化存储问题；
2. **双向排版算法（The Bidirectional Algorithm，即 Unicode 附录 UAX #9）**：解决从右向左书写的文字（阿拉伯文、希伯来文）与从左向右书写的文字（拉丁文、希腊文、西里尔文）在同一文本流中混合时的数学排版与视觉换向逻辑；
3. **东亚文字体系（East Asian Scripts）**：深入分析汉字文化圈中源自中国的表意文字（CJK Unihan 汉字）、字形描述语言（CDL）以及具有极致数学对称性的韩国谚文（Hangul）音节构造模型。

---

## 1. 字符的分解与正规化（Decompositions and Normalizations）

在 Unicode 体系中，同一个人类肉眼可见的字形，往往可以通过不止一种底层的码位序列在计算机内存中进行表达。例如带抑扬符（Circumflex）的小写字母 `â`，既可以编码为单一的预合成字符（Precomposed Character）`U+00E2`（LATIN SMALL LETTER A WITH CIRCUMFLEX），也可以由基础拉丁字母 `a`（`U+0061`）后接非间距组合抑扬符（Combining Circumflex Accent）`U+0302` 组成的双码位序列来表示。

如果文本处理系统不对这种多义性制定严格的规范，那么在文档检索、数据库查询、字符串散列比较（Hashing）以及网页排版匹配时，就会产生灾难性的“同字不同码”失效。

### 1.1 组合字符与结合类（Combining Characters & Combining Classes）

在深入分解算法之前，必须首先对**组合字符（Combining Characters）**的物理吸附机制进行正交数学分类。在 Unicode 标准中，共有数百个组合字符，它们被严密地划分为 **53 个结合类（Combining Classes，简称 cc）**：

| 结合类代号 (cc) | 类别几何方位描述 | 典型结合符示例 | 排版吸附行为 |
| :---: | :--- | :--- | :--- |
| **0** | 间距基底字符（Spacing / Base Glyphs） | 普通字母 `a`, `B`, 数字 `1` | 具备独立进深宽度，作为后续组合符的几何寄主 |
| **1** | 覆盖叠加符（Overlay） | 粗斜线叠加符 `U+0338` (̸) | 从几何正中心横跨基底字符 |
| **7** | 努克塔符（Nukta） | 印度系文字核音变音点 | 紧密吸附于辅音字母右下角 |
| **8** | 假名半浊音/浊音符（Kana Voicing） | 日文浊音符 `U+3099` (゙) | 位于假名右上侧 |
| **9** | 纯辅音抑制符（Virama） | 梵文/印地文去元音符 `U+094D` | 促使辅音形成连写合字（Conjuncts） |
| **202** | 附着于下方（Attached Below） | 下加尾形符（Cedilla `U+0327`）、反尾形符（Ogonek `U+0328`） | 物理笔画直接焊连在基底字符底部 |
| **214** | 附着于上方（Attached Above） | 扁平横线、特定重音符 | 物理笔画焊连在基底字符顶端 |
| **216** | 附着于右上角（Attached Above Right） | 越南文角符（Horn `U+031B` ơ, ư） | 吸附于元音字母的右上肩部 |
| **218** | 附着于左下角（Attached Below Left） | 专用发音辅助圈记 | 吸附于左下基准点 |
| **220** | 绝对下方非附着（Below） | 下加点符（Dot Below `U+0323`）、下抑扬符（Caron Below `U+032C`） | 悬浮位于基底字符正下方，预留光学间隙 |
| **222** | 绝对右下方非附着（Below Right） | 下方右侧辅助符 | 位于右下角光学间隙 |
| **228** | 绝对左方（Left） | 希伯来文/叙利亚文前置引导标 | 位于基底字符左侧空间 |
| **230** | 绝对上方非附着（Above） | 锐音符（Acute `U+0301`）、抑音符（Grave `U+0300`）、抑扬符（Circumflex `U+0302`） | 悬浮位于基底字符正上方 |
| **232** | 绝对右上角非附着（Above Right） | 上加右角符 | 位于右上光学空间 |
| **234** | 顶端最上方（Top Above） | 多层重叠音调符的最外层 | 堆叠在其他上方重音之上的最高空域 |

这一分类体系蕴含着两条关键的排版几何公理：
1. **正交类别的几何独立性**：属于不同非零结合类的组合字符（例如一个下方变音符 `cc=220` 和一个上方变音符 `cc=230`），在物理空间上互不干涉。无论它们在字符串中谁先谁后输入，排版引擎渲染出的最终复合字形在视觉上是完全相同的。
2. **同类结合符的次序敏感性**：属于相同非零结合类的两个组合符（例如两个同在下方的变音符），其输入次序代表了自基底字符向外逐层堆叠（Stacking）的物理拓扑次序，交换它们的顺序将产生不同的字形含义。

### 1.2 规范排序算法（Canonical Ordering Algorithm）

为了消解由于正交结合符输入次序不同导致的二进制不一致，Unicode 提出了**规范排序算法（Canonical Ordering Algorithm）**。

算法流程如下：
1. 遍历待正规化的字符序列，确定每个字符的结合类数值 `cc`；
2. 找出所有连续的由非零结合类字符组成的子序列（即基底字符之后的一串组合变音符）；
3. 对该子序列执行**稳定排序（Stable Sort）**，排序键值为各字符的 `cc` 属性值。所谓“稳定”，是指当两个字符的 `cc` 值相同时，算法必须严格保持它们在原始输入流中的相对次序不变；而当两个字符的 `cc` 值不同时，`cc` 较小的字符必须排在 `cc` 较大的字符之前。

#### 实例演练：复杂多重变音符排序
假设存在一个由基础字母 `a` 以及三个变音符构成的输入序列：
```
1. U+0061  (LATIN SMALL LETTER A)               [cc = 0]
2. U+0302  (COMBINING CIRCUMFLEX ACCENT, 上方)    [cc = 230]
3. U+032C  (COMBINING CARON BELOW, 下方)          [cc = 220]
4. U+0323  (COMBINING DOT BELOW, 下方)            [cc = 220]
```
- 组合符序列为 `[U+0302 (230), U+032C (220), U+0323 (220)]`；
- 执行稳定排序后，由于 $220 < 230$，两个下方变音符必须前移；且由于稳定排序保证相同键值保持相对顺序，`U+032C` 依然位于 `U+0323` 之前；
- 排序后的标准化输出序列为：
```
1. U+0061  (a)         [cc = 0]
2. U+032C  (caron blw) [cc = 220]
3. U+0323  (dot blw)   [cc = 220]
4. U+0302  (circumflx) [cc = 230]
```

### 1.3 规范等价性与兼容等价性（Canonical vs Compatibility Equivalence）

Unicode 严格区分了两种不同深度的等价概念：
1. **规范等价（Canonical Equivalence）**：指在纯文本语义和排版表现上完全一致的等价。预合成字符与经过规范排序的分解序列之间即属于规范等价。
   $$\text{U+00E2} \equiv \text{U+0061} + \text{U+0302}$$
2. **兼容等价（Compatibility Equivalence）**：指在纯文本核心语义上等价，但在视觉风格、排版格式（如上标、下标、字体花体变体）、环绕圈记或度量布局上存在差异的等价。
   - 上标数字与基底数字：$\text{U+00B2} \ ({}^2) \approx \text{U+0032} \ (2)$（带有 `<sup>` 格式标签）；
   - 带圈数字：$\text{U+2460} \ (\text{①}) \approx \text{U+0031} \ (1)$（带有 `<circle>` 标签）；
   - 专用连字与宽字符：$\text{U+FB01} \ (\text{fi}) \approx \text{U+0066} + \text{U+0069}$（带有 `<compat>` 标签）；
   - 复合度量单位：$\text{U+33A1} \ (\text{km}^3) \approx \text{U+006B} + \text{U+006D} + \text{U+0033}$。

### 1.4 四大正规化形式（NFC, NFD, NFKC, NFKD）

结合上述两种分解机制与重新合成逻辑，Unicode 定义了四种标准的文本正规化形式：

```
                    +--------------------+
                    |   Raw Text Stream  |
                    +---------+----------+
                              |
              +---------------+---------------+
              |                               |
       Canonical Decompose          Compatibility Decompose
              |                               |
              v                               v
       +-------------+                 +-------------+
       |     NFD     |                 |    NFKD     |
       +------+------+                 +------+------+
              |                               |
       Canonical Compose               Canonical Compose
              |                               |
              v                               v
       +-------------+                 +-------------+
       |     NFC     |                 |    NFKC     |
       +-------------+                 +-------------+
```

1. **NFD（Canonical Decomposition）**：规范分解形式。将所有合体字完全拆分为基底字符与组合符，并按结合类执行规范排序。
2. **NFC（Canonical Decomposition followed by Canonical Composition）**：规范分解后进行规范合成。**这是万维网联盟（W3C）推荐的 Web 网页标准文本传输形式**。文本先展开为 NFD，随后算法在可能的情况下，尽可能将基底字符与后续组合符重新融合成单一的预合成码位。
3. **NFKD（Compatibility Decomposition）**：兼容分解形式。将所有兼容字符（连字、上标、圈记字符、分数）彻底展开为基本语义字符序列，并执行规范排序。常用于全文搜索索引引擎，使搜索 `km3` 能精确召回含有 `km³` 的文档。
4. **NFKC（Compatibility Decomposition followed by Canonical Composition）**：兼容分解后进行规范合成。在去除所有排版格式变体后，再执行可能的最大化规范预合成。

---

## 2. Unicode 双向排版算法（The Bidirectional Algorithm / UAX #9）

在现代多语言排版体系中，最具算法挑战性的工程难题当属**双向文本（Bidirectional Text，简称 Bidi）**。希伯来文（Hebrew）、阿拉伯文（Arabic）、叙利亚文（Syriac）以及马尔代夫的塔安娜文（Thaana）均是从右向左（Right-to-Left，简称 RTL）书写的；而拉丁字母、汉字、假名、希腊文则是从左向右（Left-to-Right，简称 LTR）书写的。

### 2.1 双向排版的微观拓扑难题

假设在一篇由左向右书写的英文论文中，引用了一句从右向左书写的阿拉伯谚语：
- 如果这句阿拉伯谚语非常短，仅占半行，排版引擎只需在英文行中划出一块局部区域，让阿拉伯词汇在此区域内从右向左排布；
- 但如果这句阿拉伯文字很长，**跨越了物理换行边界**，问题立刻变得极度复杂：
  - 英文文本行从页面的左边距开始排布；
  - 阿拉伯文本在折行后，第一行的末尾应当停留在页面的左边缘还是右边缘？第二行的起始词应当靠在页面的右边距还是左边距？
  - 遇到双语夹杂的标点符号（句号、逗号）或括号（圆括号、方括号）时，标点究竟归属于外层英文字符流，还是归属于内层阿拉伯语流？

为了给全球所有浏览器、文本编辑器与排版引擎提供唯一无歧义的排版标准，Unicode 联盟制定了著名的 **Unicode 标准附录第 9 号规范（UAX #9: Unicode Bidirectional Algorithm）**。

### 2.2 19 种双向字符类型全表

UAX #9 根据字符在排版中的自然书写方向倾向，为每一个 Unicode 码位赋予了唯一的 `Bidi_Class` 属性，共计 19 种类型：

| 大类划分 | 属性代码 | 类型技术全称 | 涵盖的典型字符群 |
| :---: | :---: | :--- | :--- |
| **强方向类型 (Strong)** | **L** | Left-to-Right | 拉丁字母、汉字、日文假名、韩文谚文、希腊字母、西里尔字母 |
| | **R** | Right-to-Left | 希伯来字母及相关的纯右向左辅音字母 |
| | **AL** | Right-to-Left Arabic | 阿拉伯字母、波斯字母、乌尔都字母及阿拉伯语专属标点 |
| **弱方向类型 (Weak)** | **EN** | European Number | 欧洲数字（ASCII 数字 `0`–`9`） |
| | **ES** | European Number Separator | 欧洲数字分隔符（正号 `+`、负号 `-`） |
| | **ET** | European Number Terminator | 欧洲数字终止符（百分号 `%`、货币符号 `$`, `€`, `¥`） |
| | **AN** | Arabic Number | 阿拉伯-印度数字（`٠`–`٩`） |
| | **CS** | Common Number Separator | 通用数字分隔符（小数点 `.`、千分位逗号 `,`、时间冒号 `:`） |
| | **NSM** | Nonspacing Mark | 非间距组合字符，继承其所吸附的基底字符的方向属性 |
| | **BN** | Boundary Neutral | 边界中性符（零宽空格 `ZWSP`、不可见格式控制符） |
| **中性类型 (Neutral)** | **B** | Paragraph Separator | 段落分隔符（回车换行符 `\n`, `\r`） |
| | **S** | Segment Separator | 行内制表符（Tab `\t`） |
| | **WS** | Whitespace | 常规空格字符（ASCII Space） |
| | **ON** | Other Neutral | 其他中性标点与数学符号（`=`、`@`、引号等） |
| **显示格式控制符** | **LRE** | Left-to-Right Embedding | 显式开启左向右嵌入层级（`U+202A`） |
| | **RLE** | Right-to-Left Embedding | 显式开启右向左嵌入层级（`U+202B`） |
| | **LRO** | Left-to-Right Override | 强制覆盖所有后续字符为左向右显示（`U+202D`） |
| | **RLO** | Right-to-Left Override | 强制覆盖所有后续字符为右向左显示（`U+202E`） |
| | **PDF** | Pop Directional Format | 终结最近一次显式嵌入或覆盖，弹出堆栈（`U+202C`） |

### 2.3 UAX #9 双向算法的六大核心步骤

Bidi 算法的终极目标，是将文本在逻辑内存中的线性存储序列（Logical Order），精确转化为在屏幕物理像素上的显示排列序列（Visual Order）。整个算法被严谨地划分为 6 个阶段：

```
+-------------------------------------------------------------+
| Step 1: 段落分割与基底方向确定 (P1 - P3)                      |
| * 扫描段落首个强方向字符，确立基底嵌入级别 (偶数 0 或奇数 1)      |
+------------------------------|------------------------------+
                               v
+-------------------------------------------------------------+
| Step 2: 显式格式控制符处理与方向堆栈维护 (X1 - X10)          |
| * 压入/弹出 LRE, RLE, LRO, RLO, PDF，确定每个字符的显式层级 |
+------------------------------|------------------------------+
                               v
+-------------------------------------------------------------+
| Step 3: 弱方向类型消解 (W1 - W7)                            |
| * 处理相邻数字、正负号、百分号、小数点，将弱类型提升为强类型 |
+------------------------------|------------------------------+
                               v
+-------------------------------------------------------------+
| Step 4: 中性类型与成对括号消解 (N1 - N2)                    |
| * 结合上下文双向边界，消解空格与标点；成对括号算法匹配方向    |
+------------------------------|------------------------------+
                               v
+-------------------------------------------------------------+
| Step 5: 隐式层级最终确定 (I1 - I2)                          |
| * 根据消解后的最终强类型，为每个字符赋予最终整数级别 Level  |
+------------------------------|------------------------------+
                               v
+-------------------------------------------------------------+
| Step 6: 视觉层级反转与字形镜像 (L1 - L4)                    |
| * 从最高级别到最低奇数级别递归反转子串；翻转成对镜像字符      |
+-------------------------------------------------------------+
```

1. **第一步：段落划分与基底层级判定（Paragraph Level）**：
   - 将文本流以段落分隔符（`B`）切割为独立段落；
   - 扫描段落内出现的**第一个强方向字符（Strong Type）**：如果第一个强字符是 `L`，则本段的基底嵌入层级（Base Level）确定为偶数 `0`（代表 LTR 主流）；如果首个强字符是 `R` 或 `AL`，则基底嵌入层级确定为奇数 `1`（代表 RTL 主流）。
2. **第二步：显式层级与堆栈推演（Explicit Levels）**：
   - 维护一个方向状态栈，最大深度为 125 层；
   - 遍历字符流：遇到 `RLE` 则将当前层级提升至最近的更高奇数并压栈；遇到 `LRE` 则提升至最近的更高偶数并压栈；遇到 `PDF` 则出栈恢复上一层级。
3. **第三步：弱方向类型消解规则（Weak Types Resolution）**：
   - **W1 规则**：非间距组合符 `NSM` 转换为其前驱字符的类型；
   - **W2 规则**：紧随阿拉伯强类型 `AL` 之后的欧洲数字 `EN` 转换为阿拉伯数字 `AN`；
   - **W4 规则**：夹在两个同类型数字中间的数字分隔符（如 `12:30` 或 `1,000`）被转换为数字类型；
   - **W5 规则**：与欧洲数字直接相连的终止符（如 `100%` 或 `$50`）转换为欧洲数字 `EN`；
   - **W7 规则**：在 LTR 上下文中的欧洲数字 `EN` 最终被视同为纯左向右强类型 `L`。
4. **第四步：中性类型与括号匹配消解（Neutral Types & Paired Brackets）**：
   - **成对括号算法（Bidi Bracket Algorithm）**：检查中性字符中的开闭括号对（如 `(` 与 `)`）。如果括号内部包含的内容属于强方向，则将这一对括号的显示方向调整为与括号内强内容一致；
   - **N1/N2 规则**：夹在两个相同强类型之间的中性符（如空格、连字符）转变为该强类型；否则退化为当前段落的基底方向。
5. **第五步：隐式层级计算（Implicit Levels）**：
   - 经过弱类型与中性类型消解后，每个字符都获得了最终的确定方向；
   - 根据字符类型与其所处层级的奇偶性，执行细微的层级加成（+1 或 +2），使每个字符分配到一个精确的整数**显示层级（Resolved Embedding Level）**。
6. **第六步：视觉重排与镜像翻转（Reordering & Mirroring）**：
   - 找出整个段落中出现的最大层级数 $M$；
   - 从最大层级 $M$ 开始，向下循环递减至段落内的最低奇数层级：在每一次循环中，找出所有连续层级大于或等于当前层级的字符子串，**将其整体顺序进行镜像反转（Reverse）**！
   - **字形镜像映射（Glyph Mirroring）**：在所有被判定为奇数层级（RTL 区域）的字符中，检索 Unicode 数据库的 `BidiMirroring.txt` 文件。如果该字符存在镜像对应项（例如开括号 `(` 必须翻转为闭括号 `)`），则通知排版引擎调用其在水平方向翻转后的镜像字形！

---

## 3. 东亚文字体系（East Asian Scripts）

东亚文字体系在世界文字史上独树一帜。由中国创造的汉字不仅承载了数千年的华夏文明，更在漫长的历史交流中深度融入了日本、朝鲜半岛与越南的语言文化，形成了举世闻名的**汉字文化圈（Sinosphere）**。

### 3.1 中日韩统一表意文字（CJK Unified Ideographs）

在计算机字符编码史上，汉字的处理曾经是一场旷日持久的技术纷争：
- 中国大陆制定了 GB 2312、GB 12345、GBK 及后来的强制性国家标准 GB 18030；
- 中国台湾制定了五大码（Big5）与 CNS 11643；
- 日本制定了 JIS X 0208 与 JIS X 0213；
- 韩国制定了 KS X 1001 与 KS X 1002。

各个国家和地区在 20 世纪各自对数万个汉字进行了彼此冲突的区位码划分，导致跨区域文档交流时产生极其严重的“乱码（Mojibake）”现象。

```
+-------------------------------------------------------------+
|                Unicode Han Unification Rules                |
|                                                             |
|   1. Source Separation Rule (源语素分离规则):                |
|      If two ideographs are distinguished in any primary     |
|      source standard (e.g. GB 2312 or JIS X 0208), they     |
|      MUST remain separated in Unicode (NO UNIFICATION).     |
|                                                             |
|   2. Cognate Analysis (同源认知分析):                       |
|      If two glyphs share historical etymology and abstract  |
|      topological structure, they map to the same codepoint. |
|                                                             |
|   3. Abstract Shape vs. Design Variation:                   |
|      Font designer differences in stroke slant / serif do   |
|      NOT justify creating new Unicode characters.           |
+-------------------------------------------------------------+
```

为了彻底解决这一历史遗留问题，中日韩三国专家与 Unicode 联盟联合成立了中日韩联合研究组（JRG，后演进为表意文字工作组 IRG），确立了著名的 **汉字统合原则（Han Unification）**：
1. **源语素分离规则（Source Separation Rule）**：这是一条神圣不可侵犯的铁律——如果在任何一个创始源标准（如 GB 2312 或 JIS X 0208）中已经将两个字分别赋予了两个独立编码（即便它们在语言学上是完全同一字的繁简变体），Unicode 就必须严格保留这两个独立编码，绝不强行合并，以保证现有海量旧式数据库能够与 Unicode 实行 100% 无损往返转换（Round-trip Compatibility）。
2. **抽象骨架同源判定（Cognate Analysis）**：如果来自不同国家的两个字形，在历史造字源头上属于同一个字，且两者的抽象拓扑笔画结构（部首、笔画构件、相对空间排布）完全吻合，则被统一判定为同一个 Unicode 码位。
3. **字形设计变体分离（Design Variation）**：字体的地域性设计习惯（例如中文字体习惯将特定偏旁的竖画写直，而日文字体习惯带钩）被认定为**字体设计风格差异（Font-level Glyphic Variation）**，而非编码维度的不同字符，应通过 OpenType 的地域语言特性（如 `locl`）切换字形，而无需分配新的码位。

### 3.2 表意文字描述字符（IDC, Ideographic Description Characters）

尽管 Unicode 目前收录的汉字总数已突破 9 万大关（涵盖 Ext-A 至 Ext-I 扩展区），但人类在古籍文献、人名地名、历史宗谱中依然会不断发现无法在现有字库中检索到的未编码罕见字。

为解决这一“字符集永远滞后于古籍发现”的矛盾，Unicode 引入了一组极其精妙的算子——**表意文字描述字符（Ideographic Description Characters，简称 IDC，码位区间 U+2FF0 至 U+2FFB）**：

| 码位 | 字符形态 | 技术名称 | 运算目数 | 构字拓扑语法说明 |
| :---: | :---: | :--- | :---: | :--- |
| `U+2FF0` | ⿰ | Left to Right | 二目 | 将后序两个构件左右并列排布（如 `⿰木木` $\to$ 林） |
| `U+2FF1` | ⿱ | Above to Below | 二目 | 将后序两个构件上下垂直叠放（如 `⿱木木` $\to$ 𣏯） |
| `U+2FF2` | ⿲ | Left to Middle and Right | 三目 | 将后序三个构件自左至右横向均分（如 `⿲木木木` $\to$ 𣡗） |
| `U+2FF3` | ⿳ | Above to Middle and Below | 三目 | 将后序三个构件自上而下纵向均分（如 `⿳一八口` $\to$ 𠀤） |
| `U+2FF4` | ⿴ | Full Surround | 二目 | 外框全包围内嵌构件（如 `⿴囗大` $\to$ 因） |
| `U+2FF5` | ⿵ | Surround from Above | 二目 | 三包围：自上方及左右两侧下垂包围（如 `⿵门日` $\to$ 间） |
| `U+2FF6` | ⿶ | Surround from Below | 二目 | 三包围：自下方及左右两侧向上包围（如 `⿶凵凶` $\to$ 幽） |
| `U+2FF7` | ⿷ | Surround from Left | 二目 | 三包围：自左侧向上及向右包围（如 `⿷匚矢` $\to$ 医） |
| `U+2FF8` | ⿸ | Surround from Upper Left | 二目 | 两包围：自左上角向下向右展开（如 `⿸广林` $\to$ 麻） |
| `U+2FF9` | ⿹ | Surround from Upper Right | 二目 | 两包围：自右上角向下向左展开（如 `⿹气米` $\to$ 气） |
| `U+2FFA` | ⿺ | Surround from Lower Left | 二目 | 两包围：自左下角向上向右垫底（如 `⿺辶走` $\to$ 辵） |
| `U+2FFB` | ⿻ | Overlaid | 二目 | 两个构件相互穿插十字交叉叠加（如 `⿻十口` $\to$ 申） |

IDC 采用严密的**前缀波兰表达式（Prefix Polish Notation）**语法。借助这组算子，排版软件即使在遇到尚未编入标准的生僻汉字时，也可以通过纯文本串（如 `⿰氵⿱艹⿵门日`）向读者传达该字的结构全貌，甚至由动态排版引擎解析并在运行时自动拼接渲染出该未知汉字的临时轮廓。

### 3.3 字形描述语言（Character Description Language, CDL）

在 1980 年代，汉学专家汤姆·毕晓普（Tom Bishop）与文林研究所开发了一种基于 XML 的矢量汉字描述规范——**CDL（Character Description Language）**。

CDL 摒弃了将汉字视为孤立闭合贝塞尔曲线的传统思路，而是将汉字建立在一个标准的 **$128 \times 128$ 虚拟坐标网格** 之上，通过构件（Components）与笔画（Strokes）的层级引证进行参数化构建：

```xml
<cdl char="明">
  <component char="日" points="0,0 55,128" />
  <component char="月" points="65,0 128,128" />
</cdl>
```

#### CDL 30 种基础笔画系统
CDL 提炼出构成一切汉字的 30 种不可再分的原子笔画（如横 `h`、竖 `s`、撇 `p`、捺 `n`、折 `z`、钩 `g`），每个原子笔画在 XML 中均由起点、控制点与终点的离散坐标直接参数化驱动。这一架构不仅将整个汉字库的物理存储体积压缩了 90% 以上，更使得计算机能够精确知晓汉字的真实书写笔顺，成为汉字书法动态教学、智能字形拉伸与光学补偿的绝佳工程载体。

---

## 4. 韩国谚文（Hangul）的数学构造模型

如果说汉字代表了表意文字演化的高峰，那么朝鲜王朝第四代君主**世宗大王（King Sejong the Great）**于 1446 年颁布《训民正音》（*Hunminjeongeum*）所创制的**谚文（Hangul）**，则代表了人类文字设计史上无与伦比的严密数学理性与音素构字奇迹。

```
+-------------------------------------------------------------+
|             Hangul Syllabic Block Architecture              |
|                                                             |
|   1. Initial Consonant (初声 Choseong / L) : 19 types       |
|      [ᄀ ᄁ ᄂ ᄃ ᄄ ᄅ ᄆ ㅂ ᄈ ㅅ ᄊ ㅇ ㅈ ㅉ ㅊ ㅋ ㅌ ㅍ ㅎ] |
|                                                             |
|   2. Medial Vowel (中声 Jungseong / V) : 21 types           |
|      [ㅏ ㅐ ㅑ ㅒ ㅓ ㅔ ㅕ ㅖ ㅗ ㅘ ㅙ ㅚ ㅛ ㅜ ㅝ ㅞ ㅟ ㅠ ㅡ ㅢ ㅣ] |
|                                                             |
|   3. Final Consonant (终声 Jongseong / T) : 28 states       |
|      [None, ᆨ, ᆩ, ᆪ, ᆫ, ᆬ, ᆭ, ᆮ, ᆯ, ᆰ, ᆱ, ᆲ, ᆳ, ᆴ, ᆵ, ᆶ,  |
|       ᆷ, ᆸ, ᆹ, ᆺ, ᆻ, ᆼ, ᆽ, ᆾ, ㅋ, ㅌ, ㅍ, ㅎ]           |
|                                                             |
|   Total Permutations: 19 * 21 * 28 = 11,172 Syllable Blocks |
+-------------------------------------------------------------+
```

### 4.1 字母（Jamo）分类与语音发生学

谚文的基本构字单元称为**字母（Jamo，자모）**：
- **辅音字母的生理仿生设计**：世宗大王及其学者在设计辅音时，直接模拟了人类发音器官的物理几何形态——舌根闭合喉部模拟为 `ㄱ`，舌尖抵住上颚模拟为 `ㄴ`，嘴唇闭合形态模拟为 `ㅁ`，牙齿形态模拟为 `ㅅ`，喉头形态模拟为 `ㅇ`；
- **元音字母的哲学宇宙观**：元音的设计源自东方传统的“三才”哲学——圆点 `·` 代表天（Heaven），横线 `ㅡ` 代表地（Earth），竖线 `ㅣ` 代表人（Man）。

### 4.2 谚文音节块的数学组合全景

一个完整的韩语音节块必须包含一个**初声辅音（Initial, L）**和一个**中声元音（Medial, V）**，并可选包含一个**终声辅音（Final, T / 支音）**：
- 初声数量：$L_{\text{count}} = 19$；
- 中声数量：$V_{\text{count}} = 21$；
- 终声数量：$T_{\text{count}} = 28$（包含“无终声”状态）。

因此，所有可能构成的现代标准韩语音节总数精确等于：
$$N = 19 \times 21 \times 28 = 11,172 \ \text{个音节}$$

### 4.3 编解码数学投影方程

Unicode 在 `U+AC00` 至 `U+D7A3` 的连续区间内，以极其严苛的代数顺序完整收录了这全部 11,172 个预合成音节块。任何一个韩语音节块的码位 $S$ 与其组成字母 Jamo 索引之间，存在着严格的一一对应解析算术方程：

设基础常数：
$$\text{SBase} = \text{0xAC00}$$
$$L_{\text{count}} = 19, \quad V_{\text{count}} = 21, \quad T_{\text{count}} = 28$$
$$N_{\text{count}} = V_{\text{count}} \times T_{\text{count}} = 21 \times 28 = 588$$

#### 1. 正向合成计算公式（Composition）
给定初声索引 $L_{\text{index}} \in [0, 18]$、中声索引 $V_{\text{index}} \in [0, 20]$ 和终声索引 $T_{\text{index}} \in [0, 27]$，其预合成音节的绝对 Unicode 标量值 $S$ 为：

$$S = \text{SBase} + (L_{\text{index}} \times 588) + (V_{\text{index}} \times 28) + T_{\text{index}}$$

#### 2. 反向算术分解算法（Decomposition）
给定任意一个处于预合成区间的韩语音节码位 $S$（$\text{0xAC00} \le S \le \text{0xD7A3}$），计算其音节内偏移量：
$$S_{\text{index}} = S - \text{SBase}$$

则其各组成 Jamo 的精确索引可通过纯整数除法与取模运算瞬间得出：
$$L_{\text{index}} = \lfloor S_{\text{index}} / 588 \rfloor$$
$$V_{\text{index}} = \lfloor (S_{\text{index}} \bmod 588) / 28 \rfloor$$
$$T_{\text{index}} = S_{\text{index}} \bmod 28$$

#### 3. 生产级 Python 算法实现
```python
def decompose_hangul(codepoint: int):
    """
    将预合成韩语音节码位无损分解为 (L, V, T) Jamo 索引
    """
    SBase = 0xAC00
    LBase = 0x1100
    VBase = 0x1161
    TBase = 0x11A7
    
    if not (0xAC00 <= codepoint <= 0xD7A3):
        return None  # 非预合成音节
        
    s_index = codepoint - SBase
    l_index = s_index // 588
    v_index = (s_index % 588) // 28
    t_index = s_index % 28
    
    l_char = chr(LBase + l_index)
    v_char = chr(VBase + v_index)
    t_char = chr(TBase + t_index) if t_index > 0 else ""
    
    return l_char, v_char, t_char

# 测试：分解 "한" (U+D55C)
# 预期：L=ㅎ (U+1112), V=ㅏ (U+1161), T=ㄴ (U+1102)
print(decompose_hangul(0xD55C))
```

这种极致的数学对称性，使得现代计算机系统无需维护任何庞大的外部查找字典，仅凭几条基础 CPU 算术移位指令，即可在极微秒内完成韩语音节的无损正反向转码与拼写检查，堪称计算机文字编码学中最优雅的工程杰作之一。
"""

for lang in ['zh']:
    p = 'docs/zh/fonts-encodings/chapter-4.md'
    with open(p, 'w', encoding='utf-8') as f:
        f.write(ch4_zh)
    print(f"Wrote {p} ({len(ch4_zh)} chars)")
