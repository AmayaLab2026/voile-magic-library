---
title: "Introduction: Explorations"
description: "Unabridged English text from Yannis Haralambous, Fonts & Encodings: The Letter and Its Parts, Letterpress Typesetting, Digital Typesetting, Font Formats, Between Characters and Glyphs, and Book Structure."
---

# Introduction: Explorations
**By Yannis Haralambous, Ph.D. (Translated by P. Scott Horne)**
*From Fonts & Encodings (O'Reilly 2007), pp. 1–26*

---

```text
Introduction
Homo sapiens is a species that writes. And among the large number of tools used for
writing, the most recent and the most complex is the computer—a tool for reading and
writing, a medium for storage, and a means of exchanging data, all rolled into one. It has
become a veritable space in which the text resides, a space that, as MacLuhan and others
correctly predicted, has come to transcend geographic barriers and encompass the entire
planet.
Within this digital space for writing, fonts and encodings serve fundamentally different
needs. Rather, they form an inseparable duo, like yin and yang, Heaven and Earth, theory
and practice. An encoding emerges from the tendency to conceptualize information; it
is the result of an abstraction, a construction of the mind. A font is a means of visually
representing writing, the result of concrete expression, a graphical construct.
An encoding is a table of characters—a character being an abstract, intangible entity. A
font is a container for glyphs, which are images, drawings, physical marks of black ink on a
white background. When the reader enters the digital space for writing, he participates in
the unending ballet between characters and glyphs: the keys on the keyboard are marked
with glyphs; when a key is pressed, a character is transmitted to the system, which, unless
the user is entering a password, in turn displays glyphs on the screen. To send an email
message is to send characters, but these are displayed to the recipient in the form of glyphs.
When we run a search on a text file, we search for a string of characters, but the results
are shown to us as a sequence of glyphs. And so on.
For the Western reader, this perpetual metamorphosis between characters and glyphs remains on the philosophical level. That is hardly surprising, as European writing systems
have divided their fundamental constituents (graphemes) so that there is a one-to-one
correspondence between character and glyph. Typophiles have given us some exceptions
that prove the rule: in the word “film” there are four letters (and therefore four characters) but only three glyphs (because the letters ‘f’ and ‘i’ combine to form only one
glyph). This phenomenon, which is called a ligature, can be orthographically significant
(as is the case for the ligature ‘œ’, in French) or purely aesthetic (as with the f-ligatures
‘fi’, ‘ff’, ‘ffi’, etc.).
In any case, these phenomena are marginal in our very cut-and-dried Western world.
In the writing systems of the East, however, the conflict between characters and glyphs
becomes an integral part of daily life. In Arabic, the letters are connected and assume
```

```text
Introduction
different forms according to their position in the word. In the languages of India and
Southeast Asia, they combine to form more and more complex graphical amalgamations. In the Far East, the ideographs live in a sort of parallel universe, where they are
born and die, change language and country, clone themselves, mutate genetically, and
carry a multitude of meanings.
Despite the trend towards globalization, the charm of the East has in no way died out; its
writing systems still fire our dreams. But every dream is a potential nightmare. Eastern
writing systems present a challenge to computer science—a challenge that goes beyond
mere technical problems. Since writing—just like images, speech, and music—is one of
the fundamental concerns of humanity, computer science cannot approach it haphazardly: Eastern writing systems must be handled just as efficiently as the script that is part
of our Latin cultural heritage. Otherwise, some of those writing systems may not survive
computerization.
But more is at stake than the imperatives of cultural ecology. The French say that “travel
educates the young”. The same goes for writing: through thinking about the writing systems of other cultures and getting to know their problems and concerns, we come to
know more about our own.
Then there is also the historical perspective: in the digital space for writing that we are
exploring in this book, the concepts and techniques of many centuries dwell together.
Terminology, or rather the confusion that reigns in this field, clearly shows that computer science, despite its newness, lies on a historical continuum of techniques and practices. For example, when we set type in Times Ten at 8 points, we say that we are using a
“body size of 8 points” and an “optical size of 10 points”. Can the same characters have
two different sizes? To understand the meaning of these terms, it is necessary to trace the
development of the concept of “type size” from the fifteenth century to the PostScript
and TrueType fonts of our modern machines.
So far we have briefly surveyed the three axes on which this book is based: the systemic
approach (abstraction/concrete expression, encoding/font, character/glyph), geographicity
(East/West), historicity (ancient/modern, mechanical/computerized processes). These
three aspects make up the complexity and the scope of our subject, namely the exploration
of the digital space for writing.
Finally, there is a fourth axis, less important than the previous three but still well
grounded in our day-to-day reality, which is industrial competition. A phenomenon that
leads to an explosion in technologies, to gratuitous technicality, to a deliberate lack of
clarity in documentation, and to all sorts of other foolish things that give the world of
business its supposed charm. If we didn’t have PostScript fonts and TrueType fonts and
OpenType fonts and Apple Advanced Typography (AAT) fonts, the world might be a
slightly better place and this book would be several hundred pages shorter.
In this regard, the reader should be aware of the fact that everything pertaining to encodings, and to fonts in particular, is considered to be industrial knowledge and therefore
cannot be disseminated, at least not completely. It is hard to imagine how badly the
“specifications” of certain technologies are written, whether because of negligence or
```

Explorations
out of a conscious desire to prevent the full use of the technologies. Some of the appendices of this book were written for the very purpose of describing certain technologies
with a reputation for inaccessibility, such as AAT tables and TrueType instructions, as
clearly and exhaustively as possible.
In the remainder of this introduction, we shall outline, first of all, the jargon used in the
rest of the book, so as to clarify the historical development of certain terms. This will
also enable us to give an overview of the transition from mechanical to computerized
processes.
Next, we will give the reader a synthetic view of the book by outlining several possible
ways to approach it. Each profile of a typical reader that we present is focused on a specific
area of interest, a particular way to use this book. We hope that this part of the introduction will allow the reader to find her own path through the forest of 2.5 million letters
that she is holding in her hands.
Explorations
When one walks around a new city for the first time, one discovers places, acquires a
better understanding of the reasons behind certain historical events, and puts together
the pieces of the puzzle that make up the city’s environment. Here we shall do the same.
Our first stroll through the digital space for writing that we plan to explore will allow
us to take inventory of concepts and techniques, establish our terminology, and briefly
outline the conflict between the mechanical and the electronic.
Let us set aside for the moment the geographical axis and begin with a very specific case
of a glyph that comprises the molecular level of our space: the (Latin) letter.
The Letter and Its Parts
The terminology for describing the letter as a design varies greatly from one writer to
the next—a phenomenon, incidentally, that affects all terminology in the entire field of
typography. In Figure 0-1, we have listed in roman type the terms that are used in this
book and in italics some other terms that exist for the same parts of letters. Thus a stem
is also called a stroke or a downstroke.
These terms come from a variety of sources: the calligrapher’s technique (stroke, terminal), the engraver’s art (counter), geometry (apex, vertex), analogy or anatomy (arm, eye,
ear, tail, shoulder), mechanics or architecture (finial), etc.
The most important among them are:
• The stem, or stroke: a thick vertical or diagonal line found in such letters as ‘H’, ‘l’, ‘N’,
and ‘v’. If the letter is lower-case, or small, two possibilities may occur:
– the stem extends upward to the same height as the capitals or even higher, as in
the letters ‘b’, ‘d’, ‘h’, etc. This upper part of the stem is called an ascender.

::: tip Typographical Specimen Plate (Figure 0-1)
![Figure 0-1: The parts of a letter](/images/fonts-encodings/fig0-1-parts-of-a-letter.png)
*Figure 0-1: The parts of a letter.*
:::

![Figure 0-1: The parts of a letter](/images/fonts-encodings/fig0-1-parts-of-a-letter.png)
*Figure 0-1: The parts of a letter.*

Introduction
Apex
Vertex
Bar,
crossbar
Bar, crossbar,
cross stroke
Stem,
stroke,
downstroke
Head serif,
wedge serif
Bowl
Bowl
Counter
Counter
Tail
Ear,
spur
Bulb,
pear-shaped
terminal
Diagonal,
leg
Diagonal
Diagonal
Descender
Ascender
Aperture, inner space
Link
Loop
Serif
Serif
Serif
Serif
Serif
Foot, terminal spur
Foot, finial
Stem
Arch, shoulder
Figure 0-1: The parts of a letter. The terms used in this book are in roman; alternative terms are
shown in italics.
– the stem passes beneath the baseline, as in the letters ‘p’ and ‘q’. This lower part
of the stem is called a descender.
• The bowl, which is a full circle, as in ‘O’, or the greater part of a circle, as in ‘q’.
• The counter, which is the inner part of a letter; for example, the space inside an ‘o’,
an ‘O’, a ‘D’, etc. The counter of an ‘e’ is commonly called an eye. When the letter is
open at one end, as is the case with ‘n’, we speak instead of an aperture.
• The arm, a thin horizontal stroke that is open at one end, as the two arms atop a ‘T’
and the upper and lower arms of an ‘E’.

Explorations
• The crossbar (or bar), which is a thin horizontal connecting stroke, as in ‘A’ and ‘H’.
A horizontal stroke that crosses a vertical one, as in ‘f’ and ‘t’, is also called a cross
stroke.
• The serif, which is the “pedestal” at the bottom and top of the vertical strokes and
at the ends of some horizontal strokes. Thus the letter ‘I’ has two serifs, while the
letter ‘H’ has four. The left part of an upper serif that appears on some letters, a
remnant of the short lead-in made by the pen where it touches the paper before
a downstroke, is called a head serif. It is the head serif that distinguishes ‘l’ from ‘I’,
for example. In humanist and garalde typefaces (see Chapter 11), the head serif is
slanted, whereas it is perfectly horizontal in didones.
• The terminal, which is the opposite of the head serif: it is the movement of the pen
that finishes the letter. Again, it is a half-serif, this time the right side of the serif, and
it occurs primarily at the baseline.
If these terms apply just as well to traditional as to digital typography, that is because
they refer to abstract graphical characteristics.
Now that we have named the components of letters, we can explore ways to describe them precisely. How do we describe the proportions of letters, their graphical
characteristics—in short, everything that distinguishes one typographic character from
another?
There are two answers to that question: that of the professional, which is to say that of the
craftsman (engraver of characters, typographer) or other typographic specialist (historian),
and that of the mathematician.
In the first case, we study the letterforms according to their history, the cultural context
behind their creation and their use, and their development over time relative to the
development of Western culture. To this approach we have devoted Chapter 11, which
presents the history of typographic characters and one classification of them from a point
of view that is more historical and cultural than formal and geometric.
The second case, that of the mathematician, involves the study of letters as geometric
shapes. This approach is hardly new.1 In Figure 0-2 we see four studies of the Latin alphabet, corresponding to two eras and three countries: the first was made by an Italian
humanist, Friar Luca de Pacioli, from his work Divine Proportion [273], published in
Venice in 1509. The second comes to us from the hands of the great German engraver Albrecht Dürer and is dated 1535. It presents different models of alphabets in a work whose
title is less ambitious than that of Pacioli: Instructions on Measurement [124]. The third
dates from 1524 and is from France: it is the manual of Geofroy Tory, a great Parisian
humanist to whom we also owe the use of the accents and the cedilla in the French language. His descriptions appear in his finest work, the Champ fleury, au quel eNt contenu Lart
& Science de la deue & vraye Proportiõ des Lettres Attiques (“The Floured Feelde, wherein be
1 Readers who wish to know more about the history of the mathematical description of letterforms are
encouraged to consult Donald Knuth [221, p. 48] and Jacques André [35].

::: tip Typographical Specimen Plate (Figure 0-2)
![Figure 0-2: Six mathematical descriptions of the letter 'E'](/images/fonts-encodings/fig0-2-mathematical-descriptions-letter-e.png)
*Figure 0-2: Six mathematical descriptions of the letter 'E'.*
:::

![Figure 0-2: Six mathematical descriptions of the letter 'E'](/images/fonts-encodings/fig0-2-mathematical-descriptions-letter-e.png)
*Figure 0-2: Six mathematical descriptions of the letter 'E'.*

Introduction Figure 0-2: Six mathematical descriptions of the letter ‘E’: Luca de Pacioli (1509), Albrecht Dürer (1535), Geofroy Tory (1524), the Jaugeon Commission (1716), and two screenshots from the software package FontLab (today).

Explorations contayned the Arte & Scyence of the iufte and true Proporcion of Atticke Letters”) [332]. Finally, in 1716, as a result of an undertaking by Louis XIV, the Jaugeon Commission drafted the design for a royal script, entirely geometrical in nature, called the Romain du Roi [276] (“the King’s roman”). Many things strike us from an examination of these four examples. First of all, we notice that, in all four instances, the artists wished to place their letters within perfect squares, in the same way as the characters of the Far East. We also notice that they use finer and finer Cartesian grids in order to obtain more precise mathematical descriptions. While Tory uses a grid of 10×10 squares, the Jaugeon Commission resorts to 6×6 small squares within 8 × 8 large ones, for a total of 48 × 48—2,304 squares in all, which was an enormous degree of precision for the time. While the challenge was originally of a humanist nature (in the fifteenth century, when perspective was invented, Europeans began to wonder about the relationship between beauty and mathematics), it became one of power (Louis XIV took control of everything in his kingdom, right down to the microscopic level) and, finally, in the twentieth century, one of technology. Why? Because these mathematical descriptions of letters are the precursors of the digital fonts of today, defined on a grid of 1,024×1,024 (PostScript) or 4,096×4,096 (TrueType) squares, or even more. There is only a difference of mathematical scale: whereas the letters in the first four examples are described by circles and lines in the manner of Euclid (“with straightedge and compass”), today’s fonts use curves defined by third-degree polynomials that were introduced by the French engineer Pierre Bézier (see Appendix G). In the last two examples in Figure 0-2, we see two contemporary approaches to the design of glyphs: they are screenshots from the software system FontLab. What is the situation today? Have Bézier curves extinguished the little flame that is the genius of the master engraver? Quite the opposite. We use Bézier curves today because we have interactive tools that allow modern designers to create fonts worthy of their predecessors. We have devoted Chapters 12 to 14 and Appendix F to the description of the best available tools for creating fonts. Letterpress Typesetting In the previous section, we discussed the individuals that populate the digital space for writing: letters. But this space would be quite sad if each letter lived all by itself in its own little bubble. Far from being so isolated, letters, and more generally glyphs of all kinds, are highly social creatures. They love to form little groups (words), which in turn form larger and larger groups (lines, paragraphs, pages, books). We call this process typesetting. And the human who weaves the fates of the letters together to form structures on a higher level is a typesetter. Having come to this point, we can no longer content ourselves with the abstraction in which the previous section indulged. The way in which we put letters together depends on the technology that we use. It is therefore time to abandon the realm of the abstract

Introduction Figure 0-3: An eighteenth-century type case (from the Encyclopédie of Diderot and d’Alembert).

::: tip Typographical Specimen Plate (Figure 0-3)
![Figure 0-3: An 18th-century French type case](/images/fonts-encodings/fig0-3-eighteenth-century-type-case.png)
*Figure 0-3: An 18th-century French type case.*
:::

![Figure 0-3: An 18th-century French type case](/images/fonts-encodings/fig0-3-eighteenth-century-type-case.png)
*Figure 0-3: An 18th-century French type case.*

```text
Explorations
beauty of letters and to come down to earth to describe the mechanical process of typesetting. For computerized typesetting is based on mechanical typesetting, and the terms
that we use today were invented by those people whose hands were indelibly blackened,
not with oil (the liquid that pollutes our ecosystem), but with printer’s ink (the liquid
that bears wisdom).
Let us therefore quickly review the manual setting of type for the letterpress, which was
used from the fifteenth century until the end of the nineteenth, when the Linotype and
Monotype typesetting machines made their appearance.
Letterpress printing is based on movable type, little metal blocks (sorts) made from an
amalgam of lead, zinc, and antimony that have on one side a mirror image of a letter,
carved in relief. In Figure 0-3, taken from the Encyclopédie of Diderot and d’Alembert,
we see at the top a type case containing type and, below it, the table that supports the
different cases from which type is taken for composition. The top half of the case, the “upper case”, contains the capital letters, the small capitals, and certain punctuation marks;
the bottom half, the “lower case”, contains the small letters (called “lowercase” for this
very reason), the numerals, and various “spaces” (blocks of lead with no letter carved
into them that serve to separate words). We can see how type is arranged in the case. Of
course, the arrangement varies from country to country according to the frequency of
letters in the dominant language.
Figure 0-4: A composing stick (from the Encyclopédie of Diderot and d’Alembert).
The typesetter takes type sorts out of the case and places them on a composing stick, which
is illustrated in Figure 0-4. A whole line at a time is prepared on a composing stick. The
width of the composing stick is that of the measure of the page; thus the typesetter knows
when he has reached the end of the line and can take appropriate action. He can decide
to divide the word or to fill out the line with thin strips of extra spacing between the
words to extend it to the full measure.
When the line is ready, the typesetter adds it to the other lines of the page, eventually
inserting horizontal strips of lead, called leading, between the lines. At the bottom of
Figure 0-5, there are three lines that are set in this fashion:
Gloire à DIEU.
Honneur au ROI.
Salut aux Armes.
In this example, we can notice several tricks that enable us to overlap the faces of letters.
First, the face of the italic ‘H’ in the second line extends beyond the body of the type sort
```

::: tip Typographical Specimen Plate (Figure 0-4)
![Figure 0-4: A composing stick](/images/fonts-encodings/fig0-4-composing-stick.png)
*Figure 0-4: A composing stick.*
:::

::: tip Typographical Specimen Plate (Figure 0-5)
![Figure 0-5: Three lines of movable type in a composing stick](/images/fonts-encodings/fig0-5-three-typeset-lines.png)
*Figure 0-5: Three lines of movable type in a composing stick.*
:::

![Figure 0-5: Three lines of movable type in a composing stick](/images/fonts-encodings/fig0-5-three-typeset-lines.png)
*Figure 0-5: Three lines of movable type in a composing stick.*

![Figure 0-4: A composing stick](/images/fonts-encodings/fig0-4-composing-stick.png)
*Figure 0-4: A composing stick.*

```text
Introduction
Figure 0-5: Three typeset lines (from the Encyclopédie of Diderot and d’Alembert).
and reaches over the ‘o’ that follows. This overlapping, called kerning, is indispensable,
since italic letters are not slanted but occupy upright parallelepipeds. The italic ‘I’ also
kerns with the following letter.
Another trick: the lower parts of the faces of the letters are cut on an angle. The benefit
of this device is that it permits the vertical kerning of certain letters in the following line
that are slightly taller than the others. For example, the apex of the ‘A’ extends above the
rectangular body of the type sort and fits underneath the italic ‘R’ in the line above. This
projection is called overshoot at the tops of the letters and overhang at the baseline; in both
cases, it can be round or pointed. Overshoot exists to correct the optical illusion by which
a triangle (or a circle) seems smaller than a square of the same height.
What, then, are the units by which metal type is measured? There are
body size
set-width
two basic ones: the height of the type, called the body size, and the width
of the metal type sort for each character, called its set-width.
The ‘G’ of the word “Gloire” in Figure 0-5 is set in a larger font, which
is why the typesetter has added a row of spaces above the remainder
of the first line of text. It is important to understand that the concept
of “body size” is distinct from that of the size of the letters themselves.
Thus, in the same figure, the letters ‘L’, ‘O’, ... ‘E’ of “Gloire” are smaller than those
of “DIEU”, but their body size is the same, as the metal type sorts that bear them are
of equal height. In this particular case, we have capital letters (in the word “DIEU”) and
small capitals (for “loire”) of the same body size.
We use the term x-height for the height of the faces (and, therefore, the area actually
printed) of lowercase letters such as ‘x’. We say that a character has a “large x-height”
or a “small x-height” when the ratio of the height of its face to the body size is large or
small.
```

Explorations Likewise, the set-width is theoretically independent of the width of the face of the letter, since the latter may be smaller than the former. In that case, we say that the there are right and/or left bearings between the face and the edge of the type sort. Conversely, the face may extend beyond the type sort, if it has a kern. Digital Typesetting Since the 1950s, phototypesetting has gradually conquered the world of printing. It is based on removing the typesetting process from its material roots. This departure from the physical grew more acute with the move towards computerization in the 1970s and 1980s. Now that we have no metal type sorts to measure, what should we make of the terms “body size”, “set-width”, and “x-height”? Have they lost their relevance? Far from it. They are more useful than ever because they ensure continuity between the results of traditional typesetting and those of phototypesetting or digital typesetting. This continuity is essential, since the quality of the final product, the book, must not be adversely affected because of a change in technology. In order to produce books of quality equal to, or better than, that of traditional printing, we must preserve its points of reference, its conventions, and its visual approaches. Therefore, we have to redefine these terms to adapt them to the reality of digital typesetting, which is divorced from physical references. To understand how that has been done, let us investigate the model of digital typesetting: Glyphs (i.e., the visual forms of typographic symbols) are placed in abstract rectangles whose heights are initially undetermined and whose width is equal to the set-width. We need to introduce another new concept, that of the baseline, which is the imaginary line on which all the glyphs with a flat base, such as ‘f’, rest. Those with a round base, such as ‘c’, dip slightly below the baseline as a result of overhang. The intersection of the baseline and the leftmost edge of the glyph’s box is called the origin of the glyph. We describe a glyph mathematically on a system of coordinates with this point as its origin. The set-width can be thought of as a vector connecting the origin of one glyph to that of the following glyph. This vector is called the advance vector (or escapement vector). Digital typesetting consists of nothing more than drawing a glyph, moving as indicated by the advance vector, and preparing to draw the glyph that follows. A glyph “floats” in its imaginary box. The width of the space that will eventually fall between the glyph and the edge of the box is known as the bearing (right or left, as the case may be). In certain cases, the glyph may be located partly or completely outside its box—proof of the relative independence of container and contents, or box and glyph.

Introduction While it was relatively easy to adapt the concept of set-width to the digital realm, the same is not true of the body size. Indeed, we mentioned above that the box containing the glyph is of “undetermined” height. Of all the various typesetting systems, only TEX concerns itself with the height and depth of these boxes, and that is why we have shown the boxes’ upper and lower boundaries, albeit with dotted lines, in the figure. The other systems employ set-width almost exclusively, and PostScript and TrueType fonts contain no information about the height or depth of the box other than the dimensions of the glyph itself. There are also scripts that are written vertically (such as ideographic scripts and Mongolian), in which the advance vector points downward. We say in such cases that there is a vertical set-width. The heights of the spaces that will appear between the glyph and the horizontal edges of the box are thus called upper and lower bearings, as the case may be. But let us return to the concept of “body size”. We continue to speak of setting type “with a body size of 10 points” (or, more professionally, at “10/12”, where the first figure is the type size and the second is the body, which includes leading). But what is a point, and how is this information managed in software? The point is a typographic unit invented by Father Sébastien Truchet in 1699 to describe the arithmetic progression of type sizes [276]. This unit, related to the Paris foot (pied du roi, the actual length of the king’s foot), was redefined by Pierre-Simon Fournier in 1664 and later by François-Ambroise Didot in 1783. Since the end of the nineteenth century, the Anglo-Saxons have used the pica point [87]. The PostScript language sought to simplify calculations by defining the point to be exactly 1 72 of an inch. Today we have points of three different sizes: the pica point (approximately 0.351 mm), the Didot point2 (approximately 0.376 mm), and the PostScript point (approx. 0.353 mm). As for body size, its precise definition depends on the system being used (PostScript, TrueType, TEX), but in general the idea is as follows: glyphs are described with a system of Cartesian coordinates based on an abstract unit of length. There is a relationship between these units and the “body size” of the font. Thus a PostScript font uses a grid of 1,024 units, which means, for example, that an ‘a’ designed with a height of exactly 512 units, when typeset at a font size of 10 points, will appear on paper with a real height of half of the body size, namely 5 points. The user is still free to magnify or reduce the letter as much as he likes. In this book, we use the term actual size for the size of the letter as it appears on paper, after any magnification or reduction performed according to the principle explained below. In the days of the letterpress, there was no way to magnify or reduce a shape arbitrarily. The different body sizes of a given typographic character were engraved separately. And typesetters took advantage of this necessity to improve the legibility of each size: the small sizes had letters that were relatively wider and more spacious than those of the large ones, which were drawn with more details, more contrast between thick and thin strokes, and so on. 2 The Didot point is still used in Greece, where letterpress typesetters complain that text set with the pica point “comes out too small”.

```text
Explorations
By way of illustration, here are a 72-point font and a 6-point font, scaled to the same
actual size:
Laurel & Hardy
The actual size of this sequence of glyphs is 24 points. The 72-point letters (“Laurel &”)
seem too narrow, with horizontal strokes that are too thin, whereas the 6-point letters
(“Hardy”) seem too wide, bordering on awkwardness.
We use the term optical size for the size at which the glyph in question was designed.
Digital fonts usually have only one optical size for all actual sizes—a fact that Ladislas
Mandel calls the “original sin” of phototypesetting. Usually we do not even know the
optical size of a digital font. In a few exceptional cases, the name of the font reveals its
optical size, as is the case with Times Ten (10 points), Times Seven (7 points), etc. There are
also a few rare families of digital fonts designed in several optical sizes: Computer Modern,
by Donald Knuth (see pages 937 and 938); the splendid HW Caslon, by the late Justin
Howes (page 388); HTF Didot, by Jonathan Hoefler (page 392); and ITC Bodoni (page 393),
by Holly Goldsmith, Jim Parkinson, and Sumner Stone. We can only hope that there will
be more such font families in the years to come.
Disregard for optical size can lead to very poor results. Anne Cuneo’s book Le maître de
Garamond (“Garamond’s Master”) [105] was composed in 1530 Garamond, a very beautiful Garamond replica designed by Ross Mills—but at an actual size of 11, while the optical
size of the font is around 48. The print is hard to read, and all the beauty of this wonderful
Garamond is lost.
What about the x-height? According to Peter Karow [206] and Jacques André [34, pp.
24–26], one good approximation to the concept of x-height (in the absence of a physical leaden type sort to serve as a reference) is the relationship between the height of
the lowercase letters and the height of the uppercase letters (for example, the heights of
‘x’ and ‘X’). The closer the lowercase letters come to the height of the uppercase letters,
the greater the x-height is. Fonts such as Courier and Clarendon have a large x-height; fonts
such as Centaur and Nicolas Cochin have a small one:
The term kerning also takes on a different meaning. In digital typesetting, kerning is a
second advance vector that is added to the first. Thus, to set the word “AVATAR”:
```

Introduction the system first draws the ‘A’, then moves ahead by an amount equal to the set-width of an ‘A’, then moves back slightly before drawing the ‘V’, and so on. Because kerning refers to pairs of letters, this information is stored in the fonts as kerning pairs. These values are negative when letters are drawn closer together (for example, ‘A’ and ‘V’) and positive when they are pushed farther apart (for example, a ‘D’ and an ‘O’). Kerning may be good or bad, according to the skills of the font designer, but one thing is certain: fonts that have no kerning pairs should not be trusted, and unfortunately there are more of these than there should be. Font Formats We have mentioned PostScript and TrueType fonts several times. What are they, exactly? A font is a container for glyphs. To set a sequence of glyphs, the software calls up a font through the operating system and asks for the glyphs that it needs. The way in which the glyphs are described depends on the font format: PostScript, TrueType, or any of a number of others, all of them quite different. The earliest fonts were bitmaps: the glyphs were described by white and black pixels (see Appendix A). Although we can easily describe a bitmap font for use on a screen, in which each glyph contains at most a few dozen pixels, it would be cumbersome to do the same for high-resolution printers, for which a single glyph may require thousands of pixels. Two solutions emerged: compress the bitmapped glyphs or switch to a different type of font. Donald Knuth adopted the first solution to the TEX system in 1978: he designed a program with the pretty name of METAFONT that generated compressed bitmap fonts from a description in a very powerful programming language (Appendix A). The method of compression (§A.5.3) was designed so that the size of the glyphs would only slightly affect the size of the files produced. The second solution was notably adopted by John Warnock, founder of Adobe, in 1985. He developed a programming language named PostScript (§C.1) that describes the entire printed page with mathematical constructs. In particular, the PostScript language possesses a font format that even today is one of the most common in the world: Type 1 fonts (§C.3). These fonts, which describe glyphs with mathematical constructs, are called vector fonts. The companies Bitstream and Hewlett-Packard also proposed their own vector font formats, Speedo [188] and Intellifont [101], which did not last long, despite the originality of their ideas. Adobe began to grow thanks to PostScript and the Type 1 fonts, and certain other companies (Apple and Microsoft, without mentioning any names) decided that it was time to break Adobe’s monopoly. Therefore they jointly and hastily developed a competitor to Type 1 fonts, called TrueType (Appendix D). TrueType fonts are not necessarily better or worse than Type 1 fonts, but they present considerable technical differences, which are described in this book.

Explorations The first outgrowth from Type 1 were the Multiple Master fonts, the shapes of whose glyphs could vary under the user’s control. Multiple Master fonts were never a screaming success, no doubt because of the difficulty of developing them. At the same time, the countries of the Far East were struggling to find a way to typeset their ideographic and syllabic writing systems. Adobe offered them another offshoot of Type 1, the CID fonts (§C.1). The fact that the TrueType format was already compatible with ideographic writing systems gave it a head start in this area. Apple and Microsoft separately began to work on improving the TrueType fonts. Apple invested in an extension of TrueType called TrueType GX and later rechristened AAT (“Apple Advanced Typography”, §D.11). Microsoft sought help from its former adversary, Adobe, and together they brought out a competitor to TrueType GX: OpenType (§D.9). OpenType is both an extension to TrueType and an outgrowth of Type 1. In addition, there are two varieties of OpenType fonts: OpenType-TTF (which are TrueType with a few extra features) and OpenType-CFF (which are Type 1 fonts extended and integrated into TrueType structures). Both AAT and OpenType attempt to solve two kinds of problems: those of high-quality Latin typography (with ligatures, old-style [not ranging] figures, correctly spaced punctuation, etc.) and those of the Asian languages (Arabic, Hebrew, Indian languages, Southeast Asian languages, etc.). A large part of Appendix D is devoted to the exploration of these two font formats, which still have surprises in store for us. Between Characters and Glyphs: the Problems of the Electronic Document We have outlined the digital model of typesetting and also the font formats that exist. To continue our exploration of digital writing, we must address another important concept, that of the electronic document. That is the name that we give to a digital entity containing text (and often images, sound, animation, and fonts as well). We find electronic documents everywhere: on hard disks, on CD-ROMs, on the Web. They can be freely accessible or protected. At the heart of our digital space for writing, electronic documents have problems of their own. At the beginning of this introduction, we spoke of the “unending ballet between characters and glyphs”. But the previous two sections did not even speak of characters. On the contrary, the reader may have been left with the impression that the computer transforms characters into glyphs and typesets documents with the use of fonts, leaving the user with nothing to do but display the output on a screen or print it out. That was true some 15 years ago, before the advent of the Web, CD-ROMs, and other means for distributing information in the form of electronic documents. An electronic document takes the appearance of a paper document when it is displayed or printed out, but it has a number of features that hardcopy lacks. It is a file that can be used directly—i.e., without any particular processing or modification—on most computer platforms. But what is involved in using a file of this sort?

```text
Introduction
An electronic document is read or consulted. When reading, we need features that facilitate our task: a table of contents with hypertext links to structural units, the display of a
two-page spread, enlargement or reduction of characters according to the quality of the
screen and the visual acuity of the reader, etc. When consulting a document, we need
the ability to perform rapid searches with multiple criteria and to have rapid access to
the information found.
A search may be performed not only on a single document but on a whole virtual library or even on the entire Web. The electronic document must therefore be indexable.
And if we want the indexing to be “intelligent”, which is to say enriched by structural or
semantic metadata, it is in our interest to prepare the document in a structured form, in
the style of XML.
When we perform searches within a document, they are searches for strings of characters.
Few software systems support searching for strings with specific typographic attributes,
such as specifications of font, point size, or font style. Indeed, to return to the example
of the word “film” given on page 1, we could hardly tell the reader of an electronic document that he would have to enter his search with the glyph for the ‘fi’ ligature or else
the word would not be found.
And since strings are what we search for in a document, strings are also what must be
indexed if our searches are to be rapid. Conclusion: an electronic document must contain
characters if it is to be indexed and become a full-fledged part of the World Wide Web.
But we also expect an electronic document to have the appearance of a paper document
or to yield an equivalent appearance when printed out. It must therefore be typeset; that
is, it must contain glyphs arranged very precisely on lines, with due regard for kerning.
These lines must form paragraphs and pages according to the typographic conventions
developed through the ages. Conclusion: an electronic document must contain glyphs arranged with a great deal of precision in order to be a worthy successor of the paper document.
Corollary: an electronic document must contain both characters and glyphs. The characters must be readily accessible to the outside world and, if possible, structured and
annotated with metadata. The glyphs must be arranged precisely, according to the rules
of the typographic art.
Fulfilling these two often contradictory objectives is in itself a challenge for computer
science. But the problems of the electronic document do not end there. Characters and
glyphs are related like the two sides of a coin, like yin and yang, like signifier and signified. When we interact with an electronic document, we select glyphs with the mouse
and expect that the corresponding characters will be copied onto the system’s clipboard.
Therefore, the document must contain a link between each glyph and the character corresponding to it, even in cases in which one glyph is associated with multiple characters
or multiple glyphs with one character, or, to cite the most complex possibility, when
multiple glyphs are associated with multiple characters in a different order.
Another major problem: the copyright on the various constituents of an electronic document. While we have the right to make our own text and images freely available, the
same is not necessarily true of the fonts that we use. When one “buys” a font, what one
```
