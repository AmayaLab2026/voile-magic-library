---
title: "第 14 章：フォントの知性化：高度なタイポグラフィ機能"
description: "OpenType レイアウトエンジン、AFDKO 機能ファイル文法、GSUB/GPOS、VOLT 視覚的アンカー設計、FontForge、Apple Advanced Typography (AAT) 有限状態機械の全景。"
---

# 第 14 章：フォントの知性化：高度なタイポグラフィ機能
### Chapter 14: Enriching Fonts: Advanced Typography
ヤニス・ハラランボス（Yannis Haralambous, Ph.D.）著
選書『Fonts & Encodings』第 551–598 頁
*訳者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

## 1. 高度組版体系の全景（Introduction）

従来のフォント（PostScript Type 1 や初期の TrueType）は、文字コード（Unicode/ASCII）から単一の静的グリフ形状への一対一の写像しか提供できませんでした。しかし、人類の高度な組版の伝統（合字、スモールキャップス、オールドスタイル数字）や、世界中の複雑な書記系（アラビア文字の語頭・語中・語末・独立形の連筆変化、デーヴァナーガリー文字の子音結合と母音記号の並べ替えなど）をスクリーン上で完全に表現するには、フォント自身が「文脈を理解する知性」を備える必要があります。

### 1.1 文字からグリフへ：テキストシェイピング（Text Shaping）の動的変容
現代のテキストレンダリングにおいて、入力されたプレーンテキストは組版シェイピングエンジン（HarfBuzz, CoreText, DirectWrite）を通過し、次のような多対多の動的変換を経ます：
- **一対多**：単一の文字が複数のグリフ片に分解される（例: ベンガル文字母音記号の前後分割）；
- **多対一**：複数の連続する文字が単一の合字グリフへ融合される（例: `f` + `i` $\to$ `fi`）；
- **文脈的置換**：隣接する前後の文字に応じてグリフ形状が動的に差し替えられる（アラビア文字の接続形）；
- **微細幾何位置決め**：基底文字の上下左右の厳密なアンカー点にダイアクリティカルマーク（アクセント記号）を吸着配置する。

### 1.2 高度組版の 2 大テーブル：GSUB と GPOS
OpenType はこの処理を 2 つのモジュールテーブルに分離して標準化しました：
1. **GSUB（Glyph Substitution Table）**：グリフの同定と置換を担当（リガチャ、異体字、スモールキャップス、分数表記など）；
2. **GPOS（Glyph Positioning Table）**：グリフの微細な幾何位置決めを担当（カーニング、マーク吸着配置、筆記体の接続など）；
3. **標準機能タグ（Feature Tags）**：4 文字のアスキー識別子で機能を分類（`liga` 標準合字、`dlig` 任意合字、`smcp` スモールキャップス、`c2sc` 大文字スモールキャップス、`onum` オールドスタイル数字、`tnum` 表用等幅数字、`kern` 水平カーニング、`mark` マーク位置決め、`mkmk` マーク間位置決め等）。

---

## 2. FontLab における OpenType と AFDKO 言語の管理

FontLab Studio は、Adobe が開発した業界標準の **AFDKO（Adobe Font Development Kit for OpenType）機能定義構文（Feature File Syntax）**をネイティブにサポートしています。

### 2.1 AFDKO 機能定義言語の構文体系

#### 1. グリフクラス（Glyph Classes）の定義
グリフクラスはアットマーク `@` で始まり、一括処理を行うグリフのグループを定義します：

```fea
# 形式 1：明示的列挙
@LOWERCASE = [a b c d e f g h i j k l m n o p q r s t u v w x y z];

# 形式 2：範囲表記（ASCII 昇順）
@DIGITS = [zero-nine];

# 形式 3：接尾辞付き範囲表記
@SC_LETTERS = [a.sc-z.sc];

# 形式 4：クラスの包含と入れ子
@ALL_LETTERS = [@LOWERCASE A-Z];
```

#### 2. 書記系、言語、機能のブロック構造
機能定義は、対象とする書記系（`script`）、言語システム（`language`）、そして機能ブロック（`feature`）の階層構造をとります：
$$\text{Scripts} \longrightarrow \text{Languages} \longrightarrow \text{Features} \longrightarrow \text{Lookups}$$

```fea
languagesystem DFLT dflt; # デフォルト言語システム
languagesystem latn dflt; # ラテン文字デフォルト
languagesystem latn TRK ; # ラテン文字トルコ語（点なし i の特別処理用）

feature liga {
    # 標準合字機能
    sub f i by f_i;
    sub f l by f_l;
    sub f f i by f_f_i;
} liga;
```

