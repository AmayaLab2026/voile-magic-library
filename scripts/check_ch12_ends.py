with open('docs/zh/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    text = f.read()

sec6_first = text[24613:32182]
sec6_second = text[32182:]

print('sec6_first end:')
print(sec6_first[-500:])
print('='*50)
print('sec6_second end:')
print(sec6_second[-500:])
