---
title: "Introduction: Explorations"
description: "Unabridged English text from Yannis Haralambous, Fonts & Encodings: The Letter and Its Parts, Letterpress Typesetting, Digital Typesetting, Font Formats, Between Characters and Glyphs, and Book Structure."
---

# Introduction: Explorations
**By Yannis Haralambous, Ph.D. (Translated and Expanded by P. Scott Horne, Ph.D.)**  
*From Fonts & Encodings (O'Reilly Media, 2007), pp. 1–26*

---

Homo sapiens is a species that writes. And among the large number of tools used for writing, the most recent and the most complex is the computer—a tool for reading and writing, a medium for storage, and a means of exchanging data, all rolled into one. It has become a veritable space in which the text resides, a space that, as MacLuhan and others correctly predicted, has come to transcend geographic barriers and encompass the entire planet.

Within this digital space for writing, fonts and encodings serve fundamentally different needs. Rather, they form an inseparable duo, like yin and yang, Heaven and Earth, theory and practice. An encoding emerges from the tendency to conceptualize information; it is the result of an abstraction, a construction of the mind. A font is a means of visually representing writing, the result of concrete expression, a graphical construct.

An encoding is a table of characters—a character being an abstract, intangible entity. A font is a container for glyphs, which are images, drawings, physical marks of black ink on a white background. When the reader enters the digital space for writing, he participates in the unending ballet between characters and glyphs: the keys on the keyboard are marked with glyphs; when a key is pressed, a character is transmitted to the system, which, unless the user is entering a password, in turn displays glyphs on the screen. To send an email message is to send characters, but these are displayed to the recipient in the form of glyphs. When we run a search on a text file, we search for a string of characters, but the results are shown to us as a sequence of glyphs. And so on.

For the Western reader, this perpetual metamorphosis between characters and glyphs remains on the philosophical level. That is hardly surprising, as European writing systems have divided their fundamental constituents (graphemes) so that there is a one-to-one correspondence between character and glyph. Typophiles have given us some exceptions that prove the rule: in the word “film” there are four letters (and therefore four characters) but only three glyphs (because the letters ‘f’ and ‘i’ combine to form only one glyph). This phenomenon, which is called a ligature, can be orthographically significant (as is the case for the ligature ‘œ’, in French) or purely aesthetic (as with the f-ligatures ‘fi’, ‘ff’, ‘ffi’, etc.).

In any case, these phenomena are marginal in our very cut-and-dried Western world. In the writing systems of the East, however, the conflict between characters and glyphs becomes an integral part of daily life. In Arabic, the letters are connected and assume

different forms according to their position in the word. In the languages of India and Southeast Asia, they combine to form more and more complex graphical amalgamations. In the Far East, the ideographs live in a sort of parallel universe, where they are born and die, change language and country, clone themselves, mutate genetically, and carry a multitude of meanings.

Despite the trend towards globalization, the charm of the East has in no way died out; its writing systems still fire our dreams. But every dream is a potential nightmare. Eastern writing systems present a challenge to computer science—a challenge that goes beyond mere technical problems. Since writing—just like images, speech, and music—is one of the fundamental concerns of humanity, computer science cannot approach it haphazardly: Eastern writing systems must be handled just as efficiently as the script that is part of our Latin cultural heritage. Otherwise, some of those writing systems may not survive computerization.

But more is at stake than the imperatives of cultural ecology. The French say that “travel educates the young”. The same goes for writing: through thinking about the writing systems of other cultures and getting to know their problems and concerns, we come to know more about our own.

Then there is also the historical perspective: in the digital space for writing that we are exploring in this book, the concepts and techniques of many centuries dwell together. Terminology, or rather the confusion that reigns in this field, clearly shows that computer science, despite its newness, lies on a historical continuum of techniques and practices. For example, when we set type in Times Ten at 8 points, we say that we are using a “body size of 8 points” and an “optical size of 10 points”. Can the same characters have two different sizes? To understand the meaning of these terms, it is necessary to trace the development of the concept of “type size” from the fifteenth century to the PostScript and TrueType fonts of our modern machines.

So far we have briefly surveyed the three axes on which this book is based: the systemic approach (abstraction/concrete expression, encoding/font, character/glyph), geographicity (East/West), historicity (ancient/modern, mechanical/computerized processes). These three aspects make up the complexity and the scope of our subject, namely the exploration of the digital space for writing.

Finally, there is a fourth axis, less important than the previous three but still well grounded in our day-to-day reality, which is industrial competition. A phenomenon that leads to an explosion in technologies, to gratuitous technicality, to a deliberate lack of clarity in documentation, and to all sorts of other foolish things that give the world of business its supposed charm. If we didn’t have PostScript fonts and TrueType fonts and OpenType fonts and Apple Advanced Typography (AAT) fonts, the world might be a slightly better place and this book would be several hundred pages shorter.

In this regard, the reader should be aware of the fact that everything pertaining to encodings, and to fonts in particular, is considered to be industrial knowledge and therefore cannot be disseminated, at least not completely. It is hard to imagine how badly the “specifications” of certain technologies are written, whether because of negligence or

out of a conscious desire to prevent the full use of the technologies. Some of the appendices of this book were written for the very purpose of describing certain technologies with a reputation for inaccessibility, such as AAT tables and TrueType instructions, as clearly and exhaustively as possible.

In the remainder of this introduction, we shall outline, first of all, the jargon used in the rest of the book, so as to clarify the historical development of certain terms. This will also enable us to give an overview of the transition from mechanical to computerized processes.

Next, we will give the reader a synthetic view of the book by outlining several possible ways to approach it. Each profile of a typical reader that we present is focused on a specific area of interest, a particular way to use this book. We hope that this part of the introduction will allow the reader to find her own path through the forest of 2.5 million letters that she is holding in her hands.

When one walks around a new city for the first time, one discovers places, acquires a better understanding of the reasons behind certain historical events, and puts together the pieces of the puzzle that make up the city’s environment. Here we shall do the same. Our first stroll through the digital space for writing that we plan to explore will allow us to take inventory of concepts and techniques, establish our terminology, and briefly outline the conflict between the mechanical and the electronic.

Let us set aside for the moment the geographical axis and begin with a very specific case of a glyph that comprises the molecular level of our space: the (Latin) letter.

The terminology for describing the letter as a design varies greatly from one writer to the next—a phenomenon, incidentally, that affects all terminology in the entire field of typography. In Figure 0-1, we have listed in roman type the terms that are used in this book and in italics some other terms that exist for the same parts of letters. Thus a stem is also called a stroke or a downstroke.

::: tip Typographical Anatomy Plate (Figure 0-1)
![Figure 0-1: The parts of a letter](/images/fonts-encodings/fig0-1-parts-of-a-letter.png)
*Figure 0-1: The parts of a letter. Terms used in this book are in roman; alternative terms are in parentheses.*
:::



These terms come from a variety of sources: the calligrapher’s technique (stroke, terminal), the engraver’s art (counter), geometry (apex, vertex), analogy or anatomy (arm, eye, ear, tail, shoulder), mechanics or architecture (finial), etc.

The most important among them are:

• The stem, or stroke: a thick vertical or diagonal line found in such letters as ‘H’, ‘l’, ‘N’, and ‘v’. If the letter is lower-case, or small, two possibilities may occur:

– the stem extends upward to the same height as the capitals or even higher, as in

the letters ‘b’, ‘d’, ‘h’, etc. This upper part of the stem is called an ascender.

Apex

Diagonal

Serif

Bar, crossbar

Stem, stroke, downstroke

Diagonal

Vertex

Ascender

Serif

Serif

Bowl

Bulb,  pear-shaped terminal Diagonal, leg

Counter

Head serif,

wedge serif

Bar, crossbar, cross stroke

Foot, finial

Aperture, inner space

Tail

Foot, terminal spur

Serif

Arch, shoulder

Counter

Link

Stem

Ear, spur

Bowl

Descender

Serif

Loop

Figure 0-1: The parts of a letter. The terms used in this book are in roman; alternative terms are shown in italics.

– the stem passes beneath the baseline, as in the letters ‘p’ and ‘q’. This lower part

of the stem is called a descender.

• The bowl, which is a full circle, as in ‘O’, or the greater part of a circle, as in ‘q’.

• The counter, which is the inner part of a letter; for example, the space inside an ‘o’, an ‘O’, a ‘D’, etc. The counter of an ‘e’ is commonly called an eye. When the letter is open at one end, as is the case with ‘n’, we speak instead of an aperture.

• The arm, a thin horizontal stroke that is open at one end, as the two arms atop a ‘T’ and the upper and lower arms of an ‘E’.

• The crossbar (or bar), which is a thin horizontal connecting stroke, as in ‘A’ and ‘H’. A horizontal stroke that crosses a vertical one, as in ‘f’ and ‘t’, is also called a cross stroke.

• The serif, which is the “pedestal” at the bottom and top of the vertical strokes and at the ends of some horizontal strokes. Thus the letter ‘I’ has two serifs, while the letter ‘H’ has four. The left part of an upper serif that appears on some letters, a remnant of the short lead-in made by the pen where it touches the paper before a downstroke, is called a head serif. It is the head serif that distinguishes ‘l’ from ‘I’, for example. In humanist and garalde typefaces (see Chapter 11), the head serif is slanted, whereas it is perfectly horizontal in didones.

• The terminal, which is the opposite of the head serif: it is the movement of the pen that finishes the letter. Again, it is a half-serif, this time the right side of the serif, and it occurs primarily at the baseline.

If these terms apply just as well to traditional as to digital typography, that is because they refer to abstract graphical characteristics.

Now that we have named the components of letters, we can explore ways to describe them precisely. How do we describe the proportions of letters, their graphical characteristics—in short, everything that distinguishes one typographic character from another?

There are two answers to that question: that of the professional, which is to say that of the craftsman (engraver of characters, typographer) or other typographic specialist (historian), and that of the mathematician.

In the first case, we study the letterforms according to their history, the cultural context behind their creation and their use, and their development over time relative to the development of Western culture. To this approach we have devoted Chapter 11, which presents the history of typographic characters and one classification of them from a point of view that is more historical and cultural than formal and geometric.

The second case, that of the mathematician, involves the study of letters as geometric shapes. This approach is hardly new.1 In Figure 0-2 we see four studies of the Latin alphabet, corresponding to two eras and three countries: the first was made by an Italian humanist, Friar Luca de Pacioli, from his work Divine Proportion [273], published in Venice in 1509. The second comes to us from the hands of the great German engraver Albrecht Dürer and is dated 1535. It presents different models of alphabets in a work whose title is less ambitious than that of Pacioli: Instructions on Measurement [124]. The third dates from 1524 and is from France: it is the manual of Geofroy Tory, a great Parisian humanist to whom we also owe the use of the accents and the cedilla in the French language. His descriptions appear in his finest work, the Champ fleury, au quel eNt contenu Lart & Science de la deue & vraye Proportiõ des Lettres Attiques (“The Floured Feelde, wherein be

::: tip Mathematical Letterforms Plate (Figure 0-2)
![Figure 0-2: Six mathematical descriptions of the letter 'E'](/images/fonts-encodings/fig0-2-mathematical-descriptions-letter-e.png)
*Figure 0-2: Six mathematical descriptions of the letter ‘E’: Luca de Pacioli (1509), Albrecht Dürer (1525), Geofroy Tory (1529), Commission Jaugeon (1693), and contemporary digital Bézier outlines.*
:::



1 Readers who wish to know more about the history of the mathematical description of letterforms are encouraged to consult Donald Knuth [221, p. 48] and Jacques André [35].

Figure 0-2: Six mathematical descriptions of the letter ‘E’: Luca de Pacioli (1509), Albrecht Dürer (1535), Geofroy Tory (1524), the Jaugeon Commission (1716), and two screenshots from the software package FontLab (today).

contayned the Arte & Scyence of the iufte and true Proporcion of Atticke Letters”) [332]. Finally, in 1716, as a result of an undertaking by Louis XIV, the Jaugeon Commission drafted the design for a royal script, entirely geometrical in nature, called the Romain du Roi [276] (“the King’s roman”).

Many things strike us from an examination of these four examples. First of all, we notice that, in all four instances, the artists wished to place their letters within perfect squares, in the same way as the characters of the Far East. We also notice that they use finer and finer Cartesian grids in order to obtain more precise mathematical descriptions. While Tory uses a grid of 10×10 squares, the Jaugeon Commission resorts to 6×6 small squares within 8 × 8 large ones, for a total of 48 × 48—2,304 squares in all, which was an enormous degree of precision for the time.

While the challenge was originally of a humanist nature (in the fifteenth century, when perspective was invented, Europeans began to wonder about the relationship between beauty and mathematics), it became one of power (Louis XIV took control of everything in his kingdom, right down to the microscopic level) and, finally, in the twentieth century, one of technology.

Why? Because these mathematical descriptions of letters are the precursors of the digital fonts of today, defined on a grid of 1,024×1,024 (PostScript) or 4,096×4,096 (TrueType) squares, or even more. There is only a difference of mathematical scale: whereas the letters in the first four examples are described by circles and lines in the manner of Euclid (“with straightedge and compass”), today’s fonts use curves defined by third-degree polynomials that were introduced by the French engineer Pierre Bézier (see Appendix G). In the last two examples in Figure 0-2, we see two contemporary approaches to the design of glyphs: they are screenshots from the software system FontLab.

What is the situation today? Have Bézier curves extinguished the little flame that is the genius of the master engraver? Quite the opposite. We use Bézier curves today because we have interactive tools that allow modern designers to create fonts worthy of their predecessors. We have devoted Chapters 12 to 14 and Appendix F to the description of the best available tools for creating fonts.

In the previous section, we discussed the individuals that populate the digital space for writing: letters. But this space would be quite sad if each letter lived all by itself in its own little bubble. Far from being so isolated, letters, and more generally glyphs of all kinds, are highly social creatures. They love to form little groups (words), which in turn form larger and larger groups (lines, paragraphs, pages, books). We call this process typesetting. And the human who weaves the fates of the letters together to form structures on a higher level is a typesetter.

Having come to this point, we can no longer content ourselves with the abstraction in which the previous section indulged. The way in which we put letters together depends on the technology that we use. It is therefore time to abandon the realm of the abstract

Figure 0-3: An eighteenth-century type case (from the Encyclopédie of Diderot and d’Alembert).

::: tip Letterpress Movable Type Case (Figure 0-3)
![Figure 0-3: An 18th-century French type case](/images/fonts-encodings/fig0-3-eighteenth-century-type-case.png)
*Figure 0-3: An 18th-century French type case (Encyclopédie of Diderot and d’Alembert).*
:::



beauty of letters and to come down to earth to describe the mechanical process of typesetting. For computerized typesetting is based on mechanical typesetting, and the terms that we use today were invented by those people whose hands were indelibly blackened, not with oil (the liquid that pollutes our ecosystem), but with printer’s ink (the liquid that bears wisdom).

Let us therefore quickly review the manual setting of type for the letterpress, which was used from the fifteenth century until the end of the nineteenth, when the Linotype and Monotype typesetting machines made their appearance.

Letterpress printing is based on movable type, little metal blocks (sorts) made from an amalgam of lead, zinc, and antimony that have on one side a mirror image of a letter, carved in relief. In Figure 0-3, taken from the Encyclopédie of Diderot and d’Alembert, we see at the top a type case containing type and, below it, the table that supports the different cases from which type is taken for composition. The top half of the case, the “upper case”, contains the capital letters, the small capitals, and certain punctuation marks; the bottom half, the “lower case”, contains the small letters (called “lowercase” for this very reason), the numerals, and various “spaces” (blocks of lead with no letter carved into them that serve to separate words). We can see how type is arranged in the case. Of course, the arrangement varies from country to country according to the frequency of letters in the dominant language.

Figure 0-4: A composing stick (from the Encyclopédie of Diderot and d’Alembert).

::: tip Typesetting Composing Stick (Figure 0-4)
![Figure 0-4: A composing stick](/images/fonts-encodings/fig0-4-composing-stick.png)
*Figure 0-4: A composing stick (Encyclopédie of Diderot and d’Alembert).*
:::



The typesetter takes type sorts out of the case and places them on a composing stick, which is illustrated in Figure 0-4. A whole line at a time is prepared on a composing stick. The width of the composing stick is that of the measure of the page; thus the typesetter knows when he has reached the end of the line and can take appropriate action. He can decide to divide the word or to fill out the line with thin strips of extra spacing between the words to extend it to the full measure.

When the line is ready, the typesetter adds it to the other lines of the page, eventually inserting horizontal strips of lead, called leading, between the lines. At the bottom of Figure 0-5, there are three lines that are set in this fashion:

::: tip Composed Movable Lines (Figure 0-5)
![Figure 0-5: Three typeset lines](/images/fonts-encodings/fig0-5-three-typeset-lines.png)
*Figure 0-5: Three typeset lines (Encyclopédie of Diderot and d’Alembert).*
:::



Gloire à DIEU. Honneur au ROI. Salut aux Armes.

In this example, we can notice several tricks that enable us to overlap the faces of letters. First, the face of the italic ‘H’ in the second line extends beyond the body of the type sort

Figure 0-5: Three typeset lines (from the Encyclopédie of Diderot and d’Alembert).

and reaches over the ‘o’ that follows. This overlapping, called kerning, is indispensable, since italic letters are not slanted but occupy upright parallelepipeds. The italic ‘I’ also kerns with the following letter.

Another trick: the lower parts of the faces of the letters are cut on an angle. The benefit of this device is that it permits the vertical kerning of certain letters in the following line that are slightly taller than the others. For example, the apex of the ‘A’ extends above the rectangular body of the type sort and fits underneath the italic ‘R’ in the line above. This projection is called overshoot at the tops of the letters and overhang at the baseline; in both cases, it can be round or pointed. Overshoot exists to correct the optical illusion by which a triangle (or a circle) seems smaller than a square of the same height.

What, then, are the units by which metal type is measured? There are

two basic ones: the height of the type, called the body size, and the width of the metal type sort for each character, called its set-width.

set-width

body size

The ‘G’ of the word “Gloire” in Figure 0-5 is set in a larger font, which is why the typesetter has added a row of spaces above the remainder of the first line of text. It is important to understand that the concept of “body size” is distinct from that of the size of the letters themselves. Thus, in the same figure, the letters ‘L’, ‘O’, ... ‘E’ of “Gloire” are smaller than those of “DIEU”, but their body size is the same, as the metal type sorts that bear them are of equal height. In this particular case, we have capital letters (in the word “DIEU”) and small capitals (for “loire”) of the same body size.

We use the term x-height for the height of the faces (and, therefore, the area actually printed) of lowercase letters such as ‘x’. We say that a character has a “large x-height” or a “small x-height” when the ratio of the height of its face to the body size is large or small.

Likewise, the set-width is theoretically independent of the width of the face of the letter, since the latter may be smaller than the former. In that case, we say that the there are right and/or left bearings between the face and the edge of the type sort. Conversely, the face may extend beyond the type sort, if it has a kern.

Since the 1950s, phototypesetting has gradually conquered the world of printing. It is based on removing the typesetting process from its material roots. This departure from the physical grew more acute with the move towards computerization in the 1970s and 1980s. Now that we have no metal type sorts to measure, what should we make of the terms “body size”, “set-width”, and “x-height”?

Have they lost their relevance? Far from it. They are more useful than ever because they ensure continuity between the results of traditional typesetting and those of phototypesetting or digital typesetting. This continuity is essential, since the quality of the final product, the book, must not be adversely affected because of a change in technology. In order to produce books of quality equal to, or better than, that of traditional printing, we must preserve its points of reference, its conventions, and its visual approaches.

Therefore, we have to redefine these terms to adapt them to the reality of digital typesetting, which is divorced from physical references. To understand how that has been done, let us investigate the model of digital typesetting:

Glyphs (i.e., the visual forms of typographic symbols) are placed in abstract rectangles whose heights are initially undetermined and whose width is equal to the set-width.

We need to introduce another new concept, that of the baseline, which is the imaginary line on which all the glyphs with a flat base, such as ‘f’, rest. Those with a round base, such as ‘c’, dip slightly below the baseline as a result of overhang. The intersection of the baseline and the leftmost edge of the glyph’s box is called the origin of the glyph. We describe a glyph mathematically on a system of coordinates with this point as its origin.

The set-width can be thought of as a vector connecting the origin of one glyph to that of the following glyph. This vector is called the advance vector (or escapement vector). Digital typesetting consists of nothing more than drawing a glyph, moving as indicated by the advance vector, and preparing to draw the glyph that follows.

A glyph “floats” in its imaginary box. The width of the space that will eventually fall between the glyph and the edge of the box is known as the bearing (right or left, as the case may be). In certain cases, the glyph may be located partly or completely outside its box—proof of the relative independence of container and contents, or box and glyph.

While it was relatively easy to adapt the concept of set-width to the digital realm, the same is not true of the body size. Indeed, we mentioned above that the box containing the glyph is of “undetermined” height. Of all the various typesetting systems, only TEX concerns itself with the height and depth of these boxes, and that is why we have shown the boxes’ upper and lower boundaries, albeit with dotted lines, in the figure.

The other systems employ set-width almost exclusively, and PostScript and TrueType fonts contain no information about the height or depth of the box other than the dimensions of the glyph itself.

There are also scripts that are written vertically (such as ideographic scripts and Mongolian), in which the advance vector points downward. We say in such cases that there is a vertical set-width. The heights of the spaces that will appear between the glyph and the horizontal edges of the box are thus called upper and lower bearings, as the case may be.

But let us return to the concept of “body size”. We continue to speak of setting type “with a body size of 10 points” (or, more professionally, at “10/12”, where the first figure is the type size and the second is the body, which includes leading). But what is a point, and how is this information managed in software?

The point is a typographic unit invented by Father Sébastien Truchet in 1699 to describe the arithmetic progression of type sizes [276]. This unit, related to the Paris foot (pied du roi, the actual length of the king’s foot), was redefined by Pierre-Simon Fournier in 1664 and later by François-Ambroise Didot in 1783. Since the end of the nineteenth century, the Anglo-Saxons have used the pica point [87]. The PostScript language sought to simplify calculations by defining the point to be exactly 1

72 of an inch. Today we have points of three different sizes: the pica point (approximately 0.351 mm), the Didot point2

(approximately 0.376 mm), and the PostScript point (approx. 0.353 mm).

As for body size, its precise definition depends on the system being used (PostScript, TrueType, TEX), but in general the idea is as follows: glyphs are described with a system of Cartesian coordinates based on an abstract unit of length. There is a relationship between these units and the “body size” of the font. Thus a PostScript font uses a grid of 1,024 units, which means, for example, that an ‘a’ designed with a height of exactly 512 units, when typeset at a font size of 10 points, will appear on paper with a real height of half of the body size, namely 5 points.

The user is still free to magnify or reduce the letter as much as he likes. In this book, we use the term actual size for the size of the letter as it appears on paper, after any magnification or reduction performed according to the principle explained below.

In the days of the letterpress, there was no way to magnify or reduce a shape arbitrarily. The different body sizes of a given typographic character were engraved separately. And typesetters took advantage of this necessity to improve the legibility of each size: the small sizes had letters that were relatively wider and more spacious than those of the large ones, which were drawn with more details, more contrast between thick and thin strokes, and so on.

2 The Didot point is still used in Greece, where letterpress typesetters complain that text set with the pica point “comes out too small”.

By way of illustration, here are a 72-point font and a 6-point font, scaled to the same actual size:

Laurel & Hardy

The actual size of this sequence of glyphs is 24 points. The 72-point letters (“Laurel &”) seem too narrow, with horizontal strokes that are too thin, whereas the 6-point letters (“Hardy”) seem too wide, bordering on awkwardness.

We use the term optical size for the size at which the glyph in question was designed. Digital fonts usually have only one optical size for all actual sizes—a fact that Ladislas Mandel calls the “original sin” of phototypesetting. Usually we do not even know the optical size of a digital font. In a few exceptional cases, the name of the font reveals its optical size, as is the case with Times Ten (10 points), Times Seven (7 points), etc. There are also a few rare families of digital fonts designed in several optical sizes: Computer Modern, by Donald Knuth (see pages 937 and 938); the splendid HW Caslon, by the late Justin Howes (page 388); HTF Didot, by Jonathan Hoefler (page 392); and ITC Bodoni (page 393), by Holly Goldsmith, Jim Parkinson, and Sumner Stone. We can only hope that there will be more such font families in the years to come.

Disregard for optical size can lead to very poor results. Anne Cuneo’s book Le maître de Garamond (“Garamond’s Master”) [105] was composed in 1530 Garamond, a very beautiful Garamond replica designed by Ross Mills—but at an actual size of 11, while the optical size of the font is around 48. The print is hard to read, and all the beauty of this wonderful Garamond is lost.

What about the x-height? According to Peter Karow [206] and Jacques André [34, pp. 24–26], one good approximation to the concept of x-height (in the absence of a physical leaden type sort to serve as a reference) is the relationship between the height of the lowercase letters and the height of the uppercase letters (for example, the heights of ‘x’ and ‘X’). The closer the lowercase letters come to the height of the uppercase letters, the greater the x-height is. Fonts such as Courier and Clarendon have a large x-height; fonts such as Centaur and Nicolas Cochin have a small one:

The term kerning also takes on a different meaning. In digital typesetting, kerning is a second advance vector that is added to the first. Thus, to set the word “AVATAR”:

the system first draws the ‘A’, then moves ahead by an amount equal to the set-width of an ‘A’, then moves back slightly before drawing the ‘V’, and so on.

Because kerning refers to pairs of letters, this information is stored in the fonts as kerning pairs. These values are negative when letters are drawn closer together (for example, ‘A’ and ‘V’) and positive when they are pushed farther apart (for example, a ‘D’ and an ‘O’). Kerning may be good or bad, according to the skills of the font designer, but one thing is certain: fonts that have no kerning pairs should not be trusted, and unfortunately there are more of these than there should be.

We have mentioned PostScript and TrueType fonts several times. What are they, exactly?

A font is a container for glyphs. To set a sequence of glyphs, the software calls up a font through the operating system and asks for the glyphs that it needs. The way in which the glyphs are described depends on the font format: PostScript, TrueType, or any of a number of others, all of them quite different.

The earliest fonts were bitmaps: the glyphs were described by white and black pixels (see Appendix A). Although we can easily describe a bitmap font for use on a screen, in which each glyph contains at most a few dozen pixels, it would be cumbersome to do the same for high-resolution printers, for which a single glyph may require thousands of pixels.

Two solutions emerged: compress the bitmapped glyphs or switch to a different type of font. Donald Knuth adopted the first solution to the TEX system in 1978: he designed a program with the pretty name of METAFONT that generated compressed bitmap fonts from a description in a very powerful programming language (Appendix A). The method of compression (§A.5.3) was designed so that the size of the glyphs would only slightly affect the size of the files produced.

The second solution was notably adopted by John Warnock, founder of Adobe, in 1985. He developed a programming language named PostScript (§C.1) that describes the entire printed page with mathematical constructs. In particular, the PostScript language possesses a font format that even today is one of the most common in the world: Type 1 fonts (§C.3). These fonts, which describe glyphs with mathematical constructs, are called vector fonts.

The companies Bitstream and Hewlett-Packard also proposed their own vector font formats, Speedo [188] and Intellifont [101], which did not last long, despite the originality of their ideas.

Adobe began to grow thanks to PostScript and the Type 1 fonts, and certain other companies (Apple and Microsoft, without mentioning any names) decided that it was time to break Adobe’s monopoly. Therefore they jointly and hastily developed a competitor to Type 1 fonts, called TrueType (Appendix D). TrueType fonts are not necessarily better or worse than Type 1 fonts, but they present considerable technical differences, which are described in this book.

The first outgrowth from Type 1 were the Multiple Master fonts, the shapes of whose glyphs could vary under the user’s control. Multiple Master fonts were never a screaming success, no doubt because of the difficulty of developing them.

At the same time, the countries of the Far East were struggling to find a way to typeset their ideographic and syllabic writing systems. Adobe offered them another offshoot of Type 1, the CID fonts (§C.1). The fact that the TrueType format was already compatible with ideographic writing systems gave it a head start in this area.

Apple and Microsoft separately began to work on improving the TrueType fonts. Apple invested in an extension of TrueType called TrueType GX and later rechristened AAT (“Apple Advanced Typography”, §D.11). Microsoft sought help from its former adversary, Adobe, and together they brought out a competitor to TrueType GX: OpenType (§D.9).

OpenType is both an extension to TrueType and an outgrowth of Type 1. In addition, there are two varieties of OpenType fonts: OpenType-TTF (which are TrueType with a few extra features) and OpenType-CFF (which are Type 1 fonts extended and integrated into TrueType structures).

Both AAT and OpenType attempt to solve two kinds of problems: those of high-quality Latin typography (with ligatures, old-style [not ranging] figures, correctly spaced punctuation, etc.) and those of the Asian languages (Arabic, Hebrew, Indian languages, Southeast Asian languages, etc.). A large part of Appendix D is devoted to the exploration of these two font formats, which still have surprises in store for us.

Between Characters and Glyphs: the Problems of the Electronic Document

We have outlined the digital model of typesetting and also the font formats that exist. To continue our exploration of digital writing, we must address another important concept, that of the electronic document.

That is the name that we give to a digital entity containing text (and often images, sound, animation, and fonts as well). We find electronic documents everywhere: on hard disks, on CD-ROMs, on the Web. They can be freely accessible or protected. At the heart of our digital space for writing, electronic documents have problems of their own.

At the beginning of this introduction, we spoke of the “unending ballet between characters and glyphs”. But the previous two sections did not even speak of characters. On the contrary, the reader may have been left with the impression that the computer transforms characters into glyphs and typesets documents with the use of fonts, leaving the user with nothing to do but display the output on a screen or print it out.

That was true some 15 years ago, before the advent of the Web, CD-ROMs, and other means for distributing information in the form of electronic documents. An electronic document takes the appearance of a paper document when it is displayed or printed out, but it has a number of features that hardcopy lacks.

It is a file that can be used directly—i.e., without any particular processing or modification—on most computer platforms. But what is involved in using a file of this sort?

An electronic document is read or consulted. When reading, we need features that facilitate our task: a table of contents with hypertext links to structural units, the display of a two-page spread, enlargement or reduction of characters according to the quality of the screen and the visual acuity of the reader, etc. When consulting a document, we need the ability to perform rapid searches with multiple criteria and to have rapid access to the information found.

A search may be performed not only on a single document but on a whole virtual library or even on the entire Web. The electronic document must therefore be indexable. And if we want the indexing to be “intelligent”, which is to say enriched by structural or semantic metadata, it is in our interest to prepare the document in a structured form, in the style of XML.

When we perform searches within a document, they are searches for strings of characters. Few software systems support searching for strings with specific typographic attributes, such as specifications of font, point size, or font style. Indeed, to return to the example of the word “film” given on page 1, we could hardly tell the reader of an electronic document that he would have to enter his search with the glyph for the ‘fi’ ligature or else the word would not be found.

And since strings are what we search for in a document, strings are also what must be indexed if our searches are to be rapid. Conclusion: an electronic document must contain characters if it is to be indexed and become a full-fledged part of the World Wide Web.

But we also expect an electronic document to have the appearance of a paper document or to yield an equivalent appearance when printed out. It must therefore be typeset; that is, it must contain glyphs arranged very precisely on lines, with due regard for kerning. These lines must form paragraphs and pages according to the typographic conventions developed through the ages. Conclusion: an electronic document must contain glyphs arranged with a great deal of precision in order to be a worthy successor of the paper document.

Corollary: an electronic document must contain both characters and glyphs. The characters must be readily accessible to the outside world and, if possible, structured and annotated with metadata. The glyphs must be arranged precisely, according to the rules of the typographic art.

Fulfilling these two often contradictory objectives is in itself a challenge for computer science. But the problems of the electronic document do not end there. Characters and glyphs are related like the two sides of a coin, like yin and yang, like signifier and signified. When we interact with an electronic document, we select glyphs with the mouse and expect that the corresponding characters will be copied onto the system’s clipboard. Therefore, the document must contain a link between each glyph and the character corresponding to it, even in cases in which one glyph is associated with multiple characters or multiple glyphs with one character, or, to cite the most complex possibility, when multiple glyphs are associated with multiple characters in a different order.

Another major problem: the copyright on the various constituents of an electronic document. While we have the right to make our own text and images freely available, the same is not necessarily true of the fonts that we use. When one “buys” a font, what one

actually buys is a license to use it. According to the foundry, this license may or may not specify the number of machines and/or printers on which the font may be installed and used. But no foundry will allow someone who has bought a license for one of its fonts to distribute that font publicly. How, then, can one display the glyphs of a document in a particular font if one does not have the right to distribute it?

Electronic documents are caught between the past (typography, glyphs and their arrangement, fonts) and the future (the Web, characters, information that can be indexed at will and made available to everyone). In saying that, we have taken only two axes of our digital space for writing into account: the system approach (characters/glyphs) and historicity. There remain the geographic axis (East/West, with all the surprises that the writing systems of other cultures have in store for us) and the industrial axis (problems of file format, platform, etc.).

In this book, we aim to offer the reader a certain number of tools to confront these problems. We do not concern ourselves with all aspects of the electronic document, just those pertaining to characters and glyphs, aspects that directly and inevitably affect encodings and fonts.

This book contains 14 chapters grouped into 4 units and 7 appendices. We have repeatedly said that fonts and encodings interact like yin and yang. Here we use this metaphor to give a graphical illustration of the book’s structure with the yin–yang symbol (Figure 0-6) in the background. On the left, in the gray-shaded area: encodings. On the right, in the white part: fonts.

::: tip Global Curriculum & Knowledge Map (Figure 0-6)
![Figure 0-6: The general structure of this book](/images/fonts-encodings/fig0-6-book-structure.png)
*Figure 0-6: The general structure of this book across Encodings/Characters (left) and Fonts/Glyphs (right).*
:::



At the top of the circle is the introduction that the reader is currently reading.

The first box, the one on the left, contains the five chapters on encodings, in particular Unicode.

In the first chapter, entitled “Before Unicode”, we present a history of codes and encodings, starting in antiquity. After a few words on systems of encoding used in telecommunication before the advent of the computer, we proceed immediately to the most well-known encoding of all, ASCII, and its staunch competitor, EBCDIC. Then follows the ISO 8859 series of encodings, the most recent of which was released in 2001. At the same time, we discuss the problems of the countries of the Far East and the different solutions offered by ISO, Microsoft, and the UNIX world. Finally, we end with a few words on electronic mail and the Web.

The second chapter, “Characters, Glyphs, Bytes”, is an introduction to Unicode. In it, we develop the underlying concepts of Unicode, the principles on which it is based, its philosophy, and the technical choices that it has made. We finish the chapter with a quick look at the different tables of Unicode, including a preview of the tables that are still at the stage of consideration that precedes inclusion in the encoding.

Next comes the chapter “Unicode Character Properties”, which leads us into the morass of the data that accompanies the characters. Often this data indicates that the character

o

f

n

ts

/

g

l

y

p

h

s

6. Font management     on the Macintosh 7. Font management     under Windows 8. Font management     under X Window

1. Before Unicode 2. Characters,    glyphs, bytes 3. Unicode character    properties 4. Normalizations,     bidirectionality,     CJK characters 5. Using Unicode

11. History and      classifications 12. Editing and creating     fonts 13. Optimizing the rendering 14. Advanced typographical      features F.  METAFONT and      its derivatives

9.  Fonts under      TEX and Ω 10. Fonts and the Web

rs

e

ct

a

r

a

h

c

/

s

g

n

i

d

o

e

c

n

Appendices

Bibliographic

references General index Index of names

A. Bitmap fonts B. TEX et Ω fonts C. PostScript fonts D. TrueType, OpenType       and AAT fonts E. TrueType instructions G. Bézier curves

Figure 0-6: Structure of the chapters of this book.

in question plays a certain role. We explain this role by showing the reader some of the internal workings of the encoding.

On the subject of internal workings, we have assembled three of the most complex in Chapter 4. This chapter’s title is merely a list of these three mechanisms: normalization, the bidirectional algorithm, and the handling of East Asian characters. Normalization is a set of ways to make a text encoded in Unicode more efficient by removing certain ambiguities; in particular, one of the normalization forms that we describe is required for the use of Unicode on the Web. Bidirectionality concerns the mixture of left-to-right and right-to-left scripts. Unicode gives us an algorithm to define the typesetting of a text containing a mixture of this sort. Finally, by “East Asian scripts” we mean both Chinese ideographs and hangul syllables. For the former, we present a handful of techniques to obtain characters not supplied in Unicode; for the latter, we describe the method for forming syllables from hangul letters.

Finally, the last chapter in this unit is less theoretical than the others. We address a specific problem: how to produce a text encoded in Unicode? We offer three possible answers: by entering characters with a mouse, by creating virtual keyboards, and by converting texts written in other encodings. In each of these three cases, we describe appropriate tools for use under Mac OS, Windows, or UNIX.

This unit lies entirely within the gray section (“encodings”), as we discuss only encodings, not fonts, in its chapters.

The second unit (Chapters 6 to 8) lies within the white section (“fonts”), but we have placed it in the center of the circle because it discusses not fonts themselves but their management. Thus it takes up the installation of fonts, tools for activation/deactivation, font choices—in short, the management of a large number of fonts, which is of concern to graphic designers and other large consumers of fonts. The unit is divided into three chapters so that we can discuss the two most popular operating systems—Mac OS (9 or X) and Windows, as well as the X Window windowing system from the UNIX world. We discover that the Macintosh is privileged (it has the greatest number of tools for font management), that the same tools exist for Windows but that their quality is often poorer, and that X Window is a world unto itself, with its own advantages and drawbacks. These three chapters will thrill neither the computer scientist nor the typophile, but they may be of great practical value to those whose lives are plagued by system crashes, unexplainable slow-downs, poor quality of output (who has never been surprised to see his beautiful Bembo replaced by a hideous Courier?), corrupted documents, and all sorts of other such mishaps, often caused by fonts. They will also delight those who love order and who dream of being able to find and use almost instantaneously any font among the thousands of similar ones that they have collected on multiple CD-ROMs. On the other hand, if the reader uses only the fonts that come standard on his operating system, he has no need to read these chapters.

The third unit (Chapters 9 and 10) gets more technical. It deals with the use of fonts in two specific cases: the TEX typesetting system (and its successor, Ω, of which the author is

co-developer) and Web pages. TEX is a software system and a programming language devoted to typesetting. It is also used today to produce electronic documents. Its approach to managing fonts is unique and totally independent of the operating system being used. In this chapter, we have tried to cover as thoroughly as possible all the many aspects of the use of fonts under TEX. Technical descriptions of the font formats used in Chapter 9 appear in Appendix B (“The Font Formats of TEX and Ω”).

The situation is different in the case of the Web, which presents both technical problems (How to supply a font to the browser? How to make the browser use it automatically?) and legal ones (What about the font’s copyright?). We describe the different solutions that Microsoft and Bitstream have offered for this problem and also another spectacular solution: the GlyphGate font server. This approach can be called conventional: we use the HTML markup system and supply the fonts in addition. The Web Consortium has proposed another, cleaner, solution: describe the font in XML, just like the rest of the document. This solution is part of the SVG standard for the description of vector graphics, which we describe in detail.

These two chapters are also placed in the middle of the circle because they deal with subjects that lie in between encodings and fonts: TEX and HTML can both be considered as vehicles for passing from characters to glyphs; they are bridges between the two worlds.

The fourth unit (Chapters 11 to 14 and Appendix F) is devoted completely to fonts. The first chapter, “History and Classifications”, is a unique chapter in this book, as it discusses computers very little but deals mainly with the history of printing, especially the history of Latin typographic characters. We have seen that for designing high-quality fonts it is not enough to have good tools: a certain knowledge of the history of the fonts that surround us is also essential. Even in the history presented here, however, the point of view is that of the user of digital fonts. Thus most of the examples provided were produced with digital fonts rather than from reproductions of specimens of printing from an earlier era. We also frequently compare the original specimens with digital fonts created by a variety of designers.

Chapter 11 goes beyond history. It continues with a description of three methods for classifying fonts. The first two (Vox and Alessandrini) finish offthe history, in a way, and recapitulate it. The Vox classification gives us a jargon for describing fonts (garalde, didone, etc.) that every professional in the fields of graphic design and publishing must know. The scheme of Alessandrini should be considered a critique (with a heaping helping of humor) of Vox’s; we couldn’t resist the pleasure of presenting it here.

The third classification scheme is quite different and serves as a link between this chapter and the rest of the book. It is Panose-1, a mathematical description of the properties of glyphs. Each font is characterized by a sequence of 10 numbers, which correspond to 10 practically independent properties. Both Windows and the Cascading Style Sheets standard make use of this classification system to select substitute fonts by choosing the available font whose Panose-1 distance from the missing font is the smallest. Despite the fame of the Panose-1 system, a precise description of it is very difficult to find. This book provides one, thanks to the generosity of Benjamin Bauermeister, the creator of Panose- 1, who was kind enough to supply us with the necessary information.

Chapters 12 to 14 describe the existing tools for creating (or modifying) fonts. We have chosen two basic tools, FontLab and FontForge (formerly PfaEdit), and we describe their most important capabilities in this chapter. There are three chapters instead of only one because we have broken the font-creation process into three steps: drawing glyphs, optimizing the rendering, and supplementing the font with “advanced typographic” properties. Optimization of the rendering involves adding the PostScript hints or TrueType instructions needed to make the rendering optimal at all body sizes. In this chapter, we also describe a third tool that is used specifically for instructing fonts: Microsoft’s Visual TrueType. Since the hinting and instructing of fonts are reputed to be arcane and poorly documented techniques, we have tried to compensate by devoting an entire chapter to them, complete with many real-world examples. In addition, Appendix E is devoted to the description of the TrueType assembly language for instructing fonts; it is the ideal companion to Chapter 13, which is concerned more with the tools used for instructing than with the instructions themselves.

Chapter 14 discusses the big new development of recent years, OpenType properties. Adobe and Microsoft, the companies that have supported this technology, had two purposes in mind: Latin fonts “of typographic quality” (i.e., replete with such gadgets as ligatures, variant glyphs, glyphs for the languages of Central Europe, etc.) and specific non-Latin fonts (with contextual analysis, ligature processing, etc.). High-quality Latin fonts make use of the “advanced typographic features”. Right now several foundries are converting their arsenals of PostScript or TrueType fonts into OpenType fonts with advanced properties, and the tools FontLab and FontForge lend themselves admirably to the task, to which we have devoted the first part of the chapter. Along the way, we also describe a third tool dedicated to this task: VOLT, by Microsoft.

The second part of the chapter is devoted to OpenType’s competitor, the AAT fonts (formerly called TrueType GX). These fonts are considered by some to be more powerful than OpenType fonts, but they suffer from a lack of tools, poor documentation, and, what is worse, a boycott by the major desktop publishing systems (Adobe Creative Suite, Quark XPress, etc.). But these problems may prove to be only temporary, and we felt that AAT deserved to be mentioned here along with OpenType. In this chapter, the reader will learn how to equip TrueType fonts with AAT tables by using the only tool that is able to do the job: FontForge.

Finally, we include in this unit Appendix F, “METAFONT and Its Derivatives”. METAFONT is a programming language dedicated to font creation, the work of the same person who created TEX, the famous computer scientist Donald Knuth of Stanford University. METAFONT is a very powerful tool full of good ideas. The reason that we have not included it in the main part of the book is that it has become obsolete, in a way, by virtue of its incompatibility with the notion of the electronic document. Specifically, METAFONT creates bitmap fonts without a trace of the characters to which the glyphs correspond; thus they cannot be used in electronic documents, as the link between glyph and character is broken. Furthermore, these bitmap fonts depend on the characteristics of a given printer; thus there can be no “universal” METAFONT font that is compatible with every printer—whereas PostScript and TrueType fonts are based on that principle of universality. Nonetheless, we have described METAFONT in this book for three reasons:

for nostalgia and out of respect for Donald Knuth, for METAFONT’s intrinsic value as a tool for designing fonts, and, finally, because some recent software attempts to make up for the shortcomings of METAFONT by generating PostScript or TrueType fonts from the same source code used for METAFONT or from a similar type of source. We describe two attempts of this kind: METATYPE1 and MetaFog.

Without a doubt, this book distinguishes itself by the uncommonly large size of its appendices. We have aimed to compile and present the main font formats in our own way—an undertaking that has consumed a great deal of time and energy, not to mention pages.

Appendix A can be considered a sort of history of font formats, as it discusses a type of fonts—bitmap fonts—that has virtually disappeared.

Appendix B discusses the “real” and virtual fonts of TEX.

Appendix C aims to discuss all of the PostScript font formats, from Type 1 (released in 1985) to CFF, which is a part of the OpenType standard, with a brief mention of the obsolete formats (Type 3 and Multiple Masters) and the special formats for Far Eastern scripts. So that we can understand the PostScript code for these fonts, we have also provided an introduction to this very specialized programming language.

In Appendix D, we take on the challenge of describing in detail all the TrueType, OpenType, and AAT tables. So as not to bore the reader with low-level technical details on the numbers of bytes in each field, the pointers between the tables, the number of bytes of padding—in short, the horror of editing raw binary data—we describe these tables in an XML syntax used by the tool TTX. This tool, developed in Python by Just van Rossum, the brother of Guido van Rossum (who invented Python), makes it possible to convert TrueType, OpenType, and AAT binary data into XML and vice versa. Thus we can consider the TTX representation of these fonts to be equivalent to their binary form, and we shall take advantage of this convenience to describe the tables as XML structures. That approach will not make their complexity disappear as if by waving a magic wand, but it will at least spare the reader needless complexity that pertains only to aspects of the binary format of the files themselves. Thus we shall be able to focus on the essence of each table. We shall systematically illustrate the definition of the tables by means of practical examples.

This appendix will be of interest to more people than just computer scientists. Large consumers of OpenType fonts will also find it valuable for the simple reason that current software products that are compatible with the OpenType font format use only a tiny percentage of its possibilities. Readers eager to know what OpenType has under the hood will find out in this appendix.

Appendix E is the logical continuation of Appendix D and the ideal complement to Chapter 13 on optimizing the rendering of fonts. In it, we describe the instructions of the TrueType assembly language. TrueType instructions have a reputation for being arcane and incomprehensible—a reputation due as much to their representation (in assembly language) as to their purpose (modifying the outline of a glyph to obtain a better rendering) and to some implied concepts (notably the concepts of projection vector, freedom

vector, twilight zones, etc.). And it is due most of all to the poor quality of the documentation supplied by Microsoft, which is enough to discourage even the most motivated programmer. We hope that this appendix will be easier to understand than the document that it cites and that it will be a helpful adjunct to Chapter 13.

We close with a brief introduction to Bézier curves, which are used again and again in the text (in discussions of font creation, the description of the PostScript and METAFONT languages, etc.). We have mentioned that most books on these languages give very little information on Bézier curves, often no more than the formula for the Bézier polynomial and a few properties. To compensate for the deficiency, we offer a genuine mathematical presentation of these objects, which today are indispensable for the description of fonts. The reader will find in this section the most important theorems and lemmas concerning these mathematical objects, with proofs to follow in due course.

The book ends with a bibliography that includes as many URLs as possible so that the reader can read the original documents or order copies of them. It also includes two indexes: the general index, for terms, and an index of names, which includes creators of software, font designers, and all other people mentioned for one reason or another.

This book contains introductions to certain technologies, “user’s manuals” for software, technical specifications, and even histories of fonts and encodings. It plays the dual role of textbook and reference manual. To help the reader derive the greatest benefit from it, we offer the following profiles of potential readers and, for each of these, a corresponding sequence of readings that we deem appropriate. Of course, these sequences are only recommendations, and the best approach to the book is always the one that the reader discovers on his own.

For the well-versed user of Unicode

The most interesting chapters will, of course, be Chapters 1 to 5. In order to use Unicode, a user needs suitable fonts. Once she has tracked them down on the Web, she will want to install them; thus reading Chapter 6, 7, or 8 (according to her operating system) may be of great benefit. And if she needs glyphs to represent characters not found in the fonts, she may wish to add them herself. Then she becomes a font designer/editor. (See “For the novice font designer”, below.)

For the devoted TEXist

Chapter 9 will be ideal. While reading it, he may wish to try his hand at input or output. For the former, he will want to prepare documents in Unicode and typeset them with Ω; therefore, we advise him to read the chapters on Unicode as well. For the latter, he may want to create fonts for use with TEX; thus he may benefit from Chapters 12 and 14, which discuss the creation of PostScript and TrueType fonts, or perhaps Appendix F, on the use of METAFONT.

For the reader who simply wants to produce beautiful documents

A beautiful document is, first and foremost, a well-coded document; it is useful, therefore, to know the workings of Unicode in order to use it to greatest advantage. Reading Chapters 2, 3, and 5 (and perhaps skimming over Chapter 4) is recommended. Next, a beautiful document must employ beautiful fonts. After reading the history of fonts (Chapter 11), the reader will be more capable of choosing fonts appropriate to a given document. Once she has found them, she will need to install them; to that end, she should read Chapter 6, 7, or 8, according to the operating system. Finally, to create a beautiful document, one needs high-quality typesetting software. If, by chance, the reader has chosen TEX (or Ω) to produce her document, reading Chapter 9 is a must.

For the reader who wishes to create beautiful Web pages

The sequence given in the preceding profile is recommended, with the difference that the last chapter should instead be Chapter 10, which discusses the Web.

For the typophile or collector of fonts

Chapter 11 will delight the reader with its wealth of examples, including some rather uncommon ones. But the true collector does not merely buy treasures and put them on a shelf. He spends his time living with them, adoring them, studying them, keeping them in good condition. The same goes for fonts, and font design/editing software is also excellent for getting to know a font better, studying it in all of its detail, and perhaps improving it, supplementing it, correcting its kerning pairs, etc. The reader will thus do well to read Chapter 12 carefully, and Chapters 13 and 14 as well. If technical problems arise, Appendices C and D will enable him to find a solution. Finally, to share his collection of fonts with his fellow connoisseurs, there is nothing like a beautiful Web page under GlyphGate to show the cherished glyphs to every visitor, without compromising security. Chapter 10 provides the necessary details.

For the novice font designer

Reading Chapter 11 may encourage her further and help her to find her place on the historic continuum of font design. This book does not give lessons in the graphical design of fonts, but it does describe the needed tools in great detail. Read Chapter 12 very carefully and then, before distributing the fonts you have created, read Chapters 13 and 14 to learn how to improve them even more.

For the experienced font designer

Chapters 11 and 12 will not be very instructive. In Chapters 13 and 14, however, he will find useful techniques for getting the most out of his beautiful font designs. He may also enjoy sampling the delights of METAFONT and creating PostScript fonts with METATYPE1 that would be very difficult or impossible to produce with a manual tool such as FontLab or FontForge. If he is a user of FontLab, he may also try his hand at the Python language and learn in Chapter 11 how to control the FontLab software through programming. If he already knows font design, instruction, and advanced typographical features, Appendices C and D will show him some of OpenType’s possibilities that will

surprise him because, for the time being, they are not exploited by OpenType-compatible software. Finally, reading the description of the Panose standard in Chapter 11 will enable him to classify his fonts correctly and thus facilitate their use.

For the developer of applications

Chapters 2 to 4 will teach her what she needs to know to make her applications compatible with Unicode. Next, Appendices C, D, and E will show her how to make them compatible with PostScript or OpenType fonts. Appendix G may prove useful in the writing of algorithms that make calculations from the Bézier curves that describe the outlines of glyphs.

For the reader who doesn’t match any of the preceding profiles

The outline presented in this introduction, together with the table of contents, may suggest a path to the information that interests him. If this information is very specific, the index may also come in handy. If necessary, the reader may also contact us at the address given below.

We have done our best to reread and verify all the information in this book, but we may nonetheless have failed to catch some errors in the course of production.3 Please point out any errors that you notice and share with us your suggestions for future editions of this book by writing to:

O’Reilly Media Inc. 1005 Gravenstein Highway North Sebastopol, CA 95472

You may also send us email. To join our mailing list or request a catalog, send a message to:

info@oreilly.com

To ask a technical question or send us your comments on the book, write to:

somebody@oreilly.com

This book has its own web site, where you will find all the code fragments that appear in the book, a list of errata, and plans for future editions. Please visit the following URL:

http://www.oreilly.com/somewhere/fonts-and-encodings.html

For more information on this book and its author, visit O’Reilly’s web site:

http://www.oreilly.com

3 On this subject, we recommend a hilarious book: An Embarrassment of Misprints: Comical and Disastrous Typos of the Centuries, by Max Hall (1995) [154].