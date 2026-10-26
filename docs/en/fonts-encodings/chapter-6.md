---
title: "Chapter 6: Font Management on the Macintosh"
description: "Unabridged English text: Classic Mac OS 9 font architecture, resource forks, suitcases, QuickDraw, Mac OS X Quartz 2D, ATS, font management tools (ATM, Suitcase, FontAgent, Font Book), and TransType font conversion."
---

# Chapter 6: Font Management on the Macintosh
**By Yannis Haralambous, Ph.D.**
*From Fonts & Encodings, pp. 189–208*

---


Our concern in this chapter will be the installation and management of fonts under
Mac OS 9 and Mac OS X. The Mac OS 9 operating system is the fruit of a long devel-
opment process that began in 1984 with System 1.0, which came with the very ﬁrst
Macintosh. It is not astonishing that practically all extant types of fonts are found under
Mac OS 9. We shall begin by describing these types of fonts and giving a little glimpse at
font management à la Macintosh.
But Mac OS 9 will soon be nothing but a ﬂeeting memory, since Mac OS X, the new
Unix-based operating system, now comes standard on Macintoshes. At the beginning of
the twenty-ﬁrst century, Mac OS X aimed to simplify font management while also adding
new functionality. We shall discuss the new features in the second part of this chapter.
Nevertheless, one thing has remained unchanged throughout the long course of devel-
opment that led to Mac OS X: the ease of installing fonts. All that was necessary, dixit
Apple, was to place them in the system folder (under Mac OS 9 and earlier systems) or in one
of the designated folders (under Mac OS X). What more, then, need we say about installing
fonts on the Macintosh?
In fact, a number of factors combine to make font management on the Macintosh more
complex than Apple claims. First of all, fonts placed in the system folder are loaded into
memory; thus they take up RAM and slow down both booting and the launching of
applications (which systematically analyze the fonts contained in the system folder). Sec-
ond, fonts are ﬁles that remain permanently open and that can be corrupted upon the
slightest system crash. A corrupted font loaded by the system will cause a fatal system
crash. Such crashes are often fraught with consequences, and this type of corrupt ﬁle is
also diﬃcult to detect.
187


188
For all of these reasons, therefore, we are wise to use tools to manage our fonts, install
and uninstall them on the ﬂy, check their integrity and correct any problems that may
arise, and so forth. The third part of this chapter will be devoted to describing these tools.
Before discussing fonts, one quick word on managing ﬁles on the Macintosh. One of the
Mac’s idiosyncrasies is the dual nature of its ﬁles: every Macintosh ﬁle may have a part
containing data and a part containing resources [49, p. I-103]. A resource is a set of data
associated with a type (a string of four characters), a number, and possibly a name. As its
name suggests, the data part usually contains data, whereas the resource part contains
executable code, components of a user interface (menus, dialog windows, etc.), and all
sorts of other “resources”.
The two parts, data and resources, are connected in a transparent manner, and the Mac-
intosh windowing manager, called the Finder, displays only one object, represented by
an icon. A Macintosh ﬁle may lack a data part (as do some executable ﬁles, for example)
or a resource part. In the latter case, it is often represented by a “generic” icon in the
Finder.
This phenomenon occurs because the icons used to represent ﬁles are selected by the
Finder from two pieces of information contained not in the ﬁle itself but in the directory
of ﬁles on the disk’s partition: this information is also stored as strings of four characters
called the creator and the type of the ﬁle. Thanks to the “creator”, the Finder can launch
the correct application when we double-click on a ﬁle’s icon, wherever the application
may be stored on the disk(s). Thanks to the “type”, the application in question knows
what type of data we are providing. Owing to this approach, the Macintosh has never
needed to make recourse to ﬁlename extensions, which, however, are indispensable under
Windows and quite helpful under Unix.
Let us now move on to the special family of ﬁles that is of particular concern to us:
font ﬁles. In Figure 6-1 we see a certain number of Mac OS 9 icons that represent fonts.
Monaco and Optima are icons for “font suitcases”. These “suitcases” contain bitmap or
TrueType fonts. When we double-click on a suitcase (see Monaco in the ﬁgure), it opens
like any other ﬁle and displays a list of the fonts that it contains, which we can move at
will. Monaco-ISO-8859-1 9 and Charcoal are icons of bitmap and TrueType fonts
extracted from font suitcases. Conversely, TT0003C_.TTF is a Windows TrueType font
that is recognized as a TrueType font even though it comes from the Windows world
and is used as it is by Mac OS 9. Zapfino.dfont is a font of type dfont, which is speciﬁc to
Mac OS X: it is not recognized by Mac OS 9, which explains the lack of an icon particular
to it. FREESans.otf is an OpenType font.
The other ﬁles in the ﬁgure are all for PostScript Type 1 fonts. The ﬁrst three (DidotL-
HIta, TotoRom, FreeSan) were produced by three major font-design software packages:
Macromedia Fontographer, Letraset FontStudio, and FontLab. All the others come from
diﬀerent founderies: Adobe, Monotype, P22, Bitstream, ITC, Hoeﬂer, Paratype, Font-


