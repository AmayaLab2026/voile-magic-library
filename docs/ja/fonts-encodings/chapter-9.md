---
title: "第 9 章：TeX と Omega におけるフォントとそのインストールおよび使用"
description: "TeX のボックス・グルーモデル、改行アルゴリズム、NFSS、DVI 形式、afm2tfm、fontinst 仮想フォント合成、Omega の16ビット多方向組版を詳解。"
---

# 第 9 章：$\TeX$ と $\Omega$ におけるフォントとそのインストールおよび使用
### Chapter 9: Fonts in $\TeX$ and $\Omega$, Their Installation and Use
選書『Fonts & Encodings』第 235–314 頁
*訳者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

$\TeX$ およびその後継システムである $\Omega$（オメガ）は、世界で最も精緻かつ強力なデジタル組版システムです。そのため、これらのシステムにおけるフォント管理メカニズムは、初学者にとっては極めて複雑で奥深いものに見えることが少なくありません。本章では、$\TeX$ と $\Omega$ のフォント体系を以下の 3 つの中核的観点から包括的かつ厳密に解剖していきます：

1. **$\TeX$ および $\Omega$ におけるフォントの使用**：システムにインストール済みのフォントを、一般的な $\TeX$ や $\LaTeX$ 文書内でどのように呼び出し、設定し、体系化するか；
2. **フォントの基本インストール手順**：PostScript Type 1、TrueType、Multiple Master などの外部アウトラインフォントを、$\TeX$ と $\Omega$ が認識可能な低レベルのメトリックファイルや設定ファイルへ変換するパイプライン；
3. **フォントの高度なカスタマイズ**：仮想フォント（Virtual Fonts, VF）や変換マクロパッケージ（`fontinst` など）を駆使し、複合アクセント文字、特殊リガチャ（合字）、疑似スモールキャピタル（Fake Small Capitals）、さらには文脈依存の接続解析まで実行する高度なカスタムフォントファミリの構築法。

最後に、従来の 8 ビットの壁を打ち破った $\Omega$ システムを取り上げます。複数バイト内部エンコーディング、OFM（Omega Font Metrics）、OVF（Omega Virtual Fonts）、動的有限状態ストリーム変換器 OTP（Omega Translation Processes）、そして 32 種類もの直交書字方向を自在に操る多方向組版エンジンの全貌を明らかにします。

---

## 1. $\TeX$ におけるフォントの使用（Using Fonts in $\TeX$）

### 1.1 $\TeX$ 序論：組版哲学とボックス・グルーモデル（Introduction to $\TeX$）

$\TeX$ がフォントをどのように扱っているかを本質的に理解するためには、WYSIWYG 型デスクトップパブリッシング（DTP）ソフト特有の「画面キャンバス上に文字を直接描画する」という直感的思考をまず捨て去らなければなりません。ドナルド・E・クヌース（Donald E. Knuth）教授が構築した $\TeX$ の宇宙において、組版の中核的本質とは純粋な数学的抽象化と 2 次元配置エンジニアリングに他なりません。

#### ボックス（Boxes）とグルー（Glue）

$\TeX$ は、組版を構成する要素を 2 つの基本的な物理実体に抽象化します。それが**ボックス（Box）**と**グルー（Glue）**です。

1. **ボックス（Box）**：
   $\TeX$ エンジンの視点において、すべての文字、すべての約物（句読点）、すべての罫線、さらには外部の図版に至るまで、例外なく剛体の長方形空間に厳密に封入されます。任意の文字ボックスに対して、$\TeX$ はその内部にどのような美しい曲線が描かれているかには一切関知せず、2 次元平面上における以下の 3 つの幾何学的寸法パラメータのみを追跡します：
   - **幅（Width, $w$）**：現在のベースライン（Baseline）に沿った水平方向の広がり；
   - **高さ（Height, $h$）**：ベースラインから上方のアウトライン最高点までの垂直距離；
   - **深さ（Depth, $d$）**：ベースラインから下方のディセンダ（Descender）最下点までの垂直距離。

   ベースラインは組版の基準線です。文字ボックスの左下隅の少し上が基準原点 $(0,0)$ となります。たとえば、小文字「x」の高さは一般に x-height と呼ばれ、その深さは 0 です。一方、ディセンダを持つ小文字「p」や「y」は正の深さを持ち、アセンダ（Ascender）を持つ小文字「d」や「h」は大きな高さを持ちます。

2. **グルー（Glue）**：
   ボックスが文書という建築物を築く剛直なレンガであるならば、グルーはレンガ同士を接合する弾力的なモルタルです。欧文組版において、単語と単語の間のスペースは固定幅の実体ではなく、伸縮自在のグルーです。グルーは 3 つの数学的成分を持ちます：
   - **自然長（Natural Space）**：外力による伸長・圧縮を受けていない理想的な幅；
   - **伸長量（Stretchability）**：行全体の均等割り付け（Justification）のために文字の総幅が不足している場合、グルーが伸ばされることを許容する最大の弾性マージン；
   - **収縮量（Shrinkability）**：行全体の文字が版面幅をわずかに超過した場合、グルーが縮められることを許容する最大の弾性マージン。

