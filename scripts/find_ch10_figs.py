with open('scripts/ch10_pdf_dump.txt', 'r', encoding='utf-8') as f:
    text = f.read()

import re
matches = re.findall(r'Figure 10-[0-9]+:.*', text)
for m in matches:
    print(m.encode('ascii', 'replace').decode('ascii'))
