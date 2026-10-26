---
title: "第14章：高度組版体系：OpenType と AAT 機能の実践"
description: "完全無削除 1:1 学術全訳：複雑文字体系の組版課題（デーヴァナーガリー文字の結合子分離と母音記号前置リオーダー、アラビア文字の連筆形態素と双方向組版、西欧の歴史的合字と真のスモールキャピタル）；OpenType レイアウト構造（GSUB 置換テーブル1〜8型、GPOS 位置指定テーブル1〜6型、標準機能タグ Feature Tags）；FontLab における Adobe 機能定義言語（AFDKO .fea 構文、文脈依存規則、ネストされたルックアップ）；マイクロソフト VOLT による工業的ビジュアル開発（プロジェクト管理、置換・位置指定ウィンドウ、Proofing 単歩トレース打鍵検証）；FontForge での高度組版管理（アンカークラス、連鎖文脈ウィザード）；アップル高度組版（AAT）有限状態オートマトン（FSM、morx テーブル、状態遷移マトリクス、マークとスタック操作）。"
---

# 第14章：高度組版体系：OpenType と AAT 機能の実践

**ヤニス・ハラランブス（Yannis Haralambous, Ph.D.）著**  
*『Fonts & Encodings』第 549–598 頁より*

*訳者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

# 導言：複雑組版の世紀の挑戦

本章の表題は、デジタルフォント技術の王冠に輝く至宝——**OpenType** およびアップル **AAT**（Apple Advanced Typography）の「**高度組版機能**」（Advanced Typographic Features）を直接の主題としている。

活字印刷と初期のデスクトップパブリッシング（DTP）の長き歴史において、組版システムは「1つの入力文字コードに対して、1つの固定された物理活字を割り当てる」という単純な前提に束縛されてきた。しかしながら、人類文明が育んできた広大な文字体系の世界において、このような単純な機械的一対一写像は、複雑文字体系（Complex Scripts）の前に脆くも破綻をきたす：

1. **インド系文字（デーヴァナーガリー文字など）**：サンスクリット語やヒンディー語においては、子音同士が融合して複雑な結合子（Conjuncts）を形成する。さらに驚くべきことに、短母音記号「i-matra」（ि）は論理コード上は子音の後に打ち込まれるにもかかわらず、物理印刷においては**視覚的に前方の子音結合クラスターを飛び越えて、単語の先頭左端へと回り込んで覆いかぶさらなければならない！**
2. **アラビア文字体系**：アラビア文字は生来の連筆草書体系である。各文字は、語頭形（Initial）、語中形（Medial）、語末形（Final）、そして独立形（Isolated）においてまったく異なる字形骨格を取らなければならず、さらに上下の発音母音記号（タシュキール）は文字の高さに応じて動的に浮動整列しなければならない。
3. **ヘブライ文字および東南アジア文字**：ヘブライ文字の母音記号（ニクード）や聖書詠唱記号はインクが重複しないよう精密に積み重なる必要があり、タイ文字やビルマ文字では多層的な垂直スタッキングが要求される。
4. **西欧古典組版の極致**：規則的に見えるラテン文字においても、格調高き書籍組版は極めて精緻な動的変換を要求する：標準合字（$\text{fi}, \text{fl}, \text{ffi}, \text{ffl}$）、歴史的稀少合字（$\text{ct}, \text{st}, \text{long-s}$）、真のスモールキャピタル（Small Capitals）、上付き・下付き数字、プロポーショナル数字、表組み用等幅数字、古典的なオールドスタイル数字（Old-Style Figures）、そして分数（Fractions）の自動合成である。

統一された単一のフォントファイル内部にこれら高度な言語的知性を包含するため、現代のタイポグラフィ工学は2大金字塔を生み出した：マイクロソフトと Adobe が主導した **OpenType レイアウト体系**、そしてアップルが独自に切り拓いた **AAT 有限状態オートマトン体系** である。

---

# OpenType レイアウト構造の全景

OpenType の高度組版能力は、主として2つの根幹テーブルによって支えられている：**GSUB**（Glyph Substitution Table，字形置換テーブル）および **GPOS**（Glyph Positioning Table，字形位置指定テーブル）である。

