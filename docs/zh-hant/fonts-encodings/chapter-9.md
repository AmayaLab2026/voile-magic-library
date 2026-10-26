---
title: "第 9 章：TeX 與 Omega 中的字型及其安裝與使用"
description: "詳盡解析 TeX 的盒子-膠水物理模型、斷行演算法、NFSS、DVI 格式、afm2tfm、fontinst 虛擬字型合成與 Omega 16位元多向排版。"
---

# 第 9 章：$\TeX$ 與 $\Omega$ 中的字型及其安裝與使用
### Chapter 9: Fonts in $\TeX$ and $\Omega$, Their Installation and Use
選自《Fonts & Encodings》第 235–314 頁
*譯者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

$\TeX$ 及其後繼者 $\Omega$（Omega）堪稱世界上最精密、最強大的數位排版系統。正因如此，這兩個系統中的字型管理機制在初涉者眼中往往顯得格外繁複且深奧。在本章中，我們將從三個核心維度對 $\TeX$ 與 $\Omega$ 的字型體系展開全面而嚴謹的剖析：

1. **字型在 $\TeX$ 與 $\Omega$ 中的使用**：探討使用者如何在普通 $\TeX$ 或 $\LaTeX$ 文件中調用、配置並組織系統中已安裝的字型；
2. **字型的基本安裝流程**：系統闡述如何將外部輪廓字型（如 PostScript Type 1、TrueType 以及 Multiple Master 字型）轉換為 $\TeX$ 與 $\Omega$ 能夠識別的底層度量檔案與設定檔；
3. **字型的深度定制**：探索如何借助虛擬字型（Virtual Fonts, VF）與變換巨集套件（如 `fontinst`），構建包含複合重音、特殊連字、偽小型大寫字母（Fake Small Capitals）、甚至能夠進行上下文連綴分析的高級定制字型族。

最後，我們將深入探索打破傳統 8 位元束縛的 $\Omega$ 系統——它引入了多位元組內部編碼、OFM（Omega Font Metrics）、OVF（Omega Virtual Fonts）、動態有限狀態流轉換器 OTP（Omega Translation Processes）以及支援 32 種正交書寫方向的宏大多向排版引擎。

---

## 1. 在 $\TeX$ 中使用字型（Using Fonts in $\TeX$）

### 1.1 $\TeX$ 導論：排版哲學與盒子-膠水模型（Introduction to $\TeX$）

要真正理解 $\TeX$ 是如何對待字型的，我們必須首先摒棄所見即所得（WYSIWYG）桌面排版軟體中那種「將字元直接繪製到螢幕畫布」的直觀思維。在唐納德·高德納（Donald E. Knuth）教授構建的 $\TeX$ 宇宙中，排版的核心本質是純粹的數學抽象與二維裝配工程。

#### 盒子（Boxes）與膠水（Glue）

$\TeX$ 將排版構件抽象為兩大基本物理實體：**盒子（Box）**與**膠水（Glue）**。

1. **盒子（Box）**：
   在 $\TeX$ 引擎眼中，每一個字元、每一個標點、每一條實線規則甚至每一幅外部插圖，都被嚴格封裝在一個剛性的矩形空間內。對於任意字元盒子，$\TeX$ 完全不在意其內部究竟繪製了何種優美的筆畫曲線，而僅僅追蹤該字元在二維平面上的三個基礎幾何度量參數：
   - **寬度（Width, $w$）**：字元沿當前基線（Baseline）延伸的水平跨度；
   - **高度（Height, $h$）**：字元從基線向上伸展至最高輪廓邊緣的垂直距離；
   - **深度（Depth, $d$）**：字元從基線向下延伸至降部（Descender）最低底部的垂直距離。

   基線是排版的靈魂基準。字元盒子的左下角偏上位置即為參考原點 $(0,0)$。例如，小寫字母「x」的高度即為通常所稱的 x 高度（x-height），其深度為 0；而帶有降部的小寫字母「p」與「y」，則具有顯著的正向深度；帶有升部（Ascender）的字母「d」與「h」，則具有顯著的高度。

2. **膠水（Glue）**：
   如果說盒子是構建文件大廈的剛性磚石，那麼膠水就是連接磚石的彈性水泥。在西文排版中，詞與詞之間的空格並非固定寬度的實體，而是一段具有彈性的膠水。膠水具有三個核心數學分量：
   - **自然尺寸（Natural Space）**：膠水在未受任何外力拉伸或壓縮時的理想寬度；
   - **可伸展量（Stretchability）**：當整行文字需要被兩端對齊（Justified）而字元總寬度不足時，該膠水允許被拉長的最大彈性裕量；
   - **可收縮量（Shrinkability）**：當整行文字稍微超出排版版心寬度時，該膠水允許被壓縮擠緊的最大彈性裕量。

#### 水平盒子（hbox）與垂直盒子（vbox）的層級嵌套

$\TeX$ 透過層級遞迴將微觀元素裝配為宏觀頁面：
- 若干個字元盒子與詞間膠水在水平方向上依次排列，構成**水平盒子（hbox）**。段落中的單行文字即為一個 hbox；
- 若干個水平盒子再與行間膠水（Baselineskip，即基線行距膠水）在垂直方向上從上至下堆疊排列，構成**垂直盒子（vbox）**。文件中的文字欄、整個頁面、甚至帶有邊註與頁尾的完整版面，都是一層層嵌套的 vbox。

#### 斷行演算法與折損機制（Line Breaking and Demerits）

普通文字處理軟體通常採用貪婪演算法（Greedy Algorithm）進行逐行排版：一行只要放得下單詞就繼續放，放不下就強行斷行。這種局部最佳化策略往往導致段落末尾出現極其醜陋的巨大空白或極度稀疏的字行。

Knuth 為 $\TeX$ 設計了革命性的全域動態規劃斷行演算法：
1. **不良度（Badness, $b$）**：衡量某一行內膠水偏離其自然尺寸的惡劣程度。若一行被拉伸或壓縮得過於嚴重，其不良度將急劇上升；
2. **懲罰值（Penalties, $p$）**：在潛在斷行位置（如連字元處、標點後、數學公式間）人為施加的代價權重。例如，在連字元處斷行會引入正向懲罰，而在顯式禁止斷行處懲罰為無窮大（$+10,000$）；
3. **折損值（Demerits, $d$）**：綜合單行不良度、斷行懲罰值以及相鄰兩行膠水鬆緊差異（防止一行極緊、下一行極鬆的視覺突兀）計算出的段落全域惡劣評分。

$\TeX$ 會構建整個段落所有可能斷行方案的有向無環圖（DAG），並透過動態規劃演算法找出全域折損值總和最小的完美斷行路徑。這使得 $\TeX$ 排出的段落灰度（Typographic Color）極其均勻平穩。

#### 電腦現代字型族（Computer Modern Family）與光學尺寸

伴隨 $\TeX$ 系統誕生的基石字型是高德納親自使用 METAFONT 程式語言設計的**電腦現代字型族（Computer Modern, CM）**。CM 字型族基於 19 世紀末蘇格蘭現代體（Modern Face，以 Monotype Modern 8A 為藍本）精心繪製，具有極高的筆畫對比度、幾何垂直的軸線與銳利的細襯線。

CM 字型族不僅涵蓋了豐富的風格變體：
- `cmr`（Computer Modern Roman，正體）
- `cmbx`（Computer Modern Bold Extended，粗體展寬）
- `cmti`（Computer Modern Text Italic，內文字型義大利斜體）
- `cmsl`（Computer Modern Slanted，偽斜體/機械傾斜體）
- `cmss`（Computer Modern Sans Serif，無襯線體）
- `cmtt`（Computer Modern Typewriter，等寬打字機體）
- `cmmi`（Computer Modern Math Italic，數學斜體）
- `cmsy`（Computer Modern Math Symbols，數學符號）
- `cmex`（Computer Modern Math Extension，數學可變延展符號）

更為關鍵的是，CM 字型族忠實繼承了金屬活字時代的**光學尺寸（Optical Sizing）**傳統。在金屬活字時代，5 磅的活字絕不是 10 磅活字的簡單等比例縮小；若機械縮小，小磅數的細筆畫將在印刷墨暈或視覺感知中徹底斷裂消失，字懷（Counter）也會糊成一片。

高德納在 METAFONT 程式碼中為不同的設計尺寸定義了精細的光學修正參數：
- `cmr5`（5pt）：專用於註腳、角標與複雜分式上下標。其字懷格外開闊，筆畫對比度顯著降低，主幹粗細相對加粗，襯線更加厚實，字面率與字間距均經過大幅放寬；
- `cmr7`（7pt）：專用於一級上下標與圖表標題；
- `cmr10`（10pt）：標準內文字型；
- `cmr12` 與 `cmr17`（12pt 與 17pt）：用於章節目大標題。其細筆畫極其纖細銳利，筆畫對比度極高，字距緊湊緻密，展現出現代體優雅華貴的光學美感。

---

### 1.2 高層介面：基本 $\LaTeX$ 命令與新字型選擇方案 NFSS（The High Level: Basic $\LaTeX$ Commands and NFSS）

在原始 Plain $\TeX$ 中，字型切換是極其原始且僵硬的。使用者只能直接透過底層命令載入具體字型，例如 `\font\tenrm=cmr10`，然後調用 `\tenrm`。這種硬編碼方式將字型族、尺寸、字重緊密綁定在一起；一旦想要將整篇文件內文由 10pt 改為 12pt，或者將內文由 CM 字型替換為 Times，必須對所有底層命令進行地毯式重寫。

