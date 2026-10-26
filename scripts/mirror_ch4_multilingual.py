import opencc, os, re

with open('docs/zh/fonts-encodings/chapter-4.md', 'r', encoding='utf-8') as f:
    zh_text = f.read()

# 1. Generate zh-hant via opencc
converter = opencc.OpenCC('s2t')

blocks = []
def repl_block(m):
    idx = len(blocks)
    blocks.append(m.group(0))
    return f"___CODE_BLOCK_{idx}___"

protected = re.sub(r'(```[\s\S]*?```|\$\$[\s\S]*?\$\$|`[^`\n]+`)', repl_block, zh_text)
hant_protected = converter.convert(protected)

for idx, b in enumerate(blocks):
    hant_protected = hant_protected.replace(f"___CODE_BLOCK_{idx}___", b)

hant_protected = hant_protected.replace('*译者：', '*譯者：')

with open('docs/zh-hant/fonts-encodings/chapter-4.md', 'w', encoding='utf-8') as f:
    f.write(hant_protected)
print(f"Wrote docs/zh-hant/fonts-encodings/chapter-4.md ({len(hant_protected)} chars)")

# 2. Build Japanese version for Chapter 4
ja_text = r"""---
title: 第四章：正規化、双方向テキストと東アジア文字体系
description: Unicode 文字規範分解と合成（NFC/NFD/NFKC/NFKD）、双方向組版アルゴリズム（UAX #9）、CJK統合漢字（Unihan）、文字記述言語（CDL）、ハングル（Hangul）数学的構成モデルの全貌
---

# 第 4 章：正規化、双方向テキストと東アジア文字体系

*翻訳者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

本章では、Unicode 規格における極めて専門的でありながら、近代デジタル組版および自然言語処理において決定的な意義を持つ 3 つの中核的領域を詳細に検討します：
1. **文字の分解と正規化（Decompositions and Normalizations）**：メモリ上の複数通りの文字列表現における等価性の判定と標準化された格納形式の確立；
2. **双方向組版アルゴリズム（The Bidirectional Algorithm、Unicode 附属書 UAX #9）**：右から左へ書く文字（アラビア文字、ヘブライ文字）と左から右へ書く文字（ラテン、ギリシャ、キリル文字）が混在するテキストストリームにおける視覚的リバースと折り返しの数学的制御；
3. **東アジア文字体系（East Asian Scripts）**：漢字文化圏における中国起源の表意文字（CJK統合漢字）、字形記述言語（CDL）、および完全な数学的対称性を誇る韓国ハングル（Hangul）音節構造モデルの解明。

---

## 1. 文字の分解と正規化（Decompositions and Normalizations）

Unicode において、人間の目に同一に見える文字が、コンピュータの内部表現として複数の異なるコードポイント列でエンコード可能であるケースは珍しくありません。例えばサーカムフレックス付きの小文字 `â` は、単一の合成済み文字（Precomposed Character）`U+00E2`（LATIN SMALL LETTER A WITH CIRCUMFLEX）としても、基底文字 `a`（`U+0061`）に結合サーカムフレックス（Combining Circumflex Accent）`U+0302` を後置した 2 文字のシーケンスとしても表現できます。

この多義性を厳密に標準化しなければ、文書検索、データベース照合、文字列ハッシュ比較において致命的な不整合が生じます。

### 1.1 結合文字と結合クラス（Combining Characters & Combining Classes）

Unicode 標準には数百の結合文字（結合ダイアクリティカルマーク）が収録されており、幾何学的な吸着位置に基づき **53 種類の結合クラス（Combining Classes, cc）** に分類されています：

| 結合クラス (cc) | 幾何学的配置の説明 | 代表的な結合文字 | 組版上の吸着挙動 |
| :---: | :--- | :--- | :--- |
| **0** | 間隔基底文字（Spacing / Base Glyphs） | 通常の英数字 `a`, `B`, `1` | 独立した送り幅を持ち、後続結合符の幾何的アンカーとなる |
| **1** | 重ね合わせ符号（Overlay） | 斜線重ね合わせ符 `U+0338` (̸) | 基底文字の中央を斜断する |
| **7** | ヌクタ符（Nukta） | インド系文字の核音変音点 | 子音文字の右下に密着 |
| **8** | 仮名濁点・半濁点（Kana Voicing） | 濁点 `U+3099` (゙) | 仮名の右肩に配置 |
| **9** | 純粋子音抑制符（Virama） | サンスクリット等の無母音化符 `U+094D` | 後続子音との結合合字形成を促す |
| **202** | 下部直接付着（Attached Below） | セディラ（Cedilla `U+0327`）、オゴネック（`U+0328`） | 基底文字のストローク底部に直接結合 |
| **214** | 上部直接付着（Attached Above） | フラットなアクセントバー等 | 基底文字のストローク天面に直接結合 |
| **216** | 右上付着（Attached Above Right） | ベトナム語のホーン（Horn `U+031B` ơ, ư） | 母音文字の右肩に付着 |
| **220** | 下部配置・非接触（Below） | 下点（Dot Below `U+0323`）、下部キャロン（`U+032C`） | 光学的余白を空けて基底文字の下方に浮遊配置 |
| **230** | 上部配置・非接触（Above） | アキュート（`U+0301`）、グレイヴ（`U+0300`）、サーカムフレックス（`U+0302`） | 基底文字の真上に浮遊配置 |

ここには 2 つの重要な公理があります：
1. **直交クラスの独立性**：異なる結合クラス（例：下部 `cc=220` と上部 `cc=230`）は空間的に干渉しないため、入力順序に関わらず同一の合成結果をレンダリングします。
2. **同種クラスの順序依存性**：同一結合クラスの結合符同士は、基底文字からの幾何的積層順（Stacking Order）を表すため、順序の入れ替えは意味の変更をもたらします。

### 1.2 正準順序付けアルゴリズム（Canonical Ordering Algorithm）

直交結合符の入力順序による不整合を解消するため、Unicode は**正準順序付けアルゴリズム（Canonical Ordering Algorithm）** を規定しています：
1. 文字列を走査し、各文字の `cc` 値を特定する。
2. 非ゼロの `cc` を持つ連続した結合文字シーケンスを抽出する。
3. `cc` 値をキーとして**安定ソート（Stable Sort）** を実行する。`cc` 値が同一の文字間では元の相対順序を保ち、異なる場合は `cc` の小さい順に並べ替える。

### 1.3 正準等価と互換等価（Canonical vs Compatibility Equivalence）

- **正準等価（Canonical Equivalence）**：純粋テキストの意味および組版表示において完全同一の等価関係。
  $$\text{U+00E2} \equiv \text{U+0061} + \text{U+0302}$$
- **互換等価（Compatibility Equivalence）**：基本的なセマンティクスは同一だが、書式（上付き、下付き、丸囲み、フォント変種、組版メトリクス）が異なる等価関係。
  - 上付き数字：$\text{U+00B2} \ ({}^2) \approx \text{U+0032} \ (2)$
  - 合字：$\text{U+FB01} \ (\text{fi}) \approx \text{U+0066} + \text{U+0069}$
  - 単位記号：$\text{U+33A1} \ (\text{km}^3) \approx \text{U+006B} + \text{U+006D} + \text{U+0033}$

### 1.4 4つの標準正規化形式（NFC, NFD, NFKC, NFKD）

1. **NFD（Canonical Decomposition）**：正準分解。すべての結合文字を分解し、正準順序でソートする。
2. **NFC（Canonical Decomposition followed by Canonical Composition）**：正準分解後に可能な限り正準合成を行う。**W3C が Web テキスト伝送に推奨する業界標準形式**。
3. **NFKD（Compatibility Decomposition）**：互換分解。互換文字も基本文字へ完全展開する。検索エンジンのインデックス作成に多用される。
4. **NFKC（Compatibility Decomposition followed by Canonical Composition）**：互換分解後に最大正準合成を行う。

---

## 2. Unicode 双方向組版アルゴリズム（UAX #9）

アラビア文字やヘブライ文字などの右横書き（RTL）と、ラテン文字や漢字などの左横書き（LTR）が同一行内で混在するテキストを**双方向テキスト（Bidirectional Text, Bidi）**と呼びます。

### 2.1 19 種類の双方向文字型

UAX #9 は各コードポイントに以下の `Bidi_Class` 属性を割り当てています：
- **強方向型（Strong）**：`L`（左横書き）、`R`（ヘブライ等の右横書き）、`AL`（アラビア系右横書き）
- **弱方向型（Weak）**：`EN`（欧文数字）、`ES`（欧文符号 `+`, `-`）、`ET`（通貨記号 `$`, `%`）、`AN`（アラビア数字）、`CS`（共通数値区切り点 `,`, `.`）、`NSM`（非間隔記号）、`BN`（境界中立符）
- **中立型（Neutral）**：`B`（段落区切り）、`S`（セグメント区切り）、`WS`（空白文字）、`ON`（その他の記号）
- **明示的制御符**：`LRE`, `RLE`, `LRO`, `RLO`, `PDF`

### 2.2 UAX #9 の 6 つの主要ステップ

1. **段落分割と基本レベル判定（P1 - P3）**：段落内の最初の強方向文字を検出し、段落全体の基本レベル（LTR なら偶数 0、RTL なら奇数 1）を決定する。
2. **明示的制御符の展開（X1 - X10）**：最大深度 125 の方向スタックを管理し、`RLE`/`LRE`/`PDF` による入れ子レベルを計算する。
3. **弱方向型の解決（W1 - W7）**：数値や記号の文脈依存ルールを適用し、弱文字を強文字型へ変換する。
4. **中立型と括弧ペアの解決（N1 - N2）**：対になる括弧（`(` と `)`）の内容方向を判定し、中立空白を前後の強方向へ同化させる。
5. **暗黙レベルの確定（I1 - I2）**：各文字の最終的な整数埋め込みレベル（Level）を確定する。
6. **視覚的並べ替えと文字鏡像化（L1 - L4）**：最高レベルから最低奇数レベルへ向かって連続文字列を再帰的に反転し、RTL 領域内の括弧記号等を `BidiMirroring.txt` に従って鏡像グリフへ置換する。

---

## 3. 東アジア文字体系（East Asian Scripts）

### 3.1 CJK統合漢字（CJK Unified Ideographs）

東アジア諸国における漢字コードの乱立を克服するため、中日韓の専門家と Unicode コンソーシアムは以下の統合法則を確立しました：
1. **原典分離規則（Source Separation Rule）**：GB 2312 や JIS X 0208 などの原典規格で区別されていた文字は、往復変換可能性（Round-trip）を保証するため Unicode でも必ず別コードを維持する。
2. **同源認知分析（Cognate Analysis）**：歴史的造字源流が同一であり、抽象的な骨格構造（部首・筆画配置）が一致する字形は同一コードに統合する。
3. **デザイン差の分離（Design Variation）**：地域的な筆法の差異（日本の明朝体と中国の宋体におけるハネ・トメの違いなど）はフォント側の異体字（OpenType `locl` 機能等）に委ねる。

### 3.2 漢字構成記述文字（IDC）

未収録の古漢字や人名外字を表現するため、Unicode は `U+2FF0` から `U+2FFB` の 12 個の**漢字構成記述文字（Ideographic Description Characters, IDC）**を導入しました：
- `⿰`（左右並列）、`⿱`（上下積層）、`⿲`（左中右三分）、`⿳`（上中下三分）、`⿴`（全包囲）、`⿵`（上部三包囲）、`⿶`（下部三包囲）、`⿷`（左部三包囲）、`⿸`（左上二包囲）、`⿹`（右上二包囲）、`⿺`（左下二包囲）、`⿻`（重ね合わせ交叉）。
前置ポーランド記法（Prefix Polish Notation）により、未登録の文字構造（例：`⿰氵⿱艹⿵门日`）をテキストとして正確に記述可能です。

### 3.3 文字記述言語（Character Description Language, CDL）

Tom Bishop 氏らによって開発された XML ベースの漢字記述仕様。$128 \times 128$ のグリッド座標系上で 30 種類の基本構成筆画（横 `h`、縦 `s`、左払い `p`、右払い `n`、折れ `z` 等）をパラメータ化し、正確な筆順アニメーションや動的字形補正を実現します。

---

## 4. 韓国ハングル（Hangul）の数学的構造モデル

1446 年、世宗大王によって公布された『訓民正音』（*Hunminjeongeum*）に基づく**ハングル（Hangul）**は、世界で最も数学的かつ音素論的に洗練された文字体系です。

### 4.1 子音・母音（Jamo）の分類

- **初声（Choseong / L）**：19 種類（`ᄀ`, `ᄁ`, `ᄂ`, ..., `ㅎ`）
- **中声（Jungseong / V）**：21 種類（`ㅏ`, `ㅐ`, ..., `ㅣ`）
- **終声（Jongseong / T）**：28 状態（終声なしを含む）

現代標準ハングルの全音節数は正確に以下の通りです：
$$N = 19 \times 21 \times 28 = 11,172 \ \text{音節}$$

### 4.2 符号化と数学的写像方程式

Unicode は `U+AC00` から `U+D7A3` にかけて、これら 11,172 個の合成済み音節ブロックを厳密な代数順序で配列しています：

$$\text{SBase} = \text{0xAC00}, \quad L_{\text{count}} = 19, \quad V_{\text{count}} = 21, \quad T_{\text{count}} = 28, \quad N_{\text{count}} = 588$$

#### 1. 正方向合成式（Composition）
$$S = \text{SBase} + (L_{\text{index}} \times 588) + (V_{\text{index}} \times 28) + T_{\text{index}}$$

#### 2. 逆方向算術分解式（Decomposition）
$$S_{\text{index}} = S - \text{SBase}$$
$$L_{\text{index}} = \lfloor S_{\text{index}} / 588 \rfloor$$
$$V_{\text{index}} = \lfloor (S_{\text{index}} \bmod 588) / 28 \rfloor$$
$$T_{\text{index}} = S_{\text{index}} \bmod 28$$

```python
def decompose_hangul(codepoint: int):
    SBase = 0xAC00
    LBase = 0x1100
    VBase = 0x1161
    TBase = 0x11A7
    
    if not (0xAC00 <= codepoint <= 0xD7A3):
        return None
        
    s_index = codepoint - SBase
    l_index = s_index // 588
    v_index = (s_index % 588) // 28
    t_index = s_index % 28
    
    l_char = chr(LBase + l_index)
    v_char = chr(VBase + v_index)
    t_char = chr(TBase + t_index) if t_index > 0 else ""
    
    return l_char, v_char, t_char

# "한" (U+D55C) の分解テスト
print(decompose_hangul(0xD55C))
```

この驚異的な数学的整合性により、コンピュータは巨大な辞書引きを行うことなく、最小限の CPU 算術演算のみでハングルの相互変換やスペルチェックを瞬時に実行できます。
"""

with open('docs/ja/fonts-encodings/chapter-4.md', 'w', encoding='utf-8') as f:
    f.write(ja_text)
print(f"Wrote docs/ja/fonts-encodings/chapter-4.md ({len(ja_text)} chars)")
