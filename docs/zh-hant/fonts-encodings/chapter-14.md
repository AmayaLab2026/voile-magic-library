---
title: "第 14 章：豐富字體：高級排版功能"
description: "OpenType 與 AAT 高級排版功能深度解析：AFDKO 特性語法規範、微軟 VOLT 工程實戰、Apple Advanced Typography (AAT) 有限狀態自動機、GSUB/GPOS 查找表體系。"
---

# 第 14 章：豐富字型：高階排版功能

*譯者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

### Chapter 14: Enriching Fonts: Advanced Typography

本章標題所指的“高階排版功能”，特指微軟（Microsoft）、Adobe 與蘋果（Apple）公司在基礎 TrueType 格式之上引入的擴充套件布局表系統——即當今數字印藝領域的兩大支柱體系：**OpenType** 與 **Apple Advanced Typography（AAT）**。

在鉛字活字印刷與機械排字機時代，排版師面對多語言混排、阿拉伯文連寫變形、南亞諸文字子音簇疊印、以及嚴苛的西文活字連字（Ligatures）、小型大寫體（Small Capitals）、老式不等高數字（Oldstyle Figures）與上下文長短 's' 替換時，依賴的是人工的揀字經驗與手工墊片微調。進入早期個人電腦桌面出版時代後，傳統 PostScript Type 1 與基礎 TrueType 字型僅僅是一張平面的“字元編碼到字形外觀”的靜態投影表（`cmap`），對於上下文變形和複雜書寫系統，只能依賴作業系統層或獨立應用程式硬編碼的排版外掛（如早期蘋果系統的 QuickDraw GX 擴充套件或 QuarkXPress、InDesign 的私有字形替換引擎）。

OpenType 與 AAT 的革命性突破在於：**將文字動態排版的“智慧規則”直接固化、封裝在字型檔案自身內部**。排版引擎（Shaping Engine，如現代開源基石 HarfBuzz、Windows 系統的 DirectWrite、macOS 系統的 CoreText）不再需要硬編碼各語系的拼寫語法，而是遵循統一的規範讀取字型檔內部的排版規則表，由字型設計大師完全掌控其字形在不同語言環境、上下文語境下的變形、連綴與微觀幾何位移。

---

## 1. 排版智慧化的演進與正規化轉移（Introduction）

### 1.1 從字元到字形：文字整形（Text Shaping）的動態蛻變

現代數字文字處理的核心理論，建立在**字元（Character）**與**字形（Glyph）**的嚴格二元分離之上：
* **字元**：是計算機資訊處理系統中的純粹語義抽象單位，由 Unicode 標量值（Code Point）唯一標識，代表“這個文字是什麼”；
* **字形**：是呈現在螢幕畫素或紙張墨跡上的具體可視物理形態，由字型檔中的輪廓資料（Bézier 曲線段）、圖元指令與空間度量構成，代表“這個文字怎麼呈現”。

在簡單西方文字的無修飾排版中，一個字元通常對應一個字形（例如字元 'A' 對應字形 `A`）。但在世界各大原生文字系統與高階西文典籍排印中，字元與字形之間存在著極度複雜的非單射、非雙射的動態對映關係：
1. **多對一對映（Many-to-One）**：連字現象。如輸入字元序列 `'f' + 'i'`，排版引擎應將其自動融鑄為單一的高階連字型字形 `fi`（`f_i`）；在阿拉伯文中，輸入 `'l' + 'a'` 必須強制合成為連字 `lam_alif`；
2. **一對多對映（One-to-Many）**：字形分解。如某些南亞印度系文字（Indic Scripts）或東南亞高棉文（Khmer），一個母音字元在邏輯上掛載於子音之後，但在實際書寫視覺上，其筆畫必須分裂拆解為前置部首、上標聲調與後置主幹三個獨立的物理字形，環繞包圍子音字母；
3. **一對一上下文條件變體（One-to-One Contextual Variation）**：阿拉伯文與希伯來文的字母在詞首（Initial）、詞中（Medial）、詞尾（Final）與孤立狀態（Isolated）具有截然不同的四種書寫骨架；在古典英語排印中，字母 `'s'` 若出現在詞首或詞中應選用長長伸展的 `longs`（'ſ'），而出現在詞尾或特定子音後則選用常規的圓弧 `'s'`；
4. **二維空間微觀吸附（2D Spatial Attachment）**：希臘文多重變音符（Polytonic Accents）、希伯來文母音發音符號（Nikud）、阿拉伯文點標（Nuqta）與印度天城文半子音疊印，要求符號不僅要在水平方向緊跟基字，更必須依據基字的具體幾何輪廓高度、筆畫傾斜角，在二維空間內精準定位吸附。

現代排版引擎將文字從邏輯碼點轉化為最終螢幕呈現的幾何拓撲流，其數學處理管線可嚴格抽象為以下四階轉換：

$$\text{Unicode Code Points} \xrightarrow{\quad\text{cmap 映射}\quad} \text{Glyph IDs} \xrightarrow{\quad\text{GSUB 替换}\quad} \text{Glyph IDs} \xrightarrow{\quad\text{GPOS 定位}\quad} \text{Positioned Glyphs}$$

---

### 1.2 高階排版雙翼：字形替換（GSUB）與幾何定位（GPOS）

在 OpenType 架構中，實現上述智慧排版的動力核心被清晰解耦為兩大並行的二進位制資料表：負責“改換形態”的 **`GSUB`（Glyph Substitution Table，字形替換表）** 與負責“空間微調”的 **`GPOS`（Glyph Positioning Table，字形定位表）**。

#### 1. 字形替換的六大形態（GSUB）

`GSUB` 表內部被組織為一個結構精密的樹狀層級體系：包含指令碼列表（ScriptList）、語言系統列表（LangSysList）、排版特性列表（FeatureList）與查詢表列表（LookupList）。其中每個查詢表根據排印學需求，被嚴格劃分為六種原子操作形態：

1. **單字替換（Single Substitution, Lookup Type 1）**：將單一輸入字形等量替換為另一個目標字形。
   * *典型場景*：小寫字母替換為小型大寫體（Small Caps, `smcp`），如 `a` $\to$ `a.sc`；表意數字替換為等寬表格數字（Tabular Figures, `tnum`）或老式非等高數字（Oldstyle Figures, `onum`）。
2. **多字替換（Multiple Substitution, Lookup Type 2）**：將單一輸入字形拆解為由兩個或更多字形構成的有序序列。
   * *典型場景*：歷史活字中未編碼連字的動態拆分，如將歷史遺留字形 `ffi` 拆解為獨立的 `f` + `f` + `i`；在印度系文字中將複合子音印章分解為獨立字母與虛線子音架。
3. **備選替換（Alternate Substitution, Lookup Type 3）**：為單一輸入字形提供一個可選的字形陣列集合，允許使用者或排版軟體根據審美需要互動式選擇。
   * *典型場景*：書法花體變體（Swashes, `swsh`），如著名書法字型 Zapfino 中為字母 `'d'` 提供了多達九種飄逸長尾變體；樂譜符號與花邊裝飾符（Ornaments, `ornm`）的選擇。
4. **合字替換（Ligature Substitution, Lookup Type 4）**：將一個嚴格按序出現的輸入字形序列融鑄坍縮為一個單一的目標字形。
   * *典型場景*：標準拉丁連字（Standard Ligatures, `liga`），如 `'f' + 'i' \to 'fi'`、`'f' + 'l' \to 'fl'`；歷史珍本連字（Discretionary Ligatures, `dlig`），如 `'c' + 't' \to 'ct'`、`'s' + 't' \to 'st'`；德文長 's' 連字（Historical Ligatures, `hlig`）；阿拉伯文中極為普遍的二字、三字連寫整體。
5. **上下文替換（Contextual Substitution, Lookup Type 5）**：僅當目標字形處在特定的前驅或後繼字元上下文字串中時，才觸發對輸入序列中字形的替換。但經典上下文替換有一個致命缺陷：被匹配的“上下文環境字元”會被當前子表消耗鎖定，無法參與後續鏈條的進一步替換。
6. **鏈式上下文替換（Chained Contextual Substitution, Lookup Type 6）**：上下文替換的最強形態。允許排版師將上下文環境明確劃分為三大獨立隔離區間：**回溯序列（Backtrack Glyphs）**、**匹配目標序列（Input Glyphs）** 與 **前瞻序列（Lookahead Glyphs）**。只有當這三個區間的字形同時全部命中預設規則時，才對匹配目標區間內的指定字形執行級聯替換，而回溯與前瞻字元保持完好，繼續供下游規則鏈條匹配。
7. **反向鏈式上下文單字替換（Reverse Chaining Contextual Single Substitution, Lookup Type 8）**：專為烏爾都語（Urdu）波斯折體（Nastaliq）等極端書寫系統量身定製。它逆轉了常規文字掃描方向，從左至右逆向評估上下文，以適配從右向左書寫且筆畫沿對角線階梯向下懸垂坍落的特殊文字。

