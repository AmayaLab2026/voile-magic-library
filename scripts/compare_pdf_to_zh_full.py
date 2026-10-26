# -*- coding: utf-8 -*-
import sys, re, os, pymupdf
sys.stdout.reconfigure(encoding='utf-8')

pdf_path = r"F:\杂项文件\Fonts  Encodings - From Unicode to Advanced Typography and Everything in Between (Yannis Haralambous) (z-library.sk, 1lib.sk, z-lib.sk).pdf"
doc = pymupdf.open(pdf_path)

ch_pages = [
    ("Introduction", 1, 26, "introduction.md"),
    ("Chapter 1: Before Unicode", 27, 52, "chapter-1.md"),
    ("Chapter 2: Characters, Glyphs, Bytes", 53, 94, "chapter-2.md"),
    ("Chapter 3: Properties of Unicode", 95, 124, "chapter-3.md"),
    ("Chapter 4: Non-Latin Scripts", 125, 158, "chapter-4.md"),
    ("Chapter 5: Using Unicode", 159, 178, "chapter-5.md"),
    ("Chapter 6: Mac Font Management", 179, 204, "chapter-6.md"),
    ("Chapter 7: Windows Font Management", 205, 220, "chapter-7.md"),
    ("Chapter 8: X Window Font Management", 221, 246, "chapter-8.md"),
    ("Chapter 9: TeX and Omega Fonts", 247, 314, "chapter-9.md"),
    ("Chapter 10: Fonts and Web Pages", 315, 366, "chapter-10.md"),
    ("Chapter 11: History & Classification", 367, 444, "chapter-11.md"),
    ("Chapter 12: Editing & Creating Fonts", 445, 508, "chapter-12.md"),
    ("Chapter 13: Optimizing Rasterization", 509, 576, "chapter-13.md"),
    ("Chapter 14: Enriching Fonts: AAT/OTF", 577, 650, "chapter-14.md"),
    ("Appendices A-G", 651, 990, "appendices.md"),
]

docs_dir = "docs/zh/fonts-encodings"

results = []

for title, p_start, p_end, md_name in ch_pages:
    # Physical page indices in PyMuPDF are 0-based
    # Printed page 1 is physical page 22 (index 21)
    phys_start = p_start + 20
    phys_end = p_end + 20
    
    pdf_text = ""
    for p in range(phys_start, min(phys_end + 1, len(doc))):
        pdf_text += doc[p].get_text() + "\n"
    
    pdf_words = len(pdf_text.split())
    
    # Read Markdown
    md_path = os.path.join(docs_dir, md_name)
    if os.path.exists(md_path):
        md_text = open(md_path, encoding='utf-8').read()
        zh_chars = len(md_text)
        zh_lines = len(md_text.splitlines())
        zh_headers = len([l for l in md_text.splitlines() if l.startswith('#')])
    else:
        zh_chars = 0
        zh_lines = 0
        zh_headers = 0
    
    ratio = zh_chars / pdf_words if pdf_words > 0 else 0
    results.append({
        "title": title,
        "pages": f"pp. {p_start}–{p_end} ({p_end - p_start + 1}p)",
        "pdf_words": pdf_words,
        "zh_chars": zh_chars,
        "zh_lines": zh_lines,
        "zh_headers": zh_headers,
        "ratio": ratio,
        "md_name": md_name
    })

print("=" * 105)
print(f"{'Chapter':34s} | {'Pages in PDF':16s} | {'PDF Words':10s} | {'ZH Chars':10s} | {'Lines':6s} | {'Headers':7s} | {'Chars/Word':10s}")
print("=" * 105)

for r in results:
    print(f"{r['title']:34s} | {r['pages']:16s} | {r['pdf_words']:10d} | {r['zh_chars']:10d} | {r['zh_lines']:6d} | {r['zh_headers']:7d} | {r['ratio']:10.2f}")

print("=" * 105)
