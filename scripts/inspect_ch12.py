with open('docs/zh/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(230, 245):
    print(f'{i+1}: {repr(lines[i])}')
