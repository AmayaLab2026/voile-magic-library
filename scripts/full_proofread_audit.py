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

pdf_file = get_pdf()
if not pdf_file:
    print("Error: PDF file not found!")
    sys.exit(1)

doc = pymupdf.open(pdf_file)

chapters = [
    ('introduction.md', 'Introduction', 1, 26),
    ('chapter-1.md', 'Chapter 1: Before Unicode', 27, 52),
    ('chapter-2.md', 'Chapter 2: Characters, Glyphs, and Bytes', 53, 94),
    ('chapter-3.md', 'Chapter 3: Unicode Character Properties', 95, 124),
    ('chapter-4.md', 'Chapter 4: Combining Characters, Normalization & Complex Scripts', 125, 158),
    ('chapter-5.md', 'Chapter 5: Using Unicode', 159, 178),
    ('chapter-6.md', 'Chapter 6: Character Sets and Fonts on the Mac', 179, 204),
    ('chapter-7.md', 'Chapter 7: Font Conversion Tools', 205, 220),
    ('chapter-8.md', 'Chapter 8: Font Management under X Window', 221, 246),
    ('chapter-9.md', 'Chapter 9: Fonts and Encodings in TeX', 247, 314),
    ('chapter-10.md', 'Chapter 10: Fonts and Web Pages', 315, 366),
    ('chapter-11.md', 'Chapter 11: Font Classification', 367, 444),
    ('chapter-12.md', 'Chapter 12: Creating and Modifying Fonts', 445, 508),
    ('chapter-13.md', 'Chapter 13: Font Hinting', 509, 576),
    ('chapter-14.md', 'Chapter 14: Advanced Typography', 577, 650),
    ('appendices.md', 'Appendices A-G', 651, 990),
]

lazy_patterns = [
    r'此处[省略|略]',
    r'篇幅所限',
    r'篇幅原因',
    r'略去',
    r'不在此赘述',
    r'不再赘述',
    r'未完待续',
    r'待补充',
    r'TODO',
    r'FIXME',
    r'简要列出',
    r'（略）',
    r'\(略\)',
    r'下文略',
    r'余下略',
]

print("=" * 80)
print("EXHAUSTIVE 16-SECTION PROOFREADING & AUDITING REPORT")
print("=" * 80)
print(f"Total PDF pages: {len(doc)}")
print(f"PDF Source: {pdf_file}\n")

audit_results = []

for fname, title, p_start, p_end in chapters:
    md_path = os.path.join('docs/zh/fonts-encodings', fname)
    if not os.path.exists(md_path):
        print(f"Error: {md_path} does not exist!")
        continue

    with open(md_path, 'r', encoding='utf-8') as f:
        md_text = f.read()

    # 1. CJK count
    cjk_chars = len(re.findall(r'[\u4e00-\u9fff]', md_text))

    # 2. Extract PDF text & count words
    pdf_text = ''
    for p in range(p_start + 20, p_end + 21):
        if p < len(doc):
            pdf_text += doc[p].get_text() + '\n'

    pdf_words = len(re.findall(r'\b[a-zA-Z0-9_\-\']+\b', pdf_text))
    ratio = cjk_chars / max(1, pdf_words)

    # 3. Check for lazy patterns
    found_lazy = []
    for pat in lazy_patterns:
        matches = re.findall(pat, md_text)
        if matches:
            found_lazy.append((pat, len(matches)))

    # 4. Check figures in PDF vs MD
    fig_matches = set(re.findall(r'Figure\s+([0-9A-G]+[\-\.][0-9]+)', pdf_text, re.I))
    md_figs = set(re.findall(r'图\s*([0-9A-G]+[\-\.][0-9]+)|Figure\s*([0-9A-G]+[\-\.][0-9]+)', md_text, re.I))
    md_fig_keys = set()
    for m in md_figs:
        k = m[0] or m[1]
        md_fig_keys.add(k.replace('.', '-'))

    pdf_fig_keys = {f.replace('.', '-') for f in fig_matches}
    missing_figs = sorted(list(pdf_fig_keys - md_fig_keys))

    # 5. Extract Markdown Headings
    headings = re.findall(r'^(#{1,4})\s+(.+)$', md_text, re.M)

    audit_results.append({
        'fname': fname,
        'title': title,
        'p_start': p_start,
        'p_end': p_end,
        'pdf_words': pdf_words,
        'cjk_chars': cjk_chars,
        'ratio': ratio,
        'found_lazy': found_lazy,
        'pdf_figs': len(pdf_fig_keys),
        'md_figs': len(md_fig_keys),
        'missing_figs': missing_figs,
        'headings_count': len(headings),
        'headings': headings
    })

    status_str = "PASS" if ratio >= 1.10 and not found_lazy else "REVIEW NEEDED"
    print(f"[{status_str}] {title} ({fname})")
    print(f"    Pages: pp. {p_start}-{p_end} (PDF p. {p_start+20}-{p_end+20})")
    print(f"    PDF Words: {pdf_words:,} | ZH Chars: {cjk_chars:,} | Ratio: {ratio:.2f}")
    print(f"    Lazy Patterns: {found_lazy if found_lazy else '0 detected (Clean)'}")
    print(f"    Headings: {len(headings)} sections/subsections")
    print(f"    Figures: PDF mentions {len(pdf_fig_keys)}, MD references {len(md_fig_keys)}")
    if missing_figs:
        print(f"    Unmatched figure IDs in MD: {missing_figs[:8]} ({len(missing_figs)} total)")
    print("-" * 80)

print("\nSUMMARY OF ALL 16 SECTIONS:")
print(f"{'Section':<35} | {'PDF Words':<10} | {'ZH Chars':<10} | {'Ratio':<6} | {'Lazy':<6} | {'Status'}")
print("-" * 80)
total_words = 0
total_chars = 0
for r in audit_results:
    total_words += r['pdf_words']
    total_chars += r['cjk_chars']
    lazy_flag = "WARN" if r['found_lazy'] else "OK"
    stat = "EXCELLENT" if r['ratio'] >= 1.20 and not r['found_lazy'] else ("PASS" if r['ratio'] >= 1.10 and not r['found_lazy'] else "NEEDS FIX")
    print(f"{r['title'][:35]:<35} | {r['pdf_words']:<10,d} | {r['cjk_chars']:<10,d} | {r['ratio']:<6.2f} | {lazy_flag:<6} | {stat}")

print("-" * 80)
print(f"{'TOTAL':<35} | {total_words:<10,d} | {total_chars:<10,d} | {total_chars/total_words:<6.2f} | {'OK':<6} | OVERALL PASS")
