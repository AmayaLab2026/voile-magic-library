---
title: "第 12 章：字體的設計、編輯與製作技術"
description: "完整無刪節 1:1 學術全譯：數字字體制作工具演進史（Fontographer、FontStudio、Ikarus、FontLab、FontForge）；矢量輪廓數學機理（PostScript 三次貝塞爾與 TrueType 二次 B-樣條、極值點約束、輪廓方向與非零纏繞法則、排印度量網格）；FontLab 工業生產全流程（Names/Pages/Ranges/Index 四大字符視圖、Font Info 核心排印度量與 OpenType 元數據、字形繪圖與節點拓撲優化、字距調整與 Kerning 類、Multiple Master 多重母版設計空間、原生 Python 腳本自動化編程）；FontForge 開源架構與高級特性（X11 交互環境、垂直排版度量、CID 鍵控字體與扁平化）；位圖自動描摹技術（Potrace 與 ScanFont 參數調優與幾何缺陷）。"
---

# 第 12 章：字體的設計、編輯與製作技術

**雅尼斯·哈拉蘭博斯（Yannis Haralambous, Ph.D.）著**  
*選自《Fonts & Encodings》第 441–504 頁*

*譯者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

現在，我們來到了全書最爲核心的聖殿：**創造字體**。

我們是否必須成爲像赫爾曼·察普夫（Hermann Zapf）或讓·弗朗索瓦·波爾謝茲（Jean François Porchez）那樣的曠世設計大師，纔能有資格踏入字體創作的領域？絕非如此。正如任何人都可以揮毫寫下一封書信、繪出一幅素描一樣，今天每一個具備基本審美與技術直覺的人，都可以投身於字體的設計與改良。

在計算機排版技術徹底普及的今天，創造一套高品質的數字矢量字體不再是隻有大型鑄字工坊與跨國軟件巨頭才能染指的祕術。隨着個人圖形工作站與專業字體設計軟件（Font Editors）的飛速演進，獨立字體設計師、排版學者乃至業餘愛好者，都能夠直接在屏幕上操縱純粹的幾何矢量輪廓，賦予每一個字符以獨特的靈魂與生命力。

然而，字體設計是一門在“極致自由的藝術靈感”與“冰冷嚴苛的數學和工業標準”之間走鋼絲的高難度科學。在字形美感背後，隱藏着一整套涉及貝塞爾微積分、輪廓纏繞拓撲學、整型網格離散化、排印度量度量系統以及複雜的跨平臺二進制格式包裝邏輯。本章將全面解構現代數字字體創作的核心軟件生態與底層幾何技術機理。

---

# 字體設計與編輯軟件全景

在過去二十餘年的數字字體演進史上，至少有六套具有里程碑意義的大型系統塑造了現代字體工業的工作流：

## 1. 拓荒時代的先驅：Fontographer 與 FontStudio

* **Macromedia Fontographer**（最早由 Altsys 公司的吉姆·馮·赫爾（Jim von Ehr）於 1986 年開發）：這是人類歷史上首個在 Macintosh 圖形界面上實現直接用貝塞爾鋼筆工具交互繪製 PostScript Type 1 輪廓的革命性字體編輯器。它讓千萬排印創作者從晦澀的 PostScript 純代碼座標中徹底解脫出來。儘管後續歷經 Altsys 轉讓給 Macromedia、再轉手給 FontLab 的滄桑歷程，其界面更新一度陷入停滯，但其直觀的“字體字符網格窗口”與“字形編輯畫板”奠定了後世所有字體軟件的人機交互範式（圖 12-1）。
* **Letraset FontStudio**（運行於經典 Mac OS 9 時代）：由著名的幹印即貼字字模巨頭 Letraset 打造的高端專業級字體工坊軟件。它引入了極其先進的自動微調提示（Auto-hinting）、灰度預覽與多圖層度量網格系統，在 1990 年代初受到各大專業鑄字廠商的極高推崇（圖 12-2）。
* **URW Ikarus**：由彼得·卡羅（Peter Karow）領導的德國 URW 公司開發的史詩級工業系統。與面向微機的軟件不同，Ikarus 誕生於大型機與專業繪圖板時代，率先採用了切線點、角點與圓弧極值點的嚴密數學描述體系，成爲全球頂級字體公司數字化歷史鉛字檔案的核心基石。
* **FontToolbox**：一套在專業排印工程師圈子內廣泛流傳的底層字體操作工具集。

