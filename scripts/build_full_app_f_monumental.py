# -*- coding: utf-8 -*-
"""
Builder for Monumental Appendix F: METAFONT and Its Derivatives
Target: ~16,000 characters
"""

content = r"""# 附录 F：METAFONT 与 MetaPost 技术参考指南（METAFONT and Its Derivatives）

*译者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

1977 年，高德纳在构思 TeX 的同时，深刻认识到传统的“点阵像素描画”与“刚性轮廓录入”无法从根本上解决文字随磅重、笔画倾角与纸张墨晕动态演变的排印本质。他开创性地开发了 **METAFONT 语言**，将书法家手中的毛笔与平头硬笔抽象为几何运笔过程，确立了全人类首个**纯声明式数学方程驱动的参数化字体设计范式**。随后，高德纳的弟子约翰·霍比（John Hobby）在此基础上研发了能够直接输出矢量 PostScript 曲线的 **MetaPost** 系统，开源社区更演化出了 MetaFog、METATYPE1 以及由波兰字体大师博古斯瓦夫·雅茨科夫斯基（Bogusław Jackowski）重铸的 Antykwa Półtawskiego 经典字族。

本附录将对 METAFONT 内部声明式方程求解器的线性代数机制、画笔包络线微分几何理论、转向数定理（Turning Number Theorem）、Computer Modern 家族全部 62 个神圣设计参数词典以及从参数化源文件向现代矢量字体转化的 MF2PT1 流水线进行深度解构。

---

## F.1 METAFONT 编程语言与声明式几何方程求解器

在 METAFONT 代码中，设计师从来不以过程式命令赋值坐标（如传统编程中的 `x = 5; y = 10`），而是直接书写一组平等的联立代数方程：

```metafont
x1 = x2 + 0.5w;
y1 = y2 = 0.5h;
z1 - z2 = whatever * (dir 30);
z3 = 0.5[z1, z2];
```

METAFONT 解释器内部运行着一个极其高效的**动态符号线性方程求解机（Linear Equation Solver）**：

::: tip METAFONT 方程求解网络与未定元胶囊（Capsule）环（Figure F-1, F-2）
![METAFONT 方程网络（Figure F-1）](/images/fonts-encodings/fig-app-f1.png)
*METAFONT 方程网络（Figure F-1）*
:::

*图 F-1：METAFONT 内部变量依赖拓扑。每个未定未知数被包装为一个“胶囊（Capsule）”，并在内存中维护一个双向依赖环。*

::: tip 线性代数高斯消元与解空间坍缩（Figure F-2）
![高斯消元解空间（Figure F-2）](/images/fonts-encodings/fig-app-f2.png)
*高斯消元解空间（Figure F-2）*
:::

*图 F-2：当新的线性约束输入时，解释器立即执行高斯-约旦消元法（Gauss-Jordan Elimination）：将已知变量代入其余胶囊，缩减未知自由度，直到整个几何系统完全定解。*

### 1. 核心符号表示理论
每个内部数值被表示为一个仿射线性多项式：

$$V = c_0 + c_1 X_1 + c_2 X_2 + \dots + c_k X_k$$

* 当用户声明 `z1 = z2 + (10, 20)` 时，系统并不强求立即知道 $z1$ 或 $z2$ 的绝对坐标，而是建立等式约束：$X_{z1} - X_{z2} = 10$ 与 $Y_{z1} - Y_{z2} = 20$；
* 解释器实时检测方程组的秩（Rank）：若方程出现矛盾则报错报告过度约束（Inconsistent equation）；若自由度未满，程序继续向下解析，直到后续代码提供了足够的几何切线或边界约束，整个方程网络瞬间坍缩收敛出唯一的精确浮点解！

### 2. 小写字母 'n' 的纯数学参数化设计实战

以下源码展示了如何用 METAFONT 严密书写一个带双立柱衬线、平滑拱门与动态笔宽的小写拉丁字母 'n'：

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

#### 循环测试字重演进：
只需包裹一层 `for` 循环，令 `stem = (i/63)[join, 2.2u]`，METAFONT 便能在一瞬间自动生成 64 档从 Hairline 到 Ultra-Black 的极其饱满匀称的字重连续变体！

---

## F.2 画笔几何学（Penspeck）与包络线光栅化

与现代字体将字形视为由空心多边形轮廓构成的“皮囊”不同，METAFONT 认为**文字是由一支具有特定物理几何形状的画笔（Pen）沿着一条骨架轨迹（Path）运动而扫掠出的实体墨迹**！

::: tip 凸多边形画笔 Penspeck 离散网格化（Figure F-3, F-4）
![Penspeck 画笔结构（Figure F-3）](/images/fonts-encodings/fig-app-f3.png)
*Penspeck 画笔结构（Figure F-3）*
:::

*图 F-3：画笔规范体 `penspeck` 的离散化。椭圆画笔首先被投影并多边形化为由一系列网格偏移向量构成的离散凸包（Convex Hull）。*

::: tip 画笔扫掠包络线（Envelope Tracing）微积分模型（Figure F-4）
![画笔包络线微分轨迹（Figure F-4）](/images/fonts-encodings/fig-app-f4.png)
*画笔包络线微分轨迹（Figure F-4）*
:::

*图 F-4：包络线微分方程：当具有中心点 $\mathbf{z}(t)$ 与凸包顶点 $\mathbf{v}_i$ 的画笔沿轨迹行进时，墨迹边界由外侧切线法向量决定。*

数学上，画笔扫掠区域（Envelope）的外边缘曲线方程为：

$$\mathcal{E}(t) = \mathbf{z}(t) + \mathbf{v}_{\text{active}}(t)$$

其中活动顶点 $\mathbf{v}_{\text{active}}(t)$ 满足：画笔在该顶点处的向外法向量与骨架曲线在 $t$ 时刻的切线向量严格平行！高德纳设计了精妙的包络线追踪算法（Envelope Tracing Algorithm），将该微积分过程无缝映射为离散 Bresenham 直线与圆弧生成器的协同运笔。

---

## F.3 转向数定理（Turning Number Theorem）与拓扑环绕数

在评估复杂封闭贝塞尔轮廓的有效性与合法性时，METAFONT 引入了微分拓扑学中的**转向数定理（Turning Number Theorem）**：

::: tip 转向数定理与自相交环绕拓扑（Figure F-5, F-6）
![转向数拓扑判定（Figure F-5）](/images/fonts-encodings/fig-app-f5.png)
*转向数拓扑判定（Figure F-5）*
:::

*图 F-5：平面光滑闭曲线 $\mathcal{C}$ 切线向量在单位圆上的高斯映射（Gauss Map）。切线向量沿曲线完整遍历一圈所旋转的总角度，必须是 $2\pi$ 的整数倍！*

::: tip 曲线拓扑奇异点与尖点消除（Figure F-6）
![曲线奇异点自愈（Figure F-6）](/images/fonts-encodings/fig-app-f6.png)
*曲线奇异点自愈（Figure F-6）*
:::

*图 F-6：当曲线发生自相交（Self-intersection）或出现曲率无限大的奇异尖点（Cusps）时，转向数发生突变，METAFONT 自动启动切分与外轮廓布尔提取。*

对于一条无自相交的简单正向闭合路径，其全总曲率积分恒等于 $2\pi$（转向数 $T = +1$）：

$$\frac{1}{2\pi} \oint_\mathcal{C} \kappa(s) \, ds = T \in \mathbb{Z}$$

这一严格的数学判据，使 METAFONT 能够自动识别轮廓是外边界还是内镂空孔洞（如字母 'O' 的内部），并在光栅化时彻底杜绝翻转走样的发生。

---

## F.4 Computer Modern 字体家族 62 维全量参数参考词典

Computer Modern（CM）是高德纳采用 METAFONT 编写的经典字体家族。整个庞大的字族（包含 75 款独立字库，覆盖 5pt 到 17pt 的光学比例尺）全部由一组定义在 `cmbase.mf` 与各个字体驱动文件中的宏观几何参数所控制。

### 1. 垂直尺寸与高度参数（Vertical Dimensions）
* `u#`：基本设计单位宽度（Unit width in sharp units / points）；
* `width_corr#`：字符宽度微调补偿量；
* `x_height#`：小写字母 'x' 的主干高度（Ex-height）；
* `cap_height#`：大写正文字母高度（Cap height）；
* `asc_height#`：小写字母升部高度（如 'b', 'd', 'h' 的顶部）；
* `desc_depth#`：小写字母降部深度（如 'p', 'q', 'y' 的底部）；
* `body_height#`：带重音大写字母或最高括号的极限包围盒顶部；
* `fig_height#`：等宽阿拉伯数字的标准高度；
* `math_axis#`：数学符号中轴线高度（分数线与加减号的中心高度）；
* `bar_height#`：小写字母 'e' 的横梁高度与字母 'A', 'H' 的交叉横杠高度；
* `comma_depth#`：逗号与分号尾巴探入基线以下的深度。

### 2. 主干与笔画宽度参数（Stem and Stroke Widths）
* `hair#`：最细衬线或连接线画笔直径（Hairline thickness）；
* `stem#`：小写正文字母主垂直干笔画宽度（Main vertical stem）；
* `curve#`：小写圆弧字母弯角处最大膨胀宽度（如字母 'o', 'c' 的两侧最厚处）；
* `ess#`：字母 's' 中部倾斜主梁的最厚宽度；
* `flare#`：水滴状笔画端点（Teardrop terminal）的球头最大直径（如字母 'a', 'c', 'f', 'r' 的端部）；
* `dot_size#`：小写字母 'i', 'j' 上方圆点与标点句号的直径；
* `cap_hair#`：大写字母最细笔画厚度；
* `cap_stem#`：大写字母主垂直干笔画宽度；
* `cap_curve#`：大写圆弧字母两侧最大弧厚（如字母 'O', 'C', 'G'）；
* `cap_ess#`：大写字母 'S' 中部斜干最大厚度；
* `rule_thickness#`：数学公式分数线与方框线条的标准物理厚度；
* `thin_join#`：对角斜线交叉连接处的极小理论过渡宽度。

### 3. 衬线与括号连接参数（Serifs and Brackets）
* `dish#`：衬线底部的凹陷微弧度（Serif dish curvature）；
* `bracket#`：衬线与主干之间的过渡圆角支架高度（Serif bracket height）；
* `jut#`：小写字母水平衬线向外挑出的水平长度（Serif protrusion）；
* `cap_jut#`：大写字母衬线外挑长度；
* `beak_jut#`：大写字母 'E', 'F', 'T' 臂部尖喙（Beak）向外突出的水平长度；
* `beak#`：尖喙的垂直切削深度；
* `serif_drop#`：单向悬挂衬线向下滑落的垂直距离；
* `stem_corr#`：小写字母主干交汇处的切入收缩量；
* `vair_corr#`：细笔画在连接拐角处的补偿膨胀量；
* `slab#`：粗衬线字体（Slab Serif）中方形水平衬线的厚度；
* `cap_bar#`：大写字母横杠厚度；
* `cap_band#`：大写字母封闭环带厚度；
* `cap_notch_cut#`：大写字形锐角内侧为了防止墨水堆积而切除的凹槽深度（Notch cut）。

### 4. 光学修正与高级形态参数（Optical Corrections & Style）
* `o#`：曲线或尖角在越过基线或顶线时的光学过冲量（Overshoot），消除人眼视觉缩小错觉；
* `apex_o#`：大写字母 'A', 'V', 'W' 尖顶或尖底处的额外过冲量；
* `apex_corr#`：尖顶点连接处的几何回缩修正；
* `slant`：字体的倾斜率 $\tan(\theta)$（正体为 0.0，斜体通常为 0.25）；
* `fudge`：针对低分辨率或特殊黑度的全比例缩放软调整因子；
* `math_spread`：数学公式符号之间的垂直松弛度；
* `superness`：超椭圆参数（Superellipse factor），控制曲线饱满度（通常 $0.707 \dots 0.75$）；
* `superpull`：超椭圆内侧向内吸附拉扯的修正系数；
* `beak_darkness`：尖喙区域黑度衰减权重。

### 经典 CM 字形在 10 磅下的参数对拍表（CMR10 vs CMBX10 vs CMTI10 vs CMSS10 vs CMTT10）：

| 参数名 | `cmr10`（正体） | `cmbx10`（粗体） | `cmti10`（西文斜体） | `cmss10`（无衬线） | `cmtt10`（等宽打字机） |
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

## F.5 MetaPost、MetaFog 与现代矢量转换管线

1990 年代，约翰·霍比在 MetaPost 中用三次样条曲线平滑求解器替换了 METAFONT 的点阵光栅化模块，使其能够直接生成工业级的 EPS（Encapsulated PostScript）矢量输出。

### 1. MetaFog：从轮廓到骨架的矢量重构
理查德·柯施（Richard Kinch）开发了著名的 MetaFog 引擎：
* 拦截 METAFONT 生成的高分辨率点阵位图；
* 对离散像素进行多项式边界拟合与拐点提取；
* 将离散的黑色墨迹还原为光滑的三次贝塞尔曲线。

### 2. MF2PT1 与 Antykwa Półtawskiego 革命
波兰著名字体工程师博古斯瓦夫·雅茨科夫斯基与雅努什·诺瓦茨基（Janusz M. Nowacki）推出了 **METATYPE1** 架构，并以此成功重铸了波兰国家级经典字族 Antykwa Półtawskiego：
1. 运行 MetaPost 解析带有提示锚点的 METAFONT 源码，生成无损的 PostScript 贝塞尔矢量轮廓；
2. 提取源码中定义的极值点与笔画特征，自动将其转换为 PostScript Type 1 规范的 `hstem` 与 `vstem` 提示；
3. 将字符轮廓打包入 Type 1 二进制格式，使古老而深奥的 METAFONT 参数化书法字库，彻底无缝融入当今现代桌面的 OpenType 与 PDF 矢量印刷工作流！
"""

with open('scripts/app_builders/app_f.md', 'w', encoding='utf-8') as f:
    f.write(content.strip() + '\n')
print("Successfully written scripts/app_builders/app_f.md, total length:", len(content))

# Update build_app_f.py
py_f = """# -*- coding: utf-8 -*-
import os

def get_appendix_f():
    p = os.path.join(os.path.dirname(__file__), 'app_f.md')
    with open(p, 'r', encoding='utf-8') as f:
        return f.read()
"""
with open('scripts/app_builders/build_app_f.py', 'w', encoding='utf-8') as f:
    f.write(py_f)
print("Updated build_app_f.py")
