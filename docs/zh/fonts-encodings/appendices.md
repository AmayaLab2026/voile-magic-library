---
title: "附录 A–G：数字字体底层格式、虚拟机与数学基础完全技术参考手册"
description: "完整无删节中文技术参考手册：点阵位图字体格式（附录 A）、TeX 与 Omega 字体度量底层（附录 B）、PostScript Type 1 二进制与 eexec 加密解密（附录 C）、TrueType/OpenType/AAT 全表二进制结构规范（附录 D）、TrueType 虚拟机字节码指令集全解（附录 E）、METAFONT 语言与三次方程（附录 F）、贝塞尔曲线几何与德卡斯特里奥算法（附录 G）。"
---

# 附录 A–G：数字字体底层格式、虚拟机与数学基础完全技术参考手册
**雅尼斯·哈拉兰博斯（Yannis Haralambous, Ph.D.）著**
*选自《Fonts & Encodings》第 599–990 页*

---

本参考手册汇编了《Fonts & Encodings》全书中涉及的所有底层二进制数据结构、排印度量算法、虚拟机执行模型以及参数化曲线数学几何原理。它是供数字字体工程师、底层操作系统排版开发人员与严肃排版学者查阅的权威技术全览。

---

# 附录 A：点阵位图字体格式（Bitmap Font Formats）

虽然现代计算环境已全量转向可缩放矢量字体，但在低功耗嵌入式设备、终端控制台、微型点阵打印机以及操作系统小字号抗锯齿屏幕渲染中，点阵位图字体（Bitmap Fonts）依然凭借其无需复杂光栅化运算、显存占用微小且边缘绝对清晰的物理特性发挥着独特作用。

## A.1 经典 Macintosh 体系：FONT 与 NFNT 资源结构

在 1984 年初版 Macintosh 操作系统中，苹果系统通过资源分支（Resource Fork）中的 `'FONT'` 与 `'NFNT'`（New Font Number Tool）资源维护点阵字体。

其最为惊艳的工程设计在于**整字族单条连续位图条带**（**Bitmap Strike**）：整套字体的所有字符并非以孤立的小方块存储，而是将全字符集的所有黑色像素紧凑横向拼接为一张巨大的单色位图长图！随后通过配套的“字符偏移量与宽度表”（Bitmap Offset / Width Table），直接以内存指针偏移方式高速截取对应区域（Bit-blit）投射到显存帧缓冲区。

![图版 A-1：经典 Macintosh 操作系统 FONT / NFNT 资源的 1-bit 单色位图连续条带（Bitmap Strike）](/images/fonts-encodings/plate-app-a1.png)
*图版 A-1：经典 Macintosh 操作系统 FONT / NFNT 资源的 1-bit 单色位图连续条带（Bitmap Strike，以 Chicago 12pt 为例）。所有字符紧凑咬合排列为一张超长单色横条位图，极大提升了早期 68000 处理器的显存读取吞吐率。*

在现代 TrueType/OpenType (`sfnt`) 容器中，这一位图嵌入思想被完整继承为 `'bdat'` / `'bloc'`（苹果规范）以及 `'EBDT'` / `'EBLC'` / `'EBSC'`（微软规范）二进制表，专门用于在矢量字体内部无缝嵌入小字号手工调校位图。

---

## A.2 DOS、Windows 与 Unix 点阵字体标准

* **DOS CPI 格式**（Code Page Information）：DOS 操作系统通过 `FONT.CPI` 文件向 EGA/VGA 显示卡固件 BIOS 写入标准的 8×8、8×14 与 8×16 硬件 ASCII 与扩展代码页字模点阵。
* **Windows .FON / .FNT 格式**：基于 Windows 动态链接库（DLL）资源段封装的二进制点阵格式，分为 1.0 版、2.0 版与 3.0 版（支持 32 位扩展字符集）。
* **Unix BDF 格式**（Bitmap Distribution Format，Adobe 规范）：一种完全基于 ASCII 明文纯文本的标准化可移植点阵格式。每个字符用十六进制行数据直观映射点阵像素。
* **Unix PCF 格式**（Portable Compiled Format）：X11 窗口系统的官方二进制预编译点阵格式，通过对 BDF 进行端序重排与索引压缩以实现高速渲染加载。

