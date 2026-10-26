---
title: "Chapter 6: Font Management on the Macintosh"
description: "Unabridged English text: Macintosh resource forks and data forks, suitcases, Mac OS X font domains, Font Book, Core Graphics text rendering."
---

# Chapter 6: Font Management on the Macintosh
**By Yannis Haralambous, Ph.D.**
*From Fonts & Encodings, pp. 189–208*

---

For all of these reasons, therefore, we are wise to use tools to manage our fonts, install
and uninstall them on the fly, check their integrity and correct any problems that may
arise, and so forth. The third part of this chapter will be devoted to describing these tools.
The Situation under Mac OS 9
Before discussing fonts, one quick word on managing files on the Macintosh. One of the
Mac’s idiosyncrasies is the dual nature of its files: every Macintosh file may have a part
containing data and a part containing resources [49, p. I-103]. A resource is a set of data
associated with a type (a string of four characters), a number, and possibly a name. As its
name suggests, the data part usually contains data, whereas the resource part contains
executable code, components of a user interface (menus, dialog windows, etc.), and all
sorts of other “resources”.
The two parts, data and resources, are connected in a transparent manner, and the Macintosh windowing manager, called the Finder, displays only one object, represented by
an icon. A Macintosh file may lack a data part (as do some executable files, for example)
or a resource part. In the latter case, it is often represented by a “generic” icon in the
Finder.
This phenomenon occurs because the icons used to represent files are selected by the
Finder from two pieces of information contained not in the file itself but in the directory
of files on the disk’s partition: this information is also stored as strings of four characters
called the creator and the type of the file. Thanks to the “creator”, the Finder can launch
the correct application when we double-click on a file’s icon, wherever the application
may be stored on the disk(s). Thanks to the “type”, the application in question knows
what type of data we are providing. Owing to this approach, the Macintosh has never
needed to make recourse to filename extensions, which, however, are indispensable under
Windows and quite helpful under Unix.
Let us now move on to the special family of files that is of particular concern to us:
font files. In Figure 6-1 we see a certain number of Mac OS 9 icons that represent fonts.
Monaco and Optima are icons for “font suitcases”. These “suitcases” contain bitmap or
TrueType fonts. When we double-click on a suitcase (see Monaco in the figure), it opens
like any other file and displays a list of the fonts that it contains, which we can move at
will. Monaco-ISO-8859-1 9 and Charcoal are icons of bitmap and TrueType fonts
extracted from font suitcases. Conversely, TT0003C_.TTF is a Windows TrueType font
that is recognized as a TrueType font even though it comes from the Windows world
and is used as it is by Mac OS 9. Zapfino.dfont is a font of type dfont, which is specific to
Mac OS X: it is not recognized by Mac OS 9, which explains the lack of an icon particular
to it. FREESans.otf is an OpenType font.
The other files in the figure are all for PostScript Type 1 fonts. The first three (DidotLHIta, TotoRom, FreeSan) were produced by three major font-design software packages:
Macromedia Fontographer, Letraset FontStudio, and FontLab. All the others come from
different founderies: Adobe, Monotype, P22, Bitstream, ITC, Hoefler, Paratype, Font-

![Figure 6-1: Mac OS 9 font files and suitcases](/images/fonts-encodings/fig6-1-macos9-font-files.png)
*Figure 6-1: Mac OS 9 font files and suitcases.*

The Situation under Mac OS 9
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
Figure 6-1: A Mac OS 9 screenshot showing a certain number of Macintosh font files.
Font, Agfa (before its merger with Monotype), URW, Font Bureau, Font Company, ATF
Kingsley, Esselte Letraset, Mecanorma, and Red Rooster.
Let us now take a closer look at these different file types. First of all, note that we can
classify them into two categories from the point of view of their file structure: those—
the more recent ones—whose resource part is empty (the OpenType, dfont, and Windows
TrueType files), and those for which all the data is stored in the resources (all other files).
What about these resources?
The most interesting of them is the resource FOND [49, p. I-215], which is common to all
the Mac OS 9 font formats. It contains general information on bitmap, TrueType, and
PostScript Type 1 fonts. It never contains glyphs as such but merely pointers to resources
or files that do contain them. It has a name, and this name is, from the point of view of
the Macintosh system and its applications, the only name by which the font is recognized
and can be used. Beyond the name, it contains the following information:
• A font identification number (which is in fact the number of the resource itself).
• Some technical information of no great importance.
• Some tables for width and kerning.

