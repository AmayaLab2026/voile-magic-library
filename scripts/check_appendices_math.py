import sys, re
sys.stdout.reconfigure(encoding='utf-8')
for lang in ['zh', 'zh-hant', 'ja']:
    p = f'docs/{lang}/fonts-encodings/appendices.md'
    with open(p, 'r', encoding='utf-8') as f:
        text = f.read()
    blocks = re.findall(r'\$\$(.*?)\$\$', text, re.DOTALL)
    print(f'{lang} appendices: {len(text)} chars, {len(blocks)} display math blocks')
