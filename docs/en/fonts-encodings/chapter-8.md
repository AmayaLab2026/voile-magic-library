---
title: "Chapter 8: Font Management under X Window"
description: "Unabridged English text: X11 logical font descriptors (XLFD), X font servers (XFS), modern client-side rendering with FreeType, Fontconfig, and Xft."
---

# Chapter 8: Font Management under X Window
**By Yannis Haralambous, Ph.D.**
*From Fonts & Encodings, pp. 221–234*

---

```text
But let us be clear on one point: while Mac OS and Windows had only two or three
bitmap fonts—relics from their infancy—in only two or three point sizes and with no
attempt at grandeur, X provides a sophisticated system for font classification, with a substitution mechanism that keeps us from ever running short of fonts. This system is called
XLFD (an unpronounceable acronym that stands for X Logical Font Description), and we
shall describe it below.
As for the notorious fragility of fonts under Mac OS and Windows, it stemmed primarily
from the fact that the files in question were left continuously open by the operating
system. Under X we use a font server named xfs (X Font Server). This server is also a font
manager, as it is capable of invoking fonts from a multitude of directories, even on other
machines. Applications thus send requests to the server, indicating the specifications of
the font desired, and the server replies by sending the requested font if it is available
or else, thanks to the substitution mechanism, the font that is most similar to the one
requested. Alternatively, applications can request a list of available fonts from the server
by specifying the characteristics requested by the user, who may then make his choice
from the list returned and obtain a single font.
Logical Description of a Font under X
Here is the problem that X developers posed to themselves. A given application needs
a certain amount of information to select a font. This information may be commercial
(foundry name), graphical (family name, weight, style, set width, point size, resolution
[in the case of a bitmap font]), or technical (the encoding). Usually we expect to find this
information in the font, or in a file accompanying the font, for every font that we have.
If we have thousands of fonts on our system,1 how can we avoid having to open them all
in order to collect this information?
The solution to these problems is to use a database containing the filenames and all this
other data, and that is what X does.
Next, these same developers set out to solve another problem, that of the classification
of fonts and interaction with the human user. It was necessary to create a syntax for describing fonts that would be both comprehensive (to cover all the information contained
in the database) and readable by a human (because a human, after all, had to select the
font). The solution that they devised is XLFD. It makes a number of compromises: XLFD
is not 100 percent comprehensive (and cannot be, since fonts exist in as much variety as
humans, if not even more) and also cannot be said to be staggeringly easy to use. But for
comprehensiveness we can always find a way to make do, and ease of use depends, at the
end of the day, on applications: after all, it is always possible to go through an ergonomic
and user-friendly user interface to interact with the font server and select a font.
1 Having merely installed Fedora (a rather popular Linux distribution) version 5, the author found himself with 2,464 (!) font files on his computer. But take note: under Unix, a font file contains only one point size
and in a single encoding. Conversely, under Mac OS and Windows, there are far fewer files, for two reasons:
first, the different point sizes of bitmaps are stored in the same file (and there is no need for them when the font
is a vector font); second, we often use not just one encoding but two: the standard encoding for the language
of the operating system and, if necessary, Unicode.
```

