---
title: "第 12 章：字體的設計、編輯與製作技術"
description: "完整無刪節中文譯本：現代數字字體制作軟件全景（Fontographer、FontStudio、FontLab Studio、FontForge、ScanFont）；PostScript 三次貝塞爾曲線與 TrueType 二次 B-樣條數學機理、輪廓順逆走向與纏繞法則、極值點約束、度量間距微調、多重母版（Multiple Master）設計空間與位圖自動描摹算法。"
---

# 第 12 章：字體的設計、編輯與製作技術
**雅尼斯·哈拉蘭博斯（Yannis Haralambous, Ph.D.）著**
*選自《Fonts & Encodings》第 445–506 頁*

*譯者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

在計算機排版技術徹底普及的今天，創造一套高品質的數字矢量字體不再是隻有大型鑄字工坊與大型軟件巨頭才能染指的秘術。隨着個人圖形工作站與專業字體設計軟件（Font Editors）的飛速演進，獨立字體設計師、排版學者乃至具備審美直覺的普通創作者，都能夠直接在屏幕上操縱純粹的幾何矢量輪廓，賦予每一個字符以獨特的靈魂與生命力。

然而，字體設計是一門在“極致自由的藝術靈感”與“冰冷嚴苛的數學與工業標準”之間走鋼絲的高難度科學。在字形美感背後，隱藏着一整套涉及貝塞爾微積分、輪廓纏繞多邊形拓撲、整型網格離散化、排印度量度量系統以及複雜的跨平台二進制格式包裝邏輯。本章將全面解構現代數字字體創作的核心軟件生態與底層幾何技術機理。

---

# 字體設計與編輯軟件全景

在數字字體演進史上，有幾款具有劃時代意義的經典軟件塑造了現代字體工業的工作流：

## 1. 拓荒時代的先驅：Fontographer 與 FontStudio

* **Macromedia Fontographer**（最早由 Altsys 公司於 1986 年開發）：這是人類歷史上首個在 Macintosh 圖形界面上實現直接用貝塞爾鋼筆工具交互繪製 PostScript Type 1 輪廓的革命性字體編輯器。它讓千萬排印創作者從晦澀的 PostScript 純代碼座標中徹底解脱出來。儘管後續歷經所有權易手與停滯，但其直觀的“字體字符網格窗口”與“字形編輯畫板”奠定了後世所有字體軟件的人機交互範式。
* **Letraset FontStudio**（運行於經典 Mac OS 9 時代）：由著名的幹印即貼字字模巨頭 Letraset 打造的高端專業級字體工坊軟件。它引入了極其先進的自動微調提示（Auto-hinting）、灰度預覽與多圖層度量網格系統，在 1990 年代初受到各大專業鑄字廠商的極高推崇。

::: tip 圖 12-1：Macromedia Fontographer 在 Mac OS X 下的字體字符總覽窗口。每個方格內直觀呈現字符圖形、Unicode 編碼與 PostScript 字形名稱
![圖 12-1：Macromedia Fontographer 在 Mac OS X 下的字體字符總覽窗口](/images/fonts-encodings/fig12-1.png)
*圖 12-1：Macromedia Fontographer 在 Mac OS X 下的字體字符總覽窗口。每個方格內直觀呈現字符圖形、Unicode 編碼與 PostScript 字形名稱。*
:::

::: tip 圖 12-2：Letraset FontStudio 在經典 Mac OS 9 系統下的單字符字形編輯工作窗口。展示了早期專業字體設計所依賴的參考基準輔助線與貝塞爾節點調控界面
![圖 12-2：Letraset FontStudio 在經典 Mac OS 9 系統下的單字符字形編輯工作窗口](/images/fonts-encodings/fig12-2.png)
*圖 12-2：Letraset FontStudio 在經典 Mac OS 9 系統下的單字符字形編輯工作窗口。展示了早期專業字體設計所依賴的參考基準輔助線與貝塞爾節點調控界面。*
:::

---

## 2. 現代工業標準霸主：FontLab Studio

由蘇聯裔天才程序員尤里·亞爾莫拉（Yuri Yarmola）於 1990 年代初創立的 **FontLab Studio**（由 SoftMaker 與 Fontlab Ltd. 聯合運營），在長達二十餘年的時間裏，無可爭辯地統治着全球各大商業字體廠商（如 Adobe、Linotype、Monotype、Bitstream）的工業生產流水線。

