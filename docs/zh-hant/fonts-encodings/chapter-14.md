---
title: "第 14 章：豐富字型：高階排版功能"
description: "深入剖析 OpenType 替換與定位（GSUB/GPOS）、AFDKO 特性檔案定義語言全語法規範、微軟 VOLT 工程實戰、FontForge 排版表與蘋果高階排版（AAT）有限狀態機（morx/kerx）。"
---

# 第 14 章：豐富字型：高階排版功能
### Chapter 14: Enriching Fonts: Advanced Typography
雅尼斯·哈拉蘭博斯（Yannis Haralambous, Ph.D.）著
選自《Fonts & Encodings》第 551–598 頁
*譯者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

## 1. 排版智慧化的演進與正規化轉移（Introduction）

在傳統數字字型技術（如原始的 PostScript Type 1 或未經擴充的經典 TrueType）中，字型檔案本質上僅僅是一個**靜態的字形輪廓容器**。作業系統在接收到一段文字字串（如 ASCII 或 Unicode 碼位序列）時，所能執行的僅僅是最原始的“查表—提取輪廓—繪製”單向對映。每個字元對應且僅對應一個固定字形，字元之間的排列完全由各自預設的水平前進寬度（Advance Width）累加決定，至多輔以一張簡單的平面字距對（Kerning Pair）調整表。

然而，人類悠久的活字排版傳統與全球紛繁複雜的書寫系統，對計算機排版引擎提出了截然不同的嚴苛要求：
- **經典西文排版美學**：為了避免字元碰撞並提升閱讀韻律，兩個或三個特定字母必須融合成精緻的連字（如 $\text{f}+\text{i} \to \text{fi}$、$\text{f}+\text{f}+\text{l} \to \text{ffl}$）；正文中的大寫字母如果與小寫字母混排，需要使用縮放至小寫字母高度的小型大寫字母（Small Capitals）；在普通段落中應使用錯落有致的舊體數字（Oldstyle Figures），而在財務表格中則必須使用等寬的齊線數字（Lining Figures）；分數的呈現需要將斜槓與數字自動轉換為對角分數（Diagonal Fractions）或堅式分數（Vertical Fractions）。
- **非拉丁複雜書寫系統**：在阿拉伯文、敘利亞文、蒙古文中，文字具有天然的草書連筆特性，同一個字母在單詞的詞首（Initial）、詞中（Medial）、詞尾（Final）以及孤立狀態（Isolated）下必須呈現完全不同的物理拓撲外形；在南亞與東南亞文字型系（如天城文 Devanagari、孟加拉文 Bengali、泰米爾文 Tamil、高棉文 Khmer）中，子音與子音相遇會結合成不可分割的半字連結符，而某些母音符號在邏輯編碼上雖然輸入在子音之後，在物理視覺呈現上卻必須被“重排”並繪製在子音簇的最左側。

如果將這些極其複雜的語言學邏輯、上下文敏感分析和微觀幾何形變硬寫進作業系統的核心或應用程式內部，不僅會導致字型的可移植性徹底喪失，更使得任何新創文字或特殊排版風格的擴充套件成為天方夜譚。

因此，20 世紀 90 年代中後期，數字字型工業迎來了一場**劃時代的正規化轉移**：**字型的知性化（Enriching Fonts）**。排版規則的解析與執行邏輯被徹底移入字型檔案本身。字型不再是一個被動的輪廓資料庫，而變成了一個**擁有自主決策能力、包含微型語法規則與有限狀態機的智慧執行實體**。當前處於統治地位的高階排版字型標準包括：
1. **OpenType（包含 TrueType 輪廓與 CFF/PostScript 輪廓）**：由微軟（Microsoft）與 Adobe 聯合制定，基於規則宣告與分級查表的架構；
2. **Apple Advanced Typography（AAT）**：由蘋果公司（Apple）基於 Mac OS 經典 QuickDraw GX 發展而來，基於純粹計算理論中的**確定性有限狀態自動機（Finite State Machine, FSM）**架構。

### 1.1 從字元到字形：文字整形（Text Shaping）的動態蛻變
在現代高階排版引擎（如開源跨平臺的 HarfBuzz、Windows 的 Uniscribe/DirectWrite、macOS 的 CoreText）的工作管線中，排版過程被稱為**文字整形（Text Shaping）**。輸入引擎的字元流（Unicode 序列）在最終變為顯示在螢幕上的畫素之前，會經歷一系列多維的動態蛻變：

$$\text{Unicode Code Points} \xrightarrow{\quad\text{cmap 對映}\quad} \text{Glyph IDs} \xrightarrow{\quad\text{GSUB 替換}\quad} \text{Glyph IDs} \xrightarrow{\quad\text{GPOS 定位}\quad} \text{Positioned Glyphs}$$

在這一過程中，字元與字形之間的一對一關係被徹底打破，呈現出豐富的對映形態：
- **一對多（One-to-Many）**：單個字元被拆分為多個字形片段（例如南亞文字中被前後分割的環繞型母音）；
- **多對一（Many-to-One）**：多個連續字元融合成單個連字字形；
- **多對多（Many-to-Many）**：一段字元序列被重構為另一組長度不同、外形迥異的字形序列；
- **動態微觀位移**：字形不再僅僅沿著基線機械排列，而是可以在二維平面內任意平移，甚至自動根據基字輪廓上的物理錨點實現畫素級的磁吸吸附。

### 1.2 高階排版雙翼：字形替換（GSUB）與幾何定位（GPOS）
在 OpenType 架構中，字型的高階排版能力被清晰地解耦為兩大核心表：**GSUB（Glyph Substitution Table，字形替換表）**與 **GPOS（Glyph Positioning Table，字形定位表）**。