• Pointers to bitmap (FONT or NFNT) or TrueType (sfnt) resources, contained in the
same file. These resources are categorized according to point size (the resource for
TrueType fonts having a pseudo-value of 0 points) and the style (0 = regular, 1 = bold,
2 = italic, 3 = bold italic).
• The names of the PostScript fonts that correspond to these various styles.
We can now make three observations:
1. The importance of the identification number
A font is identified under Mac OS 9 by its identification number. This practice was
very effective in 1985, when only a handful of Macintoshes were available; but it is
completely out of date today, when we may have tens of thousands of fonts at our
disposal. It opens the door to conflicting identification numbers.
In older versions of Mac OS, a special utility was available for loading fonts onto
the system: Font/DA Mover (which gave us the “creator” DMOV and movr fields of the
“suitcase”, bitmap, and TrueType files). This utility resolved conflicts between identification numbers and checked the integrity of the internal links to resources in each
font file before copying it onto the system. In more recent versions of Mac OS, these
procedures are automatically performed when we install fonts by placing them in
the subfolder Fonts of the system folder, which is provided for this purpose.
The fact that the system changes the identification number is obviously an improvement, but it also implies that font files are modified by the system so that they can
be added to the existing repertoire of fonts—and this modification occurs as soon
as the fonts are copied into the Fonts folder. That folder is thus very special, and its
contents must be handled with care. The font managers that we shall see below will
keep us from having to handle this folder directly.
2. A simplistic classification of fonts
As we have seen, there are only four styles in a Macintosh “font family”, called “regular”, “bold”, “italic”, and “bold italic”. We therefore see only one name (the name of
the resource FOND) within applications, and we select among the four variants with
a “style” menu.
There is no way to have a single family with more style variants; if we need more, we
must resort to creating multiple families. Each of them will, accordingly, be considered a separate font by the system’s user interface and by applications.
This special characteristic of the Macintosh is at the heart of a number of nightmares that plague the users of DTP software. For example, to set type in oblique
Optima, we may use either the “italic” style of the font Optima or a separate font
called Optima Oblique. Both of them may be associated with the same PostScript
font Optima-Oblique and may yield the same result. But that outcome depends completely on the configuration of the font family in question. We have no a priori way
to know whether the foundry has supplied distinct Macintosh styles or distinct FOND

