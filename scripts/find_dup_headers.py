with open('docs/zh/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    text = f.read()

import re

# Find occurrences of '## 第六部分：从位图扫描到矢量轮廓跟踪算法'
target = '## 第六部分：从位图扫描到矢量轮廓跟踪算法'
indices = [m.start() for m in re.finditer(re.escape(target), text)]
print('Occurrences of Section 6 header:', indices)

# Find occurrences of '## 第七部分：字体内置微观对齐控制参数与渲染提示'
target7 = '## 第七部分：字体内置微观对齐控制参数与渲染提示'
indices7 = [m.start() for m in re.finditer(re.escape(target7), text)]
print('Occurrences of Section 7 header:', indices7)
