# -*- coding: utf-8 -*-
"""
Converts docs/zh/fonts-encodings/appendices.md to docs/zh-hant/fonts-encodings/appendices.md
using opencc, protecting code blocks, math blocks, and image links.
"""
import opencc, re

with open('docs/zh/fonts-encodings/appendices.md', 'r', encoding='utf-8') as f:
    zh_text = f.read()

converter = opencc.OpenCC('s2t')

# Protect code blocks and math blocks from conversion
tokens = []
def placeholder(match):
    tokens.append(match.group(0))
    return f"__PRESERVED_BLOCK_{len(tokens)-1}__"

# Protect code blocks ``` ... ```
protected = re.sub(r'```.*?```', placeholder, zh_text, flags=re.DOTALL)
# Protect display math $$ ... $$
protected = re.sub(r'\$\$.*?\$\$', placeholder, protected, flags=re.DOTALL)
# Protect inline math $ ... $
protected = re.sub(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)', placeholder, protected)
# Protect image links
protected = re.sub(r'!\[(.*?)\]\((/images/[^)]+)\)', placeholder, protected)

# Convert prose
hant_text = converter.convert(protected)

# Restore protected blocks
for idx, token in enumerate(tokens):
    # If the token is an image link, convert alt text only
    if token.startswith('![') and '/images/' in token:
        m = re.match(r'!\[(.*?)\]\((.*?)\)', token)
        if m:
            alt = converter.convert(m.group(1))
            url = m.group(2)
            token = f"![{alt}]({url})"
    hant_text = hant_text.replace(f"__PRESERVED_BLOCK_{idx}__", token)

# Ensure translator line in zh-hant has proper escaped brackets
hant_text = re.sub(r'\*譯者：\[Lycoris.*?\)\*', r'*譯者：[Lycoris \\<lycorismisaka@gmail.com\\>](mailto:lycorismisaka@gmail.com)*', hant_text)

with open('docs/zh-hant/fonts-encodings/appendices.md', 'w', encoding='utf-8') as out:
    out.write(hant_text)

print(f"Successfully generated docs/zh-hant/fonts-encodings/appendices.md: {len(hant_text):,} characters")
