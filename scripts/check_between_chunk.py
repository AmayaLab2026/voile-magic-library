with open('docs/zh/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    text = f.read()

p1 = 24613
p2 = 32182
print('Length of between chunk:', p2 - p1)
print('Start of between chunk:')
print(text[p1:p1+300])
print('End of between chunk:')
print(text[p2-300:p2])
