---
title: 第十章：Web 網頁排版與網絡字體技術
description: HTML/CSS 字體模塊規範（CSS Fonts 1/2/3）、@font-face 規則與字體匹配算法、動態網絡字體歷史演進（TrueDoc PFR、WEFT EOT、GlyphGate）與 SVG 矢量字體規範全景技術解析
---

# 第 10 章：Web 網頁排版與網絡字體技術

*譯者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

當蒂姆·伯納斯-李（Tim Berners-Lee）在 1989 至 1990 年間於歐洲核子研究組織（CERN）發明超文本傳輸協議（HTTP）與超文本標記語言（HTML）時，他絕不可能預見到二十餘年後，“.com”將席捲整個人類文明的每一個角落。萬維網（World Wide Web）的爆發式擴張無疑是 20 世紀末人類科技史上的最高光事件之一。

然而，在萬維網誕生的前十年裏，**網頁的排版與字體渲染能力極其簡陋貧瘠**。早期互聯網主要面向高能物理學家與學術科研人員，網絡傳輸的核心目標是純學術文本與數據報告的快速共享，視覺美感與高精度印刷級排版從未被納入核心議程。然而，隨着網景瀏覽器（Netscape Navigator）與微軟 Internet Explorer 的激烈商業競爭，數十億普通用戶湧入互聯網，數以百萬計的商業網站、數字出版物、在線新聞媒體對“在瀏覽器中呈現與專業印刷紙媒同等優雅的字體”爆發出了前所未有的迫切渴望。

在本章中，我們將系統考察萬維網技術演進中字體排版的波瀾壯闊歷程：
1. **(X)HTML 與級聯樣式表（CSS）的字體模型**：從簡陋的 HTML 物理標籤到 CSS Fonts 規範（CSS 1, CSS 2/2.1, CSS 3）、字體匹配算法以及 `@font-face` 跨網絡字體裝載機制；
2. **早期網絡字體下載與嵌入式格式的血淚先驅**：深入剖析 Bitstream 公司的 **TrueDoc（PFR 格式）**、微軟公司的 **WEFT 與嵌入式 OpenType（EOT 格式）**，以及 em2 Solutions 公司的 **GlyphGate** 動態字形服務器；
3. **SVG（可縮放矢量圖形）與 SVG 字體體系**：從 XML 語法底層到 SVG 字體架構，全面解析 `<font>`、`<font-face>`、`<glyph>`、`<hkern>` 以及字形輪廓路徑的幾何規範。

---

## 1. (X)HTML、CSS 與字體規範演進

### 1.1 原始 HTML 字體標籤的致命困境

在級聯樣式表（CSS）誕生之前，網頁作者控制字體的唯一手段是依靠早期的 HTML 物理標籤，其中最具代表性的是網景在 HTML 3.2 時代引入的 `<font>` 標籤：
```html
<p>
  <font face="Verdana, Arial, Helvetica" size="3" color="#333333">
    这是一段早期 Web 文本。
  </font>
</p>
```
配合全局的 `<basefont face="..." size="...">`，網頁設計者試圖以硬編碼的方式指定渲染字體。然而，這種早期的原始機制給 Web 生態帶來了三項致命的災難性後果：
1. **語義與表現的徹底混雜**：HTML 應當忠實描述文檔的邏輯結構（標題、段落、引用、列表），而 `<font>` 標籤將大量純視覺樣式的雜亂代碼注入文檔正文，導致 HTML 體積膨脹數倍，網頁解析極其低效；
2. **本地字體依賴的“囚徒困境”**：`face` 屬性所列出的字體名稱，必須**完全預先物理安裝在終端訪問者的本地操作系統中**。如果作者在其豪華的工作站上使用了精美的經典襯線體（如 Garamond 或 Bembo），而訪問者的普通家庭電腦上只安裝了 Times New Roman，瀏覽器就會退化爲最粗糙的默認字體，導致網頁版面瞬間錯位崩塌；
3. **印刷度量與像素顯示的斷層**：HTML 的 `size="1"` 到 `size="7"` 僅爲相對標度，完全缺乏排版學中所必需的磅值（pt）、字寬（Set-width）、字重（Weight）以及行距（Leading）的數學定義。

爲終結這種混亂局面，萬維網聯盟（W3C）於 1996 年底正式發佈了 CSS 1 規範，隨後在 CSS 2 與 CSS 3 中確立了現代 Web 字體的黃金架構。

---

## 2. CSS 字體屬性全景規範（CSS Fonts Module）

CSS 將字體屬性高度抽象爲一組正交、獨立的樣式描述符（Font Descriptors）。理解每個屬性的底層機理與物理單位，是掌握現代 Web 排版的核心前提。

### 2.1 核心字體屬性全覽

#### 1. `font-family`（字體家族）
`font-family` 允許聲明一個按優先級由高到低排列的字體備選列表（Fallback Font List）：
```css
body {
  font-family: "Helvetica Neue", Helvetica, Arial, sans-serif;
}
```
瀏覽器在解析該列表時，會逐字檢測當前需要渲染的字符碼位是否存在於第一個字體中；如果第一個字體缺失該字符的字形（例如用英文字體渲染中文字符），瀏覽器會自動跳轉至下一個字體繼續檢索，直到找到可用的字形爲止。

爲了保證在一切極端情況下頁面文字均可正常閱讀，W3C 規範強制規定了 **5 種通用字體族名（Generic Font Families）**，作爲字體列表的最終兜底保底項：
- `serif`（襯線體）：字形筆畫末端帶有裝飾性襯線（如 Times New Roman, Georgia, 宋體）；
- `sans-serif`（無襯線體）：筆畫粗細均勻、末端無裝飾平直切口（如 Arial, Helvetica, Verdana, 微軟雅黑, 黑體）；
- `monospace`（等寬字體）：所有字符具有完全恆定的固定進深寬度，常用於代碼展示（如 Courier New, Consolas, Monaco）；
- `cursive`（手寫/草書體）：具有連筆手寫風格、模仿墨水毛筆的字形（如 Comic Sans MS, Zapf Chancery）；
- `fantasy`（裝飾/花體）：藝術化變體字體，常用於海報標題（如 Impact, Papyrus）。

#### 2. `font-style`（字形姿態）
用於控制字體的直立或傾斜表現：
- `normal`：標準直立正體（Roman）；
- `italic`：專門設計的**意大利斜體（True Italic）**。在西文正統字體學中，Italic 不僅具有傾斜度，其字母結構（尤其是小寫字母 `a`, `f`, `g`）往往採用類似手寫體的連筆草體形態；
- `oblique`：**算法機械傾斜體（Fake / Slanted Italic）**。排版引擎直接通過對直立正體的輪廓實施仿射剪切矩陣變換（Shearing）生成的假斜體。

