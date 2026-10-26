---
title: "Chapter 14: Advanced Typography (OpenType and AAT)"
description: "Unabridged English text: Comprehensive architecture of modern smart font systems; OpenType Layout tables (GSUB, GPOS, GDEF, BASE, JSTF); script, language system, feature and lookup hierarchies; Microsoft VOLT vs Adobe feature syntax (AFDKO); Apple Advanced Typography (AAT) line layout, metamorphosis (morx), and finite state automata."
---

# Chapter 14: Advanced Typography
**By Yannis Haralambous, Ph.D.**
*From Fonts & Encodings, pp. 551–612*

---


<!-- Page 570 (Book page 550) -->
Enriching Fonts:
Introduction
The title of this chapter refers to the “advanced typographic features” of OpenType and
AAT fonts, which are tables added to the basic TrueType fonts by Microsoft, Adobe, and
Apple. We have witnessed the emergence of two new font formats: OpenType (deﬁned
by Adobe and Microsoft, formerly called “TrueType Open”) and AAT (for “Apple ad-
vanced typography”, formerly called “TrueType GX”). Thanks to these tables, we can
better meet the needs of the non-Latin scripts, in particular the Asian scripts, but also
some of the requirements of traditional typography, well beyond the possibilities of the
original TrueType format. Here, then, is the dialog box for OpenType in Adobe Illus-
trator CS2 (under Mac OS X), where the diﬀerent OpenType features (default ligatures,
calligraphic letters, etc.) are shown in the form of buttons that are enabled only when
the feature in question is present in the font:
Whether for setting type in Sanskrit, in Urdu or Arabic with aesthetic ligatures, in He-
brew with vowel points, in Elzevirian Greek with ligatures, in calligraphic Latin, or sim-
ply in a text font with capitals and old-style ﬁgures, OpenType and AAT tables are well
549

<!-- Page 571 (Book page 551) -->
Chapter 14 : Enriching Fonts: Advanced Typography
up to these challenges, and others as well. What is particular about these fonts is that the
arrangement and substitution of the glyphs are not part of the operating system, as used
to be the case, but are included in the font—more speciﬁcally, in the OpenType and AAT
tables. That makes the use of the font a little more cumbersome, since the system must
read and interpret each font’s “advanced” tables. But at the same time, it oﬀers the font’s
designer enormous ﬂexibility, as she has full responsibility for the font’s behavior: she
can adopt rules already present in other fonts, modify them, or even invent new ones of
her own!
How, exactly, do the advanced typographic features work? Here is a general description.
We start with three concepts: “script”, “language”, and “feature”. When we use a font,
we use a given script and a given language. (If the user does not specify these values,
the default values are used: in the United States, they would be Latin for the script and
English for the language.) Within this framework, the font oﬀers a number of rules for
substitution or movement of a glyph that are stored within the features. An example
of a rule for substitution would be shifting from lining ﬁgures, 0123456789, to old-style
ﬁgures, 0123456789; the feature that contains this rule has a name, “onum”. An example
of movement would be the placing of an accent over a letter (from ‘aˆ’ to ‘â’); the feature
that contains this rule is called “mark”. Some features are programmed to be executed by
default when the font is selected; others are enabled by the user. For example, there is
the feature “liga”, which manages ordinary ligatures, such as ‘ﬁ’, ‘ﬂ’, etc. This feature is
enabled by default; nonetheless, it can be disabled at the request of the user.
OpenType features contain rules called lookups. A lookup can consist of one or more sub-
stitutions or one or more positionings of glyphs.
Substitutions can be quite complex. Thanks to them, we can set type in Arabic, Sanskrit,
Khmer, or any other highly contextual script. In these scripts, the shape of a letter de-
pends on the letters that precede it or follow it. Here is a list of the diﬀerent types of
substitutions:
• Single substitutions (§D.9.4.1): one glyph is replaced with another, as, for example, a
lowercase letter with a small capital.
• Multiple substitutions (§D.9.4.2): one glyph is replaced by several. This substitution is
rather uncommon, except when it is necessary to reposition the parts of a glyph. For
instance, it sometimes happens in German that the letter ‘T’ is followed by a vowel
with an umlaut (as in the word “Tür”), and, in some fonts, the umlaut collides with
the serif on the right arm of the ‘T’. To solve this problem, we use a positioning rule;
but ﬁrst we must separate the umlaut from the letter ‘u’, which we can do with a
multiple substitution that turns the ‘ü’ into a ‘u’ and an umlaut.
• Alternate substitutions (§D.9.4.3): the software allows us to select an alternate form of
a given glyph through a special graphical interface, such as a pull-down menu that
shows us all the available variants.
• Ligatures (§D.9.4.4): several glyphs are replaced by a single one. This is the classic case
of the ligatures ‘ﬁ’, ‘ﬂ’, ‘FFFFFFFFFFf’, etc.

<!-- Page 572 (Book page 552) -->
Introduction
Single Substitution
Multiple Substitution
(untied Indian ligature)
Contextual Substitution
(the connecting strokes of letters “d” and “s” disappear)
Alternate Substitution (the nine “d”s of font Zapﬁno)
Ligature Substitution
Reverse Chaining Contextual Single Substitution (contextuality of Urdu writing system)
examples of substitutions
• A contextual substitution (§D.9.4.5) consists of one or more substitutions of the types
listed above—single substitutions, multiple substitutions, or ligatures—which are
instantiated according to the context, i.e., whether the string of glyphs to be replaced
is preceded and/or followed by certain glyphs. The classic example is that of Arabic,
where an isolated letter turns into an initial form when followed by a letter that is
connected to it. In this case, the change of shape is a single substitution, and the
context is the following glyph.
• Chained contextual substitutions (§D.9.4.6). The example of an isolated Arabic let-
ter that becomes an initial form, mentioned above for contextual substitution, is
in fact an example of what we should not do: speciﬁcally, the “context” is used by
the substitution and cannot become the object of another substitution. The letter
that follows our isolated letter cannot in turn become, for example, a medial form.
Chained contextual substitution solves the problem by introducing the notions of
pre-chain and post-chain: once again, these are glyphs that come before or after glyphs
to be replaced, but this time the glyphs remain available for other operations.

<!-- Page 573 (Book page 553) -->
Chapter 14 : Enriching Fonts: Advanced Typography
Single Adjustment
(special parentheses for all-caps text)
MarkToBase Attachment
MarkToMark Attachment
Cursive Attachment
Pair Adjustment (kerning)
MarkToLigature Attachment
Context Positioning
examples of positioning
• Reverse chaining contextual substitution (§D.9.4.7). This is a variant of the proceeding
that was introduced especially for the Urdu language. What distinguishes it is that it
processes a string of glyphs from left to right, i.e., in the direction opposite to that of
the Urdu script, which is written from right to left.
Positioning includes kerning, of course, but also types of positioning that may be quite
sophisticated, such as contextual kerning, where the spacing of two letters closer together
or farther apart depends on their context. Here is a list of the diﬀerent types of position-
ing:
• Single adjustment positioning (§D.9.3.2): certain glyphs are moved horizontally or
vertically.
• Pair adjustment positioning (§D.9.3.3): when certain pairs of glyphs are detected in
the typeset string, their glyphs are moved horizontally and/or vertically. This posi-
tioning is more powerful than a kerning pair: in a conventional kerning pair, only
the second glyph is moved, but here it is also possible to move the ﬁrst glyph or both.
• Cursive attachment (§D.9.3.4), a truly spectacular property: a point is marked as the
“exit point” of the glyph, and another point is marked as being its “entry point”.
Cursive attachment applied to a string of glyphs will make the exit point of the nth
glyph correspond with the entry point of the (n+1)th glyph. This feature is ideal for
cursive and calligraphic fonts.
• Combining diacritical marks (§D.9.3.5): We deﬁne as marks some positions on the
glyph’s working area. Diacritical marks (accents, cedillas, etc.) also have marks of
this sort. When applied to a glyph followed by a diacritic, this positioning will attach

<!-- Page 574 (Book page 554) -->
Introduction
the diacritic to the glyph by making the appropriate marks coincide. This feature
is ideal for placing any desired accent on any desired glyph, an operation that is
indispensable for any self-respecting Unicode rendering engine.
• Multiple diacritical marks (§D.9.3.6): a variant of the preceding in which diacritical
marks combine with one another to form more complex signs. This feature is often
needed in phonetic notation.
• Diacritical marks on ligatures (§D.9.3.7): some fonts include a multitude of ligatures,
often operating on vowels. Often these vowels can bear accents. What, then, should
we do? Design the same ligatures with all the combinations of accents? This position-
ing solves the problem by deﬁning one mark for each of the ligature’s components.
• Contextual positioning (§D.9.3.8): when a glyph is moved only if it is preceded or fol-
lowed by certain other glyphs. A typical example: if we write “V.A.V.”,1 the second ‘V’
is moved closer to the second period only because that period is preceded by an ‘A’.
But the same combination of glyphs ‘.’ and ‘V’ in “V.V.” should not be kerned, or the
two ‘V’s would bump into each other—“V.V.”—and look like a ‘W’;
• Chained contextual positioning (§D.9.3.9): the same extension of contextual position-
ing as for chained contextual substitution. In other words, the glyphs that form the
context of our string are separated from it and can take part in other substitution or
positioning operations.
How can substitutions and positionings interact? Let us take a typical case: suppose that
we wish to take advantage of the “diacritical marks on ligatures” lookup to place a cir-
cumﬂex accent over the letter ‘a’ in an “ates” ligature. The ligature itself was, of course,
created by a substitution lookup. But it seems that there is a contradiction: if the original
string is (‘a’, “circumﬂex accent”, ‘t’, ‘e’, ‘s’), no ligature will be formed; and if the original
string is (‘a’, ‘t’, ‘e’, ‘s’, “circumﬂex accent”), we will obtain a ligature, but how will the
rendering engine know that the accent is intended for the letter ‘a’, not for another com-
ponent of the ligature?
To solve this sort of problem, OpenType ﬁrst classiﬁes all the glyphs into four types:
“single” (whose glyphs are also called “base glyphs”), “ligature”, “mark” (i.e., “diacritical
mark” or similar), and “component” (of a ligature or a glyph). Next, the substitutions
can choose not to apply to one or another type of glyph. For instance, in our example,
the ligature substitution will disregard the circumﬂex accent while preserving the in-
formation that is “attached” to the ﬁrst component of the ligature. Positioning, which
must necessarily come second, will collect this information, and everything will work
perfectly.
But let us leave the technical details aside and consider the implementation of OpenType
properties in existing software.
As happens often in computer science, there is a vast gap between the things that we see
on paper and those that work in the real world. The OpenType speciﬁcation allows us to
1 V.A.V. is the Vlaamse Aikido Vereniging (Flemish Aikido Union). http://www.aikido-vav.be/

<!-- Page 575 (Book page 555) -->
Chapter 14 : Enriching Fonts: Advanced Typography
hist (historical forms)
frac (diagonal fractions)
smcp (lowercase to small caps)
c2sc (uppercase to small caps)
dlig (discretionary ligatures)
liga (ligatures)
afrc (vertical fractions)
onum (oldstyle ﬁgures)
lnum (lining ﬁgures)
examples of features
saisons
faifons affligé
aFﬂigé
activiste
acivise 0123
0123
1/2
1/2
4
/
J.-Ph. Bec
J.-Ph. Bec
OUI
oui
deﬁne new features and give them any names we wish. But if we do so, no one will be able
to use the features in question, since word-processing software2 and desktop publishing
software oﬀer their users only certain predeﬁned features.
Here is a short list of the features most often recognized by applications3 in the context
of the Latin script:
• hist (“historical forms”). Certain letters are replaced with older forms. This feature
is often used to replace the ‘s’ with the “long s”, thus reprefenting the text fuch as it
would have appeared in the eigtheenth century. Warning: in English, the ‘f ’ is used
only at the beginning or in the middle of a word, as in the word“feafons”; in Ger-
man, however, the “round s” can appear in the middle of a word when that word is
a compound, as in “Au+gabe” (from “au+” and “Gabe”); compare the word “AufsaΩ”.
• liga (“standard ligatures”). These include, for example, the “f-ligatures”: all those
that begin with an ‘f’ or an ‘f ’. The distinctive characteristic of these ligatures is that
they are not immediately visible to the uninitiated. They improve the document’s
aesthetic quality without imparting a particular style. We can consider them as “de-
fault ligatures” to be used in every document.
• dlig (“discretionary ligatures”). These include, for example, the ligatures ‘c’ and ‘s’
that are found in Monotype Garamond, which give the La Pléiade series of books
all its charm. These ligatures go beyond improving the document’s aesthetic quality:
they impart a particular style to the document. Thus they should be used at the user’s
discretion, and that is the spirit of this feature.
• onum and lnum (old-style ﬁgures” and “lining ﬁgures”). The old-style ﬁgures onum, “01
23456789”, are characterized by their diﬀerent sizes and by the presence of ascenders
and descenders. Moreover, the zero resembles the letter ‘o’, and the one resembles a
2 Except Ω, which is able to use OpenType fonts directly.
3 The reader will ﬁnd a complete list of predeﬁned OpenType features in Appendix D (starting at
§D.10.2).

