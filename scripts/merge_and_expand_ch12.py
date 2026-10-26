# -*- coding: utf-8 -*-
import sys, re
import opencc

sys.stdout.reconfigure(encoding='utf-8')
t2s = opencc.OpenCC('t2s')
s2tw = opencc.OpenCC('s2twp')

# Read current zh-hant ch12 which has 15459 chars
with open('docs/zh-hant/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    hant_text = f.read()

# Protect code blocks and math blocks during conversion
def convert_t2s(text):
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

    converted = t2s.convert(text)

    for i, im in enumerate(inline_math):
        converted = converted.replace(f"__INLINE_MATH_{i}__", im)
    for i, mb in enumerate(math_blocks):
        converted = converted.replace(f"__MATH_BLOCK_{i}__", mb)
    for i, cb in enumerate(code_blocks):
        converted = converted.replace(f"__CODE_BLOCK_{i}__", cb)

    return converted

zh_base = convert_t2s(hant_text)

# Ensure standalone translator line
zh_base = re.sub(r'\*?译者：.*?\n', '*译者：[Lycoris \\<lycorismisaka@gmail.com\\>](mailto:lycorismisaka@gmail.com)*\n\n', zh_base)

# Enrich with Fontographer figure and ScanFont detailed section if missing
if 'fig12-1.png' not in zh_base:
    fig12_block = '''
::: tip Macromedia Fontographer 在 Mac OS X 下的字体视窗（Figure 12-1）
![Macromedia Fontographer 在 Mac OS X 下的字体视窗（Figure 12-1）](/images/fonts-encodings/fig12-1.png)
*Macromedia Fontographer 在 Mac OS X 下的字体视窗（Figure 12-1）*
:::

*图 12-1：Macromedia Fontographer 运行于 Mac OS X 平台下的核心操作界面。上方展现了以十六进制矩阵或字符表顺序排列的字库总览网格，每一个方格实时反映了对应字形在当前外框下的微缩剪影。*
'''
    zh_base = zh_base.replace('## 1. 字体设计与数字化全景导论（Introduction）', '## 1. 字体设计与数字化全景导论（Introduction）\n' + fig12_block)

with open('docs/zh/fonts-encodings/chapter-12.md', 'w', encoding='utf-8') as f:
    f.write(zh_base)

print(f"docs/zh/fonts-encodings/chapter-12.md written: {len(zh_base)} chars")
