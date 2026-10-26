---
title: "Chapter 9: Fonts in TEX and Ω, their installation and use"
description: "Unabridged English text: TeX compilation pipeline, TFM metric files, DVI drivers, Virtual Fonts, Omega 16/32-bit architecture, and OTPs."
---

# Chapter 9: Fonts in TEX and Ω, their installation and use
**By Yannis Haralambous, Ph.D.**
*From Fonts & Encodings, pp. 235–314*

---

```text
Chapter 9 : Fonts in TEX and Ω, their installation and use
There is no shortage of word processors or desktop publishing software. How does TEX
differ from the pack, to the point of deserving two whole chapters in this book?
Well, TEX is an outsider among word-processing systems and desktop publishing software, as it existed before all the others (neither Mac OS nor Windows existed in 1978, and
Unix was still in its infancy) and, thanks to the idealism, perspicacity, and industriousness
of Knuth and the hundreds of programmers who have contributed to TEX over the past
25 years, TEX has invested much more than the others in fine typography.2 Thus it is
natural that font management in TEX is different from, and more sophisticated than, font
management for other software.
Moreover, as free software, TEX and Ω—its successor, as of 1994, developed by John Plaice
and the author—have unlimited potential: any features that one might need can be
added to them, provided that a programmer with the time and energy to do the work
can be found. Ω in particular is fertile ground for experimentation and application of
new techniques of digital typography to “explore strange new worlds, to seek out new
life and new civilizations, to boldly go where no one has gone before”...
This chapter is intended primarily for users of TEX or Ω who wish to understand font
management on these systems and improve the appearance of their documents by making as much use as possible of the fonts available to them. To those who do not yet know
TEX but wish to discover it, we recommend the following introductory section, in which
we shall also define a number of terms and acronyms that we shall use throughout the
chapter.
Introduction to TEX
When we prepare a document on a word processor such as Microsoft Word or desktop
publishing tools like Quark XPress, we sometimes have two conflicting requirements of
the software that we use. On the one hand, we expect the software to give us complete
control over layout, like an automobile that gives us complete control over the road;
after all, the software belongs to us and must “obey” us. On the other hand, we expect it
to “do its job”; that is, it should produce precise and perfect layout worthy of the great
typographers.
Why do these two requirements come into conflict? Because we cannot be very accurate
when we use a mouse to lay out the blocks of text that we see on the screen, since the
mouse, the screen, our hands, and our eyes are themselves not very accurate. And if we
take the trouble to be accurate by using magnifying glasses and sophisticated tools for
measurement, alignment, and uniformity, along with any other devices supplied by the
software, the effort required is completely out of proportion to the result obtained—a
the Greek letters tau, epsilon, chi, the first letters of the word τχνη, which means “art” and “technique” in
classical Greek. For this reason, the pronunciation of TEX depends on the pronunciation of classical Greek in
the language being used, which differs dramatically among speakers of English, French, German, Japanese,
and, yes, modern Greek. In English, TEX rhymes with “blecchhh”, as explained by Knuth in [217].
2 So much so that the software package considered the crème de la crème of mass-market typesetting
software, Adobe InDesign, adopted TEX’s techniques for setting paragraphs—techniques that Adobe advertises
as being revolutionary. . .
```

```text
Using Fonts in TEX
result that is nothing more than the most natural thing in the world: typography worthy
of the name.
To reach this conclusion, we shall begin with the assumption that the user of the software
at least knows what she must do to obtain a good typographic result, even if she cannot
produce one. But even this assumption is false, since, as we know, most users of wordprocessing software do not know much about the typographer’s trade. They could not
be expected to have knowledge obtained only through several years of specialized study
(at the École Estienne or the University of Reading, for example) or considerable time
and effort to learn them on one’s own. Let’s face it: a person who assumes the typographer’s role without having any background in typography will produce bad documents.
Indeed, our era will certainly be characterized by historians as the era of the decline of the
typographic art...
Which bring us to TEX. For the moment, let us forget about the intrusion of computer science into the process of book production and return to the traditional model of “author–
editor–printer”: the author writes a manuscript, the editor corrects and improves it, the
printer typesets it. Next, the printer prepares proofs and sends them to the editor, who
passes them along to the author, who reviews them and corrects them. And the process
starts all over again, and continues until the day when no more corrections are made and
the author and the editor give the long-awaited “pass for press”, and the printer can then
begin the print run. This age-old model distributes both the tasks and the responsibilities
among “author”, “editor”, and “printer”.
But, to return to the twenty-first century, how can one implement this model when he
is sitting alone in front of his computer? Well, he alternately plays the roles of “author”
and “editor”, and TEX assumes the role of “printer”.
That established, we can start with Step 1: we prepare a “manuscript” (see Figure 9-1),
i.e., a “TEX” file containing our document marked up with various tags for structure or
formatting. We call these tags “commands”, since, after all, a TEX document is a program.
In addition, there is a library of subroutines written in the TEX programming language:
it is called LATEX, and it offers a set of commands that are very practical and easy to use.
Step 2: the “manuscript” is sent to the “printer” (in computer jargon, the document is
compiled by TEX), and “first proofs” are produced. The author/editor examines these
“first proofs” and corrects his “manuscript”, then hands it offonce again to TEX, which
produces another set of proofs. The process is repeated until the production of the “pass
for press”, which leads directly to printing (in our case, the output of the printer or the
films from which printing plates will be made).
What is special about TEX is the physical separation between the TEX document (what
we have called the “manuscript”; in computer jargon, the “source”) and the typeset document (the “proofs”; in computer jargon, the “compiled file”). The latter, for historical
reasons, is a file with a format particular to TEX that is known as DVI (acronym of deviceindependent). This file format, compared with formats such as PDF, PostScript, and DOC
(the file format of MS Word), is an extremely simple and abstract page description.
```

::: tip Typographical Specimen Plate (Figure 9-1)
![Figure 9-1: The TeX production process](/images/fonts-encodings/fig9-1-tex-production-process.png)
*Figure 9-1: The TeX production process.*
:::

![Figure 9-1: The TeX production process](/images/fonts-encodings/fig9-1-tex-production-process.png)
*Figure 9-1: The TeX production process.*

Chapter 9 : Fonts in TEX and Ω, their installation and use Figure 9-1: The process of producing documents with TEX. Why are simplicity and abstraction so important? Because when TEX was created (in the 1970s), each screen and each printer had its own computer codes. Rather than making as many versions of TEX as there were models of screens and printers, Knuth decided to create a sort of “pivot” format, the DVI format. Users had only to write their own screen and printer “drivers” customized for their systems. The same goes for fonts. So as not to make life complicated, TEX uses stand-ins called TEX Font Metrics. Unlike all other fonts, these are empty, in the sense that they do not contain any glyphs. Instead, they contain font-metric data for each glyph: its height, its set-width, its depth, etc. Instead of setting glyphs themselves, TEX sets type using imaginary boxes whose dimensions are taken from the TFM files. Once again, the DVI drivers mentioned above have to “dirty their hands” and replace these imaginary boxes with glyphs. The logic is the same as for the DVI format: since each printer and each screen has its own font formats, we may as well use a simple, generic font format and convert it to the format used by the peripheral. Thus TEX would produce a document with an abstract, unreal beauty, and its obedient servants, the device drivers, would bring this masterpiece down to earth by replacing the imaginary boxes with genuine glyphs and working its magic to render the data comprehensible to all the various output devices. Since this situation was quite tedious, we awaited, as if for a messiah, the arrival of a universal language that would work on all screens and all printers. And it came in 1982: it is the PostScript programming language. From that time on, we would need only one driver—a driver to convert DVI files into PostScript code. Several attempts were made to write that driver—attempts that ran into

Using Fonts in TEX
major technical problems. Finally, Tom Rokicki, one of Knuth’s doctoral students, wrote
dvips, which is the most successful and the most widely used DVI-to-PostScript driver
today.
By now the reader will certainly understand why it is only dvips, not TEX itself, that comes
into contact with modern font technology: PostScript Type 1 or Type 3, TrueType, OpenType, etc. As can be seen in Figure 9-1, TEX uses TFM fonts to produce a DVI file. Then
dvips takes over and produces PostScript code, including, if necessary, PostScript Type 1
fonts.
But we are already starting to go behind the scenes of TEX. The average user never has
anything to do with TFM fonts and rarely deals with DVI files. Instead, she focuses on
the high-level programming interface: the basic LATEX commands, the various packages
of commands customized for different typesetting contexts, etc. Being above all an “author” and possibly also an “editor”, the LATEX user does not usually worry about the tasks
generally performed by the “printer”.
Below we shall examine the use of fonts under TEX on three levels:
• The “high level”: the point of view of the end user, who plays the role of “author”.
• The “intermediate level”: that of the more informed user, who desires better control
over the fonts in his document, or the “editor”, in the sense of the person who specifies in great detail how the document will appear—in particular, the fonts to be used.
• The “low level”: the internal workings of the software, where a certain number of basic questions shall occupy our attention: What is the relationship between TEX commands and TFM files? How are fonts used in the DVI format? When do PostScript
or other “real-world” fonts come into play? What is the relationship between these
fonts and TFM fonts?
In the list above, we discuss nothing but the use of fonts. With the exceptions of the fonts
that come with TEX or Ω and are already installed on the system, however, we must first
install any other fonts that we wish to use. And it goes without saying that all three levels
are involved, and with equal importance, in the installation of PostScript fonts under
TEX. That is what we shall see below.
One other item adds to the complexity of font management in TEX as we have described
it: METAFONT fonts. Even though PostScript did not yet exist in 1978, TEX did not come
into the world deprived of fonts. On the contrary, after developing TEX, Knuth said: It is
not good that TEX should be alone; I will make him a help meet for him and therefore created
a companion for it. This lawful companion of the TEX language is a programming lan-

```text
Chapter 9 : Fonts in TEX and Ω, their installation and use
The Computer Modern fonts, shown here, are among
the most commonly used fonts in the world and
are the most distinctive feature of the vast majority of LATEX documents.
They come in a rich variety, from roman to sans-serif, and typewriter type.
All of the glyphs in this sample come from the
same METAFONT code.
Just as DNA characterizes
a human being, 62 parameters are enough to characterize a font
in
the Computer Modern family.
Figure 9-2: A sample of various fonts of the Computer Modern family.
guage herself,3 but one dedicated to creating fonts. We shall discuss her in great depth in
Appendix F of this book.
Thus we have one more font format to take into consideration when we prepare to manage fonts in the TEX or Ω system: the fonts generated by METAFONT. And this font format
is quite important indeed, as many of the older installations of TEX have nothing by
default but METAFONT fonts.
Now that we have finished outlining these general and historical considerations, let us
move on to the realm of the concrete, beginning with the three levels of font management in TEX: high, intermediate, and low.
The High Level: Basic LATEX Commands and NFSS
In this section, we shall presume that the reader is somewhat familiar with LATEX. (If
not, there are excellent introductions to the subject, such as [282], [224], and [317].) The
question that we shall discuss first is how to use fonts in LATEX. More specifically, what
does one do to specify the active font?
One can very well prepare a LATEX document without specifying a single font; after all,
when one uses commands such as \emph{...} (emphasized text), \section{...} (a section title), \footnote{...} (the text of a footnote), LATEX itself chooses the appropriate
font for each case. Which fonts are these? We might be inclined to say a priori that
the default fonts for LATEX are always the same: those of the Computer Modern family
3 The decision to feminize METAFONT is not the author’s personal initiative. TEX, in the illustrations that
accompany it, is represented by a lion.5 In the same illustrations, METAFONT is personified as a lioness. And
this leonine couple is traditionally accompanied not by a humdrum lion cub but by a new species of animal:
the computer, which not only has hands and feet but even drinks coffee. . .
4 Not for nothing is TEX represented by a lion. Donald Knuth has told us that lions are to him the
guardians of libraries in the United States because there is a statue of a lion in front of the entrance of each
large library there. Guardian of libraries, guardian of the Book—is that not indeed what TEX ultimately aspires
to be?
```

Using Fonts in TEX (see Figure 9-2), designed by Knuth on the model of Monotype Modern 8A [219]. But in fact everything depends on the LATEX stylesheet that we are using. A stylesheet is a LATEX file that specifies the details of the document’s appearance. These specifications can be more or less general: LATEX comes with some generic stylesheets of its own, and there are stylesheets on the Web for all the scientific journals, collections of works, dissertations at each university, and many other purposes. The text font, the font for mathematical formulae, the font for computer code, etc., are part of each stylesheet’s specifications. To specify the active font, the user can operate at any of a number of levels, according to the nature of the choice and his own technical expertise. Let us begin with the simplest case and proceed deeper and deeper into the workings of LATEX. Choosing fonts in LATEX: basic commands Owing to its origins in the computer, LATEX considers that there are three big categories of fonts that can coexist in a document: “serif”, “sans serif”, and “typewriter”, the last of these being used to set computer code. The following three commands set the text provided in the argument in one of these three types of fonts: \textrm{...} serif \textsf{...} sans serif \texttt{...} typewriter In the absence of any other indication, text is set by default in a light upright font that has a lower case. We can change the weight (one other possibility) and the style: \textbf{...} bold \textit{...} italic \textsl{...} slanted \textsc{...} small capitals where “slanted” is an invention of Knuth that involves artificially slanting the letters. It is tolerable for sans serif fonts, but it quickly becomes annoying in serif fonts, so please avoid it! In the list above, bold can be combined with the three styles “italic”, “slanted”, and “small capitals”, but those three styles cannot be combined with one another (a regrettable fact, since it leaves us with no way to obtain italic small capitals). To return to the normal state (light, upright, with a lower case), we have the following commands: \textmd{...} light (in fact medium) \textup{...} upright, with a lower case \textnormal{...} light and upright, with a lower case The second command cancels the effect of italics, slanted type, and small capitals. The third is the most powerful: it restores the default font of the document, with no ornamentation.

```text
Chapter 9 : Fonts in TEX and Ω, their installation and use
All of the commands described above affect the text that is given to them as an argument.
As a safety measure, this text cannot be very long; more specifically, it cannot contain
more than one paragraph. (Recall that the change of paragraphs in TEX is made with a
blank line.) To apply these same changes to a larger block of text, we must place that
block in a group (that is, within braces) and place inside that group one of the following
commands:
\rmfamily
serif
\sffamily
sans serif
\ttfamily
typewriter
\bfseries
bold
\itshape
italic
\slshape
slanted
\scshape
small capitals
\mdseries
medium weight and set-width
\upshape
upright
\normalfont
light and upright
But beware! \textit{...} is a better choice than {\itshape ...}, as the former also applies the italic correction, which is a slight space that is added after letters with an ascender
to keep them from touching the following glyph if it is, for example, a right closing parenthesis. Thus (\textit{need}) will yield “(need)”, while ({\itshape need}) will yield the
unfortunate “(need)”.
A number of commands for changing the current type size are also available. These
commands are of the same kind as the previous ones; i.e., they apply to everything that
follows, and their effect should be limited through the use of grouping:
\tiny
tiny
\scriptsize
the size of superscripts and subscripts
\footnotesize
the size of footnotes
\small
small
\normalsize
the usual size of running text
\large
slightly bigger
\Large
bigger
\LARGE
much bigger
\huge
barely tolerable
\Huge
enormous
The exact sizes depend on the stylesheet. For example, in the case of the most common
stylesheet (book class, 10 points), they are 5/6, 7/8, 8/9.5, 9/11, 10/12, 12/14, 14/18, 17/22,
20/25, 25/30 (in American printer’s points).
```

Using Fonts in TEX
We must mention here that the system covers most of the cases that the author of a LATEX
document is likely to need, but at the same time it may not always satisfy those of us
who place a little more importance on the font used in our document. For example, one
cannot choose the font’s family; nor can one specify the body size exactly or the desired
leading. No provision is made for font families that offer a broader range of weights or
styles. Last but not least, the system is profoundly Latin-centric, as serifs, italics, and small
capitals do not even exist in most of the world’s scripts.
To achieve what we desire, let us descend to another level in the LATEX machinery.
Using NFSS
In this section we shall dissect LATEX’s system for choosing fonts. This system is called the
“New Font Selection Scheme” (NFSS). [272] (Here the word “new” seems a bit out of
place today because NFSS was introduced in 1992.) The principle is very simple. Each
font is described by five independent parameters. The user requests the font by specifying the values of these parameters, and, if the system cannot supply the desired font, it
supplies an approximation based on a substitution mechanism.
These five parameters are:
• \fontfamily{...}: the name of the font’s family. This is not the true name of the
font family, in the manner of PostScript or TrueType, but rather a keyword specific
to NFSS, made up of lowercase letters and digits. For example, this keyword might
be “timesten” for Adobe Times Ten. This keyword appears in the name of the FD
(“font descriptor”) file that describes the correspondence between “logical” fonts (at
the level of NFSS) and “physical” fonts (the TFM files). Thus for a keyword timesten
there must exist on the disk a file named t1timesten.fd (or ot1timesten.fd,
t2atimesten.fd, etc.; everything depends on the encoding, as we shall see below).
How can we know which fonts are available on our system? Or, when we know that
we have a certain FD file, how can we tell which font family matches it? No simple
means are available at this time; one must prepare a list of all the FD files on the
system and try to guess the name of the font family from the filename.5 But this
5 It is quite likely that the file t1timesten.fd corresponds to the font family Adobe Times Ten; but would
t1garamond.fd go with Monotype Garamond, Adobe Garamond, or (a hideous font, in the opinion of many typographers) ITC Garamond? Let us get a bit ahead of ourselves and say right now that the only way to know is to
find, inside the FD file, the names of the TFM files that are used. If they are virtual font-metric files, one must
open them (see §B.3) and find the underlying real fonts. Finally, one must go into the configuration file(s) for
dvips and find out to which PostScript fonts they correspond. These configuration files will necessarily contain
the desired information.
Is there a way to avoid having to play “font detective”? Karl Berry [75] has finished his Font Naming Scheme,
which provides a two-letter or three-letter abbreviation for each font family.
Unfortunately, there is no shortage of drawbacks. First of all, these abbrevations neither reveal their meaning nor have much mnemonic value. While ptm, phv, pcr for Adobe Times, Adobe Helvetica, Adobe Courier do
retain a certain logic, how can one remember that ma1 is Monotype Arial and that mii is Monotype Imprint, the
favorite font of Oxford University Press? Furthermore, Berry’s list will most likely never be complete: there are
hundreds of large and small foundries throughout the world, which means that new fonts come out every day;
thus there will always be some that are not on the list. Conversely, is it necessary to change the abbreviation

Chapter 9 : Fonts in TEX and Ω, their installation and use
problem may occur less often if we install our fonts ourselves and thus choose the
NFSS keyword that represents the font family.
• \fontseries{...}: the weight and the set-width. The system used by NFSS to describe these characteristics is as follows:
ul
ultra-light
uc
ultra-condensed
el
extra-light
ec
extra-condensed
l
light
c
condensed
sl
semi-light
sc
semi-condensed
m
regular weight
m
regular width
sb
semi-bold
sx
semi-extended
b
bold
x
extended
eb
extra-bold
ex
extra-extended
ul
ultra-bold
ux
ultra-extended
Here are the rules: (a) the two expressions are combined in the order specified
(weight, then set-width); (b) the letter m is omitted when either the width or the
weight is regular; (c) m is written when both the width and the weight are regular.
Thus we write elc for an extra-light condensed font but simply el for an extra-light
font of regular width and m for a font of regular width and regular weight.
• \fontshape{...}: the “style”. This category includes italics, slanted type, small capitals, and a few other exotic styles:
n
upright
it
italic
ui
upright italic
sl
slanted
sc
small capitals
ol
outline
“Upright italic” is another of Knuth’s inventions. It involves applying a negative slant to
italic letters so that they appear vertical. The result is quite disconcerting.
Note that there is, unfortunately, no way to combine several styles. For example,
in NFSS we cannot specify italic small capitals, which could be very useful—as, for
example, when an acronym occurs inside a quotation: “Some people confuse Ionesco
and unesco”.
if a foundry releases a new version of a font? And what should a user do who has modified a font herself by
changing a glyph or reencoding the font?
In any event, no better means of identifying fonts has been discovered up to now. The solution to the problem
may come from the migration of OpenType fonts that is being carried out by the Ω system and that will open
new horizons for font management.