189
Fontes PostScript de type 1
Type LWFN
Créateur variable
«Valises» de fonte
Type FFIL
Créateur DMOV
Fonte TrueType Mac
Type tfil
Créateur movr
Fonte TrueType Win
Type sfnt
Créateur movr
Fonte OpenType
Type sfnt
Créateur ATMC
Fonte Bitmap
Type ffil
Créateur movr
Fonte dfont
Non reconnue
sous MacOS 9
![Figure 6-1: A Mac OS 9 screenshot showing a certain number of Macintosh font files](/images/fonts-encodings/fig6-1.png)
Font, Agfa (before its merger with Monotype), URW, Font Bureau, Font Company, ATF
Kingsley, Esselte Letraset, Mecanorma, and Red Rooster.
Let us now take a closer look at these diﬀerent ﬁle types. First of all, note that we can
classify them into two categories from the point of view of their ﬁle structure: those—
the more recent ones—whose resource part is empty (the OpenType, dfont, and Windows
TrueType ﬁles), and those for which all the data is stored in the resources (all other ﬁles).
What about these resources?
The most interesting of them is the resource FOND [49, p. I-215], which is common to all
the Mac OS 9 font formats. It contains general information on bitmap, TrueType, and
PostScript Type 1 fonts. It never contains glyphs as such but merely pointers to resources
or ﬁles that do contain them. It has a name, and this name is, from the point of view of
the Macintosh system and its applications, the only name by which the font is recognized
and can be used. Beyond the name, it contains the following information:
• A font identiﬁcation number (which is in fact the number of the resource itself).
• Some technical information of no great importance.
• Some tables for width and kerning.


190
• Pointers to bitmap (FONT or NFNT) or TrueType (sfnt) resources, contained in the
same ﬁle. These resources are categorized according to point size (the resource for
TrueType fonts having a pseudo-value of 0 points) and the style (0 = regular, 1 = bold,
2 = italic, 3 = bold italic).
• The names of the PostScript fonts that correspond to these various styles.
We can now make three observations:
1. The importance of the identiﬁcation number
A font is identiﬁed under Mac OS 9 by its identiﬁcation number. This practice was
very eﬀective in 1985, when only a handful of Macintoshes were available; but it is
completely out of date today, when we may have tens of thousands of fonts at our
disposal. It opens the door to conﬂicting identiﬁcation numbers.
In older versions of Mac OS, a special utility was available for loading fonts onto
the system: Font/DA Mover (which gave us the “creator” DMOV and movr ﬁelds of the
“suitcase”, bitmap, and TrueType ﬁles). This utility resolved conﬂicts between identi-
ﬁcation numbers and checked the integrity of the internal links to resources in each
font ﬁle before copying it onto the system. In more recent versions of Mac OS, these
procedures are automatically performed when we install fonts by placing them in
the subfolder Fonts of the system folder, which is provided for this purpose.
The fact that the system changes the identiﬁcation number is obviously an improve-
ment, but it also implies that font ﬁles are modiﬁed by the system so that they can
be added to the existing repertoire of fonts—and this modiﬁcation occurs as soon
as the fonts are copied into the Fonts folder. That folder is thus very special, and its
contents must be handled with care. The font managers that we shall see below will
keep us from having to handle this folder directly.
2. A simplistic classiﬁcation of fonts
As we have seen, there are only four styles in a Macintosh “font family”, called “reg-
ular”, “bold”, “italic”, and “bold italic”. We therefore see only one name (the name of
the resource FOND) within applications, and we select among the four variants with
a “style” menu.
There is no way to have a single family with more style variants; if we need more, we
must resort to creating multiple families. Each of them will, accordingly, be consid-
ered a separate font by the system’s user interface and by applications.
This special characteristic of the Macintosh is at the heart of a number of night-
mares that plague the users of DTP software. For example, to set type in oblique
Optima, we may use either the “italic” style of the font Optima or a separate font
called Optima Oblique. Both of them may be associated with the same PostScript
font Optima-Oblique and may yield the same result. But that outcome depends com-
pletely on the conﬁguration of the font family in question. We have no a priori way
to know whether the foundry has supplied distinct Macintosh styles or distinct FOND


