import re

with open('docs/zh/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    zh = f.read()
with open('docs/ja/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    ja = f.read()

m_zh = re.findall(r'\$\$([\s\S]*?)\$\$', zh)
m_ja = re.findall(r'\$\$([\s\S]*?)\$\$', ja)

print(f'ZH has {len(m_zh)} blocks:')
for i, b in enumerate(m_zh):
    print(f'  ZH[{i}]: {b.strip()[:50]}')

print(f'\nJA has {len(m_ja)} blocks:')
for i, b in enumerate(m_ja):
    print(f'  JA[{i}]: {b.strip()[:50]}')
