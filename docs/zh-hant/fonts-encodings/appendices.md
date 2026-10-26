---
title: "附錄 A–G：底層格式與數學技術參考全景指南"
description: "涵蓋位圖字體 (A)、TeX/Omega (B)、PostScript Type 1/CFF (C)、TrueType/OpenType 結構與目錄 (D)、METAFONT 與畫筆幾何 (E/F)、TrueType 虛擬機微指令集、以及曲線微分幾何學 (G)。"
---

# 附錄 A–G：底層格式與數學技術參考全景指南
### Appendices A–G: Technical Reference Manual for Digital Typography
選自《Fonts & Encodings》附錄 A 至 G 全 340 頁參考手冊
*譯者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

本參考手冊彙集了《Fonts & Encodings》全書後半部全七大技術附錄（Appendices A 至 G）。這部分是雅尼斯·哈拉蘭博斯（Yannis Haralambous）爲字型工程師、底層排版系統開發者以及數學愛好者構築的堅實基石，詳盡記錄了從 20 世紀 80 年代點陣位圖格式到 21 世紀現代 OpenType/AAT 容器結構、TrueType 虛擬機約 130 條微指令集、以及曲線微分幾何學的全套數學實現與工業級規範。

---

# 附錄 A：點陣字體格式（Bitmap Font Formats）

點陣字體（Bitmap Fonts，或稱光柵字體 Raster Fonts）是數字印藝與計算機圖形顯示史上的初始形態。在微處理器計算能力與顯示內存極其有限的 1970 至 1980 年代，計算機屏幕與點陣打印機無法承受實時計算三次貝塞爾曲線輪廓的龐大浮點運算，文字必須預先在離散的二維點陣像素網格（Pixel Grid）中逐位繪製，並以緊湊的位圖切片（Bitmaps）形式固化於存儲介質中。

儘管矢量字體在當今桌面出版領域佔據了絕對主導地位，但在嵌入式微控制器、BIOS 啓動固件、Linux 虛擬終端控制檯、低功耗電子墨水屏以及特種排版軟件（如 TeX 引擎的高分辨率物理打印驅動）中，點陣字體格式依然發揮着不可替代的高速直讀與亞像素純度優勢。本附錄對歷史上五大主流點陣字庫體系進行徹底的底層二進制解構。

---

## A.1 經典蘋果 Macintosh 體系點陣字庫（FONT 與 NFNT 資源）

在 1984 年發佈的經典 Mac OS（System 1.0 至 Mac OS 9）中，蘋果開創性地將文件系統劃分爲**數據分支（Data Fork）**與**資源分支（Resource Fork）**。字庫並非存儲爲普通的平面文件，而是作爲具名資源直接封裝在資源分支中。

Mac OS 中的點陣字型主要由兩類資源承載：
* **`FONT` 資源**：早期系統標準，資源 ID 直接編碼了字體家族號（Family ID）與點數磅重（Point Size）：$\text{Resource ID} = \text{Family ID} \times 128 + \text{Point Size}$；
* **`NFNT`（New Font Numbering Table）資源**：由於 `FONT` 架構僅支持最多 256 個字體家族，蘋果推出了 `NFNT` 資源，打破了 ID 與字號的直接耦合，支持多達 16,000 個獨立字族，並允許攜帶專有顏色查找表。

### 1. FontRec 核心二進制結構體
無論 `FONT` 還是 `NFNT`，其核心數據載荷均嚴格遵循由 QuickDraw 圖形引擎定義的 `FontRec` 結構體：

```c
struct FontRec {
    uint16 fontType;        /* 字体属性标志位字（见下文位域解析） */
    uint16 firstChar;       /* 字体支持的首个字符 ASCII 码（通常 0x00 或 0x20） */
    uint16 lastChar;        /* 字体支持的末尾字符 ASCII 码（通常 0xFF） */
    uint16 widMax;          /* 全字体字形的最大外形推进宽度（Advance Width） */
    int16  kernMax;         /* 全字体最大负字距（Negative Kerning，通常 <= 0） */
    int16  nDescent;        /* 负向降部高度（Descent，向下为负值） */
    uint16 fRectWidth;      /* 字体包围盒的最大位图宽度（Bounding Box Width） */
    uint16 fRectHeight;     /* 字体包围盒的最大位图高度（Bounding Box Height） */
    uint16 owTLoc;          /* 偏移量/字宽表（Offset/Width Table）距离本结构体首地址的 16 位字偏移 */
    int16  ascent;          /* 正向升部高度（Ascent，从基线到字身顶端） */
    int16  descent;         /* 降部深度绝对值（Descent，从基线到字身底部） */
    int16  leading;         /* 推荐行间空隙（Leading，行距增量） */
    uint16 rowWords;        /* 位图全景图像（Bit Image）每一扫描行所占的 16 位双字节字数（Words） */
    /* 紧随其后为可变长度数组：
       uint16 bitImage[rowWords * fRectHeight]; 位图图像连续扫描行矩阵
       uint16 locTable[lastChar - firstChar + 3]; 字形横向切片列定位表
       uint16 owTable[lastChar - firstChar + 3];  字宽与字距微调偏移表
    */
};
```

#### `fontType` 屬性標誌位的精細解構
* **Bit 0 (`propFont`)**：爲 0 表示等寬字體（Monospaced），爲 1 表示比例可變寬字體（Proportional）；
* **Bit 1 (`colorFont`)**：爲 1 表示當前資源爲彩色多層位圖字；
* **Bit 7 (`synthetic`)**：指示當前字庫是否爲系統通過算法加粗或傾斜合成的派生字；
* **Bits 2–3 (`depth`)**：位圖顏色深度，`00` 代表 1-bit 黑白雙色，`01` 代表 2-bit 四階灰度，`10` 代表 4-bit 十六階灰度，`11` 代表 8-bit 二百五十六階灰度。

### 2. 位圖切片投影：橫向撞擊圖像（Bit Image Strike）
Mac OS 點陣字體最具天才的設計在於其**連貫橫向帶狀圖像（Strike Font）**機制。QuickDraw 並沒有將 256 個字母分別存儲爲 256 張零散的小圖片，而是將所有字符按照 ASCII 順序從左向右**一字排開，水平縫合爲一張極其狹長的巨幅全景橫向位圖**！

::: tip Mac OS 點陣字體 FontRec 內存拓撲與 Strike 位圖解構（Figure A-1, A-2, A-3）
![Mac OS 點陣字體 FontRec 內存拓撲（Figure A-1）](/images/fonts-encodings/fig-app-a1.png)
*Mac OS 點陣字體 FontRec 內存拓撲（Figure A-1）*
:::

*圖 A-1：Mac OS 點陣字體內部內存佈局。從頭部 FontRec 結構，到底層 Strike 連貫位圖條帶與 LocTable 列偏移切片。*

::: tip Mac OS Strike 位圖橫向切片與黑白像素掃描（Figure A-2）
![Mac OS Strike 位圖橫向切片（Figure A-2）](/images/fonts-encodings/fig-app-a2.png)
*Mac OS Strike 位圖橫向切片（Figure A-2）*
:::

*圖 A-2：Strike 全景橫向位圖展示。所有字母按順序排列在同一張高度爲 `fRectHeight` 的位圖條帶中，寬度由 `rowWords * 16` 決定。*

::: tip Mac OS LocTable 與 OWTable 尋址機制（Figure A-3）
![Mac OS LocTable 與 OWTable 尋址（Figure A-3）](/images/fonts-encodings/fig-app-a3.png)
*Mac OS LocTable 與 OWTable 尋址（Figure A-3）*
:::

*圖 A-3：字符在 Strike 圖像中的提取流程：通過字符 ASCII 碼查 `locTable` 得到起始像素列 $x_{start}$ 與結束像素列 $x_{end}$，瞬間切出單個字母的位圖矩陣。*

#### 尋址與提取算法：
1. 欲渲染字符 $C$（$\text{firstChar} \le C \le \text{lastChar}$），其在 `locTable` 中的索引爲 $i = C - \text{firstChar}$；
2. 讀取該字符在全景圖像中的像素列起始座標：$x_{start} = \text{locTable}[i]$；
3. 讀取其後一個條目：$x_{end} = \text{locTable}[i+1]$；
4. 若 $x_{start} == x_{end}$，說明該字符在字庫中缺失，QuickDraw 自動跳轉至末尾繪製默認未定義符號（Missing Symbol）；
5. 若存在，則字符的物理位圖寬度即爲 $W = x_{end} - x_{start}$，高度恆定爲 `fRectHeight`；
6. 接着查閱 `owTable[i]`：高 8 位爲該字形渲染時的左側負間距（Left Kerning offset），低 8 位爲繪製後的排版光標前進量（Advance Width）。QuickDraw 僅需一次位塊傳輸（BitBlt）指令，即可將該矩形切片精準印入幀緩衝區！

---

## A.2 PC 與 Windows 體系點陣字庫（DOS CPI 與 Windows FNT/FON）

在 IBM PC 兼容機與微軟 DOS/Windows 發展史上，點陣字體經歷了從 BIOS 硬件 ROM 固化，到 DOS 動態代碼頁切換，再到 Windows 早期圖形環境的演進。

### 1. DOS 代碼頁信息文件（CPI: Code Page Information）
在 MS-DOS 3.3 引入多語言支持後，系統通過 `CPI` 文件（如 `EGA.CPI`, `LCD.CPI`）動態爲顯示適配器（EGA/VGA）的顯存刷新硬件點陣字體：
* **文件頭魔數**：固定前 7 字節爲 `0xFF, 'F', 'O', 'N', 'T', ' ', ' '`；
* **指針鏈表**：包含指向各個代碼頁塊（如 CP437, CP850）的文件偏移指針；
* **點陣載荷**：每個字符通常存儲爲 8 字節（$8 \times 8$ 點陣）、14 字節（$8 \times 14$ EGA 點陣）或 16 字節（$8 \times 16$ VGA 點陣）的緊湊單色掃描行數組。

### 2. Windows 2.0 / 3.0 光柵字體規範（`.FNT` 與 `.FON`）
在 Windows 3.1 引入 TrueType 之前，Windows 圖形設備接口（GDI）完全依賴 `.FNT` 文件。多個尺寸與字重的 `.FNT` 文件最終通過資源鏈接器被打包爲一個動態鏈接庫（DLL）形態的 `.FON` 文件。

`.FNT` 文件由一個龐大的 118 字節（Version 2.0）或 148 字節（Version 3.0）的二進制文件頭起始：

```c
#pragma pack(push, 1)
struct WinFNTHeader {
    uint16 dfVersion;            /* 格式版本号：0x0200 (Win 2.x) 或 0x0300 (Win 3.x) */
    uint32 dfSize;               /* .FNT 整个文件的总字节长度 */
    char   dfCopyright[60];      /* ASCII 编码的版权声明字符串 */
    uint16 dfType;               /* 字体类型：0x0000 代表点阵光栅字，0x0001 代表矢量矢量线框字 */
    uint16 dfPoints;             /* 标称设计磅值（Nominal Point Size） */
    uint16 dfVertRes;            /* 设计垂直分辨率（通常 96 DPI） */
    uint16 dfHorizRes;           /* 设计水平分辨率（通常 96 DPI） */
    uint16 dfAscent;             /* 基线至顶端的升部高度（Ascent in pixels） */
    uint16 dfInternalLeading;    /* 内部行距（留给重音符号的空间） */
    uint16 dfExternalLeading;    /* 外部行距（推荐的额外空隙） */
    uint8  dfItalic;             /* 斜体标志位（1 为斜体） */
    uint8  dfUnderline;          /* 下划线标志位 */
    uint8  dfStrikeOut;          /* 删除线标志位 */
    uint16 dfWeight;             /* 字重（100 Thin 至 900 Black，400 为 Regular） */
    uint8  dfCharSet;            /* 字符集代码（0: ANSI, 1: Default, 2: Symbol, 128: Shift-JIS） */
    uint16 dfPixWidth;           /* 等宽字体的像素宽度（若为 0 则为比例变宽字体） */
    uint16 dfPixHeight;          /* 字符全高的像素数（Scanlines） */
    uint8  dfPitchAndFamily;     /* 变宽/等宽标志与字族分类（Serif, Sans-serif 等） */
    uint16 dfAvgWidth;           /* 小写字母平均宽度 */
    uint16 dfMaxWidth;           /* 字体中最大字形宽度 */
    uint8  dfFirstChar;          /* 首个支持的字符码点（通常 32 空格） */
    uint8  dfLastChar;           /* 最后一个字符码点（通常 255） */
    uint8  dfDefaultChar;        /* 替代缺失字符的默认字符偏移量 */
    uint8  dfBreakChar;          /* 用于断行分词的空格字符偏移量 */
    uint16 dfWidthBytes;         /* 每一行扫描线在内存中对齐的单行字节数（必须为双字节偶数倍） */
    uint32 dfDevice;             /* 指向目标设备名称字符串的文件内字节偏移 */
    uint32 dfFace;               /* 指向字体家族名称字符串（如 "System", "Terminal"）的文件内偏移 */
    uint32 dfBitsPointer;        /* 运行时内存中的位图指针（文件中填 0） */
    uint32 dfBitsOffset;         /* 位图数据阵列距离文件头的绝对字节偏移量！ */
    /* Windows 3.0 (dfVersion == 0x0300) 额外包含扩展字段： */
    uint8  dfByteFlags;          /* 位图打包与内存管理标志 */
    uint32 dfColorMapOffset;     /* 颜色表偏移量 */
    uint32 dfReserved[4];        /* 保留字段 */
};
#pragma pack(pop)
```

#### 字符偏移表與位圖檢索機制
緊隨頭部之後的是字符表（Char Table）：
* **Version 2.0**：每個字符佔用 4 字節：`uint16 width; uint16 offset;`
* **Version 3.0**：爲了支持超過 64KB 的超大點陣字庫，擴展爲 6 字節：`uint16 width; uint32 offset;`

當 Windows GDI 需要繪製字符 $C$ 時：
1. 索引到字符條目，讀取字寬 `width` 與絕對文件偏移 `offset`；
2. 定位到 `offset` 處的單色位圖數據：數據按照從上至下的光柵行連續排列；
3. **列式優先掃描規則**：與常見水平位圖不同，Windows 2.x/3.x 的 FNT 格式在某些變體中採用逐列（Column-major）存儲或以 8 像素對齊的垂直步進存儲，GDI 通過硬件位移指令將字節流直接解包推送到顯示適配器顯存。

---

## A.3 X Window System 體系規範（BDF 與 PCF）

在 Unix 與 Linux 桌面圖形生態（X11）中，點陣字體擁有高度標準化且極爲嚴謹的開放規範。

### 1. BDF 格式（Bitmap Distribution Format）
BDF 是由 Adobe 與 X 聯盟（X Consortium）制定的**純 ASCII 純文本點陣字體交換規範**（版本爲 2.1 與 2.2）。它不依賴任何特定 CPU 架構的字節序（Endianness），可讀性極強，被全人類開源字型設計社區廣泛作爲點陣字體設計的通用源碼格式。

一個正規的 BDF 文件由全局頭部聲明、X11 邏輯字體描述符（XLFD）屬性字典、以及逐個字符的十六進制掃描線塊構成：

```bdf
STARTFONT 2.1
FONT -Adobe-Courier-Medium-R-Normal--14-100-100-100-M-90-ISO8859-1
SIZE 10 100 100
FONTBOUNDINGBOX 9 14 -1 -3
STARTPROPERTIES 18
FOUNDRY "Adobe"
FAMILY_NAME "Courier"
WEIGHT_NAME "Medium"
SLANT "R"
SETWIDTH_NAME "Normal"
ADD_STYLE_NAME ""
PIXEL_SIZE 14
POINT_SIZE 100
RESOLUTION_X 100
RESOLUTION_Y 100
SPACING "M"
AVERAGE_WIDTH 90
CHARSET_REGISTRY "ISO8859"
CHARSET_ENCODING "1"
CAP_HEIGHT 10
X_HEIGHT 7
FONT_ASCENT 11
FONT_DESCENT 3
ENDPROPERTIES
CHARS 256
STARTCHAR A
ENCODING 65
SWIDTH 600 0
DWIDTH 9 0
BBX 9 11 0 0
BITMAP
0000
0C00
1E00
3300
3300
6180
7F80
6180
6180
E0C0
0000
ENDCHAR
ENDFONT
```

#### BDF 核心字段數學語義解析：
* `SWIDTH sx sy`：可縮放寬度（Scalable Width）。以 $1/1000$ 磅（Em）爲單位。計算公式爲：$\text{SWIDTH} = \frac{\text{DWIDTH}}{\text{Point Size} \times \frac{\text{Resolution}}{72.27}} \times 1000$；
* `DWIDTH dx dy`：設備寬度（Device Width）。字符被繪製後，排版光標在屏幕物理像素上的位移增量向量（橫排文字時 $dy=0$）；
* `BBX width height x_off y_off`：字符位圖的緊包圍盒（Bounding Box）：
  * `width`：位圖實際具有墨跡像素的橫向列數；
  * `height`：位圖實際具有墨跡的垂直行數；
  * `x_off`：從邏輯原點（0,0）到包圍盒左邊緣的水平像素偏移（左側軸承 LSB）；
  * `y_off`：從邏輯基線到包圍盒底邊緣的垂直像素偏移（下降爲負值）；
* `BITMAP`：每行一個十六進制整數字符串。若 `width` 爲 9，則該行需要 2 個十六進制雙字節（16 位）表示，多餘的低位填充 0。

### 2. PCF 格式（Portable Compiled Format）
BDF 作爲文本格式，解析效率低下，體積龐大。X11 在啓動加載時，會通過 `bdftopcf` 工具將 BDF 編譯爲**PCF（Portable Compiled Format）二進制文件**。

PCF 文件由一個**塊目錄（Table Directory）**管理整個文件的物理分塊，具有極高的動態擴展性：
* **文件頭魔數**：固定爲 4 字節：`0x70, 0x63, 0x66, 0x01`（字符串 `\x01fcp`）；
* **`table_count`**：文件中包含的獨立子表總數；
* **子表目錄項**：
  ```c
  struct PCFTableEntry {
      uint32 type;        /* 子表类型位域掩码（见下文） */
      uint32 format;      /* 格式控制字：包含字节序（MSB/LSB）、字长（1/2/4字节）、压缩标志 */
      uint32 size;        /* 子表在文件中的原始字节大小 */
      uint32 offset;      /* 子表距离文件头的绝对字节偏移量 */
  };
  ```

#### PCF 核心子表類型掩碼：
* `PCF_PROPERTIES (1<<0)`：繼承自 BDF 的全部 XLFD 元數據鍵值對；
* `PCF_ACCELERATORS (1<<1)`：加速器度量（全字體是否有常數寬度、最大最小邊界等，允許 X Server 跳過逐字計算）；
* `PCF_METRICS (1<<2)`：每一個字形的 `leftSideBearing`, `rightSideBearing`, `characterWidth`, `ascent`, `descent`, `attributes`；
* `PCF_BITMAPS (1<<3)`：全字體所有字形的純位圖數據載荷陣列；
* `PCF_INK_METRICS (1<<4)`：字符墨跡的真實幾何邊界；
* `PCF_BDF_ENCODINGS (1<<5)`：字符編碼映射表（包含多字節字符集如 GB2312, JISX0208）；
* `PCF_SWIDTHS (1<<6)`：可縮放寬度表；
* `PCF_GLYPH_NAMES (1<<7)`：所有字符的 PostScript 符號名稱字符串池。

由於 PCF 在 `format` 字段中顯式標明瞭子表採用大端序（Big-Endian）還是小端序（Little-Endian），X Server 在載入字庫時可直接通過 `mmap` 系統調用將字庫無縫映射到內存空間，實現接近零開銷的瞬時字形索引！

---

## A.4 TeX 體系專用點陣格式（GF 與 PK）

高德納（Donald Knuth）在研發 TeX 與 METAFONT 系統時，爲了使排版結果在不同的操作系統與輸出設備上保持**嚴格不可動搖的數學一致性**，設計了兩大標誌性的點陣格式：**GF（Generic Font）** 與 **PK（Packed Font）**。

### 1. GF 格式（Generic Font）
GF 是 METAFONT 編譯輪廓方程並光柵化輸出的初級二進制中間產物。GF 並非簡單的位圖轉儲，而是一套**基於一維遊程編碼（Run-Length Encoding）的微型光柵機虛擬機字節碼流**！

GF 擁有多達 256 個操作碼（Opcodes），以高度精簡的流式狀態機控制虛擬畫筆：
* `paint_0` 至 `paint_63`（操作碼 0–63）：指令操作碼本身的值即代表連續繪製黑像素（Black Pixels）的個數（0 到 63 個），畫筆自動右移並交替翻轉顏色狀態；
* `paint1` 至 `paint4`（操作碼 64–67）：後接 1 至 4 字節無符號整數，用於繪製超長連續像素段；
* `boc`（操作碼 68，Begin of Character）：開啓一個全新字符，後接字符碼點、前向指針與該字符包圍盒的完整浮點度量；
* `boc1`（操作碼 69）：精簡版字符起始指令（針對普通小字符優化，減少參數字節）；
* `eoc`（操作碼 70，End of Character）：終結當前字符；
* `skip0` 至 `skip3`（操作碼 71–74）：行末換行指令，將光標跳到下方指定距離的掃描行起始處；
* `new_row_0` 至 `new_row_164`（操作碼 75–238）：**超緊湊換行指令**！一條單字節指令同時完成兩項工作：換到下一行，並在新行的開頭繪製 0 至 164 個白像素；
* `xxx1` 至 `xxx4`（操作碼 239–242）：用於在字庫中嵌入特殊註釋或 METAFONT `special` 擴展指令的透明數據載荷；
* `yyy`（操作碼 243）：用於記錄字體設計磅重與輔助參數；
* `no_op`（操作碼 244）：空操作，用於內存對齊；
* `char_loc`（操作碼 245）與 `char_loc0`（操作碼 246）：位於文件尾部的字符定位總目錄；
* `pre`（操作碼 247）：文件前導標識；
* `post`（操作碼 248）與 `post_post`（操作碼 249）：文件終結簽名。

### 2. PK 格式（Packed Font）的高階動態壓縮算法
由於 GF 文件體積相對龐大，Tomas Rokicki 在 1985 年提出了 **PK（Packed Font）格式**。PK 引入了一種革命性的**自適應動態遊程壓縮算法（Dynamic Run-Length Compression with Parameter $dyn\_f$）**，在保持快速流式解壓的同時，將點陣字體體積大幅削減了 50% 以上，成爲了全人類 TeX 生態事實上的最終輸出標準。

#### PK 字符頭（Character Header）結構
每個字符由一個標誌字節（Flag Byte）領銜，該字節的高 4 位被賦予了極其關鍵的數學控制參數：

$$\text{Flag Byte} = (dyn\_f \times 16) + (\text{first\_pixel\_black} \ ? \ 8 : 0) + \text{format\_flag}$$

* $dyn\_f$（取值 0 到 14）：由壓縮器計算得出的該字符最優動態截斷閾值！若 $dyn\_f == 14$，說明該字符爲純點陣光柵存儲（不進行遊程壓縮）；
* $\text{first\_pixel\_black}$：布爾值，指示當前字符的第一行掃描線的首個像素是黑還是白；
* $\text{format\_flag}$（0 到 7）：指示緊隨其後的字符包圍盒尺寸採用 1 字節、2 字節還是 4 字節存儲。

#### 核心動態半字節（Nybble）解包算法
在解包位圖數據時，PK 引擎按 4 位半字節（Nybble，取值 0 到 15）順序讀取字節流。遊程長度 $L$（Run-length）的解析完全遵循以下有限狀態機：

1. **單半字節情況**：若讀到的半字節 $N < dyn\_f$：
   則該遊程長度直接等於 $N$：$L = N$；
2. **雙半字節情況**：若讀到的半字節 $dyn\_f \le N \le 13$：
   則必須緊接着讀取下一個半字節 $N_2$，遊程長度由兩位基數混合計算：
   $$L = (N - dyn\_f - 1) \times 16 + N_2 + dyn\_f + 1$$
3. **三半字節情況**：若讀到的半字節 $N == 14$：
   則連續讀取後兩個半字節 $N_2$ 與 $N_3$：
   $$L = (N_2 - 16) \times 16 + N_3 + dyn\_f + 1$$
4. **多行重複標誌（Repeat Count）**：若讀到的半字節 $N == 15$：
   **並不產生像素位移**！而是讀取隨後的遊程數據，指示緊隨其後的掃描行在垂直方向上重複繪製若干次！這在處理垂直平直筆畫（如字母 `'l'`、`'H'` 的堅硬立柱）時，實現了近乎無限大的壓縮比！

#### 工業級 Python PK 解包器實現
以下給出遵循 Knuth 標準規範的 PK 遊程解析核心算法實現：

```python
def unpack_pk_runs(nybble_stream, dyn_f, first_pixel_black, total_pixels):
    """
    解压 PK 字符点阵游程流
    :param nybble_stream: 生成器，逐个产出 0-15 的 4-bit 整数
    :param dyn_f: 动态阈值 (0-14)
    :param first_pixel_black: 首像素极性
    :param total_pixels: 字符总像素数 (width * height)
    :return: 展开后的 0/1 像素一维数组
    """
    pixels = []
    is_black = first_pixel_black
    repeat_count = 0
    
    while len(pixels) < total_pixels:
        nyb = next(nybble_stream)
        
        # 状态 1: 扫描行重复计数
        if nyb == 15:
            # 读取重复因子
            repeat_count = next(nybble_stream)
            continue
            
        # 状态 2: 单半字节短游程
        if nyb < dyn_f:
            run_length = nyb
        # 状态 3: 双半字节中游程
        elif nyb <= 13:
            nyb2 = next(nybble_stream)
            run_length = (nyb - dyn_f - 1) * 16 + nyb2 + dyn_f + 1
        # 状态 4: 三半字节长游程
        elif nyb == 14:
            nyb2 = next(nybble_stream)
            nyb3 = next(nybble_stream)
            run_length = (nyb2 - 16) * 16 + nyb3 + dyn_f + 1
            
        # 将当前颜色的像素追加到结果流
        pixel_val = 1 if is_black else 0
        pixels.extend([pixel_val] * run_length)
        
        # 处理垂直扫描行重复
        if repeat_count > 0:
            row_data = pixels[-run_length:]
            for _ in range(repeat_count):
                pixels.extend(row_data)
            repeat_count = 0
            
        # 翻转像素颜色状态 (黑 <-> 白)
        is_black = not is_black
        
    return pixels[:total_pixels]
```

通過這一套極其精密且針對字符形態深度優化的數學狀態機，高德納與 Rokicki 將二十世紀點陣字型的壓縮理論推向了終極的物理極限。
---

## A.5 Windows 3.0 矢量與光柵字體 `.FNT` 二進制頭表全集

在 Windows 3.0 中，微軟將 `.FNT` 資源頭擴展爲 118 字節的龐大結構體，成爲了工業界 16 位與 32 位嵌入式設備的標準點陣參考規範：

```c
#pragma pack(push, 1)
struct Win30FontHeader {
    uint16 dfVersion;           /* 0x0300 代表 Windows 3.0 */
    uint32 dfSize;              /* 包含头部的物理文件总字节大小 */
    char   dfCopyright[60];     /* 60 字节定长版权 ASCII 字符串 */
    uint16 dfType;              /* 0 代表点阵位图光栅字，1 代表早期矢量矢量字 */
    uint16 dfPoints;            /* 设计标称点数磅值 (Point Size) */
    uint16 dfVertRes;           /* 垂直标称设计分辨率 (通常 96 DPI) */
    uint16 dfHorizRes;          /* 水平标称设计分辨率 (通常 96 DPI) */
    uint16 dfAscent;            /* 基线到字形包围盒顶部的距离 (升部) */
    uint16 dfInternalLeading;   /* 字身内部预留重音符号间距 */
    uint16 dfExternalLeading;   /* 行与行之间的推荐外部空隙 */
    uint8  dfItalic;            /* 非零代表斜体 */
    uint8  dfUnderline;         /* 非零代表下划线 */
    uint8  dfStrikeOut;         /* 非零代表删除线 */
    uint16 dfWeight;            /* 字重数值 (100..900, 400 为 Normal, 700 为 Bold) */
    uint8  dfCharSet;           /* 字符集 (0: ANSI, 1: Default, 2: Symbol, 128: Shift-JIS) */
    uint16 dfPixWidth;          /* 若为 0 表示比例变宽字；若非 0 表示全字固定点阵宽度 */
    uint16 dfPixHeight;         /* 点阵像素矩阵的物理总高度 */
    uint8  dfPitchAndFamily;    /* 字体族与间距标志 */
    uint16 dfAvgWidth;          /* 小写字母加权平均宽度 */
    uint16 dfMaxWidth;          /* 字体中最大的字符位图宽度 */
    uint8  dfFirstChar;         /* 支持的首个字符 ASCII 编码 */
    uint8  dfLastChar;          /* 支持的末尾字符 ASCII 编码 */
    uint8  dfDefaultChar;       /* 缺失字符替代符偏移 */
    uint8  dfBreakChar;         /* 单词断句空格字符偏移 */
    uint16 dfWidthBytes;        /* 位图扫描行对齐字节数 */
    uint32 dfDevice;            /* 指向目标设备名称字符串的相对文件偏移量 */
    uint32 dfFace;              /* 指向字体家族名称（如 "Arial"）的相对文件偏移量 */
    uint32 dfBitsPointer;       /* 内存中点阵位图矩阵的绝对地址（文件中预留为 0） */
    uint32 dfBitsOffset;        /* 点阵位图位流相对于文件开头的 32 位绝对字节偏移 */
    uint8  dfReserved;          /* 预留字节 */
    uint32 dfFlags;             /* 标志位 */
    uint16 dfAspace;            /* A 空间间隙（左侧负轴承补偿） */
    uint16 dfBspace;            /* B 空间间隙（位图黑体宽度） */
    uint16 dfCspace;            /* C 空间间隙（右侧轴承补偿） */
    uint32 dfColorPointer;      /* 彩色位图调色板偏移 */
    uint32 dfReserved1[4];      /* 预留对齐填充字 */
};
#pragma pack(pop)
```

通過這一結構，Windows GDI 能夠以納秒級的極速在屏幕顯存（FrameBuffer）中直接執行 `BitBlt` 塊內存拷貝，奠定了早期個人電腦視窗圖形界面飛速普及的性能基礎。
---

## A.6 DOS 代碼頁信息文件（`.CPI`）的段落拓撲與顯卡固件注入

在微軟 MS-DOS 與 IBM PC-DOS 時代，操作系統爲了在 EGA 與 VGA 圖形顯示適配器上切換不同的國家/地區字符集（如代碼頁 437 美國英語、850 西歐多語言、936 簡體中文），採用了專有的 **`.CPI`（Code Page Information）** 點陣字體封裝容器。

### 1. CPI 文件的四級二進制樹狀拓撲：
一個標準的 `.CPI` 文件在物理上由四大層級構成：
1. **Font File Header（字體文件頭）**：
   * `0x19` 字節魔數：`\xFF\x46\x4F\x4E\x54\x20\x20`（"FONT  "）；
   * 預留字段與版本號；
   * `pCodePageEntry`：指向首個代碼頁條目的文件絕對字節偏移。
2. **Code Page Entry Header（代碼頁條目頭）**：
   * `next`：指向下一個代碼頁條目的指針（爲 0 表示鏈表末尾）；
   * `device_type`：目標硬件設備代碼（1: 屏幕顯示適配器 Screen; 2: 針式/激光打印機 PRN）；
   * `device_name`：8 字節 ASCII 設備名稱（如 `"EGA     "` 或 `"4201    "`）；
   * `codepage_id`：DOS 代碼頁整數編號（如 437, 850, 852）；
   * `pFontInfo`：指向具體字體信息的偏移量。
3. **Font Info Header（點陣字體信息頭）**：
   * `version`：字體格式版本號；
   * `num_fonts`：該代碼頁下封裝的不同像素規格點陣字體總數（通常爲 3 種：$8 \times 8$, $8 \times 14$, $8 \times 16$）。
4. **Screen Font Data（屏幕點陣原始字節矩陣）**：
   * 存儲每個字符的點陣位圖。例如對於標準的 $8 \times 16$ VGA 字體，每個字符佔用 16 個連續字節（每行 8 像素佔用 1 字節）。256 個字符恰好佔用：
     $$256 \times 16 \text{ 字节} = 4096 \text{ 字节} = 4 \text{ KB}$$
   DOS 的 `MODE CON: SELECT=...` 命令正是將這 4KB 數據通過顯卡 BIOS 中斷（`INT 10h, AX=1100h`）直接寫入 VGA 顯卡的字符發生器內存平面 2（Plane 2），實現了純硬件級的即時字符渲染！

---

## A.7 X11 PCF 二進制結構與快速加載優化

在 X Window System 誕生初期，雖然 BDF 純文本格式極其易讀，但每次 X 終端啓動或切換字號時，解析數十萬行 ASCII 文本並將其轉換爲二進制點陣極爲耗時。

