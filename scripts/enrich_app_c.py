# -*- coding: utf-8 -*-
"""
Enriches app_c.md with MM PostScript code, ROS collections, and CharString disassembly.
Target: ~26,000 characters
"""

extra_c_2 = r"""
---

## C.8 多重母版字体（Multiple Master）动态实例生成实战

在 PostScript 解释器内部，用户可以通过动态混合（Blend）直接派生出全新的物理字体实例：

```postscript
% 查找基础多重母版字体
/MinionMM findfont

% 在二维设计空间中定义归一化插值坐标：
% 字重轴权重 0.45 (Light到Black之间)，字宽轴权重 0.80 (紧缩到宽体之间)
[0.45 0.80] makeblendedfont

% 将生成的派生字体注册为全局字体
/Minion-Custom findfont
12 scalefont
setfont

% 在页面上排版输出
100 700 moveto
(Voile Magic Library: Multiple Master Dynamic Instance) show
showpage
```

### 线性与非线性空间插值微积分：
在实际工程中，字体设计师往往要求插值不是简单的线性渐变，而是遵循视觉平衡曲线。Adobe MM 引入了 `NormalizeDesignVector` 映射函数：
对于设计轴输入坐标 $d_j \in [D_{j, \min}, D_{j, \max}]$，通过分段线性查找表将其非线性映射为归一化混合标量 $w_j \in [0, 1]$，再通过 Kronecker 积计算最终的 $2^k$ 个极端母版加权矩阵：

$$\mathbf{W} = \bigotimes_{j=1}^k \begin{pmatrix} 1 - w_j \\ w_j \end{pmatrix}$$

这一数学框架，成为了二十五年后现代 OpenType 1.8 矢量可变字体（Variable Fonts / Variations `fvar`, `gvar`, `HVAR`, `MVAR`）的理论祖先！

---

## C.9 东亚巨型字符集 ROS（Registry-Ordering-Supplement）全景谱系

在 CID-keyed 字体体系中，字符集的版本与规模由 **ROS 三元组** 严格定义：

| 字符集集合名称 | 适用的文字与国家/地区 | 字符总数 (Supplement) | 核心涵盖范围与标准 |
| :--- | :--- | :--- | :--- |
| **Adobe-Japan1-6** | 日文（汉字 Kanji、平假名、片假名） | 23,058 字形 (Supp 6) | JIS X 0208, JIS X 0213, JIS X 0212, 印刷用人名汉字变体、纵排变体 |
| **Adobe-GB1-5** | 中国大陆简体中文 | 30,284 字形 (Supp 5) | GB 2312, GB 13000.1, GBK, GB 18030-2000, 繁体字及少数民族拼音 |
| **Adobe-CNS1-7** | 中国台湾/香港繁体中文 | 19,088 字形 (Supp 7) | Big5, Big-5E, CNS 11643 第 1-15 字母字面、香港增补字符集 (HKSCS) |
| **Adobe-Korea1-2** | 韩国与朝鲜谚文（Hangul）及汉字 | 18,352 字形 (Supp 2) | KS X 1001, KS X 1002, 常用谚文音节块及韩国古汉字 |

每一个 Supplement 保持绝对的**向后单调递增兼容性**：新版本仅在数组末尾追加全新的 CID 编号，绝不修改或删除既有的历史 CID，彻底杜绝了跨版本文档重新排版时的文字跑位风险！
"""

with open('scripts/app_builders/app_c.md', 'r', encoding='utf-8') as f:
    text_c = f.read()

full_c = text_c.strip() + '\n' + extra_c_2.strip() + '\n'

with open('scripts/app_builders/app_c.md', 'w', encoding='utf-8') as f:
    f.write(full_c)

print("Successfully expanded scripts/app_builders/app_c.md, total length:", len(full_c))
