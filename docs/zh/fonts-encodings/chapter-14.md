---
title: "第 14 章：丰富字体：高级排版功能"
description: "OpenType 与 AAT 高级排版功能深度解析：AFDKO 特性语法规范、微软 VOLT 工程实战、Apple Advanced Typography (AAT) 有限状态自动机、GSUB/GPOS 查找表体系。"
---

# 第 14 章：丰富字体：高级排版功能

*译者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

### Chapter 14: Enriching Fonts: Advanced Typography

本章标题所指的“高级排版功能”，特指微软（Microsoft）、Adobe 与苹果（Apple）公司在基础 TrueType 格式之上引入的扩展布局表系统——即当今数字印艺领域的两大支柱体系：**OpenType** 与 **Apple Advanced Typography（AAT）**。

在铅字活字印刷与机械排字机时代，排版师面对多语言混排、阿拉伯文连写变形、南亚诸文字辅音簇叠印、以及严苛的西文活字连字（Ligatures）、小型大写体（Small Capitals）、老式不等高数字（Oldstyle Figures）与上下文长短 's' 替换时，依赖的是人工的拣字经验与手工垫片微调。进入早期个人电脑桌面出版时代后，传统 PostScript Type 1 与基础 TrueType 字体仅仅是一张平面的“字符编码到字形外观”的静态投影表（`cmap`），对于上下文变形和复杂书写系统，只能依赖操作系统层或独立应用程序硬编码的排版外挂（如早期苹果系统的 QuickDraw GX 扩展或 QuarkXPress、InDesign 的私有字形替换引擎）。

OpenType 与 AAT 的革命性突破在于：**将文本动态排版的“智能规则”直接固化、封装在字体文件自身内部**。排版引擎（Shaping Engine，如现代开源基石 HarfBuzz、Windows 系统的 DirectWrite、macOS 系统的 CoreText）不再需要硬编码各语系的拼写语法，而是遵循统一的规范读取字库内部的排版规则表，由字体设计大师完全掌控其字形在不同语言环境、上下文语境下的变形、连缀与微观几何位移。

---

## 1. 排版智能化的演进与范式转移（Introduction）

### 1.1 从字符到字形：文本整形（Text Shaping）的动态蜕变

现代数字文本处理的核心理论，建立在**字符（Character）**与**字形（Glyph）**的严格二元分离之上：
* **字符**：是计算机信息处理系统中的纯粹语义抽象单位，由 Unicode 标量值（Code Point）唯一标识，代表“这个文字是什么”；
* **字形**：是呈现在屏幕像素或纸张墨迹上的具体可视物理形态，由字库中的轮廓数据（Bézier 曲线段）、图元指令与空间度量构成，代表“这个文字怎么呈现”。

在简单西方文字的无修饰排版中，一个字符通常对应一个字形（例如字符 'A' 对应字形 `A`）。但在世界各大原生文字系统与高级西文典籍排印中，字符与字形之间存在着极度复杂的非单射、非双射的动态映射关系：
1. **多对一映射（Many-to-One）**：连字现象。如输入字符序列 `'f' + 'i'`，排版引擎应将其自动融铸为单一的高级连字体字形 `fi`（`f_i`）；在阿拉伯文中，输入 `'l' + 'a'` 必须强制合成为连字 `lam_alif`；
2. **一对多映射（One-to-Many）**：字形分解。如某些南亚印度系文字（Indic Scripts）或东南亚高棉文（Khmer），一个元音字符在逻辑上挂载于辅音之后，但在实际书写视觉上，其笔画必须分裂拆解为前置部首、上标声调与后置主干三个独立的物理字形，环绕包围辅音字母；
3. **一对一上下文条件变体（One-to-One Contextual Variation）**：阿拉伯文与希伯来文的字母在词首（Initial）、词中（Medial）、词尾（Final）与孤立状态（Isolated）具有截然不同的四种书写骨架；在古典英语排印中，字母 `'s'` 若出现在词首或词中应选用长长伸展的 `longs`（'ſ'），而出现在词尾或特定辅音后则选用常规的圆弧 `'s'`；
4. **二维空间微观吸附（2D Spatial Attachment）**：希腊文多重变音符（Polytonic Accents）、希伯来文元音发音符号（Nikud）、阿拉伯文点标（Nuqta）与印度天城文半辅音叠印，要求符号不仅要在水平方向紧跟基字，更必须依据基字的具体几何轮廓高度、笔画倾斜角，在二维空间内精准定位吸附。

现代排版引擎将文本从逻辑码点转化为最终屏幕呈现的几何拓扑流，其数学处理管线可严格抽象为以下四阶转换：

$$\text{Unicode Code Points} \xrightarrow{\quad\text{cmap 映射}\quad} \text{Glyph IDs} \xrightarrow{\quad\text{GSUB 替换}\quad} \text{Glyph IDs} \xrightarrow{\quad\text{GPOS 定位}\quad} \text{Positioned Glyphs}$$

---

### 1.2 高级排版双翼：字形替换（GSUB）与几何定位（GPOS）

在 OpenType 架构中，实现上述智能排版的动力核心被清晰解耦为两大并行的二进制数据表：负责“改换形态”的 **`GSUB`（Glyph Substitution Table，字形替换表）** 与负责“空间微调”的 **`GPOS`（Glyph Positioning Table，字形定位表）**。

#### 1. 字形替换的六大形态（GSUB）

`GSUB` 表内部被组织为一个结构精密的树状层级体系：包含脚本列表（ScriptList）、语言系统列表（LangSysList）、排版特性列表（FeatureList）与查找表列表（LookupList）。其中每个查找表根据排印学需求，被严格划分为六种原子操作形态：

1. **单字替换（Single Substitution, Lookup Type 1）**：将单一输入字形等量替换为另一个目标字形。
   * *典型场景*：小写字母替换为小型大写体（Small Caps, `smcp`），如 `a` $\to$ `a.sc`；表意数字替换为等宽表格数字（Tabular Figures, `tnum`）或老式非等高数字（Oldstyle Figures, `onum`）。
2. **多字替换（Multiple Substitution, Lookup Type 2）**：将单一输入字形拆解为由两个或更多字形构成的有序序列。
   * *典型场景*：历史活字中未编码连字的动态拆分，如将历史遗留字形 `ffi` 拆解为独立的 `f` + `f` + `i`；在印度系文字中将复合辅音印章分解为独立字母与虚线辅音架。
3. **备选替换（Alternate Substitution, Lookup Type 3）**：为单一输入字形提供一个可选的字形阵列集合，允许用户或排版软件根据审美需要交互式选择。
   * *典型场景*：书法花体变体（Swashes, `swsh`），如著名书法字体 Zapfino 中为字母 `'d'` 提供了多达九种飘逸长尾变体；乐谱符号与花边装饰符（Ornaments, `ornm`）的选择。
4. **合字替换（Ligature Substitution, Lookup Type 4）**：将一个严格按序出现的输入字形序列融铸坍缩为一个单一的目标字形。
   * *典型场景*：标准拉丁连字（Standard Ligatures, `liga`），如 `'f' + 'i' \to 'fi'`、`'f' + 'l' \to 'fl'`；历史珍本连字（Discretionary Ligatures, `dlig`），如 `'c' + 't' \to 'ct'`、`'s' + 't' \to 'st'`；德文长 's' 连字（Historical Ligatures, `hlig`）；阿拉伯文中极为普遍的二字、三字连写整体。
5. **上下文替换（Contextual Substitution, Lookup Type 5）**：仅当目标字形处在特定的前驱或后继字符上下文字符串中时，才触发对输入序列中字形的替换。但经典上下文替换有一个致命缺陷：被匹配的“上下文环境字符”会被当前子表消耗锁定，无法参与后续链条的进一步替换。
6. **链式上下文替换（Chained Contextual Substitution, Lookup Type 6）**：上下文替换的最强形态。允许排版师将上下文环境明确划分为三大独立隔离区间：**回溯序列（Backtrack Glyphs）**、**匹配目标序列（Input Glyphs）** 与 **前瞻序列（Lookahead Glyphs）**。只有当这三个区间的字形同时全部命中预设规则时，才对匹配目标区间内的指定字形执行级联替换，而回溯与前瞻字符保持完好，继续供下游规则链条匹配。
7. **反向链式上下文单字替换（Reverse Chaining Contextual Single Substitution, Lookup Type 8）**：专为乌尔都语（Urdu）波斯折体（Nastaliq）等极端书写系统量身定制。它逆转了常规文本扫描方向，从左至右逆向评估上下文，以适配从右向左书写且笔画沿对角线阶梯向下悬垂坍落的特殊文字。

#### 2. 字形微观几何定位的六大形态（GPOS）

如果说 `GSUB` 决定了“显示哪个字形”，那么 `GPOS` 则彻底掌控了“字形显示在何处”。在 `GPOS` 体系中，每一个字形的最终空间位置由一个四元值记录（Value Record）决定：

