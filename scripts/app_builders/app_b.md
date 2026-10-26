# 附录 B：TeX 与 Omega 字体度量文件规范（TFM, OFM, VF, OVF）

*译者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

在计算机排版技术史上，高德纳（Donald Knuth）在设计 TeX 系统时提出了一个彻底超越时代的软硬件解耦范式：**排版排版引擎在计算段落折行、数学公式排版与页面微积分模型时，根本不需要知道字形的长相（轮廓或位图），而仅仅需要知道字符的几何度量盒模型（Metrics Box Model）！**

这一哲学造就了 **TFM（TeX Font Metric）** 格式。在排版过程中，TeX 仅读取极小体积的 `.tfm` 二进制文件（通常仅几千字节），极大地降低了内存消耗并提升了排版速度；字形的实际绘制轮廓则完全延迟到设备驱动程序（DVI 驱动、dvips、pdfTeX）在最终输出纸张或屏幕时才进行绑定。随后，雅尼斯·哈拉兰博斯（Yannis Haralambous）与约翰·普莱斯（John Plaice）在开发多语言多方向排版系统 Omega 时，将 TFM 进一步发展为支持 16 位与 32 位 Unicode 全量字符空间的 **OFM（Omega Font Metrics）** 与 **OVF（Omega Virtual Fonts）**。

---

## B.1 TFM 文件的 12 张核心数据表与二进制拓扑

一个标准的 TFM 文件在磁盘上被组织为严格紧凑的 12 个二进制数组。所有多字节整数一律采用大端序（Big-Endian / Network Byte Order）存储：

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

### 1. 定点数数学体系：`fix_word` 的微积分精度
TFM 文件内部所有的尺寸量度（字宽、字高、字深、字距、数学参数）均采用 32 位有符号定点数 **`fix_word`** 存储。其内部结构为一个包含 1 个符号位、11 个整数位与 20 个二进制小数位的定点数：

$$1\text{ fix\_word} = \frac{\text{Value}}{2^{20}} = \frac{\text{Value}}{1,048,576} \times (\text{Design Size})$$

#### `fix_word` 的三大物理法则：
1. `fix_word` 并不是绝对的物理毫米或点数，而是一个**相对于字体标称设计尺寸（Design Size）的无量纲相对缩放因子**！
2. 内部数值 $1,048,576$（即十六进制 `0x00100000`）精确代表相对倍率 $1.0$；
3. 其数值分辨率达到了惊人的 $\frac{1}{1,048,576} \approx 9.5367 \times 10^{-7}$，即便在将字体放大至数千磅的巨幅海报排版中，也能确保累加舍入误差绝对小于一个光栅点阵像素！

### 2. `CHAR_INFO` 四字节位域的极致紧凑打包
在 TFM 中，从 `bc` 到 `ec` 的每一个字符仅占用整整 4 个字节（一个 32 位机器字），高德纳通过极其巧妙的位域切片，将四维信息彻底压缩于其中：

```
+----------------+--------+--------+------------+-----+----------------+
|  width_index   | height | depth  |   italic   | tag |   remainder    |
|    (8 bits)    | (4 bit)| (4 bit)|  (6 bits)  | (2) |    (8 bits)    |
+----------------+--------+--------+------------+-----+----------------+
  Byte 0           Byte 1 (H/D)      Byte 2 (Ital/Tag)   Byte 3
```

