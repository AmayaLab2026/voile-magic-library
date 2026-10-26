---
title: "第14章：書体の深化：高度な組版技術体系"
description: "完全無削除学術訳：ヤニス・ハラランブス『Fonts & Encodings』第14章全文学術訳：高度な組版技術体系。Adobe OpenType 機能定義言語（AFDKO Feature File Syntax）からマイクロソフト VOLT（Visual OpenType Layout Tool）による視覚的レイアウト、FontForge における OpenType および Apple AAT（Apple Advanced Typography）の低レベル状態機械管理、グリフ置換（GSUB）、精密位置調整（GPOS）、複雑な合字、アンカー結合、連鎖文脈規則、カーニング調整および有限状態オートマトンによる文字再配置機構。"
head:
  - - meta
    - name: keywords
      content: OpenType, AAT, GSUB, GPOS, VOLT, FontLab, FontForge, 合字, リガチャ, カーニング, 有限状態オートマトン, 高度組版, デーヴァナーガリー, アラビア文字
---

# 第14章：書体の深化：高度な組版技術体系
### Chapter 14: Enriching Fonts: Advanced Typography

**ヤニス・ハラランブス 博士（Yannis Haralambous, Ph.D.）著**  
**英訳および補訂：P. スコット・ホーン 博士（P. Scott Horne, Ph.D.）**  
*『Fonts & Encodings』原著第549〜598頁より*  

*訳者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

## 14.1 序論（Introduction）

伝統的な活版印刷や初期のデジタルフォントにおいて、テキストの表示とは本質的に素朴な1対1の写像であった。すなわち、1つの文字コードが入力されると、組版エンジンは対応するコードポイントから単一の固定されたグリフ（Glyph）を取り出し、あらかじめ設定された送り幅（Advance Width）に従ってベースラインに沿って前進配置する。しかし、人類の豊かな文字文化は決してこれほど無機的かつ単純なものではない。欧文古典組版における `fi`、`fl`、`ffi` 等の衝突回避リガチャ（合字）、優雅なスモールキャピタル（Small Capitals）、文脈に応じて自律的に切り替わるノンライニング数字（オールドスタイル数字 / Medieval Numbers）、伸びやかなスワッシュ（Swash）字形；あるいはアラビア文字、ペルシャ文字、ウルドゥー文字のような筆記文字において、文字が語頭（Initial）、語中（Medial）、語末（Final）、独立（Isolated）のいずれの位置にあるかに応じて動的に形状を変化させ垂直に重なり合う機構；さらには南アジア諸文字（デーヴァナーガリー、ベンガル文字、タミル文字等）に見られる子音結合子（Consonant Clusters）の再構成、半文字形態、母音記号（マトラ）が主子音の上下、さらには左側を跨いで回り込む複雑な音節合成規則——これら高度な組版要求は、現代のデジタルフォント規格に根本的な革新を迫った。

これら複雑な組版課題を抜本的に解決するため、コンピュータフォント工学界は二大峰とも呼ぶべき高度な技術アーキテクチャを創出した：

1. **OpenType レイアウト体系（OpenType Layout）**：マイクロソフトと Adobe が共同策定した規格。TrueType または PostScript フォントコンテナの内部に `GSUB`（グリフ置換表、Glyph Substitution Table）および `GPOS`（グリフ位置調整表、Glyph Positioning Table）を中核として埋め込み、補助的な `GDEF`（グリフ定義表）や `BASE`（ベースライン表）と連携させることで、言語体系（Script / Language System）、組版機能（Feature）、およびルックアップ（Lookup / Subtable）に基づく宣言的ルール書き換えと幾何位置微調整の枠組みを構築した。
2. **Apple AAT 体系（Apple Advanced Typography）**：アップル社が QuickDraw GX の革新的アーキテクチャから発展させた規格。中核となる `morx`（拡張変異テーブル、Extended Metamorphosis Table）および `kerx`（拡張カーニングテーブル、Extended Kerning Table）を介して、フォントの内部に厳密な**有限状態オートマトン（Finite State Automaton）**を直接内蔵した。組版エンジンが文字ストリームを走査する際、状態機械が現在の状態と入力クラスに応じて動的遷移を行い、グリフの並べ替え、置換、スタックバックトラック処理をリアルタイムに実行する。

本章では、現代のフォント制作の実際の現場に分け入り、FontLab Studio、マイクロソフト VOLT、およびオープンソースの FontForge において、これら高度な組版規則がいかに構築、構成、デバッグされるかを体系的に解明する。

---

## 14.2 FontLab における OpenType テーブルの管理（Managing OpenType Tables in FontLab）