DEC、MIT 與 X 聯盟推出了 **PCF（Portable Compiled Format）** 格式：
* PCF 預先在磁盤上完成了大小端字節序重排、4 字節內存頁對齊、以及各字符包圍盒的微積分計算；
* 操作系統啓動 X Server 時，只需發起一次底層的 `mmap` 系統調用，即可將全字體瞬間映射至 X11 核心顯存，比 BDF 文本解析提速了整整兩百倍！
---

## A.8 TeX 通用字體格式（GF: Generic Font）核心操作碼全集

高德納在設計 METAFONT 時的原始輸出格式爲 **`.gf`（Generic Font）**。與後續深度壓縮的 `.pk` 格式相比，GF 格式更加直接貼近光柵掃描硬件：

| 操作碼（Hex/Dec） | 助記符 | 參數形態 | 光柵化繪製與解釋器行爲 |
| :--- | :--- | :--- | :--- |
| `0..63` | `paint_0..paint_63` | 無額外參數 | 在當前行交替繪製 $0 \dots 63$ 個連續同色像素（黑/白翻轉） |
| `64..66` | `paint1..paint3` | $k$ 字節無符號數 | 繪製長達數萬像素的連續黑白遊程（參數佔用 1 到 3 字節） |
| `67` | `boc` (Begin of Char) | 四元包圍盒與字符代碼 | **字符開啓首指令**：初始化字符最小最大 $X, Y$ 座標與字符碼點 |
| `68` | `boc1` | 緊湊型字符開始 | 單字節字符編碼且包圍盒尺寸極小時的緊湊格式 |
| `69` | `eoc` (End of Char) | 無 | **字符終結指令**：完成當前字符點陣的繪製，將像素提交輸出緩存 |
| `70` | `skip0` | 無 | 結束當前掃描行，並將畫筆移至下一行起始位置（垂直 $Y$ 減 1） |
| `71..73` | `skip1..skip3` | $k$ 字節整數 | 跨越多行全白空白行（垂直 $Y$ 連續跳躍若干行） |
| `74` | `new_row_0` | 無 | 換行並將當前行橫座標 $X$ 重置爲 0 |
| `243` | `post` (Postamble) | 全局元數據指針 | 字體尾部引導表，存儲指向各字符 `char_loc` 索引的絕對文件指針 |
| `248` | `post_post` | 魔數字節與識別符 | **全文件收尾標識**：後隨 4 字節或更多 `0xDF`（十進制 223）特徵對齊字節 |

GF 格式憑藉其極度的直觀性與嚴格的時序一致性，成爲了 DVI 驅動程序驗證點陣字庫光柵完整性的第一標準。

---

# 附錄 B：TeX 與 Omega 字體度量文件規範（TFM, OFM, VF, OVF）

在計算機排版技術史上，高德納（Donald Knuth）在設計 TeX 系統時提出了一個徹底超越時代的軟硬件解耦範式：**排版排版引擎在計算段落折行、數學公式排版與頁面微積分模型時，根本不需要知道字形的長相（輪廓或位圖），而僅僅需要知道字符的幾何度量盒模型（Metrics Box Model）！**

這一哲學造就了 **TFM（TeX Font Metric）** 格式。在排版過程中，TeX 僅讀取極小體積的 `.tfm` 二進制文件（通常僅幾千字節），極大地降低了內存消耗並提升了排版速度；字形的實際繪製輪廓則完全延遲到設備驅動程序（DVI 驅動、dvips、pdfTeX）在最終輸出紙張或屏幕時才進行綁定。隨後，雅尼斯·哈拉蘭博斯（Yannis Haralambous）與約翰·普萊斯（John Plaice）在開發多語言多方向排版系統 Omega 時，將 TFM 進一步發展爲支持 16 位與 32 位 Unicode 全量字符空間的 **OFM（Omega Font Metrics）** 與 **OVF（Omega Virtual Fonts）**。

---

## B.1 TFM 文件的 12 張核心數據表與二進制拓撲

一個標準的 TFM 文件在磁盤上被組織爲嚴格緊湊的 12 個二進制數組。所有多字節整數一律採用大端序（Big-Endian / Network Byte Order）存儲：

```
+-------------------------------------------------------+
|  0: lf (Length of File, 16-bit)                       |
|  1: lh (Length of Header data, 16-bit)                |
|  2: bc (Smallest character code in font, 16-bit)      |
|  3: ec (Largest character code in font, 16-bit)       |
|  4: nw (Number of words in width table, 16-bit)       |
|  5: nh (Number of words in height table, 16-bit)      |
|  6: nd (Number of words in depth table, 16-bit)       |
|  7: ni (Number of words in italic table, 16-bit)      |
|  8: nl (Number of words in lig/kern table, 16-bit)    |
|  9: nk (Number of words in kern table, 16-bit)        |
| 10: ne (Number of words in extensible table, 16-bit)  |
| 11: np (Number of font parameter words, 16-bit)       |
+-------------------------------------------------------+
|  HEADER (lh words): Checksum, Design Size, etc.       |
+-------------------------------------------------------+
|  CHAR_INFO (ec - bc + 1 words): 4 bytes per char      |
+-------------------------------------------------------+
|  WIDTH (nw words): fix_word fractional dimensions     |
+-------------------------------------------------------+
|  HEIGHT (nh words): fix_word fractional dimensions    |
+-------------------------------------------------------+
|  DEPTH (nd words): fix_word fractional dimensions     |
+-------------------------------------------------------+
|  ITALIC (ni words): fix_word fractional dimensions    |
+-------------------------------------------------------+
|  LIG_KERN (nl words): Ligature & Kerning bytecode     |
+-------------------------------------------------------+
|  KERN (nk words): fix_word kerning amounts            |
+-------------------------------------------------------+
|  EXTEN (ne words): Extensible delimiter recipes       |
+-------------------------------------------------------+
|  PARAM (np words): Font-wide design parameters        |
+-------------------------------------------------------+
```

### 1. 定點數數學體系：`fix_word` 的微積分精度
TFM 文件內部所有的尺寸量度（字寬、字高、字深、字距、數學參數）均採用 32 位有符號定點數 **`fix_word`** 存儲。其內部結構爲一個包含 1 個符號位、11 個整數位與 20 個二進制小數位的定點數：

$$1\text{ fix\_word} = \frac{\text{Value}}{2^{20}} = \frac{\text{Value}}{1,048,576} \times (\text{Design Size})$$

#### `fix_word` 的三大物理法則：
1. `fix_word` 並不是絕對的物理毫米或點數，而是一個**相對於字體標稱設計尺寸（Design Size）的無量綱相對縮放因子**！
2. 內部數值 $1,048,576$（即十六進制 `0x00100000`）精確代表相對倍率 $1.0$；
3. 其數值分辨率達到了驚人的 $\frac{1}{1,048,576} \approx 9.5367 \times 10^{-7}$，即便在將字體放大至數千磅的巨幅海報排版中，也能確保累加舍入誤差絕對小於一個光柵點陣像素！

### 2. `CHAR_INFO` 四字節位域的極致緊湊打包
在 TFM 中，從 `bc` 到 `ec` 的每一個字符僅佔用整整 4 個字節（一個 32 位機器字），高德納通過極其巧妙的位域切片，將四維信息徹底壓縮於其中：

```
+----------------+--------+--------+------------+-----+----------------+
|  width_index   | height | depth  |   italic   | tag |   remainder    |
|    (8 bits)    | (4 bit)| (4 bit)|  (6 bits)  | (2) |    (8 bits)    |
+----------------+--------+--------+------------+-----+----------------+
  Byte 0           Byte 1 (H/D)      Byte 2 (Ital/Tag)   Byte 3
```

* **Byte 0 (`width_index`)**：字寬索引（8 位，0–255）。直接指向 `WIDTH` 數組中該字符的字寬 `fix_word`。注意：`WIDTH[0]` 恆定爲 0.0，若字符缺失則索引填 0；
* **Byte 1 高 4 位 (`height_index`)**：字高索引（0–15）。指向 `HEIGHT` 數組中的 16 種字高之一；
* **Byte 1 低 4 位 (`depth_index`)**：字深索引（0–15）。指向 `DEPTH` 數組中的 16 種字深之一；
* **Byte 2 高 6 位 (`italic_index`)**：傾斜校正與數學間距索引（0–63）。指向 `ITALIC` 數組；
* **Byte 2 低 2 位 (`tag`)**：**核心行爲標籤位（Behavior Tag）**，指示 Byte 3 `remainder` 的解釋語義：
  * `tag = 0 (no_tag)`：常規普通字符，`remainder` 字段無意義（填 0）；
  * `tag = 1 (lig_tag)`：**合字與字距鏈起始**。`remainder` 字段爲該字符在 `LIG_KERN` 字節碼數組中的第一條指令步長索引；
  * `tag = 2 (list_tag)`：**數學定界符遞增鏈表**。用於數學公式排版，`remainder` 給出比當前字符稍大一號的同形字符 ASCII 碼點！例如：小型左括號 '(' 的 `remainder` 指向中型左括號，中型指向大型左括號，大型指向超大型左括號，TeX 據此在行內根據公式高度逐級挑選合適大小的括號；
  * `tag = 3 (ext_tag)`：**無限可伸展定界符配方**。當公式高度超過所有離散預製字符時，`remainder` 指向 `EXTEN` 數組中的一條結構體記錄，指示如何使用頂部、中部、底部與重複構件拼裝出任意高度的巨型大括號或積分號。

### 3. `LIG_KERN` 虛擬字節碼指令集
`LIG_KERN` 表是一個包含了連字融鑄與成對字距調整的微型執行引擎。每條指令佔用 4 個字節：

```c
struct LigKernStep {
    uint8 skip_byte;    /* 跳跃控制字节：若 >= 128 则为停机指令（Stop Step） */
    uint8 next_char;    /* 预期紧随其后的相邻字符码点 */
    uint8 op_byte;      /* 操作码字节：若 >= 128 则为字距微调；若 < 128 则为合字替换 */
    uint8 remainder;    /* 结果：目标字距在 KERN 表中的索引，或新合成的合字码点 */
};
```

#### 指令執行狀態機算法：
1. 欲評估字符對 $(C_1, C_2)$ 是否存在連字或字距調整，首先檢查 $C_1$ 的 `tag` 是否等於 1；
2. 若是，令指令指針 $p = \text{remainder}(C_1)$，進入 `LIG_KERN` 數組循環：
   * 讀取當前步驟：`skip = LIG_KERN[p].skip_byte`；
   * 若 `LIG_KERN[p].next_char == C2`，說明**規則命中**！
     * 若 `op_byte >= 128`：觸發**字距微調（Kern）**！間隙值等於 $\text{KERN}[256 \times (\text{op\_byte} - 128) + \text{remainder}]$；
     * 若 `op_byte < 128`：觸發**合字替換（Ligature）**！替換後生成的新字符爲 `remainder`，同時 `op_byte` 的位域指示是否繼續消耗後續字符；
     * 執行完畢，退出狀態機；
   * 若未命中：
     * 若 `skip >= 128`：說明到達鏈表末端（Stop），規則未匹配，退出；
     * 否則令指針跳躍：$p = p + skip + 1$，繼續下一輪匹配。

### 4. `PARAM` 全局參數表與數學字體 22 維物理參數
`PARAM` 表定義了該字體的宏觀排印物理常數。對於普通正文字體，包含 7 個標準參數：
1. `slant`：字體傾斜率（垂直每上升 1 單位的水平傾斜位移）；
2. `space`：詞間標準空格寬度；
3. `space_stretch`：段落兩端對齊時允許空格被拉伸的最大彈性限度；
4. `space_shrink`：允許空格被壓縮的最大收縮限度；
5. `x_height`：小寫字母 'x' 的標準高度；
6. `quad`：一個全角方（Em）的基準設計寬度；
7. `extra_space`：句號等句末標點後推薦額外追加的間隙。

對於**數學符號字體（Math Symbol Fonts）**與**數學擴展字體（Math Extension Fonts）**，高德納在此擴展了多達 22 個神聖的排印參數：
* `num1`：行間陳列公式（Display style）中分子基線提升高度；
* `num2`：行內文本公式（Text style）中無分數線時的分子提升高度；
* `num3`：行內文本公式中有常規分數線時的分子提升高度；
* `denom1`：行間公式中分母基線壓低深度；
* `denom2`：行內公式中分母壓低深度；
* `sup1`：行間公式中上標基線抬升量；
* `sup2`：行內正文公式中上標抬升量；
* `sup3`：無下標伴隨時的純上標額外抬升；
* `sub1`：常規下標壓低量；
* `sub2`：上標過大時的下標額外避讓壓低；
* `supdrop`：上標構件頂部距基字的最小投影下沉；
* `subdrop`：下標底部距基字的投影下沉；
* `delim1`：行間公式中定界符（如左大括號）的最小覆蓋高度；
* `delim2`：行內公式中定界符的最小高度；
* `axis_height`：數學符號中軸線高度（分數線與減號的絕對垂直中心）。

每一個參數控制着分子分母基線提升、根號連梁厚度、分數線垂直軸心等微積分幾何學常量，成爲了全球數學印藝不可逾越的黃金規範。

---

## B.2 Omega 字體度量（OFM: Omega Font Metrics）對多語言的擴展

隨着計算機排版走向全球化，TFM 基於 8 位 ASCII（最多 256 字符）的設計成爲巨大瓶頸。1994 年，哈拉蘭博斯與普萊斯在 Omega 項目中制定了 **OFM（Omega Font Metrics）** 規範。

### 1. OFM Level 0：16 位 Unicode 寬字符擴展
OFM Level 0 將字符尋址空間擴展至 16 位整數（支持 65,536 個字符），完整覆蓋了當時的 Unicode 基本多語言平面（BMP）：
* 表頭頭部魔數擴展爲 32 位，引入了對多達數十萬字節超大度量表的直接物理尋址；
* `CHAR_INFO` 表中的每一個條目從 4 字節擴展爲 12 字節甚至更長，徹底解除了 16 種字高與 64 種傾斜校正的位域限制；
* 支持長合字鏈與上下文敏感的連字評估。

### 2. OFM Level 1：多方向動態排版支持
在 OFM Level 1 中，Omega 引進了突破性的**四向排印物理座標系統**：
* 文本不僅支持從左向右（L2R），更原生支持從右向左（R2L，如阿拉伯文、希伯來文）、從上到下（T2B，如傳統漢字、滿文）與從下到上；
* 每個字符內部包含針對四種流動方向的獨立包圍盒度量向量；
* 引入了基於上下文模式匹配規則表（Contextual Rule Tables），爲早期希臘語古籍多重變音符與阿拉伯文字符變形提供了直接度量支持。

---

## B.3 虛擬字體系統（VF 與 OVF）的指令執行引擎

虛擬字體（Virtual Fonts, `.vf` 與 `.ovf`）是 TeX 生態中最具黑客智慧的發明之一。它允許排版師**憑空創造一個物理上根本不存在的“合成字體”**！

### 1. 虛擬字體的架構哲學
假設我們希望排版希臘文，但手頭只有一份缺少重音變體字母的 Adobe Times 商業矢量字體，以及一份由 METAFONT 生成的單色重音點陣字體。通過編寫一個 `.vf` 虛擬字體映射文件：
* TeX 引擎在排版時，僅僅將該虛擬字體視爲一個普通的單一字體；
* 當遇到帶重音的希臘字母時，虛擬字體引擎會在後臺將其動態展開爲一段**微型的 DVI 字節碼渲染腳本**：先從物理字體 A 中取出字母輪廓，接着移動繪圖原點，再從物理字體 B 中調出重音符號，最後重合輸出！

### 2. 虛擬字體的 256 操作碼虛擬機指令集
VF 文件內部包含一個完整的微型 DVI 解釋器，其核心操作碼與 DVI 格式高度同構：
* `set_char_0` 至 `set_char_127`（操作碼 0–127）：從當前綁定的物理基字庫中繪製指定字符；
* `set_rule`（操作碼 132）：直接在頁面上繪製一條實心黑矩形連梁或橫線（用於分數線與底線）；
* `push`（操作碼 141）/ `pop`（操作碼 142）：將當前二維繪圖座標 $(x, y)$ 壓入硬件棧或從棧中彈出；
* `right1` 至 `right4`（操作碼 143–146）：沿水平方向推進指定數量的定點數單位；
* `down1` 至 `down4`（操作碼 157–160）：沿垂直方向向下移動；
* `fnt_def1` 至 `fnt_def4`（操作碼 243–246）：在虛擬字體內部聲明引用的外部真實物理字體（包括字名、校驗和與縮放比例）；
* `fnt_num_0` 至 `fnt_num_63`（操作碼 171–234）：快速切換當前正在調用的真實底層字體句柄。

### 3. VPL（Virtual Property List）人類可讀源碼範例
通過 `vptovf` 工具，排版師可將以下人類可讀的 `.vpl` 文件直接編譯爲二進制 `.vf` 與 `.tfm`：

```lisp
(VTITLE An Example Virtual Font for Polytonic Greek)
(DESIGNSIZE R 10.0)
(CHECKSUM O 1234567)
(MAPFONT D 0
   (FONTNAME Times-Roman)
   (FONTCHECKSUM O 1234567)
   (FONTAT R 1.0)
   (FONTDSIZE R 10.0)
   )
(MAPFONT D 1
   (FONTNAME GreekAccents)
   (FONTCHECKSUM O 7654321)
   (FONTAT R 1.0)
   )
(CHARACTER C a
   (CHARWD R 0.5)
   (CHARHT R 0.45)
   (MAP
      (SETCHAR C a)
      )
   )
(CHARACTER O 200 ; Composite alpha with acute accent
   (CHARWD R 0.5)
   (CHARHT R 0.65)
   (MAP
      (PUSH)
      (SETCHAR C a)
      (POP)
      (MOVEUP R 0.2)
      (MOVERIGHT R 0.15)
      (SELECTFONT D 1)
      (SETCHAR C acute)
      )
   )
```

通過這一套極致純粹的虛擬字體架構，TeX 體系無需重新鑄造任何物理字形，即可在排印層實現跨字庫的無限無縫熔鑄與擴展。
---

## B.4 TeX 數學排版引擎 22 維物理參數的幾何代數模型

高德納在《The TeXbook》附錄 G 中，精確公開了 TeX 數學公式排版引擎在二維平面上裝配分子、分母、根號連梁與上下標時的微積分幾何方程。這些方程直接調用 TFM 中的 `PARAM` 數組參數（在數學符號字體中稱爲 $\sigma_1 \dots \sigma_{22}$，在數學擴展字體中稱爲 $\xi_1 \dots \xi_{13}$）：

### 1. 分式（Fractions）分子分母垂直定位方程
對於行間陳列公式（Display Style），分子基線提升量 $u$ 與分母基線下沉量 $v$ 嚴格按以下不等式組約束：

$$u = \sigma_8 \quad (\text{num1}), \qquad v = \sigma_{11} \quad (\text{denom1})$$

若分子底部與分數線頂部的垂直間隙小於分數線厚度 $\xi_8$（`default_rule_thickness`）的 3 倍，系統強制將分子基線上推：

$$u \longleftarrow \max\left( u, \; \text{depth}(\text{Numerator}) + \frac{3}{2} \xi_8 + \frac{1}{2}\xi_8 + \sigma_{22} \right)$$

其中 $\sigma_{22}$（`axis_height`）是數學公式的中軸線高度。分數線的中心嚴格鎖定在 $y = \sigma_{22}$ 處，徹底保證了無論左右兩邊的括號、根號多大，分數線永遠與等號、減號的水平中軸絕對重合！

### 2. 上標與下標（Superscripts & Subscripts）空間避讓算法
設基字高度爲 $h$，深度爲 $d$：
* 上標初始抬升量：
  * 在行間公式中：$u = \sigma_{13}$（`sup1`）；
  * 在正文行內公式中：$u = \sigma_{14}$（`sup2`）；
  * 若上標爲純緊縮樣式（ScriptScript）：$u = \sigma_{15}$（`sup3`）；
* 下標初始下沉量：$v = \sigma_{16}$（`sub1`）；
* **間隙保護不等式**：當上下標同時存在時，上標底部與下標頂部的垂直淨距必須滿足：
  $$(u - \text{depth}(\text{Sup})) - (-v + \text{height}(\text{Sub})) \ge 4 \xi_8$$
  若不滿足，系統強制將下標進一步向下壓低，直到間隙等於 $4 \xi_8$，徹底杜絕了複雜數學符號互相粘連的印刷災難！

---

## B.5 Python 工業級 TFM 二進制解析器實現

```python
import struct

def parse_tfm(data: bytes):
    # 读取 12 个 16 位头表字
    lf, lh, bc, ec, nw, nh, nd, ni, nl, nk, ne, np = struct.unpack(">12H", data[:24])
    print(f"TFM File: {lf} words, Char Range: [{bc}, {ec}]")
    
    offset = 24
    # Header 表 (lh words)
    header = data[offset:offset + lh*4]
    checksum, design_size = struct.unpack(">II", header[:8])
    design_pt = design_size / (1 << 20)
    print(f"Checksum: {checksum:08X}, Design Size: {design_pt:.2f}pt")
    offset += lh * 4
    
    # CHAR_INFO 表 (ec - bc + 1 words)
    num_chars = ec - bc + 1
    char_info = []
    for _ in range(num_chars):
        w_idx, h_d_idx, i_t_idx, rem = struct.unpack(">BBBB", data[offset:offset+4])
        char_info.append({
            'width_index': w_idx,
            'height_index': h_d_idx >> 4,
            'depth_index': h_d_idx & 0x0F,
            'italic_index': i_t_idx >> 2,
            'tag': i_t_idx & 0x03,
            'remainder': rem
        })
        offset += 4
        
    # WIDTH 表 (nw words, 转换为浮点磅值)
    widths = []
    for _ in range(nw):
        val, = struct.unpack(">i", data[offset:offset+4])
        widths.append((val / (1 << 20)) * design_pt)
        offset += 4
        
    return {
        'design_size': design_pt,
        'char_info': char_info,
        'widths': widths
    }
```
---

## B.6 Omega 虛擬字體（OVF）與複雜排版流水線實戰

在多語言排版引擎 Omega 中，虛擬字體技術被推向了前所未有的頂峯：
* **多方向字符映射**：針對從右向左書寫的阿拉伯字母或自上而下書寫的漢字，OVF 內部的 DVI 字節碼能夠動態調整畫筆移動軸向；
* **動態重音合成**：在經典古希臘語多重變音符（Polytonic Greek，包含銳音符、柔音符、強音符、下標角標等多種符號交疊）中，單一物理字體往往缺少組合字形。OVF 在排版時能夠自動計算基字包圍盒頂部座標，並動態將變音符吸附在最佳視學位置，消除了傳統 TeX 宏包繁瑣的純宏計算。

---

# 附錄 C：PostScript 體系字體格式深度參考（Type 1, Type 2/CFF, MM, Type 0, CIDFont）

1984 年，約翰·沃諾克（John Warnock）與查爾斯·格施克（Charles Geschke）創立的 Adobe 公司發佈了 **PostScript 頁面描述語言**。PostScript 不僅是一套繪圖指令，更是一門圖靈完備的逆波蘭棧式編程語言。隨之誕生的 **PostScript Type 1 字體格式**，首次將三次貝塞爾曲線（Cubic Bézier Splines）與高度機密的字體微觀渲染提示（Hinting）機制引入數字印刷，徹底催生了人類的桌面出版革命（DTP Revolution）。

在長達十餘年的時間裏，Adobe 將 Type 1 的核心字節碼解釋器與加密算法視爲最頂級的商業機密，直到 1990 年面對蘋果與微軟聯手推出 TrueType 的巨大競爭壓力，才被迫公開出版了著名的黑皮書《Adobe Type 1 Font Format》。本附錄基於 PostScript 官方規範，對 Type 1、Type 2（CFF）、Multiple Master、Type 0 複合字體以及當今東亞巨型字庫的基石 CID-keyed 字體進行底層的全面技術解密。

---

## C.1 PostScript Type 1 字體的內存拓撲與解密引擎

一個物理上的 Type 1 字體在不同操作系統下有不同的打包載體：
1. **`.PFA`（PostScript Font ASCII）**：純文本封裝格式，常用於 Unix 工作站與通信信道。`eexec` 加密段被編碼爲兩位的十六進制 ASCII 字符串（Hexadecimal-encoded），每行 64 字符；
2. **`.PFB`（PostScript Font Binary）**：二進制封裝格式，常用於 IBM PC 與 Windows 系統。文件由若干個帶 6 字節二進制頭部的記錄塊（Records）拼接而成；
3. **Mac OS `POST` 資源**：在經典 Mac 操作系統中存儲於資源分支（Resource Fork）中的 `POST` 資源段中。

```
+-------------------------------------------------------+
|  .PFB 记录块结构 (Record Header: 6 Bytes)              |
+-------------------------------------------------------+
|  Byte 0:     0x80 (魔数标识符)                          |
|  Byte 1:     记录类型 (0x01: ASCII, 0x02: Binary, 0x03: EOF)
|  Bytes 2-5:  记录长度 (32-bit Little-Endian uint32)    |
|  Bytes 6..N: 载荷数据 (Payload Data)                  |
+-------------------------------------------------------+
```

整個 Type 1 字體由三大邏輯段構成：
1. **ASCII 明文頭部段**：包含字體家族聲明、版權信息與全局元數據字典；
2. **`eexec` 二進制加密段**：受到僞隨機數發生器加密保護的私有核心，包含字體全局微調參數字典 `Private` 與字形輪廓字典 `CharStrings`；
3. **512 字節全零尾部與 `cleartomark` 閉合段**：用於刷新 IBM PC 通信端口與早期激光打印機串口緩衝區。

::: tip PostScript Type 1 字體整體拓撲與 eexec 解密結構（Figure C-1, C-2）
![Type 1 字體整體拓撲（Figure C-1）](/images/fonts-encodings/fig-app-c1.png)
*Type 1 字體整體拓撲（Figure C-1）*
:::

*圖 C-1：PostScript Type 1 字體頂層數據字典組織拓撲。從根目錄 FontDirectory 到 FontInfo、Encoding、Private 與 CharStrings。*

::: tip Type 1 字體 ASCII 頭部與 eexec 加密段（Figure C-2）
![Type 1 字體 eexec 段解構（Figure C-2）](/images/fonts-encodings/fig-app-c2.png)
*Type 1 字體 eexec 段解構（Figure C-2）*
:::

*圖 C-2：Type 1 字體物理文件剖分。明文段通過 `currentfile eexec` 關鍵字瞬間切換爲二進制密碼流。*

### 1. `eexec` 線性同餘解密引擎

進入 `eexec` 關鍵字後，PostScript 解釋器啓動一套 16 位線性同餘僞隨機數發生器（Linear Congruential Generator, LCG）進行實時流式異或解密：

$$R_{n+1} = (R_n \times c_1 + c_2) \bmod M$$

$$P_n = C_n \oplus (R_n \gg 8)$$

* 模數 $M = 65536 = 2^{16}$；
* 乘數 $c_1 = 52845$；
* 增量常數 $c_2 = 22719$；
* **初始密鑰 $R_0 = 52845$**（十六進制 `0xCE6D`）；
* $C_n$ 爲當前讀入的密文字節，$P_n$ 爲解密輸出的明文字節。

**前 4 個隨機字節的丟棄原則**：在 `eexec` 密文的開頭，Adobe 強制填充了 4 個完全隨機生成的無意義字節。解密引擎在完成前 4 輪循環後，必須將這 4 字節明文直接拋棄，從第 5 個字節開始纔是真正的 PostScript 代碼。這一設計的目的在於使相同內容的字庫在每次導出時呈現完全不同的密文散列，破壞早期密碼學者的差分分析！

#### Python 工業級 eexec 解密與加密實現：
```python
def decrypt_type1_cipher(ciphertext: bytes, key: int = 52845, discard: int = 4) -> bytes:
    # PostScript Type 1 线性同余解密算法
    # key = 52845 (eexec) 或 4330 (CharStrings)
    c1 = 52845
    c2 = 22719
    r = key
    plaintext = bytearray()
    for cipher_byte in ciphertext:
        plain_byte = cipher_byte ^ (r >> 8)
        plaintext.append(plain_byte)
        r = ((cipher_byte + r) * c1 + c2) & 0xFFFF
    return bytes(plaintext[discard:])

def encrypt_type1_cipher(plaintext: bytes, key: int = 52845, random_header: bytes = b'\x00\x00\x00\x00') -> bytes:
    # PostScript Type 1 线性同余加密算法
    c1 = 52845
    c2 = 22719
    r = key
    ciphertext = bytearray()
    full_data = random_header + plaintext
    for plain_byte in full_data:
        cipher_byte = plain_byte ^ (r >> 8)
        ciphertext.append(cipher_byte)
        r = ((cipher_byte + r) * c1 + c2) & 0xFFFF
    return bytes(ciphertext)
```

### 2. `FontInfo` 與頂層字典字段全景

在明文段中，`FontDirectory` 註冊的頂層字典包含以下核心鍵值對：
* `FontName`（常字字名符號，如 `/Times-Roman`）；
* `PaintType`（整型：0 爲填充筆畫，2 爲輪廓空心線框）；
* `FontType`（整型：恆爲 1）；
* `FontMatrix`（仿射變換矩陣，通常爲 `[0.001 0 0 0.001 0 0]`，將 1000 柵格單位歸一化爲 1 磅）；
* `FontBBox`（四元實數數組：`[llx lly urx ury]`，全字體的左下角與右上角極限包圍盒）；
* `UniqueID`（24 位整數，用於激光打印機顯存全局光柵緩存索引）；
* `Encoding`（256 元素符號數組，如 `StandardEncoding` 或 `ISOLatin1Encoding`）。

`FontInfo` 子字典則進一步記錄了排版與法律元數據：
* `version`：版本號字符串；
* `Notice`：版權所有聲明；
* `FullName`：人機可讀的完整全名（如 `"Times Roman"`）；
* `FamilyName`：字體家族名（如 `"Times"`）；
* `Weight`：字重描述（`"Regular"`, `"Bold"`, `"Black"` 等）；
* `ItalicAngle`：傾斜角度（正體爲 0.0，西文斜體通常爲 $-12.0$ 度，負號表示順時針右傾）；
* `isFixedPitch`：布爾值（等寬字體爲 `true`，比例變寬字體爲 `false`）；
* `UnderlinePosition`：下劃線中心基準線相對於文本基線的垂直偏移（負值）；
* `UnderlineThickness`：下劃線的推薦物理寬度。

### 3. `Private` 字典與底層渲染微調中樞

解密後的 `eexec` 內部定義了字體的神經中樞——`Private` 字典。它控制着光柵化渲染器在低分辨率下的所有幾何對齊行爲：
* **`BlueValues` 與 `OtherBlues`**：基準藍色對齊帶。定義了基線、x 字高、大寫字高、升部與降部的平頂吸附區間；
* **`FamilyBlues` 與 `FamilyOtherBlues`**：字體家族全局共享的對齊帶，確保同一家族的不同字重在混排時視覺平齊；
* **`BlueScale`, `BlueShift`, `BlueFuzz`**：控制對齊帶隨顯示字號（Point Size）放大時何時解除強行平頂吸附的微調浮點常數；
* **`StdHW` 與 `StdVW`**：全字體的標準主導水平與垂直筆畫寬度；
* **`StemSnapH` 與 `StemSnapV`**：允許吸附對齊的多級候選筆畫寬度數組；
* **`ForceBold`**：布爾值，在小字號極低分辨率下強行將細筆畫加粗一個像素，防止文字筆畫斷裂消失；
* **`LanguageGroup`**：語言組代碼（0 代表拉丁、希臘、西里爾等西文字系；1 代表中日韓繁複漢字字系）；
* **`lenIV`**：指示字形輪廓數據 `CharStrings` 開頭包含的隨機校驗字節數（默認恆爲 4；若設爲 -1 則表示不加密）。

::: tip Type 1 字體 Private 字典與藍色對齊帶空間分佈（Figure C-3, C-4, C-5）
![Private 字典藍色對齊帶（Figure C-3）](/images/fonts-encodings/fig-app-c3.png)
*Private 字典藍色對齊帶（Figure C-3）*
:::

*圖 C-3：BlueValues 與 OtherBlues 在基線、x 字高與大寫字高周圍構築的垂直吸附禁飛區。*

::: tip StdHW 與 StemSnapH 筆畫網格吸附（Figure C-4）
![StdHW 筆畫寬度歸一化（Figure C-4）](/images/fonts-encodings/fig-app-c4.png)
*StdHW 筆畫寬度歸一化（Figure C-4）*
:::

*圖 C-4：水平主幹與垂直主幹寬度通過 StemSnap 陣列強行聚類，消除小字號下筆畫粗細不均的視覺雜訊。*

::: tip Subrs 子程序池與宏指令複用（Figure C-5）
![Subrs 子程序池（Figure C-5）](/images/fonts-encodings/fig-app-c5.png)
*Subrs 子程序池（Figure C-5）*
:::

