with open('docs/zh/fonts-encodings/chapter-4.md', 'r', encoding='utf-8') as f:
    text = f.read()

lines = text.splitlines()
print(f"Total lines: {len(lines)}")
for i, l in enumerate(lines):
    if l.startswith('#'):
        print(f"Line {i+1}: {l}")
