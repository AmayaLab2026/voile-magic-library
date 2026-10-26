---
title: "附錄 A–G：底層格式與數學全景技術參考手冊"
description: "涵蓋點陣圖字型 (A)、TeX/Omega (B)、PostScript Type 1/CFF (C)、TrueType/OpenType 表目錄 (D)、METAFONT (E)、TrueType 虛擬機器指令集 (F) 與曲線微分幾何 (G)。"
---

# 附錄 A–G ：底層格式與數學全景技術參考手冊
### Appendices A–G: Technical Reference Manual for Digital Typography
選自《Fonts & Encodings》第 599–938 頁（共 340 頁技術附錄）
*譯者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

本參考手冊涵蓋了《Fonts & Encodings》後半部全部七大技術附錄（Appendices A 至 G）。這部分內容是雅尼斯·哈拉蘭博斯（Yannis Haralambous）為數字字型工程師、底層排版引擎開發者以及計算機文字學學者構建的技術基石。它詳盡記錄了從 20 世紀 80 年代點陣點陣圖格式到 21 世紀現代 OpenType/AAT 容器表結構、虛擬機器指令集與曲線微分幾何的全部數學實現。

---

# 附錄 A：點陣圖字型格式（Bitmap Font Formats）

儘管向量輪廓字型已全面統治現代螢幕與印刷出版，但點陣圖字型（Bitmap Fonts）作為計算機圖形學與數字排版的原初形態，依然在嵌入式作業系統、BIOS 韌體、終端模擬器以及字型的點陣內嵌子集（如 EBDT/EBLC 表）中扮演著不可替代的角色。

## A.1 蘋果 Macintosh 體系：FONT 與 NFNT 資源結構

在經典 Mac OS（System 1.0 至 Mac OS 9）中，字型被封裝為資源分支（Resource Fork）中的資源。

### 1. `FONT` 與 `NFNT` 資源頭結構
`FONT` 是早期固定字號點陣資源，`NFNT`（New Font Numbering Table）則是擴充了龐大家族編號體系的演進版本。兩者在記憶體中展開為相同的二進位制資料結構：

```c
struct FontRec {
    short fontType;       // 字型型別標誌位（包含比例/等寬、顏色等屬性）
    short firstChar;      // 字符集中第一個字元的 ASCII 碼點（通常為 0 或 32）
    short lastChar;       // 最後一個字元的碼點（通常為 255）
    short widMax;         // 整個字型中字元的最大寬度（畫素）
    short kernMax;        // 最大負向字距調整量（通常 <= 0）
    short nDescent;       // 字元基線以下的負向下沉深度（負數）
    short fRectWidth;     // 字元包圍盒矩形的最大寬度
    short fRectHeight;    // 字元包圍盒矩形的最大高度
    short owTLoc;         // 偏移/寬度表（Offset/Width Table）相對於表頭的字偏移量
    short ascent;         // 基線至大寫字母頂部的上升高度
    short descent;        // 基線至降部底部的下降深度
    short leading;        // 行間額外留白
    short rowWords;       // 點陣連續影象行寬（以 16 位整數字為單位）
    // 隨後緊跟：
    // 1. Bitmaps Array: 所有字元點陣橫向拼接而成的連續點陣圖條帶（Strike-font）
    // 2. LocTable: 字元在點陣圖條帶中的水平列起始偏移索引表
    // 3. OwTable: 字元邏輯寬度與字距微調偏移表
};
```

### 2. 條帶字型（Strike-font）影象模型
Macintosh 採取了一種極其超前的記憶體佈局：**它不為每個字元單獨開闢離散矩形，而是將整套字符集的所有畫素點陣並排焊接為一條連續的橫向影象條帶（Strike-font Bitmap）**。
- `rowWords` 規定了整個點陣條帶單行的 16 位整數寬度；
- `LocTable` 記錄了字元 $c$ 在條帶中起始的水平畫素列偏移 $x_c$ 與終止列偏移 $x_{c+1}$；
- 繪製字元時，Mac 顯示卡驅動只需透過一行極簡的位塊傳輸指令（BitBlt），即可將該列區間的矩形畫素切片直投到視訊記憶體中，獲得了 20 世紀 80 年代極速的文字渲染效能。