*圖 C-5：`Subrs` 數組存儲了全字體通用的襯線輪廓、彎角弧線與提示替換宏，供所有字形頻繁調用。*

---

## C.2 Type 1 CharStrings 虛擬機解釋器深度剖析

`CharStrings` 字典內部，每一個字符外觀對應一段經過二次加密的二進制字節流。其解密算法與 `eexec` 完全相同，但**初始密鑰被替換爲 $R_0 = 4330$**。

解密後的字節碼在一個深度爲 24 的微型數值操作數棧上執行。Type 1 CharStrings 擁有極其精簡的操作碼體系，劃分爲單字節基礎指令與 `12` 開頭的雙字節轉義指令：

::: tip Type 1 曲線繪製指令與端點切線控制（Figure C-6, C-7, C-8）
![Type 1 曲線繪製指令（Figure C-6）](/images/fonts-encodings/fig-app-c6.png)
*Type 1 曲線繪製指令（Figure C-6）*
:::

*圖 C-6：`rrcurveto`、`vhcurveto` 與 `hvcurveto` 指令通過 6 個相對座標增量定義一段三次貝塞爾曲線。*

::: tip Type 1 閉合路徑與內部輪廓填充規則（Figure C-7）
![Type 1 閉合路徑（Figure C-7）](/images/fonts-encodings/fig-app-c7.png)
*Type 1 閉合路徑（Figure C-7）*
:::

*圖 C-7：`closepath` 指令將繪製點連接回當前輪廓的起點，形成封閉區域，並依據非零環繞數規則（Non-zero Winding Rule）進行光柵化填充。*

::: tip Type 1 複合字形 seac 指令構造重音字符（Figure C-8）
![Type 1 seac 指令（Figure C-8）](/images/fonts-encodings/fig-app-c8.png)
*Type 1 seac 指令（Figure C-8）*
:::

*圖 C-8：`seac`（Standard Encoding Accented Character）指令通過基字碼點與重音碼點，瞬間在二維空間將兩字合成，大幅節省字體體積。*

### 1. 操作數編碼規則（Operand Encoding）
CharStrings 中的每個字節若處於 `32..255` 之間，則被解釋爲操作數（數值），被直接壓入操作數棧：
* `32 <= b0 <= 246`：直接表示整數 $v = b_0 - 139$（範圍：$-107 \dots +107$）；
* `247 <= b0 <= 250`：雙字節正整數 $v = (b_0 - 247) \times 256 + b_1 + 108$（範圍：$+108 \dots +1131$）；
* `251 <= b0 <= 254`：雙字節負整數 $v = -(b_0 - 251) \times 256 - b_1 - 108$（範圍：$-1131 \dots -108$）；
* `b0 == 255`：隨後跟隨 4 字節的大端序 32 位有符號整數。

### 2. 核心操作碼字典全集

| 操作碼（Hex/Dec） | 指令名稱 | 參數棧形態 | 幾何繪製與虛擬機執行行爲 |
| :--- | :--- | :--- | :--- |
| `0x01 (1)` | `hstem` | $y \quad dy$ | 聲明一條水平筆畫提示（從絕對座標 $y$ 起，垂直寬度爲 $dy$） |
| `0x03 (3)` | `vstem` | $x \quad dx$ | 聲明一條垂直筆畫提示（從絕對座標 $x$ 起，水平寬度爲 $dx$） |
| `0x04 (4)` | `vmoveto` | $dy$ | 沿垂直軸相對移動當前畫筆 $dy$ 距離（水平不移動） |
| `0x05 (5)` | `rlineto` | $dx \quad dy$ | 從當前畫筆繪製一條直線至相對座標 $(dx, dy)$ |
| `0x06 (6)` | `hlineto` | $dx$ | 繪製一條水平直線，距離爲 $dx$ |
| `0x07 (7)` | `vlineto` | $dy$ | 繪製一條垂直直線，距離爲 $dy$ |
| `0x08 (8)` | `rrcurveto` | $dx_1 dy_1 dx_2 dy_2 dx_3 dy_3$ | 繪製一段三次貝塞爾曲線，三對增量分別爲第一控制點、第二控制點與曲線終點 |
| `0x09 (9)` | `closepath` | $\emptyset$ | 閉合當前子路徑輪廓 |
| `0x0A (10)` | `callsubr` | $subr\_index$ | 調用 `Subrs` 數組中索引爲 $subr\_index$ 的子程序 |
| `0x0B (11)` | `return` | $\emptyset$ | 從當前子程序返回主調用流程 |
| `0x0D (13)` | `hsbw` | $sb_x \quad wx$ | **字形初始化首指令**：設置水平左側軸承 $sb_x$ 與字符總前進字寬 $wx$ |
| `0x0E (14)` | `endchar` | $\emptyset$ | **字形終結指令**：終結當前字符的繪製，將光柵緩存提交至輸出器 |
| `0x15 (21)` | `rmoveto` | $dx \quad dy$ | 二維平面相對移動當前畫筆 |
| `0x16 (22)` | `hmoveto` | $dx$ | 沿水平軸相對移動當前畫筆 |
| `0x1E (30)` | `vhcurveto` | $dy_1 dx_2 dy_2 dx_3$ | 垂直起刀、水平落刀的簡寫貝塞爾曲線（首控制點水平位移爲 0，終控制點垂直位移爲 0） |
| `0x1F (31)` | `hvcurveto` | $dx_1 dx_2 dy_2 dy_3$ | 水平起刀、垂直落刀的簡寫貝塞爾曲線 |
| `0x0C 0x00` | `dotsection` | $\emptyset$ | 聲明進入或退出字符上的點狀微小特徵（如字母 'i', 'j' 上的圓點） |
| `0x0C 0x01` | `vstem3` | $x_1 dx_1 x_2 dx_2 x_3 dx_3$ | 同時聲明三條等距的垂直筆畫提示（如字母 'm' 的三根立柱） |
| `0x0C 0x02` | `hstem3` | $y_1 dy_1 y_2 dy_2 y_3 dy_3$ | 同時聲明三條等距的水平筆畫提示（如字母 'E' 的三根橫線） |
| `0x0C 0x06` | `seac` | $asb \quad adx \quad ady \quad bchar \quad achar$ | 標準重音合成：將基字 $bchar$ 與重音 $achar$ 在位移 $(adx, ady)$ 處瞬間拼接 |
| `0x0C 0x07` | `sbw` | $sb_x \quad sb_y \quad wx \quad wy$ | 完整四維軸承設置（包含垂直排版時的垂直軸承與前進高） |
| `0x0C 0x0C` | `div` | $num_1 \quad num_2$ | 整數除法：將棧頂兩數彈出並壓入商 $num_1 / num_2$ |
| `0x0C 0x10` | `callothersubr` | $arg_1 \dots arg_n \quad n \quad proc$ | 調用解釋器底層的驅動級擴展程序（用於 Flex 弧線與動態提示替換） |
| `0x0C 0x11` | `pop` | $\emptyset$ | 將 `callothersubr` 返回的結果從專用暫存器彈出至操作數棧 |

### 3. Flex 彈性微弧算子（Flex Operator）

當字母輪廓中包含極其平緩的淺弧線（例如字母大寫 'O' 或加長破折號的微凸弧度）時，在低分辨率屏幕上如果強行光柵化爲曲線，往往會因像素階梯效應產生一個極其醜陋刺眼的孤立凸起像素；而在高分辨率激光照排機上，排版師又必須忠實呈現該優美的弧度。

::: tip Flex 算子幾何判據與雙軌渲染切換（Figure C-9, C-10）
![Flex 算子幾何判據（Figure C-9）](/images/fonts-encodings/fig-app-c9.png)
*Flex 算子幾何判據（Figure C-9）*
:::

*圖 C-9：Flex 算子的幾何控制骨架。包含起點、兩個控制點、中途鞍點、以及終點共 7 組二維座標。*

::: tip Flex 在低分辨率與高分辨率下的不同輸出（Figure C-10）
![Flex 雙軌渲染（Figure C-10）](/images/fonts-encodings/fig-app-c10.png)
*Flex 雙軌渲染（Figure C-10）*
:::

*圖 C-10：Flex 動態決策：若該弧度矢高在當前顯示設備上摺合像素小於等於 0.5 像素（由 `BlueShift` 閾值控制），解釋器強制將其退化爲一條筆直的水平直線（`rlineto`）；一旦設備分辨率提升使弧度達到 1 像素以上，解釋器自動無縫切換爲兩條平滑拼接的三次貝塞爾曲線！*

### 4. 動態提示替換（Hint Substitution）

在複雜漢字或包含密集筆畫的西文符號（如貨幣符號 '$'、數字 '8'、字母 'B'）中，一個字符從左至右或從上到下存在數十條筆畫。由於 Type 1 虛擬機的提示寄存器容量有限，若在字符開頭一次性激活所有提示，會導致空間重疊與邏輯死鎖。

::: tip 動態提示替換在西文與漢字中的應用（Figure C-11, C-12）
![動態提示替換機制（Figure C-11）](/images/fonts-encodings/fig-app-c11.png)
*動態提示替換機制（Figure C-11）*
:::

*圖 C-11：Hint Substitution 通過調用 `callothersubr 3`，在繪製完字符上半部分後，瞬間抹除舊提示並重新聲明一套全新的筆畫提示集合。*

::: tip 漢字複雜筆畫 Hinting 拆解（Figure C-12）
![漢字 Hinting 拆解（Figure C-12）](/images/fonts-encodings/fig-app-c12.png)
*漢字 Hinting 拆解（Figure C-12）*
:::

*圖 C-12：在巨型中文字符排版中，Hint Substitution 沿書寫筆順逐筆激活局部提示，徹底消除了筆畫粘連。*

---

## C.3 CFF 容器與 Type 2 CharStrings 規範

1996 年，Adobe 在推出 OpenType 架構時，對 Type 1 進行了全方位的現代化重構，推出了 **CFF（Compact Font Format）** 與 **Type 2 CharStrings**：

### 1. CFF 內部索引表（INDEX Table）二進制佈局

CFF 徹底廢除了 PostScript 文本解釋器，採用純二進制數據佈局。其核心是通用的 **INDEX 結構**：
* `uint16 count`：對象總數；
* `uint8 offSize`：偏移數組每個指針佔用的字節寬度（1 到 4 字節）；
* `uint<offSize> offset[count + 1]`：累加字節偏移數組；
* `uint8 data[...]`：連續對象二進制載荷。

### 2. CFF 頂層段落拓撲

一個合法的 CFF 表嚴格按序包含：
1. `Header`：魔數與版本號（通常爲 `1.0`，四個字節：`0x01, 0x00, 0x04, 0x04`）；
2. `Name INDEX`：包含的字體家族名稱字符串；
3. `Top DICT INDEX`：頂層鍵值對字典（記錄 CharStrings 偏移、編碼表偏移、私有字典偏移）；
4. `String INDEX`：全字體共享的字符串池（索引 391 之後自定義字符串）；
5. `Global Subr INDEX`：全局通用子程序池；
6. `Encodings` / `Charsets`：字符編碼與字形名稱映射；
7. `FDSelect` / `Font DICT INDEX`（針對 CIDFont）：多子字族分類選擇表；
8. `CharStrings INDEX`：所有字形的 Type 2 輪廓字節碼；
9. `Private DICT`：各字族的局部私有微調字典；
10. `Local Subr INDEX`：局部子程序池。

### 3. Type 2 CharStrings 的顛覆性算子

* **`hintmask` 與 `cntrmask`**：在字形輪廓指令流中間，直接緊隨一個根據已聲明提示總數決定的位掩碼字節數組（例如 24 條提示佔用 3 字節）。解釋器在 1 字節開銷內瞬間激活指定的筆畫提示集合，徹底淘汰了 Type 1 繁瑣的 `callothersubr 3`！
* **`blend` 算子**：用於支持可變字體（Variable Fonts）與多重母版，在單次計算中完成多個設計母版座標的線性組合；
* **暫存數組與算術指令**：支持 `put`（將棧頂數存入暫存槽）、`get`（提取暫存數）、`add`, `sub`, `mul`, `div`, `sqrt`, `neg`, `abs`, `random` 等高階代數運算。

---

## C.4 多重母版字體（Multiple Master Fonts）與連續設計軸

1991 年，Adobe 研發了代表模擬排印巔峯的 **Multiple Master（MM）技術**。MM 允許字體設計師在多維幾何空間中建立連續變形軸線：

::: tip Multiple Master 二維與三維設計空間拓撲（Figure C-13, C-14）
![MM 設計空間拓撲（Figure C-13）](/images/fonts-encodings/fig-app-c13.png)
*MM 設計空間拓撲（Figure C-13）*
:::

*圖 C-13：由字重軸（Weight: Light to Black）與字寬軸（Width: Condensed to Expanded）構成的二維笛卡爾設計空間。*

::: tip MM 母版輪廓拓撲同構與控制點對應（Figure C-14）
![MM 輪廓拓撲同構（Figure C-14）](/images/fonts-encodings/fig-app-c14.png)
*MM 輪廓拓撲同構（Figure C-14）*
:::

*圖 C-14：多重母版插值鐵律：參與混配的所有母版字形，其貝塞爾輪廓必須保持**嚴格絕對的拓撲同構**！即控制點總數、起刀點編號、線段與曲線段的順序必須逐一精確對應。*

### 多重母版數學插值模型：

設設計空間包含 $k$ 個軸線，空間頂點由 $2^k$ 個極端母版字形 $M_1, M_2, \dots, M_{2^k}$ 錨定。對於用戶給定的任意歸一化設計座標 $(w_1, w_2, \dots, w_k) \in [0, 1]^k$，排版引擎通過多線性基函數計算各母版的加權權重 $W_i$：

$$P = \sum_{i=1}^{2^k} W_i M_i, \quad \text{其中 } \sum W_i = 1$$

生成的衍生字形繼承了所有母版的優秀基因，在 Adobe Acrobat SuperATM 中實現了對任意未知版面字體的無損克隆！

---

## C.5 Type 0 複合字體（Composite Fonts）

在處理中日韓（CJK）等包含數萬漢字的龐大書寫系統時，傳統 PostScript 字典 256 個字符的上限徹底失效。Adobe 由此設計了 **Type 0 複合字體架構**：

::: tip Type 0 複合字體樹狀尋址分發體系（Figure C-15）
![Type 0 複合字體分發（Figure C-15）](/images/fonts-encodings/fig-app-c15.png)
*Type 0 複合字體分發（Figure C-15）*
:::

*圖 C-15：Type 0 字體的樹狀解析管線。頂層 Type 0 字體不包含任何輪廓，而是一個路由交換機：通過 `FMapType` 算法將輸入的雙字節字符編碼拆分爲高字節與低字節，將高字節作爲索引在 `FDepVector`（子字體依賴向量）中查得對應的底層 Type 1 子字庫，再用低字節在子字庫中提取具體輪廓。*

---

## C.6 CID-keyed 字體體系與 CMap 映射映射學

Type 0 架構雖然解決了字符數量限制，但存在嚴重的性能缺陷：將漢字硬生生割裂進數十個小字庫導致字間距、度量表極度碎片化，且強行綁定了特定的本地化編碼（如 Shift-JIS 或 Big5）。

1993 年，Adobe 推出了現代泛東亞字型的終極標準——**CID-keyed 字體（CIDFontType 0 與 CIDFontType 2）**：

::: tip CID-keyed 字符標識符與 CMap 分離架構（Figure C-16, C-17）
![CID 架構圖解（Figure C-16）](/images/fonts-encodings/fig-app-c16.png)
*CID 架構圖解（Figure C-16）*
:::

*圖 C-16：字符集與字形集的徹底解耦。字庫內部所有字形按 0 到 65535 的純數字 CID（Character Identifier）無序線性排列，所有外部編碼映射完全交由外掛的 CMap 文件裁決。*

::: tip CMap 文件在多編碼環境下的動態映射（Figure C-17）
![CMap 映射機制（Figure C-17）](/images/fonts-encodings/fig-app-c17.png)
*CMap 映射機制（Figure C-17）*
:::

*圖 C-17：同一款 CID 字體（如 Adobe-Japan1-6），掛載 `UniJIS-UTF16-H` 即可作爲 Unicode 字體使用，掛載 `90ms-RKSJ-H` 即可原生支持日文 Windows Shift-JIS 編碼，掛載垂直排版 CMap 即可瞬間激活豎排字形，實現了數字字型史上最偉大的一次架構大一統！*

### 1. CMap 語法規範與映射條目

一個典型的 CMap 文件由以下核心段構成：
```postscript
/CIDInit /ProcSet findresource begin
12 dict begin
begincmap
/CIDSystemInfo 3 dict dup begin
  /Registry (Adobe) def
  /Ordering (Japan1) def
  /Supplement 6 def
end def
/CMapName /UniJIS-UTF16-H def
/CMapVersion 1.018 def
/CMapType 1 def
/UIDOffset 0 def
/XUID [1 10 25330] def
/WMode 0 def % 0 = Horizontal, 1 = Vertical

% 声明编码空间范围 (1 到 4 字节)
1 begincodespacerange
  <0000> <FFFF>
endcodespacerange

% 单字符映射 (Character to CID)
10 beginbfchar
  <0020> 1
  <0021> 2
endbfchar

% 范围连续映射 (Range to CID)
25 begincidrange
  <0022> <005F> 3
  <0060> <007E> 65
endcidrange

endcmap
CMapName currentdict /CMap defineresource pop
end
end
```

通過將字符與字形完全解耦，CMap 文件不僅支持一對一的直接尋址，更通過垂直變體（`V` 系列 CMap）與豎排度量表實現了無縫的縱向書寫切換。
---

## C.7 CFF 字典鍵值與二進制操作碼權威詞典

在 CFF 容器中，所有的屬性字典（Top DICT 與 Private DICT）均採用極其緊湊的**逆波蘭鍵值字節碼**存儲：操作數（數值）在前，操作符（Operator）在後。單字節操作符佔用 `0..21`（除 12 外），雙字節操作符以 `12` 開頭。

### 1. Top DICT 核心操作符全集：

| 操作符字節（Hex） | 鍵名（Key Name） | 參數類型 | 默認值 | 語義與排印功能 |
| :--- | :--- | :--- | :--- | :--- |
| `0x00 (0)` | `version` | SID (String ID) | 無 | 字體版本字符串索引 |
| `0x01 (1)` | `Notice` | SID | 無 | 版權聲明字符串索引 |
| `0x02 (2)` | `FullName` | SID | 無 | 人機可讀全名字串索引 |
| `0x03 (3)` | `FamilyName` | SID | 無 | 字體家族名稱索引 |
| `0x04 (4)` | `Weight` | SID | 無 | 字重描述（如 "Bold"） |
| `0x05 (5)` | `FontBBox` | 4 個數值 | `0 0 0 0` | 全字體極限全局包圍盒 `[llx lly urx ury]` |
| `0x0D (13)` | `UniqueID` | 整數 | 無 | PostScript 全局緩存唯一 ID |
| `0x0E (14)` | `XUID` | 數組 | 無 | 擴展唯一 ID 序列（用於 PDF 嵌入緩存） |
| `0x0F (15)` | `charset` | 偏移量 (offset) | 0 (ISO-Adobe) | 字形字符集映射表相對於 CFF 表首的字節偏移 |
| `0x10 (16)` | `Encoding` | 偏移量 (offset) | 0 (StandardEncoding) | 字符編碼表相對於 CFF 表首的字節偏移 |
| `0x11 (17)` | `CharStrings` | 偏移量 (offset) | 無 | **核心指針**：字形 Type 2 輪廓索引表的字節偏移 |
| `0x12 (18)` | `Private` | 長度與偏移量 | 無 | **神經中樞**：私有微調字典的字節長度與其起始偏移 |
| `0x0C 0x01` | `isFixedPitch` | 布爾值 | `false (0)` | 是否爲等寬字體 |
| `0x0C 0x02` | `ItalicAngle` | 數值 | `0.0` | 斜體傾斜角度 |
| `0x0C 0x03` | `UnderlinePosition` | 數值 | `-100` | 下劃線垂直基準線位置 |
| `0x0C 0x04` | `UnderlineThickness` | 數值 | `50` | 下劃線推薦物理厚度 |
| `0x0C 0x07` | `FontMatrix` | 6 元素數組 | `[0.001 0 0 0.001 0 0]` | 歸一化仿射變換矩陣 |
| `0x0C 0x1E` | `ROS` | 3 個 SID | 無 | **CIDFont 專屬**：Registry、Ordering 與 Supplement 三元組 |
| `0x0C 0x1F` | `CIDFontVersion` | 數值 | `0` | CID 字體版本號 |
| `0x0C 0x24` | `FDArray` | 偏移量 | 無 | **CIDFont 專屬**：子字體字典索引表（Font DICT INDEX）偏移 |
| `0x0C 0x25` | `FDSelect` | 偏移量 | 無 | **CIDFont 專屬**：字形到子字體分類映射表偏移 |

---

### 2. Private DICT 核心操作符全集：

| 操作符字節（Hex） | 鍵名（Key Name） | 參數類型 | 默認值 | 語義與光柵化控制功能 |
| :--- | :--- | :--- | :--- | :--- |
| `0x06 (6)` | `BlueValues` | 偶數個增量數組 | 無 | 主對齊帶（包含基線下沉與上衝對齊區間） |
| `0x07 (7)` | `OtherBlues` | 偶數個增量數組 | 無 | 輔助對齊帶（包含降部底部對齊區間） |
| `0x08 (8)` | `FamilyBlues` | 偶數個增量數組 | 無 | 家族共享主對齊帶 |
| `0x09 (9)` | `FamilyOtherBlues`| 偶數個增量數組 | 無 | 家族共享輔助對齊帶 |
| `0x0A (10)` | `StdHW` | 數值 | 無 | 標準水平主筆畫寬度 |
| `0x0B (11)` | `StdVW` | 數值 | 無 | 標準垂直主筆畫寬度 |
| `0x0C 0x09` | `BlueScale` | 浮點數 | `0.039625` | 對齊帶隨字號放大時解除吸附的閾值係數 |
| `0x0C 0x0A` | `BlueShift` | 數值 | `7` | 超出對齊帶多少單位後強制取消對齊的突變閾值 |
| `0x0C 0x0B` | `BlueFuzz` | 數值 | `1` | 對齊帶邊界容錯擴展像素 |
| `0x0C 0x0C` | `StemSnapH` | 遞增數組 | 無 | 允許吸附對齊的多級水平筆畫寬度候選表 |
| `0x0C 0x0D` | `StemSnapV` | 遞增數組 | 無 | 允許吸附對齊的多級垂直筆畫寬度候選表 |
| `0x0C 0x0E` | `ForceBold` | 布爾值 | `false` | 小字號極小分辨率下是否強行加粗細筆畫 |
| `0x0C 0x11` | `LanguageGroup` | 整數 | `0` | 語言羣組代碼（0: 拉丁系; 1: 中日韓繁複漢字系） |
| `0x0C 0x13` | `Subrs` | 偏移量 | 無 | 本私有字典專屬的局部子程序池偏移（Local Subrs） |
| `0x14 (20)` | `defaultWidthX` | 數值 | `0` | 全字庫大多數字符共享的默認水平字寬 |
| `0x15 (21)` | `nominalWidthX` | 數值 | `0` | 字寬差分基數（實際字寬 = 存儲增量 + nominalWidthX） |

---

### 3. Type 2 CharStrings 顛覆性指令全集權威字典

Type 2 徹底優化了 Type 1 指令流的冗餘。其操作碼體系更加高效緊湊：

#### 堆棧算術與邏輯運算指令：
* `0x0C 0x03 (and)`：邏輯與；
* `0x0C 0x04 (or)`：邏輯或；
* `0x0C 0x05 (not)`：邏輯非；
* `0x0C 0x09 (abs)`：絕對值；
* `0x0C 0x0A (add)`：加法；
* `0x0C 0x0B (sub)`：減法；
* `0x0C 0x0C (div)`：除法；
* `0x0C 0x0E (neg)`：求負數；
* `0x0C 0x0F (eq)`：相等判定；
* `0x0C 0x1A (sqrt)`：開平方；
* `0x0C 0x18 (drop)`：丟棄棧頂元素；
* `0x0C 0x1B (dup)`：複製棧頂；
* `0x0C 0x1C (exch)`：交換棧頂兩元素；
* `0x0C 0x1D (index)`：提取指定深度操作數；
* `0x0C 0x1E (roll)`：操作數棧循環滾動；
* `0x0C 0x14 (put)`：將數值存入暫存數組槽位 $i$；
* `0x0C 0x15 (get)`：從暫存數組槽位 $i$ 提取數值壓棧；
* `0x0C 0x16 (ifelse)`：條件三目選擇運算。

#### 提示掩碼指令（`hintmask` 與 `cntrmask`）：
* **操作碼 `0x13 (19)` (`hintmask`)**：
  在一條字形輪廓中，若首先聲明瞭 $H$ 條水平提示與 $V$ 條垂直提示，則提示總數爲 $N = H + V$。
  緊隨 `hintmask` 操作碼之後，直接內嵌 $\lceil N / 8 \rceil$ 個字節的二進制位掩碼！
  每一個位（Bit）對應一條提示：若第 $k$ 位爲 1，則指示當前輪廓從此時此刻起，瞬間激活第 $k$ 號提示；若爲 0 則靜默禁用該提示。
  這使得包含數十條複雜筆畫的漢字（如“囊”、“龘”）能夠在單個字符內部自由切分局部微觀幾何，且額外字節開銷極其微小！
* **操作碼 `0x14 (20)` (`cntrmask`)**：
  專門用於聲明筆畫中軸線與內部對稱留白（Counter）的排他性約束，保證在超低分辨率下小寫字母 'm' 的兩個拱門或漢字“三”的三條間隙均勻等距。

---

### 4. 工業級 CFF INDEX 解析器 Python 實現

```python
import struct

class CFFIndex:
    def __init__(self, data: bytes, offset: int = 0):
        self.count, = struct.unpack(">H", data[offset:offset+2])
        self.items = []
        if self.count == 0:
            self.total_size = 2
            return
            
        self.off_size = data[offset+2]
        offsets_start = offset + 3
        offsets_count = self.count + 1
        
        # 动态解析 1 到 4 字节的变宽偏移量
        raw_offsets = []
        for i in range(offsets_count):
            pos = offsets_start + i * self.off_size
            chunk = b'\x00' * (4 - self.off_size) + data[pos:pos+self.off_size]
            val, = struct.unpack(">I", chunk)
            raw_offsets.append(val)
            
        data_base = offsets_start + offsets_count * self.off_size - 1
        for i in range(self.count):
            item_start = data_base + raw_offsets[i]
            item_end = data_base + raw_offsets[i+1]
            self.items.append(data[item_start:item_end])
            
        self.total_size = (offsets_start + offsets_count * self.off_size + raw_offsets[-1] - 1) - offset

    def __len__(self):
        return self.count

    def __getitem__(self, idx):
        return self.items[idx]
```

通過這一套高度濃縮、架構統一的現代矢量二進制規範，PostScript CFF 體系在維持了 Type 1 極致平滑的三次貝塞爾曲線與高級提示的同時，將全字庫體積削減了 40% 以上，成爲了當今印刷出版工業無可爭議的矢量基石。
---

## C.8 多重母版字體（Multiple Master）動態實例生成實戰

在 PostScript 解釋器內部，用戶可以通過動態混合（Blend）直接派生出全新的物理字體實例：

```postscript
% 查找基础多重母版字体
/MinionMM findfont

% 在二维设计空间中定义归一化插值坐标：
% 字重轴权重 0.45 (Light到Black之间)，字宽轴权重 0.80 (紧缩到宽体之间)
[0.45 0.80] makeblendedfont

% 将生成的派生字体注册为全局字体
/Minion-Custom findfont
12 scalefont
setfont

% 在页面上排版输出
100 700 moveto
(Voile Magic Library: Multiple Master Dynamic Instance) show
showpage
```

### 線性與非線性空間插值微積分：
在實際工程中，字體設計師往往要求插值不是簡單的線性漸變，而是遵循視覺平衡曲線。Adobe MM 引入了 `NormalizeDesignVector` 映射函數：
對於設計軸輸入座標 $d_j \in [D_{j, \min}, D_{j, \max}]$，通過分段線性查找表將其非線性映射爲歸一化混合標量 $w_j \in [0, 1]$，再通過 Kronecker 積計算最終的 $2^k$ 個極端母版加權矩陣：

$$\mathbf{W} = \bigotimes_{j=1}^k \begin{pmatrix} 1 - w_j \\ w_j \end{pmatrix}$$

這一數學框架，成爲了二十五年後現代 OpenType 1.8 矢量可變字體（Variable Fonts / Variations `fvar`, `gvar`, `HVAR`, `MVAR`）的理論祖先！

---

## C.9 東亞巨型字符集 ROS（Registry-Ordering-Supplement）全景譜系

在 CID-keyed 字體體系中，字符集的版本與規模由 **ROS 三元組** 嚴格定義：

| 字符集集合名稱 | 適用的文字與國家/地區 | 字符總數 (Supplement) | 核心涵蓋範圍與標準 |
| :--- | :--- | :--- | :--- |
| **Adobe-Japan1-6** | 日文（漢字 Kanji、平假名、片假名） | 23,058 字形 (Supp 6) | JIS X 0208, JIS X 0213, JIS X 0212, 印刷用人名漢字變體、縱排變體 |
| **Adobe-GB1-5** | 中國大陸簡體中文 | 30,284 字形 (Supp 5) | GB 2312, GB 13000.1, GBK, GB 18030-2000, 繁體字及少數民族拼音 |
| **Adobe-CNS1-7** | 中國臺灣/香港繁體中文 | 19,088 字形 (Supp 7) | Big5, Big-5E, CNS 11643 第 1-15 字母字面、香港增補字符集 (HKSCS) |
| **Adobe-Korea1-2** | 韓國與朝鮮諺文（Hangul）及漢字 | 18,352 字形 (Supp 2) | KS X 1001, KS X 1002, 常用諺文音節塊及韓國古漢字 |

每一個 Supplement 保持絕對的**向後單調遞增兼容性**：新版本僅在數組末尾追加全新的 CID 編號，絕不修改或刪除既有的歷史 CID，徹底杜絕了跨版本文檔重新排版時的文字跑位風險！
---

## C.10 CFF 規範前 391 個預定義標準字符串（Standard Strings）架構

在 CFF 容器中，爲了極致壓縮字體體積，Adobe 在標準規範（Adobe Technical Note #5176）中硬編碼固化了 **391 個最常用的全語言字形名稱字符串**。在 `Top DICT`、`Private DICT` 或字形名稱尋址中：
* 任何 String ID（SID）若落在 `0 <= SID <= 390` 之間，**完全不需要在字體文件的 `String INDEX` 中佔用任何字節**！解碼引擎直接在靜態標準字符串數組中查表；
* 自定義字形名稱（如漢字 GID、私有合字）的 SID 從 391 開始分配，實際存儲在 `String INDEX` 中的物理索引爲 $\text{CustomSID} = \text{SID} - 391$。

### 核心標準字符串索引分佈表（節選）：

| SID 範圍 | 代表性字形符號名稱 | 用途與排印歸屬 |
| :--- | :--- | :--- |
| `0` | `.notdef` | 缺失字符默認外觀 |
| `1..10` | `space`, `exclam`, `quotedbl`, `numbersign`, `dollar`, `percent`, `ampersand`, `quoteright`, `parenleft`, `parenright` | 基礎 ASCII 標點符號 |
| `11..26` | `asterisk`, `plus`, `comma`, `hyphen`, `period`, `slash`, `zero`..`nine` | 運算符與阿拉伯數字 |
| `27..52` | `A` 至 `Z` | 大寫拉丁英文字母 |
| `53..78` | `a` 至 `z` | 小寫拉丁英文字母 |
| `96..145` | `Agrave`, `Aacute`, `Acircumflex`, `Atilde`, `Adieresis`, `Aring`, `Ccedilla`, `Egrave`, `Eacute`, `Igrave`, `Ntilde`, `Oacute`, `Uacute` | 西歐重音大寫字母 |
| `146..195` | `agrave`, `aacute`, `acircumflex`, `atilde`, `adieresis`, `aring`, `ccedilla`, `egrave`, `eacute`, `igrave`, `ntilde`, `oacute`, `uacute` | 西歐重音小寫字母 |
| `196..250` | `fi`, `fl`, `dotlessi`, `grave`, `acute`, `circumflex`, `tilde`, `macron`, `breve`, `dotaccent`, `dieresis`, `ring`, `cedilla`, `hungarumlaut`, `ogonek` | 經典拉丁連字與獨立變音符 |
| `251..390` | `Euro`, `trademark`, `perthousand`, `bullet`, `copyright`, `registered`, `ellipsis`, `dagger`, `daggerdbl`, `guillemotleft`, `guillemotright` | 國際通用貨幣符號與出版商印刷符號 |

