---
title: "Chapter 12: Creating and Modifying Fonts"
description: "Unabridged English text: FontLab and FontForge workflows, cubic and quadratic Bézier curves, contour winding rules, metrics and class-based kerning."
---

# Chapter 12: Creating and Modifying Fonts
**By Yannis Haralambous, Ph.D.**
*From Fonts & Encodings, pp. 445–506*

---

```text
Editing and Creating Fonts
Now we come to the heart of this book: creating fonts. Need one be a Hermann Zapf or a
Jean François Porchez nowadays to create fonts? Of course not; otherwise there would be
no need for this book. But everything depends on what one wishes to do. If it is merely a
question of designing a missing symbol, a logo, or a new letter, one can merely start with
an existing font; in this case, a good knowledge of the software tool is probably more
important than artistic talent. If one wishes to create a font from a model, such as from
scans of printed pages, then knowledge of the tool must be wedded to a certain amount
of experience if one is to replace the “black marks of ink” that form the printed glyphs
with intelligent vector contours as efficiently as possible. Finally, if one wishes to create a
new font from scratch like the great typeface designers of the past five centuries, there is
an entire craft to master, either through a specialized school (an École de Beaux-Arts with
a typographic workshop or a specialized establishment such as the École Estienne, the
Scriptorium de Toulouse in France, or the University of Reading in the United Kingdom)
or through apprenticeship with a master designer, as is still done in the traditional crafts
that industrialization has not succeeded in eliminating.
Between these extremes, then, everything is a matter of degree. The goal of the following
three chapters is to give the reader a minimum of technical knowledge to enable her to
use the software tool efficiently and, perhaps, to have a critical look at the technical level
of existing fonts and avoid the traps that this type of artistic activity can fall into—traps
related to the very nature of typeface design. In this chapter, we shall examine the use
of two of the most widely used software tools for editing/creating fonts: FontLab and
FontForge. In Chapter 13 we shall discuss the optimization of the rendering of glyphs
through the use of PostScript hints or TrueType instructions. Finally, in Chapter 14, we
shall examine the advanced typographic features of OpenType and AAT.
```

Software for Editing/Creating Fonts
Over the past 20 years, at least six large-scale systems for creating fonts1 have been produced:
• The Ikarus system [207], written by Peter Karow starting in 1973, which was the first
industrial font-design system. Ikarus was acquired by a Dutch company (Dutch Type
Library), which modularized and extended it and which sells it today under the name
of DTL FontMaster [122].
• The METAFONT programming language of Donald Knuth (1978), which we shall
study in Appendix F.
• FontStudio, written by Ernie Brock and Harold Grey at Letraset. In the opinion of the
author, it has the best user interface of all font-design software. Designing glyphs with
this sytem is a true pleasure, and one can quickly produce excellent designs. It seems,
however, that fate has dealt a blow to this extraordinary software package: Letraset
sold it to Adobe, and Adobe condemned it to death through oblivion. Available only
for Mac OS 9, FontStudio (which the author had the privilege of buying in 1990,
before it was withdrawn from the market) can handle only PostScript Type 1 fonts.
Those readers who manage to buy a copy can use it to create glyphs under Mac OS
Classic. Afterwards, they will have to use other software to generate modern fonts
from the glyphs that they have designed with FontStudio. In any event, even though
the chances may seem remote, we can hope that a future head of Adobe will fall
passionately in love with this software and will decide to undertake the investment
needed to resurrect it—to the great profit of humanity!
• Macromedia’s Fontographer [277, 244], developed by Jim von Ehr and his team when
he was still at Altsys and released in 1985. This software is without a doubt the bestknown font-design software in the world. It ran only under Mac OS 9 and Windows
until in 2005 the program was bought by FontLab and a Mac OS X version released.
Its interface is quite poor compared to that of FontStudio, but it is quite solid and
produces fonts that are relatively decent, at least typographically. Although Macromedia still sells Fontographer at its web site, this software is also on the road to extinction, as it has not been updated for years and thus cannot possibly produce OpenType or AAT fonts. Moreover, Fontographer is not compatible with Mac OS X, even
in the Classic environment. The Dutch firm Leterror tried to save this software by
injecting Python scripts into it: the result was called Robofog [235], doubtless because
its operation can be compared to the “robotization” of policeman Alex Murphy in
the American TV series RoboCop—“fog” being not the word for the meteorological
phenomenon but the Fontographer file extension. Robofog in turn died out during
the shift to Mac OS X, and the same firm is now offering a new product: RoboLab,
based on FontLab.
1 In 1987 there was a conference on font-design systems [40] at Sophia-Antipolis, France. The reader will
find in its published proceedings a description of numerous other systems.

Figure 12-1: The font window of Macromedia Fontographer, under Mac OS X. Figure 12-2: The glyph window of Letraset FontStudio, under Mac OS 9.

• FontLab [140], written by Yuri Yarmola and Vadim Suvorov, which today is the most
widespread system, thanks in particular to its rapid response to new technologies.
FontLab runs under Mac OS 9/X and Windows. It can handle fonts containing as
many as 6,400 glyphs; if more are needed, as is the case when one wishes to set type in
Japanese, Chinese, or Korean, one must purchase the “East Asian” version of FontLab, which is called AsiaFont Studio, for a price four times higher than that of FontLab (!).
• Last but not least, FontForge [352] (formerly called PfaEdit), by George Williams,
which is a real miracle: it is an extremely powerful software system offering practically all the features of FontLab, together with some unique and often revolutionary
features of its own. This software, which “plays in the big leagues”, is free, and, what is
most astonishing of all, it was developed by a single person, our dear George Williams,
an indefatigable worker who is always ready to improve his software even more every
time the opportunity arises!
In the following material, we have decided to describe only the last two of these software
packages, FontLab and FontForge, since FontStudio is now but a “remembrance of things
past”, Fontographer just has awakened from a deep coma, and DTL FontMaster is certainly
excellent but is of little interest because it costs a great deal and is little known to the
general public. On the other hand, we have dedicated an appendix to the study of the
METAFONT programming language.
We shall also discuss some systems that automatically trace glyphs, such as ScanFont (by
FontLab) and autotrace and potrace (in the public domain).
General Principles
Most of the software systems mentioned above have the same interface architecture: a
font is represented in the form of a table containing glyphs (see, for example, Figure 12-1,
which shows a Fontographer window). Each glyph is represented by a square in the table
and has a caption that can be a number, a name, or another type of information. The
order of the glyphs in the table may be that of a given encoding or the natural order of
the descriptions of the glyphs in the font.
Double-clicking on the glyph in the font window opens a glyph-editing window (see, for example, Figure 12-2, generated under FontStudio). The tools available at this level are quite
similar to those for producing vector graphics, such as Illustrator, Freehand, CorelDraw,
etc., with a few small differences: first, black is the only color allowed; second, we are
certainly free to draw curves, but they always have a zero thickness and are used only to
form surfaces; third, there are some constraints on what we can draw, such as the fact that
the tangent lines at the initial points of Bézier curves should be horizontal or vertical,
which calls for special tools that can ensure that they meet this constraint. Finally, we
are concerned here with small details such as the direction in which a curve is drawn,
the sequential numbers of the points on the Bézier curves, etc.—details that seem silly
when graphic design software is used but that can be quite useful in the context of font
design.

The challenge of the glyph-editing window is to show simultaneously as much data
about the glyph as possible. These data are related to the various steps in the process of
font creation. Among them are:
• The point of origin, the baseline, the side bearings, and various horizontal and vertical zones that serve to maintain the same dimensions (the heights of the capitals,
the ascenders, and the lowercase letters, the depths of the descenders, etc.)
• The baseline and the left and right side bearings for each glyph written in a direction
other than the primary direction for the font
• The glyph’s contour, with the starting and ending points of the Bézier curves, the
control points, information about whether a point at which two Bézier curves meet
is an angular or a smooth connection, the direction of the Bézier curves, etc.
• PostScript hints or TrueType instructions
• OpenType anchors
• Any models that were used to create the glyph, whether these models be vectorbased (and therefore contours put onto a second plane that will not be part of the
final glyph) or bitmap (and therefore background images)
• In the case of a Multiple Master font, all the master designs of the glyph in question,
with their hints, their anchors, etc.
• Other design aids, as, for example, grids in the background
That is a great deal of information to display, and often we feel overwhelmed by it. Thus
one of the greatest difficulties of learning a font-design system is without a doubt the
excess and great variety of visual information.
The tools for manipulating the data in question will themselves necessarily be quite diverse as well: for tracing curves, we need a whole panoply of vector design tools (tracing,
cutting, pasting, aligning, bending, turning horizontal or vertical, etc.). Magnetism is a
very popular technique: when we approach a point, that point changes color and thus
lets us know that by clicking on it we will be able to select it, even if the mouse’s cursor
is not exactly above the point. This technique allows us to “capture” points more easily,
but it can create a serious problem when several points are close together.
But the special features of the font-design systems are not limited to these two windows.
After all, let us not forget that glyphs are sociable animals: they love to come together,
interact, and jointly form a social fabric that we call “text”. Accordingly, the software
must also be able to determine their social behavior.
The most fundamental interaction is kerning: the software must allow the user to indicate, whether automatically or manually, the kerning of two glyphs, the similarity of
glyphs’ behavior with respect to kerning (for example, ‘É’ is kerned just like ‘E’), etc.

```text
Next, the software must support the introduction of OpenType, and even AAT, features
into our fonts. That is more easily said than done, and today’s software supports only a
few of these features, and ofter poorly at that.
Finally, beyond the encoding and the descriptions of the glyphs, there is another type of
information in a font: global data. This includes global metric data, the different names
of the font, the designer’s name, the license, the Panose classification, etc. The software
must allow the user to insert this data into the font. That may seem easy, but once again
there is a challenge: the data turn out to be quite numerous. The different font formats
(PostScript, TrueType, OpenType, AAT) and the different platforms (DOS, Windows,
OS/2, Macintosh, Unix) have accumulated such bulk of various and sundry data that a
designer can often find it hard to remember the meaning, syntax, and, most of all, importance of each type. The software must help him to complete this task with a minimum of
effort by supplying to him the most important data, insisting that he fill in the essential
data, and leaving aside (or automatically filling in) any data that is optional.
FontLab
Rest assured, dear reader: we make no claim here of describing the use of FontLab in
every detail. After all, this software has a rather large (923 pages!) set of documentation
[141] that is very well written and illustrated and also freely accessible. Instead, we shall
attempt in this section to understand this software package’s philosophy and to describe
certain major operations that the font designer uses every day.
The Font Window
The font window in FontLab plays a dual role: on the one hand, it displays the glyphs
accompanied by some data that make it possible to identify them; on the other hand, it
determines the encoding of the PostScript or TrueType fonts that will be generated.
To complete this task, the font window has four pull-down menus: one menu for specifying the size of glyph display in the table, one concerning the textual information
displayed above the glyph in the table, one for specifying the order in which glyphs are
displayed in the table and a fourth menu which complements the third one.
To understand the fine points of these tools, recall the principle of a font encoding. A font
encoding—not to be confused with a character encoding—is a correspondence between
numbers (called “code points”) and glyph descriptions. But how can we identify the description of a given glyph in a font? That is where the complications arise.
In a PostScript Type 1 or CFF font, glyph descriptions are provided with names, the
PostScript glyph names (§C.3.5). A PostScript font encoding is therefore, in reality, a
correspondence between numbers and glyph names. In the beginning, in the years
1986 through 1992, the names themselves had no importance, since what mattered was
the code point of the glyph within the table and the glyph’s description; the name was
merely a vehicle for going from one to the other. But these names took on importance
when Acrobat was released, as Adobe began to use them to find the Unicode characters
```

FontLab
to which the glyphs corresponded. Thus Adobe defined a standard syntax for naming
glyphs (§C.3.3). When this syntax is respected, Acrobat is able to associate the glyphs
in question with Unicode characters and thus to interact with the user who wishes to
search for strings, copy them, index them, etc., within PDF files.
This problem never existed for TrueType fonts: after all, the names of the glyphs in these
fonts are not required (they are sometimes included in the post table—§D.4.8—for use
when the font is converted to PostScript), and there is always a cmap table (§D.4.2), which
gives the explicit correspondence between characters and glyphs.
Just as in democracies a president is expected to rise above party politics, FontLab also
claims to be impartial with regard to the differences between PostScript and TrueType;
accordingly, it opts for a pluralistic approach—we have not only one way to represent a
font encoding but at least three (!), listed here in Figure 12-3:
Figure 12-3: The Names mode of the FontLab font window.
• Using the third pull-down menu on the bottom bar of the font window, we select the
Names mode. The fourth pull-down menu gives us then access to a large number
of font encodings, which are all defined by means of glyph names. Each of these
encodings is described in a text file with the extension .enc; on the Mac these files
are kept in subdirectories of /Library/Application Support/FontLab/Encoding.
In these files one finds first the names of the encoding and of its group as displayed
in the pull-down menu:
%%FONTLAB ENCODING: 1; Default Encoding
%%GROUP:Type 1 Western/Roman

(the number 1; in front of Default
Encoding giving the order of display in the
menu) and then a large number of lines of of the following type:
Eacute 131
which means that the glyph named Eacute is stored at decimal code point 131 in the
table.
Figure 12-4: The Pages mode of the FontLab font window.
• By selecting the Pages mode, shown in Figure 12-4, we switch to a mode that we
could also call the “mode for character encodings other than Unicode”. The pull-down
menu in the middle offers us a quite large number of character encodings.
The reader may be wondering what the difference is between this choice and the
previous one. Indeed, it is a subtle difference. Each glyph in FontLab always has two
pieces of data associated with it: its name and the Unicode character with which it
is associated. When a font is imported, FontLab tries to obtain these data from the
font tables. And whatever FontLab cannot obtain from the font it tries to guess, as
well as it can.
The two modes correspond to these two pieces of data: while in Names mode the
glyphs are arranged according to their glyph names, in Pages mode they are arranged
according to their associated Unicode characters.

FontLab
Each encoding on the pull-down menu corresponds to a file with the extension .cpg
that, on the Mac, is stored in subdirectories of /Library/Application
Support/FontLab/Codepage. These files are of the following type:
%%FONTLAB CODEPAGE: 0xff; MacOS Roman
%%GROUP:MacOS
...
0x83
0x00C9
% LATIN CAPITAL LETTER E WITH ACUTE
which means that the glyph associated with the Unicode character 0x00C9 latin
capital letter e with acute is placed at hexadecimal code point 83 (therefore decimal 131). The concrete result will be more or less the same as in glyph name mode: in
both cases we have a font (or character) encoding called MacRoman, and a font stored
in this encoding will be slightly different in each of the two modes, but most of the
glyphs will be in the same place.
What reason, then, is there to choose one approach over the other? Everything depends on context. We can ask ourselves a few questions. What is the origin of the
names of the glyphs in the font that we are importing? Where will we find the correspondences with the Unicode characters? The answers to these questions will help
us to select the most reliable approach.
In addition, when used together, these two approaches give us a very robust way
to make sure that our glyph names and correspondences with Unicode characters
are correct. All that we have to do is select the Pages mode and Names mode
approaches in turn and see which glyphs change when we go from one approach to
the other. Those are the glyphs that will need special attention.
One final argument: if the font that we are going to create will be of TrueType format,
the correspondences with the Unicode characters are more important than the glyph
names. If it is to be a PostScript font, the opposite is true. But beware: making sure
that both sets of data are correct is the best solution.
• By selecting Ranges mode (Figure 12-5), we switch to “Unicode” mode, which, in
the author’s opinion, is the only mode that is really interesting.
Here the font window shows us, one by one, all of the tables in Unicode, which we
can select from the pull-down menu. For each table, FontLab first displays (on a yellow background) the glyphs corresponding to the characters in the table, and then,
on a gray background, all the other glyphs. That allows us to do our work properly,
always being aware of the active context.
• Finally, by selecting Index mode (Figure 12-6), we switch to “index” mode.
The “indexes” are simply the sequential numbers of the glyphs’ descriptions. There
is nothing more natural and, at the same time, more haphazard: since the glyphs
are described within the file, their descriptions necessarily fall into a certain physical
order (the order in which they appear in the code), but that order does not affect the
use of the font in any way: in PostScript fonts, we specify glyphs by means of their
names; in TrueType, we specify them through the loca table—itself used by the cmap

