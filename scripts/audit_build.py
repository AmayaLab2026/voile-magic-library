import fitz, glob, os, re

doc = fitz.open(r"C:\Users\Misak\Desktop\NASA TT F-928.pdf")

build_sections = [
    ("intro", 18, 19, "docs/zh/rocket-pioneers/kondratyuk-build/index.md"),
    ("sec1", 20, 23, "docs/zh/rocket-pioneers/kondratyuk-build/section-1.md"),
    ("sec2", 23, 27, "docs/zh/rocket-pioneers/kondratyuk-build/section-2.md"),
    ("sec3", 27, 35, "docs/zh/rocket-pioneers/kondratyuk-build/section-3.md"),
    ("sec4", 36, 38, "docs/zh/rocket-pioneers/kondratyuk-build/section-4.md"),
    ("sec5", 39, 41, "docs/zh/rocket-pioneers/kondratyuk-build/section-5.md"),
    ("sec6", 42, 51, "docs/zh/rocket-pioneers/kondratyuk-build/section-6.md"),
    ("commentary", 52, 59, "docs/zh/rocket-pioneers/kondratyuk-build/commentary.md"),
]

print("=== KONDRATYUK BUILD WORD COUNT AUDIT ===")
for name, p1, p2, path in build_sections:
    en_words = sum(len(doc[p-1].get_text().split()) for p in range(p1, p2+1))
    md_content = open(path, "r", encoding="utf-8").read()
    zh_chars = len(re.findall(r'[\u4e00-\u9fff]', md_content))
    ratio = zh_chars / en_words if en_words > 0 else 0
    print(f"Build {name:12s} | pp.{p1:3d}-{p2:3d} | EN words: {en_words:5d} | ZH chars: {zh_chars:5d} | ratio: {ratio:4.2f}")
