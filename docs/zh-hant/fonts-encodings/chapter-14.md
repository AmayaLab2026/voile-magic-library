---
title: "第 14 章：高級排版體系：OpenType 與 AAT 特性深度實戰"
description: "完整無刪節 1:1 學術全譯：複雜文字排版困境（天城文連字拆分與元音前置重排、阿拉伯文連筆形態與雙向排印、西文歷史連字與小型大寫字母）；OpenType 架構全景（GSUB 替換表 1–8 類、GPOS 定位表 1–6 類、標準特性標籤 Feature Tags）；FontLab 中編寫 Adobe 特性定義語言（AFDKO .fea 語法、上下文替換規則、嵌套查找表 Lookup）；微軟 VOLT 可視化工程工作流（項目架構、替換與定位視窗、Proofing 實時字形追蹤排印測試）；FontForge 中的高級排版管理（錨點類、鏈式上下文規則）；蘋果高級排版（AAT）有限狀態自動機（FSM、morx 表、狀態轉移矩陣、標記與堆棧動作實戰）。"
---

# 第 14 章：高級排版體系：OpenType 與 AAT 特性深度實戰

**雅尼斯·哈拉蘭博斯（Yannis Haralambous, Ph.D.）著**  
*選自《Fonts & Encodings》第 549–598 頁*

*譯者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

# 導言：複雜排版的世紀挑戰

本章的標題直指數字字體技術皇冠上的明珠——**OpenType** 與蘋果 **AAT**（Apple Advanced Typography）的“**高級排版特性**”（Advanced Typographic Features）。

在活字印刷與桌面出版的漫長歲月中，排版系統長期被“一個字符對應一個固定字形模具”的簡單思維所禁錮。然而，人類文明孕育的文字系統何其廣博璀璨，這種單調的機械映射在面對複雜文字系統（Complex Scripts）時迅速陷入破產：

1. **印度次大陸文字（以天城文 Devanagari 爲代表）**：在梵文、印地文等語言中，輔音簇之間會融合成結構繁複的組合連字（Conjuncts）；更爲奇特的是，短元音符號 “i-matra”（ि）在邏輯編碼中輸入在輔音之後，但在物理印刷時卻必須在視覺上發生“逆序飛躍”，**整齊地跨越前方整個輔音簇並懸掛在詞頭最左側！**
2. **阿拉伯文字系**：阿拉伯文是天生的草書連筆文字。每一個字母在詞首（Initial）、詞中（Medial）、詞尾（Final）以及孤立狀態（Isolated）下必須呈現截然不同的字形骨架，同時上下變音符號（Tashkeel）必須依據不同字高的字母動態漂移對齊。
3. **希伯來文與東南亞文字**：希伯來文的元音點（Niqqud）與誦讀吟誦標記必須精密疊落而不發生墨跡重疊；泰文、緬甸文更具有多層垂直堆疊規則。
4. **西文高階典籍排版**：哪怕在看似規則的拉丁字母體系中，殿堂級的人文排版同樣要求極其精妙的動態變換：自動識別並替換標準連字（如 $\text{fi}, \text{fl}, \text{ffi}, \text{ffl}$）、歷史罕見連字（如 $\text{ct}, \text{st}, \text{long-s}$）、真小型大寫字母（Small Capitals）、上標與下標數字、比例數字（Proportional Figures）、無襯線表格式等寬數字（Tabular Figures）、舊式復古高低不齊的吊腳數字（Old-Style Figures）以及真分數（Fractions）。

爲了在統一的數字字體文件內部完美承載上述複雜的排印智能，現代排版學孕育出了兩大工程奇蹟：由微軟與 Adobe 聯合主導的 **OpenType 佈局架構**，以及蘋果公司獨闢蹊徑的 **AAT 有限狀態自動機架構**。

---

# OpenType 佈局架構的宏觀全景

OpenType 的高級排版能力主要建立在兩大基石表格之上：**GSUB**（Glyph Substitution Table，字形替換表）與 **GPOS**（Glyph Positioning Table，字形定位表）。

## 1. GSUB：字形替換的八大查找類型（Lookups）

字形替換表的使命，是根據上下文語義規則，將文本流中的一個或多個字形代碼（Glyph IDs）動態替換爲字模庫中的另外一個或多個目標字形：

