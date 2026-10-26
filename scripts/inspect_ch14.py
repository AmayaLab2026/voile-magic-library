# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ch14_extracted_text.txt', encoding='utf-8') as f:
    text = f.read()

pages = text.split('=== PAGE ')
print(f"Total pages extracted: {len(pages)-1}")
total_words = 0
for p in pages[1:]:
    p_num = p.split('\n')[0].strip()
    words = len(p.split())
    total_words += words
print(f"Total words: {total_words}")