$$\langle xPlacement \quad yPlacement \quad xAdvance \quad yAdvance \rangle$$

* $xPlacement$ / $yPlacement$：字形轮廓相对于逻辑原点的水平与垂直偏移量（平移绘制起点，但不改变排版笔刷前进量）；
* $xAdvance$ / $yAdvance$：字形绘制完成后，文本排版光标在水平与垂直轴线上的推进距离（前进量，Advance Width/Height）。

围绕该值记录，`GPOS` 定义了六大空间几何定位查找表类型：
1. **单一微调（Single Adjustment, Lookup Type 1）**：针对单个字形调整其外形偏移或推进度量。
   * *典型场景*：全大写排版微调（Capital Spacing, `cpsp`），当文本全为大写字母时，将括号 `()`、连字符 `-` 和破折号 `--` 向上抬升若干设计单位，以对齐大写字母的垂直视觉中心。
2. **字偶对微调（Pair Adjustment / Kerning, Lookup Type 2）**：针对特定的两两相邻字形组合，微调它们之间的相对间隙。
   * *典型场景*：经典字距微调（`kern`），如在 `'T'` 与 `'o'`、`'A'` 与 `'V'` 之间施加负向水平间隙，消除笔画负空间造成的排版空洞。支持基于具体字形对（Glyph-pair）与基于形态类（Class-based）的矩阵运算。
3. **草书平滑咬合（Cursive Attachment, Lookup Type 3）**：专为阿拉伯文、波斯体（Nastaliq）以及手写连体设计。在每个字形的连线入口放置进入锚点（Entry Anchor），在出口放置退出锚点（Exit Anchor）。排版引擎在从右向左推进时，自动平移后一个字形，使后字的 Entry 锚点与前字的 Exit 锚点在空间中严格重合，形成平滑如行云流水的斜角或弧线连缀。
4. **标音符号附着于基字（Mark-to-Base Attachment, Lookup Type 4）**：将重音符号、声调或点标精准吸附于基本字母。
   * *典型场景*：在小写字母 `'e'` 的顶部中心锚点上吸附尖音符（Acute）`´`，使组合而成的 `é` 变音符无论基字字宽如何变化，均稳固居中。
5. **标音符号附着于合字（Mark-to-Ligature Attachment, Lookup Type 5）**：连字体字形内部包含多个文字成分。该查找表允许在合字内部为每个逻辑构件分别指定锚点集合，使变音符能够精准降落在合字的第一个或第二个组成字母上方。
6. **标音符号多层附着（Mark-to-Mark Attachment, Lookup Type 6）**：处理变音符号的层叠堆印。
   * *典型场景*：在越南语排印中，字母往往同时拥有元音变音符（如扬抑符 `^`）和声调符号（如锐音符 `´`），Mark-to-Mark 定位使声调符能够精准叠加在元音变音符的顶端，避免两者在垂直空间发生重叠穿模。

---

### 1.3 OpenType 布局表的底层二进制拓扑与关键基础设施

要透彻理解 OpenType 引擎的执行机理，必须深入解剖其在二进制文件中的数据拓扑结构。无论是 `GSUB` 还是 `GPOS` 表，其顶层均严格包含一个表头（Header）：
* `uint16 majorVersion` / `uint16 minorVersion`：版本标识符（通常 1.0 或 1.1）；
* `Offset16 ScriptListOffset`：指向脚本列表（ScriptList）的字节偏移量；
* `Offset16 FeatureListOffset`：指向特性列表（FeatureList）的字节偏移量；
* `Offset16 LookupListOffset`：指向查找表列表（LookupList）的字节偏移量；
* 在 1.1 版本中，还额外包含一个 `Offset32 FeatureVariationsOffset`，用于支持 OpenType 1.8 可变字体根据轴线坐标动态切换替换规则！

#### 1. 覆盖表（Coverage Tables）的两大格式规范
在任何一个查找子表中，排版引擎做的第一件事绝不是盲目遍历整个字库，而是通过**覆盖表（Coverage Table）**快速判断当前字形是否属于该子表的作用对象：
* **Coverage Format 1（离散索引表）**：包含一个按 GID 升序严格排列的字形数组 `GlyphID glyphArray[glyphCount]`。引擎通过二分查找法在 $O(\log N)$ 时间内判定当前字形是否存在，若存在则返回其在数组中的索引作为其覆盖索引（Coverage Index）；
* **Coverage Format 2（连续区间范围表）**：当被覆盖的字形在 GID 上是连续大块分布时（例如连续 500 个汉字变体），Format 1 会浪费巨量内存。Format 2 引入了范围记录结构 `RangeRecord`：
  ```c
  struct RangeRecord {
      uint16 startGlyphID;      /* 区间起始字形 GID */
      uint16 endGlyphID;        /* 区间终结字形 GID (包含) */
      uint16 startCoverageIndex;/* 该区间首个字形对应的覆盖索引 */
  };
  ```
  引擎仅需存储若干个区间端点，即可瞬间映射成千上万个连续字形，极大压缩了字体体积并提升了查找命中速度。

#### 2. 分类定义表（Class Definition Tables）
在基于类别的字距调整（Class-based Kerning）或上下文分类替换中，字形必须被离散投影到一个整数类索引（Class ID，通常 0 为默认未分类）：
* **ClassDef Format 1**：定义了一个基准起始字形 `startGlyphID`，紧随其后为一个紧凑的单字节/双字节类值数组 `uint16 classValueArray[glyphCount]`；
* **ClassDef Format 2**：采用三元组范围记录 `ClassRangeRecord`（`startGlyphID`, `endGlyphID`, `classValue`），高效对连续字符块赋予相同类别属性。

#### 3. GDEF、BASE 与 JSTF 支撑底座
* **`GDEF`（字形定义表）**：为全字体建立字形本体论属性分类。它包含三大核心子表：
  1. `GlyphClassDef`：将字形严格归类为 Base（基字）、Ligature（合字）、Mark（附加音标）或 Component（构件）；
  2. `AttachList`：记录特定复杂字形上允许其他字符连接的物理顶点轮廓节点号；
  3. `LigCaretList`：定义合字内部允许闪烁文本光标的垂直剖分位置（Carets），使得用户在文本编辑器中按向左箭头时，光标能精准停靠在 ‘ﬁ’ 合字中间 ‘f’ 与 ‘i’ 的交界处。
* **`BASE`（跨语系基线规范表）**：当多语言在同一水平行混排时，西文的基线是小写字母的底部，中文汉字采用正方形字身框垂直居中的表意字中线（Ideographic Baseline），而印度梵文天城文则以字母顶端的平直连梁为悬挂基线（Hanging Baseline）。`BASE` 表给出了各脚本基线之间的相对差值，使文本渲染器在混排拉丁字母与梵文时，能够自动上下平移字符，保持阅读视觉重心的绝对统一；
* **`JSTF`（两端对齐表）**：针对阿拉伯文等高难度脚本的两端齐平排版。定义了多级优先级流水线（Priority Stages）：在第一级，优先使用加长字形（Swashes）；在第二级，调用连线伸展字符（Kashida）；在第三级，微调词间距。

#### 4. 标准排版特性标签体系（Standard Feature Tags）

OpenType 官方注册表中定义了近百个由 4 字节 ASCII 字符构成的排版特性标签（Feature Tags）。表 14-1 汇总了当今出版界最核心的特性及其行为：

| 特性标签 | 英文全称 | 核心排印功能与转换行为 | 默认开启状态 |
| :--- | :--- | :--- | :--- |
| `liga` | Standard Ligatures | 标准审美连字（如 fi, fl, ffi, ffl） | 默认开启（ON） |
| `dlig` | Discretionary Ligatures | 装饰性/自由连字（如 st, ct, Qu, Th） | 默认关闭（OFF） |
| `hlig` | Historical Ligatures | 历史典籍珍本文献连字（如 ſt, ſi, ſl） | 默认关闭（OFF） |
| `smcp` | Lowercase to Small Caps | 小写字母转为真小型大写体（保持大写高度与磅重统一） | 默认关闭（OFF） |
| `c2sc` | Capitals to Small Caps | 大写字母转为小型大写体（用于缩写词头等混排场景） | 默认关闭（OFF） |
| `onum` | Oldstyle Figures | 非等高老式数字（高低错落，融入正文行气流） | 默认关闭（OFF） |
| `lnum` | Lining Figures | 等高全齐平现代数字（与大写字母齐平，适合标题） | 默认开启（标题） |
| `pnum` | Proportional Figures | 比例间距数字（各数字拥有符合自身骨架的自然字宽） | 默认开启（正文） |
| `tnum` | Tabular Figures | 表格等宽数字（所有数字宽度绝对一致，确保财务报表垂直对齐） | 默认开启（表格） |
| `frac` | Diagonal Fractions | 斜线对角分数（将 `1/2` 等序列自动转换为专业分数分子分母字形） | 默认关闭（OFF） |
| `ordn` | Ordinals | 序数词上标（如英语 1st, 2nd 或法语 1er, 2e） | 默认关闭（OFF） |
| `zero` | Slashed Zero | 斜杠零（在数字 0 中增加斜杠或圆点，与大写字母 O 严格隔离） | 默认关闭（OFF） |
| `swsh` | Swash | 书法飘逸花体（为字母提供长长延伸的书法出入刀笔画） | 默认关闭（OFF） |
| `titl` | Titling | 标题专用大写体（笔画细致，专门优化大磅字排版） | 默认关闭（OFF） |
| `kern` | Kerning | 字距微调（消除字母间负空间视觉缝隙） | 默认开启（ON） |
| `cpsp` | Capital Spacing | 全大写排版间距扩展与符号垂直抬升 | 默认关闭（OFF） |
| `locl` | Localized Forms | 本地语言定制字形（如土耳其语无点 i、波兰语 kreska 倾角） | 默认开启（强制） |

