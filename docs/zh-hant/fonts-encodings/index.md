---
title: 館藏第三號 · 字體與編碼：從 Unicode 到高級排版及其中一切
description: ヴ瓦爾魔法圖書館 館藏第三號典籍：雅尼斯·哈拉蘭布斯（Yannis Haralambous）曠世鉅著《Fonts & Encodings》全書深度學術漢譯與圖解典藏。
---

# 館藏第三號典籍 ·《字體與編碼：從 Unicode 到高級排版及其中一切》
### Fonts & Encodings: From Unicode to Advanced Typography and Everything in Between
**著者：雅尼斯·哈拉蘭布斯 博士（Yannis Haralambous, Ph.D.）**  
*英譯審訂：P. Scott Horne 博士 · 原著由 O'Reilly Media 出版（ISBN 978-0-596-10242-5）*

> **“智人（*Homo sapiens*）是一種進行書寫的物種。在用於書寫的形形色色的工具之中，最新近亦最繁複的造物當屬計算機——它集閱讀工具、書寫工具、存儲媒介與數據交換手段於一身……在這一數字書寫空間內部，編碼（encoding）與字體（font）承擔着截然不同卻密不可分的核心使命：編碼源於人類對信息的概念化抽象（abstraction），是純粹思維的心智構建；而字體則是書寫符號的具象視覺呈現，是黑白墨彩的圖形實體。兩者猶如陰陽、天地、理論與實踐，在數字世界永無休止地交織共舞。”**  
> —— 雅尼斯·哈拉蘭布斯（Yannis Haralambous），《字體與編碼》導言

---

## 典籍題解與學術地位

在計算機科學與現代數字排印學（Digital Typography）交匯的發展史冊中，雅尼斯·哈拉蘭布斯（Yannis Haralambous）的《字體與編碼》（*Fonts & Encodings*）被公認爲**該領域無可替代的百科全書式“聖經”鉅著**。

全書原著逾 1,040 頁，源自法國國立布列塔尼高等電信學院（ENST Bretagne）哈拉蘭布斯教授歷時十餘載的深厚學術積澱與工程實踐。本書以宏大而嚴謹的視野，打破了傳統排印美學、計算機底層操作系統編碼、字形光柵化幾何數學（Bézier 曲線）與多語言複雜文書排版引擎之間的技術壁壘，首次將：
1. **字符編碼體系（Character Encodings & Unicode）**：從早期電傳打字機 FIELDATA、ASCII、EBCDIC、ISO 8859 系列、中日韓（CJK）早期雙字節代碼頁，到現代 Unicode 5.0 核心哲學、平面分佈、雙向排版算法（Bidi）、規範化分解（Normalization Forms）、複雜文字合字連寫規則；
2. **數字字體工程與底層格式（Digital Font Technologies）**：從早期的點陣字模（Bitmap）、高德納（Donald E. Knuth）的 METAFONT 曲線方程、Adobe PostScript Type 1 輪廓與 Hinting 提示指令，到 TrueType（TTF）底層虛擬機字節碼指令（Twilight Zone、CVT、FDIR）、OpenType 高級排版特性表（GSUB / GPOS / GDEF / BASE / JSTF）與蘋果高級排版技術（Apple Advanced Typography, AAT）有限狀態自動機引擎（Finite Automata Engine）；
3. **跨學科排版軟件與排印數學（Typographic Software & Mathematics）**：Donald Knuth 創立的 TeX 排版宏系統與 $\Omega$（Omega）多語言排版引擎、PostScript 頁面描述語言底層流解釋器、PDF 規範內部字形引用流、以及 Pierre Bézier 三次多項式參數曲線與伯恩斯坦基函數（Bernstein Basis Polynomials）數學嚴密證明；

融鑄爲一部邏輯嚴密、兼備歷史源流考據與底層工業規範工程細節的傳世經典。

---

## 責任著者與學術源流考略

### 責任著者：雅尼斯·哈拉蘭布斯 博士（Yannis Haralambous, Ph.D.）