#### 2. 字形微觀幾何定位的六大形態（GPOS）

如果說 `GSUB` 決定了“顯示哪個字形”，那麼 `GPOS` 則徹底掌控了“字形顯示在何處”。在 `GPOS` 體系中，每一個字形的最終空間位置由一個四元值記錄（Value Record）決定：

$$\langle xPlacement \quad yPlacement \quad xAdvance \quad yAdvance \rangle$$

* $xPlacement$ / $yPlacement$：字形輪廓相對於邏輯原點的水平與垂直偏移量（平移繪製起點，但不改變排版筆刷前進量）；
* $xAdvance$ / $yAdvance$：字形繪製完成後，文字排版游標在水平與垂直軸線上的推進距離（前進量，Advance Width/Height）。

圍繞該值記錄，`GPOS` 定義了六大空間幾何定位查詢表型別：
1. **單一微調（Single Adjustment, Lookup Type 1）**：針對單個字形調整其外形偏移或推進度量。
   * *典型場景*：全大寫排版微調（Capital Spacing, `cpsp`），當文字全為大寫字母時，將括號 `()`、連字元 `-` 和破折號 `--` 向上抬升若干設計單位，以對齊大寫字母的垂直視覺中心。
2. **字偶對微調（Pair Adjustment / Kerning, Lookup Type 2）**：針對特定的兩兩相鄰字形組合，微調它們之間的相對間隙。
   * *典型場景*：經典字距微調（`kern`），如在 `'T'` 與 `'o'`、`'A'` 與 `'V'` 之間施加負向水平間隙，消除筆畫負空間造成的排版空洞。支援基於具體字形對（Glyph-pair）與基於形態類（Class-based）的矩陣運算。
3. **草書平滑咬合（Cursive Attachment, Lookup Type 3）**：專為阿拉伯文、波斯體（Nastaliq）以及手寫連體設計。在每個字形的連線入口放置進入錨點（Entry Anchor），在出口放置退出錨點（Exit Anchor）。排版引擎在從右向左推進時，自動平移後一個字形，使後字的 Entry 錨點與前字的 Exit 錨點在空間中嚴格重合，形成平滑如行雲流水的斜角或弧線連綴。
4. **標音符號附著於基字（Mark-to-Base Attachment, Lookup Type 4）**：將重音符號、聲調或點標精準吸附於基本字母。
   * *典型場景*：在小寫字母 `'e'` 的頂部中心錨點上吸附尖音符（Acute）`´`，使組合而成的 `é` 變音符無論基字字寬如何變化，均穩固居中。
5. **標音符號附著於合字（Mark-to-Ligature Attachment, Lookup Type 5）**：連字型字形內部包含多個文字成分。該查詢表允許在合字內部為每個邏輯構件分別指定錨點集合，使變音符能夠精準降落在合字的第一個或第二個組成字母上方。
6. **標音符號多層附著（Mark-to-Mark Attachment, Lookup Type 6）**：處理變音符號的層疊堆印。
   * *典型場景*：在越南語排印中，字母往往同時擁有母音變音符（如揚抑符 `^`）和聲調符號（如銳音符 `´`），Mark-to-Mark 定位使聲調符能夠精準疊加在母音變音符的頂端，避免兩者在垂直空間發生重疊穿模。

---

### 1.3 OpenType 佈局表的底層二進位制拓撲與關鍵基礎設施

要透徹理解 OpenType 引擎的執行機理，必須深入解剖其在二進位制檔案中的資料拓撲結構。無論是 `GSUB` 還是 `GPOS` 表，其頂層均嚴格包含一個表頭（Header）：
* `uint16 majorVersion` / `uint16 minorVersion`：版本識別符號（通常 1.0 或 1.1）；
* `Offset16 ScriptListOffset`：指向指令碼列表（ScriptList）的位元組偏移量；
* `Offset16 FeatureListOffset`：指向特性列表（FeatureList）的位元組偏移量；
* `Offset16 LookupListOffset`：指向查詢表列表（LookupList）的位元組偏移量；
* 在 1.1 版本中，還額外包含一個 `Offset32 FeatureVariationsOffset`，用於支援 OpenType 1.8 可變字型根據軸線座標動態切換替換規則！

#### 1. 覆蓋表（Coverage Tables）的兩大格式規範
在任何一個查詢子表中，排版引擎做的第一件事絕不是盲目遍歷整個字型檔，而是透過**覆蓋表（Coverage Table）**快速判斷當前字形是否屬於該子表的作用物件：
* **Coverage Format 1（離散索引表）**：包含一個按 GID 升序嚴格排列的字形陣列 `GlyphID glyphArray[glyphCount]`。引擎透過二分查詢法在 $O(\log N)$ 時間內判定當前字形是否存在，若存在則返回其在陣列中的索引作為其覆蓋索引（Coverage Index）；
* **Coverage Format 2（連續區間範圍表）**：當被覆蓋的字形在 GID 上是連續大塊分佈時（例如連續 500 個漢字變體），Format 1 會浪費巨量記憶體。Format 2 引入了範圍記錄結構 `RangeRecord`：
  ```c
  struct RangeRecord {
      uint16 startGlyphID;      /* 区间起始字形 GID */
      uint16 endGlyphID;        /* 区间终结字形 GID (包含) */
      uint16 startCoverageIndex;/* 该区间首个字形对应的覆盖索引 */
  };
  ```
  引擎僅需儲存若干個區間端點，即可瞬間對映成千上萬個連續字形，極大壓縮了字型體積並提升了查詢命中速度。

#### 2. 分類定義表（Class Definition Tables）
在基於類別的字距調整（Class-based Kerning）或上下文分類替換中，字形必須被離散投影到一個整數類索引（Class ID，通常 0 為預設未分類）：
* **ClassDef Format 1**：定義了一個基準起始字形 `startGlyphID`，緊隨其後為一個緊湊的單位元組/雙位元組類值陣列 `uint16 classValueArray[glyphCount]`；
* **ClassDef Format 2**：採用三元組範圍記錄 `ClassRangeRecord`（`startGlyphID`, `endGlyphID`, `classValue`），高效對連續字元塊賦予相同類別屬性。

#### 3. GDEF、BASE 與 JSTF 支撐底座
* **`GDEF`（字形定義表）**：為全字型建立字形本體論屬性分類。它包含三大核心子表：
  1. `GlyphClassDef`：將字形嚴格歸類為 Base（基字）、Ligature（合字）、Mark（附加音標）或 Component（構件）；
  2. `AttachList`：記錄特定複雜字形上允許其他字元連線的物理頂點輪廓節點號；
  3. `LigCaretList`：定義合字內部允許閃爍文字游標的垂直剖分位置（Carets），使得使用者在文字編輯器中按向左箭頭時，游標能精準停靠在 ‘ﬁ’ 合字中間 ‘f’ 與 ‘i’ 的交界處。
* **`BASE`（跨語系基線規範表）**：當多語言在同一水平行混排時，西文的基線是小寫字母的底部，中文漢字採用正方形字身框垂直居中的表意字中線（Ideographic Baseline），而印度梵文天城文則以字母頂端的平直連梁為懸掛基線（Hanging Baseline）。`BASE` 表給出了各指令碼基線之間的相對差值，使文字渲染器在混排拉丁字母與梵文時，能夠自動上下平移字元，保持閱讀視覺重心的絕對統一；
* **`JSTF`（兩端對齊表）**：針對阿拉伯文等高難度指令碼的兩端齊平排版。定義了多級優先順序流水線（Priority Stages）：在第一級，優先使用加長字形（Swashes）；在第二級，呼叫連線伸展字元（Kashida）；在第三級，微調詞間距。

#### 4. 標準排版特性標籤體系（Standard Feature Tags）

OpenType 官方登錄檔中定義了近百個由 4 位元組 ASCII 字元構成的排版特性標籤（Feature Tags）。表 14-1 彙總了當今出版界最核心的特性及其行為：