---

## A.2 DOS、Windows 與 Unix 體系標準

### 1. DOS CPI 格式（Code Page Information）
MS-DOS 透過 `MODE CON CP PREP` 命令載入的螢幕點陣字型被封裝在 `.CPI` 檔案中。CPI 內部包含字型檔案頭（Font File Header）、內碼表條目頭（CPEntryHeader）以及各個解析度螢幕（如 EGA 8×14、VGA 8×16、CGA 8×8）的裸點陣位元組塊。每個字元佔用連續的 16 位元組（8×16 點陣每行 1 位元組）。

### 2. Windows FNT 與 FON 格式
- **`.FNT` 檔案**：Windows 3.x 引入的裸點陣字型檔案，內部包含版本號（`0x0200` 或 `0x0300`）、`dfPoints`（磅值）、`dfVertRes` 與 `dfHorizRes`（目標 DPI，如 96 DPI）、字元間距型別（定寬或變寬）、以及字元偏移表 `dfCharTable`；
- **`.FON` 檔案**：本質上是一個偽裝的 16 位 Windows 動態連結庫（NE 格式 DLL）或 32 位可執行檔案（PE 格式 DLL），其程式碼段為空，僅在資源段（`.rsrc`）中嵌入了若干個對應不同字號的 `.FNT` 資料流。

### 3. Unix 與 X11 體系：Adobe BDF 與 PCF 格式
- **BDF（Bitmap Distribution Format）**：由 Adobe 制定的純 ASCII 文字點陣交換格式。語法清晰可讀：
  ```text
  STARTFONT 2.1
  FONT -Adobe-Helvetica-Bold-R-Normal--14-140-75-75-P-82-ISO8859-1
  SIZE 14 75 75
  FONTBOUNDINGBOX 16 14 -2 -3
  STARTPROPERTIES 18
  FONT_ASCENT 11
  FONT_DESCENT 3
  ENDPROPERTIES
  CHARS 256
  STARTCHAR A
  ENCODING 65
  SWIDTH 705 0
  DWIDTH 10 0
  BBX 9 11 0 0
  BITMAP
  1800
  1800
  2400
  2400
  4200
  4200
  7E00
  4200
  4200
  E700
  0000
  ENDCHAR
  ...
  ENDFONT
  ```
  `SWIDTH` 表示在 1000 單元/em 下的可縮放向量寬度；`DWIDTH` 表示該點陣尺寸下的實際裝置畫素步進；`BITMAP` 塊以十六進位制逐行記錄字元點陣圖。
- **PCF（Portable Compiled Format）**：X11 將純文字 BDF 編譯為高執行效率的二進位制格式。PCF 採用小端序或大端序自適應儲存，包含獨立的指標表（Metrics Table）、點陣圖資料表與屬性字典。

---

## A.3 $\TeX$ 體系的巔峰之作：GF 與 PK 格式

唐納德·高德納為 METAFONT 輸出設計的點陣圖格式代表了資料壓縮工程的藝術極境。

### 1. GF（Generic Font）格式
METAFONT 的原始輸出格式。GF 格式採用位元組碼指令流描述字元，包含繪製單行黑白相間畫素的指令：`paint_0` 至 `paint_63`、`skip`（換行）、`boc`（Begin of Character，包含字元包圍盒）、`eoc`（End of Character）。

### 2. PK（Packed Font）格式與遊程動態壓縮演演算法
為了節約極度寶貴的磁碟空間，Tomas Rokicki 於 1985 年發明了 **PK 格式**。PK 格式透過極富創意的**動態閾值變長遊程編碼（Run-length Encoding with Dynamic Packing）**，將 GF 檔案的體積削減了近一半！