* **Byte 0 (`width_index`)**：字宽索引（8 位，0–255）。直接指向 `WIDTH` 数组中该字符的字宽 `fix_word`。注意：`WIDTH[0]` 恒定为 0.0，若字符缺失则索引填 0；
* **Byte 1 高 4 位 (`height_index`)**：字高索引（0–15）。指向 `HEIGHT` 数组中的 16 种字高之一；
* **Byte 1 低 4 位 (`depth_index`)**：字深索引（0–15）。指向 `DEPTH` 数组中的 16 种字深之一；
* **Byte 2 高 6 位 (`italic_index`)**：倾斜校正与数学间距索引（0–63）。指向 `ITALIC` 数组；
* **Byte 2 低 2 位 (`tag`)**：**核心行为标签位（Behavior Tag）**，指示 Byte 3 `remainder` 的解释语义：
  * `tag = 0 (no_tag)`：常规普通字符，`remainder` 字段无意义（填 0）；
  * `tag = 1 (lig_tag)`：**合字与字距链起始**。`remainder` 字段为该字符在 `LIG_KERN` 字节码数组中的第一条指令步长索引；
  * `tag = 2 (list_tag)`：**数学定界符递增链表**。用于数学公式排版，`remainder` 给出比当前字符稍大一号的同形字符 ASCII 码点！例如：小型左括号 '(' 的 `remainder` 指向中型左括号，中型指向大型左括号，大型指向超大型左括号，TeX 据此在行内根据公式高度逐级挑选合适大小的括号；
  * `tag = 3 (ext_tag)`：**无限可伸展定界符配方**。当公式高度超过所有离散预制字符时，`remainder` 指向 `EXTEN` 数组中的一条结构体记录，指示如何使用顶部、中部、底部与重复构件拼装出任意高度的巨型大括号或积分号。

### 3. `LIG_KERN` 虚拟字节码指令集
`LIG_KERN` 表是一个包含了连字融铸与成对字距调整的微型执行引擎。每条指令占用 4 个字节：

```c
struct LigKernStep {
    uint8 skip_byte;    /* 跳跃控制字节：若 >= 128 则为停机指令（Stop Step） */
    uint8 next_char;    /* 预期紧随其后的相邻字符码点 */
    uint8 op_byte;      /* 操作码字节：若 >= 128 则为字距微调；若 < 128 则为合字替换 */
    uint8 remainder;    /* 结果：目标字距在 KERN 表中的索引，或新合成的合字码点 */
};
```

#### 指令执行状态机算法：
1. 欲评估字符对 $(C_1, C_2)$ 是否存在连字或字距调整，首先检查 $C_1$ 的 `tag` 是否等于 1；
2. 若是，令指令指针 $p = \text{remainder}(C_1)$，进入 `LIG_KERN` 数组循环：
   * 读取当前步骤：`skip = LIG_KERN[p].skip_byte`；
   * 若 `LIG_KERN[p].next_char == C2`，说明**规则命中**！
     * 若 `op_byte >= 128`：触发**字距微调（Kern）**！间隙值等于 $\text{KERN}[256 \times (\text{op\_byte} - 128) + \text{remainder}]$；
     * 若 `op_byte < 128`：触发**合字替换（Ligature）**！替换后生成的新字符为 `remainder`，同时 `op_byte` 的位域指示是否继续消耗后续字符；
     * 执行完毕，退出状态机；
   * 若未命中：
     * 若 `skip >= 128`：说明到达链表末端（Stop），规则未匹配，退出；
     * 否则令指针跳跃：$p = p + skip + 1$，继续下一轮匹配。

### 4. `PARAM` 全局参数表与数学字体 22 维物理参数
`PARAM` 表定义了该字体的宏观排印物理常数。对于普通正文字体，包含 7 个标准参数：
1. `slant`：字体倾斜率（垂直每上升 1 单位的水平倾斜位移）；
2. `space`：词间标准空格宽度；
3. `space_stretch`：段落两端对齐时允许空格被拉伸的最大弹性限度；
4. `space_shrink`：允许空格被压缩的最大收缩限度；
5. `x_height`：小写字母 'x' 的标准高度；
6. `quad`：一个全角方（Em）的基准设计宽度；
7. `extra_space`：句号等句末标点后推荐额外追加的间隙。