FontLab 深度整合了對 Type 1、TrueType、OpenType 以及 Multiple Master 格式的全功能原生支持，其核心工作流構建在高度專業化的“四大字符總覽視圖模式”之上：

### FontLab 字體總覽窗口的四大視圖模式

在 FontLab 的主字體管理窗口中，用户可以根據當前工程任務的側重點，自如切換四種完全不同的字符組織模式：

1. **Names 模式（字形名稱模式）**：依據標準 Adobe PostScript 字形命名規範（如 `A`, `acute`, `adieresis`, `hyphen`, `ampersand`）組織排列。這是傳統 PostScript 字體工程師最習慣的視角，直觀反映字形在排版引擎內部的符號命名樹。
2. **Pages 模式（編碼代碼頁模式）**：以經典的 256 字符單字節編碼頁（Code Page，如 Windows-1252 Latin 1、MacRoman、IBM CP437、ISO 8859 系列）為基準劃分。每個代碼頁被切分為整齊的 16×16 矩陣表格，極大地方便了設計者為特定舊式操作系統或區域市場快速排查字符缺漏。
3. **Ranges 模式（Unicode 字符塊模式）**：完全遵循 Unicode 聯盟官方劃分的標準字符集區間（Unicode Blocks / Ranges，如 Basic Latin、Latin-1 Supplement、Latin Extended-A、Greek and Coptic、Cyrillic 等）。在開發包含數千字符的大型泛歐或全球化通用 OpenType 字體時，該模式是必不可少的工作中樞。
4. **Index 模式（字形索引模式）**：直接以字體二進制文件內部的物理字形索引（Glyph Index, **GID**）為順序展示。在底層 TrueType/OpenType 結構中，GID 0 永遠固定指派給缺失符號（`.notdef`），隨後的各字形按其實際編譯進字體數據流中的物理先後次序自左向右嚴格遞增排列。

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

### 全面的排印度量與元數據架構（Font Properties）

設計字體絕不僅僅是畫出好看的矢量外形，更是一項極其繁重的技術元數據配置工程。在 FontLab 的“Font Info”（字體信息屬性面板）中，涵蓋了決定字體跨平台行為的關鍵標籤頁：

* **Names and Copyright（名稱與版權信息）**：遵循嚴格的 OpenType `name` 記錄規範（多達 20 餘種預定義字符串標識符），包括字體族名稱（Family Name）、樣式名稱（Style Name）、完整字模名稱（Full Font Name）、PostScript 內部名稱、獨一無二的唯一標識符（Unique Font Identifier）、版本號以及設計者商標與法律版權聲明（圖 12-7）。
* **Key Dimensions（核心排印度量尺寸）**：精確設定字體的全身身長網格（Units per em，通常 PostScript 設定為 1000，TrueType 設定為 2048）、大寫字母高度（Cap-Height）、小寫 x-高度（X-Height）、字體上行升幅（Ascender）、下行降幅（Descender）以及行距（Line Gap）（圖 12-8）。
* **Supported Codepages and Unicode Ranges（支持的代碼頁與 Unicode 範圍標誌位）**：直接對應 TrueType/OpenType 二進制規範中 `OS/2` 表的 128 位 `ulUnicodeRange` 掩碼與 64 位 `ulCodePageRange` 掩碼。這些比特位明確通知操作系統與文字渲染管線：本字體經過認證能夠完整支持哪些語言與國家標準！

::: tip 圖 12-7：FontLab 字體屬性面板：字體命名規範、版權信息及 OpenType 擴展名稱配置標籤頁
![圖 12-7：FontLab 字體屬性面板：字體命名規範、版權信息及 OpenType 擴展名稱配置標籤頁](/images/fonts-encodings/fig12-7.png)
*圖 12-7：FontLab 字體屬性面板：字體命名規範、版權信息及 OpenType 擴展名稱配置標籤頁。*
:::

::: tip 圖 12-8：FontLab 字體屬性面板：核心排印度量尺寸（Key dimensions）、支持代碼頁與 Unicode 覆蓋區間配置標籤頁
![圖 12-8：FontLab 字體屬性面板：核心排印度量尺寸（Key dimensions）、支持代碼頁與 Unicode 覆蓋區間配置標籤頁](/images/fonts-encodings/fig12-8.png)
*圖 12-8：FontLab 字體屬性面板：核心排印度量尺寸（Key dimensions）、支持代碼頁與 Unicode 覆蓋區間配置標籤頁。*
:::

