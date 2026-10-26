import opencc, os, re

with open('docs/zh/fonts-encodings/chapter-10.md', 'r', encoding='utf-8') as f:
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

with open('docs/zh-hant/fonts-encodings/chapter-10.md', 'w', encoding='utf-8') as f:
    f.write(hant_protected)
print(f"Wrote docs/zh-hant/fonts-encodings/chapter-10.md ({len(hant_protected)} chars)")

# 2. Build Japanese version for Chapter 10
ja_text = r"""---
title: 第10章：Web ページ組版と Web フォント技術
description: HTML/CSS フォントモジュール仕様（CSS Fonts 1/2/3）、@font-face 規則とフォントマッチングアルゴリズム、動的 Web フォントの歴史的変遷（TrueDoc PFR、WEFT EOT、GlyphGate）と SVG ベクターフォント仕様の全貌
---

# 第 10 章：Web ページ組版と Web フォント技術

*翻訳者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

ティム・バーナーズ＝リー（Tim Berners-Lee）が 1989〜1990 年に欧州原子核研究機構（CERN）でハイパーテキスト転送プロトコル（HTTP）とハイパーテキスト記述言語（HTML）を発明したとき、20余年後に世界中が「.com」に熱狂することになるとは夢にも思わなかったでしょう。World Wide Web の爆発的な普及は、20世紀末における人類の科学技術史上最大のハイライトの一つです。

しかし、Web の黎明期におけるフォント組版能力は極めて貧弱なものでした。初期のインターネットは高エネルギー物理学者や学術研究者を主たる対象としており、ネットワーク通信の目的は純粋なテキストと研究データの迅速な共有にありました。視覚的な美しさや印刷レベルの高度な組版は考慮されていませんでした。しかし Netscape Navigator と Microsoft Internet Explorer の激しいブラウザ戦争を経て、何億人もの一般ユーザが Web に流入するにつれ、「ブラウザ上でも高品質な印刷物と同等の優美なタイポグラフィを実現したい」という要求が急速に高まりました。

本章では、Web 技術の進化におけるフォント組版の歴史と技術的基盤を包括的に解説します：
1. **(X)HTML とカスケーディングスタイルシート（CSS）のフォントモデル**：原始的な HTML フォントタグから CSS Fonts 仕様（CSS 1, CSS 2/2.1, CSS 3）、フォントマッチングアルゴリズム、および `@font-face` による動的 Web フォント読み込み機構；
2. **初期 Web フォント配信と埋め込み形式の先駆者たち**：Bitstream 社の **TrueDoc（PFR 形式）**、Microsoft 社の **WEFT および Embedded OpenType（EOT 形式）**、em2 Solutions 社の **GlyphGate** 動的グリフサーバ；
3. **SVG（Scalable Vector Graphics）と SVG フォント体系**：XML 構文の基礎から SVG フォント仕様、`<font>`, `<font-face>`, `<glyph>`, `<hkern>` 要素およびベクターパス幾何の全貌。

---

## 1. (X)HTML、CSS とフォント仕様の変遷

### 1.1 原始的 HTML フォントタグの限界

CSS が普及する以前、Web 制作者がフォントを指定する唯一の手段は、HTML 3.2 時代に導入された `<font>` タグでした：
```html
<p>
  <font face="Verdana, Arial, Helvetica" size="3" color="#333333">
    初期の Web テキストの例です。
  </font>
</p>
```
しかし、この仕組みは重大な欠陥を抱えていました：
1. **文書構造と視覚表現の混濁**：HTML の意味論（セマンティクス）が破壊され、マークアップが肥大化しました。
2. **ローカル環境への絶対的依存**：`face` 属性に指定されたフォントが読者のコンピュータに物理的にインストールされていなければならず、環境によってレイアウトが崩壊しました。
3. **印刷メトリクスとの断絶**：`size="1"` から `size="7"` までの粗い相対指定しか存在せず、ポイント数やレディング（行送り）の厳密な制御が不可能でした。

1996 年末に W3C が CSS 1 を策定し、続く CSS 2 および CSS 3 で本格的な Web タイポグラフィ基盤が整備されました。

---

## 2. CSS フォントプロパティ全景（CSS Fonts Module）

### 2.1 コアプロパティの体系

#### 1. `font-family`（フォントファミリ）
候補フォントを優先順位順に指定します。W3C は最終フォールバックとして **5 種類の総称ファミリ名（Generic Font Families）** を規定しています：
- `serif`（明朝・ローマンなどのセリフ体）
- `sans-serif`（ゴシック・サンセリフ体）
- `monospace`（等幅フォント）
- `cursive`（筆記体・草書体）
- `fantasy`（装飾体・ファンタジー体）

#### 2. `font-style`（フォントスタイル）
- `normal`：直立正体（Roman）
- `italic`：筆記体の骨格を持つ本来のイタリック体（True Italic）
- `oblique`：正体をアルゴリズムによって傾斜させた機械的斜体（Fake Italic）

#### 3. `font-variant`（スモールキャピタル等）
- `normal` / `small-caps`（小文字の高さに合わせた小型大写字母）

#### 4. `font-weight`（フォントウェイト）
100（極細）から 900（極太）までの 9 段階の数値、または `normal` (400), `bold` (700), `bolder`, `lighter`。

#### 5. `font-stretch`（幅の伸縮比率）
`normal`, `ultra-condensed` (50%) から `ultra-expanded` (200%) までの 9 段階。

#### 6. `font-size`（フォントサイズ）
絶対キーワード（`medium`, `large` 等）、相対キーワード、または各種単位（`px`, `pt`, `em`, `rem`, `ex`）。

#### 7. PANOSE-1 分類体系とフォント記述子
CSS は Hewlett-Packard 社の **PANOSE-1** 分類コード（10桁の数字配列）をサポートしており、スタイルの一致度をユークリッド距離で定量計算して最も近いフォントへフォールバックします。

#### 8. `unicode-range` によるサブセット分割
単一コードポイント（`U+26`）、連続範囲（`U+0000-00FF`）、ワイルドカード（`U+4??`）を指定し、必要な文字を含むファイルのみをオンデマンドで分割ダウンロードさせることが可能です。

---

### 2.2 `font-size-adjust`：x-ハイトの補正と可読性制御

同一の `font-size: 16px` を指定しても、フォントによって実際の小文字の見かけの大きさが大きく異なる現象が生じます。

![フォントごとの x-ハイト比率の比較](/images/fonts-encodings/fig10-1.png)
*図 10-1：数種類の代表的フォントにおける x-ハイト（小文字の高さとボディサイズの比率）の比較。*

#### アスペクト値（Aspect Value）の定義
字面の視覚的な大きさは、小文字 `x` の高さの比率である**アスペクト値（$a$）**によって決定されます：

$$a = \frac{\text{x-height}}{\text{font-size}}$$

- Verdana（$a \approx 0.58$）のようにアスペクト値が高いフォントは、低解像度ディスプレイでも抜群の可読性を誇ります。
- Times New Roman（$a \approx 0.46$）のようにアスペクト値が低いフォントは、フォールバック時に文字が小さく沈み込んでしまいます。

#### サイズ自動補正計算式
```css
p {
  font-family: Verdana, "Times New Roman", serif;
  font-size: 14px;
  font-size-adjust: 0.58;
}
```
フォールバック先のフォント固有のアスペクト値が $a'$ である場合、ブラウザは以下の数式に基づいて実際の計算フォントサイズ $c$ を自動拡大補正します：

$$c = \left(\frac{a}{a'}\right) \times s$$

これにより、どの代替フォントが適用されても小文字の絶対的視覚サイズが一定に保たれます。

---

### 2.3 フォントマッチングアルゴリズム（Font Matching Algorithm）

1. **フォントデータベース構築**：ローカルフォントと `@font-face` 登録フォントを統合索引化。
2. **プロパティ抽出**：対象要素の `font-family` リストと各属性を解決。
3. **ファミリ名走査**：リスト順に合致するファミリを検索。
4. **属性距離計算**：`font-stretch` $\to$ `font-style` $\to$ `font-weight` の優先順位で最近傍のウェイト・スタイルを選択。
5. **文字グリフ網羅性の検査（Glyph Coverage Check）**：**文字単位でグリフの存在を検証**。一部の文字が欠けている場合、その文字のみ後続のフォントファミリから探す。
6. **システムフォールバック**：全リストで文字が見つからない場合、OS のデフォルトフォールバックを呼び出し、最終的に「豆腐（Missing Glyph）」記号を描画。

---

## 3. `@font-face` 規則と初期 Web フォント技術の先駆者たち

### 3.1 Bitstream TrueDoc と PFR 形式

![WebFont Wizard 操作画面](/images/fonts-encodings/fig10-2.png)
*図 10-2：Bitstream TrueDoc の WebFont Wizard による PFR フォント生成ウィザード。*

- **CSR（Character Shape Recorder）**：HTML を解析し、実際に使用された文字のアウトラインのみを高圧縮な **PFR（Portable Font Resource, `.pfr`）** バイナリに記録。
- **CSP（Character Shape Player）**：Netscape Navigator 4.0 にネイティブ統合されたラスタライズエンジン。

### 3.2 Microsoft WEFT と Embedded OpenType（EOT）

![WEFT フォントデータベース画面](/images/fonts-encodings/fig10-3.png)
*図 10-3：Microsoft WEFT のフォントデータベース画面。埋め込み許諾属性（fsType）を表示。*

![WEFT EOT 作成ウィザード](/images/fonts-encodings/fig10-4.png)
*図 10-4：WEFT における EOT 作成ウィザードの進行画面。*

![WEFT 生成メインウィンドウ](/images/fonts-encodings/fig10-5.png)
*図 10-5：WEFT の EOT 圧縮生成バッチ制御ウィンドウ。*

- **ライセンス遵守**：`OS/2` テーブルの `fsType` を厳格に判定。
- **ルート文字列ドメイン拘束（Root String URL Binding）**：Web サイトのドメイン名を EOT ヘッダに暗号化署名として埋め込み、不正な直リンクやローカル抽出を防止。
- **MicroType Express**：Agfa 社の差分エントロピー圧縮技術により TTF を 50〜70% 圧縮。

### 3.3 動的グリフサーバ：em2 Solutions の GlyphGate

![GlyphGate サーバフォント一覧](/images/fonts-encodings/fig10-6.png)
*図 10-6：GlyphGate がサーバ上で検出・登録した高品質フォント一覧。*

![GlyphGate Palatino Linotype 描画画面](/images/fonts-encodings/fig10-7.png)
*図 10-7：GlyphGate により動的生成・描画された Palatino Linotype の拡張グリフ。*

数万文字を含む CJK 大規模文字セットに対し、クライアントが必要とする文字のみをサーバ側でリアルタイムに抽出し、数十バイトの動的ストリームとしてオンデマンド配信する画期的なアーキテクチャを実現しました。

---

## 4. SVG（Scalable Vector Graphics）と SVG フォント体系

### 4.1 SVG 独立フォント構文

SVG は XML テキストとしてフォント構造全体を記述する仕様を内包していました：
- `<font>`：フォントルート要素
- `<font-face>`：メトリクス情報
- `<missing-glyph>`：未収録文字の代替枠
- `<glyph>`：文字のベクターパスデータ（`d` 属性）
- `<hkern>` / `<vkern>`：水平・垂直カーニング対

### 4.2 SVG フォントメトリクスと座標系

![SVG font-face メトリクス属性の構造図解](/images/fonts-encodings/fig10-8.png)
*図 10-8：`<font-face>` 要素の主要メトリクス属性（ascent, descent, cap-height, x-height, baseline 等）の幾何学的定義。*

![SVG 水平および垂直組版の送り座標](/images/fonts-encodings/fig10-9.png)
*図 10-9：水平組版（horiz-adv-x）および垂直組版（vert-adv-y）における原点と送り幅ベクトル。*

### 4.3 実例：Le Monde Livre の大文字 'R'

![Le Monde Livre の大文字 R ベクター輪郭](/images/fonts-encodings/fig10-10.png)
*図 10-10：フランスの名作フォント Le Monde Livre における大文字「R」のベクター輪郭と制御点。*

```xml
<glyph unicode="R" glyph-name="R" horiz-adv-x="689"
  d="M 520 -15
     C 496 29 459 76 382 173
     C 305 270 244 350 200 405
     L 200 480
     C 260 485 315 500 365 525
     C 415 550 455 585 480 625
     C 505 665 515 710 515 760
     C 515 825 490 880 440 925
     C 390 970 310 995 200 1000
     L 50 1000
     L 50 0
     L 130 0
     L 130 440
     L 190 440
     C 245 440 310 350 400 230
     C 490 110 540 30 550 0
     L 660 0
     C 630 30 580 80 520 -15 Z
     M 130 520
     L 130 920
     L 190 920
     C 260 920 310 900 340 870
     C 370 840 385 790 385 730
     C 385 660 365 605 325 565
     C 285 525 220 520 130 520 Z" />
```

外側の輪郭と内側の空洞（Counter）が 3 次ベジェ曲線（`C`）と直線（`L`）で精緻に描かれ、非ゼロ巻き数規則（Non-zero Winding Rule）により充填されます。

---

## 5. Web フォント規格統一の終着点：WOFF と現代組版

- **WOFF 1.0 (2010)**：SFNT（TrueType/OpenType）テーブルを zlib で圧縮し、XML メタデータを同封するオープン規格。
- **WOFF 2.0 (2015)**：Google Brotli 圧縮を採用し、`glyf` テーブルの座標・フラグを分離再構成して極限までサイズを圧縮。
- **`font-display` プロパティ**：`auto`, `block`, `swap`, `fallback`, `optional` の各モードにより、FOIT（不可視テキストの空白）や FOUT（スタイリング前のチラつき）を完全に制御可能に。

今日、WOFF2 と可変フォント（Variable Fonts）技術の確立により、Web ブラウザは印刷技術数百年分のタイポグラフィの遺産を完全な自由度で描画できるようになりました。
"""

with open('docs/ja/fonts-encodings/chapter-10.md', 'w', encoding='utf-8') as f:
    f.write(ja_text)
print(f"Wrote docs/ja/fonts-encodings/chapter-10.md ({len(ja_text)} chars)")
