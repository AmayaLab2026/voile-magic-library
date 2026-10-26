# -*- coding: utf-8 -*-
import sys

# 1. In docs/ja/fonts-encodings/chapter-12.md:
with open('docs/ja/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    ja12 = f.read()

target12 = "文字間の空きをクラス単位で管理する**メトリッククラス（Metric Classes）**により"
replacement12 = """送り幅とサイドベアリングの幾何関係：
$$\\text{Advance Width} = \\text{LSB} + \\text{Bounding Box Width} + \\text{RSB}$$

文字間の空きをクラス単位で管理する**メトリッククラス（Metric Classes）**により"""

ja12 = ja12.replace(target12, replacement12)
with open('docs/ja/fonts-encodings/chapter-12.md', 'w', encoding='utf-8') as f:
    f.write(ja12)

# 2. In docs/ja/fonts-encodings/appendices.md:
with open('docs/ja/fonts-encodings/appendices.md', 'r', encoding='utf-8') as f:
    ja_app = f.read()

target_app = "1 の分割 $\\sum B_{i,n}(t) \\equiv 1$ と非負性により、ベジェ曲線の**凸包性（Convex Hull Property）**が保証されます。"
replacement_app = """1. **1 の分割（Partition of Unity）**：
$$\\sum_{i=0}^n B_{i,n}(t) \\equiv 1, \\quad \\forall t \\in \\mathbb{R}$$
2. **非負性（Non-negativity）**：
$$B_{i,n}(t) \\ge 0, \\quad \\forall t \\in [0, 1]$$
これによりベジェ曲線の**凸包性（Convex Hull Property）**が保証されます。"""

ja_app = ja_app.replace(target_app, replacement_app)
with open('docs/ja/fonts-encodings/appendices.md', 'w', encoding='utf-8') as f:
    f.write(ja_app)

print("Injected missing math blocks into JA.")