* **學術身份**：著名計算機科學家、應用數學家、數字排印與計算語言學泰斗，法國國立布列塔尼高等電信學院（École Nationale Supérieure des Télécommunications de Bretagne, 現 IMT Atlantique）計算機科學系終身教授。
* **早年求學與學術背景**：哈拉蘭布斯出生於希臘，早年赴法留學，在里爾第一大學（Université de Lille I）獲得純粹數學博士學位。他在抽象幾何學與拓撲學方面的深厚數理造詣，爲其日後開創性地研究文字輪廓矢量幾何、多項式樣條擬合與複雜書寫系統自動機奠定了堅實的理論基石。
* **TeX 與 $\Omega$（Omega）系統開拓**：上世紀 90 年代初，針對 Donald Knuth 傳統 TeX 系統在處理非拉丁文字（希臘文、阿拉伯文、希伯來文、梵文、藏文等）以及 8 位字符集限制上的歷史瓶頸，哈拉蘭布斯與英國計算機科學家約翰·普萊斯（John Plaice）共同開創性地開發了 **$\Omega$（Omega）排版系統**。Omega 率先引入了 16/32 位 Unicode 字符原生支持，並獨創了“有限狀態文本變換流”（Omega Translation Processes, OTPs），徹底革新了複雜文種的雙向排版與上下文自動變體處理範式。
* **全球多語言排版工程顧問**：哈拉蘭布斯長期擔任 Unicode 聯盟專家顧問、國際排版協會（ATypI）理事、TeX 國際用戶組（TUG）核心專家，爲全球各大軟件巨頭與出版學術機構攻克了無數涉及古希臘文變音符標號（Polytonic Greek）、敘利亞文、烏爾都文及現代東亞表意文字的排印算法難題。
* **本書成書源流**：本書最初以法文撰寫，由 O'Reilly France 於 2004 年出版（書名《*Fontes & codages*》）。因其學術震撼力與前所未有的工程深度，O'Reilly 美國總部特聘計算語言學與專業翻譯專家 P. Scott Horne 博士耗時三年進行深度英譯擴充，全面更新至 Unicode 5.0 與最新 OpenType / AAT 工業標準，於 2007 年正式刊行英文首版，成爲現代數字排印學的里程碑。

---

## 館藏全書卷目導航

::: tip 典籍分卷導覽
請點擊下方各編章節，翻閱本館全譯圖解正文：
:::

### 導言篇與基礎鋪墊
* **[導言 · 探索篇：字母部件、印刷排版、數字模型與全書知識圖譜](./introduction)**  
  *原著：Yannis Haralambous* —— 奠定全書基礎概念。系統論述字符（character）與字形（glyph）的心智二元性；詳解字母解剖學各部位術語（配高清全綵圖版 Figure 0-1）；考據字母“E”的六大數學幾何描述（配帕喬利、丟勒、托里、若戎委員會圖版 Figure 0-2）；回溯狄德羅百科全書手工活字拼版機制（配十八世紀字盤與手合子圖版 Figure 0-3 至 0-5）；詳解數字排版基線、進深矢量與字距微調；全景解析全書四大編體系知識圖譜（配圖版 Figure 0-6）。

### 第一編：編碼與字符集（Part I: Encodings & Unicode）
* **[第一章：前 Unicode 時代的編碼體系](./chapter-1)**  
  從電傳機與軍用 FIELDATA、7 位 ASCII 到 8 位 EBCDIC；詳解 ISO 2022 轉義序列框架；深入剖析 ISO 8859 家族（Latin-1 至 Latin-16）及東亞早期雙字節編碼標準；微軟 Windows 代碼頁與蘋果 MacRoman 歷史架構；電子郵件 MIME 與早期 Web 文本傳輸困境。
* **[第二章：字符、字形與字節：Unicode 導論](./chapter-2)**  
  文字學哲學命題；Unicode 核心原則與四維空間；UTF-8、UTF-16、UTF-32、CESU-8 與 SCSU 編碼形式底層比特流映射；基本多語言平面（BMP）與各輔助平面分佈全景。
* **[第三章：Unicode 字符核心屬性體系](./chapter-3)**  
  字符名稱規範；通用分類（General Category）；方向性與雙向算法類別；連寫與鏡像屬性；數字值與標識符規範；深入解讀 Unicode 字符數據庫（UCD）。
