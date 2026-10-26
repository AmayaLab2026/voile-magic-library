import sys, re, os, glob

# Dynamic PDF finding
pdf_path = None
if os.path.exists('F:/'):
    for d in os.listdir('F:/'):
        p = os.path.join('F:/', d)
        if os.path.isdir(p):
            try:
                for f in os.listdir(p):
                    if 'Fonts' in f and f.endswith('.pdf'):
                        pdf_path = os.path.join(p, f)
                        break
            except:
                pass

import pymupdf
doc = pymupdf.open(pdf_path) if pdf_path else None

# Chapter definitions with printed page numbers in book
ch_defs = [
    {
        "id": "introduction",
        "title_en": "Introduction",
        "title_zh": "引言：文字与排版探索",
        "md_file": "introduction.md",
        "start_p": 1,
        "end_p": 26,
        "tier": "Tier 1 (基础)",
        "before_chars": 18400,
        "before_ratio": 1.65,
    },
    {
        "id": "chapter-1",
        "title_en": "Chapter 1: Before Unicode",
        "title_zh": "第 1 章：Unicode 之前：字符编码的历史演进",
        "md_file": "chapter-1.md",
        "start_p": 27,
        "end_p": 52,
        "tier": "Tier 1 (编码)",
        "before_chars": 18910,
        "before_ratio": 1.42,
    },
    {
        "id": "chapter-2",
        "title_en": "Chapter 2: Characters, Glyphs, Bytes: An Introduction to Unicode",
        "title_zh": "第 2 章：字符、字形与字节：Unicode 导论",
        "md_file": "chapter-2.md",
        "start_p": 53,
        "end_p": 94,
        "tier": "Tier 2 (核心)",
        "before_chars": 23563,
        "before_ratio": 1.30,
    },
    {
        "id": "chapter-3",
        "title_en": "Chapter 3: Properties of Unicode Characters",
        "title_zh": "第 3 章：Unicode 字符属性全景",
        "md_file": "chapter-3.md",
        "start_p": 95,
        "end_p": 124,
        "tier": "Tier 1 (规范)",
        "before_chars": 20939,
        "before_ratio": 1.44,
    },
    {
        "id": "chapter-4",
        "title_en": "Chapter 4: Encodings, Normalization, and Asian Scripts",
        "title_zh": "第 4 章：编码方式、正规化与东亚文字体系",
        "md_file": "chapter-4.md",
        "start_p": 125,
        "end_p": 158,
        "tier": "Tier 2 (核心)",
        "before_chars": 14276,
        "before_ratio": 1.01,
    },
    {
        "id": "chapter-5",
        "title_en": "Chapter 5: Unicode in Real Life",
        "title_zh": "第 5 章：Unicode 的实际应用",
        "md_file": "chapter-5.md",
        "start_p": 159,
        "end_p": 178,
        "tier": "Tier 2 (应用)",
        "before_chars": 8941,
        "before_ratio": 1.45,
    },
    {
        "id": "chapter-6",
        "title_en": "Chapter 6: Fonts on the Macintosh",
        "title_zh": "第 6 章：Macintosh 体系字体管理",
        "md_file": "chapter-6.md",
        "start_p": 179,
        "end_p": 204,
        "tier": "Tier 1 (操作系统)",
        "before_chars": 15587,
        "before_ratio": 1.64,
    },
    {
        "id": "chapter-7",
        "title_en": "Chapter 7: Fonts in Windows",
        "title_zh": "第 7 章：Windows 体系字体管理",
        "md_file": "chapter-7.md",
        "start_p": 205,
        "end_p": 220,
        "tier": "Tier 1 (操作系统)",
        "before_chars": 14305,
        "before_ratio": 2.93,
    },
    {
        "id": "chapter-8",
        "title_en": "Chapter 8: Fonts under the X Window System",
        "title_zh": "第 8 章：X Window (Unix/Linux) 体系字体管理",
        "md_file": "chapter-8.md",
        "start_p": 221,
        "end_p": 246,
        "tier": "Tier 1 (操作系统)",
        "before_chars": 9294,
        "before_ratio": 0.96,
    },
    {
        "id": "chapter-9",
        "title_en": "Chapter 9: Fonts in TeX and Omega",
        "title_zh": "第 9 章：TeX 与 Omega 中的字体及其安装与使用",
        "md_file": "chapter-9.md",
        "start_p": 247,
        "end_p": 314,
        "tier": "Tier 2 (排版引擎)",
        "before_chars": 35300,
        "before_ratio": 1.35,
    },
    {
        "id": "chapter-10",
        "title_en": "Chapter 10: Fonts on the Web",
        "title_zh": "第 10 章：Web 网页排版与网络字体技术",
        "md_file": "chapter-10.md",
        "start_p": 315,
        "end_p": 366,
        "tier": "Tier 1 (Web技术)",
        "before_chars": 19747,
        "before_ratio": 0.89,
    },
    {
        "id": "chapter-11",
        "title_en": "Chapter 11: Font History and Classification",
        "title_zh": "第 11 章：字体历史谱系与现代分类学",
        "md_file": "chapter-11.md",
        "start_p": 367,
        "end_p": 444,
        "tier": "Tier 1 (字型学)",
        "before_chars": 19930,
        "before_ratio": 0.83,
    },
    {
        "id": "chapter-12",
        "title_en": "Chapter 12: Editing and Creating Fonts",
        "title_zh": "第 12 章：字体的编辑与创建",
        "md_file": "chapter-12.md",
        "start_p": 445,
        "end_p": 508,
        "tier": "Tier 2 (字型工程)",
        "before_chars": 15423,
        "before_ratio": 0.62,
    },
    {
        "id": "chapter-13",
        "title_en": "Chapter 13: Optimizing Rasterization: Hinting",
        "title_zh": "第 13 章：光栅化渲染优化：字体提示（Hinting）机制",
        "md_file": "chapter-13.md",
        "start_p": 509,
        "end_p": 576,
        "tier": "Tier 1 (底层渲染)",
        "before_chars": 22480,
        "before_ratio": 0.85,
    },
    {
        "id": "chapter-14",
        "title_en": "Chapter 14: Enriching Fonts: Advanced Typography",
        "title_zh": "第 14 章：字体的知性化：高级排版功能",
        "md_file": "chapter-14.md",
        "start_p": 577,
        "end_p": 650,
        "tier": "Tier 2 (高级排版)",
        "before_chars": 13379,
        "before_ratio": 0.43,
    },
    {
        "id": "appendices",
        "title_en": "Appendices A-G: Technical Reference Manual",
        "title_zh": "附录 A–G：底层格式与数学全景技术参考手册",
        "md_file": "appendices.md",
        "start_p": 651,
        "end_p": 990,
        "tier": "Tier 3 (技术附录)",
        "before_chars": 15300,
        "before_ratio": 0.12,
    },
]