Figure 12-5: The Ranges mode of the FontLab font window. table, which acts as a pivot between characters and glyphs. The index mode serves to give a general view of all the glyphs in the font, without gaps and without any risk that some glyphs may go undetected because their code points are too far away in the table. Note that the choice of Names mode or Pages mode will affect the PostScript or TrueType font that is generated. Things are less clear in Ranges mode or Index mode mode, and we advise the reader to check the encoding of the generated font by inspecting the AFM file (for PostScript fonts) or through the use of TTX (for TrueType fonts). One last comment to conclude the issue of encodings: when we select an encoding in Names mode or in Pages mode, we change only the positions of the glyphs in the table. In other words, the data for the individual glyphs (contours, names, Unicode correspondences, etc.) do not change one iota. But there is also a more radical way to modify the font’s table: “re-encoding”. The name of this operation is rather poorly chosen: when we move, for example, from one code page to another, we also “re-encode” the font—whereas here the operation is much more radical, even brutal. When we select Glyphs>Glyph Names>Reencode Glyphs, FontLab will take the glyphs in their current positions and regard them from that point on as being glyphs in a

```text
FontLab
Figure 12-6: The Index mode of the FontLab font window.
certain font encoding that we will specify. The glyph names and the Unicode correspondences already established are simply disregaded: everything is flattened, and nothing is
left but the new encoding, with its own names and correspondences. This radical method
is very useful, but it must be employed with caution: first, we choose the correct code
page; then we verify that the glyph contours do indeed correspond to the names and
code points specified (and make any necessary changes); finally, we call for the font to
be “re-encoded” for this encoding. The effect of the operation should not be dramatic: it
is rather a consolidation and a reinitialization of the glyph names according to the proper
conventions.
The more dramatic use of this operation is that of rectifying the glyphs’ names and the
Unicode correspondences for non-Latin fonts that have been encoded as if they were
Latin fonts: there is, unfortunately, a plethora of Russian, Greek, Arabic, and other fonts
in which the letters have names as appropriate as Eacute and lozenge. If the order of the
glyphs, despite the poor choice of names, is nonetheless that of a recognized encoding—
and the chances of that are good if the font has been used before under an operating
system—, then we may simply request “re-encoding”, taking care to check the result very
carefully for any errors. The best way to check that the glyphs have been interpreted
correctly is to switch to Unicode mode and to check, table by table, that everything is
where it belongs.
Regardless of the way in which we have chosen to arrange the glyphs, the font window
offers us nine (!) different ways to label them:
Specifically, by their names (the default choice), by the corresponding Unicode character,
by their indexes (i.e., the sequential numbers of their glyph descriptions), by their set-
```

```text
widths, by their left and right side-bearings, by their code-point numbers (in decimal,
hexadecimal, or octal), by the corresponding character in the ANSI encoding, and by
any data generated by a Python macro. We can also color the boxes to facilitate their
identification: that is done by selecting the glyphs and choosing Mark followed by the
color (red, blue, green, magenta, cyan, or a custom value) on their contextual menu.
Finally, to wrap up the discussion of the font window, there is a pull-down menu at the
lower right that enables us to enlarge or reduce the size of its glyph cells, from 16×16 to
128×128 pixels, 32×32 being the default value.
Opening and Saving a Font
We can open PostScript Type 1, Multiple Master, TrueType, and OpenType fonts, as well
as fonts in the FontLab format (VFA or VFB) and in Ikarus format (IK extension).
We can set some preferences for opening fonts in the Preferences panel. For PostScript
fonts, these are Decompose all composite glyphs, i.e., replace the composite glyphs
with genuine contours; Generate Unicode indices for all glyphs, a must; Generate
basic OpenType features for Type 1 fonts with Standard encoding, a very useful
feature for easily obtaining “intelligent” OpenType fonts; Find matching encoding
table if possible, which means that FontLab will try to identify the encoding as being
one listed on the pull-down menu, otherwise it will call it Imported.
For TrueType fonts, these are Convert TrueType curves into PostScript curves;
Store TrueType native hinting; Import embedded bitmaps; Autohint font,
which means “throw away the existing hints or instructions and create new ones on the
fly”; Scale the font to 1000 UPM, i.e., change the coordinate grid and switch from
2,048 units to 1,000, as for PostScript fonts; Decompose composites; Store custom
TrueType/OpenType tables i.e. preserve TrueType tables that are not recognized by
FontLab (such as AAT, VTT, VOLT, or Graphite tables); how to deal with name records
(import them or do not—and there is also the politically incorrect choice of importing
only English ones).
For OpenType fonts there are six other options: read the OpenType tables GPOS, GSUB,
GDEF; store them in the font; interpret them; deduce kerning from the kern table; Generate missing glyph names using layout tables which means that glyphs that
are not directly accessible through the cmap table and hence have no corresponding Unicode character(s) will nevertheless get automatically generated names; and, finally, an
option that gives at least a soupçon of rehabilitation to the AAT tables, which have been
so unjustly ignored—the conversion of mort and morx tables to OpenType tables (see
Appendix D.13.2).
Many options are offered for saving fonts, with the goal of adapting the generated fonts
to the user’s needs: platform, encoding, file format, etc. FontLab’s proprietary format is
VFB: this is the format in which fonts are saved when we use File>Save or File>Save as.
To obtain a Unix, Windows, or Mac OS X font, we use Files>Generate Font. Then we
have the choice of the formats TTF (called Win TrueType/OpenType TT), OTF (called
through a second dialog window, OpenType PS), PFB (Win Type 1), PFA (ASCII/Unix
```

```text
FontLab
Type 1) and VFB (FontLab native format).2 For each type of font, we again have special
options. For instance, when generating PostScript fonts, we can choose, through a second
dialog window, to preserve the original encoding of the font or to convert universally to
Adobe Standard Encoding.
Going through the Preferences panel, we can also choose to generate PFM (font-metric
data for Windows), AFM, or INF files; to export only glyphs appearing in the encoding;
to autohint the font; to generate bitmaps using a specific rasterizer; etc.
For TrueType fonts we have the choice of including instructions; preserving the original
instructions; creating instructions for glyphs that lack them; and creating instructions
from “visual instructions”, i.e., those inserted by hand within FontLab; export a mort
table; generate a digital signature; etc. We can also decide whether or not to export TrueType bitmaps.
Finally, for OpenType fonts, we can choose to export OpenType tables or not; to export
custom tables; to export VOLT data (in order to lead VOLT to believe that it is the only
software that has edited the font); to add an OpenType property kern (rather than a kern
table); to export the strings in the name table or not, or to export only those in English;
to produce a GDEF table; to use subroutines to reduce the size of the CFF code; etc.
Which options should we select when we generate a font? According to the principle
of “whoever can do more can also do less”, the creation of VOLT data, GDEF tables, kern
properties, CFF subroutines, etc., should not bother anyone; thus we can include them
in our fonts without worries. Unless, of course, we come upon bizarre software that accepts some of the OpenType features but that is allergic to the rest. In that case, it would
behoove us to be selective and to include in our fonts only the data that will not bother
the software in question.
As for TrueType instructions, we must choose a strategy, and it depends on context. Was
the font that we are opening meticulously instructed by specialists (like Microsoft’s font
Arial)? Or was it automatically instructed by software of lower quality than FontLab
(such as Fontographer)? In the former case, it would behoove us to preserve the instructions during both opening and saving, with perhaps some additional instructions for the
glyphs that have been added or modified. As for “visual instructions”, they are a “lite”
version of TrueType instructions that has the benefit of taking advantage of FontLab’s
very seductive graphical interface. Upon exporting a font, FontLab will convert these
instructions into genuine TrueType instructions.
Finally, an option for exporting that is both interesting and dangerous: when we select
the option Open Type 1 Export Terminal, FontLab shows us an editing window
containing the beginning (public and private dictionaries) of the Type 1 font, in plain
text. We may then modify these dictionaries by hand. It is obvious that the slightest error
in the code will render the font useless—so use this option in moderation!
2 In previous versions of FontLab the type 42 output format (Unix Type 42 (Raw ASCII)) was also
provided. This is really a pity because type 42 allows us to send TrueType fonts to a PostScript device without
first converting their outlines and hints to PostScript.
```

To generate Mac OS 9 fonts (under FontLab Macintosh), we use File>Generate Mac
Suitcase. Since the Macintosh font suitcases are an endangered species, we shall not go
into detail about the various options available. It is enough to know that the window
that opens allows the four font “styles” used under Mac OS 9 to be selected in a very
convient manner: plain, italic, bold, bold italic. We select the PostScript or TrueType
fonts corresponding to these four styles, and FontLab produces a suitcase with pointers
to these four fonts. The names specified in this dialog box are “Quickdraw names”, i.e.,
the names used on the Macintosh’s menus to represent the fonts in question.
The General-Information Window
This window is opened with File>Font Info. It contains no fewer than 34 (!) tabs arranged in nine groups. Here are the most important of these tabs:
• Names and Copyright (see Figure 12-7 [a]): the different “names” of the font; i.e.,
the name of the family, the weight, and the set-width; the name of the “style” (which
is added to a PostScript family name to create a font name), the “technical” (without whitespaces) name of the font used in PostScript language calls, the “full name”
(used in PostScript fonts), the Quickdraw name (which appears on the Macintosh’s
menus), the name contained in any Macintosh FOND resource. Often it is sufficient
to enter the family name and the style name and click on the button Build Names:
FontLab will then fill in the other boxes automatically. Note that Family Name under this tab corresponds to entry 1 in the name table (Appendix D.4.6); Style Name,
to entry 2; PS Font Name, to entry 6; and Full Name to entry 4.
• OpenType-specific names: under this tab, we find entries 16 (OT Family Name)
and 17 (OT Style Name) from the name table.
• One may ask why FontLab presents us with a few sporadic entries from the name
table under the tabs discussed above instead of giving us an efficient way to gain
access to the entire table. That feature is offered under the following tab: Additional
OpenType names (see Figure 12-7 [b]). The first button collects the data from the other
tabs and inserts them into the present one. Then we can add new entries or modify
the existing ones by choosing the entry number, the system, the encoding, and the
language (Appendix D.4.6), again through the use of pull-down menus. In the Text
field, we can include Unicode characters by using the syntax \ABCD: to obtain 漢字,
we write \6F22\5B57.
• Copyright information (see Figure 12-7 (c)): while the previous tab showed us the
entire name table, this one again shows only certain entries in the table, and only in
English: the copyright (entry 0 in the name table), the trademark (entry 7), and the
description (entry 10).
• Embedding: may this font be embedded in a PDF file or any other type of file?
Under what conditions? This information comes from the contents of the fsType
field in the OS/2 table, which, unlike what one would expect from its name, is not
limited to the OS/2 operating system but also covers Windows (Appendix D.4.7).

FontLab (a) (b) (c) Figure 12-7: The tabs Names and Copyright, Additional OpenType names, and Copyright information.

