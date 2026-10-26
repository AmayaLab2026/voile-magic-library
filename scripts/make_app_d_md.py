# -*- coding: utf-8 -*-

with open('scripts/app_builders/build_app_d.py', 'r', encoding='utf-8') as f:
    text = f.read()

import re
m = re.search(r'return r"""(.*)"""', text, re.DOTALL)
if not m:
    m = re.search(r"return r'''(.*)'''", text, re.DOTALL)

if m:
    with open('scripts/app_builders/app_d.md', 'w', encoding='utf-8') as out:
        out.write(m.group(1).strip() + '\n')
    print("Successfully written scripts/app_builders/app_d.md, length:", len(m.group(1)))
else:
    print("Pattern not matched in build_app_d.py")
