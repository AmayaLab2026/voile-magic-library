---
title: "第10章：フォントとワールドワイドウェブ（Web）"
description: "完全無削除学術訳：(X)HTML および CSS フォント仕様体系、font-size-adjust による x-height アスペクト比調整、ダウンロード可能フォント（@font-face）、Web フォント埋め込み技術（Bitstream TrueDoc/PFR、マイクロソフト WEFT/EOT）、SVG ベクターフォントアーキテクチャとベジェパス解析。"
head:
  - - meta
    - name: keywords
      content: Webフォント, CSS Fonts, @font-face, font-size-adjust, TrueDoc, PFR, WEFT, EOT, SVGフォント, HTML, XHTML, XML, タイポグラフィ
---

# 第10章：フォントとワールドワイドウェブ（Web）
**ヤニス・ハラランブス（Yannis Haralambous, Ph.D.）著**  
*『Fonts & Encodings』第315〜366頁より*  
*訳者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

ティム・バーナーズ＝リー（Tim Berners-Lee）が最初に HTTP（Hypertext Transfer Protocol）および HTML（Hypertext Markup Language）を定義した当時、わずか20年後に全世界の人々が「.com」を口にする時代が訪れようとは夢にも思わなかったに違いない。ワールドワイドウェブ（World Wide Web）の爆発的普及は、20世紀末の人類情報科学史における最も輝かしい金字塔の一つである。

HTML はマークアップシステム——タグの構造と意味論を規定する規則の集合体である。これは SGML（Standard Generalized Markup Language）から派生したものである。ここでいう「汎用（Generalized）」とは、言語自体が固有の意味論を持たず、形式的な構文ルールのみを提供する枠組みであることを意味する。SGML 文書は複数の**要素（Elements）**から構成され、各要素は通常、開始タグ（`<name>`）と終了タグ（`</name>`）のペアで表される。タグの間には要素の内容（Content）が配置され、他の要素やテキストを入れ子にできる。また、要素は**属性（Attributes）**と呼ばれる任意のメタデータをキーと値のペアとして保持できる。

SGML 文書には通常、**文書型定義（Document Type Definition, DTD）**が付随する。DTD は、文書内で許容される全要素のリスト、保持可能な属性、および要素間の入れ子関係を厳密に規定する。HTML とは、本質的に特定の SGML DTD に基づいて構築された具体的なマークアップ構文である。

しかしながら、すべての命令の実行意味論が完全に厳密かつ決定論的である $\mathrm{\LaTeX}$ とは異なり、HTML のタグに付与された意味論は当初極めて曖昧であり、各ブラウザベンダーによる勝手な解釈の余地を残していた。初期のブラウザ戦争において、大手各社が独自タグを乱立させた結果、HTML 標準は断片化と混乱に見舞われた。

この混乱を収拾し、文書の論理構造と視覚的表現を厳密に分離するため、W3C は2つの強力な基盤を確立した：一つは動的振る舞いを司る **JavaScript**（ECMAScript）であり、もう一つは視覚的スタイリングを専門に担当する**カスケーディングスタイルシート（Cascading Style Sheets, CSS）**である。さらに文書構造自体も、より厳格で機械処理が容易な **XML** 仕様のもとで再構築され、**XHTML** へと結実した。

本章では、Web ブラウザという動的で異機種混在の表示環境において、いかにして高度なタイポグラフィの美学を実現するか——CSS フォント仕様、初期の Web フォント埋め込み技術（TrueDoc、EOT）、そして SVG ベクターフォントの深層構造を体系的に探訪する。

---

## 標準 HTML 要素と書体指定

初期の HTML においては、フォントの制御は極めて原始的であった。かつて広く用いられた `<font face="Arial" size="+2" color="red">` といったタグは、文書構造の中に視覚的装飾を無秩序に混入させる悪習として批判され、CSS の登場とともに非推奨（Deprecated）を経て正式に廃止された。

現代の Web 組版においては、すべての視覚的フォント指定は CSS を通じて実行される。

---

## CSS フォントモジュール仕様（CSS Fonts Module）

CSS におけるフォント指定は、一連の直交するプロパティ群によって厳密に体系化されている：

### フォント指定の中核 CSS プロパティ

#### 1. `font-family`（フォントファミリー）
優先順位の高い順にカンマ区切りで複数のフォント候補を列挙するフォールバックリスト（Fallback List）を定義する。リストの最後には、必ずブラウザ共通の汎用総称ファミリー（Generic Families）を置かなければならない：
* `serif`：明朝・ローマン系有襯線体
* `sans-serif`：ゴシック・サンセリフ系無襯線体
* `monospace`：等幅フォント
* `cursive`：筆記体・草書体
* `fantasy`：装飾的ファンタジー書体

#### 2. `font-style`（フォントスタイル）
グリフの傾斜姿勢を指定する：`normal`（正立）、`italic`（真のイタリック草書体）、`oblique`（幾何学的斜体）。

#### 3. `font-variant`（フォントバリエーション）
`normal` または `small-caps`（スモールキャピタル）。

