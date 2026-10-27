import opencc

s2t = opencc.OpenCC('s2t')

with open('docs/zh/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Section 5 enrichment (FontForge features: Vertical typesetting, CID, Autotracing in FontForge)
with open('scripts/ch12_enrichment.md', 'r', encoding='utf-8') as f:
    enrich_zh = f.read()

# Let's locate the parts of original chapter 12:
# Part A: up to end of Spiro (right before ### 4. 纵向排版)
p_spiro_end = text.find('### 4. 纵向排版（Vertical Typesetting）与纵向度量中枢')
part_before = text[:p_spiro_end].strip()

# Part B: Section 6 and Section 7 and Conclusion from sec6_second
# Find the second occurrence of '## 第六部分：从位图扫描到矢量轮廓跟踪算法'
target_sec6 = '## 第六部分：从位图扫描到矢量轮廓跟踪算法'
p_sec6_second = text.rfind(target_sec6)
part_after = text[p_sec6_second:].strip()

# Assemble clean zh
clean_zh = part_before + '\n\n' + enrich_zh.strip() + '\n\n---\n\n' + part_after + '\n'

with open('docs/zh/fonts-encodings/chapter-12.md', 'w', encoding='utf-8') as f:
    f.write(clean_zh)
print('Fixed zh/chapter-12.md cleanly. Total chars:', len(clean_zh))

# Generate zh-hant cleanly
clean_hant = s2t.convert(clean_zh)
with open('docs/zh-hant/fonts-encodings/chapter-12.md', 'w', encoding='utf-8') as f:
    f.write(clean_hant)
print('Fixed zh-hant/chapter-12.md cleanly. Total chars:', len(clean_hant))
