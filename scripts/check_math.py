import re
from scripts.app_builders import build_app_a, build_app_b, build_app_c, build_app_d, build_app_e, build_app_f, build_app_g

total_math = 0
for mod, name in [(build_app_a, 'A'), (build_app_b, 'B'), (build_app_c, 'C'), (build_app_d, 'D'), (build_app_e, 'E'), (build_app_f, 'F'), (build_app_g, 'G')]:
    func = getattr(mod, f'get_appendix_{name.lower()}')
    text = func()
    maths = re.findall(r'\$\$(.*?)\$\$', text, re.DOTALL)
    print(f'App {name}: {len(maths)} math blocks')
    total_math += len(maths)
print(f'Total math blocks: {total_math}')