::: tip 圖 12-1：Macromedia Fontographer 在 Mac OS X 下的字體字符總覽窗口。每個方格內直觀呈現字符圖形、Unicode 編碼與 PostScript 字形名稱
![圖 12-1：Macromedia Fontographer 在 Mac OS X 下的字體字符總覽窗口](/images/fonts-encodings/fig12-1.png)
*圖 12-1：Macromedia Fontographer 在 Mac OS X 下的字體字符總覽窗口。每個方格內直觀呈現字符圖形、Unicode 編碼與 PostScript 字形名稱。*
:::

::: tip 圖 12-2：Letraset FontStudio 在經典 Mac OS 9 系統下的單字符字形編輯工作窗口。展示了早期專業字體設計所依賴的參考基準輔助線與貝塞爾節點調控界面
![圖 12-2：Letraset FontStudio 在經典 Mac OS 9 系統下的單字符字形編輯工作窗口](/images/fonts-encodings/fig12-2.png)
*圖 12-2：Letraset FontStudio 在經典 Mac OS 9 系統下的單字符字形編輯工作窗口。展示了早期專業字體設計所依賴的參考基準輔助線與貝塞爾節點調控界面。*
:::

---

## 2. 現代工業標準霸主：FontLab 與開源傳奇 FontForge

在當今字體工業中，佔據統治地位的兩大旗艦軟件分別是商業領域的 **FontLab** 與開源社區的 **FontForge**：

* **FontLab Studio**：由蘇聯裔天才程序員尤里·亞爾莫拉（Yuri Yarmola）與瓦季姆·蘇沃洛夫（Vadim Suvorov）聯合傾力打造。自 1990 年代初問世以來，它在長達二十餘年的時間裏無可爭辯地統治着全球各大商業字體廠商（如 Adobe、Linotype、Monotype、Bitstream）的工業生產流水線。它具備無懈可擊的跨平臺兼容性、工業級 OpenType 特性編譯器以及強大的原生 Python 腳本擴展接口。
* **FontForge**（原名 **PfaEdit**）：由傳奇黑客**喬治·威廉姆斯**（George Williams）傾注畢生心血獨立打造的自由開源軟件（FOSS）。它不僅完全支持所有已知的矢量與位圖字體格式，更內建了完整的 TrueType 虛擬機單步調試器與深邃的數學幾何引擎。

---

# 字體工程的底層幾何與通用原則

在真正動筆繪製第一個字符之前，每一個設計者都必須牢牢掌握數字字體在底層幾何、數學與空間度量上的嚴苛通用原則：

## 1. 三次貝塞爾曲線與二次 B-樣條的本質分野

數字字體主要由兩大對立陣營的矢量數學模型所支配：
* **PostScript / OpenType CFF 陣營**：採用**三次貝塞爾曲線**（Cubic Bézier Curves）。每段曲線由 4 個點決定：2 個端點（On-curve nodes）與 2 個離散控制點（Off-curve control points）。數學公式爲：
  $$B(t) = (1-t)^3 P_0 + 3(1-t)^2 t P_1 + 3(1-t)t^2 P_2 + t^3 P_3, \quad t \in [0, 1]$$
  三次貝塞爾曲線具備極高的曲率靈活性與自由度，能夠用極少的節點描摹出極其流暢的曲線，是傳統字體藝術家的最愛。
