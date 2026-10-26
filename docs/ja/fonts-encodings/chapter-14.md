---
title: "第 14 章：フォントの拡張：高度な組版機能"
description: "OpenType および AAT の高度な組版機能の詳細解析：AFDKO 特性構文仕様、Microsoft VOLT エンジニアリング実践、Apple Advanced Typography (AAT) 有限状態オートマトン、GSUB/GPOS ルックアップテーブル体系。"
---

# 第14章：フォントの拡張：高度な組版機能

*翻訳者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

### Chapter 14: Enriching Fonts: Advanced Typography

本章のタイトルが指す「高度な組版機能（Advanced Typography）」とは、マイクロソフト、アドビ、およびアップルが基本の TrueType フォーマットの上に導入した拡張レイアウトテーブルシステム——すなわち現代のデジタルタイポグラフィの二大支柱である **OpenType** と **Apple Advanced Typography（AAT）** を指しています。

伝統的な活版印刷時代において、組版工は多言語混植、アラビア文字の接続変形、南アジア諸文字の子音結合、欧文活字の合字（リガチャ）、スモールキャピタル、オールドスタイル数字、文脈に応じた長短「s」の使い分けなど、長年の職人芸と手動のスペーサー調整に依存していました。初期のパーソナルコンピュータ時代では、PostScript Type 1 や初期の TrueType フォントは単純な「文字コードからグリフ外観への静的射影表（`cmap`）」に過ぎず、複雑な表記体系は OS や DTP ソフトの外付けエンジンに頼らざるを得ませんでした。

OpenType と AAT の革新性は、**テキスト動的組版の「インテリジェントなルール」をフォントファイル自体の内部に直接カプセル化したこと**にあります。テキスト整形エンジン（Shaping Engine、HarfBuzz、DirectWrite、CoreText など）は、各言語の規則をハードコードする必要がなくなり、フォント内部のレイアウトテーブルを解釈することで、書体設計者が意図した通りの字形変形、合字合成、微細な二次元位置調整を完全に制御できるようになりました。

---

## 1. 組版の知能化とパラダイムシフト（Introduction）

### 1.1 文字からグリフへ：テキスト整形の動的変換

現代のデジタルテキスト処理の中核理論は、**文字（Character）** と **グリフ（Glyph）** の厳密な分離に立脚しています：
* **文字**：コンピュータ情報処理における抽象的な意味論的最小単位であり、Unicode スカラー値（Code Point）によって一意に識別されます（「何という文字か」）；
* **グリフ**：スクリーンピクセルや印刷紙上に描画される具体的な視覚的物理形態であり、ベジェ曲線輪郭、ヒンティング命令、空間メトリクスから構成されます（「どのように表示されるか」）。

組版エンジンが論理コードポイントを最終的なスクリーン上の幾何トポロジー流に変換する数学的パイプラインは、以下の4段階の変換として定式化されます：

$$\text{Unicode Code Points} \xrightarrow{\quad\text{cmap マッピング}\quad} \text{Glyph IDs} \xrightarrow{\quad\text{GSUB 置換}\quad} \text{Glyph IDs} \xrightarrow{\quad\text{GPOS 配置}\quad} \text{Positioned Glyphs}$$

---

### 1.2 高度な組版の双翼：グリフ置換（GSUB）と幾何配置（GPOS）

OpenType アーキテクチャにおいて、この動的組版の心臓部は、形態変換を司る **`GSUB`（Glyph Substitution Table）** と、微小空間位置を司る **`GPOS`（Glyph Positioning Table）** の二大バイナリテーブルに完全に分離されています。

#### 1. グリフ置換の主要形態（GSUB）
1. **単一置換（Single Substitution, Type 1）**：1つのグリフを別の1つのグリフに等価置換（例：小文字からスモールキャピタル `a` $\to$ `a.sc`、等幅数字 `tnum`、オールドスタイル数字 `onum`）；
2. **複数置換（Multiple Substitution, Type 2）**：1つのグリフを2つ以上のグリフシーケンスに分解（例：合字 `ffi` の分解）；
3. **代替置換（Alternate Substitution, Type 3）**：1つのグリフに対して複数の意匠候補を提供し、ユーザーが対話的に選択可能にする（例：スワッシュ字形 `swsh`、装飾記号 `ornm`、Zapfino の9種類の「d」）；
4. **合字置換（Ligature Substitution, Type 4）**：指定された連続グリフシーケンスを1つの合字グリフに統合（例：`f` + `i` $\to$ `fi`、歴史的合字 `dlig`、アラビア文字の結合）；
5. **文脈依存置換（Contextual Substitution, Type 5）**：前後の文脈グリフが存在する場合にのみ発動する置換；
6. **連鎖文脈依存置換（Chained Contextual Substitution, Type 6）**：文脈を「後方参照（Backtrack）」「入力照合（Match）」「前方参照（Lookahead）」の3領域に厳密に分離し、柔軟な多段置換を実現；
7. **逆方向連鎖文脈置換（Reverse Chaining Contextual Single Substitution, Type 8）**：ウルドゥー語（Nastaliq）などのために右から左への逆方向走査で評価を行う特殊置換。

