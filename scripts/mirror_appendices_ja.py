# -*- coding: utf-8 -*-
"""
Script to update docs/ja/fonts-encodings/appendices.md to mirror all figures and math blocks.
"""
import sys, re

sys.stdout.reconfigure(encoding='utf-8')

# Re-read fresh zh appendices text to get exact structure
with open('docs/zh/fonts-encodings/appendices.md', 'r', encoding='utf-8') as f:
    zh_text = f.read()

with open('docs/ja/fonts-encodings/appendices.md', 'r', encoding='utf-8') as f:
    ja = f.read()

# Japanese figure blocks
fig_a1 = '''
::: tip Macintosh 伝統の Chicago フォントの全体ストライク画像（Figure A-1）
![麦金塔操作系统经典 Chicago 字体的全局条带图像（Figure A-1）](/images/fonts-encodings/fig-app-a1.png)
*麦金塔操作系统经典 Chicago 字体的全局条带图像（Figure A-1）*
:::

*図 A-1：Apple Macintosh のメニュー画面で 15 年以上にわたり使用された伝説的フォント Chicago の全体ストライクビットマップ（Strike Bitmap）。ユーロ記号（€）を含む現代改訂版。*
'''

fig_a2 = '''
::: tip BDF 仕様における表意文字ビットマップとメトリクス定義（Figure A-2）
![BDF 规范中表意汉字点阵与度量属性的定义模型（Figure A-2）](/images/fonts-encodings/fig-app-a2.png)
*BDF 规范中表意汉字点阵与度量属性的定义模型（Figure A-2）*
:::

*図 A-2：Adobe BDF 規格における単一表意文字のビットマップ配列、バウンディングボックス、ベースラインオフセット、および送り幅ベクトルの定義モデル。*
'''

fig_a3 = '''
::: tip gftodvi により 5,203 DPI で生成された Computer Modern 組版サンプル（Figure A-3）
![gftodvi 在 5,203 DPI 超高分辨率下渲染的 Computer Modern 字母排印图（Figure A-3）](/images/fonts-encodings/fig-app-a3.png)
*gftodvi 在 5,203 DPI 超高分辨率下渲染的 Computer Modern 字母排印图（Figure A-3）*
:::

*図 A-3：クヌースのユーティリティ `gftodvi` が GF フォントから生成した DVI 組版サンプル（5,203 DPI 超高解像度）。*
'''

fig_c1 = '''
::: tip PostScript パス構築と塗りつぶしコード例（Figure C-1）
![PostScript 路径构建与填充代码（Figure C-1）](/images/fonts-encodings/fig-app-c1.png)
*PostScript 路径构建与填充代码（Figure C-1）*
:::

*図 C-1：PostScript 言語によるパス構築および塗りつぶし実行命令。*
'''

fig_c2 = '''
::: tip 非ゼロ巻き数規則と偶奇規則の物理的塗りつぶし比較（Figure C-2）
![非零缠绕数规则与奇偶环绕规则的物理填充对比（Figure C-2）](/images/fonts-encodings/fig-app-c2.png)
*非零缠绕数规则与奇偶环绕规则的物理填充对比（Figure C-2）*
:::

*図 C-2：自己交差パスに対する非ゼロ巻き数規則（Nonzero Winding Number Rule、左 3 図）と偶奇規則（Even-Odd Rule、右 3 図）の比較。*
'''

fig_c7 = '''
::: tip 多言語文字メトリクスとオーバーシュートの全景（Figure C-7）
![跨文种字符度量高度与超逸（Overshoot）全景（Figure C-7）](/images/fonts-encodings/fig-app-c7.png)
*跨文种字符度量高度与超逸（Overshoot）全景（Figure C-7）*
:::

*図 C-7：Omega Serif フォントにおけるラテン、アラビア、ヘブライ、アルメニア文字の基準高さと視覚的オーバーシュート量。*
'''

fig_c9 = '''
::: tip 文字 ‘H’, ‘O’, ‘m’ のアライメントゾーンとヒント（Figure C-9）
![字母 ‘H’、‘O’、‘m’ 的对齐区与微调主干（Figure C-9）](/images/fonts-encodings/fig-app-c9.png)
*字母 ‘H’、‘O’、‘m’ 的对齐区与微调主干（Figure C-9）*
:::

*図 C-9：PostScript Type 1 字形における水平・垂直ヒント（灰色帯は `BlueValues` アライメントゾーン）。*
'''