Logical Description of a Font under X
But let us first see how XLFD goes about classifying fonts [299, 138]. A font name, as defined by XLFD, is a series of 14 strings encoded in ISO 8859-1 and separated by hyphens.
These strings may not contain hyphens, asterisks, question marks, commas, or double
quotation marks. Here is an example of one such font name:
-misc-fixed-medium-r-normal------c--iso10646We shall see below that we can replace individual values, or even groups of values, in this
syntax with wildcards. But first let us describe the 14 fields that make up a font name. Of
these fields, some are “textual” (abbreviated ‘T’), in the sense that their value, as part
of the traditional name of the font, is not standardized, and others are “standardized”
(abbreviated ‘S’), taking predefined values.
1. The foundry name (T, which must be registered with the X Consortium), or a keyword such as misc, when the foundry is unknown or not registered, or when the
font is in the public domain. Unfortunately, this rule is not always observed, and
we come across fonts whose first field is arabic (the name of a script) or jis (the
name of an encoding).
2. The family name (T). Here we find the usual name of the font (times, helvetica,
courier, palatino, etc.). We also find, under Unix, a very special set of fonts, the
character-cell fonts.2 These are bitmap fonts in which all the glyphs are drawn on a
cell of pixels whose size is fixed. So simple are the shapes of the glyphs that these
fonts, the poorest of the poor, make no claim to belong to a classic font family: they
are rather named according to the dimensions of the cell, and we are quite content
if they are legible; their classification is not a significant issue. For example, we have
fonts called 5x7, 5x8, 6x9, 6x10, etc., up to 12x24 pixels. Most of these “anonymous”
fonts are lumped under the name fixed.
3. The weight (T), expressed with the usual English terms: light, regular, book, demi
bold, bold, black, etc.
4. The slant (S): r (roman), i (italic), o (oblique), ri (reverse italic, or letters that lean
to the left in a left-to-right script and to the right in a right-to-left script), ro (reverse
oblique), ot (other).
5. The set width (T), expressed with the usual English terms: normal, condensed, narrow,
double wide, etc.
6. The style (T), expressed with the usual English terms: serif, sans serif, informal,
decorated, etc.
7. The pixel size (S). In the case of the character-cell fonts, this number corresponds to
the height of the cell.
2 Yet another example of terminological confusion between character and glyph.

```text
8. The point size (S), in tenths of an American printer’s point (the American printer’s
point being 1/72.27 of an inch). It is the “optical size”, i.e., the size that the font’s
creator had in mind when he designed the font.
9. The horizontal resolution (S) of the screen or the printer for which the font is intended.
10. The vertical resolution (S) of the screen or the printer. Unlike the screens of Mac OS or
Windows, those of Unix may have pixels that are not square. It is therefore necessary
to provide appropriately adapted fonts in order to avoid the “Cinemascope” effect.
11. The type of spacing (S): p (“proportional”) for variable-width fonts, m for monospaced
fonts, c for character-cell fonts. The difference between a monospaced font and a
character-cell font is significant. In monospaced fonts, the offset between the glyph’s
point of origin and that of the following glyph remains unchanged; the glyph itself may lie partly or entirely outside the abstract box whose width corresponds to
this offset. In character-cell fonts, there is one additional property: the pixels of the
glyph, which are entirely contained within this abstract box. A character cell font is
monospaced a fortiori; the converse may not be true. Nonetheless, most monospaced
fonts (such as Courier or Computer Modern Typewriter) can be regarded as charactercell fonts, since they simulate the output of the typewriter, which was a source of
inspiration for the character-cell fonts.
12. The average width (S), in tenths of a pixel. This is the arithmetic mean of the widths
of all the glyphs in the font. In the cases of monospaced and character-cell fonts, it is
the actual width of the glyphs.
13. The primary indicator of the encoding (S). Here, unfortunately, confusion reigns between encodings for characters and encodings for glyphs. We have, for example,
iso8859 and iso10646 (encodings for characters) alongside adobe and dec (encodings of glyphs). We specify fontspecific for a font with an arbitrary encoding (as,
for example, with fonts of symbols).
14. The secondary indicator of the encoding (S). In the case of the ISO 8859 family of encodings, this is the number of the encoding: 1, ... , 15. In the case of the encoding
ISO 10646 (Unicode’s twin sibling), this is 1 (we hope that no 2 will ever arise). In
all other cases, the value depends greatly on the primary indicator of the encoding
so that we can obtain, for example, adobe-standard, dec-dectech, koi8-ru, and so
forth.
Here are a few examples of XLFD font names and the corresponding samples:
1. -misc-fixed-medium-r-normal--20-140-100-100-c-100-iso8859-1
```