对于**数学符号字体（Math Symbol Fonts）**与**数学扩展字体（Math Extension Fonts）**，高德纳在此扩展了多达 22 个神圣的排印参数：
* `num1`：行间陈列公式（Display style）中分子基线提升高度；
* `num2`：行内文本公式（Text style）中无分数线时的分子提升高度；
* `num3`：行内文本公式中有常规分数线时的分子提升高度；
* `denom1`：行间公式中分母基线压低深度；
* `denom2`：行内公式中分母压低深度；
* `sup1`：行间公式中上标基线抬升量；
* `sup2`：行内正文公式中上标抬升量；
* `sup3`：无下标伴随时的纯上标额外抬升；
* `sub1`：常规下标压低量；
* `sub2`：上标过大时的下标额外避让压低；
* `supdrop`：上标构件顶部距基字的最小投影下沉；
* `subdrop`：下标底部距基字的投影下沉；
* `delim1`：行间公式中定界符（如左大括号）的最小覆盖高度；
* `delim2`：行内公式中定界符的最小高度；
* `axis_height`：数学符号中轴线高度（分数线与减号的绝对垂直中心）。

每一个参数控制着分子分母基线提升、根号连梁厚度、分数线垂直轴心等微积分几何学常量，成为了全球数学印艺不可逾越的黄金规范。

---

## B.2 Omega 字体度量（OFM: Omega Font Metrics）对多语言的扩展

随着计算机排版走向全球化，TFM 基于 8 位 ASCII（最多 256 字符）的设计成为巨大瓶颈。1994 年，哈拉兰博斯与普莱斯在 Omega 项目中制定了 **OFM（Omega Font Metrics）** 规范。

### 1. OFM Level 0：16 位 Unicode 宽字符扩展
OFM Level 0 将字符寻址空间扩展至 16 位整数（支持 65,536 个字符），完整覆盖了当时的 Unicode 基本多语言平面（BMP）：
* 表头头部魔数扩展为 32 位，引入了对多达数十万字节超大度量表的直接物理寻址；
* `CHAR_INFO` 表中的每一个条目从 4 字节扩展为 12 字节甚至更长，彻底解除了 16 种字高与 64 种倾斜校正的位域限制；
* 支持长合字链与上下文敏感的连字评估。

### 2. OFM Level 1：多方向动态排版支持
在 OFM Level 1 中，Omega 引进了突破性的**四向排印物理坐标系统**：
* 文本不仅支持从左向右（L2R），更原生支持从右向左（R2L，如阿拉伯文、希伯来文）、从上到下（T2B，如传统汉字、满文）与从下到上；
* 每个字符内部包含针对四种流动方向的独立包围盒度量向量；
* 引入了基于上下文模式匹配规则表（Contextual Rule Tables），为早期希腊语古籍多重变音符与阿拉伯文字符变形提供了直接度量支持。

---

## B.3 虚拟字体系统（VF 与 OVF）的指令执行引擎

虚拟字体（Virtual Fonts, `.vf` 与 `.ovf`）是 TeX 生态中最具黑客智慧的发明之一。它允许排版师**凭空创造一个物理上根本不存在的“合成字体”**！

### 1. 虚拟字体的架构哲学
假设我们希望排版希腊文，但手头只有一份缺少重音变体字母的 Adobe Times 商业矢量字体，以及一份由 METAFONT 生成的单色重音点阵字体。通过编写一个 `.vf` 虚拟字体映射文件：
* TeX 引擎在排版时，仅仅将该虚拟字体视为一个普通的单一字体；
* 当遇到带重音的希腊字母时，虚拟字体引擎会在后台将其动态展开为一段**微型的 DVI 字节码渲染脚本**：先从物理字体 A 中取出字母轮廓，接着移动绘图原点，再从物理字体 B 中调出重音符号，最后重合输出！

### 2. 虚拟字体的 256 操作码虚拟机指令集
VF 文件内部包含一个完整的微型 DVI 解释器，其核心操作码与 DVI 格式高度同构：
* `set_char_0` 至 `set_char_127`（操作码 0–127）：从当前绑定的物理基字库中绘制指定字符；
* `set_rule`（操作码 132）：直接在页面上绘制一条实心黑矩形连梁或横线（用于分数线与底线）；
* `push`（操作码 141）/ `pop`（操作码 142）：将当前二维绘图坐标 $(x, y)$ 压入硬件栈或从栈中弹出；
* `right1` 至 `right4`（操作码 143–146）：沿水平方向推进指定数量的定点数单位；
* `down1` 至 `down4`（操作码 157–160）：沿垂直方向向下移动；
* `fnt_def1` 至 `fnt_def4`（操作码 243–246）：在虚拟字体内部声明引用的外部真实物理字体（包括字名、校验和与缩放比例）；
* `fnt_num_0` 至 `fnt_num_63`（操作码 171–234）：快速切换当前正在调用的真实底层字体句柄。

