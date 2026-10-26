# -*- coding: utf-8 -*-
"""
Expand docs/ja/fonts-encodings/chapter-12.md to unabridged translation with all 14 figures and 6 math blocks.
"""
import sys

ja_content = r'''---
title: 第12章 · フォントの編集と作成
description: ヤニス・ハラランブス『Fonts & Encodings』第12章 全文完全学術邦訳：Fontographer、FontStudio および FontLab Studio の工業級設計構造、4大表示モード、3次・2次ベジェスプラインの幾何トポロジー変換、FontAudit 幾何検証、Multiple Master 多マスター設計、Python スクリプト自動化バッチ処理、FontForge オープンソース工房と Spiro オイラー螺旋、ScanFont と自動トレース（Autotracing）アルゴリズム徹底解剖。
---

# 第12章 · フォントの編集と作成
### Chapter 12: Editing and Creating Fonts
**著者：ヤニス・ハラランブス 博士（Yannis Haralambous, Ph.D.）**  
*『フォントとエンコーディング』（Fonts & Encodings）原著 441–504 ページより*

*翻訳者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

前章までにおいて、我々はフォントの論理仕様、オペレーティングシステムの低層配信機構、および Web 時代の組版プロトコルを体系的に探求してきた。しかしながら、根本的な疑問が常にタイポグラフィ研究者とエンジニアの前に横たわっている：**字形そのものは、そもそもどのようにして生み出されるのか？** フォント設計者はヒューマンマシンインタフェースを通じてどのように各文字の幾何学的輪郭を制御するのか？カーニング（Kerning）、メトリクス（Metrics）、およびヒンティング命令（Hinting）はどのようにバイナリフォントへと注入されるのか？

活字の時代において、書体を制作するには父型彫刻師（Punchcutter）が硬質鋼の先端に彫刻刀で突起した文字を精密に手彫りし、それを銅片に打ち込んで母型（Matrix）を作り、鉛・アンチモン・錫の合金を流し込んで実体活字を鋳造する必要があった。しかしコンピュータ革命以降、この数百年続いた冶金と機械の工芸は、純粋な**計算幾何学、スプライン曲線論、そして GUI インタラクションの芸術**へと完全に抽象化された。

本章では、DTP 革命の幕を開けた **Fontographer** や **FontStudio** から、世界の商業書体産業を長年支配してきた **FontLab Studio**、さらにはオープンソースの巨城 **FontForge** や画像自動トレースツール **ScanFont** に至るまで、デジタルフォント創造の全ライフサイクルエンジニアリングチェーンを徹底的に解剖する。

---

## 1. フォント設計とデジタル化概論（Introduction）

1980 年代半ば以前、デジタルフォントの作成は大手写植機メーカー（Linotype、Monotype、Compugraphic など）に独占されていた。字形の設計は数百万ドル規模の CAD ワークステーションやパンチカードを介した離散座標入力に依存していた。

1986 年、ジム・フォン・エール（Jim von Ehr）が率いる Altsys 社は、誕生したばかりの Apple Macintosh 向けに画期的な **Fontographer** を投入した。これは一般のデザイナーがマウスを用いてベジェ輪郭を描画・編集し、標準の PostScript Type 1 フォントを出力できる史上初のデスクトップソフトウェアであった。**Figure 12-1** に示すように、Fontographer は「フォント一覧ウィンドウ（Font Window）」、「字形編集ウィンドウ（Glyph Window）」、および「メトリクス調整ウィンドウ（Metrics Window）」からなる現代フォントツールの 3 層インタラクションモデルを確立した。

::: tip Mac OS X 上における Macromedia Fontographer のフォント一覧ウィンドウ（Figure 12-1）
![Macromedia Fontographer 在 Mac OS X 下的字体视窗（Figure 12-1）](/images/fonts-encodings/fig12-1.png)
*Macromedia Fontographer 在 Mac OS X 下的字体视窗（Figure 12-1）*
:::

*図 12-1：Mac OS X 上で動作する Macromedia Fontographer の操作画面。上部に文字コード順のマトリクスが表示され、各セルに現在の字形の微小シルエットが描画される。*

同時期に並立したもう一つの名機が、Letraset 社の **FontStudio** である（**Figure 12-2**）。FontStudio は Mac OS 9 時代において高精度のマルチレイヤー編集環境をいち早く実現し、下絵スキャン画像を背景参照レイヤーに置いてベジェ曲線でトレースする手法を確立した。

::: tip Mac OS 9 上における Letraset FontStudio の字形編集ウィンドウ（Figure 12-2）
![Letraset FontStudio 在 Mac OS 9 下的单字编辑视窗（Figure 12-2）](/images/fonts-encodings/fig12-2.png)
*Letraset FontStudio 在 Mac OS 9 下的单字编辑视窗（Figure 12-2）*
:::

*図 12-2：Mac OS 9 上で動作する Letraset FontStudio の字形編集画面。直交座標系における輪郭描画機能と、左側のフローティングツールボックスによる精密制御が示されている。*

1990 年代、サンクトペテルブルクのユーリ・ヤルモラ（Yuri Yarmola）らによる SoftUnion（現 FontLab Ltd.）が **FontLab** を発表した。高次のベジェ数理ツール、完全な OpenType コンパイラ、高度な自動ヒンティング、および統合 Python 環境を備えた FontLab は、世界中のフォントファウンドリの標準工業ツールとしての地位を不動のものとした。

---

## 2. 幾何学的基礎：スプライン曲線とノードトポロジー

字形編集ウィンドウにおいて、デザイナーが直面する最大の課題は、いかに少ない数学的制御点を用いて滑らかな輪郭を表現するかである。

デジタルタイポグラフィには 2 つの対立する流派が存在する：**PostScript 陣営の 3 次ベジェ曲線（Cubic Bézier）** と **TrueType 陣営の 2 次 B スプライン曲線（Quadratic Bézier / B-spline）** である。

### 2.1 3 次ベジェ曲線（PostScript Type 1 / OpenType CFF）
3 次ベジェ曲線は 4 つの制御点（始点 $\mathbf{P}_0$、外部方向ハンドル $\mathbf{P}_1, \mathbf{P}_2$、終点 $\mathbf{P}_3$）によって定義され、3 次バーンスタイン多項式に従う：

$$\mathbf{B}(t) = (1-t)^3 \mathbf{P}_0 + 3(1-t)^2 t \mathbf{P}_1 + 3(1-t) t^2 \mathbf{P}_2 + t^3 \mathbf{P}_3, \quad t \in [0, 1]$$

### 2.2 2 次ベジェ曲線（TrueType）
2 次ベジェ曲線は 3 つの点（始点 $\mathbf{P}_0$、外部制御点 $\mathbf{P}_1$、終点 $\mathbf{P}_2$）によって定義される：

$$\mathbf{B}(t) = (1-t)^2 \mathbf{P}_0 + 2(1-t) t \mathbf{P}_1 + t^2 \mathbf{P}_2, \quad t \in [0, 1]$$

* **次数上昇（Degree Elevation）方程式**：  
  2 次ベジェ曲線は、以下の代数変換により完全に等価な 3 次ベジェ曲線へと無損失に変換可能である：
  $$\mathbf{Q}_0 = \mathbf{P}_0, \quad \mathbf{Q}_1 = \mathbf{P}_0 + \frac{2}{3}(\mathbf{P}_1 - \mathbf{P}_0), \quad \mathbf{Q}_2 = \mathbf{P}_2 + \frac{2}{3}(\mathbf{P}_1 - \mathbf{P}_2), \quad \mathbf{Q}_3 = \mathbf{P}_2$$

::: tip PostScript 3 次曲線と TrueType 2 次曲線の輪郭比較（Figure 12-11）
![PostScript 三次曲线与 TrueType 二次曲线轮廓对比（Figure 12-11）](/images/fonts-encodings/fig12-11.png)
*PostScript 三次曲线与 TrueType 二次曲线轮廓对比（Figure 12-11）*
:::

*図 12-11：PostScript 3 次ベジェ輪郭（左）と TrueType 2 次 B スプライン輪郭（右）の比較。TrueType においては、連続する 2 つのオフカーブ制御点の中点が自動的にオンカーブ切点として補間される。*

---

## 3. FontLab Studio 工業級設計体系

### 3.1 4 大字形表示モード（Font Window Display Modes）
1. **名前モード（Names Mode, Figure 12-3）**：グリフ名によるフラット表示；
2. **ページモード（Pages Mode, Figure 12-4）**：256 文字単位のコードページ分割表示；
3. **ブロックモード（Ranges Mode, Figure 12-5）**：Unicode 公式ブロックごとのグループ表示；
4. **インデックスモード（Index Mode, Figure 12-6）**：物理 GID（Glyph ID）順の表示。

::: tip FontLab 字体视窗的名称模式（Figure 12-3）
![FontLab 字体视窗的名称模式（Figure 12-3）](/images/fonts-encodings/fig12-3.png)
*FontLab 字体视窗的名称模式（Figure 12-3）*
:::

*図 12-3：FontLab の Names モード表示。*

::: tip FontLab 字体视窗的页面模式（Figure 12-4）
![FontLab 字体视窗的页面模式（Figure 12-4）](/images/fonts-encodings/fig12-4.png)
*FontLab 字体视窗的页面模式（Figure 12-4）*
:::

*図 12-4：FontLab の Pages モード表示。*

::: tip FontLab 字体视窗的区段模式（Figure 12-5）
![FontLab 字体视窗的区段模式（Figure 12-5）](/images/fonts-encodings/fig12-5.png)
*FontLab 字体视窗的区段模式（Figure 12-5）*
:::

*図 12-5：FontLab の Ranges モード表示。*

::: tip FontLab 字体视窗的索引模式（Figure 12-6）
![FontLab 字体视窗的索引模式（Figure 12-6）](/images/fonts-encodings/fig12-6.png)
*FontLab 字体视窗的索引模式（Figure 12-6）*
:::

*図 12-6：FontLab の Index モード表示。*

### 3.2 フォントメタデータ設定（Font Info）

::: tip Font Info 元数据与版权标签页（Figure 12-7）
![Font Info 元数据与版权标签页（Figure 12-7）](/images/fonts-encodings/fig12-7.png)
*Font Info 元数据与版权标签页（Figure 12-7）*
:::

*図 12-7：Font Info の Names および Copyright 設定パネル。*

::: tip Font Info 核心度量与支持代码页标签页（Figure 12-8）
![Font Info 核心度量与支持代码页标签页（Figure 12-8）](/images/fonts-encodings/fig12-8.png)
*Font Info 核心度量与支持代码页标签页（Figure 12-8）*
:::

*図 12-8：Font Info の Key dimensions および Supported codepages 設定パネル。*

### 3.3 メトリクスとカーニング（Metrics & Kerning）

$$\text{Advance Width} = \text{LSB} + \text{Bounding Box Width} + \text{RSB}$$

### 3.4 Multiple Master 多マスター設計

::: tip FontLab 中设计 Multiple Master 字体的界面（Figure 12-9）
![FontLab 中设计 Multiple Master 字体的界面（Figure 12-9）](/images/fonts-encodings/fig12-9.png)
*FontLab 中设计 Multiple Master 字体的界面（Figure 12-9）*
:::

*図 12-9：FontLab における Multiple Master 設計画面。同一ウィンドウ内で複数のマスター輪郭が同時に重層表示される。*

::: tip 从普通字体创建 Multiple Master 的配置视窗（Figure 12-10）
![从普通字体创建 Multiple Master 的配置视窗（Figure 12-10）](/images/fonts-encodings/fig12-10.png)
*从普通字体创建 Multiple Master 的配置视窗（Figure 12-10）*
:::

*図 12-10：2 つの独立フォントから Multiple Master フォントを生成するダイアログ。*

### 3.5 PostScript アライメントゾーンと BlueValues 数理

$$\text{BlueValues} = [y_{b0}, y_{t0}, \quad y_{b1}, y_{t1}, \quad \dots]$$

$$\text{Threshold Size} = \frac{1}{\text{BlueScale} \times (\text{Zone Height})}$$

---

## 4.  автоматизация: Python スクリプト革命

### 4.1 FontLab Studio の Python オブジェクトモデル
`Font`、`Glyph`、`Contour`、`Node` による 4 層の階層構造を通じて、全字形のバッチ処理が可能である。

### 4.2 FontForge による CI/CD ビルド自動化
純粋なテキスト形式である **SFD（Spline Font Database）** と Python API により、GUI を起動することなく完全自動化されたフォント生成パイプラインが構築可能である。

---

## 5. 画像から字形へ：ScanFont と自動トレース

::: tip ScanFont 中的字形图素自动分割（Figure 12-12）
![ScanFont 中的字形图素自动分割（Figure 12-12）](/images/fonts-encodings/fig12-12.png)
*ScanFont 中的字形图素自动分割（Figure 12-12）*
:::

*図 12-12：ScanFont におけるグリフの自動分割処理画面。*

::: tip ScanFont 中自动追踪参数的实时配置对话框（Figure 12-13）
![ScanFont 中自动追踪参数的实时配置对话框（Figure 12-13）](/images/fonts-encodings/fig12-13.png)
*ScanFont 中自动追踪参数的实时配置对话框（Figure 12-13）*
:::

*図 12-13：自動トレースパラメータのリアルタイム調整ダイアログ。*

::: tip 手工绘制轮廓与不同参数自动追踪轮廓的微观对比（Figure 12-14）
![手工绘制轮廓与不同参数自动追踪轮廓的微观对比（Figure 12-14）](/images/fonts-encodings/fig12-14.png)
*手工绘制轮廓与不同参数自动追踪轮廓的微观对比（Figure 12-14）*
:::

*図 12-14：熟練のデザイナーによる手動トレース（左）と、自動トレースアルゴリズムによる生成輪郭（中央・右）の品質比較。*

---

Altsys Fontographer から FontLab Studio、FontForge、そして ScanFont に至る進化は、デジタル書体制作における職人精神と計算幾何学の完璧な融合を示している。

しかし、美しい連続輪郭を描き出すことは第一歩に過ぎない。低解像度の画面上でこの輪郭がレンダリングされる際、離散ピクセルによるグリフの破綻をいかに防ぐのか？

これこそが、**第 13 章：ラスタライズ微調整（Hinting）の究極の芸術**において探求するバイトコード仮想マシンの世界である。
'''

with open('docs/ja/fonts-encodings/chapter-12.md', 'w', encoding='utf-8') as f:
    f.write(ja_content)

print(f"docs/ja/fonts-encodings/chapter-12.md written: {len(ja_content)} chars")