通過這一天才設計，全套包含西歐 200 多個拉丁字符的 CFF 字體，其 `String INDEX` 內部往往**僅需存儲家族名稱與字型版本兩個短字串**，字符串表體積被壓縮至令人驚歎的 20 字節以內！

---

## C.11 複雜符號 Type 1 CharStrings 真實字節碼反彙編跟蹤（以字符 '$' 爲例）

貨幣美元符號 `$` 是字體設計中幾何複雜度最高的符號之一：它由一個平滑雙重彎曲的 'S' 形曲線軀幹與一到兩條垂直貫穿的主幹立柱構成，在有限的鉛字空間中存在多達 4 條水平提示與 4 條垂直提示。

以下爲一段真實的 Type 1 解密字節碼指令序列及其物理執行過程：

```postscript
% 1. 设置水平左侧轴承为 50，前进字宽为 500
50 500 hsbw

% 2. 声明字符上半部分的初始水平与垂直提示
% 顶部横弧 (y=650, dy=40) 与 中部横梁 (y=360, dy=35)
650 40 360 35 hstem
% 左右垂直干提示 (x=230, dx=40)
230 40 vstem

% 3. 绘制顶部衬线与第一段曲线
230 650 rmoveto
40 hlineto
-15 -30 -40 -35 -80 -40 rrcurveto

% 4. 触发动态提示替换 (Hint Substitution)
% 抹除上半部提示，激活中腰与下半部的全新笔画提示集合！
1 3 callothersubr pop
150 40 hstem % 底部横弧提示
210 40 vstem % 下干提示

% 5. 继续绘制穿越中腰的平滑反向曲线
-30 -20 -40 -30 -30 -60 rrcurveto
0 -50 vlineto
closepath

% 6. 终结绘制，提交光栅缓冲区
endchar
```

在執行 `callothersubr 3` 的瞬間，光柵化引擎重置幾何對齊網格，使美元符號上下兩個封閉線圈在低分辨率下互不干涉，完美維持了對稱飽滿的印刷輪廓。
---

## C.12 Type 0 複合字體 FMapType 尋址算法與映射模式全集

在 Type 0 複合字體中，頂層字體維護一個 `FDepVector`（子字體依賴向量）數組，並通過 `FMapType` 整數代碼指示解釋器如何對多字節文本流進行分詞與尋址：

| FMapType 代碼 | 映射模式名稱 | 輸入字節流分詞機制 | 子字體索引與內部字符映射算法 |
| :--- | :--- | :--- | :--- |
| **`2`** | 8/8 映射（兩字節對稱） | 嚴格按 2 字節（雙字節）切分 | 高字節作爲 `FDepVector` 索引選擇子字體，低字節在該子字體中提取字符 |
| **`3`** | 8/16 映射（單雙字節混合） | 首字節若爲 `EscChar` 則消耗兩字節 | 用於西文 ASCII 與日文半角/全角混合排版，動態切換單字節與雙字節子字庫 |
| **`4`** | 16/16 映射（四字節大字符集）| 嚴格按 4 字節切分 | 前雙字節選擇子字體，後雙字節在子字體內部尋址（用於超早期 CNS 繁體大字庫） |
| **`8`** | Shift-JIS 專用硬件映射 | 依據 Shift-JIS 編碼範圍智能分詞 | 首字節若落在 `0x81..0x9F` 或 `0xE0..0xFC`，自動判定爲雙字節並執行高低字節解包 |
| **`9`** | Big5 繁體中文專用映射 | 依據 Big5 高字節範圍智能分詞 | 首字節若落在 `0xA1..0xFE`，自動抓取次字節並映射至對應的繁體字形子字庫 |

儘管 Type 0 架構在 1990 年代初有效支撐了東亞桌面出版的起步，但其複雜的樹狀解析與割裂的子字庫度量，最終促使 Adobe 在 1993 年推出了架構更加扁平、純粹且強大的 CID-keyed 字體體系。

---

# 附錄 D：TrueType、OpenType 與 AAT 字體底層文件格式全景指南

1989 年，蘋果公司爲了打破 Adobe 在 PostScript 字體解釋器授權費用上的壟斷，啓動了代號爲“皇家（Royal）”的祕密項目，由 Sampo Kaasila 等人主導研發了 **TrueType 字體格式**。隨後，微軟與蘋果達成歷史性的跨平臺技術交換協議：微軟向蘋果提供 TrueImage 頁面渲染技術，蘋果向微軟全面開放 TrueType 規範。1996 年，微軟與 Adobe 宣佈握手言和，共同將 TrueType 容器擴展爲兼容 PostScript CFF 輪廓與複雜書寫系統高級排版特性的 **OpenType**；而蘋果則在 TrueType GX 基礎上演進出了 **Apple Advanced Typography（AAT）**。

無論是 `.ttf`、`.otf` 還是蘋果的 `.dfont` 與 `.ttc`，它們在物理底層均統一歸屬於 **SFNT（Spline Font / Scaled Font）容器體系**。本附錄將對 SFNT 容器總線、TTX XML 表達範式、TrueType 核心表、OpenType 佈局表（GSUB/GPOS/GDEF/BASE/JSTF）以及 AAT 有限狀態自動機擴展表進行徹底的工業級全景解構。

---

## D.1 SFNT 容器總線拓撲與目錄尋址機制

一個 SFNT 字體文件本質上是一個**基於 4 字節 ASCII 標籤索引的小型只讀文件系統**：

```c
struct TableDirectory {
    uint32 sfntVersion;     /* 格式识别魔数：0x00010000 代表 TrueType 轮廓，0x4F54544F ('OTTO') 代表 CFF OpenType */
    uint16 numTables;       /* 文件中包含的二进制子表总数 */
    uint16 searchRange;     /* 小于等于 numTables 的最大 2 的幂乘以 16：(2^floor(log2(numTables))) * 16 */
    uint16 entrySelector;   /* 二分查找最大幂次迭代步数：floor(log2(numTables)) */
    uint16 rangeShift;      /* numTables * 16 - searchRange */
    /* 紧随其后为 numTables 个子表目录项，严格按 tag 字典序升序排列： */
    struct TableRecord {
        uint32 tag;         /* 4 字节 ASCII 表名标签（如 'head', 'glyf', 'GSUB'） */
        uint32 checkSum;    /* 该子表的 32 位校验和 */
        uint32 offset;      /* 该子表在文件中的起始字节偏移量 */
        uint32 length;      /* 该子表的实际字节长度 */
    } tables[numTables];
};
```

### 1. 32 位校驗和計算法則：
排版引擎遍歷子表內部的所有 32 位大端整數進行累加（忽略溢出，模 $2^{32}$）：

$$\text{TableCheckSum} = \sum_{i=0}^{\lfloor (\text{length}+3)/4 \rfloor - 1} \text{Word32}_i$$

若子表字節長度不是 4 的倍數，在計算校驗和時末尾補零對齊。在全字體中，`head` 表的 `checkSumAdjustment` 字段具有特殊的校驗和平衡使命：計算全文件的 32 位總累加和，用神聖常數 `0xB1B0AFBA` 減去該值並存入 `head` 表，使得全字體所有 32 位字相加的最終結果恆等於 `0xB1B0AFBA`！

::: tip SFNT 容器總線目錄與子表偏移尋址拓撲（Figure D-1, D-2）
![SFNT 目錄拓撲（Figure D-1）](/images/fonts-encodings/fig-app-d1.png)
*SFNT 目錄拓撲（Figure D-1）*
:::

*圖 D-1：SFNT 頂層目錄與各個子表之間的物理指針拓撲。所有子表目錄項按 tag 字母順序排列，支持二分查找。*

::: tip SFNT 子表校驗和與內存頁對齊（Figure D-2）
![SFNT 校驗和對齊（Figure D-2）](/images/fonts-encodings/fig-app-d2.png)
*SFNT 校驗和對齊（Figure D-2）*
:::

*圖 D-2：子表在文件中的 4 字節邊界對齊，便於現代操作系統內核直接發起零拷貝內存映射（Zero-copy mmap）。*

#### Python 工業級 SFNT 目錄解析器實現：
```python
import struct

def parse_sfnt_directory(font_data: bytes):
    sfnt_version, num_tables, search_range, entry_selector, range_shift = struct.unpack(">I4H", font_data[:12])
    print(f"SFNT Version: 0x{sfnt_version:08X}, Tables Count: {num_tables}")
    
    tables = {}
    offset = 12
    for _ in range(num_tables):
        tag_bytes, checksum, table_offset, length = struct.unpack(">4s3I", font_data[offset:offset+16])
        tag = tag_bytes.decode('ascii', errors='replace')
        tables[tag] = {
            'checksum': checksum,
            'offset': table_offset,
            'length': length,
            'data': font_data[table_offset:table_offset+length]
        }
        offset += 16
    return tables
```

---

## D.2 TTX：基於 XML 的 TrueType/OpenType 鏡像表達體系

與純文本的 PostScript 字體不同，TrueType 是一門徹底二進制化的字型容器格式。由於內部充斥着密集的 16 位和 32 位相對指針與字節對齊偏移，傳統人類開發者若不借助專用的十六進制編輯器，根本無法對其進行閱讀、審查或版本控制。

2001 年，荷蘭字體設計師尤斯特·範羅蘇姆（Just van Rossum，Python 語言創始人吉多·範羅蘇姆之弟）推出了革命性的開源工具 **TTX（TrueType XML）**。TTX 能夠將任意 SFNT 二進制字庫無損解構爲一份語義高度明晰的 XML 文檔；更重要的是，它能夠執行嚴格對稱的逆向編譯，將 XML 重新組裝爲完全一致的二進制字體文件！

在 TTX 的哲學中：
* 整個字體表現爲一個 `<ttFont>` 根節點；
* 每一個 SFNT 數據表映射爲一個直接子元素（如 `<head>`, `<maxp>`, `<glyf>`, `<GSUB>`）；
* 表內部的字段、標誌位與字形座標映射爲 XML 屬性或嵌套子元素；
* 所有字形由人機可讀的具名符號（Glyph Names，如 `glyph00042`, `A`, `acute`, `uni4E2D`）進行邏輯引用，徹底消除了底層手工維護 GID 指針的痛苦。

---

## D.3 TrueType Collections（TTC）多重字體集合容器

在處理東亞超大型中日韓字庫時，同一款字體的不同變體（例如宋體、仿宋、細黑、粗黑，或豎排比例變體）往往需要複用數萬個完全相同的漢字字形輪廓。如果爲每種樣式打包一個獨立的 `.ttf` 文件，將造成鉅額的磁盤與內存浪費。

爲此，微軟與蘋果聯合制定了 **TrueType Collection（TTC，通常文件擴展名爲 `.ttc`）** 格式：
* **`ttcf` 集合頭**：以魔數 `0x74746366`（'ttcf'）開頭；
* **Header 版本**：1.0 版或 2.0 版（2.0 增加了數字簽名 DSIG 支持）；
* **`numFonts`**：集合內部封裝的邏輯字體總數；
* **`offsetTable[numFonts]`**：指向各個邏輯字體自身 `TableDirectory` 的起始字節偏移數組。

```
+-------------------------------------------------------+
|  TTC 物理文件拓扑 (TrueType Collection Topology)        |
+-------------------------------------------------------+
|  'ttcf' Header (Magic, Version, numFonts, Offsets)    |
|  ├── Font 0 Table Directory ───────────┐              |
|  └── Font 1 Table Directory ─────┐     │              |
|                                  │     │              |
|  [共享物理数据表]                  │     │              |
|  ├── 'glyf' Table (完全共享!) <────┴─────┘              |
|  ├── 'loca' Table (完全共享!) <────┴─────┘              |
|  [独立物理数据表]                                      |
|  ├── Font 0 'name' Table (名称: "MingLiU")            |
|  ├── Font 1 'name' Table (名称: "PMingLiU")           |
|  ├── Font 0 'cmap' Table (等宽映射)                    |
|  └── Font 1 'cmap' Table (比例变宽映射)                |
+-------------------------------------------------------+
```

通過允許多個子字體共享龐大的 `glyf`、`loca` 與 `CFF` 輪廓表，僅在 `name`、`OS/2` 與 `cmap` 表上保留獨立差異，TTC 技術使得數萬字的 Windows 漢字字庫體積驟降了 60% 以上！

---

## D.4 TrueType、OpenType 與 AAT 數據表全景拓撲速查

在 SFNT 體系中，數據表的分類與歸屬極其嚴謹：

| 表分類 | 4 字節標籤 (Tag) | 作用與排版使命 | 必選/可選 | 所屬體系 |
| :--- | :--- | :--- | :--- | :--- |
| **必需核心表** | `cmap` | 字符編碼碼點到字形編號 GID 映射表 | 必需 | TrueType / OpenType |
| | `head` | 字體全局頭表（設計分辨率、BBox、校驗平衡） | 必需 | TrueType / OpenType |
| | `hhea` | 水平度量頭表（排版升部、降部、行間距） | 必需 | TrueType / OpenType |
| | `hmtx` | 水平度量字寬與左側軸承表 | 必需 | TrueType / OpenType |
| | `maxp` | 最大資源配置表（內存堆棧、點數上限宣告） | 必需 | TrueType / OpenType |
| | `name` | 多語言版權、家族名、子樣式命名錶 | 必需 | TrueType / OpenType |
| | `OS/2` | 跨平臺操作系統兼容度量表（Win/Typo 度量） | 必需 | Windows / OpenType |
| | `post` | PostScript 打印機驅動與字形名稱表 | 必需 | TrueType / OpenType |
| **輪廓幾何表** | `glyf` | TrueType 二次貝塞爾輪廓與微指令表 | TT 必需 | TrueType |
| | `loca` | 字形在 `glyf` 表中的起始偏移索引表 | TT 必需 | TrueType |
| | `CFF ` | PostScript Type 2 / CFF 三次貝塞爾輪廓表 | OTF 必需 | OpenType (CFF) |
| **微指令支持表** | `cvt ` | 控制值表（Control Value Table，像素標準間距） | 可選 | TrueType Hinting |
| | `fpgm` | 字體級程序（全局宏函數定義表） | 可選 | TrueType Hinting |
| | `prep` | 渲染預處理程序（隨分辨率執行一次） | 可選 | TrueType Hinting |
| | `gasp` | 網格自適應與 ClearType 平滑模式選擇表 | 可選 | TrueType |
| **OpenType 佈局表** | `GSUB` | 字形替換表（合字、上下文變體、垂直替換） | 複雜腳本必需 | OpenType Layout |
| | `GPOS` | 字形幾何定位表（字距微調、元音標音吸附） | 複雜腳本必需 | OpenType Layout |
| | `GDEF` | 字形分類與附着錨點定義表 | 可選 | OpenType Layout |
| | `BASE` | 多文字基準線對齊表（拉丁/漢字/印度中軸） | 可選 | OpenType Layout |
| | `JSTF` | 複雜草書（阿拉伯文）對齊延伸微調錶 | 可選 | OpenType Layout |
| **AAT 擴展表** | `morx` | 擴展字形變態表（有限狀態機驅動變形） | AAT 核心 | Apple AAT |
| | `kerx` | 擴展字距微調錶（狀態機級上下文微調） | AAT 必需 | Apple AAT |
| | `feat` | 排版特性與選擇器多語言描述表 | AAT 必需 | Apple AAT |
| | `trak` | 字號跟蹤拉伸度量表 | 可選 | Apple AAT |
| | `opbd` | 視覺邊緣對齊表（掛起標點） | 可選 | Apple AAT |
| | `bsln` | 蘋果原生基準線對齊表 | 可選 | Apple AAT |
| | `lcar` | 合字光標分割線表 | 可選 | Apple AAT |

---

## D.5 TrueType 核心內核表深度解構

### 1. `head`（字體全局頭表）
`head` 是操作系統在裝載字庫時首個讀取的元數據表。其固定長度爲 54 字節：

```xml
<!-- TTX XML 表达范例 -->
<head>
  <tableVersion value="1.0"/>
  <fontRevision value="1.002"/>
  <checkSumAdjustment value="0x12345678"/>
  <magicNumber value="0x5f0f3cf5"/>
  <flags value="00000000 00001011"/>
  <unitsPerEm value="2048"/>
  <created value="Sun Dec 12 10:00:00 2004"/>
  <modified value="Mon Jan 15 14:30:00 2007"/>
  <xMin value="-350"/>
  <yMin value="-480"/>
  <xMax value="2120"/>
  <yMax value="1950"/>
  <macStyle value="00000000 00000000"/>
  <lowestRecPPEM value="9"/>
  <fontDirectionHint value="2"/>
  <indexToLocFormat value="1"/>
  <glyphDataFormat value="0"/>
</head>
```

#### 關鍵字段物理語義：
* **`magicNumber`**：恆等於十六進制 `0x5F0F3CF5`。如果該字段不匹配，操作系統字體裝載器將立即判定文件損壞並拒絕加載；
* **`unitsPerEm`**：字體設計網格分辨率。TrueType 規範強烈建議將其設置爲 2 的冪次方（如 1024, 2048, 4096），以便光柵化底層在做定點數除法時能夠直接退化爲極速的硬件位移運算（Bit Shift）；
* **`indexToLocFormat`**：**決定 `loca` 表指針寬度的核心開關**！
  * 爲 0（Short format）：`loca` 表條目爲 16 位無符號整數（`uint16`），實際在 `glyf` 表中的字節偏移量等於存儲值乘以 2（最多尋址 128KB）；
  * 爲 1（Long format）：`loca` 表條目爲 32 位無符號整數（`uint32`），直接存儲字節偏移量（支持高達 4GB 的超大型字庫）。

---

### 2. `hhea` 與 `hmtx`（水平排印度量體系）
水平度量由頭表 `hhea`（36 字節）與連續數組表 `hmtx` 協同完成：

```xml
<hhea>
  <tableVersion value="0x00010000"/>
  <ascent value="1900"/>
  <descent value="-500"/>
  <lineGap value="200"/>
  <advanceWidthMax value="2400"/>
  <minLeftSideBearing value="-120"/>
  <minRightSideBearing value="-80"/>
  <xMaxExtent value="2350"/>
  <caretSlopeRise value="1"/>
  <caretSlopeRun value="0"/>
  <caretOffset value="0"/>
  <reserved0 value="0"/>
  <reserved1 value="0"/>
  <reserved2 value="0"/>
  <reserved3 value="0"/>
  <metricDataFormat value="0"/>
  <numberOfHMetrics value="256"/>
</hhea>
```

#### `hmtx` 表的高效壓縮策略：
在包含等寬後綴字符（如全角標點、表格數字、漢字）的字體中，大量字符擁有完全相同的水平前進字寬（`advanceWidth`）。TrueType 引入了 `numberOfHMetrics` 分割線機制：
* 前 `numberOfHMetrics` 個字符，每個條目分配 4 字節：`uint16 advanceWidth` + `int16 lsb`；
* 後續從 `numberOfHMetrics` 到 `numGlyphs - 1` 的所有字符，其前進字寬被強制認定爲**與第 `numberOfHMetrics - 1` 號字符完全相同**！每個條目僅需存儲 2 字節的 `int16 lsb`，數據體積瞬間減半！

---

### 3. `maxp`（最大資源配置表）
`maxp` 表向光柵化解釋器預先宣告字庫內部所需的計算內存上限：
* **Version 0.5（CFF OpenType 使用）**：僅包含 `uint32 version` 與 `uint16 numGlyphs`（6 字節）；
* **Version 1.0（TrueType 使用）**：包含整整 14 項極其苛刻的微指令硬件資源上限：
  * `maxPoints`：單個簡單字形所包含的最大控制點總數（含輪廓點與幻影點）；
  * `maxContours`：單個簡單字形的最大封閉輪廓線條數；
  * `maxCompositePoints` / `maxCompositeContours`：複合字形嵌套展開後的極限點數與輪廓數；
  * `maxZones`：虛擬機尋址區域總數（通常爲 2：Zone 0 黃昏區與 Zone 1 字形區）；
  * `maxTwilightPoints`：黃昏區分配的最大臨時幾何錨點數；
  * `maxStorage`：Storage 暫存區寄存器最大可用槽位數；
  * `maxFunctionDefs`：在 `fpgm` 中通過 `FDEF` 聲明的最大全局函數總數；
  * `maxInstructionDefs`：通過 `IDEF` 重載或定義的最大用戶指令總數；
  * `maxStackElements`：操作數棧（Operand Stack）的最大深度深度（防止棧溢出）；
  * `maxSizeOfInstructions`：任一單字形所允許包含的最大字節碼總長度；
  * `maxComponentElements`：複合字形第一層直接引用的最大構件個數；
  * `maxComponentDepth`：複合字形遞歸嵌套的最大樹深度（防止循環引用死鎖）。

---

### 4. `OS/2`（操作系統跨平臺度量表）
由微軟與 IBM 聯合制定的重量級系統集成表：

```xml
<OS_2>
  <version value="4"/>
  <xAvgCharWidth value="1050"/>
  <usWeightClass value="400"/>
  <usWidthClass value="5"/>
  <fsType value="00000000 00000000"/>
  <ySubscriptXSize value="1331"/>
  <ySubscriptYSize value="1228"/>
  <ySubscriptXOffset value="0"/>
  <ySubscriptYOffset value="286"/>
  <ySuperscriptXSize value="1331"/>
  <ySuperscriptYSize value="1228"/>
  <ySuperscriptXOffset value="0"/>
  <ySuperscriptYOffset value="983"/>
  <yStrikeoutSize value="102"/>
  <yStrikeoutPosition value="530"/>
  <sFamilyClass value="257"/>
  <panose>
    <bFamilyType value="2"/>
    <bSerifStyle value="11"/>
    <bWeight value="5"/>
    <bProportion value="3"/>
    <bContrast value="4"/>
    <bStrokeVariation value="3"/>
    <bArmStyle value="2"/>
    <bLetterForm value="2"/>
    <bMidline value="4"/>
    <bXHeight value="4"/>
  </panose>
  <ulUnicodeRange1 value="10000000 00000000 00000000 00000001"/>
  <ulUnicodeRange2 value="00010000 00000000 00000000 00000000"/>
  <ulUnicodeRange3 value="00000000 00000000 00000000 00000000"/>
  <ulUnicodeRange4 value="00000000 00000000 00000000 00000000"/>
  <achVendID value="MSFT"/>
  <fsSelection value="00000000 01000000"/>
  <usFirstCharIndex value="32"/>
  <usLastCharIndex value="65535"/>
  <sTypoAscender value="1490"/>
  <sTypoDescender value="-431"/>
  <sTypoLineGap value="307"/>
  <usWinAscent value="1900"/>
  <usWinDescent value="500"/>
  <ulCodePageRange1 value="00000000 00000000 00000000 00000001"/>
  <ulCodePageRange2 value="00000000 00000000 00000000 00000000"/>
  <sxHeight value="1082"/>
  <sCapHeight value="1456"/>
  <usDefaultChar value="0"/>
  <usBreakChar value="32"/>
  <usMaxContext value="3"/>
</OS_2>
```

#### Windows 與專業排版度量線的衝突與融合：
在現代排印史上，`OS/2` 表中最著名的設計衝突發生在 **Windows GDI 裁剪線** 與 **Typographic 排版行距** 之間：
* **`usWinAscent` 與 `usWinDescent`**：Windows GDI 引擎強制將文本渲染區域嚴格裁剪在這兩條線之間。若字形輪廓（如帶重音的大寫字母 `Å`, `Ŵ` 或藝術襯線花體）在垂直方向稍微探出 `usWinAscent`，Windows 會在屏幕上將其**直接以像素硬截斷**（產生醜陋的削頂現象）！因此字體工程師通常將這兩條線拉得極開，以包含全字體極限包圍盒；
* **`sTypoAscender`, `sTypoDescender` 與 `sTypoLineGap`**：專業排版軟件（如 Adobe InDesign、QuarkXPress 與 LaTeX）遵循正統排版法則，兩行連續基線之間的物理行間距嚴格計算爲：
  $$\text{LineSpace} = \text{sTypoAscender} - \text{sTypoDescender} + \text{sTypoLineGap}$$
  若設置不當，會導致 Windows 下與 Mac 下同一文檔渲染出完全不同的斷行與分頁位置！OpenType 規範後續引入了 `fsSelection` 的 Bit 7（`USE_TYPO_METRICS`），指示現代操作系統強制採用 Typo 系列數值作爲系統默認行高，徹底平息了長達數十年的跨平臺行距災難。

---

### 5. `cmap`（字符碼點到字形 GID 映射表）
操作系統在拿到文本字符串後，首先訪問 `cmap` 表檢索每個字符對應的字形編號（GID）：

::: tip cmap Format 4 分段連續二分查找算法拓撲（Figure D-3, D-4）
![cmap Format 4 拓撲（Figure D-3）](/images/fonts-encodings/fig-app-d3.png)
*cmap Format 4 拓撲（Figure D-3）*
:::

*圖 D-3：cmap Format 4 的分段壓縮結構。將 16 位 Unicode 碼點劃分爲多個不相交的連續區間 `[startCode, endCode]`。*

::: tip cmap Format 12 32 位全量擴展表（Figure D-4）
![cmap Format 12 拓撲（Figure D-4）](/images/fonts-encodings/fig-app-d4.png)
*cmap Format 12 拓撲（Figure D-4）*
:::

*圖 D-4：針對超大字符集（Emoji、古籍漢字、甲骨文）的 32 位 UCS-4 映射表 Format 12。*

#### Format 4 的二分檢索與指針偏移尋址僞代碼：
```c
uint16 lookup_gid_format4(uint16 char_code, CmapFormat4* cmap) {
    uint16 segCount = cmap->segCountX2 / 2;
    int left = 0, right = segCount - 1, hit = -1;
    
    /* 二分查找命中的连续段 */
    while (left <= right) {
        int mid = (left + right) / 2;
        if (cmap->endCode[mid] >= char_code) {
            hit = mid;
            right = mid - 1; /* 继续向前探寻最小可能段 */
        } else {
            left = mid + 1;
        }
    }
    
    if (hit == -1 || cmap->startCode[hit] > char_code) {
        return 0; /* 字符不在任何合法段内，返回缺失字形 GID 0 (.notdef) */
    }
    
    /* 核心寻址逻辑 */
    if (cmap->idRangeOffset[hit] == 0) {
        return (char_code + cmap->idDelta[hit]) & 0xFFFF;
    } else {
        /* 基于指针偏移计算在 glyphIdArray 中的位置 */
        uint16* offset_addr = &cmap->idRangeOffset[hit];
        uint16* target_ptr = offset_addr + (cmap->idRangeOffset[hit] / 2) + (char_code - cmap->startCode[hit]);
        uint16 gid = *target_ptr;
        if (gid != 0) {
            gid = (gid + cmap->idDelta[hit]) & 0xFFFF;
        }
        return gid;
    }
}
```

---

### 6. `loca` 與 `glyf`（輪廓幾何與微指令）
`loca` 表是一個純粹的偏移量數組：`offset[numGlyphs + 1]`。若某個字符（如空格字符）的起始偏移等於下一個字符的起始偏移（`offset[i] == offset[i+1]`），說明該字符爲**無輪廓字形**，僅具備前進寬度而不佔用任何繪圖幾何內存。

::: tip TrueType 輪廓點陣與二次貝塞爾曲線 On/Off 節點（Figure D-5, D-6）
![TrueType 曲線解構（Figure D-5）](/images/fonts-encodings/fig-app-d5.png)
*TrueType 曲線解構（Figure D-5）*
:::

*圖 D-5：TrueType 二次貝塞爾曲線的節點拓撲。實心點爲在線控制點（On-curve），空心點爲脫線控制點（Off-curve）。連續兩個脫線控制點之間，引擎自動在其中點虛構一個隱藏的在線點！*

::: tip glyf 表標誌位流（Flags）與差分座標解包（Figure D-6）
![glyf 標誌位流（Figure D-6）](/images/fonts-encodings/fig-app-d6.png)
*glyf 標誌位流（Figure D-6）*
:::

*圖 D-6：TrueType 座標流的無損差分壓縮：每一個控制點存儲的不是絕對座標，而是相對於前一個點的增量 $\Delta x, \Delta y$。*

::: tip 複合字形矩陣變換與錨點吸附（Figure D-7, D-8）
![複合字形變換矩陣（Figure D-7）](/images/fonts-encodings/fig-app-d7.png)
*複合字形變換矩陣（Figure D-7）*
:::

*圖 D-7：複合字形通過 $2 \times 2$ 仿射變換矩陣對引用的子字形進行旋轉、縮放與傾斜。*

::: tip 複合字形嵌套與深層組件樹（Figure D-8）
![複合字形嵌套樹（Figure D-8）](/images/fonts-encodings/fig-app-d8.png)
*複合字形嵌套樹（Figure D-8）*
:::

*圖 D-8：字形部件允許深層遞歸嵌套（最多由 `maxComponentDepth` 限制），極大地節約了中日韓多字重字庫的存儲體積。*

---

### 7. `name` 表（全文字多語言命名與版權信息表）
`name` 表是字庫的人事檔案庫。爲了確保同一款字體能夠在英語 Windows、繁體中文 Mac OS、日文 X11 等異構操作系統的字體選擇菜單中正確顯示出本地化名稱，`name` 表定義了精密的多語言命名記錄結構：

```xml
<!-- TTX XML 表达范例 -->
<name>
  <namerecord nameID="0" platformID="3" platEncID="1" langID="0x409">
    Copyright © 2007 Adobe Systems Incorporated. All Rights Reserved.
  </namerecord>
  <namerecord nameID="1" platformID="3" platEncID="1" langID="0x409">
    Adobe Garamond Pro
  </namerecord>
  <namerecord nameID="2" platformID="3" platEncID="1" langID="0x409">
    Regular
  </namerecord>
  <namerecord nameID="3" platformID="3" platEncID="1" langID="0x409">
    2.000;ADBE;AGaramondPro-Regular;ADOBE
  </namerecord>
  <namerecord nameID="4" platformID="3" platEncID="1" langID="0x409">
    Adobe Garamond Pro Regular
  </namerecord>
  <namerecord nameID="6" platformID="3" platEncID="1" langID="0x409">
    AGaramondPro-Regular
  </namerecord>
</name>
```

#### 關鍵標準 NameID 權威詞典：
* **NameID 0**：版權所有聲明（Copyright Notice）；
* **NameID 1**：字體家族名（Font Family Name，如 "Adobe Garamond Pro"）；
* **NameID 2**：字體子樣式名稱（Font Subfamily Name，如 "Regular", "Bold", "Italic"）；
* **NameID 3**：全字庫唯一標識字符串（Unique Font Identifier）；
* **NameID 4**：人機友好的全名字串（Full Font Name，通常爲 Family + Subfamily）；
* **NameID 5**：版本號字符串（Version string，如 "Version 2.000;PS 002.000"）；
* **NameID 6**：PostScript 打印機驅動識別名（PostScript Name，**嚴禁包含空格與非 ASCII 字符**，激光打印機通過該名稱在顯存中精準掛接字庫！）；
* **NameID 7**：註冊商標聲明（Trademark Notice）；
* **NameID 8**：字體製造商（Manufacturer Name）；
* **NameID 9**：字體設計師（Designer）；
* **NameID 11**：廠商官方網址 URL；
* **NameID 16**：排版首選家族名（Typographic Family Name，解決傳統辦公軟件 4 字重限制的拓展家族名）；
* **NameID 17**：排版首選子樣式名（Typographic Subfamily Name，支持 Thin, Light, Semibold, ExtraBold 等豐富層級）；
* **NameID 25**：OpenType 可變字體（Variable Fonts）的 PostScript 命名變化前綴。

---

### 8. `post` 表（PostScript 驅動與字形名稱表）
`post` 表最初由蘋果設計，用於向 PostScript 打印機轉儲必要的度量與字形名稱：
* **Format 1.0**：恆定包含蘋果 Macintosh 操作系統早期標準的 258 個拉丁字形名稱（無需在字體中存儲任何字符名稱字符串，節約內存）；
* **Format 2.0**：最經典的 TrueType 字形命名格式！包含一個 16 位字符編號映射數組與一個連續 Pascal 字符串數組（每個字符串前帶 1 字節長度），支持爲數萬個非標準字形賦予自定義的 ASCII 符號名稱；
* **Format 3.0**：**零名稱極簡格式**！完全不存儲任何字形名稱字符串。當字體發佈用於網頁嵌入（Web Fonts / WOFF）或移動端系統固件時，通常採用 Format 3.0 以剝離所有無關字符串，削減數十千字節的文件開銷。

```c
struct PostTableFormat2 {
    uint32 format;              /* 0x00020000 */
    int32  italicAngle;         /* 16.16 定点数倾斜角 */
    int16  underlinePosition;   /* 下划线基准线垂直偏移 */
    int16  underlineThickness;  /* 下划线宽度 */
    uint32 isFixedPitch;        /* 是否等宽 */
    uint32 minMemType42;        /* 激光照排机下载 Type 42 所需的最小内存 */
    uint32 maxMemType42;
    uint32 minMemType1;
    uint32 maxMemType1;
    uint16 numGlyphs;           /* 包含的字形总数 */
    uint16 glyphNameIndex[numGlyphs]; /* 指向标准 258 符号或后续自定义字符串的索引数组 */
    /* 紧随其后为 Pascal-string 连续数组: uint8 length + char data[length] */
};
```