* **TrueType 陣營**：採用**二次 B-樣條曲線**（Quadratic Bézier / B-Splines）。每段曲線僅由 3 個點決定：2 個端點與 1 個控制點：
  $$B(t) = (1-t)^2 P_0 + 2(1-t)t P_1 + t^2 P_2, \quad t \in [0, 1]$$
  當兩個連續控制點相鄰出現時，TrueType 規範規定在其線段中點處隱式插入一個虛擬的端點。二次曲線的計算速度極快，但由於自由度較低，通常需要比三次曲線多出 30% 到 50% 的控制節點才能達到相同的擬合精度。現代字體編輯器必須能夠在這兩種曲線空間之間進行無損或極低誤差的互相轉換。

## 2. 整數設計網格與全身身長（Units per em, UPM）

字體內部的幾何座標並非無限精密的實數，而是映射在一個剛性的整數笛卡爾座標系中：
* 在 PostScript Type 1 / CFF 字體中，全身身長通常固定爲 **1000** 個單位；
* 在 TrueType / OpenType TTF 字體中，爲了便於二進制快速移位運算，全身身長通常設定爲 2 的冪次方，最經典的標準是 **2048** 個單位。
所有的節點座標必須被量化取整爲整數。取整誤差若處理不當，極易導致曲線光滑接點處發生肉眼可見的微小折角。

## 3. 輪廓方向與非零纏繞法則（Non-Zero Winding Rule）

一個字符往往由多個閉合子輪廓（Contours）複合而成（例如圓環 ‘O’ 包含一個外輪廓和一個內輪廓）。光柵化填充引擎如何判斷哪個區域是黑色實體、哪個區域是白色鏤空？這完全依賴於輪廓的走向與纏繞法則：
* **PostScript 鐵律**：**外層輪廓必須遵循逆時針方向（Counter-Clockwise），內層鏤空輪廓必須遵循順時針方向（Clockwise）。**
* **TrueType 鐵律**：恰好截然相反！**外層輪廓必須遵循順時針方向，內層鏤空輪廓必須遵循逆時針方向。**
若輪廓方向顛倒，現代文本渲染引擎在執行非零纏繞數（Non-zero winding number）判定時，就會發生字符“反白”或內部孔洞被完全填黑的毀滅性錯誤！字體編輯器均配備了一鍵反轉輪廓方向（Reverse Contour）與自動糾正纏繞向的工具。

## 4. 極值點約束（Extrema Points）

在貝塞爾曲線的數學切線方向平行於 X 軸或 Y 軸的最外側頂峯與谷底位置，必須嚴格放置端點（On-curve Extrema Nodes）。**這是數字字體工業的一條鐵律！**
若在曲線的極值點處缺乏端點支撐，PostScript 與 TrueType 的微調提示（Hinting）引擎將無法捕獲字符的外邊界座標，導致字號縮小時筆畫外突量失控、基線顛簸或發生嚴重的光柵化截斷。

## 5. 排印度量：步進寬度與側邊軸承（Side Bearings）

一個字符在水平排版時所佔據的空間不僅由其黑體墨跡決定，更由其看不見的虛擬外框決定：
* **字形原點（Origin, (0,0)）**：字符繪製的起始基準點。
* **左側邊距（Left Side Bearing, LSB）**：從原點到字符最左側幾何邊緣的水平距離。
* **字符寬度 / 步進寬度（Advance Width / Set-Width）**：字符排印時光標從當前字符原點跳轉到下一個字符原點的總距離。
* **右側邊距（Right Side Bearing, RSB）**：從字符最右側幾何邊緣到步進寬度終點的水平距離。
$$ \text{Advance Width} = \text{LSB} + \text{Bounding Box Width} + \text{RSB} $$
控制好 LSB 與 RSB，是確保連續文字排版時灰度均勻、間隙和諧的關鍵所在。

---

# 現代工業標準：FontLab 全景深度實戰

FontLab 深度整合了對 Type 1、TrueType、OpenType 以及 Multiple Master 格式的全功能原生支持，其核心工作流構建在高度專業化的“四大字符總覽視圖模式”之上：

## 1. FontLab 字體總覽窗口的四大視圖模式

在 FontLab 的主字體管理窗口中，用戶可以根據當前工程任務的側重點，自如切換四種完全不同的字符組織模式：

