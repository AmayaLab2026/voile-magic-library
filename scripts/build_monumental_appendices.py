# -*- coding: utf-8 -*-
"""
Master Builder for Appendices A-G
Target: >= 140,000 characters (Ratio >= 1.12 over 125,199 words)
All 38 figures embedded.
Exact matching display math blocks.
"""
import sys, re, opencc

sys.stdout.reconfigure(encoding='utf-8')

from scripts.app_builders.build_app_a import get_appendix_a
from scripts.app_builders.build_app_b import get_appendix_b
from scripts.app_builders.build_app_c import get_appendix_c
from scripts.app_builders.build_app_d import get_appendix_d
from scripts.app_builders.build_app_e import get_appendix_e
from scripts.app_builders.build_app_f import get_appendix_f
from scripts.app_builders.build_app_g import get_appendix_g

app_a = get_appendix_a()
app_b = get_appendix_b()
app_c = get_appendix_c()
app_d = get_appendix_d()
app_e = get_appendix_e()
app_f = get_appendix_f()
app_g = get_appendix_g()

print(f"App A: {len(app_a)} chars")
print(f"App B: {len(app_b)} chars")
print(f"App C: {len(app_c)} chars")
print(f"App D: {len(app_d)} chars")
print(f"App E: {len(app_e)} chars")
print(f"App F: {len(app_f)} chars")
print(f"App G: {len(app_g)} chars")

current_total = len(app_a) + len(app_b) + len(app_c) + len(app_d) + len(app_e) + len(app_f) + len(app_g)
print(f"Current total: {current_total} chars")
print(f"Target: >= 137,719 chars")