#### 1. 字形替換的六大形態（GSUB）
字形替換負責在不改變字形座標系統的前提下，根據語法上下文將當前字形替換為更適宜的候選字形：
1. **單字替換（Single Substitution）**：將一個字形直接替換為另一個字形。最典型的應用是將普通小寫字母替換為小型大寫字母（`a` $\to$ `a.sc`），或者將普通標點替換為特定語言專用標點。
2. **多字替換（Multiple Substitution）**：將單個字形分解為多個連續字形。例如，在解構複合連字或將特定南亞文字連結符還原為獨立筆畫時使用。
3. **備選字形替換（Alternate Substitution）**：為一個字形提供多個美學對等的變體，供排版軟體向使用者展示選擇選單。例如赫爾曼·察夫（Hermann Zapf）設計的著名書法字型 **Zapfino** 中，小寫字母 `d` 擁有多達 9 種不同揮灑程度的花體變體，排版引擎可以透過備選替換讓使用者自由挑選。
4. **合字替換（Ligature Substitution）**：排版中最經典的替換形式。將兩個或多個連續字形融合成單個專屬連字字形（如 `f` + `i` $\to$ `fi`、`c` + `t` $\to$ `ct`）。
5. **上下文替換（Contextual Substitution）**：替換的觸發與否完全取決於該字形所處的前後環境（Context）。最經典的案例是阿拉伯文：一個孤立字母僅在後面緊隨另一個相連字母時，才轉變為詞首形（Initial Form）。在這個過程中，字形外形的改變屬於單字替換，而緊隨其後的字形則構成了“上下文”。
6. **鏈式上下文替換（Chained Contextual Substitution）**：上下文替換的高階演進形態。在前述阿拉伯文簡單上下文中，被充當“上下文”的後隨字形由於已被規則捕獲，無法立即參與下一輪替換（導致第二個字母無法順利變為詞中形）。鏈式上下文替換引入了**回溯序列（Backtrack）**、**輸入序列（Input）**與**前瞻序列（Lookahead）**的三元劃分，使得上下文環境與實際被替換的字形徹底分離，允許規則像多米諾骨牌一樣連續鏈式觸發。
7. **逆向鏈式上下文單替換（Reverse Chaining Contextual Single Substitution）**：專門針對諸如烏爾都語（Urdu）納斯塔利格體（Nastaliq）等極端書寫系統設計的特殊機制。烏爾都語採用從右向左的書寫方向，但在排版時，一個字母的垂直懸垂高度和連筆外形取決於其**後續**字母（即視覺左側的字母）。逆向鏈式替換以與文字書寫相反的物理方向（從左向右）逆流掃描字形流，確保每一處的字形變體都能提前預知未來的上下文形態。

#### 2. 字形微觀幾何定位的六大形態（GPOS）
字形定位負責在字形外形已確定的基礎上，微調字形在二維排版網格上的度量屬性：
1. **單字調整（Single Adjustment）**：對單個字形的水平位置、垂直位置、水平前進量或垂直前進量進行微調。例如，全大寫排版時，將括號、連字元等標點符號整體向上提升若干距離，使其與大寫字母光學中心對齊。
2. **字對調整（Pair Adjustment）**：即現代化的字距調整（Kerning）。當特定的兩個字形相遇時（如 `A` 與 `V`、`T` 與 `o`），動態縮短或拉開它們之間的物理間距。OpenType 的字對調整遠超傳統 1 對 1 字距對，它既支援基於字形類的笛卡爾積批次調整，更允許在 X 軸與 Y 軸兩個維度同時進行平移。
3. **草書連筆吸附（Cursive Attachment）**：在阿拉伯文、波斯文或西文花體手寫體中，字母之間透過平滑的起伏曲線無縫連線。草書定位允許為每個字形定義一個“入刀點”（Entry Anchor）和一個“出刀點”（Exit Anchor）。排版引擎在渲染時，自動平移後一個字形，使其入刀點與前一個字形的出刀點在二維空間完全重合。
4. **標音符號吸附基字（Mark-to-Base Attachment）**：現代字型實現 Unicode 任意重音組合的核心基石。傳統字型不得不為 `á`、`à`、`ä` 等每個帶重音字母預先繪製獨立字形，導致漢明空間無限膨脹。而在 Mark-to-Base 定位下，基字（如字母 `a`）定義一個或多個吸附錨點（如頂部錨點 `(250, 450)`），重音符號（如尖音符 `acute`）在其基底定義對應的反向錨點。排版引擎動態將兩個錨點嚴絲合縫地對齊，從而理論上可以用一套重音符號為世界上所有字母精準新增聲調。
5. **標音符號疊合（Mark-to-Mark Attachment）**：允許在已有標音符號之上繼續疊合第二個、第三個標音符號（如越南語中既有揚抑符又有聲調符號 `ế`，或國際音標中的複雜上下標）。
6. **合字部件標音吸附（Mark-to-Ligature Attachment）**：當一個連字由多個母音組成（如 `ae` 連字 `æ`），而排版需要單獨在 `e` 的上方新增重音符號時，Mark-to-Ligature 允許字型工程師在單個連字內部按照邏輯部件宣告多個獨立的區域性錨點集，使得聲調符號能夠準確落在目標字母的正上方，徹底免去了為每一種重音組合重複繪製專用合字的繁重勞動。
7. **上下文定位與鏈式上下文定位（Contextual / Chained Contextual Positioning）**：定位動作的發生受制於上下文。經典範例：在排版縮寫詞 `V.A.V.` 時，第二個字母 `V` 應當向第二個句點大幅收緊負字距，這是因為該句點前面是一個帶有大傾角留白的 `A`；然而，在排版 `V.V.` 時，相同的 `.` 與 `V` 組合就絕對不能收緊字距，否則兩個 `V` 的頂部會相互撞擊，視覺上嚴重粘連並形似 `W`。