<!-- Page 576 (Book page 556) -->
Managing OpenType Tables in FontLab
small-capital ‘i’. The lining ﬁgures lnum, “0123456789”, all have the same height and
usually do not resemble any letter or other symbol. Some publishers use old-style
ﬁgures for page numbers and lining ﬁgures in the body text.
• frac and afrc (“fractions” and “alternative fractions”). Used to produce beautiful
fractions such as ‘4’, ‘2’, and ‘0’ from the glyph strings 1/4, 3/4, 1/42. The afrc
feature produces fractions with a horizontal bar: ‘ 1
2’, ‘ 3
4’, ‘ 1
42’.
• smcp and c2sc (“lowercase to small capitals” and “capitals to small capitals”).
Changes the case of glyphs.
The reader will ﬁnd in Appendix D a detailed technical description of the OpenType and
AAT tables. In the rest of this chapter, we shall discuss the practical aspects: how to enrich
a font by adding OpenType or AAT tables through the use of the two great software
packages FontLab and FontForge that we studied in the two previous chapters and by
means of another software product designed speciﬁcally for this task, Microsoft VOLT.
On the other hand, only FontForge is currently capable of incorporating AAT tables into
TrueType fonts; we have devoted the last section of this chapter to it.
Managing OpenType Tables in FontLab
Figure 14-1: The OpenType window in FontLab.
When we select Window>Panels>OpenType, FontLab presents us with the OpenType
window (see Figure 14-1). This window is divided into three parts. At the left, there is a
list of all the OpenType features in the font. The names of the features are always strings
of four letters (such as liga, c2sc, etc.). In §D.10.2 of this book, there is also a list of the
predeﬁned features, illustrated with examples.
In the window in Figure 14-1, we have selected the liga feature. In the upper right sec-
tion, we see a description of this feature in a syntax developed by Adobe and known as

::: tip Figure 14-1: The OpenType window in FontLab
![Figure 14-1: The OpenType window in FontLab](/images/fonts-encodings/fig14-1.png)
*Figure 14-1: The OpenType window in FontLab.*
:::


