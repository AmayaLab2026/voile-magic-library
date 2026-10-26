# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ch14_extracted_text.txt', encoding='utf-8') as f:
    text = f.read()

pages = text.split('=== PAGE ')
for p in pages[1:]:
    p_num = int(p.split('\n')[0].split()[0])
    lines = [l.strip() for l in p.split('\n')[1:30] if l.strip()]
    for l in lines:
        if any(h in l for h in ['Managing OpenType', 'Feature Definition Language', 'FontLab', 'VOLT', 'FontForge', 'Anchors', 'Noncontextual', 'Contextual', 'Managing AAT', 'Features and selectors', 'Finite Automata', 'Introduction', 'OpenType and AAT', 'GSUB', 'GPOS', 'morx', 'kerx', 'feat']):
            if len(l) < 80:
                print(f"p.{p_num}: {l}")
