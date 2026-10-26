---
title: 第四章 · 规范化分解、双向排版算法与东亚表意文字
description: 雅尼斯·哈拉兰布斯《Fonts & Encodings》第四章全文深度学术汉译：组合字符与规范组合等级（ccc）、NFC/NFD/NFKC/NFKD 四大规范化形式、Unicode 双向排版算法（UBA）、CJK 汉字统合原则与表意描述字符（IDC）。
---

# 第四章 · 规范化分解、双向排版算法与东亚表意文字
### Chapter 4: Normalization, Bidirectionality, and East Asian Characters
**著者：雅尼斯·哈拉兰布斯 博士（Yannis Haralambous, Ph.D.）**  
*选自《字体与编码》（Fonts & Encodings）原著第 127–184 页*

---

在本章中，我们将深入考察 Unicode 体系中在数理与工程复杂度上最富挑战性的三大核心技术领域：
1. **规范化与分解算法（Decompositions and Normalizations）**：解决字符序列等价性判定的数学基石，亦是现代万维网（Web）与 XML 规范强制要求的底层准则；
2. **Unicode 双向排版算法（The Unicode Bidirectional Algorithm, UBA）**：解决闪米特语系（阿拉伯文、希伯来文、叙利亚文）从右至左（RTL）书写流与西文、数字从左至右（LTR）书写流在二维空间中嵌套混排的物理难题；
3. **东亚表意文字处理（East Asian Characters）**：中日韩（CJK）数万汉字表意文字的统合分类原则、表意描述字符（IDC）与结构分解。

---

## 规范化与分解（Decompositions and Normalizations）

### 组合字符与规范组合等级（Canonical Combining Classes）

在第二章与第三章中，我们已经了解到 Unicode 引入了大量的**组合字符（Combining Characters）**，尤其是**非空格组合标记（Nonspacing Marks, `Mn`）**。

在视觉呈现上，一个组合字符必须依附于一个**基础字符（Base Character）**。例如，拉丁字母 “a” 后面接续一个组合锐音符 “́”（$\text{U+0301}$），排版引擎便会将锐音符精确定位绘制在字母 “a” 的正上方，合成显示为 “á”。

然而，当一个基础字符需要同时叠加多个组合标记时（例如在古希腊语或越南语中，一个元音可能同时拥有扬抑符、粗气符与下加变音点），变音符号在数据流中的先后输入顺序便引发了严重的语义歧义：
* 序列 `[a, 抑音符 ̀, 抑扬符 ̂]` 与序列 `[a, 抑扬符 ̂, 抑音符 ̀]` 是否应当被视为同一个文本？
* 两个不同方位的标记（一个在上、一个在下）输入顺序颠倒，计算引擎如何判定它们是否等价？

为了在数学层面上彻底形式化变音符的拓扑依附关系，Unicode 为所有组合标记定义了**规范组合等级（Canonical Combining Class, 简称 ccc）**。

在 Unicode 5.0 中，共定义了 53 个组合等级，取值范围为 $0 \sim 255$ 的整数：
* **等级 0（ccc = 0）**：所有独立的基础字符与产生空格的独立符号；
* **文种专属等级（ccc = 7 ~ 26）**：
  * **等级 7**：印度次大陆语言中的 **Nukta（下加点号）**，用于派生新辅音；
  * **等级 8**：日文假名的**浊音符（Dakuten ゛）与半浊音符（Handakuten ゜）**；
  * **等级 9**：印度次大陆语言中的 **Virama / Halant（杀音符 / 纯辅音符号）**；
  * **等级 10–26**：希伯来语的元音点（Niqqud）、半元音与马索拉诵读重音标记；
* **物理几何拓扑等级（ccc = 200 ~ 240）**：根据变音符号依附于基础字符的相对几何空间位置严格正交划分：
  * **等级 202**：紧贴在字符正下方（如塞维利亚软音符 Cedilla ç、下尾形符 Ogonek ę）；
  * **等级 216**：依附在字符右上角（如越南语角符 Horn ơ, ư）；
  * **等级 218**：依附在字符左下角；
  * **等级 220**：悬浮居中于字符正下方且与笔画分离（如各种下加点、下加横线）；
  * **等级 222**：悬浮于字符右下侧；
  * **等级 228**：悬浮于字符左上方；
  * **等级 230（成员最庞大的等级）**：悬浮居中于字符正上方且与笔画分离（包含锐音符 Acute、抑音符 Grave、扬抑符 Circumflex、代字号 Tilde、分音符 Umlaut 等数十种最常见的上加变音符）；
  * **等级 232**：悬浮居中于字符正上方的高层第二阶变音符；
  * **等级 240**：希腊语特有的**下加 Iota（Iota Subscript）**。