<!-- Page 577 (Book page 557) -->
Chapter 14 : Enriching Fonts: Advanced Typography
“feature deﬁnition language”. In the lower section, this syntax is used again to deﬁne
glyph classes, which are used in all of the font’s features.
Thus it is clear that we must know the syntax of this famous “feature deﬁnition language”
in order to incorporate even the slightest feature into the font. When FontLab compiles
the code written in this language to produce OpenType tables, if there is the slightest syn-
tax error, the compilation will halt with a less than comforting and informative message
of this kind:
`<PalatinoLinotype-Roman>` aborting because of errors
Fortunately, the syntax of the feature deﬁnition language is quite simple. In the follow-
ing section, we shall give a brief overview of it.
Feature Deﬁnition Language
The “feature deﬁnition language” was deﬁned by Adobe [325] in the course of work on
SDK OpenType. Adobe oﬀers a development kit with tools that compile code written in
this language and insert it into a TrueType font, which accordingly becomes an Open-
Type font. Although Adobe’s speciﬁcation is already at version 1.4, FontLab covers only
a subset of its features. This is the subset that we shall examine below.
First of all, a general rule: the goal of this syntax is to deﬁne OpenType features. To deﬁne
a feature named “foo”, we will write:
feature foo {
... rules ...
} foo ;
Between the braces we will write rules for positioning or substitution.
From the few lines of code above, we can already conclude that, as in most programming
languages, the braces serve to delimit blocks of code and the semicolon serves to termi-
nate an expression. There are other special characters that we shall encounter as they
arise. For now, let us say simply that the pound sign (#) is used for writing comments:
everything that follows it, up to the end of the line, is considered a comment.
Identifying and classifying glyphs
Folk wisdom has it that things should be called by their names. For example, we call
a glyph by its name, provided that it has one and that the name contains nothing but
ASCII letters, digits, periods, and underscores. And it may not begin with a digit.4 Font-
Lab will assign an arbitrary name to any unnamed glyph. Glyph names that are unlucky
enough to be keywords in the feature deﬁnition language must be preceded by a back-
slash (in other words, if gizmo is a keyword in the language, \gizmo is a glyph called
gizmo).
4 The language’s speciﬁcation provides for names of the type \123 for CIDs, but FontLab seems not to
recognize this form.

<!-- Page 578 (Book page 558) -->
Managing OpenType Tables in FontLab
As glyphs often have the same behavior, we are wise to group them into classes and then
to use these classes, rather than individual glyphs, in our expressions. A class is simply a
set of glyph names placed within brackets: [ e eacute egrave ]. In some cases, we can
write ranges of glyphs: [ A-Z ], [ a-z ], [ foo.023-foo.437 ], [ A.foo-Z.foo ], etc.
We can assign a name to a class. It must begin with an at sign (@):
@lowercase = [ a-z agrave eacute egrave ugrave ] ;
Other classes may appear in the deﬁnition of a class:
@letters = [ @lowercase @capitals agrave eacute ] ;
Scripts, languages, features, lookups
We have already discussed four hierarchical levels of the system of OpenType features:
script, language, feature, and lookup. Each of these levels must be speciﬁed in the feature
deﬁnition language, through the use of names of four letters or fewer. Example:
feature foo {
script latn ;
language ENG ;
... rules for English ...
language DEU ;
... rules for German ...
script grek ;
... rules for Greek ...
} foo ;
In this example, the liga feature has diﬀerent rules for the English and German lan-
guages, which belong to the Latin script, and still other rules for Greek, which is the
default language for the Greek script.
The reader will ﬁnd a complete list of scripts and languages in §D.10.1 of this book.
A few details: Every time we change scripts, the language becomes DFLT (from the word
default). The default script is latn. There is a command that combines script and lan-
guage:
languagesystem latn ENG ;
One word on the behavior of the language keyword: rules deﬁned for the “default” lan-
guage are added to those deﬁned for a speciﬁc language. In other words, when we deﬁne a
rule for the “default” language, we cannot eliminate it: it will apply to all other languages
that use the same script. We can get around that with the excludeDFLT keyword:

<!-- Page 579 (Book page 559) -->
Chapter 14 : Enriching Fonts: Advanced Typography
feature foo {
script latn ;
language DFLT ;
... rule A ...
language DEU ;
... rule B ...
language ENG excludeDFLT ;
... rule C ...
} foo ;
In this example, when the feature foo is enabled, only rule A will be applied in an Italian
document; in a German document, rules A and B will be applied, in that order; ﬁnally,
in a French document, only rule C will be applied, since the “default” rule, A, has been
excluded.
Finally, what is a lookup in this context? It is nothing but a “macro”, a way to group sub-
stitution or positioning rules in a block of code, give the block a name, and subsequently
make reference to the block by its name. For example, if we have previously deﬁned:
lookup foo {
... rules ...
} foo ;
in a property, we can then execute the rules in the block by simply writing:
lookup foo ;
To avoid misunderstandings, note that our use of the term lookup here is not really the same as the
deﬁnition that we gave in the introduction to this chapter, nor is it the same as the one found in
Appendix D. Indeed, if we write:
feature foo { ... rules ... } foo ;
without explicitly mentioning the lookup, the rules rules will nevertheless be collected into a
lookup in the generated table. By writing:
feature foo {
lookup bar { ... rules ... } bar ;
lookup bar ;
} foo ;
we obtain exactly the same result. Finally, if we write:
feature foo {
loookup bar {
... rules A ...
} bar ;
... rules B ...
lookup bar ;
} foo ;

<!-- Page 580 (Book page 560) -->
Managing OpenType Tables in FontLab
the result will be a feature foo with two lookups: the ﬁrst one, which is implicit, will contain
rules
B, and the second one, which is explicit, will contain rules
A. The names given to the
lookups are strictly internal to the feature deﬁnition language and do not appear anywhere in
the OpenType tables generated.
In the example of interaction between substitutions and positionings that we gave at the
start of this chapter, we spoke of types of glyphs. At any time, we can specify the type of
glyph to which the rules that we are writing will apply. To that end, we need only use
the keyword lookupflag followed by one or more of the following keywords, separated
by commas:
• IgnoreBaseGlyph: what follows will not apply to base glyphs
• IgnoreLigatures: what follows will not apply to ligatures
• IgnoreMarks: what follows will not apply to marks
Substitution rules
Now that we have ﬁnished these preliminaries, let us move on to the heart of the lan-
guage: the writing of substitution rules. We shall use four keywords: substitute (often
abbreviated sub), by, from, and, less often, ignore. Let us review the six types of substi-
tutions:
• single substitutions: to replace a glyph a with a glyph b, we write:
sub a by b ;
We can also use glyph classes. For instance, if @lowercase is the class of the lowercase
letters and @small_cap the class for the small capitals, we can write:
sub @lowercase by @small_cap ;
The two classes must be of the same size. Another possibility is to replace all the
members of a class with a single glyph:
sub [ space A-Z a-z ] by bullet ;
In this example, the letters and the spaces are replaced by bullets, a very handy pro-
cedure when entering passwords.
• Multiple substitution: to replace, for example, the ligature ffi with the glyphs f, f, i,
the speciﬁcation allows us to write simply:
sub ffi by f f i ;
Here we are not allowed to use classes. Note that this syntax appears in the speciﬁ-
cation but that FontLab version 5 does not yet recognize it.

<!-- Page 581 (Book page 561) -->
Chapter 14 : Enriching Fonts: Advanced Typography
• Alternate substitutions: to force word-processing software to ask the user which form
among ‘e’, ‘é’, ‘è’, and ‘ê’, for example, to use every time it encounters an ‘e’, we can
write:
sub e from [ e eacute egrave ecircumflex ] ;
• Ligatures, the most classic substitution: to replace the pair of glyphs f and i with the
glyph f_i, we can write:
sub f i by f_i ;
Any number of glyphs may be replaced by a ligature.
• Contextual substitution, whether chained or not, is a replacement of one or more glyphs
by a single one, but a replacement that occurs only if the glyphs appear in a certain
context—that is, if they are proceeded and followed by well-deﬁned strings of glyphs.
Very important: in the syntax, we use the nonoriented apostrophe (') to indicate
the glyph(s) to substitute. Everything that does not have an apostrophe is part of the
context.
For example, suppose that we have two versions of the letter ‘d’, called d and
d.prettier, and that we always wish to use the second version before a vowel. Then
we are making a single substitution of d by d.prettier, but one that occurs only if
d is followed by a glyph in the class [ a e i o u ]. Thus we shall write:
sub d' [ a e i o u ] by d.prettier ;
Another example: To replace the hyphen (hyphen) with an en dash (endash) when-
ever it occurs between two digits, we can write:
@digits = [ zero one two three four five six seven eight nine ] ;
sub @digits hyphen' @digits by endash ;
• reverse chaining contextual substitution, introduced as an afterthought for the needs
of the Urdu language, is not yet supported in the feature deﬁnition language, still
less by FontLab.
Sometimes the glyph classes can be of enormous size. For example, suppose that we have
a glyph T_e_X for the TEX logo and that we wish to replace the string “TEX” with this
glyph, but only when it is not part of a word, as it is in “CONTEXT”. We will then need
a substitution of the following type:
sub @all_but_letters T' E' X' @all_but_letters by T_e_X ;
But writing the class @all_but_letters would be quite tedious for a font with tens of
thousands of glyphs.
The keyword ignore allows us to work in the opposite direction by ﬁrst deﬁning the
excluded cases. For example, by writing:

<!-- Page 582 (Book page 562) -->
Managing OpenType Tables in FontLab
ignore sub [ A-Z Eacute ] T' E' X' [ A-Z Eacute ] ;
sub T' E' X' by T_e_X ;
we can eliminate the words “CONTEXTUAL”, “PRETEXTS”, etc., and then quietly re-
place all the remaining occurrences of “TEX” with T_e_X glyphs. But that still is not an
adequate solution: what to do about words that begin or end with “TEX”, such as “TEXT”,
“CORTEX”, etc.?
Fortunately, the syntax for the ignore keyword can take several expressions into account
simultaneously; these expressions are separated with commas. Thus, by writing:
ignore sub [ A-Z Eacute ] T' E' X' , T' E' X' [ A-Z Eacute ] ;
sub T' E' X' by T_e_X ;
we solve our problem.
Note that in the second line of code above we have used apostrophes as in contextual substitutions,
whereas the expression seems not to have a context. But—and this is a syntactic trap—the ﬁrst line
establishes a context, and thus the entire lookup is contextual. Consequently, we are required to
borrow the syntax of contextual substitutions in the second line.
Positioning rules
The speciﬁcation provides a syntax for each case of a positioning rule (whether for single
adjustment, pair adjustment, cursive attachment, diacritical marks, multiple diacritical
marks, diacritical marks on ligatures, contextual positioning, or chained contextual po-
sitioning). But FontLab currently supports only single and pair adjustment positioning
rules, possibly associated with a context. Nevertheless, the documentation for FontLab
claims that the future updates will see the incorporation of other types of positioning;
that is why we shall describe the syntax here, even though it cannot yet be used in the
current version of FontLab (version 5).
Before discussing the diﬀerent types of positioning, let us establish a few preliminary
notions: those of value records and anchors.
A “value record” is simply a series of four numbers: the ﬁrst two are the coordinates of
the displacement from the glyph’s origin (X placement and Y placement), and the other
two are those of the displacement from the glyph’s set-width, i.e., from the far end of the
glyph’s displacement vector (X advance and Y advance). If (a,b,c,d) represents these four
numbers, the syntax for the value record is < a b c d >. In the ﬁgure below:
<0 0 0 0>
<-400 0 0 0>
<-400 0 -400 0>
<-400 -400 -400 0> <-400 -400 -400 -400>
we see the eﬀect of ﬁve simple displacements applied to the letter ‘E’ with diﬀerent value
records: in the ﬁrst case, the two vectors are zero; in the second case, the origin is moved to

<!-- Page 583 (Book page 563) -->
Chapter 14 : Enriching Fonts: Advanced Typography
the left without changing the glyph’s width, i.e., the endpoint of the glyph’s displacement
vector; in the third case, we move this endpoint to the left, but its distance from the ‘X’
is restored; in the fourth case, we move the glyph’s origin downward, but the endpoint
remains on the baseline; ﬁnally, in the ﬁfth case, the endpoint is also moved downward:
all the glyphs that follow will be set at that depth, as long as the feature remains enabled.
We can also write a value record with a single number, the abscissa for the oﬀset of the dis-
placement vector, i.e., the third of these four numbers. Unless the feature is vkrn (vertical
kerning), in which case the ordinate (therefore the fourth number) is used rather than
the abscissa. When the value record consists of a single number, it is not necessary to use
the symbols < >.
An “anchor” is a location on the glyph’s working area that serves as an attachment point
for another glyph. This other glyph must also have an anchor, and the rendering engine
simply matches these two locations to place the second glyph correctly with respect to the
ﬁrst. An anchor whose coordinates are (100,200) is written `<anchor 100 200>`. Anchors
are not recognized by FontLab v.5.
Armed with these two concepts, we are ready to explore the various types of displacement
rules. In these rules, we shall use three keywords: position (usually abbreviated pos),
cursive, and mark. Here are the eight types of displacements:
• The displacement of a single glyph, where we ask some glyphs to move horizontally
and/or vertically. We simply write the keyword pos followed by the name of the
glyph and the value record for the displacement. For example, to move an ‘x’
100 units upwards without causing the following glyphs to be moved upwards
as well, we write:
pos x <0 200 0 0> ;
We can also use a class of glyphs instead of the name of a glyph.
• The displacement of a pair of glyphs, where we request that the glyphs in certain pairs
be moved horizontally and/or vertically. The general syntax is very simple: we write
each of the two glyphs followed by its value record. But in order for FontLab v.5 to
recognize this syntax, there must be only one value record (that of the second glyph),
and it must consist of only a single number. Thus we are limited to the case of a
simple kerning pair, as, for example:
pos A T - ;
The only possibility of going a bit further is to use classes instead of glyphs. For in-
stance, if we wish to kern all the letters derived from ‘A’ with all of those derived
from ‘T’, we write:
@derived_from_A = [ A Aacute Agrave Acircumflex Adieresis
Atilde Aring ] ;
@derived_from_T = [ T Tcaron Tcommaaccent ] ;
pos @derived_from_A @derived_from_T - ;

<!-- Page 584 (Book page 564) -->
Managing OpenType Tables in FontLab
This rule will then produce 21 (!) kerning pairs.
• The cursive attachment, where the “exit point” of each glyph is attached to the “entry
point” of the following one:
entrée
sortie
entrée
sortie
entrée
sortie
entrée
sortie
entrée
sortie
Thus we must deﬁne the entry and exit points of each glyph. We do so using anchors.
Merely adding the keyword cursive suﬃces:

```fea
pos cursive f <anchor - 105> <anchor 197 105> ;
pos cursive i <anchor - 105> <anchor 155 105> ;
```

and so forth. We can also use glyph classes. This type of positioning rule is not rec-
ognized by FontLab v.5.
• Combining diacritical marks, where we deﬁne marks both on the base glyph and on
the diacritical marks themselves. The rendering engine will match up these marks.
In our case, we shall, once again, use anchors. This time we shall proceed in two steps:
ﬁrst, we shall deﬁne the anchor on the diacritical mark by using the mark keyword
to show that the glyph is a diacritical mark rather than a base glyph; then we shall
use pos to indicate the anchor on the base glyph and the name of the glyph for the
diacritical mark. This approach allows us to have multiple anchors, corresponding
to the diﬀerent types of diacritical marks, on the same base glyph. Example:

```fea

```fea

```fea
mark circumflex <anchor 511 1117> ;
pos E <anchor 686 1505> mark circumflex ;
```

Note that a diacritical mark can have only one anchor, whereas a base glyph can
have any number, corresponding to the various diacritical marks. In the expressions
below, we shall also use glyph classes. This sort of positioning rule is not recognized
by FontLab v.5.
• Multiple diacritical marks, where we place diacritical marks over other diacritical
marks. For example, if we wish to place a tilde over a circumﬂex accent, we can
write:
mark circumflex `<anchor 511 1117>` ;
mark tilde `<anchor 500 1074>` ;
pos mark circumflex `<anchor 511 1606>` mark tilde ;
```

Here, in the ﬁrst line, we deﬁne the lower anchor for the circumﬂex accent (which
is used to attach the accent to a base glyph), but the anchor described in the third
line is above the circumﬂex accent and thus serves to attach the tilde to it. This type
of positioning rule is also not recognized by FontLab v.5.

<!-- Page 585 (Book page 565) -->
Chapter 14 : Enriching Fonts: Advanced Typography
• Diacritical marks on a ligature, where we take the glyph of a ligature and deﬁne as
many anchors for it as the ligature has components, in order to attach diacritical
marks to it. The syntax is a bit awkward. Suppose that in our font, Monotype Gara-
mond italic, we have a ligature “õ” that we would also like to use with two circumﬂex
accents, “•” (as in the French verb form prêtâmes). This ligature has three compo-
nents, and therefore—at least—three possible anchors. To add the two circumﬂex
accents to it, we can write:
mark circumflex <anchor 151 438> ;
pos e_t_a <anchor 286 432> `<anchor NULL>` `<anchor NULL>`
mark circumflex ;
```

pos e_t_a `<anchor NULL>` `<anchor NULL>` `<anchor 832 432>`
mark circumflex ;
where `<anchor NULL>` was added only to arrange the three anchors correctly within
the syntax. This type of positioning rule is also not recognized by FontLab v.5.
• Contextual and chained contextual positioning, where a glyph is positioned only when
it is preceded or followed by certain other glyphs. The syntax is similar to that for
substitutions:
pos A period' V' - ;
means that the pair period, V is kerned only when it is preceded by an A, which
solves the problem of the string “S.A.V.”. Recall that in a contextual rule the glyphs
that are substituted or positioned bear an apostrophe; those that have no apostrophe
establish the context. This type of positioning rule is unfortunately not recognized
by FontLab v.5.
Two exceptions: the aalt and size features
The syntax that we have examined here is valid for all features except two very special
ones: aalt (“all variants”), which enables all the glyph variants in the font, and size,
which is not really a feature but rather a location in which some data on the optical size
of the font may be stored.
Let us ﬁrst take the aalt feature. Its purpose is to enable all the single substitutions and
all choices of variants in the font. It should be placed ﬁrst on the list of features, and it
must contain the keyword feature followed by the name of a feature for all features of
this type. For example, suppose that in our font we have the features smcp (small capitals)
and ornm (choice of ornaments in the font). We can then write:
feature aalt {
feature smcp ;
feature ornm ;
} aalt ;

<!-- Page 586 (Book page 566) -->
Managing OpenType Tables in FontLab
The size aims to make up for an enormous shortcoming in PostScript (other than Multi-
ple Master, with their “optical size” axis) and TrueType fonts, which is that they completely
disregard the optical size: there are, in fact, fonts named Times New Roman Seven, Times Ten,
and ITC Bodoni Seventy-Two, but the fact that their optical sizes are, respectively, 7, 10,
and 72 appears only in their respective names,5 nowhere in the fonts themselves.
The syntax for size is as follows: We use the keyword parameters followed by four num-
bers. The ﬁrst is the font’s optical size, expressed in tenths of a point. The second is for
fonts issued in multiple optical sizes; we can say that they belong to a family and that
the members of this family are numbered sequentially, starting at 0. Finally, the two
remaining numbers express the range of optical sizes at which the font can also be used.
Let us take, for example, the excellent font ITC Bodoni. It is issued in three optical sizes:
6, 12, 72. We could thus include the following feature in the font for optical size 12:
feature size {
parameters 120 1 90 299 ;
}
which means that it has an optical size of 12, which is the second member of the family
ITC Bodoni, and that it can also be used for actual sizes between 9 and 29.9.
FontLab’s User Interface
Figure 14-2: The OpenType window in FontLab.
After this brief overview of the Adobe syntax used by FontLab to describe OpenType fea-
tures, let us return to the software itself. Selecting Window>Panels>OpenType opens
the OpenType window (Figure 14-2), which we shall examine here in detail.
To add a feature, we click on the button
and automatically obtain the following code:
5 Again, take, for example, the font Linotype Old Style 7: is it indeed meant to be used at the optical size
of 7, or does the “7” indicate something else?

::: tip Figure 14-2: The OpenType window in FontLab
![Figure 14-2: The OpenType window in FontLab](/images/fonts-encodings/fig14-2.png)
*Figure 14-2: The OpenType window in FontLab.*
:::


<!-- Page 587 (Book page 567) -->
Chapter 14 : Enriching Fonts: Advanced Typography
feature xxxx {
sub by ;
} xxxx ;
We must then replace xxxx with the name of the new feature and also replace the line
sub by ; (which is incomplete and will therefore cause compilation to fail if we leave it
there unchanged) with the code for the feature.
Clicking on
deletes the selected feature from the list.
At the bottom of the window, we can write deﬁnitions for the glyph classes that will be
available to all features.
The
button opens and saves text ﬁles containing feature code. It is very handy when
we wish to create several fonts with the same features—at least for substitutions, as po-
sitionings depend heavily on the shapes of the glyphs and cannot readily be shared by
multiple fonts.
The
button is very handy: merely clicking on the name of a glyph in the code and then
on this button will cause FontLab to display the glyph in question in the font window
or, if it is active, the glyph window. The button
replaces one glyph name with another
throughout the code.
Once we have ﬁnished writing the code for OpenType features, we must compile it, using
the button
. If there is an error in the code, the compilation will fail, and an error
message will be displayed in the Window>Panels>Output window.
Figure 14-3: The OpenType window in FontLab.
FontLab oﬀers us a very pretty interface for testing our features. Clicking on
opens
the window shown in Figure 14-3. This window contains three tabs. The one of interest
to us here is the ﬁrst: OpenType Features. We see at the left a list of the font’s features,

::: tip Figure 14-3: The OpenType testing window in FontLab
![Figure 14-3: The OpenType testing window in FontLab](/images/fonts-encodings/fig14-3.png)
*Figure 14-3: The OpenType testing window in FontLab.*
:::


<!-- Page 588 (Book page 568) -->
Managing OpenType Tables in FontLab
equipped with checkboxes. We select the feature(s) that we wish to test. We also select
the script and the language from pull-down menus, and we type a string (using a slash to
enter glyph names directly: /eacute, etc.) in the input area provided. The window then
displays, one above the other, the renderings of the string with and without the features.
Clicking on the
button causes FontLab to display the glyphs’ displacement vectors (a
feature that is very convenient when used with positioning rules). Finally, clicking on
causes the text to be rendered from right to left—an indispensable option for Arabic,
Hebrew, and Syriac fonts.
Managing glyph types
Choosing Properties on a glyph’s pop-up menu opens the win-
dow shown opposite.
In this window, we can specify the name of a glyph, the Unicode
code associated with it (if any), and, above all, its OpenType type
(“single glyph”, “ligature”, “mark”, “component”). In the case of a
ligature, we must also specify the number of components. This in-
formation is essential so that we can use the lookupflag keyword
in code and thus restrict the application of a lookup to a certain
type of glyph. The typical example of the application of this func-
tionality particular to OpenType is the case of a string of glyphs
that should ordinarily form a ligature but that is interrupted by a
diacritical mark. We can specify that the substitution of ligatures
ignore glyphs of type “mark”, and the ligature will be formed, even in the presence of a
diacritical mark.
Managing glyph classes
Figure 14-4: The OpenType window in FontLab.
FontLab has an interface for grouping glyphs into classes. Selecting Window>Panels>
Classes opens a window with two tabs; the one of interest to us is Classes (Figure 14-4).
In this tab, we can deﬁne glyph classes just as in the OpenType window (button
) and
ﬂesh them out by writing names glyphs or dragging and dropping glyphs’ boxes from
the font window.

::: tip Figure 14-4: The Classes panel in FontLab
![Figure 14-4: The Classes panel in FontLab](/images/fonts-encodings/fig14-4.png)
*Figure 14-4: The Classes panel in FontLab.*
:::


<!-- Page 589 (Book page 569) -->
Chapter 14 : Enriching Fonts: Advanced Typography
The glyph classes so deﬁned are used for kerning by class but also for writing OpenType
features. We need only check Add all glyph classes to OpenType feature definition
code in FontLab Studio>Preferences>General Options>Unicode and OpenType
to turn them all into OpenType glyph classes. Warning: even though these classes are not
displayed at the bottom of the OpenType window, they are nonetheless available in the
code. For instance, if we have deﬁned the class class1, we can use @class1 in the code
for our features.
Managing anchors
Although anchors do not yet work in the
feature deﬁnition language implemented
in FontLab v.5, the software does oﬀer a
rather convenient way to manage anchors.
It would not be unreasonable to predict
that this interface will lend itself admirably
to the management of OpenType anchors
in a future version of the software.
Let us open the glyph window. By right-
clicking (under Windows; Ctrl-click on
the Macintosh) at the point where we wish
to set an anchor, we can select Add Anchor
from the pop-up menu that opens. This pro-
cedure creates an anchor, which is a point
marked with a red cross and accompanied
by a name. We can immediately enter a name or modify it later by returning to the
pop-up menu.
Let us do so: we shall place an anchor over a letter—‘o’, for example—and give it a
name—say, top, as in the ﬁgure above.
Next, we shall go to the window for an accent, such as the tilde, and place another anchor
below the accent. Let us call it—careful, this is important!—_top, i.e., the same name as
the anchor for the base glyph, but preceded by an underscore. Now let us once again
bring up the glyph window for the letter and select the Anchors tab in the Window>
Panels>Preview window:
Surprise! We see the combination of the letter and the accent. In fact, we shall see all
the accents compatible with this letter (i.e., those with anchors whose name is the same
as an anchor on the letter)—a very helpful tool for managing interactions between base
glyphs and diacritical marks.
Thus we are eagerly looking forward to the integration of OpenType anchors into Font-
Lab’s user interface and, above all, into the code for OpenType features! As we shall see
under VOLT and FontForge, the interactive manipulation of anchors is a must for any
graphical interface for the management of OpenType positioning.

<!-- Page 590 (Book page 570) -->

## 14.3 Managing OpenType Tables in VOLT

Figure 14-5: The Preview panel window in FontLab.

## 14.3 Managing OpenType Tables in VOLT

VOLT (Visual OpenType Layout Tool) is a utility distributed freely by Microsoft whose only
purpose is to add OpenType tables to TrueType fonts. VOLT runs only under Windows.
A web page [266] at Microsoft’s site is devoted to it, but the software itself cannot be
downloaded from that page. To obtain it, one must ﬁrst register for the discussion forum:
http://communities.msn.com/MicrosoftVOLTuserscommunity
The links for downloading the software appear on this forum’s web site.
Figure 14-6: The “project” window in VOLT.
The “project” window in VOLT (see Figure 14-6) includes, from top to bottom, some
menus, a row of buttons, three graphical areas, and another row of buttons. The three
graphical areas will contain:
• The hierarchy of scripts, languages, features, and lookups in the font

::: tip Figure 14-5: The Preview panel window in FontLab
![Figure 14-5: The Preview panel window in FontLab](/images/fonts-encodings/fig14-5.png)
*Figure 14-5: The Preview panel window in FontLab.*
:::

::: tip Figure 14-6: The project window in VOLT
![Figure 14-6: The project window in VOLT](/images/fonts-encodings/fig14-6.png)
*Figure 14-6: The project window in VOLT.*
:::


<!-- Page 591 (Book page 571) -->
Chapter 14 : Enriching Fonts: Advanced Typography
• The complete list of lookups
• The list of glyph classes
Aside from the project window, there are also windows for glyphs, substitutions, posi-
tionings, glyph classes, and testing.
General mode of operation
We open a font by using the Open button. This operation will delete all the existing
OpenType tables in the font. Only the tables speciﬁc to VOLT will be preserved and in-
terpreted, which means that if we have begun to produce OpenType tables with other
software, our work will be lost6 and we shall have to start again from scratch.
The glyphs in a TrueType font do not have names, but we need names in order to write
OpenType rules. Thus we shall want to import any PostScript names for the glyphs from
the font’s name table. That can be done through Import>Import PostScript Names—
provided, of course, that these names exist in the font.
A preliminary, and often unpleasant, step for adding any OpenType feature is the clas-
siﬁcation of the glyphs into OpenType types (“single glyph”, “ligature”, “mark”, “compo-
nent”). To do so, we must check every glyph in the font with Tools>Edit Glyphs and make
sure that the type is correct. In other words, we must ﬁnd all the diacritical marks and
assign to them the type “mark”, all the ligatures (type “ligature”), and, if necessary, all
components of glyphs or ligatures (type “component”). We change the type through the
Type pull-down menu. For ligatures, we must also indicate the number of components
(Components pull-down menu).
To create a feature, we must set it in its context—its script and its language. Clicking on
Add Script creates a default script; we must then replace the text New Script <> with
the script’s four-letter name, written inside < >: for example, `<latn>`. VOLT will then
ﬁll in the complete name of the script. If the name is missing from VOLT, we simply
open tags.txt in the directory c:\Program Files\Microsoft VOLT and add the name.
Having chosen a script, we must next select a language. That is done by selecting the
script and clicking on Add Language. VOLT will select the default language (dflt); we
can modify this choice just as we changed the script.
Finally, to create a feature, we select a language and click on Add Feature. We proceed
in the same manner, by typing the four-letter abbreviated name within < >. The order
of the features is not signiﬁcant.
Now we have come to lookups. To create one, we click on the Add Positioning button
if we want a positioning or the Add Substitution button if we want a substitution. The
6 In theory there are two ways to export OpenType data from FontLab and import it into VOLT: the ﬁrst
is to check the option FontLab Studio>Preferences>Generating OpenType & TrueType>Export VOLT
data and thus export the data directly in the form of TrueType tables, and the second is to use the entry Save
features on the pull-down menu in the OpenType panel window and then to save the code for OpenType
features in VTP format. Unfortunately, however, in version 5 of FontLab, neither method works in practice.

<!-- Page 592 (Book page 572) -->

lookups are listed in the second section of the window, since they are independent of
the hierarchy of scripts, languages, and features. We assign a name to the lookup that we
create, but this name is strictly internal and can therefore be anything we wish. On the
other hand, the order of the lookups is signiﬁcant, and we can rearrange them in this
section of the window so that they will be in the right order, with only one small detail:
substitutions always appear before positionings.
Having written some lookups, we compile them by clicking on the Compile button, and
we test them in the prooﬁng window (Proofing Tool button), which we shall describe
below (page 575).
Finally, once we have deﬁned and tested all the lookups, we generate a font with no
VOLT tables, using File>Ship Font. But we can also save the glyph data (i.e., their names,
indexes, corresponding Unicode characters, and OpenType types), the lookups, the glyph
classes, and, more generally, all the OpenType data in the font, in the form of text ﬁles.
For that we use the entries on the Export menu. In this way, we can rapidly reuse these
data in similar fonts.
Glyph classes
In VOLT’s syntax, a glyph is represented by its name. We can group glyphs in three ways:
• By writing their names separated by commas and enclosing the entire list in braces:
for example, { a, e, i, o,~u~}.
• For a range (according to the order of the glyphs in the font), by simply writing the
names of the ﬁrst and last glyph with a hyphen in between and enclosing the list in
brackets: [ zero - nine ].
• For a named class, by writing the class’s name within < >: for example, `<digits>`.
To create a name class, we simply click on Add Glyph Group: a new glyph class is
created, and we can enter its name. The name is for internal use only and thus can be
anything we wish. Double-clicking on the name opens the glyph-class window. There
we can enter, one by one, the names of the glyphs belonging to the class. We can
use individual glyph names or glyph classes (within braces), ranges of glyphs (within
brackets), or references to other named classes (with the names of classes within < >).
Substitutions
Double-clicking on a lookup for a substitution opens the substitution window (see §14-7).
In this window we can write in the column From Glyphs -> To Glyphs all the substitution
rules of the lookup, in the proper order. The syntax is as simple as can be! It involves
merely writing the name of the source glyph(s), an arrow (“->”), and the target glyph(s):
• For a single substitution, such as the replacement of g with g.prettier, we write:
g -> g.prettier

<!-- Page 593 (Book page 573) -->
Chapter 14 : Enriching Fonts: Advanced Typography
Figure 14-7:
The substitution window in
VOLT.
There could hardly be a simpler syntax. Moreover, in the Shapes column, VOLT
will display images of the glyphs in the substitution, which is a good way to conﬁrm
the accuracy of the expression. Finally, VOLT will automatically determine that the
substitution is single, not of any other type.
• For a multiple substitution, such as the replacement of the ligature f_f_t by its con-
stituents, we write:
f_f_t -> f f t
• For an alternate substitution, such as oﬀering the user the glyphs a.old, a.odd,
a.pretty, a.ugly as variants of a, we write as many rules as there are variants, in the
order in which we want them to be oﬀered to the user:
a -> a.old
a -> a.odd
a -> a.pretty
a -> a.ugly
• For a ligature, such as the replacement of f and i with the glyph f_i, we write:
f i -> f_i
• For a contextual or chained contextual substitution, we write the substitution as if it
were a noncontextual substitution and we enter the glyphs for the context in the
Context Before | Context After input area at the bottom of the window. Ordinarily
there is already a vertical bar there. We write the “before” part of the context to the
left of this bar and the “after” part to the right. For example, to replace the hyphen
(hyphen) between two digits with an en dash (endash), we write:
hyphen -> endash
as the rule, and in the context area we write:

::: tip Figure 14-7: The substitution window in VOLT
![Figure 14-7: The substitution window in VOLT](/images/fonts-encodings/fig14-7.png)
*Figure 14-7: The substitution window in VOLT.*
:::


<!-- Page 594 (Book page 574) -->

## 14.3 Managing OpenType Tables in VOLT

[ zero - nine ] | [ zero - nine ]
• For a reverse chaining contextual substitution, we check the Reversal box in the up-
per right corner of the window.
In all the substitutions described above, including the context section of contextual sub-
stitutions, glyph names can be replaced by glyph classes. The only constraint is that only
one class can be used on each side of the arrow.
The string of glyphs can be displayed from right to left, if necessary, through the Text Flow
pull-down menu (RTL equals right to left, LTR equals left to right). The same is true of
the positioning window and the prooﬁng window.
Finally, a lookup can be selective and apply only to a certain type of glyphs. We have seen
an example in the introduction to this chapter: for an accent to be placed on a ligature,
the lookup for the ligature must ignore diacritical marks placed between the glyphs that
would form the ligature. To set ligatures up in this way, we have the Process Marks input
area. There we can enter ALL (process all diacritical marks), NONE (process none), or the
name of a glyph class within < >. Do not forget that this technique will work only if
all the glyphs to which it must apply have been “typed” beforehand; VOLT regards all
glyphs as being of “base glyph” type by default when it opens a TrueType font.
Positionings
Figure 14-8: The positioning window in VOLT.

::: tip Figure 14-8: The positioning window in VOLT
![Figure 14-8: The positioning window in VOLT](/images/fonts-encodings/fig14-8.png)
*Figure 14-8: The positioning window in VOLT.*
:::


<!-- Page 595 (Book page 575) -->
Chapter 14 : Enriching Fonts: Advanced Typography
While the design of the substitution window was crystal clear, the positioning window
takes a decided turn for the worse. We open this window by double-clicking on a po-
sitioning. The left part of the window has two areas in which we can enter glyph names
and, at the bottom, an area for entering the context. The right part of the window, called
the “positioning area”, displays the glyphs aﬀected by the positioning and allows the po-
sitioning of a second glyph and the anchor corresponding to it, which can be performed
either with the mouse or by entering precise coordinates.
Unlike substitutions, for which VOLT itself “guesses” the type of the lookup, for posi-
tionings we must specify the type through the pull-down menu in the upper left part
of the window. There are only ﬁve types on that menu, as the three types that involve
diacritical marks are merged and the two “contextual” types are achieved through the
input area for the context. Let us review the eight possible kinds of positioning:
• Single adjustment positioning (Single Adjustment), in which we ask a number of
glyphs to move horizontally and/or vertically. Only the list at the left is enabled, since
only one glyph is aﬀected by this positioning. In the positioning area, we can use the
mouse to move both the glyph and the brown vertical bar that represents its set-width.
• Pair adjustment positioning (Pair Adjustment), in which we ask that the members of
some pairs of glyphs be moved horizontally and/or vertically. It is as if we had two
copies of the preceding interface: there are two lists of glyphs, two glyphs in the po-
sitioning window, and even two bars for their set-widths. Everything can be moved,
both horizontally and vertically, and the possibilities thus open to us far surpass a
simple kerning pair.
• Combining diacritical marks (Anchor Attachment), in which we deﬁne marks, to be
matched up by the rendering engine, both for the base glyphs and for the diacritics.
To do so, we enter the name of the base glyph in the area at the left and the name of
the diacritic in the area at the right. The positioning area will then display the two
glyphs in their default positions, along with a brown cross.
There is a subtle point in the interface that must be understood: the brown cross
shows, at the same time, both the anchor for the base glyph and that of the diacritic.
When we move this anchor, both anchors are moved simultaneously. Only the anchor
for the base glyph has a name, which appears in the Anchor column, next to the name
of the diacritic.
To create another named anchor attached to a base glyph, we select this glyph and
any diacritic, then we write the name of the anchor under Anchor. At that moment,
the anchor in question is deﬁned for all the lookups in the font.
If we feel that the anchor is correctly positioned with respect to the base glyph, we
can lock it by checking the box Lock 1st Anchor. From then on, we cannot move
it again; if we move the diacritical mark, only the position of its anchor will be
changed.
Note that a base glyph can have multiple anchors: we simply give them distinct
names. By contrast, a diacritic can have only one anchor. If a glyph can be used as

<!-- Page 596 (Book page 576) -->

## 14.3 Managing OpenType Tables in VOLT

a diacritic in two diﬀerent ways (for example, a dot can be written above or beneath
a letter), we must create two diﬀerent glyphs, one for each use of the diacritic.
• Multiple diacritical marks, in which we set some diacritical marks over others. We use
the same interface (Anchor Attachment), the only diﬀerence being that we select two
glyphs of type “mark”. Warning: although the interface is the same, the lookup is of
a separate type; thus we cannot mix “mark on a base glyph” rules with “mark on a
mark” rules.
• Diacritical marks on ligatures, in which we take the glyph for a ligature and deﬁne
as many anchors for it as the ligature has components, so that we can attach dia-
critical marks to it. VOLT’s approach is rather funny. The positioning window dis-
plays as many anchors as there are components in the ligature. We select one of the
components through the Component pull-down menu and move the corresponding
anchor, still using the same diacritical mark. In this case, it behooves us to lock the
anchor for the diacritical mark by checking Lock 2nd Anchor; otherwise chaos may
result.
• Cursive attachment (Cursive Attachment), in which we join the “exit point” of each
glyph to the “entry point” of the following one. Once again, the interface is not very
intuitive and deserves a few words of explanation.
We might have expected to deﬁne two anchors for each glyph,7 one for entry and
one for exit. But that is not so. VOLT ’s procedure requires that anchors be deﬁned
by the interaction of the two glyphs, not on a single glyph. Thus in the positioning area
we have two glyphs (of which only the second can be moved) and only one anchor.
This anchor is at once the anchor for the exit point of the ﬁrst glyph and the anchor for
the entry point of the second glyph. The names of these anchors are required to be entry
and exit.
The prooﬁng window
The prooﬁng window (see §14-9) is one of VOLT’s best features, as it allows us to test the
behavior of an OpenType font in a very detailed manner. First we choose the script and
the language. Next we enter a string of glyphs, using glyph names separated by spaces. We
check the features to be tested. VOLT highlights the lookups used by these features.
An OpenType rendering engine will read the string of glyphs once for each lookup, in the
order in which the lookups appear. VOLT does the same, and we can follow its progress
glyph by glyph, lookup by lookup, with buttons like those of an audio CD player. The
Complete button will ﬁnish reading the string of glyphs, and the Restart button will start
again from the beginning.
Finally, in the case of a lookup for alternate substitution, we can test the diﬀerent ver-
sions of a glyph by entering the corresponding numerical values in the Alternate in-
put area.
7 FontForge, for instance, operates this way; see page 577.

<!-- Page 597 (Book page 577) -->
Chapter 14 : Enriching Fonts: Advanced Typography
Figure 14-9: The prooﬁng window in VOLT.

## 14.4 Managing OpenType Tables in FontForge

Once again, FontForge oﬀers us a perspective rather
diﬀerent from those of the other software systems, this
time with regard to OpenType tables. There is no lan-
guage to learn, unlike in FontLab; everything is man-
aged through menus and windows, which may be con-
sidered an advantage by those readers who are put oﬀ
by programming. At the same time, FontForge does
not share VOLT’s elitism; it agrees without hesitation
to read the OpenType tables already present in a font.
Conversely, the tables written by FontForge are stan-
dard OpenType tables that can be read by any other
software.
One peculiarity of the interface: only contextual tables
can be edited globally; by contrast, rules for position-
ing and substitution are attached to the glyphs. For in-
stance, to add a single substitution rule to the letter ‘f’,
we select its glyph in the font window and deﬁne this
rule through the corresponding tab in the Glyph Info
window. Rules are thus scattered throughout the set of
glyphs, which may be practical for small projects but can pose problems of organization
for large projects in which there are hundreds or even thousands of OpenType rules to
manage.
Nevertheless, we can get a synthetic view of the OpenType and AAT features through
View>Show ATT (see ﬁgure opposite). But this window allows us only to inspect the
data, not to modify them.

::: tip Figure 14-9: The proofing window in VOLT
![Figure 14-9: The proofing window in VOLT](/images/fonts-encodings/fig14-9.png)
*Figure 14-9: The proofing window in VOLT.*
:::


<!-- Page 598 (Book page 578) -->

## 14.4 Managing OpenType Tables in FontForge

Another peculiarity of FontForge is that anchors are managed in a way very diﬀerent
from that of VOLT (and one closer to what we hope to have one day in FontLab): we
deﬁne anchors, whether for diacritical marks or for cursive attachment, in the glyph
window. Thus we have a clear and precise view of the anchors deﬁned for each glyph,
and we can use them to construct positioning rules.
One last peculiarity, which is not the least of them: FontForge short-circuits the notion of a
lookup. To FontForge, a feature contains rules directly, with no intermediate hierarchical
level. When we deﬁne a new rule, we attach it to a feature, not to a lookup, as is done in
VOLT and in the OpenType ﬁle format. Never mind: the user is at least presented with
some technical details, and the result is often strictly the same.
Anchors
Figure 14-10: Two anchors deﬁned in the glyph window. Right: the anchor-class window.
As can be seen in Figure 14-10, FontForge allows us to set named anchors in the glyph
window. To set a named anchor, we must have deﬁned its class beforehand. That is done
at the level of the entire font in the Element>Font Info window, tab Anchor Classes.
Clicking on New opens a window for creating anchor classes. In this window, we specify
the name of the class—a strictly internal name that will be displayed next to the anchor
in the glyph window—the OpenType feature (Tag) to which the anchor is attached, the
scripts to which it applies, and, ﬁnally, its type: Default (mark on a base glyph or mark on
a ligature), Mk-Mk (mark on a mark), or Cursive (an anchor for a cursive attachment).
The feature to which we attach the anchor class calls for some explanation. FontForge
is well aware that we can create any features we wish but that, at the end of the day,
only certain features recognized by the major software packages have any chance of ever
being used. That is why FontForge oﬀers us six predeﬁned features (see page 577 for more
information):

::: tip Figure 14-10: Two anchors defined in the glyph window. Right: the anchor-class window in FontForge
![Figure 14-10: Two anchors defined in the glyph window (left) and the anchor-class window (right) in FontForge](/images/fonts-encodings/fig14-10.png)
*Figure 14-10: Two anchors defined in the glyph window. Right: the anchor-class window in FontForge.*
:::


<!-- Page 599 (Book page 579) -->
Chapter 14 : Enriching Fonts: Advanced Typography
• “Above-base mark positioning” (abvm), i.e., automatic positioning of diacritics that
appear above a letter. This feature is enabled by default.
• “Below-base mark positioning” (blwm), the counterpart of the preceding for marks
that appear below a letter. This feature is also enabled by default.
• “Mark positioning” (mark), which combines the previous two. Enabled by default.
• “[Diacritical] mark-to-mark positioning” (mkmk), the possibility of positioning dia-
critical marks over other diacritical marks. Enabled by default.
• “Cursive attachment” (curs), for joining letters in cursive scripts, such as Arabic or
calligraphic Latin.
• “Required feature” (RQD), a feature with no precise semantics that is nonetheless re-
quired for the given script and language.
Most of the time our choice will be made from mark, mkmk, and curs. Note: for the class
to be deﬁned and available for use in other windows, it is necessary to close the Font
Info window by clicking on OK.
Once we have deﬁned the glyph’s class, we can create an instance of it in the glyph win-
dow. We perform a contextual click where we wish to place it and then select the entry
Add Anchor Point. Doing so opens the Anchor Point Info window, where we can select
the anchor’s class from the pull-down menu. In each menu entry, we can see the feature’s
tag (ﬁrst) and the anchor’s name (last). We select the anchor’s role in this window:
• Is the anchor for a diacritical mark, so that the mark can be attached to a base glyph?
If so, we check Mark.
• Is the anchor for a ligature? Then we check Base Lig. In this case, we must also
specify the component index in the corresponding input area. (If a ligature is com-
posed of n letters, the component index is the sequential number of each component,
between 0 and n−1).
• Is the anchor for a base glyph? Then we check Base Glyph.
• Is the anchor for a diacritical mark, so that the mark can be attached to another
diacritical mark? Then we check Base Mark.
• Finally, is the anchor for the entry or exit point of a cursive attachment? Then we
check CursEntry or CursExit, respectively.
According to the type of anchor class that we choose, some of the choices will be disabled
because they are inapplicable.

<!-- Page 600 (Book page 580) -->

## 14.4 Managing OpenType Tables in FontForge

Figure 14-11: Left: the glyph window, “single substitution” tag. Right: the window for a new
single substitution.
Noncontextual Substitutions
In FontForge, we distinguish two types of substitutions: those that are independent of the
context and those that are contextual. The former are made at the glyph level, through
the Glyph Info window. The latter are deﬁned by way of the former at the same time as
contextual positionings, through the Font Info window.
Let us examine the various cases of noncontextual substitutions:
• Single substitutions, such as replacing the glyph g with another glyph, g.prettier.
We make a contextual click8 on the box for the ﬁrst glyph in the font window, and
from the menu that appears we select Glyph Info. In this window, as can be seen in
Figure 14-11, there are tabs for all types of noncontextual substitutions.
To create a single substitution, we click on the Glyph Info>Substitutions>New
button. A window entitled New Substitution Variant then appears, in which we
indicate the target glyph and the tag for the feature to which we wish to associate this
substitution (Figure 14-11, right).
On the pull-down menu for selecting feature tags, FontForge presents an enormous
list of predeﬁned features: all the predeﬁned OpenType and AAT features are found
there. Thus, if the substitution aims to replace a lowercase letter with a small capital,
we select Lowercase to Small Capitals, etc.
In the window for new substitutions, we can also select the script(s) and language(s)
to which the substitution applies. Finally, we can choose to disregard base glyphs,
ligatures, or diacritical marks.
8 Henceforth we shall use the term contextual click for a right-click under Unix and Windows and for a
click with a modifying key under Mac OS X. In Mac OS X, the modifying key associated with the right-click is
selected in the preferences of X11 or XDarwin.

::: tip Figure 14-11: Left: the glyph window, 'single substitution' tag. Right: the window for a new single substitution in FontForge
![Figure 14-11: Left: the glyph window, single substitution tag; Right: the window for a new single substitution in FontForge](/images/fonts-encodings/fig14-11.png)
*Figure 14-11: Left: the glyph window, 'single substitution' tag. Right: the window for a new single substitution in FontForge.*
:::


<!-- Page 601 (Book page 581) -->
Chapter 14 : Enriching Fonts: Advanced Typography
• Multiple substitutions, such as to replace the ligature f_f_t with its components. We
select the glyph in question and do exactly as for simple substitutions, with just two
diﬀerences: ﬁrst, we use Mult Subs tab instead; second, we enter the names of the
components, separated by spaces, in the Components area of the New Multiple
List window.
• Alternate substitutions, such as to oﬀer the user a choice of the glyphs a.old, a.odd,
a.pretty, a.ugly as alternate forms of a. Once again, we select the original glyph (a),
and from then on the procedure is the same, except that we select the tab Alt Subs
for this type of substitution and enter the names of the variant glyphs in the input
area of the New Alternate List window.
• Ligatures, such as to replace f and i with the glyph f_i. Again, we select the glyph
f_i, go to the Ligatures tab, and enter the glyph names of its components in the
appropriate area of the New Ligature window.
Thus FontForge’s interface is peculiar in that it sometimes starts with the input of the
substitution and sometimes with the output. For instance, in the case of a multiple sub-
stitution, we start with the original and enter the names of the glyph’s components in the
multiple-substitution window; conversely, for a ligature, we start with the target glyph—
that is, the ligature itself—and enter the names of the ligature’s components in the same
input area. For the former, the names are the names of the glyphs produced; for the latter,
they are the glyphs that produce the ligature.
Another peculiarity, found throughout FontForge, is that we must always associate a
feature tag with our substitutions at the time that we deﬁne them. To associate the same
substitution with more than one feature, we must redeﬁne it.
Contextual substitutions will be described later, together with contextual positionings.
Noncontextual Positionings
FontForge uses a rather diﬀerent approach for managing simple and pairwise position-
ings, cursive attachments, diacritical marks, etc. For positionings, we proceed as with
substitutions, using special tabs in the Glyph Info window. For cursive attachments and
the various operations connected to diacritical marks, we use anchors, as described on
page 577.
Here are the various types types of noncontextual positionings:
• Positioning of a single glyph, where we specify that a glyph is to be moved horizon-
tally and/or vertically. We select the glyph in the font window and request the Glyph
Info window. There we select the Positionings tab and click on New. The New Posi-
tion Variant window (Figure 14-12) opens, wherein we can select the horizontal and
vertical oﬀsets from the origin (¶X, ¶Y) and from the end of the displacement vector
(¶XAdvance, ¶YAdvance). These four numbers are the data for the glyph’s positioning.
We have good control over both the point at which the active glyph will be rendered

<!-- Page 602 (Book page 582) -->

## 14.4 Managing OpenType Tables in FontForge

Figure 14-12: The windows for simple (left) and pairwise (right) positionings.
(using its origin) and the point at which the following glyph will be rendered (using
the displacement vector). Next, as always, we select the tag for the feature with which
the positioning is associated and the relevant script and language, and we specify
whether the positioning should disregard base glyphs, ligatures, and/or diacritical
marks.
• Positioning of a pair of glyphs, where we specify that the members of certain pairs
of glyphs are to be moved horizontally and/or vertically. The procedure is the same,
except that the tab in the Glyph Info window is entitled Pairwise Pos and that
the New Pair Position window (Figure 14-12) that appears is slightly richer. Speciﬁ-
cally, here we are positioning not one but two glyphs. We must therefore indicate,
in addition to what is needed for a simple positioning, which glyph is the second
(the entry Second Glyph) and supply the data for its positioning (the origin and the
displacement vector). These are the only diﬀerences between the simple and pairwise
positioning windows. Note that horizontal kerning is a very special case of a pairwise
positioning: the case in which the only value changes is the ¶XAdvance of the ﬁrst
glyph, i.e., its set-width.
• Combining diacritical marks, for which we deﬁne marks, to be matched up by the ren-
dering engine, on both the base glyphs and the diacritics. This is done using anchors
of the same class for both diacritics and base glyphs. The features to which the po-
sitioning is associated, the script, and the relevant language are chosen through the
deﬁnition of the anchor’s class, under Font Info>Anchor Classes.

::: tip Figure 14-12: The windows for simple (left) and pairwise (right) positionings in FontForge
![Figure 14-12: The windows for simple (left) and pairwise (right) positionings in FontForge](/images/fonts-encodings/fig14-12.png)
*Figure 14-12: The windows for simple (left) and pairwise (right) positionings in FontForge.*
:::


<!-- Page 603 (Book page 583) -->
Chapter 14 : Enriching Fonts: Advanced Typography
• Multiple diacritical marks, where we place diacritics on other diacritics. We proceed as
with diacritics placed on base glyphs, but we specify that the anchor class is of type
Mk-Mk when we create it.
• Diacritical marks on ligatures, where we take the glyph for a ligature and deﬁne an an-
chor for each of the ligature’s components, so that diacritical marks can be attached
to it. Here again the procedure is the same, except that we may occasionally create
several anchors of the same class for the glyph. In that case, a sequential number is
attached to the class name. In the anchor-creation window, we specify that the glyph
is a ligature, and we enter the sequential number of the letter to which the anchor
corresponds.
• Cursive attachment, where we join the “exit point” of each glyph to the “entry point”
of the one that follows. Thus we must create two anchor classes, which we can call
“entry” and “exit”. When creating an instance of an anchor on the glyph, we choose
either “CursEntry” or “CursExit” as the anchor’s type, according to its class.
Contextual positionings are described in the following section, together with contextual
substitutions.
Contextual Substitutions and Positionings
Let us move on to contextual transformations. Here we use the Font Info window,
which is independent of any glyphs. In this window, we select the Contextual tab, which
contains subtabs corresponding to the various types of contextual transformations (see
Figure 14-13 [a]).
Whether for a simple, chained, or reverse chaining contextual transformation, the deﬁ-
nition procedure is the same. We select the appropriate tab and click on New. The usual
window opens (Figure 14-13 [b]), with the tag for the feature to which the transforma-
tion will be associated and our choices to respect or disregard base glyphs, ligatures, and
diacritical marks.
Once these choices have been made, another window opens, one with many tabs. We
use the Prev and Next buttons to move from tab to tab. The ﬁrst tab (Figure 14-13 [c])
asks us to choose one of three ways to display the transformation: do we wish to use
individual glyphs, glyph classes, or coverage tables (see §D.9.1.3)? Coverage tables are the
most practical choice, with the fewest limitations.
Suppose then that we have decided to display our substitution or our positioning in a
coverage table, which is the most attractive option. The second tab in the window (Fig-
ure 14-13 (d)) then displays the contextual transformation in a very abstract manner.
To understand it, let us ﬁrst answer one question: what are contextual substitutions and
positionings, whether chained or not?
We begin with a match—the string of n glyphs that the rendering engine will recognize
in order to launch the transformation. Let this string be denoted M = M0,... ,Mn−1. A

<!-- Page 604 (Book page 584) -->

## 14.4 Managing OpenType Tables in FontForge

(a)
(b)
(c)
(d)
Figure 14-13: The ﬁrst four steps for deﬁning a chained contextual substitution.

::: tip Figure 14-13: The first four steps for defining a chained contextual substitution in FontForge
![Figure 14-13: The first four steps for defining a chained contextual substitution in FontForge](/images/fonts-encodings/fig14-13.png)
*Figure 14-13: The first four steps for defining a chained contextual substitution in FontForge.*
:::


<!-- Page 605 (Book page 585) -->
Chapter 14 : Enriching Fonts: Advanced Typography
substitution consists of replacing some of the glyphs in M; a positioning consists of mov-
ing them. Suppose that we have a substitution (the logic for positionings is exactly the
same) and that we wish to replace the glyphs Mi and M j. Only these two glyphs will be
modiﬁed; all the others are there to “set the scene”, forming the context. The indexes of
the glyphs to be substituted are i and j. How can we perform this substitution? By means
of noncontextual substitutions: single ones, multiple ones, and ligatures.
Now let us increase the complexity a bit. We have said that we are going to display our
substitution through the use of coverage tables. That means that the M0,... ,Mn−1 that
we just saw are no longer glyphs but rather sets of glyphs Mk = {mk,0,... ,mk,ik}. The same
is true of Mi and M j, which are the glyphs that we are substituting.
To describe a substitution of this kind, we can simply specify which are the glyphs in
coverage tables M0,... ,Mn, which indexes in the coverage tables are to be substituted,
and, ﬁnally, which (noncontextual) substitutions will be applied to these indexes.
That is what FontForge does. We list the coverage tables, one by one, in the top part of
the window (Figure 14-13 (d)). In the bottom part of the window, we enter the indexes in
the table that are to be substituted and the tags for the substitutions that will be applied
to them. The substitutions must therefore have been deﬁned in advance—for each glyph
in the coverage table concerned.
How do we deﬁne coverage tables? By clicking on New, just below the match’s box, we
open an input area in which we can enter the glyph names of the elements in the table.
Two buttons facilitate this task: Set takes all the glyphs selected in the font window and
inserts them into our coverage table; Select does the opposite: all the elements in the
table are selected in the font window, so that we can check our glyph selections.
And how do we enter the indexes and tags for the substitutions to be applied? As easily as
can be: by clicking on the New button at the bottom. In the little window that appears,
we enter an index (a number between 0 and n−1, if the match contains n glyphs) and a
tag for an existing feature, which we select from a pull-down menu.
Let us take the example of ordinal numbers. We want the strings 1st, 2nd, 3rd, 4th, etc.,
to be replaced by “1st”, “2nd”, “3rd”, “4th”, etc. The feature that produced superscripts is
usually called sups. We must ﬁrst deﬁne simple substitutions to set the letters ‘s’, ‘t’, ‘n’,
‘d’, ‘r’, and ‘h’ as superscripts and then classify these substitutions under the feature sups.
Next we shall have to deﬁne four classes: a class for the number ‘1’, whose match is 1st or
1th (in the case of 11, 111, etc.), with three coverage tables: “[one]”, “[s t]”, and “[t h]”;9
similar classes for numbers ‘2’ and ‘3’, and one class for the other numbers, for which
there are three coverage tables: “[zero four five six seven eight nine]”, “[t]”,
and “[h]”.
For the ﬁrst of these classes, we shall enter in the ﬁrst input area:
9 That may cause a problem, since we transform not only “1st” and “1th” but also “1sh” and “1tt”. But who
would ever write those? They do not exist in English.

<!-- Page 606 (Book page 586) -->

## 14.4 Managing OpenType Tables in FontForge

one
s t
t h
Thus there are three sets of glyphs, and those that will be substituted are the second and
the third sets; i.e., those for superscripts 1 and 2. Then, in the second input area, we enter:
1 'sups'
2 'sups'
We proceed similarly for the second and third class. For the fourth class, we enter in the
ﬁrst input area:
zero four five six seven eight nine
t
h
and, in the second input area:
1 'sups'
2 'sups'
Now let us examine chained contextual transformations. The procedure is the same:
we select the tab Contextual>Chain Sub or the tab Contextual>Chain Pos in the
Font Info window, and in the same manner we reach the window in which we have
entered the match. Except that now there are two extra tabs at our disposal: Backtrack
and Lookahead.
The idea is as follows. We still have the same match, M = M0,... ,Mn−1; but this time,
when the rendering engine detects this match, it will also compare the glyphs that appear
before and after it. The backtrack will be a string P of glyphs (or coverage tables) that
must appear before the match in order for the transformation to take place. Likewise,
the lookahead, F, must appear after the match; otherwise the transformation will not
occur. The reader may be wondering why we do not say that the concatenation of P, M,
and F is just one big match. After all, it is not the whole match that is to be transformed
but just some of its glyphs. What diﬀerence does it make if the match is made larger?
There is a major diﬀerence that occurs not at the level of the transformations themselves
but rather at the level of the overall rendering. When the rendering engine reads the
string and detects a match for a contextual transformation, the match is “swallowed”
by the engine and cannot interact further with the rest of the string. For example, if a
hypothetical match ended with ‘f’ and were followed by ‘i’, these letters could not form
the ligature “ﬁ”. If, however, the ‘f’ is part of the lookahead, this problem will not occur,
since the lookahead “belongs to the future”: it has not yet been “read” when the trans-
formation takes place. After the transformation, the lookahead will be read as if nothing
had happened.

<!-- Page 607 (Book page 587) -->
Chapter 14 : Enriching Fonts: Advanced Typography
Thus chained contextual transformations allow us to reduce the match to a minimum
number of glyphs, often only those that are actually substituted or positioned, and to
leave the remained to the backtrack and the lookahead.
Let us take as our example of a chained transformation a chained contextual positioning:
the one for the string “V.A.V.” that we have already mentioned several times in this book.
We need to move the ‘V’ closer to the period that precedes it, but only if that period is
in turn preceded by an ‘A’. To kern the period and the ‘V’, we must ﬁrst deﬁne a (non-
contextual) pairwise positioning. Thus we select the “period” glyph (which is named
period) and click on New in the window Glyph Info>Pos. In the window for deﬁning
a simple positioning, we specify a ¶XAdvance of -300 and attach this positioning to a new
tag, e.g., skrn.
Now that we have deﬁned the positioning, we must incorporate it into its context by
deﬁning a chained contextual positioning. To do so, we click on New in the Font Info>
Contextual>Chain Pos window. Then we attach the positioning to the kern (hori-
zontal kerning) feature. Next, in the new window that opens, we choose to display the
positioning as coverage tables (Figure 14-13 [c]) and click on Next. This brings us to the
window for entering the match, the backtrack, and the lookahead.
In our case, one idea would be to take “A.V” as the match, but it turns out to be more
desirable to restrict ourselves to the period ‘.’ and to use ‘A’ as the backtrack and ‘V’ as
the lookahead. Accordingly, we select the appropriate tabs and enter the strings period,
A, and V, just as in the example for a contextual substitution. Finally, we must specify
which feature will be applied, and to which glyph, when the conditions speciﬁed in the
context are satisﬁed. To this end, we choose the index 0 to the string (after all, the match
has only one glyph) and specify skrn (which we have previously deﬁned for this purpose)
as the feature to execute. Nothing remains but to record our entries by clicking on OK,
and voilà!
Reverse chaining contextual substitutions are deﬁned in the same way, with the single
diﬀerence that we select the tab by this name in the Font Info window. The reader will
ﬁnd more information on the reasons for these very exotic substitutions in §D.9.4.7 of
this book.
Managing AAT Tables in FontForge
Up to now we have seen how the two main software packages (FontLab and FontForge),
as well as another piece of software that specializes in this task (VOLT), manage Open-
Type tables. But OpenType is not the only way to enrich a TrueType font. Recall that in
parallel with the work by Microsoft and Adobe on TrueType Open and OpenType, Apple
developed the TrueType GX format, which was latter rechristened AAT. Currently AAT
fonts can be used only under Mac OS X, but they are no less interesting for that. The
magniﬁcent font Zapﬁno

<!-- Page 608 (Book page 588) -->
Managing AAT Tables in FontForge
itself is reason enough for us to examine the possibilities of AAT fonts. The contextual
character of the Arabic and Indian fonts of the Mac OS X operating system is also man-
aged entirely by AAT.
One detail that is not insigniﬁcant: while OpenType fonts can be based on TrueType or
PostScript CFF outlines, AAT fonts can be based only on TrueType outlines.
In §D.11.5.1 of this book, we provide a rather exhaustive technical description of AAT
tables. In this section, we shall discuss only the insertion of these tables into TrueType
fonts.
For the moment, only FontForge has seriously confronted the problem.10 The problem
is in no way trivial, as AAT tables use ﬁnite automata to perform substitutions or con-
textual positionings. A ﬁnite automaton is a method that can be illustrated more easily
with diagrams, by drawing bubbles and arrows on a sheet of paper, than through the user
interface of software, through its menus, buttons, and input areas.
Not to mention that AAT also oﬀers variable fonts, in a format similar to and slightly
more powerful than Multiple Master.
Let us now describe, as simply as possible, FontForge’s user interface for creating AAT
tables.
Choosing between OpenType and AAT
No, this section will not present arguments for or against these two font formats; it will
instead give some very important information about fonts generated by FontForge.
When we generate a font, we select the font format on the pull-down menu in the dialog
box for saving ﬁles. Whether we wish to generate an OpenType or an AAT font, we select
TrueType (or TrueType (Mac dfont) under Mac OS X). Under the pull-down menu,
there is a button labeled Options. Clicking on this button brings up a window with a
number of checkboxes. Those of interest to us are Apple and OpenType. To obtain AAT
tables in the generated font, we must check the ﬁrst box. If we do, we are wise to uncheck
the second box, thanks to certain possible incompatibilities.
10 Doubtless because VOLT comes directly from Microsoft, a company with no interest in promoting AAT,
and because FontLab will probably ﬁrst cover the OpenType features completely before addressing AAT.

<!-- Page 609 (Book page 589) -->
Chapter 14 : Enriching Fonts: Advanced Typography
(a)
(b)
(c)
Figure 14-14: Editing the names of AAT features and selectors.
Features and selectors
Like OpenType, AAT also uses features, but
it enriches them by adding a new concept:
selectors. A selector is a series of proper-
ties that the user will enable or disable at
the same time as the feature. For example,
in the WorldText window shown opposite,
several features and selectors for the font
Charcoal are shown. The English version of
the software was used here, but since we
chose French from the pull-down menu
for language, the names of the features and
selectors are given to us in French. The example illustrates another clear advantage of
AAT fonts: the names of the features are contained within the font. For instance, the choice
of features available to the user is no longer the province of the software; it is now the
font’s responsibility. We can devise new features (and new selectors); they can be used
immediately in all Mac OS software.
FontForge allows us to edit the names of features and selectors in any language. In Fig-
ure 14-14 (a), we have selected the feature Ligatures (from the font Zapﬁno); FontForge
displays a list of all the translations of this name. In the bottom part of the window, we
see the names of the selectors, in French. Using the windows shown in Figure 14-14 (b)
and (c), we can modify existing translations or add new ones.
It is important to understand that only the names are deﬁned at this step. No information
about the features or selectors is given, with one exception: when we modify a selector

::: tip Figure 14-14: Editing the names of AAT features and selectors
![Figure 14-14: Editing the names of AAT features and selectors](/images/fonts-encodings/fig14-14.png)
*Figure 14-14: Editing the names of AAT features and selectors.*
:::


<!-- Page 610 (Book page 590) -->
Managing AAT Tables in FontForge
(window 14-14 [b]), we can check the box Enabled so that the selector will be enabled
by default when the font is selected.
How, then, can we deﬁne the properties of these features and selectors, with such beau-
tifully deﬁned names? In fact, the crucial data in the three windows in Figure 14-14 are
the small numbers that appear in the Feature _Id and Setting Id input areas. These are
the numbers that we shall later use to identify the pair (feature, selector).
One last detail about feature names before we move on to AAT’s ﬁnite automata. In
File>Preferences>Mac we have a tab allowing us to modify the default names of Ap-
ple’s predeﬁned features (see §D.11.5.1 for a detailed description) and a table of map-
pings between AAT features and their OpenType counterparts. This table will be used
when FontForge has to convert an AAT font to OpenType or vice versa.
### 14.5.2 Managing AAT's Finite Automata in FontForge
To the reader who is not familiar with the concept of ﬁnite automata, we highly recom-
mend reading section §D.13.1 of this book. She will ﬁnd a plethora of examples using
the same conventions and notations as the AAT tables.
Let us summarize the contents of that section. A ﬁnite automaton consists of three tables:
a table of states, a table of inputs, and a table of classes. States are the diﬀerent situations in
which the automaton may ﬁnd itself. Classes are the diﬀerent categories of glyphs that we
use. Inputs are pairs (“new state”, “action”). Actions are the operations that we perform
on glyphs.
For instance, we start from a default state (there are even two of them in AAT: state 0
is called “beginning of document”, and state 1 is called “beginning of line”). We remain
in the initial state as long as we have only glyphs that do not cause a state change. One
ﬁne day we encounter a glyph from another class. We then check the table of inputs
to see what we are to do in the current state, in the presence of this new glyph. The
table of inputs tells us that, for the given state and the given glyph class, we must move
to a certain other state and, possibly, perform a certain action. The actions depend on
the contextual table. For a morx table, there are ﬁve types of actions: rearrangements of
glyphs, contextual substitutions, ligatures, simple substitutions, and insertions of glyphs.
In the kern, for kerning, there is another action: contextual kerning.
Let us take a real-world example so as to give a better illustration of the technique of
ﬁnite automata in AAT: the example of most ordinal numerals in English (4th, 5th,
etc.). We begin by deﬁning three states: the “INITIAL” state, the “DIGITS” state and the
“T_FOUND” state. We start in the “INITIAL” state. When we write a digit, we switch to
the “DIGITS” state. When the following glyph is also a digit, we remain in the “DIGITS”
state. When the following glyph is a ‘t’, we go into the “T_FOUND” state. If the next
glyph is an ‘h’, we replace ‘th’ with ‘th’ and return to the initial state. If the next glyph is
not an ‘h’, we leave both the ‘t’ and that glyph as they are and return to INITIAL state.
For a human, the best way to describe a ﬁnite automaton is to reach for a good old
pencil and a sheet of paper, with which to draw arrows and bubbles—which is what we
have done below:

<!-- Page 611 (Book page 591) -->
Chapter 14 : Enriching Fonts: Advanced Typography
Then, when the diagram is complete, all the bubbles and arrows have been drawn, and
we have run through all the possibles paths, we must transcribe the diagram into the
three tables that we have mentioned (states, inputs, and classes). And that is where Font-
Forge comes in: it gives us an interface for entering the three tables.
Let us go to Font Info>Mac SM (for “Mac State Machines”). This tab has four subtabs,
which correspond to four operations11 requiring ﬁnite automata: rearrangement of glyphs,
contextual substitution, insertion, and kerning.
We shall examine them one by one. Let us start with the rearrangement of glyphs.
Rearrangement of glyphs
This is a very interesting transformation of the string of glyphs, as it has no counter-
part in OpenType. Speciﬁcally, in OpenType it is the Uniscribe driver that manages the
rearrangement of glyphs: for example, this driver places Indian vowels before a list of
consonants.
The idea behind the rearrangement of glyphs is as follows. We read a string G = g1,... ,gn
of glyphs, move from state to state, and at some point we decide to mark a glyph; call it gi.
We continue reading until we reach another glyph, g j, which will be the “initiator” of the
transformation. At that point, the substring gi,... ,g j will be run through the mill, and
some glyphs will be permuted. Which glyphs depends on a parameter that is given when
the initiator is reached: the simplest cases are those in which gi moves to the end and
those in which g j moves to the beginning. The more complex cases are those in which
the four glyphs gi,gi+1,g j−1,g j are permuted in diﬀerent ways, while the string in the
middle, gi+2,... ,g j−2, remains unchanged.
Let us now see how FontForge allows us to enter a transformation of this sort.
Take the example given, which may seem pointless to the Eurocentric user but in fact
simulates a transformation that is found in almost all the scripts of India: when there is a
sequence of consonants without vowels that is followed by an ‘r’, the glyph for the ‘r’ will
11 Note that one operation is missing from the morx table: ligatures. They are converted to OpenType
contextual ligatures when an AAT font is opened and converted back to AAT ligatures upon saving.

<!-- Page 612 (Book page 592) -->
Managing AAT Tables in FontForge
be placed at the beginning of the string of consonant glyphs. For instance, the Unicode
characters “KGPTHr” will produce a series “rKGPTH” of glyphs. Here, then, is what we
want: that an ‘r’ that appears after any number of occurrences of the letters ‘K’, ‘G’, ‘P’,
‘T’, and ‘H’ be moved to the beginning of that group of letters.
Let us attempt to think in terms of ﬁnite automata. The initial state is that of “beginning
of document” or “beginning of line”. As long as we are reading characters other than
consonants, we remain in the initial state. But as soon as we read a consonant, we know
that an ‘r’ may eventually appear and force a permutation. Thus we go to the “waiting
for an ‘r”’ state, which we can also call the “consonants” state. Once we are in the “con-
sonants” state, we remain there as long as we keep reading consonants. But that state is
left as soon as anything other than a consonant or an ‘r’ occurs: we then move back to
the initial state. Finally, if an ‘r’ appears, we also return to the initial state, but this time
we ﬁrst launch the permutation. One question arises: how can we know exactly where
to place the ‘r’? Because we took care to mark the location when we moved from the
initial state to the “consonants” state. Thus we shall say that the ‘r’ will go just after the
last mark in the text. That’s right: the “last” one, since each consonant in the text will
cause a transition to the “consonants” state and will thus make a mark, but only the last
mark is of interest to us.
Let us summarize what we have seen. We have three classes: consonants (‘K’, ‘G’, ‘P’,
‘T’, etc.), the letter ‘r’, and everything else. We have two states: the initial state and the
“consonants” state. We have two ways to leave the initial state: when we read a consonant
(and thus move to the “consonants” state after marking the location), and when we read
any other glyph (and thus remain in the initial state). We have three ways to leave the
“consonants” state: when we read a consonant (and thus remain in the same state), when
we read an ‘r’ (in which case we return to the initial state after permuting the glyphs),
and when we read a glyph of another type (and thus return to the initial state).
Graphically, the procedure can be shown as two bubbles (for the two states), two arrows
going out of the ﬁrst bubble, and three arrows going out of the second. Here is the dia-
gram in question:
if non-letter
if ‘K’, ‘G’, ...
if other glyph
if ‘r’
if ‘K’, ‘G’, ...
keep,
mark
keep
keep, permute
keep
keep
initial state
consonant
K, G, P, etc.
➀ 
➁ 
➂ 
➃
➄
Now let us convert the diagram for use with FontForge’s interface. First of all, we must
create an AAT feature. To do so, we go to Element>Font Info>Mac Features and click
on New. In the window that appears, we enter the number of the feature and its name,
in at least one language (it is politically correct to enter the name in multiple languages).

<!-- Page 613 (Book page 593) -->
Chapter 14 : Enriching Fonts: Advanced Typography
Likewise for the selector: we enter the number and, in at least one language, the name.
We can also check the Enabled box. After this step, the feature exists—but it does not yet
do anything. Make note of the numbers assigned to the feature and the selector: 5 and 1.
(a)
(b)
(c)
Figure 14-15: (a), The input window for the class and state tables for a rearrangement of glyphs
in AAT; (b) and (c), the input windows for the entries (state 0, class 4) and (state 2, class 5).
Then we select the Mac SM tab and choose the Indic subtab. We click on New, and
window 14-15 (a) comes up.
At the top, we enter the numbers of the feature and the selector: <5,1>. Below, we go into
the glyph classes that we shall use. The ﬁrst four classes are predeﬁned in AAT, and Font-
Forge displays them by default. We shall go into the “K P T G H” and “r” classes by
clicking on New.
Next comes the most delicate operation. We must ﬁll in the state table, which appears
at the bottom. For the moment, there are only the two initial states: 0 (“beginning of
document”) and 1 (“beginning of line”). When we designed the automaton, we provided
only one bubble for the initial state; but that does not matter, as in our example the two
initial states will have exactly the same behavior. On the other hand, we do need a new
state, for the state that we have called “consonants”. How do we reach that state? When
the automaton reads an element in the class “K P T G H”, i.e., class 4. Thus it is from the
box “class 4, state 0” that we shall move to the new state, which does not yet exist. Let us
click on this box!

::: tip Figure 14-15: (a) The input window for the class and state tables for a rearrangement of glyphs in AAT; (b) and (c) the input windows for contextual glyph substitutions
![Figure 14-15: Class and state tables for rearrangement of glyphs in AAT](/images/fonts-encodings/fig14-15.png)
*Figure 14-15: (a) The input window for the class and state tables for a rearrangement of glyphs in AAT; (b) and (c) the input windows for contextual glyph substitutions.*
:::


<!-- Page 614 (Book page 594) -->
Managing AAT Tables in FontForge
A window for editing the state transition (see §14-15 [b]), i.e., the shift from one state to
another, appears. In this window, we must enter the number of the target state, which
in our case is 2. As if by magic, state 2 appears in the table. Let us also perform the same
operation for the box “class 4, state 1”. We then obtain the arrow  of our diagram. Do
not forget to check the box Mark Current Glyph As First. Thus the consonant that
brought us to the “consonants” state and that must necessarily be the ﬁrst glyph is so
marked.
Next, we shall click on the box “class 4, state 2”: we are then in “consonants” state, and
there is a new consonant that has been read. Thus we remain in this state. Here we must
absolutely not check the box for the “ﬁrst glyph”!
Finally, the most interesting box: “class 5, state 2”. This is where an ‘r’ appears, after any
number of consonants. Here we must mark the glyph as being the “last” so that it will
initiate the permutation operation. Next, from the pull-down menu, we select the per-
mutation that we desire from the following list of choices: Ax => xA, xD => Dx, ... ABxCD
=> DCxBA. This bizarre notation can be explained as follows: A is the ﬁrst glyph, B is the
second (if any), D is the last, C is the next-to-last (if any), and x is the string that appears in
the middle, which can be arbitrarily long. In our case, we want the permutation xD =>
Dx, since we are taking the ‘r’, which is the last glyph, and placing it at the beginning.
We have just ﬁnished deﬁning the ﬁnite automaton. Note, incidentally, that unlike
OpenType features, AAT features allow us to use strings of arbitrary length (within the
limits of a line of text, as the shift to a new line always returns us to the initial state). In
OpenType, we would need a separate substitution for each string length.
Contextual substitutions
Now let us proceed to another type of operation: contextual substitution. Here the goal
is to replace certain glyphs with others, according to context, through the use of a ﬁnite
automaton. Once again we shall take a typical example of ﬁnite automata that cannot
be implemented in OpenType: fractions. In OpenType, we must specify the numerator
and the denominator of a fraction separately. Here we shall write an AAT transformation
that will convert the digits before the slash into the numerator and those after the slash
into the denominator—however many digits there be!
What are our glyph classes? On the one hand, we have “digits” (the glyphs that will be put
into the numerator or the denominator); on the other hand, we have the “slash” (which
will initiate the change from numerator to denominator). And what are our states? Start-
ing in the initial state, as soon as we detect a digit, we switch to the “numerator” state.
Then, as soon as we detect a slash, we switch to the “denominator” state, and we remain
there as long as we keep reading digits. Finally, after the last digit, we return to the initial
state. In addition, if in the “numerator” state we read a glyph that is neither a digit nor
a slash, we also return to the initial state:

<!-- Page 615 (Book page 595) -->
Chapter 14 : Enriching Fonts: Advanced Typography
if non-digit
if slash
if digit
if non-digit
if digit
if neither
digit not
slash
initial state
Numerator
Denominator
if digit
Now all that we have to do is to implement the ﬁnite automaton. We shall ﬁrst create an
AAT feature under Element>Font Info>Mac Features, just as in the previous section.
Let <11,2> be its identiﬁer.
In the editing window for contextual substitutions,
we shall then enter the data for the three tables. Let
us start with the class table: after the four default
classes (0–3), we shall deﬁne a class 4 (the digits,
zero
one
two
three
four
five
six
seven
eight nine) and a class 5 (the slash, slash). Next,
we shall ﬁll in the relevant boxes in the table of
inputs. Let us ﬁrst take class 4 (the digits): when we
encounter a digit in the initial state, we switch to a
new state, which will be state 2 (which we just called
“numerator”). At the same time, we replace the
glyph for the number with its superscript version.
Then we must indicate the simple substitution that
will produce superscript digits. This substitution
must be deﬁned for each digit. We shall therefore
select, in the font window, the glyph for the digit
zero and, in Glyph Info>Substitutions, we shall
create a new substitution by specifying the name
of the superscript zero—say, zero.superscript.
There is one technical detail that we absolutely
must respect: we must choose “--
Nested
--”
as the script/language on the pull-down menu. The
feature tag may be anything; for instance, G001.
Next we create a new simple substitution in the same way: that for the subscript form,
which we shall call G002. These two operations should be repeated for all the digits.
Now let us return to the table of inputs. We had been in class 4 (the digits). When we
come upon a digit in state 0 (or state 1), we move to state 2 (“numerator”) after replacing
the digit with its superscript version. Let us then click on the box (state 0, class 4). In the
window that appears, we indicate that the new state is 2 and that the substitution that
applies to the current glyph is G001.

<!-- Page 616 (Book page 596) -->
Managing AAT Tables in FontForge
In this window, we also see a box to check (Mark Current Glyph) and an input area
for the feature tag, entitled Mark Subs. What is the purpose of these? Let us digress
for a moment to explain the usefulness of marking. We have seen that the matches for
OpenType transformations can have contexts before and after the current glyph. Thus
we can replace a glyph when it is followed by certain other glyphs. But it is hard to see
how to do so when using a ﬁnite automaton: after all, when we are in a position to say
that one glyph is followed by certain others, it is too late to modify the glyph; we have
already passed it by. That is where marking comes into play. We mark a glyph that may
later be subject to transformation, and when the appropriate context arises, we request
that a substitution be applied to the glyph that we have marked.
Let us return from this digression to the table of inputs. The box “state 1, class 4” is in
every way identical to the preceding one. So is state 2, since any digit that appears when
we are in state 2 is also subject to a substitution, and we move on to the next glyph. To
exit state 2, we need to encounter a slash. Let us now handle class 5 (the slash). The only
box of interest to us is “state 2, class 5”: it sends us to state 3 (“denominator”). There is
no need to apply a substitution, unless, of course, there is a special glyph in the font for
a slash that was speciﬁcally designed for oblique fractions.
Only state 3 remains. The only interesting box is “state 3, class 4”, where we stay in state 3
and replace the digit with its subscript form (tag G002).
This concludes the writing of the contextual substitution.
Insertion
Insertion is an AAT feature that has no analogue in OpenType—other than a few simple
cases of insertion that can be achieved through multiple substitutions. The goal is to
insert some glyphs between the marked glyph and the current glyph, just as if the user
had entered them. But beware: the glyphs that appear are not characters; they do not exist
in the ﬁle. Does the operating system consider them as real glyphs? Can we ﬁnd them by
searching for a string? The author is doubtful. They should therefore be used sparingly:
using an insertion to replace the author’s initials with his full name would be clever but
potentially dangerous. Instead, we should set things up so that the inserted glyphs are of
less importance or, at a minimum, cannot possibly be mistaken for characters. Here are
two typical examples:
+
ligature
split insertion
insertion of kashida
At the left, we have an insertion of a kashida, which is a connecting stroke between Arabic
letters. The result is inferior typography, but often there is no better solution. After all,
true long strokes that connect Arabic letters must be curves, and that is already beyond
the capabilities of most typesetting systems. In any event, the kashida has one peculiarity:
it is not a letter in its own right but a deformation of a letter. If we obtain kashidas by

<!-- Page 617 (Book page 597) -->
Chapter 14 : Enriching Fonts: Advanced Typography
adding glyphs, that fact should not be evident to the user. In particular, the user should
not be able to select a kashida with the cursor.
The example on the right, by contrast, is that of the Cambodian script, in which vowels
are often split into two: one part remains in the logical (and phonetically correct) loca-
tion of the vowel, and the other part is moved before the group of consonants, just like
the Indian ‘r’ in our example of rearrangement.
Thus the left side of the glyph becomes detached and, at least
in the technical sense, becomes a glyph in its own right.
How will this “phantom” glyph interact with the user? Is it
possible to select it with the cursor? That depends, of course,
on the operating system; but one thing is certain: we cannot
apply the same rules as for the kashida. Speciﬁcally, the latter
are joined to the current glyph, but in the Cambodian script
the glyph to be inserted is quite far from the current glyph.
What, then, shall we do?
AAT solves this problem very simply by saying: in the ﬁrst
case, we shall say that the inserted glyph(s) behave like the
kashida. We must specify this behavior when we deﬁne the in-
sertion, both for the current glyph and for the marked glyph
(which could behave diﬀerently).
We must also specify which glyphs are to be inserted and where to put them. In fact,
we have the possibility of inserting diﬀerent strings of glyphs before or after the marked
glyph and before or after the current glyph.
All of these choices are presented to us in the interface for editing transitions in Font-
Forge. In the Mark Insert and Current Insert input areas, we enter the strings of glyphs
to insert, respectively, after the marked glyph (or before the marked glyph, if Insert Be-
fore Marked Glyph is checked) or after the current glyph (or before the current glyph,
if Insert Before Current Glyph is checked). The glyphs to be inserted are described by
their names separated by spaces, as we did above for glyph classes. We can insert up to
31 glyphs.
Kerning
Apple wanted to be innovative and oﬀer kerning for eight glyphs at the same time. That
certainly covers our celebrated string “S.A.V.”, and many other more complicated situ-
ations. How does it work? The window for inputs appears, just as with any other AAT
ﬁnite automata, with the single diﬀerence that there is no possibility of choosing a fea-
ture or a selector: Apple considers that kerning “transcends” features and that it should
always be enabled by default. Likewise, for Apple, there is only one way to perform kern-
ing, and therefore the notion of a selector does not apply.
What do we do, then? We ﬁll in the glyph classes, as usual. The state-transition window
allows us to enter four pieces of data, including the two classic ones: what is the next
state? and should we process the current glyph immediately or wait until we reach the

<!-- Page 618 (Book page 598) -->
Managing AAT Tables in FontForge
new state? The checkbox Push Current Glyph allows us to store a series of glyphs (up to
eight). These glyphs are retained in memory so that they can be “popped”. When n glyphs
are popped, n−1 kerning values are applied to them simultaneously. The kerning values
are entered in the input area at the bottom.
Each of these kerning values is therefore a path on which we
have gone through as many states as there are glyphs in the
string to be kerned: to kern A.V, we have the classes A (and
Agrave, Lambda, etc.), period (and comma, etc.), and V (and W,
etc.). When we read an A, we leave the initial state for state 2,
and we place an A on the stack. When we read a period, we
leave state 2 for state 3 and place period on the stack. When
we read a V, we leave state 3 to return to the fold by popping
the three glyphs and applying to them the kerning values 0 -
400.

<!-- Page 619 (Book page 599) -->