---


### 1.4 工业级西文经典排印四大数字体系与高级特性矩阵

数字在现代排印学中具有极其复杂的视觉层级需求。一款顶级的专业西文字体通常必须同时配备**四套截然不同的阿拉伯数字系统**，由 OpenType 特性按需调度：

#### 1. 西文四大数字体系的几何与功能对立
1. **等高齐线数字（Lining Figures, `lnum`）**：所有数字的高度严格齐平，且顶端与大写字母（Cap Height）或接近大写字高完全平齐，基底与普通字母基线对齐。适合与全大写字母混排、海报标题与大字标语。
2. **不等高老式数字（Oldstyle Figures / Non-lining Figures, `onum`）**：具有类似小写字母的升部（Ascender）与降部（Descender）。例如数字 `6` 与 `8` 向上伸展冲顶，`3`、`4`、`5`、`7`、`9` 向下伸出基线跌入降部区，而 `0`、`1`、`2` 则保持在 x 字高（x-Height）以内。老式数字在排印古典正文段落时，其墨迹灰度与小写行气浑然一体，绝不会像全齐线数字那样在大片正文中产生突兀扎眼的“黑斑”。
3. **比例间距数字（Proportional Figures, `pnum`）**：每个数字的字身外框（Bounding Box）与推进宽度（Advance Width）根据自身骨架量身定制。例如狭窄的数字 `1` 拥有极小的字宽，而丰满的数字 `0` 与 `8` 则拥有较宽的字身。比例数字使文字行具有匀称优美的自然节奏。
4. **表格等宽数字（Tabular Figures, `tnum`）**：所有 0 到 9 的数字，乃至小数点、逗号与美元货币符号，其推进宽度被强制锁定为完全相同的固定数值（例如 1000 设计单位字身框中的 550 单位）。在财务报表、资产负债表与统计图表中，只有表格等宽数字能够确保不同行之间的千位、百位与小数位实现如同机械游标卡尺般的绝对垂直纵向对齐！

#### 2. 花体修饰（Swashes）与样式集（Stylistic Sets）的高级调度
* **`swsh`（自由花体）与 `cswh`（上下文花体）**：古典书法花体字形若在单词中间随意出现，其长长的延伸笔画往往会与相邻字母发生严重的穿模碰撞。因此现代字体工程普遍使用 `cswh` 特性：通过上下文规则，仅在单词的首字母（词首花体）或最后一个字母（词尾收刀花体）处安全触发花体变体，中间字母自动回退为紧凑的常规形态；
* **样式集（`ss01` 至 `ss20`）**：允许字体设计师为整个字体打包提供多达 20 套独立的风格主题包。例如一套专门模仿包豪斯几何风格的几何无衬线大写集合（开启 `ss01`），或一套针对手写体字迹的粗糙墨晕风化变体集合（开启 `ss02`），用户可在排版软件中一键全局切换。


## 2. 在 FontLab 中管理 OpenType 表与 AFDKO 特性定义语言

在桌面字型设计软件演进史中，FontLab Studio 4 与 5 率先深度集成了由 Adobe 开发的 **AFDKO（Adobe Font Development Kit for OpenType）** 语法编译器 `makeotf`，开创了通过纯文本高级代码声明 OpenType 特性的现代工业范式。

### 2.1 AFDKO 特性定义语言的完整语法规范

AFDKO 语法采用类似于 C 语言与 PostScript 的大括号分块结构，每一条语句必须以分号（`;`）结尾。

#### 1. 字形类（Glyph Classes）的定义与集合运算

字形类是 AFDKO 代码的基石，以 `@` 字符为前缀。它将具有相同排印属性的多个字形绑定为一个具名集合：

```fea
# 1. 显式枚举定义
@LOWER_VOWELS = [a e i o u];

# 2. ASCII 字典序连续范围定义（使用连字符 -）
@UPPERCASE = [A-Z];
@DIGITS_LINING = [zero-nine];

# 3. 带特定前后缀的字形范围定义
@SMALL_CAPS = [a.sc-z.sc];
@FIGURES_OLDSTYLE = [zero.oldstyle-nine.oldstyle];

# 4. 类的嵌套与组合
@ALL_LETTERS = [@UPPERCASE @LOWER_VOWELS b c d f g h j k l m n p q r s t v w x y z];
```

#### 2. 书写系统、语言与特性的层级结构

字库必须首先声明支持的脚本（Script）与语言系统（Language System）：

```fea
languagesystem DFLT dflt;    # 兜底默认系统
languagesystem latn dflt;    # 拉丁脚本默认语言
languagesystem latn TRK ;    # 拉丁脚本土耳其语（支持点号 i 严格隔离）
languagesystem arab ARA ;    # 阿拉伯脚本阿拉伯语
languagesystem arab URD ;    # 阿拉伯脚本乌尔都语
```

在特性块定义中，排版师将具体的查找规则包裹在 `feature <tag> { ... } <tag>;` 中：

```fea
feature liga {
    # 查找规则写入此处
    sub f f i by f_f_i;
    sub f i by f_i;
    sub f l by f_l;
} liga;
```

#### 3. 命名查找表（Named Lookups）与标记标志位（`lookupflag`）

为了在不同特性之间复用规则，或精细控制规则的执行顺序与过滤条件，AFDKO 支持具名查找表：

```fea
lookup SMALL_CAPS_SUB {
    sub [a-z] by [a.sc-z.sc];
} SMALL_CAPS_SUB;

feature smcp {
    lookup SMALL_CAPS_SUB;
} smcp;
```

查找表可通过 `lookupflag` 指令直接控制底层渲染引擎的遍历过滤策略：
* `RightToLeft`：指示规则在从右向左文本流中应用；
* `IgnoreBaseGlyphs`：引擎在匹配上下文字符串时，自动跳过所有基字（仅在标记符号之间匹配）；
* `IgnoreLigatures`：自动跳过所有合字；
* `IgnoreMarks`：**工业级排印极其关键的指令**！指示排版引擎在扫描上下文时，自动无视插在字母中间的所有重音、声调与发音点标。例如，在处理带重音的法语单词时，`sub f i by f_i;` 即使中间插入了零宽重音符号，依然能够穿透标记成功触发连字！

#### 4. 字形替换规则（GSUB 规则全集）

AFDKO 覆盖了全部 6 种 GSUB 类型的代码写法：

```fea
# Type 1: 单字替换
sub a by a.sc;
sub @LOWERCASE by @SMALL_CAPS;

# Type 2: 多字拆分替换
sub f_f_i by f f i;

# Type 3: 备选替换（从数组中选其一，弹出交互菜单）
sub ampersand from [ampersand.alt1 ampersand.alt2 ampersand.swash];

# Type 4: 合字替换（注意长词优先原则，避免短序列提前截断）
sub f f l by f_f_l;
sub f l by f_l;

# Type 6: 链式上下文替换（使用单引号 ' 钉死目标输入区间）
# 规则示例 1：当且仅当前方是数字且后方是数字时，将连字符替换为短破折号
@digits = [ zero one two three four five six seven eight nine ];
sub @digits hyphen' @digits by endash;

# 规则示例 2：当小写 'd' 之后紧跟元音字母时，替换为更具流动感的 d.prettier 变体
sub d' [ a e i o u ] by d.prettier;

# 规则示例 3：著名的 TeX 标志上下文连字替换与 ignore 逆向排除技术！
# 目标：将独立的 "TEX" 字符串替换为专属的 T_e_X 标志字形，但在 "CONTEXT" 或 "PRETEXT" 中保持原样
ignore sub [ A-Z Eacute ] T' E' X' , T' E' X' [ A-Z Eacute ] ;
sub T' E' X' by T_e_X ;
```

上述 `ignore sub` 语法展示了 AFDKO 极其高超的上下文控制力：通过在 `ignore sub` 语句中用逗号隔开多个排除模式，先排除掉前驱带大写字母或后继带大写字母的所有单词，紧随其后的 `sub` 即可安全地将孤立的 "TEX" 融铸为精美的标志合字。

#### 5. 字形定位规则（GPOS 规则全集）

