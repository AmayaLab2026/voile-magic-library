# -*- coding: utf-8 -*-
"""
Enriches app_e.md with graphics state table and Twilight Zone mechanics.
Target: ~20,000 characters
"""

extra_e_2 = r"""
---

## E.6 图形状态机（Graphics State）24 维变量全景字典

在 TrueType 虚拟机执行期间，图形状态机（Graphics State）维护着一套直接决定所有几何测量与网格吸附行为的全局环境量：

| 状态机变量名 | 数据类型 | 初始默认值 | 相关的读取与设置指令 | 物理排版语义与控制行为 |
| :--- | :--- | :--- | :--- | :--- |
| `auto_flip` | Boolean | `true` | `FLIPON`, `FLIPOFF` | 是否自动翻转极性方向错误的笔画控制点 |
| `control_value_cut_in` | F26Dot6 | `17/16` (68) | `SCVTCI` | CVT 强行吸附门限值（当轮廓尺寸与 CVT 偏差小于此值时强制锁死） |
| `delta_base` | uint16 | `9` | `SDB` | Delta 指令激活的起始基础字号（PPEM） |
| `delta_shift` | uint16 | `3` | `SDS` | Delta 微位移缩放步长（$1/2^{\text{delta\_shift}}$ 像素） |
| `dual_projection_vector` | Unit Vector | $(1, 0)$ | `SPVTCA`, `SPVTL`, `SPVFS` | 在未经变换的原始设计轮廓上测量初始距离的单位向量 |
| `freedom_vector` | Unit Vector | $(1, 0)$ | `SFVTCA`, `SFVTL`, `SFVFS`, `SFVTPV` | 点被允许移动的物理自由轴向单位向量 |
| `instruct_control` | uint8 | `0` | `INSTCTRL` | 全局指令执行掩码（Bit 0: 关闭网格对齐; Bit 1: 忽略默认参数） |
| `loop` | uint16 | `1` | `SLOOP` | 循环计数器（后续多点移动指令连续执行的次数） |
| `minimum_distance` | F26Dot6 | `1.0` (64) | `SMD` | 相对移动时保持的两笔画最小物理保护间距（防止坍缩重叠） |
| `projection_vector` | Unit Vector | $(1, 0)$ | `SPVTCA`, `SPVTL`, `SPVFS` | 距离投影测量轴向单位向量 |
| `round_state` | State | `Round to Grid` | `RTG`, `RTHG`, `RTDG`, `RDTG`, `RUTG`, `ROFF`, `SROUND` | 当前数值量化为像素网格的四舍五入规则引擎 |
| `rp0` | Point Index | `0` | `SRP0`, `MDRP`, `MIRP` | 参考点 0（作为相对位移的起点锚点） |
| `rp1` | Point Index | `0` | `SRP1` | 参考点 1（用于内插指令 IP 的左基准） |
| `rp2` | Point Index | `0` | `SRP2` | 参考点 2（用于内插指令 IP 的右基准） |
| `scan_control` | uint16 | `0` | `SCANCTRL` | 极小字号下辍笔（Dropout）保护模式激活阈值 |
| `single_width_cut_in` | F26Dot6 | `0.0` | `SSWCI` | 单笔画全局宽度统一吸附阈值 |
| `single_width_value` | F26Dot6 | `0.0` | `SSW` | 全局单笔画标准物理宽度 |
| `zp0` | Zone Pointer | `1` | `SZP0`, `SZPS` | 目标点所在的几何区域指针（Zone 0 黄昏区或 Zone 1 轮廓区） |
| `zp1` | Zone Pointer | `1` | `SZP1`, `SZPS` | 参考点 1 所在的几何区域指针 |
| `zp2` | Zone Pointer | `1` | `SZP2`, `SZPS` | 参考点 2 所在的几何区域指针 |

---

## E.7 黄昏区（Twilight Zone / Zone 0）的幽灵点力学

在复杂的字形 Hinting 中，字体设计师经常需要在字形轮廓外部构筑临时辅助几何结构（例如两条切线的虚交点、两立柱正中轴线、或外接圆圆心），但这些辅助点**在最终字形光栅化时绝对不能被渲染成黑色像素**！

TrueType 专门开辟了一个与当前真实字形平行的虚拟内存区域——**黄昏区（Zone 0）**：
* 内部所有点均为临时的“幽灵点（Ghost Points）”；
* 通过将区域指针 `SZP0` 或 `SZPS` 设置为 0，所有几何微调指令（如 `ALIGNPTS`, `IP`, `ISECT`, `MDRP`）均可作用于黄昏区；
* 设计师可以先在黄昏区计算出完美的对称几何中心，再将真实字形（Zone 1）中的轮廓点绑定并内插到该中心点上，随后退出。当光栅化引擎绘制文字时，Zone 0 的数据被直接丢弃，实现了纯粹、无瑕且极度严谨的隐形空间工程学！
"""

with open('scripts/app_builders/app_e.md', 'r', encoding='utf-8') as f:
    text_e = f.read()

full_e = text_e.strip() + '\n' + extra_e_2.strip() + '\n'

with open('scripts/app_builders/app_e.md', 'w', encoding='utf-8') as f:
    f.write(full_e)

print("Successfully expanded scripts/app_builders/app_e.md, total length:", len(full_e))
