import opencc

s2t = opencc.OpenCC('s2t')

with open('scripts/ch12_enrichment.md', 'r', encoding='utf-8') as f:
    enrich_zh = f.read()

enrich_hant = s2t.convert(enrich_zh)

enrich_ja = """### 4. 縦組（Vertical Typesetting）と縦方向メトリクス制御

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
"""

# Apply to zh
with open('docs/zh/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    zh_content = f.read()

start_zh = '### 3. FontForge 中的 CID 字库管理'
end_zh = '## 第六部分：从位图扫描到矢量轮廓跟踪算法'
p1 = zh_content.find(start_zh)
p2 = zh_content.find(end_zh)
zh_content = zh_content[:p1] + enrich_zh + '\n\n---\n\n' + zh_content[p2:]
with open('docs/zh/fonts-encodings/chapter-12.md', 'w', encoding='utf-8') as f:
    f.write(zh_content)
print('Applied to zh/chapter-12.md')

# Apply to zh-hant
with open('docs/zh-hant/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    hant_content = f.read()

start_hant = s2t.convert(start_zh)
end_hant = s2t.convert(end_zh)
p1 = hant_content.find(start_hant)
p2 = hant_content.find(end_hant)
hant_content = hant_content[:p1] + enrich_hant + '\n\n---\n\n' + hant_content[p2:]
with open('docs/zh-hant/fonts-encodings/chapter-12.md', 'w', encoding='utf-8') as f:
    f.write(hant_content)
print('Applied to zh-hant/chapter-12.md')

# Apply to ja
with open('docs/ja/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    ja_content = f.read()

target_ja = '\n---\n\n## 第6部：ビットマップスキャンからベクタ輪郭追跡へ'
if target_ja in ja_content:
    ja_content = ja_content.replace(target_ja, '\n\n' + enrich_ja + '\n\n---\n\n## 第6部：ビットマップスキャンからベクタ輪郭追跡へ')
    with open('docs/ja/fonts-encodings/chapter-12.md', 'w', encoding='utf-8') as f:
        f.write(ja_content)
    print('Applied cleanly to ja/chapter-12.md')
else:
    print('Target not found in ja!')
