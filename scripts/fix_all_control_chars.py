import os

# 1. Fix app_c.md
path_c = 'scripts/app_builders/app_c.md'
if os.path.exists(path_c):
    with open(path_c, 'r', encoding='utf-8') as f:
        text = f.read()
    text = text.replace('\x08mod', '\\bmod')
    text = text.replace(' mod M', ' \\bmod M')
    with open(path_c, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'Fixed {path_c}')

# 2. Fix appendices across all 3 languages
for lang in ['zh', 'zh-hant', 'ja']:
    p = f'docs/{lang}/fonts-encodings/appendices.md'
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            text = f.read()
        text = text.replace('\x08mod', '\\bmod')
        text = text.replace(' mod M', ' \\bmod M')
        with open(p, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f'Fixed {p}')

# 3. Fix chapter-12
for lang in ['zh', 'zh-hant']:
    p = f'docs/{lang}/fonts-encodings/chapter-12.md'
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            text = f.read()
        text = text.replace('  `\x0cea\n  pos @T_LEFT @O_RIGHT -75;\n  `', '```fea\npos @T_LEFT @O_RIGHT -75;\n```')
        text = text.replace('\x0cea', 'fea')
        # Also check line 233: `$ 字母 (N^2)$`
        text = text.replace('$ 字母 (N^2)$', '字母 $O(N^2)$')
        text = text.replace('$ 字母 (N^2)$', '字母 $O(N^2)$')
        with open(p, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f'Fixed {p}')

p_gen12 = 'scripts/generate_deep_ch12.py'
if os.path.exists(p_gen12):
    with open(p_gen12, 'r', encoding='utf-8') as f:
        text = f.read()
    text = text.replace('\x0cea', 'fea')
    with open(p_gen12, 'w', encoding='utf-8') as f:
        f.write(text)
    print(f'Fixed {p_gen12}')

# 4. Fix chapter-9
for lang in ['zh', 'zh-hant', 'ja']:
    p = f'docs/{lang}/fonts-encodings/chapter-9.md'
    if os.path.exists(p):
        with open(p, 'r', encoding='utf-8') as f:
            text = f.read()
        text = text.replace('\x02;', '\\2;')
        with open(p, 'w', encoding='utf-8') as f:
            f.write(text)
        print(f'Fixed {p}')

print('All control characters fixed!')