The situation under Mac OS X
resources. And what happens if we inadvertently select the “italic” style of the font
Optima Oblique? Some software will go as far as to give the oblique version of Optima
an artificial slant, yielding a font that has been slanted twice!
Tools such as Adobe Type Reunion (ATR), which we shall describe below, attempt to
ameliorate this inconsistency by bringing the style variants of the same font together
on the user interface. Nevertheless, the problem is far from being resolved, and a
great deal of prudence is called for during the installation, modification, or creation
of fonts.
3. Disparities in the data
FOND is, in a sense, the most important resource, as without it the Macintosh usually
cannot gain access to the data in a font. Nonetheless, we shall note that this resource
never appears in isolation. It is always accompanied by other resources, either in
the same file (as with the resources FONT and NFNT for bitmap fonts and sfnt for
TrueType fonts) or in other files (as with PostScript fonts, whose filenames have to
be computed from the names of the fonts1 contained in the resource FOND). Merely
breaking the link between these resources or files will render the font unusable.
A final problem, of a different sort, affects PostScript fonts. For business reasons, no version of Mac OS (before Mac OS X) wished to allow the possibility of using PostScript
fonts for display on the screen. A separate program (Adobe Type Manager, or ATM) assumed that task. Mac OS itself uses only the bitmap fonts contained in the “font suitcase”;
thus, at a large point size, the system will have no choice but to magnify the pixels
of the bitmap fonts, and the result is a set of shapes that look like “staircases”. Using
PostScript fonts, in which the shapes are described by mathematical formulae, ATM produces bitmaps on the fly, and the visual result is the smoothing of the glyphs. But its task is
quite complex: without being integrated into the system, it must intercept all requests by
different programs to display a font, find the correct bitmap fonts, track down the links
to the corresponding PostScript files, read the files, extract the descriptions of the glyphs,
and generate bitmaps on the fly. All that has to happen in real time.
The more types of fonts we have, the more tools as well. It comes as no surprise that
font management on the Macintosh is a minefield. Before examining the different tools
that allow users (including intense users) to survive unscathed, we shall make one quick
comment on developments since the move to Mac OS X.
The situation under Mac OS X
Several years ago, before Steve Jobs returned to Apple, no one would have believed that
we could have a Unix operating system that was also a version of Mac OS. The feat was
to bring users the benefits of Unix without losing the wealth of features acquired by the
various releases of Mac OS since 1984. Fonts were also affected: we saw in the previous
1 The rule is as follows: Assume that the PostScript name is made of words in lowercase letters beginning
with a capital. We retain the first five letters of the first word and the first three letters of each of the following
words. Thus, for example, Miracle-BoldItalic becomes MiracBolIta.

Figure 6-2: The same file that is shown in Figure 6-1, as seen under Mac OS X.
section the variety of file types in use (“font suitcases”, bitmaps, TrueType, PostScript,
OpenType, etc.). Obviously Mac OS X had to accept all these file formats, for reasons of
compatibility. But Mac OS X also aimed to simplify the existing order.
And simplify it did! In Figure 6-2 we see the same window shown in Figure 6-1, as it
appears under Mac OS X. What a surprise to see that all of the files described in the
preceding section, even though they are of very different natures, are represented by the
same icon (a letter ‘A’ on a white background)! Even the file Zapfino.dfont uses this
icon, as it will henceforth be recognized by the operating system.2
Thus the system is capable of transparently recognizing and using all types of fonts (or
at least all those that were recognized3 by Mac OS 9) and furnishes a replacement for
“font suitcases”—a replacement that is essential so that Unix applications can make use
of the data.
2 Now is the time to remove the mystery that enshrouds this “new format”, which is not really a format
at all, as it is merely a “font suitcase” in which all the information that had been in the resource section has
been transferred unchanged to the data section. Thus it is a file that can be used by Unix applications but that
is functionally equivalent to the “font suitcases” that we have known since the release of the first Mac in 1984.
3 With only one exception: the FONT resources still are not recognized by Mac OS X, which considers
them too old for its taste. Tools (such as FONT→NFNT [203] or fondu [351], for example) exist to replace
resources with NFNTs systematically. Another important detail: while “carbonized” applications continue to
work as before and to use bitmap fonts if they please, applications using the new Quartz graphical library will
be incompatible with bitmap fonts from now on. Those of us who have painstakingly created bitmap fonts to
resolve various practical problems now find ourselves forced to vectorize them.

