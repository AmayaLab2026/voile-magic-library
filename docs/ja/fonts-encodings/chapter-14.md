---
title: "第 14 章：フォントの知性化：高度なタイポグラフィ機能"
description: "OpenType の置換と配置（GSUB/GPOS）、AFDKO 機能定義言語の完全な構文仕様、Microsoft VOLT による視覚的構築、FontForge、Apple Advanced Typography（AAT）の有限状態機械（morx/kerx）の全貌。"
---

# 第 14 章：フォントの知性化：高度なタイポグラフィ機能
### Chapter 14: Enriching Fonts: Advanced Typography
ヤニス・ハラランボス（Yannis Haralambous, Ph.D.）著
選書『Fonts & Encodings』第 551–598 頁
*訳者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

## 1. 組版知性化の進化とパラダイムシフト（Introduction）

従来のデジタルフォント（初期の PostScript Type 1 やプレーンな TrueType など）において、フォントファイルは本質的に**静的なグリフ輪郭のコンテナ**に過ぎませんでした。OS がテキスト文字列（ASCII や Unicode コードポイントの並び）を受け取った際に行うのは、最も単純な「テーブル引き—輪郭抽出—描画」という一方向のマッピングだけでした。各文字は常に固定された単一のグリフに対応し、文字間の配置はあらかじめ定義された水平送り幅（Advance Width）の機械的な累積加算と、せいぜい単純な字間ペアカーニング表に依存していました。

しかし、人類が何世紀にもわたり培ってきた活版印刷の伝統と、世界各地の複雑な文字体系は、コンピュータの組版エンジンに対して全く異なる要求を突きつけます：
- **西欧古典組版の審美眼**：文字の衝突を回避し視覚的リズムを高めるため、特定の連続文字は単一の洗練されたリガチャ（合字）へと融合されねばなりません（例: $\text{f}+\text{i} \to \text{fi}$、$\text{f}+\text{f}+\text{l} \to \text{ffl}$）。本文中の大文字と小文字が混在する箇所では小文字サイズに光学設計されたスモールキャピタル（Small Capitals）が要求され、地の文では上下に起伏するオールドスタイル数字（Oldstyle Figures）、財務表では等幅のライニング数字（Lining Figures）が必須となります。さらに、分数は斜めバーの分数（Diagonal Fractions）や水平バーの分数（Vertical Fractions）へと自動変換される必要があります。
- **非ラテン系複雑書記体系**：アラビア文字、シリア文字、モンゴル文字などでは文字が天然の草書連筆特性を持ち、同じ文字でも単語内の位置（語頭 Initial、語中 Medial、語末 Final、独立形 Isolated）に応じてまったく異なる物理的トポロジーを形成します。また、南アジアや東南アジアの文字（デーヴァナーガリー Devanagari、ベンガル文字 Bengali、タミル文字 Tamil、クメール文字 Khmer など）では、子音同士が結合して不可分な結合子音を形成し、特定の母音記号は論理的に子音の後ろに入力されながらも視覚的には子音クラスタの左側に回り込んで再配置（Reordering）されねばなりません。

もしこれらの複雑な言語学的規則や文脈判断を OS のカーネルや個々のアプリケーション内部にハードコーディングしてしまえば、フォントの可搬性は失われ、新たな書記系や特殊な組版スタイルの拡張は完全に不可能となります。

そのため、1990 年代中盤、デジタルフォント産業は**歴史的なパラダイムシフト**を迎えました。それが**フォントの知性化（Enriching Fonts）**です。組版規則の解析と実行ロジックはフォントファイルそのものの内部へと移譲されました。フォントは受動的なデータベースであることをやめ、**自律的な文脈判断能力とマイクロ構文規則、有限状態機械を内包した知的実行主体**へと変貌を遂げたのです。現在主流となっている高度組版フォント規格には以下の 2 つが存在します：
1. **OpenType（TrueType 輪郭および CFF/PostScript 輪郭を含む）**：Microsoft と Adobe が共同策定した、宣言的規則と階層的テーブル探索に基づくアーキテクチャ；
2. **Apple Advanced Typography（AAT）**：Apple が QuickDraw GX を源流として発展させた、計算理論における純粋な**決定性有限状態自動機（Finite State Machine, FSM）**に基づくアーキテクチャ。

