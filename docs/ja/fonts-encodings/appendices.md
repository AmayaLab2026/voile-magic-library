---
title: "付録 A–G：低レベルフォーマットと数学的基礎全景技術リファレンスマニュアル"
description: "ビットマップフォント (A)、TeX/Omega (B)、PostScript Type 1/CFF (C)、TrueType/OpenType テーブル構造 (D)、METAFONT (E)、TrueType 仮想マシン命令セット (F)、曲線微分幾何学 (G)。"
---

# 付録 A–G：低レベルフォーマットと数学的基礎全景技術リファレンスマニュアル
### Appendices A–G: Technical Reference Manual for Digital Typography
選書『Fonts & Encodings』第 599–938 頁（全 340 頁技術付録）
*訳者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

本技術リファレンスマニュアルは、『Fonts & Encodings』後半部に収録された全 7 つの技術付録（Appendices A〜G）を網羅する完全な日本語全訳です。著者のヤニス・ハラランボス（Yannis Haralambous）が、デジタルフォント技術者、組版エンジン開発者、そして計算機文字学者のために築き上げた工学的基盤です。1980 年代のビットマップ形式から 21 世紀現代の OpenType/AAT コンテナ構造、仮想マシン命令セット、曲線微分幾何学に至るすべての数学的・工学的実装を徹底解剖します。

---

# 付録 A：ビットマップフォント形式（Bitmap Font Formats）

ベクターアウトラインフォントが現代のスクリーン表示と商業印刷を席巻した今日においても、ビットマップフォント（Bitmap Fonts）は組み込み機器、BIOS ファームウェア、端末エミュレータ、そしてフォントの内蔵ビットマップ（EBDT/EBLC テーブル）において依然として代替不可能な役割を果たしています。

## A.1 Apple Macintosh 体系：FONT と NFNT リソース構造

クラシック Mac OS（System 1.0 〜 Mac OS 9）において、フォントはリソースフォーク（Resource Fork）内のリソースとしてカプセル化されていました。


::: tip Macintosh 伝統の Chicago フォントの全体ストライク画像（Figure A-1）
![麦金塔操作系统经典 Chicago 字体的全局条带图像（Figure A-1）](/images/fonts-encodings/fig-app-a1.png)
*麦金塔操作系统经典 Chicago 字体的全局条带图像（Figure A-1）*
:::

*図 A-1：Apple Macintosh のメニュー画面で 15 年以上にわたり使用された伝説的フォント Chicago の全体ストライクビットマップ（Strike Bitmap）。ユーロ記号（€）を含む現代改訂版。*

### 1. `FONT` と `NFNT` リソースヘッダー構造

`FONT` は初期の固定サイズビットマップリソースであり、`NFNT`（New Font Numbering Table）は膨大なファミリー番号体系を拡張した進化版です。両者はメモリ内で同一の `FontRec` レコード構造を共有します：

```c
struct FontRec {
    short fontType;       // フォント型フラグ（プロポーショナル/等幅、カラー属性等）
    short firstChar;      // 定義された最初の文字の ASCII/MacRoman コード
    short lastChar;       // 定義された最後の文字コード
    short widMax;         // 最大文字送り幅（バウンディングボックス幅の最大値）
    short kernMax;        // 最大負のカーニング量（先行文字との重なり量）
    short nDescent;       // ディセンダの負の深さ（ベースライン下のピクセル数）
    short fRectWidth;     // ストライク画像（Strike Image）のビットマップ幅
    short fRectHeight;    // ストライク画像（Strike Image）のビットマップ高さ
    short owTLoc;         // オフセット/幅テーブル（Offset/Width Table）へのワードオフセット
    short ascent;         // ベースライン上のアセンダ高さ
    short descent;        // ベースライン下のディセンダ深さ
    short leading;        // 行送り時の推奨行間（Leading）
    short rowWords;       // ビットマップ画像 1 行あたりの 16 ビットワード数（fRectWidth / 16）
};
```

### 2. ストライクフォント（Strike-font）ビットマップモデル

Macintosh は**ストライクフォント（Strike-font）**アーキテクチャを採用しました。これはフォント内の全文字のビットマップを 1 枚の横長ビットマップストリップとして結合したものです：
- すべてのグリフは共通の高さ $fRectHeight$ を持ち、横方向に連結されます；
- `rowWords` はラスタライン 1 行あたりの 16 ビットワード数を規定し、行境界アライメントを保証します；
- `LocTable`（位置テーブル）は各文字がストライクビットマップ内で開始する水平ビット座標を記録します；
- `owTLoc` が指すオフセット/幅テーブルは各文字の論理送り幅（Advance Width）と左サイドベアリング（LSB）を格納します。画面描画時、QuickDraw は BitBlt（Bit Block Transfer、ビットブロック転送）命令を実行し、連続ビデオメモリから指定矩形をフレームバッファへ超高速転送します。

## A.2 DOS、Windows、Unix 体系規格

### 1. DOS CPI 形式（Code Page Information）
IBM PC/MS-DOS 体系における画面表示フォントコンテナです：
- `.CPI` ファイルはファイルヘッダー、フォントヘッダー、コードページデータパケットで構成されます；
- 各フォントパケットは標準 EGA/VGA キャラクタジェネレータ用の $8\times 8$、$8\times 14$、$8\times 16$ ピクセルの生グリフマトリクスを含み、DOS の `MODE CON CP PREP` コマンドでグラフィックスカードの文字ラッチレジスタへ直接ロードされます。

