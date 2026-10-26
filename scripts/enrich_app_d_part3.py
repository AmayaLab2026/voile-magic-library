# -*- coding: utf-8 -*-
"""
Enriches app_d.md with AAT state transition matrices and OpenType vs AAT comparison.
Target: ~41,000 characters
"""

extra_d_3 = r"""
---

## D.9 AAT 有限状态自动机状态跃迁矩阵实战推导

为了深刻理解 AAT `morx` 表内部状态转移的数学精髓，我们以印地语天城体（Devanagari）的短元音 'i'（Matra-I）前置重排状态机为例进行推导：

在天城体中，逻辑编码顺序为：$\text{辅音 (Consonant)} + \text{短元音 (Matra-I)}$，但在视觉排版中，短元音必须被“向前翻转”到辅音左侧！

### 状态转移代数模型：
* **状态集合**：$Q = \{ S_0: \text{StartOfLine}, \, S_1: \text{SawConsonant}, \, S_2: \text{SawVirama} \}$；
* **字符类别**：$\Sigma = \{ C_0: \text{Other}, \, C_1: \text{Consonant}, \, C_2: \text{Matra-I}, \, C_3: \text{Virama (死符)} \}$。

#### 跃迁矩阵与动作表（StateArray & EntryTable）：

| 当前状态 | 输入类别：$C_1$ (辅音) | 输入类别：$C_2$ (短元音 Matra-I) | 输入类别：$C_3$ (Virama 死符) | 输入类别：$C_0$ (其余字符) |
| :--- | :--- | :--- | :--- | :--- |
| **$S_0$ (起点)** | 转移到 $S_1$；**动作**：将辅音压栈 (Push) | 保持 $S_0$；无动作 | 保持 $S_0$；无动作 | 保持 $S_0$；推进画笔 |
| **$S_1$ (已见辅音)**| 保持 $S_1$；清空旧栈并压入新辅音 | **触发重排**！转移到 $S_0$；**动作**：从栈中弹出辅音，先绘制短元音，再绘制辅音！ | 转移到 $S_2$；将死符压栈 | 转移到 $S_0$；弹出并清空栈 |
| **$S_2$ (已见死符)**| 转移到 $S_1$；将第二辅音压栈（构筑半辅音连缀群） | **触发连缀重排**！转移到 $S_0$；将元音抛至整个连缀左端！ | 转移到 $S_0$；清空栈 | 转移到 $S_0$；清空栈 |

这种单趟纯线性自动机机制，使得苹果 macOS 的 CoreText 图形框架在处理复杂的梵文经文、藏文千字大藏经时，以极简的查表动作完成了传统排版软件需要数十重正则匹配才能完成的宏伟变换。

---

## D.10 OpenType 与 AAT 排版体系深度技术对照

| 技术维度 | 微软 / Adobe OpenType | 苹果 Apple Advanced Typography (AAT) |
| :--- | :--- | :--- |
| **核心计算模型** | 基于多轮遍历的声明式模式替换查找表（Lookups & Features） | 基于有限状态机（Finite State Machines）的单趟流式自动机 |
| **执行时间复杂度** | 最坏情况下为多次遍历匹配（$O(N \times K)$，依赖查找链长度） | 严格单趟线性时间扫描（$O(N)$，扫描一遍文本即完成排版） |
| **排版逻辑归属** | **外部驱动主导**：字体仅提供数据，排版整形引擎（HarfBuzz, Uniscribe）承担脚本形态逻辑 | **字体内部自治**：字体自身即为完整状态机，上层排版引擎无需知道任何具体语言规则 |
| **跨文字基线支持** | `BASE` 表（罗马基线、汉字底部、中轴、数学轴） | `bsln` 表（32 种脚本原生基线优先级） |
| **字距微调能力** | GPOS Type 2（静态字偶对与分类微调矩阵） | `kerx` 表（支持跨流字距微调与状态机级 8 字符级联微调） |
| **多语言本地化** | 采用 4 字节全局 ASCII 标签（如 'liga'），UI 名称需操作系统单独提供 | `feat` 表将特性代码与 `name` 表多语言字串原生绑定，字体自带本地化菜单 |
| **工业生态与标准** | **全球绝对主导标准**：Windows, Linux, Android, Web 浏览器默认标准 | 苹果生态独占专有标准：macOS, iOS 原生支持，工业跨平台支持较弱 |
"""

with open('scripts/app_builders/app_d.md', 'r', encoding='utf-8') as f:
    text_d = f.read()

full_d = text_d.strip() + '\n' + extra_d_3.strip() + '\n'

with open('scripts/app_builders/app_d.md', 'w', encoding='utf-8') as f:
    f.write(full_d)

print("Successfully expanded scripts/app_builders/app_d.md, total length:", len(full_d))
