# 附录 G：字型设计中的曲线微分几何学与样条数学理论（Differential Geometry of Curves）

*译者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

在现代矢量字体工程中，字符轮廓并非简单的折线拼接，而是建立在极其严密的微分几何学与代数拓扑学基础之上。从 TrueType 采用的二次有理贝塞尔曲线（Quadratic Bézier），到 PostScript Type 1 与 OpenType CFF 采用的三次贝塞尔曲线（Cubic Bézier），再到高端书法设计中的欧拉螺线（Euler Spirals / Cornu Spirals），字体设计师在屏幕上拖动控制点所施加的每一个微小位移，都在底层激发了一场高阶张量与微积分方程的精密运算。

本附录将对字型设计涉及的核心微分几何学理论进行完整的纯数学解析：从伯恩斯坦基底（Bernstein Basis）的单位分解定理、极式（Blossom）映射、德卡斯特里奥（de Casteljau）递归细分算法、微分矢端曲线（Hodograph），到曲率公式（Curvature）、拐点（Inflection Points）判定与等距偏移曲线（Offset Curves）的非有理本质，以及欧拉角螺线在现代参数化字体轮廓拟合中的前沿应用。

---

## G.1 伯恩斯坦多项式基底与代数拓扑性质

一条定义在参数区间 $t \in [0, 1]$ 上的 $n$ 次贝塞尔曲线，在数学上定义为 $n+1$ 个几何控制点 $\mathbf{P}_0, \mathbf{P}_1, \dots, \mathbf{P}_n \in \mathbb{R}^2$ 关于 $n$ 次**伯恩斯坦基多项式（Bernstein Polynomials）**的凸组合线性叠加：

$$\mathbf{B}(t) = \sum_{i=0}^n B_{i,n}(t) \, \mathbf{P}_i, \quad t \in [0, 1]$$

其中 $n$ 次伯恩斯坦基函数由二项式系数与乘幂严格定义为：

$$B_{i,n}(t) = \binom{n}{i} t^i (1-t)^{n-i}, \quad i = 0, 1, \dots, n$$

这里 $\binom{n}{i} = \frac{n!}{i!(n-i)!}$ 为组合二项式系数。

### 核心微分几何定理与严格证明

#### 定理 1：单位分解性（Partition of Unity）
在全实数域上，所有 $n$ 次伯恩斯坦多项式的代数和恒等为 1：

$$\sum_{i=0}^n B_{i,n}(t) \equiv 1, \quad \forall t \in \mathbb{R}$$

*证明*：根据牛顿二项式定理（Binomial Theorem），对于任意实数 $a, b$，恒有 $(a + b)^n = \sum_{i=0}^n \binom{n}{i} a^i b^{n-i}$。令 $a = t$ 且 $b = 1-t$，则有：
$$\sum_{i=0}^n B_{i,n}(t) = \sum_{i=0}^n \binom{n}{i} t^i (1-t)^{n-i} = (t + (1-t))^n = 1^n = 1 \quad \blacksquare$$

**字型排印物理学意义**：单位分解性确保了贝塞尔曲线具有**仿射不变性（Affine Invariance）**！无论我们对字库进行整体平移、旋转、缩放还是施加倾斜矩阵变换，直接对控制点施加变换后的新曲线，与原曲线上每个点分别计算变换后的结果在数学上严格绝对重合！

#### 定理 2：非负性（Positivity）
当且仅当参数 $t$ 落在字形轮廓的合法物理区间 $[0, 1]$ 内时，所有基函数恒为非负：

$$B_{i,n}(t) \ge 0, \quad \forall t \in [0, 1]$$

结合定理 1，这证明了曲线上的任意一点 $\mathbf{B}(t)$ 都是控制多边形顶点的**真凸组合（Convex Combination）**，从而严格证明了**凸包性质（Convex Hull Property）**：整条字形轮廓线被严格约束在控制点围成的凸多边形内部，渲染引擎可借此实现毫秒级快速包围盒粗筛求交！

