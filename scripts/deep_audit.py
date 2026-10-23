import fitz, glob, os, re

doc = fitz.open(r"C:\Users\Misak\Desktop\NASA TT F-928.pdf")

print("=== DEEP AUDIT OF TRANSLATION DEFICIENCIES ===")

# Audit 1: Preface
print("\n--- 1. PREFACE AUDIT ---")
# Check US space program
pdf_p5_6 = doc[4].get_text() + doc[5].get_text()
has_mercury = "Mercury" in pdf_p5_6
md_preface = open("docs/zh/rocket-pioneers/preface.md", "r", encoding="utf-8").read()
print("Mercury/Glenn/Cooper in PDF:", has_mercury)
print("Mercury/Glenn/Cooper in MD:", "水星" in md_preface or "格伦" in md_preface or "库珀" in md_preface or "Mercury" in md_preface)

# Check list of published works in Preface (pp. 9-10)
pdf_p9_10 = doc[8].get_text() + doc[9].get_text()
print("List of works in PDF (pp. 9-10):", "Vestnik Vozdukhoplavaniya" in pdf_p9_10)
print("List of works in MD:", "Vestnik" in md_preface or "航空通报" in md_preface or "航空通报" in md_preface)

# Audit 2: Build Section-2 Fig 4
print("\n--- 2. KONDRATYUK BUILD FIG 4 AUDIT ---")
md_sec2 = open("docs/zh/rocket-pioneers/kondratyuk-build/section-2.md", "r", encoding="utf-8").read()
print("build-fig4 in section-2.md:", "build-fig4" in md_sec2)
print("build-fig3 in section-2.md:", "build-fig3" in md_sec2)

# Audit 3: Build Commentary Fig 1
print("\n--- 3. KONDRATYUK BUILD COMMENTARY FIG 1 AUDIT ---")
md_b_comm = open("docs/zh/rocket-pioneers/kondratyuk-build/commentary.md", "r", encoding="utf-8").read()
print("commentary-fig1 in commentary.md:", "commentary-fig1" in md_b_comm)
print("commentary-fig2 in commentary.md:", "commentary-fig2" in md_b_comm)

# Audit 4: Space Chapters Word Count & Text Completeness
print("\n--- 4. KONDRATYUK SPACE CHAPTERS AUDIT ---")
space_ch_pages = [
    ("author-preface", 60, 61, "docs/zh/rocket-pioneers/kondratyuk-space/index.md"),
    ("ch1", 62, 63, "docs/zh/rocket-pioneers/kondratyuk-space/chapter-1.md"),
    ("ch2", 64, 65, "docs/zh/rocket-pioneers/kondratyuk-space/chapter-2.md"),
    ("ch3", 66, 70, "docs/zh/rocket-pioneers/kondratyuk-space/chapter-3.md"),
    ("ch4", 71, 72, "docs/zh/rocket-pioneers/kondratyuk-space/chapter-4.md"),
    ("ch5", 73, 75, "docs/zh/rocket-pioneers/kondratyuk-space/chapter-5.md"),
    ("ch6", 76, 85, "docs/zh/rocket-pioneers/kondratyuk-space/chapter-6.md"),
    ("ch7", 86, 87, "docs/zh/rocket-pioneers/kondratyuk-space/chapter-7.md"),
    ("ch8", 88, 101, "docs/zh/rocket-pioneers/kondratyuk-space/chapter-8.md"),
    ("ch9", 102, 109, "docs/zh/rocket-pioneers/kondratyuk-space/chapter-9.md"),
    ("ch10", 110, 113, "docs/zh/rocket-pioneers/kondratyuk-space/chapter-10.md"),
    ("ch11", 113, 114, "docs/zh/rocket-pioneers/kondratyuk-space/chapter-11.md"),
    ("ch12", 114, 116, "docs/zh/rocket-pioneers/kondratyuk-space/chapter-12.md"),
    ("ch13", 116, 118, "docs/zh/rocket-pioneers/kondratyuk-space/chapter-13.md"),
    ("commentary", 119, 127, "docs/zh/rocket-pioneers/kondratyuk-space/commentary.md"),
]

for name, p1, p2, path in space_ch_pages:
    en_words = sum(len(doc[p-1].get_text().split()) for p in range(p1, p2+1))
    md_content = open(path, "r", encoding="utf-8").read()
    zh_chars = len(re.findall(r'[\u4e00-\u9fff]', md_content))
    ratio = zh_chars / en_words if en_words > 0 else 0
    print(f"Space {name:15s} | pp.{p1:3d}-{p2:3d} | EN words: {en_words:5d} | ZH chars: {zh_chars:5d} | ratio: {ratio:4.2f}")

# Audit 5: Historical Outline Sections Word Count
print("\n--- 5. HISTORICAL OUTLINE SECTIONS AUDIT ---")
hist_sections = [
    ("intro", 128, 136, "docs/zh/rocket-pioneers/historical-outline/index.md"),
    ("sec1", 137, 144, "docs/zh/rocket-pioneers/historical-outline/section-1.md"),
    ("sec2", 145, 148, "docs/zh/rocket-pioneers/historical-outline/section-2.md"),
    ("sec3", 149, 155, "docs/zh/rocket-pioneers/historical-outline/section-3.md"),
    ("sec4", 156, 158, "docs/zh/rocket-pioneers/historical-outline/section-4.md"),
]

for name, p1, p2, path in hist_sections:
    en_words = sum(len(doc[p-1].get_text().split()) for p in range(p1, p2+1))
    md_content = open(path, "r", encoding="utf-8").read()
    zh_chars = len(re.findall(r'[\u4e00-\u9fff]', md_content))
    ratio = zh_chars / en_words if en_words > 0 else 0
    print(f"Hist  {name:15s} | pp.{p1:3d}-{p2:3d} | EN words: {en_words:5d} | ZH chars: {zh_chars:5d} | ratio: {ratio:4.2f}")