1. **Names 模式（字形名稱模式，圖 12-3）**：依據標準 Adobe PostScript 字形命名規範（如 `A`, `acute`, `adieresis`, `hyphen`, `ampersand`）組織排列。這是傳統 PostScript 字體工程師最習慣的視角，直觀反映字形在排版引擎內部的符號命名樹。
2. **Pages 模式（編碼代碼頁模式，圖 12-4）**：以經典的 256 字符單字節編碼頁（Code Page，如 Windows-1252 Latin 1、MacRoman、IBM CP437、ISO 8859 系列）爲基準劃分。每個代碼頁被切分爲整齊的 16×16 矩陣表格，極大地方便了設計者爲特定舊式操作系統或區域市場快速排查字符缺漏。每個編碼頁在後臺直接映射至一個擴展名爲 `.cpg` 的配置文件。
3. **Ranges 模式（Unicode 字符塊模式，圖 12-5）**：完全遵循 Unicode 聯盟官方劃分的標準字符集區間（Unicode Blocks / Ranges，如 Basic Latin、Latin-1 Supplement、Latin Extended-A、Greek and Coptic、Cyrillic 等）。在開發包含數千字符的大型泛歐或全球化通用 OpenType 字體時，該模式是必不可少的工作中樞。
4. **Index 模式（字形索引模式，圖 12-6）**：直接以字體二進制文件內部的物理字形索引（Glyph Index, **GID**）爲順序展示。在底層 TrueType/OpenType 結構中，GID 0 永遠固定指派給缺失符號（`.notdef`），隨後的各字形按其實際編譯進字體數據流中的物理先後次序自左向右嚴格遞增排列。

::: tip 圖 12-3：FontLab 字體窗口中的 Names（字形名稱）視圖模式
![圖 12-3：FontLab 字體窗口中的 Names（字形名稱）視圖模式](/images/fonts-encodings/fig12-3.png)
*圖 12-3：FontLab 字體窗口中的 Names（字形名稱）視圖模式。*
:::

::: tip 圖 12-4：FontLab 字體窗口中的 Pages（單字節編碼代碼頁）視圖模式
![圖 12-4：FontLab 字體窗口中的 Pages（單字節編碼代碼頁）視圖模式](/images/fonts-encodings/fig12-4.png)
*圖 12-4：FontLab 字體窗口中的 Pages（單字節編碼代碼頁）視圖模式。*
:::

::: tip 圖 12-5：FontLab 字體窗口中的 Ranges（Unicode 標準字符區間塊）視圖模式
![圖 12-5：FontLab 字體窗口中的 Ranges（Unicode 標準字符區間塊）視圖模式](/images/fonts-encodings/fig12-5.png)
*圖 12-5：FontLab 字體窗口中的 Ranges（Unicode 標準字符區間塊）視圖模式。*
:::

::: tip 圖 12-6：FontLab 字體窗口中的 Index（物理字形索引 GID）視圖模式
![圖 12-6：FontLab 字體窗口中的 Index（物理字形索引 GID）視圖模式](/images/fonts-encodings/fig12-6.png)
*圖 12-6：FontLab 字體窗口中的 Index（物理字形索引 GID）視圖模式。*
:::

---

## 2. 全面的排印度量與元數據架構（Font Info）

設計字體絕不僅僅是畫出好看的矢量外形，更是一項極其繁重的技術元數據配置工程。在 FontLab 的“Font Info”（字體信息屬性面板，`File > Font Info`）中，涵蓋了決定字體跨平臺行爲的關鍵標籤頁：

