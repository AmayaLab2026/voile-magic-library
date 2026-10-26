# -*- coding: utf-8 -*-
import os

parts = []
for fname in ['app_d_sec1.md', 'app_d_sec2.md', 'app_d_sec2_extra.md', 'app_d_sec3.md', 'app_d_sec4.md']:
    p = os.path.join('scripts/app_builders', fname)
    with open(p, 'r', encoding='utf-8') as f:
        parts.append(f.read().strip())

full_text = '\n\n'.join(parts) + '\n'

with open('scripts/app_builders/app_d.md', 'w', encoding='utf-8') as out:
    out.write(full_text)

print("Successfully written scripts/app_builders/app_d.md, total length:", len(full_text))
