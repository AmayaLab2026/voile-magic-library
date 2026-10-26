with open('docs/zh/fonts-encodings/chapter-10.md', 'r', encoding='utf-8') as f:
    text = f.read()

import re
lines = text.splitlines()
print(f"Total lines: {len(lines)}, total chars: {len(text)}")
for i, l in enumerate(lines):
    if l.startswith('#'):
        print(f"L{i+1}: {l.encode('ascii', 'replace').decode('ascii')}")

imgs = re.findall(r'!\[.*?\]\((.*?)\)', text)
print(f"\nImages ({len(imgs)}):")
for img in imgs:
    print(" ", img)

maths = re.findall(r'\$\$[\s\S]*?\$\$', text)
print(f"\nMath blocks ({len(maths)}):")
for m in maths:
    print(" ", m.strip())
