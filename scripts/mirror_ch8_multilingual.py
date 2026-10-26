import opencc, os, re

with open('docs/zh/fonts-encodings/chapter-8.md', 'r', encoding='utf-8') as f:
    zh_text = f.read()

# 1. Generate zh-hant via opencc
converter = opencc.OpenCC('s2t')

# protect code fences and math blocks
blocks = []
def repl_block(m):
    idx = len(blocks)
    blocks.append(m.group(0))
    return f"___CODE_BLOCK_{idx}___"

protected = re.sub(r'(```[\s\S]*?```|\$\$[\s\S]*?\$\$|`[^`\n]+`)', repl_block, zh_text)
hant_protected = converter.convert(protected)

for idx, b in enumerate(blocks):
    hant_protected = hant_protected.replace(f"___CODE_BLOCK_{idx}___", b)

# fix translator line in zh-hant
hant_protected = hant_protected.replace('*译者：', '*譯者：')

with open('docs/zh-hant/fonts-encodings/chapter-8.md', 'w', encoding='utf-8') as f:
    f.write(hant_protected)
print(f"Wrote docs/zh-hant/fonts-encodings/chapter-8.md ({len(hant_protected)} chars)")

# 2. Build Japanese version for Chapter 8
ja_text = r"""---
title: 第8章：X Window システムにおけるフォント管理
description: X Window (Unix/Linux) クライアント・サーバ型ネットワーク透過グラフィックアーキテクチャ、XLFD 14フィールド論理フォント記述仕様、フォントディレクトリと設定、コアツール群と変換エコシステムの全貌
---

# 第 8 章：X Window システムにおけるフォント管理

*翻訳者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

Macintosh（Classic Mac OS および Mac OS X）と Windows システムにおけるフォントメカニズムを詳細に検討した結果、これら2大パーソナルOSがフォント処理の設計思想と実装において驚くほど類似していることが明らかになりました。ここで視点を Unix に移しましょう。Unix は元来、大規模な産業研究機関や国立研究所、学術機関を中心に使用されていましたが、現在では GNU/Linux や FreeBSD などの自由・オープンソース実装の普及により、世界中の開発者やサーバ市場を席巻しています。

Classic Mac OS や初期の Windows が OS カーネルとウィンドウ描画システムを厳密に分離していなかったのに対し、Unix はその誕生初期から極めて直交的なモジュール化思想を徹底していました。すなわち、**OS カーネル（Kernel）とウィンドウグラフィックシステム（Windowing System）は完全に独立した別個のエンティティである** という原則です。Unix の世界において、このウィンドウシステムはほぼ例外なく **X Window System（通常 X または X11 と呼ばれる）** が独占的に担ってきました。

---

## 1. X Window アーキテクチャの特異な性質と動作機構

X Window System は 1984 年にマサチューセッツ工科大学（MIT）の有名なアテナ計画（Project Athena）で産声を上げ、その後 X Consortium および現在の X.Org Foundation によって継続的に標準化と発展を遂げてきました。X Window におけるフォント管理を理解するための第一歩は、その中核である**ネットワーク透過性（Network Transparency）とクライアント・サーバ（Client-Server）アーキテクチャ** を正確に把握することです：

```
+-------------------------------------------------------------+
|                      Remote Host / Supercomputer            |
|  +-------------------------------------------------------+  |
|  |             X Client (Application: Emacs / CAD)       |  |
|  |  * Sends rendering requests via X11 Core Protocol    |  |
|  |  * Requests font metrics, character glyphs, strings   |  |
|  +-------------------------------------------------------+  |
+------------------------------|------------------------------+
                               | Network Socket (TCP/IP / SSH)
                               v
+-------------------------------------------------------------+
|                      Local Workstation / Display            |
|  +-------------------------------------------------------+  |
|  |             X Server (X.Org / XFree86)                |  |
|  |  * Manages physical screen, GPU, mouse, keyboard      |  |
|  |  * Accesses Font Path: rasterizes / draws glyphs      |  |
|  +-------------------------------------------------------+  |
|                              |                              |
|                              v                              |
|                   [ Physical Framebuffer ]                  |
+-------------------------------------------------------------+
```

1. **用語の逆転構造**：Web や FTP などの一般的なネットワークモデルでは、「サーバ」は遠隔地のデータセンターにあるホストを指し、「クライアント」は手元の端末を指します。しかし X Window の哲学では、この呼称が正反対になります：
   - **X サーバ（X Server）**：手元で物理的に操作する端末機器上で動作し、物理ディスプレイ、GPU フレームバッファ、キーボード、マウス入力を直接制御します。
   - **X クライアント（X Client）**：実際に実行されるアプリケーションプログラム（テキストエディタ、科学計算シミュレーション、CAD、組版ソフトなど）を指します。X クライアントはローカル端末上で動作することも、ギガビット LAN や数千キロ離れた遠隔のスーパーコンピュータ上で動作することも可能です。
2. **フォントラスタライズの物理的常駐位置**：
   - リモートの X クライアントが画面に文字列を描画しようとする場合、従来の X11 コアプロトコルモデルでは、クライアント自身がフォントのアウトラインやビットマップデータを送信するのではなく、ローカルの X サーバに対して「フォント $F$ を用いて座標 $(x, y)$ に文字列 $S$ を描画せよ」という描画プロトコルコマンドを発行します。
   - これが意味するのは、**フォントファイル自体が X サーバの動作する物理マシン上に存在しなければならない（あるいは X サーバが到達可能なネットワークフォントサーバによって配信されていなければならない）** という点です。リモートホストに高度な数式フォントがインストールされていても、手元の X サーバ端末側にそのフォントが配置されていなければ、画面上に描画することは原理的に不可能です。
3. **ビットマップフォントの長期支配と持続性**：
   - Classic Mac OS や Windows は初期にごくわずかなビットマップフォント（Chicago, Geneva, System, Terminal 等）を保持していたに過ぎず、TrueType 登場後は急速に全ベクターアウトラインレンダリングへと移行しました。
   - 一方、X Window System においては、誕生から最初の 15 年以上にわたり、**ビットマップフォントが絶対的な主力を担い続けました**。Unix ワークステーションの日常的作業環境である仮想端末エミュレータ（`xterm`）やエディタ（Vi, Emacs）では、文字がグリッドに厳密に整列し、各ピクセルがアンチエイリアスのボケなしに鮮明で、瞬時に描画される必要がありました。1980〜90年代のハードウェアではベクターのリアルタイム展開コストが重く、事前に最適化されたビットマップフォント（`6x13`, `8x13`, `10x20` 等）を直接メモリ転送することが極めて合理的だったのです。
   - そのため、X 評議会は 14 項目に及ぶ詳細な分類・命名仕様を策定し、フォント枯渇を防ぐフォールバック機構を整備しました。これが **XLFD（X Logical Font Description）** です。

---

## 2. X 論理フォント記述仕様（XLFD）の完全解説

**XLFD（X Logical Font Description Conventions）** は、X Window 環境においてビットマップおよびベクターフォントを一意に識別、検索、マッチング、インスタンス化するために X Consortium が制定した標準仕様です。

XLFD の定義において、正当なフォント名は **ハイフン（`-`）で区切られた 14 個の文字列フィールド** で構成され、全体がハイフンで始まり、ISO 8859-1（Latin-1）でエンコードされます。

### 2.1 命名フォーマットと予約文字の制約
典型的な XLFD 構造テンプレートは以下のとおりです：
```
-FOUNDRY-FAMILY_NAME-WEIGHT_NAME-SLANT-SETWIDTH_NAME-ADD_STYLE_NAME-PIXEL_SIZE-POINT_SIZE-RESOLUTION_X-RESOLUTION_Y-SPACING-AVERAGE_WIDTH-CHARSET_REGISTRY-CHARSET_ENCODING
```

ネットワーク越しのパース安全性を担保するため、各フィールド内部には以下の予約文字を含めることが**厳格に禁止**されています：
- ハイフン（`-`）：フィールド区切り文字
- アスタリスク（`*`）および疑問符（`?`）：ワイルドカード検索文字
- カンマ（`,`）：フォントリスト区切り文字
- ダブルクォーテーション（`"`）：文字列デリミタ

### 2.2 14 個のコアフィールドの定義と物理的単位

| 番号 | フィールド名 | 属性分類 | 単位 / 範囲 | 技術的仕様と意味 |
| :---: | :--- | :---: | :---: | :--- |
| **1** | `FOUNDRY` | ファウンドリ | 文字列 | デジタル活字製造元または提供元（`adobe`, `bitstream`, `misc`, `urw`, `b&h`, `sony`, `daewoo` 等）。`misc` は公開された汎用収集コレクションを示す。 |
| **2** | `FAMILY_NAME` | ファミリ名 | テキスト | フォントの設計ファミリ名（`times`, `helvetica`, `courier`, `fixed`, `clean`, `lucida`, `palatino` 等）。 |
| **3** | `WEIGHT_NAME` | ウェイト | 視覚分類 | ストロークの視覚的な太さ・黒度（`bold`, `medium`, `demibold`, `light`, `black`, `regular` 等）。 |
| **4** | `SLANT` | 傾斜角 | 1文字コード | グリフ姿勢の幾何コード：<br>• `r` (Roman)：直立正体；<br>• `i` (Italic)：設計されたイタリック体；<br>• `o` (Oblique)：アルゴリズムによる機械的傾斜（偽斜体）；<br>• `ri` (Reverse Italic)：逆方向（左）へのイタリック傾斜；<br>• `ro` (Reverse Oblique)：逆方向の機械的傾斜；<br>• `ot` (Other)：その他の変則姿勢。 |
| **5** | `SETWIDTH_NAME` | 幅比率 | 相対幅 | プロポーション設計上の水平幅の伸縮（`normal`, `condensed`, `semicondensed`, `narrow`, `extended` 等）。 |
| **6** | `ADD_STYLE_NAME` | 追加変体 | 文字列 | ファミリ内の特殊なバリアントを区別する追加スタイル（`sans serif`, `informal`, `serif`, `ja`, `alt` 等）。通常は空。 |
| **7** | `PIXEL_SIZE` | ピクセル高 | 整数 ($px$) | ラスタライズ後の垂直ピクセル数。スケーラブルなベクターフォント（Type 1 / TrueType）の未ラスタライズ状態では通常 `0` を指定。 |
| **8** | `POINT_SIZE` | ポイント値 | 1/10 pt | 米国印刷ポイント（$1 \ pt = 1/72.27 \ in$）の 10 倍の値（光学サイズ Optical Size）。例えば `120` は 12pt、`140` は 14pt を表す。 |
| **9** | `RESOLUTION_X` | 水平解像度 | DPI | ラスタライズ対象機器の水平物理解像度（ドット毎インチ）。旧来のスクリーンでは `75` または `100`。 |
| **10** | `RESOLUTION_Y` | 垂直解像度 | DPI | 垂直物理解像度。**Unix では正方形ピクセルでないディスプレイ（例：$100 \times 75$）が存在した** ため、水平と垂直を独立して指定する必要があった。 |
| **11** | `SPACING` | 文字間隔 | 1文字コード | 文字幅のメトリクスモデル：<br>• `p` (Proportional)：プロポーショナル（可変幅）；<br>• `m` (Monospaced)：等幅（すべての文字が同一送り幅）；<br>• `c` (Character Cell)：完全セル固定文字。端末エミュレータ用に文字枠全体が固定矩形に収まる（`fixed` 等）。 |
| **12** | `AVERAGE_WIDTH`| 平均幅 | 1/10 px | 印刷可能文字の平均送り幅の 10 倍。等幅フォントではセル幅 $\times 10$ に正確に一致。ベクターフォントでは `0` を設定可能。 |
| **13** | `CHARSET_REGISTRY`| 文字セット規格 | 国際コード | 文字セット標準化団体（`iso8859`, `iso10646`, `jisx0208.1983`, `koi8`, `adobe` 等）。 |
| **14** | `CHARSET_ENCODING`| エンコード番号 | コードページ | 当該文字セット内の具体的サブセットやコードページ（`1`, `2`, `15`, `r`, `0` 等）。 |

### 2.3 具体的な実例解析

#### 例 A：端末用 Unicode ビットマップフォント
```
-misc-fixed-medium-r-normal--20-140-100-100-c-100-iso10646-1
```
- `-misc-`：オープンソースコミュニティによる汎用管理
- `-fixed-`：標準ターミナル用等幅ファミリ
- `-medium-`：標準ウェイト
- `-r-`：直立（Roman）
- `-normal-`：標準幅
- `--`：追加スタイルなし（空）
- `-20-`：ピクセル高 20px
- `-140-`：名目ポイント 14.0pt
- `-100-100-`：100 DPI 正方形ピクセルモニタ用
- `-c-`：完全文字セル（Character Cell）
- `-100-`：平均幅 10px（$10 \times 20$ グリッド）
- `-iso10646-1`：ISO 10646 / Unicode BMP 対応

#### 例 B：URW 提供のベクター Palatino フォント
```
-urw-palatino-medium-r-normal--12-120-75-75-p-0-iso8859-2
```
- `-urw-`：ドイツ URW++ 製
- `-palatino-`：ヘルマン・ツァップ設計のパラティノ体
- `-p-`：プロポーショナル幅
- `-0-`：平均幅 0（ベクター輪郭として動的計算）
- `-iso8859-2`：東欧・中欧ラテン文字（Latin-2）

### 2.4 ワイルドカードとパターンマッチング

14 フィールドすべてを暗記して記述するのは困難であるため、XLFD にはワイルドカードが組み込まれています：
- **`*`**：0文字以上の任意の文字列にマッチ
- **`?`**：正確に1文字の任意文字にマッチ

```bash
xterm -fn "*fixed-medium-r-*-16-*-iso8859-1"
```
X サーバは登録されたフォントデータベースを照合し、優先順位に基づいて最初に合致したフォントをインスタンス化します。

### 2.5 幾何変換行列とマルチマスターのサポート

ベクターフォントの場合、XLFD はピクセルやポイントサイズのフィールドに 2×2 アフィン変換行列を記述することを許可しています：
```
[-12 0 0 12]
```
```
-adobe-utopia-regular-r-normal--[-12 0 0 12]-*-*-*-p-*-iso8859-1
```
負の符号は水平・垂直反転を意味し、非対角成分はシアー（傾き）や任意の回転を実現します。また Multiple Master フォントの軸座標を埋め込む記法も定義されています。

---

## 3. X Window フォントのインストールと配置アーキテクチャ

### 3.1 ビットマップフォントのコンパイル
- **BDF（Bitmap Distribution Format）**：ASCII テキスト形式（付録 A.4 参照）。可読性はあるが肥大。
- **PCF（Portable Compiled Format）**：バイナリ形式。高速にメモリマッピング可能。
```bash
bdftopcf myfont10x20.bdf > myfont10x20.pcf
gzip -9 myfont10x20.pcf
```

### 3.2 ディレクトリインデックス：`fonts.dir` と `fonts.scale`
各フォントディレクトリには `fonts.dir` が必須です。
先頭行に総エントリ数 $N$ が記載され、続く行に「ファイル名」と「14フィールド XLFD」がペアで並びます：
```text
3
6x13.pcf.gz -misc-fixed-medium-r-semicondensed--13-120-75-75-c-60-iso10646-1
8x16.pcf.gz -misc-fixed-medium-r-normal--16-120-75-75-c-80-iso10646-1
10x20.pcf.gz -misc-fixed-medium-r-normal--20-140-100-100-c-100-iso10646-1
```
`mkfontdir` コマンドで自動生成します。ベクターフォントの場合はまず `mkfontscale` で `fonts.scale` を生成した後に `mkfontdir` を実行します。

### 3.3 エンコーディング再マップと別名：`encodings.dir` / `fonts.alias`
外部の `.enc` ファイルを用いて非標準フォントを Unicode 空間へ再配置する `encodings.dir`、および `times12` などの簡易名を正式な XLFD へ結びつける `fonts.alias` 機構が提供されます。

### 3.4 動的フォントパスと `xfs` フォントサーバ
```bash
# フォント検索パスの先頭に追加
xset +fp /usr/share/fonts/local/
# X サーバのキャッシュ再読み込み
xset fp rehash
```
無ディスク端末（X Terminals）環境では、ポート 7100 で動作する **X Font Server (`xfs`)** が集中管理とリモート配信を担いました。

---

## 4. X Window フォント管理ツール群

### 4.1 視覚的フォントセレクタ：`xfontsel`

![xfontsel 操作画面](/images/fonts-encodings/fig8-1.png)
*図 8-1：X Window 伝統のインタラクティブフォント選択ツール `xfontsel`。*

### 4.2 文字グリッド表示器：`xfd`

![xfd 文字グリッド表示画面](/images/fonts-encodings/fig8-2.png)
*図 8-2：`xfd` による ISO 10646 準拠 10x20 ビットマップフォントの全グリフ一覧表示。*

### 4.3 コマンドライン検索：`xlsfonts`
```bash
xlsfonts -fn "*-koi8-r"
```

---

## 5. Unix におけるフォント変換エコシステム

- **The GNU Font Tools**：Kathryn A. Hargreaves, Karl Berry, David MacKenzie らによるベクター中間形式 BZR および BPL（Bezier Property List）。
- **George Williams のツール群**：`bdf2pcf`, `macbinary`, `fon2fnts` など、Mac/Windows フォントを Unix で活用するための基盤ツール群。
- **コンソール・ビットマップ変換**：Dimitar Zharkov による `fontconv`（RAW, PSF, FNT の相互変換）。

---

## 6. 現代の Xft / Fontconfig アーキテクチャへの進化

21 世紀に入り、コア X11 フォントプロトコルの制約（ネットワーク往復レイテンシ、アンチエイリアス/サブピクセルレンダリングの欠如、OpenType 複雑スクリプト処理の不能）を克服するため、Keith Packard らによって **Xft + Fontconfig + FreeType** の近代化パイプラインが導入されました。

フォントのマッチングとラスタライズ処理をすべて**クライアント側**で実行し、生成された滑らかなアルファマスクのみを **XRender 拡張** 経由で X サーバに転送・合成する現代的アーキテクチャへと脱皮を遂げました。
"""

with open('docs/ja/fonts-encodings/chapter-8.md', 'w', encoding='utf-8') as f:
    f.write(ja_text)
print(f"Wrote docs/ja/fonts-encodings/chapter-8.md ({len(ja_text)} chars)")