## 1. GSUB：字形置換の8大ルックアップ種別（Lookups）

字形置換テーブルの使命は、前後の文脈規則に従い、テキストストリーム内の1つまたは複数のグリフコード（GID）を、フォント内の別の1つまたは複数のグリフへと動的にすり替えることである：

* **単一グリフ置換（Single Substitution, Type 1）**：1対1の置換。小文字「a」をスモールキャピタル「ᴀ」へと変換する処理（`smcp` 特性）や、大文字用の高位括弧への置換。
* **複数グリフ置換（Multiple Substitution, Type 2）**：1対多の分解。結合リガチャを構成要素の独立した子音列へと分解する。
* **選択的グリフ置換（Alternate Substitution, Type 3）**：1対多の対話的選択。同一文字に対してデザインされた複数の華麗なスワッシュ（Swash）花体字形などを、ユーザがDTP画面上で選択できるようにする。
* **合字置換（Ligature Substitution, Type 4）**：多対1の融合。連続する文字ストリーム（$f + i \to \text{fi}$ など）を単一の専用リガチャグリフへと統合する。
* **文脈依存置換（Contextual Substitution, Type 5）**：特定の前後関係のもとでのみ置換を発動する。
* **連鎖文脈置換（Chained Contextual Substitution, Type 6）**：最高峰の組版知性ツール。環境を**後方参照（Backtrack）**、**入力一致（Input）**、**前方参照（Lookahead）**の3つの独立区間に分解し、すべてが合致した際にのみ中央の入力グリフに置換を適用する。
* **拡張置換（Extension Substitution, Type 7）**：16ビットのオフセット限界（64KB制約）を突破するための長距離ジャンプ機構。
* **逆方向連鎖文脈置換（Reverse Chaining Contextual Single Substitution, Type 8）**：右から左へのテキストストリームに対応するため、逆順で文脈を走査して単一置換を適用する。

## 2. GPOS：字形位置指定の6大ルックアップ種別

GPOS はグリフの ID 自体は変更せず、幾何学的座標オフセット（$X$ 移動量、$Y$ 移動量、水平アドバンス増分 $\Delta X$、垂直アドバンス増分 $\Delta Y$）をナノメートル単位で制御する：

* **単一字形位置調整（Single Adjustment, Type 1）**：オールキャップス組版時に約物（ピリオドやハイフン）を大文字の中心線へと持ち上げる。
* **ペア位置調整・カーニング（Pair Adjustment / Kerning, Type 2）**：「AV」「To」などの文字間の空隙を詰める。
* **草書連筆アンカー配置（Cursive Attachment, Type 3）**：連続する手書き風文字の「入口アンカー（Entry Anchor）」と「出口アンカー（Exit Anchor）」を剛体吸着させ、滑らかな筆の連続性を保証する。
* **ベース記号吸着（Mark-to-Base Attachment, Type 4）**：基底文字（Base）とダイアクリティカルマーク（Mark）にそれぞれアンカーを設定し、実行時に両者を重ね合わせる。これにより、数千もの合成済み文字を個別に制作する必要がなくなる。
* **合字記号吸着（Mark-to-Ligature Attachment, Type 5）**：リガチャを構成する個々の文字の頭上に正確にアクセントを吸着させる。
* **多重記号吸着（Mark-to-Mark Attachment, Type 6）**：アクセント記号の上にさらに声調記号を多重に積み重ねる。

## 3. 標準4文字機能タグ（Feature Tags）

* `liga`（標準合字）：基本合字（$\text{fi}, \text{fl}$）；
* `dlig`（任意合字）：歴史的・装飾的合字（$\text{ct}, \text{st}$）；
* `smcp`：小文字から真のスモールキャピタルへの変換；
* `c2sc`：大文字からスモールキャピタルへの変換；
* `lnum` / `onum`：ライニング数字 / オールドスタイル数字；
* `pnum` / `tnum`：プロポーショナル数字 / 表組み等幅数字；
* `frac`：斜線分数の自動合成（$1/2 \to \frac{1}{2}$）；
* `hist`：歴史的異体字（長音の s など）；
* `salt` / `swsh`：スタイルセット・スワッシュ字形；
* `init`, `medi`, `fina`, `isol`：アラビア文字の各語位形態素；
* `size`：光学サイズ推奨値のメタデータ。

