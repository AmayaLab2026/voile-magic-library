---

## D.7 Apple Advanced Typography（AAT）高级扩展表体系

在苹果公司与微软分别主导字型技术演进的时期，苹果在 macOS（自 Mac OS X 10.0 引入）与 iOS 底层坚持并完善了源自 TrueType GX 的 **AAT（Apple Advanced Typography）** 体系。

与 OpenType 基于静态查找表（Lookups）与多轮模式匹配（Pattern Matching）不同，**AAT 的底层核心是图灵完备的“有限状态自动机（Finite State Machines / State Tables）”！**

::: tip AAT morx 变态表与 kerx 扩展字距表拓扑（Figure D-9, D-10）
![AAT morx 表拓扑（Figure D-9）](/images/fonts-encodings/fig-app-d9.png)
*AAT morx 表拓扑（Figure D-9）*
:::

*图 D-9：AAT `morx`（Extended Glyph Metamorphosis Table）内部由链表链条（Chains）构成，每个链条包含独立的特性掩码与状态机子表。*

::: tip AAT trak 跟踪排印与字间距动态补偿（Figure D-10）
![AAT trak 跟踪表（Figure D-10）](/images/fonts-encodings/fig-app-d10.png)
*AAT trak 跟踪表（Figure D-10）*
:::

*图 D-10：AAT `trak`（Tracking Table）结构。针对不同显示磅数（Point Sizes）定义字间距自动扩展与收缩曲线。*

---

### 1. AAT 扩展状态机（Extended State Table）的代数结构

一个标准的 AAT 状态机子表在二进制内存中由四大连续组件构成：
1. **Header（状态机头）**：记录状态总数、类总数、以及到后续三张表的相对字节偏移量；
2. **ClassTable（字形到类别映射表）**：将输入的 GID 映射为一个 16 位整数类别（Class ID）；
3. **StateArray（二维状态跃迁转移矩阵）**：一个行数为状态数、列数为类别数的稠密二维数组。给定当前状态 $S$ 与输入类别 $C$，查得转移条目索引：
   $$\text{EntryIndex} = \text{StateArray}[S][C]$$
4. **EntryTable（动作条目数组）**：每一个条目占用 4 字节，编码了三大核心排版动作：
   * `newState`：状态机转移到的下一个目标状态；
   * `flags`：执行动作标志位（指示是否将当前字形压入内部回溯硬件栈、是否标记当前位置、是否向前推进画笔）；
   * `actionIndex`：指向字形替换数组或字距微调数组的操作索引。

```
+-------------------------------------------------------+
|  AAT 状态机执行流 (State Machine Execution Pipeline)   |
+-------------------------------------------------------+
|  Input Glyph GID                                      |
|       │                                               |
|       ▼                                               |
|  [ ClassTable ] ──> Class ID (C)                      |
|                           │                           |
|  Current State (S) ───────┼───> [ StateArray[S][C] ]  |
|                                         │             |
|                                         ▼             |
|                                 [ EntryTable ]        |
|                                 ├── Next State (S')   |
|                                 ├── Push/Pop Stack    |
|                                 └── Action (Subst/Kern)
+-------------------------------------------------------+
```

由于状态机在处理连续文本时**仅需向前线性扫描一次（$O(N)$ 单趟时间复杂度）**，AAT 在处理极为繁复的南亚印度系文字（如天城体、泰米尔体、高棉体）与阿拉伯文时，其排版性能与抗死锁能力在历史上长期碾压早期未经硬件优化的 OpenType 引擎！

---

### 2. `morx` 表（扩展字形变态表）的五大子表形态

`morx`（Extended Glyph Metamorphosis）是 AAT 排版体系的心脏。它划分为五种专有子表类型：
1. **Type 0（Rearrangement Subtable / 字形重排状态机）**：
   * 专为印度系文字设计。在印地语中，某些短元音在逻辑字符编码上书写在辅音之后，但视觉呈现上必须被“抛掷”到辅音甚至整个辅音连缀的前方！Type 0 状态机包含一个最多容纳 4 个字符的微型硬件回溯栈，支持从栈中任意重排字符的物理绘制次序；
2. **Type 1（Contextual Glyph Substitution / 上下文替换状态机）**：
   * 在状态转移的同时，根据 `actionIndex` 查表对当前标记的字形进行一对一或基于类的变体替换；