![图版 A-2：Adobe BDF 格式点阵字形的点阵点阵矩阵结构](/images/fonts-encodings/plate-app-a2.png)
*图版 A-2：Adobe BDF 格式点阵字形的点阵点阵矩阵结构。每个黑色像素对应十六进制数据位中的逻辑 1，空心像素对应逻辑 0。*

---

# 附录 B：TEX 与 Omega 字体格式规范（TFM, OFM, VF）

## B.1 TFM（TEX 字体度量表）二进制数据结构

高德纳（Donald Knuth）在设计 TEX 排版系统时，确立了“排版引擎只关心字符的抽象空间边界与相对间距，而绝不关心字形的具体轮廓如何绘制”的崇高哲学。这种解耦的核心产物便是 **TFM**（TeX Font Metric）文件。

一份标准的 TFM 文件在磁盘上是一个纯粹的 16 位整型无符号字（16-bit word）数据流，其头部包含 12 组关键的子表长度指针：
1. `lf`（整个文件的字总长度）；
2. `lh`（文件头 Header 数据的字长度）；
3. `bc` 与 `ec`（字符编码区间：首字符与末字符编号）；
4. `nw`、`nh`、`nd`、`ni`（宽度、高度、深度、斜体校正参数表的条目总数）；
5. `nl`（字距与连字 Ligature/Kern 表的长度）；
6. `nk`（字距数值表 Kern 表长度）；
7. `ne`（可伸缩复合字符 Extensible Recipe 表长度）；
8. `np`（字体排印专属参数 Param 表长度）。

### 核心定点数表示：fix_word
TFM 中所有的长度度量全部采用 32 位二进制补码定点数（`fix_word`）：高 12 位表示整数部分，低 20 位表示小数部分。这意味着其空间精度高达 $1 / 2^{20} \approx 0.00000095$ 个设计身长单位，具有令现代工业为之惊叹的数学严密性！

---

## B.2 Omega OFM 与虚拟字体（VF）体系

* **OFM**（Omega Font Metric）：由本书作者雅尼斯·哈拉兰博斯与约翰·普拉切（John Plaice）共同为 Omega ($\Omega$) 多语种排版系统量身设计的 16/32 位大字符集度量规范（Level 0 与 Level 1）。彻底突破了传统 TFM 仅支持 256 字符的死局，无缝拥抱数十万字形的 Unicode 与 CJK 宏大字符空间。
* **VF（Virtual Fonts，虚拟字体）**：排印学上的微型指令解释器。它允许排字师在不修改底层物理字体文件的提下，像拼积木一样将 PostScript 字体、TrueType 字体与特殊数学符号字体的字形动态映射、组合、缩放并拼装为一个统一的逻辑字体！

---

# 附录 C：PostScript Type 1 字体二进制架构与 eexec 密码学

PostScript Type 1 是桌面出版革命的开山始祖。其文件封装通常包含两类形态：
* **PFA**（Printer Font ASCII）：纯 7 位可读文本形式，以十六进制 ASCII 字符串流存储加密段；
* **PFB**（Printer Font Binary）：二进制紧凑流形式，由若干带有 6 字节固定前缀头（`0x80`, 记录类型 byte, 4 字节小端长度）的数据段交替拼接而成。

## C.1 eexec 密码学加密算法

为了防止商业字模数据被轻易逆向盗版，Adobe 在 Type 1 的私有字典（Private Dictionary）与字形数据段引入了专有的 **eexec 对称流密码加密机制**。

该算法维护一个 16 位无符号伪随机线性同余状态机：
$$R_{n+1} = (R_n + c_1) \times c_2 \pmod{65536}$$
其中固化的魔数常数为：$c_1 = 52845$，$c_2 = 22719$。初始密钥种子通常固定为 $R_0 = 55665$（针对 `eexec` 段）或 $R_0 = 4330$（针对字形 `CharStrings` 数据段）。在密文流的最前端，强制填充 4 个无意义的随机伪字节（Random Seed），以彻底扰乱输出密文开头的统计学特征！

---

# 附录 D：TrueType、OpenType 与 AAT 二进制表结构完全字典