#### 水平ボックス（hbox）と垂直ボックス（vbox）の階層的ネスト

$\TeX$ は、階層的な再帰構造によって微小な要素から巨大なページを組み立てていきます：
- 複数の文字ボックスと単語間グルーが水平方向に順次並ぶことで、**水平ボックス（hbox）**が形成されます。段落内の 1 行のテキストは 1 つの hbox です；
- 複数の水平ボックスと行間グルー（Baselineskip）が垂直方向に上から下へと積み重なることで、**垂直ボックス（vbox）**が形成されます。段落、段組カラム、1 ページ全体、さらには欄外注やノンブルを含む完全な版面も、多層にネストされた vbox なのです。

#### 改行アルゴリズムとデメリット（Line Breaking and Demerits）

一般的なワープロソフトは貪欲法（Greedy Algorithm）を用いて 1 行ずつ組版を行います。行に単語が入る限り詰め込み、溢れたら強制的に改行します。このような局所的最適化戦略は、段落末尾に極端に不揃いな大きな空白や、間延びした行を生み出しがちです。

クヌースは、$\TeX$ のために革新的な大域的動的計画法による改行アルゴリズムを考案しました：
1. **バッドネス（Badness, $b$）**：ある行内のグルーがその自然長からどれほど極端に乖離しているかを表す悪さの指標。行が過度に引き伸ばされたり圧縮されたりすると、バッドネスは急激に増大します；
2. **ペナルティ（Penalties, $p$）**：潜在的な改行位置（ハイフネーション箇所、句読点の後、数式の間など）に意図的に課されるコスト。たとえばハイフンでの改行は正のペナルティを課され、改行禁止箇所では無限大（$+10,000$）となります；
3. **デメリット（Demerits, $d$）**：単一の行のバッドネス、改行ペナルティ、そして隣接する 2 行間のグルーの張りの差異（極端に緩い行の直後に極端に詰まった行が来る視覚的違和感を防ぐ）を総合して算出される段落全体の不快度スコア。

$\TeX$ は段落全体のすべての可能な改行候補を有向非巡回グラフ（DAG）として構築し、動的計画法によってデメリットの総和が最小となる完璧な改行経路を一括探索します。これにより、$\TeX$ が出力する段落の濃度（Typographic Color）は極めて均一で安定したものになります。

#### Computer Modern フォントファミリとオプティカルサイズ

$\TeX$ システムの誕生とともに産声をあげた金字塔的フォントが、クヌース自身がプログラミング言語 METAFONT を用いて設計した **Computer Modern（CM）フォントファミリ**です。CM ファミリは 19 世紀末のスコッチ・モダンフェイス（Monotype Modern 8A を規範とする）をベースに丹念に描かれ、極めて高いストロークコントラスト、幾何学的に垂直な軸、鋭利な極細セリフを特徴とします。

CM ファミリは、以下のような多彩なスタイルバリエーションを網羅しています：
- `cmr`（Computer Modern Roman，立体正体）
- `cmbx`（Computer Modern Bold Extended，太字幅広）
- `cmti`（Computer Modern Text Italic，本文用イタリック斜体）
- `cmsl`（Computer Modern Slanted，斜体／機械的傾斜）
- `cmss`（Computer Modern Sans Serif，サンセリフ体）
- `cmtt`（Computer Modern Typewriter，等幅タイプライター体）
- `cmmi`（Computer Modern Math Italic，数学用イタリック）
- `cmsy`（Computer Modern Math Symbols，数学記号）
- `cmex`（Computer Modern Math Extension，可変伸長数学記号）

さらに決定的なのは、CM ファミリが金属活字時代の**オプティカルサイズ（Optical Sizing）**の伝統を忠実に受け継いでいる点です。金属活字の時代において、5 ポイントの活字は 10 ポイントの活字を単に縮小したものではありませんでした。機械的に縮小すると、小さなサイズの細いストロークは印刷のインク潰れや人間の視覚特性によって完全に消失し、カウンター（文字の懐）が潰れて判読不能になってしまうからです。

クヌースは METAFONT のコード内で、設計サイズごとに精密な視覚補正パラメータを定義しました：
- `cmr5`（5pt）：脚注、添字、複雑な分数の上下付き添字専用。カウンターを広く設計し、ストロークコントラストを抑え、主ステムを相対的に太くし、セリフを肉厚にし、字間を大きく広げています；
- `cmr7`（7pt）：主添字や図表キャプション専用；
- `cmr10`（10pt）：標準的な本文用フォント；
- `cmr12` および `cmr17`（12pt および 17pt）：章見出し・大見出し用。ヘアラインストロークは極限まで繊細かつ鋭利に研ぎ澄まされ、コントラストが極めて高く、字間は緊密に引き締められ、モダンフェイス特有の優雅で気品ある美しさを放ちます。

---

### 1.2 高レベルインターフェース：基本 $\LaTeX$ コマンドと新フォント選択方式 NFSS（The High Level: Basic $\LaTeX$ Commands and NFSS）

