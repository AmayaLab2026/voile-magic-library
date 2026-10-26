---
description: 雅尼斯·哈拉蘭布斯《Fonts & Encodings》附錄 A–G 全文深度學術漢譯：數字字體底層格式、虛擬機與數學基礎完全技術參考手冊。涵蓋點陣位圖字體格式（Macintosh FONT/NFNT、Windows FNT/FON、Unix BDF/PCF、TeX PK/GF）、TeX 與 Omega 度量體系（TFM/OFM/VF/OVF）、PostScript Type 1 二進制架構與 eexec 密碼學、Multiple Master 多主控字體、CIDFont 架構、TrueType/OpenType/AAT 底層表結構全字典、TrueType 虛擬機指令集、METAFONT 語言數學參數以及三次貝塞爾曲線德卡斯特里奧細分算法。
---

# 附錄 A–G · 數字字體底層格式、虛擬機與數學基礎完全技術參考手冊
### Appendices A–G: Technical Reference Manual
**著者：雅尼斯·哈拉蘭布斯 博士（Yannis Haralambous, Ph.D.）**  
**英譯與增訂：P. 斯科特·霍恩 博士（P. Scott Horne, Ph.D.）**  
*選自《字體與編碼》（Fonts & Encodings）原著第 599–990 頁*

---

# 附錄 A：點陣位圖字體格式（Bitmap Font Formats）

*譯者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

在輪廓向量字體（Outline Vector Fonts）統治數字排印世界之前，計算機屏幕與點陣打印機完全依賴離散的點陣位圖（Bitmap）呈現文字。瞭解這些古老的二進制位圖格式，是洞悉操作系統字體子系統進化史的鑰匙。

## A.1 經典 Macintosh 體系：FONT 與 NFNT 資源結構

在經典 Mac OS（System 1 至 Mac OS 9）中，位圖字體作爲資源分支（Resource Fork）中的資源存儲，其資源類型標籤爲 `'FONT'` 或 `'NFNT'`（New Font）。

每個字號的點陣數據被打包爲一個連續的水平 1-bit 位圖條帶（Bitmap Strike）。字體的所有字形被橫向拼接在同一個條帶內，並輔以偏移表（Offset Table）與寬度表（Width Table）來界定每個字形的左右邊界。

::: tip 圖版 A-1：經典 Macintosh 操作系統 Chicago 字體的連續位圖條帶 (Figure A-1)
![Figure A-1: The global image of the font Chicago](/images/fonts-encodings/fig-app-a1.png)
*圖版 A-1：二十多年來長盛不衰的 Macintosh 系統界面字體 Chicago 的全局點陣條帶（選自原著第 621 頁）。所有字形水平無縫緊貼排列，字身間距完全通過底層的位圖度量表進行尋址切分。*
:::

## A.2 DOS、Windows 與 Unix 點陣字體標準

### 1. DOS CPI 格式
在 MS-DOS 環境下，顯示器與打印機的硬件點陣字體被封裝在 `.CPI`（Code Page Information）容器中，內含針對 EGA/VGA 顯示卡特製的 $8 	imes 8$、$8 	imes 14$ 與 $8 	imes 16$ 像素點陣字模。

### 2. Windows FNT 與 FON 格式
Windows 1.0 至 3.x 引入了 `.FNT`（單個位圖字形資源）與 `.FON`（封裝在 16 位 NE 架構 DLL 中的點陣字庫）。其內部包含字形位移矩陣、字頭元數據與字符映射表。

### 3. Unix 與 X11 體系：Adobe BDF 與 PCF 格式
在 Unix/X Window 系統中，**BDF（Bitmap Distribution Format）** 是一種基於 ASCII 純文本的可移植位圖字體交換格式。

