import re

with open('docs/zh/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    text_zh = f.read()
with open('docs/ja/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    text_ja = f.read()

m_zh = re.findall(r'\$\$([\s\S]*?)\$\$', text_zh)
m_ja = re.findall(r'\$\$([\s\S]*?)\$\$', text_ja)

print('ZH blocks:')
for i, b in enumerate(m_zh):
    print(f'[{i}] in JA? {b.strip() in text_ja}')
    if not (b.strip() in text_ja):
        print(f'   MISSING: {b.strip()[:100]}')
