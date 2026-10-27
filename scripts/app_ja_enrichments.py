import os
import re

c1_c2_ja = r"""## C.1 PostScript ページ記述言語技術概論（Introduction to the PostScript Language）

1985 年、最初のレーザープリンター（Apple LaserWriter）の市場投入以来、PostScript 言語は印刷工業からオフィス文書管理、個人の高品質プリントに至るまで、コンピュータの世界を席巻した。本付録では、PostScript 体系の各種フォント形式（Type 1、Type 3、Type 42、Type 0、CID アーキテクチャ、マルチプルマスター、CFF/Type 2）を詳細に解読する。

個々のフォント形式を分析する前に、フォント内部で用いられる構文構造とオブジェクト操作の本質を把握するため、PostScript 言語の基礎を精緻に導入する。

### C.1.1 構文モデルと逆ポーランド記法スタックマシン（Syntax）

PostScript は純粋な**解釈型・スタック指向・後置記法（Postfix / Reverse Polish Notation, RPN）**プログラミング言語である。構文は空白で区切られた**トークン（Tokens）**から構成され、`%` 以降はコメントとして扱われる。

解釈系がトークンを走査する際：
- リテラル定数（数値、文字列等）は**オペランドスタック（Operand Stack）**へ直ちにプッシュされる；
- 実行可能な演算子（Operator）やプロシージャ名に遭遇すると直ちに実行され、スタックトップから必要な引数をポップして計算結果をスタックへ再プッシュする。

```postscript
3 4 add
```

計算完了後、スタックトップには整数の結果 `7` のみが残る。

主なデータ型：
1. **数値型（Numbers）**：整数（`123`）、8進数（`8#177`）、16進数（`16#FF`）、実数（`3.14159`）；
2. **真偽値型（Booleans）**：`true` および `false`；
3. **文字列型（Strings）**：丸括弧定界の標準文字列（`(Hello)`）または山括弧の16進数（`<48656C6C6F>`）；
4. **名前型（Names）**：
   - **リテラル名（Literal Name）**：スラッシュ前置記号（`/Helvetica`、`/width`）。即時評価されずスタックへ格納；
   - **実行可能名（Executable Name）**：スラッシュなし識別子（`add`、`moveto`）。辞書スタックから検索され即時実行；
5. **配列（Arrays）**：角括弧定界のオブジェクト列（`[ 1 2 (three) /four ]`）；
6. **手続き（Procedures）**：波括弧定界の実行可能コードブロック（`{ add 2 div }`）；
7. **辞書（Dictionaries）**：キー・バリューのハッシュテーブル。

### C.1.2 物理座標系とユーザー空間（The System of Coordinates）

PostScript の幾何描画は抽象的な**ユーザー空間（User Space）**で行われ、ラスタライズ時に**デバイス空間（Device Space）**へと自動投影される。

- **標準測定単位**：伝統的な**ビッグポイント（PostScript Point）**：
  $$1 \text{ pt} = \frac{1}{72} \text{ inch} = \frac{25.4}{72} \text{ mm} \approx 0.352778 \text{ mm}$$
- **原点と座標軸**：デフォルトの原点 $(0, 0)$ は用紙の**左下隅**に位置し、$x$ 軸は右方向、$y$ 軸は上方向へ延伸する。

### C.1.3 カレント変換マトリクス（Current Transformation Matrix, CTM）

ユーザー座標 $(x, y)$ をデバイス座標 $(x', y')$ へ写像するアフィン変換行列は以下のように表現される：

$$\begin{bmatrix} x' & y' & 1 \end{bmatrix} = \begin{bmatrix} x & y & 1 \end{bmatrix} \begin{bmatrix} a & b & 0 \\ c & d & 0 \\ t_x & t_y & 1 \end{bmatrix} = \begin{bmatrix} a x + c y + t_x & b x + d y + t_y & 1 \end{bmatrix}$$

内部では配列 `[a b c d tx ty]` として保持され、`translate`、`scale`、`rotate`、`concat`、`matrix`、`currentmatrix`、`setmatrix` 等の演算子によって動的に操作される。

### C.1.4 ベクターパスシステム（Paths）

輪郭描画の中核は**パス（Path）**である：
- `newpath`：パスバッファの初期化；
- `moveto` / `rmoveto`：カレントポイントを $(x, y)$ へ移動；
- `lineto` / `rlineto`：カレントポイントから直線セグメントを生成；
- `curveto` / `rcurveto`：3次ベジェ曲線セグメントを生成：
  $$B(t) = (1-t)^3 P_0 + 3(1-t)^2 t P_1 + 3(1-t) t^2 P_2 + t^3 P_3, \quad t \in [0, 1]$$
- `closepath`：カレントサブパスの始点へ直線を結び閉合；
- `pathbbox`：パスのバウンディングボックス `llx lly urx ury` を算出；
- `clip`：閉じたパスをクリッピング領域として設定。

### C.1.5 輪郭着色と2大塗りつぶしトポロジー則（Shapes & Filling Rules）

- `stroke`：線幅と線端形状を用いてパスを線描；
- `fill`：**ノンゼロ・ワインディング・ルール（Non-zero Winding Number Rule）**による塗りつぶし；
- `eofill`：**偶奇ルール（Even-Odd Rule）**による塗りつぶし。

### C.1.6 ビットマップ画像の描画（Bitmap Images）

- `imagemask`：1ビットの白黒マスク描画（ビットマップフォントの高速印字に使用）；
- `image`：多値グレースケールおよびフルカラー連続階調画像のサンプリング描画。

### C.1.7 仮想マシンスタック・配列・辞書管理（Stack & Dictionaries）

- **オペランドスタック操作**：`dup`、`pop`、`exch`、`copy`、`index`、`roll`、`clear`；
- **辞書管理**：`dict`、`begin`、`end`、`def`、`load`。

### C.1.8 フォント制御と組版演算子（Font Management & Typesetting）

- `findfont`：フォント辞書の取得；
- `scalefont`：指定ポイントへのスケーリング；
- `setfont`：グラフィックス状態へのフォントの登録；
- `show`：文字列の連続印字とカレントポイントの前進；
- `stringwidth`：指定フォントにおける文字列の送り幅算出；
- `charpath`：文字の幾何輪郭をカレントパスとして抽出。

### C.1.9 グラフィックス状態スタック（Graphics State）

- `gsave` / `grestore`：グラフィックスコンテキスト（CTM、線幅、色等）の退避と復元；
- 線属性：`setlinewidth`、`setlinecap`、`setlinejoin`、`setmiterlimit`、`setdash`；
- 色空間：`setgray`、`setrgbcolor`、`setcmykcolor`。

### C.1.10 構造化コメント規約（DSC: Document Structuring Conventions）

`%!PS-Adobe-3.0`、`%%BoundingBox`、`%%Pages`、`%%Page`、`%%Trailer`、`%%EOF` 等の標準メタデータ規約。

---

## C.2 自由プログラマブル文字形式：Type 3 フォント構造（Type 3 Fonts）

Type 3 フォントは、CharStrings による低レベルバイトコードではなく、**正則な PostScript 高水準プロシージャをそのまま用いてグリフを描画する**極めて柔軟な形式である。

### C.2.1 技術的特長と制約
- **メリット**：PostScript の全グラフィックス演算子（フルカラーグラデーション、画像の埋め込み、動的テクスチャ等）を制約なく利用可能；
- **デメリット**：ヒンティング（Hinting）機構を持たないため、低解像度での小サイズ表示においてジャギーや線の潰れが生じる。

### C.2.2 Type 3 辞書の必須キー
`FontType`（固定値 3）、`FontMatrix`、`FontBBox`、`Encoding`、`BuildGlyph`（または `BuildChar`）。

### C.2.3 `setcachedevice` と `setcharwidth`
- **`setcachedevice`**（`wx wy llx lly urx ury setcachedevice`）：グリフをビットマップキャッシュに登録（内部でのカラー指定は禁止）；
- **`setcharwidth`**（`wx wy setcharwidth`）：キャッシュを行わず毎回動的に描画（カラーグリフや特殊効果フォント向け）。
"""