#### 3. 標準排版特性標籤體系（Standard Feature Tags）
為了讓世界各地的文書處理軟體（InDesign、Word、Web 瀏覽器）能夠以標準化的方式啟用這些功能，OpenType 將所有的 GSUB 與 GPOS 操作歸類進一組由 **4 個 ASCII 字元組成的特性標籤（Feature Tags）**中：

| 特性標籤 | 英文全稱 | 類別 | 核心功能與應用場景 |
|:---|:---|:---|:---|
| `liga` | Standard Ligatures | GSUB | 標準合字（預設開啟）：處理 `fi`, `fl`, `ff` 等基礎排版連字，消除字形碰撞 |
| `dlig` | Discretionary Ligatures | GSUB | 自由/美學連字（預設關閉）：特殊歷史或裝飾性連字，如 `st`, `ct`, `Th` |
| `hist` | Historical Forms | GSUB | 歷史異體字：長 `s`（`ſ`）等古典排版字形替換 |
| `smcp` | Lowercase to Small Capitals | GSUB | 將普通小寫字母替換為光學設計的小型大寫字母 |
| `c2sc` | Capitals to Small Capitals | GSUB | 將普通大寫字母替換為小型大寫字母（用於全小大寫混排） |
| `onum` | Oldstyle Figures | GSUB | 舊體/懸掛數字：具有高低起伏升降部的數字（`0123456789`），融入正文文字流 |
| `lnum` | Lining Figures | GSUB | 齊線數字：高度完全一致的現代西文數字，常用於表格排版 |
| `tnum` | Tabular Figures | GPOS | 表格等寬數字：強制所有數字具有完全相同的水平前進寬度，保證賬目縱向對齊 |
| `pnum` | Proportional Figures | GPOS | 比例數字：每個數字具有符合自身形態的自然字寬 |
| `frac` | Diagonal Fractions | GSUB | 對角斜線分數：將 `1/2`, `3/4` 自動替換為單字分數或分子下標/分母上標 |
| `afrc` | Alternative Fractions | GSUB | 豎線水平分數：將分數排版為帶水平橫線的垂直堆疊結構 |
| `kern` | Kerning | GPOS | 字距調整（預設開啟）：微調特定字對之間的水平物理間隙 |
| `mark` | Mark Positioning | GPOS | 標音符號吸附（預設開啟）：將音標磁吸至基底字元的物理錨點上 |
| `mkmk` | Mark-to-Mark Positioning | GPOS | 多重標音符號堆疊吸附 |
| `curs` | Cursive Attachment | GPOS | 草書連筆平滑連線 |
| `size` | Optical Size | 雜項 | 光學尺寸引數宣告：宣告字型專屬設計的字號與推薦使用字號區間 |
| `aalt` | Access All Alternates | 元特性 | 彙集字形的所有變體，供排版軟體的“字形調色盤”全域性檢視 |

---

## 2. 在 FontLab 中管理 OpenType 表與 AFDKO 特性定義語言

**FontLab Studio**（版本 4.x 與 5.x）是商業字型開發領域的工業級標杆。在 FontLab 中，OpenType 排版表並非透過散亂的表單配置，而是直接採用了由 Adobe 制定並在開源社群廣泛通行的標準：**AFDKO（Adobe Font Development Kit for OpenType）特性定義語言（Feature Definition Language）**。

在 FontLab 的主選單中開啟 `Window > Panels > OpenType`，即可喚出 OpenType 面板。該面板頂部列出當前字型中定義的所有 Feature，中部為純文字程式碼編輯區，底部則是全域性字形類的宣告區。如果在編譯時程式碼存在哪怕一個語法錯誤，FontLab 將直接中斷並報錯：
`<PalatinoLinotype-Roman> aborting because of errors`
因此，深入掌握 AFDKO 語法是每位專業字型工程師的必修基本功。

### 2.1 AFDKO 特性定義語言的完整語法規範

#### 1. 字形類（Glyph Classes）的定義與集合運算
在字型排版中，許多字形遵循完全相同的上下文行為。AFDKO 允許使用中括號 `[` 和 `]` 將字形組織為**字形類（Glyph Class）**，類名必須以 `@` 符號開頭：

```fea
# 1. 顯式列舉定義
@VOWELS = [ a e i o u y ];

# 2. ASCII 字典序連續範圍定義（使用連字元 -）
@UPPERCASE = [ A-Z ];
@DIGITS = [ zero-nine ];

# 3. 帶特定前字尾的字形範圍定義
@SC_LETTERS = [ a.sc-z.sc ];
@HIST_FIGURES = [ foo.023-foo.437 ];

# 4. 類的巢狀與組合
@ALL_LETTERS = [ @UPPERCASE @VOWELS agrave eacute ];
```

#### 2. 書寫系統、語言與特性的層級結構
AFDKO 程式碼嚴格對映 OpenType 內部的四級索引樹：**Script（書寫系統） $\longrightarrow$ Language（語言系統） $\longrightarrow$ Feature（特性） $\longrightarrow$ Lookup（查詢表）**。