#### 定理 3：端点插值与边界切线控制（Endpoint Interpolation）
代入 $t = 0$ 与 $t = 1$，有：
$$\mathbf{B}(0) = \mathbf{P}_0, \quad \mathbf{B}(1) = \mathbf{P}_n$$
曲线在起点的切线方向平行于向量 $\mathbf{P}_1 - \mathbf{P}_0$，在终点的切线方向平行于向量 $\mathbf{P}_n - \mathbf{P}_{n-1}$。这一极其优美的几何性质，赋予了字体设计师通过直接移动前后控制点把控曲线两端连接切线的绝对权力。

#### 定理 4：递推关系与微分性质（Recurrence & Derivatives）
$$B_{i,n}(t) = (1-t) B_{i,n-1}(t) + t B_{i-1,n-1}(t)$$
$$\frac{d}{dt} B_{i,n}(t) = n \left( B_{i-1,n-1}(t) - B_{i,n-1}(t) \right)$$

---

## G.2 极式（Blossoms / Polar Forms）与多线性映射理论

由法国数学家保罗·德卡斯特里奥与拉马尔·拉姆齐（Lyle Ramshaw）提出的**极式（Polar Form，或称 Blossom 花式）理论**，将抽象繁琐的贝塞尔曲线代数运算彻底转化为优美纯粹的多线性仿射几何学。

对于一条 $n$ 次单变量多项式曲线 $\mathbf{P}(t)$，存在唯一一个关于 $n$ 个独立变量的对称多重仿射函数（Symmetric Multiaffine Map） $p(u_1, u_2, \dots, u_n)$，满足以下三大公理：
1. **全对称性（Symmetry）**：交换任意两个输入参数的次序，函数值严格不变：
   $$p(u_{\pi(1)}, u_{\pi(2)}, \dots, u_{\pi(n)}) = p(u_1, u_2, \dots, u_n)$$
2. **多重仿射性（Multiaffinity）**：固定其中任意 $n-1$ 个变量，关于剩余的一个变量是纯粹的仿射线性映射：
   $$p(\dots, \, (1-\alpha)u + \alpha v, \, \dots) = (1-\alpha) p(\dots, u, \dots) + \alpha p(\dots, v, \dots)$$
3. **对角坍缩性（Diagonal Property）**：当所有 $n$ 个参数全部取同一数值 $t$ 时，极式瞬间坍缩为原始贝塞尔曲线本身：
   $$p(t, t, \dots, t) = \mathbf{P}(t)$$

### 极式视角的控制点黄金对应律：
曲线的几何控制点 $\mathbf{P}_i$，在极式空间中具有令人惊叹的离散端点取值表达：

$$\mathbf{P}_i = p(\underbrace{0, \dots, 0}_{n-i \text{ 个}}, \, \underbrace{1, \dots, 1}_{i \text{ 个}})$$

例如对于三次贝塞尔曲线（$n=3$）：
* 起点：$\mathbf{P}_0 = p(0, 0, 0)$；
* 第一控制点：$\mathbf{P}_1 = p(0, 0, 1)$；
* 第二控制点：$\mathbf{P}_2 = p(0, 1, 1)$；
* 终点：$\mathbf{P}_3 = p(1, 1, 1)$。

在子区间 $[a, b]$ 上对曲线进行局部截取时，新曲线的控制点只需直接求值 $p(a, a, a), p(a, a, b), p(a, b, b), p(b, b, b)$，彻底终结了繁琐的坐标变换公式！

---

## G.3 升阶代数矩阵：从二次 TrueType 到三次 PostScript

在字体格式跨平台转换中，将 TrueType（二次贝塞尔曲线，$n=2$）转换为 PostScript Type 1 / OpenType CFF（三次贝塞尔曲线，$n=3$）是一项核心基础操作。**升阶（Degree Elevation）必须保证曲线在几何形状、切线方向与曲率上绝对恒定**。

