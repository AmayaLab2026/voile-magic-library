# -*- coding: utf-8 -*-
"""
Synchronize display math blocks between ZH, ZH-HANT, and JA.
"""
import sys, re

# Fix chapter-9.md in JA
with open('docs/ja/fonts-encodings/chapter-9.md', 'r', encoding='utf-8') as f:
    ja_ch9 = f.read()

ja_ch9 = ja_ch9.replace(
    '$$1\\text{ pt} = 65,536\\text{ sp} = 2^{16}\\text{ sp}$$\n\n$$1\\text{ sp} \\approx 5.363\\text{ nm（ナノメートル）}$$',
    '$$1\\text{ pt} = 65,536\\text{ sp} = 2^{16}\\text{ sp}$$\n\n$$1\\text{ sp} \\approx 5.363 \\times 10^{-6}\\text{ mm} = 5.363\\text{ nm}$$\n'
)
ja_ch9 = ja_ch9.replace(
    '（$\\text{slant} = \\tan \\theta$）；',
    '：\n$$\\begin{pmatrix} x\' \\\\ y\' \\end{pmatrix} = \\begin{pmatrix} 1 & \\text{slant} \\\\ 0 & 1 \\end{pmatrix} \\begin{pmatrix} x \\\\ y \\end{pmatrix}$$\n通常、`-s 0.167`（約 $9.5^\\circ$ の傾き、$\\text{slant} = \\tan \\theta$）などを指定します；'
)
ja_ch9 = ja_ch9.replace(
    '- `LIG`（$A + B \\to C$，クラシック完全置換）；\n- `/LIG`（$A + B \\to A + C$，後方置換・前方保持）；\n- `LIG/`（$A + B \\to C + B$，前方置換・後方保持）；\n- `/LIG/`（$A + B \\to A + C + B$，文脈保持・中間挿入）。',
    '1. **`LIG`（完全置換）**：\n$$A + B \\to C$$\n入力文字 $A$ と $B$ を消費し、合字 $C$ を出力；\n2. **`/LIG`（後方置換・前方保持）**：\n$$A + B \\to A + C$$\n3. **`LIG/`（前方置換・後方保持）**：\n$$A + B \\to C + B$$\n4. **`/LIG/`（文脈保持・中間挿入）**：\n$$A + B \\to A + C + B$$'
)
with open('docs/ja/fonts-encodings/chapter-9.md', 'w', encoding='utf-8') as f:
    f.write(ja_ch9)