```fea
# 宣告字型支援的全域性語言系統
languagesystem DFLT dflt; # 預設預設語言
languagesystem latn dflt; # 拉丁文預設
languagesystem latn TRK ; # 拉丁文土耳其語（點 i 特殊處理）
languagesystem cyrl dflt; # 西里爾文預設

feature liga {
    script latn;
    language DFLT;
        # 針對拉丁文預設語言應用規則 A
        sub f i by f_i;
    language DEU;
        # 德語繼承預設規則，並追加規則 B
        sub c k by c_k;
    language ENG excludeDFLT;
        # 英語顯式排除預設規則（excludeDFLT），僅應用專用規則 C
        sub f f l by f_f_l;
} liga;
```
- `languagesystem` 語句必須在整個特性的最外層預先宣告；
- `excludeDFLT` 關鍵字具有極高的工程實用價值：當特定語言不希望繼承預設規則時，可以乾淨利落地將其遮蔽。

#### 3. 命名查詢表（Named Lookups）與標記標誌位（`lookupflag`）
查詢表（Lookup）是組織替換或定位規則的獨立原子程式碼塊。在一個特性內部，可以透過 `lookup` 關鍵字定義命名查詢表，從而被其他特性複用或精確控制執行次序：

```fea
lookup MyLigatures {
    sub f i by f_i;
    sub f l by f_l;
} MyLigatures;

feature liga {
    lookup MyLigatures;
} liga;
```

為了防止標音符號或連字破壞上下文匹配，AFDKO 提供了 `lookupflag` 指令，用於指示排版引擎在掃描字元流時忽略特定型別的字形：
- `lookupflag IgnoreBaseGlyphs;`：跳過普通基底字形；
- `lookupflag IgnoreLigatures;`：跳過連字字形；
- `lookupflag IgnoreMarks;`：**跳過所有標音符號**。這是西文和阿拉伯文連字排版的關鍵指令，確保字母 `f` 與 `i` 之間即使插入了一個重音符號（如聲調標音），引擎依然能夠識別出 `f` 與 `i` 相鄰並順利觸發連字；
- `lookupflag RightToLeft;`：指示該查詢表專門服務於從右向左的書寫系統。

#### 4. 字形替換規則（GSUB 規則全集）
- **單字替換（Single）**：
  `sub a by a.sc;`
  也可以在兩個等長類之間實現全自動平行替換：
  `sub @UPPERCASE by @SC_LETTERS;`
- **合字替換（Ligature）**：
  `sub f i by f_i;`
  `sub f f i by f_f_i;`
- **多字替換（Multiple）**：
  `sub f_f_i by f f i;`
- **備選替換（Alternate）**：
  `sub ampersand from [ ampersand.alt1 ampersand.alt2 ampersand.alt3 ];`
- **上下文替換（Contextual Substitution）與撇號語法（`'`）**：
  在 AFDKO 語法中，**非定向撇號（`'`）**是判定上下文作用域的關鍵標尺。**帶有撇號的字形代表實際要被替換的目標，而未帶撇號的字形僅僅構成周圍的上下文環境**：
  ```fea
  # 當字母 d 後面緊隨母音時，將 d 替換為更舒展的花體 d.prettier
  sub d' @VOWELS by d.prettier;

  # 當字母 i 出現在連字 f 或 ff 之後時，將其替換為無點 i（i.nodot），防止與 f 的出刀端相撞
  sub [ f f_f ] i' by i.nodot;
  ```
- **例外排除規則：`ignore sub` 的語法陷阱**：
  假設我們希望將普通文字中獨立出現的單詞 “TEX” 替換為專有標誌字形 `T_e_X`。如果直接書寫 `sub T E X by T_e_X;`，那麼包含這三個字母的正常單詞（如 `CONTEXTUAL`、`PRETEXTS`、`TEXT`、`CORTEX`）都會遭到誤傷，被替換成破碎的標誌。
  我們必須使用 `ignore sub` 宣告前後如果緊鄰英文字母則忽略替換。AFDKO 允許使用逗號將多個忽略條件並聯：
  ```fea
  # 必須使用撇號標記上下文作用域
  ignore sub [ A-Z ] T' E' X' , T' E' X' [ A-Z ] ;
  sub T' E' X' by T_e_X ;
  ```
  > [!WARNING] **AFDKO 語法陷阱**
  > 注意上述第二行程式碼中的 `T' E' X'` 也必須帶上撇號！雖然第二行表面上看是一個普通合字替換，但由於第一行的 `ignore sub` 為整個查詢表確立了上下文語境，整個程式碼塊被編譯器強制提升為上下文查詢表，第二行的被替換目標必須嚴格借用撇號語法，否則編譯將直接失敗。

#### 5. 字形定位規則（GPOS 規則全集）
排版位移的核心是 **值記錄（Value Record）**，它是由尖括號包裹的 4 個整數：
$$\langle xPlacement \quad yPlacement \quad xAdvance \quad yAdvance \rangle$$
- $xPlacement$：字形在 X 軸的物理繪製原點偏移量；
- $yPlacement$：字形在 Y 軸的物理繪製原點偏移量；
- $xAdvance$：字形在 X 軸上的前進寬度增減量；
- $yAdvance$：字形在 Y 軸上的前進高度增減量（用於垂直排版）。

常見物理行為模式：
1. `<0 0 -50 0>`：僅縮減前進寬度 50 單元，字形本身繪製位置不變，使下一個字形向左靠攏 50 單元（最經典的單值字距調整，可簡寫為 `-50`）；
2. `<30 0 0 0>`：字形向右平移 30 單元，但前進寬度不變；
3. `<0 30 0 0>`：字形向上提升 30 單元，基線保持不變（全大寫括號提升）；
4. `<0 -30 0 -30>`：字形向下平移 30 單元，且下一個字形的基線起點也同步下沉 30 單元。