* **單字形替換（Single Substitution, Lookup Type 1）**：一對一替換。例如將普通小寫字母 ‘a’ 替換爲小型大寫字母 ‘ᴀ’（`smcp` 特性），或將平直括號替換爲大寫字母專用的高位括號。
* **多字形替換（Multiple Substitution, Lookup Type 2）**：一對多分解。例如將組合印地文連字拆解爲其各自的原始輔音構件，或將單個特殊連字拆分成基礎字母序列。
* **擇一字形替換（Alternate Substitution, Lookup Type 3）**：一對多交互選擇。爲同一字符提供多種可選的藝術異體花體（如由設計者精心繪製的多種花體大寫字母 Swash），供排版軟件彈出視窗由用戶手工點選。
* **連字替換（Ligature Substitution, Lookup Type 4）**：多對一融合。將連續輸入的一串字符序列合體爲一個獨一無二的專用連字字模（最經典如 $f + i \to \text{fi}$，$f + f + l \to \text{ffl}$）。
* **上下文替換（Contextual Substitution, Lookup Type 5）**：在特定的前後文字符環繞語境下觸發替換。例如：當且僅當小寫字母 ‘s’ 出現在詞尾且前接元音時，將其替換爲終端優雅捲曲形式。
* **鏈式上下文替換（Chained Contextual Substitution, Lookup Type 6）**：這是排印智能的王牌工具！它將排印環境解構爲三大獨立區間：**前瞻回溯區（Backtrack）**、**當前匹配區（Input）**與**後顧前瞻區（Lookahead）**。只有當這三個區間的字符同時嚴絲合縫地命中規則時，纔對當前匹配區內的目標字形施加嵌套替換！
* **擴展字形替換（Extension Substitution, Lookup Type 7）**：突破 16 位二進制偏移量（64 KB 限制）的超長距離跳轉機制。
* **反向鏈式上下文單替換（Reverse Chaining Contextual Single Substitution, Lookup Type 8）**：以從右向左的逆序方向評估上下文並進行單字替換，專爲某些從中東到南亞的複雜從右至左文字流設計。

## 2. GPOS：字形定位的六大核心查找類型

字形定位表並不改變字形本身的物理 ID，而是通過精確操縱字形的幾何座標偏移量（$X$ 軸位移、$Y$ 軸位移、水平步進增量 $\Delta X$、垂直步進增量 $\Delta Y$），在二維平面上對文字進行納米級的微調定位：

* **單字形位置微調（Single Adjustment, Lookup Type 1）**：例如當輸入全大寫文本時，自動將句號、連字符、圓括號整體向上抬升數個像素，使其在視覺上與大寫字高居中對齊。
* **字距調整對（Pair Adjustment / Kerning, Lookup Type 2）**：這就是現代排印中不可或缺的 Kerning！消除如 “AV”、“To”、“WA” 等特定字對之間的刺眼空隙。
* **草書連筆錨點定位（Cursive Attachment, Lookup Type 3）**：在每個連續草書字形的“入口點”（Entry Anchor）與“出口點”（Exit Anchor）之間建立剛性吸附，確保手寫連筆文本無論如何變形，筆畫連接處永遠天衣無縫！
* **標點/重音基字符吸附（Mark-to-Base Attachment, Lookup Type 4）**：在基字符（Base Glyph）與變音符（Mark）上分別預設座標錨點，排版引擎在運行時將兩者的錨點強行對齊重合。這一機制徹底解放了字體庫——設計者無需再爲帶有銳音符、鈍音符、抑揚符的每個字母單獨繪製數百個預製字模，只需繪製一套基字符和一套重音標點，即可通過錨點在屏幕上即時拼合！
* **連字標點吸附（Mark-to-Ligature Attachment, Lookup Type 5）**：將重音符號精密吸附在連字內部的各個獨立構件上方。
* **標點疊落吸附（Mark-to-Mark Attachment, Lookup Type 6）**：用於多重變音符疊加（如在阿拉伯文或越南文中，一個元音字母上方同時疊加抑揚符和聲調符），後一個標點直接以底層標點的頂部錨點爲基準向上吸附。

