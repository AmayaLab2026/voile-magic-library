---
title: "第 12 章：フォントの編集と作成"
description: "フォント編集ソフト（FontLab Studio、FontForge）、Python によるバッチ自動化、3 次/2 次ベジェ曲線変換、Spiro 幾何学、PostScript ヒンティング（BlueValues、StemSnap、ヒント置換）の全景。"
---

# 第 12 章：フォントの編集と作成
### Chapter 12: Editing and Creating Fonts
ヤニス・ハラランボス（Yannis Haralambous, Ph.D.）著
選書『Fonts & Encodings』第 501–550 頁
*訳者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

---

## 1. 文字作成の全景（Introduction）

デジタルフォントの作成と編集は、純粋な視覚芸術と厳密なコンピュータサイエンスが交差する極致の領域です。1 文字（グリフ）のデザインは、単なる幾何学的スケッチではなく、厳密な座標系、アフィン変換、位相幾何学的方向規則、そしてラスタライズエンジン（レンダラ）との対話のための命令群によって成立しています。

### 1.1 グリフの解剖学的構造
グリフ空間は仮想デザイングリッド（通常、TrueType では $2048 \times 2048$、PostScript/CFF では $1000 \times 1000$ 単位の EM 正方形）上に配置されます：
- **ベースライン（Baseline, $y = 0$）**：すべての文字が水平に整列する基本基準線；
- **送り幅（Advance Width）**：現在の文字の原点から次の文字の原点までの水平変位；
- **左サイドベアリング（LSB, Left Sidebearing）**：グリフの原点（$x=0$）から文字の最も左端の輪郭点までの距離；
- **右サイドベアリング（RSB, Right Sidebearing）**：文字の最も右端の輪郭点から送り幅の終端までの余白：
$$\text{Advance Width} = \text{LSB} + \text{Bounding Box Width} + \text{RSB}$$
- **アセンダ線（Ascender line）**：'d', 'h', 'k' などの上部ステムの上限；
- **ディセンダ線（Descender line）**：'p', 'q', 'y' などの下部ステムの最下端；
- **キャップハイト（Cap Height）**：大文字 'H', 'E' などの平坦な頂点の高さ；
- **エックスハイト（x-height）**：小文字 'x', 'v', 'w' などの平坦な上端の高さ。

### 1.2 曲線幾何：3 次ベジェ曲線と 2 次ベジェ曲線の本質的差異
- **PostScript / CFF（3 次ベジェ曲線）**：各曲線セグメントは 2 つの端点（$\mathbf{P}_0, \mathbf{P}_3$）と 2 つの独立した制御点（$\mathbf{P}_1, \mathbf{P}_2$）を持ち、変曲点（S 字カーブ）や非対称な張力変化を 1 つのセグメントでエレガントに表現できます：
$$\mathbf{B}(t) = (1-t)^3 \mathbf{P}_0 + 3(1-t)^2 t \mathbf{P}_1 + 3(1-t) t^2 \mathbf{P}_2 + t^3 \mathbf{P}_3, \quad t \in [0, 1]$$

- **TrueType（2 次ベジェ曲線）**：各セグメントは 2 つの端点（$\mathbf{P}_0, \mathbf{P}_2$）と 1 つの制御点（$\mathbf{P}_1$）のみを持ちます：
$$\mathbf{B}(t) = (1-t)^2 \mathbf{P}_0 + 2(1-t) t \mathbf{P}_1 + t^2 \mathbf{P}_2, \quad t \in [0, 1]$$
曲率変化を表現するには複数の放物線セグメントを連続させる必要があり、TrueType では連続する 2 つのオフカーブ（制御点）の中点を暗黙のオンカーブ点として扱うことでデータサイズを節約します。

---

## 2. FontLab Studio 商業フォント開発体系

FontLab Studio（バージョン 4 および 5）は、タイポグラフィ産業において長年にわたり事実上のデファクトスタンダードとして君臨してきたプロフェッショナル向けフォントエディタです。