### 升阶通用递推公式：
将 $n$ 次曲线升为 $n+1$ 次曲线，新的控制点 $\mathbf{P}_i^{(n+1)}$ 由旧控制点线性组合得出：

$$\mathbf{P}_i^{(n+1)} = \frac{i}{n+1} \mathbf{P}_{i-1}^{(n)} + \left(1 - \frac{i}{n+1}\right) \mathbf{P}_i^{(n)}, \quad i = 0, 1, \dots, n+1$$

### 二次转三次升阶封闭解：
设二次 TrueType 曲线由起点 $\mathbf{P}_0$、脱线控制点 $\mathbf{P}_1$ 与终点 $\mathbf{P}_2$ 定义，升阶为三次曲线后的四个控制点 $\mathbf{Q}_0, \mathbf{Q}_1, \mathbf{Q}_2, \mathbf{Q}_3$ 精确等于：

$$\begin{cases}
\mathbf{Q}_0 = \mathbf{P}_0 \\
\mathbf{Q}_1 = \mathbf{P}_0 + \frac{2}{3}(\mathbf{P}_1 - \mathbf{P}_0) = \frac{1}{3}\mathbf{P}_0 + \frac{2}{3}\mathbf{P}_1 \\
\mathbf{Q}_2 = \mathbf{P}_2 + \frac{2}{3}(\mathbf{P}_1 - \mathbf{P}_2) = \frac{2}{3}\mathbf{P}_1 + \frac{1}{3}\mathbf{P}_2 \\
\mathbf{Q}_3 = \mathbf{P}_2
\end{cases}$$

此公式在数学上严谨证明了：**任何二次贝塞尔曲线均可以毫无任何误差、100% 精确地表达为一条三次贝塞尔曲线**！反之，三次曲线由于自由度更高（具有两个独立控制点，可能包含拐点），通常无法用单一二次曲线精确表示，必须通过曲率极值点分割算法切断为多段二次曲线逼近。

---

## G.4 德卡斯特里奥（de Casteljau）递归细分算法

在光栅化碰撞检测、字符曲线相交运算与局部裁剪时，德卡斯特里奥算法提供了数值上极度稳定的几何细分手段。

### 细分三角形金字塔算法：
给定参数 $t_0 \in (0, 1)$，定义点序列的递归线性插值：

$$\mathbf{P}_i^{(k)}(t_0) = (1-t_0)\mathbf{P}_i^{(k-1)}(t_0) + t_0 \mathbf{P}_{i+1}^{(k-1)}(t_0)$$

其中 $\mathbf{P}_i^{(0)} = \mathbf{P}_i$ 为原始控制点。当 $k=n$ 时，顶峰点 $\mathbf{P}_0^{(n)}(t_0) = \mathbf{B}(t_0)$ 即为曲线上对应点的物理坐标。

细分完成后，原始曲线在 $t_0$ 处被切断为两段独立的子贝塞尔曲线：
* 左段曲线控制点序列：$\mathbf{P}_0^{(0)}, \mathbf{P}_0^{(1)}, \mathbf{P}_0^{(2)}, \dots, \mathbf{P}_0^{(n)}$；
* 右段曲线控制点序列：$\mathbf{P}_0^{(n)}, \mathbf{P}_1^{(n-1)}, \mathbf{P}_2^{(n-2)}, \dots, \mathbf{P}_n^{(0)}$。

#### Python 工业级德卡斯特里奥细分实现：
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

### 变分缩减性质（Variation Diminishing Property）：
**贝塞尔曲线的波动幅度绝不会超过其控制多边形！** 任何一条直线与贝塞尔曲线轮廓的实际交点个数，恒小于等于该直线与对应控制多边形折线的交点个数。该定理彻底保证了字体设计师在调整控制点时，轮廓绝不会莫名其妙地产生多余的寄生波纹与褶皱震荡！