- **類間字距對調整（Class-based Kerning）**：
  ```fea
  pos @Left_Round @Right_Round -40;
  ```
  如果 `@Left_Round` 包含 7 個字形，`@Right_Round` 包含 3 個字形，該單行語句在編譯後將自動在 GPOS 表中展開並生成 $7 \times 3 = 21$ 個高精度的字對調整記錄！
- **草書連筆定位（Cursive Attachment）**：
  ```fea
  pos cursive f <anchor -10 0> <anchor 197 105>;
  pos cursive i <anchor -5 0>  <anchor 155 105>;
  ```
  前一個 anchor 宣告當前字形的入刀點（Entry），後一個 anchor 宣告出刀點（Exit）。
- **合字上的標音符號吸附（Mark-to-Ligature）**：
  以義大利文或法文中帶雙揚抑符的三部件合字 `e_t_a`（如 `prêtâmes`）為例，合字擁有 3 個邏輯槽位：
  ```fea
  mark circumflex <anchor 151 438>;
  pos ligature e_t_a <anchor 286 432> <anchor NULL> <anchor 832 432> mark circumflex;
  ```
  使用 `<anchor NULL>` 巧妙跳過中間字母 `t`，直接為第一個部件 `e` 和第三個部件 `a` 分別賦予精準的聲調吸附座標。

#### 6. 光學尺寸特性（`size`）與備選彙總（`aalt`）
傳統向量字型徹底遺棄了金屬活字時代隨字號變化而微調粗細比率的“光學尺寸”傳統。OpenType 透過 `size` 特性填補了這一鴻溝：
```fea
feature size {
    parameters 120 1 90 299;
} size;
```
- `120`：字型的標準設計光學尺寸（Design Size），以十分之一點（decipoints）為單位，即 **12.0 pt**；
- `1`：字型在所屬家族光學尺寸序列中的編號（從 0 開始計數）；
- `90` 與 `299`：推薦排版軟體應用該字型的字號區間：**9.0 pt 至 29.9 pt**。當使用者在排版軟體中將字號調整至 36 pt 時，引擎將自動排程專為大標題設計的 ITC Bodoni 72。

### 2.2 FontLab Studio 圖形化工作流實戰
1. **程式碼編寫與即時編譯**：在 OpenType 面板中輸入上述程式碼，點選右上角的 **Compile** 按鈕。FontLab 將呼叫內部整合的 AFDKO 編譯器進行語法檢查並生成二進位制表結構。
2. **Preview 預覽面板互動**：開啟 `Window > Panels > Preview`。在預覽視窗中，字型工程師可以勾選需要啟用的 Feature（如 `liga`, `smcp`, `onum`），從下拉選單中指定 `script` 和 `language`，並在文字框中輸入測試字串（支援透過斜槓輸入字形名稱，如 `/eacute`）。視窗將上下分欄對比展示開啟特性前後的實時向量渲染效果。
3. **位移向量視覺化**：點選預覽面板中的箭頭按鈕，FontLab 將直接在螢幕上以高亮線段繪製出每個字形的前進位移向量與錨點重合狀態。
4. **字形型別分類（Glyph Typing）**：在字形單元格上右鍵選擇 `Properties`，在彈出視窗中可明確將字形標記為 `Single Glyph`、`Ligature`、`Mark` 或 `Component`。這一分類資料將直接被寫入 OpenType 的 `GDEF`（字形定義表）中，作為 `lookupflag IgnoreMarks` 能夠準確執行的底層依據。

---

## 3. 在微軟 VOLT 中視覺化構建 OpenType 排版表（Managing OpenType Tables in VOLT）

由微軟官方推出的 **VOLT（Visual OpenType Layout Tool）** 是專門用於為 TrueType/OpenType 字型新增複雜高階排版表的高階專用工具。與 FontLab 的純文字編譯模式不同，VOLT 提供了一套深度繫結 Windows **Uniscribe** 整形引擎的視覺化圖形工作流。

### 3.1 VOLT 的架構哲學與私有資料表
- **專屬工作環境**：VOLT 僅執行在 Windows 平臺下。
- **字型無損保留與破壞性開啟**：VOLT 採用了一種特殊的內部專案儲存方式。當在 VOLT 中儲存字型時，它會將全部工程原始碼、組名、錨點連線網以私有二進位制資料表（如 `TSIV` 表）的形式直接嵌入到 TTF 字型檔案內部。
  > [!CAUTION] **資料覆蓋警告**
  > 當使用 VOLT 開啟一個由其他軟體（如 FontLab 或 FontForge）生成的 OpenType 字型時，VOLT 會**強制抹除所有現存的標準 GSUB/GPOS 表**，僅保留自身能夠識別的私有表！若未備份原始碼，此前的排版表工作將徹底丟失。
- **PostScript 名稱匯入**：由於 TrueType 字形在底層僅以 GID（字形編號）標識，VOLT 開啟字型後第一步必須執行 `Import > Import PostScript Names`，從字型的 `post` 表或 `name` 表中恢復人類可讀的字形名稱。
- **全字形型別標記（Glyph Typing）**：在 `Tools > Edit Glyphs` 視窗中，字型工程師必須對字型中所有字形進行嚴格的類別稽核，將每個符號確鑿歸類為 `base`（基字）、`ligature`（連字，需指定部件數目）、`mark`（標音符號）或 `component`（部件）。

### 3.2 查詢表與規則編輯
VOLT 的專案主視窗（Project Window）呈現清晰的三欄架構：
1. **層次樹（Hierarchy Area）**：展示 Script、Language、Feature 的樹形隸屬關係；
2. **查詢表庫（Lookup List）**：平鋪展示字型中所有全域性獨立的 Lookup；
3. **字形組庫（Glyph Classes）**：展示所有預定義的字形分組。

