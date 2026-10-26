---
title: 馆藏第三号 · 字体与编码：从 Unicode 到高级排版及其中一切
description: ヴ瓦尔魔法图书馆 馆藏第三号典籍：雅尼斯·哈拉兰布斯（Yannis Haralambous）旷世巨著《Fonts & Encodings》全书深度学术汉译与图解典藏。
---

# 馆藏第三号典籍 ·《字体与编码：从 Unicode 到高级排版及其中一切》
### Fonts & Encodings: From Unicode to Advanced Typography and Everything in Between
**著者：雅尼斯·哈拉兰布斯 博士（Yannis Haralambous, Ph.D.）**  
*英译审订：P. Scott Horne 博士 · 原著由 O'Reilly Media 出版（ISBN 978-0-596-10242-5）*

> **“智人（*Homo sapiens*）是一种进行书写的物种。在用于书写的形形色色的工具之中，最新近亦最繁复的造物当属计算机——它集阅读工具、书写工具、存储媒介与数据交换手段于一身……在这一数字书写空间内部，编码（encoding）与字体（font）承担着截然不同却密不可分的核心使命：编码源于人类对信息的概念化抽象（abstraction），是纯粹思维的心智构建；而字体则是书写符号的具象视觉呈现，是黑白墨彩的图形实体。两者犹如阴阳、天地、理论与实践，在数字世界永无休止地交织共舞。”**  
> —— 雅尼斯·哈拉兰布斯（Yannis Haralambous），《字体与编码》导言

---

## 典籍题解与学术地位

在计算机科学与现代数字排印学（Digital Typography）交汇的发展史册中，雅尼斯·哈拉兰布斯（Yannis Haralambous）的《字体与编码》（*Fonts & Encodings*）被公认为**该领域无可替代的百科全书式“圣经”巨著**。

全书原著逾 1,040 页，源自法国国立布列塔尼高等电信学院（ENST Bretagne）哈拉兰布斯教授历时十余载的深厚学术积淀与工程实践。本书以宏大而严谨的视野，打破了传统排印美学、计算机底层操作系统编码、字形光栅化几何数学（Bézier 曲线）与多语言复杂文书排版引擎之间的技术壁垒，首次将：
1. **字符编码体系（Character Encodings & Unicode）**：从早期电传打字机 FIELDATA、ASCII、EBCDIC、ISO 8859 系列、中日韩（CJK）早期双字节代码页，到现代 Unicode 5.0 核心哲学、平面分布、双向排版算法（Bidi）、规范化分解（Normalization Forms）、复杂文字合字连写规则；
2. **数字字体工程与底层格式（Digital Font Technologies）**：从早期的点阵字模（Bitmap）、高德纳（Donald E. Knuth）的 METAFONT 曲线方程、Adobe PostScript Type 1 轮廓与 Hinting 提示指令，到 TrueType（TTF）底层虚拟机字节码指令（Twilight Zone、CVT、FDIR）、OpenType 高级排版特性表（GSUB / GPOS / GDEF / BASE / JSTF）与苹果高级排版技术（Apple Advanced Typography, AAT）有限状态自动机引擎（Finite Automata Engine）；
3. **跨学科排版软件与排印数学（Typographic Software & Mathematics）**：Donald Knuth 创立的 TeX 排版宏系统与 $\Omega$（Omega）多语言排版引擎、PostScript 页面描述语言底层流解释器、PDF 规范内部字形引用流、以及 Pierre Bézier 三次多项式参数曲线与伯恩斯坦基函数（Bernstein Basis Polynomials）数学严密证明；

融铸为一部逻辑严密、兼备历史源流考据与底层工业规范工程细节的传世经典。

---

## 责任著者与学术源流考略

### 责任著者：雅尼斯·哈拉兰布斯 博士（Yannis Haralambous, Ph.D.）