## 3. 標準四字符特性標籤（Feature Tags）

在 OpenType 架構中，所有上述底層 Lookups 必須被封裝在具有特定語義的 4 字符標籤（Feature Tag）之內，操作系統與排版軟件（如 InDesign、Word、Web 瀏覽器）正是通過識別這些標籤來向用戶呈現功能開關：

* `liga`（Standard Ligatures，默認開啓）：通用標準連字（$\text{fi}, \text{fl}$）；
* `dlig`（Discretionary Ligatures）：藝術性可選連字（如 $\text{ct}, \text{st}$）；
* `smcp`（Small Capitals from Lowercase）：將小寫字母轉換爲真小型大寫字母；
* `c2sc`（Small Capitals from Capitals）：將大寫字母轉換爲小型大寫字母；
* `lnum`（Lining Figures）：與大寫字母等高的全齊平大寫數字；
* `onum`（Oldstyle Figures）：參差不齊的復古高低吊腳數字；
* `pnum` 與 `tnum`：比例間隔數字與表格等寬對齊數字；
* `frac`（Fractions）：斜線分數自動合體（如 $1/2 \to \frac{1}{2}$）；
* `hist`（Historical Forms）：歷史變體字形（如長 s，$\text{ſ}$）；
* `salt`（Stylistic Alternates）：風格備用字形；
* `swsh`（Swash）：華麗花體字端；
* `init`, `medi`, `fina`, `isol`：阿拉伯文的詞首、詞中、詞尾與獨立字形形態；
* `size`（Optical Size）：字體的光學推薦字號區間與基準設計字號元數據。

---

# 在 FontLab 中掌控 OpenType 表與 AFDKO 語法

FontLab 深度整合了 Adobe 的 **AFDKO**（Adobe Font Development Kit for OpenType）編譯器，採用行業通用的**特性定義語言**（**Feature Definition Language**, 擴展名通常爲 `.fea`）。

在 FontLab 的 OpenType 面板中（`Window > Panels > OpenType`，圖 14-1 與 14-2），設計者可以用極其優雅的人類可讀代碼來編寫整套排印規則：

::: tip 圖 14-1：FontLab 中編寫與調試 OpenType 特性定義語言（AFDKO .fea 語法）的主編輯視窗
![圖 14-1：FontLab 中編寫與調試 OpenType 特性定義語言的主編輯視窗](/images/fonts-encodings/fig14-1.png)
*圖 14-1：FontLab 中編寫與調試 OpenType 特性定義語言的主編輯視窗。*
:::

::: tip 圖 14-2：FontLab 中 OpenType 特性編譯成功與錯誤語法診斷面板
![圖 14-2：FontLab 中 OpenType 特性編譯成功與錯誤語法診斷面板](/images/fonts-encodings/fig14-2.png)
*圖 14-2：FontLab 中 OpenType 特性編譯成功與錯誤語法診斷面板。*
:::

## 1. 核心語法範例與機制

### 字符類（Classes）的定義
使用 `@` 符號聲明字形集合，極大地精簡後續規則的書寫：
```fea
@UPPERCASE = [A-Z];
@FIGURES_LINING = [zero one two three four five six seven eight nine];
@FIGURES_OLDSTYLE = [zero.oldstyle one.oldstyle two.oldstyle three.oldstyle four.oldstyle five.oldstyle six.oldstyle seven.oldstyle eight.oldstyle nine.oldstyle];
```

### 語言系統聲明（Languagesystem）
通知排版引擎該特性適用於哪些文字與語言：
```fea
languagesystem DFLT dflt;
languagesystem latn DFLT;
languagesystem latn DEU; /* 德語體系 */
```

### 基礎連字與小型大寫字母規則
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

### 上下文與鏈式排除規則（Contextual & Ignore Rules）
在特性定義語言中，**單引號** `'` 標記了當前規則中實際被執行替換的目標字符！
例如，在排版中我們要將孤立出現的三個字母 “T E X” 自動合體爲專有的 $\text{\TeX}$ 標識，但若該詞嵌入在更長的單詞（如 “TEXAS”）中時則必須嚴禁合體：
```fea
feature dlig {
    ignore sub [A-Z Eacute] T' E' X' ;
    ignore sub T' E' X' [A-Z Eacute] ;
    sub T' E' X' by T_e_X;
} dlig;
```

