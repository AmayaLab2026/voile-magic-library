with open('scripts/ch4_content.md', 'r', encoding='utf-8') as f:
    text = f.read()

p = 'docs/zh/fonts-encodings/chapter-4.md'
with open(p, 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Wrote {p} ({len(text)} characters)")