---

## G.5 微分矢端曲线（Hodograph）与速度加速度张量

贝塞尔曲线的各阶导数本身**依然是一条纯粹的贝塞尔曲线**！其控制向量构成了几何学上的**矢端曲线（Hodograph）**。

### 一阶导数（速度向量 / 切线向量）：
$$\mathbf{B}'(t) = n \sum_{i=0}^{n-1} B_{i,n-1}(t) \, (\mathbf{P}_{i+1} - \mathbf{P}_i)$$

* 曲线在起点的切线方向恒平行于向量 $\mathbf{P}_1 - \mathbf{P}_0$；
* 曲线在终点的切线方向恒平行于向量 $\mathbf{P}_n - \mathbf{P}_{n-1}$。

### 二阶导数（加速度向量）：
$$\mathbf{B}''(t) = n(n-1) \sum_{i=0}^{n-2} B_{i,n-2}(t) \, (\mathbf{P}_{i+2} - 2\mathbf{P}_{i+1} + \mathbf{P}_i)$$

二阶导向量反映了字形轮廓在行进过程中偏离直线的弯曲加速度，直接决定了下文的曲率演变。

---

## G.6 平面曲线曲率（Curvature）与微分不变量

曲率 $\kappa(t)$ 是衡量字体轮廓在某一点弯曲程度的核心不变量，其物理意义为单位弧长内切线方向角的旋转变化率：

$$\kappa(t) = \frac{x'(t)y''(t) - y'(t)x''(t)}{\left(x'(t)^2 + y'(t)^2\right)^{3/2}}$$

* **曲率半径（Radius of Curvature）**：$R(t) = \frac{1}{|\kappa(t)|}$；
* **密切圆（Osculating Circle）**：在点 $\mathbf{B}(t)$ 处沿法向量向内偏移 $R(t)$ 处的圆，与曲线在该点具有二阶切触精度；
* **拐点（Inflection Point）**：曲率变号的位置，即分子 cross product 恒等于零之处：
  $$x'(t)y''(t) - y'(t)x''(t) = 0$$
  在高质量字形设计中，二次贝塞尔曲线由于二阶导数恒为常数向量，其内部**绝对不可能出现拐点**；三次贝塞尔曲线内部**最多只能存在一个拐点**！若字符设计需要呈现“S”形平滑波浪，必须确保该拐点处的二阶曲率保持 $G^2$ 连续（曲率数值大小与正负无缝衔接），否则人眼在反射光影下会察觉到极度刺眼的“断腰”视觉残瑕！
* **奇异尖点（Cusps）**：当一阶速度向量同时归零时：$x'(t) = y'(t) = 0$。曲率在此处退化，切线发生 $180^\circ$ 倒转。

---

## G.7 等距偏移曲线（Offset Curves）的非多项式物理本质

在字体加粗（Stroke Boldening）、空心字生成（Outline Stroke）以及字形轮廓膨胀算法中，排版引擎需要沿法线方向将曲线向外推挤 $\delta$ 距离，生成**等距偏移曲线（Offset Curve / Parallel Curve）**：

$$\mathbf{C}_\delta(t) = \mathbf{C}(t) + \delta \, \mathbf{n}(t) = \mathbf{C}(t) + \delta \, \frac{\left(-y'(t), \, x'(t)\right)}{\sqrt{x'(t)^2 + y'(t)^2}}$$

### 字体工程中的终极难题：偏移曲线的非有理本质
计算机辅助几何设计（CAGD）领域的一个著名残酷定理指出：**除了平凡的直线段与圆弧之外，任何多项式贝塞尔曲线的等距偏移曲线，在数学上绝对不可能再用有限阶的有理贝塞尔曲线精确表示！**