### GPOS 位置微調與錨點語法
```fea
# 調整特定字對的 Kerning
pos T -50;
pos A V -100;

# 標點吸附錨點語法（MarkToBase）
markClass [acute] <anchor 150 450> @TOP_MARKS;
pos base [e] <anchor 250 450> mark @TOP_MARKS;
```

在 FontLab 的預覽面板中（Preview Panel，圖 14-5），設計者可以勾選不同的特性複選框，輸入多行長文本，實時測試 OpenType 特性在屏幕上的展開效果。

::: tip 圖 14-5：FontLab 的預覽面板（Preview Panel）。支持在不同字號與行距下實時測試與校驗 OpenType 特性的編譯渲染表現
![圖 14-5：FontLab 的預覽面板](/images/fonts-encodings/fig14-5.png)
*圖 14-5：FontLab 的預覽面板。支持在不同字號與行距下實時測試與校驗 OpenType 特性的編譯渲染表現。*
:::

---

# 微軟 Visual OpenType Layout Tool（VOLT）工業級實戰

如果說 FontLab 代表了程序員所鍾愛的純文本代碼編譯流，那麼微軟官方出品的 **VOLT**（**Visual OpenType Layout Tool**）則是大型商業鑄字工坊進行極其複雜的阿拉伯文、天城文與東亞字體工程的絕對權威標準。

VOLT 的架構完全摒棄了手寫代碼，其核心採用高度嚴密的**圖形數據庫驅動模式**：

::: tip 圖 14-6：微軟 VOLT（Visual OpenType Layout Tool）項目全局管理主視窗。左側展示腳本與語言分層樹，右側列出全部獨立的 Lookups 查找表集合
![圖 14-6：微軟 VOLT 項目全局管理主視窗](/images/fonts-encodings/fig14-6.png)
*圖 14-6：微軟 VOLT 項目全局管理主視窗。左側展示腳本與語言分層樹，右側列出全部獨立的 Lookups 查找表集合。*
:::

## 1. VOLT 的核心工作流：

* **項目視窗（Project Window，圖 14-6）**：以嚴格的層次結構組織腳本（Scripts）、語言系統（Languages）、特性（Features）以及全局獨立的 Lookups 庫。
* **字形替換視窗（Substitution Window，圖 14-7）**：採用極其直觀的視覺表格：
  * **To**（原始字形）與 **By**（替換字形）；
  * **Context**（前置語境）與 **Lookahead**（後置語境）；
  * 勾選 `Reverse Chaining` 可直接一鍵將查找表編譯爲罕見的 Lookup Type 8！
* **位置與錨點視窗（Positioning Window，圖 14-8）**：設計師可以直接在字形畫布上，用鼠標直觀地拖拽基字符錨點與標點符號錨點，在極度放大的視窗中實時對拍兩者的重合位置，徹底告別盲猜座標數字的痛苦。
* **打樣測試臺（Proofing Window，圖 14-9）**：VOLT 的測試臺堪稱排印偵探：當輸入一串複雜的天城文或阿拉伯文文本時，測試臺不僅呈現最終渲染圖像，更能**逐幀回放每一個 Lookup 的執行次序、匹配上下文以及被成功替換或定位的字形步驟軌跡！**

::: tip 圖 14-7：VOLT 中的字形替換編輯視窗。展示了前置語境、匹配字形類與目標替換類的圖形化配置界面
![圖 14-7：VOLT 中的字形替換編輯視窗](/images/fonts-encodings/fig14-7.png)
*圖 14-7：VOLT 中的字形替換編輯視窗。展示了前置語境、匹配字形類與目標替換類的圖形化配置界面。*
:::

::: tip 圖 14-8：VOLT 中的交互式標點吸附（Mark-to-Base）錨點直觀配置視窗
![圖 14-8：VOLT 中的交互式標點吸附錨點直觀配置視窗](/images/fonts-encodings/fig14-8.png)
*圖 14-8：VOLT 中的交互式標點吸附錨點直觀配置視窗。*
:::

