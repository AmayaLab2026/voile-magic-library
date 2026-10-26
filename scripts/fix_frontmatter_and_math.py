# -*- coding: utf-8 -*-
"""
Fix YAML frontmatter and KaTeX formulas across chapter-9, chapter-12, chapter-14, appendices in zh, zh-hant, ja.
"""
import os, sys, re

meta = {
    'chapter-9.md': {
        'zh': {
            'title': '第 9 章：TeX 与 Omega 中的字体及其安装与使用',
            'desc': '详尽解析 TeX 的盒子-胶水物理模型、折行算法、NFSS、DVI 格式、afm2tfm、fontinst 虚拟字体合成与 Omega 16位多向排版。'
        },
        'zh-hant': {
            'title': '第 9 章：TeX 與 Omega 中的字型及其安裝與使用',
            'desc': '詳盡解析 TeX 的盒子-膠水物理模型、斷行演算法、NFSS、DVI 格式、afm2tfm、fontinst 虛擬字型合成與 Omega 16位元多向排版。'
        },
        'ja': {
            'title': '第 9 章：TeX と Omega におけるフォントとそのインストールおよび使用',
            'desc': 'TeX のボックス・グルーモデル、改行アルゴリズム、NFSS、DVI 形式、afm2tfm、fontinst 仮想フォント合成、Omega の16ビット多方向組版を詳解。'
        }
    },
    'chapter-12.md': {
        'zh': {
            'title': '第 12 章：字体的编辑与创建',
            'desc': '系统剖析 FontLab Studio、FontForge、贝塞尔曲线几何、度量类、Python 脚本批处理与 PostScript BlueValues 提示系统。'
        },
        'zh-hant': {
            'title': '第 12 章：字型的編輯與建立',
            'desc': '系統剖析 FontLab Studio、FontForge、貝塞爾曲線幾何、度量類、Python 腳本批次處理與 PostScript BlueValues 提示系統。'
        },
        'ja': {
            'title': '第 12 章：フォントの編集と新規作成',
            'desc': 'FontLab Studio、FontForge、ベジェ曲線幾何学、メトリッククラス、Python スクリプト自動化、PostScript BlueValues ヒンティングを詳解。'
        }
    },
    'chapter-14.md': {
        'zh': {
            'title': '第 14 章：赋予字体智慧：高级排版技术',
            'desc': '深入 OpenType 与 Apple Advanced Typography (AAT) 架构，剖析 AFDKO 语法、VOLT 视觉化定位与 FontForge 状态机实战。'
        },
        'zh-hant': {
            'title': '第 14 章：賦予字型智慧：進階排版技術',
            'desc': '深入 OpenType 與 Apple Advanced Typography (AAT) 架構，剖析 AFDKO 語法、VOLT 視覺化定位與 FontForge 狀態機實戰。'
        },
        'ja': {
            'title': '第 14 章：フォントに知性を宿す：高度組版技術',
            'desc': 'OpenType および Apple Advanced Typography (AAT) のアーキテクチャ、AFDKO 構文、VOLT、FontForge 状態機械の実践を詳解。'
        }
    },
    'appendices.md': {
        'zh': {
            'title': '附录 A–G：底层格式与数学全景技术参考手册',
            'desc': '涵盖位图字体 (A)、TeX/Omega (B)、PostScript Type 1/CFF (C)、TrueType/OpenType 表目录 (D)、METAFONT (E)、TrueType 虚拟机指令集 (F) 与曲线微分几何 (G)。'
        },
        'zh-hant': {
            'title': '附錄 A–G：底層格式與數學全景技術參考手冊',
            'desc': '涵蓋點陣字型 (A)、TeX/Omega (B)、PostScript Type 1/CFF (C)、TrueType/OpenType 表目錄 (D)、METAFONT (E)、TrueType 虛擬機指令集 (F) 與曲線微分幾何 (G)。'
        },
        'ja': {
            'title': '付録 A–G：低レベルフォーマットと数学的基礎技術リファレンスマニュアル',
            'desc': 'ビットマップフォント (A)、TeX/Omega (B)、PostScript Type 1/CFF (C)、TrueType/OpenType テーブル構造 (D)、METAFONT (E)、TrueType 仮想マシン命令セット (F)、曲線微分幾何学 (G)。'
        }
    }
}

# Function to fix frontmatter
for fname, lang_dict in meta.items():
    for lang, m in lang_dict.items():
        fpath = f"docs/{lang}/fonts-encodings/{fname}"
        if not os.path.exists(fpath):
            continue
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Strip existing frontmatter if any
        if content.startswith('---'):
            parts = content.split('---', 2)
            if len(parts) >= 3:
                content = parts[2].lstrip()
        
        # Replace broken \text tabs with \text{...}
        content = content.replace('\text{', '\\text{')
        content = content.replace('\to', '\\to')
        content = content.replace('\times', '\\times')
        content = content.replace('\approx', '\\approx')
        content = content.replace('\begin{pmatrix}', '\\begin{pmatrix}')
        content = content.replace('\end{pmatrix}', '\\end{pmatrix}')

        frontmatter = f"""---
title: "{m['title']}"
description: "{m['desc']}"
---

"""
        new_content = frontmatter + content
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Fixed frontmatter in {fpath}")

print("Frontmatter fix complete.")
