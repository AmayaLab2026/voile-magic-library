import re

def compare(fname):
    with open(f'docs/zh/fonts-encodings/{fname}', 'r', encoding='utf-8') as f:
        zh_text = f.read()
    with open(f'docs/ja/fonts-encodings/{fname}', 'r', encoding='utf-8') as f:
        ja_text = f.read()

    m_zh = re.findall(r'\$\$([\s\S]*?)\$\$', zh_text)
    m_ja = re.findall(r'\$\$([\s\S]*?)\$\$', ja_text)

    print(f'=== {fname} ===')
    print(f'ZH blocks: {len(m_zh)}, JA blocks: {len(m_ja)}')
    for i in range(max(len(m_zh), len(m_ja))):
        zh_b = m_zh[i].strip() if i < len(m_zh) else '---'
        ja_b = m_ja[i].strip() if i < len(m_ja) else '---'
        same = zh_b == ja_b
        if not same:
            print(f'Block {i}: same={same}')
            print(f'   ZH: {zh_b[:70]}')
            print(f'   JA: {ja_b[:70]}')

compare('chapter-12.md')
compare('appendices.md')
