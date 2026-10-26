# -*- coding: utf-8 -*-
import sys, re
sys.stdout.reconfigure(encoding='utf-8')

for name in ['chapter-9.md', 'chapter-12.md', 'chapter-14.md', 'appendices.md']:
    with open(f'docs/zh/fonts-encodings/{name}', encoding='utf-8') as f:
        text = f.read()
    matches = re.findall(r'\$\$(.*?)\$\$', text, re.DOTALL)
    print(f"{name}: {len(matches)} display math formulas in ZH")
    for idx, m in enumerate(matches):
        print(f"  [{idx+1}] {m.strip()[:60]}")