Logical Description of a Font under X This font is unnamed (because it is marked misc) and is a character-cell font (spacing type c), with a cell size of 10x20, designed at an optical size of 14 points and for a screen of 100 points per inch. Its encoding is ISO 8859-1. 2. -urw-palatino-medium-r-normal--12-120-75-75-p-0-iso8859-2 The font Palatino from the foundry URW, designed at an optical size of 12 points and for a screen of 75 points per inch. Since it is a vector font, its average width is 0. Encoding: ISO 8859-2. 3. -b&h-lucidatypewriter-medium-r-normal-sans-25-180-100-100-n-150-iso10646-1 The monospaced version of the font Lucida Sans from the foundry Bigelow & Holmes, designed at an optical size of 18 points and for a screen of 100 points per inch. It is encoded in Unicode, but in reality it covers only a few Unicode tables (no Greek, no Cyrillic, no Hebrew, no Armenian, no mathematical symbols). 4. -jis-fixed-medium-r-normal--24-170-100-100-c-240-jisx0208.1983-0 A Japanese font in the Mincho 明朝tradition. It is unnamed (jis in the field for the foundry’s name) and is a character-cell font (spacing type c) with a cell size of 24x24 pixels. It was designed at an optical size of 17 points and a screen resolution of 100 pixels. Its encoding is JIS-X 208, which dates to 1983. In this example, we see two rows of kana syllables and two rows of some of the most common kanji ideographs. Note that this is only the first part of XLFD, the part that concerns font names. A second part, for font properties, goes further in defining a number of keyword–value pairs that describe the font in greater detail. These “properties” are stored in the font but are not used by most software during font selection. They are all optional, and we may add “private” properties.

```text
XLFD also provides a syntax for “polymorphic” fonts, i.e., fonts in which certain parameters can vary, a typical example being the Multiple Master fonts.
For more details on font properties and polymorphic fonts, the reader is referred to
[138].
In addition, the XLFD specification also includes two wildcard characters: * (representing
0, 1, or more characters of any kind) and ? (representing any single character), which we
can use as substitutes for any part of an XLFD font name.
Finally, let us have a quick foretaste of the tool xlsfonts, which will display a complete
list of all the available fonts. To filter this tool’s output, we can simply follow it with an
XLFD name containing wildcards. Here is an example:
xlsfonts "*palatino*"
In this syntax, it is important not to forget to enclose in quotation marks the string
containing wildcards; otherwise, the Unix shell will interpret the wildcards as parts of
a filename and will accordingly look for corresponding files before executing the command.
Installing fonts under X
Upon startup, the xfs font server [299, 233] reads a configuration file, which is:
/usr/X11R6/lib/X11/fs/config
by default. In this file we specify certain default values, such as the screen resolution and
the default set width. But most important of all: the file contains the list of directories
where fonts are stored. Here is an example:
/usr/X11R6/lib/X11/fonts/misc,
/usr/X11R6/lib/X11/fonts/Speedo,
/usr/X11R6/lib/X11/fonts/Type1,
/usr/X11R6/lib/X11/fonts/CID,
/usr/X11R6/lib/X11/fonts/75dpi,
/usr/X11R6/lib/X11/fonts/100dpi,
/usr/share/fonts/default/Type1,
/usr/share/fonts/default/TrueType,
/home/yannis/texmf/fonts/pfb
Each of these directories must contain a file named fonts.dir. This is a very simple text
file. It begins with the number of lines to follow, written on a line by itself. Then there
is a single line for each font file. These lines are divided into two columns: the filename
and the font’s XLFD name. Example:
```