The situation under Mac OS X
Now let us move on to the installation of fonts. Where should we place font files so that
they can be used by the system? Since Unix is a multiuser system, we need to manage
the permissions of users, and the same goes for fonts as well. At the same time, we must
not forget that Mac OS 9 is still with us, through the Classic environment. It is therefore
desirable to make the same fonts accessible on both Mac OS X and Mac OS 9 under
Classic. Apple has provided five different locations to place (or not to place) font files
[202, 60]:
1. In ~/Library/Fonts, where ~ is the home directory of the active user. These fonts
are available to that user only.
2. In /Library/Fonts. These fonts are available to all local users. Only an administrator
may place fonts here.
3. In /Network/Library/Fonts. These fonts are available to all users on the local network. Only a network administrator may place fonts here.
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
If, on the other hand, we still have to go through Classic in order to use our favorite applications, the issue of permissions does not arise; we simply place our fonts into the good
old system folder of Mac OS 9, and they will be accessible by both Mac OS 9 applications
and Mac OS X applications.
PostScript fonts are easier to use under Mac OS X. We no longer need ATM, the program
that used PostScript fonts associated with FOND to display smoothed glyphs on the screen.
Mac OS X itself interprets the PostScript code and smooths the glyphs.
Despite the large number of folders in which fonts may be found, Mac OS X has thus
managed to simplify the use of fonts: no longer do we have to worry about differences
in font type, as everything is processed in the same manner, and we no longer need a tool
external to the system in order to display PostScript fonts. But have the problems mentioned in the previous section—namely, the importance of the identification number,
the simplistic classification into styles, and the disparity of data files—been resolved?
Not at all. The identification number is still with us, the styles are all the same (because
the new dfont are only ordinary “font suitcases” stored in a different way on the disk),

and the disparity among files is the same (we still need two files for a single PostScript
font). The problems are all the same; they have just been hidden from the view of the end
user. The tools that help us to get around these problems are therefore as indispensable
as they ever were, and we shall now describe them, in the following section.
Font-Management Tools
In this section, we shall describe a handful of tools that are useful, or even indispensable in certain cases, for the effective management of fonts under Mac OS. We shall
describe only those tools that run under Mac OS X (while noting their compatibility with
Mac OS 9), except, of course, in the case of important tools that have not yet been ported
to OS X (such as ATM).
Tools for Verification and Maintenance
We have already mentioned the dangers that fonts face under Mac OS—dangers stemming primarily from the fact that the files that contain them are permanently left open,
since the system needs to have regular access to them in order to load the information
necessary for displaying text. A font file is in direct contact with the system; when the
system crashes, the file can also be affected. This fact explains why fonts are the most
fragile files on the Macintosh. And a corrupted font is often the cause of new system
crashes.
If we have no cure for this situation, we can at least limit the damage by regularly checking the status of our fonts and replacing with fresh copies those files that have been
corrupted. One popular tool for performing this sort of maintenance on the font repertoire is Font Doctor, by Morrison SoftDesign [275].
This tool allows us to verify and repair all the fonts contained in the folders specified by
the user. When repairs are impossible, the font is set aside in a special folder. Font Doctor
also plays a preventive role; thus it will warn the user if it finds duplicates of a font or
identical fonts in different formats (for example, PostScript Type 1 and TrueType). Here
is the list of the operations carried out in the course of a “diagnostic” check on the fonts:
• Resolving conflicts in identification numbers (the numbers of the resource FOND).
• Detecting duplicates (= fonts of the same format and of the same version that contain
the same glyphs).
• Deleting unwanted bitmap files in order to keep only one point size per font. Indeed,
since Mac OS X handles display at all sizes, bitmap fonts are in theory no longer
necessary. I say “in theory” because manually edited bitmap fonts will always be
better than those generated by the computer; thus we are wise to retain them. For
this reason, the automatic deletion of bitmap fonts is not always desirable.
• Detecting fonts that are available in several different formats. We can specify that
priority should go to PostScript and OpenType fonts or to TrueType fonts.

Font-Management Tools
Figure 6-3: Font Doctor’s configuration interface.
• Detecting “orphaned bitmaps”. The term is ill chosen, as it applies not necessarily to
bitmaps but rather to FOND resources containing links to PostScript fonts that are not
available.
• Detecting “orphaned PostScript fonts”. Here we have the opposite situation: we have
a PostScript font but no FOND resource that would enable the system to recognize the
font in question. Note that when Font Doctor finds “orphaned bitmap fonts” and
“orphaned PostScript fonts” that correspond to them, it performs a “family reunion”
by re-creating the missing links.
• Verifying the integrity of the files. FOND and NFNT are checked for compliance with
Apple’s specifications. Font Doctor takes advantage of the procedure to replace old
FONT resources (which are no longer recognized by Mac OS X) with NFNT resources.

