# -*- coding: utf-8 -*-
import os

for letter in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
    py_path = f'scripts/app_builders/build_app_{letter}.py'
    content = f"""# -*- coding: utf-8 -*-
import os

def get_appendix_{letter}():
    p = os.path.join(os.path.dirname(__file__), 'app_{letter}.md')
    with open(p, 'r', encoding='utf-8') as f:
        return f.read()
"""
    with open(py_path, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Updated {py_path}")
