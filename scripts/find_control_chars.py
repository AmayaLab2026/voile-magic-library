import os

def check_file(filepath):
    with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()
    
    bad = []
    for idx, c in enumerate(content):
        cp = ord(c)
        # allow \t (9), \n (10), \r (13)
        if cp < 32 and cp not in (9, 10, 13):
            line_no = content[:idx].count('\n') + 1
            bad.append((line_no, cp, repr(c)))
    return bad

found = 0
for root, dirs, files in os.walk('docs'):
    for file in files:
        if file.endswith('.md'):
            p = os.path.join(root, file)
            b = check_file(p)
            if b:
                print(f'{p}:')
                for l, cp, r in b:
                    print(f'  Line {l}: ord={cp} {r}')
                found += len(b)

for root, dirs, files in os.walk('scripts'):
    for file in files:
        if file.endswith('.md') or file.endswith('.py'):
            p = os.path.join(root, file)
            b = check_file(p)
            if b:
                print(f'{p}:')
                for l, cp, r in b:
                    print(f'  Line {l}: ord={cp} {r}')
                found += len(b)

print(f'Total bad control characters found: {found}')
