---
title: 附录全编 · 字体格式、底层架构与数学原理全景手册
description: 雅尼斯·哈拉兰布斯《Fonts & Encodings》附录 A 至 G 全景学术精要：点阵字库（BDF/PCF/PK）、TeX/Omega 度量体系（TFM/OFM/VF）、PostScript 页面描述语言与 Type 1/CFF、TrueType/OpenType/AAT 底层表结构汇编、METAFONT 衍生系统、以及贝塞尔曲线数学定理严密推导。
---

# 附录全编 · 字体格式、底层架构与数学原理全景手册
### Appendices A–G: Font Formats, Virtual Machines & Mathematical Foundations
**著者：雅尼斯·哈拉兰布斯 博士（Yannis Haralambous, Ph.D.）**  
*选自《字体与编码》（Fonts & Encodings）原著第 599–1010 页*

---

本附录合编汇集了雅尼斯·哈拉兰布斯教授在《字体与编码》末尾倾注毕生学术心血编纂的**全景技术附录（Appendices A 至 G）**。它不仅是全书各章排印理论的底层工程基石，更是全人类数字字体工业界有史以来最为详尽、严密的格式白皮书与数学参考典范。

---

## 附录 A：点阵字体格式全景（Bitmap Font Formats）

在矢量轮廓技术成熟之前，点阵字体（Bitmap Fonts）曾统治计算机屏幕与针式/激光打印机数十年。哈拉兰布斯在原著中系统解构了五大生态体系下的点阵格式：

### 1. 经典操作系统阵营
* **Macintosh 生态**：
  * **`FONT` 资源**：早期经典 Mac OS 7/8/9 的基础点阵资源，内部包含字形图像字条（Bitmaps Strip）与字符偏移表；
  * **`NFNT` 资源（New Font Numbering Table）**：为克服 512 个字体家族 ID 限制而升级的现代化点阵资源；
* **DOS 与 Windows 生态**：
  * **`CPI` 格式（Code Page Information）**：DOS 控制台驱动（`DISPLAY.SYS`）使用的全硬件字模文件；
  * **`FNT` / `FON` 格式**：Windows 3.x/95/98 的核心点阵格式。`.fon` 本质上是一个仅包含资源段（Resource-only）的 16 位 Windows 可执行文件（NE / PE 封装），内部嵌入了多种字号的 `.fnt` 位图流；
* **Unix / X Window 生态**：
  * **BDF（Bitmap Distribution Format）**：Adobe 制定的纯 ASCII 文本点阵交换格式，结构极度清晰，包含字形边界盒（`BBX`）、公制度量（`DWIDTH`）与十六进制点阵掩码；
  * **PCF（Portable Compiled Format）**：X11 将 BDF 编译后生成的紧凑二进制文件，支持多架构字节序自适应，至今仍是 Linux 终端低开销启动的基石；
  * **HBF（Hanzi Bitmap Font）**：由东亚开源先驱（如陈向东等）制定的汉字大点阵索引标准，巧妙解决了海量汉字位图的快速随机定位。

### 2. TeX 科学排版阵营：GF 与 PK 压缩算法
在高德纳的 $\TeX$ 体系中，METAFONT 生成的原始点阵为 **GF（Generic Font）** 格式，随后由工具转换为极度精炼的 **PK 格式（Packed Font）**：
* PK 格式采用**动态行程长度编码（Dynamic Run-length Encoding）**；
* 高德纳巧妙地根据黑白相间的平均概率分布，将重复长度动态打包进半字节（Nybble, 4 位）中；
* 一款包含完整西文字符集的 300 DPI 点阵字库，经 PK 压缩后通常不足 20 KB，达到了二十世纪八十年代信息熵压缩的数学极境。

---

## 附录 B：TeX 与 $\Omega$ 度量文件规范（TeX & Omega Formats）