#### 3. 名前付きルックアップとフラグ（Named Lookups and Lookupflags）
処理の順序とスキップ条件を厳密に制御するため、名前付きルックアップと `lookupflag` を使用します：

```fea
lookup SkipMarksAndCursive {
    lookupflag IgnoreMarks; # ダイアクリティカルマークを無視して隣接判定
    sub f f by f_f;
} SkipMarksAndCursive;
```

#### 4. 置換規則（GSUB 規則全集）
- **単一置換（Single Substitution）**：
  `sub a by a.sc;` またはクラス間置換 `sub @LOWERCASE by @SC_LETTERS;`
- **多対一合字（Ligature Substitution）**：
  `sub f f l by f_f_l;`
- **一対多置換（Multiple Substitution）**：
  `sub f_f_i by f f i;`
- **選択置換（Alternate Substitution）**：
  `sub ampersand from [ampersand.alt1 ampersand.alt2 ampersand.alt3];`
- **文脈的置換（Contextual Substitution）**：
  置換対象のグリフにプライム記号 `'`（アポストロフィ）を付加します：
  `sub [f f_f] i' by i.nodot;`（先行文字が f または ff の場合のみ、i を点なし i に置換）
- **無視規則（Ignore Rules）**：
  `ignore sub e' t c;`（etc という連続の中の e は置換対象から除外）

#### 5. 位置決め規則（GPOS 規則全集）
GPOS の移動量は **Value Record**（4 つの固定小数点数値）で指定されます：
$$\langle xPlacement \quad yPlacement \quad xAdvance \quad yAdvance \rangle$$
- **単一グリフ調整**：
  `pos hyphen <0 30 0 0>;`（ハイフンを 30 単位上方にシフト）
- **ペアカーニング（Pair Kerning）**：
  `pos T e -80;`（T と e の間隔を 80 単位詰める）
  `pos @Left_Round @Right_Round -40;`（クラス間カーニング）
- **筆記体接続（Cursive Attachment）**：
  `pos cursive meem.medial <anchor 350 0> <anchor 0 150>;`
- **マーク位置決め（Mark-to-Base）**：
  基底文字のアンカーとアクセント記号のアンカーを合致させて吸着配置：
  `pos base [a e o] <anchor 250 450> mark @TOP_MARKS;`

#### 6. 光学サイズ `size` と代替字形 `aalt`
- **`aalt`（Access All Alternates）**：ユーザーがフォント内のすべての異体字にアクセスできるようにするメタ機能；
- **`size` パラメータ**：光学サイズ（Optical Size）用のデザイン寸法仕様：
  `parameters 10.0 3 8.0 11.9;`（デザインサイズ 10 pt、サブファミリー識別子 3、推奨表示範囲 8.0 pt 〜 11.9 pt）。

### 2.2 FontLab Studio における視覚的 OpenType パネル実戦
FontLab の OpenType パネルでは、左側に定義コードを記述し、下部のプレビューエリアでリアルタイムにテキストを入力して合字やカーニングの動作を即座に視覚的検証（Vector Preview）できます。

---

## 3. Microsoft VOLT による高度タイポグラフィのプロフェッショナル開発

マイクロソフトが開発した **VOLT（Visual OpenType Layout Tool）**は、Windows の Uniscribe エンジン用にアラビア文字、ヘブライ文字、インド系諸言語の複雑なフォントを構築するための最高峰のツールです。

### 3.1 VOLT の内部プロジェクトアーキテクチャ
- VOLT はフォントバイナリ内にプライベートな XML ソーステーブル（`TSIV` 等）を埋め込み、プロジェクトデータを直接管理します；
- **逆方向連鎖文脈置換（Reverse Chaining Contextual Single Substitution）**：アラビア文字のように右から左へ進行し、後続の文字形状に依存して先行文字が変化する書記系において、後ろから前へと走査する特殊なルックアップ形式を完全にサポート。

### 3.2 視覚的アンカー位置決め（Visual Anchor Attachment）
VOLT は GUI 上で基底文字とマーク記号のアンカーポイント（Anchor Points）をマウスでドラッグ＆ドロップして配置できます：
- 単純な基底文字とマーク（Mark-to-Base）；
- マークの上にさらにマークを重ねる階層吸着（Mark-to-Mark）；
- 合字グリフ内の個々のコンポーネントに対する独立したアンカー群（Mark-to-Ligature）。

---

## 4. FontForge における OpenType テーブルの管理

オープンソースの FontForge も、完全な OpenType GSUB/GPOS 作成インターフェースを備えています。