• Designer information: entries 9, 12, and 11 from the name table—the designer’s
name, her URL, and the URL of the foundry.
• License information: entries 13 and 14 from the name table—a description of the
license and a URL giving more information.
• Version and Identification: the version number (base version and revision), entry 5 of the name table.
• Identification settings: the unique ID record of a TrueType font, the unique identifier of a Type 1 font (UID), the extended identifier (XUID), the TrueType vendor
code (contained in the achVendID entry of the OS/2 table, Appendix D.4.7).
• Panose identification: Panose-1 identifier (see Chapter 11).
• IBM and MS identification: the identifications of IBM (see Chapter 11), PCL, Ventura Publisher, Microsoft (Roman, with serifs; Swiss, sans serif; Modern, the author
cannot guess; and also Script, Decorative, and Don't know).
• Metrics and Dimensions: usually we design glyphs through the use of integer
coordinates on a grid of 1,000 units per em (PostScript, fixed value) or 2,048 units
per em (TrueType, variable value). Here we can specify the exact size of the grid,
without exceeding 10,000 units per em. Note that 1,000 units per em already gives
us a considerable degree of fineness, if we consider that for type set at 10 points a
unit in a PostScript font is on the order of 3.5 microns, which is one twentieth of the
diameter of a human hair!
• Key dimensions (see Figure 12-8 (a)): dimensions that will be used very frequently:
the height of the ascenders, the depth of the descenders, the height of the capitals, the
height of the lowercase letters, the angle of the (true) italics, the angle of the artificial
slant, the depth and thickness of the underscore.
• TrueType-specific metrics: this panel deals with dimensions drawn from certain specific TrueType tables. For example, here we find the dimensions TypoAscender, TypoDescender, and TypoLineGap from the OS/2 table: the “typographically
correct” values, therefore those that are based on aesthetics rather than on physical
measurements, the height of the ascenders, the depth of the descenders, and leading. WinAscent and WinDescent, from the OS/2 table, and Ascender, Descender, and
LineGap, from the hhea table (§D.4.4), are the “Macintosh versions” of the parameters just mentioned.
• Subscript and Superscript: the sizes and offsets of these inappropriate typographic
constructs that are found in the OS/2 table (ySubscriptXSize, ySubscriptYSize,
ySuperscriptXSize, ySuperscriptYSize, ySubscriptXOffset, ySubscriptYOffset,
ySuperscriptXOffset, and ySuperscriptYOffset).
• Encoding and Unicode (see Figure 12-8 [b]): depending on the glyphs contained
in a font, we can choose one or more font encodings from this list. Mac OS 8.5, Windows 95, and more recent versions of these operating systems will pretend to show

FontLab (a) (b) (c) Figure 12-8: The tabs Key dimensions, Supported codepages and default character set, and Supported Unicode ranges.

the user multiple fonts; in fact, what will be shown is the same font under different encodings. The name of the font will be the font’s usual name followed by the
name of an encoding in parentheses. The data in question are hidden amongst the
64 pages of the ulCodePageRange1 and ulCodePageRange2 entries in the OS/2 table.
Under this same tab are other data intended for PFM files: the “Microsoft Character
Set” (dfCharSet) and the replacement glyph (dfDefaultChar) (see [47]). We also find
here two pieces of data meant for use in Macintosh font suitcases—the name of the
“Worldscript script” and the Quickdraw font number.
• Custom [cmap] encodings: this panel (which is new in FontLab v5) allows the user
to build his own cmap table by specifying the type and contents of each subtable (see
Appendix §D.4.2).
• Unicode ranges (see Figure 12-8 [c]): the Unicode ranges of which this font contains
at least one glyph. Do not neglect this tab! Some of the author’s students at ENST Brittany have designed beautiful glyphs in the Latin Extended-A table without declaring
that table under this tab. The result? Windows completely disregarded their new
glyphs and replaced them with those from Arial. A very understandable attitude:
if we insist on saying that this table is empty, why should the software doubt us?
• We will describe the panels on hinting Hinting Settings, Standard stems (T1
hinting), Additional hinting parameters, T1 Autohinting in Chapter 13.
• PostScript-specific settings: do we need to create a PFM file? An AFM or an INF
file? Use the parameters WinAscent and WinDescent from the OS/2 table as vertical
coordinates of the bounding box? Which font encoding should we use for the font?3
Should we open a Type 1 export terminal for this font?4
• TrueType-specific settings: Is it necessary to instruct the font? Must we preserve
any pre-existing instructions? Must we convert the simplified instructions that have
been inserted by hand within FontLab? Do we need to instruct any glyphs, if only
those that do not have any instructions? Do we need to export any bitmaps? Do
we need to rearrange the glyph descriptions in the font? Use Unicode correspondences to create a TrueType encoding? Use a particular font encoding for the first
256 glyphs? Which encoding do we need to use for the first subtable of the cmap table
(§D.4.2)? Do we export the kern table?
• Mapping: options for the cmap table: add .null glyphs, the carriage return, and the
space?
• Device metrics: options for the hdmx and VDMX tables (§D.8.3, D.8.5); here we have
the possibility of specifying the sizes (in pixels per em) for which the fonts will con3 The best choice is Always write custom encoding. In this case, FontLab will use the encoding chosen
through the font window.
4 Under this tab, FontLab plays a dirty trick on us: Open
Type
Export
Terminal appears as
, but we have to read it carefully, lest we mistake the first two words for OpenType rather than Open and Type!

FontLab
tain set-widths in precalculated pixels. We can also decide whether we wish to include
a VDMX table in the font.
• Font smoothing: options for the gasp table (§D.8.2). Choose the range of sizes
(measured in pixels per em) to which we shall apply the instructions alone, gray
levels, or instructions and gray levels together.
• Font flags: [head] table: options for the head table (§D.4.3)—the parameters
lowestRecPPEM (the size below which the font is illegible) and fontDirectionHint (a
global view of the directionality of the glyphs, with the possible values 0 [left-to-right
and right-to-left], 1 [left-to-right only], 2 [left-to-right and neutral characters, such as
the space and the period], -1 and -2 [the opposites of 1 and 2: right-to-left only and
right-to-left with neutral characters]).
• Tabs PCLT table, Font identification, Font metrics, Codepages: parameters
from the PCLT table (§D.8.7).
• Binary and custom tables: the ability to selectively erase exotic TrueType tables that
were imported when the font was opened.
• Font note: a textual comment that will accompany the font.
The Glyph Window
When we double-click on a glyph in the font window, it is displayed in the glyph window
for us to edit. In this window we find several layers of data, and they can be partly or
entirely displayed or hidden, as the user wishes. The display can be personalized in this
way through the menus View>Show Layers, View>Lock Layers, and View>Snap to
Layers (which enables the magnetism between the given layers).
The most important layer of data is, of course, the contour of the glyph, for which we
can decide whether or not to display the nodes (starting and ending points of the Bézier

curves) and their types (tangent or angular nodes), the control points, the coordinates
(in the form of pairs of numbers), the direction of the contour, etc.
Behind the glyph, we can place several other layers of data:
• A grid: we can choose the orientation (horizontal or vertical) of this grid from the
Preferences>Glyph Window&lt;Dimensions tab, using the Grid step input fields.
• Some guidelines: we can define a number of straight lines (horizontal, vertical, or
slanted) that will be displayed locally (only for the glyph for which they were defined) or globally (for all glyphs). These horizontal or vertical lines are defined in
the same way as under Photoshop or Illustrator—we click on the horizontal or vertical
ruler at the edges of the window and slide the line that appears until it is in the
desired location. Giving one of these lines a slant is a lot of fun: if we place the cursor
on the line but near the edges of the window, we can change its slant; if we select it
near the middle of the window, we move it in parallel, without changing its angle.
By right-clicking on a guideline (Ctrl-click under Mac OS), we can convert it into a
global line, delete it, or change its properties.
• A mask: this is another contour, one that will not be taken into account during the
generation of the PostScript or TrueType font but that serves only to assist with the
creation/editing of the current glyph. For example, we can use the glyphs of another
font as a “source of inspiration”. Magnetism can be quite useful for following the
mask with a great degree of precision without being obliged to work under enormous magnification factors. The mask is managed by the Tools>Mask menu. If we
wish to work with the mask itself, we can exchange it for the regular contour (entry
Swap Outline with Mask). To generate masks globally from the glyphs of another
font, we can use Tools>Mask>Assign Font Mask. Likewise, we can personalize
the display of a mask by using Preferences>Glyph window>Colors.
• A global mask, which is a mask common to all the glyphs in the font. We cannot
work directly with a template, but we can convert part of a contour or a mask into
a template through the Tools>Templates menu.
• A background, which is a mask in the form not of a contour but of a bitmap. Suppose
that the reader wishes to reproduce the handwriting of Vicentino Ludovico degli
Arrighi, used in his calligraphy textbook La operina da imparare di scrivere littera cancellarescha of 1523:
The first step (and certainly the most costly, unless one has very good friends who
are librarians or collectors) is to obtain a copy of this work and scan all the letters
very carefully, in PICT or TIFF format. Next, one will use each of these scans as
a background by specifying it on the File>Import>Background menu. What is

FontLab
important here is to position the bitmap in question correctly with respect to the
glyph’s origin and to give it the correct size. To do so, one selects entry Tools>Background>Move and scale. To set the bitmap to an exact scale value, one is required,
at least as of version 4.6 of FontLab, to use a Python script. Once the background has
been imported, one may use a rapid solution—use another software product from
the same company (ScanFont), which will automatically draw the glyphs’ contours—
or a slow solution—tracing the contours oneself by maintaining a balance between
faithfulness to the original contour and the elegance of the trace.
The glyph window can be used under four basic modes, each of which has its own tools
and its own interface. These modes are:
• The editing mode, which is the most important mode, as it is the one in which we
create or modify the glyph’s contour.
• The sketch mode (Contour>Sketch mode), which offers an alternative to editing the
traces of glyphs, inspired by Peter Karow’s program Ikarus.5 In this mode, following
Karow’s approach, we use neither Bézier curves nor nodes nor control points; instead, we insert points of three types: “angular”, “curvilinear”, and “tangent”). The
software will trace the contour along these points, which we may move at will. When
we need more precision, we add more points. Once we have finished with our points,
FontLab will convert everything to Bézier curves. Since the author is not convinced
that this mode will last long, nothing more will be said about it in this book.
• The vector paint mode, (View>Toolbar>Paint and then click on a button in the
Paint toolbar). Vector paint mode offers several interesting functions: drawing a
rectangle, an ellipse, or a polygon. We can even write text in a given font, and it
will automatically become a contour! But this mode is characterized most of all by
gadgets such as brushes that are round or rectangular or that even have the shape of
the brushes used in Chinese or Japanese calligraphy. It goes without saying that we
can hardly obtain an aesthetically appealing result with these so-called calligraphic
brushes; use them, therefore, in moderation.
• The measurement mode (
button), which allows us to measure distances with a great
deal of precision. By holding down the shift key, we can restrict ourselves to horizontal or vertical measurements or those taken at an angle of any multiple of 15 degrees.
Of these modes, the only one that is worth describing in detail is the “editing” mode,
which we discuss below.
To trace a curve or a line, we enable the button
(not to be confused with
, which is
for the “sketch” mode) and then click within the window to select the curve’s starting
5 This program calls into question the notion of a mathematically defined curve. What Karow [207, p.
117] claims is that what is essential about a contour is that it goes through a certain number of points and that
we must know whether these points are smooth, angular, or angular on one side and smooth on the other.
Once we have specified the major points, the software will take care of the rest, and then it does not matter
whether the curves are quadratic, cubic, or conic: the result will be the same (!). And if the curve is not exactly
what we wanted, we need only add a few more points. . .

```text
point. If we wish to produce a straight line, we release the mouse button and click a
second time, while holding down the alt key, to select the ending point. If, however, we
wish to produce a curve, we drag the mouse while holding the button down: the point
at which we release the button will be the location of the first control point. When we
click again, we select the curve’s ending point. If we drag the mouse, we obtain not the
second control point but its opposite relative to the ending point.
FontLab considers nodes to be smooth by default; thus the node itself and its control
points lie on the same straight line, the one that is tangent to the curve.
We can change this behavior by holding down the alt key. Then the link between the
entering and exiting directions of the node disappears, and we can continue to trace in
another direction. The simplest way to obtain an angular node is to click without pressing alt, to drag the mouse until the “entering” control point is correct, and then to press
the alt key: the “exiting” control point will then be released, and we can place it where
we wish by releasing the mouse button.
The use of the alt key to switch from a smooth node to an angular one when tracing
curves will be difficult at first for those who are used to FontStudio but quite natural to
users of Fontographer or Illustrator, software packages that follow the same conventions.
To close a contour, one need only click on it—according to the manual. But having tried
this procedure many times, always in vain, the author has reached the conclusion that it
is better to close the contour somewhere near its starting point and then to use the mouse
to move the ending point so that it coincides with the starting point. A good test to see
if curves are really closed is to switch to preview mode (menu View>Show Layers>Fill
Outline) and check that all surfaces have been blackened.
To modify a curve that has already been traced, we can move the nodes, the control
points, or even the entire curve by dragging. Three buttons are available for adding
nodes: by enabling
and clicking on the curve, we convert the section of the curve that
lies between the last node and the location of the click into a straight line and insert a
node where we clicked; by enabling
and clicking on the curve, we obtain a new node
on the curve without modifying the curve, and the node is a smooth one; by enabling
and performing the same operation, we obtain an angular node.
To obtain new nodes, we can also use the “knife” tool
. By drawing a line with this tool,
we cut a curve or a closed contour into two. When we apply this operation to a closed
contour, FontLab adds the missing straight line segments to obtain two closed contours
again.
The contextual menu (clicking while holding the ctrl key) of a node offers us several
operations related to it: making it the first node of the curve; converting it into a
smooth/angular node; deleting it; copying it; deleting its control points (Retract BCPs);
reversing the contour’s direction; or making it into an angular node with tangents whose
angle is 90 degrees. This same contextual menu can also operate on the entire contour:
making it the first contour; deleting it; subtracting it from the contour that appears
below; selecting it; or creating a parallel contour at the left, at the right, or on both
sides, at a given distance.
```

FontLab
Drawing shapes is all very well; but if the shapes are simple, having them available for
ready use is even better. That is why we have the Primitives Panel (Windows>Panels>
Smart Shapes menu). On it, we can select a grid (Grid), arcs, horizontal rectangles,
rectangles at any desired angle (Free Rectangle), ellipses, stars with any number of
branches, polygons with any number of sides.
For transforming contours, a whole panoply of tools is available. Let us begin with the
most classic ones: scaling
, rotation
, slanting
, but also moving
and reflection
. To gain access to the last two of these transformations, it is necessary to use the
Window>Panels>Transformation panel.
On this same panel, there is a little button
that seems unassuming enough at first
blush. But this button offers us a veritable factory of transformations: the transformation
window (also accessible from the Tools>Action menu). In this window we find a long
list of transformations, divided into four groups: transformations for contours, operations related to hints and instructions, transformations of font metrics, and more exotic
transformations called effects:
• The transformations of contours are the classic ones that we mentioned above, plus the
following: decomposition of a composite glyph; conversion of Type 1 contours into
TrueType contours and vice versa; reversal of the directions of all the contours; insertion of endpoints for the horizontal and vertical tangents; deletion of juxtaposed
parts; optimization of the glyph.
• We shall examine the transformations of hints and instructions in Chapter 13, which
discusses the optimization of fonts.
• The transformations of font metrics involve changing the set-width (Set Width) or the
side bearings (Set Sidebearings), centering the glyph with respect to its set-width,
automatically calculating the side bearings from an analysis of the glyph’s contour
(Autospacing), or changing the font’s metrics dramatically (Adjust Metrics).
• The effects are best explained by an illustration:

Here we have tortured the font Le Monde Livre. The last result, in which “Tous les effets” (meaning “All the effects”) is barely legible, comes from the application of all the effects in the order shown. It goes without saying that the only one of these effects that is of interest for the production of fonts worthy of the name is Effects>Bold, which allows us to increase the weight of the glyphs. For example, we can simulate the optical correction by adding a small amount of weight and slightly increasing the width and the side bearings. Another possible application: we can add a slight amount of weight to some fonts in order to adapt them better to others (for example, the mathematical symbols of Computer Modern, for use with text in Times Roman). Just above, we spoke of a “factory of transformations”. But every factory has an assembly line. We can perform several transformations sequentially through the window Tools> Action Set. There is no limit to the number or the variety of the transformations that can appear in a sequence. We can also specify precisely the glyphs to which we wish to apply these transformations: the choice can range from a single glyph to the entire font to all the open fonts or even to all the fonts in a given directory. And if the user successfully makes an ideal transformation, she may save it in a file by using the button , which appears on the Action Set window. On the vertical Tools toolbar, we also find button , which surrounds the contour with a frame that has handles. By moving these handles with the mouse, we can perform the classic transformations: scaling, rotation, and slanting. There are several other transformations of contours that must be applied manually: they are listed on the Transform toolbar (obtained through the View>Toolbars>Contour menu) and should not be confused with the Transformation panel. The first two buttons of the Transform toolbar are just shortcuts for horizontal and vertical reflection. The third button initiates an interpolation procedure. Clicking on this button opens the following window: As long as this window remains visible, we are in “interpolation mode”. In this mode, we can click on any node and make it into a reference point. A reference point can stay in its original position or be moved. The principle of interpolation is as follows. All points that lie between two reference points are moved proportionally by interpolating the displacement vector of the reference points. All the points that lie before the first reference point or after the last one are moved by the same amount as the reference points. These calculations are performed individually within each contour. Once we have displaced all the reference points to our satisfaction, we click on OK to confirm the operation. The button launches an operation of simplification. By simplification we mean the replacement of a number of Bézier curves by a single one that assumes, as much as

```text
FontLab
possible, the shape of those curves. Used with discretion, this operation can improve a
glyph: often a single Bézier curve is infinitely more beautiful than a dozen laboriously
drawn subcurves. Here is how it works: We select all the nodes with a ctrl-A (°-A on
the Macintosh), we click on
, we click on the node that will be the starting point of
the simplified curve, we click on the node that will be the ending point of the simplified
curve, and voilà! In order to join the new section of curve smoothly with the rest of the
contour, we may depress the shift key while selecting the corresponding nodes.
Other operations are less important:
allows for the precise definition of the coordinates of each node, either absolutely or relative to a reference point, in Cartesian or polar
coordinates;
allows us to squash a glyph by changing the curvature of the background
on which we are designing it (meant for lovers of gadgets and psychedelic fonts; sensitive
souls should steer clear of this feature!);
allows us to change the direction of some
contours by clicking on any node of a contour whose direction we wish to reverse and
double-clicking on it to complete the operation and accept the result.
Finally, if all of FontLab’s capabilities taken together will not yield the result that we
want, we can use other vector-design software, save the contour in EPS format, and import the result into FontLab through the menu File>Import>EPS.
The Metrics Window
Like human beings, glyphs never live in isolation. But to form communities of glyphs
(what humans call “words”), they have to maintain certain distances: neither too close
together nor too far apart. Finding the correct distances between each pair of glyphs is
an art in itself. And it is not a pointless exercise: the legibility of the text depends on it.
We manage the distances between glyphs by kerning them—i.e., by moving them closer
together or farther apart, starting with the natural distances obtained by setting the starting point of the second glyph at the ending point of the first glyph’s displacement vector.
It is the most thankless task in font design: when, after hundreds of tests and many sleepless nights spent putting the finishing touches on the kerning, we have finally achieved
a good result, no one even notices. Any problems with kerning, however, will stand out
like a sore thumb.
To facilitate the chore of kerning as much as possible, FontLab puts several tools at the
user’s disposal.
All the operations are performed in a special window called the metrics window (menu
Window>New Metrics Window):
```

