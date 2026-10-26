# -*- coding: utf-8 -*-
import sys, re

def get_math(p):
    with open(p, encoding='utf-8') as f:
        return [m.strip() for m in re.findall(r'\$\$(.*?)\$\$', f.read(), re.DOTALL)]

print("ZH 12:")
for m in get_math('docs/zh/fonts-encodings/chapter-12.md'):
    print(" ", m[:40])

print("JA 12:")
for m in get_math('docs/ja/fonts-encodings/chapter-12.md'):
    print(" ", m[:40])

print("\nZH App:")
for m in get_math('docs/zh/fonts-encodings/appendices.md'):
    print(" ", m[:40])

print("JA App:")
for m in get_math('docs/ja/fonts-encodings/appendices.md'):
    print(" ", m[:40])