### 4.1 ルックアップ管理センター：Element > Font Info > Lookups
FontForge では、GSUB と GPOS の全ルックアップがツリー構造で管理されます。各ルックアップの下に複数のサブテーブル（Subtables）を作成し、ドラッグ＆ドロップで優先順位を入れ替えることが可能です。

### 4.2 アンカークラス（Anchor Classes）の作成と適用
FontForge のグリフエディタ上で `Anchor Point` を作成し、クラス名（例: `Top`, `Bottom`）と役割（`Base`, `Mark`, `Ligature`）を割り当てます。すべてのグリフが同一名のアンカーを持つことで、自動的に GPOS Mark ルックアップテーブルがコンパイルされます。

---

## 5. Apple Advanced Typography（AAT）状態機械の実戦

Apple が macOS の CoreText エンジン向けに開発した **AAT（Apple Advanced Typography）**は、OpenType とは根本的に異なる計算機科学的哲学に基づいています。

### 5.1 OpenType と AAT の計算理論的対比
- **OpenType**：宣言的な「パターン照合規則テーブル」モデル。シェイピングエンジンが文字列に対して前方・後方の文脈規則を網羅的に走査・探索します；
- **AAT**：決定性「**有限状態機械（Finite State Machine, FSM）**」モデル。テキストストリームを 1 文字ずつ消費しながら状態を遷移させ、状態遷移表（State Table）のアクションを実行します。計算量は入力文字列長に対して常に厳密な $O(N)$（線形時間）であり、バックトラックが発生しないため極めて高速です。

### 5.2 AAT のテーブル構成と機能選択システム
AAT は以下のモジュールテーブルで構成されます：
- **`morx`（Extended Glyph Metamorphosis Table）**：AAT の置換および並べ替え状態機械の中核；
- **`kerx`（Extended Kerning Table）**：状態機械による文脈的カーニング；
- **`feat`（Feature Name Table）**：macOS のタイポグラフィパネルに表示されるユーザー向けオプション名；
- **`trak`（Tracking Table）**：フォントサイズに応じた行全体のトラッキング（字間送り）自動調整。

### 5.3 AAT 状態機械の 4 つのコアオペレーション

FontForge の AAT テーブルエディタは、`morx` 内の 4 つの状態機械動作を直接プログラム可能です：

#### 1. グリフ並べ替え状態機械（Glyph Rearrangement）
インド系文字（デーヴァナーガリー、ベンガル等）において、論理的な入力順序と視覚的な表示順序が逆転する場合に使用されます：
- 状態機械が子音群を読み込みながらスタックにプッシュ；
- 前置母音記号に到達した瞬間、スタックから子音をポップし、母音記号の左側へと一撃で順序を反転（例: $K + G + P + T + H + r \longrightarrow r + K + G + P + T + H$）。

#### 2. 文脈置換状態機械（Contextual Substitution）
先行文字と現在文字のペアに基づいて、一方または両方のグリフを状態遷移表のアクションにより瞬時に置換します。

#### 3. グリフ動的挿入状態機械（Glyph Insertion）
特定の文字の組み合わせの間、あるいは単語の末尾に、元のテキストストリームには存在しなかった新規グリフを動的に割り込ませます：
- アラビア文字の Kashida（タトウィール、引き伸ばし線）の動的挿入；
- クメール文字の分割母音記号の自動補完。

#### 4. 文脈的カーニング状態機械（Contextual Kerning / `kerx`）
AAT はカーニングを有限状態機械として実行します：
文字を読み進めながら `Push Current Glyph` フラグでスタックにグリフを保持し、後続の文字の形状を確認した時点でスタックから文字をポップしながら、各文字間に最適なカーニングオフセットを適用します。これにより、3 文字以上の複雑な文脈カーニング（例: クォーテーションマークと大文字、ピリオドの組み合わせ）が線形時間で解決されます。

---

## 6. 結語と現代の組版エンジンの展望（Conclusions and Modern Outlook）

OpenType と AAT の並立は、デジタルフォント技術が到達した最高峰の成果です。今日、オープンソースの **HarfBuzz** エンジンの登場により、OpenType と AAT の両方の仕様が世界中のあらゆるブラウザ（Chrome, Firefox）、オペレーティングシステム（Linux, Android）、そしてデスクトップ出版ソフトウェアに浸透しました。

フォントはもはや単なる受動的な画像の集まりではありません。それは自律的な計算能力と文脈判断力を持つ「生きたソフトウェア」であり、数千年に及ぶ人類の書記文化の美と叡智を未来へと継承する架け橋なのです。

*本章の全訳および技術校正は ヴワル魔法図書館（Voile Magic Library）文献翻訳工房 により完了しました。*
