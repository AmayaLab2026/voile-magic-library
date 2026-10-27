---
title: 第12章 · フォントの編集と作成
description: ヤニス・ハラランブス博士『Fonts & Encodings』第12章：Macromedia Fontographer、Letraset FontStudio、FontLab Studio の操作体系、ベジェスプライン曲線幾何学、3次・2次ベジェ相互昇階・細分近似アルゴリズム、Python による字形自動生成バッチ処理、FontForge SFD プレーンテキスト形式、ラフ・レヴィアン（Raph Levien）の Spiro オイラー螺旋曲率連続性理論、ScanFont／Potrace によるラスタ画像自動トレース（Freeman 鎖状符号、Douglas-Peucker 簡略化、最小二乗法フィッティング）、および PostScript / CFF ヒンティング・アライメント領域の完全解説。
---

# 第12章 · フォントの編集と作成
### Chapter 12: Editing and Creating Fonts
**著者：ヤニス・ハラランブス 博士（Yannis Haralambous, Ph.D.）**  
*『Fonts & Encodings』原著第 445–508 頁より*

*翻訳者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

フォントの創造は、純粋な視覚的リズムと古典的プロポーションを追求する造形芸術であると同時に、厳密な微分幾何学、多項式スプライン近似、離散ラスタトポロジー、そして低レイヤのバイナリデータ構造の上に構築された現代ソフトウェア工学でもあります。

タイプデザイナーにとって、グリフは単なる静的なイラストではなく、あらゆる表示解像度においてリアルタイムに描画可能な動的数学輪郭モデルです。本章では、Fontographer、FontStudio、そして業界標準の FontLab Studio の操作トポロジーを解剖し、3次・2次ベジェ曲線の代数変換を導出し、オープンソースの雄 FontForge の SFD 構造と Spiro オイラー螺旋理論を詳解し、Python スクリプトおよび画像ベクタライズ追跡アルゴリズムの全貌を明らかにします。

---

## 第1部：デジタルフォント設計ツールの進化と操作トポロジー

::: tip Macromedia Fontographer の Mac OS X 画面（Figure 12-1）
![Macromedia Fontographer の Mac OS X 画面（Figure 12-1）](/images/fonts-encodings/fig12-1.png)
*Macromedia Fontographer の Mac OS X 画面（Figure 12-1）*
:::

*図 12-1：Mac OS X プラットフォームにおける Macromedia Fontographer のフォントウィンドウ。16進数文字順に並んだセルに、現在のフォントサイズでの各グリフのレンダリング縮小プレビューがリアルタイムに表示される。*

### 1. 初期の先駆的フォントエディタ：Fontographer と FontStudio

1980年代半ば、Macintosh と Adobe PostScript の結合により、PC 上での高品位ベクタフォント設計が可能になりました：
* **Macromedia Fontographer（図 12-1）**：Altsys 社が開発。ベジェ曲線をデスクトップフォント産業に導入し、フォントウィンドウ（全体一覧）とグリフウィンドウ（個別編集）の2層操作モデルを確立；
* **Letraset FontStudio（図 12-2）**：Mac OS 9 時代の高機能スイート。複合輪郭ブラシツール、TrueType の2次放物線編集、アンチエイリアスグレープレビューを先駆的に提供。

::: tip Letraset FontStudio の Mac OS 9 グリフ編集ウィンドウ（Figure 12-2）
![Letraset FontStudio の Mac OS 9 グリフ編集ウィンドウ（Figure 12-2）](/images/fonts-encodings/fig12-2.png)
*Letraset FontStudio の Mac OS 9 グリフ編集ウィンドウ（Figure 12-2）*
:::

*図 12-2：Letraset FontStudio（Mac OS 9）のグリフ編集画面。デカルト座標系上での閉路パス描画、多様な制御点ツールとブラシフィッティング機能を提供する。*

### 2. 現代の工業標準：FontLab Studio

FontLab Studio（第4・第5世代）は、高度な数学的整合性と OpenType 機能サポートにより、プロの書体設計現場でデファクトスタンダードとなりました。フォントウィンドウでは、多言語環境に対応するため4つの表示モードを備えています：

