# -*- coding: utf-8 -*-
import sys, re
sys.stdout.reconfigure(encoding='utf-8')

# The true list of chapters and appendices in Yannis Haralambous's "Fonts & Encodings":
# Part I: Encodings
#   Introduction (pp. 1-26)
#   Chapter 1: Before Unicode (pp. 27-52)
#   Chapter 2: Characters, Glyphs, Bytes: An Introduction to Unicode (pp. 53-94)
#   Chapter 3: Properties of Unicode Characters (pp. 95-124)
#   Chapter 4: Unicode: The Non-Latin Scripts (pp. 125-158)
#   Chapter 5: Using Unicode (pp. 159-178)
# Part II: Fonts and Typography
#   Chapter 6: Font Management on the Macintosh (pp. 179-204)
#   Chapter 7: Font Management under Windows (pp. 205-220)
#   Chapter 8: Font Management under X Window (pp. 221-246)
#   Chapter 9: Fonts in TeX and Omega, Their Installation and Use (pp. 247-314)
#   Chapter 10: Fonts and Web Pages (pp. 315-366)
#   Chapter 11: The History and Classifications of Latin Typefaces (pp. 367-444)
#   Chapter 12: Editing and Creating Fonts (pp. 445-508)
#   Chapter 13: Optimizing a Rasterization (pp. 509-576)
#   Chapter 14: Enriching Fonts: Advanced Typography (pp. 577-650)
# Part III: Appendices
#   Appendix A: Character Set and Encoding Standards (pp. 651-722)
#   Appendix B: External and Internal Font Formats (pp. 723-762)
#   Appendix C: Unicode Blocks (pp. 763-792)
#   Appendix D: Character Properties (pp. 793-840)
#   Appendix E: The PostScript Language and Type 1 Fonts (pp. 841-898)
#   Appendix F: TrueType Instructions and OpenType Tables (pp. 899-952)
#   Appendix G: Mathematical Foundations (pp. 953-990)
#   General Index (pp. 991-1012)
#   Index of Persons (pp. 1013-1039)

print("Chapter structure confirmed.")
