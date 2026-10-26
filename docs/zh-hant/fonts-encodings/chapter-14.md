---
description: 雅尼斯·哈拉蘭布斯《Fonts & Encodings》第十四章全文深度學術漢譯：高級排版技術體系。從 Adobe OpenType 特性定義語言（AFDKO Feature File Syntax）到微軟 VOLT（Visual OpenType Layout Tool）視覺化佈局工具，再到 FontForge 中的 OpenType 與 Apple AAT（Apple Advanced Typography）底層狀態機管理，涵蓋字形替換（GSUB）、精確定位（GPOS）、複雜連字、錨點附着、鏈式上下文規則、字偶距微調與有限狀態自動機重排機制。
---

# 第 14 章 · 豐富字體：高級排版技術體系
### Chapter 14: Enriching Fonts: Advanced Typography
**著者：雅尼斯·哈拉蘭布斯 博士（Yannis Haralambous, Ph.D.）**  
**英譯與增訂：P. 斯科特·霍恩 博士（P. Scott Horne, Ph.D.）**  
*選自《字體與編碼》（Fonts & Encodings）原著第 549–598 頁*

---

## 14.1 引言（Introduction）

在傳統活字排版或基礎數字字體中，文本的呈現本質上是一種樸素的一對一映射：輸入一個字符編碼，排版引擎便在其對應的碼位處提取單個固定的字形（Glyph），並按照預設的字身寬度（Advance Width）在基線上向前步進。然而，人類燦爛的文字排印文明絕非如此刻板機械。無論是在拉丁文字中追求極致美感的西文古典排版——例如處理 `fi`、`fl`、`ffi` 等字母碰撞連字（Ligatures）、優雅的小型大寫字母（Small Capitals）、隨段落上下文自動切換的老式非等高數字（Oldstyle Figures / Medieval Numbers）與上下浮動花體尾綴（Swashes）；還是在阿拉伯文、波斯文、烏爾都文等天然草體書寫體系中，字母必須依據其位於詞首（Initial）、詞中（Medial）、詞尾（Final）或孤立（Isolated）狀態而發生動態形變與垂直懸掛連接；抑或是南亞諸文字（天城文 Devanagari、孟加拉文、泰米爾文等）中輔音字母簇（Consonant Clusters）重組、半字形態與元音符號在主輔音上方、下方甚至左側跨字身纏繞附着的複雜音節合成機制——這些高階視覺訴求都對現代數字字體格式提出了革命性的挑戰。

爲了在根本上解決這些複雜排版問題，計算機字體工程界演化出了兩大頂峯級別的技術架構體系：
1. **OpenType 高級排版體系（OpenType Layout）**：由微軟與 Adobe 聯合制定，通過在 TrueType 或 PostScript 字體容器中深度內嵌 `GSUB`（字形替換表，Glyph Substitution Table）與 `GPOS`（字形定位表，Glyph Positioning Table）兩大二進制狀態表，輔以 `GDEF`（字形定義與附加元數據表）和 `BASE`（基準線表），建立起一套基於語言系統（Script / Language System）、排版特性（Feature）以及查找子表（Lookup / Subtable）的聲明式規則重寫與幾何微調框架。
2. **Apple AAT 體系（Apple Advanced Typography）**：由蘋果公司在經典 QuickDraw GX 革命性架構基礎上提煉而成，核心通過 `morx`（擴展變異變形表，Extended Metamorphosis Table）與 `kerx`（擴展字偶間距調整表，Extended Kerning Table），直接在字體底層植入嚴謹的**有限狀態自動機（Finite State Automaton）**。排版引擎在掃描字符流時，狀態機根據當前狀態與輸入類別驅動動態狀態轉移，並即時執行字形重排、替換與堆棧回溯動作。

在本章中，我們將深入現代字體設計的實際生產環境，全面剖析在 FontLab Studio、微軟 VOLT 以及開源字體工坊 FontForge 中，如何構建、配置與調試這套複雜的高級排版規則。