初期の Plain $\TeX$ において、フォントの切り替えは極めて原始的かつ硬直的でした。ユーザーは `\font\tenrm=cmr10` のように低レベル命令で特定のフォントを直接読み込み、`\tenrm` と呼び出すしかありませんでした。この手法はフォントファミリ、サイズ、ウェイトが密結合しており、文書全体の本文を 10pt から 12pt に変更したり、CM から Times に差し替えたりする場合、すべての命令を手作業で書き直すという悪夢に直面しました。

この問題を解決するため、フランク・ミッテルバッハ（Frank Mittelbach）とライナー・ショップ（Rainer Schöpf）は 1989 年に $\LaTeX$ のための**新フォント選択方式（New Font Selection Scheme, NFSS）**を設計・導入しました（$\LaTeX 2_\varepsilon$ において NFSS2 へ発展）。

#### NFSS の 5 次元直交選択空間

NFSS の核心は**直交性（Orthogonality）**にあります。フォントの属性を互いに独立した 5 つの離散的次元に完全に分離しました：

| 次元 | コマンド例 | 意味と標準的な値の例 |
| :--- | :--- | :--- |
| **エンコーディング（Encoding）** | `\fontencoding{...}` | フォントのスロット対応規格（`OT1`, `T1`, `TS1`, `T2A`, `LY1` など） |
| **ファミリ（Family）** | `\fontfamily{...}` | フォントファミリの略称（`cmr`, `ptm` [Times], `phv` [Helvetica], `pcr` [Courier] など） |
| **シリーズ（Series）** | `\fontseries{...}` | ウェイト（太さ）と幅の結合（`m` [Medium], `b` [Bold], `bx` [Bold Extended], `c` [Condensed] など） |
| **シェイプ（Shape）** | `\fontshape{...}` | ストロークの姿勢と変体（`n` [Normal 直立], `it` [Italic], `sl` [Slanted], `sc` [Small Caps] など） |
| **サイズ（Size）** | `\fontsize{s}{b}\selectfont` | 物理サイズ $s$ とベースライン送り $b$（例：`\fontsize{10pt}{12pt}\selectfont`） |

NFSS の状態機械において、サンセリフ体（`\sffamily`）を選択している状態で太字コマンド `\bfseries` を実行すると、シリーズ次元のみが変更され（`series = b`）、ファミリ次元（`family = sf`）は厳密に保持されるため、サンセリフ太字が得られます。ローマン太字に勝手に戻ってしまうことはありません。すべての次元の変更は、低レベルプリミティブ `\selectfont` が呼ばれた瞬間に初めて 1 つの具象フォントへと解決されます。

#### フォント定義ファイル（`.fd`）と自動置換

5 次元のパラメータが決まった後、$\LaTeX$ はディスク上のどの `.tfm` メトリックファイルを読み込むべきかを、`<Encoding><Family>.fd` という命名規則の**フォント定義ファイル（Font Definition File）**を参照して決定します。

たとえば、Times ファミリの T1 エンコーディングにおける定義ファイル `t1ptm.fd` の内部構造は以下のようになっています：

```latex
\ProvidesFile{t1ptm.fd}[2001/06/04 font definitions for T1/ptm.]

\DeclareFontFamily{T1}{ptm}{}

\DeclareFontShape{T1}{ptm}{m}{n}{
   <-> ptmr8t
}{}
\DeclareFontShape{T1}{ptm}{m}{it}{
   <-> ptmri8t
}{}
\DeclareFontShape{T1}{ptm}{m}{sl}{
   <-> ptmo8t
}{}
\DeclareFontShape{T1}{ptm}{m}{sc}{
   <-> ptmrc8t
}{}
\DeclareFontShape{T1}{ptm}{bx}{n}{
   <-> ptmb8t
}{}
\DeclareFontShape{T1}{ptm}{bx}{it}{
   <-> ptmbi8t
}{}
\DeclareFontShape{T1}{ptm}{b}{n}{<->ssub * ptm/bx/n}{}
\DeclareFontShape{T1}{ptm}{bx}{sl}{<->ssub * ptm/bx/it}{}
```

`\DeclareFontShape` 内の `<-> ssub * ptm/bx/n` は**サイレント置換（Silent Substitution）**を指定しています。文書が通常の太字 `ptm/b/n` を要求したものの、フォント側が幅広太字 `ptm/bx/n` しか提供していない場合、NFSS は組版を中断することなく透過的に代替フォントを割り当てます。

#### NFSS フォントエンコーディング体系の全景

1. **OT1（Old $\TeX$ 1，クヌースの原初 7 ビットエンコーディング）**：
   128 スロットの制約上、ギリシャ大写字母（$\Gamma, \Delta, \dots$）、欧文基本リガチャ（ff, fi, fl, ffi, ffl）、感嘆符・疑問符の倒置符（¿, ¡）が収容されました。しかし、**西欧言語のアクセント付き文字（é, à, ç, ü など）が一切含まれていません**でした。OT1 では `\accent` プリミティブを用いて実行時にアクセント記号を文字の上に重ね合わせていたため、**アクセント付き単語において $\TeX$ の自動ハイフネーション機能が完全に停止してしまう**という致命的な欠陥を抱えていました。
