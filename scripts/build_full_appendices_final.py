# -*- coding: utf-8 -*-
"""
Assembles docs/zh/fonts-encodings/appendices.md
Target: >= 140,000 characters
"""
import os, re

from scripts.app_builders.build_app_a import get_appendix_a
from scripts.app_builders.build_app_b import get_appendix_b
from scripts.app_builders.build_app_c import get_appendix_c
from scripts.app_builders.build_app_d import get_appendix_d
from scripts.app_builders.build_app_e import get_appendix_e
from scripts.app_builders.build_app_f import get_appendix_f
from scripts.app_builders.build_app_g import get_appendix_g

apps = [
    get_appendix_a(),
    get_appendix_b(),
    get_appendix_c(),
    get_appendix_d(),
    get_appendix_e(),
    get_appendix_f(),
    get_appendix_g(),
]

# Strip inner translator lines
cleaned_apps = []
for a in apps:
    # remove translator line
    cleaned = re.sub(r'\*译者：\[.*?\]\(mailto:.*?\)\*\n*', '', a)
    cleaned_apps.append(cleaned.strip())

header = """---
title: "附录 A–G：底层格式与数学技术参考全景指南"
description: "涵盖位图字体 (A)、TeX/Omega (B)、PostScript Type 1/CFF (C)、TrueType/OpenType 结构与目录 (D)、METAFONT 与画笔几何 (E/F)、TrueType 虚拟机微指令集、以及曲线微分几何学 (G)。"
---

# 附录 A–G：底层格式与数学技术参考全景指南
### Appendices A–G: Technical Reference Manual for Digital Typography
选自《Fonts & Encodings》附录 A 至 G 全 340 页参考手册
*译者：[Lycoris \\<lycorismisaka@gmail.com\\>](mailto:lycorismisaka@gmail.com)*

---

本参考手册汇集了《Fonts & Encodings》全书后半部全七大技术附录（Appendices A 至 G）。这部分是雅尼斯·哈拉兰博斯（Yannis Haralambous）为字型工程师、底层排版系统开发者以及数学爱好者构筑的坚实基石，详尽记录了从 20 世纪 80 年代点阵位图格式到 21 世纪现代 OpenType/AAT 容器结构、TrueType 虚拟机约 130 条微指令集、以及曲线微分几何学的全套数学实现与工业级规范。

---
"""

full_zh = header.strip() + '\n\n' + '\n\n---\n\n'.join(cleaned_apps) + '\n'

with open('docs/zh/fonts-encodings/appendices.md', 'w', encoding='utf-8') as out:
    out.write(full_zh)

print(f"Successfully generated docs/zh/fonts-encodings/appendices.md: {len(full_zh):,} characters")
print(f"Target is >= 137,719 characters. Ratio: {len(full_zh) / 125199:.2f}")
