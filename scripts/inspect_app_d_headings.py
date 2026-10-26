# -*- coding: utf-8 -*-
with open('appendices_real_text.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

import re
d_lines = []
in_d = False
for i, line in enumerate(lines):
    if re.match(r'^(APPENDIX|Appendix)\s+D', line.strip()):
        in_d = True
    elif re.match(r'^(APPENDIX|Appendix)\s+E', line.strip()):
        in_d = False
    if in_d:
        if line.strip().startswith('D.') or (line.strip().isupper() and len(line.strip()) < 40 and not line.strip().startswith('PAGE')):
            d_lines.append((i, line.strip()))

for idx, heading in d_lines[:40]:
    print(f"Line {idx}: {heading}")