2. **T1（Cork エンコーディング / EC フォント）**：
   1990 年のアイルランド・コーク会議で制定された 8 ビット（256 文字）欧州統一標準です。西欧および東欧の主要ラテン言語に必要なすべてのアクセント付き文字を単一のスロットとして独立収録し、多言語文書における自動ハイフネーションの課題を根本から解決しました。
3. **TS1（Text Companion エンコーディング）**：
   T1 の補助記号セット。ユーロ記号（€）、ポンド（£）、円（¥）、セント（¢）などの通貨記号、度記号、分数、特殊約物を収録します。
4. **T2 系列および X2（キリル文字全集）**：
   スラブ系および非スラブ系キリル諸言語の莫大な文字を網羅するため、T2A, T2B, T2C, T2D, X2 の 5 つのサブエンコーディングに分割体系化されました。
5. **その他の専門エンコーディング**：
   - **T3**：国際音声記号（IPA）；
   - **T4**：アフリカラテン文字体系；
   - **T5**：多重声調とホーン記号を持つベトナム語専用エンコーディング；
   - **LY1（TeX 'n' ANSI）**：Windows ANSI（CP1252）に親和性の高い商業出版用 8 ビットエンコーディング。

#### 数式フォントと微細記号の NFSS メカニズム

$\TeX$ の最も輝かしい功績は、複雑な数式組版能力にあります。しかし、数式モードにおける文字は単なるテキストではなく数学的変数であり、特殊な傾斜とサイドベアリングを持つ数式用イタリック（Math Italic）が必須となります。

さらに、伝統的な $\TeX$ エンジンには**「同時にロード可能な数式フォントファミリは最大 16 個（0〜15）」というハードウェア的な極めて厳しい制限**が存在します。NFSS は以下の抽象マクロによってこの限られた 16 スロットを高度に制御します：
- `\DeclareMathAlphabet{\mathbf}{OT1}{cmr}{bx}{n}`：数式用アルファベットの宣言；
- `\DeclareSymbolFont{letters}{OML}{cmm}{m}{it}`：数式記号ファミリの宣言；
- `\DeclareMathSymbol{\alpha}{\mathord}{letters}{"0B}`：数式記号とスロットの結合。

可変長の大型区切り子（括弧、中括弧など）は、`cmex10` フォント内の上部パーツ（Top）、底部パーツ（Bottom）、中間パーツ（Mid）、そして反復可能な垂直伸長パーツ（Extender）を組み合わせて、任意の高さの括弧をパイプのように組み立てることで実現されます。

---

### 1.3 低レベルメカニズム：$\TeX$ エンジンと DVI バイトコードフォーマット（The Low Level: $\TeX$ and DVI）

ユーザーがコマンドラインで `latex document.tex` を実行した際、$\TeX$ エンジンが出力するのは PDF でも PostScript でもなく、極限まで無駄を削ぎ落としたバイナリ中間形式——**DVI（Device Independent）ファイル**です。

#### DVI 仮想マシンの内部構造とレジスタ状態機械

DVI フォーマットの実体は、純粋な**仮想マシンバイトコード命令ストリーム**です。DVI 仮想マシンは 6 つの中核内部レジスタからなる幾何学的状態機械を維持します：

$$h, v, w, x, y, z$$

- $h$：ページ上の現在の**水平座標**（左基準点から右方向への変位）；
- $v$：ページ上の現在の**垂直座標**（上基準点から下方向への変位）；
- $w, x$：水平方向の移動量を記憶する変位レジスタ；
- $y, z$：垂直方向の移動量を記憶する変位レジスタ。

さらに、DVI 仮想マシンは**座標スタック（Coordinate Stack）**を備えており、`push` 命令で $(h, v, w, x, y, z)$ の全状態を退避し、`pop` 命令で親座標系へ瞬時に復帰できます。

#### DVI 核心バイトコード命令全集

DVI バイトコード命令は極めてコンパクトであり、主に以下のカテゴリに分類されます：
1. **文字配置・出力命令**：`set_char_0` 〜 `set_char_127`（1 バイト命令で文字番号 $c$ を出力し水平座標 $h$ を文字幅分前進させる）、`set1` 〜 `set4`、`put1` 〜 `put4`（文字を出力するが $h$ を前進させない；アクセントの重ね打ち等に使用）；
2. **幾何学的罫線描画命令**：`set_rule`（高さ $a$ と幅 $b$ の黒い長方形を描画し $h$ を前進）、`put_rule`；
3. **座標変位命令**：`right1..4`、`down1..4`、レジスタ付き相対移動 `w`, `x`, `y`, `z`；
4. **フォント定義・選択命令**：`fnt_num_0` 〜 `fnt_num_63`、`fnt_def1..4`（フォント番号、チェックサム、スケーリングサイズ、デザインサイズ、フォント名を登録）；
5. **ページ構造命令**：`bop`（Begin of Page，前ページへの逆方向ポインタ付き）、`eop`（End of Page）、`pre`（Preamble）、`post`（Postamble，全ページ数と全フォント定義リストを総括）、`post_post`。

