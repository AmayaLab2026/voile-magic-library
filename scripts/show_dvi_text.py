# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ch9_extracted_text.txt', encoding='utf-8') as f:
    text = f.read()

pages = text.split('=== PAGE ')
for p in pages[1:]:
    p_num = int(p.split('\n')[0].split()[0])
    if 259 <= p_num <= 264:
        print(f"=== PAGE {p_num} ===")
        print(p[:1500])