| 特性標籤 | 英文全稱 | 核心排印功能與轉換行為 | 預設開啟狀態 |
| :--- | :--- | :--- | :--- |
| `liga` | Standard Ligatures | 標準審美連字（如 fi, fl, ffi, ffl） | 預設開啟（ON） |
| `dlig` | Discretionary Ligatures | 裝飾性/自由連字（如 st, ct, Qu, Th） | 預設關閉（OFF） |
| `hlig` | Historical Ligatures | 歷史典籍珍本文獻連字（如 ſt, ſi, ſl） | 預設關閉（OFF） |
| `smcp` | Lowercase to Small Caps | 小寫字母轉為真小型大寫體（保持大寫高度與磅重統一） | 預設關閉（OFF） |
| `c2sc` | Capitals to Small Caps | 大寫字母轉為小型大寫體（用於縮寫詞頭等混排場景） | 預設關閉（OFF） |
| `onum` | Oldstyle Figures | 非等高老式數字（高低錯落，融入正文行氣流） | 預設關閉（OFF） |
| `lnum` | Lining Figures | 等高全齊平現代數字（與大寫字母齊平，適合標題） | 預設開啟（標題） |
| `pnum` | Proportional Figures | 比例間距數字（各數字擁有符合自身骨架的自然字寬） | 預設開啟（正文） |
| `tnum` | Tabular Figures | 表格等寬數字（所有數字寬度絕對一致，確保財務報表垂直對齊） | 預設開啟（表格） |
| `frac` | Diagonal Fractions | 斜線對角分數（將 `1/2` 等序列自動轉換為專業分數分子分母字形） | 預設關閉（OFF） |
| `ordn` | Ordinals | 序數詞上標（如英語 1st, 2nd 或法語 1er, 2e） | 預設關閉（OFF） |
| `zero` | Slashed Zero | 斜槓零（在數字 0 中增加斜槓或圓點，與大寫字母 O 嚴格隔離） | 預設關閉（OFF） |
| `swsh` | Swash | 書法飄逸花體（為字母提供長長延伸的書法出入刀筆畫） | 預設關閉（OFF） |
| `titl` | Titling | 標題專用大寫體（筆畫細緻，專門最佳化大磅字排版） | 預設關閉（OFF） |
| `kern` | Kerning | 字距微調（消除字母間負空間視覺縫隙） | 預設開啟（ON） |
| `cpsp` | Capital Spacing | 全大寫排版間距擴充套件與符號垂直抬升 | 預設關閉（OFF） |
| `locl` | Localized Forms | 本地語言定製字形（如土耳其語無點 i、波蘭語 kreska 傾角） | 預設開啟（強制） |

---


### 1.4 工業級西文經典排印四大數字體系與高階特性矩陣

數字在現代排印學中具有極其複雜的視覺層級需求。一款頂級的專業西文字型通常必須同時配備**四套截然不同的阿拉伯數字系統**，由 OpenType 特性按需排程：

#### 1. 西文四大數字體系的幾何與功能對立
1. **等高齊線數字（Lining Figures, `lnum`）**：所有數字的高度嚴格齊平，且頂端與大寫字母（Cap Height）或接近大寫字高完全平齊，基底與普通字母基線對齊。適合與全大寫字母混排、海報標題與大字標語。
2. **不等高老式數字（Oldstyle Figures / Non-lining Figures, `onum`）**：具有類似小寫字母的升部（Ascender）與降部（Descender）。例如數字 `6` 與 `8` 向上伸展衝頂，`3`、`4`、`5`、`7`、`9` 向下伸出基線跌入降部區，而 `0`、`1`、`2` 則保持在 x 字高（x-Height）以內。老式數字在排印古典正文段落時，其墨跡灰度與小寫行氣渾然一體，絕不會像全齊線數字那樣在大片正文中產生突兀扎眼的“黑斑”。
3. **比例間距數字（Proportional Figures, `pnum`）**：每個數字的字身外框（Bounding Box）與推進寬度（Advance Width）根據自身骨架量身定製。例如狹窄的數字 `1` 擁有極小的字寬，而豐滿的數字 `0` 與 `8` 則擁有較寬的字身。比例數字使文字行具有勻稱優美的自然節奏。
4. **表格等寬數字（Tabular Figures, `tnum`）**：所有 0 到 9 的數字，乃至小數點、逗號與美元貨幣符號，其推進寬度被強制鎖定為完全相同的固定數值（例如 1000 設計單位字身框中的 550 單位）。在財務報表、資產負債表與統計圖表中，只有表格等寬數字能夠確保不同行之間的千位、百位與小數位實現如同機械遊標卡尺般的絕對垂直縱向對齊！

#### 2. 花體修飾（Swashes）與樣式集（Stylistic Sets）的高階排程
* **`swsh`（自由花體）與 `cswh`（上下文花體）**：古典書法花體字形若在單詞中間隨意出現，其長長的延伸筆畫往往會與相鄰字母發生嚴重的穿模碰撞。因此現代字型工程普遍使用 `cswh` 特性：透過上下文規則，僅在單詞的首字母（詞首花體）或最後一個字母（詞尾收刀花體）處安全觸發花體變體，中間字母自動回退為緊湊的常規形態；
* **樣式集（`ss01` 至 `ss20`）**：允許字型設計師為整個字型打包提供多達 20 套獨立的風格主題包。例如一套專門模仿包豪斯幾何風格的幾何無襯線大寫集合（開啟 `ss01`），或一套針對手寫體字跡的粗糙墨暈風化變體集合（開啟 `ss02`），使用者可在排版軟體中一鍵全域性切換。


## 2. 在 FontLab 中管理 OpenType 表與 AFDKO 特性定義語言

在桌面字型設計軟體演進史中，FontLab Studio 4 與 5 率先深度整合了由 Adobe 開發的 **AFDKO（Adobe Font Development Kit for OpenType）** 語法編譯器 `makeotf`，開創了透過純文字高階程式碼宣告 OpenType 特性的現代工業正規化。

### 2.1 AFDKO 特性定義語言的完整語法規範

AFDKO 語法採用類似於 C 語言與 PostScript 的大括號分塊結構，每一條語句必須以分號（`;`）結尾。

#### 1. 字形類（Glyph Classes）的定義與集合運算

字形類是 AFDKO 程式碼的基石，以 `@` 字元為字首。它將具有相同排印屬性的多個字形繫結為一個具名集合：

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

#### 2. 書寫系統、語言與特性的層級結構

字型檔必須首先宣告支援的指令碼（Script）與語言系統（Language System）：

```fea
languagesystem DFLT dflt;    # 兜底默认系统
languagesystem latn dflt;    # 拉丁脚本默认语言
languagesystem latn TRK ;    # 拉丁脚本土耳其语（支持点号 i 严格隔离）
languagesystem arab ARA ;    # 阿拉伯脚本阿拉伯语
languagesystem arab URD ;    # 阿拉伯脚本乌尔都语
```

在特性塊定義中，排版師將具體的查詢規則包裹在 `feature <tag> { ... } <tag>;` 中：

```fea
feature liga {
    # 查找规则写入此处
    sub f f i by f_f_i;
    sub f i by f_i;
    sub f l by f_l;
} liga;
```

#### 3. 命名查詢表（Named Lookups）與標記標誌位（`lookupflag`）

為了在不同特性之間複用規則，或精細控制規則的執行順序與過濾條件，AFDKO 支援具名查詢表：

```fea
lookup SMALL_CAPS_SUB {
    sub [a-z] by [a.sc-z.sc];
} SMALL_CAPS_SUB;

feature smcp {
    lookup SMALL_CAPS_SUB;
} smcp;
```

查詢表可透過 `lookupflag` 指令直接控制底層渲染引擎的遍歷過濾策略：
* `RightToLeft`：指示規則在從右向左文字流中應用；
* `IgnoreBaseGlyphs`：引擎在匹配上下文字串時，自動跳過所有基字（僅在標記符號之間匹配）；
* `IgnoreLigatures`：自動跳過所有合字；
* `IgnoreMarks`：**工業級排印極其關鍵的指令**！指示排版引擎在掃描上下文時，自動無視插在字母中間的所有重音、聲調與發音點標。例如，在處理帶重音的法語單詞時，`sub f i by f_i;` 即使中間插入了零寬重音符號，依然能夠穿透標記成功觸發連字！

#### 4. 字形替換規則（GSUB 規則全集）

AFDKO 覆蓋了全部 6 種 GSUB 型別的程式碼寫法：

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

上述 `ignore sub` 語法展示了 AFDKO 極其高超的上下文控制力：透過在 `ignore sub` 語句中用逗號隔開多個排除模式，先排除掉前驅帶大寫字母或後繼帶大寫字母的所有單詞，緊隨其後的 `sub` 即可安全地將孤立的 "TEX" 融鑄為精美的標誌合字。

#### 5. 字形定位規則（GPOS 規則全集）

在 AFDKO 中，位置調整使用 `pos` 關鍵字宣告：

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

#### 6. 光學尺寸特性（`size`）與備選彙總（`aalt`）

