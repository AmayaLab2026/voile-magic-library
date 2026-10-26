# -*- coding: utf-8 -*-
import os

def get_appendix_b():
    p = os.path.join(os.path.dirname(__file__), 'app_b.md')
    with open(p, 'r', encoding='utf-8') as f:
        return f.read()