其根源在于法向量分母中的平方根项 $\sqrt{x'(t)^2 + y'(t)^2}$ 引入了不可约化的代数分支割线。不仅如此，当偏移距离 $\delta$ 超过局部最小曲率半径 $R(t)$ 时，偏移曲线内部必然会产生极其诡异的**燕尾自相交奇异点（Swallowtail Singularities）**！

现代专业字体设计软件（如 FontLab、Glyphs、FontForge）在执行“扩大笔画轮廓”时，必须调用高阶数值逼近管线：
1. 计算曲率极大值点，将原始曲线切分为单调曲率段；
2. 依据 Tiller-Hanson 算法，在每段曲线两端估算法向量偏移控制点；
3. 检测并执行微分拓扑裁剪，彻底消除燕尾自交环；
4. 最终以微米级公差拟合出平滑封闭的高品质 OpenType 矢量轮廓。

---

## G.8 欧拉角螺线（Euler Spirals / Cornu Spirals）与现代样条

在传统三次贝塞尔曲线中，曲线的曲率通常是参数 $t$ 的高阶有理分式，其曲率分布极难保持单调或线性变化，往往导致字形高光反射线呈现轻微的扭曲（称为“曲率抖动”）。

为了追求终极的书法级光学平滑度，拉夫·莱维恩（Raph Levien）在设计 Spiro 样条引擎时，引入了经典力学与光学中的**欧拉螺线（又称柯奴螺线，Cornu Spirals / Clothoids）**。

### 欧拉螺线核心物理方程：
欧拉螺线的几何本质在于：**曲线的曲率 $\kappa$ 与弧长 $s$ 严格成正比**！

$$\kappa(s) = \frac{d\theta}{ds} = 2 a s$$

对弧长进行积分，得到切线倾角方程：

$$\theta(s) = \int_0^s \kappa(u) \, du = a s^2$$

在笛卡尔坐标系中，欧拉螺线的参数方程由著名的菲涅耳积分（Fresnel Integrals）严格定义：

$$x(s) = \int_0^s \cos(a u^2) \, du, \quad y(s) = \int_0^s \sin(a u^2) \, du$$

由于曲率随弧长完美线性渐变，两个由欧拉螺线连接的几何线段天然具备绝对完美的 $G^2$ 甚至 $G^3$ 连续性。现代前沿字体设计工具先通过欧拉螺线建立全局美学骨架，再将其自适应切分转化为标准 OpenType 三次贝塞尔曲线，实现了古代书法艺术与现代微分几何学的最高统一。
---

## G.9 几何光滑度连续性阶次（Continuity Classes: $C^k$ vs $G^k$）

在高质量字体轮廓拼接（Spline Joining）中，两个相邻贝塞尔曲线段在连接点处的平滑度，划分为**参数连续性（Parametric Continuity, $C^k$）**与**几何连续性（Geometric Continuity, $G^k$）**两大流派：

### 1. 各级连续性的微分定义：
* **$C^0$ / $G^0$ 连续（位置连续）**：两曲线段首尾相接，共用同一点：$\mathbf{B}_1(1) = \mathbf{B}_2(0)$；
* **$C^1$ 连续（一阶导数连续）**：两曲线不仅切线方向重合，且一阶导数向量的大小与方向完全相等：$\mathbf{B}_1'(1) = \mathbf{B}_2'(0)$；
* **$G^1$ 连续（切线方向连续）**：两曲线在连接点处的单位切向量平行，但模长允许不相等：
  $$\frac{\mathbf{B}_1'(1)}{\|\mathbf{B}_1'(1)\|} = \frac{\mathbf{B}_2'(0)}{\|\mathbf{B}_2'(0)\|}$$
  在字型设计中，这意味着控制点 $\mathbf{P}_2$、端点 $\mathbf{P}_3 = \mathbf{Q}_0$ 与后一曲线控制点 $\mathbf{Q}_1$ **三点严格共线**，但线段长度比可以任意调整；
