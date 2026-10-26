# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ch14_extracted_text.txt', encoding='utf-8') as f:
    text = f.read()

pages = text.split('=== PAGE ')

for i in range(37, len(pages)):
    p = pages[i]
    p_num = p.split('\n')[0].strip()
    print(f"=== {p_num} (words: {len(p.split())}) ===")
    lines = [l.strip() for l in p.split('\n')[1:] if l.strip()]
    for l in lines[:6]:
        print("  ", l[:100])
