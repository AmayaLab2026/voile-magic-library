# -*- coding: utf-8 -*-
"""
Expander for Appendix D
Generates scripts/app_builders/app_d.md (~45,000 characters)
"""

# Let's write the complete text of app_d.md
p = "scripts/app_builders/app_d.md"

# Let's inspect the current app_d.md first
with open(p, 'r', encoding='utf-8') as f:
    current = f.read()

print("Current app_d.md length:", len(current))
