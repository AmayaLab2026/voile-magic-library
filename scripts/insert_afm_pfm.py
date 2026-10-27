import opencc

s2t = opencc.OpenCC('s2t')

with open('scripts/app_c_afm_pfm_zh.md', 'r', encoding='utf-8') as f:
    snippet_zh = f.read()

snippet_hant = s2t.convert(snippet_zh)

# Update zh
with open('docs/zh/fonts-encodings/appendices.md', 'r', encoding='utf-8') as f:
    zh_text = f.read()

target_zh = '## C.7 CFF 字典键值与二进制操作码权威词典'
if target_zh in zh_text:
    zh_text = zh_text.replace(target_zh, snippet_zh + '\n\n---\n\n' + target_zh)
    with open('docs/zh/fonts-encodings/appendices.md', 'w', encoding='utf-8') as f:
        f.write(zh_text)
    print('Inserted AFM/PFM into zh/appendices.md. Total chars:', len(zh_text))
else:
    print('Target not found in zh!')

# Update zh-hant
with open('docs/zh-hant/fonts-encodings/appendices.md', 'r', encoding='utf-8') as f:
    hant_text = f.read()

target_hant = s2t.convert(target_zh)
if target_hant in hant_text:
    hant_text = hant_text.replace(target_hant, snippet_hant + '\n\n---\n\n' + target_hant)
    with open('docs/zh-hant/fonts-encodings/appendices.md', 'w', encoding='utf-8') as f:
        f.write(hant_text)
    print('Inserted AFM/PFM into zh-hant/appendices.md. Total chars:', len(hant_text))
else:
    print('Target not found in zh-hant!')
