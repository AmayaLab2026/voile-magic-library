with open('docs/zh/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    text = f.read()

part1 = text[:24613] # up to the first Section 6
sec6_first = text[24613:32182]
sec6_second = text[32182:]

print('sec6_first length:', len(sec6_first))
print('sec6_second length:', len(sec6_second))
print('sec6_first start:', sec6_first[:200])
print('sec6_second start:', sec6_second[:200])
