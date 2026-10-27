with open('docs/zh/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    zh = f.read()
with open('docs/ja/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    ja = f.read()

target1 = r'E(\mathbf{P}_1, \mathbf{P}_2)'
target2 = r'\text{BlueValues}'
target3 = r'\text{Threshold Size}'

for t in [target1, target2, target3]:
    print(f'=== {t} in ZH: ===')
    idx = zh.find(t)
    if idx != -1:
        print(zh[idx-50:idx+150])
    print(f'=== {t} in JA: ===')
    idx_j = ja.find(t)
    if idx_j != -1:
        print(ja[idx_j-50:idx_j+150])
    else:
        print('NOT FOUND IN JA')
