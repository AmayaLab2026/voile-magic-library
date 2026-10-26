# -*- coding: utf-8 -*-
import sys, re, os, pymupdf
sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"F:\杂项文件\Fonts  Encodings - From Unicode to Advanced Typography and Everything in Between (Yannis Haralambous) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
doc = pymupdf.open(pdf_path)

ch_pages = [
    ("introduction", 1, 26, "introduction.md"),
    ("chapter-1", 27, 52, "chapter-1.md"),
    ("chapter-2", 53, 94, "chapter-2.md"),
    ("chapter-3", 95, 124, "chapter-3.md"),
    ("chapter-4", 125, 158, "chapter-4.md"),
    ("chapter-5", 159, 178, "chapter-5.md"),
    ("chapter-6", 179, 204, "chapter-6.md"),
    ("chapter-7", 205, 220, "chapter-7.md"),
    ("chapter-8", 221, 246, "chapter-8.md"),
    ("chapter-9", 247, 314, "chapter-9.md"),
    ("chapter-10", 315, 366, "chapter-10.md"),
    ("chapter-11", 367, 444, "chapter-11.md"),
    ("chapter-12", 445, 508, "chapter-12.md"),
    ("chapter-13", 509, 576, "chapter-13.md"),
    ("chapter-14", 577, 650, "chapter-14.md"),
    ("appendices", 651, 990, "appendices.md"),
]

docs_dir = "docs/zh/fonts-encodings"

print(f"{'Chapter':15s} | {'PDF Pages':12s} | {'PDF Words':10s} | {'ZH Chars':10s} | {'ZH Lines':8s} | {'ZH Sections':12s}")
print("-" * 80)

for name, p_start, p_end, md_name in ch_pages:
    # count words in PDF range
    # Note: PDF page offset: check where page 1 of body is
    # In O'Reilly book, Arabic page 1 is around physical PDF page 23
    # Let's find exact page offset
    pass
