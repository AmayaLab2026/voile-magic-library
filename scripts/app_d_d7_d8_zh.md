## D.7 点阵嵌入表族：EBLC、EBDT、EBSC 与 bhed（Bitmap Management）

在低分辨率液晶屏或打印机上，依靠矢量轮廓与 Hinting 虚拟机实时解算微观网格有时依然难以兼顾极佳的阅读质感，尤其对于拥有繁复交织笔画的东亚巨型汉字库而言更是如此。为此，微软与苹果在 OpenType/TrueType 架构中设计了一组专门用于在矢量字体内部直接封装离散手绘点阵字符的底层数据表：

### D.7.1 嵌入位图定位与数据表：`EBLC` 与 `EBDT`（亦名 `bloc` 与 `bdat`）

`EBLC`（Embedded Bitmap Location Table）与 `EBDT`（Embedded Bitmap Data Table）在逻辑上必须成对共存。在苹果 AAT 规范中，这两个表分别被称为 `bloc` 与 `bdat`，两者的二进制拓扑结构完全兼容。

- **`EBLC`（定位索引表）**：
  不保存具体的单色点阵位图像素，而是专门存储整座字库在不同目标显示尺寸下的**字号打击表（`bitmapSizeTable` / Strike）**与指向对应字形位图数据的字节偏移指针。每个 Strike 声明了适用的水平与垂直分辨率（如 96 DPI）、字号像素大小（ppem）、颜色位深（1 位单色、2/4/8 位抗锯齿灰度），并引用一组子索引表（`IndexSubTable`）。
- **五大子索引表类型（`IndexSubTable` Formats 1–5）**：
  * **Format 1**：等长字形位图变长数据索引，包含各字形的显式数据偏移数组；
  * **Format 2**：所有字形共享完全相同的度量尺寸与位图字节长度，偏移量可通过简单线性乘法算得；
  * **Format 3**：双字节变长偏移索引，适用于较紧凑的字库；
  * **Format 4**：基于稀疏字形 ID 数组的非连续码表索引；
  * **Format 5**：稀疏固定尺寸点阵索引。
- **`EBDT`（真实位图数据流）**：
  紧跟在 `EBLC` 之后，严格由各个具体字形的单色或多阶灰度位图数据包（`bitmapGlyph`）紧密排布而成。规范定义了 Formats 1 至 9 多达九种位图存储编码：
  * **Format 1/2**：小尺寸度量头加按字节对齐（Byte-aligned）或位对齐（Bit-aligned）的原始位图点阵；
  * **Format 5**：仅包含纯位图位流，完全省略度量头（所有字形强制继承外部统一 Strike 度量）；
  * **Format 8/9**：复合点阵字形（Component Bitmap Glyphs），允许通过多个子图元叠加拼装形成复杂的合字或重音汉字！

### D.7.2 嵌入位图尺寸倍率缩放表：`EBSC`

当应用程序请求的显示字号恰好落在字库未曾内置真实手工点阵的中间地带（例如字库仅手工绘制了 12px 与 16px 点阵，而用户请求了 14px）时，`EBSC`（Embedded Bitmap Scaling Table）表负责介入仲裁：它向渲染系统声明是否允许通过对最邻近的已有点阵 Strike 进行整数倍插值或抽取缩放来合成中间尺寸，从而避免突兀地切换回生硬的未优化矢量轮廓。

### D.7.3 位图头表：`bhed`

在仅包含纯点阵字形而完全剔除矢量 `glyf` 表的极端嵌入式 TrueType 点阵字库中，苹果规范规定使用 `bhed` 表完全取代原有的矢量 `head` 表，其字段定义与标准 `head` 完全一致，唯独在魔数与特性标志位上向系统声明这是一座纯位图字体。

---

## D.8 核心可选辅助表族：`DSIG`、`gasp`、`hdmx`、`LTSH`、`kern` 与 `VDMX`（Optional Tables）

除核心骨干表外，一座高工业规格的 OpenType/TrueType 商业字体通常还包含一系列精妙的可选度量与安全控制表：

### D.8.1 数字签名表：`DSIG`

`DSIG`（Digital Signature Table）用于保证字体文件在互联网或企业分发过程中的知识产权归属与未篡改完整性。该表内嵌由权威公钥基础设施（PKI / VeriSign 等）签发的 X.509 标准 PKCS#7 格式二进制加密证书签名。当 Windows 操作系统加载字体时，内核字体驱动会解析 `DSIG` 表并比对全表校验和；若签名有效，字体属性面板将展示“受信任商业数字签名”徽标。

### D.8.2 网格拟合与平滑光栅化策略表：`gasp`