### 1.1 文字からグリフへ：テキストシェイピング（Text Shaping）の動的変容
現代の組版シェイピングエンジン（オープンソースの HarfBuzz、Windows の Uniscribe/DirectWrite、macOS の CoreText など）のパイプラインにおいて、この処理は**テキストシェイピング（Text Shaping）**と呼ばれます。入力された Unicode 文字列は画面上に描画されるまでに次のような多次元の動的変容を経ます：

$$\text{Unicode Code Points} \xrightarrow{\quad\text{cmap マッピング}\quad} \text{Glyph IDs} \xrightarrow{\quad\text{GSUB 置換}\quad} \text{Glyph IDs} \xrightarrow{\quad\text{GPOS 配置}\quad} \text{Positioned Glyphs}$$

この過程において、文字とグリフの間の 1 対 1 の関係は完全に打破され、多彩なマッピング形態が出現します：
- **1 対多（One-to-Many）**：単一の文字が複数のグリフ部品に分解される；
- **多対 1（Many-to-One）**：複数の連続文字が単一のリガチャグリフへと融合される；
- **多対多（Many-to-Many）**：一連の文字列が長さや形態の異なる別のグリフ列へと再構成される；
- **動的微細幾何変位**：グリフはもはやベースライン上に機械的に並ぶだけでなく、2 次元平面内で自在にシフトし、基底文字輪郭上の物理アンカーに対してピクセル精度で磁気吸着します。

### 1.2 高度組版の双翼：字形置換（GSUB）と幾何配置（GPOS）
OpenType アーキテクチャにおいて、フォントの高度組版機能は **GSUB（Glyph Substitution Table、字形置換テーブル）** と **GPOS（Glyph Positioning Table、字形配置テーブル）** の 2 つのモジュールテーブルに明快に分離されています。

#### 1. 字形置換の 6 大形態（GSUB）
字形置換は座標系を変更することなく、構文的文脈に応じて現在のグリフを最適な候補グリフへと差し替えます：
1. **単一置換（Single Substitution）**：あるグリフを別のグリフに直接置換（例: `a` $\to$ `a.sc`）；
2. **複数置換（Multiple Substitution）**：単一のグリフを複数の連続するグリフに分解（連字の解体や結合文字の分解）；
3. **代替字形置換（Alternate Substitution）**：美学的に等価な複数のバリアントを提供。例えば Hermann Zapf の **Zapfino** では小文字 `d` に 9 種類もの流麗なバリエーションが存在し、ユーザーが自由に選択できます；
4. **合字置換（Ligature Substitution）**：複数の連続グリフを単一の合字グリフへ融合（`f` + `i` $\to$ `fi`）；
5. **文脈的置換（Contextual Substitution）**：置換の発生が前後の環境に依存。アラビア文字のように、後続に文字が存在する場合にのみ語頭形へと変化します；
6. **連鎖文脈置換（Chained Contextual Substitution）**：文脈環境を**後退列（Backtrack）**、**入力列（Input）**、**前進列（Lookahead）**の 3 つに分離し、文脈と置換対象を独立させることで連続的な連鎖トリガーを可能にします；
7. **逆方向連鎖文脈単一置換（Reverse Chaining Contextual Single Substitution）**：ウルドゥー語（Urdu）のナスタアリーク体（Nastaliq）のように、右横書きでありながら後続（左側）の文字形状に依存して先行文字の垂下高さや連筆が決定される文字のため、書字方向とは逆の左から右へと逆流スキャンして置換を行います。

#### 2. 字形微視幾何配置の 6 大形態（GPOS）
1. **単一調整（Single Adjustment）**：単一グリフの水平・垂直位置や送り幅を微調整（全大文字時の括弧類の引き上げなど）；
2. **ペア調整（Pair Adjustment / Kerning）**：特定のグリフペアの間隔を X 軸・Y 軸で微調整；
3. **筆記体接続（Cursive Attachment）**：各グリフに「入刀点（Entry）」と「出刀点（Exit）」アンカーを定義し、前後のグリフを 2 次元空間で滑らかに吸着接続；
4. **マーク吸着基底（Mark-to-Base Attachment）**：基底文字のアンカーに対してダイアクリティカルマーク（アクセント記号）を精密に磁気吸着；
5. **マーク間吸着（Mark-to-Mark Attachment）**：既存のマークの上にさらに別のマークを多重積層；
6. **合字部品マーク吸着（Mark-to-Ligature Attachment）**：合字内の各構成コンポーネントに対して個別のアンカーを割り当て、合字中の特定母音の上にだけアクセントを正確に配置；
7. **文脈配置および連鎖文脈配置（Contextual / Chained Contextual Positioning）**：文脈に応じて配置を発動（例: `V.A.V.` ではピリオドと V を詰めるが、`V.V.` では文字衝突を防ぐため詰めない）。