c6_ja = """---

## C.6 PostScript 外部メトリクス仕様：AFM、AMFM、および Windows PFM（Font Metrics Files）

DTP ソフトウェア（InDesign、QuarkXPress）や $\\mathrm{\\TeX}$ 処理系において、組版エンジンが行長計算やカーニングを処理する際、重厚かつ暗号化されたベクター輪郭を読む必要はなく、純粋な幾何メトリクスデータのみを要求する。その標準形式が **AFM（Adobe Font Metrics）** [22] および Windows 用バイナリ形式 **PFM（Printer Font Metrics）** である。

### C.6.1 AFM ファイルの構造と構文
- **全体情報（Global Information）**：`FontName`、`FullName`、`Weight`、`ItalicAngle`、`IsFixedPitch`、`FontBBox`、`Ascender`、`Descender`、`CapHeight`、`XHeight`；
- **個別文字メトリクス（CharMetrics）**：`C`（文字コード）、`WX`（水平送り幅）、`N`（PostScript グリフ名）、`B`（バウンディングボックス）、`L`（リガチャ規則）；
- **カーニング対データ（KernData）**：`StartKernPairs`、`KPX leftGlyph rightGlyph amount`、`EndKernPairs`；
- **トラックカーニング（TrackKern）**：文字サイズに応じた動的文字間隔調整値。

### C.6.2 マルチプルマスターメトリクス：AMFM
デザイン軸（Weight, Width, Optical Size）とブレンド行列を定義する `.amfm` ファイル。

### C.6.3 Windows 用バイナリメトリクス：PFM
Windows GDI 高速化のため AFM をバイナリ構造体へ変換した形式（`dfType`、`dfAscent`、`dfWeight`、`dfWidthTable`、`dfPairKernTable` 等）。
"""