---

## 14.2 在 FontLab 中管理 OpenType 表（Managing OpenType Tables in FontLab）

FontLab 深度內嵌了基於 Adobe 特性文件定義語言（Feature Definition Language）的純文本語法編譯器。字體設計師無需手寫底層的二進制字節偏移，只需在特性編輯窗口中使用人類可讀的語法描述替換與定位規則，編譯引擎便會自動將其打包爲符合 OpenType 規範的 `GSUB` 與 `GPOS` 表。

### 14.2.1 特性定義語言（Feature Definition Language）

Adobe 特性定義語法基於嚴謹的聲明式結構，其頂層邏輯由特性聲明塊（Feature Block）構成：

```fea
feature liga {
    sub f i by f_i;
    sub f l by f_l;
    sub f f i by f_f_i;
} liga;
```

在上述代碼中，`feature liga` 聲明瞭標準連字特性（Standard Ligatures）。其內部的 `sub ... by ...` 語句代表字形替換指令。在排版引擎處理文本時，當連續遇到字形 `f` 與 `i`，便會自動將其摺疊替換爲預先設計好的連字字形 `f_i`。

::: tip 圖 14-1：FontLab 中管理與配置 OpenType 樣式的面板窗口 (Figure 14-1)
![Figure 14-1: The OpenType window in FontLab](/images/fonts-encodings/fig14-1.png)
*圖 14-1：FontLab 中管理與配置 OpenType 樣式的面板窗口。左側窗格羅列當前字體已聲明的所有 OpenType 特性；右上方爲代碼編輯區；右下方爲編譯日誌與錯誤提示反饋。*
:::

#### 1. 語言系統聲明（Language Systems）
OpenType 規則並非全局盲目生效，而是嚴格錨定在特定的書寫系統（Script）與語言體系（Language System）之下。在特性文件的最頂端，必須顯式聲明所支持的腳本與語言：

```fea
languagesystem DFLT dflt;
languagesystem latn dflt;
languagesystem latn TRK ; /* 土耳其語特殊環境 */
```

在此聲明後，排版引擎在爲特定語言環境渲染段落時，纔會激活該分支下綁定的特性。例如土耳其語中帶有小圓點的字母 `i`（點小寫 i）對應的大寫是帶點的 `İ`，而無點小寫 `ı` 對應無點大寫 `I`；因此在土耳其語環境中，必須禁止將 `fi` 替換爲常規連字，否則會導致帶點 `i` 的原字形特徵丟失，引發拼寫語義歧義。

#### 2. 字形類別（Glyph Classes）
爲了避免爲成百上千個字形逐一編寫冗長重複的替換規則，特性語言引入了命名類別（Classes）概念。字形類別以 `@` 符號爲前綴聲明：

```fea
@UPPERCASE = [A B C D E F G H I J K L M N O P Q R S T U V W X Y Z];
@SMCP = [A.sc B.sc C.sc D.sc E.sc F.sc G.sc H.sc I.sc J.sc K.sc L.sc M.sc N.sc O.sc P.sc Q.sc R.sc S.sc T.sc U.sc V.sc W.sc X.sc Y.sc Z.sc];
@FIGURES_LINING = [zero one two three four five six seven eight nine];
@FIGURES_OLDSTYLE = [zero.oldstyle one.oldstyle two.oldstyle three.oldstyle four.oldstyle five.oldstyle six.oldstyle seven.oldstyle eight.oldstyle nine.oldstyle];
```

利用字形類別，只需一條規則即可完成整套小型大寫字母（Small Capitals）的替換定義：

```fea
feature smcp {
    sub @UPPERCASE by @SMCP;
} smcp;
```