#### 1. 替換規則的視覺化與箭頭語法
雙擊一個替換查詢表，VOLT 呈現出極其直觀的編輯介面。在規則網格中，規則以簡單的箭頭形式書寫：
- **單字替換**：`a -> a.sc`（VOLT 會自動在旁側列繪製出字形的真實微縮點陣圖）；
- **連字替換**：`f i -> f_i`；
- **多字替換**：`f_f_t -> f f t`；
- **交替字形**：連續書寫多條單字對映：
  ```text
  a -> a.old
  a -> a.odd
  a -> a.pretty
  ```
- **上下文替換**：在被替換字形兩側使用管道符 `|` 宣告前後上下文環境：
  ```text
  [ zero - nine ] | [ zero - nine ] -> [ slash.fraction ]
  ```
- **逆向鏈式替換（Reversal）**：在查詢表屬性中勾選 **Reversal** 選項框。針對烏爾都語的倒序排版，VOLT 將指示 Uniscribe 引擎從右向左逆流掃描，完美解決複雜的斜向垂直懸掛排版問題。

#### 2. 定位規則與互動式錨點吸附（Visual Anchor Attachment）
在定位編輯視窗中，VOLT 徹底展現了視覺化互動的巨大威力：
- 視窗右側為大尺寸的高精度字形工作畫布；
- 字型工程師在定義 Mark-to-Base 或 Mark-to-Ligature 時，畫布上會同時浮現出基字與標音符號的向量輪廓；
- 工程師可以直接用滑鼠在畫布上拖拽標音符號，將其拖動至視覺上最完美的相對位置，VOLT 會在後臺自動計算兩者的相對距離並精確鎖定各自的 Anchor 座標；
- 支援為合字中的每一個組成部件依次建立名為 `Component 1: Anchor`、`Component 2: Anchor` 的分立吸附點。

### 3.3 VOLT 校對工具（Proofing Tool）與成品釋出
VOLT 內建了強大的 **Proofing Tool**（校對工具）。點選該按鈕即可開啟一個專門的排版測試視窗，該視窗直接呼叫作業系統底層的 Uniscribe 引擎。工程師可以輸入任意長文字測試用例，視窗將一步一步動態高亮展示每條查詢表的觸發過程、字形替換前後的序列演變以及各錨點的吸附向量。

測試無誤後，透過 `File > Ship Font` 命令即可匯出最終商用字型。VOLT 在此時會自動編譯出純淨的標準 OpenType 表，並徹底剔除龐大的內部 `TSIV` 工程表，生成體積高度最佳化的最終檔案。

---

## 4. 在 FontForge 中管理 OpenType 表（Managing OpenType Tables in FontForge）

與商業軟體 FontLab 的程式碼驅動和 VOLT 的排他性架構完全不同，開源自由軟體 **FontForge**（由 George Williams 領銜開發）提供了一種**純選單化、原生雙向無損**的 OpenType 管理體驗。

FontForge 不強迫使用者學習任何專有程式碼語法，一切排版表操作均透過圖形視窗、樹狀列表和嚮導式對話方塊完成。更重要的是，FontForge 能夠直接解析字型中現有的任何 OpenType 表，並在儲存時直接寫回標準的二進位制表結構。

### 4.1 核心控制檯：Element > Font Info > Lookups
在 FontForge 中開啟 `Element > Font Info`，切換至 **Lookups** 選項卡。該面板被清晰地劃分為兩大部分：**GSUB** 選項卡與 **GPOS** 選項卡。

在每個選項卡內部，Lookups 以樹狀摺疊列表的形式呈現。使用者可以點選 `Add Lookup` 建立新的查詢表，指定其型別（如 Single Substitution、Ligature、Pairwise Positioning 等），並在其下點選 `Add Subtable` 為其掛載具體的規則子表。查詢表的執行嚴格遵循從上到下的幾何物理次序，使用者可以透過 `Up` 和 `Down` 按鈕隨時調整其優先順序。

### 4.2 錨點體系與類定義（Anchor Classes）
FontForge 將錨點的管理提升到了字形畫布的核心互動層：
1. **全域性類宣告**：在 `Font Info > Anchor Classes` 視窗中點選 `New`，定義錨點類的名稱（如 `Top`、`Bottom`、`Entry`、`Exit`），並指定其排版語義：
   - `abvm`：基字上方標音定位（Above-base mark positioning）；
   - `blwm`：基字下方標音定位（Below-base mark positioning）；
   - `mark`：通用標音吸附；
   - `mkmk`：標音疊合標音定位；
   - `curs`：草書連續連筆定位。
2. **畫布直觀放置**：關閉設定後開啟任意字形的編輯視窗，在輪廓上的目標位置右鍵點選，選擇 `Add Anchor Point`。在彈出的下拉選單中選擇此前定義的錨點類（如 `Top`），該錨點即以圖形標記的形式釘死在畫布上。字形視窗中會實時顯示該錨點的名稱與絕對座標，一目瞭然。

### 4.3 非上下文替換與定位
在字形列表視窗中，右鍵選中任意字形並點選 `Glyph Info`：
- **單字替換（Single Subs）**：在 `Substitutions` 標籤下點選 `New`，指定目標替換字形與關聯的 Feature Tag；
- **多字替換（Mult Subs）**：輸入拆解後的多個字形名稱（以空格分隔）；
- **交替字形（Alt Subs）**：輸入多個備選變體列表；
- **合字替換（Ligatures）**：在目標合字（如 `f_i`）的屬性視窗中，填入構成它的源字形元件列表（`f i`）。

