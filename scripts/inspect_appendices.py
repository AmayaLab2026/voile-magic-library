import re
for p in ['docs/zh/fonts-encodings/appendices.md', 'docs/zh-hant/fonts-encodings/appendices.md', 'docs/ja/fonts-encodings/appendices.md']:
    with open(p, 'r', encoding='utf-8') as f_in:
        text = f_in.read()
    blocks = re.findall(r'\$\\$\$', text, re.DOTALL)
    figs = re.findall(r'!\[.*?\]\((.*?)\)', text)
    print(p, 'chars:', len(text), 'math blocks:', len(blocks), 'figs:', len(figs))