#### 4. `font-weight`（フォントウェイト）
筆画の太さを指定する：`normal` (400)、`bold` (700)、あるいは 100 から 900 までの 100 刻みの9段階数値。

#### 5. `font-stretch`（フォントストレッチ）
文字の幾何学的幅の伸縮を指定する：`normal`、`condensed`、`expanded` など。

#### 6. `font-size`（フォントサイズ）
絶対サイズキーワード（`xx-small`〜`xx-large`）、相対サイズ（`smaller`、`larger`）、絶対長（`pt`、`px`、`mm`）、または相対単位（`em`、`ex`、`%`）。

---

#### 7. `font-size-adjust`（アスペクト比調整）と x-height の幾何法則

Web タイポグラフィにおいて最も見落とされがちでありながら致命的な問題が、**フォントごとの x-height（小文字 x の高さ）とエムサイズ（身長）の比率（アスペクト比）の劇的な差異**である。

**図 10-1** に示されるように、同じ 100 pt のフォントサイズであっても、小文字の実際の見かけの大きさは書体によって全く異なる：

::: tip 図 10-1：伝統的活字書体における x-height（小文字の高さと全角身長の比率）の比較
![Figure 10-1: Comparison of x-heights of various fonts](/images/fonts-encodings/fig10-1.png)
*図 10-1：同一のエムサイズにおける各種欧文書体の小文字の実際の高さの比較。上から下へ、各主流フォント間で小文字の物理的寸法が大きく乖離していることが一目瞭然である。*
:::

優先度の高い第1候補フォントが利用できず、第2候補のフォントへフォールバックした際、もし両者の x-height 比率が大きく異なっていると、本文の可読性とグレー度が崩壊し、行間が詰まりすぎたり空きすぎたりする現象が発生する。

この問題を解決するため、CSS は **`font-size-adjust`** プロパティを規定した：
$$\text{調整後サイズ} = \text{指定フォントサイズ} \times \left( \frac{\text{指定アスペクト値}}{\text{代替フォント実測アスペクト値}} \right)$$
これにより、いかなる代替フォントが呼び出された場合でも、小文字の見かけの大きさを完全に一定に保つことが可能となる。

---

### ダウンロード可能フォント規格（`@font-face`）

閲覧者のローカル環境に存在しない独自のフォントを用いて Web ページを描画するため、CSS2 において革新的な **`@font-face`** ルールが制定された：

```css
@font-face {
  font-family: "MyCustomSerif";
  src: url("https://example.com/fonts/custom-serif.woff") format("woff");
}

body {
  font-family: "MyCustomSerif", Georgia, serif;
}
```

この仕様により、Web デザイナーは数世紀にわたる印刷用活字の美学をそのままインターネットの世界へと解き放つ自由を獲得した。

---

## 初期の Web フォント配信・埋め込み技術

しかし、1990年代末から2000年代初頭にかけては、著作権侵害を恐れるフォントベンダー各社の抵抗と、回線帯域の狭さゆえに、生の TrueType/OpenType ファイルをそのまま配信することは困難であった。この時代に登場した二大独自技術が以下である：

### 1. Bitstream 社の TrueDoc 動的フォント技術（PFR）

米 Bitstream 社が開発した **TrueDoc** は、Web ページ内で使用されている文字のアウトラインのみを抽出・暗号化し、超軽量な **PFR（Portable Font Resource）** 形式として配信する技術であった：

::: tip 図 10-2：Bitstream WebFont Wizard の操作画面
![Figure 10-2: Bitstream WebFont Wizard interface](/images/fonts-encodings/fig10-2.png)
*図 10-2：WebFont Wizard のインターフェース：[a] フォント選択ウィザード；[b] 文字サブセット選択（英数字、西欧ラテン、カスタム範囲）；[c] グリフ全景プレビュー；[d] ターゲット Web サイトのドメイン URL ロック設定。*
:::

PFR は、フォントを特定の Web サイトのドメイン名に厳格に暗号拘束（URL Locking）することで不正流用を防止した。Netscape Navigator が標準でネイティブサポートした（図 10-6、10-7）。

::: tip 図 10-6：WebFont Wizard により生成された利用可能フォントリストのブラウザ表示画面
![Figure 10-6: Browser display of available fonts generated by WebFont Wizard](/images/fonts-encodings/fig10-6.png)
*図 10-6：ブラウザ上で PFR 動的フォントが正常に認識され、一覧表示されている様子。*
:::

::: tip 図 10-7：ブラウザ上での Palatino Linotype フォントの Unicode 基本ラテン文字の描画プレビュー
![Figure 10-7: Browser rendering of Palatino Linotype glyphs](/images/fonts-encodings/fig10-7.png)
*図 10-7：PFR 形式を通じてクライアントへ動的配信された Palatino Linotype の美しいレンダリング。*
:::

---

### 2. マイクロソフトのフォント埋め込み技術：WEFT と EOT

一方、マイクロソフトは Internet Explorer 向けに **WEFT（Web Embedding Fonts Tool）** と **EOT（Embedded OpenType）** 形式を推進した：