在所有 OpenType 特性中，有兩個具有超脫於常規排版邏輯的特殊語法地位：
1. **`aalt`（All Alternates，全備選彙總）**：其唯一使命是將字型檔中分散在 `smcp`, `onum`, `salt`, `titl` 等各個獨立特性中的所有單字替換變體進行集中大彙編，供 Adobe InDesign 等軟體的“字形調板（Glyphs Panel）”一次性向使用者展示當前字元的所有可用外觀變體。它通常必須置於特性的最首行：
   ```fea
   feature aalt {
       feature smcp;
       feature c2sc;
       feature onum;
       feature salt;
   } aalt;
   ```
2. **`size`（光學尺寸後設資料宣告）**：用於彌補傳統數字字型徹底抹殺金屬活字“物理級磅重尺寸微調”的巨大缺陷。在 AFDKO 中，`size` 特性不包含任何字形替換或定位規則，而是包含四個核心工程浮點引數與一個多語言名稱塊：
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

### 2.2 FontLab Studio 圖形化工作流實戰

在 FontLab Studio 中，排版師不僅可以直接編寫上述底層 AFDKO 程式碼，更可以透過豐富的圖形化視窗直觀管理特性、類與視覺錨點：

::: tip FontLab 4/5 中的 OpenType 特性編輯視窗（Figure 14-1）
![FontLab 4/5 中的 OpenType 特性編輯視窗（Figure 14-1）](/images/fonts-encodings/fig14-1.png)
*FontLab 4/5 中的 OpenType 特性編輯視窗（Figure 14-1）*
:::

*圖 14-1：FontLab 中的 OpenType 核心工作視窗。左側為當前字型檔宣告的排版特性列表（Feature Tags），右上為選定特性（如 `liga`）的 AFDKO 原始碼編輯區，右下為編譯日誌與錯誤輸出控制檯。*

::: tip FontLab 視窗中詳細的特性與類管理介面（Figure 14-2, 14-3, 14-4）
![FontLab 視窗 OpenType 詳細特性視窗（Figure 14-2）](/images/fonts-encodings/fig14-2.png)
*FontLab 視窗 OpenType 詳細特性視窗（Figure 14-2）*
:::

*圖 14-2：FontLab 中的 OpenType 特性管理視窗。展示了特性的啟用依賴關係、指令碼隔離與獨立的查詢錶鏈。*

::: tip FontLab 視窗 Kerning 類矩陣選項卡（Figure 14-3）
![FontLab 視窗 Kerning 類矩陣選項卡（Figure 14-3）](/images/fonts-encodings/fig14-3.png)
*FontLab 視窗 Kerning 類矩陣選項卡（Figure 14-3）*
:::

*圖 14-3：FontLab 的 OpenType 視窗中的 Kerning 標籤頁。展示了基於類的字距微調對與類矩陣分配。*

::: tip FontLab 視窗 Classes 字元類定義標籤頁（Figure 14-4）
![FontLab 視窗 Classes 字元類定義標籤頁（Figure 14-4）](/images/fonts-encodings/fig14-4.png)
*FontLab 視窗 Classes 字元類定義標籤頁（Figure 14-4）*
:::

*圖 14-4：FontLab 視窗中的 Classes 標籤頁。展示了字型設計師如何將數十個重音變體歸入同一形態類，並在右側文字框中直觀預覽所屬字形。*

::: tip FontLab 實時互動排版預覽視窗（Figure 14-5）
![FontLab 實時互動排版預覽視窗（Figure 14-5）](/images/fonts-encodings/fig14-5.png)
*FontLab 實時互動排版預覽視窗（Figure 14-5）*
:::

*圖 14-5：FontLab 的 Preview Panel（實時預覽面板）。設計師可在面板中直接實時輸入任意長文字字串，並自由勾選開啟或關閉特定的 OpenType 特性（如 liga、onum、kern），即時檢驗特性編譯後的動態渲染效果。*

#### FontLab 視覺錨點（Anchors）管理法
在 FontLab 單字編輯視窗中，使用者可透過右鍵選單選擇 `Add Anchor` 建立一個帶紅色十字游標的錨點：
* 在字母基字（如 `o`）上方放置一個名為 `top` 的錨點；
* 開啟波浪變音符（`tilde`）視窗，在其底部關鍵位置放置一個名為 `_top` 的錨點（**關鍵規範：必須以下劃線 `_` 開頭且後接基字完全相同的錨點名**）；
* 當設計師開啟 `Window > Panels > Preview` 視窗並切換至 `Anchors` 選項卡時，FontLab 會自動計算這兩個座標之間的向量相對位移，實時展現變音符在基字上的完美吸附效果！

---


### 2.3 工業級 AFDKO 特性檔案的高階架構設計模式

在開發涵蓋數萬字形的大型泛東亞（CJK）字型檔或巨型西文排版大系時，單體 `.fea` 特性檔案往往會膨脹到數萬行。現代工業字型工程普遍採用模組化架構模式：

#### 1. 宏替換與檔案包含（Include Directives）
AFDKO 支援類似於 C 語言前處理器的 `include()` 指令：
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

#### 2. 條件編譯與指令碼分流（Script Sub-routing）
在大型字型檔中，同一特性在不同語言體系下需要表現出差異化的排版行為。例如在土耳其語、亞塞拜然語與克里米亞韃靼語中，拉丁字母 `'i'` 擁有大寫的帶點 `'İ'`（U+0130）與小寫的無點 `'ı'`（U+0131），與常規英語中大寫 `'I'` 變為小寫 `'i'` 的規則徹底衝突！
在 AFDKO 中，排版師必須利用 `script` 與 `language` 分支實現精密的語系隔離：

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

#### 3. 連字截斷陷阱與拓撲偏序原則（Topological Subsumption）
在編寫 `GSUB Type 4`（合字替換）時，若規則書寫順序不當，排版引擎會按照“先入為主”的原則提前消耗字首字元，導致更長的合字永遠無法被觸發！
* **致命錯誤順序**：
  ```fea
  sub f i by f_i;
  sub f f i by f_f_i; # 永远死锁！引擎在读到 'f' + 'f' + 'i' 时，在遇到 'f' + 'i' 时已将后两字吃掉合成为 f_i，从而产生 'f' + 'f_i'，三重连字被永久截断！
  ```
* **工業級標準偏序**：
  ```fea
  # 必须严格遵循“自长至短（Longest Match First）”的偏序排列：
  sub f f l by f_f_l;
  sub f f i by f_f_i;
  sub f f by f_f;
  sub f l by f_l;
  sub f i by f_i;
  ```


## 3. 在微軟 VOLT 中視覺化構建 OpenType 排版表（Managing OpenType Tables in VOLT）

與 Adobe 基於純文字程式碼編譯的 AFDKO 路線不同，微軟推出了重量級的純圖形化開發環境——**VOLT（Visual OpenType Layout Tool）**。VOLT 曾承擔了包括 Windows 系統中全部阿拉伯文、希伯來文、泰文以及印度數十種複雜地方官方文字字型檔的排版工程研發。

### 3.1 VOLT 的架構哲學與私有資料表

VOLT 並不直接解析或生成 AFDKO 程式碼，而是在 TrueType 字型二進位制內部開闢了一組私有資料表：
* `TSVT`：VOLT 專案主拓撲與工程設定表；
* `TSVC`：字元類定義表；
* `TSVG`：字形命名、Unicode 對映與後設資料；
* `TSVP`：定位與查詢表引數。

當排版師在 VOLT 中完成全部視覺化規則編排並點選“Compile”後，VOLT 內部的編譯器會將這套私有拓撲一鍵編譯為標準的工業級二進位制 `GSUB`、`GPOS` 和 `GDEF` 表。而在字型檔釋出階段，設計師可以選擇執行“Ship Font”，徹底剝離這組體積龐大的私有表，僅保留純淨的標準 OpenType 佈局表。

::: tip 微軟 VOLT 工程主專案控制視窗（Figure 14-6）
![微軟 VOLT 工程主專案控制視窗（Figure 14-6）](/images/fonts-encodings/fig14-6.png)
*微軟 VOLT 工程主專案控制視窗（Figure 14-6）*
:::

*圖 14-6：微軟 VOLT 主專案視窗。從上至下清晰展現了字元字形對映（Glyphs）、字元類矩陣（Classes）、排版特性（Features）與底層查詢表（Lookups）的層級依賴拓撲。*

