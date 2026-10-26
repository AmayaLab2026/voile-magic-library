# -*- coding: utf-8 -*-
"""
Enriches app_d.md with Section D.11: OpenType 1.8 Variable Fonts (fvar, gvar, HVAR, MVAR).
Target: ~46,000 characters total for app_d.md
"""

extra_d_4 = r"""
---

## D.11 OpenType 1.8 矢量可变字体（Variable Fonts）体系演进

2016 年 9 月，苹果、微软、Adobe 与 Google 在波兰华沙的 ATypI 大会上联合发布了历史性的 **OpenType 1.8 规范**。该规范引入了源自苹果 TrueType GX 与 Adobe Multiple Master 的集大成者——**OpenType 字体可变机制（OpenType Font Variations）**。

### 1. `fvar` 表（字体变化轴与命名实例表）
`fvar`（Font Variations Table）定义了字体在 $k$ 维设计空间中的连续变化轴线：

```xml
<fvar>
  <!-- 声明五大注册标准设计轴之一：字重轴 (wght) -->
  <Axis>
    <AxisTag value="wght"/>
    <Flags value="0x0000"/>
    <MinValue value="100.0"/>
    <DefaultValue value="400.0"/>
    <MaxValue value="900.0"/>
    <AxisNameID value="256"/>
  </Axis>
  <!-- 声明字宽轴 (wdth) -->
  <Axis>
    <AxisTag value="wdth"/>
    <Flags value="0x0000"/>
    <MinValue value="75.0"/>
    <DefaultValue value="100.0"/>
    <MaxValue value="125.0"/>
    <AxisNameID value="257"/>
  </Axis>

  <!-- 预定义命名的静态样式快照 (Named Instances) -->
  <NamedInstance nameID="258"> <!-- "Light Condensed" -->
    <Coordinates>
      <Coord axis="wght" value="300.0"/>
      <Coord axis="wdth" value="75.0"/>
    </Coordinates>
  </NamedInstance>
  <NamedInstance nameID="259"> <!-- "Bold" -->
    <Coordinates>
      <Coord axis="wght" value="700.0"/>
      <Coord axis="wdth" value="100.0"/>
    </Coordinates>
  </NamedInstance>
</fvar>
```

#### 五大国际注册标准轴标签（Standard Registered Axes）：
* **`wght`（Weight / 字重轴）**：取值范围 $1 \dots 1000$（400 为 Regular，700 为 Bold）；
* **`wdth`（Width / 字宽轴）**：以基准设计宽度的百分比衡量（75% Condensed 至 125% Expanded）；
* **`slnt`（Slant / 倾斜角轴）**：文字顺时针倾斜度数（正数为倾斜度，如 $-12$）；
* **`ital`（Italic / 意大利体轴）**：二元或连续轴（0 代表正体 Roman，1 代表真正的手写斜体 Italic）；
* **`opsz`（Optical Size / 视觉字号轴）**：指示字体当前排版使用的物理磅值（如 6pt 至 72pt），引擎据此自动调整笔画粗细对比度与字距。

---

### 2. `gvar` 表（字形变化量数据表 Tuple Variation Store）
在可变字体中，基础轮廓仅存储在 `glyf` 表中（默认母版坐标）。当用户在 CSS 中指定 `font-weight: 550` 时，渲染引擎查询 `gvar` 表：
* 每个轮廓控制点存储的不是绝对坐标，而是一组**变化量差分向量（Delta Vectors: $\Delta x, \Delta y$）**；
* 通过 **元组变化存储器（Tuple Variation Store）** 算法，引擎将用户输入的浮点轴向坐标映射为归一化标量因数；
* 最终物理轮廓点由默认坐标与各轴向 Delta 的标量加权和瞬间线性计算得出：
  $$\mathbf{P}_{\text{rendered}} = \mathbf{P}_{\text{default}} + \sum_{i=1}^m \text{Scalar}_i \times \Delta \mathbf{P}_i$$

不仅轮廓点，OpenType 1.8 更引入了 `HVAR`（水平度量变化表）与 `MVAR`（全局度量变化表），动态联动调整升部、降部与字宽，使原本需要包含数十个独立 `.ttf` 文件（总计数十兆字节）的巨型家族，以**单一紧凑文件（通常仅增加 20% 体积）**的形式完整覆盖了无限连续维度的排印设计空间！
"""

with open('scripts/app_builders/app_d.md', 'r', encoding='utf-8') as f:
    text_d = f.read()

full_d = text_d.strip() + '\n' + extra_d_4.strip() + '\n'

with open('scripts/app_builders/app_d.md', 'w', encoding='utf-8') as f:
    f.write(full_d)

print("Successfully expanded scripts/app_builders/app_d.md, total length:", len(full_d))
