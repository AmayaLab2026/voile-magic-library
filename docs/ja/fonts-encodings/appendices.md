---
title: 付録 A–G · デジタルフォント内部構造、仮想マシンと数学的基礎の完全技術リファレンスマニュアル
description: ヤニス・ハラランブス『Fonts & Encodings』付録 A–G 全文の学術和訳：デジタルフォント低水準形式、仮想マシンと数学的基礎の完全技術リファレンスマニュアル。ビットマップフォント形式（Macintosh FONT/NFNT、Windows FNT/FON、Unix BDF/PCF、TeX PK/GF）、TeX と Omega のメトリクス体系（TFM/OFM/VF/OVF）、PostScript Type 1 バイナリアーキテクチャと eexec 暗号、Multiple Master、CIDFont 構造、TrueType/OpenType/AAT テーブル構造辞典、TrueType 仮想マシン命令セット、METAFONT 言語と 3 次ベジェ曲線のド・カステリョ細分アルゴリズム。
---

# 付録 A–G · デジタルフォント内部構造、仮想マシンと数学的基礎の完全技術リファレンスマニュアル
### Appendices A–G: Technical Reference Manual
**著者：ヤニス・ハラランブス 博士（Yannis Haralambous, Ph.D.）**  
**英訳・増補：P. スコット・ホーン 博士（P. Scott Horne, Ph.D.）**  
*『フォントとエンコーディング』（Fonts & Encodings）原著第 599–990 頁より*  
*訳者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

# 付録 A：ビットマップフォント形式（Bitmap Font Formats）

輪郭ベクトルフォント（Outline Vector Fonts）がデジタルタイポグラフィの世界を席巻する以前、コンピュータディスプレイやドットインパクトプリンタは、文字の表現を離散的なビットマップ（Bitmap）に完全に依存していた。これら往年のバイナリビットマップ形式を理解することは、オペレーティングシステムのフォントサブシステム進化史を紐解くための鍵となる。

## A.1 古典的 Macintosh 体系：FONT および NFNT リソース構造

クラシック Mac OS（System 1 から Mac OS 9 まで）において、ビットマップフォントはリソースフォーク（Resource Fork）内のリソースとして格納され、そのリソースタイプタグは `'FONT'` または `'NFNT'`（New Font）であった。

各文字サイズのビットマップデータは、連続した水平方向の 1 ビットビットマップストライク（Bitmap Strike）としてパックされていた。フォント内のすべてのグリフは同一のストリップ内に横方向に隙間なく連結配置され、各グリフの左右境界はオフセットテーブル（Offset Table）および幅テーブル（Width Table）によって定義された。

::: tip 図版 A-1：クラシック Macintosh システムフォント Chicago の連続ビットマップストリップ (Figure A-1)
![Figure A-1: The global image of the font Chicago](/images/fonts-encodings/fig-app-a1.png)
*図版 A-1：二十年以上にわたり親しまれた Macintosh システムフォント Chicago の全体ビットマップストリップ（原著第 621 頁より）。すべてのグリフが水平方向に隙間なく並び、文字間隔は下位のメトリクステーブルによって切り出される。*
:::

## A.2 DOS、Windows および Unix のビットマップフォント標準

### 1. DOS CPI 形式
MS-DOS 環境下において、ディスプレイおよびプリンタ用のハードウェアビットマップフォントは `.CPI`（Code Page Information）コンテナに格納され、EGA/VGA グラフィックカード向けに特化された $8 \times 8$、$8 \times 14$、$8 \times 16$ ピクセルのビットマップフォントパターンを保持していた。

### 2. Windows FNT および FON 形式
Windows 1.0 から 3.x は、`.FNT`（単一のビットマップグリフリソース）および `.FON`（16 ビット NE アーキテクチャの DLL 内にパッケージ化されたフォントライブラリ）を導入した。内部にはグリフ変位マトリクス、ヘッダメタデータ、文字マッピングテーブルが含まれる。