Note that Font Doctor will not usually correct a defective font when a major problem
arises but will rather warn you that a problem has been found. Thus you must use more
powerful font-editing tools to set the situation straight. For example, in the case of an
“orphaned PostScript font” for which no corresponding FOND can be found, only fontdesign software such as FontLab can create the missing resource. We shall discuss this
sort of software in Chapter 12.
Other tools for verifying and maintaining fonts exist, but they are less efficient and less
stable than Font Doctor. We may mention, by way of example, FontAgent, by Insider Software [189], which has the benefit of having a Windows version that is identical in every
detail to the Mac OS version.
ATM: the “Smoother” of Fonts
We have already mentioned ATM [18], a tool that is indispensable when we work with
PostScript fonts under Mac OS 9 or earlier. Its role is to read PostScript fonts pointed to
by FOND resources and to use the contours described therein to display glyphs at all sizes.
This operation, which seems trivial for TrueType fonts because Mac OS handles the display of TrueType glyphs at all sizes (using the contours contained in the resource sfnt), is
a little more difficult for ATM, which has to find the files containing PostScript data with
no other clue than the PostScript name of the font being sought (which rarely coincides
with the name of the file containing that font).
To facilitate the task of detecting files, Adobe also equipped ATM with features for managing font files. Finally, ATM was released in two versions: ATM Light, the free version,
which only “smooths” glyphs, and the commercial version ATM Deluxe [17], which also
serves as a font manager and a tool for checking the integrity of fonts. Before delving
into font managers, we should say a few words about the “smoother”.
Figure 6-4: The configuration interface of ATM.
The configuration interface of this program (Figure 6-4) is quite simple:

Font-Management Tools
Figure 6-5: The letters ‘Aa’ in Agfa’s splendid font Throhand, at 128 points. From the left: display without ATM; display with ATM but without glyph smoothing; and display with ATM and
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
which makes a spectacular difference in the quality of the output (Figure 6-5).
• An option to enable smoothing through gray levels only for type at or above a certain
point size (which is not specified). As it happens, smoothing at small sizes is hardly
noticeable and only slows down the displaying of glyphs.
• An option for “precise positioning of the character”, which lets us increase the precision with which the positions of glyphs are calculated below the threshold of the
pixel. This feature will work only if it is supported by the software that displays
glyphs.
• Enabling font substitution. The same method used by Adobe Acrobat is also used
in ATM. When we know the widths of the glyphs in a font but do not have the font
itself, the corresponding glyphs in the Multiple Master fonts Adobe Serif MM or Adobe
Sans MM are displayed. This feature works quite well in Acrobat because the widths
of the glyphs must be supplied. ATM, however, cannot carry out the substitution unless it has access to these data. It therefore needs access to at least one FOND resource in
order to implement this method. The substitution affects only “orphaned bitmaps”,

and no provision is made for documents that use fonts that are entirely unknown to
the system.
But automatic substitution poses another very serious problem, both to Acrobat and
to ATM: the fonts Adobe Serif MM and Adobe Sans MM contain only the glyphs needed
for a few Western European languages. Substitution fails when the missing glyphs
are symbols or letters in a non-Latin alphabet, or in the Latin alphabet but in a language other than the favored ones of Western Europe. More specifically, either the
software is aware of the type of glyphs needed but fails to perform the substitution,
knowing that it is unable to carry it out, or it substitutes incorrect glyphs, thereby
mangling the document into illegible gibberish. Unfortunately, the latter seems to
happen most of the time, for the simple reason that most software identifies glyphs
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
the instance is available to every application; it is identified by the values of its parameters on a submenu of the font-selection menu (see Figure 6-6, right).
Figure 6-6: The interface for creating and selecting Multiple Master font instances.
In conclusion, let us note that even though ATM is no longer necessary under Mac OS X
and Adobe has announced that it has halted development of this product, the latest ver4 Note that certain applications, such as Adobe Illustrator and Quark XPress, have their own internal
interface for creating Multiple Master instances. In this case, we can modify the font’s parameters in real time
to adapt it to the graphical context. ATM’s built-in interface will suffice for applications that have no interface
of their own.