---

## 3. 開源世界的傳奇旗幟：FontForge

在自由與開源軟件（FOSS）領域，由傳奇黑客**喬治·威廉姆斯**（George Williams）傾注畢生心血獨立打造的 **FontForge**（原名 **PfaEdit**），是一座令人肅然起敬的豐碑。

FontForge 基於 Unix/X11 圖形架構開發，以完全開放、完全無商業壁壘的姿態，實現了對當時市面上所有已知字體格式（Type 1, TrueType, OpenType, CID-keyed, CFF, SVG, BDF, PCF, UFO）的絕對全功能原生讀寫與無損交叉轉譯。更令學術界與排版極客痴迷的是：FontForge 深度內置了強大的 C 語言與 Python 腳本控制枱，允許開發者以純代碼方式批量自動化遍歷字體中數萬個字符的輪廓幾何拓撲，執行極其複雜的自動提示、座標圓整、輪廓布爾運算與字體健康診斷！

---

# 矢量輪廓的幾何與拓撲數學機理

數字字體本質上是由平面幾何中的參數化曲線閉合路徑所構成的數學矢量對象。在字體的微觀世界中，存在兩大並立又相互對立的數學技術流派：

## 1. PostScript 三次貝塞爾曲線 vs TrueType 二次 B-樣條

::: tip 圖 12-11：PostScript 三次貝塞爾曲線輪廓（左）與 TrueType 二次 B-樣條曲線輪廓（右）的幾何結構對比。實心黑點代表鏈上節點（On-curve nodes），白色空心圓點代表鏈外控制點（Off-curve control handles）
![圖 12-11：PostScript 三次貝塞爾曲線輪廓（左）與 TrueType 二次 B-樣條曲線輪廓（右）的幾何結構對比](/images/fonts-encodings/fig12-11.png)
*圖 12-11：PostScript 三次貝塞爾曲線輪廓（左）與 TrueType 二次 B-樣條曲線輪廓（右）的幾何結構對比。實心黑點代表鏈上節點（On-curve nodes），白色空心圓點代表鏈外控制點（Off-curve control handles）。*
:::

### PostScript 三次貝塞爾曲線（Cubic Bézier Splines, 3階）
由法國雷諾汽車工程師皮埃爾·貝塞爾（Pierre Bézier）在汽車車身設計中首創，後被 Adobe 採納為 PostScript 核心。
* **數學階數**：三階多項式方程：
  $$B(t) = (1-t)^3 P_0 + 3(1-t)^2 t P_1 + 3(1-t) t^2 P_2 + t^3 P_3, \quad t \in [0, 1]$$
* **節點結構**：每個獨立的曲線段必須嚴格由 **4 個座標點**決定：起始鏈上端點 $P_0$、第 1 控制手柄 $P_1$、第 2 控制手柄 $P_2$ 以及終止鏈上端點 $P_3$。
* **特性**：能夠以極少數量的控制點勾勒出極其飽滿、曲率變化自然且具有極高階導數連續性（$C^2$ 平滑度）的優雅藝術曲線，是專業字體設計師手工塑形的首選工具。

### TrueType 二次 B-樣條（Quadratic Splines, 2階）
由蘋果與微軟聯合制定的 TrueType 格式核心幾何規範。
* **數學階數**：二階多項式方程：
  $$B(t) = (1-t)^2 P_0 + 2(1-t)t P_1 + t^2 P_2, \quad t \in [0, 1]$$
* **節點結構**：每個獨立的拋物線弧段僅由 **3 個座標點**決定：起點 $P_0$、單個控制手柄 $P_1$ 以及終點 $P_2$。
* **隱式內插節點特性（Implicit On-Curve Points）**：為了極大壓縮 TrueType 字體文件在網絡與磁盤上的體積，TrueType 規範引入了絕頂聰明的存儲策略：**當兩個鏈外控制點（如 $P_1$ 與 $P_2$）在數據序列中連續相鄰出現時，渲染引擎將自動在兩點的絕對幾何中點處 $\frac{P_1 + P_2}{2}$，隱式內插一個虛擬鏈上端點**！如此一來，設計複雜的弧線時可以省略大量鏈上錨點的座標存儲。
* **特性**：由於僅涉及二階乘法運算，早期微處理器光柵化計算二次樣條的速度比計算三次曲線快數倍以上；但其缺點是需要更多的控制節點才能逼近同一段高階自由曲線。