### 3. Unix および X11 体系：Adobe BDF および PCF 形式
Unix / X Window System において、**BDF（Bitmap Distribution Format）** は ASCII プレーンテキストに基づく可搬性の高いビットマップフォント交換形式であった。

::: tip 図版 A-2：Adobe BDF 形式におけるビットマップグリフのマトリクス構造 (Figure A-2)
![Figure A-2: BDF's vision of the bitmap and vector versions of an ideograph](/images/fonts-encodings/fig-app-a2.png)
*図版 A-2：Adobe BDF 仕様における単一漢字表意文字のビットマップマトリクスとメトリクスフレームワーク（原著第 629 頁より）。バウンディングボックス、変位ベクトル（DWIDTH/SWIDTH）、アスタリスクによるドットパターン、原点とベースライン座標系を示す。*
:::

実際のシステム読み込み時、BDF は通常、メモリマッピング（mmap）による超高速読み込みを実現するため、バイナリ形式の **PCF（Portable Compiled Format）** または **SNF（Server Natural Format）** へとコンパイルされた。

## A.3 TeX 体系のビットマップ出力：GF および PK 形式

ドナルド・クヌースの TeX 組版体系において、METAFONT コンパイラはまず汎用の **GF（Generic Font）** バイナリファイルを出力する。次いで `gftopk` ツールにより、高圧縮されたコンパクトな **PK（Packed Font）** 形式へと変換される。

::: tip 図版 A-3：METAFONT 出力による gftodvi 高解像度字型見本 (Figure A-3)
![Figure A-3: A page from the DVI file produced by gftodvi from Computer Modern Roman 10](/images/fonts-encodings/fig-app-a3.png)
*図版 A-3：`gftodvi` ツールにより Computer Modern Roman 10pt の GF ファイルから生成されたピクセルレベルのマクロ見本（原著第 638 頁より）。ピクセル格子上の骨格、制御点、ピクセル塗りつぶし分布を示す。*
:::

---

# 付録 B：TeX および Omega フォント形式仕様（TFM, OFM, VF）

TeX 組版システムは、「組版処理と描画の完全な分離」という極めて先駆的な工学哲学を備えている。TeX エンジンが段落の改行計算や数式組版を行う際、**グリフの輪郭やビットマップピクセルを読み取る必要は一切ない**。必要とされるのは、個々の文字のマクロな幾何メトリクス（外接枠の寸法、カーニング、合字規則、視覚的サイズ補正）のみである。

## B.1 TFM（TeX フォントメトリクス表）バイナリデータ構造

各 TeX フォントメトリクスファイル（`.tfm`）は 16 ビットのビッグエンディアン符号なし整数で構築され、論理的に以下の 10 個の連続するデータ領域に分割されている。

| 領域インデックス | 名称 | 内容と役割 |
| :--- | :--- | :--- |
| 1 | `header` | チェックサム、デザインサイズ（Design Size）、符号化スキーム文字列 |
| 2 | `char_info` | 文字インデックス表：幅インデックス（`width_index`）、高さ・深さインデックス（`height_depth_index`）、イタリック補正インデックス（`italic_index`）、タグフィールド |
| 3 | `width` | 文字幅配列（固定小数点数 `fix_word` で格納） |
| 4 | `height` | ベースライン上方の文字高さ配列 |
| 5 | `depth` | ベースライン下方の文字深さ配列 |
| 6 | `italic` | イタリック傾斜角および字間余白補正量配列 |
| 7 | `lig_kern` | 合字およびカーニング状態遷移マイクロ命令仮想マシンプログラム（Ligature/Kerning Table） |
| 8 | `kern` | 物理的カーニング値テーブル |
| 9 | `exten` | 大型数学伸長文字の組み立て記述表（括弧や積分記号の部品結合など） |
| 10 | `param` | フォント全体組版パラメータ配列（`fontdimen`）：空白基準幅、伸縮量、x-ハイト、数式軸の高さなど |

### 中核の固定小数点数表現：`fix_word`
TFM ファイル内の幾何寸法はすべて、クヌースが創案した 32 ビットの 2 の補数固定小数点数 `fix_word` で表現される。上位 12 ビットが整数部、下位 20 ビットが小数部を表す。絶対基準単位はフォントのデザインサイズである（$1.0 = 2^{20} = 1,048,576$ 内部単位）。この精緻な設計により、TeX の幾何計算はいかなるハードウェア環境においても完全に同一かつ再現可能な結果を保証する。

## B.2 Omega OFM と仮想フォント（VF）体系

TFM が 256 文字しかサポートできないという制約を打破するため、Omega プロジェクトは **OFM（Omega Font Metrics）** を導入し、文字インデックスを 16 ビットおよび 32 ビットの Unicode 全域へと拡張した。

**VF（Virtual Font、仮想フォント）** は、組版エンジンが異なる物理フォントに属するグリフを組み合わせて単一の論理フォントを合成することを可能にした。VF バイトコードにより、実行時にグリフの拡大縮小、変位、重ね合わせ、回転を動的に実行でき、現代の複合フォントの先駆的プロトタイプとなった。

---

# 付録 C：PostScript Type 1 フォントのバイナリアーキテクチャと eexec 暗号

Adobe の PostScript Type 1 フォントは、現代ベクトルタイポグラフィの礎石である。

## C.1 PostScript パストラッキングと塗りつぶし規則

PostScript インタプリタはベジェ曲線命令によって輪郭を記述し、「ノンゼロ・ワインディング数ルール（Nonzero Winding Number Rule）」を用いて閉領域の内外判定を行う。

::: tip 図版 C-1：PostScript パス構築と形状塗りつぶしのコード例 (Figure C-1)
![Figure C-1: Examples of PostScript code: tracing a path, filling a shape](/images/fonts-encodings/fig-app-c1.png)
*図版 C-1：PostScript ベクトルコード例：パス構築、線画描画、形状塗りつぶし（原著第 662 頁より）。*
:::

::: tip 図版 C-2：ノンゼロ・ワインディング数塗りつぶし規則の幾何判定ロジック (Figure C-2)
![Figure C-2: Examples of filling according to the nonzero winding number rule](/images/fonts-encodings/fig-app-c2.png)
*図版 C-2：ノンゼロ・ワインディング数規則の幾何判定（原著第 663 頁より）。外部への半直線を引き、輪郭の周回方向の代数和を計算して穴あき複合領域を判定する。*
:::

## C.2 テキスト描画演算子と Scrabble フォント

PostScript は多彩なテキスト出力演算子を提供する。基本的な `show`、文字間隔を一様に拡張する `ashow`、各グリフに個別の変位座標を与える `xyshow` などである。

::: tip 図版 C-3：PostScript show 演算子とその字間拡張バリアント (Figure C-3)
![Figure C-3: The show operator and variants: ashow, xyshow](/images/fonts-encodings/fig-app-c3.png)
*図版 C-3：`show` 演算子とそのバリアント `ashow`（トラッキング調整）および `xyshow`（個別文字幅バランシング）（原著第 667 頁より）。*
:::

::: tip 図版 C-4：ジャック・アンドレ設計による Scrabble 拼字ゲーム Type 3 フォント (Figure C-4)
![Figure C-4: The font Scrabble, by Jacques André](/images/fonts-encodings/fig-app-c4.png)
*図版 C-4：フランスのタイポグラフィの泰斗ジャック・アンドレ（Jacques André）が設計した Scrabble ゲーム用 Type 3 フォント（原著第 675 頁より）。同一文書の連続 4 回の印刷で、木目テクスチャと文字の揺らぎがランダムに変化する。*
:::

## C.3 エンコーディングテーブルとグリフ輪郭メトリクス

::: tip 図版 C-5：Adobe Standard 欧文フォントエンコーディング表 (Figure C-5)
![Figure C-5: The Adobe Standard font encoding, illustrated with Monotype Columbus](/images/fonts-encodings/fig-app-c5.png)
*図版 C-5：Adobe Standard 符号化仕様（Monotype Columbus フォントによる例示、原著第 681 頁より）。*
:::

::: tip 図版 C-6：Adobe Expert 専門家向け拡張エンコーディング表 (Figure C-6)
![Figure C-6: The Adobe Expert font encoding, illustrated with Monotype Columbus Expert](/images/fonts-encodings/fig-app-c6.png)
*図版 C-6：Adobe Expert 拡張符号化仕様。本格的なスモールキャピタル、オールドスタイル数字、合字を完備（原著第 681 頁より）。*
:::

::: tip 図版 C-7：各言語書記体系における関連高さと突出量メトリクス (Figure C-7)
![Figure C-7: The relevant heights, with overshoot, of various script glyphs](/images/fonts-encodings/fig-app-c7.png)
*図版 C-7：ラテン文字、アラビア文字等におけるグリフの視覚的突出量（Overshoot）、ベースライン、キャップハイト、ディセンダーラインのメトリクス（原著第 683 頁より）。*
:::

::: tip 図版 C-8：The Sans Mono Condensed Light における小文字 'e' の輪郭記述 (Figure C-8)
![Figure C-8: Description of the glyph 'e' in The Sans Mono Condensed Light](/images/fonts-encodings/fig-app-c8.png)
*図版 C-8：リュック(アス)・ド・フロート設計の The Sans Mono における文字 ‘e’ の絶対ベクトル輪郭と 3 次スプライン分割（原著第 686 頁より）。*
:::

## C.4 PostScript ヒンティング（Hinting）体系

低解像度機器（72〜150 DPI の画面や初期の 300 DPI レーザープリンタなど）においてステム幅の一貫性を保ち、黒みの潰れを防ぐため、Type 1 仕様は洗練されたヒンティング機構を導入した。

::: tip 図版 C-9：文字 H、O、m における潜在的ヒントゾーン (Figure C-9)
![Figure C-9: Potential hints for the letters 'H', 'O', and 'm'](/images/fonts-encodings/fig-app-c9.png)
*図版 C-9：文字 ‘H’、‘O’、‘m’ のヒント適用区間（原著第 688 頁より）。灰色領域はピクセル格子に整列・固定すべき主ステム幅を表す。*
:::

::: tip 図版 C-10：文字 'B' における 4 つのヒントの動的置換ロジック (Figure C-10)
![Figure C-10: Replacing four hints in the letter 'B'](/images/fonts-encodings/fig-app-c10.png)
*図版 C-10：複雑なグリフ ‘B’ の描画過程におけるヒント置換（Hint Replacement）の実行（原著第 689 頁より）。*
:::

::: tip 図版 C-11：2 つの 3 次ベジェ曲線から構成される Flex 浅曲率制御 (Figure C-11)
![Figure C-11: Flex formed by two cubic Bézier curves](/images/fonts-encodings/fig-app-c11.png)
*図版 C-11：2 本の 3 次ベジェ曲線で構成される Flex 機構（原著第 690 頁より）。緩やかな円弧が低解像度で不自然な直線や階段状ジャギーに退化するのを防ぐ。*
:::

::: tip 図版 C-12：PostScript Type 1 フォントのカウンターコントロール (Figure C-12)
![Figure C-12: Counter controls of PostScript Type 1 fonts](/images/fonts-encodings/fig-app-c12.png)
*図版 C-12：Type 1 フォントの内部空白カウンター制御機構（原著第 692 頁より）。‘m’ などの多幹文字において、小サイズでも均等な内白を保持する。*
:::

::: tip 図版 C-13：Times-Roman の各サイズにおける字間調整曲線 (Figure C-13)
![Figure C-13: Two examples of letterspacing in Times-Roman](/images/fonts-encodings/fig-app-c13.png)
*図版 C-13：Times-Roman における 5pt から 15.5pt までのトラッキングカーニング（TrackKern）対比（原著第 696 頁より）。*
:::

## C.5 Multiple Master フォントと多次元デザイン空間

Adobe の Multiple Master（MM）技術は、フォントデザイナーが連続的な多次元デザイン空間（Design Space）を構築することを可能にした。軸の両極や中間にマスターグリフ（Master Designs）を設定し、ユーザーのパラメータに応じて多次元線形補間を行う。

::: tip 図版 C-14：Adobe Kepler MM フォントにおける文字 'A' の 8 つのマスターデザイン (Figure C-14)
![Figure C-14: Eight master designs of the glyph 'A' in Adobe Kepler MM](/images/fonts-encodings/fig-app-c14.png)
*図版 C-14：Adobe Kepler MM において「ウェイト（Weight）」「幅（Width）」「光学サイズ（Optical Size）」の 3 次元立方体空間に配置された 8 つの極限マスターデザインと中間補間形態（原著第 698 頁より）。*
:::

## C.6 OCF および CIDFont アーキテクチャ

東アジアの日中韓（CJK）の膨大な漢字需要に応えるため、Adobe は OCF（Original Composite Format）および画期的な **CIDFont** アーキテクチャを開発した。CIDFont は文字エンコーディング（CMap）とグリフ輪郭（CIDFont ファイル）を完全に分離し、各グリフは一意の数値インデックス（CID, Character Identifier）でアドレッシングされる。

::: tip 図版 C-15：古典的 OCF 複合フォントの二層参照機構 (Figure C-15)
![Figure C-15: How OCF fonts work](/images/fonts-encodings/fig-app-c15.png)
*図版 C-15：古典的 OCF フォントの入れ子型辞書と 2 バイト参照モデル（原著第 706 頁より）。*
:::

::: tip 図版 C-16：CIDFont ファイル（CID Type 0）の全体構造 (Figure C-16)
![Figure C-16: Overall structure of a CIDFont file (CID type 0)](/images/fonts-encodings/fig-app-c16.png)
*図版 C-16：CIDFont バイナリファイル（Type 0）の全体トポロジー構造とインタプリタの探索パス（原著第 709 頁より）。*
:::

::: tip 図版 C-17：Type 2 Charstrings における高次ヒントマスク管理 (Figure C-17)
![Figure C-17: Hint management in charstrings of Type 2](/images/fonts-encodings/fig-app-c17.png)
*図版 C-17：Type 2 Charstrings における高次ヒントマスク管理（原著第 723 頁より）。複雑な漢字「講」（11 本の水平ステムヒント）におけるヒントマスクの切り替えを示す。*
:::

---

# 付録 D：TrueType、OpenType および AAT バイナリテーブル構造完全辞典

TrueType および OpenType フォントファイルは、低水準においてテーブルディレクトリ（Table Directory）と複数の独立したバイナリテーブル群（Tables）から構成される。

## D.1 ビットマップおよびデバイスメトリクステーブル

::: tip 図版 D-1：EBLC 表におけるビットマップグリフの水平・垂直メトリクスモデル (Figure D-1)
![Figure D-1: Horizontal and vertical metrics of a bitmap glyph in an EBLC table](/images/fonts-encodings/fig-app-d1.png)
*図版 D-1：TrueType EBLC テーブルに内蔵されたビットマップグリフの水平・垂直幾何メトリクスパラメータ（原著第 756 頁より）。*
:::

::: tip 図版 D-2：中国語テキストの 12 ppem と 24 ppem におけるビットマップ描画対比 (Figure D-2)
![Figure D-2: Comparison of Chinese text rendered at 12 and 24 ppem](/images/fonts-encodings/fig-app-d2.png)
*図版 D-2：漢字テキストにおける 12 ppem と 24 ppem のビットマップヒンティング効果の対比（原著第 760 頁より）。*
:::

::: tip 図版 D-3：Verdana フォント文字 'A' の ppem に伴うピクセル幅の階段状分布 (Figure D-3)
![Figure D-3: Distribution of sizes in pixels of the letter 'A' from Verdana](/images/fonts-encodings/fig-app-d3.png)
*図版 D-3：Verdana フォントの文字 ‘A’ が `hdmx` テーブル内で文字サイズに伴って示す離散ピクセル幅の曲線（原著第 764 頁より）。*
:::

## D.2 レイアウト検索と連筆結合

::: tip 図版 D-4：OpenType 連筆結合（Cursive Attachment）ルックアップフラグ (Figure D-4)
![Figure D-4: Two examples of cursive attachment lookup flag](/images/fonts-encodings/fig-app-d4.png)
*図版 D-4：ウルドゥー語ナスタアリーク体において Cursive Attachment フラグを用いたベースライン係留効果（原著第 788 頁より）。*
:::

::: tip 図版 D-5：ハムザ付きアラビア文字 Yeh Barree のグリフ変異と合字の変遷 (Figure D-5)
![Figure D-5: The glorious fate of arabic letter yeh barree with hamza above](/images/fonts-encodings/fig-app-d5.png)
*図版 D-5：コード U+06D3 が GSUB 置換テーブルを経て遂げる変形プロセスの全景（原著第 804 頁より）。*
:::

::: tip 図版 D-6：Ampersands フォントファミリーにおける 202 種類のアンパサンド変体 (Figure D-6)
![Figure D-6: The 202 ampersands of AmpersandsOne and AmpersandsTwo](/images/fonts-encodings/fig-app-d6.png)
*図版 D-6：米国タイポグラフィ協会によって編纂された Ampersands フォント収録の 202 種におよぶ古典・現代の「＆」記号バリアント（原著第 806 頁より）。*
:::

::: tip 図版 D-7：ヘルマン・ツァップ Zapfino による三言語愛の詩篇 (Figure D-7)
![Figure D-7: A trilingual and tri-fontal love poem in Zapfino](/images/fonts-encodings/fig-app-d7.png)
*図版 D-7：巨匠ツァップ設計による Zapfino で組まれた 3 言語 3 書体の名作愛の詩篇（原著第 861 頁より）。極端なスウォッシュと上下行の交差装飾を示す。*
:::

::: tip 図版 D-8：Apple Skia フォントの wght ウェイト軸に沿った連続変形 (Figure D-8)
![Figure D-8: Apple Skia variations along the wght axis](/images/fonts-encodings/fig-app-d8.png)
*図版 D-8：Apple AAT Skia フォントにおける `wght` 軸上の滑らかな無段階モーフィング（原著第 873 頁より）。*
:::

## D.3 AAT 有限状態機械（Finite State Automaton）遷移モデル

::: tip 図版 D-9：AAT 決定性有限オートマトンの二つの典型状態遷移モデル (Figure D-9)
![Figure D-9: Two examples of finite automata](/images/fonts-encodings/fig-app-d9.png)
*図版 D-9：AAT 状態遷移オートマトンモデルの例（原著第 878 頁より）。楕円が状態ノード、有向矢印が入力文字クラスによる状態遷移を表す。*
:::

::: tip 図版 D-10：二重初期状態を持つ拡張型 AAT オートマトンモデル (Figure D-10)
![Figure D-10: Finite automaton with an additional initial state](/images/fonts-encodings/fig-app-d10.png)
*図版 D-10：行頭（Beginning of Line）と行中の文脈識別を分離した拡張型 AAT 有限状態オートマトン（原著第 881 頁より）。*
:::

---

# 付録 E：TrueType 仮想マシン命令セット完全リファレンスマニュアル

TrueType フォントはチューリング完全な仮想プロセッサコアを内蔵している。各グリフ内部にはプリヒンティング・バイトコードプログラムが格納されている。インタプリタは制御点グリッドの操作、投影ベクトル・測定ベクトルの射影計算、自由度の調整を通じて、精緻無比なピクセルグリッド調整（Grid-fitting）を実行する。

::: tip 図版 E-1：Courier フォント文字 'T' の低水準制御点トポロジー (Figure E-1)
![Figure E-1: The 'T' of TrueType Courier with instructions](/images/fonts-encodings/fig-app-e1.png)
*図版 E-1：Apple/Bitstream Courier フォント文字 ‘T’ の元の制御点グリッド（原著第 913 頁より）。*
:::

::: tip 図版 E-2：Verdana フォント文字 'O' の仮想マシン命令実行シーケンス (Figure E-2)
![Figure E-2: The 'O' from TrueType Verdana with instructions](/images/fonts-encodings/fig-app-e2.png)
*図版 E-2：Microsoft の名作画面フォント Verdana における文字 ‘O’ のヒンティング実行とピクセル丸めロックの過程（原著第 922 頁より）。*
:::

---

# 付録 F：METAFONT 言語と 3 次スプライン微分幾何学

ドナルド・クヌースが創始した METAFONT 言語は、計算機フォント学史上最も深遠な数学的記念碑である。METAFONT において、文字は静的に描画された輪郭ポリゴンではなく、厳密な代数方程式と微分幾何パラメータによって動的に駆動される「生きたプログラム」である。

::: tip 図版 F-1：古典 Computer Modern フォントファミリー全集（第 1 部） (Figure F-1)
![Figure F-1: The fonts of the original Computer Modern distribution (1/2)](/images/fonts-encodings/fig-app-f1.png)
*図版 F-1：TeX オリジナル配布版に収録された Computer Modern フォントファミリー：ローマン立体、傾斜体、サンセリフ、ボールドの見本（原著第 958 頁より）。*
:::

::: tip 図版 F-2：古典 Computer Modern フォントファミリー全集（第 2 部） (Figure F-2)
![Figure F-2: The fonts of the original Computer Modern distribution (2/2)](/images/fonts-encodings/fig-app-f2.png)
*図版 F-2：Computer Modern の等幅タイプライター体、数式用イタリック、特殊記号の見本（原著第 959 頁より）。*
:::

::: tip 図版 F-3：Computer Modern フォントファミリーの 62 個の幾何パラメータ全景 (Figure F-3)
![Figure F-3: The parameters of the Computer Modern fonts](/images/fonts-encodings/fig-app-f3.png)
*図版 F-3：Computer Modern を生成する 3 次スプライン中核幾何パラメータ図解（原著第 961 頁より）：x-ハイト、ディセンダー深さ、主ステム幅（`stem`）、ヘアライン幅（`hair`）、ドット径（`dot_size`）、セリフ傾角（`serif_drop`）など。*
:::

::: tip 図版 F-4：METAFONT weed 対話的スプライン設計デバッガ画面 (Figure F-4)
![Figure F-4: The window of weed showing METAFONT glyph design](/images/fonts-encodings/fig-app-f4.png)
*図版 F-4：専用グラフィックツール `weed` 上での 3 次スプライン方程式による METAFONT 動的グリフ輪郭デバッグ（原著第 967 頁より）。*
:::

::: tip 図版 F-5：ポーランド古典書体 Antykwa Półtawskiego デジタル版見本 (Figure F-5)
![Figure F-5: The fonts of the Antykwa Półtawskiego distribution](/images/fonts-encodings/fig-app-f5.png)
*図版 F-5：METAFONT パラメータ記述によって復元されたポーランド民族タイポグラフィの至宝 Antykwa Półtawskiego 書体ファミリー（原著第 977 頁より）。*
:::

::: tip 図版 F-6：Antykwa Półtawskiego 書体ファミリーの中核パラメータ骨格 (Figure F-6)
![Figure F-6: The parameters of the Antykwa Półtawskiego font family](/images/fonts-encodings/fig-app-f6.png)
*図版 F-6：Antykwa Półtawskiego 書体ファミリーの特徴パラメータマトリクス図解（原著第 979 頁より）。*
:::

---

# 付録 G：ベジェ曲線（Bézier Curve）の数学的性質とド・カステリョのアルゴリズム

デジタルフォントの輪郭は、本質的に区分 3 次多項式スプライン曲線である。

## G.1 バーンスタイン多項式（Bernstein Polynomials）と基底定義

平面上に $n+1$ 個の制御点 $P_0, P_1, \dots, P_n$ が与えられたとき、$n$ 次ベジェ曲線 $B(t)$ は次のように定義される。
$$B(t) = \sum_{i=0}^n B_{i,n}(t) P_i, \quad t \in [0, 1]$$
ここでバーンスタイン基底多項式 $B_{i,n}(t)$ は次の通りである。
$$B_{i,n}(t) = \binom{n}{i} t^i (1-t)^{n-i}$$

フォント工学において、PostScript Type 1、OpenType CFF、および TrueType（2 次曲線を昇階計算）は一般に 3 次ベジェ曲線（$n=3$）を採用する。
$$B(t) = (1-t)^3 P_0 + 3(1-t)^2 t P_1 + 3(1-t) t^2 P_2 + t^3 P_3$$

## G.2 中核的数学性質

1. **アフィン不変性（Affine Invariance）**：曲線に対する任意の平行移動、回転、拡大縮小、剪断変形は、その制御多角形に対する同一の変換と等価である。
2. **凸包性（Convex Hull Property）**：曲線全体は、その制御多角形の凸包（Convex Hull）の内部に完全に包含される。レンダリングエンジンは、外接矩形クリッピング判定において複雑なスプライン方程式を解くことなく、制御点の極値のみで高速に判定できる。
3. **端点補間と接線幾何**：曲線は厳密に始点 $P_0$ と終点 $P_3$ を通過し、端点における接線方向は最初と最後の制御ベクトル $P_1 - P_0$ および $P_3 - P_2$ に正確に平行である。
   $$B'(0) = 3(P_1 - P_0), \quad B'(1) = 3(P_3 - P_2)$$
4. **変差減少性（Variation Diminishing Property）**：任意の平面直線とベジェ曲線の交点数は、その直線と制御多角形の交点数を決して超えない。これにより、曲線が想定外の不要な振動を起こさないことが数学的に保証される。

## G.3 ド・カステリョのアルゴリズム（De Casteljau's Algorithm）

**ド・カステリョのアルゴリズム（De Casteljau's Algorithm）** は、単純な線形補間に基づく数値的に極めて安定した計算フレームワークである。任意のパラメータ $t \in [0, 1]$ に対し、以下の反復によって点列を構築する。
$$P_i^{[0]} = P_i$$
$$P_i^{[k]} = (1-t) P_i^{[k-1]} + t P_{i+1}^{[k-1]}, \quad k = 1, \dots, n, \quad i = 0, \dots, n-k$$

$k=n$ のとき、最終収束点 $P_0^{[n]}$ は正確に $t$ における曲線の座標 $B(t)$ と一致する！ さらに重要なことに、途中で生成された制御点系列：
* 前半区間の制御点：$P_0^{[0]}, P_0^{[1]}, P_0^{[2]}, P_0^{[3]}$
* 後半区間の制御点：$P_0^{[3]}, P_1^{[2]}, P_2^{[1]}, P_3^{[0]}$

は、元の 3 次ベジェ曲線を二つの独立した滑らかに接続された 3 次曲線へと正確に分割する。ラスタライザ（Rasterizer）はこの性質を利用して再帰的二分割細分（Recursive Subdivision）を実行し、個々の微小曲線と直線線分の離散誤差が単一ピクセル未満になるまで分割を繰り返すことで、驚異的な超高速でアンチエイリアスビットマップラスタライズを完遂するのである！

---

# 結び

ここに、ヤニス・ハラランブス教授の記念碑的大著『Fonts & Encodings』の全十四章および付録 A〜G の学術和訳が完結した。人類の最も原初的な鉛活字の物理力学から、森羅万象を統べる Unicode の符号化空間に至るまで；古典的デスクトップ OS のフォントバスから、現代の Web 動的タイポグラフィと SVG ベクトル流に至るまで；ベジェ曲線の微分幾何学から、仮想マシンのチューリング完全なヒンティング論理に至るまで――デジタルフォントとは単なる計算機工学アルゴリズムの結晶であるのみならず、人類の文字文明がシリコンの時代において永劫に息づくための壮大なる神殿なのである！
