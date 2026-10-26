# -*- coding: utf-8 -*-
import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')

toc_lines = open("scripts/full_pdf_toc_extracted.txt", encoding="utf-8").readlines()

# Let's extract chapters and page ranges from TOC
chapters_pdf = []
current_ch = None

for line in toc_lines:
    line_s = line.strip()
    # match chapter start like "1\nExplorations" or "10 Fonts and Web Pages" or "Part I" or "Appendix A"
    # In O'Reilly TOC format:
    # "1" followed on next line or same line by title
    # or "Appendix A ..."
    pass

# Let's inspect the first 100 lines of TOC to see pattern
for i in range(120):
    print(f"{i+1:3d}: {toc_lines[i].strip()}")