* **$C^2$ 连续（二阶导数连续）**：两曲线的二阶导数向量严格相等：$\mathbf{B}_1''(1) = \mathbf{B}_2''(0)$；
* **$G^2$ 连续（曲率连续，Curvature Continuity）**：两曲线在连接点处的**曲率数值与曲率中心严格连续**：
  $$\kappa_1(1) = \kappa_2(0)$$

### 2. 为什么专业字体设计必须追求 $G^2$ 连续？
人眼视觉感知对曲率的跳跃极其敏感。在仅仅满足 $G^1$ 连续的轮廓连接处（例如圆弧平整过渡到直线的传统倒角），虽然切线没有折角，但曲率从常数（$1/R$）瞬间断崖式跌落到直线的 0。在屏幕光栅化或印刷高光下，人眼会在该拐角处清晰察觉到一条刺眼的暗影折痕（称为“光学断骨”）。

通过调节控制点使曲线在交界处达成 $G^2$ 连续，字形轮廓的曲率梳（Curvature Comb）将呈现连续光滑演变，赋予字符如水银泻地般的有机书法美感！

---

## G.10 基于矢端极值点求根的极限包围盒（BBox）极速求值算法

在字体渲染管线中，精确计算字符曲线在 X 轴与 Y 轴上的极限包围盒（Bounding Box: $x_{\min}, y_{\min}, x_{\max}, y_{\max}$）是一项每秒触发数万次的极高频操作。

由于贝塞尔曲线可能在区间内部向外隆起凸出，极限坐标并不一定出现在端点处，而是可能出现在一阶导数等于零的**极值驻点（Stationary Points）**处！

### 三次贝塞尔导数二次方程求解：
一阶导数方程 $x'(t) = 0$ 展开为一个一元二次多项式：

$$x'(t) = 3(1-t)^2(x_1 - x_0) + 6(1-t)t(x_2 - x_1) + 3t^2(x_3 - x_2) = A t^2 + B t + C = 0$$

其中系数展开为：

$$\begin{cases}
A = 3(-x_0 + 3x_1 - 3x_2 + x_3) \\
B = 6(x_0 - 2x_1 + x_2) \\
C = 3(x_1 - x_0)
\end{cases}$$

利用求根公式求出判别式 $\Delta = B^2 - 4AC$。若 $\Delta \ge 0$，求出实数根 $t = \frac{-B \pm \sqrt{\Delta}}{2A}$。筛选出落在区间 $(0, 1)$ 内部的合法根代入 $x(t)$ 求值，与端点 $x(0), x(1)$ 共同取极值，即可在 $O(1)$ 时间内以纳秒级速度算出绝对精确的字形像素包围盒！
---

## G.11 贝塞尔剪裁算法（Bézier Clipping）与高速几何求交

在字体光栅化渲染、轮廓布尔运算（Boolean Union/Difference）以及轮廓重叠消除（Remove Overlap）中，两段三次贝塞尔曲线 $\mathbf{P}(t)$ 与 $\mathbf{Q}(u)$ 的空间求交点是计算几何中最昂贵的操作之一。

传统牛顿迭代法由于高度依赖初始猜测值，在面对多交点或切触点时极易发散。由西德伯格（Sederberg）与西村（Nishita）提出的 **贝塞尔剪裁算法（Bézier Clipping）**，以几何凸包收缩代替纯代数迭代，实现了超级稳定的超二次收敛速度：