在 AFDKO 中，位置调整使用 `pos` 关键字声明：

```fea
# Type 1: 单字微调（四元值记录：<xPlacement yPlacement xAdvance yAdvance>）
# 将全大写排版中的圆括号向上抬升 50 单位，并将前进量向右扩展 50 单位
pos [parenleft parenright] <0 50 0 50>;

# Type 2: 字偶对字距微调（Kerning）
pos T -50 o -20;
# 基于类的字距调整：将大写 T 类与小写 o 类的所有组合施加 -80 单位压缩
pos @CAPS_T @LOWER_O -80;
# 使用 enum pos 显式展开矩阵：
enum pos [ T Tacute Tcaron ] [ a aacute acircumflex adieresis ] -50; # 瞬间展开为 3x4=12 对字距微调！

# Type 3: 草书连缀定位（定义进出锚点）
pos cursive beh.med <anchor 350 120> <anchor 0 100>;

# Type 4: 标音符号吸附于基字
markClass [ acute grave ] <anchor 0 0> @top_accents;
pos base o <anchor 250 500> mark @top_accents;

# Type 5: 标音符号吸附于合字（为合字的各个构件分别指定锚点）
pos ligature f_i <anchor 200 600> mark @top_accents ligComponent <anchor 400 700> mark @top_accents;

# Type 6: 标音符号多层重叠吸附（Mark-to-Mark）
pos mark circumflex <anchor 150 400> mark @top_accents;
```

#### 6. 光学尺寸特性（`size`）与备选汇总（`aalt`）

在所有 OpenType 特性中，有两个具有超脱于常规排版逻辑的特殊语法地位：
1. **`aalt`（All Alternates，全备选汇总）**：其唯一使命是将字库中分散在 `smcp`, `onum`, `salt`, `titl` 等各个独立特性中的所有单字替换变体进行集中大汇编，供 Adobe InDesign 等软件的“字形调板（Glyphs Panel）”一次性向用户展示当前字符的所有可用外观变体。它通常必须置于特性的最首行：
   ```fea
   feature aalt {
       feature smcp;
       feature c2sc;
       feature onum;
       feature salt;
   } aalt;
   ```
2. **`size`（光学尺寸元数据声明）**：用于弥补传统数字字体彻底抹杀金属活字“物理级磅重尺寸微调”的巨大缺陷。在 AFDKO 中，`size` 特性不包含任何字形替换或定位规则，而是包含四个核心工程浮点参数与一个多语言名称块：
   ```fea
   feature size {
       # 参数依次为：设计物理尺寸（点数的 10 倍，如 100 代表 10pt）、子家族识别码、推荐适用尺寸下限、推荐适用尺寸上限
       parameters 10.0 0 8.0 11.9;
       
       # 为支持此特性的操作系统提供本地化显示的尺寸家族名称（nameID 256+）
       featureNames {
           name 3 1 0x0409 "Regular (10pt Text)";  # Windows 英语
           name 3 1 0x040C "Texte standard (10pt)"; # Windows 法语
           name 1 0 0 "Regular (10pt Text)";       # Mac 英语
       };
   } size;
   ```

---

### 2.2 FontLab Studio 图形化工作流实战

在 FontLab Studio 中，排版师不仅可以直接编写上述底层 AFDKO 代码，更可以通过丰富的图形化视窗直观管理特性、类与视觉锚点：

::: tip FontLab 4/5 中的 OpenType 特性编辑视窗（Figure 14-1）
![FontLab 4/5 中的 OpenType 特性编辑视窗（Figure 14-1）](/images/fonts-encodings/fig14-1.png)
*FontLab 4/5 中的 OpenType 特性编辑视窗（Figure 14-1）*
:::

*图 14-1：FontLab 中的 OpenType 核心工作视窗。左侧为当前字库声明的排版特性列表（Feature Tags），右上为选定特性（如 `liga`）的 AFDKO 源码编辑区，右下为编译日志与错误输出控制台。*

::: tip FontLab 视窗中详细的特性与类管理界面（Figure 14-2, 14-3, 14-4）
![FontLab 视窗 OpenType 详细特性视窗（Figure 14-2）](/images/fonts-encodings/fig14-2.png)
*FontLab 视窗 OpenType 详细特性视窗（Figure 14-2）*
:::

*图 14-2：FontLab 中的 OpenType 特性管理视窗。展示了特性的启用依赖关系、脚本隔离与独立的查找表链。*

::: tip FontLab 视窗 Kerning 类矩阵选项卡（Figure 14-3）
![FontLab 视窗 Kerning 类矩阵选项卡（Figure 14-3）](/images/fonts-encodings/fig14-3.png)
*FontLab 视窗 Kerning 类矩阵选项卡（Figure 14-3）*
:::

*图 14-3：FontLab 的 OpenType 视窗中的 Kerning 标签页。展示了基于类的字距微调对与类矩阵分配。*

::: tip FontLab 视窗 Classes 字符类定义标签页（Figure 14-4）
![FontLab 视窗 Classes 字符类定义标签页（Figure 14-4）](/images/fonts-encodings/fig14-4.png)
*FontLab 视窗 Classes 字符类定义标签页（Figure 14-4）*
:::

*图 14-4：FontLab 视窗中的 Classes 标签页。展示了字型设计师如何将数十个重音变体归入同一形态类，并在右侧文本框中直观预览所属字形。*

::: tip FontLab 实时交互排版预览视窗（Figure 14-5）
![FontLab 实时交互排版预览视窗（Figure 14-5）](/images/fonts-encodings/fig14-5.png)
*FontLab 实时交互排版预览视窗（Figure 14-5）*
:::

*图 14-5：FontLab 的 Preview Panel（实时预览面板）。设计师可在面板中直接实时输入任意长文本字符串，并自由勾选开启或关闭特定的 OpenType 特性（如 liga、onum、kern），即时检验特性编译后的动态渲染效果。*

#### FontLab 视觉锚点（Anchors）管理法
在 FontLab 单字编辑窗口中，用户可通过右键菜单选择 `Add Anchor` 创建一个带红色十字光标的锚点：
* 在字母基字（如 `o`）上方放置一个名为 `top` 的锚点；
* 打开波浪变音符（`tilde`）窗口，在其底部关键位置放置一个名为 `_top` 的锚点（**关键规范：必须以下划线 `_` 开头且后接基字完全相同的锚点名**）；
* 当设计师打开 `Window > Panels > Preview` 视窗并切换至 `Anchors` 选项卡时，FontLab 会自动计算这两个坐标之间的向量相对位移，实时展现变音符在基字上的完美吸附效果！

---


### 2.3 工业级 AFDKO 特性文件的高阶架构设计模式

在开发涵盖数万字形的大型泛东亚（CJK）字库或巨型西文排版大系时，单体 `.fea` 特性文件往往会膨胀到数万行。现代工业字型工程普遍采用模块化架构模式：

#### 1. 宏替换与文件包含（Include Directives）
AFDKO 支持类似于 C 语言预处理器的 `include()` 指令：
```fea
# 主特性入口文件：features.fea
include(classes.fea);
include(tables/gsub_lookups.fea);
include(tables/gpos_kerning.fea);

languagesystem DFLT dflt;
languagesystem latn dflt;

include(features/liga.fea);
include(features/smcp.fea);
include(features/onum.fea);
include(features/cpsp.fea);
```

#### 2. 条件编译与脚本分流（Script Sub-routing）
在大型字库中，同一特性在不同语言体系下需要表现出差异化的排版行为。例如在土耳其语、阿塞拜疆语与克里米亚鞑靼语中，拉丁字母 `'i'` 拥有大写的带点 `'İ'`（U+0130）与小写的无点 `'ı'`（U+0131），与常规英语中大写 `'I'` 变为小写 `'i'` 的规则彻底冲突！
在 AFDKO 中，排版师必须利用 `script` 与 `language` 分支实现精密的语系隔离：

```fea
feature locl {
    # 针对拉丁脚本、土耳其语系统的专属隔离规则
    script latn;
    language TRK exclude_dflt;
        sub i by i.dotaccent;
        sub I by I.nodot;
        
    language AZE exclude_dflt; # 阿塞拜疆语
        sub i by i.dotaccent;
        sub I by I.nodot;
        
    # 针对罗马尼亚语与摩尔多瓦语的逗号重音（Comma-below）隔离
    language ROM exclude_dflt;
        sub Scedilla by Scommaaccent;
        sub scedilla by scommaaccent;
        sub Tcedilla by Tcommaaccent;
        sub tcedilla by tcommaaccent;
} locl;
```

#### 3. 连字截断陷阱与拓扑偏序原则（Topological Subsumption）
在编写 `GSUB Type 4`（合字替换）时，若规则书写顺序不当，排版引擎会按照“先入为主”的原则提前消耗前缀字符，导致更长的合字永远无法被触发！
* **致命错误顺序**：
  ```fea
  sub f i by f_i;
  sub f f i by f_f_i; # 永远死锁！引擎在读到 'f' + 'f' + 'i' 时，在遇到 'f' + 'i' 时已将后两字吃掉合成为 f_i，从而产生 'f' + 'f_i'，三重连字被永久截断！
  ```