---

### 9. `gasp` 表（網格自適應與抗鋸齒平滑控制表）
`gasp`（Grid-fitting and Scan-conversion Procedure Table）是 Windows 操作系統在執行屏幕抗鋸齒與 ClearType 亞像素渲染時極其關鍵的決策調度表。

它針對不同的屏幕顯示每 Em 像素尺寸（PPEM），精細控制何時啓用 TrueType 指令（Grid-fitting）、何時啓用灰度平滑（Grayscale Smoothing）、以及何時啓用 ClearType 對稱平滑：

```xml
<gasp>
  <version value="1"/>
  <gaspRange rangeMaxPPEM="8" rangeGaspBehavior="2"/> <!-- 仅执行灰度平滑，关闭提示 -->
  <gaspRange rangeMaxPPEM="16" rangeGaspBehavior="1"/> <!-- 极小字号：强行开启网格提示对齐 -->
  <gaspRange rangeMaxPPEM="2048" rangeGaspBehavior="15"/> <!-- 正常与大字号：同时开启微指令、灰度与 ClearType 平滑 -->
  <gaspRange rangeMaxPPEM="65535" rangeGaspBehavior="14"/> <!-- 超大海报：关闭微指令，仅执行全平滑 -->
</gasp>
```

#### `rangeGaspBehavior` 四大標誌位位域：
* **Bit 0 (`GASP_GRIDFIT`)**：在此分辨率下激活 TrueType 虛擬機執行輪廓對齊；
* **Bit 1 (`GASP_DOGRAY`)**：在此分辨率下啓用標準單色灰度抗鋸齒；
* **Bit 2 (`GASP_SYMMETRIC_SMOOTHING`)**：針對 ClearType 激活水平亞像素平滑；
* **Bit 3 (`GASP_SYMMETRIC_GRIDFIT`)**：激活 ClearType 對稱網格對齊。

---

### 10. `vhea`、`vmtx` 與 `VORG`（垂直排版核心度量體系）
在中文、日文、韓文與傳統蒙古文等東亞豎排排版中，字形並非沿着水平基線從左向右推進，而是**沿着垂直中軸線從上向下流動**！

OpenType 爲此定義了完整的垂直度量表簇：
* **`vhea`（Vertical Header Table）**：
  * `vertTypoAscender` / `vertTypoDescender`：垂直排版升部與降部；
  * `vertTypoLineGap`：垂直行距；
  * `advanceHeightMax`：全字庫最大垂直前進高度；
  * `minTopSideBearing` / `minBottomSideBearing`：全局最小頂部與底部軸承；
  * `numOfLongVerMetrics`：在 `vmtx` 中擁有獨立垂直度量的字符數。
* **`vmtx`（Vertical Metrics Table）**：
  * 與 `hmtx` 完全同構，存儲每個字符的 `advanceHeight`（垂直前進高，通常爲一個全角 Em 高度）與 `topSideBearing`（頂部軸承，即基字頂部距前一字符繪製基線的間隙）；
* **`VORG`（Vertical Origin Table，垂直繪製原點表）**：
  * 在 CFF OpenType 中，由於三次貝塞爾曲線座標系天然以左下角爲設計原點，在垂直排版時需要將原點平移到字符頂部的幾何中心。`VORG` 表通過一個緊湊的默認高度與特異字典，爲每個字形直接宣告其在垂直排版時的絕對中心原點 Y 座標（`vertOriginY`），使得排版引擎在進行豎排變換時無需重新解壓和計算龐大的 `glyf` 輪廓包圍盒！

---

## D.6 OpenType 佈局與形態表（GSUB, GPOS, GDEF, BASE, JSTF）

OpenType 徹底超越傳統點陣與靜態矢量的核心，在於其將排印學提升爲一門**上下文敏感的文法重寫系統**。排版引擎在加載字庫後，首先構建起全局佈局查找拓撲：

$$\text{ScriptList} \longrightarrow \text{LangSysRecord} \longrightarrow \text{FeatureList} \longrightarrow \text{LookupList} \longrightarrow \text{SubTables}$$

```xml
<!-- OpenType 顶层布局结构拓扑 (TTX 范例) -->
<GSUB>
  <Version value="0x00010000"/>
  <ScriptList>
    <ScriptRecord index="0">
      <ScriptTag value="latn"/>
      <Script>
        <DefaultLangSys>
          <ReqFeatureIndex value="65535"/>
          <FeatureIndex index="0" value="0"/> <!-- 指向 'liga' -->
          <FeatureIndex index="1" value="1"/> <!-- 指向 'smcp' -->
          <FeatureIndex index="2" value="2"/> <!-- 指向 'cpsp' -->
        </DefaultLangSys>
      </Script>
    </ScriptRecord>
  </ScriptList>
  <FeatureList>
    <FeatureRecord index="0">
      <FeatureTag value="liga"/>
      <Feature>
        <LookupListIndex value="0"/>
      </Feature>
    </FeatureRecord>
    <FeatureRecord index="1">
      <FeatureTag value="smcp"/>
      <Feature>
        <LookupListIndex value="1"/>
      </Feature>
    </FeatureRecord>
  </FeatureList>
  <LookupList>
    <Lookup index="0">
      <LookupType value="4"/> <!-- Ligature Substitution -->
      <LookupFlag value="0"/>
      <!-- 具体子表 -->
    </Lookup>
    <Lookup index="1">
      <LookupType value="1"/> <!-- Single Substitution -->
      <LookupFlag value="0"/>
    </Lookup>
  </LookupList>
</GSUB>
```

---

### 1. 基礎構件：Coverage 表與 ClassDef 表
在所有 GSUB 與 GPOS 子表中，兩個最基礎的篩選構件是 **Coverage 表** 與 **ClassDef 表**：

#### Coverage 表（覆蓋字形集合）：
用於快速裁決當前字形是否屬於本子表的受控目標，並將 GID 轉換爲緻密的從 0 開始的覆蓋索引（Coverage Index）：
* **Format 1（離散字形數組）**：
  ```c
  struct CoverageFormat1 {
      uint16 coverageFormat; /* 恒为 1 */
      uint16 glyphCount;     /* 受控字形总数 */
      uint16 glyphArray[glyphCount]; /* 严格按 GID 字典序升序排列 */
  };
  ```
* **Format 2（連續區間數組）**：
  ```c
  struct CoverageRangeRecord {
      uint16 startGlyphID;   /* 连续区间起始 GID */
      uint16 endGlyphID;     /* 连续区间结束 GID */
      uint16 startCoverageIndex; /* 该区间首个字符分配的连续覆盖索引 */
  };
  struct CoverageFormat2 {
      uint16 coverageFormat; /* 恒为 2 */
      uint16 rangeCount;     /* 区间总数 */
      struct CoverageRangeRecord rangeRecords[rangeCount];
  };
  ```

#### ClassDef 表（字形分類定義表）：
將成百上千個字形劃分爲若干個等價類（Class ID: 0 到 65535），極大地壓縮上下文匹配規則矩陣：
* **Format 1**：指定 `startGlyphID` 與連續數組 `classValueArray`；
* **Format 2**：通過 `ClassRangeRecord` 將連續區間指定爲特定的類編號。

---

### 2. `GSUB` 表內部 8 大查找子表規範與 TTX 源碼全景

#### Type 1：單字替換（Single Substitution）
* **Format 1（固定增量）**：將輸入字形的 GID 加上固定標量 `DeltaGlyphID`；
* **Format 2（一一映射查找表）**：
  ```xml
  <Lookup index="1">
    <LookupType value="1"/>
    <LookupFlag value="0"/>
    <SingleSubst index="0" Format="2">
      <Substitution in="a" out="a.sc"/>
      <Substitution in="b" out="b.sc"/>
      <Substitution in="c" out="c.sc"/>
      <Substitution in="d" out="d.sc"/>
    </SingleSubst>
  </LookupList>
  ```

#### Type 2：多字分解（Multiple Substitution）
將單個輸入字形在排版流中原地解構爲一個連續的字形序列：
```xml
<Lookup index="2">
  <LookupType value="2"/>
  <LookupFlag value="0"/>
  <MultipleSubst index="0" Format="1">
    <!-- 将连字符 'ffi' 还原分解为独立的三个字形 -->
    <Sequence glyph="f_f_i">
      <Substitute value="f"/>
      <Substitute value="f"/>
      <Substitute value="i"/>
    </Sequence>
  </MultipleSubst>
</Lookup>
```

#### Type 3：備選替換（Alternate Substitution）
爲單個字符提供一組等價的美學候選變體，供排版師在交互式菜單中按需挑選：
```xml
<Lookup index="3">
  <LookupType value="3"/>
  <LookupFlag value="0"/>
  <AlternateSubst index="0" Format="1">
    <AlternateSet glyph="ampersand">
      <Alternate glyph="ampersand.italic"/>
      <Alternate glyph="ampersand.swash1"/>
      <Alternate glyph="ampersand.swash2"/>
    </AlternateSet>
  </AlternateSubst>
</Lookup>
```

#### Type 4：合字替換（Ligature Substitution）
包含按首字母聚合的 `LigatureSet` 數組，內部包含各連字組件與生成的目標合字：
```xml
<Lookup index="0">
  <LookupType value="4"/>
  <LookupFlag value="0"/>
  <LigatureSubst index="0" Format="1">
    <LigatureSet glyph="f">
      <!-- 遇到 'f' + 'i' 触发替换为 'fi' (GID 280) -->
      <Ligature components="i" glyph="f_i"/>
      <!-- 遇到 'f' + 'l' 触发替换为 'fl' (GID 281) -->
      <Ligature components="l" glyph="f_l"/>
      <!-- 遇到 'f' + 'f' + 'i' 触发替换为 'ffi' -->
      <Ligature components="f,i" glyph="f_f_i"/>
    </LigatureSet>
  </LigatureSubst>
</Lookup>
```

#### Type 5 與 Type 6：上下文與鏈式上下文替換（Contextual & Chained Contextual）
Type 6 是 OpenType 文法重寫的頂峯。它維護 Backtrack、Input、Lookahead 三重滑動窗口：
```xml
<Lookup index="6">
  <LookupType value="6"/>
  <LookupFlag value="0"/>
  <ChainContextSubst index="0" Format="3">
    <!-- 回溯序列：前面必须有大写字母 -->
    <BacktrackCoverage index="0" Format="1">
      <Glyph value="A"/>
      <Glyph value="E"/>
    </BacktrackCoverage>
    <!-- 输入序列：当前字符小写 'e' -->
    <InputCoverage index="0" Format="1">
      <Glyph value="e"/>
    </InputCoverage>
    <!-- 前瞻序列：后面必须跟随字母 'r' -->
    <LookaheadCoverage index="0" Format="1">
      <Glyph value="r"/>
    </LookaheadCoverage>
    <!-- 动作：在当前输入位置 0 处，调用 Lookup 1 (小型大写替换) -->
    <SubstLookupRecord index="0">
      <SequenceIndex value="0"/>
      <LookupListIndex value="1"/>
    </SubstLookupRecord>
  </ChainContextSubst>
</Lookup>
```

#### Type 7 與 Type 8：
* **Type 7（Extension Substitution）**：打破 16 位 64KB 內部相對偏移限制的 32 位跳轉包裝器；
* **Type 8（Reverse Chaining Contextual Single）**：專爲烏爾都文納斯塔裏克體（Nastaliq）量身定製，排版引擎從後向前逆序求值，確保向下傾斜的級聯詞尾字符能夠正確變形。

---

### 3. `GPOS` 表內部 9 大幾何定位子表與 TTX 源碼全景

`GPOS` 不修改字形代碼，而是通過對字形施加二維矢量偏移與前進寬度修正，完成毫秒級空間裝配：

#### Type 1：單字定位調整（Single Adjustment）
```xml
<Lookup index="7">
  <LookupType value="1"/>
  <LookupFlag value="0"/>
  <SinglePos index="0" Format="1">
    <Coverage Format="1">
      <Glyph value="hyphen"/>
      <Glyph value="endash"/>
    </Coverage>
    <!-- 将连字符向上抬高 120 栅格单位以匹配大写字母中心 -->
    <Value YPlacement="120"/>
  </SinglePos>
</Lookup>
```

#### Type 2：基於類的字偶距微調（Class-based PairPos）
```xml
<Lookup index="8">
  <LookupType value="2"/>
  <LookupFlag value="8"/> <!-- 忽略结合音标 -->
  <PairPos index="0" Format="2">
    <Coverage Format="1">
      <Glyph value="T"/>
      <Glyph value="V"/>
      <Glyph value="W"/>
    </Coverage>
    <ClassDef1 Format="1">
      <ClassDefinition glyph="T" class="1"/>
      <ClassDefinition glyph="V" class="2"/>
      <ClassDefinition glyph="W" class="2"/>
    </ClassDef1>
    <ClassDef2 Format="1">
      <ClassDefinition glyph="o" class="1"/>
      <ClassDefinition glyph="c" class="1"/>
      <ClassDefinition glyph="e" class="1"/>
      <ClassDefinition glyph="a" class="2"/>
    </ClassDef2>
    <!-- 类别 1 (T) 与 类别 1 (o, c, e) 相遇时的字距调整 -->
    <Class1Record index="1">
      <Class2Record index="1">
        <Value1 XAdvance="-180"/>
      </Class2Record>
      <!-- 类别 1 (T) 与 类别 2 (a) 相遇时微调 -150 -->
      <Class2Record index="2">
        <Value1 XAdvance="-150"/>
      </Class2Record>
    </Class1Record>
  </PairPos>
</Lookup>
```

#### Type 3：草書連貫吸附（Cursive Attachment）
```xml
<Lookup index="9">
  <LookupType value="3"/>
  <LookupFlag value="1"/> <!-- 从右向左排版 -->
  <CursivePos index="0" Format="1">
    <Coverage Format="1">
      <Glyph value="ar_baa.init"/>
      <Glyph value="ar_noon.medi"/>
    </Coverage>
    <EntryExitRecord index="0">
      <EntryAnchor Format="1">
        <XCoordinate value="0"/>
        <YCoordinate value="150"/>
      </EntryAnchor>
      <ExitAnchor Format="1">
        <XCoordinate value="600"/>
        <YCoordinate value="100"/>
      </ExitAnchor>
    </EntryExitRecord>
  </CursivePos>
</Lookup>
```

#### Type 4：基字標音吸附（MarkToBase Attachment）
定義字母主幹上的固定錨點與音標符號上的對齊錨點：
```xml
<Lookup index="10">
  <LookupType value="4"/>
  <LookupFlag value="0"/>
  <MarkBasePos index="0" Format="1">
    <MarkCoverage Format="1">
      <Glyph value="acute"/>
      <Glyph value="grave"/>
    </MarkCoverage>
    <BaseCoverage Format="1">
      <Glyph value="a"/>
      <Glyph value="e"/>
      <Glyph value="o"/>
    </BaseCoverage>
    <BaseArray>
      <BaseRecord index="0">
        <!-- 字母 'a' 顶部的对齐中心锚点 -->
        <BaseAnchor index="0" Format="1">
          <XCoordinate value="260"/>
          <YCoordinate value="680"/>
        </BaseAnchor>
      </BaseRecord>
    </BaseArray>
    <MarkArray>
      <MarkRecord index="0">
        <Class value="0"/>
        <MarkAnchor Format="1">
          <XCoordinate value="0"/>
          <YCoordinate value="0"/>
        </MarkAnchor>
      </MarkRecord>
    </MarkArray>
  </MarkBasePos>
</Lookup>
```

---

### 4. `GDEF`、`BASE` 與 `JSTF` 表深度解構

* **`GDEF`（字形全局屬性定義表）**：
  * `GlyphClassDef`：將全字庫字形劃分爲四種神聖類型：
    1. **Base Glyph（單字基字）**：常規文本字符；
    2. **Ligature Glyph（合字字符）**：由多字拼接而成的連字；
    3. **Mark Glyph（結合附着符號）**：無前進寬度的變音符或聲調符號；
    4. **Component Glyph（組件字符）**：不可單獨顯示的內部拼裝部件。
  * `AttachList`：在輪廓上顯式標明可用於幾何組裝的錨點編號；
  * `LigCaretList`：定義多字符合字（如 'ffi'）內部的文本光標閃爍分界線（Caret Positions）；
* **`BASE`（跨文字基準線對齊表）**：
  * 在同一段落中混合排版西文拉丁字母、漢字方塊字、藏文與印度天城體時，各種文字的歷史基準參考線完全不同。`BASE` 表統一定義了 `romn`（羅馬基線）、`ideo`（漢字底部基線）、`idcm`（漢字正中軸線）以及 `math`（數學公式中軸），排版引擎依據各文字的基線偏差矩陣自動平移字身，實現跨語系視覺平齊；
* **`JSTF`（兩端對齊與段落調整表）**：
  * 專爲阿拉伯文等複雜書寫系統設計。當需要對段落執行兩端對齊（Justification）時，`JSTF` 定義了多級優先級的微調動作：第一級拉長筆畫橫樑（Kashida 填充）；第二級調用更寬的備選字形；第三級微調字距；第四級允許空格適度拉伸，再現了傳統手抄本時代的極致排印美感。

---

## D.7 Apple Advanced Typography（AAT）高級擴展表體系

在蘋果公司與微軟分別主導字型技術演進的時期，蘋果在 macOS（自 Mac OS X 10.0 引入）與 iOS 底層堅持並完善了源自 TrueType GX 的 **AAT（Apple Advanced Typography）** 體系。

與 OpenType 基於靜態查找表（Lookups）與多輪模式匹配（Pattern Matching）不同，**AAT 的底層核心是圖靈完備的“有限狀態自動機（Finite State Machines / State Tables）”！**

::: tip AAT morx 變態表與 kerx 擴展字距表拓撲（Figure D-9, D-10）
![AAT morx 表拓撲（Figure D-9）](/images/fonts-encodings/fig-app-d9.png)
*AAT morx 表拓撲（Figure D-9）*
:::

*圖 D-9：AAT `morx`（Extended Glyph Metamorphosis Table）內部由鏈表鏈條（Chains）構成，每個鏈條包含獨立的特性掩碼與狀態機子表。*

::: tip AAT trak 跟蹤排印與字間距動態補償（Figure D-10）
![AAT trak 跟蹤表（Figure D-10）](/images/fonts-encodings/fig-app-d10.png)
*AAT trak 跟蹤表（Figure D-10）*
:::

*圖 D-10：AAT `trak`（Tracking Table）結構。針對不同顯示磅數（Point Sizes）定義字間距自動擴展與收縮曲線。*

---

### 1. AAT 擴展狀態機（Extended State Table）的代數結構

一個標準的 AAT 狀態機子表在二進制內存中由四大連續組件構成：
1. **Header（狀態機頭）**：記錄狀態總數、類總數、以及到後續三張表的相對字節偏移量；
2. **ClassTable（字形到類別映射表）**：將輸入的 GID 映射爲一個 16 位整數類別（Class ID）；
3. **StateArray（二維狀態躍遷轉移矩陣）**：一個行數爲狀態數、列數爲類別數的稠密二維數組。給定當前狀態 $S$ 與輸入類別 $C$，查得轉移條目索引：
   $$\text{EntryIndex} = \text{StateArray}[S][C]$$
4. **EntryTable（動作條目數組）**：每一個條目佔用 4 字節，編碼了三大核心排版動作：
   * `newState`：狀態機轉移到的下一個目標狀態；
   * `flags`：執行動作標誌位（指示是否將當前字形壓入內部回溯硬件棧、是否標記當前位置、是否向前推進畫筆）；
   * `actionIndex`：指向字形替換數組或字距微調數組的操作索引。

```
+-------------------------------------------------------+
|  AAT 状态机执行流 (State Machine Execution Pipeline)   |
+-------------------------------------------------------+
|  Input Glyph GID                                      |
|       │                                               |
|       ▼                                               |
|  [ ClassTable ] ──> Class ID (C)                      |
|                           │                           |
|  Current State (S) ───────┼───> [ StateArray[S][C] ]  |
|                                         │             |
|                                         ▼             |
|                                 [ EntryTable ]        |
|                                 ├── Next State (S')   |
|                                 ├── Push/Pop Stack    |
|                                 └── Action (Subst/Kern)
+-------------------------------------------------------+
```

由於狀態機在處理連續文本時**僅需向前線性掃描一次（$O(N)$ 單趟時間複雜度）**，AAT 在處理極爲繁複的南亞印度系文字（如天城體、泰米爾體、高棉體）與阿拉伯文時，其排版性能與抗死鎖能力在歷史上長期碾壓早期未經硬件優化的 OpenType 引擎！

---

### 2. `morx` 表（擴展字形變態表）的五大子表形態

`morx`（Extended Glyph Metamorphosis）是 AAT 排版體系的心臟。它劃分爲五種專有子表類型：
1. **Type 0（Rearrangement Subtable / 字形重排狀態機）**：
   * 專爲印度系文字設計。在印地語中，某些短元音在邏輯字符編碼上書寫在輔音之後，但視覺呈現上必須被“拋擲”到輔音甚至整個輔音連綴的前方！Type 0 狀態機包含一個最多容納 4 個字符的微型硬件回溯棧，支持從棧中任意重排字符的物理繪製次序；
2. **Type 1（Contextual Glyph Substitution / 上下文替換狀態機）**：
   * 在狀態轉移的同時，根據 `actionIndex` 查表對當前標記的字形進行一對一或基於類的變體替換；
3. **Type 2（Ligature Substitution / 狀態機連字替換）**：
   * 支持任意跨度、任意複雜度的多字合字。狀態機在掃描連字組件時將它們依次推入內部棧，在遇到連字閉合字符時，一次性將棧中所有組件彈出並整體替換爲最終目標合字；
4. **Type 4（Non-contextual Substitution / 非上下文單字替換）**：
   * 無狀態機開銷，通過單一查找表執行全局單字變體替換；
5. **Type 5（Glyph Insertion / 動態字形插入狀態機）**：
   * 允許狀態機在當前文本流中憑空插入一個或多個嶄新的字形（例如插入方向控制符號、連字符或裝飾襯花），而無需上層應用程序修改原始 Unicode 文本緩衝區。

---

### 3. `kerx` 表（擴展字距微調錶）

AAT 的 `kerx` 表是對傳統 TrueType `kern` 表的革命性升級：
* **Format 0（簡單有序字偶對）**：經典 $(Left, Right) \to \text{Value}$ 二分查找數組；
* **Format 1（狀態機驅動的上下文多字符微調）**：能夠在跨越多箇中間字符的複雜語境下，同時對多達 8 個暫存字符施加高精度的相對二維座標微調！
* **Format 2（基於類的字距矩陣）**：利用稠密矩陣執行全字庫大面積字距補償；
* **Format 4（跨流字距微調 Cross-Stream Kerning）**：**在垂直於文本流動方向的軸線上施加位移**！例如在阿拉伯文草書排版中，當某個字符向下傾斜時，後續字符通過跨流字距在垂直 Y 軸上整體抬高，完美模擬出波斯體書法連綿起伏、層層疊疊的瀑布式美感！

---

### 4. `feat` 表（排版特性多語言定義表）

與 OpenType 採用 4 字節 ASCII 縮寫標籤（如 `liga`, `smcp`）且未在字體內部定義本地化名稱不同，AAT 的 `feat` 表將排版特性定義爲兩級數字代號：
* **`FeatureType`（特性類別）**：如 1 代表合字（Ligatures），3 代表備選字形（Alternate Pos），22 代表文字變體；
* **`SettingSelector`（設置選擇器）**：如對於合字特性，選擇器 0 爲關閉所有合字，2 爲啓用標準合字，4 爲啓用歷史連字；
* **多語言本地化支持**：每個特性與選擇器直接綁定一個 `nameID`，在 `name` 表中存儲英語、法語、中文、日語等原生字符串。使得 macOS 的“字體面板（Font Panel）”能夠無需任何外部配置，原生爲用戶渲染出一個全本地化、支持勾選切換的高級排版功能交互式界面！

---

### 5. `trak`、`opbd`、`bsln` 與 `lcar` 表

* **`trak`（Tracking Table / 字距跟蹤表）**：
  * 在傳統金屬活字排版中，大磅字號（如 72 磅海報標題）需要適度收緊字距，而極小字號（如 6 磅版權小字）必須大幅放寬字間距以保證辨識度。`trak` 表定義了由字體設計師繪製的字號-字距連續非線性補償樣條曲線，操作系統排版器根據當前渲染磅值動態求值並自動施加均勻的微米級字間距平移；
* **`opbd`（Optical Bounds / 視覺邊緣對齊表）**：
  * 人眼的視覺心理物理學（Psychophysics）表明：當一段文字左側包含左雙引號 `“` 或小寫字母 `o` 時，若將其物理包圍盒與下方大寫字母 `H` 機械對齊，視覺上會顯得左側凹陷不平。`opbd` 表爲每個字符定義了左、上、右、下四個方向的**光學凸出量（Optical Offsets）**，使標點符號在段落邊緣能夠極其優美地“掛起”探出邊框（Hanging Punctuation）；
* **`bsln`（Baseline Table / AAT 基線表）**：
  * 定義了多達 32 種不同文字系統的基線系統，並在同一字庫內部存儲各文字基線的相對垂直座標與主控基線（Dominant Baseline）優先權；
* **`lcar`（Ligature Caret Table / 合字光標分割線表）**：
  * 當文本光標在合字（如 'ffi'）內部移動時，`lcar` 爲其定義了兩個內部邏輯切分點（Caret Coordinates）。光標在合字中間閃爍時能夠精確停留在 'f' 與 'i' 之間的虛擬空間，徹底解決了用戶在編輯連字時無法定位內部字符的交互噩夢。

通過 SFNT 容器的彈性封裝、TrueType 虛擬機的微觀粒子控制、OpenType 佈局引擎的圖靈文法重寫、以及 AAT 狀態機的毫秒級流式處理，數字字體工程構建起了人類信息文明史上最爲精密、優雅且深邃的排印技術巨塔。
---

## D.8 複雜書寫系統（Complex Scripts）排版佈局實戰案例

爲了徹底展示 OpenType 與 AAT 處理阿拉伯文、南亞印度系文字（Indic Scripts）以及東亞縱排文字的工業級能力，以下剖析三大高級排版實戰結構：

### 1. 阿拉伯文四態上下文替換（Contextual Substitution GSUB Type 5）
在阿拉伯文字體中，每個字母具有四種截然不同的書寫形態：
* **孤立態（Isolated）**：字符前後均未連筆；
* **詞首態（Initial）**：僅與後一字符連筆；
* **詞中態（Medial）**：前後均連筆；
* **詞尾態（Final）**：僅與前一字符連筆。

OpenType 引擎首先通過 `init`、`medi`、`fina`、`isol` 四個排版特性，使用 GSUB Type 5（基於類的上下文替換）進行狀態匹配：

```xml
<Lookup index="15">
  <LookupType value="5"/> <!-- Contextual Substitution -->
  <LookupFlag value="1"/> <!-- RightToLeft -->
  <ContextSubst index="0" Format="2">
    <!-- 覆盖所有具有连笔能力的阿拉伯文字母 -->
    <Coverage Format="1">
      <Glyph value="ar_baa"/>
      <Glyph value="ar_jeem"/>
      <Glyph value="ar_seen"/>
    </Coverage>
    <ClassDef Format="1">
      <ClassDefinition glyph="ar_baa" class="1"/>
      <ClassDefinition glyph="ar_jeem" class="1"/>
      <ClassDefinition glyph="space" class="2"/>
    </ClassDef>
    <!-- 当 Class 1 (字母) 后紧随 Class 1 (字母) 时，触发替换为词首态 -->
    <SubClassSet index="1">
      <SubClassRule index="0">
        <ClassSequence>
          <Class value="1"/>
        </ClassSequence>
        <SubstLookupRecord index="0">
          <SequenceIndex value="0"/>
          <LookupListIndex value="20"/> <!-- 词首态替换子表 -->
        </SubstLookupRecord>
      </SubClassRule>
    </SubClassSet>
  </ContextSubst>
</Lookup>
```

---

### 2. 多重音標堆疊與碰撞規避（Mark-to-Mark GPOS Type 6）
在阿拉伯文《古蘭經》誦讀記號或希伯來文聖經多重變音符中，字母上方往往需要垂直堆疊兩到三個獨立的讀音與聲調符號。若機械放置，符號必然重疊。

GPOS Type 6 構築了音標之間的遞歸相對幾何錨點：
```xml
<Lookup index="16">
  <LookupType value="6"/> <!-- MarkToMark Attachment -->
  <LookupFlag value="0"/>
  <MarkMarkPos index="0" Format="1">
    <!-- 顶层音标：开音符 (Fathah) -->
    <Mark1Coverage Format="1">
      <Glyph value="ar_fathah"/>
    </Mark1Coverage>
    <!-- 底层音标：鼻音化轻读符 (Tanwin) -->
    <Mark2Coverage Format="1">
      <Glyph value="ar_tanwin"/>
    </Mark2Coverage>
    <Mark2Array>
      <Mark2Record index="0">
        <!-- 在底层音标顶端定义向上的对接锚点 -->
        <Mark2Anchor index="0" Format="1">
          <XCoordinate value="0"/>
          <YCoordinate value="220"/>
        </Mark2Anchor>
      </Mark2Record>
    </Mark2Array>
    <Mark1Array>
      <Mark1Record index="0">
        <Class value="0"/>
        <Mark1Anchor Format="1">
          <XCoordinate value="0"/>
          <YCoordinate value="0"/>
        </Mark1Anchor>
      </Mark1Record>
    </Mark1Array>
  </MarkMarkPos>
</Lookup>
```

無論下層音標的位置因基字高度發生何種位移，上層音標通過實時錨點對齊，永遠浮動在下層音標正上方 220 柵格單位處，徹底消除了文字重疊！

---

### 3. 合字光標分割線（`GDEF` Ligature Caret List）
當用戶使用光標鍵在一個連字合字（如 'ffi'）內部穿行時，文字處理軟件查詢 `GDEF` 表的 `LigCaretList`：

```xml
<GDEF>
  <Version value="0x00010002"/>
  <LigCaretList>
    <Coverage Format="1">
      <Glyph value="f_f_i"/>
    </Coverage>
    <LigGlyph index="0">
      <!-- 'f' 与第二个 'f' 之间的光标闪烁 X 坐标 -->
      <CaretValue index="0" Format="1">
        <Coordinate value="320"/>
      </CaretValue>
      <!-- 第二个 'f' 与 'i' 之间的光标闪烁 X 坐标 -->
      <CaretValue index="1" Format="1">
        <Coordinate value="650"/>
      </CaretValue>
    </LigGlyph>
  </LigCaretList>
</GDEF>
```

軟件依據這些座標，在屏幕上繪製閃爍的垂直光標，並在用戶按下退格鍵（Backspace）時，精準將合字拆解還原，提供毫無破綻的原生多字符編輯體驗。
---

## D.9 AAT 有限狀態自動機狀態躍遷矩陣實戰推導

爲了深刻理解 AAT `morx` 表內部狀態轉移的數學精髓，我們以印地語天城體（Devanagari）的短元音 'i'（Matra-I）前置重排狀態機爲例進行推導：

在天城體中，邏輯編碼順序爲：$\text{辅音 (Consonant)} + \text{短元音 (Matra-I)}$，但在視覺排版中，短元音必須被“向前翻轉”到輔音左側！

### 狀態轉移代數模型：
* **狀態集合**：$Q = \{ S_0: \text{StartOfLine}, \, S_1: \text{SawConsonant}, \, S_2: \text{SawVirama} \}$；
* **字符類別**：$\Sigma = \{ C_0: \text{Other}, \, C_1: \text{Consonant}, \, C_2: \text{Matra-I}, \, C_3: \text{Virama (死符)} \}$。

#### 躍遷矩陣與動作表（StateArray & EntryTable）：

| 當前狀態 | 輸入類別：$C_1$ (輔音) | 輸入類別：$C_2$ (短元音 Matra-I) | 輸入類別：$C_3$ (Virama 死符) | 輸入類別：$C_0$ (其餘字符) |
| :--- | :--- | :--- | :--- | :--- |
| **$S_0$ (起點)** | 轉移到 $S_1$；**動作**：將輔音壓棧 (Push) | 保持 $S_0$；無動作 | 保持 $S_0$；無動作 | 保持 $S_0$；推進畫筆 |
| **$S_1$ (已見輔音)**| 保持 $S_1$；清空舊棧並壓入新輔音 | **觸發重排**！轉移到 $S_0$；**動作**：從棧中彈出輔音，先繪製短元音，再繪製輔音！ | 轉移到 $S_2$；將死符壓棧 | 轉移到 $S_0$；彈出並清空棧 |
| **$S_2$ (已見死符)**| 轉移到 $S_1$；將第二輔音壓棧（構築半輔音連綴羣） | **觸發連綴重排**！轉移到 $S_0$；將元音拋至整個連綴左端！ | 轉移到 $S_0$；清空棧 | 轉移到 $S_0$；清空棧 |