FontLab は、Adobe が策定した特性ファイル定義言語（AFDKO Feature Definition Language）に基づく純テキスト構文コンパイラを深く統合している。書体デザイナーは低レベルのバイナリバイトオフセットを手作業で記述する必要はなく、特性編集ウィンドウで人間可読な構文を用いて置換・配置規則を記述するだけで、コンパイルエンジンがそれを OpenType 規格準拠の `GSUB` および `GPOS` テーブルへと自動的にパッケージ化する。

### 14.2.1 特性定義言語（Feature Definition Language）

Adobe 特性定義構文は厳格な宣言的構造に基づいており、その基本単位はフィーチャーブロック（Feature Block）である：

```fea
feature liga {
    sub f i by f_i;
    sub f l by f_l;
    sub f f i by f_f_i;
} liga;
```

上記のコードにおいて、`feature liga` は標準合字機能（Standard Ligatures）を宣言している。内部の `sub ... by ...` 文はグリフ置換命令である。組版エンジンがテキストを走査する際、グリフ `f` と `i` が連続して出現すると、自動的にあらかじめ設計された合字グリフ `f_i` へと折り畳まれて置換される。

::: tip 図 14-1：FontLab における OpenType 機能管理・構成パネルウィンドウ
![Figure 14-1: The OpenType window in FontLab](/images/fonts-encodings/fig14-1.png)
*図 14-1：FontLab の OpenType 機能編集画面。左ペインに宣言された全 OpenType フィーチャー一覧、右上にコードエディタ、右下にコンパイルログおよび構文エラーフィードバックが表示される。*
:::

#### 1. 言語体系の宣言（Language Systems）
OpenType の規則は無差別に大域適用されるのではなく、特定の書字体系（Script）および言語体系（Language System）に厳密にバインドされる。特性ファイルの先頭で、対応するスクリプトと言語を明示的に宣言しなければならない：

```fea
languagesystem DFLT dflt;
languagesystem latn dflt;
languagesystem latn TRK ; /* トルコ語専用環境 */
```

この宣言を行うことで、組版エンジンは特定の言語環境で段落を描画する際にのみ、該当ブランチに紐づけられた規則を活性化する。例えばトルコ語においては、点付きの小文字 `i` の大文字は点付きの `İ` であり、点なしの小文字 `ı` の大文字は点なしの `I` である。したがって、トルコ語環境では `fi` を通常の合字に置換することを厳禁しなければならない（さもなければ点付き `i` のドットが消失し、綴りの意味的混乱を引き起こすためである）。

#### 2. グリフクラス（Glyph Classes）
大量の文字を効率的に一括処理するため、デザイナーはグリフをクラスとしてグループ化できる：

```fea
@FIGURES_LINING   = [zero one two three four five six seven eight nine];
@FIGURES_OLDSTYLE = [zero.oldstyle one.oldstyle two.oldstyle three.oldstyle ...];

feature onum {
    sub @FIGURES_LINING by @FIGURES_OLDSTYLE;
} onum;
```

組版エンジンは対応する位置のグリフを1対1で高速並行置換する。

---

### 14.2.2 GSUB（グリフ置換）テーブルの6大ルックアップ種別

`GSUB` テーブルは以下の6種類の異なる置換ルックアップ（Lookups）をサポートする：
1. **単一置換（Single Substitution）**：1個のグリフを別の1個のグリフへ置換（例：小文字からスモールキャピタルへの置換）；
2. **複数置換（Multiple Substitution）**：1個のグリフを連続する複数のグリフへ展開（例：合字の分解）；
3. **選択的置換（Alternate Substitution）**：1個のグリフに対して複数の意匠バリエーションが存在し、ユーザーが手動選択（例：異なるカリグラフィ装飾スワッシュ）；
4. **合字置換（Ligature Substitution）**：連続する複数のグリフを単一の複合合字グリフへ結合（`f + i -> f_i`）；
5. **文脈依存置換（Contextual Substitution）**：前後の文脈環境に応じて特定のグリフを置換；
6. **連鎖文脈依存置換（Chaining Contextual Substitution）**：先行文脈（Backtrack）、入力グリフ（Input）、後続文脈（Lookahead）をそれぞれ厳密に定義し、入力部分のみを選択的に置換する高度な規則：
   ```fea
   sub [a e i o u] f' i' by f_i; /* 直前が母音の場合のみ fi を合字化 */
   ```

::: tip 図 14-2：FontLab における文脈連鎖置換（Chaining Contextual Substitution）のルックアップ定義画面
![Figure 14-2: Chaining Contextual Substitution in FontLab](/images/fonts-encodings/fig14-2.png)
*図 14-2：FontLab の文脈依存置換定義。先行文脈と後続文脈の制約のもとで特定の置換を実行する規則の設計画面。*
:::