### 2.1 4 つのフォントウィンドウ表示モード（Font Window Display Modes）
FontLab は文字セットを体系的にナビゲートするために 4 つの表示モードを提供します：
1. **名前モード（Names Mode）**：Adobe Glyph Naming 規約に準拠したグリフ識別子（`A`, `acute`, `adieresis`, `afii10017` 等）を表示；
2. **ページモード（Pages Mode）**：256 文字ごとのコードページ単位で文字テーブルを分割表示；
3. **範囲モード（Ranges Mode）**：Unicode の公式ブロック範囲（Basic Latin, Latin-1 Supplement, Cyrillic, Greek 等）に基づきグリフをフィルタリング；
4. **インデックスモード（Index Mode）**：フォントファイル内の物理的なグリフインデックス（GID 0, 1, 2...）順に配列。

### 2.2 輪郭編集の幾何学：ノードタイプと位相幾何拘束
FontLab の輪郭エディタは、ノード（頂点）を厳密な位相的役割によって分類します：
- **コーナーノード（Corner Node, 四角形アイコン）**：接線方向が不連続な角点。両側のハンドルが独立に回転；
- **スムーズノード（Smooth Node, 丸型アイコン）**：$C^1$ 連続性（傾きの一致）を維持し、両側のハンドルが 180 度の一直線を形成；
- **タンジェントノード（Tangent Node, 三角形アイコン）**：直線セグメントと曲線セグメントが滑らかに合流する接続点。

#### 輪郭方向の物理的絶対則（Contour Direction）
ラスタライザが内外判定（Fill/Winding Rule）を正しく実行するため、輪郭の描画方向には厳格な規約が存在します：
- **PostScript Type 1 / OpenType (CFF)**：外側のアウトラインは反時計回り（Counter-Clockwise, CCW）、内側の穴（カウンター）は時計回り（Clockwise, CW）；
- **TrueType**：外側のアウトラインは時計回り（CW）、内側の穴は反時計回り（CCW）。
輪郭の向きが反転すると、TrueType ラスタライザで文字が「中空（塗りつぶされない）」あるいは「反転」する重大な描画破綻が発生します。

### 2.3 メトリクスとカーニング体系（Metrics and Kerning）

#### 1. LSB、RSB と文字幅の計算
文字の読みやすさは、白と黒の視覚的バランス（空間配分）によって決定されます。丸い文字（'O', 'C'）や斜めの文字（'A', 'V'）では、幾何学的なバウンディングボックスの境界を視覚的な「錯視補正（Overshoot）」によって外側へわずかに突き出させる必要があります。

#### 2. クラスカーニング（Class-based Kerning）
数千文字に及ぶフォントにおいて、個別のグリフペアごとにカーニング値を設定することは不可能です。FontLab は**クラスカーニング（Kerning Classes）**を導入しました：
- 左側クラス `@Left_Round`（`O`, `C`, `G`, `Q`, `OE` 等）
- 右側クラス `@Right_Round`（`O`, `D`, `P`, `Q` 等）
- `@Left_Round` と `@Right_Round` の間に $-40$ 単位のカーニングを設定することで、数千の文字ペアの適切なスペーシングが一撃で定義されます。

### 2.4 輪郭の幾何変換とフィルタ
- **スラント変換（Slanting）**：傾き角度 $\theta$ による斜体（Oblique）の自動生成；
- **ステム太さ拡張（Expand Stroke）**：アウトラインの平行オフセットによるボールド化；
- **ブーリアン演算（Remove Overlap）**：交差する複数の独立パスを単一の外周輪郭へと自動マージ。

---

## 3. Python スクリプトによる FontLab Studio の自動制御

FontLab は内部に Python インタプリタを組み込んでおり、全フォントオブジェクト、グリフ、ノード、カーニングペアをプログラミングから直接操作可能です。