#### 3. 標準機能タグ体系（Standard Feature Tags）
4 つの ASCII 文字からなるタグにより世界中の組版ソフトウェアから呼び出されます：`liga`, `dlig`, `hist`, `smcp`, `c2sc`, `onum`, `lnum`, `tnum`, `pnum`, `frac`, `afrc`, `kern`, `mark`, `mkmk`, `curs`, `size`, `aalt` 等。

---

## 2. FontLab における OpenType テーブルと AFDKO 構文の管理

**FontLab Studio**（バージョン 4.x / 5.x）は、Adobe が策定した業界標準 **AFDKO（Adobe Font Development Kit for OpenType）機能定義構文** をネイティブに採用しています。

### 2.1 AFDKO 機能定義言語の構文体系

#### 1. グリフクラス（Glyph Classes）の定義
グリフクラスは `@` で始まり、一括処理するグリフ群をブラケット `[` と `]` でグループ化します：

```fea
@VOWELS = [ a e i o u y ];
@UPPERCASE = [ A-Z ];
@SC_LETTERS = [ a.sc-z.sc ];
@ALL_LETTERS = [ @UPPERCASE @VOWELS agrave eacute ];
```

#### 2. 書記系、言語、機能のブロック構造
OpenType の 4 段階階層（Script $\longrightarrow$ Language $\longrightarrow$ Feature $\longrightarrow$ Lookup）を直接記述します：

```fea
languagesystem DFLT dflt;
languagesystem latn dflt;
languagesystem latn TRK ;

feature liga {
    script latn;
    language DFLT;
        sub f i by f_i;
    language DEU;
        sub c k by c_k;
    language ENG excludeDFLT;
        sub f f l by f_f_l;
} liga;
```

#### 3. 名前付きルックアップと lookupflag
`lookupflag` によりスキャン時のスキップ対象を厳密に制御します：
- `lookupflag IgnoreMarks;`：ダイアクリティカルマークを無視して隣接文字を判定。合字判定において極めて重要；
- `lookupflag RightToLeft;`：右横書き専用。

#### 4. 置換規則（GSUB）とアポストロフィ構文（`'`）
文脈置換において、**アポストロフィ（`'`）が付いたグリフが実際の置換対象**であり、付いていないグリフは単なる文脈環境です：

```fea
sub [ f f_f ] i' by i.nodot;
```

- **`ignore sub` の構文トラップ**：
  ロゴ "TEX" を置換する際、`CONTEXTUAL` や `TEXT` などの通常単語を保護するため、カンマで複数除外条件を記述します：
  ```fea
  ignore sub [ A-Z ] T' E' X' , T' E' X' [ A-Z ] ;
  sub T' E' X' by T_e_X ;
  ```
  1 行目に `ignore sub` があるため、ルックアップ全体が文脈的とみなされ、2 行目の置換対象にもアポストロフィが必須となります。

#### 5. 配置規則（GPOS）と値レコード
値レコードは 4 つの整数ベクトルです：
$$\langle xPlacement \quad yPlacement \quad xAdvance \quad yAdvance \rangle$$
- クラス間カーニング：`pos @Left_Round @Right_Round -40;`
- 筆記体接続：`pos cursive f <anchor -10 0> <anchor 197 105>;`
- 合字マーク吸着：`<anchor NULL>` で不要なコンポーネントをスキップ可能。

#### 6. 光学サイズ特性（`size`）
```fea
feature size {
    parameters 120 1 90 299;
} size;
```
設計光学サイズ 12.0 pt、ファミリー通し番号 1、推奨適用範囲 9.0 pt 〜 29.9 pt を明示。

