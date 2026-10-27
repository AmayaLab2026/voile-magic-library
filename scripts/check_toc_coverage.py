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

pdf_path = get_pdf()
doc = pymupdf.open(pdf_path)

# Load TOC extracted
with open('scripts/full_toc_extracted.txt', 'r', encoding='utf-8') as f:
    raw = f.read()

lines = [l.strip() for l in raw.split('\n') if l.strip()]
cleaned = [l for l in lines if l != '=== PAGE ===' and l != 'Contents' and not re.match(r'^[ivxLCDM]+$', l, re.I)]

entries = []
cur_title = []
for item in cleaned:
    if re.match(r'^\d+$', item) and int(item) <= 1039:
        title = ' '.join(cur_title)
        title = re.sub(r'[\.\s]{2,}', ' ', title).strip()
        entries.append((title, int(item)))
        cur_title = []
        continue
    m = re.search(r'[\.\s]+(\d+)$', item)
    if m and int(m.group(1)) <= 1039:
        page = int(m.group(1))
        item_text = item[:m.start()].strip()
        if item_text: cur_title.append(item_text)
        title = ' '.join(cur_title)
        title = re.sub(r'[\.\s]{2,}', ' ', title).strip()
        entries.append((title, page))
        cur_title = []
        continue
    if set(item) <= {'.', ' '}:
        continue
    cur_title.append(item)

# Map page boundaries to chapters
ch_boundaries = [
    ('introduction.md', 'Introduction', 1, 26),
    ('chapter-1.md', 'Chapter 1', 27, 52),
    ('chapter-2.md', 'Chapter 2', 53, 94),
    ('chapter-3.md', 'Chapter 3', 95, 124),
    ('chapter-4.md', 'Chapter 4', 125, 158),
    ('chapter-5.md', 'Chapter 5', 159, 178),
    ('chapter-6.md', 'Chapter 6', 179, 204),
    ('chapter-7.md', 'Chapter 7', 205, 220),
    ('chapter-8.md', 'Chapter 8', 221, 246),
    ('chapter-9.md', 'Chapter 9', 247, 314),
    ('chapter-10.md', 'Chapter 10', 315, 366),
    ('chapter-11.md', 'Chapter 11', 367, 444),
    ('chapter-12.md', 'Chapter 12', 445, 508),
    ('chapter-13.md', 'Chapter 13', 509, 576),
    ('chapter-14.md', 'Chapter 14', 577, 650),
    ('appendices.md', 'Appendices A-G', 651, 990),
]

print("=== CHECKING SECTION COVERAGE AGAINST PDF TOC ===")
for fname, ch_name, p_start, p_end in ch_boundaries:
    # Filter TOC entries in this page range
    ch_toc = [e for e in entries if p_start <= e[1] <= p_end and e[0]]
    
    md_path = os.path.join('docs/zh/fonts-encodings', fname)
    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read().lower()
    
    missing_toc = []
    for title, page in ch_toc:
        # Normalize title
        # Check if key words of title appear in md_text
        words = [w for w in re.findall(r'[a-zA-Z0-9]+', title) if len(w) > 2 and w.lower() not in {'and', 'the', 'for', 'with', 'from', 'under', 'into'}]
        if not words:
            continue
        # If none of the words appear in md_text
        matched_words = [w for w in words if w.lower() in md_text]
        if len(matched_words) < max(1, len(words) // 2):
            missing_toc.append((title, page, words, matched_words))
            
    print(f"\n[{ch_name}] ({fname}) - {len(ch_toc)} TOC sections, {len(missing_toc)} potential misses:")
    for t, p, w, mw in missing_toc:
        print(f"   p. {p:3d}: '{t}' (key: {w} -> found: {mw})")