# Fix chapter-12.md in JA
with open('docs/ja/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    ja_ch12 = f.read()

ja_ch12 = ja_ch12.replace(
    'ドラッグして LSB と RSB をリアルタイム変更可能。',
    'ドラッグして LSB と RSB をリアルタイム変更可能：\n$$\\text{Advance Width} = \\text{LSB} + \\text{Bounding Box Width} + \\text{RSB}$$'
)
ja_ch12 = ja_ch12.replace(
    '3 次ベジェと 2 次ベジェの可逆的な双方向変換；',
    '3 次ベジェと 2 次ベジェの可逆的な双方向変換：\n$$\\mathbf{Q}_0 = \\mathbf{P}_0, \\quad \\mathbf{Q}_1 = \\mathbf{P}_0 + \\frac{2}{3}(\\mathbf{P}_1 - \\mathbf{P}_0), \\quad \\mathbf{Q}_2 = \\mathbf{P}_2 + \\frac{2}{3}(\\mathbf{P}_1 - \\mathbf{P}_2), \\quad \\mathbf{Q}_3 = \\mathbf{P}_2$$\nにより二次曲線を無損失で三次曲線へ昇格；'
)
ja_ch12 = ja_ch12.replace(
    '`BlueValues` は、ベースラインや x-height の微小なオーバーシュート（Overshoot）を管理する整数のペア配列です：',
    '`BlueValues` は、整数のペア配列です：\n$$\\text{BlueValues} = [y_{b0}, y_{t0}, \\quad y_{b1}, y_{t1}, \\quad \\dots]$$'
)
ja_ch12 = ja_ch12.replace(
    '- 画面サイズが閾値（`BlueScale` による計算値）より小さい場合',
    '- 画面サイズが閾値サイズより小さい場合：\n$$\\text{Threshold Size} = \\frac{1}{\\text{BlueScale} \\times (\\text{Zone Height})}$$'
)
with open('docs/ja/fonts-encodings/chapter-12.md', 'w', encoding='utf-8') as f:
    f.write(ja_ch12)

# Fix chapter-14.md in JA
with open('docs/ja/fonts-encodings/chapter-14.md', 'r', encoding='utf-8') as f:
    ja_ch14 = f.read()

ja_ch14 = ja_ch14.replace(
    '階層構造：$\\text{Scripts} \\to \\text{Languages} \\to \\text{Features} \\to \\text{Lookups}$；',
    '階層構造：\n$$\\text{Scripts} \\longrightarrow \\text{Languages} \\longrightarrow \\text{Features} \\longrightarrow \\text{Lookups}$$\n'
)
with open('docs/ja/fonts-encodings/chapter-14.md', 'w', encoding='utf-8') as f:
    f.write(ja_ch14)

# Fix appendices.md in ZH-HANT and JA
for lang in ['zh-hant', 'ja']:
    path = f'docs/{lang}/fonts-encodings/appendices.md'
    with open(path, 'r', encoding='utf-8') as f:
        app = f.read()
    
    # 1. fix L formula
    app = re.sub(
        r'動的圧縮アルゴリズム.*?Tomas Rokicki|動態壓縮演算法.*?Tomas Rokicki',
        lambda m: m.group(0),
        app
    )
    if 'nibble_1' not in app:
        app = app.replace(
            '4 ビットニブル（Nibble）パッキングと行反復',
            'ランレングス $L$ の計算：\n$$L = (nibble_1 - dyn\\_f - 1) \\times 16 + nibble_2 + dyn\\_f + 1$$\n4 ビットニブルパッキングと行反復'
        )
        app = app.replace(
            '較長遊程以兩個或三個半位元組編碼；',
            '較長遊程以兩個或三個半位元組編碼：\n$$L = (nibble_1 - dyn\\_f - 1) \\times 16 + nibble_2 + dyn\\_f + 1$$\n'
        )

    # 2. fix fix_word
    app = app.replace(
        '$$\\text{fix\\_word} =',
        '$$1\\text{ fix\\_word} ='
    )

    # 3. fix Bernstein properties
    if '\\sum_{i=0}^n B_{i,n}(t)' not in app:
        app = app.replace(
            '単位の分割 $\\sum B_{i,n}(t) \\equiv 1$ と非負性により、ベジェ曲線の**凸包性（Convex Hull Property）**が保証されます。',
            '1. **単位の分割（Partition of Unity）**：\n$$\\sum_{i=0}^n B_{i,n}(t) \\equiv 1, \\quad \\forall t \\in \\mathbb{R}$$\n2. **非負性（Non-negativity）**：\n$$B_{i,n}(t) \\ge 0, \\quad \\forall t \\in [0, 1]$$\nこれによりベジェ曲線の**凸包性（Convex Hull Property）**が保証されます。'
        )
        app = app.replace(
            '單位分解性 $\\sum B_{i,n}(t) \\equiv 1$ 與非負性保證了**凸包性（Convex Hull Property）**。',
            '1. **單位分解性（Partition of Unity）**：\n$$\\sum_{i=0}^n B_{i,n}(t) \\equiv 1, \\quad \\forall t \\in \\mathbb{R}$$\n2. **非負性（Non-negativity）**：\n$$B_{i,n}(t) \\ge 0, \\quad \\forall t \\in [0, 1]$$\n這保證了貝塞爾曲線的**凸包性（Convex Hull Property）**。'
        )

    with open(path, 'w', encoding='utf-8') as f:
        f.write(app)

print("Math synchronization complete.")
