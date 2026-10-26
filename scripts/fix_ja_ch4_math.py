with open('docs/ja/fonts-encodings/chapter-4.md', 'r', encoding='utf-8') as f:
    text = f.read()

target = r"""$$\text{SBase} = \text{0xAC00}, \quad L_{\text{count}} = 19, \quad V_{\text{count}} = 21, \quad T_{\text{count}} = 28, \quad N_{\text{count}} = 588$$"""
replacement = r"""$$\text{SBase} = \text{0xAC00}$$
$$L_{\text{count}} = 19, \quad V_{\text{count}} = 21, \quad T_{\text{count}} = 28$$
$$N_{\text{count}} = V_{\text{count}} \times T_{\text{count}} = 21 \times 28 = 588$$"""

text = text.replace(target, replacement)
with open('docs/ja/fonts-encodings/chapter-4.md', 'w', encoding='utf-8') as f:
    f.write(text)

print("Updated ja math blocks!")