---

## 3. Microsoft VOLT による視覚的 OpenType 構築（Managing OpenType Tables in VOLT）

Microsoft の **VOLT（Visual OpenType Layout Tool）** は Windows の **Uniscribe** エンジンと密結合した高機能レイアウトツールです。

### 3.1 VOLT のプロジェクト構造と私有テーブル
- フォント内部に `TSIV` などの非標準 XML 私有テーブルを保持してプロジェクトを管理；
- 他ツールで作成された標準 OpenType テーブルを破壊的に初期化するため、事前のバックアップが不可欠；
- PostScript 名のインポートと全グリフの型（`base`, `ligature`, `mark`, `component`）分類。

### 3.2 視覚的アンカー吸着と校正ツール
- 矢印構文による直感的な置換定義：`f i -> f_i`；
- ウルドゥー語等のための逆方向連鎖置換（Reversal チェックボックス）；
- 画面上でマウスドラッグによる直感的なアンカー座標吸着；
- **Proofing Tool**：Uniscribe を介したリアルタイムのテキストシェイピング検証環境；
- `File > Ship Font`：私有テーブルを完全に剥離したクリーンな商用フォントの出力。

---

## 4. FontForge における OpenType テーブルの管理（Managing OpenType Tables in FontForge）

FontForge はコードの知識を必要とせず、完全なメニューとダイアログによって OpenType 表を視覚的かつ無損失で管理できます。

### 4.1 Lookups 管理とアンカークラス
- `Element > Font Info > Lookups`（GSUB/GPOS 分割タブ）；
- `Anchor Classes` で `mark`, `mkmk`, `curs` を定義し、グリフ編集画面で右クリックから `Add Anchor Point` により対話的にアンカーを配置；
- 単一、複数、代替、合字置換のグラフィカル設定；
- 4 段階ウィザードによる連鎖文脈置換（Backtrack, Input, Lookahead）。

---

## 5. FontForge による Apple Advanced Typography（AAT）有限状態機械の構築

AAT は OpenType とは根本的に異なり、純粋な**決定性有限状態自動機（FSM）**として組版を処理します。

### 5.1 AAT の計算理論的優位性
- 単一方向の線形スキャン、計算量は厳密に $O(N)$ でバックトラックが存在しない；
- 中核テーブル：`morx`（変形）、`kerx`（拡張字距）、`feat`（特性名）、`trak`（トラッキング）。

### 5.2 AAT 状態機械の 4 つのコアオペレーション
1. **グリフ並べ替え（Glyph Rearrangement）**：
   天城文等で前置される短元音 `r` を子音クラスタの先頭へ移動（`KGPTHr` $\longrightarrow$ `rKGPTH`）。状態 0、状態 2（子音蓄積）、`xD => Dx` による一瞬の順序反転。
2. **文脈置換（Contextual Substitution）**：
   一方向スキャンの時間的矛盾を解決する「Mark Current Glyph」と遅延置換（斜め分数 `1/2` の分子・分母自動変換）。
3. **グリフ動的挿入（Glyph Insertion）**：
   アラビア語の Kashida（タトウィール引き伸ばし線）やクメール文字の分割母音記号をテキストストリームへ動的に無中生有で挿入。カーソル選択可否の属性制御。
4. **文脈的拡張字距（Contextual Kerning / `kerx`）**：
   状態機械内にスタック（最大 8 個）を維持し、`Push Current Glyph` と `Pop` により、`A.V.` などの 3 文字文脈において $n-1$ 個の字間オフセットを同時に適用。

---

## 6. 結語と現代の組版エンジンの展望（Conclusions and Modern Outlook）

Uniscribe と CoreText の歴史的競争を経て、今日ではオープンソースの **HarfBuzz** が OpenType と AAT の両仕様を完全に統合し、世界中のブラウザや OS で稼働しています。

フォントはもはや単なる画像の集合ではありません。幾何学、代数学、オートマトン理論を内包した**自律的マイクロコンピュータ**であり、人類の書記文化の美をデジタル空間に永続させる架け橋なのです。

*本章の完全 1:1 全景翻訳および技術校正は ヴワル魔法図書館（Voile Magic Library）文献翻訳工房 により完了しました。*