#### 规范排序算法（Canonical Ordering Algorithm）
有了组合等级（ccc），计算机便能消除变音符输入顺序的歧义：在任意一个由基础字符引导的组合字符序列中，**算法保持基础字符不动，并按照每个变音符号的 ccc 数值对后续所有非零组合标记执行稳定的升序排序（Stable Sort）**！
* 若两个组合标记的 ccc 等级不同，数值小的必然排在数值大的前面；
* 若两个组合标记的 ccc 等级相同（例如两个同时位于正上方的变音符号），则保留它们原始的输入先后顺序（因为同方向叠加的上下层叠顺序具有明确的视觉与发音差异）。

---

## 规范等价与兼容等价

在 Unicode 文本比对中，存在着两个截然不同维度的等价性概念：

### 1. 规范等价（Canonical Equivalence, $\equiv$）
规范等价指**两个字符序列在功能、语义与最终呈现的外观上具有绝对的、不可区分的同一性**。
* 例如：单一预组合字符 “é”（$\text{U+00E9}$）与拆分序列 `[e (U+0065),  ́ (U+0301)]`；
* 规范等价的序列在人类读者眼中完全是一模一样的文本，在任何符合 Unicode 标准的系统里都必须被视为完全相等的同一字符串。

### 2. 兼容等价（Compatibility Equivalence, $\approx$）
兼容等价指**两个字符序列在核心纯文本语义上相同，但在格式排版、字形变体、数学语义或历史代码页兼容性上存在着某种精细差异**。
* 例如：
  * **连字字形与分离字符**：连字字形 “$\text{ﬁ}$”（$\text{U+FB01}$）兼容等价于 `['f', 'i']`；
  * **全角与半角形式**：全角英文字符 “Ａ”（$\text{U+FF21}$）兼容等价于 ASCII 字符 “A”（$\text{U+0041}$）；
  * **上标与下标数字**：上标平方 “²”（$\text{U+00B2}$）兼容等价于数字字符 “2”（$\text{U+0032}$）；
  * **分数字符**：分数 “½”（$\text{U+00BD}$）兼容等价于序列 `['1', '/', '2']`；
  * **带圈数字**：带圈数字 “④”（$\text{U+2463}$）兼容等价于数字字符 “4”；
  * **字体样式变体**：数学黑板粗体 “$\mathbb{R}$”（$\text{U+211D}$）兼容等价于普通字母 “R”。
* 兼容等价分解必然伴随着**排版与格式信息的不可逆丢失**！一旦将 “²” 分解为 “2”，数学公式中的平方指数语义便退化为了普通基数。

---

## 四种 Unicode 规范化形式（The Four Normalization Forms）

为了在存储、网络通信与数据库检索中确立唯一的确定性标准形态，Unicode 联合 W3C 定义了四种标准的**规范化形式（Normalization Forms, UAX #15）**：

```
                    ┌────────────────────────┐
                    │    原始输入文本序列    │
                    └───────────┬────────────┘
                                │
               ┌────────────────┴────────────────┐
               ▼                                 ▼
       【规范等价分解】                   【兼容等价分解】
      Canonical Decomposition           Compatibility Decomposition
               │                                 │
               ▼                                 ▼
       ┌───────────────┐                 ┌───────────────┐
       │   NFD 形式    │                 │   NFKD 形式   │
       └───────┬───────┘                 └───────┬───────┘
               │                                 │
       【规范等价组合】                   【规范等价组合】
      Canonical Composition             Canonical Composition
               │                                 │
               ▼                                 ▼
       ┌───────────────┐                 ┌───────────────┐
       │   NFC 形式    │                 │   NFKC 形式   │
       │ (Web 默认标准)│                 │ (搜索比对标准)│
       └───────────────┘                 └───────────────┘
```