### 3.1 FontLab Python API アーキテクチャ
- `fl`：FontLab のメインアプリケーションオブジェクト；
- `Font`：開かれているフォントファイル（グリフ配列、ヘッダー情報、メトリック辞書）；
- `Glyph`：個々のグリフ（ノードリスト、コンポーネント、アンカー、幅）；
- `Node`：輪郭上の点座標 $(x, y)$、タイプ、スムーズ属性；
- `Point`：2 次元ベクトル演算。

### 3.2 実戦スクリプト：全自動文字検査と合成グリフ生成

#### スクリプト 1：フォント全グリフのメトリック検査と極値検出
全グリフを走査し、バウンディングボックスの異常値やベースライン沈み込みを検出するスクリプトです：

```python
# -*- coding: utf-8 -*-
# FontLab Studio 用グリフバウンディングボックス検査スクリプト
import fl

font = fl.font
print(f"フォント名: {font.font_name}")
print(f"総グリフ数: {len(font.glyphs)}")

overflow_glyphs = []
for index, glyph in enumerate(font.glyphs):
    bbox = glyph.GetBoundingBox()
    # bbox は Rect(xmin, ymin, xmax, ymax)
    if bbox.top > font.ascender + 100:
        overflow_glyphs.append((glyph.name, bbox.top))

print(f"アセンダを著しく超過したグリフ数: {len(overflow_glyphs)}")
for name, top in overflow_glyphs[:10]:
    print(f"  グリフ [{name}]: 上端 Y = {top}")
```

#### スクリプト 2：アクセント記号付き合成グリフ（Composite Glyphs）の全自動生成
基底文字（例: `A`）の上にアクセント記号（例: `acute`）をアンカー座標に基づいて自動配置し、新規グリフ `Aacute` を組み立てるスクリプトです：

```python
# -*- coding: utf-8 -*-
# アンカーに基づく自動合成グリフビルダー
import fl

font = fl.font

def build_accented_glyph(base_name, accent_name, target_name):
    base_idx = font.FindGlyph(base_name)
    accent_idx = font.FindGlyph(accent_name)
    
    if base_idx == -1 or accent_idx == -1:
        print(f"エラー: 基底文字またはアクセントが見つかりません: {base_name}, {accent_name}")
        return
        
    base_glyph = font.glyphs[base_idx]
    accent_glyph = font.glyphs[accent_idx]
    
    # 新規グリフの作成または取得
    target_idx = font.FindGlyph(target_name)
    if target_idx == -1:
        new_glyph = fl.Glyph()
        new_glyph.name = target_name
        font.glyphs.append(new_glyph)
        target_glyph = font.glyphs[-1]
    else:
        target_glyph = font.glyphs[target_idx]
        target_glyph.Clear()
        
    # 送り幅の継承
    target_glyph.width = base_glyph.width
    
    # 基底文字コンポーネントの追加
    c1 = fl.Component(base_idx, fl.Point(0, 0))
    target_glyph.components.append(c1)
    
    # アクセントの配置オフセット計算（中央揃え）
    base_bbox = base_glyph.GetBoundingBox()
    accent_bbox = accent_glyph.GetBoundingBox()
    
    offset_x = (base_bbox.left + base_bbox.right) / 2 - (accent_bbox.left + accent_bbox.right) / 2
    offset_y = base_bbox.top - accent_bbox.bottom + 20 # 20 単位の間隔
    
    c2 = fl.Component(accent_idx, fl.Point(offset_x, offset_y))
    target_glyph.components.append(c2)
    
    font.modified = 1
    print(f"合成成功: {target_name} ({base_name} + {accent_name})")

build_accented_glyph("A", "acute", "Aacute")
build_accented_glyph("E", "grave", "Egrave")
fl.UpdateFont()
```

---

## 4. FontForge オープンソースフォント工房

George Williams によって開発された **FontForge** は、GNU GPL ライセンスの下で提供される比類なき高機能オープンソースフォントエディタです。

