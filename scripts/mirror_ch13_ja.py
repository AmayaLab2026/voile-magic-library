# -*- coding: utf-8 -*-
"""
Mirror expansions to docs/ja/fonts-encodings/chapter-13.md:
- Matches all 13 figures
- Adds the 2 display math blocks
"""
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open('docs/ja/fonts-encodings/chapter-13.md', encoding='utf-8') as f:
    ja_text = f.read()

ja_expansion = r'''

---

## 5. FreeType 仮想マシン、自動ヒンティング（Auto-hinter）とサブピクセル描画

現代のデジタルタイポグラフィ環境において、オープンソースの **FreeType** ライブラリ（David Turner、Robert Wilhelm、Werner Lemberg らが創設）は、Linux、Android、ChromeOS などのプラットフォームで文字描画の中核を担っています。

### 1. アップル特許紛争とオープンソースの克服

1990年代初頭、アップルは TrueType のヒンティング技術に関して広範な特許（Auto-flipping、投影ベクトルと自由ベクトル、CVT Cut-In 閾値制御）を取得しました。商用 Linux ディストリビューションに対する特許侵害訴訟のリスクを回避するため、FreeType は長年にわたりバイトコード仮想マシンの実装をデフォルトで無効化（`#define TT_CONFIG_OPTION_BYTECODE_INTERPRETER` をコメントアウト）せざるを得ませんでした。2010年頃、これら特許の保護期間（20年）が満了したことで、FreeType は完全なバイトコード解釈系を公式に標準有効化しました。

### 2. FreeType 自動ヒンティング（Auto-hinter）アルゴリズム

特許封鎖の時代に開発された FreeType Auto-hinter は、フォント内部の命令に依存せず、ベジェ曲線から直接グリフの骨格を解析する高度な数学的パイプラインです：
1. **セグメント解析（Segment Analysis）**：曲線の1次導関数（速度ベクトル）を計算し、水平・垂直に近い微小線段を検出：
$$\mathbf{B}'(t) = \big( x'(t), \, y'(t) \big)$$
2. **エッジ検出（Edge Detection）**：同方向の微小線段をクラスタリングし、仮想ステムエッジを合成；
3. **ステム結合（Stem Linking）**：対向する平行エッジを探索して主幹（ステム）を同定し、メモリ上で等価的な標準ステム幅（CVT）を動的に統計算出；
4. **グリッドスナップ（Grid Snapping）**：ベースライン、x-ハイト、キャップハイトのアライメント領域に吸着させ、内部空間のプロポーションを均等に保ちます。

### 3. サブピクセル描画（Subpixel Rendering / ClearType）の物理革命

カラー液晶ディスプレイ（LCD）の各ピクセルは、赤（R）・緑（G）・青（B）の3つの微細な物理サブピクセルで構成されています。
マイクロソフトの **ClearType** や FreeType の LCD フィルタリング技術は、RGB を一体として扱う従来の制限を破り、各サブピクセルを独立に輝度制御することで、**水平方向の実効解像度を3倍に向上（$3\times$ Horizontal Resolution）**させました。

色にじみ（カラーフリンジ）を防止するため、5タップ FIR ローパスフィルタ核が適用されます：

$$W = \left[ \frac{1}{16}, \, \frac{4}{16}, \, \frac{6}{16}, \, \frac{4}{16}, \, \frac{1}{16} \right]$$

これにより、96 DPI の通常液晶ディスプレイにおいても、印刷物のような滑らかで読みやすい文字描画が実現されました。

---

## 結び：離散グリクセルから高精細 Retina 時代へ

PostScript の宣言型ヒント、TrueType のチューリング完全な仮想マシン、VTT Talk 高級言語、そして FreeType の自動ヒンティングとサブピクセル描画技術は、粗い離散格子の上で文字の美と可読性を守るために築き上げられた工学的金字塔です。

次章**第14章：高度な組版機能 (OpenType/AAT)**では、文字の形態を超え、多言語テキストストリームにおける文脈依存置換、合字、ダイアクリティカルマークの動的配置といった現代組版の最高峰技術を解剖します。
'''

target_to_replace = r'''# 結語

Hinting は妥協の芸術である。それは数学の連続性とピクセルの厳密な離散性の間に橋を架ける。高解像度（Retina）ディスプレイの普及によりその直接的な重要性は薄れつつあるが、中小画面や特殊環境において、それは文字の尊厳と可読性を守る最後の砦であり続けている。'''

if target_to_replace in ja_text:
    new_ja = ja_text.replace(target_to_replace, ja_expansion)
else:
    new_ja = ja_text + "\n\n" + ja_expansion

with open('docs/ja/fonts-encodings/chapter-13.md', 'w', encoding='utf-8') as f:
    f.write(new_ja)

print(f"docs/ja/fonts-encodings/chapter-13.md written: {len(new_ja)} characters")