191
resources. And what happens if we inadvertently select the “italic” style of the font
Optima Oblique? Some software will go as far as to give the oblique version of Optima
an artiﬁcial slant, yielding a font that has been slanted twice!
Tools such as Adobe Type Reunion (ATR), which we shall describe below, attempt to
ameliorate this inconsistency by bringing the style variants of the same font together
on the user interface. Nevertheless, the problem is far from being resolved, and a
great deal of prudence is called for during the installation, modiﬁcation, or creation
of fonts.
3. Disparities in the data
FOND is, in a sense, the most important resource, as without it the Macintosh usually
cannot gain access to the data in a font. Nonetheless, we shall note that this resource
never appears in isolation. It is always accompanied by other resources, either in
the same ﬁle (as with the resources FONT and NFNT for bitmap fonts and sfnt for
TrueType fonts) or in other ﬁles (as with PostScript fonts, whose ﬁlenames have to
be computed from the names of the fonts1 contained in the resource FOND). Merely
breaking the link between these resources or ﬁles will render the font unusable.
A ﬁnal problem, of a diﬀerent sort, aﬀects PostScript fonts. For business reasons, no ver-
sion of Mac OS (before Mac OS X) wished to allow the possibility of using PostScript
fonts for display on the screen. A separate program (Adobe Type Manager, or ATM) as-
sumed that task. Mac OS itself uses only the bitmap fonts contained in the “font suitcase”;
thus, at a large point size, the system will have no choice but to magnify the pixels
of the bitmap fonts, and the result is a set of shapes that look like “staircases”. Using
PostScript fonts, in which the shapes are described by mathematical formulae, ATM pro-
duces bitmaps on the ﬂy, and the visual result is the smoothing of the glyphs. But its task is
quite complex: without being integrated into the system, it must intercept all requests by
diﬀerent programs to display a font, ﬁnd the correct bitmap fonts, track down the links
to the corresponding PostScript ﬁles, read the ﬁles, extract the descriptions of the glyphs,
and generate bitmaps on the ﬂy. All that has to happen in real time.
The more types of fonts we have, the more tools as well. It comes as no surprise that
font management on the Macintosh is a mineﬁeld. Before examining the diﬀerent tools
that allow users (including intense users) to survive unscathed, we shall make one quick
comment on developments since the move to Mac OS X.
Several years ago, before Steve Jobs returned to Apple, no one would have believed that
we could have a Unix operating system that was also a version of Mac OS. The feat was
to bring users the beneﬁts of Unix without losing the wealth of features acquired by the
various releases of Mac OS since 1984. Fonts were also aﬀected: we saw in the previous
1 The rule is as follows: Assume that the PostScript name is made of words in lowercase letters beginning
with a capital. We retain the ﬁrst ﬁve letters of the ﬁrst word and the ﬁrst three letters of each of the following
words. Thus, for example, Miracle-BoldItalic becomes MiracBolIta.


192
![Figure 6-2: The same files shown in Figure 6-1, as seen under Mac OS X](/images/fonts-encodings/fig6-2.png)
section the variety of ﬁle types in use (“font suitcases”, bitmaps, TrueType, PostScript,
OpenType, etc.). Obviously Mac OS X had to accept all these ﬁle formats, for reasons of
compatibility. But Mac OS X also aimed to simplify the existing order.
And simplify it did! In Figure 6-2 we see the same window shown in Figure 6-1, as it
appears under Mac OS X. What a surprise to see that all of the ﬁles described in the
preceding section, even though they are of very diﬀerent natures, are represented by the
same icon (a letter ‘A’ on a white background)! Even the ﬁle Zapfino.dfont uses this
icon, as it will henceforth be recognized by the operating system.2
Thus the system is capable of transparently recognizing and using all types of fonts (or
at least all those that were recognized3 by Mac OS 9) and furnishes a replacement for
“font suitcases”—a replacement that is essential so that Unix applications can make use
of the data.
2 Now is the time to remove the mystery that enshrouds this “new format”, which is not really a format
at all, as it is merely a “font suitcase” in which all the information that had been in the resource section has
been transferred unchanged to the data section. Thus it is a ﬁle that can be used by Unix applications but that
is functionally equivalent to the “font suitcases” that we have known since the release of the ﬁrst Mac in 1984.
3 With only one exception: the FONT resources still are not recognized by Mac OS X, which considers
them too old for its taste. Tools (such as FONT→NFNT [203] or fondu [351], for example) exist to replace
resources with NFNTs systematically. Another important detail: while “carbonized” applications continue to
work as before and to use bitmap fonts if they please, applications using the new Quartz graphical library will
be incompatible with bitmap fonts from now on. Those of us who have painstakingly created bitmap fonts to
resolve various practical problems now ﬁnd ourselves forced to vectorize them.


193
Now let us move on to the installation of fonts. Where should we place font ﬁles so that
they can be used by the system? Since Unix is a multiuser system, we need to manage
the permissions of users, and the same goes for fonts as well. At the same time, we must
not forget that Mac OS 9 is still with us, through the Classic environment. It is therefore
desirable to make the same fonts accessible on both Mac OS X and Mac OS 9 under
Classic. Apple has provided ﬁve diﬀerent locations to place (or not to place) font ﬁles
[202, 60]:
1. In ~/Library/Fonts, where ~ is the home directory of the active user. These fonts
are available to that user only.
2. In /Library/Fonts. These fonts are available to all local users. Only an administrator
may place fonts here.
3. In /Network/Library/Fonts. These fonts are available to all users on the local net-
work. Only a network administrator may place fonts here.
4. In /System/Library/Fonts. This is the location for system fonts. Apple encourages
us to leave this directory alone.
5. In the Mac OS 9 system folder. These fonts are available to all local users and also to
applications that run under Classic.
Thus everything depends on how we use our fonts. If we are in a modern environment in
which all the software is carbonized, or better yet in Cocoa, then there is no need to place
fonts into the Mac OS 9 system folder. This is especially true if we belong to a workgroup
that uses shared resources and we would also like to share private fonts without violating
the law, by making them accessible only to members of a certain group. In this case, all
that we have to do is to sort our fonts into private fonts, fonts that are locally public, and
fonts that are public at the network level, and place them in the appropriate location.
If, on the other hand, we still have to go through Classic in order to use our favorite appli-
cations, the issue of permissions does not arise; we simply place our fonts into the good
old system folder of Mac OS 9, and they will be accessible by both Mac OS 9 applications
and Mac OS X applications.
PostScript fonts are easier to use under Mac OS X. We no longer need ATM, the program
that used PostScript fonts associated with FOND to display smoothed glyphs on the screen.
Mac OS X itself interprets the PostScript code and smooths the glyphs.
Despite the large number of folders in which fonts may be found, Mac OS X has thus
managed to simplify the use of fonts: no longer do we have to worry about diﬀerences
in font type, as everything is processed in the same manner, and we no longer need a tool
external to the system in order to display PostScript fonts. But have the problems men-
tioned in the previous section—namely, the importance of the identiﬁcation number,
the simplistic classiﬁcation into styles, and the disparity of data ﬁles—been resolved?
Not at all. The identiﬁcation number is still with us, the styles are all the same (because
the new dfont are only ordinary “font suitcases” stored in a diﬀerent way on the disk),


