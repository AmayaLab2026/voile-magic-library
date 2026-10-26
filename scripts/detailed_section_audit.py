# -*- coding: utf-8 -*-
import sys, re, os
sys.stdout.reconfigure(encoding='utf-8')

pdf_toc = open("scripts/full_pdf_toc_extracted.txt", encoding="utf-8").read()

# Let's write a script that analyzes each markdown file's sections
docs_dir = "docs/zh/fonts-encodings"
files = [
    "introduction.md",
    "chapter-1.md",
    "chapter-2.md",
    "chapter-3.md",
    "chapter-4.md",
    "chapter-5.md",
    "chapter-6.md",
    "chapter-7.md",
    "chapter-8.md",
    "chapter-9.md",
    "chapter-10.md",
    "chapter-11.md",
    "chapter-12.md",
    "chapter-13.md",
    "chapter-14.md",
    "appendices.md"
]

print("SECTION AUDIT OF DOCS/ZH/FONTS-ENCODINGS:")
for f in files:
    path = os.path.join(docs_dir, f)
    text = open(path, encoding='utf-8').read()
    h2 = [l.strip() for l in text.splitlines() if l.startswith('## ')]
    h3 = [l.strip() for l in text.splitlines() if l.startswith('### ')]
    print(f"\n[{f}] (H2: {len(h2)}, H3: {len(h3)})")
    for h in h2[:6]:
        print(f"   {h}")
    if len(h2) > 6:
        print(f"   ... and {len(h2)-6} more H2 headings")