#### 32 ビット純整数固定小数点演算：Scaled Point 単位 `sp`

クヌースは DVI の設計において鉄の掟を定めました：**「DVI ファイルは、いかなるハードウェア、いかなる OS 上であっても、ピクセル単位で完全に同一の結果を出力しなければならない」**。CPU ごとの浮点数演算（IEEE 754 の丸め誤差）の揺らぎを完全に排除するため、$\TeX$ と DVI の内部における幾何学的距離は**すべて 32 ビット符号付き整数の固定小数点演算**で計算されます。

その最小単位が **Scaled Point（`sp`）** です：

$$1\text{ pt} = 65,536\text{ sp} = 2^{16}\text{ sp}$$

$$1\text{ sp} \approx 5.363 \times 10^{-6}\text{ mm} = 5.363\text{ nm}$$


この単位は可視光の波長よりも微小であり、高精度印刷機の物理解像度を遥かに凌駕します。組版処理中のボックス幅の累積、カーニング、グルーの伸縮はすべて整数の四則演算として実行されるため、累積丸め誤差が絶対に発生しません。

#### DVI バイトコードの逆アセンブル透視：DVX 形式

Haralambous が開発した `dvi2dvx` ツールにより、DVI のバイナリ切片を XML（DVX）として可視化できます：

```xml
<fontdef id="18" checksum="20786036" scale="655360" designsize="655360" name="T1lemondemn"/>
<font id="18"/>
<set>the</set>
<right dim="167112"/>
<set>te</set>
<right dim="-14745"/>
<set>xt</set>
<right dim="167112"/>
<set>tha</set>
<right dim="-18350"/>
<set>t</set>
<right dim="167112"/>
<set>y</set>
<right dim="-11141"/>
<set>ou</set>
<right dim="167112"/>
<set>ar</set>
<right dim="-7864"/>
<set>e</set>
<right dim="167112"/>
<set>curr</set>
<right dim="-9830"/>
<set>ently</set>
<right dim="167112"/>
<set>r</set>
<right dim="-13107"/>
<set>eading</set>
```

この切片から明らかなように、単語間のグルー展開量（`dim="167112"`）だけでなく、文字間のカーニング調整（`-14745` や `-18350`）も、$\TeX$ によってすでに計算され、直接物理座標の変位として焼き込まれています。

#### 文字ボックスと物理的インクの完全な分離

この低レベルメカニズムは、$\TeX$ の最も深遠な設計思想を物語っています：**$\TeX$ の内部には文字の「輪郭（Glyph）」は存在せず、あるのはただの「幾何学的ボックス（Box）」である**ということです。
- $\TeX$ エンジンはボックスをどこに配置するかのみを計算します；
- DVI ファイルには、どの位置にどの文字番号を置くかだけが記録されます；
- 文字がどのような黒白ビットマップか、あるいはどのような 3 次ベジェ曲線アウトラインかについて、$\TeX$ は一切知りませんし、知る必要もありません；
- 実際の物理的ラスタライズとインク描画は、コンパイルパイプラインの後処理工程——すなわち**デバイスドライバ（DVI Drivers）**へと完全に委ねられているのです。

---

### 1.4 ポスト $\TeX$ 時代：物理的出力と現実世界への対峙（“Après-$\TeX$”: Confronting the Real World）

DVI ファイルを PostScript や PDF に変換するドライバの代表格が、トーマス・ロキツキ（Tomas Rokicki）の `dvips`、および `dvipdfmx` です。

#### `kpathsea` と自動フォント生成パイプライン

現代の $\TeX$ 配布物では、カール・ベリー（Karl Berry）の `kpathsea` パス検索ライブラリがすべてのツールに統合されています。
`dvips` が DVI ファイル内のフォントに遭遇すると、`kpathsea` は以下の自動パイプラインを起動します：
1. **`mktextfm`**：メトリック TFM が見つからない場合、バックグラウンドで自動生成；
2. **`mktexmf`**：METAFONT ソースが見当たらない場合、動的にソースを合成；
3. **`mktexpk`**：指定されたプリンタ解像度（600 DPI など）に応じて METAFONT を起動し、圧縮ビットマップフォント（`.pk`）を生成。

#### `dvips` による PostScript Type 1 フォントの処理と `psfonts.map`

出版業界が PostScript などのベクター形式へ移行するにつれ、`dvips` は **`psfonts.map`**（または `pdftex.map`）を読み込んで Type 1 フォントと TFM を結びつけるようになりました：

```text
ptmr8t Times-Roman " T1Encoding ReEncodeFont " <[T1-WGL4.enc <ptmr8a.pfb
```

この 1 行により、論理 TFM 名 `ptmr8t` は、PostScript 内部フォント名 `Times-Roman`、再エンコード処理 `" T1Encoding ReEncodeFont "`、エンコーディングファイル `T1-WGL4.enc`、そして実体アウトラインファイル `ptmr8a.pfb` の埋め込み指定へと結びつけられます。

#### `pdftex` とマイクロタイポグラフィ（Micro-typography）

