# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

text = open("scripts/full_pdf_toc_extracted.txt", encoding="utf-8").read()

start = text.find("Fonts in TEX and Ω")
if start == -1:
    start = text.find("Fonts in")
end = text.find("10 Fonts and Web Pages", start)

print(text[start-50:end+50])
