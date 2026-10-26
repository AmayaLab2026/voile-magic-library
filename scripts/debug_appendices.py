import re

with open('docs/zh/fonts-encodings/appendices.md', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.split('\n')
in_code = False
count = 0
for i, l in enumerate(lines, 1):
    if l.strip().startswith('```'):
        in_code = not in_code
        continue
    if in_code:
        continue
    if '$' in l:
        count += 1
        if count <= 20:
            print(f'Line {i}: {l}')

print(f'Total lines with dollar: {count}')
