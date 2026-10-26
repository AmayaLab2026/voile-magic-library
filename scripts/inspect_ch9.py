with open('docs/zh/fonts-encodings/chapter-9.md', 'r', encoding='utf-8') as f:
    lines = f.readlines()
for i in range(890, 900):
    print(f'{i+1}: {repr(lines[i])}')
