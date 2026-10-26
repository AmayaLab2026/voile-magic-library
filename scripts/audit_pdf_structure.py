# -*- coding: utf-8 -*-
import sys, re, os, pymupdf
sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"F:\杂项文件\Fonts  Encodings - From Unicode to Advanced Typography and Everything in Between (Yannis Haralambous) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
doc = pymupdf.open(pdf_path)

print(f"Total pages in PDF: {len(doc)}")

# Read the TOC from PDF pages 7 to 22
toc_text = ""
for p in range(6, 23):
    toc_text += f"\n--- TOC PAGE {p+1} ---\n" + doc[p].get_text()

with open("scripts/full_pdf_toc_extracted.txt", "w", encoding="utf-8") as f:
    f.write(toc_text)

print("TOC saved to scripts/full_pdf_toc_extracted.txt")
