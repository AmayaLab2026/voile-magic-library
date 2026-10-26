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

with open('scripts/ch10_pdf_dump.txt', 'w', encoding='utf-8') as out:
    for p in range(315 + 20, 366 + 21):
        out.write(f"\n\n=== PDF PAGE {p} (Printed {p-20}) ===\n\n")
        out.write(doc[p].get_text())

print("Dumped Chapter 10 PDF text to scripts/ch10_pdf_dump.txt")
