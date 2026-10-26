# -*- coding: utf-8 -*-
"""
Expand Chapter 14 to full unabridged depth (Japanese).
"""
import sys

target_path = r"docs/ja/fonts-encodings/chapter-14.md"

content = r"""# 第 14 章：フォントに知性を宿す：高度組版技術
### Chapter 14: Enriching Fonts: Advanced Typography
選書『Fonts & Encodings』第 549–598 頁
*訳者：[Lycoris <lycorismisaka@gmail.com>](mailto:lycorismisaka@gmail.com)*

---

本章のタイトルが指し示すのは、OpenType および AAT フォントにおける「高度組版機能（Advanced Typographic Features）」です。技術的本質において、これらの機能はマイクロソフト（Microsoft）、アドビ（Adobe）、そしてアップル（Apple）が従来の TrueType 形式の上に拡張・追加した一連の専用データテーブルです。私たちは 2 つの新しいフォント形式の台頭を目の当たりにしました：Adobe と Microsoft が共同策定した **OpenType**（かつては TrueType Open と呼ばれた）、そして Apple が開発した **AAT**（Apple Advanced Typography、かつては TrueType GX と呼ばれた）です。

これらのデータテーブルにより、デジタルフォントは地球上の多様な書字体系の組版の試練に真に対峙する力を初めて獲得しました。これら「高機能」スマートフォントの中核的特質は、**グリフの幾何学的配置、文脈依存置換、そして微細な位置調整ルールが OS 底層にハードコードされるのではなく、フォントファイル自身の内部に完全にパッケージ化・固定化されている**という点にあります。

この設計は、テキストレンダリングエンジンによるフォントの読み込みや解釈をより複雑で重厚なものにしますが、同時にフォントデザイナーに前例のない自由と主権をもたらします。デザイナーはフォントの動的組版挙動に対して完全な責任と裁量を持つことができます。既存の成熟した組版ルールを採用することも、それらを自由に変更することも、あるいは未知の新文字体系のために全く新しい組版ロジックを発明することさえ、OS のアップデートを待つことなく実現できるのです。

---

## 1. 高度組版体系全景序論（Introduction）

### 1.1 文字からグリフへ：テキストシェイピング（Text Shaping）の動的変容

デジタル組版において、**文字（Character）**と**グリフ（Glyph）**は厳格に区別されなければなりません：
- **文字**は抽象的な情報単位（Unicode によって一意のコードポイントが付与される）であり、テキストの保存、検索、語彙解析の唯一の主体です；
- **グリフ**は具体的な視覚的グラフィック表現です。

西洋の基本的なアルファベット体系では両者は単純な 1 対 1 対応を示すことが多いですが、東洋や中東の書字体系では、文字とグリフの対立は日常的な組版の前提となります：
- アラビア文字では文字が筆記体として連結され、語頭・語中・語末・独立形の各位置に応じて全く異なる字形を採ります；
- インド系諸言語や東南アジア文字では、複数の子音と母音が複雑に絡み合い、視覚的な合字塊を形成します；
- 洗練された欧文古典組版においても、リガチャ（合字）、オールドスタイル数字、真のスモールキャピタル、そして前後の文字に応じて姿を変える文脈依存異体字が、同一の文字に多様なグリフの衣をまとわせます。

高度組版エンジンにおいて、入力された文字列は**テキストシェイピング（Text Shaping）**と呼ばれる多段階の動的パイプラインを通過します：

```
[生の Unicode 文字ストリーム] 
        │
        ▼ (cmap テーブルによるマッピング)
[公称グリフシーケンス (Nominal Glyphs)] 
        │
        ▼ (GSUB / morx テーブル：文脈依存置換エンジン)
[配置・置換後のグリフシーケンス (Substituted Glyphs)] 
        │
        ▼ (GPOS / kerx テーブル：微細幾何配置エンジン)
[正確な 2 次元変位 (X, Y, Advance) を持った最終グリフストリーム]
```

### 1.2 高度組版機能の分類全景

OpenType と AAT は、フォントの持つ組版能力を大きく 2 つの操作カテゴリに分類します：**グリフ置換（Glyph Substitution）** と **グリフ位置調整（Glyph Positioning）** です。

#### 1. グリフ置換の中核的形態（GSUB）
- **単一置換（Single Substitution）**：1 つのグリフを別のグリフへ置換（スモールキャピタル化、オールドスタイル数字への置換など）；
- **合字置換（Ligature Substitution）**：連続する複数のグリフを 1 つの複合グリフへ統合（`f` + `i` $\to$ `fi`、`c` + `t` $\to$ `ct`）；
- **複数置換（Multiple Substitution）**：1 つのグリフを複数の構成要素グリフへ分解（インド系複合合字の分解など）；
- **代替置換（Alternate Substitution）**：1 つの文字に対して複数の視覚的候補グリフを提供（Zapfino の華麗な 9 種類もの「d」異体字など）；
- **文脈依存置換（Contextual Substitution）**：特定の文脈環境下でのみ発動する置換（小文字「d」と「s」が隣接した際に、突き出た連結ストロークを自動除去するなど）。

#### 2. 微細幾何位置調整の操作形態（GPOS）
- **単一位置調整（Single Adjustment）**：特定グリフの座標微調整（オールキャピタル環境下で括弧の位置を上方へシフトするなど）；
- **ペア位置調整（Pair Adjustment / Kerning）**：隣接するグリフペア間の字間微調整；
- **ベースに対するマーク配置（Mark-to-Base Attachment）**：基底文字とダイアクリティカルマーク（アクセント記号）に設けた光学アンカー（Anchors）を一致させ、マークを完璧に吸着配置；
- **マークに対するマーク配置（Mark-to-Mark Attachment）**：アクセント記号の上にさらに別のアクセント記号を多段スタック配置（国際音声記号や多調ギリシャ語など）；
- **合字に対するマーク配置（Mark-to-Ligature Attachment）**：合字（`ffi` など）の各構成パーツの上に個別にアンカーを設け、複数のマークを正確に配置；
- **筆記連結配置（Cursive Attachment）**：アラビア文字やスクリプト書体において、先行グリフの出筆アンカー（Exit）と後続グリフの入筆アンカー（Entry）をシームレスに溶接。

#### 3. 代表的な標準機能タグ（Feature Tags）
4 文字のタグで識別されます：
- `smcp`（スモールキャピタル）、`c2sc`（大文字からスモールキャピタル）；
- `onum`（オールドスタイル数字）、`lnum`（ライニング数字）、`pnum`（プロポーショナル数字）、`tnum`（等幅数字）；
- `zero`（スラッシュ付きゼロ）；
- `frac`（斜線分数）、`afrc`（水平線分数）；
- `liga`（標準リガチャ）、`dlig`（任意リガチャ）、`hlig`（歴史的リガチャ）；
- `hist`（歴史的異体字，長S：ſ など）；
- `calt`（文脈依存異体字）、`salt`（スタイルセット異体字）；
- `kern`（カーニング）、`mark`（マーク配置）、`mkmk`（マーク間配置）。

---

## 2. FontLab における OpenType テーブルと AFDKO 言語の管理（Managing OpenType Tables in FontLab）

フォント制作の業界標準ツール FontLab Studio 5 は、Adobe の **AFDKO（Adobe Font Development Kit for OpenType）** 構文をネイティブ統合しており、宣言的な**機能定義言語（Feature Definition Language, `.fea`）**を用いて高度組版を記述します。

### 2.1 機能定義言語（AFDKO）の基本構文

#### 1. グリフクラス（Glyph Classes）の定義
角括弧 `[...]` と `@` プレフィックスにより、意味論的な文字グループを定義します：

```fea
@Uppercase = [A-Z];
@SmallCaps = [A.sc-Z.sc];
@Vowels = [a e i o u];
@AccentedVowels = [aacute eacute iacute oacute uacute agrave egrave igrave ograve ugrave];
@AllVowels = [@Vowels @AccentedVowels];
```

#### 2. 書字系・言語と機能構造（Languagesystem）
ファイル先頭で言語システムを宣言します：

```fea
languagesystem DFLT dflt;
languagesystem latn dflt;
languagesystem latn DEU ;
languagesystem latn ROM ;
languagesystem latn ENG ;
```

機能ブロック内では、言語ごとのルール上書きが可能です：

```fea
feature foo {
    script latn;
    language DFLT;
    sub s cedilla by s.cedilla;

    language DEU;
    sub germandbls by S S;

    language ENG excludeDFLT;
    # 英語環境ではデフォルトルール（DFLT）を完全破棄し、専用ルールのみを適用
    sub a by a.alt;
} foo;
```

#### 3. 名前付きルックアップとフラグ（Lookups and Lookupflags）
```fea
lookup CustomLigatures {
    lookupflag IgnoreBaseGlyphs, IgnoreMarks;
    sub f_i' j by f_i_j;
} CustomLigatures;
```
`lookupflag` により、基底文字（`IgnoreBaseGlyphs`）、合字（`IgnoreLigatures`）、マーク（`IgnoreMarks`）のスキップが自在に指定できます。

#### 4. 置換ルール全解（GSUB）

- **単一置換**：`sub @Uppercase by @SmallCaps;`
- **代替置換**：`sub e from [e eacute egrave ecircumflex];`
- **合字置換**：`sub f i by f_i;`
- **文脈依存置換とアポストロフィ記法**：
  アポストロフィ `'` が付いたグリフのみが実際に置換される対象となり、アポストロフィのないグリフは前後の文脈環境（Context）として機能します：
  ```fea
  sub @letters d' @word_boundaries by d.fina;
  ```
- **除外ルール（Ignore Rules）**：
  大文字 `TEX` をロゴ合字 `T_e_X` に置換しつつ、`TEXT` や `CONTEXT` を破壊しないための実戦テクニック：
  ```fea
  feature calt {
      ignore sub [A-Z Eacute] T' E' X', T' E' X' [A-Z Eacute];
      sub T' E' X' by T_e_X;
  } calt;
  ```

#### 5. 微細幾何配置全解（GPOS）

値レコード（Value Record）は 4 つの整数値で構成されます：

$$\langle xPlacement \quad yPlacement \quad xAdvance \quad yAdvance \rangle$$

Haralambous は本章で代表的な 5 つの幾何挙動を整理しています：
1. `<x y 0 0>`：グリフ原点のみを移動し、送り幅は一切変更しない；
2. `<0 0 x 0>`：原点はそのままに、送り幅のみを $x$ 増加させる；
3. `<x 0 x 0>`：原点と送り終点を同時に $x$ 平行移動；
4. `<0 y 0 0>`：原点を下方に移動するが、送り終点はベースラインに留まる；
5. `<0 y 0 y>`：原点と送り終点の双方を下方に移動（後続文字すべてがその深さで組まれる）。

- **クラスベースカーニング**：
  ```fea
  feature kern {
      pos [A Aacute Agrave Acircumflex Atilde Adieresis Aring] [v w y] -50;
  } kern;
  ```
- **合字上の多重マーク配置**：
  ```fea
  pos ligature p_r_e_t
      <anchor 120 700> mark @TOP_MARKS
      ligComponent
      <anchor 250 700> mark @TOP_MARKS
      ligComponent
      <anchor 380 700> mark @TOP_MARKS
      ligComponent
      <anchor 500 700> mark @TOP_MARKS;
  ```

#### 6. 2 つの重要特例：`aalt` と `size`
- **`aalt`**：フォント内の全異体字をパレットに集約；
- **`size`**：オプティカルサイズメタデータ（設計サイズ、ファミリ番号、適用範囲）。

---

## 3. Microsoft VOLT による実戦（Managing OpenType Tables in VOLT）

Microsoft の **VOLT（Visual OpenType Layout Tool）** は、アラビア文字やインド系複雑文字のための究極のツールです。
- TrueType バイナリ（`.ttf`）を直接操作；
- 階層構造：$\text{Scripts} \to \text{Languages} \to \text{Features} \to \text{Lookups}$；
- ビジュアルアンカー配置（Base と Mark の対話的スナップ）；
- Uniscribe と同一のレンダリングを再現するプルーフテスト機能。

---

## 4. FontForge における OpenType テーブル管理（Managing OpenType Tables in FontForge）

FontForge は、OpenType のデータ構造を直接グラフィカルにマッピングします。
- `Element > Font Info > Lookups` による GSUB / GPOS の一元管理；
- グリフ描画キャンバス上での直接アンカー配置；
- クラス別カーニング表（Kern by Classes）；
- 連鎖文脈依存ルックアップ（Chained Contextual Lookups）。

---

## 5. Apple Advanced Typography（AAT）と状態遷移オートマトン（Managing AAT Tables in FontForge）

### 5.1 OpenType と AAT の設計哲学の対比

| 比較軸 | OpenType 体系 | Apple Advanced Typography (AAT) 体系 |
| :--- | :--- | :--- |
| **中核エンジン** | パターンマッチング型静的宣言テーブル（GSUB/GPOS） | **有限状態自動機（Finite State Automata, FSM）** |
| **レンダラ負荷** | **極めて重厚**：言語ごとの状態機械を OS 側にハードコード | **極めて軽量**：Core Text はフォント内蔵の状態機械を実行する汎用 VM |
| **中核テーブル** | `GSUB`, `GPOS`, `GDEF`, `BASE` | **`morx`**, **`kerx`**, **`feat`**, **`trak`** |
| **新言語の拡張性** | OS レンダラの改修が必須 | **完全内蔵型**：古い Apple デバイスでも新文字が即座に動作可能 |

### 5.2 AAT の 4 大状態機械

FontForge の `Element > Font Info > Mac SM` で設計可能な 4 大オートマトン：
1. **グリフ並べ替え（Glyph Rearrangement）**：インド系文字における母音の先行配置（例：`KGPTHr` $\to$ `rKGPTH`）；
2. **文脈置換状態機械（Contextual Substitution）**：連字や語尾異体字の状態遷移表；
3. **グリフ動的挿入（Glyph Insertion）**：アラビア語カシーダ（引き伸ばし線）の不可視挿入；
4. **文脈カーニング（Contextual Kerning / `kerx`）**：最大 8 グリフをスタックにプッシュし、ポップ時に $n-1$ 個のカーニングを一括適用する強力な多文字間位置調整。

---

## 6. 結論と現代組版エンジンへの展望（Conclusions and Modern Outlook）

高度組版技術の進化は、人類の文字文化とデジタル計算機の深遠な融合の結晶です。
現代のオープンソースエコシステムでは、**HarfBuzz** テキストシェイピングエンジンが OpenType の宣言的レイアウトと AAT のオートマトンアルゴリズムを高次元で統合し、世界中の数十億台のデバイス上で、人類のすべての文明の書字体系の美を精緻に描き出し続けています。
"""

with open(target_path, 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully written {target_path}, length: {len(content)} chars.")
