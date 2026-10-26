# -*- coding: utf-8 -*-
import pymupdf, sys

doc = pymupdf.open(r"F:\杂项文件\Fonts  Encodings - From Unicode to Advanced Typography and Everything in Between (Yannis Haralambous) (z-library.sk, 1lib.sk, z-lib.sk).pdf")

for p in range(15, 30):
    text = doc[p].get_text()
    if "Homo sapiens is a species that writes" in text or "Introduction" in text:
        print(f"Physical PDF page {p+1}:")
        for line in text.splitlines()[:5]:
            print("  ", line)