* **工业级标准偏序**：
  ```fea
  # 必须严格遵循“自长至短（Longest Match First）”的偏序排列：
  sub f f l by f_f_l;
  sub f f i by f_f_i;
  sub f f by f_f;
  sub f l by f_l;
  sub f i by f_i;
  ```


## 3. 在微软 VOLT 中可视化构建 OpenType 排版表（Managing OpenType Tables in VOLT）

与 Adobe 基于纯文本代码编译的 AFDKO 路线不同，微软推出了重量级的纯图形化开发环境——**VOLT（Visual OpenType Layout Tool）**。VOLT 曾承担了包括 Windows 系统中全部阿拉伯文、希伯来文、泰文以及印度数十种复杂地方官方文字字库的排版工程研发。

### 3.1 VOLT 的架构哲学与私有数据表

VOLT 并不直接解析或生成 AFDKO 代码，而是在 TrueType 字体二进制内部开辟了一组私有数据表：
* `TSVT`：VOLT 项目主拓扑与工程设置表；
* `TSVC`：字符类定义表；
* `TSVG`：字形命名、Unicode 映射与元数据；
* `TSVP`：定位与查找表参数。

当排版师在 VOLT 中完成全部可视化规则编排并点击“Compile”后，VOLT 内部的编译器会将这套私有拓扑一键编译为标准的工业级二进制 `GSUB`、`GPOS` 和 `GDEF` 表。而在字库发布阶段，设计师可以选择执行“Ship Font”，彻底剥离这组体积庞大的私有表，仅保留纯净的标准 OpenType 布局表。

::: tip 微软 VOLT 工程主项目控制视窗（Figure 14-6）
![微软 VOLT 工程主项目控制视窗（Figure 14-6）](/images/fonts-encodings/fig14-6.png)
*微软 VOLT 工程主项目控制视窗（Figure 14-6）*
:::

*图 14-6：微软 VOLT 主项目视窗。从上至下清晰展现了字符字形映射（Glyphs）、字符类矩阵（Classes）、排版特性（Features）与底层查找表（Lookups）的层级依赖拓扑。*

#### VOLT 标准操作流
1. **打开字体与数据重置**：点击 `Open` 载入字体。**重要警告**：此操作会完全抹除字体内所有由其他工具生成的非 VOLT OpenType 表！
2. **导入 PostScript 字形名称**：TrueType 原生字形仅有 GID 数字编号，点击 `Import > Import PostScript Names` 自动从 `post` 表导入具名符号；
3. **分配 GDEF 字形类型**：进入 `Tools > Edit Glyphs`，为每个字形赋予 Single glyph、Ligature、Mark 或 Component 类型，并注明合字包含的部件数量；
4. **添加脚本、语言与特性**：点击 `Add Script` 输入 `<latn>` 等四字标签，接着点击 `Add Language` 选择 `<dflt>`，最后点击 `Add Feature` 输入 `<liga>` 建立排版特性插槽。

### 3.2 查找表与规则编辑

#### 1. 替换规则的可视化与箭头语法

双击任一替换查找表，即可进入直观的字形替换网格视窗：

::: tip VOLT 中字形替换查找表的可视化配置视窗（Figure 14-7）
![VOLT 中字形替换查找表的可视化配置视窗（Figure 14-7）](/images/fonts-encodings/fig14-7.png)
*VOLT 中字形替换查找表的可视化配置视窗（Figure 14-7）*
:::

*图 14-7：VOLT 中查找表（Lookup）编辑视窗。展示了可视化的替换规则映射网格，支持通过直观的箭头拖拽定义输入字符序列到目标字形的变换映射。*

排版师可以直接在网格左侧输入基准字形名或字形类，右侧输入目标替换字形名，甚至通过 `[ zero - nine ] | [ zero - nine ]` 的上下文分割竖线语法建立高阶替换，VOLT 会在后台自动完成覆盖表格式的离散划分与索引二分查找树优化。

#### 2. 定位规则与交互式锚点吸附（Visual Anchor Attachment）

在定位规则编辑视窗中，VOLT 提供了强大的双重视窗联动：

::: tip VOLT 中的草书锚点与二维空间定位视窗（Figure 14-8）
![VOLT 中的草书锚点与二维空间定位视窗（Figure 14-8）](/images/fonts-encodings/fig14-8.png)
*VOLT 中的草书锚点与二维空间定位视窗（Figure 14-8）*
:::

*图 14-8：VOLT 的定位（Positioning）编辑视窗。展示了在阿拉伯文字形上交互式放置进入锚点（Entry）与退出锚点（Exit），实时观察两字沿斜角咬合的力学状态。*

视窗左侧定义参与定位的字形对或字形类，右侧则以图形画布展现两个字符在当前锚点下的拼接状态。设计师可直接用鼠标拖动锚点十字星，画布上的两个字符会实时响应吸附位移，极大地降低了复杂草书连缀的数学心智负担。

### 3.3 VOLT 校对工具（Proofing Tool）与实战

在复杂书写系统排版中，一个输入字符串可能会连续激发数十个级联查找表。一旦某个查找表发生逻辑死锁或意外截断，在成品文本中极难排查根因。VOLT 配备了享誉业界的交互式校对检验工具（Proofing Tool）：

::: tip VOLT 复杂脚本交互式校对与排印预览视窗（Figure 14-9）
![VOLT 复杂脚本交互式校对与排印预览视窗（Figure 14-9）](/images/fonts-encodings/fig14-9.png)
*VOLT 复杂脚本交互式校对与排印预览视窗（Figure 14-9）*
:::

*图 14-9：VOLT 交互式校对检验视窗（Proofing Window）。在复杂的阿拉伯文与乌尔都语长句排版中，实时展示当前应用的查找表执行轨迹链条。*

在校对视窗中输入长文本字符串后，VOLT 会在下方逐条打印执行报告（Execution Trace）：哪一个查找表在第几个字符上命中、输入字形被转化为什么中间 GID、哪些标记符号被忽略、光标坐标被累加了多少偏移量。排版师可以像使用调试器单步跟踪代码一样，一帧一帧地检查整个排版管线的状态跃迁。

### 3.4 工业级挑战：乌尔都语波斯折体（Nastaliq）在 VOLT 中的排版工程全景

波斯折体（Nastaliq）被公认为全人类排印技术皇冠上的明珠。它拥有极其严苛、甚至是违反直觉的排印物理学定律：
1. **级联阶梯倾斜跌落（Cascading Stems）**：在一个词内部，每一个字母不是水平排在后方，而是跌落在前一个字母的左下后方，整词呈现为从右上向左下以约 $45^\circ$ 倾斜的悬垂阶梯；
2. **点标自适应避让（Dynamic Dot Placement）**：阿拉伯辅音字母带有单个、成对或三个发音点标（Nuqta）。由于字形随上下文不断升降，点标必须根据邻近笔画的空间拓扑，动态在空间中上下平移移动，绝对不可与邻近字母发生笔画穿模碰撞；
3. **笔画死结反向嵌套**：后方的字母尾部可能会向左下深远回勾，穿插进前一个字母内部的负空间中。

在微软著名的《Urdu Typesetting》项目中，VOLT 展现了不可替代的统治力：
* **第一步：上下文形态拆解与合字替换**：通过大量的 GSUB Type 4（Ligature）与 Type 6（Chained Contextual），将上千种高频两字、三字辅音组合预先熔铸为独立的倾斜整体；
* **第二步：草书锚点精确咬合**：使用 GPOS Type 3（Cursive Attachment），在每一个字形的入刀点（Entry）与出刀点（Exit）放置精确锚点。排版引擎在从右向左排版时，自动将后字的 Entry 锚点与前字的 Exit 锚点在空间中对齐，从而自然形成了全单词平滑连贯的 $45^\circ$ 阶梯跌落！
* **第三步：反向链式上下文（GSUB Type 8）动态修剪**：当词尾字母具有长长的水平回勾大弧线时，通过 Type 8 反向扫描前方词干的高度层级，动态将词尾替换为不同长度与深度的回弯变体；
* **第四步：多层点标避让附着（GPOS Type 4 与 Type 6）**：为每个辅音字形配置上中下多个等级的候选锚点，并通过上下文定位规则检测下沉深度，自动将发音点标推向不受阻挡的安全视觉区域。

---


### 3.5 VOLT 查找表拓扑与依赖图（Lookup Dependency DAG）