Installing fonts under X
6x12.pcf.gz -misc-fixed-medium-r-semicondensed------c--iso106466x13.pcf.gz -misc-fixed-medium-r-semicondensed------c--iso106466x10.pcf.gz -misc-fixed-medium-r-normal------c--iso10646-
... (356 lines) ...
9x15-KOI8-R.pcf.gz -misc-fixed-medium-r-normal------c--koi8-r
or, in the case of PostScript Type 1 fonts:
UTRG____.pfa -adobe-utopia-medium-r-normal------p--iso8859UTI_____.pfa -adobe-utopia-medium-i-normal------p--iso8859UTB_____.pfa -adobe-utopia-bold-r-normal------p--iso8859-
... (85 lines) ...
l049036t.pfa -b&h-Luxi Serif-bold-i-normal------p--adobe-standard
To install fonts, therefore, we must place them into one of these directories and then
create or update the corresponding fonts.dir file. The fonts.dir files can be generated
by a certain number of tools, according to their format. We shall see the details below.
Aside from the XLFD font names, which by their nature are difficult to remember and
to write, we also have font-name aliases. These are defined in fonts.alias files, which are
also placed in the same directories. Once again, these are ASCII files with two columns,
the first column being the alias, the second being the XLFD font name. Here is an example:
utopia
-adobe-utopia-medium-r-normal------p--iso8859utopiaI -adobe-utopia-medium-i-normal------p--iso8859utopiaB -adobe-utopia-bold-r-normal------p--iso8859Finally, there is a third series of files that must be available to the server: encodings. These
are ASCII files of the following type:
STARTENCODING iso8859ALIAS tis620ALIAS tis620.2529ALIAS tis620.2533ALIAS tis620.2533STARTMAPPING unicode
UNDEFINE 0x7F 0xA0
0xA1 0x0E01
# THAI CHARACTER KO KAI
0xA2 0x0E02
# THAI CHARACTER KHO KHAI
0xA3 0x0E03
# THAI CHARACTER KHO KHUAT
0xA4 0x0E04
# THAI CHARACTER KHO KHWAI
... (85 lines) ...
ENDMAPPING
ENDENCODING

```text
We see in this illustration a line STARTENCODING (which also gives the name of the encoding), a number of aliases for the name of the encoding, and finally a table of mappings
to Unicode (STARTMAPPING ... ENDMAPPING), in which each line contains two columns:
the position in the font and the corresponding Unicode character. (What follows the
character # is nothing but a comment.)
The encodings are stored in the same way as the fonts: in encodings.dir files that contain one line per encoding, with the name of the encoding in the first column and the
corresponding file (which may be gzip-compressed) in the second column:
dec-special /usr/X11R6/lib/X11/fonts/encodings/dec-special.enc
ksxjohab- /usr/X11R6/lib/X11/fonts/encodings/large/ksc5601.1992-.enc.gz
... (43 lines) ...
iso8859- /usr/X11R6/lib/X11/fonts/encodings/iso8859-.enc
adobe-dingbats /usr/X11R6/lib/X11/fonts/encodings/adobe-dingbats.enc.gz
Note that the names of encodings must correspond to the last fields of the XLFD font
names.
Installing Bitmap Fonts
The bitmap format used by X is called “Bitmap Distribution Format” (BDF; see §A.4.2).
Bitmap fonts under X are files with the extension .bdf (the ASCII version of the BDF
format) or .pcf (the binary version of the same format; see §A.4.4). We can also find
files compressed by gzip: .pcf.gz. These are automatically decompressed by the server.
To install bitmap fonts, we can simply launch the utility mkfontdir within the directory
in question. It will create the required fonts.dir file. This procedure is quite simple
because usually BDF fonts already contain the XLFD font name; thus there is no need
to construct this name from various information contained within the font.
Once the current directory is equipped with its fonts.dir file, we can add it to the list
of directories in the configuration file by using the utility chkfontpath as follows:
chkfontpath -a /home/yannis/fonts/bitmap
Next, we can confirm that the directory in question has indeed been added to the configuration file, by executing
chkfontpath -l
We obtain a list of all the directories in the configuration file.
Finally, we need to load our new fonts into this directory in order to use them. To do so,
we can type:
xset +fp /home/yannis/fonts/bitmap
xset fp rehash
```