#### 2. グリフ微小幾何配置の主要形態（GPOS）
各グリフの最終的な空間配置は、以下の4要素の値レコード（Value Record）によって定義されます：

$$\langle xPlacement \quad yPlacement \quad xAdvance \quad yAdvance \rangle$$

1. **単一調整（Single Adjustment, Type 1）**：個別グリフの位置や送り幅の微調整（例：オールキャップス時の括弧の垂直引き上げ `cpsp`）；
2. **ペア調整（Pair Adjustment / Kerning, Type 2）**：隣接する2つのグリフ間の空隙調整（カーニング `kern`）；
3. **筆記体接続（Cursive Attachment, Type 3）**：各グリフの接続入口（Entry）と出口（Exit）にアンカーを配置し、滑らかな接続を実現（アラビア文字・波斯折体）；
4. **ベースへのマーク配置（Mark-to-Base, Type 4）**：基本文字のアンカーにアクセント記号や母音記号を吸着結合；
5. **合字へのマーク配置（Mark-to-Ligature, Type 5）**：合字の内部コンポーネントごとに独立したアンカーを定義；
6. **マークへのマーク配置（Mark-to-Mark, Type 6）**：多重アクセント記号の垂直・水平多層スタック配置（ベトナム語など）。

---

### 1.3 OpenType レイアウトテーブルのバイナリ構造

* **カバレッジテーブル（Coverage Tables）**：
  * **Format 1**：昇順ソートされたグリフ ID 配列による二分探索；
  * **Format 2**：連続区間範囲（`RangeRecord`）による効率的な圧縮。
* **クラス定義テーブル（ClassDef Tables）**：クラスベースのカーニングや文脈置換のためのグリフ分類整数マッピング。
* **`GDEF`（Glyph Definition）**：Base、Ligature、Mark、Component の分類、キャレット位置（`LigCaretList`）の管理。
* **`BASE`**：ラテン基線、表意文字中央基線、サンスクリット懸垂基線など、多言語混植時の垂直ベースライン揃え。
* **`JSTF`（Justification）**：アラビア文字カシーダ（伸展線）や語間調整の多段階優先順位パイプライン。

---

## 2. FontLab における OpenType テーブル管理と AFDKO 構文

FontLab Studio は、アドビが開発した **AFDKO（Adobe Font Development Kit for OpenType）** 構文コンパイラを統合し、テキストコードベースでの OpenType 開発を確立しました。

### 2.1 AFDKO の構文仕様

```fea
languagesystem DFLT dflt;
languagesystem latn dflt;

# クラス定義
@UPPER = [A-Z];
@LOWER = [a-z];
@SC = [a.sc-z.sc];

# 単一置換
feature smcp {
    sub @LOWER by @SC;
} smcp;

# 合字置換（最長一致の優先順序）
feature liga {
    sub f f i by f_f_i;
    sub f i by f_i;
    sub f l by f_l;
} liga;

# 文脈置換と ignore 構文（TEX ロゴの置換例）
feature liga {
    ignore sub [A-Z] T' E' X', T' E' X' [A-Z];
    sub T' E' X' by T_e_X;
} liga;

# GPOS カーニング
feature kern {
    pos T -50 o -20;
    pos @CAPS_T @LOWER_O -80;
} kern;

# 光学サイズ特性
feature size {
    parameters 10.0 0 8.0 11.9;
    featureNames {
        name 3 1 0x0409 "Regular (10pt Text)";
        name 3 1 0x0411 "レギュラー (10pt 本文)";
    };
} size;
```

::: tip FontLab 4/5 における OpenType 機能編集ウィンドウ（Figure 14-1）
![FontLab 4/5 における OpenType 機能編集ウィンドウ（Figure 14-1）](/images/fonts-encodings/fig14-1.png)
*FontLab 4/5 における OpenType 機能編集ウィンドウ（Figure 14-1）*
:::

*図 14-1：FontLab の OpenType パネル。左側に機能タグリスト、右上に AFDKO コード編集画面、右下にコンパイルログが表示される。*