Font-Management Tools
sion of ATM Light (version 4.6.2) was developed with the intention that it be used under
Classic.
ATR: classification of fonts by family
We have already mentioned the crude nature of the Macintosh’s classification of fonts
by style. According to this classification, only four possible style variants, called “regular”, “bold”, “italic”, and “bold italic”, are possible in a FOND resource. To associate other
variants with the same font, one must create a new FOND resource that is also supplied
with these same four predefined styles.
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
more closely to commercial needs: specifically, the foundry can produce two separate
products, of which the second is a sort of extension of the first. Indeed, this is the approach followed by Linotype, which sells the font Optima in two sets of style variants,
with two overlapping pairs of bold weights.
The program Adobe Type Reunion (ATR) [19] frees us from these restrictions and affords
us the possibility of choosing style variants in a more natural manner, using submenus.
But its most important benefit is the possibility of specifying that a given PostScript font
belongs to a certain Macintosh font family, and even giving the name under which the
font will be displayed by the various applications. In Figure 6-7, we see the interface for
classifying font families and personalizing the names of the fonts. The same tool also

Figure 6-7: The interface for classifying font families and personalizing font names in Adobe
Type Reunion.
allows us to define groups of font families by adding a third level of classification to the
font-selection menus.
Font Managers
What do we need in order to manage fonts efficiently? Imagine that we have thousands
of fonts—not an unrealistic proposition, if we work in a graphic-design studio. The following are the most frequent operations that we will have to perform:
1. Choosing the correct font for our project. At this time, software is not yet able to recommend a font according to the characteristics of the project that we have in mind,
but it can help us to create catalogues of type specimens from which our professional
experience will allow us to make the right choice.
2. Finding the font among the thousands in our possession. This operation may be
quite delicate because, as we have seen, we often have multiple copies of the same
font (or fonts with the same name), in different formats, coming from different
foundries, etc. Later in this book, we shall see the differences among font formats
and learn which are the most appropriate for each project. For now, what we can
expect of a font manager is to present the available choices in a convenient fashion
and to give us all the information that we need in order to make the decision.
3. Enabling the font, and thus allowing our software to make use of it, preferably without having to restart the software or the computer.
4. Disabling the font once our work is finished and re-enabling it automatically when
we open a file in which it is used.

Font-Management Tools
5. Rapidly assembling all of the fonts used in a file and copying them into a folder near
the file, if the file is to be sent to a colleague.
These are precisely the tasks performed by the four most popular font managers: Apple’s Font Book (which is part of Mac OS X 10.3+), FontAgent Pro by Insider Software, Font
Reserve (formerly by DiamondSoft [119], currently by Extensis), and Suitcase [132], also
by Extensis. Font Reserve was discontinued when DiamondSoft was bought by Extensis,
and its functionality was added to the latest version of Suitcase: Suitcase Fusion. A fifth
competitor, ATM Deluxe [17], has unfortunately withdrawn from the race because it is not
compatible with Mac OS X. Adobe has announced that it has no intention to continue
its development. The abandonment of the “glyph smoother”, ATM, on the grounds that
it was no longer needed on Mac OS X also sounded the death knell for the font-manager
component of ATM Deluxe, which was nevertheless greatly appreciated by its users.
Figure 6-8: Font Book v.1.0 (which comes standard with Mac OS X 10.3+).
Font Book (see Figure 6-8), not to be confused with FontBook (by Lehmke Software), is
a relatively recent piece of software: its first version came out only in System 10.3 (Panther). It is quite easy to use: it presents a list of fonts that can be enabled or disabled by
double-clicking. Single-clicking on a font gives us a specimen of its glyphs in the window
to the right. We can group fonts into “collections” (list at left), which allows us to enable
or disable all the fonts in a collection at the same time. These features stop here: there is
no cataloging, printing, or automatic enabling. Those features will doubtless be added
in future versions.
But there is one thing that Font Book does indirectly: when we use the Character Palette,
a utility for selecting Unicode characters that is launched through the entry with this
name on the keyboard menu (the keyboard menu is the one represented by a little flag
corresponding to the active keyboard), an extra section at the bottom of the Character
Palette shows us all of the glyphs representing the selected character:

