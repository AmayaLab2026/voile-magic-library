# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

zh_ch9 = open('docs/zh/fonts-encodings/chapter-9.md', encoding='utf-8').read()
print(f"Current zh chapter-9 length: {len(zh_ch9)} chars, lines: {len(zh_ch9.splitlines())}")
for l in zh_ch9.splitlines()[:40]:
    print(l)
