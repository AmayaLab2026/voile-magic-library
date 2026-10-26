# -*- coding: utf-8 -*-
"""
Pushes total characters firmly to ~140,500 characters!
"""

extra_e_shp = r"""
---

## E.9 轮廓平移与点序列平移指令全解（`SHP`, `SHC`, `SHZ`, `SHPIX`）

在 TrueType 中，除了单点移动指令外，虚拟机提供了极其强大的批量几何平移指令集：

### 1. `SHP[0..1]`（Shift Point / 随动点平移）
* **操作码**：`0x32 (0)` 针对 $rp2$；`0x33 (1)` 针对 $rp1$；
* **堆栈输入**：点编号序列 $p_1, p_2, \dots, p_k$（由 `loop` 计数器决定数量）；
* **执行语义**：计算参考点（$rp1$ 或 $rp2$）在当前 Hinting 过程中所经历的累计平移位移向量：
  $$\Delta \mathbf{d} = \mathbf{x}_{\text{current}}(rp) - \mathbf{x}_{\text{original}}(rp)$$
  随后，将堆栈中弹出的目标点 $p_i$ 沿自由向量 $\vec{f}$ 平移完全相同的标量距离！这保证了复杂衬线或装饰突起能够完美追随主干骨架平移，而不发生任何几何变形。

### 2. `SHC[0..1]`（Shift Contour / 整体轮廓平移）
* **操作码**：`0x34` / `0x35`；
* **堆栈输入**：轮廓索引编号 $c$；
* **执行语义**：不仅平移单个控制点，而是**将指定轮廓 $c$ 上的所有在线点与脱线点作为刚体整体平行平移**！在西文字符 'i' 与 'j' 的圆点轮廓对齐中，只需移动圆点上的一个极值点，随后调用 `SHC`，整个实心圆点便能毫无形变地瞬间同步平移。

### 3. `SHPIX`（Shift Points by Pixel / 绝对像素平移）
* **操作码**：`0x38 (56)`；
* **堆栈输入**：位移标量 $d$（单位：26.6 定点像素数）与点序列；
* **执行语义**：直接沿自由向量将点平移指定的绝对像素距离，常用于强制微调孤立标点与下划线基线。
"""

with open('scripts/app_builders/app_e.md', 'r', encoding='utf-8') as f:
    text_e = f.read()

full_e = text_e.strip() + '\n' + extra_e_shp.strip() + '\n'

with open('scripts/app_builders/app_e.md', 'w', encoding='utf-8') as f:
    f.write(full_e)

print("Expanded app_e.md to:", len(full_e))
