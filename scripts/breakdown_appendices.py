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

doc = pymupdf.open(get_pdf())

# The 7 Appendices
app_specs = [
    ("Appendix A: Bitmap Font Formats", 599, 622, r"# 附录 A|# Appendix A"),
    ("Appendix B: The Characters of a Font", 623, 634, r"# 附录 B|# Appendix B"),
    ("Appendix C: PostScript Font Formats", 635, 702, r"# 附录 C|# Appendix C"),
    ("Appendix D: TrueType & OpenType Formats", 703, 878, r"# 附录 D|# Appendix D"),
    ("Appendix E: TrueType Instructions", 879, 904, r"# 附录 E|# Appendix E"),
    ("Appendix F: METAFONT and Its Derivatives", 905, 960, r"# 附录 F|# Appendix F"),
    ("Appendix G: Bézier Curves", 961, 976, r"# 附录 G|# Appendix G"),
]

with open('docs/zh/fonts-encodings/appendices.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Split appendices by top headers
# Find occurrences of # 附录 X
matches = list(re.finditer(r'^#\s+附录\s+([A-G])', text, re.M))

app_texts = {}
for i, m in enumerate(matches):
    letter = m.group(1)
    start = m.start()
    end = matches[i+1].start() if i + 1 < len(matches) else len(text)
    app_texts[letter] = text[start:end]

print(f"{'Appendix':<40} | {'Pages':<9} | {'PDF Words':<10} | {'ZH Chars':<9} | {'Ratio':<6}")
print("-" * 85)

for name, p_start, p_end, pat in app_specs:
    letter = name.split()[1][0]
    md_sub = app_texts.get(letter, "")
    zh_chars = len(md_sub)
    
    # PDF words
    pdf_text = ""
    for p in range(p_start + 20, p_end + 21):
        if p < len(doc):
            pdf_text += doc[p].get_text() + "\n"
    pdf_words = len(re.findall(r'\b[a-zA-Z0-9_\-\']+\b', pdf_text))
    ratio = zh_chars / max(1, pdf_words)
    print(f"{name:<40} | {p_start:3d}-{p_end:<4d} | {pdf_words:<10,d} | {zh_chars:<9,d} | {ratio:<6.2f}")
