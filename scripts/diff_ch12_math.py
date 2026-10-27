import re

with open('docs/zh/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    zh_text = f.read()

with open('docs/ja/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    ja_text = f.read()

zh_blocks = re.findall(r'\$\$([\s\S]*?)\$\$', zh_text)
ja_blocks = re.findall(r'\$\$([\s\S]*?)\$\$', ja_text)

print(f'ZH blocks: {len(zh_blocks)}')
print(f'JA blocks: {len(ja_blocks)}')

ja_cleaned = [b.strip() for b in ja_blocks]

for i, b in enumerate(zh_blocks):
    b_strip = b.strip()
    if b_strip not in ja_cleaned:
        print(f'\n--- Missing in JA block {i}: ---')
        print(b_strip)
