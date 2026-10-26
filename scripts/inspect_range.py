# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ch14_extracted_text.txt', encoding='utf-8') as f:
    text = f.read()

pages = text.split('=== PAGE ')

def summarize_range(start_idx, end_idx):
    for i in range(start_idx, end_idx):
        p = pages[i]
        p_num = p.split('\n')[0].strip()
        print(f"=== {p_num} (words: {len(p.split())}) ===")
        # print first few non-empty lines
        lines = [l.strip() for l in p.split('\n')[1:] if l.strip()]
        for l in lines[:8]:
            print("  ", l[:100])

print("Range 557-568:")
summarize_range(9, 21)
