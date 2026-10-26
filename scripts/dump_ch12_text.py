# -*- coding: utf-8 -*-
import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open(r'F:\杂项文件\Fonts  Encodings - From Unicode to Advanced Typography and Everything in Between (Yannis Haralambous) (z-library.sk, 1lib.sk, z-lib.sk).pdf')

with open('ch12_extracted_text.txt', 'w', encoding='utf-8') as out:
    for p in range(445+20, 509+20):
        out.write(f'=== PAGE {p-20} (phys {p}) ===\n')
        out.write(doc[p].get_text('text'))
        out.write('\n\n')

print('Saved ch12_extracted_text.txt')
