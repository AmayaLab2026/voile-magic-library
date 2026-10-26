# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('appendices_real_text.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i in range(16000, 19500):
    line = lines[i].strip()
    if 'Table F.' in line or 'F.2' in line or 'F.3' in line or 'F.4' in line or 'cmbase' in line:
        print(f"Line {i}: {line}")
