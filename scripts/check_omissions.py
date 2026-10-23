import fitz, glob, os, re

doc = fitz.open(r"C:\Users\Misak\Desktop\NASA TT F-928.pdf")

def check_phrases(pdf_pages, md_path, test_phrases):
    pdf_text = " ".join([doc[p-1].get_text() for p in pdf_pages])
    md_text = open(md_path, "r", encoding="utf-8").read()
    results = []
    for en_phrase, zh_concept in test_phrases:
        in_pdf = en_phrase.lower() in pdf_text.lower()
        in_md = any(k.lower() in md_text.lower() for k in zh_concept)
        results.append((en_phrase, zh_concept, in_pdf, in_md))
    return results

print("=== CHECKING SPECIFIC PHRASES FOR OMISSIONS ===")

# Test 1: Historical Outline Section 1 (pp. 137-144)
# Meshcherskiy's equations and Tsiolkovskiy's formulas
p1_tests = [
    ("variable-mass point", ["变质量", "变质量点"]),
    ("Vestnik Vozdukhoplavaniya", ["航空通报", "Vestnik"]),
    ("Cosmic Rocket Trains", ["宇宙火箭列车", "火箭列车"]),
    ("hydrocarbons", ["烃", "碳氢化合物"]),
    ("combustion chamber", ["燃烧室"]),
    ("44,000 to 45,000 m", ["44000", "45000", "44,000", "45,000"]),
    ("semi-jet stratoplane", ["半喷气", "半喷气式平流层飞机"]),
    ("graphite rudders", ["石墨舵", "燃气舵"]),
]
res1 = check_phrases(range(137, 145), "docs/zh/rocket-pioneers/historical-outline/section-1.md", p1_tests)
print("\n--- Hist Sec 1 (pp. 137-144) ---")
for en, zh, in_p, in_m in res1:
    print(f"[{'MISSING' if not in_m else 'OK'}] '{en}': in_pdf={in_p}, in_md={in_m}")

# Test 2: Space Chapter 8 (pp. 88-101)
# Atmospheric resistance and equations
p8_tests = [
    ("equation (29)", ["式 (29)", "式(29)", "公式 (29)", "公式(29)"]),
    ("equation (30)", ["式 (30)", "式(30)", "公式 (30)", "公式(30)"]),
    ("equation (33)", ["式 (33)", "式(33)", "公式 (33)", "公式(33)"]),
    ("equation (34)", ["式 (34)", "式(34)", "公式 (34)", "公式(34)"]),
    ("k4 = 1/3", ["k_4 = 1/3", "k4", "1/3"]),
    ("c/P = 1/62,500", ["62,500", "62500"]),
    ("m = 29.3", ["29.3"]),
    ("T = 0.09", ["0.09"]),
]
res8 = check_phrases(range(88, 102), "docs/zh/rocket-pioneers/kondratyuk-space/chapter-8.md", p8_tests)
print("\n--- Space Chapter 8 (pp. 88-101) ---")
for en, zh, in_p, in_m in res8:
    print(f"[{'MISSING' if not in_m else 'OK'}] '{en}': in_pdf={in_p}, in_md={in_m}")

# Test 3: Space Chapter 6 (pp. 76-85)
p6_tests = [
    ("tangential trajectory", ["切向", "切向轨道"]),
    ("hybrid type trajectory", ["混合", "混合轨道"]),
    ("Figure 1", ["图 1", "Figure 1", "space-fig1"]),
    ("Figure 2", ["图 2", "Figure 2", "space-fig2"]),
    ("equations (1)", ["式 (1)", "公式 (1)", "公式(1)"]),
    ("equations (11)", ["式 (11)", "公式 (11)", "公式(11)"]),
    ("equations (12)", ["式 (12)", "公式 (12)", "公式(12)"]),
    ("equations (17)", ["式 (17)", "公式 (17)", "公式(17)"]),
    ("equations (25)", ["式 (25)", "公式 (25)", "公式(25)"]),
]
res6 = check_phrases(range(76, 86), "docs/zh/rocket-pioneers/kondratyuk-space/chapter-6.md", p6_tests)
print("\n--- Space Chapter 6 (pp. 76-85) ---")
for en, zh, in_p, in_m in res6:
    print(f"[{'MISSING' if not in_m else 'OK'}] '{en}': in_pdf={in_p}, in_md={in_m}")