#### 3. `font-variant`（字母變體）
- `normal`：默認常規字形；
- `small-caps`：**小型大寫字母（Small Capitals）**。排版引擎使用與小寫字母 x-高度相當的高度來渲染大寫字母形態。在專業 OpenType 字體中，真實的 Small Caps 具備加粗的主莖寬度，以避免機械縮小產生筆畫過於細弱的光學缺陷。

#### 4. `font-weight`（字重與黑度）
用於控制筆畫的視覺粗細。CSS 引入了九級標準化絕對數值體系：
- 離散整百數值：`100`（Thin / Hairline）、`200`（Extra Light）、`300`（Light）、`400`（Normal / Regular）、`500`（Medium）、`600`（Semi Bold）、`700`（Bold）、`800`（Extra Bold）、`900`（Black / Heavy）；
- 相對關鍵字：`bolder`（在當前繼承值基礎上向更重一級躍升）與 `lighter`（向更輕一級衰減）。

#### 5. `font-stretch`（字體展寬比例）
定義字符水平方向的壓縮或擴展程度：
- `normal`（100% 原始寬度）；
- 緊縮系列：`ultra-condensed` (50%)、`extra-condensed` (62.5%)、`condensed` (75%)、`semi-condensed` (87.5%)；
- 擴展系列：`semi-expanded` (112.5%)、`expanded` (125%)、`extra-expanded` (150%)、`ultra-expanded` (200%)。

#### 6. `font-size`（字號尺寸與度量單位）
- **絕對關鍵字**：基於七級比例階梯構建：`xx-small`, `x-small`, `small`, `medium`（基準默認值，通常爲 16px）, `large`, `x-large`, `xx-large`；
- **相對關鍵字**：`smaller`, `larger`；
- **物理與屏幕長度單位**：
  - `px`（CSS 像素）：屏幕顯示最穩定的絕對參考單位；
  - `pt`（印刷磅）：$1 \ pt = 1/72 \ in$，常用於打印樣式表（Print Stylesheet）；
  - `em`：相對於當前元素的父級 `font-size` 的比例值（如 `1.5em` 表示當前字號的 1.5 倍）；
  - `rem`（Root EM）：相對於文檔根節點 `<html>` 的字號比例，避免了多層嵌套時 `em` 的雪崩式乘法縮放；
  - `ex`：相對於當前字體小寫字母 `x` 的實際物理高度（x-height）。

---


#### 7. PANOSE-1 分類學體系與 `@font-face` 物理描述符
在高端排版與智能字體匹配中，僅靠字形名稱與粗略字重遠遠不夠。CSS 規範深度吸收了惠普（Hewlett-Packard）公司研發的 **PANOSE-1 字體分類編碼體系**。PANOSE-1 是一個由 10 個離散十進制十進制數字構成的特徵指紋數組：
```css
@font-face {
  font-family: "MyClassicSerif";
  src: url("classic-serif.woff2") format("woff2");
  panose-1: 2 4 6 3 5 4 5 2 3 4;
}
```
這 10 個數字在排版學上分別代表：
1. `Family Kind`（字體大類：2 爲拉丁正文字體，3 爲拉丁手寫體，4 爲裝飾字體，5 爲等寬字）；
2. `Serif Style`（襯線形態：小三角、直角、平頭、凹陷、圓形襯線等）；
3. `Weight`（字重量級：極細至極黑）；
4. `Proportion`（長寬比例：現代、古典、展開、緊縮）；
5. `Contrast`（主副筆畫粗細對比度）；
6. `Stroke Variation`（筆畫過渡漸變平緩度）；
7. `Arm Style`（字干與字臂裝飾角形態）；
8. `Letterform`（字母字身幾何輪廓構造：直立、手寫、斜角）；
9. `Midline`（橫畫中線位置與 x-高度視覺相對關係）；
10. `X-height`（x-高度佔整個字身方格的離散相對比例）。

當聲明瞭 `panose-1` 指紋後，瀏覽器能夠在本地備選字體庫中計算各字體的 **PANOSE 加權歐式幾何距離**，從而在降級替換時精準挑選中視覺風格、筆畫粗細對比度與原字最接近的替代字體。

#### 8. `unicode-range` 的三種語法範式與字體按需切片
`unicode-range` 是實現現代 Web 字體按需分片（Font Splitting）的基石。它支持三種精確的聲明語法：
1. **單碼位指定**：`unicode-range: U+26;`（僅匹配 `&` 符號）；
2. **閉區間範圍指定**：`unicode-range: U+0020-007F;`（精確覆蓋基本 ASCII 字符區）；
3. **問號通配符範圍（Wildcard Range）**：`unicode-range: U+4??;`（問號匹配十六進制任意一位，即匹配 `U+0400` 至 `U+04FF`，完整覆蓋西裏爾字母全區）。

通過在樣式表中聲明多個同名但擁有不同 `unicode-range` 的 `@font-face` 規則，瀏覽器能夠實現**多語言混合智能按需分流**：渲染英文字符時僅下載 15KB 的西文子集；當頁面出現俄文時僅增量下載 20KB 的西里爾子集；當出現漢字時才觸發東亞大子集的異步加載。

### 2.2 `font-size-adjust`：x-高度微調與光學可讀性自適應

在 Web 字體排版中，最令排版設計師感到困惑的問題之一是：**爲什麼在相同的 `font-size: 16px` 下，不同字體的肉眼可讀性與字形大小感會有天壤之別？**

![不同字體的 x-高度比例對比](/images/fonts-encodings/fig10-1.png)
*圖 10-1：數款典型字體的 x-高度比例（小寫字母高度與字身字號的比率）對比。自上而下：Times New Roman、Verdana、Georgia 等。*

#### 寬高比值（Aspect Value）的數學定義
這一視覺差異的根源在於**字體的 x-高度（x-height）佔總字身尺寸（Font Size）的比例**，CSS 規範將其形式化定義爲字體的**寬高比值（Aspect Value，記爲 $a$）**：

$$a = \frac{\text{x-height}}{\text{font-size}}$$

- **高 Aspect 值字體**：例如微軟專門爲低分辨率 CRT/LCD 屏幕設計的 Verdana（$a \approx 0.58$）與 Georgia（$a \approx 0.50$）。其小寫字母高大豐滿，即使在 10px 極小字號下，字母內部的空腔（Counter）依然清晰可見；
- **低 Aspect 值字體**：例如經典金屬活字傳統的 Times New Roman（$a \approx 0.46$）。其專爲高密度印刷紙張設計，小寫字母相對低矮，在低分辨率屏幕上小字號渲染時，筆畫往往極易粘連成團。

