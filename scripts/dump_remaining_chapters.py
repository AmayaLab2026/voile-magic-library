import fitz, os, sys
sys.stdout.reconfigure(encoding='utf-8')

pdf_path = None
for root, dirs, files in os.walk('F:/'):
    for f in files:
        if f.endswith('.pdf') and 'Fonts' in f:
            pdf_path = os.path.join(root, f)
            break
    if pdf_path:
        break

print(f"Found PDF at: {pdf_path}")
doc = fitz.open(pdf_path)

# Chapter ranges from previous physical page offsets:
# Ch 8: 243 to 256 (0-indexed: 242 to 255)
# Ch 10: 337 to 388 (0-indexed: 336 to 387)
# Ch 11: 389 to 462 (0-indexed: 388 to 461)
# Ch 12: 463 to 526 (0-indexed: 462 to 525)
# Ch 13: 527 to 570 (0-indexed: 526 to 569)
# Appendices: 621 to 960 (0-indexed: 620 to 959)

def dump_range(start_idx, end_idx, out_name):
    print(f"Dumping {out_name}: pages {start_idx+1} to {end_idx+1}...")
    with open(out_name, 'w', encoding='utf-8') as out:
        for idx in range(start_idx, end_idx + 1):
            out.write(f"\n=== PHYS PAGE {idx+1} ===\n")
            out.write(doc[idx].get_text())
    print(f"Done {out_name}.")

dump_range(242, 255, "ch8_real_text.txt")
dump_range(336, 387, "ch10_real_text.txt")
dump_range(388, 461, "ch11_real_text.txt")
dump_range(462, 525, "ch12_real_text.txt")
dump_range(526, 569, "ch13_real_text.txt")