Using Fonts in TEX
Figure 9-3: The OT1 glyph encoding (TEX’s default encoding). Accented letters are built up from
letters and accents.
• \fontencoding{...}: the encoding used by the font.
Since the introduction of NFSS, many TEX-specific encodings have emerged. The
most important of these are:
– OT1, Knuth’s original encoding; see Figure 9-3 [217, p. 427]
– T1, an encoding inspired by ISO Latin-1 that also incorporates glyphs for the languages of Central Europe and the Baltic countries; see Figure 9-4 [211]
– TS1, the catchall companion to T1; see Figure 9-4 [211]
– T2A, T2B, and T2C, a trio of encodings for European and Asian languages that use
the Cyrillic alphabet; and T2D, a font encoding for Old Cyrillic; see Figure 9-5 and
Figure 9-6 [73]
– T3, an encoding for the glyphs of the International Phonetic Alphabet; see Figure 9-7 [302]
– T4, an encoding for Maltese and the African languages that use the Latin script;
see Figure 9-7 [211]
The name of the encoding also appears in the name of the FD file; thus, if there is
a file t1palatino.fd on our system and the system has been configured correctly,
we should be able to use the Palatino font family, in the T1 encoding, in our LATEX
documents.
Note that the encoding, unlike the weight and the style, is not taken into account by
the substitution mechanism. In other words, a font in a given encoding that is not
available will never be replaced by the same font in a different encoding.
• \fontsize{...}{...}: the body size and leading. When we write \fontsize{10pt}{
12pt}, we specify a font of body size 10 set on 12 points (American printer’s points)
of leading. Some other units are also available: Didot points, dd (still in use in some
European countries, such as Greece); PostScript points, bp (‘b’ for big, since they are

Chapter 9 : Fonts in TEX and Ω, their installation and use Figure 9-4: Glyph encodings: T1, or the “Cork encoding”, named for the city of Cork, Ireland, where it was defined in 1990 (for the European languages that use the Latin script), and its “catchall” companion, named TS1 [211].

Using Fonts in TEX Figure 9-5: The T2A and T2B glyph encodings (for European and Asian languages that use the Cyrillic alphabet) [73].

Chapter 9 : Fonts in TEX and Ω, their installation and use Figure 9-6: The T2C (Asian languages that use the Cyrillic script) and T2D (Old Cyrillic) glyph encodings.

```text
Using Fonts in TEX
slightly larger than American printer’s points); millimeters, mm; etc. Note that leading, like the encoding, is ignored by the substitution mechanism.
One small detail of some importance: in TEX, a change of leading has effect only if there is at
least one change of paragraph within the group. Thus—and it is a very common error among
beginners—in the example below, the text will be set in 9-point type, but the change of leading
to 10 points will not take effect:
{\fontsize{9pt}{10pt}\selectfont This is the section of the contract
that is printed in small type so that you will not read it. It commits
you to donating your soul in due form to the undersigned Mephistopheles,
immediately after your physical death.}
To obtain the desired effect, adding a blank line before the closing brace would suffice:
...
you to donating your soul in due form to the undersigned Mephistopheles,
immediately after your physical death.
}
A few examples of the use of NFSS commands. To obtainFive words in Centaur italic...:
\fontfamily{centaur}\fontsize{11}{13}\fontshape{it}\selectfont
Five words in Centaur italic...
To obtain italics, bold italics, bold italics in Univers...:
\fontshape{it}\selectfont italics,
\fontseries{bx}\selectfont bold italics,
\fontfamily{unive}\selectfont bold italics in Univers...
Finally, to obtain 11/13 type in American printer’s points, in PostScript points, in
Didot points:
\fontsize{11}{13}\selectfont 11/13 type in American printer's points,
\fontsize{11bp}{13bp}\selectfont in PostScript points,
\fontsize{11dd}{13dd}\selectfont in Didot points.
The example above shows the tiny but nonetheless perceptible differences among the
three kinds of typographic points: American printer’s points, PostScript points, and Didot points.
As we can see from the first example above, in order to avoid triggering the substitution
process too soon, the commands \fontfamily, \fontseries, \fontshape, \fontencoding, and \fontsize have no effect until the command \selectfont is issued. It is interesting to note that NFSS always attempts to combine the active font with the new
properties that the user specifies. For example, \fontseries{bx}\selectfont will yield
extended bold in an upright context and extended bold italic in an italic context; the
family, the body size, the leading, and the encoding of the font remain unchanged in
both cases.
```

Chapter 9 : Fonts in TEX and Ω, their installation and use Figure 9-7: The T3 (IPA) [302] and T4 glyph encodings (for African languages that use the Latin script) [211].

Using Fonts in TEX
Configuring NFSS
But how does NFSS know which font to use in order to match the choices made by the
user? And what happens if the user’s wishes cannot be fulfilled? The system’s magic is all
found in its configuration.
Here it is, in broad strokes: to each font family (“family” in the NFSS sense, described
above) and each font encoding (of the encodings used with NFSS: T1, OT1, T2, etc.), there
corresponds a font description file. The file name reflects these two kinds of data—the
encoding and the family. Its extension is .fd (= font descriptor). For example, the file for
the Palatino family and the T1 encoding will be named t1palatino.fd.
Within each file, there are two new LATEX macros: \DeclareFontFamily and \DeclareFontShape. Although only two macros are provided, one can do a great deal with them.
In fact, the designers of NFSS developed an entire font-configuration syntax, which is
what we shall examine in the remainder of this section.
First of all, let us present the problem. We have a set of constraints (typesetting specifications: roman or italic, light or bold, lowercase or small capitals, body size) and a set
of possible solutions (“physical” fonts, which is to say the TFM files that are found on
our system). On the one hand, there is order: the rational, logical classification of font
properties and the clear and precise expression of the user’s wishes. On the other hand,
there is chaos: files with names that are often incomprehensible, containing fonts with
properties that often cannot be obtained other than by visual inspection of the glyphs.
The method adopted is as follows:
• As we have already mentioned, the encoding and the font family (again, in the NFSS
sense) are parts of the filename and thus remain unchanged in the file.
• There is only one \DeclareFontFamily command in the file, and it includes the information stated in the previous item (the encoding and the font family).
• There are multiple \DeclareFontShape commands, each of them corresponding to
a combination of weight and style.
• A special syntax is used in an argument to the \DeclareFontShape command to specify the fifth and last NFSS parameter, the body size.
Note that leading does not appear anywhere in this configuration; it is considered a
global property of the document, independent of the active font. Also note that there is a
fundamental difference between body size and the other NFSS parameters: the encoding,
the family, the style, and the weight take well-determined and unique values from a set
of predefined ones. The body size follows a different logic. On the one hand, it employs
numbers with a decimal part and, therefore, there may be very many possible values,
according to the precision desired. On the other hand, we often think not in terms of
specific sizes but rather in terms of intervals; for example, we may use one “physical”
font for sizes between 9 (inclusive) and 10 (noninclusive), another font for the interval

```text
Chapter 9 : Fonts in TEX and Ω, their installation and use
between 10 (inclusive) and 11.754 (noninclusive), and so on. It is clear that the description of constraints on body size calls for a syntax more complex than the simple list of
keywords that is used for the other NFSS parameters.
Along with that problem comes another question, an almost metaphysical one. Namely,
“What is meant by the size of a font?” In the era of lead type, this question had a simple
answer: the “size” was the height of the leaden type sort. Thus, when rows of characters
were placed one above another, the result was copy set with a distance between baselines
that was equal to the body size. (Typographers often spoke of this procedure as setting
type “solid”, in the sense that nothing was placed between the lines of type.) For a 10/12
setting, one used 10-point type and added a strip of lead 2 points thick between the rows
of characters.
The transition of typography from the material realm to the computer entailed the loss
of physical items that could serve as points of reference for a new definition of “size”.
In the heyday of bitmap fonts, one last point of reference remained: glyphs had a given
size, measured not in points but in pixels. The advent of vector fonts wiped out this last
point of reference. A vector font can be used at any size, from the microscopic sizes used
on electronic components to the often inordinate sizes used in signage. What does body
size mean for a font that is so “micromegalous”?
Well, there are two ways to define it, each of them useful—but it is important to keep
them separate. There is the actual size, a furtive, localized value that depends the graphics
software or word processor. For instance, if we set type in “10-point Optima”, the shapes of
the glyphs in the Optima font do not depend on the actual size. We can change the size
but not the shapes themselves. When Hermann Zapf designed this font [228, p. 329],
in 1958, he had no specific size in mind; as a result, Optima is the same at all sizes, all
actual sizes.
There is also the optical size. It is a parameter that the designer specifies for her font.
Take the example of “Linotype Times Ten”. As its name suggests, it was designed for use
at 10 points; thus its optical size is 10. In other words, it will yield the best results at an
actual size of 10. That is not to say that we are not allowed to use it at other actual sizes.
But it will give the best results at 10 points.
For more information on the differences between actual size and body size, we refer the
reader to page 12. The reason that we have raised this issue again here is that this duality
of concepts is responsible for the complexity of the syntax of NFSS.
It is time for some concrete illustrations. Here is an extract of code from a .fd file:
\DeclareFontFamily{T1}{palatino}{}
\DeclareFontShape{T1}{palatino}{m}{n}{<-> palatino}{}
\DeclareFontShape{T1}{palatino}{m}{it}{<-> palatinoi}{}
\DeclareFontShape{T1}{palatino}{bx}{n}{<-> palatinob}{}
\DeclareFontShape{T1}{palatino}{bx}{it}{<-> palatinobi}{}
The first command states that in this file we are describing the family Palatino in
the T1 font encoding. It follows that this code necessarily appears in a file named
```

```text
Using Fonts in TEX
t1palatino.fd. The four commands that follow specify that there are four combinations
of weight (m for medium, bx for bold extended) and style (n for neutral, it for italic).
The fifth argument to each of these commands shows the correspondence between the
actual size and a TFM file (whose name is given without the extension .tfm).
Here we have a simple case: there is only one design for the Palatino font; therefore, we
consider this design to be optimal at all sizes. The symbol <-> indicates that the TFM
font that follows is to be used at “all actual sizes”.
More precisely, the syntax is as follows: we write &lt;m-n&gt;, where m and n are rational numbers, to indicate “all sizes from m (inclusive) to n (non-inclusive)”. Omitting one or both
of this numbers indicates that there is no limit; for example, <-8> means “used for all
sizes strictly lower than 8”, and <12.5-> means “used for all sizes greater than or equal
to 12 1
2 points”.
Let us take an example. The excellent font ITC Bodoni [323] is sold at three optical sizes:
6, 12, and 72. Assuming that the TFM files for light upright type in these three versions
are named itcbodoni6.tfm, itcbodoni12.tfm, and itcbodoni72.tfm, we can imagine a
font descriptor containing the following code:
\DeclareFontFamily{T1}{itcbodoni}{}
\DeclareFontShape{T1}{itcbodoni}{m}{n}{
<-> itcbodoni6
<9-> itcbodoni12
<18-> itcbodoni72
}{}
That means: font “6” when setting type smaller than 9 points, font “12” when setting
type between 9 and 18 points, and font “72” when setting type larger than 18 points.6
Thus, when we call for ITC Bodoni at an actual size of 10 points, LATEX will set it at the
optical size of 12, reduced by 16.67 percent. At an actual size of 9, the optical size of 12
will still be used, but this time the type will be reduced by 25 percent. At an actual size
of 8.5, we will use the optical size of 6 magnified 41.67 percent. And if we request an
actual size of 12, we will have a perfect result, since the actual size and the optical size
will be identical!
Now suppose that we have a font on hand that has the different optical sizes of 6,7,8,9,
... ,24 points. Few fonts have so many optical sizes designed by hand; but these optical
sizes can also result from a “mechanical” interpolation made from a Multiple Master
font (see §C.4). We have an example in Figure 9-8: the Adobe font Kepler MM, which we
have instantiated 20 times to obtain the optical sizes between 5 and 24 points, one point
apart. Suppose that the corresponding TFM files are named kepler5, ... , kepler24. Then
we can imagine an FD file like the preceding one, with intervals for the actual sizes:
6 Obviously these choices are arbitrary, but it must be admitted that 6-point or 72-point text seldom
appears in a document; thus, if we took the font names literally, fonts “6” and “72” would practically never
be used. We have “cheated” slightly in order to improve these three fonts’ chances of being used together in a
document.
```

Chapter 9 : Fonts in TEX and Ω, their installation and use Figure 9-8: Some specimens of the font Adobe Kepler MM at optical sizes between 5 and 24 points.

Using Fonts in TEX \DeclareFontFamily{T1}{kepler}{} \DeclareFontShape{T1}{kepler}{m}{n}{ <-.5> kepler5 <5.5-.5> kepler6 <6.5-.5> kepler7 ... <22.5-.5> kepler23 <23.5-> kepler24 }{} That means that any difference, however small, between two actual sizes of these fonts will always be valid (requesting 5 points or 5.1 points gives two different fonts, the second one a tenth of a point larger) and that the difference between optical sizes and actual sizes will never be greater than 1 point. All very well. But is this attitude really sound? If we are already fortunate enough to have different optical sizes spaced one point apart (a luxury indeed), do we really need to indulge in the perverse, unhealthy pleasures of half-points or even tenths or hundredths of a point? Would it not be more elegant to use the pristine optical sizes themselves, as their designer intended, at their true dimensions? That can be done. Simply specify exact actual sizes: \DeclareFontFamily{T1}{kepler}{} \DeclareFontShape{T1}{kepler}{m}{n}{ <5> kepler5 <6> kepler6 <7> kepler7 ... <23> kepler23 <24> <25> <26> <27> <28> <29> <30> kepler24 }{} With the configuration shown above, NFSS will only set type at actual sizes that are whole numbers between 5 and 30. If these sizes are less than or equal to 24, the optical size will coincide with the actual size. Beyond that level, the optical size of 24 will be magnified, but only so as to form the integer-valued actual sizes of 25,26,... ,30. If LATEX—for whatever reason, be it an explicit request from the user or the calculations made by the stylesheet—calls for an actual size other than those explicitly indicated, the nearest size on the list will be substituted. Thus whether one calls for 9.33, 9.25, or 9.17, the result will be the same: the size of 9 points. To simplify the task of writing a font descriptor, LATEX provides the keyword gen *: \DeclareFontFamily{T1}{kepler}{} \DeclareFontShape{T1}{kepler}{m}{n}{ <5> <6> <7> <8> <9> <10> <11> <12> <13> <14>

```text
Chapter 9 : Fonts in TEX and Ω, their installation and use
<15> <16> <17> <18> <19> <20> <21> <22> <23>
<24> gen * kepler
<25> <26> <27> <28> <29> <30> kepler24
}{}
In this case, NFSS will generate the name of the TFM font by concatenating the actual
size (taken from the list) onto the string that follows gen *, which is kepler.7
Now let us discuss the other parameters in the FD file: style and weight (which, as we
saw above, is in fact the combination of weight and set-width). What happens when a
combination of the values of these parameters is unavailable? NFSS allows us to plan
for such cases by making substitutions. For example, the keyword sub * enables us to
redirect the request for a font to another combination of values of parameters, which
can in turn be redirected, and so on.
Thus, in the following example, we ask NFSS to redirect all requests for “slanted” fonts
to the italic font:8
\DeclareFontFamily{T1}{mtgara}{}
\DeclareFontShape{T1}{mtgara}{m}{n}{ <-> mtgaramond }{}
\DeclareFontShape{T1}{mtgara}{m}{it}{ <-> mtgaramondit }{}
\DeclareFontShape{T1}{mtgara}{m}{sl}{ <-> sub * mtgara/m/it }{}
Warning: what follows the keyword sub * must be an “NFSS specification”, i.e., a triplet
of “NFSS family name”, “weight”, and “style”, separated by slashes. Also note that that
allows us to invoke a font belonging to a different font family (which will therefore be
described in another FD file), provided that the font encoding remains the same.
Now let us examine another very interesting feature of NFSS: explicit scaling. Suppose
that in a single document we wish to combine two fonts whose letters are of noticeably
different sizes at the same actual size. We must therefore make their sizes consistent. To
that end, we need only specify the desired magnification or shrinking factor in brackets
just before the name of the TFM font:
\DeclareFontShape{T1}{laurel}{m}{n}{ <-> [1.2] hardy }{}
In this example, the font hardy will be magnified 20 percent to scale it up to the size of
laurel.
7 We can also use this feature with intervals of sizes, by writing, for example, <5-24> gen * kepler; but in
that case we really have to cross our fingers in the hope that LATEX will never call for nonintegral sizes, for then it
might generate the name of a file that does not exist. Thus if for any reason LATEX asks NFSS for an actual size of
9 1
4 points, NFSS will try to use the TFM font kepler9.25 and will fail if that font is not available on our system
(unless there is an external mechanism for automatically generating fonts, as in the case of METAFONT fonts—
something possible in theory for Multiple Master fonts, but no one has taken the trouble of implementing it).
8 Of course, and as we shall see below, we can always slant a PostScript font by including a little PostScript
command in the configuration file for dvips. But is that aesthetically acceptable? It might work for sans serif
fonts in some instances, but for serif fonts—especially those based on classical models, such as Monotype Garamond in the example shown above—that borders on sacrilege!
```

```text
Using Fonts in TEX
But beware! As is the case for most “miracle solutions”, there is a catch. A font contains
different types of glyphs, and when we attempt to regularize the sizes of some glyphs, we
may make things worse for others. Often the ratio of the height of the lowercase letters
to the point size is not the same for two fonts. In the past [142, p. 7], we spoke of “regular
x-height”, “large x-height”, or “small x-height”. Today the “x-height” refers to the ratio of
the height of the lowercase letters to the point size.9 When we calibrate the heights of
the lowercase letters in two fonts, we produce uppercase letters of noticeably different
heights—a very unpleasant effect. And there are still other elements in a font that must
be regularized: the parentheses, the heights of the hyphen and the dashes, the height
of the apostrophe, etc. If we wish to regularize two fonts correctly, we should take them
apart and handle separately the different types of glyphs found within them.
A less risky, and in fact more common, case of regularizing the heights of glyphs is that
of combining different scripts. Thus when we combine the Latin and Arabic scripts, or
Japanese and Hindi, we must take care to use suitable relative sizes.
We have seen the most important features of NFSS. Now let us enter the gray zone where we
describe the rare, more technical, and, finally, more dubious cases. The reader will certainly have
wondered what the purpose is of the last argument to the \DeclareFontFamily and \DeclareFontShape commands, which has consistently been empty in all our examples. This argument
contains TEX macros or primitives that will be executed when we load a TFM font. Since loading is
performed only once, the first time the font is used in the document, the selection of commands
that can be executed is rather limited.
You are free to experiment with this argument, but please be aware that we have reached the limits
of TEX here and that it behooves us to restrict ourselves to the few commands recommended by
the developers of LATEX, with the appropriate warnings. What are these commands?
The most useful of them is \hyphenchar. This command, which is in fact a TEX primitive, changes
the value of the glyph used as the end-of-line hyphen. The command
\DeclareFontFamily{T1}{bizarre}{\hyphenchar\font=127}
specifies that glyph 127 will henceforth be used as the end-of-line hyphen instead of the regular
hyphen, whose glyph ordinarily appears in code point 45 (which corresponds to the Unicode character 0x002D hyphen-minus). But does the end-of-line hyphen have a different shape from that of
the regular hyphen? Not at all: the two glyphs are identical. The reasons for making this substitution are obscure and technical. There is a rule in TEX that says that a word cannot be further
divided if it already has a potential breakpoint. This rule is useful: if you write thera\-pist, it is
precisely to avoid hyphenation after “the”; thus it makes sense that the presence of \- in a word
gives you complete control over the word’s division and that TEX cannot break the word elsewhere.
The weakness of TEX is that division is handled at the glyph level. Consequently, when one writes
“so-so”, if the glyph for the hyphen used in this word is the same as that used for word division,
TEX regards the word as already containing a potential word break and refuses to divide it further.
That may seem harmless enough for “so-so”, but it becomes downright annoying for words as long
as “Marxism-Leninism” or “physico-mathematical”. By using another glyph for the end-of-line hyphen, we can deceive TEX, which will no longer see any reason not to divide words containing a
hyphen.
9 Some people define x-height as the ration of the height of the lowercase letters to the height of the
uppercase letters [34, 206]. We shall employ the first definition.
```

Chapter 9 : Fonts in TEX and Ω, their installation and use
Another possibility: by writing \hyphenchar=-1, we can completely disable hyphenation. That
may be useful when we write computer code or when we write in a language that does not have
the concept of word division, such as Arabic, for example. But—and there is always a “but”—when
writing computer code, which will be set in typewriter type, we may wish to have better control
over the situation, since the “typewriter” font could also be used for commercial correspondence.
In the latter case, of course, we would want the words to be hyphenated. Thus inhibiting hyphenation must be done not at the level of the font’s configuration but at the level of the LATEX commands used in the document. In those languages that do not employ hyphenation, it is inhibited
in the linguistic configuration (for example, we obtain the same result by writing \language=99)
and is independent of the font being used.
Finally, for those with a flair for surgical procedures, we can use the last argument of the \DeclareFontFamily and \DeclareFontShape commands to modify some of the font’s internal parameters.
By writing \fontdimen5\font=2pt, we designate that parameter number 5 of the font (or of all the
fonts in the family) assume the value of 2 points. We can have up to 50 global parameters in an
ordinary TEX font, but in most cases we use only the first seven. Here is what they represent:
• \fontdimen1 specifies the slant, expressed by the tangent of the angle; in other words, the
horizontal displacement at a height of 1 point. This value is used when TEX places accents
over letters, so that the accents will be centered over the letters’ axes—axes that, in this case,
are oblique.
• \fontdimen2 specifies the ideal interword space, i.e., the interword space used in the font in
question when justification does not impose any constraints.
• \fontdimen3 specifies the maximum stretch allowed for the interword space.
• \fontdimen4 specifies the maximum shrink allowed for the interword space.
• \fontdimen5 specifies the height of the short letters (lowercase letters with no ascenders or
descenders). This information is used by TEX to place accents on letters. Suppose, for example, that the \fontdimen5 of a font is x and that we wish to place an accent over a letter of
height x′ > x. We shall thus have to move the accent upward by x′ −x. We have direct and
elegant access to this parameter through the unit of measure ex.
• \fontdimen6 specifies the size of the font’s em. We have access to it through the unit em.
• \fontdimen7 applies primarily to the English and German typographic traditions. In these
traditions, it consists of increasing the space that follows a sentence-final punctuation mark.
When more space is left after the final punctuation mark, the reader’s eye can more easily see
where each sentence begins and can more easily distinguish periods used in abbreviations,
which are not followed by extra whitespace. Since this practice is not observed in France, TEX
uses the name \frenchspacing for the command that disables it.
Thus by writing \fontdimen2=2.5pt, we set the font’s “natural” interword space to 2.5 points. Note
that we can also use \fontdimen on the right-hand side of an expression. For example, by writing
\DeclareFontShape{T1}{timesten}{m}{n}{ <-> timesten }{
\fontdimen2\font=.8\fontdimen2\font
\fontdimen3\font=.8\fontdimen3\font
\fontdimen4\font=.8\fontdimen4\font
}

Using Fonts in TEX
we will set our type in Times Ten 20 percent more tightly than usual with regard to the regular
interword space and to the stretching and shrinking thereof.
Once again, we advise the reader who is thinking of modifying these parameters, which are of vital
importance to the font, to do so within the font itself (see §B.1) or by creating a virtual font (see
§B.3). Here is an example of the trap that awaits sorcerers’ apprentices: TEX loads a TFM font only
once. If you write
\DeclareFontShape{T1}{timesten}{m}{n}{ <-> timesten }{}
\DeclareFontShape{T1}{timesten}{c}{n}{ <-> timesten }{
\fontdimen2\font=.8\fontdimen2\font
\fontdimen3\font=.8\fontdimen3\font
\fontdimen4\font=.8\fontdimen4\font
}
and then try to use the “weight/set-width” settings m and c defined above in a single document, the
c one will come out exactly as the m one—for the simple reason that the underlying TFM font is
the same, and thus TEX loads it only once. The values of the parameters can be modified only at the
very moment when the font is loaded; it is not possible to change them afterwards.
It is time to leave this gray zone and continue our tour of the use of fonts in TEX by
descending one level lower than LATEX and NFSS—to the level of the \font primitive,
which is responsible for loading TFM fonts in TEX.
The Low Level: TEX and DVI
The primitives for selecting fonts
By now we have already spoken of the TFM files many times. Here is the font-metric
information contained in a TFM file:
• Each glyph’s width.
• Each glyph’s height.
• Each glyph’s depth, which is the vertical dimension of the part located below the
glyph’s baseline.
• Each glyph’s italic correction, which is the amount of space to add when the glyph is
followed, for example, by a right closing parenthesis. This correction actually applies
only to certain italic letters with ascenders, such as ‘f’: for ‘f )’ looks better than ‘f)’, and
the latter would inevitably result in the absence of the correction because the glyphs
are set in two different fonts and therefore no automatic kerning can be performed
to move them apart.
• A certain amount of global information, including the \fontdimen settings that we
saw in the previous section.
• The kerning pairs.