194
and the disparity among ﬁles is the same (we still need two ﬁles for a single PostScript
font). The problems are all the same; they have just been hidden from the view of the end
user. The tools that help us to get around these problems are therefore as indispensable
as they ever were, and we shall now describe them, in the following section.
In this section, we shall describe a handful of tools that are useful, or even indispens-
able in certain cases, for the eﬀective management of fonts under Mac OS. We shall
describe only those tools that run under Mac OS X (while noting their compatibility with
Mac OS 9), except, of course, in the case of important tools that have not yet been ported
to OS X (such as ATM).
Tools for Veriﬁcation and Maintenance
We have already mentioned the dangers that fonts face under Mac OS—dangers stem-
ming primarily from the fact that the ﬁles that contain them are permanently left open,
since the system needs to have regular access to them in order to load the information
necessary for displaying text. A font ﬁle is in direct contact with the system; when the
system crashes, the ﬁle can also be aﬀected. This fact explains why fonts are the most
fragile ﬁles on the Macintosh. And a corrupted font is often the cause of new system
crashes.
If we have no cure for this situation, we can at least limit the damage by regularly check-
ing the status of our fonts and replacing with fresh copies those ﬁles that have been
corrupted. One popular tool for performing this sort of maintenance on the font reper-
toire is Font Doctor, by Morrison SoftDesign [275].
This tool allows us to verify and repair all the fonts contained in the folders speciﬁed by
the user. When repairs are impossible, the font is set aside in a special folder. Font Doctor
also plays a preventive role; thus it will warn the user if it ﬁnds duplicates of a font or
identical fonts in diﬀerent formats (for example, PostScript Type 1 and TrueType). Here
is the list of the operations carried out in the course of a “diagnostic” check on the fonts:
• Resolving conﬂicts in identiﬁcation numbers (the numbers of the resource FOND).
• Detecting duplicates (= fonts of the same format and of the same version that contain
the same glyphs).
• Deleting unwanted bitmap ﬁles in order to keep only one point size per font. Indeed,
since Mac OS X handles display at all sizes, bitmap fonts are in theory no longer
necessary. I say “in theory” because manually edited bitmap fonts will always be
better than those generated by the computer; thus we are wise to retain them. For
this reason, the automatic deletion of bitmap fonts is not always desirable.
• Detecting fonts that are available in several diﬀerent formats. We can specify that
priority should go to PostScript and OpenType fonts or to TrueType fonts.