d7_d8_ja = """## D.7 組み込みビットマップ表群：EBLC、EBDT、EBSC、および bhed（Bitmap Management）

極小サイズ表示において、微小グリッドへのヒンティング解算を代替し、完璧な可読性を保証するために用意されたビットマップ格納テーブル群：
- **`EBLC`（または `bloc`）**：ビットマップの解像度（Strike）、サイズ（ppem）、各グリフのデータオフセットインデックス（Format 1〜5）；
- **`EBDT`（または `bdat`）**：実ビットマップデータ本体（Format 1〜9：バイトアライン、ビットアライン、複合ビットマップ等）；
- **`EBSC`**：手作業ビットマップが存在しない中間サイズ向けの倍率スケーリング定義テーブル；
- **`bhed`**：アウトラインを持たない純粋なビットマップ TrueType 用の代替ヘッダーテーブル。

---

## D.8 核心的オプション補助テーブル群：DSIG、gasp、hdmx、LTSH、kern、VDMX（Optional Tables）

- **`DSIG`（デジタル署名）**：PKCS#7 準拠の暗号証明書による改ざん検証；
- **`gasp`（グリッドフィッティング規約）**：サイズ（ppem）ごとの `GASP_GRIDFIT`（バイトコード強制実行）および `GASP_DOGRAY`（アンチエイリアス平滑化）の切り替え制御；
- **`hdmx` および `LTSH`**：小サイズにおける整数ピクセル送り幅の事前キャッシュテーブルおよび線形近似閾値テーブル；
- **`kern`**：伝統的な字偶間隔調整テーブル（Format 0：二分探索カーニング対配列）；
- **`VDMX`（垂直デバイスメトリクス）**：非線形ヒンティング時の最大アセンダ・ディセンダ整数ピクセル量子化テーブル；
- **`vhea` / `vmtx`**：東アジア縦組用の垂直ベースラインおよび送り幅テーブル；
- **`PCLT`**：HP LaserJet PCL 5 用属性テーブル。
"""

