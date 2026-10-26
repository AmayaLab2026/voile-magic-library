import sys, re
sys.stdout.reconfigure(encoding='utf-8')
with open('docs/zh/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    text = f.read()

blocks = re.findall(r'\$\$(.*?)\$\$', text, re.DOTALL)
for i, b in enumerate(blocks):
    print(f'[{i+1}]:\n{b.strip()}\n')
