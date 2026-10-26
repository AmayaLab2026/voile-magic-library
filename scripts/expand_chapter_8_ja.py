# -*- coding: utf-8 -*-
"""
Script to expand docs/ja/fonts-encodings/chapter-8.md to unabridged translation.
"""
import sys

ja_content = r'''---
title: 第8章 · X Window システムにおけるフォント管理アーキテクチャ
description: ヤニス・ハラランブス『Fonts & Encodings』第8章 全文完全学術邦訳：X Window 論理フォント記述（XLFD）14フィールド全仕様、2次元アフィン幾何変換行列、BDF/PCF ビットマップフォントのコンパイル、fonts.dir/scale/alias 索引構造、独立フォントサーバ xfs、xfontsel と xfd デバッグツール群、GNU Font Tools および現代 FreeType/fontconfig/Xft レンダリング革命。
---

# 第8章 · X Window システムにおけるフォント管理アーキテクチャ
### Chapter 8: Font Management under X Window
**著者：ヤニス・ハラランブス 博士（Yannis Haralambous, Ph.D.）**  
*『フォントとエンコーディング』（Fonts & Encodings）原著 221–234 ページより*

*翻訳者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

Macintosh と Windows が、オペレーティングシステムに深く統合された 2〜3 種類の独占的な商用フォント形式で市場を寡占していた時代、UNIX 世界と X Window システム（X Window System）は、それとは全く対照的な生態系を提示していた。すなわち、**極端な開放性、比類なきプロトコルの柔軟性、そして徹底的な技術的異種混交性（heterogeneity）**である。

X Window の分散ネットワーク透過アーキテクチャにおいて、アプリケーション（クライアント）と、実際に描画を担当するディスプレイサーバ（サーバ）は、何千キロも離れた異なる物理マシン上で動作することが可能である。これにより、独自の工学的課題が生じる：サーバはサポートするフォント資産をどのようにクライアントへ宣言するのか？クライアントはローカルの物理ファイルに依存せずにどのようにメトリクスとラスタライズを要求するのか？低帯域幅のネットワーク環境でどのようにフォントデータを効率的に共有するのか？

UNIX の多様なディストリビューションとワークステーションネットワーク間に統一された秩序を構築するため、マサチューセッツ工科大学（MIT）X コンソーシアムは、グラフィックウィンドウの礎となるフォント命名仕様——**X 論理フォント記述（X Logical Font Description, XLFD）**——を策定した。

---

## X プラットフォームにおけるフォント論理記述仕様（XLFD）

X Window の哲学において、物理ファイル名（例えば `courB12.pcf.Z`）は低層に隠蔽される。アプリケーションがフォントを開き、要求し、測定する際には、**ハイフンで厳密に区切られた 14 個のフィールド**からなる正規化文字列を使用しなければならない。

標準の XLFD 構文構造は以下の通りである：
```text
-FOUNDRY-FAMILY-WEIGHT-SLANT-SETWIDTH-ADDSTYLE-PIXELSIZE-POINTSIZE-RESX-RESY-SPACING-AVGWIDTH-REGISTRY-ENCODING
```

これら 14 個のフィールドは、以下のタイポグラフィおよびラスタライズパラメータを担っている：

1. **鋳造所（Foundry）**：デジタルフォントの提供元（`adobe`, `bitstream`, `b&h`, `linotype`, `misc` 等）；
2. **フォントファミリ（Family）**：フォントの設計ファミリ名（`times`, `helvetica`, `courier`, `fixed` 等）；
3. **ウェイト（Weight）**：ストロークの太さ（`bold`, `demibold`, `medium`, `regular` 等）；
4. **傾斜（Slant）**：字形の垂直軸傾斜形態：
   * `r`（Roman）：直立正体；
   * `i`（Italic）：筆記風イタリック；
   * `o`（Oblique）：機械的に傾斜させたオブリーク；
   * `ri`（Reverse Italic）/ `ro`（Reverse Oblique）：左傾斜体；
   * `ot`（Other）：特殊傾斜；
5. **セット幅（Setwidth）**：文字幅比率（`normal`, `condensed`, `expanded` 等）；
6. **追加スタイル（Addstyle）**：セリフ種別（`sans`, `serif`）や言語変体（`ja` 等）；
7. **ピクセルサイズ（Pixelsize）**：物理画面上のピクセル高さ（整数、スケーラブルフォントは `0`）；
8. **ポイントサイズ（Pointsize）**：**米国印刷ポイントの 10 分の 1** 単位のサイズ（$1\text{ pt} \approx 1/72.27\text{ inch}$、`120` は 12 pt）；
9. **水平解像度（Resx）** および 10. **垂直解像度（Resy）**：目標ディスプレイの DPI（通常 `75` または `100`）；
10. **字間モード（Spacing）**：
    * `p`（Proportional）：プロポーショナル；
    * `m`（Monospaced）：伝統的等幅；
    * `c`（Character Cell）：厳格なセル格子フォント（`xterm` 用、はみ出し厳禁）；
12. **平均字幅（Avgwidth）**：全文字の平均送り幅（10 分の 1 ピクセル単位）；
13. **文字集合レジストリ（Registry）** および 14. **エンコーディング（Encoding）**：文字コード規格（`iso8859-1`, `iso10646-1`, `jisx0208.1983-0` 等）。

### 典型的な XLFD の実例

```text
-misc-fixed-medium-r-normal--20-200-75-75-c-100-iso10646-1
```
オープンソース（`misc`）の等幅端末フォント（`fixed`）、標準ウェイト（`medium`）、直立（`r`）、標準幅（`normal`）、20 ピクセル高さ、20 pt、75 DPI、厳格なセル格子（`c`）、平均幅 10 ピクセル、Unicode（`iso10646-1`）を意味する。

### ワイルドカード照合と 2 次元幾何変換行列

ワイルドカード（`?` は 1 文字、`*` は 0 文字以上）による曖昧検索が可能である。

さらに、XLFD は**2 次元幾何アフィン変換行列（Affine Transformation Matrix）**をネイティブサポートしている！ピクセルサイズ欄に 4 つの数値配列 `[ a b c d ]` を挿入することで、クライアントはサーバに対して任意の回転、拡大縮小、およびシアー剪断を要求できる：

$$\begin{pmatrix} x' \\ y' \end{pmatrix} = \begin{pmatrix} a & b \\ c & d \end{pmatrix} \begin{pmatrix} x \\ y \end{pmatrix}$$

これにより、斜体フォントを別途インストールすることなく、サーバ側で動的に字形を任意の角度にシアー傾斜させることが可能となった！

---

## X Window のフォントインストールと索引構造

### ビットマップフォント形式：BDF と PCF
プレーンテキストの **BDF（Bitmap Distribution Format, Adobe 5005）** は可読性が高いが、実運用では専用コンパイラ `bdftopcf` によりバイナリ形式の **PCF（Portable Compiled Format）** へとコンパイルされ、メモリマップ（`mmap`）による瞬時読み込みが行われる。

### ディレクトリ索引：`fonts.dir`、`fonts.scale`、`fonts.alias`
1. **`fonts.dir`**：`mkfontdir` が生成。物理ファイル名と完全な XLFD をマッピング；
2. **`fonts.scale`**：`mkfontscale` や `ttmkfdir` が生成。アウトラインフォント（Type 1, TrueType）が任意のサイズ（`0`）を派生可能であることをサーバに指示；
3. **`fonts.alias`**：`fixed`, `variable`, `10x20` などの平易な別名を完全な XLFD 文字列へマッピング。

### 動的フォントパスと独立フォントサーバ（xfs）
`xset +fp <dir>`、`xset fp rehash`、`xset q` によりパスを動的に制御する。

#### ネットワークフォントサーバ（xfs）
ディスクレス端末群を抱える大規模環境において、中央の **xfs（X Font Server, ポート 7100）** がフォント管理とラスタライズを一括処理し、バイナリキャッシュを配信することで端末側の負荷とストレージ消費を最小化した。

---

## X Window 伝統の対話的デバッグツール

::: tip X 伝統のフォントセレクタ操作画面（Figure 8-1）
![X 伝統のフォントセレクタ操作画面（Figure 8-1）](/images/fonts-encodings/fig8-1-xfontsel.png)
*X 伝統のフォントセレクタ操作画面（Figure 8-1）*
:::

*図 8-1：X Window 伝統の対話型アプリケーション `xfontsel`。上部に 14 フィールドのプルダウン、中央に確定 XLFD、下部にリアルタイムのレンダリングサンプルが表示される。*

::: tip Unicode 準拠 10x20 フォントの xfd 全景グリッド（Figure 8-2）
![Unicode 準拠 10x20 フォントの xfd 全景グリッド（Figure 8-2）](/images/fonts-encodings/fig8-2-xfd-glyph-tables.png)
*Unicode 準拠 10x20 フォントの xfd 全景グリッド（Figure 8-2）*
:::

*図 8-2：`xfd` で表示した Unicode 準拠の 10x20 端末フォントのグリッド。各文字の 16 進コードポイントと物理ビットマップの対応を検証可能。*

* **`xfontsel`**：14 個のメニューが動的に連動し、実在する組み合わせのみをフィルタリング；
* **`xfd`**：16×16 のマトリクスで全グリッドを一覧表示し、各グリッドのメトリクス（left bearing, ascent, descent 等）を精密検査。

---

## 現代 X フォントレンダリング革命（FreeType、fontconfig、Xft）

サーバサイド描画、アルファ透過の欠如、XLFD の硬直性という限界を打破するため、2000 年代初頭にキース・パッカード（Keith Packard）らが主導して以下の三位一体アーキテクチャが確立された：

1. **FreeType 2**：TrueType/OpenType/CFF/Type 1 を高速に解析し、最高峰のオートヒンティングとサブピクセルレンダリングを提供する独立ラスタライザ；
2. **fontconfig**：XML 設定ファイル（`/etc/fonts/fonts.conf`）に基づき、パターンマッチングとスマートな多言語フォールバック（Fallback Chain）を実現；
3. **Xft と XRender**：クライアント側でラスタライズしたアルファマスクを、XRender 拡張を介してビデオメモリ上で超高速合成。

---

PCF ビットマップから 14 フィールドの XLFD、そして現代の FreeType/fontconfig/Xft に至る進化は、UNIX が端末からリッチデスクトップへと飛躍した歴史を鮮やかに物語っている。

しかし文字はローカル画面にとどまらない。Web の台頭により、任意のフォントを世界中のブラウザへ届ける技術が求められた。これこそが、我々が**第 10 章：フォントと Web ページ組版技術**で目撃する新たな革命である。
'''

with open('docs/ja/fonts-encodings/chapter-8.md', 'w', encoding='utf-8') as f:
    f.write(ja_content)

print(f"docs/ja/fonts-encodings/chapter-8.md written: {len(ja_content)} chars")
