with open('scripts/ch10_content.md', 'r', encoding='utf-8') as f:
    text = f.read()

p = 'docs/zh/fonts-encodings/chapter-10.md'
with open(p, 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Applied ch10 to {p} ({len(text)} characters)")
