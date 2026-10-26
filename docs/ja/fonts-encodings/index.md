---
title: 『フォントとエンコーディング：Unicode と高度な組版技術全解』
description: ヴワル魔法図書館 蔵書典籍：『フォントとエンコーディング：Unicode と高度な組版技術全解』（Fonts & Encodings / 字体与编码 / 字體與編碼）。ヤニス・ハラランブス（Yannis Haralambous）記念碑的大著日本語学術訳・図版完全収録版。
head:
  - - meta
    - name: keywords
      content: フォントとエンコーディング, 字体与编码, 字體與編碼, Fonts & Encodings, Yannis Haralambous, Unicode, OpenType, TrueType, Typography, 組版技術, 文字コード, フォント設計
---

# 蔵書典籍 ·『フォントとエンコーディング：Unicodeから高度な組版技術まで』
### Fonts & Encodings: From Unicode to Advanced Typography and Everything in Between
**著者：ヤニス・ハラランブス 博士（Yannis Haralambous, Ph.D.）**  
*英訳監修：P. スコット・ホーン 博士（P. Scott Horne, Ph.D.） · 原著：O'Reilly Media 刊（ISBN 978-0-596-10242-5）*
*訳者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

> **「ホモ・サピエンス（*Homo sapiens*）とは、文字を記す種族である。書字のために人類が生み出してきた無数の道具の中で、最も新しく、かつ最も精緻な創造物がコンピュータにほかならない。それは読書具であり、筆記具であり、記憶媒体であり、データ交換の手段でもある……このデジタル書字空間において、エンコーディング（encoding）とフォント（font）は、本質的に異なりながらも分かち難く結びついた使命を担っている。エンコーディングは人間の概念的抽象（abstraction）から生じる純粋な思考の産物であり、フォントは書字記号の具象的な視覚的顕現、すなわち白黒のインクが織りなす図形的実体である。両者は陰と陽、天と地、理論と実践のごとく、デジタル世界において果てなき輪舞を踊り続けている。」**  
> —— ヤニス・ハラランブス（Yannis Haralambous）、『フォントとエンコーディング』序論より

---

## 典籍解題と学術的位置づけ

計算機科学と現代デジタル・タイポグラフィ（Digital Typography）の交錯する歴史において、ヤニス・ハラランブス（Yannis Haralambous）の『フォントとエンコーディング』（*Fonts & Encodings*）は、**当該分野において他の追随を許さない百科全書的「聖典」**として世界的に高く評価されています。

原著は全1,040ページ余におよび、フランス国立ブルターニュ高等情報通信学校（ENST Bretagne、現 IMT Atlantique）のハラランブス教授が十余年にわたり積み重ねた深遠な学術的探究と工学実践の結晶です。本書は壮大かつ厳密な視野をもって、伝統的活版印刷の美学、OS低層の文字符号化、ベジェ曲線によるグリフのラスタライズ幾何数学、そして多言語複合文書組版エンジンの間に横たわる技術的断絶を打破しました。

1. **文字符号化体系（Character Encodings & Unicode）**：黎明期の軍用テレタイプ通信規格 FIELDATA、ASCII、EBCDIC、ISO 8859 系列、東アジア（日中韓）の初期2バイトコードページから、現代の Unicode 5.0 の基本哲学、プレーン（面）構造、双方向テキスト組版アルゴリズム（Bidi）、正規化形式（Normalization Forms）、複雑文字の合字・連筆規則までを網羅；
2. **デジタルフォント工学と低層フォーマット（Digital Font Technologies）**：初期のビットマップフォント、ドナルド・クヌース（Donald E. Knuth）の METAFONT 方程式、Adobe PostScript Type 1 の輪郭とヒンティング（Hinting）命令から、TrueType（TTF）の低層仮想マシン・バイトコード命令（Twilight Zone、CVT、FDIR）、OpenType 高度タイポグラフィ機能テーブル（GSUB / GPOS / GDEF / BASE / JSTF）、Apple 高度組版技術（Apple Advanced Typography, AAT）の有限状態オートマトン・エンジンまでを詳解；
3. **学際的組版ソフトウェアと組版数学（Typographic Software & Mathematics）**：Donald Knuth による TeX 組版マクロ体系と $\Omega$（Omega）多言語組版エンジン、PostScript ページ記述言語の低層ストリーム解釈系、PDF 仕様内部のグリフ参照ストリーム、そしてピエール・ベジェ（Pierre Bézier）による3次パラメトリック曲線とバーンスタイン基底多項式（Bernstein Basis Polynomials）の厳密な数学的証明まで；