::: tip FontLab の4つの表示モード（Figure 12-3, 12-4, 12-5, 12-6）
![FontLab ウィンドウ Names モード（Figure 12-3）](/images/fonts-encodings/fig12-3.png)
*FontLab ウィンドウ Names モード（Figure 12-3）*
:::

*図 12-3：FontLab ウィンドウの Names モード。PostScript グリフ標準名マッピングを直接確認可能。*

::: tip FontLab ウィンドウ Pages モード（Figure 12-4）
![FontLab ウィンドウ Pages モード（Figure 12-4）](/images/fonts-encodings/fig12-4.png)
*FontLab ウィンドウ Pages モード（Figure 12-4）*
:::

*図 12-4：FontLab ウィンドウの Pages モード。256文字単位のコードページごとにグリフ群を管理。*

::: tip FontLab ウィンドウ Ranges モード（Figure 12-5）
![FontLab ウィンドウ Ranges モード（Figure 12-5）](/images/fonts-encodings/fig12-5.png)
*FontLab ウィンドウ Ranges モード（Figure 12-5）*
:::

*図 12-5：FontLab ウィンドウの Ranges モード。Unicode 公式ブロックごとに展開し、多言語カバレッジを一元把握。*

::: tip FontLab ウィンドウ Index モード（Figure 12-6）
![FontLab ウィンドウ Index モード（Figure 12-6）](/images/fonts-encodings/fig12-6.png)
*FontLab ウィンドウ Index モード（Figure 12-6）*
:::

*図 12-6：FontLab ウィンドウの Index モード。低レイヤ GID（Glyph ID）順に配列され、OpenType の `cmap` 整合性を検証。*

### 3. グローバルメトリクスとメタデータ：Font Info

グリフ制作に先立ち、Font Info ウィンドウで物理メトリクスと知的所有権メタデータを定義します：

::: tip Font Info メタデータと著作権タブ（Figure 12-7）
![Font Info メタデータと著作権タブ（Figure 12-7）](/images/fonts-encodings/fig12-7.png)
*Font Info メタデータと著作権タブ（Figure 12-7）*
:::

*図 12-7：FontLab の Font Info ウィンドウにおける Names、Copyright、OpenType パラメータ設定画面。*

::: tip Font Info の寸法とコードページタブ（Figure 12-8）
![Font Info の寸法とコードページタブ（Figure 12-8）](/images/fonts-encodings/fig12-8.png)
*Font Info の寸法とコードページタブ（Figure 12-8）*
:::

*図 12-8：Font Info における Key dimensions（基本寸法）、Supported codepages、Supported Unicode ranges の設定画面。*

---

## 第2部：3次および2次ベジェ曲線の数学的本質と代数変換

::: tip PostScript と TrueType の曲線制御点比較（Figure 12-11）
![PostScript と TrueType の曲線制御点比較（Figure 12-11）](/images/fonts-encodings/fig12-11.png)
*PostScript と TrueType の曲線制御点比较（Figure 12-11）*
:::

*図 12-11：PostScript（3次）と TrueType（2次）のグリフ輪郭微視的対比。TrueType では連続するオフカーブ点の中点が暗黙のオンカーブ点として計算される。*

### 1. 3次ベジェ曲線の微分幾何学

始点 $\mathbf{P}_0$、第1制御ハンドル $\mathbf{P}_1$、第2制御ハンドル $\mathbf{P}_2$、終点 $\mathbf{P}_3$ による3次バーンスタイン基底多項式展開：

$$\mathbf{B}(t) = (1-t)^3 \mathbf{P}_0 + 3(1-t)^2 t \mathbf{P}_1 + 3(1-t) t^2 \mathbf{P}_2 + t^3 \mathbf{P}_3, \quad t \in [0, 1]$$

その1次導関数（速度ベクトル・ホドグラフ）は2次ベジェ多項式となります：

$$\mathbf{B}'(t) = 3(1-t)^2 (\mathbf{P}_1 - \mathbf{P}_0) + 6(1-t)t (\mathbf{P}_2 - \mathbf{P}_1) + 3t^2 (\mathbf{P}_3 - \mathbf{P}_2)$$

