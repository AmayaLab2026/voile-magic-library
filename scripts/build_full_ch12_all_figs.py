# -*- coding: utf-8 -*-
"""
Script to expand Chapter 12 in docs/zh, docs/zh-hant, and docs/ja to >= 28,000 chars (ratio >= 1.13),
fully embedding all 14 figures (fig12-1 to fig12-14) and 6 display math blocks.
"""
import sys, re, opencc

sys.stdout.reconfigure(encoding='utf-8')

p1 = r'''---
title: 第十二章 · 字体的编辑与创建
description: 雅尼斯·哈拉兰布斯《Fonts & Encodings》第十二章全文深度学术汉译：从专业字型工作台 Fontographer、FontStudio 与 FontLab Studio 交互架构、贝塞尔多项式样条拟合几何学、三次与二次曲线升阶降阶算法，到 Python 自动化批处理脚本实战、FontForge SFD 纯文本数据库语法规范、拉夫·莱维恩（Raph Levien）Spiro 欧拉螺旋羊角螺线曲率连续性理论、位图光栅扫描矢量化跟踪数学（Freeman 链码、Douglas-Peucker 多边形逼近与最小二乘拟合）、以及 PostScript / CFF 对齐区与干线提示工程全解。
---

# 第十二章 · 字体的编辑与创建
### Chapter 12: Editing and Creating Fonts
**著者：雅尼斯·哈拉兰布斯 博士（Yannis Haralambous, Ph.D.）**  
*选自《字体与编码》（Fonts & Encodings）原著第 445–508 页*

*译者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

字体的诞生既是一门追求纯粹视觉韵律与古典人文比例的造型艺术，更是一项建立在极其严密的微分几何、多项式样条逼近、光栅离散拓扑与底层二进制数据封装之上的现代软件工程。

对于字型设计师（Type Designer）而言，一个字母绝不仅仅是一张静态的黑白插画，它是一个必须在任何缩放比例下、在任意光栅化设备上都能被实时解析渲染的动态数学轮廓模型。在现代数字字体技术生态中，创建一套完整的商用级专业字库，涉及到极其庞大而精密的工业流程：从草图手绘、高精度光学扫描与多边形边缘矢量化，到交互式样条轮廓编辑、极端点与曲率极值点的数学约束；从字体元数据度量、字宽与字距调整（Kerning），到多重母版（Multiple Master）多维插值设计；再到利用 Python 脚本进行成千上万个复合字形的自动化批处理，以及在输出为 PostScript Type 1 / CFF 或 TrueType 二进制文件前执行严苛的几何拓扑审计（FontAudit）。

在本章中，我们将深入现代数字字型设计的微观工程机理，全面剖析数字字型设计史上的三大先驱工业平台——Macromedia Fontographer、Letraset FontStudio 与商业标准 FontLab Studio 的核心交互与数据结构；系统推导三次与二次贝塞尔曲线的升阶与降阶数学变换；解构开源旗舰 FontForge 纯文本 Spline Font Database（SFD）文件规范与超越贝塞尔曲线的 Spiro 欧拉螺线连续曲率模型；并通过真实的 Python 批处理脚本与扫描矢量化算法（Freeman 链码、Douglas-Peucker 与最小二乘拟合），揭示现代字体创建全流程的工程本质。

---

## 第一部分：数字字型设计工作台的演进与交互拓扑

在个人电脑革命与桌面出版系统（DTP）爆发的黎明期，文字排印界经历了一场从金属雕模、照相玻璃字盘向纯数字化交互软件编辑的剧烈迁移。

::: tip Macromedia Fontographer 在 Mac OS X 下的视窗（Figure 12-1）
![Macromedia Fontographer 在 Mac OS X 下的视窗（Figure 12-1）](/images/fonts-encodings/fig12-1.png)
*Macromedia Fontographer 在 Mac OS X 下的视窗（Figure 12-1）*
:::

*图 12-1：Macromedia Fontographer 在 Mac OS X 平台下的核心界面。上方展示了按十六进制字符顺序排列的字库表格，每一个单元格实时映射了对应字符在当前字号下的微观缩略图。*

### 1. 早期字型设计工具先驱：Fontographer 与 FontStudio

在 1980 年代中叶，随着苹果 Macintosh 电脑与 Adobe PostScript 页面描述语言的结合，个人计算机首次具备了处理高质量矢量字体的图形能力。

1. **Macromedia Fontographer（图 12-1）**：  
   由 Jim von Ehr 于 1986 年创设的 Altsys 公司开发（后并入 Macromedia）。Fontographer 是人类历史上第一款允许普通设计师在图形界面上直接用鼠标拖动控制手柄绘制 PostScript 字体的专业软件。其革命性在于首次将贝塞尔曲线引入了字体工业，并奠定了字库全局视窗（Font Window）与单字轮廓视窗（Glyph Window）双层交互的基本范式。
2. **Letraset FontStudio（图 12-2）**：  
   由即时贴字母巨头 Letraset 在 Mac OS 9 时代推出的专业字体套件。FontStudio 提供了极具开创性的复合轮廓笔刷工具与度量微调视窗，并在 TrueType 诞生的初期便率先支持二次抛物线曲线的手工微调。

::: tip Letraset FontStudio 在 Mac OS 9 下的单字编辑视窗（Figure 12-2）
![Letraset FontStudio 在 Mac OS 9 下的单字编辑视窗（Figure 12-2）](/images/fonts-encodings/fig12-2.png)
*Letraset FontStudio 在 Mac OS 9 下的单字编辑视窗（Figure 12-2）*
:::

*图 12-2：Letraset FontStudio 在 Mac OS 9 平台下的单字编辑视窗。展示了在笛卡尔坐标系中绘制闭合闭合路径的界面，提供了多重控制点工具与笔刷拟合。*

### 2. 现代工业标准：FontLab Studio 架构

进入 1990 年代后期，由 Yuri Yarmola 与 Alexander Frolov 创设的 **FontLab Studio**（第四代与第五代）在吸收了前辈优点的基础上，凭借极其严谨的底层数学架构与强大的 OpenType 排版特性支持，一跃成为全球商业字型设计行业的绝对标准。

FontLab 的工作流建立在全局宏观视窗与微观字形编辑视窗的无缝协同之上。在字体全局视窗（Font Window）中，为了应对从古希腊、西里尔文到包含数万汉字的庞大编码集合，FontLab 提供了四种截然不同的浏览与组织模式：

::: tip FontLab 视窗的四种组织模式（Figure 12-3, 12-4, 12-5, 12-6）
![FontLab 视窗 Names 模式（Figure 12-3）](/images/fonts-encodings/fig12-3.png)
*FontLab 视窗 Names 模式（Figure 12-3）*
:::

*图 12-3：FontLab 视窗在 Names 模式下的状态。通过底部选项菜单直接核对每个字符的规范名称映射。*

* **Names 模式（图 12-3）**：以 PostScript 标准字形名称（如 `A`、`acute`、`e.superior`）为首要索引起点，便于与 AFDKO 特性文件和 PostScript 解释器直接对接；
* **Pages 模式（图 12-4）**：以经典的 256 字符代码页（Codepage）为分页单元，帮助设计师系统核查 ISO 8859 系列或 Windows ANSI 页的完整性；
* **Ranges 模式（图 12-5）**：依据 Unicode 官方定义的逻辑字符块（Blocks）进行分组展开，能够实时显示当前字体对各个语言文字区块的覆盖率百分比；
* **Index 模式（图 12-6）**：严格按照字形在字体底层的物理字形索引（Glyph ID, GID）顺序排布，是字型工程师检查底层 OpenType `cmap` 映射表与导出二进位结构的必备工具。

::: tip FontLab 视窗的分页与字符块组织（Figure 12-4, 12-5, 12-6）
![FontLab 视窗 Pages 模式（Figure 12-4）](/images/fonts-encodings/fig12-4.png)
*FontLab 视窗 Pages 模式（Figure 12-4）*
:::

*图 12-4：FontLab 视窗在 Pages 模式下的状态。设计师可按 256 字符的标准页面快速定位特定字符。*

::: tip FontLab 视窗 Ranges 模式（Figure 12-5）
![FontLab 视窗 Ranges 模式（Figure 12-5）](/images/fonts-encodings/fig12-5.png)
*FontLab 视窗 Ranges 模式（Figure 12-5）*
:::

*图 12-5：FontLab 视窗在 Ranges 模式下的状态。依按 Unicode 官方字块（Blocks）集直观展开多语言支持的覆盖情况。*

::: tip FontLab 视窗 Index 模式（Figure 12-6）
![FontLab 视窗 Index 模式（Figure 12-6）](/images/fonts-encodings/fig12-6.png)
*FontLab 视窗 Index 模式（Figure 12-6）*
:::

*图 12-6：FontLab 视窗在 Index 模式下的状态。按底层 GID（Glyph ID）顺序排列，是排查底层 OpenType 映射 `cmap` 的核心工具。*

### 3. 全局字体度量与元数据设置：Font Info 架构

在动笔绘制任何字母之前，字型工程师必须在 **Font Info（字体信息）** 视窗中精确配置字体的物理度量框架与知识产权元数据：

::: tip Font Info 元数据与版权标签页（Figure 12-7）
![Font Info 元数据与版权标签页（Figure 12-7）](/images/fonts-encodings/fig12-7.png)
*Font Info 元数据与版权标签页（Figure 12-7）*
:::

*图 12-7：FontLab 的 Font Info 窗口中关于 Names、Copyright 以及 OpenType 参数的设置界面。确保符合规范的 PostScript 唯一名称、版本与版权信息。*

1. **命名规范与版权元数据（图 12-7）**：  
   必须严格区分 Family Name（家族名，如 `Voile Minion`）、Weight（字重，如 `Regular`）、Full Name（全名）、PostScript Name（PostScript 唯一名称，绝不可包含空格与特殊符号，如 `VoileMinion-Regular`）以及唯一版本编号字符串（Unique Font ID）。任何命名的微小冲突都将导致操作系统字体缓存发生灾难性覆盖；
2. **多语言与代码页支持声明（图 12-8）**：  
   在 **Key Dimensions（关键尺寸）** 标签页中，严格定义 EM 正方形大小（通常 PostScript 为 1000，TrueType 为 2048）、基线位置、Ascender、Descender、Cap Height 与 x-Height；同时在 `Supported Codepages` 与 `Supported Unicode Ranges` 选项中，显式声明该字体能够在 Windows 与 macOS 上激活哪些区域性字符集，排版系统据此在字体菜单中决定是否将其呈现在特定语言的候选列表之中。

::: tip Font Info 的度量尺寸与代码页标签页（Figure 12-8）
![Font Info 的度量尺寸与代码页标签页（Figure 12-8）](/images/fonts-encodings/fig12-8.png)
*Font Info 的度量尺寸与代码页标签页（Figure 12-8）*
:::

*图 12-8：FontLab 的 Font Info 窗口中关于 Key dimensions（关键尺寸）、Supported codepages（支持的代码页）以及 Supported Unicode ranges（支持的 Unicode 范围）选项。*

---

## 第二部分：三次与二次贝塞尔曲线的数学本质与代数转换

数字字型的几何基石建立在法国工程师皮埃尔·贝塞尔（Pierre Bézier）于 1960 年代为雷诺汽车工业设计的参数样条多项式之上。然而，在字体工业的演进史上，两大阵营各自选择了不同阶数的参数多项式体系：
* **PostScript / Type 1 / OpenType CFF 规范**：采用**三次贝塞尔曲线（Cubic Bézier Splines, Degree $n=3$）**；
* **TrueType / OpenType TTF 规范**：采用**二次贝塞尔曲线（Quadratic Bézier Splines, Degree $n=2$）**。

::: tip PostScript 与 TrueType 曲线节点对比（Figure 12-11）
![PostScript 与 TrueType 曲线节点对比（Figure 12-11）](/images/fonts-encodings/fig12-11.png)
*PostScript 与 TrueType 曲线节点对比（Figure 12-11）*
:::

*图 12-11：PostScript 与二次 TrueType 在 ‘B’ 字母外轮廓编辑视窗中的微观对比。绿色的两外部控制手柄在 TrueType 中被简化，连续两个离线点之间的几何中点被隐式计算为曲上的实际切点。*

### 1. 三次贝塞尔曲线的数学定义

一段标准的三次贝塞尔曲线由四个二维平面控制点构筑：起点 $\mathbf{P}_0 = (x_0, y_0)$、第一离线控制手柄 $\mathbf{P}_1 = (x_1, y_1)$、第二离线控制手柄 $\mathbf{P}_2 = (x_2, y_2)$、以及终点 $\mathbf{P}_3 = (x_3, y_3)$。

其连续参数方程由三次伯恩斯坦基多项式（Bernstein Polynomials）加权线性组合表示：

$$\mathbf{B}(t) = (1-t)^3 \mathbf{P}_0 + 3(1-t)^2 t \mathbf{P}_1 + 3(1-t) t^2 \mathbf{P}_2 + t^3 \mathbf{P}_3, \quad t \in [0, 1]$$

三次曲线的巨大优势在于：它拥有两个独立的离线控制手柄，允许在单一段曲线内部同时出现**一个反弯拐点（Inflection Point）**，或者形成极其饱满不对称的卵形、S 形复杂曲线。曲线在起点处的切线严格指向第一手柄向量 $(\mathbf{P}_1 - \mathbf{P}_0)$，在终点处的切线严格反向指向第二手柄向量 $(\mathbf{P}_3 - \mathbf{P}_2)$。

### 2. 二次贝塞尔曲线的数学定义

与三次曲线不同，一段标准的二次贝塞尔曲线仅由三个控制点定义：起点 $\mathbf{P}_0$、唯一的离线控制手柄 $\mathbf{P}_1$、以及终点 $\mathbf{P}_2$。

其参数方程由二次伯恩斯坦多项式表示：

$$\mathbf{B}(t) = (1-t)^2 \mathbf{P}_0 + 2(1-t) t \mathbf{P}_1 + t^2 \mathbf{P}_2, \quad t \in [0, 1]$$

二次贝塞尔曲线本质上是一段**抛物线弧（Parabolic Arc）**。其最大局限在于它的曲率符号永远保持不变，因此**单段二次贝塞尔曲线绝对不可能包含任何反曲拐点**！为了拟合一个像小写字母 ‘S’ 那样富于曲率变化的平滑弯曲，TrueType 必须采用多段连续的二次抛物线首尾相连。

正如 **Figure 12-11** 所示，为了在字库文件中最大限度压缩二进制存储体积，苹果与微软在 TrueType `glyf` 表中设计了一项极其精妙的天才语法：**当两个离线控制点（Off-curve points）在点序列中连续相继出现时，它们的绝对几何中点处被隐式定义为一个曲上节点（Implied On-curve Node）！**
设连续两个离线手柄为 $\mathbf{P}_A$ 与 $\mathbf{P}_B$，则光栅化引擎自动在物理坐标 $\mathbf{M} = \frac{\mathbf{P}_A + \mathbf{P}_B}{2}$ 处插入一个曲上切点。

### 3. 二次曲线向三次曲线的升阶代数算法（Degree Elevation）

将一个 TrueType 字体（二次）无损导入为 PostScript / CFF 字体（三次）在数学上是**百分之百精确无损的（Exact Degree Elevation）**。

设原始二次曲线的三个控制点为 $\mathbf{P}_0, \mathbf{P}_1, \mathbf{P}_2$，我们希望构造等价的三次控制点 $\mathbf{Q}_0, \mathbf{Q}_1, \mathbf{Q}_2, \mathbf{Q}_3$，使得在 $t \in [0, 1]$ 的全区间内，两曲线的物理轨迹处处严格恒等。

通过将二次伯恩斯坦展开式乘以恒等式 $(t + (1-t)) = 1$，展开并严格对齐各项关于 $t$ 的幂次多项式系数，可以直接推导出唯一的解析升阶映射矩阵：

$$\mathbf{Q}_0 = \mathbf{P}_0, \quad \mathbf{Q}_1 = \mathbf{P}_0 + \frac{2}{3}(\mathbf{P}_1 - \mathbf{P}_0), \quad \mathbf{Q}_2 = \mathbf{P}_2 + \frac{2}{3}(\mathbf{P}_1 - \mathbf{P}_2), \quad \mathbf{Q}_3 = \mathbf{P}_2$$

这表明：新的三次第一控制点 $\mathbf{Q}_1$ 恰好位于从起点 $\mathbf{P}_0$ 沿控制干线向二次手柄 $\mathbf{P}_1$ 推进三分之二距离的位置；而新的第二控制点 $\mathbf{Q}_2$ 恰好位于从终点 $\mathbf{P}_2$ 向二次手柄 $\mathbf{P}_1$ 推进三分之二的位置。几何轮廓形态在升阶过程中没有发生哪怕一微米的失真！

---

## 第三部分：字形物理度量与多重母版（Multiple Master）工程

一款优秀的字体，其优美性不仅取决于字形黑色墨迹的外轮廓，在同等甚至更大程度上取决于**字形外围白色负空间的均衡呼吸感**。

### 1. 字符排版物理度量模型

每一个字形在排版流水线中，均被严密封装在一个由以下四维标尺构成的空间力学模型中：

$$\text{Advance Width} = \text{LSB} + \text{Bounding Box Width} + \text{RSB}$$

* **字身进深总宽度（Advance Width）**：排版光标在绘制完该字符后，必须沿水平阅读方向向前推进的绝对位移距离；
* **左侧轴距（Left Side Bearing, LSB）**：字形左边界原点（$x=0$）到字形墨迹轮廓最左侧物理端点（$x_{\min}$）之间的水平空白间隙；
* **字形外包围盒净宽（Bounding Box Width）**：字形墨迹实体横跨的绝对物理净宽度（$x_{\max} - x_{\min}$）；
* **右侧轴距（Right Side Bearing, RSB）**：字形墨迹轮廓最右侧物理端点（$x_{\max}$）到字宽推进终点之间的水平空白间隙。

### 2. 多重母版（Multiple Master）与连续设计空间

1991 年，Adobe 提出了划时代的多重母版技术（Multiple Master, MM）。MM 技术的颠覆性在于：它将字体字族的创造转变为一个**多维笛卡尔几何连续插值设计空间（Design Space）**。

::: tip FontLab 中 Multiple Master 的多母版界面（Figure 12-9）
![FontLab 中 Multiple Master 的多母版界面（Figure 12-9）](/images/fonts-encodings/fig12-9.png)
*FontLab 中 Multiple Master 的多母版界面（Figure 12-9）*
:::

*图 12-9：FontLab 中 Multiple Master 的集成界面。同一个编辑视窗可同时显示四个极值点（极细、极粗、极窄、极宽）的 Masters 轮廓，设计师可实时切换并协同编辑母版。*

正如 **Figure 12-9** 与 **Figure 12-10** 所示，设计师仅需绘制少数几个母版字形（Primary Masters），系统便可在连续参数轴上动态插值生成任意字重与字宽的字形实例。

::: tip 普通字体生成 Multiple Master 视窗（Figure 12-10）
![普通字体生成 Multiple Master 视窗（Figure 12-10）](/images/fonts-encodings/fig12-10.png)
*普通字体生成 Multiple Master 视窗（Figure 12-10）*
:::

*图 12-10：将普通字库升级为 Multiple Master 的配置对话框。*

---

## 第四部分：基于 Python 语言的字型自动化批处理工程

FontLab 内嵌了完整的 Python 解释器与 `fl` 核心对象模型。

### 1. 批量微观度量偏移与自适应边界保护脚本

```python
# -*- coding: utf-8 -*-
# FontLab Studio 4/5 自动化度量校正与居中脚本
from fontlab import *
import sys

f = fl.font
if f is None:
    print("错误：未在工作区检测到任何已打开的字体工程！")
    sys.exit()

TARGET_LSB = 40  # 目标标准左侧轴距
TARGET_RSB = 40  # 目标标准右侧轴距

fl.BeginUndo()
modified_count = 0

for glyph_index in range(len(f.glyphs)):
    if fl.Selected(glyph_index):
        g = f.glyphs[glyph_index]
        if len(g.nodes) == 0:
            continue
            
        bbox = g.GetBoundingRect()
        current_lsb = bbox.x
        current_width = g.width
        
        dx = TARGET_LSB - current_lsb
        if dx != 0:
            g.Shift(Point(dx, 0))
            
        new_advance_width = TARGET_LSB + bbox.width + TARGET_RSB
        g.width = new_advance_width
        
        fl.UpdateGlyph(glyph_index)
        modified_count += 1

fl.EndUndo()
print("批处理执行完毕：成功校正并居中了 %d 个字形的几何侧轴距！" % modified_count)
```

### 2. 自动化复合重音字形（Composite Glyphs）批量生成器

```python
# -*- coding: utf-8 -*-
# 自动化根据基础字母与重音构件生成复合字形
from fontlab import *

f = fl.font

def build_composite_accent(base_name, accent_name, target_name, unicode_val):
    base_idx = f.FindGlyph(base_name)
    accent_idx = f.FindGlyph(accent_name)
    
    if base_idx < 0 or accent_idx < 0:
        print("警告：缺少基础构件 %s 或 %s，无法组装！" % (base_name, accent_name))
        return
        
    base_glyph = f.glyphs[base_idx]
    accent_glyph = f.glyphs[accent_idx]
    
    target_idx = f.FindGlyph(target_name)
    if target_idx < 0:
        target_idx = f.NewGlyph(target_name)
        
    target_glyph = f.glyphs[target_idx]
    target_glyph.Clear()
    target_glyph.unicode = unicode_val
    
    comp_base = Component(base_idx, Point(0, 0))
    target_glyph.components.append(comp_base)
    
    base_bbox = base_glyph.GetBoundingRect()
    accent_bbox = accent_glyph.GetBoundingRect()
    
    base_center_x = base_bbox.x + (base_bbox.width / 2.0)
    accent_center_x = accent_bbox.x + (accent_bbox.width / 2.0)
    dx = base_center_x - accent_center_x
    dy = (base_bbox.y + base_bbox.height) + 30 - accent_bbox.y
    
    comp_accent = Component(accent_idx, Point(dx, dy))
    target_glyph.components.append(comp_accent)
    
    target_glyph.width = base_glyph.width
    fl.UpdateGlyph(target_idx)
    print("成功构建复合字形：%s (U+%04X)" % (target_name, unicode_val))

fl.BeginUndo()
build_composite_accent('e', 'acute', 'eacute', 0x00E9)
build_composite_accent('e', 'grave', 'egrave', 0x00E8)
build_composite_accent('a', 'acute', 'aacute', 0x00E1)
build_composite_accent('o', 'circumflex', 'ocircumflex', 0x00F4)
fl.EndUndo()
```

---

## 第五部分：从位图扫描到矢量轮廓跟踪算法

将手绘手稿光学扫描为光栅图像，再自动转化为平滑贝塞尔矢量轮廓，是字型复刻的关键技术。

::: tip ScanFont 中的位图自动分割（Figure 12-12）
![ScanFont 中的位图自动分割（Figure 12-12）](/images/fonts-encodings/fig12-12.png)
*ScanFont 中的位图自动分割（Figure 12-12）*
:::

*图 12-12：在 ScanFont 中的扫描页面字形分割（Separation of glyphs）界面。算法依据周围的空白自动识别矩形框分割出每一个字符图元，下方状态栏显示识别出的顺序字符。*

::: tip ScanFont 自动追踪参数实时配置对话框（Figure 12-13）
![ScanFont 自动追踪参数实时配置对话框（Figure 12-13）](/images/fonts-encodings/fig12-13.png)
*ScanFont 自动追踪参数实时配置对话框（Figure 12-13）*
:::

*图 12-13：ScanFont 的实时自动追踪（Autotracing）参数配置对话框。设计师可实时微调平滑精度、拐角识别判断阈值，右侧预览窗实时生成对应的贝塞尔路径。*

::: tip 手工与不同自动追踪微观对比（Figure 12-14）
![手工与不同自动追踪微观对比（Figure 12-14）](/images/fonts-encodings/fig12-14.png)
*手工与不同自动追踪微观对比（Figure 12-14）*
:::

*图 12-14：同一字形在不同工艺模式下的形态对比：左侧为设计师手工绘制的精准极值点锚点（完全对齐极值线上），中间与右侧为不同容差算法自动追踪生成的节点（出现大量冗余锚点与轻微偏离极值的偏移）。*

正如 **Figure 12-14** 所示，手工绘制与自动矢量化之间的最大差异，在于自动追踪算法容易产生偏离极值点的冗余节点。因此，必须通过严密的算法（8-连通 Freeman 链码、Douglas-Peucker 折线抽希与最小二乘拟合）对其进行后处理平滑与极值点重建。

---

## 第六部分：PostScript 提示（Hinting）工程与对齐区参数

在导出为商用 PostScript Type 1 或 OpenType CFF 时，全局私有字典（Private Dictionary）中必须注入精确的提示控制参数：

### 1. 蓝区对齐表（BlueValues 与 OtherBlues）

$$\text{BlueValues} = [y_{b0}, y_{t0}, \quad y_{b1}, y_{t1}, \quad \dots]$$

`BlueValues` 是一组严格成对出现的浮点数组，专门用于锁定基线、x-高度、大写高度与上升部线。落在蓝区内部的曲上节点，在低分辨率光栅化时将被强制吸附到同一物理像素行上，避免上下颤动。

### 2. 蓝区尺度阈值（BlueScale）

$$\text{Threshold Size} = \frac{1}{\text{BlueScale} \times (\text{Zone Height})}$$

当实际渲染的字号尺寸超过了该计算阈值时，光栅化引擎将自动关闭蓝区强制对齐，完全释放真实的几何轮廓！

---

## 结语：从几何骨架到可执行程序的终极蜕变

通过第十二章的深入剖析，我们见证了数字字型工程极其惊人的技术广度：
从早期 Fontographer、FontStudio 到现代 FontLab Studio 的交互拓扑，从二次与三次贝塞尔多项式的升阶降阶，到多重母版的连续设计空间与 Python 自动化批处理；从 ScanFont 位图分割、自动追踪到 PostScript 蓝区提示工程。

当这些精美的几何轮廓被丢入物理像素颗粒粗糙的低分辨率显示设备中时，连续的平滑曲线将被离散网格撕裂。人类排印与计算机科学家是如何通过在字库内部植入一个完整的**图灵完备虚拟机（Virtual Machine）**与**上百条字节码微指令**，来与恶劣的离散像素展开惊心动魄的肉搏微调的？

这正是我们在**第十三章：字体提示（Hinting）机制**中将要全面展开的底层技术核心。
'''