在定位方面，`Glyph Info > Pairwise Pos` 允許為當前字形新增字對定位規則。在彈出的配對視窗中選擇第二字形（Second Glyph），即可獨立調整第一字形和第二字形的原點偏移與前進量 $\Delta XAdvance$。

### 4.4 鏈式上下文排版嚮導（Chained Contextual Lookups）
針對複雜的上下文排版，FontForge 提供了強大的 4 步向導式配置流程（見圖 14-13）：
- **步驟 1：格式選擇（Format）**：選擇規則基於字形覆蓋列表（By Coverage）、基於字形類別（By Classes）還是基於獨立字形列舉（By Glyphs）。
- **步驟 2：序列劃分（List of Classes）**：將目標文字流劃分為三大連續區域：
  1. **Backtrack（回溯序列）**：匹配目標之前必須出現的字形環境；
  2. **Match / Input（匹配序列）**：當前正在掃描並即將被改變的目標字形序列；
  3. **Lookahead（前瞻序列）**：匹配目標之後必須緊隨的字形環境。
- **步驟 3：巢狀子查詢表繫結（Sub-lookup Calls）**：在 Match 序列中，精確指定將第幾個字形交由哪一個此前已定義好的非上下文查詢表（如某個單字替換或合字替換）進行實際處理。
- **步驟 4：多規則覆蓋排序**：為整個上下文特性配置一系列規則的匹配優先順序，確保長詞優先、特殊模式優先於一般模式。

---

## 5. 在 FontForge 中構建蘋果高階排版（AAT）有限狀態機（Managing AAT Tables in FontForge）

在整個數字排版世界中，FontForge 是極少數（甚至在很長一段歷史時期內是唯一一個）能夠完整建立與編輯 **Apple Advanced Typography（AAT）** 表的通用工具。

### 5.1 AAT 與 OpenType 的計算理論對決
深入理解 AAT，必須首先理解其背後由 QuickDraw GX 奠定的電腦科學哲學。AAT 與 OpenType 構成了排版引擎設計上的兩條截然不同的路線：

```
OpenType 架構：宣告式模式匹配樹（Declarative Pattern-Matching Engine）
  [ 掃描輸入流 ] ──> [ 全域性遍歷 Feature 規則 ] ──> [ 遞迴回溯匹配 ] ──> [ 規則替換 ]
  特徵：計算複雜度受上下文深度與規則鏈巢狀影響，最壞情況下存在回溯與效能抖動。

AAT 架構：確定性有限狀態自動機（Deterministic Finite State Automata, FSM）
  [ 字元流輸入 ] ──> [ 狀態轉移：State_i ─(Class_k)─> State_j ] ──> [ 觸發瞬時動作 ]
  特徵：單向線性掃描，時間複雜度恆定為 O(N)，無回溯，底層執行極度高速穩定。
```

AAT 廢棄了龐雜的規則匹配，將排版完全建模為一個帶有動作的**有限狀態機（Finite State Machine）**。字型檔案內部包含四張核心 AAT 表：
1. **`morx`（Extended Glyph Metamorphosis Table）**：形態變換表，包含全部基於狀態機的字形替換與重排；
2. **`kerx`（Extended Kerning Table）**：擴充套件字距表，包含基於狀態機的上下文字距微調；
3. **`feat`（Feature Name Table）**：特性與選擇器名稱表，向作業系統 UI 提供本地化的人類可讀選單名；
4. **`trak`（Tracking Table）**：全域性字間距跟蹤表，根據實際字號自動拉開或收緊整行文字的字距。

### 5.2 特性與選擇器命名體系（Features and Selectors）
在 AAT 中，每一個排版效果由一個**特性（Feature）**和一個具體的**選擇器（Selector）**二元組共同標識：
- 在 FontForge 中開啟 `Element > Font Info > Mac Features`；
- 每一個 Feature 擁有一個數字識別符號 `Feature_Id`（例如 5 代表合字，11 代表數字樣式）；
- 每個 Feature 包含若干個可選的 `Setting_Id`（例如設定 0 為開啟常用合字，1 為開啟罕見合字）；
- 字型工程師可以為特性和選擇器輸入多種自然語言的本地化字串（英語、法語、中文等）。當在 Mac OS X 的文字程式（如 TextEdit、Pages）中開啟排版面板時，系統將直接根據當前系統語言顯示這些優雅的原生選單。

### 5.3 AAT 狀態機四大核心操作（Font Info > Mac SM）
在 `Font Info > Mac SM`（Mac State Machines）面板中，包含了 AAT 的四大核心狀態機引擎：

#### 1. 字形重排狀態機（Glyph Rearrangement）
**這是 AAT 獨步天下、而在 OpenType 中完全沒有對應底層表的革命性設計**。在 OpenType 中，字元重排必須依賴作業系統外部驅動（如 Uniscribe）對特定語言的硬寫支援；而 AAT 允許字型本身直接透過內部狀態機完成任意複雜的字形物理位置對調。

- **南亞文字天城文重排案例**：
  在天城文中，短母音 `r` 在邏輯編碼上輸入在子音簇之後，但在物理顯示時必須移至整組子音的前面。例如，輸入字元序列 `KGPTHr`，必須自動蛻變為顯示序列 `rKGPTH`。
- **狀態轉移圖推演**：
  1. **狀態 0（初始狀態/行首）**：當遇到非子音字元時保持狀態 0；一旦遇到屬於子音類的字元（`K`, `G`, `P`, `T`, `H`），系統發生轉移，躍遷至 **狀態 2（子音收集狀態）**，並勾選動作 **Mark Current Glyph As First**（將該子音標記為重排區間的起始點 A）；
  2. **狀態 2（子音迴圈狀態）**：若繼續讀入子音字元，系統停留在狀態 2，不改變標記；
  3. **遇到母音觸發重排**：當在狀態 2 讀入字元 `r`（類 5）時，系統立即將當前字元 `r` 標記為區間終點 D，並在下拉選單中選擇執行代號為 `xD => Dx` 的重排指令！
  4. 瞬間，原本位於尾部的終點字形 `r` 被精準移送至起始子音的前方，隨後狀態機重置回狀態 0，整個過程僅耗費極微小的 CPU 週期。

