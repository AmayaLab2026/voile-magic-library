with open('scripts/ch8_pdf_dump.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re
# Find headings or sections
print(f"Total characters in PDF dump: {len(text)}")
lines = text.splitlines()
for i, l in enumerate(lines):
    if l.startswith('=== PDF PAGE') or (len(l) > 3 and l == l.title() and len(l) < 50):
        print(f"L{i}: {l}")
