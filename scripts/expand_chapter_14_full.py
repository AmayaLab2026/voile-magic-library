# -*- coding: utf-8 -*-
"""
Deeply expand Chapter 14 to >= 35,500 characters (ratio >= 1.13):
- Preserves git HEAD's rich foundation
- Embeds all 15 figures (fig14-1 to fig14-15)
- Preserves 2 display math blocks
- Deep technical expansion of GSUB/GPOS tables, AFDKO, VOLT, AAT state machines
"""
import subprocess, sys, re, opencc

sys.stdout.reconfigure(encoding='utf-8')

proc = subprocess.run(['git', 'show', 'HEAD:docs/zh/fonts-encodings/chapter-14.md'], stdout=subprocess.PIPE)
head_text = proc.stdout.decode('utf-8')

print(f"HEAD text length: {len(head_text)}")