#### VOLT 標準操作流
1. **開啟字型與資料重置**：點選 `Open` 載入字型。**重要警告**：此操作會完全抹除字型內所有由其他工具生成的非 VOLT OpenType 表！
2. **匯入 PostScript 字形名稱**：TrueType 原生字形僅有 GID 數字編號，點選 `Import > Import PostScript Names` 自動從 `post` 表匯入具名符號；
3. **分配 GDEF 字形型別**：進入 `Tools > Edit Glyphs`，為每個字形賦予 Single glyph、Ligature、Mark 或 Component 型別，並註明合字包含的部件數量；
4. **新增指令碼、語言與特性**：點選 `Add Script` 輸入 `<latn>` 等四字標籤，接著點選 `Add Language` 選擇 `<dflt>`，最後點選 `Add Feature` 輸入 `<liga>` 建立排版特性插槽。

### 3.2 查詢表與規則編輯

#### 1. 替換規則的視覺化與箭頭語法

雙擊任一替換查詢表，即可進入直觀的字形替換網格視窗：

::: tip VOLT 中字形替換查詢表的視覺化配置視窗（Figure 14-7）
![VOLT 中字形替換查詢表的視覺化配置視窗（Figure 14-7）](/images/fonts-encodings/fig14-7.png)
*VOLT 中字形替換查詢表的視覺化配置視窗（Figure 14-7）*
:::

*圖 14-7：VOLT 中查詢表（Lookup）編輯視窗。展示了視覺化的替換規則對映網格，支援透過直觀的箭頭拖拽定義輸入字元序列到目標字形的變換對映。*

排版師可以直接在網格左側輸入基準字形名或字形類，右側輸入目標替換字形名，甚至透過 `[ zero - nine ] | [ zero - nine ]` 的上下文分割豎線語法建立高階替換，VOLT 會在後臺自動完成覆蓋表格式的離散劃分與索引二分查詢樹最佳化。

#### 2. 定位規則與互動式錨點吸附（Visual Anchor Attachment）

在定位規則編輯視窗中，VOLT 提供了強大的雙重視窗聯動：

::: tip VOLT 中的草書錨點與二維空間定位視窗（Figure 14-8）
![VOLT 中的草書錨點與二維空間定位視窗（Figure 14-8）](/images/fonts-encodings/fig14-8.png)
*VOLT 中的草書錨點與二維空間定位視窗（Figure 14-8）*
:::

*圖 14-8：VOLT 的定位（Positioning）編輯視窗。展示了在阿拉伯文字形上互動式放置進入錨點（Entry）與退出錨點（Exit），實時觀察兩字沿斜角咬合的力學狀態。*

視窗左側定義參與定位的字形對或字形類，右側則以圖形畫布展現兩個字元在當前錨點下的拼接狀態。設計師可直接用滑鼠拖動錨點十字星，畫布上的兩個字元會實時響應吸附位移，極大地降低了複雜草書連綴的數學心智負擔。

### 3.3 VOLT 校對工具（Proofing Tool）與實戰

在複雜書寫系統排版中，一個輸入字串可能會連續激發數十個級聯查詢表。一旦某個查詢表發生邏輯死鎖或意外截斷，在成品文字中極難排查根因。VOLT 配備了享譽業界的互動式校對檢驗工具（Proofing Tool）：

::: tip VOLT 複雜指令碼互動式校對與排印預覽視窗（Figure 14-9）
![VOLT 複雜指令碼互動式校對與排印預覽視窗（Figure 14-9）](/images/fonts-encodings/fig14-9.png)
*VOLT 複雜指令碼互動式校對與排印預覽視窗（Figure 14-9）*
:::

*圖 14-9：VOLT 互動式校對檢驗視窗（Proofing Window）。在複雜的阿拉伯文與烏爾都語長句排版中，實時展示當前應用的查詢表執行軌跡鏈條。*

在校對視窗中輸入長文字字串後，VOLT 會在下方逐條列印執行報告（Execution Trace）：哪一個查詢表在第幾個字元上命中、輸入字形被轉化為什麼中間 GID、哪些標記符號被忽略、游標座標被累加了多少偏移量。排版師可以像使用偵錯程式單步跟蹤程式碼一樣，一幀一幀地檢查整個排版管線的狀態躍遷。

### 3.4 工業級挑戰：烏爾都語波斯折體（Nastaliq）在 VOLT 中的排版工程全景

波斯折體（Nastaliq）被公認為全人類排印技術皇冠上的明珠。它擁有極其嚴苛、甚至是違反直覺的排印物理學定律：
1. **級聯階梯傾斜跌落（Cascading Stems）**：在一個詞內部，每一個字母不是水平排在後方，而是跌落在前一個字母的左下後方，整詞呈現為從右上向左下以約 $45^\circ$ 傾斜的懸垂階梯；
2. **點標自適應避讓（Dynamic Dot Placement）**：阿拉伯子音字母帶有單個、成對或三個發音點標（Nuqta）。由於字形隨上下文不斷升降，點標必須根據鄰近筆畫的空間拓撲，動態在空間中上下平移移動，絕對不可與鄰近字母發生筆畫穿模碰撞；
3. **筆畫死結反向巢狀**：後方的字母尾部可能會向左下深遠回勾，穿插進前一個字母內部的負空間中。

在微軟著名的《Urdu Typesetting》專案中，VOLT 展現了不可替代的統治力：
* **第一步：上下文形態拆解與合字替換**：透過大量的 GSUB Type 4（Ligature）與 Type 6（Chained Contextual），將上千種高頻兩字、三字子音組合預先熔鑄為獨立的傾斜整體；
* **第二步：草書錨點精確咬合**：使用 GPOS Type 3（Cursive Attachment），在每一個字形的入刀點（Entry）與出刀點（Exit）放置精確錨點。排版引擎在從右向左排版時，自動將後字的 Entry 錨點與前字的 Exit 錨點在空間中對齊，從而自然形成了全單詞平滑連貫的 $45^\circ$ 階梯跌落！
* **第三步：反向鏈式上下文（GSUB Type 8）動態修剪**：當詞尾字母具有長長的水平回勾大弧線時，透過 Type 8 反向掃描前方詞幹的高度層級，動態將詞尾替換為不同長度與深度的回彎變體；
* **第四步：多層點標避讓附著（GPOS Type 4 與 Type 6）**：為每個子音字形配置上中下多個等級的候選錨點，並透過上下文定位規則檢測下沉深度，自動將發音點標推向不受阻擋的安全視覺區域。

---


### 3.5 VOLT 查詢表拓撲與依賴圖（Lookup Dependency DAG）

在微軟 VOLT 中組織上百個查詢表時，排版師必須將其構建為一個嚴格的有向無環圖（Directed Acyclic Graph, DAG）。每個查詢表絕非孤立存在，而是遵循嚴密的依賴注入機制：
1. **預處理查詢表（Preprocessing Lookups）**：負責將 Unicode 原始碼點清洗為字型檔規範基字（Canonical Forms）。例如消除多重零寬空格（ZWNJ/ZWJ）帶來的碼點漂移；
2. **形態重構查詢表（Morphological Analysis）**：依次執行詞首（`init`）、詞中（`medi`）、詞尾（`fina`）孤立（`isol`）四態判定；
3. **連字坍縮查詢表（Ligature Formation）**：自長至短逐級合併；
4. **後處理修剪查詢表（Post-processing Trimming）**：針對特定字尾進行反向伸展修剪；
5. **空間幾何吸附（Spatial Anchoring）**：在所有字形形態徹底定型之後，啟動 GPOS 查詢錶鏈，依次執行基線平移、字偶間隙、草書咬合與標音吸附。

在處理包含多套變音符號的古代文獻字型時，VOLT 的錨點系統支援多達 16 層的遞迴附著。排版師透過在基字上配置 `TopAnchor`、`BottomAnchor`、`RightAnchor`、`LeftAnchor`，並在變音符上配置配對的 `_TopAnchor`、`_BottomAnchor` 等，實現了全自動的二維網格化字母裝配流水線。


## 4. 在 FontForge 中管理 OpenType 表（Managing OpenType Tables in FontForge）

作為自由開源陣營的代表，FontForge（George Williams 主導開發）提供了一套極其貼近底層 TrueType/OpenType 二進位制資料結構的排版表管理環境。

### 4.1 核心控制檯：Element > Font Info > Lookups

在 FontForge 中開啟 `Element > Font Info`，並導航至 `Lookups` 選項卡。這是 FontForge 管理高階排版功能的中樞神經系統。該介面清晰地將整個字型內部的排版規則劃分為兩大並行視窗：
* `GSUB` 樹狀節點：展示所有字形替換查詢表；
* `GPOS` 樹狀節點：展示所有字形定位查詢表。

使用者點選 `Add Lookup` 按鈕時，FontForge 會彈出一個嚴謹的型別配置對話方塊，列出標準 OpenType 規範支援的全部查詢表型別（Single, Multiple, Alternate, Ligature, Contextual, Chained Contextual, Pairwise, Cursive, Mark-to-Base, Mark-to-Ligature, Mark-to-Mark）。每一個查詢表下方，可以進一步掛載一個或多個子表（Subtables）。