::: tip 圖 14-9：VOLT 強大的交互式排印打樣測試臺（Proofing Window）。支持單步單幀追蹤複雜排印特性的命中與執行鏈條
![圖 14-9：VOLT 強大的交互式排印打樣測試臺](/images/fonts-encodings/fig14-9.png)
*圖 14-9：VOLT 強大的交互式排印打樣測試臺。支持單步單幀追蹤複雜排印特性的命中與執行鏈條。*
:::

---

# 在 FontForge 中管理高級排版特性

作爲開源旗艦，FontForge 同樣提供了極其完整且兼顧圖形與底層數據結構的 OpenType 表管理面板（`Element > Font Info > Lookups`）：

* **錨點類系統（Anchor Classes，圖 14-10）**：在單個字形內部明確區隔 `Base`、`Mark`、`Ligature` 與 `Cursive` 錨點；
* **單向與成對位置微調（圖 14-12）**：提供類似電子表格的 Kerning 表格界面；
* **鏈式上下文替換配置嚮導（Chained Contextual Wizard，圖 14-13 [a]–[d]）**：將極其複雜的鏈式查找表拆解爲四步引導向導：
  1. 設定前瞻回溯字形類；
  2. 設定當前匹配目標類；
  3. 設定後顧前瞻字形類；
  4. 綁定被調用的嵌套底層 Lookup 規則。

::: tip 圖 14-10：FontForge 中的錨點類（Anchor Classes）配置面板。直觀定義基字符與變音符號的物理吸附錨點
![圖 14-10：FontForge 中的錨點類配置面板](/images/fonts-encodings/fig14-10.png)
*圖 14-10：FontForge 中的錨點類配置面板。直觀定義基字符與變音符號的物理吸附錨點。*
:::

::: tip 圖 14-11：FontForge 中的單字替換配置面板（左：字形標籤頁；右：新替換規則創建對話框）
![圖 14-11：FontForge 中的單字替換配置面板](/images/fonts-encodings/fig14-11.png)
*圖 14-11：FontForge 中的單字替換配置面板。*
:::

::: tip 圖 14-12：FontForge 中的簡單位置調整（左）與成對字距調整 Kerning（右）配置視窗
![圖 14-12：FontForge 中的簡單位置調整與成對字距調整配置視窗](/images/fonts-encodings/fig14-12.png)
*圖 14-12：FontForge 中的簡單位置調整與成對字距調整配置視窗。*
:::

::: tip 圖 14-13：FontForge 中配置四步鏈式上下文替換向導的連續交互界面：(a) 查找表類型選擇；(b) 格式指定；(c) 規則覆蓋範圍設定；(d) 語境與替換動作綁定
![圖 14-13：FontForge 中配置四步鏈式上下文替換向導的連續交互界面](/images/fonts-encodings/fig14-13.png)
*圖 14-13：FontForge 中配置四步鏈式上下文替換向導的連續交互界面：(a) 查找表類型選擇；(b) 格式指定；(c) 規則覆蓋範圍設定；(d) 語境與替換動作綁定。*
:::

---

# 蘋果高級排版（AAT）與有限狀態自動機（FSM）

在排版工程史上，蘋果公司走了一條與微軟/Adobe 截然不同、在理論計算機科學上極其優美高貴的道路——**基於有限狀態自動機（Finite State Automata, FSM）的 AAT 技術**（存儲於字體的 `morx`、`kerx` 與 `feat` 表中）。

在 OpenType 中，排版引擎必須在字符串中進行反覆的上下文正則回溯匹配，當面對極長或極複雜的文句時，計算複雜度極易退化；而蘋果的 AAT 引擎**在底層本質上是一個純粹的確定性有限狀態機（DFA）**！文本流中的字符被當作狀態機的一個個輸入事件，引擎在常數時間複雜度內即時驅動狀態轉移，運行速度極快且極具數學確定性。

::: tip 圖 14-14：FontForge 中編輯 AAT 特性與選擇器（Features and Selectors）名稱的三個管理視窗：(a) 特性族名稱；(b) 選擇器屬性與默認激活開關；(c) 多語言本地化字符串
![圖 14-14：FontForge 中編輯 AAT 特性與選擇器的三個管理視窗](/images/fonts-encodings/fig14-14.png)
*圖 14-14：FontForge 中編輯 AAT 特性與選擇器的三個管理視窗：(a) 特性族名稱；(b) 選擇器屬性與默認激活開關；(c) 多語言本地化字符串。*
:::

