import opencc

s2t = opencc.OpenCC('s2t')

with open('docs/zh/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    zh_content = f.read()

# Update zh-hant by converting zh directly
hant_content = s2t.convert(zh_content)
with open('docs/zh-hant/fonts-encodings/chapter-12.md', 'w', encoding='utf-8') as f:
    f.write(hant_content)
print('Synced zh-hant/chapter-12.md with zh. Total chars:', len(hant_content))
