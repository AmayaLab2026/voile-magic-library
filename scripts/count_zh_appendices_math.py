# -*- coding: utf-8 -*-
import re

with open('docs/zh/fonts-encodings/appendices.md', 'r', encoding='utf-8') as f:
    text = f.read()

maths = re.findall(r'\$\$(.*?)\$\$', text, re.DOTALL)
print(f"ZH Appendices math blocks count: {len(maths)}")
for i, m in enumerate(maths):
    print(f"[{i+1}] {m.strip()[:60]}...")
