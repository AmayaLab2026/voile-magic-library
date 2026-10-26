# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('appendices_real_text.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(8000, 14000):
    line = lines[i].strip()
    if line.startswith('D.5.') or line.startswith('D.6.') or '<Lookup' in line or '<Feature' in line or 'morph' in line.lower() or 'state table' in line.lower():
        print(f"Line {i}: {line}")