在微软 VOLT 中组织上百个查找表时，排版师必须将其构建为一个严格的有向无环图（Directed Acyclic Graph, DAG）。每个查找表绝非孤立存在，而是遵循严密的依赖注入机制：
1. **预处理查找表（Preprocessing Lookups）**：负责将 Unicode 原始码点清洗为字库规范基字（Canonical Forms）。例如消除多重零宽空格（ZWNJ/ZWJ）带来的码点漂移；
2. **形态重构查找表（Morphological Analysis）**：依次执行词首（`init`）、词中（`medi`）、词尾（`fina`）孤立（`isol`）四态判定；
3. **连字坍缩查找表（Ligature Formation）**：自长至短逐级合并；
4. **后处理修剪查找表（Post-processing Trimming）**：针对特定字尾进行反向伸展修剪；
5. **空间几何吸附（Spatial Anchoring）**：在所有字形形态彻底定型之后，启动 GPOS 查找表链，依次执行基线平移、字偶间隙、草书咬合与标音吸附。

在处理包含多套变音符号的古代文献字体时，VOLT 的锚点系统支持多达 16 层的递归附着。排版师通过在基字上配置 `TopAnchor`、`BottomAnchor`、`RightAnchor`、`LeftAnchor`，并在变音符上配置配对的 `_TopAnchor`、`_BottomAnchor` 等，实现了全自动的二维网格化字母装配流水线。


## 4. 在 FontForge 中管理 OpenType 表（Managing OpenType Tables in FontForge）

作为自由开源阵营的代表，FontForge（George Williams 主导开发）提供了一套极其贴近底层 TrueType/OpenType 二进制数据结构的排版表管理环境。

### 4.1 核心控制台：Element > Font Info > Lookups

在 FontForge 中打开 `Element > Font Info`，并导航至 `Lookups` 选项卡。这是 FontForge 管理高级排版功能的中枢神经系统。该界面清晰地将整个字体内部的排版规则划分为两大并行视窗：
* `GSUB` 树状节点：展示所有字形替换查找表；
* `GPOS` 树状节点：展示所有字形定位查找表。

用户点击 `Add Lookup` 按钮时，FontForge 会弹出一个严谨的类型配置对话框，列出标准 OpenType 规范支持的全部查找表类型（Single, Multiple, Alternate, Ligature, Contextual, Chained Contextual, Pairwise, Cursive, Mark-to-Base, Mark-to-Ligature, Mark-to-Mark）。每一个查找表下方，可以进一步挂载一个或多个子表（Subtables）。

### 4.2 锚点体系与类定义（Anchor Classes）

::: tip FontForge 中的锚点与锚点类编辑视窗（Figure 14-10）
![FontForge 中的锚点与锚点类编辑视窗（Figure 14-10）](/images/fonts-encodings/fig14-10.png)
*FontForge 中的锚点与锚点类编辑视窗（Figure 14-10）*
:::

*图 14-10：FontForge 中锚点系统的定义。左侧为单字编辑视窗中直观放置的具名锚点（Named Anchors）；右侧为锚点类定义窗口，清晰展示了基字锚点与标记符号锚点的配对关系。*

FontForge 将锚点严格组织为**锚点类（Anchor Classes）**：
1. 在 `Font Info > Contextual` 中创建一个锚点类，例如命名为 `TopAccent`；
2. 为该类指定查找表类型为 `Mark to Base`；
3. 打开基字（如字符 `a`），选择 `Point > Add Anchor`，类型选择 `Base`，归入 `TopAccent` 类，拖动到字符顶部中心；
4. 打开重音变体字形（如 `grave`），新建锚点选择 `Mark`，同样归入 `TopAccent` 类，拖动到重音符号基底部；
5. FontForge 会在后台自动完成两者在 `GPOS` Format 1 表中的坐标偏移矩阵换算。

### 4.3 非上下文替换与定位

在单字编辑视窗中，设计师可以通过标签页直观配置简单的非上下文规则：

::: tip FontForge 非上下文替换与定位编辑（Figure 14-11, 14-12）
![FontForge 非上下文替换视窗（Figure 14-11）](/images/fonts-encodings/fig14-11.png)
*FontForge 非上下文替换视窗（Figure 14-11）*
:::

*图 14-11：FontForge 的非上下文替换视窗。左侧展示了单字替换（Single Substitution）标签页，右侧为新建替换规则的参数对话框。*

::: tip FontForge 单字与字偶对定位视窗（Figure 14-12）
![FontForge 单字与字偶对定位视窗（Figure 14-12）](/images/fonts-encodings/fig14-12.png)
*FontForge 单字与字偶对定位视窗（Figure 14-12）*
:::

*图 14-12：FontForge 的简单单字定位（左）与成对字距定位（右）窗口。*

在字距调整（Kerning）视窗中，FontForge 支持成组导入字形类矩阵。设计师可以将包含相同左侧或右侧轮廓特征的字母归类，大大削减需要人工填写的数值单元格总数。

### 4.4 链式上下文排版向导（Chained Contextual Lookups）

在 OpenType 各种查找表中，链式上下文替换与定位由于涉及回溯（Backtrack）、匹配（Match）与前瞻（Lookahead）三大字符区间的逻辑嵌套，手动编写容易产生死循环。FontForge 专门设计了一个四步向导流程：

::: tip FontForge 中定义链式上下文替换的前四步流程（Figure 14-13）
![FontForge 中定义链式上下文替换的前四步流程（Figure 14-13）](/images/fonts-encodings/fig14-13.png)
*FontForge 中定义链式上下文替换的前四步流程（Figure 14-13）*
:::

*图 14-13：在 FontForge 中定义链式上下文替换（Chained Contextual Substitution）的四步引导流程：(a) 选择特性标签；(b) 设定覆盖表类型；(c) 定义回溯、匹配输入与前瞻字符序列覆盖集；(d) 绑定对应的子查找表索引。*

向导执行逻辑：
1. **步骤 (a)**：选定触发该规则的目标特性标签（如 `calt` 或 `liga`）以及适用的语言系统；
2. **步骤 (b)**：选择覆盖表格式（Coverage Format 1 针对离散字形枚举，Format 2 针对连续区间）；
3. **步骤 (c)**：定义三大字符区间的字形或字形类序列。排版师在 Backtrack 列表中输入前置字符类，在 Match 列表中输入当前需要被替换的字符，在 Lookahead 列表中输入后续触发条件；
4. **步骤 (d)**：为 Match 序列中的每一个指定槽位，绑定预先建立好的简单替换（Single Substitution）或定位子查找表。引擎运行时在匹配到整体上下文后，即对目标槽位实施调用的子动作。

---


### 4.5 实战案例：使用链式上下文覆盖表构建英文序数词（Ordinals）自动化排版

在英文正文排版中，序数词格式有着极其严苛的规则：
* 词尾为 1 的数字（除 11 外）后接 `st`（如 1st, 21st, 101st）；
* 词尾为 2 的数字（除 12 外）后接 `nd`（如 2nd, 22nd, 102nd）；
* 词尾为 3 的数字（除 13 外）后接 `rd`（如 3rd, 23rd, 103rd）；
* 其余所有数字（包括 11, 12, 13）均后接 `th`（如 4th, 11th, 12th, 13th, 20th）。
优秀的字体应当在用户输入普通文本时，自动将 `st`, `nd`, `rd`, `th` 提升为优美的上标字形（Superscript），同时保持数字本身为常规字形。

在 FontForge 中，我们通过以下四步向导精确实现：
1. **第一步：建立底层非上下文单字替换子表**：
   在 `sups` 特性下，新建一个单字替换查找表，将常规字母映射为其上标变体：
   `s -> s.superior`, `t -> t.superior`, `n -> n.superior`, `d -> d.superior`, `r -> r.superior`, `h -> h.superior`。
2. **第二步：划分覆盖表集合（Coverage Tables）**：
   为避免规则碰撞，我们将字符划分为独立的覆盖集合：
   * `Cov_Digit1`：`[one]`；
   * `Cov_Digit2`：`[two]`；
   * `Cov_Digit3`：`[three]`；
   * `Cov_DigitsOther`：`[zero four five six seven eight nine]`；
   * `Cov_Teen1`：`[one]`（用于匹配十位上的 1）；
   * `Cov_st`：`[s]`, `[t]`；
   * `Cov_nd`：`[n]`, `[d]`；
   * `Cov_rd`：`[r]`, `[d]`；
   * `Cov_th`：`[t]`, `[h]`。
3. **第三步：配置链式上下文匹配规则（Chained Contextual Rules）**：
   在向导的 (c) 与 (d) 视窗中，我们定义多条互斥的匹配链条：
   * *规则 1（处理 11th, 12th, 13th 特例）*：
     * **Backtrack 序列**：`Cov_Teen1`；
     * **Match 序列**：`[one two three]`（索引 0） + `[t]`（索引 1） + `[h]`（索引 2）；
     * **调用的子查找表**：仅在索引 1 与索引 2 上调用 `sups` 单字替换！索引 0（数字）不被修改；
   * *规则 2（常规 1st）*：
     * **Backtrack 序列**：无或 `[zero two-nine]`；
     * **Match 序列**：`Cov_Digit1`（索引 0） + `[s]`（索引 1） + `[t]`（索引 2）；
     * **调用的子查找表**：在索引 1 和 2 上调用 `sups`；
   * *规则 3（常规 2nd）*：
     * **Match 序列**：`Cov_Digit2` + `[n]` + `[d]` 并在 `nd` 上调用 `sups`；
   * *规则 4（常规 3rd）*：
     * **Match 序列**：`Cov_Digit3` + `[r]` + `[d]` 并在 `rd` 上调用 `sups`；
   * *规则 5（兜底 4th..0th）*：
     * **Match 序列**：`Cov_DigitsOther` + `[t]` + `[h]` 并在 `th` 上调用 `sups`。