### 3. VPL（Virtual Property List）人类可读源码范例
通过 `vptovf` 工具，排版师可将以下人类可读的 `.vpl` 文件直接编译为二进制 `.vf` 与 `.tfm`：

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

通过这一套极致纯粹的虚拟字体架构，TeX 体系无需重新铸造任何物理字形，即可在排印层实现跨字库的无限无缝熔铸与扩展。
---

## B.4 TeX 数学排版引擎 22 维物理参数的几何代数模型

高德纳在《The TeXbook》附录 G 中，精确公开了 TeX 数学公式排版引擎在二维平面上装配分子、分母、根号连梁与上下标时的微积分几何方程。这些方程直接调用 TFM 中的 `PARAM` 数组参数（在数学符号字体中称为 $\sigma_1 \dots \sigma_{22}$，在数学扩展字体中称为 $\xi_1 \dots \xi_{13}$）：

### 1. 分式（Fractions）分子分母垂直定位方程
对于行间陈列公式（Display Style），分子基线提升量 $u$ 与分母基线下沉量 $v$ 严格按以下不等式组约束：

$$u = \sigma_8 \quad (\text{num1}), \qquad v = \sigma_{11} \quad (\text{denom1})$$

若分子底部与分数线顶部的垂直间隙小于分数线厚度 $\xi_8$（`default_rule_thickness`）的 3 倍，系统强制将分子基线上推：

$$u \longleftarrow \max\left( u, \; \text{depth}(\text{Numerator}) + \frac{3}{2} \xi_8 + \frac{1}{2}\xi_8 + \sigma_{22} \right)$$

其中 $\sigma_{22}$（`axis_height`）是数学公式的中轴线高度。分数线的中心严格锁定在 $y = \sigma_{22}$ 处，彻底保证了无论左右两边的括号、根号多大，分数线永远与等号、减号的水平中轴绝对重合！

### 2. 上标与下标（Superscripts & Subscripts）空间避让算法
设基字高度为 $h$，深度为 $d$：
* 上标初始抬升量：
  * 在行间公式中：$u = \sigma_{13}$（`sup1`）；
  * 在正文行内公式中：$u = \sigma_{14}$（`sup2`）；
  * 若上标为纯紧缩样式（ScriptScript）：$u = \sigma_{15}$（`sup3`）；
* 下标初始下沉量：$v = \sigma_{16}$（`sub1`）；
* **间隙保护不等式**：当上下标同时存在时，上标底部与下标顶部的垂直净距必须满足：
  $$(u - \text{depth}(\text{Sup})) - (-v + \text{height}(\text{Sub})) \ge 4 \xi_8$$
  若不满足，系统强制将下标进一步向下压低，直到间隙等于 $4 \xi_8$，彻底杜绝了复杂数学符号互相粘连的印刷灾难！

---

## B.5 Python 工业级 TFM 二进制解析器实现

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

## B.6 Omega 虚拟字体（OVF）与复杂排版流水线实战

在多语言排版引擎 Omega 中，虚拟字体技术被推向了前所未有的顶峰：
* **多方向字符映射**：针对从右向左书写的阿拉伯字母或自上而下书写的汉字，OVF 内部的 DVI 字节码能够动态调整画笔移动轴向；
* **动态重音合成**：在经典古希腊语多重变音符（Polytonic Greek，包含锐音符、柔音符、强音符、下标角标等多种符号交叠）中，单一物理字体往往缺少组合字形。OVF 在排版时能够自动计算基字包围盒顶部坐标，并动态将变音符吸附在最佳视学位置，消除了传统 TeX 宏包繁琐的纯宏计算。