#### 降級替換時的文本崩塌
假設網頁主標題設計爲 Verdana 字體，字號設定爲 12px。如果訪問者的系統中沒有 Verdana，瀏覽器自動降級使用備選的 Times New Roman。由於 Times 的 x-高度僅爲 0.46，原本在 Verdana 下清晰可讀的正文在切換爲 Times 後，小寫字母尺寸驟降，文本頓時變得模糊難辨，整體段落灰度嚴重破壞。

#### 補償修正公式
爲解決這一問題，CSS 引入了 `font-size-adjust` 屬性：
```css
p {
  font-family: Verdana, "Times New Roman", serif;
  font-size: 14px;
  font-size-adjust: 0.58; /* 锁定目标 Verdana 的宽高比 */
}
```
當瀏覽器發生字體降級時，它會讀取實際調用的備選字體自身的寬高比 $a'$，並根據以下數學公式**動態調整備選字體的實際計算字號 $c$**：

$$c = \left(\frac{a}{a'}\right) \times s$$

其中 $s$ 爲原始聲明的 `font-size`。
- 如果備選字體是 Times New Roman（$a' = 0.46$），其實際渲染字號將自動補償放大爲：
  $$c = \left(\frac{0.58}{0.46}\right) \times 14 \approx 1.26 \times 14 \approx 17.65 \ px$$
- 這一放大完美抵消了字體本身小寫字母低矮的缺陷，確保無論備選字體如何切換，頁面正文小寫字母的絕對視覺高度恆定保持在 $14 \times 0.58 = 8.12 \ px$，極大地捍衛了跨平臺跨字體的閱讀舒適度。

---

### 2.3 複合屬性 `font` 的簡寫語法法則

CSS 提供了 `font` 簡寫屬性，允許在一行內定義全部核心樣式：
```css
/* 语法规范模板 */
font: [font-style || font-variant || font-weight || font-stretch]? font-size [/ line-height]? font-family;
```

**書寫規則約束**：
1. `font-size` 與 `font-family` 是**絕對強制必填項**，省略任何一個均會導致整個 `font` 聲明完全作廢；
2. 如果包含 `line-height`（行高），必須緊跟在 `font-size` 之後，並以正斜槓 `/` 分隔（如 `16px/1.5`）；
3. 前置修飾詞（`font-style`, `font-variant`, `font-weight`, `font-stretch`）可以以任意順序書寫，未聲明的屬性將自動恢復爲其初始默認值（`normal`）；
4. `font` 屬性還允許直接借用操作系統的系統主題字體關鍵字：`caption`, `icon`, `menu`, `message-box`, `small-caption`, `status-bar`。

---

### 2.4 CSS 字體匹配算法（Font Matching Algorithm）

當瀏覽器遍歷 DOM 樹渲染文本時，它會爲每一個字符執行一套高度嚴密的 **6 步字體匹配算法**：

```
+-------------------------------------------------------------+
| Step 1: 构建本地及网络字体描述数据库 (Font Database)           |
| * 收集系统物理字体、本地安装字体及所有已激活的 @font-face 规则 |
+------------------------------|------------------------------+
                               v
+-------------------------------------------------------------+
| Step 2: 逐元素提取计算样式 (Computed Styles)                 |
| * 确定 font-family 列表、stretch, style, weight, size 等绝对值|
+------------------------------|------------------------------+
                               v
+-------------------------------------------------------------+
| Step 3: 按优先级线性匹配 font-family 家族名称                |
| * 遍历家族名；若完全不命中，回退至 generic font family       |
+------------------------------|------------------------------+
                               v
+-------------------------------------------------------------+
| Step 4: 多维属性模糊度量距离逼近 (Descriptive Matching)     |
| * 优先级顺序: 1. font-stretch -> 2. style -> 3. weight      |
+------------------------------|------------------------------+
                               v
+-------------------------------------------------------------+
| Step 5: 逐字符码位覆盖性验证 (Glyph Coverage Check)          |
| * 检查命中的字体实例是否真正包含目标字符的字形 (Glyph)       |
| * 若包含则调用渲染；若缺失则保持当前属性回跳至 Step 3 下一家族 |
+------------------------------|------------------------------+
                               v
+-------------------------------------------------------------+
| Step 6: 终极系统替补兜底 (Ultimate System Fallback)          |
| * 若整个列表穷尽仍无法渲染，调用系统底层“缺失字符方框”符号   |
+-------------------------------------------------------------+
```

1. **構建數據庫（Database Construction）**：瀏覽器掃描當前系統所有的可用物理字體以及當前樣式表中所有通過 `@font-face` 聲明的網絡字體，構建多維字體索引表；
2. **提取計算屬性（Property Extraction）**：確定目標元素在繼承與級聯計算後的絕對字體屬性；
3. **家族名順序遍歷（Family Matching）**：取 `font-family` 列表中的下一個候選字名進行匹配；
4. **多屬性距離逼近（Attribute Distance Search）**：
   - 首先匹配 `font-stretch`：如果完全匹配則繼續；否則在緊縮/擴展方向尋找最接近的變體；
   - 其次匹配 `font-style`：若請求 `italic`，優先尋找真正的意大利體；次優尋找 `oblique`；若仍無則使用 `normal` 正體；
   - 再次匹配 `font-weight`：若請求 `400`（normal），優先尋找 400，次優尋找 500；若請求 `500`，優先尋找 500，次優尋找 400；若請求大於等於 `600`，優先尋找更重字重，若無則尋找更輕字重；若請求小於等於 `300`，優先尋找更輕字重；
5. **字形覆蓋性檢驗（Glyph Availability Verification）**：這是最核心的特性——**字體匹配是以單個字符爲粒度進行的**！即使某款字體被成功選中，但如果它不包含當前正在排版的特定古希臘字母或中文漢字，瀏覽器**絕不會**顯示空白或亂碼，而是將該單個字符從當前字體中脫出，退回到 `font-family` 列表中的後續字體繼續尋找覆蓋該碼位的可用字形；
6. **最終回退兜底（System Fallback）**：如果整個列表的所有字體均無法覆蓋該字符，瀏覽器調用操作系統最底層的默認後備字體（如 Windows 上的 Arial / SimSun，Mac 上的 Lucida Grande / PingFang），直至顯示著名的“缺失字符替換符號”（通常爲一個帶問號的黑色菱形或十六進制碼位線框）。

---

## 3. `@font-face` 規則與早期網絡字體技術先驅

爲了打破必須依賴用戶本地已裝字體的桎梏，CSS 2 正式引入了 `@font-face` 規則，允許網頁作者指定從遠程服務器動態下載字體文件。

### 3.1 `@font-face` 描述符規範

```css
@font-face {
  font-family: "MyCustomFont";
  src: url("https://example.com/fonts/myfont.woff2") format("woff2"),
       url("https://example.com/fonts/myfont.woff") format("woff"),
       url("https://example.com/fonts/myfont.ttf") format("truetype");
  font-weight: bold;
  font-style: normal;
  font-stretch: normal;
  unicode-range: U+0000-00FF, U+0131, U+0152-0153;
}
```

`@font-face` 內部包含一系列專門的描述符：
- `font-family`：定義該網絡字體在後續 CSS 樣式中被引用的虛擬名稱；
- `src`：定義字體的遠程網絡 URL 地址以及顯式格式提示（`format(...)`）；
- `unicode-range`：**按需分片與子集化下載技術基石**。指定本字體文件所涵蓋的 Unicode 碼位區間（如 `U+0000-00FF` 僅含 ASCII 與西歐基本字符）。如果當前頁面未出現該區間內的任何文字，現代瀏覽器會自動攔截並**完全放棄下載該字體文件**，從而極大節約了移動網絡帶寬；
- 字體度量微調描述符：`units-per-em`, `ascent`, `descent`, `cap-height`, `x-height`, `bbox`, `stemv`, `stemh`。

然而，在 1990 年代末至 2000 年代初，由於字體廠商（Monotype, Linotype, Adobe）極度恐懼將價值數千美元的商業字體文件（TrueType/OpenType）裸放在 Web 服務器上會被用戶右鍵直接竊取，字體下載技術經歷了一場長達十年的殘酷陣營割據與格式戰爭。

---

### 3.2 先驅之一：Bitstream TrueDoc 與 PFR 格式

1990 年代中葉，著名數字字模開發商 Bitstream 開發了歷史上首個成熟的 Web 字體嵌入解決方案——**TrueDoc**。

![WebFont Wizard 轉換交互界面](/images/fonts-encodings/fig10-2.png)
*圖 10-2：Bitstream TrueDoc 的核心工具 WebFont Wizard 軟件操作截圖。左側選擇系統已安裝字體，右側配置字符子集與目標生成選項。*


#### 3. CSR（字符形態記錄器）的幾何擬合與動態貝塞爾重建
Bitstream TrueDoc 之所以在 1990 年代名噪一時，核心在於其獨創的 **CSR（Character Shape Recording）矢量擬合技術**。
- **高階曲線離散化**：當 CSR 處理 TrueType 的二階貝塞爾曲線或 Type 1 的三階貝塞爾曲線時，爲了規避各操作系統平臺底層光柵化引擎的專利壁壘，它首先將輪廓離散化爲一系列極細密的特徵多邊形折線；
- **自適應凸凹分割與拓撲壓縮**：算法通過檢測輪廓曲率符號的變換點（拐點與極值點），將字形筆畫劃分爲連續的單調區間（Monotonic Intervals）。在這些區間內，算法並不存儲浮點數座標，而是存儲相對於前一個特徵頂點的**一維動態位移增量（Delta Offsets）**；
- **CSP 客戶端內存即時重建**：當瀏覽器的 Character Shape Player（CSP）讀取 PFR 字節流時，它在內存中即時執行三階樣條插值與輪廓縫合，並直接掛鉤操作系統的圖形設備上下文（GDI 或 X11 GC）實施硬件繪製。這種“在作者端抽絲剝繭，在讀者端現場重構”的思想，使得 100 個西文字符的完整字形能夠在短短 8KB 至 12KB 內高質量傳輸。

#### 核心工作流與架構
TrueDoc 的核心設計目標是**防範盜版並實現極端壓縮**。它由兩大模塊構成：
1. **Character Shape Recorder（CSR，字符形態記錄器）**：這是一個運行在網頁作者端的預處理工具（如圖 10-2 所示的 WebFont Wizard）。CSR 掃描作者本地安裝的任意 PostScript Type 1 或 TrueType 字體，並不完整拷貝字體，而是掃描指定的 HTML 頁面，抽取頁面實際使用到的字符輪廓，並將這些輪廓編譯爲一種經過高強度壓縮與專有加密的緊湊二進制文件——**PFR（Portable Font Resource，便攜式字體資源，文件後綴 `.pfr`）**；
2. **Character Shape Player（CSP，字符形態播放器）**：這是一個內嵌在瀏覽器中的動態柵格化引擎。網景公司在 Netscape Navigator 4.0 中完整原生集成了 CSP 引擎，用戶無需額外安裝任何插件，即可在 Netscape 中實時渲染 `.pfr` 字體。而在 Internet Explorer 中，Bitstream 則通過提供 ActiveX 控件來實現跨平臺兼容。

雖然 TrueDoc 具有極高的字形還原品質與極小的文件體積，但隨着網景在瀏覽器大戰中的潰敗，以及微軟拒絕在 IE 中原生支持 PFR，TrueDoc 最終在 2000 年代初逐漸淡出了歷史舞臺。

---


### 3.3 先驅之二：微軟 WEFT 與嵌入式 OpenType（EOT）

爲了在網絡字體領域建立絕對霸權並保護字體知識產權，微軟於 1997 年推出了自己的專有 Web 字體解決方案：**WEFT（Web Embedding Fonts Tool）** 與 **EOT（Embedded OpenType，文件後綴 `.eot`）**。

![WEFT 字體數據庫界面](/images/fonts-encodings/fig10-3.png)
*圖 10-3：微軟 WEFT 軟件的字體數據庫視圖。清晰列出系統中各款字體的可嵌入權限等級（Embedding Permissions）。*

![WEFT 創建 EOT 字體的分步向導](/images/fonts-encodings/fig10-4.png)
*圖 10-4：WEFT 創建 EOT 嵌入字體的交互式嚮導流程步驟。*

![WEFT 生成 EOT 字體的主控制窗口](/images/fonts-encodings/fig10-5.png)
*圖 10-5：WEFT 最終分析 HTML 站點並批量生成 EOT 壓縮字體的配置窗口。*

#### 1. WEFT 的五步構建流水線
如圖 10-3、10-4 和 10-5 所示，微軟 WEFT 工具在生成 EOT 文件時執行了一套極其精密的工程管線：
1. **站點網絡爬蟲分析（Site Web Crawling）**：WEFT 內嵌了一個遞歸超文本分析器。用戶輸入一個網站的主 URL，WEFT 會自動抓取整站所有 HTML 文檔及外部 CSS 樣式表，解析所有可見文本，統計全站出現的所有字符的字符頻率直方圖（Character Frequency Histogram）；
2. **字體許可判定（License Validation）**：如圖 10-3 所示，WEFT 嚴密檢查所有候選字體的 `OS/2` 表中 `fsType` 字段（詳見本書附錄 D）。如果字體未開放嵌入權限（如被標註爲 `Restricted License`），WEFT 會彈出嚴厲的安全警告並從生成列表中剔除；
3. **字形子集裁剪（Subsetting）**：爲了避免向網絡傳輸數兆字節的完整字庫，WEFT 依據爬蟲抓取到的文本，僅保留網站實際用到的字符字形（例如 2000 個英漢混合字符中實際只用到了 180 個字符），將多餘字符的輪廓數據全部從數據表中剝離，並重新計算重構 `cmap`、`loca` 和 `glyf` 表的偏移指針；
4. **根域名強綁定加密（Root String Binding）**：作者必須在嚮導中顯式輸入該網站合法的 HTTP/HTTPS 域名（例如 `https://www.example.com`）。WEFT 將該字符串注入 EOT 頭部專有結構中，並在加載時交由 Internet Explorer 進行運行時同源反查；
5. **MicroType Express 高強度壓縮**：調用專利算法對字體二進制數據流執行無損熵壓縮，最終生成體積極小且無法在本地直接運行的 `.eot` 文件。

#### 2. EOT 文件的底層二進制頭部解構
一個標準的 EOT 文件並不等同於傳統的 TTF/OTF 文件，它在物理前端封裝了一套極其複雜的專有數據頭：
```
+-------------------------------------------------------------------+
|                     EOT Binary Header Anatomy                     |
|                                                                   |
|   uint32   EOTSize;             // 整个 EOT 文件总字节数            |
|   uint32   FontDataSize;        // 原始未压缩字体数据字节数        |
|   uint32   Version;             // EOT 规范版本 (0x00010000 / 0x02) |
|   uint32   Flags;               // 压缩/子集化标志位               |
|   uint8    FontPANOSE[10];      // 10 字节 PANOSE-1 视觉分类指纹     |
|   uint8    Charset;             // 字符集标识 (如 ANSI, DEFAULT)   |
|   uint8    Italic;              // 0=正体, 1=斜体                  |
|   uint32   Weight;              // 绝对字重数值 (如 400, 700)       |
|   uint16   fsType;              // 原始字体嵌入许可标志字          |
|   uint16   MagicNumber;         // 幻数 (固定为 0x504C, 即 'LP')   |
|   uint32   UnicodeRange1..4;    // 128 位 Unicode 码位覆盖位掩码    |
|   uint32   CodePageRange1..2;   // 64 位 Windows 代码页支持掩码     |
|   uint32   CheckSumAdjustment;  // 原字体 head 表中的校验和调整项   |
|   uint32   Reserved[4];         // 预留保留字段                    |
|   uint16   Padding1;            // 内存对齐填充                    |
|   // 可变长度字符串数组 (每个字符串以 uint16 长度引导，UTF-16LE 编码)  |
|   uint16   FamilyNameSize;      byte FamilyName[...];             |
|   uint16   StyleNameSize;       byte StyleName[...];              |
|   uint16   VersionNameSize;     byte VersionName[...];            |
|   uint16   FullNameSize;        byte FullName[...];               |
|   uint16   RootStringSize;      byte RootString[...]; // 绑定域名   |
|   // 紧随其后为 MicroType Express 压缩或原始的 SFNT 二进制数据流     |
+-------------------------------------------------------------------+
```
這種設計兼顧了瀏覽器的極速預檢（讀取頭部即可獲知字體名、PANOSE 和域名合法性）與核心輪廓資產的高度安全性。

### 3.4 動態字形服務器先驅：em2 Solutions 的 GlyphGate

對於包含數萬個複雜漢字、日文假名及韓文諺文的東亞大字符集，直接在網絡上下載一個包含全量字符的完整字體文件（動輒 10MB 至 30MB）在撥號上網時代是絕對不可承受的災難。

爲了解決大字符集在網頁上的實時展示，em2 Solutions 公司開發了突破性的 **GlyphGate** 動態字形服務器系統。

![GlyphGate 發現的服務器字體列表](/images/fonts-encodings/fig10-6.png)
*圖 10-6：瀏覽器中顯示的 GlyphGate 服務器端實時掃描並註冊的高質量可用字體列表。*

![GlyphGate 動態呈現 Palatino Linotype 擴展字符](/images/fonts-encodings/fig10-7.png)
*圖 10-7：瀏覽器窗口截屏：通過 GlyphGate 動態實時截取並渲染的 Palatino Linotype 字體在 Unicode Latin Extended-1 碼位區間的精美字形。*

#### 動態按需切片（On-demand Subsetting）
GlyphGate 徹底重構了傳統的數據流：
- 網頁客戶端並不下載靜態字體文件，而是安裝一個超輕量級的瀏覽器前端偵聽模塊；
- 當客戶端打開一個包含生僻漢字或複雜古代文字的頁面時，前端自動攔截所有未能在本地渲染的字符碼位，並向後端的 GlyphGate 服務器發出異步 HTTP 請求；
- 如圖 10-6 與 10-7 所示，後端的 GlyphGate 服務器集羣即時加載主幹大字體，在內存中毫秒級抽取這幾個特定字符的矢量輪廓，動態打包生成一份僅包含幾十字節的微型臨時 PFR 或動態矢量流即時傳回瀏覽器播放。這一架構成爲了今天現代 Web 字體動態雲託管（如 Google Fonts API 與 Adobe Fonts）的直接靈感始祖。

---

## 4. SVG（可縮放矢量圖形）與 SVG 字體體系

在 W3C 的衆多圖形標準中，**SVG（Scalable Vector Graphics）** 佔據着極其特殊的崇高地位。SVG 不僅是一個二維矢量繪圖語言，其規範在歷史上曾包含了一套**純粹基於 XML 語法描述的完整數字字體標準——SVG 字體（SVG Fonts）**。

### 4.1 XML 基礎概念速覽
SVG 建立在標準 XML 規範之上，必須嚴格遵循 XML 的語法契約：
- **良構性（Well-formedness）**：所有的標籤必須閉合（如 `<path ... />`），標籤對大小寫極度敏感，屬性值必須使用單引號或雙引號嚴密包裹；
- **命名空間（Namespaces）**：通過 `xmlns="http://www.w3.org/2000/svg"` 明確界定標籤詞彙表的權威歸屬；
- **DOM 樹狀層次（Document Object Model）**：文檔由根節點 `<svg>` 展開，包含座標系統、圖形圖元、樣式與濾鏡定義。

---


### 4.2 SVG 文本排版原語與排版空間

在探討純 SVG 字體之前，必須首先理解 SVG 是如何在沒有獨立字體定義的情況下，通過標準圖形元素控制文本佈局的。SVG 提供了專用的 `<text>` 與 `<tspan>` 標籤體系：

```xml
<svg width="600" height="200" viewBox="0 0 600 200" xmlns="http://www.w3.org/2000/svg">
  <!-- 基础水平文本排版 -->
  <text x="50" y="80" 
        font-family="Georgia, serif" 
        font-size="32" 
        fill="#1a1a1a"
        text-anchor="start">
    Voile <tspan fill="#e74c3c" font-weight="bold">Magic</tspan> Library
  </text>

  <!-- 纵向排版 (东亚竖排模式) -->
  <text x="450" y="30" 
        font-family="'Noto Serif CJK SC', serif" 
        font-size="24"
        writing-mode="tb-rl"
        glyph-orientation-vertical="0">
    古籍排版·数位典藏
  </text>
</svg>
```

#### 關鍵排版屬性與座標對齊：
1. `text-anchor`（文本錨點對齊方式）：
   - `start`：文本起始邊緣對齊於指定的 $(x, y)$ 座標點（在 LTR 文本中爲左對齊）；
   - `middle`：整個文本字符串的幾何中心水平對齊於 $(x, y)$；
   - `end`：文本末尾邊緣對齊於 $(x, y)$（在 LTR 文本中爲右對齊）。
2. `writing-mode`（書寫模式）：
   - `lr-tb`（Left-to-Right, Top-to-Bottom）：標準的現代橫向書寫；
   - `rl-tb`（Right-to-Left, Top-to-Bottom）：阿拉伯/希伯來橫向右向左書寫；
   - `tb-rl`（Top-to-Bottom, Right-to-Left）：東亞傳統自上而下縱向書寫，行流自右向左推進。
3. `glyph-orientation-vertical`：控制豎排時西文字母與數字的旋轉姿態（`0` 度直立堆疊，或 `90` 度順時針倒臥）。

#### 異體字與字形精細替換：`<altGlyph>` 體系
在處理古文字或複雜排版時，作者可能希望強制指定字體中的某一個特定字形編號（Glyph ID），而繞過標準的 Unicode 文本字符映射。SVG 規範爲此設計了 `<altGlyphDef>`, `<altGlyphItem>` 與 `<altGlyph>`：
```xml
<defs>
  <altGlyphDef id="ampersand-variants">
    <altGlyphItem>
      <!-- 优先尝试字形编号 142 (古典花体 &) -->
      <glyphRef glyphRef="#glyph142" />
    </altGlyphItem>
    <altGlyphItem>
      <!-- 次选回退标准 & -->
      <glyphRef glyphRef="#glyph38" />
    </altGlyphItem>
  </altGlyphDef>
</defs>

<text x="100" y="100">
  Smith <altGlyph xlink:href="#ampersand-variants">&amp;</altGlyph> Sons
</text>
```
這種精細到單一字形級別的引用控制，使得 SVG 在無需完整排版引擎協助的情況下，能夠直接驅動 OpenType 中高階的花體（Swash）、上下文連字（Contextual Alternates）以及歷史異體字呈現。

### 4.2 獨立 SVG 字體規範與元素語法

SVG 字體將字體的全部物理結構（頭信息、度量參數、每一個字符的貝塞爾曲線輪廓、甚至字偶距對調整）完全表達爲標準的 XML 文本元素。其核心語法架構如下：

```xml
<svg xmlns="http://www.w3.org/2000/svg">
  <defs>
    <font id="MyWebFont" horiz-adv-x="1000">
      <!-- 1. 字体度量与元数据定义 -->
      <font-face 
        font-family="MyWebFont"
        units-per-em="1000"
        panose-1="2 0 5 3 0 0 0 0 3 2"
        ascent="800"
        descent="-200"
        cap-height="700"
        x-height="500"
        bbox="-100 -250 1100 850"
        underline-thickness="50"
        underline-position="-100" />

      <!-- 2. 缺失字符兜底定义 -->
      <missing-glyph horiz-adv-x="500" d="M 50 0 L 450 0 L 450 700 L 50 700 Z" />

      <!-- 3. 具体字符字形轮廓定义 -->
      <glyph unicode="A" glyph-name="A" horiz-adv-x="720"
        d="M 100 0 L 320 650 L 400 650 L 620 0 L 510 0 L 450 180 L 270 180 L 210 0 Z M 360 480 L 290 260 L 430 260 Z" />

      <!-- 4. 水平字偶距对调整 (Kerning) -->
      <hkern u1="A" u2="V" k="-80" />
      <hkern g1="T" g2="y" k="-50" />
    </font>
  </defs>

  <!-- 引用该内联字体进行排版 -->
  <text font-family="MyWebFont" font-size="48" x="50" y="100">AVANT-GARDE</text>
</svg>
```

---

### 4.3 SVG 字體度量屬性與物理座標系

![SVG font-face 核心度量屬性圖解](/images/fonts-encodings/fig10-8.png)
*圖 10-8：`<font-face>` 元素的各種度量屬性在排版空間中的相對位置定義。左側圖示：(1) ascent 上伸高、(2) cap-height 大寫字高、(3) x-height 小寫字高、(4) 基準線 baseline、(5) descent 下延深；右側圖示：總體包圍盒 bbox 與 units-per-em 空間範圍。*

如圖 10-8 所示，SVG 字體通過 `<font-face>` 元素內嵌的屬性集完整確立了字體的數學度量空間：
- `units-per-em`（Em 單位精度）：將字身正方形（Em 方格）細分的高精度網格數，通常爲 1000（對應 PostScript 規範）或 2048（對應 TrueType 規範）；
- `ascent`：自水平基準線（Baseline，即 $y=0$）向上延伸至字體最高筆畫邊緣的設計高度；
- `descent`：自基準線向下延伸至字符最低下延筆畫（如小寫字母 `p`, `g`, `y` 的底部）的距離。**在 SVG 規範中，descent 明確採用負數表示**（如 `-200`）；
- `cap-height`：大寫字母正體（如 `H`, `I`）頂端平直筆畫相對於基線的垂直高度；
- `x-height`：小寫字母正體（如 `x`, `v`, `z`）頂端相對於基線的垂直高度；
- `bbox`：四個數值構成的全局包圍盒空間 `[min-x, min-y, max-x, max-y]`，指示整個字庫中一切字符輪廓所可能達到的極值邊界。

---

### 4.4 水平與縱向書寫模式：進深與原點幾何

![SVG 水平與垂直排版進深座標向量](/images/fonts-encodings/fig10-9.png)
*圖 10-9：水平與垂直排版下的字形進深幾何座標圖示。(1) 箭頭起始於水平原點 (horiz-origin-x, horiz-origin-y)，終結於字符右側進深位置；(2) 箭頭起始於垂直原點並向下延伸指示縱向走字進深。*

SVG 極其出色地原生統一了**橫排（Horizontal Typesetting）**與**豎排（Vertical Typesetting）**的雙重空間度量，如圖 10-9 所示：
1. **水平排版度量（Horizontal Metrics）**：
   - 默認原點座標位於基線上的字符左側邊界點 $(0, 0)$，由全局屬性 `horiz-origin-x` 與 `horiz-origin-y` 定義；
   - `horiz-adv-x`：字符排版後的水平前進位移距離（Advance Width）。當前字符繪製完畢後，排版光標自動在水平方向向右平移 `horiz-adv-x` 個設計單位，作爲下一個字符的基準原點。
2. **垂直排版度量（Vertical Metrics，東亞傳統豎排）**：
   - 垂直走字的原點通常位於字符頂端的幾何中心，通過 `vert-origin-x` 與 `vert-origin-y` 顯式設置；
   - `vert-adv-y`：字符排版後的垂直向下前進位移量（Vertical Advance Height）。繪製完畢後，光標向下平移該數值，爲下一字提供落腳點。

---

### 4.5 字偶距調整（Kerning）：`<hkern>` 與 `<vkern>`

在排版高品質西文字符串（如 `AV`, `Te`, `WA`）時，由於相鄰字符形狀互補，若僅依賴固定字符寬度會導致字符間產生刺眼的空洞。SVG 字體爲此提供了基於 XML 聲明的字偶距微調系統：
- `<hkern>`：水平字偶距調整；
- `<vkern>`：垂直字偶距調整。


#### 批量字偶距羣組定義語法
在大型專業字體中，如果爲每一個字符對單獨書寫一行 `<hkern>`，會導致 SVG 字體文件體積膨脹至數萬行。SVG 字體規範爲此提供了強大的批量羣組（Grouping）匹配語法：
- **逗號分隔多字符匹配**：`u1="A,B,D" u2="V,W,Y"` 指示集合 $\{A, B, D\}$ 中的任意字符後接集合 $\{V, W, Y\}$ 中的任意字符時，統一應用指定的緊縮量；
- **字符範圍語法（Range Syntax）**：`u1="A-Z"` 允許使用短橫線直接界定 Unicode 字符區間，極大簡化了全大寫字母間的間距壓縮規則書寫；
- **混合標識符過濾**：允許同時混合使用 `u1`、`g1` 與 `u2`、`g2`，例如 `g1="T,Tbar" u2="a-z" k="-45"`。排版引擎在掃描字符對時，會按照字形優先級匹配最狹窄的特化規則，賦予了 SVG 字體極其靈活的微觀排版調控能力。

#### 語法過濾規則：
- `u1` 與 `u2`：以 Unicode 字符形式指定左/右字符（例如 `u1="A" u2="V"`）；
- `g1` 與 `g2`：以字形名稱（Glyph Name）指定匹配字符；
- `k`：字偶距增減值（Kerning Value）。該值通常爲**負數**，指示第二個字符的原點相對於第一個字符應當向左回拉靠攏的單位距離。

---

### 4.6 深度剖析：法國經典字體 Le Monde Livre 的大寫字母 'R'

爲了讓讀者直觀感受真實世界中商業級 SVG 字體的代碼風貌，我們以讓·弗朗索瓦·波爾謝（Jean François Porchez）大師設計的著名經典正文字體 **Le Monde Livre** 中的大寫字母 `R` 爲例，分析其經由 FontForge 完整轉換出的原生 SVG 代碼：

![Le Monde Livre 字體中大寫字母 R 的矢量輪廓](/images/fonts-encodings/fig10-10.png)
*圖 10-10：法國頂級數字字體 Le Monde Livre 中的大寫字母 'R' 的貝塞爾曲線輪廓與控制點網格視圖，精確映射至下方的 SVG 路徑。*

```xml
<glyph unicode="R" glyph-name="R" horiz-adv-x="689"
  d="M 520 -15
     C 496 29 459 76 382 173
     C 305 270 244 350 200 405
     L 200 480
     C 260 485 315 500 365 525
     C 415 550 455 585 480 625
     C 505 665 515 710 515 760
     C 515 825 490 880 440 925
     C 390 970 310 995 200 1000
     L 50 1000
     L 50 0
     L 130 0
     L 130 440
     L 190 440
     C 245 440 310 350 400 230
     C 490 110 540 30 550 0
     L 660 0
     C 630 30 580 80 520 -15 Z
     M 130 520
     L 130 920
     L 190 920
     C 260 920 310 900 340 870
     C 370 840 385 790 385 730
     C 385 660 365 605 325 565
     C 285 525 220 520 130 520 Z" />
```

#### 路徑幾何與排版學解碼：
1. **外輪廓與內空腔（Sub-paths & Counters）**：
   - 第一個以 `M 520 -15` 開始的子路徑勾勒出字母 `R` 的巨大外部主輪廓，包含其標誌性優雅彎曲的右下右伸腿（Leg / Tail）；
   - 第二個以 `M 130 520` 開始的子路徑勾勒出字母 `R` 頭部的內部封閉空腔（Counter）；
2. **三次貝塞爾曲線算子（Cubic Bézier, `C`）**：
   - 路徑中的 `C` 指令後嚴格跟隨着 6 個座標參數：第一控制點 $(x_1, y_1)$、第二控制點 $(x_2, y_2)$ 以及目標錨點 $(x, y)$。這精確對應了 PostScript Type 1 字體格式的平滑曲率方程；
3. **閉合多邊形算子（`Z`）**：
   - 確保內外路徑各自形成水密閉合區域，供渲染引擎應用**非零纏繞數規則（Non-zero Winding Rule）**實施完美的矢量抗鋸齒填充。

---

## 5. Web 字體歷史博弈的終局：WOFF 與現代排版紀元

縱觀 Web 字體的拓荒史：
- Bitstream TrueDoc 帶來了最初的防盜版矢量流，但因瀏覽器分裂而隕落；
- 微軟 EOT 擁有極高壓縮率與域名綁定，但因其封閉私有而被其他廠商聯合抵制；
- SVG 字體雖然完全公開透明，但由於其純文本 XML 結構對於西文及 CJK 數萬字形而言過於冗長、解析開銷巨大且完全缺乏 TrueType/OpenType 指令級 Hinting 支持，最終於 2010 年代初被 W3C 移出 Web 標準推薦規範，僅在移動端極個別舊式 Safari 環境中短暫保留。

直到 2009 至 2010 年，Mozilla 基金會核心工程師弗拉基米爾·武基切維奇（Vladimir Vukićević）聯合多家字體廠商，正式提出了 **WOFF（Web Open Font Format）**，並在數年後升級爲 **WOFF 2.0**，徹底改寫了網絡字體排版的格局。

### 5.1 WOFF 1.0 與 WOFF 2.0 的底層技術革命

| 技術維度 | WOFF 1.0 (2010) | WOFF 2.0 (2015) |
| :--- | :--- | :--- |
| **底層核心算法** | 工業標準 zlib / Deflate 壓縮 | Google Brotli 針對字體字節流深度優化的通用熵壓縮 |
| **數據表重構** | 逐表獨立壓縮，保留原始 SFNT 表結構 | **深度變換重構（Table Transforms）**：徹底解構 `glyf` 與 `loca` |
| **相對體積節省** | 比原始 TTF/OTF 減小約 40%–50% | **比 WOFF 1.0 再進一步縮減 30%–50%**（體積僅爲原字體 25%–35%） |
| **元數據支持** | 完整的 XML 擴展元數據（版權、許可、發行者） | 延續 XML 元數據並精簡二進制封裝開銷 |
| **解包性能** | 簡單解壓，內存重構極快 | 解壓即時重構標準化 OpenType 內存映像 |

#### WOFF 2.0 對 `glyf` 表的顛覆性重構
在傳統 TrueType 字體中，每一個字符在 `glyf` 表中存儲時，其輪廓點數量、座標數組（X/Y 座標差值）、標誌位字節（Flags）與複合字形部件緊密交織在一起。這種局部交錯的數據排列極大地破壞了數據流的熵連續性，導致任何壓縮算法都無法充分施展拳腳。

WOFF 2.0 採取了一種激進的**數據流解構重組算法（Stream Separation Transformation）**：
1. 將整個字體所有字形的 X 座標差值抽取出來，合併爲一個獨立的連續純數值數據流；
2. 將所有 Y 座標差值合併爲第二個獨立流；
3. 將所有點標誌位抽取爲第三個獨立流；
4. 將所有輪廓端點索引抽取爲第四個流；
5. **完全刪除 `loca`（字形偏移索引表）**！因爲所有字形被重組後，解壓器可以通過掃描重構流中的字形長度動態實時推導恢復 `loca` 表，從而憑空節約了數千字節的開銷。
這種分流重組使得相似的數據（如連續相近的座標差值）緊密聚攏在一起，配合 Google Brotli 高達 16MB 的滑動窗口與預設靜態字典，實現了令人驚歎的極高壓縮比。

---

### 5.2 現代 Web 排版性能：`font-display` 與 FOIT / FOUT 控制

隨着網絡字體普及，前端開發者面臨着兩種極其痛苦的頁面加載視覺體驗缺陷：
1. **FOIT（Flash of Invisible Text，無內容閃爍）**：瀏覽器在下載網絡字體的幾十至幾百毫秒內，頁面正文文字完全處於透明不可見狀態，用戶面對一片空白的網頁無法閱讀；
2. **FOUT（Flash of Unstyled Text，無樣式文本閃爍）**：瀏覽器先立即使用本地默認字體（如 Times 或 Arial）渲染文字，當網絡字體下載完成後突然粗暴地重繪替換，導致文字瞬間跳變重排，極度損傷視覺連續性。

爲此，CSS Fonts 規範引入了 **`font-display`** 屬性，賦予網頁開發者對字體加載生命週期的完全掌控權：
```css
@font-face {
  font-family: "MyModernFont";
  src: url("myfont.woff2") format("woff2");
  font-display: swap;
}
```

#### 五大調度模式：
- `auto`：瀏覽器默認行爲（絕大多數現代瀏覽器採取大約 3 秒的 FOIT 阻斷期，隨後若未加載完成則降級爲 FOUT）；
- `block`：給予極短的空白等待期（約 3 秒），若在此時限內字體就緒則直接無縫顯示，專爲不可被替代的特殊品牌標誌字體設計；
- `swap`：**正文閱讀的最佳實踐**！阻止期爲 0 秒，瀏覽器立即使用後備字體渲染出文字（確保用戶第一時間讀到內容），網絡字體一旦就緒立刻原地平滑替換；
- `fallback`：極短的阻塞期（約 100 毫秒）與較短的替換窗口。如果字體未在 3 秒內就緒，則永久放棄本次網絡字體替換，在本頁面生命週期內完全使用本地後備字體，避免頁面在用戶深度閱讀中途發生突兀跳動；
- `optional`：專爲弱網環境設計（如 2G/3G 移動端）。僅在緩存中命中或在極瞬息內下載完成時才使用網絡字體；若網絡稍有延遲則徹底放棄下載，以最快速度節省用戶移動流量。

---



縱觀 Web 字體的拓荒史：
- Bitstream TrueDoc 帶來了最初的防盜版矢量流，但因瀏覽器分裂而隕落；
- 微軟 EOT 擁有極高壓縮率與域名綁定，但因其封閉私有而被其他廠商聯合抵制；
- SVG 字體雖然完全公開透明，但由於其純文本 XML 結構對於西文及 CJK 數萬字形而言過於冗長、解析開銷巨大且完全缺乏 TrueType/OpenType 指令級 Hinting 支持，最終於 2010 年代初被 W3C 移出 Web 標準推薦規範，僅在移動端極個別舊式 Safari 環境中短暫保留。

直到 2009 至 2010 年，Mozilla 基金會核心工程師弗拉基米爾·武基切維奇（Vladimir Vukićević）聯合多家字體廠商，正式提出了 **WOFF（Web Open Font Format）**：
- WOFF 放棄了另起爐竈建立新幾何格式的幻象，而是迴歸常識：**直接將工業標準的 SFNT 字體（TrueType 或 OpenType CFF）進行模塊化無損解構**；
- 引入經過深度優化的 zlib（以及 WOFF 2.0 中的 Google Brotli）流壓縮算法，將各表數據壓縮 30% 到 50%；
- 允許在文件頭中注入公開的 XML 格式元數據（包含鑄模廠版權、設計師簽名與許可聲明），既不使用侵入式的 DRM 加密，又充分給予了商業字模廠合法的法律申訴證據。

WOFF 與 WOFF2 迅速被全球所有現代瀏覽器（Chrome, Firefox, Safari, Edge）全票通過接納，正式終結了長達十五年的 Web 字體格式亂局。今天，藉助 `@font-face`、WOFF2 以及 OpenType 1.8 可變字體技術，人類終於在萬維網的每一個屏幕像素上，完整實現了幾百年來由古登堡、阿爾杜斯、加拉蒙與察普夫在金屬活字上所締造的高雅排版之夢。
