import sys, re
sys.stdout.reconfigure(encoding='utf-8')
p = 'docs/zh/fonts-encodings/appendices.md'
with open(p, 'r', encoding='utf-8') as f:
    text = f.read()
blocks = re.findall(r'\$\$(.*?)\$\$', text, re.DOTALL)
print(f'Appendices has {len(blocks)} math blocks:')
for i, b in enumerate(blocks):
    print(f'[{i+1}]: {b.strip()}\n')