### 算法几何步骤：
1. **建立局部坐标系**：连接曲线 $\mathbf{P}$ 的起点 $\mathbf{P}_0$ 与终点 $\mathbf{P}_3$ 构筑基准弦线 $L$，计算每个控制点距直线 $L$ 的正负带符号垂直距离 $d_0, d_1, d_2, d_3$；
2. **构建一维隐式距离函数**：构造一维距离函数 $d(t) = \sum_{i=0}^3 B_{i,3}(t) d_i$，其与横轴的交点即为曲线 $\mathbf{P}$ 与直线 $L$ 的交点；
3. **凸多边形剪裁**：在参数平面 $(u, d)$ 上，绘制第二条曲线 $\mathbf{Q}(u)$ 关于距离轴的凸包，计算该凸包与 $d=0$ 轴相交的最小与最大参数区间 $[u_{\min}, u_{\max}]$；
4. **区间修剪**：将参数区间 $[0, 1]$ 瞬间裁剪缩小至 $[u_{\min}, u_{\max}]$。通过德卡斯特里奥算法截取子曲线，交替对两曲线重复执行，通常仅需 3 至 4 轮迭代，交点参数即可收敛至浮点机极限精度（$10^{-12}$）！

---

## G.12 极式（Blossom）多线性公理的严密代数构造

为了彻底理解极式 $p(u_1, u_2, \dots, u_n)$ 的数学本质，我们给出从单变量单项式基底向多线性对称极式转化的代数构造律：

对于任意单项式 $t^k$（其中 $0 \le k \le n$），其对应的 $n$ 元极式为基本对称多项式除以组合数：

$$\mathcal{B}[t^k] \, (u_1, u_2, \dots, u_n) = \frac{1}{\binom{n}{k}} \sum_{1 \le j_1 < j_2 < \dots < j_k \le n} u_{j_1} u_{j_2} \dots u_{j_k}$$

### 三次多项式极式展开全貌：
对于三次曲线 $\mathbf{P}(t) = \mathbf{a}_0 + \mathbf{a}_1 t + \mathbf{a}_2 t^2 + \mathbf{a}_3 t^3$，其关于三个独立变量 $u_1, u_2, u_3$ 的唯一极式为：

$$p(u_1, u_2, u_3) = \mathbf{a}_0 + \frac{\mathbf{a}_1}{3}(u_1 + u_2 + u_3) + \frac{\mathbf{a}_2}{3}(u_1 u_2 + u_2 u_3 + u_3 u_1) + \mathbf{a}_3 u_1 u_2 u_3$$

#### 代数检验：
1. **对称性**：显然，交换 $u_1, u_2, u_3$ 中任意两者的次序，上式各项完全对称不变；
2. **多重仿射性**：固定 $u_2, u_3$ 时，关于 $u_1$ 是形如 $A u_1 + B$ 的严格一次多项式；
3. **对角坍缩**：令 $u_1 = u_2 = u_3 = t$，有：
   $$p(t, t, t) = \mathbf{a}_0 + \frac{\mathbf{a}_1}{3}(3t) + \frac{\mathbf{a}_2}{3}(3t^2) + \mathbf{a}_3 t^3 = \mathbf{a}_0 + \mathbf{a}_1 t + \mathbf{a}_2 t^2 + \mathbf{a}_3 t^3 = \mathbf{P}(t)$$

极式理论的创立，不仅为计算机字体几何学提供了最坚固的代数奠基石，更将曲线微积分完全转化为优雅的多项式组合对称学，成为了全人类计算机图形学与几何设计皇冠上最璀璨的明珠。
---

## G.13 欧拉角螺线在现代排印工程学中的终极统一

在现代字型设计工具（如 FontForge 的 Spiro 模式与 Glyphs 的曲线平滑插件）中，欧拉螺线（Cornu Spiral）的工程实现基于拉夫·莱维恩的有限元求解器：
* 字体设计师只需在字母转角处放置若干个离散锚点并指定端点切线；
* Spiro 引擎自动求解变分泛函最小化问题（Minimum Energy Curve）：
  $$E = \int \left( \frac{d\kappa}{ds} \right)^2 ds \longrightarrow \min$$
* 求解出的平滑螺线保证了全曲线的曲率导数能量极小化，再通过自适应德卡斯特里奥细分，自动导出符合 OpenType 规范的标准三次贝塞尔曲线，彻底消除了手工反复调节控制点所带来的微小视觉瑕疵！
