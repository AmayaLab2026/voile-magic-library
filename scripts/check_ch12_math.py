import re

with open('docs/zh/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    text_zh = f.read()
with open('docs/zh-hant/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    text_hant = f.read()
with open('docs/ja/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    text_ja = f.read()

m_zh = re.findall(r'\$\$([\s\S]*?)\$\$', text_zh)
m_hant = re.findall(r'\$\$([\s\S]*?)\$\$', text_hant)
m_ja = re.findall(r'\$\$([\s\S]*?)\$\$', text_ja)

print(f'ZH: {len(m_zh)}, HANT: {len(m_hant)}, JA: {len(m_ja)}')

# Let's inspect zh-hant conversion: if zh-hant is converted from zh, why did it have 14?
# Because apply_ch12_enrichment.py failed earlier on zh-hant due to a mismatched end_kw!