2次導関数（加速度ベクトル）：

$$\mathbf{B}''(t) = 6(1-t)(\mathbf{P}_2 - 2\mathbf{P}_1 + \mathbf{P}_0) + 6t(\mathbf{P}_3 - 2\mathbf{P}_2 + \mathbf{P}_1)$$

任意点 $t$ における2次元スカラー曲率 $\kappa(t)$：

$$\kappa(t) = \frac{x'(t) y''(t) - y'(t) x''(t)}{\big( x'(t)^2 + y'(t)^2 \big)^{3/2}}$$

### 2. 2次ベジェ曲線

始点 $\mathbf{P}_0$、単一のオフカーブハンドル $\mathbf{P}_1$、終点 $\mathbf{P}_2$ による2次バーンスタイン多項式：

$$\mathbf{B}(t) = (1-t)^2 \mathbf{P}_0 + 2(1-t) t \mathbf{P}_1 + t^2 \mathbf{P}_2, \quad t \in [0, 1]$$

その1次導関数：

$$\mathbf{B}'(t) = 2(1-t)(\mathbf{P}_1 - \mathbf{P}_0) + 2t(\mathbf{P}_2 - \mathbf{P}_1)$$

2次導関数（定数ベクトル）：

$$\mathbf{B}''(t) = 2(\mathbf{P}_2 - 2\mathbf{P}_1 + \mathbf{P}_0) = \text{常数向量}$$

### 3. 2次から3次への昇階代数（Degree Elevation）

TrueType から PostScript への変換は**厳密に可逆・無損失**です：

$$\mathbf{Q}_0 = \mathbf{P}_0, \quad \mathbf{Q}_1 = \mathbf{P}_0 + \frac{2}{3}(\mathbf{P}_1 - \mathbf{P}_0), \quad \mathbf{Q}_2 = \mathbf{P}_2 + \frac{2}{3}(\mathbf{P}_1 - \mathbf{P}_2), \quad \mathbf{Q}_3 = \mathbf{P}_2$$

---

## 第3部：グリフの物理メトリクスとマルチプルマスター（Multiple Master）

### 1. グリフ送り幅の力学モデル

$$\text{Advance Width} = \text{LSB} + \text{Bounding Box Width} + \text{RSB}$$

### 2. マルチプルマスター（Multiple Master, MM）

::: tip FontLab における Multiple Master 編集環境（Figure 12-9）
![FontLab における Multiple Master 編集環境（Figure 12-9）](/images/fonts-encodings/fig12-9.png)
*FontLab における Multiple Master 編集環境（Figure 12-9）*
:::

*図 12-9：FontLab の Multiple Master 統合画面。4つの極値マスター輪郭を同時に可視化・編集可能。*

任意の補間インスタンス生成式：

$$\mathbf{M}_{\text{instance}} = (1 - w) \mathbf{M}_{\text{master0}} + w \mathbf{M}_{\text{master1}}$$

::: tip 通常フォントから Multiple Master への生成ダイアログ（Figure 12-10）
![通常フォントから Multiple Master への生成ダイアログ（Figure 12-10）](/images/fonts-encodings/fig12-10.png)
*通常フォントから Multiple Master への生成ダイアログ（Figure 12-10）*
:::

*図 12-10：既存フォントを Multiple Master 空間へ拡張・昇格させる設定ダイアログ。*

---

## 第4部：Python によるフォント自動化バッチ処理

FontLab 組み込みの Python と `fl` オブジェクトモデルを活用したサイドベアリング一括補正、複合グリフ自動生成、および FontAudit 自動検証スクリプト。

---

## 第5部：オープンソースの雄——FontForge と Spiro オイラー螺旋

ジョージ・ウィリアムズ（George Williams）氏開発の FontForge によるプレーンテキスト SFD（Spline Font Database）構造と、ラフ・レヴィアン（Raph Levien）博士の Spiro（オイラー螺旋／クロソイド曲線）による曲率連続（$G^2/G^4$）造形理論：