::: tip 図 10-3：マイクロソフト WEFT のシステムフォント検出およびライセンス判定画面
![Figure 10-3: Microsoft WEFT font detection and licensing interface](/images/fonts-encodings/fig10-3.png)
*図 10-3：WEFT のフォントライセンス検査画面。各フォントの埋め込み許可ビット（Embedding Permissions）を厳格に照合する。*
:::

WEFT は、Windows システム内の各フォントの `OS/2` テーブルに刻まれた著作権フラグ（Installable、Editable、Print & Preview、Restricted）を自動検証し、正規のライセンスが許諾されているフォントのみを対象に、ページ内で実際に使用された文字だけを抽出したサブセット EOT ファイルを作成した（図 10-4、10-5）：

::: tip 図 10-4：WEFT による EOT Web フォント作成の中核工程画面
![Figure 10-4: The core steps of creating EOT fonts in WEFT](/images/fonts-encodings/fig10-4.png)
*図 10-4：WEFT の工程：[a] 対象 Web ページの追加；[b] 検出されたフォント一覧；[c] Unicode 文字サブセット選択エディタ；[d] EOT パッケージングウィザード。*
:::

::: tip 図 10-5：WEFT における EOT ファイル生成と CSS コード出力画面
![Figure 10-5: EOT generation and CSS code output in WEFT](/images/fonts-encodings/fig10-5.png)
*図 10-5：WEFT が自動生成した `@font-face` CSS 定義コード。*
:::

---

## SVG 形式とネイティブベクターフォント体系

W3C が制定した 2次元ベクターグラフィックス規格 **SVG（Scalable Vector Graphics）** は、XML 構文のみを用いて自己完結したベクターフォントを定義する**SVG フォント（SVG Fonts）**規格を備えていた。

### SVG フォントのアーキテクチャ

SVG フォントは、`<font>` 要素の中に `<font-face>` および複数の `<glyph>` 要素を内包する形式をとる：

```xml
<svg xmlns="http://www.w3.org/2000/svg">
  <defs>
    <font id="MySVGFont" horiz-adv-x="1000">
      <font-face font-family="MySVGFont" units-per-em="1000"
                 ascent="800" descent="-200" />
      <glyph unicode="A" horiz-adv-x="650"
             d="M 100 0 L 300 700 L 400 700 L 600 0 Z" />
    </font>
  </defs>
</svg>
```

#### SVG フォントメトリクスと配置基準線
SVG は、水平および垂直方向の組版寸法を精密に定義可能な属性群を備えている：

::: tip 図 10-8：SVG font-face 要素の中核幾何メトリクス属性の概念図
![Figure 10-8: Key geometric metric attributes of SVG font-face](/images/fonts-encodings/fig10-8.png)
*図 10-8：SVG フォントのメトリクス：左図は垂直寸法（(1) ascent 上昇幅；(2) descent 下降幅；(3) cap-height 大文字高；(4) x-height）。右図は整列基準線（(5) baseline ベースライン；(6) center line 中心線；(7) overline 上線；(8) strikethrough 取消線；(9) underline 下線）。*
:::

::: tip 図 10-9：水平組版と垂直組版における幾何原点および送りベクトルの比較概念図
![Figure 10-9: Comparison of geometric origins and advance vectors between horizontal and vertical typesetting](/images/fonts-encodings/fig10-9.png)
*図 10-9：組版原点の比較：(1) 矢印の起点はそれぞれ「水平原点」（左）と「垂直原点」（右）；(2) 送り幅変位ベクトル dx および dy。*
:::

---

### 実践解剖：古典的活字グリフを純粋な SVG ベクターパスへ変換する

**図 10-10** は、名作活字 Le Monde Livre の大文字「R」を、純粋な SVG ベジェ曲線パス（`d="..."` 属性）へと幾何分解した圧巻の解析図である：

::: tip 図 10-10：Le Monde Livre フォントの文字「R」を SVG ベジェ曲線パスへ変換した幾何解析図
![Figure 10-10: Geometric analysis of letter 'R' from Le Monde Livre converted to SVG path](/images/fonts-encodings/fig10-10.png)
*図 10-10：文字「R」のアウトラインを構成する各3次ベジェ曲線の制御点（コントロールハンドル）と端点アンカーの連結シーケンスを完全可視化した図。*
:::

各曲線区間は、SVG の `C`（Cubic Bézier Curve）コマンドによって、2個の制御点と1個の終点座標の連なりとしてプレーンテキストで記述される。SVG フォントは一切のバイナリコンパイラを必要とせず、あらゆるテキストエディタで直接閲覧・編集できる究極の透明性を誇った。

---

# 結び

かつて「テキストの表示が乱れやすい不毛の地」と見なされていた万維網（Web）は、CSS フォントモジュールの成熟、`@font-face` の標準化、そして暗号化埋め込み技術から現代のオープンな WOFF/WOFF2 規格への発展を通じて、世界で最もダイナミックかつ表現力豊かなタイポグラフィの舞台へと進化を遂げた。

構造（HTML）、装飾（CSS）、対話（JavaScript）、そしてベクター表現（SVG）の四位一体の協調により、古典活版印刷の栄光と精緻な組版規律は、現代のデジタル Web 空間において完全なる再生を果たしたのである。
