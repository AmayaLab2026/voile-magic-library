# -*- coding: utf-8 -*-
"""
Converter to pure markdown files in scripts/app_builders/
"""
import re, os

# Let's check build_app_a.py
with open('scripts/app_builders/build_app_a.py', 'r', encoding='utf-8') as f:
    text_a = f.read()
# extract between return r''' and '''
m = re.search(r"return r'''(.*)'''", text_a, re.DOTALL)
if m:
    with open('scripts/app_builders/app_a.md', 'w', encoding='utf-8') as out:
        out.write(m.group(1).strip() + '\n')
    print("app_a.md written, length:", len(m.group(1)))

# Let's check build_app_b.py
with open('scripts/app_builders/build_app_b.py', 'r', encoding='utf-8') as f:
    text_b = f.read()
m = re.search(r"return r'''(.*)'''", text_b, re.DOTALL)
if m:
    with open('scripts/app_builders/app_b.md', 'w', encoding='utf-8') as out:
        out.write(m.group(1).strip() + '\n')
    print("app_b.md written, length:", len(m.group(1)))

# Let's check app_e_full_dictionary.py
with open('scripts/app_builders/app_e_full_dictionary.py', 'r', encoding='utf-8') as f:
    text_e = f.read()
m = re.search(r"return r'''(.*)'''", text_e, re.DOTALL)
if m:
    with open('scripts/app_builders/app_e.md', 'w', encoding='utf-8') as out:
        out.write(m.group(1).strip() + '\n')
    print("app_e.md written, length:", len(m.group(1)))