![Figure 6-8: Mac OS X Font Book](/images/fonts-encodings/fig6-8-macos-font-book.png)
*Figure 6-8: Mac OS X Font Book.*

It is quite impressive. We even see the variants of glyphs, and we can select them by
clicking on them.
Let us move on to the leading software competitors: Suitcase Fusion (Figure 6-9) and
FontAgent Pro (Figure 6-10).
In both cases, we select individual fonts or entire directories to be analyzed by the program, which will display them in the bottom part of the interface. In both programs,
we can create “sets” of fonts in the top part of the window and add fonts to those sets
by dragging them up from the bottom part of the window or directly from a disk. We
can thus enable or disable individual fonts or families or sets of fonts by clicking on
the button in the leftmost column. There are three possible states: disabled, temporarily
enabled (until the computer is rebooted or another font with the same name is enabled),
and permanently enabled.
Note that both programs allow fonts to be enabled automatically, with plug-ins for three
very popular pieces of software: Adobe Illustrator (since version 8), Adobe Photoshop (for
FontAgent Pro), Adobe InDesign (since version 2), and Quark XPress (since version 3.3).
These plug-ins analyze each open document and automatically enable every font contained in the document and all the EPS files included in the document. If the exact font
cannot be found, they use a close substitute (for example, if a font of the same name but
of a different format is available, they will use it instead).
As for displaying font specimens, Suitcase Fusion has a vertical area and FontAgent Pro a
horizontal one; both are permanently left open and can be customized. Both programs
can show a “waterfall” (different sizes of the same text), a paragraph of text, or just a few
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

Font-Management Tools
Figure 6-9: Suitcase Fusion.
Figure 6-10: FontAgent Pro.

Figure 6-11: Two specimens created by FontBook v.4.4. The fonts shown here are among the
most admirable reconstructions of historic fonts, with a simulated effect of the bleeding of ink:
Historical Fell Type and Historical English Textura, by Jonathan Hoefler.
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

Tools for Font Conversion
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
fresh copy, we can always rapidly clean up the mess left by a crash, without risk of mistaking the font for another one with the same name. The second reason (drawn from the
commercial literature of both servers) is that the network could also go down; in that
case, if no copy of the font were available locally on the disk, the user would find himself
out of service, even for the documents on which he was currently working. Is that really
a valid argument in favor of copying the files onto the client’s machine, or just a feeble
excuse? Let the reader decide.
Tools for Font Conversion
Today we are more and more in the habit of using multiple operating systems: Mac OS 9,
Mac OS X, Windows, Linux, PalmOS, Symbian, etc. These systems do not always use
the same font formats; therefore, we must be able to convert our fonts so that we can
use them on more than one system. Conversion can be trivial or complicated. Moving
from the Macintosh PostScript format to PFB is trivial: practically nothing is involved
other than reading the PostScript code in the POST resource and writing it out to a file.
Converting a TrueType font to PostScript or vice versa is much less trivial: the types of
contours change between cubic and quadratic Bézier curves; the techniques for optimizing the rendering are fundamentally different; the means of encoding the glyphs are not
the same.
Thus it is hardly surprising that there is a dearth of tools for converting fonts on the
market; after all, it is a very thorny task.
TransType Pro
The company FontLab offers the only really solid tool: TransType Pro [139]. What could
be more natural than to take a part of FontLab’s code and transform it into a powerful,
easy-to-use conversion utility?
TransType Pro can perform all possible and imaginable conversions among TrueType,
PostScript Type 1, Multiple Master and OpenType/CFF fonts—from Mac to Mac, or from
5 Unfortunately, this is not handled automatically for PostScript fonts because there is no standard way
to provide the information within each font. The problem has, however, been corrected in TrueType fonts, in
which the table OS/2 contains these data (§D.4.7).