* **学术身份**：著名计算机科学家、应用数学家、数字排印与计算语言学泰斗，法国国立布列塔尼高等电信学院（École Nationale Supérieure des Télécommunications de Bretagne, 现 IMT Atlantique）计算机科学系终身教授。
* **早年求学与学术背景**：哈拉兰布斯出生于希腊，早年赴法留学，在里尔第一大学（Université de Lille I）获得纯粹数学博士学位。他在抽象几何学与拓扑学方面的深厚数理造诣，为其日后开创性地研究文字轮廓矢量几何、多项式样条拟合与复杂书写系统自动机奠定了坚实的理论基石。
* **TeX 与 $\Omega$（Omega）系统开拓**：上世纪 90 年代初，针对 Donald Knuth 传统 TeX 系统在处理非拉丁文字（希腊文、阿拉伯文、希伯来文、梵文、藏文等）以及 8 位字符集限制上的历史瓶颈，哈拉兰布斯与英国计算机科学家约翰·普莱斯（John Plaice）共同开创性地开发了 **$\Omega$（Omega）排版系统**。Omega 率先引入了 16/32 位 Unicode 字符原生支持，并独创了“有限状态文本变换流”（Omega Translation Processes, OTPs），彻底革新了复杂文种的双向排版与上下文自动变体处理范式。
* **全球多语言排版工程顾问**：哈拉兰布斯长期担任 Unicode 联盟专家顾问、国际排版协会（ATypI）理事、TeX 国际用户组（TUG）核心专家，为全球各大软件巨头与出版学术机构攻克了无数涉及古希腊文变音符标号（Polytonic Greek）、叙利亚文、乌尔都文及现代东亚表意文字的排印算法难题。
* **本书成书源流**：本书最初以法文撰写，由 O'Reilly France 于 2004 年出版（书名《*Fontes & codages*》）。因其学术震撼力与前所未有的工程深度，O'Reilly 美国总部特聘计算语言学与专业翻译专家 P. Scott Horne 博士耗时三年进行深度英译扩充，全面更新至 Unicode 5.0 与最新 OpenType / AAT 工业标准，于 2007 年正式刊行英文首版，成为现代数字排印学的里程碑。

---

## 馆藏全书卷目导航

::: tip 典籍分卷导览
请点击下方各编章节，翻阅本馆全译图解正文：
:::

### 导言篇与基础铺垫
* **[导言 · 探索篇：字母部件、印刷排版、数字模型与全书知识图谱](./introduction)**  
  *原著：Yannis Haralambous* —— 奠定全书基础概念。系统论述字符（character）与字形（glyph）的心智二元性；详解字母解剖学各部位术语（配高清全彩图版 Figure 0-1）；考据字母“E”的六大数学几何描述（配帕乔利、丢勒、托里、若戎委员会图版 Figure 0-2）；回溯狄德罗百科全书手工活字拼版机制（配十八世纪字盘与手合子图版 Figure 0-3 至 0-5）；详解数字排版基线、进深矢量与字距微调；全景解析全书四大编体系知识图谱（配图版 Figure 0-6）。

### 第一编：编码与 Unicode（Part I: Encodings & Unicode）
* **[第一章：前 Unicode 时代的编码体系](./chapter-1)**  
  从电传机与军用 FIELDATA、7 位 ASCII 到 8 位 EBCDIC；详解 ISO 2022 转义序列框架；深入剖析 ISO 8859 家族（Latin-1 至 Latin-16）及东亚早期双字节编码标准；微软 Windows 代码页与苹果 MacRoman 历史架构；电子邮件 MIME 与早期 Web 文本传输困境。
* **[第二章：字符、字形与字节：Unicode 导论](./chapter-2)**  
  文字学哲学命题；Unicode 核心原则与四维空间；UTF-8、UTF-16、UTF-32、CESU-8 与 SCSU 编码形式底层比特流映射；基本多语言平面（BMP）与各辅助平面分布全景。
* **第三章：Unicode 字符核心属性体系**  
  字符名称规范；通用分类（General Category）；方向性与双向算法类别；连写与镜像属性；数字值与标识符规范；解读 Unicode 数据表（UCD）。
* **第四章：规范化分解、双向排版算法与东亚表意字符处理**  
  Unicode 规范等价与兼容等价；四种规范化形式（NFC、NFD、NFKC、NFKD）；Unicode 双向排版算法（Bidi Algorithm）解析；CJK 统一汉字（Unihan）编码历史源流、字形统合规则（Han Unification）与康熙字典部首索引。