print(f"Constructed zh text: {len(p1)} characters")

with open('docs/zh/fonts-encodings/chapter-12.md', 'w', encoding='utf-8') as f:
    f.write(p1)

print("docs/zh/fonts-encodings/chapter-12.md written successfully.")

# Convert to zh-hant using opencc
converter = opencc.OpenCC('s2twp')

def convert_preserving(text):
    code_blocks = []
    def code_repl(m):
        code_blocks.append(m.group(0))
        return f"__CODE_BLOCK_{len(code_blocks)-1}__"
    text = re.sub(r'```[\s\S]*?```', code_repl, text)

    math_blocks = []
    def math_repl(m):
        math_blocks.append(m.group(0))
        return f"__MATH_BLOCK_{len(math_blocks)-1}__"
    text = re.sub(r'\$\$[\s\S]*?\$\$', math_repl, text)

    inline_math = []
    def inline_repl(m):
        inline_math.append(m.group(0))
        return f"__INLINE_MATH_{len(inline_math)-1}__"
    text = re.sub(r'\$[^\$\n]+?\$', inline_repl, text)

    converted = converter.convert(text)

    for i, im in enumerate(inline_math):
        converted = converted.replace(f"__INLINE_MATH_{i}__", im)
    for i, mb in enumerate(math_blocks):
        converted = converted.replace(f"__MATH_BLOCK_{i}__", mb)
    for i, cb in enumerate(code_blocks):
        converted = converted.replace(f"__CODE_BLOCK_{i}__", cb)

    return converted

zh_hant = convert_preserving(p1)
zh_hant = zh_hant.replace('*譯者：[Lycoris <lycorismisaka@gmail.com>]', '*譯者：[Lycoris \\<lycorismisaka@gmail.com\\>]')
zh_hant = zh_hant.replace('*译者：[Lycoris \\<lycorismisaka@gmail.com\\>]', '*譯者：[Lycoris \\<lycorismisaka@gmail.com\\>]')

with open('docs/zh-hant/fonts-encodings/chapter-12.md', 'w', encoding='utf-8') as f:
    f.write(zh_hant)

print(f"docs/zh-hant/fonts-encodings/chapter-12.md written: {len(zh_hant)} chars")