fig_c10 = '''
::: tip 文字 ‘B’ における 4 重ヒント置換の実行プロセス（Figure C-10）
![字母 ‘B’ 中四重提示替换的执行过程（Figure C-10）](/images/fonts-encodings/fig-app-c10.png)
*字母 ‘B’ 中四重提示替换的执行过程（Figure C-10）*
:::

*図 C-10：文字 ‘B’ 内部におけるヒント置換（Hint Substitution）の段階的プロセス。*
'''

fig_c11 = '''
::: tip PostScript Type 1 2連3次ベジェ Flex 機構（Figure C-11）
![PostScript Type 1 双三次贝塞尔 Flex 机制（Figure C-11）](/images/fonts-encodings/fig-app-c11.png)
*PostScript Type 1 双三次贝塞尔 Flex 机制（Figure C-11）*
:::

*図 C-11：2 つの 3 次ベジェ曲線 $abcd$ と $defg$ で構成される Flex 弾性的ヒンティング構造。*
'''

fig_c12 = '''
::: tip 漢字「講」および「皿」におけるカウンター制御（Figure C-12）
![汉字 “講” 与 “皿” 内部的白空主干计数控制（Figure C-12）](/images/fonts-encodings/fig-app-c12.png)
*汉字 “講” 与 “皿” 内部的白空主干计数控制（Figure C-12）*
:::

*図 C-12：複雑な東アジア表意文字に対する PostScript Type 1 / Type 2 のカウンター制御（Counter Control）。*
'''

fig_c16 = '''
::: tip CIDFont（Type 0）全体のデリファレンスアーキテクチャ（Figure C-16）
![CIDFont（Type 0）整体解引用架构（Figure C-16）](/images/fonts-encodings/fig-app-c16.png)
*CIDFont（Type 0）整体解引用架构（Figure C-16）*
:::

*図 C-16：CIDFont において CID 番号から字形データを解決する全体パイプライン。*
'''

fig_d1 = '''
::: tip EBLC ビットマップテーブルにおける水平・垂直メトリクス（Figure D-1）
![EBLC 点阵表中字形的水平与垂直度量（Figure D-1）](/images/fonts-encodings/fig-app-d1.png)
*EBLC 点阵表中字形的水平与垂直度量（Figure D-1）*
:::

*図 D-1：TrueType EBLC テーブルにおける内蔵ビットマップ字形のメトリクス定義。*
'''

fig_d3 = '''
::: tip Verdana フォント letter ‘A’ の gasp テーブル制御下におけるピクセル分布（Figure D-3）
![Verdana 字体 letter ‘A’ 在 gasp 表控制下的栅格尺寸分布（Figure D-3）](/images/fonts-encodings/fig-app-d3.png)
*Verdana 字体 letter ‘A’ 在 gasp 表控制下的栅格尺寸分布（Figure D-3）*
:::

*図 D-3：Verdana フォントにおける `gasp` テーブルによるアンチエイリアスとヒンティングの ppem 段階的切り替え。*
'''

fig_d6 = '''
::: tip CastleType 社による 202 個の優美なアンパサンド（&）異体字（Figure D-6）
![CastleType 的 202 个花体 Ampersand 字符全景（Figure D-6）](/images/fonts-encodings/fig-app-d6.png)
*CastleType 的 202 个花体 Ampersand 字符全景（Figure D-6）*
:::

*図 D-6：CastleType ファウンドリによる 202 個のカリグラフィ的アンパサンド（&）合字群。*
'''

fig_d8 = '''
::: tip Apple Skia フォントの wght 軸における連続変形（Figure D-8）
![Apple Skia 字体在 wght 轴上的连续变形全景（Figure D-8）](/images/fonts-encodings/fig-app-d8.png)
*Apple Skia 字体在 wght 轴上的连续变形全景（Figure D-8）*
:::

*図 D-8：Apple AAT バリアブルフォント Skia の太さ（`wght`）軸に沿った滑らかな連続補間。*
'''

