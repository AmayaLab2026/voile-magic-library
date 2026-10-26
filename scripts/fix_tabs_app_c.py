# -*- coding: utf-8 -*-
with open('scripts/app_builders/app_c.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Replace tab followed by 'ext' or 'imes'
fixed = text.replace('\times', '\\times').replace('\text', '\\text')
# Also in case raw tab byte exists
fixed = fixed.replace('\t', '\\t')

with open('scripts/app_builders/app_c.md', 'w', encoding='utf-8') as f:
    f.write(fixed)

print("Fixed app_c.md math formulas")