f1_f4_ja = """## F.1 METAFONT 宣言型プログラミング言語の基本構造（The METAFONT Programming Language）

高徳納（Donald E. Knuth）教授による **METAFONT** は、一次線形方程式制約解算システムに基づく宣言型ベクターフォント記述言語である。

### F.1.1 核心データ型と連立方程式解算（Basic Concepts）
8大データ型（`numeric`、`pair`、`pen`、`path`、`picture`、`transform`、`boolean`、`string`）。
等号 `=` は単なる代入ではなく**数学的恒等式**であり、ガウス消去法によって未知座標が自動連立求解される。

### F.1.2 描画・塗りつぶしとスプライン張力（Drawing & Filling）
`..`（曲率連続スプライン）、`--`（直線）、`---`（直線・曲線接線連続）、`{dir theta}`（方向指定）、`tension`（ベジェ曲線の張力調整）。
演算子：`pickup`、`draw`、`fill`、`unfill`、`cull`。

### F.1.3 パラメータ化とマクロ幾何設計（Advanced Concepts）
- **設計寸法**：`u# = 1pt#`、`em# = 10pt#`（解像度非依存）；
- **ピクセル変換**：`define_pixels(u, em)`；
- **文字定義マクロ**：`beginchar` および `endchar`（GF/PK ビットマップおよび TFM メトリクスを同時生成）。

### F.1.4 ラスタライズ最適化（Optimizing the Rasterization）
`good.x`、`good.y` によるピクセルグリッド吸着と `autorounding` による極値点の自動丸め。

---

## F.4 ポーランド METATYPE1 体系と Antykwa Półtawskiego の復興

**Bogusław Jackowski** 氏、**Janusz M. Nowacki** 氏、**Piotr Strzelczyk** 氏が開発した **METATYPE1** アーキテクチャは、METAFONT の宣言型幾何方程式から PostScript Type 1 / OpenType への直接コンパイルを実現した。

ポーランドのグラフィック巨匠**アダム・プウタフスキ（Adam Półtawski）**が 1928 年に設計した銘作活字 **Antykwa Półtawskiego** を、METATYPE1 の純数学パラメータ方程式によって完全デジタル復刻し、現代のオープンソース活字史における金字塔となった。
"""

with open('docs/ja/fonts-encodings/appendices.md', 'r', encoding='utf-8') as f:
    ja_text = f.read()

# 1. Insert C.1 and C.2
target_c_ja = '## C.1 PostScript Type 1 フォントのメモリ構造と復号エンジン'
if target_c_ja in ja_text:
    ja_text = ja_text.replace(target_c_ja, c1_c2_ja.strip() + '\n\n---\n\n## C.3 PostScript Type 1 フォントのメモリ構造と復号エンジン')
    print('Inserted C.1/C.2 into JA')
else:
    print('Target C not found in JA!')

# 2. Insert C.6 (AFM/PFM)
target_c6_ja = '## C.7 CFF 辞書キーとバイナリオペレータ完全辞書'
if target_c6_ja in ja_text:
    ja_text = ja_text.replace(target_c6_ja, c6_ja.strip() + '\n\n---\n\n' + target_c6_ja)
    print('Inserted C.6 into JA')
else:
    print('Target C.6 not found in JA!')

# 3. Insert D.7 and D.8
target_d_ja = '## D.11 OpenType 1.8 ベクターバリアブルフォント（Variable Fonts）体系の進化'
if target_d_ja in ja_text:
    # already inserted earlier or re-check
    pass

# 4. Insert F.1 and F.4
target_f_ja = '## F.1 METAFONT プログラミング言語と宣言的幾何方程式式ソルバー'
if target_f_ja in ja_text:
    ja_text = ja_text.replace(target_f_ja, f1_f4_ja.strip() + '\n\n---\n\n## F.2 METAFONT プログラミング言語と宣言的幾何方程式式ソルバー')
    print('Inserted F.1/F.4 into JA')
else:
    print('Target F not found in JA!')

with open('docs/ja/fonts-encodings/appendices.md', 'w', encoding='utf-8') as f:
    f.write(ja_text)
print('Updated ja/appendices.md successfully. Total chars:', len(ja_text))