為了解決這一工程夢魘，弗蘭克·米特爾巴赫（Frank Mittelbach）與賴納·舍普夫（Rainer Schöpf）於 1989 年為 $\LaTeX$ 設計並引入了**新字型選擇方案（New Font Selection Scheme, NFSS）**（並在 $\LaTeX 2_\varepsilon$ 中升級為 NFSS2）。

#### 經典 $\LaTeX$ 字型切換命令與其語義模型

NFSS 將文字層級的樣式切換抽象為兩套高層介面：
1. **帶參數的作用域文字命令**：如 `\textbf{...}`、`\textit{...}`、`\textsf{...}`、`\textsc{...}`。這類命令不僅限制在局部大括號內生效，而且具備智慧的字型修正功能（例如在斜體末尾自動插入傾斜校正 `\/`）；
2. **狀態宣告命令**：如 `\bfseries`、`\itshape`、`\sffamily`。這類命令會修改當前排版環境的全域狀態機，直到遇到當前組（Group）的閉合括號。

#### NFSS 的五維正交選擇空間

NFSS 的靈魂在於**正交性（Orthogonality）**。它將任何字型的屬性徹底解耦為五個彼此獨立、互不干擾的離散維度：

| 維度 | 參數命令 | 含義與標準取值範例 |
| :--- | :--- | :--- |
| **編碼（Encoding）** | `\fontencoding{...}` | 描述字型槽位映射標準，如 `OT1`, `T1`, `TS1`, `T2A`, `LY1` |
| **字型族（Family）** | `\fontfamily{...}` | 字型家族名稱簡寫，如 `cmr` (Computer Modern Roman), `ptm` (Times), `phv` (Helvetica), `pcr` (Courier) |
| **字重與字寬（Series）** | `\fontseries{...}` | 結合了重量（Weight）與寬度（Width），如 `m` (Medium), `b` (Bold), `bx` (Bold Extended), `c` (Condensed), `bc` (Bold Condensed) |
| **字形（Shape）** | `\fontshape{...}` | 筆畫姿態與變體，如 `n` (Normal 直立), `it` (Italic 義大利斜體), `sl` (Slanted 機械傾斜), `sc` (Small Caps 小型大寫) |
| **尺寸與行距（Size）** | `\fontsize{s}{b}\selectfont` | 物理字號 $s$ 與基線行距 $b$（如 `\fontsize{10pt}{12pt}\selectfont`） |

在 NFSS 狀態機下，若使用者當前處於無襯線體（`\sffamily`），此時執行粗體命令 `\bfseries`，NFSS 只會修改字重維度（`series = b`），而嚴格保留字族維度（`family = sf`），從而得到無襯線粗體，絕不會粗暴地跌回襯線粗體。所有維度的修改必須在調用底層原語 `\selectfont` 時才會被一次性解析為具體字型。

#### 字型定義檔案（`.fd`）與自動替換機制

當五維參數確定後，$\LaTeX$ 如何知道去磁碟載入哪一個實際的 `.tfm` 度量檔案？這一映射規則被固化在以 `<Encoding><Family>.fd` 命名的**字型定義檔案（Font Definition File）**中。

例如，Times 字族在 T1 編碼下的定義檔案為 `t1ptm.fd`，其內部核心語法結構如下：

```latex
\ProvidesFile{t1ptm.fd}[2001/06/04 font definitions for T1/ptm.]

\DeclareFontFamily{T1}{ptm}{}

\DeclareFontShape{T1}{ptm}{m}{n}{
   <-> ptmr8t
}{}
\DeclareFontShape{T1}{ptm}{m}{it}{
   <-> ptmri8t
}{}
\DeclareFontShape{T1}{ptm}{m}{sl}{
   <-> ptmo8t
}{}
\DeclareFontShape{T1}{ptm}{m}{sc}{
   <-> ptmrc8t
}{}
\DeclareFontShape{T1}{ptm}{bx}{n}{
   <-> ptmb8t
}{}
\DeclareFontShape{T1}{ptm}{bx}{it}{
   <-> ptmbi8t
}{}
\DeclareFontShape{T1}{ptm}{b}{n}{<->ssub * ptm/bx/n}{}
\DeclareFontShape{T1}{ptm}{bx}{sl}{<->ssub * ptm/bx/it}{}
```

在 `\DeclareFontShape` 宣告中：
- `<-> ptmr8t` 表示對該字形下的**任意尺寸**，統一映射到底層度量檔案 `ptmr8t.tfm`；
- 如果支援光學尺寸（如 Computer Modern），則可使用離散區間語法進行尺寸分段：
  ```latex
  \DeclareFontShape{OT1}{cmr}{m}{n}{
     <-6> cmr5
     <6-7> cmr6
     <7-8> cmr7
     <8-9> cmr8
     <9-10> cmr9
     <10-12> cmr10
     <12-17> cmr12
     <17-> cmr17
  }{}
  ```
- `<-> ssub * ptm/bx/n`：**靜默替換（Silent Substitution）**機制。當文件請求普通粗體 `ptm/b/n` 而實際字型只提供了展寬粗體 `ptm/bx/n` 時，NFSS 會自動橋接替換而不會中斷排版。

#### NFSS 字型編碼體系全景解析

在 NFSS 問世之前，$\TeX$ 世界的字型編碼極度混亂。隨著國際化排版需求的爆發，$\TeX$ 使用者組（TUG）與歐洲 $\TeX$ 組織共同制定了系統化的標準化字型編碼規範：

1. **OT1（Old $\TeX$ 1，高德納原始 7 位元編碼）**：
   這是 8 位元位元組誕生前 Knuth 為原始 $\TeX$ 設計的 128 字元編碼方案。由於 128 個槽位極其有限，Knuth 做出了若干充滿智慧卻也帶有歷史局限性的折衷：
   - 0–9 槽位被挪用於存放希臘大寫字母（$\Gamma, \Delta, \Theta, \Lambda, \Xi, \Pi, \Sigma, \Upsilon, \Phi, \Psi, \Omega$）；
   - 包含常用的五種經典西文連字：ff (11), fi (12), fl (13), ffi (14), ffl (15)；
   - 包含西班牙語倒問號（¿）與倒嘆號（¡）；
   - **痛點**：OT1 中完全沒有包含西歐語言所需的重音帶符字母（如 é, à, ç, ü）。在 OT1 下，重音字母必須透過 `\accent` 原語在排版執行時動態裝配（將獨立的重音符號疊加在無重音基底字母上方）。這種動態合成不僅在某些縮放倍率下重音位置容易發生微小偏移，更為致命的是：**$\TeX$ 的自動斷字分詞引擎在遇到由動態重音拼裝而成的單詞時會徹底失效**！因為分詞演算法只能處理單一連續的底層字元槽位序列，一旦遇到 `\accent` 切換，當前單詞的斷字分析就會在重音處硬生生被掐斷。

2. **T1（Cork 編碼 / EC 字型）**：
   1990 年在愛爾蘭科克（Cork）舉行的 TUG 大會上正式確立的 8 位元歐洲統一編碼標準（256 個槽位）。
   - T1 編碼將西歐與東歐主要拉丁語系所需的所有帶重音字元（如德語、法語、西班牙語、波蘭語、捷克語、匈牙利語、北歐語系的 ð, þ, æ, ø, å, œ, ß 等）全部固化為**獨立的單個字元槽位**；
   - 徹底解決了歐洲多語言環境下自動斷字與連字元切分的頑疾；
   - 規範了西文引號體系：收錄了法式雙書名引號 Guillemets（« 與 »）以及基線雙低引號（„ 與 “）。

3. **TS1（Text Companion 伴隨符號編碼）**：
   伴隨 T1 編碼誕生的補充符號集（又稱 TC 字型）。由於 256 個字元依然裝不下所有排版輔助符號，TS1 專門用於容納各類非字母文字符號：
   - 貨幣符號全家桶：歐元（€）、英鎊（£）、日圓（¥）、美分（¢）、佛羅林（ƒ）、通用貨幣符號（¤）；
   - 度量與科學符號：攝氏度（℃）、微度（µ）、公制與角分符號；
   - 預製通用分數（¼, ½, ¾）與上標數字（¹²³）；
   - 標點符號變體：長破折號、雙破折號、項目符號圓點（Bullet）等。

4. **T2 系列與 X2（西里爾字母全景體系）**：
   西里爾字母體系涉及俄語、白俄羅斯語、烏克蘭語、塞爾維亞語、馬其頓語、保加利亞語以及中亞數十種前蘇聯少數民族語言，字元變體多達百餘種，絕無可能塞進單一的 256 字元表中。為此，T2 委員會將其嚴密拆解為互補的四大子編碼：
   - **T2A**：覆蓋俄語、白俄羅斯語及大部分斯拉夫西里爾語言；
   - **T2B**：覆蓋烏克蘭語及若干少數民族西里爾語言；
   - **T2C**：覆蓋高加索與西伯利亞地區的非斯拉夫語言西里爾文字；
   - **T2D**：覆蓋中亞非斯拉夫語言（如哈薩克語、塔吉克語變體）；
   - **X2**：容納所有歷史古西里爾字母與極罕見變體符號。

5. **其他專用區域編碼**：
   - **T3**：國際音標（IPA）專用編碼；
   - **T4**：非洲拉丁字母體系（包含加納語、奈及利亞語等所需的特殊舌根輔音字母）；
   - **T5**：越南語專用編碼（越南語擁有多達 5 種聲調與獨特的觸角元音 ơ, ư，聲調與觸角還會產生複合雙重疊置，必須依賴專用編碼矩陣）；
   - **LY1（TeX 'n' ANSI / Y&Y 編碼）**：商業排版巨頭 Y&Y 公司制定的 8 位元編碼，高度相容 Windows ANSI (CP1252) 標準，在商業 PostScript 印刷出版中曾廣為流行。

