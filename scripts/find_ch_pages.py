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

print(f"PDF path: {pdf_path}")
doc = pymupdf.open(pdf_path)

# Let's inspect TOC or search chapter titles
for i in range(10, 30):
    t = doc[i].get_text()
    if 'Contents' in t or 'Chapter 4' in t or 'Chapter 8' in t or 'Chapter 10' in t:
        print(f"Page {i}:")
        for line in t.splitlines()[:20]:
            print("  ", line)
