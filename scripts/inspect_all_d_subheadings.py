# -*- coding: utf-8 -*-
with open('appendices_real_text.txt', 'r', encoding='utf-8') as f:
    lines = f.readlines()

import re
in_d = False
for i in range(5549, 14675):
    line = lines[i].strip()
    if re.match(r'^D\.\d+(\.\d+)?\s+', line):
        print(f"Line {i}: {line}")
