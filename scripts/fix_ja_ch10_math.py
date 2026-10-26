with open('docs/ja/fonts-encodings/chapter-10.md', 'r', encoding='utf-8') as f:
    text = f.read()

target = r"""$$c = \left(\frac{a}{a'}\right) \times s$$"""
replacement = r"""$$c = \left(\frac{a}{a'}\right) \times s$$

例えば Times New Roman（$a' = 0.46$）へフォールバックした場合、実際の描画サイズは自動的に拡大補正されます：

$$c = \left(\frac{0.58}{0.46}\right) \times 14 \approx 1.26 \times 14 \approx 17.65 \ px$$"""

text = text.replace(target, replacement)

with open('docs/ja/fonts-encodings/chapter-10.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated ja chapter 10 math blocks!")