これらすべてを有機的に融合し、歴史的変遷の文献考証と産業標準の低層工学仕様を完璧に兼ね備えた不朽の古典です。

---

## 著者および学術的背景

### 著者：ヤニス・ハラランブス 博士（Yannis Haralambous, Ph.D.）

* **学術的地位**：高名な計算機科学者、応用数学者、デジタル・タイポグラフィおよび計算言語学の世界的権威。フランス国立ブルターニュ高等情報通信学校（École Nationale Supérieure des Télécommunications de Bretagne、現 IMT Atlantique）計算機科学科終身教授。
* **来歴と数学的基礎**：ギリシャ出身。若くしてフランスへ留学し、リール第1大学（Université de Lille I）にて純粋数学の博士号を取得。抽象幾何学およびトポロジーにおける卓越した数理的素養が、後に文字輪郭のベクトル幾何、多項式スプライン補間、複雑書字系オートマトンの先駆的研究を結実させる基盤となりました。
* **TeX および $\Omega$（Omega）システムの開発**：1990年代初頭、Donald Knuth の古典的 TeX システムが非ラテン文字（ギリシャ文字、アラビア文字、ヘブライ文字、サンスクリット、チベット文字等）の処理や8ビット文字セットの制約に直面した際、ハラランブスは英計算機科学者ジョン・プレイス（John Plaice）とともに革新的な **$\Omega$（Omega）組版システム** を共同開発しました。Omega は16/32ビット Unicode のネイティブ対応をいち早く実現し、「有限状態テキスト変換プロセス」（Omega Translation Processes, OTPs）を導入して、複雑書字系の双方向組版と文脈依存異体字処理のパラダイムを一新しました。
* **国際多言語組版の標準化**：Unicode コンソーシアム専門委員、国際タイポグラフィ協会（ATypI）理事、TeX ユーザーグループ（TUG）幹部を歴任。ポリトニック・ギリシャ語アクセント記号、シリア文字、ウルドゥー文字、現代東アジア表意文字の組版アルゴリズムにおいて、国際標準化に計り知れない貢献を果たしました。
* **本書の成立経緯**：本書は元来フランス語で執筆され、2004年に O'Reilly France より『*Fontes & codages*』として刊行されました。その圧倒的な学術的完成度と前例のない工学的深度を受け、米国オライリー本社が計算言語学・学術翻訳の第一人者 P. スコット・ホーン博士を招聘。3年の歳月を費やして全編を英訳・大幅拡充し、Unicode 5.0 および最新の OpenType / AAT 工業規格へと全面改稿の上、2007年に英語版初版が公刊されました。
*訳者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

## 蔵書全編目録ナビゲーション

::: tip 典籍目録
各編章をクリックすると、完全日本語訳の本文および高精細図版を閲覧できます：
:::

### 序論および基礎編
* **[序論 · 探求篇：文字の解剖学、活版印刷、デジタルモデルと知識体系体系図](./introduction)**  
  *原著：Yannis Haralambous* —— 全書の基盤概念を確立。文字（character）とグリフ（glyph）の二元性を論じ、文字の解剖学各部名称を詳解（高精細図版 Figure 0-1）；アルファベット「E」の6大幾何学的記述（パチョーリ、デューラー、トリー、ロワ委員会図版 Figure 0-2）；ディドロ百科全書に見る活版組版機構（18世紀の活字ケースとステッキ Figure 0-3〜0-5）；デジタル組版のベースライン、送り幅ベクトル、カーニング；全4部構成の知識体系図（Figure 0-6）を俯瞰。

---

### 第一部：符号化と文字集合（Part I）
* **[第1章：前Unicode時代の符号化体系（FIELDATAからISO 8859まで）](./chapter-1)**  
  軍用野戦通信 FIELDATA から ASCII、EBCDIC、ISO 646、ISO 8859-1〜16 各文字集合、ISO 2022 エスケープ・シーケンス、日中韓（CJK）2バイト符号化（Shift_JIS、EUC-JP、GB 2312、Big5）に至る歴史的変遷を総括。
* **[第2章：文字、グリフ、バイト（Unicode序説と基本構造）](./chapter-2)**  
  Unicode の基本理念、BMP（基本多言語面）および SMP/SIP/SSP 各プレーンの構造、UTF-8 / UTF-16 / UTF-32 のバイト変換アルゴリズム、文字とグリフの概念的境界を厳密に解明。
