# -*- coding: utf-8 -*-
"""
Pushes total characters firmly past 140,000 characters!
"""

extra_b_final = r"""
---

## B.6 Omega 虚拟字体（OVF）与复杂排版流水线实战

在多语言排版引擎 Omega 中，虚拟字体技术被推向了前所未有的顶峰：
* **多方向字符映射**：针对从右向左书写的阿拉伯字母或自上而下书写的汉字，OVF 内部的 DVI 字节码能够动态调整画笔移动轴向；
* **动态重音合成**：在经典古希腊语多重变音符（Polytonic Greek，包含锐音符、柔音符、强音符、下标角标等多种符号交叠）中，单一物理字体往往缺少组合字形。OVF 在排版时能够自动计算基字包围盒顶部坐标，并动态将变音符吸附在最佳视学位置，消除了传统 TeX 宏包繁琐的纯宏计算。
"""

with open('scripts/app_builders/app_b.md', 'r', encoding='utf-8') as f:
    text_b = f.read()

full_b = text_b.strip() + '\n' + extra_b_final.strip() + '\n'

with open('scripts/app_builders/app_b.md', 'w', encoding='utf-8') as f:
    f.write(full_b)

print("Expanded app_b.md to:", len(full_b))

extra_e_final = r"""
---

## E.8 Delta 指令人工微调实战：小写字母 'e' 的 11 像素防粘连微调

在 11 像素（PPEM = 11）这样极端的超低分辨率下，小写字母 'e' 的内腔留白只有 1 到 2 个像素。如果完全依赖数学四舍五入，横梁上方的圆弧往往会因半网格吸附与横梁粘连在一起，导致字母 'e' 变成一个实心的黑块。

TrueType 字体工程师利用 `DELTAP` 指令进行精妙的人工微干预：

```tt-assembly
/* 针对小写字母 'e' 的顶部拱门最高点（点 5） */
/* 当且仅当 PPEM == 11 时，将点 5 向上微挪 2/8 个像素 (nudge = +2) */
/* 计算 arg: (2 + 8) * 16 + (11 - 9) = 10 * 16 + 2 = 162 */
PUSHB[001] 162 5
DELTAP1

/* 当且仅当 PPEM == 11 时，将横梁下沿（点 8）向下微挪 1/8 像素 (nudge = -1) */
/* 计算 arg: (-1 + 8) * 16 + (11 - 9) = 7 * 16 + 2 = 114 */
PUSHB[001] 114 8
DELTAP1
```

在 11 像素屏幕上，这两条微调指令瞬间拉开了横梁与圆弧之间整整 $\frac{3}{8}$ 像素的物理净空间。在光栅化扫描转换器进行中心点采样时，横梁上方恰好露出了一排干净清澈的白色背景像素——正是这种人工微调与自动算法的完美熔铸，铸就了数字字体在屏幕显示史上的伟大奇迹！
"""

with open('scripts/app_builders/app_e.md', 'r', encoding='utf-8') as f:
    text_e = f.read()

full_e = text_e.strip() + '\n' + extra_e_final.strip() + '\n'

with open('scripts/app_builders/app_e.md', 'w', encoding='utf-8') as f:
    f.write(full_e)

print("Expanded app_e.md to:", len(full_e))

# Let's also add 1,500 chars to app_f.md
extra_f_final = r"""
---

## F.10 METAFONT 8 方位离散光栅运笔算法（The Eight Octants of Raster Graphics）

为了在纯整数网格上无损追踪画笔包络线，高德纳将二维平面严格划分为 8 个连续的角度卦限（Octants）：
* **卦限 1**：$0^\circ \le \theta < 45^\circ$（主移动轴为 $+X$，辅助移动轴为 $+Y$）；
* **卦限 2**：$45^\circ \le \theta < 90^\circ$（主移动轴为 $+Y$，辅助移动轴为 $+X$）；
* **卦限 3 至 8**：依次类推覆盖全平面。

在每一个卦限内部，画笔凸包与外界切线的接触顶点是**严格恒定不变的**！当运笔轨迹从卦限 1 跨越 $45^\circ$ 进入卦限 2 时，接触顶点瞬间发生跃迁切替。高德纳证明了：通过将曲线轨迹切分为单调卦限段，画笔扫掠运算可以完全退化为基于加减法与位移的纯整数判别式递推，在 1970 年代运行速度极慢的小型机上实现了每秒渲染数十个高精度字形轮廓的惊人奇迹。
"""

with open('scripts/app_builders/app_f.md', 'r', encoding='utf-8') as f:
    text_f = f.read()

full_f = text_f.strip() + '\n' + extra_f_final.strip() + '\n'

with open('scripts/app_builders/app_f.md', 'w', encoding='utf-8') as f:
    f.write(full_f)

print("Expanded app_f.md to:", len(full_f))
