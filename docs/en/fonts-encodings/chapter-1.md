---
title: "Chapter 1: Before Unicode"
description: "Unabridged English text: FIELDATA, ASCII, EBCDIC, ISO 2022, ISO 8859 families, East Asian encodings, Microsoft and Apple code pages, email and Web encodings."
---

# Chapter 1: Before Unicode
**By Yannis Haralambous, Ph.D.**
*From Fonts & Encodings, pp. 27–52*

---

The Structure of the Book and Ways to Use It actually buys is a license to use it. According to the foundry, this license may or may not specify the number of machines and/or printers on which the font may be installed and used. But no foundry will allow someone who has bought a license for one of its fonts to distribute that font publicly. How, then, can one display the glyphs of a document in a particular font if one does not have the right to distribute it? Electronic documents are caught between the past (typography, glyphs and their arrangement, fonts) and the future (the Web, characters, information that can be indexed at will and made available to everyone). In saying that, we have taken only two axes of our digital space for writing into account: the system approach (characters/glyphs) and historicity. There remain the geographic axis (East/West, with all the surprises that the writing systems of other cultures have in store for us) and the industrial axis (problems of file format, platform, etc.). In this book, we aim to offer the reader a certain number of tools to confront these problems. We do not concern ourselves with all aspects of the electronic document, just those pertaining to characters and glyphs, aspects that directly and inevitably affect encodings and fonts. The Structure of the Book and Ways to Use It This book contains 14 chapters grouped into 4 units and 7 appendices. We have repeatedly said that fonts and encodings interact like yin and yang. Here we use this metaphor to give a graphical illustration of the book’s structure with the yin–yang symbol (Figure 0-6) in the background. On the left, in the gray-shaded area: encodings. On the right, in the white part: fonts. At the top of the circle is the introduction that the reader is currently reading. The first box, the one on the left, contains the five chapters on encodings, in particular Unicode. In the first chapter, entitled “Before Unicode”, we present a history of codes and encodings, starting in antiquity. After a few words on systems of encoding used in telecommunication before the advent of the computer, we proceed immediately to the most well-known encoding of all, ASCII, and its staunch competitor, EBCDIC. Then follows the ISO 8859 series of encodings, the most recent of which was released in 2001. At the same time, we discuss the problems of the countries of the Far East and the different solutions offered by ISO, Microsoft, and the UNIX world. Finally, we end with a few words on electronic mail and the Web. The second chapter, “Characters, Glyphs, Bytes”, is an introduction to Unicode. In it, we develop the underlying concepts of Unicode, the principles on which it is based, its philosophy, and the technical choices that it has made. We finish the chapter with a quick look at the different tables of Unicode, including a preview of the tables that are still at the stage of consideration that precedes inclusion in the encoding. Next comes the chapter “Unicode Character Properties”, which leads us into the morass of the data that accompanies the characters. Often this data indicates that the character

::: tip Typographical Specimen Plate (Figure 0-6)
![Figure 0-6: The general structure of this book](/images/fonts-encodings/fig0-6-book-structure.png)
*Figure 0-6: The general structure of this book.*
:::

```text
Introduction
A. Bitmap fonts
B. TEX et Ω fonts
C. PostScript fonts
D. TrueType, OpenType
and AAT fonts
E. TrueType instructions
G. Bézier curves
2. Characters,
glyphs, bytes
3. Unicode character
properties
bidirectionality,
CJK characters
6. Font management
on the Macintosh
7. Font management
under Windows
8. Font management
under X Window
9.  Fonts under
TEX and Ω
classifications
fonts
13. Optimizing the rendering
14. Advanced typographical
features
F.  METAFONT and
its derivatives
Introduction
Bibliographic
references
General index
Index of names
e
n
c
o
d
i
n
g
s
/
c
h
a
r
a
ct
e
rs
f
o
n
ts
/
g
l
y
p
h
s
Appendices
Figure 0-6: Structure of the chapters of this book.
```

```text
The Structure of the Book and Ways to Use It
in question plays a certain role. We explain this role by showing the reader some of the
internal workings of the encoding.
On the subject of internal workings, we have assembled three of the most complex in
Chapter 4. This chapter’s title is merely a list of these three mechanisms: normalization,
the bidirectional algorithm, and the handling of East Asian characters. Normalization
is a set of ways to make a text encoded in Unicode more efficient by removing certain
ambiguities; in particular, one of the normalization forms that we describe is required
for the use of Unicode on the Web. Bidirectionality concerns the mixture of left-to-right
and right-to-left scripts. Unicode gives us an algorithm to define the typesetting of a text
containing a mixture of this sort. Finally, by “East Asian scripts” we mean both Chinese
ideographs and hangul syllables. For the former, we present a handful of techniques to
obtain characters not supplied in Unicode; for the latter, we describe the method for
forming syllables from hangul letters.
Finally, the last chapter in this unit is less theoretical than the others. We address a
specific problem: how to produce a text encoded in Unicode? We offer three possible
answers: by entering characters with a mouse, by creating virtual keyboards, and by
converting texts written in other encodings. In each of these three cases, we describe
appropriate tools for use under Mac OS, Windows, or UNIX.
This unit lies entirely within the gray section (“encodings”), as we discuss only encodings,
not fonts, in its chapters.
The second unit (Chapters 6 to 8) lies within the white section (“fonts”), but we have
placed it in the center of the circle because it discusses not fonts themselves but their
management. Thus it takes up the installation of fonts, tools for activation/deactivation,
font choices—in short, the management of a large number of fonts, which is of concern to graphic designers and other large consumers of fonts. The unit is divided into
three chapters so that we can discuss the two most popular operating systems—Mac OS
(9 or X) and Windows, as well as the X Window windowing system from the UNIX world.
We discover that the Macintosh is privileged (it has the greatest number of tools for
font management), that the same tools exist for Windows but that their quality is often
poorer, and that X Window is a world unto itself, with its own advantages and drawbacks.
These three chapters will thrill neither the computer scientist nor the typophile, but
they may be of great practical value to those whose lives are plagued by system crashes,
unexplainable slow-downs, poor quality of output (who has never been surprised to see
his beautiful Bembo replaced by a hideous Courier?), corrupted documents, and all sorts
of other such mishaps, often caused by fonts. They will also delight those who love order
and who dream of being able to find and use almost instantaneously any font among the
thousands of similar ones that they have collected on multiple CD-ROMs. On the other
hand, if the reader uses only the fonts that come standard on his operating system, he
has no need to read these chapters.
The third unit (Chapters 9 and 10) gets more technical. It deals with the use of fonts in
two specific cases: the TEX typesetting system (and its successor, Ω, of which the author is
```

```text
Introduction
co-developer) and Web pages. TEX is a software system and a programming language devoted to typesetting. It is also used today to produce electronic documents. Its approach
to managing fonts is unique and totally independent of the operating system being used.
In this chapter, we have tried to cover as thoroughly as possible all the many aspects of
the use of fonts under TEX. Technical descriptions of the font formats used in Chapter 9
appear in Appendix B (“The Font Formats of TEX and Ω”).
The situation is different in the case of the Web, which presents both technical problems
(How to supply a font to the browser? How to make the browser use it automatically?)
and legal ones (What about the font’s copyright?). We describe the different solutions
that Microsoft and Bitstream have offered for this problem and also another spectacular
solution: the GlyphGate font server. This approach can be called conventional: we use
the HTML markup system and supply the fonts in addition. The Web Consortium has
proposed another, cleaner, solution: describe the font in XML, just like the rest of the
document. This solution is part of the SVG standard for the description of vector graphics, which we describe in detail.
These two chapters are also placed in the middle of the circle because they deal with
subjects that lie in between encodings and fonts: TEX and HTML can both be considered
as vehicles for passing from characters to glyphs; they are bridges between the two worlds.
The fourth unit (Chapters 11 to 14 and Appendix F) is devoted completely to fonts. The
first chapter, “History and Classifications”, is a unique chapter in this book, as it discusses
computers very little but deals mainly with the history of printing, especially the history
of Latin typographic characters. We have seen that for designing high-quality fonts it
is not enough to have good tools: a certain knowledge of the history of the fonts that
surround us is also essential. Even in the history presented here, however, the point of
view is that of the user of digital fonts. Thus most of the examples provided were produced with digital fonts rather than from reproductions of specimens of printing from an
earlier era. We also frequently compare the original specimens with digital fonts created
by a variety of designers.
Chapter 11 goes beyond history. It continues with a description of three methods for
classifying fonts. The first two (Vox and Alessandrini) finish offthe history, in a way,
and recapitulate it. The Vox classification gives us a jargon for describing fonts (garalde,
didone, etc.) that every professional in the fields of graphic design and publishing must
know. The scheme of Alessandrini should be considered a critique (with a heaping helping of humor) of Vox’s; we couldn’t resist the pleasure of presenting it here.
The third classification scheme is quite different and serves as a link between this chapter
and the rest of the book. It is Panose-1, a mathematical description of the properties
of glyphs. Each font is characterized by a sequence of 10 numbers, which correspond
to 10 practically independent properties. Both Windows and the Cascading Style Sheets
standard make use of this classification system to select substitute fonts by choosing the
available font whose Panose-1 distance from the missing font is the smallest. Despite the
fame of the Panose-1 system, a precise description of it is very difficult to find. This book
provides one, thanks to the generosity of Benjamin Bauermeister, the creator of Panose1, who was kind enough to supply us with the necessary information.
```

```text
The Structure of the Book and Ways to Use It
Chapters 12 to 14 describe the existing tools for creating (or modifying) fonts. We have
chosen two basic tools, FontLab and FontForge (formerly PfaEdit), and we describe their
most important capabilities in this chapter. There are three chapters instead of only
one because we have broken the font-creation process into three steps: drawing glyphs,
optimizing the rendering, and supplementing the font with “advanced typographic”
properties. Optimization of the rendering involves adding the PostScript hints or TrueType instructions needed to make the rendering optimal at all body sizes. In this chapter,
we also describe a third tool that is used specifically for instructing fonts: Microsoft’s
Visual TrueType. Since the hinting and instructing of fonts are reputed to be arcane
and poorly documented techniques, we have tried to compensate by devoting an entire
chapter to them, complete with many real-world examples. In addition, Appendix E is
devoted to the description of the TrueType assembly language for instructing fonts; it
is the ideal companion to Chapter 13, which is concerned more with the tools used for
instructing than with the instructions themselves.
Chapter 14 discusses the big new development of recent years, OpenType properties.
Adobe and Microsoft, the companies that have supported this technology, had two purposes in mind: Latin fonts “of typographic quality” (i.e., replete with such gadgets as
ligatures, variant glyphs, glyphs for the languages of Central Europe, etc.) and specific
non-Latin fonts (with contextual analysis, ligature processing, etc.). High-quality Latin
fonts make use of the “advanced typographic features”. Right now several foundries are
converting their arsenals of PostScript or TrueType fonts into OpenType fonts with advanced properties, and the tools FontLab and FontForge lend themselves admirably to
the task, to which we have devoted the first part of the chapter. Along the way, we also
describe a third tool dedicated to this task: VOLT, by Microsoft.
The second part of the chapter is devoted to OpenType’s competitor, the AAT fonts (formerly called TrueType GX). These fonts are considered by some to be more powerful
than OpenType fonts, but they suffer from a lack of tools, poor documentation, and,
what is worse, a boycott by the major desktop publishing systems (Adobe Creative Suite,
Quark XPress, etc.). But these problems may prove to be only temporary, and we felt that
AAT deserved to be mentioned here along with OpenType. In this chapter, the reader
will learn how to equip TrueType fonts with AAT tables by using the only tool that is
able to do the job: FontForge.
Finally, we include in this unit Appendix F, “METAFONT and Its Derivatives”. METAFONT is a programming language dedicated to font creation, the work of the same person
who created TEX, the famous computer scientist Donald Knuth of Stanford University.
METAFONT is a very powerful tool full of good ideas. The reason that we have not
included it in the main part of the book is that it has become obsolete, in a way, by
virtue of its incompatibility with the notion of the electronic document. Specifically,
METAFONT creates bitmap fonts without a trace of the characters to which the glyphs
correspond; thus they cannot be used in electronic documents, as the link between glyph
and character is broken. Furthermore, these bitmap fonts depend on the characteristics
of a given printer; thus there can be no “universal” METAFONT font that is compatible
with every printer—whereas PostScript and TrueType fonts are based on that principle of
universality. Nonetheless, we have described METAFONT in this book for three reasons:
```

