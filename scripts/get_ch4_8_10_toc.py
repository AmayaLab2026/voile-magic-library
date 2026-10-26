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

# Let's extract TOC from pages 9 to 16
for p in range(9, 15):
    t = doc[p].get_text()
    for line in t.splitlines():
        # filter for Chapter 4, 8, 10
        if any(f" {c} " in f" {line} " or f"Chapter {c}" in line for c in [4, 8, 10]):
            print(f"P.{p}: {line.encode('ascii', 'replace').decode('ascii')}")

print("\n--- Detailed TOC lines for Ch 4, 8, 10 ---")
in_target = False
target_num = None
for p in range(9, 15):
    t = doc[p].get_text()
    for line in t.splitlines():
        line_clean = line.strip()
        if line_clean in ["4", "8", "10"]:
            target_num = line_clean
            in_target = True
            print(f"\n=== CHAPTER {line_clean} ===")
            continue
        if line_clean in ["5", "9", "11", "Appendices"]:
            in_target = False
        if in_target:
            print("  ", line_clean.encode('ascii', 'replace').decode('ascii'))