#### 2. 上下文替換狀態機（Contextual Substitution）
在確定性有限狀態機中，由於文字流只能向前單向推進，當排版引擎讀到後隨字元從而確認上下文時，前一個字元在時間線上已經“過去了”。
AAT 巧妙地透過 **標記當前字形（Mark Current Glyph）** 機制解決了這一時空矛盾：
- 狀態機在掃描過程中，先為可能發生改變的字形打上臨時標記（Mark）；
- 繼續前行掃描後置上下文，一旦後置條件滿足，立即觸發 **Mark Subs** 動作，對早先標記的那個字形執行回溯性替換；
- **斜向分數實戰**：輸入 `1/2` 自動轉換為漂亮的對角分數：
  - 遇到第一個數字 `1` 時，將其標記，狀態遷移至“分子狀態”；
  - 遇到斜槓 `/` 時，確認分數結構成立，觸發對被標記的數字 `1` 執行替換，將其變為分子字形 `1.numerator`，斜槓自身替換為分數斜槓，狀態遷移至“分母狀態”；
  - 遇到後隨的數字 `2` 時，直接替換為分母字形 `2.denominator`。

#### 3. 字形動態插入狀態機（Glyph Insertion）
該狀態機允許在原始文字流中**憑空動態插入原本不存在的全新字形**，這在處理複雜書寫系統時具有無可替代的威力：
- **阿拉伯文 Kashida（拉長線）動態注入**：在兩端對齊排版中，阿拉伯文不是透過拉大字間距來對齊，而是在字母連筆處插入一條被稱為 Kashida（Tatweel）的水平連線線。AAT 能夠根據排版引擎的拉伸訊號，在特定的字母連線點狀態機中動態插入若干個 Kashida 字形；
- **高棉文裂變母音（Split Vowels）注入**：柬埔寨文字中的部分複合母音需要同時出現在子音的左側和右側。狀態機在掃描到該母音時，原地保留右側部分，同時在子音左側動態插入一個新的左側字形。
- **游標互動屬性控制**：狀態機專門提供了屬性核取方塊，用於指示插入的字形是作為獨立字元響應滑鼠游標選擇，還是作為依附於相鄰字元的“幽靈字形”（不可單獨選中文字），完美保障了文字編輯時的互動體驗。

#### 4. 上下文擴充套件字距狀態機（Contextual Kerning / `kerx`）
AAT 將字距調整徹底升級為一個**帶堆疊的狀態機系統**：
- 狀態轉移單元中提供了一個核取方塊 **Push Current Glyph**（將當前字形壓入記憶體棧，最多可連續壓棧 8 個字形）；
- 狀態機一路讀取字元並壓棧，當識別出終結匹配的字元時，系統觸發出棧（Pop）動作；
- 當 $n$ 個字形連續出棧時，系統在底部的引數區同時賦予 $n-1$ 個字距偏移量！
- **應用場景**：完美解決 `A.V.` 縮寫詞的字距問題。遇到 `A` 壓棧，遇到 `.` 壓棧，遇到 `V` 出棧，對 `A-.` 賦予 0 偏移，對 `.-V` 賦予 `-400` 強力負字距，而在普通文字流中則絕不誤傷。

---

## 6. 結語與現代排版技術圖景（Conclusions and Modern Outlook）

回顧從早期數字排版到 OpenType 與 AAT 的輝煌演進，我們可以清晰地看到計算文字學（Computational Typography）的發展脈絡：

1. **歷史力量的交匯與博弈**：
   20 世紀 90 年代末，微軟主導的 Windows Uniscribe 引擎與蘋果主導的 Mac OS ATSUI/CoreText 引擎展開了長達十餘年的技術競爭。OpenType 憑藉 Adobe 的全力支援與 AFDKO 開源工具鏈的普及，贏得了跨平臺桌面出版與商業字型廠商的壓倒性青睞；而 AAT 則以其驚世駭俗的有限狀態機理論高度和對極端複雜文字的優雅掌控，在蘋果生態圈中深深紮根。
2. **現代排版大一統：HarfBuzz 的崛起**：
   進入 21 世紀 10 年代後，由 Behdad Esfahbod 領銜開發的現代開源文字整形引擎 **HarfBuzz** 徹底終結了分裂局面。HarfBuzz 內部完美相容並原生實現了 OpenType（GSUB/GPOS/GDEF）與 AAT（morx/kerx）的全部規範，被廣泛整合到 Google Chrome、Mozilla Firefox、Android 系統、Linux 桌面乃至最新的 Adobe 產品中。
3. **字型的本質躍遷**：
   現代字型已經徹底擺脫了“字元編碼翻譯表”的原始定義。每一款現代 OpenType/AAT 字型都是一個**兼具幾何學、代數學與自動機理論的自洽微型計算機**。正是這些深藏在二進位制表結構底層的特性、錨點與狀態機，使得數千年人類文明沉澱下來的書法神韻與排版規度，得以在現代數字高精度螢幕與高速印刷機上生生不息、完美重現。

*本章的完整 1:1 全景翻譯與專業技術校正由 ヴワル魔法図書館（Voile Magic Library）文獻翻譯工房 嚴格依據原著核對呈現。*