$$\kappa(s) = \frac{d\theta}{ds} = a \cdot s + b$$


### 4. 縦組（Vertical Typesetting）と縦方向メトリクス制御

東アジアの諸文字（漢字・仮名・ハングル）以外では稀にしか用いられないものの、TrueType および PostScript Type 1 は低層規格において縦組を完全サポートしている。そのためには、フォント内部に網羅的な**縦方向メトリクスデータ（Vertical Metrics）**、すなわち各グリフの縦方向送り幅（Vertical Set-widths）と縦方向カーニング対（Vertical Kerning Pairs）が格納されていなければならない。

フォントエンジニアにとって、縦組は悪夢のような難題である：ディスプレイ表示やグラフィックスシステムの座標系は、ほぼ例外なく左から右への水平ベースラインを前提としている。水平組版においてグリフは共通のベースライン上に整列するが、縦組では文字の幾何学的または光学的中心を通る垂直中心線に沿って整列しなければならず、座標原点は左下ベースラインから上部中央点へとジャンプする！

グリフの縦方向送り幅とカーニングを直感的に生成・調整するため、FontForge はメトリクスウィンドウ（Metrics Window）上で専用の操作系を提供する：メトリクスウィンドウのメニューから **`View > Vertical`（表示 > 縦方向）** を選択するだけで、水平に並んでいたグリフ列が瞬時に垂直のテキスト柱へと切り替わる。デザイナーは水平モードと同様に、マウスドラッグによって文字間の垂直距離や送り幅を微調整し、縦組テキストのリズムとグレースケールを直感的に校正できる。

### 5. FontForge における CID フォントの高度な管理

東アジアの大規模な表意文字（CJK：数万字におよぶ漢字と仮名）プロジェクトにおいて、従来の 256 や 65,536 文字のプレーン構造では効率的なインデックスを担保できない。CID フォント（詳細は付録 C.7 節を参照）は、PostScript 初期の 256 文字制限を突破するためにアドビ社が開発した中核アーキテクチャである。

FontForge において CID フォントを開くか作成すると、メニューバーに専用の **`CID`** 特権メニューが出現し、極めて高度な産業用コマンド群が利用可能となる：
* **`CID > Flatten`（フラット化）**：現在の CID 階層構造を「消去」し、通常の単一フォント（Normal Font）へと統合変換する。これにより、複雑な CID フォントを直接通常の PostScript Type 1 や TrueType としてエクスポートできる；
* **`CID > Flatten By CMap`（CMap によるフラット化）**：上記と同様だが、フラット化後のグリフ割り当てを指定の外部 **CMap ファイル** に基づいて再マッピングする（アドビ公式の標準 CMap [26] を使用可能）；
* **`CID > Insert Font`（サブフォントの挿入）**：外部の単一フォントファイルを、現在の CID ファミリー内部へ新規サブフォント（Subfont）として直接組み込む；
* **`CID > Change Supplement`（補遺バージョンの更新）**：現在関連付けられている ROS（Registry-Ordering-Supplement）の補遺番号を上位互換版（例：`Adobe-Japan1-4` から `Adobe-Japan1-6`）へ更新する。

### 6. オートトレース（Autotracing）の理論的落とし穴と正当な適用領域

自動ベクター化ツールの紹介にあたり、Haralambous 氏は厳しい警告を発している：フォント制作においてオートトレースに過度に依存すると、ほぼ確実に低品質な文字が生み出される。機械的な輪郭検出アルゴリズムは、文字の深層に宿るプロポーションの美や幾何学的調和、そして低解像度レンダリングを支配するヒンティング（Hinting）の原理を一切理解できないからである。

しかしながら、以下の3つの特殊なユースケースにおいては、オートトレースの利用は極めて正当であり、生産性を飛躍的に向上させる：
1. **「自由設計」（Free Design）フォント**：厳密な幾何学的計算や古典的調和に縛られない、ポップアート体やグラフィティ、装飾的ファンタジー書体；
2. **手書き文字（Handwriting Fonts）**：自らの手書き肉筆による書籍組版を実現する場合。人間の手書き特有の有機的な揺らぎや不規則性を再現する上では、トレースアルゴリズムによる微小なノイズはむしろ生命感を与える；
3. **極めて高解像度のスキャン原図**：原図の解像度が極めて高く、エッジが極限までシャープでノイズが事実上無視できる場合。