* **第五章：Unicode 实践与系统支持**  
  编程语言中的 Unicode 处理；数据库、操作系统 API 与多语言输入法；国际化组件（ICU）框架。
* **第六章：Unicode 传输与压缩编码**  
  UTF-EBCDIC、BOCU-1 与 SCSU 压缩算法详解；网络标准中的字符集识别与协商机制。
* **第七章：Web 环境下的字体与排版**  
  CSS 字体模块发展；Web 字体格式演进；网页中文本排印的高级控制与跨浏览器渲染差异。

### 第二编：数字字体（Part II: Fonts）
* **第八章：从字符到字形：文本渲染管线**  
  字形映射逻辑；复杂文本布局引擎（HarfBuzz、DirectWrite、CoreText）架构；文本整形（Text Shaping）核心流程。
* **第九章：字体解剖学与度量度**  
  字形外框边界盒（Bounding Box）；水平与垂直排版度量系统；EM 方块与缩放矩阵；光学大小与字重梯队。
* **第十章：字体的元设计（Metadesign）**  
  高德纳 METAFONT 哲学：用数学方程描述字母之魂；笔刷行进方程与参数化设计；从代码生成字形。
* **第十一章：字体历史演进与分类学**  
  从古希腊罗马碑铭体、黑色卡罗林小草体到威尼斯人文主义体、加拉蒙德老明朝体、迪多现代体与现代无衬线体；Vox-ATypI 分类法与 Panose 视觉度量编码体系。
* **第十二章：点阵字体与栅格化原理**  
  早期的 BDF、PCF 与 X11 字模；光栅转换算法（Bresenham）；抗锯齿（Anti-aliasing）与亚像素渲染（Subpixel Rendering / ClearType）。
* **第十三章：PostScript Type 1 字体**  
  Type 1 字体的内部结构；字形轮廓运算符；CharStrings 字节码；提示指令（Hints：Stem Hints, Blue Zones）与栅格优化。
* **第十四章：TrueType 与 OpenType 字体**  
  二次与三次样条曲线对比；TrueType 表结构（`head`, `hhea`, `maxp`, `cmap`, `glyf`, `loca`）；TrueType 虚拟机指令集；OpenType 架构全解。
* **第十五章：字体高级排版特性（OpenType & AAT）**  
  替换表（GSUB）与定位表（GPOS）；上下文合字与位置变体；有限状态自动机驱动的苹果 AAT 引擎；多主控（Multiple Master）与可变字体（Variable Fonts）原理。

### 第三编：排版软件与工业标准（Part III: Typographic Software）
* **第十六章：TeX 与 Metafont 系统**  
  Knuth 的算法世界：断行折行最优规划算法（Dynamic Programming Line Breaking）；数学公式排版规则；TFM、VF 与 DVI 文件格式深度剖析。
* **第十七章：PostScript 页面描述语言**  
  逆波兰记号与堆栈机模型；路径绘制、裁剪与坐标变换矩阵；字体字典与嵌入式资源。
* **第十八章：PDF 便携式文档格式**  
  PDF 对象体系（交叉引用表、字典、流）；字体子集化嵌入（Subsetting）；ToUnicode 映射表与文本提取困境。
* **第十九章：桌面排版（DTP）系统与现代出版**  
  QuarkXPress、InDesign 与现代专业出版排版工作流；高保真色彩管理与印前制版。

### 第四编：技术附录（Part IV: Appendices）
* **附录 A：TeX 与 $\Omega$ 的字体格式规范**  
* **附录 B：PostScript 语言深入参考**  
* **附录 C：TrueType、OpenType 与 AAT 底层表结构全景速查**  
* **附录 D：TrueType 虚拟机指令集汇编全书**  
* **附录 E：METAFONT 语言与衍生系统（METATYPE1 / MetaFog）**  
* **附录 F：现代字体设计与编辑软件实操指南（FontLab / FontForge）**  
* **附录 G：Bézier 曲线与排印数学严密证明导引**  
