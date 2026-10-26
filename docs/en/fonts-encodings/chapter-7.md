---
title: "Chapter 7: Font Management under Windows"
description: "Unabridged English text: Windows Fonts folder, GDI logical fonts (LOGFONT), registry management, ClearType subpixel rendering."
---

# Chapter 7: Font Management under Windows
**By Yannis Haralambous, Ph.D.**
*From Fonts & Encodings, pp. 209–220*

---

in fact, points to the directory c:\winnt\fonts, where all the fonts are stored. In Figure 7-1,
we see a screenshot of this directory under Windows XP. It is a very special type of directory, as the names of the icons are not filenames but rather the names of fonts in
Windows.
Among the icons seen in that window, several are marked with a red uppercase letter ‘A’.
These are bitmap fonts (with the extension .fon). In some cases (such as the Modern,
Roman, and Script fonts), they may be vector fonts in an arcane format called vector fonts
that is as old as the hills. It is a format that versions 1 and 2 of Windows used, much
like that of CAD systems such as AutoCAD, in which glyphs are built up of strokes, not
of filled-in shapes. These fonts are vestiges of the distant past that are condemned to
extinction.
The fonts whose icon bears a double ‘T’ are TrueType fonts, whose extension is .ttf.
Those whose icon contains an ‘O’ are usually OpenType fonts, but they may also be
simple TrueType fonts. Indeed, Microsoft meant for the extension .ttf to be used for
OpenType-TTF fonts and .otf for OpenType-CFF fonts; since one extension is clearly
insufficient for distinguishing TrueType fonts from OpenType-TTF, we may get the impression that the system assigns the icons at random.
The icons that contain a lowercase ‘a’ correspond to Type 1 PostScript fonts. Just as on
the Macintosh, here two files are required for each PostScript font: a file of font metrics,
whose extension is .pfm (= PostScript font metrics), and a file containing PostScript code,
whose extension is .pfb (= PostScript font binary, as opposed to .pfa = PostScript font ASCII,
which is most commonly found on Unix). The font-metrics file contains the information
needed by Windows, such as the Windows name, the widths of the characters, and the
kerning pairs, but also the font’s PostScript name.
As on the Macintosh, a PostScript or TrueType font may exist in as many as four styles:
“regular”, “bold”, “italic”, and “bold italic”.1 But unlike the Macintosh, here styles are not
assembled in a single file: each style is contained in a file of its own. To avoid creating an
excessively large number of icons for fonts, the Fonts window allows us to display only
one icon per “font family”, i.e., those that differ only in style: go to the View menu and
click on Hide Variations (Bold, Italic, etc.).
To install fonts, we can select Install New Font... under the File menu in the Fonts
window. The dialog box that appears displays a list of all the fonts contained in a given
directory. Once again, these are names of fonts that are displayed, not filenames—a very
practical outcome, because the filenames of Windows fonts, thanks to the former restriction of filenames to eight letters, are often quite cryptic, as, for example, bm______.ttf
for the splendid font Bembo. Next to the filename is the type of the file. At the lower right
part of the window is the checkbox Copy fonts to Fonts folder. This checkbox allows
us to choose between copying fonts into the c:\winnt\fonts folder and simply making
a reference to the existing files. In the latter case, only a link to the font in question is
1 In addition, this “style” of the font is stored in a variable in the table head that is called macStyle. But
in the table OS/2 there is another variable: fsSelection, which may also take the values “underscored”, “negative” (white on black), “contour”, “strikethrough”, and all their combinations. The specification gives rules for
compatibility between macStyle and fsSelection.

![Figure 7-1: Windows Fonts folder](/images/fonts-encodings/fig7-1-windows-fonts-folder.png)
*Figure 7-1: Windows Fonts folder.*

Figure 7-2: Dialog box for installing fonts.
created; these are the icons that have a little arrow at the lower left. Note that this link
is not an ordinary file: if we run dir at the Windows command prompt, these “links” do
not appear among the files.
Figure 7-3: List of fonts “by similarity”.
Also note that the View menu in this window has one very special entry: List Fonts By
Similarity. In this case, the Panose-1 classification of the fonts is used to categorize them
according to their similarity to a given font. We shall examine the Panose-1 classification
in Chapter 11 of this book. For the moment, let us simply say that Panose-1 allows us to
classify fonts according to their design in a 10-dimensional space; “similarity” is nothing
but the distance between two points in this space, points that represent two fonts. In
Figure 7-3, we can see the classification of fonts by their similarity to the font Linotype
Palatino; we discover that there are two fonts that are “very similar” to it, namely Georgia
and the font itself. Conversely, Times New Roman is merely “fairly similar” to Linotype
Palatino, and Arial is “not similar”. Nonetheless, the Panose-1 classification may be very
useful on the Web, as we shall see in the chapter dedicated to this subject (page 327). The
CSS specification incorporates the Panose description; thus the developer of a Web site

