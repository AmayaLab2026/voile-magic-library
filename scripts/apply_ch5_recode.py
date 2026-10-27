import opencc

s2t = opencc.OpenCC('s2t')

with open('scripts/recode_snippet_zh.md', 'r', encoding='utf-8') as f:
    snippet_zh = f.read()

snippet_hant = s2t.convert(snippet_zh)

snippet_ja = """
---

### 伝説的トランスコーディングツール：François Pinard の `recode` ユーティリティ

Unix フリーソフトウェアの歴史において、数十年におよぶ深い伝統を誇る伝説的文字コード変換ツールが、カナダ・ケベック州の著名なプログラマーであるフランソワ・ピナール（François Pinard）氏によって主導された **`recode`** [293] である。その原型（当時は別名称）は1970年代にまで遡り、現代のバージョンは低層において GNU `libiconv` ランタイムアーキテクチャに立脚している。

#### 1. 簡潔かつ直感的なパイプライン構文

コマンドラインにおけるファイル `foo.txt` の変換構文は極めて直感的である：`recode` の膨大なサポートリストから変換元エンコーディング $A$ と変換先エンコーディング $B$ を指定するだけで、直接その場で上書き変換を実行できる：

```bash
recode A..B foo.txt
```

元ファイルを保持したまま標準出力リダイレクトで別ファイルへ出力することも可能である：

```bash
recode A..B < foo.txt > foo-converted.txt
```

さらに驚くべきことに、`recode` は単一のコマンド実行内で任意の多段変換ホップを連鎖させることができる：

```bash
recode A..B..C..D..E foo.txt
```

#### 2. 「表面」（Surface）シリアライゼーション機構

`recode` の最も画期的な設計理念の一つは、「表面」（Surface）と呼ばれる概念の導入である。これは本質的に Unicode のシリアライゼーション機構（Serialization Mechanisms）に対応するものであり、**文字の抽象的エンコーディングを変更することなく、その物理的格納・伝送表現形式を変換する**。

$S$ を特定の表面機構とするとき、スラッシュ記法を用いて目的エンコーディングの直後に付加できる：

```bash
recode A..B/S foo.txt
```

$A \to B$ のエンコーディング変換を行うと同時に、特定のシリアライズ表現が自動的に適用される。主な表面機構は以下の通りである：
* **`b64`**：標準 Base64 エンコーディング；
* **`d1, d2, d4`**：文字を10進数数値列としてダンプ（それぞれ 1 バイト単位 byte-by-byte、2 バイト単位 wyde-by-wyde、4 バイト単位 tetrabyte-by-tetrabyte）；
* **`h1, x2, x4`**（および8進数 `o1`）：16進数または8進数形式でのバイトシーケンス出力；
* **`QP`**：電子メール等で広く用いられる Quoted-Printable 印刷可能文字エンコーディング；
* **`CR` および `CR-LF`**：改行コードの正規化変換（Unix の LF をクラシック Mac の CR、あるいは Windows/DOS の CR-LF へ相互変換）。

#### 3. 包括的な Unicode および ISO 10646 形式のサポート

現代の Unicode 体系への変換に向けて、`recode` はきめ細やかなエイリアス体系を提供している：
* **`u7`**：UTF-7（純粋な ASCII 文字列のみで表現され、欧州言語において人間可読性を維持可能）；
* **`u8`**：標準 UTF-8；
* **`u6`**：汎用 UTF-16（ホストマシンのローカル CPU アーキテクチャに応じたエンディアン）；
* **`UTF-16BE` および `UTF-16LE`**：ビッグエンディアンおよびリトルエンディアンの明示的 UTF-16；
* **ISO 10646 規格エイリアス**：
  - `UCS-2-INTERNAL`：ローカルエンディアンの 16 ビット符号化；
  - `UCS-2-SWAPPED`：ローカルと逆順のエンディアンによる 16 ビット符号化；
  - `UCS-2LE`：リトルエンディアン 16 ビット符号化；
  - `UCS-4-INTERNAL`、`UCS-4-SWAPPED`、`UCS-4BE`、`UCS-4LE`：32 ビット完全幅エンコーディングの全エンディアンマトリクス。

変換不能な文字が存在する場合、データ破損防止のためデフォルトでは処理が停止するが、**`-f`（Force）オプション** を指定することで強制的に変換を完遂させることができる（非可逆置換となるため検証が必要）。

#### 4. 277 種類のエンコーディング体系と独自の「疑似エンコーディング」（Pseudo-Encodings）

バージョン 3.6 時点で、`recode` は実に 277 種類のエンコーディングをサポートしている：
* **`us`**：米国ローカライズ ASCII（ISO 646.1991-IRV）；
* **Macintosh 体系**：`MacRoman`、`MacCentralEurope`、`MacJapanese` 等のクラシックリソースフォークエンコーディング群；
* **東アジア言語**：`BIG5`、`CHINESE`（GB 2312）、`EUC-CN`、`Shift_JIS`（`SJIS`）、`EUC-JP`、`ISO-2022-JP`、`JOHAB`、`EUC-KR` 等；
* **ISO 8859 ファミリー**：`l1` 〜 `l9`（Latin-1〜9）、`cyrillic`、`arabic`、`greek`、`hebrew`；
* **Microsoft コードページ**：`CP932`、`CP1252` 等。

さらに圧巻なのは、`recode` が独自に備える**「疑似エンコーディング」（Pseudo-Encodings）**である：
* **`TeX`**：ダイアクリティカルマーク付き文字を正規の $\\mathrm{\\TeX}$ コマンド（`\\'{e}` や `\\`{a}`）へと自動逆変換；
* **`h1, ..., h4`**：各 HTML バージョンに応じた文字実体参照（`&eacute;` 等）への置換；
* **`flat`**：全アクセント記号を剥ぎ取り、ベースとなるプレーンラテン文字へと平坦化；
* **`dump-with-names`**：文書内の全文字を走査し、その公式 Unicode 標準名称（例：`0x0041 LATIN CAPITAL LETTER A`）を一覧出力する、文字属性解析・文字化け究明における最強のデバッグ手段！
"""

# Apply to zh
with open('docs/zh/fonts-encodings/chapter-5.md', 'r', encoding='utf-8') as f:
    zh_content = f.read()

target = '### 现代脚本语言中的转码生态'
zh_new = zh_content.replace(target, snippet_zh + '\n\n' + target)
with open('docs/zh/fonts-encodings/chapter-5.md', 'w', encoding='utf-8') as f:
    f.write(zh_new)
print('Applied to zh/chapter-5.md')

# Apply to zh-hant
with open('docs/zh-hant/fonts-encodings/chapter-5.md', 'r', encoding='utf-8') as f:
    hant_content = f.read()

target_hant = s2t.convert(target)
hant_new = hant_content.replace(target_hant, snippet_hant + '\n\n' + target_hant)
with open('docs/zh-hant/fonts-encodings/chapter-5.md', 'w', encoding='utf-8') as f:
    f.write(hant_new)
print('Applied to zh-hant/chapter-5.md')

# Apply to ja
with open('docs/ja/fonts-encodings/chapter-5.md', 'r', encoding='utf-8') as f:
    ja_content = f.read()

target_ja = '### 現代のスクリプト言語における文字コード生態系'
ja_new = ja_content.replace(target_ja, snippet_ja + '\n\n' + target_ja)
with open('docs/ja/fonts-encodings/chapter-5.md', 'w', encoding='utf-8') as f:
    f.write(ja_new)
print('Applied cleanly to ja/chapter-5.md')
