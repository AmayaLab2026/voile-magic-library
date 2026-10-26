import sys, re
import opencc

sys.stdout.reconfigure(encoding='utf-8')
converter = opencc.OpenCC('s2twp')

with open('docs/zh/fonts-encodings/chapter-4.md', 'r', encoding='utf-8') as f:
    zh = f.read()

def convert_preserving(text):
    code_blocks = []
    def code_repl(m):
        code_blocks.append(m.group(0))
        return f"__CODE_BLOCK_{len(code_blocks)-1}__"
    text = re.sub(r'```[\s\S]*?```', code_repl, text)

    math_blocks = []
    def math_repl(m):
        math_blocks.append(m.group(0))
        return f"__MATH_BLOCK_{len(math_blocks)-1}__"
    text = re.sub(r'\$\$[\s\S]*?\$\$', math_repl, text)

    inline_math = []
    def inline_repl(m):
        inline_math.append(m.group(0))
        return f"__INLINE_MATH_{len(inline_math)-1}__"
    text = re.sub(r'\$[^\$\n]+?\$', inline_repl, text)

    converted = converter.convert(text)

    for i, im in enumerate(inline_math):
        converted = converted.replace(f"__INLINE_MATH_{i}__", im)

    for i, mb in enumerate(math_blocks):
        converted = converted.replace(f"__MATH_BLOCK_{i}__", mb)

    for i, cb in enumerate(code_blocks):
        converted = converted.replace(f"__CODE_BLOCK_{i}__", cb)

    return converted

zh_hant = convert_preserving(zh)
zh_hant = zh_hant.replace('*譯者：[Lycoris <lycorismisaka@gmail.com>]', '*譯者：[Lycoris \\<lycorismisaka@gmail.com\\>]')

with open('docs/zh-hant/fonts-encodings/chapter-4.md', 'w', encoding='utf-8') as f:
    f.write(zh_hant)

print(f"docs/zh-hant/fonts-encodings/chapter-4.md written: {len(zh_hant)} chars")
