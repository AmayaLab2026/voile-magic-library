import re

with open('scripts/generate_comprehensive_audit_report.py', 'r', encoding='utf-8') as f:
    text = f.read()

# find CHAPTER_DEFS block
m = re.search(r'CHAPTER_DEFS = \{(.*?)\n\}', text, re.DOTALL)
if m:
    for line in m.group(1).splitlines():
        if 'pages' in line or 'title_zh' in line:
            print(line.strip())