Chapter 9 : Fonts in TEX and Ω, their installation and use
• The automatic ligatures, such as ‘fi’, ‘fl’, etc.
Note that these data, including the “width”, the “height”, the “depth”, and the “italic
correction”, are not connected in any way to actual glyphs (i.e., images of characters,
made up of contours or pixels). The object that TEX manipulates is merely a box whose
sides have the stated dimensions. The actual image of the character, which is unavailable
to TEX but will be placed within this box when the DVI file is converted to PostScript
(or another format), may lie within this box, extend beyond it, or even be outside it
altogether. In reality, all of these cases occur: glyphs neatly contained within their boxes,
glyphs whose boxes are reduced to a single point (the point of origin of the glyphs), boxes
with nonzero dimensions that nonetheless do not contain a glyph, boxes reduced to a
point that contain no glyph...
The NFSS specification
\DeclareFontShape{T1}{timesten}{m}{n}{ <-> timesten }{}
assumes the existence of a TFM file named timesten.tfm somewhere on the disk where
TEX can find it.10 In the case of METAFONT fonts, when the TFM file with the specified
name is missing, TEX is capable of launching METAFONT to generate the font and, in the
same stroke, the missing TFM file.
The TEX primitive that loads a TFM file is \font. It can be used in three different ways:
\font\myfontA=timesten
\font\myfontB=timesten at 12pt
\font\myfontC=timesten scaled 1200
To understand the differences among these three approaches, we need some extra information. In every TFM file, the optical size of the font is specified. In the first line of our
example, we are using the font at an actual size equal to the optical size. Thus, if the font
was designed to be used at an actual size of 10 points (as the name Times Ten suggests),
TEX will use it at that size. All that we have to do is write
{\myfontA Hello}
so that this font will be used at its default size, which corresponds to the the optical size.
In the second line, we have explicitly requested a specific actual size. TEX will divide the
requested actual size by the optical size and will use their quotient as a stretching or
shrinking factor.
In the third line, we have expliticly specified a stretching or shrinking factor. TEX will
therefore apply this factor to the optical size to obtain the actual size.
10 On most current TEX systems, the paths to the directories that may contain TFM files are found in a file
named texmf.cnf. This file contains the definitions of the environment variables TFMFONTS (the directories
containing TFM files) and OFMFONTS (the directories containing OFM files, which are extended TFM files used
by Ω), as well as VFFONTS and OVFFONTS, which dvips and odvips use to find virtual fonts.

Using Fonts in TEX
The DVI file
After the blizzard of LATEX and TEX commands that we have just seen, now we shall observe the total calm that reigns in a DVI file. Only the essentials are found there: the
locations of glyphs, black boxes (for drawing lines, for example), “specials” (i.e., pockets
of code in other languages, such as the PostScript language or the HTML markup system). How is the data on fonts stored in a DVI file? Through the use of two commands:
• FONTDEF, followed by five parameters:
– the internal number for the font, which will be used to select it as the active font;
– a checksum, which must match the one found in the TFM file (see §B.1);
– the actual size, expressed in sp units, which are integer multiples of 1/216 of an
American printer’s point. Not for nothing did Knuth decide to use this very small
unit of length: he wished to ensure that all the measurements in a DVI file would
be performed in integer arithmetic, with no rounding at all;11
– the optical size, also expressed in sp units;
– the name of the TFM file, without the .tfm extension.
The FONTDEF defines a font and associates it with a number. A font must be defined
before it is first used. All of the font definitions are repeated in the DVI file’s postamble (the part between the last typeset page and the end of the file).
• FONT, followed by the font’s internal number. This command selects as the active font
the one that bears this number. The font so selected will be used for all glyphs to
follow, until the active font is changed again.
By way of example, here is the DVI code for the definition and choice of the font in which
“the text that you are currently reading” is set:
&lt;fontdef id="14" checksum="20786036" size="655360"
designsize="655360" name="T1lemondemn"/>
&lt;font id="14"/&gt;
&lt;set&gt;the&lt;/set&gt;
11 And that, incidentally, was one of the greatest difficulties in converting DVI files to PostScript. When
we “draw” the vertical bars in a table such as the following:
A
B
C
D
the alignment of these bars, one for each line, does not pose a problem in a DVI file, since its extreme precision
makes an error of 1 sp invisible to the naked eye. But when we convert the file to PostScript, the basic unit
becomes the PostScript point; thus we are working with numbers containing three or four decimal places,
and rounding is unavoidable. But how, then, can we be sure that the vertical bar for each line will be joined
correctly with the one in the line above it? To ensure correct alignment, dvips analyzes the file and tracks down
alignments of this type (an approach much like that of hinting fonts), then adjusts the rounding for consistency.

```text
Chapter 9 : Fonts in TEX and Ω, their installation and use
&lt;right dim="167112"/&gt;
&lt;set&gt;te&lt;/set&gt;
&lt;right dim="-"/&gt;
&lt;set&gt;xt&lt;/set&gt;
&lt;right dim="167112"/&gt;
&lt;set&gt;tha&lt;/set&gt;
&lt;right dim="-"/&gt;
&lt;set&gt;t&lt;/set&gt;
&lt;right dim="167112"/&gt;
&lt;set&gt;y&lt;/set&gt;
&lt;right dim="-"/&gt;
&lt;set&gt;ou&lt;/set&gt;
&lt;right dim="167112"/&gt;
&lt;set&gt;ar&lt;/set&gt;
&lt;right dim="-"/&gt;
&lt;set&gt;e&lt;/set&gt;
&lt;right dim="167112"/&gt;
&lt;set&gt;curr&lt;/set&gt;
&lt;right dim="-"/&gt;
&lt;set&gt;ently&lt;/set&gt;
&lt;right dim="167112"/&gt;
&lt;set&gt;r&lt;/set&gt;
&lt;right dim="-"/&gt;
&lt;set&gt;eading&lt;/set&gt;
Since DVI is a binary format, we have decided to present the preceding block of text
in an XML representation. This format, known as DVX, can be obtained by tools called
dvi2dvx and dvx2dvi [157]. In the example, we are using a font whose TFM file is named
T1lemondemn.tfm (explanation: T1 is the encoding; lemonde [= Le Monde Livre], the name
of the font; m, the weight; n, the style), at an actual size of 10 (655,360 being 10 times 216)
and also at an optical size of 10. To make sure that the TFM file has not been corrupted,
we also include this file’s checksum: 20,786,036. This font has the internal number 18,
and we shall use it right away by making it the active font. The set commands that follow
set the strings “the”, “te”, “xt”, “tha”, “t”, “y”, “ou”, “ar”, “e”, “curr”, “ently”, “r”, “eading”.
Between each pair of strings, there is a right command, which causes a move to the right
(or to the left, if negative), also expressed in sp units. Some of these offsets are for word
spaces; others are for kerning. For example, between “te” and “xt” there is an offset of
−19,657 sp, or 0.3 American printer’s points, to the left. We can also see that the word
spaces are all exactly 167,112 sp, or 2.55 points, which shows the extreme rigor with which
TEX sets type.
What can we conclude from this section? That the DVI file contains, all in all, very little
information on the fonts that it uses: a TFM filename, an actual size, and an optical size.
And the software that will process the DVI file is not even required to consult the TFM
```

```text
Using Fonts in TEX
file, because even the kerning pairs have already been explicitly applied in the DVI file.12
All that remains is to replace the &lt;set&gt; commands with actual glyphs.
“Après-TEX”: Confronting the Real World
It is often said that TEX lives in an ivory tower: the DVI file contains only one slight reference to the name of a file in TFM, a format used by TEX alone. We are far removed from
the jungle of fonts in PostScript, TrueType, OpenType, Speedo, Intellifont, and other
formats. Yet to come to the end of the process of document production, we do have to
pass through this jungle. The bold spirit that will lead the way is none other than dvips
(and its near cousin odvips, which is part of the Ω distribution).
Accordingly, the role of dvips is to read the DVI file, find for each TFM file (after checking one or more configuration files) the bitmap font generated by METAFONT or the
PostScript font that corresponds to it, and finally write out a PostScript file that contains
all the required fonts or, if they reside on the printer, references to them.
We shall first consider how dvips processes METAFONT fonts and then consider how it
handles PostScript fonts.
Automatic generation of bitmap fonts from METAFONT source code
We have already mentioned METAFONT, the companion to TEX. It is a programming
language devoted to font creation that we shall describe more precisely in Appendix F.
The most important application of METAFONT has been the Computer Modern family of
fonts, which Knuth developed together with TEX and which remains TEX’s default font
family. These fonts’ filenames follow strict rules: they consist of an abbreviation of the
name of the family, the style, the weight, and an optical size. For example, cmr10 is the
font Computer Modern Roman at 10 points, cmitt12 is the 12-point italic typewriter font,
cmbxsl17 is 17-point bold slanted, etc.
To change from one font to another, one need only change the values of some 62 parameters, which are very clearly explained in [219], a very special book: in its 588 pages, it
presents the entire source code, with comments, for the Computer Modern fonts, together
with images of their glyphs. While the possible combinations are practically unlimited,
Knuth decided to include only 75 basic fonts in the original distribution of TEX. Users,
however, are perfectly free to create their own new fonts by modifying the values of the
parameters.
But even the modification of these parameters to create new combinations of style,
weight, set-width, and size requires a certain basic knowledge of METAFONT, and not
everyone is willing to delve into it. Enter John Sauter [311], who rewrote the code in
which the METAFONT parameters are defined so that now one can tell METAFONT that
one wishes to generate one or another font not supplied by Knuth, simply by stating
that font’s name.
12 Nevertheless, in the case of sophisticated DVI drivers access to TFM files is necessary, not because of
kerning pairs, but to obtain the dimensions of glyph boxes (which are not included in the DVI file).
```

Chapter 9 : Fonts in TEX and Ω, their installation and use
In addition to Sauter’s system, most TEX and Ω distributions are equipped with a manager of searches and file generation that is called kpathsea (= Karl [Berry]’s Path Search
[78]). This system is said to speed up searches for files done by all of the tools of the TEX
world (including TEX, Ω, and dvips) and to generate files on demand. To generate files,
kpathsea has three utilities at its disposal:
• mktextfm, which generates a missing TFM file. This utility is called by TEX and Ω when
they cannot find a TFM file for a font used in the document.
• mktexmf, which generates the METAFONT source file corresponding to the METAFONT used in the document if this font does not already exist.
• mktexpk, which generates a bitmap font from the corresponding METAFONT source
files.
A few words of explanation: PK (for “packaged”) is TEX’s bitmap font format13 (§A.5.3).
These tools combine in the following manner. When TEX encounters a declaration for
the font foo and cannot find a corresponding TFM file, it launches mktextfm. This program searches the disk for a file named foo.mf, whose extension, .mf, is used for METAFONT files. If it finds this file, it launches METAFONT and generates the missing TFM
file. If it cannot find the file, it launches mktexmf in an attempt to generate foo.mf from
generic METAFONT files, and then it launches METAFONT with foo.mf to generate the
missing TFM file. If all these steps fail, TEX uses a default font (Computer Modern Roman).
The same goes for dvips: if a PK font is missing, dvips launches mktexpk in order to generate it, and mktexpk may in turn launch mktexmf to generate the METAFONT source code
for the missing font.14
The three mktex* tools are shell scripts. Only mktexpk has a handful of command-line
options, which are listed below:
• --dpi followed by an integer: the font’s “resolution”
• --bdpi followed by an integer: the font’s “base resolution”
• --mag followed by a rational number: the magnification factor, by default 1.0
• --mfmode followed by a keyword: the “METAFONT mode”
• --destdir followed by a pathname: the directory into which the PK files will be
placed
13 In fact, and for historical reasons, to obtain a PK font one must first go through another bitmap font
format, called GF (for “generic font”, §A.5.2). Converting from GF to PK involves nothing but compressing
the data. The tool that converts GF files to PK is called gftopk. A tool to do the opposite, pktogf, exists for use
in debugging.
14 Note that mktexpk will even try to convert PostScript Type 1 fonts and TrueType fonts to bitmap format,
if it has been properly configured. But this solution is really less than optimal, as the bitmap format is compatible with file formats such as PDF only to a very limited extent.

Using Fonts in TEX
To understand what the first four of these parameters mean, one must enter into the
logic of METAFONT. First of all, let us recall that unlike vector fonts (PostScript Type 1,
TrueType, OpenType), which are rasterized by the printer, bitmap fonts are “ready for
use”. Thus they have to be adapted to the needs of the printer; in other words, there must
be as many versions of the same PK font as there are models of printers.
METAFONT makes use of the notion of “mode”—a certain number of parameters that
describe the characteristics of a given printer. There are, for example, a mode ljfour that
corresponds to the Hewlett Packard LaserJet 4 printer and a mode cx that corresponds to
the Canon PostScript printers equipped with a drum that operate at 300 dots per inch.
The keywords for the METAFONT modes are classified according to types of compatible
printers and are stored in a file named modes.mf ([76] and [69, 70, 173]), which is regularly updated by Karl Berry.
The “base resolution” of the font is in fact the resolution of the printer. This information
is also part of the printer’s METAFONT mode; thus there is no need to specify it if one
uses the --mode option. On the other hand, if one does not know the mode, mktexpk will
attempt to use a generic mode based on the specified resolution.
The font’s magnification factor is the quotient of the actual size and the optical size. Thus
if one wishes to use Computer Modern Roman at 15 points (a size not supplied by Knuth
and therefore not among the sizes available in the original TEX distribution), one can
request the 12-point font magnified by 25 percent, simply by writing:
mktexpk --mag 1.25 cmr12
Note that this manipulation is not needed for the Computer Modern fonts because Sauter’s
“generic files” allow one to request cmr15 directly.
Finally, the “resolution” is the base resolution multiplied by the magnification factor.
Thus the specifications “--bdpi 300 --mag 1.2” and “--dpi 360” are equivalent.
Let us review. If one finds a printer that is represented on the list of METAFONT modes,
one can use --mode and --mag to obtain a bitmap font adapted to the printer and magnified appropriately. If the printer is not on the list, or if one cannot be bothered to look for
it, one can merely state the printer’s resolution by using --bdpi and --mag or even just
-bdpi, which is the product of the two numbers.
Since Knuth, many other people have created METAFONT fonts, which can be found in
TEX distributions and on the Web.
But let us return to the tool mktexpk. It attempts to generate missing fonts automatically.
We have seen that when running this tool manually one needs a certain amount of information, in particular the printer’s METAFONT mode or, at a minimum, its resolution. In
its infinite discretion, mktexpk would not dream of asking us for this information; like a
big boy, it looks up these values by itself in a configuration file. It is our responsibility to
supply the correct values in the configuration file; else our hard copy will never come out
right. This file is called mktex.opt and is usually kept in the configuration directory of
the TEX distribution (/&lt;somewhere&gt;/TeX/texmf/web2c under Unix). Here are the lines
of this file that concern us:

```text
Chapter 9 : Fonts in TEX and Ω, their installation and use
: \${MODE=ljfour}
: \${BDPI=600}
All that we have to do is to replace the values ljfour and 600 by those for our system
(the METAFONT mode and the printer’s resolution).
We close this section by stating that, despite the extreme beauty and elegance of the
METAFONT language, we discourage the use of bitmap fonts in documents, unless,
of course, the document in question is meant to be printed—and only to be printed. To
those who wish to continue to use the Computer Modern fonts, we recommend switching
to their PostScript Type 1 versions, in particular the CM-Super collection of Vladimir
Volovich [341], which is a veritable tour de force, as it covers the TEX glyph encodings
T1, TS1, T2A, T2B, and T2C, as well as the Adobe Standard encoding. We can only hope that
METAFONT will be recast, in the near future, into a tool for creating PostScript Type 1
or TrueType fonts (see Appendix F).
The processing of PostScript fonts by dvips
Now that we have finished our tour of the world of bitmap fonts, let us return to the
twenty-first century and see how to use dvips to produce PostScript code using PostScript
fonts.
At first blush, we are living in the best of worlds, and we have only two tasks to complete
in order to achieve our goal: (a) configure dvips to be aware of the correspondences between TFM fonts and these three types of fonts; (b) ensure that all of the required files
are in the right places, i.e., in directories accessible to dvips.
In fact, reality is a trifle more complex.
A number of problems arise when these two worlds (TEX, on the one hand, and the
PostScript fonts, on the other) come together. A typical problem is conflicting encodings.
For acceptable typesetting in Western European languages, LATEX recommends the T1
font encoding. This encoding is specific to TEX; we have presented a diagram of it in Figure 9-4, on page 246. Since most PostScript Type 1 fonts are encoded in Adobe Standard
(see Figure C-5, page 660), one of the two sides (TEX or the font) must be adapted so that a
collaboration can occur. Another problem that can arise is the absence of certain glyphs.
The Adobe Standard encoding does not contain any accented letters, a fact that makes
it useless for typesetting in the French language. Accented glyphs usually do exist in a
given font, but the encoding hides them. In other cases, the accented glyphs do not exist.
What shall we do then?
We shall see two techniques that enable us to solve problems of this kind: re-encoding and
virtual fonts.
When re-encoding is employed, the PostScript font will be used with an encoding other
than its original one. Thus any accented glyphs that exist in the font will appear in the
encoding, and in the positions in which TEX expects to find them (so as to simulate, for
example, the T1 font encoding).
```

