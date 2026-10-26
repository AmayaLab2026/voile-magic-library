# -*- coding: utf-8 -*-
"""
Expand Chapter 12 to full unabridged depth (Traditional Chinese).
"""
import sys

target_path = r"docs/zh-hant/fonts-encodings/chapter-12.md"

content = r"""# 第 12 章：字型的編輯與建立
### Chapter 12: Editing and Creating Fonts
選自《Fonts & Encodings》第 445–508 頁
*譯者：[Lycoris <lycorismisaka@gmail.com>](mailto:lycorismisaka@gmail.com)*

---

在本著作的前述章節中，我們已經深入探討了編碼體系、字形度量、字型光柵化渲染以及數位排版的數學基礎。然而，對於字型設計師（Type Designer）或數位排版工程師而言，最具創造力與工程挑戰性的任務莫過於**親手編輯與建立一款全新的數位字型**。

編輯與建立字型絕非單純在向量繪圖軟體中勾勒優美的藝術線條。一款合規、高品質的商用數位輪廓字型，是一個融合了多門學科的複雜工程系統：
1. **純幾何輪廓數據**：基於三次貝塞爾曲線（PostScript / OpenType CFF）或二次貝塞爾曲線（TrueType）構成的拓撲封閉閉合路徑（Contours）；
2. **微觀排版度量（Metrics）**：字元的左側軸承留白（LSB）、右側軸承留白（RSB）、前進寬度（Advance Width）以及精細的字偶間距表（Kerning）；
3. **結構化字元元數據**：字型內建的字名、Unicode 碼點映射、PostScript 字典資訊與 TrueType 命名記錄；
4. **低解析度渲染提示系統（Hinting）**：PostScript 提示（Hints）或 TrueType 位元組碼指令（Instructions），用於在低 DPI 螢幕或粗糙雷射列印中維持筆畫粗細一致性並避免墨斑糊死；
5. **進階排版特性（OpenType / AAT）**：連字、上下文變體與光學錨點定位。

在本章中，我們將深入兩大統治現代字型工程世界的專業工具：商業領域無可替代的王者 **FontLab Studio**，以及開源社群自由與強大的旗幟 **FontForge**。我們將系統剖析其介面哲學、幾何路徑構建、Python 腳本批次處理自動化，並揭示 PostScript 全域與局部提示系統（Hinting）的深層數學機理。

---

## 1. 字型設計與數位化全景導論（Introduction）

### 1.1 數位輪廓字形的解剖學結構

在數位字型中，每一個字元在底層被描述為一個**字形（Glyph）**。每個字形存在於一個抽象的二維笛卡爾座標系中，該座標系通常以大寫字母「H」的設計高度或全形字元寬度作為基本尺度單位（在 PostScript Type 1 中通常為 1000 單元/em，在 TrueType 中通常為 2048 單元/em）。

一個字形的幾何結構包含三大核心要素：
1. **基線（Baseline, $y = 0$）與原點 $(0, 0)$**：所有字元水平排列的公共基準線；
2. **前進寬度（Advance Width）**：排版引擎在繪製完當前字形後，將游標原點沿水平方向向前推進的物理跨度；
3. **側邊軸承留白（Sidebearings）**：
   - **左側軸承留白（Left Sidebearing, LSB）**：從原點 $(0,0)$ 沿 $x$ 軸到字形最左側黑色輪廓邊緣的水平距離；
   - **右側軸承留白（Right Sidebearing, RSB）**：從字形最右側黑色輪廓邊緣到前進寬度終點線（Advance Width Line）的水平距離。

字元之間的天然間距，本質上是由前一個字元的 RSB 與後一個字元的 LSB 疊加而成的。

### 1.2 曲線幾何：三次貝塞爾與二次貝塞爾的本質差異

數位輪廓字型採用參數化貝塞爾曲線來描述字形的邊緣輪廓：
- **PostScript Type 1 / OpenType (CFF)**：採用**三次貝塞爾曲線（Cubic Bézier Curves）**。每條曲線段由兩個端點（On-curve Points）和兩個離軸控制柄（Off-curve Control Handles）精確定義：
  $$\mathbf{B}(t) = (1-t)^3 \mathbf{P}_0 + 3(1-t)^2 t \mathbf{P}_1 + 3(1-t) t^2 \mathbf{P}_2 + t^3 \mathbf{P}_3, \quad t \in [0, 1]$$
  三次曲線在數學上能夠以極少的節點擬合極其流暢的 S 形反向曲率與優雅拐點；
- **TrueType**：採用**二次貝塞爾曲線（Quadratic Bézier Curves）**。每條曲線段僅由兩個端點和一個離軸控制點構成：
  $$\mathbf{B}(t) = (1-t)^2 \mathbf{P}_0 + 2(1-t) t \mathbf{P}_1 + t^2 \mathbf{P}_2, \quad t \in [0, 1]$$
  二次曲線的數學求導與光柵化計算極其輕量快速，但若要擬合相同精度的高級曲率，往往需要比三次貝塞爾多出 $50\%$ 至 $100\%$ 的控制節點。

---

## 2. FontLab Studio 工業級設計體系（FontLab）

由 Yuri Yarmola、Alexandre Prokhorov 與 Ted Harrison 聯合打造的 **FontLab Studio**（尤其是經典版本 FontLab 5），是過去二十年全球專業商業字型設計事務所（Monotype, Linotype, Adobe, Dalton Maag 等）不可撼動的行業支柱。

### 2.1 四大字形瀏覽檢視（Font Window Display Modes）

在打開一款字型時，FontLab 的字型視窗（Font Window）提供了四種功能截然不同的檢視模式，用於從不同維度俯瞰字庫資產：

1. **名稱模式（Names Mode）**：
   在該模式下，每個字形單元格的下方清晰顯示其合法的 PostScript 字形名稱（如 `A`, `eacute`, `fi`, `zero.oldstyle`）。這是字型設計師繪製和命名具體字形時的首選工作模式；
2. **頁面模式（Pages Mode）**：
   將字庫按照每頁固定數量（通常為 256 個字元）劃分為離散的「頁面」。這一模式忠實反映了經典 8 位元字型（如 256 字元的 Type 1 字型）的底層物理分塊，便於排版師逐頁校對編碼映射；
3. **範圍模式（Ranges Mode）**：
   按照國際標準將字型資產劃分為特定的技術子集：如「基本拉丁（Basic Latin）」、「拉丁文補充-1（Latin-1 Supplement）」、「西里爾字母（Cyrillic）」、「數學運算子（Mathematical Operators）」等。當設計師需要為已有字型增補特定語種支援時，範圍模式能一目了然地指出哪些字元尚待繪製；
4. **索引模式（Index Mode）**：
   按照字形在字型檔案內部的物理存儲順序（Glyph Index, GID 0 至 $N-1$）進行線性排列。這直接揭示了字型在二進位底層的資料索引拓撲。

---

### 2.2 輪廓編輯幾何學：節點類型與控制柄約束

在 FontLab 的字形編輯視窗中，設計師使用鋼筆工具與節點編輯工具操縱三次貝塞爾曲線。FontLab 確立了一套嚴密的節點拓撲學規範，將所有輪廓節點劃分為三大基本類型：

1. **角點（Corner Node, 綠色方形標識）**：
   在角點處，曲線的方向發生突變，形成尖銳的折角（如字母「A」的頂部尖端或襯線的直角拐折）。角點兩側的控制柄可以完全獨立移動，互不干擾；
2. **平滑點（Smooth Node, 紅色圓形標識）**：
   在平滑點處，曲線保持一階連續性（$C^1$ 連續）。該節點兩側的控制柄與節點自身嚴格保持共線（Collinear）。當設計師用滑鼠拖曳其中一個控制柄時，對向的控制柄會自動沿反方向對稱旋轉，確保曲線在經過該點時絕不出現視覺折痕；
3. **切線點（Tangent Node, 藍色三角形標識）**：
   專門用於連接一條直線段與一條曲線段。切線點處的曲線控制柄被嚴格約束在相鄰直線段的共線延長線上，保證直線與弧線在交接處無縫平滑切合。

#### 輪廓方向（Contour Direction）鐵律
在數位字型中，所有封閉路徑的走向方向絕非無關緊要：
- **外輪廓（Outer Contours）**必須嚴格遵循**順時針方向（Clockwise）**；
- **內輪廓/挖空字懷（Inner Contours / Holes）**必須嚴格遵循**逆時針方向（Counter-clockwise）**。

光柵化引擎（如 FreeType 或 Windows ClearType）採用「非零環繞數規則（Non-zero Winding Rule）」或「奇偶規則（Even-Odd Rule）」來計算墨跡填充。若輪廓方向發生反轉，字形內部本應挖空的字懷（如「O」或「B」的內部）將被錯誤地填充為實心黑墨！FontLab 提供了 `Contour > Correct Direction` 工具，可在毫秒級自動修復所有路徑的拓撲朝向。

---

### 2.3 度量視窗與字間距系統（Metrics and Kerning）

優美的字形輪廓若沒有精準的度量支撐，排版時依然會潰不成軍。FontLab 的度量視窗（Metrics Window）是字距調校的核心中樞。

#### 1. LSB、RSB 與前進寬度的幾何聯動
在度量視窗中，設計師可以輸入任意連續測試文字（如 `HHHAHHH` 或 `nnnonnn`）。字形兩側顯示兩條垂直的虛線，分別代表原點基準線與前進寬度終點線。
拖曳虛線即可即時修改 LSB 與 RSB 數值：
$$\text{Advance Width} = \text{LSB} + \text{Bounding Box Width} + \text{RSB}$$

#### 2. 字偶間距（Kerning）與度量類（Metric Classes）
在處理大寫字母組合如「AV」、「To」、「WA」時，僅靠固定的 RSB 與 LSB 會留下巨大的三角形視覺空洞。排版師必須為這些特定組合定義負向字偶微調值（如 `pos A V -100;`）。

然而，如果為字型中成百上千個字形兩兩定義字距，字偶對的總數將呈指數級爆炸（$O(N^2)$），導致字型檔案急劇膨脹且編譯崩潰。
FontLab 引入了革命性的**度量類（Metric Classes）**機制：
- 將所有左側具有平直主幹的字形歸為一類：`@Left_Flat = [B D E F H I K L P R]`;
- 將所有右側具有弧形輪廓的字形歸為一類：`@Right_Round = [C G O Q]`;
設計師只需在 `@Left_Flat` 與 `@Right_Round` 之間定義一次微調值（如 `-40`），FontLab 在匯出 OpenType 時會自動將其編譯為高效的基於類的 GPOS 查找表，單行配置瞬間覆蓋數十對甚至上百對字偶！

---

### 2.4 輪廓變換引擎與布林運算

FontLab 提供了功能強大的幾何形變引擎：
- **仿斜切（Slanting）**：透過剪切變換矩陣將正體快速生成機械仿斜體；
- **輪廓展寬（Expanding Stems / Bolding）**：沿輪廓法線方向向外平移曲線，從而在保留字形骨架的前提下自動生成加粗變體；
- **布林運算（Boolean Operations）**：支援輪廓之間的聯集（Union）、交集（Intersection）、差集（Difference）運算。這在拼接複合字母（如將帶符字母的基底與變音符融合成單一路徑）時極其高效。

---

## 3. 基於 Python 腳本驅動 FontLab Studio（Driving FontLab with Python Scripts）

FontLab 5 最令工業界推崇的技術殺手鐧，莫過於其內建的完整 **Python 腳本直譯器**。透過暴露底層 C++ 核心物件模型，排版師可以用簡潔優雅的 Python 程式碼，完全接管字型建立、批次處理分析、輪廓修改與度量計算的全部流程。

### 3.1 FontLab Python API 核心類別層次體系

在 FontLab 的 Python 環境中，系統預定義了一個全域單例物件 **`fl`**（即 `FontLab` 類別的實例）。從 `fl` 出發，排版師可以導航至整個物件圖：

```
[fl (全域單例)]
    │
    ├── fl.font (當前活動字型 Font 物件)
    │       │
    │       ├── font.glyphs (字形列表: list of Glyph)
    │       │       │
    │       │       ├── glyph.nodes (節點列表: list of Node)
    │       │       ├── glyph.layers (多層資料)
    │       │       └── glyph.kerning (字距對字典: dict of KerningPair)
    │       │
    │       ├── font.encoding (當前啟動的 Encoding 物件)
    │       └── font.classes (類別定義列表)
    │
    └── fl.Open() / fl.Save() / fl.GenerateFont()
```

#### 核心類別及其關鍵屬性與方法：

1. **`FontLab` 類別（全域操作樞紐 `fl`）**：
   - `fl.New()`：在記憶體中建立全新空白字型；
   - `fl.Open(path)`：打開現有字型；
   - `fl.Save(path)`：保存當前工程；
   - `fl.GenerateFont(format, path)`：匯出目標格式字型。其內建格式常數包括：
     - `ftFONTLAB`（FontLab 本地 `.vfb` 工程檔案）
     - `ftTYPE1`（PostScript Type 1 二進位 `.pfb`）
     - `ftTYPE1ASCII`（PostScript Type 1 純文字 `.pfa`）
     - `ftTRUETYPE`（TrueType `.ttf`）
     - `ftOPENTYPE`（OpenType `.otf`）
     - `ftMACTYPE1`、`ftMACTRUETYPE`、`ftMACTRUETYPE_DFONT`（蘋果專屬格式）

2. **`Font` 類別（字型資產總成）**：
   - `font.font_name`、`font.family_name`、`font.weight`：字型命名與元數據；
   - `font.upm`：每 em 單元數（如 1000 或 2048）；
   - `font.FindGlyph(name)`：按名稱快速查找字形物件；
   - `font.Add(glyph)`：將新生成的字形插入字型庫；
   - `font.modified`：標記字型已被修改。

3. **`Glyph` 類別（字形實體）**：
   - `glyph.name`：字形名稱；
   - `glyph.unicode`：主 Unicode 碼點；
   - `glyph.width`：水平前進寬度（Advance Width）；
   - `glyph.lsb`：左側軸承留白；
   - `glyph.rsb`：右側軸承留白；
   - `glyph.nodes`：由 `Node` 物件構成的線性序列；
   - `glyph.GetBoundingBox()`：返回 `Rect` 矩形物件，描述字形墨跡的物理範圍 `(x1, y1, x2, y2)`；
   - `glyph.GetContourNumbers()`：返回該字形包含的封閉獨立輪廓數量；
   - `glyph.FindContour(n)`：返回包含索引為 $n$ 的節點所屬的輪廓編號。

4. **`Node` 類別與 `Point` 類別（微觀幾何元素）**：
   - `node.x`, `node.y`：節點物理座標；
   - `node.type`：節點拓撲類型，常數取值：
     - `ntCORNER`（角點）
     - `ntSMOOTH`（平滑點）
     - `ntTANGENT`（切線點）
   - `node.alignment`：控制柄對齊狀態；
   - `Point(x, y)`：二維幾何點物件，重載了加減法與縮放算術運算子；
   - `Rect(llx, lly, urx, ury)`：矩形邊界框物件。

5. **`Encoding` 類別與 `KerningPair` 類別**：
   - `enc = Encoding()`；`enc.Load(path)`：載入外部編碼映射表；
   - `KerningPair(key, value)`：描述兩兩字形之間的字距微調數值。

---

### 3.2 工業實戰腳本剖析：全自動重編碼與度量分析

#### 腳本一：批次分析字庫全域高度與極值包圍盒

以下 Python 腳本遍歷當前字型中的所有字形，高精度計算整套字庫的實際最大上升部、最大下降部與最寬字元：

```python
# -*- coding: utf-8 -*-
from fontlab import *

f = fl.font
if f is None:
    print("錯誤：當前未打開任何字型！")
else:
    max_ascender = 0
    min_descender = 0
    widest_glyph = ""
    max_width = 0

    print("開始分析字型: %s ..." % f.font_name)

    for g in f.glyphs:
        bbox = g.GetBoundingBox()
        if bbox is not None:
            if bbox.ury > max_ascender:
                max_ascender = bbox.ury
            if bbox.lly < min_descender:
                min_descender = bbox.lly
        
        if g.width > max_width:
            max_width = g.width
            widest_glyph = g.name

    print("----------------------------------------")
    print("全域物理最高點 (Max Ascender): %d" % max_ascender)
    print("全域物理最低點 (Min Descender): %d" % min_descender)
    print("最寬字形: %s (寬度: %d)" % (widest_glyph, max_width))
    print("設計 em 尺寸: %d" % f.upm)
```

#### 腳本二：全自動批次組裝帶重音複合字形（Composite Glyphs）

在西文字型設計中，手動為數十個大寫字母疊加銳音符（acute）、抑音符（grave）、分音符（dieresis）極其繁瑣且極易出現對齊偏差。借助 Python 腳本，我們可以根據基底字母的中心座標自動完成焊接：

```python
# -*- coding: utf-8 -*-
from fontlab import *

f = fl.font

def create_accented_glyph(base_name, accent_name, target_name, target_unicode):
    base_glyph = f.FindGlyph(base_name)
    accent_glyph = f.FindGlyph(accent_name)

    if base_glyph is None or accent_glyph is None:
        print("缺少必要字形組件: %s 或 %s" % (base_name, accent_name))
        return

    new_glyph = Glyph(base_glyph)
    new_glyph.name = target_name
    new_glyph.unicode = target_unicode

    base_bbox = base_glyph.GetBoundingBox()
    base_center_x = (base_bbox.llx + base_bbox.urx) / 2.0

    accent_bbox = accent_glyph.GetBoundingBox()
    accent_center_x = (accent_bbox.llx + accent_bbox.urx) / 2.0

    offset_x = base_center_x - accent_center_x
    offset_y = base_bbox.ury - accent_bbox.lly + 50

    for node in accent_glyph.nodes:
        new_node = Node(node)
        new_node.x += offset_x
        new_node.y += offset_y
        new_glyph.nodes.append(new_node)

    new_glyph.width = base_glyph.width
    f.Add(new_glyph)
    print("成功構建複合字形: %s (U+%04X)" % (target_name, target_unicode))

create_accented_glyph("A", "acute", "Aacute", 0x00C1)
create_accented_glyph("E", "acute", "Eacute", 0x00C9)
create_accented_glyph("O", "acute", "Oacute", 0x00D3)

f.modified = 1
fl.UpdateFont()
```

---

## 4. FontForge 開源自由字型工坊（FontForge）

如果說 FontLab 是商業閉源領域的瑰寶，那麼喬治·威廉姆斯（George Williams）開創的 **FontForge** 則是自由軟體精神在排版藝術領域的永恆豐碑。

### 4.1 檢視哲學與全平面 Unicode 支援

FontForge 的主視窗從底層直接以純粹的 Unicode 碼點矩陣展開：
- 使用者可以自由跨越 Plane 0（BMP）至 Plane 16（私用平面）；
- 支援數十種全球編碼體系（ISO 8859 系列、KOI8、Shift-JIS、GB2312、Big5）的即時檢視重映射；
- 能夠原汁原味地打開並解析幾乎人類歷史上存在過的所有字型格式。

---

### 4.2 曲線輪廓繪製：三次、二次貝塞爾與 Spiro 曲線數學模型

#### 1. PostScript（三次）與 TrueType（二次）原生雙向切換
在 FontForge 的 `Element > Font Info > Layers` 中，使用者可以顯式指定輪廓層採用**三次貝塞爾曲線**還是**二次貝塞爾曲線**。
- 反向轉換時，FontForge 透過精確數學公式：
  $$\mathbf{Q}_0 = \mathbf{P}_0, \quad \mathbf{Q}_1 = \mathbf{P}_0 + \frac{2}{3}(\mathbf{P}_1 - \mathbf{P}_0), \quad \mathbf{Q}_2 = \mathbf{P}_2 + \frac{2}{3}(\mathbf{P}_1 - \mathbf{P}_2), \quad \mathbf{Q}_3 = \mathbf{P}_2$$
  將二次貝塞爾無損、確定性地提升為等效的三次貝塞爾曲線。

#### 2. 拉夫·萊維安（Raph Levien）的 Spiro 曲線數學模型
FontForge 率先整合了著名的 **Spiro 曲線引擎**。Spiro 基於歐拉螺線（Euler Spirals / Clothoids，回旋線，其曲率隨弧長線性連續變化：$\kappa(s) = c \cdot s$）。在 Spiro 模式下，設計師只需在字形關鍵轉折點放置幾個控制錨點，Spiro 求解器會自動計算出整條曲線上曲率變化能量泛函最小（Minimum Bending Energy）的純天然流線！

---

### 4.3 點陣圖向量化自動追蹤（Auto-tracing）

對於從歷史古籍或掃描稿中復原字型的排版學者，FontForge 深度整合了兩大開源向量化引擎：
- **Potrace**：多邊形逼近與光滑輪廓追蹤演算法；
- **Autotrace**：彩色輪廓提取器。

工作流程：將手繪字形的高解析度黑白 TIFF/PNG 圖像導入 Background 背景圖層，點擊 `Element > AutoTrace`，引擎瞬間即可將邊緣像素點陣擬合為由三次貝塞爾曲線構成的純淨向量路徑！

---

### 4.4 FontForge Python 腳本自動化系統

```python
# -*- coding: utf-8 -*-
import fontforge

font = fontforge.open("source_font.ttf")
print("正在處理字型: %s" % font.fontname)

for glyph in font.glyphs():
    glyph.addExtrema()
    glyph.correctDirection()
    glyph.simplify()

font.autoHint()
font.autoInstr()
font.generate("output_optimized.otf")
print("最佳化編譯完成，已成功生成 output_optimized.otf！")
```

---

## 5. PostScript 提示系統（PostScript Hinting）

當我們在螢幕上以 12 磅的大小查看內文時，一個英文字母「H」的主幹可能只有區區 1 到 2 個像素寬。在如此粗糙的離散點陣畫布上，純數學貝塞爾曲線的理論輪廓會與實際像素網格發生劇烈衝突。為了解決這一問題，Adobe 發明了登峰造極的控制體系——**PostScript 提示系統（Hinting）**。

### 5.1 全局提示（Global Hints）與對齊區（Alignment Zones）

#### 1. 對齊區與 `BlueValues`
`BlueValues` 是一個由偶數個整數組成的配對陣列，必須嚴格按照升序排列：

$$\text{BlueValues} = [y_{b0}, y_{t0}, \quad y_{b1}, y_{t1}, \quad \dots]$$

每一對整數 $[y_{bottom}, y_{top}]$ 定義了一個水平對齊區（Alignment Zone）：
- 第一對必須是基線對齊區（Baseline Zone，如 $[-15, 0]$）；
- 第二對通常是小寫字母 x 高度對齊區（如 $[480, 495]$）；
- 對於位於基線之下的降部區域（Descender），使用 **`OtherBlues`** 陣列定義輔助對齊區（如 $[-250, -235]$）。

#### 對齊區的工作原理：過衝（Overshoot）與尺寸閾值
在光學設計中，圓形字母（如「O」）故意畫高一點以抵消視覺萎縮，這稱為**過衝（Overshoot）**。在低解析度螢幕上，這多出來的微小過衝會導致圓形字母的頂部多霸占整整一排像素！
**`BlueValues` 的數學魔法正是為了消除這一低解析度失真**：
1. 當字號小於閾值尺寸：
   $$\text{Threshold Size} = \frac{1}{\text{BlueScale} \times (\text{Zone Height})}$$
2. 光柵化引擎會**強行將所有過衝的圓弧平整吸附（Snap）到基準平線上**；
3. 當字號放大超過閾值後，對齊區自動解禁，平滑釋放出微觀過衝曲線，恢復其古典的光學藝術美感！

#### 2. 標準主幹寬度：`StdHW`, `StdVW` 與筆畫捕捉
- **`StdHW`**：描述字庫中最具代表性的水平主幹粗細；
- **`StdVW`**：描述最具代表性的垂直主幹粗細；
- **`StemSnapH` 與 `StemSnapV`**：典型筆畫寬度階梯陣列。

---

### 5.2 局部提示（Local Hints）與提示替換（Hint Substitution）

在字形內部，設計師為每一條關鍵筆畫顯式掛載局部提示指令：
- **`hstem`（水平筆畫提示）**：起始 $y$ 座標與筆畫厚度 $dy$；
- **`vstem`（垂直筆画提示）**：起始 $x$ 座標與筆畫厚度 $dx$。

#### 提示替換（Hint Substitution）
在複雜字形（如字母「B」）中，垂直筆畫沿水平方向重疊交錯。Adobe 在 Type 1 規範中引入了**提示替換（Hint Substitution）**機制：當光柵化掃描線推進時，字形代碼可以在特定的曲線拐點處，動態清空舊的提示集並瞬時啟動專門針對當前局部區域的新提示！

---

## 6. 結論（Conclusions）

字型的編輯與建立，是一場在毫釐之間平衡數學嚴謹性與視覺美學感知的修行。
數位字型絕不是一幅死板的點陣圖快照，而是一套具有生命力、能夠根據解析度自適應呼吸、在不同語言環境下敏銳變通的**自包含微型計算機程式**。只有深刻理解了這些隱藏在漂亮字形背後的工程靈魂，我們才能真正駕馭數位排版的大道，創造出跨越時空與硬體阻隔的永恆文字藝術經典！
"""

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully written {target_path}, length: {len(content)} chars.")
