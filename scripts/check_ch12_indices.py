import opencc

s2t = opencc.OpenCC('s2t')

with open('docs/zh/fonts-encodings/chapter-12.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Locate duplicate
# The duplicate begins at index 24613 and ends at index 32182
# Let's inspect text[22000:25000]
p1 = text.find('### 4. 纵向排版（Vertical Typesetting）与纵向度量中枢')
p2 = text.find('## 第六部分：从位图扫描到矢量轮廓跟踪算法')
p3 = text.find('## 第六部分：从位图扫描到矢量轮廓跟踪算法', p2 + 10)

print(f'p1: {p1}, p2: {p2}, p3: {p3}')

# What we want:
# Section 5 continues with p1 (enrichment)
# Then Section 6 starts ONCE
# Then Section 7
# Then conclusion

# Let's see what is between p2 and p3:
# Between p2 and p3 is: Section 6 content + enrichment!
# So p1 was placed AFTER p2!
# Let's clean this up properly!