### 4.2 錨點體系與類定義（Anchor Classes）

::: tip FontForge 中的錨點與錨點類編輯視窗（Figure 14-10）
![FontForge 中的錨點與錨點類編輯視窗（Figure 14-10）](/images/fonts-encodings/fig14-10.png)
*FontForge 中的錨點與錨點類編輯視窗（Figure 14-10）*
:::

*圖 14-10：FontForge 中錨點系統的定義。左側為單字編輯視窗中直觀放置的具名錨點（Named Anchors）；右側為錨點類定義視窗，清晰展示了基字錨點與標記符號錨點的配對關係。*

FontForge 將錨點嚴格組織為**錨點類（Anchor Classes）**：
1. 在 `Font Info > Contextual` 中建立一個錨點類，例如命名為 `TopAccent`；
2. 為該類指定查詢表型別為 `Mark to Base`；
3. 開啟基字（如字元 `a`），選擇 `Point > Add Anchor`，型別選擇 `Base`，歸入 `TopAccent` 類，拖動到字元頂部中心；
4. 開啟重音變體字形（如 `grave`），新建錨點選擇 `Mark`，同樣歸入 `TopAccent` 類，拖動到重音符號基底部；
5. FontForge 會在後臺自動完成兩者在 `GPOS` Format 1 表中的座標偏移矩陣換算。

### 4.3 非上下文替換與定位

在單字編輯視窗中，設計師可以透過標籤頁直觀配置簡單的非上下文規則：

::: tip FontForge 非上下文替換與定位編輯（Figure 14-11, 14-12）
![FontForge 非上下文替換視窗（Figure 14-11）](/images/fonts-encodings/fig14-11.png)
*FontForge 非上下文替換視窗（Figure 14-11）*
:::

*圖 14-11：FontForge 的非上下文替換視窗。左側展示了單字替換（Single Substitution）標籤頁，右側為新建替換規則的引數對話方塊。*

::: tip FontForge 單字與字偶對定位視窗（Figure 14-12）
![FontForge 單字與字偶對定位視窗（Figure 14-12）](/images/fonts-encodings/fig14-12.png)
*FontForge 單字與字偶對定位視窗（Figure 14-12）*
:::

*圖 14-12：FontForge 的簡單單字定位（左）與成對字距定位（右）視窗。*

在字距調整（Kerning）視窗中，FontForge 支援成組匯入字形類矩陣。設計師可以將包含相同左側或右側輪廓特徵的字母歸類，大大削減需要人工填寫的數值單元格總數。

### 4.4 鏈式上下文排版嚮導（Chained Contextual Lookups）

在 OpenType 各種查詢表中，鏈式上下文替換與定位由於涉及回溯（Backtrack）、匹配（Match）與前瞻（Lookahead）三大字元區間的邏輯巢狀，手動編寫容易產生死迴圈。FontForge 專門設計了一個四步向導流程：

::: tip FontForge 中定義鏈式上下文替換的前四步流程（Figure 14-13）
![FontForge 中定義鏈式上下文替換的前四步流程（Figure 14-13）](/images/fonts-encodings/fig14-13.png)
*FontForge 中定義鏈式上下文替換的前四步流程（Figure 14-13）*
:::

*圖 14-13：在 FontForge 中定義鏈式上下文替換（Chained Contextual Substitution）的四步引導流程：(a) 選擇特性標籤；(b) 設定覆蓋表型別；(c) 定義回溯、匹配輸入與前瞻字元序列覆蓋集；(d) 繫結對應的子查詢表索引。*

嚮導執行邏輯：
1. **步驟 (a)**：選定觸發該規則的目標特性標籤（如 `calt` 或 `liga`）以及適用的語言系統；
2. **步驟 (b)**：選擇覆蓋表格式（Coverage Format 1 針對離散字形列舉，Format 2 針對連續區間）；
3. **步驟 (c)**：定義三大字元區間的字形或字形類序列。排版師在 Backtrack 列表中輸入前置字元類，在 Match 列表中輸入當前需要被替換的字元，在 Lookahead 列表中輸入後續觸發條件；
4. **步驟 (d)**：為 Match 序列中的每一個指定槽位，繫結預先建立好的簡單替換（Single Substitution）或定位子查詢表。引擎執行時在匹配到整體上下文後，即對目標槽位實施呼叫的子動作。

---


### 4.5 實戰案例：使用鏈式上下文覆蓋表構建英文序數詞（Ordinals）自動化排版

在英文正文排版中，序數詞格式有著極其嚴苛的規則：
* 詞尾為 1 的數字（除 11 外）後接 `st`（如 1st, 21st, 101st）；
* 詞尾為 2 的數字（除 12 外）後接 `nd`（如 2nd, 22nd, 102nd）；
* 詞尾為 3 的數字（除 13 外）後接 `rd`（如 3rd, 23rd, 103rd）；
* 其餘所有數字（包括 11, 12, 13）均後接 `th`（如 4th, 11th, 12th, 13th, 20th）。
優秀的字型應當在使用者輸入普通文字時，自動將 `st`, `nd`, `rd`, `th` 提升為優美的上標字形（Superscript），同時保持數字本身為常規字形。

在 FontForge 中，我們透過以下四步向導精確實現：
1. **第一步：建立底層非上下文單字替換子表**：
   在 `sups` 特性下，新建一個單字替換查詢表，將常規字母對映為其上標變體：
   `s -> s.superior`, `t -> t.superior`, `n -> n.superior`, `d -> d.superior`, `r -> r.superior`, `h -> h.superior`。
2. **第二步：劃分覆蓋表集合（Coverage Tables）**：
   為避免規則碰撞，我們將字元劃分為獨立的覆蓋集合：
   * `Cov_Digit1`：`[one]`；
   * `Cov_Digit2`：`[two]`；
   * `Cov_Digit3`：`[three]`；
   * `Cov_DigitsOther`：`[zero four five six seven eight nine]`；
   * `Cov_Teen1`：`[one]`（用於匹配十位上的 1）；
   * `Cov_st`：`[s]`, `[t]`；
   * `Cov_nd`：`[n]`, `[d]`；
   * `Cov_rd`：`[r]`, `[d]`；
   * `Cov_th`：`[t]`, `[h]`。
3. **第三步：配置鏈式上下文匹配規則（Chained Contextual Rules）**：
   在嚮導的 (c) 與 (d) 視窗中，我們定義多條互斥的匹配鏈條：
   * *規則 1（處理 11th, 12th, 13th 特例）*：
     * **Backtrack 序列**：`Cov_Teen1`；
     * **Match 序列**：`[one two three]`（索引 0） + `[t]`（索引 1） + `[h]`（索引 2）；
     * **呼叫的子查詢表**：僅在索引 1 與索引 2 上呼叫 `sups` 單字替換！索引 0（數字）不被修改；
   * *規則 2（常規 1st）*：
     * **Backtrack 序列**：無或 `[zero two-nine]`；
     * **Match 序列**：`Cov_Digit1`（索引 0） + `[s]`（索引 1） + `[t]`（索引 2）；
     * **呼叫的子查詢表**：在索引 1 和 2 上呼叫 `sups`；
   * *規則 3（常規 2nd）*：
     * **Match 序列**：`Cov_Digit2` + `[n]` + `[d]` 並在 `nd` 上呼叫 `sups`；
   * *規則 4（常規 3rd）*：
     * **Match 序列**：`Cov_Digit3` + `[r]` + `[d]` 並在 `rd` 上呼叫 `sups`；
   * *規則 5（兜底 4th..0th）*：
     * **Match 序列**：`Cov_DigitsOther` + `[t]` + `[h]` 並在 `th` 上呼叫 `sups`。

透過這種“覆蓋集巢狀 + 槽位繫結”的精妙結構，FontForge 編譯生成的 `GSUB Format 6` 表具有最高等級的執行效率與魯棒性。


## 5. 在 FontForge 中構建蘋果高階排版（AAT）有限狀態機（Managing AAT Tables in FontForge）

在數字排版技術的另一座技術巔峰上，佇立著蘋果公司的 **Apple Advanced Typography（AAT）**。AAT 源於 1990 年代初蘋果研發的 TrueType GX 架構，在蘋果作業系統生態中（macOS、iOS）擁有最頂級的底層原生支援。

### 5.1 AAT 與 OpenType 的計算理論對決