can add Panose characteristics to the explicit names of the fonts. The client’s system will
then be able to display the text in the font that is the most similar to the one requested.
Active fonts on Windows are exposed just as much to the risk of system crashes as they
are on the Macintosh, since they are files that are permanently kept open. Therefore we
are wise to verify our font files on a regular basis, to optimize their use by opening them
only when they are needed, and to take other protective measures. Next we shall present
a few tools for managing fonts under Windows.
Tools for Managing Fonts
The Extension of Font Properties
Let us begin with a tool that should ideally be part of the operating system. It is a little
utility called ttfext [257] that Microsoft provides free of charge. It is launched every time
we ask to see the properties of a TrueType or OpenType font. Its interface takes the form
of a window with tabs. It includes the classic General tab (which is also the only way to
determine the name of a given font) and adds nine others:
Figure 7-4: Two tabs of the Properties window of the font Linotype Palatino. Left: OpenType
properties. Right: a general description of the font.
• Embedding: can the font in question be embedded in a document? There are four
possibilities: Installable embedding allowed (the font can be embedded in a document
and can even be installed on the client’s system), Editable embedding allowed (the font

Tools for Managing Fonts
can be embedded in a document and can be used to edit text, but it can be only temporarily installed on the client’s machine), Print & Preview embedding allowed (the
font can be embedded in a document but can be used only for display and printing,
and it may be only temporarily installed), and Restricted license embedding (the font
may not be embedded in a document).
• CharSet/Unicode: what is the font’s default encoding? Which Unicode zones does the
font cover? Which other encodings are compatible with the font?
• Version, which also includes the date when the file was created and the date when it
was last modified.
• Hinting/Font Smoothing: does the font contain hinting, and at which point size should
the system begin to smooth the font through the use of pixels at different levels of
gray? A setting of the type O+ means “starting from 0 points”, i.e., at all sizes.
• Names: what are the names of the font, its font family, and its vendor? What are its
copyright and trademark?
• Features: a description of the font’s OpenType properties—for example, how many
glyphs it contains, whether it contains bitmaps, whether it contains a glyph for the
euro sign, whether it is a TTF or a CFF font—and a list of the scripts, languages, and
GSUB and GPOS tables covered by the font.
• Links: hypertext links pertaining to the foundry, the font’s designer, and the web site
of Microsoft’s typography department.
• Description: a document describing the font and its history and also providing the
name of its designer.
• License: a tab devoted to royalties, with a hypertext link to the full document that
describes them.
This tool provides easy access to the information that otherwise would have necessitated
converting the font into data readable by TTX or opening it with font-editing software
such as FontLab or FontForge. In both cases, we would need a good knowledge of the
tools and of the OpenType format in order to recover the information. The only negative
point about this tool: it abandons us altogether when the font is of PostScript Type 1.
Tools for Verification and Maintenance
The fact that operating systems crash is a law of Mother Nature. Since we cannot prevent
crashes, we should try to limit the extent of the damage by detecting corrupted fonts as
quickly as possible, before they cause new crashes themselves. On the other hand, when
we collect fonts from a wide variety of places, it may well happen that several fonts with
the same name will be open at the same time. That may also cause problems, especially if
the fonts are in differents formats. This situation frequently arises, since most foundries

Figure 7-5: Interface for configuring FontAgent, v.8.8.
simultaneously release their fonts in both traditional formats: PostScript Type 1 and
TrueType.
Fortunately, there are tools for detecting both corrupted fonts and duplicates. One such
tool is FontAgent, by Insider Software [189]. This program can do all of the following:
• Detecting and eliminating duplicates. We can specify whether we prefer the TrueType version or the PostScript Type 1 version. We can also retain fonts with the same
name if they come from different foundries.
• Detecting “orphaned” PostScript fonts (a .pfb without a .pfm or vice versa). Unlike
Font Doctor (under Mac OS), this program does not perform a “family reunion”:
when it finds a .pfb and its corresponding .pfm in different folders, it does not place
them in the same directory.
• Gathering fonts into a folder or a tree structure of folders organized by the first letter
of the font—or even a separate folder for each font (and these folders can bear a suffix
for the font format: “tt” or “t1”, for TrueType fonts and Type 1 fonts, respectively;
OpenType is not supported). We can also ask that only the strict minimum be left
in the Fonts system folder.
• Renaming font files. We can give them the name of the font itself (instead of a horrible abbreviation, as often occurs because of the restrictions on the length of filenames under MS-DOS). Of course, that assumes that the files are very well organized,
because we have even more chances to end up with duplicates.
• Removing corrupted files or duplicates by placing them in a special folder.