---

### 14.2.3 GPOS（グリフ位置調整）テーブルとカーニング

`GPOS` テーブルは、グリフの字幅（Advance Width）や配置座標（$X, Y$ オフセット）をミリ単位で微調整する責務を担う：
* **単一位置調整（Single Adjustment）**：特定グリフの字幅やベースライン高さを単独で微小移動；
* **ペア位置調整（Pair Adjustment, カーニング）**：特定の文字の組み合わせ（`AV`、`To`、`Wa` など）が出現した際、文字間の過度なホワイトスペースを詰める。クラスベースカーニング（Class-based Kerning）を用いることで、何万組ものペアを極めて軽量なデータ量で高速処理する；
* **アタッチメント位置調整（Mark-to-Base, Mark-to-Mark）**：アラビア文字のシャクル（母音記号）やヘブライ文字のニクードを、基底文字の所定のアンカーポイント（Anchor）へ幾何学的に吸着配置させる。

::: tip 図 14-3：FontLab のメトリクスウィンドウにおけるクラスベース・ペアカーニングの視覚的調整画面
![Figure 14-3: Class-based kerning interface in FontLab](/images/fonts-encodings/fig14-3.png)
*図 14-3：FontLab のペアカーニング調整画面。左側のグリフクラスと右側のグリフクラスの間の送り幅アキを視覚的に操作する。*
:::

::: tip 図 14-4：FontLab におけるアンカーポイント（Anchors）による発音記号の自動吸着配置画面
![Figure 14-4: Anchor attachment interface in FontLab](/images/fonts-encodings/fig14-4.png)
*図 14-4：基底文字と上部アクセント記号のアンカー結合設計画面。*
:::

---

## 14.3 マイクロソフト VOLT（Visual OpenType Layout Tool）

複雑な非ラテン文字（特にアラビア文字や南アジアのインド系文字）を制作するタイポグラフィ技術者にとって、マイクロソフトが無償提供する **VOLT（Visual OpenType Layout Tool）** は、業界の絶対的な標準開発環境である。

FontLab がテキストコードによる記述を重んじるのに対し、VOLT は完全な**視覚的グラフィカルインターフェース**を採用している：

::: tip 図 14-5：マイクロソフト VOLT のメインプロジェクト管理ウィンドウ
![Figure 14-5: Microsoft VOLT main project window](/images/fonts-encodings/fig14-5.png)
*図 14-5：VOLT のメインプロジェクト画面。グリフ定義、グリフグループ、ルックアップ、スクリプトおよびフィーチャーの階層的ツリーが整然と管理されている。*
:::

VOLT の開発パイプラインは極めて体系的である：
1. **グリフ定義とコンポーネント分類**：フォント内の全グリフを Base（基底文字）、Ligature（合字）、Mark（発音記号）、Component（構成部品）の4種に厳密に分類する（これが `GDEF` テーブルの骨格となる）；
2. **グリフグループ（Groups）の編成**：共通の文脈振る舞いを持つグリフ群を直感的なドラッグ＆ドロップで視覚的に束ねる；
3. **ルックアップの構築とプレビュー**：置換前後のグリフを画面上で並べて確認しながら、文脈依存規則や合字分解規則を直感的に組み上げる；
4. **統合テスト・校正ウィンドウ**：VOLT 内蔵の校正エンジンにより、実際の複雑な文字列を入力して、各ルックアップがどの順序で発火しグリフがどのように変形・結合されるかを1ステップずつリアルタイムに追跡できる（図 14-6、14-7、14-8）。

::: tip 図 14-6：VOLT における合字置換（Ligature Substitution）の視覚的定義画面
![Figure 14-6: Visual definition of Ligature Substitution in VOLT](/images/fonts-encodings/fig14-6.png)
*図 14-6：VOLT の合字ルックアップ編集画面。*
:::

::: tip 図 14-7：VOLT における文脈依存グリフ置換（Contextual Substitution）の編集画面
![Figure 14-7: Contextual substitution interface in VOLT](/images/fonts-encodings/fig14-7.png)
*図 14-7：VOLT の文脈依存置換編集画面。*
:::

::: tip 図 14-8：VOLT におけるマーク結合（Mark-to-Base）アンカー配置のグラフィカル設定画面
![Figure 14-8: Mark-to-Base anchor attachment in VOLT](/images/fonts-encodings/fig14-8.png)
*図 14-8：VOLT のアンカー結合画面。*
:::