```text
Using Fonts in TEX
The technique of virtual fonts goes further than that. It involves saying to dvips: “If you
find a glyph from this font in a DVI file, replace it with the handful of DVI commands
that I have provided.” The simplest case is replacing one glyph with another, either in
the same font or in a different one. But in fact everything is possible: we can replace a
glyph with thousands of commands, even with the contents of an entire page. Virtual
fonts can also call one another: among the commands that will replace a glyph, there
may be some that call for glyphs in other virtual fonts. Moreover, nothing at the level of
DVI code distinguishes a glyph in a virtual font from a glyph in a “real” font. It is dvips
that concludes that a font for which no TFM file is named in the configuration files for
dvips is not a PostScript font. In that instance, two possibilities exist: either the font is a
virtual font or it is a METAFONT that will be generated at the correct size, as we saw in
the previous section.
The two approaches (conversion of encodings and virtual fonts) are complementary: a
virtual font can do many things, but it cannot operate at the level of a PostScript font
in order to make hidden glyphs appear, for example, or slant or stretch a font. Conversely, conversion of encodings can make hidden glyphs appear, but it can never, for
example, combine accents with letters to yield accented letters.
In this section, we shall see how the configuration file for dvips is arranged and how to
use virtual fonts. In the next section, we shall concern ourselves with the installation of
PostScript fonts in a TEX (or Ω) system.
Configuring dvips
Configuring dvips thus involves informing it of the correspondence between TFM fonts
(recognized by TEX and used in DVI files) and PostScript fonts. These data are stored in
text files whose extension is .map (from the word mapping), the most widespread of which
is psfonts.map. In these files, there is one line of text for each TFM file. This line contains
the name of the TFM file, the PostScript name of the font,15 possibly some PostScript
code that will modify the font, and, finally, possible paths to the files containing the
PostScript font, and any new encoding for the font.
Here is an example:
Bookman-Demi Bookman-Demi
This example illustrates the simplest case: a font recognized by TEX under the name
Bookman-Demi (which presupposes the existence of the file Bookman-Demi.tfm), whose
PostScript name is exactly the same. Since no path is specified to the PostScript font file
or any other, it is implied that the font is “resident”; that is, a copy of the font exists on
the printer’s ROM, RAM or hard disk. If the printer already recognizes this font, there
is no need to incorporate it again into the PostScript file generated by dvips.
Another example:
15 Warning: do not mistake the PostScript name, which is an internal name for the PostScript font, and the
PostScript filename, which is the name of the file containing the PostScript font (cf. §C.3.2).
```

```text
Chapter 9 : Fonts in TEX and Ω, their installation and use
TimesTenRomSC TimesTen-RomanSC
&lt;TimesTenRomSC.pfa
TimesTenItaSC TimesTen-RomanSC " .167 SlantFont " &lt;TimesTenRomSC.pfa
The first line of this example illustrates the most typical case: TEX recognizes this font
under the name of TimesTenRomSC (which, by the way, is a PostScript name abbreviated
according to Adobe’s rules). Its PostScript name is slightly longer (and more descriptive):
“TimesTen-RomanSC”, where “SC” means “small capitals”. Thus it contains the small
capitals for the font Times Ten. Our font is stored on disk in the file TimesTenRomSC.pfa,
whose contents will be embedded in the PostScript file generated by dvips. We have not
given an explicit path to this file; dvips will search for it in the default directories for
PostScript fonts.16
The line below is there to fill a gap in the Adobe Times Ten family of PostScript fonts: italic
small capitals do not exist in this font. Two things have been changed: the name of the
TFM file (on the one hand, this font is slanted; on the other hand, most of the glyphs
require an italic correction), and the part that precedes the name of the PostScript font.
This extra part consists of the PostScript code needed to give all the glyphs in the font a
slant of 0.167 (i.e., an angle of φ = 9.48 degrees, whose tangent is 0.167). We can see that
the same PostScript file is employed; only when this font is used by the printer will the
glyphs be artificially slanted.
In addition to SlantFont, two other keywords are available to us: ExtendFont, which
stretches or compresses all the glyphs in a font horizontally, and ReEncodeFont, which
re-encodes the font. Thus, by writing
TimesTenRomNarrow TimesTen-Roman " 0.87 ExtendFont " &lt;TimesTenRom.pfa
we obtain a font whose set-width is compressed by 13 percent. Now let us see an example
of conversion of the encoding:
uver8r VendomeT-Regu " TeXBase1Encoding ReEncodeFont " <[8r.enc &lt;uver8a.pfb
Here we are using a font known to TEX under the cryptic name uver8r. Its PostScript
name is VendomeT-Regu; behind this technical name is hidden the splendid font Vendôme,
designed in 1952 by François Ganeau for Fonderie Olive in Marseille [39] and widely
used in France in the 1950s and 1960s. Here we have decided to convert the font to use
the T1 encoding. We request this conversion with the command ReEncodeFont, which
takes the parameter TeXBase1Encoding. (PostScript is a programming language that uses
reverse Polish notation: parameters are written before the commands that use them.)
Since this encoding is certainly not recognized by the PostScript printer, we include the
file 8r.enc, which contains its definition.17 Finally, we include the file uver8a.pfb, which
16 These directories are indicated in the global configuration file of the TEX distribution (texmf.cnf), in
the environment variable T1FONTS.
17 The bracket in <[8r.enc indicates to dvips that the file that it has encountered is not yet the font file
but rather an auxiliary file, in this case a file containing an encoding. This bracket is not required, but it can
be useful in some cases for removing ambiguities.
```

```text
Using Fonts in TEX
contains the font’s PostScript data. This time we have a PFB file, thus a binary file. It will
be converted by dvips to PFA format so that it can be embedded in the PostScript code
that is generated.
The reader will no doubt be surprised that we have not given any example of an encoding
file other than 8r.enc. For instance, why is there no encoding file for obtaining the T2A
or T2B or T3 or T4 glyph encoding? The answer is that we do not live in an ideal world.
Fonts containing glyphs of these kinds usually do not follow any standard for naming
glyphs. If the names of the glyphs are not the same from one PostScript Type 1 font to
another, a given encoding file will in practice be useful for only a single font. Thus it
is better to write an encoding file specifically for that font, on a case-by-case basis. Or,
better yet, one can regularize the names of the glyphs, which requires changing the fonts
themselves. We shall discuss this latter possibility in Chapter 12.
Here, then, are the contents of the .map file. But how does dvips know which .map files
it is to read? The names of these files are found in the configuration files for dvips. But
which configuration files are these? The approach to this question taken by dvips is quite
original: instead of preserving the same extension and changing the filename, it does just
the opposite. Thus we have a number of files,18 all of them named “config”, but with
different extensions: config.cm, config.cm-super, config.belleek, etc. Among them,
the file config.ps is the default configuration file for dvips. The others are read at the
user’s request, which is made through the command-line option -P of dvips. One writes:
dvips -P foo ...
to instruct dvips to read the configuration file config.foo.
Within these configuration files, we can use the following syntax to indicate the names
of the .map files to be examined:
p /usr/TeX/texmf/dvips/config/psfonts.map
p +/home/yannis/texmf/config/yhpsfonts.map
Here the + indicates that the file in question will be read after the preceding file, and
in addition to it. Note that if several lines of the .map file refer to the same TFM font,
only the last of them will be retained. Thus the order of the files in the config.* file is
important, as it allows us to install new fonts even if there is a risk that they may already
be defined in the existing configuration files; indeed, by simply adding another configuration file after those that appear by default, we can force our new definitions to replace
any existing ones.
In this section we have examined the possibilities for configuring dvips for use with
PostScript fonts. While the procedure that dvips uses to find fonts may appear very
complex, there is no reason for us to feel discouraged: configuring dvips is itself quite
18 The location of these files is governed by the environment variable TEXCONFIG of the global configuration file of the TEX distribution, texmf.cnf.
```

Chapter 9 : Fonts in TEX and Ω, their installation and use
simple. In broad strokes, it involves inserting into a configuration file as many lines as
there are fonts, each line being built up from the name of a TFM file, the internal name
of the target font, and that font’s filename.
Next, we shall head offin a different direction, still with the goal of making TFM fonts
and “real-world” fonts work together. Instead of modifying the latter, we shall create a
new type of font that will function as an intermediary between the two formats. It will
be called a virtual font.
Virtual fonts
The concept of virtual fonts [220, 180] is quite simple: where TEX sees nothing but a
single glyph, the virtual font will generate a certain number of DVI commands, which
may in turn contain glyphs from virtual fonts and may therefore lead to the production
of new DVI commands, and so forth. Most of the time we use virtual fonts to convert
fonts to a new encoding or to combine letters and accents in order to generate accented
letters.
In a DVI file, the process for replacing glyphs from virtual fonts with the corresponding
DVI commands in an iterative manner, until no more virtual fonts are in use, is called
devirtualization. Devirtualization is carried out internally by dvips, but we can also perform it with an external tool, named dvicopy (or odvicopy, in the Ω distribution).
The format for virtual fonts is called Virtual Font (VF). In Appendix §B.3, the reader will
find a more rigorous description of this font format. For every virtual font, there must
also exist a corresponding TFM file; this is the file that makes it visible to TEX.
But let us return to the VF file. A VF file contains some data beyond those found in TFM
files, specifically two types of data: global data (definitions of the base fonts being used)
and the DVI commands that make up each virtual glyph:
• The choices of active font.
• Push and pop operations applied to coordinates. In a DVI file, we can keep track of the
current position so that we can easily return to it. An example: when setting lines,
we can record the coordinates of the beginning of the line by pushing them onto a
stack; later, when we wish to move to the next line, we can go back to the same place
(by popping the coordinates offthe stack), and then all that we have to do is move
downward.
• Horizontal and vertical movement.
• Black boxes, which are used for drawing lines.
• Specials, which are pockets of code in a format other than DVI (such as PostScript or
HTML code).
By comparing these operations to the commands of the DVI file format, we observe that
the two are practically identical: anything that can be described in a DVI file (other than

Using Fonts in TEX
the change of pages) can also be found in the description of a glyph in a virtual font and
vice versa.
Virtual fonts can be used in a large number of situations:
• The PostScript font that we wish to use is not in the correct encoding: we will create
a virtual font with the desired encoding whose glyphs will be references to the positions of the glyphs in the PostScript font.
• A handful of accented letters, be they letters from the languages of Western Europe
(which are found in almost all fonts) or from those of Eastern Europe (which are
much less commonly found, typically in fonts labeled “CE”, such as Monotype Bookman OldStyle CE, for example), are missing from the font that we wish to use. The
glyphs in the virtual font will be combinations of letters and accents placed in the
correct locations.
• In LATEX, when we call for small capitals, TEX expects to find the small capitals, the full
capitals, and the punctuation marks all in the same font. But PostScript fonts are not
always so arranged. For instance, the “Expert” fonts contain the small capitals and a
few other special glyphs, but no full capitals or punctuation marks. The virtual font
will be a merger of small capitals from the “Expert” font and other glyphs drawn
from the regular font.
• We wish to use old-style figures (of varying height) rather than the modern forms (of
uniform height). Often the glyphs for these figures are found in an “Expert” font.
Once again, the virtual font will be a copy of the normal font in which the figures
will be replaced with those from the “Expert” font.
• We wish to adjust the balance between the uppercase and lowercase letters by enlarging the latter. The virtual font will be made by merging one copy of the original
font (containing everything but the lowercase letters) and another copy of the same
font with a different magnification factor (for the lowercase letters).
• We wish to obtain letterspaced fonts, i.e., those with more space between the letters—
but only between letters, not between letters and punctuation marks, etc. In addition, this space must take into account the kerning that the letters in question would
have if they were not letterspaced. The virtual font will be a copy of the regular font
with a large number of additional kerning pairs for the various combinations of letters.
• We would like to apply PostScript transformations and special effects to the glyphs,
such as by coloring them or subjecting them to rotations, translations, or scaling. The
virtual font will contain PostScript code for each glyph.
• And many other situations can be imagined.

```text
Chapter 9 : Fonts in TEX and Ω, their installation and use
The astute reader may make the following observation: everything described above can
also be done at the level of TEX through the use of commands; after all, TEX is a programming language, thus we can do anything with it. Why, then, should we resort to a
construct as peculiar as a virtual font?
The justification for the utility of virtual fonts is based on a special characteristic of the
way that TEX operates. Specifically, there are three operations that TEX can carry out
only when it is setting type with just one font. These operations are kerning, the formation of ligatures, and hyphenation. In order to be able to kern characters, form ligatures,
or hyphenate words between two glyphs, those glyphs must belong to the same font;
furthermore, no TEX command may come between them.
Thus, in TEX, we can always form any combination of a letter and an accent mark,
whether or not that combination actually occurs in any of the world’s languages. To do
so, we use a primitive by the name of \accent, which takes two arguments: the accent
and the letter to which the accent is to be applied. But if we use this primitive in a word,
there is no longer any way to perform kerning, form ligatures, or hyphenate words. This
situation in TEX is unacceptable.
We can deceive TEX by using a virtual font. We give TEX glyphs that look perfectly normal
from its point of view, and it will set them as usual, with all the required kerning, ligatures, and word divisions. Then dvips comes along and sees that the glyphs in question
must be replaced in the DVI file by combinations of glyphs that will produce the desired
effect. The complexity of the virtual fonts is irrelevant: TEX has already finished setting
the type, the words are attractively kerned, and the lines are beautifully divided. And
TEX did all that without even knowing that the glyphs that it was manipulating would
generate far more DVI code than TEX itself!
Virtual fonts and Acrobat
In the previous section, we presented a fairy-tale description of virtual fonts. We are not
going to debate the existence of Santa Claus, but one thing is certain: the uses of virtual
fonts have their limits as well. The problem is that everything in TEX was designed from
the perspective of hard copy, or of noninteractive output to a screen. That makes sense,
since in 1990, when Knuth published his virtual fonts, neither Acrobat nor the Web yet
existed.
Thus when, using a virtual font, we write an accented letter by placing an accent over the
letter, what is important is the visual result, and it is indeed impeccable. But when DVI
is converted to PostScript, dvips devirtualizes the code; thus the accented letter ceases to
exist. In its place we find separate PostScript glyphs for the letter and for the accent. That
does not pose a problem to the PostScript printer, or even to Acrobat Distiller or ps2pdf
when they convert the PostScript code to PDF.
The problems begin when Acrobat is used. For Acrobat offers a number of interesting
features: the ability to select blocks of text and copy them onto the clipboard, the ability
to search for strings in a PDF document, full-text indexing of PDF documents, Unicode
support. But how can we identify an accented letter if in reality it consists of nothing but
an “accent” character placed over the glyph for a “letter” character?
```

Using Fonts in TEX
Recall that the method (cf. C.3.3) used by Acrobat Distiller to associate Unicode characters with the glyphs that it finds in PostScript files is as follows: it examines the PostScript
name for the glyph; if this name is of the form uniHHHH, where HHHH is a hexadecimal
number, it matches the glyph to Unicode character 0xHHHH; otherwise, it checks a table
of correspondences between glyph names and Unicode characters that was developed by
Adobe. If it cannot find the glyph’s name in this table, the process fails.
If we are to obtain a good result, there must be only one glyph per Unicode character,
and this glyph must bear its correct name in the PostScript font. For example, to obtain
an ‘á’ in a PDF file, which corresponds to the Unicode character 0x00E1 latin small letter a acute, we must use a single glyph, named “aacute”. But when this glyph is not one
but two, therefore a composite of the glyph ‘a’ and a glyph often called “acute”, there is
no way for Acrobat Distiller or ps2pdf to associate it with the correct Unicode character. If
we use the mouse in Acrobat to copy a word containing this letter, we will obtain, at best,
an ‘a’ followed by an acute accent; at worst, we will obtain some haphazard characters.
Among the examples of the use of virtual fonts that we presented in the previous section,
some of them present problems of this type. Let us review them, one by one, and check
their compatibility with conversion to PDF:
• The PostScript Type 1 font that we wish to use is not in the correct encoding, and we plan
to remap its glyphs. No problem arises, but we must nonetheless make sure that the
PostScript glyphs obtained have the correct names.
• A handful of accented letters are missing from the font that we wish to use... ; the glyphs
in the virtual font will be combinations of letters and accents correctly placed. Avoid this
approach! The composite glyphs will under no circumstances be recognized by Acrobat as Unicode characters. Use this approach only when no decomposable Unicode
character corresponds to this combination of a letter and an accent. And even in
this case, be careful (a) to place the accent after the letter in the virtual font, since
that is the convention in Unicode (combining characters occur after base characters)
and (b) to make sure that the name of the glyph for the accent corresponds to the
Unicode character in the table of combining characters (see page 127).
• The “Expert” fonts (in the Adobe Expert encoding; see Figure C-6, page 660) contain the
small capitals and a few other special glyphs, but not the full capitals or the punctuation
marks. Yes, but handle with care, for the glyphs for the small capitals in the “Expert”
font have different names. For instance, ‘a’ has the glyph name Asmall. Because of
this particularity, the correspondence between glyph names and Unicode characters
is very bad.
• We wish to use old-style figures (of varying height) rather than the modern forms (of uniform
height). Same problem as above, since the old-style figures have glyph names such as
oneoldstyle.
• We wish to adjust the balance between the uppercase and lowercase letters by enlarging the
latter. No problem.

Chapter 9 : Fonts in TEX and Ω, their installation and use
• We wish to obtain letterspaced fonts, i.e., fonts with more space between the letters. Handle with care, as no distinction between offsets corresponding to interword spaces
and offsets resulting from kerning is made in a DVI file. Acrobat uses a threshold
beyond which an offset is considered to be a space (and thus corresponds to the Unicode character space) and beneath which an offset is regarded as a kern (no Unicode
character). That works very well under ordinary conditions, but we may exceed the
threshold if we add too much letterspacing, and Acrobat will then insert spaces between the Unicode characters of the string when it is copied.
• We would like to apply PostScript transformations and special effects to the glyphs. In principle that should not create any difficulties, since Acrobat Distiller should correctly
digest the PostScript code. All the same, you had better test it first.
We shall return to this subject when we discuss the editing and modifying of virtual fonts
(page 285).
Installing Fonts for TEX
In the previous section, we described font management under TEX at every level: the user
level; the level of TEX and DVI; and the level of PostScript. At this point, we shall assume
that we have purchased, or downloaded from the network, some fonts that we would
like to use with TEX. If they are METAFONT fonts, we need only place them in a location
where METAFONT can find them, launch mktexlsr so that the TEX system knows they are
there, and the mktexpf and mktexmf scripts will do everything else; there is nothing more
to say on this subject. Therefore, we shall assume that we are dealing with PostScript
fonts.
To adapt them for use with TEX, we have to work at the three levels that we just mentioned:
• At the LATEX level, we have to provide one (or more) NFSS font family name(s) to the
new fonts and prepare one (or more) FD file(s).
• At the TEX/DVI level, we have to prepare TFM files for the new fonts, in both their
original encoding and an encoding that TEX can use, such as T1.
• At the PostScript level, we have to prepare virtual fonts that will make the connection between the TFM files in the TEX encoding and the TFM files in the original
encoding. We must also update the configuration file for dvips, possibly with commands for converting between encodings.
Let us be a little more practical. We are starting from the assumption that we have at our
disposal some PFB/PFA files (PostScript Type 1) and AFM files (PostScript Type 1 font
metrics) files, that we would like to adapt for use with TEX or Ω. Thus we must produce
FD, TFM, and VF files and update the configuration file for dvips.