高德纳的 $\TeX$ 编译排版系统不直接读取字形图像，而完全依托**度量文件**。本附录详细解密了其二进制字节流规范：

### 1. TFM（TeX Font Metric）二进制解剖
TFM 文件由一连串 32 位大端无符号字（Words）构成，严格划分为十个数据段：
1. **Header**：校验码（Checksum）、设计字号（Design Size，定点数表示）及字符集说明；
2. **Char Info Table（字符信息表）**：定长 256 项数组，每项 4 字节，紧凑打包了：
   * 宽度索引（`width_index`, 8 位）；
   * 高度与深度索引（`height_index` 4 位, `depth_index` 4 位）；
   * 斜度修正索引（`italic_index`, 6 位）；
   * 标记类型（`tag`, 2 位）：声明该字符是普通字符、连字字距机入口、抑或是数学超大括号的垂直延伸件；
   * 剩余数据指针（`remainder`, 8 位）；
3. **Width / Height / Depth / Italic Tables**：存储浮点度量常量；
4. **Lig/Kern Program Table**：状态机跳转微指令表，指导引擎何时执行替换或微调；
5. **Extensible Recipe Table**：数学符号拼装配方表；
6. **Font Parameters Table（`fontdimen`）**：全局字体排版常数（空格宽度、伸缩量、收缩量、x 字高、四则运算上下标对齐线高度）。

### 2. OFM（Omega Font Metric）与 OVF（Omega Virtual Font）
针对经典 TFM 仅支持 256 字符的死穴，雅尼斯·哈拉兰布斯开创了 **OFM 格式**：
* 引入两级表结构（Level 0 与 Level 1）；
* 全面支持 16 位与 32 位字符索引（突破至 65,536 及 1,114,112 码位）；
* 扩展了多向排版（从右至左、从上至下）的度量原点位移；
* **OVF（Omega 虚拟字体）**：允许在虚拟机指令中直接嵌入 32 位 Unicode 字符级联与动态字形算术合成。

---

## 附录 C：PostScript 页面语言与 Type 1 / CFF 字体

Adobe 的 PostScript 是一种图灵完备的**逆波兰式堆栈解释型编程语言（Stack-based Language）**。

### 1. PostScript 语言核心运行机制
* **四大多态运算栈**：操作数栈（Operand Stack）、执行栈（Execution Stack）、字典栈（Dictionary Stack）、图形状态栈（GState Stack）；
* **当前变换矩阵（Current Transformation Matrix, CTM）**：
  $$\begin{bmatrix} x' & y' & 1 \end{bmatrix} = \begin{bmatrix} x & y & 1 \end{bmatrix} \begin{bmatrix} a & b & 0 \\ c & d & 0 \\ t_x & t_y & 1 \end{bmatrix}$$
  实现任意视口平移（`translate`）、缩放（`scale`）与任意角度旋转（`rotate`）；
* **路径与轮廓绘制**：`newpath`, `moveto`, `lineto`, `curveto`（三次贝塞尔样条）, `closepath`, `fill`, `stroke`。

### 2. Type 1 与 Type 2 / CFF 底层字形指令（CharStrings）
在 Type 1 / CFF 字体中，每一个字符由一段高度加密与压缩的二进制字节码表示：
* **加密算法**：采用 Adobe 专有的双层伪随机异或加密（`eexec` 与 `charstring encrypt`）；
* **Type 2 相对坐标编码**：为了极致节省空间，Type 2 抛弃了绝对坐标，所有参数均为相对前一个节点的位移差值（$\Delta x, \Delta y$），并使用变长字节编码整数；
* **核心运算符**：
  * `rmoveto`：相对移动起始点；
  * `rlineto`：相对直线绘制；
  * `rrcurveto`：绘制三次贝塞尔曲线段（传入三组相对控制点坐标偏移）；
  * `hstem` / `vstem` / `hstemhm`：声明水平与垂直主干提示；
  * `endchar`：终止当前字形解释并执行全局闭合填充。