#### 3. 字形替換類型全景（Substitution Types）
OpenType `GSUB` 規範支持六種不同維度的字形替換類型：
1. **單字形替換（Single Substitution）**：一個輸入字形映射到一個輸出字形。例如上述的小寫轉小型大寫字母，或等寬數字（Tabular Figures）切換。
2. **多對一連字替換（Multiple to One / Ligature Substitution）**：多個連續輸入字形融合成一個單一的特殊字形（如 `sub f f l by f_f_l;`）。
3. **一對多分解替換（One to Multiple / Multiple Substitution）**：單個字形被分解爲若干獨立構件（如將特定複合標點拆解爲基礎字符序列）。
4. **單對多候選交替替換（Alternate Substitution）**：一個輸入字形對應多個可選的美術修飾變體，由用戶交互選擇（例如 `sub ampersand from [ampersand.1 ampersand.2 ampersand.3];`）。
5. **上下文替換（Contextual Substitution）**：僅在特定前驅或後繼字形環繞的特定語境下才觸發的替換規則。輸入字形使用單引號 `'` 標定核心匹配項：
   ```fea
   sub [f long_s]' [b h k l] by [f_alt long_s_alt];
   ```
6. **鏈式上下文替換（Chained Contextual Substitution）**：分別指定回退前綴上下文（Backtrack）、輸入匹配核心（Input）以及前瞻前置上下文（Lookahead）的最高階替換邏輯：
   ```fea
   sub @BACKTRACK @INPUT' @LOOKAHEAD by @REPLACEMENT;
   ```

::: tip 圖 14-2：FontLab 中利用 Adobe Feature 純代碼語法編輯替換與定位規則的編輯器 (Figure 14-2)
![Figure 14-2: The OpenType window in FontLab](/images/fonts-encodings/fig14-2.png)
*圖 14-2：FontLab 中利用 Adobe Feature 純代碼語法編輯替換與定位規則的編輯器。在此可以編寫複雜的查表規則（Lookups）與多重特性映射。*
:::

### 14.2.2 FontLab 的用戶交互界面（FontLab's User Interface）

FontLab 在純文本編譯器的基礎上，提供了一套深度的圖形化輔助面板。

::: tip 圖 14-3：FontLab 中測試 OpenType 語法規則實際渲染效果的交互式演練窗口 (Figure 14-3)
![Figure 14-3: The OpenType testing window in FontLab](/images/fonts-encodings/fig14-3.png)
*圖 14-3：FontLab 中測試 OpenType 語法規則實際渲染效果的交互式演練窗口。設計師可以隨時鍵入樣例文本，勾選或取消勾選特定 Feature 標籤（如 `liga`、`calt`、`onum`），即時觀察排版引擎的字形變換反饋。*
:::

在“Classes”（字形分組管理）面板中，設計師可以直接通過鼠標從字體主表格中框選字形拖入類別容器，FontLab 會自動維護類別名稱與字形列表的映射同步，防止手寫語法時產生由於字形遺漏而導致的類別長度不匹配（Class length mismatch）編譯故障。

::: tip 圖 14-4：FontLab 中將字形集合聚類爲命名類別（Classes）的分組管理面板 (Figure 14-4)
![Figure 14-4: The Classes panel in FontLab](/images/fonts-encodings/fig14-4.png)
*圖 14-4：FontLab 中將字形集合聚類爲命名類別（Classes）的分組管理面板。*
:::

在動態預覽（Preview）窗口中，設計師不僅能審查靜態字形輪廓，還能以不同字號實時渲染連字與複雜字偶距調整效果。

::: tip 圖 14-5：FontLab 的動態預覽（Preview）窗口 (Figure 14-5)
![Figure 14-5: The Preview panel window in FontLab](/images/fonts-encodings/fig14-5.png)
*圖 14-5：FontLab 的動態預覽（Preview）窗口，用於實機觀察特性規則生效後的實際視覺灰度與間距韻律。*
:::

---

## 14.3 在微軟 VOLT 中管理 OpenType 表（Managing OpenType Tables in VOLT）