### 2. Windows FNT と FON 形式
Windows 1.0 〜 3.1x で標準とされたビットマップ規格です：
- `.FNT`：個々のポイントサイズと文字セットに対応する生のビットマップバイナリストリーム；
- `.FON`：16 ビット NE（New Executable）または 32 ビット PE（Portable Executable）形式のダイナミックリンクライブラリ（DLL）コンテナ。コードは持たず、リソースセクション（`.rsrc`）内に複数の `.FNT` ストリームをパッケージングします。各グリフは `GLYPHENTRY`（文字幅とビットマップオフセット）によってインデックスされます。


::: tip BDF 仕様における表意文字ビットマップとメトリクス定義（Figure A-2）
![BDF 规范中表意汉字点阵与度量属性的定义模型（Figure A-2）](/images/fonts-encodings/fig-app-a2.png)
*BDF 规范中表意汉字点阵与度量属性的定义模型（Figure A-2）*
:::

*図 A-2：Adobe BDF 規格における単一表意文字のビットマップ配列、バウンディングボックス、ベースラインオフセット、および送り幅ベクトルの定義モデル。*

### 3. Unix および X11 体系：Adobe BDF と PCF 形式
- **BDF（Bitmap Distribution Format）**：ASCII テキストベースのオープンビットマップ交換フォーマット。`FONT`、`SIZE`、`FONTBOUNDINGBOX`、各グリフの `SWIDTH`（スケーラブル幅）、`DWIDTH`（デバイスピクセル幅）、`BBX`、16 進数 `BITMAP` 行で構成されます；
- **PCF（Portable Compiled Format）**：BDF を X サーバー用にバイナリコンパイルした高速テーブル形式で、エンディアン独立なテーブルディレクトリ構造を持ちます。

## A.3 $\TeX$ 体系の精緻：GF と PK 形式

Donald E. Knuth の METAFONT コンパイラと現代の $\TeX$ 出力エンジンにおいて、ビットマップフォントは極めて高度な圧縮数学を誇ります。




::: tip gftodvi により 5,203 DPI で生成された Computer Modern 組版サンプル（Figure A-3）
![gftodvi 在 5,203 DPI 超高分辨率下渲染的 Computer Modern 字母排印图（Figure A-3）](/images/fonts-encodings/fig-app-a3.png)
*gftodvi 在 5,203 DPI 超高分辨率下渲染的 Computer Modern 字母排印图（Figure A-3）*
:::

*図 A-3：クヌースのユーティリティ `gftodvi` が GF フォントから生成した DVI 組版サンプル（5,203 DPI 超高解像度）。*

### 1. GF（Generic Font）形式
METAFONT が `.mf` ソースコードを解釈した直後に出力する原始バイトコードです。グラフィックス描画コマンド `paint_0`..`paint_63`、スキップ行 `skip0`..`skip3`、文字定義 `boc`（beginning of character）、`eoc`（end of character）により、幾何輪郭からラスタライズされたランレングスデータを記述します。

### 2. PK（Packed Font）形式と動的閾値圧縮アルゴリズム
Tomas Rokicki が考案した PK 形式は、GF ファイルを約 50% 圧縮する標準フォーマットです。PK は動的閾値 $dyn\_f$（$0 \le dyn\_f \le 14$）を用いた可変長ニブル（4 ビット）ランレングスエンコーディングを採用しています。

#### 動的圧縮閾値 $dyn\_f$ の数学原理
黒ピクセルと白ピクセルの連続長（Run-length）$L$ をパッキングする際、バイトストリームは 4 ビットのニブル単位に分解されます：
- $L \le dyn\_f$ の場合、単一のニブル（値 $L$）で表現；
- $dyn\_f < L \le (13 - dyn\_f) \times 16 + dyn\_f$ の場合、2 個のニブル $nibble_1, nibble_2$ で表現され、長さは次式で復元されます：
$$L = (nibble_1 - dyn\_f - 1) \times 16 + nibble_2 + dyn\_f + 1$$
- より長いランレングスや 1 行全体の反復（`repeat count`）には特殊オペコードが割り当てられます。各文字の開始時に最適な $dyn\_f$ が動的に算出され、文字パケットヘッダーに格納されます。

---

# 付録 B：$\TeX$ および $\Omega$ フォント形式仕様（TFM, OFM, VF, OVF）

## B.1 TFM（$\TeX$ Font Metrics）データ構造

TFM ファイルは 32 ビットビッグエンディアン符号付き整数（4 バイトワード）で構成される完全な固定長配列の集合です。物理グリフのビットマップや輪郭は一切含まず、組版エンジンが必要とする厳密な幾何寸法と状態機械のみを記述します。

### 1. 固定小数点数単位 `fix_word`
TFM 内のすべての寸法測定値（幅、高さ、深さ、カーニング値など）は、フォントのデザインサイズ（Design Size）を $1.0$ とする **`fix_word`** 形式（32 ビット固定小数点数）で格納されます：
- 符号ビット 1 ビット、整数部 11 ビット、小数部 20 ビット；
- 精度は $2^{-20} \approx 0.00000095$ デザインサイズ単位です：