```text
Installing Fonts for TEX
We shall consider two tools that will enable us to carry out these operations. The first of
them, afm2tfm, is a simple and rapid executable tool suitable for use in ordinary cases. Its
benefits are its speed and ease of use. It generates TFM and VF files directly, along with
the line of code to include in the dvips configuration file.
The second tool, fontinst, is the Rolls-Royce of tools for installing PostScript fonts. It
generates PL and VPL files (i.e., human-readable versions of TFM and VF files; see Appendix B) and even FD files. It is written in TEX and can therefore be used on any platform on which TEX runs. It offers a large number of TEX commands that make it possible
to configure the adaptation of fonts for use with TEX in a very precise manner.
In the examples that illustrate the use of these two tools in the following sections, we
shall use Monotype Centaur, a font designed in 1915 by Bruce Rogers [228, p. 62] and considered by many people to be one of the most beautiful fonts of the twentieth century.
We shall assume that we have just bought this font family and that we have the following
AFM files:
CentaurMT.afm
CentaurMT-Italic.afm
CentaurMT-Bold.afm
CentaurMT-BoldItalic.afm
CentaurExpertMT.afm
CentaurExpertMT-Italic.afm
CentaurExpertMT-Bold.afm
CentaurExpertMT-BoldItalic.afm
and the following PFB files:
CentaMT.pfb
CentaMTIta.pfb
CentaMTBol.pfb
CentaMTBolIta.pfb
CentaExpMT.pfb
CentaExpMTIta.pfb
CentaExpMTBol.pfb
CentaExpMTBolIta.pfb
The “Expert” roman font CentaExpMT.pfb contains—among the glyphs of interest to
us—the small capitals and the ligatures ‘ff’, ‘ffi’, etc. The other “Expert” fonts contain
nothing but ligatures.
The Tool afm2tfm
The program afm2tfm comes with the dvips distribution. Its purpose is to read an AFM
file and possibly one or two font encoding files, and then to generate a TFM file and
possibly a VPL file (the human-readable version of a VF file; see Appendix B).
```

```text
Chapter 9 : Fonts in TEX and Ω, their installation and use
Suppose that we have the AFM file CentaurMT.afm and wish to produce from it a virtual
font named t1centaurmn.vpl, in the T1 encoding. To do so, we need only write:
afm2tfm CentaurMT.afm -v t1centaurmn.vpl -T EC.enc
In the code shown above, EC.enc is a file, provided in the dvips distribution, that describes the T1 font encoding. The -T option indicates that we will need a virtual font in
addition to a reencoded version of the PostScript font in order to obtain the desired result. Once the application is launched, afm2tfm writes the following lines to the console:
CentaurMT CentaurMT " ECEncoding ReEncodeFont " &lt;EC.enc
where the second entry is the PostScript name of the font. This is the line that will have to
be added to the dvips configuration file by appending, if necessary, an instruction to embed the PFB file in the PostScript code produced by dvips:
CentaurMT CentaurMT " ECEncoding ReEncodeFont " <[EC.enc &lt;CentaMT.pfb
What are the actual steps needed to adapt a PostScript font family for use with TEX?
Suppose that we begin with the following AFM files (which correspond to the Monotype
Centaur family; the “Expert” fonts are omitted in this example):
CentaurMT.afm
CentaurMT-Italic.afm
CentaurMT-Bold.afm
CentaurMT-BoldItalic.afm
We must select an encoding and an NFSS family name. For this example, let us take the
T1 encoding, which is the encoding most suited to the Western European languages, and
use centaur as the family name. It will be sensible to name the virtual fonts that we shall
produce T1centaur*.vpl, in which we will replace the asterisk with mn, mit, bxn, or bxit,
thus using the NFSS codes for weight and style. Thus we must run afm2tfm four times,
as shown below:
afm2tfm CentaurMT.afm -v T1centaurmn.vpl -T EC.enc
afm2tfm CentaurMT-Italic.afm -v T1centaurmit.vpl -T EC.enc
afm2tfm CentaurMT-Bold.afm -v T1centaurbxn.vpl -T EC.enc
afm2tfm CentaurMT-BoldItalic.afm -v T1centaurbxit.vpl -T EC.enc
It will generate the following four lines:
CentaurMT CentaurMT " ECEncoding ReEncodeFont " &lt;EC.enc
CentaurMT-Italic CentaurMT-Italic " ECEncoding ReEncodeFont " &lt;EC.enc
CentaurMT-Bold CentaurMT-Bold " ECEncoding ReEncodeFont " &lt;EC.enc
CentaurMT-BoldItalic CentaurMT-BoldItalic " ECEncoding ReEncodeFont "
&lt;EC.enc
```

```text
Installing Fonts for TEX
to which we will add instructions to include the PFB files, as follows:
CentaurMT CentaurMT " ECEncoding ReEncodeFont " <[EC.enc
&lt;CentaMT.pfb
CentaurMT-Italic CentaurMT-Italic " ECEncoding ReEncodeFont " <[EC.enc
&lt;CentaMTIta.pfb
CentaurMT-Bold CentaurMT-Bold " ECEncoding ReEncodeFont " <[EC.enc
&lt;CentaMTBol.pfb
CentaurMT-BoldItalic CentaurMT-BoldItalic " ECEncoding ReEncodeFont "
<[EC.enc &lt;CentaMTBolIta.pfb
Then we will add these lines at the end of psfonts.map or any other configuration file
that dvips may use.
Next, we must convert the VPL files to VF format:
vptovf T1centaurmn
vptovf T1centaurmit
vptovf T1centaurbxn
vptovf T1centaurbxit
and copy the TFM and VF files to locations where TEX will be able to find them. Finally,
we must prepare the FD file T1centaur.fd:
\DeclareFontFamily{T1}{centaur}{}
\DeclareFontShape{T1}{centaur}{m}{n}{ <-> T1centaurmn }{}
\DeclareFontShape{T1}{centaur}{m}{it}{ <-> T1centaurmit }{}
\DeclareFontShape{T1}{centaur}{bx}{n}{ <-> T1centaurbxn }{}
\DeclareFontShape{T1}{centaur}{bx}{it}{ <-> T1centaurbxit }{}
which we shall also place in a location where TEX can find it.
Basic Use of the Tool fontinst
In the previous section, we examined practically all the features of afm2tfm. We saw that it
is a tool for adapting PostScript fonts for use with TEX that also supports re-encoding. The
tool fontinst, by Alan Jeffrey [199], goes much further: it allows us to generate arbitrarily
configurable VPL files from one or more AFM files.
For example, if among the fonts that we wish to adapt there are some that use the “Expert” encoding, we have no choice but to use fontinst, since afm2tfm is unable to read
multiple AFM at the same time and merge the compiled data into a single VPL font.
fontinst is written in TEX, which means that it comes with a TEX file that “drives” the
procedure and that TEX, when it reads this file, will begin to read the required AFM files
and some auxiliary files of fontinst so that it can eventually write out the required PL,
VPL, and FD files.
```

Chapter 9 : Fonts in TEX and Ω, their installation and use
In this section, we shall consider only the basic commands of fontinst, since our aim is
merely to install PostScript fonts directly for use with TEX. We shall return to fontinst later
in this book (page 518), when we discuss ways to adapt fonts to meet the user’s needs.
Then we shall examine in detail the commands that make it possible to define virtual
glyphs one by one.
Assume that we are in the same situation as in the previous section; that is, we have the
following AFM files:
CentaurMT.afm
CentaurMT-Italic.afm
CentaurMT-Bold.afm
CentaurMT-BoldItalic.afm
But this time let us assume that we also have a few other Monotype Centaur fonts—the
“Expert” fonts, shown here:
CentaurExpertMT.afm
CentaurExpertMT-Italic.afm
CentaurExpertMT-Bold.afm
CentaurExpertMT-BoldItalic.afm
To produce fonts in the T1 encoding, we will need to collect the glyphs from all the AFM
files, and that will entail reencoding the PostScript fonts (since some glyphs may not
appear in the encoding). The approach of fontinst is as follows:
• During the first pass, it will convert a number of AFM files. This conversion may be
done for reasons of scaling, slanting the glyphs, or changing the encoding.
• Next, it will read the AFM files generated, in an order specified by the user.
• When it finds a glyph that it needs to process, it makes a note of the glyph and does
not look for that glyph again.
• When it has processed all the AFM files, it generates a VPL file in the requested encoding, using all the glyphs that it has found.
The file that drives fontinst must have the following structure: first, a command to include
the fontinst macros and a command to start the process:
\input fontinst.sty
\installfonts
At the end of the file, the corresponding closing commands are used:
\endinstallfonts
\end

```text
Installing Fonts for TEX
According to the principles of NFSS, we need an FD file for each family of fonts that we
are to create. Here is the command that creates this file; it is written in the file that drives
fontinst:
\installfamily{T1}{centaur}{}
Now let us convert the fonts to the T1 encoding (which is not necessary for the “Expert”
fonts, since these use a special encoding of their own and generally do not contain any
hidden glyphs). We need new names for the AFM files to be generated; we shall simply
append “T1” to the names that we have, yielding CentaMTT1, CentaMTItaT1, etc.
Here is the code that will convert our four fonts to the T1 encoding so that any glyphs
that may be hidden by these fonts’ encodings will be revealed:
\transformfont{CentaurMTT1}{\reencodefont{T1}{
\fromafm{CentaurMT&#125;&#125;}
\transformfont{CentaurMT-ItalicT1}{\reencodefont{T1}{
\fromafm{CentaurMT-Italic&#125;&#125;}
\transformfont{CentaurMT-BoldT1}{\reencodefont{T1}{
\fromafm{CentaurMT-Bold&#125;&#125;}
\transformfont{CentaurMT-BoldItalicT1}{\reencodefont{T1}{
\fromafm{CentaurMT-BoldItalic&#125;&#125;}
The other transformations that can be performed with fontinst are general scaling
(\scalefont), scaling on the horizontal or vertical axis only (\xscalefont, \yscalefont), and slanting (\slantfont). In the example above, we read AFM files (\fromafm{
...}), but we could also read PL files (\frompl{...}) or MTX files (\frommtx{...}).
But let us return to our example. Of course, we must notify dvips that a conversion of
encodings has occurred, and that is the only task that fontinst does not perform—perhaps
because dvips is not the only DVI driver and fontinst decided that if it could not produce
code for every DVI driver it might as well not produce code for any of them. Thus the
lines to append to the configuration file for dvips are the following:
CentaurMTT1 CentaurMT " ECEncoding ReEncodeFont "
&lt;EC.enc &lt;CentaMT.pfb
CentaurMT-ItalicT1 TimesNewItalic " ECEncoding ReEncodeFont "
&lt;EC.enc &lt;CentaMTIta.pfb
CentaurMT-BoldT1 TimesNewBold " ECEncoding ReEncodeFont "
&lt;EC.enc &lt;CentaMTBol.pfb
CentaurMT-BoldItalicT1 TimesNewBoldItalic " ECEncoding ReEncodeFont "
&lt;EC.enc &lt;CentaMTBolIta.pfb
Having obtained fonts in the desired encoding, we can now move on to the heart of the
matter and install the NFSS fonts. To do so, we shall use the command \installfont,
which takes the following arguments:
```