---

# FontLab における OpenType テーブルと AFDKO 構文

FontLab は Adobe の **AFDKO**（Adobe Font Development Kit for OpenType）コンパイラを統合し、業界標準の機能定義言語（`.fea` 構文）をサポートする（図 14-1, 14-2）：

::: tip 図 14-1：FontLab の OpenType 機能定義エディタウィンドウ
![図 14-1：FontLab の OpenType 機能定義エディタウィンドウ](/images/fonts-encodings/fig14-1.png)
*図 14-1：FontLab の OpenType 機能定義エディタウィンドウ。*
:::

::: tip 図 14-2：FontLab の OpenType コンパイル・構文診断パネル
![図 14-2：FontLab の OpenType コンパイル・構文診断パネル](/images/fonts-encodings/fig14-2.png)
*図 14-2：FontLab の OpenType コンパイル・構文診断パネル。*
:::

```fea
@UPPERCASE = [A-Z];
languagesystem DFLT dflt;
languagesystem latn DFLT;

feature liga {
    sub f i by f_i;
    sub f l by f_l;
} liga;

# 文脈規則：単独の 'T E X' を合体させ、'TEXAS' などの単語内では合体を抑止する
feature dlig {
    ignore sub [A-Z] T' E' X' ;
    ignore sub T' E' X' [A-Z] ;
    sub T' E' X' by T_e_X;
} dlig;
```

FontLab のプレビューパネル（図 14-5）により、機能をリアルタイムに検証できる。

::: tip 図 14-5：FontLab のプレビューパネル（Preview Panel）
![図 14-5：FontLab のプレビューパネル](/images/fonts-encodings/fig14-5.png)
*図 14-5：FontLab のプレビューパネル。*
:::

---

# マイクロソフト VOLT によるビジュアル工学開発

マイクロソフトの **VOLT**（**Visual OpenType Layout Tool**）は、アラビア文字や南アジア文字の大規模開発における世界標準ツールである：

::: tip 図 14-6：マイクロソフト VOLT のプロジェクト管理メインウィンドウ
![図 14-6：マイクロソフト VOLT のプロジェクト管理メインウィンドウ](/images/fonts-encodings/fig14-6.png)
*図 14-6：マイクロソフト VOLT のプロジェクト管理メインウィンドウ。*
:::

* **プロジェクト管理（図 14-6）**：文字体系、言語、機能、Lookups を階層管理。
* **置換編集（図 14-7）**：To/By、Context/Lookahead の視覚的マッピング。
* **位置指定・アンカー配置（図 14-8）**：キャンバス上でマウスを用いて記号の吸着アンカーを直感的に配置。
* **Proofing ウィンドウ（図 14-9）**：入力テキストに対して、どの Lookup がどの順序で適用されたかをフレーム単位で追跡・再生できる。

::: tip 図 14-7：VOLT の字形置換編集画面
![図 14-7：VOLT の字形置換編集画面](/images/fonts-encodings/fig14-7.png)
*図 14-7：VOLT の字形置換編集画面。*
:::

::: tip 図 14-8：VOLT の記号吸着アンカー配置画面
![図 14-8：VOLT の記号吸着アンカー配置画面](/images/fonts-encodings/fig14-8.png)
*図 14-8：VOLT の記号吸着アンカー配置画面。*
:::

::: tip 図 14-9：VOLT の打鍵検証・組版テスト台（Proofing Window）
![図 14-9：VOLT の打鍵検証・組版テスト台](/images/fonts-encodings/fig14-9.png)
*図 14-9：VOLT の打鍵検証・組版テスト台。*
:::

---

# FontForge における高度組版管理