* **[第3章：Unicode文字プロパティ体系](./chapter-3)**  
  General Category（一般カテゴリ）、Bidi_Class、Canonical Combining Class（結合クラス）、Decomposition_Type、East Asian Width（全角半角幅）など、Unicode 文字プロパティの全容。
* **[第4章：正規化形式、双方向テキスト（Bidi）と東アジア文字](./chapter-4)**  
  NFC / NFD / NFKC / NFKD の4大正規化形式の数学的性質；アラビア語・ヘブライ語の双方向組版アルゴリズム（UBA）；日中韓表意文字統合（Han Unification）の歴史的背景と異体字セレクタ。
* **[第5章：Unicode実践と文字入力ツール](./chapter-5)**  
  Mac OS X、Windows、X Window/Linux 各環境における文字パレット、BabelMap、キーボード配列カスタマイズ（MSKLC、Keyman）の実践的運用。

---

### 第二部：OSにおけるフォント管理（Part II）
* **[第6章：Macintosh環境におけるフォント管理](./chapter-6)**  
  Classic Mac OS の FONT / NFNT リソースから Mac OS X の dfont、Font Book（フォントブック）、Core Text アーキテクチャへの進化。
* **[第7章：Windows環境におけるフォント管理](./chapter-7)**  
  Windows 3.1 から XP/Vista に至るフォントディレクトリ、GDI レンダリングパイプライン、Uniscribe 複合テキスト整形エンジン。
* **[第8章：X WindowとUnix環境におけるフォント管理](./chapter-8)**  
  XLFD（X Logical Font Description）、コアXフォントプロトコル、Xft および Fontconfig による現代的フォント検索・照合機構。

---

### 第三部：組版エンジンとWebフォント技術（Part III）
* **[第9章：TeXおよびOmegaシステムのフォント技術](./chapter-9)**  
  TFM（TeX Font Metric）、仮想フォント（VF）、フォントインストールパイプライン、Omega 組版エンジンによる OTP（Omega Translation Process）ストリーム。
* **[第10章：Webページ組版技術（Webフォントの起源とCSS標準）](./chapter-10)**  
  HTML `<font>` タグの栄枯盛衰；CSS `@font-face` 仕様；Bitstream TrueDoc（PFR）、Microsoft WEFT（EOT）、SVG フォント、WOFF への道標。

---

### 第四部：書体設計学と高度な組版（Part IV）
* **[第11章：ラテン文字書体の歴史的変遷と分類学](./chapter-11)**  
  グーテンベルクのテクスチャー体からジェンソン、ガラモン、カズロン、バスカヴィル、ボドニ、ディド、サンセリフの登場まで；Thibaudeau、Vox-ATypI、DIN 16518、Alessandrini、PANOSE 各分類法。
* **[第12章：フォント設計と編集の実践](./chapter-12)**  
  Fontographer、FontStudio、FontLab、FontForge による輪郭設計、グリフメトリクス調整、マルチプルマスター（MM）技術、スキャン画像からの自動トレース工学。
* **[第13章：ラスタライズ最適化とヒンティング技術](./chapter-13)**  
  低解像度画面におけるドロップアウト制御、アライメントゾーン、PostScript ヒント置換、TrueType デルタ命令によるピクセル最適化。
* **[第14章：高度な組版機能（OpenTypeとAAT）](./chapter-14)**  
  OpenType GSUB/GPOS テーブル、VOLT によるフィーチャー記述；Apple Advanced Typography（AAT）のモーフ（morx）テーブルと有限状態機械駆動の自動コンテキスト置換。

---

### 第五部：技術付録（Part V）
* **[付録全編：デジタルフォント底層フォーマット、仮想マシンと数学原理完全リファレンス](./appendices)**  
  * **付録 A**：Macintosh、Windows、X11/BDF、TeX PK ビットマップフォントフォーマット
  * **付録 B**：Adobe Font Metrics（AFM / AMFM）完全仕様
  * **付録 C**：PostScript Type 1、Type 2 Charstring、CFF、CID-keyed フォント構造
  * **付録 D**：TrueType / OpenType 各テーブル（head, hhea, hmtx, maxp, OS/2, cmap, glyf, GSUB, GPOS 等）詳細仕様
  * **付録 E**：TrueType 仮想マシン命令セット（グラフィックス状態、スタック操作、ポイント移動、デルタ命令）
  * **付録 F**：METAFONT 言語仕様、ペンモデル、数式による書体定義
  * **付録 G**：ベジェ曲線、バーンスタイン多項式、ド・カステリョのアルゴリズム、幾何学的性質の数学的厳密証明