Figure 6-12: The main window of TransType Pro.
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
dfontifier
This little utility [121] fulfills a role that TransType overlooked: converting a Macintosh
font suitcase to a dfont file and vice versa. We drag and drop fonts onto the window in
order to convert from one format to the other: it is simple, useful, and, moreover, free.

Tools for Font Conversion
FontFlasher, the “Kobayashi Maru” of Fonts
According to the company FontLab, the purpose of this software, which in fact is a plugin for FontLab, is to produce bitmap fonts that can be displayed under Macromedia Flash
without anti-aliasing. The intention is praiseworthy: it is true that bitmap fonts at small
sizes are more legible when they are displayed with simple black-and-white pixels rather
than with levels of gray.
But how can we control the display on a given machine? How can we be sure that antialiasing will not be performed? It is, a priori, impossible to be sure. The computer always
has the last word.
The reader must surely be wondering why we have called this software a “kobayashi
maru”. The story [128] has it that Captain James Kirk had to take a final test in a flight
simulator in order to obtain his diploma. On this test, the Enterprise received a call for
help from a vessel called Kobayashi Maru (the word “maru”, in fact, is used after ship
names in Japanese) in the Klingon territories. The captain was morally obliged to go to
the aid of the vessel. But the request was a trap. The Klingons attacked the Enterprise and
destroyed it. End of test. And an inevitable outcome, because refusing to assist a vessel
in distress would have been an equally bad solution.
That is why “kobayashi maru” has come to denote, in hacker jargon, a no-win situation.
What, then, did our Captain Kirk do? The night before the test, he broke into the computer room and modified the program. The Kobayashi Maru was not a trap any longer. In
a word, he cheated. But one has the right to cheat when a vessel and its crew are at risk.
What does that have to do with FontFlasher? Well, here we find ourselves in a kobayashi
maru: how on earth can we force the operating system not to anti-alias a font?
By cheating. If the operating system anti-aliases all fonts, let us give it a font that it will
not have to anti-alias. And the only font that it will not anti-alias is a font that already
has the precise shape of the pixels. If the pixels on the screen correspond with absolute
precision to the font’s vector contours, there will be nothing to anti-alias.
This is precisely what FontFlasher does. It generates a vector contour that is identical to
the pixels. At the given size, this contour yields a perfect “bitmap” font—which, at any
other size, is a catastrophe.
Given so many ways to obtain bitmap fonts once again, as in the good old days of Macintosh System 4.3, we may well ask the question:
The image above is a screenshot of text in 11-point Futura and in Futura processed by
FontFlasher. Here is what we get at high resolution:

What is more readible, this vector font with anti-aliasing
or this simulation  of bitmap font with pixels given by outlines?
(Note that we have not manually retouched the glyphs of the processed font; we have
shown the raw rendering.) And here, under FontLab, is the raw output of FontFlasher,
in which each pixel is a vector-drawn square; at right, the same glyph after retouching
and merger of the squares:
In the background, we can see the vector contour of the glyph in the original font.

Font Management
under Windows
Our concern in this chapter will be the installation and management of fonts under
Windows 2000 and XP. These procedures are similar in many ways to their Macintosh
counterparts, for several reasons: most of the most common software packages, be they
for office automation or artistic design, have been ported from one platform to the other
(from Windows to the Macintosh, in the case of office automation; from the Macintosh
to Windows, in the case of desktop publishing and the graphic arts). Why should the
same not apply to ancillary resources—in particular, fonts?
Figure 7-1: The Fonts directory in Windows XP.
Installing fonts under Windows is as easy as installing them under Mac OS: one need
only go into the Control Panel and open the shortcut to the Fonts directory, which,