::: tip 図 14-9：VOLT のテキスト組版校正・デバッグウィンドウ
![Figure 14-9: Text proofing and testing window in VOLT](/images/fonts-encodings/fig14-9.png)
*図 14-9：VOLT のテストウィンドウ。複雑な文字列が所定のルールに従って正しく音節結合されているかをリアルタイムに検証する。*
:::

---

## 14.4 FontForge における OpenType および Apple AAT の管理

オープンソースの雄 **FontForge** は、OpenType レイアウト規則の構築と、アップル独自の **Apple Advanced Typography（AAT）** の低レベル状態機械の構築を同時にサポートする唯一無二の多機能フォントエディタである。

::: tip 図 14-10：FontForge におけるフォント情報パネル内の OpenType 特性・ルックアップ管理インターフェース
![Figure 14-10: FontForge Font Info window: OpenType features management](/images/fonts-encodings/fig14-10.png)
*図 14-10：FontForge の OpenType 機能管理画面。GSUB および GPOS の各ルックアップがツリー構造で一覧化されている。*
:::

::: tip 図 14-11：FontForge における単一グリフのアンカーポイント編集画面
![Figure 14-11: Anchor points editing in FontForge](/images/fonts-encodings/fig14-11.png)
*図 14-11：FontForge のアンカーポイント編集画面。*
:::

::: tip 図 14-12：FontForge における文脈依存連鎖置換（Contextual Chaining）のルール作成ダイアログ
![Figure 14-12: Contextual Chaining rule configuration in FontForge](/images/fonts-encodings/fig14-12.png)
*図 14-12：FontForge の文脈連鎖ルール設定ダイアログ。*
:::

### Apple AAT の有限状態オートマトン（State Machine）設計

Apple AAT は、OpenType のような入れ子状のルックアップではなく、**有向グラフによる有限状態機械（State Machine）**を採用している。FontForge は AAT の `morx` テーブルの設計インターフェースを完全に備えている（図 14-13、14-14、14-15）：

* **クラス分類（Classes）**：文字をその振る舞いに応じて有限個の入力シンボルクラス（Class 0 = End of Text、Class 1 = Out of Bounds、Class 2 = デフォルト、Class 3 以降 = 各種子音・母音）に割り当てる；
* **状態（States）**：初期状態（State 0 = Start of Text、State 1 = Start of Line）から、文字を読み進めるごとに状態番号が遷移する；
* **状態遷移表（State Transition Table）**：マトリクスの各セルにおいて、次の状態番号（Next State）と、その際に実行すべきアクションフラグを定義する：
  * 現在のグリフをマーク（Mark）として記憶する；
  * 先行してマークされたグリフを特定の代替グリフへ置換する；
  * 現在のグリフを置換する；
  * 文字列の読み取り位置を巻き戻す（Push/Pop）。

::: tip 図 14-13：FontForge における Apple AAT 状態機械（State Machine）のグリフクラス割り当て画面
![Figure 14-13: Glyph class assignment for Apple AAT state machine in FontForge](/images/fonts-encodings/fig14-13.png)
*図 14-13：FontForge による AAT 状態機械のグリフクラス定義画面。*
:::

::: tip 図 14-14：FontForge における Apple AAT 状態機械の状態遷移マトリクス編集ウィンドウ
![Figure 14-14: State transition table of Apple AAT in FontForge](/images/fonts-encodings/fig14-14.png)
*図 14-14：FontForge の AAT 状態遷移マトリクス。入力クラスと現在の状態に基づいて、次状態と実行動作を決定する。*
:::

::: tip 図 14-15：FontForge における Apple AAT 状態遷移に伴うグリフ置換・変形アクション設定ダイアログ
![Figure 14-15: Glyph substitution actions configuration in FontForge AAT](/images/fonts-encodings/fig14-15.png)
*図 14-15：状態遷移時に発火する具体的なグリフ置換アクションの指定画面。*
:::

---

## 14.5 結び（Conclusion）

OpenType Layout と Apple AAT という二大高度組版体系の確立により、デジタルフォントはかつての「静的な輪郭の詰め合わせ」から、「文脈を自己解釈して動的に振る舞う知的ソフトウェア」へと決定的な脱皮を遂げた。

ラテン文字の優美な合字や数字スタイルの自動調和から、アラビア文字の流麗なリガチャ変形、そしてインド系諸言語の複雑極まる音節合成に至るまで——フォントの深層に焼き付けられたこれら高度な組版テーブルこそが、人類が何千年もの歳月をかけて紡ぎ出してきた多様な筆記文化の魂を、現代のデジタルスクリーンの上で損なうことなく完全に再現することを可能にしているのである。