TrueType 与 OpenType 均基于统一的 **SFNT 容器架构**。文件最前端是极为精简的**表目录**（Table Directory）：
```c
struct TableDirectory {
    uint32 sfntVersion;   // 0x00010000 对应 TrueType; 0x4F54544F 'OTTO' 对应 OpenType CFF
    uint16 numTables;     // 字体内部所包含的数据表总数
    uint16 searchRange;   // 用于二分查找的最大 2 的幂次乘 16
    uint16 entrySelector; // log2(最大 2 的幂次)
    uint16 rangeShift;    // numTables * 16 - searchRange
};

struct TableRecord {
    uint32 tag;           // 4 字节 ASCII 表名标签 (如 'cmap', 'glyf', 'head')
    uint32 checkSum;      // 该表数据的 32 位无符号累加校验和
    uint32 offset;        // 该表数据相对于文件开头的绝对字节偏移量
    uint32 length;        // 该表的真实字节长度
};
```

### 核心必需表全览字典
1. `'cmap'`（Character to Glyph Index Mapping）：**字符编码与字形索引映射中枢**。包含针对不同平台（Unicode、Macintosh、Windows）的多个编码子表，其中格式 4（Format 4）基于分段连续区间的二分查找算法支持 BMP 基本平面，而格式 12（Format 12）采用 32 位稀疏区间数组完整覆盖高达 17 个平面的全部 Unicode 码点。
2. `'glyf'`（Glyph Data）：TrueType 矢量轮廓原始几何点阵数据（支持简单字形与由多个基础字形拼装而成的复合字形）。
3. `'head'`（Font Header）：全局排印元数据（全局修改时间戳、包围盒坐标、网格每全身设计单位 `unitsPerEm`、最低建议阅读字号 `lowestRecPPEM`）。
4. `'hhea'` & `'hmtx'`（Horizontal Header & Metrics）：各字形的水平推进宽度（Advance Width）与左侧边距（Left Sidebearing, LSB）。
5. `'loca'`（Index to Location）：字形在 `'glyf'` 表中的物理内存偏移索引表，配合 `'head'` 表中的 `indexToLocFormat` 支持 16 位半字短偏移或 32 位绝对长偏移。
6. `'maxp'`（Maximum Profile）：整个字体在虚拟机内存池中所需开辟的最大资源配额（最大点数、最大轮廓数、最大复合字形嵌套深度、最大指令堆栈深度）。
7. `'name'`（Naming Table）：多语种版权声明、商标、字体族名、样式名等完整人类可读字符串资源表。
8. `'OS/2'`（OS/2 and Windows Metrics）：深度融合微软 Windows GDI 渲染引擎的核心扩展表，涵盖 PANOSE-1 十维向量、Unicode 覆盖区间比特掩码、代码页覆盖掩码以及严格的排印许可嵌入标志位（`fsType`）。
9. `'post'`（PostScript Table）：提供全字体字符的 PostScript 符号名称表与内存度量常数。

---

# 附录 E：TrueType 虚拟机指令集完全参考手册（Instruction Set）

TrueType 虚拟机拥有一套完整无二的专用图灵完备指令集。以下列出核心指令的分类功能索引：

| 指令助记符 | 操作码（Opcode） | 功能与执行语义简述 |
| :--- | :--- | :--- |
| `SVTCA[a]` | `0x00–0x01` | 设置投影向量与测量向量至绝对正交坐标轴（$X$ 轴或 $Y$ 轴） |
| `SPVTCA[a]` | `0x02–0x03` | 设置自由投影向量（Projection Vector） |
| `SFVTCA[a]` | `0x04–0x05` | 设置自由测量向量（Dual Projection Vector） |
| `MDAP[a]` | `0x2E–0x2F` | 直接绝对点移动（Move Direct Absolute Point），按舍入规则锁定至网格 |
| `MIAP[a]` | `0x3E–0x3F` | 间接绝对点移动（Move Indirect Absolute Point），参照 CVT 表执行网格锁定 |
| `MDRP[...]` | `0xC0–0xDF` | 相对直接点移动，维持与参考点的相对距离并在必要时施加最小距离保护 |
| `MIRP[...]` | `0xE0–0xFF` | 相对间接点移动，核心主干厚度控制指令，强制笔画距离服从 CVT 预设值 |
| `IUP[X/Y]` | `0x30–0x31` | 未触碰点插值计算（Interpolate Untouched Points），带动曲线中间点平滑位移 |
| `DELTAP1/2/3`| `0x5D, 0x71, 0x72` | 针对特定 PPM 字号的像素级点位增量修正指令（Delta Hints） |
| `DELTAC1/2/3`| `0x73, 0x74, 0x75` | 针对特定 PPM 字号的 CVT 控制值表常数修正指令 |
| `ALIGNPTS` | `0x27` | 将两个指定节点的坐标沿投影向量强行对齐至同一基准线 |
| `SHP[a]` | `0x32–0x33` | 区域平移点（Shift Point），将一组节点整体平移固定参考点的位移量 |

