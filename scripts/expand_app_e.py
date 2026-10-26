# -*- coding: utf-8 -*-
"""
Expander for Appendix E: TrueType Instructions Reference Dictionary
Adds full execution trace for glyph hinting and graphics state transition tables.
Target: ~22,000 characters
"""

extra_trace = r"""
---

## E.5 实战演练：大写字母 'H' 的完整虚拟机字节码执行跟踪（Instruction Execution Trace）

为了彻底理解 TrueType 虚拟机的微观运作机制，我们以大写字母 'H' 为例，完整跟踪光栅化引擎在执行 `glyf` 表内部字节码时的操作数栈、寄存器与控制点坐标变化。

### 1. 字母 'H' 的几何控制点拓扑：
字母 'H' 由 12 个关键控制点构成（全部为在线点 On-curve Points）：
* 左立柱（Left Stem）：点 0（左下）、点 1（右下）、点 2（右上）、点 3（左上）；
* 中间横梁（Crossbar）：点 4（左下交点）、点 5（右下交点）、点 6（右上交点）、点 7（左上交点）；
* 右立柱（Right Stem）：点 8（左下）、点 9（右下）、点 10（右上）、点 11（左上）。
此外，系统自动追加两个幻影点（Phantom Points）：点 12（原点，X=0）与点 13（前进宽度点，X=AdvanceWidth）。

### 2. Y 轴方向网格对齐指令流执行跟踪：

```tt-assembly
/* 步骤 1：将投影向量与自由向量同时设置为 Y 轴 (0, 1) */
SVTCA[y]

/* 步骤 2：对齐基线 */
/* 将点 0（左立柱底端）直接对齐到最近的物理像素网格边界，并标记为已触碰 (Touched) */
PUSHB[000] 0
MDAP[round]

/* 步骤 3：以点 0 为基准，拉伸并锁定左立柱高度 */
/* 设置参考点 rp0 = 0 */
PUSHB[000] 0
SRP0
/* 将点 3（左立柱顶端）移动到距 rp0 经 CVT 切入控制的标准大写字高处 */
PUSHB[001] 3 1  /* 参数：目标点 3，CVT 槽位 1 (CapHeight) */
MIRP[round,min,set_rp0] /* 移动后将 rp0 自动更新为点 3 */

/* 步骤 4：以大写字高为基准，平移右立柱顶端与横梁 */
/* 将点 10（右立柱顶端）与点 3 对齐在同一水平线上 */
PUSHB[000] 10
ALIGNRP

/* 将点 0 与点 9（右立柱底端）对齐到基线 */
PUSHB[000] 0
SRP0
PUSHB[000] 9
ALIGNRP

/* 步骤 5：定位横梁并锁定横梁厚度 */
/* 沿 Y 轴内插横梁下沿点 4 的位置 */
PUSHB[002] 4 0 3 /* 目标点 4，参考点 0 与 3 */
IP
/* 以点 4 为基准，向上锁定横梁厚度（读取 CVT 槽位 2: BarHeight） */
PUSHB[000] 4
SRP0
PUSHB[001] 7 2
MIRP[round,min,color_black]

/* 步骤 6：全局平滑内插 Y 轴所有剩余未触碰点 */
IUP[y]
```

### 3. X 轴方向网格对齐指令流：

```tt-assembly
/* 切换至 X 轴方向 (1, 0) */
SVTCA[x]

/* 对齐左侧轴承 (LSB) */
PUSHB[000] 0
MDAP[round]

/* 锁定左立柱宽度（从 CVT 槽位 3 读取 StdVW 垂直主干宽） */
PUSHB[000] 0
SRP0
PUSHB[001] 1 3
MIRP[round,min,set_rp0]

/* 锁定右立柱位置与宽度 */
/* 读取 CVT 槽位 4 (立柱间距)，将点 8 平移到正确间距 */
PUSHB[001] 8 4
MIRP[round,min,set_rp0]
/* 以点 8 为基准锁定右立柱宽度（点 9） */
PUSHB[001] 9 3
MIRP[round,min,color_black]

/* 横梁左右端点对齐到立柱内侧边 */
PUSHB[000] 1
SRP0
PUSHB[001] 4 7
ALIGNRP
ALIGNRP

PUSHB[000] 8
SRP0
PUSHB[001] 5 6
ALIGNRP
ALIGNRP

/* 最终对齐右侧幻影点（锁定字符总前进字宽） */
PUSHB[000] 9
SRP0
PUSHB[001] 13 5 /* CVT 槽位 5: 推荐前进字宽 */
MIRP[round,set_rp0]

/* 全局平滑内插 X 轴所有剩余未触碰点 */
IUP[x]
```

通过这一系列仅占用约 60 字节紧凑机器码的指令，字母 'H' 在从 9 像素到 200 像素的任意屏幕分辨率下，均能呈现绝对笔直、对称、且粗细毫无波动的纯净像素晶格！
"""

with open('scripts/app_builders/app_e.md', 'r', encoding='utf-8') as f:
    text_e = f.read()

full_e = text_e.strip() + '\n' + extra_trace.strip() + '\n'

with open('scripts/app_builders/app_e.md', 'w', encoding='utf-8') as f:
    f.write(full_e)

print("Successfully expanded scripts/app_builders/app_e.md, total length:", len(full_e))

py_e = """# -*- coding: utf-8 -*-
import os

def get_appendix_e():
    p = os.path.join(os.path.dirname(__file__), 'app_e.md')
    with open(p, 'r', encoding='utf-8') as f:
        return f.read()
"""
with open('scripts/app_builders/build_app_e.py', 'w', encoding='utf-8') as f:
    f.write(py_e)
print("Updated build_app_e.py")