1996 年、ハーン・テ・タイン（Hàn Thế Thành）が開発した **`pdftex`** は、DVI を経由せず直接 PDF を出力する革命を起こしました。さらにタインは、ヘルマン・ツァップ（Hermann Zapf）が提唱した現代組版の最高峰アルゴリズムを実装しました：

1. **マージンカーニング / プロトルージョン（Character Protrusion）**：
   行頭や行末にある句読点や特定の文字（A, V, W など）を版面の境界線の外側へわずかに（文字幅の 20%〜70%）突出させることで、人間の視覚認知における行末のガタつきを解消し、直線的で美しいマージンを形成します；
2. **フォントの微小伸縮（Font Expansion / hz-algorithm）**：
   単語間のグルー調整だけでなく、行内のすべての文字のアウトラインを水平方向に極微小（$\pm 1\% \sim \pm 2\%$）に拡大・縮小させることで、字形の歪みを感知させることなく改行の自由度を劇的に向上させ、段落の均一な濃度を達成します。

---

## 2. $\TeX$ への新規フォントの導入（Installing Fonts for $\TeX$）

### 2.1 $\TeX$ ディレクトリ構造（TDS）規格
- `fonts/afm/`：Adobe メトリック（`.afm`）
- `fonts/type1/`：PostScript Type 1 アウトライン（`.pfb`）
- `fonts/truetype/`：TrueType アウトライン（`.ttf`）
- `fonts/opentype/`：OpenType アウトライン（`.otf`）
- `fonts/tfm/`：$\TeX$ フォントメトリック（`.tfm`）
- `fonts/vf/`：仮想フォント（`.vf`）
- `fonts/map/`：ドライバマップファイル（`.map`）
- `tex/latex/`：マクロ定義ファイル（`.fd`, `.sty`）
ファイルを配置した後は、`mktexlsr`（`texhash`）を実行してファイルインデックスを更新します。

### 2.2 簡易ツール：`afm2tfm` の活用
```bash
afm2tfm CentaurMT.afm -v t1centaurmn.vpl -T EC.enc
```
- `-s slant`：幾何学的傾斜による疑似イタリックの生成：
$$\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} 1 & \text{slant} \\ 0 & 1 \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}$$
通常、`-s 0.167`（約 $9.5^\circ$ の傾き、$\text{slant} = \tan \theta$）などを指定します；
- `-d extend`：水平方向の拡大・縮小；
- `-T encfile`：エンコーディングの再マッピング；
- `-v vplfile`：仮想フォント記述ファイル（VPL）の出力。

出力された設定行を `psfonts.map` に追加し、`vptovf` でバイナリの `.vf` と `.tfm` を生成します：

```bash
vptovf t1centaurmn.vpl t1centaurmn.vf t1centaurmn.tfm
```

### 2.3 工業用フォント導入ツール：`fontinst`
商用エキスパートフォント（スモールキャピタル、オールドスタイル数字、特殊リガチャ）を単一の NFSS ファミリへ統合するため、アラン・ジェフリー（Alan Jeffrey）らが開発したのが、$\TeX$ 自身で記述された超強力マクロパッケージ **`fontinst`** です。

```
[原始 AFM ファイル] 
      │ (\transformfont で変換)
      ▼
[MTX メトリックファイル] (\setglyph, \setglyphdim 等のテキスト記述)
      │
      ├───────────────────────┐
      ▼                       ▼
[ETX エンコーディング目標]    [ユーザー定義ルールスクリプト]
      │                       │
      └───────────┬───────────┘
                  │ (\installfont で合成)
                  ▼
         [VPL 仮想プロパティリスト] + [PL プロパティリスト]
                  │
      ┌───────────┴───────────┐
      ▼ (vptovf を呼出)       ▼ (pltotf を呼出)
[VF 仮想フォントファイル]  [TFM メトリックファイル] + [.fd 定義ファイル]
```

ユーザーは簡潔なドライバスクリプト（`install-centaur.tex`）を実行するだけで、AFM の解析、TeXBase1 (8r) へのマッピング、`latin.mtx` による複合アクセント文字の合成、そして最終的な `t1centaur.fd` の生成までが全自動で完結します：

```latex
\input fontinst.sty

\needsfontinstversion{1.926}

\recordtransforms{centaur-rec.tex}

\transformfont{rcen8r}{\reencodefont{8r}{\fromafm{CentaurMT}}}
\transformfont{rceni8r}{\reencodefont{8r}{\fromafm{CentaurMT-Italic}}}
\transformfont{rcenb8r}{\reencodefont{8r}{\fromafm{CentaurMT-Bold}}}
\transformfont{rcenbi8r}{\reencodefont{8r}{\fromafm{CentaurMT-BoldItalic}}}

\installfonts

\installfamily{T1}{centaur}{}

\installfont{rcen8t}{rcen8r,latin}{t1}{T1}{centaur}{m}{n}{}
\installfont{rceni8t}{rceni8r,latin}{t1}{T1}{centaur}{m}{it}{}
\installfont{rcenb8t}{rcenb8r,latin}{t1}{T1}{centaur}{bx}{n}{}
\installfont{rcenbi8t}{rcenbi8r,latin}{t1}{T1}{centaur}{bx}{it}{}
\installfont{rcenc8t}{rcen8r,latin}{t1c}{T1}{centaur}{m}{sc}{}
\installfont{rceno8t}{rcen8r,latin}{t1j}{T1}{centaur}{m}{ol}{}

\endinstallfonts

\endrecordtransforms
\bye
```