#### 動態壓縮閾值 $dyn\_f$ 的數學機理：
每一行畫素被分解為交替出現的“白畫素遊程長度”與“黑畫素遊程長度”。PK 引入一個整數引數 $dyn\_f$（取值 $0 \le dyn\_f \le 14$）：
- 較短的遊程長度 $L$（滿足 $L < dyn\_f$）僅用**單個 4 位半位元組（Nibble）**直接編碼；
- 介於 $dyn\_f$ 與特定區間的遊程，用兩個半位元組編碼：
  $$L = (nibble_1 - dyn\_f - 1) \times 16 + nibble_2 + dyn\_f + 1$$
- 更大的遊程則以特定字首引導 3 個半位元組或獨立位元組編碼；
- 當某一行畫素與上一行完全相同時，直接傳送行重複指令 `repeat`。
METAFONT 編譯器在打包每個字元時，會遍歷嘗試 $dyn\_f = 0$ 至 $14$ 的所有可能性，自動挑選壓縮率最高的最優 $dyn\_f$ 固化在字元頭中，展現出高德納時代駭客對位元效率的極致追求。

---

# 附錄 B：$\TeX$ 與 $\Omega$ 字型格式規範（TFM, OFM, VF, OVF）

## B.1 TFM（$\TeX$ Font Metrics）二進位制資料結構

TFM 檔案是 $\TeX$ 排版引擎感知字型的唯一視窗。一個合法的 TFM 檔案由 12 個物理子表順次拼接而成，所有資料均以 **32 位大端序整數（4 位元組字）** 儲存。

```
┌────────────────────────────────────────────────────────┐
│ 1. HEADER (檔案頭後設資料，包含校驗和與設計尺寸)           │
├────────────────────────────────────────────────────────┤
│ 2. CHAR_INFO (字元資訊表，每個字元佔用一個 4 位元組字)     │
├────────────────────────────────────────────────────────┤
│ 3. WIDTH (寬度陣列)                                    │
├────────────────────────────────────────────────────────┤
│ 4. HEIGHT (高度陣列，至多 16 種不同高度)                 │
├────────────────────────────────────────────────────────┤
│ 5. DEPTH (深度陣列，至多 16 種不同深度)                 │
├────────────────────────────────────────────────────────┤
│ 6. ITALIC (傾斜校正陣列，至多 64 種不同校正量)          │
├────────────────────────────────────────────────────────┤
│ 7. LIG_KERN (連字與字偶間距狀態機程式指令表)            │
├────────────────────────────────────────────────────────┤
│ 8. KERN (實際物理字距數值陣列)                         │
├────────────────────────────────────────────────────────┤
│ 9. EXTEN (大型可伸展數學字元拼接零件裝配表)             │
├────────────────────────────────────────────────────────┤
│ 10. PARAM (字型全域性排版引數: 包含空格自然長、伸縮量等)   │
└────────────────────────────────────────────────────────┘
```

### 1. 定點數字單位：`fix_word`
TFM 內部的所有幾何距離均採用 **`fix_word`** 格式表示。`fix_word` 是一個帶符號的 32 位定點數，其中前 12 位表示整數部分，後 20 位表示小數部分：

$$1\text{ fix\_word} = \frac{\text{Value}}{2^{20}} = \frac{\text{Value}}{1,048,576} \times (\text{Design Size})$$

這保證了在不借助任何硬體浮點數單元的前提下，所有字元度量在跨平臺計算中保持微米級的絕對精度。

