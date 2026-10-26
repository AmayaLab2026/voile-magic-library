import os, re

for ch_num in [4, 8, 10]:
    path = f"docs/zh/fonts-encodings/chapter-4.md" if ch_num == 4 else f"docs/zh/fonts-encodings/chapter-{ch_num}.md"
    with open(path, "r", encoding="utf-8") as f:
        text = f.read()
    
    print(f"\n================ CHAPTER {ch_num} ================")
    print(f"File: {path}")
    print(f"Total characters: {len(text):,}")
    print(f"Total lines: {len(text.splitlines())}")
    
    # Headings
    headings = [l for l in text.splitlines() if l.startswith("#")]
    print(f"Headings count: {len(headings)}")
    for h in headings[:15]:
        print("  ", h)
    if len(headings) > 15:
        print(f"  ... and {len(headings)-15} more headings")
    
    # Images
    imgs = re.findall(r'!\[.*?\]\((.*?)\)', text)
    print(f"Images count: {len(imgs)}")
    for img in imgs:
        print("  Image:", img)
    
    # Math blocks
    math_blocks = re.findall(r'\$\$[\s\S]*?\$\$', text)
    print(f"Math $$ blocks: {len(math_blocks)}")