微軟開發的 **VOLT（Visual OpenType Layout Tool，視覺化 OpenType 佈局工具）** 是數字排印史上的一座豐碑。VOLT 是一款運行在 Windows 環境下的專業級工程軟件，其核心設計目標是爲世界上最嚴苛複雜的書寫系統（如阿拉伯文、烏爾都文納斯塔裏克體 Nastaliq、天城文、藏文等）提供無可挑剔的高精度交互式佈局生產能力。

::: tip 圖 14-6：微軟 VOLT（Visual OpenType Layout Tool）的項目總覽工程面板 (Figure 14-6)
![Figure 14-6: The project window in VOLT](/images/fonts-encodings/fig14-6.png)
*圖 14-6：微軟 VOLT（Visual OpenType Layout Tool）的項目總覽工程面板。自上而下分別展示字體基礎度量、腳本與語言系統樹、特性綁定列表、獨立 Lookup 查表池以及全局字形組（Groups）。*
:::

### VOLT 的工程架構哲學
與 FontLab 依賴代碼編譯器不同，VOLT 採用高度解耦的數據庫模型：
1. **獨立查找池（Lookups Pool）**：所有的字形替換與定位邏輯均作爲獨立的 Lookup 對象存在，擁有唯一的工程名稱與行爲定義。
2. **多對多特性綁定（Feature Mapping）**：一個排版特性（如 `init`、`medi`、`fina`）僅僅是一個指向一個或多個 Lookup 的指針集合。不同的語言環境可以自由複用已有的 Lookup 鏈。
3. **視覺化錨點吸附系統（Visual Anchor Positioning）**：在阿拉伯文或印度諸文字中，一個字形上可能包含多個物理附着錨點（例如標音符號附着點 `mark`、連字次級構件附着點 `mkmk`、草體基線進出點 `curs`）。VOLT 允許設計師在交互式畫布中通過鼠標拖動十字瞄準線，以亞像素精度將附加符號的附着點與底字錨點嚴絲合縫地重合鎖定。

::: tip 圖 14-7：微軟 VOLT 中定義複雜字形替換邏輯的工程配置窗口 (Figure 14-7)
![Figure 14-7: The substitution window in VOLT](/images/fonts-encodings/fig14-7.png)
*圖 14-7：微軟 VOLT 中定義複雜字形替換邏輯的工程配置窗口。直觀呈現輸入字形隊列與匹配替換產物。*
:::

::: tip 圖 14-8：微軟 VOLT 中利用交互式錨點配置字形精確定位（Positioning）的窗口 (Figure 14-8)
![Figure 14-8: The positioning window in VOLT](/images/fonts-encodings/fig14-8.png)
*圖 14-8：微軟 VOLT 中利用交互式錨點配置字形精確定位（Positioning）的窗口。通過視覺化調整上標、下標與變音符號的物理錨點，實現字符流的動態咬合。*
:::

VOLT 還內置了全球最強大的打樣渲染與調試窗口（Proofing Window）。在打樣窗口中，設計師可以輸入整段複雜經文，單步回放排版引擎執行的每一輪 Lookup 變換，實時捕獲定位漂移或連字擊穿故障。

::: tip 圖 14-9：微軟 VOLT 中對整篇複雜排版文本進行實機渲染打樣驗證（Proofing）的工作窗口 (Figure 14-9)
![Figure 14-9: The proofing window in VOLT](/images/fonts-encodings/fig14-9.png)
*圖 14-9：微軟 VOLT 中對整篇複雜排版文本進行實機渲染打樣驗證（Proofing）的工作窗口。*
:::

---

## 14.4 在 FontForge 中管理 OpenType 表（Managing OpenType Tables in FontForge）

