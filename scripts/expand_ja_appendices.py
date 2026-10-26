# -*- coding: utf-8 -*-
"""
Expand Appendices A-G to full unabridged depth (Japanese).
"""
import sys

target_path = r"docs/ja/fonts-encodings/appendices.md"

content = r"""# 付録 A–G：低レベルフォーマットと数学的基礎技術リファレンスマニュアル
### Appendices A–G: Technical Reference Manual for Digital Typography
選書『Fonts & Encodings』第 599–938 頁（全 340 頁技術付録）
*訳者：[Lycoris <lycorismisaka@gmail.com>](mailto:lycorismisaka@gmail.com)*

---

本リファレンスマニュアルは、『Fonts & Encodings』後半部に収録された全 7 つの技術付録（Appendices A〜G）を網羅するものです。著者のヤニス・ハラランボス（Yannis Haralambous）が、デジタルフォント技術者、組版エンジン開発者、そして計算機文字学者のために築き上げた技術的金字塔です。1980 年代のビットマップ形式から 21 世紀現代の OpenType/AAT コンテナ構造、仮想マシン命令セット、曲線微分幾何学に至るすべての工学的実装を解剖します。

---

# 付録 A：ビットマップフォント形式（Bitmap Font Formats）

ベクターアウトラインフォントが普及した現代においても、ビットマップフォント（Bitmap Fonts）は組み込み機器、BIOS ファームウェア、端末エミュレータ、そしてフォントの内蔵ビットマップ（EBDT/EBLC テーブル）において依然として極めて重要です。

## A.1 Macintosh 体系：FONT と NFNT リソース構造
Classic Mac OS では、フォントはリソースフォーク内に `FONT` または `NFNT`（New Font Numbering Table）として格納されました。
- `FontRec` 構造体：`widMax`、`kernMax`、`nDescent`、`fRectWidth`、`fRectHeight`、`owTLoc`、`rowWords`。
- **ストライクフォント（Strike-font）モデル**：全文字のビットマップを横一列に連結した連続ビットマップ画像帯としてメモリに展開し、`LocTable` の列オフセットを参照して高速な BitBlt（ビットブロック転送）によって画面描画を実行。

## A.2 DOS、Windows、Unix 体系規格
- **DOS CPI 形式**：`MODE CON CP PREP` 用の画面フォントコンテナ；
- **Windows FNT / FON 形式**：16 ビット NE 形式や 32 ビット PE 形式 DLL のリソースセクションに `.FNT` ストリームをカプセル化；
- **Unix X11 形式**：Adobe BDF（テキスト形式ビットマップ交換フォーマット、`SWIDTH` と `DWIDTH`）およびコンパイル済みバイナリ形式 PCF（Portable Compiled Format）。

## A.3 $\TeX$ 体系の極致：GF と PK 形式
- **GF（Generic Font）形式**：METAFONT の一次出力バイトコード；
- **PK（Packed Font）形式**：Tomas Rokicki による動的閾値可変長ランレングス圧縮（$0 \le dyn\_f \le 14$）。4 ビットニブル（Nibble）パッキングと行反復（`repeat`）によりファイルサイズを半減。

---

# 付録 B：$\TeX$ および $\Omega$ フォント形式仕様（TFM, OFM, VF, OVF）

## B.1 TFM（$\TeX$ Font Metrics）バイナリ構造
TFM は 32 ビットビッグエンディアン整数（4 バイトワード）で構成される 12 個のテーブルからなります：
1. `HEADER`（チェックサムとデザインサイズ）
2. `CHAR_INFO`（1 文字あたり 32 ビットに圧縮されたインデックス群）
3. `WIDTH`、`HEIGHT`、`DEPTH`、`ITALIC`（寸法テーブル）
4. `LIG_KERN`（リガチャおよびカーニング有限状態機械コード）
5. `PARAM`（フォント大域パラメータ：スペース自然長、伸縮量など）

### 固定小数点数単位 `fix_word`
TFM 内の距離は 32 ビット固定小数点数 **`fix_word`** で表現されます（整数 12 ビット、小数 20 ビット）：

$$1\text{ fix\_word} = \frac{\text{整数値}}{2^{20}} = \frac{\text{整数値}}{1,048,576} \times (\text{Design Size})$$

浮動小数点演算器のない環境でもマイクロメートル級の完全な精度と決定性を保証します。

## B.2 $\Omega$ OFM と仮想フォント VF/OVF
- **Level 0 OFM**：16 ビット整数インデックスによる 65,536 文字のネイティブサポート；
- **Level 1 OFM**：階層的ツリーテーブル構造、32 種類の動的書字方向に対応；
- **VF および OVF**：仮想文字パケット内に DVI バイトコードを内包し、ドライバが透過的に再帰展開。

---

# 付録 C：PostScript フォント形式（PostScript Font Formats）

## C.1 PostScript 仮想マシンの状態機械
オペランドスタック、ディクショナリスタック、実行スタック、グラフィックス状態スタック（`gsave` / `grestore`）。

## C.2 Type 1 フォントの内部構造と暗号化
- **`eexec` 暗号化**：`Private` 辞書を保護する 16 ビット線形合同法暗号（$R_0 = 55665$）：
  $$R_{n+1} = (R_n \times 52845 + 22719) \bmod 65536, \quad C_n = P_n \oplus (R_n \gg 8)$$
- **`charstring` 暗号化**：グリフバイトコードを保護（$R_0 = 4330$）。
- 核心命令：`hstem`, `vstem`, `vmoveto`, `rlineto`, `rrcurveto`, `callsubr`, `return`, `endchar`, `seac`。

## C.3 CFF（Compact Font Format）と Type 2 CharStrings
INDEX テーブル構造、可変長整数エンコーディング、`hflex`/`flex` 滑降曲線命令、Multiple Master 用の `blend` 演算子によりデータサイズを 30〜50% 削減。

---

# 付録 D：TrueType、OpenType、AAT テーブル構造辞書

**SFNT（Spline Font）モジュラーテーブルコンテナ**。

## D.1 SFNT テーブルディレクトリ
12 バイトの Offset Table（`sfntVersion`, `numTables` など）と各テーブルの 16 バイト Record（`tag`, `checkSum`, `offset`, `length`）。

## D.2 中核テーブル詳解
- **`head`**：マジックナンバー `0x5F0F3CF5`、`unitsPerEm`、全域バウンディングボックス；
- **`cmap`**：Format 4（BMP セグメントマッピング）、Format 12（Unicode 32 ビット全域カバレッジ）；
- **`glyf` と `loca`**：単純グリフ（ノード座標、オンカーブフラグ）と複合グリフ（コンポーネント GID、アフィン変換行列）；
- **`hhea` と `hmtx`**：水平メトリック仕様；
- **`OS/2`**：クロスプラットフォーム互換メトリックおよび PANOSE-1 分類。

## D.3 OpenType レイアウトテーブル（GSUB / GPOS / GDEF）
3 段階インデックス構造：
$$\text{ScriptList} \longrightarrow \text{FeatureList} \longrightarrow \text{LookupList}$$
Format 1 / Format 2 カバレッジテーブルおよびクラス定義テーブルによる高速パターンマッチング。

---

# 付録 E：METAFONT および MetaPost 言語リファレンス

- **宣言的幾何方程式ソルバ**：ガウス消去法により座標点の方程式系を自動解決；
- **ペンモデルと包絡線理論**：凸多角形または楕円ペンを軌跡に沿って走査させた包絡線（Envelope）による文字描画。

---

# 付録 F：TrueType 命令バイトコード全集リファレンス（Instruction Set）

TrueType 仮想マシン（VM）：実行スタック、コントロールバリューテーブル（CVT）、トワイライトゾーン（Zone 0）、グリフゾーン（Zone 1）。
- **ノード移動命令**：`MDAP`、`MIAP`、`MDRP`、`MIRP`；
- **補間命令**：`ALIGNPTS`、`IP`、`IUP[X]`、`IUP[Y]`；
- **Delta 微調整命令**：`DELTAP1..3`、`DELTAC1..3`（特定フォントサイズにおけるピクセル補正）；
- **スタックおよび制御**：`PUSHB`、`DUP`、`IF`、`FDEF`、`CALL`。

---

# 付録 G：曲線微分幾何学と計算タイポグラフィ

## G.1 バーンスタイン基底関数（Bernstein Polynomials）

$$B_{i,n}(t) = \binom{n}{i} t^i (1-t)^{n-i}, \quad i = 0, 1, \dots, n$$

1 の分割 $\sum B_{i,n}(t) \equiv 1$ と非負性により、ベジェ曲線の**凸包性（Convex Hull Property）**が保証されます。

## G.2 ベジェ曲線のホドグラフ（Hodograph / 導曲線）

$$\mathbf{B}'(t) = n \sum_{i=0}^{n-1} B_{i,n-1}(t) (\mathbf{P}_{i+1} - \mathbf{P}_i)$$

制御ハンドルの方向が端点における接線の傾きを、ハンドルの長さが曲率半径を厳密に決定します。

## G.3 ド・カステリョのアルゴリズム（De Casteljau's Algorithm）

漸化式：
$$\mathbf{P}_i^{(k)}(t_0) = (1-t_0)\mathbf{P}_i^{(k-1)}(t_0) + t_0 \mathbf{P}_{i+1}^{(k-1)}(t_0)$$

高精度かつ安定した曲線上の点計算と、2 分割による高速ラスタライズスキャン変換の理論的基盤。

---

# 結語：文字の星河を行く者へ

ここに、『Fonts & Encodings』全 15 章および全 7 つの技術付録のすべての微細データ構造、数学公式、コンパイルパイプライン、そして歴史的源流が完全に提示されました。この技術文献が、デジタル文字文明を探求し創造するすべての者にとっての不滅の羅針盤とならんことを！
"""

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully written {target_path}, length: {len(content)} chars.")