1. **NFD（Normalization Form D, 规范等价分解）**：  
   将所有预组合字符依据 `UnicodeData.txt` 的规范映射递归拆解为基础字符，并依据 ccc 进行规范排序。
   * 范例：字符 “é”（$\text{U+00E9}$）$\to$ 序列 `[e (U+0065),  ́ (U+0301)]`。
2. **NFC（Normalization Form C, 规范等价分解后组合）**：  
   **全球万维网（W3C / HTML / XML）与现代操作系统的官方默认基准规范化形式！**  
   它首先对文本执行 NFD 完整分解并规范排序，随后利用 Unicode 组合算法，尽可能将相邻的基础字符与组合变音符“重新熔炼装配”为唯一的单一预组合字符。
   * 范例：序列 `[e,  ́]` $\to$ 字符 “é”（$\text{U+00E9}$）。
   * 为什么 NFC 成为互联网首选？因为在绝大多数欧洲语言中，单一预组合字符占用的字节数显著少于分离的多字符序列，传输更加高效，且与早期基于单字节代码页的陈旧系统保持着最高的结构相似度。
3. **NFKD（Normalization Form KD, 兼容等价分解）**：  
   对文本执行最彻底的平坦化兼容分解，抹平所有的排版格式特征、连字、全半角、上标与带圈记号。
   * 范例：连字 “$\text{ﬁ}$” $\to$ `['f', 'i']`；分数字符 “½” $\to$ `['1', '⁄', '2']`。
4. **NFKC（Normalization Form KC, 兼容等价分解后规范组合）**：  
   首先执行深度平坦化的 NFKD 兼容分解，随后执行规范组合。常用于全文搜索引擎与自然语言处理分词中，实现超越视觉格式噪音的纯语义检索匹配。

---

## Unicode 双向排版算法（The Bidirectional Algorithm, UBA）

当一份文献中同时包含从左至右（LTR）书写的文字（拉丁语、希腊语、俄语、汉语）与从右至左（RTL）书写的文字（阿拉伯语、希伯来语、叙利亚语）时，排版系统面临着极度复杂的物理排版难题：
* 文本在计算机内存中必须保持纯粹的**逻辑书写顺序（Logical Order）**；
* 但当文字呈现在屏幕上并发生跨行断行时，阿拉伯文单词必须自右向左流淌，而嵌入其中的英文技术名词与阿拉伯数字却必须自左向右排列！

这项由 Unicode 附录第 9 号（**UAX #9: Unicode Bidirectional Algorithm**）所规定的复杂自动机，是所有现代浏览器排版引擎的核心支柱。

### 1. 字符的方向性属性（Directional Character Types）

在 UBA 算法中，每一个 Unicode 字符都被赋予了一个方向性类别：
* **强方向字符（Strong Types）**：自身的书写方向不可动摇，不受周围上下文影响：
  * **`L`（Left-to-Right）**：强从左到右字符（所有拉丁、西里尔、希腊字母及汉字）；
  * **`R`（Right-to-Left）**：强从右到左字符（希伯来字母及大部分闪米特标点）；
  * **`AL`（Right-to-Left Arabic）**：阿拉伯强右向字符（具有特殊的数字跟随语法）；
* **弱方向字符（Weak Types）**：通常伴随数字或特定语境出现：
  * **`EN`（European Number）**：欧洲数字（ASCII 0–9）；
  * **`ES`（European Number Separator）**：欧洲数字分隔符（加号 `+`、减号 `-`）；
  * **`ET`（European Number Terminator）**：欧洲数字终止符（货币符号 `$`, `€`, `%`）；
  * **`AN`（Arabic Number）**：阿拉伯东部数字（٠–٩）；
  * **`CS`（Common Number Separator）**：通用数字分隔符（小数点 `.`、千分位逗号 `,`）；
  * **`NSM`（Nonspacing Mark）**：非空格组合标记（继承其基础字符的方向性）；
* **中性字符与分隔符（Neutral & Separator Types）**：其最终呈现方向完全由两侧的强字符上下文决定：
  * **`B`（Paragraph Separator）**：段落分隔符；
  * **`S`（Segment Separator）**：制表符 Tab；
  * **`WS`（Whitespace）**：空格；
  * **`ON`（Other Neutral）**：其他中性符号（所有成对的括号、各类通用标点与数学符号）。