---

## 附录 D：TrueType、OpenType 与 AAT 底层表结构汇编

现代智能字体文件由一个**表目录（Table Directory）**与一簇以 4 字节标签（Tag）命名的独立二进制表格构成：

```
+-------------------------------------------------------+
| sfnt 封装头 (4 字节: 0x00010000 或 'OTTO')            |
+-------------------------------------------------------+
| numTables (表格总数) | searchRange | entrySelector     |
+-------------------------------------------------------+
| 表记录项 1: 'head' (校验和, 偏移量 offset, 长度 length)  |
| 表记录项 2: 'cmap' (校验和, 偏移量 offset, 长度 length)  |
| 表记录项 3: 'glyf' / 'CFF ' ...                       |
+-------------------------------------------------------+
| 各独立表格的原始二进制数据载荷 (4 字节对齐)             |
+-------------------------------------------------------+
```

### 1. 核心骨干表速查
| 表标签（Tag） | 表格中文全称 | 核心字段与技术职责 |
| :--- | :--- | :--- |
| **`head`** | 字体通用全局头信息 | 记录字体魔数（`0x5F0F3CF5`）、版本号、设计网格单位（`unitsPerEm`, 如 1000 或 2048）、全局边界盒 `[xMin, yMin, xMax, yMax]`、以及 `loca` 表索引偏移格式（16位短整数 vs 32位长整数）。 |
| **`cmap`** | 字符编码到字形映射 | 包含多个子表：Subtable 0（单字节 256 映射）、Subtable 4（经典 BMP 16 位分段二分搜索表）、Subtable 12（现代全量 32 位 Unicode 密集段映射表）。 |
| **`maxp`** | 资源最大需求清单 | 向光栅化引擎预告字形总数（`numGlyphs`）、最大轮廓点数、最大指令堆栈深度、复合字形最大递归嵌套层级，供操作系统一次性分配渲染内存。 |
| **`hhea` / `hmtx`** | 水平排版度量头与数组 | `hhea` 记录字体总上升高度（`Ascender`）、总下沉深度（`Descender`）、行间距（`LineGap`）；`hmtx` 数组存储每一个字形的水平进身宽（`advanceWidth`）与左字边距（`lsb`）。 |
| **`OS/2`** | 跨平台排版兼容表 | 微软与 IBM 联合制定：包含 Panose 十维编码、Unicode 覆盖范围位图掩码（128 位）、代码页范围掩码、字重等级（`usWeightClass` 100-900）、上标与下标的物理几何偏移。 |
| **`name`** | 多语言版权与命名表 | 包含数十项 NameID：版权声明 (0)、字体家族名 (1)、字体子家族名 (2)、唯一识别标识符 (3)、全名 (4)、版本字符串 (5)、PostScript 内部名称 (6)。全部支持按平台与语言 ID 国际化本地化。 |

### 2. 轮廓存储表：`glyf` 与 `loca`
在 TrueType 字体中：
* **`loca` 表（Index to Location）**：记录每个 Glyph ID 在 `glyf` 表中的起始字节偏移量；
* **`glyf` 表（Glyph Data）**：
  * **简单字形（Simple Glyph）**：记录轮廓线数 $N$、各轮廓终点索引数组、标志位字节数组（标记每个控制点是在曲线内部 On-curve 还是曲线外部 Off-curve，以及坐标压缩标志）、以及坐标差值序列；
  * **复合字形（Composite Glyph）**：自身不包含轮廓点，而是引用其他字形 ID，并附带 $2 \times 2$ 仿射变换矩阵（缩放、旋转、斜切）与平移量（用于由基底字母与重音符瞬时组装成复合字符）。

---

## 附录 E：METAFONT 语言与衍生系统（METAFONT & Derivatives）