```text
Installing fonts under X
Here xset is a general-purpose application for configuration in X [299, 312]. The first argument, fp, on the command line indicates that we are concerned with fonts (fp = font
path). The + that precedes it on the first line indicates that the path in question should
go before all the other paths. This feature is useful because the server will use the first
instance of a specified font that it comes across. If the new fonts that we have just installed
have the same names as some old ones, this is their only chance to be read first and to
be chosen by the server.
The line xset fp rehash allows us to rebuild the tables in the database of the font server.
Only after this final operation do the fonts become available to all X clients.
Installing PostScript Type 1 or TrueType Fonts
Here things become more complicated, as the PostScript Type 1 fonts and the TrueType
fonts do not contain all of the information needed to create the XLFD font name, at least
not in a manner as direct as that of the BDF fonts. The method that we shall use, therefore, is the following:
First of all, using specialized tools (mentioned below), we shall create an intermediate
file called fonts.scale. Here is an extract of one such file:
UTRG____.pfa -adobe-utopia-medium-r-normal------p--iso8859UTI_____.pfa -adobe-utopia-medium-i-normal------p--iso8859UTB_____.pfa -adobe-utopia-bold-r-normal------p--iso8859UTBI____.pfa -adobe-utopia-bold-i-normal------p--iso8859cour.pfa -adobe-courier-medium-r-normal------m--iso8859cour.pfa -adobe-courier-medium-r-normal------m--iso8859cour.pfa -adobe-courier-medium-r-normal------m--iso8859cour.pfa -adobe-courier-medium-r-normal------m--iso8859-
... 77 lines of similar code ...
l049036t.pfa -b&h-Luxi Serif-bold-i-normal------p--iso8859l049036t.pfa -b&h-Luxi Serif-bold-i-normal------p--iso8859l049036t.pfa -b&h-Luxi Serif-bold-i-normal------p--iso8859l049036t.pfa -b&h-Luxi Serif-bold-i-normal------p--adobe-standard
Notice in the syntax shown above that the same PFA fonts can be used to cover multiple
character encodings, giving a separate XLFD entry for each.
Tools that create font.scale files include, for example, type1inst [243] for PostScript
Type 1 fonts and ttmkfdir [294] for TrueType fonts.
In view of some idiosyncrasies of these tools, certain precautions are in order. First, the
TrueType fonts should be separated from the PostScript Type 1 fonts, for two reasons:
each of these tools overwrites the fonts.scale generated by the other; also, type1inst
also attempts to analyze TrueType fonts but gives results inferior to those of ttmkfdir, and
confusion may ensue.
In the directory into which we have placed our PostScript Type 1 fonts, we will run:
```

```text
type1inst
possibly with the option -nogs to avoid creating a Fontmap file (which is a font catalog
for ghostscript). type1inst is a Perl script written by an Australian volunteer; it was last
updated in 1998, and it contains a number of gaps, notably with respect to encodings.
Specifically, of all the encodings that fonts may have, it recognizes only one: Adobe Standard, which it calls iso8859-1 (even though it has nothing to do with that encoding). In
all other cases, it writes adobe-fontspecific.
Thus it is absolutely necessary to edit the fonts.scale file a posteriori and to correct the
encodings (at least) in the XLFD font names before continuing.
In the directory containing the TrueType files, we run:
ttmkfdir > fonts.scale
possibly with the option --panose, if we are certain that the font contains a correct
Panose-1 classification. Unlike type1inst, this tool functions as a freetype library and manages to analyze fonts with much greater precision. Nevertheless, we are always wise to
inspect the fonts.scale file before continuing.
Also note the existence of mkfontscale [95], another relatively recent tool that can be
found on certain Unix distributions, which examines both PostScript Type 1 fonts and
TrueType fonts at the same time. Contrariwise, mkfontscale seems not to be suitable for
bitmap fonts.
Having generated the fonts.scale file, we launch (still in the same directory) mkfontdir,
specifying the directory containing the encodings.dir file:
mkfontdir -e /usr/X11R6/lib/X11/fonts/encodings
If several of these files are present on the system, we can use this option multiple times,
but it is more sensible to have a central encodings.dir file that contains all the encodings
used on the machine.
Afterwards, the remaining procedures are the same as for bitmap fonts. For instance, if
/home/yannis/fonts/ttf is the current directory, we type
chkfontpath -a /home/yannis/fonts/ttf
to add it to the configuration file on the server and
xset +fp /home/yannis/fonts/ttf
xset fp rehash
to fill it in and rebuild the internal tables in the file server’s database.
```

