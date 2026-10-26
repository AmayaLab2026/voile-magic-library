with open('scripts/ch4_pdf_dump.txt', 'r', encoding='utf-8') as f:
    text = f.read()

pages = text.split('=== PDF PAGE ')
print(f"Total pages in Ch 4: {len(pages)-1}")
for p in pages[1:]:
    p_header = p.split('\n')[0]
    lines = [l.strip() for l in p.split('\n')[1:] if l.strip()]
    print(f"\n--- Page {p_header} ({len(lines)} lines) ---")
    for l in lines[:6]:
        print(" ", l.encode('ascii', 'replace').decode('ascii'))
