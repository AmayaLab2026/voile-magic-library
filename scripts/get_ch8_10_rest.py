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

# Let's inspect TOC page 11 and 12
for p in [11, 12]:
    print(f"\n--- Page {p} ---")
    t = doc[p].get_text()
    for l in t.splitlines():
        print(l.encode('ascii', 'replace').decode('ascii'))