### 2. `CHAR_INFO` 的緊湊位域裝配
TFM 將一個字元的全部度量索引不可思議地壓縮排了**單單一組 32 位整數字（4 位元組）**中：
- **Byte 0（第 0–7 位）**：`width_index`（指向 `WIDTH` 陣列的索引，支援 256 種寬度）；
- **Byte 1 高 4 位（第 8–11 位）**：`height_index`（指向 `HEIGHT` 陣列，至多 16 種不同高度）；
- **Byte 1 低 4 位（第 12–15 位）**：`depth_index`（指向 `DEPTH` 陣列，至多 16 種不同深度）；
- **Byte 2 高 6 位（第 16–21 位）**：`italic_index`（指向 `ITALIC` 陣列，至多 64 種傾斜校正）；
- **Byte 2 低 2 位（第 22–23 位）**：`tag`（標籤型別：0 = 無特性，1 = 存在連字/字距微調列表，2 = 存在較大字號連結串列，3 = 屬於可延伸數學裝配字元）；
- **Byte 3（第 24–31 位）**：`remainder`（依據 `tag` 的含義，指向 `LIG_KERN` 或 `EXTEN` 的起始偏移）。

---

## B.2 $\Omega$ 系統 OFM（Omega Font Metrics）規範

為了突破 TFM 只能容納 256 個字元的桎梏，Yannis Haralambous 與 John Plaice 設計了 **OFM 格式**。
- **Level 0 OFM**：檔案頭標誌為大數值，將字元索引直接擴充套件為 16 位整數，支援原生定址 65,536 個字元；
- **Level 1 OFM**：引入了先進的**稀疏分層樹形表結構**，包含橫向與縱向雙軸包圍盒、字形旋轉度數定義，以及支援 32 種動態排版書寫方向的專屬度量矩陣。

---

## B.3 虛擬字型 VF（Virtual Fonts）二進位制規範

VF 檔案由 `vptovf` 編譯生成。
- **`pre` 指令**：包含校驗和與設計尺寸；
- **`fnt_def` 指令**：宣告當前虛擬字型所呼叫的底層物理字型（Real Fonts）或巢狀虛擬字型；
- **字元資料包（Packet）**：每個字元包含一段原生的 DVI 位元組碼指令流。DVI 驅動讀取該字元時，直接將其就地展開並遞迴執行。

---

# 附錄 C：PostScript 字型格式（PostScript Font Formats）

## C.1 PostScript 語言執行機與圖形狀態

PostScript 是一門基於堆疊操作的、圖靈完備的逆波蘭表示法（Postfix）程式語言。直譯器維護著四大堆疊：
1. **運算元棧（Operand Stack）**：暫存數值、字串、字典與幾何路徑；
2. **字典棧（Dictionary Stack）**：檢索全域性與區域性變數；
3. **執行棧（Execution Stack）**：控制流程迴圈與過程呼叫；
4. **圖形狀態棧（Graphics State Stack）**：透過 `gsave` 與 `grestore` 儲存/恢復當前座標變換矩陣（CTM）、剪下路徑與線條線寬。

---

## C.2 Type 1 字型的內部架構與加密數學

PostScript Type 1 字型不僅包含輪廓，更內嵌了一套高強度的專用加密機制：
- **`eexec` 加密演演算法**：用於保護字型私有字典（`Private Dictionary`）。採用 16 位線性同餘偽隨機數流加密：
  $$R_{n+1} = (R_n \times 52845 + 22719) \bmod 65536$$
  $$C_n = P_n \oplus (R_n \gg 8)$$
  其中初始密碼種子金鑰 $R_0 = 55665$。檔案在進入正式程式碼前必須填充 4 個隨機位元組以混淆密文起始狀態；
- **`charstring` 加密演演算法**：用於加密 `CharStrings` 字典內部的具體字形位元組碼，使用相同的數學同餘公式，但初始種子金鑰固定為 $R_0 = 4330$。

### Type 1 CharString 核心操作碼全集