```text
On the bottom bar of this window, we can enter a line of text (possibly using the \ABCD
notation for glyphs representing Unicode characters or the /name_of_glyph notation to
specify a glyph by means of its name). By choosing Panel in the Options pull-down
menu a table appears with the following information for each glyph: its name, set-width,
and left and right side bearings. The values of these cells in the table can be modified, either by entering a new value or by typing an equal sign followed by the name of another
glyph: the corresponding value will then be copied. This operation applies one time only:
if we enter =o in the box for the left-hand side bearing of the ‘e’, that letter will inherit
the value for the left-hand side bearing of the ‘o’, but no link will be established between
the two; and if the value of the former changes, the latter will not be affected.
When the second pull-down menu is set to Metrics, we are in “set-width and side bearings” mode. In this mode, clicking on a glyph lets us modify its left and right side bearings and its position relative to the set-width. By selecting Kerning in the pull-down
menu, we switch to “kerning” mode. A new line is added to the table: it contains the
values of the kerning pairs. By clicking on a glyph, we can modify its kerning relative
to the preceding glyph. Warning: as Knuth said in [218, p. 317], it is very easy to do too
much kerning, and all excesses in typography are bad. To avoid this trap, we should, dixit
Knuth, apply the amount of kerning that seems perfect on the screen, and then—use only
half as much! A word to the wise.
A few very interesting features of this window: the button
displays the text from right
to left, a boon for the designers of Arabic, Hebrew, or Syriac fonts. The button
displays
a red horizontal line called the measure line. When the measure line is visible, the left and
right side bearings are calculated not according to the actual side bearings of the letters
but according to the intersections of the contours with this line. That may be beneficial
for certain pairs of letters (such as “AV” or “LY”) but catastrophic for others (such as “AA”
or “XX”). Used judiciously, this line can be very useful; do not neglect to take advantage
of it. A helpful tip: To change the height of this line, go into a glyph window in which
the layer of vertical metrics has already been unlocked in Window>Panels>Editing
Layers; then simply move it up or down with the mouse.
By selecting Auto... in the Tools pull-down menu we have the possibility to generate
new metrics or new kerning pairs (according to the mode) for a single glyph, for the
glyphs displayed, or even for all of the glyphs in the font. The author can hardly imagine
that a font in which the set-widths, the side bearings, and the kerning pairs were all calcu-
```

```text
FontLab
lated automatically could really be functional; but we have to admit that that would be a
good starting point. With kerning pairs, we can avoid excesses by specifying an absolute
value below which a kerning pair is considered too small and does not appear, together
with a maximum number of kerning pairs. Various options give us more or less control
over the process of automatically generating kerning pairs.
We shall discuss the insertion of OpenType properties in Chapter 14. But before we get
to that point, there is a concept borrowed from OpenType that we can use immediately
to simplify the process of producing kerning pairs: the concept of glyph class. By sorting
the glyphs into classes whose members behave the same with respect to kerning, we can
generate a large number of kerning pairs automatically. For example, it is obvious that
the glyphs ‘A’, ‘À’, ‘Á’, ‘Ä’, and ‘ ˛
A’ will need the same kerning pairs with every other letter.
When we write “AT”, for instance, any accent that appears on the ‘A’ will not interact
with the ‘T’ in any way. Thus it is desirable to place all the varieties of ‘A’ in a class and
to define kerning pairs for only one ‘A’; the others will follow.
To do so, we use the class-definition window (Window>Panels>Classes panel):
We click on the button
to create a new class. The zone at the left displays the name
of the new class: class1. We can then work in “console mode”. We replace the string
class1: in the input method at the bottom right with the name of the class (for example,
_kernA), followed by a colon, the name of the representative glyph (the “union steward”
of all the glyphs in the class) followed by an apostrophe, and the names of all the glyphs
in the class. Once all those data have been entered, we click on
, and the list appears
in the area immediately above. Instead of keyboarding glyph names we can also drag
glyphs from the glyph window into the main area of the classes panel.
Now it is time to use the classes that we have defined. The window Tools>Kerning
Assistance allows us to specify which of these classes are left-hand classes and which
are right-hand classes. When we have checked the respective boxes, we have two possible
choices: we can save by selecting Apply and Save, in which case FontLab will create an
OpenType table of type kern that will contain the classes and their respective kerning
pairs, or we can request Expand Kerning, in which case FontLab will calculate all the
kerning pairs thus produced and add them to the list of kerning pairs that already exist.
That is how we can obtain, for example, new kerning pairs in an AFM file. But beware:
once again, the connection is not permanent. If we later change the kerning of the representative glyphs, we must use Expand Kerning again to update all the pairs.
```

```text
The classes that we have just described are not used only to define kerning pairs. Through
the window Tools>Metrics Assistance, we can also change the set-widths or the side
bearings of all the glyphs in a single class.
Finally, fonts are often—but, alas, not always—accompanied by AFM (or PFM) files that
contain kerning pairs. We can import these values: in the metrics window, we use the
Open metrics entry of the Tools pull-down menu and select the file to be read, together
with certain options. We can also save the font’s metrics in an external file by using Save
metrics.
Multiple Master Fonts
Multiple Master fonts, or “accordion fonts”, are dynamic PostScript Type 1 fonts in the
sense that the contour of each glyph can vary according to several parameters. These
fonts were introduced by Adobe at the same time as the program Acrobat, in which
they play a crucial role: specifically, how to substitute for a missing font without harming
the layout? The substituted font must be able to adapt itself to the characteristics of the
missing font—in particular, to the set-widths of its glyphs.
That is what the Multiple Master fonts that come standard with Acrobat—with names
as generic as Adobe Serif and Adobe Sans—do very efficiently: often we do not even notice
that a substitution has taken place.
The reader will find in Appendix §C.4 a technical description of the Multiple Master
format. This section is dedicated to the way in which FontLab manages these fonts. Incidentally, their features under FontLab are slightly more powerful than those of the Multiple Master specification; indeed, independently of the Multiple Master font format,
FontLab uses that format’s technique of linear interpolation as an internal technique for
creating intermediate fonts, whatever their final format may be. That strategic choice is
very significant because the Multiple Master font format has been officially abandoned:
Adobe has withdrawn the Multiple Master tables from the OpenType format and, in so
doing, signed a death warrant for this technology.6
A glyph in a Multiple Master font has a variable contour. Its variability is structured in
the following manner. The font has a certain number (2, 4, 8, or 16) of “master designs”
for each glyph that cover the axes of variation, which may number from 1 to 4. The master
designs are found at the extreme ends of these axes: thus there are necessarily 2n master
designs for n axes. To obtain any particular instance of a variable glyph, it is sufficient
to perform linear interpolation on the master designs by giving a precise value to the
parameters that correspond to the various axes. To the end user, that takes the form of
a window with one sliding bar for each axis: as values are specified, the selected glyphs
change dynamically. Here is the interface, under Illustrator 10:
6 That said, the dynamic font technology still exists in the AAT fonts (§D.12). But as yet no tool really
supports the creation of these fonts.
```

```text
FontLab
Without going into the technical details, we wish to bring one very important constraint
of the Multiple Master format to the reader’s attention. Although the different master
designs do, of course, have contours of their own, they must still share some nontrivial
similarities: the same number of nodes, nodes of the same type, nodes placed in positions
in which anomalies (such as curves reduced to a single point or curves that intersect) will
never occur. In other words, the possible degree of variation is still quite restricted, and
we are far from having carte blanche in the choice of our master designs!
The four possible axes of a Multiple Master font may be given any names, but Adobe recommends the following names (and roles): Weight, Width (set-width), Size, and Style.
One can imagine how difficult it can be to create Multiple Master fonts: starting from an
existing font, one must reduce or increase the weight of the glyphs uniformly; one must
ensure that the extreme designs are aesthetically acceptable and that an interpolation
made from them yields as its “average” the original font; to achieve any modification
to an intermediate design, the master designs must be modified.7 In other words, the
designer must envision the glyphs in his mind as multidimensional objects—already a
difficult task—and, in addition, understand that to obtain an intermediate glyph, one
that will be used every day and that must be impeccable, we have to design extreme
glyphs: extra-thin, ultra-wide, super-bold, etc., and arrange for the interpolation of these
extremes to yield the desired intermediate form.
Is that possible? By morphing a basketball player and a sumo wrestler, can we obtain a
normal man, or even a beautiful one? Can beauty, which in typography lies in moderation and normality, come from the interpolation of extremes? It is hard to answer that
philosophical question. And that is without doubt the reason for which there are so few
Multiple Master fonts, most of them being simple sans serif designs.
In any event, FontLab offers the interface shown in Figure 12-9: we design all the master designs in the same glyph window; a Masters palette allows us to display them or
hide them and to indicate the archetype that we are currently designing (the others are
locked); another palette, Axis, allows us to set values for the axes of variation, which
are applied to an invisible contour. What is the use of this “invisible contour”? There
is none, except that we can ask that it be shaded gray, and then we can see it just like a
mask. Thus we can freely modify the master designs and observe the consequences of
our modifications on the intermediate glyph.
7 In fact, knowing that intermediate masters are often the most useful, Adobe has included in the Multiple Master specifications the possibility of using a master not as an extremity of a variation axis but as an
intermediate value. But this functionality is not supported by FontLab which will not even open such fonts.
```

```text
Master
(1,1,1)
Master
(0,0,0)
Mask
Figure 12-9: The interface for designing Multiple Master fonts in FontLab. In it are shown
the contours of two master designs (one ultra-light, ultra-condensed, and at an optical size of
6 points; the other ultra-bold, ultra-wide, and at an optical size of 72 points) and, shaded in
gray, an (invisible) intermediate contour. This is Adobe’s font Kepler.
By modifying the values of the axes of variation in the Axis window, we see that beyond
a certain maximum value (and below a certain minimum value), the values are displayed on a yellow background. That is called extrapolation, a property specific to FontLab
that does not appear in the Multiple Master specification. Extrapolation merely “goes
further” and yields even more extreme results, often verging on the grotesque, and sometimes even on the paradoxical.8
A proverb says that “all is fair in love and war”. Well, here neither love nor war is at
stake, but FontLab follows this principle all the same by offering us tools for producing Multiple Master fonts that border on the slovenly! Thus, here—very quickly—is a
practical way to obtain the light and bold master designs. We select a font that has a
bold weight. Obviously there is no guarantee that the glyphs in the bold weight will be
8 Note that in the font Kepler the optical size can be extrapolated downward all the way to the value −28!
Which raises a truly metaphysical issue: what is a negative optical size?
```

FontLab Figure 12-10: The window for creating Multiple Master fonts from two ordinary fonts taken as master designs: the fonts Univers 47 (light condensed) and Univers 67 (bold condensed). “compatible” with those in the light weight, i.e., that they will have the same nodes, of the same kind, and in the same places. But here is what FontLab offers us. We select the two fonts, together with the name of the new axis of variation, in the window Tools> Blend Fonts (see Figure 12-10), and we check the box Build the Multiple Master Font. Then FontLab will meticulously compare the two versions of the glyphs and make a decision about their compatibility. If, for a given glyph, the light version and the bold version are “compatible”, the box for the glyph in the font window will be colored green. Then we can apply the action Tools>Multiple Master>Mask to Master, and the bold version will become the glyph’s second master design. If, however, the glyphs are not compatible, we can move the nodes of the second master design (which is, by default, identical to the first) until the contour looks just like the bold version, which is shown as a mask. Note that for the example of the fonts in Figure 12-10, 65 percent of the glyphs were already characterized by FontLab as “compatible”, and we had nothing more to do than to handle the 35 percent that remained in order to obtain a true Multiple Master font with one axis (weight). This is not a contrived example, as Univers is the canonical example of a “variable” font, and it is but a short step from Adrien Frutiger’s arrangement of Univers in several series [144, pp. 13–25] to the Multiple Master axes. The same method of “multimasterization” in FontLab can be applied to versions of a font with different set-widths or optical sizes, or indeed any other type of variation.9 Clearly this sort of practice almost turns the design of Multiple Master fonts into child’s play. 9 For example, the well-known designer Luc[as] de Groot designed a Multiple Master font called MoveMeMM for which the first master design is a very proper sans serif font and the second is a series of awfully raunchy images [112]. This font, offlimits to minors, follows in the long tradition of anthropomorphic and often erotic typefaces [92].

```text
Driving FontLab with Python Scripts
The greatest strength of FontLab over other font-editing software is without doubt the
fact that it can be driven by a very enjoyable programming language called Python. Even
though FontLab is proprietary software whose source code will never be available to the
ordinary mortal, we can still go under the hood and take control of its actions by writing
a few lines of simple, comprehensible code.
Under Windows, before trying to run any Python scripts, one must install Python on the computer, as explained in:
http://www.python.org/download/releases/2.4.1/
In the next part of this section, up to page 488, we shall assume that the reader has a basic
knowledge of Python. If that is not the case, we recommend a number of books, by a
certain publisher named O’Reilly: first, if the reader is new to programming, she can very
well start out by learning the basics of programming in Python with the excellent book
Python Programming for the Absolute Beginner, by Michael Dawson [111]. If, however, she is
an experienced programmer and wishes only to learn Python, we recommend Learning
Python, by Mark Lutz and David Ascher [241]. Finally, for the reader who already has
some experience with Python and is looking for a reference book, we enthusiastically
recommend Python in a Nutshell, by Alex Martelli [247].
Python code is entered in the Window>Panels>Edit Macro window. This window has
four buttons on the left with the following meanings: open a file open/save window; run
the current script; stop it; re-initialize the Python interpreter (in case something went
wrong and the interpreter hangs). There is also a button on the right which allows editing
the script in a separate editor (such as BBEdit for the Macintosh or UltraEdit for Windows), if the latter has been defined in the FontLab Studio>Preferences>General
Options>Python scripting panel.
If we are going to use a Python script often, it is convenient to call it from FontLab’s
user interface. To do so, we need only save it (always with the extension .py) in one
of the many subdirectories of /Library/Application
Support/FontLab/Studio
5/Macros/System. The location at which the script’s name appears in FontLab’s
interface will depend on the subdirectory in which we store the script. For example,
if we store it in the Kerning subdirectory, the script’s name will appear in the “context
menu” when we click inside the metrics window obtained through Window>New
Metrics Window.
The name of the script, as shown through this interface, is the name of the script file,
unless we have included the following line in the code:
#FLM: A more friendly name
in which case it is the “more friendly name” that will appear in the menu.
Let us proceed by exploring some of the Python classes, attributes, and methods that
FontLab places at our disposal.
```

FontLab
The FontLab class
The base class, which has no constructor but is always predefined, is FontLab. The only
instance of this class that is available to us is fl (abbreviation of “FontLab”). Here are its
most important attributes:
• font, which returns an object of type Font (the active font); count, which returns the
number of open fonts; ifont, which returns the index of the active font among the
open fonts. Note that fl can also be used as a list of length len(fl) that is indexed by
the open fonts. For example, f=fl.font and f=fl[fl.ifont] yield the same result.
• glyph, which returns an object of type Glyph (the active glyph in the font window,
the glyph window, or the metrics window); count_selected, which returns the number of selected glyphs;10 iglyph, which returns the index of the active glyph among
all the glyphs of the active font. Note that a Font object can also be used as a list that
is indexed by its glyphs. For example, g=fl.glyph and g=fl.font[fl.iglyph] yield
the same result, with only one small difference: in the first case, g is an orphaned
object, whereas in the second case its parent is the active font.
• path, filename, version, productnumber, serialnumber, username yield, respectively, the path and the filename of the application, its version, its product number,
its serial number, and the username of the current user.
• namfilename, which returns the name of the file containing the standard glyph
names corresponding to the Unicode characters.
And here are the most important methods:
• Open(filename) opens the font filename.
• Close(f) closes the font whose index is f.
• Save(f, filename) saves the font f under the filename filename.
• GenerateFont(type, filename) generates a font named filename. Here are the possible types:
– ftFONTLAB, a font in FontLab format VFB
– ftTYPE1, a PostScript Type 1 font, PFB file
– ftTYPE1_MM, a Multiple Master font, binary
– ftTYPE1ASCII, a PostScript Type 1 font, PFA file
– ftTYPE1ASCII_MM, a Multiple Master font, ASCII
– ftTRUETYPE, a TrueType font, TTF file
– ftOPENTYPE, an OpenType-CFF font, OTF file
10 Note: several glyphs may be “selected”, but only one is “active”.

