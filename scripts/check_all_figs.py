import fitz, glob, os, re

doc = fitz.open(r"C:\Users\Misak\Desktop\NASA TT F-928.pdf")

# Extracted images in folder
extracted = [os.path.basename(f) for f in glob.glob("docs/public/images/rocket-pioneers/*.png")]

print("=== CHECKING ALL FIGURES IN PDF VS EXTRACTED FILES ===")

# 1. Kibalchich (pp. 12-17): Fig 1, Fig 2
print("Kibalchich:")
print("  kibalchich-fig1.png in folder:", "kibalchich-fig1.png" in extracted)
print("  kibalchich-fig2.png in folder:", "kibalchich-fig2.png" in extracted)

# 2. Build (pp. 18-51): Fig 1 to 26
print("\nBuild (Figs 1-26):")
for i in range(1, 27):
    fn = f"build-fig{i}.png"
    print(f"  {fn}: {fn in extracted}")

# 3. Build Commentary (pp. 52-59): Fig 1, 2, 3, 4
print("\nBuild Commentary (Figs 1-4):")
for i in range(1, 5):
    fn = f"commentary-fig{i}.png"
    print(f"  {fn}: {fn in extracted}")

# 4. Space (pp. 60-109): Fig 1 to 8
print("\nSpace (Figs 1-8):")
for i in range(1, 9):
    fn = f"space-fig{i}.png"
    print(f"  {fn}: {fn in extracted}")

# 5. Historical Outline (pp. 128-158): Fig 1, Fig 2
print("\nHistorical Outline (Figs 1-2):")
print("  history-nezhdanovskiy-manuscript.png (Fig 1, p.132):", "history-nezhdanovskiy-manuscript.png" in extracted)
print("  history-fedorov-pipe.png (Fig 2, p.136):", "history-fedorov-pipe.png" in extracted)

# Wait! Are there any other figures or illustrations in Historical Outline?
# Let's check pages 128 to 158
for p in range(127, 158):
    txt = doc[p].get_text()
    figs = re.findall(r'(?:Figure|Fig\.?)\s*(\d+[a-z]?)', txt, re.IGNORECASE)
    if figs:
        print(f"  Page {p+1}: {figs}")
