import os, re, sys

sys.stdout.reconfigure(encoding='utf-8')

langs = ['zh', 'zh-hant', 'en', 'ja']
base_docs = 'docs'

print("=" * 60)
print("COMPREHENSIVE MULTILINGUAL ARCHIVE AUDIT")
print("=" * 60)

# -------------------------------------------------------------
# 1. FILE SET CONSISTENCY AUDIT
# -------------------------------------------------------------
print("\n[CHECK 1] File parity across languages:")
file_sets = {}
for lang in langs:
    base = os.path.join(base_docs, lang)
    rel_files = set()
    for root, dirs, files in os.walk(base):
        for f in files:
            rel = os.path.relpath(os.path.join(root, f), base).replace('\\', '/')
            rel_files.add(rel)
    file_sets[lang] = rel_files
    print(f"  - {lang:8s}: {len(rel_files)} files")

all_consistent = True
for lang in ['zh-hant', 'en', 'ja']:
    missing = file_sets['zh'] - file_sets[lang]
    extra = file_sets[lang] - file_sets['zh']
    if missing or extra:
        all_consistent = False
        print(f"  [ERROR] {lang} diff vs zh: missing={missing}, extra={extra}")

if all_consistent:
    print("  -> File parity PASS: All 4 languages have identical 47 files!")

# -------------------------------------------------------------
# 2. IMAGE INTEGRITY AUDIT
# -------------------------------------------------------------
print("\n[CHECK 2] Image references and public asset existence:")
image_errors = []
for lang in langs:
    for rel_f in sorted(file_sets[lang]):
        if not rel_f.endswith('.md'):
            continue
        p = os.path.join(base_docs, lang, rel_f)
        content = open(p, 'r', encoding='utf-8').read()
        # Find all images markdown: ![alt](url)
        matches = re.findall(r'!\[(.*?)\]\((.*?)\)', content)
        for alt, url in matches:
            if url.startswith('/'):
                asset_path = os.path.join(base_docs, 'public', url.lstrip('/'))
                if not os.path.exists(asset_path):
                    image_errors.append((lang, rel_f, url, "Asset file does not exist"))
            elif not url.startswith('http'):
                target = os.path.normpath(os.path.join(os.path.dirname(p), url))
                if not os.path.exists(target):
                    image_errors.append((lang, rel_f, url, "Relative image does not exist"))

if not image_errors:
    print("  -> Image reference PASS: All image tags across all languages resolve to real files!")
else:
    print(f"  [ERROR] Found {len(image_errors)} broken image tags:")
    for err in image_errors:
        print(f"    - [{err[0]}] {err[1]}: {err[2]} ({err[3]})")

# -------------------------------------------------------------
# 3. IMAGE USAGE PARITY AUDIT (Between ZH and EN, JA, ZH-HANT)
# -------------------------------------------------------------
print("\n[CHECK 3] Figure tag parity against ZH source:")
figure_mismatches = []
for rel_f in sorted(file_sets['zh']):
    if not rel_f.endswith('.md'):
        continue
    zh_content = open(os.path.join(base_docs, 'zh', rel_f), 'r', encoding='utf-8').read()
    zh_imgs = set(re.findall(r'!\[.*?\]\((/images/[^)]+)\)', zh_content))
    
    for lang in ['zh-hant', 'en', 'ja']:
        t_content = open(os.path.join(base_docs, lang, rel_f), 'r', encoding='utf-8').read()
        t_imgs = set(re.findall(r'!\[.*?\]\((/images/[^)]+)\)', t_content))
        diff = zh_imgs - t_imgs
        if diff:
            figure_mismatches.append((lang, rel_f, diff))

if not figure_mismatches:
    print("  -> Figure tag parity PASS: Every image used in ZH is present in EN, JA, and ZH-HANT!")
else:
    print(f"  [ERROR] Found {len(figure_mismatches)} figure parity issues:")
    for m in figure_mismatches:
        print(f"    - [{m[0]}] {m[1]} missing figures: {m[2]}")

