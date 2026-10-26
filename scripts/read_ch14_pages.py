# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ch14_extracted_text.txt', encoding='utf-8') as f:
    text = f.read()

pages = text.split('=== PAGE ')

# Check pages 549 to 556:
print("Pages 549-556:")
for p in pages[1:9]:
    p_num = p.split('\n')[0].strip()
    print(f"--- Page {p_num} ---")
    for l in p.split('\n')[1:10]:
        if l.strip():
            print("  ", l.strip())
