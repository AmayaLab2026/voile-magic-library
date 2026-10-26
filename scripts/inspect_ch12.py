# -*- coding: utf-8 -*-
import fitz, sys
sys.stdout.reconfigure(encoding='utf-8')

doc = fitz.open(r'F:\杂项文件\Fonts  Encodings - From Unicode to Advanced Typography and Everything in Between (Yannis Haralambous) (z-library.sk, 1lib.sk, z-lib.sk).pdf')

print("Extracting Chapter 12 TOC & headings...")
for p in range(445+20, 508+20):
    page = doc[p]
    blocks = page.get_text('blocks')
    for b in blocks:
        txt = b[4].strip()
        lines = txt.split('\n')
        if len(lines) <= 2 and len(txt) < 80:
            if any(k in txt for k in ['FontLab', 'FontForge', 'Bézier', 'B-spline', 'Spiro', 'Kerning', 'Anchor', 'Python', 'TrueType', 'PostScript', 'Hinting', 'Creating', 'Editing', 'Drawing', 'Contour']):
                print(f"p.{p-20}: {txt}")