#### 數學字型與微觀符號的 NFSS 機制

$\TeX$ 最引以為傲的成就在於其無與倫比的複雜數學公式排版能力。然而，在底層實現上，數學排版與文字排版有著天壤之別：
- 在數學模式下，單個字母代表的是數學變數，它們必須使用具有特殊傾斜角度與側邊留白的數學斜體（Math Italic）；
- 行間數學公式需要無級縮放的大型括號、中括號、花括號、積分號（$\int$）與求和號（$\sum$）；
- 傳統 $\TeX$ 引擎內部存在一個**極度嚴苛的硬體級硬性約束：至多只能同時載入 16 個數學字型家族（Math Families, 編號 0 至 15）**！每一個數學符號在底層被編碼為一個三元組 `(family, class, position)`。

NFSS 透過高度抽象的巨集命令對這 16 個有限的數學家族進行統一排程：
- `\DeclareMathAlphabet{\mathbf}{OT1}{cmr}{bx}{n}`：宣告數學字母表；
- `\DeclareSymbolFont{letters}{OML}{cmm}{m}{it}`：宣告符號字型家族；
- `\DeclareMathSymbol{\alpha}{\mathord}{letters}{"0B}`：將數學符號與其具體的家族及槽位精準錨定。

數學公式中的大型變長定界符（Delimiters）則依賴底層的**可延伸字元裝配機制**：當定界符需要隨公式高度無限伸展時，$\TeX$ 會調用 `cmex10` 字型中的頂部零件（Top）、底部零件（Bottom）、中間連接件（Mid）以及可重複鋪設的垂直連接段（Extender），像拼接水管一樣拼裝出任意高度的完美大括號！

---

### 1.3 底層機制：$\TeX$ 引擎與 DVI 位元組碼格式（The Low Level: $\TeX$ and DVI）

當使用者在命令行執行 `latex document.tex` 時，$\TeX$ 引擎內部究竟發生了什麼？$\TeX$ 並不會直接輸出 PDF，更不會直接操縱印表機硬體。它的輸出是一份精簡至極的二進位中間檔案——**DVI（Device Independent，設備無關檔案）**。

#### DVI 虛擬機的內部結構與暫存器狀態機

DVI 檔案格式在本質上是一份極其純粹的**虛擬機位元組碼指令流**。DVI 虛擬機維護著一個嚴密的幾何狀態機，包含六個核心內部暫存器：

$$h, v, w, x, y, z$$

- $h$：當前筆刷在頁面上的**水平座標**（從左側參考點向右度量）；
- $v$：當前筆刷在頁面上的**垂直座標**（從頂部參考點向下度量）；
- $w, x$：水平方向的當前步長記憶暫存器；
- $y, z$：垂直方向的當前步長記憶暫存器。

此外，DVI 虛擬機配備了一個**座標堆疊（Coordinate Stack）**，支援透過 `push` 指令將當前 $(h, v, w, x, y, z)$ 完整壓入堆疊保存，並在完成局部複雜排版（如上下標或盒子組裝）後透過 `pop` 指令瞬間恢復母座標系。

#### DVI 核心位元組碼指令全集

DVI 位元組碼指令極其緊湊，主要分為以下幾大類別：

1. **字元設置與列印指令**：
   - `set_char_0` 至 `set_char_127`（單位元組操作碼 0–127）：列印字元編號 $c$ 並使水平座標 $h$ 自動向前遞增該字元的寬度 $w(c)$；
   - `set1` 至 `set4`：後跟 1 至 4 位元組的字元槽位編號，用於列印大字元集的字元並自動前進；
   - `put1` 至 `put4`：列印指定字元，但**不移動水平座標 $h$**（常用於重音疊加或多字元就地重合）。

2. **幾何實線繪製指令**：
   - `set_rule`：後跟規則的高度 $a$ 與寬度 $b$，在當前座標 $(h, v)$ 處繪製一個實心黑矩形，並將 $h$ 前移 $b$；
   - `put_rule`：繪製矩形但不改變 $h$。

3. **座標位移指令**：
   - `right1..4`：水平向右移動指定距離（若為負數則向左移）；
   - `down1..4`：垂直向下移動指定距離（若為負數則向上移）；
   - `w0`, `w1..4`, `x0`, `x1..4`：帶暫存器記憶的水平相對位移；
   - `y0`, `y1..4`, `z0`, `z1..4`：帶暫存器記憶的垂直相對位移。

4. **字型選擇與定義指令**：
   - `fnt_num_0` 至 `fnt_num_63`（操作碼 171–234）：單位元組快速切換當前活動字型編號；
   - `fnt1..4`：切換任意編號的活動字型；
   - `fnt_def1..4`：宣告字型元數據，緊隨五個關鍵參數：
     1. 字型內部數字索引；
     2. 字型校驗和（Checksum，必須與底層 `.tfm` 檔案頭嚴格一致）；
     3. 縮放尺寸（Actual Size，以 `sp` 為單位）；
     4. 光學設計尺寸（Optical Design Size，以 `sp` 為單位）；
     5. 字型名稱字串（不含 `.tfm` 後綴）。

5. **頁面結構與檔案導言指令**：
   - `bop`（Begin of Page）：頁面起始標誌，後跟 10 個計數暫存器（用於定位頁碼）以及指向上一頁 `bop` 的反向指標（使得 DVI 閱讀器能夠閃電般地逆向翻頁瀏覽）；
   - `eop`（End of Page）：當前頁面排版終結，強制清空堆疊；
   - `pre`（Preamble）：檔案起始導言，記錄 DVI 格式版本號及單位縮放比例因子；
   - `post`（Postamble）：後置導言，位於所有排版頁面之後，彙總全域頁面總數、最大堆疊深度、以及整篇文件所用到的所有 `fnt_def` 字型定義列表；
   - `post_post`：位於檔案絕對末尾，記錄指向 `post` 的物理偏移指標，並在最後填補至少四個操作碼 223（Hex `DF`）位元組。

#### 純整數定點運算機制：縮放點單位 `sp`

Knuth 在設計 DVI 格式時確立了一條鐵律：**DVI 檔案在任何硬體架構、任何作業系統上必須輸出像素級絕對一致的結果**。為了徹底消滅不同 CPU 在浮點數運算（IEEE 754 浮點捨入誤差）上的微小精度漂移，$\TeX$ 與 DVI 內部的所有幾何距離**全部採用純 32 位元有符號整數進行定點算術運算**！

其最基礎的度量單位被稱為**縮放點（Scaled Point, `sp`）**：

$$1\text{ pt} = 65,536\text{ sp} = 2^{16}\text{ sp}$$

由於 1 美制印刷磅（pt）約等於 $1/72.27$ 英吋，1 個 `sp` 的物理跨度僅為：

$$1\text{ sp} \approx 5.363 \times 10^{-6}\text{ mm} = 5.363\text{ 奈米 (nm)}$$

這一極度微小的度量粒度遠小於可見光的波長，更遠超任何高精度工業雷射照排機的物理解析度。在整篇文件排版過程中，所有的字框寬度累加、字距微調與膠水拉伸完全在純整數空間內進行加減乘除，杜絕了任何累積捨入誤差。

#### DVI 位元組碼的反彙編透視：DVX 格式

為了直觀觀察 DVI 的位元組碼流，我們借助 Haralambous 開發的 `dvi2dvx` 工具將一段編譯後的二進位 DVI 切片轉換為 XML 文字表述（DVX）：

```xml
<fontdef id="18" checksum="20786036" scale="655360" designsize="655360" name="T1lemondemn"/>
<font id="18"/>
<set>the</set>
<right dim="167112"/>
<set>te</set>
<right dim="-14745"/>
<set>xt</set>
<right dim="167112"/>
<set>tha</set>
<right dim="-18350"/>
<set>t</set>
<right dim="167112"/>
<set>y</set>
<right dim="-11141"/>
<set>ou</set>
<right dim="167112"/>
<set>ar</set>
<right dim="-7864"/>
<set>e</set>
<right dim="167112"/>
<set>curr</set>
<right dim="-9830"/>
<set>ently</set>
<right dim="167112"/>
<set>r</set>
<right dim="-13107"/>
<set>eading</set>
```

在這段真實的剖析片段中：
1. `T1lemondemn` 字型（Le Monde Livre 字族的正體，T1 編碼）被宣告為內部編號 18，縮放尺寸為 655,360 `sp`（即精確的 10pt）；
2. 詞間空格透過 `<right dim="167112"/>` 實現（167,112 `sp` 約等於 2.55pt，這是該字型在當前行計算出的詞間彈性膠水展開量）；
3. 單詞內部的字母組合之間出現了負向的 `<right dim="-..."/>`（例如在 "t" 與 "e" 之間收緊 14,745 `sp`，在 "a" 與 "t" 之間收緊 18,350 `sp`）。這表明：**$\TeX$ 在將段落寫入 DVI 時，已經將字偶間距調整（Kerning）全部計算完畢並直接硬編碼為物理座標微調**！

#### 字元盒子與物理墨跡的徹底解耦

