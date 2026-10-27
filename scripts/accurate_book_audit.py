import sys
import os
import re
import pymupdf

sys.stdout.reconfigure(encoding='utf-8')

def get_pdf():
    for d in os.listdir('F:/'):
        p = os.path.join('F:/', d)
        if os.path.isdir(p):
            try:
                for f in os.listdir(p):
                    if 'Fonts' in f and f.endswith('.pdf'):
                        return os.path.join(p, f)
            except Exception:
                pass
    return None

pdf_path = get_pdf()
doc = pymupdf.open(pdf_path)

# Correct printed page ranges:
book_structure = [
    ("introduction.md", "Introduction", 1, 26),
    ("chapter-1.md", "Chapter 1: Before Unicode", 27, 52),
    ("chapter-2.md", "Chapter 2: Characters, Glyphs, and Bytes", 53, 94),
    ("chapter-3.md", "Chapter 3: Unicode Character Properties", 95, 124),
    ("chapter-4.md", "Chapter 4: Combining Characters, Normalization & Complex Scripts", 125, 158),
    ("chapter-5.md", "Chapter 5: Using Unicode", 159, 178),
    ("chapter-6.md", "Chapter 6: Character Sets and Fonts on the Mac", 179, 204),
    ("chapter-7.md", "Chapter 7: Font Management under Windows", 205, 220),
    ("chapter-8.md", "Chapter 8: Font Management under X Window", 221, 235),
    ("chapter-9.md", "Chapter 9: Fonts and Encodings in TeX", 236, 314),
    ("chapter-10.md", "Chapter 10: Fonts and Web Pages", 315, 366),
    ("chapter-11.md", "Chapter 11: Font Classification", 367, 440),
    ("chapter-12.md", "Chapter 12: Creating and Modifying Fonts", 441, 504),
    ("chapter-13.md", "Chapter 13: Optimizing a rasterization (Hinting)", 505, 548),
    ("chapter-14.md", "Chapter 14: Enriching Fonts: Advanced Typography", 549, 598),
    ("appendices.md", "Appendices A-G", 599, 976),
]

print(f"{'File':<18} | {'Chapter Name':<38} | {'Printed':<9} | {'PDF Words':<10} | {'ZH Chars':<9} | {'Ratio':<6}")
print("-" * 105)

total_pdf_words = 0
total_zh_chars = 0

for fname, title, p_start, p_end in book_structure:
    md_path = os.path.join('docs/zh/fonts-encodings', fname)
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()
    
    zh_chars = len(md_text)
    
    # PDF text
    pdf_text = ""
    # Physical PDF page offset is printed page + 20
    for p in range(p_start + 20, p_end + 21):
        if p < len(doc):
            pdf_text += doc[p].get_text() + "\n"
            
    pdf_words = len(re.findall(r'\b[a-zA-Z0-9_\-\']+\b', pdf_text))
    ratio = zh_chars / max(1, pdf_words)
    
    total_pdf_words += pdf_words
    total_zh_chars += zh_chars
    
    print(f"{fname:<18} | {title:<38} | {p_start:3d}-{p_end:<4d} | {pdf_words:<10,d} | {zh_chars:<9,d} | {ratio:<6.2f}")

print("-" * 105)
print(f"{'TOTAL':<18} | {'All 16 Sections':<38} | 1-976     | {total_pdf_words:<10,d} | {total_zh_chars:<9,d} | {total_zh_chars/total_pdf_words:<6.2f}")