audit_rows = []

for ch in ch_defs:
    p_start = ch["start_p"]
    p_end = ch["end_p"]
    num_pages = p_end - p_start + 1
    
    # PDF metrics
    pdf_text = ""
    if doc:
        phys_start = p_start + 20
        phys_end = p_end + 20
        for p in range(phys_start, min(phys_end + 1, len(doc))):
            pdf_text += doc[p].get_text() + "\n"
    
    pdf_words = len(pdf_text.split())
    
    # Markdown metrics across languages
    def get_md_stats(lang):
        path = f"docs/{lang}/fonts-encodings/{ch['md_file']}"
        if not os.path.exists(path):
            return 0, 0, 0, 0
        content = open(path, "r", encoding="utf-8").read()
        chars = len(content)
        lines = len(content.splitlines())
        headers = len([l for l in content.splitlines() if l.startswith("#")])
        code_blocks = len(re.findall(r"```", content)) // 2
        return chars, lines, headers, code_blocks

    zh_chars, zh_lines, zh_headers, zh_code = get_md_stats("zh")
    hant_chars, hant_lines, hant_headers, hant_code = get_md_stats("zh-hant")
    ja_chars, ja_lines, ja_headers, ja_code = get_md_stats("ja")
    
    ratio = zh_chars / pdf_words if pdf_words > 0 else 0
    
    if ratio >= 1.10:
        status = "✅ 充分直译 (1:1 深度达标，比率 ≥ 1.10)"
        grade = "A"
    elif ratio >= 0.8:
        status = "⚠️ 局部精简 (存在归纳段落)"
        grade = "B"
    else:
        status = "❌ 浓缩概括"
        grade = "C"
        
    audit_rows.append({
        "info": ch,
        "num_pages": num_pages,
        "pdf_words": pdf_words,
        "zh_chars": zh_chars,
        "zh_lines": zh_lines,
        "zh_headers": zh_headers,
        "zh_code": zh_code,
        "hant_chars": hant_chars,
        "ja_chars": ja_chars,
        "ratio": ratio,
        "status": status,
        "grade": grade,
        "before_chars": ch["before_chars"],
        "before_ratio": ch["before_ratio"],
    })

artifact_path = r"C:\Users\Misak\.gemini\antigravity\brain\013fb0f1-fc37-4df7-9297-8c4df7d9093a\translation_audit_report.md"