這一底層機制揭示了 $\TeX$ 最精妙的架構哲學：**$\TeX$ 內部根本沒有字形（Glyphs），只有幾何盒子（Boxes）**。
- $\TeX$ 引擎只負責計算盒子在哪裡擺放；
- DVI 檔案中只記載哪個位置放哪個字元編號；
- 字元究竟長什麼樣？是由黑白像素構成的點陣位圖，還是由三次貝塞爾曲線構成的向量輪廓？$\TeX$ 完全不知情，也根本不需要知情！
- 真實的物理光柵化與墨跡繪製工作，被徹底推遲到了編譯流水線的後處理環節——由專門的**設備驅動程式（DVI Drivers）**來接管並直面物理世界。

---

### 1.4 後 $\TeX$ 時代：直面物理輸出與真實世界（“Après-$\TeX$”: Confronting the Real World）

當 DVI 檔案離開 $\TeX$ 的象牙塔後，必須直面複雜的物理設備生態。負責將 DVI 解析並轉化為印刷品或顯示圖像的軟體被稱為 DVI 驅動程式，其中最著名的代表是托馬斯·羅基茨基（Tomas Rokicki）開發的 `dvips`，以及後來由韓國學者朝真（Cho Jin-Hwan）與 Hirata 擴展的 `dvipdfmx`。

#### `kpathsea` 檔案路徑檢索子系統與動態點陣生成鏈

在現代 $\TeX$ 發行版（如 TeX Live 與 MacTeX）中，所有命令行工具的底層都整合了卡爾·貝里（Karl Berry）開發的 `kpathsea` 動態路徑檢索庫。

當 `dvips` 讀取 DVI 檔案並遇到一個名為 `cmr10` 的字型請求時，`kpathsea` 會啟動三級自動化檔案尋訪與生成流水線：
1. **`mktextfm`**：若系統中缺失該字型的度量檔案 `cmr10.tfm`，自動在背景觸發生成該 TFM；
2. **`mktexmf`**：若缺少對應的 METAFONT 原始碼 `cmr10.mf`，自動嘗試從通用母版或參數包中動態拼裝出原始碼；
3. **`mktexpk`**：若需要點陣光柵化渲染，`mktexpk` 會根據目標輸出設備的具體物理解析度（如 600 DPI）與驅動模式（如惠普雷射印表機模式 `ljfour`），自動調用 METAFONT 編譯引擎生成對應的壓縮點陣字型檔案 `cmr10.600pk`。

#### `dvips` 對 PostScript Type 1 字型的解析與映射機制

隨著桌面出版徹底倒向向量時代，基於 METAFONT 的 PK 點陣字型已不再適應螢幕縮放與高階雷射照排的需求。印刷工業全面採用了由 Adobe 制定的 PostScript Type 1 向量字型標準。

由於 DVI 檔案中僅記載著 TFM 檔案的名稱（如 `ptmr8t`），`dvips` 必須依據一套嚴密的映射資料庫——**`psfonts.map`**（或現代的 `pdftex.map`）來決定如何翻譯每一個字型條目。

一條典型的 `psfonts.map` 映射條目如下所示：

```text
ptmr8t Times-Roman " T1Encoding ReEncodeFont " <[T1-WGL4.enc <ptmr8a.pfb
```

這條配置包含了驅動程式完成向量排版所需的全部密碼：
- `ptmr8t`：DVI 檔案中所引用的 TFM 邏輯名稱；
- `Times-Roman`：PostScript 直譯器內部識別的標準 PostScript 字型名稱（FontName）；
- `" T1Encoding ReEncodeFont "`：一段在 PostScript 直譯器中即時執行的 PostScript 程式碼片段，指示直譯器使用隨後的編碼向量對字型的字元字典進行就地重新索引（Re-encoding）；
- `<[T1-WGL4.enc`：指示 `dvips` 讀取外部編碼向量檔案 `T1-WGL4.enc` 並將其作為陣列載入 PostScript 資料流；
- `<ptmr8a.pfb`：指示 `dvips` 打開磁碟上的二進位 Type 1 字型檔案 `ptmr8a.pfb`，將其內容完整內嵌（Embed）到最終生成的 `.ps` 列印檔案中；如果該欄位為空，則表明該字型屬於印表機 ROM 中內建的核心字型（Resident Font），驅動程式將只生成調用指令而不內嵌輪廓數據。

#### `pdftex` 的革命性演進與微觀排版（Micro-typography）

1996 年，捷克布爾諾馬薩里克大學的博士生韓越康（Hàn Thế Thành）推出了改變 $\TeX$ 歷史進程的引擎——**`pdftex`**。

`pdftex` 徹底顛覆了「$\TeX \to$ DVI $\to$ PostScript $\to$ Distiller $\to$ PDF」的傳統冗長流水線，直接在 $\TeX$ 引擎內部整合了 PDF 向量生成器與 Type 1 / TrueType 字型解析器。更為震撼的是，Thành 在 `pdftex` 中首次在軟體工程層面實現了赫爾曼·察普夫（Hermann Zapf）夢寐以求的現代排版兩大頂峰演算法：

1. **字元邊緣凸出（Character Protrusion / Margin Kerning）**：
   在純幾何排版中，若一行以標點符號（如逗號、句號、引號、連字元）或具有大角度外傾筆畫的字母（如大寫「A」, 「V」, 「W」）作為行首或行尾，由於這些字元的空白面積較大，會導致文字塊在視覺感知上出現參差不齊的凹陷。`pdftex` 允許根據每個字元的光學權重，將標點符號與特定字母的邊緣**微量懸掛凸出到排版邊框邊界線之外**（通常為字元寬度的 20% 至 70%），從而在人眼視覺感知中塑造出如刀削般筆直完美的段落邊緣！

2. **字型橫向微伸縮（Font Expansion / hz-algorithm）**：
   傳統斷行演算法僅能調節單詞之間的詞間膠水（Glue）。當某行單詞較長時，僅拉伸詞間距往往造成難以容忍的巨大縫隙（視覺「白溪」或「河流」）。察普夫與 Thành 提出的 hz 演算法允許 $\TeX$ 在進行全域斷行評估時，**對整行中所有字元的字型輪廓進行極微量的橫向幾何縮放**（通常在 $\pm 1\%$ 至 $\pm 2\%$ 之間微調）。這種極細微的變形在人眼視覺下完全無法察覺任何字形失真，卻為動態規劃斷行演算法提供了極其寬廣的數學解空間，使斷行不良度（Badness）與連字元斷字概率斷崖式下降，排版灰度達到了空前絕後的均勻與緻密。

---

## 2. 為 $\TeX$ 安裝新字型（Installing Fonts for $\TeX$）

### 2.1 $\TeX$ 目錄結構（TDS）規範

將外部商業字型安裝到 $\TeX$ 系統絕非隨意將檔案扔進某個目錄。現代 $\TeX$ 系統遵循嚴格的**$\TeX$ 目錄結構標準（$\TeX$ Directory Structure, TDS）**。對於任意字型包，其內部構件必須精確歸位至系統本地樹（如 `TEXMFLOCAL`）：

- `fonts/afm/<supplier>/<typeface>/`：存放 Adobe 原始度量檔案（`.afm`）；
- `fonts/type1/<supplier>/<typeface>/`：存放 PostScript Type 1 輪廓檔案（`.pfb` / `.pfa`）；
- `fonts/truetype/<supplier>/<typeface>/`：存放 TrueType 輪廓檔案（`.ttf`）；
- `fonts/opentype/<supplier>/<typeface>/`：存放 OpenType 輪廓檔案（`.otf`）；
- `fonts/tfm/<supplier>/<typeface>/`：存放 $\TeX$ 專用底層度量檔案（`.tfm`）；
- `fonts/vf/<supplier>/<typeface>/`：存放虛擬字型檔案（`.vf`）；
- `fonts/map/dvips/<typeface>/`：存放驅動映射檔案（`.map`）；
- `tex/latex/<typeface>/`：存放 $\LaTeX$ 字型定義巨集檔案（`.fd` 與 `.sty`）。

歸檔完成後，必須在終端機執行 `mktexlsr`（或 `texhash`）以重建 `ls-R` 路徑雜湊索引資料庫，確保 `kpathsea` 能夠在毫秒級定位檔案。

---

### 2.2 快速工具：`afm2tfm` 深度運用

對於普通西文字型的快速整合，系統提供了一個短小精悍的 C 語言命令行工具——**`afm2tfm`**。

#### 底層幾何變換與命令行參數

`afm2tfm` 能夠直接解析標準 AFM 檔案中的字元包圍盒與字偶間距表，並生成 $\TeX$ 核心所需的 TFM 檔案：

```bash
afm2tfm CentaurMT.afm -v t1centaurmn.vpl -T EC.enc
```

其關鍵高級控制參數具有深厚的幾何意義：
- **`-s slant`（仿斜體變換）**：
  若某款字型只有正體而缺乏義大利斜體，可透過 `-s` 施加仿斜切變換。其變換矩陣對應於剪切形變：
  $$\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} 1 & \text{slant} \\ 0 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}$$
  通常傳入參數如 `-s 0.167`（對應約 $9.5^\circ$ 的向右傾角，$\text{slant} = \tan \theta$）。
- **`-d extend`（展寬/壓縮變換）**：
  對字型沿水平 $x$ 軸施加縮放比例因子（如 `-d 0.85` 為緊縮體，`-d 1.15` 為展寬體）。
- **`-T encoding_file`**：
  指定目標重編碼向量（如 `EC.enc` 對應 T1 編碼，`8r.enc` 對應 TeXBase1 編碼）。
- **`-v vpl_file`**：
  指示生成虛擬屬性列表（Virtual Property List, `.vpl`）檔案，從而允許在更高層級拼裝複合虛擬字型。

