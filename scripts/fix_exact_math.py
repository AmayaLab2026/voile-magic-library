# -*- coding: utf-8 -*-
import sys

# 1. Fix docs/ja/fonts-encodings/chapter-12.md
with open('docs/ja/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    ja12 = f.read()

ja12 = ja12.replace(
    'ドラッグして LSB と RSB をリアルタイム変更可能：',
    'ドラッグして LSB と RSB をリアルタイム変更可能：\n$$\\text{Advance Width} = \\text{LSB} + \\text{Bounding Box Width} + \\text{RSB}$$\n'
)
with open('docs/ja/fonts-encodings/chapter-12.md', 'w', encoding='utf-8') as f:
    f.write(ja12)

# 2. Fix docs/ja/fonts-encodings/appendices.md
with open('docs/ja/fonts-encodings/appendices.md', 'r', encoding='utf-8') as f:
    ja_app = f.read()

# Replace fix_word formula in JA to match ZH format with \text{整数値}
zh_app_text = open('docs/zh/fonts-encodings/appendices.md', encoding='utf-8').read()

# Let's align fix_word in JA and ZH-HANT to use a clean formula:
formula_fixword = r"""$$1\text{ fix\_word} = \frac{\text{Value}}{2^{20}} = \frac{\text{Value}}{1,048,576} \times (\text{Design Size})$$"""

# Replace in zh, zh-hant, and ja
for p in ['docs/zh/fonts-encodings/appendices.md', 'docs/zh-hant/fonts-encodings/appendices.md', 'docs/ja/fonts-encodings/appendices.md']:
    txt = open(p, encoding='utf-8').read()
    txt = txt.replace(
        r"""$$1\text{ fix\_word} = \frac{\text{物理整数值}}{2^{20}} = \frac{\text{物理整数值}}{1,048,576} \times (\text{Design Size})$$""",
        formula_fixword
    )
    txt = txt.replace(
        r"""$$1\text{ fix\_word} = \frac{\text{物理整數值}}{2^{20}} = \frac{\text{物理整數值}}{1,048,576} \times (\text{Design Size})$$""",
        formula_fixword
    )
    txt = txt.replace(
        r"""$$1\text{ fix\_word} = \frac{\text{整数値}}{2^{20}} = \frac{\text{整数値}}{1,048,576} \times (\text{Design Size})$$""",
        formula_fixword
    )
    # Also separate R_{n+1} and C_n
    txt = txt.replace(
        r"""$$R_{n+1} = (R_n \times 52845 + 22719) \bmod 65536, \quad C_n = P_n \oplus (R_n \gg 8)$$""",
        "$$R_{n+1} = (R_n \\times 52845 + 22719) \\bmod 65536$$\n$$C_n = P_n \\oplus (R_n \\gg 8)$$"
    )
    # Ensure Bernstein 7 & 8 are display math
    if "$$\\sum_{i=0}^n B_{i,n}(t)" not in txt:
        txt = txt.replace(
            "1. **単位の分割（Partition of Unity）**：\n$$\\sum_{i=0}^n B_{i,n}(t) \\equiv 1, \\quad \\forall t \\in \\mathbb{R}$$\n2. **非負性（Non-negativity）**：\n$$B_{i,n}(t) \\ge 0, \\quad \\forall t \\in [0, 1]$$",
            "$$\\sum_{i=0}^n B_{i,n}(t) \\equiv 1, \\quad \\forall t \\in \\mathbb{R}$$\n\n$$B_{i,n}(t) \\ge 0, \\quad \\forall t \\in [0, 1]$$"
        )
    open(p, 'w', encoding='utf-8').write(txt)

print("Exact math alignment complete.")