Chapter 9 : Fonts in TEX and Ω, their installation and use
• The name of the VPL file generated
• A list of AFM, MTX, or PL files, to be read in this order (possibly followed by the
keyword scaled and a magnification factor à la TEX, which is to say that it is multiplied by 1,000
• The fontinst encoding to use
• The NFSS attributes of the generated font: its NFSS encoding, family, weight, style,
and size
Observations:
1. We have already mentioned the “MTX” file format on two occasions. Do not worry,
dear reader: MTX is not a new font format. It is merely a form in which fontinst rewrites
an AFM file in a syntax that TEX finds easier to digest. Thus, the first time a font family
is processed by fontinst, the current directory is filled with MTX files. That eliminates the
need to reread the same AFM files.19 Also note that when we say that fontinst “reencodes”
a font, that actually means that it creates an MTX file and a PL file in the new encoding
when it reads an AFM file. Thus do not expect to find new AFM files; fontinst writes out
only MTX and PL!
2. We have here two “encodings”, which we shall call the “fontinst encoding” and the
“NFSS encoding”. These result simply from the fact that the NFSS encodings OT1, T1,
etc., are closer to character encodings than to font encodings, while the fontinst encodings
are genuine font encodings. Let us explain! We have not mentioned it up to now, but
whether a font contains lowercase letters or small capitals, modern or old-style figures, we
shall always say that it is of (NFSS) encoding T1. In TEX/NFSS, the change from a normal
font to a font containing small capitals is a change of font, not one of encoding. Nevertheless, fontinst provides four different encodings (in the sense of “fontinst encodings”), all
of them derived from the encoding (in the sense of “NFSS encoding”) T1:
NFSS encoding
fontinst encoding
Small capitals
Old-style figures
T1
T1
no
no
T1
T1c
yes
no
T1
T19
no
yes
T1
T19c
yes
yes
Here, then, is the code to write for our eight AFM fonts, which will produce five NFSS
fonts (the four combinations of roman/italic, light/bold, and the light upright small capitals):
19 Important corollary: if you modify your AFM files, delete all the MTX files so that they will be generated
afresh. Unfortunately, fontinst is not make and thus is not able to check the date of the last modification of your
MTX files relative to that of the AFM files from which they were generated...

Installing Fonts for TEX
\installfont{T1centaurmn}{CentaurMTT1,CentaurExpertMT,
latin}{T1}{T1}{centaur}{m}{n}{}
\installfont{T1centaurmit}{CentaurMT-ItalicT1,CentaurExpertMT-Italic,
latin}{T1}{T1}{centaur}{m}{it}{}
\installfont{T1centaurbxn}{CentaurMT-BoldT1,CentaurExpertMT-Bold,
latin}{T1}{T1}{centaur}{bx}{n}{}
\installfont{T1centaurbxit}{CentaurMT-BoldItalicT1,
CentaurExpertMT-BoldItalic,latin}{T1}{T1}{centaur}{bx}{it}{}
\installfont{T1centaurmsc}{CentaurMTT1,CentaurExpertMT,
latinsc}{T1c}{T1}{centaur}{m}{sc}{}
Two more comments:
1. We can see that the keywords latin and latinsc appear at the end of the list of AFM
files. These are MTX files that come with fontinst and whose role is to consolidate the generated VPL files generated through a salvage operation. Let us explain. For every glyph
that is not found in any AFM file on the list, a replacement, or a compromise solution,
will be inserted into these files. Those glyphs that can be generated by their companions
(for example, the Dutch ligature ‘ij’ can be produced by concatenating the glyph ‘i’ and
the glyph ‘j’) will be so generated. Those that cannot be generated or simulated (such as
the Scandinavian glyph thorn ‘þ’) will be replaced by a black box and will generate a
PostScript error message. The fact that these files appear at the end of the list ensures us
that we have already searched through all the AFM files by the time that we reach that
point, and thus that it is really a “solution of last resort”. It is, in fact, essential to leave
latin and latinsc at the end of the list of AFM files.
2. fontinst will also create PL files for the “Expert” fonts. Thus be careful not to forget
to add the following lines (with no instructions about reencoding) to the configuration
file for dvips:
CentaurExpertMT CentaurExpertMT &lt;CentaExpMT.pfb
CentaurExpertMT-Italic CentaurExpertMT-Italic &lt;CentaExpMTIta.pfb
CentaurExpertMT-Bold CentaurExpertMT-Bold &lt;CentaExpMTBol.pfb
CentaurExpertMT-BoldItalic CentaurExpertMT-BoldItalic &lt;CentaExpMTBolIta.pfb
Let us now compile the driver file in TEX (the plain format is sufficient; there is no need
to use LATEX). It will then generate a number of files:
• MTX files: these may be deleted when we are finished;
• PL files: these must be converted to TFM with pltotf and placed in a location where
TEX can find them;
• VPL files: these must be converted to VF with vptovf and placed in a location where
dvips can find them;
• An FD file, which must be placed in a location where TEX can find it.

Chapter 9 : Fonts in TEX and Ω, their installation and use
˝0x
`
´
ˆ
˜
¨
˝
˚
ˇ
˘
¯
˙
¸
˛
‚
‹
›
˝1x
“
”
„
«
»
ı
ff
fi
fl
ffi
ffl
˝2x
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
+
,
-
.
/
˝3x
:
;
<
=
>
?
˝4x
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
K
L
M
N
O
˝5x
P
Q
R
S
T
U
V
W
X
Y
Z
[
\
]
^
_
˝6x
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
k
l
m
n
o
˝7x
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
{
|
}
~
-
˝8x
˘A
˛A
´C
ˇC
ˇD
ˇE
˛E
˘G
´L
L’
Ł
´N
ˇN
˝O
´R
˝9x
ˇR
´S
Š
¸S
ˇT
¸T
˝U
˚U
Ÿ
´Z
Ž
˙Z
IJ
˙I
¯d
§
˝Ax
˘a
˛a
´c
ˇc
d’
ˇe
˛e
˘g
´l
l’
ł
´n
ˇn
˝o
´r
˝Bx
ˇr
´s
š
¸s
t’
¸t
˝u
˚u
´z
ž
˙z
ij
¡
¿
£
˝Cx
À
Á
Â
Ã
Ä
Å
Æ
Ç
È
É
Ê
Ë
Ì
Í
Î
Ï
˝Dx
Ð
Ñ
Ò
Ó
Ô
Õ
Ö
Œ
Ø
Ù
Ú
Û
Ü
Ý
Þ
SS
˝Ex
à
á
â
ã
ä
å
æ
ç
è
é
ê
ë
ì
í
î
ï
˝Fx
ð
ñ
ò
ó
ô
õ
ö
œ
ø
ù
ú
û
ü
ý
þ
ß
˝0
˝1
˝2
˝3
˝4
˝5
˝6
˝7
˝8
˝9
˝A
˝B
˝C
˝D
˝E
˝F
Figure 9-9: The layout of the font t1centaurmn, produced by fontinst. Compare it with the table
of the T1 glyph encoding (Figure 9-4). The font does not contain glyphs for ‘%’, ‘j’, ‘N’, or ‘n’; these
glyphs have been replaced by black boxes.
Note that TEX reported a number of error messages during compilation, such as these:
Warning: missing glyph `endash'.
Warning: missing glyph `emdash'.
Warning: missing glyph `perthousandzero'.
Warning: missing glyph `dotlessj'.
Warning: missing glyph `Ng'.
Warning: missing glyph `ng'.
These mean that the glyphs for endash (the en dash, ‘–’), emdash (the em dash, ‘—’),
perthousandzero (the little zero ‘%’ that we write after the percent sign ‘%’ to produce
the per-mille sign, the per-ten-thousand sign, and so on: “%%, %%%, %%%%,... ”), dotlessj
(the ‘j’ with no dot, which is needed when accents are placed over a ‘j’), Ng and ng (the
Sámi letter eng ‘N, n’) could not be simulated by their companions and thus were replaced by black boxes, as can be seen in Figure 9-9. In the same figure, the reader will see
several glyphs for the languages of Central Europe. They were generated by combining
a letter with an accent. The result is rather poor in some cases, such as, for example, the

Installing Fonts for TEX
letters ‘´c’, ‘´r’, and ‘´s’, whose accents are set peculiarly far to the left, or the Polish barred L
‘Ł’, whose bar should be symmetrical relative to the downstroke. Later (page 520) we
shall see how to correct these small errors by modifying the configuration file for fontinst
or by directly editing the virtual fonts themselves.
For the sake of completeness, here are a few substitutions that are generally added to FD
files in order to ensure that the substitution mechanism works correctly:
\substitutesilent{b}{bx}
\substitutesilent{sb}{bx}
\substitutesilent{db}{bx}
\substitutesilent{sl}{it}
With these instructions, we replace bold, semi-bold, and demi-bold with bold extended
and also replace “slanted” type with italic. There is a variant of \substitutesilent,
called \substitutenoisy, which exhibits the same behavior but also displays an error
message.
In this section, we have seen the basic ways to use fontinst to install a family of PostScript
fonts. fontinst manages to get the most out of PostScript fonts; we get the best results
when we combine fontinst with a reencoding of the fonts, as done in our example, and
when we thus cause all the interesting glyphs to become visible. A few problems remain:
• Missing glyphs. There will always be some, especially with font encodings other than
T1. In this case, there is only one solution: one must design them oneself with fontediting software such as FontStudio, Fontographer, FontLab, or FontForge. We shall
see how to do so in Chapter 12.
• Accents placed incorrectly. This problem can be solved with an ad hoc configuration
of fontinst; we shall see the procedure on page 520. But first we must figure out where
the problem originates, and that involves delving into the VPL and AFM files in
search of anything that could have caused the improper alignment.
• Some incompatibilities between virtual fonts and Acrobat. To solve this problem,
one must, once again, open the font with font-editing software—this time not to
design new glyphs but (a) to correct the names of the glyphs, if necessary; and (b) to
combine letters and glyphs in order to form “precomposed” glyphs. Then all of the
problems of virtual fonts at the Acrobat level will disappear.
Before finishing this chapter on basic font management in TEX and Ω, let us present one
more little section on a type of fonts on the road to extinction: the Multiple Master fonts.
Multiple Master fonts
Neither TEX nor Ω can directly process Multiple Master fonts (see Appendix C.4), in the
sense of being able to take advantage of these fonts’ inherent transformation capabilities
to produce special effects or perform much more powerful NFSS commands.

Chapter 9 : Fonts in TEX and Ω, their installation and use
For example, one might have envisioned NFSS commands with numerical values for
weight and set-width that, when combined with optical size, could produce Multiple
Master fonts by supplying triplets of the values of these parameters. One might also have
envisioned a TEX or an Ω that could calculate actual sizes and optical sizes in a way that
would make books run to an exact multiple of 16 pages, which would greatly simplify
the printers’ jobs. Other possibilities could also be imagined.
But these possibilities do not exist, and the fact that the Multiple Master fonts have been
officially abandoned by Adobe does not help matters. Only one solution exists for using
Multiple Master fonts in TEX or Ω: extracting the desired instance and using it like an
ordinary Type 1 font.
To this end, there are the tools mmafm and mmpfb [223]:
mmafm --weight=380 --width=460 --optical-size=6 MinionMM.amfm \
> minion_380_460_6.afm
mmpfb --weight=380 --width=460 --optical-size=6 MinionMM.pfb \
> minion_380_460_6.pfb
Here we generate the instance 380 460 6 of a font for which we have an AMFM file (the
Multiple Master version of the AFM format, cf. §C.4.2), all the AFM files for the masters
(a list of these masters appears in the AMFM file;20 there can be as many as eight), and a
PFB file. These files must all be in the current directory.
In the preceding lines of code, we used three axes. There is also a fourth, called --style
(not used by the Adobe Minion MM font in our example). Two other useful options:
• --precision, which gives the number of decimal digits to use when performing divisions (in mmafm and mmpfb). The default value is 3 digits of precision; but if we
wish to adapt the font subsequently for use with TEX by running fontinst, we should
instead select the value 0, because fontinst is not good at digesting numbers with a
decimal part. In this case, take care to apply the same precision to both the AFM
files and the PFB files so as not to create discrepancies between the two.
• --kern-precision (only in mmafm), the threshold below which kerning pairs are ignored (2 by default). Since kerning pairs are calculated through linear interpolation
(as is the contour of each glyph as well), these kerning values may become very small.
Below a certain threshold, the kerning pairs will have no visual effect; thus we can
use this option to disregard them.
After performing these operations, we proceed, as usual, to obtain the TFM, VF, and FD
files and add a line to the configuration file for dvips. The only precaution that must
be taken is to inspect the AFM file generated by mmafm to obtain the PostScript name
assigned to the newly generated font. Ordinarily this name is produced from the name
20 Warning: the AFM files must have the PostScript names of the fonts that they represent. For example,
the AFM file for the font whose FontName is MinionMM-SixIt must also have this name (and not MinioMMSixIt,
which is the abbreviated version of the name).

Customizing TEX Fonts for the User’s Needs
of the “parent” font followed by the values of the parameters, separated by underscores:
MinionMM_380_460_6_ (here there is one extra underscore because the fourth axis has no
value), but it is prudent to check. In our case, the line for the dvips configuration file will
therefore be:
minion_380_460_6 Minion_M_380_460_6_
" ECEncoding ReEncodeFont " \
&lt;EC.enc &lt;minion_380_460_6.pfb
Customizing TEX Fonts for the User’s Needs
In this section, we shall learn how we can reconfigure fontinst to obtain fonts customized
for our typographic needs: with accented letters, slanted letters, colored letters, special
ligatures, letterspacing, special behavior, etc. First, however, we must study the mechanism by which fontinst describes a virtual font and then apply it to a number of interesting examples.
How to Configure a Virtual Font
Here is the philosophy of fontinst:
• To produce a virtual font, we need a font encoding and a set of glyphs. The encoding
is describen in an ETX file (extension .etx); the glyphs are described in a set of MTX
files (extension .mtx).
• Each \setslot entry in an encoding file is associated with a number (the position of
the glyph in the encoding) and contains a glyph’s name. In an entry in an encoding
file, we can also provide other information:
– Any ligatures (\ligature) whose sequences begin with the glyph in question
– The fact that the glyph is part of a sequence of substitutions, as in mathematical
fonts, or a set of large mathematical delimiters (see Appendix B.1.4, where we
describe these gadgets)
• A glyph must be defined by a \setglyph instruction. It may later be redefined
(\resetglyph).
• The behavior of a glyph with respect to kerning may be similar to that of another
glyph; for instance, ‘é’ kerns in the same way as ‘e’. This fact is established through
the instructions \setleftrightkerning, \setleftkerning, and \setrightkerning,
depending on whether the kerning is similar on both sides, only on the left side, or
only on the right side.
• The definition of a glyph may include different types of commands. Thus we can be
very precise about the construction of a glyph from several others, possibly drawn
from different fonts at different sizes.

Chapter 9 : Fonts in TEX and Ω, their installation and use
• The set-width of the resulting glyph may be calculated automatically from its components, or it may be modified after the fact, possibly by starting with the set-widths
of other glyphs and making appropriate calculations.
• More generally, all of the richness of the TEX programming language can be put to
use to allow arbitrarily complex calculations and constructs.
Let us take these points one at a time. We have mentioned the ETX and MTX files. Why
do we need these two types of files? The answer is connected to the nature of virtual fonts:
• Since a virtual font may collect glyphs from multiple fonts, often the same glyph exists
in several fonts. We shall take the first instance that we find, in the order in which the
fonts are read. Thus we do indeed need multiple MTX files that contain descriptions
of the glyph.
• On the other hand, a virtual font may use only one encoding. Thus we shall read
only one ETX file, which we must choose with care.
The difference between MTX and ETX is reflected in the fontinst syntax for installing
fonts, as we have already seen on page 280:
\installfont{T1centaurmsc}{CentaurMTT1,CentaurExpertMT,
latinsc}{T1c}{T1}{centaur}{m}{sc}{}
The names CentaurMTT1, CentaurExpertMT, and latinsc correspond to MTX files that
will be read in that order. The first contains the most important glyphs; the second contains the glyphs for the small capitals; the third is there for any salvage operations: if
a glyph is hopelessly absent, latinsc.mtx will suggest a substitute. Using the third argument of this command, fontinst will read the ETX file T1c.ext, which designates the
unique encoding of the virtual font that we are going to produce. Its name, “T1c”, gives
a hint about its nature: it contains the T1 (Cork) TEX encoding, for small capitals.
The ETX file
The ETX file has a structure of the following type:
\relax
...documentation...
\encoding
...encoding commands...
\endencoding
The “encoding commands” will be in this form:
\setslot{foo}
\comment{This is the glyph foo}
\endsetslot

```text
Customizing TEX Fonts for the User’s Needs
This command associates the glyph foo with the current position. The current position
is 0 by default and increases by 1 every time \setslot appears. We can also be explicit
and assign the glyph bar, for example, to position 10,564:
\nextslot{10564}
\setslot{bar}
\comment{This is the glyph bar}
\endsetslot
There is also the command \skipslots{i}, which allows us to skip i positions in the
table. The \comment command allows us to insert a comment into the code.
TEX fonts offer the possibility of defining ligatures, which TEX will automatically employ.
For instance, we can specify that whenever an ‘f’ is followed by an ‘i’, these two glyphs
will be automatically replaced by the glyph ‘fi’. This approach is compatible with both
hyphenation (the ‘fi’ ligature will be changed back to the glyphs ‘f’ and ‘i’ if we should
have to divide the word between those two letters) and kerning (we can create kerning
pairs with ‘fi’ and any other glyph whatsoever).
There are eight types of ligatures in TEX. Simple ligatures (which we shall call LIG) simply
replace a pair of glyphs with another glyph. The other seven types of ligatures (/LIG,
/LIG>, etc.), known as smart ligatures, will leave one or both of the glyphs in place while
adding a new glyph, etc. We shall describe the eight types of ligatures in detail in §B.1.3.
To obtain a ligature from a glyph whose position we are defining, we use the \ligature
command. For example, here is a possible \setslot instruction for the letter ‘f’, including all the ligatures that exist in the font:
\setslot{f}
\ligature{LIG}{i}{f_i}
\ligature{LIG}{f}{f_f}
\ligature{LIG}{l}{f_l}
\ligature{LIG}{t}{f_t}
\ligature{LIG}{j}{f_j}
\comment{The letter 'f', a descendant of the Greek digamma F}
\endsetslot}
Note that the \ligature command does not repeat the letter ‘f’, since it is already known:
it is, after all, the current glyph. Thus \ligature{LIG}{i}{f_i} indicates that we wish
to obtain a ligature of LIG type between the current glyph (f) and the glyph i: the glyph
that will replace these two is f_i (according to the rules for naming glyphs that were
formulated by Adobe, page 659).
Finally, two “gadgets” from TEX’s mathematical fonts: the sequence of extensible glyphs
and composition (see Appendix B.1.4). Here is how to tell TEX which is the glyph larger
than the current glyph that must be used when a mathematical expression requests a
delimiter of a larger size:
```

```text
Chapter 9 : Fonts in TEX and Ω, their installation and use
\setslot{foo}
\nextlarger{foo2}
\endsetslot
where foo2 is the larger glyph that immediately follows foo in the sequence of extensible
glyphs arranged in order of increasing size.
Likewise, to specify that an extended brace is formed from an upper part called top, a
lower part called bottom, a middle section called middle, and a repeating segment called
repeating, we write:
\setslot{repeating}
\varchar
\vartop{top}
\varbot{bottom}
\varmid{middle}
\varrep{repeating}
\endvarchar
\endsetslot
The MTX file
This is where things become interesting. In the previous section, we described the ETX
file, which contains the font’s encoding. Here we shall describe the glyphs, by all possible
and conceivable means. If these glyphs appear in the encoding, very well: they will also
appear in the font. If they do not appear in the encoding, they will be ignored. Thus we
can use the same MTX files with multiple ETX files.
An MTX file must have a structure of the following kind:
\relax
...documentation...
\metrics
...definitions of glyphs...
\endmetrics
In order to understand why this file is useful, let us take a typical line from a fontinst
installation file:
\installfont{T1centaurmsc}{CentaurMTT1,CentaurExpertMT,
latinsc}{T1c}{T1}{centaur}{m}{sc}{}
There is a fundamental difference between the two files CentaurMTT1.mtx and CentaurExpertMT.mtx and the file latinsc.mtx: the former are generated on the fly from AFM
files of the same name; the latter is painstakingly prepared by the developer. Thus the
former contain, in the ideal case, nothing but the information contained in the AFM
```

Customizing TEX Fonts for the User’s Needs
files. It is latinsc.mtx that will take advantage of the information to do more interesting
things. We also have the option of redefining glyphs. This option would not make sense if
we humans were the only ones to define them, but it assumes capital importance when
the glyphs are defined in a way that may not seem optimal at the first glance at the AFM
files.
The MTX file that we prepare, and that we ultimately instruct fontinst to read, is thus the
file of last resort: in it, we correct poorly defined glyphs and add those that could not be
defined.
To define a new glyph, we use the command
\setglyph{foo}
...glyph commands...
\endsetglyph
where foo is the name of the glyph, a name that must be strictly identical (same case, no
whitespace) to the one used in the ETX file.
If the glyph has already been defined, we instead use the following variant:
\resetglyph{foo}
...glyph commands...
\endresetglyph
To avoid error messages if we are not sure whether the glyph in question has been defined, we may use the command \unsetglyph{foo}, which will cause fontinst to “forget”
the glyph.
What are these celebrated “glyph commands” that we can insert in a glyph’s definition?
Well, this should come as no surprise to the reader who has read this book carefully and
has understood the principles behind virtual fonts: a virtual font is a font that replaces
references to glyphs in a DVI file with some DVI instructions. Thus we have glyph commands associated with various types of DVI instructions:
• The command \glyph{bar}{1000} will insert the (real or virtual) glyph bar. Warning: bar must have been defined beforehand. The number 1000, divided by a thousand, indicates the glyph’s scaling factor. The displacement vector for this glyph will
start at the current point of displacement.
• The command \glyphrule{123}{456} will draw a black box of width 123 and height
456 thousandths of an em.
• The commands \movert{500} and \moveup{500} will move the current point rightwards or upwards by 500 thousandths of an em.
• The commands \push and \pop will, respectively, push the current point onto the
stack and pop it offthe stack.

Chapter 9 : Fonts in TEX and Ω, their installation and use
• Finally, \glyphspecial{code} will insert the code code at this point, much like the
\specials of TEX.
In addition to these five commands, there is a sixth that generates a PostScript error message: \glyphwarning{Warning: missing glyph!} will warn us when dvips is attempting
to insert the missing glyph into the PostScript code.
The commands above enable us to combine glyphs and calculate the global displacement
vector by using the vectors of the combined constituents—but we may often wish to
change the metrics of the new glyph directly. To do so, we have the following commands
at our disposal:
• \resetwidth{1234}, to redefine the glyph’s set-width
• \resetheight{1234}, for its height
• \resetdepth{1234}, for its depth
• \resetitalic{1234}, for its italic correction
• \resetglyphbb{a}{b}{c}{d}, to redefine its bounding box
The bounding box is the rectangle that contains the glyph. It thus depends entirely on the
glyph and is independent of the set-width.
It is interesting to observe that when we redefine a glyph, we can refer to its previous
definition in the new definition. For example:
\resetglyph{A}
\movert{30}
\glyph{A}{1000}
\movert{30}
\endresetglyph
will increase the spacing on each side of the glyph A, without causing an infinite loop, as
we might have expected it to do.
We have used whole numbers in the various definitions that we have presented above.
But fontinst would be of very little interest if we were required to give explicit numbers
systematically. All of the system’s power comes from the fact that we can use the dimensions of glyphs that are already defined:
• \width{foo}, \height{foo}, \depth{foo}, and \italic{foo} yield the set-width,
height, depth, and italic correction of the glyph foo, which must have been defined
previously.
• \bbleft{foo}, \bbbottom{foo}, \bbright{foo}, and \bbtop{foo} yield the four coordinates of the glyph’s bounding box.

Customizing TEX Fonts for the User’s Needs
• \kerning{foo}{bar} yields the kerning, if any, between foo and bar.
We can perform arbitrarily complex calculations by using the fundamental arithmetical
operations:
• \neg{a}, the negation of a
• \add{a}{b}, the sum a+b
• \sub{a}{b}, the difference a−b
• \mul{a}{b}, the product ab
• \div{a}{b}, the quotient a
b
• \scale{a}{b}, the product
ab
1,000
• \max{a}{b}, the value max(a,b)
• \min{a}{b}, the value min(a,b)
• \half{a}, half of a, rounded down
• \otherhalf{a}, half of a, rounded up
We can also define numeric variables corresponding to the relevant dimensions of the
font. For example:
\setint{italicslant}{0}
% slant
\setint{xheight}{\height{x&#125;&#125;
% height of the lowercase letters
\setint{capheight}{\height{A&#125;&#125;
% height of the capitals
\setint{ascender}{\height{d&#125;&#125;
% height of the ascenders
\setint{descender}{\depth{g&#125;&#125;
% depth of the descenders
\setint{underlinethickness}{40} % thickness of the underscore
\setint{smallcapsscale}{800}
% scaling factor for small capitals
\setint{smallcapskerning}{900}
% kerning factor for small capitals
The values of these variables can be used in calculations by means of the \int{variable}
command. They can also be modified at any time.
We shall have the opportunity to see some typical examples of several of these calculations.
But let us return to the contents of the MTX file. Aside from defining glyphs, we can also
define kerning behavior equivalences. For example, it is quite natural to suppose that the
ligature ‘Œ’ will behave, with respect to other glyphs, like an ‘O’ on the left and like an ‘E’
on the right. That fact can be expressed with the following commands:

```text
Chapter 9 : Fonts in TEX and Ω, their installation and use
\setleftkerning{OE}{O}{1000}
\setrightkerning{OE}{E}{1000}
where, once again, 1000 represents a scaling factor multiplied by 1,000. There is also a
command, \setleftrightkerning, that combines the previous two:
\setleftrightkerning{Eacute}{E}{1000}
means that Eacute kerns like E on both sides.
For a complete and detailed list of the available commands, the reader is invited to consult the documentation for fontinst [200].
ETX and MTX files for a simple virtual font
In the simple case, where we use only the information contained in the AFM files, there
is an ETX file for the T1 encoding, an MTX file for each AFM file, and an MTX file “of
last resort”. What do these files contain?
The file t1.etx contains definitions of code points in the encoding’s table, of the following type:
\setslot{comma}
\ligature{LIG}{comma}{quotedblbase}
\comment{The comma `,'.}
\endsetslot
Here we have defined a code point for the glyph comma and a ligature of two consecutive
commas that produces a glyph called quotedblbase, i.e., the German opening quotation
mark („).
There is a trick in this file (and in all the files of the fontinst distribution) that may seem a
bit obscure at first blush: the uppercase letters are defined not by a simple \setslot{A}
command but by \setslot{\uc{A}{a&#125;&#125;. Likewise, the lowercase letters are defined by
\setslot{\lc{A}{a&#125;&#125;. What is the point of this complexity?
To understand it, consider the file t1c.etx, which describes the font encoding for the
small capitals. In this file, we read:
\setcommand\lc#1#2{#1small}
\setcommand\uc#1#2{#1}
In other words, the glyph names of the lowercase letters are formed by the first argument
of the command \lc{A}{a}, followed by the string small. Thus, instead of a, we find
Asmall. Thus we can reuse the code in the t1.etx file by simply adapting this convention
of Adobe for naming glyphs, which affects the names of the small capitals.
Other tricks of this kind are used for ligatures, old-style figures, etc.
```

```text
Customizing TEX Fonts for the User’s Needs
What do we find right now in the MTX file latin.mtx? Since it consists of programming,
the authors of this file (Alan Jeffrey and Ulrik Vieth) first define a number of commands
that will be useful to them later in the file. For example, they define \unfakable, in the
following manner:
\setcommand\unfakable#1{
\setglyph{#1}
\glyphrule{500}{500}
\glyphwarning{missing glyph `#1'}
\endsetglyph
}
The idea is that the glyph in question cannot be simulated or replaced by any other
glyph.21 Thus we shall later encounter
\unfakable{A}
which means that if the font does not contain the letter ‘A’, the glyph in question will be
replaced by a square 500 units long on each side (the units here are the units of PostScript
fonts, thus thousandths of an em). Moreover, a PostScript error message will be issued
when the PostScript code is displayed or printed.
What else is there in the file latin.mtx? Well, we find, for example, the description of
the glyph ‘É’:
\setglyph{Eacute}
\topaccent{E}{acute}{500}
\endsetglyph
The \topaccent command is defined in the same file. The number 500 indicates that
the accent must be centered relative to the middle of the base glyph’s set-width. Thus it
is an ad hoc command written specially for the needs of this glyph encoding. Here is its
definition:
\setcommand\topaccent#1#2#3{
\push
21 Let us note here, by way of an anecdote, that unfakability is an entirely relative concept. For instance,
in some fonts sold in France by a company that shall go unnamed, the Icelandic glyph thorn (þ) was replaced
by ‘pb’, i.e., a ‘p’ and a ‘b’ superimposed! If it were not for the legendary sangfroid of the Scandinavian peoples,
this construction could have driven Icelandic readers to the point of suicide. . .
```

Chapter 9 : Fonts in TEX and Ω, their installation and use
\moveup{\max{0}{\sub{\height{#1&#125;&#125;{\int{xheight&#125;&#125;&#125;&#125;
\movert{\add{\sub{\scale{\width{#1&#125;&#125;{#3&#125;&#125;{\scale{\width{#2&#125;&#125;{500&#125;&#125;}
{\scale{\sub{\height{#1&#125;&#125;{\int{xheight&#125;&#125;}{\int{italicslant&#125;&#125;&#125;&#125;
\glyph{#2}{1000}
\pop
\glyph{#1}{1000}
}
Here is an explanation of the code:
• We store the current point by means of a \push operation.
• We move the accent upward. This is necessary because in TEX the glyphs for the accents have
a height that is ideal for the lowercase letters. For the uppercase letters, therefore, the accent
must be moved upward a distance equal to the difference in height between the uppercase
and lowercase letters: \sub{\int{capheight&#125;&#125;{\int{xheight&#125;&#125;. Here the authors wanted to
write an all-purpose \topaccent macro that will work with all glyphs. Accordingly, they chose
a different approach (not necessarily an optimal one): they used not the standard height of the
capitals but the height of the current glyph: \sub{\height{#1&#125;&#125;{\int{xheight&#125;&#125;. This means
that the acute accent of the ‘Ó’ will be slightly higher than that of the ‘É’, since the ‘O’ is larger
than the ‘E’. That is the price to pay for a macro that will work in all situations.
One last detail: it may happen that, for one reason or another, the height of the current letter
will be less than that of the lowercase letters—for example, if the user decided to place a circumflex accent over a comma (ˆ,). In this case, the accent must not descend below the level of
the lowercase letters; in other words, its displacement may not be negative. Thus we choose
maximum of the calculated quantity and 0.
• We move the accent rightward. If G is the base glyph’s set-width and A is the set-width of the
accent, we move the accent by G
2 −A
2 , which causes us to center it relative to the middle of
the glyph’s set-width. Next, if s is the slope (in the TEX sense) of the font, we multiply s by
the difference between the height of the glyph and the height of the lowercase letters. That is
necessary because the accent in the slanted font is designed in such a way as to take the slant
into account, but only for the lowercase letters. By multiplying s by the difference in height, we
obtain the amount of extra slant required, which will cause the accent to be centered correctly
over the letter’s (slanted) central axis. Finally, we take the sum of the two, which gives us the
horizontal displacement of the accent.
• We insert the glyph for the accent.
• We pop the position at which we were before this insertion.
• We insert the base glyph.
Despite its sophistication, the code above is not optimal. It uses the principle that the setwidths of the glyphs are all the information that we need to make effective combinations
of glyphs. That is true if the glyphs have symmetric side spacing, i.e., if their contours are
centered in the abstract boxes that contain them; in that case, we can use their widths.
But it is not true if the glyph has more spacing on one side than on the other.
In the latter case, it is much more effective to use the glyphs’ bounding boxes. At the end
of the day, when we know the exact dimensions of a glyph’s contour, no matter how it
may be placed in its abstract box, we can always center it with respect to another glyph.

```text
Customizing TEX Fonts for the User’s Needs
Why, then, is fontinst based on set-widths rather than on bounding boxes? Because
the concept of bounding box is peculiar to TEX. The TEX font-metric files, be they real
(TFM/OFM) or virtual (VF/OVF), do not contain bounding boxes. There is no way to
know where the glyph is positioned in the abstract boxes given in these files. The fonts
created by METAFONT do not contain this information. Thus fontinst cannot guarantee
that the information will exist; it prefers to use values, such as set-width, that will be
found in all font files.
Although fontinst has been around for more than 10 years, only in a recent version (1.926,
the current one being 1.928) supports making calculations on the basis of bounding
boxes—by loading the file bbox.sty. One must insert the following commands:
\needsfontinstversion{1.926}
\input{bbox.sty}
at the beginning of the font’s installation file in order to ensure that the macros in question will be available.
Later in this book, we shall come back to the different types of combinations of glyphs
that are possible.
One last word on the latin.mtx file. It contains macros of the following type:
\setleftkerning{IJ}{I}{1000}
\setleftrightkerning{Iacute}{I}{1000}
\setleftrightkerning{Icircumflex}{I}{1000}
\setleftrightkerning{Idieresis}{I}{1000}
\setleftrightkerning{Idotaccent}{I}{1000}
\setleftrightkerning{Igrave}{I}{1000}
\setrightkerning{IJ}{J}{1000}
to create kerning between “nonstandard” glyphs. Thus the number of kerning pairs in
a font is often multiplied by six: for each pair ‘AT’, there will also be the pairs ‘ÁT’, ‘A¸T’,
‘Á¸T’, and so forth.
In the text to follow, we shall examine different scenarios for building up particular
glyphs from components. These scenarios will allow us to illustrate both the variety of
typographical needs of the different scripts with regard to combining glyphs and the advanced techniques offered by fontinst.
Adding ligatures to a font
A “mademoiselle” for the font Zapfino
Suppose that we wish to adapt the delightful font Zapfino (a creation of a great master
who shall go nameless here) for use with TEX—or rather with Ω, since the latter supports
```

Chapter 9 : Fonts in TEX and Ω, their installation and use far more than 256 glyphs. One step in the process of adaptation will be to write the code for the ligatures. Thanks to this code, some strings in the input will automatically produce ligatures. Being a great patriot and defender of la francophonie, I have chosen, from the multitude of ligatures provided in Zapfino, one that is as French as can be: ‘t’ (for “mademoiselle”, the French equivalent of the title “Miss”), from which I have removed the period that Zapf unfortunately added. How can we obtain a ligature automatically from the string Mlle? The reason that we chose this example (rather than the bland ‘fi’ ligature) is that there is a catch. Specifically, in TEX, unlike in OpenType or AAT, we cannot define ligatures of more than two glyphs at a time. Thus, to produce the four-glyph ligature ‘t’, we will have to have positions in the font’s table for each of the intermediate ligatures: ‘u’, ‘uv’, and ‘uw’. Thus we shall have the following in the ETX file: \setslot{M} \ligature{LIG}{l}{M_l} \comment{Letter M} \endsetslot \setslot{M_l} \ligature{LIG}{l}{M_l_l} \comment{(False) ligature Ml} \endsetslot \setslot{M_l_l} \ligature{LIG}{l}{M_l_l_e} \comment{(False) ligature Mll} \endsetslot \setslot{M_l_l_e} \comment{Original ligature Mlle} \endsetslot We are therefore taking up four positions in the font’s table, while only two of them will actually be used. Moreover, these two positions (‘u’ and ‘t’) are the only ones that will actually appear in the font. The other two are really nothing but jury-rigging. What will appear in the MTX file? For the “real” glyphs, we will have the customary code: \setglyph{M} \glyph{M}{1000} \endsetglyph \setglyph{M_l_l_e} \glyph{M_l_l_e}{1000} \endsetglyph

```text
Customizing TEX Fonts for the User’s Needs
\setleftkerning{M_l_l_e}{M}{1000}
\setrightkerning{M_l_l_e}{e}{1000}
We shall obtain the others by simply concatenating glyphs (taking their possible kerning
into account):
\setglyph{M_l}
\glyph{M}{1000}
\movert{\kerning{M}{l&#125;&#125;
\glyph{l}{1000}
\endsetglyph
\setleftkerning{M_l}{M}{1000}
\setrightkerning{M_l}{l}{1000}
\setglyph{M_l_l}
\glyph{M}{1000}
\movert{\kerning{M}{l_l&#125;&#125;
\glyph{l_l}{1000}
\endsetglyph
\setleftkerning{M_l_l}{M}{1000}
\setrightkerning{M_l_l}{l_l}{1000}
In the second case above, we are using not a string of three glyphs but a glyph ‘M’ and
a ligature ‘ll’, since the ligature does exist in Zapfino and it would be a shame not to use
it. Thus when we type an ‘M’ followed by an ‘l’, we shall obtain the ligature ‘Ml’, which
we shall never see, as the glyph for this ligature is identical in every way to the glyphs
‘M’ and ‘l’ in sequence. The same is true of ‘Mll’. Only when the ‘e’, the fourth character
of ‘Mlle’, is read will the combined ligature become visible.
What will happen when the DVI file produced by TEX (or Ω) is converted to PostScript
and then to PDF? Will the intermediate “false ligatures” of our approach create any
problems? Not at all. Do not forget that dvips will first “devirtualize” the DVI code before converting it to PostScript. For the positions in the virtual font that represent true
ligatures, a PostScript glyph will be inserted. This glyph, in the Zapfino font, will have a
name formed from Adobe’s rules for naming glyphs (Appendix C.3.3). Acrobat will thus
recognize this glyph as being equivalent (with respect to indexing, selection, searching,
etc.) to the corresponding string: the glyph M_l_l_e corresponds to the string Mlle.
As for the false ligatures, they will be replaced by the corresponding DVI code during
devirtualization. For example, M_l will be replaced by the glyphs M and l, and M_l_l will
be replaced by the pair of glyphs M and l_l, the second of these being a true ligature,
equivalent to the string ll. Thus all is well, in the best of worlds.
```

```text
Chapter 9 : Fonts in TEX and Ω, their installation and use
Contextual analysis in Arabic
Another example of the use of ligatures: the contextual analysis of the Arabic script. For
simplicity’s sake, we shall assume that there are only two letters: one with two forms,
and one with four forms. To assist the reader who does not read Arabic, we shall take
two letters whose forms are quite different from one another: ghayn (isolated, J; initial,
K; medial, L; final, M) and dal (isolated, ; final, N). Thus the four two-letter words that
we can write are J and  (letters not connected), NK and MK (letters connected). The
three-letter words with all the letters joined up are MLK and NLK. And so forth.
Ordinarily the glyphs that we are going to discuss are called afii57434 for ghayn and
afii57423; but since these names will not necessarily help the reader to understand the
example, we shall instead use the names ghayn and dal. The glyphs at our disposal are
therefore ghayn.isol, ghayn.init, ghayn.medi, ghayn.fina, dal.isol, and dal.fina.
Unlike the representative glyph in Unicode, which is in the isolated form, the default
glyph in TEX that will represent an Arabic character in our font is in the medial form,
if it has four forms, or the final form, if it has only two. Therefore, by default, when we
ask TEX to set a ghayn or a dal, it will set a L (ghayn.medi) or a N (dal.fina). Now we must
write the ligatures that will produce the other contextual forms.
First, let us deal with the beginning of the word. We want L and N to become K and
, respectively, in that position. But what is the beginning of a word? That question is
anything but trivial. In fact, we must enumerate all the glyphs that may appear before
either ghayn or dal. The opening parenthesis (parenright) is one such glyph. Therefore
we shall write, in the definition of this glyph, in the ETX file:
\setslot{parenright}
\ligature{/LIG}{ghayn.medi}{ghayn.init}
\ligature{/LIG}{dal.fina}{dal.isol}
\endsetslot
The slash before the keyword LIG means that we are keeping the preceding glyph and
that the new glyph obtained will replace the second glyph; thus we keep the parenthesis
and replace one Arabic letter with another. That solves the problem of ‘L)’ and ‘N)”, which
become ‘K)’ and ‘)’, respectively.
Nonetheless, most of the time it is a space that will appear at the beginning of a word.
And we find ourselves once again faced with the peculiarity of TEX that the “space” is
not a glyph but merely an offset. How can we specify the behavior of a glyph when it is
preceded by an offset, be it horizontal (within a line) or vertical (at the beginning of a
line)? TEX uses the following trick: A position in the table is declared to be the “left-hand
delimiter” of words. At the beginning of a word (preceded by a space), TEX will act as if
this special glyph were present. Thus we can assign it to ligatures or to kerning pairs. In
fontinst, we use a special command, \setleftboundary, in the following manner:
\setleftboundary{percent}
\ligature{/LIG}{ghayn.medi}{ghayn.init}
```

```text
Customizing TEX Fonts for the User’s Needs
\ligature{/LIG}{dal.fina}{dal.isol}
\endsetslot
Above we have used the glyph ‘%’ as the left-hand delimiter. That does not affect the
actual glyph ‘%’ at all. All kerning pairs, however, with the percent sign as their first letter
will also be applied at the beginnings of words, as if an invisible ‘%’ were present at those
locations. We should choose as the left-hand delimiter a glyph that does not have any
kerning pairs, so as not to confuse the kerning pairs of the “real glyph” with those of its
alter ego, the pseudoglyph for the left-hand delimiter.
There is one other case in which we would like to change from a medial form to an initial
form: this is when the glyph is preceded by a dal. Indeed, this letter has only two forms:
isolated and initial. When it is followed by another Arabic letter, the latter behaves as if
it were at the beginning of a word. Thus we must also supply the ligatures engendered
by dal.isol or dal.fina:
\setslot{dal.fina}
\ligature{/LIG}{ghayn.medi}{ghayn.init}
\ligature{/LIG}{dal.fina}{dal.isol}
\endsetslot
\setslot{dal.isol}
\ligature{/LIG}{ghayn.medi}{ghayn.init}
\ligature{/LIG}{dal.fina}{dal.isol}
\endsetslot
Now let us take care of the end of the word. When a word ends with dal, we already have
a final (or isolated) form; thus the contextual analysis is already finished. But when a
word ends with a medial ghayn, that letter must change to its final form. When it is in
the initial form, it must assume its isolated form instead.
Once again we shall start by writing all the explicit ligatures with punctuation marks
and other glyphs that may follow a word, and then we shall declare that one glyph will
play the role of an “end-of-word space”: this will be the right-hand delimiter. We define
the right-hand delimiter with the \setrightboundary command, which has no ending
command \endsetrightboundary, since the pseudoglyph in question is not supposed to
form ligatures with other glyphs that follow it; it exists only to serve as the second term
in ligatures with real glyphs.
Thus we write:
\setrightboundary{percent}
The percent sign thus serves two purposes: it is the left-hand and the right-hand delimiter.
The entry for medial ghayn might thus be:
```

Chapter 9 : Fonts in TEX and Ω, their installation and use
\setslot{ghayn.medi}
\ligature{LIG/}{percent}{ghayn.fina}
\ligature{LIG/}{period}{ghayn.fina}
\ligature{LIG/}{comma}{ghayn.fina}
\ligature{LIG/}{parenleft}{ghayn.fina}
... and so on for all the punctuation marks ...
\endsetslot
The slash that follows the keyword LIG indicates that the second term in the ligature
will remain unchanged. Thus if medial ghayn is followed by a period, the first term, the
medial ghayn, is replaced by a final ghayn, while the period remains where it is. In the
absence of this mechanism, we would be required to have positions in the font table
containing final ghayn followed by different punctuation marks. That would cause the
number of glyphs in the font to explode.
Note that in the code above, by writing percent, we obtain a final glyph both before a
space at the end of a word or the end of a line (since percent is the right-hand delimiter)
and before an actual ‘%’ sign. For TEX, it is impossible to distinguish the two. Thus we
should choose as our delimiter a glyph that we use rarely, or even never.
To conclude, here is the declaration for initial ghayn:
\setslot{ghayn.init}
\ligature{LIG/}{percent}{ghayn.isol}
\ligature{LIG/}{period}{ghayn.isol}
\ligature{LIG/}{comma}{ghayn.isol}
\ligature{LIG/}{parenleft}{ghayn.isol}
... and so on for all the punctuation marks ...
\endsetslot
Thus, for example, when we write the string “space”, “ghayn”, “space”, we obtain a medial ghayn, which becomes an initial ghayn under the action of the left-hand delimiter;
then the initial ghayn will form an isolated ghayn with the right-hand delimiter, and we
are done.
In this section, we have described a simplified version of the contextual analysis of the
Arabic script. There are advantages and disadvantages to this method:
• advantages. Contextual analysis is done automatically. Provided that she can set
type from right to left (for which she needs either Ω or eTEX), the user has nothing to
do but to enter the codes for the Arabic characters, and the rest will be done by the
font. Analysis does not involve any macros, so it can be performed in any context: in
a table, within a mathematical formula, in verbatim mode, etc. This independence
from the context of the font’s behavior corresponds closely to the fundamentally natural character of contextual analysis in the Arabic script. This approach is completely
compatible with conversion to PDF; the glyph ghayn.isol, for example, will be represented by a PostScript glyph of the same name, and Acrobat will able to determine
very easily which Unicode character it represents.

Customizing TEX Fonts for the User’s Needs
• disadvantages. Contextual analysis is very fragile: even the empty group {} can
break it. It would be very difficult to insert vowel points or other diacritical marks
between the letters. We must explicitly list glyphs that are not Arabic letters and that
will cause a medial glyph to become initial or final (and will cause an initial glyph
to become isolated); theoretically, all non-Arabic Unicode characters fall into this
case, which means that we have thousands of glyphs, thus hundreds of thousands,
even millions, of ligatures. Of course, we shall only write the relevant ligatures (the
case of an ideograph immediately followed by an Arabic letter, for example, can be
easily excluded... ), but that entails a degree of uncertainty in the analysis; the day
when that rare case does occur, the user will have to be able to notice it rapidly and to
correct the problem by using glyphs representing the Unicode characters ZWJ and
ZWNJ.22
Keeping ‘f’ from running into ‘è’
Last but not least, an example drawn from the French version of this book. The reader
may have noticed that the letter ‘f’ becomes ‘¦’ when it appears before an ‘è’, a ‘ü’, or any
other letter that bears an accent that inconveniently gets in the way. A humble intervention on our part has prevented the ‘fè’ effect that would ordinarily be obtained with this
font, in a word like Italian “caF¦è”.
All that we had to do was to design a new glyph ‘¦ ’ whose upper portion is narrower,
place it into an auxiliary font (the license for our installation does not allow us to modify the original font), and create a number of ligatures of LIG/ type: ‘¦ ’ + ‘è’ →‘¦è’, etc.
When we use an “intelligent” ligature, the ‘f’ is replaced with an ‘¦’, and the second letter
remains unchanged. Suppose that the new letter is named f.narrow. Then the fontinst
code could be:
\setslot{f}
\ligature{LIG/}{egrave}{f.narrow}
\ligature{LIG/}{ecircumflex}{f.narrow}
\ligature{LIG/}{edieresis}{f.narrow}
... and similarly for all other accented
letters that cause a problem ...
\endsetslot
That approach saves us the trouble of defining new positions in the font’s table for each
pair ‘¦è’, ‘¦ê’, ‘¦ë’, etc. The same procedure was needed for the ‘ff’ ligature, which became ‘F¦ ’.
The problem of the pair of letters ‘¦è’ is not new. It unfortunately occurs in a great many
fonts of high quality. Yet it can be resolved in a trice, with nothing more than a narrower
head on the ‘f ’ and a line of fontinst code.
22 These are empty zero-width glyphs that play either the role of an Arabic letter with four forms or the
role of a non-Arabic letter. Since they have zero width, these glyphs allow us to force Arabic letters to assume
a certain form.

```text
Chapter 9 : Fonts in TEX and Ω, their installation and use
Placing a diacritical mark
In the section “ETX and MTX Files for a Simple Virtual Font” (page 292), we considered
the case of placing a single diacritical mark—an accent centered over a letter. For this
purpose, we used the set-widths of the accent and the letter, in the hope that these glyphs
were indeed centered in their abstract boxes so that the centering of the set-widths would
be equivalent to the centering of the contours.
Now we shall write the same code23 by using the bounding boxes of the glyphs:
\setglyph{Eacute}
\topbbaccent{E}{acute}
\endsetglyph
\def\bbcenter#1{\add{\half{\sub{\bbright{#1&#125;&#125;{\bbleft{#1&#125;&#125;&#125;&#125;{%
\bbleft{#1&#125;&#125;}
\setcommand\topbbaccent#1#2{
\push
\moveup{\max{0}{\sub{\bbtop{#1&#125;&#125;{\int{xheight&#125;&#125;&#125;&#125;
\movert{\add{\sub{\bbcenter{#1&#125;&#125;{\bbcenter{#2&#125;&#125;}
{\scale{\sub{\bbtop{#1&#125;&#125;{\int{xheight&#125;&#125;}{\int{italicslant&#125;&#125;&#125;&#125;
\glyph{#2}{1000}
\pop
\glyph{#1}{1000}
}
The \bbcenter command yields the horizontal center of the bounding box: it is
computed as half of (\bbright minus \bbleft) plus the spacing on the left (which is
\bbleft). Next, in the code for \topbbaccent, we merely replace \scale{\width{#1&#125;&#125;{
500} with \bbcenter{#1} and replace \height with \bbtop (which is, strictly speaking,
the same thing, since the only information about height that we find in an AFM file is
the height of the bounding box).
Making an ‘h’ believe that it is an ‘l’
Kaj nun, ankora˘u pli interesa ekzemplo: la litero ‘h’ uzata en Esperanto, lingvo tiel idealisma kaj ˆcarma en sia strangeco. (Now for a more interesting example: the letter ‘h’ used
23 For simplicity’s sake, we shall assume that the accent is centered; thus it lacks the third parameter of
\topaccent, which we shall assume to have the value of 500.
```

```text
Customizing TEX Fonts for the User’s Needs
in Esperanto,24 a language so idealistic and charming in its awkwardness.) It is obvious
that centering the accent (like this: ‘ˆh’) would yield a horribly ugly result. Therefore, we
need a way to center the accent above the downstroke of the ‘h’. In the absence of an
OpenType accent indicator or a shape-recognition system to detect the downstroke, we
must resort to a trick to achieve our goal.
Here it is: in the overwhelming majority of fonts, the downstroke of the ‘h’ is a perfect
copy of the letter ‘l’, and the amount of spacing on the left of these two letters is the same.
Thus we have only to place the accent over the ‘h’ as if it were an ‘l’:
\setglyph{hcircumflex}
\topbbaccentlikeif{h}{circumflex}{l}
\endsetglyph
\def\bbcenter#1{\add{\half{\sub{\bbright{#1&#125;&#125;{%
\bbleft{#1&#125;&#125;&#125;&#125;{\bbleft{#1&#125;&#125;}
\setcommand\topbbaccentlikeif#1#2#3{
\push
\moveup{\max{0}{\sub{\bbtop{#1&#125;&#125;{\int{xheight&#125;&#125;&#125;&#125;
\movert{\add{\sub{\bbcenter{#3&#125;&#125;{\bbcenter{#2&#125;&#125;}
{\scale{\sub{\bbtop{#1&#125;&#125;{\int{xheight&#125;&#125;}{\int{italicslant&#125;&#125;&#125;&#125;
\glyph{#2}{1000}
\pop
\glyph{#1}{1000}
}
The code has hardly changed. We have defined a command \topbbaccentlikeif (or
“accent appearing above a letter, calculated on the basis of bounding boxes and placed
as if the letter were a different letter”), which takes three arguments: the base letter (‘h’),
the accent (the circumflex), and the letter that will serve as a reference for placing the
accent (‘l’).
The same thing, but on the other side
To go a step further, we shall now leave the Latin alphabet and dive into the mysterious
Old Cyrillic (or “Slavonic”) script, used for liturgical documents in the countries that
24 Invented by Ludwig Lazare Zamenhof, a nineteenth-century idealist, Esperanto purports to be a universal language, but in reality it is completely Eurocentric, as it merely mixes elements of the various Romance
and Germanic languages. Its main use was as a pivot language during the Cold War: since the West was hesitant
to learn Russian or Chinese and the Eastern Bloc was equally hesitant to learn English or French, Esperanto
served as a common language for communication between people from the two rival blocs.
```

```text
Chapter 9 : Fonts in TEX and Ω, their installation and use
use the Cyrillic script. This alphabet includes a letter named yus: ‘k’ (Unicode 0x0467
cyrillic small letter little yus). Like all the vowels in this alphabet, yus can bear
accents (the accents of the Greek language, carry-overs from the Greek cultural heritage).
Here it bears an acute accent: ‘m’. Up to now, there has been nothing out of the ordinary,
typographically speaking.
A phonetic variant of yus is written with a preceding small capital ‘i’: ‘i’ (0x0469 cyrillic
small letter iotified little yus). This letter can also bear an accent, and in this case
the accent is not centered but rather placed over the yus: ‘l’. Once again, therefore, we
must place an accent by making reference to another letter, but in this case the other
letter appears on the right-hand side of the construct. Here is the code that will position
the accent correctly for us:
\setglyph{uni0469_acute}
% uni0467 is the yus
% uni0469 is the yus preceded by an i
\topbbaccentlikeifreverse{uni0469}{acute}{uni0467}
\endsetglyph
\def\bbcenter#1{\add{\half{\sub{\bbright{#1&#125;&#125;{%
\bbleft{#1&#125;&#125;&#125;&#125;{\bbleft{#1&#125;&#125;}
\setcommand\topbbaccentlikeifreverse#1#2#3{
\push
\moveup{\max{0}{\sub{\bbtop{#1&#125;&#125;{\int{xheight&#125;&#125;&#125;&#125;
\movert{\bbright{#1&#125;&#125;
\movert{\add{\neg{\sub{\bbcenter{#3&#125;&#125;{\bbcenter{#2&#125;&#125;&#125;&#125;
{\scale{\sub{\bbtop{#1&#125;&#125;{\int{xheight&#125;&#125;}{\int{italicslant&#125;&#125;&#125;&#125;
\glyph{#2}{1000}
\pop
\glyph{#1}{1000}
}
The code is hardly more complex than the preceding example; there are only a few differences. First, the name of the macro is perfectly hideous (\topbbaccentlikeifreverse).
Second, we have added the line \movert{\bbright{#1&#125;&#125;, which moves to the rightmost
extremity of the glyph. Finally, the alignment of the base glyph and the accent is performed from right to left; thus we have inserted a \neg into the code, to force movement
towards the left.
```

```text
Customizing TEX Fonts for the User’s Needs
Making a letter forget that it has a horn
But letters are not the only characters that are replaced with (more respectable) letters.
The same phenomenon occurs with accents, and sometimes with a letter and an accent at
the same time. Let us return to the Latin alphabet, but not just any Latin alphabet! This
example will delight those who love accent marks, the ne plus ultra of the ravages of colonialism: the Vietnamese alphabet. In this alphabet, there is—among other things—a
combination of the circumflex and acute accents ‘p’ and also the letter ‘o’ with a horn: ‘q’.
To place the double accent over a letter, we shall center not the entire glyph, but only
the part that constitutes the circumflex accent, over the letter. In the same vein, to place
an accent over the letter ‘q’, we shall center it not with respect to the set-width of the
entire glyph but only with respect to the part corresponding to an unadorned ‘o’. Here
is this special letter with the special double accent: ‘r’. To obtain it, we shall write a TEX
command that will center an accent A over a letter L by acting as if it were a different
accent, A′:
\setglyph{oxxx_circumflex_acute}
\topbbaccentlikeiflikeif{oxxx}{o}{circumflex_acute}{circumflex}
\endsetglyph
\def\bbcenter#1{\add{\half{\sub{\bbright{#1&#125;&#125;{%
\bbleft{#1&#125;&#125;&#125;&#125;{\bbleft{#1&#125;&#125;}
\setcommand\topbbaccentlikeiflikeif#1#2#3#4{
\push
\moveup{\max{0}{\sub{\bbtop{#2&#125;&#125;{\int{xheight&#125;&#125;&#125;&#125;
\movert{\add{\sub{\bbcenter{#4&#125;&#125;{\bbcenter{#2&#125;&#125;}
{\scale{\sub{\bbtop{#2&#125;&#125;{\int{xheight&#125;&#125;}{\int{italicslant&#125;&#125;&#125;&#125;
\glyph{#3}{1000}
\pop
\glyph{#1}{1000}
}
Putting breathing marks in the margin
Finally, one more interesting example that is nonetheless too often spurned by incompetent Greek typesetters: when an uppercase Greek vowel appears at the beginning of a
paragraph or a line of verse, the breathing mark and any accent that it bears are set in
the margin:
```

Chapter 9 : Fonts in TEX and Ω, their installation and use
Note that in the case of the letters alpha and omicron, we are also required to kern the
breathing mark and the letter.
Two ways to achieve this behavior come to mind:
• Either we create a zero-width glyph containing nothing but the breathing mark (or
the breathing mark together with the accent) and write a kerning pair for this breathing mark and the letter.
• Or we create glyphs that are combinations of breathing marks and letters, with the
breathing mark appearing outside the glyph’s abstract box.
We shall give examples of code for these two cases and show why the first case ultimately
cannot be made to work.
First, let us assume that we have a glyph named rough (the rough breathing, or spiritus
asper) and that we wish to obtain a rough.zerowidth (zero-width rough breathing). Here
is a fragment of code for this purpose:
\setglyph{rough.zerowidth}
\push
\movert{\neg{\width{rough&#125;&#125;}
\glyph{rough}{1000}
\pop
\endsetglyph
Thanks to \push and \pop, we can achieve a zero width. By first moving towards the left
a distance equal to the set-width of the “normal” rough breathing, we obtain a glyph
placed entirely outside and to the left of its abstract box.
Everything is fine up to this point: we place the glyph in front of a capital epsilon, and it
is indeed set in the margin. Now we have only to solve the problem of kerning between
the breathing mark and the uppercase letter alpha or epsilon that follows. And there we
discover the snag in our approach: if we kern the breathing and the letter, the distance between the two glyphs becomes aesthetically acceptable, but the letter is no longer where
it should be.
The very purpose of this maneuver is to align the uppercase vowels. Thus we should
move the breathing mark closer to the letter not by moving the letter to the left but
rather by moving the breathing mark to the right and leaving the letter right where it

```text
Customizing TEX Fonts for the User’s Needs
is. Unfortunately, TEX has made no provision for this procedure: in a kerning pair, it is
always the second term that is moved, never the first.
Thus this is the reason for which our first attempt has failed: it is impossible to perform
kerning without moving the letter, and that is just what we wished to avoid.
Now let us attempt to define a glyph Alpha_rough.bp (“bp” for “beginning of paragraph”), which will incorporate a rough breathing and a capital alpha, with the breathing
moved out into the margin but at the proper distance from the letter:
\setglyph{Alpha_rough.bp}
\push
\movert{\neg{\width{rough&#125;&#125;}
\movert{\neg{\kerning{rough}{Alpha&#125;&#125;}
\glyph{rough}{1000}
\pop
\glyph{Alpha}{1000}
\endsetglyph
This time we have succeeded: we set up a \push and \pop pair, we move the breathing to
the left so that it will be to the left of the box, and then we move it to the right a distance
equal to the kerning between the breathing and the letter. Since this kerning ordinarily
operates to the left (backward motion), we use the \neg command to achieve motion to
the right. After making all these moves, we set the glyph for the breathing. We restore
the current point to what it was before the \push/\pop (i.e., the original coordinates), we
set the letter alpha, and voilà!
Keeping accented capitals from taking up too much vertical space
To conclude this series of examples of the placement of diacritical marks, here are two
more that may prove to be singularly important for the typesetting of the several European languages, especially when fonts designed outside Europe are used.
Let us start with a very simple case. We know that the capital letters in most Europeanlanguages should be written with their accents. But when the heights of the letters are
uneven, the accents over the letters can often modify the leading. That problem results
from the fact that TEX adds extra space to lines that contain slightly taller glyphs, which
may occur if we write accents over our capitals. To prevent this problem, we can use the
\smash macro, which “smashes” a glyph’s abstract box and treats the glyph as if it were
of zero height. But this solution is neither elegant nor compatible with the very delicate
properties of kerning and hyphenation. A more elegant solution is therefore needed,
and here it is: we can force the abstract boxes of the accented capitals to have the same
dimensions as those of the letters without accents. Here is an example:
```

```text
Chapter 9 : Fonts in TEX and Ω, their installation and use
\setglyph{Eacute}
\topaccent{E}{acute}{500}
\resetheight{\height{E&#125;&#125;
\endsetglyph
Building Europe while showing respect for cultural differences
Our last example illustrates a problem that has always poisoned Franco-German relations. No, we are not referring to Alsace-Lorraine, nor to the deportation of Daniel CohnBendit in May 1968, but to the difference in the height of the diaeresis. Germans, in fact,
place their umlaut quite low, so that it is almost attached to the letter that bears it, and
in any event lower than the dot on the ‘i’. For example, the font Transitional 521, by
Bitstream, is very well adapted to German, as the dot on its ‘i’ is at the height of 609 units
whereas the umlaut is at 529. A difference of 80 units is a fifth of the height of the lowercase letters, hardly a negligible amount.
The German way The French way
The French, on the other hand, tend to place the diaeresis at the same height as the dot
on the ‘i’. Here is how to rectify the situation. Instead of writing:
\setglyph{udieresis}
\topaccent{u}{dieresis}{500}
\endsetglyph
we shall write:
\setglyph{udieresis}
\frenchdieresis{u}
\endsetglyph
with \frenchdieresis defined in the following manner:
\setcommand\frenchdieresis#1{
\push
\moveup{\neg{\height{dieresis&#125;&#125;}
\moveup{\height{i&#125;&#125;
```

```text
Customizing TEX Fonts for the User’s Needs
Figure 9-10: The utility LTR Bleifrei LayerPlayer of Letterror.
\movert{\add{\sub{\scale{\width{#1&#125;&#125;{500&#125;&#125;{%
\scale{\width{dieresis&#125;&#125;{500&#125;&#125;}
{\scale{\sub{\height{#1&#125;&#125;{\int{xheight&#125;&#125;}{\int{italicslant&#125;&#125;&#125;&#125;
\glyph{dieresis}{1000}
\pop
\glyph{#1}{1000}
}
The only difference between that command and the usual \topaccent command is that
we first move down by a depth equal to the height of the font’s diaeresis; next, we move
up to a height equal to that of the ‘i’. When we set the diaeresis, therefore, it has exactly
the same height as the dot on the ‘i’. Note that this procedure is not necessary for the font
in which this book has been typeset, for the very simple reason that that font comes from
France, having been designed by our dear beloved Jean François Porchez and being used
in the “newspaper of reference” known as Le Monde.
Setting lead type with TEX
To conclude this chapter on TEX and fonts with a flourish, let us see a simple example that
is as dramatic as it is instructive. In 2001 the Dutch foundry Letterror of Just van Rossum
and Erik van Blokland issued a font named Bodoni Bleifrei [338]. The adjective bleifrei
means “lead-free” in German. The font is a reproduction of a 48-point roman by Bodoni
that manages to give the appearance of a series of type sorts arranged on a composing
stick.
A utility by the name of LTR Bleifrei LayerPlayer (for Mac OS 9 only), which is shown
in Figure 9-10, allows one to enter text in this font and select colors to produce special
effects. We enter a few words in this utility’s window and save the result in EPS format;
then it can be used in any vector-based image software.
```

```text
Chapter 9 : Fonts in TEX and Ω, their installation and use
But how does it work? In fact, there are three superimposed fonts. These three fonts
can be of different colors, for producing special effects. The first font, Bodoni BleifreiImprint, reproduces the impressions of the type—i.e., the glyphs as they are usually seen.
In the example shown in Figure 9-10, we have selected the Chrome configuration; in it,
the Bleifrei-Imprint font appears in white.
Let us take another example and separate the layers. Here is the first layer (in which we
have made the background gray in order to make the white text visible):
The second layer, called Bodoni Bleifrei-Leaded, is used in black. It represents the printable
surface of the type, the edges of which have been blackened to give the impression of
depth:
Finally, the third layer, called Bodoni Bleifrei-Slugs, consists of boxes that establish the
background color:
In the example, this color is a very pretty purple, its CMYK parameters being 42, 42,
19, 10. And here are the three layers put together:
It is entirely possible to obtain the same result in TEX. Virtual fonts will allow us to use
a single font that will produce the three layers, with any colors that we wish.
Let BodonBleImp.afm, BodonBleLea.afm, and BodonBleSlu.afm be the names of the AFM
files associated with the three base fonts. A glyph in our virtual font will combine the
corresponding glyphs from these three fonts. For example, the F of the virtual font will
superimpose the F of BodonBleImp.afm with the F of BodonBleLea.afm and that of BodonBleSlu.afm.
The first hurdle: if we wish to refer to these three letters F in a single fontinst glyph definition, they must have different names.
```

```text
Customizing TEX Fonts for the User’s Needs
Thus we must rename the glyphs in at least two of these fonts. Does that mean that we
have to open the PostScript code for the font and edit it? Not at all; in any event, our
user’s license for the font forbids us to do so. We shall simply create new AFM files, since
fontinst can read only AFM.
A little Perl script something like
open IN, "BodonBleLea.afm";
open OUT, ">nouveaux/BodonBleLea.afm";
while (&lt;IN&gt;) {
s/;[ \t]*N ([A-Za-z0-]+)[ \t]*;/; \1.lead ;/;
print OUT;
}
close OUT; close IN;
will append the suffix .lead to all the glyphs in BodonBleLea.afm. We do likewise for
BodonBleSlu (with the suffix .slug). Now we have three fonts whose glyphs have distinct
names.
The second hurdle: we wish to change the color of a glyph, and we know that we can use
the fontinst command \glyphspecial, but what is the corresponding PostScript code?25
There is no need to reinvent the wheel. It is sufficient to create a little TEX in which we
change the color of a word and then read the DVI file to see which blocks of PostScript
code are inserted. We can use the specifications of the color purple that we wish to obtain.
Thus, by writing
\textcolor[cmyk]{.42,.42,.19,.10}{blabla}
we obtain a DVI file in which we find the following lines. (We have converted the DVI
code to DVR so as to make it readable to a human.)
XXX "color push cmyk .42 .42 .19 .10"
SET blabla
XXX "color pop"
Conclusion: We need only add the PostScript code color push cmyk .42 .42 .19 .10
before the glyph and color pop after the glyph. As the names “push” and “pop” suggest,
we are pushing the color onto the stack of PostScript’s graphics state.
Here, then, is the fontinst code to obtain the letter ‘F’ in our virtual font:
\setglyph{F}
\push
\glyphspecial{color push cmyk .42 .42 .19 .10}
25 The reader who feels ill at ease with the PostScript language may consult our introduction to this language in Appendix C.1 on page 635 of this book.
```

Chapter 9 : Fonts in TEX and Ω, their installation and use \glyph{F.slug} \glyphspecial{color pop} \pop \push \glyph{F.lead} \pop \glyph{F} \endsetglyph We start with the lowest layer so that we can superimpose the other two upon it. What is incredible is that this font is perfectly ordinary to TEX, which will perform kerning, hyphenation, etc., as usual without being aware that the font exists under several layers with different colors. Conclusions and Glimpses at the Future In this chapter we have seen, without going too deeply into the details, various aspects of font management in TEX and Ω. Its apparent complexity is related to the clash of cultures that occurred between the initial philosophy of TEX (TFM metrics, on the one hand, and GF or PK bitmaps on the other) and the chaotic real world of the fonts of the past two decades. How can we get the most benefits from TEX font metrics—and from virtual fonts in particular? At the same time, how can we adapt fonts (PostScript, TrueType, OpenType, etc.) for use with TEX when they are a priori foreign to it? We have seen that most of the problems stem from the incompatibility between these two philosophies and from the fact that we cannot provide more information to TEX than what exists within the concept of a virtual font. For instance, PostScript and TrueType fonts contain the notion of a bounding box, whereas virtual fonts know nothing about it. We are therefore obliged to perform all the operations involving a bounding box (e.g., precise placement of diacritical marks) while we still have access to this information— namely, at the time that the virtual font is created by fontinst, when it has just read the AFM files and accumulated the data for the bounding boxes. After that, it will be too late: TEX will never again have access to the information. Another example, going in the opposite direction: ligatures. We have seen that when ligatures appear in PostScript fonts adapted for use with TEX, it is certainly not because they were already indicated in the AFM files. In reality, AFM usually disregard ligatures altogether. If we have ligatures at our disposal, it is because they were systematically inserted, thanks to the file latin.mtx. But what about OpenType or AAT files, which specify with great precision which ligatures should be made and under which conditions? Furthermore, it must be admitted that the mechanisms for using ligatures provided by OpenType and AAT are more powerful than those of TEX or Ω. By what convoluted means can we convert an AAT finite automaton for ligatures into a series of ligatures in a virtual font? The idea of writing a generic algorithm to convert AAT finite automata into ligatures in a virtual font could be the inspiration for a horror movie by Stephen King...

Conclusions and Glimpses at the Future Thus only one possible solution can be imagined: opening the doors to the perspective of TEX, or rather Ω (since TEX is enjoying eternal rest in the heavenly kingdom of deceased software), for those who come into direct contact with OpenType, AAT, and all the other kinds of fonts that the future holds in store for us. It is time, then, to toll the knell of TFM, VF, OFM, OVF, and other font-metric file formats that are not up to the standard of today’s fonts. The author’s research team at ENST Bretagne is working on version 2 of Ω, based on textemes [167, 168, 71]. A texteme is a data structure containing, all in one: a character, one or more glyphs, and, potentially, a set of key-value pairs called properties (Arabic form, color, hyphenation, font, Semitic root, Chinese ideographic radical and/or decomposition, language, horizontal and vertical offset of the glyph, and whatever else the user may need). The goal of textemes is to replace characters by becoming the atomic units of text, so that information which is missing from characters in the current Unicode-based model of text, can be injected at a level other than mark up. Using textemes in the Ω input document, the typesetting process becomes an accumulation of texteme properties so that Ω output contains essentially the same textemes as the input document, but with many more properties. How does Ω v2 deal with OpenType fonts? During processing by Ω, texteme string are filtered by external engines. One of these engines corresponds roughly to Uniscribe/παν語 and will segment text, apply contextual analysis for Arabic, re-order Indic glyphs, etc. Two other external engines correspond to the two basic OpenType tables GSUB and GPOS. These engines will read the font data and will apply OpenType transformations to the flow of textemes (in fact: to the glyphs contained in the textemes). This approach has the advantage that one keeps absolute control on the way the text is transformed, since one can act on the texteme flow at any moment, even after the GPOS engine or between engines. Ω v2 is still an experimental project, a heavy-duty approach to the problem of marrying the TEX principles of versatile high-level typography and the OpenType way of processing international text.