* **Names and Copyright（名稱與版權信息，圖 12-7 [a]）**：遵循嚴格的 OpenType `name` 記錄規範（多達 20 餘種預定義字符串標識符），包括字體族名稱（Family Name）、樣式名稱（Style Name）、完整字模名稱（Full Font Name）、PostScript 內部名稱、獨一無二的唯一標識符（Unique Font Identifier）、版本號以及設計者商標與法律版權聲明。
* **Key Dimensions（核心排印度量尺寸，圖 12-8 [a]）**：精確設定字體的全身身長網格（Units per em，通常 PostScript 設定爲 1000，TrueType 設定爲 2048）、大寫字母高度（Cap-Height）、小寫 x-高度（X-Height）、字體上行升幅（Ascender）、下行降幅（Descender）以及行距（Line Gap）。
* **Supported Codepages and Unicode Ranges（支持的代碼頁與 Unicode 範圍標誌位，圖 12-8 [b]、[c]）**：直接對應 TrueType/OpenType 二進制規範中 `OS/2` 表的 128 位 `ulUnicodeRange` 掩碼與 64 位 `ulCodePageRange` 掩碼。這些比特位明確通知操作系統與文字渲染管線：本字體經過認證能夠完整支持哪些語言與國家標準！
* **TrueType 特定高級度量表**：包括預計算字形水平物理像素寬度的 `hdmx` 表、垂直度量對齊控制的 `VDMX` 表，以及決定在特定低分辨率下是否開啓平滑抗鋸齒的 `gasp` 表。

::: tip 圖 12-7：FontLab 字體屬性面板：字體命名規範、版權信息及 OpenType 擴展名稱配置標籤頁：(a) 核心名稱與版權；(b) 附加 OpenType 名稱字段；(c) 法律說明與版權詳錄
![圖 12-7：FontLab 字體屬性面板：字體命名規範、版權信息及 OpenType 擴展名稱配置標籤頁](/images/fonts-encodings/fig12-7.png)
*圖 12-7：FontLab 字體屬性面板：字體命名規範、版權信息及 OpenType 擴展名稱配置標籤頁：(a) 核心名稱與版權；(b) 附加 OpenType 名稱字段；(c) 法律說明與版權詳錄。*
:::

::: tip 圖 12-8：FontLab 字體屬性面板：核心排印度量尺寸（Key dimensions）、支持代碼頁與 Unicode 覆蓋區間配置標籤頁：(a) 全身尺寸與基準高度；(b) 支持的代碼頁與默認字符集；(c) 支持的 Unicode 區間掩碼
![圖 12-8：FontLab 字體屬性面板：核心排印度量尺寸（Key dimensions）、支持代碼頁與 Unicode 覆蓋區間配置標籤頁](/images/fonts-encodings/fig12-8.png)
*圖 12-8：FontLab 字體屬性面板：核心排印度量尺寸（Key dimensions）、支持代碼頁與 Unicode 覆蓋區間配置標籤頁：(a) 全身尺寸與基準高度；(b) 支持的代碼頁與默認字符集；(c) 支持的 Unicode 區間掩碼。*
:::

---

## 3. 字形繪製、節點拓撲與度量微調視窗

在 FontLab 的字形繪製編輯視窗中（圖 12-9），設計師擁有極高精度的鋼筆工具與變換操縱桿：
* **節點類型系統**：FontLab 將節點分爲角節點（Corner nodes，兩側控制桿獨立運動）、光滑切線節點（Smooth nodes，兩側控制桿保持共線反向聯動）以及對稱節點（Symmetric nodes）。
* **背景臨摹層（Template Layer）**：可將高分辨率手繪掃描線稿或歷史字模位圖直接導入背景層，通過半透明高亮輔助矢量勾勒。
* **輪廓極值自動對齊與曲線平滑優化**：具備一鍵清理冗餘多餘控制節點（Optimize Curve）功能，在保持極高視覺保真度的同時將文件體積壓縮至極致。

在字距度量視窗中（Metrics Window，圖 12-10）：
* 支持任意字符串文本的即時排印流預覽；
* 設計師可直接用光標拖拽字符兩側的側邊軸承虛線，實時微調 LSB 與 RSB；
* **字距調整對（Kerning Pairs）與基於類的字距（Class-based Kerning）**：對於大寫字母組合如 “AV”、“To”、“WA”，常規固定間距會導致字符間出現刺眼的巨大空間縫隙。通過定義特定字符對的負向微調值，可使兩字緊密咬合。爲了避免 $O(N^2)$ 組合爆炸，FontLab 提供了強大的“字距調整類”功能，將具有相似右側輪廓的字符歸爲一組（如 ‘A’, ‘À’, ‘Á’, ‘Â’, ‘Ã’），實現跨字符組的批量聯動微調！

