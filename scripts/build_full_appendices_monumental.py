# -*- coding: utf-8 -*-
"""
Builder for Appendices A-G Monumental Reference Manual
Target: >= 140,000 characters (Ratio >= 1.12 over 125,199 words)
All 38 figures embedded.
Exact 15 display math blocks.
"""
import sys, os, re, opencc

sys.stdout.reconfigure(encoding='utf-8')

print("Starting generation of Appendices A-G...")