::: tip FontLab 機能管理およびクラス管理詳細ウィンドウ（Figure 14-2, 14-3, 14-4）
![FontLab 詳細機能ウィンドウ（Figure 14-2）](/images/fonts-encodings/fig14-2.png)
*FontLab 詳細機能ウィンドウ（Figure 14-2）*
:::

*図 14-2：FontLab の OpenType 機能管理ウィンドウ。機能のスクリプト依存性とルックアップの階層関係。*

::: tip FontLab カーニングクラスタブ（Figure 14-3）
![FontLab カーニングクラスタブ（Figure 14-3）](/images/fonts-encodings/fig14-3.png)
*FontLab カーニングクラスタブ（Figure 14-3）*
:::

*図 14-3：FontLab のクラスベースカーニング編集タブ。*

::: tip FontLab グリフクラス定義タブ（Figure 14-4）
![FontLab グリフクラス定義タブ（Figure 14-4）](/images/fonts-encodings/fig14-4.png)
*FontLab グリフクラス定義タブ（Figure 14-4）*
:::

*図 14-4：FontLab の Classes タブ。同等の輪郭特性を持つ文字群をクラスとして一括管理。*

::: tip FontLab リアルタイム組版プレビューパネル（Figure 14-5）
![FontLab リアルタイム組版プレビューパネル（Figure 14-5）](/images/fonts-encodings/fig14-5.png)
*FontLab リアルタイム組版プレビューパネル（Figure 14-5）*
:::

*図 14-5：FontLab のプレビューパネル。テキストを入力し、各種 OpenType 機能のチェックボックスをオン/オフしてレンダリング結果を検証できる。*

---

## 3. マイクロソフト VOLT による視覚的 OpenType 構築

マイクロソフトの **VOLT（Visual OpenType Layout Tool）** は、GUI ベースで複雑な表記体系（アラビア文字、ウルドゥー語、南アジア諸文字）のフォントを構築するための標準開発環境です。

### 3.1 VOLT の構造とプライベートテーブル

VOLT は `TSVT`、`TSVC`、`TSVG`、`TSVP` というプライベートテーブル内に編集データを保持し、コンパイル時に標準の `GSUB`/`GPOS`/`GDEF` に焼き付けます。

::: tip マイクロソフト VOLT プロジェクトメインウィンドウ（Figure 14-6）
![マイクロソフト VOLT プロジェクトメインウィンドウ（Figure 14-6）](/images/fonts-encodings/fig14-6.png)
*マイクロソフト VOLT プロジェクトメインウィンドウ（Figure 14-6）*
:::

*図 14-6：VOLT のプロジェクトウィンドウ。Glyphs、Classes、Features、Lookups のトポロジーが表示される。*

::: tip VOLT の置換ルックアップ編集ウィンドウ（Figure 14-7）
![VOLT の置換ルックアップ編集ウィンドウ（Figure 14-7）](/images/fonts-encodings/fig14-7.png)
*VOLT の置換ルックアップ編集ウィンドウ（Figure 14-7）*
:::

*図 14-7：VOLT の置換編集画面。直感的なグリッドと矢印構文による置換マッピング。*

::: tip VOLT の筆記体アンカーおよび幾何配置ウィンドウ（Figure 14-8）
![VOLT の筆記体アンカーおよび幾何配置ウィンドウ（Figure 14-8）](/images/fonts-encodings/fig14-8.png)
*VOLT の筆記体アンカーおよび幾何配置ウィンドウ（Figure 14-8）*
:::

*図 14-8：VOLT の配置編集画面。Entry/Exit アンカーを対話的に操作し、文字間の滑らかな接続を確認。*

::: tip VOLT のインタラクティブ校正ウィンドウ（Figure 14-9）
![VOLT のインタラクティブ校正ウィンドウ（Figure 14-9）](/images/fonts-encodings/fig14-9.png)
*VOLT のインタラクティブ校正ウィンドウ（Figure 14-9）*
:::

*図 14-9：VOLT の校正ウィンドウ（Proofing Window）。複雑な文字列に対して、どのルックアップがどの順序で適用されたかの実行トレースを1ステップずつ追跡可能。*

---

## 4. FontForge における OpenType テーブル管理

FontForge では `Element > Font Info > Lookups` から GSUB および GPOS テーブルを直接編集できます。

::: tip FontForge におけるアンカーとアンカークラス編集（Figure 14-10）
![FontForge におけるアンカーとアンカークラス編集（Figure 14-10）](/images/fonts-encodings/fig14-10.png)
*FontForge におけるアンカーとアンカークラス編集（Figure 14-10）*
:::