這種單趟純線性自動機機制，使得蘋果 macOS 的 CoreText 圖形框架在處理複雜的梵文經文、藏文千字大藏經時，以極簡的查表動作完成了傳統排版軟件需要數十重正則匹配才能完成的宏偉變換。

---

## D.10 OpenType 與 AAT 排版體系深度技術對照

| 技術維度 | 微軟 / Adobe OpenType | 蘋果 Apple Advanced Typography (AAT) |
| :--- | :--- | :--- |
| **核心計算模型** | 基於多輪遍歷的聲明式模式替換查找表（Lookups & Features） | 基於有限狀態機（Finite State Machines）的單趟流式自動機 |
| **執行時間複雜度** | 最壞情況下爲多次遍歷匹配（$O(N \times K)$，依賴查找鏈長度） | 嚴格單趟線性時間掃描（$O(N)$，掃描一遍文本即完成排版） |
| **排版邏輯歸屬** | **外部驅動主導**：字體僅提供數據，排版整形引擎（HarfBuzz, Uniscribe）承擔腳本形態邏輯 | **字體內部自治**：字體自身即爲完整狀態機，上層排版引擎無需知道任何具體語言規則 |
| **跨文字基線支持** | `BASE` 表（羅馬基線、漢字底部、中軸、數學軸） | `bsln` 表（32 種腳本原生基線優先級） |
| **字距微調能力** | GPOS Type 2（靜態字偶對與分類微調矩陣） | `kerx` 表（支持跨流字距微調與狀態機級 8 字符級聯微調） |
| **多語言本地化** | 採用 4 字節全局 ASCII 標籤（如 'liga'），UI 名稱需操作系統單獨提供 | `feat` 表將特性代碼與 `name` 表多語言字串原生綁定，字體自帶本地化菜單 |
| **工業生態與標準** | **全球絕對主導標準**：Windows, Linux, Android, Web 瀏覽器默認標準 | 蘋果生態獨佔專有標準：macOS, iOS 原生支持，工業跨平臺支持較弱 |
---

## D.11 OpenType 1.8 矢量可變字體（Variable Fonts）體系演進

2016 年 9 月，蘋果、微軟、Adobe 與 Google 在波蘭華沙的 ATypI 大會上聯合發佈了歷史性的 **OpenType 1.8 規範**。該規範引入了源自蘋果 TrueType GX 與 Adobe Multiple Master 的集大成者——**OpenType 字體可變機制（OpenType Font Variations）**。

### 1. `fvar` 表（字體變化軸與命名實例表）
`fvar`（Font Variations Table）定義了字體在 $k$ 維設計空間中的連續變化軸線：

```xml
<fvar>
  <!-- 声明五大注册标准设计轴之一：字重轴 (wght) -->
  <Axis>
    <AxisTag value="wght"/>
    <Flags value="0x0000"/>
    <MinValue value="100.0"/>
    <DefaultValue value="400.0"/>
    <MaxValue value="900.0"/>
    <AxisNameID value="256"/>
  </Axis>
  <!-- 声明字宽轴 (wdth) -->
  <Axis>
    <AxisTag value="wdth"/>
    <Flags value="0x0000"/>
    <MinValue value="75.0"/>
    <DefaultValue value="100.0"/>
    <MaxValue value="125.0"/>
    <AxisNameID value="257"/>
  </Axis>

  <!-- 预定义命名的静态样式快照 (Named Instances) -->
  <NamedInstance nameID="258"> <!-- "Light Condensed" -->
    <Coordinates>
      <Coord axis="wght" value="300.0"/>
      <Coord axis="wdth" value="75.0"/>
    </Coordinates>
  </NamedInstance>
  <NamedInstance nameID="259"> <!-- "Bold" -->
    <Coordinates>
      <Coord axis="wght" value="700.0"/>
      <Coord axis="wdth" value="100.0"/>
    </Coordinates>
  </NamedInstance>
</fvar>
```

#### 五大國際註冊標準軸標籤（Standard Registered Axes）：
* **`wght`（Weight / 字重軸）**：取值範圍 $1 \dots 1000$（400 爲 Regular，700 爲 Bold）；
* **`wdth`（Width / 字寬軸）**：以基準設計寬度的百分比衡量（75% Condensed 至 125% Expanded）；
* **`slnt`（Slant / 傾斜角軸）**：文字順時針傾斜度數（正數爲傾斜度，如 $-12$）；
* **`ital`（Italic / 意大利體軸）**：二元或連續軸（0 代表正體 Roman，1 代表真正的手寫斜體 Italic）；
* **`opsz`（Optical Size / 視覺字號軸）**：指示字體當前排版使用的物理磅值（如 6pt 至 72pt），引擎據此自動調整筆畫粗細對比度與字距。

---

### 2. `gvar` 表（字形變化量數據表 Tuple Variation Store）
在可變字體中，基礎輪廓僅存儲在 `glyf` 表中（默認母版座標）。當用戶在 CSS 中指定 `font-weight: 550` 時，渲染引擎查詢 `gvar` 表：
* 每個輪廓控制點存儲的不是絕對座標，而是一組**變化量差分向量（Delta Vectors: $\Delta x, \Delta y$）**；
* 通過 **元組變化存儲器（Tuple Variation Store）** 算法，引擎將用戶輸入的浮點軸向座標映射爲歸一化標量因數；
* 最終物理輪廓點由默認座標與各軸向 Delta 的標量加權和瞬間線性計算得出：
  $$\mathbf{P}_{\text{rendered}} = \mathbf{P}_{\text{default}} + \sum_{i=1}^m \text{Scalar}_i \times \Delta \mathbf{P}_i$$

不僅輪廓點，OpenType 1.8 更引入了 `HVAR`（水平度量變化表）與 `MVAR`（全局度量變化表），動態聯動調整升部、降部與字寬，使原本需要包含數十個獨立 `.ttf` 文件（總計數十兆字節）的巨型家族，以**單一緊湊文件（通常僅增加 20% 體積）**的形式完整覆蓋了無限連續維度的排印設計空間！

---

# 附錄 E：TrueType 虛擬機微指令全景參考詞典（TrueType Instructions Reference Dictionary）

在所有現代字型格式中，TrueType 的指令系統（Hinting Instructions）是複雜度最高、表現力最強、也是最接近計算機體系結構底層的部分。與 PostScript Type 1 僅提供陳述式聲明的“提示（Hints）”不同，**TrueType 內部直接嵌入了一臺功能完整的圖靈完備虛擬機（TrueType Virtual Machine, TT-VM）！**

在這臺虛擬機中，字形輪廓上的每一個控制點（Point）不僅僅是幾何座標，更是一個可被尋址、被數學變換、被條件邏輯驅動的“物理粒子”。通過執行字節碼程序，字體設計師可以針對特定的屏幕點陣分辨率（PPEM），動態伸縮筆畫、平移波谷、強制對稱並消除走樣。本附錄將對 TrueType 虛擬機的內存模型、圖形狀態機（Graphics State）以及全部約 130 條指令的操作碼、堆棧效應與執行語義進行權威字典級解構。

---

## E.1 TrueType 虛擬機架構與程序生命週期

TrueType 虛擬機是一臺純粹的**大端序棧式計算機（Stack-based Machine）**。它不具備通用寄存器，所有算術、幾何與邏輯運算均在一個 32 位整數操作數棧上完成。

```
+-------------------------------------------------------+
|  TrueType 虚拟机硬件资源全景                           |
+-------------------------------------------------------+
|  1. 操作数栈 (Operand Stack, 通常 256-512 深度)        |
|  2. 控制值表 (Control Value Table, CVT, 16位有符号字)   |
|  3. 存储区 (Storage Area, 32位通用暂存数组)             |
|  4. 黄昏区 (Twilight Zone, Zone 0, 临时辅助几何点池)   |
|  5. 字形区 (Glyph Zone, Zone 1, 真实轮廓控制点阵列)     |
|  6. 图形状态机寄存器组 (Graphics State Registers)       |
+-------------------------------------------------------+
```

### 虛擬機的三大執行生命週期（Lifecycle）
1. **字體級程序（`fpgm` 表）**：在字庫被操作系統首次載入內存時**僅執行整整一次**。它用於編譯通用的全局函數定義（`FDEF`）與用戶自創指令（`IDEF`），建立全字通用的幾何計算子程序庫；
2. **渲染預處理程序（`prep` 表）**：在用戶調整字號（PPEM 發生變化）、屏幕分辨率或發生仿射變換時**執行一次**。它根據當前的微觀分辨率，批量計算並將物理網格尺寸寫入控制值表（CVT），並設置全局圖形狀態（如舍入規則）；
3. **字形級指令流（`glyf` 表內部）**：在光柵化引擎實際繪製每一個具體字形時**每次獨立執行**。它操縱該字形的在線點與脫線點，將其強制吸附對齊到物理像素網格。

::: tip TrueType 虛擬機執行流與圖形狀態機變換（Figure E-1, E-2）
![TT 虛擬機架構（Figure E-1）](/images/fonts-encodings/fig-app-e1.png)
*TT 虛擬機架構（Figure E-1）*
:::

*圖 E-1：TrueType 虛擬機的執行總線拓撲。操作數棧、CVT 查表、Storage 暫存區與雙幾何區域的協同交互。*

::: tip 控制值表 CVT 與像素網格切入（Figure E-2）
![CVT 網格切入（Figure E-2）](/images/fonts-encodings/fig-app-e2.png)
*CVT 網格切入（Figure E-2）*
:::

*圖 E-2：控制值表（CVT）網格切入機制（Control Value Cut-In）：當實際筆畫寬度與 CVT 理想值的偏差小於閾值時，強行吸附到 CVT 規範值；一旦偏差過大，立即解除鎖定，恢復自由網格對齊。*

---

## E.2 圖形狀態機（Graphics State）核心寄存器組

圖形狀態機由一組直接控制幾何計算行爲的專用寄存器構成：
* **自由向量（Freedom Vector, $\vec{f} = (f_x, f_y)$）**：**點被允許移動的物理方向單位向量**。當執行移動指令時，點只能沿着 $\vec{f}$ 方向平移；
* **投影向量（Projection Vector, $\vec{p} = (p_x, p_y)$）**：**距離度量方向單位向量**。所有點間距離、筆畫寬度均投影到 $\vec{p}$ 軸線上進行標量測量；
* **雙投影向量（Dual Projection Vector, $\vec{dp}$）**：在未經 Hinting 的原始輪廓設計網格上測量初始距離的向量；
* **參考點寄存器（Reference Points: $rp0, rp1, rp2$）**：作爲相對移動與內插幾何基準的錨定點索引；
* **區域指針（Zone Pointers: $zp0, zp1, zp2$）**：指示當前引用的幾何點屬於 Zone 0（黃昏區）還是 Zone 1（當前字形輪廓區）；
* **舍入狀態（Rounding State）**：控制浮點數值如何量化爲整數像素網格。包含網格舍入（`RTG`，舍入到最近像素中心）、半網格舍入（`RTHG`，舍入到 0.5 像素邊界）、雙倍網格舍入（`RTDG`）、向下取整（`RDTG`）、向上取整（`RUTG`）以及由週期（Period）、相位（Phase）與閾值（Threshold）定製的超強舍入（`SROUND`）；
* **極小距離閾值（Single Minimum Distance, `SMD`）**：在執行相對移動時，防止兩筆畫因四捨五入坍縮重疊的物理最小保護間隙；
* **控制值切入閾值（Control Value Cut-In, `SCVTCI`）**：決定何時啓用 CVT 強行吸附的差值上限；
* **循環計數器（Loop Counter）**：由 `SLOOP` 指令設置，控制後續指令自動重複執行的次數。

---

## E.3 核心微指令分類權威參考詞典

### 1. 堆棧壓入指令（PUSH Instructions）

| 操作碼（Hex/Dec） | 指令助記符 | 參數形態 | 堆棧效應（Stack Effect） | 執行邏輯與物理語義 |
| :--- | :--- | :--- | :--- | :--- |
| `0xB0..0xB7 (176..183)` | `PUSHB[abc]` | $n$ 字節無符號數 | $\emptyset \to b_1, b_2, \dots, b_k$ | 將指令後緊隨的 $k = abc + 1$（1 到 8）個單字節整數按序壓入棧頂 |
| `0xB8..0xBF (184..191)` | `PUSHW[abc]` | $n$ 雙字節有符號數 | $\emptyset \to w_1, w_2, \dots, w_k$ | 將指令後緊隨的 $k = abc + 1$（1 到 8）個 16 位大端整數按序壓入棧頂 |
| `0x40 (64)` | `NPUSHB` | 計數 $n$ + $n$ 字節 | $\emptyset \to b_1, \dots, b_n$ | 批量壓棧：第一個字節 $n$ 爲數量，隨後 $n$ 個單字節依次壓棧 |
| `0x41 (65)` | `NPUSHW` | 計數 $n$ + $n$ 雙字 | $\emptyset \to w_1, \dots, w_n$ | 批量字壓棧：第一個字節 $n$ 爲數量，隨後 $n$ 個 16 位整數依次壓棧 |

### 2. 存儲區（Storage）與控制值表（CVT）訪問指令

| 操作碼（Hex/Dec） | 助記符 | 堆棧輸入 | 堆棧輸出 | 執行語義 |
| :--- | :--- | :--- | :--- | :--- |
| `0x43 (67)` | `RS` | $index$ | $value$ | 從存儲區（Storage Area）讀取索引爲 $index$ 處的 32 位值壓棧 |
| `0x42 (66)` | `WS` | $value, index$ | $\emptyset$ | 將 32 位值 $value$ 寫入存儲區索引 $index$ 槽位 |
| `0x45 (69)` | `RCVT` | $index$ | $value$ | 讀取 CVT 表中索引爲 $index$ 的當前網格縮放值（單位：26.6 像素定點數） |
| `0x44 (68)` | `WCVTP` | $value, index$ | $\emptyset$ | 將經像素網格縮放的值 $value$ 寫入 CVT 表中的 $index$ 槽位 |
| `0x70 (112)` | `WCVTF` | $value, index$ | $\emptyset$ | 將未經縮放的設計單位值 $value$ 寫入 CVT（引擎自動執行當前 PPEM 比例縮放） |

### 3. 圖形狀態機向量與區域設置指令

| 操作碼（Hex/Dec） | 助記符 | 堆棧輸入 | 堆棧輸出 | 執行語義 |
| :--- | :--- | :--- | :--- | :--- |
| `0x00 (0)` | `SVTCA[y]` | $\emptyset$ | $\emptyset$ | 將自由向量與投影向量同時設置爲 Y 軸：$\vec{f} = \vec{p} = (0, 1)$ |
| `0x01 (1)` | `SVTCA[x]` | $\emptyset$ | $\emptyset$ | 將自由向量與投影向量同時設置爲 X 軸：$\vec{f} = \vec{p} = (1, 0)$ |
| `0x02 (2)` | `SPVTCA[y]` | $\emptyset$ | $\emptyset$ | 僅將投影向量設置爲 Y 軸 |
| `0x03 (3)` | `SPVTCA[x]` | $\emptyset$ | $\emptyset$ | 僅將投影向量設置爲 X 軸 |
| `0x04 (4)` | `SFVTCA[y]` | $\emptyset$ | $\emptyset$ | 僅將自由向量設置爲 Y 軸 |
| `0x05 (5)` | `SFVTCA[x]` | $\emptyset$ | $\emptyset$ | 僅將自由向量設置爲 X 軸 |
| `0x06..0x07` | `SPVTL[0..1]` | $p_1, p_2$ | $\emptyset$ | 將投影向量設置爲平行於點 $p_1$ 到 $p_2$ 的直線（若爲 1 則逆時針旋轉 90 度建立垂直線） |
| `0x08..0x09` | `SFVTL[0..1]` | $p_1, p_2$ | $\emptyset$ | 將自由向量設置爲平行於點 $p_1$ 到 $p_2$ 的直線（若爲 1 則旋轉 90 度） |
| `0x0A (10)` | `SPVFS` | $x, y$ | $\emptyset$ | 通過顯式輸入的向量分量設置投影向量：$\vec{p} = \frac{(x, y)}{\sqrt{x^2+y^2}}$ |
| `0x0B (11)` | `SFVFS` | $x, y$ | $\emptyset$ | 通過顯式輸入的向量分量設置自由向量 |
| `0x0E (14)` | `SFVTPV` | $\emptyset$ | $\emptyset$ | 將自由向量設置爲與當前投影向量相同：$\vec{f} = \vec{p}$ |
| `0x10..0x12` | `SRP0,1,2` | $p$ | $\emptyset$ | 設置參考點寄存器：分別將 $rp0, rp1, rp2$ 指向輪廓點編號 $p$ |
| `0x13..0x15` | `SZP0,1,2` | $zone$ | $\emptyset$ | 設置區域指針：將 $zp0, zp1, zp2$ 綁定到 Zone 0（黃昏區）或 Zone 1（字形區） |
| `0x16 (22)` | `SZPS` | $zone$ | $\emptyset$ | 同時將 $zp0, zp1, zp2$ 全部綁定到指定區域 |
| `0x17 (23)` | `SLOOP` | $count$ | $\emptyset$ | 設置循環計數器：後續的 `SHP`、`IP`、`ALIGNPTS` 等指令自動連續執行 $count$ 次 |

### 4. 點位移動與微觀幾何對齊指令

#### `IUP[x]` 與 `IUP[y]`（內插未觸碰點，Interpolate Untouched Points）
TrueType 中**最重要的全局收尾指令**！在整個 Hinting 過程中，設計師通常只對字形輪廓上關鍵的骨架駐點（Touched Points，約佔總點數的 20%）執行了移動對齊。其餘 80% 的曲線過渡點處於“未被觸碰（Untouched）”狀態。
當在程序末尾調用 `IUP[x]` 或 `IUP[y]` 時，渲染引擎會沿着每一條封閉輪廓線進行線性掃描：在任意兩個被觸碰的極值錨點之間，依據原始設計網格的比例關係，**通過仿射內插算法一次性平滑重排中間所有未觸碰點的像素座標**，完美維持曲線的有機飽滿張力！

#### `MIRP[0..31]`（Move Indirect Relative Point）的五維位掩碼解構
操作碼範圍從十六進制 `0xCE` 到 `0xDF`（十進制 206–223）。這是一條極度強大的複合指令，指令編號本身低 5 位即編碼了完整的幾何控制邏輯：

```
MIRP[abcde] (操作码 = 0xCE + abcde)
Bit 4 (a): set_rp0      -> 若为 1，在完成移动后将 rp0 自动更新为当前目标点 p
Bit 3 (b): min_distance -> 若为 1，强制施加单极小距离约束（距离 >= SMD）
Bit 2 (c): round_dist   -> 若为 1，根据当前 RoundingState 对距离执行网格舍入
Bits 1-0 (de): color    -> 笔画距离色彩约束：
                           00: 灰度距离（无约束）
                           01: 黑色距离（笔画实体内部）
                           10: 白色距离（笔画之间的空白负空间）
```

*執行語義*：以參考點 $rp0$ 爲基準，讀取 CVT 表中索引爲 $cvt$ 的標準距離，沿自由向量 $\vec{f}$ 平移目標點 $p$，使得 $p$ 在投影向量 $\vec{p}$ 上的位移精確等於經網格舍入與切入判斷後的 CVT 間距！

#### `MDRP[0..31]`（Move Direct Relative Point）
與 `MIRP` 完全同構，但距離不取自 CVT，而是直接在原始設計輪廓上測量 $rp0$ 與目標點 $p$ 的初始歐氏距離。

### 5. 增量微調微指令（DELTAP 與 DELTAC）

在某些極具挑戰性的低分辨率場景下（例如在 10 像素或 12 像素點陣屏排版英文字母 'e' 或漢字“日”），通用的數學舍入規則往往會導致局部筆畫粘連或像素鏤空缺失。TrueType 提供了終極的物理級人工微調武器：**Delta 指令組**。

* **`DELTAP1`**：針對 9 到 24 像素（PPEM）的超小顯示環境；
* **`DELTAP2`**：針對 25 到 40 像素的中等環境；
* **`DELTAP3`**：針對 41 到 56 像素的大字號環境。

#### Delta 參數編碼與數學微調量方程：
每條 Delta 指令接受一組壓棧的參數對：$(arg, p)$，其中 $p$ 爲目標控制點索引，$arg$ 是一個通過單字節緊湊編碼的微位移複合數：

$$arg = (\text{nudge} + 8) \times 16 + (\text{target\_ppem} - \text{base\_ppem})$$

* **目標字號**：當且僅當當前屏幕光柵化分辨率 $\text{PPEM} == \text{base\_ppem} + (arg \bmod 16)$ 時，該指令纔會瞬間被激活！在其他任何字號下自動無視跳過；
* **微調量（Nudge）**：位移幅度由 $arg$ 的高 4 位決定（數值範圍從 $-8$ 到 $+7$）。實際施加在控制點上的空間物理平移向量爲：
  $$\Delta \vec{x} = \text{nudge} \times \left( \frac{1}{2^{\text{delta\_shift}}} \right) \text{ pixels} \times \vec{f}$$

通過將 `delta_shift` 設置爲 3（即 $\frac{1}{8}$ 像素分辨率），字體設計師可以極其優雅地宣告：“當字號恰好等於 11 像素時，將橫筆畫第 5 號節點向下微挪 $\frac{2}{8}$ 個像素”——正是這種微積分級別的極端控制力，成就了 Windows 操作系統在 CRT 顯示器時代傲視羣雄的卓越正文清晰度！

---

## E.4 字母表級全指令權威詞典速查（Alphabetical Instruction Reference）

以下按英文字母順序，完整收錄 TrueType 規範中定義的全部微指令執行細則：

### A 系列指令
* **`AA` (0x7F, 127)**：Adjust Angle。根據投影向量與自由向量調整參考線夾角。
* **`ADD` (0x60, 96)**：加法。棧頂兩數相加彈出，壓入兩數之和：$d = a + b$（單位：26.6 定點數）。
* **`ALIGNPTS` (0x27, 39)**：對齊兩點。彈出點 $p_1, p_2$，沿自由向量平移它們，使得兩者在投影向量上的座標重合到它們的中點。
* **`ALIGNRP` (0x3C, 60)**：對齊參考點。將目標點 $p$ 沿自由向量平移，使其在投影向量上的投影與參考點 $rp0$ 嚴格重合。
* **`AND` (0x5A, 90)**：邏輯與。棧頂兩數若皆非零壓入 1，否則壓入 0。

### C 系列指令
* **`CALL` (0x2B, 43)**：調用函數。彈出函數標識符，跳轉執行在 `fpgm` 中由 `FDEF` 預先定義的指令塊。
* **`CEILING` (0x67, 103)**：天花板向上取整。將 26.6 定點數的有效小數部分舍入到下一個整數邊界。
* **`CINDEX` (0x25, 37)**：複製指定深度操作數。彈出整數 $k$，將棧頂向下第 $k$ 個元素複製並壓入棧頂。
* **`CLEAR` (0x22, 34)**：清空操作數棧。將當前棧中所有殘留元素徹底彈出丟棄。

### D 系列指令
* **`DEBUG` (0x4F, 79)**：調試指令。用於字型調試器掛起執行，在發佈版字庫中自動忽略。
* **`DELTAC1..3` (0x73..0x75)**：控制值表微調。在特定 PPEM 下微調 CVT 槽位數值。
* **`DELTAP1..3` (0x5D, 0x71, 0x72)**：點位微調。在特定 PPEM 下對輪廓點施加 $\pm \frac{k}{8}$ 像素平移。
* **`DEPTH` (0x24, 36)**：測量棧深度。統計當前操作數棧中的元素總數壓入棧頂。
* **`DIV` (0x62, 98)**：除法。$d = (a \times 64) / b$，維持 26.6 標度。
* **`DUP` (0x20, 32)**：複製棧頂。將棧頂第一個元素複製一份壓入棧頂。

### E–F 系列指令
* **`EIF` (0x59, 89)**：條件分支結束（End If）。
* **`ELSE` (0x1B, 27)**：條件分支否定分支。
* **`ENDF` (0x2D, 45)**：函數定義結束（End Function）。
* **`EQ` (0x54, 84)**：相等判定。若 $a == b$ 壓入 1，否則壓入 0。
* **`EVEN` (0x57, 87)**：偶數判定。
* **`FDEF` (0x2C, 44)**：定義函數。在 `fpgm` 中開啓一段由函數 ID 標識的代碼塊。
* **`FLIPOFF` (0x4E, 78)**：強制將指定區間的點設置爲脫線控制點（Off-curve）。
* **`FLIPON` (0x4D, 77)**：強制將指定區間的點設置爲在線點（On-curve）。
* **`FLIPPT` (0x80, 128)**：翻轉點極性（On-curve $\leftrightarrow$ Off-curve）。
* **`FLOOR` (0x66, 102)**：地板向下取整。截斷 26.6 定點數小數位。

### G–I 系列指令
* **`GC[0..1]` (0x46..0x47)**：讀取點座標。測量點 $p$ 在投影向量上的當前物理座標（0 代表當前網格，1 代表原始設計網格）。
* **`GETINFO` (0x88, 136)**：查詢運行環境。獲取渲染器版本、是否支持灰度、ClearType 亞像素狀態。
* **`GFV` (0x0D, 13)**：讀取當前自由向量。
* **`GPV` (0x0C, 12)**：讀取當前投影向量。
* **`GT` / `GTEQ` (0x52, 0x53)**：大於與大於等於判定。
* **`IDEF` (0x89, 137)**：指令定義（Instruction Definition）。允許字庫重載或定義全新的虛擬機操作碼！
* **`IF` (0x58, 88)**：條件執行。彈出布爾值，若爲真繼續執行，若爲假跳至 `ELSE` 或 `EIF`。
* **`INSTCTRL` (0x8E, 142)**：指令執行控制。允許全局關閉 Hinting 或禁用特定平滑算法。
* **`IP` (0x39, 57)**：內插點（Interpolate Point）。以參考點 $rp1$ 與 $rp2$ 爲空間基準，將目標點 $p$ 沿自由向量平移，使其與兩參考點的相對距離比例保持不變。
* **`ISECT` (0x0F, 15)**：相交計算。計算直線 $(a_0, a_1)$ 與直線 $(b_0, b_1)$ 的空間幾何交點，並將目標點直接置於交點處。
* **`IUP[0..1]` (0x30..0x31)**：內插未觸碰點（0 針對 Y 軸，1 針對 X 軸）。

### J–M 系列指令
* **`JMPR` (0x1C, 28)**：無條件相對跳轉。
* **`JROF` / `JROT` (0x78, 0x79)**：條件相對跳轉（爲假跳轉 / 爲真跳轉）。
* **`LOOPCALL` (0x2A, 42)**：循環調用函數。連續執行指定函數若干次。
* **`LT` / `LTEQ` (0x50, 0x51)**：小於與小於等於判定。
* **`MAX` / `MIN` (0x63, 0x8B)**：極值選擇。
* **`MD[0..1]` (0x49..0x4A)**：測量兩點間距離（0 測量當前座標，1 測量原始輪廓）。
* **`MDAP[0..1]` (0x2E..0x2F)**：直接移動並對齊點。將點 $p$ 舍入到網格邊界並標記爲“已觸碰”。
* **`MDRP[0..31]` (0xC0..0xDF)**：直接相對移動點（根據 5 位標誌位解碼執行）。
* **`MIAP[0..1]` (0x3E..0x3F)**：間接移動並對齊點。將點 $p$ 移動到由 CVT 槽位指定的絕對距離處。
* **`MIRP[0..31]` (0xE0..0xFF)**：間接相對移動點（根據 5 位標誌位從 CVT 讀取距離執行）。
* **`MPPEM` (0x4B, 75)**：讀取當前每 Em 像素尺寸（Pixels Per Em）。
* **`MPS` (0x4C, 76)**：讀取當前點數磅值（Point Size）。
* **`MSIRP[0..1]` (0x3A..0x3B)**：移動直接絕對點並不施加網格舍入。
* **`MUL` (0x63, 99)**：乘法：$d = (a \times b) / 64$。

### N–R 系列指令
* **`NEG` (0x65, 101)**：數值取反：$d = -a$。
* **`NEQ` (0x55, 85)**：不等於判定。
* **`NOT` (0x5C, 92)**：邏輯非。
* **`NROUND[0..3]` (0x6C..0x6F)**：不施加引擎補償的四種純淨舍入。
* **`ODD` (0x56, 86)**：奇數判定。
* **`OR` (0x5B, 91)**：邏輯或。
* **`POP` (0x21, 33)**：彈出棧頂元素。
* **`RCVT` (0x45, 69)**：讀取 CVT 控制值。
* **`RDTG` (0x7D, 125)**：設置舍入狀態爲向下朝網格舍入（Round Down to Grid）。
* **`ROFF` (0x7A, 122)**：關閉網格舍入（Round Off）。
* **`ROLL` (0x8A, 138)**：操作數棧頂三元素迴轉滾動。
* **`ROUND[0..3]` (0x68..0x6B)**：帶光柵化引擎光學補償的網格舍入。
* **`RS` (0x43, 67)**：讀取 Storage 存儲區。
* **`RTDG` (0x3D, 61)**：設置舍入狀態爲雙倍網格舍入（0.5 像素精度）。
* **`RTG` (0x18, 24)**：設置舍入狀態爲常規網格舍入（Round to Grid）。
* **`RTHG` (0x19, 25)**：設置舍入狀態爲半網格舍入（Round to Half Grid）。
* **`RUTG` (0x7C, 124)**：設置舍入狀態爲向上朝網格舍入（Round Up to Grid）。

### S 系列指令
* **`S45ROUND` (0x77, 119)**：設置針對 $45^\circ$ 對角斜線的特殊網格舍入參數。
* **`SANGW` (0x7E, 126)**：設置傾斜角度權重。
* **`SCANCTRL` (0x85, 133)**：掃描轉換輟筆控制（Dropout Control）。激活極小像素孤立筆畫保護。
* **`SCANTYPE` (0x8D, 141)**：設置輟筆保護模式（簡單輟筆、智能相交輟筆）。
* **`SCFS` (0x48, 72)**：直接設置點在投影軸上的絕對座標。
* **`SCVTCI` (0x1D, 29)**：設置 CVT 切入閾值（Control Value Cut-In）。
* **`SDB` (0x5E, 94)**：設置 Delta 基準偏移量（Delta Base）。
* **`SDS` (0x5F, 95)**：設置 Delta 步進位移標度（Delta Shift）。
* **`SFVFS` (0x0B, 11)**：通過向量分量顯式設置自由向量。
* **`SFVTCA[0..1]` (0x04..0x05)**：設置自由向量平行於座標軸。
* **`SFVTL[0..1]` (0x08..0x09)**：設置自由向量平行或垂直於指定線段。
* **`SFVTPV` (0x0E, 14)**：令自由向量等於當前投影向量。
* **`SHC[0..1]` (0x34..0x35)**：平移輪廓（Shift Contour）。將指定輪廓上的所有點，按照參考點發生的位移整體平行平移！
* **`SHP[0..1]` (0x32..0x33)**：平移點（Shift Point）。將指定點按照參考點的位移平移。
* **`SHPIX` (0x38, 56)**：以絕對像素距離平移點序列。
* **`SHZ[0..1]` (0x36..0x37)**：平移整個幾何區域（Shift Zone）。
* **`SLOOP` (0x17, 23)**：設置後續單點指令的循環執行計數。
* **`SMD` (0x1A, 26)**：設置極小距離保持閾值（Minimum Distance）。
* **`SPVFS` (0x0A, 10)**：通過向量分量顯式設置投影向量。
* **`SPVTCA[0..1]` (0x02..0x03)**：設置投影向量平行於座標軸。
* **`SPVTL[0..1]` (0x06..0x07)**：設置投影向量平行或垂直於指定線段。
* **`SROUND` (0x76, 118)**：定製超強舍入狀態（顯式輸入 Period、Phase、Threshold）。
* **`SRP0..2` (0x10..0x12)**：分別將參考點寄存器 $rp0, rp1, rp2$ 指向指定點。
* **`SSW` (0x1F, 31)**：設置單筆畫全局寬度（Single Stroke Width）。
* **`SSWI` (0x20, 32)**：設置單筆畫寬度設計單位輸入值。
* **`SUB` (0x61, 97)**：減法：$d = a - b$。
* **`SVTCA[0..1]` (0x00..0x01)**：同時設置自由向量與投影向量平行於座標軸。
* **`SWAP` (0x23, 35)**：交換棧頂兩個元素的位置。
* **`SZP0..2` (0x13..0x15)**：分別設置區域指針 $zp0, zp1, zp2$ 綁定到 Zone 0 或 Zone 1。
* **`SZPS` (0x16, 22)**：同時將全部三個區域指針綁定到指定區域。

