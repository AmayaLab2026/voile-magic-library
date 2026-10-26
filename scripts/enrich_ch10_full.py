import re

with open('scripts/ch10_content.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's expand Section 2 (PANOSE, unicode-range, openType features)
# Section 3 (WEFT EOT binary layout, PFR chunks, GlyphGate architecture)
# Section 4 (SVG text layout, altGlyph, path mathematics)
# Section 5 (WOFF 1.0 vs WOFF 2.0 Brotli transform, font-display FOIT/FOUT)

p_sec2 = text.find('### 2.2 `font-size-adjust`')
sec2_extra = r"""
#### 7. PANOSE-1 分类学体系与 `@font-face` 物理描述符
在高端排版与智能字体匹配中，仅靠字形名称与粗略字重远远不够。CSS 规范深度吸收了惠普（Hewlett-Packard）公司研发的 **PANOSE-1 字体分类编码体系**。PANOSE-1 是一个由 10 个离散十进制十进制数字构成的特征指纹数组：
```css
@font-face {
  font-family: "MyClassicSerif";
  src: url("classic-serif.woff2") format("woff2");
  panose-1: 2 4 6 3 5 4 5 2 3 4;
}
```
这 10 个数字在排版学上分别代表：
1. `Family Kind`（字体大类：2 为拉丁正文字体，3 为拉丁手写体，4 为装饰字体，5 为等宽字）；
2. `Serif Style`（衬线形态：小三角、直角、平头、凹陷、圆形衬线等）；
3. `Weight`（字重量级：极细至极黑）；
4. `Proportion`（长宽比例：现代、古典、展开、紧缩）；
5. `Contrast`（主副笔画粗细对比度）；
6. `Stroke Variation`（笔画过渡渐变平缓度）；
7. `Arm Style`（字干与字臂装饰角形态）；
8. `Letterform`（字母字身几何轮廓构造：直立、手写、斜角）；
9. `Midline`（横画中线位置与 x-高度视觉相对关系）；
10. `X-height`（x-高度占整个字身方格的离散相对比例）。

当声明了 `panose-1` 指纹后，浏览器能够在本地备选字体库中计算各字体的 **PANOSE 加权欧式几何距离**，从而在降级替换时精准挑选中视觉风格、笔画粗细对比度与原字最接近的替代字体。

#### 8. `unicode-range` 的三种语法范式与字体按需切片
`unicode-range` 是实现现代 Web 字体按需分片（Font Splitting）的基石。它支持三种精确的声明语法：
1. **单码位指定**：`unicode-range: U+26;`（仅匹配 `&` 符号）；
2. **闭区间范围指定**：`unicode-range: U+0020-007F;`（精确覆盖基本 ASCII 字符区）；
3. **问号通配符范围（Wildcard Range）**：`unicode-range: U+4??;`（问号匹配十六进制任意一位，即匹配 `U+0400` 至 `U+04FF`，完整覆盖西里尔字母全区）。

通过在样式表中声明多个同名但拥有不同 `unicode-range` 的 `@font-face` 规则，浏览器能够实现**多语言混合智能按需分流**：渲染英文字符时仅下载 15KB 的西文子集；当页面出现俄文时仅增量下载 20KB 的西里尔子集；当出现汉字时才触发东亚大子集的异步加载。

"""

text = text[:p_sec2] + sec2_extra + text[p_sec2:]

# Now let's expand Section 3 with EOT binary anatomy and WEFT crawling
p_sec3_3 = text.find('### 3.3 先驱之二：微软 WEFT 与嵌入式 OpenType（EOT）')
p_sec3_4 = text.find('### 3.4 动态字形服务器先驱：em2 Solutions 的 GlyphGate')

sec3_weft_enrich = r"""
### 3.3 先驱之二：微软 WEFT 与嵌入式 OpenType（EOT）

为了在网络字体领域建立绝对霸权并保护字体知识产权，微软于 1997 年推出了自己的专有 Web 字体解决方案：**WEFT（Web Embedding Fonts Tool）** 与 **EOT（Embedded OpenType，文件后缀 `.eot`）**。

![WEFT 字体数据库界面](/images/fonts-encodings/fig10-3.png)
*图 10-3：微软 WEFT 软件的字体数据库视图。清晰列出系统中各款字体的可嵌入权限等级（Embedding Permissions）。*

![WEFT 创建 EOT 字体的分步向导](/images/fonts-encodings/fig10-4.png)
*图 10-4：WEFT 创建 EOT 嵌入字体的交互式向导流程步骤。*

![WEFT 生成 EOT 字体的主控制窗口](/images/fonts-encodings/fig10-5.png)
*图 10-5：WEFT 最终分析 HTML 站点并批量生成 EOT 压缩字体的配置窗口。*

#### 1. WEFT 的五步构建流水线
如图 10-3、10-4 和 10-5 所示，微软 WEFT 工具在生成 EOT 文件时执行了一套极其精密的工程管线：
1. **站点网络爬虫分析（Site Web Crawling）**：WEFT 内嵌了一个递归超文本分析器。用户输入一个网站的主 URL，WEFT 会自动抓取整站所有 HTML 文档及外部 CSS 样式表，解析所有可见文本，统计全站出现的所有字符的字符频率直方图（Character Frequency Histogram）；
2. **字体许可判定（License Validation）**：如图 10-3 所示，WEFT 严密检查所有候选字体的 `OS/2` 表中 `fsType` 字段（详见本书附录 D）。如果字体未开放嵌入权限（如被标注为 `Restricted License`），WEFT 会弹出严厉的安全警告并从生成列表中剔除；
3. **字形子集裁剪（Subsetting）**：为了避免向网络传输数兆字节的完整字库，WEFT 依据爬虫抓取到的文本，仅保留网站实际用到的字符字形（例如 2000 个英汉混合字符中实际只用到了 180 个字符），将多余字符的轮廓数据全部从数据表中剥离，并重新计算重构 `cmap`、`loca` 和 `glyf` 表的偏移指针；
4. **根域名强绑定加密（Root String Binding）**：作者必须在向导中显式输入该网站合法的 HTTP/HTTPS 域名（例如 `https://www.example.com`）。WEFT 将该字符串注入 EOT 头部专有结构中，并在加载时交由 Internet Explorer 进行运行时同源反查；
5. **MicroType Express 高强度压缩**：调用专利算法对字体二进制数据流执行无损熵压缩，最终生成体积极小且无法在本地直接运行的 `.eot` 文件。

#### 2. EOT 文件的底层二进制头部解构
一个标准的 EOT 文件并不等同于传统的 TTF/OTF 文件，它在物理前端封装了一套极其复杂的专有数据头：
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
这种设计兼顾了浏览器的极速预检（读取头部即可获知字体名、PANOSE 和域名合法性）与核心轮廓资产的高度安全性。

"""

text = text[:p_sec3_3] + sec3_weft_enrich + text[p_sec3_4:]

# Now let's expand Section 4 with SVG text layout, altGlyph, and writing modes
p_sec4_2 = text.find('### 4.2 独立 SVG 字体规范与元素语法')
sec4_text_primitives = r"""
### 4.2 SVG 文本排版原语与排版空间

在探讨纯 SVG 字体之前，必须首先理解 SVG 是如何在没有独立字体定义的情况下，通过标准图形元素控制文本布局的。SVG 提供了专用的 `<text>` 与 `<tspan>` 标签体系：

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

#### 关键排版属性与坐标对齐：
1. `text-anchor`（文本锚点对齐方式）：
   - `start`：文本起始边缘对齐于指定的 $(x, y)$ 坐标点（在 LTR 文本中为左对齐）；
   - `middle`：整个文本字符串的几何中心水平对齐于 $(x, y)$；
   - `end`：文本末尾边缘对齐于 $(x, y)$（在 LTR 文本中为右对齐）。
2. `writing-mode`（书写模式）：
   - `lr-tb`（Left-to-Right, Top-to-Bottom）：标准的现代横向书写；
   - `rl-tb`（Right-to-Left, Top-to-Bottom）：阿拉伯/希伯来横向右向左书写；
   - `tb-rl`（Top-to-Bottom, Right-to-Left）：东亚传统自上而下纵向书写，行流自右向左推进。
3. `glyph-orientation-vertical`：控制竖排时西文字母与数字的旋转姿态（`0` 度直立堆叠，或 `90` 度顺时针倒卧）。

#### 异体字与字形精细替换：`<altGlyph>` 体系
在处理古文字或复杂排版时，作者可能希望强制指定字体中的某一个特定字形编号（Glyph ID），而绕过标准的 Unicode 文本字符映射。SVG 规范为此设计了 `<altGlyphDef>`, `<altGlyphItem>` 与 `<altGlyph>`：
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
这种精细到单一字形级别的引用控制，使得 SVG 在无需完整排版引擎协助的情况下，能够直接驱动 OpenType 中高阶的花体（Swash）、上下文连字（Contextual Alternates）以及历史异体字呈现。

"""

text = text[:p_sec4_2] + sec4_text_primitives + text[p_sec4_2:]

# Now expand Section 5 with WOFF 1 vs WOFF 2 technical details and FOIT/FOUT
p_sec5 = text.find('## 5. Web 字体历史博弈的终局：WOFF 与现代排版纪元')
sec5_rich = r"""## 5. Web 字体历史博弈的终局：WOFF 与现代排版纪元

纵观 Web 字体的拓荒史：
- Bitstream TrueDoc 带来了最初的防盗版矢量流，但因浏览器分裂而陨落；
- 微软 EOT 拥有极高压缩率与域名绑定，但因其封闭私有而被其他厂商联合抵制；
- SVG 字体虽然完全公开透明，但由于其纯文本 XML 结构对于西文及 CJK 数万字形而言过于冗长、解析开销巨大且完全缺乏 TrueType/OpenType 指令级 Hinting 支持，最终于 2010 年代初被 W3C 移出 Web 标准推荐规范，仅在移动端极个别旧式 Safari 环境中短暂保留。

直到 2009 至 2010 年，Mozilla 基金会核心工程师弗拉基米尔·武基切维奇（Vladimir Vukićević）联合多家字体厂商，正式提出了 **WOFF（Web Open Font Format）**，并在数年后升级为 **WOFF 2.0**，彻底改写了网络字体排版的格局。

### 5.1 WOFF 1.0 与 WOFF 2.0 的底层技术革命

| 技术维度 | WOFF 1.0 (2010) | WOFF 2.0 (2015) |
| :--- | :--- | :--- |
| **底层核心算法** | 工业标准 zlib / Deflate 压缩 | Google Brotli 针对字体字节流深度优化的通用熵压缩 |
| **数据表重构** | 逐表独立压缩，保留原始 SFNT 表结构 | **深度变换重构（Table Transforms）**：彻底解构 `glyf` 与 `loca` |
| **相对体积节省** | 比原始 TTF/OTF 减小约 40%–50% | **比 WOFF 1.0 再进一步缩减 30%–50%**（体积仅为原字体 25%–35%） |
| **元数据支持** | 完整的 XML 扩展元数据（版权、许可、发行者） | 延续 XML 元数据并精简二进制封装开销 |
| **解包性能** | 简单解压，内存重构极快 | 解压即时重构标准化 OpenType 内存映像 |

#### WOFF 2.0 对 `glyf` 表的颠覆性重构
在传统 TrueType 字体中，每一个字符在 `glyf` 表中存储时，其轮廓点数量、坐标数组（X/Y 坐标差值）、标志位字节（Flags）与复合字形部件紧密交织在一起。这种局部交错的数据排列极大地破坏了数据流的熵连续性，导致任何压缩算法都无法充分施展拳脚。

WOFF 2.0 采取了一种激进的**数据流解构重组算法（Stream Separation Transformation）**：
1. 将整个字体所有字形的 X 坐标差值抽取出来，合并为一个独立的连续纯数值数据流；
2. 将所有 Y 坐标差值合并为第二个独立流；
3. 将所有点标志位抽取为第三个独立流；
4. 将所有轮廓端点索引抽取为第四个流；
5. **完全删除 `loca`（字形偏移索引表）**！因为所有字形被重组后，解压器可以通过扫描重构流中的字形长度动态实时推导恢复 `loca` 表，从而凭空节约了数千字节的开销。
这种分流重组使得相似的数据（如连续相近的坐标差值）紧密聚拢在一起，配合 Google Brotli 高达 16MB 的滑动窗口与预设静态字典，实现了令人惊叹的极高压缩比。

---

### 5.2 现代 Web 排版性能：`font-display` 与 FOIT / FOUT 控制

随着网络字体普及，前端开发者面临着两种极其痛苦的页面加载视觉体验缺陷：
1. **FOIT（Flash of Invisible Text，无内容闪烁）**：浏览器在下载网络字体的几十至几百毫秒内，页面正文文字完全处于透明不可见状态，用户面对一片空白的网页无法阅读；
2. **FOUT（Flash of Unstyled Text，无样式文本闪烁）**：浏览器先立即使用本地默认字体（如 Times 或 Arial）渲染文字，当网络字体下载完成后突然粗暴地重绘替换，导致文字瞬间跳变重排，极度损伤视觉连续性。

为此，CSS Fonts 规范引入了 **`font-display`** 属性，赋予网页开发者对字体加载生命周期的完全掌控权：
```css
@font-face {
  font-family: "MyModernFont";
  src: url("myfont.woff2") format("woff2");
  font-display: swap;
}
```

#### 五大调度模式：
- `auto`：浏览器默认行为（绝大多数现代浏览器采取大约 3 秒的 FOIT 阻断期，随后若未加载完成则降级为 FOUT）；
- `block`：给予极短的空白等待期（约 3 秒），若在此时限内字体就绪则直接无缝显示，专为不可被替代的特殊品牌标志字体设计；
- `swap`：**正文阅读的最佳实践**！阻止期为 0 秒，浏览器立即使用后备字体渲染出文字（确保用户第一时间读到内容），网络字体一旦就绪立刻原地平滑替换；
- `fallback`：极短的阻塞期（约 100 毫秒）与较短的替换窗口。如果字体未在 3 秒内就绪，则永久放弃本次网络字体替换，在本页面生命周期内完全使用本地后备字体，避免页面在用户深度阅读中途发生突兀跳动；
- `optional`：专为弱网环境设计（如 2G/3G 移动端）。仅在缓存中命中或在极瞬息内下载完成时才使用网络字体；若网络稍有延迟则彻底放弃下载，以最快速度节省用户移动流量。

---

"""

text = text[:p_sec5] + sec5_rich + text[p_sec5+len('## 5. Web 字体历史博弈的终局：WOFF 与现代排版纪元'):]

with open('scripts/ch10_content.md', 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Enriched scripts/ch10_content.md to {len(text)} characters!")