### 2.4 Multiple Master フォントの $\TeX$ への適用
ウェイト、幅、オプティカルサイズが連続変化する Multiple Master（MM）フォントは、LCDF Typetools の `mmafm` および `mmpfb` を用いて特定座標の離散的インスタンスを切り出します：

```bash
mmafm --weight=380 --width=460 --optical-size=6 MinionMM.amfm > minion_380_460_6.afm
mmpfb --weight=380 --width=460 --optical-size=6 MinionMM.pfb  > minion_380_460_6.pfb
```

切り出された単体 Type 1 フォントは、`psfonts.map` に登録されることで、通常のフォントと同様に NFSS 体系内にシームレスに組み込まれます。

---

## 3. ユーザーの要求に応じた $\TeX$ フォントのカスタマイズ（Customizing $\TeX$ Fonts for the User's Needs）

### 3.1 仮想フォント（Virtual Fonts）の設計思想
仮想フォント（`.vf`）は、DVI 仮想マシン上で動作する高レベルのマクロ展開ルールです。
- ある文字スロットを別のフォントの特定文字へ転送する；
- ベース文字の上にアクセント記号を相対移動（`right`, `down`）して重ねる；
- 仮想フォントから別の仮想フォントを再帰的に呼び出す；
- PostScript 特効コードを直接埋め込む。
ドライバ側で透過的に展開されるため、$\TeX$ 本体の組版エンジンには一切の負荷や複雑化を与えません。

### 3.2 ETX と MTX によるリガチャ・メトリック記述

#### ETX ファイルのリガチャ状態機械
```latex
\setslot{f}
   \ligature{LIG}{i}{f_i}
   \ligature{LIG}{f}{f_f}
   \ligature{LIG}{l}{f_l}
\endsetslot
```
1. **`LIG`（完全置換）**：
$$A + B \to C$$
入力文字 $A$ と $B$ を消費し、合字 $C$ を出力；
2. **`/LIG`（後方置換・前方保持）**：
$$A + B \to A + C$$
3. **`LIG/`（前方置換・後方保持）**：
$$A + B \to C + B$$
4. **`/LIG/`（文脈保持・中間挿入）**：
$$A + B \to A + C + B$$

#### MTX ファイルの文字合成とカーニング継承
```latex
\setleftkerning{Eacute}{E}{1000}
\setrightkerning{Eacute}{E}{1000}
```
アクセント文字 `Eacute` の左右のカーニング特性を、母体文字 `E` から 100% 継承させることで、何千ものカーニングペアを手作業で定義する労力を一瞬で削減します。

### 3.3 実践的応用事例

#### 事例 1：疑似スモールキャピタル（Fake Small Caps）の精密合成
```latex
\setint{smallcapsscale}{800}
\setint{smallcapskerning}{900}

\installglyph{Asmall}{A}{
   \glyph{A}{\int{smallcapsscale}}
   \movert{\int{smallcapskerning}}
}
```
大文字を 80% にスケーリングし、縮小によって詰まりすぎた字間を `smallcapskerning` で広げることで、均一な組版濃度を達成します。

#### 事例 2：カスタムリガチャの追加
フランス語の敬称略記（Mademoiselle $\to$ $\text{M}^{\text{lle}}$，Madame $\to$ $\text{M}^{\text{me}}$）やオランダ語の「ij」「uw」リガチャ木構造を構築。ユーザーが通常の文字列 `Mlle` を入力するだけで、リガチャ状態機械が $M+l \to M_l \to M_{ll} \to M^{lle}$ と自動遷移します：

```latex
\setslot{M}
   \ligature{LIG}{l}{M_l}
\endsetslot

\setslot{M_l}
   \ligature{LIG}{l}{M_l_l}
\endsetslot

\setslot{M_l_l}
   \ligature{LIG}{e}{M_l_l_e}
\endsetslot
```

#### 事例 3：8 ビット仮想フォントによるアラビア文字の文脈接続解析
アラビア文字の 4 つの形態（独立形、語頭形、語中形、語末形）を、8 ビット $\TeX$ のリガチャ機械（`/LIG`, `LIG/`）を巧みに連鎖させることで、完全自動選択させるオートマトンを構築。

#### 事例 4：狭幅文字置換によるアクセント衝突の回避
背の高いアクセント母音（è, ê, ë）の直前で、頭部の出っ張りを抑えた `f.narrow` を `LIG/` で自動選択し、インクの衝突を回避。

#### 事例 5：ベトナム語のホーン（角）付き母音と多重アクセント処理
基底母音（o, u）とホーン記号を合成し、さらに声調記号を配置する際に「一時的に角の存在を忘れて母音中心に記号を配置する」幾何補正アルゴリズム。