在解密後的位元組流中，操作碼分為單位元組指令（0–31）與帶轉義的二位元組指令（操作碼 12 引導）：
- `hstem` (1), `vstem` (3)：宣告水平與垂直主幹提示；
- `vmoveto` (4), `rlineto` (5), `hlineto` (6), `vlineto` (7)：相對座標直線繪製；
- `rrcurveto` (8)：相對座標三次貝茲曲線繪製（輸入 6 個相對座標增量：$dx_a, dy_a, dx_b, dy_b, dx_c, dy_c$）；
- `callsubr` (10), `return` (11)：呼叫/返回區域性子程式（Subrs，用於複用襯線、圓弧等通用元件）；
- `endchar` (14)：字形繪製終結；
- `rmoveto` (21), `hmoveto` (22)：相對移動原點；
- `vhcurveto` (30), `hvcurveto` (31)：垂直/水平先導的切線貝茲曲線；
- `seac` (12-6, Standard Encoding Accented Character)：高階複合字元裝配指令，輸入基底字元、重音字元及其相對座標，瞬間拼裝出帶重音字母。

---

## C.3 CFF（Compact Font Format）與 Type 2 CharStrings

隨著 OpenType 的普及，Adobe 徹底重構了 Type 1 的老舊冗餘語法，推出了 **CFF 容器** 與 **Type 2 字元指令集**：
- 採用無縫的 **INDEX 索引表結構**，所有資料偏移與長度採用純二進位制整型表頭索引；
- 引入 **Type 2 CharStrings**：支援可變長度整數編碼、瞬時清除運算元棧；
- 新增 `hflex`, `flex` 曲線平滑指令、`callgsubr`（全域性子程式呼叫）、以及用於 Multiple Master 插值融合的 `blend` 運算子，使字型輪廓體積相比傳統 Type 1 縮減了 $30\%$ 至 $50\%$！

---

# 附錄 D：TrueType、OpenType 與 AAT 容器表結構字典

TrueType 與 OpenType 共同基於 **SFNT（Spline Font）模組化表容器架構**。

## D.1 SFNT 表目錄（Table Directory）

一個 SFNT 檔案以 12 位元組的檔案頭（Offset Table）起始：
- `sfntVersion`：`0x00010000`（TrueType 輪廓）或 `'OTTO'`（OpenType CFF 輪廓）；
- `numTables`：包含的資料表總數；
- `searchRange`, `entrySelector`, `rangeShift`：用於對錶標籤（Tags）執行極速二分查詢（Binary Search）的數學最佳化常量。

緊隨其後的是 `numTables` 個由 16 位元組構成的**表目錄記錄（Table Directory Records）**：
```c
struct TableRecord {
    char tag[4];        // 4 字元表標籤，如 "head", "cmap", "glyf", "GSUB"
    unsigned int checkSum; // 該資料表的 32 位全字校驗和
    unsigned int offset;   // 從檔案絕對開頭的位元組物理偏移量
    unsigned int length;   // 該資料表的物理位元組長度
};
```

---

## D.2 核心基礎資料表詳解

### 1. `head`（Font Header）
記錄字型的全域性物理常量：
- `magicNumber`：固定常量值 `0x5F0F3CF5`（用於驗證合法性）；
- `unitsPerEm`：設計網格解析度（通常為 2048）；
- `xMin`, `yMin`, `xMax`, `yMax`：整套字型檔所有字元幾何輪廓的全域性絕對外接矩形；
- `indexToLocFormat`：`0` 表示 `loca` 表使用 16 位短整型偏移，`1` 表示使用 32 位長整型偏移。

### 2. `cmap`（Character to Glyph Index Mapping）
將外部字元編碼轉換為內部字形索引（GID）。包含多個子表：
- **Format 4（段對映至 Delta 值）**：Windows 早期為 BMP 基本多語言平面設計的經典子表。將連續碼點劃分為若干段（Segments），透過 `startCount`, `endCount`, `idDelta`, `idRangeOffset` 執行範圍查詢；
- **Format 12（分段覆蓋）**：現代 Unicode 全平面的標準子表，直接支援從 `U+0000` 到 `U+10FFFF` 的 32 位字元連續段對映；
- **Format 14（變體序列選擇符）**：專門支援 Unicode 變體選擇符（Variation Selectors, VS1–VS256）。

