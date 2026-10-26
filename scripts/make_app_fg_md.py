# -*- coding: utf-8 -*-
import re

for letter in ['f', 'g']:
    with open(f'scripts/app_builders/build_app_{letter}.py', 'r', encoding='utf-8') as f:
        text = f.read()
    m = re.search(r'return r"""(.*)"""', text, re.DOTALL)
    if not m:
        m = re.search(r"return r'''(.*)'''", text, re.DOTALL)
    if m:
        with open(f'scripts/app_builders/app_{letter}.md', 'w', encoding='utf-8') as out:
            out.write(m.group(1).strip() + '\n')
        print(f"app_{letter}.md written, length:", len(m.group(1)))
    else:
        print(f"Failed for {letter}")