Tools for Managing Fonts
It is strongly recommended that the user save backups of all fonts before using FontAgent, since improper handling cannot be ruled out.
ATM: the “Smoother” of Fonts
Since Windows 2000, the smoothing of PostScript Type 1 glyphs has been performed
by the operating system, and Adobe Type Manager (ATM, whose Macintosh version we
described on page 196) is, in principle, no longer necessary. Indeed, when we install it under Windows 2000 or XP, its configuration interface offers the choice of only two folders
containing PostScript font files: one folder for .pfb and .otf files containing PostScript
code for Type 1 fonts and OpenType-CFF fonts, and one folder for .pfm and .mmm files containing Windows font metrics for Type 1 and Multiple Master fonts. (It should be noted
that Vista is not compatible with Adobe Type Manager.)
Figure 7-6: The interface for creating instances of Multiple Master fonts.
There is, however, a valid reason to install ATM under Windows 2000 or XP: it allows us
to create Multiple Master instances. The procedure is as follows (see Figure 7-6). When
we select a Multiple Master font, the different axes of variation are displayed in the form
of sliders. We can thus choose one value for each axis with the use of a little sample of text
that is transformed on the fly. Once we have chosen the values that we desire, we click
on Add, and a .pfm file representing this instance of the Multiple Master font is created
in the folder c:\psfonts\pfm, which is used by ATM only. At the same time, a link to this
file is created in the Fonts system folder.
Once the new instances have been created under ATM, they are available for use by all
applications. We can recognize them by the underscore character that separates the name
of the file from the values of the parameters. Thus in Figure 7-7 we are using the instance

Figure 7-7: Using Multiple Master font instances under WordPad.
bold 435, width 350, optical size 68 of the font Kepler MM Swash in the application
WordPad.
Note that we can also use Multiple Master fonts like ordinary Type 1 fonts under Windows 2000/XP, without going through the step of creating an instance; but in that case
we have access only to the default instance of each font.
Font Managers
We have seen how to solve the problem of corrupted and duplicate fonts and also how to
create Multiple Master font instances. The remaining question is how to manage active
fonts: how to find a practical method for enabling and disabling fonts without going
through the Fonts system folder—automatically, if possible, when we open a document
that requires a certain number of fonts that are available on the system but not necessarily enabled. And if we have a large number of fonts, we also need a practical system
for selecting the correct font (which implies creating catalogs of type specimens) and for
finding the corresponding files (which implies a database containing references to all the
fonts in our possession).
All these tasks are performed by font managers. Just as under Mac OS, there are two very
highly developed font managers and a number of tools that, while less sophisticated, may
be shareware or even freeware. The two “big” font managers are Font Reserve (Figure 7-8)
[119] and Suitcase (Figure 7-9) [132]—both from Extensis, now that Extensis has acquired
DiamondSoft, the company that produced Font Reserve.
In both cases, we select individual fonts or entire directories to be analyzed by the program, which will display them in the bottom part of the interface. Font Reserve enables
us to personalize the information displayed for each font; Suitcase, however, displays
only the name, the type, and the foundry. In both programs, we can create “sets” of fonts
in the top part of the window and add fonts to those sets by dragging them up from
the bottom part of the window or directly from a disk. We can thus enable or disable
individual fonts or families or sets of fonts by clicking on the button in the leftmost column. There are three possible states: disabled, temporarily enabled (until the computer
is rebooted or another font with the same name is enabled), and permanently enabled.