在屏幕渲染历史上，`gasp`（Grid-fitting and Scan-conversion Procedure Table）是微软为协调 TrueType 虚拟机字节码 Hinting 与操作系统抗锯齿（ClearType）渲染而设立的决策总指挥部。

`gasp` 表按字号像素尺寸（ppem）划分区间，为不同的显示精度阶梯配置四种核心标志位组合：
* **`GASP_GRIDFIT` (`0x0001`)**：启用 TrueType 字节码执行引擎，强行将控制点对齐物理像素网格；
* **`GASP_DOGRAY` (`0x0002`)**：启用多级灰度亚像素抗锯齿平滑；
* **`GASP_SYMMETRIC_SMOOTHING` (`0x0008`)**：启用全对称平滑滤波；
* **`GASP_SYMMETRIC_GRIDFIT` (`0x0004`)**：启用高精对称网格拟合。

典型配置法则：在极小字号（如 $0 \le \text{ppem} \le 8$）下仅启用灰度平滑（防止笔画粘连成黑块）；在阅读字号（$9 \le \text{ppem} \le 16$）下同时强制开启 `GRIDFIT` 与 `DOGRAY`（获得最清晰锐利的正文字骨）；而在超大字号（$\ge 17$）下关闭字节码 Hinting、全权交由纯平滑抗锯齿渲染以呈现自然曲率。

### D.8.3 高速设备度量缓存与线性阈值表：`hdmx` 与 `LTSH`

- **`hdmx`（Horizontal Device Metrics）**：
  由于 TrueType 提示指令（Hinting）会在离散像素级别强行推拉控制点，导致小字号下的实际像素前进宽度（Advance Width in Pixels）往往偏离由浮点数线性缩放算出的理想宽度。为了避免排版引擎在计算长文本换行时频繁调用沉重的虚拟机解释器逐字解算，`hdmx` 表预先将常见字号下全体字形的整数像素宽度烘焙固化为极速查表数组。
- **`LTSH`（Linear Threshold Table）**：
  记录每个字形的“线性阈值”（以 ppem 为单位）。在该阈值尺寸之下，字形受 Hinting 扭曲影响显著，宽度必须查阅 `hdmx`；而一旦字号超过该阈值，字形宽度的非线性形变降至可忽略不计的程度，排版引擎可安全切回极速浮点线性乘法。

### D.8.4 传统字距微调表：`kern`

在 OpenType `GPOS` 表横空出世之前，经典 TrueType 与早期 Mac 字体完全依赖 `kern` 表实现字符对之间的字距微调。

`kern` 表包含多个子表（Subtables），最常用的为 **Format 0（有序字偶微调对）**：
- 子表头部声明字偶微调对总数 `nPairs`；
- 紧随其后的是按 `(leftGlyph, rightGlyph)` 严格二分递增排列的条目数组；
- 每个条目由左字形 ID、右字形 ID 以及一个带符号的 16 位整数 `FWord` 距离微调值构成。现代排版引擎若在字体中同时探测到 `GPOS` 与 `kern` 表，规范要求**优先执行 `GPOS` 表的上下文微调并静默屏蔽 `kern`**。

### D.8.5 垂直设备度量量化表：`VDMX`

`VDMX`（Vertical Device Metrics Table）用于解决在非线性 Hinting 介入下，字体在特定 ppem 尺寸下实际渲染像素的最高上升部（Max Ascender）与最低下降部（Min Descender）偏离全局设计比例的问题。它为每一个目标字号提供了一对强制量化的像素整数极值，供 Windows GDI 等渲染框架在计算单行文本物理行高边界框时使用，彻底消除了文本滚动时因行高抖动引发的屏幕闪烁撕裂。

### D.8.6 垂直排版度量头与进深表：`vhea` 与 `vmtx`

与水平排版的 `hhea` 和 `hmtx` 高度镜像对称，`vhea`（Vertical Header Table）与 `vmtx`（Vertical Metrics Table）是驱动东亚纵向直排的关键数据底座：
- `vhea` 声明全局垂直基线距离、最大纵向进深与超限参数；
- `vmtx` 存储每个字形的纵向步进高度（`advanceHeight`）与顶端边距（`topSideBearing`，即字形包围盒顶缘距离纵向原点的垂直落差）。

### D.8.7 惠普 PCL 5 属性表：`PCLT`

`PCLT` 表专门服务于 HP LaserJet 打印机及兼容 PCL 5 页面描述协议的工业输出设备。该表容纳了字体的 16 位校验和、原厂字库代号、笔画字重数字、宽度比例、衬线样式代码（Serif Style）以及专门用于 PCL 字体匹配的专属符号集代码。