*図 14-10：FontForge のアンカー定義画面。ベースグリフのアンカーとマーク記号のアンカーの対応関係。*

::: tip FontForge 単一置換および配置ウィンドウ（Figure 14-11, 14-12）
![FontForge 単一置換ウィンドウ（Figure 14-11）](/images/fonts-encodings/fig14-11.png)
*FontForge 単一置換ウィンドウ（Figure 14-11）*
:::

*図 14-11：FontForge の非文脈置換ウィンドウ。*

::: tip FontForge 単一およびペア配置ウィンドウ（Figure 14-12）
![FontForge 単一およびペア配置ウィンドウ（Figure 14-12）](/images/fonts-encodings/fig14-12.png)
*FontForge 単一およびペア配置ウィンドウ（Figure 14-12）*
:::

*図 14-12：FontForge の単一配置（左）とペアカーニング（右）画面。*

::: tip FontForge 連鎖文脈置換ウィザードの4ステップ（Figure 14-13）
![FontForge 連鎖文脈置換ウィザードの4ステップ（Figure 14-13）](/images/fonts-encodings/fig14-13.png)
*FontForge 連鎖文脈置換ウィザードの4ステップ（Figure 14-13）*
:::

*図 14-13：FontForge の連鎖文脈置換ウィザード：(a) 機能タグ選択、(b) カバレッジ形式、(c) 後方・照合・前方クラスシーケンス定義、(d) ネストするサブルックアップの指定。*

---

## 5. FontForge における Apple Advanced Typography（AAT）有限状態機械の構築

### 5.1 AAT と OpenType の計算理論的対比

* **OpenType**：宣言的なグラフ書き換えルール群。エンジンがテキスト全体を何度も複数パス走査するため、計算量は $O(K \cdot N)$；
* **AAT**：**決定性有限状態トランスデューサ（DFA / FST）**。すべての文脈ルールが事前に単一の二次元状態遷移表に最適化・統合されており、テキストを先頭から末尾まで一度だけ走査する**シングルパス走査**で実行され、時間計算量は物理的限界の $O(N)$ を達成します。

$$M = \langle Q, \, \Sigma, \, \Gamma, \, \delta, \, q_0, \, F \rangle$$

::: tip AAT 機能およびセレクタの多言語名称編集（Figure 14-14）
![AAT 機能およびセレクタの多言語名称編集（Figure 14-14）](/images/fonts-encodings/fig14-14.png)
*AAT 機能およびセレクタの多言語名称編集（Figure 14-14）*
:::

*図 14-14：FontForge での AAT 機能名編集。`feat` テーブル内に多言語のローカライズ表示名が格納される。*

::: tip AAT 状態機械クラス表と状態遷移マトリクスウィンドウ（Figure 14-15）
![AAT 状態機械クラス表と状態遷移マトリクスウィンドウ（Figure 14-15）](/images/fonts-encodings/fig14-15.png)
*AAT 状態機械クラス表と状態遷移マトリクスウィンドウ（Figure 14-15）*
:::

*図 14-15：FontForge の AAT 状態機械編集画面。(a) 入力クラス表、(b) 状態遷移マトリクス。各行がマシン状態、各列が入力クラスを表し、セル内に遷移先状態と実行アクションが記録される。*

#### AAT の4大状態機械：
1. **グリフ並べ替え（Glyph Rearrangement）**：インディック系文字などの子音と母音の順序入れ替え；
2. **文脈置換（Contextual Substitution）**：対角線分数（`1/2`）の分子・分数線・分母への三段置換；
3. **グリフ挿入（Glyph Insertion）**：アラビア文字均等割り付けのためのカシーダ（伸展線）動的挿入；
4. **文脈カーニング（Contextual Kerning / `kerx`）**：最大8文字のスタック保持による「S.A.V.」などの句読点を挟む複数文字一括カーニング。

---

## 6. 結びと現代の組版技術の展望

今日、OpenType は Adobe と Microsoft の主導により世界標準の地位を確立し、AAT は Apple プラットフォームにおいて極めて洗練された高速処理の規範として生き続けています。さらに、現代のオープンソース整形エンジン **HarfBuzz** は両者の長所を統合し、全プラットフォームの基盤となっています。また、OpenType 1.8 で登場した**バリアブルフォント（Variable Fonts）**は、`FeatureVariations` テーブルを通じて、デザイン軸のパラメータに応じて字形置換を連続的に切り替える新たな地平を切り拓いています。