`afm2tfm` 在控制台輸出的映射字串，可直接追加到 `psfonts.map` 中：

```text
CentaurMT CentaurMT " ECEncoding ReEncodeFont " <[EC.enc <CentaMT.pfb
```

隨後調用 `vptovf` 實用程式將文字格式的 `.vpl` 檔案組裝為最終的二進位 `.vf` 與 `.tfm` 檔案：

```bash
vptovf t1centaurmn.vpl t1centaurmn.vf t1centaurmn.tfm
```

---

### 2.3 工業級字型安裝利器：`fontinst` 體系

雖然 `afm2tfm` 足以應對單一字型的簡單轉換，但在面對龐大的商業專家級字型族時，它就顯得力不從心了。

商業專業字型（如 Adobe Garamond Premier Pro、Monotype Dante 等）往往拆分為若干互補的子字型檔案：
- 常規文字字型（包含常規大寫字母、小寫字母與基本標點）；
- 專家集字型（Expert Set, `.sc` / `.exp`，包含真正設計的小型大寫字母、全套舊體數字 Oldstyle Figures、分數符、修飾花體）；
- 替換字形字型（包含連字 `ct`, `st`, `ffi`, `ffl`，重音大寫字母等）。

$\LaTeX$ 的 NFSS 規範要求：**同一個字形組合（如小型大寫字母 `\textsc`）必須在一個統一的編碼方案內無縫呈現**。如果使用 `afm2tfm`，使用者將無法讓大寫字母與來自另一個檔案的小型大寫字母以及來自常規檔案的標點符號協同工作。

為了徹底打通這一複雜鴻溝，艾倫·傑弗里（Alan Jeffrey）、羅蘭·霍爾茨（Rowland McDonnell）與烏爾里克·迪爾克（Ulrik Vieth）共同研發了 $\TeX$ 歷史上最強悍的字型安裝基礎設施——**`fontinst` 巨集套件**。

#### `fontinst` 的四步流水線架構

`fontinst` 並非獨立編譯的二進位程式，而是**完全使用 $\TeX$ 巨集語言寫成的高階巨集套件系統**！它利用 $\TeX$ 自身的巨型計算引擎來操縱度量數據。

其標準處理流水線如下：

```
[原始 AFM 檔案] 
      │ (透過 \transformfont 轉換)
      ▼
[MTX 度量檔案] (包含 \setglyph, \setglyphdim 等純文字度量指令)
      │
      ├───────────────────────┐
      ▼                       ▼
[ETX 編碼目標檔案]      [使用者自定義規則腳本]
      │                       │
      └───────────┬───────────┘
                  │ (透過 \installfont 編譯合成)
                  ▼
         [VPL 虛擬屬性列表] + [PL 屬性列表]
                  │
      ┌───────────┴───────────┐
      ▼ (調用 vptovf)          ▼ (調用 pltotf)
[VF 虛擬字型檔案]        [TFM 度量檔案] + [.fd 巨集套件定義檔案]
```

#### 標準安裝驅動腳本剖析

使用者只需編寫一個簡短的驅動檔案（如 `install-centaur.tex`）：

```latex
\input fontinst.sty

\needsfontinstversion{1.926}

\recordtransforms{centaur-rec.tex}

\transformfont{rcen8r}{\reencodefont{8r}{\fromafm{CentaurMT}}}
\transformfont{rceni8r}{\reencodefont{8r}{\fromafm{CentaurMT-Italic}}}
\transformfont{rcenb8r}{\reencodefont{8r}{\fromafm{CentaurMT-Bold}}}
\transformfont{rcenbi8r}{\reencodefont{8r}{\fromafm{CentaurMT-BoldItalic}}}

\installfonts

\installfamily{T1}{centaur}{}

\installfont{rcen8t}{rcen8r,latin}{t1}{T1}{centaur}{m}{n}{}
\installfont{rceni8t}{rceni8r,latin}{t1}{T1}{centaur}{m}{it}{}
\installfont{rcenb8t}{rcenb8r,latin}{t1}{T1}{centaur}{bx}{n}{}
\installfont{rcenbi8t}{rcenbi8r,latin}{t1}{T1}{centaur}{bx}{it}{}
\installfont{rcenc8t}{rcen8r,latin}{t1c}{T1}{centaur}{m}{sc}{}
\installfont{rceno8t}{rcen8r,latin}{t1j}{T1}{centaur}{m}{ol}{}

\endinstallfonts

\endrecordtransforms
\bye
```

執行 `tex install-centaur.tex` 後：
1. `fontinst` 自動解析 AFM，將字形映射到 TeXBase1 (8r) 基礎度量空間；
2. 引入 `latin.mtx` 標準度量變換庫，計算所有複合重音字母的裝配間距；
3. 根據目標編碼 `t1.etx`，自動生成完整的虛擬字型定義；
4. 自動合成並輸出規範的 `t1centaur.fd` 巨集套件，無需人工干預即可在 $\LaTeX$ 中直接透過 `\fontfamily{centaur}\selectfont` 進行排版！

---

### 2.4 多重母版字型（Multiple Master Fonts）在 $\TeX$ 中的實現

在 20 世紀 90 年代，Adobe 推出了劃時代的向量字型格式——**多重母版字型（Multiple Master, MM）**。MM 字型允許在同一個字型檔案內部定義多個連續的設計軸（Design Axes），最常見的三大設計軸為：
1. **字重軸（Weight）**：從超細（Extra Light，如數值 300）到極粗（Black，如數值 800）連續漸變；
2. **字寬軸（Width）**：從特緊縮（Condensed，如數值 450）到特展寬（Expanded，如數值 850）連續漸變；
3. **光學尺寸軸（Optical Size）**：從內文字型（6pt）到大標題（72pt）連續漸變。

#### 連續設計軸與 $\TeX$ 離散體系的衝突

理論上，如果 $\TeX$ 能夠動態操縱 Multiple Master 字型，排版學者可以實現許多震撼的排版特效：
- 例如依據當前行排版的充盈度，動態微調整行字元的寬度軸，從而消除連字元；
- 或者透過微調字重與光學尺寸，使得一本書的排版版面精準契合 16 頁印張（Signature）的整數倍！

然而，$\TeX$ 誕生的哲學是基於不可變離散度量檔案（TFM）的確定性排版，無法直接接入執行時的多維參數插值引擎。此外，Adobe 後來全面轉向 OpenType，並官方放棄了 MM 格式。

#### 利用 LCDF Typetools 進行切片固化

在 $\TeX$ 或 $\Omega$ 中使用 MM 字型的唯一現實路徑是：**預先透過插值工具從連續設計空間中「切片提取」出特定的離散實例（Instances），並將其偽裝為標準的 PostScript Type 1 字型交付 $\TeX$ 使用**。

埃迪·科勒（Eddie Kohler）編寫的開源工具集 **LCDF Typetools** 中的 `mmafm` 與 `mmpfb` 提供了這一工業級能力：

```bash
mmafm --weight=380 --width=460 --optical-size=6 MinionMM.amfm > minion_380_460_6.afm
mmpfb --weight=380 --width=460 --optical-size=6 MinionMM.pfb  > minion_380_460_6.pfb
```

上述命令指示插值引擎在 Minion MM 字型的三維空間中精確定位座標點 `(weight=380, width=460, optical_size=6)`，並計算出該點處所有三次貝塞爾控制點與字元度量的物理數值，分別生成對應的單體 `.afm` 與 `.pfb` 檔案。

生成的字型在 `dvips` 中的映射配置如下：

```text
minion_380_460_6 Minion_M_380_460_6_ " ECEncoding ReEncodeFont " <EC.enc <minion_380_460_6.pfb
```

從此，該實例便可完全作為一個常規的單體 Type 1 字型，透過標準的 `fontinst` 流程無縫編織進 NFSS 體系。

---

## 3. 按使用者需求深度定制 $\TeX$ 字型（Customizing $\TeX$ Fonts for the User's Needs）

### 3.1 虛擬字型（Virtual Fonts）的體系架構與設計哲學

虛擬字型（Virtual Font, VF）是高德納與戴維·福斯（David Fuchs）在 1989 年引入 $\TeX$ 世界的最具革命性的軟體工程創造之一。

#### 虛擬字型與真實字型的本質分野

在底層物理意義上，真實字型（Real Font，如 PK 點陣字型、Type 1 PFB、TrueType TTF）是**字形輪廓或像素數據的最終提供者**。

而虛擬字型（`.vf` 檔案配合 `.tfm`）在本質上是**一份寄生於 DVI 虛擬機上層的高度結構化的「巨集重定向規則庫」**：
- 當 $\TeX$ 編譯文件時，它讀取虛擬字型的 `.tfm`，認為自己在用一款具有確定高度、寬度與深度的常規字型；
- 當 DVI 驅動程式（如 `dvips`）解析 DVI 檔案遇到該虛擬字型的字元設置指令時，驅動程式會攔截該指令，並在其內部展開為一段包含若干條基礎 DVI 原語的子指令序列！

#### 虛擬字元展開的無限可能性

在虛擬字型的內部指令塊中，排版師擁有操縱 DVI 虛擬機的全部特權：
- **字形替換與跨字型引用**：字元槽位可以直接指向另一個真實字型的特定槽位，甚至從十個不同的字型檔案中各借調一部分字元組裝成一個虛擬字型；
- **幾何移動與重疊合成**：可以發出任意 `right` 與 `down` 移動指令，將一個獨立的重音符號精準疊加在某個大寫字母的正上方；
- **遞迴嵌套**：虛擬字型可以透明地調用另一款虛擬字型；
- **繪製複雜規則與外部內嵌程式碼**：甚至可以在單個字元槽位內注入一段 PostScript 特效程式碼（如為字元添加陰影、旋轉、下劃線、繪製花邊）。

