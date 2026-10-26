---
title: "Fonts & Encodings: From Unicode to Advanced Typography and Everything in Between"
description: "Vol. 03 of Voile Magic Library. Definitive monumental work by Yannis Haralambous, Ph.D. Complete unabridged 1:1 original English edition."
---

# Fonts & Encodings: From Unicode to Advanced Typography and Everything in Between
### Voile Magic Library · Collection Vol. 03
**Author: Yannis Haralambous, Ph.D. (Translated and Expanded by P. Scott Horne, Ph.D.)**  
**Catalog Call Number: `VML-Z250.8.H37-2007`** · **Publisher: O'Reilly Media, Inc. (2007)**

---

## Archival Overview

*Homo sapiens* is a species that writes. And among the large number of tools used for writing, the most recent and the most complex is the computer—a tool for reading and writing, a medium for storage, and a means of exchanging data, all rolled into one. It has become a veritable "space in which the text resides," a space that has encircled our planet.

Within this digital writing space, **fonts** and **encodings** play distinct yet fundamentally intertwined roles:
* **Encoding** is an abstraction of the mind, a table of abstract characters;
* **Font** is a container of concrete glyphs, visual depictions that appear on screen or paper.

This monumental treatise—spanning over 1,000 pages—stands as the definitive, encyclopedic reference on digital typography, character encodings, and the mathematical foundations of computer typography.

---

## Author Profile: Yannis Haralambous, Ph.D.

* **Academic Position**: Professor of Computer Science at IMT Atlantique (formerly École Nationale Supérieure des Télécommunications de Bretagne, ENST Bretagne), Brest, France.
* **Background & Theoretical Formations**: Born in Greece, Haralambous studied pure mathematics in France and obtained his doctorate in pure mathematics from Université de Lille I. His deep expertise in differential geometry and topology enabled him to revolutionize computer typography and glyph contour modeling.
* **Pioneer of the $\Omega$ (Omega) System**: In the 1990s, together with John Plaice, Haralambous created $\Omega$, an extension of Donald E. Knuth's TeX typesetting system that broke through 8-bit limitations to provide native 16/32-bit Unicode support and finite-state text translation processes (OTPs).
* **International Expert**: Active member and consultant for the Unicode Consortium, the Association Typographique Internationale (ATypI), and the TeX Users Group (TUG).

---

## Table of Contents & Curriculum Structure

### Preliminaries
* **[Introduction: Explorations](./introduction)**  
  The letter and its parts, letterpress typesetting, digital typesetting, font formats, characters and glyphs, and the general structure of the book.

### Part I: Encodings & Unicode
* **[Chapter 1: Before Unicode](./chapter-1)**  
  FIELDATA, ASCII, EBCDIC, ISO 2022, ISO 8859 families (Latin-1 through Latin-16), East Asian multi-byte encodings, vendor code pages, email, and the early Web.
* **[Chapter 2: Characters, glyphs, bytes: An introduction to Unicode](./chapter-2)**  
  Philosophical issues, Unicode core principles, character encoding forms (UTF-8, UTF-16, UTF-32, CESU-8, SCSU), the BMP and higher planes.
* **[Chapter 3: Properties of Unicode characters](./chapter-3)**  
  Names, blocks, scripts, general categories, case properties, rendering properties (Arabic/Syriac), grapheme clusters, numeric properties, and the UCD.
* **[Chapter 4: Normalization, bidirectionality, and East Asian characters](./chapter-4)**  
  Canonical and compatibility decompositions, normalization forms (NFC, NFD, NFKC, NFKD), Unicode Bidirectional Algorithm (Bidi), and CJK Unihan ideographs.
* **[Chapter 5: Using Unicode](./chapter-5)**  
  Character palette tools across Mac OS X, Windows, and Linux; keyboard layout tools (MSKLC, Keyman Developer); ICU framework.

### Part II: Font Management
* **[Chapter 6: Font Management on the Macintosh](./chapter-6)**  
  Mac OS 9 resource forks and suitcases; Mac OS X font domains and Font Book; Core Graphics rendering pipeline.
* **[Chapter 7: Font Management under Windows](./chapter-7)**  
  Windows Fonts folder, GDI logical fonts (LOGFONT), registry management, and ClearType subpixel rendering.
* **[Chapter 8: Font Management under X Window](./chapter-8)**  
  X11 logical font descriptors (XLFD), X font servers (XFS), modern client-side rendering with FreeType, Fontconfig, and Xft.

### Part III: Typographic Software & Web
* **[Chapter 9: Fonts in TEX and Ω, their installation and use](./chapter-9)**  
  Knuth's TeX compilation architecture, TFM metric files, DVI drivers, Virtual Fonts, and Omega's 16/32-bit OTP pipeline.
* **[Chapter 10: Fonts and Web Pages](./chapter-10)**  
  HTML and CSS font specifications, aspect ratio and `font-size-adjust`, web font embedding (Bitstream TrueDoc, Microsoft WEFT/EOT), and SVG fonts.

### Part IV: Typeface Art, Design & Typography
* **[Chapter 11: The History and Classifications of Latin Typefaces](./chapter-11)**  
  Historical evolution from Gutenberg and Jenson to modern sans-serifs, Vox/ATypI classification, and Panose-1 10-digit visual metric system.
* **[Chapter 12: Creating and Modifying Fonts](./chapter-12)**  
  FontLab and FontForge workflows, cubic vs quadratic Bézier curves, contour winding rules, metrics, and class-based kerning.
* **[Chapter 13: Optimizing a rasterization](./chapter-13)**  
  Low-resolution rasterization dilemmas, PostScript declarative hints (BlueValues, stem hints), and TrueType virtual machine instructions.
* **[Chapter 14: Enriching Fonts: Advanced Typography](./chapter-14)**  
  OpenType layout architecture (GSUB, GPOS, GDEF), Adobe feature file syntax, Microsoft VOLT, and Apple AAT finite state automata.

### Part V: Technical Reference Manual
* **[Appendices A–G: Technical Reference Manual](./appendices)**  
  Comprehensive reference: Bitmap fonts (A), TeX & Omega formats (B), PostScript language and Type 1/CFF (C), TrueType/OpenType/AAT table specifications (D), TrueType instruction set (E), METAFONT (F), and Bézier curve mathematical proofs (G).