### 2. 双向算法执行流水线

UBA 算法的处理流程包含严格定义的阶段流水线：
1. **确定段落嵌入基础方向（Base Direction）**：  
   扫描段落中出现的第一个强方向字符：若为 `L`，则全段默认基准等级为 0（从左至右）；若为 `R` 或 `AL`，则全段默认基准等级为 1（从右至左）；
2. **弱类型与中性类型消歧（Resolving Weak & Neutral Types）**：  
   利用严密的上下文状态转移规则（W1 至 W7、N1 至 N2），将数字、加减号、逗号与空格解析为具体的强方向属性。例如：
   * 夹在两个欧洲数字（`EN`）之间的斜杠（`ES`）或逗号（`CS`），会被自动解析为数字流的一部分，保持从左到右；
   * 被阿拉伯强字符（`AL`）统领的欧洲数字，会自动被提升为阿拉伯数字（`AN`）处理；
3. **隐式嵌入等级计算（Implicit Embedding Levels）**：  
   为段落中的每一个字符分配一个非负整数等级（Level）：
   * 偶数等级代表从左到右（LTR）；
   * 奇数等级代表从右到左（RTL）；
   * 等级数值越大，代表该文本片段在嵌套层次中嵌入得越深；
4. **成对标点符号镜像翻转（Bidi Mirrored）**：  
   对于具有 `Bidi_Mirrored=Yes` 属性的字符（如圆括号 ‘(’ 与 ‘)’、方括号 ‘[’ 与 ‘]’、书名号 ‘《’ 与 ‘》’）：**在奇数等级（RTL 语境）下，排版引擎必须自动将其图元镜像翻转为反向括号**！因为人类在阅读从右向左的文字时，开启句子的前括号在物理上必须位于右侧！
5. **视觉显示重排（Reordering for Display）**：  
   从最高嵌入等级开始，逐层对同等级的字符连续游程（Runs）执行数组逆序反转，直至完成整个段落的屏幕视觉重排。

---

## 东亚表意文字：CJK 统一汉字（CJK Unified Ideographs）

在 Unicode 的宏大版图中，东亚汉字表意文字占据了半壁江山。面对中国大陆（GB 2312/GB 18030）、台湾地区（Big5/CNS 11643）、日本（JIS X 0208/0212/0213）与韩国（KS C 5601）各自制定的庞大国家汉字标准，Unicode 成功实现了世界排印史上最具魄力的统合工程。

### 汉字统合三大法则（The Three Principles of Han Unification）

负责汉字统合的国际专家组织是 **表意文字统合小组（Ideographic Rapporteur Group, 简称 IRG）**。为了避免将同一个汉字在不同国家标准中重复编码造成数据冗余，IRG 确立了严格的三级统合仲裁准则：

```
                    ┌────────────────────────┐
                    │    中日韩候选汉字字形  │
                    └───────────┬────────────┘
                                │
               【第一原则：来源权威审查】(Source Rule)
               确认该字是否被各源标准列为独立字位
                                │
                                ▼
               【第二原则：拓扑构形审查】(Topology Rule)
               部件拓扑骨架是否相同？
                                │
                 ┌──────────────┴──────────────┐
                 ▼                             ▼
              【相同】                      【不同】
                 │                             │
                 ▼                             ▼
    【第三原则：抽象笔画审查】          【确认为不同汉字】
    (Abstract Shape Rule)               独立分配新码位
    笔画特征属于字形风格变体？
                 │
          ┌──────┴──────┐
          ▼             ▼
       【是】        【否】
          │             │
          ▼             ▼
    【统合为一个】   【独立分配】
    【单一码位】     【新码位】
```

1. **来源规则（The Source Rule）**：  
   所有候选汉字必须严格可追溯至中国大陆、台湾地区、日本、韩国、越南等官方国家标准中的确切源头（如 G 源、T 源、J 源、K 源、V 源）；
2. **构形与拓扑规则（Component & Topology Rule）**：  
   分析汉字的内部结构部件及其空间拓扑装配关系。若两个字形的部件拓扑关系不同（例如一个是左右结构，一个是上下结构；或者一个包含“木”旁，另一个包含“本”旁），则**判定为不同字符，坚决不予统合**；
