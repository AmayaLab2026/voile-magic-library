# -*- coding: utf-8 -*-
"""
Fixes:
1. Frontmatter in chapter-14.md (zh, zh-hant, ja)
2. Link false positive \mathcal{B}[t^k](u_1, ...) in app_g.md and appendices.md (zh, zh-hant, ja)
"""

# 1. Frontmatter for chapter-14.md
fm_zh = """---
title: "第 14 章：丰富字体：高级排版功能"
description: "OpenType 与 AAT 高级排版功能深度解析：AFDKO 特性语法规范、微软 VOLT 工程实战、Apple Advanced Typography (AAT) 有限状态自动机、GSUB/GPOS 查找表体系。"
---

"""

fm_hant = """---
title: "第 14 章：豐富字體：高級排版功能"
description: "OpenType 與 AAT 高級排版功能深度解析：AFDKO 特性語法規範、微軟 VOLT 工程實戰、Apple Advanced Typography (AAT) 有限狀態自動機、GSUB/GPOS 查找表體系。"
---

"""

fm_ja = """---
title: "第 14 章：フォントの拡張：高度な組版機能"
description: "OpenType および AAT の高度な組版機能の詳細解析：AFDKO 特性構文仕様、Microsoft VOLT エンジニアリング実践、Apple Advanced Typography (AAT) 有限状態オートマトン、GSUB/GPOS ルックアップテーブル体系。"
---

"""

for path, fm in [
    ('docs/zh/fonts-encodings/chapter-14.md', fm_zh),
    ('docs/zh-hant/fonts-encodings/chapter-14.md', fm_hant),
    ('docs/ja/fonts-encodings/chapter-14.md', fm_ja)
]:
    with open(path, 'r', encoding='utf-8') as f:
        text = f.read()
    if not text.startswith('---'):
        text = fm + text
        with open(path, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f"Added frontmatter to {path}")

# 2. Fix \mathcal{B}[t^k](u_1, ...) in app_g.md and appendices.md
with open('scripts/app_builders/app_g.md', 'r', encoding='utf-8') as f:
    text_g = f.read()

fixed_g = text_g.replace(r'\mathcal{B}[t^k](u_1', r'\mathcal{B}[t^k] \, (u_1')
with open('scripts/app_builders/app_g.md', 'w', encoding='utf-8') as f:
    f.write(fixed_g)
print("Fixed app_g.md")

for p in [
    'docs/zh/fonts-encodings/appendices.md',
    'docs/zh-hant/fonts-encodings/appendices.md',
    'docs/ja/fonts-encodings/appendices.md'
]:
    with open(p, 'r', encoding='utf-8') as f:
        t = f.read()
    fixed_t = t.replace(r'\mathcal{B}[t^k](u_1', r'\mathcal{B}[t^k] \, (u_1')
    with open(p, 'w', encoding='utf-8') as f:
        f.write(fixed_t)
    print(f"Fixed {p}")