OpenType 與 AAT 代表了電腦科學中兩種完全不同的計算哲學路線：
* **OpenType 的“宣告式模式匹配”路線**：將字型排版視為一系列宣告式的圖重寫規則集合（Graph Rewriting Rules）。排版引擎在執行時載入字串，像一個多遍歷掃描器一樣，一遍遍掃描整段文字，按順序匹配查詢表。其優點是規則邏輯直觀、易於移植；但缺點是在處理複雜上下文時，引擎必須往復掃描字串，且容易發生規則順序依賴與歧義碰撞。
* **AAT 的“確定性有限狀態自動機（DFA / FST）”路線**：AAT 認為，**文字流在排版引擎中的流動本質上是一個時間序列訊號**！任何上下文條件替換、字距微調與連字融鑄，都可以嚴格抽象為一個**有限狀態轉換器（Finite State Transducer, FST）**。字型檔內部儲存的不是分散的規則碎片，而是一張結構嚴密的二維狀態轉移矩陣。

### 5.2 特性與選擇器命名體系（Features and Selectors）

與 OpenType 使用晦澀的 4 字元 ASCII 縮寫標籤（如 `smcp`, `onum`）不同，AAT 採用兩級整數分層架構：**特性型別（Feature Type）** 與 **特性選擇器（Feature Selector）**。
更具顛覆性的是：**AAT 將排版特性的多語言本地化顯示名稱直接儲存在字型檔內部的 `feat` 表中**！任何排版軟體無需更新應用程式程式碼，只需讀取字型檔自身的 `feat` 表，即可自動在介面下拉選單中向使用者渲染出由字型設計師親自編寫的母語選項（如“連字開啟”、“斜線分數”、“老式數字”）。

::: tip AAT 特性與選擇器多語言名稱編輯（Figure 14-14）
![AAT 特性與選擇器多語言名稱編輯（Figure 14-14）](/images/fonts-encodings/fig14-14.png)
*AAT 特性與選擇器多語言名稱編輯（Figure 14-14）*
:::

*圖 14-14：FontForge 中編輯 AAT 特性與選擇器名稱介面。展示了在 `feat` 表中為特定排版特性（如連字特性、數字樣式）配置法語、英語等多語言本地化顯示標籤。*

### 5.3 AAT 狀態機四大核心操作（Font Info > Mac SM）

::: tip AAT 狀態機類表與狀態轉移矩陣視窗（Figure 14-15）
![AAT 狀態機類表與狀態轉移矩陣視窗（Figure 14-15）](/images/fonts-encodings/fig14-15.png)
*AAT 狀態機類表與狀態轉移矩陣視窗（Figure 14-15）*
:::

*圖 14-15：FontForge 中 AAT 狀態機類表與狀態轉移矩陣輸入視窗。(a) 輸入類表分配；(b) 狀態轉移矩陣視窗，表格每一行代表一個機器狀態，每一列代表輸入類別，單元格內標明目標狀態與觸發動作。*

在 FontForge 中開啟 `Font Info > Mac SM`，可以構建 AAT 的四大狀態自動機：

#### 1. 字形重排狀態機（Glyph Rearrangement）
專用於印度系與東南亞文字中子音與母音的物理時空重排。例如在孟加拉文或高棉文中，輸入序列為子音 $C$ 接母音 $V$，但在視覺呈現上母音符號必須出現在子音左側。狀態機在掃描到子音時將其壓入內部暫存槽，在掃描到母音時觸發重排動作，直接在底層輸出流中對調兩者的繪製次序。

#### 2. 上下文替換狀態機（Contextual Substitution）
以對角線專業分數（Fractions，如 `1/2`）的排版為例，AAT 的狀態機設計堪稱工程典範：
1. **輸入類別劃分**：
   * 類別 0：End of text（文字終結符）；
   * 類別 1：Out of bounds（越界符）；
   * 類別 2：Non-digits（非數字字元）；
   * 類別 3：Slash（斜槓字元 `/`）；
   * 類別 4：Digits（數字字元 `0-9`）。
2. **狀態機狀態轉移規劃**：
   * **狀態 0（Start of text）**：若讀取到類別 4（數字），勾選 `Mark Current Glyph`（標記當前字形），躍遷至**狀態 2（Seen Numerator）**；若讀取到其他字元，保持狀態 0；
   * **狀態 2（Seen Numerator）**：若繼續讀取到數字，保持狀態 2；若讀取到類別 3（斜槓），躍遷至**狀態 3（Seen Slash）**；若讀取到非數字，重置回狀態 0；
   * **狀態 3（Seen Slash）**：若讀取到類別 4（數字），立刻觸發雙重動作：將此前被標記的字元替換為**分子字形（Numerator Glyph）**，將當前的斜槓替換為**對角分數線（Fraction Slash）**，並將當前數字替換為**分母字形（Denominator Glyph）**！狀態躍遷至**狀態 4（Seen Denominator）**；
   * **狀態 4（Seen Denominator）**：若後續繼續出現數字，直接替換為分母字形；一旦遇到非數字，重置回到狀態 0。

#### 3. 字形動態插入狀態機（Glyph Insertion）
AAT 獨樹一幟的殺手級功能。在 OpenType 中，替換隻能是一對一或多對一，無法憑空向文字流中注入全新字形。而在 AAT 中，狀態機允許在當前字形與標記字形之間**動態插入全新字形**！
* *阿拉伯文兩端對齊伸展線（Kashida Insertion）*：排版引擎在掃描到阿拉伯字母單詞內部合法的伸展斷點時，狀態機自動插入一個或多個連線拉伸字形（Kashida），而無需更改原始文字的邏輯字元序列；
* *高棉文/柬埔寨文筆畫分裂*：當掃描到複雜的環繞母音時，自動在子音前後插入對應的括號式分離部件。

#### 4. 上下文擴充套件字距狀態機（Contextual Kerning / `kerx`）
蘋果在 AAT `kerx` 表中實現了一次性對多達 **8 個字元** 同時施加跨字元字距調整的驚人能力！
例如處理帶標點的西文縮寫，如 `"S.A.V."` 或 `"A.V"`：
傳統 OpenType 的 `kern` 表只能處理兩兩相鄰的字元對（Pair Kerning），面對 `'A'` 與 `'V'` 之間被一個實心句號 `'.'` 隔開的場景束手無策，導致 `'A'` 與 `'.'`、`'.'` 與 `'V'` 的間距無法聯動微調。
而在 AAT 狀態機中：
1. 狀態機配備了一個深度為 8 的硬體回溯棧（Push Current Glyph）；
2. 當掃描到 `'A'` 時，執行 `Push`；掃描到 `'.'` 時，繼續 `Push`；當掃描到 `'V'` 時，觸發彈出（Pop）；
3. 狀態機在彈出 $n$ 個壓棧字元的同時，**一步同時向這組序列施加 $n-1$ 個相互關聯的字距調整偏移矩陣**！從而在字母跨越標點符號時，依然能夠實現完美平滑的視覺負空間咬合。

---


### 5.6 AAT 狀態機完整二維轉移矩陣與對角分數演算法執行跟蹤

為了徹底闡明 AAT 有限狀態自動機的工程實現，表 14-2 給出了構建專業斜線分數（Diagonal Fractions）時，AAT `morx` 表內部由編譯器生成的完整狀態轉移矩陣：

| 狀態（State） | 類別 0（End of Text） | 類別 1（Out of Bounds） | 類別 2（Non-digits） | 類別 3（Slash `/`） | 類別 4（Digits `0-9`） |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **State 0（文字起始 / 待機）** | State 0 (無動作) | State 0 (無動作) | State 0 (無動作) | State 0 (無動作) | **State 2** (標記當前字形為分子起點 `MarkFirst`, 推進) |
| **State 1（行起始）** | State 0 (無動作) | State 0 (無動作) | State 0 (無動作) | State 0 (無動作) | **State 2** (標記當前字形為分子起點 `MarkFirst`, 推進) |
| **State 2（已讀入分子數字）** | State 0 (無動作) | State 0 (無動作) | State 0 (無動作) | **State 3** (推進指標，等待分母) | **State 2** (繼續累計分子數字，推進) |
| **State 3（已讀入斜槓）** | State 0 (回滾無動作) | State 0 (回滾無動作) | State 0 (回滾無動作) | State 0 (回滾無動作) | **State 4** (觸發級聯三動作：替換標記為分子、替換斜槓為分數線、替換當前為分母，推進) |
| **State 4（已讀入分母數字）** | State 0 (重置) | State 0 (重置) | State 0 (重置) | State 0 (重置) | **State 4** (替換當前為分母，推進) |

