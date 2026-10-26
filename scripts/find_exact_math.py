# -*- coding: utf-8 -*-
import sys, re
sys.stdout.reconfigure(encoding='utf-8')

def get_math(p):
    with open(p, encoding='utf-8') as f:
        return re.findall(r'\$\$(.*?)\$\$', f.read(), re.DOTALL)

zh_12 = get_math('docs/zh/fonts-encodings/chapter-12.md')
ja_12 = get_math('docs/ja/fonts-encodings/chapter-12.md')
print('CH12 ZH:', len(zh_12), 'JA:', len(ja_12))
for i, z in enumerate(zh_12):
    has = any(z.strip() == j.strip() for j in ja_12)
    print(f"  ZH12 [{i+1}] {z.strip()[:40]}... (in JA: {has})")

zh_app = get_math('docs/zh/fonts-encodings/appendices.md')
ja_app = get_math('docs/ja/fonts-encodings/appendices.md')
print('APP ZH:', len(zh_app), 'JA:', len(ja_app))
for i, z in enumerate(zh_app):
    has = any(z.strip() == j.strip() for j in ja_app)
    print(f"  ZH_APP [{i+1}] {z.strip()[:40]}... (in JA: {has})")