最為關鍵的是：**在 DVI 格式規範內，驅動程式完全負責虛擬字型的遞迴展開，外部巨集套件與 $\TeX$ 排版引擎完全感受不到虛擬字型的存在**。這使得排版系統在保留絕對確定性的同時，獲得了近乎無限的結構擴展能力。

---

### 3.2 ETX 與 MTX 檔案的高級語法與數據模型

在 `fontinst` 體系中，虛擬字型被嚴格解構為兩個核心檔案：**編碼模板檔案（`.etx`）**與**度量計算檔案（`.mtx`）**。

#### ETX（Encoding $\TeX$）檔案的語法架構

`.etx` 檔案定義了目標字型中每個槽位的排版語義。其核心語法形式如下：

```latex
\relax
\encoding

\setslot{A}
   \comment{The letter A.}
\endsetslot

\setslot{f_i}
   \comment{The ligature fi.}
\endsetslot

\setslot{f}
   \ligature{LIG}{i}{f_i}
   \ligature{LIG}{f}{f_f}
   \ligature{LIG}{l}{f_l}
\endsetslot
```

在 `\setslot` 塊內，最精妙的機制在於**連字控制命令 `\ligature`**。$\TeX$ 內部的連字與字距機在底層支援極其複雜的四種狀態轉移機制：

1. **`LIG`（經典全替換連字）**：
   $$A + B \to C$$
   吞噬輸入字元 $A$ 與 $B$，直接輸出複合連字 $C$（如 $f + i \to fi$）；
2. **`/LIG`（後向保留連字 / Post-ligature）**：
   $$A + B \to A + C$$
   保留首個字元 $A$，將後續字元 $B$ 替換為特定形態 $C$；
3. **`LIG/`（前向保留連字 / Pre-ligature）**：
   $$A + B \to C + B$$
   將首個字元 $A$ 替換為變體形態 $C$，但保留後續字元 $B$；
4. **`/LIG/`（雙向保留連字 / Contextual ligature）**：
   $$A + B \to A + C + B$$
   保留兩端字元，僅在中間動態注入連接構件；
5. **`/LIG/>` 與 `LIG/>`（步進狀態機連字）**：
   控制內部指標在完成替換後跳過若干字元，防止狀態機陷入死循環。

#### MTX（Metrics $\TeX$）檔案的語法架構

`.mtx` 檔案則負責具體的字元物理幾何與合成工程。其核心原語構架包括：

- **`\setglyph{glyph_name} ... \endsetglyph`**：宣告一個新字形；
- **`\glyph{source_name}{scale}`**：從源字型中提取指定字形並按比例縮放（$1000$ 表示 $100\%$）；
- **`\movert{dimension}` 與 `\moveup{dimension}`**：在局部笛卡爾座標系中相對平移筆刷原點；
- **`\installglyph{glyph_name}{etx_name}{commands}`**：高階複合字形裝配指令；
- **字距微調繼承（Kerning Inheritance）**：
  ```latex
  \setleftkerning{Eacute}{E}{1000}
  \setrightkerning{Eacute}{E}{1000}
  \setleftrightkerning{Ecircumflex}{E}{1000}
  ```
  上述指令指示度量引擎：帶尖音符的 `Eacute` 在左側與右側的字距微調行為，與母體字母 `E` 嚴格保持 $100\%$（$1000/1000$）一致，排版師無需為數百個帶重音字母手動重複定義成千上萬個字偶間距！

---

### 3.3 實戰應用範例全解

#### 範例一：偽小型大寫字母（Fake Small Capitals）的精確合成

小型大寫字母（Small Capitals）是西文專業排版中不可或缺的元素，常用於縮寫詞（如 NASA, UNESCO）、人名以及章節首行。如果一款商用字型未附帶專門設計的原生小型大寫字母（`Expert Set`），直接使用大寫字母縮小往往導致筆畫過於纖細弱小，在視覺灰度上產生刺眼的蒼白感。

借助 `fontinst`，排版師可以編寫高階演算法自動合成高品質的偽小型大寫字母：

```latex
\setint{smallcapsscale}{800}
\setint{smallcapskerning}{900}

\installglyph{Asmall}{A}{
   \glyph{A}{\int{smallcapsscale}}
   \movert{\int{smallcapskerning}}
}
```

在合成程式碼中：
1. 將大寫字母 `A` 的輪廓統一等比縮放至 $80\%$（高度接近 x 高度）；
2. 由於等比縮放後字元筆畫相對變細，且原大寫字母的側邊留白被成比例縮小，導致字元在排版時顯得過於擁擠。程式碼透過 `\movert{\int{smallcapskerning}}` 顯式增加額外的側邊字距微調，使偽小型大寫字母在文字行中展現出更加均衡穩定的排版灰度。

#### 範例二：為西歐文字增補定制連字（Adding Ligatures to a Font）

法語出版界擁有一批經典的尊稱縮寫歷史習慣，例如：
- 稱呼未婚女性的「Mademoiselle」（小姐）在傳統法文排版中必須書寫為帶有下劃修飾或緊湊連字的「$\text{M}^{\text{lle}}$」；
- 稱呼已婚女士的「Madame」（夫人）書寫為「$\text{M}^{\text{me}}$」；
- 荷蘭語中的雙字母連綴「ij」與「uw」。

若字型中未內嵌這些專用連字，`fontinst` 允許透過連字樹進行智慧構造：

```latex
\setslot{M}
   \ligature{LIG}{l}{M_l}
\endsetslot

\setslot{M_l}
   \comment{(False) intermediate ligature Ml}
   \ligature{LIG}{l}{M_l_l}
\endsetslot

\setslot{M_l_l}
   \comment{(False) intermediate ligature Mll}
   \ligature{LIG}{e}{M_l_l_e}
\endsetslot

\setslot{M_l_l_e}
   \comment{Real final ligature Mlle}
\endsetslot
```

在 MTX 檔案中，複合字形 `M_l_l_e` 的裝配邏輯如下：

```latex
\installglyph{M_l_l_e}{M_l_l_e}{
   \glyph{M}{1000}
   \movert{\kerning{M}{l}}
   \moveup{300}
   \glyph{l}{650}
   \movert{-50}
   \glyph{l}{650}
   \movert{-50}
   \glyph{e}{650}
}
\setleftkerning{M_l_l_e}{M}{1000}
\setrightkerning{M_l_l_e}{e}{1000}
```

當排版引擎讀取文字流遇到連續的 `M-l-l-e` 四個字元時，$\TeX$ 內部的有限狀態機將沿連字樹步步推進：$M+l \to M_l$；$M_l+l \to M_{ll}$；$M_{ll}+e \to M^{lle}$！這一連綴變換過程對終端使用者完全透明，文件作者只需輸入常規字串 `Mlle`，編譯後即可自動呈現出精雕細琢的古典縮寫連字！

#### 範例三：基於 8 位元虛擬字型實現阿拉伯文上下文連綴分析（Contextual Analysis in Arabic）

阿拉伯文字是典型的草書連綴書寫系統。同一個阿拉伯字母在單詞的不同位置，其筆畫形態會發生顛覆性的劇烈改變：
1. **孤立態（Isolated Form）**：當字元前後均無連綴時；
2. **詞首態（Initial Form）**：當字元與後續字母相連時；
3. **詞中態（Medial Form）**：當字元同時與前後字母相連時；
4. **詞尾態（Final Form）**：當字元僅與前序字母相連時。

在現代系統（如 OpenType 與 HarfBuzz）誕生前，傳統 $\TeX$ 引擎被普遍認為絕對不可能排版阿拉伯文，因為 8 位元 $\TeX$ 完全缺乏上下文敏感替換機制。

然而，Haralambous 在本章中揭示了一個令世人驚嘆的技術創舉：**完全利用 $\TeX$ 底層的 `\ligature` 狀態機指令網路，在純 8 位元虛擬字型中硬生生模擬出了阿拉伯文的上下文連綴引擎**！

其核心機理是引入虛擬的不可見「前驅探測符」與「後繼邊界符」：
- 當一個字母遇到左連綴條件時，觸發 `/LIG` 連字指令將自身重寫為詞首態；
- 若後續字元持續連綴，則觸發 `/LIG/` 雙向連字持續鎖定在詞中態；
- 一旦遇到空格、標點符號或詞尾邊界符，立即觸發終結連字跌入詞尾態或孤立態：

```latex
\setslot{ghayn.init}
   \ligature{/LIG}{ghayn.medi}{ghayn.medi}
   \ligature{/LIG}{dal.fina}{dal.isol}
\endsetslot

\setslot{ghayn.medi}
   \ligature{LIG/}{space}{ghayn.fina}
   \ligature{LIG/}{comma}{ghayn.fina}
   \ligature{LIG/}{period}{ghayn.fina}
\endsetslot
```

這一精妙的有限狀態自動機設計，證明了 $\TeX$ 底層虛擬機架構所蘊含的深厚圖靈完備潛能。

#### 範例四：窄體字母替換與避頭尾碰撞最佳化

在精緻的西文內文字型中，小寫字母 `f` 的右側頂部橫勾往往向前大幅伸展。當 `f` 後方緊跟帶有高聳重音符號的元音字母時（如法語中的 `fè`, `fê`, `fë`），`f` 的筆尖會硬生生地刺入後續重音符號的輪廓內部，造成極度刺眼的物理重疊墨漬。