FontForge は、直感的なダイアログによって OpenType 機能を管理する：
* **アンカークラス（図 14-10）**：基底文字と記号のアンカー定義；
* **単一置換・ペア位置指定（図 14-11, 14-12）**；
* **連鎖文脈置換ウィザード（図 14-13 [a]–[d]）**：4段階のウィザード形式で複雑な文脈テーブルを構築。

::: tip 図 14-10：FontForge のアンカークラス設定パネル
![図 14-10：FontForge のアンカークラス設定パネル](/images/fonts-encodings/fig14-10.png)
*図 14-10：FontForge のアンカークラス設定パネル。*
:::

::: tip 図 14-11：FontForge の単一字形置換設定パネル
![図 14-11：FontForge の単一字形置換設定パネル](/images/fonts-encodings/fig14-11.png)
*図 14-11：FontForge の単一字形置換設定パネル。*
:::

::: tip 図 14-12：FontForge の単純位置調整およびカーニング設定画面
![図 14-12：FontForge の単純位置調整およびカーニング設定画面](/images/fonts-encodings/fig14-12.png)
*図 14-12：FontForge の単純位置調整およびカーニング設定画面。*
:::

::: tip 図 14-13：FontForge における連鎖文脈置換構築ウィザード（a〜d）
![図 14-13：FontForge における連鎖文脈置換構築ウィザード](/images/fonts-encodings/fig14-13.png)
*図 14-13：FontForge における連鎖文脈置換構築ウィザード。*
:::

---

# アップル高度組版（AAT）と有限状態オートマトン（FSM）

アップルの **AAT**（Apple Advanced Typography）は、理論計算機科学における**決定性有限状態オートマトン（DFA）**をフォント内部に直接埋め込むという、優美な設計思想を持つ（`morx`、`kerx`、`feat` テーブル）。

OpenType が文字列全体のバックトラック探索を必要とするのに対し、AAT は入力文字をイベントとして受け取り、状態遷移テーブルに従って定数時間 $O(1)$ で次々と状態を遷移させながら置換を実行する。

::: tip 図 14-14：FontForge における AAT 機能とセレクタ（Features and Selectors）の編集画面
![図 14-14：FontForge における AAT 機能とセレクタの編集画面](/images/fonts-encodings/fig14-14.png)
*図 14-14：FontForge における AAT 機能とセレクタの編集画面。*
:::

## 状態遷移マトリクスと実践例：自動分数変換器

AAT 状態機は、クラス分類テーブル（Class Table）と状態遷移マトリクス（State Transition Matrix）によって動作する。各セルには、**次の状態（Next State）**、**現在文字のマーク（Mark）**、**マーク済み文字の置換**、**現在文字の置換**、そして**スタックへのプッシュ（Push to Stack、最大8段階）**が記録される。

::: tip 図 14-15：FontForge における AAT 有限状態オートマトン遷移マトリクスの構成画面
![図 14-15：FontForge における AAT 有限状態オートマトン遷移マトリクスの構成画面](/images/fonts-encodings/fig14-15.png)
*図 14-15：FontForge における AAT 有限状態オートマトン遷移マトリクスの構成画面。*
:::

図 14-15 に示す自動分数変換オートマトン：
1. **初期状態（State 1）**：数字が入力されるとマークして **State 2（分子候補）**へ遷移。
2. **State 2**：数字が続く間はマークを保持；スラッシュ `/` が入力されると、マークされていた数字群を一括して**上付き分子数字**に置換し、スラッシュを**分数斜線記号**（Fraction Slash）に置換して **State 3（分母待ち）**へ遷移。
3. **State 3**：後続の数字を**下付き分母数字**へと即座に置換；非数字が来た時点で State 1 へ復帰完結する。

---

# 結語

単一文字の置換から多層連鎖文脈判定、浮動アンカーから有限状態オートマトンに至るまで、高度組版技術は冷厳なベジェ曲線の鋳型に深い言語学的知性を吹き込んだ。これらの精緻なルックアップと状態遷移マトリクスこそが、数世紀に及ぶ活字の物理的束縛を解き放ち、画面上の文字をして人間の思考の息吹とともに躍動せしめる真の原動力なのである。