3. **Type 2（Ligature Substitution / 状态机连字替换）**：
   * 支持任意跨度、任意复杂度的多字合字。状态机在扫描连字组件时将它们依次推入内部栈，在遇到连字闭合字符时，一次性将栈中所有组件弹出并整体替换为最终目标合字；
4. **Type 4（Non-contextual Substitution / 非上下文单字替换）**：
   * 无状态机开销，通过单一查找表执行全局单字变体替换；
5. **Type 5（Glyph Insertion / 动态字形插入状态机）**：
   * 允许状态机在当前文本流中凭空插入一个或多个崭新的字形（例如插入方向控制符号、连字符或装饰衬花），而无需上层应用程序修改原始 Unicode 文本缓冲区。

---

### 3. `kerx` 表（扩展字距微调表）

AAT 的 `kerx` 表是对传统 TrueType `kern` 表的革命性升级：
* **Format 0（简单有序字偶对）**：经典 $(Left, Right) \to \text{Value}$ 二分查找数组；
* **Format 1（状态机驱动的上下文多字符微调）**：能够在跨越多个中间字符的复杂语境下，同时对多达 8 个暂存字符施加高精度的相对二维坐标微调！
* **Format 2（基于类的字距矩阵）**：利用稠密矩阵执行全字库大面积字距补偿；
* **Format 4（跨流字距微调 Cross-Stream Kerning）**：**在垂直于文本流动方向的轴线上施加位移**！例如在阿拉伯文草书排版中，当某个字符向下倾斜时，后续字符通过跨流字距在垂直 Y 轴上整体抬高，完美模拟出波斯体书法连绵起伏、层层叠叠的瀑布式美感！

---

### 4. `feat` 表（排版特性多语言定义表）

与 OpenType 采用 4 字节 ASCII 缩写标签（如 `liga`, `smcp`）且未在字体内部定义本地化名称不同，AAT 的 `feat` 表将排版特性定义为两级数字代号：
* **`FeatureType`（特性类别）**：如 1 代表合字（Ligatures），3 代表备选字形（Alternate Pos），22 代表文字变体；
* **`SettingSelector`（设置选择器）**：如对于合字特性，选择器 0 为关闭所有合字，2 为启用标准合字，4 为启用历史连字；
* **多语言本地化支持**：每个特性与选择器直接绑定一个 `nameID`，在 `name` 表中存储英语、法语、中文、日语等原生字符串。使得 macOS 的“字体面板（Font Panel）”能够无需任何外部配置，原生为用户渲染出一个全本地化、支持勾选切换的高级排版功能交互式界面！

---

### 5. `trak`、`opbd`、`bsln` 与 `lcar` 表

* **`trak`（Tracking Table / 字距跟踪表）**：
  * 在传统金属活字排版中，大磅字号（如 72 磅海报标题）需要适度收紧字距，而极小字号（如 6 磅版权小字）必须大幅放宽字间距以保证辨识度。`trak` 表定义了由字体设计师绘制的字号-字距连续非线性补偿样条曲线，操作系统排版器根据当前渲染磅值动态求值并自动施加均匀的微米级字间距平移；
* **`opbd`（Optical Bounds / 视觉边缘对齐表）**：
  * 人眼的视觉心理物理学（Psychophysics）表明：当一段文字左侧包含左双引号 `“` 或小写字母 `o` 时，若将其物理包围盒与下方大写字母 `H` 机械对齐，视觉上会显得左侧凹陷不平。`opbd` 表为每个字符定义了左、上、右、下四个方向的**光学凸出量（Optical Offsets）**，使标点符号在段落边缘能够极其优美地“挂起”探出边框（Hanging Punctuation）；
* **`bsln`（Baseline Table / AAT 基线表）**：
  * 定义了多达 32 种不同文字系统的基线系统，并在同一字库内部存储各文字基线的相对垂直坐标与主控基线（Dominant Baseline）优先权；
* **`lcar`（Ligature Caret Table / 合字光标分割线表）**：
  * 当文本光标在合字（如 'ffi'）内部移动时，`lcar` 为其定义了两个内部逻辑切分点（Caret Coordinates）。光标在合字中间闪烁时能够精确停留在 'f' 与 'i' 之间的虚拟空间，彻底解决了用户在编辑连字时无法定位内部字符的交互噩梦。

通过 SFNT 容器的弹性封装、TrueType 虚拟机的微观粒子控制、OpenType 布局引擎的图灵文法重写、以及 AAT 状态机的毫秒级流式处理，数字字体工程构建起了人类信息文明史上最为精密、优雅且深邃的排印技术巨塔。