FontForge における標準的なオートトレース手順は厳密な4工程から成る：
1. **下絵ビットマップのインポート**：輪郭ウィンドウで背景レイヤー（Background Layer）へ切り替え、`Edit > Import` でスキャン画像を読み込む；
2. **手動位置合わせとクリーンアップ**：背景レイヤー上で画像をスケーリングし、ベースラインとバウンディングボックスに厳密に合致させる（最も時間を要する工程）；
3. **オートトレースの実行**：**`Element > AutoTrace`（エレメント > オートトレース）** を実行。FontForge はバックグラウンドで外部のオープンソースエンジンを自動呼び出しする——ユーザーが `File > Preferences` で指定した設定に応じ、**Martin Weber 氏の `AutoTrace`** または **Peter Selinger 氏の `potrace`** がシームレスに駆動される！
4. **ベジェ制御点の手動補正**：FontForge のベクターツールを用い、アルゴリズムが生成した過剰な制御点を削減し、極値点へと正確に再配置する。

**プロの裏技**：**`Shift` キー** を押しながら `Element > AutoTrace` をクリックすると特殊な引数ダイアログが開き、エンジニアは `potrace` や `AutoTrace` に渡すコマンドラインパラメータ（コーナー閾値 `alphamax` や許容誤差 `opttolerance`）を直に指定してベクター品質を根本から制御できる！


---

## 第6部：ビットマップスキャンからベクタ輪郭追跡へ

::: tip ScanFont における自動文字領域分割（Figure 12-12）
![ScanFont における自動文字領域分割（Figure 12-12）](/images/fonts-encodings/fig12-12.png)
*ScanFont における自動文字領域分割（Figure 12-12）*
:::

*図 12-12：ScanFont におけるスキャン原稿のグリフ自動分離（Separation of glyphs）画面。*

::: tip ScanFont の自動トレースパラメータ設定（Figure 12-13）
![ScanFont の自動トレースパラメータ設定（Figure 12-13）](/images/fonts-encodings/fig12-13.png)
*ScanFont の自動トレースパラメータ設定（Figure 12-13）*
:::

*図 12-13：ScanFont のリアルタイム Autotracing パラメータ設定ダイアログ。*

最小二乗法フィッティングの残差エネルギー最小化目的関数：

$$E(\mathbf{P}_1, \mathbf{P}_2) = \sum_{k=0}^M \big\| \mathbf{B}(t_k; \mathbf{P}_0, \mathbf{P}_1, \mathbf{P}_2, \mathbf{P}_3) - \mathbf{S}_k \big\|^2$$

::: tip 手動作図と自動トレースのノード配置比較（Figure 12-14）
![手動作図と自動トレースのノード配置比较（Figure 12-14）](/images/fonts-encodings/fig12-14.png)
*手動作図と自動トレースのノード配置比較（Figure 12-14）*
:::

*図 12-14：手動描画（左）と各種自動トレースアルゴリズム（中・右）のノード生成比較。*

---

## 第7部：PostScript ヒンティング（Hinting）工学とアライメント領域

### 1. ブルーゾーン整列テーブル（BlueValues と OtherBlues）

$$\text{BlueValues} = [y_{b0}, y_{t0}, \quad y_{b1}, y_{t1}, \quad \dots]$$

### 2. ブルーゾーン解除スケール（BlueScale）

$$\text{Threshold Size} = \frac{1}{\text{BlueScale} \times (\text{Zone Height})}$$

---

第12章ではベジェ曲線による幾何輪郭生成を詳解しました。次章**第13章：フォントヒンティング（Hinting）機構**では、これら輪郭を低解像度ピクセル上で破綻なく描画するためのチューリング完全な仮想マシンとバイトコード命令体系を解き明かします。