作爲現代自由軟件世界的旗艦字體編輯器，喬治·威廉姆斯（George Williams）開發的 FontForge 提供了全功能且極具學術深度的高級排版管理界面。在 FontForge 中，設計師可以通過直觀的樹狀菜單直接操作 `GSUB` 與 `GPOS` 的每一個層級。

### 14.4.1 物理定位錨點（Anchors）

在字形編輯畫布中，設計師可以隨時右鍵執行“Add Anchor”（添加定位錨點）。每一個錨點被賦予一個命名類別（Anchor Class），並被歸類爲“Base”（基底附着點）、“Mark”（浮動符號附着點）或“Ligature”（連字多構件附着點）。

::: tip 圖 14-10：FontForge 中在字形畫板中建立物理定位錨點（左）與錨點大類配置面板（右） (Figure 14-10)
![Figure 14-10: Two anchors defined in the glyph window (left) and the anchor-class window (right) in FontForge](/images/fonts-encodings/fig14-10.png)
*圖 14-10：FontForge 中在字形畫板中建立物理定位錨點（左）與錨點大類配置面板（右）。圖左展示了爲重音符號與上下標預留的物理座標十字靶；圖右展示了該錨點大類在全局度量系統中的繼承與匹配規則。*
:::

### 14.4.2 非上下文替換（Noncontextual Substitutions）

對於單字形變體、非上下文連字以及交替候選字，FontForge 提供了極簡的嚮導式面板。在字形信息窗口的“Substitutions”標籤頁中，只需點選目標特性（如 `smcp` 或 `liga`），並指定目標字形名稱即可完成映射。

::: tip 圖 14-11：FontForge 中單字形替換的交互式配置面板 (Figure 14-11)
![Figure 14-11: Left: the glyph window, single substitution tag; Right: the window for a new single substitution in FontForge](/images/fonts-encodings/fig14-11.png)
*圖 14-11：FontForge 中單字形替換（Single Substitution）的交互式配置面板。左側爲字形屬性窗口標籤；右側爲新建單字形替換的參數綁定對話框。*
:::

### 14.4.3 非上下文定位（Noncontextual Positionings）

定位規則用於修正字形的幾何位置與進退度量。最常見的定位規則是字偶間距微調（Pairwise Kerning，特性標籤 `kern`）。在 FontForge 中，設計師既可以爲特定字母對（如 `T` 與 `o`、`A` 與 `V`）單獨設置水平位移修正量 $\\Delta x$，也可以建立基於字形分類的類別字偶距矩陣（Class Kerning Matrix），將成百上千個帶有重音變體的拉丁字母按輪廓特徵歸併計算，極大地壓縮了最終字體的二進制體積。

::: tip 圖 14-12：FontForge 中簡單單字定位（左）與字偶間距微調（右）的配置界面 (Figure 14-12)
![Figure 14-12: The windows for simple (left) and pairwise (right) positionings in FontForge](/images/fonts-encodings/fig14-12.png)
*圖 14-12：FontForge 中簡單單字定位（左，Simple Positioning）與字偶間距微調（右，Pairwise Positioning）的配置界面。*
:::

### 14.4.4 上下文替換與定位（Contextual Substitutions and Positionings）

當排版邏輯需要根據周圍環境動態抉擇時，FontForge 會啓動鏈式上下文替換引導向導。嚮導將複雜的鏈式規則拆解爲四個清晰的漸進步驟：
1. **指定匹配格式（Coverage Format）**：選擇是以字形列表（Glyph List）、類別列表（Class List）還是覆蓋範圍表（Coverage Table）組織數據；
2. **定義回退上下文（Backtrack Glyphs）**：錄入匹配核心之前必須出現的字形模式序列；
3. **定義前瞻上下文（Lookahead Glyphs）**：錄入匹配核心之後必須出現的字形模式序列；
4. **綁定嵌套子查找（Nested Lookups）**：指定當模式完全吻合時，對核心位置字形所執行的次級替換或位移操作。

