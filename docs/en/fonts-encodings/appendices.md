---
title: "Appendices A–G: Font Formats, Virtual Machines & Mathematical Foundations"
description: "Unabridged English technical reference: Bitmap fonts (A), TeX & Omega (B), PostScript (C), TrueType/OpenType/AAT tables (D), TrueType instructions (E), METAFONT (F), Bézier curves (G)."
---

# Appendices A–G: Technical Reference Manual
**By Yannis Haralambous, Ph.D.**
*From Fonts & Encodings, pp. 599–990*

---

```text
A
Bitmap Font Formats
Without a doubt, bitmap font formats are things of the past. Aside from a few visionaries
such as Luc Devroye [117], who dreams of the perfect rendition of a font in bitmap form with
a pixel having the size of a molecule of ink (!), few people give serious consideration to bitmap
fonts today, since all operating systems, without exception, have switched to vector fonts.
Yet bitmap fonts are practical for display on screen. First, they are rendered more cleanly:
as much as we sing the praises of vector fonts, a good, sturdy bitmap font is more efficient
than the most beautiful Aldine for displaying text on the screen as it is typed, especially at a
small size. Moreover, bitmap fonts are easy to modify and adapt to changing needs. Creating
a new glyph takes less than a minute; modifying it is a matter of a few clicks to enable or
disable a handful of pixels.
Bitmap fonts can always be useful in any application oriented towards reading on a screen
rather than towards printing, such as the Unix console that we use every day but hardly ever
print out.
Next, there are also bitmap fonts that go with vector fonts. An intelligent operating system
can take advantage of them to display certain actual sizes optimally while using vector fonts
for printing.
Below we shall examine the most common bitmap font formats. Most of them are surprisingly simple, unlike those for vector fonts.
A.1
The Macintosh World
A.1.1
The FONT Format
In 1984, the first Macintosh was already equipped with 17 fonts, some of which, such as Venice,
Athens, and Cairo, rather quickly left the scene; others, such as Chicago (which was replaced by
```

................................................................................................................................................................................................................................................................
........................................................................................................................**..................................................*.......*...........................................................................
.......................................................................................................................**.......********.....................................*.....*..........*..*...*...**.***.............**.........................*........
.......................**............*****..*************............***..***..........*...**...**.....................*.......**......*.............*............***..**..**************.*...*..*..***.*..*..*...****...*.*..*...*....................*.****...
........**............****.......*.......*.......*......**..............**.............*..*..*.*..*........*...*....***.***...**.*...*.*............***...........**.....*.*..*...*..****.*.********.*.**..*.*...**..**..***..***.*.*.................*.**..****
.....*..**..*........**..**.....***......**......*.*...*.**.............**................*..*.*..*.......**..***..*********.**...*.*..*..*........*****.......*..*.*.....**...*.*...****.*..*..*..***...**..*...**..**.****..**.***...*..............*.**..**..
.....**.**.**.......**....**...**.**......*......*..*.*...**...*........**........*....*...*******.......**..*****.*******..**.....*...*.**..........*.........**....*....**....*....***.....*..*..***......*.....**....*.**..***.*.*..*.............*..**.***..
******************.**......**.**...**.....**.....*...*.....**.**........**........**...*.....*.*........**..**************...**...*.*..******.**.**.....**.**.****....*...**....*....***...*******..***.....*....**..***..**..**..*..*****..*****....*..******..
.....**.**.**.....****....*****.....*......*.....*..*.*...**.***********..***********......*******.*...**....*****.*********..**.*...*.*.**..........*.........**.*.......**....*....***....*..*.....***...*..**.**..**...**..**.......*............*...***.**..
.....*..**..*........*....*................**....*.*...*.**...**..................**...*..*..*.*..***.**......***..*********...**......*..*..........*.........*..*.......**...*.*...*......*..*.....***...*.*..***..**...**..**.......*............*...**..**..
........**...........*....*.................*....*......**.....*..................*..******..*.*..*.***........*....*******.....********...........................*.....*.*..*...*..***...........*.*.*..*..*..***..**...**..**..........**.....***....**..**..
.....................******.................*************.............................***..**...**...*...............**.**...........................*..............*****..*************............***...*...**..****.....*..*...........**.....***.....****...
.......................................................................................*.............................................................*.......................*.....*.................*......................**.............*....................
............................................................................................................................................................................*.......*.....................................................*.....................
................................................................................................................................................................................................................................................................
................................................................................................................................................................................................................................................................
................................................................................................................................................................................................................................................................
......................................................................................................................................................................................................................................................****....**
**.****.******....**.******..***.******.****..****......................****...........****.*****..****.*****.**********.****.**..******....****...****...*........**.....*.****.*****..****.*****..***.********..****..****..**..****..****..**********.*.....*
***...**...**....***.**.....**.......****..****..**.......**......**...*...**..*****..**..****..****...***..****...**...**...***..**.**.....****..**.**...**......****....***..****..****..****..****..*..**..**..****..****..**..****..****..**....****..*....*
**....**..**....*.**.**....**........****..****..******..**........**......**.*.....*.**..****..****....**..****...**...**....**..**.**.....****.**..**...***....******...***..****..****..****..****.....**..**..****..****..**..****..****..**....****..*....*
**....**.****..*..**.*****.*****.....**.****.**..******.**..******..**....**.*..***..***..****..****....**..****...**...**....**..**.**.....******...**...****..********..***..****..****..****..*****....**..**..****..****..**..**.****.**..**...**.**...*...*
**...**.....***...**.....****..**...**.**..****..**....**............**..**..*.*..*..************.**....**..******.****.**.*********.**.....*****....**...*.*****.***.***.***..*******.**..*******..***...**..**..****..****..**..**..**...****...**..**...*...*
**..**......*********....****..**..**..**..**.*****.....**..******..**...**..*.*..*..***..****..****....**..****...**...**..****..**.**.**..******...**...*..***..***..******..****....**..****..**..***..**..**..****..****..**..**.****...**...**...**....*..*
**.**.......**....**.....****..**..**..**..**....**......**........**........*..**.**.**..****..****....**..****...**...**..****..**.**.**..****.**..**...*...*...***...*****..****....**..****..**...**..**..**..****..****..**..****..**..**..**....**....*..*
****....*...**....**.*...****..**..**..**..**...**.****...**......**.....**...*.......**..****..****...***..****...**...**..****..**.**.**..****..**.**...*.......***....****..****....**..****..***..**..**..**..**.****..*..**..*.**..**..**..**....**.....*.*
********.****.....**..****..****...**...****..***..****..................**....*****..**..*******..****.*****.*******....****.**..******.****.**...********.......***.....*.****.**.....****.**..**.***...**...****...**....**..**..**..**..**..********.....*.*
......................................................*...................................................................................................................................**..........................................................***.....**
.....................................................*.....................................................................................................................................**...................................................................
................................................................................................................................................................................................................................................................
...........................................................................................................................................................................................**...........*..**..*.............................................**.
....................................................................................................................................................................................*..*..*..*.........*..*..**...*..*..*..*................................*..*
*.............*.........................................................................................................................................................***...............*..*..................................*....*.....**.........**..*.*..*
*..*...........*.......**.............**........***......**....**...****....**.............................................**..........................................*.*.*........****..****..****.******.....*.****.**..**..*......*...*..*..*..*.*..**...**.
*.*.*...........*......**.............**.......**........**...........**....**.............................................**..........................................*.*.*.......**..****..****...***...**....***..****..**...................................
**...*............****.*****..***..*****.****.****..**********.**...****..*************.*****..****.*****..*******.**.***.******..****..****..**..****..****..********.*.*.*..**..***..****..****....**...***...***..****..**.****..****..****..****..****..****
*................*...****..****..***..****..**.**..**..****..****...****.**.****..**..****..****..****..****..*****..**..*.**.**..****..****..**..****..****..**....**.*.*.*.*..**.**..****..****....**...****..***..****..***...***...***...***...***...***...*
*.................*******..****...**..****..**.**..**..****..****...******..****..**..****..****..****..****..****...***...**.**..****..****..**..**.****.**..**...**.*..*..*......**************....****.*.***.***..****..**.*****.*****.*****.*****.*****.****
*................**..****..****...**..********.**..**..****..****...*****...****..**..****..****..****..****..****....***..**.**..****..****..**..**..**..**..**..**...*.*.*.......**..****..****....**...*..******..****..****..****..****..****..****..****..*
*................**..****..****...**..****.....**..**..****..****...******..****..**..****..****..****..****..****.....***.**.**..****..****..**..**.****.**..**.**....*.*.*.......**..****..****....**...*...*****..****..****..****..****..****..****..****..*
*................**..****..****..***..****...*.**..**..****..****...****.**.****..**..****..****..****..****..****...*..**.**.**.***.****..*..**..*.**..****..****.....*.*.*.......**..****..****...***...*....****..****..****..****..****..****..****..****..*
*.....********....**********..***..*****.****..**...*******..****...****..******..**..****..**.****.*****..*******....***...**.**.**..**....**..**..**..**.***********.*.*.*.......**..****..**.****.******.....*.****..****..*****.*****.*****.*****.*****.****
*......................................................**...........**..............................**........**..............................................**........***......................**.............................................................
...................................................*...**........*..**..............................**........**..........................................*...**..................................*.............................................................
....................................................****..........***......................................................................................****..................................*..............................................................
................................................................................................................................................................................................................................................................
................................................................................................................................................................................................................................................................
..........*....*.....**.........**..**......**..*...*....*.....**.........**..*...*....*.....**.................*..........***..................................................................................................................................
.........*......*...*..*..*..*.*..**..**..**..**...*......*...*..*..*..*.*..**...*......*...*..*..*..*..*..**..***...***..*...*......******.****....****....****..***.*...*..**..*........********...****.*.........................**....**..............******
.......................................................................................................****..**.*.*.**..*.**........**..*.***..**..*....*..*....*..*..**.**.*............**..**.....**..**...........................**..**..........***...**...
..****..****..****..****..****.****.**..**.*****..****..****..****..****..****.**..****..****..****..**.*.*..**.*...**.....**...***.**..*.***..**.*.***..**..**..*.*..*.*.**..........*..**..**.....**..**..***...****...*....*..*..********.**..**....**...*...
***...***..****..****..****..******.**..**.**..****..****..****..****..****..****..****..****..****..**.*..**.*.*...**....*.**.*******..*.***.**..*.*..*.**.*..*.*.*..*...*.......*********..**.....**.***.*...*.**...*..*...*....*....**....**..**...****..**..
***....**..****..****..****..******.**..**.**..****..****..****..****..****..****..****..****..****..**.*.....*.*.*****...*..*******.****.***..**.*.***..**.*....*...................*...********...***.**.*....**....*******......*********.**..**..**.**...**.
***....****************************.**..**.**..****..****..****..****..****..****..****..****..****..**........***..**....**..******....*.***...***.*..*.**.*..*.*................*********..**.....**..**.*...**.*...*..*...*....*....**....**..**.**..**....**
***....**....**....**....**....****.**..**.**..****..****..****..****..****..****..****..****..****..**.........*...**.....**.*.***.....*.***...***.*..*.**..**..*..................*....**..**.....**..**..****...***...*....*..*.....**....**..**.**..**...**.
***...***...***...***...***...*****.**..**.**..****..****..****..****..****..****.*****.*****.*****.***.............**...*..**..........*.***...**.*....*..*....*........................**..**....***..**.............................**....**..**.**..*....*..
*.****..****..****..****..****.****.**..**.**..**.****..****..****..****..****..**.**.**.**.**.**.**.**............******....**.........*.***.***...****....****.........................**..******..****..............*************...**....*****.*.***....**..
...**.....................................................................................................................*...*..............................................................................................................*..............*...
....*......................................................................................................................***..............................................................................................................*..............**...
...*......................................................................................................................................................................................................................................................******
............................................................................................................................*....**..*.**..*....................................................................................................................
.............................................................................................................................*..*..**.*..**.................................................................*..*................................................
..............................................................................***...............................................................................................................................................................................
*********...........**.***..***...****......................**..**............*....**......................................****..****..****..********.......................*..***.**.***.............*..*.**..**....*................***.**..******.*..........
*.**..**.........*.**.*..****.**.**..**.....................**..**...........*....**..........*...........................**..****..****..****..**.........................*..*.**.***.**........*.........**..**...*....****........**......**...*****.........
..**..**..*******..**..******.****....**.********...****.*...................*....**......*...*......*..**..*.............**..****..****..****..**....********.............**.**.*..***.*..*....*.*..**..****..**...*...*....*..**..************..**.*..........
..**..**.*.**..**..**.**.****.****....***...**..**.**..**...**..**......*...*....****.****...*.*....*..*..*..*............**..****..****..****..**...**..**..**............**.***..*.***.......*...*.**..****..**..*...*.......****..**...**.**...**.*..........
..**..**...**..**..**.**.****.****....**.*****..**.**..**...**..*********...*.....**.*....*..*.*...*..*....*..*...........**************..****..****.**..**..**************..............******.....***..**.****...*..*******.**..**.**...**.**...*******.......
..**..**...**..**..**..****.***..*....*.**..******.**.***..**...**....*..*.*......**..****..*...*.*..*......*..*..........**..****..****..****..**...**..******................................*...*.**..**..**....*...*......**..**.**...**.**...**.*.**.......
..**..**...**..**..**.............*..*..**..**.....***.**.**....**....*..*.*......**.*......*...*..*..*....*..*...........**..****..****..****..**...**..**................................*....*.*..**..**..**...*...******...****..**...**.**...**............
..**..**...**..**..**.**********..*..*..**..**...*.**..**.**...***........*.......**.......*.....*..*..*..*..*..**..**..****..****..****..****..**...**..**...*..................................*...**..**..**...*.....*....*..**...**...**.**...**.....****.**
..**..**...*...*...**............**..**..********.*.****...****.**........*.......**.......*******...*..**..*...**..**..****..****..**.****..********.********........................................*****..**..*.......****........**...**.**...**.....****.**
..**..**...........**.............................................................**.....................................................................................................................**...............................................*.*..*
*.**..**..........**.............................................................**..................................................................................................................*...**..............................................*.*..*.
*.**..**..............................................................................................................................................................................................****......................................................
...............**...**.....*........*....*.**.....*....*....**.............*......*....**....*..........................**.....................
..............*..*.*..*...*....*.*...*..*.*..**..*.*..*....*..*......**.....*....*....*..*....*........................*..*....................
....................................................................**..............................**..**..******...***..*...*.*..*..*........
.**.***.......****.*****.****.************.**..**.**.****..****.....*.....****.**..****..****..**..*..**..**......***...**...*.*....**.********
*..*.*.......**..****...**..****...**...**.**..**.****..****..**.***.***.**..****..****..****..**......................................*......*
*..*.*.......**..****...**..****...**...**.**..**.****..****..*************..****..****..****..****....................................*......*
.**.*........**..****...**..****...**...**.**..**.****..****..*********..**..****..****..****..****....................................*......*
....*........**********.**********.****.**.**..**.****..****..*********..**..****..****..****..****....................................*......*
....*.**..**.**..****...**..****...**...**.**..**.****..****..*************..****..****..****..****....................................*......*
...*.*..**..***..****...**..****...**...**.**..**.****..****..*************..****..****..****..****....................................*......*
...*.*..**..***..****...**..****...**...**.**..**.****..****..**.*******.**..****..****..****..****....................................*......*
..*...**..**.**..*********..**************.**..**.**.****..****...**.**...****..****..****..****.**....................................*......*
...........................................................................................................................**....**....********
............................................................................................................................*....*.............
...........................................................................................................................*......*............gp
Figure A-1: The global image of the font Chicago, which was used on the Macintosh’s menus for more than
15 years. It is an up-to-date version of the font, as we can see that the euro sign has been included.
Charcoal to give the Mac’s desktop a new look), stayed around for a while; finally, two of them
have survived to the present, becoming vector fonts along the way: Geneva and Monaco.
These fonts were all resources of type FONT. The “Macintosh Programmer’s Guide” (Inside
Macintosh [49, p. I-227]) of the era explains the structure of these resources in great detail.
Here is a brief description: A FONT resource is a series of pairs of bytes in little-endian order
that consists of the following:
• Global parameters: the “type of font” (monospaced or proportional), the positions of the
first and last glyphs in the table, the maximum set-width, the “maximum kern”1), the
number of pixels below the baseline, the width and height of the bounding box, a pointer
to the table of set-widths, the leading (i.e., the number of pixels to add between lines of
glyphs), and the width of the font’s global image (see below).
• The global image: the concatenation of all the glyphs into a single—very long—bitmap
image (see Figure A-1). Apple requires us not to leave any space between the glyphs.
The pixels of this image are grouped into lines of the same length, running from top to
bottom, which means that, to obtain a glyph, we must read its first line and then make
a leap equal to the width of the global image to find its second line, and so on.
• A table of pointers to the origins of the glyphs in the global image.
• A table of offsets of the lower left pixel of the glyphs with respect to the origin, as well as
the values of the displacement vectors.
For instance, a program that wants to display an italic ‘f ’, whose terminal may extend a few
pixels beyond the origin, will go to the table of pointers to find the origin of the ‘f ’ in the
1 The term “kern” here is used in an unexpected way: here it refers to the number of pixels that appear
to the left of the origin of the displacement vector. This sense corresponds to what kerning meant in the days
of metal type: that part of the character that extended beyond its parallelepiped to appear over the preceding
parallelepiped or the following one.

```text
A.2. The DOS World
global image, and then to the table of offsets to find out how much it should move to the left
before beginning to draw any pixels, and, at the same time, how many pixels it should move
forward after drawing the pixels. Clean and simple.
A.1.2
The NFNT Format
A short time later, when Apple realized that it would be convenient to have several point sizes
of the same bitmap font, a new type of resource was introduced: the FOND resource (see §6).
This is a “font family” resource that dispatches to the different bitmap fonts that are available.
Since FONT resources were stand-alone resources, a new name was given to this new type of
resources in order to avoid any confusion: henceforth FONT resources that belonged to a FOND
family would be called NFNT ([50, p. IV-35, 43]). Apple took advantage of the change to add
two optional tables to the end of the resource: a new table of displacement vectors and a table
of glyph heights.
A.1.3
Color
In 1986 [51, p. V-181], after the release of the incredibly sexy Macintosh II and its wonderful
color screen, a new type of resource was added to FOND and NFNT: the fctb (font color table).
We have the choice of four levels of color: 1 (black and white), 2 (four colors or gray levels), 4
(16 colors), and 8 (256 colors, which at the time was considered the height of luxury). Whatever the number of colors may be, it always refers to indexed colors: specifically, the fctb
resource makes the connection between the indices of the colors and their actual RGB values
(in a space of 248 possible colors, since each value of red, green, or blue is a 16-bit number!).
The reader must surely be wondering, “But, if implementing beautiful colored fonts was
technically possible, why were we never inundated with them?” Well, Apple’s intention was
not so much to provide “beautiful colored fonts” as to accelerate access to fonts by making
available a system of bitmap images already adapted to the level of colors on the screen. In
other words, black and white would remain black and white; only the image would be larger,
since there would be 2, 4, or even 8 bits per pixel.
In any event, we can create such fonts, whether to speed up processing or to add gray levels, a
possible colored background, or actual colors. To do so, we must merely ensure that the fcbt
resource has the same number as the NFNT resource and that a number of flags are enabled
in the latter’s “font type”.
A.2
The DOS World
A.2.1
The CPI Format
The DOS font format is CPI (for “Code Page Information”, in the Microsoft sense; see
page 45). The peculiarity of the CPI fonts is the fact that they contain several fonts, arranged
first by code page, then by type size.
They are console fonts, therefore monospaced; what is more, they have a constant width equal
to 8 pixels (which is equal to 8 bits, or 1 byte). Usually three sizes are found: 8, 14, and 16 pixels. Each font contains exactly 256 glyphs.
```

The structure of CPI fonts [91] is quite natural: there is a global heading, then the file is
divided into sections corresponding to code pages (each with its own heading), themselves
subdivided into subsections corresponding to the various available sizes, and each subsection
again has its own heading and, finally, the bitmap data for the size in question.
The global heading is fixed:
ff 46 4f 4e 54 20 20 20 00 00 00 00 00 00 00 00
01 00 01 17 00 00 00 01 00
except for the last two bytes, which indicate the number of code pages supplied in the file (in
this case, just one; the number 1 is written in little-endian order).
Next comes a section for each code page, with the following heading:
• a fixed 2-byte number: 00 1c; a 4-byte pointer to the heading of the following code page
(or ff ff ff ff); a 2-byte number with the value 1 (screen font) or 2 (printer font);
an 8-byte ASCII string to indicate the type of screen/printer (for example, “EGA
”);
the Microsoft code-page number, written as 2 bytes: 437 (United States), 850 (“multilingual”), 863 (Canadian French), etc.; 6 null bytes; a 4-byte pointer to the next font heading,
or else 0; a fixed 2-byte number: 00 01;2 a 2-byte number: the number of fonts belonging
to this code page; the total size of these fonts.
Next come the fonts belonging to this code page. Each one is preceded by a font heading: one
byte to indicate the size (6, 8, 14, or 16), and 5 fixed bytes (00 00 00 01 00).
Finally come the bitmap data, glyph by glyph and line by line. As each line contains pixels,
therefore 8 bits, it occupies exactly 1 byte. Each glyph therefore occupies as many bytes as the
size of the font.
A.3
The Windows World
The malicious say that there is a connection between the names FNT of Microsoft and NFNT
of Apple, as well as between Microsoft’s FON and Apple’s FOND. That is not so: aside from the
fact that both cases combine a single bitmap font with a font “family”, their approaches have
very little in common.
A.3.1
The FNT Format
A.3.1.1
Bitmap FNT Fonts
FNT is a format for individual bitmap fonts. The latest update of this format dates to 1991,
which was before the advent of the TrueType format; but it already gives us a foretaste of the
parameters that we shall see a few years later in the TrueType fonts.
The reason is that the FNT fonts of Windows, unlike Apple’s NFNT fonts, are crawling with
global parameters of all kinds [45].
2 The font format described here is that of MS-DOS and PC-DOS. There are also CPI fonts for the DRDOS and Novell-DOS operating systems. Their format differs in significant ways from the one described here;
in particular, the number in question here takes the value 2.

A.3. The Windows World
• “Typographical” parameters: the optical size (!); the vertical and horizontal resolutions
for which the font was designed; the number of pixels above the baseline; two types of
leading (internal leading, which can include accents or other marks, and external leading,
which must be left white); the presence of italics, underscoring, or strikethrough; the
weight (on a scale between 1 and 1,000, with 400 being the average value); the size of the
grid on which the glyphs were designed; the average set-width; the maximum set-width;
the font’s name.
• Parameters for “organization”: the version of the format (2 for fonts meant for Windows 2
and 3 for fonts meant for Windows 3 and later); the font’s type (bitmap or vector); the
font’s copyright notice; the positions of the first glyph and the last glyph in the font table; the font’s “character set number” (8 bits); the (very rough) classification of the font
(“roman”, “swiss” [i.e., sans serif], “modern” [i.e., monospaced], “script”, “ornamental”,
and “don’t care”); finally, the “default glyph”, which is the glyph displayed when a glyph
that does not exist in the font is requested.
• A parameter for interaction with typesetting software, which affects characters rather
than glyphs: the character that the software is supposed to use as a word delimiter. This
character is the space by default, and that is how the font tells the software how to divide
the text into words.
• Parameters for managing a glyph’s width and height. A font is said to be of “type ABC”3
if three types of data are provided for each glyph: “A” equals the left side bearing, “B”
equals the width of the glyph’s bounding box, “C” equals the right side bearing. In this
way, A + B + C yields the glyph’s offset vector. The heading contains the maximum values
of these three quantities.
• Some low-level computer-related parameters: the total size of the file; the number of
bytes in each line of the bitmap image; a pointer to the font’s name; a pointer to the name
of a peripheral; the “absolute machine address” (i.e., an address within the computer’s
RAM, a highly volatile piece of data!) of the bitmap image; an internal pointer to this
same image; a number of flags indicating whether the font is monospaced/proportional
and/or of “type ABC” and/or of color level 1, 4, 8, or outright RGB; a pointer to the table
of colors; and, finally, the name of the output peripheral, if the font is intended for a
specific peripheral device.
After these parameters comes a table of widths (possibly broken down into three quantities:
A, B, C) and pointers to the bitmaps of the glyphs and to the font’s bitmap image.
Note that the pixels are organized in a way different from that of Apple’s bitmap fonts. Specifically, the glyphs are stored within the image in sequential order: the pixels of glyph n all
occur between those of glyph n−1 and those of glyph n+1. But each glyph is not necessarily
filled in from top to bottom for its entire width; rather, columns of a fixed width (given as a
parameter in the font’s heading) are used.
3 We can only admire the imagination of the developers at Microsoft who came up with this name, which
has absolutely nothing to do with what it represents.

A.3.1.2
Vector FNT fonts
There are also “vector” FNT fonts, but the author, despite his many efforts, has not been able
to find documentation for them. They are outline fonts: only the outlines are displayed; they
are not filled in. The thickness of the outline depends on the display device; usually it is one
pixel, giving these fonts very thin strokes. Three of these fonts have survived in Windows 2000
and XP: Modern, Roman, and Script.
A.3.2
The FON Format
Since 1992 [304], Windows has used the concept of resources, which are similar to the resources of the Mac and of X Window. Resources are compiled by a special tool that reads a
resource-description file (extension .rc) and a number of binary files needed to create the
resources.
Thus the FNT files examined above become “font resources”; for that purpose, we need
only prepend to them a resource heading. By grouping several of these resources together and
adding to them a “font directory” resource, we obtain a FON file.
A.4
The Unix World
A.4.1
The PSF Format of Linux
The acronym PSF stands for “PC Screen Font”. This font format is peculiar to Linux and is
used only for monospaced fonts meant for on-screen display. It was defined in 1989 by Peter
Arvin for his DOS font editor, fontedit. Later adopted by Linus Torvalds for Linux, it was supplemented with Unicode tables in 1994 and, finally, was updated in version 2 of 1999.
Version 1 of the PSF format is of a childlike simplicity. It begins with a 4-byte heading, in
which the first 2 bytes are fixed (0x3604), the third contains three flags (does the font contain
256 or 512 glyphs? does it have a Unicode table? does this table contain character sequences?4),
and the fourth contains the height of the glyphs in pixels. Next come the bitmap images of all
the glyphs, described in the following manner: the width being fixed at 8 pixels (one byte),
each glyph is described row by row, and thus needs as many bytes as there are pixels in its
height.
The heading in Version 2 of the PSF format is slightly longer (32 bytes, or even more), since
this version considerably extends the preceding one: the number of glyphs is arbitrary (encoded as 4 bytes), and the height and width of the glyphs are configurable. Here is this heading
(made up of eight 4-byte numbers):
• A fixed value (0x72b54a86)
• The version (0x00)
• The size of the heading (to allow for later versions with longer headings)
4 By Unicode character sequences, we mean a Unicode character followed by at least one combining character.

A.4. The Unix World
• Flags (only one is used at present: does the font have a Unicode table?)
• The number of glyphs
• The number of bytes used for each glyph
• The maximum number of rows of pixels for each glyph
• The maximum set-width of a glyph, in pixels
To calculate the number of bytes used for each glyph, we take the glyph’s width in pixels,
round it to obtain whole bytes, and multiply by the number of rows.
A.4.1.1
The Unicode table
The most attractive property of PSF fonts is without a doubt the possible presence of a Unicode table, to the point that we have developed the habit of assigning the extension .psfu to
PSF fonts that have a Unicode table and .psf to those that do not. We shall see that there are
tools for equipping PSF fonts with Unicode tables.
The Unicode table immediately follows the bitmap image of the final glyph. Its structure is
as follows: There are as many entries as glyphs. Each entry consists of:
1. Zero, one, or more Unicode characters, represented either in UCS-16LE (2 bytes, littleendian) for version 1 of PSF or in UTF-8 for version 2.
2. Zero, one, or more Unicode sequences. The characters are represented in the same way
as in (1). Each sequence is preceded by a “sequence initiator” (0xfffe in version 1 of PSF,
0xfe in version 2).
3. An entry terminator (0xffff in version 1 of PSF, 0xff in version 2).
Thus, for example, the glyph ‘Ÿ’ might have the following entry in a Unicode table (PSF
Version 1):
0x0178
latin capital letter y with diaeresis
0x03ab
greek capital letter upsilon with dialytika
0xfffe
sequence initiator
0x0059 0x0308
latin capital letter y followed by combining diaeresis
0xfffe
sequence initiator
0x03a5 0x0308
greek capital letter upsilon followed by combining diaeresis
0xffff
entry terminator.
To obtain the entry in Version 2 of PSF, represent the Unicode characters in UTF-8 and replace
the initiators and terminators with the corresponding one-byte values.
The utilities psfaddtable and psfgettable, which are included in practically every Linux distribution, allow the user to add the Unicode table to a PSF font and to retreive the table from
the font. The text-based version of the required Unicode table (or the table thus obtained)
is in the following format: For each glyph, one line of text is written, which includes some

integers—the first number, written in decimal, octal (preceded by a 0), or hexadecimal (preceded by 0x) notation, indicates the glyph’s position in the font, and the other numbers (in
U+hhhh notation) indicate the corresponding Unicode characters. When there is a sequence,
the base character is separated from the combining characters with commas. Lines beginning
with a crosshatch (#) are comments.
For example, the line corresponding to the sample entry that we gave above would be
# Y WITH DIAERESIS
0x0178 U+0178 U+03ab U+0059,U+0308 U+03a5,U+0308
The utility psfstriptable will delete the Unicode table from a PSF font.
A.4.2
The BDF Format
As astonishing as this may seem, the BDF format, which is the basis for practically all Unix
fonts, was defined by Adobe, a company that we do not usually associate with this operating
system. BDF is a doubly deceptive acronym: the ‘F’ stands not for “font” but for “format”, and
the ‘B’ stands not for “binary” but for “bitmap”: “bitmap distribution format” (yes, you read
it correctly: the word “font” does not appear).
According to the first paragraph of the documentation [8], this format was intended to be
nothing more or less than “easily understandable by both humans and machines”. Indeed,
what is the most striking is the fact that everything is written in pure ASCII, according to the
“keyword/values” schema, with one keyword per line.
The global structure of the font is in no way surprising: first come the global parameters,
then come the descriptions of the glyphs. The most important keys in the first section are
the following:
• STARTFONT followed by the version number of the format: either 2.2 (the latest official
version, dating to March 22, 1993) or 2.3 (an extension of the BDF format by Microsoft
to support glyphs with a gray scale, [349]).
• FONT followed by the name of the font. This name, according to Adobe, must be identical
to the font’s PostScript name, if one exists.
• SIZE followed by three numbers: the actual size and the horizontal and vertical resolutions of the device for which the font was designed.
Note that in version 2.3 of these fonts, this keyword takes a fourth parameter: the number
of bits per pixel (1, 2, 4, and 8, corresponding to 2, 4, 16, or 256 gray levels).
• FONTBOUNDINGBOX followed by four numbers: the font’s bounding box.
• METRICSSET followed by a number selected from 0, 1, and 2. Here is what the numbers
mean: 0, which is the default value, indicates that the font is horizontal; 1 indicates a
vertical font; and in the case of 2, the font can be used in both directions.
• SWIDTH, SWIDTH1, DWIDTH, DWIDTH1, VVECTOR: the default metrics (see below for their descriptions).

A.4. The Unix World
• ENDFONT, the end of the file.
Aside from these properties defined in the BDF specification, a font can contain an arbitrary
number of “properties”, which are any keywords followed by values. It is good practice to
use for those properties those of the X logical font description XLFD (see Chapter 8, page 222).
Specification 2.1 of BDF [354] even recommends the use of the properties FONT_ASCENT,
FONT_DESCENT, and DEFAULT_CHAR.
These global properties of the font must be surrounded by the lines STARTPROPERTIES (followed by the number of properties) and ENDPROPERTIES.
Next comes the section for the description of the glyphs, which begins with a CHARS line (followed by the number of glyphs) and ends with the line ENDFONT.
Each glyph contains the following keywords:
• STARTCHAR followed by the name of the glyph. Adobe recommends the use of the same
glyph name or CID number as in PostScript fonts.
• ENCODING followed by one or two numbers. Here Adobe shows itself viciously lacking in
political correctness by favoring its own font encoding, Adobe Standard (see page 660), a
font encoding known not to contain any accented letters. If the glyph in question belongs
to the Adobe Standard set of glyphs, then the keyword ENCODING is followed by its position in this table; if, however, the glyph is not present in that set, the keyword is followed
by the number −1 and then the position of the glyph in the other encoding. Note that
we are never allowed to specify the name of the other encoding, whose only shortcoming
is that it is not Adobe Standard.
• ENDCHAR, the end of the glyph’s description.
and two types of metric properties (see Figure A-2):
1. Metric properties at the pixel level:
• DWIDTH, followed by two whole values: the coordinates of the glyph’s primary displacement vector (called “horizontal” in the specifications). As a vector, it can, in
principle, be at an angle rather than strictly horizontal. Nonetheless, Adobe persists
in calling it “horizontal”. This displacement vector starts from the glyph’s primary
origin.
• DWIDTH1, followed by two whole values: the coordinates of the glyph’s “vertical” displacement vector. As in the previous case, verticality can be relative. This vector starts
from the glyph’s secondary origin, which is used for vertical typesetting.
• BBX, followed by four whole values (BBw, BBh, BBxo, BByo): a “bounding box” whose
definition is different from that of the bounding boxes of PostScript fonts. In the
present case, we first write the width and the height of the glyph’s envelope, then the
horizontal and vertical offsets of its lower left pixel relative to the origin.
• VVECTOR, followed by two whole values: the coordinates of the vector that starts at
the primary origin and ends at the secondary origin.

.......*.o.........
.......***.........
...*..**....*......
...***********.....
...*.........*.....
...***********.....
...*.........*.....
...***********.....
...*........**.*...
...***************.
...*...........*...
...**************..
.*.*..*....*...**..
.***..*....**..**..
.*....*....*...**..
.***********...**..
o*.........**.**...
.*.........*.***...
.*...........*.....
BBw (17 pixels)
BBxo (1 pixel)
BByo (–3 pixels)
BBh (19 pixels)
VVECTOR (10 × 17 pixels)
DWIDTH1 (0 × –19 pixels)
DWIDTH (19 × 0 pixels)
SWIDTH 1000 0
SWIDTH1 0 -1000
Figure A-2: BDF’s vision of the bitmap and vector versions of a single ideographic character, with all the
associated metric properties.
2. Metric properties established on a grid of 1,000 × 1,000 units (similar to that of the
PostScript fonts):
• SWIDTH, the equivalent of DWIDTH, but with the greater precision of the new grid
• SWIDTH1, the equivalent of DWIDTH1
The mixing of values in pixels with “abstract” values is bound to make display or printing
more precise when the screen or printer has a higher resolution than the font. Even better, if
the bitmap font is accompanied by a vector font, and therefore the values SWIDTH and SWIDTH1
are those of the widths of the vector glyphs, then the typesetting software can work on two
levels: it can use DWIDTH (or DWIDTH1) for display on screen with the bitmap font and SWIDTH
(or SWIDTH1) to define with precision the PostScript code sent to the printer, which will use
the corresponding vector font.
Finally comes the glyph’s bitmap image:
• BITMAP, on a line by itself, followed by as many lines of text as the glyph contains rows
of pixels. Each line contains the values of the pixels encoded as hexadecimal numbers, to
which we add null bits (at the right) to obtain full bytes.
For example, if we have the row ..**.* (6 pixels), and therefore the binary value 001101,
we add two zeroes at the right, 00110100, to obtain the hexadecimal number 0x34.5
Note that if the font format used is 2.3, the pixels in the image can be at a gray scale
(2, 4, or 8 bits per pixel: 4, 16, or 256 gray levels). In this case as well, we write the bits as
hexadecimal numbers. For instance, the same number 0x93 = 10010011 can, according
5 The advantage of this notation is that with a little Perl program like while (<>) { s/([0-9A-F][0-9AF])/sprintf("%08b", hex(\$1))/ge ; tr/01/.*/ ; print ; } we can convert the hexadecimal numbers
into series of dots and asterisks, as in Figure A-2.

A.4. The Unix World
to the number of gray levels, represent 8 black-and-white pixels *..*..**, or 4 pixels at
4 gray levels (with the values 2, 1, 0, 3), or 2 pixels at 16 gray levels (9, 3), or 1 pixel at
256 gray levels (147).
A.4.3
The HBF Format
The acronym HBF comes from Hanzi Bitmap Font, where “hanzi” is the transcription of 漢
字, which means “Chinese character”, a name used not only in Chinese but also in Japanese,
Korean, and old Vietnamese for the ideographic characters common to these languages (with
a few minor differences). HBF [296, 295] was developed by four Chinese researchers (one
from Hong Kong and three from the United States) in order to optimize the use of disk space
and memory by storing in separate files, which could be loaded into memory or not, as the
application required.
The idea is very simple: since the glyphs of the ideographic scripts all have exactly the same
dimensions, we can eliminate the bounding boxes and other data on width, height, etc. Even
better, since the bitmap image of each glyph occupies exactly t bits, we can include all the
glyphs, concatenated together, in a single image file: the nth glyph will appear at position nt
in the file.
But the positions of the glyphs in the font table are not always contiguous; on the contrary,
many East Asian encodings include structures in subblocks that contain the glyphs. For example, the Taiwanese encoding Big5 contains two subblocks: 0x40-0x7e and 0xa1-0xfe; any
2-byte code outside these subblocks is not valid in the encoding. This property is supported
in the HBF format through the following keywords:
• HBF_START_BYTE_2_RANGES, followed by a whole number: the number of valid subblocks;
• HBF_BYTE_2_RANGE, followed by a range of hexadecimal numbers in uppercase (for example, 0x40-0x7E): one such block;
• HBF_END_BYTE_2_RANGES, the end of this section;
• Note that the same keywords with a 3 in place of the 2 are provided for 3-byte encodings.
But, again, not all the valid positions will necessarily contain glyphs. We must therefore be
more precise and determine which parts of these subblocks actually contain glyphs. That is
what HBF does, through the use of the following keywords:
• HBF_START_CODE_RANGES, followed by a whole number: the number of contiguous sections with glyphs.
• HBF_CODE_RANGE, followed by a range of hexadecimal numbers in uppercase, a filename,
and a whole number. This is the most important keyword in HBF: the range designates
the positions of the glyphs contained in the file, the number indicates the position of the
offset of the first glyph in the range, starting at the beginning of the file. Thus, by writing
HBF_CODE_RANGE 0xA140-xA3E0 spcfont.24 0
HBF_CODE_RANGE 0xA440-xC67E stdfont.24k 0
HBF_CODE_RANGE 0xC940-xF9FE stdfont.24k 388872

we employ two fonts (spcfont.24 and stdfont.24k), of which the second contains contiguous glyphs, with the exception of a hole (the glyphs from 0xc67f to 0xc93f are missing); thus we invoke this file twice, the second time with an offset directly addressing
glyph 0xc940.
• HBF_END_CODE_RANGES, the end of the section.
The other keywords in HBF are:
• HBF_START_FONT, followed by the version of the format (currently 1.1): it replaces the
STARTFONT keyword of BDF.
• HBF_CODE_SCHEME, followed by the name of the encoding being used. The values provided
are GB2312-1980 (Chinese); Big5 (Taiwanese); Big5 ETen 3.10 (the Big5 encoding with
additions by the Taiwanese company ETen 倚天資訊); CNS11643-92pi, with i between 1
and 7 (Taiwanese), Unicode
1.1 (the only one available at the time), JISX0208-1990
(Japanese), and KSC5601-1987 (Korean).
• HBF_BITMAP_BOUNDING_BOX, followed by four whole values: a stricter version of BDF’s
FONTBOUNDINGBOX (see [296, section “Bounding Boxes”]).
• HBF_END_FONT: the end of the file.
Note that this bitmap font format can be used only for monospaced fonts, such as ideographic
fonts. The reduction in space is impressive: a Chinese font at 24×24 pixels takes up 550 kB in
HBF (of which 1.6 kB is for the HBF specification file and the rest is for bitmap image files),
961 kB in PCF, and 1.935 MB in BDF.
A.4.4
The SNF, PCF, and ABF Formats
The SNF font format (for “Server Normal Format”), which has been consigned to history,
was the first attempt at “compressing” BDF fonts, until Version X11 R4 of X Window. Its
peculiarity was that it depended on the platform (byte format, size of numbers, etc.). Thus
there were as many different SNF formats as manufacturers of Unix workstations: NCD,
Hewlett-Packard, IBM, DEC, SCO, Sun Microsystems, and so forth. Rather than converting
SNF formats among themselves, the method used was to go through the BDF format by decompiling (with the snftobdf utility) and recompiling (bdftosnf).
The X Consortium took advantage of the change from X11 R4 to R5 in 1991 to change its font
format radically. Since the biggest drawback of the SNF format was that it depended on the
platform and was therefore not portable, what was more natural than to adopt a new portable
format that nonetheless remained compiled? PCF, accordingly, stands for Portable Compiled
Font. To obtain PCF fonts, we can use the tools pcftobdf and bdftopcf.
When Adobe finally took up the BDF format, in 1992, it wanted to issue its own version of
a binary format associated with it. The result was ABF (for “Adobe Binary Font”).
We shall not describe the internal structure of these three formats: they contain no more or
fewer data than the BDF fonts that were used to create them; the information is merely stored
in a more compact manner.

```text
A.5. The TEX World
As for the SNF format, a description is given in issue 2 of the journal The X Resource [251].
For more information, one may also consult the source code of the X 11 R 6.4 distribution—
more specifically, the modules for reading SNF fonts [46].
For the PCF format, the situation is a bit better, since, beyond the corresponding source-code
modules [285], which are, after all, the final authority, there is also the attempt of George
Williams [350] to describe the format.
Finally, the ABF format, given its origins, is the only one that is perfectly described in a publicly available document, an Adobe technical note [3]. Yet, while there are clearly a great
many SNF fonts and vastly more PCF fonts in the world, the author has never seen a single
ABF font.
A.4.5
The RAW and CP Formats
To bring the section on Unix to a close, let us discuss two obsolete formats that have long
since been forgotten: RAW and CP.
RAW has at least one big point in its favor: it is the simplest bitmap font format. It contains
only the bitmap images of the glyphs, without any sort of heading or escape character!
Here is a little riddle: if there is no heading, how on earth does the system know how to find
a given glyph in the font? Answer: the width of the glyphs is always 8 pixels. There are always
exactly 256 glyphs. If the height of each glyph is h pixels, the file necessarily contains 8×256×
h bytes. Conversely, if the size of the file is T, the height, h, of the font is necessarily
T
8×256, and
the ith glyph appears in position i×8×h in the file. Elementary, my dear Watson!
The CP format is another story altogether. Yann Dirson (of Debian) [120] has called it an
“awful thing” and a “horror”. It is a stripped-down version of DOS’s CPI format with a unique
code page (see §A.2.1). A CPI font ordinarily contains multiple code pages (in the Microsoft
sense; see page 45) of fonts. The codepage utility (whose name could lead to confusion) will
extract as many fonts from the CPI file as there are code pages. For example, if we assume
that we have a CPI file ega.cpi and that we execute
codepage ega.cpi -a
we will obtain the fonts 850.cp, 437.cp, and so on for each code page contained in the CPI
file. These fonts can then be used as Linux console fonts by running them through the utility
setfont.
A.5
The TEX World
Appendix B of this book deals with the real and virtual metric data of TEX and Ω. But TEX long
used bitmap fonts, compiled from font descriptions written in the METAFONT programming
language (see Appendix F). In this section, we shall discuss the bitmap formats defined by
Knuth and his students for the needs of TEX.
```

A.5.1
The PXL and CHR Formats
Unlike humans, who learn languages as they grow up, METAFONT was born speaking several
languages, which she later forgot. For instance, in 1983, METAFONT6 was able to produce
fonts in FNT (nothing to do with the Windows FNT format; these were fonts for the Xerox Graphics Printer), VNT (for the Varian Versatec printer), ANT (Alphatype CRS), RST
(Canon), OC (Dover), and WD (PrePress).
It quickly became clear that it would be more practical to have a single bitmap format and to
generate the data on the fly from this generic format, whether the task be on-screen display
or printing. That became a reality in November 1981, when David Fuchs announced the PXL
font format [145].
The PXL format (the abbreviation comes from the word pixel) is a variable-width bitmap
format without compression: the glyphs are described by bitmap images, and at the end of
the file there is a table of metric data. PXL had two main drawbacks: a font could contain no
more than 128 glyphs, and the lack of compression made the size of these files substantial for
large type sizes or high-resolution printers.
Just as TFM and VF (see Appendix B) can be converted to a human-readable format and
vice versa without loss of data, PXL can be converted to one such format, by the name of
CHR (a poorly chosen name, as it comes from “character”, whereas glyphs are being discussed
here). As we frequently do in this book when a “humanized” format exists, we are going to
employ this format here instead of the binary format, which is of interest to no one but the
machine. The utilities for converting PXL to CHR and vice versa are pxtoch and chtopx.
The CHR format contains a global heading followed by descriptions of glyphs, each of them
preceded by a glyph heading. Here is an example of a global heading for the font Computer
Modern Roman, 10 points, generated for a 360-DPI printer:
Font file info :
Number of char :128
Checksum
:1274110073
Magnification
:1800
Design size
:10485760
Directory ptr
:4547
Pixel Id
:1001
Max height
:50
Max width
:49
A few words of explanation:
• Since 200 DPI is, in a sense, the “default” resolution of the system, we can say that a 360DPI font is a “standard font” to which we have applied a magnification factor of 1.8. The
value of magnification is this factor multiplied by 1,000.
6 We are referring, of course, to METAFONT78, the ancestor of the current METAFONT, which was written
in the proprietary language of the SAIL system. The interested reader can find all the SAIL files for the TEX and
METAFONT projects in [43].

A.5. The TEX World
• The design size is expressed in 220-ths of an American printer’s point; in our case, we have
a value of 10,485,760, which, when divided by 220, gives us 10 points.
• Directory ptr is a pointer to a table of metric data in the PXL file; this information is useless, as chtopx recalculates the pointer.
• Pixel Id is the signature of this version of the font format.
And here is the complete description of the glyph ‘a’:
chrcode
:141
height
:24
width
:22
right
:22
left
:1
depth
:2
x offset
:-
y offset
:22
tfm width
:524290
raster width
:24
internal width :22
right kerning
:22
top
:1
bottom
:24
data row count :24
-+
.....******...........
...**.....***.........
..*........****.......
.****.......***.......
.*****......****......
.*****.......****.....
.*****.......****.....
..***........****.....
.............****.....
.............****.....
.........********.....
......****...****.....
....***......****.....
..****.......****.....
..***........****.....
.****........****.....
****.........****....*
****.........****....*
****.........****....*
****........*****....*
****........*****....*
.****......*..****..*.
:..****....*...*******.
....******......****..
In the header, chrcode gives the position of the glyph in the table, in octal notation. tfm width
gives the width of the glyph in the corresponding TFM file; it is calculated in 220-ths of an
American printer’s point.
In the image shown beneath the heading, the characters - and : are the projections of the
glyph’s origin onto the coordinate axes. The character +, on the other hand, indicates the
point (−1,−1) in the bitmap image (whose origin is the upper left corner).
A.5.2
The GF Format
When Donald Knuth set about rewriting TEX and METAFONT in Pascal-WEB, he also addressed
the problem of bitmap fonts. Drawing his inspiration from DVI (the format for “generic”
page description), he created a format for “generic” fonts that is structured like a DVI file.

This format is called GF (for “generic font”) [216, pp. 484-489], and it remains to this day the
output format of METAFONT.
A GF file contains operators and values thereof; each operator is represented in the file by a
1-byte value (which the reader will find in [216, pp. 484-489]). Globally, the file consists of a
preamble, the description of the glyphs, and a postamble.
The preamble is as follows: the pre operator, followed by two parameters, the second being a
string of comments less than 256 characters long and the first being the string’s length, stored
in a one-byte value.
Each glyph description begins with a boc operator and ends with an eoc. The boc operator takes
six parameters: the glyph’s position in the table (4 bytes: thus there can be 4 billion glyphs in
a font, the world record!), a pointer to the glyph in the same position in the previous plane,
which takes the value −1 if the plane does not exist,7 and then the dimensions of the grid
containing the glyph.
Now we have come to the description of a glyph. At any moment there is a “current color”:
white or black. Here are some of the most important operators:
• The operator paint_0 permutes the current color.
• The operators from paint_1 to paint_63 paint the following 1 to 63 pixels in the current
color and then switch from black to white or from white to black.
• The operator skip0 moves to the following line and changes the current color to white.
• The operator skip1, followed by a 1-byte number n, skips n rows and switches to white.
• The operator new_row_0 skips a row and changes to black.
• The operators from new_row_1 to new_row_164 move to the following line, skip from 1
to 164 pixels, and switch to black.
• The operator xxx1, followed by two parameters (the second of which is a string of fewer
than 256 characters and the first of which is the length of this string), is a “special”, i.e., an
external block of code that can be read and processed by certain software (for example,
it might contain PostScript code).
• The operator yyy1, followed by a 4-byte number, is used by METAFONT to incorporate
into the code for a glyph the numbers of the points defined in the code.
Finally, the postamble, which begins with a post operator followed by nine parameters. These
nine parameters include the font’s optical size, a checksum, the proportions of the pixels (if
7 An explanation is in order. Years before the valiant developers of Ω set about implementing them,
Knuth had already planned for fonts with more than 256 glyphs. But to him a font of that sort would be useful
only for the ideographic languages, and it is well known that all the glyphs in those languages have the same
dimensions. Thus he dreamed of a GF font with several “planes” of 256 glyphs, all of them obeying a single TFM
file with 256 positions. The parameter in question in the GF file is used to leap from one plane to another. The
least that we can say is that these fonts were never really implemented, so the parameter has very seldom been
used. There is another operator, boc1, which eliminates this parameter by assuming that it has the value −1.

```text
A.5. The TEX World
they are not square), and the dimensions of the global grid that incorporates all the grids of
the glyphs.
The post operator is followed by a series of char_loc operators, which point to the start of each
glyph’s description in the file. These operators take five parameters: the glyph’s position in the
table; the coordinates of the glyph’s displacement vector;8 the exact set-width of the glyph, as
defined in the TFM file; and, finally, the pointer to the boc operator at the beginning of the
glyph’s description.
The postamble ends with a postpost operator followed by a pointer to post, a number indicating the version of the format, and as many instances of 0xdf as needed to make the size of
the file a multiple of 4 bytes.
Thus we can see that the GF format is very different from all the bitmap formats of the era,
and even from those of today. We can raise questions about the efficiency of the process:
on the one hand, the interpretation of the operators requires processing that is too complex
for direct display; on the other hand, the compression achieved by these operators may be
attractive at the level of each row, but nothing is done for identical rows that are repeated.
Nevertheless, that remains fertile ground for experimentation.
The program gftype allows for debugging GF fonts by generating a human-readable list of the
operators used to describe each glyph. Here, for example, are the beginning and end of the
description of the glyph ‘a’ in the font Computer Modern Roman 10:
4101: beginning of char 97: 2<=m<=27 0<=n<=23
(initially n=23) paint (5)9
4109: newrow 3 (n=22) paint 2(7)4
4113: newrow 2 (n=21) paint 4(8)3
4117: newrow 2 (n=20) paint 5(8)3
4121: newrow 2 (n=19) paint 5(8)4
4125: newrow 2 (n=18) paint 5(9)4
4129: newrow 4 (n=17) paint 1(11)4
4133: newrow 16 (n=16) paint 4
4135: newrow 16 (n=15) paint 4
4137: newrow 16 (n=14) paint 4
4139: newrow 9 (n=13) paint 11
4141: newrow 6 (n=12) paint 5(5)4
...
4179: newrow 0 (n=4) paint 5(10)5(4)1
4185: newrow 1 (n=3) paint 4(10)5(4)1
4191: newrow 1 (n=2) paint 5(8)1(1)5(2)2
4199: newrow 3 (n=1) paint 4(5)2(3)7
4205: newrow 5 (n=0) paint 7(7)4
4209: eoc
8 Note that the displacement vector may be vertical, or even oblique, whereas TEX moves only horizontally while setting type.
```

.<--This pixel's lower left corner is at (2,24) in METAFONT coordinates
*********
**
****
****
***
*****
***
*****
****
*****
****
*
****
****
****
****
***********
*****
****
*****
****
****
****
****
****
*****
****
*****
****
*
*****
****
*
*****
****
*
*****
*****
*
****
*****
*
*****
* *****
**
****
**
*******
*******
****
.<--This pixel's upper left corner is at (2,0) in METAFONT coordinates
In the code, the numbers at the beginning of each line refer to positions in the file, and
newrow * refers to a new_row_* operator that begins a new row and leaves a certain number
of pixels white. In addition, paint refers to a series of paint_* operators, where the numbers
in parentheses are white pixels and the other numbers are black pixels.
Unfortunately, gftype, as its name suggests, is not a tool for conversion without loss of information but rather a tool for debugging. It is not possible to capture its output and generate a GF
font from it.
Another very appealing tool (and, for some people, the major attraction of the GF format)
is gftodvi. Provided that we have used the METAFONT command labels for all the points on
the outline and that we have generated a GF file with a strictly positive value to the proofing
value and a sufficiently high resolution, gftodvi will produce, from the GF file alone, a DVI
file with as many pages as there are glyphs in the font. On each page, we find a rather large
and very precise copy of the glyph on which all the “labeled” points are also identified. And
if there are points that are too close to existing points, a list of them is shown separately, with
their coordinates relative to the nearest points.
In Figure A-3 we see the glyph ‘a’ of the font Computer Modern Roman at an optical size of 10,
the result of the following manipulations:

```text
A.5. The TEX World
Figure A-3: A page from the DVI file produced by gftodvi from the font Computer Modern Roman 10, at
5,203 DPI.
mf "\mag:=2; input cmr10"
gftodvi cmr10.5203gf
dvips -D 300 -p 27 -l 27 -E cmr10.dvi
(Because no mode is indicated, METAFONT has used the proofing mode, which usually produces fonts at 2,602 DPI. Thanks to mag:=2, we have achieved a resolution of 5,203 DPI. Next,
gftodvi produced a DVI file cmr10.dvi, of which we have converted only page 27, corresponding to the glyph ‘a’, to EPS. The parameter -D 300 of dvips is present for this reason: in the
DVI file, a very special font by the name of gray is used to achieve the gray shading effect. For
Figure A-3, which, in any case, was going to be reduced for inclusion in this book, using the
gray font at a very high resolution turned out to be pointless; thus we imposed a resolution
of 300 DPI for this font. This restriction does not affect the other fonts on the page, which are
all vector fonts.)
A.5.3
The PK Format
The latest in the saga of bitmap formats for TEX, PK was announced to the world by Tom
Rokicki (student of Knuth and developer of dvips) in 1985 [306, 305]. PK solves the main
```

problems of the GF format: its complexity and its size. The description of a glyph is no longer
a series of operators that must be interpreted but a pre-structured block of code, similar to
the other bitmap font formats. What distinguishes PK from the other formats studied in this
chapter is the fact that it is compressed (incidentally, the acronym PK comes from packed).
The method of compression chosen for the PK format is simple and efficient: average compressions of 60 to 65 percent over GF files are achieved. It is RLE (run-length encoding) compression, and its principle is very simple: if there are, for example, 57 black pixels, instead of
57 bits (= almost 8 bytes), we write the number 57 (which can be encoded with 6 bits) followed
by the black pixel (1 bit), which saves us 50 bits. But the question is: are there often glyphs
with so many consecutive pixels? The answer is no, and that is why the RLE compression used
in the PK format is adapted to the needs of each glyph.
Here is how it is done. (Warning: The description of the format in [306, 305] is a bit hard to
understand.)
• We have seen that the GF format encodes the rows of a glyph as a series of numbers that
indicate alternately the number of black pixels and white pixels. Here we shall go a bit
farther: we shall also encode repeated rows while concatenating all the rows into one. For
instance, if the glyph
......***......
...***...***...
...***...***...
......***......
is encoded
(6) 3 (6)
(3) 3 (3) 3 (3)
(3) 3 (3) 3 (3)
(6) 3 (6)
in GF (the numbers in parentheses being the white pixels), then in PK it will be (6) 3
(9) [1] 3 (3) 3 (9) 3 (6), where the [1] means that the current row is repeated
once. To understand this notation, let us proceed step by step. First of all, we detect the
repeated rows:
......***......
...***...***... [1]
...***...***...
......***......
Next, we describe the first row and the beginning of the second, up to the first transition
between black and white on the line that will be repeated:
......***......
...

A.5. The TEX World
That already gives us (6) 3 (9), and it is at that point that we insert the information on
the repetition of a row [1]. Henceforth we act as if the repeated row did not exist (we are
between the third and fourth pixels of the second row):
......***......
...***...***...
......***......
and thus we continue with 3 (3) 3 (9) 3 (6).
• Now that we have a new representation of the glyph ((6) 3 (9) [1] 3 (3) 3 (9) 3
(6)), we must merely encode it in RLE.
• We decide to work not at the level of bytes or bits but at the level of nybbles (4 bits). We
can see that we have two types of information to encode: the repetition of rows, and the
number of black (or white) pixels in sequence. Already we need a kind of flag to indicate
which type of information will follow.
• Since a nybble consists of 4 bits, it can take values between 0 and 15. We therefore decide
that the value 15 indicates that the current line is repeated once ([1] in the glyph’s representation). Moreover, the value 14 of the nybble, followed by a “packed number” N (we
shall see what it is below), means that the current row is repeated N times (= [N]).
• All that remains is to encode the pixels, and that is where the procedure turns interesting.
We can say that the value 1 of the nybble means “1 pixel”; the value 2, “2 pixels”; etc. But
we can also say that we are switching to bytes and that the first nybble is in fact multiplied
by 16 and added to the second one. The first method is efficient for encoding small values;
the second will be more efficient for large ones. We decide to use both, but then the
question arises: when do we switch from the “1-nybble” schema to the “2-nybble” one
(or to one for even more nybbles)?
Rokicki answered this question by giving an algorithm (by Knuth) that calculates a
“magic” number: the value beyond which we move from 1 to 2 nybbles, and which gives
the best compression. Rokicki’s idea was to recalculate this number for each glyph.
For instance, if M is the magic number for the current glyph, the sequences of 1 to M
pixels will be encoded as a single nybble (whose value is between 1 and M), and sequences
of M + 1 to (13−M) ∗16+ M pixels will be encoded as 2 nybbles (the first of which will
take the values between M +1 and 13). Finally, the value 0 of the nybble will be used for
sequences of more than (13 −M) ∗16 + M pixels, which will be encoded with “packed”
numbers.
• What is a “packed” number? Here the principle is the same as in the UTF-8 encoding: we
use “escape sequences” to indicate the number of nybbles to follow. The escape sequences
are null nybbles: 1 null nybble indicates that there are 2 nybbles to follow, 2 null nybbles
indicate that there are 3 nybbles to follow, and so forth.
Let us point out that if we apply the method above to our example (supposing that the magic
number is greater than or equal to 9), we obtain 6 3 9 F 3 3 3 9 3 6, thus 10 nybbles
(5 bytes). Since the PXL format would have required 48 bits (6 bytes) for the same bitmap,

we can see that the gain is not huge. For even smaller glyphs (or glyphs without repetition),
compression in RLE could even be negative. In that case, the PK format allows the glyph to
be represented in PXL. When that occurs, the “magic number” is equal to 14.
Thus we see that everything has been done so that the bitmap for each glyph will be encoded
as efficiently as possible, by choosing the “magic number” on the fly and even abandoning
compression when it does not have the desired result.
In conclusion, here is a description of the PK format itself:
• The principle of GF (itself borrowed from the DVI format) is used: there are operators
and their values. Only the operators xxx (“specials”), yyy, pre, and post are retained from
the GF format. Placing xxx or yyy inside glyphs is prohibited.
• Each glyph is represented in the manner described above and is preceded by a heading.
• This heading contains the following parameters: the “magic number”, the length of the
glyph’s description (including the heading), the glyph’s position in the table, the setwidth (drawn from the TFM file), the horizontal displacement vector, the width and
height of the glyph’s image, the horizontal and vertical offsets of the image relative to the
origin. Each of these values takes up 1 byte (except the TFM set-width, which takes 3). If
the values of these parameters are larger, longer forms of headings may be employed.
• The first byte of the heading plays a special role: its first nybble contains the “magic number” (which is 14 if the glyph is encoded in PXL), the next bit indicates whether the glyph
begins with a black or a white pixel, and the bits after that indicate whether the short
version of the heading or one of the longer versions is being used.
A.5.4
Fonts or Images? Both!
One interesting application of the PK
 

 

 

 

format is the utility bm2font, by Friedhelp
Sowa, developed between 1989 and 1993.
The goal is to segment an image (GIF,
TIFF, PCX, etc.) into small square blocks
and to store these blocks in a font as
glyphs. That may seem incongruous to
us today, but in the late 1980s, when the
PostScript language was not as common
as it is today, there was a big problem of
compatibility between DVI drivers and
image formats. By creating a PK font
instead of an image, we were assured of
having printed output, though the quality
be inferior. Whereas if we supplied a bitmap to a driver that did not know how to interpret
it, we had no chance of producing an image.
The photos of Ernestine and Danae above were processed by bm2font from TIFF images at
gray levels and at a resolution of 300 DPI. Each image is built up from 12 glyphs distributed
over two PK fonts. Here are the command lines that were used:

A.6. Other Less Common Bitmap Formats bm2font -b1 -fernestine -x8 ernestine.tif bm2font -b1 -fdanae -x8 danae.tif in which -b1 reduces the number of gray levels by half in order to brighten the image, - fernestine causes the creation of font files and TEX files named ernesti* and danae* (because of the limitations on the length of DOS filenames), and -x8 indicates the number of bits per pixel (here there are 8 bits, yielding 28 = 256 gray levels). There is a range of other options that the reader will find in the documentation for the tool [319]. A.6 Other Less Common Bitmap Formats Other bitmap formats exist. Usually they are connected to hardware manufacturers. For instance, the Hewlett-Packard printers, at one time, used a font format called HP Soft Font [176, Chapter 7], with the file extensions .sfp (‘p’ for “portrait”) and .sfl (‘l’ for “landscape”). Why did we need two different formats for portrait mode and landscape mode? Because these printers’ page-description language (called “PCL”) did not by default support the automatic rotation of glyphs when we switched from one printing format to the other. Being accustomed to the PostScript language, we no longer think about problems of this kind. A.7 Whoever Can Do More Can Also Do Less Finally, some vector formats can also be used to contain bitmap fonts. That is the case for PostScript Type 3 and TrueType, OpenType, and AAT fonts. PostScript Type 3 fonts are used, for example, by dvips to incorporated TEX’s PK fonts into PostScript code. dvips generates temporary fonts in which the operator BuildChar uses the operator imagemask, which takes a bitmap in the form of a hexadecimal string and displays it (§C.2). TrueType, OpenType, and AAT fonts often contain bitmaps for the most common sizes for on-screen display. These bitmaps are managed by the tables EBLC and EBDT (called bloc and bdat in AAT) and EBSC. See §D.7 for a detailed description of these tables.

B TEX and Ω Font Formats B.1 TFM The TFM format (for “TEX font metrics”) was defined in 1980 by Lyle Ramshaw, a student of Knuth, and remains today the only font format recognized by TEX. Only in recent years have extensions of TEX finally used other font formats: TrueType and OpenType. TFM is a binary format, but there is a human-readable form called PL (for “property list”). In this book, we have adopted the principle of showing only the “humanized” form of a font format whenever it exists, provided that conversion from binary to legible format and vice versa can be done without loss of information. To convert from TFM to PL, we have a tool: tftopl, written by Leonidas Guibas in 1978. When used in one of the following ways: tftopl cmr10 > cmr10.pl tftopl cmr10.tfm cmr10.pl it will convert the font cmr10.tfm, wherever it is found on the disk, to the PL format and store this representation of the font in the file cmr10.pl in the current directory. This manipulation would be useless if the antidote did not exist: the opposite tool pltotf, which restores our font to its binary form. This tool is used as follows: pltotf cmr10 pltotf cmr10.pl othername.tfm In the first case, a file by the same name as the PL file and with extension .tfm will be created in the current directory, whereas in the second case we explicitly provide the names of these files.

Appendix B : TEX and Ω Font Formats The principle of the PL file syntax is very simple: there are expressions, which have the following form: (KEYWORD VALUE) where KEYWORD is a keyword and VALUE is its value, which may be another keyword, a set of keywords and numeric values, or another expression (again in parentheses). The keywords are written in uppercase letters, as computer code was written 20 years ago, in the era of Fortran IV and IBM 360/370 assembly language. Here is a short extract of a hypothetical PL file: (FAMILY HYPOTHETICAL) (FACE F MIE) (CODINGSCHEME ASCII) (DESIGNSIZE D 10) (COMMENT THIS EXAMPLE IS PURELY) (COMMENT HYPOTHETICAL) (FONTDIMEN (SLANT R .25) (SPACE R .33) (SHRINK R .17) (STRETCH R .17) (XHEIGHT R 0.4) (QUAD R 1.0) ) (LIGTABLE (LABEL C f) (LIG C i O 0) (STOP) (LABEL C i) (KRN C f R 0.05) (STOP) ) (CHARACTER C f (CHARWD R 0.3) (CHARHT R 0.7) ) (CHARACTER C i (CHARWD R 0.278) (CHARHT R 0.67) ) (CHARACTER O 0 (CHARWD R 0.488) (CHARHT R 0.7) ) Inserting a carriage return after each expression is not required, nor is leaving three spaces at the beginning of every line when we are inside an expression. We have presented the code in this way because tftopl does so.

B.1. TFM
One detail of the syntax: numbers are always preceded by a letter selected from the following:
R (real), O (octal), H (hexadecimal), D (decimal). When we refer to the code point of an ASCII
character other than the parentheses, we can also write C followed by the character itself.
Example: C i is the number 105.
From a glance at this code, we can see that the file is divided into four sections:
• Global declarations
• Font parameters
• Kerning pairs and ligatures
• Metric properties of the glyphs
B.1.1
Global Declarations
Below we shall give the complete list of available keywords, but note that only one is really
useful to TEX: DESIGNSIZE.
Here is the complete list of keywords and their official interpretations:
• CHECKSUM, followed by a 4-byte whole number, is a checksum used to confirm the physical
integrity of the file.
• DESIGNSIZE, followed by a whole number between 0 and 2,048, is the font’s design size,
expressed in American printer’s points.
• DESIGNUNITS, followed by a positive real number, indicates the correspondence between
the abstract units used in the PL file and the design size (which is a dimension from the
real world, as it is expressed in American printer’s points). Its default value is 1.0, which
means that to find a real dimension it is necessary to multiply the abstract dimension
by the design size. To have abstract units equal to those of the PostScript Type 1 fonts, it
would be sufficient to take (DESIGNUNITS R 1000) (because the unit of a PostScript font
is one-thousandth of the design size).
The simplest choice is to leave DESIGNUNITS equal to 1. We quickly acquire the habit of
interpreting (WIDTH R 0.7) as “width of seven-tenths of the design size”.
• CODINGSCHEME, FAMILY, FACE: three data that are obsolete, no longer used.
B.1.2
Font Parameters
Unlike the preceding section, this one is very interesting, as the font’s global behavior depends
on it. It contains the font’s global parameters, which can be as numerous as 255 (in current
implementations of TEX), but only the first 22 parameters have special names. Among them,
the first seven [which correspond to the \fontdimens that we saw in the section on configuring
NFSS] are used in text fonts. The others are used only with mathematical fonts. Here are the
meanings of the first seven parameters:

Appendix B : TEX and Ω Font Formats
• SLANT specifies the slope, expressed as the tangent of the angle—in other words, the horizontal displacement at a height of 1 point. This value is used when TEX places an accent
over a letter so that the accent will remain centered over the letter’s axis, which in this
case is oblique.
• SPACE specifies the ideal interword space, i.e., the space used to set type in the font in
question in the absence of any constraints imposed by justification.
• STRETCH specifies the maximum stretching allowed for the interword space.
• SHRINK specifies the maximum shrinking allowed for the interword space.
• XHEIGHT specifies the font’s “x-height”, i.e., the height of the lowercase letters. This information is used by TEX for the placement of accents over letters. By way of example, let us
assume that the XHEIGHT of a font is x and that we wish to place an accent over a letter
of height x′ > x. We will therefore move the accent up by the amount of x′ −x. We have
direct and very elegant access to the value of this parameter through the dimension ex.
• QUAD specifies the size of the font’s em. We have access to it through the dimension em.
• EXTRASPACE applies primarily to the Anglo-Saxon and German typographic traditions.
Within these traditions, it involves an increase of the interword space whenever this space
comes after a punctuation mark that ends a sentence. When more space is inserted after a
sentence-final punctuation mark, the reader’s eye can more easily detect the beginnings
of sentences and can more easily distinguish periods used in abbreviations, which are not
followed by extra space. This practice is not observed in France; indeed, TEX even calls the
command that disables this property \frenchspacing.
The next 15 parameters are named NUM1 (or DEFAULTRULETHICKNESS), NUM2 (or BIGOPSPACING1), NUM3 (or BIGOPSPACING2), DENOM1 (or BIGOPSPACING3), DENOM2 (or BIGOPSPACING4), SUP1
(or BIGOPSPACING5), SUP2, SUP3, SUB1, SUB2, SUPDROP, SUBDROP, DELIM1, DELIM2, and AXISHEIGHT. They are indispensable for mathematical fonts and serve to manage the composition
of glyphs into two-dimensional mathematical constructions, such as fractions, superscripts
and subscripts, extensible delimiters, etc.
We can also use the keyword PARAMETER
D followed by an integer between 1 and 255 to
indicate any parameter.
B.1.3
Kerning Pairs and Ligatures
The rules for the interactions of glyphs with each other appear in this table. Two glyphs that
are set side by side can attract or repel each other: this information constitutes a kerning pair.
They can also become “very close” to each other and form a new glyph: a ligature. They can
also remain intact but give birth to a new glyph that appears between them: we call that
approach, and some variations on the theme, smart ligatures.
All these operations are carried out within the expression (LIGTABLE operations). They are
classified according to the first glyph in the kerning pair or ligature. Each of these initial
glyphs is represented by an expression (LABEL
glyph). At the end of all these operations
affecting a given glyph, we find the expression (STOP). For example, if a period or comma
following the letter ‘f’ should be moved 1.5 points closer to the letter, we write:

B.1. TFM
(LIGTABLE
(LABEL C f)
(KRN C . R -.15)
(KRN C , R -.15)
(STOP)
)
In the code above, we can already see the kerning operation, represented by the keyword KRN.
This glyph is followed by the second glyph in the pair and the amount of kerning requested:
a negative amount when we move glyphs closer together, a positive one when we move them
farther apart. Two points must be noted:
• Once kerning has been performed, the second letter of the kerning pair is “free” and can
take part in other kernings or ligatures.
• If we request both kerning and a ligature between two letters, the one that appears first
in the file will be executed.
Let us now move on to ligatures. The operation for a simple ligature, LIG, is written as follows:
(LIGTABLE
(LABEL C f)
(LIG C f H 13)
(LIG C i H 14)
(LIG C l H 15)
(STOP)
)
In the code above, the glyph pairs “ff”, “fi”, and “fl” are replaced by other glyphs (in hexadecimal positions 13, 14, 15) that represent the ligatures ‘ff’, ‘fi’, and ‘fl’. When a new glyph is
inserted, it is granted the same rights as the glyphs explicitly inserted by the user, and it in turn
takes part in the formation of other ligatures or kerning pairs. For example, to obtain an ‘ffi’,
we first form the ligature “f + f = ff” and then “ff+ i = ffi”. That means that forming a ligature
of n glyphs requires, in addition to the ligature itself, n−2 intermediate positions in the glyph
table.
Now let us discuss “smart” ligatures. What distinguishes “smart” ligatures from “simple” ligatures is the fact that we preserve the old glyphs when inserting the new one. We write /LIG/
if we wish to preserve both glyphs and place the new one in the middle, /LIG if we wish to
preserve only the first glyph, and LIG/ if we wish to preserve only the second.
Smart ligatures allow us to save space in the glyph table. Let us take an example. Suppose
that, in a rather exotic font, we wish to have two types of apostrophes: one used after capitals,
the other used after lowercase letters. Suppose that the latter is the rule and the former is
the exception. Then in the box for the apostrophe there will be a “lowercase apostrophe”. We
need another code point for the glyph of the “uppercase apostrophe”. If we used only simple
ligatures, we would need 26 new glyphs: one for each combination of an uppercase letter and
a special apostrophe. Not to mention the accented letters.

Appendix B : TEX and Ω Font Formats
With smart ligatures, however, it is sufficient to use /LIG: in this case, the uppercase letter
remains intact, and only the apostrophe changes. No extra box in the table is required.
Having reached this point, we may well wonder what happens after the replacement. Does
the new glyph, or even the old glyphs kept intact, take part in the formation of new kerning
pairs or ligatures? For instance, in the preceding example, supposing that we wrote ‘A’ ’, the
apostrophe would become an “uppercase apostrophe”; but can it also be kerned with the
letter ‘A’? That is very desirable indeed. But there is also the risk of an infinite loop: if xy
produces xy′ and there is a ligature between x and y′ that brings us back to the starting point,
xy, a few iterations will certainly cause the software to crash. Noticing that the question of the
“time of availability” of the glyphs used to form a ligature does not have only one answer,
Knuth provided for all the possible cases:
• /LIG: we replace the first glyph and examine the possible kerning pairs and ligatures that
the newly inserted glyph might form with the second, before examining those that the
second glyph might form with the glyph that follows it.
• /LIG>: we replace the first glyph and continue with the possible kerning pairs and ligatures of the second glyph with the one that follows.
• LIG/: we replace the second glyph and examine the possible kerning pairs and ligatures
of the first glyph (kept intact) with the newly inserted glyph, and then those of the second
glyph with the one that follows.
• LIG/>: we replace the second glyph and continue with the possible kerning pairs and
ligatures that the second glyph might form with the one that follows.
• /LIG/: we insert a new glyph between the first and the second and then examine first the
kerning pairs and ligatures that the first glyph forms with the new one, then those that
the new glyph (or whatever it became, if it was in turn replaced by something else) forms
with the second, and then those that the second forms with the one that follows.
• /LIG/>: we insert a new glyph between the first and the second and then examine first
the kerning pairs and ligatures that the new glyph forms with the second, then those that
the second forms with the one that follows.
• /LIG/>>: we insert a new glyph between the first and the second and then examine the
possible kerning pairs and ligatures of the second glyph with the one that follows.
It is evident that the potential of smart ligatures remains yet unexplored: very few fonts use
them, and their complexity is due more to Knuth’s penchant for thoroughness than to any
real need. The most common criticism of smart ligatures is that they are inseparably tied
to the font and cannot be enabled or disabled according to context. For example, about 15
years ago, the author developed an Arabic font in which contextual analysis was managed
entirely by smart ligatures. But in view of the rigidity of this approach and the problems he
encountered, he was quite happy to abandon the approach altogether and perform the same
operations with ΩTPs [170], which are filters internal to Ω1, and later with Ω2 internal modules. The difference between these approaches corresponds to the difference between AAT
and OpenType fonts: in the former case, the font itself manages contextual analysis without

B.1. TFM
leaving many opportunities for intervention to the typesetting software; in the latter case,
software modules (including the rules for contextual analysis) and the software are responsible for applying them, and sophisticated software may allow for all kinds of interventions by
the user.
But let us return to smart ligatures. One peculiarity of TEX relative to other typesetting systems is that the interword space is not a glyph but an offset. What, then, should be done to
define ligatures between a “normal” glyph and a space? For instance, in some decorative fonts
there is an ‘e’ with a longer curve, used at the end of a word. If the word is followed by a
punctuation mark, we can write a ligature between the letter ‘e’ and that mark; but what can
be done if it is followed by a space, when the space is not a glyph? The same question arises
for ligatures at the beginning of a word.
This possibility is covered—in a somewhat awkward way, it must be admitted—at least for
ligatures at the end of a word. To define a ligature at the beginning of a word, we write
(LABEL BOUNDARYCHAR)
etc.
(STOP)
Everything is fine up to this point. It is the ligatures at the end of a word that are problematic.
We must define a glyph as being the “word boundary”, using the expression (BOUNDARYCHAR
glyph). This glyph may be an empty box that is used only to convey the abstract concept of
“word boundary”. But it may also be an actual glyph. The same ligatures and kerning pairs
will apply in both cases. If there is an empty box in the font, that box can play the role of
“word boundary”, and the problem will not arise. But in most font encodings of the TEX
world—T1, T2, etc.—no box is left empty; thus we must select a “real” glyph that will never
be used as such. One stopgap is to use the glyph for a combining accent (code points 0 to 12
in the T1 encoding), which will never be placed next to another glyph but will only be placed
above or below another glyph by means of the \accent primitive. But that means that we
have long since left the realm of elegant programming and taken up hacking. Once again,
these problems are handled better by Ω and its internal filters, which are closer to the original
text and the Unicode characters than to the typeset result, the fonts, and the glyphs.
B.1.3.1
Optimizing operations
In the table of kerning pairs and ligatures, another layer of complexity comes on top of the
complexity inherent in simple and smart ligatures: the optimization of operations. There are
historical reasons for that: it must be borne in mind that this file format dates from the 1970s
and that every byte of memory saved represented a non-negligible savings. Thus everything
was done to make the table of kerning pairs and ligatures as small as possible. Here are some
of the strategies for optimization:
• If two or more glyphs behave the same way towards the following glyphs with respect to
kerning, they are listed together. For example, in cmr10, we find the code:
(LABEL C F)
(LABEL C V)
(LABEL C W)

Appendix B : TEX and Ω Font Formats
(KRN C o R -.083334)
(KRN C e R -.083334)
(KRN C u R -.083334)
(KRN C r R -.083334)
(KRN C a R -.083334)
(KRN C A R -.111112)
(LABEL C K)
(LABEL C X)
(KRN C O R -.027779)
(KRN C C R -.027779)
(KRN C G R -.027779)
(KRN C Q R -.027779)
(STOP)
which means that the letters ‘F’, ‘V’, and ‘W’ behave the same way relative to the letters ‘o’,
‘e’, ‘u’, ‘r’, ‘a’, ‘A’, ‘O’, ‘C’, ‘Q’, and ‘R’. Moreover, the letters ‘K’ and ‘X’ behave the same
way as the preceding, but only towards the last four letters: ‘O’, ‘C’, ‘Q’, and ‘R’. Without
optimization, we would need 48 lines to describe the same kerning pairs; here, however,
we have only 16. That represents compression of 75 percent.
• Now suppose that two glyphs behave in the same way towards a great many other glyphs,
except in one case. And suppose that in that case there are two distinct nonzero kerning
pairs or two distinct ligatures. The format shown above assumes that the “partners” of
one glyph form a subset of the “partners” of the other. That is not the case here. To cope
with this situation, Knuth introduced the operation (SKIP integer), which allows us to
skip a given number of operations.
Let us take an example. Suppose that we have an ‘f’ and an ‘f ’ (long ‘s’). These two letters
have the same kerning pairs with, for example, the period and the comma. But they form
different ligatures with the letter ‘i’. Suppose that we have placed the ‘f ’ in the box for
the ‘s’. We want the following operations:
(LABEL C s)
(KRN C . R -.1)
(KRN C , R -.1)
(LIG C i H 0)
(STOP)
(LABEL C f)
(KRN C . R -.1)
(KRN C , R -.1)
(LIG C i H 1)
(STOP)
where we have placed the ligature ‘f i’ in code point 0 and the ligature ‘f i’ in code point 1.
How can we optimize this code? The first step is to write:
(LABEL C s)
(LIG C i H 0)
(LABEL C f)

B.1. TFM
(LIG C i H 1)
(KRN C . R -.1)
(KRN C , R -.1)
(STOP)
In this code, it is the fourth line that causes a problem, when we start reading from the
first line: specifically, we are concerned with the long ‘s’, and we discover that there are
two ligatures, the second of which has nothing to do with it. Thus we introduce a SKIP
just after the second line:
(LABEL C s)
(LIG C i H 0)
(SKIP D 2)
(LABEL C f)
(LIG C i H 1)
(KRN C . R -.1)
(KRN C , R -.1)
(STOP)
In this way, when we start reading from the first line, we skip from the third line directly
to the sixth and thus avoid the problematic ligature.
One can imagine software tools that carry out these optimizations. The fact that they do not
exist after almost 25 years, since the TFM format was created, perhaps shows that this optimization is no longer really indispensable.
B.1.4
The Metric Properties of Glyphs
We have reached the most important and, at the same time, the simplest part: the metric
properties of each glyph. These properties are four in number, plus two “gadgets”. Here are
the four metric properties:
• CHARWD: the glyph’s set-width.
• CHARHT: its height.
• CHARDP: its depth, i.e., the vertical dimension of the part located below the baseline.
• CHARIC: its italic correction, i.e., the amount of kerning to perform when the glyph is set
“up against a wall”. For example, let us take an italic ‘f’ followed by an upright bracket:
“f]”. The result is rather catastrophic and calls for kerning: “f ]”. But this kerning is technically not possible, as the two glyphs belong to different fonts and nothing yet has been
done for executing kerns or ligatures between glyphs of different fonts. Thus the software
must add a bit of space, at a higher level. But how much space? After all, if instead of
the ‘f’ there had been a ‘g’ (also italic), the problem would not have occurred. This datum
is the letter’s “italic correction”, and it is one of the four dimensions of each TEX glyph.
The two “gadgets” are the following:

Appendix B : TEX and Ω Font Formats
• NEXTLARGER, followed by a reference to another glyph in the font. In mathematical typography, we have some constructions that assume the size of the expression that they
enclose,1 such as roots and large delimiters, for example. The approach is quite impressive: specifically, we can have any number of predefined sizes of these objects. We must
merely arrange them in order and include within each one a reference to the one that
immediately follows. TEX will then run through this linked list of glyphs and stop at the
one that is closest to the desired size. The author used this property to produce expanding
parentheses and braces in some 30 different sizes in the yhmath package [162].
• We all know that mathematicians can never be satisfied. However large the predefined
symbols may be, there will always be even larger mathematical constructs. There as well,
TEX anticipated the problem: beyond a certain point, it offers symbols built up from basic
components. For example, to produce a huge brace, we need only take the top part, the
notch in the middle, and the bottom part, and then insert small vertical strokes between
these pieces. Since any number of vertical strokes may be used, our brace can be arbitrarily large. That is defined in the TFM file as follows (example drawn from the font
cmex10.tfm):
(CHARACTER O 71
(CHARWD R 0.888891)
(CHARDP R 0.900009)
(VARCHAR
(TOP O 71)
(MID O 75)
(BOT O 73)
(REP O 76)
)
)
where TOP, MID, and BOT denote, respectively, the glyph placed at the top, in the middle,
and at the bottom of the extensible delimiter and REP denotes that will be repeated as
much as necessary in both the top and bottom parts of the delimiter. This approach may
seem limited at first glance, but it yields quite acceptable results for the usual delimiters;
for more aesthetically satisfactory delimiters, we can always resort to METAFONT to produce larger sizes and store them either in section 0x80-0xFF of the font table or directly in
an Ω font that may contain up to 65,536 glyphs—which is what the yhmath package does.
B.2
OFM
The OFM format (for “Ω font metrics”) was defined by John Plaice and the author in 1994.
It is an extension of the TFM format. The only difference (and it is important) is that the
maximum number of glyphs grows from 256 to 65,536 and that the maximum number of
kerning pairs and ligatures grows from 216 to 232. The human-readable file format associated
with the OFM binary format is called OPL (= “Ω properties list”). The tools that convert OFM
to OPL and OPL to OFM are, respectively, ofm2opl and opl2ofm.
1 Michael Spivak, in his book The Joy of TEX [321], full of nasty allusions, speaks of “things that grow”.

B.3. VF
B.3
VF
The VF format (= “virtual font”) was proposed by Knuth in 1990. It was immediately implemented by dvips and many other DVI drivers. We have already explained the advantages and
disadvantages of virtual fonts in Sections 9 and 9. Here we shall present their structure.
Let us recall the principle behind virtual fonts: the idea is to replace, within a DVI file, a glyph
in a virtual font with more interesting DVI code that for various reasons cannot be produced
by TEX. This code can be as short as the simple naming of another glyph or as long as an
entire page.
As with TFM files, VF also have a human-readable counterpart, the format VPL (for “virtual
properties list”), which is what we shall describe here. The VPL file format is an extension of
the PL file format: it contains the same expressions and also a few others that are specific to
virtual fonts.
Note that every virtual font must be accompanied by a TFM font with the same metrics,
for the very simple reason that TEX can read only TFM files. We can easily obtain the real
font associated with a virtual font: all that we have to do is switch to VPL and delete all the
expressions specific to the VPL format; we then obtain a PL file that we can then convert
to TFM.
The new expressions are of two types: those placed in the preamble, which apply to the entire
font, and those found within each glyph, which describe the DVI code that will ultimately
replace it. The global expressions are font definitions:
• (MAPFONT D number ...), which defines a font and associates with it an internal number.
This expression contains a series of expressions, defined below.
• (FONTNAME string), the name of the corresponding TFM file (without the extension).
This font may be real or virtual; if it is virtual (i.e., if there is a VF file by the same
name), dvips will follow the references until it finds a real font (unless it gets stuck in
an infinite loop).
• (FONTAREA string), the name of the directory in which the font is stored. By all means
avoid this expression, which makes the font dependent upon the local file system.
• (FONTCHECKSUM 4-byte integer), the checksum of the TFM font.
• (FONTAT R real number), the magnification factor requested (where R 1.0 is the factor 1,
unlike in TEX, where the factor must be divided by 1,000).
• (FONTDSIZE R real number), the requested optical size of the font. Changing this value
apparently has no effect on anything.
And here are the instructions that we can include in each glyph:
• (MAP
...
), the expression that is placed under CHARACTER and that contains all the
others.

Appendix B : TEX and Ω Font Formats
• (SELECTFONT D number) selects the font whose number is number, defined in advance, as
the active font. This font will remain active until the next SELECTFONT. The font selected
by default is the one defined first in MAPFONT.
• (PUSH) stores the current coordinates in the DVI and places these coordinates on a stack.
• (POP) retrieves the coordinates from the stack and makes them the current coordinates.
• (MOVERIGHT real number) moves to the right.
• (MOVELEFT real number) moves to the left.
• (MOVEUP real number) moves upwards.
• (MOVEDOWN real number) moves downwards.
• (SETCHAR glyph) sets the glyph glyph in the active font.
• (SETRULE height width) sets a black box of the given dimensions.
• (SPECIAL string), a “special”, i.e., an island containing arbitrary code.
• (SPECIALHEX series of bytes in hexadecimal notation). Within the SPECIAL instruction there is a problem of protection. Specifically, how can we include a closing parenthesis in any “special” that occurs, when the closing parenthesis is what terminates the
expression? The solution (a bit awkward, but radical) is to write the entire special in hexadecimal notation. For example, to obtain the equivalent of \special{ps:(hi\)) show},
we would have to write (SPECIALHEX 70 73 3A 28 68 69 5C 29 29 20 73 68 6F 77).
We can see that every DVI instruction can be incorporated within a VF glyph. There is also
a very basic tool for creating virtual fonts, written by Eberhard Mattes (the developer of the
long-famous emTEX) and called qdtexvpl (for “quick and dirty TEX to VPL”) [249], which does
the opposite: we write a TEX file containing the TEX commands that correspond to each virtual glyph, then compile this file to obtain a DVI file, and qdtexvpl reads the DVI file, extracts
the DVI codes corresponding to each glyph, and produces a VPL file containing these instructions.
B.4
OVF
The OFM format was defined by John Plaice and the author in 1994, for Ω1 (version 1.* of Ω).
It is an extension of the TFM format. The only difference with VF (and it is important) is that
the maximum number of glyphs grows from 256 to 65,536 and that the maximum number of
kerning pairs and ligatures grows from 216 to 232. The human-readable file format associated
with the OFM binary format is called OPL (for “Ω properties list”). The tools that convert
OFM to OPL and OPL to OFM are, respectively, ofm2opl and opl2ofm.

```text
C
PostScript Font Formats
Since its appearance in 1985, the year in which the first laser printer (the Apple LaserWriter)
came onto the market, the PostScript language has conquered the computer world, in everything from the industrial production of printed material to office management and the
personal printing of documents. In this chapter, we shall describe the various PostScript font
formats: Type 1, of course, but also Type 3, Type 42, Type 0, CID, Multiple Master, and the
very recent CFF/Type 2.
Before beginning to describe these font formats, we shall start with a brief introduction to
the PostScript language—an introduction that is essential for understanding the syntax of
the language used in fonts as well as the nature of the objects being manipulated. This introduction has no pretensions to thoroughness; after all, the specification of the PostScript
language [24] contains no fewer than 912 pages, and very dense ones at that! Instead, our
goal will be merely to give the basic information that is needed in order to understand what
follows. The reader eager to obtain more information on the PostScript language may consult
three books by Adobe (the red [24], blue [22], and green [20] books); there are also many
introductory books [303, 318, 250], and some works focused on the PostScript capabilities of
certain printers, such as the LaserWriter [52, 182].
C.1
Introduction to the PostScript Language
PostScript is an interpreted programming language, in the sense that it does not involve a step
for compilation: the printer or the rendering software reads the PostScript code and executes
it at the same time. The goal of the PostScript language is to describe a page for the purpose
of printing or display:1 an abstract description of the page (made up of mathematical objects)
1 We have seen people use the PostScript language to do calculations, but that remains in the realm of
the anecdotal.
```

is supplied to the PostScript interpreter. When an entire page has been described, it is then
printed out, and execution continues with the following page.
The objects that can be manipulated are straight lines, cubic Bézier curves (see Appendix G),
shapes whose outlines are made of straight lines or cubic Bézier curves, and, finally, fonts
(whose glyphs are also made of—straight lines and cubic Bézier curves).
C.1.1
Syntax
PostScript may seem strange to those accustomed to languages such as C and Java. First of all,
it is a language written in reverse Polish notation: to perform an operation, we first write the
operands and then the operator (“2 2 +” instead of “2 + 2”). Next, it is a language based on
a stack: we are not required to write declarations that end with a special character, as in other
languages. In PostScript, we write data, and these data are automatically placed on a stack;
then we write operators, and the operators pop the data from the stack, and possibly push
others onto the stack.
Here is a simple example of a block of PostScript code:
40 60 add 2 div sqrt round
and here is an interpretation: we place the numbers 40 and 60 onto the stack; add then adds
them and leaves 100 on the stack; we push a 2 onto the stack; the div operator takes the objects
100 and 2 and performs the division 100
2 ; thus it leaves 50 on the stack; then sqrt calculates
the square root and leaves
√
50 on the stack; round then rounds this number and leaves on
the stack the final result: 7.
As the example shows, to understand how a block of PostScript code works, we must think in
terms of the stack, always being aware of which data appear where on the stack and knowing
what effect each operator has on the stack’s data.
The peculiarities of the PostScript language do not end there. The objects2 manipulated by
the PostScript language can be of various types: integer, real number, string, name (a name is a
word that cannot be interpreted as a number; a name designates an executable object, unless
it is preceded by a slash), operator, table (a series of objects, placed within brackets), procedure
(a series of objects, placed within braces, that can be executed), dictionary (a series of keyword/value pairs, where the keyword is a name and the value can be any object), file, boolean
(true or false), etc.
The representation of strings obeys a few rules:
• They are written in ASCII and placed within parentheses. Certain characters must be
protected: \n (newline), \r (carriage return), \t (tab), \b (backspace), \f (form feed), \\
(backslash), \( and \) (parentheses), \123 to obtain the character whose decimal code
is 123.
2 PostScript’s “objects” have nothing to do with those of object-oriented programming. We have preserved the name in accordance with the official specification, and also to avoid less elegant choices such as
“thing” or “gizmo”.

C.1. Introduction to the PostScript Language
• Or they are written in hexadecimal (and thus need not be protected). We write the hexadecimal code in lowercase letters and enclose it in brackets: <6561737920746F2072656164>.
Any object can be pushed onto the stack or popped offthe stack.
A table, a procedure, or a dictionary can contain objects of all types, mixed together. For
instance, the following table [ 1 true [ /foo pop ] (hello) ] contains a number, 1;
a boolean, true; a subtable (itself containing a nonexecutable name, /foo, and an operator,
pop); and a string, (hello).
C.1.2
The System of Coordinates
We work on a Cartesian plane whose origin is the lower left corner of the page (and thus
the x-axis points to the right and the y-points upward). Lengths are measured in units called
PostScript points. A PostScript point is equal to 1
72 of an inch (approximately 0.3528 mm). It is
therefore slightly larger than the American printer’s point, which is equal to
72.27 of an inch
(approximately 0.3515 mm), but smaller than the Didot point (approximately 0.376 mm).
C.1.3
The current transformation matrix
The current transformation matrix (CTM) allows us to change the system of coordinates at any
time. The reader will certainly have used vector-design software before: we use it to define a
shape, and then we can enlarge the shape, turn it, scale it homogeneously or heterogeneously,
etc. In the PostScript language, these operations are also possible, but there is a slight difference of a philosophical nature: it is not the shape that changes but rather the system of
coordinates in which it is expressed. For example, instead of saying “I am drawing twice as large”,
we say “Henceforth my units of length will be twice as large”; instead of saying “I am drawing
my shape at a 45° angle”, we say “I am rotating my system of coordinates 45°”; thus the same
PostScript code can generate infinitely many different shapes, according to the properties of
the selected system of coordinates. In the case of fonts, this approach allows us to preserve
the definition of the glyphs and set them at any size and at any angle: only the system of
coordinates changes.
But how do we indicate a change to the system of coordinates?
A bit of mathematics: a linear transformation of the Euclidean plane is a function (x,y) →
(ax+by+tx,cx+dy+ty), where (x,y) ∈R2 and a,b,c,d,tx,ty are real numbers. A linear transformation can thus be written as a system of two linear equations in two variables:
x′ = ax+by+tx
y′ = cx+dy+ty
and we say then that it is characterized by the six parameters (a,b,c,d,tx,ty).
We all know from our high-school math courses (and if we have forgotten, it is easy enough
to verify) that translation, scaling, and rotation are linear transformations and that we can use
matrix notation to describe them. For instance:

x
y

→

x+tx
y+ty

,

x
y

→

sx x
sy y

,

x
y

→

x cosθ−y sinθ
x sinθ+y cosθ


```text
are, respectively, a translation of (tx,ty), a scaling of (sx,sy), and a rotation of the axes by the
angle θ.
Thus we can say that translation is the sum of the matrix ( x
y) with the matrix
txty

, whereas scaling and rotation are the products of the matrix ( x
y) with the matrices

sx 0
0 sy
and
 cosθ −sinθ
sinθ
cosθ

.
In the former case, we add matrices; in the latter, we multiply them.
That is quite a nuisance if we wish to find a general way to describe linear transformations,
one that applies to translations just as it applies to scaling and rotations. After all, these three
transformations are the most important operations performed by vector-design software.
Fortunately, mathematicians have found a way to solve the problem. Rather than going into
the details of the theory,3 let us go straight to the method that is used in practice: instead of
working with two-row matrices to indicate a point in space, which seems logical since the
Euclidean plane is two-dimensional, we shall work with three-row matrices, in which the
third row always contains the value 1.
Scaling and rotations thus become multiplications by 3×3 matrices, as follows:
⎛
⎜
⎝
sx
sy
⎞
⎟
⎠,
⎛
⎜
⎝
cosθ
−sinθ
sinθ
cosθ
⎞
⎟
⎠.
And the pleasant surprise is that translation also becomes a multiplication by a 3× 3 matrix,
namely:
⎛
⎜
⎝
tx
ty
⎞
⎟
⎠.
What could be more natural, then, than to say that we model transformations of the plane with
matrices?
M =
⎛
⎜
⎝
a
b
tx
c
d
ty
⎞
⎟
⎠,
where the parameters (a,b,c,d,tx,ty) are precisely those of the linear transformation with
which we started. The transformation of a point (x,y) of the plane is therefore the product of
this point, considered as the matrix
 x
y
, by the transformation matrix M.
Even better, suppose that we carry out a series of operations (translations, scalings, rotations)
with the matrices M1,M2,... ,Mn. The result will be an operation whose matrix M is the product of the matrices M1M2 ···Mn. Even other operations, such as reflection about an axis, can
be expressed in this manner.
3 For the reader with a mathematical background, the method involves switching from the plane R2
to the projective plane P2. The latter is the quotient of R3 \ {(0,0,0)} by the equivalence relation (x,y,z) ∼=
(x′,y′,z′) ⇐⇒(x′,y′,z′) = r(x,y,z) for r > 0. If z̸ = 0, since all values of r(x,y,z) correspond to the same point in
projective space, we can take r = 1/z and write this point as (x,y,1). That is exactly what we do. For more practical details, consult [246, p. 21]; the theory is admirably described in a course by the unforgettable professor
Rémi Goblot [149, 150].
```

C.1. Introduction to the PostScript Language
Let us leave the platonic world of mathematics and come back down to earth. It is for all
these reasons that the PostScript language uses the methods that we have just examined. In
our code, we shall use the notation [a b c d tx ty] to represent a transformation by the
matrix

a b tx
c d ty
0 0 1

.
As we have just seen, some special cases of linear transformations are:
• Translation: [1 0 0 1 tx ty]
• Scaling: [sx 0 0 sy 0 0]
• Rotation by the angle θ: [c s -s c 0 0] (where c = cosθ and s = sinθ)
PostScript considers that every object is governed at any time by a transformation, whose
matrix is the current transformation matrix. Thus, between the coordinates that appear in our
code and what appears on paper or on the screen, we always pass through the current transformation, whether we are drawing an outline or filling one in. That is equivalent to the change
of system of coordinates that we have just described.
It remains to be seen how we can manipulate this CTM within code. We can:
• Initialize it, using the operator initmatrix).
• Give it a new value (with the operator [a b c d tx ty] setmatrix).
• But the most elegant approach is certainly to multiply it by another transformation matrix. The operator that does so is concat.4 Thus we can write, for example, [1 0 0 1
100 100] concat to set the current transformation with a translation of the system of
coordinates by 100 units to the right and 100 units upwards.
• There are simplified versions of concat for the three most important operations:
– Translation by (tx,ty) PostScript units: tx ty translate
– Scaling by the horizontal factor sx and the vertical factor sy: sx sy scale
– Rotation by the angle θ: θ rotate
Since matrix multiplication is not commutative, it is obvious that the result will be different
if the order of these operations changes.
C.1.4
Paths
We use two mathematical objects to draw: straight lines and cubic Bézier curves (Appendix G).
The straight line between the starting point (x0,y0) and the ending point (x1,y1) is the function:
t →(1−t)

x0
y0

+t

x1
y1

[0,1] →R2
4 Do not be surprised by the name: Adobe calls the product of matrices “concatenation”.

The cubic Bézier curve with starting point (x0,y0), control points (x1,y1) and (x2,y2), and ending point (x3,y3) is the function:
t →(1−t)3

x0
y0

+3t(1−t)2

x1
y1

+3t2(1−t)

x2
y2

+t3

x3
y3

[0,1] →R2
If f1, f2 are functions of these kinds (straight lines or cubic Bézier curves) in which the ending
point of the first coincides with the starting point of the second, their concatenation is the
function:
t →
⎧
⎨
⎩
f1(t),
if x ∈[0, 1
2[
f2(t),
otherwise, with limt→1
2 f1(t) = f2(1)
[0,1] →R2
We use the term path for the concatenation of any number of straight lines and cubic Bézier
curves. Here are some of the PostScript operators that produce paths:
• To trace a path, one must first initialize it (in other words, create a current path). That is
done with the newpath operator. After this operator has been invoked, the current point
is no longer defined. Before using any other operation, we must define it by using an
absolute displacement.
• moveto is the operator for this purpose: by writing x y moveto, we set the current point
to (x,y). This operator does not draw anything.
• There are also operators for relative displacement: x y rmoveto. There is nothing magical
about them; the displacement is simply performed relative to the previous current point,
rather than in an absolute way.
• Along the lines of moveto and rmoveto, there are the operators x y lineto and x y
rlineto, which draw straight lines using the previous current point as the starting point.5
• Likewise, there are the operators curveto and rcurveto, which produce cubic Bézier
curves:
– If ( xcyc ) is the current point before the operator is executed, x1 y1 x2 y2 x3 y3
curveto will draw the Bézier curve with starting point ( xcyc ), control points ( x1
y1 ) and
( x2
y2 ), and ending point ( x3
y3 ).
– x1 y1 x2 y2 x3 y3 rcurveto, however, will draw the Bézier curve with the same
starting point but with control points
 xc+x1
yc+y1

and
 xc+x2
yc+y2

and ending point
 xc+x3
yc+y3

.
5 Note that lineto, unlike moveto, will not initialize the current point. Therefore, after a newpath, we
must perform a moveto to obtain a current point before drawing anything.

C.1. Introduction to the PostScript Language
 newpath
 100 50 moveto
 0 50 50 75 100 100 rcurveto
 -100 0 rlineto
 2 setlinewidth
 stroke
 newpath
 200 50 moveto
 100 0 rlineto
 0 100 rlineto
 0 -25 -50 -50 -100 -50 rcurveto
 closepath
 0.8 setgray
 fill






Figure C-1: Examples of PostScript code: tracing a path, filling a shape.
• thickness setlinewidth specifies the thickness of the current path in PostScript points.
Note that the thickness 0 is in fact one pixel (thus it is invisible to the naked eye, if the
printer is of high resolution).
• A colored path, specified by t setgray (gray level, with t between 0 and 1, where 0 is
white and 1 is black), r v b setrgbcolor (a three-color specification: red, green, blue),
or c m j n setcmykcolor (a four-color specification: cyan, magenta, yellow, black).
• All the operators above are used only to construct an abstract path. Nothing is actually
drawn until we use the operator stroke. This operator has the effect of newpath and will
initialize a new current path.
On the left side of Figure C-1, we can see an example of a PostScript path.
C.1.5
Shapes
A shape is drawn by filling in an outline or multiple outlines. An outline is a closed path, in
the sense that the starting and ending points coincide.
In fact, this condition is not sufficient for the PostScript language: it is necessary to close a
path explicitly, using the closepath operator. If the extremities of the path actually do coincide, this operator will have no visual effect. Otherwise, it will draw a straight line between
the extremities.
Above we mentioned the inside of an outline. This notion, so intuitive to the human,6 is not
at all obvious to the computer. When a shape is built up from several outlines that intersect
or that are contained one inside another, what is the “inside” of the shape? And even if it is
made of only one outline, that outline could well intersect itself, leaving our intuition about
inside and outside on shaky ground.
The PostScript language provides two rules for calculating the inside of a shape (only the first
of which is used in Type 1 fonts, as we shall see below):
1. The nonzero winding number rule: to determine whether a point is inside or outside the
shape, trace a ray from the point to infinity. Ensure that the ray does not pass through any
point at which paths intersect and is not tangent to any path. (If by bad luck it happens
6 Incidentally, some geometric constructions, such as the Möbius strip and the Klein bottle, prove that
the concepts of inside and outside are in no way trivial.

+1
-1
-1
-1
-1
-1
-1
-1
fill
eofill
Figure C-2: Examples of filling according to the nonzero winding number rule (the three figures at the left)
and the even–odd rule (the three figures at the right).
to violate this condition, adjust it by some epsilon to bring it into compliance.) Let n = 0.
Suppose that we are standing on the ray and that we start walking from its point of origin
to infinity. Every time we encounter a curve or a straight line belonging to the shape that
runs from right to left,7 we will decrement n by 1. In the opposite case, we will increment
n by 1. If, at the end, n is zero, we declare that the point is outside the shape; otherwise,
it lies inside the shape (see Figure C-2, left).
2. The even–odd rule: we perform the same manipulation, but this time we merely increment n, irrespective of the direction of any curve or line segment that we encounter. If
at the end n is odd, then the point lies inside the curve; if n is even, the point lies outside
the curve (see Figure C-2, right).
The first method is more powerful, since it makes use of the direction of the paths.
The fill operator fills the current closed path with the current color, using the nonzero
winding number rule to decide what is inside the curve and what is outside. The eofill does
the same but uses the even–odd rule.
C.1.6
Bitmap Images
Vector operations (tracing, filling, typesetting) are certainly important, but it is also perfectly
possible to include bitmap images in the description of a PostScript page. The image format is specific to the PostScript language (and therefore is neither JPEG nor TIFF nor any
other bitmap format in the industry). A bitmap image is incorporated into a PostScript page
through the use of the image operator, which reads the following parameters on the stack:
width height depth matrix source image
where width and height are the image’s dimensions in pixels, depth is the number of bits
per color (1, 2, 4, 8, or 12), matrix is the transformation matrix being applied to the image,
and source is either a procedure (which manages the image dynamically), a string, or a file
(which may be compressed with LZW, RLE, CCITT, etc.) [24, pp. 129–156].
7 A more rigorous way to describe this situation is to say that if we take a point of reference orthonormal
to R3 whose first unit vector,⃗i, lies on the ray (and points to infinity), the second unit vector,⃗j, lies on the
tangent to the curve at the point of intersection (and points in the direction of the curve), and the third unit
vector,⃗k =⃗i∧⃗j, points to the reader (we apply the famous “right-hand rule”).

```text
C.1. Introduction to the PostScript Language
The image operator will draw an image with its own colors. But now let us imagine that the
image is not an ordinary image but a glyph in bitmap form (like those contained in bitmap
fonts). In this case, we do not want our glyph to have a set color; we want it to be able to assume
the active color from the context. That can be done with a variant of image by the name of
imagemask:
width height polarity matrix source imagemask
The image produced is of depth 1, and its color depends on the context; an image of this kind
is called a “mask”, whence the name of the operator. The parameter polarity enables us to
obtain the “negative” of a glyph (the values of all the pixels are inverted). This is the operator
that is used by dvips in Type 3 bitmap fonts.
C.1.7
Managing the Stack, Tables, and Dictionaries
To place an item on the stack, we merely . . . write it. If we want to get rid of it, we can use
pop, which deletes the top item from the stack. The exch operator swaps the first and second
entries on the stack. dup duplicates the top item on the stack. count returns the number of
items contained on the stack, and clear deletes them all. These are simple operators. Now
let us look at two operators for stack management that are a bit more complex:
xn ... x1 x0 n index
The index operator retrieves the number n from the pile, descends n + 1 levels below that
number, and places a copy of element xn (found at that position) on the top of the stack.
Example: a b c d e 3 index leaves the stack as a b c d e b.
xn ... x1 n j roll
The roll retrieves the numbers j and n, then performs j cyclic permutations of n entries: xn
... x1. Example: a b c d e 4 2 roll leaves the stack as a d e b c.
To place an element into a table, we have the put operator. This operator takes three arguments: the table, the index of the new element, and the new element. For instance, [ a b
c ] 1 d put returns [ a d b c ]. (Counting starts at 0!) The get operator takes a table and
an index as its arguments and returns the corresponding element in the table: [ a b c ] 2
get returns c. And length returns the length of the table.
As in any other self-respecting programming language, we can define variables in PostScript
as well. But given the nature of the language, “definition” has a rather peculiar meaning here:
defining a variable with the def operator means, in fact, creating a new entry in the current
dictionary. Thus, by writing /foo 2 def, we can say that the interpreter should henceforth
systematically replace foo with 2, but we can also say that we are going to create a new entry
in the current dictionary, with the keyword foo and the value 2.
To create a new dictionary, we use the dict operator, which takes as its argument a whole
number: the size of the dictionary. The reader will notice that the name of the dictionary
appears nowhere. How is that possible? Heavens! Let us not forget that we are always in a
dictionary (the current dictionary) and that we need only define the dictionary that we wish
to create as an entry in the current dictionary. The key for this entry will be the dictionary’s
name. For example, if I write:
```

```text
/foo
10 dict
def
I create a dictionary of size 10 and call it foo. The begin operator, with a dictionary as its
argument, makes that dictionary the current dictionary; in other words, it places it on the top of
the dictionary stack. And end performs the opposite operation: it pops the current dictionary.
For example, to add entries to the dictionary foo, I can write:
foo begin
/bar (abc) def
end
After these operations, the dictionary foo contains an entry—bar—, whose value is (abc).
Another way to write the same operation is:
foo /bar (abc) put
To look up a value in a dictionary, we use get:
foo /bar get
If we do not know in which dictionary a given entry is contained, we use load:
/bar load
The interpreter will then search through all the dictionaries (in the order in which they appear on the dictionary stack) until it finds an entry whose keyword has this name.
To delete an entry from a dictionary, we use undef (which takes as its arguments a dictionary
and a keyword). To check whether an entry exists in a dictionary, we use either known (which
takes as its arguments a dictionary and a keyword) or where (which takes as its argument
a keyword). The former returns a boolean; the latter returns the dictionary containing the
keyword, together with the boolean true, or simply the boolean false, if the entry cannot
be found in any dictionary.
Before concluding this section, let us discuss a somewhat technical operator that nevertheless
often appears in fonts and thus should be well understood. It is the bind operator. It takes a
procedure as its argument and returns the same procedure. Its effect is to take all the operators
in the procedure and replace them with their values, if any. For example, if an operator is the
name of a procedure (in technical terms, a keyword in the current dictionary whose value is a
procedure), the name is replaced by the procedure itself. For example, suppose that we have
defined increase as follows:
/increase { 1 add } def
In other words, increase is a procedure with the effect of adding 1 to the item on top of the
stack. If we now write
```

```text
C.1. Introduction to the PostScript Language
/temporary { increase } def
/stable { increase } bind def
then both temporary and stable are procedures whose effect is the same as increase. What
is the difference? temporary will have the behavior of increase: if we redefine the latter, the
former will also change. stable will have the behavior not of increase but of 1 add, since
bind first replaced increase by its value before def was executed. The action of bind is recursive. Thus we really do process the procedure thoroughly and avoid the risk of depending on
the value of any intermediate variable. Accordingly, the behavior of stable will never change
[unless a virus changes the behavior of add, which would be a great nuisance indeed].
C.1.8
Font Management and Typesetting
Since this subject is the emphasis of our book, we shall discuss it in somewhat more detail.
In the PostScript language, a font (whatever its type) is a dictionary. Fonts are stored in a larger
dictionary called the font directory. When we ask the printer to produce a list of the available
fonts, it is the contents of this dictionary that are explored, and the font names displayed are
those contained in this dictionary.
For example, to use the font Palatino-Roman, when it is already present in the font directory,
at an actual size of 24 PostScript points, we write:
/Palatino-Roman findfont 24 scalefont setfont
which means that we place the keyword for the font onto the stack, and it is then popped by
the findfont operator, which places the dictionary of the corresponding font onto the stack.
Next, we place the number 24 onto the stack; the scalefont pops the font’s dictionary and
the number, and then places a new font dictionary onto the stack: the glyphs are scaled for
setting type at 24 PostScript points; finally, the setfont operator takes the font dictionary off
the stack and makes it the active font.
The scalefont operator affects only the actual size of the glyphs.
We can also distort the glyphs in a more flexible way by modifying the font’s transformation
matrix (whose initial value is part of the font dictionary, as we shall soon see). By writing:
/Palatino-Roman findfont [21.6 0 0 24 0 0] makefont setfont
we multiply the font’s current transformation matrix by
 21.6 0 0
24 0
0 1
, which will yield glyphs
with a “horizontal size” of 21.6 and a “vertical size” of 24 PostScript points—that is, a 24-point
font condensed 90 percent.
To produce the time-honored string “Hello, world!”, we can write:
200 200 moveto (Hello, world!) show
The first moveto is needed so that we will be well inside the page (the current point is by default
(0,0), i.e., the lower left corner of the page). The show operator will typeset the preceding
```

(Voici du texte) show
(Voici du texte) [10 0 ... 10 0] xyshow
5 0 (Voici du texte) ashow
0 5 116 (Voici du texte) widthshow
Figure C-3: The show and three of its variants: ashow (letterspacing), xyshow (equalizing the set-widths of
all the glyphs), and widthshow (the glyph ‘t’ has a slanted width vector). We can see clearly that PostScript
does not manage kerning automatically: the glyphs ‘V’ and ‘o’ are a bit too far apart.
string in the active font (and the data on the current font also include the actual size, as we
saw above).
There are several variants of the show operator:
• string table xyshow retrieves two numbers from the table for every character in the
string. These are the coordinates of each glyph’s width vector. Thus we can set type with
metrics totally different from the font’s original metrics.
• string table xshow is analogous to xyshow except that only one number is retrieved for
each character, since the width vector is horizontal and this number is its length.
• string table yshow is similar, but with a vertical width vector.
• cx cy char string widthshow is a very unusual operator. It sets the string with the
font’s original set-widths, except for the occurrences of the glyph char, which will be set
with the width vector (cx, cy). That is most useful for changing the interword space, by
modifying the width of glyph 32 (the space). It goes without saying that this operator is
so crude that we strongly discourage its use.
• ax ay string ashow letterspaces glyphs (i.e., inserts space between them) in a uniform
manner. The string will be typeset, but with the vector (ax, ay) added to each glyph’s
width vector. Note that this approach to letterspacing is also discouraged because it does
not take kerning pairs into account—which is no surprise, as kerning pairs are not among
the data contained in the font dictionary but are found in an auxiliary file (the AFM file;
see §C.3.7).
• cx cy char ax ay string awidthshow is a combination of the widthshow and ashow
operators.
C.1.9
The Image Model and the Graphics State
Let us review. To fill in a page, we perform four types of operations:
• We draw lines or Bézier curves (with the stroke operator).

C.1. Introduction to the PostScript Language
• We fill the insides of shapes whose outlines are made up of lines and Bézier curves (with
the fill operator).
• We incorporate bitmap images (with the image operator).
• We typeset glyphs taken from fonts (with the show operator).
These operations imply the existence of several parameters that are updated by the various
operators and that have, at any time, a “current” value: the current transformation matrix,
the coordinates of the current point, the current color, the current path, the current stroke
thickness, the current font, etc. All these values make up what we call the “graphics state”.
We can save the current graphics state and return to it at any time, using the operators gsave
and grestore. In fact, there is a stack for graphics states: thus we can save many of them and
recover them one by one in the order opposite that in which they were stored.
We can also create a “graphics state object” and place it on the stack of operands, using the
save operator. We can return to this graphics state at any time by using restore, which retrieves a graphics state object from the stack.
C.1.10
Structured Comments (DSCs)
We have quickly come to realize that describing a page through the use of an interpreted programming language may not always be the best strategy, especially if the software that reads
the code must retain it in memory, ensure that certain resources are present, or retrieve them
before processing the document, etc. That becomes all the more critical when the software is
interactive, as, for example, is ghostscript, which displays a PostScript document for viewing:
when we view a document, we have the desire to change from page to another, to move ahead
several pages, or even to back up. How can we do so if there is no marker in the document
that says “Here is where page 135 begins”, “This document requires the font Throhand-Roman”,
“This document requires 42 megabytes of memory”, etc.?
But how can we introduce this data without imposing in some way upon the authors of
PostScript code? After all, we live in a democracy, and PostScript neither more nor less than
a programming language; each person has the right to prepare her PostScript documents as
she sees fit, as long as the printed result satisfies her. When we raise questions of this sort, the
solution is often to employ metadata. And the only metadata provided by the syntax of the
PostScript language are comments. Adobe therefore declared that a self-respecting PostScript
document must contain several comments of a special type, called “Document Structuring
Conventions” (DSCs). And Adobe took itself so seriously that the specification of these DSCs
[4] runs to no fewer than 109 pages! Adobe requires, among other things, that a certain subset
of the DSCs be respected if a document is to be considered DSC-compliant.
We shall give a few examples and several DSCs related to fonts.
First of all, every DSC-compliant PostScript document must begin with the following line:
%!PS-Adobe-.0
If you believe that the ‘3’ here represents the level of the PostScript language, you are wrong!
It refers to version 3 of the DSCs.

```text
This initial line is at the same time an exception to the general rule that says that all DSC
comments begin with two percent signs. For example, the level of the PostScript language
can indeed be indicated by a DSC: %%LanguageLevel: 2; the document’s bounding box is
given by %%BoundingBox:
579; the virtual memory required for a resource is
given by %%VMUsage: 56000; the date of a document’s creation is given by %%CreationDate:
4 Apr 1998; and so on.
In some cases, the software that produces the PostScript code happens to be genuinely unable to include some data in the DSCs. Imagine, for example, the case of a scientific software
package that draws clouds of points from data on nuclear particles that pass through a membrane. This drawing occurs in real time, and therefore the software has no way to know, at the
beginning of the file, what the final bounding box will be. In that case, we can write (atend)
instead of the data and include the same DSC comment with the correct values at the end of
the document. The instruction (atend) (note: just one ‘t’!) asks the interpreter to wait until
the end of the file to read the data in question.
The DSCs that will concern us below are those related to resources. PostScript categorizes resources into several types, and we shall examine those of the types font and encoding.
If a document requires a font (for example, Palatino-Roman) that is not included in the
PostScript code, the following DSC can be used in the preamble to the file:
%%DocumentNeededResources: font Palatino-Roman
Somewhere in the file (before the corresponding findfont operator), we shall write an instruction to include this resource:
%%IncludeResource: font Palatino-Roman
Note one peculiarity of the syntax: if we have to refer to multiple fonts, we shall write the
keyword only once per line. We can change lines with the comment %%+. Example:
%%IncludeResource: font Foo-Roman Foo-Italic Foo-Bold Foo-BoldItalic
%%+ font Foo-Ciccio Foo-Franco Foo-Laurel Foo-Hardy
Be careful about one detail of some importance. When we ask for a resource to be included,
the request is made of the PostScript interpreter. If this interpreter is located in a printer, the
resource (the font) must be stored there as well. It is then what we call a resident font. Do not
suppose that the printer will go looking for the font on your computer’s disk drive; it is much
too late for that!
If the font is not resident, it behooves us to include it in the PostScript code. In this case, we
use the DSC:
%%DocumentSuppliedResources: font Palatino-Roman
in the preamble. Next, we incorporate the code for the font (in PFA format, if the font is of
Type 1) into the PostScript file, surrounded by the following DSCs:
```

```text
C.1. Introduction to the PostScript Language
%%BeginResource: font Palatino-Roman
... the font ...
%%EndResource
The operation shown above will have the effect of temporarily loading the font into memory,
i.e., only while the current document is being printed.
Now suppose that we wish to load the font into memory permanently. To do so, we create a
special PostScript document [6, pp. 12–13] that will contain a rather special DSC comment:
%!PS-Adobe-.0
%%BeginExitServer: 0
serverdict begin
0 exitserver
%%EndExitServer
%%BeginResource: font Palatino-Roman
... the font ...
%%EndResource
followed by the font, as a PostScript resource. What does this comment mean? What is the
zero (0) that appears twice? Well, it is important to know that a printer, for its own security,
encloses all the PostScript documents that it receives (its “print jobs”) between the operators
save and restore. Thus whatever atrocities we ask it to print, it emerges in its virgin state at
the end of every print job, just as it was when it was first used.
That is all very well, but the system administrator, as the printer’s legal guardian, must still
be able to modify its “permanent state”. To do so, he needs a password (also assigned by the
administrator when he installed the printer). The 0 in the code above is the default password
(administrators often do not bother to change this password).8 The exitserver operator
takes the password offthe stack; if it is correct, the operator breaks the infinite cycle of save
and restore and arranges for the document that follows to be able to make lasting changes
to the printer’s virtual memory.
But let us return to the DSCs. A document of several pages that aims to be DSC-compliant
should include DSC comments of the type:
%%Page: 37 15
at the beginning of the description of each page. (The first number is the number of the physical page; the second is the page number.) We can then be a bit more precise about resources
and say that a certain resource is used on the current page. Smart software will then be able
to load fonts as they are needed for the page that it is currently displaying. The corresponding
DSC comment is:
%%PageResources: font Palatino-Roman
8 We may well wonder why system administrators, usually so passionate about security, do not have
the habit of changing the printer’s password. The answer may be that the effects of this “permanent
configuration”—if it is made within the printer’s virtual memory, as is usually the case—last only until the
printer is next rebooted. The situation is different when one or more hard disks are connected to the printer.
```

Finally, every DSC-compliant file ends with the DSC comment %%EOF (end of file).
Now that we have finished this brief introduction to the PostScript language, we can examine
the PostScript font formats.
C.2
Type 3 Fonts
We shall first describe Type 3 fonts, as they are the closest to the standard PostScript language that we have just described. In fact, the glyphs in these fonts are defined by arbitrary
PostScript operators: everything is permitted, including drawing, filling, including bitmaps,
and even typesetting with other fonts. In theory, any PostScript page could become a single
glyph in a Type 3 font.9 But then why, despite this immense power, have Type 3 fonts been
an unprecedented commercial flop? Why do we find hardly any at all in the world, be they
free or commercial?
Simply because we must not confuse the typesetting of text with graphical design. In typesetting,
we use the graphical elements of fonts, i.e., their glyphs. These are characterized by three
properties: their high degree of repetition (which calls for the optimization of resources),
their small size, and the uniformity of their strokes. The first property (repetition) is managed
very well by all types of fonts, thanks to the structure of the font dictionary. The last two
properties, on the other hand, present a significant problem. If most of the capital letters
have predominantly vertical strokes, the aesthetic tradition would have these strokes be of
the same thickness within a single font. The printer must therefore know that it must assign
the same number of pixels to each of these strokes, whatever their position or the orientation
of the glyphs on the page may be. Worse yet, if we change sizes, the number of pixels in a
“generic” vertical stroke will also change, but the condition of uniformity remains the same:
within a single font, the vertical strokes must have the same thickness, period!
That requirement exceeds the capabilities of PostScript operators: indeed, while we can ask
the printer to draw a stroke with precision, we cannot ask it how many pixels it used for that
stroke so that we can store the number and reuse it for the following stroke. And even if we
could do so, it would greatly slow down an operation that should be the most natural and
the fastest in the world: the typesetting of a simple document.
Type 3 fonts are thus unable to ensure uniform rendering of the glyphs; the result is a poorly
printed document, unless the printer has very high resolution, where the difference of a single pixel is invisible to the naked eye.
Given their enormous shortcomings, how can Type 3 fonts be useful?
They allow us to do things that Type 1 fonts cannot handle: we can use them for dynamic
fonts, random fonts, fonts in color or with gray levels, bitmap fonts, etc. We shall give a few
examples below.
Now let us describe these fonts. A Type 3 font is a dictionary containing the following entries:
• A few global parameters:
9 The reader will recognize here the principle behind the SVG fonts and, in part, that of the virtual fonts
of TEX.

C.2. Type 3 Fonts
– FontType, equal to 3.
– FontMatrix, containing the transformation matrix that allows us to switch from the
font’s system of coordinates to that of the PostScript page. If we draw glyphs on grids
of 1,000 units, this matrix will be the one for scaling by a factor of one thousandth:
[0.001 0 0 0.001 0 0]. Thus 1,000 units of the font will become 1,000 thousandths
of a PostScript point on the page. This quantity will then be multiplied by the actual size: if we are setting type at 10 points, the 1,000 units of the font will become
10 PostScript points, or one em.
– FontBBox, the bounding box of all the glyphs in the font.
– FontName, the font’s name, often used to store the font in the global font dictionary.
– FontInfo, a dictionary of less-important data on the font.
– LanguageLevel, the level (1 or 2) of the PostScript language being used.
• The font encoding: a table of 256 glyph names. Every unused position in the table must
contain the name .notdef (the only name that is allowed to begin with a period).
• Most important of all, a procedure named BuildChar and possibly another named
BuildGlyph.
What do BuildChar and BuildGlyph do?
When the PostScript sets a string using a Type 3 font and the font has a BuildGlyph procedure,
it will apply this procedure to all the characters in the string. For each byte representing a
character, the interpreter must go through the font’s encoding to retrieve the glyph’s name; it
will place it on the stack. Next, it will push the font dictionary onto the stack. Finally, it will
push the BuildGlyph operator, which will pop the name and use it to draw the glyph.
The BuildGlyph operator belongs to level 2 of the PostScript language. If it is not defined in
the font, the interpreter will fall back on the BuildChar operator, which is required at all levels
of the PostScript language. BuildChar will not go through the encoding to retrieve the glyph’s
name; it will use only the glyph’s position in the font table. Which means that a font that
contains only BuildChar cannot easily change encodings. That is why Adobe asks developers
to use a “real” BuildGlyph, and a “phony” BuildChar that invokes it, as follows:
/BuildChar {
1 index /Encoding get exch get
1 index /BuildGlyph get exec
} bind def
The entry Encoding, which is a table, is retrieved from the font dictionary. From this table,
we read the entry whose position is supplied as a parameter, which is the name of the glyph
that we desire. We push this name onto the stack, push the font dictionary onto the stack,
and, finally, retrieve the BuildGlyph procedure from the font dictionary and execute it.
Usually (but this is not at all mandatory) we create a dictionary that contains one procedure
per glyph—a procedure whose name coincides with that of the glyph. Next, we arrange for
BuildGlyph to execute the procedure whose name is given as a parameter.

```text
Note also that BuildGlyph and BuildChar, before drawing anything, must both supply to the
PostScript interpreter the glyph’s width and bounding box, using the setcachedevice operator. This operator retrieves six entries from the stack: two values for the width (horizontal and
vertical) and four values for the bounding box. At the same time, the interpreter will try to
place the image of this glyph in the font’s cache in order to speed up any subsequent access to
the glyph. For internal reasons, when we use setcachedevice, we are not allowed to modify
the current color10 or to incorporate a bitmap by means of the image operator. In that case,
we can use the setcharwidth operator, which supplies only the width of the glyph and does
not attempt to place the glyph in the cache (and therefore has no need to know its bounding
box, which is used only to allocate memory for the caching of the glyph).
To achieve a better understanding of the structure of Type 3 fonts, we shall examine a realworld case: the Type 3 version of the font Computer Modern Roman 10, generated by Graham
Toal in 1990. This font does not contain a BuildGlyph but only a BuildChar. On the other
hand, it contains three different dictionaries: one for the widths, another for the bounding
boxes, and a third for the glyphs’ outlines. The names of the glyphs are of no interest: they are
formed with the prefix char and the position of the glyph in the table, expressed as a decimal
number. These same names are used as keywords in the three dictionaries as well as in the
encoding table.
Here are the font’s global parameters:
/FontType 3 def
/PaintType 0 def
/FontMatrix [.001 0 0 .001 0 0] def
/FontBBox [- - 1006 747] def
/UniqueID 1034 def
and here is the encoding table:
/Encoding [
/char0 /char1 /char2 /char3
/char4 /char5 /char6 /char7
...
/char124 /char125 /char126 /char127
/.notdef /.notdef /.notdef /.notdef
...
/.notdef /.notdef /.notdef /.notdef
] def
which stops at 127 because the Computer Modern Roman 10 font (OT1 encoding) contains only
128 glyphs, plus the pseudoglyph .notdef.
Here are the three dictionaries:
10 The outside of the glyph is considered transparent. For example, when we set type in a color, we use only
one color, that of the interior of the shapes. What is forbidden when we use setcachedevice is the explicit use
of two or more colors other than “transparent”, which is nothing but the absence of color.
```

```text
C.2. Type 3 Fonts
/Metrics 129 dict dup begin
/.notdef 0 def
/char0 621 def
/char1 830 def
...
/char126 499 def
/char127 499 def
end def
/BBox 129 dict dup begin
/.notdef [0 0 0 0] def
/char0 [33 0 578 679] def
/char1 [45 0 782 703] def
...
/char126 [84 570 408 665] def
/char127 [103 565 394 668] def
end def
/CharacterDefs 129 dict dup begin
/.notdef {} def
/char0 {
33 679 moveto
549 679 lineto
...
33 679 lineto
closepath
} def
...
/char127 {
333 667 moveto
390 680 422 594 362 569 curveto
...
93 558 82 655 141 667 curveto
closepath
} def
end def
and, finally, here is the heart of the font, the BuildChar procedure:
/BuildChar {
0 begin
/char exch def
/fontdict exch def
/charname fontdict /Encoding get char get def
fontdict begin
/Metrics charname get 0
/BBox charname get aload pop
setcachedevice
/CharacterDefs charname get exec
```

```text
(1)
(2)
(3)
(4)
Figure C-4: The font Scrabble, by Jacques André [32]. Four consecutive printings of the same document,
with slight random displacements of the letters. Here is the code that produced these three words: 2 8
moveto (JACQUES) show 4 6 moveto (ANDRE) show 4 9 moveto (scrabble) show. We can notice
two things: (a) the capital letters are set horizontally and the lowercase letters are set vertically; (b) the
system of coordinates is such that the numbers given as arguments to moveto are the coordinates of the first
letter of the word according to the game Scrabble.
eofill
end
end
} def
where we first read the position of the desired glyph and store it in the variable char, and
then read the font dictionary, which we store in fontdict. Next we define the procedure
charname as fontdict /Encoding get char get (which pushes the font dictionary onto the
stack, extracts from it the value of the entry Encoding, which is a table, and finally retrieves
the glyph’s name from its position in this table). Then we make the font dictionary the active dictionary, extract from it the entry corresponding to the glyph’s name in the dictionary
Metrics and then in the dictionary BBox (since the bounding box is a table, we retrieve the
elements from the table with aload pop), and finally execute the corresponding entry in the
dictionary CharacterDefs. The latter constructs an outline, which we fill with eofill.
The example font shown above is neither a masterpiece of elegance nor an original and innovative application of Type 3 fonts; it is simply an ordinary text font with the distinction of
being a real-world example.
The other examples of Type 3 fonts that we find are either pedagogical or experimental.
For instance, in [24, p. 341], we find a font whose glyphs are a square and a triangle; in [22,
pp. 219 and 223], we have a similar font as well as a bitmap font; in [303, p. 41], we have a
font whose glyphs are random strokes; and so forth.
As for experimental fonts, Jacques André and Irène Vatton [42] have created a font of extensible mathematical symbols with automatic optical correction; Jacques André once again, but
this time with font designer Christian Delorme [37], has created a font called Delorme whose
glyphs are “contextual”, in the sense that they can build automatic ligatures without requiring
these ligatures to be predefined; finally, this same Jacques André [32] has written the code for
```

C.3. Type 1 Fonts
a Type 3 font for the game of Scrabble, shown in Figure C-4. [33] gives a good description of
these experimental fonts.
Unfortunately, there is less and less software that is compatible with Type 3 fonts. Acrobat
displays them poorly in PDF files, and xpdf refuses to display them at all. Only ghostscript
seems to display them decently, which is to be expected, as this software can display any
PostScript code. As for creating, modifying, and editing these fonts, the situation could not
be worse: no software recognizes them, which is not surprising. The only software that could
even partly process Type 3 fonts was Metamorphosis, from the now-defunct company Altsys.
Metamorphosis would directly convert simple Type 3 fonts, and when that proved impossible,
it would connect to a PostScript printer, download the font, and retrieve its outlines from the
printer in order to produce from it a Type 1 font. Having seen Metamorphosis in action, the
author can confirm that that was indeed possible, but it must be admitted that the Type 1
fonts so generated almost always required manual corrections. One could imagine passing
through a rendering at a very large size and an automatic vectorization of the bitmaps obtained from ScanFont or potrace (see Chapter 12), but the automation of this procedure has
never turned out to be necessary, doubtless because of the small number of Type 3 fonts that
are actually available.
C.3
Type 1 Fonts
In this section, we shall describe the most widely available fonts on Earth (at least if we extrapolate from office-automation software, where TrueType seems to be the leader). Incidentally,
Adobe has managed—God knows how—to make the structure of these fonts an ISO standard!
It is part 3, “Glyph Shape Representation”,11 of ISO standard 9541, Information Technology—
Font Information Interchange, of May 1, 1994 [195].
The structure of these fonts is quite close to that of Type 3, with a few exceptions of considerable importance:
• First, Type 1 fonts do not use the standard PostScript operators to describe outlines; instead, they use a smaller set of special operators.
• Second, they have a number of tools for optimizing rasterizations (the famous hints).
• Finally, they are binary, encoded, and encrypted.
A Type 1 font consists of four components:
• The “public dictionary” (global parameters written in plain text in the font)
• The “private dictionary” (encoded and encrypted parameters that mainly affect the optimization of the rasterization)
11 Reading this specification is a real thrill since one finds in it all the properties of Type 1 fonts—and even
a few hints on the internal workings of the black box that is the Type 1 font renderer—properties described
in a much more serious style than the Adobe specification [21]. One feels that Adobe has put a big effort into
rewriting the specification in ISO’s jargon. Note that the name “Adobe” does not appear anywhere and that
the name “PostScript” appears just once in a footnote in the appendix on compatibility with existing software.

• Subroutines (procedures used in the descriptions of outlines)
• The descriptions of the outlines (also encoded and encrypted), called charstrings
C.3.1
Before We Begin: the Format of the File that Contains
the Font
A Type 1 font is a dictionary that we shall describe in the following section. First, however,
here is a bit of information on the format of the file that contains this PostScript dictionary.
Under Unix and Windows, there are two types of Type 1 files: PFB and PFA. The ‘PF’ shared
by these two types comes from PostScript Font, and the letters ‘B’ and ‘A’ mean “binary” and
“ASCII”, as often happens.
In a PFA file [6, p. 7], the last three parts (private dictionary, subroutines, descriptions of outlines) are encoded in the form of a long hexadecimal string with 512 copies of the character 0
at the end, followed by the operator cleartomark.12
The PFB file [6, p. 9] has adopted a more pragmatic attitude. The encoded and encrypted
part (private dictionary, subroutines, descriptions of outlines) is written in binary, while the
public dictionary remains in ASCII. But how, then, can we know where the binary part begins
and thus exactly which part of the file must be decoded and decrypted? The solution is very
simple. The PFB format assumes that there are two types of data in a PFB font: (1) PostScript
code in ASCII, and (2) encoded and encrypted binary data. Any block of text of type 1 or 2
is preceded by a 6-byte header of which the first byte is always 0xA0, the second is always of
type (0x01 or 0x02), and the last four represent the size of the block in the form of a 4-byte
big-endian number. And the file ends with the two bytes 0xA003.
On the Macintosh, an equivalent system has been adopted. The PostScript code for a font is
stored in a resource group of type POST. The identification numbers of these resources must
begin with the number 501 and be sequential. The resources must not be processed in the
same way by the interpreter: it is the first byte of the resource that indicates to the interpreter
how it must proceed. There are four cases [6, p. 8]: (1) if the first byte is 01, the data are in
ASCII; (2) if it is 02, the data are binary; (3) if it is 03, the resource indicates the end of the
font file; finally, (4) if it is 00, it is a comment that will not be sent to the interpreter.
Since the PFB, PFA, and “POST resource” formats are strictly equivalent, from the point of
view of the data contained in them, there are tools for switching from one to another [175]:
t1ascii (from PFB to PFA), t1binary (from PFA to PFB), t1mac (from PFB or PFA to Macintosh
resources), and t1unmac (from Macintosh resources to PFB or PFA). In the last two cases,
Macintosh resources in the “AppleSingle”, “AppleDouble”, “MacBinary”, or “BinHex” format
are manipulated.
Note that the PFB format is very fragile: specifically, the beginning of the file (aside from
the first six bytes) suggests that it is a text file, and text editors too often have the habit of
12 Its raison d’être is that, when the interpreter decodes the hexadecimal part, it may skip over the nonzero
characters and “swallow” some of the zeroes. It is not important to know how many zeroes are thus used, since
one of the last operators to be decoded is mark, which inserts a mark. The cleartomark returns to that mark,
and everything runs smoothly.

C.3. Type 1 Fonts
converting newlines between the original format of the font (which could be for the Macintosh, Unix, or Windows) and the format of the current platform. But we know that Windows
uses 2 bytes to encode newlines (0x0A followed by 0x0D) where the Macintosh and Unix use
only 1. A modification of this kind, which is harmless enough in a document in text format,
will immediately corrupt the file, since the length of the block of text will no longer be the
same, thus making the header incorrect.
Last but not least, a word on what is to come. Just as elsewhere in this book, rather than discussing the binary structure of the Type 1 font format, we are going to describe the “humanreadable version” of the format. This code cannot be used directly by the computer; there are
tools for converting it to PFB or PFA and vice versa. The tools in question [175] are t1disasm
(which converts PFB to “plain text”) and t1asm (which converts “plain text” to PFB or PFA).
No loss of information occurs among the PFB, PFA, and “plain text” formats: they are three
different representations of the same data.
C.3.2
The Public Dictionary
The public dictionary contains seven obligatory entries:
• FontType, equal to 1.
• FontMatrix, containing the transformation matrix that allows us to switch from the
font’s system of coordinates to that of the PostScript page. If we draw glyphs on grids of
1,000 units, this matrix will be that of scaling by a factor of one-thousandth: [0.001 0 0
0.001 0 0]. Thus 1,000 units of the font will become 1,000 thousandths of a PostScript
point on the page. This quantity will then be multiplied by the actual size: if we are
setting type at 10 points, the 1,000 units of the font will become 10 PostScript points, or
one em.
• FontBBox, the bounding box of all the glyphs in the font.
• Encoding, the font’s encoding; in other words, a table of size 256 whose elements are
names of glyphs (or the name of the pseudoglyph .notdef, if one or more positions are
unused). The position of a glyph name in this table (counting starts at 0) is the position of
the corresponding glyph in the encoding. See §C.3.3 for more information on the glyph
names recognized by Adobe. Two encodings are predefined in Adobe’s implementations
of PostScript: StandardEncoding (Figure C-5) and ISOLatin1Encoding (ISO 8859-1; see
page 36).
• PaintType, equal to 1 if the outlines are to be filled (or to 2 if the outlines are to be drawn,
which we strongly discourage).
• Private, a dictionary of internal information used to optimize the rasterization of the
glyphs.
• CharStrings: a dictionary whose keywords are the names of glyphs and whose values are
descriptions of the outlines of glyphs.
There may also be up to four optional entries:

• FontName, the name of the font, which is often used to store the font in the global font
dictionary.
• FontInfo, a dictionary of optional data:
– FamilyName, the name of the “font family”. Adobe gives us no instructions, other
than the obvious fact that fonts belonging to the same font family must have the
same value of FamilyName.
– FullName, the long version of the font’s name, meant only for the human reader.
– Notice, the font’s copyright message.
– Weight, the font’s weight, in free form.
– Version, the version of the font, in free form.
– ItalicAngle, the slope of the font in degrees, in the trigonometric direction (i.e.,
counterclockwise).
– isFixedPitch, a boolean value (true or false)—is the font monospaced?
– UnderlinePosition and UnderlineThickness, the vertical offset and thickness of the
underline.
• UniqueID, a unique identifier for the font, between 0 and 224 −1 (see below).
• XUID (for “eXtended Unique Identifier”), a table of numbers, of which the first is the
identifier of the “organization” and the others are freely assigned by this organization
(see below).
A few words on the unique identifiers. As poetic as the concept of a “unique identifier” may
seem—are we humans not in quest of a “unique identifier” all our lives?—the utility of these
identifiers is quite concrete: when the interpreter caches rasterized glyphs, these glyphs are
“marked” by their glyph names and the unique identifier of the font to which they belong.
The absence of a unique identifier is not a serious problem: there would simply be more
glyphs in the cache, which would slow printing down slightly and require a little more virtual
memory. But an incorrect assignment of a unique identifier (for example, two fonts with the
same identifier) could lead to catastrophes. And, unfortunately, some font-design software
(such as Fontographer) has the infuriating habit of assigning the same “unique” identifier to
all the fonts that it produces. Thus it is the responsibility of the font’s creator to assign a truly
unique number to the font.
How to do so? In the beginning it was done either by choosing at random a number between
4 million (inclusive) and 5 million (exclusive)—after all, if the number selected is that large,
the probability that another font in the same document will have the same number is very
small—or by contacting Adobe to obtain an “official” number.
Things got better with the introduction of “extended” unique identifiers (with the unpronounceable acronym XUID). An extended identifier is a PostScript table containing whole
numbers. The idea is brilliantly simple: the first number is assigned by Adobe to an “organization”, and all the other numbers are assigned by the “organization”. To register as an “organization”, one must first obtain an Adobe Solutions Network (ASN) account and then register
the “organization’s” name through Adobe’s web site, at https://partners.adobe.com/asn/

```text
C.3. Type 1 Fonts
tech/idreg/xuid/index.jsp). For example, ENST-Bretagne has the XUID 1039. Once this
formality has been completed, the “organization” adds other numbers without justifying
them or explaining them to anyone; it must merely ensure that they are unique. Adobe
delegates the responsibility for uniqueness to the “organizations”. We have written the word
“organization” in quotation marks in this paragraph because there is no control over the registration of “organizations”: it is entirely possible to make one up. There is also no procedure
for searching for the individual behind an XUID number: confidentiality is preserved. All
that we have is Adobe’s guarantee that the XUID number is unique, which is quite a lot in
itself.
C.3.3
Encodings for Type 1 Fonts
The most common encodings for Type 1 fonts are Adobe Standard and Adobe Expert. The first
has the peculiarity of not containing any accented letters: the font may well contain information on combining letters and accents, but these combinations do not appear in the encoding.
The second contains glyphs that are used more in desktop publishing than in office automation, hence the name “expert”: the small capitals; the ligatures “ff”, “ffi”, “ffl”; the old-style
figures; and so forth. One slight inconsistency: while Standard contains no accented letters,
Expert does contain accented small capitals. The reader will find the tables for these two encodings, illustrated with Monotype’s font Columbus, in Figures C-5 and C-6.
In the previous section, we saw that the encoding of a Type 1 font is a table of 256 strings
that are either .notdef (if the position is empty) or glyph names, for which a description
must exist in the font. Everything is fine up to that point. But we may well ask ourselves the
reasonable question: how to select the glyph names?
Like any good programmer (according to Larry Wall [343], a good programmer must be
lazy), let us first ask another question: before we get bogged down in almost metaphysical
problems, does the choice of the glyph’s name matter at all?
Ten years ago, the answer would have been no. What does it matter whether the glyph name
for the glyph “É” is Eacute or foo, as long as the glyph is rendered correctly on the page?
Indeed, if the glyph’s final destination is a sheet of paper, the glyph name is of no importance.
But things have changed since Adobe introduced the PDF file format [28]. Through programs
like Acrobat, xpdf, etc., we do more than just read a document: we interact with it. This interaction may be a search, an indexing operation, or any other operation. But when, for example,
we search for a string in a document, we are searching for characters, not for glyphs. Thus the
software must be able to match the characters with the glyphs.
The encoding table of a PostScript Type 1 font can contain at most 256 entries. The way to
refer to these 256 glyphs in PostScript code is the same as always: in the strings that we typeset
using show (or its avatars), we use either ASCII characters or notations of the type \123 (the
glyph found in octal code point 123 in the encoding). No reference—really, none at all—is
made to the glyph’s semantics. Thus there is no way to recover the character to which this
glyph belongs.
To work around that problem, Adobe came up with the following idea: the correspondence
between characters and glyphs will be established by means of glyph names. The idea is at once
brilliant and absurd. Brilliant, because the glyph names are the only information that we are
assured of having for each glyph; absurd, because the correspondence between characters and
```

0A
0B
0C
0D
0E
0F
1A
1B
1C
1D
1E
1F
!
"
#
\$
%
&
’
(
)
*
2A
+
2B
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
@
A
B
C
D
E
F
G
H
I
J
4A
K
4B
L
4C M
4D
N
4E
O
4F
P 50
Q 51
R 52
S 53
T 54
U 55
V 56 W57
X 58
Y 59
Z 5A
[
5B
\ 5C
]
5D
^ 5E
_ 5F
‘
a
b
c
d
e
f
g
h
i
j
6A
k
6B
l
6C
m
6D
n
6E
o
6F
p 70
q 71
r 72
s 73
t 74
u 75
v 76
w 77
x 78
y 79
z 7A
{ 7B
| 7C
} 7D
~ 7E
7F
8A
8B
8C
8D
8E
8F
9A
9B
9C
9D
9E
9F
A0
¡
A1
¢
A2
£
A3
⁄
A4
¥
A5
ƒ
A6
§
A7
¤
A8
'
A9
“
AA
«
AB
‹
AC
›
AD
fi
AE
fl
AF
B0
– B1
† B2
‡ B3
·
B4
B5
¶ B6
• B7
‚
B8
„ B9
” BA
» BB …BC ‰BD
BE
¿ BF
C0
` C1
´ C2
ˆ C3
˜ C4
¯ C5
˘ C6
˙ C7
¨ C8
C9
˚ CA
¸ CB
CC
˝ CD
˛ CE
ˇ CF
—D0
D1
D2
D3
D4
D5
D6
D7
D8
D9
DA
DB
DC
DD
DE
DF
E0 Æ E1
E2
ª
E3
E4
E5
E6
E7
Ł E8
Ø E9 ŒEA
º EB
EC
ED
EE
EF
F0
æ F1
F2
F3
F4
ı
F5
F6
F7
ł
F8
ø F9
œ FA
ß FB
FC
FD
FE
FF
Figure C-5: The Adobe Standard font encoding, illustrated with the font Monotype Columbus.
0A
0B
0C
0D
0E
0F
1A
1B
1C
1D
1E
1F
!
˝ 22
\$ 24
\$ 25
& 26
´ 27
⁽
⁾
‥ 2A
․ 2B
,
2C
- 2D
.
2E
⁄
2F
:
3A
;
3B
,
3C
—
3D
.
3E
?
3F
a
b 42
¢
d 44
e
i
4A
4B
l
4C
m 4D
ⁿ 4E
o 4F
r
s
t
ff56
fi57
fl58 ffi59 ffl5A
₍
5B
5C
₎
5D
ˆ 5E
-
5F
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
l 6C
m 6D
n 6E
o 6F
p 70
q 71
r 72
s 73
t 74
u 75
v 76
w 77
x 78
y 79
z 7A
₡ 7B
1 7C Rp7D
˜ 7E
7F
8A
8B
8C
8D
8E
8F
9A
9B
9C
9D
9E
9F
A0
¡
A1
¢
A2
ł A3
A4
A5
š A6
ž A7
¨ A8
˘ A9
ˇ AA
AB
˙ AC
AD
AE
¯ AF
B0
B1
‒ B2
-
B3
B4
B5
˛ B6
˚ B7
¸ B8
B9
BA
BB
¼ BC
½ BD
¾ BE
¿ BF
⅛C0
⅜C1
⅝C2
⅞C3
⅓C4
⅔C5
C6
C7
⁰ C8
¹ C9
² CA
³ CB
⁴ CC
⁵ CD
⁶ CE
⁷ CF
⁸ D0
⁹ D1
₀ D2
₁ D3
₂ D4
₃ D5
₄ D6
₅ D7
₆ D8
₇ D9
₈ DA
₉ DB
¢
DC
\$ DD
.
DE
,
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
ð F0
ñ F1
ò F2
ó F3
ô F4
õ F5
ö F6
œ F7
ø F8
ù F9
ú FA
û FB
ü FC
ý FD
þ FE
ÿ FF
Figure C-6: The Adobe Expert font encoding, illustrated with the font Monotype Columbus Expert.

C.3. Type 1 Fonts
glyphs may be more complex than what a measly string (representing a glyph name) could
ever represent.
Nevertheless, such was Adobe’s decision, and the program Acrobat Distiller (which converts
PostScript files to PDF) follows this approach.
Here is what Adobe decided in regard to glyph naming (still with the aim of achieving a
correspondence between glyphs and Unicode characters) [27]:
• First of all, some glyphs already have names that were assigned by Adobe, either because
they are included in one of Adobe’s font encodings or because they have been given
names from Association for Font Information Interchange (AFII), an initiative that still
exists as the ISO 10036 standard [29]. These names are mandatory, and the file [25] contains the list of corresponding Unicode characters (a list called AGL, for “Adobe Glyph
List”, by the initiated).
• If the glyph is not on the AGL but corresponds, say, to Unicode character 0xABCD on the
basic plane (16-bit characters), it will have the name uniABCD.
• If the glyph is not on the AGL but corresponds, say, to Unicode character 0xABCDEF on
one of the higher planes (characters beyond 16 bits), it will have the name uABCDEF.
• If there are several variants of the glyph, each of them will have a name from those described above, followed by a period and a string of characters (capital letters, lowercase
letters, digits). Example: a.gothic, uni0137.alt3.
• In addition to the conventions listed above, if the glyph does not correspond to a single
Unicode character but is instead a ligature, we write the names of the ligature’s constituents, separated by underscores. For instance, the glyph for the ligature ‘ft’ will have
the name f_t. Note: we can have variants of ligatures but not ligatures of variants. In
other words, f_t.gothic has a meaning, but f.gothic_t does not; the latter would be
interpreted as “the variant gothic_t of the glyph f.
Note that some software (such as FontStudio and Fontographer) does not know about these
conventions and does not accept glyph names containing an underscore or a period (with
the exception of the pseudoglyph .notdef).
C.3.4
The Private Dictionary
Now we are entering the dark cave that is the encoded and encrypted part of Type 1 fonts.
Recall that we shall present the data in the form of “plain text” and that the tools t1disasm
and t1asm [175] allow us to convert from plain text to the formats PFB/PFA and vice versa.
The private dictionary contains various and sundry global parameters whose purpose is to
optimize the rasterization of the glyphs. As the optimization mechanism is, in a way, a “black
box”, the role of font creator/optimizer is very limited: we provide a certain set of data to the
PostScript processor and hope that they will be used judiciously.
We can divide the entries of the private dictionary into five categories.

Figure C-7: The relevant heights, with overshoot, of a number of glyphs in various scripts (Latin, Arabic,
Hebrew, Armenian). The font is Omega Serif.
C.3.4.1
Relevant heights
The question arises: what are the most relevant heights of the glyphs? If the font is a Latin one,
a number of candidates occur to us immediately: the height of the capital letters, the height
of the lowercase letters with or without ascenders, the baseline, the depth of the descenders,
etc. For a Hebrew or Chinese font, the relevant heights are certainly different. On the one
hand, owing to certain optical effects, a letter whose uppermost part is curved will be slightly
taller than the letters that are flat on the top: for instance, an ‘O’ will be slightly taller than
a ‘Z’ (at the same point size and in the same font). The difference between the two (the height
of the horizontal line tangent to the upper curve of the ‘O’ and the height of the ‘Z’) is called
overshoot.
The private dictionary can contain the height of the baseline and up to six relevant heights
above the baseline and five relevant heights below it. For each of these heights and depths,
we also specify any overshoot that may exist. The alignment zones thus established must not
overlap; there is even a minimum distance between them that must be respected. Below a
certain number of pixels, the processor will align the glyphs whose heights fall into the same
alignment zone. It is even possible to do so for different fonts belonging to the same “family”:
each font need only know the relevant heights/depths of the “family’s” default font.
We have explained the principle; now let us move on to the representation of this data in
PostScript code, which does not win any medals for simplicity:
• The y-coordinates of the relevant heights and the overshoot values, starting with the baseline, are given in the entry BlueValues in the form of an expanding table of integers.
For example, if the baseline is at 0, the maximum overshoot is -10, the height of the ‘Z’
is 700, and the height of the ‘O’ is 710, then we have two zones: /BlueValues [-10 0 700
710] def.
• The y-coordinates of the relevant depths are shown in the same way in the entry OtherBlues.
• Similar to BlueValues and OtherBlues are FamilyBlues and FamilyOtherBlues, which
contain the corresponding values for the default font in the font “family”.13
13 Quite frankly, we may well wonder what the use of this information is. They would be meaningful if
we could use the “individual” values in a document that employed only one font and the “family” values in
a document containing glyphs from many members of the font “family”. In the first case, priority would go

C.3. Type 1 Fonts
• The entry BlueScale allows us to specify when the processor will stop aligning the pixels
that fall within the alignment zone. The value of this entry is given by the following
formula: if we want alignment to stop at point size p (for a 300-DPI printer), then the
value of BlueScale will be p−0,49
240 .
• Using BlueScale gives us alignment up to a certain point size and “normal” behavior
beyond that point. The entry BlueShift allows us to manage overshoot for sizes beyond
BlueScale. If a given overshoot at a size greater than BlueScale exceeds BlueShift, the
rendering engine will be forced to represent it with at least one pixel. The idea is to regularize the overshoot. Suppose that the letter ‘O’ has upper and lower overshoot values of
5 pixels and that, on the grid that we are using, only one of these overshoot values yields
a pixel. If we set BlueShift equal to 5 (its value is 7 by default), the rendering engine will
produce identical numbers of pixels for each overshoot value, irrespective of the grid.
Only BlueValues is required (but its value may perfectly well be an empty table).
C.3.4.2
Revelant stroke thicknesses
Just as we were able to select the most relevant heights in a font, we can also specify to the
rendering engine the most relevant thicknesses of the horizontal and vertical strokes. For
example, we can indicate the thickness of the downstrokes of the capital letters (that of the ‘I’),
the lowercase letters (that of the ‘l’), the numerals (that of the ‘1’), etc. We can indicate up to
12 horizontal thicknesses and as many vertical ones. If the glyph is slanted, we measure the
thickness perpendicular to the stroke’s central axis.
In our code, we write /StdHW [thickness] def for the most important thickness of a horizontal stroke and /StemSnapH [th1 th2 ...] def, which will contain the 12 most important
thicknesses of horizontal strokes (including the thickness given in StdHW), in ascending order.
For the thicknesses of vertical strokes, we use StdVW and StemSnapV, in the same manner.
One technical note from Adobe [5] is completely dedicated to these four entries in the private
dictionary.
C.3.4.3
Parameters specific to ideographic scripts
The glyphs of the ideographic characters may be among the most complex in the world: there
can be as many as 30 or so strokes in each one, and the glyphs pose a real challenge to rendering engines, whether for printed output or on-screen display.
Adobe offers two methods for addressing this situation:
1. First, we have the possibility of artificially magnifying the representation of a glyph if its
complexity requires. The entry ExpansionFactor is a real number indicating the amount
of expansion allowed for the glyphs in the font: giving it a value of 0.3 means that the
glyph can be magnified by 30 percent. The default value of this entry is 0.06.
to the accuracy of the rendering; in the second case, it would go to consistency between members of the same
family. But is the PostScript processor capable of knowing that several fonts of the same family are used within
the same document? The author has serious doubts.

```text
2. Second, a special mechanism was established at the level of each glyph’s description to
indicate the glyph’s counters (white areas). We shall return to this subject in the section
on the description of glyphs, §C.3.6.2.
One question remains: How does the rendering engine know whether or not the current font
is an ideographic one? Adobe asks us to indicate the answer with the following code:
/LanguageGroup 1 def
/RndStemUp false def
C.3.4.4
Miscellaneous parameters
The entry /ForceBold
true
def tells the rendering engine that the font is boldface and
that the rendering should thus be “fat” (so that the difference between the font and a lighter
version will be immediately noticeable).
The following entries, with the values shown, must be included “for historical reasons”:
/MinFeature{16 16} noaccess def
/password 5839 def
Do not be surprised, dear reader, by the following code at the beginning of the private dictionary:
/-|{string currentfile exch readstring pop}executeonly def
/|-{noaccess def}executeonly def
/|{noaccess put}executeonly def
It defines the three operators -|, |-, and |, which are later used in the code for the font. The
purpose of this maneuver is to improve the legibility of the code. In some cases, these three
operators are named RD, ND, and NP. This code is required.
C.3.4.5
Subroutines and “other subroutines”
Subroutines are blocks of code used in glyph descriptions. These blocks of code must end
with the operator return. The space saved through the judicious use of subroutines can be
enormous. They are stored in an entry in the private dictionary, called Subrs. There is no
limit on the number of subroutines, but the first five (from 0 to 4) are reserved by Adobe:
dup 0 { 3 0 callothersubr pop pop setcurrentpoint return } |
dup 1 { 0 1 callothersubr return } |
dup 2 { 0 2 callothersubr return } |
dup 3 { return } |
dup 4 { 1 3 callothersubr pop callsubr return } |
The code shown above is not the actual code executed by the PostScript interpreter when it
encounters one of these subroutines. On the contrary, it is merely a stopgap—the code to be
executed by interpreters that do not know the secret meaning of these subroutines.
```

C.3. Type 1 Fonts
/e {
52 500 hsbw
394 298 rmoveto
 109 -62 98 -126 vhcurveto
 -128 -78 -107 -151 hvcurveto
 -174 85 -81 125 vhcurveto
 59 0 63 16 52 25 rrcurveto
 -14 48 rlineto
 -50 -26 -51 -14 -46 0 rrcurveto
 -92 -72 54 152 hvcurveto
 13 vlineto
 334 hlineto
 1 13 0 15 0 10 rrcurveto
closepath
-59 7 rmoveto
 -272 hlineto
 9 102 60 53 71 0 rrcurveto
 78 54 -56 -99 hvcurveto
closepath
endchar
} ND













ORIG
ORIG
Figure C-8: The description of the glyph ‘e’ in the font The Sans Mono Condensed Light, by Luc[as] de Groot.
There is another type of subroutine, one that is less interesting for the font designer because he usually cannot modify them. These subroutines—whose name, “other subroutines”,
shows a severe lack of imagination—are written in the ordinary PostScript language, not in
the more limited language of Type 1 fonts. They are stored in the entry OtherSubrs in the
private dictionary.
The entry OtherSubrs is optional unless we are using this format’s advanced features, which
are flex, hint replacement, and the control of counters. Subrs is also optional unless OtherSubrs is being used.
C.3.5
Glyph Descriptions
Glyph descriptions are contained in the dictionary CharStrings (which is at the same level as
Private, in the font’s global dictionary). The keyword for an entry in this dictionary is a glyph
name, one assigned according to Adobe’s conventions (see §C.3.3). The value of an entry in
this dictionary is the description of the glyph in question—a description given in a language
similar to PostScript but highly constrained: only 25 operators in all. A description of this
sort is called a charstring (from the dictionary’s name). We shall later see that the Type 2 font
format includes more sophisticated charstrings, with some 30 additional operators.
Below we shall briefly describe the most important operators. The curious reader will find a
complete description of all the operators in [21, 10].
The first operator in a glyph description must be hsbw (the abbreviation of horizontal sidebearing [and] width). This operator takes two arguments: the left side-bearing (the distance

```text
between the origin of the abstract box containing the glyph and the leftmost point of the
glyph) and the set-width (the glyph’s width vector). It defines the current point as the glyph’s
left side-bearing. Nevertheless, it does not initialize a path. There is an extended version of
this operator: sbw allows for the definition of a side-bearing and a set-width that need not be
horizontal.
To begin to draw, we must first initialize a path. That is done with an operator that effects
movement. There are three such operators: one for arbitrary movement (rmoveto, two arguments), one for horizontal only (hmoveto, one argument), and one for vertical (vmoveto, one
argument). The arguments are always relative: they express motion from the current point.
We can draw straight lines or cubic Bézier curves starting at the current point. For the former,
we use three operators that are similar to the ones used for movement: rlineto (two arguments: the offset of the ending point relative to the starting point), hlineto (one argument:
the horizontal offset), vlineto (one argument: the vertical offset); for the latter, we use the
arguments rrcurveto (six arguments), hvcurveto, and vhcurveto. The operator rrcurveto
has two ‘r’s in its name because it is doubly relative: specifically, the six arguments express the
offset of the first control point relative to the starting point, the offset of the second control
point relative to the first, and the offset of the ending point relative to the second control
point. The other two operators are used for special cases in which the tangent line at the
starting point is horizontal and that at the ending point vertical, and vice versa.
The closepath operator (no arguments) closes a path. Unlike the homonymous operator in
the PostScript language, this one really does require us to close the path with an operator that
completes the drawing; in other words, we must make sure that the starting and ending points
of the path are identical. closepath will only check the validity of a path that has already been
closed. Finally, endchar (no arguments) terminates the glyph’s description. In Figure C-8, the
reader can see a real example of a glyph description.
The remaining operators concern subroutines and hints. Subroutines are called through
callsubr, which takes one argument: the number of the subroutine in question. The code
inside a subroutine is made up of any Type 1 operators and must end with a return. “Other
subroutines” are called through callothersubr, in the same manner.
C.3.6
Individual Hints
“Individual” hints are part of the description of each glyph. A hint is a piece of data, intended
for the rendering engine, whose aim is to optimize the glyph’s rasterization. We have already
seen two types of “global” hints, i.e., those defined at the level of the entire font, or even at
the level of a font “family”: the relevant stroke thicknesses (§C.3.4.2) and the alignment zones
(§C.3.4.1). Adobe calls Type 1 hints “declarative”, in the sense that a font designer is asked to
declare the peculiarities and essential strokes of the font’s glyphs, and Adobe then manages,
in its own way, to make as much use as possible of these declarations.14
At the level of the description of a given glyph, we must first indicate which are the relevant horizontal and vertical strokes. That is done by specifying their coordinates. We use the
operator hstem to indicate a relevant horizontal stroke. This operator takes two arguments:
14 But Adobe cannot guarantee that the rasterization will be perfect, nor can the font’s designer clearly
see the cause-and-effect relationships that these hint declarations entail: everyone is swimming in an artistic
haze, with the peace of mind that everything has been done to make the rendering as good as possible.
```

C.3. Type 1 Fonts
684 57 114
387 444 30 93
413 476 39 92
225 278
411 464
-9
-9
-9
Figure C-9: Potential hints for the letters ‘H’, ‘O’, and ‘m’. The gray zones are the font’s alignment zones.
the lower y-coordinate of the stroke (calculated from the left side-bearing) and the stroke’s
thickness. Similarly, the vstem is used to indicate a relevant vertical stroke, and its two arguments are the left-hand x-coordinate (calculated from the left side-bearing) and the stroke’s
thickness. In the ‘H’ in Figure C-9, for example, the code for the hints of the vertical strokes
and the horizontal bar would be:
57 57 vstem 387 57 vstem 327 48 hstem
In the same figure, we see the font’s alignment zones: the one for the baseline (at 0), the
one for the height of the lowercase letters (at 480), and the one for the height of the capitals
(at 675). These zones are well defined, but they do not suffice for aligning the ‘H’ with the
other letters. Specifically, an individual hint is needed in order for the alignment to take place.
In the case of the letter ‘O’, we have natural horizontal hints: the stroke thicknesses of the ‘O’
at its two vertical extremes. The letter ‘H’ does not have any visual characteristic that can serve
as an “anchor” for horizontal hints linked to the two alignment zones. Thus we use “ghost
hints”, which will apply to the inside of the alignment zones and, as Adobe has decreed, will
have a thickness of 21 units:
0 21 hstem 654 21 hstem
For the letter ‘O’, there is no need for a ghost hint; everything works naturally:
30 63 vstem 413 63 vstem - 50 hstem 634 50 hstem
The letter ‘m’ is special—not only because we want the three downstrokes to have the same
width, but also because we want the white spaces between them to have the same width.

0 57 vstem
300 60 vstem
-3 47 hstem
327 46 hstem
631 46 hstem
(1)
0 57 vstem
276 59 vstem
-3 47 hstem
327 46 hstem
631 46 hstem
(2)
0 57 vstem
300 60 vstem
-3 47 hstem
327 46 hstem
675 -20 hstem
(3)
0 57 vstem
276 59 vstem
-3 47 hstem
327 46 hstem
631 46 hstem
(4)
0 57 vstem
300 60 vstem
-3 47 hstem
327 46 hstem
631 46 hstem
(5)
Figure C-10: An example of replacing four hints in the letter ‘B’. Image 1 shows the initial situation;
images 2 to 5 show the situation after each hint replacement. The thickest stroke is the one drawn in each
configuration of hints.
Adobe has introduced a new operator for this purpose: vstem3 (the ‘3’ doubtless means that
the hint applies to three downstrokes). This operator takes the six arguments that three consecutive vstem operators would have taken, reading from left to right:
39 53 225 53 411 53 vstem3
There is an hstem3 for analogous situations with horizontal strokes (for instance, the Greek
letter ‘Ξ’).
C.3.6.1
Technical peculiarities of hints
In this section, we shall discuss two properties of hints that can prove very useful for improving the rendering of glyphs: hint replacement and flex.
Let us begin with hint replacement. The problem is the following: hints cannot be superimposed. In the case of simple letters, such as ‘H’, ‘O’, or ‘m’, that does not happen. But consider
the letter ‘B’: often the top part of this letter is slightly smaller than the bottom part, but not
so much that the vertical hint for the one will not touch that of the other. We see an example
in Figure C-10: the hint for the bottom part should be 300 60 vstem and the one for the top
part, 276 59 vstem; but we cannot have both at the same time, because they touch. What,
then, should we do?
The makeshift solution given by Adobe [21, pp. 69–71] [234, p. 5] is as follows: we start by
drawing the contours, and at certain times we change the configuration of the hints; i.e., we
erase them all and we redefine them in a way that is optimal for the part of the outline that
we are preparing to draw.
Here is an example from the real world: the hinting of the letter ‘B’ by FontLab. We begin at
the beginning: after the operator hsbw, which initializes the glyph description, we supply an
initial series of hints and draw part of the letter (see part 1 in Figure C-10):
/B {
82 500 hsbw
- 47 hstem 327 46 hstem 631 46 hstem

C.3. Type 1 Fonts
a
(100,-10)
b
(120,-10)
d'
(160,-10)
(140,5)
c
(160,5)
d
(180,5)
e
f
(200,-10)
g
(220,-10)
Figure C-11: An example of flex formed by two cubic Bézier curves, abcd and de fg. The point of reference
is d′.
0 57 vstem 300 60 vstem
360 196 rmoveto
0 90 - 57 - 14 rrcurveto
In parallel, we create a subroutine (here it bears the number 5), into which we place the
second series of hints:
dup 5 {
- 47 hstem 327 46 hstem 631 46 hstem
0 57 vstem 276 59 vstem
return
} NP
In the code for the glyph, we call this subroutine in the following manner (yes, most bizarre):
5 1 3 callothersubr pop callsubr
The hints are then replaced, and we can draw part 2 of the glyph as follows:
70 26 36 62 0 71 rrcurveto
98 - 63 - vhcurveto
We continue in this manner three more times to draw parts 3, 4, and 5 of the glyph. Since
configuration 4 is identical to configuration 2, we can reuse subroutine 5. Configuration 3 is
different from 1 and from 5: FontLab uses a ghost hint, 675 -20 hstem, to align the top part
of the glyph, instead of using the regular hint for the top of the vertical stroke, 631 46 hstem.
Flex [21, §8.3] is a mechanism that manages curves in the shape of horizontal or vertical Gaussian bell curves. It works only for very flat curves (20 units at the most). The ideal application
of flex is at the bottom of serifs (see Figure C-11).
The most important things to know are the conditions that are necessary for a flex to be usable. There are five of these conditions. Let us describe them using the example in Figure C-11:

(1) there must be exactly two cubic Bézier curves, abcd and defg, to be drawn; (2) the endpoints, a and g, must have the same x-coordinate or the same y-coordinate; (3) line ce must
be parallel to line ag; (4) if d′ is the projection of d onto ag, then the distance dd′ must be less
than or equal to 20 units; and (5) the variable BlueShift in the private dictionary must be
strictly greater than dd′. Point d′ is called the point of reference, because all the coordinates are
rewritten with respect to it.
Flex is expressed in the code in a rather obscure way. Suppose that the usual code for the curves
would have been:
100 - rmoveto
20 0 20 15 20 0 rrcurveto
20 0 20 - 20 0 rrcurveto
The final code is the following:
100 - rmoveto
1 callsubr
60 0 rmoveto 2 callsubr
- 0 rmoveto 2 callsubr
20 15 rmoveto 2 callsubr
20 0 rmoveto 2 callsubr
20 0 rmoveto 2 callsubr
20 - rmoveto 2 callsubr
20 0 rmoveto 2 callsubr
50 220 - 0 callsubr
Here we find a call to subroutine 1, which initiates the process; as many rmoveto instructions
and calls to subroutine 2 as there are points between the first control point of the first curve
and the ending point of the second; a call to subroutine 0 with three arguments: the first of
them, very important, is the size, in hundredths of a pixel, below which this pair of Bézier
curves becomes a straight line—the last two are the absolute coordinates of the ending point
of the flex.
C.3.6.2
“Counter control”
Adobe soon noticed that the problems of the letters ‘m’ and ‘Ξ’ look trivial when we start
to set type in other alphabets—in particular, using ideographic languages such as Chinese,
Japanese, and Korean. For instance, the ideographic character 事(koto, “fact, matter”), which
already has no fewer than six horizontal strokes, is eighteenth on the list of the most frequent
characters in the Japanese language [155]. And the character 書(sho, “write”), with its eight
horizontal strokes, is 166th. Not to mention exceptional cases, such as 驫(ky(, “horses”),
which is made up of three copies of 馬(uma, “horse”), and 警(kei, “alert”), which are true
challenges for printers and readers alike.
To address this problem, Adobe introduced a special hint [10] in 1994 for Chinese/Japanese/
Korean glyphs: “counter control”. It involves describing the counters, which are the white
spaces between horizontal or vertical strokes. For simple glyphs such as 目(moku, “eye”) and

C.3. Type 1 Fonts
H1
H2
V1
V2
-90
-114
82 146
265 329
612 676
808 872
525 583
717 775
Figure C-12: The “counter controls” of PostScript Type 1 fonts, illustrated on the glyph 講(k(, “oration”).
皿(sara, “dish”), it is sufficient to give the coordinates of these famous counters in order to
obtain a good rendering, dixit Adobe.
But things become more complicated when the glyph contains several zones with different counters. Take the example in Figure C-12: we have the glyph 講(k(, “oration”), which
has two zones of horizontal counters (“H1” and “H2”) and two zones of vertical counters
(“V1” and “V2”). The problem is as follows: Suppose that the rendering is done so that the
strokes in zone H1 are rendered properly; then if those in zone H2 follow the model of those
in zone H1, the glyph will be deformed. We must be able to treat each of the two parts of
the glyph independently, as if they were two different glyphs. That is what we do, and here
is how:
Let us begin with the horizontal counters of 講. There are five of them in zone H1, and we
can identify them as follows: we give the y-coordinate of the bottom part of the lowest stroke
(-114) and the successive thicknesses of the strokes and counters, proceeding from bottom to
top (24 206 24 112 24 108 24 116 24 106 24), which gives us 12 altogether. Let us proceed
in the same way for zone H2: there are also five counters, but they are arranged differently,
as follows: 42 24 101 24 93 24 76 24 94 24 82 24. We also have two zones for vertical
counters: V1 (525 58 134 58, going from left to right) and V2 (82 58 119 58 103 58 312 58).

We might have expected a handy operator that would take all these values as arguments.
But there is none.15 After a series of technical transformations of no great interest, which is
explained in [10, pp. 13–14], the counter controls are finally declared with the following code:
24 93 24 76 24 94 24 106 - 2 525 58 192 - 82
58 119 58 103 58 370 - 22 12 callothersubr
2 - 24 206 24 112 24 108 24 116 24 130 - 42 24
101 16 13 callothersub
In conclusion, let us note that the order of the zones need not be from bottom to top or from
left to right. In fact, it is the order of their graphical priority: we put the most graphically
important part first. If the interpreter has to choose between rendering one or the other of
these zones correctly, the decision will favor the one that was declared first.
C.3.7
AFM Files
Before proceeding to the other PostScript font formats, let us briefly discuss a type of file that
accompanies practically all PostScript fonts: the AFM file (for “Adobe font metrics”) [12]. The
AFM file is a set of generic and platform-independent metrics from which we can generate
PFM files under Windows or FOND resources on the Macintosh. This approach is similar to
that of BDF files, which make up the “generic bitmaps” from which we can easily produce
other bitmap formats that are more efficient and more appropriate for the various platforms.
There is another very important property that AFM files share with BDFs: they are quite legible to the human eye. We might even say that they were meant to be read by humans, so much
so that the separators and other notational apparatus found in programming languages are
all absent. An AFM file is just a sequence of keywords and values. The overall structure of an
AFM file is also very simple. It is divided into four parts: the heading, the metric properties
of the glyphs, data on letterspacing and kerning, and composite glyphs.
An AFM file is entirely contained between the lines StartFontMetrics 3.0 and EndFontMetrics. The number that follows StartFontMetrics is the version of the AFM format: currently
we are at version 4.1, but the examples given by the specification [12] still use version 3.
The header of an AFM file contains a number of keywords that represent part of the data
contained in the Type 1 font or that add new data:
• FontName (required), the name of the font, as used with the findfont operator of the
PostScript language.
• FullName, a version of FontName that is less strict and intended only for the human reader.
• FamilyName, the name of the font “family”.
• Weight, the font’s weight, in a free form.
• FontBBox, the bounding box of all the glyphs in the font.
• Version, the font’s version, which is taken from the data contained in the font.
15 In fact, it will not appear until the charstrings of Type 2.

C.3. Type 1 Fonts
• Notice, the copyright notice.
• EncodingScheme, the font’s encoding, if it has a name recognized by Adobe, or FontSpecific, in the general case.
• CharacterSet is a little more specific than the font’s encoding: AdobeStandardLatin,
AdobeStandardCyrillic, etc. There is no default value.
• Characters, the number of glyphs in the font.
• VVector (required if the font is set in two directions), the coordinates of the vector that
connects the origin of the first direction of writing to the origin of the second. If this
keyword is present, that indicates that the vector is shared by all the glyphs.
• IsFixedV takes the value true if the keyword VVector above is defined and the value
false otherwise.
• CapHeight, the height of the capitals.
• XHeight, the height of the lowercase letters without ascenders.
• Ascender, the height of the lowercase letters with ascenders.
• Descender, the depth of the lowercase letters with descenders.
• StdHW and StdVW: the entries of the same name in the font’s private dictionary.
• MetricsSets, the number of possible directions of writing: 0 (by default), horizontal; 1,
vertical; 2, both.
Depending on the value of MetricsSets, we have one or two sections StartDirection i ...
EndDirection, where i can take the values 0 and 1. Each such section (which is implicit if
MetricsSet is missing or has the value 0) contains the following entries:
• UnderlinePosition, the y-coordinate of the center of the underline, if any
• UnderlineThickness, the thickness of the underline, if any
• ItalicAngle, the slope of the font, measured in degrees in the trigonometric direction
(thus negative for the usual italic Latin fonts)
• CharWidth, followed by two numbers—the coordinates of the glyph’s width vector, if that
width vector is common to all the glyphs, as is the case for some ideographic fonts
• IsFixedPitch, true if CharWidth exists, false otherwise
Now we come to the section for the metric properties of each glyph. This section is delimited
by the entries StartCharMetrics i ... EndCharMetrics, where i is the number of glyphs described in the section. Each glyph is described in the form of a line containing keyword/value
pairs separated by semicolons, as shown:

C 131 ; WX 599 ; N Eacute ; B 33 0 549 923 ;
Here is the list of possible keywords:
• C, followed by an integer, indicates the glyph’s position in the current encoding, -1 if
none. Note that we can also use hexadecimal numbers: the keyword becomes CH, and
the hexadecimal number, written in uppercase letters, is placed within < and > (e.g.,
CH <91F8>).
• WX, the horizontal part of the glyph’s width vector, if there is only one direction of writing.
If there are two directions of writing, we use the keywords W0X and W1X.
• WY, the vertical part of the glyph’s width vector, if there is only one direction of writing,
otherwise W0Y and W1Y. There are also W, W0, and W1, followed by two numbers, which
combine the two coordinates of the different width vectors.
• VV, followed by two numbers: the coordinates of the vector that connects the origin of
the first direction of writing to the origin of the second.
• N, followed by a string: the glyph’s name.
• B, followed by four numbers: the glyph’s bounding box.
• L, followed by two strings: a ligature. For instance, N f ; L i fi ; means that the glyph f
followed by the glyph i produces the glyph fi.
Then come the data on kerning, placed between StartKernData and EndKernData. We distinguish two types of data: letterspacing (i.e., the overall expansion or contraction of the distance
between the glyphs) and individual kerning pairs (i.e., the drawing together or moving apart
of specific pairs of letters).
Letterspacing values are placed between the keywords StartTrackKern i ... EndTrackKern,
where i is the number of letterspacing values to follow.
Letterspacing values are distinguished by their degree: an integer that is positive if we are moving glyphs apart and negative if we are drawing them together. The degree 0 is the absence
of letterspacing.
Each letterspacing value is described by a keyword
TrackKern d p k P K,
where the parameters are numeric values: d is the degree; p, a small point size; k, the letterspacing corresponding to p; P, a large point size; and K, the letterspacing corresponding
to P. For any point size between p and P, letterspacing will be interpolated; for any point size
outside this interval, letterspacing will remain constant.
The reader will have noticed that something very interesting has happened here. For the first
time in the whole chapter, we have come upon a metric property of PostScript fonts that
is not independent of the point size. Thus, rather than saying that letterspacing is the same at
every point size of the font, we have established limits beyond which letterspacing becomes
constant.

C.3. Type 1 Fonts Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, mes yeux se fermaient si vite que je n’avais pas le temps de me dire : Je m’endors. Et, une demi- heure après, la pensée q Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, mes yeux se fermaient si vite que je n’avais pas le temps de me dire : Je m’endors. Et, une demi- heure Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, mes yeux se fermaient si vite que je n’avais pas le temps de me dire : Je m’endors. Et, Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, mes yeux se fermaient si vite que je n’avais pas le temps de me dire : Je m Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, mes yeux se fermaient si vite que je n’avais pas le temps de me Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, mes yeux se fermaient si vite que je n’avais pas le tem Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, mes yeux se fermaient si vite que je n’avais p Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, mes yeux se fermaient si vite que je n Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, mes yeux se fermaient si vite q Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, mes yeux se fermaient si Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, mes yeux se fermaie Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, mes yeux se fe Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, mes yeux Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, mes ye Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, me Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie étein Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie é Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bou Longtemps, je me suis couché de bonne heure. Parfois, à peine ma b Longtemps, je me suis couché de bonne heure. Parfois, à peine ma L o n g t e m p s, j e m e s u i s c o u c h é d e b o n n e h e u r e . P a r f o i s , à p e i n e m a b o u g i e é t e i n t e , m e s y e u x s e f e r m a i e n t s i v i t e q u e j e n ’ a v a i s p a s l e t e m p s d e m e d i r e : J e m ’ e n d o r s . E t , u n e d e m i - h e Longtemps , je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, mes yeux se fermaient si vite que je n’avais pas le temps de me dire : Je m’endors. Et, Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, mes yeux se fermaient si vite que je n’avais pas le temps de me dire : Je m’e Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, mes yeux se fermaient si vite que je n’avais pas le temps de me dire Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, mes yeux se fermaient si vite que je n’avais pas le temps de Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, mes yeux se fermaient si vite que je n’avais pas le t Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, mes yeux se fermaient si vite que je n’avais p Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, mes yeux se fermaient si vite que je n Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, mes yeux se fermaient si vite q Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, mes yeux se fermaient si Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, mes yeux se fermaie Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, mes yeux se fe Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, mes yeux Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, mes ye Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, me Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteinte, Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éteint Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie éte Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie é Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bougie Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bou Longtemps, je me suis couché de bonne heure. Parfois, à peine ma bo Figure C-13: Two examples of letterspacing in the font Times-Roman for sizes between 5 and 15.5. In the first case, letterspacing varies with the point size throughout its magnitude: TrackKern 1 5 0.5 15.5 1.55. In the second case, letterspacing remains constant below 8 points and above 12 points: TrackKern 1 8 0.8 12 1.2. We can request that letterspacing remain constant below 5 PostScript points and above 240 points. By making that specification, we give the values of letterspacing at its extremes. The value of letterspacing for an intermediate point size is calculated by interpolation from the extremes. In other words, if at every point size below p the letterspacing is k and if at every point size below P it is K, then for c ∈[p,P] the letterspacing will be (K−k)(c−p) P−p +k. Note that nothing prevents us from taking inordinately large values of P and ridiculously small ones of p in order to keep letterspacing from becoming constant in a document. For example, a specification such as TrackKern 10 1 0.1 65535 6553

```text
is entirely possible and will produce letterspacing of one point at point size 10, two points at
point size 20, and so on.
Now we have come to the kerning pairs, which, most of the time, are the only interesting
material in an AFM file. They are placed in a section StartKernPairs i ... EndKernPairs,
where i is the number of kerning pairs to follow. If there are two directions of writing, there
will also be two sections, StartKernPairs0 i0 ... EndKernPairs and StartKernPairs1 i1
... EndKernPairs.
Each pair is written on a line of the type KPX nom1 nom2 k, where nom1 and nom2 are the
names of the glyphs in the pair (in the logical order, thus independent of whether we are
writing from left to right or from right to left) and k is the amount of kerning—positive if we
are moving the glyphs apart, negative if we are drawing them closer together. Example:
KPX F comma -
There are variants of KPX: KPY for vertical kerning, and KP for kerning with two coordinates.
It may happen that some glyphs have no names. In that case, we use their positions in the
encoding, written as hexadecimal numbers, and the keyword becomes KPH. Since KPH is a
variant of KP, it must be followed by two numbers: the coordinates of the kerning vector.
Example:
KPH <305A> <3002> - 0
which expresses (horizontal) kerning between the ideographic character ‘ず’ and the ideographic period, ‘。’, provided that these glyphs have been encoded according to Unicode.
We have come to the final section, the one for composite characters. It supplies complementary data that are ofter indispensable to a Type 1 font, especially if the font does not contain
any glyphs for accented letters.. . .
This section is delimited by the keywords StartComposites i ... EndComposites, where i is
the number of composite glyphs in the font. The description of a glyph of this type takes up
one line, which consists of the keyword CC followed by the name of the glyph and the number, c, of its components, then c instances of the keyword PCC. Each instance of PCC is followed
by the name of the glyph for the component and the coordinates of its width vector. For
instance, if the glyph “circumflex accent” in the font was designed for the letter ‘e’, it may
be moved to the right when it is placed over a ‘w’ (as is done in Welsh) or upward when it is
placed over an ‘E’. Here is an example of a composite glyph:
CC Eacute 2 ; PCC E 0 0 ; PCC acute 195 224 ;
Note that a composite glyph must also appear in the section on the glyphs’ metric properties,
even though its position in the encoding is often -1, as, for example, in the font encoding
AdobeStandardEncoding.
This concludes the description of the AFM font format. There are other keywords that are
specific to Type 0, CID, or Multiple Master fonts. We shall present them gradually in the
description of these font formats.
```

C.4. Multiple Master Fonts Axe 1 : weight Axe 2 : width Axe 3 : optical size 275,350,5 510,350,5 275,850,5 275,600,5 775,600,5 775,600,72 510,850,5 775,600,12 510,600,12 275,600,12 775,850,5 775,350,5 275,350,72 275,850,72 510,850,72 775,850,72 275,850,12 510,850,12 775,850,12 275,350,12 510,350,12 775,350,12 775,350,72 0.1 0.2 0.3 0.4 0.5 0.6 0.7 0.8 0.9 internal values external values (in PostScript points) Axe 3 : optical size (correspondence between internal and external values) Figure C-14: The eight master designs of the glyph ‘A’ in the font Adobe Kepler MM, together with several intermediate glyphs. Next to each glyph, we can read the triplets of values for the parameters. The glyph whose values are 510,600,12 appears in the middle of the cube and is, in a sense, the average value of the glyph ‘A’ in this font. C.4 Multiple Master Fonts The idea is very simple. A master is an outline of a master design, which is most often designed by a human. The computer can interpolate two or more master designs to obtain arbitrary intermediate outlines called instances. Thus we have not only a single glyph for every character but an infinite number16 of instances, described by their coefficients of interpolation from some number of master designs. We can have up to 16 master designs in a Multiple Master font, and they can be organized around four axes of interpolation. Each axis of interpolation is defined by two master designs placed at extreme locations. We can also decide that certain master designs will appear not at the extremities of an axis but at “intermediate positions” along a given axis. Here we have a practical example: the font Adobe Kepler MM is a Multiple Master font with three axes, respectively called “weight”, “width”, and “size”. In the left part of Figure C-14, we see the three axes of the font represented in Cartesian form. The encircled glyphs take on the extreme values and are therefore master designs. Now let us look at the technical side. Multiple Master fonts have a well-deserved reputation for being quite complex. Here is some information that will help us to understand Adobe’s strategy: 1. According to the nature of the axes that have been defined, some properties remain fixed and others vary. For instance, in the case of Adobe Kepler MM, the property ItalicAngle remains equal to 0, regardless of the instance. It is a fixed property. But we can easily 16 In computer science, the term “infinity” means “a very large number”.

```text
imagine a Multiple Master font with one axis for the slope; in that case, the property
would be variable. Thus it is helpful to distinguish the two types of properties in the font.
2. Suppose that a Multiple Master font is sent to an aging PostScript interpreter that does
not know beans about Multiple Master. Instead of getting a stupid PostScript error and
an aborted print job or rendering on screen, would it not be preferable to make do with
even a “standard” instance of the font? To that end, Adobe ensures that all the variable
data appear twice in a Multiple Master font file: the first time, they take only one value,
which corresponds to a canonical “standard” instance; the second time, they appear as
tables with as many values as there are master designs. We can therefore hope that the
obsolete PostScript interpreter will be content with the first values and will ignore the
second.
3. Finally, one little additional complication that is very useful: there are two “spaces” for
the values of the parameters: “external” values, defined by the font’s designer (design values), which may have some typographic semantics (for example, in Figure C-14, the units
of the third axis are true PostScript points for the optical size); and internal (blend values),
which always fall between 0 and 1. Adobe’s brilliant idea was to say that the correspondence between the design values and the blend values is not linear but piecewise linear!
Let us explain. The font Adobe Kepler MM offers optical sizes between 5 and 72. Fonts
grow like humans: the difference (in design) between 6 and 12 points can be enormous,
whereas between 66 and 72 it is certainly much smaller. Thus it would be stupid to
split up the interval [0,1] evenly across sizes running from 5 to 72. On the other hand,
it would be much more prudent to devote a large portion of this interval to text sizes
and to leave a small portion for sizes used in titles. That is what Adobe did: as the right
side of Figure C-14 shows, the blend values between 0 and 0.5 roughly correspond to the
optical sizes from 5 to 13; then the section between 0.5 and 0.8 corresponds to the sizes
from 13 to 18, and only the remaining fifth of the interval is dedicated to sizes beyond 18.
Now we shall see how these data are represented in PostScript code.
A Multiple Master font is, above all, a Type 1 font. Thus it includes a FontInfo dictionary.
We shall store all the “fixed” values in this dictionary. To them we shall add three entries:
1. BlendAxisTypes, a table containing the names of the axes. Example:
/BlendAxisTypes [ /Weight /Width /OpticalSize ] def ;
2. BlendDesignPositions, a table containing a subtable for each master design. Each subtable contains the coordinates of the master design, according to the axes. For instance,
in the font Adobe Kepler MM, we have
/BlendDesignPositions [ [0 0 0] [1 0 0] [0 1 0]
[1 1 0] [0 0 1] [1 0 1] [0 1 1] [1 1 1] ] def
i.e., the eight vertices of the cube in Figure C-14. If some of the master designs are intermediate values rather than extreme ones, that will be seen from their coordinates, which
assume values between O and 1.
```

```text
C.4. Multiple Master Fonts
3. BlendDesignMap, a table containing a subtable for each axis. Each subtable contains subsubtables that are the coordinates of the points that define the linear (or piecewise-linear)
relationship between design values and blend values. Most of the time, we find here only
the extreme design values. In Adobe Kepler MM, for example, the first two subtables of
BlendDesignMap are [[275 0][775 1]] and [[350 0][850 1]], which means that the
design values of the first axis (weight) range from 275 to 775 and that those of the second
axis (width) range from 350 to 850. The third subtable of this font is more complex: it
contains eight correspondences between design values and blend values (see Figure C-14),
which gives us a linear relationship in seven pieces. Here is this table: [[5 0][6 0.15][7
0.24][8 0.30][10 0.44][13 0.50][18 0.80][72 1]].
These three entries are of capital importance, since they define the system of instances globally. Now let us move on to the “variable” data. At the same level as FontInfo, there is a
small dictionary called Blend. There are three entries in this dictionary: FontBBox, FontInfo,
and Private. In each of them we find the customary subentries of Type 1 fonts, except that
here everything is done in a table, with one element for each master design. For instance, the
FontBBox of the font Adobe Kepler MM is:
/FontBBox &#123;&#123;- - - -} {- - - - }
{- - - -} {- - - - }
{1052 1155 1291 1429} {693 816 1103 1183 }
{866 892 925 925} {798 850 854 871 &#125;&#125; def
Here we see eight bounding boxes, for the eight master designs17 (in the order in which they
are defined in BlendDesignPositions).
One little detail that has irritated plenty of people: When we define the Blend dictionary, we
are not in “private territory”. Indeed, we are still in the public part of the font, and the private
part is usually found in the encrypted binary section. Thus we write:
/Blend 3 dict dup begin
/FontBBox&#123;&#123;- ... &#125;&#125;def
/FontInfo 14 dict dup begin ... end readonly def
/Private 14 dict def
end def
and leave it at that, without giving any more information about the Private dictionary. Later,
this dictionary will be filled in with values. Let us take an example, drawn from the font Adobe
Kepler MM. There are six alignment zones in the font, which therefore means 12 values in
BlueValues. Here is the BlueValues entry in the private dictionary of Blend:
/BlueValues[
[ - - - - - - - - ][ 0 0 0 0 0 0 0 0]
[ 630 630 654 654 642 642 655 654 ][ 652 652 676 676 664 664 677 676 ]
17 We have used braces here instead of brackets because FontBBox is considered to be a procedure rather
than a table; thus instead of using a table of tables, we have a procedure of procedures.
```

[ 425 427 430 426 413 413 413 413 ][ 447 449 452 448 435 435 435 435 ] [ 609 609 631 632 613 613 636 634 ][ 626 626 650 650 625 625 650 650 ] [ 655 655 679 679 673 667 705 679 ][ 672 672 701 699 683 677 715 692 ] [ 598 602 622 627 604 599 614 626 ][ 598 602 622 627 604 599 614 626 ] ] def We see that each number has indeed become a table of eight numbers. In some cases, these numbers are identical. That is of no importance: what matters is that we do indeed have a value for each master design. Now let us examine another type of data: that for the standard instance. Specifically, a Multiple Master font must contain various data on a privileged instance. To find out which instance this is, we have three entries18 at the level of Blend: 1. DesignVector, which is a table of numbers containing as many entries as there are axes. These numbers are the design values of the instance. 2. NormDesignVector, which is a table of numbers (between 0 and 1) with as many entries as there are axes. These numbers are the blend values of the instance. 3. WeightVector, which is a table of numbers (between 0 and 1) with as many entries as there are master designs. These numbers indicate the weight of each master design in creating the instance. The total of these numbers must be equal to 1. The font’s private dictionary (the entry Private, at the same level as CharStrings) is the one for the standard instance. Thus an interpreter that cannot understand the font’s interpolation properties can still continue by using the properties of the standard instance, which are quite consistent with those of ordinary Type 1 fonts. Last but not least, we have come to the glyph descriptions. We shall not go into the details here. The principle is as follows: We have the most standard operators of Type 1. But instead of supplying fixed numeric arguments to them, we multiply the number of arguments by the number of master designs and send this mass of data through certain subroutines (numbers 14 through 18) that will interpolate them and give the operators the exact number of arguments that they are expecting—no more, no fewer. Here is an example, drawn from the font Adobe Kepler MM, of what has happened to the extremely simple rlineto operator, which ordinarily takes two arguments (the coordinates of the ending point of the line that is to be drawn): 6 38 - 0 0 - - - - 8 0 15 - - - - 8 15 callsubr rlineto There are indeed 2 × 8 arguments supplied to subroutine 15, which will deduce two arguments from them according to the selected instance of the font and then supply these arguments to the good old rlineto operator for Type 1 fonts. 18 The entries DesignVector and NormDesignVector do not appear in the Multiple Master specifications [10], but they are indeed used in various Adobe fonts. We shall describe them as if they were part of the specifications.

C.4. Multiple Master Fonts
We cannot refrain from emphasizing once more the great weakness of Multiple Master fonts,
which becomes apparent here: all the instances share the same operators; only the values
change. Be the instances of a single glyph ultra-bold or extra-light, be they as wide as a sumo
wrestler or as thin as a statue by Giacometti, be they used in titles spanning five columns or for
the subscripts of variables appearing in footnotes, they always have exactly the same number
of Bézier curves, in the same order and in the same arrangement. That requires unprecedented discipline on the part of font designers and often results in aesthetic compromises.
C.4.1
Using Multiple Master Fonts in the PostScript Language
Ultra-technical though the innards of Multiple Master fonts may be, their use in the
PostScript language is of a childlike simplicity. As explained in [10, §3.7] and [7, §5], we
use the same findfont operator, which will track down the instantiation of the font in a
transparent manner. But how does it know the values of the parameters of the font instance?
Quite simply, from the name of the font.
Specifically, the font’s name is followed by an underscore and one numerical value for each
axis in the font, these values also being separated by underscores.19 For example, to obtain
the instance 385 575 10 of the font Adobe Kepler MM, whose FontName is KeplMM, we simply
write:
KeplMM_385_575_10 findfont
C.4.2
The AMFM file
Every Multiple Master is ordinarily20 accompanied by an AMFM file (for “Adobe Multiple
[Master] Font Metrics”). The format of this file is an extension of the AFM file format; it is
described in [12, §6].
To show that it is AMFM rather than AFM, the file begins with StartMasterFontMetrics 4.1
and ends with EndMasterFontMetrics.
In the preamble to the AMFM file, we find the same global data on the font as in an AFM
file: FullName, FontName, FamilyName, Weight, Notice, Version, IsFixedPitch, etc.
Next, some global data reminiscent of Multiple Master:
• Masters, followed by the number of master designs.
• Axes, followed by the number of axes.
• BlendDesignPositions, BlendDesignMap, BlendAxisTypes, with exactly the same values
as in the font itself.
19 Slight variations on this syntax are possible; see [7].
20 We criticize Adobe for not supplying the AMFM files for the Multiple Master fonts. A high-ranking
official at Adobe with whom the author raised this question said in reply that “the true solution would be to
create software that does not need an AFM file”—an answer that clearly shows Adobe’s reversal in the direction
of OpenType. In any event, to obtain an AMFM file, one need only open and save the font in FontLab. For
reasons of compatibility with older operating systems, the extension that FontLab appends to AMFM files is
.amm.

• WeightVector, the description of the standard instance, with the same values as in the
font itself.
• For each axis, a StartAxis on one line, followed by an AxisLabel with the name of the
axis and an AxisType with the type of the axis (by “type”, Adobe means a keyword selected
from Weight, Width, and OpticalSize), and, finally, an EndAxis.
• A list of “primary” fonts, which are the instances corresponding to the master designs
and the standard instance. The keyword StartPrimaryFonts is followed by the number
of those fonts. Next, for each font, there is a keyword PC followed by the design values
of the instance’s axes (required), and possibly a keyword PL followed by the instance’s
labels (see [7, Appendix B]) and a keyword PN followed by a human-readable font name.
A semicolon comes at the end of this list of values. The list of “primary” fonts ends with
EndPrimaryFonts.
Finally, for each master design there is a section StartMaster ... EndMaster containing the
font names (FullName, FontName, FamilyName), the version (Version), and, most important
of all, the WeightVector of each master design (which is made up entirely of 0s and 1s if it
is at a vertex of the cube but may contain values between 0 and 1 if it is an “intermediate”
master design).
C.5
Type 42 Fonts
Ever since version 2013, PostScript interpreters have contained a TrueType rendering engine.
This engine allows for direct rendering of glyphs found in TrueType fonts, without first going through a conversion to PostScript (which would be catastrophic, since the nature of the
curves is different and the hints in the two systems have absolutely nothing to do with each
other). The only problem is communication: how to transfer data from a TrueType font to
the TrueType rendering engine inside a PostScript interpreter? To this end, Adobe introduced
Type 42 [13].
The reader surprised by this sudden switch from small numbers (Types 0, 1, 2, 3. . . ) to the
number 42 will understand once he has read The Hitchhiker’s Guide to the Galaxy, by Douglas
Adams [2], a gem of British science fiction and British humor, and a must for those who wish
to learn about hacker culture. In this book, the number 42 is of central importance, as it
represents the “answer to the Ultimate Question of Life, the Universe, and Everything”.21
Type 42 combines the PostScript and TrueType formats into one. Does it solve the problems
of these two formats? Not really. A Type 42 must rather be considered as a wrapper for a
21 In fact, according to Adams, an extraterrestrial race designed a supercomputer called Deep Thought to
find the answer to the Ultimate Question of Life, the Universe, and Everything. After seven and a half million
years, Deep Thought proclaimed that the answer is “42”. Thus we noticed that the answer is worthless if we do not
know the question. Deep Thought therefore designed an even more enormous computer to find the question,
after 10 million years of calculations. This computer is Earth, it is powered by mice, and humanity’s reason for
being is to feed the mice. But five minutes before fulfilling its mission, Earth was destroyed to make room for
an intergalactic highway.
Ken Lunde, in [240, p. 280], even gives the name of the person who is responsible for assigning the number 42
to this type of font: Kevin Andresen, an employee of Xerox. Apparently all the computers used by his team
had names drawn from this book, and their network printer was called Forty-Two.

C.5. Type 42 Fonts
TrueType font—a wrapper that is used to send the data to the TrueType processor through
the PostScript language, much as we send a letter through the postal service in an envelope
that the recipient rips open because she is concerned mainly with the letter’s contents.
Nevertheless, it is worth while to study format 42 in order to observe Adobe’s efforts to supply a minimum of data on the font’s glyphs to the PostScript interpreter—data to which the
PostScript interpreter has no direct access because they are stored inside the TrueType code,
which is a sort of black box.
Before we begin, one small detail that could cause big problems if neglected: the current
transformation matrix is [1
0], which means that the units used in the font
are not divided by 1,000, as is the case for Type 1 fonts. Thus one must be careful to use the
correct units when writing values such as the set-width, the left side-bearing, the thickness of
the underline, etc.
Now we shall describe the dictionary entries that are either new or different from those of
Type 1:
• The entries PaintType (was the glyph produced by filling or by drawing outlines?) and
StrokeWidth (the stroke width, if the glyph was drawn with outlines) are required. Recommended values: /PaintType 0 def /StrokeWidth 0 def.
• Here an element in the dictionary CharStrings contains not a glyph description but a
number. This number is the index of the glyph in question within the TrueType tables
loca (table of pointers to the glyph descriptions, which are stored in the table glyf) and
hmtx (table of horizontal set-widths). This approach is quite interesting: it completely
short-circuits the table cmap, and therefore the TrueType font encoding.
• The (optional) dictionary Metrics contains the left-hand side-bearings and the set-widths
of the glyphs: the keywords are glyph names, and the values are tables containing two
numbers [24, §5.9.2]. There can also be tables with four numbers, which will be the two
numbers just mentioned followed by their vertical counterparts.
• Likewise, if we have defined the direction 1 (vertical) in the font, we can have a second
dictionary, Metrics2, with the side-bearings and widths for that direction.
• Most important of all: the entry sfnts contains the data for the TrueType font in the
form of binary or hexadecimal strings. In fact, the value of sfnts is a table containing
one or more strings: it is necessary because strings in PostScript cannot contain more than
65,535 characters. Thus the TrueType code is cut into pieces, which become the elements
of a table.
Finally, an entry that is very interesting but apparently not universally construed in the same
way by all PostScript interpreters: GlyphDirectory. The idea is as follows: It is all very well
to have an entire TrueType font at one’s disposal, but if we actually need only a few glyphs
from the font, what is the point of loading the entire font? The GlyphDirectory dictionary
contains separate TrueType descriptions for each glyph. An intelligent (well, very intelligent)
PostScript driver can reconstruct a TrueType font with only the glyphs that it desires and
deliver that font to the TrueType processor as if nothing had happened. Better yet, the description can begin with the glyph’s metrics (set-width, left side-bearing). For that purpose,
the entry MetricsCount must have the value 2 or 4 (see [13, §5.7]).

C.6
Type 0, or OCF, Fonts
This font format is an example of a bad business strategy. In order to make it possible to set
type in the languages of East Asia without extending the Type 3 or Type 1 fonts to support
more than 256 glyphs, Adobe decided to use hierarchical fonts with several levels, in which
references to characters are dispatched by a central file to subfonts, which ultimately yield
very ordinary Type 3 or Type 1 fonts. These fonts were called “composite fonts”, and the entry for the font type in the FontInfo dictionary took the value 0. Apparently Adobe did not
immediately release precise and comprehensive specifications; as a result, several Asian companies tried to “guess” the specifications (through reverse engineering) and delivered fonts
that were more or less similar but not always compatible. Adobe subsequently developed a
more powerful font format, known as CID, and immediately declared the Type 0 fonts null
and void. The “composite” fonts were then given a new name: OCF (for “original composite
fonts”), where “original” was a synonym for “obsolete”. To this day, Adobe has never stopped
denigrating OCF and singing the praises of CID. Most Asian foundries issue their fonts in
both OCF and CID. (One wonders why, if CID is so much better.)
Now let us examine the description of OCF, based on a bit of information published by
Adobe.
We have already said that OCF fonts are those whose FontType entry takes the value 0.
The first problem that arises concerns the typesetting operator show: how does it handle ideographic languages? Seeking a simple approach, Adobe used the same show operator as for the
Western languages, but its complexity greatly increased at the font level. To set type in Chinese, for example, one would apply the show operator to strings represented by one, two, or
even three bytes, in different encodings. The show operator was expected to adopt completely
different behavior according to the representation of the characters and the encoding of the
text data, while the font remained the same.
In fact, just the opposite is done: the font must be adapted to the text data, and show determines how it is to behave from the type of the OCF font being used. Thus it will use a special
method, according to the font, to interpret the strings. The interpreting procedure will yield
pairs of integers: subfont number plus glyph number. Using these numbers, the interpreter will
finally find the correct glyph in the correct subfont of the OCF font.
Thus there are two important aspects, independent of the OCF font: the aspect of “character
mapping” and the aspect of the “hierarchical organization of the fonts”.
C.6.1
Character Mapping
Character mapping refers to describing the various methods that are available for representing ideographic characters in the form of one or more bytes. Here is the general schema. Each
Type 0 font must contain three required entries:
• FMapType, an integer between 2 and 9 that indicates how strings are to be interpreted in
PostScript code. By applying the correct method, the PostScript interpreter will obtain
pairs of integers consisting of a “subfont number” and a “glyph number”.

C.6. Type 0, or OCF, Fonts
(13, 142)
Encoding
FDepVector
DaiFonto33
/DaiFonto33
...
...
...
...
...
...
Figure C-15: How OCF fonts work: the show operator supplies a pair of integers “subfont number plus
glyph number”; by means of the subfont number, an index for the subfont is obtained from the table Encoding; by means of the subfont index, the name of the subfont is obtained from the table FDepVector; finally,
by means of the subfont name and the glyph number, the much-desired glyph (here, 女, that is, onna, or
“woman”) is obtained.
• Encoding, a table of integers. The interpreter uses the “subfont number” above as an index into this table to obtain a whole number that is the “subfont index”. (Do not confuse
the “subfont number” and the “subfont index”!)
• FDepVector, a table of subfont dictionaries that represents all the descendants of the
“root” font. The interpreter uses the “subfont index” above as an index into this table22
to obtain and load the correct subfont dictionary.
Only one question remains: how to interpret the “glyph numbers” obtained by interpreting
the strings in the PostScript code? That depends on the type of the target subfont. If it is of
Type 1, 3, or 42, it represents the glyph’s position in the subfont table. We need merely go to
the Encoding dictionary of the target subfont to obtain the corresponding glyph name. If the
target subfont is a CID (types 9 to 12), it is a CID identifier; we shall see those in the following
section, which is dedicated to CIDs.
All that remains is to describe the different methods for representing strings. Here they are:
• FMapType equal to 2 (“8/8 mapping”): show reads two bytes per character, the first being
the subfont number, the second being the glyph number. This is what is used, for example, for the JIS and EUC encodings.
• FMapType equal to 3 (“escape mapping”): we have the concepts of “current subfont”
and “escape character”. The escape character is given by another entry (optional, by
default 0xFF) in the font, called EscChar. At the beginning of the string, the current
subfont is number 0. The show operator reads bytes, and if it finds an escape character,
then the following byte is the subfont number of the new current subfont. Otherwise, it
is a glyph number.
22 One may well ask why it is necessary to go through two distinct tables to obtain the subfont dictionary.
Could FMapType not supply the correct subfont dictionary number directly? The answer is that the procedure
allows the same font, with just a change to the Encoding table, to be used for several compatible encodings.
For example, an OCF font can be used in JIS, Shift-JIS, or EUC, and the Encoding table plays a pivotal role.

• FMapType equal to 4 (“1/7 mapping”): a byte is read; its first bit gives the subfont number, and the other bits give the glyph number. The result is rather paltry: two fonts of
128 glyphs each. We would be better offwith a single font of 255 glyphs.
• FMapType equal to 5 (“9/7 mapping”): a 16-bits number is read (the most significant byte
comes first). The first 9 bits represent the subfont number and the remaining 7 bits represent the glyph number. Thus we can have up to 512 fonts of 128 glyphs each.
• FMapType equal to 7 (“double escape mapping”): an extension of escape mapping, described above. If an escape character is followed by a second escape character, a third byte
is read. The subfont number will then be the value of the byte plus 256. With this value
of FMapType, we can have as many as 512 fonts (but the strings may be longer, since there
will be more escape characters).
• FMapType equal to 8 (“shift mapping”): also an extension of escape mapping. Here, however, there are two escape characters, corresponding to the entries ShiftIn (by default 15)
and ShiftOut (by default 14), and only two subfonts are possible, numbers 0 and 1. The
first escape character switches to subfont 1; the second takes us back to subfont 0.
There are also two more sophisticated ways to represent characters: SubsVector and CMap.
The SubsVector method corresponds to an FMapType equal to 6. It uses the value of the entry
SubsVector to describe the method of representation. Suppose that the number of bytes per
character in our method of representation is n. The value of SubsVector is a hexadecimal
string whose first byte is equal to n−1: an initial byte with the value 0x00 means that show will
read one byte at a time, 0x001 means that it will read two bytes at a time, and so on. Next come
as many n-byte groups as there are subfonts. Each of these groups is a number whose value is
the maximum number of glyphs in the subfont. For example, the “8/8 mapping” method uses
two bytes per character, the first being the subfont number (thus a maximum of 256 fonts),
the second being the glyph number (thus a maximum of 256 glyphs). The corresponding
SubsVector string would be 01 followed by 256 repetitions of 0100.
Finally, the method CMap corresponds to an FMapType equal to 9 and works only in Level 3
PostScript. It assumes that a CMap dictionary exists within the font and that it is the dictionary
used for finding a subfont number and a glyph number, in the fashion of CID fonts (see the
following section). By means of this method, we can use methods specific to CID fonts, even
if the root font is not explicitly CID.
The rules to observe when we create Type 0 fonts with several levels of embedding (the root
font refers to composite fonts, which in turn refer to other fonts) are quite complex. The
reader will find them in [24, pp. 363–364].
C.6.2
The ACFM File
As the reader will have guessed, the ‘C’ in ACFM comes from “composite”. ACFM is a special
metric file for composite fonts. Just as with AMFM, we do not find the metrics of individual
glyphs in an ACFM file, only general data about the subfonts of the OCF font.
An ACFM file is enclosed within a section StartCompFontMetrics
... EndCompFontMetrics. The entry Descendents gives the number of subfonts provided in the OCF font. After the usual global entries (FontName, FontBBox, Version, etc.) come several entries specific

C.7. CID Fonts (Types 9–11, 32)
to OCF: EncodingScheme, MappingScheme, EscChar, CharacterSet, Characters, and IsBaseFont, which take the same values as their counterparts in the font.
Then follows a section StartDescendent min max ... EndDescendent for each subfont. The
values min and max give the values of the characters in the original string that correspond
to the glyphs in the subfont. For each subfont, there are the usual global entries (FontName,
FontBBox, Version, etc.) and the entry IsBaseFont, which here takes the value true. We can
also have global glyph metrics: in ideographic fonts there is often a CharWidth 500 0, which
means that all of the glyphs in the font have a set-width of 500 units.
Clearly the description of an OCF font in an ACFM file is only the tip of the iceberg. It is also
necessary to have an AFM file for each subfont.
C.7
CID Fonts (Types 9–11, 32)
The idea behind CID fonts is very simple. Over the past 10 years, Adobe has defined “character collections” (incorrectly named character collections, although they concern glyphs, not
characters), containing numbered glyphs: typically we have one character collection for traditional Chinese glyphs, another collection for simplified Chinese glyphs, a collection of Korean glyphs, a collection of Japanese glyphs, etc. CIDs are fonts whose glyphs have no names
but are described in relation to a character collection.
A member of a character collection is identified by a number called “CID” (glyph identifier),
whence the name of this type of font: the glyphs are identified by the CID numbers of a given
character collection.
For a CID font, at least two files (or two PostScript resources) are needed:
• The first is called CMap (for “character map”), and it establishes the correspondence between characters (as read by the PostScript show operator) and glyphs, in a character
collection. Thus it is a somewhat peculiar font encoding: instead of using glyph names as
its basis, as do the Type 1 font encodings, it uses CID—i.e., the glyph numbers in a given
character collection.
• The second is called CIDFont, and it is a sort of Type 1 font with up to 65,536 glyphs that
are indexed not by glyph names but by CID numbers.
The traditional findfont operator establishes the connection between CIDFont and CMap:
put together, these data form a CID font. Thus we can have arbitrary fonts with arbitrary
encodings:23 the font encoding becomes a separate file, and the merging of the font encoding and the part of the font that contains the glyphs is done automatically when the font is
declared in PostScript code.
Below we shall describe CMap and CIDFont files/resources separately. The official specification is found in [11], but [24, pp. 364–370] and [9] are also good introductions to the subject.
23 The concept is not far removed from that of virtual fonts in TEX: the font defined by findfont can borrow
glyphs from all sorts of fonts (Type 1, Type 3, CID, etc.), in any encoding. The difference is that a virtual font
can also combine multiple glyphs into one, which is not possible with the CMap.

DSC Comments
Global entries
Font mini-dictionaries
Font mini-dictionary 1
Font mini-dictionary 2
Font mini-dictionary 3
Font mini-dictionary 4
...
Font mini-dictionary n
Pointer to charstring
Charstring
Pointers to subroutines
Subroutines
CID
Figure C-16: The overall structure of a CIDFont file (of CID type 0) and the path that must be followed
to obtain the data needed for rendering the glyph. The starting point is the datum for the CID number.
C.7.1
CIDFont
The CIDFont file exists in four flavors, identified by their CID type number but also by their
“traditional” type number (the same type as for fonts of Type 0, Type 1, Type 3, etc.). Here
are these four flavors:
• CID type 0, or “Type 9”: the glyphs are described by charstrings, as in “Type 1”
• CID type 1, or “Type 10”: the glyphs are described by BuildGlyph procedures, as in
“Type 3”
• CID type 2, or “Type 11”: the glyphs are described by TrueType code, as in “Type 42”
• CID type 4, or “Type 32”: the glyphs are bitmaps
Be careful not to confuse “CID type 0” (“Type 1” CID) with “Type 0” (OCF) or “CID type 1”
(“Type 3” CID) with “Type 1”.
To understand the structure of a CIDFont file, let us recall what a Type 1 font is: global data
(“public” and “private”), including the encoding, subroutines, and a set of glyph descriptions.
In the case of CIDs, the encoding is absent (because the glyph name is replaced by the CID
identifier to which we have access through a simple table of pointers), and the glyph descriptions do not change. This situation may pose a problem: the “global” data may not be
sufficiently global. Specifically, if in a font we mix Latin letters and Chinese ideographs, it is
unlikely that the same hinting parameters or the same subroutines will be optimal for both.
Thus it would be more desirable to classify the glyphs into a number of sets that share the
same characteristics and to create for each set a “mini–font dictionary” containing the set’s
“private” parameters and subroutines. By “mini–font dictionary”, we mean a structure similar to a Type 1 font dictionary, but without the encoding, subroutines, and glyph descriptions.
Then each glyph identifier (CID) will be associated with one of these mini–font dictionaries.

C.7. CID Fonts (Types 9–11, 32)
When the CMap asks the CIDFont to draw a glyph by supplying the glyph’s CID, the interpreter will first look up the CID’s entry in a table (see Figure C-16). This table will supply two
things: a pointer to the glyph’s description, and a number for the corresponding mini–font
dictionary. For rendering the glyph, the glyph description is not sufficient: the code for the
subroutines, which are also contained in the binary section, is also required. The mini–font
dictionary provides a pointer to the table of subroutines, which in turn supplies pointers to
the subroutines themselves.
The structure of a CIDFont file is quite simple: there are a few structured comments, a few
global entries, a few mini–font dictionaries corresponding to the different types of glyphs in
the CID font, and an enormous binary section containing descriptions of the glyphs en masse,
which sometimes occupies up to 99.9 percent of the space in a CIDFont file.
The section for structured comments in a CIDFont resembles the following code:
%!PS-Adobe-.0 Resource-CIDFont
%%DocumentNeededResources: ProcSet (CIDInit)
%%DocumentSuppliedResources: CIDFont (WadaMin-Regular)
%%IncludeResource: ProcSet (CIDInit)
%%BeginResource: CIDFont (WadaMin-Regular)
%%Title: (WadaMin-Regular Adobe Japan1 1)
%%Version: 3.002
In the Title field, we have the font name followed by three pieces of data that define the
character collection with which it is associated (see below).
Next come some global entries that stem from the Type 1 font entries—FontBBox, FontInfo,
etc.—as well as a few entries specific to CID fonts. Of the latter, a few are used for identification:
• CIDFontType: the CID type.
• CIDFontName: the font name.
• CIDSystemInfo: a subdictionary containing three entries of crucial importance. These
entries define the character collection with which the font is associated:
– Registry: the name of the organization that defined the character collection.
– Ordering: the name of the language, followed by a number to cover the possibility
of having multiple character collections for the same language.
– Supplement: an integer indicating the version of the “supplement”. A supplement is
a batch of glyphs defined at a given moment. Glyph collections are built up from
successive supplements. A CID, once defined, cannot be deleted or replaced, but new
CIDs can be defined as often as we wish.
• CIDFontVersion: the font’s version.
Here is an example of entries used for identification:

```text
20 dict begin
/CIDFontName /WadaMin-Regular def
/CIDFontVersion 3.002 def
/CIDFontType 0 def
/CIDSystemInfo 3 dict dup begin
/Registry (Adobe) def
/Ordering (Japan1) def
/Supplement 1 def
end def
/FontBBox [ - - 1023 900 ] def
/UIDBase 2483200 def
/XUID [1 11 2483200] def
/FontInfo 5 dict dup begin
/Notice (\050c\051 Copyright 1996 Adobe Systems
Incorporated. All rights reserved.) readonly def
/FullName (WadaMin-Regular) readonly def
/FamilyName (WadaMin-Regular) readonly def
/Weight (Medium) readonly def
/FSType 4 def
end readonly def
Next there are four more technical entries that are indispensable for entering the binary
section. To understand them, we need only give the description of this block. It begins with
a table of fixed-length records. Each of these records is divided into two parts: the first part
contains the number of a mini–font dictionary, and the second contains a pointer to the start
of a charstring, calculed as the offset of bytes from the beginning of the binary section. The
length, in bytes, of these two sections is given by the entries FDBytes and GDBytes. The records
correspond to consecutive CID numbers. The first record corresponds to the CID number
given by the entry CIDMapOffset. The number of records is given by the entry CIDCount,
which is the fourth and last of the “technical” entries. Example:
/CIDMapOffset 0 def
/FDBytes 1 def
/GDBytes 3 def
/CIDCount 8286 def
Finally, there are the mini–font dictionaries. These contain the usual entries of a Type 1
font—BlueValues, BlueScale, BlueFuzz, BlueShift, StdHW, StdVW, StemSnapH, StemSnapV,
etc.—as well as three entries specific to CID fonts that give access to subroutines. Once again,
it is important to know that the code for the subroutines in the binary section is preceded
by a table of records of fixed length. The entry SubrMapOffset is a pointer to the record corresponding to subroutine 0 in the current mini-dictionary, SubrCount gives the number of
records, which is the number of subroutines that apply to this mini-dictionary, and SDBytes
gives the length of each record in bytes. Each record contains a pointer to the beginning of
```

```text
C.7. CID Fonts (Types 9–11, 32)
the code for a subroutine. Counting always begins at 0. There are no “other subroutines”
(OtherSubr), because these are defined in the global private dictionary of the CIDFont file.
The mini-dictionaries are subentries of the entry FDArray:
/FDArray 5 array
dup 0
14 dict
%beginning of mini-dictionary 0
begin
/FontName /WadaMin-Regular-Alphabetic def
/FontType 1 def
/FontMatrix [ 0.001 0 0 0.001 0 0 ] def
/PaintType 0 def
/Private 18 dict dup begin %beginning of private section
/MinFeature{16 16}def
/BlueValues [ - 0 800 806 550 575 ] def
...
/SubrMapOffset 33148 def
/SDBytes 3 def
/SubrCount 119 def
end def
%end of private section
currentdict end %end of mini-dictionary 0
put
dup 1
14 dict
%beginning of mini-dictionary 1
begin
/FontName /WadaMin-Regular-Dingbats def
...
def
Thus we see that while the font name used in our example24 is WadaMin-Regular, the names
of the mini-dictionaries consist of the same name followed by -Alphabetic and -Dingbats.
In this same CID font, there are three other mini-dictionaries: -Generic, -Kana, and -Kanji.
Finally, after the final def of the entry FDArray, comes the binary section. This section is
preceded by a call to the procedure StartData, which takes two values: a string that is either
(Binary) or (Hex) (if the latter, the data are encoded in hexadecimal), and a number indicating the exact length of the binary data. The keyword StartData must be followed by a space.
The first byte after the space is the first byte of the data. At the end of the data, three structured
comments conclude the file with a flourish:
24 It is a Japanese font freely distributed by Adobe [23].
```

%%EndData
%%EndResource
%%EOF
Last but not least, one very important piece of data: the binary section contains no global
parameters, only charstrings and subroutines, which can be read as needed. There is no need
to keep all this data in memory. The PostScript will therefore keep the global parameters
and the mini-dictionaries in memory and will leave the binary section on disk, thus allowing
Chinese/Japanese/Korean to be typeset on printers with very little RAM available.
C.7.2
CMap
A CMap file is an ASCII file that defines the correspondence between a character encoding
and a character collection. There are two types of CMap files: “abstract” ones, which make
no reference to a given font, and “concrete” ones, which invoke one or more fonts and thus
allow for combining the glyphs of multiple fonts.
Let us begin with “abstract” CMap files. A file of this kind begins with a few structured comments, an identification block, and a number of tables that contain the correspondences
between characters in the input and CIDs in the output, etc.
The block of DSC structured comments is typical:
%!PS-Adobe-.0 Resource-CMap
%%DocumentNeededResources: ProcSet (CIDInit)
%%DocumentNeededResources: CMap (90ms-RKSJ-H)
%%IncludeResource: ProcSet (CIDInit)
%%IncludeResource: CMap (90ms-RKSJ-H)
%%BeginResource: CMap (90ms-RKSJ-V)
%%Title: (90ms-RKSJ-V Adobe Japan1 2)
%%Version: 11.001
%%EndComments
Note that lines 2 and 4 indicate that the current CMap (90ms-RKSJ-V) is based on another
CMap, called 90ms-RKSJ-H. The difference between the two is that 90ms-RKSJ-H contains the
glyphs for horizontal kanji ideographs, whereas 90ms-RKSJ-V (less often used) contains only
the specifically vertical glyphs and shares the vast majority of its glyphs with the first (which
are thus both horizontal and vertical). In this case, we will find the operator usecmap at the
beginning of the file, as follows:
/90ms-RKSJ-H usecmap
to load the data from the other CMap file.
The identification block contains the following entries:
• CIDSystemInfo, a dictionary containing three subentries—Registry, Ordering, Supplement—which are strictly the same as for the CIDFont

C.7. CID Fonts (Types 9–11, 32)
• CMapName, followed by the name of the CMap
• CMapVersion, followed by the version expressed in the form of a rational number
• CMapType, equal to 1
• possibly an XUID, similar to that of the Type 1 fonts
• WMode, followed by 0 if the direction of writing is horizontal, and 1 if it is vertical
Here is an example, again drawn from the same CMap:
/CIDSystemInfo 3 dict dup begin
/Registry (Adobe) def
/Ordering (Japan1) def
/Supplement 2 def
end def
/CMapName /90ms-RKSJ-V def
/CMapVersion 11.001 def
/CMapType 1 def
/XUID [1 10 25344] def
/WMode 1 def
Next begin the tables of correspondences. As a general rule, each table foo is delimited by the
operators beginfoo and endfoo. The operator beginfoo is preceded by the number of entries
in the table. A table can contain at most 100 entries; if more are needed, we start a new table
of the same type.
The first table, codespacerange (CID), indicates the set of valid characters—i.e., those that we
expect to read in the input. It turns out to be crucial for knowing whether we should read 1, 2,
3, or 4 bytes in the input in order to obtain one character. For example, the codespacerange
of the Shift-JIS encoding is
4 begincodespacerange
<00> <80>
% JIS X 0201- Roman
<8140> <9FFC> % The first 16-bit block
&lt;A0&gt; &lt;DF&gt;
% Half-width katakana
&lt;E040&gt; &lt;FCFC&gt; % The second 16-bit block
endcodespacerange
which means that we can expect to read single bytes between 0x00 and 0x80, or between 0xA0
and 0xDF. But if we ever come upon a byte between 0x81 and 0x9F, or between 0xE0 and 0xFC,
we will read a second byte, and the two bytes together will form the character from the input.
The most important table is the one that matches characters with CIDs. For practical reasons,
these tables come in two types: one for ranges of consecutive characters and CIDs (cidrange),
and one for isolated characters (cidchar). Example:

```text
2 begincidrange
<20> <7F>
&lt;A20&gt; &lt;A7F&gt;
endcidrange
2 begincidchar
<80> 247
&lt;FFFD&gt; 3972
endcidchar
In this example, we match the consecutive characters between 0x20 and 0x7F with the same
number of consecutive CIDs, starting with CID 132 (and therefore ending with CID 240; there
is no need to write it explicitly). Next, we match the interval [0xA20, 0xA7F] to the CIDs [847,
955]. Finally, the second table allows us to match the characters 0x80 and 0xFFFD directly with
the CIDs 97 and 3972. Reminder: hexadecimal numbers can be recognized by the fact that
they are enclosed in angle brackets.
What happens if the input contains a character for which there is unfortunately no CID in
the font? Remember that in Type 1 fonts we must always have a glyph called .notdef, which
takes care of such situations. Here, however, we can have a different glyph according to the
range in which the character appears. Those glyphs are configured in the table notdefrange,
by which ranges of characters are matched to CIDs. Example:
1 beginnotdefrange
&lt;A1&gt; &lt;DF&gt; 1
endnotdefrange
which maps the characters between 0xA1 and 0xDF (in the Shift-JIS encoding, these are the
half-width katakana ｶﾀｶﾅ; compare the full-width katakana, カタカナ) to CID 1. Everything
that is not listed is mapped to CID 0. What is the benefit of this operation? If we leave aside
for the moment any possible kerning, all the ideographs have the same set-width. Some of
them are condensed and have half the width of the others. If the glyph for substitution has
the same width as the missing glyph, the document’s layout will be preserved, despite the
substitution of glyphs.
Finally, we can indicate the font’s current transformation matrix with the operators beginusematrix [...] endusematrix.
C.7.3
Rearrangement of a CID font
Now let us discuss the “concrete” CMap fonts [11, §6]. The problem that must be solved is the
following: when we write, for example, in Japanese, we merrily mix four types of script. These
scripts are the kanji (漢字) ideographs of Chinese origin, the syllabic scripts hiragana (ひら
がな) and katakana (カタカナ), and the altered Latin script romaji. “Altered”, in the
sense that the Latin letters must obey the same rules for set-width as the ideographs: thus they
will be of full width or of half width, even if that seems a
little
bizarre
to
us
Westerners. A self-respecting Japanese CID font will necessarily
contain the glyphs required for these four types of script.
```

```text
C.7. CID Fonts (Types 9–11, 32)
Now suppose that we wish to mix our kanji with the kana of another font and with the
Latin letters of yet another font. The visual result is certainly promising, but we will have
to change the font, using the mouse, every two or three characters from the beginning of the
document to the end, which means thousands of times. Could we do so without losing our
mental health? Not likely.
Once again approaching TEX’s concept of virtual fonts, Adobe offers another type of CMap
file, with explicit indication of the fonts being used. The procedure is called font rearrangement,
and we can use it to combine any number of fonts of any type (Type 0, Type 1, Type 3, Type 42,
or CIDFont). Each font can have its own current transformation matrix and can also be scaled,
translated, rotated, or reflected.
The syntax is very simple: first, we use the operator beginrearrangedfont to define the new
font and to indicate the fonts on which it will be based. This operator takes the name of the
font as its first argument and a table containing the names of the base fonts as its second
argument. Example:
/Jun101-Light-K-G-R-pv-RKSJ-H
[ /Jun101-Light-pv-RKSJ-H
/Palatino-Roman
/ShinseiKai-CBSK1-pv-RKSJ-H
/FutoGoB101-Bold-pv-RKSJ-H
/FutoMinA101-Bold-pv-RKSJ-H
/HSMinW3Gai30
] beginrearrangedfont
In the first position (position 0), we have the original font; then, in any order, come the fonts
from which we are going to borrow glyphs. For example, in position 1, we have the font
Palatino-Roman, which is of Type 1. The rearranged font should be regarded as a variant of
font 0, which thus is of paramount importance; in particular, font 0 must be a CID font.
The usefont operator takes the font number in the table as its argument. But since up to now
we have seen only cidrange and cidchar tables that return CID numbers, which non-CID
fonts do not have, we need a new type of table: the bfrange and bfchar tables (“bf” comes
from “base font”) match up ranges of characters or isolated characters with glyph names or
code points in the font’s encoding.
For example, by writing:
1 usefont
1 beginbfrange
<30> <39> <30>
endbfrange
2 beginbfchar
<5C> yen
<7F> <7F>
endbfchar
```

we replace the digits, the yen sign, and the mysterious character 0x7F in Jun101-Light-83pvRKSJ-H with those from Palatino-Roman. We can use the operators beginusematrix [...] endusematrix with a different value for each base font. We write the number of the font as the argument to the operator beginusematrix: 1 beginusematrix [1.1 0 0 1.1 0 0] endusematrix Here we scale the glyphs from the font Palatino-Roman up by a factor of 110 percent. One last small detail: to ensure the successful inclusion of all the files needed for the PostScript project, we should also include a number of structured comments at the beginning of the file, as shown: %!PS-Adobe-.0 Resource-Font %%ADOResourceSubCategory: RearrangedFont %%DocumentNeededResources: procset CIDInit %%+ font Jun101-Light-pv-RKSJ-H %%+ font Palatino-Roman %%+ font ShinseiKai-CBSK1-pv-RKSJ-H %%+ font FutoGoB101-Bold-pv-RKSJ-H %%+ font FutoMinA101-Bold-pv-RKSJ-H %%+ font HSMinW3Gai30 %%IncludeResource: procset CIDInit %%IncludeResource: font Palatino-Roman %%IncludeResource: font HSMinW3Gai30 %%BeginResource:Font Jun101-Light-K-G-R-pv-RKSJ-H %%Version: 1 C.7.4 The AFM File for the CID Font Unlike OCF fonts, which have their own AFM file format called ACFM, the CID fonts use ordinary AFM files. Only two differences reveal that the font is a CID font: an entry IsCIDFont, which takes the value true, and the fact that there are numbers instead of glyph names. C.7.5 Using a CID Font Last but not least, how do we use a CID font in a PostScript file? We simply use the classic findfont operator and specify as its argument a CIDFont name followed by two hyphens and a CMap name [11, Appendix B]: WadaMin-Regular--ms-RKSJ-V findfont There could hardly be a simpler approach. If the font is a rearranged font, we use the name of its CMap.

```text
C.8. Type 2/CFF Fonts
C.8
Type 2/CFF Fonts
Type 2 and CFF fonts are the ne plus ultra of Adobe font technology. There has never been
a Type 2 font or a CFF font.25 If the reader finds these two sentences contradictory, she does
not know Adobe very well. Let us clarify the matter (as much as we can): “Type 2” [15] is
not a type of font but a type of charstring—in other words, a type of glyph description. The
charstrings of traditional Type 1 fonts were of Type 1, without being aware of it. Now we have
charstrings of Type 2, which are more powerful and more efficient.
CFF (for “compact font format”) [14] is not a font format either, despite its name. It is a way
to compress existing font formats, in particular the two most successful formats: Type 1 fonts
and CIDs.
Wait! We are not finished. When we compress Type 1 or CID fonts, Adobe requires us to use
charstrings of Type 2. Can we use the result as an alternative to traditional fonts? Is it a new
type of font? Not at all! The only way to use a CFF font is within an OpenType font, in the form
of a CFF table.
Thus both Type 2 and the CFF format were created to make PostScript fonts easier to incorporate into an OpenType font structure.26 There has been a precursor to this: at some
time, in the early days, it was possible to insert a complete Type 1 PostScript font in a special,
nowadays obsolete, TrueType table called typ1. On the Mac, such a font looks like any other
TrueType font (a font suitcase containing a sfnt resource), it is only by investigating the tables
contained in the TrueType structure that one discovers the existence of PostScript data. Once
extracted, the PostScript data can be saved in a PFA file and used normally.
C.8.1
The Compact Font Format
This format is a different way to write code in binary, more powerful than the approach of
Type 1 fonts. Fortunately, the tool TTX, used to display OpenType fonts in a human-readable
form, can also handle CFF code. In this book, we have decided to (re)present TrueType and
OpenType code using TTX; and CFF will be no exception. Thus we shall focus on CFF as
represented by TTX rather than looking at the actual binary data.
TTX is based on XML. What we usually consider to be an entry in a PostScript dictionary
becomes an XML element here. If the value of the entry is a number or a string, it is represented in TTX by a value attribute. If it is a subdictionary, we obtain an XML subelement.
Only charstrings are always represented as PostScript code.
Here is an example of a CFF table as seen through TTX:
&lt;CFF&gt;
&lt;CFFFont name="ComputerModern-Regular"&gt;
&lt;version value="002.000"/&gt;
&lt;Notice value="Copyright (c) Selwyn Hollis."/&gt;
25 With the possible exception of a few fonts woven on the spot into the PDF files produced by Acrobat
Distiller. We have learned that FontForge will henceforth produce CFF fonts without an OpenType wrapper.
26 That also explains why we did not mention Type 42 when we mentioned the “most successful font
formats” two paragraphs earlier: incorporating a TrueType font into a PostScript font that was in turn incorporated into an OpenType font would be befitting of the Marquis de Sade.
```

&lt;Copyright value="Computer Modern typefaces..."/&gt;
&lt;FullName value="ComputerModern Regular"/&gt;
&lt;FamilyName value="ComputerModern"/&gt;
&lt;Weight value="Regular"/&gt;
&lt;isFixedPitch value="0"/&gt;
&lt;ItalicAngle value="0"/&gt;
&lt;UnderlinePosition value="-"/&gt;
&lt;UnderlineThickness value="40"/&gt;
&lt;PaintType value="0"/&gt;
&lt;CharstringType value="2"/&gt;
&lt;FontMatrix value="0.001 0 0 0.001 0 0"/&gt;
&lt;UniqueID value="4113773"/&gt;
&lt;FontBBox value="- - 1195 940"/&gt;
&lt;StrokeWidth value="0"/&gt;
&lt;Encoding value="0"/&gt;
&lt;Private&gt;
&lt;BlueValues value="- 0 431 448 514 528 652 666 680 705"/&gt;
&lt;OtherBlues value="- -"/&gt;
&lt;BlueScale value="0.36364"/&gt;
&lt;BlueShift value="7"/&gt;
&lt;BlueFuzz value="1"/&gt;
&lt;StdHW value="31"/&gt;
&lt;StdVW value="25"/&gt;
&lt;StemSnapH value="22 25 31 40"/&gt;
&lt;StemSnapV value="25 66 69 83"/&gt;
&lt;ForceBold value="0"/&gt;
&lt;LanguageGroup value="0"/&gt;
&lt;ExpansionFactor value="0.06"/&gt;
&lt;initialRandomSeed value="0"/&gt;
&lt;defaultWidthX value="500"/&gt;
&lt;nominalWidthX value="673"/&gt;
&lt;Subrs&gt;
&lt;CharString index="0"&gt;
hvcurveto
- - - - - - - - rlinecurve
- callsubr
23 43 2 36 hhcurveto
31 26 callgsubr
...
&lt;/CharString&gt;
&lt;/Subrs&gt;
&lt;/Private&gt;
&lt;CharStrings&gt;
&lt;CharString name=".notdef"&gt;
endchar
&lt;/CharString&gt;

C.8. Type 2/CFF Fonts
&lt;CharString name="A"&gt;
- callgsubr
457 - hstem
- callsubr
endchar
&lt;/CharString&gt;
...
&lt;/CharStrings&gt;
&lt;/CFFFont&gt;
&lt;GlobalSubrs&gt;
&lt;CharString index="0"&gt;
rmoveto
- 4 27 - 47 hhcurveto
21 61 14 81 hvcurveto
56 - - vlineto
...
&lt;/CharString&gt;
...
&lt;/GlobalSubrs&gt;
&lt;/CFF&gt;
There can be several CFF fonts in a CFF table: they are represented by CFFFont elements. Their
subelements correspond to entries in the Type 1 (or CID, as the case may be) font dictionary.
There is one new element: CharStringType, which takes the value 2.
Each of the fonts may have its own local subroutines (the element Subrs), but there can
also be global subroutines (the element GlobalSubrs). The glyph descriptions are found in
the element CharStrings. Under a subroutine (be it local or global) or under CharStrings
(with an ‘s’), we find CharString elements (without the ‘s’). In the case of subroutines, these
elements contain an attribute index, which makes their order explicit. In the case of glyph
descriptions, they have an attribute name, whose value is the glyph’s name. But beware: appearances are deceiving. It is TTX that assigned the names to the glyph descriptions, using a
number of internal tables, in order to make it easier for us to read the XML document. The
correspondence is not so direct; in fact, in an OpenType font, the glyphs are obtained by their
indices in a table, not by their names.
In any event, the XML representation of a CFF table seems cleaner than the representation
in text format of a Type 1 font, and that is no accident. For instance, the attentive reader will
have noticed that this font does not have any “other subroutines”; thus we have managed to
avoid that nightmare dating back to the 1980s: PostScript code that was hard to understand,
that could not be modified, and that, finally, was part of the system of that “black box” known
as the rendering engine for Type 1 fonts. Also missing are the obscure but obligatory entries
such as MinFeature and password. Good riddance!
Let us now move on to the syntax of the charstrings of Type 2.

```text
C.8.2
The charstrings of Type 2
In the transition from charstrings of Type 1 to those of Type 2, Adobe killed three birds on
one stone:
1. Clean-up. All the constructions with uncertain syntax (hstem3, flex, hint replacements,
counter controls) now have their own elegant and concise operators. In addition, irritating operators such as callothersub were eliminated.
2. Compression. Much was done to reduce the size of the code.
3. Innovation. There are new features: oblique flex, more arithmetic operations, and even
a random-number generator.
The general schema of a charstring of Type 2 is as follows: First, we give the glyph’s set-width,
not followed by any operator. Next come, in order, the horizontal hints, the vertical hints,
the counter controls, and the hint replacements. Finally, one movement operator, followed
by a closed path. If there are other paths, they must be preceded by a movement operator.
Before moving on to the description of the operators, let us take note of one striking peculiarity of the new syntax: the operators are polymorphic, in the sense that they can read a variable
number of arguments and change their behavior accordingly. A simple example: the rlineto
operator usually takes two arguments: the coordinates of the ending point of the line that
is to be drawn. In fact, we can supply up to 24 pairs of arguments (a limit imposed by the
implementation; see [15, Appendix B]), and it will be executed as many times. Similarly, most
operators also accept a variable number of arguments; their behavior changes according to
rules that are sometimes quite elaborate.
Here is a brief description of the most important operators. The reader will find a detailed
description in [15, §4].
Let us begin with the simplest case: movement operators. There are three of them: one for
arbitrary movement (rmoveto, two arguments), one for horizontal movement (hmoveto, one
argument), and one for vertical movement (vmoveto, one argument). The arguments are always relative: they express movement relative to the current point.
We can draw straight lines or cubic Bézier curves starting from the current point. For the
former, we use three operators, just as for movement: rlineto (two arguments: the offset
of the ending point relative to the starting point), hlineto (one argument: the horizontal
offset), vlineto (one argument: the vertical offset); for the latter, we can use the operator
rrcurveto (six arguments). This operator has two ‘r’s in its name because it is doubly relative: specifically, the six arguments express the offset of the first control point relative to the
starting point, the offset of the second control point relative to the first, and the offset of the
ending point relative to the second control point. There are four “abbreviated” forms of this
operator, according to the tangents of the starting and ending points: hhcurveto (four arguments, horizontal tangents), hvcurveto (four arguments, horizontal and vertical tangents),
hvcurveto (four arguments, vertical and horizontal tangents), hhcurveto (four arguments,
vertical tangents). There are also two operators that combine Bézier curves and line segments:
rcurveline (eight arguments) draws first a curve and then a line; rlinecurve does the opposite.
```

```text
C.8. Type 2/CFF Fonts
There are several arithmetic operators: abs (absolute value), add (addition), sub (subtraction),
div (division), neg (change of sign), random (generation of a random rational number in the
interval (0,1]), mul (multiplication), sqrt (square root). Some logical operators and tests: and,
or, not, eq (tests whether two numbers are equal; returns 0 or 1), a b c d ifelse (returns
a if a ≤b, otherwise b). There are also some operators for stack management: drop (discards
an element from the stack), exch (swaps the top two elements on the stack), dup (duplicates
the top element on the stack), n index (replaces n with the nth element below it), n j roll
(makes j cyclic permutations of the n elements below).
There are also 32 areas in memory for temporarily storing numerical values (at the level of a
charstring). We store them with put and retrieve them with get. That has never been necessary in PostScript, since we can simply place the values on the stack and retrieve them when
we need them. But most of the operators for charstrings of Type 2 reset the stack after their
execution; thus another way for storing useful numerical values is needed.
Finally, endchar (with no arguments) ends the description of a glyph.
The remaining operators are for subroutines, flex, and hints. Subroutines are called with
callsubr (or callgsubr, if the subroutine is a global one), which takes one argument: the
number of the subroutine in question. The code inside a subroutine is constructed from any
Type 2 operators and must end with a return or an endchar if the charstring ends with the
subroutine in question.
The flex operator takes no fewer than 13 arguments: the coordinates (relative to the current point) of the starting point, the control points, and the ending points of the two curves,
and, at the end, the threshold, expressed in hundredths of a pixel, below which the curves
are so flat that they become a straight line. If we use the notation of Figure C-11 (§C-11),
the arguments are the relative coordinates of points b, c, d, e, f, and g; and if the threshold
is T, the distance dd′ must be smaller than T hundredths of a pixel for the curves to become
straight. Note once again that the restrictions imposed on Type 1 flex (horizontal or vertical
orientation, etc.) have been removed, and we can have flex at any angle. There are also the abbreviated versions flex1, hflex, and hflex1 for the cases in which the curves have horizontal
tangents.
C.8.2.1
Hints in charstrings of Type 2
We have come to hint management, whose syntax is much simpler than that of Type 1
charstrings. The methods used for hints are exactly the same (simple hints, ghost hints, hstem3,
hint replacement, counter control), but the way to represent them in code is much cleaner.
First, all the hints are declared at the beginning of the charstring, irrespective of whether some
of them overlap. They are declared from left to right (or from bottom to top), relative to their
left (or lower) edges. No other hint can be declared later. The operators hstem and vstem are
used to declare hints, unless there is at least one hint replacement in the glyph; in that case,
the operators hstemhm and vstemhm are used instead.
Hints always have a positive thickness, with the exception of ghost hints, which have a thickness of -20 (when the desired alignment is towards the right/top) or -21 (when the alignment
is towards the left/bottom).
Now suppose that we have declared our horizontal and vertical hints. If some hints overlap,
we must be able to enable and disable some of them while the glyph is being drawn (see
```

```text
H1
H2
V1
V2
2 3
(a)
(b)
(c)
Figure C-17: Hint management in charstrings of Type 2. From left to right: hint replacement, counter
control for three downstrokes, counter control for 11 horizontal and 7 vertical strokes.
Figure C-10). Here is how we proceed: we associate a bit with each hint; the bit will have the
value 1 if the hint is enabled, otherwise 0. These bits aligned in order (horizontal hints first)
form a number with as many bytes as necessary: we pad it with zeroes to obtain complete
bytes. This number is called the hint mask. The hintmask operator, followed27 by the hint mask,
will enable the hint indicated in the mask. This operator, and it alone, may appear anywhere
in the code for the charstring.
Let us examine the example in Figure C-17 (a): there are three horizontal hints and three
vertical hints. Of the latter, hints 2 and 3 touch. Thus we must enable hint 2 at one time
and hint 3 at another. There are therefore two masks: 11011100, which is the number 220,
and 10111100, which is 188. By writing hintmask 220 and hintmask 188, we switch from
one configuration of enabled hints to the other. Note that there is only one hintmask, which
manages horizontal and vertical hints at the same time.
The management of counter controls is similar: the strokes on the two sides of each counter
must have hints; we create a mask by enabling the hints corresponding to them. The operator cntrmask, followed by this mask, declares a set of counter controls. Unlike hintmask,
the cntrmask operators all appear at the beginning of the charstring, before the first drawing
instruction. In Figure C-17 (c), we see the ideograph 講(kô, “oration”), which has 11 horizontal hints and 7 vertical hints. We must therefore define the two horizontal zones H1 and H2
and the two vertical zones V1 and V2. Thus we shall use the operator cntrmask twice, combining the first and second horizontal and vertical zones. The horizontal hints of zone H1
are 1, 3, 5, 7, 9, 11; the others are in zone H2. Likewise, the vertical hints of zone V1 are
4 and 6, and those of zone V2 are 1, 2, 3, 5, 7. The two corresponding masks are therefore
101010101010001010000000 (11,182,720) and 010101010101110101000000 (5,594,432).
As with Type 1, counter control works only if LanguageGroup has the value 1; otherwise we can
still use cntrmask, but only with three strokes: we have the functionality of the old operators
hstem3 and vstem3, which is useful for the letters ‘m’ and ‘Ξ’. For example, in Figure C-17 (b)
we have the letter ‘m’, whose three downstrokes have the hints 1, 2, and 3. The mask of cn27 Warning! Arguments usually precede their operators; hintmask is an exception.
```

C.8. Type 2/CFF Fonts trmask will therefore be 11111 (31). This mask is unique, since there is only one zone, and therefore all the hints can be enabled at the same time.

D The TrueType, OpenType, and AAT Font Formats Microsoft is not the only company that wants to take over the world. To a smaller degree, Adobe also sought to control the world of printing during the years 1987 through 1989, i.e., when its PostScript language first met with success. That was a source of no little worry to the two giants of the day (Apple and Microsoft), who started looking for another system for rendering fonts on screen. The two companies joined forces to develop one such system and thus break free of Adobe. Apple was supposed to be in charge of the fonts, and Microsoft was responsible for the engine for rendering graphics. The product that Microsoft promised to Apple was called TrueImage. But TrueImage never saw the light of day. For its part, Apple had a number of projects in hand. One project, called Royal, by a Finnish engineer named Sampo Kaasila, was selected and delivered to Microsoft. Microsoft renamed it: “TrueType” was a better match for “TrueImage”. In March 1991, Apple released a preliminary version of TrueType as a plug-in for its Mac OS 6. Microsoft took one year longer to incorporate TrueType into Windows 3.1 in 1992 [258]. The beginnings of TrueType under Windows were difficult because Kaasila, working with Apple, naturally wrote the code for 32-bit machines, whereas Windows 3.1 was still at 16 bits. These problems were not really resolved until 1995, with the release of Windows 95. During the 1990s, Mac OS and Windows equipped their respective operating systems with TrueType fonts exclusively. At the same time, both Apple and Microsoft were working independently on extensions to TrueType. Apple had a great deal invested in TrueType GX (‘GX’ for “graphics extended”) [54, 55], a technology that added several new features to TrueType, notably for the typesetting of East Asian scripts. Apple adopted the approach of finite automata, where contextual analysis is done through states. The rendering engine is considered to be in a certain state, the current state,

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
at any moment. It can move from one state to another according to the glyphs that it is processing; conversely, it can process glyphs differently according to the current state.
It goes without saying that GX technology never really has won the hearts of the “specialists”
in graphic design and publishing—Quark and Adobe. After all, if the fonts are too intelligent,
there is less work for the desktop publishing software, thus there are fewer reasons to buy it.
Not to mention that both Quark and Adobe have for ages been issuing their software in Windows and Macintosh versions, with the same functionality, at least in theory. But GX exists
only for Mac OS—one more reason not to invest in this technology. To exorcise this commercial failure, the name “TrueType GX” was abandoned, and the technology was rechristened
AAT (for “Apple advanced typography”). AAT is an integral part of Mac OS X.
Microsoft has done work on TrueType Open [259]. This technology also addresses East Asian
scripts, but only through the use of the context. In other words, the shape of a glyph depends
on the glyphs that precede it and those that follow it. The more precise the context described
in the font, the smarter the transformation of the glyphs can be. TrueType Open was developed jointly with Adobe.1 To fill the gap between TrueType and PostScript, Adobe provided
for the inclusion of PostScript data in TrueType fonts, within a special table called CFF (see
Appendix C). Finally, “TrueType Open” (a name that reminds us a bit too much of the tennis
championship known as the “U.S. Open”) was renamed “OpenType”.
In this chapter, we shall describe, in order, the basic TrueType format, the OpenType extensions, and the AAT extensions. This description will be facilitated by the fact that the data in a
TrueType font are stored in tables. Since each table has a very specific role, the data contained
therein are clearly classified (unlike those of PostScript fonts, where everything is jumbled
together). In TrueType there are required tables and optional tables; and OpenType and AAT
have additional tables of their own. In addition, the TrueType file format is a tolerant one:
the rendering engine, be it for TrueType, OpenType, or AAT, collects the data that it requires
from only the tables that it recognizes; the presence of other tables, ones that it may not
recognize at all, does not bother it in the least. Even better, every font developer can define
new tables and include them in fonts. If the fonts in question are meant to be distributed, the
new table names can be registered with Apple (for AAT) or with the OpenType Consortium
(for OpenType). The discussion forum opentype@topica.com, which is followed by officials
at Adobe and Microsoft, is the ideal place to discuss proposals for new tables.
Before we continue with the description of TrueType tables, one little word on the wonderful
tool TTX, which allows us to manipulate these fonts in a user-friendly manner far removed
from the binary editors, pointers, checksums, and all the other things that are the daily bread
of low-level programmers but that need not concern font designers.
D.1
TTX: TrueType Fonts Represented in XML
Unlike PostScript fonts, TrueType is a completely binary font format. The system of tables is
technically efficient precisely because the TrueType file teems with pointers to the tables and,
beyond that, to entries within the tables. By following pointers, software that recognizes the
1 Such is the ballet of alliances and rivalries: at the end of the 1980s, it was Microsoft and Apple against
Adobe; a decade later, it is Microsoft and Adobe against Apple. In 2010, we may perhaps see an alliance of
Apple and Adobe against Microsoft, if the first two have not been bought out by the third in the meantime.
```

```text
D.1. TTX: TrueType Fonts Represented in XML
structure of the tables will thus very quickly find the data that it needs. It is a clean, rapid, and
efficient approach. At the same time, however, it is rather badly designed for humans. Unlike
PostScript fonts, in which one can read and even modify the code through a conversion with
t1disasm and t1binary, these fonts cannot be handled by a human who does not have a binary
editor and a great deal of patience.
To bridge this gap, font designer Just van Rossum, brother of the famous creator of the Python
language, Guido van Rossum, developed a free tool in 2001, called TTX (‘TT’ for “TrueType”
and ‘X’ for “XML”), which converts TrueType into a human-readable format, the file format
also being called TTX. The most attractive feature of this tool is that it also performs the
opposite operation just as easily: from a TTX file, it can generate another TrueType font that
is identical to the original. Thus we can say that TTF and TTX are equivalent, in the sense that
they contain the same data.
Following the general principle on which this book was organized, we shall describe TTX
in this appendix rather than TTF: thus we shall be able to focus on the essential, leaving
aside all the boring issues of pointers, offsets, short and long numbers, signed and unsigned
numbers, etc.
Even better, the TTX format is based on the XML markup system. Thus a TrueType font becomes an XML document, a TrueType table becomes an XML element, the entries in the table
become subelements or attributes, etc. This approach makes the hierarchy of the data in a
TrueType font even clearer. Do not worry if you are not familiar with XML: here we shall use
only the rudiments of the system. In fact, we shall use it merely as a syntax for representing
data.2 On page 345 in Chapter 10, we give a brief introduction to this syntax in the scope of
an introduction to the SVG fonts, which are also described in XML.
Now let us talk about the program TTX [307].
There are binary versions for Mac OS 9 and Windows; for other systems, it is a simple matter
to obtain the source code and compile it oneself.3
To convert foo.ttf into foo.ttx, we write:
ttx foo.ttf
Likewise, for the opposite conversion, from TTX to TTF:
ttx foo.ttx
Note that the TTX file is often more than 10 times larger than the original TTF. The
command-line option -l gives us a list of the tables in the font; for instance, TTX generates
the following list for the OpenType font Palatino Linotype:
2 In particular, there will be no DTD, no schemas, no validation, no XSL transformation, no advanced
XML techniques.
3 To do so, one must also obtain the numpy library for numerical calculations [63], and then the source
code in Python. To install Python libraries, one goes into the top-level directory of the uncompressed source
code and runs python setup.py install while logged in as root.
```

Appendix D : The TrueType, OpenType, and AAT Font Formats
ttx -l pala.ttf
Listing table info for "pala.ttf":
tag
checksum
length
offset
----
----------
-------
-------
BASE
0x7b5692db
DSIG
0x6edef86c
GDEF
0x4106d6ad
GPOS
0x8193c0a3
GSUB
0x9e8956bf
JSTF
0x58023ab0
LTSH
0x0d0716a6
OS/2
0x7db7af65
PCLT
0x5f35eba2
VDMX
0xfaaee43a
cmap
0x5bd843ef
cvt
0x03bf08d3
fpgm
0x1c783cd8
gasp
0x00180009
glyf
0x2a83b1cb
hdmx
0x463cb359
head
0xd1e333a7
hhea
0x12870cbc
hmtx
0x54010411
kern
0x4d914fd6
loca
0x123a1952
maxp
0x0ee612f2
name
0xe1785cd3
post
0xbffb3888
prep
0x053578ed
The tables are presented in alphabetical order (first uppercase letters, then lowercase), and
the checksum, length, and pointer to the start of the table is also given in each entry.
Other interesting options:
• The option -s allows us to store each table in a separate file. There will be as many files
pala.B_A_S_E_.ttx,4 pala.D_S_I_G_.ttx, pala.G_D_E_F_.ttx, . . . , as there are TrueType tables and also a coordination file pala.ttx containing a list of the generated files.
The opposite procedure is, of course, also possible. One must merely ensure that all the
files are in the same directory.
4 The reader must be wondering why TTX inserts underscores into the tables’ names. The answer is very
simple. The case of the ASCII characters that make up a table name is significant: BASE, base, baSe, etc., must
not be mixed up. But not all operating systems are sufficiently advanced to distinguish uppercase and lowercase
letters. Therefore, TTX’s approach involves saying “we shall place an underscore before a lowercase letter and
after a capital. Thus the three examples that we just gave would become B_A_S_E_, _b_a_s_e, _b_aS__e; the
names are unambiguous, even under primitive operating systems such as MS-DOS, without naming names.

D.2. TrueType Collections
• If we write -t followed by a table name, only that table will be extracted. To obtain multiple tables, we use this option multiple times. Warning: do not forget any space characters
that occur in the table name. Example: ttx -t "cvt " pala.ttf.
• -x followed by a table name: do not extract the table in question. To specify multiple
tables, use this option several times. The same precautions apply.
D.2
TrueType Collections
A TrueType collection (TTC) [258] is a file with the extension .ttc that contains a set of TrueType fonts that share some tables. The header of a file of this sort is also a TrueType table,
named ttcf. What is interesting about a TTC relative to the individual TTFs that it contains
is the fact that the TTFs can share a large part of their resources. For example, recall that
the Japanese language has four scripts: the kanji (漢字) ideographs, of Chinese origin; the
hiragana (ひらがな) and katakana (カタカナ) syllabaries; and the “modified” Latin script
romaji. Thus we can easily imagine Japanese fonts that share the kanji but contain
different kana or different Latin letters.5 Given that the kanji make up perhaps 95 to 99 percent of the total volume of the glyph descriptions, it would be strictly redundant to have the
same kanji in multiple Japanese fonts. In a TTC, we can set things up so that the same table of
glyphs (for all the glyphs, including the different versions of kana) is used in different ways,
which is equivalent to providing several TrueType fonts.
TTX processes TTCs by converting the fonts that they contain into separate TTX files, then
combining all of these files into a TTC once again. Optimizations of the structure are performed automatically: every time TTX comes across two tables with the same checksum, it
considers them to be data shared by different fonts in the collection. Thus it is necessary to
make sure that the tables are strictly identical (with cut-and-paste operations, if necessary).
For instance, by running:
ttx msmincho.ttc
we obtain msmincho1.ttx, msmincho2.ttx, and msmincho3.ttx. Conversely, when we run:
ttx -collect msmincho1.ttx msmincho2.ttx msmincho3.ttx -o msmincho.ttc
the three fonts are assembled into a TTC collection.
D.3
General Overview of TrueType Tables
The tables of a TrueType, OpenType, or AAT font are identified by a tag, which must be a
string of four ASCII characters (possibly including spaces, but only at the end of the string).
Tags that are entirely in lowercase are the private hunting ground of Apple. It was doubtless
5 We have already seen this sort of situation during the rearrangement of a CID font (§C.7.3). It shows
that each font system tries to solve this problem, inherent in the Japanese language, as well as it can. The same
problem arises every time scripts are mixed: in Korean, for example, we can combine hangul (한글) and hanja
(漢字), etc.

Appendix D : The TrueType, OpenType, and AAT Font Formats
in response to that that the OpenType-specific tables, as we shall see, use tags consisting of
uppercase letters only.
There are some tables that are required in every TrueType font, therefore also in OpenType
and AAT fonts:
• cmap (mapping between characters and glyphs, §D.4.2).
• head (header, §D.4.3).
• hhea (header for the horizontal metrics, §D.4.4).
• hmtx (horizontal metrics, §D.4.4).
• maxp (maximum profile, §D.4.5).
• name (table of names, §D.4.6).
• OS/2 (information related to OS/2 and Windows, §D.4.7). Microsoft considers it mandatory, but Apple does not.
• post (information that is useful when the font is used in a PostScript environment,
§D.4.8).
Next, everything depends on whether the glyph descriptions are written in TrueType or in
PostScript. In the first case, there are five other tables that must not be missing:
• cvt (table of control values, §D.5.3)
• fpgm (font program, §D.5.3)
• glyf (glyph descriptions, §D.5.2)
• loca (pointers to the glyph descriptions, §D.5.1)
• prep (program of control values, §D.5.3)
In the second case, which is the one seen in Appendix C, §C.8, where the OpenType font
contains a PostScript CFF font with Type 2 charstrings, there are two required tables:
• CFF [OpenType] (PostScript CFF font, §D.6.1)
• VORG [OpenType] (coordinates of the origins of the glyphs for vertical typesetting, §D.6.2)
Note that in the earliest versions of OpenType there were two other tables: MMSD (Multiple
Master supplementary data) and MMFX (Multiple Master font metrics), which contained information on PostScript Multiple Master fonts. These were abandoned in version 1.3, and
we shall not describe them.
Some tables manage bitmap fonts:
• EBDT (bitmap data, §D.7.1), an extension of bdat [AAT]

D.3. General Overview of TrueType Tables
• EBLC (pointers to bitmap data, §D.7.1), an extension of bloc [AAT]
• EBSC (data on the scaling of bitmaps, §D.7.2)
• bhed [AAT] (the head table, which was renamed only to show that the font is a bitmap
font, §D.7.3)
A few other optional tables:
• DSIG [OpenType] (digital signature, §D.8.1)
• gasp (fitting to the grid, §D.8.2)
• hdmx (horizontal metrics relative to the rendering device, §D.8.3)
• kern (kerning, §D.8.4)
• LTSH (linear threshold, §D.8.3)
• PCLT (data for the PCL 5 printer, §D.8.7)
• VDMX (vertical metrics relative to the rendering device, §D.8.5)
• vhea (header for vertical metrics, §D.8.6)
• vmtx (vertical metrics, §D.8.6)
Finally, let us discuss the TrueType extensions as such. These are “advanced” OpenType and
AAT tables:
• BASE [OpenType] (table of the different baselines, §D.9.2)
• GDEF [OpenType] (various definitions, §D.9.6)
• GPOS [OpenType] (glyph positionings, §D.9.3)
• GSUB [OpenType] (glyph substitutions, §D.9.4)
• JSTF [OpenType] (justification, §D.9.5)
• acnt [AAT] (attachment of accents, §D.11.1)
• avar [AAT] (variation of the axes, §D.12.2)
• bsln [AAT] (different baselines, §D.11.2)
• cvar [AAT] (variation of the control values, §D.12.4)
• fdsc [AAT] (font descriptors, §D.11.3)
• feat [AAT] (features of the font, §D.11.5)
• fmtx [AAT] (font metrics, §D.11.4)

Appendix D : The TrueType, OpenType, and AAT Font Formats
• fvar [AAT] (font variation, §D.12.1)
• gvar [AAT] (glyph variation, §D.12.3)
• just [AAT] (justification, §D.13.3)
• lcar [AAT] (ligature caret, §D.11.6)
• morx [AAT] (table of metamorphosis, §D.13.2, formerly mort)
• opbd [AAT] (optical boundaries, §D.11.7)
• prop [AAT] (properties, §D.11.8)
• trak [AAT] (leading, §D.11.9)
• Zapf [AAT] (various data on the glyphs, §D.11.10)
There are also private tables, which are not part of the specifications for OpenType or those
for AAT, such as the following:
• The table VTT, incorporated into a TrueType font with Microsoft’s tool VTT (Visual TrueType) [262]
• The tables TSID, TSIP, TSIS, and TSIV, incorporated into a TrueType font with Microsoft’s
tool VOLT [266]
• The tables Silf, Gloc and Glat, by Graphite: another extension of TrueType, developed
by the Summer Institute of Linguistics [184]
• And doubtless other applications unknown to the author
Below we shall describe the tables in the following order:
• First, the required tables that are shared by everybody: the “kernel” of the TrueType fonts
(§D.4).
• Next, the basic tables that are specific to TrueType-style glyph descriptions (§D.5).
• The OpenType tables, specific to PostScript glyph descriptions (§D.6).
• The tables specific to bitmap fonts (§D.7).
• The various and sundry optional tables (§D.8).
• Finally, the most interesting part: the tables for “advanced typography”. First, those defined by Microsoft and Adobe in OpenType (§D.9).
• Next, those defined by Apple in AAT, starting with the general tables (§D.11).
• The AAT tables for font variation (§D.11).

D.4. The Kernel of the TrueType Tables
• Finally, the AAT tables with finite automata (§D.11).
Note that in both systems (OpenType and AAT) there is the notion of feature, and in both
cases the respective instances present quite long lists of predefined features. We shall describe
these predefined features in §D.10.2 for OpenType and in §D.11.5.1 for AAT.
Recall that in this appendix we shall describe the TrueType tables as represented in XML by
TTX: thus we shall speak of XML elements, names, and values of attributes, etc. If the reader
does not feel at ease with the jargon of the XML syntax, now would be the ideal time to reread
the introduction to XML on pages 345 through 349 of this book.
It is time to begin, at the beginning—with the tables that are indispensable for every TrueType font.
D.4
The Kernel of the TrueType Tables
These are the tables defined and used since the first version of TrueType.
Before describing them, let us say a few words about the global structure of TTX documents.
The global element of these XML documents is ttFont:
&lt;ttFont sfntVersion="\x00\x01\x00\x00" ttLibVersion="2.0b2"&gt;
This element contains two attributes:
• sfntVersion, the version of the TrueType format. Fortunately, we are still at version 1
of TrueType, despite the extensions made by OpenType and AAT. Yet the value of this
attribute has a peculiar appearance in the example below. In fact, it is the rational number 1.0 written with 32 bits, of which the first 16 bits contain the integer part and the
other 16 contain the fractional part: 0x00010000. Here this number is written as a sequence of four bytes, \x00\x01\x00\x00.
• ttLibVersion, the version of TTX—a very useful value, as TTX is an evolving system and
no one can guarantee that the format of a TTX document will not change in the future.
Now we shall describe the different elements that are found in a TTX document and that
correspond to the tables of the kernel of TrueType.
D.4.1
The GlyphOrder Table
There is no GlyphOrder table; indeed, how could there have been one? The name, containing
more than four letters, is not in any way compliant with the TrueType specifications! Yet, in
a TTX document, it is the first element after ttFont:
&lt;GlyphOrder&gt;
&lt;GlyphID id="0" name="missing"/&gt;
&lt;GlyphID id="1" name=".null"/&gt;
&lt;GlyphID id="2" name="nonmarkingreturn"/&gt;

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
&lt;GlyphID id="3" name="A"/&gt;
&lt;GlyphID id="4" name="B"/&gt;
&lt;GlyphID id="5" name="C"/&gt;
&lt;GlyphID id="6" name="D"/&gt;
&lt;GlyphID id="7" name="E"/&gt;
...
&lt;GlyphID id="1326" name="uni1EF9"/&gt;
&lt;GlyphID id="1327" name="uni20A0"/&gt;
&lt;/GlyphOrder&gt;
What is this table? It is, in fact, a great service that TTX has done for us. In a binary TrueType
font, when we refer to glyphs, we always do so through their numbers. For example, in a kerning pair for ‘A’ and ‘C’, we refer to the glyphs by their respective numbers: 3 and 5. If the same
thing were done in a TTX document, we would be obliged to search constantly through the
tables in order to find out which glyphs are 3 and 5. TTX thus generously takes the initiative
of assigning unique names to the glyphs and referring to them by these names. This operation
is not without risks: how can TTX know which name to assign to each glyph? Obviously there
are some indications, but TTX may nonetheless make a mistake. Never mind: even if TTX goes
astray, the worst that can happen is that the human reader will err in the interpretation of a
glyph. That will not affect the internal structure of the font in any way, since the names vanish
upon conversion to TTF and become anonymous numbers once again. In other words, the
binary TTF font will be the same regardless of the names that TTX gives to the glyphs.
Thus this table is indispensable to the “humanization” of the TrueType font.
D.4.2
The cmap Table
Do not confuse this table with the CMap files of the CID fonts (which are written with the
capital letters “CM”). This table contains mappings of the glyphs in the font to the characters
in various encodings. Here is an example:
&lt;cmap&gt;
&lt;tableVersion version="0"/&gt;
&lt;cmap_format_4 platformID="0" platEncID="3" version="0"&gt;
&lt;map code="0x20" name="space"/&gt;<!-- SPACE -->
&lt;map code="0x21" name="exclam"/&gt;<!-- EXCLAMATION MARK -->
&lt;map code="0x22" name="quotedbl"/&gt;<!-- QUOTATION MARK -->
&lt;map code="0x23" name="numbersign"/&gt;<!-- NUMBER SIGN -->
...
&lt;map code="0xfb05" name="uniFB05"/&gt;<!-- LATIN
SMALL LIGATURE LONG S T -->
&lt;map code="0xfb06" name="uniFB06"/&gt;<!-- LATIN SMALL LIGATURE ST -->
&lt;map code="0xfffc" name="uniFFFC"/&gt;<!-- OBJECT
REPLACEMENT CHARACTER -->
&lt;/cmap_format_4&gt;
&lt;cmap_format_6 platformID="1" platEncID="0" version="0"&gt;
&lt;map code="0x0" name=".null"/&gt;
```

```text
D.4. The Kernel of the TrueType Tables
&lt;map code="0x1" name="missing"/&gt;
&lt;map code="0x2" name="missing"/&gt;
...
&lt;map code="0xfe" name="ogonek"/&gt;
&lt;map code="0xff" name="caron"/&gt;
&lt;/cmap_format_6&gt;
...
&lt;/cmap&gt;
The map elements match the code point code of a given encoding to the glyph indicated by the
attribute name. When there is no glyph associated with a code point in the encoding, either the
corresponding map element is omitted or the glyph name missing is used. The cmap contains
many subtables, which are represented by cmap_format_* subelements and correspond to the
different encodings of the font.
The format of the subtable will vary according to the type of the encoding: small encodings
will have subtables in which all the code points are represented, while 16-bit encodings will
have subtables with only those code points for which a glyph exists. Even 32-bit encodings
are supported (for example, Unicode with surrogates, or the higher planes of Unicode 3.2
and later versions).
There are seven formats for subtables, corresponding to seven different elements in TTX:
Format
TTX
Peculiarities
cmap_format_0
Anonymous
8-bit
font
encoding:
all
the
positions
from 0x00 to 0xff must be represented by &lt;map&gt; elements.
cmap_format_2
Mixed 8-bit/16-bit font encoding. This is used for some
ideographic encodings, in which some bytes represent characters while other bytes must be followed by a second byte,
the two jointly forming one 16-bit character. This subtable
must not contain any holes: all the valid characters must be
represented.
cmap_format_4
A 16-bit font encoding that may contain holes.
cmap_format_6
A lighter version of the preceding: a character encoding in
any contiguous zone in the 16-bit table.
cmap_format_8
The equivalent of 2, but in 16-bit/32-bit. This subtable is
ideal for Unicode surrogates.
cmap_format_10
The equivalent of 6, but in 32-bit: any contiguous zone in
the 32-bit table.
cmap_format_12
The most powerful of all: the equivalent of 4, but in 32-bit.
Ideal for Unicode with the higher planes.
The reader must have thought of one fundamental question: if each subtable corresponds to
a font encoding, where does its name appear? Nowhere, unfortunately. To find it, we have
only the values of the attributes platformID and platEncID. There are three possibilities for
the former: 0 = Unicode, 1 = Macintosh, 3 = Windows. Here are the possibles values for the
latter, according to the value of the former:
```

Appendix D : The TrueType, OpenType, and AAT Font Formats
• If platformID is 0 (Unicode), then platEncID can take the following values: 0 (default),
1 (version 1.1), 3 (version 2 or later). We therefore recommend 0 or 3.
• If platformID is 1 (Macintosh), then platEncID can take the following values: 0 (Roman,
i.e, the Latin alphabet for the countries of Western Europe), 1 (Japanese), 2 (traditional
Chinese), 3 (Korean), 4 (Arabic), 5 (Hebrew), 6 (“monotonic” Greek), 7 (Russian), 8 (all
sorts of symbols), 9 (Devanagari), 10 (Gurmukhi), 11 (Gujarati), 12 (Oriya), 13 (Bengali),
14 (Tamil), 15 (Telugu), 16 (Kannada), 17 (Malayalam), 18 (Sinhala), 19 (Burmese), 20
(Khmer), 21 (Thai), 22 (Lao), 23 (Georgian), 24 (Armenian), 25 (simplified Chinese), 26
(Tibetan), 27 (Mongolian), 28 (Geez), 29 (Old Cyrillic), 30 (Vietnamese), 31 (Sindhi), 32
(not interpreted). Each case refers to the corresponding Macintosh encoding.
• If platformID is 3 (Windows), then platEncID can take the following values: 0 (symbols),
1 (Unicode), 2 (Shift-JIS, Japan), 3 (GB, People’s Republic of China), 4 (Big5, Taiwan),
5 (Wansung, precomposed encoding, Korea), 6 (Johab, non-precomposed encoding, Korea), 10 (UCS-4, i.e., 32-bit Unicode).
For example, the font Palatino Linotype contains the following 6 cmap subtables: 4/0/0, (i.e.,
format 4, platform 0, encoding 0 = Unicode version 2 and later), 6/1/0 (Macintosh, Latin alphabet, Western Europe), 6/1/6 (Macintosh, “monotonic” Greek), 6/1/7 (Macintosh, Russian),
6/1/29 (Macintosh, Old Cyrillic), 4/3/1 (Windows, Unicode). Note that the tables 4/0/0 and
4/3/1 are identical in every respect.
Finally, Apple requests that the subtables that correspond to a given language also have a
language attribute, whose value is drawn from Apple’s table of language identifiers [56, Chapter 6].
The cmap table is indispensable for communication between the font and the operating system, which knows about nothing but characters. But the problem is that some glyphs do
not belong to any character and others belong to the same character. As we shall see, a large
number of resources are put into service so that we can make use of these glyphs, either by
going beyond the cmap table or by supplementing it.
D.4.3
The head Table
The font’s global header, with 17 entries. Here is an example:
&lt;head&gt;
<!-- Most of this table will be recalculated by the compiler -->
&lt;tableVersion value="1.0"/&gt;
&lt;fontRevision value="1.0"/&gt;
&lt;checkSumAdjustment value="0x10AE3726"/&gt;
&lt;magicNumber value="0x5F0F3CF5"/&gt;
&lt;flags value="00001000 00011011"/&gt;
&lt;unitsPerEm value="2048"/&gt;
&lt;created value="Mon Jan 29 10:11:20 1996"/&gt;
&lt;modified value="Tue Jun
8 10:02:55 1999"/>
&lt;xMin value="-"/&gt;
&lt;yMin value="-"/&gt;

D.4. The Kernel of the TrueType Tables
&lt;xMax value="2907"/&gt;
&lt;yMax value="2150"/&gt;
&lt;macStyle value="00000000 00000000"/&gt;
&lt;lowestRecPPEM value="9"/&gt;
&lt;fontDirectionHint value="2"/&gt;
&lt;indexToLocFormat value="1"/&gt;
&lt;glyphDataFormat value="0"/&gt;
&lt;/head&gt;
A few interesting subelements:
• flags contains 16 flags that cover all sorts of things: for example, bit 0 means that the
baseline is at y = 0, bit 8 means that the font is subject to a morx metamorphosis table (and
therefore is an AAT font), bit 13 means that the font has been optimized for ClearType
on-screen display technology, etc.
• unitsPerEm defines the grid for the glyphs: it is the number of abstract units per em.
Maximum possible value: 16,384. The most common value is 2,048 for TrueType fonts
and 1,000 for PostScript.
• xMin, yMin, xMax, yMax: the bounding box for all the glyphs that do contain outlines (in
other words, empty glyphs do not have a bounding box, which may seem obvious, but
we may as well state it).
• macStyle, six flags that indicate the font’s “Quickdraw style” (bit 0, bold; bit 1, italic; bit 2:
underlined; bit 3, outline; bit 4, shadowed; bit 5, condensed; bit 6, extended).
• lowestRecPPEM: the size (expressed in pixels!) below which the font is no longer legible.
• fontDirectionHint: a global hint about the direction in which the glyphs are typeset.
Possible values: 0 (left-to-right and right-to-left), 1 (left-to-right only), 2 (left-to-right and
neutral, such as the space and the period), -1 and -2 (the opposites of 1 and 2: right-toleft only, and right-to-left and neutral).
D.4.4
The Tables hhea and hmtx
The table hhea contains global data for horizontal typesetting. Like head, it also contains
17 subelements. Here is an example:
&lt;hhea&gt;
&lt;tableVersion value="1.0"/&gt;
&lt;ascent value="1499"/&gt;
&lt;descent value="-"/&gt;
&lt;lineGap value="682"/&gt;
&lt;advanceWidthMax value="2861"/&gt;
&lt;minLeftSideBearing value="-"/&gt;
&lt;minRightSideBearing value="-"/&gt;
&lt;xMaxExtent value="2907"/&gt;

Appendix D : The TrueType, OpenType, and AAT Font Formats
&lt;caretSlopeRise value="1"/&gt;
&lt;caretSlopeRun value="0"/&gt;
&lt;caretOffset value="0"/&gt;
&lt;reserved0 value="0"/&gt;
&lt;reserved1 value="0"/&gt;
&lt;reserved2 value="0"/&gt;
&lt;reserved3 value="0"/&gt;
&lt;metricDataFormat value="0"/&gt;
&lt;numberOfHMetrics value="1328"/&gt;
&lt;/hhea&gt;
A few interesting subelements:
• ascent and descent: the height of the ascenders and the depth of the descenders.
• lineGap: the leading recommended for this font, minus the height of the ascenders and
the depth of the descenders.
• advanceWidthMax, the maximum width vector.
• minLeftSideBearing and minRightSideBearing: the minimum values of the left and
right side-bearings. Warning: when we say “minimum”, we do not mean an absolute
value! Glyphs that extend beyond their abstract boxes have negative side-bearings. Here,
then, we are looking for the greatest amount of overhang.
• xMaxExtent is the maximum horizontal extent of the glyph.
• The entries caretSlopeRise, caretSlopeRun, and caretOffset pertain to the mouse’s
cursor: they are the coordinates of the vector for the direction towards which it is pointing. As an example, the cursor will be vertical for the values 1 and 0; for 0 and 1, it will
be horizontal; but it may very well be slanted (for an italic font, for instance). The third
parameter indicates a possible horizontal offset of the cursor. This value will be primarily
for highlighting: we wish to ensure that the entire body of each glyph will be contained
in the highlighted area, even if the font is heavily sloped.
• numberOfHMetrics refers to the following table: hmtx. It is the number of entries in that
table.
The table hmtx is one of the simplest that exist: for each glyph, it contains the values of the
width vector and the left side-bearing. Here is how it is represented in TTX:
&lt;hmtx&gt;
&lt;mtx name=".null" width="0" lsb="0"/&gt;
&lt;mtx name="A" width="1593" lsb="35"/&gt;
&lt;mtx name="AE" width="1933" lsb="0"/&gt;
&lt;mtx name="AEacute" width="1933" lsb="0"/&gt;
&lt;mtx name="AEacutesmall" width="1503" lsb="10"/&gt;
...

D.4. The Kernel of the TrueType Tables
&lt;mtx name="zeta" width="1022" lsb="82"/&gt;
&lt;mtx name="zsuperior" width="597" lsb="6"/&gt;
&lt;/hmtx&gt;
Note that there are counterparts of tables hhea and hmtx that are used for vertical typesetting:
they are the optional tables vhea and vmtx (see §D.8.6).
D.4.5
The maxp Table
The name maxp comes from “maximum profile”. This table contains data that are useful to
the processor during allocation of the memory required to process a font. This table contains
15 entries. Here is an example:
&lt;maxp&gt;
<!-- Most of this table will be recalculated by the compiler -->
&lt;tableVersion value="0x10000"/&gt;
&lt;numGlyphs value="1328"/&gt;
&lt;maxPoints value="180"/&gt;
&lt;maxContours value="16"/&gt;
&lt;maxCompositePoints value="166"/&gt;
&lt;maxCompositeContours value="9"/&gt;
&lt;maxZones value="1"/&gt;
&lt;maxTwilightPoints value="0"/&gt;
&lt;maxStorage value="27"/&gt;
&lt;maxFunctionDefs value="75"/&gt;
&lt;maxInstructionDefs value="0"/&gt;
&lt;maxStackElements value="2382"/&gt;
&lt;maxSizeOfInstructions value="4475"/&gt;
&lt;maxComponentElements value="3"/&gt;
&lt;maxComponentDepth value="1"/&gt;
&lt;/maxp&gt;
A few interesting subelements:
• tableVersion takes the value 0x10000 if the font contains TrueType glyph descriptions.
If it is a CFF font, the value of this entry must be 0x5000.
• numGlyphs, the number of glyphs. This is the only entry in the table (along with
tableVersion) for the CFF fonts.
• maxPoints and maxContours: the maximum numbers of points and contours for simple
glyphs.
• maxCompositePoints and maxCompositeContours: the maximum numbers of points and
contours for composite glyphs.
• maxComponentElements: the maximum number of components in composite glyphs.

Appendix D : The TrueType, OpenType, and AAT Font Formats
• maxComponentDepth: can the components themselves be composite glyphs, and to what
depth? 1 means that the components are simple glyphs.
• The other entries concern TrueType instructions, i.e., the assembly language that is used
for optimizing the rendering of the glyphs. We shall examine it in detail in Appendix E.
D.4.6
The name Table
This table is a gem of political correctness on the part of Apple and Microsoft: we can provide
a certain amount of information in 150 different languages (including, among others, Breton,
Esperanto, and even Latin6). Here is an extract of this table:
&lt;name&gt;
&lt;namerecord nameID="0" platformID="0" platEncID="3" langID="0x0"&gt;
Copyright 1981-, 1989,1993, 1998 Heidelberger...
&lt;/namerecord&gt;
&lt;namerecord nameID="1" platformID="0" platEncID="3" langID="0x0"&gt;
Palatino Linotype
&lt;/namerecord&gt;
&lt;namerecord nameID="2" platformID="0" platEncID="3" langID="0x0"&gt;
Regular
&lt;/namerecord&gt;
...
&lt;/name&gt;
This table contains only namerecord elements. Each of these elements is associated with a platform, an encoding, and a language. We find the same approach as for the cmap table, which
uses the same attributes platformID and platEncID, with the same values (see §D.4.2). What
is new here is the language (attribute langID). The language identifiers depend on the platform. For example, for the “Unicode” platform (platformID equal to 0), there are none. For
the “Macintosh” platform (platformID equal to 1), there are some 150 identifiers, described
in [264]. For the “Windows” platform (platformID equal to 3), there are some 135 identifiers:
0x0409 is American English, 0x040c is French, etc.
We have seen how to indicate the language of a record. Now let us give a list of the records
provided in the specification:
• 0: the copyright notice.
• 1: the name of the font family.
• 2: the “style”, which is what must be added to the name of the font family (1) to obtain
the name of the font (4).
6 The reader may be wondering of what use a description of the font in Latin can be. Well, today there are
still admirers of this language, which was still heard in Catholic churches 50 years ago. Note that in Finland,
that European Union member country renowned for the humor of its residents, there is a state-run radio station [288] that has been broadcasting the news in Latin every week for more than 15 years! A Finnish jazz group
even released a CD entitled Variationes Horatianae Iazzicae, with songs in Latin, to celebrate the bimillennial
anniversary of the death of Horace.

D.4. The Kernel of the TrueType Tables
• 3: the unique identifier (UID) of the font.
• 4: the complete name of the font.
• 5: the version of the font, in a very strict format, which follows: the string Version followed by a primary version number, a period, and a secondary version number (the
numbers must be between 0 and 65535).
• 6: the PostScript name of the font. This information must appear twice, with the following value of the attributes: platform 1, encoding 0, language 0; and platform 3, encoding 1, language 0x0409.
• 7: the trademark.
• 8: the name of the foundry.
• 9: the name of the designer.
• 10: a description of the font (at most 65,536 characters).
• 11: the URL of the foundry.
• 12: the URL of the designer.
• 13: a description of the license. The OpenType specification includes the following exhortation: “This field should be written in plain language, not legalese”. We may well wonder
whether that exhortation is itself legal.
• 14: the URL for the license.
• 16: a “family name” that can be used by Windows in menus that list fonts.
• 17: a “style name” that can be used by Windows in menus that list fonts.
• 18: a “family name” that can be used by the Macintosh in menus that list fonts.
• 19: a sample of text; for example, a pangram.7
• 20: a CID font name, with the CMap component. The notes in 6, above, also apply to the
values of the parameters for this record.
7 A pangram, from the Greek πν (“all”) and γρμμα (“letter”), is a sentence containing all the letters in
a given alphabet. For example, in English, “The quick brown fox jumps over the lazy dog”; in French, Portez
ce vieux whisky au juge blond qui fume (“Take this old whisky to the blond judge who is smoking”); in German,
Franz jagt im komplett verwahrlosten Taxi quer durch Bayern (“Franz chases straight across Bavaria in a completely
run-down taxi”); in Russian, в чащах юга жил-был цитрус... да, но фальшивый экземпляръ! (“Once upon
a time there was a citrus in the bushes of the south—yes, but a fake one!”) [358]; in Greek, γαζε
κα μυρτι

δν θ βρ πι στ χρυσαφ ξφωτο (“No more shall I see acacias or myrtles in the golden clearing”) [137], etc.

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
D.4.7
The OS/2 Table
The name of this table is deceptive: one is likely to think that it applies only to the littledistributed and rather peculiar operating system known as IBM OS/2. That is not so, for this
table applies above all to another operating system, much more widely used, by the name of
Windows. While hhea is a table intended primarily for the Macintosh, OS/2 assembles some
data from that table for the Windows environment.
It has a record number of entries: 37! Here is an example of the table:8
&lt;OS_2&gt;
&lt;version value="2"/&gt;
&lt;xAvgCharWidth value="912"/&gt;
&lt;usWeightClass value="400"/&gt;
&lt;usWidthClass value="5"/&gt;
&lt;fsType value="00000000 00001000"/&gt;
&lt;ySubscriptXSize value="1285"/&gt;
&lt;ySubscriptYSize value="1230"/&gt;
&lt;ySubscriptXOffset value="0"/&gt;
&lt;ySubscriptYOffset value="0"/&gt;
&lt;ySuperscriptXSize value="1285"/&gt;
&lt;ySuperscriptYSize value="1230"/&gt;
&lt;ySuperscriptXOffset value="0"/&gt;
&lt;ySuperscriptYOffset value="560"/&gt;
&lt;yStrikeoutSize value="120"/&gt;
&lt;yStrikeoutPosition value="530"/&gt;
&lt;sFamilyClass value="260"/&gt;
&lt;panose&gt;
&lt;bFamilyType value="2"/&gt;
&lt;bSerifStyle value="4"/&gt;
&lt;bWeight value="5"/&gt;
&lt;bProportion value="2"/&gt;
&lt;bContrast value="5"/&gt;
&lt;bStrokeVariation value="5"/&gt;
&lt;bArmStyle value="5"/&gt;
&lt;bLetterForm value="3"/&gt;
&lt;bMidline value="3"/&gt;
&lt;bXHeight value="4"/&gt;
&lt;/panose&gt;
&lt;ulUnicodeRange1 value="11100000 00000000 00000011 10000111"/&gt;
&lt;ulUnicodeRange2 value="01000000 00000000 00000000 00010011"/&gt;
&lt;ulUnicodeRange3 value="00000000 00000000 00000000 00000000"/&gt;
&lt;ulUnicodeRange4 value="00000000 00000000 00000000 00000000"/&gt;
&lt;achVendID value="LINO"/&gt;
&lt;fsSelection value="00000000 01000000"/&gt;
8 The reader will notice that the global element in this TTX table is OS_2, not OS/2, a name that is not
suitable for XML, as it contains a slash.
```

D.4. The Kernel of the TrueType Tables
&lt;fsFirstCharIndex value="32"/&gt;
&lt;fsLastCharIndex value="65532"/&gt;
&lt;sTypoAscender value="1499"/&gt;
&lt;sTypoDescender value="-"/&gt;
&lt;sTypoLineGap value="682"/&gt;
&lt;usWinAscent value="2150"/&gt;
&lt;usWinDescent value="613"/&gt;
&lt;ulCodePageRange1 value="00100000 00000000 00000001 10011111"/&gt;
&lt;ulCodePageRange2 value="00000000 00000000 00000000 00000000"/&gt;
&lt;sxHeight value="925"/&gt;
&lt;sCapHeight value="1405"/&gt;
&lt;usDefaultChar value="0"/&gt;
&lt;usBreakChar value="32"/&gt;
&lt;usMaxContext value="3"/&gt;
&lt;/OS_2&gt;
A few interesting entries:
• version: today we are at version 3.
• xAvgCharWidth, the average width of all the glyphs (except those that have a zero width).
• usWeightClass, the font’s weight, an even number of hundreds between 100 (very light)
and 900 (very bold). Usual value: 400.
• usWidthClass, the font’s width, an integer between 1 (ultra-condensed) and 9 (ultraextended). Usual value: 5.
• fsType, a very important entry, as it determines whether the font is protected, whether
it can be incorporated into a publicly distributed document, and, if so, under what conditions. Sixteen flags are available. If they are all disabled, there is no restriction on including the font within documents. Here are the meanings of some of the other bits:
– Bit 1: if it is enabled, and if it is the only bit enabled (the value of fsType thus being
0x0002), then the font is under a strict license: it may not be incorporated into a
document in any way!
– Bit 2: if it is enabled, the font may be installed temporarily on other systems, but
only for the purposes of reading and printing (as is the case, for example, in PDF
documents);
– Bit 3: like the preceding, but the font may also be used for editing (as is the case, for
example, with fonts included in Word documents);
– Bit 8: this flag, if enabled, prohibits the use of partial fonts.9
– Bit 9: if this flag is enabled, only the bitmaps contained in the font may be included
in a document.
9 Yet partial fonts are a good thing, as they are less bulky and better protected against piracy: what would
a pirate do with a font half of whose glyphs were missing?

Appendix D : The TrueType, OpenType, and AAT Font Formats
• ySubscriptXSize, ySubscriptYSize, ySuperscriptXSize, ySuperscriptYSize: the horizontal and vertical sizes of the font’s subscripts and superscripts (the two sizes are kept
separate in case we should wish to stretch or shrink the superscripts and subscripts to
achieve an optical correction).
• ySubscriptXOffset, ySubscriptYOffset, ySuperscriptXOffset, ySuperscriptYOffset:
the horizontal and vertical offsets of the subscripts and superscripts. As for the horizontal
offset, the typesetting software would be better offusing the bounding box of each glyph:
examples such as A2 (superscript too far to the right) and f 2 (superscript too far to the
left) show that this offset cannot be the same for every glyph. As for the vertical offset, the
situation is a bit better, but TrueType forgot the case in which we have both a superscript
and a subscript. In this case, it is better to separate the subscripts from the superscripts.
Just compare x0x0 and x0
0: the subscript is higher in the former than in the latter. This
detail, of course, escaped the notice of TrueType.
• yStrikeoutPosition and yStrikeoutSize: the position and thickness of the strikethrough
bar, if any.
• sFamilyClass and Panose, with their subelements: the IBM (derived from ISO 9541-5)
and Panose-1 classifications of the font. These are described in Chapter 11 of this book,
starting on page 416.
• ulUnicodeRange1 (bits 0–31) to ulUnicodeRange4 (bits 96–127), a sequence of 128 flags,
of which the first 92 correspond to Unicode tables. The list of tables is given in [264]. The
question that arises is “Is the font operational for this or that Unicode table?” For example,
if bit 70 is enabled, it is claimed that one can set type in Tibetan with this font.
• achVendID, a string of four ASCII characters that identifies the foundry. The list of
foundries appears in [270]; there are already 240!
• fsSelection, the Windows counterpart for the entry macStyle in the head table: seven
flags that describe the font. In order, starting with bit 0: italic, underlined, white on black,
outline, strikethrough, bold, average weight and width.
• usFirstCharIndex and usLastCharIndex, the first and last Unicode code points for which
the font contains a glyph.
• sTypoAscender, sTypoDescender, and sTypoLineGap: entries that are oddly similar to ascent, descent, and lineGap in the hhea table but that should not necessarily be so precise
or so closely tied to the vagaries of the glyphs’ outlines. Windows supposedly uses these
values to find the ideal parameters for layout; thus we have a certain degree of artistic
freedom.
• usWinAscent and usWinDescent, once again, are for ascenders and descenders, but here
their definition is clear: they are the font’s vertical extrema, taken from the bounding box.
• ulCodePageRange1 and ulCodePageRange2, a sequence of 64 flags representing the font’s
compatibility with the same number of Microsoft code pages:

D.4. The Kernel of the TrueType Tables
Bit
Code page
Name
Latin 1
Latin 2
Cyrillic
Greek (“monotonic”)
Turkish
Hebrew
Arabic
Windows for the Baltic states
Vietnamese
Thai
JIS/Japan
Chinese, simplified
Korean, Wansung
Chinese, traditional
Korean, Johab
MacRoman
OEM
Symbols
IBM Greek
MS-DOS Russian
MS-DOS Nordic
Arabic
MS-DOS Canadian French
Hebrew
MS-DOS Icelandic
MS-DOS Portuguese
IBM Turkish
IBM Cyrillic
Latin 2
MS-DOS Baltic
Greek (ex 437 G)
Arabic (ASMO 708)
Latin 1
United States
• sxHeight and sCapHeight, what the designer considers the height of the lowercase letters
and the capitals to be.

Appendix D : The TrueType, OpenType, and AAT Font Formats
• usDefaultChar and usBreakChar: what is the Unicode substitution character (the character whose glyph is displayed when we ask the font to display a character that it does
not support), and what is the Unicode character that separates the words in a sentence
of running text? The latter is a very bad idea, for it actually depends on the script. For
example, the words in Thai are not separated, and we may use the Unicode character
0x200B (zero width space) to indicate their boundaries. A font may contain glyphs for
several scripts; which one should it favor over the others?
• Finally—and here again we have a mixed bag—usMaxContext indicates the maximum
length of the context in the advanced OpenType tables. For instance, if the font contains
an ‘ffi’ ligature, it will usually have a ligature feature ffi →‘ffi’ and therefore a context
string (see §D.9.4.4) ffi of length 3. If this is the longest ligature, its length will be the
value of this entry.
D.4.8
The post Table
In Appendix C, §C.5, we saw that to transfer TrueType data to a TrueType processor hidden
deep in the bowels of a PostScript printer, we can employ a PostScript Type 42 font. But
creating that font requires a certain amount of data, and it is easier to collect them into a table
made for the purpose than to go rummaging all over the font. The post table is devoted to
the task. Here is an example:
&lt;post&gt;
&lt;formatType value="2.0"/&gt;
&lt;italicAngle value="0.0"/&gt;
&lt;underlinePosition value="-"/&gt;
&lt;underlineThickness value="120"/&gt;
&lt;isFixedPitch value="0"/&gt;
&lt;minMemType42 value="0"/&gt;
&lt;maxMemType42 value="0"/&gt;
&lt;minMemType1 value="0"/&gt;
&lt;maxMemType1 value="0"/&gt;
&lt;psNames&gt;
<!-- This file uses unique glyph names based on the information
found in the 'post' table. Since these names might not be unique,
we have to invent artificial names in case of clashes. In order to
be able to retain the original information, we need a name to
ps name mapping for those cases where they differ. That's what
you see below. -->
&lt;/psNames&gt;
&lt;extraNames&gt;
<!-- following are the name that are not taken from the standard
Mac glyph order -->
&lt;psName name="missing"/&gt;
&lt;psName name=".null"/&gt;
&lt;psName name="nonmarkingreturn"/&gt;
&lt;psName name="Abreve"/&gt;

D.4. The Kernel of the TrueType Tables
&lt;psName name="Aringacute"/&gt;
...
&lt;psName name="uni1EF9"/&gt;
&lt;psName name="uni20A0"/&gt;
&lt;/extraNames&gt;
&lt;/post&gt;
There have been five successive versions of this table (1, 2, 2.5, 3, and 4), of which 2.5 is obsolete and deprecated. The first nine entries are common to all the versions:
• formatType, the version.
• italicAngle to isFixedPitch correspond to the entries in the PostScript dictionary of
the same name, which is found in every PostScript font (Appendix C).
• minMemType42 and minMemType42 correspond not to PostScript entries but to DSC comments (see §C.1.10). They are the minimum and maximum amounts of virtual memory
to allocate to reading the font. There are two values because processors are often quite
clever and set resources aside when they are shared by several fonts: the maximum value
covers the situation in which no resource is shared, and the minimum value is for the
case in which everything that can be shared already has been shared.
• minMemType1 and minMemType1 are similar, but they are applied when the TrueType font
is converted to PostScript Type 1 (the only solution that was available before Type 42).
One big problem remains: in a PostScript font, the glyphs have names. That is not the case in a
TrueType font, although TTX gives us the illusion of glyph names because of its pseudotable
GlyphOrder. Yet some software, such as Adobe Acrobat, needs these names. It would therefore
be good if we could supply them rather than leaving them to be guessed from the cmap table.
And indeed it is in their strategies for naming glyph that the successive versions of this table
differ.
In version 1, for example, the glyphs were assumed to be named according to a list of
258 glyphs supplied by Apple [56, table post]. It is not very politically correct to favor in this
manner the Latin alphabet as used for the languages of Western Europe, but such questions
did not often arise at the time. In version 2, an explicit name is given to each glyph (other
than those on the list in version 1). Version 3 declares that there are no predefined glyph
names. Let us cite the OpenType specification [264, Chapter 6]: “The printing behavior of
this format on PostScript printers is unspecified, except that it should not result in a fatal or
unrecoverable error.” Finally, version 4 (AAT only) is for composite fonts, in which the only
way to refer to a glyph is through its index. In this case, the post table provides a glyph index
for each glyph in the font (this information comes from the numGlyphs entry in the table
maxp), and in the same order.
The reader must have noticed that what we have just stated in the previous paragraph is not
necessarily reflected in the XML code for the example of a post table in TTX. That comes
from the fact that this information is duplicated in the GlyphOrder table (see §D.4.1), which
plays exactly the same role: it matches names with glyphs. The element psNames contains the
possible exceptions—cases in which the name given in GlyphOrder does not correspond to

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
the PostScript glyph name. Finally, the element extraNames is for informational purposes
only; it contains the glyph names that are not on Apple’s famous list.
D.5
The Tables That Pertain
to TrueType-Style Glyph Descriptions
We have already mentioned that an OpenType font can be of either of two types: it can contain glyph descriptions written in TrueType, or it can contain PostScript CFF code with Type 2
charstrings. In this section, we shall concern ourselves with the tables that pertain to the first
case. TrueType and AAT fonts must necessarily be of this type.
D.5.1
The loca Table
In a binary TTF file, loca is a table of pointers to glyph descriptions in the glyf table (pointers
calculated with reference to the start of the glyf table). This table does not belong in a TTX
document (this is precisely the sort of calculations that we avoid by converting to XML). We
find merely
&lt;loca&gt;
<!-- The 'loca' table will be calculated by the compiler -->
&lt;/loca&gt;
Isn’t that beautiful?
D.5.2
The glyf Table
This table is often the bulkiest one in a TrueType font. It is certainly the most important one,
as it contains the descriptions of the contours of the glyphs, and a font without glyphs is like a
forest without trees. Here is an example of the glyf table: the letter ‘A’ from the font Palatino
Linotype:
&lt;glyf&gt;
...
&lt;TTGlyph name="A" xMin="35" yMin="-" xMax="1545" yMax="1487"&gt;
&lt;contour&gt;
&lt;pt x="44" y="-" on="1"/&gt;
&lt;pt x="35" y="0" on="1"/&gt;
&lt;pt x="35" y="52" on="1"/&gt;
... 43 similar lines ...
&lt;pt x="363" y="0" on="0"/&gt;
&lt;pt x="266" y="0" on="1"/&gt;
&lt;pt x="156" y="0" on="0"/&gt;
&lt;/contour&gt;
&lt;contour&gt;
&lt;pt x="500" y="553" on="1"/&gt;
&lt;pt x="1006" y="553" on="1"/&gt;
```

```text
D.5. The Tables That Pertain to TrueType-Style Glyph Descriptions
&lt;pt x="755" y="1156" on="1"/&gt;
&lt;/contour&gt;
&lt;contour&gt;
&lt;pt x="803" y="1487" on="1"/&gt;
&lt;/contour&gt;
&lt;contour&gt;
&lt;pt x="780" y="-" on="1"/&gt;
&lt;/contour&gt;
&lt;instructions&gt;&lt;assembly&gt;
NPUSHB[ ]
/* 40 values pushed */
51 24 20 20 58 6 51 1 11 13 51 1 83 61 51 1 237 51 1 123
51 251 51 2 11 51 203 51 2 19 12 51 1 30 51 40 23 27 72 16
... 366 lines of code ...
SDB[ ]
DELTAP1[ ]
CALL[ ]
&lt;/assembly&gt;&lt;/instructions&gt;
&lt;/TTGlyph&gt;
...
&lt;/glyf&gt;
The structure is very simple: there is a TTGlyph element for each glyph. Each of these elements
has the following attributes: the glyph’s name (name) and its bounding box (the xMin, yMin,
xMax, and yMax attributes).
Next, there is one contour element for each distinct closed contour in the glyphs. Each contour includes points, which are represented by point elements. The point element has three
attributes: the coordinates of the point (x and y) and an indication of whether the point lies
on the contour or is a control point (see Appendix G). The on attribute takes the value 1 if the
former and 0 if the latter. That may seem simplistic, but owing to the structure of B-splines,
these data are sufficient to describe a TrueType glyph contour.
Note that there are always two more points than are required. These last two points are auxiliary: they are the origin of the coordinate system and the far end of the width vector. They
are sometimes called “phantom points”. Using these two points, we can very conveniently
obtain two vital data: the glyph’s set-width and offset relative to the origin.10 In addition, as
we shall see in Appendix E, these points can be moved under the control of TrueType instructions. For instance, the left side-bearing and the glyph’s set-width can also be generated, quite
naturally, by instructions—something inconceivable under PostScript, where the set-width is
not influenced by hints at all.
The astute reader may have noticed that in the example of the letter ‘A’ above, after the two
“genuine” contours of the letter ‘A’, which are the external and internal contours, there are
two “false” contours that contain only one point each. These are the markers that we shall use
in the OpenType advanced typographic tables. In this example, they are markers for placing
an accent above the letter and an accent below.
10 In PostScript Type 1 charstrings, these same two data are given by the first command in the glyph description, named hsbw. TrueType puts these data at the end of the list of points.
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
After the last contour or component element comes an instructions element, which contains the TrueType instructions for optimizing the glyph’s rasterization. These are written in
an assembler-type language in which the TrueType hints are described; we shall describe this
language in Appendix E.
D.5.2.1
Composite glyphs
Aside from the glyphs with genuine contours, we also have, here just as in the AFM files
for PostScript fonts or in TEX’s virtual fonts, the concept of a composite glyph, which is a set
of references to other glyphs, each of them positioned with a certain offset. This feature of
TrueType is often used to create glyphs for accented letters, except, of course, when the accents
for the various letters differ slightly and thus must be designed separately. Here is an example
of a composite glyph, the letter ‘É’ in the same font:
&lt;TTGlyph name="Eacute" xMin="73" yMin="-" xMax="1165" yMax="1894"&gt;
&lt;component glyphName="E" x="0" y="0" flags="0x214"/&gt;
&lt;component glyphName="Acute" x="470" y="0" flags="0x14"/&gt;
&lt;instructions&gt;&lt;assembly&gt;
NPUSHB[ ]
/* 29 values pushed */
3 159 94 1 223 94 1 94 5 3 16 94 1 160 94 176 94 2 0 94 16 94 2 0 94
94 53 53 37
... 8 lines of code ...
DELTAP2[ ]
DELTAP3[ ]
SHC[1]
&lt;/assembly&gt;&lt;/instructions&gt;
&lt;/TTGlyph&gt;
Thus there is one component element for each component of the composite glyph. Each component element takes four attributes: the name of the glyph in question, the coordinates of
the offset, and a number (flags) that is in fact a sequence of 16 flags of no great interest (we
can give the value 0x214 to the first component and 0x14 to the others without much worry;
there are more details in [56, 264]).
D.5.3
The Tables fpgm, prep, and cvt
The tables fpgm and prep contain global TrueType instructions (which, therefore, are not
attached to any specific glyph). These instructions are executed when the first glyph in the
active font is typeset (for fpgm) and every time the type size or the current transformation
matrix is changed (for prep). Examples of these tables:
&lt;fpgm&gt;
&lt;assembly&gt;
NPUSHB[ ]
/* 47 values pushed */
74 73 72 71 70 59 58 57 54 51 50 49 48 47 46 45 44 43 42 41 39
31 30 29 28 27 26 25 24 22 21 20 19 18 17 15 14 13 12 11 8 3 2
... 1357 lines of code ...
```

```text
D.6. The TrueType Tables That Affect PostScript-Style Glyph Descriptions
POP[ ]
EIF[ ]
ENDF[ ]
&lt;/assembly&gt;
&lt;/fpgm&gt;
&lt;prep&gt;
&lt;assembly&gt;
NPUSHB[ ]
/* 17 values pushed */
223 224 22 23 28 212 213 22 23 28 123 124 22 27 123 124 25
PUSHW[ ]
/* 1 value pushed */
... 1449 lines of code ...
SWAP[ ]
WS[ ]
&lt;/assembly&gt;
&lt;/prep&gt;
The table cvt contains the values of global variables, which are used by the instructions (see
§D.8.5). Here is an example:
&lt;cvt&gt;
&lt;cv index="0" value="1481"/&gt;
&lt;cv index="1" value="0"/&gt;
&lt;cv index="2" value="0"/&gt;
...
&lt;cv index="627" value="1067"/&gt;
&lt;cv index="628" value="1539"/&gt;
&lt;cv index="629" value="1427"/&gt;
&lt;/cvt&gt;
D.6
The TrueType Tables That Affect
PostScript-Style Glyph Descriptions
D.6.1
The Table CFF
The table CFF contains a PostScript CFF font with Type 2 charstrings. We have described this
type of table in Appendix C, §C.8.
D.6.2
The Table VORG
This table was born from a small gap in the TrueType structure. When we want to calculate a
glyph’s offset, we know that the starting point of the width vector is the point (0,0) and that
the table hmtx contains the magnitude of the vector. All, then, is well.
But here we find ourselves in utter political incorrectness: that approach works only for horizontal movement, and not everyone in the world uses horizontal movement only. What
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
happens if we move vertically? Well, there is, of course, the table vmtx, which contains the
magnitude of the vertical width vector.
But what is that vector’s starting point? Without that information, we cannot compute its
ending point. Fortunately, the coordinates of the starting point and the ending point appear
in the table glyf: they are the last two points described in the table, the phantom points.
Yes, but OpenType fonts with a CFF table do not have a glyf table! Where, then, shall we find
even the height of the starting point of the width vector?
We have a hard way and an easy way to go about it. The hard way involves interpreting the
charstring and calculating the vertical extrema of all the Bézier curves. The easy way is to use
the VORG table.
This table has only one piece of information to offer us: the y-coordinate of the glyph’s vertical
origin. Here is an example of this type of table:
&lt;VORG&gt;
&lt;majorVersion value="1"/&gt;
&lt;minorVersion value="0"/&gt;
&lt;defaultVertOriginY value="878"/&gt;
&lt;numVertOriginYMetrics value="2"/&gt;
&lt;VOriginRecords&gt;
&lt;VOriginRecord&gt;
&lt;glyphName value="A"/&gt;
&lt;vOrigin value="800"/&gt;
&lt;/VOriginRecord&gt;
&lt;VOriginRecord&gt;
&lt;glyphName value="AE"/&gt;
&lt;vOrigin value="900"/&gt;
&lt;/VOriginRecord&gt;
...
&lt;/VOriginRecords&gt;
&lt;/VORG&gt;
In this table we find the version (major and minor components), a default value for the ordinate of vertical origins, the number of exceptions to this rule, one VOriginRecord subelement
for every different vertical origin of the default value. Each of these subelements contains a
glyph name and the value of the ordinate of that glyph’s vertical origin.
D.7
Bitmap Management
D.7.1
The Tables EBLC and EBDT (Alias bloc and bdat)
Every effort was made so that TrueType fonts could contain bitmaps, together with—or instead of—vector contours. We have seen in Appendix A that a number of bitmap formats
have appeared in the past 20 years and that some of them turned out to be better suited than
others to certain situations. For instance, there are fonts with multiple sizes of glyphs, others
with only one size, monospaced and proportional fonts, etc. The fact that ideographic fonts
```

```text
D.7. Bitmap Management
containing thousands, even tens of thousands of glyphs are monospace fonts is a decisive factor: when there are tens of thousands of glyphs, every single bit saved in the glyph descriptions
is important; thus such fonts will not be described in the same way as alphabetic fonts, in
which each letter may in principle have a different width.
TrueType had an ingenious idea: a font can be “multiformat”; i.e., we divide its glyphs into
a number of blocks, and for each block we use the appropriate bitmap font format. If many
glyphs have the same metrics, we store those metrics separately and declare that they apply
to all of the glyphs in the block in question. If they have different metrics, those metrics will
be stored with the glyphs.
Thus there are different sizes of bitmap fonts and, for each size, different font formats, which
are applied to collections of glyphs in different blocks. TrueType provides two tables: one
(EBLC) classifies the glyphs, the other (EBDT) contains the bitmaps. Thus the system that needs
a bitmap glyph will first go to the table EBLC; there it will find a subtable corresponding to the
desired size (measured in pixels per em), and that subtable will lead it to a table containing
collections of glyphs. There it will learn the block to which the glyph corresponds and that
block’s format; according to the format, it will find the metrics at that very location in the
EBLC table or else in the glyph descriptions, in the EBDT table. Finally, the EBLC table will
provide the system with the exact address of the glyph description in the EBDT table, and voilà!
Here is an example of the tables EBLC and EBDT:
&lt;EBLC&gt;
&lt;tableVersion version="2.0"/&gt;
&lt;numSizes value="4"/&gt;
&lt;bitmapSize ppemX="9" ppemY="9"&gt;
&lt;numberOfIndexSubTables value="1"/&gt;
&lt;colorRef value="0"/&gt;
&lt;hori&gt;
&lt;ascender value="7"/&gt;
&lt;descender value="0"/&gt;
&lt;widthMax value="9"/&gt;
&lt;caretSlopeNumerator value="0"/&gt;
&lt;caretSlopeDenominator value="0"/&gt;
&lt;caretOffset value="0"/&gt;
&lt;minOriginSB value="0"/&gt;
&lt;minAdvanceSB value="0"/&gt;
&lt;maxBeforeBL value="7"/&gt;
&lt;minAfterBL value="0"/&gt;
&lt;/hori&gt;
&lt;vert&gt;
&lt;ascender value="0"/&gt;
&lt;descender value="0"/&gt;
&lt;widthMax value="0"/&gt;
&lt;caretSlopeNumerator value="0"/&gt;
&lt;caretSlopeDenominator value="0"/&gt;
&lt;caretOffset value="0"/&gt;
&lt;minOriginSB value="0"/&gt;
```

Appendix D : The TrueType, OpenType, and AAT Font Formats
&lt;minAdvanceSB value="0"/&gt;
&lt;maxBeforeBL value="0"/&gt;
&lt;minAfterBL value="0"/&gt;
&lt;/vert&gt;
&lt;startGlyphIndex value="1"/&gt;
&lt;endGlyphIndex value="256"/&gt;
&lt;bitDepth value="1"/&gt;
&lt;flags value="1"/&gt;
&lt;indexSubTables&gt;
&lt;indexSubTable firstGlyph="1" lastGlyph="256"
indexFormat="1" imageFormat="2" imageDataOffset="4">
&lt;hexdata&gt;
00000000 0000000d 00000019 00000026
00000032 00000040 0000004d 0000005a
00000067 00000074 00000080 0000008e
...
00000e66 00000e73 00000e81 00000e8e
00000e9b 00000ea8 00000eb5 00000ec3
00000ed0 00000edd 00000eea 00000ef7
&lt;/hexdata&gt;
&lt;/indexSubTable&gt;
&lt;/indexSubTables&gt;
&lt;/bitmapSize&gt;
&lt;/EBLC&gt;
&lt;EBDT version="00020000"&gt;
&lt;hexdata&gt;
08092422 595555ff 1c2b0807 0108094c
06080702 0809252a 0aa92011 3c080800
...
9834c0b5 a9560809 01080908 552f152a
c3fe541e 08080108 0908bfaa aeb17b9d
&lt;/hexdata&gt;
&lt;/EBDT&gt;
The exact structure of the EBLC table is as follows:
• At the highest level, there are just two pieces of information: the version (tableVersion)
of the table (currently 2), and the number of bitmap fonts that it contains (numSizes).
In TrueType jargon, a bitmap font is called a strike. For each strike there is a bitmapSize
element, whose attributes ppemX and ppemY give its size: the number of pixels per em,
horizontally and vertically.
• Inside a bitmapSize we find, first, some global data, including metrics and other data;
and, second, a subelement that will contain tables of pointers to the glyphs’ bitmaps.
• The global data that we find in a bitmapSize are the following:

D.7. Bitmap Management
a
b
g
h
Horizontal origin
Vertical origin
Horizontal advance
Vertical advance
Horizontal metrics
Vertical metrics
Horizontal
baseline
Vertical baseline
Width
Height
c
e
f
d
Figure D-1: The horizontal and vertical metrics of a bitmap glyph in an EBLC table. To avoid giving incomprehensible names, we have used the letters a, ... , h for some measurements that we shall use later.
– The number of tables of pointers (numberOfIndexSubTables). Specifically, for each
bitmap font, we can have several blocks of glyphs, in different formats. And these
tables of pointers can also be in formats different from the bitmaps—which yields
many possible combinations, and therefore as many potential pointers.
– The depth of the bits (between 1 for black-and-white and 8 for 256 gray levels) and the
color mode: for Microsoft, this value must always be 0; for Apple, it can be 0 (a standard black-and-white font), 1 (a black-and-white font, but with more bits per pixel,
so that it can be displayed without interpolation on devices with a greater depth of
bits), or 2 (a color font or a font with gray scales).
– The indices of the first and last glyphs (startGlyphIndex, endGlyphIndex).
– A flag, flags, to indicate whether the glyphs are horizontal (value 1) or vertical
(value 2). A word of explanation is needed: of the formats for tables of poiners,
there are some with “short metrics” and others with “long metrics”. “Long metrics”
support two directions of writing. “Short metrics” support only one, and it must be
the same for the entire font—which is why we have this flag that is relevant only to
“short metrics”.
– Two subelements, called sbitLineMetrics in TrueType jargon, that contain global
horizontal (hori) and vertical (vert) metrics. These are the metrics that come into
play if the chosen format for the table of pointers is “without metrics” (a method well
suited to the ideographic scripts, in which tens of thousands of glyphs have the same
metrics). These metrics contain the following subelements: the height of the ascenders (ascender) and the depth of the descenders (descender); the maximum width
of the glyph (widthmax); the slope and offset of the caret (caretSlopeNumerator,
caretSlopeDenominator, and caretOffset); according to Figure D-1, in the horizontal case, the minimum value of a (minOriginSB), the minimum value of b
(minAdvanceSB), the maximum value of c (maxBeforeBL), and the minimum value
of d (minAfterBL); in the vertical case, the minimum value of g (minOriginSB), the

Appendix D : The TrueType, OpenType, and AAT Font Formats
minimum value of h (minAdvanceSB), the maximum value of e (maxBeforeBL), and
the minimum value of f (minAfterBL).11
– An element indexSubTables, containing a subelement indexSubTable (without
an ‘s’) for each block of glyphs in the strike. Each indexSubTable element has four
attributes: the index of the first glyph in the block (firstGlyph), the index of the
last glyph (lastGlyph), the format number of the table of pointers (indexFormat),
the format number of the bitmap data (imageFormat), and, finally, the offset
(imageDataOffset) of the description of the first glyph in the EBDT table—an offset
computer starting from the beginning of the table. Then comes the table of pointers,
in the form of hexadecimal data.
All that remains is to describe the various formats for the table of pointers. Some of them
contain metrics; others do not. Here they are:
• Format 1: the simplest format. The glyphs’ bitmaps are of variable size. Each position
between firstGlyph and lastGlyph has a 4-byte pointer into the EBDT table, even if there
is no corresponding glyph (in which case the pointer points to the end of the last glyph
that exists before the positions that precede the current position).
• Format 2: the format specific to ideographic scripts. All the bitmap images for glyphs are
of the same size. This format is not at all similar to the previous one. In particular, instead
of the block of code in hexadecimal, the following elements appear:
&lt;indexSubTable firstGlyph="1" lastGlyph="256"
indexFormat="2" imageFormat="2" imageDataOffset="4">
&lt;imageSize value="81"/&gt;
&lt;height value="7"/&gt;
&lt;width value="0"/&gt;
&lt;horiBearingX value="9"/&gt;
&lt;horiBearingY value="0"/&gt;
&lt;horiAdvance value="0"/&gt;
&lt;vertBearingX value="9"/&gt;
&lt;vertBearingY value="0"/&gt;
&lt;vertAdvance value="0"/&gt;
&lt;/indexSubTable&gt;
where the entries have the following meanings, as shown in Figure D-1: height (height),
width (width), a (horiBearingX), c (horiBearingY), horizontal advance (horiAdvance), e
(vertBearingX), g (vertBearingY), vertical advance (vertAdvance).
These measurements are called “big metrics” in TrueType jargon because they contain
information about the horizontal and vertical directions; they are also used in the EBDT
table when the bitmaps are accompanied by metrics, as in Format 1, above. There are also
the “small metrics” (used only in the EBDT table); for them, we have the entries BearingX,
11 Note: Here we have used the letters a, . . . , h to denote measurements, rather than giving those
measurements’ names. The Microsoft and Apple specifications assign quite disconcerting names to these measurements: for example, c is called horiBearingY, i.e., “horizontal side-bearing on the y-axis (!). The reader’s
mental well-being seemed more important to us than the need to assign a name to absolutely everything.

D.7. Bitmap Management
BearingY, and Advance, which have the meaning of horiBearingX, etc., when the flags
entry that we saw above has the value 1 and the meaning of vertBearingX, etc., when
that entry has the value 2.
• Format 3 is identical to Format 1, except that only 2 bytes are used for each pointer. Thus
the format takes up less space, but the EBDT can be no larger than 64 kilobytes.
• Format 4 solves the problem of sparse blocks—those that have a few glyphs at the beginning and a few more several thousand positions later. With a table of Format 1 or
Format 2, we would have to include useless pointers for all the intermediate positions.
Here we have the number of glyphs, in the form of the additional attribute numGlyphs
in the indexSubTable element. Next, in a hexadecimal block, we have, for each glyph
that actually exists in the EBDT table, its index (2 bytes) and its position in the table (also
2 bytes).
• Format 5 combines formats 4 (sparse tables) and 2 (glyphs of identical size). In it, therefore, appear the element imageSize and the “big metrics” of Format 2, together with the
attribute numGlyphs of Format 4. The hexadecimal block that follows contains the indices
of the glyphs that actually exist, encoded as 2-byte values.
Note that formats 4 and 5 of the table of pointers can be used only within EBLC, not within
bloc (the Apple table corresponding to EBLC). That is the only difference between EBLC
and bloc.
Now let us move on to the description of the EBDT table. In TTX, its appearance is quite deceptive: just a block of hexadecimal data. At the beginning of this block is a 4-byte version
number; all the rest is merely bitmap data. What, then, can we say about these bitmap data?
Well, we can describe their structure, even though TTX does not give us any more help. We
thus find ourselves forced to make recourse to the good old-fashioned method of counting
bytes, which we have used for most other bitmap formats (Appendix A) but have elegantly
avoided when describing the other TrueType tables, thanks to TTX.
The contents of the EBDT table are divided into several subblocks, each of which can be in
another format. When we are inside the EBDT table, there is no way to know where each
subblock begins; only the EBLC table contains that information.
There are nine formats for subblocks in EBDT:
• Format 1: for each glyph, we have first a series of “small metrics” (5 bytes) and then the
bitmap data, aligned on 1-byte boundaries (in other words, when a row of pixels ends
within a byte, we pad the byte with bits having the value zero). Aligning the images on
1-byte boundaries gives us access to the glyphs a few milliseconds faster.
• Format 2: as above, except that the alignment is performed even within the bytes. In
other words, the data contain only the pixels that appear within the glyph’s bounding
box; no padding bits are used.
• Format 3 is obsolete.

Appendix D : The TrueType, OpenType, and AAT Font Formats
• Format 4 (used only in bdat tables) uses Huffman compression. This is a first, since, as
we saw in Appendix A, no other bitmap font format than TEX’s PK format is compressed.
The Huffman compression [255, pp. 61–71] of a string composed of symbols drawn from
a certain set of symbols involves creating a binary tree (a tree in which each node that is
not a leaf has exactly two children) corresponding to the frequency of the symbols in the
string. The most common symbol will therefore be at the top of the tree, and the least
frequent symbols will appear at the leaves. Since each node has exactly two children, we
can say that these children correspond to the numbers 0 and 1. The path that connects the
root of the tree to any given leaf is therefore a binary number. The larger this number,
the less common the corresponding symbol. We replace the symbols in the string with
these binary numbers, and the compression is finished.
This method of compression is quite efficient because the most frequent symbols are
replaced by very few bits. To decompress a string, we first read the tree and then read
the data bit by bit, following along in the tree: every time we reach a leaf, we replace the
bits read with the symbol in question. This extremely simple method of compression,
developed by Daniel Huffman in 1952 [185], is applied here by taking two sets of symbols:
the groups of black pixels and the groups of white pixels. We build a separate tree for
each group. We read the bits and interpret them alternately as belonging to the first or
the second tree.
In this type of subblock, we have, first of all, three pointers (of 4 unsigned bytes each) to
the tree of white pixels, the tree of black pixels, and the start of the data; next come these
three types of data, in the same order.
• Format 5 contains no metrics: the glyphs are assumed to have the same metrics, therefore
the same number of pixels. The rows of pixels are aligned on bits (within the bytes).
• Format 6 is like Format 1, but the glyphs have “big metrics” (a useful format when glyphs
are to be used horizontally and vertically).
• Format 7 is the combination of 2 and 6 (alignment on bits, with “big metrics”).
• Formats 8 and 9 contain composite glyphs. The principle is the same as for the composite
glyphs in AFM files (see §C.3.7) or TEX’s virtual fonts (see §B.3): we take n glyphs, each
of which may be displaced in both directions, and create a new glyph from them. For
example, we can combine the glyph “acute accent” with the glyph ‘e’ to obtain an ‘é’. We
can have as many glyphs as we please, and each of them can in turn be a composite.
The data of Format 8 are structured as follows: First, a set of “small metrics” for the
composite glyph, followed by the number of components. Next, for each glyph, its glyph
code and its horizontal and vertical offsets, encoded as one signed byte (an offset can be
between −127 and +128 pixels).
Format 9 is similar, but its metrics are “big.”
Note that Format 4 can be used only in bdat tables and that Formats 8 and 9 can be used only
in EBDT tables.

```text
D.7. Bitmap Management
這本書寫得十分好用了很合當的例子我十分欣賞
Figure D-2: Comparison of a line of Chinese text rendered at 12 pixels per em and 24 pixels per em (by a
rather poor rendering engine), then enlarged from 12 to 24 by means of the EBSC table. Finally, the same
text in a vector font.
D.7.2
The EBSC Table
Suppose that you have just finished designing the 7,000 bitmap glyphs of a fine Chinese font
at the sizes of 9 and 12. Your boss then comes to you and asks for size 18 as well, due tomorrow! Panic sets in! It is in these difficult moments that the EBSC table comes to the rescue:
thanks to it, we can request that a new size be generated from an existing one. The procedure
in question involves scaling bitmaps and rounding to the nearest pixel. We can thus obtain
size 18 in a flash, simply by scaling size 12 up by 150 percent. Unfortunately, the quality of
the resulting font is very much in doubt, but could we expect anything better?
The EBSC table has the following structure:
&lt;EBSC&gt;
&lt;tableVersion version="2.0"/&gt;
&lt;numScales value="1"/&gt;
&lt;bitmapScale ppemX="18" ppemY="18"
substitutePpemX="12" substitutePpemY="12">
&lt;hori&gt;
&lt;ascender value="12"/&gt;
&lt;descender value="0"/&gt;
&lt;widthMax value="11"/&gt;
&lt;caretSlopeNumerator value="0"/&gt;
&lt;caretSlopeDenominator value="0"/&gt;
&lt;caretOffset value="0"/&gt;
&lt;minOriginSB value="0"/&gt;
&lt;minAdvanceSB value="0"/&gt;
&lt;maxBeforeBL value="12"/&gt;
&lt;minAfterBL value="0"/&gt;
&lt;/hori&gt;
&lt;vert&gt;
&lt;ascender value="0"/&gt;
&lt;descender value="0"/&gt;
&lt;widthMax value="0"/&gt;
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
&lt;caretSlopeNumerator value="0"/&gt;
&lt;caretSlopeDenominator value="0"/&gt;
&lt;caretOffset value="0"/&gt;
&lt;minOriginSB value="0"/&gt;
&lt;minAdvanceSB value="0"/&gt;
&lt;maxBeforeBL value="0"/&gt;
&lt;minAfterBL value="0"/&gt;
&lt;/vert&gt;
&lt;/bitmapScale&gt;
&lt;/EBSC&gt;
Here we recognize the elements hori and vert from the EBLC table (see §D.7.1).
D.7.3
The bhed Table
The bhed table is used by Apple alone. It is identical to the head table and replaces that table
when the font has no vector contours but only bitmaps. A font containing bhed must, first
of all, also contain bloc and bdat tables and, second, must not contain head or glyf tables.
D.8
Some Other Optional Tables
We shall leap all over the place in this section, since we shall describe all the optional TrueType tables that are not “advanced tables” (in the sense of OpenType and AAT).
D.8.1
The DSIG Table
The DSIG table (OpenType only) contains a digital signature of the font. The principle of digital
signatures is as follows: the font’s designer or vendor registers with a provider of digital signatures (such as VeriSign, Cybertrust, or another) and obtains two “keys”: a private key and a
public key. Using the private key, she produces the font’s digital signature. Operating systems
and other software that uses fonts will read the public key and use it to authenticate the font.
In other words, they check that it does indeed correspond to the original data.
OpenType accepts PKCS#7 digital signatures with an X.509 certificate [308, 187].
TTX shows the contents of the DSIG table in the form of hexadecimal data, but at the same
time it warns the user that the table will no longer be valid after conversion to TTF.
Microsoft freely distributes a tool [256] that digitally signs OpenType and TrueType fonts. The
tool is free, but the certificate provided by VeriSign [339] costs the considerable annual sum
of more than \$430. And take note: before committing yourself, consider that you will never
be able to stop your annual subscription if you do not want your users to be confronted with
warning messages about a revoked certificate! We may well ask who are the greater crooks:
font pirates or authenticators.12
12 Fortunately, books such as Web Security, Privacy & Commerce [147] show us how to create certificates
ourselves.
```

D.8. Some Other Optional Tables
D.8.2
The gasp Table
The name gasp is the acronym of grid-fitting and scan procedure. It is a small table whose purpose is to tell the system how to render the glyphs at different point sizes. Here is one such
table:
&lt;gasp&gt;
&lt;gaspRange rangeMaxPPEM="8" rangeGaspBehavior="2"/&gt;
&lt;gaspRange rangeMaxPPEM="16" rangeGaspBehavior="1"/&gt;
&lt;gaspRange rangeMaxPPEM="65535" rangeGaspBehavior="3"/&gt;
&lt;/gasp&gt;
The gasp element contains several gaspRange elements. The attribute rangeGaspBehavior
indicates the method for rendering; it may take the following values:
• 0: use neither TrueType instructions TrueType nor gray levels.
• 1: use TrueType instructions but not gray levels.
• 2: use gray levels but not TrueType instructions.
• 3: use both TrueType instructions and gray levels.
The idea is that we are often better offusing gray levels when setting type at small sizes; at
moderate sizes, we benefit more from using instructions; at large sizes, we can use both; and
at very large sizes, we need neither instructions nor gray levels. The attribute rangeMax gives
the maximum value of each interval; the intervals are arranged in increasing order. In the
example above, therefore, we start with gray levels (up to 8 pixels per em), then we move on
to instructions (up to 16 pixels per em), and finally we combine the two. The maximum size
is encoded as a 2-byte value in the TTF file; therefore, 65,535 is the largest value allowed for
this attribute.
The gasp table can be used only with TrueType glyphs; it does not work in OpenType/CFF
fonts.
D.8.3
The Tables hdmx and LTSH
Do not confuse hdmx with its near cousin hmtx. Both tables contain horizontal widths; the
only difference is that the widths in hmtx (a required table) are expressed in TrueType units
while those of hdmx (an optional table) are expressed in pixels.
According to Microsoft, what is useful about the hdmx is that it relieves the system from having
to perform scaling and rounding operations for every size of glyphs in the hmtx table. We may
well wonder whether the savings in time and CPU cycles is really significant enough to justify
another table. In any event, these tables do exist, and have existed since the beginning.
In its binary form, this table contains subtables corresponding to the different sizes supported. Each subtable contains indices for glyphs and the corresponding widths.
TTX, on the other hand, displays this table in a much more convenient manner. Here, for
example, is an hdmx table as presented by TTX:

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
&lt;hdmx&gt;
&lt;hdmxData&gt;
ppem:
... 100 ;
.notdef:
... 100 ;
.null:
...
0 ;
A:
...
68 ;
AE:
...
99 ;
AEacute:
...
99 ;
...
&lt;/hdmxData&gt;
&lt;/hdmx&gt;
Here we have omitted the sizes between 19 and 100 so that the code will fit on the page. The
first line indicates the sizes (there are 31 in all); the following lines show the widths corresponding to these sizes for each glyph. Microsoft asks us to include at least the following sizes
in the table: 11, 12, 13, 15, 16, 17, 19, 21, 24, 27, 29, 32, 33, 37, 42, 46, 50, 54, 58, 67, 75, 83,
92, and 100.
Note that there is also a VDMX table (see §D.8.5); but it is quite different from hdmx, as it does
not provide the (vertical) widths for each glyph in the font, only their extreme values.
The astute reader will certainly have noticed that the letter ‘A’ is narrower at 10 points than
at 9. How can that be possible? There is only one plausible explanation: δ instructions. The
font’s designer specified that the last auxiliary point (the glyph’s width) at size 10 be moved to
the left; thus the width is smaller than that of the preceding size, for which no δ instruction
has been given. That, by the way, is one of the raisons d’être for this table: without it, the
rendering engine would be required to apply all the TrueType instructions before making a
decision about the width of a given glyph.
In Figure D-3, we see the widths of the letter ‘A’ in Verdana as they are given in the font’s hdmx
table. Although there is still a bit of chaos at the smallest sizes, we see that the distribution
becomes almost linear beyond 50 points, which is to be expected, since the effect of TrueType
instructions becomes less marked at large sizes. If the distribution is linear, there is no need
for the hdmx: we merely apply a simple rule of three and round to the nearest pixel. But how
do we know at what point the distribution becomes linear?
Instead of placing these crucial data into the hdmx table, the inventor of TrueType decided
to create a new table for this purpose, LTSH (unpronounceable acronym of linear threshold).
This table contains the size in pixels per em beyond which the widths in pixels follow a linear
distribution (aside from rounding). Here is an example:
&lt;LTSH&gt;
&lt;yPel name=".notdef" value="1"/&gt;
&lt;yPel name=".null" value="1"/&gt;
&lt;yPel name="A" value="50"/&gt;
&lt;yPel name="AE" value="51"/&gt;
&lt;yPel name="AEacute" value="51"/&gt;
&lt;yPel name="Aacute" value="50"/&gt;
```

D.8. Some Other Optional Tables
taille en ppem
chasse de la lettre A en pixels
yPel
Figure D-3: The distribution of the sizes in pixels of the letter ‘A’ from the font Verdana, as a function of
point size, expressed in pixels per em. The data come from the font’s gasp table.
&lt;yPel name="Abreve" value="50"/&gt;
...
&lt;yPel name="z" value="17"/&gt;
&lt;yPel name="zacute" value="17"/&gt;
&lt;yPel name="zcaron" value="17"/&gt;
&lt;yPel name="zeta" value="13"/&gt;
&lt;/LTSH&gt;
The reader may be astonished to see that the threshold for the letter ‘A’ and its variants is only
50 or 51 pixels per em, whereas it is 17 pixels per em for the letter ‘z’. That is due to the fact
that the definition of this threshold is slightly more complex. For a size to be considered the
“threshold”, at least one of the following two conditions must obtain beyond that size:
• The width as calculated by linear extrapolation coincides with the width after rendering.
• The difference between these two widths is less than 2 percent, but in this case the threshold cannot be lower than 50 pixels per em.
In our example, the letter ‘z’ is apparently stable enough to meet the first condition, whereas
‘A’ is less stable and thus has a higher threshold (which just happens to be 50, the minimum
value in the second condition).
The values in the gasp table that exceed the LTSH threshold are useless.
D.8.4
The kern Table
The kern table was hit with the full force of the font war fought by Microsoft, Apple, and
Adobe. It differs greatly according to the context (TrueType, OpenType, or AAT) and applies
only to fonts with TrueType glyph descriptions (and not, for example, to OpenType/CFF
fonts).
As the name suggests, the purpose of this table is to manage kerning between glyphs.
Here is an example:

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
&lt;kern&gt;
&lt;version value="0"/&gt;
&lt;kernsubtable coverage="1" format="0"&gt;
&lt;pair l="A" r="S" v="-"/&gt;
&lt;pair l="A" r="T" v="-"/&gt;
&lt;pair l="A" r="U" v="-"/&gt;
&lt;pair l="A" r="V" v="-"/&gt;
&lt;pair l="A" r="W" v="-"/&gt;
&lt;pair l="A" r="Y" v="-"/&gt;
...
&lt;pair l="z" r="oslash" v="-"/&gt;
&lt;pair l="z" r="q" v="-"/&gt;
&lt;/kernsubtable&gt;
&lt;/kern&gt;
The first element is the version of the table. In the binary version of this table, we have already
seen a disagreement among the companies mentioned—one that borders on provocation.
Everyone agrees that the table begins with a header containing two numbers: the version
number and the number of subtables. That is quite customary, as most TrueType tables begin
the same way. Yes, but for Microsoft these numbers are encoded as two-byte values, whereas
for Apple they are encoded with four bytes (as if kerning tables with more than 65,536 subtables were anticipated). Result: an incompatibility between the two variants of the kern
table—one that renders the tables for one system useless on the other. Apple backed down
in order to compensate for this ridiculous situation, and today AAT can detect the origin of
the table and read both the version with 2 bytes and the one with 4.
Aside from the difference in the “version” field, there is also a difference in value: 0 for TrueType and OpenType, 1 for AAT.
Then come some kernsubtable elements. These are subtables, and there can be several of
them, in different formats. The format attribute is the format of the table: OS/2 accepts only
Format 0; the OpenType specification OpenType describes formats 0 and 2, but Microsoft
declares in another document [265] that only Format 0 is recognized by Windows. Finally,
Apple accepts formats 0, 1, 2, and 3.
The coverage attribute contains a series of flags that are also victims of this skirmish: for
Microsoft, the first flag, when set, indicates that the kerning pairs are horizontal; the second
flag indicates that the subtable contains “minimal data” (we shall see what these are); the third
indicates that the kerning pairs are applied perpendicularly to the direction of the text (cross
stream); and the fourth indicates that the values of this table’s kerning pairs replace those of
the preceding tables.
Apple, on the other hand, recognizes neither the “minimal data” nor the replacement of the
kerning values. To Apple, the first flag is set if the pairs are vertical (!), the second indicates
cross stream, the third indicates that the different subtables belong to AAT font variations (see
the fvar and gvar tables of AAT).
What is “minimal data”? The concept is quite confused: the OpenType specification declares
that the values of the same kerning pairs taken from the different subtables are added together; to keep the final result from becoming unreasonably large, the specification provides
```

```text
D.8. Some Other Optional Tables
subtables containing only the “minimal data”, which reduces the waste. In any case, Microsoft
makes this concept obsolete by imposing the restriction that there be only one subtable in a
kern table in an OpenType font.
D.8.4.1
The kern subtables common to OpenType and AAT
The most widely used subtable is that of Format 0. It is also the one that we see in the sample
code above. It contains pair subelements, each of which has three attributes: the glyph on the
left (l), the glyph on the right (r), and the kerning value (v). There could hardly be a simpler
approach.
Format 2 sorts the glyphs into different classes according to their behavior with respect to
kerning. For instance, we can say that the kerning applied to ‘AV’ will also apply to ‘ÂV’,
‘ÁV’, ‘ÀV’, etc. The glyphs ‘A’, ‘Â’, ‘Á’, and ‘À’ will therefore be placed into the same class. This
approach is convenient but can be disastrous in certain cases: for example, ‘f è’ must not be
kerned in the same way as ‘fe’.
TTX does not process the tables of Format 2; it represents them as hexadecimal data.
D.8.4.2
The kern subtables specific to AAT
Let us begin with a table of Format 3, which is an improved version of Format 2. The reader is
certainly familiar with the technique of value indexing, which is used, for example, in the GIF
graphics format, in which instead of giving the true value of each pixel, that value is stored
in a table, and the pixel is represented by the index of its value into the table. The benefit is
that when a pixel in an image with 16.7 million colors required three bites, if the image has
fewer than 256 colors, a single byte for the index of the color is sufficient. The image is thus
one third the size.
The same applies here: we index the kerning values on the assumption that there will be
at most 256 different values. We also assume that there is a maximum of 256 classes for the
glyph at the left and the same number for the glyph at the right. Thus the entire table is
encoded as single bytes rather than as two-byte values, as with the tables of Format 2. Other
structural optimizations make this formate more efficient (in both memory space and CPU
time necessary for processing) than Format 2.
Format 1 is the ne plus ultra of kerning: Apple uses a finite automaton, just as with the morx and
just tables. In this regard, we invite the reader to read the introduction to finite automata
for AAT fonts in the relevant section (§D.13.1).
Here the actions of the finite automaton serve (1) to place the glyphs onto a special stack,
called the kerning stack; (2) to retrieve the glyphs from that stack while applying a certain
amount of kerning to each. The benefit is that the stack may contain up to eight glyphs: thus
we can kern as many as eight glyphs simultaneously.
The English-speaking, or merely Eurocentric, reader may wonder why anyone would want
to kern eight glyphs simultaneously. Indeed, eight is a rather high number, but we can easily
find triplets of glyphs that give a different result if we kern them pairwise. For example, the
result will be different if the upper part of the glyph on the left protrudes to the right, the
opposite is true of the glyph on the right, and the glyph in the middle is rather low.
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
To find an example of one such triplet, let us take the Vlaamse Aikido Vereniging (Flemish
Aikido Union), or V.A.V. The reader’s eye will have caught the problem: when we write ‘VAV’,
the letters are correctly kerned; but when periods appear between these letters, the distance
between the period and the letter preceding it is too great. That is very much to be expected,
since when examining the pair ‘.A’ we are no longer aware that the period is preceded by
a ‘V’ (and similarly for the second period). What if there were a different letter before the
period? The designer of the font used in this book, Jean François Porchez, handled the most
extreme case (for example, two ‘V’s in a row: ‘V.V’) and moved the period as far from the ‘V’ as
necessary for the pair of glyphs in question to be correctly kerned. His decision was perfectly
logical, but it causes problems for the opposite extreme: ‘V.A’ and ‘A.V’. How, then, can we
obtain ‘V.A’ and ‘A.V’?
This sort of adjustment is supported by Format 1 of the kern table—a format that is, as you
will recall, reserved for AAT, i.e., for Mac OS X.
Here is an example of a table of this type. We begin with the header:
&lt;kern&gt;
&lt;version value="1"/&gt;
&lt;kernsubtable coverage="1" format="1"&gt;
&lt;stateSize value="7"/&gt;
Next come the table of classes:
&lt;classes&gt;
&lt;class value="0"&gt;
&lt;glyph name=".notdef"/&gt;
&lt;glyph name=".null"/&gt;
...
&lt;glyph name="zerowidthjoiner"/&gt;
&lt;/class&gt;
&lt;class value="1"&gt;
&lt;glyph name="A"/&gt;
&lt;glyph name="B"/&gt;
...
&lt;glyph name="Z"/&gt;
&lt;/class&gt;
...
&lt;/classes&gt;
the table of states:
&lt;states&gt;
&lt;state value="0"&gt;
&lt;entry class="0" value="2"/&gt;
&lt;entry class="1" value="0"/&gt;
...
&lt;entry class="7" value="2"/&gt;
```

```text
D.8. Some Other Optional Tables
&lt;/state&gt;
&lt;state value="1"&gt;
&lt;entry class="0" value="2"/&gt;
&lt;entry class="1" value="0"/&gt;
...
&lt;entry class="7" value="0"/&gt;
&lt;/state&gt;
...
&lt;/states&gt;
the table of entries (or “arrows leading into a state”):
&lt;entries&gt;
&lt;entry value="0" newState="0" flags="0x8000" action="0"/&gt;
&lt;entry value="1" newState="2" flags="0x8000" action="0"/&gt;
&lt;entry value="2" newState="0" flags="0x0000" action=""/&gt;
...
&lt;entry value="5" newState="0" flags="0x8000" action="2"/&gt;
&lt;/entries&gt;
and, finally, the table of actions:
&lt;actions&gt;
&lt;action value="0"&gt;
&lt;eol/&gt;
&lt;/action&gt;
&lt;action value="1"&gt;
&lt;kern value="682"/&gt;
&lt;eol/&gt;
&lt;/action&gt;
&lt;action value="2"&gt;
&lt;flag value="0x8000"/&gt;
&lt;eol/&gt;
&lt;/action&gt;
&lt;/actions&gt;
&lt;/kernsubtable&gt;
&lt;/kern&gt;
These four tables are the four ingredients of a finite automaton: classes, states, entries, and actions. In class, the glyphs are classified according to their behavior. A state contains, for each
class, the entries corresponding to the arrows that leave the state in question. The “entries” are
pairs (ε, α): the action α associated with the arrow leading into state ε. For instance, an entry
entry contains a “new state” value (newState) and a value for the action action. There is one
other attribute: flags. This attribute supplements the action: it is a set of flags describing the
behavior of the processor while it performs the action. Finally comes the element actions,
which contains the actions: each action is a sequence of kerning values or flags, terminated
by an end-of-list marker, eol.
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
If the actions seem complicated in this syntax, that is because, according to the size of the
kerning stack, they can contain up to eight kerning values, which will be applied to the eight
glyphs read from the stack.
D.8.5
The VDMX Table
The VDMX table is in no way a “vertical version” of the hdmx table (and doubtless it is precisely
to avoid this sort of misunderstanding that its name is written in full capitals). It does not
contain the vertical widths in pixels of all the glyphs, only their extreme values. Here is an
example:
&lt;VDMX&gt;
&lt;version version="0"/&gt;
&lt;ratRanges&gt;
&lt;ratRange bCharSet="1" xRatio="1" yStartRatio="1" yEndRatio="1"&gt;
&lt;records startsz="8" endsz="255"&gt;
&lt;record yMax="7" yMin="-" yPelHeight="8"/&gt;
&lt;record yMax="9" yMin="-" yPelHeight="9"/&gt;
&lt;record yMax="10" yMin="-" yPelHeight="10"/&gt;
&lt;record yMax="11" yMin="-" yPelHeight="11"/&gt;
...
&lt;record yMax="233" yMin="-" yPelHeight="254"/&gt;
&lt;record yMax="233" yMin="-" yPelHeight="255"/&gt;
&lt;/records&gt;
&lt;/ratRange&gt;
&lt;/ratRanges&gt;
&lt;/VDMX&gt;
The version can take the value 0 or 1, but Microsoft recommends version 1. The element
ratRanges (“ranges of ratios”) contains some ratRange values corresponding to the different
ratios of width to height. The meaning of the bCharSet attribute depends on the version: if the
version is 0, a bCharSet of 0 means that the record data of the ratRange have been calculated
for all the glyphs; a bCharSet of 1 means that only the “proper” glyphs (those belonging to
the Windows ANSI encoding for Western European languages) have been used in the calculations. For version 1, the meanings are, generally speaking, just the opposite.
The xRatio attribute is the numerator, and yStartRatio and yEndRatio are the extreme values of the range of denominators of the fractions that make the ratios compatible with the
current ratRange.
The records element (with an ‘s’) contains the entries to this table (startsz and endsz indicate the extreme sizes in pixels per em). Each record (without an ‘s’) corresponds to a size in
pixels per em. The attributes yMax and yMin indicate the maximum and minimum values of
the glyphs’ heights.
The data in this table will help the system to calculate the ideal leading for a given font without first rendering all the glyphs in the font.
```

```text
D.8. Some Other Optional Tables
D.8.6
The Tables vhea and vmtx
The vhea table is the spitting image of its horizontal counterpart, hhea. What are left and right
side-bearings in the latter become upper (the vertical distance between the vertical origin and
the upper extremity of the glyph) and lower (the distance between the lower extremity and
the vertical set-width) side-bearings in the former. Here is an example:
&lt;vhea&gt;
&lt;tableVersion value="1.0"/&gt;
&lt;ascent value="1024"/&gt;
&lt;descent value="-"/&gt;
&lt;lineGap value="0"/&gt;
&lt;advanceHeightMax value="0"/&gt;
&lt;minTopSideBearing value="0"/&gt;
&lt;minBottomSideBearing value="0"/&gt;
&lt;yMaxExtent value="0"/&gt;
&lt;caretSlopeRise value="0"/&gt;
&lt;caretSlopeRun value="0"/&gt;
&lt;reserved0 value="0"/&gt;
&lt;reserved1 value="0"/&gt;
&lt;reserved2 value="0"/&gt;
&lt;reserved3 value="0"/&gt;
&lt;reserved4 value="0"/&gt;
&lt;metricDataFormat value="0"/&gt;
&lt;numberOfVMetrics value="247"/&gt;
&lt;/vhea&gt;
There is a version 1.1 of this table, in which the three dimensions ascent, descent, and lineGap, which can ordinarily be calculated from the glyph descriptions, are replaced by the “noble” values vertTypoAscender, vertTypoDescender, and vertTypoLineGap. These are the vertical counterparts of the entries sTypoAscender, sTypoDescender, and sTypoLineGap, which
are found in the OS/2 table. The idea is that the entries that contain the word “typo” are
chosen by the font’s (human) designer and do not strictly correspond to measurements made
within the font. We can thus avoid the risk of having an excessively large or small value caused
by an isolated glyph of secondary importance.
The vmtx table is as simple as its cousin hmtx: it contains the vertical set-width and the top
side-bearing for each glyph in the font. Here is an example:
&lt;vmtx&gt;
&lt;mtx name=".notdef" height="256" tsb="65"/&gt;
&lt;mtx name="A" height="128" tsb="43"/&gt;
&lt;mtx name="Alpha" height="256" tsb="43"/&gt;
&lt;mtx name="B" height="128" tsb="45"/&gt;
&lt;mtx name="Beta" height="256" tsb="42"/&gt;
...
&lt;mtx name="y" height="128" tsb="104"/&gt;
```

Appendix D : The TrueType, OpenType, and AAT Font Formats
&lt;mtx name="z" height="128" tsb="104"/&gt;
&lt;mtx name="zero" height="128" tsb="43"/&gt;
&lt;mtx name="zeta" height="256" tsb="42"/&gt;
&lt;/vmtx&gt;
Here tsb comes from top side-bearing. There is a short version of this table for fonts in which
many glyphs are of the same width (such as ideographic fonts), which cuts the size of the
table down by half. If the font contains numGlyphs glyphs (a value drawn from maxp) and the
table vhea contains a numberOfVMetrics that is different from numGlyphs, then the first numberOfVMetrics glyphs in the vmtx table have both a vertical set-width and a top side-bearing;
the remaining glyphs have only top side-bearings, their set-widths being equal to that of the
last glyph with a stated set-width.
D.8.7
The PCLT Table
This table provides data for the Hewlett-Packard printers that use the PCL 5 language. It is
interesting to note that the original specification for TrueType [258] states that this table
is “highly recommended”, the OpenType specification [264] states that its use in fonts containing TrueType glyph descriptions is “strongly discouraged”, and the AAT specification [56]
ignores it outright. Thus it is a controversial table, to say the least. Here is an example of this
table:
&lt;PCLT&gt;
&lt;version value="1.0"/&gt;
&lt;fontNumber value="1292025634"/&gt;
&lt;pitch value="569"/&gt;
&lt;xHeight value="1062"/&gt;
&lt;style value="0"/&gt;
&lt;typeFamily value="16602"/&gt;
&lt;capHeight value="1466"/&gt;
&lt;symbolSet value="0"/&gt;
&lt;typeface value="M Arial
"/>
&lt;characterComplement value="ffffffff003ffffe"/&gt;
&lt;fileName value="ARLR00"/&gt;
&lt;strokeWeight value="0"/&gt;
&lt;widthType value="0"/&gt;
&lt;serifStyle value="64"/&gt;
&lt;reserved value="0"/&gt;
&lt;/PCLT&gt;
Here is a very brief description of the key entries. (The reader will find more detailed information in [264].)
• fontNumber and typeFamily: identifiers for the font and the font “family” that also identify the foundry.
• pitch: the set-width of the whitespace. (The whitespace in some software is a glyph representing the Unicode character space.)

D.9. The OpenType Advanced Typographic Tables
• xHeight and capHeight: the height of the lowercase and uppercase letters, in TrueType
units.
• style, a number that combines three characteristics of the font: the type of stroke filling
(plain, hollow, shadowed, etc.), the set-width (regular, condensed, extended, etc.), and the
slope (upright, slanted forward, slanted backward).
• symbolSet: what we usually call character set, i.e., the set of glyphs contained in the font.
• typeface: the name of the font as it appears on the printer’s LCD display. It must be
mentioned that neither Microsoft nor Adobe gave any thought to this sort of feature.
• characterComplement: a series of flags that indicate this font’s compatibility with several
encodings. In theory there are 64 possibilities, but only 10 are actually defined.
• fileName: the suggested filename. Six uppercase characters, which brings us back to the
glorious era of MS-DOS filenames—and even earlier, since MS-DOS supported eightcharacter filenames.
• StrokeWeight: the font’s weight, ranging from −7 (“ultra-light”) to 4 (“extra-bold”).
• WidthType: the font’s set-width, ranging from −5 (“ultra-compressed”) to 3 (“extraextended”). The specification states that this value “The values are not directly related to
those in the appearance with field of the style word above”, with no further comments.
• serifStyle: the style of serifs, presented as a list of names, with neither comments nor
examples.
D.9
The OpenType Advanced Typographic Tables
In this section, we shall describe the tables BASE, GDEF, GPOS, GSUB, and JSTF, which make up
the major artillery of the OpenType format. They are called advanced typographic tables, not to
be confused with AAT (Apple advanced typographic tables), which we shall see in the following
section, §D.11.
D.9.1
Important concepts
D.9.1.1
Script, language, feature, lookup
In the advanced typographic tables, we use the concepts of script and language. OpenType
considers that the behavior of a font should differ according to its script, and sometimes even
according to the language being used. Of course, this is an enormous simplification of what
actually happens in the real world, but we can accomplish quite a lot even with this simplification.
More original are the concepts of feature and lookup. In an interactive context, the font’s user
selects those of the font’s features that she wishes to apply. Some features can be enabled
automatically when the font is selected. Each feature includes a number of lookups in the
string being typeset. Each of these lookups can, according to the string being typeset, contain
some operations: positionings or glyph substitutions, etc.

Appendix D : The TrueType, OpenType, and AAT Font Formats
The system works in the following way: the user selects the script and possibly the language
(otherwise the default language will be used); the software shows the available features; the
user decides to apply some of them to a block of text; each feature contains some lookups, all
of which are applied to the block of text; each lookup contains a number of rules for positioning or substitution that depend on the string being set, and the first rule that matches the
conditions imposed is the one that will be executed.
For example, in a Latin font, we declare the Latin script and select English as the default
language. In this font there is a feature called liga (the names of features are like the names of
TrueType tables: they contain four Latin letters; see §D.10.2 for a description of many of the
predefined features). Inside this feature we define a lookup that will handle the “f-ligatures”
(‘fi’, ‘ff’, etc.). Within this lookup we write the rules “f + i →fi”, etc. The user informs the
software that he is using the Latin alphabet and the English language. The software informs
the user that the liga feature is available. The user selects the word “afflict” and enables liga.
The software consults the feature, which supplies a list of the lookups to execute—in this
example, the lookup for the f-ligatures. The lookup in question applies substitution rules.
The word is converted to “afflict” (with the ‘ffl’ ligature), and the task is complete.
In this entire example, order is important only for the rules inside the lookup. Indeed, the
specification does not state whether the lookups are executed in a given order (and even if
they were, the high muckamucks at Adobe declared that their software would execute the
lookups on the OpenType list in the order that it deemed best). Conversely, the order of the
rules is crucial: in the word “afflict”, if the rule “f + l →fl” were placed before the rule “f +
f + l →ffl”, the latter rule would never be executed, and the word would be set as “afflict”
(with the ‘fl’ ligature but not the ‘ffl’ ligature).
Lookups are usually applied to all the glyphs in the input string, but we have the possibility
of limiting their scope to certain types of glyphs. In the GDEF table, we classify the glyphs into
four classes: base glyphs, diacritical marks, ligatures, and components of composite glyphs.
Each lookup has a number called LookupFlag that is, as its name suggests, a series of flags.
The flags contained in this number allow us to apply lookups in a selective manner, ignoring
certain types of glyphs. For instance, suppose that in our font (say, Monotype Garamond italic)
we have a ligature “õ” but also wish to use it with an acute accent and a circumflex accent
(“ö”) or with two circumflex accents (“•”, as in the French verb form “nous prêtâmes”). To
do so, we will arrange for the lookup for ligatures to ignore any accents that appear between
the letters and to create the ligature first. Then the accents will be set by a special lookup
whose purpose is to position accents over the constituents of a ligature. Here are the meanings
of the flags in LookupFlag:
• The first bit, when enabled, indicates that the script is of the Urdu type, in which the text
is typeset at an angle and the last glyph in the word must appear on the baseline. This flag
seems extremely specialized, but for the specific case of Urdu it is of pivotal importance
(see §D.9.3.4).
• The second, third, and fourth bits, when enabled, tell the lookup to ignore base glyphs,
ligatures, and diacritical marks, respectively.
• The last eight bits tell the lookup to ignore not all diacritical marks, but a certain type
(see §D.9.6)

```text
D.9. The OpenType Advanced Typographic Tables
D.9.1.2
Device tables
Another innovation that characterizes the OpenType advanced typographic tables: device tables, so called because they adapt the font data to given resolutions for rendering. We have
already dealt with tables whose purpose is to avoid the need to use TrueType instructions. For
example, the hdmx table contains the values of set-widths as they stand after the instructions
have been executed. Device tables generalize this idea. We take any dimension (for example,
the x-coordinate of a point) and indicate the variations that that dimension has at different
sizes—variations expressed in pixels per em. As this approach recalls that of the δ instructions
(see §E.2.4), these values are called δ values. Here is an example of a device table:
&lt;XAdvDevice&gt;
&lt;StartSize value="9"/&gt;
&lt;EndSize value="19"/&gt;
&lt;DeltaFormat value="1"/&gt;
&lt;DeltaValue value="[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -]"/&gt;
&lt;/XAdvDevice&gt;
where the sizes from 9 to 19 pixels per em are considered and the δ correction is zero everywhere but at the ends of the interval, where it takes the values 1 and −1. That means
that at sizes between 10 and 18, the calculation of the dimension in question from the value
in abstract TrueType units gives good results. Only for the values 9 and 19 is it necessary to
correct the calculation, as indicated.
D.9.1.3
Coverage tables
Another important concept: there is a general method for selecting the glyphs that will be
subjected to positioning or substitution, the coverage table for an operation. The selected
glyphs are placed into a Coverage element. This element takes a single attribute: Format.
There are, in fact, two formats for the Coverage element, but one can look in vain for the
difference between these two formats in the XML code produced by TTX: in both cases, Coverage contains a list of glyphs in the form of Glyph elements. TTX displays both formats in
the same manner, leaving us with a difficult decision for the choice of format. It is enough to
note that Format 1 is better suited to short or sparse lists while Format 2 is better suited to
series of glyphs with contiguous identifiers. Here is an example of a coverage table as shown
by TTX:
&lt;Coverage Format="2"&gt;
&lt;Glyph value="A"/&gt;
&lt;Glyph value="B"/&gt;
&lt;Glyph value="C"/&gt;
...
&lt;Glyph value="uni1EF8"/&gt;
&lt;Glyph value="uni1EF9"/&gt;
&lt;Glyph value="uni20A0"/&gt;
&lt;/Coverage&gt;
Coverage tables are nothing more than lists of glyphs. Their benefit is that their binary form
can be accommodated to the nature of the lists that contain them. For example, if the indices
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
of the glyphs in question are contiguous, we can use a coverage table that contains only the
extreme values of these indices; if, however, the list of indices is sparse, we can use a type of
table adapted to sparse lists. For each type of list of glyphs, there is an appropriate coverage
table. But TTX glosses over these differences by showing us only what is essential: the glyphs
contained in the list.
D.9.2
The BASE Table
Let us begin our tour of the OpenType advanced typographic tables with the most basic one:
the BASE table. This table aims to solve the problem of the different baselines that various
scripts have. The reader will certainly have noticed that we cannot always use the same baseline when mixing scripts. Here are three well-known examples:
I’m based
Here we see the Latin, ideographic Chinese (and Japanese hiragana syllabary), and Tibetan
scripts. The baseline for the ideographs, i.e., the bottom edge of the abstract square in which
each glyph is drawn, is traditionally placed slightly lower than the baseline of the Latin script.
As for Tibetan, its baseline is actually at the top (as with various other scripts of northern
India, as well as Hebrew).
We shall apply the principles of OpenType: first the script, then the language, and finally the
features (there are no lookups). There is another classification at a level higher than script: the
direction of writing.
Here is an example of a BASE table, the one for the font Palatino Linotype, which contains Latin,
Greek, and Cyrillic glyphs but not Chinese or Tibetan ones:
&lt;BASE&gt;
&lt;Version value="1.0"/&gt;
&lt;HorizAxis&gt;
&lt;BaseTagList&gt;
<!-- BaseTagCount=3 -->
&lt;BaselineTag index="0" value="hang"/&gt;
&lt;BaselineTag index="1" value="ideo"/&gt;
&lt;BaselineTag index="2" value="romn"/&gt;
&lt;/BaseTagList&gt;
&lt;BaseScriptList&gt;
<!-- BaseScriptCount=3 -->
&lt;BaseScriptRecord index="0"&gt;
&lt;BaseScriptTag value="cyrl"/&gt;
&lt;BaseScript&gt;
&lt;BaseValues&gt;
&lt;DefaultIndex value="2"/&gt;
<!-- BaseCoordCount=3 -->
&lt;BaseCoord index="0" Format="1"&gt;
&lt;Coordinate value="1405"/&gt;
```

D.9. The OpenType Advanced Typographic Tables
&lt;/BaseCoord&gt;
&lt;BaseCoord index="1" Format="1"&gt;
&lt;Coordinate value="-"/&gt;
&lt;/BaseCoord&gt;
&lt;BaseCoord index="2" Format="1"&gt;
&lt;Coordinate value="0"/&gt;
&lt;/BaseCoord&gt;
&lt;/BaseValues&gt;
<!-- BaseLangSysCount=0 -->
&lt;/BaseScript&gt;
&lt;/BaseScriptRecord&gt;
&lt;BaseScriptRecord index="1"&gt;
&lt;BaseScriptTag value="grek"/&gt;
&lt;BaseScript&gt;
...
&lt;/BaseScript&gt;
&lt;/BaseScriptRecord&gt;
&lt;BaseScriptRecord index="2"&gt;
&lt;BaseScriptTag value="latn"/&gt;
&lt;BaseScript&gt;
...
&lt;/BaseScript&gt;
&lt;/BaseScriptRecord&gt;
&lt;/BaseScriptList&gt;
&lt;/HorizAxis&gt;
&lt;/BASE&gt;
The structure of this table is quite complex. First of all, it must be understood that this table
contains baseline systems, on the one hand, and scripts, on the other. The baseline systems in
the example above are hang for hanging scripts, ideo for ideographic scripts, and romn for
alphabetic scripts. The scripts are cyrl (Cyrillic), grek (Greek), and latn (Latin). For each
script, we do two things: first, we indicate the most appropriate baseline system; second, we
supply the offsets needed for switching from this baseline system to each of the other baseline
systems.
Thus, if we take cyrl as the “dominant script” (if we write in Russian, for example), the table
tells us that the romn baseline (that for the Western languages) is the default line and that the
baseline for Tibetan, for example, will be set at a height of 1,405 TrueType units relative to
the Western baseline.
Now let us examine a sample BASE table in more detail. It contains:
• Two higher-level elements: HorizAxis (the horizontal direction) and VertAxis (the vertical direction).
• Below them, two elements: BaseTagList and BaseScriptList, described here.
• BaseTagList contains one BaselineTag for each baseline system.

Appendix D : The TrueType, OpenType, and AAT Font Formats
• BaseScriptList contains BaseScriptRecords, which correspond to the BaseTagLists.
Each BaseScriptRecord contains the name of a script (BaseScriptTag) and a BaseScript
element.
• BaseScript contains, first of all, the default baseline for the script: it is in the DefaultIndex element.
• Next, it contains the coordinates for the offset required to switch from the default baseline of the dominant script to another baseline: BaseCoord has an index attribute that
connects it to a BaselineTag element and gives us the corresponding baseline system. It
contains a subelement, Coordinate, which is the y-coordinate (or the x-coordinate, if we
are setting type vertically) of the baseline.
We had to go through all these steps before coming to something concrete: the y-coordinates
of the baselines. And we might have hoped that the work would end there, but, alas, the
designers of OpenType are merciless. Therefore let us continue: the element BaseCoord also
contains an attribute format, which can take the values 1, 2, or 3. Indeed, there are three ways
to express the exact position of the baseline in question:
1. The simplest is to give its x-coordinate in TrueType units. That is what we see in the example.
2. Format 2 involves additionally supplying a glyph and a point on the glyph’s contour. This
is a warning for the case in which the TrueType instructions transform the glyph in such a
way that the “uninstructed” baseline is no longer correct. Thus we supply a glyph (which
could be an actual glyph or one designed only for use in this manipulation) and a point
on the glyph, and the TrueType processor will use the position of this point, after the
instructions have been executed, to obtain the baseline.
3. If the reader had imagined that Format 2 was the ne plus ultra of establishing the baseline,
she was mistaken. Format 3 uses a device table (see above, §D.9.1). Thus the processor
has direct access to the number of pixels between two baselines, which is calculated very
precisely and stored in the device table.
We have now dissected the example. But the specification of the BASE table goes even further.
Aside from the baselines, the bounding boxes of the glyphs are also of interest when we calculate the spacing between lines. In the horizontal case, we are concerned with the upper and
lower edges of the box for all the glyphs in the font. We call it MinMax. Unlike the baselines,
MinMax also depends on the current language and the current features.
Therefore we can continue our example by adding the following code within the element
BaseScript and after the last BaseValues:
&lt;DefaultMinMax index="0"/&gt;
&lt;BaseLangSysRecord index="0"&gt;
&lt;BaseLangSysTag value="RUS"/&gt;
&lt;MinMax&gt;
&lt;MinCoord value="-"/&gt;

D.9. The OpenType Advanced Typographic Tables
&lt;MaxCoord value="1861"/&gt;
&lt;FeatMinMaxRecord&gt;
&lt;FeatureTableTag value="smcp"/&gt;
&lt;MinCoord value="-"/&gt;
&lt;MaxCoord value="1861"/&gt;
&lt;/FeatMinMaxRecord&gt;
&lt;FeatMinMaxRecord&gt;
&lt;FeatureTableTag value="ital"/&gt;
&lt;MinCoord value="-"/&gt;
&lt;MaxCoord value="1851"/&gt;
&lt;/FeatMinMaxRecord&gt;
&lt;/MinMax&gt;
&lt;/BaseLangSysRecord&gt;
Suppose that we are in the cyrl (Cyrillic) script. We select a language, in this case Russian
(RUS), and supply the extrema of the glyphs for that language. It is MinMax that contains these
extrema, in the form of the two elements MinCoord and MaxCoord. But the extrema can vary
according to the selected features. That is why MinMax can also contain FeatMinMaxRecord
subelements (for “record of minima and maxima with features”), in which we specify the features (here smcp means “small capitals” and ital means “italics”). One may ask what happens
when we use several features at the same time. The answer does not appear in the specification, but probably the system will take the maximum values for the selected features.
D.9.2.1
Types of baselines predefined for the BASE table
The OpenType specification defines seven types of baselines, with their respective tags:
• romn: the baseline for the alphabetic scripts. (The name is politically incorrect because it
comes from the word “Roman”, whereas not all alphabetic scripts are derived from that
of the Romans.)
• math: the central axis of the mathematical symbols.
• hang: the baseline of “hanging” scripts, such as certain scripts of India (Devanagari, for
instance), Tibetan, and also ancient Hebrew.
• ideo and idtp: the lower and upper baselines of the ideal ideographic square.
• icfb and icft: the lower and upper baselines for ideographic alignment, also known as
ICF parameters (for “ideographic character face”).
The last four deserve some explanation: on the one hand, there is the ideal ideographic square,
one em wide; on the other hand, there is the square for ideographic alignment, a square concentric with the previous one but smaller. This square is used for aligning Japanese glyphs.
This property of glyphs recalls the opbd table of AAT (§D.11.7) or the opbd feature of OpenType (§D.10.2.1), where the concern is with the edges of the glyph when it is aligned at the
beginning of a line. Here is an example of these two types of squares:

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
ideal ideographic square
square for ideographic alignment (ICF)
alphabetic baseline
The reader should not be surprised that we are speaking here of “squares”, whereas when
presenting the description of the types of baseline we spoke only of lower and upper lines.
Let us not forget that both horizontal and vertical baselines are defined in the BASE table. In
the definitions above, lower and upper become left and right when we set type vertically. By
combining the lines icfb and icft (or ideo and idtp) for the two directions, we do indeed
obtain a rectangle. And the age-old philosophy of the Chinese script requires this rectangle
to be a square, symbol of balance and perfection.
Finally, let us note that associating the lower baseline with the left baseline (and the opposite
for the upper baseline) when switching from horizontal to vertical typesetting is a good choice
for the ideographic languages, in which vertical lines are written from right to left, but a poor
choice for Mongolian, in which vertical lines are written from left to right—and for which the
equivalent of the lower baseline would rather be the right baseline.
D.9.3
The GPOS Table
The GPOS table manages the positioning of the glyphs. Its applications are numerous: they
range from simple kerning to the positioning of diacritical marks, the positioning of diacritical marks over other diacritical marks, typesetting at an angle in Urdu, and many others.
This table shares with the others its schema for organizing data: we start with a script (script)
and possibly a language; then we select one or more features (features), and the features lead
us to a number of lookups. These lookups are of nine types, and we shall study them by starting
with the simplest ones.
D.9.3.1
Scripts and features
The sample GPOS table that we show here is from the font Palatino Linotype. Note that this
table is enormous: 9,560 lines of XML code.
The table begins with a Version element and the list of scripts offered (ScriptRecord), which
is contained within the element ScriptList. Let us take the code for the Latin script:
&lt;GPOS&gt;
&lt;Version value="1.0"/&gt;
&lt;ScriptList&gt;
&lt;ScriptRecord index="2"&gt;
&lt;ScriptTag value="latn"/&gt;
&lt;Script&gt;
&lt;DefaultLangSys&gt;
&lt;ReqFeatureIndex value="65535"/&gt;
```

```text
D.9. The OpenType Advanced Typographic Tables
<!-- FeatureCount=3 -->
&lt;FeatureIndex index="0" value="3"/&gt;
&lt;FeatureIndex index="1" value="4"/&gt;
&lt;FeatureIndex index="2" value="0"/&gt;
&lt;/DefaultLangSys&gt;
<!-- LangSysCount=4 -->
&lt;LangSysRecord index="0"&gt;
&lt;LangSysTag value="DEU "/&gt;
&lt;LangSys&gt;
&lt;ReqFeatureIndex value="65535"/&gt;
<!-- FeatureCount=3 -->
&lt;FeatureIndex index="0" value="3"/&gt;
&lt;FeatureIndex index="1" value="4"/&gt;
&lt;FeatureIndex index="2" value="0"/&gt;
&lt;/LangSys&gt;
&lt;/LangSysRecord&gt;
&lt;LangSysRecord index="1"&gt;
&lt;LangSysTag value="ROM "/&gt;
&lt;LangSys&gt;
&lt;ReqFeatureIndex value="65535"/&gt;
<!-- FeatureCount=3 -->
&lt;FeatureIndex index="0" value="3"/&gt;
&lt;FeatureIndex index="1" value="4"/&gt;
&lt;FeatureIndex index="2" value="0"/&gt;
&lt;/LangSys&gt;
&lt;/LangSysRecord&gt;
&lt;LangSysRecord index="2"&gt;
&lt;LangSysTag value="TRK "/&gt;
&lt;LangSys&gt;
&lt;ReqFeatureIndex value="65535"/&gt;
<!-- FeatureCount=3 -->
&lt;FeatureIndex index="0" value="3"/&gt;
&lt;FeatureIndex index="1" value="4"/&gt;
&lt;FeatureIndex index="2" value="0"/&gt;
&lt;/LangSys&gt;
&lt;/LangSysRecord&gt;
&lt;LangSysRecord index="3"&gt;
&lt;LangSysTag value="VIT "/&gt;
&lt;LangSys&gt;
&lt;ReqFeatureIndex value="65535"/&gt;
<!-- FeatureCount=4 -->
&lt;FeatureIndex index="0" value="3"/&gt;
&lt;FeatureIndex index="1" value="4"/&gt;
&lt;FeatureIndex index="2" value="5"/&gt;
&lt;FeatureIndex index="3" value="0"/&gt;
&lt;/LangSys&gt;
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
&lt;/LangSysRecord&gt;
&lt;/Script&gt;
&lt;/ScriptRecord&gt;
Under ScriptRecord we have a ScriptTag, which contains the name of the script in question
(here, latn), and a Script element containing data on the languages that share this script.
In our example, we find one DefaultLangSys element for the “default language”—i.e., the
behavior of the font when the language is not specified—and four LangSysRecord elements
for four languages written in the Latin alphabet: DEU (German), ROM (Romanian), TRK (Turkish), VIT (Vietnamese).
The difference between DefaultLangSys and LangSysRecord is that the latter contains a
LangSysTag element with information on the name of the language and a LangSys element
that contains the features, whereas DefaultLangSys contains only features.
Now we come to the features attached to each language. There is one that is privileged:
ReqFeatureIndex, the required feature. It is the only feature that is enabled automatically,
without interaction with the user. It must be a feature inextricably tied to the language in
question. If there is no such feature, we set value equal to 0xffff.
Next comes a list of features, or rather pointers to descriptions of features, which appears in
another branch of the XML document, under the element FeatureList. It is the value attribute that gives the identifier of the feature in question. In our example, for instance, when
we set type in the default language, in German, in Romanian, or in Turkish, we have access
to the features 3, 4, and 0. We shall see below that these are the features subs (subscripts),
sinf (scientific subscripts), and kern (kerning). In addition, when we set type in Vietnamese,
we have access to feature 5, mark (positioning of diacritical marks).
Now let us continue with the code for the features:
&lt;FeatureList&gt;
<!-- FeatureCount=6 -->
&lt;FeatureRecord index="0"&gt;
&lt;FeatureTag value="kern"/&gt;
&lt;Feature&gt;
<!-- LookupCount=1 -->
&lt;LookupListIndex index="0" value="0"/&gt;
&lt;/Feature&gt;
&lt;/FeatureRecord&gt;
&lt;FeatureRecord index="1"&gt;
&lt;FeatureTag value="kern"/&gt;
&lt;Feature&gt;
<!-- LookupCount=1 -->
&lt;LookupListIndex index="0" value="1"/&gt;
&lt;/Feature&gt;
&lt;/FeatureRecord&gt;
&lt;FeatureRecord index="2"&gt;
&lt;FeatureTag value="kern"/&gt;
```

```text
D.9. The OpenType Advanced Typographic Tables
&lt;Feature&gt;
<!-- LookupCount=1 -->
&lt;LookupListIndex index="0" value="2"/&gt;
&lt;/Feature&gt;
&lt;/FeatureRecord&gt;
&lt;FeatureRecord index="3"&gt;
&lt;FeatureTag value="subs"/&gt;
&lt;Feature&gt;
<!-- LookupCount=1 -->
&lt;LookupListIndex index="0" value="3"/&gt;
&lt;/Feature&gt;
&lt;/FeatureRecord&gt;
&lt;FeatureRecord index="4"&gt;
&lt;FeatureTag value="sinf"/&gt;
&lt;Feature&gt;
<!-- LookupCount=1 -->
&lt;LookupListIndex index="0" value="4"/&gt;
&lt;/Feature&gt;
&lt;/FeatureRecord&gt;
&lt;FeatureRecord index="5"&gt;
&lt;FeatureTag value="mark"/&gt;
&lt;Feature&gt;
<!-- LookupCount=4 -->
&lt;LookupListIndex index="0" value="5"/&gt;
&lt;LookupListIndex index="1" value="6"/&gt;
&lt;LookupListIndex index="2" value="7"/&gt;
&lt;LookupListIndex index="3" value="8"/&gt;
&lt;/Feature&gt;
&lt;/FeatureRecord&gt;
&lt;/FeatureList&gt;
This branch of the document contains the lookups associated with each feature. Each FeatureRecord contains, first of all, a name (FeatureTag), and then a Feature element that contains
value pointers to lookups called Lookup. These lookups are found in another branch of the
document, the one that appears under LookupList.
The other 98.6 percent of the table is found under LookupList: the list of lookups. This element
contains the well-known Lookups to which the features point. Each Lookup contains, first, a
LookupType (the type of the lookup; there are nine in the GPOS table), and then a LookupFlag
(see §D.9.1.1).
Here is the beginning of a LookupList:
&lt;LookupList&gt;
<!-- LookupCount=9 -->
&lt;Lookup index="0"&gt;
&lt;LookupType value="2"/&gt;
&lt;LookupFlag value="8"/&gt;
```

Appendix D : The TrueType, OpenType, and AAT Font Formats
The lookup in question is thus of type 2, and the flag LookupFlag indicates that we should
disregard combining marks.
Below we shall examine the types of lookups one by one.
D.9.3.2
Lookup type 1: positioning of a single glyph
This type involves positioning a single glyph, as, for example, when creating a superscript or
a subscript, centering parentheses better when setting type in small capitals, centering mathematical signs better when using old-style figures, etc. Here is an example of its use:
We see the word “BACH” with regular parentheses, the same word in small capitals with the
default parentheses, and, finally, small capitals with the parentheses corrected. It is incredible
how much better the result became when we simply moved the parentheses downward a few
points.
Here is the code for moving the parentheses:
&lt;Lookup index="0"&gt;
&lt;LookupType value="1"/&gt;
&lt;LookupFlag value="0"/&gt;
<!-- SubTableCount=1 -->
&lt;SinglePos index="0" Format="1"&gt;
&lt;Coverage Format="1"&gt;
&lt;Glyph value="parenleft"/&gt;
&lt;Glyph value="parenright"/&gt;
&lt;/Coverage&gt;
&lt;ValueFormat value="2"/&gt;
&lt;Value YPlacement="-"/&gt;
&lt;/SinglePos&gt;
&lt;/Lookup&gt;
The SinglePos element corresponds to the type of lookup that we are examining: the positioning of a single glyph. It contains a coverage table, which in turn contains the glyphs for
the parentheses. Next, it contains an element for a formatted value. This is a peculiarity of the
GPOS table: to represent a positioning value, we use the Value element, which can take eight
attributes:
• XPlacement, for horizontal positioning of the glyph
• YPlacement, for vertical positioning of the glyph
• XAdvance, for a modification to the glyph’s horizontal set-width

D.9. The OpenType Advanced Typographic Tables
• YAdvance, for a modification to the glyph’s vertical set-width
• XPlaDevice, a pointer to a device table, for horizontal positioning of the glyph
• YPlaDevice, a pointer to a device table, for vertical positioning of the glyph
• XAdvDevice, a pointer to a device table, for a modification to the glyph’s horizontal setwidth
• YAdvDevice, a pointer to a device table, for a modification to the glyph’s vertical set-width
Moreover, to make it easier for the processor to read these attributes, we include, before the
first Value, a ValueFormat element. The value attribute of this element contains a series of
eight flags that indicate which attributes will subsequently be used.
D.9.3.3
Lookup type 2: positioning of a pair of glyphs
The positioning of a pair of glyphs is not simply a sophisticated way to talk about kerning. This
operation goes much further, as each of the two glyphs can be moved separately, and in any
direction. Here is one example of this type of table:
&lt;Lookup index="2"&gt;
&lt;LookupType value="2"/&gt;
&lt;LookupFlag value="8"/&gt;
<!-- SubTableCount=1 -->
&lt;PairPos index="0" Format="1"&gt;
&lt;Coverage Format="1"&gt;
&lt;Glyph value="A"/&gt;
&lt;/Coverage&gt;
&lt;ValueFormat1 value="4"/&gt;
&lt;ValueFormat2 value="0"/&gt;
<!-- PairSetCount=2 -->
&lt;PairSet index="0"&gt;
<!-- PairValueCount=1 -->
&lt;PairValueRecord index="0"&gt;
&lt;SecondGlyph value="T"/&gt;
&lt;Value1 XAdvance="-"/&gt;
&lt;/PairValueRecord&gt;
&lt;/PairSet&gt;
&lt;PairSet index="1"&gt;
<!-- PairValueCount=0 -->
&lt;/PairSet&gt;
&lt;/PairPos&gt;
&lt;/Lookup&gt;
We see here that the type of the lookup is indeed 2. This lookup is represented by a PairPos
element, for which there are two distinct formats. The first (as in the example) uses a coverage
table for the first glyph and then one PairSet element for each element in the coverage table.

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
In each PairSet element, we find a PairValue element for each kerning pair with the same
first glyph. Each PairValue contains, first, a Glyph, which gives us the second glyph, and usually two elements Value1 and Value2, which are formatted values—the positionings of each of
the two glyphs in the kerning pair. Needless to say, Value2 usually is lacking, since we usually
change the spacing of the first glyph rather than moving the second.
The second format for PairPos uses glyph classes. Here is an example of one such element:
&lt;Lookup index="3"&gt;
&lt;LookupType value="2"/&gt;
&lt;LookupFlag value="8"/&gt;
<!-- SubTableCount=1 -->
&lt;PairPos index="0" Format="2"&gt;
&lt;Coverage Format="1"&gt;
&lt;Glyph value="A"/&gt;
&lt;Glyph value="Aacute"/&gt;
&lt;/Coverage&gt;
&lt;ValueFormat1 value="68"/&gt;
&lt;ValueFormat2 value="0"/&gt;
&lt;ClassDef1 Format="2"&gt;
&lt;ClassDef glyph="A" class="1"/&gt;
&lt;ClassDef glyph="Aacute" class="1"/&gt;
&lt;/ClassDef1&gt;
&lt;ClassDef2 Format="2"&gt;
&lt;ClassDef glyph="T" class="1"/&gt;
&lt;/ClassDef2&gt;
<!-- Class1Count=1 -->
<!-- Class2Count=1 -->
&lt;Class1Record index="0"&gt;
&lt;Class2Record index="0"&gt;
&lt;Value1 XAdvance="-"&gt;
&lt;XAdvDevice&gt;
&lt;StartSize value="15"/&gt;
&lt;EndSize value="24"/&gt;
&lt;DeltaFormat value="1"/&gt;
&lt;DeltaValue value="[-, 0, 0, 0, 0, 0, 0, 0, -, -]"/&gt;
&lt;/XAdvDevice&gt;
&lt;/Value1&gt;
&lt;/Class2Record&gt;
&lt;/Class1Record&gt;
&lt;/PairPos&gt;
&lt;/Lookup&gt;
In the example, we see the lookup type (LookupType), the series of flags (LookupFlag; see
§D.9.1.1), the coverage table (Coverage), and the formatted values (ValueFormat1 and ValueFormat2), which did not exist in Format 1. But rather than addressing the glyph pairs right off
the bat, we first define glyph classes: for instance, the ClassDef1 element contains a ClassDef
```

```text
D.9. The OpenType Advanced Typographic Tables
for each initial glyph in the pair; ClassDef2 contains the glyphs that appear second. Each
ClassDef contains the glyph name and the class, in the form of attributes.
Once the classes have been defined, there are some kerning pairs, which are classified in the
following manner: the element Class1Record contains Class2Record subelements for all the
pairs whose first glyph is in a class given by its index attribute. Class2Record contains a formatted value.
In the example above, we first see a pair between classes 1 and 0. Class 1 is that of the letter ‘A’
and similar glyphs (‘Á’, for example, is in the same class). Class 0 is the class for all the glyphs
that do not have a ClassDef (not surprisingly, that includes thousands of glyphs). The value
of the positioning is 0, which is not surprising, as if we wished to kern the letter ‘A’ with every
glyph, we would be better offchanging its width; that would take less time to calculate. Thus
it is a phony Class2Record.
What follows is more useful: a kerning pair between the classes 1 and 4. Class 1 is still the
class for the letter ‘A’; Class 4 is for the letter ‘V’ and similar glyphs. The amount of kerning
requested comes from a device table: the exact value is −195 TrueType units, but there are also
10 δ values, which cover the sizes between 15 and 24 pixels per em. The corrections concern
the extreme values: at 15, 23, and 24 pixels per em, one additional pixel of kerning is needed.
At and above 25 pixels per em, we leave the decision to the processor, which will transform
the 195 TrueType units into pixels and round them.
D.9.3.4
Lookup type 3: cursive attachment
letters, and what a child can do at school, a computer should also be able to do. But how can
we be sure that the stroke that emerges from the letter ‘s’, for example, and the one that leads
into the letter ‘c’ will actually coincide? Up to now, font designers needed damn good organization to make all the letters join up correctly. Lookup type 3 turns this task into child’s play.
Here is a table of this type:
&lt;Lookup index="4"&gt;
&lt;LookupType value="3"/&gt;
&lt;LookupFlag value="8"/&gt;
<!-- SubTableCount=1 -->
&lt;CursivePos index="0" Format="1"&gt;
&lt;Coverage Format="1"&gt;
&lt;Glyph value="a"/&gt;
&lt;Glyph value="b"/&gt;
&lt;Glyph value="c"/&gt;
&lt;/Coverage&gt;
<!-- EntryExitCount=1 -->
&lt;EntryExitRecord index="0"&gt;
&lt;EntryAnchor Format="1"&gt;
&lt;XCoordinate value="1425"/&gt;
&lt;YCoordinate value="654"/&gt;
```

Appendix D : The TrueType, OpenType, and AAT Font Formats
&lt;/EntryAnchor&gt;
&lt;ExitAnchor Format="2"&gt;
&lt;XCoordinate value="1425"/&gt;
&lt;YCoordinate value="654"/&gt;
&lt;AnchorPoint value="34"/&gt;
&lt;/ExitAnchor&gt;
&lt;/EntryExitRecord&gt;
&lt;/CursivePos&gt;
&lt;/Lookup&gt;
Each glyph has an entry anchor and an exit anchor. The processor will match the exit anchor of
one glyph up with the entry anchor of the following glyph. Provided that all these anchors
are at the same height, this method drastically simplifies the development of a cursive font.
Let us look more closely at the sample code. After the usual LookupType and LookupFlag, we
have an element CursivePos. This element contains, first, a coverage table containing glyphs,
and then an EntryExitRecord element for each glyph. Each of these elements contains the
data for the glyph’s entry anchors (EntryAnchor) and exit anchors (ExitAnchor). There are
three ways to define these anchors:
• Format 1: we provide merely the point’s x-coordinate (XCoordinate) and y-coordinate
(YCoordinate).
• Format 2: like Format 1, but a point on the glyph’s contour is also supplied. Coordinates are sufficient for preliminary calculations, but when the time comes to render the
glyphs in question, the point will be much more precise, because any instructions that
are present could move it in extremis.
• Format 3: even more powerful than Format 2. We still supply precise coordinates, but we
also add device tables for each of the point’s coordinates. Thus the last word will no longer
go to the TrueType instructions but to the designer, who determines the exact number
of pixels at each size.
Let us recall the primordial role played by the first bit in the LookupFlag in this very special
lookup: if it is enabled, then for each “word” (the software decides what constitutes a “word”),
we first set all the glyphs by matching up their entry and exit anchors, and then we move the
entire word so that the last glyph will lie on the baseline. If the bit is disabled, the first glyph
will be placed on the baseline, as usual, and the others will deviate from it according to the
angle between the entry and exit anchors. We have given two examples of the use of this bit
in Figure D-4.
D.9.3.5
Lookup type 4: diacritical marks
In Europe, èš¯p˘eçîåł´lÿ í˙f ôñé i˛6 ä ˘g8˛eâ¸t àP ˇm˜i8ër¸ ˝o˙f Qîã5ˇrï¸t˘i˙c ˛a´l `m%8k¸ˆs, like the author, one often
complains that Americans do not pay enough attention to the needs of our languages, with
their accents and other oddities. That era has been definitively reversed: thanks to Type 4
lookups, we can place any diacritical mark on any letter. And not in just any way: we can indicate this type of positioning with a great deal of precision.

```text
D.9. The OpenType Advanced Typographic Tables
➀
➀
➁
➁
Figure D-4: Two examples of the use of the lookup flag for cursive attachment. First example: in the Urdu
script, groups of connected letters (written from right to left, don’t forget!) must end on the baseline. Case 1:
bit enabled, correct typesetting; case 2: bit disabled, poor typesetting (going offin every direction).
Second example: a figurative use of typeset text: letters “sent flying”. Case 1: bit disabled, correct typesetting;
case 2: bit enabled, poor typesetting (the letters seem to be climbing out of the basement; the image is
spoiled).
The principle is simple and powerful: each diacritical mark has a point of attachment; the
diacritical marks are arranged into several classes according to their behavior; each “base”
glyph has a point of attachment for each class of diacritical marks. We select a base glyph and
a diacritical mark, and the processor bends over backwards to make us happy by matching
the correct point of attachment on the base glyph with that of the diacritical mark.
Here is an example of one such table:
&lt;Lookup index="5"&gt;
&lt;LookupType value="4"/&gt;
&lt;LookupFlag value="0"/&gt;
<!-- SubTableCount=1 -->
&lt;MarkBasePos index="0" Format="1"&gt;
&lt;MarkCoverage Format="1"&gt;
&lt;Glyph value="dotaccent"/&gt;
&lt;/MarkCoverage&gt;
&lt;BaseCoverage Format="1"&gt;
&lt;Glyph value="A"/&gt;
&lt;Glyph value="E"/&gt;
&lt;/BaseCoverage&gt;
<!-- ClassCount=2 -->
&lt;MarkArray&gt;
<!-- MarkCount=1 -->
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
&lt;MarkRecord index="0"&gt;
&lt;Class value="1"/&gt;
&lt;MarkAnchor Format="2"&gt;
&lt;XCoordinate value="0"/&gt;
&lt;YCoordinate value="-"/&gt;
&lt;AnchorPoint value="12"/&gt;
&lt;/MarkAnchor&gt;
&lt;/MarkRecord&gt;
&lt;/MarkArray&gt;
&lt;BaseArray&gt;
<!-- BaseCount=1 -->
&lt;BaseRecord index="0"&gt;
&lt;BaseAnchor index="0" Format="2"&gt;
&lt;XCoordinate value="803"/&gt;
&lt;YCoordinate value="1487"/&gt;
&lt;AnchorPoint value="52"/&gt;
&lt;/BaseAnchor&gt;
&lt;BaseAnchor index="1" Format="2"&gt;
&lt;XCoordinate value="780"/&gt;
&lt;YCoordinate value="-"/&gt;
&lt;AnchorPoint value="53"/&gt;
&lt;/BaseAnchor&gt;
&lt;/BaseRecord&gt;
&lt;/BaseArray&gt;
&lt;/MarkBasePos&gt;
&lt;/Lookup&gt;
After the usual LookupType and LookupFlag, we find the element MarkBasePos. This element
has a very simple structure: first come some coverage tables for the diacritical marks and the
base glyphs; then come the coordinates of the points of attachment for the diacritical marks;
finally, there are similar coordinates for the base glyphs.
The coverage tables are exactly the same as the ones that we have already seen; the only
difference is that here, since we have two types of tables, we have named the corresponding
elements MarkCoverage (mark for “diacritical mark”) and BaseCoverage.
In the global element MarkArray that follows, there is a MarkRecord subelement for each
glyph in MarkCoverage. Each MarkRecord corresponds to a diacritical mark. The first piece
of data that it contains is the diacritical mark’s class, obtained through the Class element.
The coordinates of the point of attachment of a diacritical mark are given in the MarkAnchor
element, which immediately follows the Class element. MarkAnchor is of the same type as the
EntryAnchor of the preceding type of lookup; thus there are three different formats: either
we give only the precise coordinates (format 1) or we also add a point on the glyph’s contour
(format 2) or we even add device tables for each of the point’s two coordinates (format 3). In
the example, the MarkAnchor is of format 2.
Finally, in BaseArray, there are BaseRecord elements, which correspond to the base glyphs
as these are listed in BaseCoverage. Each BaseRecord contains a BaseAnchor for each class of
diacritical marks.
```

```text
D.9. The OpenType Advanced Typographic Tables
In the example, for instance, there are two classes of diacritical marks: class 0 corresponds to
accents placed above the letter (the acute accent acutecomb, the grave accent gravecomb, etc.),
and class 1 is for those placed beneath the letter (the underdot dotbelowcomb). Thus there is
the same number of BaseAnchor elements in each BaseRecord, corresponding to the points
of attachment of each class of diacritical marks. The class is given by the attribute index. The
position of the point of attachment BaseAnchor is given in the same way as that of MarkAnchor: once again, there are three formats (coordinates alone, a point on the contour, device
tables).
We see in the example that the points of attachment for the letter ‘A’ are (803,1487) for upper
accents and (780,−60) for lower accents. We can see that, contrary to the visual impression
that is left, the axes for upper and lower accents do not coincide, since their x-coordinates
differ by 23 TrueType units. The difference is doubtless attributable to the fact that the letter’s
design is not strictly symmetrical.
It can be seen that this table can be used to combine diacritical marks and base glyphs arbitrarily. All that is necessary is to supply the corresponding points of attachment for each
glyph and create multiple glyphs for each diacritical mark in case the diacritical mark should
have several possible behaviors. For example, the diacritical marks “dot above a letter” and
“dot below a letter” must come from different glyphs, even if the contour of the dot is the
same and we could have simply moved the dot in order to switch from one diacritical mark
to the other. The reason is connected to the fact that each diacritical mark belongs to only
one class and can be attached to only one point of attachment on the base glyph.
D.9.3.6
Lookup type 6: multiple diacritical marks
Whether in Vietnamese, in the International Phonetic Alphabet, or in Greek with the lengths
of the syllables marked, we sometimes need multiple diacritical marks. For instance, in the
following line of Vietnamese text:13
there are no fewer than three letters with double accents: the letter ‘e’ with the circumflex
and acute accents, the letter ‘a’ with the breve and the acute accent, and the letter ‘a’ with the
circumflex and acute accents. That is due to the fact that, on the one hand, the letters ‘â’, ‘˘a’, ‘ê’,
and ‘ô’ are considered basic letters of the alphabet and, on the other hand, the tone of every
vowel has to be indicated with a diacritical mark. The four vowels that already bear diacritical
marks thus end up with two diacritics.
We could, of course, design these double accents for Vietnamese and thus avoid the problem
of multiple diacritical marks. But for purposes such as the International Phonetic Alphabet,
in which there is a plethora of diacritical marks that can appear together on the same base
glyph, we simply cannot cover every possibility. Furthermore, any software that claims to be
Unicode-compatible must be able to set any characters followed by any series of combining
characters. Thus there is a genuine problem, and lookup type 6 is less useless than it might
have seemed at first glance.
13 Revelation 1:7: “Behold, He cometh with clouds; and every eye shall see Him”, set in Stempel Schneidler,
from the Neufville Digital Foundry, adapted for Vietnamese by the author.
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
From a technical point of view, we find the same structure as for lookup type 4. The difference
is that here, instead of having tags that begin with Mark (diacritical mark) and Base (base
glyph), there are tags that begin with Mark1 (diacritical mark) and Mark2 (diacritical mark that
plays the role of base glyph). Here, for example, is the TTX code for the lookup that produces
the double accents of Vietnamese:
&lt;Lookup index="6"&gt;
&lt;LookupType value="6"/&gt;
&lt;LookupFlag value="0"/&gt;
<!-- SubTableCount=1 -->
&lt;MarkMarkPos index="0" Format="1"&gt;
&lt;Mark1Coverage Format="1"&gt;
&lt;Glyph value="grave"/&gt;
&lt;Glyph value="acute"/&gt;
&lt;Glyph value="tilde"/&gt;
&lt;Glyph value="caron"/&gt;
&lt;Glyph value="dotaccent"/&gt;
&lt;/Mark1Coverage&gt;
&lt;Mark2Coverage Format="1"&gt;
&lt;Glyph value="circumflex"/&gt;
&lt;Glyph value="breve"/&gt;
&lt;/Mark2Coverage&gt;
<!-- ClassCount=1 -->
&lt;Mark1Array&gt;
<!-- MarkCount=1 -->
&lt;MarkRecord index="0"&gt;
&lt;Class value="1"/&gt;
&lt;MarkAnchor Format="1"&gt;
&lt;XCoordinate value="0"/&gt;
&lt;YCoordinate value="170"/&gt;
&lt;/MarkAnchor&gt;
&lt;/MarkRecord&gt;
&lt;/Mark1Array&gt;
&lt;Mark2Array&gt;
<!-- Mark2Count=1 -->
&lt;Mark2Record index="0"&gt;
&lt;Mark2Anchor index="0" Format="1"&gt;
&lt;XCoordinate value="0"/&gt;
&lt;YCoordinate value="-"/&gt;
&lt;/Mark2Anchor&gt;
&lt;/Mark2Record&gt;
&lt;/Mark2Array&gt;
&lt;/MarkMarkPos&gt;
&lt;/Lookup&gt;
The Mark1Record elements thus contain the points of attachment for the “secondary” accents
and a class value for each. The Mark2Record elements contain the different points of attach-
```

```text
D.9. The OpenType Advanced Typographic Tables
ment for the “base” accents, according to the class of the “secondary” accent (given by the
index attribute).
D.9.3.7
Lookup type 5: diacritical marks on ligatures
“The aesthetic quality of this font is undeniable, but”—but we need some accents. The font
used here is Prestige, by the foundry Présence Typo, located in Hautes-Alpes (France). This
font contains a great many ligatures, all of them quite beautiful. The only problem is that no
accents are provided. Yet the Lexique des règles en usage à l’Imprimerie nationale [48] does indeed
call for accents in French. Doubtless the accents were omitted because the composition of
ligatures and accents would have necessitated thousands of additional glyphs. That is where
OpenType comes to the rescue.
Table 5 is devoted to diacritical marks placed on ligatures. How can we put an acute accent
over the ligature ‘T’ in the French word “ESTHÉTIQUE”? or an acute accent over the ligature ‘E’ in the word “INDÉNIABLE”?
Technically, this type of lookup also draws its inspiration from Type 4, but here the tags
beginning with Base are replaced with Ligature tags. In addition, there is a level below LigatureArray in the hierarchy: components of the ligature. Thus there is no LigatureRecord but
rather a LigatureAttach containing ComponentRecords that correspond to the components.
Here is an example of one such subtable:
&lt;Lookup index="7"&gt;
&lt;LookupType value="5"/&gt;
&lt;LookupFlag value="0"/&gt;
<!-- SubTableCount=1 -->
&lt;MarkLigPos index="0" Format="1"&gt;
&lt;MarkCoverage Format="1"&gt;
&lt;Glyph value="dotaccent"/&gt;
&lt;Glyph value="grave"/&gt;
&lt;Glyph value="acute"/&gt;
&lt;Glyph value="tilde"/&gt;
&lt;Glyph value="caron"/&gt;
&lt;/MarkCoverage&gt;
&lt;LigatureCoverage Format="1"&gt;
&lt;Glyph value="X"/&gt;
&lt;Glyph value="Y"/&gt;
&lt;/LigatureCoverage&gt;
<!-- ClassCount=2 -->
&lt;MarkArray&gt;
<!-- MarkCount=1 -->
&lt;MarkRecord index="0"&gt;
&lt;Class value="1"/&gt;
&lt;MarkAnchor Format="2"&gt;
&lt;XCoordinate value="0"/&gt;
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
&lt;YCoordinate value="-"/&gt;
&lt;AnchorPoint value="12"/&gt;
&lt;/MarkAnchor&gt;
&lt;/MarkRecord&gt;
&lt;/MarkArray&gt;
&lt;LigatureArray&gt;
<!-- LigatureCount=1 -->
&lt;LigatureAttach index="0"&gt;
<!-- ComponentCount=1 -->
&lt;ComponentRecord index="0"&gt;
&lt;LigatureAnchor index="0" Format="2"&gt;
&lt;XCoordinate value="803"/&gt;
&lt;YCoordinate value="1487"/&gt;
&lt;AnchorPoint value="52"/&gt;
&lt;/LigatureAnchor&gt;
&lt;LigatureAnchor index="1" Format="2"&gt;
&lt;XCoordinate value="780"/&gt;
&lt;YCoordinate value="-"/&gt;
&lt;AnchorPoint value="53"/&gt;
&lt;/LigatureAnchor&gt;
&lt;/ComponentRecord&gt;
&lt;/LigatureAttach&gt;
&lt;/LigatureArray&gt;
&lt;/MarkLigPos&gt;
&lt;/Lookup&gt;
Thus we divide the ligature into several hypothetical components. In each of these components, we insert one point of attachment for every class of diacritical marks. These points
of attachment are LigatureAnchors and, like other types of lookups in the GPOS table, they
can be represented in three different ways (format 0: the coordinates only; format 1: the coordinates and a point on the contour; format 2: the coordinates and two device tables for
them). The element ComponentRecord, which contains the poins of attachment, corresponds
to a component of the ligature. It is contained in a LigatureAttach, which corresponds to a
ligature.
Note that the OpenType font merely supplies to the typesetting software the data necessary
for the positioning of the diacritical mark; the software must be able to detect the presence
of a ligature even when accents are present, which is no easy task. For instance, if the software
knows that the characters latin capital letter t, latin capital letter h, and latin capital letter e automatically form a ligature, it must also be aware that an ‘E’ with an acute
accent, 0x00C9 latin capital letter e acute can be decomposed into latin capital letter e
followed by 0x0301 combining acute accent (oxia, tonos) and that a ligature should still
be formed, through the use of the mechanism for accenting ligatures in the GPOS table.
To conclude this section, one small detail about an unforeseen problem: given that the ‘E’ in
the ligature ‘E’ is reversed, the acute accent placed on this letter should be reversed as well.
But the reversed acute accent has a name: it is called a grave accent. Positioning should therefore be followed by a substitution, as is done in the GSUB table.
```

```text
D.9. The OpenType Advanced Typographic Tables
D.9.3.8
Lookup type 7: contextual positioning
The two types of lookups that follow are, in a sense, “virtual” lookups, since they direct the
processor to other lookups. Here is their purpose: they search for a certain set of strings of
glyphs (called context strings), and when one of these strings is found, a given lookup from
types 1 to 6 is applied to each glyph in the string. The role of the lookup for contextual positioning is therefore to recognize the model string of glyphs and indicate which lookup must
be applied to each glyph in the string.
The overall procedure is as follows: As we have already seen, the user selects a script and a
language; the operating system then offers some features. The user chooses one of the features, and that action triggers a series of lookups. Each lookup in turn contains a series of
positioning rules: context strings and numbers of the lookups to apply to each of their glyph.
Warning: while all the lookups for a given feature are executed, only the first matching context string in the lookup will cause the positioning of a glyph.
For example, to illustrate contextual kerning, let us revisit the example that we gave in the
kern table, Format 1 (§D.8.4.2): the problematic string “S.A.V.”, in which we wish to kern the
period and the ‘V’. Here is how we shall present the problem: we select ‘A.V’ (i.e., A, period,
and V) as the context string, and we request kerning of −400 units between the glyphs period
and V. Here is the code for the “virtual” lookup:
&lt;Lookup index="8"&gt;
&lt;LookupType value="7"/&gt;
&lt;LookupFlag value="0"/&gt;
<!-- SubTableCount=1 -->
&lt;ContextPos index="0" Format="1"&gt;
&lt;Coverage Format="1"&gt;
&lt;Glyph value="A"/&gt;
&lt;/Coverage&gt;
<!-- PosRuleSetCount=1 -->
&lt;PosRuleSet index="0"&gt;
<!-- PosRuleCount=1 -->
&lt;PosRule index="0"&gt;
<!-- GlyphCount=3 -->
<!-- PosCount=1 -->
&lt;Input index="0" value="period"/&gt;
&lt;Input index="1" value="V"/&gt;
&lt;PosLookupRecord index="0"&gt;
&lt;SequenceIndex value="1"/&gt;
&lt;LookupListIndex value="5"/&gt;
&lt;/PosLookupRecord&gt;
&lt;/PosRule&gt;
&lt;/PosRuleSet&gt;
&lt;/ContextPos&gt;
&lt;/Lookup&gt;
This code first creates a coverage table for the first glyph in the context string: the one that concerns us is A. Next, there is one PosRuleSet for each glyph in the coverage table. A PosRuleSet
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
contains all the context strings that begin with the corresponding letter in the coverage table.
Each context string corresponds to a PosRule element.
This element contains Input elements corresponding to the other glyphs in the string of
glyphs. Finally, we have one PosLookupRecord for each lookup that is to be applied. The
subelements SequenceIndex and LookupIndex indicate the index of the glyph to which the
lookup will be applied, together with the number of that lookup: in our case, we shall apply
lookup number 5 to glyph 1 (i.e., the period, since counting starts at 0).
Which lookup will number 5 be? Easy: it is a lookup for single glyph positioning (see
§D.9.3.2) in which we shall reduce the period’s width by 400 TrueType units. Here it is:
&lt;Lookup index="5"&gt;
&lt;LookupType value="1"/&gt;
&lt;LookupFlag value="0"/&gt;
&lt;SinglePos index="0" Format="1"&gt;
&lt;Coverage Format="1"&gt;
&lt;Glyph value="period"/&gt;
&lt;/Coverage&gt;
&lt;ValueFormat value="4"/&gt;
&lt;Value index="0" XAdvance="-"/&gt;
&lt;/SinglePos&gt;
&lt;/Lookup&gt;
We have just described Format 1 of the Type 7 lookup. There are two additional formats:
Format 2 is richer, since it uses glyph classes rather than individual glyphs. Thus our context
string becomes a “meta-string”. Not only ‘A.V’ but also ‘Á.V’ and ‘À.V’ and ‘Â.V’, and even
‘A.W’ and perhaps ‘A.T’, ‘A.Y’, etc. We need only declare that the glyphs ‘A’, ‘Á’, ‘À’, and so on
are part of the same class; likewise for ‘V’, ‘W’, ‘T’, ‘Y’, etc.
The code for this lookup is slightly more elaborate, since after Coverage we insert a table of
class definitions that is in every way identical to that of lookup 2, format 2 (see §D.9.3.3):
&lt;Lookup index="9"&gt;
&lt;LookupType value="7"/&gt;
&lt;LookupFlag value="0"/&gt;
<!-- SubTableCount=1 -->
&lt;ContextPos index="0" Format="2"&gt;
&lt;Coverage Format="1"&gt;
&lt;Glyph value="A"/&gt;
&lt;Glyph value="Agrave"/&gt;
&lt;Glyph value="Aacute"/&gt;
&lt;/Coverage&gt;
&lt;ClassDef Format="2"&gt;
&lt;ClassDef glyph="A" class="1"/&gt;
&lt;ClassDef glyph="Aacute" class="1"/&gt;
&lt;ClassDef glyph="Agrave" class="1"/&gt;
&lt;ClassDef glyph="V" class="3"/&gt;
```

```text
D.9. The OpenType Advanced Typographic Tables
&lt;ClassDef glyph="W" class="3"/&gt;
&lt;ClassDef glyph="period" class="2"/&gt;
&lt;/ClassDef&gt;
<!-- PosClassSetCount=4 -->
&lt;PosClassSet index="0"&gt;
<!-- PosClassRuleCount=0 -->
&lt;/PosClassSet&gt;
&lt;PosClassSet index="1"&gt;
<!-- PosClassRuleCount=1 -->
&lt;PosClassRule index="0"&gt;
<!-- GlyphCount=3 -->
<!-- PosCount=1 -->
&lt;Class index="0" value="2"/&gt;
&lt;Class index="1" value="3"/&gt;
&lt;PosLookupRecord index="0"&gt;
&lt;SequenceIndex value="1"/&gt;
&lt;LookupListIndex value="0"/&gt;
&lt;/PosLookupRecord&gt;
&lt;/PosClassRule&gt;
&lt;/PosClassSet&gt;
&lt;PosClassSet index="2"&gt;
<!-- PosClassRuleCount=0 -->
&lt;/PosClassSet&gt;
&lt;PosClassSet index="3"&gt;
<!-- PosClassRuleCount=0 -->
&lt;/PosClassSet&gt;
&lt;/ContextPos&gt;
&lt;/Lookup&gt;
Thus we see that the coverage table Coverage also contains the other glyphs in the same class
as ‘A’. Next comes the class table, ClassDef1, and that is where each glyph is associated with
one class, and only one. Next, PosClassSet contains all the meta–context strings that begin
with the class given by the index attribute (class 0 being the default class—the one that includes all the glyphs that do not belong to any other class).
In our example, obviously, the only PosClassSet of interest to us is the one for class 1: those
context strings whose first glyph is in class 1.
Inside the PosClassSet we find the same data as in Format 1. The only difference is that here,
instead GlyphIDs, there are Classes: it is the list of classes that makes up our context string
(which is a string not of glyphs, but of classes of glyphs).
Let us point out that Format 2, as flexible as it may seem, suffers from a few drawbacks. These
drawbacks are due primarily to the fact that each glyph can belong to only one class. Suppose
then that we are interested in the context strings “ATA”, in which the first ‘A’, but not the
second, can also be an ‘À’. On the other hand, the second ‘A’ can also be an ‘Â’. How can we
define the classes in question? We cannot. The only solution is to use Format 1 and explicitly
write out all the permitted combinations of glyphs.
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
Or we can use Format 3, which has a different approach. To avoid the problem that we just
mentioned, we use not classes but coverage tables. Thus a context string becomes a string of
coverage tables. The main difference is that we are free to put the same glyph into more than
one coverage table—something that is not possible with classes.
Here is the same example, this time in Format 3:
&lt;Lookup index="10"&gt;
&lt;LookupType value="7"/&gt;
&lt;LookupFlag value="0"/&gt;
<!-- SubTableCount=1 -->
&lt;ContextPos index="0" Format="3"&gt;
<!-- GlyphCount=3 -->
<!-- PosCount=1 -->
&lt;Coverage index="0" Format="1"&gt;
&lt;Glyph value="A"/&gt;
&lt;Glyph value="Agrave"/&gt;
&lt;Glyph value="Aacute"/&gt;
&lt;/Coverage&gt;
&lt;Coverage index="1" Format="1"&gt;
&lt;Glyph value="period"/&gt;
&lt;/Coverage&gt;
&lt;Coverage index="2" Format="1"&gt;
&lt;Glyph value="V"/&gt;
&lt;Glyph value="W"/&gt;
&lt;Glyph value="Y"/&gt;
&lt;/Coverage&gt;
&lt;PosLookupRecord index="0"&gt;
&lt;SequenceIndex value="1"/&gt;
&lt;LookupListIndex value="0"/&gt;
&lt;/PosLookupRecord&gt;
&lt;/ContextPos&gt;
&lt;/Lookup&gt;
The structure of this Lookup is quite different. First of all, there is no PosRuleSet or PosClassSet here. Next, we have not just one Coverage entry but one for each glyph in the context
string. Finally, we need only supply a PosLookupRecord for each glyph that could be moved
by another lookup, and the task is done.
This format for lookup 7 is so powerful that the reader must be wondering why we still retain
Format 2. Yet there are cases in which Format 2 is much more powerful. For example, all the
context strings in Format 3 have exactly the same length. For instance, it is impossible a string
of three glyphs and a string of four glyphs at the same time—something that can be done with
Format 2.
D.9.3.9
Lookup type 8: extended contextual positioning
Now we come to the ne plus ultra of positioning: extended contextual positioning. But in what
way can it be “extended”? Can we leave the plane to extend the positioning into space? Of
```

```text
D.9. The OpenType Advanced Typographic Tables
course not. In fact, it is the context that is “extended”. In lookup type 7, we would indicate a
string of glyphs, and when that string occurred in a document, it became the context. Within
this context, we would move certain glyphs. Here we still have the concept of a context string;
but when that string occurs, we can also examine what happens before and after it.
Let us put ourselves in the position of the processor. We read glyph codes and render the
corresponding glyphs. Suddenly we encounter an extended context string, “ABC”. Processing
it entails (a) having retained the preceding glyphs (those that we had just set before “ABC”) in
memory, retrieving them, and checking whether or not they match another string of glyphs
that we call the backtrack; (b) being able to move forward and examine what will follow,
without setting the glyphs but instead merely checking whether the following glyphs match
another string of glyphs that we call the lookahead.
Why should we do such a thing? Because the glyphs in the context string can no longer be
used for other lookups. Suppose that our context string is “TAT” and that another ‘A’ comes
after this string. We would have wanted kerning between the second ‘T’ and the ‘A’ to follow.
But it is too late: the formatting is ruined, because the string “TAT” was used whole in a
certain operation, even if only the first or the second glyph was moved. Once this lookup
has been finished, the string disappears from circulation, and kerning with what follows can
no longer be performed.
By using an extended context, on the other hand, we can take as a context string only the
glyph that is to be moved. What occurs before that string will be the backtrack; what occurs
after the string will be the lookahead.
Here is our example of a lookup of type 7, rewritten in type 8:
&lt;Lookup index="11"&gt;
&lt;LookupType value="8"/&gt;
&lt;LookupFlag value="0"/&gt;
<!-- SubTableCount=1 -->
&lt;ChainContextPos index="0" Format="1"&gt;
&lt;Coverage Format="1"&gt;
&lt;Glyph value="period"/&gt;
&lt;/Coverage&gt;
<!-- ChainPosRuleSetCount=1 -->
&lt;ChainPosRuleSet index="0"&gt;
<!-- ChainPosRuleCount=1 -->
&lt;ChainPosRule index="0"&gt;
<!-- BacktrackGlyphCount=1 -->
&lt;Backtrack index="0" value="A"/&gt;
<!-- InputGlyphCount=2 -->
&lt;Input index="0" value="period"/&gt;
<!-- LookAheadGlyphCount=1 -->
&lt;LookAhead index="0" value="V"/&gt;
<!-- PosCount=1 -->
&lt;PosLookupRecord index="0"&gt;
&lt;SequenceIndex value="0"/&gt;
&lt;LookupListIndex value="0"/&gt;
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
&lt;/PosLookupRecord&gt;
&lt;/ChainPosRule&gt;
&lt;/ChainPosRuleSet&gt;
&lt;/ChainContextPos&gt;
&lt;/Lookup&gt;
What has changed? The elements ContextPos (the type of lookup), PosRuleSet (the set of
rules), and PosRule (a rule) have become ChainContextPos, ChainPosRuleSet, and ChainPosRule; only the name has changed. On the other hand, two elements have been added at
the same level as Input: Backtrack and LookAhead. These two elements contain glyphs listed
in a certain order. This order is the logical order of the glyphs in the lookahead for LookAhead
and the order opposite that of the lookahead for Backtrack. For example, if we wish to move
the string “DEF” only if it is preceded by “ABC” and followed by “GHI”, the lookahead will be
in the order ‘G’, ‘H’, and ‘I’; conversely, the backtrack will be in the opposite order: ‘C’, ‘B’, ‘A’.
That is due to the fact that the glyphs are placed on a stack; when they are popped, they will
necessarily be in the order opposite to that in which they were pushed.
We have not yet discussed formats. Type 8 also offers three formats. There is nothing surprising about that: the formats are the same as for type 7. First we take individual glyphs
(Format 1); then we extend Format 1 by taking glyph classes (Format 2); finally, we extend
it in a different way by taking coverage tables for glyphs. The advantages and disadvantages
of the three formats are the same as for type 7: Format 1 is simple and precise but may be
quite long when there are many glyphs; Format 2, which is suited to very precise and distinct
categories of glyphs, allows us to save a great deal of space by defining glyph classes, and we can
use these classes to write the context string, the backtrack, and the lookahead; Format 3 uses
coverage tables rather than classes, which has the advantage that we can use the same glyph
in different ways, since it can appear in several coverage tables at the same time—which is not
true of classes.
Here is our example of code, rewritten in Format 2:
&lt;Lookup index="12"&gt;
&lt;LookupType value="8"/&gt;
&lt;LookupFlag value="0"/&gt;
<!-- SubTableCount=1 -->
&lt;ChainContextPos index="0" Format="2"&gt;
&lt;Coverage Format="1"&gt;
&lt;Glyph value="period"/&gt;
&lt;/Coverage&gt;
&lt;BacktrackClassDef Format="2"&gt;
&lt;ClassDef glyph="A" class="1"/&gt;
&lt;ClassDef glyph="Aacute" class="1"/&gt;
&lt;ClassDef glyph="Agrave" class="1"/&gt;
&lt;/BacktrackClassDef&gt;
&lt;InputClassDef Format="2"&gt;
&lt;ClassDef glyph="period" class="1"/&gt;
&lt;/InputClassDef&gt;
```

```text
D.9. The OpenType Advanced Typographic Tables
&lt;LookAheadClassDef Format="2"&gt;
&lt;ClassDef glyph="V" class="1"/&gt;
&lt;ClassDef glyph="W" class="1"/&gt;
&lt;/LookAheadClassDef&gt;
<!-- ChainPosClassSetCount=2 -->
&lt;ChainPosClassSet index="0"&gt;
<!-- ChainPosClassRuleCount=0 -->
&lt;/ChainPosClassSet&gt;
&lt;ChainPosClassSet index="1"&gt;
<!-- ChainPosClassRuleCount=1 -->
&lt;ChainPosClassRule index="0"&gt;
<!-- BacktrackGlyphCount=1 -->
&lt;Backtrack index="0" value="1"/&gt;
<!-- InputGlyphCount=2 -->
&lt;Input index="0" value="1"/&gt;
<!-- LookAheadGlyphCount=1 -->
&lt;LookAhead index="0" value="1"/&gt;
<!-- PosCount=1 -->
&lt;PosLookupRecord index="0"&gt;
&lt;SequenceIndex value="0"/&gt;
&lt;LookupListIndex value="0"/&gt;
&lt;/PosLookupRecord&gt;
&lt;/ChainPosClassRule&gt;
&lt;/ChainPosClassSet&gt;
&lt;/ChainContextPos&gt;
&lt;/Lookup&gt;
In the first part, we define the classes for the backtrack (BacktrackClassDef), the context
string (InputClassDef), and the lookahead (LookAheadClassDef). Next, within the element
ChainPosClassSet corresponding to class 1, the class for the period in the context string, there
is a rule named ChainPosClassRule. This rule operates on the backtrack ‘A’ (Backtrack), the
context string ‘.’ (Input), and the lookahead ‘V’ (LookAhead). The PosLookupRecord has not
changed, except that the ‘.’ now appears at index 0, since it is the only glyph in the context
string.
Note that the coverage table is concerned only with the first glyph in the context string (not
with the first glyph in the backtrack, even though the backtrack, as its name suggests, logically
precedes the context string).
One important note: In type 7, we saw that defining classes is quite constraining. If the same
glyph occurs multiple times in the context string, it must have the same behavior each time,
since it can belong to only one class—the class that was part of the context string, not the
glyph itself. This constraint still exists in type 8, but it is greatly lightened by the fact that the
classes for the backtrack, the context string, and the lookahead are defined separately. Thus
there are fewer chances of having the same glyph with different behavior.
In any event, we have now come to Format 3 of type 8. As in type 7, here again we use coverage
tables. Here is our perennial example of “A.V”, written in Format 3:
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
&lt;Lookup index="13"&gt;
&lt;LookupType value="8"/&gt;
&lt;LookupFlag value="0"/&gt;
<!-- SubTableCount=1 -->
&lt;ChainContextPos index="0" Format="3"&gt;
<!-- BacktrackGlyphCount=1 -->
&lt;BacktrackCoverage index="0" Format="1"&gt;
&lt;Glyph value="A"/&gt;
&lt;/BacktrackCoverage&gt;
<!-- InputGlyphCount=1 -->
&lt;InputCoverage index="0" Format="1"&gt;
&lt;Glyph value="period"/&gt;
&lt;/InputCoverage&gt;
<!-- LookAheadGlyphCount=1 -->
&lt;LookAheadCoverage index="0" Format="1"&gt;
&lt;Glyph value="V"/&gt;
&lt;/LookAheadCoverage&gt;
<!-- PosCount=1 -->
&lt;PosLookupRecord index="0"&gt;
&lt;SequenceIndex value="0"/&gt;
&lt;LookupListIndex value="0"/&gt;
&lt;/PosLookupRecord&gt;
&lt;/ChainContextPos&gt;
&lt;/Lookup&gt;
What is there to say? This lookup is simple and powerful: we can take as many glyphs as we
wish for the backtrack, the context string, or the lookahead, and we can choose a coverage
table for each glyph in these three strings. In short, we enjoy total freedom. The coverage tables for the glyphs in the backtrack are called BacktrackCoverage; those in the context string,
InputCoverage; finally, those in the lookahead, LookAheadCoverage. The PosLookupRecord is
not changed.
D.9.3.10
Lookup type 9: an extension
Having seen the epitome of power in tables 7 and 8, one may well ask apprehensively: “what
could there be in table 9?”. Do not worry. Suppose that you wish to make a hole in the fence
on the other side of your yard and that the power cord for your drill is not long enough. What
do you do? You use an extension cord. Type 9 is exactly the same thing: an extension.
One thing that we have not mentioned—since TTX allows us to avoid this sort of banal
detail—is the fact that in the GPOS table there are often pointers to lookups and that these
pointers are always 2-byte values. That means that a subtable for a lookup can never be more
than 64 kilobytes from the start of the table. That seems reasonable at first glance because the
font itself is often smaller than 64 kB.
But imagine that we have a super-font with thousands of glyphs, each of which behaves differently. The developer would have to create thousands of classes or coverage tables, and the
threshold of 64 kB would quickly be surpassed. Type 9 comes to the rescue. It has a 4-byte
pointer, and we can therefore point to data as far as 232 = 4 gigabytes from the start of the
```

```text
D.9. The OpenType Advanced Typographic Tables
table. The lookup of type 9 is thus the “local representative” of the more distant lookup: we
place the former less than 64 kB from the start of the table and point to it when we need to
use the latter.
D.9.4
The GSUB Table
The GSUB table manages glyph substitution. Its applications are numerous: it can be used
to replace one glyph with another in a certain context given by the feature, to choose from
among several variants of the same glyph, to form ligatures (or, conversely, to decompose
them), to perform contextual analysis, etc.
It shares with the other tables its schema for organizing data: we start with a script (script)
and possibly a language; then we choose one or more features (features), which lead us to a
number of lookups. These lookups are of seven types, and we shall study them by starting
with the simplest ones.
D.9.4.1
Lookup type 1: simple substitution
This is the simplest case: if the feature is enabled, a given glyph is systematically replaced by
another. For example, when we select the “small capitals” feature, the lowercase letters are
replaced with small capitals. Here is the beginning of the GPOS table followed by an example
of one such lookup, drawn from the font Palatino Linotype:
&lt;GSUB&gt;
&lt;Version value="1.0"/&gt;
&lt;ScriptList&gt;
<!-- ScriptCount=3 -->
&lt;ScriptRecord index="0"&gt;
&lt;ScriptTag value="cyrl"/&gt;
&lt;Script&gt;
&lt;DefaultLangSys&gt;
&lt;ReqFeatureIndex value="65535"/&gt;
<!-- FeatureCount=8 -->
&lt;FeatureIndex index="0" value="0"/&gt;
...
&lt;FeatureIndex index="5" value="5"/&gt;
&lt;FeatureIndex index="6" value="6"/&gt;
&lt;FeatureIndex index="7" value="7"/&gt;
&lt;/DefaultLangSys&gt;
<!-- LangSysCount=0 -->
&lt;/Script&gt;
&lt;/ScriptRecord&gt;
&lt;ScriptRecord index="1"&gt;
...
&lt;/ScriptRecord&gt;
&lt;ScriptRecord index="2"&gt;
...
&lt;/ScriptRecord&gt;
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
&lt;/ScriptList&gt;
&lt;FeatureList&gt;
&lt;FeatureRecord index="5"&gt;
&lt;FeatureTag value="subs"/&gt;
&lt;Feature&gt;
<!-- LookupCount=1 -->
&lt;LookupListIndex index="0" value="9"/&gt;
&lt;/Feature&gt;
&lt;/FeatureRecord&gt;
...
&lt;/FeatureList&gt;
&lt;LookupList&gt;
...
&lt;Lookup index="9"&gt;
&lt;LookupType value="1"/&gt;
&lt;LookupFlag value="0"/&gt;
&lt;SingleSubst index="0" Format="2"&gt;
&lt;Substitution in="a" out="asuperior"/&gt;
&lt;Substitution in="ae" out="aesuperior"/&gt;
...
&lt;Substitution in="zero" out="zeroinferior"/&gt;
&lt;/SingleSubst&gt;
&lt;/Lookup&gt;
&lt;/LookupList&gt;
&lt;/GSUB&gt;
where we also see the sections ScriptList and FeatureList, which are identical to those that
have already been described in the section on the GPOS table (see §D.9.3.1).
The lookup is also arranged as in the GPOS table: first its type (LookupType), then the usual
LookupFlag (see §D.9.1.1). Next, there is a Substitution element for each substitution: the
in attribute contains the name of the original glyph, and out contains the name of the glyph
that we obtain in its place. There could hardly be anything simpler.
The reader must have noticed that the SingleSubst element also has a Format attribute,
which has not been mentioned yet. Indeed, there are two formats for lookups of type 1. The
first assumes that the identification numbers of the target glyphs have a fixed offset relative
to the original glyphs. Thus we supply, in the TTF file, the original numbers and the offset,
and the processor immediately finds the target glyphs. The second format is more general: it
contains a coverage table for the original glyphs and a table of the corresponding glyphs to be
substituted. In any case, TTX flattens all that and shows us only the Substitution elements;
thus there is no need to worry about the choice of format and its implementation.
D.9.4.2
Lookup type 2: multiple substitution
It is relatively rare to replace one glyph with several. The font Nafees Nasta’leeq [1], for example, uses this mechanism to replace an Arabic glyph by its base part and its dots (see
Figure D-5). Do not forget that after going through the GSUB table we must still go through
```

```text
D.9. The OpenType Advanced Typographic Tables
Table GSUB
Feature medi
Type 2 lookup
Table GPOS
Feature medi
Type 8 lookup and then
type 3 lookup
➂
➀
➁
➂
➀
➁
Unicode character
U+06D3
Figure D-5: The glorious fate of the character 06d3 arabic letter yeh barree with hamza above: first
it becomes a glyph; then the glyph is replaced (through a type 2 lookup) by the three glyphs above; finally,
the three glyphs are repositioned by a number of lookups. The feature in question is medi—i.e., the letter’s
medial form. Thus the whole process involves moving from the isolated form (which represents the original
Unicode character) to the medial form by decomposing the glyph into three parts for greater flexibility.
GPOS; therefore, we can very precisely reposition the glyphs generated through the multiple
substitution in question.
Here is an example of a multiple substitution. The code has been taken from the font Nafees
Nasta’leeq.
&lt;Lookup index="2"&gt;
&lt;LookupType value="2"/&gt;
&lt;LookupFlag value="1"/&gt;
<!-- SubTableCount=1 -->
&lt;MultipleSubst index="0" Format="1"&gt;
&lt;Coverage Format="2"&gt;
&lt;Glyph value="uni0628"/&gt;
&lt;Glyph value="afii57506"/&gt;
&lt;/Coverage&gt;
<!-- SequenceCount=2 -->
&lt;Sequence index="0"&gt;
<!-- GlyphCount=2 -->
&lt;Substitute index="0" value=".notdef#49"/&gt;
&lt;Substitute index="1" value=".notdef#714"/&gt;
&lt;/Sequence&gt;
&lt;Sequence index="1"&gt;
<!-- GlyphCount=2 -->
&lt;Substitute index="0" value=".notdef#49"/&gt;
&lt;Substitute index="1" value=".notdef#716"/&gt;
&lt;/Sequence&gt;
&lt;/MultipleSubst&gt;
&lt;/Lookup&gt;
The element that corresponds to lookup type 2 is MultipleSubst. For now, there is only
one format. It is followed by a coverage table for the original glyph. For each element in
the coverage table, there is a Sequence element, which contains the glyphs with which that
glyph is to be replaced. They are given in the desired order. Do not be astonished by glyph
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
names as bizarre as .notdef#716: the font may happen to be a pure TrueType font, and its
developers may not have provided an adequate PostScript name for each glyph. After all, in
a TrueType font we refer to glyphs by their numbers (glyph identifiers, or GlyphIDs), not by
their names. When TTX tried to give names to these poor nameless glyphs, it had to use the
default PostScript name (.notdef); and since glyph names must also be unique in TTX, it
added a number to each nameless glyph that it encountered. Just for information: there are
962 glyphs in this font, no fewer than 790 (!) of which have names of the .notdef#123 variety.
D.9.4.3
Lookup type 3: variant selection
In the discussion of characters and glyphs, we said that a character can be represented by
thousands of glyphs. But who takes on the responsibility of representing all those glyphs?
Most will be in the various fonts, which come from different designers from different countries, different eras, and different contexts. But some may appear in the same font or, at a
minimum, in the same font family. For example, are the glyphs ‘a’, ‘A’, and ‘A’, not variants
of ‘A’?
We have acquired the habit of separating roman from small capitals, italics, and bold in separate fonts, just as formerly we had schools for girls and schools for boys. But the fact of
separating them imposed numerous limitations: no kerning between glyphs from different
fonts; no word division in words containing letters from several fonts; no searching or indexing, since a font change is data that settles inside a word like a foreign body. The problem of
an italic letter followed by an upright bracket (as in “[horrid]”), for which TEX invented the
concept of italic correction, would not have existed if the two glyphs ‘d’ and ‘]’ had been present
in the same font.
Not to mention those cases in which a little silliness is desired: actual collections of variants of
the same glyph, as in the case of the fonts AmpersandsOne and AmpersandsTwo, which together
have no fewer than 202 variants of the ampersand (Figure D-6).
Now that we have demonstrated the attraction (or the pleasure) in having several variants
of the same glyph in the same font, let us see the technique for implementing variants. The
lookup of type 3 offers us the possibility of associating any number of variants with a glyph.
What is spectacular is not the lookup itself (which is very simple) but the way that software
uses it. By enabling a glyph in the document and bringing up the contextual menu, we obtain
a list of all the variants. Faced with this splendid list, we truly have an embarrassment of
riches.
Here is an example of one such lookup, drawn from the font Palatino Linotype:
&lt;Lookup index="3"&gt;
&lt;LookupType value="3"/&gt;
&lt;LookupFlag value="0"/&gt;
<!-- SubTableCount=1 -->
&lt;AlternateSubst index="0" Format="1"&gt;
&lt;AlternateSet glyph="s"&gt;
&lt;Alternate glyph="longs"/&gt;
&lt;/AlternateSet&gt;
&lt;/AlternateSubst&gt;
&lt;/Lookup&gt;
```

```text
D.9. The OpenType Advanced Typographic Tables
! " # \$ % & ' ( ) * + , - . /
0 1 2 3 4 5 6 7 8 9 : ; < =
> ? @ A B C D E F G H I J K
L M N O P Q R S T U V W X Y Z
[ \ ] ^ _ ` a b c d e f g h
i j k l m n o p q r s t u v
w x y z { | } ~  Ä Å Ç É Ñ Ö
Ü á à â ä ã å ç é è ê ë í ì î ï
ñ ó ò ô ö õ ú ù û ü † ° ¢
£ § • ¶ ß ® © ™´ ¨ ≠Æ Ø ∞
± ≤≥¥ μ ∂∑∏π ∫ª º Ω
æ ø ¿ ¡ ¬ √ƒ ≈Δ « » …   À
Ã Õ Œ œ – — “ ” ‘ ’ ÷ ◊ÿ Ÿ
⁄ € ‹ › fifl‡ · ‚ „ ‰ Â Ê
Á Ë È Í
Figure D-6: The 202 (!) ampersands of the two fonts AmpersandsOne and AmpersandsTwo, by the American foundry CastleType. In these fonts we find everything, from the sublime to the horrible.
We could hardly do anything simpler. The element AlternateSubst contains all the cases
of glyphs with variants. Each AlternateSet contains one such glyph and its variants. The
original glyph is given by the glyph attribute of the element AlternateSet. This element can
contain any number of Alternate elements, which represent the variants. Once again, it is
the glyph attribute that contains the name of the corresponding glyph.
The little example of code above is for the ‘s’ and the “long s”. Although one would never have
guessed, this example contains a whole page of German history. If Hitler had not banned
the Gothic script in 1941 (see page 403) and if the Americans in 1945 had not considered
this script to have a Nazi character, the Germans would probably still be writing in gothic,
and therefore with a “long s”. But since History—“with a capital H”, as Georges Pérec said—
decided otherwise, the “long s”, banned from the living languages, has been condemned to be
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
a “variant”, a relic of the past, a bad memory. This lookup, obeying the hist (for “historic”)
feature, replaces the ‘s’ that we know and love with a “long s”.
This lookup has only one format. Once again, the reader will be happy to know that TTX
enormously simplifies life by offering us these data in a very simple fashion. The binary table
in a TTF is more complex, since it contains a coverage table and another table with subtables
for variants that correspond to the entries in the coverage table.
D.9.4.4
Lookup type 4: ligatures
“Et ouais, ça va, je les souffle, mes bougies ! — FFFFFFFFFFFf !” (Michel Albertini, Les Merdicoles, 1998, 173.)” This extract from the Dictionnaire des onomatopées [131, p. 214] contains the
longest ligature that the author has ever seen. Unfortunately, in the book in question, it is not
properly typeset,14 and we have the impression of seeing a series of six classic “ff” ligatures. . .
But there are more realistic cases as well. Contemporary typesetting makes frequent use of
ligatures, be they ‘’, ‘fi’, ‘fl’, ‘Ff’, ‘Ffi’, ‘Ffl’, the Flemish ‘ij’, or the Scandinavian ‘æ’, etc. And in
the Arabic script and the scripts of India, there are literally hundreds of ligatures. Ligatures
have always been cosseted by typographers, to the point that a special issue of the journal
Cahiers GUTenberg is dedicated to them [38].
Let us talk technically now: how do we encode ligatures in a GSUB table? In view of the title
of this section, the answer is not surprising: we use a type 4 lookup.
Here is the code for one such lookup, drawn from the font Palatino Linotype:
&lt;Lookup index="4"&gt;
&lt;LookupType value="4"/&gt;
&lt;LookupFlag value="0"/&gt;
<!-- SubTableCount=1 -->
&lt;LigatureSubst index="0" Format="1"&gt;
&lt;LigatureSet glyph="I"&gt;
&lt;Ligature components="J" glyph="IJ"/&gt;
&lt;/LigatureSet&gt;
&lt;LigatureSet glyph="Ismall"&gt;
&lt;Ligature components="Jsmall" glyph="IJsmall"/&gt;
&lt;/LigatureSet&gt;
&lt;LigatureSet glyph="f"&gt;
&lt;Ligature components="f,i" glyph="ffi"/&gt;
&lt;Ligature components="f,l" glyph="ffl"/&gt;
&lt;Ligature components="f,t" glyph="fft"/&gt;
&lt;Ligature components="f,b" glyph="ffb"/&gt;
&lt;Ligature components="f,h" glyph="ffh"/&gt;
&lt;Ligature components="f,k" glyph="ffk"/&gt;
&lt;Ligature components="i" glyph="fi"/&gt;
&lt;Ligature components="l" glyph="fl"/&gt;
&lt;Ligature components="f" glyph="ff"/&gt;
14 It is surprising that a publisher as prestigious as Presses Universitaires de France did not take the trouble
of asking a font designer to create a duodectuple ‘f’. We may well wonder where French publishing is headed!
```

```text
D.9. The OpenType Advanced Typographic Tables
&lt;Ligature components="t" glyph="ft"/&gt;
&lt;Ligature components="b" glyph="fb"/&gt;
&lt;Ligature components="h" glyph="fh"/&gt;
&lt;Ligature components="k" glyph="fk"/&gt;
&lt;Ligature components="j" glyph="fj"/&gt;
&lt;/LigatureSet&gt;
&lt;LigatureSet glyph="i"&gt;
&lt;Ligature components="j" glyph="ij"/&gt;
&lt;/LigatureSet&gt;
&lt;LigatureSet glyph="t"&gt;
&lt;Ligature components="t" glyph="tt"/&gt;
&lt;/LigatureSet&gt;
&lt;/LigatureSubst&gt;
&lt;/Lookup&gt;
We have refrained from shortening this code because it also gives us the full list of ligatures in
the magnificent font that is Palatino Linotype: those that we have already mentioned, but also
‘ft’, ‘fb’, ‘fh’, ‘fk’, ‘g’, ‘fft’, ‘ffb’, ‘ffh’, ‘ffk’, the ‘IJ’,15 the ‘ij’, the ‘ij’, and the ‘tt’. The code is very
simple: the LigatureSubst contains all the rules for this lookup; for each initial letter in the
ligature there is a LigatureSet (whose glyph attribute contains the letter in question). Finally,
within each LigatureSet there is one Ligature for each ligature beginning with the same
letter. Each Ligature takes a components attribute, which contains the other glyphs from
which the ligature is built up, and the glyph attribute contains the name of the glyph that
represents the ligature. Note in this regard that the glyph names given here do not correspond
to those suggested by Adobe; indeed, according to Adobe’s rules, the glyph name of a ligature
is built up from the names of the components, separated by underscores. For example, the
glyph name of the ‘fft’ ligature should be f_f_t (see §C.3.3).
D.9.4.5
Lookup type 5: contextual substitutions
Just as with lookups 7 through 9 in the GPOS table, lookups 5 through 7 in the GSUB table are
“virtual”, in the sense that the refer the processor to other lookups, from types 1 through 4. A
number of strings of glyphs, called context strings, are available, and when one of these strings
occurs, a certain lookup is applied to each of its glyphs. The role of the lookup for contextual
substitution is therefore to recognize the model string of glyphs and to indicate which lookup
should be applied to each glyph in the string.
The procedure is the same as for the contextual lookups in GPOS: the user selects a script
(script) and a language (language); the software then offers a number of features (features). The
user selects a feature, and that launches a series of lookups. Each lookup in turn contains a
series of substitution rules: context strings and lookup numbers to apply to each of the glyphs.
15 Notice here a major error in appreciation: the reader will observe that this list contains neither an ‘œ’
nor an ‘æ’, which is quite correct, since both glyphs represent linguistic, not aesthetic, ligatures. In other words,
in French, the ‘o’ and the ‘e’ are not necessarily connected: consider the word “moelleux”; likewise, the ‘æ’ in
the Scandinavian languages is a genuine separate letter, not a common ephemeral ligature between the ‘a’
and the ‘e’. The error lies in the fact of including in this list the Dutch ligature ‘ij’; indeed, this ligature is not
obligatory in this language. There are words, in particular foreign words such as “bijou” that do not take this
ligature. Thus it does not belong in this table.
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
Warning: although each of the lookups for a given feature is executed, only the first matching
context string in the lookup invokes a glyph substitution.
To illustrate contextual substitution, let us take the case of the old-fashioned form of the ampersand: ‘&c.’. Here is the code for the lookup that will use “etc.” as a context string and replace
the first two glyphs with an ampersand:
&lt;Lookup index="5"&gt;
&lt;LookupType value="5"/&gt;
&lt;LookupFlag value="0"/&gt;
<!-- SubTableCount=1 -->
&lt;ContextSubst index="0" Format="1"&gt;
&lt;Coverage Format="1"&gt;
&lt;Glyph value="e"/&gt;
&lt;/Coverage&gt;
<!-- SubRuleSetCount=1 -->
&lt;SubRuleSet index="0"&gt;
<!-- SubRuleCount=1 -->
&lt;SubRule index="0"&gt;
<!-- GlyphCount=4 -->
<!-- SubstCount=1 -->
&lt;Input index="0" value="t"/&gt;
&lt;Input index="1" value="c"/&gt;
&lt;Input index="2" value="period"/&gt;
&lt;SubstLookupRecord index="0"&gt;
&lt;SequenceIndex value="0"/&gt;
&lt;LookupListIndex value="8"/&gt;
&lt;/SubstLookupRecord&gt;
&lt;/SubRule&gt;
&lt;/SubRuleSet&gt;
&lt;/ContextSubst&gt;
&lt;/Lookup&gt;
In this code, we find the lookup type (5) and the lookup’s flag (0). The element containing the
rules for substitution is ContextSubst. Above we see Format 1 of this element. It begins with
a coverage table for the first glyph. Next there is a SubRuleSet for each glyph in the coverage
table. Each SubRuleSet contains the rules that begin with the same glyph, which are given in
the coverage table. A rule of that kind is a SubRule element that in turn contains a GlyphCount
(the total number of glyphs in a context string), an Input (a list of Glyph glyphs), a SubstCount
(the number of substitutions to perform), and a SubstLookupRecord for each substitution to
perform.
The subelement SequenceIndex in SubstLookupRecord gives the position of the glyph to
which the current substitution in the string is to be applied. Here a great deal of attention is
required, for unlike the PosLookupRecords that we saw in §D.9.3.8, the number of glyphs can
vary throughout the process. For instance, if the first SubstLookupRecord is of type 2 (multiple
substitution), there will be more glyphs after the substitution than before it. Conversely, if it
is of type 4 (ligature), there may be fewer glyphs.
```

```text
D.9. The OpenType Advanced Typographic Tables
Let us take an example. Suppose that we wish to abuse the word “rifle” in the following manner: first, we decompose the glyph ‘i’ into a “dotless i” (duly positioned by a GPOS lookup that
will subsequently be executed); next, we replace the glyphs ‘f’ and ‘l’ with the glyph ‘fl’. What
will the values of SequenceIndex be?
Counting starts at zero; therefore, the glyph ‘i’ is in position 1. But after the first rule has
been executed, our string of glyphs is ‘r’, ‘ı’, dot, ‘f’, ‘l’, ‘e’. The ‘f’ is therefore in position 3, not
position 2, as it was before.
Let us return to our example of substitution, ‘&c.’ Here is the type 4 lookup that will produce
the ligature “e + t →&”:
&lt;Lookup index="8"&gt;
&lt;LookupType value="4"/&gt;
&lt;LookupFlag value="0"/&gt;
<!-- SubTableCount=1 -->
&lt;LigatureSubst index="0" Format="1"&gt;
&lt;LigatureSet glyph="e"&gt;
&lt;Ligature components="t" glyph="ampersand"/&gt;
&lt;/LigatureSet&gt;
&lt;/LigatureSubst&gt;
&lt;/Lookup&gt;
Now let us move on to the other type 5 lookup formats: formats 2 and 3. For the reader
who has read the description of lookups 7 and 8 of the GPOS table, there is no surprise: while
Format 1 is the simplest (a coverage table for the first glyph, explicit choices for the other
glyphs), Format 2 uses glyph classes, and Format 3 uses coverage tables for all the glyphs.
Thus we extend the possibilities for formats in two different ways. In the case of Format 2, it is
sufficient to define the class of each glyph; according to those classes, the processor will select
the substitution rule to use. This format is very practical when there are glyphs with welldefined and quite distinct behaviors: they belong to as many classes as there are behaviors.
The Arabic contextual forms, for example, are examples of classes: a glyph cannot be initial
and medial at the same time. Format 3, conversely, is very convenient when there are sets
of glyphs that we wish to combine in order to make substitutions; but Format 3 also has
drawbacks, such as the fact that the context strings must all be of the same length.
Here is the same example of a substitution, in Format 2:
&lt;Lookup index="6"&gt;
&lt;LookupType value="5"/&gt;
&lt;LookupFlag value="0"/&gt;
<!-- SubTableCount=1 -->
&lt;ContextSubst index="0" Format="2"&gt;
&lt;Coverage Format="1"&gt;
&lt;Glyph value="e"/&gt;
&lt;/Coverage&gt;
&lt;ClassDef Format="2"&gt;
&lt;ClassDef glyph="c" class="3"/&gt;
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
&lt;ClassDef glyph="e" class="1"/&gt;
&lt;ClassDef glyph="period" class="4"/&gt;
&lt;ClassDef glyph="t" class="2"/&gt;
&lt;/ClassDef&gt;
<!-- SubClassSetCount=1 -->
&lt;SubClassSet index="0"&gt;
<!-- SubClassRuleCount=1 -->
&lt;SubClassRule index="0"&gt;
<!-- GlyphCount=4 -->
<!-- SubstCount=1 -->
&lt;Class index="0" value="2"/&gt;
&lt;Class index="1" value="3"/&gt;
&lt;Class index="2" value="4"/&gt;
&lt;SubstLookupRecord index="0"&gt;
&lt;SequenceIndex value="0"/&gt;
&lt;LookupListIndex value="8"/&gt;
&lt;/SubstLookupRecord&gt;
&lt;/SubClassRule&gt;
&lt;/SubClassSet&gt;
&lt;/ContextSubst&gt;
&lt;/Lookup&gt;
We see that the element ContextSubst always contains the same coverage table for the same
glyph. But here it is immediately followed by a class definition table: we start counting from 1
because class 0 is the default class for the glyphs in the font. Next, there are several SubClassSets, which contain the substitution rules that begin with the same class; the class number is
given by the index attribute. Within a SubClassSet, there is a SubClassRule for each substitution rule beginning with a glyph in the class in question. GlyphCount gives the total number
of glyphs in the context string. It is followed by a list of classes that describes the string in question. Finally, there is a series of SubstLookupRecord containing the numbers of the lookups
to execute, each of them associated with a position in the string of classes. The usual caveat
applies: since the number of glyphs is subject to change for each lookup, we must calculate
the position every time, taking account of the strings produced by the preceding lookups.
Finally, here is the same example in Format 3:
&lt;Lookup index="7"&gt;
&lt;LookupType value="5"/&gt;
&lt;LookupFlag value="0"/&gt;
<!-- SubTableCount=1 -->
&lt;ContextSubst index="0" Format="3"&gt;
<!-- GlyphCount=4 -->
<!-- SubstCount=1 -->
&lt;Coverage index="0" Format="1"&gt;
&lt;Glyph value="e"/&gt;
&lt;/Coverage&gt;
&lt;Coverage index="1" Format="1"&gt;
```

```text
D.9. The OpenType Advanced Typographic Tables
&lt;Glyph value="t"/&gt;
&lt;/Coverage&gt;
&lt;Coverage index="2" Format="1"&gt;
&lt;Glyph value="c"/&gt;
&lt;/Coverage&gt;
&lt;Coverage index="3" Format="1"&gt;
&lt;Glyph value="period"/&gt;
&lt;/Coverage&gt;
&lt;SubstLookupRecord index="0"&gt;
&lt;SequenceIndex value="0"/&gt;
&lt;LookupListIndex value="8"/&gt;
&lt;/SubstLookupRecord&gt;
&lt;/ContextSubst&gt;
&lt;/Lookup&gt;
The form is much simpler because there is no rearrangement according to the first letter in
the context string. Thus there is a coverage table, Coverage, for each position in the context
string (here the context strings are all of the same length). The SubstLookupRecords are exactly the same as in all other formats.
D.9.4.6
Lookup type 6: extended contextual substitutions
Just as in the GPOS table, we extend contextual substitutions by adding backtracks and lookaheads. For those that have not read the section describing the type 8 lookup of the GPOS
table (§D.9.3.9), let us put ourselves in the position of the processor: we read glyph codes
and render the corresponding glyphs. Suddenly the extended context string “ABC” occurs.
Processing it entails (a) having retained the preceding glyphs (those that we had just set before
“ABC”) in memory, retrieving them, and checking whether or not they match another string
of glyphs that we call the backtrack; (b) being able to move forward and examine what will
follow, without setting the glyphs but instead merely checking whether the following glyphs
match another string of glyphs that we call the lookahead.
When the backtrack, the context string, and the lookahead match the string of glyphs that is
being typeset, the substitution is performed.
The existence of the backtrack and the lookahead seems to complicate the situation, but this
complication is far from being gratuitous. On the contrary, it allows us to shorten the context
string as much as possible and to leave the backtrack and the lookahead available for other
purposes. For instance, in the previous example, we can be more precise and require a space
before the ‘e’ in “etc.” Then the space will be the backtrack, and “c.” will be the lookahead.
Here is the corresponding code:
&lt;Lookup index="8"&gt;
&lt;LookupType value="6"/&gt;
&lt;LookupFlag value="0"/&gt;
<!-- SubTableCount=1 -->
&lt;ChainContextSubst index="0" Format="1"&gt;
&lt;Coverage Format="1"&gt;
&lt;Glyph value="e"/&gt;
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
&lt;/Coverage&gt;
<!-- ChainSubRuleSetCount=1 -->
&lt;ChainSubRuleSet index="0"&gt;
<!-- ChainSubRuleCount=1 -->
&lt;ChainSubRule index="0"&gt;
<!-- BacktrackGlyphCount=1 -->
&lt;Backtrack index="0" value="space"/&gt;
<!-- InputGlyphCount=3 -->
&lt;Input index="0" value="e"/&gt;
&lt;Input index="1" value="e"/&gt;
<!-- LookAheadGlyphCount=2 -->
&lt;LookAhead index="0" value="c"/&gt;
&lt;LookAhead index="1" value="period"/&gt;
<!-- SubstCount=1 -->
&lt;SubstLookupRecord index="0"&gt;
&lt;SequenceIndex value="0"/&gt;
&lt;LookupListIndex value="1"/&gt;
&lt;/SubstLookupRecord&gt;
&lt;/ChainSubRule&gt;
&lt;/ChainSubRuleSet&gt;
&lt;/ChainContextSubst&gt;
&lt;/Lookup&gt;
The substitution rules are contained in the element ChainContextSubst. This element contains a coverage table for the first glyph in the context string (note: it is indeed the context
string, not the backtrack) and then a ChainSubRuleSet for each glyph in the coverage table.
Each ChainSubRuleSet contains the rules corresponding to the context strings whose first
glyph is the glyph in question. Each of these rules is contained in a ChainSubRule.
So far, the structure resembles that of the lookups of type 5. But at this point there are six new
elements: the length of the backtrack (BacktrackGlyphCount) and its glyphs in the opposite
order (Backtrack), the length of the context string (InputGlyphCount) and its glyphs (Input),
and finally the length and glyphs of the lookahead (LookAheadGlyphCount, LookAhead). The
SubstLookupRecord that follows is identical to the lookup of type 5: it contains, on the one
hand, the position of the glyph, or the substring of glyphs, to which the rule is to be applied
within the context string, and on the other hand the number of the lookup to apply to the
glyph or substring of glyphs.
The example above uses Format 1 of the lookup of type 5. Once again, just as in the preceding
type of lookup and the type 8 lookup of the GPOS table (§D.9.3.9), we have a Format 2 that uses
glyph classes and a Format 3 that uses coverage tables for all the glyphs in the backtrack, the
context string, and the lookahead, with the advantages and disadvantages explained above.
Here is the code for the same example, rewritten in Format 2:
&lt;Lookup index="9"&gt;
&lt;LookupType value="6"/&gt;
&lt;LookupFlag value="0"/&gt;
```

```text
D.9. The OpenType Advanced Typographic Tables
<!-- SubTableCount=1 -->
&lt;ChainContextSubst index="0" Format="2"&gt;
&lt;Coverage Format="1"&gt;
&lt;Glyph value="e"/&gt;
&lt;/Coverage&gt;
&lt;BacktrackClassDef Format="2"&gt;
&lt;ClassDef glyph="space" class="1"/&gt;
&lt;/BacktrackClassDef&gt;
&lt;InputClassDef Format="2"&gt;
&lt;ClassDef glyph="e" class="1"/&gt;
&lt;ClassDef glyph="t" class="2"/&gt;
&lt;/InputClassDef&gt;
&lt;LookAheadClassDef Format="2"&gt;
&lt;ClassDef glyph="c" class="1"/&gt;
&lt;ClassDef glyph="period" class="2"/&gt;
&lt;/LookAheadClassDef&gt;
<!-- ChainSubClassSetCount=1 -->
&lt;ChainSubClassSet index="0"&gt;
<!-- ChainSubClassRuleCount=1 -->
&lt;ChainSubClassRule index="0"&gt;
<!-- BacktrackGlyphCount=1 -->
&lt;Backtrack index="0" value="1"/&gt;
<!-- InputGlyphCount=3 -->
&lt;Input index="0" value="1"/&gt;
&lt;Input index="1" value="2"/&gt;
<!-- LookAheadGlyphCount=2 -->
&lt;LookAhead index="0" value="1"/&gt;
&lt;LookAhead index="1" value="2"/&gt;
<!-- SubstCount=1 -->
&lt;SubstLookupRecord index="0"&gt;
&lt;SequenceIndex value="0"/&gt;
&lt;LookupListIndex value="1"/&gt;
&lt;/SubstLookupRecord&gt;
&lt;/ChainSubClassRule&gt;
&lt;/ChainSubClassSet&gt;
&lt;/ChainContextSubst&gt;
&lt;/Lookup&gt;
Here we have defined separate classes for each of the three strings. And here is the same example in Format 3:
&lt;Lookup index="10"&gt;
&lt;LookupType value="6"/&gt;
&lt;LookupFlag value="0"/&gt;
<!-- SubTableCount=1 -->
&lt;ChainContextSubst index="0" Format="3"&gt;
<!-- BacktrackGlyphCount=1 -->
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
&lt;BacktrackCoverage index="0" Format="1"&gt;
&lt;Glyph value="space"/&gt;
&lt;/BacktrackCoverage&gt;
<!-- InputGlyphCount=2 -->
&lt;InputCoverage index="0" Format="1"&gt;
&lt;Glyph value="e"/&gt;
&lt;/InputCoverage&gt;
&lt;InputCoverage index="1" Format="1"&gt;
&lt;Glyph value="t"/&gt;
&lt;/InputCoverage&gt;
<!-- LookAheadGlyphCount=2 -->
&lt;LookAheadCoverage index="0" Format="1"&gt;
&lt;Glyph value="c"/&gt;
&lt;/LookAheadCoverage&gt;
&lt;LookAheadCoverage index="1" Format="1"&gt;
&lt;Glyph value="period"/&gt;
&lt;/LookAheadCoverage&gt;
<!-- SubstCount=1 -->
&lt;SubstLookupRecord index="0"&gt;
&lt;SequenceIndex value="0"/&gt;
&lt;LookupListIndex value="1"/&gt;
&lt;/SubstLookupRecord&gt;
&lt;/ChainContextSubst&gt;
&lt;/Lookup&gt;
Here we have a coverage table for each glyph in the three strings.
D.9.4.7
Lookup type 8: reverse chaining contextual substitutions
This is a variant of type 6 that was developed specially for Urdu. What is so unusual about this
script? Well, it is a variety of the Arabic script that is unique in the world because it is written
diagonally, at the level of the individual word. The lines of text run from right to left, but
each word16 begins at the upper right and ends at the left on the baseline. Thus each word
has its own little baseline, as can be seen in the few words below, which are set in the font
Nafees Nast’aliq [1]:
But how is this script so different from the others that it needs a type of lookup all to itself?
After all, it is only a variant of the Arabic script, and for that script there has never been a
need for a lookup of type 8.
16 In fact, each connected part of a word. In the Arabic script, there are letters that have only two forms:
the isolated form and the final form. When those letters are placed within a word, they break it into several
parts. The letters within each part are connected. The same is true in Urdu: each connected part of a word is
written diagonally.
```

```text
D.9. The OpenType Advanced Typographic Tables
Well, if the Arabic script can be considered cursive, that is even more true of Urdu. The letters
take more forms than the four forms (isolated, initial, medial, final) of the script, even though
only four forms exist from a grammatical point of view. In the example below, the same letter beh has been typed multiple times: first (starting at the right) by itself, then as two, three,
four, five, and six copies of the letter beh. The reader may admire the different forms that this
letter takes as it connects—to itself:
Let us now try to dissect the last of these strings of glyphs:
=
➀
➁➂➃➄➅
At the right we see the same word, but with the letters disconnected. Thus we see that we have
a final form, ; an initial form, ; and no fewer than four medial forms,  through . Of
the medial forms, the first, , is a “pre-final” form; it is used to attach the preceding letters
to the final consonant. The second, , is the right half of the fourth, ; it is used to attach
the preceding letters to the pre-final consonant. Things become more regular starting from
the third form: if we had continued to write beh, we would have had an infinite sequence of
 and . Finally, the initial, , is a slight variant of , the difference being that its lead-in
stroke is pointed, since it is a lead-in stroke, not a connecting one.
Now let us observe the evolution of the forms as we gradually add behs. Form  first appears
in the third word (the one with three behs) and then remains stable. Form  first appears in
the fourth word and then remains stable. Indeed, by comparing these words, we can see that
the word is built up from left to right: the end of the word remains stable, and the beginning
of the word changes, moving higher and higher.
We have just said that words are built up from left to right. This is why it is quite natural that
the lookup of type 8 processes the string from left to right.
The author knows one other example of a script in which words are built up from left to
right even though writing runs from right to left: biblical Hebrew with the Masoretic signs,
for which he was the first to develop a typesetting system [158].
But let us leave the fragrant spheres of the East and return to our lookup.
There is only one format for this lookup: Format 1 (which is, however, actually Format 3 of
the lookups of types 5 and 6). And the lookups invoked by substitution rules must necessarily
be simple substitutions.
Here is the code for one such example:
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
&lt;Lookup index="11"&gt;
&lt;LookupType value="8"/&gt;
&lt;LookupFlag value="0"/&gt;
<!-- SubTableCount=1 -->
&lt;ReverseChainSingleSubst index="0" Format="1"&gt;
&lt;Coverage Format="1"&gt;
&lt;Glyph value="e"/&gt;
&lt;Glyph value="eacute"/&gt;
&lt;/Coverage&gt;
<!-- BacktrackGlyphCount=1 -->
&lt;BacktrackCoverage index="0" Format="1"&gt;
&lt;Glyph value="space"/&gt;
&lt;/BacktrackCoverage&gt;
<!-- LookAheadGlyphCount=3 -->
&lt;LookAheadCoverage index="0" Format="1"&gt;
&lt;Glyph value="t"/&gt;
&lt;/LookAheadCoverage&gt;
&lt;LookAheadCoverage index="1" Format="1"&gt;
&lt;Glyph value="c"/&gt;
&lt;/LookAheadCoverage&gt;
&lt;LookAheadCoverage index="1" Format="1"&gt;
&lt;Glyph value="period"/&gt;
&lt;/LookAheadCoverage&gt;
<!-- GlyphCount=2 -->
&lt;Substitute index="0" value="E"/&gt;
&lt;Substitute index="1" value="Eacute"/&gt;
&lt;/ReverseChainSingleSubst&gt;
&lt;/Lookup&gt;
This example, as hypothetical as it is useless, will replace ‘e’ (or ‘é’) with ‘E’ (or ‘É’) if the letter
is preceded by a space and followed by ‘tc.’.
D.9.4.8
Lookup type 7: an extension
As in the case of GPOS, it may happen that a table will exceed 64 kB. In this case, the various
pointers in the table will no longer point to the data that that table contains. Therefore, as
with lookup 9 of the GPOS table, we use a special lookup that serves as an “extension”: its only
role is to point to a lookup that appears further on. The processor will follow the pointer of
a lookup of type 7, which is a 32-bit value that can thus manage tables as large as 4 gigabytes.
Fortunately, TTX masks these fastidious details, which are due to the inadequacies of the
TrueType format.
D.9.5
The JSTF Table
Here is the verse “All things were made by him; and without him was not any thing made
that was made” (John 1:3), set in a font very close to that of Gutenberg (the font Historical
English Textura, which is part of the splendid collection of historical fonts from the American
foundry Hoefler):
```

D.9. The OpenType Advanced Typographic Tables Omnia per ip∫um facta ∫unt: et ∫ine ip∫o factum e∫t nichil. (The spelling nichil, with a ‘ch’, is that of Gutenberg.) And here is the same verse presented after applying the same ligatures and abbreviations that Gutenberg used for this verse in the Göttingen Bible [280]: Oμia « iπm facta ∫unt: & ~ne iπo factum eÁ ni∏il. The difference is clear: the text is 15 percent narrower. The ligatures and abbreviations are indisputably a good way to achieve fine control over the widths of words. They can be used to improve the management of interword spaces. To do so, however, one must be able to “enable” or “disable” them dynamically, according to the requirements of each line of text. The JSTF table goes in that direction: it gives the typesetting software the means to expand or reduce the width of certain words in order to obtain the best interword spaces. To that end, three strategies are employed: extenders, GPOS and GSUB lookups, and specific JSTF lookups. D.9.5.1 Extenders In the first strategy, certain glyphs are designated as extenders. An extender is a glyph whose purpose is to expand the text. The typical example is the Arabic kashida, or “connecting stroke”, which is used to expand words. This stroke is fundamental to the Arabic script, whether for emphasizing letters by spreading them apart (that is done in poetry) or for achieving good justification, since word division is not allowed. The only problem is that typesetting systems very often define the kashida as a straight horizontal line segment—doubtless because it is easier to draw a straight line than to calculate a curve with the correct properties in real time. In the example below, we see what a real connecting stroke should be: In this example, typeset with the superb font Decotype Naskh by the Dutch company Decotype [271], we have marked with arrows the locations at which a connecting stroke occurs. An Arabic font must indeed be very modern for rectilinear extenders to work. One such example appears below: it shows the same line as above, this time set in a “journalistic” font. It goes without saying that the author does not consider the line below a masterpiece of typography. But let us return to the JSTF table. Here is the code for one JSTF table, inspired by the font Arial Unicode:

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
&lt;JSTF&gt;
&lt;Version value="1.0"/&gt;
<!-- JstfScriptCount=1 -->
&lt;JstfScriptRecord index="0"&gt;
&lt;JstfScriptTag value="arab"/&gt;
&lt;JstfScript&gt;
<!-- JstfLangSysCount=1 -->
&lt;JstfLangSysRecord&gt;
&lt;JstfLangSysTag value="ARA"/&gt;
&lt;JstfLangSys&gt;
&lt;ExtenderGlyph&gt;
<!-- GlyphCount=5 -->
&lt;ExtenderGlyph index="0" value="afii57440"/&gt;
&lt;ExtenderGlyph index="1" value="afii57391"/&gt;
&lt;ExtenderGlyph index="2" value="afii57440-"/&gt;
&lt;ExtenderGlyph index="3" value="afii57440-"/&gt;
&lt;ExtenderGlyph index="4" value="afii57440-"/&gt;
&lt;/ExtenderGlyph&gt;
&lt;/JstfLangSys&gt;
&lt;/JstfLangSysRecord&gt;
&lt;/JstfScript&gt;
&lt;/JstfScriptRecord&gt;
&lt;/JSTF&gt;
The element JstfScriptRecord contains the rules associated with a given script, whose name
JstfScriptTag contains: arab, for the Arabic script. Next, as in other OpenType advanced
typographic tables, comes the level of specialization, which involves separating the rules according to the current language. There may be an element DefJstfLangSys for the “default
language” and a JstfLangSysRecord for each language in which extenders are used. Within
the JstfLangSysRecord is the name of the language (JstfLangSysTag)—here, the Arabic language. Next, there is an element JstfLangSys, which contains the rules for justification: in
this case, the definitions of the extenders.
The glyphs that are extenders are indicated in the value attributes of the ExtenderGlyph elements. In the example above, they are five connecting strokes (kashida) of different widths.
D.9.5.2
GPOS and GSUB lookups
The second strategy, infinitely more powerful than the first, involves the judicious application
of lookups taken from the two main OpenType tables: GPOS (positionings) and GSUB (substitutions). Thus we are free to become modern-day Gutenbergs and define a series of ligatures
or rearrangements of glyphs (as in the font Prestige, seen in §D.9.3.7) that will either reduce
or increase the widths of words.
Here is how this table works. We divide the lookups into priority levels. As the priority level
gradually increases, the effect of the selected lookups must be more pronounced. The typesetting software recognizes the shortage or excess of space between the words and applies the
groups of lookups one after the other, according to increasing priority level. This operation
is repeated until the shortage or excess of space has been corrected.
```

```text
D.9. The OpenType Advanced Typographic Tables
Note that the lookups of the different priority levels are independent and that their effects
are not cumulative. For instance, if at extender level 1 we have designated the decomposition
of the triple ligatures ‘ffi’ (into ‘f’ and ‘fi’) and ‘ffl’ (into ‘f’ and ‘fl’), and at level 2 we break up
all the “f-ligatures”, we must include the lookups for the triple ligatures in the description of
level 2. That allows us to change the method of expansion or contraction completely when
moving from one level to another.
But it also introduces a major risk. Suppose that at priority level 1 we use the “f-ligatures”
(which are rather infrequent) and at level 2 we use variants of the letter ‘e’ (which is the most
common letter in English). Statistically, in a line of text, we have a much greater chance of
finding an ‘e’ than of finding an “f-ligature”. Unless, of course, the text that we are typesetting
is La disparition [289], by Georges Perec.17 No one can guarantee that priority level 2 will
give better results than priority level 1. But not to worry: after all, that is a problem for the
typesetting software, which confirms once again the principle of the OpenType fonts: the font
proposes, the software disposes.
Let us now see how these software levels appear in code. Each priority level is contained in a
JstfPriority element. This element can contain 10 subelements: five for shrinkage and five
for extension. For both shrinkage and extension, we can enable or disable an operation, and
the lookups can appear in the GPOS table or the GSUB table. By combining choices in this way,
we obtain the eight subelements: their names begin with Shrinkage or Extension, continue
with Enable or Disable, and end with GPOS or GSUB. The two remaining subelements are
described in the following section (§D.9.5.3).
Here is an example of code drawn from the font Palatino Linotype:
&lt;JstfPriority index="1"&gt;
&lt;ShrinkageEnableGSUB&gt;
<!-- LookupCount=2 -->
&lt;GSUBLookupIndex index="1" value="4"/&gt;
&lt;GSUBLookupIndex index="0" value="12"/&gt;
&lt;/ShrinkageEnableGSUB&gt;
&lt;ExtensionDisableGSUB&gt;
<!-- LookupCount=2 -->
&lt;GSUBLookupIndex index="1" value="4"/&gt;
&lt;GSUBLookupIndex index="0" value="12"/&gt;
&lt;/ExtensionDisableGSUB&gt;
&lt;/JstfPriority&gt;
Here the priority level is 1, which offers only enabling and disabling of shrinkage through the
GSUB lookups. Lookups 4 and 12 of the GSUB table are enabled. By checking to see what these
lookups look like, we see that lookup 4 is indeed the one that produces all the Latin ligatures
(the f-ligatures, but also the Flemish ‘ij’, etc.); incidentally, we have described it on page 786.
17 A 300-page book from 1969 that does not contain the letter ‘e’ even once (although an urban legend
claims that one, and only one, letter ‘e’ lies hidden in the text). [Translator’s note: An English translation by
Gilbert Adair, A Void [291], observes the same constraint.] Perec shows how a letter can disappear without
leaving a void in the book. Somewhat like his parents, who disappeared quite suddenly—on the front lines
and at Auschwitz. Perec struck again in 1972 with Les Revenentes [290], a 137-page novel with no vowel other
than ‘e’.
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
We expected this type of lookup. On the other hand, lookup 12 is much more enigmatic: it
is for the substitution of the glyphs ‘¸S’ and ‘¸s’, which are used in Turkish or, with a comma
in the place of the cedilla, in Romanian. But whether written with a cedilla, a comma, or no
diacritical mark at all, these glyphs always have exactly the same set-width. We may therefore
wonder what the purpose of this lookup is, especially since the font’s designer, if he was Turkish or Romanian, would certainly be chagrined to see these glyphs change their nationality
at random.
As for “substitutions made for justification”, it can never be said too much: they must be
handled with care. The reader should not forget that the software enables and disables substitution lookups haphazardly, according to the distribution of spaces in each line. A text in
which there is an ‘ffi’ ligature on one line while the ligature is broken on the following line
is a poorly typeset text, irrespective of the marvelous technology that helped to optimize the
spacing.
In order for this operation to succeed, the presence or absence of ligatures or glyph variants
must not affect the legibility of the text in any way. Gutenberg succeeded with his great many
ligatures, used in a rather arbitrary manner. In a way, he also trained the reader’s eye not to
pay attention to ligatures or glyph variants. That is a more difficult goal to achieve in a long
Latin text in which the only ligatures that occur are f-ligatures.
On the other hand, ligatures and variants often have semantic significance. In German, for
example, a ligature is broken up when its glyphs straddle two constituents of the word: Auflage
(“edition”) is set without a ligature because it is a word made up of auf and Lage; the word
fliegen (“to fly”), however, should be written with a ligature. Here, therefore, it is out of the
question to take action for the purposes of justification if the meaning that the ligature or its
absence has would be sacrificed.
The same is true of variants. The example below
shows us very beautiful Arabic typesetting (using the font Decotype Naskh) in which we have
marked the variant
of the Arabic letter kaf with a solid arrow and two beautiful
connecting strokes (kashida) with hollow arrows. This calligraphic variant of kaf has often
been used for justification. But Vlad Atanasiu, in his dissertation on Ottoman calligraphy [61,
Chapter 12], teaches us that this glyph has been known since the thirteenth century as the
“kaf of impiety”, doubtless because calligraphers copying out the Koran used it in particular
to write the word kufr (= “impiety”) in order to stigmatize impious persons. And the history
of this glyph does not stop there: since the regular kaf is used in the Sindhi language for
the sound ‘gk’, the kaf of impiety is used in that language for the sound ‘k’. That is how a
glyph, even one with so bad a reputation, managed to hit the jackpot and become a character:
U+06AA arabic letter swash kaf.
```

```text
D.9. The OpenType Advanced Typographic Tables
Therefore, be careful: do not use a glyph substitution for purposes of justification unless you
are sure that the modification thus made to the text concerns only a character of a purely
graphical nature that has no cultural or semantic repercussions.
D.9.5.3
JSTF lookups
This strategy is less spectacular than the previous one, but safer. It involves using lookups that
are in every respect similar to those of the GPOS table (contextual lookups are excluded). But
how do they differ from the ShrinkageEnableGPOS, etc., of the previous section?
There is one difference: size. Up to now, OpenType tables have always supplied exact values
(for offset, positioning, etc.). If a lookup specified an offset of 500 TrueType units, then enabling the lookup would cause an offset of 500 units—no more, no fewer.
In the case of JSTF lookups, the software is allowed to use a value (for offset, positioning, etc.)
less than or equal to the value specified. That approach allows very fine and flexible control of
spacing.
Let us discuss the technical details. As their name suggests, JSTF lookups are described in
the JSTF table itself. They are found in ShrinkageJSTFMax and ExtensionJSTFMax elements
(the two elements that were missing from the previous section). Here is an example of those
lookups, drawn from the font Palatino Linotype:
&lt;JstfPriority index="2"&gt;
&lt;ShrinkageJstfMax&gt;
<!-- LookupCount=1 -->
&lt;Lookup index="0"&gt;
&lt;LookupType value="1"/&gt;
&lt;LookupFlag value="0"/&gt;
<!-- SubTableCount=1 -->
&lt;SinglePos index="0" Format="1"&gt;
&lt;Coverage Format="1"&gt;
&lt;Glyph value="space"/&gt;
&lt;/Coverage&gt;
&lt;ValueFormat value="4"/&gt;
&lt;Value XAdvance="350"/&gt;
&lt;/SinglePos&gt;
&lt;/Lookup&gt;
&lt;/ShrinkageJstfMax&gt;
&lt;ExtensionJstfMax&gt;
<!-- LookupCount=1 -->
&lt;Lookup index="0"&gt;
&lt;LookupType value="1"/&gt;
&lt;LookupFlag value="0"/&gt;
<!-- SubTableCount=1 -->
&lt;SinglePos index="0" Format="1"&gt;
&lt;Coverage Format="1"&gt;
&lt;Glyph value="space"/&gt;
&lt;/Coverage&gt;
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
&lt;ValueFormat value="4"/&gt;
&lt;Value XAdvance="550"/&gt;
&lt;/SinglePos&gt;
&lt;/Lookup&gt;
&lt;/ExtensionJstfMax&gt;
&lt;/JstfPriority&gt;
In this example, a lookup of type 1 (positioning of a single glyph) is applied to the glyph
space, which is the whitespace character. The lookup involves changing the space’s width: in
the first instance, it is reduced by 350 units; in the second, it is increased by 550 units. Since
the width of this pseudoglyph is 512 units (information that we have in the table htmx), the
code above tells the software that the space character can vary between 512−350 = 162 and
512+550 = 1,062 units during typesetting.
And here, by way of information, is the priority level immediately above:
&lt;JstfPriority index="3"&gt;
&lt;ShrinkageJstfMax&gt;
<!-- LookupCount=1 -->
&lt;Lookup index="0"&gt;
&lt;LookupType value="1"/&gt;
&lt;LookupFlag value="0"/&gt;
<!-- SubTableCount=1 -->
&lt;SinglePos index="0" Format="1"&gt;
&lt;Coverage Format="2"&gt;
&lt;Glyph value="A"/&gt;
&lt;Glyph value="B"/&gt;
&lt;Glyph value="C"/&gt;
... 1319 lines ...
&lt;Glyph value="uni1EF8"/&gt;
&lt;Glyph value="uni1EF9"/&gt;
&lt;Glyph value="uni20A0"/&gt;
&lt;/Coverage&gt;
&lt;ValueFormat value="1"/&gt;
&lt;Value XPlacement="-"/&gt;
&lt;/SinglePos&gt;
&lt;/Lookup&gt;
&lt;/ShrinkageJstfMax&gt;
&lt;ExtensionJstfMax&gt;
<!-- LookupCount=1 -->
&lt;Lookup index="0"&gt;
&lt;LookupType value="1"/&gt;
&lt;LookupFlag value="0"/&gt;
<!-- SubTableCount=1 -->
&lt;SinglePos index="0" Format="1"&gt;
&lt;Coverage Format="2"&gt;
&lt;Glyph value="A"/&gt;
```

D.9. The OpenType Advanced Typographic Tables
&lt;Glyph value="B"/&gt;
&lt;Glyph value="C"/&gt;
... 1319 lines ...
&lt;Glyph value="uni1EF8"/&gt;
&lt;Glyph value="uni1EF9"/&gt;
&lt;Glyph value="uni20A0"/&gt;
&lt;/Coverage&gt;
&lt;ValueFormat value="1"/&gt;
&lt;Value XPlacement="10"/&gt;
&lt;/SinglePos&gt;
&lt;/Lookup&gt;
&lt;/ExtensionJstfMax&gt;
&lt;/JstfPriority&gt;
Here we take all the glyphs in the font and apply to them the same type 1 lookup: a reduction or expansion of the set-width by 10 units. It is too little to be visible to the naked eye;
therefore this technique cannot be called letterspacing. But is it effective? Let us take a typical
line: 60 glyphs, 12 spaces. By multiplying the increase by 60 and dividing it by 12, we find
that each space can thus be reduced by 50 units. That is a negligible amount in comparison
to the previous lookup, in which the changes to the spaces could be 11 (!) times larger. But
the visual result is certainly better, since the space is distributed among the glyphs, albeit in
homeopathic doses.
D.9.6
The GDEF Table
We have now come to the last OpenType advanced typographic table. It is an auxiliary table,
a space in which we store certain data that will be useful to the other tables. In this table,
which is something of a hodgepodge, we find four types of data:
• An arrangement of all the glyphs in the font into four classes: “base glyph”, “ligature”,
“combining glyph”, and “glyph component”. Knowing the class to which a given glyph
belongs is useful for (among other things) applying the famous LookupFlag that appears
in every lookup and that we have only briefly discussed up to now.
• A list of all the glyphs that have points of attachment, together with these points. This
list allows the software to prepare itself and not be caught by surprise when a lookup
suddenly asks it to attach a diacritical mark to a glyph.
• A list of the positions of the cursor inside ligatures. Specifically, if the font contains a
ligature, the user must not be prevented from selecting with the mouse those letters that
make up the ligature. To do so, he must be able to place the cursor inside a ligature,
and the software must know the most appropriate location. This table gives the possible
cursor positions for each ligature in the font.
• Finally, an arrangement of all the “combining glyphs” into different classes, so that a
lookup, through the use of the LookupFlag, can ignore one of them.
Here is an example of a GDEF table (drawn from the font Palatino Linotype). First, the subtable
for glyph classes:

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
&lt;GDEF&gt;
&lt;Version value="1.0"/&gt;
&lt;GlyphClassDef Format="2"&gt;
&lt;ClassDef glyph=".null" class="1"/&gt;
&lt;ClassDef glyph="A" class="1"/&gt;
&lt;ClassDef glyph="AE" class="2"/&gt;
... 9 lines ...
&lt;ClassDef glyph="Acute" class="3"/&gt;
&lt;ClassDef glyph="Acutesmall" class="3"/&gt;
... 1181 lines ...
&lt;ClassDef glyph="zerotext" class="1"/&gt;
&lt;ClassDef glyph="zeta" class="1"/&gt;
&lt;ClassDef glyph="zsuperior" class="1"/&gt;
&lt;/GlyphClassDef&gt;
This subtable is contained in a GlyphClassDef element. Each glyph is represented by a ClassDef subelement whose attributes glyph and class indicate, respectively, the glyph’s name and
class. Ordinarily there are four classes: 1 (base glyph), 2 (ligature), 3 (diacritical mark), and
4 (glyph component, like the two parts of the ‘j’, for example). In the example above, only
the first three are present.
Next comes the list of glyphs that have points of attachment (those points being given in a
coverage table), together with the list of these points, classified by glyph:
&lt;AttachList&gt;
&lt;Coverage Format="1"&gt;
&lt;Glyph value="A"/&gt;
&lt;Glyph value="E"/&gt;
&lt;Glyph value="I"/&gt;
... 24 lines ...
&lt;Glyph value="acutecomb"/&gt;
&lt;Glyph value="tildecomb"/&gt;
&lt;Glyph value="hookabovecomb"/&gt;
&lt;/Coverage&gt;
<!-- GlyphCount=30 -->
&lt;AttachPoint index="0"&gt;
<!-- PointCount=2 -->
&lt;PointIndex index="0" value="52"/&gt;
&lt;PointIndex index="1" value="53"/&gt;
&lt;/AttachPoint&gt;
...
&lt;AttachPoint index="29"&gt;
<!-- PointCount=1 -->
&lt;PointIndex index="0" value="32"/&gt;
&lt;/AttachPoint&gt;
&lt;/AttachList&gt;
```

```text
D.9. The OpenType Advanced Typographic Tables
This subtable is contained in an AttachList element. In it we find, first of all, a coverage table
containing the glyphs of interest to us. Next, for each of these glyphs, there is an AttachPoint
element containing the PointIndex point numbers. These are the points of attachment of
each glyph.
Next comes the list of positions of the cursor within the ligatures:
&lt;LigCaretList&gt;
&lt;Coverage Format="1"&gt;
&lt;Glyph value="AE"/&gt;
&lt;Glyph value="OE"/&gt;
&lt;Glyph value="ae"/&gt;
... 36 lines ...
&lt;Glyph value="AEsmall"/&gt;
&lt;Glyph value="OEsmall"/&gt;
&lt;Glyph value="IJsmall"/&gt;
&lt;/Coverage&gt;
<!-- LigGlyphCount=42 -->
&lt;LigGlyph index="0"&gt;
<!-- CaretCount=1 -->
&lt;CaretValue index="0" Format="1"&gt;
&lt;Coordinate value="1010"/&gt;
&lt;/CaretValue&gt;
&lt;/LigGlyph&gt;
...
&lt;LigGlyph index="40"&gt;
<!-- CaretCount=1 -->
&lt;CaretValue index="0" Format="2"&gt;
&lt;CaretValuePoint value="45"/&gt;
&lt;/CaretValue&gt;
&lt;/LigGlyph&gt;
&lt;LigGlyph index="41"&gt;
<!-- CaretCount=1 -->
&lt;CaretValue index="0" Format="3"&gt;
&lt;Coordinate value="645"/&gt;
&lt;DeviceTable&gt;
&lt;StartSize value="9"/&gt;
&lt;EndSize value="19"/&gt;
&lt;DeltaFormat value="1"/&gt;
&lt;DeltaValue value="[1, 0, 0, 0, 0, 0, 0, 0, 0, 0, -]"/&gt;
&lt;/DeviceTable&gt;
&lt;/CaretValue&gt;
&lt;/LigGlyph&gt;
&lt;/LigCaretList&gt;
&lt;/GDEF&gt;
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
This list is contained within a LigCaretList element. In it, we find a coverage table containing
the glyphs that we declared as ligatures (class 2) in GlyphClassDef. Next come LigGlyph elements, one for each glyph in the coverage table. Each LigGlyph contains CaretValue elements
corresponding to the various positions of the cursor.
The CaretValue elements can be of three different formats (which are, with one slight difference, identical to the three formats of the elements EntryAnchor, etc.; see §D.9.3.4): Format 1
indicates that only the x-coordinate (or the y-coordinate, if the direction of the text is vertical) of the cursor’s position is given; Format 2 indicates that not the x-coordinate or the
y-coordinate18 but a point on the glyph’s contour is given, which has the benefit that we
can track the development of the contour under the influence of TrueType instructions and
that the cursor’s position will take account of those instructions; finally, Format 3, the most
powerful of all, includes the x-coordinate (or the y-coordinate) and that coordinate’s device
table.
Finally, the subtable of classes for combining glyphs:
&lt;MarkAttachClassDef Format="2"&gt;
&lt;ClassDef glyph="Acute" class="1"/&gt;
&lt;ClassDef glyph="Acutesmall" class="1"/&gt;
&lt;ClassDef glyph="Breve" class="1"/&gt;
... 40 lines ...
&lt;ClassDef glyph="dotbelowcomb" class="2"/&gt;
... 25 lines ...
&lt;ClassDef glyph="uni1FFD" class="1"/&gt;
&lt;ClassDef glyph="uni1FFE" class="1"/&gt;
&lt;ClassDef glyph="vrachy" class="1"/&gt;
&lt;/MarkAttachClassDef&gt;
It is the spitting image of the GlyphClassDef subtable, except for the name of the global element, which is MarkAttachClassDef. The specification gives no indication of the choice of
classes of combining glyphs. Here we have adopted a very simplistic classification: 1 for accents placed above a letter, 2 for those placed below. We could also use a classification similar
to that of combining characters in Unicode (see page 127).
The last eight bits of the LookupFlag in a lookup can take the value of a class of combining
glyphs. The combining glyphs of that class will then be ignored by the lookup.
D.10
Predefined Features, Languages, and Scripts
D.10.1
Predefined Languages and Scripts
The OpenType specification defines tags for scripts and languages. Here is the list of scripts:
18 There is one slight difference. In the case of EntryAnchor and ExitAnchor, Format 2 included both the
x-coordinate or y-coordinate and the number of the point on the contour. Here only the point on the contour
is used.
```

D.10. Predefined Features, Languages, and Scripts Arabic arab Georgian geor Mongolian mong Armenian armn Greek grek Ogham ogam Bengali beng Gujarati gujr Oriya orya Bopomofo bopo Gurmukhi guru Runic runr Braille brai Hangul hang Sinhalese sinh Burmese mymr Hangul Jamo jamo Syriac syrc Byzantine music byzm Hebrew hebr Tamil taml Canadian syllabics cans Hiragana kana Telugu telu Cherokee cher Kannada knda Thaana thaa CJK Ideographic hani Katakana kana Thai thai Cyrillic cyrl Khmer khmr Tibetan tibt Default DFLT Lao lao Yi yi Devanagari deva Latin latn Ethiopian ethi Malayalam mlym And here is the list of languages, following ISO 639-2 [191]: Abkhazian ABK Greek, Modern (1453–) GRE/ ELL Nyankole NYN Achinese ACE Greenlandic KAL Nynorsk, Norwegian NNO Acoli ACH Guarani GRN Nyoro NYO Adangme ADA Gujarati GUJ Nzima NZI Adygei ADY Gwicht’in GWI Occitan (post1500) OCI Adyghe ADY Haida HAI Oirat XAL Afar AAR Haitian HAT Ojibwa OJI Afrihili AFH Haitian Creole HAT Old Bulgarian CHU Afrikaans AFR Hausa HAU Old Church Slavonic CHU Afro-Asiatic (Other) AFA Hawaiian HAW Old Newari NWC Ainu AIN Hebrew HEB Old Slavonic CHU Akan AKA Herero HER Oriya ORI Akkadian AKK Hiligaynon HIL Oromo ORM Albanian ALB/ SQI Himachali HIM Osage OSA

Appendix D : The TrueType, OpenType, and AAT Font Formats Alemani GSW Hindi HIN Ossetian OSS Aleut ALE Hiri Motu HMO Ossetic OSS Algonquian languages ALG Hittite HIT Otomian languages OTO Altaic (Other) TUT Hmong HMN Pahlavi PAL Amharic AMH Hungarian HUN Palauan PAU Angika ANP Hupa HUP Pali PLI Apache languages APA Iban IBA Pampanga PAM Arabic ARA Icelandic ICE/ ISL Pangasinan PAG Aragonese ARG Ido IDO Panjabi PAN Aramaic ARC Igbo IBO Papiamento PAP Arapaho ARP Ijo IJO Papuan (Other) PAA Araucanian ARN Iloko ILO Pedi NSO Arawak ARW Inari Sami SMN Persian PER/ FAS Armenian ARM/ HYE Indic (Other) INC Persian, Old (ca. 600– 400 bc) PEO Aromanian RUP IndoEuropean (Other) INE Philippine (Other) PHI Artificial (Other) ART Indonesian IND Phoenician PHN Arumanian RUP Ingush INH Pilipino FIL Assamese ASM Interlingua (International Auxiliary Language Association) INA Pohnpeian PON Asturian AST Interlingue ILE Polish POL Athapascan languages ATH Inuktitut IKU Portuguese POR Australian languages AUS Inupiaq IPK Prakrit languages PRA Austronesian (Other) MAP Iranian (Other) IRA Provençal OCI Avaric AVA Irish GLE Provençal, Old (to 1500) PRO

D.10. Predefined Features, Languages, and Scripts Avestan AVE Irish, Middle (900–1200) MGA Punjabi PAN Awadhi AWA Irish, Old (to 900) SGA Pushto PUS Aymara AYM Iroquoian languages IRO Quechua QUE Azerbaijani AZE Italian ITA Rajasthani RAJ Bable AST Japanese JPN Rapanui RAP Balinese BAN Javanese JAV Rarotongan RAR Baltic (Other) BAT Judeo-Arabic JRB Reserved for local use QAAQTZ Baluchi BAL Judeo-Persian JPR RhaetoRomance ROH Bambara BAM Kabardian KBD Romance (Other) ROA Bamileke languages BAI Kabyle KAB Romanian RUM/ RON Banda BAD Kachin KAC Romany ROM Bantu (Other) BNT Kalaallisut KAL Rundi RUN Basa BAS Kalmyk XAL Russian RUS Bashkir BAK Kamba KAM Salishan languages SAL Basque BAQ/ EUS Kannada KAN Samaritan Aramaic SAM Batak (Indonesia) BTK Kanuri KAU Sami languages (Other) SMI Beja BEJ Kara-Kalpak KAA Samoan SMO Belarusian BEL KarachayBalkar KRC Sandawe SAD Bemba BEM Karelian KRL Sango SAG Bengali BEN Karen KAR Sanskrit SAN Berber (Other) BER Kashmiri KAS Santali SAT Bhojpuri BHO Kashubian CSB Sardinian SRD Bihari BIH Kawi KAW Sasak SAS Bikol BIK Kazakh KAZ Saxon, Low NDS Bilin BYN Khasi KHA Scots SCO Bini BIN Khmer KHM Scottish Gaelic GLA

Appendix D : The TrueType, OpenType, and AAT Font Formats Bislama BIS Khoisan (Other) KHI Selkup SEL Blin BYN Khotanese KHO Semitic (Other) SEM Bokmål, Norwegian NOB Kikuyu KIK Sepedi NSO Bosnian BOS Kimbundu KMB Serbian SCC/ SRP Braj BRA Kinyarwanda KIN Serer SRR Breton BRE Kirdki ZZA Shan SHN Buginese BUG Kirghiz KIR Shona SNA Bulgarian BUL Kirmanjki ZZA Sichuan Yi III Buriat BUA Klingon TLH Sicilian SCN Burmese BUR/ MYA Komi KOM Sidamo SID Caddo CAD Kongo KON Sign languages SGN Carib CAR Konkani KOK Siksika BLA Castilian SPA Korean KOR Sindhi SND Catalan CAT Kosraean KOS Sinhala SIN Caucasian (Other) CAU Kpelle KPE Sinhalese SIN Cebuano CEB Kru KRO Sino-Tibetan (Other) SIT Celtic (Other) CEL Kuanyama KUA Siouan languages SIO Central American Indian (Other) CAI Kumyk KUM Skolt Sami SMS Chagatai CHG Kurdish KUR Slave (Athapascan) DEN Chamic languages CMC Kurukh KRU Slavic (Other) SLA Chamorro CHA Kutenai KUT Slovak SLO/ SLK Chechen CHE Kwanyama KUA Slovenian SLV Cherokee CHR Ladino LAD Sogdian SOG Chewa NYA Lahnda LAH Somali SOM Cheyenne CHY Lamba LAM Songhai SON Chibcha CHB Lao LAO Soninke SNK

D.10. Predefined Features, Languages, and Scripts Chichewa NYA Latin LAT Sorbian languages WEN Chinese CHI/ ZHO Latvian LAV Sotho, Northern NSO Chinook Jargon CHN Letzeburgesch LTZ Sotho, Southern SOT Chipewyan CHP Lezghian LEZ South American Indian (Other) SAI Choctaw CHO Limburgan LIM South Ndebele NBL Chuang ZHA Limburger LIM Southern Altai ALT Church Slavic CHU Limburgish LIM Southern Sami SMA Church Slavonic CHU Lingala LIN Spanish SPA Chuukese CHK Lithuanian LIT Sranan Togo SRN Chuvash CHV Lojban JBO Sukuma SUK Classical Nepal Bhasa NWC Low German NDS Sumerian SUX Classical Newari NWC Low Saxon NDS Sundanese SUN Coptic COP Lower Sorbian DSB Susu SUS Cornish COR Lozi LOZ Swahili SWA Corsican COS Luba-Katanga LUB Swati SSW Cree CRE Luba-Lulua LUA Swedish SWE Creek MUS Luiseño LUI Swiss German GSW Creoles and pidgins (Other) CRP Lule Sami SMJ Syriac SYR Creoles and pidgins, English-based (Other) CPE Lunda LUN Tagalog TGL Creoles and pidgins, French-based (Other) CPF Luo (Kenya and Tanzania) LUO Tahitian TAH

Appendix D : The TrueType, OpenType, and AAT Font Formats Creoles and pidgins, Portuguesebased (Other) CPP Lushai LUS Tai (Other) TAI Crimean Tatar CRH Luxembourgish LTZ Tajik TGK Crimean Turkish CRH MacedoRomanian RUP Tamashek TMH Croatian SCR/ HRV Macedonian MAC/ MKD Tamil TAM Cushitic (Other) CUS Madurese MAD Tatar TAT Czech CZE/ CES Magahi MAG Telugu TEL Dakota DAK Maithili MAI Tereno TER Danish DAN Makasar MAK Tetum TET Dargwa DAR Malagasy MLG Thai THA Dayak DAY Malay MAY/ MSA Tibetan TIB/ BOD Delaware DEL Malayalam MAL Tigre TIG Dhivehi DIV Maldivian DIV Tigrinya TIR Dimili ZZA Maltese MLT Timne TEM Dimli ZZA Manchu MNC Tiv TIV Dinka DIN Mandar MDR tlhIngan-Hol TLH Divehi DIV Mandingo MAN Tlingit TLI Dogri DOI Manipuri MNI Tok Pisin TPI Dogrib DGR Manobo languages MNO Tokelau TKL Dravidian (Other) DRA Manx GLV Tonga (Nyasa) TOG Duala DUA Maori MAO/ MRI Tonga (Tonga Islands) TON Dutch DUT/ NLD Marathi MAR Tsimshian TSI Dutch, Middle (ca. 1050– 1350) DUM Mari CHM Tsonga TSO Dyula DYU Marshallese MAH Tswana TSN Dzongkha DZO Marwari MWR Tumbuka TUM Eastern Frisian FRS Masai MAS Tupi languages TUP

D.10. Predefined Features, Languages, and Scripts Efik EFI Mayan languages MYN Turkish TUR Egyptian (Ancient) EGY Mende MEN Turkish, Ottoman (1500–1928) OTA Ekajuk EKA Mi’kmaq MIC Turkmen TUK Elamite ELX Micmac MIC Tuvalu TVL English ENG Minangkabau MIN Tuvinian TYV English, Middle (1100– 1500) ENM Mirandese MWL Twi TWI English, Old (ca. 450–1100) ANG Miscellaneous languages MIS Udmurt UDM Erzya MYV Mohawk MOH Ugaritic UGA Esperanto EPO Moksha MDF Uighur UIG Estonian EST Moldavian MOL Ukrainian UKR Ewe EWE Mon-Khmer (Other) MKH Umbundu UMB Ewondo EWO Mongo LOL Undetermined UND Fang FAN Mongolian MON Upper Sorbian HSB Fanti FAT Mossi MOS Urdu URD Faroese FAO Multiple languages MUL Uyghur UIG Fijian FIJ Munda languages MUN Uzbek UZB Filipino FIL N’Ko NQO Vai VAI Finnish FIN Nahuatl NAH Valencian CAT Finno-Ugrian (Other) FIU Nauru NAU Venda VEN Flemish DUT/ NLD Navaho NAV Vietnamese VIE Fon FON Navajo NAV Volapük VOL French FRE/ FRA Ndebele, North NDE Votic VOT French, Middle (ca. 1400–1600) FRM Ndebele, South NBL Wakashan languages WAK French, Old (842–ca. 1400) FRO Ndonga NDO Walamo WAL Friulian FUR Neapolitan NAP Walloon WLN

Appendix D : The TrueType, OpenType, and AAT Font Formats Fulah FUL Nepal Bhasa NEW Waray WAR Ga GAA Nepali NEP Washo WAS Gaelic GLA Newari NEW Welsh WEL/ CYM Galician GLG Nias NIA Western Frisian FRY Ganda LUG NigerKordofanian (Other) NIC Wolof WOL Gayo GAY Nilo-Saharan (Other) SSA Xhosa XHO Gbaya GBA Niuean NIU Yakut SAH Geez GEZ No linguistic content ZXX Yao YAO Georgian GEO/ KAT Nogai NOG Yapese YAP German GER/ DEU Norse, Old NON Yiddish YID German, Low NDS North American Indian NAI Yoruba YOR German, Middle High (ca. 1050– 1500) GMH North Ndebele NDE Yupik languages YPK German, Old High (ca. 750– 1050) GOH Northern Frisian FRR Zande ZND Germanic (Other) GEM Northern Sami SME Zapotec ZAP Gikuyu KIK Northern Sotho NSO Zaza ZZA Gilbertese GIL Norwegian NOR Zazaki ZZA Gondi GON Norwegian Bokmål NOB Zenaga ZEN Gorontalo GOR Norwegian Nynorsk NNO Zhuang ZHA Gothic GOT Nubian languages NUB Zulu ZUL Grebo GRB Nyamwezi NYM Zuni ZUN Greek, Ancient (to 1453) GRC Nyanja NYA

D.10. Predefined Features, Languages, and Scripts
D.10.2
Predefined Features
In this section, we shall describe the 123 features that are predefined in the OpenType specification and cataloged by Microsoft. We have subdivided them into four categories:
• General features, those specific to the Latin script
• Features specific to the Semitic scripts
• Features specific to the scripts of India and Southeast Asia
• Features specific to the ideographic scripts
Please note that this classification is arbitrary and very rough. For example, it includes Latin
fonts with initial, medial, and final glyphs, but such fonts are rare; conversely, every Arabic
font is required, by the very nature of the Arabic script, to include those forms. That is why
Arabic fonts have been classified in the section for the Semitic languages.
D.10.2.1
General features, or those specific to the Latin script
• aalt (access all alternatives): show the user all the variants of a given glyph.
• abvm (above-based mark [positioning]): supports placing a diacritical mark on a base glyph,
possibly one that already bears other diacritical marks. Should be enabled by default.
• afrc (alternative fractions): automatically yields fractions with a horizontal bar. Not to be
confused with frac: afrc replaces ‘3/4’ with ‘ 3
4’, while frac replaces it with ‘2’. Should be
disabled by default.
• blwm (below-base mark [positioning]): place a diacritical mark below a base glyph, possibly
one that already bears other diacritical marks. Should be enabled by default.
• blws (below-base substitutions): replace a base glyph bearing a lower diacritical mark with
a ligature when appropriate. Should be enabled by default.
• calt (contextual alternatives): replace a glyph with one of its variants that is more appropriate in the context. Should be enabled by default.
• case (case-sensitive forms): replace the glyphs for punctuation marks with other glyphs
that are better suited to capital letters and “modern” digits; also replace old-style figures
with modern figures.
• clig (contextual ligatures): replace certain glyphs with a ligature, if the context is appropriate. Should be enabled by default.
• cpsp (capital spacing): add a bit more space between the letters for type set in full capitals.
Should be enabled by default.
• cwsh (contextual swash): replace a glyph with one of its calligraphic variants that is more
appropriate in the given context. If more than one variant is available, the interface may
present a palette of glyphs to the user.

Appendix D : The TrueType, OpenType, and AAT Font Formats
• c2pc (petite capitals from capitals). Warning: font designers have invented a new type of
letters—small capitals that are smaller than small capitals. To distinguish these letters
from small capitals, they have given them the pseudo-French name petite capitals. This
feature converts capitals into petite capitals.
• c2sc (small capitals from capitals): converts capitals into small capitals.
• dlig (discretionary ligatures): replace a string of glyphs with a ligature upon the express
request of the user. Example: in Japanese, one writes ㌖for キロメートル(kiromeetoru,
or “kilometer”), ㍿for 株式会社(kabushiki-gaishya, or “corporation”), etc.
• frac (fractions): replace a number followed by a slash and another number with a fraction
written with a slanted bar. Example: “3/4” is replaced with 2. This feature calls the two
internal features numr and dnom in order to produce the numerator and the denominator.
Should be disabled by default.
• hist (historical forms): ufe, for example, the long ‘f ’. Handle with care, becaufe the ufe of
this letter is often contextual (there is no long ‘f ’ at the end of a word) or even grammatical (in German the long ‘f ’ is not written at the end of a conftituent of a word: “Efel”, but
“Ausgabe”). The feature is more general and affects all the hiftorical forms of the letter.
Should be difabled by default.
• hlig (historical ligatures): use a number of obsolete ligatures. It is up to the designer to
decide which ligatures are “current” and which are “obsolete”. Should be disabled by
default.
• ital (italics): switch to italics. It is an excellent idea to have roman and italic glyphs in the
same font: it allows for kerning between the two!
• jalt (justification alternative): show the user some glyph variants (wider or narrower letters that are intended to improve justification.
• kern (kerning): enable kerning. Should be enabled by default for horizontal typesetting.
• liga (standard ligatures): produce the standard ligatures, such as ‘fi’ and ‘fl’.
• lnum (lining figures): replace old-style figures with modern figures.
• locl (localized forms): tailor the glyphs to the selected language. In certain scripts, such as
Cyrillic, the ways of writing a given letter vary from one country behind the former Iron
Curtain to another. Another example: in German the umlaut is written lower than the
French diaeresis; compare “GHI” (German) and “äöü” (French). This difference is certainly due to the fact that French gives precedence to the other accent marks, with which
the diaeresis must be aligned: “äéöèüê”. This feature produces forms tailored to the active
language. Should be enabled by default.
• mark (mark positioning): places diacritical marks on the glyphs. Should be enabled by default.

D.10. Predefined Features, Languages, and Scripts
• mgrk (mathematical Greek): use the glyphs for Greek letters that are better suited to mathematics than to Greek text. Warning: using special letterforms for Greek mathematics is a
habit peculiar to the English-speaking countries. Traditionally the French use the letters
from Greek text faces in formulae as well. See [163] for a series of examples.
• mkmk (mark-to-mark positioning): supports the placing of diacritical marks over other diacritical marks. Should be enabled by default.
• nalt (alternate annotation forms): show the user a list of “annotated” letters or digits—i.e.,
those enclosed in circles or boxes, written white on black, etc.
• onum (oldstyle figures): replace modern figures with old-style figures.
• opbd (optical bounds): a feature that plays the same role as the opbd table in AAT (see
§D.11.7), i.e., to align the glyphs according to their contours rather than their abstract
boxes (their origin, at the left, and their set-width, at the right). It calls two internal features: lfbd (when the glyph appears at the beginning of a line) and rtbd (when it comes
at the end of a line).
• ordn (ordinals): cause the number to be interpreted as an ordinal rather than as a cardinal. In other words, replace ‘2’ with ‘2nd’ in English, ‘2e’ in French, ‘2.’ in German, ‘2οP’
in Greek, etc. Use in moderation: the font is unable to decide whether what follows is
masculine or feminine. Thus how can we obtain ‘1er’ and ‘1re’ in French? The situation
is even more complicated in Greek because ordinals are declined: ‘2οP’, ‘2ου’, ‘2A’, ‘2ον’,
‘2ε’, etc. Therefore, do not rely on the font to choose the right form!
• ornm (ornaments): help the user to enter ornamental glyphs. Two different approaches are
covered: either the user enters a bullet and the system shows him a palette of ornamental
glyphs (which is appropriate for interactive use) or the user enters ASCII characters that
the system proceeds to replace with ornamental glyphs according to a given transcription.
• pcap (petite capitals) replace lowercase letters with “petite capitals” (special small capitals
that are smaller than the ordinary small capitals), which we saw above in the discussion
of the feature c2pc.
• pnum (proportional figures): use figures whose set-widths may be unequal; the approach is
more aesthetically appealing but less useful when setting bills or balance sheets, where
the figures absolutely must be aligned.
• rand (randomize): the font is supposed to contain some slightly different glyphs that the
system can select at random when this feature is enabled. The author cannot resist pointing out that in PostScript it is the printer that performs this selection: in particular, that
is how the fonts Punk [41], Beowolf [86], and Tekla [118] work.
• rlig (required ligatures): produce only the strictly essential ligatures—for instance, in Arabic, the lam-alif O or the special lam-lam-ha that is used to write the name of Allah (P-).
Should be enabled by default.
• salt (stylistic alternatives): obtain variants that cannot be classified either as historical or
as calligraphic.

Appendix D : The TrueType, OpenType, and AAT Font Formats
• sinf (scientific inferiors): replaces figures at text size with figures at a smaller size that are
moved downward for use as subscripts.
• size (optical size): this feature is a notorious hack to enter information on optical size
into a font. Adobe asks us to include this feature in a GPOS table, but without associating
it with any lookup. This table contains the optical size and perhaps also the ranges of
optical sizes at which the font may be used.
• smcp (small capitals): replace lowercase letters with small capitals. Not to be confused with
c2sc, which replaces capitals with small capitals.
• ss01 to ss20 (stylistic sets 1–20): gives the user another way to obtain variant glyphs.
• subs (subscript): replaces a glyph at text size with the same glyph as a subscript. Not to be
confused with sinf, which places the glyph in subscript position—i.e., slightly below the
baseline.
• sups (superscript): replaces a glyph at text size with the same glyph as a superscript.
• swsh (swash): presents a palette for selecting calligraphic variant glyphs.
• titl (titling): replaces ordinary capitals with capitals customized for use in titles.
• tnum (tabular figures): replaces proportional figures with glyphs of uniform space, which
are more suited for use in accounting, in which the figures must be aligned.
D.10.2.2
Features specific to the Semitic scripts
• curs (cursive positioning): connects the letters in the cursive scripts, such as Arabic.
• falt (final glyph on line alternatives): select a variant glyph adapted for use at the end of
a line.
• fin2 and fin3 (terminal form #2/#3): these features are used only to change the shape of
the Syriac letter alaph in the Serto script when this letter is preceded by dalath or rish, with
or without a dot.
The reader must be wondering what could justify two features that apply to only one
letter.
Here is the situation. In the Syriac Serto script, the letter alaph can have two isolated
forms: the curvilinear shape Y and the upright shape X . The author has long attempted
(see [160]) to find the rules that determine how this letter is to be written. Here are his
conclusions: (a) the curvilinear form is used at the beginning of a word and the final form
in the middle and at the end of a word; (b) the curvilinear form is used in the middle or
at the end of a word when it is preceded by the letter rish (\), dalath (Z), or waw (_). All is
well so far. But the author has found several exceptions in the dictionaries: oar \]^ “air”,
diabol b`Xe “devil”, daro XdX[ “combat”, etc. Therefore the form that this letter should take
is by no means clear, and it is better to have a feature that supports easy switching from
one form to the other.

D.10. Predefined Features, Languages, and Scripts
• fina (terminal forms): select a glyph variant suited for use at the end of the word. Essential
in Arabic, where the final form of a letter is obtained.
• init (initial forms): select a glyph variant suited for the beginning of a word. Essential in
Arabic, where the initial form of a letter is obtained.
• isol (isolated forms): select a glyph variant suited for an isolated letter. Essential in Arabic,
where the isolated form of a letter is obtained.
• medi (medial forms): select a glyph variant adapted to a letter in the middle of a word.
Essential in Arabic, where the medial form of a letter is obtained.
• med2 (medial form #2): change the glyph for the letter alaph in the Serto script when the
preceding letter cannot be connected to it. Should be enabled by default.
• mset: place diacritical marks over Arabic letters. This feature applies only to Microsoft
fonts under Windows 95.
• rtla (right-to-left alternatives): replaces left-to-right glyphs with their right-to-left counterparts. For example, the parentheses, brackets, braces, and other delimiters will be shown
in mirror image.
D.10.2.3
Features specific to the scripts of Inda and Southeast Asia
• abvf (above-base forms): In scripts such as Khmer, there are often vowels in two parts, of
which one is anteposed (placed to the left of the consonant to which the vowel applies)
and the other is placed over the consonant in the manner of a diacritical mark. The second of these two components is the one produced by this feature. For example, according
to Unicode notation, the vowel oe in Khmer is written L; applying it to the consonant
cho P yields MQ. The feature abvf allows us to obtain the part O of this vowel. Should be
enabled by default.
• abvs (above-base substitutions): replaces a base glyph bearing an upper diacritical mark
with a ligature, when appropriate. Should be enabled by default.
• akhn (akhand = “unbreakable” in Hindi) produces the independent ligatures for every
context in the scripts of India. In Devanagari, for example, when a ka (;) with no vowel
is followed by a ssa (=), the ligature kssa (>) is obtained; likewise, when a ja (5) with no
vowel is followed by a nya (?), the ligature jnya (@) is obtained. Should be enabled by
default.
• blwf (below-base forms): obtain the subscript form of a consonant in a consonant complex.
In Khmer, for example, if the consonant nno R with no vowel is followed by nyo (S), the
latter assumes its subscript form, and the overall result is U (nnnyo). Should be enabled
by default.
• dist (distances): manages distances between the glyphes in the languages of India.

Appendix D : The TrueType, OpenType, and AAT Font Formats
• half (half forms): produces the half-forms of the Indian consonants. What is a half-form?
In the languages of India, the consonants by default include an inherent short vowel ‘a’
(thus the written form “prtk” is pronounced “parataka”). When several consonants with
no intervening vowel must be pronounced, a number of orthographic subterfuges are
used to indicate the absence of an inherent vowel. One of these subterfuges is the “halfform”: only half of the consonant is written. Examples: in Devanagari, the half-form of
the consonant ja (5) is 6; that of the consonant kha (7) is 8, and so forth.
• haln (halant forms): replace an Indian consonant with its special form lacking an inherent
vowel. In Devanagari, for example, the form of nga (9) that lacks a vowel is written :. It
involves the mere addition of a virama (<), but specially designed glyphs are often used,
for aesthetic reasons.
• nukt (nukta): In the scripts of India, a diacritical mark called nukta. The role of this sign,
which is shaped like a dot, is to indicate a new letter whose pronunciation differs from
that of the original letter. For example, the letter ka (A) becomes qa (B) when this sign
is applied to it, and that is what this feature does. That said, since Unicode does provide
letters with nukta, the author believes that the responsibility for producing them lies with
the keyboard rather than the font.
• pref (pre-base forms): In the languages of India and Southeast Asia, there are letters that
are placed before a group of consonants even though they logically (and phonetically)
come afterwards. This feature allows us to obtain the anteposed form of a letter. For
example, Khmer has the consonant ro (V) (not to be confused with the vowel e [M]). The
consonant cho (P) without a vowel, followed by ro (V), yields WP (chro): ro here has assumed its anteposed form. Should be enabled by default.
• pres (pre-base substitutions): like the feature pref, except that a ligature is produced between the two glyphs, rather than simply a more appropriate form of the first glyph. For
example, the consonant nga (9) with no vowel, followed by the consonant ma (C), gives
the spectacular form D (ngma).
• pstf (post-base forms): In the languages of India and Southeast Asia, some letters have a
special form when they follow a group of consonants. This feature produces that form.
• psts (post-base substitution): like the feature pstf, except that a ligature of the two glyphs
is produced rather than merely a more appropriate form of the second glyph.
• rphf (reph form): In the languages of India and Southeast Asia, this feature produces the
special form of a consonant preceded by the letter ‘r’ (with no vowel). For example, ra (K)
with no vowel, followed by ka (;), yields rka (J), and that is what this feature does.
D.10.2.4
Features specific to the ideographic languages
• ccmp (glyph composition/decomposition): decompose a glyph in order to reconstitute it in
a way more suited to interaction with other glyphs, diacritical marks, etc. For example,
separate the dots of the Arabic letters and replace them as indicated in the GPOS table,
or, even more spectacularly, produce Korean syllables from hangul letters (see the ljmo
feature).

D.10. Predefined Features, Languages, and Scripts
• expt (expert forms). No, this has nothing to do with Adobe’s “Expert” font encodings; it
is a set of Japanese ideographic glyph variants [239] that are needed in printing but that
are not covered by Unicode.
• fwid (full widths): write with
letters
as
wide
as
the
ideographs. This “modified” Latin script is quite useful in the ideographic
countries for aligning Latin, Cyrillic, and Greek letters with ideographs. Should be disabled by default.
• hkna (horizontal kana alternatives): use kana that were specially designed for horizontal
typesetting. Should be disabled by default.
• hngl (hangul): replace Chinese ideographs with the Korean phonetic hangul script. For
instance, 漢字will become 한글, etc. Since the choice is not always unique, the application should be able to offer the user a list of the possible choices.
• hwid and halt (half width and alternative half widths): set type in half-width characters in
the ideographic languages—either in “modified Latin” as illustrated by these few
words or in katakana カタカナ. The halt offers the user a second list of possible glyphs.
• jp78, jp83, jp90 (JIS78/JIS83/JIS90 forms): offer the user some variants of ideographic
glyphs that are based on the JIS C 6226-1978, JIS X 0208-1983, and JIS X 0208-1990 standards. These features aim to make up for the shortcomings of Unicode: when the ideographic glyphs were unified, it was not possible to envision all the variants of each glyph.
But in some branches of publishing, such as dictionaries, history, and geography, these
variants are indeed needed. To use them, one selects the nearest Unicode character and
employs features of this type to obtain the desired variant. See [239] for more details.
• ljmo, vjmo, tjmo (leading, vowel, trailing jamo). The Korean hangul script works as follows:
a syllable is made from a group of consonants, a possible group of vowels, and a possible
second group of consonants. These three groups of letters are combined in an ideographic
square. Example: the consonant ‘p’ (Ä) followed by the vowel ‘˘o’ (ä) and the consonant ‘m’ (Ü) produces the syllable ‘p˘om’ (â). In general, all of the syllables required for
modern Korean are supplied in Unicode and also in fonts. But to write Old Korean, one
must sometimes combine letters explicitly. The features ljmo, vjmo, and tjmo are used
to give each group of letters its status of “first group of consonants”, “group of vowels”,
“second group of consonants”. Finally, through the feature ccmp, these three groups are
combined into one syllable. As an example (specially concocted by the author according
to [267]), let us take as the first group of consonants the letters ‘p’ (Ä), ‘s’ (Å), and ‘t’ (Ç),
and apply the feature ljmo to it; then let us take the group of vowels ‘o’ (É) and ‘ye’ (Ñ)
and apply vjmo to it; finally, let us take as the second group of consonants ‘l’ (Ö), ‘m’ (Ü),
and ‘h’ (á) and apply the feature tjmo to it. In conclusion, let us apply the feature ccmp
to the full set of eight letters, bake for a few milliseconds, and observe the result: the
astonishing syllable pstoyelmh (à)!
• nlck (NLC kanji forms): like the features expt, jp78, jp83, and jp90, this one yields
Japanese ideographic glyph variants.

Appendix D : The TrueType, OpenType, and AAT Font Formats
• pwid and palt: (proportional [alternate] widths): When we set text in the Latin alphabet within an ideographic context, this feature switches from full-width
Latin
letters or half-width Latin letters to the Latin letters that
we know and love—i.e., letters with “proportional widths”. The “alternative” feature
gives us a variant of these glyphs.
• qwid (quarter widths): set type in quarter-width characters in the ideographic languages—
using either “modified Latin” as illustrated by these few words or katakana カタカナ. For timid authors.
• ruby (ruby notation forms): Ruby characters, or furigana, are phonetic (or other) annotations used in Japanese, notably to enable children and adolescents to read books with
ideographs that they have not yet learned at school. Here is an example of ideographs
with ruby characters:
k
日
{ì
本
T
語の
Ç
文
X
字(nihon-go-no moji, “Japanese characters”). Given the
small size of these glyphs, we are wise to use variants that have been optically customized,
and that is what this feature does: it chooses glyph variants that are suited for use as ruby
characters.
• smpl (simplified forms): replace the traditional forms of Chinese and Japanese ideographs
with simplified forms.
• tnam (traditional name forms): offers a range of traditional Japanese ideographs that are
variants of the selected ideograph. These variants are used especially for proper names,
especially surnames.
• trad (traditional forms): replace the simplified forms of Chinese and Japanese ideographs
with their traditional forms. If necessary, offer the user a selection of various choices.
• twid (third widths): compose type in the ideographic languages at one third of the standard width—using either “modified Latin” as illustrated by these few words or katakana カタカナ.
For authors less timid than those who use quarter-width characters, but timid nonetheless.
D.11
General AAT Tables
Apple [56] has defined 17 TrueType tables that for now are used only under Mac OS X. These
tables are known by the name “AAT” (= Apple Advanced Typography). We shall divide them
into three groups.
The first group, to which this section is devoted, contains eight various and sundry tables. The
second group, with five tables, is dedicated to fonts with variation, a concept close to Multiple
Master. Finally, the third group, with four tables, contains the big guns of the AAT tables—
i.e., tables for positioning, substitution, and justification; they use finite automata to do their
task, which makes them very powerful—and very difficult to design.
But let us begin with the relatively simple tables: acnt, bsln, fdsc, feat (with the list of predefined AAT features), lcar, opbd, prop, trak, and Zapf.

```text
D.11. General AAT Tables
D.11.1
The acnt Table
This table’s name comes from the word “accent”. In fact, it is a table for describing composite
glyphs, in the same vein as AFM files (§C.3.7) or the virtual fonts of TEX (§B.3). Composite
glyphs consist of a base glyph (here called the primary glyph) and one or more combining
glyphs (here called secondary glyphs). The table contains the names of the glyphs in question
and their relative positions.
Rather than giving a global offset for the combining glyph (as in AFM files or TEX virtual
fonts), the acnt table adopts a more efficient strategy that is also closer to the type 4 lookups
of the GPOS table: a point on the base glyph’s contour and a point on the combining glyph’s
contour are selected, and the second glyph is moved so that the points coincide.
The benefit of this method is that it takes into account the TrueType instructions that may
move the points in question. It thus offers better control over the positioning of diacritical
marks at any size.
Here is an example of one such table:
&lt;acnt&gt;
&lt;Version value="1"/&gt;
&lt;Glyph value="Aacute" format="0"&gt;
&lt;primaryGlyph value="A"/&gt;
&lt;secondaryGlyph index="0" value="acute"&gt;
&lt;primaryAttachmentPoint value="24"/&gt;
&lt;secondaryAttachmentPoint value="7"/&gt;
&lt;/secondaryGlyph&gt;
&lt;/Glyph&gt;
...
&lt;/acnt&gt;
The acnt element contains an element for the version and one Glyph element for each composite glyph in the table. Each Glyph element has two attributes: value, which gives the name
of the composite glyph, and format, which is 0 if there is only one diacritical mark or 1 if there
are more than one.
The Glyph element contains an element primaryGlyph, whose value attribute gives the
name of the base glyph, and one secondaryGlyph for each glyph that combines with the
baes glyph to form the composite glyph. Each secondaryGlyph takes a value attribute,
which contains the name of the combining glyph and has two elements: the numbers of the
points of attachment on the base glyph (primaryAttachmentPoint) and the combining glyph
(secondaryAttachmentPoint). The number of the point of attachment on the base glyph is
repeated in each secondaryGlyph, for the simple reason that this point can be different for
each combining glyph.
D.11.2
The bsln Table
This table’s name comes from the word baseline. It attempts to solve the same problem as the
BASE table of OpenType: the possibility of having several baselines, according to the type of
script. The figure below (taken from page 754):
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
I’m based
illustrates the situation for the BASE table of OpenType. In it, we see three types of script
(Latin, ideographic, Tibetan), with three different baselines. Here, in the case of bsln, the
approach to the ideographic script is different: the ideographic baseline is considered to run
through the middle of the glyphs. Therefore we have redrawn this figure with regard to the bsln
table:
➀
➁
➃
➂
I’m based
Here we see:
1. English, for the “Latin” baseline (number 0).
2. Japanese typeset so as to be consistent with the English, i.e., moved slightly downward.
Since the baseline here is considered to run through the middle of the glyphs, the baseline appears at the location indicated in the figure. This baseline (number 2) is called the
“ideographic baseline”.
3. More Japanese, this time on the Latin baseline. Here the baseline that runs through the
middle of the ideographs (number 1) is called the “central ideographic” line. This baseline is used in documents containing nothing but ideographs (or characters assimilated
to ideographs—do not forget that Asian fonts and encodings contain Latin glyphs and
characters, respectively, that have the exact dimensions of the ideographs and that are
typeset in the same way).
4. Tibetan, using a “hanging” baseline (number 3).
What is missing from this figure is a fifth “baseline”, the axis for the vertical centering of
mathematical symbols: ‘=’, ‘+’, ‘−’, ‘∗’, ‘⊗’, ‘⊕’, ‘◦’, etc.
AAT supposes that we can, in theory, have up to 32 baselines. But do not plan to define any
others: only the five described above are permitted; the other 27 are reserved by Apple.
There are four formats for the bsln table: in Format 0, the baselines apply to all the glyphs in
the font and are defined by y-coordinates expressed in TrueType units; in Format 1, they are
again defined by y-coordinates but can take different values for each glyph; in Format 2, they
are defined with points on the contour of a model glyph and take the same value for every
glyph; finally, Format 3 combines formats 1 and 2: the baselines are defined by points on the
contour of a model glyph and can take different values for each glyph.
Here is an example of a bsln table of format 0:
&lt;bsln&gt;
&lt;Version value="1"/&gt;
&lt;baselines format="0"&gt;
&lt;defaultBaseline value="0"/&gt;
```

```text
D.11. General AAT Tables
&lt;deltas&gt;
&lt;delta index="0" value="0"/&gt;
&lt;delta index="1" value="352"/&gt;
&lt;delta index="2" value="352"/&gt;
&lt;delta index="3" value="705"/&gt;
&lt;delta index="4" value="352"/&gt;
&lt;/deltas&gt;
&lt;/baselines&gt;
&lt;/bsln&gt;
After the customary Version, we find a baselines element, which contains the data for the
table. Its format attribute gives the table’s format. In baselines, we find an element defaultBaseline. This element allows us to select the font’s default baseline. Since we are using
Format 0, the rest of the content of baselines is a single element: deltas. This element
contains the descriptions of the different baselines. These descriptions consist of delta (with
no ‘s’) elements whose value attributes are the distances between the lines in question and
the default baseline. (The name “delta” comes from the fact that the values are not absolute
coordinates but rather offsets from the default value).
Format 1 adds, after the end of the deltas, a Glyphs element, like this:
&lt;Glyphs&gt;
&lt;Glyph value="A" baseline="0"/&gt;
&lt;Glyph value="B" baseline="0"/&gt;
&lt;Glyph value="C" baseline="0"/&gt;
...
&lt;/Glyphs&gt;
This element contains, in the form of attributes, the glyph names and baselines associated
with each glyph. The value of the baseline attribute corresponds to the value of the index
attribute of the element delta.
Format 2 resembles Format 0, but instead of delta elements there are ctlPoint elements:
&lt;bsln&gt;
&lt;Version value="1"/&gt;
&lt;baselines format="2"&gt;
&lt;defaultBaseline value="0"/&gt;
&lt;stdGlyph value="P"/&gt;
&lt;ctlPoints&gt;
&lt;ctlPoint index="0" value="34"/&gt;
&lt;ctlPoint index="1" value="35"/&gt;
&lt;ctlPoint index="2" value="35"/&gt;
&lt;ctlPoint index="3" value="36"/&gt;
&lt;ctlPoint index="4" value="35"/&gt;
&lt;/ctlPoints&gt;
&lt;/baselines&gt;
&lt;/bsln&gt;
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
But it is not enough to give the numbers of points on the contour: we must also specify
the glyph in which the points appear. That is the role of the element stdGlyph. The value
attributes of the ctlPoint elements contain the numbers of points on the contour of the
glyph in question. Finally, Format 3 contains in addition the Glyphs element that we saw
in Format 1.
D.11.3
The fdsc Table
The idea behind this table, whose name is an abbreviation of font descriptor, is to classify the
font so that a suitable substitute can be found. For example, the user selects a block of text in
the font and specifies a different font family. The system will then select the individual fonts
from that font family that most closely match the characteristics of the text itself.
The table is a small one: it merely supplies some general information on the font—information
that also appears in part in OS/2, head, and elsewhere. Here is an example of this table:
&lt;fdsc&gt;
&lt;Version value="1"/&gt;
&lt;descriptors&gt;
&lt;descriptor tag="wght" value="0.8"/&gt;
&lt;descriptor tag="wdth" value="1.0"/&gt;
&lt;descriptor tag="slnt" value="0"/&gt;
&lt;descriptor tag="opsz" value="10"/&gt;
&lt;descriptor tag="nalf" value="3"/&gt;
&lt;/descriptors&gt;
&lt;/fdsc&gt;
The descriptors element contains descriptor elements (with no ‘s’). Each descriptor contains one piece of data on the font; it has a “name”, which is the value of the tag, and a value.
Here are the descriptors defined by Apple: wght is the font’s weight relative to the standard
weight of the “font family” (1 by default), wdth is the font’s width relative to the standard
width (1 by default), slnt is the slant (measured clockwise in degrees), opsz is the optical
size (in American printers’ points), and nalf is a classification of the font as “alphabetic”
(value 0), “dingbats” (1), “pi characters” (i.e., symbol fonts such as Symbol; value 2), “fleurons” (3), “decorative borders” (4), “international symbols” (5), “mathematical symbols” (6).
The specification provides no other explanation in the specification on the difference between
“pi characters” and “mathematical symbols” or on the meaning of “international symbols”
(are they internationally recognized symbols, such as the pictograms that we see in airports,
or simply the glyphs of non-Latin scripts?).
D.11.4
The fmtx Table
One more small table that makes up, to some extent, for the absence of the concept of “device
table” that we have in OpenType. The question at issue here is “The tables head, OS/2, etc.,
give us explicit values; what would happen if the TrueType instructions changed these values
for certain font sizes?”
In the OpenType context, we had “device tables”. AAT offers something simpler: We select a
glyph as our model. For each relevant dimension in the font, we select a point on the model
```

```text
D.11. General AAT Tables
glyph whose x-coordinate or y-coordinate will serve as a reference for us. Then the relevant
dimensions of interest to us will develop according to the wishes of the TrueType instructions.
Note that this model glyph may very well be an ad hoc glyph whose only reason for existence
is to be a model for the behavior of other glyphs—an attitude worthy of the Tibetan monks.
Here is an example of one such table:
&lt;fmtx&gt;
&lt;Version value="1"/&gt;
&lt;glyphIndex value="X"/&gt;
&lt;horizontalBefore value="15"/&gt;
&lt;horizontalAfter value="17"/&gt;
&lt;horizontalCaretHead value="29"/&gt;
&lt;horizontalCaretBase value="29"/&gt;
&lt;verticalBefore value="15"/&gt;
&lt;verticalAfter value="19"/&gt;
&lt;verticalCaretHead value="31"/&gt;
&lt;verticalCaretBase value="29"/&gt;
&lt;/fmtx&gt;
The element glyphIndex gives us the model glyph. We shall use the points on this glyph and
their offsets under the influence of the instructions in order to obtain the dimensions of interest to us. There are eight of them: horizontalBefore indicates the height of the ascenders,
horizontalAfter indicates the depth of the descenders, horizontalCaretHead indicates the
size of the cursor, horizontalCaretBase indicates its depth. The word “horizontal” is a bit
jarring because its values represent both height and depth; in fact, its name refers rather to
the direction of typesetting. The same concepts exist in vertical typesetting; the names of the
corresponding elements begin with vertical. Note that when we say “height of ascenders”
and “depth of descenders” we refer not to the exact values but rather to values given by the
designer that are used for the management of leading.
D.11.5
The feat Table
Could it be rivalry between Apple and Adobe/Microsoft? Or proof that universal truth exists?
Whatever the case may be, it is a fact that both OpenType and AAT share the concept of a
feature. We described the features of OpenType in §D.10.2; in this section, we shall describe
the features of AAT.
But AAT features have two flagrant disadvantages, and we may as well mention them right
away: AAT features are flexible and easy to use. Specifically, AAT features have selectors: series
of properties specific to each, which the user enables or disables upon selecting the feature.
On the other hand, their names are not vulgar four-letter ASCII strings, like those of the
OpenType features, but namerecords from the name table—which means that the designer
can translate the name of a feature into every language and script in the world! OpenType
can only dream of such richness.19
19 The reader must be wondering why the author is so hostile. Well, first of all, what he is exhibiting is not
hostility but anger. And the reason is as follows: the fact that OpenType features are described by four-letter
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
But before describing the features, let us say a few words about the feat table, whose role is
to list their names.
Here is an example of one such table:
&lt;feat&gt;
&lt;Version value="1"/&gt;
&lt;FeatureNames&gt;
<!-- featureNameCount=3 -->
&lt;FeatureName nameIndex="260" index="0" code="0"
exclusiveSettings="0" defaultSetting="0">
<!-- nSettings=1 -->
&lt;Setting code="0" nameIndex="261"/&gt;
&lt;/FeatureName&gt;
&lt;FeatureName nameIndex="262" index="0" code="3"
exclusiveSettings="1" defaultSetting="0">
<!-- nSettings=1 -->
&lt;Setting code="0" nameIndex="268"/&gt;
&lt;Setting code="3" nameIndex="264"/&gt;
&lt;Setting code="4" nameIndex="265"/&gt;
&lt;/FeatureName&gt;
...
&lt;/FeatureNames&gt;
&lt;/feat&gt;
The element that follows Version and that contains all the data is FeatureNames. It contains
a FeatureName (with no ‘s’) for each feature that exists in the font. Each FeatureName has five
attributes: its number (index); the number of the corresponding namerecord in the name table
that contains the name of the feature (nameIndex); the feature’s “code”—i.e., its number in
the official list of Apple features that we shall present below (code); an indication of whether
or not the selectors for the feature should be exclusive (exclusiveSettings), the difference
being that if they are exclusive, the user interface will represent them with radio buttons, and
if they are not exclusive, they will be represented with checkboxes; and the number of the
selector that is enabled by default (defaultSetting).
Each FeatureName contains a Setting element for each selector. A Setting selector is described by three attributes: index gives its number among the feature’s selectors; code gives
its number in the official list of AAT features, which we shall see below; and nameIndex gives
the number of the namerecord in the name table that contains its name, in all possible and
imaginable languages.
tags, which by definition are incomprehensible to the ordinary user; Adobe has used this fact as an excuse for
including only a few predefined features in the user interface to Adobe InDesign, thus completely and inexorably
disregarding all the marvelous features that the designer might have included in a font.
In this book, we have learned how to create fonts with new features; yet Adobe InDesign does not allow us to
use those features, simply because it considers their four-letter names unseemly. And that situation is likely
to continue, because OpenType makes no provision for assigning to these unfortunate features names that are
more legible and better adapted to localizable user interfaces. As if the name had not existed since the very
beginning of the TrueType format. Therefore, long live AAT!
```

D.11. General AAT Tables
Let us move on now to the comprehensive list of AAT features, as of late 2006. (On its web
site, Apple has warned us that the list is a “dynamic list”, but the last update was made in
May 1998.).
D.11.5.1
The AAT features
For each feature, we present below its “official” name (in fact, it is the name given in the code
for Apple’s API [58]) and its code number.
The selectors with an On in their name are always accompanied by opposite selectors that
disable the property in question. For example, a selector called SomethingOnSelector (code n)
is always accompanied by a selector SomethingOffSelector (code n+1), which we shall omit
in the following discussion.
• AllTypographicFeaturesType (code 0): all the features. This is “all or nothing”. There is
only one selector:
– AllTypeFeaturesOnSelector (code 0): all the features are enabled.
• LigaturesType (code 1): ligatures. Certain types of ligatures are enabled. Here are the
selectors:
– RequiredLigaturesOnSelector (code 0): enables the ligatures that are absolutely
necessary for the active language, such as simple connections of Arabic letters.
– CommonLigaturesOnSelector (code 2): enables the most common ligatures, such as
the f-ligatures for the Latin alphabet.
– RareLigaturesOnSelector (code 4): enables the less common ligatures, such as ‘ft’
or ‘yy’.
– LogosOnSelector (code 6): enables the ligatures that produce logos: for example, the
font may systematically replace “O’REILLY” with the logo of this illustrious publishing house,
.
– RebusPicturesOnSelector (code 8): according to the dictionary, a rebus is a pictographic character that designates an object by its shape or by the sound associated with the
word that it depicts. This selector enables rebuses.
– DiphthongLigaturesOnSelector (code 10): enables “diphthongs”, i.e., the letters ‘Æ’,
‘Œ’, etc.
– SquaredLigaturesOnSelector (code 12): enables the ligatures used in the ideographic scripts, such as ㌖(kiromeetoru, or “kilometer”), ㍿(kabushiki-gaisha, or
“corporation”), ㍬. (“8:00 pm”), ㏯. (“the 16th day of the month”), etc.
– AbbrevSquaredLigaturesOnSelector (code 14): another type of ideographic ligatures that packs Latin letters like sardines into the famous ideographic square. Here
are some typical examples: ㎢, ㏒, ㎒, ㎯, etc.
– SymbolLigaturesOnSelector (code 16): enables ligatures that have become symbols,
such as ‘lb’, the symbol for the pound (approx. 453 grams), etc.
• CursiveConnectionType (code 2): cursive script with connected letters. Applies to both Arabic and calligraphic Latin scripts. Its selectors:

Appendix D : The TrueType, OpenType, and AAT Font Formats
– UnconnectedSelector (code 0): everything is disconnected
– PartiallyConnectedSelector (code 1): some, but not all, letters are connected
– CursiveSelector (code 2): all the letters that can be connected are connected
• LetterCaseType (code 3): change of case, for scripts that do have this property (the Latin,
Greek, Cyrillic, Armenian, and old Georgian alphabets). The selectors correspond to the
various types of case that are available:
– UpperAndLowerCaseSelector (code 0): uppercase and lowercase letters are mixed,
and the user’s choice of case is respected
– AllCapsSelector (code 1): everything is shown in capitals
– AllLowerCaseSelector (code 2): everything is shown in lowercase letters
– SmallCapsSelector (code 3): everything is shown in small capitals
– InitialCapsSelector (code 4): everything is shown in lowercase letters except the
first letter of each word, which is changed to uppercase (thanks to finite automata,
we can define with a great deal of precision what is a word and what is not)
– InitialCapsAndSmallCapsSelector (code 5): everything is shown in small capitals
except the first letter, which is changed to uppercase
• VerticalSubstitutionType (code 4): choice of glyph for vertical typesetting. When type is
set vertically, some glyphs change their shape. For instance, the parentheses, brackets,
braces, and other delimiters are turned 90 degrees. There is only one selector:
– SubstituteVerticalFormsOnSelector (code 0): selects the glyphs customized for
vertical typesetting
• LinguisticRearrangementType (code 5): rearrangement of glyphs for grammatical reasons.
In some languages of India or Southeast Asia, the glyphs are not displayed in their logical
or phonetic order. In the example below:
+
+
h(a)
r(a)
ei
ei
r
h
This is set in the Khmer font Moul, which was designed by the author [159]. The consonants h(a) and r(a), and the vowel ei, are shown at the left. At the right, the three letters
combined yield hrei phonetically, although graphically the ei comes first and is followed
by r(a) and then h(a). This is the sort of behavior that this feature controls. There is only
one selector:
– LinguisticRearrangementOnSelector (code 0): enables the grammatical rearrangement of the glyphs

D.11. General AAT Tables
• NumberSpacingType (code 6): choice of monospaced digits. This feature allows us to choose
between digits of variable width and digits of fixed width. The latter are useful in tables
of numbers, in which all figures must be aligned. Two selectors:
– MonospacedNumbersSelector (code 0): digits of fixed width.
– ProportionalNumbersSelector (code 1): digits of variable width.
– ThirdWidthNumbersSelector (code 2): digits of two-thirds width: 1, 2, 3, 4.
– QuarterWidthNumbersSelector (code 3): digits of one-quarter width: 1, 2, 3, 4. This is
extremely narrow. Of what good is it? Perhaps it can be used to display astronomical
numbers: “I won 100,000,000 cents in the lottery!”
• SmartSwashType (code 8): management of calligraphic variants. When these selectors are
enabled, the context will enable or disable certain calligraphic glyph variants. Five selectors:
– WordInitialSwashesOnSelector (code 0): enables the variants at the beginning of a
word (once again, the finite automata allow us to define precisely which glyphs form
words)
– WordFinalSwashesOnSelector (code 2): ditto, but at the end of a word
– LineInitialSwashesOnSelector (code 4): ditto, but at the beginning of a line
– LineFinalSwashesOnSelector (code 6): ditto, but at the end of a line
– NonFinalSwashesOnSelector (code 8): enables the variants that do not occur at the
end of a word
• DiacriticsType (code 9): display of diacritical marks.
– ShowDiacriticsSelector (code 0): the marks are displayed as usual
– HideDiacriticsSelector (code 1): the marks are completely hidden
– DecomposeDiacriticsSelector (code 2): rather than combining them with letters,
they are shown at the side, as independent glyphs
• VerticalPositionType (code 10): management of superscripts and subscripts. The name
“vertical position” may lead one astray: in fact, it refers to converting a glyph into a superscript or a subscript, as the font allows. The selectors:
– NormalPositionSelector (code 0): neither superscripts nor subscripts
– SuperiorsSelector (code 1): superscripts
– InferiorsSelector (code 2): subscripts
– OrdinalsSelector (code 3): like a superscript, but often it requires something else,
such as the Spanish a and o
• FractionsType (code 11): automatic fractions. There are two techniques for obtaining
beautiful fractions: either predefined glyphs for fractions are used, or the fraction bar is
combined with superscript and subscript digits to construct the fraction.
– NoFractionsSelector (code 0): no automatic construction of fractions

Appendix D : The TrueType, OpenType, and AAT Font Formats
– VerticalFractionsSelector (code 1): uses the font’s precomposed fractions
– DiagonalFractionsSelector (code 2): fractions obtained with a superscript, a fraction bar, and a subscript
• OverlappingCharactersType (code 13): prevents collisions. This features helps us to prevent collisions of glyphs with protruding elements. Only one selector:
– PreventOverlapOnSelector (code 0): prevents collisions
• TypographicExtrasType (code 14): automatic application of typographic conventions . Some
software already handles this: for example, to obtain an em dash, the user enters two hyphens, and the software automatically performs the substitution. Here are the selectors
for this feature:
– HyphensToEmDashOnSelector (code 0): two hyphens yield an em dash.
– HyphenToEnDashOnSelector (code 2): a hyphen between two spaces or between two
digits becomes an en dash.
– SlashedZeroOnSelector (code 4): use a zero with a slash through it (as is done in
some fonts used to display computer code in order to distinguish the zero from the
letter ‘O’, but there is a risk of confusion with the empty set, /0, and the Scandinavian Ø).
– FormInterrobangOnSelector (code 6): The year 1962 saw the birth of not only the
author but also a bizarre punctuation mark: the interrobang [320], shown here: ‘!?’.
This feature replaces the strings !? and ?! with this beast.
– SmartQuotesOnSelector (code 8): replaces computer-style quotation marks (also
known as “straight quotes” or “double quotes”) with proper English quotation
marks.
– PeriodsToEllipsisOnSelector (code 10): replaces the string “...” with an ellipsis as
used in English-language typography.
• MathematicalExtrasType (code 15): assistance with mathematical typesetting. Automated
typesetting mechanisms specializing in mathematical typesetting. Here are the selectors:
– HyphenToMinusOnSelector (code 0): a hyphen between two spaces or between two
digits becomes a mathematical minus sign.
– AsteriskToMultiplyOnSelector (code 2): an asterisk between two spaces is replaced
by the multiplication sign, (×). Handle with care, since the asterisk is also (rarely, it
is true) used in mathematics as an operator.
– SlashToDivideOnSelector (code 4): the slash between two spaces becomes the division sign, (÷).
– InequalityLigaturesOnSelector (code 6): replaces the strings ‘<=’ and ‘>=’ with the
symbols ‘≤’ and ‘≥’. A funny choice, since, to the author’s eye, ‘<=’ symbolizes implication (⇐) rather than inequality (≤); but never mind.
– ExponentsOnSelector (code 8): the digit that follows the ASCII caret (^) becomes a
superscript. This is similar to TEX’s convention for superscripts; but then why can we
not have the same thing for subscripts by using an underscore?

D.11. General AAT Tables
• OrnamentSetsType (code 16): selection of special glyphs. This feature dates from the dark
days before Unicode. In that era, it was very difficult to select nonalphabetic glyphs. Apple thus had the following idea: in a font of dingbats or any other font, the glyphs should
be accessible by entering alphabetic characters, and the characters A–Z, etc., are converted
into symbols, dingbats, and so on according to the selector chosen. Here are the selectors:
– NoOrnamentsSelector (code 0): no special glyphs
– DingbatsSelector (code 1): a set of dingbats, or miscellaneous symbols
– PiCharactersSelector (code 2): a set of “pi” glyphs, which are symbols used in various contexts (cartography, hotel management, military medals, etc.)
– FleuronsSelector (code 3): a set of fleurons
– DecorativeBordersSelector (code 4): a set of decorative borders and lines
– InternationalSymbolsSelector (code 5): a set of internationally recognized symbols (road signs, safety, etc.)
– MathSymbolsSelector (code 6): mathematical symbols
• CharacterAlternativesType (code 17): choice among the variants of a glyph. The software
should provide one selector for each variant of a given glyph. Only one selector is predefined:
– NoAlternatesSelector (code 0): no variants
• DesignComplexityType (code 18): choice of calligraphic level. A calligraphic font may have
several variants of each glyph that are arranged as more or less calligraphic forms. The
examples below are drawn from the different levels of the font Zapfino:
– DesignLevel1Selector (code 0):
– DesignLevel2Selector (code 1):
– DesignLevel3Selector (code 2):

Appendix D : The TrueType, OpenType, and AAT Font Formats
– DesignLevel4Selector (code 3):
– DesignLevel5Selector (code 4):
– DesignLevel6Selector (code 5):
– DesignLevel7Selector (code 6):
– DesignLevel8Selector (code 7):
– DesignLevel9Selector (code 8):

D.11. General AAT Tables
• StyleOptionsType (code 19): choice of “style”. For this purpose, “style” means glyphs for
titling, engraved glyphs, illuminated glyphs, etc. The selectors:
– NoStyleOptionsSelector (code 0): no “style”
– DisplayTextSelector (code 1): glyphs customized for large sizes
– EngravedTextSelector (code 2): glyphs set in relief, as if engraved in stone
– IlluminatedCapsSelector (code 3): illuminated glyphs, as in mediaeval illuminated
manuscripts, or like the beautiful romantic dropped capitals of the nineteenth century
– TitlingCapsSelector (code 4): capitals customized for use in titles
– TallCapsSelector (code 5): very tall capitals
• CharacterShapeType (code 20): choice of glyph for a CJK character (where CJK means “Chinese, Japanese, Korean”). We know that Unicode unified the Chinese, Japanese, and Korean ideographs. But when there are several glyphs to represent an ideographic character,
we need a way to gain access to those glyphs, since there will always be a need for particular variants in the different areas of human knowledge: geography, history, surnames, etc.
This feature allows us to select a glyph according to its membership in a set of predefined
glyphs. The selectors:
– TraditionalCharactersSelector (code 0): traditional Chinese ideographs (Taiwan, etc.)
– SimplifiedCharactersSelector (code 1): simplified Chinese ideographs (People’s
Republic of China)
– JIS1978CharactersSelector (code 2): Japanese ideographs, according to JIS C62261978
– JIS1983CharactersSelector (code 3): ditto, but according to JIS X 0208-1983
– JIS1990CharactersSelector (code 4): ditto, but according to JIS X 0208-1990
– TraditionalAltOneSelector (code 5) to TraditionalAltFiveSelector (code 9):
Chinese ideographs, sets 1 to 5
– ExpertCharactersSelector (code 10): Japanese ideographs, according to the Fujitsu
FMR set of glyphs
• NumberCaseType (code 21): choice of digit shapes. Do not be surprised by the name of this
feature. It refers not to the “case of the digits” but rather to old-style and modern figures:
– LowerCaseNumbersSelector (code 0): old-style figures

Appendix D : The TrueType, OpenType, and AAT Font Formats
– UpperCaseNumbersSelector (code 1): modern figures
• TextSpacingType (code 22): choice of glyph spacing. This feature is especially useful for CJK
ideographs. Selectors:
– ProportionalTextSelector (code 0): proportional spacing
– MonospacedTextSelector (code 1): monospaced
– HalfWidthTextSelector (code 2): half width
– NormalTextSelector (code 3): default spacing
• TransliterationType (code 23): phonetic transcription of ideographs. Chinese ideographs
are used in both Japan and Korea, but so are scripts that are specific to those two countries. Japan uses kana: hiragana for Japanese words and katakana for foreign words; Korea
uses hangul. All three are examples of syllabic scripts that are therefore purely phonetic.
In addition, Japan also uses the Latin script (officially recognized as the country’s fourth
script). This feature allows us to switch from one script to another or to give the possible
solutions for switching from the Chinese ideographs in the Korean language to hangul.20
Here are the selectors:
– NoTransliterationSelector (code 0): no phonetic transcription
– HanjaToHangulSelector (code 1): Korean ideographs to hangul; for example, 再會
(chae-hoe, “meeting”) →재회
– HiraganaToKatakanaSelector (code 2): hiragana to katakana; for example, はらら
んぶす→ハラランブス
– KatakanaToHiraganaSelector (code 3): katakana to hiragana; for example, ハララ
ンブス→はららんぶす
– KanaToRomanizationSelector (code 4): kana to Latin script; for example, はららん
ぶす→hararanbusu (the author’s name, pronounced in a Japanese style)
– RomanizationToHiraganaSelector (code 5): Latin script to hiragana; for example,
hararanbusu →はららんぶす
– RomanizationToKatakanaSelector (code 6): Latin script to katatana; for example,
hararanbusu →ハラランブス
– HanjaToHangulAltOneSelector
(code
7)
to
HanjaToHangulAltThreeSelector
(code 9): Korean ideographs to hangul, alternative selections 1 to 3
• AnnotationType (code 24): encircled glyphs, glyphs in parentheses, etc. Selectors:
– NoAnnotationSelector (code 0): no annotation
– BoxAnnotationSelector (code 1): glyphs inside boxes
– RoundedBoxAnnotationSelector (code 2): glyphs in boxes with rounded corners
– CircleAnnotationSelector (code 3): encircled glyphs
– InvertedCircleAnnotationSelector (code 4): ditto, but white on black
20 See [171, p. 161] for an attempt at the automatic transcription into kana of the Chinese ideographs of
the Japanese language.

D.11. General AAT Tables
– ParenthesisAnnotationSelector (code 5): glyphs in parentheses
– PeriodAnnotationSelector (code 6): glyphs followed by a period
– RomanNumeralAnnotationSelector (code 7): numbers written as Roman numerals
– DiamondAnnotationSelector (code 8): glyphs inside diamonds
– InvertedBoxAnnotationSelector (code 9): glyphs inside boxes, white on black
– InvertedRoundedBoxAnnotationSelector (code 10): glyphs inside boxes with rounded
corners, white on black
• KanaSpacingType (code 25): choice of kana spacing. Kana are the Japanese phonetic script.
Since aesthetically they look different from the kanji (Japanese characters of Chinese origin), they are sometimes handled differently. In particular, one can choose to set them
“Western-style”—i.e., with variable widths—while keeping the ideographs enclosed in
their perfect ideographic square. Selectors:
– FullWidthKanaSelector (code 0): “Chinese-style” typesetting of the kana—i.e., at a
fixed width
– ProportionalKanaSelector (code 1): “Western-style” typesetting of the kana (with
variable widths)
• IdeographicSpacingType (code 26): choice of ideographic spacing. We can extend the principle of the previous feature to the ideographs of Chinese origin (han in Chinese, kanji
in Japanese, hancha in Korean). There are three options:
– FullWidthIdeographsSelector (code 0): “Chinese-style”—i.e., at a fixed width
– ProportionalIdeographsSelector (code 1): “Western-style” (with variable widths)
– HalfWidthIdeographsSelector (code 2): “economically”—i.e., at half width
• CJKRomanSpacingType (code 103): width of Latin letters in an ideographic context. We have
already seen what happens to our poor Latin letters in the hands of our East Asian colleagues, as
in
this
sample
of
text. Here is how to
manage the width of this “modified Latin” script:
– HalfWidthCJKRomanSelector (code 0): half width, as in this sample of text
– ProportionalCJKRomanSelector (code 1): normal typesetting
– DefaultCJKRomanSelector (code 2): the default choice
– FullWidthCJKRomanSelector (code 3): full-width Chinese typesetting, like
this
• UnicodeDecompositionType (code 27): choice of Unicode decomposition. If the font does not
contain a certain glyph, we attempt to decompose the Unicode character with which it
is associated. We can decompose it in the canonical manner or in compatibility mode:
– CanonicalCompositionOnSelector (code 0): canonical decomposition
– CompatibilityCompositionOnSelector (code 2): compatibility mode. Example: suppose that the glyph ‘l.’, which is needed for the Catalan digraph “l.l” does not exist;
then it will be replaced with an ‘l’ followed by a mathematical centered dot (as in a·
b).

Appendix D : The TrueType, OpenType, and AAT Font Formats
• RubyKanaType (code 28): Japanese annotation. In Japanese, there is a custom of annotating the ideographs with small glyphs placed above them. Most of the time, these small
glyphs are kana, and therefore the annotation is a phonetic transcription intended for
children and teenagers who do not yet have the education needed to read kanji directly.
Example:
k
日
{ì
本
T
語の
Ç
文
X
字(nihon-go-no moji, “Japanese characters”). These annotations are
called furigana, or ruby. Note that it is essential, from a typographic point of view, that
ruby characters be set in a font that has been optically corrected and customized for their
small size; otherwise the difference in the stroke thicknesses between the ruby characters
and the base characters will be intolerable. Two selectors:
– NoRubyKanaSelector (code 0): without ruby characters
– RubyKanaSelector (code 1): with ruby characters
• CJKSymbolAlternativesType (code 29): choice of CJK symbols. The “CJK symbols” are the
equivalent of our punctuation marks for the ideographic languages. They can have different variants. Selectors:
– NoCJKSymbolAlternativesSelector (code 0): no variants (default glyphs only)
– CJKSymbolAltOneSelector (code 1) to CJKSymbolAltFiveSelector (code 5): variants
1 to 5
• IdeographicAlternativesType (code 30): ideographic variants. More variants of ideographs:
– NoIdeographicAlternativesSelector (code 0): default glyphs
– IdeographicAltOneSelector (code 1) to IdeographicAltFiveSelector (code 5):
variants 1 to 5
• CJKVerticalRomanPlacementType (code 31): behavior of Latin glyphs during vertical typesetting.
– CJKVerticalRomanCenteredSelector (code 0): centered
– CJKVerticalRomanHBaselineSelector (code 1): aligned on the horizontal baseline
• ItalicCJKRomanType (code 32): italics in CJK context. Ideographic fonts usually do not
have any italic Latin letters. The user who wishes to obtain italic letters may use this
feature (if the font does include italics):
– NoCJKItalicRomanSelector (code 0): no italics in an ideographic context
– CJKItalicRomanSelector (code 1): italic Latin letters in an ideographic context
D.11.6
The lcar Table
The lcar table (ligature caret) addresses the problem of placing the mouse’s cursor over ligatures. If a font contains ligatures and therefore replaces individual glyphs with large glyphs
containing several components (i.e., ligatures), that must not be done at the expense of interaction with the user. Specifically, if the user typesets the word “afflicted” and wishes to select
the string ‘fli’, a problem immediately arises, since ‘ffl’ is only one glyph: how can we select
one part of the glyph with the mouse?

```text
D.11. General AAT Tables
The lcar table comes to the rescue: for each ligature, it gives the number of components and
the possible values of the position of the cursor to place between the components. In the
case of ‘ffl’, for instance, lcar will advise the system that there are three components (and
therefore two possible positions for the cursor to be placed within the ligature) and will give
the system the x-coordinates of these cursor positions (or their y-coordinates, if we are setting
type vertically). lcar fulfills the same role as the LigCaretList subtable of the OpenType
table GDEF.
It exists in two formats: in Format 0, the x-coordinates of the cursor positions are given expliticly in TrueType units; in Format 1, points on the glyph’s contour are furnished to the
system. The second case is more powerful, since it takes into account any TrueType instructions that are present, which may play an important role at a low resolution.
Here is an example of this table, in Format 0:
&lt;lcar&gt;
&lt;Version value="1"/&gt;
&lt;LigCaretClassEntries format="0"&gt;
&lt;LigCaretClassEntry index="0"&gt;
&lt;distance index="0" value="239"/&gt;
&lt;distance index="1" value="475"/&gt;
&lt;/LigCaretClassEntry&gt;
...
&lt;/LigCaretClassEntries&gt;
&lt;Glyphs&gt;
&lt;Glyph value="f_f_l" class="0"/&gt;
...
&lt;/Glyphs&gt;
&lt;/lcar&gt;
After the usual Version element, we have two other elements: LigCaretClassEntries contains the different combinations of cursor positions, with no reference to glyphs, which we
call caret classes; Glyphs contains glyphs, with reference to caret classes. In LigCaretClassEntries, there is a LigCaretClassEntry for each class. It contains distance elements, which
represent the cursor positions. Their value value (or class) attributes contain glyph names
(or numbers of caret classes).
And here is an example of this table, in Format 1:
&lt;lcar&gt;
&lt;Version value="1"/&gt;
&lt;LigCaretClassEntries format="1"&gt;
&lt;LigCaretClassEntry index="0" format="1"&gt;
&lt;ctlPoint index="0" value="50/&gt;
&lt;/LigCaretClassEntry&gt;
...
&lt;/LigCaretClassEntries&gt;
&lt;Glyphs&gt;
&lt;Glyph value="f_r" class="0"/&gt;
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
Figure D-7: A trilingual and tri-fontal love poem (the fonts, in order: the sublime Zapfino, by Hermann
Zapf; equally sublime, for fonts of its kind, Δεκαεξρια τ!
κσσα
[“Sixteen-point [letters] taken from
the case”] by Tereza Tranaka-Haralambous; and Monotype Modern italic). Left: default typesetting, with
simple line changes and justification according to the letter’s point of origin. Right: the same typesetting,
but with the use of the opbd table: the verses are aligned better.
...
&lt;/Glyphs&gt;
&lt;/lcar&gt;
Instead of distance elements, we have ctlPoint elements, whose value element contains
the number of a point on the glyph’s contour. That means, of course, that all the glyphs in
the same class must have the same point on the contour at the same location, which requires
some attention when designing the glyph.
D.11.7
The opbd Table
This table is quite original and deserves a beautiful love poem (Figure D-7). Its name is the
unpronounceable abbrevation of optical bounds. It solves one simple, but fundamental, problem. We know that all glyphs have side-bearings (i.e., the space on each side of the glyph).
These side-bearings are as indispensable as the rules of courtesy in human society: without
them, the glyphs would touch, yielding an illegible jumble.
Thus side-bearings are a good thing. But what happens when we wish to align glyphs, such as
at the beginning of the line? Stupid typesetting software will not align the glyphs, only their
points of origin. If the side-bearings of all the glyphs were the same, that approach would effectively align the glyphs. But who can guarantee that the side-bearings will indeed be the same?
Figure D-7 shows that the side-bearings in different fonts may indeed be quite different—
especially when roman and italic are mixed.
The opbd table supplies the glyphs’ “optical bounds”—i.e., the coordinates of the abstract box
that will ultimately be used for alignment. Software must be quite intelligent to be able to
say “I am aligning at the left; therefore I shall take the left edge of the abstract box in opbd as
the left part of the glyph and use its usual box for the other edges”.
The reader will have observed that we could just as well take the glyph’s bounding box. That
is only partly true: the font’s designer may have wished to disregard a part of the glyph. For
example, the letter ‘d’ at the beginning of the third line in the figure could have been aligned
not according to its ascender but according to its lower part. No software in the world can be
```

```text
D.11. General AAT Tables
as intelligent as the designer, nor as capable of foreseeing this detail. Thus it is quite useful
to have in the font a piece of data, distinct from the bounding box, that will be used for this
purpose.
Here is an example of the opbd table:
&lt;opbd&gt;
&lt;Version value="1"/&gt;
&lt;bounds format="0"&gt;
&lt;Glyph value="A" left="-" top="15" right="0" bottom="0"/&gt;
&lt;Glyph value="C" left="-" top="5" right="55" bottom="-"/&gt;
...
&lt;/bounds&gt;
&lt;/opbd&gt;
Once again, there are two formats for this table: in format 0, we use coordinates in TrueType
units; in Format 1, we use the numbers of points on the contour. The bounds element contains Glyph glyphs. Each Glyph has five attributes: the glyph name (value) and the left (left),
top (top), bottom (bottom), and right (right) optical bounds. The vertical limits are used
when we set type in that direction.
The values given are the amounts by which the glyph must be displaced so that it will reach
its optical bounds. The same table in Format 1 would yield:
&lt;opbd&gt;
&lt;Version value="1"/&gt;
&lt;bounds format="1"&gt;
&lt;Glyph value="A" left="32" top="41" right="-" bottom="-"/&gt;
&lt;Glyph value="C" left="36" top="37" right="38" bottom="39"/&gt;
...
&lt;/bounds&gt;
&lt;/opbd&gt;
Here the values are the numbers of points on the contour. The software must therefore align
those points in order to achieve optimal alignment. A value of −1 means that no correction of
the alignment is necessary for that side of the glyph. Note that there is a predefined OpenType
feature that bears the same name and plays the same role as the opbd table of AAT.
D.11.8
The prop Table
“Zounds!” This table, whose name comes from “property”, gives us certain data on the glyphs,
some of those data inspired in part by the Unicode properties of the characters to which the
glyphs belong. For example, the table tells us whether a glyph is “floating” (in the sense that
it has zero width and that the software has to place it in the right spot); whether it must be set
in the margin (like the quotation marks that begin this paragraph21); whether it should be
inverted when we switch from left-to-right typesetting to right-to-left typesetting or vice versa,
21 Whose presence justifies the unexpected exclamation at the beginning of the paragraph.
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
as with the left parenthesis, which becomes a right parenthesis, etc.; where appropriate, the
identity of its mirror-image alter ego;22 whether the current glyph is “physically attached” to
the glyph at its right—in other words, if the two glyphs are playing Romeo and Juliet, the
software must not do anything that would separate them or move them apart, even by the
slightest amount; finally, the Unicode directionality class (see page 142) of the character to
which the glyph belongs.
Here is an example of one such table:
&lt;prop&gt;
&lt;Version value="3"/&gt;
&lt;properties&gt;
&lt;defaultGlyph floater="0" hangLeft="0" hangRight="0"
mirrored="0" mirrorGlyph="A" attachRight="0"
directionalityClass="0"/>
&lt;Glyph value="A" floater="0" hangLeft="0" hangRight="0"
mirrored="0" mirrorGlyph="A" attachRight="0"
directionalityClass="0"/>
&lt;Glyph value="parenleft" floater="0" hangLeft="0" hangRight="0"
mirrored="1" mirrorGlyph="parenright" attachRight="0"
directionalityClass="11"/>
...
&lt;/properties&gt;
&lt;/prop&gt;
The properties element contains Glyph elements corresponding to the different glyphs and
a defaultGlyph element that supplies the values of the glyph’s properties that do not appear
on the list. For each of these elements, there are eight attributes (seven for defaultGlyph,
since it does not have a glyph name): the glyph’s name (value); an indication of whether it
hangs in the left margin (hangLeft) or the right margin (hangRight); an indication of whether
it is mirrored (mirrored), and, if appropriate, the name of the glyph that is its mirror image
(mirrorGlyph); an indication of whether the glyph is “physically” attached to the glyph at its
right (attachRight); and, finally, the Unicode directionality class of the character to which
the glyph belongs (directionalityClass).
These data are indeed very useful, but reality is often a bit more complex: for example, the
accents and breathing marks of the Greek language (which are placed before capital letters,
as in the word Z ΕλληναP) must be set in the margin, but only at the beginning of a paragraph
or a verse. But this table does not accommodate the fact that a glyph may change its properties
according to its context.
D.11.9
The trak Table
This table manages global letterspacing. Its name comes from tracking, just as with the TrackKern entries of the AFM files (see §C.3.7). Here is an example of one such table:
22 Warning: we use the glyph’s number to find the mirror-image glyph, but there is a catch—the offset
between the two glyphs must not exceed 15. Apple asks that glyphs that are mirror images of each other appear
consecutively in the font in order to avoid the problem of their being located too far apart.
```

```text
D.11. General AAT Tables
&lt;trak&gt;
&lt;Version value="1"/&gt;
&lt;tracking format="0"&gt;
&lt;horizData&gt;
<!-- nTracks=3 -->
&lt;trackEntry index="0" value="-" nameIndex="15"&gt;
<!-- nSizes=2 -->
&lt;track size="12" value="-"/&gt;
&lt;track size="24" value="-"/&gt;
&lt;/trackEntry&gt;
&lt;trackEntry index="1" value="0" nameIndex="16"&gt;
<!-- nSizes=2 -->
&lt;track size="12" value="0"/&gt;
&lt;track size="24" value="0"/&gt;
&lt;/trackEntry&gt;
&lt;trackEntry index="2" value="1" nameIndex="17"&gt;
<!-- nSizes=2 -->
&lt;track size="12" value="50"/&gt;
&lt;track size="24" value="20"/&gt;
&lt;/trackEntry&gt;
&lt;/horizData&gt;
&lt;vertData&gt;
<!-- nTracks=0 -->
&lt;/vertData&gt;
&lt;/tracking&gt;
&lt;/trak&gt;
In the tracking element, which contains all the data, we find a horizData for horizontal
typesetting and a vertData for vertical typesetting. In each of these two cases, there are several
trackEntry elements, which correspond to different levels of predefined letterspacing. Each
level has an integer value value (0 for the absence of letterspacing, negative for tightly spaced
text, positive for loosely spaced text) and a name. Apple exhibits political correctness: the
name of the level of letterspacing is not a bland four-letter tag (like the names of OpenType
features) but an entry in the name table, which, as we know, contains names and other short
texts in all the languages into which the font’s designer wished to translate them! The value
of nameIndex is therefore a number of the entry namerecord in the name table (see §D.4.6).
The element trackEntry contains several track entries, which are values of letterspacing in
TrueType units (the value attribute), for a given actual size (the size attribute, in American printers’ points). In our example, for instance, there is negative letterspacing, whose
English name could have been “tight spacing”; it involves reducing the widths of the glyphs
by 15 units at 12 points and by 7 units at 24 points. For every size other than 12 and 24, the
value of letterspacing will be interpolated (or extrapolated, as the case may be).
Note that this table is rather simplistic, for several reasons. First of all, letterspacing is sometimes “semantic”; i.e., it is deliberately requested by the author in order to highlight a block of
text—a technique that replaces italics in some typographic traditions. Semantic letterspacing
is used in Russian, gothic German, Greek, etc. But in this case [163, 164] we move only the
```

Appendix D : The TrueType, OpenType, and AAT Font Formats
letters apart, not the punctuation marks! That is, unfortunately, impossible with the trak table. Another shortcoming: the actual values of letterspacing are given only at an actual size in
points. But we should be able to force letterspacing by one pixel more or fewer, for example,
depending on the resolution of the display or printing device. Here, a structure like the device
table of the OpenType tables would be quite suitable for giving the values of letterspacing in
pixels, according to the size of the glyphs.23 But as the proverb says, faute de chien, on emmène
le cabri à la chasse; in other words, we must make do with what we have.
D.11.10
The Zapf Table
The name of this table is inspired by the name of a great font designer who shall remain
nameless here. He is a member of the very small group of famous people such as Bach, Kant,
Hugo, Zola, Dalí, Tati, etc., whose names contain only four letters. (Bill Gates fell just short
of membership in this group of immortals.)
The aim of this table is both ambitious and praiseworthy: it is there for nothing more or less
than giving order to the chaos that reigns when we switch from characters to glyphs. Mr. Zapf
(not to name names) is the great Oracle who answers the existential questions about each
glyph: “where do I come from?”, “which is my character?”, “what had to happen to bring
me into being?”, “which other glyphs resemble me?”, “how did the holy Designer describe
me?”, “by what name do others identify me?” It is a pity that there is no Zapf table for human
beings.
Let us talk concretely. The Zapf table collects a range of data about each glyph. Here they are:
• Some Unicode characters that can yield the glyph (which are, therefore, its potential fathers).
• Some strings of characters that describe the glyph. Each of these strings is of a certain
type, as shown:
– type 0: a string, nothing more
– type 1: the glyph’s “Apple name”
– type 2: the glyph’s name, according to Adobe’s specifications (see §C.3.3)
– type 3: the glyph’s AFII name (§C.3.3 and [29])
– type 4: the Unicode description of the glyph
– type 64: the glyph’s CID number (see §C.7), if it is a Japanese ideograph
– type 65: ditto, if it is a traditional Chinese ideograph
– type 66: ditto, if it is a simplified Chinese ideograph
– type 67: ditto, if it is a Korean ideograph
23 Do not confuse “size” and “point size”: the size is given in pixels per em, whereas the point size is given
in American printers’ points. To convert from one to the other, one must know the resolution: the glyphs of a
font at size 9, when displayed on a screen with 72 pixels per inch, will have a point size of 9
72 = 0.125 inches =
9.03374 American printers’ points; the same glyphs displayed at 96 ppi will have an effective point size of
6.7753 points!

D.11. General AAT Tables
– type 68: a namerecord entry number in the name table; this entry should allow the
designer to describe, in every language supported, the history of all the versions of
the glyph
– type 69: another namerecord number, this time used to write the designer’s name
– type 70: as above, but a longer name (. . . )
– type 71: as above, for the designer to explain the glyph’s usage
– type 72: as above, for the designer to place the glyph in the historical context of typography (for example, “this ‘d’ was cut by Claude Garamond on December 24, 1534,
the memorable day when his friend Antoine Augereau was burned at the stake in
Maubert Square” [105])
• The glyph’s membership in a group of glyphs. The groups are defined in the same table; they consist of a namerecord number that contains the group’s name, and several
glyphs belonging to the group. Among these groups, there may be some that are groups
of groups—sets of references to groups of glyphs. That may happen when a glyph belongs
to more than one group.
• Last but not least, an indication of whether the glyph is the result of the application of a
set of AAT features, in a certain context. Let us explain: We have seen, in the description
of the feat table (§D.11.5), that AAT offers several features, each of which has its own
selectors. To obtain a given glyph, we must, if necessary, enable certain selectors for some
of these features, and also be in a given context—e.g., at the beginning of a line. Here is
a list of the possible contexts:24
– 0: not in any context
– 1, 2, 4: beginning, middle, or end of line
– 8, 16, 32: beginning, middle, or end of word
– 64, 128: numerator or denominator of a fraction
All those things (features, selectors, context) are stored in the Zapf table.
Here is the first part of a Zapf table:
&lt;Zapf&gt;
&lt;Version value="1"/&gt;
&lt;GlyphInfos&gt;
&lt;GlyphInfo value="A" GroupInfo="0" FeatureInfo="-"&gt;
&lt;unicodes&gt;
<!-- n16BitUnicodes=1 -->
&lt;unicode value="0041"/&gt;
&lt;/unicodes&gt;
24 Bizarrely enough, these contexts are the values of flags, yet, contrary to the way in which flags are usually employed, it is not possible to enable several of these flags at the same time—something that the author
considers absurd: if a word consists of only one glyph, then the glyph appears at the beginning of the word, in
the middle, and at the end. And the glyph may also very well occur at the end of the line. . .

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
&lt;kindNames&gt;
<!-- nNames=2 -->
&lt;kindName kind="2" value="A"/&gt;
&lt;kindName kind="4" value="LATIN CAPITAL LETTER A"/&gt;
&lt;kindName kind="69" value="18"/&gt;
&lt;/kindNames&gt;
&lt;/GlyphInfo&gt;
...
&lt;/GlyphInfos&gt;
We see here that the list GlyphInfo of glyphs is contained within a GlyphInfos (with an ‘s’)
element, which makes up the first part of the table. Each GlyphInfo has three attributes: the
glyph name (value), the number of the associated group of glyphs (GroupInfo, an element
that appears in the second part; it can also represent a group of groups), and the number of
a list of features (FeatureInfo; this list appears in the third part of the table).
In a GlyphInfo element, there are two subelements: unicodes, which contains several Unicode characters to which the glyph belongs, each of them represented by a unicode (with
no ‘s’) element, and kindNames, which contains a number of strings that describe the glyph.
Each string is represented by a kindName element, of which the kind attribute describes the
meaning and the value attribute contains the string itself. Above, we presented the list of
possible values of kind and the associated meanings. In the snippet of code, we see three cases:
when kind is equal to 2, it is the glyph’s Adobe name (A); when kind is equal to 4, it is the
Unicode name of the glyph (latin capital letter a); and when kind is equal to 69, it is the
number of a namerecord, in the name table, that contains the name of the glyph’s designer.
Here is the second part of our example:
&lt;GroupInfos&gt;
&lt;GroupInfo index="0" nameIndex="19" isSubdivided="0"&gt;
<!-- nGlyphs=26 -->
&lt;Glyph value="A"/&gt;
&lt;Glyph value="B"/&gt;
...
&lt;Glyph value="Z"/&gt;
&lt;/GroupInfo&gt;
&lt;GroupInfo index="1" nameIndex="20" isSubdivided="0"&gt;
<!-- nGlyphs=6 -->
&lt;Glyph value="a"/&gt;
&lt;Glyph value="e"/&gt;
...
&lt;Glyph value="y"/&gt;
&lt;/GroupInfo&gt;
&lt;GroupInfo index="2" nameIndex="21" isSubdivided="0"&gt;
<!-- nGlyphs=20 -->
&lt;Glyph value="b"/&gt;
&lt;Glyph value="c"/&gt;
```

```text
D.11. General AAT Tables
...
&lt;Glyph value="z"/&gt;
&lt;/GroupInfo&gt;
...
&lt;GroupInfoGroup index="7" nameIndex="22"&gt;
<!-- nGroups=2 -->
&lt;GroupInfo ref="1"/&gt;
&lt;GroupInfo ref="2"/&gt;
&lt;/GroupInfoGroup&gt;
...
&lt;/GroupInfos&gt;
This part contains the definitions of groups of glyphs, which are contained in GroupInfos
elements. Each GroupInfo contains merely a list of glyphs. In addition, it has three attributes:
its number (index), the number of the associated namerecord in the name table (nameIndex),
and a flag indicating whether it is a subdivision of a larger group (in which case isSubdivided
takes the value 1).
In the example, we also see a group of groups, GroupInfoGroup. It contains not glyphs but references to groups of glyphs, in the form of GroupInfo elements whose ref attribute contains
the number of the group in question.
Finally, here is the third part of our example:
&lt;FeatureInfos&gt;
&lt;FeatureInfo index="0" context="0"&gt;
<!-- nAATFeatures=3 -->
&lt;Feature value="1" selector="4"/&gt;
&lt;Feature value="8" selector="2"/&gt;
&lt;Feature value="8" selector="6"/&gt;
&lt;/FeatureInfo&gt;
...
&lt;/FeatureInfos&gt;
&lt;OTTags&gt;
<!-- nOTTags=2 -->
&lt;tag value="hist"/&gt;
&lt;tag value="ss07"/&gt;
&lt;/OTTags&gt;
&lt;/Zapf&gt;
This part contains a list of features and a given context. If the glyph GlyphInfo, through the
attribute FeatureInfo, refers to this list of features, it is thanks to them that it was possible
to typeset it.
The element FeaturesInfo contains a FeatureInfo (with no ‘s’) for each list of features. Each
FeatureInfo contains a context attribute that gives the context (according to the list presented above). It contains Feature elements, each of which represents an AAT feature; more
precisely, there are a feature number (the value attribute) and a selector number (selector).
See §D.11.5.1 for a list of the features and their selectors.
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
Finally, the element OTTags is an attempt at reconciliation with the OpenType world. Let us
quote the author of this table, David Opstad: “When I designed the ‘Zapf’ table I explicitly
wanted to provide for OpenType as well as AAT, for a more harmonious future” (private communication of September 24, 2003). The tag subelements of OTTags contain the tags for the
OpenType features that are required in order to obtain the glyph in question. That assumes
a mixed OpenType/AAT table, for which we are still waiting.
D.12
The AAT Tables for Font Variation
The principle of font variation is close to that of the Multiple Master fonts: we define several
“axes of variation” and take a few points in the space formed by these axes—in other words,
several combinations of the values of these axes. Example: if we define the weight and the
optical size as axes, and if the weights range from −1 to +1 and the optical sizes range from 6
to 72, we can take the combinations (0,10) = weight 0 and optical size 10, (−1,10), (+1,10),
(−1,6), (+1,72), etc. To each of these pairs of values, there corresponds a version of the font.
In the case of Multiple Master, we made the distinction between master designs and intermediate values. That means that a designer could focus on several specific designs and let the
system perform the requisite interpolations on the positions of the points to yield all the
other possible variants.
Here the situation is slightly more complex. The master designs still exist, but they can differ
for each glyph. Therefore a glyph that never varies will be described only once. The glyphs
that vary only slightly will have only a few master designs. Those with many details will have
more master designs. It is a genuine miracle if the processor manages to cope with all these
values and generate a reasonable rendering.
D.12.1
The fvar Table
Almost all the tables in this section, which is devoted to font variation, have a name that ends
in var. Here it is fvar (“font variation”). Later we shall see variations of axis (avar), glyph
(gvar), and table of control values (cvar).
The fvar table contains definitions of axes and predefined instances. It is quite simple: we
define the names, the extreme values, and the default values of the axes, and then we give
the values (on the axes) of the predefined instances. Here is an example of the first part of
this table:
&lt;fvar&gt;
&lt;Version value="1"/&gt;
&lt;sfntVariations&gt;
<!-- axisCount=2 -->
&lt;sfntVariationAxis index="0" flags="0"&gt;
&lt;axisTag value="wght"/&gt;
&lt;minValue value="0.5"/&gt;
&lt;defaultValue value="1.0"/&gt;
&lt;maxValue value="2.0"/&gt;
&lt;nameIndex value="256"/&gt;
```

D.12. The AAT Tables for Font Variation
&lt;/sfntVariationAxis&gt;
&lt;sfntVariationAxis index="1" flags="0"&gt;
&lt;axisTag value="wdth"/&gt;
&lt;minValue value="0.5"/&gt;
&lt;defaultValue value="1.0"/&gt;
&lt;maxValue value="2.0"/&gt;
&lt;nameIndex value="257"/&gt;
&lt;/sfntVariationAxis&gt;
&lt;/sfntVariations&gt;
In this example, we define two axes, sfntVariationAxis, which we place within an sfntVariations element. Each sfntVariationAxis has a zero-valued flags attribute and five
subelements:
• axisTag: the tag, or the four-letter ASCII name of the axis: we have the choice of wght
(weight), wdth (width), or slnt (slant).
• opsz, the optical size.
• The minimum value (minValue), default value (defaultValue), and maximum value
(maxValue) of the axis.
• The record number, namerecord, of the name table, stored in the subelement nameIndex.
Thanks to the name table, we can give each axis a human-readable name—in every language
in the world (something that is pitifully lacking from the Multiple Master fonts).
In the example above, we have defined two axes: weight and width. These two axes can take
values between 0.5 and 2, and their common default value is 1.
Here is the second part of this table:
&lt;sfntInstances&gt;
<!-- instanceCount=3 -->
&lt;sfntInstance index="0" flags="0"&gt;
&lt;nameIndex value="258"/&gt;
&lt;coords&gt;
&lt;coord index="0" value="0.5"/&gt;
&lt;coord index="1" value="1.0"/&gt;
&lt;/coords&gt;
&lt;/sfntInstance&gt;
&lt;sfntInstance index="1" flags="0"&gt;
&lt;nameIndex value="258"/&gt;
&lt;coords&gt;
&lt;coord index="0" value="2.0"/&gt;
&lt;coord index="1" value="1.5"/&gt;
&lt;/coords&gt;
&lt;/sfntInstance&gt;

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
&lt;sfntInstance index="2" flags="0"&gt;
&lt;nameIndex value="258"/&gt;
&lt;coords&gt;
&lt;coord index="0" value="2.0"/&gt;
&lt;coord index="1" value="0.5"/&gt;
&lt;/coords&gt;
&lt;/sfntInstance&gt;
&lt;/sfntInstances&gt;
&lt;/fvar&gt;
Here there are four font instances—i.e., four pairs of values of axes (we say pairs because each
font has only two axes). The instances are represented by sfntInstance elements contained in
an sfntInstances (with an ‘s’) element. Each sfntInstance instance has a zero-valued flags
attribute, a subelement nameIndex that points back to a name of the instance in the name
table, and an element coords that contains the values of the axes for the instance. The coords
element, in turn, contains a coord subelement for each axis. Each of them contains a value
(the value attribute), the value of that coordinate on the axis.
D.12.2
The avar Table
The avar table is a very small table based on a simple idea: why should the interpolation
of the coordinates of points on the contour be linear as we move along an axis? Indeed, it
would be attractive to be able to interpolate the points in a manner other than mere linear
interpolation. Unfortunately, the AAT processor does not afford us the luxury of arbitrary
interpolation, but it nevertheless does allow one thing: piecewise linear interpolation.
Let us take an example. Suppose that the values of an axis (for example, the axis for optical
size) range from 6 to 72. The user selects the correct value through a user interface that offers,
for example, a sliding bar to select a value between these two extremes:
But if the values are represented linearly, that means that for values between 6 and 12 points,
which are, incidentally, the most important ones, one must be extremely precise to place the
triangle in the correct location:
7 8 9 10 11 12 18
That calls for the precision of a watchmaker, whereas the rest of the sliding bar is underused.
Therefore we can do as follows: we can set aside half of the bar for the values between 6 and 12,
the next quarter for the values between 12 and 24, and the remaining quarter for the values
between 24 and 72:
```

```text
D.12. The AAT Tables for Font Variation
This is a much more rational approach that allows for precision where it is most needed, by
sacrificing other areas in which precision is less important.
That is exactly what the avar table does. It associates values on an axis with the user’s values.
Between two pairs of values so linked, interpolation is linear. On the sample bar that we
presented above, the associated pairs are (0,6), ( 1
2,12), ( 3
4,24), (1,72).
Here is an example of one such table:
&lt;avar&gt;
&lt;Version value="1"/&gt;
<!-- axisCount=2 -->
&lt;axis index="0"&gt;
<!-- pairCount=4 -->
&lt;pair index="0" from="0" to="6"/&gt;
&lt;pair index="1" from="0.5" to="12"/&gt;
&lt;pair index="2" from="0.75" to="24"/&gt;
&lt;pair index="3" from="1" to=72/&gt;
&lt;/axis&gt;
&lt;axis index="1"&gt;
<!-- pairCount=2-->
&lt;pair index="0" from="-" to="-"/&gt;
&lt;pair index="1" from="1" to="1"/&gt;
&lt;/axis&gt;
&lt;/avar&gt;
Its structure is very simple. There is one axis element for each axis. Each axis element contains pair elements that represent pairs of values: the from attribute contains the “user’s
value” (in our case, the subdivision of the bar), and the to attribute contains the value on the
corresponding axis. In our example, we have taken the case shown by the bar as our axis 0
and the identity between the user values and the axis values for our axis 1.
Note that the very same technique (piecewise linear interpolation) is also applied in Multiple
Master fonts—in the BlendDesignMap entry of the PostScript dictionary (see §3). In Multiple
Master jargon, the user values are called design values and are defined by the font’s designer;
the axis values are called blend values and always lie between 0 and 1. Aside from these insignificant differences, the technique is exactly the same.
D.12.3
The gvar Table
The gvar table contains the data needed to transform the glyphs according to the different
axes of variation. These data are in fact offsets from points on the contour; but it is necessary
to decide, for each glyph, which points are to be modified and for which axis values the required
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
This is font Skia. “Skia” in Greek means “shadow”.
This is font Skia. “Skia” in Greek means “shadow”.
This is font Skia. “Skia” in Greek means “shadow”.
This is font Skia. “Skia” in Greek means “shadow”.
This is font Skia. “Skia” in Greek means “shadow”
This is font Skia. “Skia” in Greek means “shadow
This is font Skia. “Skia” in Greek means “shadow
This is font Skia. “Skia” in Greek means “shado
This is font Skia. “Skia” in Greek means “shado
This is font Skia. “Skia” in Greek means “shad
Figure D-8: The font Apple Skia and its variations along the wght axis.
offsets are to be given explicitly (whereas for the other axis values, the system will perform
the necessary interpolations to obtain appropriate glyphs).
The structure of this table is relatively simple, at least when it is represented in TTX (whereas
its binary version is a bit of a nightmare for the programmer, doubtless because of the large
number of optimizations found within it).
It is divided into two main sections: the definition of the n-tuplets of axis values (where n is
the number of axes), and the provision of offsets from the points for each glyph in the font.
Here is an example of the first section:
&lt;gvar&gt;
&lt;Version value="1"/&gt;
&lt;header axisCount="2" flags="0"/&gt;
&lt;sharedCoordinates&gt;
<!-- globalCoordCount=4 -->
&lt;sharedCoord index="0"&gt;
&lt;coord index="0" value="-.0"/&gt;
&lt;coord index="1" value="0.0"/&gt;
&lt;/sharedCoord&gt;
&lt;sharedCoord index="0"&gt;
&lt;coord index="0" value="1.0"/&gt;
&lt;coord index="1" value="0.0"/&gt;
&lt;/sharedCoord&gt;
&lt;sharedCoord index="0"&gt;
&lt;coord index="0" value="0.0"/&gt;
&lt;coord index="1" value="-.0"/&gt;
&lt;/sharedCoord&gt;
&lt;sharedCoord index="0"&gt;
&lt;coord index="0" value="0.0"/&gt;
```

```text
D.12. The AAT Tables for Font Variation
&lt;coord index="1" value="1.0"/&gt;
&lt;/sharedCoord&gt;
&lt;/sharedCoordinates&gt;
Here we assume that there are two axes; therefore, the “n-tuplets” are pairs. The header element contains the number of axes (which must be the same as in the fvar table). Next comes
the element sharedCoordinates, which contains pairs of predefined axis values. In a Multiple
Master font, it corresponds to coordinates of the master designs. Here we have the possibility
of defining other pairs of “private” axis values for individual glyphs.
Each sharedCoordinate (with no ‘s’) corresponds to a pair of values shared by all the glyphs.
It contains a coord element for each axis in the font. The value attribute contains the value
of the “coordinate” for the axis in question.
In the first section, therefore, we have defined the axis values that are available to all the
glyphs. But nothing compels any glyph to use these values; indeed, it can add others or even
replace these values outright.
Here is the second part of the table:
&lt;Glyphs&gt;
&lt;Glyph value="A" index="0"&gt;
&lt;sharedPointNumbers&gt;
<!-- pointcount=10 -->
&lt;pointNumber index="0" value="0"/&gt;
&lt;pointNumber index="1" value="1"/&gt;
...
&lt;pointNumber index="8" value="8"/&gt;
&lt;pointNumber index="9" value="9"/&gt;
&lt;/sharedPointNumbers&gt;
&lt;tuples sharedPointNumbers="1"&gt;
<!-- tupleCount=4 -->
&lt;tuple index="0"&gt;
&lt;sharedCoord index="0"/&gt;
&lt;deltas&gt;
&lt;xDelta index="0" value="169"/&gt;
... 12 lignes semblables ...
&lt;xDelta index="13" value="0"/&gt;
&lt;yDelta index="0" value="86"/&gt;
... 12 lignes semblables ...
&lt;yDelta index="13" value="0"/&gt;
&lt;/deltas&gt;
&lt;/tuple&gt;
&lt;tuple index="0"&gt;
&lt;sharedCoord index="1"/&gt;
...
&lt;/tuple&gt;
&lt;tuple index="0"&gt;
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
&lt;sharedCoord index="2"/&gt;
...
&lt;/tuple&gt;
&lt;tuple index="0"&gt;
&lt;sharedCoord index="3"/&gt;
...
&lt;/tuple&gt;
&lt;/tuples&gt;
&lt;/Glyph&gt;
...
&lt;/Glyphs&gt;
&lt;/gvar&gt;
There is a Glyph element for each glyph in the font. For each of these elements, there are two
types of information: the numbers of the points on the contour that are to be offset, and the
offsets of these points for each pair of axis values.
The numbers of points on the contour are contained in the element sharedPointNumbers.
That is hardly surprising: there is a pointNumber element for each point that may be modified;
the value attribute contains the numbers of these points.
Let us point out once again that these points are shared by all the master designs but that each
master design may also use its own “private” points. Finally, one important detail: here we list
only the points on the contour that are of interest to us, but the font will give the offsets for
four additional points. These points, called “phantom points”, are the origin of the glyph, its
set-width (these points have already been given in the description of the contour), its vertical
origin, and its “vertical set-width” (i.e., the ending point of the displacement vector during
vertical typesetting). Do not be astonished that the example above describes 10 points but
then lists 14 offsets!
Next comes a rather bulky element called tuples. This name deserves a brief explanation.
American hackers love to create new names (as we have already seen with byte and nybble).
The word tuple comes from the common ending of words “sextuple”, “septuple”, “octuple”,
etc.
The tuples element (with an ‘s’) contains the different pairs of axis values selected for the
glyph. In this example, there are four pairs of predefined values. There is a tuple element
(with no ‘s’) for each of the axis values. Any “personalized” pair of axis values will be contained in a subelement of tuple that is called embeddedCoord. In the example above, there
are only predefined values; they are indicated by sharedCoord elements, which refer (through
the index attribute) to elements of the same name that appear directly under gvar.
A tuple may refer to shared points on the contour (contained in sharedPointNumbers), or it
may define its own points on the contour (called “private point numbers” and included in
privatePointNumbers). In any event, it contains, after sharedCoord (or embeddedCoord), the
offsets corresponding to these points. These offsets are represented by two series of elements:
xDelta (horizontal offsets) and yDelta (vertical offsets).
Note that this specification unfortunately gives explicit offset values and does not support
specifying them as points (to take the effects of any TrueType instructions into account) or as
“device tables”, as is done in OpenType.
```

```text
D.12. The AAT Tables for Font Variation
In any case, we enjoy a great deal of flexibility for defining different master designs for each
glyph; thus the system is undeniably powerful. And, last but not least, since the disappearance
of the Multiple Master fonts, the AAT fonts with variation tables are now the only “dynamic”
fonts on the market, if we exclude fonts created in the form of computer programs, such as those
written in METAFONT.
D.12.4
The cvar Table
The cvar table is constructed in the same way as gvar, but in the place of numbers of points
on the contour, there are numbers of CVT entries (values of the control table; see the cvt
table). Recall that the CVT entries are global values (at the level of the entire font) used in
TrueType instructions for the glyphs. The control values are used to store certain characteristics of the font: the heights of the ascenders, the thicknesses of the strokes, the widths of the
serifs, etc.
For each n-tuplet of axis values in fvar and gvar—in other words, for each choice of master
design—cvar contains a set of offsets from control values, which are customized for the master designs. For example, if stroke thickness varies, the value of the corresponding entry in
the CVT table should do so as well.
Here is an example of the cvar table:
&lt;cvar&gt;
&lt;Version value="1"/&gt;
&lt;cvtEntries&gt;
<!-- cvtCount=10 -->
&lt;cvtEntry index="0" value="17"/&gt;
&lt;cvtEntry index="1" value="24"/&gt;
...
&lt;cvtEntry index="8" value="137"/&gt;
&lt;cvtEntry index="9" value="249"/&gt;
&lt;/cvtEntries&gt;
&lt;tuples&gt;
<!-- tupleCount=4 -->
&lt;tuple index="0"&gt;
&lt;deltas&gt;
&lt;delta index="0" value="169"/&gt;
&lt;delta index="1" value="0"/&gt;
&lt;delta index="2" value="0"/&gt;
&lt;delta index="3" value="169"/&gt;
&lt;delta index="4" value="1"/&gt;
...
&lt;/deltas&gt;
&lt;/tuple&gt;
&lt;tuple index="0"&gt;
&lt;sharedCoord index="1"/&gt;
...
&lt;/tuple&gt;
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
&lt;tuple index="0"&gt;
&lt;sharedCoord index="2"/&gt;
...
&lt;/tuple&gt;
&lt;tuple index="0"&gt;
&lt;sharedCoord index="3"/&gt;
...
&lt;/tuple&gt;
&lt;/tuples&gt;
&lt;/cvar&gt;
We see here the two main elements: cvtEntries, which contains the relevant entry numbers
in the CVT table, and tuples, which contains a tuple subelement (with no ‘s’) for each master
design (n-tuplets of axis values). Each tuple contains a deltas element (with an ‘s’), which
in turn contains delta subelements (with no ‘s’) corresponding to the cvtEntry entries in
cvtEntries. Each delta is an offset (contained in the value attribute) from the corresponding
CVT entry.
D.13
AAT Tables with Finite Automata
In this section, we shall describe the big guns of the AAT tables: those used as finite automata
to perform positionings, substitutions, and justification. They are the tables morx (the new
version of the mort table) and just: they play the same role as the tables GPOS/GSUB and JSTF
in OpenType. Before we confront the formidable morx table, let us say a few words about finite
automata.
D.13.1
Finite Automata
A finite automaton is a way to represent certain simple programs. In our case, we shall describe
in this manner the program that reads the string of glyphs for a line of text and then displays
the glyphs. A program of this type may be in one or more states. Being in a given state means
that the program reacts in a certain manner when it reads the glyphs, and that this manner
is always the same for the same glyph; in other words, if in state A the program replaces an a
with a b, then that will always be the case, however many times the letter a occurs, as long
as the program remains in that state. The program’s reaction consists of performing an action
(leaving the glyph as it is, modifying it, replacing it, moving it, etc.) and possibly changing
states. When the program changes state, we say that a transition has occurred. The automaton
is called “finite” because this type of program has only a finite number of possible states,
therefore only a finite number of transitions.
In Figure D-9, we see two examples of finite automata. Let us take case (a). We shall consider
the following problem: describing the automaton that will keep the first letter in a string, add
a period to it, and hide the rest. In this way, we car replace personal names with initials: thus
“John Fitzgerald” becomes “J. F.”
The ellipses in the figure symbolize the possible states. For example, at time t, there are two
possibilities: we are either outside a word (the “initial state”) or inside one (“inside a word”).
When the first glyph arrives, we are always in the initial state. If the glyph is not a letter,
```

```text
D.13. AAT Tables with Finite Automata
if non-letter
if letter
if non-letter
if letter
keep,
insert a point
keep
keep
delete
initial state
word
interior
(a) Simple case.
(b) More complex case.
if non-letter
if non-letter
if consonant, except ‘h’
if vowel
or ‘h’
if non-letter
if letter
keep,
insert
a point
delete,
insert a point
keep,
insert a point
keep
keep
keep
keep
delete
initial state
second
glyph
word
interior
if ‘h’
if letter other than ‘h’
➀
➁
➂
➃
➀
➁
➂
➃
➄
➅
➆
➇
Figure D-9: Two examples of finite automata.
we preserve it and stay within the same state (arrow ). When a letter arrives, we perform
an action: we retain the letter and append a period to it; at the same time, we change states
(arrow ), and then we are in the state “inside a word”. Thus we find ourselves in the ellipse
at the right. Once again, there are two cases. If the following glyph is a letter, that means that
we are still inside a word. We therefore hide the letter and remain in the state (arrow ). If a
nonletter arrives, we retain it (our marching orders did not ask us to delete nonletters) and
return to the initial state (arrow ).
It is important to understand the concepts represented in Figure D-9. The ellipses are states.
The arrows are transitions. The words set in bold italic Gill are the actions that accompany the
transitions. The tests of style—“if a letter” and “if not a letter”—are the conditions required
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
for an action to occur. We say that there are classes of glyphs: in the initial state, the classes
are “letter” and “nonletter”. The same is true of the state “inside a word”.
To understand the structure of this diagram, the reader is advised to go through the intellectual exercise of saying “I am the string Raymond; what will happen to me if I pass through this
automaton?”
Having established our terminology and our basic concepts, let us make our problem slightly
more complex. The automaton shown in Figure D-9 (a) may satisfy most of our friends, but it
will leave others unhappy: Philippe, Christian, Thierry, Kharostani, Dharmaputtra, XhiangGo, and many other individuals whose names begin with a consonant followed by an ‘h’. For
their names, we are accustomed to writing two letters, not just one, as an abbreviation: ‘Ph.’,
‘Ch.’, ‘Th.’, etc. Of course, this convention has no effect on names that begin with an ‘H’, since
‘Hh’ can never occur.
How does this convention affect what we have done? First observation: if the first letter is
not a consonant, then there is nothing to change. That is the condition that arrow  will
handle: it is no longer “if a letter” but rather “if a vowel or ‘h’ ”. The case of the vowels and ‘h’
is therefore settled. Now, if the first letter is a consonant (other than ‘h’), a new arrow, ,
leaves from the initial state and goes to a new state that we shall call “second glyph”. Thus we
have processed the first glyph, which is a consonant (other than ‘h’), and we are preparing to
process the second. Three cases must be handled: (1) the character is not a letter, and so we
return to the initial state (arrow ); (2) the character is the letter ‘h’, and so we preserve the
letter and append a period to it (arrow ); (3) the letter is not an ‘h’, and so we omit the glyph
but still insert a period (something that was not done during action , unlike action ).
Here, then, is how we have extended our automaton to take account of the new condition
that represents the nature of the second letter.
For those of our readers who have previously programmed in lex (a very widely used lexical parser),
the automaton in our example would be written as follows:
%{
%}
%x INSIDE_A_WORD
%x SECOND_GLYPH
%%
[BCDFGKLMNPQRSTVWX]
{ ECHO; GOTO SECOND_GLYPH; }
[A-Z]
{ ECHO; printf("."); GOTO INSIDE_A_WORD; }
&lt;SECOND_GLYPH&gt;[h]
{ printf("h."); GOTO INSIDE_A_WORD; }
&lt;SECOND_GLYPH&gt;[a-z]
{ printf("."); GOTO INSIDE_A_WORD; }
&lt;SECOND_GLYPH&gt;.|\n
{ ECHO; GOTO 0; }
&lt;INSIDE_A_WORD&gt;[a-z]
{ }
&lt;INSIDE_A_WORD&gt;.|\n
{ ECHO; GOTO 0; }
.|\n
{ ECHO; }
%%
```

D.13. AAT Tables with Finite Automata
int yywrap (void) { return 1; }
void main (void) { yylex(); }
In this code, the part before %% declares the states other than the initial state. The lines between the
two instances of %% correspond to the arrows in our example. At the left, we have the patterns to
match, possibly preceded by a state in which we must be. When the patterns are checked, the first
match will be retained. Thus we place the pattern [BCDFGKLMNPQRSTVWX] first: it means that we are
searching for a consonant (other than ‘h’, which is not in the list). The second pattern is [A-Z], or all
the capital letters. Since the consonant did not match the first pattern, if we find a consonant at this
point, it will necessarily be a vowel or an ‘H’. The pattern in the eighth line is .|\n, which means
“any character”: we can use it because this line comes at the end and thus matches any character
that the other patterns rejected. We shall not go into the details of the code here, for we wished
merely to give the reader the chance to compare the two (the figure and the code) and understand
that they are two ways to represent the same thing: the finite automaton.
But let us return to the case of interest to us: AAT fonts. We have already given two ways to
represent a finite automaton, and here is a third: by writing three tables. These three tables
are the state table, the entry table, and the class table. Where are we headed with these tables?
It should be clear: we are going to store a finite automaton in a TrueType table. Thus we shall
use neither diagrams nor Lex code to achieve our goal. The approach of using three tables is
the only one that is appropriate.
How do we write these three tables? The approach is both easy and ingenious. The first table is
the class table: the glyphs are classified according to the conditions for applying a given action.
In our example, the classes are the consonants (other than ‘h’), the vowels, the letter ‘h’, and
the nonletters.
The second table is the entry table. Here the word “entry” is not used in the sense of “dictionary entry” but rather in the sense of “act of entering”. We might have called it a table of
entering arrows, but that is a bit too Western for our tastes. In any event, it is used to catalog
all the combinations of actions and the targets of the transitions—in other words, the state to
which each arrow points and the action associated with it.
Finally, the third, and most important, table is the state table. The columns correspond to
classes, and the rows correspond to states. The cells contain “entries”, in the sense of the previous table.
Let us review. To implement the automaton in Figure D-9, we need the following ingredients:
• The ovals; that is, the states. We have them: they are the rows in the state table.
• The arrows; that is, the following information: where does the arrow start? under which
condition? where does it lead? which action is associated with it? Here are the answers:
– Where does the arrow start? We have this information in the state table, since we
know that we have a given transition arrow for a given class and a given state.
– Under which condition? Once again, this information is in the state table, since we
know that a given arrow will start from a given state for a well-defined set of classes.
This set of classes is our starting condition.

Appendix D : The TrueType, OpenType, and AAT Font Formats
if non-letter
if non-letter
if non-letter
if consonant, except ‘h’
if consonant, except ‘h’
if vowel
or ‘h’
if vowel
or ‘h’
if non-letter
if letter
keep,
insert a
point
delete,
insert a
point
keep,
insert
a point
keep,
insert
a point
keep
keep
keep
keep
keep
keep
delete
initial state 1
(“line begin”)
initial state 0
(“text begin”)
second
glyph
word
interior
if ‘h’
if letter other than ‘h’
➀
➁
➂
➃
➄



.
➆
➇
Figure D-10: The second example of a finite automaton, with an additional initial state.
– Where does it lead? The entry table answers this question. The state table gives us
a reference to the entry table, and an entry contains, among other things, a “target
state”, which is where the corresponding arrow leads.
– Which action is associated with it? This is the other piece of information contained
in an entry, within the entry table.
In these tables we have all the information needed to implement the diagram. It can be shown
that the converse is also true: the tables can be constructed from the diagram. The two representations are therefore equivalent.
Now we shall describe, by way of an example, the tables associated with the automaton in
Figure D-9 (b). But there is a problem: Apple imposes on us not one initial state, but two:
the start of text and the start of line. Specifically, when text is selected with the mouse, if the
start of the selection is at the beginning of the line, state 1 will be the initial state; otherwise
state 0 will be.
Thus we have to add complexity to our diagram once again. The reader can examine the new
automaton in Figure D-10. We have had to make the following modifications. The former
“initial state” is now called initial state 1 (“start of line”) (the quotation marks around “start of
line” are there to remind us that we are handling not only the start of a line, but much more
as well: we are in this state whenever we are not within a word); there is a new state called
initial state 0 (start of text); when we are in this state, three windows to the future are opened:
if we have a consonant, it is retained, and we move to the second glyph; if we have a vowel, it
is retained, and we move directly to the state inside a word; finally, if we have a nonletter, it is
retained, and we move to initial state 1. Thus the new state is one in which everything flows

```text
D.13. AAT Tables with Finite Automata
out but nothing flows in—which is to be expected, since the text has only one starting point,
just as there is only one birth (in the corporal sense, of course) in a person’s life.
We shall denote the state inside a word as 2 and the state second glyph as 3.
Here is the class table (the numbers from 0 to 3 are reserved by Apple):
Description
Class
Consonants (other than ‘h’)
Vowels
The letter ‘h’
Nonletters (default case)
We have four different actions; let us number them: “retain” (or “do nothing”) will be action 0, “delete” will be action 1, “retain, insert a period” will be action 2, and “delete, insert
a period” will be action 3. Thus the entry table looks like this:
Entry number
Arrow
New state
Action





The reader must have noticed that there are fewer entries than arrows in Diagram D-10. That
is because the arrows , , , , and , , , and , . end in the same states and are
associated with the same actions. Thus each of these groups gives rise to only one entry. The
ingenuity of this table is that only the distinct combinations of a new state and an action are
cataloged.
Finally, the state table:
Classes
States
Initial 0
Initial 1
Inside a word (2)
Second glyph (3)
What can we conclude from the table above? First, that states 0 and 1 have exactly the same
behavior (their rows are identical). Second, that the nonletters are ignored during processing
(their column contains only zeroes). Third, that when we leave state 0 or state 1, the letter ‘h’
is considered a vowel (since ‘Hh’ never occurs). Fourth, and last, that Figure D-10 is more
verbose than all the tables together!
```

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
After this introduction to finite automata, we are ready to describe the AAT tables that use
this technique. Note that we have already encountered a finite automaton previously: it was
used in subtable 1 of the kern table (§D.8.4.2), a subtable specific to AAT.
D.13.2
The morx Table (Formerly mort)
The mort table has shuffled offthis mortal coil. It has been dead since Apple replaced it with
the table morx (for “mort extended”). The morx table is nothing but version 2 of mort; why,
then, was it necessary to change the name? As often happens in the course of human history,
the morx was born because of a regrettable mistake: Apple noticed, when it was already too
late to change anything, that the system’s code did not check the version of the mort table
after a change of font. Every new version of this table will therefore be misunderstood, poorly
received, and disrespected by the system, with more or less severe consequences—failure to
display the font, or perhaps even a revolt by the system, leading to a total crash. The only
solution for avoiding this cascade of horrors was to assign a new name to the second version
of mort: specifically, morx.
Let us now see how morx works. We have already seen that AAT has the concept of feature,
just like OpenType. But rather than using lookups, as OpenType does, AAT offers a system
based on supply and demand. In a morx table, we define some features and some operations
(called “subtables” in AAT jargon). The link between the two is a 4-byte number N that is
used as a series of 32 flags. The morx table—more precisely, a substructure of it that is called
a string—establishes the default value of N, which we shall call Nd.
Suppose that that the user selects a section of text and chooses n features. Let F1 be the first
feature selected. This feature has two numbers that are specific to it: F1,e and F1,d. We shall perform a logical and and a logical or between these values and Nd. The new value of N, which
we shall designate N1, will be N1 = (Nd and F1,d) or F1,e. Likewise, if F2 is the second feature
selected, we have N2 = (N1 andF2,d)orF2,e, and so forth. After all the and and or operations
corresponding to the n features selected, we obtain a number Nn, which we denote N′.
Now we can begin to carry out the operations, in the order established in the font. Each
operation i has a signature in the form of a series of flags, Si, of its own. We perform a logical
and: N′ andSi. If the result is nonzero, we perform the operation.
This method is extremely flexible. First of all, it is the font’s designer who decides which
features and which selectors for those features will come into play in setting up the series
of flags N. If 32 flags are not enough (which happens when there are many features and/or
selectors), we create other “chains”, with new default values and new features.
But the most interesting characteristic of this method is that the features and operations are
independent—what we have called “supply and demand”. The features establish the number N′, which is a sort of “mission statement”. Next, the operations, one by one, compare their
signatures to this “mission statement”. If the result is nonzero, the operation will take place;
otherwise, it will give way to the following operation. The last operation is an empty one that
merely returns control to the system.
On the other hand, we see the importance of the number Nd: even before the user chooses a
single feature, several operations have already been preselected. For example, we can declare
that certain ligatures are required by default. The user can always disable them, but they will
```

D.13. AAT Tables with Finite Automata
be enabled by default. And it is easy to change a font’s default behavior: one merely changes
the number Nd of the corresponding string in the morx table.
The code for the morx table is therefore subdivided, as one would expect, into two sections:
a section that describes the features and one that describes the operations (or “subtables”).
Here is an example of the first section, drawn from the font Skia:
&lt;morx&gt;
&lt;Version value="2"/&gt;
<!-- nChains=2 -->
&lt;chain index="0" defaultFlags="\x00021449"&gt;
&lt;features&gt;
<!-- nFeatureEntries=30 -->
&lt;featureTable index="0"&gt;
&lt;type value="15"/&gt;
&lt;setting value="2"/&gt;
&lt;enableFlags value="\x00040000"/&gt;
&lt;disableFlags value="\xffffffff"/&gt;
&lt;/featureTable&gt;
&lt;featureTable index="1"&gt;
&lt;type value="15"/&gt;
&lt;setting value="0"/&gt;
&lt;enableFlags value="\x00080000"/&gt;
&lt;disableFlags value="\xffffffff"/&gt;
&lt;/featureTable&gt;
...
&lt;/features&gt;
After the usual Version, there is a chain element. The “chain” is a subdivision of morx that is
of no great interest: its only reason for being is the fact that the number N that contains the
flags is of a limited size and can contain no more than 32 flags. When the font’s needs surpass
these 32 flags, we fill up the first N, write the corresponding features and operations, and then
start a new chain with a new N, and so forth, until we have covered all the flags required for
our superfont.
The chain element has two attributes: index (its number) and defaultFlags, which contains
the number Nd (i.e., the default values of the 32 flags) written in hexadecimal form. Within
chain, we have the features: several featureTable elements, each of them having four subelements:
• Its “type” (type). Here one must not assume that the “type” has anything to do with the
feature’s behavior. It is simply a link to the feat table, which we redirect to the name table, which contains the names of the features in every language. This information allows
for displaying the feature’s name on the software’s user interface and for grouping the
corresponding selectors together.
• Its “selector” (setting). Each feature has selectors; here, we give the value desired. Once
again, this information is used only for displaying the selector in question on the user

Appendix D : The TrueType, OpenType, and AAT Font Formats
interface. Recall that the feat table contains a piece of information on the exclusivity of
the selectors: if the selectors are exclusive, they are displayed as radio buttons; otherwise,
they are displayed as checkboxes.
• The numbers enableFlags and disableFlags, which will modify the current value of N
as follows: first, we perform an and with disableFlags; then an or with enableFlags,
which is what we noted above: Ni+1 = (Ni andF1,d)orF1,e.
But why do we need both an and and an or? Suppose that we have two sets of ligatures,
A and B. Then we have two flags: 01 for A and 10 for B, the default value being 00. We
select the string of text and apply set A of ligatures: in order for the number to become 01,
we need an or: 00 or 01 = 01. The enableFlags for A will then be 01. But now suppose
that B must disable A because the designer does not want both sets of ligatures to be used
at the same time. If the enableFlags for B is 10 and we perform 01 or 11, we obtain 11,
which means that both sets of ligatures are enabled. Thus we also need a disableFlags
for B, which will be 10. By computing 11 and 10, we obtain 10, which is B, not A ∪B.
Now we are better equipped to understand the meanings of the names enableFlags and
disableFlags. We enable our own flags and disable the flags for other features—i.e., those
that we wish to exclude.
Now let us examine the operations. It is they that will serve the needs created by the features.
Each operation comes in turn, quite humbly, and compares its signature Si with the number N′. If the result of SiandN′ is nonzero, the operation will be executed. If not, it will forever
hold its peace (well, until the next group of glyphs is examined by the font).
Operations can be of five types. Here, and here only, the “types” are actually significant. No
longer are we in the realm of features, where everything is oriented towards the user interface.
Here we dive in, and what is important is the transformation of glyphs that we have to perform.
There are five types of transformations, which differ from one another in fundamental ways:
• Type 0, a change in the order of the glyphs, called “Indian rearrangement”, since it applies
most of all to the languages of India.
• Type 1, glyph substitution according to the previous glyph, pompously called “contextual
substitution”.
• Type 2, ligatures (from 1 to 16 glyphs!).
• Type 4, glyph substitution pure and simple, even more pompously called “noncontextual
glyph substitution”.
• Type 5, insertion of between 1 and 31 glyphs, according to context.
These types (except type 4) have in common the fact that they occur within the scope of a
finite automaton. The differences among the corresponding finite automata lie mainly in the
actions that they perform. Below, we shall examine the first type in detail, and then present
only the ways in which the other types differ from it.

D.13. AAT Tables with Finite Automata
D.13.2.1
Operations of type 0: changing the order of the glyphs
As a finite automaton, this operation is described in TTX in the form of three tables: the class
table, the state table, and the entry table (or table of “in-bound arrows”). Before we begin to
describe the classes, here is the preamble from an operation of type 0, drawn from the font
Monotype Devanagari, which was furnished standard with Mac OS 8.5 but was dropped from
later versions of Mac OS:
&lt;IndicRearrangementSubtable index="0"&gt;
&lt;coverage value="\x0000"/&gt;
&lt;subFeatureFlags value="\x00000001"/&gt;
&lt;stateSize value="11"/&gt;
The element that contains the data for this operation is IndicRearrangementSubtable. The
first three subelements are
• coverage, a number that consists of three flags and the type of the operation. The flags
are \x8000 (if the flag is enabled, the operation applies only to vertical typesetting; if it is
disabled, the operation applies only to horizontal typesetting), \x4000 (a very important
flag: if it is enabled, the string of glyphs is red starting from the end!), \x2000 (a flag that
allows us to cancel the choice indicated by flag \x8000: if it is enabled, the operation
applies to both horizontal and vertical typesetting).
• subFeatureFlags, the signature Si of this operation, which will be compared (through a
logical and operation) with N′ to determine whether the operation should be performed
or not.
• stateSize, the size in bytes of a row in the state table; in other words, the number of
classes.
Once it has read these lines, the AAT processor already knows whether it should perform the
operation or not, and, if necessary, in which direction it should read the glyphs.
Now let us continue with the class table:
&lt;classes&gt;
<!-- nbClasses=11 -->
...
&lt;class value="1"&gt;
&lt;glyph name="edeva"/&gt;
&lt;glyph name="aideva"/&gt;
...
&lt;/class&gt;
...
&lt;class value="5"&gt;
&lt;glyph name="rvocalicdeva"/&gt;
&lt;/class&gt;
...
&lt;/classes&gt;

```text
Appendix D : The TrueType, OpenType, and AAT Font Formats
The classes element contains a class subelement for each class. Each of these subelements
contains some glyphs, identified by their names. No surprise there.
The state table is just as simple:
&lt;states&gt;
<!-- nbStates=10 -->
&lt;state value="0"&gt;
&lt;entry class="0" value="0"/&gt;
&lt;entry class="1" value="0"/&gt;
...
&lt;entry class="10" value="0"/&gt;
&lt;/state&gt;
...
&lt;state value="10"&gt;
&lt;entry class="0" value="6"/&gt;
&lt;entry class="1" value="6"/&gt;
...
&lt;entry class="5" value="6"/&gt;
&lt;/state&gt;
&lt;/states&gt;
For each state state in states (with an ‘s’), there is an entry entry for each class. Each entry
contains, in the form of attributes, the number of the class (class) and the number of the
corresponding entry (value).
Finally, the entry table (or table of “in-bound arrows”):
&lt;entries&gt;
<!-- nbEntries=12 -->
&lt;entry value="0" newState="0"/&gt;
&lt;entry value="1" newState="2" markFirst="1"/&gt;
&lt;entry value="2" newState="0" markLast="1" verb="1"/&gt;
&lt;entry value="3" newState="3"/&gt;
&lt;entry value="4" newState="4"/&gt;
&lt;entry value="5" newState="5" markLast="1"/&gt;
&lt;entry value="6" newState="0" dontAdvance="1" verb="4"/&gt;
&lt;entry value="7" newState="6" markLast="1"/&gt;
&lt;entry value="8" newState="7"/&gt;
&lt;entry value="9" newState="9" markLast="1"/&gt;
&lt;entry value="10" newState="8"/&gt;
&lt;entry value="11" newState="0" markLast="1" verb="4"/&gt;
&lt;/entries&gt;
The entries element contains the entry elements that correspond to the entries. Each entry
contains, in the form of attributes, its number (value), the state into which the arrow leads
```

D.13. AAT Tables with Finite Automata
(newState), and the action. But things turn complicated here. To describe the action, we use
several attributes, which vary from one type of operation to another.
Here are the attributes specific to an operation of type 0:
• markFirst, whose value can be 0 or 1 (if the attribute is omitted, its value is 0). The action
consists of marking the current glyph as being the first to be rearranged.
• markLast is similar, but the current glyph is the last of the glyphs to be rearranged; in
other words, this operation initiates rearrangement.
• verb, a number between 0 and 15 that indicates the nature of the rearrangement (see
below).
• dontAdvance, whose value can be 0 or 1; this attribute appears in all operations and
means that we must perform the requested action, change state, and then act as if we
have not yet processed the glyph and read it again.
Now all that we have left to describe is the rearrangement itself (the verb attribute). To do
so, we shall use the following notation: ‘1’, ‘2’, ‘3’, ‘4’ will be four glyphs that we are going to
rearrange, and ‘XYZ’ will be a string of one or more glyphs that appear among the candidates
for rearrangement and that will not be modified. For example, if the string ‘abcd’ becomes
‘dbca’, we can say that ‘1’ is ‘a’, ‘2’ is ‘d’, and ‘XYZ’ is ‘bc’. Here are all the possible cases of
rearrangement and the associated values of verb:
verb
Before
After
verb
Before
After
-
-
1-XYZ-2-3
2-3-XYZ-1
1-XYZ
XYZ-1
ditto
3-2-XYZ-1
XYZ-1
1-XYZ
1-2-XYZ-3
3-XYZ-1-2
1-XYZ-2
2-XYZ-1
ditto
3-XYZ-2-1
1-2-XYZ
XYZ-1-2
1-2-XYZ-3-4
3-4-XYZ-1-2
ditto
XYZ-2-1
ditto
3-4-XYZ-1-2
XYZ-1-2
1-2-XYZ
ditto
4-3-XYZ-1-2
ditto
2-1-XYZ
ditto
4-3-XYZ-2-1
Let us mention an undeniable benefit of finite automata that becomes clear here. What we
have denoted “XYZ” in the table above is an arbitrarily long string of glyphs. For instance,
we can “mark” a glyph, move forward, and much farther along find its “companion” for
permutation. Irrespective of what we read between the two glyphs, we can always apply a
rearrangement between them, according to the table. That is one thing that would be hard
to do in OpenType, since all of the patterns for strings in OpenType are of a fixed length.
An example: in the scripts of India and Southeast Asia, when consonants occur consecutively
without any intervening vowels, we speak of “consonant complexes”. These complexes can
sometimes include as many as six or seven consonants. When the last consonant of a complex

Appendix D : The TrueType, OpenType, and AAT Font Formats
is an ‘r’, the ‘r’ will appear graphically at the beginning of the string. Thus here is a typical type
of situation that an AAT operation of type 0 allows us to solve: we mark the first consonant
after a vowel or a nonletter, we accumulate consonants, and when we encounter an ‘r’, it is
placed before the marked consonant, irrespective of the distance traversed and the glyphs that
have been set in the meantime.
D.13.2.2
Operations of type 1: contextual substitution
By contextual substitution, we mean the substitution of two glyphs (possibly separated by
a string of glyphs) by two other glyphs. The first of the two will be “marked”, and when we
reach the second, the two will be replaced with two other glyphs, provided that we are still in
the right state. We may also change only one of the glyphs. And there is symmetry between
the “marked” glyph (which comes first) and the “active” glyph (which comes second), since
we can read the glyphs from start to finish or from finish to start, according to the value of
flag 0xx4000 in coverage.
An example: in the font Apple Skia, there is a feature that assists with entering mathematics.
When we enter an asterisk (∗) surrounded by spaces or digits, the asterisk is replaced with
a multiplication sign (×). That does not occur when the asterisk is between two letters, for
example. How does this substitution work? There are four states. When we are in the initial
state and a digit or a space is read, we switch to state 2 (which we could describe as the “state for
waiting for an asterisk”). In state 2, when an asterisk is encountered, we mark it and change
to state 3 (which could be described as the “state in which we have just read an asterisk”).
There are two ways to get out of state 3: if the following glyph is neither a space nor a digit,
we return to state 0, and the game is over; conversely, if the following glyph is a space or a
digit, we replace the asterisk with the multiplication sign and return to state 2 to wait for
another possible asterisk.
From the point of view of TTX’s code, this operation is only slightly different from the previous one. The global element is ContextualGlyphSubstitutionSubtable. The class, state, and
entry tables are the same, with only one small difference: the entry entries have their specific
attributes, which describe the actions connected to contextual substitution. These actions are
• setMark (0 or 1), which marks the current glyph.
• dontAdvance (0 or 1), as in the previous operation.
• substituteMarkedGlyph, whose value is the name of a glyph. When this attribute takes
a nonzero value, the marked glyph is to be replaced by the glyph in question. If the attribute is omitted, the marked glyph cannot be modified.
• substituteCurrentGlyph is the same, but for the current glyph.
For example, suppose that we have the string ‘f’, ‘i’, and that we would like to replace the first
glyph with “fi” and the second with an empty glyph. That is a very practical way to obtain
a ligature. When we come upon an ‘f’, we mark it. Next, when the ‘i’ is read, we replace the
marked glyph (i.e., the ‘f’) with “fi” and the current glyph (i.e., the ‘i’) with the empty glyph
(for example, the glyph .null).

```text
D.13. AAT Tables with Finite Automata
D.13.2.3
Operations of type 2: ligatures
In the preceding type of operation, we saw how to obtain simple ligatures. Type 2 is much
more powerful and, as it happens, more complex. Specifically, this operation uses a stack of
glyphs onto which all the marked glyphs are placed as components of the ligature. Then it
will pop the series of glyphs and will perform several replacements. The size of the stack is 16;
therefore, we can obtain ligatures with up to 16 components!
The global element for this operation is LigatureSubstitutionSubtable. Its code is richer
than that of the previous operations. First of all, entry has, once again, its own attributes:
setComponent (whose value is 0 or 1), to indicate whether the current glyph is a component
of the ligature; dontAdvance, as in the preceding types; ligature, to indicate the name of the
glyph for the ligature that will replace the last of these marked glyphs.
Here is an example of the entries table, drawn from the font Skia:
&lt;entries&gt;
<!-- nbEntries=12 -->
&lt;entry value="0" newState="0" setComponent="0"/&gt;
&lt;entry value="1" newState="2" setComponent="1"/&gt;
&lt;entry value="2" newState="1" setComponent="0"/&gt;
&lt;entry value="3" newState="2" setComponent="0"/&gt;
&lt;entry value="4" newState="3" setComponent="1"/&gt;
&lt;entry value="5" newState="0" setComponent="1" ligature="fi"/&gt;
&lt;entry value="6" newState="0" setComponent="1" ligature="fj"/&gt;
&lt;entry value="7" newState="0" setComponent="1" ligature="fl"/&gt;
&lt;entry value="8" newState="0" setComponent="1" ligature="ft"/&gt;
&lt;entry value="9" newState="0" dontAdvance="1" ligature="ff"/&gt;
&lt;entry value="10" newState="3" setComponent="0"/&gt;
&lt;entry value="11" newState="0" setComponent="1" ligature="ffi"/&gt;
&lt;entry value="12" newState="0" setComponent="1" ligature="ffl"/&gt;
&lt;/entries&gt;
We can see that for the ligatures ‘fi’, ‘g’, ‘fl’, and ‘ft’, which are “terminal”, there is an entry
whose new state is the initial state (0), whose setComponent has the value 1 (and therefore
its second glyph—‘i’, ‘j’, ‘l’, ‘t’—is indeed a component), and whose ligature has a nonempty
value. This is the simple case.
Now let us see what happens for triple ligatures. When an ‘f’ occurs, we are in state 2. When
a second ‘f’ occurs, we move to state 3 via entry 4. This entry tells us that the second ‘f’ is
indeed a component, but nothing more than that. At that point, three cases are possible:
1. What follows is an ‘i’. We then move to state 0 via entry 11. This entry concludes the
process.
2. What follows is an ‘l’. We do as for the ‘i’, but using entry 12.
3. What follows is neither an ‘i’ nor an ‘l’. Ordinarily we would say “OK, we’ll set the ‘ff’
and return to the starting point”. But things are not so simple: after the second ‘f’, we
are in state 3. The following glyph takes us to state 0. But suppose that the next glyph is
```

Appendix D : The TrueType, OpenType, and AAT Font Formats
another ‘f’. After that ‘f’ we will again be in state 0, whereas ordinarily after an initial ‘f’
we would be in state 2 to prepare for a possible ligature! Thus we have skipped a step: the
switch from state 3 to state 0 caused us to skip state 2, where we should be. That is why
we use the attribute dontAdvance. We thus act as if we had not seen the ‘f’ and proceed to
examine it again. In the meantime, however, we have switched to state 0, and therefore
the ‘f’ will move us back to state 2, and everything works as it should.
D.13.2.4
Operations of type 5: insertion of glyphs
The aim of this operation is to insert glyphs before or after the marked glyph or the current
glyph. There are two types of inserted glyphs: those that are attached to the preceding or following glyph, and those that lie at a certain distance and seem to be independent of the glyph
that caused their insertion. The canonical examples are, for the first case, the connection of
Arabic letters, and, for the second, the Khmer “split vowels”:
+
ligature
split insertion
insertion of kashida
The actual difference between these two types of inserted glyphs is at the level of text selected
by the user. In the first case, the glyphs cannot be dissociated from the current glyph—that is,
the one that caused them to appear. In the second case, they attach themselves to the marked
glyph. For example, in the case of the split vowels, the following phenomenon occurs: a group
of consonants ‘BCD’ followed by the vowel ‘aA’ becomes ‘aBCDA’, where ‘DA’ is a new glyph
that replaces ‘D’ and ‘a’ attaches itself to ‘B’. The possible selections that the user can make
within ‘aBCDA’ are therefore ‘aB’, ‘C’, and ‘DA’. On the other hand, in the case of Arabic, if
‘kml’ becomes ‘k__m__l’, the possible selections are ‘k__’, ‘m__’, and ‘l’.
We can insert up to 31 glyphs before or after the marked glyph, and the same number before
or after the current glyph.
In TTX, the global element for this operation is GlyphInsertionSubtable. The TTX code for
this operation is slightly richer than the code for the previous operation: while the class and
state tables are the same, the entry tables include entry entries that, for the first time, can
have content. Indeed, up to now, we have placed the value for a substitution or a ligature in
an entry attribute. In this case, however, there is a variable number of glyphs to insert; thus
we cannot forgo the introduction of new XML elements. The entry element can contain two
elements: currentInsertList (a list of glyphs to insert before or after the current glyph) and
markedInsertList (likewise, but before or after the marked glyph). For its part, entry has
the following attributes:
• value: its number.
• newState: the new state that is reached when we follow this arrow.
• setMark: mark the current glyph.
• dontAdvance: act as if the glyph has not been processed and process it again after changing
state.

D.13. AAT Tables with Finite Automata
• currentIsKashidaLike (0 or 1): do the glyphs inserted before or after the current glyph
behave like the kashida (1), or more like “split” vowels (0)?
• markedIsKashidaLike (0 or 1): the same, but for the marked glyph rather than the current glyph.
• currentInsertBefore (0 or 1): should glyphs be inserted before (1) or after (0) the current glyph?
• markedInsertBefore (0 or 1), the same, but for the marked glyph.
• currentInsertCount (from 0 to 31): how many glyphs shall we insert before or after the
current glyph?
• markedInsertCount (from 0 to 31): the same, but for the marked glyph.
Each of currentInsertList and markedInsertList can contain up to 31 Glyph elements, for
which the value attribute contains the glyph’s name.
D.13.2.5
Operations of type 4: simple glyph substitution
We have left this operation for last because it is in a way the “poor sibling” of the operations:
it is not a finite automaton but rather a table of correspondences between replaced glyph and
replacement glyph:
&lt;NonContextualGlyphSubstitutionSubtable index="0"&gt;
&lt;coverage value="\x2004"/&gt;
&lt;subFeatureFlags value="\x00000001"/&gt;
&lt;substitutions&gt;
<!-- nSubstitutions=10 -->
&lt;substitution from="zero" to="zerooldstyle"/&gt;
&lt;substitution from="one" to="oneoldstyle"/&gt;
&lt;substitution from="two" to="twooldstyle"/&gt;
&lt;substitution from="three" to="threeoldstyle"/&gt;
&lt;substitution from="four" to="fouroldstyle"/&gt;
&lt;substitution from="five" to="fiveoldstyle"/&gt;
&lt;substitution from="six" to="sixoldstyle"/&gt;
&lt;substitution from="seven" to="sevenoldstyle"/&gt;
&lt;substitution from="eight" to="eightoldstyle"/&gt;
&lt;substitution from="nine" to="nineoldstyle"/&gt;
&lt;/substitutions&gt;
&lt;/NonContextualGlyphSubstitutionSubtable&gt;
Apart from the horribly long name of the global element (NonContextualGlyphSubstitutionSubtable), there is no surprise here: we find coverage (the nature of the operation) and
subFeatureFlags (the number Si that is used to determine whether or not this operation is
to be executed), just as in the other tables. Immediately afterwards comes an element substitutions that contains substitution elements (with no ‘s’). Each substitution has two

Appendix D : The TrueType, OpenType, and AAT Font Formats
attributes that contain glyph names: from for the original glyph and to for the glyph that is
obtained after the substitution.
The sample code above is for the operation that switches from “modern” to old-style digits.
D.13.3
The just Table
No, it is not the given name of the author of TTX, Just van Rossum. As with the JSTF table
in OpenType, the just table in AAT manages the optimization of the justification of lines.
We shall see that the developers of AAT had a whale of a time with this one. With it, we can
do things as simple as changing the interword space or as complex as using font variation to
expand or contract certain specified glyphs.
Like the other tables, this one begins with a version element and a format element, which
have fixed values. It contains one or two JustificationTable elements, according to the
direction of typesetting (horizontal or vertical), which is given by the attribute of the
same name:
&lt;just&gt;
&lt;Version value="1"/&gt;
&lt;Format value="0"/&gt;
&lt;JustificationTable direction="h"&gt;
The table is divided into three parts:
• The table of justification classes
• The quantitative table
• The qualitative table
Let us start with the first of these.
D.13.3.1
The table of justification classes
These classes assign to each glyph in the string a class that will manage its behavior with
respect to justification. It is clear that the same glyph may behave differently according to
its position in the string: we can more easily expand the left side-bearing of the letter ‘a’ if it
appears at the beginning of a word; otherwise, the expansion will be what we call letterspacing,
which not everyone fancies. Therefore, we absolutely cannot use a simple class table in which
each glyph name is associated with a fixed and unchanging class value.
The solution that AAT proposes is to use a finite automaton to assign justification classes. Here
we must be careful not to confuse the glyph classes of the finite automaton (the class table is
an indispensable ingredient of any finite automaton) with the justification classes. Here is the
code for one such finite automaton:
&lt;justClassTable&gt;
&lt;stateSize value="9"/&gt;
&lt;classes&gt;

D.13. AAT Tables with Finite Automata
<!-- nbClasses=9 -->
...
&lt;class value="1"&gt;
&lt;glyph name="a"/&gt;
&lt;glyph name="b"/&gt;
...
&lt;glyph name="z"/&gt;
&lt;/class&gt;
...
&lt;/classes&gt;
&lt;states&gt;
<!-- nbStates=4 -->
&lt;state value="0"&gt;
&lt;entry class="0" value="0"/&gt;
&lt;entry class="1" value="0"/&gt;
...
&lt;entry class="8" value="0"/&gt;
&lt;/state&gt;
...
&lt;/states&gt;
&lt;entries&gt;
<!-- nbEntries=13 -->
&lt;entry value="0" newState="0"/&gt;
...
&lt;entry value="4" newState="3" currentClass="3"/&gt;
...
&lt;/entries&gt;
&lt;/justClassTable&gt;
This code is no different from that of the other finite automata that we have seen up to now.
The global element is justClassTable, and, as always, the entry elements have a certain
number of attributes that are specific to this finite automaton:
• setMark (0 or 1): mark the current glyph.
• dontAdvance (0 or 1): act as if the glyph had not been processed and read it again after
changing state.
• markClass (between 0 and 255): the justification class of the marked glyph.
• currentClass (between 0 and 255): the same, but for the current glyph.
Thus we can say that we assign to ‘a’ class 35 if it is at the beginning of a word and if it is
followed by an ‘f’: to do so, we will mark an ‘a’ that occurs after a nonletter by using setMark,
and then we will watch for the appearance of an ‘f’, and when the ‘f’ does appear, we will give
markClass the value 35: thus class 35 will be assigned not to the ‘f’ that we have just read but
to the preceding ‘a’. Of course, nothing stops us from assigning a class to the ‘f’ at the same
time and/or marking it before continuing.

Appendix D : The TrueType, OpenType, and AAT Font Formats
At this point, we have assigned justification classes to our glyphs in the most intelligent way
possible. Now we need to make use of them.
D.13.3.2
The quantitative table
What we have blandly called the “quantitative table” has a very cool English name: width delta
clusters. Here is where the classes are associated with quantitative behaviors. In other words,
this is where we decide how much we can expand or contract a glyph, whether to do so at the
left or at the right, and what the global priority of this operation will be. In the following
table (the “qualitative table”), we shall decide how the glyph will fill in the extra space that
we have given it, or how it will squeeze into the more limited space that we have allotted.
Here is an example of a quantitative table:
&lt;widthDeltaClustersTable&gt;
&lt;widthDeltaCluster&gt;
&lt;widthDeltaPair index="0" justClass="0"
beforeGrowLimit=".5" beforeShrinkLimit="0"
afterGrowLimit=".5" afterShrinkLimit="0"
growUnlimitedGap="1" shrinkUnlimitedGap="1"
growPriority="2" shrinkPriority="2"/>
...
&lt;/widthDeltaCluster&gt;
&lt;/widthDeltaClustersTable&gt;
The global element is widthDeltaClustersTable, which contains widthDeltaClusters,
which in turn contain widthDeltaPairs. The latter are the elements that match up a justification class (justClass) with a certain number of quantitative properties:
• beforeGrowLimit and afterGrowLimit, expressed in ems: how much we can expand the
width (the width vector) of this class of glyphs at the left (or at the top, if we are setting
type vertically) or at the right (or bottom).
• beforeShrinkLimit and afterShrinkLimit, expressed in ems—the same, but for reducing the width.
• growUnlimitedGap and shrinkUnlimitedGap (0 or 1): should the values of the attributes
*GrowLimit and *ShrinkLimit be considered “infinite”, thus giving us carte blanche to
do anything?
• growPriority et shrinkPriority (between 0 and 3): the priority that we assign to this
instance of expansion or narrowing. Four possible cases:
– Value 0: “kashida priority”. This is the highest priority. Kashidas are there to absorb
all the extra interword space, and they can be used excessively. (This type of straight
kashida does not necessarily yield good typographical results; see §D.9.5.1).
– Value 1: “whitespace priority”. This is the priority for interword spaces. This priority
is assigned to the pseudoglyphs “space”, “unbreakable space”, etc.
– Value 2: the default case for the glyphs that are somehow involved in justification.

D.13. AAT Tables with Finite Automata
– Value 3: “zero priority”. The exceptional case for glyphs that should not be involved
in justification. We can also create a justification class with zero values for expansion
and narrowing; the result will be the same.
Now we know to what extent we can play with the width of each glyph in our string. All that
we need to know is how, and that is what we shall see in the following section.
D.13.3.3
The qualitative table
This involves associating with a justification class several possible actions. These actions
will be performed in order until justification is complete. The global element for this table
is postcompTable. It contains one or more glyphActionRecords, which in turn contain
glyphActions. Each glyphAction is therefore a justification action; it has two parameters,
given by their attributes: the justification class to which it applies (class) and the type of
action to perform (type).
Here is a typical example:
&lt;postcompTable&gt;
&lt;glyphActionRecord index="0"&gt;
&lt;glyphAction index="0" class="35" type="0"&gt;
...
&lt;/glyphAction&gt;
&lt;/glyphActionRecord&gt;
&lt;/postcompTable&gt;
All that we need to know is the content of glyphAction: it depends on the action’s type. Here
are the various types that are available:
• Type 0: ligature decomposition. We decide to decompose some ligatures in order to expand
some words slightly. This approach should be used with care, since we must refrain from
disturbing the reader’s eye by setting an ‘fi’ in one place and an ‘fi’ in another—not to
mention committing semantic blunders by decomposing ligatures in German, since that
is done only for compound words (see the discussion in §D.9.5.2). Example:
&lt;glyphAction index="0" class="35" type="0"&gt;
&lt;decomposition lowerLimit=".25" upperLimit=".25" order="3"&gt;
&lt;Glyph index="0" value="f"/&gt;
&lt;Glyph index="1" value="f"/&gt;
&lt;Glyph index="2" value="i"/&gt;
&lt;/decomposition&gt;
&lt;/glyphAction&gt;
We see that glyphAction (which is of type 0) contains a subelement decomposition that
has three attributes. Among them, lowerLimit and upperLimit give the minimum and
maximum values, expressed in ems, for which the ligature will be decomposed; order
gives a relative order for the choice of ligatures to break up: when the software must
choose among various ligatures to break up, it will use this number to do the job in the
optimal order.

Appendix D : The TrueType, OpenType, and AAT Font Formats
On the other hand, glyphAction contains some Glyphs, which are those into which the
ligature will be decomposed.
• Type 1: glyph insertion. Here we merely insert a glyph that will be distorted horizontally
to fill the space that we ask it to fill. Here is an example:
&lt;glyphAction index="1" class="35" type="1"&gt;
&lt;addGlyph value="kashida"/&gt;
&lt;/glyphAction&gt;
The addGlyph element contains the name of a glyph to insert, in the form of a value of
the value attribute.
• Type 2: intelligent glyph insertion. Here we do a bit better than in type 1: we set a limit,
measured in ems, for the width. If adding the glyph in question causes the limit to be
exceeded, we replace the original glyph (the one whose justification class spawned this
action) with another glyph. The idea is that if we add a very long kashida, we may just
as well take a wider version of the original glyph, which could only improve the aesthetic
result. Thus we try to salvage what we can and replace kashidas (which, by definition,
are typographically unpleasant) with specially designed wider forms of letters. Here is an
example of one such action:
&lt;glyphAction index="2" class="35" type="2"&gt;
&lt;addGlyph value="kashida"/&gt;
&lt;substGlyph threshhold="1.5" value="swashnoon"/&gt;
&lt;/glyphAction&gt;
A new element is found in the addGlyph of type 1: substGlyph. Here we call for replacing
the original glyph with the one given in the value attribute of substGlyph, if and only
if the value of the extra space required is greater than the treshhold attribute, expressed
in ems.
• Type 3: glyph stretching. We stretch the glyph horizontally to fill the space available. The
element glyphAction is empty in this case, since no extra information is needed.
• Type 4: glyph stretching managed by font variation. This is the high-tech version of type 3:
rather than blindly stretching a glyph, we use an axis of variation in the font to obtain the
same result in a neat manner. Example:
&lt;glyphAction index="4" class="35" type="4"&gt;
&lt;ductileGlyph variationAxis="duct" minimumLimit="0.7"
maximumLimit="2.0" noStretchValue="1.0"/>
&lt;/glyphAction&gt;
Here we are using ductileGlyph, which has four attributes:
– variationAxis, which answers the question “which axis is the axis of variation?” In
the example, we can take wdth, the axis for widths; but the AAT specification allows
us to create an axis on the fly, called duct.

D.13. AAT Tables with Finite Automata
– minimumLimit and maximumLimit, which give the extreme values at which variation
is still permitted.
– Finally, noStretchValue, which gives the value at which variation is not allowed. Its
default value is 1.
• Type 5: repeated insertion of a glyph. In types 1 and 2, we added only one glyph to the string
in order to optimize justification. Type 5 allows us to insert any number of copies of the
same glyph. Example:
&lt;glyphAction index="1" class="35" type="5"&gt;
&lt;addGlyph flags="0" value="kashida"/&gt;
&lt;/glyphAction&gt;
As in type 1, the addGlyph contains the name of the glyph to be inserted, in the form of
a value of the value attribute.

```text
E
TrueType Instructions
TrueType instructions have the same purpose as PostScript hints: the optimization of the
bitmap rasterization of glyphs. That is why people often speak of “TrueType hints”—a false
term that loses the meaning of “hint”, which is “indication”, “suggestion”. There is a fundamental difference between the strategies for optimizing rasterization that the PostScript and
TrueType fonts use. In the former, the font’s designer gives a few indications to the PostScript
interpreter, in the hope that his wishes will be granted. What he provides are nothing but indications: a few relevant dimensions, such as the height of the lowercase letters and the thickness
of the strokes, and a few strokes that he would like to have rendered in the same way. These
data are supplied to the “black box” that is the interpreter, and one can only hope that they
will be used appropriately. But there is no guarantee as to the final result—only the promises
of Adobe, balanced by a few arguments such as “if you give us the correct hints, we’ll give
you a good optimization”, which could also be interpreted as “if the optimization is poor,
the hints you gave us were incorrect; don’t blame us!”
TrueType’s strategy is different: one provides some clear and precise instructions to the TrueType processor and expects that they will be applied. A set of instructions is a program, written
in a syntax similar to assembly language. This approach is also more democratic, since anyone
can write his own TrueType rendering engine: all that is required is to follow the instructions
to the letter, according to the descriptions given in the specifications of Microsoft and Apple.
We have much more control, but also much more responsibility. But before we begin, we
must learn and master the programming language.
You may be wondering why you should bother to learn this language if there are tools for producing TrueType glyphs with instructions in an interactive graphical manner, as we demonstrated abundantly in Chapter 13. Such tools do indeed exist, but it must be acknowledged
that it is far harder to create interactive tools for writing code in TrueType instructions than
for designing glyphs in TrueType. To design glyphs, one need only place the points in the right
places and indicate whether they are points on the curve or control points. That can be done
```

```text
on the screen through the use of the mouse. But how can instructions be represented graphically? Our programming language includes variables, subroutines, tests, loops—in short,
series of instructions that are executed in a certain order, which depends on the context.
All that we can expect from a graphical utility is one window for writing code and another
in which we can watch the result unfold step by step, instruction by instruction, as in the
IDEs for traditional programming languages. That is the approach adopted by FontForge (see
page 546). Other software, such as FontLab, page 520, or Visual TrueType, page 529, offers us
the possibility of indicating certain operations in a graphical manner. The software will take
our indications and turn them into a program of TrueType instructions. Here only a subset
of the language’s features is available to us, but often it is better to let the software instruct
the font automatically, through what we call autohinting.
In this appendix, we shall attempt to refute the claim of Luc Devroye [116], who said that
“If you are not a computer scientist with at least a B average from MIT, you can forget about
understanding the TrueType specs.” TrueType instructions have a reputation for being complex and incomprehensible; it is time to shatter that reputation and show that, while there is
indeed a certain amount of complexity, there is also quite a bit of logic and common sense.
The main reason for the apparent complexity of TrueType instructions is the logic of assembly languages. In a third-generation programming language, such as C or Pascal, one writes
commands (which have names) followed by their parameters. There are, of course, global
variables; the commands have access to them, and thus the result of a command often depends as well on parameters other than those formally supplied; but that is something that we
can avoid when programming as we should. And it does not cost a great deal of computational
time to supply the same parameter three or four times to three consecutive commands.
In the language for TrueType instructions, we wish to avoid repetition. For instance, if two
consecutive commands must operate on the same point, we prefer to keep that point in memory and write only the commands. That need gave rise to the concept of a reference point: being
a reference point means that the given point will be used by several consecutive instructions.
If the same point is used by several consecutive instructions, there will be fewer instructions
to execute than if we were required to rewrite the point’s number each time.
On the basis of this reflection, we turn reference points (there are three of them!) into a true
method. Most instructions use reference points and assign new values to them. For example,
when we write instructions, there is, behind the scenes, a ballet of reference points that is performed, without any evidence of it in the code. We have restored this ballet of reassignments
of points in the comments to the samples of code presented a bit later in this appendix.
Let us consider a metaphor. When we learn to drive, we learn to pay attention to a relatively
large amount of information at the same time (the vehicle’s direction, its speed, the other vehicles, the rear-view mirror, the clutch, the pedestrians, the presence of any police officers, and
so on). The same is true of TrueType instructions: to understand them, we must constantly
keep in mind the current reference points, the current vectors, the stack and the storage area,
the zones, etc.
We hope that this appendix will show the reader how all these elements interact and that it
will reveal the full potential of TrueType instructions.
The primary bibliographic references are the specifications of Microsoft [258] and Apple [56],
as well as a few introductory texts [102, 263, 59].
```

```text
E.1. Basic Concepts
E.1
Basic Concepts
We shall briefly review the most important concepts of TrueType instruction: reference
points, freedom and projection vectors, the interpreter’s stack and the instruction stream,
and a few less important concepts such as zones, the cut-in, etc.
E.1.1
Interpreter’s Stack, Instruction Stream
Let us begin at the beginning. Just as in the PostScript language, there is a stack for the interpreter, on which the instructions place their arguments to be read by other instructions.
But unlike the PostScript language, not everything is placed on this stack systematically. For,
alongside the stack, there is also the instruction stream. The instructions themselves are thus
not on the interpreter’s stack; only the data generated by the commands are found there. But
there are also hard-coded data in the font that appear in the instruction stream. There are
instructions whose role is to retrieve values from the instruction stream and place them on
the interpreter’s stack.
We work on a plane containing a number of points: the starting points, control points, and
ending points of the Bézier curves, which form the glyph’s various contours, and which are
given in the font’s glyf table, before the section dedicated to TrueType instructions. In this
table, we provide each point’s coordinates and indicate whether the point lies on the curve or
offit—i.e., whether it is a control point.
The task involves modifying the points’ coordinates to adapt them to the grid of pixels being
used. We can even convert a point on the curve into a control point and vice versa, but that
is rather uncommon (and can have quite drastic consequences).
E.1.2
Reference Points
For reasons explained in the previous section, we have three reference points: rp0, rp1, rp2.
These points are used as parameters to the instructions. We say that “this instruction takes
rp0 and does that with it”, etc. The instruction MIRP[], for example, retrieves two numbers
from the interpreter’s stack, but it also uses the point rp0. After its execution, the points
rp1 and rp2, and sometimes even rp0, have different values. Thus we observe reassignments of
values, carried out in the background, that have a decisive effect on the program’s execution.
E.1.3
Freedom and Projection Vectors
Let us now discuss vectors. We measure and modify distances between points; to do so, we
switch to polar coordinates: instead of saying that we “move this much horizontally and that
much vertically”, we say that we “move this much in a given direction”, called the freedom
vector. To measure distances, we proceed in the same way: we measure not the direct distance
between two points but the distance between their projections onto an axis. The direction of
that axis is the projection vector, which is not necessarily the same as the freedom vector.
These two vectors are used together. If I say “to go from p to p′ I move point p a distance of d”,
that actually means “I move point p in the direction of the freedom vector as much as necessary for the projection of pp′ onto the projection vector to be d”. Of course, the two vectors
```

cannot be orthogonal, else we would have infinite amounts—amounts that the computer, unlike mathematicians, does not appreciate. Here are some useful techniques. E.1.4 Table of Control Vectors and Storage Area There are two ways of setting values aside for subsequent reuse: either storing them in the control value table (CVT), a data structure contained in the TrueType table cvt, or storing them in the storage area. The storage area is temporary, and its effect is limited to the current glyph, whereas the CVT is shared by all the glyphs in the font. E.1.5 Touched and Untouched Points We have the concepts of touched and untouched points. A “touched point” is a point whose position has been modified by an instruction. What is useful about untouched points is that there is a magical instruction that corrects their positions by performing interpolation on the positions of the touched points, as well as any necessary rounding. In other words, this instruction (named IUP[]) will restore the shape of a glyph that our instructions may have seriously altered. There is a way to “untouch” touched points so that they can be processed by IUP[]. E.1.6 Minimum Distance and Cut-In Another interesting notion is that of minimum distance. It ensures us that between two points there will always be a space of at least 1 pixel, come what may. For example, in an ‘o’ there will always be a hole in the middle, no matter what the point size, because the hole is a property sine qua non of the letter (which would become an ordinary bullet without it). There is also an amount called the cut-in. It is a threshold below which two coordinates are equated at the pixel level. It resembles the blue values of PostScript and allows for establishing a certain degree of uniformity among the glyphs. At the same time, when the difference between two points exceeds that threshold, it can be taken to be a relevant difference—an aesthetic characteristic of the font. For example, a font that deliberately chooses to make the two downstrokes of the ‘H’ uneven in height, like the ‘H’ in the very funny font Garamouche of the P22 foundry, which claims to be the hypothetical work of an intoxicated Garamond, should have a cut-in less than the difference between the downstrokes, else the difference may be eliminated. E.1.7 Twilight Zone and Zone Pointers To create “temporary” points that will not ultimately effect the glyph’s contour, we double our workspace: there will be a real workspace and one for scratch work. In TrueType jargon, these two workspaces are called zones. The “scratch” workspace is also called the “twilight zone”, after the famous American science-fiction series by Rod Serling broadcast from 1959 to 1964 and from 1970 to 1973. Let us make the situation a bit more complex. We have three numbers—zp0, zp1, zp2—that are zone pointers. They take the value 0 or 1, depending on whether they point to the “real” zone or the “twilight” zone. The instructions will use one, two, or even three points: we say

E.2. Instructions
that the first point used is in zone zp0 and that the first and second, if they occur, are in zones
zp1 and zp2. For example, if we want the next instruction to take its third point from zone 1,
we merely change the value of zp2 to 1 just before executing the instruction. The principle
is the same for reference points: in a high-level language, we would have said that the “zone
number of the third point” is one of the function’s parameters, given each time it is needed;
here, we agree by convention that the instruction always takes its third point from zone zp2,
and before executing the instruction we set zp2 to the correct value.
E.2
Instructions
The language for TrueType instructions is an assembly language; that is, a language very close
to the processor (in this case, the processor for TrueType fonts). In this language, concepts
such as strings do not exist: everything is done with numbers.
E.2.1
Instructions for Managing the Stack and Storage Area
The following instructions allow for managing the interpreter’s stack:
• NPUSH[], PUSHB[], NPUSHW[] et PUSHW[] take several entries from the instruction stream
and place them onto the interpreter’s stack.
• DUP[] copies the element on the top of the stack.
• POP[] deletes it.
• CLEAR[] deletes the entire stack.
• SWAP[] exchanges the first two elements on the stack.
• DEPTH[] returns the depth of the stack.
• Both CINDEX[] and MINDEX[] retrieve a number n from the top of the stack and then copy
(CINDEX[]) or move (MINDEX[]) the nth element on the stack to the top position.
• Finally, ROLL[] performs a cyclic permutation of the top three elements on the stack.
We have access to a number of places in the “storage area” (their exact number is given in the
font’s maxp table—more specifically, in the maxStorage entry of that table). The instruction
RS[] retrieves the position number from the stack and returns the value stored at that position. The instruction WS[] retrieves a value and a position number: it places the value at the
stated position. The storage area is temporary, and it lasts only as long as the glyph is being
processed.
We have another way to store data: the CVT. The CVT contains all the relevant metric information for the font (height of the capitals and of the lowercase letters, thicknesses of characteristic strokes, etc.); but these data bear neither names nor comments. The author of the
instructions must therefore know what corresponds to each entry in the CVT. The CVT is
initialized by the processor when the font is loaded into memory, using the font’s cvt table.

```text
There is a basic difference between the CVT and the storage area: the storage area can hold
any numeric values, whereas the CVT holds only measurements (heights, thicknesses, etc.).
But there are two ways to view measurements: abstractly, through the use of abstract units
based on the font’s grid, and concretely, using pixels, according to the font’s actual size and
the resolution of the display device. The CVT always gives us values in pixels. For instance, the
instruction RCVT[] takes a CVT entry number from the stack and returns the value of the
corresponding entry, in pixels.
We can also write in the CVT. There are two instructions for doing so, according to the nature of the data that we wish to record: if the data is in abstract units, we use the instruction
WCVTF[]; if it is in pixels, we use WCVTP[]. Both instructions take a value and a CVT entry
number offthe stack and write the value of the CVT entry in question.
E.2.2
Managing Vectors, Zones, and Reference Points
In this section, we shall concern ourselves with another category of instructions: those for
setting up our working tools, i.e., the freedom vectors and projection vectors, the “real” and
“twilight” zones, and the three reference points.
Let us begin with the two vectors. There are four ways to define them:
1. Using the stack: SFVFS[] and SPVFS[] retrieve two values, y and x, from the stack. These
are the normalized coordinates of the freedom vector and the projection vector, respectively. Warning! These numbers are expressed in “F2.14”, which means 2 bits for the integer part and 14 bits for the decimal part; the coordinates must be normalized, which is to
say that

x2 +y2 = 0x4000, where 0x4000 is nothing but the number 1 written in “F2.14”.
2. Using two points on the plane. To do so, we use the instructions SFVTL[0] and SPVTL[0],
which take two point numbers, a1 and a2, from the stack. The direction of the freedom
vector or the projection vector, respectively, will be that of the vector connecting the
points pa1 and pa2.
There are variants of these instructions: SFVTL[1] and SPVTL[1] define a perpendicular
freedom vector or projection vector connecting the points pa1 and pa2. It is as if the vector
produced by SFVTL[0] or SPVTL[0] were rotated 90 degrees, in the trigonometric sense
(counterclockwise).
3. Parallel to one axis of the system of coordinates: SFVTCA[0] and SPVTCA[0] make the
freedom and projection vectors, respectively, point upwards (the y-axis); with SFVTCA[1]
and SPVTCA[1], they point to the right (the x-axis).
4. With respect to each other: when the instruction SFVTPV[] is used, the freedom vector
will take the direction of the projection vector. The inverse operation (which corresponds
to the hypothetical instruction SPBTFV[]) does not exist.
The coordinates of the freedom and projection vectors are retrieved by means of the instructions GFV[] and GPV[]), respectively.
Finally, to change the values of the reference points rp0, rp1, and rp2, we use the instructions
SRP0[], SRP1[], and SRP2[]. These retrieve the number of a point from the stack and make it
```

```text
E.2. Instructions
the new reference point. Likewise, the instructions SZP0[], SZP1[], and SZP2[] retrieve a zone
number (0 for the “real” zone and 1 for the “twilight” zone) from the stack and consequently
change the values of the zone pointers zp0, zp1, and zp2. If you wish to give the same value to
all three pointers at the same time (thus saving a few thousandths of a second in processing
time), the instruction SZPS[] is made for you; it works just like the others.
E.2.3
Moving Points
We have reached the end of the line: moving points, be they points on the contour or control
points. It is by moving points that we manage to adapt a contour to the grid of pixels.
Let us begin with the simple cases. We obtain the “coordinate” of a point by using the instruction GC[0], which retrieves the number of a point from the stack. The reader must be
wondering which coordinate is meant by “the coordinate”. After all, we are on a plane, and
the points are defined by pairs of coordinates. Heavens, have we forgotten the projection vector?
GC[0] gives us the value of the projection of the point in question onto the projection vector.
In other words, if the projection vector is horizontal, that will be the abscissa; if it is vertical,
we will obtain the ordinate; and so on.
Now suppose that several points have already been moved. The processor still keeps in memory the coordinates of the original points. We can obtain them through the use of a variant
of GC[0], called GC[1].
How, then, do we move a point? A simple way is to use the instruction SCFS[]. It takes a
distance d and the number of a point from the stack and moves the point in question by
that distance. Once again, the reader who has not yet fully understood the logic of the TrueType instructions may be wondering: “moving a point—fine, but in which direction?” In the
direction of the freedom vector, of course! That, incidentally, is why it is called the “freedom
vector”: because that is the only direction in which we are free to move the point. Can we then
say that we move by d in the direction of the freedom vector? Not really, because if we say
that, we forget about the other vector—the projection vector. What actually happens is that
we move as much as is necessary (in the direction of the freedom vector) so that the projection
of the move onto the projection vector will be equal to d.
The instruction MD[0] allows us to measure the “distance” between two points. It takes the
numbers of two points from the stack and returns the distance between the points (along the
projection vector) in pixels. The variant MD[1] of this instruction yields the distance between
the original positions of the points—those given in the glyf table before the TrueType instructions were applied.
Mimicry is not always a praiseworthy attitude in life. But when we move points, it very often
happens that we wish to move several of the points on the contour in the same way as the
other points. For example, if we decide to move the lower left point of the downstroke of a
letter ‘I’, we should move the upper right point similarly, or the left side of the downstroke
will no longer be parallel with the right side.
There are three instructions—SHP[0], SHC[0], SHZ[0]—that move, respectively, a single
point, all the points of a contour, and all the points in a zone by the same amount as reference
point rp2 was previously moved. These three instructions take the number of a point, a
contour, or a zone, respectively, offthe stack. The contour numbers are simply obtained
from the order in which the contours are defined in the glyf table (counting from 0). The
```

```text
variants SHP[1], SHC[1], and SHZ[1] of these three instructions uses reference point rp1
instead of rp2.
Now, let us move on to the most complex and most useful instructions: MDAP[], MDRP[],
MIAP[], and MIRP[]. These instructions move a point. In the case of the instructions whose
names begin with “MD” (‘D’ for “direct”), the number of a point to be moved is retrieved from
the stack. In the case of the instructions whose names begin with “MI” (‘I’ for “indirect”), the
motion will be made with respect to a value in the CVT; thus first a CVT entry number is
retrieved, and then the number of a point to be moved. Thus we have “direct” and “indirect”
moves.
But there are also “absolute” moves (MDAP[], MIAP[]) and “relative” moves (MDRP[] and
MIRP[]). In the former, we set the point at absolute coordinates, which are retrieved from
either the stack or the CVT; in the latter, the move will be relative to reference point rp0.
The instructions above are never used in isolation but are always accompanied by a set of
flags: MIRP[10110], MDAP[1], etc. The meanings of these flags always depend on the instruction.
Let us examine all that more closely. The instruction MIRP[] (“indirect relative move”) takes
an entry number from the CVT and the number of a point from the stack. Suppose that the
value of the entry in the CVT is d and that the point to be moved is p. The instruction will
move p so that it stands at the distance d from reference point rp0. So far there has been nothing especially complicated: we take a piece of relevant metric data (for example, the thickness
of a stroke) from the CVT, we designate as reference point rp0 a point of interest to us, and
we move a second point so that its distance from the reference point is precisely the relevant
metric datum that we retrieved.
Complications arise when we begin to enable the flags. When bit 2 is enabled,1 the processor
will apply the cut-in. That means that it will measure the distance between rp0 and p, and
then compare it with d; if the difference between the two is below a certain value, it will
move the point so that the distance between rp0 and p will be exactly d; otherwise, it will
not move the point. This value is called the cut-in value; by default, it is equal to 17
16 of a pixel,
but its value can be changed at any time through the instruction SCVTCI[]. Next—and this is
very important—the processor will round the position of p according to the current rounding
method.
Let us review. If flag 2 is enabled, we are asking the processor to make a certain distance equal
to a “relevant” value—a value general and important enough to be stored in the CVT. If our
original distance is close enough to the relevant value, the processor will do so; otherwise it
will completely ignore our request. But in any case, whether or not the distance has changed,
it will round the point that we are moving. By rounding the pixel value of a point, we set the
point on the edge of a pixel, irrespective of the location of the contour relative to the grid of pixels.
In other words, the behavior of pixels that we obtain is independent of the vagaries of placing
a glyph on the screen or on a printed page, and that is indeed the goal of the hinting process.
1 TTX labels the flags from left to right; thus “bit 2”, which in the usual binary notation (10110) is the
third digit from the right, is in our case the third digit from the left. TTX made that decision; we cannot do
anything about it.
```

```text
E.2. Instructions
If flag 1 is enabled, the principle of minimum distance applies. This principle states that the
points in question (here, p and rp0) must be distinct; in other words, the distance between
them must be at least one pixel.
Finally, if flag 0 is enabled, then after the move, point p becomes the new reference point rp0
and can therefore be reused in other operations of this kind. Thus we have series of MIRP[]
instructions in which the point p of one instruction becomes the rp0 of the following one—
which is not surprising, as that means that the points are corrected in order, that the correction of one point depends on that of the previous point, and so on.
The instruction MIAP[] (“indirect absolute move”) is similar to MIRP[], but in this case we do
not use rp0. We retrieve a piece of relevant data from the CVT table and place the point p at
the corresponding coordinate. There is only one flag: MIAP[1] applies the cut-in and rounds
the result; MIAP[0] does nothing.
The instruction MDRP[] (“direct relative move”) is an instruction for “re-establishing correct
distances”. Specifically, a point p is moved so that its distance from the point rp0 is the initial
distance (before any moves) between p and rp0. The method of cut-ins applies. In addition,
if flag 2 of this instruction’s parameter is enabled, the position of p is rounded. Flag 1 will
enable the constraint of the maximum distance.
We see that the difference between “direct” and “indirect” moves lies in the fact that the first
is a move according to a given value (which is retrieved from the CVT or the stack), whereas
the second is merely a synchronization of moves: if rp0 has moved from its initial position,
then p will move in the same manner. In both cases, we go through a step involving a cut-in
and rounding. The cut-in ensures that the equalization is intended and does not represent the
loss of one of the letter’s relevant characteristics: if the difference between the values before
and after correction is less than the cut-in, there has been an error due to the pixel grid, and
the correction is carried out; if the difference exceeds the cut-in, that difference is necessitated
by the letter’s shape and should be preserved (if it survives the subsequent step of rounding).
Only one instruction remains to be described: MDAP[]. It is a fine philosophical puzzle: if ‘D’
means that the amount of the move comes from the difference between the original contour
and the modified contour, and if ‘A’ means that it is not a distance between two points on the
contour but the coordinates of a single point, what can MDAP[] mean? Well, it is very simple:
it does nothing at all. Even though there is an ‘M’ (for “move”) in its name, MDAP[] does not
move anything. If its only flag is enabled, this instruction will merely round point p.
Note that after the instructions MIRP[] and MDRP[], the point rp1 will take the value of the
previous rp0 and the point p will become the new rp2. If their flag 0 is enabled, then p will also
become the new rp0. In addition, following the instructions MIAP[] and MDAP[], the point p
becomes the new rp0 and the new rp1. This is the “ballet” of reference points to which we
alluded above.
We have two other ways to move points: alignment and interpolation.
Alignment involves making the distance between two points zero. Taken outside the context of the
TrueType instructions, this phrase would have no meaning: everyone knows that two points
located at a distance of zero are much more than merely aligned—they are identical! Alas,
do not forget that we are in a context quite different from the Euclidean geometry that we
learned at school. Remember that all distances are measured along the axis of projection; thus
```

```text
there may well be points whose distance from each other is zero but that are not identical:
they need only lie on the same line perpendicular to the axis of projection. And “being on
the same line” is synonymous with “being aligned”.
The instruction ALIGNPTS[] does just that: it takes the numbers of two points from the stack
and moves the corresponding points in such a way that their projections onto the projection
vector are identical. Therefore they are aligned relative to a line perpendicular to the projection vector.
ALIGNRP[] goes a bit further: it aligns not only a pair of points but any number of points.
Specifically, there is a variable for the graphics state, named loop. Its default value is 1, but it
can be changed through the instruction SLOOP[]. What does it have to do with ALIGNRP[]?
Well, the latter takes loop elements from the stack—the numbers of loop points to be aligned
with rp0. Thus we can align a heap of points with a single instruction. After this instruction
has been executed, the variable loop is reset to its default value, namely 1.
The instruction ISECT[] moves a point p so that it falls at the intersection of two straight
lines. It retrieves from the stack the four points that make up the two line segments, and then
the point p. If the segments are parallel, the point p is placed at the center of mass of the
parallelogram thus formed.
There is also an instruction for interpolation: IP[]. It takes a point p offthe stack and moves
it so that the ratio of its distances to reference points rp1 and rp2 is the same as in the original
contour. In other words, if d(pa, pb) is the distance between pa and pb, and if the prime mark
denotes the initial positions, we are asking that d(p,rp1)
d(p,rp2) = d(p′,rp′
1)
d(p′,rp′
2).
This instruction is very powerful because it allows us to recover the ratios between the initial
distances (i.e., those before the instructions were executed) in a very simple way. For example,
suppose that a point lies halfway between the edges of a letter’s downstroke. We have just
moved those edges, and we want the point in question to be moved so that it still lies halfway
between them. If we take a projection vector perpendicular to the edges, then every point on
one of the edges is projected onto the same point on the projection vector. Thus it suffices
to take a point on each edge, make reference points rp1 and rp2, and then apply IP[] to the
point in question. As if by magic, it will again appear in the middle of the downstroke.
And, speaking of magic, we have now come to the magical instructions IUP[0] and IUP[1].
They interpolate all the untouched points: IUP[0] performs horizontal interpolation and
IUP[1] performs vertical interpolation. An untouched point is a point to which no instruction
for movement has been applied. The usual approach is to proceed in three steps: first we move
certain important points individually, and very carefully; then we use IP[] to interpolate
some other, less important, points; at the end, we correct all the other points en masse with a
single stroke of our magic wand, through the use of the IUP[] instructions.
What, then, shall we do if we also wish to interpolate a point that is unlucky enough to have
been touched? For that purpose, there is the instruction UTP[], which will “untouch” a point.
Thus the IUP[] instructions allow us to rectify all the points in between the relevant points
that we have so abundantly moved; they are among the most frequently used instructions,
and the most spectacular.
```

```text
E.2. Instructions
E.2.4
δ Instructions
The pretty name of δ instruction comes from the fact that the letter ‘δ’ is often used for infinitesimal increments. We can consider δ-instructions as exceptions to the rule—the rule being
all the moves performed by the instructions that we have seen up to this point. The reader
may reply that the instructions in question are already exceptions to the rule, which is the
glyph’s regular contour. By modifying the contour to adapt it to the pixel grid, we have already created an “exception”: an exceptional contour tailored to the present situation. True,
but that contour, as exceptional as it may be, is nonetheless based on instructions independent
of the sizes of the glyphs. The same instructions will be applied (with more or less success)
whether the glyph is rendered at 5, 10, 15, or 50 pixels, whether on screen or on paper. We can
only hope that the validity of the instructions for movement will ensure an ideal rendering
at all sizes.
Unfortunately, that is not always the case. Sometimes we must make slight corrections that
apply only to a specific size: those are δ instructions. There are two kinds of δ instructions:
“DELTAP”, which apply to points on the contour, and “DELTAC”, which apply to entries in
the CVT.
We use two variables for a graphics state (delta_base and delta_shift) to specify, with as much
precision as possible, how large the correction should be and at which sizes it should be applied. Thus there are two quantitative data to supply to a δ instruction: the magnitude of the
correction and the size at which it is applied.
The life of the TrueType instructor would be much easier if the δ instructions could simply retrieve these two pieces of data from the stack. Unfortunately, in order to make our code more
compact, we are required to compress these two pieces of data into a single 8-bit number. This
poor number must indicate both the exact size at which the correction is to be applied and the
magnitude of the correction itself. The font’s size (in pixels per em) may vary between, say,
5 and 250; the correction may be on the order of one-sixteenth of a pixel, or half a pixel. How
can we pack all this information into a tiny byte, which will never have more than 8 bits?
We shall divide this famous byte right down the middle, into two nibbles. The first nibble is devoted to the font size to which the correction will be applied. A nibble contains
4 bits, and that corresponds to 16 numeric values; thus we have an interval of 16 consecutive
sizes at our disposal. That is not very many. Through the use of three different instructions
(DELTAP1[], DELTAP2[], DELTAP3[], and likewise for DELTAC1[], etc.), we can have three intervals of 16 sizes, which is to say one large interval of 48 consecutive sizes, which is more
reasonable. Next, everything depends on the size at which we start counting: if we start counting from 5 pixels, we can cover all sizes between 5 and 52 pixels per em; if we start at 9,
we will have the interval between 9 and 56 pixels per em; and so on. The minimum size is
stored in the graphics state variable delta_base, whose value can be changed at any time with
the instruction SDB[]. For instance, if we specify that delta_base has the value 5, DELTAP1[]
will cover the sizes between 5 and 20, DELTAP2[] will cover those between 21 and 36, and
DELTAP3[] will cover those between 37 and 52 pixels per em. That is our makeshift solution
for font sizes. Conversely, if we know that we want size α, we first figure out in which interval
it lies, according to the value of delta_base, and then we subtract from α the smallest value in
that interval. Since each interval is of size 16, the difference will necessarily be less than 16;
therefore, it can be encoded in one nibble.
```

Let us now move on to the magnitude of the correction. Here we have not whole values but
fractions of a pixel. To get the greatest use out of the four little bits that we have on hand,
we shall use another graphics state variable, called delta_shift. It indicates the precision in the
form of a power of two. If delta_shift has the value 4, we will have a precision of 1
24 , i.e., onesixteenth of a pixel. Accordingly, we distribute the possible values of our 4 bits according to
the following table, which gives us the value of the numerator:
Value of the nibble
8 9 10 11 12 13 14 15
Numerator
−8 −7 −6 −5 −4 −3 −2 −1 1 2 3
where the denominator is 2 to the power delta_shift. We change the value of delta_shift with
the instruction SDS[].
A practical example: we wish to move point 13 to the left by seven thirty-seconds of a pixel
at the size of 17 pixels per em. Suppose that, for whatever reason, delta_base is equal to 5.
Since 17−5 = 12, we are in the scope of DELTAP1[], and the first nibble of our byte will have
the value 12 (in binary, 1100). As for the magnitude, in order to work with thirty-seconds of a
pixel, we must have delta_shift equal to 5. Since −8 thirty-seconds corresponds to 0000 and +8
corresponds to 1111, it follows that 7 corresponds to 1110. Taken together, these two nibbles
form the byte 11001110, which is the number 206. There, then, is the argument to DELTAP1[].
And the requirement that the correction be made to the left can be handled very quickly: we
merely set the freedom vector to point in that direction.
The example above works because we requested a correction of less than 8 times delta_shift. If
we had wanted a correction of 31 thirty-seconds, for example, it would not have been possible.
We would have had to approximate that fraction by a fraction whose numerator is less than 8:
the best that TrueType could do for us would be 7
8, with a delta_shift of 3. Thus the greater
the correction, the lower its precision; that is what always happens when we are required to
compress information into a fixed number of bits.
E.2.5
Tests and Logical and Arithmetic Functions
There is an “if/else/end” test structure, which works as follows: The IF[] instruction retrieves
an entry from the stack. If the entry is nonzero, the test has the value true, and the following
instructions will be executed. If the entry is zero, the interpreter proceeds to the next ELSE[]
or EIF[] (= “end of test”). It then executes the instructions that follow.
To prevent some instructions from being executed, we can skip them with the instruction
JMPR[] (from “jump relative”), which takes a number n from the stack and moves forward
as many instructions in the instruction stream. We can also combine a test and a jump,
with JROT[] (“jump relative if true”) and JROF[] (“jump relative if false”), which take two
numbers, b and n, from the stack and move forward n instructions if b is nonzero or zero,
respectively.
There is a heap of logical and arithmetic functions. To describe them, let us suppose that the
top two elements on the stack are a1 and a2:
• LT[] (“strictly less than”) places 0 on the stack if a1 < a2 and 1 otherwise.

E.2. Instructions
• LTEQ[] (“less than or equal”) places 0 on the stack if a1 ≤a2 and 1 otherwise.
• GT[] and GTEQ[] are the “greater-than” counterparts of LT[] and LTEQ[].
• EQ[] and NEQ[] test for equality and inequality, respectively.
• EVEN[] and ODD[] test for evenness and oddness, respectively.
• AND[] and OR[] are the logical operations and and or.
• NOT[] is logical negation.
• ADD[], SUB[], MUL[], and DIV[] are the four arithmetic operations a1+a2, a1−a2, a1a2, a1
a2 .
The calculations are performed on numbers in “F26.6” format, i.e., 26 bits for the integer
part and 6 bits for the decimal part.
• ABS[] is absolute value, and NEG[] changes the sign.
• FLOOR[] and CEILING[] round up and down, respectively.
• MAX[] and MIN[] return the larger and the smaller, respectively, of a1 and a2.
E.2.6
Definitions of Subroutines and New Instructions
In the tables cvt and fpgm of a TrueType font, we can define subroutines of instructions (which
can subsequentely be called by the code of any glyph) and even new instructions.
To define a block of code as a subroutine, we surround it with the instructions FDEF[] (“subroutine definition”) and ENDF[] (“end of subroutine definition”). FDEF[] will take a number
offthe stack, which will be the number of the subroutine. To call the subroutine, we place
that same number onto the stack and execute the instruction CALL[]. We can also use the
instruction LOOPCALL[] (“iterative call to a subroutine”), which takes two numbers offthe
stack: the first is the subroutine’s number, and the second is the number of times that we
wish to execute the subroutine.
Each TrueType instruction is represented by a 1-byte number. To define a new instruction
that will represent a certain block of code, we must find a number that does not correspond to
any instruction. Then we place that number on the stack and surround the new instruction’s
block of code by the instructions IDEF[] (“instruction definition”) and ENDF[].
The instruction IDEF[] was introduced to ensure upward compatibility for the anticipated
addition of new instructions. Suppose that Microsoft and Apple decided to introduce a new
instruction COFFEE[] that would turn a coffee maker on every time we wrote a certain glyph
that represented a coffee bean. What would current processors do when they encountered this
instruction? To keep them from crashing, we can give this instruction a phony definition by
using IDEF: a processor that knows the real COFFEE[] instruction would skip the redefinition;
other processors would apply the phony definition, and the problem would be solved.
But that has in fact never happened: in the 15 years that TrueType has existed, never once has
a new instruction been introduced!

```text
31 32
Figure E-1: The ‘T’ of the TrueType font Courier, by Apple/Bistream. The control points are not indicated.
E.3
Some Examples
Here are a few examples that will, the author hopes, show concretely how the instructions
described in the previous section are used.
E.3.1
The ‘T’ in the Font Courier
Here we have the font Courier v. 4.0d2, which belongs to Apple and Bitstream and is part of
the Mac OS X operating system. More precisely, it is the font “Courier with rounded caps”, not
to be confused with Adobe’s Courier font, which is much lighter and has square terminals.
This letter has many points (52!) but few instructions, and those instructions are easy to understand. There are no δ instructions. Below we show the actual code, with no simplification
or other changes.
In Figure E-1, the reader can see the letter whose instructions we shall examine. We have
indicated the positions of the points that lie on the contour and those of the auxiliary points:
the origin (50) and the ending point of the displacement vector (51).
Here are the letter’s instructions, as represented by TTX. We have added in comments (C-style,
not XML-style, as we are using assembly-language syntax) the numbers that the instructions
retrieve from the stack and the values of the reference points rp0, rp1, and rp2 that the instructions leave after their execution. This data turns out to be indispensable for understanding how
the instructions work. Here is the complete code; below we shall examine it line by line:
```

```text
E.3. Some Examples
&lt;instructions&gt;&lt;assembly&gt;
NPUSHB[ ]
28 27 0 49 10 17 13 27 21 18 9 6 0 6 28 24 3
48 28 185 13 228 45 30 196 38 39 45 47 42 32
38 29 35 14 18 17 3 27 21 13 10 9 3 6 0 27 49
21 72 35 71 29 0 49 6 72 29 15 42 71 47 50
SRP0[ ]
/* 50.
rp0=50 */
MDRP[10100]
/* 47.
rp0=47, rp1=50, rp2=47 */
MIRP[00100]
/* 71, 42.
rp2=42 */
MIRP[01100]
/* 15, 29.
rp2=29 */
MIRP[10100]
/* 82, 6.
rp0=6, rp2=6 */
MIRP[01100]
/* 49, 0.
rp1=6, rp2=0 */
SRP0[ ]
/* 29.
rp0=29 */
MIRP[00100]
/* 71, 35.
rp1=29, rp2=35 */
MIRP[10100]
/* 72, 21.
rp0=21, rp2=21 */
MIRP[01110]
/* 49, 27.
rp1=21, rp2=27 */
SRP1[ ]
/* 0.
rp1=0 */
SRP2[ ]
/* 6.
rp2=6 */
SLOOP[ ]
/* 3 */
IP[ ]
/* 13, 10, 9 */
SRP1[ ]
/* 21.
rp1=21 */
SRP2[ ]
/* 27.
rp2=27 */
SLOOP[ ]
/* 3 */
IP[ ]
/* 17, 18, 14 */
SRP1[ ]
/* 35.
rp1=35 */
SRP2[ ]
/* 29.
rp2=29 */
IP[ ]
/* 38 */
IP[ ]
/* 32 */
SRP1[ ]
/* 42.
rp1=42 */
SRP2[ ]
/* 47.
rp2=47 */
IP[ ]
/* 45 */
IP[ ]
/* 39 */
IUP[1]
SVTCA[0]
MDAP[1]
/* 38.
rp0=38, rp1=38 */
MIRP[01110]
/* 196, 30. rp1=38, rp2=30 */
SHP[0]
/* 45 */
MIRP[11110]
/* 228, 13. rp0=13, rp2=13 */
MIRP[01110]
/* 185, 28. rp1=13, rp2=28 */
SHP[0]
/* 48 */
MDRP[00110]
/* 3.
rp2=3 */
SHP[0]
/* 24 */
SRP1[ ]
/* 28.
rp1=28 */
SLOOP[ ]
/* 6 */
IP[ ]
/* 0, 6, 9, 18, 21, 27 */
SRP2[ ]
/* 13.
rp2=13 */
```

```text
IP[ ]
/* 17 */
IP[ ]
/* 10 */
IUP[0]
&lt;/assembly&gt;&lt;/instructions&gt;
How many numbers can a human (the reader, the author, anyone else) retain in memory?
Two dozen? At the beginning of the code, we ask the processor to retain 63 numbers in memory (!), through the use of the instruction NPUSHB[]:
NPUSHB[ ]
28 27 0 49 10 17 13 27 21 18 9 6 0 6 28 24 3
48 28 185 13 228 45 30 196 38 39 45 47 42 32
38 29 35 14 18 17 3 27 21 13 10 9 3 6 0 27 49
21 72 35 71 29 0 49 6 72 29 15 42 71 47 50
This clearly shows that the code was not written to be read by a human. Never mind: writing
the numbers retrieved by each instruction at the side makes the code perfectly legible, however many instructions were placed on the stack at the start of the program.
The code that follows can be divided into two parts: the first concerns horizontal modifications to the contour; it ends with the instruction IUP[1], which is a global interpolation in the
horizontal direction. The second part deals with vertical modifications and ends with IUP[0].
Let us begin at the beginning. After NPUSHB[] and the 63 numbers placed on the interpreter’s
stack, the code continues with an SRP0[]:
SRP0[ ]
/* 50.
rp0=50 */
which takes the number 50 offthe stack. This instruction sets auxiliary point 50 (the glyph’s
origin) as reference point rp0.
Next come the instructions to move the point. The first instruction is an MDRP[]:
MDRP[10100]
/* 47.
rp0=47, rp1=50, rp2=47 */
i.e., a direct move. It applies to point 47, which appears on the left edge of the main downstroke. Recall that the purpose of this instruction is to restore the original distance between
reference point rp0 (currently 50) and the point in question, and then to round the point.
Here there is nothing to restore (since neither 50 nor 47 has been modified); thus we merely
round the position of point 47 and set it at the edge of a pixel. When we have also applied
this correction to point 48, which also lies on the left edge of the downstroke, this stroke
will have the same thickness as all the other downstrokes of letters in the font. Note that
after this instruction, point 50 becomes rp1 and point 47 becomes rp2. Since its first bit is
enabled, point 47 becomes the new rp0, and therefore we shall use that point as we continue
to “correct” other points.
Next, we address the lower left serif. We have an MIRP[] instruction:
MIRP[00100]
/* 71, 42.
rp2=42 */
```

```text
E.3. Some Examples
which takes the numbers 71 and 42 offthe stack; it will therefore use CVT number 71 (whose
value is 266, as seen in the cvt table) and point 42. What about MIRP[], which is an instruction
for indirect movement? It will cause the distance between point 42 (which in our case is the
end of the serif) and reference point rp0 (point 47: the left edge of the main downstroke) to
be equal to entry 71 in the CV.
We have just solved one of the font’s mysteries: the role of entry 71 in its CVT! This entry,
whose value is 266, is the width of a horizontal serif. There is a very good chance that the
letters ‘Y’ and ‘I’ use the same CVT entry. The reader must now be feeling the same shivers
that Einstein felt when he discovered the laws of general relativity—perhaps on a smaller
scale, but, after all, everything is relative.
As it exits the stage, this instruction leaves us in the following situation: point 47 has become rp1 and point 42 has become rp2. Since flag 0 of the latter instruction is disabled, the
point rp0 has not changed, and therefore is still 47—i.e., the left edge of the main downstroke.
The MIRP[] instruction that comes next:
MIRP[01100]
/* 15, 29.
rp2=29 */
takes CVT entry number 15 and point 29 offthe stack. Point 29 is on the right edge of the
downstroke! Conclusion: though you would never have guessed, CVT entry 15 (whose value
is 156) contains the font’s stroke thickness. It is not surprising that that value is one of the first
in the CVT (which has 328 values in all): for an “Egyptian” font—one whose stroke width is
constant—it is of capital importance!
The last MIRP[] had bit 0 disabled; therefore, the point rp0 still has not changed. What else
can we correct with our celebrated point 47? We have already corrected the length of the serif
and the thickness of the downstroke. What remains? Well, the horizontal bar of the letter ‘T’!
It is still an important property because without a horizontal bar there can be no letter ‘T’;
even Ernestine (the author’s elder daughter) knew that already at the age of five. Next comes
an MIRP[] instruction:
MIRP[10100]
/* 82, 6.
rp0=6, rp2=6 */
which will use CVT entry 82 and point 6: the left edge of the letter. Well, 82 is not far from 71,
but it is quite far from 15; thus we might reasonably assume that these CVT entries are specific to the letter ‘T’. They are for correcting the distance the left edge of the downstroke and
the letter’s left side. Surprise: this MIRP[] instruction has its bit 0 enabled! Point 6 therefore
becomes the new reference point rp0.
Why? Because the left side of the letter is also the left edge of the left vertical serif. And now
we must make sure that the thickness of this serif is correct. We shall try to correct the position
of point 0 by using point 6: indeed, the following MIRP[] instruction:
MIRP[01100]
/* 49, 0.
rp1=6, rp2=0 */
makes use of point 0 and a CVT entry—this time, entry 49 (whose value is 141).
The astute reader must be wondering why we should use a CVT entry other than 15. Have we
not said that 15 contains the stroke’s thickness? Answer: yes, 15 contains the stroke’s thickness,
```

```text
but who said that the stroke thickness of an “Egyptian” font is always exactly the same? And
what about artistic license? Here, then, is the inside scoop on the font in question: just as
Marilyn was not a true blonde, this font is not a true “Egyptian”!
After this instruction, an SRPO[]:
SRP0[ ]
/* 29.
rp0=29 */
forces us to change our reference point: our new rp0 is the point 29—i.e., the right edge of the
main downstroke. Up to now we have been handling the left side, but now we are moving
over to the right. Fortunately, everything is symmetric. The three instructions that follow:
MIRP[00100]
/* 71, 35.
rp1=29, rp2=35 */
MIRP[10100]
/* 72, 21.
rp0=21, rp2=21 */
MIRP[01110]
/* 49, 27.
rp1=21, rp2=27 */
are MIRP[] instructions applied to the points 35 (the right edge of the serif, with CVT entry 71,
as we just saw), 21 (the right side of the letter, CVT entry 72), and 27 (the left edge of the right
serif, CVT entry 49 for the distance between 21 and 27). Since points 35, 21, and 27 are the
symmetric counterparts of points 42, 6, and 0, there is nothing surprising: we use the same
CVT entries as before.
We have finished our “relevant” corrections; now we need to modify all the other points to
match. What does that mean, exactly? Well, the entire upper left part of the letter must be
modified according to the corrections made to 0 and 6. The entire upper right part must be
modified according to the changes made to 21 and 27. What are the points on the upper left
part? There are, for example, 9, 10, and 13. We shall use the instruction IP[], applied to these
three points, to perform interpolation:
SRP1[ ]
/* 0.
rp1=0 */
SRP2[ ]
/* 6.
rp2=6 */
SLOOP[ ]
/* 3 */
IP[ ]
/* 13, 10, 9 */
The first two (SRP1[] and SRP2[]) change points 0 and 6 to rp1 and rp2. Next, SLOOP[] takes
the number 3 offthe stack and assigns that value to the variable loop. That variable is used
by IP[], which takes three points offthe stack: the points 13, 10, and 9. The effect of an IP[]
instruction is to correct the positions of the points that we supply to it, with respect to two
reference points rp1 and rp2: thus we have just corrected points 13, 10, and 9. The four lines
of code that follow:
SRP1[ ]
/* 21.
rp1=21 */
SRP2[ ]
/* 27.
rp2=27 */
SLOOP[ ]
/* 3 */
IP[ ]
/* 17, 18, 14 */
do the same for the points 17, 18, and 14 (rp1 being 21 and rp2 being 27).
Next, we deal with the serif:
```

```text
E.3. Some Examples
SRP1[ ]
/* 35.
rp1=35 */
SRP2[ ]
/* 29.
rp2=29 */
IP[ ]
/* 38 */
IP[ ]
/* 32 */
Points 35 and 29 become, respectively, rp1 and rp2. We first interpolate point 38 (through the
first instruction IP[], which interpolates only a single point, since loop has become equal to 1
again) and then point 32 (through the second IP[] instruction).
The reader must be wondering why we use repeated IP[] instructions rather than a single
instruction that interpolates loop points all at once. The answer is simple: we wish to interpolate two points, and therefore we must place 2 onto the stack, perform an SLOOP[], and
then perform an IP[]—that makes three operations, whereas performing an IP[] and then
another IP[] makes only two operations. Thus we have saved a whole microsecond of processing time!
We have just processed the right side of the horizontal serif; now let us do the same for the
left side:
SRP1[ ]
/* 42.
rp1=42 */
SRP2[ ]
/* 47.
rp2=47 */
IP[ ]
/* 45 */
IP[ ]
/* 39 */
Points 42 and 47 become rp1 and rp2, and then we interpolate points 45 and 39.
There are a few other points that have not been corrected: in particular, all the control points,
which have not even been indicated in Figure E-1. We shall correct all these points with the
magical instruction IUP[1]:
IUP[1]
which performs horizontal interpolation for everyone, or at least for the points that have
been “touched”. And that concludes the horizontal corrections to this letter.
The next instruction:
SVTCA[0]
makes the two vectors vertical. Henceforth we shall think “vertically”.
The vertical corrections follow the same schema: an MDAP[]:
MDAP[1]
/* 38.
rp0=38, rp1=38 */
makes absolute corrections to the position of point 38, which is the bottom of the letter. Next:
MIRP[01110]
/* 196, 30. rp1=38, rp2=30 */
```

```text
point 30 is corrected relative to 30, through the use of CVT entry 196 (whose value is 141,
which is indeed the same as 49, the thickness of the vertical serif). Thus we have corrected
the lower serif. Next, with 30 as our reference point rp2, we execute an SHP[0] instruction:
SHP[0]
/* 45 */
applied to point 45. That means that we move the point in question as much as reference
point rp2 was moved.
That move was necessary because when we corrected the distance between points 38 and 30,
we corrected only the right side of the serif. By requiring that 45 do the same as 30, we maintain the thickness of the serif and the vertical downstroke.
Next comes an MIRP[]:
MIRP[11110]
/* 228, 13. rp0=13, rp2=13 */
which uses CVT entry 228 (value: 1,186) and is applied to point 13. This point lies on the
letter’s top edge; the current point rp0 is 38, which is at the bottom of the letter. One would
never have guessed, but CVT entry 228 contains the height of the capital letters, at least those
that have no overshoot. Furthermore, by looking at the bounding boxes of the capital letters,
we can see that most of them are of height 1,186. The last MIRP[] therefore corrects the letter’s
height; we can say that it is the equivalent of a blue zone in the hints of PostScript Type 1 fonts.
Since the last MIRP[] has its flag 0 enabled, reference point rp0 changes and becomes point 13.
Next comes another MIRP[]:
MIRP[01110]
/* 185, 28. rp1=13, rp2=28 */
which will correct point 28 (the lower edge of the horizontal bar) relative to the top of the
letter. Then an SHP[0]:
SHP[0]
/* 48 */
will apply the same correction as for the last rp2 (which was 28) to point 48, which is also on
the lower edge of the horizontal bar, but at the other end of the downstroke. Thus we obtain
an optimal horizontal bar.
Now we handle the vertical serifs. The MDRP[] that comes next:
MDRP[00110]
/* 3.
rp2=3 */
requests that the point 3 that appears at the end of the left serif be corrected in the same
way as the current point rp0, which is 13: the upper edge of the horizontal bar. Next follows
an SHP[0]:
SHP[0]
/* 24 */
```

```text
E.3. Some Examples
which applies the same correction to point 24, on the end of the other serif. That concludes
the correction of the serifs.
We have now handled all the “relevant” points as well as we can. Now is the time to perform
interpolation, and we shall do so in a big way: six (!) points will be interpolated at one stroke.
They are the points 0, 6, 9, 18, 21, and 27. These points form the top parts of the serifs. They
shall be interpolated relative to the current points rp1 and rp2, which are 28 (the lower part
of the horizontal bar) and 3 (the end of the vertical serif):
SRP1[ ]
/* 28.
rp1=28 */
SLOOP[ ]
/* 6 */
IP[ ]
/* 0, 6, 9, 18, 21, 27 */
Finally, we also interpolate points 10 and 17 relative to 28 and 13:
SRP2[
/* 13.
rp2=13 */
IP[ ]
/* 17 */
IP[ ]
/* 10 */
i.e., relative to the two edges of the horizontal bar. And we are ready to launch the great
magical instruction IUP[0]:
IUP[0]
which will interpolate everything—at least all the points that have not been “touched”. And
that concludes the program for this glyph’s instructions.
We have seen that the strategy adopted in this example is as logical as it is natural: we correct
the positions of the points by starting with the most important ones; we proceed by basing
the correction of each point on that of another point that has already been corrected; when
we correct the most relevant points, we make some local interpolations to correct other, less
important, points, that appear in the same context; finally, when all of the smart operations
have been completed, we run one great big massive interpolation to correct all of the points
that have not been corrected with ready-made instructions.
E.3.2
The ‘O’ from the Font Verdana
We have examined a letter from a font by Apple/Bitstream; now let us look at a font by
Microsoft: Verdana, a font that is part of Windows XP and that was specifically designed for
display on screen.
The instructions for this letter are few:
&lt;instructions&gt;&lt;assembly&gt;
NPUSHB[ ]
4 0 4 6 11 12 11 18 23 0 23 6 25 12 25
18 87 1 87 5 83 7 95 11 88 13 88 17 95
19 83 23 16 118 9 121 21 2 27 52 21 2
```

```text
33 52 9 10 24 21 3 115 37 15 37 1 15 37
31 37 63 37 3 30 21 15 104 36
SRP0[ ]
/* 36.
rp0=36 */
MIRP[10110]
/* 104, 15.
rp0=15, rp1=36, rp2=15 */
MIRP[01101]
/* 21, 30.
rp1=15, rp2=30 */
DELTAP1[ ]
/* 3, 37, 63, 37, 31, 37, 15 */
DELTAP1[ ]
/* 1, 37, 15 */
SRP0[ ]
/* 37.
rp0=37 */
MIRP[10110]
/* 115, 3.
rp0=3, rp1=37, rp2=3 */
MIRP[01101]
/* 21, 24.
rp1=3, rp2=24 */
SVTCA[0]
MIAP[1]
/* 10, 9.
rp0=9, rp1=9 */
MIRP[01101]
/* 52, 33.
rp1=9, rp2=33 */
MIAP[1]
/* 2, 21
rp0=21, rp1=21 */
MIRP[01101]
/* 52, 27
rp1=21, rp2=27 */
DELTAP1[ ]
/* 2, 21, 121, 9, 118 */
IUP[1]
IUP[0]
SVTCA[1]
DELTAP1[ ]
/* 16, 23, 83, 19, 95, 17, 88, 13, 88,
11, 95, 7, 83, 5, 87, 1, 87, 18, 25,
12, 25, 6, 23, 0, 23, 18, 11, 12, 11,
6, 4, 0, 4 */
&lt;/assembly&gt;&lt;/instructions&gt;
Yet they are quite efficient. As we see above, a few δ instructions appear among them.
Let us begin at the beginning. In Figure E-2, the reader can see the glyph that we shall examine. Let us point out, in passing, the interesting optical illusion that can be seen on the
contour: we have the impression that points 28 and 26 are slightly higher than point 27, yet
they are in fact perfectly aligned! The same is true of the points 32-33-34, and vertically for
29-30-31 and 35-24-25.
First of all, we shall place 66 numbers on the interpreter’s stack:
NPUSHB[ ]
4 0 4 6 11 12 11 18 23 0 23 6 25 12 25
18 87 1 87 5 83 7 95 11 88 13 88 17 95
19 83 23 16 118 9 121 21 2 27 52 21 2
33 52 9 10 24 21 3 115 37 15 37 1 15 37
31 37 63 37 3 30 21 15 104 36
Next, after the instruction:
SRP0[ ]
/* 36.
rp0=36 */
our first reference point, rp0, becomes the point 36. It is the first auxiliary point and therefore
the origin of the glyph. Next comes an MIRP[] instruction:
```

```text
E.3. Some Examples
Figure E-2: The ‘O’ from the TrueType font Verdana, by Microsoft.
MIRP[10110]
/* 104, 15.
rp0=15, rp1=36, rp2=15 */
which for is CVT entry number 104 and point 15. The value of the CVT entry is 115; point 15
is at the left boundary of the glyph. Thus we place that boundary at the edge of a pixel.
Since this instruction’s bit 0 is enabled, reference point rp0 changes and becomes point 15.
Next comes another MIRP[]:
MIRP[01101]
/* 21, 30.
rp1=15, rp2=30 */
This time it is for point 30, which lies exactly opposite point 15, on the other side of the stroke.
The value of the CVT entry in question (entry 21) is 206. Thus it represents the thickness of
the stroke.
After these two MIRP[] instructions, we have corrected the left side of the letter. That does
not leave us with a beautiful letter ‘O’, but it is a good start.
Before continuing, we have two δ instructions for special cases:
DELTAP1[ ]
/* 3, 37, 63, 37, 31, 37, 15 */
DELTAP1[ ]
/* 1, 37, 15 */
The first is a DELTAP1[]; therefore, it pertains to the range of sizes between 9 (the current value
of delta_base) and 25 points.
```

```text
We can see that the three applications of the δ instruction affect the same point: point 37. That
is not just any point: it is the ending point of the displacement vector. Thus we are correcting
its position in three different cases, which correspond to the attribute values 63, 31, and 15.
Let us proceed to “decode” these values. We have not changed the default value of delta_shift;
thus it is still 3. These numbers in binary are 00111111, 00011111, and 00001111. Thus the
lower nibbles are still 1111, or 15, which is the maximum magnitude for this delta_shift: 8
8 of
a pixel. The three upper nibbles are 0011 (3), 0001 (1), and 0000 (0); thus we are applying this
modification to the sizes of 9, 10, and 12 pixels per em.
Apparently this δ correction was not enough for size 9, as we apply a second δ instruction to
the same point, 37, for a new move of 8
8 of a pixel.
The reader must be wondering why we are going to such pains to correct the position of
point 37 when that point is not on the contour and no pixel is found there. Apart from the
fact that the correction allows us to modify the glyph’s width according to its size, the question
is answered in part by the subsequent instructions: specifically, we are now adjusting the right
side of the glyph, and we start by making this famous point 37 our reference point rp0. By
starting on the right to adjust the right side of our glyph, we mirror, in a way, the operations
that we carried out at the beginning of the program to correct the left side of the glyph. The
only difference: for the left side, we left point 36 where it was (the instruction SRP[] does
nothing but a rounding operation), whereas on the right side we are applying several δ instructions to “configure” point 37 according to the type size.
Next, we correct the position of point 3 (the rightmost limit of our contour) relative to
point 37 by performing:
SRP0[ ]
/* 37.
rp0=37 */
MIRP[10110]
/* 115, 3.
rp0=3, rp1=37, rp2=3 */
The CVT entry used is 115 (value 114, thus one unit less than the left side). Once we have
corrected this point, which appears at the right edge of the stroke, we expect to correct the
left edge as well.
And we do indeed. Since reference point rp0 has been set to point 3, which we have just
corrected, we now have an MIRP[]:
MIRP[01101]
/* 21, 24.
rp1=3, rp2=24 */
applied to point 24. This point appears right across from point 3. No surprises with regard
to the CVT entry chosen: it is entry 24, the same one used for the pair of points 15, 30. That
confirms our assumption that entry 24 contains the stroke thickness for this type of letter.
After that instruction, an SVTCA[0]:
SVTCA[0]
switches to the vertical mode. Let us mention that Apple, in the previous example, first interpolated all the untouched points before switching to vertical mode. Microsoft has chosen to
do so afterwards.
The MIAP[] instruction:
```

```text
E.3. Some Examples
MIAP[1]
/* 10, 9.
rp0=9, rp1=9 */
places a point at a coordinate given by the CVT entry. Here it is point 9, which is the lowest
point on the glyph, and the CVT entry in question is 10 (value: −31). The conclusion is easy:
entry 10 of the CVT is nothing but the overhang of this font, or at least the overhang used by
some glyphs in the font (the lowercase letters may have a smaller overhang). Thus we round
this position by possibly applying the cut-in.
The reader must have guessed what comes next: we shall correct the stroke’s thickness by
addressing point 33.
That is indeed right. The MIRP[] instruction that follows:
MIRP[01101]
/* 52, 33.
rp1=9, rp2=33 */
corrects the (vertical) position of this point by using CVT entry number 52. Surprise! this
CVT entry has the value 171, which is noticeably smaller than the one that we used for the
“horizontal” thickness of the stroke. Thus we have just discovered a subtlety of the font: near
the horizontal tangent, the curves are 15 percent thinner than near the vertical tangent.
Next we address the upper part of the letter. In the horizontal case, we first handled the
left side and then corrected auxiliary point 37 to continue from right to left and correct the
right side.
Here the situation is different: the height of our letter is “standard”, since it is simply the height
of the uppercase letters with overshoot. Thus we shall act as if the lower part of the letter did not
exist, and go on to point 21 (the top of the letter) with an MIAP[] instruction:
MIAP[1]
/* 2, 21
rp0=21, rp1=21 */
using CVT table entry number 2 (value: 1,520). The fact that it is the second entry in the CVT
table shows the importance and general application of this value.
Finally—no surprise—an MIRP[]:
MIRP[01101]
/* 52, 27
rp1=21, rp2=27 */
moves us from point 21 to point 27 through CVT entry 52, the same one that we used in the
lower part of the letter.
Nonetheless, there is a δ instruction:
DELTAP1[ ]
/* 2, 21, 121, 9, 118 */
It applies to points 21 and 9 (the boundaries of the letter). The attributes are 121 (01111001)
and 118 (01110110). The lower nibbles are 1001 (9) and 0110 (6); thus the corrections are
small ones of 2
8 and −2
8, which is to say a quarter of a pixel upwards for point 21 and the
same amount downwards for point 9. These corrections are applied to the same size: 16 pixels
per em.
Now that we have finished the most important changes, the time has come to play “Harry
Potter” and launch our two magical instructions:
```

```text
IUP[1]
IUP[0]
which will interpolate all the points that we have not yet mentioned.
That could have been the last of the instructions. But it seems that there are still some other
horizontal δ corrections to perform. Thus we switch to horizontal mode with:
SVTCA[1]
and issue no fewer than 16 (!) δ instructions:
DELTAP1[ ]
/* 16, 23, 83, 19, 95, 17, 88, 13, 88,
11, 95, 7, 83, 5, 87, 1, 87, 18, 25,
12, 25, 6, 23, 0, 23, 18, 11, 12, 11,
6, 4, 0, 4 */
applied to points 23, 19, 17, 13, 11, 7, 5, 1 (which are the control points for the slanted external
tangents) and 18, 12, 6, 0 (which are the points on the curve for the same tangents). The
corrections that we have requested take the values 83 (−5
8 of a pixel, size 14), 95 (1 pixel,
size 14), 88 ( 1
8 of a pixel, size 14), 87 ( 7
8 of a pixel, size 14), 25 ( 2
8 of a pixel, size 10), 23 (−1
8 of a
pixel, size 10), 11 ( 4
8 of a pixel, size 9), 4 (−4
8 of a pixel, size 9). In other words, the corrections
to the control points apply only to size 14, whereas the corrections to the points on the curve
apply to sizes 10 and 9.
We can also understand why we waited until the end to make these corrections: it is because
all these points are “untouched” points, and only after global interpolation instructions have
been used do they assume their definite positions. A δ correction is a precise, localized operation; to interpolate a point after performing the δ correction would be in contradiction to
the precision and specificity of this operation.
```

F METAFONT and Its Derivatives Donald Knuth is an incurable perfectionist. He considered the issue of fonts when he decided to create a programming language for typesetting his books on programming. While he was at it, he decided to resolve the question of fonts once and for all by creating the ultimate programming language for creating all possible and imaginable fonts in the same logical, efficient way. That was 1979. The programming language in question is METAFONT. In 1983, a second version of the software was released to improve the language. That is the version that we use today. In the same year, 1983, John Warnock of Adobe was working on the PostScript language. That language was the ideal complement to TEX, since a DVI file produced by TEX could then be very profitably converted to PostScript. But the PostScript language, and even more the PDF format, signed the death warrant for METAFONT, at least in its current form. Knuth’s philosophy was to say that the rendering of glyphs was best handled by the central processing unit, since it could interpret the METAFONT language and construct perfect glyphs according to as many parameters as necessary. Having multiple printers is no problem: we merely tell METAFONT which printer we wish to use, and it applies the correct parameters. PostScript’s philosophy is different: according to PostScript, the printer should have a rendering engine intelligent enough to render any glyph according to the parameters provided. We send the printer some contours, and it fills them with pixels. Each approach has its advantages and disadvantages. We saw those of PostScript in Appendix C, where we discussed that language. Let us now examine those of METAFONT. METAFONT is extremely powerful for describing glyphs and even for describing their rendering. METAFONT does not work with contours, since glyphs have a certain dynamic that completely defies description by contours. For example, consider the ampersand, (&): it consists of a single stroke that goes down, up, and down again. Described in this way, the glyph has a visual logic, and that logic can be used for its optical correction (i.e., its adaptation to

```text
different optical sizes), its adaptation to the characteristics of the printer or the screen, and
even to its rasterization. The same glyph described by a PostScript contour no longer has any
dynamics: the contour does not even know that the strokes cross; thus it cannot tell that the
strokes on the two sides of an intersection must match up graphically. It is for such reasons
that there has never been a satisfactory way to create dynamic glyphs in PostScript.
The disadvantages of METAFONT are practical in nature. METAFONT must come between the
“abstract document” and the output device. But that goes against the principle of electronic
documents. An electronic document downloaded from the Web must be suitable for printing
anywhere, which means that METAFONT would have to be installed on every machine, that
fonts written in METAFONT (thus readily susceptible to piracy) would have to accompany
the document, and that the user would have to have a perfect knowledge of the technical
characteristics of his printer in order to share them with METAFONT. Not to mention that
the designer of METAFONT fonts would have to handle all possible and conceivable cases of
printers and screens in her code. Of course, if the industry had given METAFONT a slightly
warmer reception, we could imagine printers equipped with compilers for the language, and
also a form of PostScript that would incorporate METAFONT code to send it to the printer. We
could imagine Acrobat with a built-in METAFONT rendering engine that would perform the
rendering in real time. But that is nothing but fiction: the industry did not welcome METAFONT and did not deliver any support for it.
Nonetheless, we present METAFONT in this book, albeit only in the appendix, because there
is still a glimmer of hope. In the past few years, several attempts to “revive” this marvelous language have come to light. METATYPE1 is a project that uses a language similar to METAFONT
to create PostScript Type 1 fonts, and METATYPE is another whose purpose is to produce
TrueType fonts. Thus we can consider not the METAFONT software but the METAFONT programming language as a tool for “contemporary” font design. The possibilities of METAFONT
as a programming language go far beyond those of other font-design software. Only one thing
is missing: an interactive approach. But there is a good chance that the coming years will
bring us an interactive font editor that would work as a front end to the METAFONT language.
Stay tuned!
In the following text, the reader will find a very brief description of the language, based on
the personal experience of the author, who made his debut in the TEX community in the late
1980s by designing Gothic, Arabic, Hebrew, Greek, and other fonts, always in METAFONT.
F.1
The METAFONT Programming Language
F.1.1
Basic Concepts
There is a fundamental peculiarity of the METAFONT language that distinguishes it from all
other languages for graphical description: it takes initiatives. More precisely, METAFONT has
an inherent notion of “beauty”, and if we give it enough room for maneuver, it will draw
curves that it considers “beautiful”.
Let us take an example. Suppose that we have a line segment AB and that we ask a graphic
artist to draw a curve from point A, with a tangent perpendicular to the segment, that ends
at point B, once again perpendicularly to the segment. In the absence of other information,
what will he draw? We have no idea. But we know what METAFONT will do: it will draw
```

F.1. The METAFONT Programming Language a semicircle of diameter AB. Any other language for graphical description, such as PostScript or SVG or CGM, would have stopped and made the ironic and condescending remark “insufficient data”, worthy of the famous “Illogical, Captain!” that the noted Vulcan frequently uttered to the helpless human Captain Kirk. But since Kirk always won in the end, thanks to his human qualities and despite his illogicality, METAFONT always manages to draw “beautiful” curves, despite the lack of data supplied by its human operator. We have just said “despite the lack of data”. We could go further: most of the time it is “thanks to the lack of data”. Indeed, the author has often noticed that supplying fewer data to METAFONT produces a more beautiful curve. But how does METAFONT conceive of “beauty”? In his article “Mathematical Typography” [215], drawn from a presentation of January 4, 1978, Knuth defined the notion of the most pleasing curve, abbreviated “MPC”. After a description of the mathematical models of letters created by Dürer, Tory, Pacioli, Jaugeon, etc., he gives six principles for the MPC that passes through n given points: invariance (if the points of an MPC are rotated or translated, we obtain another MPC), symmetry (a cyclic permutation of the points does not change the result), extensibility (if we add a new point that is already on the MPC, the new curve is an MPC identical to the previous one), locality (the curve between two points zi and zi+3 depends only on the four points zi,... ,zi+3), and roundness (if four given points are consecutive points on a circle, then the MPC is that circle). He then shows that these conditions cannot all be respected at the same time but that we can work reasonably well by sacrificing one principle, and the principle that he chose to sacrifice was extensibility. In other words, if, starting with an MPC, we add a point that is already on the curve, the new MPC may not be the same. It was his thesis student, John Hobby [177], who put this theory into practice, using cubic Bézier curves (see Appendix G). Thus whenever we ask METAFONT to draw a curve, it always starts out as an MPC. But, of course, we can also impose constraints on it, and if we do badly enough, the “most pleasing curve” may well turn out not to be pleasing at all. METAFONT introduced an important concept, in the absence of Bézier curves and the PostScript language: the concept of pens. A pen is a shape of which a given point—which we shall call the “center”, even though it is not necessarily the center of the shape—moves along a Bézier curve. The pixels that it blackens are those that have been touched by the shape at a given moment during its trajectory. It is very important to understand that even though the center of the pen follows a Bézier curve, the contour of the blackened surface need not be made of Bézier curves! That is the main difficulty in converting from METAFONT to a type of font based on contours. In the absence of a precise mathematical solution, we must make do with methods for the autotracing of surfaces to obtain PostScript or TrueType contours from METAFONT glyphs. At least no risk is involved, since we can arbitrarily enlarge the bitmaps produced by METAFONT—which leaves the autotracing software no excuse for drawing the contour badly. One important concept is mode. By mode, we mean the characteristics of a printing or display device: its resolution, any additional blackening of pixels that may be required, the need to preserve the overshoot of rounded letters, the need to correct sharp corners by adding pixels, etc. These technical data may sometimes be difficult to understand, but we must have them

```text
in order to produce fonts that are perfectly suited to the device. As early as 1991, Karl Berry
undertook the monumental task of compiling modes for all printers and all displays; the
result is a file called modes.mf that is part of every TEX distribution. The reader should find
what he needs in that file; if not, the file explains how to test a printer in order to obtain the
correct values of the parameters.
Another essential notion: what are our base units? We have already seen in this book that
both PostScript and TrueType used abstract systems of coordinates connected to the real
world by transformation matrices. METAFONT is fundamentally different: it works with pixels!
But then we can legitimately raise the question: are we to use explicit values of pixels to
describe a glyph? Of course not. That is where the magic of the programming language
comes in. When we describe a glyph, we use variables that play the role of abstract units.
But we are the ones who get to define those variables. The connection with the real world is
made in a very clever way. There are two types of dimensions: sharp dimensions and plain old
dimensions. Sharp dimensions are followed by a crosshatch. Thus by writing 1dd#, we request
a true Didot point, whatever the optical size or resolution of the font may be. Conversely,
when we say 1dd, we obtain a number, which is the number of pixels that correspond to 1dd#
for the optical size of the font and the resolution of the current mode.
That allows us to work on two levels. First we define the parameters in sharp dimensions, and
when we have all the parameters that we need, we switch to pixel mode and ask METAFONT
to calculate the values of these parameters in pixels. From that point on, we work with those
values through the use of variable names, etc.
F.1.2
The Basics: Drawing and Filling
The reader will certainly have noticed that the METAFONT logo uses a font designed just for
it. For the TEX logo, we can use any font we please; we must merely make sure to move the ‘E’
correctly. For the METAFONT logo, however, we are required to use the Logo font.
We write METAFONT code in files with the extension “.mf”. METAFONT will read these files
and produce a GF font (see §A.5.2) and a TFM font (see §B.1). To produce the font, METAFONT first reads a configuration file, which gives the values of some parameters; then it reads a
number of files that contain descriptions of glyphs; finally, it reads files with data on kerning,
etc. This order is not fixed, but it is the most practical. Like TEX, METAFONT also has some
predefined instructions, called primitives. The primitives are rarely used; instead, we tend to
use the high-level instructions defined in a file called format. Currently the most commonly
used format is plain.
To run METAFONT, we enter on the command line the name of the executable file, the name
of the format (preceded by an at sign), the name of the mode, and the name of the “source”
file, which is to say the file that contains the values of the parameters and that will trigger the
reading of all the other files. The name of the font produced will be that of the source file.
But for very technical reasons, the syntax of this command line is quite peculiar. To specify
the plain format, the mode cx (which corresponds to the Canon printing engine, which is
embedded in the Apple LaserWriter printers), and the source file cmr10.mf, we write:
mf "&cm \mode:=cx; input cmr10"
```

```text
F.1. The METAFONT Programming Language
where the backslash indicates that we are already supplying METAFONT code rather than a
filename.
Now we are at a point at which we may ask: what does one write in a METAFONT file?
The basic syntax of METAFONT is much more approachable than that of TEX, for the simple
reason that it includes practically no text data, just instructions. And since there is nothing but
instructions, we are not required to protect those instructions, and everything is much easier
to do. Thus everything works as in an ordinary programming language: there are expressions
that end with a semicolon, and they contain instructions and parameters. Depending on the
situation, the parameters may be sharp dimensions or abstract numbers that designate pixels.
For example, the expression
z1=(50,50);
creates a variable z1 and assigns the value (50,50) to it. A few words of explanation are in
order: By writing x1=50; y1=50; we define the coordinates of point ‘1’. They may be written
with ‘x’ and ‘y’ for abscissas and ordinates or with ‘z’ (the symbol for complex numbers in
mathematics) to designate both coordinates at the same time. Conversion from ‘x’ and ‘y’
to ‘z’ and vice versa happens automatically.
The system of coordinates used by METAFONT is as follows: the origin of the coordinates
coincides with the origin of the glyph, and the units of the coordinate system are pixels. Thus
by writing (50,50), we obtain a point 50 pixels to the right of the origin and 50 pixels above it.
It behooves us to start out within the perspective of creating glyphs. To that end, here are two
instructions that “enclose” the code for the description of a given glyph:
beginchar(65,10pt#,10pt#,0pt#);
% the code for the glyph goes here
endchar;
bye
The instruction beginchar is a macro-command (or “macro”) that initializes METAFONT
so that it is ready to draw a glyph. Between parentheses, we write the parameters for the
macro, which are four in number: the glyph’s position in the font table (an abstract number;
in this case, 65), the set-width (in “sharp dimension”; here, 10 American printers’ points), and
the height and depth of the box containing the glyph. A semicolon terminates the expression.
The second line in the sample code begins with a percent sign; that line is a comment. The
third line is the endchar command, which terminates the code for the glyph’s description.
The last line tells METAFONT that the program ends at that location. If we omit that line,
METAFONT will switch to interactive mode and await additional instructions from the user.
What, then, shall we write for the glyph’s description? We have seen how to define points
through the use of explicit coordinates in pixels. But since the number of pixels depends on
the resolution and we want our glyph to be independent of the resolution, we shall define a
utility variable u, which will serve as our “base unit”. The value that we shall assign to this
variable is not of great importance. Let us take, for example, the equivalent of a point in
pixels:
```

u#=1pt#; define_pixels(u);
By writing u#=1pt#;, we define a “sharp” version of our variable—i.e., one that uses amounts
from the real world. In this case, its value is one American printers’ point.
Next, by writing define_pixels(u#), we request the creation of a variable u whose value is
the equivalent in pixels of u#. Here is where the conditions of rendering—mode, resolution,
size of pixels, etc.—come into play. Henceforth the value of u is a certain number (most likely
a rational one) of pixels. We do not know that number, but we shall use it to define the glyph.
Here is the brilliance of METAFONT: we do not define the variable u; rather, we define u# and
ask METAFONT to convert it to u according to the current size and mode.
METAFONT does the same for the three dimensions of the abstract box that contains the
glyph: using the “sharp” data that we provide, it defines the three variables w, h, and d, which
are the width, the height, and the depth of the glyph, expressed in pixels.
Thus, by writing:
z1=(.5w,0);
we define a point z1 that appears in the middle of the glyph’s width and on the baseline.
Defining points is very useful, but it is time to blacken a few pixels—by drawing something
pretty, if possible. That is done in two different ways: by drawing or by filling.
The first approach is that of the pencil or the paintbrush: we move our imaginary drawing
tool, and it leaves a mark on the page. That mark depends on the shape of the tool. The second
approach is that of the PostScript and TrueType fonts: we define a contour and fill it in black.
We can also combine the two approaches, by drawing a closed curve and then filling it.
Let us begin with drawing. To do so, we must first define the tool with which we intend
to draw. That is done through the instruction pickup followed by a description of the pen.
There are several types of pens: the most important are circular pens, defined by pencircle;
rectangular pens, defined by pensquare; and “razor” pens, defined by penrazor.
When we write:
pickup pencircle;
METAFONT will take a circular pen as the active pen. But what is its size? Since we have not
specified the size, the pen will be of diameter 1, i.e., one pixel. That is a rather poor choice,
as at a high resolution that poor little pixel is not visible to the naked eye. To specify the size
of a pen, we transform the default pen. We shall see that the transformation operators that we
shall apply to pens can in fact be applied to any METAFONT object. Here are some of these
operators:
• scaled, followed by a dimension, scales an object. There are two variants: xscaled
changes only the horizontal scaling factor, and yscaled changes the vertical one.
• rotated, followed by an angle (an abstract number), rotates an object through the angle
specified.

```text
F.1. The METAFONT Programming Language
Thus to obtain a round pen of thickness 0.4pt (four-tenths of an American printers’ point),
we write
pickup pencircle scaled 0.4pt;
Now we are ready to draw. By writing:
z1=(.5w,0); z2=(.5w+2u,0);
z3=(.5w+2u,2u); z4=(.5w,0);
draw z1--z2--z3--z4--cycle;
we obtain a square of side 2u. The double hyphen means that we are drawing a straight line
between the two points. The instruction cycle closes the contour.
We can rewrite the code above as a sequence of relative moves:
z1=(.5w,0); z2=z1+(2u,0);
z3=z2+(0,2u); z4=z3+(-2u,0);
draw z1--z2--z3--z4--cycle;
The result is the same, but the way of describing the path is a little more intuitive.
Before continuing with the drawing of curves, let us play around by modifying the pen. Let
us take an elliptical pen with a major axis of 0.6pt and a minor axis of 0.3pt that is turned
30 degrees and use it to draw the same square:
pickup pencircle xscaled 0.6pt
yscaled 0.3pt rotated 30;
z1=(.5w,0); z2=z1+(2u,0);
z3=z2+(0,2u); z4=z3+(-2u,0);
draw z1--z2--z3--z4--cycle;
The outline is already more interesting. And now let us take a “razor” pen, 0.6pt wide, that
is slanted 45 degrees:
pickup penrazor xscaled 0.6pt
rotated 45;
z1=(.5w,0); z2=z1+(2u,0);
z3=z2+(0,2u); z4=z3+(-2u,0);
draw z1--z2--z3--z4--cycle;
Now is the time to move on to curves. By writing two periods (“..”) instead of two hyphens
(“--”), we obtain curves instead of line segments. Let us apply the double period to two points,
using a slightly smaller circular pen:
pickup pencircle scaled 0.2pt;
z1=(.5w,0); z2=z1+(-3u,0);
draw z1..z2..cycle;
```

```text
Surprise! We obtain a circle, yet we never specified that that was the shape that we wanted.
What happened?
The expression z1..z2..cycle must be read as a whole: we start from z1 and return to the
same point, passing through z2 as well. In the absence of other instructions, METAFONT drew
the MPC (most pleasing curve) that passes through z1, z2, and z1 again: it is simply a circle of
diameter z1z2 that is drawn counterclockwise, starting from z1 and moving up and to the left.
The circle is certainly the most perfect shape, according to Eastern philosophers. But unless
we are designing a Futura or an Avant Garde, we will need other shapes as well. How can we
modify this basic shape?
The first thing that we can do is to impose an initial direction other than the vertical. We
indicate the direction that a curve takes when leaving a point through the use of an expression
in braces that is placed after the point in question. This expression can be a point or even a
primary direction (up, down, right, left), or it can be the keyword dir followed by an angle
in degrees.
For example, if we write z1{dir45}, the path will leave point z1 at an angle of 45°. Here an
angle of 0° corresponds to a direction that starts out towards the right (to the east, on a map);
thus 45° corresponds to a departure to the right and upwards (to the northeast).
In the circle that we obtained by default, the departure from point z1 was vertical, which
corresponded to an angle of 90°. Let us request an angle of 120°:
pickup pencircle scaled 0.2pt;
z1=(.5w,0); z2=z1+(-3u,0);
draw z1{dir120}..z2..cycle;
From this result, we can draw several conclusions. First, when we say “cycle”, we return to
the initial point, but not necessarily with the initial angle. Second, by modifying an angle
in the northern half of the cycle, we also modify the southern half; specifically, the angle of
approach to the point z2 has changed, and therefore also the angle of departure from that
point, and that is what changed the part of the curve that lies below the baseline.
Another way to modify the curve involves adding tension. The default value for tension is 1.
Let us use a tension of 1.5 between z2 and cycle—in other words, in the bottom half of the
curve:
pickup pencircle scaled 0.2pt;
z1=(.5w,0); z2=z1+(-3u,0);
draw z1{dir120}..z2..tension1.5..cycle;
Result: the lower half is tighter; the angles of approach to and departure from point z2 have
changed.
Now let us combine curves and straight lines. Let us define a point z3 below the baseline and
ask METAFONT to produce a curve between z1 and z2 and straight lines to connect z2, z3,
and again z1:
```

```text
F.1. The METAFONT Programming Language
pickup pencircle scaled 0.2pt;
z1=(.5w,0); z2=z1+(-3u,0);
z3=z1+(-1.5u,-2u);
draw z1..z2--z3--cycle;
A new surprise awaits us: the curve z1..z2 takes its simplest form, that of a straight line.
Conclusion: when we approach z2 with a curve and depart with a straight line, there is no
smooth connection between the two.
Now let us add a third hyphen between z2 and z3. Here is what we obtain:
pickup pencircle scaled 0.2pt;
z1=(.5w,0); z2=z1+(-3u,0);
z3=z1+(-1.5u,-2u);
draw z1..z2---z3--cycle;
How could we have obtained this head of an extraterrestrial? Because three hyphens are a
short way to say ..tension infinity..; thus we replaced a straight line segment with a curve,
but one of infinite tension. In this way, we obtain both the look of a straight line and a smooth
connection to the curve that precedes it.
What happens if we also replace the segment z3--cycle with a curve of infinite tension?
The result is deceptive: nothing changes, because we are making contradictory demands of
METAFONT. If z3---cycle is of infinite tension, it has the shape of a line segment. But then
it cannot form a smooth connection with z2--z3. Therefore METAFONT drops the smooth
connection and produces the same drawing for us.
Up to now we have seen the syntax of various lines that we can draw. Without being aware of
it, we have created a data structure that is very important in METAFONT, that of the path. We
can define a variable for a path with the keyword path and assign as its value an expression
similar to the one that we just saw:
path p; p=z1..z2---z3;
Later, we can use the variable p in a drawing instruction: draw
p;. If we have two paths,
p and q, for which the end of the former coincides with the start of the latter, we can merge
them with an ampersand (&). Thus draw p & q; will draw the concatenation of the two paths.
A path need not be closed. But if it is closed, we can fill it, using the fill command:
```

```text
z1=(.5w,0); z2=z1+(-3u,0);
z3=z1+(-1.5u,-2u);
fill z1..z2---z3--cycle;
Here we encounter a fundamental difference between METAFONT and PostScript or TrueType. In the latter, pixels can be either black or white, and applying black on black yields
white. In METAFONT, however, pixels are weighted. When they are of weight 0, they are
white. When we add a layer of black, the weight of the pixels is increased by 1; thus they
become black. When we add other layers of black, the weight increases; but as long as it
remains positive, the pixels will appear black.
The opposite command exists: unfill reduces the weight of a pixel. In the code below, we
shall define a second path inside the first and apply an unfill to it:
z4=(.5w-.5u,0); z5=z4+(-2u,0);
z6=z4+(-u,-1.5u);
unfill z4..z5---z6--cycle;
z1=(.5w,0); z2=z1+(-3u,0);
z3=z1+(-1.5u,-2u);
fill z1..z2---z3--cycle;
Note that we have deliberately “emptied” the path before “filling” it. After the unfill, the
pixels contained in the first path have a weight of −1. With the fill that followed, they were
assigned a weight of 0 and thus remained white.
The undraw command will “undraw” a path; that is, it will draw a path with a negative weight.
The commands filldraw and unfilldraw will draw and fill (or undraw and unfill) at the
same time. As simpler versions of draw and undraw, there are drawdot and undrawdot, which
draw or undraw a single point.
Now we shall try, as an exercise, to draw a circle inside a square. To obtain a square, we can
define points as follows:
z1=(0.5w-.5u,0); z2=(0.5w+1.5u,0);
z3=(0.5w+1.5u,3u); z4=(0.5w-.5u,3u);
But there is also a more elegant way. We can define the points’ coordinates separately, according to the logic of a horizontal square. For example, we can begin by observing that points
1 and 2 are at the same height, as are points 3 and 4, and that the height is known in each case:
y1=y2=0; y3=y4=3u;
```

```text
F.1. The METAFONT Programming Language
Next, we can say that points 1 and 4, and also points 2 and 3, have the same x-coordinate:
x1=x4; x2=x3;
Next, we can say that the square is symmetric about the bisector of the glyph’s width:
.5(x1+x2)=.5w;
Finally, we have the fact that it is a square; that is, its horizontal side is equal to its vertical side:
x2-x1=y4-y1;
The advantage of this way of expressing the points is that the length of the square’s side appears only once (when we say y3=y4=3u). Simply changing that one value will change the size
of the square automatically. And it will still remain centered relative to its set-width.
The syntax used above is an algebraic syntax. The equal sign does not have the same function
as in other programming languages. Specifically, when we write \$x1=\$x4; in the Perl language, for example, that means that the variable \$x1 takes the value of the variable \$x4. Here
that is not the case, for when we write x1=x4, neither of the two variables has a known value
yet. Using an algebraic syntax means that METAFONT will consider the expressions written
above as linear equations. When there is an equation for every variable, it will solve the linear
system and obtain values for those variables.
Let us return to our exercise. We shall draw the circle using a “calligraphic” pen—one that
is elliptical and turned at an angle. The circle will touch the square at the midpoints of the
sides. To express the fact, for example, that point z5, which is the starting point of the circle,
is halfway between z1 and z2, we can use the following notation:
z5=.5[z1,z2];
Instead of the .5, we can use any rational number. Writing a 0 gives us the first point; writing
a 1, the second.
Here, then, is an initial attempt to obtain a circle in the square:
pickup pencircle scaled 0.1pt;
y1=y2=0; y3=y4=3u; x1=x4; x2=x3;
.5(x1+x2)=.5w; x2-x1=y4-y1;
draw z1--z2--z3--z4--cycle;
pickup pencircle xscaled 0.5pt
yscaled 0.1pt rotated 45;
z5=.5[z1,z2]; z6=.5[z2,z3];
y8=y6; x7=x5; y7=y3; x8=x1;
draw z5..z6..z7..z8..cycle;
Seeing the result, we cannot really say that the circle lies within the square, as it slightly exceeds
the square’s bounds. Indeed, it is the center of the pen that touches the square, and we wanted
the edges of the pen to touch it.
```

```text
But when we draw a curve, it is the center of the pen that we manipulate. How can we know
the exact coordinates of the pen’s edges?
METAFONT has a very practical notation for that: by writing top z1, we obtain the uppermost
point of the pen whose center is placed on the point z1. If top is the top, we also have bot (the
bottom), rt (the right side), lft (the left). We can also combine them: bot lft z2 is the lower
left edge of the pen whose center is at the point z2.
We shall use these operators to draw our circle within the square:
pickup pencircle scaled 0.1pt;
y1=y2=0; y3=y4=3u; x1=x4; x2=x3;
.5(x1+x2)=.5w; x2-x1=y4-y1;
draw z1--z2--z3--z4--cycle;
pickup pencircle xscaled 0.5pt
yscaled 0.1pt rotated 45;
bot z5=.5[z1,z2]; rt z6=.5[z2,z3];
y8=y6; x7=x5; top y7=y3; lft x8=x1;
draw z5..z6..z7..z8..cycle;
Before moving on to the next important concept, pen strokes, let us do one exercise by way of
review: we shall draw the yin–yang symbol as elegantly as possible.
We shall use a width of 8 points and leave side-bearings of 1 point on each side. The outer
circle of the symbol will be drawn with a pen whose thickness is 1
3 of a point, and it must
descend by 1 point below the baseline:
beginchar(110,8pt#,8pt#,0pt#);
pickup pencircle scaled 0.2pt;
x3=x1=.5w; y2=y4=.5[y1,y3];
bot y1=-1pt;
w-rt x2=lft x4=1pt;
y3-y1=x2-x4;
draw z1..z2..z3..z4..cycle;
endchar;
Next, we shall fill in the left side:
beginchar(110,8pt#,8pt#,0pt#);
pickup pencircle scaled 0.2pt;
x3=x1=.5w; y2=y4=.5[y1,y3];
bot y1=-1pt;
w-rt x2=lft x4=1pt;
y3-y1=x2-x4;
draw z1..z2..z3..z4..cycle;
fill z3{left}..z4..z1{right} &
z1{left}.. .5[z1,z3]{right}
..z3{left} ..cycle;
endchar;
```

```text
F.1. The METAFONT Programming Language
Finally, we must draw the points that symbolize the birth of the new yin in the yang and the
new yang in the yin. To do so, we can go back to drawing mode, but first we select a pen whose
size is that of the dot. Since the centers of these dots are known, we need only draw a dot with
the pen and “undraw” one for the upper part, and our work is done:
beginchar(110,8pt#,8pt#,0pt#);
pickup pencircle scaled 0.2pt;
x3=x1=.5w; y2=y4=.5[y1,y3];
bot y1=-1pt;
w-rt x2=lft x4=1pt;
y3-y1=x2-x4;
draw z1..z2..z3..z4..cycle;
fill z3{left}..z4..z1{right} &
z1{left}.. .5[z1,z3]{right}
..z3{left} ..cycle;
draw z1..z2..z3..z4..cycle;
pickup pencircle scaled 1pt;
drawdot .25[z1,z3];
undrawdot .75[z1,z3];
endchar;
F.1.3
More Advanced Concepts: Pen Strokes and Parameterization
Let us not delude ourselves: the “pens” that we described in the previous section are poor
tools for the graphic designer. How can we draw beautiful things with a pen that changes
neither its shape nor its angle of inclination? The letters that we design in that way will be
singularly dull, artificial, boring.
To account for that problem, METAFONT introduced another concept: pen strokes. This time
the logic is different. We shall work with “razor” pens and define a number of pen positions. A
pen position includes both the coordinates of its center and the width and angle of the pen.
Suppose, for example, that we define two points z1=(6u,0) and z2=(2u,0). We place a pen
of width 1u and angle 60° on the first point. On the second, we place a pen of width 2u and
angle 120°. To do so, we use the macro penpos, followed by three arguments: the position
number, the width of the pen, and the angle of the pen position.
METAFONT will then calculate the position of the extremities of these pen positions. They are
denoted z1l (left extremity of point z1), z1r (right extremity of point z1), etc. It is important
to understand here that “left” and “right” here are defined from the point of view of someone
who is standing on the pen position.
Now, to draw the pen stroke that goes between these two positions, we use the keyword penstroke, and the suffix e for each of the positions. That suffix indicates that we are referring
not to the point at the center of the position but rather to the whole pen position. Only one
thing remains: defining the initial direction. If the position of pen 1 has an angle of 60°, it
makes sense that the initial direction be perpendicular to the pen’s angle; it will therefore
be 60+90 = 150°. Here is the result:
```

```text
z1=(6u,0); z2=(2u,0);
penpos1(1u,60); penpos2(2u,120);
penstroke z1e{dir150}..z2e;
All of the tricks of the previous section can be applied here: directions, tension, the keyword cycle, triple hyphens. Furthermore, we are not required to state the coordinates of
the center of a pen position immediately. We can very well define the position and give its
coordinates only at the last minute. But flexibility has its limits: the values of the arguments
of the penpos macro may not be unknown when the position is defined. When we write
penpos1(width,angle), the values of width and angle must be known.
To achieve a better understanding of the vast possibilities that METAFONT’s concept of pen
stroke offers us, we shall examine an example from the real world, step by step. We shall write
the code for the following glyph, which is inspired by the ‘n’ of the font Vendôme:
The first step is to place the pen positions at the correct locations. We need to capture the dynamics of the letter. To get a better feeling for these dynamics, let us consider some questions:
What would happen if these parameters changed? If the letter became lighter or bolder?
What are its relevant strokes? What are the strokes that will remain the same irrespective of
the values of the parameters?
After due reflection, the author came to the conclusion that the the most relevant pen positions might be the following:
```

```text
F.1. The METAFONT Programming Language
1l
1r
3l
3r
2l
2r
4l
4r
5l
5r
6l
6r
7l
7r
8l
8r
9l
9r
10l
10r
11l
11r
12l
12r
13l
13r
14l
14r
Let us analyze this configuration. The letter includes a downstroke on the left, an arch that
starts from the inside of the left-hand downstroke and ends in the right-hand downstroke, two
serifs on the baseline, and a head serif on the left-hand downstroke. Among these elements,
the most important are the two downstrokes and the arch. We can start with those. The lefthand downstroke corrects pen positions 3 and 4. It is slightly curved. The location of pen
position 4 seems clear. But at what height should we place position 3?
If we set positions 9 and 10 at those precise locations, it is because they are where the edges of
the arch are horizontal and vertical, respectively. By taking measurements, we find that the
center of pen 9 is at the same height as that of pen 1, which is the starting point of the head
serif. But let us not forget that our letter does not appear in isolation: it is part of a font; and in
that font, as in any Latin font, there is a relevant height, that of the lowercase letters, which
we call the x-height. It turns out that the left edge of pen 1 appears at the x-height. If z9l is
slightly higher, that is because we have overshoot.
Without even being aware of it, we have been performing parameterization. We have already
established two parameters for the font: the height of the lowercase letters and the amount
of overshoot. There are four other parameters that appear very clearly in our construction:
the thickness of the downstroke, which is that of pens 4 and 11; the thickness of the upstroke,
which is that of pen 8; the thickness of the tips of the serifs (pens 1, 5, 7, etc.), and the “inside”
thickness of the serifs (pens 6 and 13). These are the parameters that will determine the behavior of our glyph. We shall call them stem, join, serif_tip, serif_ht. Likewise, we shall
use x_height for the x-height and oo for the overshoot.
But let us go back to our analysis. Using arrows, we find the (hypothetical) motion made by
the calligrapher who drew this letter. Why was z8 placed at the midpoint of the left downstroke? After all, what difference would it make if we placed farther to the left or the right,
as long as it lies within the downstroke? Because we cannot know the thickness of the heavy
stroke in advance. If we place z8 too far to the right, it may lie outside the downstroke if that
```

```text
stroke is too light. If we place z8 too far to the left, it may become exposed if the downstroke
is light. By placing it in the middle, we make sure that the arch will always begin within the
downstroke.
That is also why we place z3 on the hypothetical curve that connects z1 to z2.
Now let us begin writing code. First, we must define our parameters. To that end, we have
the instruction numeric, whose role is to define simple numeric variables:
numeric x_height, oo, stem, join, serif_tip, serif_ht;
There is another instruction, pair, to define points—pairs of numeric values—but we do not
need it here. Next, we shall give provisional values to these parameters. To obtain an initial set
of values, we can place an ordinary sheet of tracing paper, with a grid marked in millimeters,
over the letter’s sketch and take some measurements. Here are some of the values obtained
in this manner:
x_height=5.1u; oo=.2u;
stem=1.1u; join=.2u;
serif_tip=.2u; serif_ht=.7u;
Now let us address the left-hand downstroke. Although we will be more malevolent later on,
we can begin by using a measured value taken from our graph paper as the x-coordinate of
pen 4. On the other hand, close examination reveals that the serifs are slightly flared. Let
us use the name delta (a value that is very small but not zero) for the heights of points
z4 and z11:
numeric delta; delta=.033u;
z4=(1.6u,delta);
As for point z3, we would like to control the angle of the downstroke. Let us use offset for
the offset between the x-coordinates of points z3 and z4, and let us give it the provisional
value of 0.125u. Thus we need only write:
numeric offset; offset=.125u;
x3=x4+offset; y3r=x_height;
Before drawing the downstroke, we need to define pen positions 3 and 4. For pen 4, this is
easy:
penpos4(stem,180);
On the other hand, pen 3 is not perfectly horizontal. Thus we shall construct this pen position from the data that we have. We already know the locations of x3 and y3r. It would be
interesting to have a horizontal projection of our pen that is equal to stem:
x3l-x3r=stem;
```

```text
F.1. The METAFONT Programming Language
Finally, we can say that the difference in height between z3l and z3r is half of serif_tip:
y3l-y3r=.5serif_tip;
Thus it has turned out to be unnecessary to write penpos3: we found the pen position by
calculating the coordinates of points z3r and z3l. Nonetheless, METAFONT cannot read our
minds; we do have to tell it that z3 lies halfway between points z3l and z3r:
z3=.5[z3l,z3r];
To draw the stroke, we have only to specify the direction in which to start. For now, we can
allow METAFONT to choose the starting direction; we shall merely state that point z4 must
be approached vertically:
penstroke z3e..{down}z4e;
And here is the result:
beginchar("n",7pt#,6pt#,0pt#);
u#=1pt#; define_pixels(u);
numeric x_height, oo, stem,
join, serif_tip, serif_ht;
x_height=5.1u; oo=.2u;
stem=1.1u; join=.2u;
serif_tip=.2u; serif_ht=.7u;
numeric delta; delta=.033u;
z4=(1.6u,delta);
numeric offset; offset=.125u;
x3=x4+offset; y3r=x_height;
penpos4(stem,180);
x3l-x3r=stem;
y3l-y3r=.5serif_tip; z3=.5[z3l,z3r];
penstroke z3e..{down}z4e;
endchar;
A great deal of code for just one stroke, but it will be much easier from now on! Now let us
draw the connecting stroke and the second downstroke. We shall use graph paper to measure
the x-coordinate of z11; its y-coordinate will be the same as that of z4. But let’s be wicked:
since we measured the x-coordinate of z4 from the glyph’s origin, let us measure that of z11
from the glyph’s set-width. In this way, the glyph is tied to the dimensions of the abstract box
that contain it.
x11=w-.65u; y11=y4; penpos11(stem,180);
As for points z8r and z10r, we can see that they are at the same height, which is seven-tenths
of the x-height:
y10=y8=.7x_height;
```

```text
We want the angle of segment z11--z10 to be the same as that of segment z4--z3. To that
end, we shall use a keyword that is very important in METAFONT, the keyword whatever.
The expression:
z10-z11=whatever*(z3-z4);
can be interpreted as “the vector −−−→
z10z11 is a scalar multiple of the vector −→
z3z4”, which means
that they “have the same direction”. Thus we need only give the height of z10 to establish the
exact position of that point. We have already given the height of z10r; now we must give the
characteristics of pen position 10. For consistency’s sake, we can decide that this pen will have
the same width and angle as pen 3:
z10l-z10r=z3l-z3r; z10=.5[z10l,z10r];
We now have pens 10 and 11; let us proceed for 9 and 8. What will the width of pen 9 be? We
do not yet know. But we can say that it must be proportional to both 10 (i.e., the parameter
stem) and 8 (the parameter join). It is sufficient to indicate where this value lies between
join and stem. Using measurements from our graph paper, we find that the width of 9 is
.87[join,stem] and that its angle is −136°:
penpos9(.87[join,stem],-);
We have already determined the height of z9l:
y9l=x_height+oo;
but what is its x-coordinate? That is a delicate question, because the aesthetic quality of the
arch depends on that x-coordinate. Since the widths of the pens can vary according to the
values of the parameters, we should reason in terms of a “skeleton” stroke. Thus we shall
define the x-coordinate of the center of pen z9 according to those of points z8 and z10:
x9=.68[x8,x10];
On the other hand, we may suppose, for simplicity’s sake, that z8 lies on the line connecting
z3 and z4:
z8=whatever[z3,z4];
Now all that remains is to determine the width and the angle of pen 8. First, what is the
starting angle of the arch? We can measure it, of course; in the figure, it is 37°. But that angle
will change if the width of the glyph changes. It would be more appropriate to say that the
line tangent to the arch at initial point z8 must intersect the (hypothetical) extension of the
right-hand downstroke at a given height:
```

```text
F.1. The METAFONT Programming Language
8l
8r
9l
9r
10l
10r
8'
By defining point z8' and allowing the stroke that starts from z8 to head in the direction of
that point, we have a way of starting our arch independently of the letter’s set-width. Here is
how we can define z8':
z8'=whatever[z11,z10]; y8'=6.33u;
Pen 8 must be perpendicular to the direction z8--z8':
penpos8(join,angle(z8'-z8)-);
All that remains is to draw the stroke:
penstroke z8e{z8'-z8}..z9e{right}..z10e..{down}z11e;
And here is the result:
beginchar("n",7pt#,6pt#,0pt#);
... previous code ...
x11=w-1.65u; y11=y4; penpos11(stem,180);
y10=y8=.7x_height; z8=whatever[z3,z4];
z10-z11=whatever*(z3-z4);
z10l-z10r=z3l-z3r; z10=.5[z10l,z10r];
penpos9(.87[join,stem],-136);
y9l=x_height+oo;
x9=.68[x8,x10];
z8'=whatever[z11,z10]; y8'=1.25x_height;
penpos8(join,angle(z8'-z8)-90);
penstroke z8e{z8'-z8}..z9e{right}..
z10e..{down}z11e;
endchar;
We can see that we may have allowed METAFONT a bit too much freedom: the arch and
the right-hand downstroke are a bit too soft; we wanted something tighter. Let us adjust the
tension between 8 and 9 and replace z10e..z11e with a curve of infinite tension:
```

```text
beginchar("n",7pt#,6pt#,0pt#);
... previous code ...
x11=w-1.65u; y11=y4; penpos11(stem,180);
y10=y8=.7x_height; z8=whatever[z3,z4];
z10-z11=whatever*(z3-z4);
z10l-z10r=z3l-z3r; z10=.5[z10l,z10r];
penpos9(.87[join,stem],-136);
y9l=x_height+oo;
x9=.68[x8,x10];
z8'=whatever[z11,z10]; y8'=1.25x_height;
penpos8(join,angle(z8'-z8)-90);
penstroke z8e{z8'-z8}..tension 1.5..
z9e{right}..z10e---z11e;
endchar;
The result is already much more acceptable. Now let us add the head serif to the left-hand
downstroke. We see that we shall need a new parameter: the width of the serif. Our model
glyph has serifs of highly varying width; we shall take one of them as a parameter, and the
others will have values proportional to it. Let us take the left serif of the right-hand downstroke as our starting point and define serif as:
numeric serif; serif=x11r-x12=1u;
A measurement from our graph paper shows us that x7-x4l is also equal to serif. On the
other hand, x3r-x1=.95serif, x4r-x5=.9serif, and x14-x11l=.8serif. Therefore, we have:
x7-x4l=serif; x3r-x1=.95serif; x4r-x5=.9serif; x14-x11l=.8serif;
Now we need to set pen positions 1 and 2. Here is the data that we already know:
y1=y3; penpos1(serif_tip,-); z2=z3l;
But that does not give us the angle of pen 2. That angle must be equal to the starting angle
of the stroke connecting positions 3 and 4. What is that angle? We do not know, because we
have allowed METAFONT to choose it. By writing:
penstroke z3e..{down}z4e;
we have only decided that the angle at the end of the stroke must be vertical. How, then, can
we find the angle that we need? If METAFONT chose it, then METAFONT must know what it
is. Indeed, there is a command, named direction, that gives us the direction that a path has
at a given moment.
Let us pause briefly to explain this command. We have seen that METAFONT has a data structure called the “path”. A path is obtained by drawing Bézier curves (or straight line segments)
that go through several points. If there are n+1 points, z0,z1,... ,zn, we say that at time t, we
are at point zi. And at time t′ ∈[t,t +1], we are somewhere between zt and zt+1.
```

```text
F.1. The METAFONT Programming Language
The direction command takes as its arguments a time t and a path. It returns the direction
of the path at the specified time.
In our case, the path is none other than:
z3l..{down}z4l
and the time, for simplicity’s sake, is that of the start of the path, namely 0. The path’s direction at time 0 is:
direction 0 of (z3l..{down}z4l)
But to define a pen position, we need an angle, not a direction. Never fear: the angle command will give us the angle of a direction:
angle(direction 0 of (z3l..{down}z4l))
and we can therefore define pen position 2 as follows:
penpos2(1.25serif_ht,direction 0 of (z3l..{down}z4l));
We draw the head serif in this way:
penstroke z1e{right}..z2e;
Here is the result:
beginchar("n",7pt#,6pt#,0pt#);
... previous code ...
numeric serif; serif=x11r-x12=1.55u;
x7-x4l=serif; x3r-x1=.95serif;
x4r-x5=.9serif; x14-x11l=.8serif;
y1l=y3l; penpos1(serif_tip,-90); z2=z3l;
penpos2(1.25serif_ht,angle(direction 0
of (z3l..{down}z4l)));
penstroke z1e{right}..z2e;
endchar;
Only the serifs remain. The code is simple:
penpos5(serif_tip,-); penpos7(serif_tip,-);
penpos12(serif_tip,-); penpos14(serif_tip,-);
penpos6(serif_ht,-); penpos13(serif_ht,-);
y5r=y7r=y12r=y14r=0; z6r=z4; z13r=z11;
penstroke z5e{right}..z6e & z6e..{right}z7e;
penstroke z12e{right}..z13e & z13e..{right}z14e;
```

```text
And here is the result:
beginchar("n",7pt#,6pt#,0pt#);
... previous code ...
penpos5(serif_tip,-90); penpos7(serif_tip,-
90);
penpos12(serif_tip,-90);penpos14(serif_tip,-
90);
penpos6(serif_ht,-90); penpos13(serif_ht,-
90);
y5r=y7r=y12r=y14r=0; z6r=z4; z13r=z11;
penstroke z5e{right}..z6e &
z6e..{right}z7e;
penstroke z12e{right}..z13e &
z13e..{right}z14e;
endchar;
But what would happen if serif became so large that the space between the downstrokes was
not wide enough to hold the two half-serifs? We do not want the serifs to overlap. On the
contrary, we would like for a safe distance to be preserved between z7 and z12—a distance
of .2u, let us say.
For that purpose, we shall use two of METAFONT’s other features: (re)assignments and tests.
The following code tests whether the sum of x7-x4, .2u, and x11-x12 exceeds the letter’s aperture (i.e., x11-x4). If that is the case, we redefine the values of x12 and x7:
if (x7-x4+.2u+x11-x12 > x11-x4):
x7:=.5[x4,x11]-.1u;
x12:=.5[x4,x11]+.1u; fi
Here, by way of review, is the code for this letter ‘n’, which has enabled us to explore quite a
few of METAFONT’s features:
beginchar(110, 7pt#, 6pt#, 0pt#);
u# = 1pt#; define pixels(u);
numeric x_height, oo, stem, join, serif_tip, serif_height, delta, offset;
x_height = 5.1u; oo = .2u; stem = 1.1u; join = .2u;
serif_tip = .2u; serif_height = .7u; delta = .033u; offset = .125u;
z4 = (1.6u, delta); penpos4(stem, 180);
x3 = x4 +offset; y3r = x_height;
x3l −x3r = stem; y3l −y3r = .5serif_tip; z3 = .5[z3l, z3r];
penstroke z3e . . {down}z4e;
x11 = w−1.65u; y11 = y4; penpos11(stem, 180);
y10 = y8 = .7x_height; z8 = whatever[z3, z4];
z10 −z11 = whatever ∗(z3 −z4);
z10l −z10r = z3l −z3r; z10 = .5[z10l, z10r];
penpos9(.87[join, stem], −136); y9l = x_height +oo; x9 = .68[x8, x10];
z8′ = whatever[z11, z10]; y8′ = 1.25x_height;
```

```text
F.1. The METAFONT Programming Language
penpos8(join, angle(z8′ −z8)−90);
penstroke z8e{z8′ −z8} . . tension 1.5 . . z9e{right} . . z10e - - z11e;
numeric serif; serif = x11r −x12 = 1u;
x7 −x4l = serif; x3r −x1 = .95serif ; x4r −x5 = .9serif ; x14 −x11l = .8serif ;
y1l = y3l; penpos1(serif_tip, −90); z2 = z3l;
penpos2(1.25serif_height, angle(direction 0 of (z3l . . {down}z4l)));
penstroke z1e{right} . . z2e;
if (x7 −x4 +.2u+x11 −x12 > x11 −x4):
x7 := .5[x4, x11]−.1u;
x12 := .5[x4, x11]+.1u; fi
penpos5(serif_tip, −90); penpos7(serif_tip, −90);
penpos12(serif_tip, −90); penpos14(serif_tip, −90);
penpos6(serif_height, −90); penpos13(serif_height, −90);
y5r = y7r = y12r = y14r = 0; z6r = z4; z13r = z11;
penstroke z5e{right} . . z6e &z6e . . {right}z7e;
penstroke z12e{right} . . z13e &z13e . . {right}z14e;
endchar;
The formatting of the code above was done by a pretty-printer for METAFONT code, known
as mft. This utility converts METAFONT code into TEX code with a rather refined layout that,
unfortunately, can be compiled only under the plain format. There is a LATEX package called
mftinc that allows code produced by mft to be included in a LATEX document, as we did above.
The reason that we used so many parameters in the METAFONT code above is to have the
ability to play with them. Let us try some tests.
First of all, we can have fun modifying the thickness of the downstroke (the stem parameter).
For example, we can start with stem=join and go up to stem=2.2u, which is twice the standard
value.
To do so, we shall create a test font in which the first 64 glyphs will be variants of the one that
we have just designed. We shall use the following code:
input modes.mf;
mode_setup;
font_size 10pt#;
font_quad 18pt#;
font_normal_space 6pt#;
u#=1pt#; define_pixels(u);
numeric i;
for i=0 step 1 until 63:
beginchar(i,7pt#,6pt#,0pt#);
...
```

```text
stem=(i/63)[join,2.2u];
...
endchar;
endfor
bye
And we shall generate the font by writing:
mf "\mode:=linoone; proofing:=0; mag:=1.5; input testfont;"
gftopk testfont.1905gf
A few words of explanation: The mode linoone is for the Linotype phototypesetters that were
used to make the plates for this book; since that mode has a resolution of 1,270 ppi and the
font used in the test is a 15-point font, the file generated by METAFONT has a resolution of
1,905 points. In the METAFONT code, we first call for the reading of the file modes.mf, which
contains the definition of the linoone mode; then we perform mode_setup to establish the
conversion from “true” units to units in pixels; then we give some of the font’s metric parameters: the type size, the size of the em, and the width of the normal space.
Next, we define a numeric variable i and create a loop using that variable, with an increment of 1, running from 0 to 63. Finally, instead of writing stem=1.1u in the code, we write
stem=(i/63)[join,2.2u], which means that we go from the value of the connecting stroke
to 2.2u in 64 steps.
And here is the result:
 






```


Æ













!
"
#
\$
%
&
'
(
)
*
+
,
-
.
/
:
;
<
=
>
?
Note that we have modified only one parameter and that properly increasing the glyph’s
weight would also have required the modification of the other parameters at the same time.
Let us run another test: we shall modify the glyph’s set-width. We wish to emphasize that it
is not merely a matter of reducing the image’s horizontal scaling factor. We shall modify the
set-width while leaving all the stroke thicknesses unchanged. Here is the result:


        Æ       ! " # \$ % &

F.1. The METAFONT Programming Language
'
(
)
*
+
,
-
 .
/






:
;
<
=
>
?
Let us continue the torture session to which we are subjecting this innocent glyph. We shall
make this font into a mechanistic font worthy of those of the nineteenth century. To do so,
we shall increase the thickness of the ends of the serifs—that is, the parameter serif_tip.
In doing so, we notice that we have not taken all the necessary precautions. In particular,
we wrote the following in our code: serif_tip=.2u;
serif_ht=.7u;. What will happen
if serif_tip becomes larger than serif_ht? To prevent that eventuality, let us replace the
line with:
serif_tip=.2u; serif_ht=max(serif_tip,.7u);
Now serif_ht is always at least as large as serif_tip. One other change to make: as the serifs become larger, it is also desirable to thicken the letter’s connecting stroke slightly. Here
we shall take connecting strokes whose thickness is at least half that of the tips of the serifs:
join=max(.2u,.5serif_tip);. Here is what we get once these precautions have been taken:
 








Æ













!
"
#
\$
%
&
'
(
)
*
+
,
-
.
/
:
;
<
=
>
?
Finally, we can play with the lengths of the serifs—the serif parameter. Let us draw glyphs
for which the serif parameter ranges from 0 to 1.5 times the usual serif:
 








Æ













!
"
#
\$
%
&
'
(
)
*
+
,
-
.
/
:
;
<
=
>
?

```text
F.1.4
Optimizing the Rasterization
In Chapter 13, we saw the different techniques that PostScript and TrueType fonts use to
optimize the rasterization at a low resolution, whether on the screen or in printed output.
What does METAFONT do?
As we shall see in this section, METAFONT goes far beyond the other formats in this area. The
reason is very simple. We have already mentioned that in METAFONT code we work with
pixels. Thus optimization is merely a matter of checking whether the values of the different
dimensions are whole (not just rational) and that the dimensions that traditionally cause
problems, such as stroke thicknesses, are equal. Unlike PostScript fonts, our METAFONT fonts
have no need of hints, as we have complete control over the rendering; and unlike TrueType,
METAFONT does not use obscure assembly instructions but rather a genuine high-level programming language.
Let us examine several examples to see how METAFONT optimizes the rendering. First, let us
take the most classic case, that of the letter ‘H’. To check the rendering of this glyph at low
resolution, we shall use the utility gftype (see §A.5.2). Here is what we obtain for METAFONT
mode epsdrft at a resolution of 72 ppi:
autorounding:=0;
smoothing:=0;
u#=2pt#; define_pixels(u);
beginchar("H",14pt#,12pt#,0pt#);
pickup pensquare scaled 1u;
lft bot z1=(1u,0);
x2=x1; top y2=h;
x3=w-x1-.666u; y3=y1; x4=x3; y4=y2;
z5=.5[z1,z2]; z6=.5[z3,z4];
draw z1--z2; draw z3--z4; draw z5--z6;
endchar;
GGGG
GGG
GGGG
GGG
GGGG
GGG
GGGG
GGG
GGGG
GGG
GGGG
GGG
GGGG
GGG
GGGG
GGG
GGGGGGGGGGGGGG
GGGGGGGGGGGGGG
GGGGGGGGGGGGGG
GGGGGGGGGGGGGG
GGGG
GGG
GGGG
GGG
GGGG
GGG
GGGG
GGG
GGGG
GGG
GGGG
GGG
GGGG
GGG
GGGG
GGG
We see that what we feared did indeed come to pass: the downstroke on the left is not of the
same thickness as the downstroke on the right. We must admit that we did in fact deliberately create this catastrophe: we explicitly asked METAFONT not to optimize the rendering
automatically, by setting the parameters autorounding and smoothing to zero.
The solution is easy: METAFONT has an instruction called round that rounds the value given
as its argument. Here, the values x1 and x3 have not been rounded; thus let us change our
code to:
```

```text
F.1. The METAFONT Programming Language
autorounding:=0;
smoothing:=0;
u#=2pt#; define_pixels(u);
beginchar("H",14pt#,12pt#,0pt#);
pickup pensquare scaled 1u;
lft bot z1=round(1u,0);
x2=x1; top y2=h;
x3=round(w-x1-.666u); y3=y1; x4=x3; y4=y2;
z5=.5[z1,z2]; z6=.5[z3,z4];
draw z1--z2; draw z3--z4; draw z5--z6;
endchar;
GGG
GGGG
GGG
GGGG
GGG
GGGG
GGG
GGGG
GGG
GGGG
GGG
GGGG
GGG
GGGG
GGG
GGGG
GGGGGGGGGGGGGGG
GGGGGGGGGGGGGGG
GGGGGGGGGGGGGGG
GGGGGGGGGGGGGGG
GGG
GGGG
GGG
GGGG
GGG
GGGG
GGG
GGGG
GGG
GGGG
GGG
GGGG
GGG
GGGG
GGG
GGGG
That did not work. Indeed, we were very clumsy: on the left we rounded the left side of the
pixel, and on the right we rounded the center of the pixel. It is not surprising that the result
was poor. To correct it, we must round the pixels on both sides. Thus we shall write:
rt x3=round(w-lft x1-.666u);
which does indeed give the correct result:
autorounding:=0;
smoothing:=0;
u#=2pt#; define_pixels(u);
beginchar("H",14pt#,12pt#,0pt#);
pickup pensquare scaled 1u;
lft bot z1=round(1u,0);
x2=x1; top y2=h;
rt x3=round(w-lft x1-
.666u); y3=y1; x4=x3; y4=y2;
z5=.5[z1,z2]; z6=.5[z3,z4];
draw z1--z2; draw z3--z4; draw z5--z6;
endchar;
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGGGGGGGGGGGGGG
GGGGGGGGGGGGGGG
GGGGGGGGGGGGGGG
GGGGGGGGGGGGGGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
Now let us take a more complex case, that of the letter ‘T’. We shall draw it in a rather peculiar
way in order to force an asymmetric rendering:
```

```text
beginchar("T",11.8pt#,12pt#,0pt#);
pickup pensquare scaled .9u;
bot z1=(.5w-.33u,0);
x2=x1; top y2=top y3=top y4=h;
lft x3=0; rt x4=w-.66u;
draw z1--z2; draw z3--z4;
endchar;
GGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
Indeed, we have 8 pixels on the left and only 7 on the right. What to do?
We can start by noticing that since the error in the rendering came from the rounding
of (w-.66u), that error cannot be more than 1 pixel at the most. Thus we can compare
the number of pixels in the horizontal stroke to the right and to the left of the stem. If the
number on the right is larger, we shall subtract a pixel from it; if the number on the left is
larger, we shall do the opposite.
Here is the code, along with the result, which is good:
beginchar("T",11.8pt#,12pt#,0pt#);
pickup pensquare scaled .9u;
lft bot z1=(round(lft .5w-.33u),0);
x2=x1; top y2=top y3=top y4=h;
lft x3=0; rt x4=w-.66u;
if (round(lft x1)-round(lft x3) >
round(rt x4)-round(rt x1)):
x4 := x4+1; fi
if (round(lft x1)-round(lft x3) <
round(rt x4)-round(rt x1)):
x4 := x4-1; fi
draw z1--z2; draw z3--z4;
endchar;
GGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGG
GGGGGGGGGGGGGGGGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
GGG
This code is somewhat inelegant. It is easier to use a macro defined by Knuth to solve problems of this kind: change_width. The idea is that we want what is left of the glyph’s set-width,
after we have taken a pixel from the downstroke, to be an even number of pixels. If that is
not the case, we add or subtract a pixel, as needed, so as to be closer to the unrounded value.
Adding or subtracting a pixel changes the parity of the set-width and solves the problem.
To avoid such problems from the start, we can define “correct amounts in pixels for the active pen”. Explanation: if we define, for example, sidebearing as the left side-bearing, then
there is no point in rounding its value, since if we place the center of a pen on the point
z1=(sidebearing,0), it is the left edge of the pen, not its center, that will be rounded.
Thus we should lft z1=(round(lft sidebearing),0). A more elegant way to write it is:
```

```text
F.1. The METAFONT Programming Language
z1 = (good.x sidebearing,0);
Even better, we can define the pixel version of sidebearing# as a “correct value”:
define_good_x_pixels(sidebearing);
After that, the value of sidebearing is correct, for the active pen, in the sense that lft sidebearing is a round number.
A case similar to that of ‘T’: the point of the letter ‘V’. A naive approach would be to write:
beginchar("V",13pt#,12pt#,0pt#);
pickup pencircle scaled .3u;
lft top z1=(0,h); rt top z3=(w,h);
z2=(.5w-eps,good.y 0);
draw z1--z2--z3;
endchar;
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
GG
G
But the point is not symmetrical. Why not? Because the row of pixels immediately above the
point contains two pixels. Aside from the point, the rest of the letter is symmetrical. Thus we
have the same number of pixels on each side. Conclusion: the problem comes from the fact
that the sum of all the pixels is an even number. Thus we shall adopt Knuth’s solution: we
shall check whether the total width of the letter is an even number of pixels, and, if it is, we
shall use the change_width command.
To check whether a number is even, we merely take half of the number and compare it with
its rounded version. If the two are equal, the original number is even. Here, then, is the code,
together with the results obtained:
beginchar("V",13pt#,12pt#,0pt#);
pickup pencircle scaled .3u;
if (.5w = round(.5w)): change_width; fi
lft top z1=(0,h); rt top z3=(w,h);
z2=(.5w-eps,good.y 0);
draw z1--z2--z3;
endchar;
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G G
G G
G
```

```text
Note that the change_width method works because the letter’s width in pixels is directly related to the set-width.
Let us take one last example, a more complicated one: that of the letter ‘O’. Our first attempt
will be to write:
beginchar("O",10pt#,12pt#,0pt#);
pickup pencircle scaled .3u;
lft z1=(0,.5h);
z2=(.5w,0); x4=x2; y4-y2=x3-x1;
rt z3=(w,.5h);
draw z1..z2..z3..z4..cycle;
endchar;
GGGGGGGGG
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
GG
GG
GGGGGGG
We see that there are far more pixels at the bottom than at the top. The problem comes
from the fact that at the bottom of the letter we placed the center of the pen on the baseline,
whereas at the top we really do not know exactly what is going on, since y4-y2=x3-x1 has no
reason to be round. We could, of course, round that amount, but doing so would not ensure
that the letter would turn out symmetrical; indeed, it would not, as can be seen below:
beginchar("O",10pt#,12pt#,0pt#);
pickup pencircle scaled .3u;
lft z1=(0,.5h);
z2=(.5w,0); x4=x2; rt x3=w;
y4-y2=round(x3-x1); y3=.5h;
draw z1..z2..z3..z4..cycle;
endchar;
GGGGGGGGG
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
GG
GG
GGGGGGG
What we need is to rewrite the code so that y2 and y4 are “correct” for the current pen, and
then y1 will then simply be defined as half of the distance between them. Here is what we
shall do, together with the result that we obtain:
beginchar("O",11.8pt#,12pt#,0pt#);
pickup pencircle scaled .333u;
lft x1=0;
z2= (.5w,good.y 0); x4=x2;
rt x3=w; y4=good.y (y2+x3-x1);
y3=y1=.5[y2,y4];
draw z1..z2..z3..z4..cycle;
endchar;
GGGGG
GG
GG
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
G
GG
GG
GGGGG
```

F.2. The Computer Modern Family of Fonts
Quite a success!
F.2
The Computer Modern Family of Fonts
When Knuth developed TEX, his goal was to be able to typeset his own books. But to do so he
needed a font—nay, an entire family of fonts, with a “typewriter” version (for computer code)
and all the mathematical symbols that he wanted. He needed to find a reasonably neutral
typeface that would be suitable for any type of text, yet one that was also sophisticated enough
to demonstrate the possibilities of the METAFONT language. And, if possible, an American
typeface. After some investigation, Knuth decided to focus on the “legible” typefaces from the
turn of the twentieth century, an in particular on Monotype Modern. He found several designs
of Modern, including one produced by Monotype’s American branch, the typeface Modern 8A.
This is the typeface that he used as a basis for designing what was to become one of the most
widely used typefaces on the planet, at least in the academic world: Computer Modern.
In this section, we shall very quickly present the structure of this family of fonts, which greatly
exceeds in its complexity everything else that has ever been designed in METAFONT, before or
since. To be sure, some people may say that this complexity was somewhat gratuitous and that
Knuth wished to face the challenge of a single program that could generate roman type, italic
type, slanted type, “typewriter” type, sans serif type, calligraphic type—all in every weight and
every optical size. Was it really necessary? Let the reader decide. In any event, as the inseparable companion of TEX, this font family has traveled the world and has even been extended
to other scripts, as we shall see in §F.2.2.
Another peculiarity of this font family is that it is perhaps the only one in the world whose
code has been published in book form. Specifically, the fifth, and last, volume of Knuth’s Computers & Typesetting series is entitled Computer Modern Typefaces. It presents the METAFONT
code for this font family, illustrated and documented. Not surprisingly, that code takes up no
fewer than 588+xvi pages!
But first, a few words about the general structure of Computer Modern.
F.2.1
General Structure
The original distribution of Computer Modern included 128 files, of five types:
• Parameter files: cmr10.mf, cmr12.mf, etc. These files contain the appropriate values of the
parameters for each font variation. Their names indicate the type and optical size of the
font. These are the files that METAFONT reads first.
• Driver files: roman.mf, textit.mf, etc. These are the files that will drive the rest of the
font-generation process. They are invoked by the parameter files, and they in turn invoke
the other required files. There are only eight of them, for the eight font “categories”:
roman, titling, extended ASCII, small capitals, italic, mathematical italic, mathematical
symbols, extensible mathematical symbols.
• Program files: romanu.mf, itall.mf, etc. These contain descriptions of the glyphs, arranged according to their type. For example, there is a file for the lowercase Latin letters,
another for the italics, another for the lowercase Greek letters, another for punctuation,
and so forth.

• A “base” file: cmbase.mf. It contains the definitions of all of the subroutines required to
describe the glyphs. It is the only file that is read by all the fonts; it contains neither glyph
descriptions nor values of parameters but only indispensable chunks of code.
• Test files: 3test.mf, 6test.mf. These files display several styles of the same glyph on the
screen so that the designer can test the effect of his code on several values of the parameters at the same time.
But exactly which fonts does this family contain?
As can be seen in Figures F-1 and F-2, the original distribution, described in [219], contained
75 fonts:
• Roman, cmr, in optical sizes ranging from 5 to 17 points. Size 5 is intended for superscripts
of superscripts, and size 17 is intended for titles. Knuth never was a fan of superlatives,
unlike Caslon and Bodoni; therefore, this family does not contain a size 72 or a size 96.
• Slanted type, cmsl, in 8, 9, 10, and 12 points. “Slanted” type is an invention of Knuth that
serves to distinguish the statement of a theorem, set in slanted type, from mathematical
variables, which are set in italic.
• Extended bold, cmbx, in sizes ranging from 5 to 12 points. This is the default version of
bold; the nonextended version is seldom used. Versions for slanted (cmbxsl) and italic
(cmbxti) also exist, but only in 10 points.
• “Typewriter” type, cmtt, in 8, 9, 10, and 12 points. This font is without a doubt Knuth’s
greatest success; it is infinitely more beautiful than the ubiquitous Courier.
• Four variants of “typewriter” type: slanted (cmsltt), italic (cmitt), small capitals (cmtcsc),
and variable width (cmvtt), only in 10 points.
• “Extended typewriter”, cmtex, in 8, 9, and 10 points. The parameters for these fonts are
the same as for cmtt, but they contain special glyphs: some Greek letters, some mathematical symbols, etc. The number of glyphs per font was limited to 128 at the time, and
the addition of a few new glyphs called for the creation of a new font. These glyphs did,
in fact, exist on the experimental keyboard used by Knuth, a keyboard that the author
was fortunate enough to see before it was sent to the Computer Museum in Boston.
• Sans serif (cmss), in sizes from 8 to 17.
• Slanted sans serif (cmssi), also in sizes from 8 to 17.
• Two variants of weight and width in sans serif type: condensed semi-bold (cmssdc) and
extended bold (cmssbx), in 10 points only.
• A mammoth font called cminch (because the capitals are one inch high) that is in fact
an extended bold sans serif of 72.27 points. This font contains only capitals and digits,
and it is used primarily for the numbers and letters of the chapters in The TEXbook and
The METAFONTbook, which were the inspiration for the chapter numbers and letters in
the book that you are now reading, which was also set with TEX but in the font Le Monde
Livre, by Porchez. The font cminch does not mention its size because that size is fixed.

F.2. The Computer Modern Family of Fonts Figure F-1: The fonts of the original Computer Modern distribution, 1/2.

Figure F-2: The fonts of the original Computer Modern distribution, 2/2.

F.2. The Computer Modern Family of Fonts
• A “Dutch” sans serif font (i.e., one with a very large x-height), “sans serif quotation”
(cmssq), and its italic (cmssqi), used by Knuth for the wonderful quotations that appear
at the end of each chapter of his books. Only in 8 points.
• “Dunhill” (cmdunh), a typeface with capitals and lowercase letters that have very tall ascenders, whose name refers to the logo of the famous brand of cigarettes. Only in 10 points.
• Bold non-extended (cmb), an anemic version of cmbx.
• A “funny” font (cmff, the ‘f’ coming from funny), whose italic version (cmfi) has a positive slope whereas the upright version has a backslant. Only in 10 points.
• An experimental typeface, “Fibonacci”, so called because the values of its parameters
were all derived from the series of numbers devised by this famous mathematician. It is,
of course, a joke, but the result is not necessarily unattractive. In 8 points only, because
10 is not a Fibonacci number, but 8 is. Other permissible sizes: 5, 13, 21, 34 . . .
• Text italic (cmti), in sizes from 7 to 12 points.
• Mathematical italic (cmmi), slightly wider than text italic, and with no kerning pairs (since
in mathematical mode the distances are generated in a different way). In sizes from 5 to
12 points. There is also a bold version of this font (cmmib), in 10 points only.
• “Upright italic” (cmu), which uses the glyphs for the italic letters, but with a zero slope.
Only in 10 points. Not very satisfying.
• Small capitals (cmcsc), in 10 points only.
• Mathematical symbols (cmsy), in sizes from 5 to 10 points. There is also a bold version
(cmbsy), in 10 points only.
• Extensible mathematical symbols (cmex), i.e., the large delimiters, the large operators,
and everything else that either is very large or must be built up from components. In
10 points only.
To generate a font of the Computer Modern family, one need only give the values of its 62 parameters. We have illustrated in Figure F-3 some of the ways in which they are used. Here is
a list of them, in the order in which they appear in the parameter files:
• u: the “base unit”, used primarily to define the widths of the glyphs. The smaller this
parameter is, the narrower the letters will be.
• width_adj: an empirical parameter for “correction” that is added to certain widths.
• serif_fit: the side-bearings of lowercase letters with serifs.
• cap_serif_fit: the side-bearings of capitals with serifs.
• letter_fit: a value that is added systematically to all side-bearings.
• body_height: the height of the parentheses, brackets, and other large symbols.

curve curve vair bar_height body_height cap_height asc_height x_height x_height desc_depth comma_depth notch_cut apex_oo fig_height thin_join stem beak beak_jut cap_bar math_axis dot_size dot_size cap_stem cap_curve cap_band rule_thickness crisp tiny fine flare hair ess cap_ess bar slab serif_drop bracket apex_o o oo vair vair' curve cap_curve cap_hair dish cap_jut jut Figure F-3: The parameters of the Computer Modern fonts.

F.2. The Computer Modern Family of Fonts
• asc_height: the height of the ascenders.
• cap_height: the height of the capitals.
• fig_height: the height of the digits.
• x_height: the height of the lowercase letters.
• math_axis: the height of the mathematical axis of symmetry; that is, the axis relative to
which such symbols as <> ÷ = +−⊕⊗, etc., are centered.
• bar_height: the height of the cross-stroke of the ‘e’. Knuth admits that this parameter
was an excess and recommends that it always be kept between 50 percent and 55 percent
of the x_height.
• comma_depth: the depth of the bottom of the comma.
• desc_depth: the depth of the descenders.
• crisp: the diameter for the rounded ends of serifs. It is zero for roman, but it is clearly
visible for “typewriter type”.
• tiny: the diameter of the rounded ends of the fundamental strokes (such as the downstrokes of sans serif letters, for example).
• fine: the diameter of the more tightly rounded corners, such as that of the terminal of
the sans serif ‘a’.
• thin_join: a very thin stroke thickness, used internally. For example, the thickness of the
beginning of the second downstroke of the roman ‘h’.
• hair: the horizontal thickness of the connecting strokes of the lowercase letters.
• stem: the thickness of the thick upright strokes of the lowercase letters.
• curve: the thickness of the thick curved strokes of the lowercase letters.
• ess: the thickness of the stem of the lowercase ‘s’ at its center of gravity.
• flare: the diameter of the ball terminals of ‘a’ and ‘c’ (that of ‘f’ is .8[stem,flare]).
• dot_size: the diameter of the dot on the ‘i’ and, for that matter, of any dot. In Figure F-3,
we see that the dots on the division sign (÷) are thicker than those of the ‘i’ and the ‘;’,
yet all of these dots use the dot_size parameter. The difference is due to the pen used
to draw and fill the dot: for the former, it is a pen of thickness rule_thickness; for the
latter, it is a pen of thickness fine.
• cap_hair: the horizontal thickness of the connecting strokes of the capitals.
• cap_stem: the thickness of the thick upright strokes of the capitals.
• cap_curve: the thickness of the thick curved strokes of the capitals.

• cap_ess: the thickness of the stem of the capital ‘s’ at its center of gravity.
• rule_thickness: the thickness of the strokes of the “geometrical” symbols, such as the
mathematical symbols ‘<’, ‘>’, ‘÷’, ‘=’, ‘+’, ‘−’, ‘⊕’, ‘⊗’, etc.
• dish: the height of the arch in the serifs.
• bracket: the height of the serif’s bracket, which is to say the distance between the height
of the point at which we leave the letter’s stem and the height of the serif’s bar.
• jut: the width of the serif of a lowercase letter (measured from the edge of the letter’s stem).
• cap_jut: like jut, but for the capitals.
• beak_jut: for slanted serifs, such as the one on the upper arm of the ‘F’, the horizontal
projection of the slanted part.
• beak: the height of a slanted serif, measured from the internal boundary of the cross
stroke.
• vair: the vertical thickness of the connecting strokes of the lowercase letters.
• notch_cut: the vertical distance between the inner and outer points of the ‘v’.
• bar: the thickness of the crossbar of the ‘f’.
• slab: the thickness of the serifs.
• cap_bar: the thickness of the crossbars of the letters ‘E’, ‘F’, ‘G’, and ‘H’.
• cap_band: likewise, but for the letters ‘A’, ‘B’, ‘D’, ‘P’, and ‘R’. In most cases, cap_bar is
equal to cap_band.
• cap_notch_cut: the vertical distance between the inner and outer points of the ‘V’.
• serif_drop: the obliqueness of the upper half-serifs of the letters ‘b’, ‘d’, ‘h’, ‘i’, ‘j’, ‘k’, ‘l’,
‘m’, ‘n’, ‘p’, ‘r’, and ‘u’.
• stem_corr: a parameter for correcting stem. By subtracting this parameter from stem, we
obtain stem′; likewise for cap_stem′.
• vair_corr: a parameter for correcting vair. By adding the two, we obtain vair′.
• apex_corr: a parameter for correcting apex, used, for example, for the apex of the ‘A’.
• o: the overshoot of the round strokes of the capital letters. From o we calculate oo, the
overshoot of the round strokes of the lowercase letters.
• apex_o: the overshoot of the apexes of the capital letters. From apex_o we calculate
apex_oo, the overshoot of the apexes of the lowercase letters.
• slant: the slant.

F.2. The Computer Modern Family of Fonts
• fudge: a multiplicative factor for correcting thicknesses, used, for example, for the ‘v’ in
the “typewriter” fonts.
• math_spread: the distance between the bars of the equal sign at small point sizes.
• superness: the curvature of the round letters. It is this parameter that enables us to distinguish the letter ‘O’ from the zero ‘0’ in the “typewriter” font.
• superpull: the thinning of the strokes of the round letters.
• beak_darkness: the coefficient for filling the serifs: nonzero for roman, zero for “typewriter”.
• ligs: a whole number that indicates the number of ligatures to include in the font.
• square_dots: a boolean value that indicates whether the dots are round (roman) or
square (sans serif).
• hefty: a boolean value that indicates whether we want to lighten the strokes or not.
• serifs: a boolean value that indicates whether want to have serifs or not.
• monospace: a boolean value that indicates whether the font is monospace or not.
• variant_g: a boolean value that indicates whether the ‘g’ is of the roman (‘g’) or italic (‘g’)
variety.
• low_asterisk: a boolean value that indicates whether the asterisk is low (the mathematical symbol ‘∗’) or high (the editorial symbol ‘*’).
• math_fitting: a boolean value that indicates whether or not we want spacing that has
been customized for the mathematical mode.
To those, of course, are added the name of the font, its optical size, its metric parameters (see
§B.1.2), and the choice of driver file.
In 1986, John Sauter [311] developed an extended version of the Computer Modern parameter
files; people began to refer to the “Sauterized” versions of the fonts. In Sauter’s version, the
fonts can be generated at any optical size. If we request an optical size that already exists
in Knuth’s original distribution, we obtain exactly the same font. If, however, we request a
different size, the original values are interpolated so as to generate the font on the fly. Generating fonts in this way could not be easier. Suppose that we wish to obtain the font cmitt
at 17.28 points. We create a file cmitt1728.mf that contains only one line of code:
design_size:=17.28; input b-cmitt

```text
F.2.2
Extensions
From the beginning, Knuth invited the friends of TEX and METAFONT to extend Computer
Modern to other languages and other alphabets. Extensions were not long in coming.
Starting in 1981 [236], Hermann Zapf designed mathematical fonts for the American Mathematical Society; they are implemented in his AMSTEX package. These fonts are programmed
in METAFONT78, and the code has never been made public. In 1985 [67, 68], the AMS supplemented these fonts with additional mathematical symbols and some Cyrillic fonts. Only
in 1995 were the fonts rewritten in METAFONT82, improved, and publicly released as METAFONT source code [31].
In 1988, Silvio Levy [238] developed a Greek version (in the hapla style) of Computer Modern:
 


!"#\$
%&
'()*+,-./01
Unfortunately, the parameters work only for roman; there are neither italic nor sans serif
nor “typewriter” fonts. In 1989, the author and his friend Klaus Thull [172] (known by the
pseudonym Mahilata Shamaya) added small capitals and the glyphs needed for Greek numeration.
In 1989, in an article in the journal TUGboat [174], Doug Henderson explained how to obtain
Computer Modern fonts as contours.
In 1990, at the meeting of the TEX Users Group in Cork, Ireland, a new font encoding, called
the “Cork encoding” (or T1), was adopted. This encoding, which is a mixture of ISO 88591 and 8859-2, was quickly implemented by Norbert Schwarz and Jörg Knappen [212, 213],
in the DC font family. Most of the glyphs are combinations of glyphs from Computer Modern
(letters and accents, etc.), but a few new glyphs were also designed: the thorn, the edh, etc.
Finally, in 1997, Jörg Knappen [214] renamed this font family EC.
In 1991, Dean Guenther and Janene Winter, of Washington State University, developed a
LaTEX package for typesetting the International Phonetic Alphabet [153, 286]. Unfortunately,
the METAFONT code is of poor quality. The situation was corrected in 1996 when Fukui Rei
[302] issued his own system, of excellent quality, for typesetting in the International Phonetic
Alphabet.
In that same year, 1991, Mícheál Ó Searcóid [315] designed a Gaelic Computer Modern
font, EIAD:
 

 !"#\$%&'()*+,-./01234
In 1993, Jörg Knappen [211] developed an extension of Computer Modern for the African languages that use the Latin alphabet and for certain languages not supported by DC: Maltese,
Esperanto, etc. These fonts are called FC.
In 1996, at the TEX Users Group meeting in Moscow, Olga Lapko [227] presented a new family of Computer Modern Cyrillic fonts that were of higher quality than those of the AMS and
that contained enough glyphs for all of the languages, including the Asian ones, that use the
Cyrillic alphabet. These fonts are called LH:
 





 
#
\$
```

F.3. MetaFog 



```text
-./0123456789
:;<=>?@ABCD
EFG
In 1998, Walter Schmidt [314] noticed that the sans serif font of Computer Modern was used
mainly as a supplementary typeface for roman but was ill suited for use on its own. He released CM Bright, a lighter sans serif font that is appropriate for running text:
 


 !"#\$%&'()*+,-./01234
Starting in 2000, Hàn Th© Thành [328, 327] designed Computer Modern fonts for Vietnamese,
the VN fonts.
In 2001, Alan Hoenig [181] tried to adapt the parameters of Computer Modern to Monotype
Modern. The result, called Modernized Modern, is very interesting:
 



!"#\$%&'()*
+,-./01234
F.3
MetaFog
Over the past 20 years, there have been several attempts to produce PostScript or TrueType
fonts from METAFONT code, the first of them doubtless being that of Shimon Yanai and
Daniel Berry [355], who developed a program called mf2ps that converted METAFONT surfaces into PostScript Type 1 contours. The code for this software (which is in fact a changefile for METAFONT—i.e., a file for adding Pascal code to METAFONT and modifying that
code) can be found on the CTAN servers (http://www.ctan.org), but it is difficult to compile
today, as it depends on a library of subroutines peculiar to Sun that dates from the years
1990 to 1991.
Richard Kinch, in his TrueTEX system [210], offered a program (for Windows only) called MetaFog [209] that converts METAFONT code into TrueType contours.
The process is quite complex:
1. We begin by compiling the METAFONT sources with METAPOST (!). The latter produces
a file for each glyph in the font. We assemble the glyphs into a ZIP archive.
2. We launch MetaFog on those glyphs through the use of an AWK script. MetaFog produces
two types of glyph-description files: reduced ones (those that have valid contours) and
nonreduced ones (in which the contours of the different METAFONT pen strokes have not
been merged). It is the filename that differs: for example, _065.eps is a reduced file, and
_065u.eps is a nonreduced file.
3. We open the nonreduced files in the program weed (Figure F-4). This program is a type
of glyph editor in which we can do only one thing: separate the Bézier curves that will
be part of the glyph’s contour from those that will not. We do so by clicking on them. It
is quite entertaining to see the glyph take its shape amidst a heap of useless curves.
```

Figure F-4: The window of weed, where we see the METAFONT glyph that we designed in §F.1.3. 4. Finally, one last script collects the files produced by weed into a TTF font. MetaFog includes quite a few “administrative” scripts: those that calculate the metrics, manage the encoding, etc. Richard Kinch used MetaFog to produce the Computer Modern TrueType fonts that accompany TrueTEX. The result is excellent. In fact, Kinch was the only one to do serious work on the mathematical calculation of the curves that envelop the METAFONT strokes. He gives an overview of his calculations in [209]. The tragedy is that these calculations, with which we could have created splendid fonts, remain prisoner to MetaFog, a program that does indeed do an admirable job of “vectorizing” METAFONT code but that is in general of such abominably complex structure that it would give any programmer nightmares—and that is, alas, inaccessible to nonprogrammers. We can only hope that Richard will manage in the coming years to convert this chaotic set of

```text
F.4. METATYPE1 and Antykwa Półtawskiego
scripts into a true software package; that will be a great breakthrough for the TEX/METAFONT
community and a wonderful tool for all font designers.
The reader who is eager to encourage Richard to work towards this goal can send him email
at kinch@truetex.com.
F.4
METATYPE1 and Antykwa Półtawskiego
In 1999, three Poles—Bogusław Jackowski, Janusz Nowacki, and Piotr Strzelczyk—shocked
the TEX world by issuing a new family of fonts, Antykwa Półtawskiego (see §F.4.3), completely
programmed in METATYPE1 [198].
In this section, we shall discuss the tool METATYPE1. By developing the tool together with
the fonts produced by it, as Knuth had done with METAFONT and the Computer Modern fonts,
the three Poles showed that the tool is of genuine practical interest. Let us also mention that
in 2003 [197], Bogusław Jackowski and Janusz Nowacki produced Computer Modern fonts with
METATYPE1, but not simply by rereading the METAFONT code; in fact, they started with
PostScript Type 1 fonts and converted them to METATYPE1 code. Next, they cleaned the
code up and fitted it with accents for the Latin languages. This is an interesting application of
METATYPE1, even though it does not allow us to produced arbitrary Computer Modern fonts.
F.4.1
Installing and Using METATYPE1
While METAFONT does not require any installation, since it has been included in every TEX
distribution since the 1980s, things are different for METATYPE1. What is METATYPE1, technically speaking?
It is a set of tools, the most important of which is METAPOST, a program derived from METAFONT, also written by Knuth’s student John Hobby, that produces graphics in Encapsulated
PostScript [179]. Jackowski and his colleagues wrote special routines in the METAPOST language to generate fonts and also wrote a postprocessor in the AWK language (the ancestor
of Perl).
To install METATYPE1, one must have METAPOST, which, fortunately, is included in most
TEX distributions, as well as gawk (the GNU implementation of AWK). One also needs the
t1utils (which were described on page 233; see also [175]) to convert from PFB to humanreadable PostScript code and vice versa. To create PFM files (which are required if we wish to
use the PostScript fonts under Windows), we also need Perl. Finally, to obtain the documentation, we also need the tool mft, which is a pretty-printer for METAFONT and METAPOST code.
To install METATYPE1 under Windows, one downloads the installation from ftp://bop.
eps.gda.pl/pub/metatype1/ and places the scripts (files with the extension .bat) into a directory listed in the PATH.
Under Unix or Mac OS X, installation is similar. The files can be downloaded from CTAN
(http://www.ctan.org/tex-archive/systems/unix/mtype13); they were ported to Unix by
Włodzimierz (Włodek) Bzyl. The scripts have slightly different names (without the 1 and the
.bat extension). They must be placed somewhere where the system can find them when it
looks for an executable file.
```

Whether under Windows or Unix, the files with the extension .mp (which are files of METAPOST code), including the one that appears in extra, must be placed in a directory accessible
to METAPOST. Do not forget to rebuild the TEX file-finding base by running mktexlsr or by
performing the corresponding operation in the current TEX distribution.
Once the scripts have been installed, one must open mt1set.bat (or mt1set under Unix) in a text
editor and modify the value of the environment variable METATYPE1. This is the absolute path of
the directory that contains the METATYPE1 scripts.
Another detail: The Poles use a special version TEX called mex. Some TEX distributions contain it,
but not all. In the script mkfont1.bat (or mkfont), it is mex that is invoked. If you do not have it
available, replace the line:
mex \$FNAME.tex
with:
tex "&plain \$FNAME.tex"
METATYPE1 offers three scripts (written in the AWK language) to the user:
• mt1set.bat (or mt1set under Unix), a script that initializes the environment variable
METATYPE1; it must be launched at the start of the session.
• mkfont1.bat (or mkfont under Unix), takes as its argument the name of a file of font
parameters. This name must contain the extension .mp. It is the system’s main script; it
will launch METAPOST as well as the AWK scripts and the required t1utils binaries.
• mkproof.bat (or mkproof under Unix), a script that launches the pretty-printer mft
and a number of other utilities to produce an attractively presented version of METAPOST code.
To use METATYPE1, we change to the directory containing the font files to be processed—let
us call it bar.mp—and run the script mkfont1.bat (or mkfont under Unix):
mkfont1.bat bar
Warning: Do not write the extension .mp of the METAPOST file! METATYPE1 then does the
rest, and in a few moments we find ourselves with a PFB font.
F.4.2
Syntactic Differences from METAFONT
The authors of METATYPE1 did everything they could to smooth out the syntactic differences
between METAFONT and METAPOST; nonetheless, there remain some major differences due
to the PostScript Type 1 output format, which has needs other than those of the GF bitmap
fonts traditionally produced by METAFONT.
We shall illustrate these differences by translating the code for our pseudo-Vendôme sample
letter ‘n’ into METATYPE1.
First of all, we need a special package of macros, called fontbase.mp. Thus we begin our
code with:

```text
F.4. METATYPE1 and Antykwa Półtawskiego
input fontbase;
Next, we need to define the unit u that we have used so much for describing distances. In
METAFONT we would have first defined a “true unit” u# of one American printer’s point;
then we would have converted it into pixels to obtain u. Here we give the value of u directly
in PostScript font units:
u:=100;
A PostScript Type 1 font needs some metadata. These are supplied by macros whose names
begin with pf_:
pf_info_familyname "Pseudo-Vendome";
pf_info_fontname "Pseudo-Vendome-Regular";
pf_info_weight "Normal";
pf_info_version "1";
pf_info_capheight 7u;
pf_info_xheight 5.1u;
pf_info_space 3u;
pf_info_author "Yannis Haralambous, for 'Fonts & Encodings'";
pf_info_encoding "AdobeStandard";
pf_info_creationdate;
The last of these, pf_info_creationdate, may be given with no argument. In that case, the
data given to the font will be the date and hour of compilation.
Having given these global data, we can now begin the font:
beginfont;
One peculiarity that stems from a choice made by Jackowski and his colleagues: there is
no longer a beginchar macro that gives both the code for the glyph and its abstract dimensions. We use several types of macros:
wd.n=7u;
ht.n=6u;
dp.n=0u;
encode("n")(110);
introduce "n"(utilize)(0);
In the code above, we first see that the dimensions of the box containing the glyph have been
dissociated from the glyph’s description. Thus we can place these dimensions in another file;
they will become, in a sense, the font’s metric parameters.
The encode command produces the PostScript font encoding—a problem that did not exist
under METAFONT, where it was sufficient for each glyph to have a position in the table (i.e., a
number between 0 and 255). The encode command takes two arguments: the PostScript name
of the glyph and the glyph’s position in the font encoding.
The introduce command is quite peculiar. It takes four arguments:
```

```text
1. The glyph’s name.
2. A string that may be either utilize or store, or both: utilize+store. “Utilize” means
to create a glyph in the font; “store” means to create a global path variable glyph.name,
where name is the glyph’s name—a path that will be used in other glyphs. In this way, the
glyph for the comma, for example, can be used to produce the apostrophe, the English
and German quotation marks, etc.
3. A number 0 or 1. If 1, the glyph in question is slanted when the font is oblique; if 0,
the glyph remains unchanged, irrespective of the slant. For example, the mathematical
symbols ‘+’, ‘⊕’, ‘⊗’, ‘÷’, etc., are never slanted.
4. A string that is in fact the name of the future EPS file, which is used when we create a file
of documentation for the font. The EPS file is supposed to contain a bitmap image that
can be compared with the vector contour. Thus if we wish to simulate a typeface from
scans, we can directly compare the scans and the contours, using FontLab masks.
As a result, beginglyph takes only one argument, the name of the glyph:
beginglyph("n");
The first task is to initialize the variables that correspond to the abstract dimensions of the
glyph, something that METAFONT would do automatically:
w:=wd.n; h:=ht.n; d:=dp.n;
Now we are ready to write the code for the glyph’s description.
The first peculiarity of METATYPE1: we do not use pens. As Richard Kinch said [209, p. 236],
“Algebra tells us that stroking a 3rd degree polynomial curve (the ellipse approximated by
Bézier curves) along a 3rd degree polynomial curve (the Bézier curve of the stroked path)
results in a 6th degree envelope curve.” Neither METAFONT nor METAPOST knows how to
solve polynomials of this kind; we have to abandon pens and restrict ourselves to filling operations.
Fortunately, we can still use the pen strokes of METAFONT, which, in fact, are nothing but
filling operations that give us the illusion of working with pens. And in any event, we used
nothing but pen strokes in our example of the letter ‘n’. Thus this specific sample of code
should be compatible with METATYPE1. Indeed, we can make a first attempt by taking the
glyph’s METAFONT code as it stands, with no changes. Result: there are no syntax errors, but
some parts of the glyph do not appear! Why?
Because we have run into another serious constraint: the filling operations that we do must
never have tangent points. Let us explain. It often happens that our pen strokes intersect. But a
glyph in a PostScript Type 1 font is a contour with no intersections. Thus we must merge the
contours for the different pen strokes. To do so, we must find the points at which the curves
intersect. But that is possible only if we are working with isolated points. If two contours share
part of a Bézier curve, or if their intersection is in fact a point at which the two curves touch,
it is impossible to merge them.
```

```text
F.4. METATYPE1 and Antykwa Półtawskiego
If the mountain will not come to Mohammed, Mohammed must go to the mountain. In
other words, since we cannot force METATYPE1 to merge our pen strokes properly, we have
to write them in such a way that they will not come into contact.
Let us examine our glyph as we divided it up in order to write the METAFONT code:
1l
1r
3l
3r
2l
2r
4l
4r
5l
5r
6l
6r
7l
7r
8l
8r
9l
9r
10l
10r
11l
11r
12l
12r
13l
13r
14l
14r
There are three spots that cause a problem; we have drawn them with a heavy line:
1l
1r
3l
3r
2l
2r
4l
4r
5l
5r
6l
6r
7l
7r
11l
11r
12l
12r
13l
13r
14l
14r
In the case of z2--z2r (left), the problem is that this stroke is common to the curve z2l--
z2r..z4l{down} at pen position z2 of the stroke z1e{right}..z2e. Thus the two contours
are identical there. One possible solution is to replace the pen stroke with a filling operation:
1l
1r
3l
3r
2l
2r
Thus we must find a point on the path z1r{right}..z2r that is quite close to z2 and then
draw the part of the path between z1r and our point, and between our point and z2. Then
there will be no more problem with paths that coincide.
```

To find this “nameless” point, we shall use the subpath command of METAFONT (and of
METAPOST), which gives us a subpath from a given path. Here, then, is how we write the
path that is shown with a heavy line:
fill subpath(0,0.9) of (z1r{right}..z2r)--z2--z2l..
z1l{left}--cycle;
Explanation: subpath (a command present in METAFONT) takes four arguments: the “times”
of departure and arrival, the keyword of, and the original path. By “time” we mean the parameter for the path’s development, which begins at 0 and takes whole values for each Bézier
curve on the path. Here we have only one Bézier curve; thus the point at time 0 on the path
is z1r and the point at time 1 is z2r. By choosing a time of arrival of 0.9, we come quite close
to the right edge of the downstroke without actually reaching it.
The two other problematic cases are the feet of the downstrokes. The curve for the serif
z5r..z6r{right}..z7r is tangent to pen position z4r--z4l; the same goes for position z11r-
-z11l on the other serif. Here the solution is much easier: we merely move the pen positions
up slightly, making sure that they still remain within the area of the serifs. Since the parameter serif_ht can take on very small values, it behooves us to define the height of z4 and z11
with respect to that parameter. In addition, we must not forget delta, which gives us the
height of the serif’s arch. Here is a possible solution:
y4=delta+.25serif_ht; y11=delta+.25serif_ht;
4l
4r
5l
5r
6l
6r
7l
7r
11l
11r
12l
12r
13l
13r
14l
14r
Now let us continue with the syntactic differences between the languages. Under METAFONT,
one merely writes penstroke to draw the pen stroke. Under METATYPE1, one does not draw
the strokes directly; one keeps all the pen strokes in memory in order to merge them at the
end and fill the global contour. Thus we create a table stroke[] of paths and fill in its elements one by one.
Here is the glyph’s code at the point that we have reached:
save stroke_; path stroke_[];
numeric x_height, oo, stem, join, serif_tip, serif_ht, delta, offset;
x_height=5.1u; oo=.2u; stem=1.1u; join=.2u;
serif_tip=.2u; serif_ht=.7u; delta=.033u; offset=.125u;
z4=(1.6u,.5serif_ht); penpos4(stem,180);
x3=x4+offset; y3r=x_height;
x3l-x3r=stem; y3l-y3r=.5serif_tip; z3=.5[z3l,z3r];
stroke_2:=penstroke z3e..{down}z4e;

```text
F.4. METATYPE1 and Antykwa Półtawskiego
x11=w-.65u; y11=y4; penpos11(stem,180);
y10=y8=.7x_height; z8=whatever[z3,z4];
z10-z11=whatever*(z3-z4);
z10l-z10r=z3l-z3r; z10=.5[z10l,z10r];
penpos9(.87[join,stem],-); y9l=x_height+oo; x9=.68[x8,x10];
z8'=whatever[z11,z10]; y8'=1.25x_height;
penpos8(join,angle(z8'-z8)-);
stroke_3:=penstroke z8e{z8'-z8}..tension 1.5..z9e{right}..z10e---z11e;
numeric serif; serif=x11r-x12=1u;
x7-x4l=serif; x3r-x1=.95serif; x4r-x5=.9serif; x14-x11l=.8serif;
y1l=y3l; penpos1(serif_tip,-); z2=z3l;
penpos2(1.25serif_ht,angle(direction 0 of (z3l..{down}z4l))+eps);
stroke_4:=subpath(0,0.9) of (z1r{right}..z2r) -- z2 -- z2l..z1l{left}--cycle;
if (x7-x4+.2u+x11-x12 > x11-x4):
x7:=.5[x4,x11]-.1u;
x12:=.5[x4,x11]+.1u; fi
penpos5(serif_tip,-); penpos7(serif_tip,-);
penpos12(serif_tip,-); penpos14(serif_tip,-);
penpos6(serif_ht,-); penpos13(serif_ht,-);
y5r=y7r=y12r=y14r=0; z6r=(x4,delta); z13r=(x11,delta);
stroke_5:=penstroke z5e{right}..z6e & z6e..{right}z7e;
stroke_6:=penstroke z12e{right}..z13e & z13e..{right}z14e;
In this code, we have defined five pen strokes (with indices from 2 to 6). We have omitted
index 1 for a reason: the command find_outlines, which merges the contours, and which
we shall employ later, uses index 1 to store the result of the merger of the contours.
Now we shall gradually merge the contours:
find_outlines(stroke_4, stroke_2)(stroke_);
find_outlines(stroke_1, stroke_3)(stroke_);
find_outlines(stroke_1, stroke_5)(stroke_);
find_outlines(stroke_1, stroke_6)(stroke_);
Now the contour for the entire glyph is stored in stroke_1. The command that actually draws
the contour is:
Fill stroke_1;
The ‘F’ in Fill is capitalized to distinguish the command from the fill command of METAFONT.
```

```text
If our glyph had counters, we would use the unFill command to write a contour in the opposite direction, inside the first contour, which would produce the required “holes”.
At this stage we are not yet finished; we still have to specify the set-width of the PostScript
glyph and terminate the description of the glyph and the font:
fix_hsbw(w,0,0);
endglyph;
endfont.
The command fix_hsbw takes three arguments: the set-width of the glyph and the sidebearings. The latter will form the abstract box that contains the glyph.
Ordinarily we include here the definitions of any hints. Thus we write:
fix_vstem(foo)(stroke_1);
fix_hstem(bar)(stroke_1);
for a horizontal stem of thickness foo or a vertical stem of thickness bar. But there are no
vertical or horizontal stems in our example (because the two downstrokes of the letter ‘n’ are
slightly slanted); thus it is not possible to define hints for this particular case.
And here is the result:
The PostScript image above was produced by the documentation module of METATYPE1.
Here, in its entirety, is the code, pretty-printed by mft, that enabled us to obtain the font
containing this single glyph:
input fontbase;
u := 100;
pf_info_familyname"Pseudo−Vendome";
pf_info_fontname"Pseudo−Vendome−Regular";
pf_info_weight"Normal";
pf_info_version"1";
pf_info_capheight7u;
pf_info_xheight5.1u;
```

```text
F.4. METATYPE1 and Antykwa Półtawskiego
pf_info_space3u;
pf_info_author"Y. Haralambous for ’Fonts & encodings’";
pf_info_encoding"AdobeStandard";
pf_info_creationdate;
beginfont
wd_n = 7u; ht_n = 6u; dp_n = 0u;
encode("n")(ASCII "n");
introduce"n"(utilize)(0)();
beginglyph("n");
w := wd_n; h := ht_n; d := dp_n;
save stroke_; path stroke_[];
numeric x_height, oo, stem, join, serif_tip, serif_height, delta, offset;
x_height = 5.1u; oo = .2u; stem = 1.1u; join = .2u;
serif_tip = .2u; serif_height = .7u; delta = .033u; offset = .125u;
z4 = (1.6u, .5serif_height); penpos4(stem, 180);
x3 = x4 +offset; y3r = x_height;
x3l −x3r = stem; y3l −y3r = .5serif_tip; z3 = .5[z3l, z3r];
stroke_2 := penstroke z3e . . {down}z4e;
x11 = w−1.65u; y11 = y4; penpos11(stem, 180);
y10 = y8 = .7x_height; z8 = whatever[z3, z4];
z10 −z11 = whatever ∗(z3 −z4);
z10l −z10r = z3l −z3r; z10 = .5[z10l, z10r];
penpos9(.87[join, stem], −136); y9l = x_height +oo; x9 = .68[x8, x10];
z8′ = whatever[z11, z10]; y8′ = 1.25x_height;
penpos8(join, angle(z8′ −z8)−90);
stroke_3 := penstroke z8e{z8′ −z8} . . tension 1.5 . . z9e{right} . . z10e - - - z11e;
numeric serif; serif = x11r −x12 = 1u;
x7 −x4l = serif; x3r −x1 = .95serif ; x4r −x5 = .9serif ; x14 −x11l = .8serif ;
y1l = y3l; penpos1(serif_tip, −90); z2 = z3l;
penpos2(1.25serif_height, angle(direction 0 of (z3l . . {down}z4l))+eps);
stroke_4 := subpath(0, 0.9) of (z1r{right} . . z2r) - - z2 - - z2l . . z1l{left} - - cycle;
if (x7 −x4 +.2u+x11 −x12 > x11 −x4):
x7 := .5[x4, x11]−.1u;
x12 := .5[x4, x11]+.1u; fi
penpos5(serif_tip, −90); penpos7(serif_tip, −90);
penpos12(serif_tip, −90); penpos14(serif_tip, −90);
penpos6(serif_height, −90); penpos13(serif_height, −90);
y5r = y7r = y12r = y14r = 0; z6r = (x4, delta); z13r = (x11, delta);
stroke_5 := penstroke z5e{right} . . z6e &z6e . . {right}z7e;
stroke_6 := penstroke z12e{right} . . z13e &z13e . . {right}z14e;
find_outlines(stroke_4, stroke_2)(stroke_);
```

Figure F-5: The fonts of the Antykwa Półtawskiego distribution, v.0.52.
find_outlines(stroke_1, stroke_3)(stroke_);
find_outlines(stroke_1, stroke_5)(stroke_);
find_outlines(stroke_1, stroke_6)(stroke_);
Fillstroke_1;
fix_hsbw(w, 0, 0);
endglyph;
endfont
F.4.3
Antykwa Półtawskiego
The Antykwa Półtawskiego font family is based on a Polish typeface designed in the 1920s by
a great Polish typographer, Adam Półtawski (1881–1952). According to Nowacki [281], this
typeface was used in almost half of all works printed in Poland before the era of phototypesetting and the computer. We have shown all the optical sizes and styles of this typeface in
Figure F-5.
Technically, this font is organized in a simpler and perhaps more rational way than Computer
Modern. There are five types of files:
• Driver files (extension .mp). These are the files that we invoke. Their names are those of
the fonts that they generate: antpr (roman), antpi (italic), antpb (bold), and antpbi (bold
italic), at 6, 8, 10, 12, and 17 points. They contain calls to the other required files.

F.4. METATYPE1 and Antykwa Półtawskiego
• Parameter files (extension .par). These have the same names as the driver files and contain the specific values of the parameters for each font, including all the set-widths and
the encode and introduce commands for all the glyphs. There are also a file antp.par of
global parameters and a file ap_names.mp containing the PostScript names of the glyphs.
• Files of general METAPOST subroutines. There is only one: ap_lego.mp, its name being
inspired by the Lego brand of toys, since the code for the glyphs in Antykwa Półtawskiego
is based on the principle of building blocks.
• Glyph-description files, which contain the METAPOST code for the capital letters, the
lowercase letters, the digits, the mathematical symbols, the Greek letters, etc.
• Files of kerning pairs. There is only one: antp.lkp.
All of these are amply documented; we merely run the script mkproof1.bat (or mkproof under
Unix) to produce the TEX file of documentation. This documentation even contains the EPS
images of the glyphs; after all, METAPOST creates PostScript code, so we may as well take
advantage of it to produce the automatically generated documentation.
In Figure F-6, we have shown the main parameters for the glyphs in the Antykwa Półtawskiego
font family. Here they are:
• beak_gap: the offset between the outer two arms of the ‘E’.
• beak_ht: the height of the serif on an upper or lower arm (on the letters ‘E’, ‘F’, etc.).
• beak_wd: the filling width of the serif on an upper or lower arm (on the letters ‘E’, ‘F’, etc.).
• depth_ogonek: the depth of the ogonek.
• depth: the depth of the descenders (the letters ‘g’, ‘p’, ‘y’, etc.).
• dot_size: the theoretical diameter of the dots (“theoretical” because the dots are in fact
either hexagons or octagons).
• equal_shift: the distance between the axis of symmetry and the middle of a stroke of
the equals sign.
• horn_ht: the height of the serif on the middle bar of the ‘E’.
• horn_wd: the width for filling the serif on the middle bar of the ‘E’.
• hstem_ogonek: the maximum vertical thickness of the ogonek.
• lc_crook_ht: the height of the serif on the upper terminal of the ‘c’.
• lc_crook_shift: the offset of the serif on the upper terminal of the ‘c’.
• lc_height: the height of the lowercase letters.
• lc_overshoot: the overshoot of the round strokes of the lowercase letters.
• lc_serif_jut: the width of the serifs of the lowercase letters.

math_axis
math_stem
equal_shift
ligne de base
ligne de base
beak_wd
beak_gap
horn_wd
horn_ht
beak_ht
lc_height
depth
slang
lc_overshoot
uc_overshoot
lc_stem'
uc_stem'
num_height
uc_crook_ht
uc_crook_shift
lc_crook_shift
lc_crook_ht
lc_stem
depth_ogonek
uc_stem
thin_stem
uc_height
dot_size
underline_pos
marg
hstem_ogonek
vstem_ogonek
depth_ogonek
serif_slab
spread_wd
spread_ht
lc_serif_jut
uc_serif_jut
Figure F-6: The parameters of the Antykwa Półtawskiego font family.
• lc_stem': the thickness of the thick curved strokes of the lowercase letters.
• lc_stem: the thickness of the thick upright strokes of the lowercase letters.
• marg: the standard side-bearings of the glyphs.
• math_axis: the height of the horizontal axis of symmetry of the mathematical symbols.
• math_stem: the stroke thickness of the “geometrical” mathematical symbols.
• num_height: the height of the digits.
• serif_slab: the thickness of the serifs.
• slang: the angle of the italic glyphs (N.B.: this is λ in METAFONT, but here it is the angle
φ = tan(λ)).

F.4. METATYPE1 and Antykwa Półtawskiego
• spread_ht: the height of the point at which the vertical stem begins to reach a serif.
• spread_wd: the width of the vertical stems.
• thin_stem: the width of the connecting strokes.
• uc_crook_ht: the height of the serif on the terminal of the ‘C’.
• uc_crook_shift: the offset of the serif on the terminal of the ‘C’.
• uc_height: the height of the capitals.
• uc_overshoot: the overshoot of the round strokes of the capitals.
• uc_serif_jut: the width of the serifs of the capitals.
• uc_stem': the thickness of the thick curved strokes of the capitals.
• uc_stem: the thickness of the thick upright strokes of the capitals.
• underline_pos: the depth of the underscore. There are no underscored letters in the font,
but this information is part of the standard font dictionary of PostScript Type 1 fonts.
• vstem_ogonek: the maximum horizontal thickness of the ogonek.
The development of the Antykwa Półtawskiego font family continues, and future years will
certainly add other styles and glyphs to the ones that we have today.

```text
G
Bézier Curves
G.1
History
We can hardly imagine the connection between the splendid curves of a font like Monotype
Garamond and the hood of a Renault. Yet both consist of curves, and in both cases the production process (whether the final product be a Type 1 font or a piece of metal) went through
a phase of computer-assisted design.
But how were car bodies designed before the computer era? Engineers made models out of
wood or plaster and approached the desired result through successive approximations. Developing one model after another was neither rapid nor efficient. Pierre Bézier (1910–1999),
an engineer at Renault since 1933, started doing research on computer science in 1960 to find
a system for modeling curves, or even surfaces, that would be easy to compute and also easy
for the human to manipulate.
The curves that bear his name satisfy these conditions. But he was not the only one to work
on these techniques. There were also Paul de Casteljau, an engineer at Citroën, and Birkhoff,
Garabedian, and de Boor, at General Motors, in the United States. Bézier’s work gave us
the curves, which today are known around the world because they are at the heart of every
computer-assisted design system; de Casteljau’s work gave us the algorithm that we shall see
below; Boor and his colleagues worked on B-splines (‘B’ as in “Bézier”), a more refined version
of Bézier curves.
In the text that follows, we shall present the main properties of the Bézier curves. This text
was inspired primarily by [246].
G.2
Bézier Curves
To draw a straight line with graphic-design software, it is usually sufficient to click once
with the mouse to select the starting point and once again to select the ending point.
```

```text
These two points define the line segment perfectly: it is a linear function—i.e., a first-degree
polynomial—and is therefore defined by two points.
We would like to be able to do the same thing with curves: click to obtain the starting point
and the ending point, and then use an intuitive means, accessible even to those with the most
severe case of technophobia, to modify the curve and obtain the precise curve that we want
from the infinite range of curves that can be drawn between two points.
That is precisely what Bézier curves do: they are third-degree polynomials and are therefore
defined by four points. We already have two of those points: the starting point and the ending
point; we need only define the two that remain. We call those two points the control points.
In most software packages like Illustrator and CorelDraw, we click once to obtain the starting
point, then drag the mouse to obtain the first control point, release the mouse button, move,
click again to obtain the ending point, and drag the mouse again to obtain the second control
point. How do we know where to place the last of these? Well, as soon as we have indicated
the ending point, the software begins to draw a Bézier curve, which changes dynamically as
we drag the mouse to set the second control point. Thus we watch the curve develop, and we
stop as soon as it is optimal.
Later we can come back and change the location of the first control point. By playing with
the two control points, we almost always manage to find the desired curve, whether it be a
new curve that we have just created and that evaluate according to our aesthetic criteria or a
curve that must be as close as possible to a model that we see behind the screen.
Drawing Bézier curves in this way is so intuitive and efficient that it has become second nature
to graphic artists and industrial designers. And no one wonders anymore how the computer
can be so powerful—and especially how it could have been so powerful in the late 1980s,
when Adobe Illustrator v.1 came out—to display a mathematical curve, a third-degree polynomial, that changes, moves, and leaps about in real time while following the hand of the
designer. Does the computer solve a third-degree equation every millisecond? It would not
be able to do so!
What happens, then? What mystery lies hidden behind these polynomials that makes them
so easy to represent graphically on a computer, even the clunkiest one? Let us push the envelope farther: just as Hercules always found himself faced with two new heads whenever he cut
a head offthe Hydra at Lerna, whenever we “cut” a Bézier curve with the software’s “scissors”
tool, we instantly find ourselves with two new Bézier curves, yet the path covered by these two
curves is exactly the same as that covered by the original one. How is that possible? And how
could the computer have calculated the coordinates of the control points of these new curves
in a fraction of a second?
The solution to this mystery lies in the algorithm of de Casteljau, which we shall describe in
this chapter. It is unfortunate that the name of Paul de Casteljau is less well known that that
of Bézier, since the curves of the latter would be of little interest without the algorithm of the
former.
In the following text, we shall present the mathematical bases of the technique of Bézier
curves, which are indispensable to anyone who wishes to manipulate the curves in any way
other than with a mouse and a screen.
```

```text
G.2. Bézier Curves
G.2.1
Definition and Interesting Properties
Definition. — Let z0,z1,z2,z3 be elements of R2. Then the cubic Bézier curve with starting
point z0, ending point z3, and control points z1 and z2 is:
b(t) = (1−t)3z0 +3t(1−t)2z1 +3t2(1−t)z2 +t3z3
for t ∈[0,1].
z0
z1
z2
z3
Interesting properties. — (1) Control points lie on the lines tangent to the starting and ending
points.
(2) Bézier curve b lies completely within the polygon z0z1z2z3.
z0
z1
z2
z3
polygon z0z1z2z3
(3) Let A be an affine transformation (for example, a rotation, reflection, translation, or scaling operation). Then the image of b under A is equal to the Bézier curve defined by the points A(z0),A(z1),
A(z2),A(z3).
Comments. — Property 1 makes the drawing of the curves more intuitive. Property 2 ensures
us that the entire curve will remain within the visible area of the screen if the four points that
define it lie in that area: after all, who would want to see curves that could fly offto infinity
at any time? Finally, property 3 implies that design software can very easily torture Bézier
curves by moving them, rotating them, reflecting them, and scaling them up or down. That
is because software in fact transforms only four points. The calculation of the curve is then
done by the famous algorithm of de Casteljau, once the four new points have been established. Applying an affine transformation to four points is not really a great feat of numerical
computation.
Proof of the properties. — (1) We need only derive b:
b′(t) = 3[t2z0 +t(2−3t)z1 +(1−4t +3t2)z2 −(1−t)2z3];
therefore b′(0) = 3(z2 −z3),b′(1) = 3(z0 −z1). In other words, the slopes of the lines tangent to
the curve at the points t = 0 (the starting point) and t = 1 (the ending point) are parallel to the
```

```text
vectors −−→
z0z1 and −−→
z2z3, respectively. Since the tangent lines are parallel to the vectors, and since each
has a point in common with them, the vectors therefore lie on the tangents, and so do the points
z1 and z2.
(2) The inside of the polygon z0z1z2z3 is the set of points:
λ0z0 +λ1z1 +λ2z2 +λ3z3, where ∑λi = 1 and λi ≥0.
It is sufficient to prove that λ0(t) = t3,λ1(t) = 3(1−t)t2,λ2(t) = 3(1−t)2t,λ3(t) = (1−t)3; then the
two properties above will be confirmed for every t ∈[0,1]. Three lines of calculation of no great
interest.
(3) If z = (x,y) is the representation of z ∈R2 in Cartesian coordinates, an affine transformation A
can, by definition, be written:
A(x,y) = (αx+βy+γ,δx+εy+ζ).
We wish to show that A(b(t)) = (1−t)3A(z0)+3t(1−t)2A(z1)+3t2(1−t)A(z2)+t3A(z3).
Let us simplify by writing b(t) = ∑3
i=0 bi(t)zi and then proceed:
A(b(t)) = A

∑
i=0
bi(t)zi

=

α
∑
i=0
bi(t)xi +β
∑
i=0
bi(t)yi +γ,δ
∑
i=0
bi(t)xi + ε
∑
i=0
bi(t)yi +ζ

.
But we just proved in Property 2 that ∑3
i=0 bi(t) = 1 for all t. We can therefore multiply γ and ζ by
this expression:
A(b(t)) =(α
∑
i=0
bi(t)xi +β
∑
i=0
bi(t)yi +γ
∑
i=0
bi(t),δ
∑
i=0
bi(t)xi
+ε
∑
i=0
bi(t)yi +ζ
∑
i=0
bi(t)).
And we can remove ∑3
i=0 bi(t) from the expression: A(b(t)) = ∑3
i=0 bi(t)·(αxi+βyi+γ,δxi+εyi+ζ) =
∑3
i=0 bi(t)·A(xi,yi).
qed
G.2.2
de Casteljau’s Algorithm
Theorem. — Let z0,z1,z2,z3 be elements of R2 and let b(t) be the cubic Bézier curve defined on [0,1]
by these points. We shall define a set of points in the plane {zi,j(t)|0 ≤j ≤3,0 ≤i ≤3−j} as follows:
zi,0(t) = zi for all 0 ≤i ≤3 and all t ∈[0,1]
zi,1(t) = (1−t)zi,0(t)+t zi+1,0(t) for all 0 ≤i ≤2
zi,2(t) = (1−t)zi,1(t)+t zi+1,1(t) for all 0 ≤i ≤1
z0,3(t) = (1−t)z0,2(t)+t z1,2(t).
Therefore b(t) = z0,3(t).
```

G.2. Bézier Curves Proof. — We need only replace zi,j(t) with their values: z0,1(t) = (1−t)z0 +t z1 z1,1(t) = (1−t)z1 +t z2 z2,1(t) = (1−t)z2 +t z3 and therefore: z0,2(t) = (1−t)[(1−t)z0 +t z1]+t[(1−t)z1 +t z2] z1,2(t) = (1−t)[(1−t)z1 +t z2]+t[(1−t)z2 +t z3] which gives: z0,3(t) = (1−t)  (1−t)[(1−t)z0 +t z1]+t[(1−t)z1 +t z2]  +t  (1−t)[(1−t)z1 +t z2]+t[(1−t)z2 +t z3]  = (1−t)3z0 +3t(1−t)2z1 +3t2(1−t)z2 +t3z3 = b(t). qed Comments. — de Casteljau’s algorithm can be represented graphically as follows: z0 = b(0) z3 = b(1) z0,3 b(2/3) z1 z2 z0,1 z0,2 z1,1 z1,2 z2,1 where we have chosen to determine the point b( 2 3) graphically. The point z0,1 lies at 2 3 of the distance between z0 and z1. The same goes for z1,1 and z2,1. We draw the line segments z0,1z1,1 and z1,1z2,1. Then we find the points z0,2 and z1,2, which are 2 3 of the distance between the endpoints of the line segments. We draw the segment z0,2z1,2. It must necessarily be tangent to the Bézier curve. The point of intersection of this segment with the curve is b( 2 3). G.2.3 Subdivision of Bézier Curves Definition. — Let b(t) be a Bézier curve and let κ be in [0,1]. Then b(t) is subdivided into two Bézier curves bstart(t) = b(κt) and bend(t) = b( t−κ 1−κ). Theorem. — Let z0,z1,z2,z3 be in R2 and let b be the cubic Bézier curve defined on [0,1] by those points. Let κ be in [0,1]. Let bstart and bend be the two Bézier curves obtained by subdividing b at the

point b(κ). Let z0,1,z1,1,z2,1,z0,2,z1,2 be the points obtained by applying de Casteljau’s algorithm to the curve b. Then the points z0,1 and z0,2 are the control points of bstart, and the points z1,2 and z2,1 are the control points of bend. z0 = b(0) z3 = b(1) z0,3 b(2/3) z1 z2 z0,1 z0,2 z1,1 z1,2 z2,1 bstart bend Comments. — The mystery is solved: here is how the software instantly knows the control points of the new Bézier curve obtained by “cutting” the old Bézier curve into two pieces. As soon as we click on a point z on the curve, the software calculates the value t of that point through the bisection method: it takes b( 1 2) and checks whether the point z lies in the polygon formed by the four points of bstart or bend. According to the result, the curve is subdivided again, and the the software determines in which polygon the point lies, and so forth. By continuing in this manner, it can calculate the value of t for which b(t) ≈z with ever greater precision. Proof. — By performing the calculations of de Casteljau’s algorithm on the point κ, we find: z0,1 = (1−κ)z0 +κz1 z0,2 = (1−κ)[(1−κ)z0 +κz1]+κ[(1−κ)z1 +κz2] z0,3 = (1−κ)  (1−κ)[(1−κ)z0 +κz1]+κ[(1−κ)z1 +κz2]  +κ  (1−κ)[(1−κ)z1 +κz2]+κ[(1−κ)z2 +κz3]  . Suppose that the theorem is true. Then we have: bstart(t) = (1−t)3z0 +3t(1−t)2z0,1 +3t2(1−t)z0,2 +t3z0,3. Make the substitutions: bstart(t) = (1−t)3z0 +3t(1−t)2[(1−κ)z0 +κz1] +3t2(1−t)  (1−κ)[(1−κ)z0 +κz1]+κ[(1−κ)z1 +κz2]  +t3  (1−κ)  (1−κ)[(1−κ)z0 +κz1]+κ[(1−κ)z1 +κz2]  +κ  (1−κ)[(1−κ)z1 +κz2]+κ[(1−κ)z2 +κz3]  .

G.2. Bézier Curves We need only check that this expression is equal to: b(κt) = (1−κt)3z0 +3κt(1−κt)2z1 +3κ2t2(1−κt)z2 +t3κ3z3. Simply carry out the calculations term by term. A full page of calculations of no great interest.

```text
Bibliography
[1] Atif Aamir. Nafees Nasta’leeq, 2003. http://www.crulp.org/nafeesNastaleeq.html
[2] Douglas Adams. The Hitchhiker’s Guide to the Galaxy. Pan Books, 1979.
[3] Adobe Developer Support.
Adobe Binary Screen Font Files Specification v. 2, Technote
5006, 1992. http://partners.adobe.com/asn/developer/pdfs/tn/5006.ABF_Spec.
pdf
[4] Adobe Developer Support. PostScript Language Document Structuring Conventions Specification, Technote 5001, 1992. http://partners.adobe.com:80/asn/developer/pdfs/
tn/5001.DSC_Spec.pdf
[5] Adobe Developer Support. The StemSnap Hint Operator for Type 1 Font Programs, 1992.
http://partners.adobe.com:80/asn/developer/pdfs/tn/5049.StemSnap.pdf
[6] Adobe Developer Support. Supporting Downloadable PostScript Language Fonts, Technote
5040, 1992. http://partners.adobe.com/asn/developer/pdfs/tn/5040.Download_
Fonts.pdf
[7] Adobe Developer Support. Font Naming Issues, Technote 5088, 1993. http://partners.
adobe.com/asn/developer/pdfs/tn/5088.FontNames.pdf
[8] Adobe Developer Support.
Glyph Bitmap Distribution Format (BDF) Specification v.
2.2, Technote 5005, 1993. http://partners.adobe.com/asn/developer/pdfs/tn/5005.
BDF_Spec.pdf
[9] Adobe Developer Support. CID-Keyed Font Technology Overview, Technote 5092, 1994.
http://partners.adobe.com:80/asn/developer/pdfs/tn/5092.CID_Overview.pdf
[10] Adobe Developer Support. Type 1 Font Format Supplement, Technote 5015, 1994. http:
//partners.adobe.com:80/asn/developer/pdfs/tn/5015.Type1_Supp.pdf
[11] Adobe Developer Support.
Adobe CMap and CIDFont Files Specification, Technote
5014,
1996.
http://partners.adobe.com:80/asn/developer/pdfs/tn/5014.CMap_
CIDFont_Spec.pdf
[12] Adobe Developer Support. Adobe Font Metrics File Format Specification v. 4.1, Technote
5004, 1998. http://partners.adobe.com/asn/developer/pdfs/tn/5004.AFM_Spec.
pdf
```

```text
Bibliography
[13] Adobe Developer Support. The Type 42 Font Format Specification, Technote 5012, 1998.
http://partners.adobe.com:80/asn/developer/pdfs/tn/5012.Type42_Spec.pdf
[14] Adobe Developer Support. The Compact Font Format Specification, Technote 5176, 2000.
http://partners.adobe.com:80/asn/developer/pdfs/tn/5176.CFF.pdf
[15] Adobe Developer Support.
The Type 2 Charstring Format, 2000. http://partners.
adobe.com:80/asn/developer/pdfs/tn/5177.Type2.pdf
[16] Adobe Developer Support. Adobe-Japan1-6 character collection for CID-keyed fonts,
technote 5078. Technical report, Adobe Systems Inc., 2004. http://partners.adobe.
com/public/developer/en/font/5078.Adobe-Japan1-6.pdf
[17] Adobe Systems. Adobe Type Manager Deluxe. http://www.adobe.com/products/atm/
main.html
[18] Adobe Systems.
Adobe Type Manager Light. http://www.adobe.com/products/
atmlight/main.html
[19] Adobe Systems. Adobe Type Reunion Deluxe. http://www.adobe.com:80/products/
atm/atr.html
[20] Adobe Systems.
PostScript Language Program Design.
Addison-Wesley, 1988.
http://partners.adobe.com/asn/tech/ps/download/samplecode/ps_psbooks/
GreenBook.zip
[21] Adobe Systems. Adobe Type 1 Font Format, version 1.1. Addison-Wesley, 1990. http:
//partners.adobe.com:80/asn/developer/pdfs/tn/T1_SPEC.PDF
[22] Adobe Systems.
PostScript Language Tutorial and Cookbook.
Addison-Wesley, 1990.
http://partners.adobe.com/asn/tech/ps/download/samplecode/ps_psbooks/
BlueBook.zip
[23] Adobe Systems. WadaMin-Regular CIDFont file, 1996. ftp://ftp.oreilly.com/pub/
examples/nutshell/cjkv/adobe/samples
[24] Adobe Systems. PostScript Language Reference Manual. Addison-Wesley, 3rd edition,
1999. http://partners.adobe.com/asn/developer/pdfs/tn/PLRM.pdf
[25] Adobe Systems. Adobe glyph list, 2002. http://partners.adobe.com:80/asn/tech/
type/glyphlist.txt
[26] Adobe Systems. CMaps for PDF 1.4 CJK fonts, 2003. http://partners.adobe.com/
asn/acrobat/technotes.jsp
[27] Adobe Systems. Unicode and glyph names, 2003. http://partners.adobe.com:80/
asn/tech/type/unicodegn.jsp
[28] Adobe Systems.
PDF Reference: Version 1.6.
Addison-Wesley, 5th edition, 2004.
http://partners.adobe.com/asn/acrobat/docs/File_Format_Specifications/
PDFReference.zip
```

```text
Bibliography
[29] AFII. Registration Authority for Font-Related Objects, 2001. http://www.glocom.ac.jp/
iso10036/
[30] Jean Alessandrini. Nouvelle classification typographique: Codex 1980. Communication
et Langages, 43:35–56, 1979.
[31] AMS. AMSFonts, 1995. http://www.ams.org/tex/amsfonts.html
[32] Jacques André. The Scrabble font. The PostScript Journal, 3(1):53–55, 1990.
[33] Jacques André. Contribution à la création de fontes en typographie numérique, Habilitation
à diriger des recherches. PhD thesis, Université de Rennes 1, IFSIC, 1993.
[34] Jacques André. Lucida, a-t-elle un gros œil ? La Lettre GUTenberg, 5:24–26, 1997. http:
//www.gutenberg.eu.org/pub/GUTenberg/publicationsPDF/lettre5.pdf
[35] Jacques André.
De Pacioli à Truchet, trois siècles de géométrie pour les caractères.
In Actes du treizième colloque Inter-IREM d’Histoire et d’Épistémologie des mathématiques,
2000. http://www.univ-irem.fr/commissions/epistemologie/colloques/co00.htm
[36] Jacques André. Histoire d’@, histoire d’Œ. Rumeurs, traitement de textes et enseignement. In Traitement de texte et production de documents, INRP, Octobre 2004, pages 19–34,
2004. http://jacques-andre.fr/japublis/dida/andrej.htm
[37] Jacques André and Christian Delorme. Le Delorme: un caractère modulaire et dépendant du contexte. Communication et Langages, 86:65–76, 1990.
[38] Jacques André et al.
Ligatures et caractères contextuels, Cahier GUTenberg 22, 1995.
http://www.gutenberg.eu.org/publications/cahiers/48-cahiers22.html
[39] Jacques André et al. La fonte du jour: Vendôme. La Lettre GUTenberg, 16:16–20, 1999.
http://www.gutenberg.eu.org/pub/GUTenberg/publicationsPDF/lettre16.pdf
[40] Jacques André, Roger Hersch, et al.
Workshop on font design systems (SophiaAntipolis, 18–19 mai 1987), 1987.
[41] Jacques André and Victor Ostromoukhov.
Punk: de METAFONT à PostScript.
Cahiers GUTenberg, 4:23–28, 1989. http://www.gutenberg.eu.org/pub/GUTenberg/
publicationsPDF/4-ostromoukhov.pdf
[42] Jacques André and Irène Vatton. Dynamic optical scaling and variable-sized characters.
Electronic Publishing—Origination, Dissemination, and Design, 7(4):231–250, 1994.
[43] Anonymous. Archives of the SAIL (Stanford Artificial Intelligence Laboratory) project,
1966-1990. http://z.baumgart.org/saildart/prog/SYS/index.html
[44] Anonymous. Introduction à la calligraphie chinoise. Éditions du centenaire, Paris, 1983.
[45] Anonymous.
Font-file format.
Technical report, Microsoft Knowledge Base, 199?
http://support.microsoft.com/default.asp?scid=KB;en-us;q65123
[46] Anonymous. snfstr.h and snfread.c, taken from X11 R6.4 source code, 1998. http:
//ftp.x.org/pub/
```

```text
Bibliography
[47] Anonymous.
PFM file format, 2000. http://homepages.fbmev.de/bm134751/pfm_
fmt_en.html
[48] Anonymous. Lexique des règles typographiques en usage à l’imprimerie nationale. Imprimerie Nationale, 2002.
[49] Apple Computer. Apple Inside Macintosh, Volume I. Addison-Wesley, 1985. http://
developer.apple.com/techpubs/mac/pdf/MoreMacintoshToolbox.pdf
[50] Apple Computer. Apple Inside Macintosh, Volume IV. Addison Wesley, 1985. http://
developer.apple.com/techpubs/mac/pdf/MoreMacintoshToolbox.pdf
[51] Apple Computer. Apple Inside Macintosh, Volume V. Addison Wesley, 1986. http://
developer.apple.com/techpubs/mac/pdf/MoreMacintoshToolbox.pdf
[52] Apple Computer. LaserWriter Reference. Addison-Wesley, 1988.
[53] Apple Computer. Guide to Macintosh Software Localization. Addison-Wesley, 1992.
[54] Apple Computer. TrueType GX Font Formats, 1993.
[55] Apple Computer. QuickDraw GX Typography. Addison-Wesley, 1994. ftp://ftp.apple.
com/developer/Technical_Publications/Archives/QDGX_Typography.sit.hqx
[56] Apple Computer. The TrueType Reference Manual, 1996. http://developer.apple.com/
fonts/TTRefMan/index.html
[57] Apple Computer. Installable keyboard layouts, 2002. http://developer.apple.com/
technotes/tn2002/tn2056.html
[58] Apple Computer.
SFNT file layout structures and constants, in macos x, 2002.
/System/Library/Frameworks/ApplicationServices.framework/Versions/A/
Frameworks/ATS.framework/Versions/A/Headers/SFNTLayoutTypes.h
[59] Apple Computer.
Instructing fonts, 2003. http://developer.apple.com/fonts/
TTRefMan/RM03/Chap3.html
[60] Apple Computer. Using and Managing Fonts in Mac OS X, A Guide for Creative Professionals, 2003. http://205.134.180.85/UsingFontsinMacOSX.pdf
[61] Vlad Atanasiu. Le phénomène calligraphique à l’époque du sultanat mamluk. PhD thesis,
École pratique des Hautes Études, Section des Sciences historiques et philologiques,
2003. http://atanasiu.freesurf.fr/thesis/atanasiu2003phd.pdf
[62] Peter Bain and Paul Shaw. Blackletter: Type and National Identity. Princeton Architectural Press, 1998.
[63] Paul Barrett et al.
Numerical Python, 2000. http://sourceforge.net/projects/
numpy
[64] Dieter Barron. ttftot42, 1999. http://ftp.giga.or.at/pub/nih/ttftot42/
```

Bibliography [65] Benjamin Bauermeister. A manual of Comparative Typography: The PANOSE System. Van Nostrand Reinhold, 1988. [66] Benjamin Bauermeister. Panose classification guide - numeric specifications for classification of fonts in the panose typeface matching system. Technical report, Elseware Corporation, 1992. [67] Barbara Beeton. Mathematical symbols and cyrillic fonts ready for distribution. TUGboat, 6(2):59–63, July 1985. [68] Barbara Beeton. Mathematical symbols and cyrillic fonts ready for distribution (revised). TUGboat, 6(3):124–128, November 1985. [69] Barbara Beeton. METAFONT mode_def settings for various TEX output devices. TUGboat, 8(1):33–33, 1987. [70] Barbara Beeton. Update: METAFONT mode_def settings for TEX output devices. TUGboat, 8(2):132–134, 1987. [71] Gábor Bella and Yannis Haralambous. Fontes intelligentes, textèmes et typographie dynamique. Document Numérique, 9:167–216, 2006. [72] Bob Bemer. How ASCII got its backslash, 2002. http://www.bobbemer.com/BACSLASH. HTM [73] A. Berdnikov, O. Lapko, M. Kolodin, A. Janishevsky, and A. Burykin. Cyrillic encodings for LATEX2ε multi-language documents. TUGboat, 19(4):403–416, 1998. [74] Tim Berners-Lee, R. Fielding, U.C. Irvine, and L. Masinter. Uniform Resource Identifiers (URI): Generic Syntax, RFC 2396. IETF, 1998. http://www.ietf.org/rfc/rfc2396.txt [75] Karl Berry. Filenames for fonts. TUGboat, 11(4):517–520, 1990. [76] Karl Berry. modes.mf, a collection of METAFONT mode_def’s, 2005. http://www.ctan. org/tex-archive/fonts/modes/modes.mf [77] Karl Berry and Kathryn A. Hargreaves. GNU font utilities, v. 0.6, 1992. http://www. math.utah.edu/docs/info/fontu_toc.html [78] Karl Berry and Olaf Weber. kpathsea library, version 3.5.4, 2005. http://www.tug.org/ teTeX/tetex-texmfdist/doc/programs/kpathsea.pdf [79] Tom Bishop and Richard Cook. A specification for cdl Character Description Language. Technical report, Wenlin, 2003. http://www.wenlin.com/cdl/cdl_spec_2003_10_31. pdf [80] Tom Bishop and Richard Cook. Character description language cdl: The set of basic CJK unified stroke types. Technical report, Wenlin, 2004. http://www.wenlin.com/ cdl/cdl_strokes_2004_05_23.pdf [81] Bitstream. TrueDoc. http://www.bitstream.com/categories/developer/truedoc/ index.html

```text
Bibliography
[82] Lewis Blackwell. Twentieth-Century Type. Yale University Press, 2004 (revised edition).
[83] Gérard Blanchard. Pour une sémiologie de la typographie. PhD thesis, École des hautes
études en sciences sociales, 1980.
[84] Gérard Blanchard. Aide au choix de la typo-graphie. Atelier Perrousseaux, 2001.
[85] Gérard Blanchard et al. Pour une sémiologie de la typographie. Rémy Magermans, 1979.
[86] Erik van Blokland and Just van Rossum. Random code—the Beowulf random font.
The PostScript Journal, 3(1):8–11, 1990.
[87] Andrew Boag. Typographic measurement: a chronology. Typography Papers, 1:105–
121, 1996.
[88] Bert Bos, Hakon Wium Lie, Chris Lilley, and Ian Jacobs (eds.). Cascading Style Sheets,
level 2. CSS2 Specification. W3C, 1998. http://www.w3.org/TR/REC-CSS2
[89] René Bouvard. Notions de typographie orientale. Éditions de l’École Estienne, 1893.
[90] Jim Breen. The EDICT project, 1991-2003. http://www.csse.monash.edu.au/~jwb/
edict.html
[91] Andries Brouwer. Font Formats Recognized by the Linux kbd Package, 2002. http://www.
win.tue.nl/~aeb/linux/kbd/font-formats.html
[92] Max Bruinsma. The erotics of type, 2000. http://www.xs4all.nl/%7emaxb/erotype.
html
[93] Ian Caldwell and Dustin Thomason. The Rule of Four. The Dial Press, 2004.
[94] Harry Carter. A view of early typography up to about 1600. Hyphen Press, 2002.
[95] Juliusz Chroboczek. mkfontscale - Create an Index of Scalable Font Files for X. http://www.
xfree86.org/current/mkfontscale.1.html
[96] Marcel Cohen, Jean Sainte Fare Garnot, et al. L’écriture et la psychologie des peuples, XXIIe
semaine de synthèse. Armand Colin, 1963.
[97] Collectif. De plomb, d’encre & de lumière. Essai sur la typographie & la communication
écrite. Imprimerie nationale Éditions, 1982.
[98] Collectif. Les caractères de l’Imprimerie nationale. Imprimerie nationale Éditions, 1990.
[99] John Collins and Bob Thomas. Coding of Outline Fonts: PFR Specification (Version 1.3).
Bistream, 2005. http://www.bitstream.com/font_rendering/pdfs/pfrspec1.3.pdf
[100] François Colonna.
Hypnerotomachia polophili, 1499. http://mitpress.mit.edu/
e-books/HP/
[101] Agfa Compugraphic. Intellifont scalable typeface format, 1992.
[102] Vincent Connare. Basic hinting philosophies and TrueType instructions, 1997. http:
//www.microsoft.com/typography/hinting/tutorial.htm
```

Bibliography [103] Robin Cover. Language identifiers in the markup context. Technical report, OASIS, 2002. http://xml.coverpages.org/languageIdentifiers.html [104] Dan Crevier, Richard Northcott, Abbey Kazuya, and Ayumi Kimura. UniDict, 1999. http://www.enfour.co.jp/unidict/e/manual.html [105] Anne Cuneo. Le maître de Garamond. Stock, 2003. [106] Peter Daniels and William Bright. The World’s Writing Systems. Oxford University Press, 1996. [107] John Davies, Dieter Fensel, and Frank van Harmelen. Towards the Semantic Web: Ontology-Driven Knowledge Management. John Wiley & Sons, 2003. [108] Mark Davis. Unicode Standard Annex #24. script names. Technical report, Unicode Consortium, 2003. http://www.unicode.org/reports/tr24 [109] Mark Davis and Martin Dürst. Unicode Standard Annex #15. Unicode normalization forms. Technical report, Unicode Consortium, 2003. http://www.unicode.org/ reports/tr15 [110] Mark Davis and Markus Scherer. Binary-Ordered Compression for Unicode, 2001. http://oss.software.ibm.com/icu/docs/papers/binary_ordered_compression_ for_unicode.html [111] Michael Dawson. Python Programming for the Absolute Beginner. Thomson Course Technology, 2003. [112] Luc[as] de Groot. MoveMeMM, a porno font, 1996. http://www.fontfabrik.com/ lucfuse.html [113] Michael S. de Laurentis. PANOSE 2.0 white paper. Hewlett-Packard document EWC92-0015h, 1993. http://www.w3.org/Fonts/Panose/pan2.html [114] Jacques Derrida. De la grammatologie. Les Éditions de Minuit, 1967. [115] Jacques Derrida. Signature événement contexte, dans Marges de la philosophie. Les Éditions de Minuit, 1972. [116] Luc Devroye. TrueType versus Type 1, 2001. http://cg.scs.carleton.ca/~luc/ ttvst1.html [117] Luc Devroye. Font formats, talk given at EuroTEX 2003, ENST Bretagne, Brest, 2003. [118] Luc Devroye and Michael McDougall. Random fonts for the simulation of handwriting. Electronic Publishing—Origination, Dissemination, and Design, 8(4):281–294, 1995. http://cajun.cs.nott.ac.uk/compsci/epo/papers/volume8/issue4/ep129ld.pdf [119] DiamondSoft. Font Reserve for Macintosh, Font Reserve for Windows, Font Reserve Server. http://www.diamondsoft.com/products/index.html

```text
Bibliography
[120] Yann Dirson.
The CP file format.
Technical report, Debian, 1998. http:
//www.ambienteto.arti.beniculturali.it/cgi-bin/dwww?type=file&location=
/usr/share/doc/console-tools/file-formats/cp
[121] Mark Douma.
dfontifier, 2003. http://homepage.mac.com/mdouma46/dfont/dfont.
html
[122] DTL. FontMaster, 1995. http://www.fontmaster.nl/english/
[123] Duden. Rechtschreibung der deutschen Sprache und der Fremdwörter. Bibliographisches
Institut Mannheim, 1961.
[124] Albrecht Dürer. On the Just Shaping of Letters. Dover, 1917, reprint 1965.
[125] Martin Dürst. Coordinate-independent font description using Kanji as an example.
Electronic Publishing—Origination, Dissemination, and Design, 6(3):133–143, 1993.
[126] Martin Dürst, François Yergeau, Richard Ishida, Misha Wolf, and Tex Texin. W3C working draft. character model for the World Wide Web 1.0. Technical report, W3C, 2003.
http://www.w3.org/TR/charmod/
[127] David Earls. Designing Typefaces. RotoVision, 2002.
[128] Julia Ecklar. Kobayashi Maru. Star Trek, 1989.
[129] David Eisenberg. SVG. O’Reilly France, 2003. http://www.oreilly.fr/catalogue/
SVG.html
[130] em2 Solutions. Glyphgate. http://www.glyphgate.com/info/
[131] Pierre Enckell and Pierre Rézeau. Dictionnaire des onomatopées. puf, 2003.
[132] Extensis. Suitcase for Macintosh, Suitcase for Windows, Suitcase Server. http://www.
extensis.com/fontman/
[133] Carl Faulmann.
Das Buch der Schrift enthaltend die Schriftzeichen und Alphabete aller
Zeiten und aller Völker des Erdkreises. Druck und Verlag der kaiserlich-königlichen Hofund Staatsdruckerei, Wien, 1880.
[134] Jon Ferraiolo, Jun Fujisawa, and Dean Jackson (eds.). Scalable Vector Graphics (SVG) 1.1
Specification. W3C, 2003. http://www.w3.org/TR/SVG11/
[135] Gabriel Valiente Feruglio.
Modern Catalan typographical conventions.
TUGboat,
16(3):329–338, 1995.
[136] James Février. Histoire de l’écriture. Payot, 1995.
[137] Dimitrios Filippou. Διαγωνισμ[P 'λληνικο\ παγγρ!μματοP: τ^ &ποτελ0σματα. To
Eutupon, 9:57–59, 2002. http://ocean1.ee.duth.gr/eutupon/eutupon9.pdf
[138] Jim Flowers and Stephen Gildea.
X Logical Font Description Conventions, version 1.5.
Digital Equipment Corporation, 1994. http://www.xfree86.org/current/xlfd.pdf
```

Bibliography
[139] FontLab. TransType, 1999-2003. http://www.fontlab.com/html/transtype.html
[140] FontLab.
FontLab Studio – next-generation pro font editor, 1999-2006. http://
fontlab.com/Font-tools/FontLab-Studio/
[141] FontLab.
FontLab 5 user manual, 2006. http://www.font.to/downloads/manuals/
FLS5MacManual.zip
[142] Fournier, le jeune. Manuel typographique, utile aux gens de lettres & à ceux qui exercent les
différentes parties de l’Art de l’Imprimerie. Imprimé par l’Auteur, rue des Postes, 1764,
facsimile réédité en 1995.
[143] Jeffrey Friedl. Mastering Regular Expressions. O’Reilly France, 3rd edition, 2006. http:
//www.oreilly.com/catalog/regex3/index.html
[144] Adrien Frutiger. Type Sign Symbol. ABC Edition, 1999.
[145] David Fuchs. The format of PXL files. TUGboat, 2(3):8–12, 1981.
[146] Jim Fulton. xfd - Display All the Characters in an X Font. http://www.xfree86.org/4.3.
0/xfd.1.html
[147] Simon Garfinkel. Web Security, Privacy & Commerce. O’Reilly, 2nd edition, 2001. http:
//www.oreilly.com/catalog/websec2/index.html
[148] Roudzéro Sergeïevitch Gilyarevskii and Vladimir Sergeïevitch Grivnin.
Определитель языков мира по письменностям (Language identification through its writing
system). Издательство восточной литературы, Москва, 1960.
[149] Rémi Goblot. Algèbre Géométrique, polycopié de cours donné à l’Université de Lille
I, 1982-83.
[150] Rémi Goblot. Thèmes de géométrie: Géométrie affine et euclidienne — agrégation de mathématiques. Dunod Masson, 1998.
[151] Danny Goodman. Dynamic HTML. The Definitive Reference. O’Reilly, 2e edition, 2002.
http://www.oreilly.com/catalog/dhtmlref2/
[152] David Gourley and Brian Totty. HTTP: The Definitive Guide. O’Reilly, 2002. http://
www.oreilly.com/catalog/httptdg/index.html
[153] Dean Guenther and Janene Winter. An international phonetic alphabet. TUGboat,
12(1):149–156, 1991.
[154] Max Hall. An Embarrassment of Misprints: Comical and Disastrous Typos of the Centuries.
Fulcrum
Publishing,
1995.
http://www.amazon.com/exec/obidos/tg/detail/
-/1555912028/qid=1101141316/sr=1-4/ref=sr_1_4/102-1069734-0297715?v=
glance&s=books
[155] Jack Halpern. The Kodansha Kanji Learner’s Dictionary. Kodansha International, 1999.

```text
Bibliography
[156] Tereza Haralambous and Yannis Haralambous. Characters, glyphs and beyond. In Proceedings of the Glyph and Typesetting Workshop, Kyoto, Japon, 2003. http://omega.enstb.
org/yannis/pdf/kyoto-tereza.pdf
[157] Yannis Haralambous. The DVR and DVX formats, specifications and tools. http://
omega.enstb.org/yannis/dvi2dvr
[158] Yannis Haralambous.
Tiqwah, a typesetting system for biblical Hebrew, based
on TEX.
In Proceedings of the Fourth International Colloquium “Bible and Computer:
Desk and Discipline, The impact of computers on Bible Studies,” Amsterdam, 1994, pages
445–470. Honoré Champion Éditeur, 1994. http://omega.enstb.org/yannis/pdf/
biblical-hebrew94.pdf
[159] Yannis Haralambous. Typesetting Khmer. Electronic Publishing—Origination, Dissemination, and Design, 7(4):197–215, 1994.
[160] Yannis Haralambous. Sabra, a Syriac TEX system. In Proceedings of SyrCOM-95, the 1st
International Forum on Syriac Computing, Washington DC 1995, pages 3–24, 1995. http:
//omega.enstb.org/yannis/pdf/syriac96.pdf
[161] Yannis Haralambous. Tour du monde des ligatures. Cahiers GUTenberg, 22:69–80, 1995.
http://omega.enstb.org/yannis/pdf/ligatures.pdf
[162] Yannis Haralambous.
Large brackets and accents: the yhmath package.
TUGboat,
6(1):6–8,
1996.
http://tug.ctan.org/cgi-bin/getFile.py?fn=/usergrps/uktug/
baskervi/bask6_1.pdf
[163] Yannis Haralambous.
From Unicode to typography, a case study: the Greek script.
In Proceedings of the 14th International Unicode Conference, Boston 1999, pages b.10.1–
b.10.36, 1999. http://omega.enstb.org/yannis/pdf/boston99.pdf
[164] Yannis Haralambous. DruqsaΩ in gebrocenen Scri#en. In Proceedings of the DANTE
2000 Conference, 2000. http://omega.enstb.org/yannis/pdf/dante2000.pdf
[165] Yannis Haralambous.
Unicode et typographie : un amour impossible.
Document
Numérique, 6(3-4):105–137, 2002. http://omega.enstb.org/yannis/pdf/docnum.pdf
[166] Yannis Haralambous. Ο# \$ναφορ
τν μονοτονιστν στν Βιλαμ'βιτ
κα στν Γε)ργιο
Χατζιδκι (References of monotonists to Wilamowitz and to Georgios Hadzidakis). Ο μικρ[P
&στρολ!βοP, Ε`θ9νη, 2007. http://www.polytoniko.org/haralambous.php
[167] Yannis Haralambous and Gábor Bella. Injecting information into atomic units of text.
In Proceedings of the ACM Symposium on Document Engineering, Bristol, 2005.
[168] Yannis Haralambous and Gábor Bella. Open-belly surgery in Ω2. TUGboat, 27(1):91–
97, 2006.
[169] Yannis Haralambous et al.
Homepage of the citizen’s movement for the reintroduction of the polytonic system. http://www.polytoniko.gr
```

```text
Bibliography
[170] Yannis Haralambous and John Plaice. Multilingual typesetting with Ω, a case study:
Arabic. In Proceedings of the International Symposium on Multilingual Information Processing, Tsukuba 1997, pages 137–154. ETL Japan, 1997. http://omega.enstb.org/yannis/
pdf/tsukuba-arabic97.pdf
[171] Yannis Haralambous and John Plaice. Traitement automatique des langues et composition sous Ω. Cahiers Gutenberg, 39-40:139–166, 2001. http://omega.enstb.org/
yannis/pdf/metz2001.pdf
[172] Yannis Haralambous and Klaus Thull. Typesetting modern Greek with 128 character
codes. TUGboat, 10(3):354–359, 1989.
[173] Doug Henderson. Update: METAFONT mode_def settings for TEX output devices. TUGboat, 8(3):268–270, 1987.
[174] Doug Henderson. Outline fonts with METAFONT. TUGboat, 10(1):36–38, 1989.
[175] Lee Hetherington and Claire Connelly. Type 1 utilities version 1.28, 2003. http://www.
lcdf.org/~eddietwo/type/#t1utils
[176] Hewlett Packard.
PCL 5 Printer Language Technical Reference Manual, 1992. http://
h20000.www2.hp.com/bc/docs/support/SupportManual/bpl13210/bpl13210.pdf
[177] John D. Hobby. Digitized Brush Trajectories. PhD thesis, Stanford University, 1985. http:
//cm.bell-labs.com/who/hobby/thesis.pdf
[178] John D. Hobby and Gu Guoan. A Chinese meta-font. TUGboat, 5(2):119–136, 1984.
[179] Alan Hoenig. Introducing METAPOST. TUGboat, 16(1):45–45, 1995.
[180] Alan Hoenig. Virtual fonts, virtuous fonts. TUGboat, 18(2):113–121, 1997.
[181] Alan Hoenig. Modernizing Computer Modern. TUGboat, 22(3):216–219, 2001.
[182] David A. Holzgang. Programming the LaserWriter. Addison-Wesley, 1991.
[183] Gerard J. Holzmann and Björn Pehrson. The first telegraphs. http://labit501.upct.
es/ips/libros/TEHODN/ch-2-1.5.html
[184] Martin Hosken and Sharon Correll.
Extending TrueType for Graphite.
Technical
report, Summer Institute for Linguistics, 2003. http://scripts.sil.org/cms/sites/
nrsi/media/GraphiteBinaryFormat_pdf.pdf
[185] David A. Huffman. A method for the construction of minimum-redundancy codes.
Proceedings of the IRE, 40:1098–1101, 1952.
[186] IANA. Character sets, 2004. http://www.iana.org/assignments/character-sets
[187] IETF. Public-key infrastructure X.509 (PKIX). http://www.ietf.org/html.charters/
pkix-charter.html
[188] Bitstream Inc. Bitstream Speedo font file format, 1993. http://www.bitstream.com/
fonts/support/speedo_fonts.html
```

```text
Bibliography
[189] Insider
Software.
FontAgent.
http://www.insidersoftware.com/products/
fontagentpro/
[190] ISO 3166/MA. ISO 3166-1:1997 Codes for the representation of names of countries and
their subdivisions — Part 1: Country codes, 1974-1997. http://www.iso.ch/iso/en/
prods-services/iso3166ma/02iso-3166-code-lists/list-fr1-semic.txt
[191] ISO 639 Joint Advisory Committee. ISO 639, codes for the representation of names of
languages — part 2: alpha-3 code, 2003. http://www.loc.gov/standards/iso639-2/
[192] ISO/ECMA. 7-bit coded character set, 1991. http://www.ecma-international.org/
publications/standards/Ecma-006.htm
[193] ISO/ECMA. Ecma-35/iso 2022 character coded structure and extensions techniques,
1994.
http://www.ecma-international.org/publications/standards/Ecma-035.
htm
[194] ISO/IEC.
Information Technology — Font Information Interchange, Part 1: Architecture
ISO/IEC 9541-1:1991(E), 1991. http://www.iso.ch/iso/fr/CatalogueDetailPage.
CatalogueDetail?CSNUMBER=17280
[195] ISO/IEC.
Information Technology — Font Information Interchange, Part 3: Glyph
Shape Representation ISO/IEC 9541-3:1994(E), 1994. http://www.iso.ch/iso/fr/
CatalogueDetailPage.CatalogueDetail?CSNUMBER=17280
[196] ISO/IEC.
International register of coded character sets to be used with escape sequences, 2003. http://www.itscj.ipsj.or.jp/ISO-IR/
[197] Bogusław Jackowski and Janusz Nowacki. Accents, accents, accents... — enhancing CM
fonts with “funny” characters. In Proceedings of the 24th Annual TUG Meeting, Waikoloa,
Hawai’i, 2003.
[198] Bogusław Jackowski, Janusz Nowacki, and Piotr Strzelczyk. Antykwa Półtawskiego: a
parameterized outline font. MAPS, 25:86–102, 2000.
[199] Alan Jeffrey and Rowland McDonnell. fontinst - font installation software for TEX, 1998.
http://www.tug.org/applications/fontinst/
[200] Alan Jeffrey, Sebastian Rahtz, Ulrik Vieth, and Lars Hellström. fontinst, a utility for font
installation, 1993. http://www.tug.org/applications/fontinst/
[201] Tom Jennings.
ASCII: American Standard Code for Information Infiltration, 2001.
http://www.wps.com/projects/codes/index.html
[202] Brian Jepson and Ernest E. Rothman. Mac OS X for Unix Geeks. O’Reilly, 2002. http:
//www.oreilly.com/catalog/mosxgeeks/
[203] Erik A. Johnson. FONT→NFNT FONT→NFNT, 1991. http://www.mirror.ac.uk/
collections/hensa-micros/local/mac/converters/font_to_nfnt.hqx%5Bpeek%5D
[204] Nadine Kano. Developing International Software for Windows 95 and Windows NT. Microsoft Press, 1995.
```

Bibliography [205] Albert Kapr. Fraktur: Form und Geschichte der gebrochenen Schriften. Schmidt, 1993. [206] Peter Karow. Typeface Statistics. URW Verlag, 1993. [207] Peter Karow. Font Technology, Description and Tools. Springer, 1994. [208] Sakasai Katsumi 逆井克己. 日本文字組版(Typesetting in Japanese Characters). 日本印 刷新聞社, 1999. [209] Richard Kinch. MetaFog: Converting METAFONT shapes to contours. TUGboat, 16(3):233–243, 1995. [210] Richard Kinch. TrueTEX software, 1995-2000. http://www.truetex.com/ [211] Jörg Knappen. Fonts for Africa: the fc-fonts. TUGboat, 14(2):104–106, 1993. [212] Jörg Knappen. Release 1.2 of the dc-fonts: Improvements to the European letters and first release of text companion symbols. TUGboat, 16(4):381–387, 1995. [213] Jörg Knappen. The dc fonts 1.3: Move towards stability and completeness. TUGboat, 17(2):99–101, 1996. [214] Jörg Knappen. Ankündigung: Die ec-Schriten 1.0 sind da! Technische Komödie, 4/96:8– 9, 1997. [215] Donald E. Knuth. Mathematical typography. Bulletin of the American Mathematical Society (new series), 10:337–372, 1979. [216] Donald E. Knuth. METAFONT: The Program, volume D of Computers and Typesetting. Addison-Wesley, Reading, MA, USA, 1986. [217] Donald E. Knuth. The TEXbook, volume A of Computers and Typesetting. Addison-Wesley, Reading, MA, USA, 1986. [218] Donald E. Knuth. The METAFONTbook, volume C of Computers and Typesetting. Addison-Wesley, Reading, MA, USA, 1986. [219] Donald E. Knuth. Computer Modern Typefaces, volume E of Computers and Typesetting. Addison-Wesley, Reading, MA, USA, 1986. [220] Donald E. Knuth. Virtual Fonts: More Fun for Grand Wizards. TUGboat, 11(1):13–23, 1990. [221] Donald E. Knuth. Digital Typography. CSLI Publications, 1999. [222] Donald E. Knuth and Pierre MacKay. Mixing right-to-left texts with left-to-right texts. TUGboat, 8(1):14–25, 1987. [223] Eddie Kohler. LCDF typetools, 2003. http://www.lcdf.org/type/ [224] Helmut Kopka and Patrick W. Daly. Guide to LATEX. Addison-Wesley, 4th edition, 2003. [225] Jukka Korpela. Soft hyphen (SHY) — a hard problem?, 1997-2002. http://www.cs. tut.fi/~jkorpela/shy.html

```text
Bibliography
[226] Jukka Korpela. Character histories: notes on some ASCII code positions, 2000. http:
//www.cs.tut.fi/~jkorpela/latin1/ascii-hist.html
[227] Olga G. Lapko. Full Cyrillic: How many languages? TUGboat, 17(2):174–180, 1996.
[228] Alexander Lawson. Anatomy of a Typeface. Hamish Hamilton, London, 1990.
[229] Azzeddine Lazrek. Aspects de la problématique de la confection d’une fonte pour les
mathématiques arabes. Cahiers GUTenberg, 39-40:51–62, 2001. http://www.gutenberg.
eu.org/pub/GUTenberg/publicationsPDF/39-lazrek.pdf
[230] Azzeddine Lazrek. Vers un système de traitement du document scientifique arabe. PhD
thesis, University Cady Ayyad, Marrakech, 2002.
[231] Liane Lefaivre. Leon Battista Alberti’s Hypnerotomachia poliphili. MIT Press, 1997.
[232] Mark Leisher.
The XmBDFEd BDF font editor, 2001. http://crl.NMSU.Edu/
~mleisher/xmbdfed.html
[233] Dave Lemke and Keith Packard. xfs, X Font Server. http://www.xfree86.org/4.3.0/
xfs.1.html
[234] David Lemon. Basic Type 1 hinting. Technical report, Adobe Systems Inc., 1999. http:
//www.pyrus.com/downloads/hinting.pdf
[235] Leterror. robofog, 1999. http://www.letterror.com/code/old/robofog/index.html
[236] William J. LeVeque. Font development at the AMS. TUGboat, 2(2):39–40, July 1981.
[237] Noah Levitt. gucharmap, resisting the worldwide hegemony of english!, 2003. http:
//gucharmap.sourceforge.net/
[238] Silvio Levy. Using Greek fonts with TEX. TUGboat, 9(1):20–24, April 1988.
[239] Ken Lunde. Accessibility of unencoded glyphs. In Proceedings of the 13th Unicode Conference, San José, 1998. Unicode Consortium, 1998. http://www.unicode.org/iuc/iuc13/
a10/paper.pdf
[240] Ken Lunde.
CJKV Information Processing.
O’Reilly, 1st edition, 1999. http://www.
oreilly.com/catalog/cjkvinfo/
[241] Mark Lutz and David Asher. Introduction à Python. O’Reilly France, 2000. http://www.
oreilly.fr/catalogue/lpython.html
[242] Charles E. MacKenzie.
Coded Character Sets, History and Development.
The Systems
Programming Series. Addison-Wesley, 1980.
[243] James Macnicol.
type1inst.
ftp://sunsite.unc.edu/pub/Linux/X11/xutils/
type1inst-0.6.1.tar.gz
[244] Macromedia.
Fontographer, 1995-2003. http://www.macromedia.com/software/
fontographer/
```

```text
Bibliography
[245] Ladislas Mandel. Écritures, miroir des hommes et des sociétés. Atelier Perrousseaux, 1998.
[246] Duncan Marsh. Applied Geometry for Computer Graphics and CAD. Springer Undergraduate Mathematics Series. Springer, 1999.
[247] Alex Martelli. Python in a Nutshell. O’Reilly, 2003.
[248] Bernard Marti. Télématique. Techniques, normes, services. Dunod, 1990.
[249] Eberhard Mattes.
Quick and dirty TEX to VPL, 1993. http://www.ctan.org/
tex-archive/fonts/utilities/qdtexvpl/
[250] Henry McGilton and Mary Campione. PostScript by Example. Addison-Wesley, 1992.
[251] Dinah McNutt and Miles O’Neal. The X administrator: Font formats and utilities. The
X Resource, 2(1):14–34, 1992.
[252] W. Scott Means and Elliotte Rusty Harold.
XML in a Nutshell, manuel de référence.
O’Reilly France, 3rd edition, 2004. http://www.oreilly.com/catalog/xmlnut3/
index.html
[253] Philip Meggs. Revival of the Fittest: Digital Versions of Classic Typefaces. North Light
Books, 2000.
[254] Eric Meyer. CSS: The Definitive Guide. O’Reilly, 3rd edition, 2006. http://www.oreilly.
com/catalog/csstdg3/index.html
[255] John Miano. Compressed Image File Formats. ACM Press - SIGGRAPH Series. AddisonWesley, 2000.
[256] Microsoft. Digital signatures. http://www.microsoft.com/typography/developers/
dsig/default.htm
[257] Microsoft.
Font Properties Extension. http://www.microsoft.com/typography/
property/property.htm
[258] Microsoft. TrueType 1.0 Font Files, Technical Specification, version 1.66, 1995. http://www.
microsoft.com/typography/tt/ttf_spec/_toc.doc
[259] Microsoft. Welcome to TrueType Open, 1997. http://www.microsoft.com/typography/
tt/ch1.htm
[260] Microsoft.
Visual TrueType resources, sample fonts, 1999. http://www.microsoft.
com/typography/tools/vttfont.htm
[261] Microsoft. 1-year license agreement for Microsoft Visual TrueType tool, 2000. http:
//www.microsoft.com/typography/tools/vttlicen.htm?fname=%20&fsize=
[262] Microsoft.
Visual TrueType, 2000. http://www.microsoft.com/typography/tools/
vtt.htm
[263] Microsoft.
Hinting and production guidelines specification, 2002. http://www.
microsoft.com/typography/developers/delivery/hinting.htm
```

```text
Bibliography
[264] Microsoft.
The OpenType Specification, v. 1.4, 2002. http://www.microsoft.com/
typography/otspec/default.htm
[265] Microsoft. Recommendation for OpenType fonts, 2002. http://www.microsoft.com/
typography/otspec/recom.htm
[266] Microsoft.
Visual OpenType Layout Tool, 2002. http://www.microsoft.com/
typography/developers/volt/default.htm
[267] Microsoft. Features for the Korean Hangul script, 2003. http://www.microsoft.com/
typography/otfntdev/hangulot/features.htm
[268] Microsoft. Microsoft Keyboard Layout Creator, 2003. www.microsoft.com/globaldev/
tools/msklc.mspx
[269] Microsoft.
Web Embedding Font Tool, 2003. http://www.microsoft.com/
typography/web/embedding/weft3/default.htm
[270] Microsoft.
Microsoft typography registered vendors, 2007. http://www.microsoft.
com/typography/links/links.aspx?type=vendor&part=1
[271] Thomas Milo. Decotype, Support for Authentic Arabic, 1998. http://diwww.epfl.ch/
w3lsp/conferences/ridt98/decotype.html
[272] Frank Mittelbach and Rainer Schöpf. A new font selection scheme for TEX macro packages — the basic macros. TUGboat, 10(2):222–238, 1989.
[273] Stanley Morison. Pacioli’s Classic Roman Alphabet. Dover, 1933, reprint 1994.
[274] Shigeki Moro. Surface or essence: beyond character model set. In Proceedings of the
Glyph and Typesetting Workshop, Kyoto, Japon, 2003. http://coe21.zinbun.kyoto-u.ac.
jp/ws-type-2003.html.en
[275] Morrison Soft Design. Font Doctor. http://www.morrisonsoftdesign.com/fd_mac.
html
[276] James Mosley and al. Le Romain du Roi. La typographie au service de l’État, 1702-2002.
Musée de l’imprimerie, 2002.
[277] Stephen Moye. Fontographer: Type by Design. Hungry Minds, 1995.
[278] Neuber Software GbR. Typograf. http://www.neuber.com/typograph/
[279] Han-Wen Nienhuys. mftrace. scalable PostScript fonts for METAFONT, 2003. http:
//www.xs4all.nl/~hanwen/mftrace/
[280] Nordsächsische Staats- und Universitätsbibliothek Göttingen. The Göttingen Gutenberg Bible. http://www.gutenbergdigital.de/gudi/eframes/
[281] Janusz M. Nowacki and Bogusław Jackowski. Antykwa Toru´nska: An electronic replica
of a Polish traditional type. TUGboat, 19(3):242–243, 1998.
```

```text
Bibliography
[282] Tobias Oetiker, Hubert Partl, Irene Hyna, and Elisabeth Schlegl. The Not So Short Introduction to LATEX2ε, or LATEX2ε in 138 minutes, 4.22 edition, 2007. http://www.ctan.org/
tex-archive/info/lshort/english/lshort.pdf
[283] Oscar Ogg. Three Classics of Italian Calligraphy: Arrighi, Tagliente, Palatino. Dover, 1953.
[284] P22 Type Foundry. P22 online, 2003. http://www.p22.com
[285] Keith Packard. pcf.h and pcfread.c, taken from X11 R6.4 source code, 1998. http:
//ftp.x.org/pub/
[286] Anshuman Pandey. Using the WSU International Phonetic Alphabet, 1992. http://
www.ctan.org/tex-archive/fonts/wsuipa/
[287] Minje Byeng-sen Park. Histoire de l’imprimerie coréenne des origines à 1910. Maisonneuve
& Larose, Paris, 2003.
[288] Tuomo Pekkanen, Reijo Pitkäranta, et al. Nuntii latini, 1999. http://www.yle.fi/
fbc/latini/index.html
[289] Georges Pérec. La disparition. Julliard, 1969.
[290] Georges Pérec. Les revenentes. Julliard, 1972.
[291] Georges Perec. A Void. Verba Mundi, 2005.
[292] Toby Phipps.
Unicode technical report #26. compatibility encoding scheme for
UTF-16: 8-Bit (CESU-8). Technical report, Unicode Consortium, 2002. http://www.
unicode.org/unicode/reports/tr26
[293] François Pinard. Free recode package, 1999. http://recode.progiciels-bpi.ca/
[294] Joerg Pommnitz.
ttmkfdir. http://freshmeat.net/projects/ttmkfdir/?topic_id=
[295] Man-Chi Pong 龐文治, Fung Fung Lee 李楓峰, Ricky Yeung 楊振富, and Yongguang
Zhang 張永光. Han character font sharing across incompatible bitmap file formats.
Technical Report HKUST-CS94-5, The Hong Kong University of Science and Technology, 1994. http://www.ibiblio.org/pub/packages/ccic/software/info/hbfa.html
[296] Man-Chi Pong 龐文治, Fung Fung Lee 李楓峰, Ricky Yeung 楊振富, and Yongguang
Zhang 張永光. Hanzi Bitmap Font (HBF) File Format Version 1.1, 1994. http://www.
ibiblio.org/pub/packages/ccic/software/info/HBF-1.1/
[297] René Ponot. Classification typographique. Communication et Langages, 81:40–54, 1989.
[298] Peter Prymmer. Perl and EBCDIC? The Perl Journal, 2(4), October 1997. http://www.
foo.be/docs/tpj/issues/vol2_4/tpj0204-0005.html
[299] Valerie Quercia and Tim O’Reilly. X Window System User’s Guide. O’Reilly, 1993. http:
//www.oreilly.com/catalog/v3m/
```

```text
Bibliography
[300] Erik T. Ray.
Learning XML.
O’Reilly, 2nd edition, 2003. http://www.oreilly.com/
catalog/learnxml2/index.html
[301] Red Hat.
Cygwin user’s guide, 2003. http://www.cygwin.com/cygwin-ug-net/
cygwin-ug-net.pdf.gz
[302] Fukui Rei.
TIPA: A system for processing phonetic symbols in LATEX.
TUGboat,
17(2):102–114, 1996.
[303] Glenn C. Reid. Thinking in PostScript. Addison-Wesley, 1990.
[304] Floyd Rogers. Win32 binary resource formats. Technical report, Microsoft, 1992. http:
//www.powerbasic.com/files/pub/docs/RESFMT.ZIP
[305] Tomas Rokicki. Packed font file format. TUGboat, 6(3):115–120, 1985.
[306] Tomas Rokicki. GFtoPK, v. 2.3, 1990. http://www.ctan.org/tex-archive/systems/
knuth/mfware/gftopk.web
[307] Guido van Rossum.
TTX, from OpenType to XML and back, 2001. http://
sourceforge.net/projects/fonttools/
[308] RSA Laboratories. PKCS-7: Cryptographic Message Syntax Standard, v. 1.5, 1993. ftp://
ftp.rsasecurity.com/pub/pkcs/ascii/pkcs-7.asc
[309] Geoffrey Sampson. Writing Systems. Stanford University Press, 1985.
[310] Ferdinand de Saussure and Roy Harris. Course in General Linguistics. London: Duckworth, 1983.
[311] John Sauter. Building Computer Modern Fonts. TUGboat, 7(3):151–152, 1986.
[312] Bob Scheifler and David Krikorian.
xset - User Preference Utility for X. http://www.
xfree86.org/4.3.0/xset.1.html
[313] Markus Scherer and Mark Davis.
Unicode Technical Note #6. BOCU-1: MIMECompatible Unicode Compression.
Technical report, Unicode Consortium, 2002.
http://www.unicode.org/notes/tn6/
[314] Walter Schmidt. The Computer Modern Bright family of fonts, 1998. http://www.
ctan.org/tex-archive/help/Catalogue/entries/cmbright.html
[315] Mícheál Ó Searcóid. The Irish alphabet. TUGboat, 12(1):139–148, 1991.
[316] Peter Selinger.
potrace. transforming bitmaps into vector graphics, 2003. http://
potrace.sourceforge.net
[317] Raymond Seroul and Silvio Levy. A Beginner’s Book of TEX. Springer, 1995.
[318] Ross Smith. Learning PostScript, a Visual Approach. Peachpit Press, 1990.
[319] Friedhelm Sowa.
bm2font, 1993. http://vega.rz.uni-duesseldorf.de/sowa/
bm2font/
```

```text
Bibliography
[320] Penny Spector. The interrobang: A twentieth century punctuation mark, 2001. http:
//www.interrobang-mks.com/
[321] Michael Spivak. The Joy of TEX: A Gourmet Guide to Typesetting With the AMS-TEX Macro
Package. American Mathematical Society, 2e edition, 1990.
[322] Siegfried H. Steinberg. Five Hundred Years of Printing. Oak Knoll Press, 1996.
[323] Sumner Stone. ITC Classics: ITC Bodoni. http://www.itcfonts.com/fonts/classics.
asp?nCo=AFMT&sec=fnt&art=bodoni
[324] Ralph R. Swick and Mark Leisher. xfontsel - Point and Click Selection of X11 Font Names.
X Consortium, 1989. http://www.xfree86.org/4.0.2/xfontsel.1.html
[325] Adobe Systems. OpenType feature file specification, v. 1.4, 2003. http://partners.
adobe.com/asn/tech/type/otfdk/techdocs/OTFeatureFileSyntax.jsp
[326] Péter Szabó. TEXtrace, 2001. http://www.inf.bme.hu/~pts/textrace/
[327] Hàn Th© Thành. Making type 1 fonts for Vietnamese. In Proceedings of the 24th Annual
TUG Meeting, Waikoloa, Hawai’i, 2003.
[328] Hán Thê Thánh.
Vietnamese TEX and LATEX support, 2000. http://www.ctan.org/
tex-archive/language/vietnamese/vntex/
[329] The Apache Software Foundation. Batik SVG Toolkit. http://xml.apache.org/batik/
index.html
[330] The FreeType Project. FreeType & patents, 2003. http://www.freetype.org/patents.
html
[331] Bhavani Thuraisingham. XML Databases and the Semantic Web. CRC Press, 1st edition,
2002. http://www.crcpress.com
[332] Geofroy Tory. Champ fleury. Au quel est contenu Lart & Science de la deue & vraye
Proportiõ des Lettres Attiques, quõ dit autrem˜et Lettres Antiques, & vulgairement Lettres Romaines proportionnees selon le Corps & Visage humain, 1529.
[333] Adam Twardoch and Andreas Eigendorf.
Unofficial FontLab 4.5 Python reference,
2003. http://dev.fontlab.net/flpydoc/
[334] Unicode Consortium.
Code charts (PDF version), 2006. http://www.unicode.org/
charts/
[335] Unicode Consortium. The Unicode Standard. Version 5.0. Addison Wesley, 5th edition,
2006. http://www.unicode.org/book/aboutbook.html
[336] Daniel B. Updike. Printing Types, their History, Forms, and Use. Harvard University Press,
2e edition, 1937.
[337] R. H. van Gent. Islamic-western calendar converter. http://www.phys.uu.nl/~vgent/
islam/islam_tabcal.htm
```

Bibliography [338] Just van Rossum and Erik van Blokland. Bleifrei!, 1992-2001. http://www.letterror. com/catalog/bleifrei/index.html [339] VeriSign. VeriSign digital ID for Microsoft Authenticode technology, 2000. ttps:// digitalid.verisign.com/developer/help/mscs_intro.htm [340] Michel Villandry. Brest, Ouessant. Parages, 2000. http://www.parages.ens.fr/n1/ 15.html [341] Vladimir Volovich. CM-Super font package, version 0.3.3, 2002. ftp://ftp.vsu.ru/ pub/tex/font-packs/cm-super/ [342] Maximilien Vox. Faisons le point. Larousse, 1963. [343] Larry Wall, Tom Christiansen, and Jon Orwant. Programming Perl. O’Reilly, 3e edition, 2000. [344] Martin Weber. AutoTrace. converts bitmap to vector graphics, 1998. http:// autotrace.sourceforge.net/ [345] Heinz Wendt. Sprachen. Fischer Taschenbuch Verlag, 1987. [346] Andrew West. BabelMap, 2002-2006. http://www.babelstone.co.uk/Software/ BabelMap.html [347] Ken Whistler and Mark Davis. Unicode technical report #17. character encoding model. Technical report, Unicode Consortium, 2000. http://www.unicode.org/ unicode/reports/tr17 [348] George Williams. PostScript font utilities, 2001. http://bibliofile.mc.duke.edu/ gww/FreeWare/MyToys.html [349] George Williams. Extensions to Adobe’s BDF for Greymap Fonts, 2002. http://pfaedit. sourceforge.net/BDFgrey.html [350] George Williams. Format for X11 PCF Bitmap Font Files, 2002. http://pfaedit. sourceforge.net/pcf-format.html [351] George Williams. Fondu – a set of programs to interconvert between Mac font formats and PFB, TTF, OTF and BDF files on unix, 2003. http://fondu.sourceforge.net/ [352] George Williams. PfaEdit, an outline font editor, 2003. http://pfaedit.sourceforge. net/overview.html [353] Misha Wolf, Ken Whistler, Charles Wicksteed, Mark Davis, Asmus Freytag, and Markus Scherer. Unicode Technical Report #6. a standard compression scheme for Unicode. Technical report, Unicode Consortium, 2003. http://www.unicode.org/ unicode/reports/tr6 [354] X Consortium. Bitmap Distribution Format, v. 2.1, 1997. ftp://ftp.x.org/pub/R6.6/ xc/doc/hardcopy/BDF/bdf.PS.gz

Bibliography [355] Shimon Yanai and Daniel M. Berry. Environment for translating METAFONT to PostScript. TUGboat, 11(4):525–541, 1990. [356] Candy Yiu, Wai Wong, and Kelvin Ng. Typesetting rare chinese characters in LATEX. TUGboat, 24(3):582–588, 2003. http://www.tug.org/TUGboat/Articles/ tb24-3/wong.pdf [357] Dimitar Zhekov. fontconv, 2003. http://www.is-vn.bg/hamster/jimmy-en.html [358] Maxim Zhukov. A Russian pangram, 2001. http://gmunch.home.pipeline.com/ typo-L/articles/tsitrus.html
