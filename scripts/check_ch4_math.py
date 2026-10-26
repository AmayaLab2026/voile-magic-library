import sys, re
sys.stdout.reconfigure(encoding='utf-8')
for lang in ['zh', 'zh-hant', 'ja']:
    p = f'docs/{lang}/fonts-encodings/chapter-4.md'
    with open(p, 'r', encoding='utf-8') as f:
        text = f.read()
    blocks = re.findall(r'\$\$(.*?)\$\$', text, re.DOTALL)
    print(f'{lang} ch4: {len(text)} chars, {len(blocks)} display math blocks')
    for i, b in enumerate(blocks):
        print(f'  [{i+1}]: {b.strip()[:60]}...')