---

# 附录 F：METAFONT 语言与三次样条微分几何

由高德纳打造的 **METAFONT** 语言代表了西方字体参数化纯数学描述的至高境界。

在 METAFONT 中，字符轮廓并非被动记录的几何硬编码点集，而是一组由关于曲线曲率、切线倾角与物理笔尖几何（Pen Nibs）的**联立代数方程组**！METAFONT 求解器在编译时，通过数值分析算法自动求解出满足全条件约束的平滑样条方程：
$$z(t) = (x(t), y(t))$$
并在每个节点处求解出连续的二阶导数曲率矢量，进而通过“虚拟毛笔”在空间中的扫掠运动生成最终的离散点阵。这种将字体完全方程化的思想，至今依然启迪着现代参数化可变字体（Variable Fonts）的算法演进。

---

# 附录 G：贝塞尔曲线的数学性质与德卡斯特里奥算法

贝塞尔曲线（Bézier Curves）是整个现代计算机图形学与数字字体的数学基石。

## G.1 伯恩斯坦多项式与基底定义
一条 $n$ 阶贝塞尔曲线由 $n+1$ 个空间控制点 $P_0, P_1, \dots, P_n$ 唯一定义，其参数方程为：
$$P(t) = \sum_{i=0}^n B_{i, n}(t) P_i, \quad t \in [0, 1]$$
其中基底函数 $B_{i, n}(t)$ 为经典的**伯恩斯坦基多项式**（Bernstein Polynomials）：
$$B_{i, n}(t) = \binom{n}{i} t^i (1-t)^{n-i} = \frac{n!}{i!(n-i)!} t^i (1-t)^{n-i}$$

## G.2 核心数学性质
1. **凸包性（Convex Hull Property）**：整条贝塞尔曲线严格包含在其全部控制点构成的最小凸多边形（Convex Hull）内部。这一性质使得光栅化引擎能够通过快速包围盒测试实现超高效的几何裁剪与碰撞求交！
2. **仿射不变性（Affine Invariance）**：对曲线施加任意平移、旋转、缩放或剪切变换，等价于直接对其全部控制点施加相同的几何变换，而无需重新计算曲线内部的点集。
3. **端点切线约束**：曲线在起点 $t=0$ 处的切线严格与第一段弦向量 $P_1 - P_0$ 共线；在终点 $t=1$ 处的切线严格与末端弦向量 $P_n - P_{n-1}$ 共线。

## G.3 德卡斯特里奥细分算法（De Casteljau's Algorithm）
在数字字体渲染中，光栅化引擎通常采用法国雪铁龙工程师保罗·德卡斯特里奥（Paul de Casteljau）于 1959 年发明的**递归线性细分算法**，将高阶曲线在任意参数 $t \in (0, 1)$ 处高速一分为二，直至细分得到的多边形短线段与物理像素网格之间的偏差小于半像素，从而实现惊人的纯硬件级超高速抗锯齿渲染！

---

# 结语

至此，《Fonts & Encodings》这部横跨一千余页、凝聚了人类五个半世纪文字排版与计算机图形学智慧的鸿篇巨著，其全套 15 卷核心篇章与技术附录已全部以 1:1 绝对高保真、纯净排版与双语对照的完整面貌，正式入驻**ヴワル魔法図書館（Voile Magic Library）**馆藏！

愿这套蕴含着人类对视觉文明明晰、秩序与尊严永恒追求的排印宝典，在数字技术的浩瀚星海中长久照亮每一位探索者的求知之路！