3. **抽象形状与笔画规则（Abstract Shape Rule）**：  
   若两个字形拓扑结构完全一致，仅在书法风格、笔画连断、长短或细微装饰性形态上存在差异（例如中国新字形、台湾国字标准字体与日本常用汉字在部分笔画点勾上的印刷习惯差异），则**判定为同一抽象字符的区域字形变体（Glyph Variants），坚决统合为一个单一 Unicode 码位**！具体的区域字形呈现，完全交由上层 OpenType 字体的语言系统标签（`locl` 特性）负责动态切换。

---

## 汉字结构描述符（Ideographic Description Characters, IDC）

面对历史古籍、出土简牍与方言生僻字中无穷无尽的新发现汉字，Unicode 不可能无限穷举预分配码位。为此，Unicode 在基本多语言平面辟出了 12 个极其精妙的**表意文字描述字符（IDC, $\text{U+2FF0} \sim \text{U+2FFB}$）**：

| 码位 | 图元 | 规范名称 | 汉字空间装配拓扑 |
| :---: | :---: | :--- | :--- |
| $\text{U+2FF0}$ | **⿰** | IDEOGRAPHIC DESCRIPTION CHARACTER LEFT TO RIGHT | 左右并列并排结构 |
| $\text{U+2FF1}$ | **⿱** | IDEOGRAPHIC DESCRIPTION CHARACTER ABOVE TO BELOW | 上下叠放结构 |
| $\text{U+2FF2}$ | **⿲** | IDEOGRAPHIC DESCRIPTION CHARACTER LEFT TO MIDDLE AND RIGHT | 左中右三分结构 |
| $\text{U+2FF3}$ | **⿳** | IDEOGRAPHIC DESCRIPTION CHARACTER ABOVE TO MIDDLE AND BELOW | 上中下三分结构 |
| $\text{U+2FF4}$ | **⿴** | IDEOGRAPHIC DESCRIPTION CHARACTER FULL SURROUND | 全包围封闭结构（如“国”、“回”） |
| $\text{U+2FF5}$ | **⿵** | IDEOGRAPHIC DESCRIPTION CHARACTER SURROUND FROM ABOVE | 上三包围结构（如“同”、“风”） |
| $\text{U+2FF6}$ | **⿶** | IDEOGRAPHIC DESCRIPTION CHARACTER SURROUND FROM BELOW | 下三包围结构（如“凶”、“画”） |
| $\text{U+2FF7}$ | **⿷** | IDEOGRAPHIC DESCRIPTION CHARACTER SURROUND FROM LEFT | 左三包围结构（如“区”、“巨”） |
| $\text{U+2FF8}$ | **⿸** | IDEOGRAPHIC DESCRIPTION CHARACTER SURROUND FROM UPPER LEFT | 左上包围结构（如“广”、“厅”） |
| $\text{U+2FF9}$ | **⿹** | IDEOGRAPHIC DESCRIPTION CHARACTER SURROUND FROM UPPER RIGHT | 右上包围结构（如“句”、“司”） |
| $\text{U+2FFA}$ | **⿺** | IDEOGRAPHIC DESCRIPTION CHARACTER SURROUND FROM LOWER LEFT | 左下包围结构（如“这”、“建”） |
| $\text{U+2FFB}$ | **⿻** | IDEOGRAPHIC DESCRIPTION CHARACTER OVERLAID | 两部件穿插重叠结构（如“巫”、“爽”） |

IDC 采用波兰表示法（前缀表达式），使得任何尚未被正式编码的生僻汉字均能被严谨地数学化描述。例如：
$$\text{⿰ 木 木} \longrightarrow \text{“林”}$$
$$\text{⿳ 木 木 木} \longrightarrow \text{“森”}$$
这种前缀描述机制为东亚文献数字化建立了前所未有的动态扩展通道。

---

至此，我们已经完整攻克了 Unicode 宏大体系中最核心的四大支柱：编码历史、字符属性、规范化算法与双向/汉字复杂文本处理。

在第一编的剩余章节中，我们将走出纯粹的字符理论世界，进入**第五章：Unicode 实践与系统支持**、**第六章：Unicode 传输与压缩**、以及**第七章：Web 环境下的字体与排版**，探寻现代操作系统与互联网协议如何将这些规范转化为驱动数十亿终端设备高效运转的工程实体。