– ftMACTYPE1, a PostScript Type 1 font, Macintosh font suitcase and LWFN file
– ftMACTRUETYPE, a TrueType font, Macintosh font suitcase
– ftMACTRUETYPE_DFONT, a TrueType font, .dfont file
• UpdateFont() updates the active font after modifications performed by a program.
UpdateFont(fi) does the same for the font whose index is fi.
• UpdateGlyph() updates the active glyph after modifications performed by a program. UpdateGlyph(gi) does the same for the glyph whose index is gi.
• EditGlyph() and EditGlyph(gi) open the glyph window for the active glyph or for
the glyph whose index is gi.
• Selected() and Selected(gi) return the boolean value True if the active glyph (or
the glyph whose index is gi) is selected.
• Select(glyphid) selects the glyph identified by glyphid, which may be a glyph
name, a number (the glyph’s index), or Uni(number), in which case number is the
glyph’s Unicode index. A second argument, 0, to Select will unselect the glyph.
• Unselect() rapidly unselects all the glyphs.
• Message("You, who have known my heart from infancy,\nAnd all its feelings of disdainful pride,\nSpare me the shame of disavowing all\nThat
I profess'd.","Friend, ask me not.","OK, I will","No way") produces a
dialog box:11
If the user clicks on OK, I will, the method will return 1; if he clicks on No way, it
will return 2.
• Random(min, max) returns a random integer between min (inclusive) and max (not
inclusive).
11 These splendid lines come from Robert Bruce Boswell’s translation (Phaedra) of Racine’s play Phèdre.

FontLab A few examples To open all files of type .pfa or .pfb (the extensions may be written in uppercase or lowercase) in the directory /home/yannis/, we can write: import os, re r1=re.compile(r'.+\.pf[ab]\$', re.IGNORECASE) for file in (os.listdir("/home/yannis/")): if r1.match(file): fl.Open("/home/yannis/"+file) To obtain all the files in a given directory, we can use the listdir method of module os. To select the files with the extension .pfa or .pfb, we first prepare the regular expression12 r1, using the compile method of module re. This method takes as its first argument the pattern of the regular expression: r'.+\.pf[ab]\$', which means “any character, one or more times, followed by the string .pf, followed by an a or a b, at the end of the string”. The second argument to this method (re.IGNORECASE) indicates that matching will disregard the case of the specified characters. Next, for each filename file that matches the regular expression, we execute FontLab’s Open method. To convert all the PFB fonts in a given directory into OpenType-CFF, we can write: import os, re r1=re.compile(r'(.+)\.pfb\$', re.IGNORECASE) for file in (os.listdir("/home/yannis/")): if r1.match(file): newfile=r1.match(file).group(1)+".otf" fl.Open("/home/yannis/"+file) fl.GenerateFont(ftOPENTYPE,"/home/yannis/"+newfile) fl.Close(fl.ifont) Here the regular expression is more complex because we have added parentheses to isolate the filename without the extension: (.+)\.pfb\$. The string in parentheses forms the first group of the expression, which we can use by writing: newfile=r1.match(file).group(1)+".otf" The rest is self-explanatory. To find all the glyphs whose name begins with an ‘f’ and display the number in a dialog box while also selecting the glyphs, we can write: 12 For more information on regular expressions in Python, consult [247, p. 145]. But there is also an excellent book on regular expressions in general: [143].

import re
total=0
r1=re.compile(r'^f')
fl.Unselect()
for gi in range(len(fl.font)):
if r1.match(fl.font[gi].name):
total += 1
fl.Select(gi)
fl.Message("","There are "+str(total)+" glyphs beginning with f")
The Font class
This is the class that comes immediately after FontLab. One possible constructor is
Font(). After instantiating a Font object, we do indeed have a new font, but we must
use fl.Add to open the window corresponding to this font:
f=Font()
fl.Add(f)
We can also instantiate Font objects by copying existing fonts: if f1 is one of them, we
can write f2=Font(f1) to produce a carbon copy of it.
Here are the most important attributes of this class:
• Many identification attributes, such as file_name, the complete path to the file containing the font; family_name; style_name; full_name, the full name of the font; and
so on (see [333] for the complete list of identification attributes). For instance, we can
write:
f=Font()
fl.Add(f)
f=fl.font
f.family_name="Times New Roman"
f.style_name="Regular"
f.full_name="Times New Roman"
f.font_name="TimesNewRomanPSMT"
f.font_style=64
f.menu_name="Times New Roman"
f.apple_name="Times New Roman"
• More important, attributes for various dimensions: upm, the number of units per
em; ascender[0], the height of the ascenders; descender[0], the depth of the descenders; cap_height[0], the height of the capital letters; x_height[0], the height
of the lowercase letters (the last five of these dimensions are lists: there is one entry for each master design in a Multiple Master font); slant_angle, the artificial

FontLab
slant; italic_angle, the natural slant of the italic letters; is_fixed_pitch, to indicate whether the font is monospaced; underline_position, the depth of the underline; underline_thickness, the thickness of the underline. For instance, we can
write:
f.upm=2048
f.ascender[0]=1420
f.descender[0]=-
f.cap_height[0]=1356
f.x_height[0]=916
f.default_width[0]=500
f.slant_angle=0.0
f.italic_angle=0.0
f.is_fixed_pitch=0
f.underline_position=-
f.underline_thickness=100
• modified, which is 1 if the font has been modified, otherwise 0.
• classes, a list of all the glyph classes; and ot_classes, the glyph classes defined on
the OpenType panel using the Adobe syntax (§14).
• features, a list of all the OpenType properties, each of them being an object of type
Feature (§14).
• encoding, the current encoding of the font, an object of type Encoding.
• Last but not least, glyphs, a list of objects of type Glyph that represent the glyphs in
the font.
In addition, an object of type Font can also be considered as a list whose objects are
Glyphs; thus the len() operator yields the length of this list, which is the number of
glyphs in the font.
Let us move on to the methods. They are relatively few and are concerned with saving
AFM files in VFB format and some other general operations:
• Open(file) and Save(file), to open and save a font in VFB format. For example,
we can write:
f=Font()
f.Open("/home/yannis/myfonts/Times New Roman.vfb")
fl.Add(f)
• OpenAFM(file) and SaveAFM(file), to read an AFM file and replace its internal metrics or to save the metrics in an AFM file.
• Reencode(encoding), where encoding is an object of type Encoding, re-encodes the
font. We shall see an example below when we describe the Encoding class.

• FindGlyph(name) or FindGlyph(pos) returns the index of the glyph that has the
name name or that represents the Unicode character in position pos. For example,
we can write:
i=fl[fl.ifont].FindGlyph(int("220F",16))
where the int function, with 16 as its second argument, will interpret the string 220F
as a hexadecimal number. If this glyph does not exist in the font, the value −1 is
returned.
• GenerateUnicode() generates new Unicode indices for all the glyphs on the basis of
their glyph names. This is the operation to perform in order to consolidate the font
after correcting the glyph names.
• Generatenames() generates new glyph names for all the glyphs on the basis of their
Unicode indices. This is the operation to perform in order to consolidate the font
after correcting the Unicode indices.
The Encoding and EncodingRecord classes
An object of type Encoding is a font encoding—a set of correspondences between glyph
names and Unicode code points. Each of these correspondences is an EncodingRecord
(which has two attributes: name and unicode), and an Encoding object can be considered
as a list of EncodingRecords, whose length may be obtained through the len operation.
Thus we can write:
enc=fl[fl.ifont].encoding
for i in range(len(enc)):
print str(i)+": "+enc[i].name+" -> "+str(enc[i].unicode)
to obtain a description of an encoding, line by line. Note that the output of the print
method appears in the Window>Panels>Output panel (which will not open automatically; you’ll have to open it yourself!).
We can create a new encoding e1 with e1=Encoding() or by copying an existing encoding e2 with e1=Encoding(e2). Since an encoding is a Python list, all the methods for list
management apply; in particular, we can write:
• e1.append(x) to add a new entry x to e1
• e1.extend(e2) to append encoding e2 to e1
• e1.insert(i,x) to insert entry x at position i of e1
• e1.remove(x) to delete the first occurrence of x in e1, etc.
We also have the following methods:

FontLab
• FindName(name_to_find) finds the entry for which the name attribute is equal
to name_to_find and returns the value of its unicode attribute, or −1 if it cannot be
found.
• Load(file) reads the encoding from a file with the extension .enc. For example, we
can write:
enc=Encoding()
enc.Load("/Library/Application Support/FontLab/Encoding/T1
non-Western/iso_8859-.enc")
for i in range(len(enc)):
print str(i)+": "+enc[i].name+" -> "+str(enc[i].unicode)
• To save an encoding file, we need three pieces of information: the full set of
name/Unicode code point pairs, a unique identifier (FontLab recommends numbers
such as 1,001), and a string that will serve as a quick description of the encoding
(the description that will appear on the pull-down menu of encodings in FontLab’s
font table). If we have these three pieces of information, we can write Save(file,
description, identifier).
We can also read the encoding of a font and store it in a file. Here is an example of the
code that we might use:
enc=Encoding()
enc=fl[fl.ifont].encoding
enc.Save("/home/yannis/test.enc","My font's encoding",1001)
We thus obtain a file of this type:
%%FONTLAB ENCODING: 1001; My font's encoding
_0000 0
Eth 1
eth 2
Lslash 3
...
A 65
B 66
C 67
...
hungarumlaut 253
ogonek 254
caron 255
with lines of type “glyph name, code point”. If a code point is unoccupied, FontLab will
use an ad hoc glyph name formed by taking an underscore (_) followed by the position
in the font table, written as a four-digit decimal number.

For re-encoding, we can use the Reencode method of the Font class. But we must be very
careful with this method, which is the equivalent of the re-encoding operation in FontLab: it is extremely brutal. If at a given position in the target encoding there is a glyph
foo, then whichever glyph is unfortunate enough to appear at that position when the
method is executed will be renamed foo. Be careful, therefore—and, again, be careful!
After every re-encoding, confirm that the glyphs have not been renamed incorrectly.
Here is some code that we could use to “re-encode” a font. In this example, we rename
glyphs that are arranged according to the Macintosh Central European encoding but
whose glyph names are incorrect:
enc=Encoding()
enc.Load("/Library/Application Support/FontLab/Encoding/T1
non-Western/mac_ce.enc")
fl[fl.ifont].Reencode(enc)
fl.UpdateFont()
The Glyph class
After FontLab and Font comes the third fundamental class of FontLab. We shall see that
one other class comes before it in the hierarchy, the class of nodes. Once again, we may
use Glyph as a Python list whose elements are nodes (i.e., objects of type Node) and whose
number is given by len().
The constructor for the Glyph class is Glyph() for an empty glyph and Glyph(g) (if g is a
glyph) to create a copy of g.
The Glyph class is extremely rich, which is no surprise in view of the amount of information that appears in the glyph window. Here are its most important attributes:
• index, the glyph’s index (which cannot be changed).
• name, the glyph’s name.
• unicode, the corresponding Unicode character.
• width and height, the glyph’s width and height.
• bounding_box, the glyph’s bounding box, given in the form of a Rect (rectangle)
object. It is better to use the GetBoundingRect() method because then the bounding
box is actually calculated; otherwise, it is simply read from the font file.
• number_of_contours, the number of contours for the current glyph.
• kerning returns a list of KerningPair objects: all the kerning pairs whose first glyph
is the current glyph.
• hguides and vguides, the glyph’s horizontal and vertical guidelines—these are lists
of objects of type Guide.

FontLab
• mark, which is nonzero if the glyph is marked with a special color. The possible values
for the colors range from 1 to 255 and cover the entire spectrum. We invite the reader
to find a font with at least 256 glyphs indexed from 0 to 255 (add some if necessary)
and write:
for i in range(255):
fl[fl.ifont][i].mark=i
fl.UpdateFont()
The beautiful rainbow that FontLab offers us will then become visible.
And several methods:
• Assign(g) replaces the current glyph with g. Thus we can create a fresh glyph with
g=Glyph(), draw in it, and, finally, replace the current glyph with g: fl[fl.ifont]
[fl.iglyph].Assign(g). Do not forget to copy its set-width as well!
• Add(n) appends the node n to the contour. The same method can be used to add all
the contours of a glyph to a given glyph: g1.Add(g2) adds the contours of g2 to g1.
• Insert(n, i) inserts node n in the ith position of the contour. We can also insert
a glyph at a given position on the current contour, which may have very strange
consequences that may remind us of the human bodies fused to the metal of the
warship in that incredible B-flick called The Philadelphia Experiment.
• Delete(i,j) deletes the nodes between the ith and jth positions.13
• Shift(Point(x,y)) moves the glyph by a coordinate vector (x,y).
• Scale(Point(x,y),Point(cx,cy)) scales the glyph according to the horizontal x
and vertical y factors. Scaling is performed using the point (cx,cy) as the center.
• isAnySelected() returns True if at least one node is selected, Selection() returns
the list of selected nodes, and SelectedCount() returns their number.
• SelectAll() (and UnselectAll()) selects (unselects) all the nodes.
• InvertSelection() selects the unselected nodes and unselects the selected nodes.
• SelectRect(r) (and UnselectRect(r)), where r is an object of type Rect, selects (unselects) all the nodes that fall within the rectangle r.
• RemoveOverlap() joins the overlapping contours—a very useful feature when we
add an appendage to a glyph, such as the cedilla under the ‘c’.
• Badd(g), Bsubtract(g), Bintersect(g): the logical addition, subtraction, and intersection between the current glyph and glyph g.
13 Warning: This is a Python list operation, so counting begins at 0; the nodes, however, start with 1—thus
there will be a difference of 1.

• GetContourNumbers() returns the number of contours in the glyph.
• GetContourBegin(i), GetContourLength(i), SelectContour(i), DeleteContour(i),
isContourClockwise(i), ReverseContour(i): these commands return the first node
or the number of nodes in the ith contour or select it, delete it, tell us whether it is
oriented clockwise, or reverse its direction.
• FindContour(n) returns the index of the contour containing node n.
• JoinAll() attempts to join all the open contours (some of which are close enough
to show that they were meant to be connected: a sort of civil union for nodes).
• SaveEPS(filename) and LoadEPS(filename) save the glyph as an EPS file or read an
EPS file for inclusion as a glyph, respectively.
These methods are useful, intelligent, and logical. For those who like strong sensations
there are several other methods, corresponding to the various effects:
• Rotate3D, Extrude3D, Shadow, College, Gradient, and Warp produce the effects of the
same name.
• Distance(x,y,a), a method that creates a parallel contour offset by (x,y) (inside if
x and y are positive, outside if they are negative). This method may prove useful in
very many cases, whether to make a glyph slightly bolder or to create a contour, etc.
There can be side effects for some nodes: check the result carefully!
Here is an example of making a glyph bolder (by 30 units):
g=Glyph()
g=fl[fl.ifont][fl.iglyph]
g.Distance(-,-,1)
fl.UpdateFont()
And here is an example of creating a contour (with a thickness of 10 units):
g=Glyph()
g=fl[fl.ifont][fl.iglyph]
g1=Glyph(g)
g.Distance(-, -, 1)
g.Bsubtract(g1)
fl.UpdateFont()
This is what we did: We created an instance g1 of a glyph and made it a copy of g.
Next, we made g bolder by 10 units and substracted from it the glyph g1 (which thus
became smaller than g). That left a contour of thickness 10.
• Interpolate(pairs), where “pairs” refers to any number of pairs (i,p), in which i is
the index of a node and p is a Point object. For example, we can write:

```text
FontLab
g=Glyph()
g=fl[fl.ifont][fl.iglyph]
p1=Point(943,-)
p2=Point(743,-)
g.Interpolate(((33,p1),(8,p2)))
fl.UpdateFont()
The result of this method is as follows. The nodes that we have specified by the indices i are moved in order to obtain the corresponding points p. All the other points
of the glyph are interpolated as a result. Interpolation is done as follows: the points
that lie between two “reference” points are interpolated linearly, and those that lie
outside those reference points (before the former and after the latter) are moved by
the same amount as the nearest reference point.
The Point, Rect, and KerningPair classes
These are very simple utilitarian classes:
Point represents a point on the plane. The possible constructors are Point() (an instance
with zero coordinates), Point(p) (the same coordinates as p), and Point(x,y) (coordinates x and y). The attributes are x (abscissa) and y (ordinate). The methods: Add(p),
vector addition; Sub(p), vector subtraction; Mul(s), multiplication by the scalar s.
Rect represents a rectangle. The possible constructors are Rect() (all the coordinates
are zero), Rect(p) (where p is a Point object: the rectangle runs from (0,0) to p),
Rect(r) (where r is a Rectangle object: a copy of r), Rect(p1,p2) (the rectangle between
p1 and p2), Rect(x1,y1,x2,y2) (the rectangle between points 1 and 2).
The attributes are ll (lower left point), ur (upper right point), x and y (the coordinates
of ll), width and height (the width and the height of the rectangle).
The methods are Shift(x,y) (translation), Resize(width,height) (new dimensions),
Include(r) or Include(p) (redimension so that the rectangle r or the point p is included), Check(r) (check whether r lies within the rectangle or crosses it), Check(p)
(check whether the point p lies within the rectangle).
We can, for example, replace a glyph with the rectangle that represents its bounding box,
as follows:
g=Glyph()
g=fl[fl.ifont][fl.iglyph]
r=Rect(g.GetBoundingRect())
g.Clear()
n=Node(nMOVE,r.ll)
g.Add(n)
n=Node(nLINE,Point(r.x,r.y+r.height))
g.Add(n)
n=Node(nLINE,r.ur)
g.Add(n)
```

```text
n=Node(nLINE,Point(r.x+r.width,r.y))
g.Add(n)
n=Node(nLINE,r.ll)
g.JoinAll()
g1=Glyph(g)
g.Distance(-,-,1)
g1.Distance(15,15,1)
g.Bsubtract(g1)
fl.UpdateFont()
where we are getting a bit ahead of ourselves by using the Node class.
Now we jump to a new subject: KerningPair represents a kerning pair. The possible constructors are KerningPair() (an empty pair), KerningPair(k) (a copy of pair k), KerningPair(i) (kerning, set to a zero value, with the glyph whose index is i), KerningPair(i,v) (paired with glyph i, the kerning value set to v). Its attributes are key (the
index of the glyph to the right) and value (the value of the kerning pair).
Thus to obtain a list of all the kerning pairs for which the glyph at the left is A (assuming
that the index of A in this font is 36), we can write:
g=Glyph()
f=fl[fl.ifont]
g=f[36]
for i in range(len(g.kerning)):
print f[g.kerning[i].key].name+" : "+str(g.kerning[i].value)
A few words of explanation: g.kerning is a Python list, and therefore len() yields its
length. The expression g.kerning[i].key returns the index of the glyph at the left (despite its name, key, which gives the impression that we are obtaining the glyph’s name).
To obtain the glyph’s name, we must go through the glyph object and request its name
attribute: f[g.kerning[i].key].name. Finally, since g.kerning[i].value is a number,
we must convert it to a string in order to concatenate it to our output string; we do so
here with the function str().
The Node class
A glyph contour is made of nodes. This class could have been the smallest in the FontLab
architecture; it is not, however, as below it there is another class, Point, representing a
point on the plane. But what is a node, if not a point? Indeed, this class is simple, having
few attributes or methods; but, unlike the classes Font and Glyph, which are as clear as
a bell, this one can only be understood if we exercise our gray matter a little.
There are two complementary ways to classify nodes: by their type (straight line? curved
segment?) and by their alignment (smooth? sharp?). Intuitively we can imagine a node
as the starting point of a Bézier curve (which, since the curve is closed, is also necessarily
the ending point of another curve). FontLab’s vision of the concept of a node is different:
to FontLab, a node is the ending point of a Bézier curve and of the preceding curve as well.
```

FontLab
4 nCURVE
5 nLINE
6 nLINE
7 nLINE
8 nLINE
9 nLINE
nLINE 10
nCURVE 11
nLINE 12
nLINE 13
2 nCURVE
3 nLINE
1 nMOVE|nFIXED
nCURVE|nFIXED 15
nLINE|nSMOOTH 14
10 nLINE
11 nLINE
13 nLINE
12 nLINE
14 nLINE
15 nLINE
nLINE 16
nOFF 17
nOFF 18
nOFF 19
nOFF 20
nLINE 21
nLINE 22
nLINE 23
4 nLINE
5 nLINE
1 nMOVE
2 nOFF
3 nOFF
7 nOFF
6 nOFF
8 nOFF
9 nOFF
nLINE 24
nOFF 25
nOFF 26
15'
11'
15''
11''
4'
4''
2'
2''
Figure 12-11: Contours in PostScript (left) and TrueType (right). The control points are represented by white dots. In TrueType, they are considered to be nodes in their own right; in
PostScript, they are part of the data for the node that follows, and so control points 4′ and 4′′
“belong” to node 4.
The situation varies according to the type of Bézier curve. If quadratic curves are used
(as in TrueType), there are three types of nodes:
• Those reached by a move (type nMOVE, typically used for the first node of a contour)
• Those reached by a straight line segment (type nLINE)
• And those that are control points (type nOFF, so called because they are offthe curve)
Thus we act as if there were nothing but straight line segments in a TrueType contour.
And since the issue of alignment does not arise between straight lines (the alignment can
be smooth only if those lines are parallel, in which event the node is useless), classification by alignment does not apply to TrueType. On the right side of Figure 12-11, we see
an example of a TrueType contour with nodes of type nMOVE, nLINE, and nOFF.
If, however, the contours use cubic curves (as in PostScript Type 1), then nOFF nodes will
never occur, since the control points are not counted as nodes. Let us examine the left
side of Figure 12-11 and consider the Bézier curve formed by points 3 (the starting point),
4′ (the first control point), 4′′ (the second control point), and 4 (the ending point). The
last three of these points are regarded as forming a node of type nCURVE. It may seem

::: tip Typographical Specimen Plate (Figure 12-11)
![Figure 12-11: PostScript and TrueType contour directions](/images/fonts-encodings/fig12-11-postscript-truetype-contours.png)
*Figure 12-11: PostScript and TrueType contour directions.*
:::

![Figure 12-11: PostScript and TrueType contour directions](/images/fonts-encodings/fig12-11-postscript-truetype-contours.png)
*Figure 12-11: PostScript and TrueType contour directions.*

incongruous that control point 4′, which, after all, “belongs” to point 3, and a priori has
nothing to do with point 4, should be attached to point 4, so to speak. But that is just how
FontLab chooses to structure the data. In the same figure, we see nodes of type nMOVE
(the first node of the contour), nCURVE (for the curves), and nLINE (for the straight lines).
Now the classification by alignment type comes into play. Most nodes are of type nSHARP
(i.e., they form a sharp angle). These are not explicitly indicated in the figure because
we are using flag 0, which therefore applies by default. Node 14 is smooth (nSMOOTH),
which means that the tangents at the two sides of this point have the same slope and
that there is only one line tangent to the curve at this point. Nodes 15 and 1 (which
correspond, in fact, to the same point) are of alignment type nFIXED. This type of alignment is a variant of nSMOOTH. The difference is not visible on the contour; it is more of
an ergonomic nature. When we modify the curve in question by sliding the cursor of
the mouse over it (not by moving its control points), the tangents to the control points
can change their slope if the node is of type nSHARP or nSMOOTH; if, however, the node is
nFIXED, the tangents will not change direction.
To conclude this excessively long but, alas, indispensable description of node types, let us
point out that the contour in the figure reveals a weakness in the letter’s design: node 4
should also be nSMOOTH, just like node 14. This peculiarity of the design is, no doubt,
accidental.
Let us return to the Node() class. It has three possible constructors: Node() creates a fresh
node, Node(n) copies another node, and Node(t,p) creates a node of type t whose point
(on the curve) is p.
The attributes of Node are:
• type, the type (nMOVE, nLINE, nCURVE, or nOFF)
• alignment, the type of alignment (nSHARP, nSMOOTH, nFIXED)
• selected, boolean True if the node is selected
• point, the ending point (a Point object) of the Bézier curve
• points, a Python list containing the three points that make up a node of type nCURVE:
the ending point of the Bézier curve and the first and second control points
• x and y: the coordinates of the point attribute
Thus to create a node n of type nCURVE with ending point p1 and control points p2 and p3,
we can write:
n=Node(nCURVE,p1)
n.points=(p1,p2,p3)
To indicate the alignment type, we have the choice between a binary or at the time of
construction or the use of the alignment attribute. For instance:

```text
FontLab
n=Node(nCURVE|nSMOOTH,p1)
is equivalent to
n=Node(nCURVE,p1)
n.alignment=nSMOOTH
The methods of the Node class are dedicated to the Multiple Master fonts, with one exception: Shift(p) will move all the points in the node by an amount equal to the coordinates of point p.
Here is an example of the use of nodes. Let us take the letter ‘Z’ from the font Monotype
Old Style. To obtain a list of all the nodes and their points, we need only write:
g=Glyph(fl[fl.ifont][fl.iglyph])
for i in range(len(g)):
print i, g[i], g[i].points
The result is:
0 &lt;Node: type=0x411, x=519, y=0&gt; [&lt;Point: x=519, y=0, active refernce&gt;]
1 &lt;Node: type=0x401, x=594, y=208&gt; [&lt;Point: x=594, y=208, active refernce&gt;]
2 &lt;Node: type=0x401, x=564, y=208&gt; [&lt;Point: x=564, y=208, active refernce&gt;]
3 &lt;Node: type=0x1423, x=493, y=108&gt; [&lt;Point: x=493, y=108, active refernce&gt;,
&lt;Point: x=536, y=154, active refernce&gt;, &lt;Point: x=523, y=136, active refernce&gt;]
...
12 &lt;Node: type=0x401, x=451, y=647&gt; [&lt;Point: x=451, y=647, active refernce&gt;]
13 &lt;Node: type=0x401, x=18, y=17&gt; [&lt;Point: x=18, y=17, active refernce&gt;]
14 &lt;Node: type=0x401, x=18, y=0&gt; [&lt;Point: x=18, y=0, active refernce&gt;]
15 &lt;Node: type=0x401, x=519, y=0&gt; [&lt;Point: x=519, y=0, active refernce&gt;]
To draw this letter through pure programming, we need only take its coordinates and
write:
g=Glyph()
g.Add(Node(0x11,Point(519, 0)))
g.Add(Node(0x1,Point(594, 208)))
g.Add(Node(0x1,Point(564, 208)))
n=Node(0x1023,Point(493, 108))
n.points=(Point(493, 108),Point(536, 154),Point(523, 136))
g.Add(n)
n=Node(0x1023,Point(283, 30))
n.points=(Point(283, 30),Point(436, 56),Point(364, 30))
g.Add(n)
g.Add(Node(0x1,Point(139, 30)))
g.Add(Node(0x1,Point(582, 675)))
g.Add(Node(0x1,Point(122, 675)))
```

```text
g.Add(Node(0x1,Point(58, 488)))
g.Add(Node(0x1,Point(84, 488)))
n=Node(0x1023,Point(155, 581))
n.points=(Point(155, 581),Point(114, 539),Point(128, 557))
g.Add(n)
n=Node(0x1023,Point(360, 647))
n.points=(Point(360, 647),Point(208, 626),Point(272, 647))
g.Add(n)
g.Add(Node(0x1,Point(451, 647)))
g.Add(Node(0x1,Point(18, 17)))
g.Add(Node(0x1,Point(18, 0)))
g.Add(Node(0x1,Point(519, 0)))
g.JoinAll()
g.width=605
g.name="Z"
g.unicode=int("005A",16)
fl[fl.ifont][fl.iglyph].Assign(g)
fl.UpdateGlyph()
Note that here, rather than using the constants nLINE etc., we have given the explicit
numeric values of the types and the alignments. We close the contour with g.JoinAll().
FontForge
Aside from the visual appearance of its interface, which lacks the splendor of that of FontLab, FontForge (formerly named PfaEdit) is extraordinary software! It includes a large
portion of FontLab’s functionality, a few features of its own (a debugger for TrueType instructions, an editor for OpenType tables, and even an editor for AAT tables), the ability
to save fonts with more than 65,536 glyphs, even in CID format—and all that for the low
price of zero dollars. Thus it is a great free software package, and, unlike collective freesoftware projects such as Emacs, Mozilla, Gimp, etc., FontForge was developed entirely by
a single person: a Californian by the name of George Williams.
In addition, being free of charge, FontForge can also be localized as much as one wishes.
There are already French, German, Italian, Spanish, Russian, Vietnamese, and Japanese
versions.
FontForge runs under Unix/X Window. Not to worry if you use Mac OS X or Windows. Under
Mac OS X you need only install X11 first; it has been supplied with the system since version 10.3.
Under Windows, you must install CygWin [301, p. 10]. The procedure is duly explained on FontForge’s Web site [352].
As with all free software, one can compile FontForge oneself. Nonetheless, if one is not a seasoned
programmer, compiling the software will entail a small risk: a problem may arise if the system’s
configuration is slightly more recent than that of the initial developer. And if a problem arises,
one is truly stuck. Furthermore, compiling FontForge requires a number of libraries of external
subroutines that one must download oneself from their respective Web sites and place in the right
```

FontForge
locations. Again, the versions of the libraries used by the developer must be compatible with the
ones that the user has downloaded.
Finally, if one is on a widely used Unix platform (Linux, Mac OS X, Cygwin), it is easier to obtain a
pre-built binary for one’s system. Installation is completed in a trice, and any possible annoyances
related to programming are thus avoided.
By default, FontForge’s windows are of a gray color as sad as the image that Michel Villandry
painted of the French city of Brest: “... things are swallowed up in the gray background as if everything were hiding behind everything else” [340]. While we may not be able to do anything about
Brest, we can change the background of FontForge to a brighter color. To obtain, for example, a
pretty, creamy white, perform the following operation:
• If it does not already exist, create the file .Xdefaults in the login directory (execute cd ~ to
go there).
• Add to the file the following line (or modify it, as the case may be):
Gdraw.Background: #ffffcc
where #ffffcc is a creamy hue of white expressed as an RGB (red, green, blue) triplet.
• Finally, run:
xrdb ~/.Xdefaults
to update the X resource database.
• Add this last operation to the file .bashrc or to any other Unix script that sets up the user’s
environment.
To launch FontForge, type fontforge & on the command line. A file-opening window
appears, inviting us to open a font file on the disk or to create a new font by clicking
on New. Warning: unlike most applications, FontForge has no “generic window”. If at
startup time we do not open any font (whether pre-existing or new), the application will
terminate.
The Font-Table Window
Let us select a font through the opening dialog box. The font-table window opens, which
also contains the various menus of FontForge:

```text
The font-table window shows the font’s glyphs within boxes whose size we can specify
(it may range from 24 to 96 pixels) through the View window. In each box, and above
each glyph, is displayed the corresponding Unicode character or a red question mark if
the glyph does not correspond to any Unicode character. Using View>Label glyph by,
we can choose glyph cells to be labeled by Unicode codepoint or by PostScript name or
position in the imported encoding. When a cell is selected, a certain set of data is displayed under the menu bar: the glyph’s index in the font (in decimal and hexadecimal),
the hexadecimal code of the corresponding Unicode character, the PostScript name of
the glyph, and the name of the Unicode table in which we are working.
We can categorize the glyph boxes by coloring them. To do so, we select a box and choose
the color on the pull-down menu Element>Glyph Info>Comment>Color. We also
have the option of adding comments on the glyph. The comments and the color are
stored in a “private” table—a TrueType table that is recognized only by FontForge.
Opening/Saving a Font
We can open fonts in the formats PFA (whence the former name of this software), PFB,
Type 42, PostScript CID, GSF (the vector font format of the software ghostscript), TrueType/OpenType and TTC (in this case, an opening window asks us which of these we
wish to open from among the fonts in the collection), SVG,14 IK (the font format of the
Ikarus system of Peter Karow), and a few bitmap formats: FON, FNT, BDF. A font can be
compressed in .Z or .gz format; FontForge will uncompress it before opening it.
Faced with this impressive choice of font formats, we may well ask ourselves which formats FontForge cannot open. Very few, in fact. In the version of January 20, 2004, the
only formats that FontForge could not yet open were certain exotic formats that are of
no interest to anyone anymore, such as the FON vector format (for which no one, not
even Microsoft, seems to have the specifications), Intellifont, Speedfont, and PFR.
FontForge’s native font format is SFD (for “Spline Font Database”). We can, of course,
open SFD files and also save them (with File>Save or File>Save as).
To generate fonts in formats other than SFD, we use
File>Generate Fonts, which opens the font-generation
dialog box shown at the side.
We are given the choice of PostScript (single PFB or
multiple PFB, PFA, Type 3, Type 0, Multiple Master,
CID, CFF, CFF CID), TrueType (possibly with OpenType
or AAT tables), OpenType/CFF or OpenType/CID, and
SVG. The choice “PS Type 1 (Multiple)” means that
if the font contains more than 256 glyphs, it will be
broken into pieces with 256 glyphs (or fewer) and that
we will end up with as many Type 1 fonts. The choice
“CFF (Bare)” means that the raw CFF data will be placed
in a file without being enveloped in a TrueType structure.
14 To open fonts in SVG format, it is necessary to ensure in advance that the libxml2 library of subroutines
has been installed on the system.
```

FontForge
The Options button will open a small window in which we may choose the auxiliary
files to generate (AFM, PFM, TFM/ENC for PostScript fonts) and certain options pertaining to TrueType fonts: include instructions? include PostScript glyph names in the
post table? include Apple or OpenType advanced typographic tables? include a special
FontForge table that may contain comments and choices of colors for the boxes?
There is a slight problem on Mac OS 9: X Window under Mac OS X does not have access
to the resource part of Mac OS 9 files. But the data for all Mac OS 9 font formats have
always been stored in the resource section. In order to create resources, FontForge offers
no other solution than to create MacBinary files, which the user may then convert to the
Macintosh’s data/resources file format.
To keep users from having to perform these manipulations, Mac OS X introduced the
dfont font format, a “flattened” format in which the resource section immediately follows the data section. FontForge, of course, can read and write dfont files.
Accordingly, if a Macintosh font is destined to be used only under Mac OS X, we will use
the dfont format, or even just TTF or OTF files. If, however, it is also meant for use under
Mac OS 9, we have no choice but to go through the MacBinary format.
To generate Mac OS 9 font families, we use File>Generate Mac Family. But to have
access to this feature, we must have previously opened other fonts that will be the members of this new family. FontForge will present, in the font-family generation window,
the potential members of the family; all that we have to do is to select them and choose
the Macintosh style (roman, italic, bold, bold italic) for each of them.
The General-Information Window
We open this window through the menu Element>Font Info. The window contains
14 tabs, which often take us to other windows, subwindows, etc. Here are these 14 tabs:
• Names: in this tab, we can enter the different names of the font (the PostScript
name, family name, “long” name) as well as its weight, version, and copyright notice.
• General, where we can enter a number of numerical parameters such as the height
of the ascenders, the depth of the descenders, the number of units per em, the slope,
the parameters related to underlining, the unique identifier (UID) and the extended
unique identifier (XUID), the presence or lack of vertical metrics in the font, and,
finally, whether the Bézier curves in the font are cubic or quadratic.
• PS UID, where we enter the Unique Identfier of a PostScript font.
• PS Private Dictionary, where we can view and modify the private parameters of the
PostScript Type 1 format: BlueValues and OtherBlues, StdHW and StdVW, BlueScale,
BlueShift, BlueFuzz, and ForceBold. The first four can take several values each, for
overshoot and the relevant thicknesses of horizontal and vertical strokes. For these
four parameters, FontForge displays a histogram with the values actually obtained
by these parameters in the font. Thus we can designate values for these parameters
with the benefit of a global view of the font.

• OS/2. In this window, we can view and modify the parameters specific to the TrueType tables: classes for weight and set-width (in the OS/2 table), authorization to incorporate the font in a document (ditto), leading (hhea table), vertical leading (vhea
table), the 10 parameters of the Panose classification (see Chapter 11), for which we
can set the values not as numbers but through the use of the names given in the
classification, etc.
• TTF Names: we can enter each of the 18 strings in the name table in about a hundred
combinations of languages and encodings.
• T˙X (actually written in Greek). FontForge can produce TEX font-metric files (TFM),
but to do so it needs a certain amount of information: the optical size, the slope,
the ideal space between words, the amount of stretching and shrinking allowed at
the current set-width, the height of the lowercase letters, and the extra space used in
English typography at the end of a sentence. By selecting “T˙X Math” or “T˙X Math
Ext”, we gain access to the advanced parameters for fonts of mathematical symbols
and extensible mathematical symbols.
• The other tabs are used to edit the advanced typographic features of fonts. We shall
examine them in the chapter on enriching fonts.
The Glyph Window
Double-clicking on a glyph in the font-table
window opens the glyph for editing in a
glyph window. Together with this window,
FontForge offers two palettes: the first, called
Tools,15 contains some 18 buttons representing all the graphical tools; the second,
Layers, allows for the selection of the various
types of information to display in the glyph
window.
The most important layer of data is, of course,
the glyph’s contour, and there are three
imaginary planes on which we can do our
work: the “foreground”, which will be used
when we generate a font; the “background”,
which contains auxiliary guidelines that will
be ignored when the font is generated; and
the “guide”, which contains the guidelines and other supporting material common to
the backgrounds of all the glyphs. The three buttons just to the side of Fore, Back, and
Guide in the Layers palette allow us to switch from one working plane to another. The
buttons on the left side of the window make the appropriate plane visible. (The active
plane is always visible.) The other buttons at the bottom pertain to hints and OpenType
properties, with the exception of the last two (HMetrics and VMetrics), which are used
to display or hide the horizontal and vertical baseline and set-width.
15 But its name cannot be read without widening the window.

```text
FontForge
When the cursor is moved onto the working plane, its coordinates (in the coordinate
system of the glyphs) are displayed at the upper left of the window, on the menu bar.
To draw a curve, just as in any other vector-design or font-design software, we use the
tool. When we click on a point, we create a new node for the curve; by dragging the
mouse, we move the control point; finally, when we release the mouse button, we fix the
position of the control point, and we can proceed to another point. If, after clicking on a
point on the plane, we release the mouse button without moving the mouse, the point
in question will be connected to the preceding points by a straight line segment, not by
a Bézier curve.
To move a contour, we must first select all its nodes. We can select them one by one or,
by double-clicking anywhere along the contour, all at the same time. Then we can move
the contour with the mouse—but beware! We must take care to “grab” it by a node. If we
try to pick up a contour by clicking on an intermediate point between two nodes, we
will merely alter the Bézier curve in question, and the rest of the contour will not even
budge.
There is another way to draw curves in FontForge, one that is noticeably different from
that of FontStudio, FontLab, or even Illustrator: in these other software systems, we obtain a point by clicking on a certain location, and by dragging the mouse (while keeping
the button depressed) we change the curve’s control point; here, however, when we drag
the mouse, the point to be created moves as well—it only becomes definitively set when
we release the mouse button. Which also means that we cannot modify the control
points at the time that we create the curve.
More precisely, there are three buttons that are used to create three types of points:
produces a smooth point (having a Bézier curve on each side),
produces a “tangent”
point (with a smooth Bézier curve on the side leading in and a straight line on the other
side), and
produces a vertex of a polygonal line. Thus the best way to trace a new path
is to anticipate, every time, both the position of the new point and its type, to choose the
appropriate tool from the Tools palette, and to click on the right location, possibly also
dragging the mouse to get the position just right—without worrying about the control
points. Afterwards, one can change to the “move” tool
and easily move both the nodes
of the curve and the control points. The reader who wishes to use these tools should get
used to the fact that the first curve drawn will not be good; it is produced just to break
ground—and the precise positioning of the control points is what will yield the desired
contour for the glyph.
Note that for changing the type of a point (among “smooth”, “sharp”, and “tangent”),
one uses the Point menu in the glyph window.
To copy and paste paths, one uses the Edit menu, as in any other software. But this menu
offers several other very useful entries: Edit>Copy Reference allows us to copy onto
the clipboard not the contour itself but a reference to the contour so as to create composite glyphs by pasting references of this type; Edit>Copy Width allows us to copy onto
the clipboard the set-width of another glyph; Element>Simplify allows us to simplify
a path by eliminating the selected nodes—the tangents at the endpoints will remain
```

```text
unchanged; finally, Edit>Copy Fg to Bg copies the contents of the working plane onto
the background.
The knife tool
is also slightly different from its analogue in FontStudio or FontLab.
Nothing happens when we click on a contour; however, if we click outside a curve and
drag the mouse, we obtain a “cut line”. This is the line that will cut the curve. Needless
to say, this operation is quite close to the use of our kitchen knives or the craft knife of
the model builder.
The tool
is used to measure distances between two points. Click on the starting point
and drag the mouse. FontForge will then display, in real time, the distance between the
two points, the horizontal and vertical projections of the vector thus obtained, and its
slope.
The buttons
,
,
, and
are used for scaling, reflection, rotation, or slanting of the
selected parts of a contour. These operations are performed strictly by eye; one may use
the transformation tool Element>Transformations>Transform for more precision.
The two tools
and
allow for the drawing of predefined curves: rectangles or polygons. When these buttons are clicked, they change shape (
and
); then they will
produce ellipses and stars. To draw a rectangle or an ellipse, one may decide whether the
pointer will indicate the center of the shape or the upper left corner of its bounding box;
to do so, one merely double-clicks on the button in question and registers the choice in
the little window that appears. By holding down the shift key, one can obtain a square or
a circle. Likewise, by double-clicking on the button for the polygon or the star, one may
select the number of vertices.
Finally, the tool
is mostly a gimmick: it is used for freehand drawing. One may trace
any path at all, and it will immediately be converted into Bézier curves. This method
is certainly very useful in software for freehand drawing, such as Photoshop or Painter,
but the author can see little need for it in the context of font design, especially when
one compares the original drawing to the Bézier curves obtained. Double-clicking on the
button opens a dialog box that offers the choice of “pen” shapes, à la METAFONT (§F.1.3).
In theory it could be used for drawing “calligraphic” letters, but one quickly finds out
that a calligrapher never uses a pen as rigid as those of the software; the glyphs obtained
thus give an impression of rigidity and artificiality. Note, however, that it is possible to
use Wacom pen tablets and associate levels of pressure on the stylus with different widths
of pens.
The glyph window comes with several very useful menus. For example, selecting Element>Glyph info opens a little window with information on the glyph, arranged in
several tabs. Most of these tabs are for the advanced OpenType properties and will therefore be examined in Chapter 14. The first tab (Unicode) allows us to name the glyph
according to its Unicode position or, conversely, to determine the Unicode position associated with a glyph from its name, according to Adobe’s conventions for naming glyphs
(see page C.3.3).
The menu option Element>Transformations>Transform opens a transformation
window that applies to the selected part of the contour. In this window we may select
```

```text
FontForge
from one to three common transformation(s) (translation, rotation, scaling, reflection,
slanting) by setting the desired values.
Other interesting menu options: Element>Expand stroke transforms a Bézier curve
into a “tube”; thus one can draw the skeleton of a letter and then “puffup” its strokes
in order to make an “Egyptian” letter. Element>Overlap processes superimposed
closed contours in various ways, the most interesting ones being union (Remove Overlap) and intersection (Intersect). Element>Simplify simplifies a contour. Element>
Add extrema adds nodes to the horizontal and vertical tangent lines of the curves. Element>Effects offers four typographically questionable effects (outline, inline, shadow,
wireframe).
The option Element>Align performs several very practical operations: Average Points
aligns the points either horizontally or vertically (the direction in which there is the least
variation in the coordinates is selected), giving them all an abscissa or an ordinate equal
to the average of the original abscissas or ordinates. Space points is more complex:
FontForge chooses three points a, b, c and, considering two of the points (for example,
a and b) to be fixed, moves c so that it falls on the perpendicular bisector of the segment ab. Then c will be moved in parallel to ab. What is less clear is how FontForge
selects the fixed points and the point to be moved. Finally, Make Parallel applies only
to straight lines; it makes them parallel to one another by moving the last node selected.
The options Element>Clockwise, Element>Counter
Clockwise, and Element>
Correct direction allow the direction of Bézier curves on a contour to be changed.
One can confirm that the direction has been set correctly by having the contour filled in
(View>Fill); however, it is important not to remain in “filled-in contour” mode, as the
filling of the contour is not always refreshed correctly.
The Metrics Window
The metrics window (Windows>New Metrics Windows) is used to establish and test
the ways in which glyphs interact with one another: we can enter a string of glyphs and
check their set-widths and their kerning. The keyboard can be used to enter a string
of glyphs in the little input area at the upper left. If a glyph cannot be entered from
```

```text
the keyboard, it can still be dragged in from the font window in the area for previewing glyphs. Clicking on a cell in the rows Width (set-width), LBearing (left-hand side
bearing), RBearing (right-hand side bearing) at the bottom of the window causes the
corresponding glyph to be selected. Once a glyph has been selected, we can make simple substitutions (look-up of OpenType Type 1 substitutions) through View>Substitutions, where we find a list of all the look-up operations of this kind that apply to the
glyph.
By clicking on a given glyph, we can use the mouse to modify its left-hand side bearing
(with the red cursor containing an ‘L’), its right-hand side bearing (with the red cursor
containing an ‘R’), or its kerning with the preceding glyph (red cursor containing a ‘K’).
To center a glyph in its box, we use Metrics>Center in Width. The option Metrics>
Thirds in Width is similar but yields a right-hand side bearing that is twice the size of
the left-hand side bearing.
The metrics window in itself is quite simple, but its effect is only local: it allows for the
rather precise management of the metrics of certain individual glyphs. We can also manage metrics in a global fashion. That is done through the Metrics menu, but the options
in question are accessible only through the font window (doubtless in order to force their
effect to be global).
There we find two interesting options: Metrics>Auto Width and Metrics>Auto Kern.
The first of these rearranges the set-widths. More precisely, FontForge will arrange side by
side the glyphs that we wish to examine and will also modify their left and right side bearings if necessary. The Spacing parameter gives an order of magnitude for the distance
that the user considers optimal. According to George Williams’s description [352], the
value of this parameter expresses the distance between two sans serif ‘I’ glyphs. The default value of the parameter is none other than the width of the contour for the glyph ‘n’.
The option Metrics>Auto Kern will attempt to kern the glyphs that we have specified,
by taking three parameters into consideration: Spacing (as in Auto width), Total Kerns
(the maximum number of kerning pairs), and Threshold (the threshold below which
the kerning pair is ignored; this value prevents the proliferation of insignificant kerning
pairs). Unlike Auto Width, this option displays the kerning pairs to be evaluated in a
text file of the following format:
AV
AU+0150
U+0100U+0150
U+1E00V
The syntax of this file is very simple: there is one line for each kerning pair, with the
glyphs indicated by an ISO Latin-1 character or by the notation U+ABCD, where ABCD is
the hexadecimal code for the corresponding Unicode character.
We can alter the set-width of one or more glyphs by using Metrics>Set Width. It allows
us to replace the set-widths with a fixed width, to apply a scaling factor to them, or to
increment them by a fixed amount.
```

```text
FontForge
Finally, it is possible to define kerning classes and to have the kerning of a pair of glyphs
applied to their respective classes. We shall see how in Chapter 14, when we discuss the
enrichment of fonts with advanced typographic features (OpenType or AAT).
What About Vertical Typesetting?
Although this possibility is little used outside the East Asian scripts, both TrueType and
PostScript Type 1 allow us to set type vertically by supplying vertical metrics (set-widths
and kerning pairs). Vertical typesetting turns out to be a real headache for the programmer: since screens and graphical interfaces were designed for horizontal writing, how can
we switch efficiently to the vertical mode?
It comes as no surprise that FontLab and even AsiaFont Studio, its special “East Asian”
version, turn evasive when the issue of vertical fonts comes up. In fact, FontForge is the
only software today that takes on the challenge of vertical metrics.
For a PostScript font, vertical metrics are vertical displacement vectors and vertical kerning pairs in AFM files (see §C.3.7). In an OpenType font, vertical set-widths are stored in
the vmtx table (see §D.8.6), and vertical kerning pairs are stored in a subtable of the kern
table, all of whose coverage flags have their first bit cleared (see §D.8.4).
In FontForge, the vertical mode is “enabled” by checking Element>Font Info>General>Has Vertical Metrics. Pressing
this button enables the Vertical Origin field, which appears
immediately below: it contains the height of the vertical origin
relative to the horizontal baseline. This value may be changed at
any time; it is used to offset the glyphs vertically within their
vertical set-widths (which, by default, are equal to the sum of the
Ascent and Descent parameters in the hhea table).
As for the horizontal placement of the vertical origin, it is automatically set to a distance from the horizontal origin that is
equal to half of the vertical set-width. These choices are not arbitrary: indeed, they are the optimal choices for ideographic characters, whose set-widths (both horizontal and vertical) are fixed
and whose vertical baseline runs through the (horizontal) center
of the glyphs.
For modifying a font’s vertical metrics, the following features are
at our disposal: Metrics>Set Vertical Advance (like Metrics>
Set Width for the horizontal case) offers global modifications
through the application of a given increment or scaling factor;
Metrics>VKern By Classes adopts the system of kerning-pair
classes; Metrics>VKern From HKern is useful primarily for vertical typesetting simulated by horizontally setting glyphs rotated 90 degrees: for each horizontal kerning pair,
we obtain a vertical kerning pain between the rotated glyphs, calculated through a substitution look-up of the vert or vrt2 property.
```

```text
To generate the set-widths and vertical kerning for the glyphs, we can also use the metrics
window. To switch from horizontal to vertical mode, we need only select View>Vertical
in this window; then the string of glyphs is displayed vertically, and we can move them
with the mouse, as usual.
CID Fonts
One other technique is used primarily for the ideographic languages. The CID fonts (see
§C.7 for a technical description) are Adobe’s work-around to the 256-code-point limit
on the size of a PostScript font encoding. The idea is as follows: since, on the one hand,
we need an arbitrarily large number of ideographic glyphs and, on the other, Unicode’s
unification of the ideographic languages is disastrous for typesetting (as the variants of
ideographs may be distinct characters in one language and glyphs for a single character in another), Adobe had the ingenious idea of short-circuiting Unicode and offering
“catalogs of glyphs” that are specific to each ideographic language, and even to each encoding. These catalogs are called character collections (although they contain glyphs and
not characters), and Adobe offers one for Japanese16 (Japan1, covering the JIS X 02011997, JIS X 0208-1990, JIS X 0212-1990, and JIS X 0213-2004 encodings), two for Chinese
(GB1 for simplified, and CNS1 for traditional), one for Korean (Korea1), and one—that
has been in preparation for several years—for the old Vietnamese script.
What is interesting is that the character collections are periodically updated and, moreover, the updates are done so as to ensure upward compatibility. Thus Adobe adds new
glyphs while preserving the old ones. For example, the Japanese character collection
Japan1 is already at version 6 (the seventh version [16], as counting begins at zero; it
contains 23,058 glyphs!), and those for simplified Chinese and traditional Chinese are at
version 4 (29,057 and 18,964 glyphs, respectively).
The glyphs of a CID font are contained in a file called CIDFont. We use it by means of
a font encoding called CMap (not to be confused with the cmap table of TrueType fonts)
that is found in another file. For instance, the same font may be used with any encoding,
and the same encoding can apply to any font (in the same character collection). A CID
font can also be contained within an OpenType structure; in that case, the CIDFont data
will be stored in a CFF table.
The reason that we have mentioned CID here is that FontForge is the only software that
can manipulate them.17
A CID font is made up of several subfonts. This property is used to classify its glyphs: alphabetic ones, dingbats (pictograms), kana (the Japanese syllabaries), kanji (ideographs),
etc. When opening a CID font, FontForge displays the first of these subfonts in the font
window. The others are accessible through the CID menu, where the names of the subfonts appear in the bottom section.
16 Previously there were two character collections for Japanese; they were merged in 2004.
17 AsiaFont Studio (the “East Asian” version of FontLab) can open the subfonts of a PostScript CID font.
Both FontLab and its elder brother can open OpenType CID fonts, but only by flattening them—i.e., by discarding their classification into subfonts. Neither software package can save CID fonts—a rather annoying
limitation, especially in such expensive software.
```

Autotracing
This menu has a number of interesting features:
• CID>Flatten will “forget” the font’s CID structure and convert it into a normal font.
For example, we can save the font in PostScript Type 1 or TrueType format.
• CID>Flatten By CMap operates in the same way, but the “flattened” font thus
obtained will have an encoding drawn from a CMap file. This option requires a file
of this sort to be specified. We can obtain one from Adobe [26] or create one ourselves.18 (See §C.7.2 for a complete description of the CMap files).
• CID>Insert Font inserts a new subfont from an external “flattened” font into the
CID font.
• CID>Insert Blank inserts a new blank subfont that we can then fill in.
• CID>Remove Font removes a subfont.
• CID>CID Font Info is a variant of Element>Font Info with data on the entire
CID font rather than on just a single given subfont. For instance, if we wish to enable
vertical mode, we must use CID>CID Font Info>General.
A glyph in a CID font has the CID number corresponding to its position in the font table.
This is the number that appears in red at the beginning of the menu bar when we select
the glyph in this table.
The character collection of a CID font cannot be changed. Only at the time when a font
is created (when we use CID>Convert to CID) can we associate a character collection
with the new font.
All in all, FontForge offers a good way to modify existing CID fonts, build new CID
fonts, and store them in both the old PostScript format (file CIDFont) and an OpenType
structure with a CFF glyph description.
Autotracing
Autotracing is the operation of generating a vector contour for a glyph from a bitmap image without any intervention from the user. In this section we shall describe two systems
for autotracing fonts. We have placed this section at the end because we are reluctant
to discuss this topic at all. Indeed, there are too many fonts of poor quality that were
produced through autotracing. We have seen in this chapter how to obtain contours
described by precise and elegantly arranged Bézier curves. Autotracing software cannot
recognize symmetry, the thickness of equal strokes, or the heights and depths kept consistent throughout a font; in short, the intelligence of a good vector design cannot be
obtained automatically. And when we speak of “intelligence”, we are alluding, of course,
to artificial intelligence, whose limitations are by now well known.
18 Which does, however, require some patience, since, at least for the ideographic languages, it involves
matching up some 20,000 (!) ideographs to positions in the encoding table.

After this introduction intended to discourage the reader from using autotracing software, let us see when we can use such software without doing too much harm:
• When the font is of a “free design”, in the sense that there is no calculation hidden
behind its proportions, dimensions, etc.
• When the font represents handwriting. Who has never wanted to publish entire
books in his own handwriting? In this case, autotracing cannot make any more flaws
than the human hand already has, with regard to the precision of the strokes.
• When the image whose contours we wish to autotrace is large and has a high resolution and when the perfection of the curves is not critical. The difficulty in this case is
obtaining sufficiently rich images. One case in which it is possible is when the font
is in another vector format (such as METAFONT), or when we have printed samples
of very high quality and at a large size.
potrace
There are two great free software packages for autotracing: AutoTrace, by Martin Weber
[344], released in 1998, and potrace, by Peter Selinger [316], which was not released until 2001. Both are SourceForge projects, and it is widely acknowledged that the latter
is more powerful and that the former supports more file formats for both input and
output.
These software packages can perform autotracing on any bitmap images; they have no
special features related to fonts.
If we wish to convert a METAFONT font to PostScript Type 1, there are at least two utilities (mftrace [279], written in Python, and TEXtrace [326], written in Perl) that take control
of the entire process of launching METAFONT, assembling the files, autotracing each
glyph, and compiling everything into a PostScript font with correct metrics.
When we are beginning not with a METAFONT font but with a series of images, we can
use FontForge. To do so, we first install on our system one of the autotracing packages
(AutoTrace or potrace) and declare it to FontForge (File>Preferences). Next, we must
perform the following operations:
1. Import the images in the form of masks (File>Import) into the correct positions in
the table. We can do so manually or import an entire batch of images at the same
time. To import a batch of images, name the images uniHHHH.png (where HHHH is a
four-digit hexadecimal number and the image corresponds to the Unicode character
in that position), perform File>Import, and choose Series of images as the file
type. Select the first image in the series; the others will be loaded into the boxes
corresponding to their Unicode code points.
2. Establish a set-width for each glyph and, if necessary, move the mask relative to the
set-width so that it is correctly centered and at the correct height.

```text
ScanFont
3. Select Element>AutoTrace. FontForge then invokes AutoTrace or potrace (according to the choice that the user has indicated in File>Preferences) and autotraces
the mask.
4. Correct the contours, using FontForge’s tools for vector design.
Step 2 is the longest, unless ideographs or “typewriter” fonts with a fixed width are being used.
The quality of the autotracing will depend on the values of the parameters. To change a
value, select the option Element>AutoTrace while holding down the shift key. Then it
is possible to enter the command-line options that the user will find explained in detail
at the web site of potrace (http://potrace.sourceforge.net).
We shall show an example of the result of an operation of this kind in the next section.
ScanFont
ScanFont (version 4) is a program developed by FontLab Ltd. It runs under Windows
and Mac OS, but under Windows it is stand-alone software, whereas under Mac OS it
is distributed as a FontLab plug-in.
Figure 12-12: Separation of glyphs under ScanFont.
The autotracing of a font under ScanFont is a procedure performed in two steps. The
first involves separating the glyphs in an image that contains several. The software includes several algorithms to do so and a number of parameters for optimizing the result.
If the algorithm places two parts of the same letter in different boxes, we can connect
them; conversely, if two letters are inadvertently placed in the same box, we can separate
them. And we can also frame the glyphs manually. In Figure 12-12, we see the inside of
a glyph-separation window; the result shown was obtained with the default values of the
parameters.
Next comes the step of autotracing the individual glyphs. When this operation is initiatied, a configuration window opens (Figure 12-13). In this window, we can vary the
values of three parameters (trace tolerance, curve fit quality, straightness of angles). What
is extremely interesting is that we see the effect of these parameters on the trace in real
```

Figure 12-13: Dialog box for the real-time configuration of autotracing under ScanFont. time. Thus we can rapidly find the ideal values for each font. These values can be stored and used as a set of predefined values. Original ScanFont potrace Figure 12-14: Comparing a contour traced by hand and two contours autotraced from the same rendering. In Figure 12-14, we show the result of autotracing by the two systems described: ScanFont and potrace. Obviously we cannot easily compare two software packages when their results depend a great deal on the choices of values for the parameters. We have therefore taken the default values of the parameters in both cases and autotraced an image of very high quality: the rendering at 3,432 × 3,300 pixels of a glyph from a vector font. Note that this image, owing to its size and its “artificial” character, is far better than the best scan of printed text that we will ever be able to produce. Here are the conclusions that we can draw from these images: At a global level, we cannot see any differences among the three contours. By inspecting the control points, we can tell that ScanFont used fewer points to trace the straight lines but far more to trace the curves. There is an abnormally heavy cluster of points all along the serifs. Likewise,

ScanFont ScanFont had a few problems with the inside of the apex of the letter ‘A’. For its part, potrace added some unneeded points (in the middle of straight line segments, etc.) but used fewer points at the serifs. We can only advise the reader to try both programs out before undertaking an autotracing project (potrace and AutoTrace are free, and there is a demo version of ScanFont at FontLab’s web site) and certainly to repeat the same tests by varying the values of the parameters. In conclusion, let us compare once again the three versions of the letter ‘A’ in the figure. Is the original not more elegant than the two letters derived from it? The author is convinced that those who are used to using vector design tools will spend less time vectorizing a letter (by hand, but in an intelligent and methodical way) by following its mask than correcting an autotraced contour, however good the tool that produced it.

```text
Optimizing a Rasterization
In a world peopled with fonts, we would read in Genesis: “for pixels thou art, and unto
pixels thou shalt return”. Indeed, we often forget that the ultimate goal of all the mathematical constructions that represent our glyph outlines is to produce images made from
pixels. If we had only one font size and only one resolution for our screens and printers,
we would have no need of outlines; the bitmaps would be quite sufficient. Outlines exist only to allow fonts to be adapted to the current situation and produce an adequate
bitmap on the fly.
The process of moving from the “vector outline” state to the “bitmap” state is called
rasterization. It is a crucial process because the final appearance of the text depends on it.
To understand the value of this chapter, we must examine how rasterization is done.
Since pixels are—fortunately—equidistant, we can imagine that beneath the geometrically perfect outline of a glyph there is a grid each of whose squares has the size of one
pixel. Then rasterization involves filling in some of the squares of this grid to obtain as
faithful an approximation to the glyph’s outline as possible. Some of the squares—yes,
but which ones? Therein lies the problem.
We can adopt a methodical approach: for example, we can say that we shall fill in any
pixel whose center lies inside the outline (or on the outline). This method is very fragile: sometimes a very slight difference in an outline is enough to make the centers of
an entire row of pixels suddenly fall within the outline and thus be made black—or,
conversely, it may cause them to fall outside the outline and thus be made white. In the
example below, five versions of the letter ‘H’ with slightly different heights have been
rasterized using the method of the centers of the pixels.
```