::: tip 圖 12-9：FontLab 字形繪製編輯視窗。展示了節點狀態、控制桿操縱、座標讀數以及背景參考線
![圖 12-9：FontLab 字形繪製編輯視窗](/images/fonts-encodings/fig12-9.png)
*圖 12-9：FontLab 字形繪製編輯視窗。展示了節點狀態、控制桿操縱、座標讀數以及背景參考線。*
:::

::: tip 圖 12-10：FontLab 度量與字距調整視窗（Metrics Window）。支持多字符交互混排、側邊距拖拽與 Kerning 字符對實時校正
![圖 12-10：FontLab 度量與字距調整視窗](/images/fonts-encodings/fig12-10.png)
*圖 12-10：FontLab 度量與字距調整視窗。支持多字符交互混排、側邊距拖拽與 Kerning 字符對實時校正。*
:::

---

## 4. 多重母版字體（Multiple Master Fonts）設計空間

FontLab 深度內建了對 Adobe **Multiple Master**（**MM**）技術的原生建模支持：
* 設計師可以定義多達 4 個連續設計軸（如字重 Weight 軸：從 Light 到 Black；字寬 Width 軸：從 Condensed 到 Expanded；視覺字號 Optical Size 軸：從 6pt Caption 到 72pt Display）；
* 在設計空間的各個極值角落分別繪製一套幾何拓撲完全同構的母版字形（Master Glyphs）；
* **拓撲相容性鐵律**：所有母版字形必須具備**絕對完全相同數量的閉合輪廓、完全相同數量的控制節點，以及完全相同類型的控制點序列！**
一旦母版拓撲校驗通過，系統便能在多維設計空間中進行全自動多項式線性插值，瞬間演算衍生出成百上千種截然不同的衍生字族樣式！

---

## 5. 原生 Python 腳本自動化編程

FontLab 工業價值的巔峯之一，在於其內置了完整的 Python 解釋器與極其豐富的原生對象模型（FontLab Python API）。排印工程師可以通過編寫純 Python 腳本，完全繞開耗時的人工鼠標點選，批量自動化操縱海量字庫。

### 核心對象模型：
* `fl` 全局應用上下文對象：管理當前活動字體 `fl.font`、當前字形索引 `fl.iglyph`、視窗刷新與重繪；
* `Font` 字體對象：包含了全部字形集合、元數據屬性與代碼頁表；
* `Glyph` 字形對象：包含了輪廓（Contours）、節點（Nodes）、組件（Components）與側邊軸承；
* `Node` 節點對象：包含座標 `Point`、節點類型標誌位（`nLINE`, `nCURVE`, `nMOVE`, `nSMOOTH`, `nFIXED` 等）。

### 經典實戰腳本範例：

#### 範例 1：批量篩選所有以字母 ‘f’ 開頭的字形並統計其總數

```python
import re

total = 0
r1 = re.compile(r'^f')
fl.Unselect()

for gi in range(len(fl.font)):
    glyph_name = fl.font[gi].name
    if r1.match(glyph_name):
        fl.Select(gi)
        total += 1

print(f"Total matching glyphs found: {total}")
fl.UpdateFont()
```

#### 範例 2：通過純數學腳本向當前字形動態插入幾何矩形輪廓

```python
from fontlab import *

# 獲取當前活動字形
g = fl[fl.ifont][fl.iglyph]

# 定義矩形四角座標
r_ll = Point(100, 0)
r_ur = Point(500, 700)

# 動態構築輪廓閉合環
n1 = Node(nMOVE, r_ll)
n2 = Node(nLINE, Point(r_ur.x, r_ll.y))
n3 = Node(nLINE, r_ur)
n4 = Node(nLINE, Point(r_ll.x, r_ur.y))

# 壓入字形並閉合
g.Add(n1)
g.Add(n2)
g.Add(n3)
g.Add(n4)
g.JoinAll()

# 強制重算邊界框並刷新字體
g.SetModified(1)
fl.UpdateFont()
```

