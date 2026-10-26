# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('ch9_extracted_text.txt', encoding='utf-8') as f:
    text = f.read()

pages = text.split('=== PAGE ')

def get_page_text(start, end):
    res = []
    for p in pages[1:]:
        p_num = int(p.split('\n')[0].split()[0])
        if start <= p_num <= end:
            res.append(f'--- PAGE {p_num} ---\n' + p)
    return '\n'.join(res)

print("Check pages 235-240:")
p_235_240 = get_page_text(235, 240)
print(f"Length 235-240: {len(p_235_240)}")

print("Check pages 259-264:")
p_259_264 = get_page_text(259, 264)
print(f"Length 259-264: {len(p_259_264)}")