* **[第四章：規範化分解、雙向排版算法與東亞表意文字處理](./chapter-4)**  
  Unicode 規範等價與兼容等價；四種規範化形式（NFC、NFD、NFKC、NFKD）；Unicode 雙向排版算法（Bidi Algorithm）解析；CJK 統一漢字（Unihan）編碼歷史源流、字形統合規則（Han Unification）與康熙字典部首索引。
* **[第五章：Unicode 的實踐與字符錄入工具](./chapter-5)**  
  操作系統多語言字符映射工具（Character Palette、Character Map、BabelMap、Gucharmap）；鍵盤佈局定製器（MSKLC、Keyman Developer）；ICU 國際化組件。

### 第二編：操作系統字體管理（Part II: Font Management）
* **[第六章：Macintosh 操作系統的字體管理](./chapter-6)**  
  Classic Mac OS 資源分支（Resource Fork）與數據分支；Suitcase 字體箱架構；Mac OS X 字體簿（Font Book）與字體域（Domains）；Core Graphics 文本渲染。
* **[第七章：Windows 操作系統的字體管理](./chapter-7)**  
  Windows 字體控制面板與註冊表架構；GDI 邏輯字體（LOGFONT）度量；ClearType 亞像素液晶渲染原理；OpenType 原生驅動支持。
* **[第八章：X Window 與 Unix 字體管理](./chapter-8)**  
  X11 邏輯字體描述符（XLFD）；X 字體服務器（XFS）與核心字體協議；現代 FreeType、Fontconfig 與 Xft 客戶端渲染流水線；GNU 字體工具箱。

### 第三編：排版引擎與技術生態（Part III: Typographic Software & Web）
* **[第九章：TeX 與 Omega 系統的字體技術](./chapter-9)**  
  高德納批處理編譯器架構；TFM 字體度量與 DVI 設備無關文件；虛擬字體（VF）與 PK 點陣壓縮；哈拉蘭布斯開創的 16/32 位 Omega 系統與 OTPs 有限狀態文本變換流。
* **[第十章：Web 網頁字體與排版技術](./chapter-10)**  
  萬維網排版演化史；HTML/CSS 字體模塊規範；ont-size-adjust 幾何歸一化算法與 x-height 視覺對齊；早期網絡字體技術（Bitstream TrueDoc、Microsoft WEFT/EOT）；SVG 矢量字體規範。

### 第四編：字體藝術、設計與高級排版（Part IV: Typeface Art, Design & Typography）
* **[第十一章：拉丁字體的歷史演進與分類學](./chapter-11)**  
  十五世紀金屬活字排版大爆炸；卡羅林小草書體演進；加拉蒙德、巴斯克維爾、博多尼與迪多；無襯線體的工業崛起；Vox-ATypI 分類法全系解析；Panose-1 十維視覺特徵度量編碼體系。
* **[第十二章：字體設計與編輯實操](./chapter-12)**  
  現代字體設計工作流；FontLab 與 FontForge 深度實操；PostScript 三次與 TrueType 二次貝塞爾曲線幾何轉換；輪廓遍歷方向與非零環繞數規則；字形度量與基於類的字距微調（Class-based Kerning）。
* **[第十三章：柵格化渲染優化與字形微調](./chapter-13)**  
  屏幕低分辨率下的排印困境；PostScript 聲明式微調（BlueValues 對齊區、標準筆寬 StdHW/StdVW、主幹提示 hstem/vstem）；TrueType 圖靈完備指令集虛擬機；CVT 控制值表；微點 Delta 指令實操。
* **[第十四章：豐富字體表達：高級排版特性](./chapter-14)**  
  智能字體技術全景；OpenType 佈局架構（GSUB/GPOS/GDEF 三大支柱）；Adobe 特性定義語言；微軟 VOLT 可視化工程實操；蘋果 AAT 有限狀態自動機流派深度對比。

### 第五編：技術附錄（Part V: Appendices）
* **[附錄全編：底層格式、虛擬機與數學原理手冊](./appendices)**  
  涵蓋原著附錄 A 至 G 全卷精要：點陣字庫（BDF/PCF/PK）；TeX/Omega 度量體系（TFM/OFM/VF）；PostScript 頁面描述語言與 Type 1/CFF；TrueType/OpenType/AAT 底層表結構彙編（head/cmap/loca/glyf/morx 等）；METAFONT 衍生系統；貝塞爾曲線數學定理嚴密推導。
