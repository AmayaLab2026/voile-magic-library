# -*- coding: utf-8 -*-
with open('docs/zh/fonts-encodings/appendices.md', 'r', encoding='utf-8') as f:
    text = f.read()

import re
maths = re.findall(r'\$\$(.*?)\$\$', text, re.DOTALL)
for i, m in enumerate(maths):
    if '\t' in m:
        print(f"Math block {i+1} has tab character!")
