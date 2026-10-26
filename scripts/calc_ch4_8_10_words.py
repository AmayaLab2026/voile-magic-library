import os, pymupdf

pdf_path = None
if os.path.exists('F:/'):
    for d in os.listdir('F:/'):
        p = os.path.join('F:/', d)
        if os.path.isdir(p):
            try:
                for f in os.listdir(p):
                    if 'Fonts' in f and f.endswith('.pdf'):
                        pdf_path = os.path.join(p, f)
                        break
            except:
                pass

doc = pymupdf.open(pdf_path)

def analyze_range(name, start_p, end_p):
    # offset: printed page 1 is physical page 21 (0-based)
    text = ""
    for p in range(start_p + 20, end_p + 21):
        text += doc[p].get_text() + "\n"
    words = len(text.split())
    print(f"{name}: pages {start_p}-{end_p} (phys {start_p+20}-{end_p+20}), words = {words:,}")
    return text, words

t4, w4 = analyze_range("Chapter 4", 127, 158)
t8, w8 = analyze_range("Chapter 8", 221, 234)
t10, w10 = analyze_range("Chapter 10", 315, 366)

print(f"Targets at ratio >= 1.15:")
print(f"Chapter 4:  words = {w4:,} -> target zh chars >= {int(w4 * 1.15):,}")
print(f"Chapter 8:  words = {w8:,} -> target zh chars >= {int(w8 * 1.15):,}")
print(f"Chapter 10: words = {w10:,} -> target zh chars >= {int(w10 * 1.15):,}")