---

# 開源世界的傳奇旗幟：FontForge 架構與實戰

由喬治·威廉姆斯獨立打造的 **FontForge**，是自由與開源排印世界的鎮國之寶。它基於嚴謹的 X11 視窗架構運行，底層以 C 語言寫就，兼具難以置信的跨平臺靈活性與深度技術通透性。

::: tip 圖 12-11：FontForge 主字體字符表視窗（Font Table Window）。展示了完備的 Unicode 字符方格陣列、字符編碼槽位與狀態標記
![圖 12-11：FontForge 主字體字符表視窗](/images/fonts-encodings/fig12-11.png)
*圖 12-11：FontForge 主字體字符表視窗。展示了完備的 Unicode 字符方格陣列、字符編碼槽位與狀態標記。*
:::

::: tip 圖 12-12：FontForge 字形輪廓編輯繪製視窗。展示了三次/二次混合編輯模式、多圖層管理、仿射變換工具箱與精密座標讀數
![圖 12-12：FontForge 字形輪廓編輯繪製視窗](/images/fonts-encodings/fig12-12.png)
*圖 12-12：FontForge 字形輪廓編輯繪製視窗。展示了三次/二次混合編輯模式、多圖層管理、仿射變換工具箱與精密座標讀數。*
:::

## 1. FontForge 的獨特架構優勢

* **主字體映射視窗（Font Table Window，圖 12-11）**：支持從 0 到 1,114,111 全部 Unicode 字符空間乃至自定義私有編碼頁的無級縮放總覽。
* **字形多圖層編輯視窗（Glyph Window，圖 12-12）**：具有清晰的前景圖層（Foreground）、背景臨摹層（Background）以及專業數學輔助線層（Guide Layer）。支持在三次貝塞爾與二次 B-樣條模式之間隨時切換。
* **豐富的導出伴生格式**：生成字體時，可一鍵協同生成伴生的 AFM（Adobe Font Metrics）、PFM（Printer Font Metrics）、以及專供 TeX/LaTeX 系統的 TFM（TeX Font Metric）與 ENC 編碼映射表！
* **仿射變換矩陣（Affine Transformation Matrix）**：內置強大的幾何數學工具箱，支持通過設置 $2 \times 3$ 仿射矩陣，對字符輪廓進行精確的平移、旋轉、縮放、斜切與鏡像操作：
  $$ \begin{bmatrix} x' \\ y' \end{bmatrix} = \begin{bmatrix} a & c \\ b & d \end{bmatrix} \begin{bmatrix} x \\ y \end{bmatrix} + \begin{bmatrix} t_x \\ t_y \end{bmatrix} $$

## 2. 垂直排版（Vertical Typesetting）與 CJK 度量支持

在處理中日韓（CJK）以及傳統蒙古文等東亞豎排文本時，字符的排印度量從傳統的水平基線轉向了垂直中央基線。FontForge 對垂直排版提供了全方位原生支持：
* 在度量視窗中直接啓用垂直排版模式（Vertical Metrics）；
* 獨立測量並配置每個字符的**上側邊距（Top Side Bearing, TSB）**、**垂直步進高度（Vertical Advance Height）**與底側邊距；
* 自動生成並校驗 OpenType/TrueType 二進制規範中的垂直頭信息表 `vhea` 與垂直度量表 `vmtx`，並深度配合 OpenType `vert`（垂直書寫替代）與 `vrt2` 高級佈局特性。

## 3. CID 鍵控字體（CID-keyed Fonts）與扁平化

面對包含數萬漢字的超大型東亞字庫，傳統的單字節或簡單 Unicode 扁平映射往往難以承載複雜的異體字體系。FontForge 原生支持 Adobe 的 **CID 架構**（基於字符集合 Registry-Ordering-Supplement 的 CIDFont）：
* 允許設計者將字體組織爲多子字族聚合體；
* 提供極其關鍵的 `CID > Flatten`（扁平化）指令：能夠一鍵“剝離”晦澀複雜的 CID 結構，將其直接解構降級爲普通的全局 Unicode 編碼字體，極大地方便了將舊式專業東亞字體向現代跨平臺 OpenType 格式的平民化遷移！