Tools for Managing Fonts under X
Figure 8-1: The interface of the application xfontsel.
Tools for Managing Fonts under X
The application xfontsel [324] allows us to choose a font name from the components of
its XLFD font name. For example, we have a line of text (Figure 8-2)
-fndry-fmly-wght-slant-aWdth-adstyl-...
...pxlsz-ptSz-resx-resy-spc-avgWdth-rgstry-encdng
that is nothing but a list of abbreviations of the names of XLFD’s fields. By clicking on
one of these abbreviated names, we obtain a contextual menu that shows all the possible choices for this XLFD field among all the available fonts. In the area in which this
line appears, the XLFD name is displayed. In the beginning, this name is nothing but a
sequence of * wildcards and thus represents all fonts.
When we select a value for an XLFD field, it is displayed in the XLFD font name in the
second line, and the possible choices for the other fields are reduced to those that are
compatible with the choices already made. Often there is only one choice, other than
the wildcard, on the contextual menu. We can thus fill in all the fields in the XLFD font
name and obtain the name of the unique font that matches our needs. Note that in the
upper right part of the window the phrase ... names match shows us how many fonts
that match our current choices exist. There must always be at least one, since xfontsel does
not allow us to specify values for the parameters that would not match any font. If we
click on the Select button, the selected font name is copied onto the clipboard and can
then be pasted into another window by a click on the mouse’s middle button.
Another tool, which lets us preview the installed fonts, is xfd [146]. It displays all the
glyphs in a given font, in units of 256 glyphs. Thus, if we write
xfd -fn "-misc-fixed-medium-r-normal------c--iso10646-" &
we can view the table of this font’s glyphs. In Figure 8-2 we see the first two of these tables:
0x00-0xff and 0x100-0x1ff. By clicking on a glyph, we obtain its position in the table
as well as its font-metric properties.

::: tip Typographical Specimen Plate (Figure 8-1)
![Figure 8-1: The xfontsel interface](/images/fonts-encodings/fig8-1-xfontsel-interface.png)
*Figure 8-1: The xfontsel interface.*
:::

![Figure 8-1: The xfontsel interface](/images/fonts-encodings/fig8-1-xfontsel-interface.png)
*Figure 8-1: The xfontsel interface.*

```text
Figure 8-2: Two tables of glyphs from the Unicode-encoded character-cell font 10x20, displayed
by xfd.
Tools for Converting Fonts under X
It is quite natural that a plethora of tools for converting one format to another has arisen
over time to contend with the multiplicity of font formats used under Unix. Of these we
shall mention some that are the most solid, the best documented, and the best supported
by their programmers. The reader will find vastly more through a simple Google search:
if ‘A’ and ‘B’ are names of font formats, search for A2B or AtoB. For example, a search for
“bdf2pcf” yielded 249 results, one for “bdftopcf” yielded 72,300.
The GNU Font Tools
This is a panoply of tools developed in 1992 by Karl Berry and Kathryn Hargreaves [77].
The goal is to perform auto-tracing on bitmap images to obtain their vector contours.
Today there are more powerful systems for this task (ScanFont, by FontLab; mftrace, by
Han-Wen Nienhuys; FontForge, by George Williams; etc.). But the individual GNU tools
may be of interest in their own right.
Karl Berry defined his own vector format, named BZR. It is a pivot format from which
the utility bzrto can generate METAFONT or PostScript Type 1 (in GSF format, a variant
of PFA that ghostscript uses) or PostScript Type 3. There is also a human-readable BZR
```

