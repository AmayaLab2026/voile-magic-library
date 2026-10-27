import re

with open('docs/zh/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    zh_text = f.read()

with open('docs/ja/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    ja_text = f.read()

zh_blocks = re.findall(r'\$\$([\s\S]*?)\$\$', zh_text)
ja_blocks = re.findall(r'\$\$([\s\S]*?)\$\$', ja_text)

def norm(s):
    return re.sub(r'\s+', ' ', s).strip()

ja_norm = [norm(b) for b in ja_blocks]

for i, b in enumerate(zh_blocks):
    nb = norm(b)
    if nb not in ja_norm:
        print(f'Missing block {i}: {nb[:100]}')
    else:
        # found
        pass