#### 實戰執行軌跡跟蹤（Trace Analysis）
假設使用者在鍵盤上輸入字串：`"Weight 12/34 kg"`：
1. 字元 `'W'`, `'e'`, `'i'`, `'g'`, `'h'`, `'t'`, `' '` 屬於**類別 2（Non-digits）**。狀態機恆定保持在 **State 0**，不做任何字形改寫；
2. 掃描到字元 `'1'`（類別 4）：命中單元格 `(State 0, Class 4)`，機器將字元 `'1'` 的記憶體地址壓入 `MarkRegister`，狀態躍遷至 **State 2**；
3. 掃描到字元 `'2'`（類別 4）：命中單元格 `(State 2, Class 4)`，狀態保持在 **State 2**；
4. 掃描到字元 `'/'`（類別 3）：命中單元格 `(State 2, Class 3)`，狀態躍遷至 **State 3**（此時斜槓暫不替換，防止後續不是數字時誤傷常規除號！）；
5. 掃描到字元 `'3'`（類別 4）：命中單元格 `(State 3, Class 4)`，瞬間激發三重複合替換動作：
   * 將 `MarkRegister` 中的 `'1'` 與 `'2'` 替換為分子字形 `1.numerator`, `2.numerator`；
   * 將前一個字元 `'/'` 替換為專業對角分數線 `fraction`（U+2044）；
   * 將當前字元 `'3'` 替換為分母字形 `3.denominator`；
   * 狀態躍遷至 **State 4**；
6. 掃描到字元 `'4'`（類別 4）：命中單元格 `(State 4, Class 4)`，將 `'4'` 替換為分母字形 `4.denominator`，狀態保持在 **State 4**；
7. 掃描到字元 `' '`（類別 2）：命中單元格 `(State 4, Class 2)`，狀態機平穩重置回 **State 0**。

整個識別與全套三段式字形替換過程，在排版引擎單向遍歷文字流的過程中**一氣呵成、零回溯、零重掃**，其數學邏輯的自洽與優雅堪稱軟體工程的奇蹟！


### 5.4 AAT 有限狀態自動機的數學本質與演算法複雜度

從形式語言與自動機理論（Formal Language & Automata Theory）的角度審視，AAT 的狀態機是一個嚴格定義的六元組（6-tuple）：

$$M = \langle Q, \, \Sigma, \, \Gamma, \, \delta, \, q_0, \, F \rangle$$

* $Q$：有限狀態集合 $\{s_0, s_1, \dots, s_{k-1}\}$。其中 $s_0$ 恆定為起始狀態（Start of text），$s_1$ 為行起始狀態（Start of line）；
* $\Sigma$：有限輸入字元表，即由類定義表（Class Table）投影得出的字形類別集合 $\{0, 1, \dots, C-1\}$；
* $\Gamma$：有限輸出操作集合（替換字形、設定標記、壓棧、出棧、位移）；
* $\delta: Q \times \Sigma \to Q \times \Gamma$：**狀態轉移與動作執行函式**，在物理上被編碼為一個大小為 $|Q| \times |\Sigma|$ 的緊湊二維矩陣；
* $q_0 \in Q$：初始狀態；
* $F \subseteq Q$：接受狀態集合。

#### 為什麼 AAT 在理論上具有絕對的效能優勢？
在 OpenType 引擎中，每個查詢表（Lookup）是一個獨立的匹配器。排版引擎必須在整段文字中逐字掃描；若有 30 個查詢表，引擎必須對文字進行多達 30 輪的往復遍歷掃描，演算法複雜度為 $O(K \cdot N)$（$K$ 為查詢表數量，$N$ 為文字長度）。

而在 AAT 引擎中，無論字型檔中包含多麼複雜的上下文替換規則，編譯器在離線構建字型檔時，已經透過自動機狀態合併演算法（Automata Minimization），將所有的併發規則**全部預編譯為了單一的一張確定性狀態轉移表**！
在執行時，CoreText 排版引擎僅需一個簡單的指標遍歷字串：
1. 讀取當前字形 GID，查類表得到輸入類別 $c \in \Sigma$；
2. 依據當前狀態 $s \in Q$ 與類別 $c$，在二維陣列中一步查得目標新狀態 $s' = \delta(s, c)$ 以及伴隨動作；
3. 執行動作（如設定標記、替換字元），將狀態更新為 $s'$，指標前移一個字形。

**整段文字僅需從頭到尾被掃描且僅被掃描整整一次（Single-pass Scanning），時間複雜度嚴格鎖定為物理極限的 $O(N)$！**
在處理數萬字的長篇鉅著排版時，AAT 的渲染延遲與記憶體開銷遠遠低於多輪迴圈的 OpenType 引擎，展現了電腦科學理論應用於工程實踐的極致冷峻之美。

---


### 5.5 FontForge 中 AAT 狀態轉移表（State Transition Table）完整十六進位制結構

在底層的 TrueType 字型二進位制中，AAT 狀態機被編碼為 `morx`（擴充套件變態表）或 `kerx`（擴充套件字距表）中的狀態子表（State Subtable）。其核心資料結構如下：
* **`Header`**：記錄狀態機型別、類數（Class Count）、狀態數（State Count）、類表偏移量與狀態轉移陣列偏移量；
* **`Class Table`**：一個將字形 GID 對映到輸入類別（Class ID）的查詢表。通常採用 Format 0（簡單微調陣列）或 Format 2（二分查詢區間）；
* **`State Array`**：一個二維矩陣，行索引為狀態號（State ID），列索引為輸入類別（Class ID）。每個單元格包含一個 16 位整數偏移量，指向對應的狀態轉移條目（Entry）；
* **`Entry Table`**：狀態轉移條目結構體：
  ```c
  struct MorxTransitionEntry {
      uint16 newStateOffset;    /* 转移后的新状态在状态数组中的字节偏移 */
      uint16 flags;             /* 控制标志位（如是否标记当前字形、是否推进指针） */
      uint16 markIndex;         /* 若设置了替换动作，指向被标记字形的替换表索引 */
      uint16 currentIndex;      /* 指向当前字形的替换表索引 */
  };
  ```

每個控制標誌位（Flags）具有極其精細的微指令語義：
* **Bit 15 (`Mark`)**：將當前字形壓入內部標記暫存器；
* **Bit 14 (`DontAdvance`)**：**關鍵停頓微指令**！指示排版引擎在完成本次狀態轉移後，**不要將掃描指標向前移動到下一個字形**，而是保持在當前字形上，使用新的狀態再次評估當前字形！這使得狀態機能夠處理複雜的重疊匹配與貪婪掃描；
* **Bit 13 (`Reserved`)**：保留位，恆為 0；
* **Bits 12–0 (`Verb / Sub-action`)**：在重排狀態機中指定字形交換的步長與方向。

透過這一套極致純粹的硬體級微指令，AAT 狀態機僅憑一張靜態位元組表與一個極度輕量的直譯器迴圈，即可在幾十納秒之內完成人類最複雜文字的動態排版變形！


## 6. 結語與現代排版技術圖景（Conclusions and Modern Outlook）

經過三十餘年的激烈競爭與技術融合，數字字型的智慧化排版格局已經清晰明朗：
* **OpenType** 憑藉 Adobe 與微軟在跨平臺工業軟體（InDesign、Office、Web 瀏覽器）上的龐大生態號召力，成為了當今網際網路與桌面排版事實上的全球通用標準；
* **AAT** 憑藉其超前而優雅的有限狀態自動機理論，在蘋果 macOS 與 iOS 系統生態中守護著高品質排版的底線，並在波斯體與南亞文書處理中樹立了無與倫比的效能標杆；
* **開源引擎的集大成**：以 Behdad Esfahbod 等人開發的開源排版引擎 **HarfBuzz** 為里程碑，現代計算系統成功在單一執行時內完美相容了 OpenType 規則解析與類 AAT 的狀態流水線，成為了 Chrome、Firefox、Android、LibreOffice 以及各大 Linux 發行版背後的世界引擎底座；
* **走向多維：OpenType 1.8 可變字型（Variable Fonts）**：2016 年微軟、Adobe、蘋果與谷歌聯合釋出的 OpenType 1.8 規範，將高階排版功能推向了全新的空間維度。透過在 `GSUB`/`GPOS` 中掛載 `FeatureVariations` 表，字型設計師不僅能夠在字重、字寬、視覺尺寸軸線上平滑插值輪廓，更能在設計軸滑塊行進到特定閾值時，自動無縫觸發字形骨架與排版特性的動態突變。

從金屬活字的物理枷鎖，到 PostScript 的靜態貝塞爾曲線，再到 OpenType 與 AAT 將計算邏輯植入字型核心——人類文字的排印藝術在數字時代不僅沒有消亡，反而在現代自動機理論與微觀幾何計算的滋養下，綻放出了前所未有的智慧與璀璨光芒。