### U–W 系列指令
* **`UTP` (0x29, 41)**：取消觸碰狀態（Un-touch Point）。清除點的移動標記，使其能夠在隨後的 `IUP` 指令中接受平滑內插。
* **`WCVTF` (0x70, 112)**：將未縮放設計值寫入 CVT。
* **`WCVTP` (0x44, 68)**：將已縮放像素網格值寫入 CVT。
* **`WS` (0x42, 66)**：寫入 Storage 暫存寄存器。

通過這套完備嚴謹的虛擬機微指令體系，TrueType 賦予了字形設計師在最苛刻的屏幕像素環境下自由掌控每一個黑白點陣邊界的絕對權力。
---

## E.5 實戰演練：大寫字母 'H' 的完整虛擬機字節碼執行跟蹤（Instruction Execution Trace）

爲了徹底理解 TrueType 虛擬機的微觀運作機制，我們以大寫字母 'H' 爲例，完整跟蹤光柵化引擎在執行 `glyf` 表內部字節碼時的操作數棧、寄存器與控制點座標變化。

### 1. 字母 'H' 的幾何控制點拓撲：
字母 'H' 由 12 個關鍵控制點構成（全部爲在線點 On-curve Points）：
* 左立柱（Left Stem）：點 0（左下）、點 1（右下）、點 2（右上）、點 3（左上）；
* 中間橫樑（Crossbar）：點 4（左下交點）、點 5（右下交點）、點 6（右上交點）、點 7（左上交點）；
* 右立柱（Right Stem）：點 8（左下）、點 9（右下）、點 10（右上）、點 11（左上）。
此外，系統自動追加兩個幻影點（Phantom Points）：點 12（原點，X=0）與點 13（前進寬度點，X=AdvanceWidth）。

### 2. Y 軸方向網格對齊指令流執行跟蹤：

```tt-assembly
/* 步骤 1：将投影向量与自由向量同时设置为 Y 轴 (0, 1) */
SVTCA[y]

/* 步骤 2：对齐基线 */
/* 将点 0（左立柱底端）直接对齐到最近的物理像素网格边界，并标记为已触碰 (Touched) */
PUSHB[000] 0
MDAP[round]

/* 步骤 3：以点 0 为基准，拉伸并锁定左立柱高度 */
/* 设置参考点 rp0 = 0 */
PUSHB[000] 0
SRP0
/* 将点 3（左立柱顶端）移动到距 rp0 经 CVT 切入控制的标准大写字高处 */
PUSHB[001] 3 1  /* 参数：目标点 3，CVT 槽位 1 (CapHeight) */
MIRP[round,min,set_rp0] /* 移动后将 rp0 自动更新为点 3 */

/* 步骤 4：以大写字高为基准，平移右立柱顶端与横梁 */
/* 将点 10（右立柱顶端）与点 3 对齐在同一水平线上 */
PUSHB[000] 10
ALIGNRP

/* 将点 0 与点 9（右立柱底端）对齐到基线 */
PUSHB[000] 0
SRP0
PUSHB[000] 9
ALIGNRP

/* 步骤 5：定位横梁并锁定横梁厚度 */
/* 沿 Y 轴内插横梁下沿点 4 的位置 */
PUSHB[002] 4 0 3 /* 目标点 4，参考点 0 与 3 */
IP
/* 以点 4 为基准，向上锁定横梁厚度（读取 CVT 槽位 2: BarHeight） */
PUSHB[000] 4
SRP0
PUSHB[001] 7 2
MIRP[round,min,color_black]

/* 步骤 6：全局平滑内插 Y 轴所有剩余未触碰点 */
IUP[y]
```

### 3. X 軸方向網格對齊指令流：

```tt-assembly
/* 切换至 X 轴方向 (1, 0) */
SVTCA[x]

/* 对齐左侧轴承 (LSB) */
PUSHB[000] 0
MDAP[round]

/* 锁定左立柱宽度（从 CVT 槽位 3 读取 StdVW 垂直主干宽） */
PUSHB[000] 0
SRP0
PUSHB[001] 1 3
MIRP[round,min,set_rp0]

/* 锁定右立柱位置与宽度 */
/* 读取 CVT 槽位 4 (立柱间距)，将点 8 平移到正确间距 */
PUSHB[001] 8 4
MIRP[round,min,set_rp0]
/* 以点 8 为基准锁定右立柱宽度（点 9） */
PUSHB[001] 9 3
MIRP[round,min,color_black]

/* 横梁左右端点对齐到立柱内侧边 */
PUSHB[000] 1
SRP0
PUSHB[001] 4 7
ALIGNRP
ALIGNRP

PUSHB[000] 8
SRP0
PUSHB[001] 5 6
ALIGNRP
ALIGNRP

/* 最终对齐右侧幻影点（锁定字符总前进字宽） */
PUSHB[000] 9
SRP0
PUSHB[001] 13 5 /* CVT 槽位 5: 推荐前进字宽 */
MIRP[round,set_rp0]

/* 全局平滑内插 X 轴所有剩余未触碰点 */
IUP[x]
```

通過這一系列僅佔用約 60 字節緊湊機器碼的指令，字母 'H' 在從 9 像素到 200 像素的任意屏幕分辨率下，均能呈現絕對筆直、對稱、且粗細毫無波動的純淨像素晶格！
---

## E.6 圖形狀態機（Graphics State）24 維變量全景字典

在 TrueType 虛擬機執行期間，圖形狀態機（Graphics State）維護着一套直接決定所有幾何測量與網格吸附行爲的全局環境量：

| 狀態機變量名 | 數據類型 | 初始默認值 | 相關的讀取與設置指令 | 物理排版語義與控制行爲 |
| :--- | :--- | :--- | :--- | :--- |
| `auto_flip` | Boolean | `true` | `FLIPON`, `FLIPOFF` | 是否自動翻轉極性方向錯誤的筆畫控制點 |
| `control_value_cut_in` | F26Dot6 | `17/16` (68) | `SCVTCI` | CVT 強行吸附門限值（當輪廓尺寸與 CVT 偏差小於此值時強制鎖死） |
| `delta_base` | uint16 | `9` | `SDB` | Delta 指令激活的起始基礎字號（PPEM） |
| `delta_shift` | uint16 | `3` | `SDS` | Delta 微位移縮放步長（$1/2^{\text{delta\_shift}}$ 像素） |
| `dual_projection_vector` | Unit Vector | $(1, 0)$ | `SPVTCA`, `SPVTL`, `SPVFS` | 在未經變換的原始設計輪廓上測量初始距離的單位向量 |
| `freedom_vector` | Unit Vector | $(1, 0)$ | `SFVTCA`, `SFVTL`, `SFVFS`, `SFVTPV` | 點被允許移動的物理自由軸向單位向量 |
| `instruct_control` | uint8 | `0` | `INSTCTRL` | 全局指令執行掩碼（Bit 0: 關閉網格對齊; Bit 1: 忽略默認參數） |
| `loop` | uint16 | `1` | `SLOOP` | 循環計數器（後續多點移動指令連續執行的次數） |
| `minimum_distance` | F26Dot6 | `1.0` (64) | `SMD` | 相對移動時保持的兩筆畫最小物理保護間距（防止坍縮重疊） |
| `projection_vector` | Unit Vector | $(1, 0)$ | `SPVTCA`, `SPVTL`, `SPVFS` | 距離投影測量軸向單位向量 |
| `round_state` | State | `Round to Grid` | `RTG`, `RTHG`, `RTDG`, `RDTG`, `RUTG`, `ROFF`, `SROUND` | 當前數值量化爲像素網格的四捨五入規則引擎 |
| `rp0` | Point Index | `0` | `SRP0`, `MDRP`, `MIRP` | 參考點 0（作爲相對位移的起點錨點） |
| `rp1` | Point Index | `0` | `SRP1` | 參考點 1（用於內插指令 IP 的左基準） |
| `rp2` | Point Index | `0` | `SRP2` | 參考點 2（用於內插指令 IP 的右基準） |
| `scan_control` | uint16 | `0` | `SCANCTRL` | 極小字號下輟筆（Dropout）保護模式激活閾值 |
| `single_width_cut_in` | F26Dot6 | `0.0` | `SSWCI` | 單筆畫全局寬度統一吸附閾值 |
| `single_width_value` | F26Dot6 | `0.0` | `SSW` | 全局單筆畫標準物理寬度 |
| `zp0` | Zone Pointer | `1` | `SZP0`, `SZPS` | 目標點所在的幾何區域指針（Zone 0 黃昏區或 Zone 1 輪廓區） |
| `zp1` | Zone Pointer | `1` | `SZP1`, `SZPS` | 參考點 1 所在的幾何區域指針 |
| `zp2` | Zone Pointer | `1` | `SZP2`, `SZPS` | 參考點 2 所在的幾何區域指針 |

---

## E.7 黃昏區（Twilight Zone / Zone 0）的幽靈點力學

在複雜的字形 Hinting 中，字體設計師經常需要在字形輪廓外部構築臨時輔助幾何結構（例如兩條切線的虛交點、兩立柱正中軸線、或外接圓圓心），但這些輔助點**在最終字形光柵化時絕對不能被渲染成黑色像素**！

TrueType 專門開闢了一個與當前真實字形平行的虛擬內存區域——**黃昏區（Zone 0）**：
* 內部所有點均爲臨時的“幽靈點（Ghost Points）”；
* 通過將區域指針 `SZP0` 或 `SZPS` 設置爲 0，所有幾何微調指令（如 `ALIGNPTS`, `IP`, `ISECT`, `MDRP`）均可作用於黃昏區；
* 設計師可以先在黃昏區計算出完美的對稱幾何中心，再將真實字形（Zone 1）中的輪廓點綁定並內插到該中心點上，隨後退出。當光柵化引擎繪製文字時，Zone 0 的數據被直接丟棄，實現了純粹、無瑕且極度嚴謹的隱形空間工程學！
---

## E.8 Delta 指令人工微調實戰：小寫字母 'e' 的 11 像素防粘連微調

在 11 像素（PPEM = 11）這樣極端的超低分辨率下，小寫字母 'e' 的內腔留白只有 1 到 2 個像素。如果完全依賴數學四捨五入，橫樑上方的圓弧往往會因半網格吸附與橫樑粘連在一起，導致字母 'e' 變成一個實心的黑塊。

TrueType 字體工程師利用 `DELTAP` 指令進行精妙的人工微干預：

```tt-assembly
/* 针对小写字母 'e' 的顶部拱门最高点（点 5） */
/* 当且仅当 PPEM == 11 时，将点 5 向上微挪 2/8 个像素 (nudge = +2) */
/* 计算 arg: (2 + 8) * 16 + (11 - 9) = 10 * 16 + 2 = 162 */
PUSHB[001] 162 5
DELTAP1

/* 当且仅当 PPEM == 11 时，将横梁下沿（点 8）向下微挪 1/8 像素 (nudge = -1) */
/* 计算 arg: (-1 + 8) * 16 + (11 - 9) = 7 * 16 + 2 = 114 */
PUSHB[001] 114 8
DELTAP1
```

在 11 像素屏幕上，這兩條微調指令瞬間拉開了橫樑與圓弧之間整整 $\frac{3}{8}$ 像素的物理淨空間。在光柵化掃描轉換器進行中心點採樣時，橫樑上方恰好露出了一排乾淨清澈的白色背景像素——正是這種人工微調與自動算法的完美熔鑄，鑄就了數字字體在屏幕顯示史上的偉大奇蹟！
---

## E.9 輪廓平移與點序列平移指令全解（`SHP`, `SHC`, `SHZ`, `SHPIX`）

在 TrueType 中，除了單點移動指令外，虛擬機提供了極其強大的批量幾何平移指令集：

### 1. `SHP[0..1]`（Shift Point / 隨動點平移）
* **操作碼**：`0x32 (0)` 針對 $rp2$；`0x33 (1)` 針對 $rp1$；
* **堆棧輸入**：點編號序列 $p_1, p_2, \dots, p_k$（由 `loop` 計數器決定數量）；
* **執行語義**：計算參考點（$rp1$ 或 $rp2$）在當前 Hinting 過程中所經歷的累計平移位移向量：
  $$\Delta \mathbf{d} = \mathbf{x}_{\text{current}}(rp) - \mathbf{x}_{\text{original}}(rp)$$
  隨後，將堆棧中彈出的目標點 $p_i$ 沿自由向量 $\vec{f}$ 平移完全相同的標量距離！這保證了複雜襯線或裝飾突起能夠完美追隨主幹骨架平移，而不發生任何幾何變形。

### 2. `SHC[0..1]`（Shift Contour / 整體輪廓平移）
* **操作碼**：`0x34` / `0x35`；
* **堆棧輸入**：輪廓索引編號 $c$；
* **執行語義**：不僅平移單個控制點，而是**將指定輪廓 $c$ 上的所有在線點與脫線點作爲剛體整體平行平移**！在西文字符 'i' 與 'j' 的圓點輪廓對齊中，只需移動圓點上的一個極值點，隨後調用 `SHC`，整個實心圓點便能毫無形變地瞬間同步平移。

### 3. `SHPIX`（Shift Points by Pixel / 絕對像素平移）
* **操作碼**：`0x38 (56)`；
* **堆棧輸入**：位移標量 $d$（單位：26.6 定點像素數）與點序列；
* **執行語義**：直接沿自由向量將點平移指定的絕對像素距離，常用於強制微調孤立標點與下劃線基線。

---

# 附錄 F：METAFONT 與 MetaPost 技術參考指南（METAFONT and Its Derivatives）

1977 年，高德納在構思 TeX 的同時，深刻認識到傳統的“點陣像素描畫”與“剛性輪廓錄入”無法從根本上解決文字隨磅重、筆畫傾角與紙張墨暈動態演變的排印本質。他開創性地開發了 **METAFONT 語言**，將書法家手中的毛筆與平頭硬筆抽象爲幾何運筆過程，確立了全人類首個**純聲明式數學方程驅動的參數化字體設計範式**。隨後，高德納的弟子約翰·霍比（John Hobby）在此基礎上研發了能夠直接輸出矢量 PostScript 曲線的 **MetaPost** 系統，開源社區更演化出了 MetaFog、METATYPE1 以及由波蘭字體大師博古斯瓦夫·雅茨科夫斯基（Bogusław Jackowski）重鑄的 Antykwa Półtawskiego 經典字族。

本附錄將對 METAFONT 內部聲明式方程求解器的線性代數機制、畫筆包絡線微分幾何理論、轉向數定理（Turning Number Theorem）、Computer Modern 家族全部 62 個神聖設計參數詞典以及從參數化源文件向現代矢量字體轉化的 MF2PT1 流水線進行深度解構。

---

## F.1 METAFONT 編程語言與聲明式幾何方程求解器

在 METAFONT 代碼中，設計師從來不以過程式命令賦值座標（如傳統編程中的 `x = 5; y = 10`），而是直接書寫一組平等的聯立代數方程：

```metafont
x1 = x2 + 0.5w;
y1 = y2 = 0.5h;
z1 - z2 = whatever * (dir 30);
z3 = 0.5[z1, z2];
```

METAFONT 解釋器內部運行着一個極其高效的**動態符號線性方程求解機（Linear Equation Solver）**：

::: tip METAFONT 方程求解網絡與未定元膠囊（Capsule）環（Figure F-1, F-2）
![METAFONT 方程網絡（Figure F-1）](/images/fonts-encodings/fig-app-f1.png)
*METAFONT 方程網絡（Figure F-1）*
:::

*圖 F-1：METAFONT 內部變量依賴拓撲。每個未定未知數被包裝爲一個“膠囊（Capsule）”，並在內存中維護一個雙向依賴環。*

::: tip 線性代數高斯消元與解空間坍縮（Figure F-2）
![高斯消元解空間（Figure F-2）](/images/fonts-encodings/fig-app-f2.png)
*高斯消元解空間（Figure F-2）*
:::

*圖 F-2：當新的線性約束輸入時，解釋器立即執行高斯-約旦消元法（Gauss-Jordan Elimination）：將已知變量代入其餘膠囊，縮減未知自由度，直到整個幾何系統完全定解。*

### 1. 核心符號表示理論
每個內部數值被表示爲一個仿射線性多項式：

$$V = c_0 + c_1 X_1 + c_2 X_2 + \dots + c_k X_k$$

* 當用戶聲明 `z1 = z2 + (10, 20)` 時，系統並不強求立即知道 $z1$ 或 $z2$ 的絕對座標，而是建立等式約束：$X_{z1} - X_{z2} = 10$ 與 $Y_{z1} - Y_{z2} = 20$；
* 解釋器實時檢測方程組的秩（Rank）：若方程出現矛盾則報錯報告過度約束（Inconsistent equation）；若自由度未滿，程序繼續向下解析，直到後續代碼提供了足夠的幾何切線或邊界約束，整個方程網絡瞬間坍縮收斂出唯一的精確浮點解！

### 2. 小寫字母 'n' 的純數學參數化設計實戰

以下源碼展示瞭如何用 METAFONT 嚴密書寫一個帶雙立柱襯線、平滑拱門與動態筆寬的小寫拉丁字母 'n'：

```metafont
beginchar(110, 7pt#, 6pt#, 0pt#);
  u# = 1pt#; define_pixels(u);
  numeric x_height, oo, stem, join, serif_tip, serif_height, delta, offset;
  x_height = 5.1u; oo = .2u; stem = 1.1u; join = .2u;
  serif_tip = .2u; serif_height = .7u; delta = .033u; offset = .125u;

  % 左立柱下端与上端点
  z4 = (1.6u, delta); penpos4(stem, 180);
  x3 = x4 + offset; y3r = x_height;
  x3l - x3r = stem; y3l - y3r = .5serif_tip; z3 = .5[z3l, z3r];
  penstroke z3e .. {down}z4e;

  % 右立柱与拱门相交点
  x11 = w - 1.65u; y11 = y4; penpos11(stem, 180);
  y10 = y8 = .7x_height; z8 = whatever[z3, z4];
  z10 - z11 = whatever * (z3 - z4);
  z10l - z10r = z3l - z3r; z10 = .5[z10l, z10r];

  % 拱门最高张力圆弧
  penpos9(.87[join, stem], -136); y9l = x_height + oo; x9 = .68[x8, x10];
  z8' = whatever[z11, z10]; y8' = 1.25x_height;
  penpos8(join, angle(z8' - z8) - 90);
  penstroke z8e{z8' - z8} .. tension 1.5 .. z9e{right} .. z10e -- z11e;

  % 底部衬线装配
  numeric serif; serif = x11r - x12 = 1u;
  x7 - x4l = serif; x3r - x1 = .95serif; x4r - x5 = .9serif; x14 - x11l = .8serif;
  y1l = y3l; penpos1(serif_tip, -90); z2 = z3l;
  penpos2(1.25serif_height, angle(direction 0 of (z3l .. {down}z4l)));
  penstroke z1e{right} .. z2e;

  if (x7 - x4 + .2u + x11 - x12 > x11 - x4):
    x7 := .5[x4, x11] - .1u;
    x12 := .5[x4, x11] + .1u;
  fi;

  penpos5(serif_tip, -90); penpos7(serif_tip, -90);
  penpos12(serif_tip, -90); penpos14(serif_tip, -90);
  penpos6(serif_height, -90); penpos13(serif_height, -90);
  y5r = y7r = y12r = y14r = 0; z6r = z4; z13r = z11;
  penstroke z5e{right} .. z6e & z6e .. {right}z7e;
  penstroke z12e{right} .. z13e & z13e .. {right}z14e;
endchar;
```

#### 循環測試字重演進：
只需包裹一層 `for` 循環，令 `stem = (i/63)[join, 2.2u]`，METAFONT 便能在一瞬間自動生成 64 檔從 Hairline 到 Ultra-Black 的極其飽滿勻稱的字重連續變體！

---

## F.2 畫筆幾何學（Penspeck）與包絡線光柵化

與現代字體將字形視爲由空心多邊形輪廓構成的“皮囊”不同，METAFONT 認爲**文字是由一支具有特定物理幾何形狀的畫筆（Pen）沿着一條骨架軌跡（Path）運動而掃掠出的實體墨跡**！

::: tip 凸多邊形畫筆 Penspeck 離散網格化（Figure F-3, F-4）
![Penspeck 畫筆結構（Figure F-3）](/images/fonts-encodings/fig-app-f3.png)
*Penspeck 畫筆結構（Figure F-3）*
:::

*圖 F-3：畫筆規範體 `penspeck` 的離散化。橢圓畫筆首先被投影並多邊形化爲由一系列網格偏移向量構成的離散凸包（Convex Hull）。*

::: tip 畫筆掃掠包絡線（Envelope Tracing）微積分模型（Figure F-4）
![畫筆包絡線微分軌跡（Figure F-4）](/images/fonts-encodings/fig-app-f4.png)
*畫筆包絡線微分軌跡（Figure F-4）*
:::

*圖 F-4：包絡線微分方程：當具有中心點 $\mathbf{z}(t)$ 與凸包頂點 $\mathbf{v}_i$ 的畫筆沿軌跡行進時，墨跡邊界由外側切線法向量決定。*

數學上，畫筆掃掠區域（Envelope）的外邊緣曲線方程爲：

$$\mathcal{E}(t) = \mathbf{z}(t) + \mathbf{v}_{\text{active}}(t)$$

其中活動頂點 $\mathbf{v}_{\text{active}}(t)$ 滿足：畫筆在該頂點處的向外法向量與骨架曲線在 $t$ 時刻的切線向量嚴格平行！高德納設計了精妙的包絡線追蹤算法（Envelope Tracing Algorithm），將該微積分過程無縫映射爲離散 Bresenham 直線與圓弧生成器的協同運筆。

---

## F.3 轉向數定理（Turning Number Theorem）與拓撲環繞數

在評估複雜封閉貝塞爾輪廓的有效性與合法性時，METAFONT 引入了微分拓撲學中的**轉向數定理（Turning Number Theorem）**：

::: tip 轉向數定理與自相交環繞拓撲（Figure F-5, F-6）
![轉向數拓撲判定（Figure F-5）](/images/fonts-encodings/fig-app-f5.png)
*轉向數拓撲判定（Figure F-5）*
:::

*圖 F-5：平面光滑閉曲線 $\mathcal{C}$ 切線向量在單位圓上的高斯映射（Gauss Map）。切線向量沿曲線完整遍歷一圈所旋轉的總角度，必須是 $2\pi$ 的整數倍！*

::: tip 曲線拓撲奇異點與尖點消除（Figure F-6）
![曲線奇異點自愈（Figure F-6）](/images/fonts-encodings/fig-app-f6.png)
*曲線奇異點自愈（Figure F-6）*
:::

*圖 F-6：當曲線發生自相交（Self-intersection）或出現曲率無限大的奇異尖點（Cusps）時，轉向數發生突變，METAFONT 自動啓動切分與外輪廓布爾提取。*

對於一條無自相交的簡單正向閉合路徑，其全總曲率積分恆等於 $2\pi$（轉向數 $T = +1$）：

$$\frac{1}{2\pi} \oint_\mathcal{C} \kappa(s) \, ds = T \in \mathbb{Z}$$

這一嚴格的數學判據，使 METAFONT 能夠自動識別輪廓是外邊界還是內鏤空孔洞（如字母 'O' 的內部），並在光柵化時徹底杜絕翻轉走樣的發生。

---

## F.4 Computer Modern 字體家族 62 維全量參數參考詞典

Computer Modern（CM）是高德納采用 METAFONT 編寫的經典字體家族。整個龐大的字族（包含 75 款獨立字庫，覆蓋 5pt 到 17pt 的光學比例尺）全部由一組定義在 `cmbase.mf` 與各個字體驅動文件中的宏觀幾何參數所控制。

### 1. 垂直尺寸與高度參數（Vertical Dimensions）
* `u#`：基本設計單位寬度（Unit width in sharp units / points）；
* `width_corr#`：字符寬度微調補償量；
* `x_height#`：小寫字母 'x' 的主幹高度（Ex-height）；
* `cap_height#`：大寫正文字母高度（Cap height）；
* `asc_height#`：小寫字母升部高度（如 'b', 'd', 'h' 的頂部）；
* `desc_depth#`：小寫字母降部深度（如 'p', 'q', 'y' 的底部）；
* `body_height#`：帶重音大寫字母或最高括號的極限包圍盒頂部；
* `fig_height#`：等寬阿拉伯數字的標準高度；
* `math_axis#`：數學符號中軸線高度（分數線與加減號的中心高度）；
* `bar_height#`：小寫字母 'e' 的橫樑高度與字母 'A', 'H' 的交叉橫槓高度；
* `comma_depth#`：逗號與分號尾巴探入基線以下的深度。

### 2. 主幹與筆畫寬度參數（Stem and Stroke Widths）
* `hair#`：最細襯線或連接線畫筆直徑（Hairline thickness）；
* `stem#`：小寫正文字母主垂直幹筆畫寬度（Main vertical stem）；
* `curve#`：小寫圓弧字母彎角處最大膨脹寬度（如字母 'o', 'c' 的兩側最厚處）；
* `ess#`：字母 's' 中部傾斜主樑的最厚寬度；
* `flare#`：水滴狀筆畫端點（Teardrop terminal）的球頭最大直徑（如字母 'a', 'c', 'f', 'r' 的端部）；
* `dot_size#`：小寫字母 'i', 'j' 上方圓點與標點句號的直徑；
* `cap_hair#`：大寫字母最細筆畫厚度；
* `cap_stem#`：大寫字母主垂直幹筆畫寬度；
* `cap_curve#`：大寫圓弧字母兩側最大弧厚（如字母 'O', 'C', 'G'）；
* `cap_ess#`：大寫字母 'S' 中部斜幹最大厚度；
* `rule_thickness#`：數學公式分數線與方框線條的標準物理厚度；
* `thin_join#`：對角斜線交叉連接處的極小理論過渡寬度。

### 3. 襯線與括號連接參數（Serifs and Brackets）
* `dish#`：襯線底部的凹陷微弧度（Serif dish curvature）；
* `bracket#`：襯線與主幹之間的過渡圓角支架高度（Serif bracket height）；
* `jut#`：小寫字母水平襯線向外挑出的水平長度（Serif protrusion）；
* `cap_jut#`：大寫字母襯線外挑長度；
* `beak_jut#`：大寫字母 'E', 'F', 'T' 臂部尖喙（Beak）向外突出的水平長度；
* `beak#`：尖喙的垂直切削深度；
* `serif_drop#`：單向懸掛襯線向下滑落的垂直距離；
* `stem_corr#`：小寫字母主幹交匯處的切入收縮量；
* `vair_corr#`：細筆畫在連接拐角處的補償膨脹量；
* `slab#`：粗襯線字體（Slab Serif）中方形水平襯線的厚度；
* `cap_bar#`：大寫字母橫槓厚度；
* `cap_band#`：大寫字母封閉環帶厚度；
* `cap_notch_cut#`：大寫字形銳角內側爲了防止墨水堆積而切除的凹槽深度（Notch cut）。

### 4. 光學修正與高級形態參數（Optical Corrections & Style）
* `o#`：曲線或尖角在越過基線或頂線時的光學過沖量（Overshoot），消除人眼視覺縮小錯覺；
* `apex_o#`：大寫字母 'A', 'V', 'W' 尖頂或尖底處的額外過沖量；
* `apex_corr#`：尖頂點連接處的幾何回縮修正；
* `slant`：字體的傾斜率 $\tan(\theta)$（正體爲 0.0，斜體通常爲 0.25）；
* `fudge`：針對低分辨率或特殊黑度的全比例縮放軟調整因子；
* `math_spread`：數學公式符號之間的垂直鬆弛度；
* `superness`：超橢圓參數（Superellipse factor），控制曲線飽滿度（通常 $0.707 \dots 0.75$）；
* `superpull`：超橢圓內側向內吸附拉扯的修正係數；
* `beak_darkness`：尖喙區域黑度衰減權重。

### 經典 CM 字形在 10 磅下的參數對拍表（CMR10 vs CMBX10 vs CMTI10 vs CMSS10 vs CMTT10）：

| 參數名 | `cmr10`（正體） | `cmbx10`（粗體） | `cmti10`（西文斜體） | `cmss10`（無襯線） | `cmtt10`（等寬打字機） |
| :--- | :--- | :--- | :--- | :--- | :--- |
| `u#` | $20/36\text{ pt}$ | $23/36\text{ pt}$ | $18.5/36\text{ pt}$ | $19/36\text{ pt}$ | $21/36\text{ pt}$ |
| `slant` | $0.0$ | $0.0$ | $0.25$ | $0.0$ | $0.0$ |
| `x_height#` | $155/36\text{ pt}$ | $160/36\text{ pt}$ | $155/36\text{ pt}$ | $160/36\text{ pt}$ | $155/36\text{ pt}$ |
| `cap_height#` | $250/36\text{ pt}$ | $250/36\text{ pt}$ | $250/36\text{ pt}$ | $250/36\text{ pt}$ | $235/36\text{ pt}$ |
| `hair#` | $9/36\text{ pt}$ | $13/36\text{ pt}$ | $11/36\text{ pt}$ | $18/36\text{ pt}$ | $25/36\text{ pt}$ |
| `stem#` | $24/36\text{ pt}$ | $40/36\text{ pt}$ | $23/36\text{ pt}$ | $25/36\text{ pt}$ | $25/36\text{ pt}$ |
| `curve#` | $29/36\text{ pt}$ | $45/36\text{ pt}$ | $30/36\text{ pt}$ | $25/36\text{ pt}$ | $25/36\text{ pt}$ |
| `jut#` | $28/36\text{ pt}$ | $36/36\text{ pt}$ | $0.0$ | $0.0$ | $23/36\text{ pt}$ |
| `bracket#` | $20/36\text{ pt}$ | $20/36\text{ pt}$ | $0.0$ | $0.0$ | $14/36\text{ pt}$ |

---

## F.5 MetaPost、MetaFog 與現代矢量轉換管線

1990 年代，約翰·霍比在 MetaPost 中用三次樣條曲線平滑求解器替換了 METAFONT 的點陣光柵化模塊，使其能夠直接生成工業級的 EPS（Encapsulated PostScript）矢量輸出。

### 1. MetaFog：從輪廓到骨架的矢量重構
理查德·柯施（Richard Kinch）開發了著名的 MetaFog 引擎：
* 攔截 METAFONT 生成的高分辨率點陣位圖；
* 對離散像素進行多項式邊界擬合與拐點提取；
* 將離散的黑色墨跡還原爲光滑的三次貝塞爾曲線。

### 2. MF2PT1 與 Antykwa Półtawskiego 革命
波蘭著名字體工程師博古斯瓦夫·雅茨科夫斯基與雅努什·諾瓦茨基（Janusz M. Nowacki）推出了 **METATYPE1** 架構，並以此成功重鑄了波蘭國家級經典字族 Antykwa Półtawskiego：
1. 運行 MetaPost 解析帶有提示錨點的 METAFONT 源碼，生成無損的 PostScript 貝塞爾矢量輪廓；
2. 提取源碼中定義的極值點與筆畫特徵，自動將其轉換爲 PostScript Type 1 規範的 `hstem` 與 `vstem` 提示；
3. 將字符輪廓打包入 Type 1 二進制格式，使古老而深奧的 METAFONT 參數化書法字庫，徹底無縫融入當今現代桌面的 OpenType 與 PDF 矢量印刷工作流！
---

## F.6 光學縮放（Optical Scaling）的幾何物理學：從 CMR5 到 CMR17

在金屬活字時代，雕刻師在雕刻小磅活字（如 5 磅）時，絕對不是把 10 磅的大字機械等比例縮小。如果機械縮小，小字的細筆畫會因爲低於人眼分辨率極限而徹底消失，字母內腔（Counter）會因爲墨水堆積而變成黑團。

高德納通過 METAFONT 的參數化體系，在 Computer Modern 中完美復活了這門失傳已久的**光學比例雕刻技藝**：

### 1. CMR 家族不同磅值的設計參數對比表：

| 參數項 | `cmr5` (5pt) | `cmr7` (7pt) | `cmr10` (10pt) | `cmr12` (12pt) | `cmr17` (17pt) |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **相對字寬比率** (`u / pt`) | $0.065$ | $0.058$ | $0.055$ | $0.052$ | $0.048$ |
| **粗細對比度** (`stem / hair`) | $1.75$ (極低對比度) | $2.10$ | $2.66$ | $3.05$ | $3.80$ (高對比度) |
| **x 字高佔比** (`x_height / cap_height`) | $0.68$ (超大字高) | $0.65$ | $0.62$ | $0.60$ | $0.56$ (修長典雅) |
| **襯線長度** (`jut / pt`) | $0.095$ (強壯突出) | $0.084$ | $0.077$ | $0.072$ | $0.065$ (短小細膩) |

從表中可以清晰看出高德納的神聖規律：
* **5 磅微型字（CMR5）**：筆畫粗細對比極低（細筆畫被大幅加粗），x 字高比例極大，字形整體橫向膨脹變寬，襯線粗壯外挑，確保在極端縮微環境下依舊堅挺清晰；
* **17 磅標題字（CMR17）**：筆畫粗細對比極其強烈（細筆畫如蛛絲般纖細，主幹厚重飽滿），字身修長收斂，展現出頂級古典活字的華貴排印氣派！