透過 `fontinst`，排版師可以引入一個專門設計的「窄頭 f」（`f.narrow`），並透過 `LIG/` 預連字機制實現自動上下文避讓：

```latex
\setslot{f}
   \ligature{LIG/}{egrave}{f.narrow}
   \ligature{LIG/}{ecircumflex}{f.narrow}
   \ligature{LIG/}{edieresis}{f.narrow}
\endsetslot
```

當 $\TeX$ 排版引擎在文字中掃描到 `f` 且探測到後序緊隨帶有高重音的 `e` 族字母時，會自動將當前的普通 `f` 悄然無聲地替換為向後收斂的 `f.narrow`，從而在保留優雅字距的同時徹底消除墨跡碰撞！

#### 範例五：「讓字母忘記自己頭上有角」——越南語觸角與雙重重音處理

越南語的拉丁化正字法（Quốc Ngữ）是全世界重音符號系統最為複雜的語言之一。越南語包含兩個獨特的帶觸角（Horn）元音：
- `ơ`（帶觸角的 o）
- `ư`（帶觸角的 u）

不僅如此，這兩個字母還可以疊加上越南語的五種聲調符號（銳音、抑音、問音/跌音、重音），從而形成極為複雜的**雙重複合重音**（如 `ở`, `ỡ`, `ứ`, `ừ`, `ự`）。

在絕大多數通用的歐美商業西文字型中，不僅完全沒有這些複雜的複合字元，甚至連孤立的觸角元音都未曾提供。為了解決這一難題，Haralambous 在 `fontinst` 中設計了著名的「讓字母忘記觸角」演算法：

1. **分離基底與觸角**：
   從母體字型中提取基礎字母 `o` 與 `u`，並從其他符號庫（或透過截取逗號、引號）提取微觀觸角部件 `horn`；
2. **物理裝配單觸角元音**：
   透過 `\installglyph` 將觸角嚴絲合縫地焊接在元音字母的右上角，生成基礎帶角字母；
3. **複合聲調裝配時的「遺忘」機制**：
   當需要為 `ơ` 進一步疊加聲調（如銳音符 `acute`）時，若直接將重音按常規位置居中放置，重音符號必然會與右側的觸角擠壓碰撞在一起。
   `fontinst` 的處理策略極其優雅：它讓裝配引擎在邏輯上「暫時抹掉觸角的存在」，重新讀取母體字母 `o` 的幾何中心座標，將銳音符號向左微移定位，隨後再將縮小版觸角精密焊接在最右側邊緣，從而完美實現了多重重音在微觀幾何層面的和諧共存！

#### 範例六：多重重音多調希臘語（Polytonic Greek）排版

在古典希臘語與拜占庭文獻排版中，多調希臘文（Polytonic Greek）呈現出同樣令人嘆為觀止的重音堆疊結構：
- **氣符（Breathing Marks）**：粗氣符（Spiritus Asper / Rough breathing，帶有輕微哈氣音）與柔氣符（Spiritus Lenis / Smooth breathing）；
- **調符（Accents）**：銳音符（Acute / Oxia）、抑音符（Grave / Varia）、揚抑符（Circumflex / Perispomeni）；
- **下加符（Iota Subscript）**：位於長元音下方微型雕刻的下加字母 $\iota$。

這些符號經常兩兩、甚至三三組合同時出現在同一個元音字母上方（如 $\tilde{\hat{\alpha}}$, $\tilde{\tilde{\omega}}_\iota$）。

在 `fontinst` 程式碼中，排版師必須建立龐大的笛卡爾偏移補償矩陣：

```latex
\installglyph{AlphaRoughAcute}{AlphaRoughAcute}{
   \glyph{Alpha}{1000}
   \movert{\neg{\kerning{rough}{Alpha}}}
   \moveup{\height{Alpha}}
   \glyph{roughacute}{1000}
}
```

透過精準計算字元包圍盒的真實高度與負向字距補償量，使得多重重音能夠垂直對齊在大寫字母的左上方、或居中懸浮在小寫字母的頂端，展現出典雅莊嚴的希臘古典文獻排版風貌。

---

## 4. 邁向 16 位元與多向排版的新紀元：$\Omega$（Omega）系統

隨著電腦全球化浪潮的席捲，傳統 $\TeX$ 系統固有的 8 位元體系結構遭遇了不可逾越的物理瓶頸。

### 4.1 傳統 $\TeX$ 的 8 位元技術瓶頸

1. **單字型 256 字元硬上限**：
   傳統 $\TeX$ 的底層度量（TFM）與 DVI 虛擬機將字元槽位嚴格限制在 8 位元無符號整數（0–255）。面對包含數萬個中文字、日文假名與韓文諺文的東亞 CJK 大字元集，傳統 $\TeX$ 只能採用極其笨拙的子集拆分法（將數萬字拆分為數百個 256 字元的微型子字型，再透過外部預處理器注入巨量複雜的字型切換指令）；
2. **數學模式 16 個家族上限**：
   在近代前沿數學、理論物理與數理邏輯的學術論文中，排版所涉及的特殊符號與字元變體動輒數百種，16 個數學家族的硬上限常常導致「數學字型已滿（Math font exhausted）」的災難性編譯中斷；
3. **單向排版管道的固步自封**：
   傳統 $\TeX$ 的斷行動力學引擎從底層死死綁定在**自左向右（Left-to-Right, LTR）**的單一水平維度上。當面對阿拉伯文、希伯來文等從右向左（RTL）書寫的閃米特語系，或者面對東亞傳統的自上而下、從右向左推進（Vertical TTB）的縱排文獻時，傳統 $\TeX$ 徹底束手無策。

為了從根本上砸碎這些枷鎖，Yannis Haralambous（本著作作者）與約翰·普萊斯（John Plaice）於 20 世紀 90 年代初聯手啟動了宏大的項目——**$\Omega$（Omega）**。

---

### 4.2 $\Omega$ 的架構革新與核心構件

$\Omega$ 絕非對 $\TeX$ 的簡單補丁修貼，而是一場觸及引擎靈魂深處的徹底重構。

```
[多語言輸入文字流 (Unicode / 多位元組)]
             │
             ▼
┌──────────────────────────────────────────────┐
│  OTP (Omega Translation Processes) 轉換流水線  │
│  - 詞法解析 / 語系轉寫 / 上下文形態自動分析      │
└──────────────────────────────────────────────┘
             │
             ▼
┌──────────────────────────────────────────────┐
│  多向排版引擎 (32 種動態正交書寫方向系統)         │
│  - 動態段落構建 / 任意軸向膠水拉伸與斷行分析   │
└──────────────────────────────────────────────┘
             │
             ▼
┌──────────────────────────────────────────────┐
│  OFM (Omega Font Metrics, 16位元分層度量)      │
│  OVF (Omega Virtual Fonts, 多位元組虛擬字型)  │
└──────────────────────────────────────────────┘
             │
             ▼
[擴展 DVI 檔案 / 向量 PostScript / PDF 輸出]
```

#### 16 位元 / 32 位元內部字元原生表示

$\Omega$ 徹底廢棄了單位元組字元結構，內部全部計算變數統一擴展為 **16 位元甚至 32 位元整數**，完美相容 ISO/IEC 10646 與 Unicode 標準。單個字型檔案中可容納的字元數量一舉飆升至 65,536 個甚至更高，東亞漢字全集得以在一個統一的字型檔案內原生定址。

#### OFM（Omega Font Metrics）分層度量格式

$\Omega$ 針對性擴展了 TFM 規範，設計了 **OFM（Omega Font Metrics）**格式：
- **Level 0 OFM**：平坦擴展結構，直接將字元槽位擴展至 65,536 個；
- **Level 1 OFM**：引入了先進的**分層表結構（Hierarchical Table Structure）**與稀疏存儲矩陣。對於存在大面積空白槽位的超大字庫，Level 1 OFM 僅為實際存在的字形分配度量記憶體，極大地節省了系統資源，並引入了對字形旋轉度數與多向包圍盒的原生支援。

#### OVF（Omega Virtual Fonts）多位元組虛擬字型

配合 OFM，$\Omega$ 升級了虛擬字型標準，推出了 **OVF（Omega Virtual Fonts）**。OVF 能夠在多位元組編碼空間內自由編織複雜的跨字庫映射、動態複合筆畫焊接與多語言字形回退機制。

---

### 4.3 核心引擎：OTP（Omega Translation Processes）有限狀態轉換流

$\Omega$ 最具劃時代意義的獨創設計，是其內建的**有限狀態流轉換器——OTP（Omega Translation Processes）**。

#### OTP 的核心工作原理

在傳統排版系統中，文字流直接流入分詞斷行引擎。而在 $\Omega$ 體系中，使用者可以在排版引擎內部構建一條可自由裝卸、級聯鏈接的**動態文字流處理管道**。

OTP 本質上是一門專用於字串模式匹配與流重寫的宣告式微型程式語言。排版師編寫 `.otp` 原始碼腳本，隨後使用 $\Omega$ 專屬編譯器 **`otangle`** 將其編譯為高執行效率的二進位轉換過濾器 **`.ocf`（Omega Compiled Filter）**。

#### OTP 腳本語法實戰

以下是一段真實的 OTP 程式碼片段，用於處理多音希臘文的自動正字法重寫：