高德纳开创的 METAFONT 是计算机字体设计领域唯一的纯数学代数方程系统：
* **方程求解引擎**：设计师不必计算节点的绝对坐标，只需写下几何约束方程（例如：`z2 = 0.5[z1, z3]; x4 - x2 = y3 - y1;`），METAFONT 内建的线性方程组求解器在编译时自动求出全局精确解；
* **笔刷轨迹动力学（Pen Dynamics）**：字符轮廓被抽象为一枚具有特定倾角与几何形状的笔刷（如椭圆笔 `pickup pencircle scaled 2pt yscaled 0.2 rotated 30;`）沿着骨架轨迹滑行扫过的包络面（Envelope）；
* **METATYPE1 与 MetaFog**：哈拉兰布斯详细评述了将 METAFONT 的动态笔刷包络方程自动求导、寻找切线、并逆向转换为 PostScript Type 1 闭合三次贝塞尔轮廓线的高级数学算法。

---

## 附录 G：贝塞尔曲线与排印数学严密证明导引

在附录的终卷，哈拉兰布斯以一位纯粹数学家的严谨，给出了现代数字排印学底层几何曲线的经典数学证明：

### 1. 伯恩斯坦多项式与德卡斯特里奥算法（De Casteljau's Algorithm）
次数为 $n$ 的贝塞尔曲线在数学上由**伯恩斯坦基底多项式（Bernstein Polynomials）**展开定义：
$$\mathbf{B}(t) = \sum_{i=0}^n B_{i, n}(t) \mathbf{P}_i, \quad B_{i, n}(t) = \binom{n}{i} t^i (1-t)^{n-i}, \quad t \in [0, 1]$$
德卡斯特里奥递归几何割线算法证明了：对于任意参数 $t_0 \in (0, 1)$，可以通过有限次线性插值将一条贝塞尔曲线严格无损地切分为两段独立的子贝塞尔曲线，为计算机图形学的局部裁剪与自适应细分渲染奠定了算法基础。

### 2. 二次样条升阶为三次样条（Degree Elevation）
当字体编辑器需要将 TrueType 的二次曲线转换为 PostScript 的三次曲线时，保持几何轨迹绝对不变的升阶公式为：
$$\mathbf{Q}_0 = \mathbf{P}_0, \quad \mathbf{Q}_1 = \frac{1}{3}\mathbf{P}_0 + \frac{2}{3}\mathbf{P}_1, \quad \mathbf{Q}_2 = \frac{2}{3}\mathbf{P}_1 + \frac{1}{3}\mathbf{P}_2, \quad \mathbf{Q}_3 = \mathbf{P}_2$$
这一优雅的数学恒等式，确保了跨平台字体格式转换时的轮廓保真度。

### 3. 曲率、拐点与边界盒极值判定
一条参数化曲线 $\mathbf{r}(t) = [x(t), y(t)]$ 在任意参数 $t$ 处的**曲率（Curvature）**公式为：
$$\kappa(t) = \frac{x'(t) y''(t) - y'(t) x''(t)}{\big( x'(t)^2 + y'(t)^2 \big)^{3/2}}$$
* **拐点条件**：当 $\kappa(t) = 0$ 且符号改变时，曲线发生凹凸反向（三次曲线独有，二次曲线恒不为零）；
* **紧致边界盒（Exact Bounding Box）**：计算字形边界盒不能单纯取控制点的最值（凸包外框过大），而必须分别求解一阶导数方程 $x'(t) = 0$ 与 $y'(t) = 0$ 的一元二次方程根 $t \in [0, 1]$，将求得的极值点代入原方程，与端点比对，方能求出严格切合字形轮廓的极值边界盒坐标！

---

至此，从远古泥板与中世纪抄本的灵性光辉，到现代操作系统的图灵虚拟机与微米级像素渲染，雅尼斯·哈拉兰布斯教授为全人类编织的这部千页排印技术圣典，已在**ヴワル魔法図書館（Voile Magic Library）**的浩瀚文库中完整重现、永恒长存。
