import re

path = r'node_modules/.pnpm/mathjax-full@3.2.2/node_modules/mathjax-full/js/core/MmlTree/OperatorDictionary.js'
with open(path, 'r', encoding='utf-8') as f:
    text = f.read()

ranges = []
for m in re.finditer(r'\[\s*(0x[0-9a-fA-F]+)\s*,\s*(0x[0-9a-fA-F]+)', text):
    start = int(m.group(1), 16)
    end = int(m.group(2), 16)
    ranges.append((start, end))

def in_range(cp):
    for s, e in ranges:
        if s <= cp <= e:
            return True
    return False

with open(r'docs/zh/fonts-encodings/appendices.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Check display math
math_blocks = re.findall(r'\$\$([\s\S]*?)\$\$', content)
print(f'Checking {len(math_blocks)} display blocks...')

for idx, block in enumerate(math_blocks):
    # Check if there are non-ASCII characters outside standard math ranges
    for line in block.split('\n'):
        # Match any character that isn't standard ASCII or known Greek/math
        for ch in line:
            cp = ord(ch)
            if cp > 127 and not in_range(cp):
                print(f'Block {idx+1}: char {repr(ch)} (U+{cp:04X}) in line: {line.strip()}')

# Also check inline math $...$
inline_math = re.findall(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)', content)
print(f'Checking {len(inline_math)} inline math expressions...')
for idx, inline in enumerate(inline_math):
    for ch in inline:
        cp = ord(ch)
        if cp > 127 and not in_range(cp):
            print(f'Inline {idx+1}: char {repr(ch)} (U+{cp:04X}) in: {inline.strip()}')