## 1. 特性與選擇器（Features & Selectors）

在 AAT 規範中，排印特性由兩個純整數界定：
* **Feature Type（特性大類編號）**：例如編號 1 代表連字，編號 3 代表大小寫轉換；
* **Feature Selector（特性選擇器編號）**：大類下的具體開關。例如在連字特性下，選擇器 0 代表禁用所有連字，選擇器 2 代表開啓標準連字，選擇器 4 代表開啓歷史連字。
通過在 FontForge 中編輯多語言字典（圖 14-14），可以爲 macOS 系統的字體調色板提供原生的本地化菜單名稱。

## 2. AAT 狀態轉移矩陣的運作機理

AAT 狀態機由以下核心要素咬合運轉：
1. **字符分類表（Class Table）**：將字庫中數萬個字形劃分爲若干等價類（例如：類 0 = 非數字，類 1 = 數字，類 2 = 斜線 `/`，類 3 = 文本結束符 EOT）；
2. **狀態轉移矩陣（State Transition Matrix）**：行代表“當前狀態”（Current State），列代表“當前讀入字形的類別”（Class）。矩陣單元格內嚴密記錄着：
   * **Next State（下一跳狀態編號）**；
   * **Mark Current Glyph（是否在當前字形上打上標記標記錨點）**；
   * **Substitute Marked Glyph（將之前被標記的字形替換爲指定目標）**；
   * **Substitute Current Glyph（將當前剛讀入的字形替換爲目標）**；
   * **Push to Stack（是否將當前字形壓入內部臨時堆棧，最多支持 8 個深度！）**。

::: tip 圖 14-15：FontForge 中構建 AAT 有限狀態自動機轉移矩陣的拓撲視窗。直觀展現狀態節點、類輸入遷移邊與字形堆棧操作指令
![圖 14-15：FontForge 中構建 AAT 有限狀態自動機轉移矩陣的拓撲視窗](/images/fonts-encodings/fig14-15.png)
*圖 14-15：FontForge 中構建 AAT 有限狀態自動機轉移矩陣的拓撲視窗。直觀展現狀態節點、類輸入遷移邊與字形堆棧操作指令。*
:::

### 經典實戰狀態機：自動連分數轉換器

讓我們觀察圖 14-15 中實現的自動真分數狀態機：
* **初始狀態（State 1, Start of Text）**：
  * 若輸入非數字字符，狀態保持在 State 1，無動作；
  * 若讀入數字字符（如 ‘3’），狀態機在當前數字上打上標記（Mark），並轉移至 **State 2（已命中分子候選）**。
* **分子狀態（State 2）**：
  * 若繼續讀入數字，繼續標記並保持在 State 2；
  * 若突然讀入普通斜槓 `/`，狀態機立刻將之前標記的一連串普通數字批量替換爲**高位上標分子數字**（Numerators），將當前斜槓替換爲優雅的**排印專用分數斜線**（Fraction Slash, `U+2044`），並瞬間躍遷至 **State 3（已命中分數線）**；
  * 若讀入其他非數字字符，判定當前非分數語境，靜默解除標記並回滾至 State 1。
* **分母狀態（State 3）**：
  * 在此狀態下讀入的任何後續連續數字，一律就地替換爲**低位下標分母數字**（Denominators）；
  * 直至遭遇第一個非數字字符，狀態機完成閉環，優雅跳回 State 1！

藉由這套基於圖靈自動機理論的高階狀態引擎，字體的排版邏輯在極度複雜的極端上下文與極端長文本面前，始終堅如磐石、風馳電掣。

---

# 結語

從基礎單字替換到鏈式語境判斷，從二維平面浮動錨點到確定性有限狀態自動機，高級排版技術爲冰冷僵硬的數字矢量字模注入了深邃的語言學智能。

正是這些精妙絕倫的查找表與狀態轉移矩陣，打破了數百年機械印刷的物理枷鎖，讓屏幕上躍動的一筆一劃能夠隨着人類思想與語言的節律自由呼吸、顧盼生姿。
