# -*- coding: utf-8 -*-
import sys, pymupdf
sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"F:\杂项文件\Fonts  Encodings - From Unicode to Advanced Typography and Everything in Between (Yannis Haralambous) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
doc = pymupdf.open(pdf_path)

# Chapter 9 is printed pages 247 to 314
# Physical pages: 247 + 21 = 268 (0-indexed 267) to 314 + 21 = 335 (0-indexed 334)
print("=== CHAPTER 9 TOC / OUTLINE IN PDF ===")
ch9_text = ""
for p in range(267, 335):
    text = doc[p].get_text()
    for l in text.splitlines():
        if l.strip().startswith(("9.", "9 ")):
            print(f"P.{p-20}: {l.strip()}")
