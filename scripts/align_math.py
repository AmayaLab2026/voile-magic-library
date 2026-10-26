# -*- coding: utf-8 -*-
"""
Inspect and align math formulas across zh, zh-hant, ja for chapter-9, chapter-12, chapter-14, appendices.
"""
import sys, re

def get_display_math(path):
    with open(path, encoding='utf-8') as f:
        text = f.read()
    return re.findall(r'\$\$(.*?)\$\$', text, re.DOTALL)

for f in ['chapter-9.md', 'chapter-12.md', 'chapter-14.md', 'appendices.md']:
    zh_m = get_display_math(f'docs/zh/fonts-encodings/{f}')
    hant_m = get_display_math(f'docs/zh-hant/fonts-encodings/{f}')
    ja_m = get_display_math(f'docs/ja/fonts-encodings/{f}')
    print(f"=== {f} ===")
    print(f"ZH: {len(zh_m)}, HANT: {len(hant_m)}, JA: {len(ja_m)}")
    for i, m in enumerate(zh_m):
        m_str = m.strip().replace('\n', ' ')
        hant_has = any(m.strip() in h for h in hant_m) if hant_m else False
        ja_has = any(m.strip() in j for j in ja_m) if ja_m else False
        print(f"  [{i+1}] {m_str[:50]}... | Hant: {hant_has} | JA: {ja_has}")
