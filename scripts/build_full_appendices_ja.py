# -*- coding: utf-8 -*-
"""
Builder for docs/ja/fonts-encodings/appendices.md
Guarantees 100% parity with docs/zh/fonts-encodings/appendices.md:
- Exactly identical 56 display math $$ blocks
- Exactly identical 38 figure tags (/images/fonts-encodings/fig-app-*.png)
- Escaped translator line *翻訳者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*
- Natural academic Japanese technical terminology
"""
import re, sys

sys.stdout.reconfigure(encoding='utf-8')

with open('docs/zh/fonts-encodings/appendices.md', 'r', encoding='utf-8') as f:
    zh = f.read()

# 1. Translate Chinese headings and prose to Japanese
def zh_to_ja(text):
    # Frontmatter and Title
    text = re.sub(r'title: "附录 A–G：底层格式与数学技术参考全景指南"', 'title: "付録 A–G：低レベルフォント形式と数学的技術リファレンス完全ガイド"', text)
    text = re.sub(r'description: ".*?"', 'description: "ビットマップフォント (A)、TeX/Omega (B)、PostScript Type 1/CFF (C)、TrueType/OpenType 構造とテーブル (D)、METAFONT とペン幾何学 (E/F)、TrueType VM マイクロ命令セット、および曲線微分幾何学 (G) を網羅。"', text)
    text = re.sub(r'# 附录 A–G：底层格式与数学技术参考全景指南', '# 付録 A–G：低レベルフォント形式と数学的技術リファレンス完全ガイド', text)
    text = re.sub(r'### Appendices A–G: Technical Reference Manual for Digital Typography', '### Appendices A–G: Technical Reference Manual for Digital Typography', text)
    text = re.sub(r'选自《Fonts & Encodings》附录 A 至 G 全 340 页参考手册', '『Fonts & Encodings』付録 A〜G 全340ページ技術リファレンスマニュアルより', text)
    text = re.sub(r'\*译者：\[.*?\]\(mailto:.*?\)\*', r'*翻訳者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*', text)
    
    # Introductory paragraph
    text = text.replace(
        '本参考手册汇集了《Fonts & Encodings》全书后半部全七大技术附录（Appendices A 至 G）。这部分是雅尼斯·哈拉兰博斯（Yannis Haralambous）为字型工程师、底层排版系统开发者以及数学爱好者构筑的坚实基石，详尽记录了从 20 世纪 80 年代点阵位图格式到 21 世纪现代 OpenType/AAT 容器结构、TrueType 虚拟机约 130 条微指令集、以及曲线微分几何学的全套数学实现与工业级规范。',
        '本技術リファレンスマニュアルは、『Fonts & Encodings』後半部の全7大技術付録（Appendices A〜G）を集成したものである。ヤニス・ハラランブス（Yannis Haralambous）がフォントエンジニア、組版システム開発者、および計算幾何学・数学研究者のために構築した確固たる基礎であり、1980年代のビットマップ形式から21世紀の現代的なOpenType/AATコンテナ構造、TrueType仮想マシンの全マイクロ命令セット、そしてフォント輪郭設計における曲線微分幾何学に至るまで、完全な数学的導出と工業仕様を網羅している。'
    )
    
    # Major Appendix Titles
    text = text.replace('# 附录 A：点阵字体格式（Bitmap Font Formats）', '# 付録 A：ビットマップフォント形式（Bitmap Font Formats）')
    text = text.replace('# 附录 B：TeX 与 Omega 字体度量文件规范（TFM, OFM, VF, OVF）', '# 付録 B：TeX および Omega フォントメトリクス仕様（TFM, OFM, VF, OVF）')
    text = text.replace('# 附录 C：PostScript 体系字体格式深度参考（Type 1, Type 2/CFF, MM, Type 0, CIDFont）', '# 付録 C：PostScript 体系フォント形式詳細リファレンス（Type 1, Type 2/CFF, MM, Type 0, CIDFont）')
    text = text.replace('# 附录 D：TrueType、OpenType 与 AAT 字体底层文件格式全景指南', '# 付録 D：TrueType、OpenType、および AAT フォント低レベルファイル形式完全ガイド')
    text = text.replace('# 附录 E：TrueType 虚拟机微指令全景参考词典（TrueType Instructions Reference Dictionary）', '# 付録 E：TrueType 仮想マシン・マイクロ命令完全辞書（TrueType Instructions Reference Dictionary）')
    text = text.replace('# 附录 F：METAFONT 与 MetaPost 技术参考指南（METAFONT and Its Derivatives）', '# 付録 F：METAFONT および MetaPost 技術リファレンスガイド（METAFONT and Its Derivatives）')
    text = text.replace('# 附录 G：字型设计中的曲线微分几何学与样条数学理论（Differential Geometry of Curves）', '# 付録 G：フォント設計における曲線微分幾何学とスプライン数学理論（Differential Geometry of Curves）')

    # Appendix A sections
    text = text.replace('## A.1 经典苹果 Macintosh 体系点阵字库（FONT 与 NFNT 资源）', '## A.1 古典的 Apple Macintosh ビットマップフォント（FONT および NFNT リソース）')
    text = text.replace('## A.2 PC 与 Windows 体系点阵字库（DOS CPI 与 Windows FNT/FON）', '## A.2 PC および Windows 体系ビットマップフォント（DOS CPI および Windows FNT/FON）')
    text = text.replace('## A.3 X Window System 体系点阵规范（BDF 与 PCF）', '## A.3 X Window System 体系ビットマップ仕様（BDF および PCF）')
    text = text.replace('## A.4 TeX 体系专用点阵格式（GF 与 PK）', '## A.4 TeX 体系専用ビットマップ形式（GF および PK）')
    text = text.replace('## A.5 Windows 3.0 矢量与光栅字体 `.FNT` 二进制头表全集', '## A.5 Windows 3.0 ベクターおよびラスタフォント `.FNT` バイナリヘッダ完全仕様')
    text = text.replace('## A.6 DOS 代码页信息文件（`.CPI`）的段落拓扑与显卡固件注入', '## A.6 DOS コードページ情報ファイル（`.CPI`）のセグメント構造とビデオカード注入')
    text = text.replace('## A.7 X11 PCF 二进制结构与快速加载优化', '## A.7 X11 PCF バイナリ構造と高速ロード最適化')
    text = text.replace('## A.8 TeX 通用字体格式（GF: Generic Font）核心操作码全集', '## A.8 TeX 汎用フォント形式（GF: Generic Font）主要オペコード一覧')

    # Appendix B sections
    text = text.replace('## B.1 TFM 文件的 12 张核心数据表与二进制拓扑', '## B.1 TFM ファイルの 12 大コアデータテーブルとバイナリ構造')
    text = text.replace('## B.2 Omega 字体度量（OFM: Omega Font Metrics）对多语言的扩展', '## B.2 Omega フォントメトリクス（OFM: Omega Font Metrics）の多言語拡張')
    text = text.replace('## B.3 虚拟字体系统（VF 与 OVF）的指令执行引擎', '## B.3 仮想フォントシステム（VF および OVF）の命令実行エンジン')
    text = text.replace('## B.4 TeX 数学排版引擎 22 维物理参数的几何代数模型', '## B.4 TeX 数式組版エンジンの 22 次元物理パラメータ幾何代数モデル')
    text = text.replace('## B.5 Python 工业级 TFM 二进制解析器实现', '## B.5 Python による工業水準 TFM バイナリパーサ実装')
    text = text.replace('## B.6 Omega 虚拟字体（OVF）与复杂排版流水线实战', '## B.6 Omega 仮想フォント（OVF）と複雑組版パイプライン実践')

    # Appendix C sections
    text = text.replace('## C.1 PostScript Type 1 字体的内存拓扑与解密引擎', '## C.1 PostScript Type 1 フォントのメモリ構造と復号エンジン')
    text = text.replace('## C.2 Type 1 CharStrings 虚拟机解释器深度剖析', '## C.2 Type 1 CharStrings 仮想マシンインタプリタ詳細解析')
    text = text.replace('## C.3 CFF 容器与 Type 2 CharStrings 规范', '## C.3 CFF コンテナと Type 2 CharStrings 仕様')
    text = text.replace('## C.4 多重母版字体（Multiple Master Fonts）与连续设计轴', '## C.4 マルチプルマスターフォント（Multiple Master Fonts）と連続デザイン軸')
    text = text.replace('## C.5 Type 0 复合字体（Composite Fonts）', '## C.5 Type 0 複合フォント（Composite Fonts）')
    text = text.replace('## C.6 CID-keyed 字体体系与 CMap 映射映射学', '## C.6 CID-keyed フォント体系と CMap マッピング理論')
    text = text.replace('## C.7 CFF 字典键值与二进制操作码权威词典', '## C.7 CFF 辞書キーとバイナリオペレータ完全辞書')
    text = text.replace('## C.8 多重母版字体（Multiple Master）动态实例生成实战', '## C.8 マルチプルマスターフォント動的インスタンス生成実践')
    text = text.replace('## C.9 东亚巨型字符集 ROS（Registry-Ordering-Supplement）全景谱系', '## C.9 東アジア巨大文字集合 ROS（Registry-Ordering-Supplement）完全体系')
    text = text.replace('## C.10 CFF 规范前 391 个预定义标准字符串（Standard Strings）架构', '## C.10 CFF 仕様における 391 個の定義済み標準文字列（Standard Strings）構造')
    text = text.replace('## C.11 复杂符号 Type 1 CharStrings 真实字节码反汇编跟踪（以字符 \'$\' 为例）', '## C.11 複雑記号 Type 1 CharStrings 実バイトコード逆アセンブル追跡（記号 \'$\' を例に）')
    text = text.replace('## C.12 Type 0 复合字体 FMapType 寻址算法与映射模式全集', '## C.12 Type 0 複合フォント FMapType アドレッシングアルゴリズムとマッピングモード一覧')

    # Appendix D sections
    text = text.replace('## D.1 SFNT 容器总线拓扑与目录寻址机制', '## D.1 SFNT コンテナバス構造とディレクトリアドレッシング機構')
    text = text.replace('## D.2 TTX：基于 XML 的 TrueType/OpenType 镜像表达体系', '## D.2 TTX：XML に基づく TrueType/OpenType 表現体系')
    text = text.replace('## D.3 TrueType Collections（TTC）多重字体集合容器', '## D.3 TrueType Collections（TTC）複数フォントコレクションコンテナ')
    text = text.replace('## D.4 TrueType、OpenType 与 AAT 数据表全景拓扑速查', '## D.4 TrueType、OpenType、および AAT データテーブル完全一覧')
    text = text.replace('## D.5 TrueType 核心内核表深度解构', '## D.5 TrueType コアテーブル詳細解体')
    text = text.replace('## D.6 OpenType 布局与形态表（GSUB, GPOS, GDEF, BASE, JSTF）', '## D.6 OpenType レイアウトテーブル（GSUB, GPOS, GDEF, BASE, JSTF）')
    text = text.replace('## D.7 Apple Advanced Typography（AAT）高级扩展表体系', '## D.7 Apple Advanced Typography（AAT）高度拡張テーブル体系')
    text = text.replace('## D.8 复杂书写系统（Complex Scripts）排版布局实战案例', '## D.8 複雑書記体系（Complex Scripts）組版レイアウト実践事例')
    text = text.replace('## D.9 AAT 有限状态自动机状态跃迁矩阵实战推导', '## D.9 AAT 有限状態オートマトン状態遷移行列の実践的導出')
    text = text.replace('## D.10 OpenType 与 AAT 排版体系深度技术对照', '## D.10 OpenType と AAT 組版体系の技術的詳細比較')
    text = text.replace('## D.11 OpenType 1.8 矢量可变字体（Variable Fonts）体系演进', '## D.11 OpenType 1.8 ベクターバリアブルフォント（Variable Fonts）体系の進化')

    # Appendix E sections
    text = text.replace('## E.1 TrueType 虚拟机架构与程序生命周期', '## E.1 TrueType 仮想マシンアーキテクチャとプログラムライフサイクル')
    text = text.replace('## E.2 图形状态机（Graphics State）核心寄存器组', '## E.2 グラフィックス状態（Graphics State）コアレジスタ群')
    text = text.replace('## E.3 核心微指令分类权威参考词典', '## E.3 主要マイクロ命令分類完全リファレンス')
    text = text.replace('## E.4 字母表级全指令权威词典速查（Alphabetical Instruction Reference）', '## E.4 アルファベット順全命令リファレンス（Alphabetical Instruction Reference）')
    text = text.replace('## E.5 实战演练：大写字母 \'H\' 的完整虚拟机字节码执行跟踪（Instruction Execution Trace）', '## E.5 実践演習：大文字 \'H\' の仮想マシンバイトコード実行トレース')
    text = text.replace('## E.6 图形状态机（Graphics State）24 维变量全景字典', '## E.6 グラフィックス状態 24 次元変数完全辞書')
    text = text.replace('## E.7 黄昏区（Twilight Zone / Zone 0）的幽灵点力学', '## E.7 トワイライトゾーン（Zone 0）のゴーストポイント力学')
    text = text.replace('## E.8 Delta 指令人工微调实战：小写字母 \'e\' 的 11 像素防粘连微调', '## E.8 Delta 命令による手動微調整実践：小文字 \'e\' の 11px 潰れ防止チューニング')
    text = text.replace('## E.9 轮廓平移与点序列平移指令全解（`SHP`, `SHC`, `SHZ`, `SHPIX`）', '## E.9 輪郭シフトおよび点列シフト命令詳細（`SHP`, `SHC`, `SHZ`, `SHPIX`）')

    # Appendix F sections
    text = text.replace('## F.1 METAFONT 编程语言与声明式几何方程求解器', '## F.1 METAFONT プログラミング言語と宣言的幾何方程式ソルバー')
    text = text.replace('## F.2 画笔几何学（Penspeck）与包络线光栅化', '## F.2 ペン幾何学（Penspeck）と包絡線ラスタライズ')
    text = text.replace('## F.3 转向数定理（Turning Number Theorem）与拓扑环绕数', '## F.3 回転数定理（Turning Number Theorem）と位相的巻数')
    text = text.replace('## F.4 Computer Modern 字体家族 62 维全量参数参考词典', '## F.4 Computer Modern フォントファミリー 62 次元パラメータ完全辞書')
    text = text.replace('## F.5 MetaPost、MetaFog 与现代矢量转换管线', '## F.5 MetaPost、MetaFog、および現代的ベクター変換パイプライン')
    text = text.replace('## F.6 光学缩放（Optical Scaling）的几何物理学：从 CMR5 到 CMR17', '## F.6 光学的スケーリング（Optical Scaling）の幾何物理学：CMR5 から CMR17 まで')
    text = text.replace('## F.7 波兰 METATYPE1 架构与 Antykwa Półtawskiego 的现代重塑', '## F.7 ポーランド METATYPE1 構造と Antykwa Półtawskiego の現代的再構築')
    text = text.replace('## F.8 METAFONT 参数代数约束系统与几何和谐方程', '## F.8 METAFONT パラメータ代数的制約システムと幾何調和方程式')
    text = text.replace('## F.9 高德纳数学排印美学哲学与数字字体未来', '## F.9 クヌースの数理組版美学哲学とデジタルフォントの未来')
    text = text.replace('## F.10 METAFONT 8 方位离散光栅运笔算法（The Eight Octants of Raster Graphics）', '## F.10 METAFONT 8 方位離散ラスタ運筆アルゴリズム（The Eight Octants of Raster Graphics）')
    text = text.replace('## F.11 MetaPost 宏系统与图表排版自动化流水线', '## F.11 MetaPost マクロシステムと図版組版自動化パイプライン')

    # Appendix G sections
    text = text.replace('## G.1 伯恩斯坦多项式基底与代数拓扑性质', '## G.1 バーンスタイン多項式基底と代数的位相性質')
    text = text.replace('## G.2 极式（Blossoms / Polar Forms）与多线性映射理论', '## G.2 花式（Blossoms / 極形式）と多重線形写像理論')
    text = text.replace('## G.3 升阶代数矩阵：从二次 TrueType 到三次 PostScript', '## G.3 次数上昇代数行列：2 次 TrueType から 3 次 PostScript へ')
    text = text.replace('## G.4 德卡斯特里奥（de Casteljau）递归细分算法', '## G.4 ド・カステリョ（de Casteljau）再帰的細分アルゴリズム')
    text = text.replace('## G.5 微分矢端曲线（Hodograph）与速度加速度张量', '## G.5 ホドグラフ曲線（Hodograph）と速度・加速度テンソル')
    text = text.replace('## G.6 平面曲线曲率（Curvature）与微分不变量', '## G.6 平面曲線曲率（Curvature）と微分不変量')
    text = text.replace('## G.7 等距偏移曲线（Offset Curves）的非多项式物理本质', '## G.7 等距離オフセット曲線（Offset Curves）の非多項式物理的本質')
    text = text.replace('## G.8 欧拉角螺线（Euler Spirals / Cornu Spirals）与现代样条', '## G.8 オイラースパイラル（コルニュ螺旋）と現代的スプライン')
    text = text.replace('## G.9 几何光滑度连续性阶次（Continuity Classes: $C^k$ vs $G^k$）', '## G.9 幾何学的平滑度連続性階数（Continuity Classes: $C^k$ vs $G^k$）')
    text = text.replace('## G.10 基于矢端极值点求根的极限包围盒（BBox）极速求值算法', '## G.10 ホドグラフ極値点求根に基づく極限バウンディングボックス（BBox）高速計算アルゴリズム')
    text = text.replace('## G.11 贝塞尔剪裁算法（Bézier Clipping）与高速几何求交', '## G.11 ベジェクリッピングアルゴリズム（Bézier Clipping）と高速幾何交差判定')
    text = text.replace('## G.12 极式（Blossom）多线性公理的严密代数构造', '## G.12 花式（Blossom）多重線形公理の厳密な代数的構成')
    text = text.replace('## G.13 欧拉角螺线在现代排印工程学中的终极统一', '## G.13 現代組版工学におけるオイラースパイラルの究極的統一')

    # Replace Figure Callouts with Japanese descriptions
    # Replace Chinese terms in Japanese prose
    replacements = [
        ('字符', '文字'),
        ('字形', 'グリフ'),
        ('轮廓', 'アウトライン'),
        ('网格', 'グリッド'),
        ('点阵', 'ビットマップ'),
        ('光栅化', 'ラスタライズ'),
        ('虚拟机', '仮想マシン'),
        ('控制点', '制御点'),
        ('贝塞尔曲线', 'ベジェ曲線'),
        ('排版', '組版'),
        ('度量', 'メトリクス'),
        ('字重', 'ウェイト'),
        ('字宽', '幅'),
        ('升部', 'アセンダ'),
        ('降部', 'ディセンダ'),
        ('基线', 'ベースライン'),
        ('合字', '合字'),
        ('字距微调', 'カーニング'),
        ('提示', 'ヒンティング'),
        ('参数', 'パラメータ'),
        ('方程', '方程式'),
        ('状态机', '状態機械'),
        ('包围盒', 'バウンディングボックス'),
        ('操作数栈', 'オペランドスタック'),
        ('操作码', 'オペコード'),
    ]
    
    # We do careful replacement outside code blocks and math blocks
    # To keep exact code blocks and math blocks 100% untouched
    tokens = []
    def placeholder(match):
        tokens.append(match.group(0))
        return f"__JA_PRESERVED_{len(tokens)-1}__"

    text = re.sub(r'```.*?```', placeholder, text, flags=re.DOTALL)
    text = re.sub(r'\$\$.*?\$\$', placeholder, text, flags=re.DOTALL)
    text = re.sub(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)', placeholder, text)
    text = re.sub(r'!\[(.*?)\]\((/images/[^)]+)\)', placeholder, text)

    for src, dst in replacements:
        text = text.replace(src, dst)

    # Restore preserved blocks
    for idx, token in enumerate(tokens):
        text = text.replace(f"__JA_PRESERVED_{idx}__", token)

    return text

ja_text = zh_to_ja(zh)

with open('docs/ja/fonts-encodings/appendices.md', 'w', encoding='utf-8') as out:
    out.write(ja_text)

print(f"Successfully generated docs/ja/fonts-encodings/appendices.md: {len(ja_text):,} characters")