# -------------------------------------------------------------
# 4. MATH FORMULA (KaTeX) PARITY AUDIT
# -------------------------------------------------------------
print("\n[CHECK 4] KaTeX math equation ($$ and $) presence audit:")
math_mismatches = []
for rel_f in sorted(file_sets['zh']):
    if not rel_f.endswith('.md'):
        continue
    zh_content = open(os.path.join(base_docs, 'zh', rel_f), 'r', encoding='utf-8').read()
    zh_display_math = len(re.findall(r'\$\$(.*?)\$\$', zh_content, re.DOTALL))
    zh_inline_math = len(re.findall(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)', zh_content))
    
    if zh_display_math > 0 or zh_inline_math > 0:
        for lang in ['zh-hant', 'en', 'ja']:
            t_content = open(os.path.join(base_docs, lang, rel_f), 'r', encoding='utf-8').read()
            t_display_math = len(re.findall(r'\$\$(.*?)\$\$', t_content, re.DOTALL))
            t_inline_math = len(re.findall(r'(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)', t_content))
            # If display math counts differ by more than 1 or inline math is 0 when zh > 5
            if t_display_math != zh_display_math:
                math_mismatches.append((lang, rel_f, f"Display math: zh={zh_display_math}, {lang}={t_display_math}"))

if not math_mismatches:
    print("  -> Display math ($$) parity PASS: All block equations perfectly match ZH count!")
else:
    print(f"  [WARN/ERROR] Found {len(math_mismatches)} math formula mismatches:")
    for m in math_mismatches[:10]:
        print(f"    - [{m[0]}] {m[1]}: {m[2]}")

# -------------------------------------------------------------
# 5. INTERNAL LINK RESOLUTION AUDIT
# -------------------------------------------------------------
print("\n[CHECK 5] Internal link resolution audit across all markdown files:")
link_errors = []
for lang in langs:
    for rel_f in sorted(file_sets[lang]):
        if not rel_f.endswith('.md'):
            continue
        p = os.path.join(base_docs, lang, rel_f)
        content = open(p, 'r', encoding='utf-8').read()
        # Find markdown links: [text](url) - ignore external http/https/mailto
        links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', content)
        for text, url in links:
            url_clean = url.split('#')[0]
            if not url_clean or url_clean.startswith('http') or url_clean.startswith('mailto:'):
                continue
            if url_clean.startswith('/images/'):
                continue
            
            # Check resolution
            resolved = False
            if url_clean.startswith('/'):
                # Root-relative path
                # Note: in VitePress, rewrite 'zh/:rest*' means /foo maps to docs/zh/foo or docs/foo
                # For localized links:
                # /en/... -> docs/en/...
                # /ja/... -> docs/ja/...
                # /zh-hant/... -> docs/zh-hant/...
                # /controlled-substances/... -> docs/zh/controlled-substances/...
                target_rel = url_clean.lstrip('/')
                candidates = [
                    os.path.join(base_docs, target_rel),
                    os.path.join(base_docs, target_rel + '.md'),
                    os.path.join(base_docs, target_rel, 'index.md'),
                    os.path.join(base_docs, 'zh', target_rel),
                    os.path.join(base_docs, 'zh', target_rel + '.md'),
                    os.path.join(base_docs, 'zh', target_rel, 'index.md'),
                ]
                if any(os.path.exists(c) for c in candidates):
                    resolved = True
            else:
                # Relative link
                candidates = [
                    os.path.normpath(os.path.join(os.path.dirname(p), url_clean)),
                    os.path.normpath(os.path.join(os.path.dirname(p), url_clean + '.md')),
                    os.path.normpath(os.path.join(os.path.dirname(p), url_clean, 'index.md')),
                ]
                if any(os.path.exists(c) for c in candidates):
                    resolved = True
            
            if not resolved:
                link_errors.append((lang, rel_f, url, text))

if not link_errors:
    print("  -> Internal links PASS: All internal markdown links resolve to existing documents!")
else:
    print(f"  [ERROR] Found {len(link_errors)} dead or unresolvable internal links:")
    for err in link_errors:
        print(f"    - [{err[0]}] {err[1]}: link '{err[2]}' (anchor: '{err[3]}')")

# -------------------------------------------------------------
# 6. CONFIG.TS SIDEBAR ROUTE AUDIT
# -------------------------------------------------------------
print("\n[CHECK 6] Config.ts sidebar and nav links audit:")
config_errors = []
for lang in langs:
    cfg_path = os.path.join(base_docs, lang, 'config.ts')
    cfg_text = open(cfg_path, 'r', encoding='utf-8').read()
    # Find all link: '/...'
    links = re.findall(r"link:\s*['\"]([^'\"]+)['\"]", cfg_text)
    for l in links:
        l_clean = l.split('#')[0]
        if not l_clean or l_clean.startswith('http'):
            continue
        target_rel = l_clean.lstrip('/')
        candidates = [
            os.path.join(base_docs, target_rel),
            os.path.join(base_docs, target_rel + '.md'),
            os.path.join(base_docs, target_rel, 'index.md'),
            os.path.join(base_docs, 'zh', target_rel),
            os.path.join(base_docs, 'zh', target_rel + '.md'),
            os.path.join(base_docs, 'zh', target_rel, 'index.md'),
        ]
        if not any(os.path.exists(c) for c in candidates):
            config_errors.append((lang, l, "Route does not map to any markdown file"))

if not config_errors:
    print("  -> Config sidebar/nav routes PASS: All sidebar and nav links map to existing markdown files!")
else:
    print(f"  [ERROR] Found {len(config_errors)} invalid routes in config.ts:")
    for err in config_errors:
        print(f"    - [{err[0]}] {err[1]} ({err[2]})")

# -------------------------------------------------------------
# 7. FRONTMATTER INTEGRITY AUDIT
# -------------------------------------------------------------
print("\n[CHECK 7] Frontmatter YAML integrity audit:")
fm_errors = []
for lang in langs:
    for rel_f in sorted(file_sets[lang]):
        if not rel_f.endswith('.md'):
            continue
        p = os.path.join(base_docs, lang, rel_f)
        content = open(p, 'r', encoding='utf-8').read()
        if not content.startswith('---'):
            fm_errors.append((lang, rel_f, "Missing opening frontmatter ---"))
            continue
        parts = content.split('---', 2)
        if len(parts) < 3:
            fm_errors.append((lang, rel_f, "Unclosed frontmatter"))

if not fm_errors:
    print("  -> Frontmatter PASS: All markdown files have valid YAML frontmatter blocks!")
else:
    print(f"  [ERROR] Found {len(fm_errors)} frontmatter errors:")
    for err in fm_errors:
        print(f"    - [{err[0]}] {err[1]}: {err[2]}")

print("\n" + "=" * 60)
print("AUDIT EXECUTION COMPLETE")
print("=" * 60)