### 3. `glyf`（Glyph Data）與 `loca`（Index to Location）
- **`loca` 表**：一個整數陣列，記錄每個 GID 對應的輪廓資料在 `glyf` 表中的起始偏移量；
- **`glyf` 表**：
  - 若 `numberOfContours >= 0`，為**簡單字形（Simple Glyph）**：記錄各輪廓端點索引陣列、位元組標誌位陣列（標誌當前點是否為曲線控制點、座標增量是否為 1 位元組等）、以及壓縮的 $X$ 與 $Y$ 相對座標陣列；
  - 若 `numberOfContours == -1`，為**複合字形（Composite Glyph）**：記錄若干分量字形 GID，以及 $2 \times 2$ 仿射變換矩陣（縮放、旋轉、剪下與平移位移量）。

### 4. `hhea` 與 `hmtx`
- `hhea`：記錄全域性最大上升部（`ascender`）、最大下降部（`descender`）、行間距（`lineGap`）；
- `hmtx`：緊湊陣列，前部記錄每個字形的前進寬度與 LSB，尾部為擁有相同最大寬度的等寬字元陣列。

### 5. `OS/2` 表
微軟與 IBM 聯合制定的跨系統相容度量表：
- `sTypoAscender`, `sTypoDescender`, `sTypoLineGap`：排版度量；
- `usWinAscent`, `usWinDescent`：Windows GDI 文字行裁剪硬邊界；
- `panose`：10 位元組 PANOSE-1 視覺分類指紋；
- `ulUnicodeRange1..4`：128 位掩碼，精確標識字型支援的 Unicode 區塊。

---

## D.3 OpenType 高階排版佈局表（GSUB / GPOS / GDEF）

### 1. 三級索引架構
無論是 `GSUB` 還是 `GPOS`，頂層均採用統一的三級跳轉架構：

$$\text{ScriptList} \longrightarrow \text{FeatureList} \longrightarrow \text{LookupList}$$

1. **ScriptList（書寫系統列表）**：根據輸入文字的語言系統（如 `latn`, `arab`, `deva`）查詢支援的特性索引；
2. **FeatureList（特性列表）**：定位具體特性（如 `liga`, `smcp`, `kern`）所包含的查詢表索引；
3. **LookupList（查詢表列表）**：執行具體的字形變換演演算法。

### 2. 覆蓋表（Coverage Table）與類定義表（ClassDef Table）
為了在毫秒級判斷某個字元是否參與排版規則，OpenType 引入了覆蓋表：
- **Format 1**：單個 GID 線性列表；
- **Format 2**：由連續範圍組成的區間表（`startGlyphID` 到 `endGlyphID` 對映至連續覆蓋索引）。

---

# 附錄 E：METAFONT 與 MetaPost 語言參考

高德納的 METAFONT 將字型設計從“繪製輪廓”提升到了“方程求解”的數學境界。

## E.1 宣告式幾何方程求解引擎
在 METAFONT 中，設計師不需要顯式計算交點座標，只需宣告幾何約束方程，內建的高斯消元求解器會自動解出點的位置：

```metafont
z1 = (0, 0);
z2 = (w, h);
z3 = .5[z1, z2];          % 宣告 z3 是 z1 與 z2 的正中中點！
x4 = x3; y4 = 0;          % 宣告 z4 位於 z3 的正下方基線上
draw z1--z2;              % 繪製連線線段
draw z3..z4;              % 繪製平滑穿過指定點的曲線
```

## E.2 畫筆（Pens）與包絡線理論
METAFONT 的筆觸模型基於凸多邊形或橢圓畫筆沿軌跡掃掠而成的**包絡線（Envelope）**：
- `pickup pencircle scaled 2pt;`：拾起一枚直徑為 2 磅的圓形墨水筆；
- `pickup pensquare xscaled 1pt yscaled 3pt rotated 30;`：模擬古典寬邊羽毛筆的傾斜切面。

---

# 附錄 F：TrueType 指令位元組碼全集參考（Instruction Set）

