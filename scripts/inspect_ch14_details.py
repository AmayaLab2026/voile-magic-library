# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ch14_extracted_text.txt', encoding='utf-8') as f:
    text = f.read()

pages = text.split('=== PAGE ')
for p in pages[1:]:
    p_num = int(p.split('\n')[0].split()[0])
    if p_num in [558, 559, 560, 561, 562, 570, 571, 580, 581, 590, 591, 592]:
        print(f"=== PAGE {p_num} ===")
        print(p[:1000])