---

# 位圖自動描摹技術（Autotracing）

對於通過紙張手工繪製或歷史掃描獲得的字形圖像，如果每一個字符都需要人工拉貝塞爾曲線重新勾勒，其勞動量對於數萬漢字庫而言是無法想象的。爲此，圖形學界誕生了**自動描摹技術**（**Autotracing** / 矢量化）。

然而，哈拉蘭博斯博士在此提出了極其嚴肅的排印學術警示：**自動描摹絕非靈丹妙藥，濫用描摹軟件生產的字體往往是排印學上的災難！**
* 掃描位圖中的任何微小墨暈、紙張纖維噪點或光學畸變，都會被算法不加甄別地忠實還原成數十個細碎扭曲的貝塞爾斷點；
* 算法無法理解排印學中的“骨骼對齊”概念，導致直筆不直、圓弧扁塌、左右兩柱粗細不一。

儘管如此，在掌握嚴密參數調校的前提下，現代描摹工具依然是字體拓荒的重要武器：

## 1. Peter Selinger 的開源神器：Potrace

作爲開源世界無可替代的幾何矢量化核心引擎，彼得·塞林格（Peter Selinger）編寫的 **potrace** 採用了一套精妙的多邊形逼近與三次貝塞爾平滑擬合算法：
1. **輪廓多邊形粗分解**：追蹤二值化位圖的黑白像素邊緣；
2. **最優多邊形降採樣**：基於距離懲罰函數尋找頂點最少的最優閉合多邊形；
3. **貝塞爾平滑逼近**：對多邊形連續角點進行曲率評估，自動生成極度優美光滑的三次曲線段。
FontForge 深度內嵌了對 potrace 的無縫調用接口（`Element > AutoTrace`）。

## 2. 商業描摹巔峯：ScanFont

由 FontLab 官方出品的配套工具 **ScanFont**（圖 12-13），專爲將複雜手繪圖樣轉化爲專業字模而生。它提供了極其豐富的實時交互參數滑塊：
* **Smoothness（平滑度）**：過濾微觀像素毛刺的平滑門限；
* **Corner threshold（拐角閾值）**：決定何處強制摺疊爲銳利尖角、何處圓融過渡；
* **Curve fitting tolerance（曲線擬合容差）**：控制矢量線條偏離原始像素邊緣的最大允許誤差；
* **Extrema optimization（極值點自動對齊）**：確保生成的節點嚴格落在水平與垂直極值點切線上。

::: tip 圖 12-13：ScanFont 中實時配置與動態預覽位圖自動描摹參數的交互式面板
![圖 12-13：ScanFont 中實時配置與動態預覽位圖自動描摹參數的交互式面板](/images/fonts-encodings/fig12-13.png)
*圖 12-13：ScanFont 中實時配置與動態預覽位圖自動描摹參數的交互式面板。*
:::

在實際描摹測試中對比發現：ScanFont 在處理字母 ‘A’ 尖銳的內角頂點時偶有輕微形變；而 potrace 則傾向於在平直長主幹的中段冗餘插入若干微小的控制點。**因此，任何自動描摹產物，都必須經過字體設計師在字形窗口中進行人工審查、刪除冗餘雜點、對齊極值並重構關鍵水平/垂直主幹，方能真正達到工業級出版質量標準！**

---

# 結語

字體的設計與編輯，是數字人文科學中最具魅力的交匯點。它一方面紮根於數千年書法墨跡與金屬活字的經典藝術風骨，另一方面又緊密咬合着離散微分幾何、現代計算機圖形學與龐大的二進制文件規範。

無論是駕馭商業流水線上的霸主 FontLab，還是馳騁在開源自由的 FontForge 天地中，真正賦予一套字體以不朽生命力的，始終是設計者那雙在微觀網格與宏觀排印節律之間洞悉全局的慧眼，以及對技術規範毫釐不爽的工匠之心。