$$1\text{ fix\_word} = \frac{\text{Stored Integer Value}}{2^{20}} = \frac{\text{Stored Integer Value}}{1,048,576} \times (\text{Design Size})$$

浮動小数点プロセッサが存在しない環境でも、アーキテクチャ間で 1 ナノメートルも狂わない組版の絶対的決定性を保証します。

### 2. `CHAR_INFO` の 32 ビットビットフィールドパッキング
TFM の文字情報は、文字ごとに 32 ビット（4 バイト）の単一ワードへ驚異的な密度でパックされています：

```text
 0                   1                   2                   3
 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|  width_index  | height| depth | italic_index  |tag| remainder |
|    (8 bit)    | (4bit)| (4bit)|    (6 bit)    |(2)|  (8 bit)  |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

- **`width_index`**（8 ビット）：`width` テーブルへのインデックス（最大 256 通りの異なる文字幅）；
- **`height_index`**（4 ビット）：`height` テーブルへのインデックス（最大 16 通りの高さ）；
- **`depth_index`**（4 ビット）：`depth` テーブルへのインデックス（最大 16 通りの深さ）；
- **`italic_index`**（6 ビット）：`italic` 補正値テーブルへのインデックス；
- **`tag`**（2 ビット）：`remainder` の解釈を決定するタグ：
  - `tag = 0`（`no_tag`）：通常の文字。`remainder` は未使用（0）；
  - `tag = 1`（`lig_tag`）：`remainder` は `lig_kern` 配列の開始インデックスを指し、リガチャ・カーニング有限状態機械を起動；
  - `tag = 2`（`list_tag`）：数式フォントにおける拡大グリフチェーン（大括弧や積分記号のサイズ進行）；
  - `tag = 3`（`ext_tag`）：`remainder` は `exten` 配列を指し、上部・反復部・中部・下部グリフから構成される任意長数式括弧の組み立てを指定。

## B.2 $\Omega$ システム OFM（Omega Font Metrics）仕様

8 ビット（256 文字）の制約を打破するため、John Plaice と Yannis Haralambous は $\Omega$ のために OFM 形式を設計しました：
- **Level 0 OFM**：TFM の 16 ビット直接拡張版。文字インデックスを 65,536 まで拡張し、`fix_word` は維持しつつ、Unicode 基本多言語面（BMP）の直接組版を実現；
- **Level 1 OFM**：動的ツリーテーブル構造。Unicode サロゲートペアや SMP 面へのアクセスを可能にし、32 種類の多方向組版（縦書き、右横書き、逆向進行）のための方向固有メトリックテーブルをサポート。

## B.3 仮想フォント VF（Virtual Fonts）仕様

仮想フォントは物理グリフを持たず、DVI バイトコード命令によって複数の物理フォントグリフを合成・再エンコードする極めて洗練された抽象化レイヤーです：
- パケットヘッダー `packet_bytes` と文字コード；
- パケット内部には標準 DVI 命令（`push`, `pop`, `set_char`, `right`, `down`, `fnt_num`）が直接記述され、アクセント付き文字の合成（ベース文字の上にアクセント記号を移動配置）、フォントの混合（Times の英数に Symbol のギリシャ文字を割り当て）、縮小大文字（スモールキャップス）の動的スケーリングを実現します。

---

# 付録 C：PostScript フォント形式（PostScript Font Formats）

## C.1 PostScript 仮想マシンの状態スタック

::: tip PostScript パス構築と塗りつぶしコード例（Figure C-1）
![PostScript 路径构建与填充代码（Figure C-1）](/images/fonts-encodings/fig-app-c1.png)
*PostScript 路径构建与填充代码（Figure C-1）*
:::

*図 C-1：PostScript 言語によるパス構築および塗りつぶし実行命令。*


::: tip 非ゼロ巻き数規則と偶奇規則の物理的塗りつぶし比較（Figure C-2）
![非零缠绕数规则与奇偶环绕规则的物理填充对比（Figure C-2）](/images/fonts-encodings/fig-app-c2.png)
*非零缠绕数规则与奇偶环绕规则的物理填充对比（Figure C-2）*
:::

*図 C-2：自己交差パスに対する非ゼロ巻き数規則（Nonzero Winding Number Rule、左 3 図）と偶奇規則（Even-Odd Rule、右 3 図）の比較。*


PostScript インタプリタはチューリング完全なスタック指向プログラミング言語環境です。以下の独立スタックを維持します：
1. **オペランドスタック（Operand Stack）**：数値、文字列、名前、配列、辞書オブジェクトを操作；
2. **ディクショナリスタック（Dictionary Stack）**：スコープ解決のための辞書スタック（`systemdict`, `globaldict`, `userdict`, フォント固有辞書）；
3. **実行スタック（Execution Stack）**：制御構造（`if`, `ifelse`, `for`, `loop`, プロシージャ呼び出し）；
4. **グラフィックス状態スタック（Graphics State Stack）**：現在の変換行列（CTM）、現在点 $(x, y)$、パス、線幅、色、クリッピング領域（`gsave` と `grestore` で退避・復帰）。

## C.2 Type 1 フォントの内部アーキテクチャと暗号化

Adobe Type 1 フォントは ASCII ヘッダー部、暗号化バイナリ（または 16 進数 ASCII）部、および 512 バイトのゼロクリア部（`cleartomark` 実行前のバッファフラッシュ）で構成されます。

### 1. 2 段階の線形合同法暗号アルゴリズム
Type 1 フォントはリバースエンジニアリング防止と改ざん検知のため、2 つの暗号レイヤーを備えています：
- **`eexec` 暗号化**：`Private` 辞書全体（Subrs、CharStrings、ヒントゾーン）を暗号化。初期キー $R_0 = 55665$；
- **`charstring` 暗号化**：各グリフの描画バイトコードを個別に暗号化。初期キー $R_0 = 4330$。

暗号化・復号アルゴリズムは 16 ビット線形合同法（LCG）漸化式に従います：

$$R_{n+1} = (R_n \times 52845 + 22719) \bmod 65536$$

バイト復号式（$C_n$ は暗号化バイト、$P_n$ は平文バイト）：

$$C_n = P_n \oplus (R_n \gg 8)$$

各暗号化ブロックの先頭には 4 バイトのランダムバイト（Random Bytes）が付加され、暗号文の周波数解析を無効化します。


::: tip 多言語文字メトリクスとオーバーシュートの全景（Figure C-7）
![跨文种字符度量高度与超逸（Overshoot）全景（Figure C-7）](/images/fonts-encodings/fig-app-c7.png)
*跨文种字符度量高度与超逸（Overshoot）全景（Figure C-7）*
:::

*図 C-7：Omega Serif フォントにおけるラテン、アラビア、ヘブライ、アルメニア文字の基準高さと視覚的オーバーシュート量。*


::: tip 文字 ‘H’, ‘O’, ‘m’ のアライメントゾーンとヒント（Figure C-9）
![字母 ‘H’、‘O’、‘m’ 的对齐区与微调主干（Figure C-9）](/images/fonts-encodings/fig-app-c9.png)
*字母 ‘H’、‘O’、‘m’ 的对齐区与微调主干（Figure C-9）*
:::

*図 C-9：PostScript Type 1 字形における水平・垂直ヒント（灰色帯は `BlueValues` アライメントゾーン）。*


::: tip 文字 ‘B’ における 4 重ヒント置換の実行プロセス（Figure C-10）
![字母 ‘B’ 中四重提示替换的执行过程（Figure C-10）](/images/fonts-encodings/fig-app-c10.png)
*字母 ‘B’ 中四重提示替换的执行过程（Figure C-10）*
:::

*図 C-10：文字 ‘B’ 内部におけるヒント置換（Hint Substitution）の段階的プロセス。*


::: tip PostScript Type 1 2連3次ベジェ Flex 機構（Figure C-11）
![PostScript Type 1 双三次贝塞尔 Flex 机制（Figure C-11）](/images/fonts-encodings/fig-app-c11.png)
*PostScript Type 1 双三次贝塞尔 Flex 机制（Figure C-11）*
:::

*図 C-11：2 つの 3 次ベジェ曲線 $abcd$ と $defg$ で構成される Flex 弾性的ヒンティング構造。*

### 2. Type 1 CharString 命令コード全表

CharString バイトストリームは可変長バイトコードで表現されます。数値はスタックにプッシュされ、1 バイトまたは 2 バイト（エスケープコード 12）の命令によって消費されます：

| オペコード | コマンド名 | 引数スタック | 機能解説 |
|:---|:---|:---|:---|
| `1` | `hstem` | $y, dy$ | 水平ヒントステム定義（下端 $y$ と幅 $dy$） |
| `3` | `vstem` | $x, dx$ | 垂直ヒントステム定義（左端 $x$ と幅 $dx$） |
| `4` | `vmoveto` | $dy$ | 現在点から垂直相対移動 $(0, dy)$ |
| `5` | `rlineto` | $dx, dy$ | 現在点から相対直線描画 $(dx, dy)$ |
| `6` | `hlineto` | $dx$ | 水平相対直線描画 $(dx, 0)$ |
| `7` | `vlineto` | $dy$ | 垂直相対直線描画 $(0, dy)$ |
| `8` | `rrcurveto` | $dx_a, dy_a, dx_b, dy_b, dx_c, dy_c$ | 3 次ベジェ曲線描画（制御点 $A, B$ と終点 $C$） |
| `9` | `closepath` | — | パスを閉じ、サブパスを完了 |
| `10` | `callsubr` | $subr\_index$ | `Subrs` 配列内の共通サブルーチン呼び出し |
| `11` | `return` | — | サブルーチン呼び出し元への復帰 |
| `13` | `hsbw` | $sb_x, wx$ | サイドベアリング（LSB）と水平送り幅（Advance Width）の宣言 |
| `14` | `endchar` | — | グリフ輪郭の終了とラスタライザの起動 |
| `12 0` | `dotsection` | — | 小文字 'i' や 'j' のドット等、微小領域のヒント優先度宣言 |
| `12 1` | `vstem3` | $x_1, dx_1, x_2, dx_2, x_3, dx_3$ | 3 本連動垂直ヒント（'m' など同幅ステムの均等化） |
| `12 2` | `hstem3` | $y_1, dy_1, y_2, dy_2, y_3, dy_3$ | 3 本連動水平ヒント（'E' や 'B' の横バー均等化） |
| `12 6` | `seac` | $asb, dx, dy, bchar, achar$ | 標準複合アクセント文字合成（Standard Encoding Accented Character） |
| `12 7` | `sbw` | $sb_x, sb_y, wx, wy$ | 2 次元サイドベアリングおよび送り幅宣言 |
| `12 16` | `callothersubr` | $arg_1..arg_n, n, index$ | ドライバ固有外部サブルーチン呼び出し（Flex 曲線、ヒント置換） |
| `12 17` | `pop` | — | `callothersubr` の戻り値を引数スタックへプッシュ |

## C.3 CFF（Compact Font Format）と Type 2 CharStrings

::: tip 漢字「講」および「皿」におけるカウンター制御（Figure C-12）
![汉字 “講” 与 “皿” 内部的白空主干计数控制（Figure C-12）](/images/fonts-encodings/fig-app-c12.png)
*汉字 “講” 与 “皿” 内部的白空主干计数控制（Figure C-12）*
:::

*図 C-12：複雑な東アジア表意文字に対する PostScript Type 1 / Type 2 のカウンター制御（Counter Control）。*


::: tip CIDFont（Type 0）全体のデリファレンスアーキテクチャ（Figure C-16）
![CIDFont（Type 0）整体解引用架构（Figure C-16）](/images/fonts-encodings/fig-app-c16.png)
*CIDFont（Type 0）整体解引用架构（Figure C-16）*
:::

*図 C-16：CIDFont において CID 番号から字形データを解決する全体パイプライン。*






CFF（PostScript Type 2）は OpenType の `.otf` フォントにおける CFF テーブルとして採用されています：
- **INDEX テーブル**：全オブジェクトの長さとオフセット配列を集約し、ファイル内ポインタの局所性を向上；
- **Type 2 CharStrings の進歩**：
  - `hsbw`/`sbw` を廃止し、最初の移動コマンド（`rmoveto`）のスタック引数余剰分として送り幅を暗黙定義；
  - `blend` オペレータ：Multiple Master フォントの輪郭補間を 1 つの CharString 内で直接実行；
  - 高度な曲線合成命令：`hflex`, `flex`, `hflex1`, `flex1` により、円弧や微小湾曲部を少ないバイト数で記述；
  - ヒント置換（Hint Substitution）のネイティブサポート：マスクビット命令（`hintmask`, `cntrmask`）により、グリフ内の任意の位置でヒント辞書を動的更新。

---

# 付録 D：TrueType、OpenType、AAT テーブル構造辞書

## D.1 SFNT テーブルディレクトリ（Table Directory）

SFNT コンテナはすべての TrueType/OpenType フォントの共通基盤です。ファイル先頭の 12 バイト **Offset Table** から始まります：

```c
struct OffsetTable {
    uint32_t sfntVersion;   // 0x00010000 (TrueType) または 'OTTO' (CFF OpenType)
    uint16_t numTables;     // 格納されているテーブルの総数
    uint16_t searchRange;   // (2^floor(log2(numTables))) * 16 (バイナリサーチ用)
    uint16_t entrySelector; // floor(log2(numTables))
    uint16_t rangeShift;    // numTables * 16 - searchRange
};
```

これに続き、各テーブルごとに 16 バイトの **Table Record** が `tag` のアルファベット昇順で厳密にソートされて配置されます：

```c
struct TableRecord {
    uint32_t tag;          // 4 バイトのテーブル識別子（例: 'cmap', 'glyf', 'head'）
    uint32_t checkSum;     // テーブルデータのチェックサム（32 ビット符号なし加算）
    uint32_t offset;       // ファイル先頭からのバイトオフセット（4 バイト境界にアライメント）
    uint32_t length;       // テーブルの実データ長（パディングを含まない）
};
```

## D.2 中核基本データテーブル

::: tip EBLC ビットマップテーブルにおける水平・垂直メトリクス（Figure D-1）
![EBLC 点阵表中字形的水平与垂直度量（Figure D-1）](/images/fonts-encodings/fig-app-d1.png)
*EBLC 点阵表中字形的水平与垂直度量（Figure D-1）*
:::

*図 D-1：TrueType EBLC テーブルにおける内蔵ビットマップ字形のメトリクス定義。*


::: tip Verdana フォント letter ‘A’ の gasp テーブル制御下におけるピクセル分布（Figure D-3）
![Verdana 字体 letter ‘A’ 在 gasp 表控制下的栅格尺寸分布（Figure D-3）](/images/fonts-encodings/fig-app-d3.png)
*Verdana 字体 letter ‘A’ 在 gasp 表控制下的栅格尺寸分布（Figure D-3）*
:::

*図 D-3：Verdana フォントにおける `gasp` テーブルによるアンチエイリアスとヒンティングの ppem 段階的切り替え。*


### 1. `head`（Font Header）テーブル
フォントの大域的な物理属性を定義します：
- `magicNumber`：常に `0x5F0F3CF5`（ファイル整合性検証用）；
- `unitsPerEm`：仮想デザイングリッドの解像度（TrueType では通常 2048、CFF では 1000）；
- `checkSumAdjustment`：ファイル全体のチェックサム。全ファイルの 32 ビットワードの総和が `0xB1B0AFBA` になるよう調整値を算出；
- `indexToLocFormat`：0 ならば `loca` テーブルは 16 ビット（オフセット値 / 2）、1 ならば 32 ビット絶対バイトオフセット。

### 2. `cmap`（Character to Glyph Index Mapping）テーブル
Unicode コードポイントからフォント内グリフインデックス（GID）への写像を実行します：
- **Format 4**：Unicode 基本多言語面（BMP, U+0000〜U+FFFF）用の区分線形セグメントテーブル。連続するコード範囲を `segCount` 個の区間に分割し、`endCount`, `startCount`, `idDelta`, `idRangeOffset` 配列を用いて $O(\log N)$ の二分探索で GID を高速解決；
- **Format 12**：SMP/SIP（絵文字、歴史的文字、CJK 統合漢字拡張面、U+10000〜U+10FFFF）を網羅する 32 ビット連続範囲マッピングテーブル。

### 3. `glyf`（Glyph Data）と `loca`（Index to Location）テーブル
- **単純グリフ（Simple Glyph）**：輪郭数 `numberOfContours >= 0`。各輪郭の終端点インデックス `endPtsOfContours[]`、バイトごとのフラグ `flags[]`（オンカーブ/オフカーブ、X/Y 差分圧縮フラグ）、X/Y 座標ストリーム、および TrueType バイトコード命令列 `instructions[]`；
- **複合グリフ（Composite Glyph）**：`numberOfContours == -1`。他の単純グリフ（コンポーネント）を参照し、フラグ（`ARG_1_AND_2_ARE_WORDS`, `ARGS_ARE_XY_VALUES`, `WE_HAVE_A_SCALE`, `WE_HAVE_A_TWO_BY_TWO` 等）とアフィン変換行列によってアクセント付き文字や部首合成文字を形成。

### 4. `hhea` と `hmtx` テーブル
水平組版のメトリック仕様です：
- `hhea`：最大アセンダ `ascender`、最大ディセンダ `descender`、行間 `lineGap`、最大送り幅 `advanceWidthMax`、`numberOfHMetrics`（`hmtx` 内のロングホリゾンタルメトリック数）；
- `hmtx`：グリフごとの送り幅 `advanceWidth` と左サイドベアリング `lsb` のペア配列。

### 5. `OS/2` テーブル
Windows と OS/2 の互換性のために設計され、現在では全 OpenType フォントの必須中核テーブルです：
- PANOSE-1 10 バイトフォント分類システム（文字のプロポーション、セリフ形状、コントラスト等の分類）；
- `ulUnicodeRange1`..`4`（128 ビットの Unicode カバレッジビットフィールド）；
- `achVendID`（4 バイトのベンダー識別タグ）；
- `sTypoAscender`, `sTypoDescender`, `sTypoLineGap`（アプリケーション標準行間計算パラメータ）；
- `usWinAscent`, `usWinDescent`（Windows GDI クラッシュ回避クリッピング境界）。

## D.3 OpenType 高度組版レイアウトテーブル（GSUB / GPOS / GDEF）

### 1. 3 段階インデックス階層アーキテクチャ
OpenType レイアウトエンジン（HarfBuzz, DirectWrite, CoreText）は以下の厳密な階層ツリーを走査します：

$$\text{ScriptList} \longrightarrow \text{FeatureList} \longrightarrow \text{LookupList}$$

1. **ScriptList**：書記系（`latn`, `arab`, `cyrl`, `hani` 等）を照合；
2. **LangSysTable**：言語システム（デフォルト `dflt`、言語指定 `TRK `, `URD ` 等）を照合；
3. **FeatureTable**：機能タグ（`liga`, `smcp`, `kern`, `calt`, `mark` 等）から `LookupListIndex` 配列を取得；
4. **LookupTable**：実際の変換を実行するサブテーブル（SubTable）群を包含。

### 2. カバレッジテーブル（Coverage Table）とクラス定義テーブル（ClassDef Table）

::: tip CastleType 社による 202 個の優美なアンパサンド（&）異体字（Figure D-6）
![CastleType 的 202 个花体 Ampersand 字符全景（Figure D-6）](/images/fonts-encodings/fig-app-d6.png)
*CastleType 的 202 个花体 Ampersand 字符全景（Figure D-6）*
:::

*図 D-6：CastleType ファウンドリによる 202 個のカリグラフィ的アンパサンド（&）合字群。*


::: tip Apple Skia フォントの wght 軸における連続変形（Figure D-8）
![Apple Skia 字体在 wght 轴上的连续变形全景（Figure D-8）](/images/fonts-encodings/fig-app-d8.png)
*Apple Skia 字体在 wght 轴上的连续变形全景（Figure D-8）*
:::

*図 D-8：Apple AAT バリアブルフォント Skia の太さ（`wght`）軸に沿った滑らかな連続補間。*

照合高速化のため、すべてのサブテーブルは先頭にカバレッジテーブルを持ちます：
- **Coverage Format 1**：個々の GID の昇順配列；
- **Coverage Format 2**：連続する GID 範囲 `RangeRecord { startCoverageIndex, startGlyphID, endGlyphID }` の配列；
- **ClassDef Table**：グリフをカテゴリ（基底文字、マーク、リガチャ、約物）や文字幅グループ（左側丸みグループ、右側直線グループ）に分類し、マトリクス形式のカーニングや文脈的置換を可能にします。

---

# 付録 E：METAFONT および MetaPost 言語リファレンス

Donald Knuth の METAFONT と John Hobby の MetaPost は、宣言的数式関係（Declarative Equations）に基づくベクターグラフィックス記述言語です。

## E.1 代数方程式による幾何定義

命令型グラフィックス言語（PostScript の `moveto`/`lineto` など）と異なり、METAFONT ではノード座標を連立一次方程式で定義します：

```metafont
z1 = (0.1w, 0.5h);
z2 = (0.9w, 0.5h);
z3 = 0.5[z1, z2] + (0, 0.2h);  % z1 と z2 の中点から 0.2h 上方へシフト
z1 - z4 = z2 - z3;              % 平行四辺形ベクトル関係
```

METAFONT の内部ソルバーはガウス消去法を用いてすべての末知数座標を自動的に解決します。

## E.2 ペン（Pens）と包絡線理論（Envelopes）

::: tip METAFONT 伝統の Computer Modern 書体系統樹（Figure F-1）
![METAFONT 原始 Computer Modern 字体家族谱系（1/2）（Figure F-1）](/images/fonts-encodings/fig-app-f1.png)
*METAFONT 原始 Computer Modern 字体家族谱系（1/2）（Figure F-1）*
:::

*図 F-1：クヌースによるオリジナルの Computer Modern フォントファミリー系統樹。*


METAFONT の描画は「ペン」の概念に依拠します：
- ペンは凸多角形または楕円（`pencircle`）として定義されます；
- パス $z(t)$ に沿ってペン $P$ を走査させる描画は、数学的にはミンコフスキー和（Minkowski Sum）およびその境界である包絡線（Envelope）の生成に相当します：

$\text{Stroke}(z(t), P) = \partial \left( \bigcup_{t} (z(t) + P) \right)$

MetaPost はこの包絡線を正確な 3 次ベジェ曲線アウトラインに変換し、PostScript 形式として出力します。

---

# 付録 F：TrueType 命令バイトコード全集（Instruction Set）

TrueType 仮想マシンは 2 つのスタック（オペランドスタック、呼び出しスタック）、グラフィックス状態（Graphics State）、コントロール値テーブル（CVT）、ストレージエリア（Storage Area）、および Twilight ゾーンを持つスタック型プロセッサです。

## F.1 内部ハードウェアコンポーネント

- **Projection Vector（射影ベクトル $pv$）**：距離測定の方向単位ベクトル；
- **Freedom Vector（自由ベクトル $fv$）**：ノードが移動を許可される方向単位ベクトル；
- **Dual Projection Vector（双対射影ベクトル $dpv$）**：変形前（元のデザイン空間）における距離測定ベクトル；
- **Twilight Zone（黄昏ゾーン）**：グリフ輪郭に属さない計算用の一時ノード（最大 64 個）を保持するメモリ空間。

## F.2 中核命令全集分類

::: tip Courier フォントにおける TrueType 命令制御グリッド（Figure E-1）
![Courier 字体在 TrueType 虚拟机下的指令控制点阵（Figure E-1）](/images/fonts-encodings/fig-app-e1.png)
*Courier 字体在 TrueType 虚拟机下的指令控制点阵（Figure E-1）*
:::

*図 E-1：Courier フォントの大文字 ‘T’ における TrueType 命令によるグリッド適合。*


::: tip Verdana 文字 ‘O’ における MIRP 命令による輪郭制御（Figure E-2）
![Verdana 字母 ‘O’ 在 MIRP 指令控制下的轮廓拟合（Figure E-2）](/images/fonts-encodings/fig-app-e2.png)
*Verdana 字母 ‘O’ 在 MIRP 指令控制下的轮廓拟合（Figure E-2）*
:::

*図 E-2：Verdana 文字 ‘O’ における `MIRP[10110]` 命令による CVT 参照値との距離固定。*


| カテゴリ | オペコード | コマンド名 | 機能と数学的効果 |
|:---|:---|:---|:---|
| **ノード移動** | `0x2E` | `MDAP[a]` | ノードを現在のグリッド線にスナップ（Round Point）。引数 `a=1` で丸め実行 |
| | `0x3E` | `MIAP[a]` | CVT テーブルの指定値に基づきノードを強制位置合わせ |
| | `0xC0`..`0xDF`| `MDRP[abcde]` | 基準ノードからの相対距離を維持しつつ目標ノードを配置（丸め・最小距離制御） |
| | `0xE0`..`0xFF`| `MIRP[abcde]` | 基準ノードから CVT 参照距離を維持して配置（ステム幅の一貫性を強制） |
| | `0x49` | `ALIGNPTS` | 2 つのノードの距離を射影ベクトル上でゼロにし、完全整列させる |
| **補間命令** | `0x39` | `IP` | 2 つの基準ノードの間で 1 つ以上の目標ノードの座標を線形補間 |
| | `0x30`..`0x31`| `IUP[v]` | 輪郭上の移動されていない全ノードを、移動済みノードの間で自動補間（水平/垂直） |
| **ゾーン制御** | `0x02`..`0x05`| `SRP0..3` | 基準ノードポインタ 0, 1, 2 を設定 |
| | `0x06`..`0x09`| `SZP0..3` | ゾーンポインタ（通常グリフゾーンまたは Twilight ゾーン）を設定 |
| **デルタ微調整**| `0x5D` | `DELTAP1` | 指定 PPM（ピクセル・パー・エム、9〜16 ppm）において指定ノードを $\pm n/64$ ピクセル微調整 |
| | `0x71` | `DELTAP2` | 17〜24 ppm におけるノード座標微調整 |
| | `0x72` | `DELTAP3` | 25〜32 ppm におけるノード座標微調整 |
| | `0x73`..`0x75`| `DELTAC1..3` | 特定 PPM における CVT テーブル値自体のデルタ微調整 |
| **算術・スタック**| `0x60` | `ADD` | スタックトップの 2 数を加算 |
| | `0x61` | `SUB` | 減算 |
| | `0x62` | `DIV` | 64 ビット固定小数点数除算 |
| | `0x63` | `MUL` | 64 ビット固定小数点数乗算 |
| | `0x68`..`0x6B`| `ROUND[ab]` | 指定された丸め状態（`RoundState`）に基づき数値を丸める |

---

# 付録 G：微分幾何学と曲線計算の数学的基礎

フォントアウトラインの生成と補間は、パラメトリック多項式曲線とその微分幾何学的性質に完全に支配されています。

## G.1 バーンスタイン多項式（Bernstein Polynomials）

次数 $n$ のパラメトリックベジェ曲線 $B(t)$ は、$n+1$ 個の制御点 $P_0, P_1, \dots, P_n$ とバーンスタイン基底関数の線形結合として定義されます：

$B(t) = \sum_{i=0}^n P_i B_{i,n}(t), \quad t \in [0, 1]$

バーンスタイン基底関数 $B_{i,n}(t)$ の代数定義：

$$B_{i,n}(t) = \binom{n}{i} t^i (1 - t)^{n - i} = \frac{n!}{i!(n - i)!} t^i (1 - t)^{n - i}$$

### 必須の数学的性質：
1. **非負性（Non-negativity）**：すべての $t \in [0, 1]$ において基底関数は常に非負：
$$B_{i,n}(t) \ge 0, \quad \forall t \in [0, 1]$$
2. **単位の分割（Partition of Unity）**：全基底関数の総和は恒等的に $1$ に等しい：
$$\sum_{i=0}^n B_{i,n}(t) = 1$$
3. **凸包性（Convex Hull Property）**：曲線 $B(t)$ は制御点群 $\{P_i\}$ が形成する凸包の内部に完全に包含されます。ラスタライザはこの性質を利用して極めて高速なクリッピングと交差判定を実行します。

## G.2 曲線の導関数とホドグラフ（Hodograph）

ベジェ曲線の 1 階導関数（接線ベクトル）$B'(t)$ は、元の制御点の差分から生成される次数 $n-1$ のベジェ曲線（ホドグラフ）を形成します：

$$B'(t) = n \sum_{i=0}^{n-1} (P_{i+1} - P_i) B_{i, n-1}(t)$$

同様に、曲率を決定する 2 階導関数は次式で与えられます：

$B''(t) = n(n - 1) \sum_{i=0}^{n-2} (P_{i+2} - 2P_{i+1} + P_i) B_{i, n-2}(t)$

パラメトリック平面曲線の幾何学的曲率 $\kappa(t)$：

$\kappa(t) = \frac{x'(t)y''(t) - y'(t)x''(t)}{(x'(t)^2 + y'(t)^2)^{3/2}}$

フォントデザインにおいて変曲点（$\kappa(t) = 0$）および曲率極値（極値点）の正確な検出は、極値ノード（On-curve Extrema）の自動挿入とヒンティング精度に直結します。

## G.3 ド・カステリョの細分アルゴリズム（De Casteljau's Algorithm）

ド・カステリョのアルゴリズムは、ベジェ曲線の任意のパラメータ $t \in [0, 1]$ における点評価および曲線の分割（Subdivision）を数値的に安定した反復線形補間によって実行します：

$P_i^{(0)}(t) = P_i \quad (i = 0, \dots, n)$

$$P_i^{(k)}(t) = (1 - t) P_i^{(k-1)}(t) + t P_{i+1}^{(k-1)}(t) \quad (k = 1, \dots, n; \ i = 0, \dots, n - k)$$

最終的な点 $P_0^{(n)}(t)$ は曲線上の座標 $B(t)$ と厳密に一致します。さらに、中間点群：
- 左側セグメントの制御点：$P_0^{(0)}, P_0^{(1)}, \dots, P_0^{(n)}$
- 右側セグメントの制御点：$P_0^{(n)}, P_1^{(n-1)}, \dots, P_n^{(0)}$

このアルゴリズムにより、浮動小数点丸め誤差を回避しつつ、任意の精度で輪郭を平坦な直線セグメントへと細分化（Flattening）してラスタライザへ供給することが可能となります。

---

# 結語：デジタル文字の工学的尊厳

これら全 7 編の付録が明示しているように、文字の組版とレンダリングは単なるグラフィックデザインの領域に留まりません。それは固定小数点数演算のビット境界から 3 次多項式の微分幾何学、そして仮想マシンのチューリング完全なバイトコードに至るまで、コンピュータサイエンスと応用数学が織りなす精緻な極致です。

*本付録集の全訳および完全技術校正は ヴワル魔法図書館（Voile Magic Library）文献翻訳工房 により完了しました。*