::: tip 圖版 A-2：Adobe BDF 格式點陣字形的點陣矩陣結構 (Figure A-2)
![Figure A-2: BDF's vision of the bitmap and vector versions of an ideograph](/images/fonts-encodings/fig-app-a2.png)
*圖版 A-2：Adobe BDF 規範中單個漢字表意文字的位圖矩陣與度量框架（選自原著第 629 頁）。清晰展示了字符邊框（Bounding Box）、位移向量（DWIDTH/SWIDTH）以及點陣星號與原點基線座標系。*
:::

在系統實際加載時，BDF 通常會被二進制編譯爲 **PCF（Portable Compiled Format）** 或 **SNF（Server Natural Format）**，以實現內存映射（mmap）級別的急速讀取。

## A.3 TEX 體系的點陣輸出：GF 與 PK 格式

在 Donald Knuth 的 TeX 排版世界中，METAFONT 編譯器首先輸出通用的 **GF（Generic Font）** 二進制文件。隨後通過 `gftopk` 工具將其深度壓縮爲緊湊的 **PK（Packed Font）** 格式。

::: tip 圖版 A-3：METAFONT 輸出的 gftodvi 高分辨率字模印樣 (Figure A-3)
![Figure A-3: A page from the DVI file produced by gftodvi from Computer Modern Roman 10](/images/fonts-encodings/fig-app-a3.png)
*圖版 A-3：通過 gftodvi 工具從 Computer Modern Roman 10pt 的 GF 文件生成的像素級宏觀印樣（選自原著第 638 頁）。展示了小寫字母 'a' 在像素網格上的精確骨架、控制點與像素填充分佈。*
:::

---

# 附錄 B：TEX 與 Omega 字體格式規範（TFM, OFM, VF）

TeX 排版系統具有極其超前的“排版與渲染徹底解耦”的工程哲學。TeX 引擎在進行段落折行與數學公式排版時，**完全不需要讀取任何字形輪廓或位圖像素**，它只需要精確知曉每個字符的宏觀幾何度量（外框盒尺寸、字偶距、連字規則與光學尺寸修正）。

## B.1 TFM（TEX 字體度量表）二進制數據結構

每個 TeX 字體度量文件（`.tfm`）由 16 位大端無符號整數構建，邏輯上嚴密劃分爲以下十個連續的數據區：

| 數據區索引 | 名稱 | 內容與作用 |
| :--- | :--- | :--- |
| 1 | `header` | 校驗和（Checksum）、設計字號（Design Size）以及排版編碼方案字符串 |
| 2 | `char_info` | 字符索引表：寬度索引（`width_index`）、高度與深度索引（`height_depth_index`）、斜體修正索引（`italic_index`）及標籤字段 |
| 3 | `width` | 字身寬度數組（以定點數 `fix_word` 存儲） |
| 4 | `height` | 字符基線上方高度數組 |
| 5 | `depth` | 字符基線下方深度數組 |
| 6 | `italic` | 斜體傾斜角與斜體空間修正量數組 |
| 7 | `lig_kern` | 連字與字偶間距狀態轉移微指令虛擬機程序（Ligature/Kerning Table） |
| 8 | `kern` | 物理字偶間距數值表 |
| 9 | `exten` | 大型數學延展字符裝配描述表（如括號、積分號的分段拼接構件） |
| 10 | `param` | 字體全局排版參數數組（`fontdimen`），包含空格基準寬度、拉伸量、收縮量、x-高度與數學軸高度 |

### 核心定點數表示：`fix_word`
TFM 文件中所有的幾何尺寸全部採用 Knuth 獨創的 32 位二進制補碼定點數 `fix_word` 表示。其中高 12 位表示整數部分，低 20 位表示小數部分。其絕對基準單位爲字體的設計字號（$1.0 = 2^{20} = 1048576$ 個內部單位）。這種精妙的設計使得 TeX 的幾何排版計算在任何硬件架構上均能保證絕對一致、分毫不差的跨平臺可復現性！

## B.2 Omega OFM 與虛擬字體（VF）體系

爲了突破 TFM 僅支持 256 個字符的先天瓶頸，Omega 項目引入了 **OFM（Omega Font Metrics）**，將字符索引拓展至 16 位甚至 32 位 Unicode 全域。

而 **VF（Virtual Font，虛擬字體）** 則允許排版引擎將來自不同物理字體的字形組合拼裝爲單一的邏輯字體。通過 VF 字節碼，排版引擎可以在運行時動態完成字形縮放、位移、疊加甚至旋轉，實現了現代複合字體的早期雛形。

---

# 附錄 C：PostScript Type 1 字體二進制架構與 eexec 密碼學

Adobe 的 PostScript Type 1 字體是現代矢量排印文明的基石。

## C.1 PostScript 路徑追蹤與着色規則

PostScript 解釋器通過貝塞爾曲線指令描述輪廓，並採用“非零環繞數規則（Nonzero Winding Number Rule）”來判定封閉區域的內外着色屬性。

::: tip 圖版 C-1：PostScript 路徑追蹤與形狀填充範例 (Figure C-1)
![Figure C-1: Examples of PostScript code: tracing a path, filling a shape](/images/fonts-encodings/fig-app-c1.png)
*圖版 C-1：PostScript 矢量代碼示例：路徑構建、描邊與形狀填充（選自原著第 662 頁）。*
:::

::: tip 圖版 C-2：非零環繞數着色規則的幾何判定邏輯 (Figure C-2)
![Figure C-2: Examples of filling according to the nonzero winding number rule](/images/fonts-encodings/fig-app-c2.png)
*圖版 C-2：非零環繞數規則（Nonzero Winding Number Rule）的幾何判定（選自原著第 663 頁）。通過向外引出射線統計輪廓環繞方向代數和，精準識別孔洞與複合填充區域。*
:::

## C.2 文本渲染算子與 Scrabble 字體

PostScript 提供了豐富的文本輸出算子，包括基礎的 `show`、用於字符間距均勻擴展的 `ashow` 以及爲每個字形賦予獨立座標位移的 `xyshow`。

::: tip 圖版 C-3：PostScript show 算子及其間距擴展變體 (Figure C-3)
![Figure C-3: The show operator and variants: ashow, xyshow](/images/fonts-encodings/fig-app-c3.png)
*圖版 C-3：`show` 算子及其變體 `ashow`（字距微調拉伸）與 `xyshow`（獨立字寬平衡）（選自原著第 667 頁）。*
:::

::: tip 圖版 C-4：雅克·安德烈設計的 Scrabble 拼字遊戲 Type 3 字體 (Figure C-4)
![Figure C-4: The font Scrabble, by Jacques André](/images/fonts-encodings/fig-app-c4.png)
*圖版 C-4：法國排印大師雅克·安德烈（Jacques André）設計的 Scrabble 拼字遊戲 Type 3 字體（選自原著第 675 頁）。同一文檔的連續四次打印展現了完全隨機化的木質紋理與字偶微顫效果。*
:::

## C.3 編碼表與字形輪廓度量

::: tip 圖版 C-5：Adobe 標準字體編碼表（StandardEncoding） (Figure C-5)
![Figure C-5: The Adobe Standard font encoding, illustrated with Monotype Columbus](/images/fonts-encodings/fig-app-c5.png)
*圖版 C-5：Adobe Standard 字體編碼規範，以 Monotype Columbus 字體展示（選自原著第 681 頁）。*
:::

::: tip 圖版 C-6：Adobe 專家級字體編碼表（ExpertEncoding） (Figure C-6)
![Figure C-6: The Adobe Expert font encoding, illustrated with Monotype Columbus Expert](/images/fonts-encodings/fig-app-c6.png)
*圖版 C-6：Adobe Expert 專家級擴展編碼規範，包含真正的小型大寫字母、老式數字與連字（選自原著第 681 頁）。*
:::

::: tip 圖版 C-7：各文字書寫系統中的相關高度與超出量度量 (Figure C-7)
![Figure C-7: The relevant heights, with overshoot, of various script glyphs](/images/fonts-encodings/fig-app-c7.png)
*圖版 C-7：拉丁文、阿拉伯文等文字中字形的光學超出量（Overshoot）、基線、大寫高度與降部線度量（選自原著第 683 頁）。*
:::

::: tip 圖版 C-8：The Sans Mono Condensed Light 字體中小寫字母 'e' 的輪廓描述 (Figure C-8)
![Figure C-8: Description of the glyph 'e' in The Sans Mono Condensed Light](/images/fonts-encodings/fig-app-c8.png)
*圖版 C-8：Luc(as) de Groot 設計的 The Sans Mono 中字母 'e' 的絕對矢量輪廓與三次樣條分段（選自原著第 686 頁）。*
:::

## C.4 PostScript Hints（微調提示）體系

爲了在低分辨率設備（如 72–150 DPI 屏幕或早期的 300 DPI 激光打印機）上保持字莖寬度一致並防止字形黑度失真，Type 1 規範引入了一套優雅的微調指令系統。

::: tip 圖版 C-9：字母 H、O、m 的潛在微調提示區（Hint Zones） (Figure C-9)
![Figure C-9: Potential hints for the letters 'H', 'O', and 'm'](/images/fonts-encodings/fig-app-c9.png)
*圖版 C-9：字母 'H'、'O' 與 'm' 的微調提示區間（選自原著第 688 頁）。灰色區域代表需要鎖定的主幹筆畫寬度。*
:::

::: tip 圖版 C-10：字母 'B' 中替換四個微調提示的執行邏輯 (Figure C-10)
![Figure C-10: Replacing four hints in the letter 'B'](/images/fonts-encodings/fig-app-c10.png)
*圖版 C-10：在繪製複雜字形 'B' 時動態替換微調提示（Hint Replacement）（選自原著第 689 頁）。*
:::

::: tip 圖版 C-11：由兩條三次貝塞爾曲線構成的 Flex 淺曲率控制 (Figure C-11)
![Figure C-11: Flex formed by two cubic Bézier curves](/images/fonts-encodings/fig-app-c11.png)
*圖版 C-11：由兩條三次貝塞爾曲線拼接構成的 Flex 機制（選自原著第 690 頁），用於防止極其平緩的弧線在低分辨率下退化爲生硬的階梯鋸齒或直線。*
:::

::: tip 圖版 C-12：PostScript Type 1 字體的對沖控制（Counter Controls） (Figure C-12)
![Figure C-12: Counter controls of PostScript Type 1 fonts](/images/fonts-encodings/fig-app-c12.png)
*圖版 C-12：Type 1 字體的內白對沖控制機制（選自原著第 692 頁），確保 'm' 等多豎畫字母在極小字號下內部白空間保持均等。*
:::

::: tip 圖版 C-13：Times-Roman 在不同字號下的字距微調變化曲線 (Figure C-13)
![Figure C-13: Two examples of letterspacing in Times-Roman](/images/fonts-encodings/fig-app-c13.png)
*圖版 C-13：Times-Roman 在 5pt 至 15.5pt 之間的字距微調軌跡（TrackKern）對比（選自原著第 696 頁）。*
:::

## C.5 Multiple Master 字體與四維設計空間

Adobe 的 Multiple Master（MM）技術允許字體設計師構建一個連續的多維設計空間（Design Space）。通過在軸的兩極甚至中間設定母版字形（Master Designs），計算機可以在運行時根據用戶的任意參數進行多維線性插值。

::: tip 圖版 C-14：Adobe Kepler MM 字體中字母 'A' 的八個核心設計母版 (Figure C-14)
![Figure C-14: Eight master designs of the glyph 'A' in Adobe Kepler MM](/images/fonts-encodings/fig-app-c14.png)
*圖版 C-14：Adobe Kepler MM 字體中字母 'A' 圍繞“字重（Weight）”、“字寬（Width）”與“光學字號（Optical Size）”三維立方體分佈的 8 個極端設計母版與中間插值形態（選自原著第 698 頁）。*
:::

## C.6 OCF 與 CIDFont 架構

爲了滿足東亞中日韓（CJK）成千上萬個漢字表意文字的排版需求，Adobe 先後研發了 OCF（Original Composite Format）與劃時代的 **CIDFont** 架構。CIDFont 將字符編碼（CMap）與字形輪廓（CIDFont 文件）徹底分離，每個字形通過一個全局唯一的純數字索引（CID, Character Identifier）尋址。

::: tip 圖版 C-15：經典 OCF 複合字體的雙層尋址機制 (Figure C-15)
![Figure C-15: How OCF fonts work](/images/fonts-encodings/fig-app-c15.png)
*圖版 C-15：經典 OCF 字體的嵌套字典與雙字節尋址模型（選自原著第 706 頁）。*
:::

::: tip 圖版 C-16：CIDFont 文件（CID Type 0）的全局拓撲結構 (Figure C-16)
![Figure C-16: Overall structure of a CIDFont file (CID type 0)](/images/fonts-encodings/fig-app-c16.png)
*圖版 C-16：CIDFont 二進制文件（Type 0）的全局拓撲結構與解釋器尋址路徑（選自原著第 709 頁）。*
:::

::: tip 圖版 C-17：Type 2 Charstrings 中的高階微調掩碼管理 (Figure C-17)
![Figure C-17: Hint management in charstrings of Type 2](/images/fonts-encodings/fig-app-c17.png)
*圖版 C-17：Type 2 Charstrings 中的高階微調掩碼管理（選自原著第 723 頁）。展示了從左至右在複雜漢字“講”（11 條水平莖微調）中的微調掩碼切換。*
:::

---

# 附錄 D：TrueType、OpenType 與 AAT 二進制表結構完全字典

TrueType 與 OpenType 字體文件在底層由一個根目錄（Table Directory）和若干獨立的二進制表（Tables）構成。

## D.1 點陣與設備度量表

::: tip 圖版 D-1：EBLC 表中點陣字形的水平與垂直度量幾何模型 (Figure D-1)
![Figure D-1: Horizontal and vertical metrics of a bitmap glyph in an EBLC table](/images/fonts-encodings/fig-app-d1.png)
*圖版 D-1：TrueType EBLC 表中內嵌點陣字形的水平與垂直度量幾何參數（選自原著第 756 頁）。*
:::

::: tip 圖版 D-2：中文文本在 12 ppem 與 24 ppem 下的點陣渲染對比 (Figure D-2)
![Figure D-2: Comparison of Chinese text rendered at 12 and 24 ppem](/images/fonts-encodings/fig-app-d2.png)
*圖版 D-2：中文漢字文本在 12 像素/em 與 24 像素/em 下的點陣微調效果對比（選自原著第 760 頁）。*
:::

::: tip 圖版 D-3：Verdana 字體字母 'A' 像素字寬隨 ppem 的階梯分佈 (Figure D-3)
![Figure D-3: Distribution of sizes in pixels of the letter 'A' from Verdana](/images/fonts-encodings/fig-app-d3.png)
*圖版 D-3：Verdana 字體字母 'A' 在 `hdmx` 表中隨字號變化的離散像素寬度曲線（選自原著第 764 頁）。*
:::

## D.2 佈局查找與草體連接

::: tip 圖版 D-4：OpenType 草體連接附着（Cursive Attachment）查找標誌 (Figure D-4)
![Figure D-4: Two examples of cursive attachment lookup flag](/images/fonts-encodings/fig-app-d4.png)
*圖版 D-4：在烏爾都文納斯塔裏克草體排版中使用 Cursive Attachment 查找標誌的基線錨定效果（選自原著第 788 頁）。*
:::

::: tip 圖版 D-5：帶哈姆扎的阿拉伯字母 Yeh Barree 的字形變異與連字歷程 (Figure D-5)
![Figure D-5: The glorious fate of arabic letter yeh barree with hamza above](/images/fonts-encodings/fig-app-d5.png)
*圖版 D-5：字符 U+06D3 在經歷 GSUB 替換後的宏偉歷程（選自原著第 804 頁）。*
:::

::: tip 圖版 D-6：Ampersands 字體族中的 202 種＆字符設計變體 (Figure D-6)
![Figure D-6: The 202 ampersands of AmpersandsOne and AmpersandsTwo](/images/fonts-encodings/fig-app-d6.png)
*圖版 D-6：由美國排印協會整理的 Ampersands 字體中收錄的 202 種古典與現代連字符變體全貌（選自原著第 806 頁）。*
:::

::: tip 圖版 D-7：赫爾曼·察普夫 Zapfino 字體排印的三語情詩 (Figure D-7)
![Figure D-7: A trilingual and tri-fontal love poem in Zapfino](/images/fonts-encodings/fig-app-d7.png)
*圖版 D-7：採用大師察普夫設計的 Zapfino 排印的三語三字體經典愛情詩篇（選自原著第 861 頁），生動展現了極端字偶側邊距與上下交織花體。*
:::

::: tip 圖版 D-8：Apple Skia 字體在 wght 字重軸上的連續變異 (Figure D-8)
![Figure D-8: Apple Skia variations along the wght axis](/images/fonts-encodings/fig-app-d8.png)
*圖版 D-8：Apple AAT Skia 字體在 `wght` 字重軸上的無縫平滑形變（選自原著第 873 頁）。*
:::

## D.3 AAT 有限狀態自動機轉移模型

::: tip 圖版 D-9：AAT 確定性有限狀態自動機的兩個典型狀態轉移模型 (Figure D-9)
![Figure D-9: Two examples of finite automata](/images/fonts-encodings/fig-app-d9.png)
*圖版 D-9：AAT 狀態轉移自動機模型示例（選自原著第 878 頁）。橢圓代表狀態節點，有向箭頭代表由輸入字符類別驅動的狀態遷移。*
:::

::: tip 圖版 D-10：帶有雙初始狀態的增強型 AAT 自動機模型 (Figure D-10)
![Figure D-10: Finite automaton with an additional initial state](/images/fonts-encodings/fig-app-d10.png)
*圖版 D-10：增加了專門針對行首（Beginning of Line）與行中上下文識別的增強型 AAT 有限狀態自動機（選自原著第 881 頁）。*
:::

---

# 附錄 E：TrueType 虛擬機指令集完全參考手冊（Instruction Set）

TrueType 字體包含一個圖靈完備的虛擬處理器內核。每個字形內部包含一段前微調字節碼程序。解釋器通過操縱控制點網格、執行投影與測量向量投影、以及調整局部自由度，實現極其精湛的屏幕像素點對齊。

::: tip 圖版 E-1：Courier 字體字母 'T' 的底層控制點拓撲 (Figure E-1)
![Figure E-1: The 'T' of TrueType Courier with instructions](/images/fonts-encodings/fig-app-e1.png)
*圖版 E-1：Apple/Bitstream Courier 字體字母 'T' 的原始控制點網格（選自原著第 913 頁）。*
:::

::: tip 圖版 E-2：Verdana 字體字母 'O' 的虛擬機指令執行序列 (Figure E-2)
![Figure E-2: The 'O' from TrueType Verdana with instructions](/images/fonts-encodings/fig-app-e2.png)
*圖版 E-2：微軟經典屏幕字體 Verdana 中字母 'O' 的微調指令執行與像素舍入鎖定過程（選自原著第 922 頁）。*
:::

---

# 附錄 F：METAFONT 語言與三次樣條微分幾何

高德納（Donald E. Knuth）創立的 METAFONT 語言是計算機字體學史上最深邃的數學豐碑。在 METAFONT 中，字符不再是靜態繪製的輪廓多邊形，而是一個由嚴格代數方程與微分幾何參數共同驅動的“動態活字程序”。

::: tip 圖版 F-1：經典 Computer Modern 字體家族全集（第 1 部分） (Figure F-1)
![Figure F-1: The fonts of the original Computer Modern distribution (1/2)](/images/fonts-encodings/fig-app-f1.png)
*圖版 F-1：TeX 原始發行版所包含的 Computer Modern 字體家族矩陣：羅馬正體、傾斜體、無襯線體與粗體印樣（選自原著第 958 頁）。*
:::

::: tip 圖版 F-2：經典 Computer Modern 字體家族全集（第 2 部分） (Figure F-2)
![Figure F-2: The fonts of the original Computer Modern distribution (2/2)](/images/fonts-encodings/fig-app-f2.png)
*圖版 F-2：Computer Modern 字體家族的等寬打字機體、數學斜體與特殊符號印樣（選自原著第 959 頁）。*
:::

::: tip 圖版 F-3：Computer Modern 字體家族的 62 個底層物理幾何參數全景 (Figure F-3)
![Figure F-3: The parameters of the Computer Modern fonts](/images/fonts-encodings/fig-app-f3.png)
*圖版 F-3：驅動 Computer Modern 生成的三次樣條核心物理參數圖解（選自原著第 961 頁）：涵蓋 x-高度、降部深度、主幹粗細（`stem`）、髮絲細線（`hair`）、圓點直徑（`dot_size`）與襯線傾角（`serif_drop`）。*
:::

::: tip 圖版 F-4：METAFONT weed 交互式樣條設計調試器界面 (Figure F-4)
![Figure F-4: The window of weed showing METAFONT glyph design](/images/fonts-encodings/fig-app-f4.png)
*圖版 F-4：在專用圖形交互軟件 `weed` 中調試由三次樣條方程生成的 METAFONT 動態字形輪廓（選自原著第 967 頁）。*
:::

::: tip 圖版 F-5：波蘭古典字體 Antykwa Półtawskiego 數字化發行版印樣 (Figure F-5)
![Figure F-5: The fonts of the Antykwa Półtawskiego distribution](/images/fonts-encodings/fig-app-f5.png)
*圖版 F-5：基於 METAFONT 參數化重建的波蘭民族排印瑰寶 Antykwa Półtawskiego 字體家族（選自原著第 977 頁）。*
:::

::: tip 圖版 F-6：Antykwa Półtawskiego 字體家族的核心微分參數骨架 (Figure F-6)
![Figure F-6: The parameters of the Antykwa Półtawskiego font family](/images/fonts-encodings/fig-app-f6.png)
*圖版 F-6：Antykwa Półtawskiego 字體家族的特徵參數矩陣圖解（選自原著第 979 頁）。*
:::

---

# 附錄 G：貝塞爾曲線的數學性質與德卡斯特里奧算法

數字字體的輪廓本質上是分段三次多項式樣條曲線。

## G.1 伯恩斯坦多項式與基底定義

設平面上有 $n+1$ 個控制點 $P_0, P_1, \dots, P_n$。對應的 $n$ 次貝塞爾曲線 $B(t)$ 定義爲：
$$B(t) = \sum_{i=0}^n B_{i,n}(t) P_i, \quad t \in [0, 1]$$
其中伯恩斯坦基底多項式（Bernstein Polynomials）$B_{i,n}(t)$ 爲：
$$B_{i,n}(t) = \binom{n}{i} t^i (1-t)^{n-i}$$

在字體工程中，PostScript Type 1、OpenType CFF 以及 TrueType（採用二次曲線並升階計算）普遍採用三次貝塞爾曲線（$n=3$）：
$$B(t) = (1-t)^3 P_0 + 3(1-t)^2 t P_1 + 3(1-t) t^2 P_2 + t^3 P_3$$

## G.2 核心數學性質

1. **仿射不變性（Affine Invariance）**：對曲線進行任何平移、旋轉、縮放或剪切變換，等價於直接對其控制多邊形進行相同的變換。
2. **凸包性（Convex Hull Property）**：整條曲線完全被其控制多邊形構成的凸包（Convex Hull）所包覆。排版渲染引擎在進行字體外框碰撞檢測（Bounding Box Clipping）時，無需計算樣條方程，只需對控制點外框求極值即可實現極高效的裁剪。
3. **端點插值與切線幾何**：曲線嚴格經過起點 $P_0$ 和終點 $P_3$，且端點處的切線方向精確平行於第一段向量 $P_1 - P_0$ 與最後一段向量 $P_3 - P_2$：
   $$B'(0) = 3(P_1 - P_0), \quad B'(1) = 3(P_3 - P_2)$$
4. **變差縮減性（Variation Diminishing Property）**：任何平面直線與貝塞爾曲線的交點數量，絕不會超過該直線與控制多邊形的交點數量。這從數學上保證了曲線絕不會發生莫名其妙的額外劇烈振盪。

## G.3 德卡斯特里奧細分算法（De Casteljau's Algorithm）

**德卡斯特里奧算法（De Casteljau's Algorithm）** 是一種純粹基於簡單線性插值的數值穩定計算框架。對於任意給定參數 $t \in [0, 1]$，算法通過迭代構建點序列：
$$P_i^{[0]} = P_i$$
$$P_i^{[k]} = (1-t) P_i^{[k-1]} + t P_{i+1}^{[k-1]}, \quad k = 1, \dots, n, \quad i = 0, \dots, n-k$$

當 $k=n$ 時，最終收斂點 $P_0^{[n]}$ 恰好等於曲線在 $t$ 處的座標 $B(t)$！更重要的是，中間生成的控制點序列：
* 左半段控制點：$P_0^{[0]}, P_0^{[1]}, P_0^{[2]}, P_0^{[3]}$
* 右半段控制點：$P_0^{[3]}, P_1^{[2]}, P_2^{[1]}, P_3^{[0]}$

直接將原三次貝塞爾曲線精確細分爲兩段獨立的無縫銜接三次曲線。光柵化渲染引擎（Rasterizer）以此爲基礎執行自適應遞歸二分細分（Recursive Subdivision），直至每一小段曲線與直線線段的離散誤差小於單個像素點尺寸，從而以驚人的極速完成抗鋸齒位圖光柵化！

---

# 結語

至此，我們完成了對雅尼斯·哈拉蘭布斯教授鴻篇鉅製《Fonts & Encodings》全部十四章及附錄 A–G 的全方位技術參考漢譯。從人類最原始的鉛活字物理力學，到統一萬象的 Unicode 編碼空間；從經典桌上操作系統的字庫總線，到現代網絡動態排印與 SVG 矢量流；從貝塞爾曲線的微分幾何數學，到虛擬機圖靈完備的微調邏輯——數字字體不僅是計算機科學與工程算法的結晶，更是人類文字文明在硅基時代得以永續傳承的宏偉殿堂！