Tools for Managing Fonts
Figure 7-8: Font Reserve v.2.6.5.
For displaying font specimens, Suitcase has a vertical area that is permanently left open
and that can be customized; Font Reserve, on the other hand, displays a few glyphs when
one clicks on a font’s icon in the list of fonts and keeps the mouse button held down.
Both programs can display a certain amount of general information about a font. Font
Reserve also offers a rather powerful interface for searching for fonts (see Figure 7-10),
which can be quite useful when one needs to find one font among thousands.
The reader must surely have noticed that the Windows versions of these two programs
are, despite a handful of similarities, recognizably inferior to their Mac OS counterparts.
In particular, neither Suitcase nor Font Reserve supports the generation of catalogs of
font specimens.
Thus we have good reason to examine some tools other than these two font managers
inherited from the Macintosh. In fact, there is a profusion of such font managers (shareware or freeware), the most interesting of which is certainly Typograf (Figure 7-11) [278],
written by two Germans, the Neuber brothers.
Typograf supports, of course, the fundamental operations: viewing in various ways the installed fonts and fonts contained in various directories, as well as enabling and disabling
these fonts. It has a database that we can build up by searching through directories or
even entire CD-ROMs.
For each font, it presents an impressive range of information. We can read a very detailed description of the TrueType tables (Figure 7-11), view all the kerning pairs in the
font (using the font’s own glyphs), compare a certain number of fonts by viewing their

Figure 7-9: Suitcase v.9.2.2.
Figure 7-10: The font-search interface in Font Reserve v.2.6.5.
properties side by side, and print out specimens of one or more fonts by using any of a
dozen different models, whose text can be customized. It also supports classification of
fonts and searching for fonts according to their Panose data or their “IBM class”.
Font Servers
Suitcase Server, described in the section on Mac OS (page 204), also runs under Windows NT, 2000, and XP. Font servers can be very useful for fonts in the case of, for example, a team that has a large collection of fonts. They provide rapid searching through
the collection, immediate access to the selected font, and verification of compliance with
the law, if the number of licenses purchased for each font is specified. Their only disadvantage is that their prices are often prohibitive.

Tools for Font Conversion
Figure 7-11: The main interface and window for the properties of the font Arial, in Typograf
v.4.8f.
Tools for Font Conversion
We have already described several tools for font conversion in the chapter on Mac OS.
Among them, TransType Pro and FontFlasher also exist in Windows versions that are identical to their Macintosh versions in every detail. The reader is therefore referred back to
their descriptions under Mac OS X on pages 205 through 208 of this book.
There is, however, a competitor to TransType Pro: CrossFont, by the American company
Acute Systems, whose specialty is the conversion of data between the PC and the Macintosh.
CrossFont (Figure 7-13) offers almost the same features as TransType Pro for a fraction of
the price. It even goes further than TransType Pro, as it can also manage the dfont format
of the Macintosh and can generate missing files, such as the PFM file, when a font comes
from a Unix environment, or the AFM file, when we need kerning pairs for TEX, etc. One
very interesting property: it collects the kerning pairs from any available AFM files and
integrates them into the fonts generated during conversion.
But it also has its drawbacks: we cannot view the glyphs in a font to confirm that no glyph
was overlooked or incorrectly encoded, and Multiple Master fonts are not supported.
Both programs (TransType and CrossFont) are available in a demo version that is restricted only in the number of days for which it can be used. Thus one can test out their
full functionality before deciding which one to buy.

Figure 7-12: The interface of TransType Pro under Windows XP.
Figure 7-13: The interface of CrossFont v.4.1 under Windows XP.

Font Management
under X Window
Now that we have examined Mac OS and Windows (which are strikingly similar in the
area of fonts), let us move on to Unix, an operating system that used to be largely restricted to industry and universities but that is now becoming more and more popular,
thanks in particular to its free incarnations, such as Linux. While Mac OS 9 and Windows
do not separate the operating system from the windowing system, these two systems are
distinct in Mac OS X and Unix. The windowing system manages the operating system’s
graphical interface: windows, menus, dialog boxes, the mouse, etc. The windowing system of Mac OS X is called Quartz; that of Unix, X Window (“Window” is singular, without
an ‘s’) or, among intimates, X11 or even simply X.
Special Characteristics of X Window
First, we must point out that the overall ergonomic approach of Unix is based on the
use of a terminal. This may seem to be a disadvantage to those who are accustomed to a
completely graphical interface, such as that of Mac OS 9; however, to those who like to
“retain control” over their machine, it is rather an advantage. In any event, with regard to
fonts, the terminal is clearly less demanding than a graphical application. In particular,
since we tend to use only one font size at a time on a terminal, it is not surprising that
our good old-fashioned bitmap fonts (in the formats PSF, BDF, and PCF, etc.; see §A.4)
are quite adequate for the terminal’s needs and that font management under X is based
almost entirely on bitmap fonts—at least until recent times, when vector fonts finally
made their debut under X.