195
![Figure 6-3: Font Doctor's configuration interface](/images/fonts-encodings/fig6-3.png)
• Detecting “orphaned bitmaps”. The term is ill chosen, as it applies not necessarily to
bitmaps but rather to FOND resources containing links to PostScript fonts that are not
available.
• Detecting “orphaned PostScript fonts”. Here we have the opposite situation: we have
a PostScript font but no FOND resource that would enable the system to recognize the
font in question. Note that when Font Doctor ﬁnds “orphaned bitmap fonts” and
“orphaned PostScript fonts” that correspond to them, it performs a “family reunion”
by re-creating the missing links.
• Verifying the integrity of the ﬁles. FOND and NFNT are checked for compliance with
Apple’s speciﬁcations. Font Doctor takes advantage of the procedure to replace old
FONT resources (which are no longer recognized by Mac OS X) with NFNT resources.


196
Note that Font Doctor will not usually correct a defective font when a major problem
arises but will rather warn you that a problem has been found. Thus you must use more
powerful font-editing tools to set the situation straight. For example, in the case of an
“orphaned PostScript font” for which no corresponding FOND can be found, only font-
design software such as FontLab can create the missing resource. We shall discuss this
sort of software in Chapter 12.
Other tools for verifying and maintaining fonts exist, but they are less eﬃcient and less
stable than Font Doctor. We may mention, by way of example, FontAgent, by Insider Soft-
ware [189], which has the beneﬁt of having a Windows version that is identical in every
detail to the Mac OS version.
ATM: the “Smoother” of Fonts
We have already mentioned ATM [18], a tool that is indispensable when we work with
PostScript fonts under Mac OS 9 or earlier. Its role is to read PostScript fonts pointed to
by FOND resources and to use the contours described therein to display glyphs at all sizes.
This operation, which seems trivial for TrueType fonts because Mac OS handles the dis-
play of TrueType glyphs at all sizes (using the contours contained in the resource sfnt), is
a little more diﬃcult for ATM, which has to ﬁnd the ﬁles containing PostScript data with
no other clue than the PostScript name of the font being sought (which rarely coincides
with the name of the ﬁle containing that font).
To facilitate the task of detecting ﬁles, Adobe also equipped ATM with features for man-
aging font ﬁles. Finally, ATM was released in two versions: ATM Light, the free version,
which only “smooths” glyphs, and the commercial version ATM Deluxe [17], which also
serves as a font manager and a tool for checking the integrity of fonts. Before delving
into font managers, we should say a few words about the “smoother”.
![Figure 6-4: The configuration interface of ATM](/images/fonts-encodings/fig6-4.png)
The conﬁguration interface of this program (Figure 6-4) is quite simple:


197
![Figure 6-5: The letters 'Aa' in Agfa's Throhand at 128 points, showing ATM glyph smoothing](/images/fonts-encodings/fig6-5.png)

*Figure 6-5: The letters 'Aa' in Agfa's Throhand at 128 points. Left: without ATM smoothing; right: with ATM smoothing.*
play without ATM; display with ATM but without glyph smoothing; and display with ATM and
with glyph smoothing.
• Enabling/disabling of the program.
• The amount of memory that we wish to dedicate to cache for glyphs. (This option
was important in the days when RAM on the Macintosh was on the order of a few
megabytes, which is no longer the case today.)
• A choice between giving priority to glyphs and giving priority to line spacing, when
ATM has to choose between preserving the shapes of glyphs and maintaining even
line spacing.
• Enabling of glyph smoothing. When smoothing is disabled, ATM uses only black
and white pixels; when smoothing is enabled, ATM also uses pixels along a grayscale
(an operation called anti-aliasing). It is important to remember to enable this option,
which makes a spectacular diﬀerence in the quality of the output (Figure 6-5).
• An option to enable smoothing through gray levels only for type at or above a certain
point size (which is not speciﬁed). As it happens, smoothing at small sizes is hardly
noticeable and only slows down the displaying of glyphs.
• An option for “precise positioning of the character”, which lets us increase the pre-
cision with which the positions of glyphs are calculated below the threshold of the
pixel. This feature will work only if it is supported by the software that displays
glyphs.
• Enabling font substitution. The same method used by Adobe Acrobat is also used
in ATM. When we know the widths of the glyphs in a font but do not have the font
itself, the corresponding glyphs in the Multiple Master fonts Adobe Serif MM or Adobe
Sans MM are displayed. This feature works quite well in Acrobat because the widths
of the glyphs must be supplied. ATM, however, cannot carry out the substitution un-
less it has access to these data. It therefore needs access to at least one FOND resource in
order to implement this method. The substitution aﬀects only “orphaned bitmaps”,


198
and no provision is made for documents that use fonts that are entirely unknown to
the system.
But automatic substitution poses another very serious problem, both to Acrobat and
to ATM: the fonts Adobe Serif MM and Adobe Sans MM contain only the glyphs needed
for a few Western European languages. Substitution fails when the missing glyphs
are symbols or letters in a non-Latin alphabet, or in the Latin alphabet but in a lan-
guage other than the favored ones of Western Europe. More speciﬁcally, either the
software is aware of the type of glyphs needed but fails to perform the substitution,
knowing that it is unable to carry it out, or it substitutes incorrect glyphs, thereby
mangling the document into illegible gibberish. Unfortunately, the latter seems to
happen most of the time, for the simple reason that most software identiﬁes glyphs
by their indexes in the font table and completely disregards their semantics and the
Unicode characters that correspond thereto.
Since ATM’s font substitution leaves much to be desired, we are still waiting for font
substitution worthy of Unicode.
• Create MM instances: here we are dealing with the creation of Multiple Master
instances. ATM examines the active fonts and selects those that are Multiple Masters.
For each of them, it displays (see Figure 6-6, left) the available axes of variation and
a sample (the word “Sample”). The user selects the desired values of the parameters
and requests the creation of an instance.4 ATM will then produce a FOND resource
and an NFNT resource, which it will add to the “font suitcase”. From that point on,
the instance is available to every application; it is identiﬁed by the values of its pa-
rameters on a submenu of the font-selection menu (see Figure 6-6, right).
![Figure 6-6: The interface for creating and selecting Multiple Master font instances](/images/fonts-encodings/fig6-6.png)
In conclusion, let us note that even though ATM is no longer necessary under Mac OS X
and Adobe has announced that it has halted development of this product, the latest ver-
4 Note that certain applications, such as Adobe Illustrator and Quark XPress, have their own internal
interface for creating Multiple Master instances. In this case, we can modify the font’s parameters in real time
to adapt it to the graphical context. ATM’s built-in interface will suﬃce for applications that have no interface
of their own.


199
sion of ATM Light (version 4.6.2) was developed with the intention that it be used under
Classic.
ATR: classiﬁcation of fonts by family
We have already mentioned the crude nature of the Macintosh’s classiﬁcation of fonts
by style. According to this classiﬁcation, only four possible style variants, called “regu-
lar”, “bold”, “italic”, and “bold italic”, are possible in a FOND resource. To associate other
variants with the same font, one must create a new FOND resource that is also supplied
with these same four predeﬁned styles.
Let us take an example. Suppose that we have at our disposal the Optima PostScript
fonts (by the great font designer Hermann Zapf) in the following styles: light, semi-bold,
bold, and extra-bold, each of them in vertical and oblique versions. To arrange them on
the Macintosh, one possibility would be to create two FOND resources called Optima and
Optima bold, respectively, and to create links to the PostScript fonts according to the
following correspondences:
Name of FOND resource
Macintosh style
PostScript font
Optima
“regular”
Optima
“bold”
Optima semi-bold
“italic”
Optima oblique
“bold italic”
Optima semi-bold oblique
Optima gras
“regular”
Optima bold
“bold”
Optima extra-bold
“italic”
Optima bold oblique
“bold italic”
Optima extra-bold oblique
When using a font, we would have to know that the choice of “Optima” in the “bold”
style is lighter than “Optima bold” in the “regular” style, which in turn is lighter than
“Optima bold” in the “bold” style. Another possibility (the more common choice) is to
create one family of Macintosh fonts with the light and (true) bold weights, and a second
family with semi-bold and extra-bold. This combination is less logical but corresponds
more closely to commercial needs: speciﬁcally, the foundry can produce two separate
products, of which the second is a sort of extension of the ﬁrst. Indeed, this is the ap-
proach followed by Linotype, which sells the font Optima in two sets of style variants,
with two overlapping pairs of bold weights.
The program Adobe Type Reunion (ATR) [19] frees us from these restrictions and aﬀords
us the possibility of choosing style variants in a more natural manner, using submenus.
But its most important beneﬁt is the possibility of specifying that a given PostScript font
belongs to a certain Macintosh font family, and even giving the name under which the
font will be displayed by the various applications. In Figure 6-7, we see the interface for
classifying font families and personalizing the names of the fonts. The same tool also


200
![Figure 6-7: The interface for classifying font families in Adobe ATM Deluxe](/images/fonts-encodings/fig6-7.png)
Type Reunion.
allows us to deﬁne groups of font families by adding a third level of classiﬁcation to the
font-selection menus.
Font Managers
What do we need in order to manage fonts eﬃciently? Imagine that we have thousands
of fonts—not an unrealistic proposition, if we work in a graphic-design studio. The fol-
lowing are the most frequent operations that we will have to perform:
1. Choosing the correct font for our project. At this time, software is not yet able to rec-
ommend a font according to the characteristics of the project that we have in mind,
but it can help us to create catalogues of type specimens from which our professional
experience will allow us to make the right choice.
2. Finding the font among the thousands in our possession. This operation may be
quite delicate because, as we have seen, we often have multiple copies of the same
font (or fonts with the same name), in diﬀerent formats, coming from diﬀerent
foundries, etc. Later in this book, we shall see the diﬀerences among font formats
and learn which are the most appropriate for each project. For now, what we can
expect of a font manager is to present the available choices in a convenient fashion
and to give us all the information that we need in order to make the decision.
3. Enabling the font, and thus allowing our software to make use of it, preferably with-
out having to restart the software or the computer.
4. Disabling the font once our work is ﬁnished and re-enabling it automatically when
we open a ﬁle in which it is used.


201
5. Rapidly assembling all of the fonts used in a ﬁle and copying them into a folder near
the ﬁle, if the ﬁle is to be sent to a colleague.
These are precisely the tasks performed by the four most popular font managers: Ap-
ple’s Font Book (which is part of Mac OS X 10.3+), FontAgent Pro by Insider Software, Font
Reserve (formerly by DiamondSoft [119], currently by Extensis), and Suitcase [132], also
by Extensis. Font Reserve was discontinued when DiamondSoft was bought by Extensis,
and its functionality was added to the latest version of Suitcase: Suitcase Fusion. A ﬁfth
competitor, ATM Deluxe [17], has unfortunately withdrawn from the race because it is not
compatible with Mac OS X. Adobe has announced that it has no intention to continue
its development. The abandonment of the “glyph smoother”, ATM, on the grounds that
it was no longer needed on Mac OS X also sounded the death knell for the font-manager
component of ATM Deluxe, which was nevertheless greatly appreciated by its users.
![Figure 6-8: Font Book v.1.0 (standard in Mac OS X 10.3+)](/images/fonts-encodings/fig6-8.png)
Font Book (see Figure 6-8), not to be confused with FontBook (by Lehmke Software), is
a relatively recent piece of software: its ﬁrst version came out only in System 10.3 (Pan-
ther). It is quite easy to use: it presents a list of fonts that can be enabled or disabled by
double-clicking. Single-clicking on a font gives us a specimen of its glyphs in the window
to the right. We can group fonts into “collections” (list at left), which allows us to enable
or disable all the fonts in a collection at the same time. These features stop here: there is
no cataloging, printing, or automatic enabling. Those features will doubtless be added
in future versions.
But there is one thing that Font Book does indirectly: when we use the Character Palette,
a utility for selecting Unicode characters that is launched through the entry with this
name on the keyboard menu (the keyboard menu is the one represented by a little ﬂag
corresponding to the active keyboard), an extra section at the bottom of the Character
Palette shows us all of the glyphs representing the selected character:


202
It is quite impressive. We even see the variants of glyphs, and we can select them by
clicking on them.
Let us move on to the leading software competitors: Suitcase Fusion (Figure 6-9) and
FontAgent Pro (Figure 6-10).
In both cases, we select individual fonts or entire directories to be analyzed by the pro-
gram, which will display them in the bottom part of the interface. In both programs,
we can create “sets” of fonts in the top part of the window and add fonts to those sets
by dragging them up from the bottom part of the window or directly from a disk. We
can thus enable or disable individual fonts or families or sets of fonts by clicking on
the button in the leftmost column. There are three possible states: disabled, temporarily
enabled (until the computer is rebooted or another font with the same name is enabled),
and permanently enabled.
Note that both programs allow fonts to be enabled automatically, with plug-ins for three
very popular pieces of software: Adobe Illustrator (since version 8), Adobe Photoshop (for
FontAgent Pro), Adobe InDesign (since version 2), and Quark XPress (since version 3.3).
These plug-ins analyze each open document and automatically enable every font con-
tained in the document and all the EPS ﬁles included in the document. If the exact font
cannot be found, they use a close substitute (for example, if a font of the same name but
of a diﬀerent format is available, they will use it instead).
As for displaying font specimens, Suitcase Fusion has a vertical area and FontAgent Pro a
horizontal one; both are permanently left open and can be customized. Both programs
can show a “waterfall” (diﬀerent sizes of the same text), a paragraph of text, or just a few
glyphs. Suitcase Fusion can show all styles of the same family simultaneously; that is why
the area is vertical. Both programs can display a certain amount of information about a
font upon request.
Finally, a very interesting feature: the ability to create catalogs of type specimens. Suitcase
Fusion has a utility called FontBook (not to be confused with Font Book, the program
built into Mac OS X 10.3+) that does an admirable job of generating type specimens,
but only for enabled fonts—a limitation that hampers the creation of a catalog for a
very large collection. In Figure 6-11 we see two examples of specimens created by Font
Book. There is a multitude of other “catalogers” of fonts, all with more or less similar
functionality.


203
![Figure 6-9: Extensis Suitcase Fusion](/images/fonts-encodings/fig6-9.png)
![Figure 6-10: Insider Software FontAgent Pro](/images/fonts-encodings/fig6-10.png)


204
![Figure 6-11: Two specimens created by FontBook v.4.4](/images/fonts-encodings/fig6-11.png)
most admirable reconstructions of historic fonts, with a simulated eﬀect of the bleeding of ink:
Historical Fell Type and Historical English Textura, by Jonathan Hoeﬂer.
Font Servers
The two major font managers FontAgent and Suitcase Fusion are also available in a
client-server version. The aim to is centralize font management at the level of a local
network by using one machine as the server and installing clients (which are simply the
regular versions of the two programs) on each machine.
Suitcase Server runs on Mac OS X and Windows NT, 2000, or XP, while FontAgent Pro Server
runs only under Mac OS X. Both manage users (by arranging them into workgroups and
assigning individual permissions to them) as well as fonts (by classifying them into sets
in the style of their clients). Authorized users may place fonts on the server from their
client station by simply dragging and dropping icons. In fact, servers can be administered
from any client station; the administrator’s password is all that is required. That approach
allows us to place the server’s machine where it ought to be—i.e., in a locked cabinet—
and to manage the software from any station, an ideal solution for small workgroups in
which users take turns serving as the administrator.
A feature of Suitcase Server that is very attractive to foundries is control over licenses.
Simply specify to Suitcase Server the type of rights that have been purchased for each


205
font5(e.g., the number of simultaneous user stations), and the software will alert the
administrator if the maximum number of users is exceeded. The documentation does
not state whether Suitcase Server sends a message at the same time to the foundry and
the nearest police station. Joking aside, this feature allows professionals in printing and
the graphic arts to obey the law without much worry.
Note that when a client connects to a server in order to use a font, the font is copied onto
the client’s hard disk. That approach is not really consistent with the general principles
of client-server architecture: why not directly use the copy of the font that resides on
the server? There are two possible answers to that question. First, as we have already
observed several times, fonts are fragile objects that are threatened by system crashes
(although crashes are not supposed to occur under Mac OS X!). By maintaining a clean,
fresh copy, we can always rapidly clean up the mess left by a crash, without risk of mistak-
ing the font for another one with the same name. The second reason (drawn from the
commercial literature of both servers) is that the network could also go down; in that
case, if no copy of the font were available locally on the disk, the user would ﬁnd himself
out of service, even for the documents on which he was currently working. Is that really
a valid argument in favor of copying the ﬁles onto the client’s machine, or just a feeble
excuse? Let the reader decide.
Today we are more and more in the habit of using multiple operating systems: Mac OS 9,
Mac OS X, Windows, Linux, PalmOS, Symbian, etc. These systems do not always use
the same font formats; therefore, we must be able to convert our fonts so that we can
use them on more than one system. Conversion can be trivial or complicated. Moving
from the Macintosh PostScript format to PFB is trivial: practically nothing is involved
other than reading the PostScript code in the POST resource and writing it out to a ﬁle.
Converting a TrueType font to PostScript or vice versa is much less trivial: the types of
contours change between cubic and quadratic Bézier curves; the techniques for optimiz-
ing the rendering are fundamentally diﬀerent; the means of encoding the glyphs are not
the same.
Thus it is hardly surprising that there is a dearth of tools for converting fonts on the
market; after all, it is a very thorny task.
TransType Pro
The company FontLab oﬀers the only really solid tool: TransType Pro [139]. What could
be more natural than to take a part of FontLab’s code and transform it into a powerful,
easy-to-use conversion utility?
TransType Pro can perform all possible and imaginable conversions among TrueType,
PostScript Type 1, Multiple Master and OpenType/CFF fonts—from Mac to Mac, or from
5 Unfortunately, this is not handled automatically for PostScript fonts because there is no standard way
to provide the information within each font. The problem has, however, been corrected in TrueType fonts, in
which the table OS/2 contains these data (§D.4.7).


206
![Figure 6-12: The main window of TransType Pro](/images/fonts-encodings/fig6-12.png)
Mac to PC, or from PC to Mac, or from PC to PC. When the target is a Macintosh font
suitcase, the program automatically assembles the fonts of the same family. When it
converts a Multiple Master font to an ordinary font, it can create any desired instance.
When it converts an OpenType or an AAT font between the Macintosh and Windows, it
preserves the advanced typographic tables.
The most interesting feature of TransType Pro is indisputably its batch processing of
fonts. You have a CD-ROM full of fonts in PFB format that you would like to use under
Mac OS X? All that you need to do is drag the disk’s image and drop it onto the left-hand
zone of TransType Pro’s window. The fonts will then appear, and, at the same time, on the
right-hand side of the window, we shall see the list of Macintosh font suitcases that the
software is planning to create. We can modify our font-conversion preferences separately
for each font or for several, even all of them, at a time. The names of Macintosh families
can be manually edited. When we click on the button with the spiral-shaped icon, all
of the fonts will be converted, with no other action on our part than the choice of the
target folder. A real godsend when we have thousands of fonts to convert.
dfontiﬁer
This little utility [121] fulﬁlls a role that TransType overlooked: converting a Macintosh
font suitcase to a dfont ﬁle and vice versa. We drag and drop fonts onto the window in
order to convert from one format to the other: it is simple, useful, and, moreover, free.


207
FontFlasher, the “Kobayashi Maru” of Fonts
According to the company FontLab, the purpose of this software, which in fact is a plug-
in for FontLab, is to produce bitmap fonts that can be displayed under Macromedia Flash
without anti-aliasing. The intention is praiseworthy: it is true that bitmap fonts at small
sizes are more legible when they are displayed with simple black-and-white pixels rather
than with levels of gray.
But how can we control the display on a given machine? How can we be sure that anti-
aliasing will not be performed? It is, a priori, impossible to be sure. The computer always
has the last word.
The reader must surely be wondering why we have called this software a “kobayashi
maru”. The story [128] has it that Captain James Kirk had to take a ﬁnal test in a ﬂight
simulator in order to obtain his diploma. On this test, the Enterprise received a call for
help from a vessel called Kobayashi Maru (the word “maru”, in fact, is used after ship
names in Japanese) in the Klingon territories. The captain was morally obliged to go to
the aid of the vessel. But the request was a trap. The Klingons attacked the Enterprise and
destroyed it. End of test. And an inevitable outcome, because refusing to assist a vessel
in distress would have been an equally bad solution.
That is why “kobayashi maru” has come to denote, in hacker jargon, a no-win situation.
What, then, did our Captain Kirk do? The night before the test, he broke into the com-
puter room and modiﬁed the program. The Kobayashi Maru was not a trap any longer. In
a word, he cheated. But one has the right to cheat when a vessel and its crew are at risk.
What does that have to do with FontFlasher? Well, here we ﬁnd ourselves in a kobayashi
maru: how on earth can we force the operating system not to anti-alias a font?
By cheating. If the operating system anti-aliases all fonts, let us give it a font that it will
not have to anti-alias. And the only font that it will not anti-alias is a font that already
has the precise shape of the pixels. If the pixels on the screen correspond with absolute
precision to the font’s vector contours, there will be nothing to anti-alias.
This is precisely what FontFlasher does. It generates a vector contour that is identical to
the pixels. At the given size, this contour yields a perfect “bitmap” font—which, at any
other size, is a catastrophe.
Given so many ways to obtain bitmap fonts once again, as in the good old days of Mac-
intosh System 4.3, we may well ask the question:
The image above is a screenshot of text in 11-point Futura and in Futura processed by
FontFlasher. Here is what we get at high resolution:


208
What is more readible, this vector font with anti-aliasing
or this simulation  of bitmap font with pixels given by outlines?
(Note that we have not manually retouched the glyphs of the processed font; we have
shown the raw rendering.) And here, under FontLab, is the raw output of FontFlasher,
in which each pixel is a vector-drawn square; at right, the same glyph after retouching
and merger of the squares:
In the background, we can see the vector contour of the glyph in the original font.