Tools for Converting Fonts under X format called BPL (in the fashion of TFM/PL, VF/VPL, etc.). We can convert BZR to BPL and vice versa wit the help of the tools bzrtobpl and bpltobzr. George Williams’s Tools George Williams, author of FontForge, which we shall describe at length in Chapters 12– 14, is a truly tireless person. He produced, alongside FontForge, a floppy disk of tools that handle practically all the situations that can arise when we share data between Unix and Mac OS X or Windows. For example, fondu [351] reads a set of Macintosh files and extracts all the fonts, be they PostScript (POST resource), TrueType (sfnt), bitmap (NFNT or FONT), or font-family resources (FOND). To manipulate Macintosh files containing resources under Unix, one must convert them to one of three formats: Macbinary (which “flattens” the data and resource parts), Binhex (which also converts everything to hexadecimal), or dfont (the equivalent of the Macintosh’s font suitcases under Mac OS X). There is also ufond, which performs the opposite operation: from a given Unix font, it generates a file that can be used under Mac OS 9 or Mac OS X, provided once again that it be converted to Macbinary or Binhex. Another series of tools [348] converts PFA fonts to PFB (pfa2pfb) and vice versa (pfb2pfa), generates BDF bitmaps from a PFA file (pfa2bdf), generates an AFM file from the descriptions of glyphs in a PFA file (pfa2afm), and decrypts the PostScript code in a PFA file (pfadecrypt). Next, he attacked the TTF fonts: showttf clearly displays the contents of all the TrueType or OpenType tables, and ttf2eps converts a glyph from a TTF font into an encapsulated PostScript file. Various other tools The t1utils were written by Lee Hetherington and revised by Eddie Kohler [175]. They support conversion from PFB to PFA (t1ascii) or vice versa (t1binary) and even complete decryption of the PostScript Type 1 binary code (t1disasm). Eddie Kohler [223] also added a handful of tools for the Multiple Master and OpenType fonts: mmafm and mmpfb produce Multiple Master font instances, and cfftot1 converts a CFF (Type 2) font to Type 1. Dieter Barron wrote ttftot42 [64], the only tool currently available for converting TrueType fonts to PostScript Type 42, which is essentially the same thing inside a PostScript wrapper. Converting Bitmap Fonts under Unix One very popular editor for bitmap fonts is XmBDFEd [232]. The unpronounceable acronym for this software comes from X Motif BDF Editor. It was developed by Mark Leisher. We shall not describe here its user interface for designing bitmap fonts. The

```text
reason that we have mentioned it here is that it is also a very powerful tool for font
conversion. Indeed, it can read the PK and GF formats of TEX (§A.5.2, A.5.3); HBF
(ideographic bitmap fonts), PSF (§A.4.1), and CP (§A.4.5), of Linux; FON and FNT, of
Windows (§A.3); and TrueType and TTC. It can only write PSF files.
Another tool for converting bitmap fonts under Unix is fontconv [357], by the Bulgarian
Dimitar Zharkov. This program reads and writes fonts in the RAW, PSF, and FNT formats
as well as in two more exotic ones: GRX (the native font format of the GRX graphical
library) and FNA (its human-readable version).
```

Fonts under TEX and Ω TEX and its successor Ω are the most sophisticated digital typography systems in the world. Thus it is understandable that font management on these systems is a little bit complex. In this chapter, we shall approach fonts from three points of view: 1. Their use in TEX and Ω: how we go about using fonts (already installed on the system) in TEX documents. 2. Their basic installation, i.e., with no special adaptation: how can the user who has just bought a beautiful font or downloaded one from the network install it on a TEX system for immediate use? 3. Their adaptation to the user’s needs: we quickly notice that the fonts that we buy or find on the network are merely raw material for us to adapt, mold, shape to fit our needs. For the well-versed typophile only! These three points of view correspond to this chapter’s three sections, each of which is more difficult and more technical than the one before it. Using Fonts in TEX Up to now we have examined operating systems: Mac OS, Windows, Unix. Is TEX also an operating system? No. But what is TEX, then? Born in 1978 at the prestigious Stanford University, brainchild of Donald Knuth, one of the greatest computer scientists of the twentieth century, TEX is, all in all, several things at once: a free software system for typesetting, a programming language, a syntax for writing mathematical formulae, a state of mind that often approaches religion... 1 1 A religion with, among other things, initiation rites, first and foremost being the correct pronunciation of “TEX”, which varies from language to language. In fact, the TEX logo is deceiving: it actually consists of