通过这种“覆盖集嵌套 + 槽位绑定”的精妙结构，FontForge 编译生成的 `GSUB Format 6` 表具有最高等级的执行效率与鲁棒性。


## 5. 在 FontForge 中构建苹果高级排版（AAT）有限状态机（Managing AAT Tables in FontForge）

在数字排版技术的另一座技术巅峰上，伫立着苹果公司的 **Apple Advanced Typography（AAT）**。AAT 源于 1990 年代初苹果研发的 TrueType GX 架构，在苹果操作系统生态中（macOS、iOS）拥有最顶级的底层原生支持。

### 5.1 AAT 与 OpenType 的计算理论对决

OpenType 与 AAT 代表了计算机科学中两种完全不同的计算哲学路线：
* **OpenType 的“声明式模式匹配”路线**：将字体排版视为一系列声明式的图重写规则集合（Graph Rewriting Rules）。排版引擎在运行时加载字符串，像一个多遍历扫描器一样，一遍遍扫描整段文本，按顺序匹配查找表。其优点是规则逻辑直观、易于移植；但缺点是在处理复杂上下文时，引擎必须往复扫描字符串，且容易发生规则顺序依赖与歧义碰撞。
* **AAT 的“确定性有限状态自动机（DFA / FST）”路线**：AAT 认为，**文本流在排版引擎中的流动本质上是一个时间序列信号**！任何上下文条件替换、字距微调与连字融铸，都可以严格抽象为一个**有限状态转换器（Finite State Transducer, FST）**。字库内部存储的不是分散的规则碎片，而是一张结构严密的二维状态转移矩阵。

### 5.2 特性与选择器命名体系（Features and Selectors）

与 OpenType 使用晦涩的 4 字符 ASCII 缩写标签（如 `smcp`, `onum`）不同，AAT 采用两级整数分层架构：**特性类型（Feature Type）** 与 **特性选择器（Feature Selector）**。
更具颠覆性的是：**AAT 将排版特性的多语言本地化显示名称直接存储在字库内部的 `feat` 表中**！任何排版软件无需更新应用程序代码，只需读取字库自身的 `feat` 表，即可自动在界面下拉菜单中向用户渲染出由字体设计师亲自编写的母语选项（如“连字开启”、“斜线分数”、“老式数字”）。

::: tip AAT 特性与选择器多语言名称编辑（Figure 14-14）
![AAT 特性与选择器多语言名称编辑（Figure 14-14）](/images/fonts-encodings/fig14-14.png)
*AAT 特性与选择器多语言名称编辑（Figure 14-14）*
:::

*图 14-14：FontForge 中编辑 AAT 特性与选择器名称界面。展示了在 `feat` 表中为特定排版特性（如连字特性、数字样式）配置法语、英语等多语言本地化显示标签。*

### 5.3 AAT 状态机四大核心操作（Font Info > Mac SM）

::: tip AAT 状态机类表与状态转移矩阵视窗（Figure 14-15）
![AAT 状态机类表与状态转移矩阵视窗（Figure 14-15）](/images/fonts-encodings/fig14-15.png)
*AAT 状态机类表与状态转移矩阵视窗（Figure 14-15）*
:::

*图 14-15：FontForge 中 AAT 状态机类表与状态转移矩阵输入视窗。(a) 输入类表分配；(b) 状态转移矩阵视窗，表格每一行代表一个机器状态，每一列代表输入类别，单元格内标明目标状态与触发动作。*

在 FontForge 中打开 `Font Info > Mac SM`，可以构建 AAT 的四大状态自动机：

#### 1. 字形重排状态机（Glyph Rearrangement）
专用于印度系与东南亚文字中辅音与元音的物理时空重排。例如在孟加拉文或高棉文中，输入序列为辅音 $C$ 接元音 $V$，但在视觉呈现上元音符号必须出现在辅音左侧。状态机在扫描到辅音时将其压入内部暂存槽，在扫描到元音时触发重排动作，直接在底层输出流中对调两者的绘制次序。

#### 2. 上下文替换状态机（Contextual Substitution）
以对角线专业分数（Fractions，如 `1/2`）的排版为例，AAT 的状态机设计堪称工程典范：
1. **输入类别划分**：
   * 类别 0：End of text（文本终结符）；
   * 类别 1：Out of bounds（越界符）；
   * 类别 2：Non-digits（非数字字符）；
   * 类别 3：Slash（斜杠字符 `/`）；
   * 类别 4：Digits（数字字符 `0-9`）。
2. **状态机状态转移规划**：
   * **状态 0（Start of text）**：若读取到类别 4（数字），勾选 `Mark Current Glyph`（标记当前字形），跃迁至**状态 2（Seen Numerator）**；若读取到其他字符，保持状态 0；
   * **状态 2（Seen Numerator）**：若继续读取到数字，保持状态 2；若读取到类别 3（斜杠），跃迁至**状态 3（Seen Slash）**；若读取到非数字，重置回状态 0；
   * **状态 3（Seen Slash）**：若读取到类别 4（数字），立刻触发双重动作：将此前被标记的字符替换为**分子字形（Numerator Glyph）**，将当前的斜杠替换为**对角分数线（Fraction Slash）**，并将当前数字替换为**分母字形（Denominator Glyph）**！状态跃迁至**状态 4（Seen Denominator）**；
   * **状态 4（Seen Denominator）**：若后续继续出现数字，直接替换为分母字形；一旦遇到非数字，重置回到状态 0。

#### 3. 字形动态插入状态机（Glyph Insertion）
AAT 独树一帜的杀手级功能。在 OpenType 中，替换只能是一对一或多对一，无法凭空向文本流中注入全新字形。而在 AAT 中，状态机允许在当前字形与标记字形之间**动态插入全新字形**！
* *阿拉伯文两端对齐伸展线（Kashida Insertion）*：排版引擎在扫描到阿拉伯字母单词内部合法的伸展断点时，状态机自动插入一个或多个连线拉伸字形（Kashida），而无需更改原始文本的逻辑字符序列；
* *高棉文/柬埔寨文笔画分裂*：当扫描到复杂的环绕元音时，自动在辅音前后插入对应的括号式分离部件。

#### 4. 上下文扩展字距状态机（Contextual Kerning / `kerx`）
苹果在 AAT `kerx` 表中实现了一次性对多达 **8 个字符** 同时施加跨字符字距调整的惊人能力！
例如处理带标点的西文缩写，如 `"S.A.V."` 或 `"A.V"`：
传统 OpenType 的 `kern` 表只能处理两两相邻的字符对（Pair Kerning），面对 `'A'` 与 `'V'` 之间被一个实心句号 `'.'` 隔开的场景束手无策，导致 `'A'` 与 `'.'`、`'.'` 与 `'V'` 的间距无法联动微调。
而在 AAT 状态机中：
1. 状态机配备了一个深度为 8 的硬件回溯栈（Push Current Glyph）；
2. 当扫描到 `'A'` 时，执行 `Push`；扫描到 `'.'` 时，继续 `Push`；当扫描到 `'V'` 时，触发弹出（Pop）；
3. 状态机在弹出 $n$ 个压栈字符的同时，**一步同时向这组序列施加 $n-1$ 个相互关联的字距调整偏移矩阵**！从而在字母跨越标点符号时，依然能够实现完美平滑的视觉负空间咬合。

---


### 5.6 AAT 状态机完整二维转移矩阵与对角分数算法执行跟踪

为了彻底阐明 AAT 有限状态自动机的工程实现，表 14-2 给出了构建专业斜线分数（Diagonal Fractions）时，AAT `morx` 表内部由编译器生成的完整状态转移矩阵：

| 状态（State） | 类别 0（End of Text） | 类别 1（Out of Bounds） | 类别 2（Non-digits） | 类别 3（Slash `/`） | 类别 4（Digits `0-9`） |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **State 0（文本起始 / 待机）** | State 0 (无动作) | State 0 (无动作) | State 0 (无动作) | State 0 (无动作) | **State 2** (标记当前字形为分子起点 `MarkFirst`, 推进) |
| **State 1（行起始）** | State 0 (无动作) | State 0 (无动作) | State 0 (无动作) | State 0 (无动作) | **State 2** (标记当前字形为分子起点 `MarkFirst`, 推进) |
| **State 2（已读入分子数字）** | State 0 (无动作) | State 0 (无动作) | State 0 (无动作) | **State 3** (推进指针，等待分母) | **State 2** (继续累计分子数字，推进) |
| **State 3（已读入斜杠）** | State 0 (回滚无动作) | State 0 (回滚无动作) | State 0 (回滚无动作) | State 0 (回滚无动作) | **State 4** (触发级联三动作：替换标记为分子、替换斜杠为分数线、替换当前为分母，推进) |
| **State 4（已读入分母数字）** | State 0 (重置) | State 0 (重置) | State 0 (重置) | State 0 (重置) | **State 4** (替换当前为分母，推进) |