TrueType 字型內部整合了一個功能完備的**圖靈完備堆疊虛擬機器（TrueType VM）**。它在字元輪廓光柵化之前執行，強行拉扯、對齊曲線控制點，使筆畫在離散畫素格中展現出極致的清晰度。

## F.1 虛擬機器的內部硬體環境
- **執行棧（Execution Stack）**：後進先出，支援 256 至數千個 32 位整型元素；
- **控制值表（Control Value Table, CVT）**：儲存全域性標準化筆畫寬度與對齊高度基準；
- **儲存區（Storage Area）**：提供至少 256 個臨時變數暫存器（透過 `RS` 讀、`WS` 寫）；
- **圖形狀態機（Graphics State, GS）**：維護投影向量（Projection Vector）、自由向量（Freedom Vector）、舍入狀態（Round State）與自動翻轉閾值；
- **暮光區（Twilight Zone, Zone 0）**：用於存放臨時動態建立的輔助幾何計算節點；
- **字形區（Glyph Zone, Zone 1）**：當前正在光柵化的真實字形輪廓節點。

## F.2 核心指令全集分類字典

| 操作碼分類 | 代表指令 | 功能與數學行為描述 |
| :--- | :--- | :--- |
| **點移動指令** | `MDAP[rnd]` | 移動直接絕對點：將指定節點直接對齊到當前投影向量所指的最近畫素網格線上 |
| | `MIAP[rnd]` | 移動間接絕對點：將指定節點對齊到 CVT 表中預存的標準化基準位置（如 x 高度） |
| | `MDRP[...]` | 移動直接相對點：根據與參考節點的原始幾何距離，在畫素網格上保持相對間距 |
| | `MIRP[...]` | 移動間接相對點：保持與參考節點的相對距離，同時強制使其寬度吻合 CVT 標準筆畫寬 |
| **內插與平滑** | `ALIGNPTS` | 對齊兩點：將兩點沿當前投影向量移動，使其座標絕對重合 |
| | `IP` | 內部插值點：在兩個已被網格對齊的參考點之間，根據原始比例內插中間節點的相對座標 |
| | `IUP[X]`, `IUP[Y]` | 未碰觸點終結內插：遍歷輪廓中所有未被顯式指令約束的點，依據最近的兩個受約束點平滑內插其位置 |
| **Delta 微調族** | `DELTAP1..3` | 點微調：在指定的離散字號（PPEM）下，將特定節點的座標強制微調若干分之一個畫素（專門修復某字號下的突兀畫素孤點） |
| | `DELTAC1..3` | CVT 微調：在特定字號下微調 CVT 暫存器的數值 |
| **堆疊操作** | `PUSHB`, `PUSHW` | 將 1 位元組或 2 位元組整型資料壓入堆疊 |
| | `DUP`, `POP`, `SWAP` | 複製棧頂、彈出棧頂、交換棧頂兩元素 |
| **流程控制** | `IF`, `ELSE`, `EIF` | 條件分支跳轉 |
| | `FDEF`, `ENDF` | 定義與結束函式宏 |
| | `CALL`, `LOOPCALL` | 呼叫函式與迴圈呼叫 |
| **網格舍入** | `RTG`, `RTHG`, `RDTG` | 切換舍入模式至整畫素點、半畫素點或向零下取整 |

---

# 附錄 G：曲線微分幾何與高階計算字形學

## G.1 伯恩斯坦多項式（Bernstein Polynomials）基底

$n$ 次貝茲曲線以伯恩斯坦多項式作為基底函式：

$$B_{i,n}(t) = \binom{n}{i} t^i (1-t)^{n-i}, \quad i = 0, 1, \dots, n$$

### 核心數學性質：
1. **單位分解性（Partition of Unity）**：
   $$\sum_{i=0}^n B_{i,n}(t) \equiv 1, \quad \forall t \in \mathbb{R}$$
2. **非負性（Non-negativity）**：
   $$B_{i,n}(t) \ge 0, \quad \forall t \in [0, 1]$$
