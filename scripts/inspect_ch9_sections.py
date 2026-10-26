# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ch9_extracted_text.txt', encoding='utf-8') as f:
    text = f.read()

pages = text.split('=== PAGE ')
for p in pages[1:]:
    p_num = p.split('\n')[0].strip()
    lines = [l.strip() for l in p.split('\n')[1:25] if l.strip()]
    for l in lines:
        if l in ['Using Fonts in TEX', 'Installing Fonts for TEX', 'Customizing TEX Fonts for the User’s Needs', 'Conclusions and Glimpses at the Future']:
            print(f'Page {p_num}: *** {l} ***')
        elif any(l.startswith(h) for h in ['Introduction to TEX', 'The High Level', 'The Low Level', '“Après-TEX”', 'The Tool afm2tfm', 'Basic Use of the Tool fontinst', 'Multiple Master fonts', 'How to Conﬁgure', 'How to Configure', 'ETX and MTX', 'Contextual analysis in Arabic', 'Conclusion']):
            print(f'Page {p_num}:   -> {l}')