#### 实战执行轨迹跟踪（Trace Analysis）
假设用户在键盘上输入字符串：`"Weight 12/34 kg"`：
1. 字符 `'W'`, `'e'`, `'i'`, `'g'`, `'h'`, `'t'`, `' '` 属于**类别 2（Non-digits）**。状态机恒定保持在 **State 0**，不做任何字形改写；
2. 扫描到字符 `'1'`（类别 4）：命中单元格 `(State 0, Class 4)`，机器将字符 `'1'` 的内存地址压入 `MarkRegister`，状态跃迁至 **State 2**；
3. 扫描到字符 `'2'`（类别 4）：命中单元格 `(State 2, Class 4)`，状态保持在 **State 2**；
4. 扫描到字符 `'/'`（类别 3）：命中单元格 `(State 2, Class 3)`，状态跃迁至 **State 3**（此时斜杠暂不替换，防止后续不是数字时误伤常规除号！）；
5. 扫描到字符 `'3'`（类别 4）：命中单元格 `(State 3, Class 4)`，瞬间激发三重复合替换动作：
   * 将 `MarkRegister` 中的 `'1'` 与 `'2'` 替换为分子字形 `1.numerator`, `2.numerator`；
   * 将前一个字符 `'/'` 替换为专业对角分数线 `fraction`（U+2044）；
   * 将当前字符 `'3'` 替换为分母字形 `3.denominator`；
   * 状态跃迁至 **State 4**；
6. 扫描到字符 `'4'`（类别 4）：命中单元格 `(State 4, Class 4)`，将 `'4'` 替换为分母字形 `4.denominator`，状态保持在 **State 4**；
7. 扫描到字符 `' '`（类别 2）：命中单元格 `(State 4, Class 2)`，状态机平稳重置回 **State 0**。

整个识别与全套三段式字形替换过程，在排版引擎单向遍历文本流的过程中**一气呵成、零回溯、零重扫**，其数学逻辑的自洽与优雅堪称软件工程的奇迹！


### 5.4 AAT 有限状态自动机的数学本质与算法复杂度

从形式语言与自动机理论（Formal Language & Automata Theory）的角度审视，AAT 的状态机是一个严格定义的六元组（6-tuple）：

$$M = \langle Q, \, \Sigma, \, \Gamma, \, \delta, \, q_0, \, F \rangle$$

* $Q$：有限状态集合 $\{s_0, s_1, \dots, s_{k-1}\}$。其中 $s_0$ 恒定为起始状态（Start of text），$s_1$ 为行起始状态（Start of line）；
* $\Sigma$：有限输入字符表，即由类定义表（Class Table）投影得出的字形类别集合 $\{0, 1, \dots, C-1\}$；
* $\Gamma$：有限输出操作集合（替换字形、设置标记、压栈、出栈、位移）；
* $\delta: Q \times \Sigma \to Q \times \Gamma$：**状态转移与动作执行函数**，在物理上被编码为一个大小为 $|Q| \times |\Sigma|$ 的紧凑二维矩阵；
* $q_0 \in Q$：初始状态；
* $F \subseteq Q$：接受状态集合。

#### 为什么 AAT 在理论上具有绝对的性能优势？
在 OpenType 引擎中，每个查找表（Lookup）是一个独立的匹配器。排版引擎必须在整段文本中逐字扫描；若有 30 个查找表，引擎必须对文本进行多达 30 轮的往复遍历扫描，算法复杂度为 $O(K \cdot N)$（$K$ 为查找表数量，$N$ 为文本长度）。

而在 AAT 引擎中，无论字库中包含多么复杂的上下文替换规则，编译器在离线构建字库时，已经通过自动机状态合并算法（Automata Minimization），将所有的并发规则**全部预编译为了单一的一张确定性状态转移表**！
在运行时，CoreText 排版引擎仅需一个简单的指针遍历字符串：
1. 读取当前字形 GID，查类表得到输入类别 $c \in \Sigma$；
2. 依据当前状态 $s \in Q$ 与类别 $c$，在二维数组中一步查得目标新状态 $s' = \delta(s, c)$ 以及伴随动作；
3. 执行动作（如设置标记、替换字符），将状态更新为 $s'$，指针前移一个字形。

**整段文本仅需从头到尾被扫描且仅被扫描整整一次（Single-pass Scanning），时间复杂度严格锁定为物理极限的 $O(N)$！**
在处理数万字的长篇巨著排版时，AAT 的渲染延迟与内存开销远远低于多轮循环的 OpenType 引擎，展现了计算机科学理论应用于工程实践的极致冷峻之美。

---


### 5.5 FontForge 中 AAT 状态转移表（State Transition Table）完整十六进制结构

在底层的 TrueType 字体二进制中，AAT 状态机被编码为 `morx`（扩展变态表）或 `kerx`（扩展字距表）中的状态子表（State Subtable）。其核心数据结构如下：
* **`Header`**：记录状态机类型、类数（Class Count）、状态数（State Count）、类表偏移量与状态转移阵列偏移量；
* **`Class Table`**：一个将字形 GID 映射到输入类别（Class ID）的查找表。通常采用 Format 0（简单微调数组）或 Format 2（二分查找区间）；
* **`State Array`**：一个二维矩阵，行索引为状态号（State ID），列索引为输入类别（Class ID）。每个单元格包含一个 16 位整数偏移量，指向对应的状态转移条目（Entry）；
* **`Entry Table`**：状态转移条目结构体：
  ```c
  struct MorxTransitionEntry {
      uint16 newStateOffset;    /* 转移后的新状态在状态数组中的字节偏移 */
      uint16 flags;             /* 控制标志位（如是否标记当前字形、是否推进指针） */
      uint16 markIndex;         /* 若设置了替换动作，指向被标记字形的替换表索引 */
      uint16 currentIndex;      /* 指向当前字形的替换表索引 */
  };
  ```

每个控制标志位（Flags）具有极其精细的微指令语义：
* **Bit 15 (`Mark`)**：将当前字形压入内部标记寄存器；
* **Bit 14 (`DontAdvance`)**：**关键停顿微指令**！指示排版引擎在完成本次状态转移后，**不要将扫描指针向前移动到下一个字形**，而是保持在当前字形上，使用新的状态再次评估当前字形！这使得状态机能够处理复杂的重叠匹配与贪婪扫描；
* **Bit 13 (`Reserved`)**：保留位，恒为 0；
* **Bits 12–0 (`Verb / Sub-action`)**：在重排状态机中指定字形交换的步长与方向。

通过这一套极致纯粹的硬件级微指令，AAT 状态机仅凭一张静态字节表与一个极度轻量的解释器循环，即可在几十纳秒之内完成人类最复杂文字的动态排版变形！


## 6. 结语与现代排版技术图景（Conclusions and Modern Outlook）

经过三十余年的激烈竞争与技术融合，数字字型的智能化排版格局已经清晰明朗：
* **OpenType** 凭借 Adobe 与微软在跨平台工业软件（InDesign、Office、Web 浏览器）上的庞大生态号召力，成为了当今互联网与桌面排版事实上的全球通用标准；
* **AAT** 凭借其超前而优雅的有限状态自动机理论，在苹果 macOS 与 iOS 系统生态中守护着高品质排版的底线，并在波斯体与南亚文字处理中树立了无与伦比的性能标杆；
* **开源引擎的集大成**：以 Behdad Esfahbod 等人开发的开源排版引擎 **HarfBuzz** 为里程碑，现代计算系统成功在单一运行时内完美兼容了 OpenType 规则解析与类 AAT 的状态流水线，成为了 Chrome、Firefox、Android、LibreOffice 以及各大 Linux 发行版背后的世界引擎底座；
* **走向多维：OpenType 1.8 可变字体（Variable Fonts）**：2016 年微软、Adobe、苹果与谷歌联合发布的 OpenType 1.8 规范，将高级排版功能推向了全新的空间维度。通过在 `GSUB`/`GPOS` 中挂载 `FeatureVariations` 表，字体设计师不仅能够在字重、字宽、视觉尺寸轴线上平滑插值轮廓，更能在设计轴滑块行进到特定阈值时，自动无缝触发字形骨架与排版特性的动态突变。

从金属活字的物理枷锁，到 PostScript 的静态贝塞尔曲线，再到 OpenType 与 AAT 将计算逻辑植入字型内核——人类文字的排印艺术在数字时代不仅没有消亡，反而在现代自动机理论与微观几何计算的滋养下，绽放出了前所未有的智慧与璀璨光芒。