這兩大性質構成了貝茲曲線最重要的幾何特徵——**凸包性（Convex Hull Property）**：曲線整體嚴格包含在所有控制節點構成的凸多邊形內部，這使得字型渲染引擎在執行視錐裁剪（Clipping）與碰撞檢測時可以閃電般地排除不相交區域。

## G.2 貝茲曲線的微分動量與切向量（Hodograph）

對 $n$ 次貝茲曲線 $\mathbf{B}(t) = \sum_{i=0}^n B_{i,n}(t) \mathbf{P}_i$ 求一階導數，其導函式（導曲線）是一條度數降為 $n-1$ 次的新貝茲曲線：

$$\mathbf{B}'(t) = n \sum_{i=0}^{n-1} B_{i,n-1}(t) (\mathbf{P}_{i+1} - \mathbf{P}_i)$$

對於三次貝茲曲線（$n=3$）：
- 曲線在起點 $t=0$ 處的切向量為：$\mathbf{B}'(0) = 3(\mathbf{P}_1 - \mathbf{P}_0)$；
- 曲線在終點 $t=1$ 處的切向量為：$\mathbf{B}'(1) = 3(\mathbf{P}_3 - \mathbf{P}_2)$。

這從數學嚴謹性上證明了：**控制柄的方向決定了曲線端點的精確切線斜率，控制柄的幾何長度決定了曲線離開端點時的初速度與曲率半徑**！

---

## G.3 德卡斯特里奧細分演演算法（De Casteljau's Algorithm）

德卡斯特里奧演演算法是貝茲曲線在計算機中繪製、平滑細分與求交計算的黃金基石。給定控制點 $\mathbf{P}_0, \mathbf{P}_1, \mathbf{P}_2, \mathbf{P}_3$ 與引數 $t_0 \in (0, 1)$：

```
P0 ────(t0)────> P01 ────(t0)────> P012 ────(t0)────> P0123 = B(t0)
P1 ────(t0)────> P12 ────(t0)────> P123
P2 ────(t0)────> P23
P3
```

遞推公式為：
$$\mathbf{P}_i^{(k)}(t_0) = (1-t_0)\mathbf{P}_i^{(k-1)}(t_0) + t_0 \mathbf{P}_{i+1}^{(k-1)}(t_0)$$

該演演算法不僅能在純加減法與線性插值中以極高數值穩定性計算出曲線上任意點 $\mathbf{B}(t_0)$，而且當 $t_0 = 0.5$ 時，點序列 $(\mathbf{P}_0, \mathbf{P}_0^{(1)}, \mathbf{P}_0^{(2)}, \mathbf{P}_0^{(3)})$ 與 $(\mathbf{P}_0^{(3)}, \mathbf{P}_1^{(2)}, \mathbf{P}_2^{(1)}, \mathbf{P}_3)$ 精準地構成了將原曲線一分為二後的兩條獨立子曲線的完整控制網格！光柵化引擎只需透過迴圈二分細分，直至控制多邊形扁平收斂為直線，即可實現畫素級的極速直線掃描轉換。

---

# 結語：獻給在字元星河中執燈前行者

至此，《Fonts & Encodings》全書十五個章節與七大技術附錄的所有微觀資料結構、數學公式、編譯流水線與歷史源流已全部呈現在你的眼前。

從千年前楔形文字與金屬活字在泥板與鉛印上的沉重烙印，到 8 位位元組時代高德納在斯坦福構建的 $\TeX$ 盒子宇宙，再到 16 位 Unicode、OpenType 佈局流與現代 Web 字型光柵化演演算法，人類為了跨越時空阻隔、為了讓知識與思想永存所傾注的智慧，全都被凝鍊在了這一個個精微至極的位元組、向量與貝茲控制點之中。

願這套技術文獻，能成為所有在現代數字文字文明之海中探索、求索與創造者的常備羅盤與指路明燈！
