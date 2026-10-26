# -*- coding: utf-8 -*-
"""
Extra detailed sections for Appendix D Section 2
Covers name, post, gasp, vhea, vmtx, VORG, DSIG
Target: ~10,000 characters
"""

extra = r"""---

### 7. `name` 表（全文字多语言命名与版权信息表）
`name` 表是字库的人事档案库。为了确保同一款字体能够在英语 Windows、繁体中文 Mac OS、日文 X11 等异构操作系统的字体选择菜单中正确显示出本地化名称，`name` 表定义了精密的多语言命名记录结构：

```xml
<!-- TTX XML 表达范例 -->
<name>
  <namerecord nameID="0" platformID="3" platEncID="1" langID="0x409">
    Copyright © 2007 Adobe Systems Incorporated. All Rights Reserved.
  </namerecord>
  <namerecord nameID="1" platformID="3" platEncID="1" langID="0x409">
    Adobe Garamond Pro
  </namerecord>
  <namerecord nameID="2" platformID="3" platEncID="1" langID="0x409">
    Regular
  </namerecord>
  <namerecord nameID="3" platformID="3" platEncID="1" langID="0x409">
    2.000;ADBE;AGaramondPro-Regular;ADOBE
  </namerecord>
  <namerecord nameID="4" platformID="3" platEncID="1" langID="0x409">
    Adobe Garamond Pro Regular
  </namerecord>
  <namerecord nameID="6" platformID="3" platEncID="1" langID="0x409">
    AGaramondPro-Regular
  </namerecord>
</name>
```

#### 关键标准 NameID 权威词典：
* **NameID 0**：版权所有声明（Copyright Notice）；
* **NameID 1**：字体家族名（Font Family Name，如 "Adobe Garamond Pro"）；
* **NameID 2**：字体子样式名称（Font Subfamily Name，如 "Regular", "Bold", "Italic"）；
* **NameID 3**：全字库唯一标识字符串（Unique Font Identifier）；
* **NameID 4**：人机友好的全名字串（Full Font Name，通常为 Family + Subfamily）；
* **NameID 5**：版本号字符串（Version string，如 "Version 2.000;PS 002.000"）；
* **NameID 6**：PostScript 打印机驱动识别名（PostScript Name，**严禁包含空格与非 ASCII 字符**，激光打印机通过该名称在显存中精准挂接字库！）；
* **NameID 7**：注册商标声明（Trademark Notice）；
* **NameID 8**：字体制造商（Manufacturer Name）；
* **NameID 9**：字体设计师（Designer）；
* **NameID 11**：厂商官方网址 URL；
* **NameID 16**：排版首选家族名（Typographic Family Name，解决传统办公软件 4 字重限制的拓展家族名）；
* **NameID 17**：排版首选子样式名（Typographic Subfamily Name，支持 Thin, Light, Semibold, ExtraBold 等丰富层级）；
* **NameID 25**：OpenType 可变字体（Variable Fonts）的 PostScript 命名变化前缀。

---

### 8. `post` 表（PostScript 驱动与字形名称表）
`post` 表最初由苹果设计，用于向 PostScript 打印机转储必要的度量与字形名称：
* **Format 1.0**：恒定包含苹果 Macintosh 操作系统早期标准的 258 个拉丁字形名称（无需在字体中存储任何字符名称字符串，节约内存）；
* **Format 2.0**：最经典的 TrueType 字形命名格式！包含一个 16 位字符编号映射数组与一个连续 Pascal 字符串数组（每个字符串前带 1 字节长度），支持为数万个非标准字形赋予自定义的 ASCII 符号名称；
* **Format 3.0**：**零名称极简格式**！完全不存储任何字形名称字符串。当字体发布用于网页嵌入（Web Fonts / WOFF）或移动端系统固件时，通常采用 Format 3.0 以剥离所有无关字符串，削减数十千字节的文件开销。

```c
struct PostTableFormat2 {
    uint32 format;              /* 0x00020000 */
    int32  italicAngle;         /* 16.16 定点数倾斜角 */
    int16  underlinePosition;   /* 下划线基准线垂直偏移 */
    int16  underlineThickness;  /* 下划线宽度 */
    uint32 isFixedPitch;        /* 是否等宽 */
    uint32 minMemType42;        /* 激光照排机下载 Type 42 所需的最小内存 */
    uint32 maxMemType42;
    uint32 minMemType1;
    uint32 maxMemType1;
    uint16 numGlyphs;           /* 包含的字形总数 */
    uint16 glyphNameIndex[numGlyphs]; /* 指向标准 258 符号或后续自定义字符串的索引数组 */
    /* 紧随其后为 Pascal-string 连续数组: uint8 length + char data[length] */
};
```

---

### 9. `gasp` 表（网格自适应与抗锯齿平滑控制表）
`gasp`（Grid-fitting and Scan-conversion Procedure Table）是 Windows 操作系统在执行屏幕抗锯齿与 ClearType 亚像素渲染时极其关键的决策调度表。

它针对不同的屏幕显示每 Em 像素尺寸（PPEM），精细控制何时启用 TrueType 指令（Grid-fitting）、何时启用灰度平滑（Grayscale Smoothing）、以及何时启用 ClearType 对称平滑：

```xml
<gasp>
  <version value="1"/>
  <gaspRange rangeMaxPPEM="8" rangeGaspBehavior="2"/> <!-- 仅执行灰度平滑，关闭提示 -->
  <gaspRange rangeMaxPPEM="16" rangeGaspBehavior="1"/> <!-- 极小字号：强行开启网格提示对齐 -->
  <gaspRange rangeMaxPPEM="2048" rangeGaspBehavior="15"/> <!-- 正常与大字号：同时开启微指令、灰度与 ClearType 平滑 -->
  <gaspRange rangeMaxPPEM="65535" rangeGaspBehavior="14"/> <!-- 超大海报：关闭微指令，仅执行全平滑 -->
</gasp>
```

#### `rangeGaspBehavior` 四大标志位位域：
* **Bit 0 (`GASP_GRIDFIT`)**：在此分辨率下激活 TrueType 虚拟机执行轮廓对齐；
* **Bit 1 (`GASP_DOGRAY`)**：在此分辨率下启用标准单色灰度抗锯齿；
* **Bit 2 (`GASP_SYMMETRIC_SMOOTHING`)**：针对 ClearType 激活水平亚像素平滑；
* **Bit 3 (`GASP_SYMMETRIC_GRIDFIT`)**：激活 ClearType 对称网格对齐。

---

### 10. `vhea`、`vmtx` 与 `VORG`（垂直排版核心度量体系）
在中文、日文、韩文与传统蒙古文等东亚竖排排版中，字形并非沿着水平基线从左向右推进，而是**沿着垂直中轴线从上向下流动**！

OpenType 为此定义了完整的垂直度量表簇：
* **`vhea`（Vertical Header Table）**：
  * `vertTypoAscender` / `vertTypoDescender`：垂直排版升部与降部；
  * `vertTypoLineGap`：垂直行距；
  * `advanceHeightMax`：全字库最大垂直前进高度；
  * `minTopSideBearing` / `minBottomSideBearing`：全局最小顶部与底部轴承；
  * `numOfLongVerMetrics`：在 `vmtx` 中拥有独立垂直度量的字符数。
* **`vmtx`（Vertical Metrics Table）**：
  * 与 `hmtx` 完全同构，存储每个字符的 `advanceHeight`（垂直前进高，通常为一个全角 Em 高度）与 `topSideBearing`（顶部轴承，即基字顶部距前一字符绘制基线的间隙）；
* **`VORG`（Vertical Origin Table，垂直绘制原点表）**：
  * 在 CFF OpenType 中，由于三次贝塞尔曲线坐标系天然以左下角为设计原点，在垂直排版时需要将原点平移到字符顶部的几何中心。`VORG` 表通过一个紧凑的默认高度与特异字典，为每个字形直接宣告其在垂直排版时的绝对中心原点 Y 坐标（`vertOriginY`），使得排版引擎在进行竖排变换时无需重新解压和计算庞大的 `glyf` 轮廓包围盒！
"""

with open('scripts/app_builders/app_d_sec2_extra.md', 'w', encoding='utf-8') as f:
    f.write(extra.strip() + '\n')
print("Section 2 Extra written, length:", len(extra))