---

## 2. 輪廓順逆走向與多邊形纏繞法則（Contour Direction & Winding Rules）

當一個字母（例如大寫 ‘O’ 或 ‘B’）包含外部邊緣與內部掏空的鏤空孔洞（Counters）時，光柵化引擎如何準確判定哪一部分應該填充油墨黑度、哪一部分必須保持透明空白？

圖形學主要採用**非零纏繞數規則**（Non-Zero Winding Rule）：從當前測試像素點向無窮遠處引出一條任意射線，當射線穿過一條從左向右（順時針）的輪廓曲線時，纏繞計數加 1；當穿過一條從右向左（逆時針）的曲線時，纏繞計數減 1。最終如果代數和非零，則填充黑色；若等於零，則保持透明。

這直接導致了字形輪廓走向的嚴格鐵律：**外輪廓與內腔輪廓的環繞方向必須絕對嚴格相反**！然而，令人頭疼的是，歷史上兩大巨頭在方向定義上恰恰水火不容：
* **PostScript Type 1 / OpenType (CFF)**：**外輪廓必須為順時針（Clockwise），內孔輪廓必須為逆時針（Counter-Clockwise）**！
* **TrueType / OpenType (TTF)**：**外輪廓必須為逆時針（Counter-Clockwise），內孔輪廓必須為順時針（Clockwise）**！

如果設計者在導出字體時搞錯了輪廓走向（Flipped Direction），文字在排版打印時很可能會發生可怕的“內部反色”、“實心黑坨”或在小字號光柵化時孔洞徹底粘連閉合等嚴重畸變！現代字體軟件均提供“Correct Direction”（校正輪廓走向）的自動化一鍵修復算法。

---

## 3. 極值點鐵律（Extremum Points）

在貝塞爾曲線幾何中，一條被所有資深字體大師與工業渲染引擎視為不可逾越的聖律便是：**必須在所有輪廓切線處於絕對水平（$dy/dt = 0$）與絕對垂直（$dx/dt = 0$）的最外邊緣頂點處，顯式安放鏈上節點（Extrema）**！

若違背此規則（例如在一個圓弧的左側最鼓點處不安放節點，而是用兩端斜向拉出的長控制手柄隔空跨越），將帶來一系列致命後果：
1. **微調提示（Hinting）徹底失效**：無論是 PostScript Stem Hints 還是 TrueType Grid-Fitting 字節碼指令，其對齊像素網格的前提都是捕獲水平或垂直極值點座標。缺少極值節點將導致低分辨率屏幕上出現嚴重的筆畫粗細不均、端點發虛或鋸齒暴碎。
2. **包圍盒計算失真**：部分老舊 RIP 打印機光柵化引擎在計算字形物理外接矩形（Bounding Box）時，為了節省算力，僅遍歷鏈上節點的最小/最大座標，缺少極值節點將導致字形邊緣在顯示或打印時被活生生截斷切平！

---

# 多重母版（Multiple Master）設計空間體系

在傳統排版中，一個字體家族若要包含從 Ultra Light（超細）到 Ultra Black（超黑）、從 Ultra Condensed（超窄）到 Ultra Expanded（超寬）等數十款字重與寬高變體，設計師往往需要日以繼夜地單獨雕琢每一個版式。

1991 年，Adobe 推出了革命性的**多重母版技術**（Multiple Master, **MM**）。設計師只需精心繪製處於多維設計空間極值角落上的若干個基準“母版字形”（Master Designs，例如圖 12-9 中的極細母版與極粗母版），計算機算法便能利用多維線性插值（Linear Interpolation），動態、無級、連續地衍生生成出成千上萬款擁有完美灰度與骨架過渡的衍生字體！

::: tip 圖 12-9：FontLab 中設計多重母版（Multiple Master）字體的工作窗口。同一畫板中同時疊映着極細母版與極黑母版的矢量輪廓骨架
![圖 12-9：FontLab 中設計多重母版（Multiple Master）字體的工作窗口](/images/fonts-encodings/fig12-9.png)
*圖 12-9：FontLab 中設計多重母版（Multiple Master）字體的工作窗口。同一畫板中同時疊映着極細母版與極黑母版的矢量輪廓骨架。*
:::