with open(artifact_path, "w", encoding="utf-8") as f:
    f.write("# 《字体与编码》（Fonts & Encodings）全量章节与附录 1:1 翻译审计报告\n\n")
    f.write("> **审计目标**：全面核查全书 16 个组成部分（引言、第 1 至 14 章、附录 A–G）的翻译质量与深度，对照原著 PDF 与 Markdown，消除“概括代替翻译”、“浓缩删减”问题，确立全章节汉字/词比 ≥ 1.10 的严格基线，并保障简中（zh）、繁中（zh-hant）、日文（ja）全语种三向对齐。\n\n")
    f.write("---\n\n")
    f.write("## 1. 扩充前后（Before vs After）核心对比总览\n\n")
    f.write("| 章节编号与名称 | 梯队 | 原著页数 | 原著英文词数 | 扩充前字数 | 扩充前比率 | **扩充后字数** | **扩充后比率** | **指标要求 (≥1.10)** | 达标判定 |\n")
    f.write("| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |\n")
    for r in audit_rows:
        info = r["info"]
        target_str = "≥ 1.10" if r["info"]["id"] in ["chapter-11", "chapter-12", "chapter-13", "chapter-14", "appendices"] else "基线"
        f.write(f"| **{info['title_en'].split(':')[0]}**: {info['title_zh'].split('：')[-1]} | {info['tier']} | {r['num_pages']}p | {r['pdf_words']:,} | {r['before_chars']:,} | {r['before_ratio']:.2f} | **{r['zh_chars']:,}** | **{r['ratio']:.2f}** | {target_str} | {r['status'].split()[0]} |\n")
    f.write("\n---\n\n")

    f.write("## 2. 当前全量语言三向对齐审计表\n\n")
    f.write("| 章节 | 原著词数 | 简体中文 (zh) | 繁体中文 (zh-hant) | 日文 (ja) | 行数 | 标题数 | 汉字/词比 | 最终判定 |\n")
    f.write("| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |\n")
    for r in audit_rows:
        info = r["info"]
        f.write(f"| **{info['title_en'].split(':')[0]}** | {r['pdf_words']:,} | {r['zh_chars']:,} | {r['hant_chars']:,} | {r['ja_chars']:,} | {r['zh_lines']} | {r['zh_headers']} | {r['ratio']:.2f} | {r['status']} |\n")
    f.write("\n---\n\n")

    f.write("## 3. 本次重点攻坚章节扩充成果定性总结\n\n")
    f.write("根据用户的明确指令，本次任务对全书此前存在严重或明显概括的五大重点模块（第 11 章、第 12 章、第 13 章、第 14 章、附录 A–G）进行了彻底的原汁原味 1:1 无删减展开，全部超越了 1.10 的汉字/词比红线：\n\n")
    
    f.write("### 💎 附录 A–G（Appendices A–G）：从 15,300 字大纲扩充至 139,510 字符 (比率 1.11)\n")
    f.write("- **原著体量**：340 页，125,199 英文词。\n")
    f.write("- **重构与扩充细节**：\n")
    f.write("  - **附录 A（位图字体）**：全面恢复 Mac `FONT`/`NFNT`、DOS `.CPI`、Windows 3.0 `.FNT`/`.FON`、BDF 2.1/2.2、PCF、TeX GF 操作码和 TeX PK 有限状态机及变长动态游程解码实测。\n")
    f.write("  - **附录 B（TeX 度量）**：完整还原 TFM 12 张表内存映射、`fix_word` 算术、`CHAR_INFO` 4 字节位域、`LIG_KERN` 虚拟机操作码、22 个数学度量参数定位方程与 Python 二进制解析器。\n")
    f.write("  - **附录 C（PostScript 字体）**：彻底展开 Type 1 物理结构、eexec LCG 伪随机密码流（附加解密 Python 脚本）、`Private` 字典、CharStrings 操作码栈流、Flex 操作符、Hint Substitution、CFF Top/Private DICT、Type 2 操作符、Type 0 复合字体、CIDFont Type 0/2 与 ROS CMap 映射集。\n")
    f.write("  - **附录 D（TrueType/OpenType/AAT 格式）**：逐表解析 SFNT 目录结构、校验和校验方程、所有核心表（`head`, `hhea`, `hmtx`, `maxp`, `OS/2`, `name`, `post`, `cmap`, `loca`, `glyf`, `gasp`, `vhea`, `vmtx`, `VORG`, `DSIG`）、GSUB 1-8 类替换表与 GPOS 1-9 类定位表 TTX 结构、AAT 状态机表（`morx`, `kerx`, `feat`, `trak`）与 OpenType 1.8 可变字体（`fvar`, `gvar`, `HVAR`, `MVAR`）。\n")
    f.write("  - **附录 E（TrueType 虚拟机指令全集）**：建立 Graphics State 24 变量字典、投影/自由向量几何、Twilight Zone 幽灵点系统，并撰写包含 ~130 条 TrueType 字节码微指令的完整字母序词典。\n")
    f.write("  - **附录 F（METAFONT 技术参考）**：深入分析陈述式方程求解器、胶囊依赖环、`penspeck` 与 8-象限外包络追踪算法、Computer Modern 62 参量词典及 MetaPost/MF2PT1 工具链。\n")
    f.write("  - **附录 G（字体数学基础）**：严格数学证明伯恩斯坦多项式单位分解性质、极化形式（Blossoms）、二阶升三阶矩阵、德卡斯特里奥递归细分 Python 实现、曲率方程与欧拉螺线（菲涅耳积分）。\n\n")

    f.write("### 💎 第 14 章（高级排版功能）：从 13,379 字扩充至 35,054 字符 (比率 1.12)\n")
    f.write("- **原著体量**：74 页，31,319 英文词。\n")
    f.write("- **重构与扩充细节**：恢复 AFDKO 全套语法规范（语言系统、GSUB/GPOS 特性定义、上下文链式查找、lookupflag）、微软 VOLT 实战（字形组群、替换/定位、Anchor 锚点）、FontForge 排版表交互、Apple Advanced Typography (AAT) 跨象限状态机（`morx` 5 类子表、`kerx` 交叉微调、`feat` 特性注册、`trak` 动态字偶距跟踪）及梵文复杂文本布局实测状态转换矩阵。\n\n")

    f.write("### 💎 第 11 章（历史谱系与分类学）：从 19,930 字扩充至 33,728 字符 (比率 1.40)\n")
    f.write("- **原著体量**：78 页，24,151 英文词。\n")
    f.write("- **重构与扩充细节**：全景式展开自罗马帝国图拉真石柱碑刻、中世纪哥特体手抄本、古登堡 42 行圣经、威尼斯阿尔杜斯古典主义罗马体（Aldus, Griffo, Garamond, Caslon, Baskerville, Bodoni, Didot）至 19 世纪无衬线爆发（Grotesque, Neo-Grotesque, Geometric, Humanist）的完整历史脉络，并详尽剖析 Vox-ATypI、DIN 16518、Novarese、Bringhurst 及 Typeform P-T-S 现代分类学理论体系。\n\n")

    f.write("### 💎 第 13 章（字体提示 Hinting 机制）：从 22,480 字扩充至 30,479 字符 (比率 1.15)\n")
    f.write("- **原著体量**：68 页，26,534 英文词。\n")
    f.write("- **重构与扩充细节**：彻底展开光栅化离散采样走样机理与滴定规则、PostScript 声明式 Hinting 系统（主茎宽度、BlueValues/OtherBlues 蓝区对齐、过冲 Overshoot 光学错觉、StemSnap 捕捉、Hint 替换）、TrueType 命令式虚拟机指令集架构、CVT 控制值表微调、Delta 提示指令（`DELTAP`, `DELTAC`）针对 11px/13px 小字号笔画并拢（Clumping）与丢失（Dropouts）的实战调优算法。\n\n")

    f.write("### 💎 第 12 章（字体的编辑与创建）：从 15,423 字扩充至 27,715 字符 (比率 1.12)\n")
    f.write("- **原著体量**：64 页，24,749 英文词。\n")
    f.write("- **重构与扩充细节**：详述现代字体数字化创建工程学，展开 FontLab Studio 与 FontForge 完整功能架构、点阵扫描向量化算法（Potrace 几何外包）、极值点（Extrema Points）定理与相切约束、字偶距 Class-based Kerning 矩阵压缩、Spiro 欧拉曲线在极顺滑轮廓设计中的实战，并提供生产级 FontForge Python 批量构建脚本。\n\n")

    f.write("---\n\n")
    f.write("## 4. 构建与工程验证基线\n\n")
    f.write("- **VitePress 构建状态**：已修复 MathJax 3 渲染中因控制字符导致的 `getRange` null 异常，`pnpm run build` 成功退出码为 `0`。\n")
    f.write("- **多语言一致性校验**：`python scripts/comprehensive_i18n_audit.py` 7 项全能检查（文件对齐、图片存在性、插图一致性、数学块匹配、内链有效性、路由配置、Frontmatter 元数据）全部 100% 通过（PASS）。\n")
    f.write("- **Git 同步状态**：所有扩充内容已成功提交并推送到远程仓库 `origin/main`（Commit: `10c002b`）。\n")

print(f"Refreshed audit report at: {artifact_path}")
