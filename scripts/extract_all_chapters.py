# -*- coding: utf-8 -*-
import sys, re
sys.stdout.reconfigure(encoding='utf-8')

text = open("scripts/full_pdf_toc_extracted.txt", encoding="utf-8").read()

# Pattern for Chapter / Part / Appendix in TOC
# Notice how O'Reilly TOC has:
# Number alone or "Introduction" or "Appendix X"
# followed by title, followed by dots and page number
# Let's extract all main items

lines = text.splitlines()
i = 0
toc_entries = []

while i < len(lines):
    l = lines[i].strip()
    # Check if introduction or number alone
    if l in ["Introduction", "Contents", "Index"] or re.match(r'^(Part\s+[IVX]+|\d+|Appendix\s+[A-Z])$', l):
        category = l
        if l == "Contents":
            i += 1
            continue
        title = ""
        page = ""
        # look forward for title and page
        j = i + 1
        while j < min(i + 15, len(lines)):
            l_next = lines[j].strip()
            if re.match(r'^\d+$', l_next) and j > i + 1:
                page = l_next
                break
            elif not title and l_next and not l_next.startswith("---") and not l_next.startswith("."):
                title = l_next
            elif title and l_next and not l_next.startswith("---") and not l_next.startswith("."):
                if not re.match(r'^\d+$', l_next):
                    title += " " + l_next
            j += 1
        toc_entries.append((category, title, page, i))
    i += 1

for cat, tit, pg, line_no in toc_entries:
    print(f"[{cat:12s}] {tit:45s} -> Page {pg}")
