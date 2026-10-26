# -*- coding: utf-8 -*-
import os

def get_appendix_e():
    p = os.path.join(os.path.dirname(__file__), 'app_e.md')
    with open(p, 'r', encoding='utf-8') as f:
        return f.read()
