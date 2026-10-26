# -*- coding: utf-8 -*-
"""
Enriches app_g.md with Bézier clipping algorithm and polar form algebraic proofs.
Target: ~13,500 characters
"""

extra_g_3 = r"""
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

$$\mathcal{B}[t^k](u_1, u_2, \dots, u_n) = \frac{1}{\binom{n}{k}} \sum_{1 \le j_1 < j_2 < \dots < j_k \le n} u_{j_1} u_{j_2} \dots u_{j_k}$$

### 三次多项式极式展开全貌：
对于三次曲线 $\mathbf{P}(t) = \mathbf{a}_0 + \mathbf{a}_1 t + \mathbf{a}_2 t^2 + \mathbf{a}_3 t^3$，其关于三个独立变量 $u_1, u_2, u_3$ 的唯一极式为：

$$p(u_1, u_2, u_3) = \mathbf{a}_0 + \frac{\mathbf{a}_1}{3}(u_1 + u_2 + u_3) + \frac{\mathbf{a}_2}{3}(u_1 u_2 + u_2 u_3 + u_3 u_1) + \mathbf{a}_3 u_1 u_2 u_3$$

#### 代数检验：
1. **对称性**：显然，交换 $u_1, u_2, u_3$ 中任意两者的次序，上式各项完全对称不变；
2. **多重仿射性**：固定 $u_2, u_3$ 时，关于 $u_1$ 是形如 $A u_1 + B$ 的严格一次多项式；
3. **对角坍缩**：令 $u_1 = u_2 = u_3 = t$，有：
   $$p(t, t, t) = \mathbf{a}_0 + \frac{\mathbf{a}_1}{3}(3t) + \frac{\mathbf{a}_2}{3}(3t^2) + \mathbf{a}_3 t^3 = \mathbf{a}_0 + \mathbf{a}_1 t + \mathbf{a}_2 t^2 + \mathbf{a}_3 t^3 = \mathbf{P}(t)$$

极式理论的创立，不仅为计算机字体几何学提供了最坚固的代数奠基石，更将曲线微积分完全转化为优雅的多项式组合对称学，成为了全人类计算机图形学与几何设计皇冠上最璀璨的明珠。
"""

with open('scripts/app_builders/app_g.md', 'r', encoding='utf-8') as f:
    text_g = f.read()

full_g = text_g.strip() + '\n' + extra_g_3.strip() + '\n'

with open('scripts/app_builders/app_g.md', 'w', encoding='utf-8') as f:
    f.write(full_g)

print("Successfully expanded scripts/app_builders/app_g.md, total length:", len(full_g))