---

## F.7 波蘭 METATYPE1 架構與 Antykwa Półtawskiego 的現代重塑

1990 年代末，波蘭著名字體工程師博古斯瓦夫·雅茨科夫斯基與雅努什·諾瓦茨基深刻認識到，METAFONT 生成的位圖雖然在 TeX 中表現優異，但在需要無極縮放的 PDF 與現代 PostScript 打印機中受制於固定分辨率。

他們開發了 **METATYPE1 宏包**，對 METAFONT 進行了顛覆性的改造：
1. **畫筆剝離**：將 METAFONT 的畫筆掃掠運算徹底替換爲顯式輪廓邊界微分追蹤；
2. **極值點自適應切分**：自動計算曲線在水平和垂直方向的切線極值點，並在極值點處強制切斷爲獨立的三次貝塞爾曲線段；
3. **自動化 Hinting 編譯器**：通過分析控制點之間的距離，自動生成符合 PostScript Type 1 規範的 `hstem`、`vstem` 與動態提示替換（Hint Substitution）指令塊！

利用這套宏偉的架構，他們完整復刻並開源了由亞當·波烏塔夫斯基（Adam Półtawski）在 1928 年設計的波蘭國寶級字體 **Antykwa Półtawskiego**。這部橫跨七十年的數字字體工程史詩，徹底證明了高德納聲明式參數幾何哲學的無限生命力。
---

## F.8 METAFONT 參數代數約束系統與幾何和諧方程

在設計 Computer Modern 字體時，高德納並未將 62 個參數視爲相互孤立的旋鈕，而是建立了一套極其深邃的**代數約束拓撲網（Algebraic Dependency Network）**：

### 1. 襯線與主幹的和諧方程：
* **襯線厚度與主幹協調**：
  $$\text{bracket\#} = \min\left(20/36\text{ pt\#}, \; 0.8 \times \text{stem\#}\right)$$
  當字重大幅增加（如黑體 `cmbx10`，`stem#` 從 24 暴增至 40）時，襯線托架的高度不能無限制增長，否則整個字母底座會變成實心黑塊；
* **光學過沖補償方程**：
  對於圓弧字母（如 'O'）越過基線的下垂過沖量 $o\#$ 與尖頂字母（如 'A'）的頂點過沖量 $\text{apex\_o}\#$：
  $$\text{apex\_o\#} = \frac{4}{3} \times o\#$$
  因爲尖銳單點在人眼中造成的收縮錯覺，遠比圓弧平緩接觸造成的視覺錯覺強烈得多，必須施加更大的物理幾何代數過沖！

---

## F.9 高德納數學排印美學哲學與數字字體未來

在《Digital Typography》與圖靈獎演講中，高德納曾寫下排印技術史上的傳世箴言：
> “字型不是僵死的墨跡標本，而是一組由活生生的數學思想所驅動的有機函數。”

傳統的鉛字活字將字母永久定格在金屬方塊之中，二十世紀初的光學照排又將其鎖死在靜止的感光膠片上；而 METAFONT 則將文字解放爲微分幾何與代數方程的優雅舞步。

儘管今天純粹書寫 METAFONT 代碼的字型設計師日漸稀少，但其播撒下的思想種子——從 PostScript 貝塞爾曲線、OpenType 狀態機、到可變字體（Variable Fonts）的連續設計軸與自動 Hinting 算法——已化作當今全球數字排印文明生生不息的底層血脈。
---

## F.10 METAFONT 8 方位離散光柵運筆算法（The Eight Octants of Raster Graphics）

爲了在純整數網格上無損追蹤畫筆包絡線，高德納將二維平面嚴格劃分爲 8 個連續的角度卦限（Octants）：
* **卦限 1**：$0^\circ \le \theta < 45^\circ$（主移動軸爲 $+X$，輔助移動軸爲 $+Y$）；
* **卦限 2**：$45^\circ \le \theta < 90^\circ$（主移動軸爲 $+Y$，輔助移動軸爲 $+X$）；
* **卦限 3 至 8**：依次類推覆蓋全平面。

在每一個卦限內部，畫筆凸包與外界切線的接觸頂點是**嚴格恆定不變的**！當運筆軌跡從卦限 1 跨越 $45^\circ$ 進入卦限 2 時，接觸頂點瞬間發生躍遷切替。高德納證明了：通過將曲線軌跡切分爲單調卦限段，畫筆掃掠運算可以完全退化爲基於加減法與位移的純整數判別式遞推，在 1970 年代運行速度極慢的小型機上實現了每秒渲染數十個高精度字形輪廓的驚人奇蹟。
---

## F.11 MetaPost 宏系統與圖表排版自動化流水線

MetaPost 之所以能夠從 METAFONT 中獨立演進爲學術出版界的圖表神器，關鍵在於其對宏系統（Macro System）的極致擴展：
* **`btex ... etex` 橋接機制**：MetaPost 允許在圖形代碼中內嵌原生的 LaTeX 數學公式源碼。在編譯時，MetaPost 自動調用後臺 TeX 引擎將公式排版爲 DVI 盒子並測量其精確包圍盒，再將公式輪廓無損嵌入到生成的 EPS 或 PDF 圖形中；
* **圖形對象（Pictures）與多重變換**：支持將一整組路徑組合封裝爲單一圖形對象（`picture`），並對其施加平移（`shifted`）、縮放（`scaled`）、旋轉（`rotated`）以及傾斜（`slanted`）等高階仿射矩陣變換，實現了全自動的學術期刊插圖生產線。

---

# 附錄 G：字型設計中的曲線微分幾何學與樣條數學理論（Differential Geometry of Curves）

在現代矢量字體工程中，字符輪廓並非簡單的折線拼接，而是建立在極其嚴密的微分幾何學與代數拓撲學基礎之上。從 TrueType 採用的二次有理貝塞爾曲線（Quadratic Bézier），到 PostScript Type 1 與 OpenType CFF 採用的三次貝塞爾曲線（Cubic Bézier），再到高端書法設計中的歐拉螺線（Euler Spirals / Cornu Spirals），字體設計師在屏幕上拖動控制點所施加的每一個微小位移，都在底層激發了一場高階張量與微積分方程的精密運算。

本附錄將對字型設計涉及的核心微分幾何學理論進行完整的純數學解析：從伯恩斯坦基底（Bernstein Basis）的單位分解定理、極式（Blossom）映射、德卡斯特里奧（de Casteljau）遞歸細分算法、微分矢端曲線（Hodograph），到曲率公式（Curvature）、拐點（Inflection Points）判定與等距偏移曲線（Offset Curves）的非有理本質，以及歐拉角螺線在現代參數化字體輪廓擬閤中的前沿應用。

---

## G.1 伯恩斯坦多項式基底與代數拓撲性質

一條定義在參數區間 $t \in [0, 1]$ 上的 $n$ 次貝塞爾曲線，在數學上定義爲 $n+1$ 個幾何控制點 $\mathbf{P}_0, \mathbf{P}_1, \dots, \mathbf{P}_n \in \mathbb{R}^2$ 關於 $n$ 次**伯恩斯坦基多項式（Bernstein Polynomials）**的凸組合線性疊加：

$$\mathbf{B}(t) = \sum_{i=0}^n B_{i,n}(t) \, \mathbf{P}_i, \quad t \in [0, 1]$$

其中 $n$ 次伯恩斯坦基函數由二項式係數與乘冪嚴格定義爲：

$$B_{i,n}(t) = \binom{n}{i} t^i (1-t)^{n-i}, \quad i = 0, 1, \dots, n$$

這裏 $\binom{n}{i} = \frac{n!}{i!(n-i)!}$ 爲組合二項式係數。

### 核心微分幾何定理與嚴格證明

#### 定理 1：單位分解性（Partition of Unity）
在全實數域上，所有 $n$ 次伯恩斯坦多項式的代數和恆等爲 1：

$$\sum_{i=0}^n B_{i,n}(t) \equiv 1, \quad \forall t \in \mathbb{R}$$

*證明*：根據牛頓二項式定理（Binomial Theorem），對於任意實數 $a, b$，恆有 $(a + b)^n = \sum_{i=0}^n \binom{n}{i} a^i b^{n-i}$。令 $a = t$ 且 $b = 1-t$，則有：
$$\sum_{i=0}^n B_{i,n}(t) = \sum_{i=0}^n \binom{n}{i} t^i (1-t)^{n-i} = (t + (1-t))^n = 1^n = 1 \quad \blacksquare$$

**字型排印物理學意義**：單位分解性確保了貝塞爾曲線具有**仿射不變性（Affine Invariance）**！無論我們對字庫進行整體平移、旋轉、縮放還是施加傾斜矩陣變換，直接對控制點施加變換後的新曲線，與原曲線上每個點分別計算變換後的結果在數學上嚴格絕對重合！

#### 定理 2：非負性（Positivity）
當且僅當參數 $t$ 落在字形輪廓的合法物理區間 $[0, 1]$ 內時，所有基函數恆爲非負：

$$B_{i,n}(t) \ge 0, \quad \forall t \in [0, 1]$$

結合定理 1，這證明了曲線上的任意一點 $\mathbf{B}(t)$ 都是控制多邊形頂點的**真凸組合（Convex Combination）**，從而嚴格證明了**凸包性質（Convex Hull Property）**：整條字形輪廓線被嚴格約束在控制點圍成的凸多邊形內部，渲染引擎可藉此實現毫秒級快速包圍盒粗篩求交！

#### 定理 3：端點插值與邊界切線控制（Endpoint Interpolation）
代入 $t = 0$ 與 $t = 1$，有：
$$\mathbf{B}(0) = \mathbf{P}_0, \quad \mathbf{B}(1) = \mathbf{P}_n$$
曲線在起點的切線方向平行於向量 $\mathbf{P}_1 - \mathbf{P}_0$，在終點的切線方向平行於向量 $\mathbf{P}_n - \mathbf{P}_{n-1}$。這一極其優美的幾何性質，賦予了字體設計師通過直接移動前後控制點把控曲線兩端連接切線的絕對權力。

#### 定理 4：遞推關係與微分性質（Recurrence & Derivatives）
$$B_{i,n}(t) = (1-t) B_{i,n-1}(t) + t B_{i-1,n-1}(t)$$
$$\frac{d}{dt} B_{i,n}(t) = n \left( B_{i-1,n-1}(t) - B_{i,n-1}(t) \right)$$

---

## G.2 極式（Blossoms / Polar Forms）與多線性映射理論

由法國數學家保羅·德卡斯特里奧與拉馬爾·拉姆齊（Lyle Ramshaw）提出的**極式（Polar Form，或稱 Blossom 花式）理論**，將抽象繁瑣的貝塞爾曲線代數運算徹底轉化爲優美純粹的多線性仿射幾何學。

對於一條 $n$ 次單變量多項式曲線 $\mathbf{P}(t)$，存在唯一一個關於 $n$ 個獨立變量的對稱多重仿射函數（Symmetric Multiaffine Map） $p(u_1, u_2, \dots, u_n)$，滿足以下三大公理：
1. **全對稱性（Symmetry）**：交換任意兩個輸入參數的次序，函數值嚴格不變：
   $$p(u_{\pi(1)}, u_{\pi(2)}, \dots, u_{\pi(n)}) = p(u_1, u_2, \dots, u_n)$$
2. **多重仿射性（Multiaffinity）**：固定其中任意 $n-1$ 個變量，關於剩餘的一個變量是純粹的仿射線性映射：
   $$p(\dots, \, (1-\alpha)u + \alpha v, \, \dots) = (1-\alpha) p(\dots, u, \dots) + \alpha p(\dots, v, \dots)$$
3. **對角坍縮性（Diagonal Property）**：當所有 $n$ 個參數全部取同一數值 $t$ 時，極式瞬間坍縮爲原始貝塞爾曲線本身：
   $$p(t, t, \dots, t) = \mathbf{P}(t)$$

### 極式視角的控制點黃金對應律：
曲線的幾何控制點 $\mathbf{P}_i$，在極式空間中具有令人驚歎的離散端點取值表達：

$$\mathbf{P}_i = p(\underbrace{0, \dots, 0}_{n-i \text{ 个}}, \, \underbrace{1, \dots, 1}_{i \text{ 个}})$$

例如對於三次貝塞爾曲線（$n=3$）：
* 起點：$\mathbf{P}_0 = p(0, 0, 0)$；
* 第一控制點：$\mathbf{P}_1 = p(0, 0, 1)$；
* 第二控制點：$\mathbf{P}_2 = p(0, 1, 1)$；
* 終點：$\mathbf{P}_3 = p(1, 1, 1)$。

在子區間 $[a, b]$ 上對曲線進行局部截取時，新曲線的控制點只需直接求值 $p(a, a, a), p(a, a, b), p(a, b, b), p(b, b, b)$，徹底終結了繁瑣的座標變換公式！

---

## G.3 升階代數矩陣：從二次 TrueType 到三次 PostScript

在字體格式跨平臺轉換中，將 TrueType（二次貝塞爾曲線，$n=2$）轉換爲 PostScript Type 1 / OpenType CFF（三次貝塞爾曲線，$n=3$）是一項核心基礎操作。**升階（Degree Elevation）必須保證曲線在幾何形狀、切線方向與曲率上絕對恆定**。

### 升階通用遞推公式：
將 $n$ 次曲線升爲 $n+1$ 次曲線，新的控制點 $\mathbf{P}_i^{(n+1)}$ 由舊控制點線性組合得出：

$$\mathbf{P}_i^{(n+1)} = \frac{i}{n+1} \mathbf{P}_{i-1}^{(n)} + \left(1 - \frac{i}{n+1}\right) \mathbf{P}_i^{(n)}, \quad i = 0, 1, \dots, n+1$$

### 二次轉三次升階封閉解：
設二次 TrueType 曲線由起點 $\mathbf{P}_0$、脫線控制點 $\mathbf{P}_1$ 與終點 $\mathbf{P}_2$ 定義，升階爲三次曲線後的四個控制點 $\mathbf{Q}_0, \mathbf{Q}_1, \mathbf{Q}_2, \mathbf{Q}_3$ 精確等於：

$$\begin{cases}
\mathbf{Q}_0 = \mathbf{P}_0 \\
\mathbf{Q}_1 = \mathbf{P}_0 + \frac{2}{3}(\mathbf{P}_1 - \mathbf{P}_0) = \frac{1}{3}\mathbf{P}_0 + \frac{2}{3}\mathbf{P}_1 \\
\mathbf{Q}_2 = \mathbf{P}_2 + \frac{2}{3}(\mathbf{P}_1 - \mathbf{P}_2) = \frac{2}{3}\mathbf{P}_1 + \frac{1}{3}\mathbf{P}_2 \\
\mathbf{Q}_3 = \mathbf{P}_2
\end{cases}$$

此公式在數學上嚴謹證明了：**任何二次貝塞爾曲線均可以毫無任何誤差、100% 精確地表達爲一條三次貝塞爾曲線**！反之，三次曲線由於自由度更高（具有兩個獨立控制點，可能包含拐點），通常無法用單一二次曲線精確表示，必須通過曲率極值點分割算法切斷爲多段二次曲線逼近。

---

## G.4 德卡斯特里奧（de Casteljau）遞歸細分算法

在光柵化碰撞檢測、字符曲線相交運算與局部裁剪時，德卡斯特里奧算法提供了數值上極度穩定的幾何細分手段。

### 細分三角形金字塔算法：
給定參數 $t_0 \in (0, 1)$，定義點序列的遞歸線性插值：

$$\mathbf{P}_i^{(k)}(t_0) = (1-t_0)\mathbf{P}_i^{(k-1)}(t_0) + t_0 \mathbf{P}_{i+1}^{(k-1)}(t_0)$$

其中 $\mathbf{P}_i^{(0)} = \mathbf{P}_i$ 爲原始控制點。當 $k=n$ 時，頂峯點 $\mathbf{P}_0^{(n)}(t_0) = \mathbf{B}(t_0)$ 即爲曲線上對應點的物理座標。

細分完成後，原始曲線在 $t_0$ 處被切斷爲兩段獨立的子貝塞爾曲線：
* 左段曲線控制點序列：$\mathbf{P}_0^{(0)}, \mathbf{P}_0^{(1)}, \mathbf{P}_0^{(2)}, \dots, \mathbf{P}_0^{(n)}$；
* 右段曲線控制點序列：$\mathbf{P}_0^{(n)}, \mathbf{P}_1^{(n-1)}, \mathbf{P}_2^{(n-2)}, \dots, \mathbf{P}_n^{(0)}$。

#### Python 工業級德卡斯特里奧細分實現：
```python
def de_casteljau_subdivide(points: list, t: float = 0.5):
    """
    对任意阶贝塞尔曲线在参数 t 处进行数值无损细分
    """
    n = len(points) - 1
    pyramid = [list(points)]
    
    for r in range(1, n + 1):
        prev_row = pyramid[-1]
        next_row = []
        for i in range(len(prev_row) - 1):
            p0 = prev_row[i]
            p1 = prev_row[i + 1]
            interp = (
                (1 - t) * p0[0] + t * p1[0],
                (1 - t) * p0[1] + t * p1[1]
            )
            next_row.append(interp)
        pyramid.append(next_row)
        
    left_curve = [pyramid[r][0] for r in range(n + 1)]
    right_curve = [pyramid[n - r][r] for r in range(n + 1)]
    return left_curve, right_curve
```

### 變分縮減性質（Variation Diminishing Property）：
**貝塞爾曲線的波動幅度絕不會超過其控制多邊形！** 任何一條直線與貝塞爾曲線輪廓的實際交點個數，恆小於等於該直線與對應控制多邊形折線的交點個數。該定理徹底保證了字體設計師在調整控制點時，輪廓絕不會莫名其妙地產生多餘的寄生波紋與褶皺震盪！

---

## G.5 微分矢端曲線（Hodograph）與速度加速度張量

貝塞爾曲線的各階導數本身**依然是一條純粹的貝塞爾曲線**！其控制向量構成了幾何學上的**矢端曲線（Hodograph）**。

### 一階導數（速度向量 / 切線向量）：
$$\mathbf{B}'(t) = n \sum_{i=0}^{n-1} B_{i,n-1}(t) \, (\mathbf{P}_{i+1} - \mathbf{P}_i)$$

* 曲線在起點的切線方向恆平行於向量 $\mathbf{P}_1 - \mathbf{P}_0$；
* 曲線在終點的切線方向恆平行於向量 $\mathbf{P}_n - \mathbf{P}_{n-1}$。

### 二階導數（加速度向量）：
$$\mathbf{B}''(t) = n(n-1) \sum_{i=0}^{n-2} B_{i,n-2}(t) \, (\mathbf{P}_{i+2} - 2\mathbf{P}_{i+1} + \mathbf{P}_i)$$

二階導向量反映了字形輪廓在行進過程中偏離直線的彎曲加速度，直接決定了下文的曲率演變。

---

## G.6 平面曲線曲率（Curvature）與微分不變量

曲率 $\kappa(t)$ 是衡量字體輪廓在某一點彎曲程度的核心不變量，其物理意義爲單位弧長內切線方向角的旋轉變化率：

$$\kappa(t) = \frac{x'(t)y''(t) - y'(t)x''(t)}{\left(x'(t)^2 + y'(t)^2\right)^{3/2}}$$

* **曲率半徑（Radius of Curvature）**：$R(t) = \frac{1}{|\kappa(t)|}$；
* **密切圓（Osculating Circle）**：在點 $\mathbf{B}(t)$ 處沿法向量向內偏移 $R(t)$ 處的圓，與曲線在該點具有二階切觸精度；
* **拐點（Inflection Point）**：曲率變號的位置，即分子 cross product 恆等於零之處：
  $$x'(t)y''(t) - y'(t)x''(t) = 0$$
  在高質量字形設計中，二次貝塞爾曲線由於二階導數恆爲常數向量，其內部**絕對不可能出現拐點**；三次貝塞爾曲線內部**最多隻能存在一個拐點**！若字符設計需要呈現“S”形平滑波浪，必須確保該拐點處的二階曲率保持 $G^2$ 連續（曲率數值大小與正負無縫銜接），否則人眼在反射光影下會察覺到極度刺眼的“斷腰”視覺殘瑕！
* **奇異尖點（Cusps）**：當一階速度向量同時歸零時：$x'(t) = y'(t) = 0$。曲率在此處退化，切線發生 $180^\circ$ 倒轉。

---

## G.7 等距偏移曲線（Offset Curves）的非多項式物理本質

在字體加粗（Stroke Boldening）、空心字生成（Outline Stroke）以及字形輪廓膨脹算法中，排版引擎需要沿法線方向將曲線向外推擠 $\delta$ 距離，生成**等距偏移曲線（Offset Curve / Parallel Curve）**：

$$\mathbf{C}_\delta(t) = \mathbf{C}(t) + \delta \, \mathbf{n}(t) = \mathbf{C}(t) + \delta \, \frac{\left(-y'(t), \, x'(t)\right)}{\sqrt{x'(t)^2 + y'(t)^2}}$$

### 字體工程中的終極難題：偏移曲線的非有理本質
計算機輔助幾何設計（CAGD）領域的一個著名殘酷定理指出：**除了平凡的直線段與圓弧之外，任何多項式貝塞爾曲線的等距偏移曲線，在數學上絕對不可能再用有限階的有理貝塞爾曲線精確表示！**

其根源在於法向量分母中的平方根項 $\sqrt{x'(t)^2 + y'(t)^2}$ 引入了不可約化的代數分支割線。不僅如此，當偏移距離 $\delta$ 超過局部最小曲率半徑 $R(t)$ 時，偏移曲線內部必然會產生極其詭異的**燕尾自相交奇異點（Swallowtail Singularities）**！

現代專業字體設計軟件（如 FontLab、Glyphs、FontForge）在執行“擴大筆畫輪廓”時，必須調用高階數值逼近管線：
1. 計算曲率極大值點，將原始曲線切分爲單調曲率段；
2. 依據 Tiller-Hanson 算法，在每段曲線兩端估算法向量偏移控制點；
3. 檢測並執行微分拓撲裁剪，徹底消除燕尾自交環；
4. 最終以微米級公差擬合出平滑封閉的高品質 OpenType 矢量輪廓。

---

## G.8 歐拉角螺線（Euler Spirals / Cornu Spirals）與現代樣條

在傳統三次貝塞爾曲線中，曲線的曲率通常是參數 $t$ 的高階有理分式，其曲率分佈極難保持單調或線性變化，往往導致字形高光反射線呈現輕微的扭曲（稱爲“曲率抖動”）。

爲了追求終極的書法級光學平滑度，拉夫·萊維恩（Raph Levien）在設計 Spiro 樣條引擎時，引入了經典力學與光學中的**歐拉螺線（又稱柯奴螺線，Cornu Spirals / Clothoids）**。

### 歐拉螺線核心物理方程：
歐拉螺線的幾何本質在於：**曲線的曲率 $\kappa$ 與弧長 $s$ 嚴格成正比**！

$$\kappa(s) = \frac{d\theta}{ds} = 2 a s$$

對弧長進行積分，得到切線傾角方程：

$$\theta(s) = \int_0^s \kappa(u) \, du = a s^2$$

在笛卡爾座標系中，歐拉螺線的參數方程由著名的菲涅耳積分（Fresnel Integrals）嚴格定義：

$$x(s) = \int_0^s \cos(a u^2) \, du, \quad y(s) = \int_0^s \sin(a u^2) \, du$$

由於曲率隨弧長完美線性漸變，兩個由歐拉螺線連接的幾何線段天然具備絕對完美的 $G^2$ 甚至 $G^3$ 連續性。現代前沿字體設計工具先通過歐拉螺線建立全局美學骨架，再將其自適應切分轉化爲標準 OpenType 三次貝塞爾曲線，實現了古代書法藝術與現代微分幾何學的最高統一。
---

## G.9 幾何光滑度連續性階次（Continuity Classes: $C^k$ vs $G^k$）

在高質量字體輪廓拼接（Spline Joining）中，兩個相鄰貝塞爾曲線段在連接點處的平滑度，劃分爲**參數連續性（Parametric Continuity, $C^k$）**與**幾何連續性（Geometric Continuity, $G^k$）**兩大流派：

### 1. 各級連續性的微分定義：
* **$C^0$ / $G^0$ 連續（位置連續）**：兩曲線段首尾相接，共用同一點：$\mathbf{B}_1(1) = \mathbf{B}_2(0)$；
* **$C^1$ 連續（一階導數連續）**：兩曲線不僅切線方向重合，且一階導數向量的大小與方向完全相等：$\mathbf{B}_1'(1) = \mathbf{B}_2'(0)$；
* **$G^1$ 連續（切線方向連續）**：兩曲線在連接點處的單位切向量平行，但模長允許不相等：
  $$\frac{\mathbf{B}_1'(1)}{\|\mathbf{B}_1'(1)\|} = \frac{\mathbf{B}_2'(0)}{\|\mathbf{B}_2'(0)\|}$$
  在字型設計中，這意味着控制點 $\mathbf{P}_2$、端點 $\mathbf{P}_3 = \mathbf{Q}_0$ 與後一曲線控制點 $\mathbf{Q}_1$ **三點嚴格共線**，但線段長度比可以任意調整；
* **$C^2$ 連續（二階導數連續）**：兩曲線的二階導數向量嚴格相等：$\mathbf{B}_1''(1) = \mathbf{B}_2''(0)$；
* **$G^2$ 連續（曲率連續，Curvature Continuity）**：兩曲線在連接點處的**曲率數值與曲率中心嚴格連續**：
  $$\kappa_1(1) = \kappa_2(0)$$

### 2. 爲什麼專業字體設計必須追求 $G^2$ 連續？
人眼視覺感知對曲率的跳躍極其敏感。在僅僅滿足 $G^1$ 連續的輪廓連接處（例如圓弧平整過渡到直線的傳統倒角），雖然切線沒有折角，但曲率從常數（$1/R$）瞬間斷崖式跌落到直線的 0。在屏幕光柵化或印刷高光下，人眼會在該拐角處清晰察覺到一條刺眼的暗影摺痕（稱爲“光學斷骨”）。

通過調節控制點使曲線在交界處達成 $G^2$ 連續，字形輪廓的曲率梳（Curvature Comb）將呈現連續光滑演變，賦予字符如水銀瀉地般的有機書法美感！

---

## G.10 基於矢端極值點求根的極限包圍盒（BBox）極速求值算法

在字體渲染管線中，精確計算字符曲線在 X 軸與 Y 軸上的極限包圍盒（Bounding Box: $x_{\min}, y_{\min}, x_{\max}, y_{\max}$）是一項每秒觸發數萬次的極高頻操作。

由於貝塞爾曲線可能在區間內部向外隆起凸出，極限座標並不一定出現在端點處，而是可能出現在一階導數等於零的**極值駐點（Stationary Points）**處！

### 三次貝塞爾導數二次方程求解：
一階導數方程 $x'(t) = 0$ 展開爲一個一元二次多項式：

$$x'(t) = 3(1-t)^2(x_1 - x_0) + 6(1-t)t(x_2 - x_1) + 3t^2(x_3 - x_2) = A t^2 + B t + C = 0$$

其中係數展開爲：

$$\begin{cases}
A = 3(-x_0 + 3x_1 - 3x_2 + x_3) \\
B = 6(x_0 - 2x_1 + x_2) \\
C = 3(x_1 - x_0)
\end{cases}$$

利用求根公式求出判別式 $\Delta = B^2 - 4AC$。若 $\Delta \ge 0$，求出實數根 $t = \frac{-B \pm \sqrt{\Delta}}{2A}$。篩選出落在區間 $(0, 1)$ 內部的合法根代入 $x(t)$ 求值，與端點 $x(0), x(1)$ 共同取極值，即可在 $O(1)$ 時間內以納秒級速度算出絕對精確的字形像素包圍盒！
---

## G.11 貝塞爾剪裁算法（Bézier Clipping）與高速幾何求交

在字體光柵化渲染、輪廓布爾運算（Boolean Union/Difference）以及輪廓重疊消除（Remove Overlap）中，兩段三次貝塞爾曲線 $\mathbf{P}(t)$ 與 $\mathbf{Q}(u)$ 的空間求交點是計算幾何中最昂貴的操作之一。

傳統牛頓迭代法由於高度依賴初始猜測值，在面對多交點或切觸點時極易發散。由西德伯格（Sederberg）與西村（Nishita）提出的 **貝塞爾剪裁算法（Bézier Clipping）**，以幾何凸包收縮代替純代數迭代，實現了超級穩定的超二次收斂速度：

### 算法幾何步驟：
1. **建立局部座標系**：連接曲線 $\mathbf{P}$ 的起點 $\mathbf{P}_0$ 與終點 $\mathbf{P}_3$ 構築基準絃線 $L$，計算每個控制點距直線 $L$ 的正負帶符號垂直距離 $d_0, d_1, d_2, d_3$；
2. **構建一維隱式距離函數**：構造一維距離函數 $d(t) = \sum_{i=0}^3 B_{i,3}(t) d_i$，其與橫軸的交點即爲曲線 $\mathbf{P}$ 與直線 $L$ 的交點；
3. **凸多邊形剪裁**：在參數平面 $(u, d)$ 上，繪製第二條曲線 $\mathbf{Q}(u)$ 關於距離軸的凸包，計算該凸包與 $d=0$ 軸相交的最小與最大參數區間 $[u_{\min}, u_{\max}]$；
4. **區間修剪**：將參數區間 $[0, 1]$ 瞬間裁剪縮小至 $[u_{\min}, u_{\max}]$。通過德卡斯特里奧算法截取子曲線，交替對兩曲線重複執行，通常僅需 3 至 4 輪迭代，交點參數即可收斂至浮點機極限精度（$10^{-12}$）！

---

## G.12 極式（Blossom）多線性公理的嚴密代數構造

爲了徹底理解極式 $p(u_1, u_2, \dots, u_n)$ 的數學本質，我們給出從單變量單項式基底向多線性對稱極式轉化的代數構造律：

對於任意單項式 $t^k$（其中 $0 \le k \le n$），其對應的 $n$ 元極式爲基本對稱多項式除以組合數：

$$\mathcal{B}[t^k] \, (u_1, u_2, \dots, u_n) = \frac{1}{\binom{n}{k}} \sum_{1 \le j_1 < j_2 < \dots < j_k \le n} u_{j_1} u_{j_2} \dots u_{j_k}$$

### 三次多項式極式展開全貌：
對於三次曲線 $\mathbf{P}(t) = \mathbf{a}_0 + \mathbf{a}_1 t + \mathbf{a}_2 t^2 + \mathbf{a}_3 t^3$，其關於三個獨立變量 $u_1, u_2, u_3$ 的唯一極式爲：

$$p(u_1, u_2, u_3) = \mathbf{a}_0 + \frac{\mathbf{a}_1}{3}(u_1 + u_2 + u_3) + \frac{\mathbf{a}_2}{3}(u_1 u_2 + u_2 u_3 + u_3 u_1) + \mathbf{a}_3 u_1 u_2 u_3$$

#### 代數檢驗：
1. **對稱性**：顯然，交換 $u_1, u_2, u_3$ 中任意兩者的次序，上式各項完全對稱不變；
2. **多重仿射性**：固定 $u_2, u_3$ 時，關於 $u_1$ 是形如 $A u_1 + B$ 的嚴格一次多項式；
3. **對角坍縮**：令 $u_1 = u_2 = u_3 = t$，有：
   $$p(t, t, t) = \mathbf{a}_0 + \frac{\mathbf{a}_1}{3}(3t) + \frac{\mathbf{a}_2}{3}(3t^2) + \mathbf{a}_3 t^3 = \mathbf{a}_0 + \mathbf{a}_1 t + \mathbf{a}_2 t^2 + \mathbf{a}_3 t^3 = \mathbf{P}(t)$$

極式理論的創立，不僅爲計算機字體幾何學提供了最堅固的代數奠基石，更將曲線微積分完全轉化爲優雅的多項式組合對稱學，成爲了全人類計算機圖形學與幾何設計皇冠上最璀璨的明珠。
---

## G.13 歐拉角螺線在現代排印工程學中的終極統一

在現代字型設計工具（如 FontForge 的 Spiro 模式與 Glyphs 的曲線平滑插件）中，歐拉螺線（Cornu Spiral）的工程實現基於拉夫·萊維恩的有限元求解器：
* 字體設計師只需在字母轉角處放置若干個離散錨點並指定端點切線；
* Spiro 引擎自動求解變分泛函最小化問題（Minimum Energy Curve）：
  $$E = \int \left( \frac{d\kappa}{ds} \right)^2 ds \longrightarrow \min$$
* 求解出的平滑螺線保證了全曲線的曲率導數能量極小化，再通過自適應德卡斯特里奧細分，自動導出符合 OpenType 規範的標準三次貝塞爾曲線，徹底消除了手工反覆調節控制點所帶來的微小視覺瑕疵！