fig_e1 = '''
::: tip Courier フォントにおける TrueType 命令制御グリッド（Figure E-1）
![Courier 字体在 TrueType 虚拟机下的指令控制点阵（Figure E-1）](/images/fonts-encodings/fig-app-e1.png)
*Courier 字体在 TrueType 虚拟机下的指令控制点阵（Figure E-1）*
:::

*図 E-1：Courier フォントの大文字 ‘T’ における TrueType 命令によるグリッド適合。*
'''

fig_e2 = '''
::: tip Verdana 文字 ‘O’ における MIRP 命令による輪郭制御（Figure E-2）
![Verdana 字母 ‘O’ 在 MIRP 指令控制下的轮廓拟合（Figure E-2）](/images/fonts-encodings/fig-app-e2.png)
*Verdana 字母 ‘O’ 在 MIRP 指令控制下的轮廓拟合（Figure E-2）*
:::

*図 E-2：Verdana 文字 ‘O’ における `MIRP[10110]` 命令による CVT 参照値との距離固定。*
'''

fig_f1 = '''
::: tip METAFONT 伝統の Computer Modern 書体系統樹（Figure F-1）
![METAFONT 原始 Computer Modern 字体家族谱系（1/2）（Figure F-1）](/images/fonts-encodings/fig-app-f1.png)
*METAFONT 原始 Computer Modern 字体家族谱系（1/2）（Figure F-1）*
:::

*図 F-1：クヌースによるオリジナルの Computer Modern フォントファミリー系統樹。*
'''

# Clean existing figures in ja if any
ja = re.sub(r'::: tip [^\n]*\n!\[[^\n]*\n\*[^\n]*\n:::\n\n\*[^\n]*\*\n', '', ja)

# Insert at precise locations
ja = ja.replace('### 1. `FONT` と `NFNT` リソースヘッダー構造', fig_a1 + '\n### 1. `FONT` と `NFNT` リソースヘッダー構造')
ja = ja.replace('### 3. Unix および X11 体系：Adobe BDF と PCF 形式', fig_a2 + '\n### 3. Unix および X11 体系：Adobe BDF と PCF 形式')
ja = ja.replace('### 1. GF（Generic Font）形式', fig_a3 + '\n### 1. GF（Generic Font）形式')

ja = ja.replace('## C.1 PostScript 仮想マシンの状態スタック', '## C.1 PostScript 仮想マシンの状態スタック\n' + fig_c1 + '\n' + fig_c2)
ja = ja.replace('### 2. Type 1 CharString 命令コード全表', fig_c7 + '\n' + fig_c9 + '\n' + fig_c10 + '\n' + fig_c11 + '\n### 2. Type 1 CharString 命令コード全表')
ja = ja.replace('## C.3 CFF（Compact Font Format）と Type 2 CharStrings', '## C.3 CFF（Compact Font Format）と Type 2 CharStrings\n' + fig_c12 + '\n' + fig_c16)

ja = ja.replace('## D.2 中核基本データテーブル', '## D.2 中核基本データテーブル\n' + fig_d1 + '\n' + fig_d3)
ja = ja.replace('### 2. カバレッジテーブル（Coverage Table）とクラス定義テーブル（ClassDef Table）', '### 2. カバレッジテーブル（Coverage Table）とクラス定義テーブル（ClassDef Table）\n' + fig_d6 + '\n' + fig_d8)

ja = ja.replace('## E.2 ペン（Pens）と包絡線理論（Envelopes）', '## E.2 ペン（Pens）と包絡線理論（Envelopes）\n' + fig_f1)
ja = ja.replace('## F.2 中核命令全集分類', '## F.2 中核命令全集分類\n' + fig_e1 + '\n' + fig_e2)

# Ensure translator line
ja = re.sub(r'\*?翻訳者：.*?\n', '*翻訳者：[Lycoris \\<lycorismisaka@gmail.com\\>](mailto:lycorismisaka@gmail.com)*\n\n', ja)

with open('docs/ja/fonts-encodings/appendices.md', 'w', encoding='utf-8') as f:
    f.write(ja)

print(f"docs/ja/fonts-encodings/appendices.md updated: {len(ja)} chars")