::: tip 圖 12-10：FontLab 中通過合併兩個獨立字體生成多重母版字體的配置窗口
![圖 12-10：FontLab 中通過合併兩個獨立字體生成多重母版字體的配置窗口](/images/fonts-encodings/fig12-10.png)
*圖 12-10：FontLab 中通過合併兩個獨立字體生成多重母版字體的配置窗口。*
:::

### 多重母版插值的嚴格數學相容性約束（Compatibility）
插值算法能夠在兩個母版之間流暢演算的前提，是兩者在數學拓撲上具有絕對的一一對應關係：
1. **完全相同數量的閉合輪廓（Contours）**；
2. **每個對應輪廓內部必須包含絕對完全相同數量的節點（Nodes）**；
3. **每個節點必須擁有完全相同的類型（平滑連接點 vs 角折點）**；
4. **兩者的起始節點（First Point）必須位於同一幾何特徵位置，且輪廓遍歷方向必須絕對相同**！

一旦某一個母版多了一個多餘的錨點，多重母版系統將斷然報錯拒絕生成。這一理念在今天演化為了現代數字排版王冠上的明珠——**可變字體**（OpenType Variable Fonts）。

---

# 位圖自動描摹與掃描字體（ScanFont）

許多經典的印刷字體復刻或古老書籍排印工程，始於對古籍原版的紙質掃描。由 FontLab 家族出品的專用工具 **ScanFont**，代表了數字字體領域位圖自動描摹（Autotracing）的最高專業水準。

::: tip 圖 12-12：ScanFont 軟件對掃描頁面進行自動字形切分與包圍框分離界面
![圖 12-12：ScanFont 軟件對掃描頁面進行自動字形切分與包圍框分離界面](/images/fonts-encodings/fig12-12.png)
*圖 12-12：ScanFont 軟件對掃描頁面進行自動字形切分與包圍框分離界面。*
:::

::: tip 圖 12-13：ScanFont 中實時動態配置自動描摹輪廓平滑度與抗噪參數的對話框
![圖 12-13：ScanFont 中實時動態配置自動描摹輪廓平滑度與抗噪參數的對話框](/images/fonts-encodings/fig12-13.png)
*圖 12-13：ScanFont 中實時動態配置自動描摹輪廓平滑度與抗噪參數的對話框。*
:::

::: tip 圖 12-14：手工精準雕琢輪廓（左）與兩款採用不同平滑參數自動描摹輪廓（中、右）的顯微幾何對比。清晰展現了算法自動擬合在極小拐角與弧度轉折處不可避免產生的多餘冗餘噪點
![圖 12-14：手工精準雕琢輪廓（左）與兩款採用不同平滑參數自動描摹輪廓（中、右）的顯微幾何對比](/images/fonts-encodings/fig12-14.png)
*圖 12-14：手工精準雕琢輪廓（左）與兩款採用不同平滑參數自動描摹輪廓（中、右）的顯微幾何對比。清晰展現了算法自動擬合在極小拐角與弧度轉折處不可避免產生的多餘冗餘噪點。*
:::

通過圖 12-14 的顯微對比，作者給出了極具警示意義的技術箴言：**無論計算機的位圖邊緣偵測與貝塞爾擬合算法多麼強大，自動描摹生成的輪廓永遠充滿着多餘的鋸齒噪點、缺少正交極值點，且控制點分佈極度紊亂**。因此，自動描摹只能作為起草參考底稿，一位追求卓越的字體工匠，最終必須以虔誠的耐心，親手在關鍵極值點處逐一落筆雕琢每一根優雅勻稱的貝塞爾矢量曲線！

---

# 結語

字體的數字化創造，是人類理性邏輯與感性美學最深沉的結晶。從屏幕上輕輕拖動的一個控制手柄，到底層微處理器執行的樣條微積分方程；從字形間距的一微米妥協，到 OpenType 表結構中精密咬合的幾千個數據字節——正是現代字體設計軟件與背後嚴謹科學體系的交融，賦予了文字跨越時空、在數字文明中永遠清晰綻放的永恆力量。
