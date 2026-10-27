import os
import re
import opencc

s2t = opencc.OpenCC('s2t')

# Load snippets
with open('scripts/app_c_section1_2_zh.md', 'r', encoding='utf-8') as f:
    c_snippet_zh = f.read()

with open('scripts/app_d_d7_d8_zh.md', 'r', encoding='utf-8') as f:
    d_snippet_zh = f.read()

with open('scripts/app_f_f1_f4_zh.md', 'r', encoding='utf-8') as f:
    f_snippet_zh = f.read()

# Load zh appendices.md
with open('docs/zh/fonts-encodings/appendices.md', 'r', encoding='utf-8') as f:
    zh_text = f.read()

# 1. Insert C snippet
# Target in Appendix C: right before '## C.1 PostScript Type 1 字体的内存拓扑与解密引擎'
target_c = '## C.1 PostScript Type 1 字体的内存拓扑与解密引擎'
# We rename existing C sections or insert C.1 and C.2
if target_c in zh_text:
    # We replace target_c with c_snippet_zh + '\n\n---\n\n## C.3 PostScript Type 1 字体的内存拓扑与解密引擎'
    # and update existing C.1 -> C.3 etc.
    zh_text = zh_text.replace(target_c, c_snippet_zh + '\n\n---\n\n## C.3 PostScript Type 1 字体的内存拓扑与解密引擎')
    print('Inserted C snippet into zh')
else:
    print('Target C not found!')

# 2. Insert D snippet
# Target in Appendix D: right before '## D.11 OpenType 1.8 矢量可变字体（Variable Fonts）体系演进'
target_d = '## D.11 OpenType 1.8 矢量可变字体（Variable Fonts）体系演进'
if target_d in zh_text:
    zh_text = zh_text.replace(target_d, d_snippet_zh + '\n\n---\n\n' + target_d)
    print('Inserted D snippet into zh')
else:
    print('Target D not found!')

# 3. Insert F snippet
# Target in Appendix F: right before '## F.1 METAFONT 编程语言与声明式几何方程求解器'
target_f = '## F.1 METAFONT 编程语言与声明式几何方程求解器'
if target_f in zh_text:
    zh_text = zh_text.replace(target_f, f_snippet_zh + '\n\n---\n\n## F.2 METAFONT 编程语言与声明式几何方程求解器')
    print('Inserted F snippet into zh')
else:
    print('Target F not found!')

# Write updated zh
with open('docs/zh/fonts-encodings/appendices.md', 'w', encoding='utf-8') as f:
    f.write(zh_text)
print('Updated zh/appendices.md successfully. Total chars:', len(zh_text))

# 4. Process zh-hant
hant_text = s2t.convert(zh_text)
with open('docs/zh-hant/fonts-encodings/appendices.md', 'w', encoding='utf-8') as f:
    f.write(hant_text)
print('Updated zh-hant/appendices.md successfully. Total chars:', len(hant_text))