Introduction for nostalgia and out of respect for Donald Knuth, for METAFONT’s intrinsic value as a tool for designing fonts, and, finally, because some recent software attempts to make up for the shortcomings of METAFONT by generating PostScript or TrueType fonts from the same source code used for METAFONT or from a similar type of source. We describe two attempts of this kind: METATYPE1 and MetaFog. Without a doubt, this book distinguishes itself by the uncommonly large size of its appendices. We have aimed to compile and present the main font formats in our own way—an undertaking that has consumed a great deal of time and energy, not to mention pages. Appendix A can be considered a sort of history of font formats, as it discusses a type of fonts—bitmap fonts—that has virtually disappeared. Appendix B discusses the “real” and virtual fonts of TEX. Appendix C aims to discuss all of the PostScript font formats, from Type 1 (released in 1985) to CFF, which is a part of the OpenType standard, with a brief mention of the obsolete formats (Type 3 and Multiple Masters) and the special formats for Far Eastern scripts. So that we can understand the PostScript code for these fonts, we have also provided an introduction to this very specialized programming language. In Appendix D, we take on the challenge of describing in detail all the TrueType, OpenType, and AAT tables. So as not to bore the reader with low-level technical details on the numbers of bytes in each field, the pointers between the tables, the number of bytes of padding—in short, the horror of editing raw binary data—we describe these tables in an XML syntax used by the tool TTX. This tool, developed in Python by Just van Rossum, the brother of Guido van Rossum (who invented Python), makes it possible to convert TrueType, OpenType, and AAT binary data into XML and vice versa. Thus we can consider the TTX representation of these fonts to be equivalent to their binary form, and we shall take advantage of this convenience to describe the tables as XML structures. That approach will not make their complexity disappear as if by waving a magic wand, but it will at least spare the reader needless complexity that pertains only to aspects of the binary format of the files themselves. Thus we shall be able to focus on the essence of each table. We shall systematically illustrate the definition of the tables by means of practical examples. This appendix will be of interest to more people than just computer scientists. Large consumers of OpenType fonts will also find it valuable for the simple reason that current software products that are compatible with the OpenType font format use only a tiny percentage of its possibilities. Readers eager to know what OpenType has under the hood will find out in this appendix. Appendix E is the logical continuation of Appendix D and the ideal complement to Chapter 13 on optimizing the rendering of fonts. In it, we describe the instructions of the TrueType assembly language. TrueType instructions have a reputation for being arcane and incomprehensible—a reputation due as much to their representation (in assembly language) as to their purpose (modifying the outline of a glyph to obtain a better rendering) and to some implied concepts (notably the concepts of projection vector, freedom

```text
The Structure of the Book and Ways to Use It
vector, twilight zones, etc.). And it is due most of all to the poor quality of the documentation supplied by Microsoft, which is enough to discourage even the most motivated
programmer. We hope that this appendix will be easier to understand than the document that it cites and that it will be a helpful adjunct to Chapter 13.
We close with a brief introduction to Bézier curves, which are used again and again in
the text (in discussions of font creation, the description of the PostScript and METAFONT
languages, etc.). We have mentioned that most books on these languages give very little
information on Bézier curves, often no more than the formula for the Bézier polynomial
and a few properties. To compensate for the deficiency, we offer a genuine mathematical
presentation of these objects, which today are indispensable for the description of fonts.
The reader will find in this section the most important theorems and lemmas concerning
these mathematical objects, with proofs to follow in due course.
The book ends with a bibliography that includes as many URLs as possible so that the
reader can read the original documents or order copies of them. It also includes two
indexes: the general index, for terms, and an index of names, which includes creators
of software, font designers, and all other people mentioned for one reason or another.
How to Read This Book
This book contains introductions to certain technologies, “user’s manuals” for software,
technical specifications, and even histories of fonts and encodings. It plays the dual role
of textbook and reference manual. To help the reader derive the greatest benefit from it,
we offer the following profiles of potential readers and, for each of these, a corresponding sequence of readings that we deem appropriate. Of course, these sequences are only
recommendations, and the best approach to the book is always the one that the reader
discovers on his own.
For the well-versed user of Unicode
The most interesting chapters will, of course, be Chapters 1 to 5. In order to use Unicode,
a user needs suitable fonts. Once she has tracked them down on the Web, she will want to
install them; thus reading Chapter 6, 7, or 8 (according to her operating system) may be
of great benefit. And if she needs glyphs to represent characters not found in the fonts,
she may wish to add them herself. Then she becomes a font designer/editor. (See “For
the novice font designer”, below.)
For the devoted TEXist
Chapter 9 will be ideal. While reading it, he may wish to try his hand at input or output.
For the former, he will want to prepare documents in Unicode and typeset them with
Ω; therefore, we advise him to read the chapters on Unicode as well. For the latter, he
may want to create fonts for use with TEX; thus he may benefit from Chapters 12 and 14,
which discuss the creation of PostScript and TrueType fonts, or perhaps Appendix F, on
the use of METAFONT.
```

```text
Introduction
For the reader who simply wants to produce beautiful documents
A beautiful document is, first and foremost, a well-coded document; it is useful, therefore, to know the workings of Unicode in order to use it to greatest advantage. Reading
Chapters 2, 3, and 5 (and perhaps skimming over Chapter 4) is recommended. Next,
a beautiful document must employ beautiful fonts. After reading the history of fonts
(Chapter 11), the reader will be more capable of choosing fonts appropriate to a given
document. Once she has found them, she will need to install them; to that end, she
should read Chapter 6, 7, or 8, according to the operating system. Finally, to create
a beautiful document, one needs high-quality typesetting software. If, by chance, the
reader has chosen TEX (or Ω) to produce her document, reading Chapter 9 is a must.
For the reader who wishes to create beautiful Web pages
The sequence given in the preceding profile is recommended, with the difference that
the last chapter should instead be Chapter 10, which discusses the Web.
For the typophile or collector of fonts
Chapter 11 will delight the reader with its wealth of examples, including some rather
uncommon ones. But the true collector does not merely buy treasures and put them
on a shelf. He spends his time living with them, adoring them, studying them, keeping
them in good condition. The same goes for fonts, and font design/editing software is also
excellent for getting to know a font better, studying it in all of its detail, and perhaps improving it, supplementing it, correcting its kerning pairs, etc. The reader will thus do well
to read Chapter 12 carefully, and Chapters 13 and 14 as well. If technical problems arise,
Appendices C and D will enable him to find a solution. Finally, to share his collection
of fonts with his fellow connoisseurs, there is nothing like a beautiful Web page under
GlyphGate to show the cherished glyphs to every visitor, without compromising security.
Chapter 10 provides the necessary details.
For the novice font designer
Reading Chapter 11 may encourage her further and help her to find her place on the historic continuum of font design. This book does not give lessons in the graphical design of
fonts, but it does describe the needed tools in great detail. Read Chapter 12 very carefully
and then, before distributing the fonts you have created, read Chapters 13 and 14 to learn
how to improve them even more.
For the experienced font designer
Chapters 11 and 12 will not be very instructive. In Chapters 13 and 14, however, he
will find useful techniques for getting the most out of his beautiful font designs. He
may also enjoy sampling the delights of METAFONT and creating PostScript fonts with
METATYPE1 that would be very difficult or impossible to produce with a manual tool
such as FontLab or FontForge. If he is a user of FontLab, he may also try his hand at the
Python language and learn in Chapter 11 how to control the FontLab software through
programming. If he already knows font design, instruction, and advanced typographical
features, Appendices C and D will show him some of OpenType’s possibilities that will
```

How to Contact Us surprise him because, for the time being, they are not exploited by OpenType-compatible software. Finally, reading the description of the Panose standard in Chapter 11 will enable him to classify his fonts correctly and thus facilitate their use. For the developer of applications Chapters 2 to 4 will teach her what she needs to know to make her applications compatible with Unicode. Next, Appendices C, D, and E will show her how to make them compatible with PostScript or OpenType fonts. Appendix G may prove useful in the writing of algorithms that make calculations from the Bézier curves that describe the outlines of glyphs. For the reader who doesn’t match any of the preceding profiles The outline presented in this introduction, together with the table of contents, may suggest a path to the information that interests him. If this information is very specific, the index may also come in handy. If necessary, the reader may also contact us at the address given below. How to Contact Us We have done our best to reread and verify all the information in this book, but we may nonetheless have failed to catch some errors in the course of production.3 Please point out any errors that you notice and share with us your suggestions for future editions of this book by writing to: O’Reilly Media Inc. 1005 Gravenstein Highway North Sebastopol, CA 95472 You may also send us email. To join our mailing list or request a catalog, send a message to: info@oreilly.com To ask a technical question or send us your comments on the book, write to: somebody@oreilly.com This book has its own web site, where you will find all the code fragments that appear in the book, a list of errata, and plans for future editions. Please visit the following URL: http://www.oreilly.com/somewhere/fonts-and-encodings.html For more information on this book and its author, visit O’Reilly’s web site: http://www.oreilly.com 3 On this subject, we recommend a hilarious book: An Embarrassment of Misprints: Comical and Disastrous Typos of the Centuries, by Max Hall (1995) [154].

Before Unicode
When we need precise definitions of computer-related concepts that seem a little fuzzy
to us, nothing is more refreshing and beneficial than consulting old documents. For example, in C.E. MacKenzie’s Coded Character Sets, History and Development (1980) [242], we
find the following definitions (slightly condensed here):
• a bit is a binary digit, either 0 or 1;
• a bit pattern is an ordered set of bits, usually of fixed length;
• a byte is a bit pattern of fixed length; thus we speak of 8-bit bytes, 6-bit bytes, and so
on;
• a graphic is a particular shape, printed, typed, or displayed, that represents an alphabetic, numeric or special symbol;
• a character is a specific bit pattern and a meaning assigned to it: a graphic character has
an assigned graphic meaning, and a control character has an assigned control meaning;
• a bit code is a specific set of bit patterns to which either graphic or control meanings
have been asigned;
• a code table is a compact matrix form of rows and columns for exhibiting the bit
patterns and assigned meanings of a code;
• a shifted code is a code in which the meaning of a bit pattern depends not only on the
bit pattern itself, but also on the fact that it has been preceded in the data stream by
some other particular bit pattern, which is called a shift character.

All this makes sense; only the terminology has slightly changed. Nowadays a byte is always considered to be of fixed length 8; what MacKenzie calls a “graphic” is now called a
glyph; a “bit code” is called an encoding; and a “code table” is simply a way of graphically
representing the encoding. In the old days, the position of a character in the encoding
was given by a double number: “x/y”, where x is the column number and y the row number. Nowadays we simply give its number in decimal or hexadecimal form. “Shifted”
encodings tend to become extinct because they are incompatible with human–user interaction such as copying and pasting, but at that time GUIs were still well-protected
experiments in the Palo Alto Xerox Lab.
Let us go even further back in time. It seems that the first people to invent a code-based
system for long-distance transmission of information were the Greeks: around 350 bc,
as related by the historian Polybius [183], the general Aeneas employed a two-by-five
system of torches placed on two walls to encode the Greek alphabet, an alphabet of
24 letters that could be adequately encoded by the 25 = 32 combinations of five lighted or
extinguished torches. At the end of the 18th century, the French engineer Claude Chappe
established the first telegraphic link between Paris and Lille by using semaphores visible
at distances of 10 to 15 kilometers. In 1837, Samuel Morse invented “Morse code” for
the electric telegraph, a code that was more complex because it used a variable number
of long and short pulses (dahs and dits) for each letter, with the letters being obligatorily
separated by pauses. Thus there were two basic units: dahs and dits. It was the first internationally recognized system of encoding.
In 1874, Émile Baudot took up a code invented by Sir Francis Bacon in 1605 and adapted
it to the telegraph. Unlike Morse’s code, the Baudot code used codes of five symbols that
were typed on a device bearing five keys like those of a piano. Each key was connected
to a cable that transmitted signals. The reader will find a detailed description of Baudot’s
code and keyboard in [201].
The first important encoding of the twentieth century was CCITT #2, a 58-character
shifted 5-bit code, standardized as an international telegraph code in 1931 by CCITT
(“Comité Consultatif International Télégraphique et Téléphonique”). Being shifted, it
used two “modes”, also called “cases”. The first is the letter case:
T 01
cr 02
O 03
sp 04
H 05
N 06
M 07
lf 08
L 09
R 0A
G 0B
I 0C
P 0D
C 0E
V 0F
E
Z
D
B
S
Y
F
X
A
W
J
1A
fs
1B
U
1C
Q
1D
K
1E
ls
1F
Here “lf” is the carriage return, “sp” is the blank space, “lf” is the line feed, and “ls”
(letter shift) and “fs” (figure shift) are two escape codes. “fs” shifts to figure case:
5 01
cr 02
9 03
sp 04 ***05
,
.
lf 08
) 09
4 0A ***0B
8 0C
0 0D
:
0E
;
0F
3 10
+ 11
ab 12
? 13
’
6 15 ***16
/
-
2 19
bel1A
fs 1B
7 1C
1 1D
( 1E
ls 1F
Here “***” is intended for national use (#, \$, and & in the US; Ä Ö Ü in Germany, Sweden
and Finland; Æ Ø Å in Denmark and Norway), “ab” is used for answering back, and
“bel” rings a bell. With “ls” we return to the first version of the encoding. This use of two

FIELDATA
states seems awkward to us today; after all, why not just use a sixth bit? One consequence
of this approach is that the interpretation of a position within the encoding depends on
context—whether we are in “letter” or “figure” case.
In the prehistoric era of computers (the 1930s to the 1960s), only a few brilliant visionaries, such as Alan Turing and Vannevar Bush, imagined that the computer would one
day come to use letters. To everyone else, it was just a calculating machine and therefore
was good only for processing numbers.
FIELDATA
FIELDATA was a 7-bit encoding developed by the US Army for use on military data
communication lines. It became a US military standard in 1960:
ms 40
uc 41
lc 42
lf 43
cr 44
sp 45
A 46
B 47
C 48
D 49
E 4A
F 4B
G 4C
H 4D
I 4E
J 4F
K
L
M
N
O
P
Q
R
S
T
U
5A
V
5B
W
5C
X
5D
Y
5E
Z
5F
) 60
-
+ 62
< 63
= 64
> 65
_ 66
\$ 67
* 68
( 69
" 6A
:
6B
? 6C
! 6D
,
6E stop6F
’
7A
;
7B
/
7C
.
7D spec
7E idle
7F
“ms” stands for “master space”; “uc/lc” are shift codes for uppercase and lowercase letters; “stop”, “spec”, and “idle” stand for “stop”, “special”, and “idle”. In this encoding we
already find most of the characters used a few years later in ASCII. FIELDATA survives
even today as the internal encoding of certain COBOL software.
ASCII
Towards the end of the 1950s, the telecommunications industry redoubled its efforts to
develop a standard encoding. IBM and AT&T were among the large corporations that
drove the ASA (American Standards Association) to define an encoding. Thus ASCII1963, a preliminary version of ASCII with no lower-case letters, was born on June 17,
1963, a few months after the assassination of President Kennedy.
ASCII was updated in 1967. From that time on, it would include lower-case letters. Here
is ASCII-1967:
nul00 soh01
stx02
etx03
eot04 enq05 ack06
bel07
bs 08
ht 09
lf 0A
vt 0B
ff 0C
cr 0D
so 0E
si 0F
dle10 dc111 dc212 dc313 dc414 nak15
syn16
etb17 can18
em19
sub1A
esc1B
fs 1C
gs 1D
rs 1E
us 1F
sp 20
! 21
" 22
# 23
\$ 24
% 25
& 26
'
( 28
) 29
* 2A
+ 2B
,
2C
-
2D
.
2E
/
2F
0 30
1 31
2 32
3 33
4 34
5 35
6 36
7 37
8 38
9 39
:
3A
;
3B
< 3C
= 3D
> 3E
? 3F
@ 40
A 41
B 42
C 43
D 44
E 45
F 46
G 47
H 48
I 49
J 4A
K 4B
L 4C
M 4D
N 4E
O 4F
P 50
Q 51
R 52
S 53
T 54
U 55
V 56
W57
X 58
Y 59
Z 5A
[ 5B
\
5C
] 5D
^ 5E
_ 5F

` 60
a 61
b 62
c 63
d 64
e 65
f 66
g 67
h 68
i
j
6A
k 6B
l
6C
m 6D
n 6E
o 6F
p
q
r
s
t
u
v
w
x
y
z
7A
{
7B
|
7C
}
7D
˜
7E
del
7F
The first thirty-two positions in this encoding are occupied by control codes:
• formatting control codes: cr (carriage return), lf (line feed), bs (backspace), ht (horizontal tab), vt (vertical tab), sp (blank space), ff (form feed);
• extension codes: esc (escape is a shift but modifies only the following character), so
(shift out), si (shift in);
• controls for communications: soh (start of heading), stx (start of text), etx (end of
text), eot (end of transmission), etb (end of transmission block), ack (acknowledge),
nak (negative acknowledge), syn (synchronous idle), nul (null), dle (data link escape);
• device control functions dc1, ... , dc4;
• functions for error management: can (cancel), sub (substitute), del (delete), bel
(bell).
Of the characters that do not represent controls, a few call for some explanation:
• The backslash ‘\’, used by DOS as a delimiter for directory paths and by TEX as the
escape character for commands, was introduced into encodings in September 1961
and subsequently accepted into ASCII-1963 at the suggestion of Bob Bemer [72]. A
great fan of the ALGOL language, Bemer wanted to obtain the logical operators and
(∧) and or (∨). Since the forward slash was already present in the encoding, he was
able to obtain these two operators by simply concatenating a forward slash and a
backslash (‘/\’) and vice versa (‘\/’).
• The apostrophe is represented by a vertical stroke, ‘'’, not by a raised comma, ‘”, as
printers have represented it for centuries. Today we call this type of apostrophe a
“non-oriented apostrophe”. Although it has a peculiar shape, it is perfectly suitable
for those programming languages that use it as the opening and closing delimiter for
strings.
• The same goes for the “double quote” or “non-oriented quotation marks”, ‘"’: they
served as the opening and closing American-style quotation marks, and even as the
diæresis; thus this symbol, too, had to be symmetrical.
• The grave accent ‘`’ also serves as an American-style opening quotation mark.
• The vertical bar ‘|’ was introduced to represent the or operator in the language PL/I
[226].

EBCDIC
It may seem unbelievable today, but a not insignificant number of ASCII characters
could vary according to local needs: the number sign ‘#’, the dollar sign ‘\$’, the at sign
‘@’, the square brackets ‘[’ and ‘]’, the backslash ‘\’, the caret ‘^’, the grave accent ‘`’, the
curly braces ‘{’ and ‘}’, the vertical bar ‘|’, and the tilde ‘˜’.
Thus, at one time, France used the NF Z62010 standard and the United Kingdom used
the BS 4730 standard, both of which replaced the number sign by the symbol for pounds
sterling ‘£’; Japan used the JIS C-6220 standard, which employed a yen sign ‘¥’ in the place
of the backslash; the Soviet Union used the GOST 13052 standard, which substituted a
universal currency sign ‘´’ for the dollar sign, etc. The reader will find a complete list of
these “localized ASCII encodings” in [248, p. 243]. To distinguish it from the localized
versions, the original version of ASCII was called IRV (International Reference Version).
Another problem with the ASCII encoding is that it offered a rather naïve and æsthetically unacceptable method for placing accents on letters: to obtain an ‘é’, one was asked to
type the sequence ‘e bs '’, that is: ‘letter e’, ‘backspace’, ‘apostrophe’. That is why the grave
and circumflex accents and the tilde, represented as spacing characters, are found in the
encoding. To obtain a diæresis, one used the backspace followed by a double quote; and
underscoring words was accomplished with backspaces followed by underscores.
The ASCII-1967 encoding became the ISO 646 standard in 1983. Its latest revision, published by ECMA [192], dates to 1991.
EBCDIC
While the computer giant IBM had taken part in the development of ASCII-1963, it released in 1964 a new and highly appreciated line of computers, IBM System/360, whose
low-end model came equipped with 24 kb (!) of memory. The development of these
machines was the second most expensive industrial project of the 1960s, after NASA’s
Apollo program....
The System/360 computers use the EBCDIC encoding (Extended Binary Coded Decimal
Interchange Code, pronounced “eb-cee-dic”), an 8-bit encoding in which many positions
are left empty and in which the letters of the alphabet are not always contiguous:
nul00 soh01
stx02
etx03
pf 04
ht 05
lc 06
del07
ge 08
rlf09 smm0A
vt 0B
ff 0C
cr 0D
so 0E
si 0F
dle10 dc111 dc212
tm13
res14
nl 15
bs 16
il 17 can18
em19
cc 1A
cui1B
ifs1C
igs1D
irs1E
ius1F
ds 20
sos21
fs 22
byp24
lf 25
etb26
esc27
sm 2A cu22B
2C enq2D
ack2E
bel2F
syn32
pn 34
rs 35
uc 36
eot37
3A cu33B dc43C nak3D
3E
sub3F
sp 40
¢ 4A
.
4B
< 4C
( 4D
+ 4E
|
4F
& 50
! 5A
\$ 5B
* 5C
) 5D
;
5E
¬ 5F
-
/
¦
6A
,
6B
% 6C
_ 6D
> 6E
? 6F
‘
:
7A
# 7B
@ 7C
’
7D
= 7E
" 7F

a 81
b 82
c 83
d 84
e 85
f 86
g 87
h 88
i
8A
8B
8C
8D
8E
8F
j
k
l
m
n
o
p
q
r
9A
9B
9C
9D
9E
9F
A0
˜ A1
s A2
t A3
u A4
v A5
w A6
x A7
y A8
z A9
AA
AB
AC
AD
AE
AF
{
C0
A
C1
B
C2
C
C3
D
C4
E
C5
F
C6
G
C7
H
C8
I
C9
CA
CB
π
CC
CD
∫
CE
CF
} D0
J D1
K D2
L D3
M D4
N D5
O D6
P D7
Q D8
R D9
DA
DB
DC
DD
DE
DF
\
E0
E1
S
E2
T
E3
U
E4
V
E5
W
E6
X
E7
Y
E8
Z
E9
EA
EB
ª
EC
ED
EE
EF
0 F0
1 F1
2 F2
3 F3
4 F4
5 F5
6 F6
7 F7
8 F8
9 F9
|
FA
FB
FC
FD
FE
eo FF
We may well ask: why are the letters of the alphabet distributed in so bizarre a manner
in this encoding? Why did IBM insist so firmly on its EBCDIC encoding? To understand
what happened, we need a bit of historical background.
In 1801 the Parisian weaver Joseph-Marie Jacquard used strings of punched cards to operate his looms, thus perfecting an invention by Basile Bouchon that dated to 1725.
Seventy-nine years later, on the other side of the Atlantic, a census conducted in the
United States was ruined. The failure resulted from the fact that it took 7 years (!) to
process the data on the country’s 31.8 million residents—so much time that the data were
no longer up to date. Faced with this situation, the Census Bureau organized a contest
to find an invention that could solve the problem. A certain Herman Hollerith won the
contest with a system inspired by that of Jacquard: the census-takers would carry cards
that they would punch according to the profile of the person being surveyed. Later a
machine, the ancestor of the computer, would read the cards and compile the results.
In 1890 a new census was taken. While the previous census collected only six pieces of
information for each person, this time plans were made for 245! The Bureau sent 50,000
employees all over America to conduct the census. And, as had been expected, the results
were spectacular: the data were completely processed in less than six weeks. Hollerith had
thus succeeded in processing 40 times as much information in 1/56 of the time....
Encouraged by this astounding success, Hollerith founded a company named TMC (Tabulating Machine Company). In 1924 it became International Business Machines, or IBM.
But what relationship is there between Hollerith and EBCDIC? In Figure 1-1, the reader
can see a remnant of the past: an ISO 1681 card punched by the author at the University of Lille (France) in September 1983, a few months before this medium disappeared
from that university. Punch cards were the user’s means of interacting with the computer
before the advent of terminals with screens and keyboards. Note that punch cards have
twelve rows, of which two are “unlabeled” (we call them “X” and “Y”) and the remaining
ten bear the digits from “0” to “9”. Since there are twelve potential holes, can we therefore encode numbers with 212 = 4,096 bits in a single column on the card? Alas, no.
In fact, Hollerith quickly noticed that punch cards could not be punched excessively,
lest they be torn. Therefore he invented a system by which one could encode letters and
numbers without ever using more than two holes per column. The system is called the
Hollerith code:

::: tip Typographical Specimen Plate (Figure 1-1)
![Figure 1-1: An ISO 1681 80-column punch card](/images/fonts-encodings/fig1-1-punch-card-iso-1681.png)
*Figure 1-1: An ISO 1681 80-column punch card.*
:::

![Figure 1-1: An ISO 1681 80-column punch card](/images/fonts-encodings/fig1-1-punch-card-iso-1681.png)
*Figure 1-1: An ISO 1681 80-column punch card.*

```text
ISO 2022
Figure 1-1: A punch card (ISO 1681 standard).
Holes
with X punched
A
B
C
D
E
F
G
H
I
with Y punched
J
K
L
M
N
O
P
Q
R
with 0 punched
S
T
U
V
W
X
Y
Z
neither X nor Y punched
In other words, to obtain an ‘A’, one punches row “X” and row “1”; to obtain a ‘Z’, one
punches row “0” and row “9”; to obtain a digit, one punches only one hole—the one
corresponding to that digit.
The reader will readily recognize the last four lines of the EBCDIC encoding. How could
IBM have ever abandoned the code created by its legendary founder?
Despite the awkwardness of this encoding, IBM spread it to the four corners of the earth.
The company created 57 national versions of EBCDIC. All of them suffer from the same
problem: they lack certain ASCII characters, such as the square brackets, that are indispensable for computer programming.
Extremely rare today, the EBCDIC encoding is nonetheless very much alive. As recently
as 1997, an article appeared in Perl Journal on the use of Perl 5 in an EBCDIC environment under IBM System/390 [298].
ISO 2022
In the early 1970s, the industry was well aware of the fact that the “localized” versions of
ASCII were an impediment. People had to use multiple encodings that were really quite
different, and sooner or later they had to switch from one encoding to another in the
middle of a document or a transmission. But how to indicate this change of encoding?
```

0x
1x
2x
3x
4x
5x
6x
7x
8x
9x
Ax
Bx
Cx
Dx
Ex
Fx
x0
x1
x2
x3
x4
x5
x6
x7
x8
x9
xA
xB
xC
xD
xE
xF
C0
C1
GL
GR
Figure 1-2: The manner in which ISO 2022 subdivides the 8-bit table.
It was for this reason that the ISO 2022 standard emerged, in 1973. Its latest revision
dates to 1994 [193]. It is not an encoding but a definition of a certain number of escape
sequences that make it possible to use as many as four distinct encodings within the same
set of data.
ISO 2022 starts from the principle that the 256 squares in a table of 8 bits are distributed
among four zones, which can be seen in Figure 1-2. Zones C0 and C1 are reserved for
control characters, and zones GL (“L” for “left”) and GR (“R” for “right”) are reserved
for what today are known as alphanumeric characters (and what at the time bore the
oxymoronic name “graphic characters”, whence the ‘G’).
Thus we have up to four distinct encodings at our disposal. Let us call them G0, G1,
G2, G3. These encodings may be of any of four types:
• Encodings with 94 positions: 6 columns with 16 positions each, minus the two excluded positions, namely the first and the last.
• Encodings with 96 positions: 6 columns with 16 positions each.
• Encodings with 94n positions, if we use n bytes to encode a single character. Thus for
ideographic languages we will take n = 2, and we will therefore have encodings of
942 = 8,836 positions.
• Encodings with 96n positions, if we use n bytes to encode a single character. By taking
n = 2, we will obtain encodings with 962 = 9,216 positions.
There is only one small constraint: encoding G0 must necessarily be of type 94 or 94n.
A first series of escape sequences allows us to specify encodings G0, G1, G2, G3. These sequences depend on the type of the encoding. Thus, for example, the sequences ‘esc 0x2D

::: tip Typographical Specimen Plate (Figure 1-2)
![Figure 1-2: Subdivisions of an 8-bit space in ISO 2022](/images/fonts-encodings/fig1-2-iso-2022-subdivisions.png)
*Figure 1-2: Subdivisions of an 8-bit space in ISO 2022.*
:::

![Figure 1-2: Subdivisions of an 8-bit space in ISO 2022](/images/fonts-encodings/fig1-2-iso-2022-subdivisions.png)
*Figure 1-2: Subdivisions of an 8-bit space in ISO 2022.*

```text
ISO 8859
F’, ‘esc 0x2E F’, ‘esc 0x2F F’, in which ‘F’ is an identifier for an encoding with 96 positions,
declares that the encoding designated by ‘F’ is assigned to G1, G2, or G3, respectively.
To identify the encoding, we use identifiers defined by the “competent authority”, which
today is the Information Processing Society of Japan [196]. The IPSJ’s Web site provides
a list of encodings.1 There we can discover, for example, that the ISO 8859-1 encoding
that we shall discuss below is registered under the number 100 and has the identifier
“4/1”, an old-fashioned way to represent the hexademical number 0x41. It is an encoding
with 96 positions; therefore, it cannot be assigned to G0. The escape sequences ‘esc 0x2D
0x41’, ‘esc 0x2E 0x41’, and ‘esc 0x2F 0x41’ will therefore serve to declare ISO 8859-1 as
encoding G1, G2, or G3.
Once the Gn have been defined, we can use them. There are escape sequences that switch
the active encoding until further notice. To do so, they must implement a finite automaton. These sequences consist either of ASCII control characters (so and si assign
G0 and G1 to zone GL) or of pairs of bytes beginning with esc: thus ‘esc 0x7E’ will select
G1 for zone GR, ‘esc 0x6F’ will select G3 for zone GL, etc.
There are also control characters for zone C1 that affect only the following character:
ss2 (0x8E) and ss3 (0x8F) specify that only the following character should be interpreted
as being in encoding G2 or G3, respectively. The idea is that G2 and G3 may be rare
encodings from which we draw only isolated characters now and then; it therefore makes
more sense to “flag” them individually.
ISO 2022 is based on the principle of total freedom to define new encodings. Indeed,
all that it takes to make an encoding an integral part of ISO 2022 is to register it with
the competent authority. And there are so many registered encodings today that it is
practically impossible for a computer developer to support all of them. The only viable alternative is to limit oneself to a small number of recognized and widely used
encodings—the ISO 2022-* instances that Ken Lunde has described [240, p. 147].
Thus we have, for example, ISO 2022-JP (defined in RFC 1468), which is a combination
of ASCII, JIS-Roman (JIS X 0201-1976), JIS X 0208-1978, and JIS X 0208-1983 (taken,
respectively, as encodings G0, G1, G2, G3). This is how we resolve the problem of rare
ideographic characters: we put ASCII and the most common ideographic characters in
G0 and G1, and we reserve G2 and G3 for the rare cases, in which we select the required
characters individually.
ISO 8859
As soon as the ISO 2022 standard allowed multiple encodings to be combined in a single
data flow, ISO started to define encodings with 96 positions that would supplement
ASCII. This became the ISO 8859 family of encodings, a family characterized by its
longevity—and its awkwardness.
1 This Web site is a gold mine for historians of computer science, as it offers a PDF version of the description of each registered encoding!
```

ISO 8859-1 (Latin-1) and ISO 8859-15 (Latin-9)
The new standard’s flagship, ISO 8859-1, was launched in 1987. By 1990, Bernard Marti
had written [248, p. 257]: “Unfortunately, the haste with which this standard was established [... ] and its penetration into stand-alone systems have led to incoherence in the
definition of character sets.”
This flagship is dedicated to the languages of Western Europe. Here is part GR of the
standard (parts C0 and GL are identical to those of ASCII, and part C1 was not included
in the new standard):
nbspA0
¡ A1
¢ A2
£ A3
´ A4
¥ A5
¦
A6
§ A7
¨ A8
© A9
ª AA
« AB
¬ AC
shyAD
® AE
¯ AF
°
B0
±
B1
²
B2
³
B3
´
B4
μ
B5
¶
B6
·
B7
¸
B8
¹
B9
º
BA
»
BB
¼
BC
½
BD
¾
BE
¿
BF
À C0
Á C1
Â C2
Ã C3
Ä C4
Å C5
ÆC6
Ç C7
È C8
É C9
Ê CA
Ë CB
Ì CC
Í CD
Î CE
Ï CF
Ð
D0
Ñ
D1
Ò
D2
Ó
D3
Ô
D4
Õ
D5
Ö
D6
×
D7
Ø
D8
Ù
D9
Ú
DA
Û
DB
Ü
DC
Ý
DD
Þ
DE
ß
DF
à E0
á E1
â E2
ã E3
ä E4
å E5
æ E6
ç E7
è E8
é E9
ê EA
ë EB
ì
EC
í
ED
î
EE
ï
EF
ð
F0
ñ
F1
ò
F2
ó
F3
ô
F4
õ
F5
ö
F6
÷
F7
ø
F8
ù
F9
ú
FA
û
FB
ü
FC
ý
FD
þ
FE
ÿ
FF
Certain symbols deserve a few words of explanation:
• nbsp is the non-breaking space.
• ‘¡’ and ‘¿’ are the Spanish exclamation point and question mark used at the beginning of a sentence. Thanks to these characters, we avoid in Spanish the rather annoying experience of coming to the end of a sentence only to discover that it was a
question or an exclamation—and that we shall have to read the whole sentence over
again in order to give it the proper intonation.
• ‘¢’, ‘£’, and ‘¥’ are currency symbols: the cent sign, the British pound, and the Japanese
yen.
• ‘´’ is the “universal currency sign”. The Italians were the ones to propose this symbol
as a replacement for the dollar sign in certain localized and “politically correct” versions of ASCII. The author has never seen this symbol used in text and cannot even
imagine any use for it.
• ‘ª’ and ‘º’ are used in Spanish, Italian, and Portuguese for numerals (the first being
feminine and the second masculine): ‘1ª, ‘2º’, etc.
• shy, the “soft hyphen”, may be the least coherent character in the encoding. In
ISO 8859-1 it is described as a “hyphen resulting from a line break”, while in Unicode,
which ordinarily follows ISO 8859-1 to the letter, it is described as “an invisible
character whose purpose is to indicate potential line breaks”. The reader will find a
full discussion in [225].

ISO 8859
• Unless we use a font such as Futura in which the letter ‘o’ is a perfect circle, we
must not confuse the “degree sign °” (position 0xB0) with the “superscript o º” (position 0xBA). The first is a perfect circle, whereas the latter is a letter ‘o’ written small.
Thus we write “nº” but “37,2°C”.
• The “midpoint” ‘·’ is used to form the Catalan ligature ‘l·l’ [135];
• the German eszett ‘ß’ must not be mistaken for a beta. Historically, it comes from the
ligature “long s–round s”. Its upper-case version is ordinarily ‘SS’ but can also be ‘SZ’
to distinguish certain words. Thus, in German, MASSE is the uppercase version of
Masse (= mass), whereas MASZE is the one of Maße (= measures);
• the “y with diæresis” is used in Welsh and in Old French. We find it in Modern
French in place names such as “l’Haÿe-les-Roses”, surnames such as “de Croÿ” and
“Louÿ”, or expressions such as “kir à l’aÿ” [36]. This letter is extremely rare, and its
inclusion in ISO 8859-1 is peculiar at best.
But the biggest deficiency in ISO 8859-1 is the lack of certain characters:
• While ‘ÿ’ is extremely rare in French, the ligature ‘œ’ is not. It appears in many very
common French words (“cœur” ‘heart’, “œil” ‘eye’, etc.); in some other words—less
common ones, to be sure, but that is neither here nor there—it is not used: “moelle”
‘marrow’, “coefficient”, “coexistence”, “foehn”, etc. According to an urban legend, the
French delegate was out sick the day when the standard came up for a vote and had to
have his Belgian counterpart act as his proxy. In fact [36], the French delegate was an
engineer who was convinced that this ligature was useless, and the Swiss and German
representatives pressed hard to have the mathematical symbols ‘×’ and ‘÷’ included
at the positions where Œ and œ would logically appear.
• French is not the only language neglected by ISO 8859-1. Dutch has another ligature,
‘ij’ (which, in italics, looks dangerously close to a ‘ÿ’, a fact that has led to numerous
misunderstandings [161, note 4]). This ligature is just as important as the French
‘œ’—perhaps even more important, as it has acquired the status of a letter in certain
situations. Thus, in some Dutch encyclopædias, the entries are sorted according to
an order in which ‘ij’ appears between ‘w’ and ‘y’. The upper-case version of ‘ij’ is ‘IJ’,
as in the name of the city “IJmegen”.
• Finally, if only for reasons of consistency, there should also be a ‘Ÿ’, the upper-case
version of ‘ÿ’.
ISO 8859-1 is a very important encoding because:
• it has become the standard encoding for Unix;
• Unicode is an extension of it;
• at least in Western Europe, most Web browsers and electronic-mail software have
long used it as the default encoding when no encoding was specified.

The languages covered by ISO 8859-1 are Afrikaans, Albanian, Basque, Catalan (using the
midpoint to form the ligature ‘l·l’), Dutch (without the ligature ‘ij’), English, Faeroese,
Finnish, French (without the ligature ‘œ’ and without ‘Ÿ’), German, Icelandic, Italian,
Norwegian, Portuguese, Rhaeto-Romance, Scottish Gaelic, Spanish, and Swedish.
In March 1999, when the euro sign was added, ISO took advantage of the opportunity to
correct two other strategic errors: first, the free-standing accent marks were eliminated;
second, the ligatures ‘Œ’ and ‘œ’ and the letter ‘Ÿ’, needed for French but missing from
the encoding, were finally introduced; third, the letters “Ž ž Š š”, which are used in most
Central European languages and which can be useful in personal and place names, were
also added. After the fall of the Soviet Union, the euro sign took the place of the universal
monetary symbol.
The new standard was called ISO 8859-15 (or “Latin-9”). It differs from ISO 8859-1 in only
eight positions (shown in black in the following diagram):
nbsp
A0
¡
A1
¢
A2
£
A3
¤
A4
¥
A5
Š
A6
§
A7
š
A8
©
A9
ª
AA
«
AB
¬
AC
shy
AD
®
AE
¯
AF
° B0
± B1
² B2
³ B3
Ž B4
μ B5
¶ B6
·
B7
ž B8
¹ B9
º BA
» BB ŒBC
œ BD
Ÿ BE
¿ BF
ISO 8859-2 (Latin-2) and ISO 8859-16 (Latin-10)
After ISO 8859-1, which is also known as ISO Latin-1, three other encodings for the Latin
alphabet came out: one each for the countries of Eastern Europe (ISO 8859-2), Southern
Europe (ISO 8859-3), and Northern Europe (ISO 8859-4).
Thus ISO 8859-2 (or “Latin-2”) includes the characters needed for certain languages of
Central Europe: Bosnian, Croatian, Czech, Hungarian, Polish, Romanian (but with a
cedilla instead of a comma under the letters ‘¨’ and ‘≠’), Slovak, Slovenian, and Sorbian.
It also contains the characters needed for German (commercial influence at work) and
some of the characters needed for French (some accented capitals are missing):
nbsp
A0
˛
A
A1
˘
A2
Ł
A3
´
A4
L’
A5
A6
§
A7
¨
A8
Š
A9
¸S
AA
ˇT
AB
AC
shy
AD
Ž
AE
˙Z
AF
° B0
˛a B1
. B2
ł
B3
´ B4
l’ B5
6 B6
ˇ B7
¸ B8
š B9
¸s BA
t’ BB
9 BC
˝ BD
ž BE
˙z BF
C0
Á
C1
Â
C2
˘A
C3
Ä
C4
C5
/
C6
Ç
C7
ˇC
C8
É
C9
˛E
CA
Ë
CB
ˇE
CC
Í
CD
Î
CE
ˇD
CF
Ð D0
1 D1
ˇN D2
Ó D3
Ô D4
˝O D5
Ö D6
× D7
ˇR D8
˚U D9
Ú DA
< DB
Ü DC
Ý DD
¸T DE
ß DF
E0
á
E1
â
E2
˘a
E3
ä
E4
:
E5
E6
ç
E7
ˇc
E8
é
E9
˛e
EA
ë
EB
ˇe
EC
í
ED
î
EE
d’
EF
Æ F0
7 F1
ˇn F2
ó F3
ô F4
= F5
ö F6
÷ F7
ˇr F8
˚u F9
ú FA
> FB
ü FC
ý FD
¸t FE
˙ FF
A few characters may need some explanation:
• Do not confuse the breve ‘˘’ and the háˇcek ‘ˇ’: the former is round, the latter pointed.
• Do not confuse the cedilla ‘¸’ (which opens to the left) and the ogonek ‘.’, especially
because the cedilla was often written like an ogonek in Old French, where we find
the letter ‘˛e’.

ISO 8859
• Turkish uses the letter ‘s’ with a cedilla, but in Romanian the same letter, as well as
letter ‘t’, are written with a diacritical mark shaped like a comma: ‘¨’, ‘≠’. The ISO 88592 standard was not intended to cover Turkish, yet we can see in the description of
the characters that these letters are anomalously written with a cedilla rather than a
comma.
In 2001, after the release of ISO 8859-15, which added the euro sign to ISO 8859-1 and
corrected a number of other deficiencies in that encoding, ISO did the same for ISO 88592: ISO 8859-16 (or “Latin-10”), the latest encoding in the 8859 saga, covers the languages
of Central Europe (Polish, Czech, Slovenian, Slovak, Hungarian, Albanian, Romanian),
but also French (with the ‘œ’ ligature!), German, and Italian. The coverage of this encoding stopped at the French border and did not extend to Spanish (‘ñ’ is missing) or
Portuguese (there are no vowels with a tilde). It has the distinction of being the first
(better late than never!) to include the Romanian letters ‘¨’ and ‘≠’.
Here is the ISO 8859-16 encoding:
nbspA0
˛
A A1
˛a A2
Ł A3
¤ A4
„ A5
Š A6
§ A7
š A8
© A9
∑AA
« AB
3 AC
shyAD
9 AE
˙Z AF
°
B0
±
B1
ˇC
B2
ł
B3
Ž
B4
”
B5
¶
B6
·
B7
ž
B8
ˇc
B9
¨
BA
»
BB Œ
BC
œ
BD
Ÿ
BE
˙z
BF
À C0
Á C1
Â C2
˘A C3
Ä C4
/ C5
ÆC6
Ç C7
È C8
É C9
Ê CA
Ë CB
Ì CC
Í CD
Î CE
Ï CF
Ð
D0
D1
Ò
D2
Ó
D3
Ô
D4
;
D5
Ö
D6
D7
<
D8
Ù
D9
Ú
DA
Û
DB
Ü
DC
˛E
DD
∏
DE
ß
DF
à E0
á E1
â E2
˘a E3
ä E4
5 E5
æ E6
ç E7
è E8
é E9
ê EA
ë EB
ì
EC
í
ED
î
EE
ï
EF
Æ
F0
F1
ò
F2
ó
F3
ô
F4
=
F5
ö
F6
F7
>
F8
ù
F9
ú
FA
û
FB
ü
FC
˛e
FD
≠
FE
ÿ
FF
ISO 8859-3 (Latin-3) and ISO 8859-9 (Latin-5)
The third (ISO 8859-3, or ‘Latin-3’) in the series is dedicated to the languages of “the
South”: Turkish, Maltese, and Esperanto (the last of these not being particularly Southern). In it we find certain characters from ISO 8859-1 and ISO 8859-2 and also—
surprise!—a few empty blocks:
nbspA0
∞A1
˘ A2
£ A3
´ A4
A5
ˆH A6
§ A7
¨ A8
˙I A9
¸S AA
˘G AB
ˆJ AC
shyAD
AE
˙Z AF
°
B0
Ø
B1
²
B2
³
B3
´
B4
μ
B5
h
B6
·
B7
¸
B8
ı
B9
¸s
BA
˘g
BB
ˆj
BC
½
BD
BE
˙z
BF
À C0
Á C1
Â C2
C3
Ä C4
˙C C5
ˆC C6
Ç C7
È C8
É C9
Ê CA
Ë CB
Ì CC
Í CD
Î CE
Ï CF
D0
Ñ
D1
Ò
D2
Ó
D3
Ô
D4
˙G
D5
Ö
D6
×
D7
ˆG
D8
Ù
D9
Ú
DA
Û
DB
Ü
DC
˘U
DD
ˆS
DE
ß
DF
à E0
á E1
â E2
E3
ä E4
˙c E5
ˆc E6
ç E7
è E8
é E9
ê EA
ë EB
ì
EC
í
ED
î
EE
ï
EF
F0
ñ
F1
ò
F2
ó
F3
ô
F4
˙g
F5
ö
F6
÷
F7
ˆg
F8
ù
F9
ú
FA
û
FB
ü
FC
˘u
FD
ˆs
FE
˙
FF
In 1989 the Turks, dissatisfied with ISO 8859-3, asked for a slightly modified version of
ISO 8859-1 with the Turkish characters in place of the Icelandic ones. The result was

ISO 8859-9 (or “Latin-5”), which differs from ISO 8859-1 in only six positions (shown
in black below):
˘G D0
Ñ D1
Ò D2
Ó D3
Ô D4
Õ D5
Ö D6
× D7
Ø D8
Ù D9
Ú DA
Û DB
Ü DC
˙I DD
¸S DE
ß DF
˘g F0
ñ F1
ò F2
ó F3
ô F4
õ F5
ö F6
÷ F7
ø F8
ù F9
ú FA
û FB
ü FC
ı
FD
¸s FE
ÿ FF
ISO 8859-4 (Latin-4), ISO 8859-10 (Latin-6),
and ISO 8859-13 (Latin-7)
Encoding number 4 in the series (ISO 8859-4, or “Latin-4”) is dedicated to the languages
of “the North”. Since Danish, Swedish, Norwegian, Finnish, and Icelandic are already
covered by ISO 8859-1, “languages of the North” here refers to those of the Baltic countries: Lithuanian, Latvian, Estonian, and Lapp. Here is the encoding:
nbsp
A0
˛
A
A1
±
A2
R¸
A3
´
A4
˜I
A5
L¸
A6
§
A7
¨
A8
Š
A9
!
AA
≤
AB
¥
AC
shy
AD
Ž
AE
¯
AF
° B0
˛a B1
. B2
r¸ B3
´ B4
˜ı
B5
l¸ B6
ˇ B7
¸ B8
š B9
& BA
≥BB
μ BC
∂BD
ž BE
n BF
C0
Á
C1
Â
C2
Ã
C3
Ä
C4
Å
C5
Æ
C6
*
C7
ˇC
C8
É
C9
˛E
CA
Ë
CB
˙E
CC
Í
CD
Î
CE
"
CF
Ð D0
N¸ D1
# D2
K¸ D3
Ô D4
Õ D5
Ö D6
× D7
Ø D8
+ D9
Ú DA
Û DB
Ü DC
˜U DD
\$ DE
ß DF
%
E0
á
E1
â
E2
ã
E3
ä
E4
å
E5
æ
E6
,
E7
ˇc
E8
é
E9
˛e
EA
ë
EB
˙e
EC
í
ED
î
EE
'
EF
Æ F0
n¸ F1
( F2
k¸ F3
ô F4
õ F5
ö F6
÷ F7
ø F8
- F9
ú FA
û FB
ü FC
˜u FD
) FE
˙ FF
In 1992, a new encoding (ISO 8859-10, or “Latin-6”), much more rational than the previous one, was created for the Nordic languages. It also includes all of the characters
required to write Icelandic. One special feature: certain “customs” of the ISO 8859 encodings were abandoned; for example, the universal currency symbol, the free-standing
accent marks, and the mathematical signs are not included.
nbspA0
˛
A A1
! A2
≤A3
" A4
˜I A5
K¸ A6
§ A7
L¸ A8
Ð A9
Š AA
¥ AB
Ž AC
shyAD
\$ AE
∂AF
° B0
˛a B1
& B2
≥B3
'
B4
˜ı
B5
k¸ B6
·
B7
l¸ B8
Æ B9
š BA
μ BB
ž BC —BD
) BE
n BF
C0
Á C1
Â C2
Ã C3
Ä C4
Å C5
ÆC6
* C7
ˇC C8
É C9
˛E CA
Ë CB
˙E CC
Í CD
Î CE
Ï CF
Ð D0
N¸ D1
# D2
Ó D3
Ô D4
Õ D5
Ö D6
˜U D7
Ø D8
+ D9
Ú DA
Û DB
Ü DC
Ý DD
Þ DE
ß DF
% E0
á E1
â E2
ã E3
ä E4
å E5
æ E6
,
E7
ˇc E8
é E9
˛e EA
ë EB
˙e EC
í
ED
î
EE
ï
EF
ð
F0
n¸
F1
(
F2
ó
F3
ô
F4
õ
F5
ö
F6
˜u
F7
ø
F8
-
F9
ú
FA
û
FB
ü
FC
ý
FD
þ
FE
±
FF
A few comments:
• Clearly this ISO 8859 encoding is much more mature than the previous ones. Not
only have all the useless characters been done away with, but also there is a companion to the isolated ‘ß’: the Greenlandic letter ‘±’, whose upper-case version is identical
to ‘K’.

ISO 8859
• The glyph ‘Ð’ appears twice: in position 0xA9 it represents the Croatian dje, whose
lower-case form is ‘Æ’; in position 0xD0, on the other hand, it represents the Icelandic
eth, whose lower-case form is ‘ð’.
In 1998 a third encoding dedicated to the Baltic languages came out: ISO 8859-13 (or
“Latin-7”), which has the peculiarity of combining these languages with Polish and including the appropriate types of quotation marks.
ISO 8859-5, 6, 7, 8, 11
ISO 8859-5, or “ISO Cyrillic”, stems from a Soviet standard of 1987, GOST 19768/87,
and is meant for the languages that use the Cyrillic alphabet. As there are many such
languages, all of them rich in characters, the encoding is limited to Russian as spelled
after the revolution (without the characters “fita …, yat , izhitsa ‡, i dessyatirichnoye i”
that Lenin eliminated) and to the languages spoken in European countries: Ukrainian
(without the character ‘‰ ’, which the Soviet government did not recognize), Byelorussian, Moldavian, Bulgarian, Serbian, and Macedonian. This encoding also includes the
‘№’ ligature, a number sign (like the North American English ‘#’), which appears in practically every Russian font. The ‘N’ in this character is a foreign letter; it does not appear
in the Cyrillic alphabet.
ISO 8859-6, or “ISO Arabic”, covers the Arabic alphabet. We are astonished by the minimalist appearance of this encoding: there are numerous empty blocks, yet many languages that use the Arabic script have extra characters that are not provided. ISO 8859-6
includes only the basic letters required to write Arabic and also the short vowels and
some of the diacritical marks (the wasla and the vertical fatha are missing). The punctuation marks that differ in appearance from their Latin counterparts (the comma, semicolon, question mark) are also included.
Describing the ISO 8859-7, or “ISO Greek”, encoding is a very painful experience for the
author, for he still bears the scars of that massacre of the Greek language that is known as
the “monotonic reform”. This reform of 1981 cut the Greek language offfrom its accents
and breathing marks for the sake of facilitating the work of the daily press and the computerization of the language. Which other country in the world could bear to perpetrate
so grave an injury on a 2,000-year-old language in order to accommodate it better to the
limitations of the computer? (See [169, 166].) The survivors of the massacre are collected
in this encoding: letters without accents and vowels with an acute accent. There are also
the vowels iota and upsilon with a diæresis, as well as with both an accent and a diæresis,
but their upper-case versions with the diæresis are absent.
The ISO 8859-8, or “ISO Hebrew”, encoding covers Modern Hebrew (or Ivrit). Once
again, a minimalist approach was taken: the Hebrew consonants and long vowels are all
there, but not the short vowels or any other diacritical marks. Yiddish is not provided for.
Finally, ISO 8859-11, or “ISO Thai”, which stems from Thai standard TIS 620 of 1986,
covers Thai, a Southeast Asian script that is a simplified version of the Khmer script. The
encoding is rather thorough: it contains practically all of the consonants, initial vowels,
diacritical marks, and special punctuation marks, as well as the numerals.

ISO 8859-14 (Latin-8) ISO 8859-14 (or “Latin-8”) is dedicated to the Celtic languages: Irish Gaelic (which is ordinarily written in its own alphabet), Scottish, and Welsh. Only Breton, with its famous ‘c’h’ ligature, is absent. It is a variant of ISO 8859-1 with 31 modified characters that we have shown here in black: nbspA0 ˙B A1 ˙b A2 £ A3 ˙C A4 ˙c A5 ˙D A6 § A7 `WA8 © A9 ´WAA ˙d AB `Y AC shyAD ® AE Ÿ AF ˙F B0 ˙f B1 ˙G B2 ˙g B3 ˙M B4 ˙m B5 ¶ B6 ˙P B7 `w B8 ˙p B9 ´w BA ˙S BB `y BC ¨WBD ¨w BE ˙s BF ˆWD0 Ñ D1 Ò D2 Ó D3 Ô D4 Õ D5 Ö D6 ˙T D7 Ø D8 Ù D9 Ú DA Û DB Ü DC Ý DD ˆY DE ß DF ˆw F0 ñ F1 ò F2 ó F3 ô F4 õ F5 ö F6 ˙t F7 ø F8 ù F9 ú FA û FB ü FC ý FD ˆy FE ÿ FF The Far East The first telegraph systems in the Far East were imported from the West and therefore used the Latin alphabet. How could the thousands, even tens of thousands, of ideographic characters of the Chinese writing system have been encoded, with either Morse code or anything similar? Transliteration into the Latin alphabet was not an option either, as the phonetics of the Chinese language are very ill suited to that approach. Japanese is simpler phonetically, but another problem impeded transliteration: the enormous number of homophones that are distinguished only in writing. Only computer science could enable the countries of the Far East to communicate conveniently over large distances. The country the best equipped for this task was, of course, Japan. In 1976, three years after the release of ISO 2022, the Japanese prepared the first GR-type encoding—that is, a 94-character supplement to ASCII: JIS C 6220 (which was rechristened as JIS X 0201-1976 in 1987). The ASCII used in Japan was already localized: a yen sign ‘¥’ replaced the backslash2 and the tilde was replaced by an overbar (for writing the Japanese long vowels in Latin script). JIS C 6220, based on the JISCII released in 1969, contains only katakana and a few ideographic punctuation marks (the period, the quotation marks, the comma, the raised dot), all in half-width characters: nbsp A0 ｡ A1 ｢ A2 ｣ A3 ､ A4 ･ A5 ｦ A6 ｧ A7 ｨ A8 ｩ A9 ｪ AA ｫ AB ｬ AC ｭ AD ｮ AE ｯ AF ｰB0 ｱB1 ｲB2 ｳB3 ｴB4 ｵB5 ｶB6 ｷB7 ｸB8 ｹB9 ｺBA ｻBB ｼBC ｽBD ｾBE ｿBF ﾀ C0 ﾁ C1 ﾂ C2 ﾃ C3 ﾄ C4 ﾅ C5 ﾆ C6 ﾇ C7 ﾈ C8 ﾉ C9 ﾊ CA ﾋ CB ﾌ CC ﾍ CD ﾎ CE ﾏ CF ﾐD0 ﾑD1 ﾒD2 ﾓD3 ﾔD4 ﾕD5 ﾖD6 ﾗD7 ﾘD8 ﾙD9 ﾚDA ﾛDB ﾜDC ﾝDD ﾞDE ﾟDF The phonetic modifiers were supplied as independent characters even though there was enough space to encode all of their combinations with letters. The syllable ‘ペ’ was thus obtained from the character ‘ヘ’ followed by a modifier character ‘°’. 2 As a result of which right up to this day, thirty years later, TEX commands in Japanese handbooks always start with a yen sign rather than a backslash.. . .

```text
The Far East
On January 1, 1978, after nine years of hard effort, the first true Japanese encoding,
JIS C 6226-1978, known today as “old JIS”, officially came into effect. It contains 6,694
characters: the Latin, Greek, and Cyrillic alphabets, the kana, and 6,349 kanji ideographic
characters, distributed over two levels. It was revised three times, finally to become
JIS X 0208-1997 in January 1997. This last encoding is perhaps the most important
Japanese encoding of all. Its structure complies with ISO 2022: there are 94 GR tables of
94 characters each.
In 1990 a second Japanese encoding was released: JIS X 0212-1990. It supplements the
first with 5,801 ideographic characters and 266 other characters. A third encoding,
JIS X 0213-2000, was released in January 2000. It adds another two levels of kanji to
those of JIS X 0208-1997: the third level contains 1,249 kanji; the fourth, 2,436.
China did not lag far behind Japan: in 1981, on the symbolic date of May 1, it issued the
first Chinese encoding, GB 2312-80. This encoding, which contains 7,445 characters, is
compatible with the ISO 2022 standard. It is suspiciously similar to the Japanese encodings, at least in its choice of non-ideographic characters: it includes the Latin, Greek, and
Cyrillic letters, and even the Japanese kana.
Over time there were numerous extensions to GB 2312-80. By 1992, the number of characters totaled 8,443. After Mao’s Cultural Revolution, the People’s Republic of China
adopted a simplified writing system of ideographic characters, and the encodings respect
it. But, contrary to what one might have expected, China also issued encodings in traditional characters. Thus in 1990 the GB/T 12345-90 encoding was released. The letter ‘T’ in
its name comes from the character 推and means “optional”—after all, in a country that
has simplified its writing system, the traditional form could only be regarded as optional.
An encoding was also released in Taiwan on a May 1, but this time in 1984 (three years
after the People’s Republic of China released its own encoding). It is called, in English,
“Big Five”, and its name refers to the five big Taiwanese corporations that collaborated on
its development. It seems that Taiwan went all out to surpass its bigger cousin: Big Five
contains no fewer than 13,494 characters, 13,053 of which are ideographic, arranged on
two levels. Finally, 1992 saw the release of the CNS 11643-1992 encoding, which broke
all the records for number of characters: a total of 48,711, including 48,027 ideographic
characters, organized into seven planes with approximately 6 to 8 thousand characters
each. The first two planes correspond roughly to the two levels of Big Five.
As for the other Chinese-speaking countries, Singapore uses mainly the GB encodings of
mainland China, and Hong Kong, despite its recent annexation into China, uses mainly
Big Five.
The encoding frenzy began in South Korea in 1992 with the KS X 1001-1992 encoding, which contains 4,888 ideographic characters, 2,350 hangul phonetic characters, and
986 other characters, once again including Latin, Greek, Cyrillic, and the Japanese kana,
strictly in imitation of the Japanese encoding JIS X 0208-1997.
North Korea is said to have abolished the ideographic characters, yet the first North
Korean encoding, KPS 9566-97 of 1997, contained 4,653 ideographic characters as well
as 2,679 hangul characters and 927 other characters. This encoding was inspired by
```

```text
the South Korean one but presents certain incompatibilities. In addition, positions
0x0448 to 0x044D fulfill an important state purpose: they contain the names of honorable
party president Kim Il-sung and his son and successor Kim Jong-il ... a funny way to
achieve immortality.
Using ISO 2022 to gain access to the characters in these encodings is not always very
practical because at any given time one must be aware of the current mode, that is, which
of G0, G1, G2, and G3 is the active encoding. In Japan there have been two attempts
to overcome this problem and make use of the characters of the JIS encodings without
employing escape sequences:
1. Shift-JIS is an initiative of Microsoft. The idea is very simple: the JIS encodings are
made up of tables of 94×94 characters, and, if we count in ranges of 16 characters,
that makes 6×6 = 36 ranges. But 36 can also be written as 3×12; thus we can obtain
any character by using two bytes, of which the first covers three different ranges and
the second covers twelve different ranges. We select the ranges 0x81-0x9F and 0xE00xEF for the first byte and 0x40-0x7E and 0x80-0xFC for the second. Why have we
chosen those particular ranges for the first byte? Because they leave section 0x200x7F free for ASCII and section 0xA0-0xDF free for the katakana. Thus, upon reading a
byte, the computer knows if it is a single-byte character or if a second byte will follow,
and a simple calculation is sufficient to find the table and the position of the desired
character.
Shift-JIS was widely used under Windows and MacOS. Its flagrant drawback is that
the technique of 3 × 12 severely limits the number of characters accessible through
this method. Thus there is no hope at all of adding any extra characters. And we cannot automatically change encodings because we do not have access to the ISO 2022
escape sequences.
2. EUC (Extended Unix Coding) is a variant of ISO 2022 without escape sequences.
There is not just one EUC but an assortment of localized versions: EUC-JP, EUC-CN,
etc. In each of them, one chooses from one to four encodings. The first two are obtained from suitable choices of ranges of characters. The third and fourth encodings
are ultimately formed through the use of two control characters: ss2 (0x8E) and ss3
(0x8F), followed by one or two other characters.
Thus, for example, EUC-JP includes ASCII, JIS X 0208-1997, the katakana, and
JIS X 0212-1990. Among these four, ASCII is obtained directly, JIS X 0208-1997
is obtained from the characters 0xA1-0xFE×0xA1-0xFE, the katakana are obtained
with ss2 followed by 0xA1-0xDF, and JIS X 0212-1990 is obtained with ss3 followed
by 0xA1-0xFE×0xA1-0xFE.
While Shift-JIS is peculiar to Japan, EUC has also been used in other countries: there are
the encodings EUC-CN (mainland China), EUC-TW (Taiwan), EUC-KR (South Korea).
The interested reader will find a very detailed description of these encodings and a host
of other information in Ken Lunde’s book CJKV Information Processing [240].
```

Microsoft’s code pages
Microsoft’s code pages
The term codepage for “encoding” was oined by Microsoft. As the DOS system, for example, was console-based, we find in the DOS code pages a set of graphical symbols used
to draw user interfaces through the simple arrangement of straight segments, corners,
crosses, etc. There are even lattices of pixels that simulate various shades of gray.
In the US, the most commonly used DOS code pages were 437 (“United States”) and 850
(“Multilingual”). In both cases, 128-position extensions to ASCII were made (the entire
upper half of the table). Here is the part of the table beyond ASCII for code page 437,
entitled “MS-DOS Latin US”:
Ç 80
ü 81
é 82
â 83
ä 84
à 85
å 86
ç 87
ê 88
ë 89
è 8A
ï
8B
î
8C
ì
8D
Ä 8E
Å 8F
É 90
æ 91
Æ92
ô 93
ö 94
ò 95
û 96
ù 97
ÿ 98
Ö 99
Ü 9A
¢ 9B
£ 9C
¥ 9D Pts9E
f
9F
á A0
í
A1
ó A2
ú A3
ñ A4
Ñ A5
ª A6
º A7
¿ A8
. A9
{ AA
½ AB
¼ AC
¡ AD
« AE
» AF
^^B0 __B1 ||B2
2 B3
8 B4
M B5
N B6
B B7
A B8
O B9
= BA
C BB
I BC
H BD
G BE
4 BF
5 C0
: C1
9 C2
7 C3
1 C4
; C5
J C6
K C7
F C8
@ C9
U CA
R CB
L CC
< CD
X CE
S CF
T D0
P D1
Q D2
E D3
D D4
> D5
? D6
W D7
V D8
6 D9
3 DA [[DB ZZDC
\ DD
] DE YYDF
α E0
β E1
Γ E2
π E3
Σ E4
σ E5
μ E6
τ E7
Φ E8
Θ E9
Ω EA
δ EB
∞EC
φ ED
ε EE
∩EF
≡F0
± F1
≥F2
≤F3
/ F4
0 F5
÷ F6
≈F7
° F8
• F9
·
FA
√
FB
n
FC
² FD
a FE nbspFF
This code page is a real mixed bag: a few accented letters (there is an ‘É’ but no ‘È’... ),
a handful of currency symbols, some punctuation marks, three rows of building blocks
for drawing user interfaces, and a number of mathematical symbols, including a small
range of Greek letters. One startling fact: the author does not know whether the character in position xE1 is a Greek beta ‘β’ or a German eszett ‘ß’. Its location between alpha
and gamma suggests that it is a beta, but at the same time the presence of the German
letters ‘ä’, ‘ö’, and ‘ü’ implies that this encoding should logically include an ‘ß’. Could it
be that the same character was supposed to serve for both? If so, depending on the font,
we would have had aberrations such as “ßιßλον” or “Gieβgefäβ”...
Code page 850 (MS-DOS Latin 1) is a variant of the preceding. It contains fewer graphical
characters and more characters for the languages of Western Europe. Note that the German eszett ‘ß’ appears in the same position as the ‘β / ß’ of code page 437:
Ç 80
ü 81
é 82
â 83
ä 84
à 85
å 86
ç 87
ê 88
ë 89
è 8A
ï
8B
î
8C
ì
8D
Ä 8E
Å 8F
É 90
æ 91
Æ92
ô 93
ö 94
ò 95
û 96
ù 97
ÿ 98
Ö 99
Ü 9A
ø 9B
£ 9C
Ø 9D
× 9E
f
9F
á A0
í
A1
ó A2
ú A3
ñ A4
Ñ A5
ª A6
º A7
¿ A8
® A9
{ AA
½ AB
¼ AC
¡ AD
« AE
» AF
^^B0 __B1 ||B2
2 B3
8 B4
Á B5
Â B6
À B7
© B8
O B9
= BA
C BB
I BC
¢ BD
¥ BE
4 BF

5 C0
: C1
9 C2
7 C3
1 C4
; C5
ã C6
Ã C7
F C8
@ C9
U CA
R CB
L CC
< CD
X CE
´ CF
ð
D0
Ð
D1
Ê
D2
Ë
D3
È
D4
ı
D5
Í
D6
Î
D7
Ï
D8
D9
DA [[
DB ZZ
DC
¦
DD
Ì
DE YY
DF
Ó E0
ß E1
Ô E2
Ò E3
õ E4
Õ E5
μ E6
þ E7
Þ E8
Ú E9
Û EA
Ù EB
ý EC
Ý ED
¯ EE
´ EF
shy
F0
±
F1
< F2
¾
F3
¶
F4
§
F5
÷
F6
¸
F7
°
F8
¨
F9
·
FA
¹
FB
³
FC
²
FD
a
FE nbsp
FF
There were numerous other MS-DOS code pages [204]: 708–710, 720, and 864 (Arabic); 737 and 869 (“monotonic” Greek); 775 (Baltic countries); 852 (countries of Central
Europe); 855 and 866 (Cyrillic, with 866 being for Russian only); 857 (Turkish); 860
(Portuguese); 861 (Icelandic); 862 (Hebrew, without the short vowels); 863 (“Canadian
French”, a pastiche of 437 and 850); 865 (Nordic countries); 874 (Thai); 932 (Japanese);
936 (simplified Chinese); 949 (Korean); 950 (traditional Chinese).
When Windows came out, there was no longer any need for “graphical characters”, and
a change of encodings was called for (even though it caused big problems for users who
were porting their documents from MS-DOS to Windows). In the meantime, the first
ISO 8859 encodings were released, and Microsoft decided to adopt them—but avoided
their major shortcoming: the characters 0x80-0x9F were not control characters in Microsoft’s implementation.
Thus code page 1252 Windows Latin 1, also known as “ANSI”, is an ISO 8859-1 encoding
to which the following two lines have been added:
¤
,
f
„
...
†
‡
ˆ
88 ‰
Š
8A
‹
8B Œ
8C
8D
Ž
8E
8F
‘
’
“ 93
” 94
• 95
– 96 —97
˜ 98 ™99
š 9A
› 9B
œ 9C
9D
ž 9E
Ÿ 9F
We can only rejoice at the fact that the letters ‘Œ’, ‘œ’, and ‘Ÿ’ are found in this encoding.
There are also the single guillemets ‘‹ ›’ and the two most common Central European
letters, ‘Š š’ and ‘Ž ž’. A few details: ‘,’ and ‘„’ are the German single and double opening
quotation marks, also called Gänsefüßchen (= ‘[little] goose feet’).
Code page 1250 Windows Latin 2 both extends and modifies ISO 8859-2. Positions 0x800xBF are the ones that have undergone modification:
¤ 80
,
„ 84
...
† 86
‡ 87
88 ‰89
Š 8A
‹ 8B
0 8C
ˇT 8D
Ž 8E
3 8F
‘
’
“ 93
” 94
• 95
– 96 —97
98 ™99
š 9A
› 9B
6 9C
t’ 9D
ž 9E
9 9F
nbspA0
ˇ A1
˘ A2
Ł A3
´ A4
˛
A A5
¦
A6
§ A7
¨ A8
© A9
¸S AA
« AB
¬ AC
shyAD
® AE
˙Z AF
° B0
± B1
. B2
ł
B3
´ B4
μ B5
¶ B6
·
B7
¸ B8
˛a B9
¸s BA
» BB
L’ BC
˝ BD
l’ BE
˙z BF
There has never been a Windows Latin 3 or a Windows Latin 4, but there is a 1254 Windows
Latin 5 for Turkish, which differs from 1252 Windows Latin 1 in only six positions:
˘G D0
Ñ D1
Ò D2
Ó D3
Ô D4
Õ D5
Ö D6
× D7
Ø D8
Ù D9
Ú DA
Û DB
Ü DC
˙I DD
¸S DE
ß DF
˘g F0
ñ F1
ò F2
ó F3
ô F4
õ F5
ö F6
÷ F7
ø F8
ù F9
ú FA
û FB
ü FC
ı
FD
¸s FE
ÿ FF

Apple’s encodings
These are the same differences that we find between ISO 8859-1 and ISO 8859-9.
Other Windows code pages are 1251 Windows Cyrillic, 1253 Windows Greek (“monotonic
Greek” is implied3), 1255 Windows Hebrew, 1256 Windows Arabic, and 1257 Windows
Baltic.
Apple’s encodings
From the beginning, the Macintosh used its own encoding, an extension of ASCII
that was still incomplete on the first Macintosh (released in 1984) but was gradually
fleshed out. The unusual aspect of the Macintosh encodings is that they, like the MSDOS code pages, include mathematical symbols. Since most fonts do not contain these
symbols, MacOS had a special substitution procedure. Whichever font one used, the
mathematical symbols almost always came from the same system fonts. Other special
features of the Macintosh encodings: they include the ‘fi’ and ‘fl’ ligatures as well as the
famous bitten apple ‘z’ that Apple uses as its logo.
Here is the encoding used on the Macintoshes sold in the US and in Western Europe,
which is called Standard Roman [53] (a rather poorly chosen name, since the term “roman” refers to a font style rather than to a writing system):
Ä 80
Å 81
Ç 82
É 83
Ñ 84
Ö 85
Ü 86
á 87
à 88
â 89
ä 8A
ã 8B
å 8C
ç 8D
é 8E
è 8F
ê 90
ë 91
í
ì
î
ï
ñ 96
ó 97
ò 98
ô 99
ö 9A
õ 9B
ú 9C
ù 9D
û 9E
ü 9F
† A0
° A1
¢ A2
£ A3
§ A4
• A5
¶ A6
ß A7
® A8
© A9 ™AA
´ AB
¨ AC̸
= AD
ÆAE
Ø AF
∞
B0
±
B1
≤
B2
≥
B3
¥
B4
μ
B5
∂
B6
∑B7
∏B8
π
B9
 BA
ª
BB
º
BC
Ω
BD
æ
BE
ø
BF
¿ C0
¡ C1
¬ C2
√
C3
f
C4
≈C5
Δ C6
« C7
» C8
...
C9 nbspCA
À CB
Ã CC
Õ CD ŒCE
œ CF
–
D0 —
D1
“
D2
”
D3
‘
D4
’
D5
÷
D6
♦
D7
ÿ
D8
Ÿ
D9
/
DA
´
DB
‹
DC
›
DD
fi
DE
fl
DF
‡ E0
·
E1
,
E2
„ E3 ‰E4
Â E5
Ê E6
Á E7
Ë E8
È E9
Í EA
Î EB
Ï EC
Ì ED
Ó EE
Ô EF
z
F0
Ò
F1
Ú
F2
Û
F3
Ù
F4
ı
F5
ˆ
F6
˜
F7
¯
F8
˘
F9
˙
FA
˚
FB
¸
FC
˝
FD
.
FE
ˇ
FF
A few details: we have already seen the German quotation marks ‘,’ and ‘„’ in the 1252
Windows Latin 1 encoding. The character 0xDA ‘/ ’ is a fraction bar. Do not mistake the
characters ‘∑’ and ‘∏’ for the Greek letters ‘Σ’ and ‘Π’: the former, the mathematical
symbols for sum and product, are larger than the ordinary Greek letters, which are of
regular size. In addition, both may appear in one formula: ∑∞
i=0 Σi = ∏∞
j=0 Π j. The two
glyphs look very much alike, but in position xA1 we have the degree sign (a perfect circle)
while in position xBC there is a superscript letter ‘o’, used in Spanish, French, and other
languages. The letter ‘ı’ in position F5 is not intended for Turkish but to be combined
with accents.
3 This encoding long irritated the Greeks because it differs only slightly from ISO 8859-7: the accented
capital letter alpha occurs in position 0xA2 on the Windows code page and in position 0xB6 in the ISO encoding;
thus the letter tends to disappear when a document is transferred from Windows to Unix or the opposite.. . .

There is an Icelandic version of this encoding that differs from Standard Roman in six positions: ‘Ý’ (0xA0), ‘Ð’ (0xDC), ‘ð’ (0xDD), ‘Þ’ (0xDE), ‘þ’ (0xDF), ‘ý’ (0xE0).
There is a Turkish version as well, that differs from Standard Roman in six consecutive
positions: ‘˘G’ (0xDA), ‘˘g’ (0xDB), ‘˙I’ (0xDC), ‘ı’ (0xDD), ‘¸S’ (0xDE), ‘¸s’ (0xDF). Position 0xF5
of this encoding has been left empty so that the letter ‘ı’ would not appear twice.
In addition, there is a Romanian version of the encoding, Romanian, that again differs
from Standard Roman in six positions: ‘˘A’ (0xAE), ‘∑’ (0xAF), ‘˘a (0xBE), ‘¨’ (0xBF), ‘∏’ (0xDE),
‘≠’ (0xDF).
For the languages of Central Europe and the Baltic countries, Apple offers the Central
European encoding, shown below:
Ä 80
% 82
É 83
˛
A 84
Ö 85
Ü 86
á 87
˛a 88
ˇC 89
ä 8A
ˇc 8B
/ 8C
5 8D
é 8E
3 8F
ˇD
í
d’
!
&
˙E
ó
˙e
ô
ö
9A
õ
9B
ú
9C
ˇE
9D
ˇe
9E
ü
9F
† A0
° A1
˛E A2
£ A3
§ A4
• A5
¶ A6
ß A7
® A8
© A9 ™AA
˛e AB
¨ AC̸
= AD
≥AE
* AF
,
B0
"
B1
≤
B2
≥
B3
'
B4
K¸
B5
∂
B6
Σ
B7
ł
B8
L¸
B9
l¸
BA
L’
BB
l’
BC
BD
:
BE
N¸
BF
n¸ C0
1 C1
¬ C2
√
C3
7 C4
ˇN C5
Δ C6
« C7
» C8
...
C9 nbspCA
ˇn CB
˝O CC
Õ CD
= CE
# CF
–
D0 —
D1
“
D2
”
D3
‘
D4
’
D5
÷
D6
♦
D7
(
D8
D9
DA
ˇR
DB
‹
DC
›
DD
ˇr
DE
R¸
DF
r¸ E0
Š E1
,
E2
„ E3
š E4
0 E5
6 E6
Á E7
ˇT E8
t’ E9
Í EA
Ž EB
ž EC
\$ ED
Ó EE
Ô EF
)
F0
˚U
F1
Ú
F2
˚u
F3
<
F4
>
F5
+
F6
-
F7
Ý
F8
ý
F9
k¸
FA
˙Z
FB
Ł
FC
˙z
FD
≤
FE
ˇ
FF
Notice that, for an unknown reason, the ‘Σ’ has resumed its customary size and that there
is no ‘Π’. This encoding covers Polish, Czech, Slovak, Slovenian, Hungarian, Lithuanian,
Latvian, and Estonian. It does not cover Croatian because it lacks the letter ‘Ð Æ’. For this
reason, Apple issued a special encoding (Croatian) for the Croatian language.
Other Apple encodings: Arabic (Arabic, Persian, Urdu, still without wasla but with vertical fatha), Chinese Traditional, Cyrillic (for the European languages that use the Cyrillic alphabet, with the exception of Ukrainian, for which the letter ‘‰’ is missing), Greek
(“monotonic” Greek), Hebrew (Hebrew with vowels, semivowels, and schwa), Japanese,
Korean, Devanagari, Gujarati, Gurmukhi, and Thai.
Electronic mail
The protocol for electronic mail that is still in use today was published in 1982: it is
RFC 822 (in which RFC stands for “Request for Comments”, a way to demonstrate the
democratic nature of the Web’s standards). This RFC stipulates that electronic messages
are to be encoded in ASCII.
To mitigate that drawback, a new RFC published in 1996 (RFC 2045) introduced a technique that has since become an integral part of electronic mail: the MIME protocol
(= “Multipurpose Internet Mail Extensions”). MIME allows for the attachment of files to
e-mail messages and for dividing a message into multiple segments, each one potentially

Electronic mail
of a different type, or, if it is of type text, potentially in a different encoding. To specify
the encoding of a message or a part of a message, we use two operators:
• charset is the encoding of the content. Its value must appear on a list [186] established and regularly updated by IANA (= “Internet Assigned Numbers Authority”).
In February 2004 there were 250 registered encodings, such as US-ASCII, ISO-2022JP, EBCDIC-INT, ISO-8859-1, IBM437 (code page 437), windows-1252 (Windows code
page 1252), etc.
The encoding affects only those segments of MIME type text (the subtype being
plain, which indicates that the text is not enriched). The syntax is as follows:
Content-Type: text/plain; charset=US-ASCII
• Content-Transfer-Encoding specifies how to translate the coming binary (beyond 0x7f) bytes into ASCII data. This is necessary because MIME did not change
the nature of electronic mail—which remains based on ASCII just as much as it
was twenty years ago. In fact, MIME offers only makeshift methods for converting
binary bytes to ASCII and vice versa. Two methods are available: “quoted-printable”
text and text in “base 64”.
Quoted-printable involves using the equals sign as an escape character. Three possibilities exist:
1. The character to convert is a “printable” ASCII character—that is, in the
range of 0x20 to 0x7e—other than the equals sign (ASCII 0x3d). In this case
it passes through unchanged.
2. The character is a control character (0x00-0x1f), a binary character (0x80-0xff),
or an equals sign. In this case we write the equals sign followed by the position of
the character in the table, in the form of a two-digit hexadecimal number. Thus,
if we have specified that we are using ISO 8859-1, the word “voilà” is written
voil=E0.
3. Since the length of the lines in the message is limited, we will divide any excessively long line by adding an equals sign followed by a newline. A line break
of this kind will ordinarily be disregarded by the application that decodes the
“quoted-printable” text.
A message encoded in “quoted-printable” format must include the following line in
its header:
Content-Transfer-Encoding: quoted-printable
The other method, “base 64”, involves taking three consecutive bytes of text and
regarding them as four groups of six bits (3 × 8 = 4 × 6). Each group of six bits is
represented by one ASCII character, as follows:
– the letters A to Z represent the numbers between 0 and 25;
– the letters a to z represent the numbers between 26 and 51;

– the digits 0 to 9 represent the numbers between 52 and 61;
– + and / represent respectively the numbers 62 and 63.
The remaining possibility is that one or two bytes will be left over after translation of
all of the three-byte sequences. Suppose that one byte, notated xxxxxxxx, is left over.
Then we will use the two six-bit groups xxxxxx and xx0000, and we will append two
equals signs to the converted string. If two bytes, xxxxxxxx and yyyyyyyy, are left
over, we will use the three six-bit groups xxxxxx, xxyyyy, and yyyy00, and we will
append a single equals sign to the converted string.
Example: to encode the word “voilà” (01110110
11100000), we start by taking the first four letters and dividing them into groups
of six bits (011101
000000), namely the numbers 29, 38, 61, 41, 27, and 0, which give us the alphanumerics dm9pbA. The remaining
letter ‘à’ (11100000) gives us two groups of six bits (111000 000000), namely the numbers 56 and 0, and therefore the codes 4A. We will append an equal signs to indicate
that one letter is missing to complete the triplet. Thus the result is dm9pbA4A=.
A message encoded in “base 64” must include the following line in its header:
Content-Transfer-Encoding: base64
What are the advantages and disadvantages of the conversions to “quoted-printable” or
“base 64”? When the encoding and decoding are performed transparently by the e-mail
software, the difference is of little importance, apart from the fact that a message in ASCII
with few binary characters will take up less space in “quoted-printable” than in “base 64”,
while for a message entirely in binary characters the opposite is true. Nevertheless, if
the message could be read with software that is not compatible with MIME, “quotedprintable” text will be legible in languages such as French or German that do not use
accented or special lettetrs with great frequency, whereas text in “base 64” will have to
be processed by computer.
While RFC 2045 specified the encoding of text segments, no provision was made for the
subject line of the message or the other lines in the header that would contain text. The
solution was provided by RFC 2047, which defined a way to change encodings at any
time, either within a string in the header or within the body of the message. It is nothing
revolutionary: we once again use the equals sign (which plays a special rôle in both forms
of conversion to ASCII) as an escape character:
=?name?*?converted_string?=
where name is the IANA name of the encoding, * is either Q (= quoted-printable) or B
(= base 64), and converted_string is the converted string. Thus the word “voilà” encoded in ISO 8859-1 can be written in the following two ways:
=?iso--?Q?voil=E0?=
=?iso--?B?dm9pbA4A=?=
Alas, neither of them is really legible...

```text
The Web
The Web
The Web is the exchange of HTML data under the protocol HTTP (“Hypertext Transfer
Protocol”). Version 1.1 of this protocol is described in RFC 2616 of 1999. Browsers and
servers communicate through this protocol by sending each other messages that may or
may not contain HTML data. Thus, when one types a URL followed by a carriage return
in the appropriate area in the browser, the browser sends an HTTP request to the server
in question. The server replies by sending the HTML data corresponding to the URL,
or with an error message. In all three cases (request, transmission of HTML data, error
message), the parties to the communication send each other messages through HTTP.
HTTP is based on three concepts: the encoding (called charset), which by default is
ISO 8859-1 (and not ASCII); the type of compression to be applied (called contentcoding, whose values may be gzip, compress, zlib, or identity); and the “transfer coding” to be used. The transfer coding corresponds to the “quoted-printable” and “base 64”
of MIME, except that here data transfer is binary and thus does not require conversion
to ASCII. The “transfer coding” that we use is chunk, which means that the data will be
divided into blocks of a fixed length.
Here is an example of an HTTP header for a message in ISO 8859-1 with gzip compression:
Content-Type: text/html; charset=iso--
Content-Encoding: gzip
Transfer-coding: chunked
where the first line specifies that the MIME type of the following document is text, with
html as its subtype.
HTTP headers can also be included in the value of the content attribute of the meta
element of HTML and XHTML. Each occurrence of this element contains a line of the
HTTP header.
The first two parameters (encoding and compression) can also be used in the HTTP request sent to the server, to express the browser’s possibilities. In this way the browser can
request a certain encoding that it knows how to use or even multiple encodings arranged
in order of preference, one or more types of compression, etc. By writing
Accept-Charset: iso--, iso--;q=0.8
the client specifies that it can read, in order of preference, text in ISO 8859-15 and
ISO 8859-1. The parameter q=0.8 (‘q’ as in “quality” and a number between 0 and 1)
that follows the second encoding applies to it alone and indicates that the use of this
encoding will give a result with 80% quality. Using this list of requested encodings and
their weights with respect to quality, the server will decide which encoding to use to
send data. If none of the requested encodings is available, the server will reply with an
error message: “406: not acceptable”.
The same is true for compression:
```

```text
Accept-Encoding: gzip;q=1.0, identity;q=0.5, *;q=0
where the asterisk is the “wildcard”. The line shown above should be interpreted as follows: the document may be compressed with gzip (top quality) or not compressed at all
(50% quality), and every other type of compression is of “0% quality”, which means unacceptable.
One details that may lend itself to confusion: here “charset” is used to designate the character encoding and “coding”, or even “encoding” in the “accept” commands, is used for
compression.
```