::: tip 圖 14-13：FontForge 中配置鏈式上下文替換的前四個關鍵引導步驟 (Figure 14-13)
![Figure 14-13: The first four steps for defining a chained contextual substitution in FontForge](/images/fonts-encodings/fig14-13.png)
*圖 14-13：FontForge 中配置鏈式上下文替換（Chained Contextual Substitution）的前四個關鍵引導步驟。[a] 選擇特性所屬格式；[b] 設定上下文序列類別；[c] 構建前後依賴拓撲；[d] 確認並綁定觸發動作。*
:::

---

## 14.5 在 FontForge 中管理 AAT 表（Managing AAT Tables in FontForge）

Apple Advanced Typography（AAT）是數字排印史上在技術深度上極富遠見的設計。與 OpenType 依賴龐大靜態查表的模式截然不同，AAT 將整個文本排版過程抽象爲數學上的**確定性有限狀態自動機（DFA, Deterministic Finite Automaton）**。

### 14.5.1 特性與選擇器（Features and Selectors）

在 AAT 哲學中，每一個排版視覺維度被稱爲一個“特性類型（Feature Type）”，而在該特性之下包含若干互相排斥或可多選的“選擇器（Selector）”。例如在特性類型 1（Ligatures）下，包含“Common Ligatures On/Off”、“Rare Ligatures On/Off”等選擇器。

::: tip 圖 14-14：在 AAT 規範中編輯與配置特性名稱與選擇器的面板 (Figure 14-14)
![Figure 14-14: Editing the names of AAT features and selectors](/images/fonts-encodings/fig14-14.png)
*圖 14-14：在 AAT 規範中編輯與配置特性名稱（Features）與選擇器（Selectors）的面板。左側羅列特性大類（如連字、小型大寫字母、分數），右側配置其默認開啓狀態與多語言本地化標籤。*
:::

### 14.5.2 在 FontForge 中管理 AAT 有限狀態自動機（Managing AAT's Finite Automata in FontForge）

AAT 的核心引擎依賴於**狀態轉移表（State Transition Table）**。其算法運轉流程如下：
1. **輸入字符流類別劃分（Class Table）**：字體將所有字形映射爲有限個離散類別（Classes），例如將所有普通小寫字母歸爲 Class 0，特定連字前驅 `f` 歸爲 Class 1，元音字母歸爲 Class 2 等。
2. **狀態矩陣尋址（State Table）**：當前狀態機處於某個具體狀態（如初始狀態 State 0）。當接收到類別爲 $c$ 的字形輸入時，算法在二維狀態轉移矩陣中查詢行（State）與列（Class）的交叉點。
3. **執行原子動作（Transition Actions）**：交叉單元格內存儲兩個核心指令：
   * **下一轉移狀態（Next State）**：狀態機跳轉至新的目標狀態；
   * **字形堆棧動作（Glyph Actions）**：指示當前字形是否推入暫存堆棧（Mark）、是否與堆棧頂部字形發生重排置換、或者執行特定的字形替換。

::: tip 圖 14-15：AAT 狀態轉移表與字形重排算法的輸入配置界面全貌 (Figure 14-15)
![Figure 14-15: Class and state tables for rearrangement of glyphs in AAT](/images/fonts-encodings/fig14-15.png)
*圖 14-15：AAT 狀態轉移表與字形重排算法的輸入配置界面全貌：[a] 字符類別劃分與狀態轉移矩陣網格；[b] 與 [c] 上下文字形替換與堆棧動作控制表。*
:::

這種基於狀態機的排版範式運算複雜度極低，能夠以嚴格的單遍線性掃描（$O(n)$ 時間複雜度）完成極其複雜的雙向文字重排與動態變異渲染。時至今日，AAT 在 macOS 與 iOS 底層文本系統（Core Text）中依然扮演着不可替代的關鍵角色，與 OpenType 共同構成了現代數字字體技術的璀璨雙璧！
