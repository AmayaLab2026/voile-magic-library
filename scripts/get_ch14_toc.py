# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

text = open("scripts/full_pdf_toc_extracted.txt", encoding="utf-8").read()

start = text.find("14 Enriching Fonts")
if start == -1:
    start = text.find("Enriching Fonts")
end = text.find("Appendix A", start)

print(text[start:end])