### 4.1 幾何学と全平面 Unicode サポート
FontForge は最初から Unicode 体系（UTF-32/UCS-4）をネイティブ内部構造として設計されており、BMP（基本多言語面）のみならず、SMP（第 1 面、歴史的文字や音楽記号）、SIP（第 2 面、CJK 統合漢字拡張面）に至る 100 万を超える文字コード空間をシームレスに扱えます。

### 4.2 3 次/2 次ベジェの双方向変換と Spiro 幾何学
1. **PostScript と TrueType の双方向変換**：
   FontForge は 3 次ベジェと 2 次ベジェを相互に自動変換します。2 次ベジェ曲線から 3 次ベジェ曲線への次数上昇（Degree Elevation）は数学的に完全に無損失で行われます：
$$\mathbf{Q}_0 = \mathbf{P}_0, \quad \mathbf{Q}_1 = \mathbf{P}_0 + \frac{2}{3}(\mathbf{P}_1 - \mathbf{P}_0), \quad \mathbf{Q}_2 = \mathbf{P}_2 + \frac{2}{3}(\mathbf{P}_1 - \mathbf{P}_2), \quad \mathbf{Q}_3 = \mathbf{P}_2$$
一方、3 次曲線を 2 次曲線へダウンサンプリングする際は、許容誤差（Tolerance）パラメータに基づいて自動的に最適な中間オンカーブ点を挿入します；
2. **Raph Levien の Spiro 幾何学モデル**：
   FontForge はオイラーの螺旋（クロソイド曲線、Clothoid）に基づく **Spiro** モードを内包しています。曲率 $\kappa$ が弧長 $s$ に対して線形に変化する性質を持つため、曲率が跳躍することなく完全に連続する $G^2$ / $G^3$ 連続の極めて滑らかな輪郭をわずか数個のアンカー点から自動生成できます。

### 4.3 ビットマップの自動ベクター追跡（Auto-tracing）
FontForge はオープンソースのトレースエンジン（Potrace および Autotrace）と緊密に統合されています。スキャンされた高解像度活字ビットマップを取り込み、閾値二値化、輪郭検出、多角形近似、そして滑らかな 3 次ベジェ曲線フィッティングを完全に自動で実行します。

### 4.4 FontForge Python 自動化パイプライン
FontForge は強力なスタンドアロン Python モジュール（`import fontforge`）を提供し、GUI なしでサーバーサイドや CI/CD パイプライン内でフォントをコンパイルできます：

```python
# -*- coding: utf-8 -*-
# FontForge による自動ビルド・ヒンティング・出力スクリプト
import fontforge

# UFO または SFD ソースの読み込み
font = fontforge.open("MyFont-Regular.sfd")

# 重なり輪郭の自動除去（ブーリアン結合）
for glyph in font.glyphs():
    glyph.removeOverlap()

# 極値点の自動追加（ラスタライズとヒンティングの必須条件）
for glyph in font.glyphs():
    glyph.addExtrema()

# 正しい輪郭方向への強制修正
for glyph in font.glyphs():
    glyph.correctDirection()

# 自動ヒンティング（Auto-Hinting）
font.autoHint()

# 高品質 OpenType (CFF) フォントとしてエクスポート
font.generate("dist/MyFont-Regular.otf", flags=("opentype", "round"))
print("フォント出力完了: dist/MyFont-Regular.otf")
```

---

## 5. PostScript ヒンティング体系（PostScript Hinting）

低解像度画面や 300〜600 dpi のオフィスプリンタにおいて、数学的に純粋なベジェ曲線輪郭はラスタライズの量子化誤差（グリッド交点への丸め）により、ステムの太さの不揃い、ドットの消失、文字の歪みといった深刻な視覚劣化を引き起こします。PostScript はこれを防ぐため、**ヒンティング（Hinting）**と呼ばれる幾何学的補正技術を開発しました。

### 5.1 大域ヒント（Global Hints）とアライメントゾーン（Alignment Zones）

