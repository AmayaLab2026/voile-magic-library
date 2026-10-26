# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ch9_extracted_text.txt', encoding='utf-8') as f:
    text = f.read()

pages = text.split('=== PAGE ')
for p in pages[1:]:
    p_num = p.split('\n')[0].strip()
    p_int = int(p_num.split()[0])
    if 280 <= p_int <= 314:
        lines = [l.strip() for l in p.split('\n') if l.strip()]
        for i, l in enumerate(lines):
            # Find short lines that look like headings
            if len(l) < 60 and not l.isdigit() and not l.startswith('Chapter 9') and not l.startswith('Customizing') and not l.startswith('Installing') and not l.startswith('Conclusions'):
                if any(k in l for k in ['fontinst', 'ETX', 'MTX', 'Figure', 'virtual', 'Virtual', 'Arabic', 'Greek', 'Omega', 'OTP', 'OFM', 'OVF', 'Horn', 'horn', 'Contextual', 'ligature', 'kern', 'Mathematical']):
                    print(f'p.{p_int}: {l}')