#### 事例 6：古典多調ギリシャ語（Polytonic Greek）のアクセント重畳
気符（有気記号・無気記号）、調符（鋭アクセント・曲アクセント）、イオータ・サブスクリプトの 2 重・3 重の幾何学的スタック計算。

---

## 4. 16 ビットと多方向組版の新世紀：$\Omega$（オメガ）システム

### 4.1 従来の 8 ビット $\TeX$ の物理的限界
1. 1 フォントあたり 256 文字の上限（東アジア CJK の膨大な文字集合を扱えない）；
2. 数式フォントファミリ最大 16 個の制限；
3. 左から右（LTR）への水平方向に固定された 1 次元組版パイプライン。

### 4.2 $\Omega$ のアーキテクチャ革新
Yannis Haralambous と John Plaice が開発した $\Omega$ は、内部文字表現を **16 ビット / 32 ビット（Unicode 完全互換）** に拡張しました。
- **OFM（Omega Font Metrics）**：階層型テーブル構造（Level 1）により、東アジアの数万文字のメトリックを省メモリでサポート；
- **OVF（Omega Virtual Fonts）**：複数バイト対応の次世代仮想フォント。

### 4.3 中核エンジン：OTP（Omega Translation Processes）
組版パイプライン内に自由に組み込める宣言型有限状態ストリーム変換エンジンです。`.otp` ソースを `otangle` でコンパイルし、`.ocf` フィルタとして実行します。
入力文字コード変換（Shift_JIS $\to$ Unicode など）、文字転写、文脈依存字形置換などを、改行処理の前後に柔軟にフックさせることが可能です：

```otp
input: 2;
output: 2;

expressions:

`a'  => @"03AC";
`e'  => @"03AD";

"s" { " " | "." | "," | ";" | "!" | "?" } =>
   @"03C2" ;
```

### 4.4 32 方向の動的多方向組版システム
文字の進行方向（L, R, T, B）と行の進行方向（L, R, T, B）を直交組み合わせることで、**32 種類の書字方向**を完全サポートします：

| モード | 文字進行方向 | 行進行方向 | 代表的組版文化・言語 |
| :---: | :---: | :---: | :--- |
| **`TL`** | 上から下（Top to Bottom） | 右から左（Right to Left） | **東アジア古典籍縦組み**：日本語・中国語・韓国語の伝統的縦書き |
| **`TR`** | 上から下（Top to Bottom） | 左から右（Left to Right） | **伝統的モンゴル文字**および満洲文字縦組み |
| **`LT`** | 左から右（Left to Right） | 上から下（Top to Bottom） | **現代欧文および現代和文横組み**（世界標準横書き） |
| **`RT`** | 右から左（Right to Left） | 上から下（Top to Bottom） | **アラビア語・ヘブライ語・ペルシア語横組み** |
| **`BL`** | 下から上（Bottom to Top） | 右から左（Right to Left） | 歴史的碑文・古文字学（古代オガム文字変種等） |
| **`BR`** | 下から上（Bottom to Top） | 左から右（Left to Right） | 古代マヤ碑銘・特殊学術図表 |
| **`LB`** | 左から右（Left to Right） | 下から上（Bottom to Top） | 地中海牛耕式転回組版（Boustrophedon）移行行 |
| **`RB`** | 右から左（Right to Left） | 下から上（Bottom to Top） | 反転拓本・牛耕式組版 |

改行アルゴリズムやグルーの伸縮計算がすべての方向において数学的に対称に動作し、縦組みボックスと横組みボックスを 1 ページ内で自在にネストすることが可能です。

---

## 5. 結論と未来への展望（Conclusions and Glimpses at the Future）

### 古典的アーキテクチャの歴史的使命
TFM、DVI、仮想フォントは、メモリが極度に乏しかった時代に驚異的な組版美を実現しました。しかし、現代の印刷出版界が OpenType（GSUB、GPOS、BASE テーブルを内包）と PDF を標準とする中で、外部メトリックや DVI に依存する古典的構造はその歴史的使命を終えつつあります。

### $\Omega$ から Aleph、XeTeX、そして LuaTeX へ
$\Omega$ が切り拓いた多方向組版と 16 ビット Unicode の先駆的試みは、現代の組版エンジンへと確実に受け継がれました：
1. **Aleph（$\aleph$）**：$\Omega$ の多方向組版と安定した `pdftex` の融合；
2. **XeTeX**：OS ネイティブのフォント描画（Core Text, HarfBuzz）を直接活用し、システム上の OpenType フォントを即座に利用可能にした実用主義的エンジン；
3. **LuaTeX**：$\TeX$ の心臓部に Lua スクリプトインタープリタを埋め込み、内部データ構造を完全に公開した現代の極限的 $\TeX$ エンジン。

クヌースが黒板に記したボックスとグルーの数式から、Haralambous が描いた $\Omega$ の多次元組版の夢を経て、現代の LuaTeX や HarfBuzz に至るまで、至高の組版の美を追求する精神は、デジタル文明の星河の中で今なお燦然たる輝きを放ち続けています。
