# -*- coding: utf-8 -*-
import re
from scripts.app_builders import build_app_a, build_app_b, build_app_c, build_app_d, build_app_e, build_app_f, build_app_g

all_figs = []
for mod, name in [(build_app_a, 'A'), (build_app_b, 'B'), (build_app_c, 'C'), (build_app_d, 'D'), (build_app_e, 'E'), (build_app_f, 'F'), (build_app_g, 'G')]:
    func = getattr(mod, f'get_appendix_{name.lower()}')
    text = func()
    figs = re.findall(r'!\[.*?\]\((/images/fonts-encodings/fig-app-[a-z0-9]+\.png)\)', text)
    print(f"App {name}: {len(figs)} figures: {figs}")
    all_figs.extend(figs)

print(f"\nTotal unique figures found: {len(set(all_figs))}")
print(f"Total figure references found: {len(all_figs)}")