#### 1. `BlueValues` と `OtherBlues`
すべてのグリフの垂直位置（ベースライン、x-height、キャップハイト、ディセンダ）を整列させるため、Type 1 フォントは `Private` 辞書内に整列ゾーン配列を定義します：
- `BlueValues`：最大 7 ペア（14 個）の符号付き整数配列。下端境界と上端境界をペアで記述します：
$$\text{BlueValues} = [y_{b0}, y_{t0}, \quad y_{b1}, y_{t1}, \quad \dots]$$
ベースラインゾーン（例: `[-15, 0]`）および上部ゾーン（例: x-height `[450, 465]`、Cap Height `[700, 715]`）を指定します；
- `OtherBlues`：最大 5 ペアの配列。ディセンダゾーン（例: `[-215, -200]`）を定義。

#### 錯視補正（Overshoot）と丸め抑制の数学
文字 'O' や 'C' などの丸い輪郭は、幾何学的に直線文字 'H' や 'I' と同じ高さにすると視覚的に小さく見えます。そのため、デザイナーは輪郭の頂点をわずかに外側へ突き出させます（Overshoot）。
低解像度において、この突き出しが 1 ピクセルの余分な突起となって文字がガタつくのを防ぐため、ラスタライザは解像度が特定のピクセル閾値以下のときに**オーバーシュートをベースラインまたはキャップハイトへ強制平坦化**します。

この平坦化が解除される最大解像度（閾値ポイントサイズ）は、`BlueScale` パラメータによって数学的に決定されます：
$$\text{Threshold Size} = \frac{1}{\text{BlueScale} \times (\text{Zone Height})}$$

デフォルト値 `BlueScale = 0.039625` の場合、$PPM_{max} \approx 24.7$ ピクセルとなり、25 ピクセル未満の小型表示では常にオーバーシュートが抑制されて端正な整列が維持されます。

#### 2. 標準ステム幅：`StdHW`, `StdVW` とスナップ配列
- **`StdHW`（Standard Horizontal Stem Width）**：フォント内で最も支配的な水平ステムの太さ（例: 'E', 'H' の横バー）；
- **`StdVW`（Standard Vertical Stem Width）**：最も支配的な垂直ステムの太さ（例: 'l', 'H' の縦ステム）；
- **`StemSnapH`, `StemSnapV`**：最大 12 個の代表的なステム幅の昇順配列。
ラスタライザは、個々の文字のステム幅がこれら代表値に近い場合、強制的に同一のピクセル幅（例: 12 pt で正確に 1 ピクセル、18 pt で正確に 2 ピクセル）へスナップ（量子化）し、同一行の文字群で線の太さが不揃いになる現象を完全に根絶します。

### 5.2 局所ヒント（Local Hints）とヒント置換（Hint Substitution）

各文字の CharString 内において、ステムの位置は `hstem`（水平ステム）および `vstem`（垂直ステム）オペコードによって局所的に宣言されます。

#### ヒント置換（Hint Substitution）の革新的メカニズム
複雑な文字（例: 'B', 'R', 'g', 'e', 漢字）において、グリフ全体で単一のヒントセットを適用すると、上下や左右でステム定義が衝突・交差し、かえってラスタライザを混乱させます。
Type 1（Subr 12 経由）および Type 2（`hintmask` バイトコード）は**ヒント置換**を導入しました：
輪郭の描画パスの途中で、それまでのヒントセットを無効化し、現在の幾何学的サブパスに特化した新たなヒントセットへと動的に切り替えます。これにより、極限の低解像度下でも複雑な文字のカウンターとステムが驚異的な明瞭さでレンダリングされます。

---

## 6. 結語（Conclusions）

フォントの作成と編集は、幾何学的な直観と計算機的な厳密性の見事な融合です。FontLab や FontForge を使いこなし、Python によるスクリプティングと PostScript ヒンティングの数学的基礎を深く理解することによって、初めて数百年受け継がれてきたタイポグラフィの美を、現代のシリコンと液晶のディスプレイ上に忠実に再現することが可能となるのです。

*本章の全訳および技術校正は ヴワル魔法図書館（Voile Magic Library）文献翻訳工房 により完了しました。*