```otp
input: 2;
output: 2;

expressions:

`a'  => @"03AC";
`e'  => @"03AD";
`h'  => @"03AE";
`i'  => @"03AF";
`o'  => @"03CC";
`u'  => @"03CD";
`w'  => @"03CE";

"s" { " " | "." | "," | ";" | "!" | "?" } =>
   @"03C2" ;
```

在這段簡潔的規則中：
1. `input: 2; output: 2;` 宣告該轉換流處理 16 位元雙位元組字元；
2. 規則將 ASCII 轉寫序列（如小寫字母加單引號）自動映射為標準的 Unicode 希臘語帶銳音字元碼點（如 `@"03AC"` 為 Greek Small Letter Alpha with Tonos）；
3. 規則 `"s" { ... } => @"03C2" \2;` 實現了精巧的希臘文小寫西格瑪（Sigma）終結態分析：當字母 `s`（常規 $\sigma$）後方緊跟空格或標點符號時，OTP 狀態機在流推進中自動將其重寫為詞尾專用西格瑪字形 $\varsigma$（碼點 `U+03C2`），並將匹配的標點符號原樣送還輸出流！

#### 多級掛載點機制

$\Omega$ 允許排版師將 OTP 過濾器掛載在排版流程的不同關鍵階段：
- **輸入層掛載（Input OTP）**：在字元流進入 $\TeX$ 詞法分析器之前執行，常用於不同字元編碼體系之間的即時轉碼（如將 Big5 即時轉碼為 Unicode）；
- **排版前掛載（Pre-typesetting OTP）**：在段落斷行之前執行，用於處理複雜的連寫分析、重音重排與詞法注音；
- **排版後掛載（Post-typesetting OTP）**：在頁面裝配階段執行，操縱最終輸出的字元槽位與標度。

---

### 4.4 32 種動態排版書寫方向系統（Multi-directional Typesetting）

$\Omega$ 對世界數位排版最偉大的貢獻，莫過於徹底打破了一維水平排版的束縛，建立了一套數學完備的**32 種正交書寫方向系統**。

#### 文字方向的四元軸向矩陣

$\Omega$ 將排版方向拆解為三個彼此獨立的正交物理維度：
1. **字元行進方向（Direction of Writing）**：沿基線一個字元接著一個字元推進的方向；
2. **行進推進方向（Direction of Line Progression）**：排滿一行之後，下一行相對於前一行的推進方向；
3. **字形旋轉朝向（Glyph Orientation）**：字元輪廓自身在局部盒子內的直立或旋轉角度（$0^\circ, 90^\circ, 180^\circ, 270^\circ$）。

$\Omega$ 定義了四個基礎軸向向量：
- **`L`（Left）**：自右向左，向左推進；
- **`R`（Right）**：自左向右，向右推進；
- **`T`（Top）**：自下而上，向上推進；
- **`B`（Bottom）**：自上而下，向下推進。

透過兩兩組合字元方向與行推進方向，$\Omega$ 構成了八種主書寫模式，每種模式均可搭配四種字形朝向，從而構成了完整的 $8 \times 4 = 32$ 種動態書寫系統：

| 模式標識 | 字元行進方向 | 行進推進方向 | 典型應用文明與語言排版場景 |
| :---: | :---: | :---: | :--- |
| **`TL`** | 自上而下（Top to Bottom） | 自右向左（Right to Left） | **東亞古典典籍標準縱排**：中文、日文、韓文傳統古籍直排，行自右向左換行推進 |
| **`TR`** | 自上而下（Top to Bottom） | 自左向右（Left to Right） | **傳統蒙古文（Traditional Mongolian）**與滿文直排：字元從上向下流淌，行自左向右換行推進 |
| **`LT`** | 自左向右（Left to Right） | 自上而下（Top to Bottom） | **現代西文與現代漢語橫排**：標準的全球現代通用排版模式 |
| **`RT`** | 自右向左（Right to Left） | 自上而下（Top to Bottom） | **阿拉伯文、希伯來文與波斯文橫排**：字元自右向左書寫，行自上而下順次換行 |
| **`BL`** | 自下而上（Bottom to Top） | 自右向左（Right to Left） | 歷史碑文、特殊工程繪圖與古文字學（如部分愛爾蘭歐甘文字變體） |
| **`BR`** | 自下而上（Bottom to Top） | 自左向右（Left to Right） | 古代中美洲瑪雅碑銘與特殊學術圖表標註 |
| **`LB`** | 自左向右（Left to Right） | 自下而上（Bottom to Top） | 極少數古代地中海牛耕式轉折書寫（Boustrophedon）過渡行 |
| **`RB`** | 自右向左（Right to Left） | 自下而上（Bottom to Top） | 牛耕式迴旋排版與反向拓印文獻 |

#### 動態局部嵌套機制

在 $\Omega$ 文件中，排版師可以隨時隨地透過命令切換書寫方向：

```latex
\textdir TL
這裡是古典中文直排文獻內容...
\textdir RT
هنا نص عربي (這裡是一段阿拉伯文橫排內容)
\textdir LT
Return to Western horizontal typography.
```

更為震撼的是：**$\Omega$ 的膠水拉伸動力學與 Knuth 斷行演算法完全適應這 32 種方向**！在 `TL`（直排）模式下，垂直方向的行間距變成了水平方向的列間距，字元的寬度變成了高度，垂直列滿時的換行懲罰與不良度完全沿軸向無縫旋轉。不同書寫方向的文字盒子可以像樂高積木一樣在一張頁面中任意互相嵌套，徹底征服了人類歷史上所有已知文明的書寫體系排版難題。

---

## 5. 結論與未來展望（Conclusions and Glimpses at the Future）

回顧 $\TeX$ 與 $\Omega$ 走過的壯麗歷程，我們不僅目睹了一場技術演進的史詩，更見證了數位排版先驅們為了人類文化的完美傳承所付出的無窮智慧。

### 歷史架構的技術極限與使命完成

高德納開創的 TFM、DVI 與虛擬字型（VF）體系，在電腦硬體資源極度匱乏的 20 世紀 70 至 80 年代，以極其有限的記憶體開銷與純整數算術實現了超越時代的絕美排版。

然而，隨著印刷出版全面邁入 21 世紀，這一套建立在「外部度量檔案、有限狀態連字樹與後處理映射」之上的古典架構，其歷史局限性已無可迴避：
1. **與現代字型標準的割裂**：現實工業界已全面普及 OpenType 字型。OpenType 內部自帶了功能強大的高級版面表（Advanced Typographic Tables）：用於上下文連字替換的 **`GSUB`** 表、用於高精度字距微調與光學錨點定位的 **`GPOS`** 表、用於基線對齊的 **`BASE`** 表。在傳統 $\TeX$ 或 $\Omega$ 中，排版師不得不編寫龐雜的腳本將這些早已原生存在於字型內部的高級數據，千方百計地逆向剝離為 TFM/OFM 與虛擬字型，這無疑構成了巨大的工程內耗；
2. **DVI 格式的時代落幕**：在 PDF 成為全球電子文件事實標準的今天，繼續堅持輸出中間 DVI 位元組碼再由後處理驅動轉換，已難以滿足現代透明度混合、色彩管理系統（ICC Profiles）以及互動式超連結的複雜需求。

### 從 $\Omega$ 到 Aleph、XeTeX 與 LuaTeX 的鳳凰涅槃

$\Omega$ 系統的諸多超前探索（尤其是多向排版模型與 16 位元字元統一支援），為 $\TeX$ 世界的現代化轉型播下了最關鍵的火種：

1. **Aleph（$\aleph$）**：由熱羅姆·勞雷（Jérôme Laurens）等人發起的項目，將 $\Omega$ 的多向排版核心與穩定的 `pdftex` 引擎進行深度雜交，消除了早期 $\Omega$ 的諸多底層 Bug，實現了直接生成高品質 PDF 的壯舉；
2. **XeTeX**：由喬納森·丘（Jonathan Kew）開發，採取了「徹底擁抱現代作業系統」的務實哲學。XeTeX 摒棄了傳統的 TFM 與外部映射機制，直接調用作業系統底層的字型光柵化渲染引擎（macOS 上的 Core Text 以及跨平台的 FreeType/HarfBuzz），使得排版師可以在 $\LaTeX$ 文件中直接透過字型名稱調用系統安裝的任意 OpenType/TrueType 字型，並原生啟用其內部的全部高級特性；
3. **LuaTeX**：由哈基姆·霍克沃特（Hartmut Henkel）、塔克·霍克斯（Taco Hoekwater）與漢斯·哈根（Hans Hagen）傾力打造的當代終極 $\TeX$ 引擎。LuaTeX 徹底拆除了 $\TeX$ 固步自封的底層藩籬，將一個現代、高效、輕量級的 **Lua 腳本直譯器嵌入到了 $\TeX$ 引擎的心臟深處**！在 LuaTeX 中，不僅 TFM 編譯、斷行計算、數學公式排版的所有內部數據結構全部以 Lua 表的形式暴露給開發者，排版師甚至可以用 Lua 語言重寫 $\TeX$ 的整個段落斷行演算法與 OpenType 字型解析管線。

從高德納最初在史丹佛大學黑板上寫下的盒子與膠水公式，到 Yannis Haralambous 構筑的 $\Omega$ 宏偉多向世界，再到今天由 LuaTeX 與 HarfBuzz 驅動的現代開源排版文明，$\TeX$ 所代表的追求排版至臻至美的精神核心，歷經半個世紀的洗禮，不僅未曾褪色，反而如同陳釀的美酒，在人類知識與文明的數位星河中愈發散發出奪目璀璨的光芒！
