---
title: "Chapter 13: Optimizing a Rasterization (Rasterization and Hinting)"
description: "Unabridged English text: The physics and mathematics of low-resolution font rendering; PostScript Type 1 hinting (alignment zones, BlueValues, stem hints, hint substitution, flex mechanism, counter hints); TrueType hinting virtual machine architecture (CVT, Twilight Zone, graphics state, instructions, delta hints, VTT and FontForge debugging)."
---

# Chapter 13: Optimizing a Rasterization
**By Yannis Haralambous, Ph.D.**
*From Fonts & Encodings, pp. 507–550*

---


<!-- Page 526 (Book page 506) -->
In a world peopled with fonts, we would read in Genesis: “for pixels thou art, and unto
pixels thou shalt return”. Indeed, we often forget that the ultimate goal of all the math-
ematical constructions that represent our glyph outlines is to produce images made from
pixels. If we had only one font size and only one resolution for our screens and printers,
we would have no need of outlines; the bitmaps would be quite suﬃcient. Outlines ex-
ist only to allow fonts to be adapted to the current situation and produce an adequate
bitmap on the ﬂy.
The process of moving from the “vector outline” state to the “bitmap” state is called
rasterization. It is a crucial process because the ﬁnal appearance of the text depends on it.
To understand the value of this chapter, we must examine how rasterization is done.
Since pixels are—fortunately—equidistant, we can imagine that beneath the geometri-
cally perfect outline of a glyph there is a grid each of whose squares has the size of one
pixel. Then rasterization involves ﬁlling in some of the squares of this grid to obtain as
faithful an approximation to the glyph’s outline as possible. Some of the squares—yes,
but which ones? Therein lies the problem.
We can adopt a methodical approach: for example, we can say that we shall ﬁll in any
pixel whose center lies inside the outline (or on the outline). This method is very frag-
ile: sometimes a very slight diﬀerence in an outline is enough to make the centers of
an entire row of pixels suddenly fall within the outline and thus be made black—or,
conversely, it may cause them to fall outside the outline and thus be made white. In the
example below, ﬁve versions of the letter ‘H’ with slightly diﬀerent heights have been
rasterized using the method of the centers of the pixels.
505

<!-- Page 527 (Book page 507) -->
The ﬁrst two have problems with diﬀerent thicknesses of strokes. In addition, the cross-
bar changes from 1 pixel to 2, and then, in the last two letters, back to 1 pixel again.
Conclusion: Even if the outline is perfect, the rasterization can ruin everything and cause
completely unpredictable behavior. We cannot just sit idly by and hope that some poorly
rendered glyphs will pass unnoticed. It is well known that as soon as something goes
wrong in typography, it will be noticed right away. Besides, it is, after all, unworthy of
our fonts: if we have spent hours creating impeccable outlines, we cannot accept poor
rasterizations. We have to take action—aggressive action!
Each of the three main font formats (PostScript Type 1, TrueType, METAFONT) oﬀers a
diﬀerent approach to this problem:
• In the case of METAFONT, rasterization—and everything else, for that matter—is
controlled through programming. The situation is quite unusual, as the bitmaps
are created by METAFONT before they are used. Provided that the characteristics of
a screen or a printer are known, METAFONT will generate bitmap fonts that are
adapted to it in advance. The rasterization will therefore be perfect, but the price
to pay for that perfect rasterization is total dependence on a certain kind of display
or printing hardware—the kind for which the bitmap fonts were generated. In the
day when METAFONT was developed, that constraint posed no problem at all: one
would prepare fonts speciﬁcally for one’s screen and printer. When one switched to
a new printer, one would ﬁgure out its characteristics somehow and generate new
fonts adapted appropriately.
But this balance fell apart with the advent of the Web: an “electronic document”
must be immediately and universally legible and printable. It cannot be restricted
to a particular type of output device. METAFONT is therefore incompatible with the
Web. We shall describe METAFONT’s approach in Appendix F.
• In the case of PostScript Type 1 or OpenType/CFF fonts, the rasterization is optimized
through the use of hints. Adobe’s strategy has been to refrain from stating exactly how
rasterization works and to give users nothing more than the possibility of vaguely
indicating some of the font’s characteristics, in the hope that the rendering engine
will see ﬁt to use them. This approach is often decried by programmers but was ac-
tually welcomed by font designers, since, in a certain way, it relieved them of the
responsability to optimize the rasterization of their fonts. For them it is enough to
give a few indications to the black box that is the rendering engine in order to make

<!-- Page 528 (Book page 508) -->
it “work”. And when “it doesn’t work”, Adobe will say that the designers are to blame
for not having supplied the correct hints, the designers will point a ﬁnger at Adobe,
and, if no other information surfaces, the matter will go no further. But none of that
is a serious problem, since PostScript fonts are used mainly in phototypesetting, and
hints are quite useless for that purpose because diﬀerences of one pixel in the thick-
ness of a stroke are too small for the human eye to detect. We shall give a technical
description of hints in Appendix C.
• TrueType fonts use TrueType instructions, a programming language akin to assembly
language, to deﬁne the behavior of rasterization relative to the grid. There is no
“black box”; everything is disclosed, explained, exposed. For that reason, TrueType
instructions are much more complex than hints. Predictably, TrueType instructions
have been ill received by font designers, since their manipulation calls for a great
deal of eﬀort and a way of organizing work that diﬀers greatly from the designers’
own habits. With the exception of some fonts from big foundries such as Mono-
type, which were instructed by engineers specialized in instructing fonts, most of
the TrueType fonts that we ﬁnd today are automatically instructed by font-design
software—which is a real pity, since much of the potential of instructions remains
unexploited. We have devoted all of Appendix E to the technical description of True-
Type instructions.
Since the technical descriptions appear in the appendices, we shall focus here on the
practical question “How do we place hints, or how do we instruct a font?” And, more
precisely, how to do so with tools such as FontLab, FontForge, and Visual TrueType (or
VTT, a program for instructing TrueType fonts that is distributed free of charge by Mi-
crosoft).
In this section we shall examine hinting, which is the placement of hints in PostScript
Type 1 or CFF fonts. In Figure 13-1, the reader can compare the same text in various ras-
terizations, three of them optimized with hints in diﬀerent ways and one not optimized
at all.
There are two types of PostScript hints: global hints, which aﬀect the entire font, and
individual hints, which aﬀect only a single glyph.
Global PostScript Hints
Of the global hints, two are very important: the alignment zones (i.e., the relevant heights
and the overshoots that go with them) and the relevant stroke thicknesses (see §C.3.4.1–
C.3.4.3). Some examples are shown in Figure 13-2. Thus it is necessary to “take inven-
tory” of the alignment zones and the stroke thicknesses that seem relevant: for a Latin
font, these are more or less classic; for another font, these must be determined by taking
measurements and trying to observe similarities and analogies. We shall see how Font-
Lab and FontForge can help us to identify the most relevant values.

<!-- Page 529 (Book page 509) -->




Figure 13-1: A comparison of various optimizations of the rasterization of a PostScript Type 1
font. The font is Monotype Old Style. Left: as rasterized by freetype with gray levels. Right: with-
out gray levels.  The font’s original hints.  The font without hints.  The hints generated by
FontForge.  The hints generated by FontLab. The text is from Goethe: “Ye wavering shapes,
again ye do enfold me / As erst upon my troubled sight ye stole,” etc.

::: tip Figure 13-1: A comparison of various optimizations of the rasterization of a PostScript Type 1 font. The font is Monotype Old Style
![Figure 13-1: A comparison of various optimizations of the rasterization of a PostScript Type 1 font (Monotype Old Style)](/images/fonts-encodings/fig13-1.png)
*Figure 13-1: A comparison of various optimizations of the rasterization of a PostScript Type 1 font. The font is Monotype Old Style.*
:::


<!-- Page 530 (Book page 510) -->







V1
V1
H3
H3
H2
H2
H4
H2
H2
H2
H1
V1
V1
V1
V2
V2
V2
V2
Figure 13-2: Some alignment zones: – the height of the capitals and the overshoot of the ‘O’;
– the height of the lowercase letters and the overshoot of the ‘o’; – the baseline and the
overhang of the ‘o’; – the baseline again, and the overhang of the ‘O’. Some relevant stroke
thicknesses: V1, the thickness of the vertical strokes and the curves (at the point where the tan-
gents are vertical) of the capital letters; V2, the same, for the lowercase letters; H1, the thickness
of the horizontal strokes of the capitals; H2, the thickness of the ‘E’ and the ‘H’, but also of the
curves of the ‘o’; H3, the thickness of the curves of the ‘O’ where the tangents are horizontal;
H4, the thickness of the top part of the ‘z’. The font shown here is Computer Modern Sans Serif.
Let us get a bit more technical: alignment zones are pairs of values: a “relevant height” and
an “overshoot”. They are stored in a PostScript font parameter called BlueValues. When
these zones lie completely below the baseline, they are instead stored in another param-
eter, called OtherBlues. Beyond these parameters, three others of lesser importance also
appear in PostScript fonts: BlueScale, BlueShift, and BlueFuzz. We shall describe them
in §C.3.4.1. Finally, there is one other boolean parameter, which has the advantage of
being easily to understand, even for those who do not know much about how the raster-
izing engine goes about using it: ForceBold. This parameter indicates to the rasterizing
engine that the font is bold and that the rasterization should be made “heavy” (so that
the diﬀerence between the font and any possible light version will be immediately evi-
dent).
The relevant stroke thicknesses are stored in the following manner: the “most relevant”
horizontal stroke thickness is stored in a parameter called StdHW, and its vertical counter-
part is stored in StdVW; all other horizontal and vertical stroke thicknesses are stored in
two other parameters, StemSnapH and StemSnapV. Note that there can be no more than
twelve stroke thicknesses in each direction.
Now, here is how FontLab and FontForge manage global hints.
FontLab and global hints
In FontLab, we enter the following three types of data about global hints under three
tabs of the font-information window (File>Font Info):
• Hinting: alignment zones (see Figure 13-3 [a]): the two lists Primary zones and Secondary
zones contain the alignment zones for BlueValues and OtherBlues (the latter lie

::: tip Figure 13-2: Some alignment zones: (1) the height of the capitals and the overshoot of the 'O'; (2) the height of the lowercase letters and the overshoot of the 'o'; (3) the baseline and the bottom overshoot of 'o' and 'p'; (4) the bottom of the descenders and the overshoot of 'p'
![Figure 13-2: Some alignment zones](/images/fonts-encodings/fig13-2.png)
*Figure 13-2: Some alignment zones: (1) the height of the capitals and the overshoot of the 'O'; (2) the height of the lowercase letters and the overshoot of the 'o'; (3) the baseline and the bottom overshoot of 'o' and 'p'; (4) the bottom of the descenders and the overshoot of 'p'.*
:::


<!-- Page 531 (Book page 511) -->
(a)
(b)
(c)
Figure 13-3: The tabs “Hinting Settings”, “Hinting Settings: Standard stems”, and “Additional
hinting parameters”.

::: tip Figure 13-3: The tabs 'Hinting Settings', 'Hinting Settings: Standard stems', and 'Additional hinting parameters'
![Figure 13-3: FontLab Hinting Settings tabs](/images/fonts-encodings/fig13-3.png)
*Figure 13-3: The tabs 'Hinting Settings', 'Hinting Settings: Standard stems', and 'Additional hinting parameters'.*
:::


<!-- Page 532 (Book page 512) -->
completely below the baseline). Clicking on the button Auto zones causes FontLab
to take the measurements and ﬁll in the two lists for us.
• Hints: standard stems (see Figure 13-3 [b]): we enter in V Stems relevant thicknesses
of the vertical stems (the ﬁrst goes in StdVW, the rest go in StemSnapV) and, like-
wise, the thicknesses of the horizontal strokes in H Stems. The ForceBold checkbox
enables this property. Clicking on the button Auto stems causes FontLab to take the
measurements for us and ﬁll in the two lists as it sees ﬁt.
• Additional hinting parameters (see Figure 13-3 [c]): we supply values for the parameters
ForceBoldThreshold, BlueScale, BlueShift, BlueFuzz.
FontForge and global hints
In FontForge, the management of global hints
is, as one might expect, both less pleasant and
more powerful than in FontLab. The data are
entered under a single tab of the font-information
window (Element>Font Info>PS Private Dic-
tionary), shown opposite.
In the top part of the window, we choose the
parameter that we wish to modify: BlueValues
(alignment zones), OtherBlues (alignment zones
beneath the baseline), BlueScale, BlueShift,
BlueFuzz, StdHW (the most relevant horizon-
tal stroke thickness), StdVW (ditto, but vertical),
ForceBold (whose value must be either false or
true). Other than ForceBold, the values that we
supply to FontForge must be written in PostScript’s tabular syntax, i.e., in the form of
numbers separated by spaces, with brackets around the whole entry.
The reader must be wondering what happened to the other relevant stroke thicknesses
(StemSnapV, StemSnapH). Clicking on the Add button reveals other parameters, in-
cluding these two, from the “private” part of the PostScript Type 1 or CFF font. There
are even parameters speciﬁc to the ideographic scripts, such as ExpansionFactor and
LanguageGroup (see §C.3.4.3) and all the rest.
The functionality for the parameters for alignment zones and relevant stroke thicknesses
is the same as in FontLab: there is a Guess button, which will take the measurements for
us and supply values for these parameters. But FontForge goes further! For each of these
parameters there is a Hist (histogram) button; when we click on this button, FontForge
shows us an interactive histogram:

<!-- Page 533 (Book page 513) -->
In the ﬁgure above, we see the histogram for the vertical stroke thickness parameter. In
the Bar Width input area, we can specify the width of the histogram’s bars. That might
seem pointless: why should we want to change the width of the bars in the histogram?
Well, as with everything else in FontForge, there is a reason: the bars of the histogram
are, in fact, interactive. When we slide over a bar, a small text box appears with a great
deal of information: what is the exact value of the bar? How many glyphs have this same
value? Even better: which glyphs have this value?
Then, when we click on the bar, its value becomes the primary value (here StdVW).
Clicking with the shift key depressed adds the value to the secondary values (here Stem-
SnapV).
Finally, the parameter Sum Around is also very interesting: it “blows up” the histogram
and thus allows for a better understanding of the clustering of data by eliminating iso-
lated extreme values.
Individual PostScript Hints
As their name shows, individual hints are deﬁned at the level of each glyph. The basic
idea is very simple: we tell the rasterizing engine which are the relevant horizontal and
vertical strokes. The rasterizing engine detects strokes that appear at the indicated coor-
dinates and arranges for them to have the same thickness in pixels, irrespective of the
location of the centers of the adjacent pixels. The reason for the name “hint” is now clear:
we hint to the rasterizing engine which strokes should have the same thickness, either
within a single glyph or over all the glyphs in the font. Then the rendering engine will
manage to perform its task correctly, respecting at all costs the directions that we have
given.
Unfortunately, that does not work as well as one might wish: there are complications and
special cases to handle. The complications result from the way in which hints are deﬁned:
rather than connecting them to precise nodes on the glyph, Adobe preferred to consider

<!-- Page 534 (Book page 514) -->
hints as vertical or horizontal zones in such a way that all the strokes that coincide with
these zones are optimized. The intention was noble, but the approach works only if the
zones deﬁned by the individual hints do not touch. For example, in the letter ‘H’, the
zones that will optimize the two stems do not touch, and so everything works perfectly.
But there are cases in which zones will inevitably touch. Take the letter ‘B’ below:
1
2
3
There are three vertical zones. By the very nature of the letter ‘B’, zones 2 and 3 will
inevitably overlap. What should we do in this case? To solve this speciﬁc problem in
Type 1 fonts, Adobe invented a horribly complicated method called “hint replacement”.
This method involves enabling and disabling, while the glyph is being traced, the hints
that overlap. That is one of the major diﬃculties in placing hints. We shall describe hint
replacement in §C.3.6.1 of this book. The situation is better for Type 2 (OpenType/CFF)
fonts: we must still do “hint replacement”, but the relevant structure and syntax are much
more rational (see §C.8.2.1).
The special cases that arise with hints come from a visual characteristic of the glyphs:
the fact that the symmetry between stems also extends to the white counters between
them. Take the example of the letter ‘m’: the stems of this letter must, of course, have the
same width, but that also applies to the two white spaces that separate them. It is just as
important to ensure that the two “crotches” of the ‘m’ have exactly the same width, in
pixels. But hints operate only on strokes, not on counters.
Adobe tried to solve this problem in two steps. The ﬁrst measure taken aﬀects only con-
ﬁgurations of three parallel stems, as in ‘m’, the Greek ‘Ξ’, the Cyrillic letters ‘Ш’, ‘ш’, ‘Щ’,
‘щ’, the symbol ≡, ideographs such as 三, 且, 山, 彐, 日, 王, 田, etc. It involved an operator
(by the name of hstem3 or vstem3; see §C.3.6) to which we would supply three hint zones,
and the blank spaces between these zones would be equalized.
But Adobe quickly realized that handling conﬁgurations of three strokes was not
enough! One need only consider ideographs such as 皿, 目(4 strokes), 冒(7 strokes),
etc., to convince oneself that more powerful operators are needed. Moreover, when the
number of strokes runs that high, we realize that the danger is not so much that we
may have unequal white spaces but rather that there may not be any white spaces at all.
Indeed, the rasterization at a low resolution of a glyph such as 癴is a real challenge,
one that rasterizing engines in East Asia must face every day. Accordingly, Adobe’s
second attempt involved developing a system—once again inordinately complicated—
to manage situations of this kind (§C.3.6.2). This system was named “counter control”

<!-- Page 535 (Book page 515) -->
Figure 13-4: Displaying individual hints in FontLab.
and was used only in East Asian fonts. Only with the advent of Type 2 (OpenType/CFF)
fonts did Adobe ﬁnally provide a stable and robust operator to perform operations of
this type (§C.8.2.1).
We have presented a quick overview of the properties of individual hints. Now let us see
how they are implemented in the two large software packages FontLab and FontForge.
FontLab and individual hints
To display PostScript hints in FontLab, select Tools>Hints & Guides>Type 1 Hinting.
This will open the Type 1 Hinting button bar and display the hinting lines as pairs of
green lines (see Figure 13-4). Finally, by clicking on the button
on this button bar, we
obtain a display of specimens at various sizes.
It is very easy to add hints to a glyph in FontLab. Simply place the cursor over a ruler
(a horizontal one for a horizontal hint; otherwise a vertical one) and press the ° key
(under Mac OS X; Ctrl under Windows). Then drag the pair of lines until one of them
is in the right place. Next, hold down the shift key and move the other line until the hint
zone has the correct width. To delete a hint, select the entry Delete on the pop-up menu
for one of these two lines.
The pop-up menu for hints also allows us to specify precisely the hint’s coordinates
(Properties), change its direction (Reverse), and even turn the hint’s value into a global
alignment zone for the font (by means of the option Define Stem).
That is all very useful, but FontLab goes further! It introduces a new notion, that of the
link. Through this new notion, FontLab aims to correct Adobe’s bad decision to regard

::: tip Figure 13-4: Displaying individual hints in FontLab
![Figure 13-4: Displaying individual hints in FontLab](/images/fonts-encodings/fig13-4.png)
*Figure 13-4: Displaying individual hints in FontLab.*
:::


<!-- Page 536 (Book page 516) -->
hints as abstract zones independent of the glyph’s outline. A link is a hint attached to nodes
of the outline. If these nodes are moved (either manually or through programming), the
corresponding hint will also be moved. Thus it is safer to work with links, which FontLab
will, in any event, translate into hints when a Type 1 or Type 2 (OpenType/CFF) font is
generated.
Links (horizontal and vertical) are inserted by means of Tools>Hints & Guides>Add
New Horizontal Link and Tools>Hints & Guides>Add New Vertical Link. We can
also replace a hint with a link or vice versa by using the options Convert to Link and
Convert to Hint on the pop-up menu for the hint or the link. This conversion can also
be applied to all the hints and links of one or more glyphs, by means of Tools>Hints &
Guides>Convert Hints to Links or the opposite.
But beware: automatic conversions cannot perform miracles! A link is, by deﬁnition, a
pair of nodes traversed by two lines for a hint’s zone. When we ask FontLab to convert
a hint to a link, it will ﬁrst check whether there are indeed nodes on the two lines for
the hint. If there are not, as sometimes happens in poorly optimized fonts, the hint will
remain a hint, and FontLab will not issue an error message or otherwise complain. Thus
we should supervise this operation carefully.
The Tools>Hints
&
Guides menu
also allows us to initiate autohint-
ing. But beware: before using this
command, it would behoove you to
check its conﬁguration panel File>
Font
Info>Hinting
Settings>T1
Autohinting.
The numeric values in this conﬁguration panel are of little importance, except perhaps in
extreme cases: for example, if the font has very thin strokes, Min width must be reduced;
if it has very thick strokes, increase Max width; if you want more hints globally, reduce
Min length. What is also really important is to select Tools>Hints & Guides>Remove
Hints>Both, since FontLab will otherwise add new hints to the old ones, thus making
the situation catastrophic. In Figure 13-1, the reader can compare the results of FontLab
autohinting to the lack of hints and to the analogous operation in FontForge.
Finally, a few words on hint replacement, a problem due to a poor deﬁnition of the con-
cept of hints. We have seen that “hint zones”, i.e., the pairs of horizontal or vertical lines
that indicate the relevant strokes in a glyph, are deﬁned for the entire working area of the
glyph. In Figure 516, we see at the left the hint zone that corresponds to the lower bowl
of the ‘B’ and, at the right, the zone that corresponds to the upper bowl. Obviously these
two hint zones do touch, thus running counter to the deﬁnition of hints. What can we
do so that when rasterizing the lower part of the glyph the rasterizing engine will ignore
the upper part, and vice versa?
The solution is as follows: ﬁrst we divide up the outline of the letter, then we “attach”
hints to the various segments. When there is a hint within a given group of segments, we

<!-- Page 537 (Book page 517) -->
Active outline segment
Active hint
Replacement point of active hint
Active outline segment
Active hint
Replacement point of active hint
Other active hint
Segment 1
Segment 2
Figure 13-5: Hint replacement in FontLab.
attach the hint to this group. The rasterizing engine will process each group separately,
taking into account only the hints attached to the segment being processed.
To divide an outline into segments, we use “replacement points”. Here is how to do so
in FontLab. We set the hints by hand. When two hint zones overlap, their intersection is
displayed in yellow. Then we select the ﬁrst node of a segment of the outline and choose
on its pop-up menu Add replace point here. FontLab segments the outline and auto-
matically attaches to this segment of the outline the hints that it considers relevant.
In Figure 13-5, we see the glyph window for the letter ‘B’ with four manually inserted
replacement points. At the left we see the ﬁrst segment of the outline (in black, whereas
the rest of the outline is in gray); at the right, the second segment. The hint zones are the
zones attached to the active segment; the software shows them in dark green. We see that
there is only one hint zone at the left, while there are two at the right, since the segment
also contains the left part of the letter. Hint zones can be attached to multiple outlines:
for example, the internal outlines are attached to all the hints that touch them.
We can intervene if FontLab has attached hints to the segments of an outline incorrectly.
To do so by hand, we activate the segment in question and, on the hint’s pop-up menu,
select Add this vertical hint (or Add this horizontal hint if it is horizontal), and the
task is done.
The tedious operations that we have just described are fortunately quite rare. During
automatic optimization of a rasterization, FontLab automatically applies this sort of
method whenever hints overlap. Nonetheless, it is recommended that the user verify
the choice of replacement points: it is easy to do once the principle is understood, and

::: tip Figure 13-5: Hint replacement in FontLab
![Figure 13-5: Hint replacement in FontLab](/images/fonts-encodings/fig13-5.png)
*Figure 13-5: Hint replacement in FontLab.*
:::


<!-- Page 538 (Book page 518) -->
FontLab does what is needed to make the glyphs with overlapping hints easy to detect:
the disputed area is painted yellow.
FontForge and individual hints
Figure 13-6: The management of individual hints in FontForge.
The management of individual hints in FontForge is a little less powerful than in Font-
Lab. It is true that FontForge has a very eﬃcient autohinting feature (Hints>AutoHint),
but, on the other hand, there are few possibilities for manual intervention. The hint
zones are marked with dotted lines and colored sky blue. The intersection of a hint zone
with a vertical or horizontal stroke is colored purple (for a vertical hint) or green (for a
horizontal hint).
Using Hints>Review Hints, one can modify the coordinates of the hint zones or add
or subtract hint zones. But those actions are done with coordinates, not with the mouse;
we are thus far from the pleasant interface of FontLab, where we can create hints and set
their positions in a few seconds, by simply moving the mouse.
When two hint zones overlap, the word “Overlap” appears in the Review Hints dia-
log box. FontForge will automatically divide the outline into segments and place the
replacement points for the hints—but there is no visible evidence of this operation, nor
any possibility of manual intervention.

::: tip Figure 13-6: The management of individual hints in FontForge
![Figure 13-6: The management of individual hints in FontForge](/images/fonts-encodings/fig13-6.png)
*Figure 13-6: The management of individual hints in FontForge.*
:::


<!-- Page 539 (Book page 519) -->
TrueType instructions are the means that we have for optimizing the rasterization of
glyphs in a TrueType font. Unlike PostScript hints, they are not values of parameters or
graphical zones but a genuine programming language. Furthermore, the view that font
designers have of TrueType instructions is not very diﬀerent from Freud’s opinion of the
unconscious: “a cave where repressed desires move around in the dark”. Indeed, the sight
of hundreds of lines of code of this type:
MIRP[00100]
MIRP[10100]
MIRP[01110]
SRP1[ ]
SRP2[ ]
SLOOP[ ]
is enough to make anyone, not just a technophobe, break out in a cold sweat.
But is this cold sweat justiﬁed?
It is true that, unlike Adobe, Apple—which sparked the development of the TrueType
instructions—has always been partial to “hard” notation in computer science, perhaps to
highlight the contrast between the roles of Macintosh “user” (who communicates with
his machine through menus and dialog boxes) and “programmer” (who stumbled into
assembly language as a child).
We might have envisioned a high-level language that, when compiled, would produce
the assembly code for the instructions of today; after all, that is precisely what Knuth
did with METAFONT (see Appendix F). This high-level language does not yet exist and,
no doubt, never will. Nonetheless, various tools have been created to make up for this
deﬁciency: FontLab oﬀers a simpliﬁed version of instructions with a graphical interface;
Visual TrueType, by Microsoft, oﬀers a graphical interface that is a veritable factory for
instructions; and FontForge oﬀers a built-in programming environment with an inter-
active debugger.
Not to mention that both FontLab and FontForge pride themselves on automatically
generating instructions for our fonts. As often happens in life, we have the choice of
• A quick solution (just a click on the button for automatically generating instruc-
tions), without troubling ourselves much over the details
• Or a method that gives us more room for maneuver, with a concomitantly greater
investment required on our part
• Or, ﬁnally, a diﬃcult method that gives us 100 percent control over the rasterization
of our glyphs and also 100 percent of the responsibility for the result but that requires
extensive study of a nontrivial technique

<!-- Page 540 (Book page 520) -->
In this section, we shall adopt the second solution: a small dose of technical learning
through which we will gain control over the situation. For those who dare to pursue the
third course, we have written a very thorough description of instructions, illustrated by
real-world examples: it is Appendix E of this book.
The principle of instructions is as follows: to optimize the rasterization of a glyph, we
change the shape of its vector outline. The change involves modifying the underlying grid of
pixels. Then we will obtain a new outline, more or less diﬀerent from the original one, for
each grid, and thus for each size of glyph. We call this new outline the grid-ﬁtted outline.
It must be understood that the grid-ﬁtted outline will not necessarily be as beautiful as
the original outline. After all, no one will ever see it, since it exists only to yield a good
rasterization. Once the grid-ﬁtted outline has been obtained, the rasterization engine
need only apply the rule about the centers of the pixels (blacken the pixel if its center
lies within the outline, else leave it white) in a strict, even stupid, manner, and the job
is done.
Why should one bother to obtain an outline customized for each size when it would
be enough to activate or disactivate pixels? Because the customized outline, unlike the
original outline, is not designed speciﬁcally by the font’s designer; on the contrary, it is
produced automatically by means of a number of rules. By stating these rules, we obtain
all the customized outlines for every size. In fact, this rule is not absolute, as there is
indeed a way (we call it a δ instruction) to modify the individual outlines customized
for certain sizes. But it is the exception, and in most cases a few rules for customizing the
outline are enough to render all glyph sizes correctly.
The goal of instructions is to express these rules (and their exceptions).
How should we go about altering an outline? For the TrueType language, an outline is
nothing more than a series of points, some of which (the nodes) lie on the curve and oth-
ers (the control points) oﬀthe curve. An outline can be modiﬁed only by manipulating
these points.
Let us summarize: instructions move the points of the outline to form a new outline
customized for the rasterization of the glyph at a given size.
Next question: how can we know how much to move a point, and in which direction?
There are (at least) three possible cases:
• Some points are simply aligned relative to one of the edges, or to the center, of the
pixel that contains them. We shall say that these points have been “touched”, in the
sense that they have been moved and now appear in the correct location. A touched
point will not be moved again (which does not cause problems, as we can always
“untouch” a point if necessary).
• Other points will be set at an appropriate distance from a touched point. The appro-
priate distances in a list of values called CVT (for “Control Value Table”), which is
found in the TrueType table cvt. When we move two points so that they are set at an
appropriate distance, this distance is always at least one pixel; thus we have a property
for the minimum distance.

<!-- Page 541 (Book page 521) -->
• Still other points—and these form the silent masses, the proletariat of the glyph—
are not involved directly but take part passively in the movement of other points. In
other words, they do what the other points do, no questions asked. They can imitate
the movement of another point or even interpolate the movement of several other
points. In addition, there is a “magical” instruction that causes the interpolation of
all the points that have not been touched.
Already we see in broad strokes how the instruction of a glyph is done: we start by selecting
some points that will be aligned relative to the pixel that contains them; then we apply a
number of appropriate distances (stroke thicknesses, relevant heights, breadths of serifs,
etc.); next we interpolate the points that depend on two or more of the points that have
been moved; ﬁnally, we interpolate all the other points.
Now that we have explained the general principle, let us move on without delay to the
management of instructions by the chief software systems. We shall see how each of them
manages instructions in a diﬀerent way, with its own advantages and disadvantages.
Managing Instructions in FontLab
It is clear that FontLab has undertaken an enormous eﬀort in the area of the design
of instructions and of their human interface, even though it provides only a simpliﬁed
version of instructions. FontLab has succeeded in reducing the essence of the instructions
to six visual operations called visual hints:1alignments, links, double links, interpolations,
and two types of δ instructions: medial δs and ﬁnal δs. With these six operations, the user
can instruct her font and view the rasterization in real time. When a TrueType font is
generated, the visual hints are converted into genuine TrueType instructions.
What is striking about visual hints is the blend between the concepts of instructions
(alignments, interpolations, δ instructions) and those of PostScript hints: links, intro-
duced by FontLab as an improvement to the concept of a hint zone. Indeed, FontLab
considers hints as a sort of preliminary step to instructions. For instance, global hints
(relevant heights, relevant stroke thicknesses, etc.) are used in PostScript and TrueType
alike. Moreover, FontLab has no direct function for automatically optimizing a rasteri-
zation through the use of instructions; instead, we ﬁnd, on the one hand, optimization
through the addition of hints and, on the other, an operation for converting hints into
visual hints.
The user interface
The interface for managing instructions in FontLab deserves some discussion. At ﬁrst
blush it may give the impression of being a “juggernaut”; but when we become familiar
with its tools, we ﬁnd that they are all useful and that the various methods for represent-
ing information are actually complementary and globally eﬀective. Because we should
not deceive ourselves: a user interface that claims to present to the user all the informa-
tion about the instructions of a given glyph (at a given size) should be able to display,
1 Not to be confused with Microsoft’s Visual TrueType operations, which are also called visual hints and
which we shall study in the section dedicated to this software.

<!-- Page 542 (Book page 522) -->
Figure 13-7: Managing visual hints in FontLab.
all at the same time, the original outline, the customized outline, the resulting rasteriza-
tion, the grid of pixels (with their centers, the baseline, and the alignment zones clearly
displayed), the six types of visual hints represented by diﬀerent symbols, and, ﬁnally, the
rasterization of the glyph at its actual size, since what seems horrible at a large size is
often impeccable at the actual size. Representing all this information simultaneously is
a real challenge, and we can say that FontLab is well up to the task.
In Figure 13-7, we see FontLab’s basic working environment for visual hints. To switch to
“instruction” mode, we need only select Tools>Hints & Guides>TrueType Hinting.
Then the TrueType Tools, shown above and to the left, appears, together with the
TrueType Options dialog box, which is shown immediately below.
To see the diﬀerent layers of information and the two other windows that appear to
the right of the glyph, we use the last button at the right end of the bar, the button
.
Clicking on this button opens a pull-down menu with the following options:
• Hinted outline: show the glyph’s customized outline. To see it, pay close attention
to Figure 13-7: the hinted outline is the gray one shown inside the black outline,
marked with node numbers. The hinted outline depends on instructions and is up-
dated whenever the instructions are modiﬁed.
• Grid lines: show the grid. The ﬁrst option in the TrueType Options box (Current
PPM, or “current pixels per em”) shows us the size of the glyph. In the ﬁgure, the
glyph is of size2 15, with a set-width of 11 pixels.
2 Recall that we speak of “size” when we measure the height of a glyph in pixels and of “actual size” when
we measure it in points.

::: tip Figure 13-7: Managing visual hints in FontLab
![Figure 13-7: Managing visual hints in FontLab](/images/fonts-encodings/fig13-7.png)
*Figure 13-7: Managing visual hints in FontLab.*
:::


<!-- Page 543 (Book page 523) -->
• Pixel centers: mark the center of each pixel on the grid with a dot. This feature is
not oﬀered for ornamental purposes. As we know, a pixel in the ﬁnal outline will be
black if its center lies inside the modiﬁed outline. Thus it is quite important to know
where the centers of the pixels lie with respect to the modiﬁed outline so that we can
insert a δ instruction that will make a pixel black or white by slightly modifying the
outline. In addition, we see in the image that the pixels (2,3) and (4,3) came within
a hair’s breadth of being made black, which would have made the curve’s descent
too dark.
• Resulting image: show the pixels of our rasterization—an indispensable option.
• Point numbers: show the point numbers. This option is useful only when com-
bined with the TrueType Program window, which we shall discuss just below.
• Program panel: open the TrueType Program window. This box shows us a list
of all the visual hints for the glyph, in the order in which they will be executed.
Clicking on an instruction causes it to be shown in bright red within the glyph. The
bottom part of the window allows us to modify the instructions and see the result by
clicking on Apply. This window is a good compromise between the syntactic horrors
of the real TrueType instructions and the graphical representation of visual hints
within the glyph: the list of instructions gives a good summary of the method of
optimization that was followed, and the possibility of manipulating the parameters
of the instructions gives us total control over them without going through the glyph’s
representation.
• Finally, Preview panel: open the TrueType Preview window, which will display a
number of sizes of the active glyph and also a characteristic sentence—for example,
a pangram (see page 721, note 7, for a series of examples of pangrams). The little
pull-down menu at the right (available only under Windows) allows us to move
from display without gray levels to display with gray levels, and even a display using
ClearType, a new display technology in Windows. Display with gray levels or through
ClearType often masks the imperfections of the rendering; thus it behooves us to be
strict with ourselves and approach the rasterization of our glyphs in their pure state,
with no embellishment.
Of the buttons in TrueType Tools, there are two whose eﬀect is global: the button
displays vertical visual hints (i.e., those that apply to horizontal strokes), and
displays
horizontal visual hints (applied to vertical strokes). The eﬀect of these buttons is not
conﬁned to display: we can even switch outright from a “vertical mode” to a “horizontal
mode”. According to the active mode, the buttons that we shall discuss below will pro-
duce horizontal or vertical visual hints.
Now let us take another look at the diﬀerent types of visual hints and their manipulation.
Alignments
Alignments are made with the button
. They are horizontal or vertical, according to the
active mode. The term “alignment” is a bit unfortunate: here it refers not to aligning two

<!-- Page 544 (Book page 524) -->
points with each other but rather to aligning a point with respect to the boundary or
center of a pixel. It would be more correct to speak of “rounding relative to the grid”. In
any event, alignment is often the ﬁrst operation that we perform (moreover, it is always
executed ﬁrst, as the reader will notice on the list in the TrueType Program window).
It consists of the “correct” placement of an initial point, from which we will then place
other points.
To “align” a point, we click on the button
and then choose the ap-
propriate method of rounding in the group of buttons that appears
in the middle of the TrueType Option window, shown opposite.
The ﬁrst three buttons mean, respectively, “place the point on the
nearest pixel boundary” (for vertical alignment, that would mean
moving the point up if it appeared above the center of the pixel and down if it appeared
below the center), “place the point at the bottom of the pixel” (the left side, in horizontal
mode), and “place the point at the top of the pixel” (the right). The two buttons below
are used for more sophisticated alignment: Center means that the point will be identi-
ﬁed with the center of the pixel that contains it. We thus obtain a pixel surrounding the
point, whatever the circumstances of the rasterization may be; that may prove useful, for
example, for the point of the letter ‘v’, which should be “as pointed as possible”. Finally,
Double means that we will round according to a grid twice as ﬁne as the current grid:
the point will be moved either to the edge or to the middle of the pixel. Thus we can
manage cases in which we must place a point in the middle of a row of pixels when we
do not know whether the number of those pixels is even or odd. (We shall see below that
a more natural way to do it is to use interpolation.)
Having chosen the type of rounding, we click on the point that we wish to “align”. A little
blue symbol around the point represents this procedure, and a new line will be added
to the list of visual hints in the TrueType Program window.
In vertical mode, there is another type of alignment for points: alignment with respect
to a hint zone. Let us recall what a hint zone is: a relevant height (the baseline, the height
of the lowercase letters, the height of the capitals, etc.) and its overshoot (the little part
that extends over the limit when the letter is round). Hint zones are part of the global
hints. FontLab stores these data under the Hinting Settings tab in the File>Font Info
window. Thus it is quite useful to go to this window and request automatic generation
of the hint zones by clicking on Auto zones.
When in vertical mode we click on a point in order to “align” it, if the point lies in a
hint zone, it will be automatically aligned relative to that zone, and rounding is done
in the direction of the relevant height. We can prevent this automatic behavior by hold-
ing down the shift key while we click.
One last comment: aside from the points of the outline (the nodes and the control
points), two other types of points can be manipulated—the glyph’s origin and its set-
width. The origin is always “aligned”, but there is no reason that the set-width should
also be so aligned. If our glyph is symmetrical (like the ‘O’ in Figure 13-7), we should
reﬂect on the left side of the glyph the behavior of the right side. To this end, the least
that we can ask is for the point representing the glyph’s set-width to be “aligned” as well.

<!-- Page 545 (Book page 525) -->
Single and double links
Links follow the same principle as PostScript hints: they “link” two points in such a way
that their distance is handled in a certain manner, whatever the size of the glyph may be.
What exactly is this treatment? It depends on the link’s type. We have already said that
there are “single” and “double” links. A single link is a link whose starting point must be
a touched point, whereas its ending point must not be one. The most interesting single
links are those that are connected to a relevant distance. Let us explain. While discussing
PostScript hints, we mentioned relevant stroke thicknesses. We can generalize this con-
cept and say that in a font there are some distances that are used in multiple glyphs
and that guarantee the font’s aesthetic uniformity. For instance, it may happen that the
counter of an ‘n’ in a given font is equal to those of the ‘m’ or that the breadth of the ‘O’
is the same as that of the ‘Q’.
We can store dimensions of this kind and use them to create inter-
esting links. To do so, we click on the ellipsis in the top part of the
TrueType Options window, shown opposite.
The window below then appears:
Each line on the list corresponds to a relevant dimension. The lines on a clear back-
ground correspond to vertical dimensions; those on a yellow background, to horizontal
ones. The name of the relevant dimension is also shown in the glyph’s window each time
a link makes use of the dimension. The second column contains the dimension’s value.
The other columns contain the size of the glyph, in pixels, at which the dimension in
question changes from 1 to 2 pixels, then from 2 to 3 pixels, and so on, up to 6 pixels.
(The diﬀerence in stroke width is assumed to be insigniﬁcant from 6 pixels onwards.)
By clicking on a line, we can edit it—in the bottom of the window. For example, we can
specify precisely the moment at which a new pixel will be added to the dimension, and
our speciﬁcation will apply to the entire font.
To establish a single link, we click on the button
(a yellow circle) on the bar True-
Type Tools. Then we determine, in the window TrueType Options, how this link will
be connected to a relevant dimension: should FontLab automatically ﬁnd the nearest
relevant dimension (Automatic)? Is there no relevant dimension that is connected to

<!-- Page 546 (Book page 526) -->
this link (None)? We can also designate the relevant dimension on the pull-down menu.
Finally, we click on the link’s starting point (remember, it must be a touched point) and
drag it to the starting point (which must not be a touched point). The ending point will
then be touched.
To respect the constraint “touched






  4
36
point at the start, nontouched point
at the end”, we must sometimes deﬁne
the links in a certain order. Take the
example of the letter ‘m’ shown oppo-
site. We start with the ﬁve links , ,
, , and , which must be deﬁned in
that order. Point 4 is the starting point
of link ; it is “aligned” on the left
edge of the pixel. This optimization
that the stems and the counters will
be of uniform width. But this very
uniformity causes the width of the glyph to vary greatly, and that is why we have added
a sixth link, , which connects point 36 to the glyph’s set-width. This link does not
correspond to any relevant dimension.
The reader must certainly be wondering of what use a link that is not connected to any
relevant dimension can be. Do not forget that a link “joins” its ending point to the rest
of the outline and that, were it not for the link, the point could appear too close or
too far away if the outline were signiﬁcantly modiﬁed. We have prepared two exam-
ples, drawn from the optimization of this same letter, ‘m’. We use a heavy vertical stroke
to represent the set-width of the optimized glyph and a broken stroke to represent the
glyph’s original set-width. The image on the left is that of the glyph without link ; the
image on the right includes this link.
At 9 points, without link  the customized outline is much wider, which causes the op-
timized set-width (which is nothing but a rounded version of the original set-width) to
be too narrow and the right-hand side bearing to be missing altogether:

<!-- Page 547 (Book page 527) -->
Conversely, at 12 points, the customized outline is much narrower (because the stroke
widths are always one pixel and the counters always two pixels) and the set-width is too
wide,3 giving a right-hand side bearing of 3 (!) pixels:
In these two examples, the addition of link  restores the situation and shows the utility
of a link that is not connected to any relevant dimension.
In addition to single links, we also have double links. Their peculiarity lies in the fact that
they are placed between two non-touched points—which, consequently, become touched.
Establishing a relationship between a double link and a relevant dimension works just
as with a single link.
What does it mean to say that the two points of the double
link must not have been touched? It means that the double
link is, in a sense, “independent” of everything else—that it
is not its position that matters but its dimension. For example,
we shall place double links on the two sides of the letter ‘O’—
links connected to the dimension “thick stroke of the ‘O’ ”,
shown opposite.
What matters here is not the width of the ‘O’ but the fact that
its two sides have exactly the same width, and that is what the
two double links ensure.
To establish a double link, we click on the button
(a blue circle) on the TrueType
Tools bar and then proceed as with a single link.
Should we use single or double links? Both are useful, but often we achieve a good result
with less eﬀort by using double links.
Interpolations
This operation allows us to interpolate the movement of a point relative to those of two
other points. We have already mentioned that all the nontouched points are interpolated
relative to the touched points anyway at the end of the optimization process. The diﬀer-
ence here is that, ﬁrst, this interpolation is done before the execution of the links and,
3 We could have requested, through the control table for the relevant dimensions, that the counters of
the ‘m’ increase to 3 pixels starting at 12 points (in the example in question, that happens only at 14 points).
That would have produced a wider glyph. It is up to the designer to choose the less unattractive solution. Note
that a decision of that sort would also have had repercussions on a plethora of other glyphs (the ‘n’, the ‘h’, etc.)
that use the same relevant dimension.

<!-- Page 548 (Book page 528) -->
second, rather than relying on automatic interpolation, which is based on the nearest
points, we can perform interpolation here relative to carefully chosen points—points
that may be arbitrarily far away.
To interpolate a point c relative to two points a and b, we ﬁrst click on the button
(a
green circle) on the TrueType Tools bar. Then we click on a, drag it to c, and click on b.
δ instructions
FontLab adopted unchanged the technique of δ instructions as it is deﬁned in the True-
Type speciﬁcation. The intention is noble, but one small problem remains: TrueType’s
δ instructions are inserted into a program; thus they appear at a given moment and
operate on the position of the points at that very moment. Here the time at which the
δ instructions are instantiated is less clear: all that we know is that alignments come ﬁrst,
then interpolations, and ﬁnally links, in the order in which they were created by the user.
If we add a visual δ hint, when will it be executed?
Not to worry. FontLab has taken a wise decision by deﬁning two types of visual δ hints:
medial δs and ﬁnal δs. Medial δs are executed along with the links, while ﬁnal δs are ex-
ecuted at the end of the optimization process, after global interpolation. Thus medial δs
are modiﬁcations to the optimized outline that take part in the work done by the links,
whereas ﬁnal δs are last-minute solutions employed to eliminate an annoying pixel or
creating a pixel where its absence is most cruelly felt.
Certainly the reader is beginning to wonder: is it not dangerous to play with pixels? Af-
ter all, at every size the conﬁguration of the pixels is so diﬀerent that we cannot sensibly
talk about pixels without also specifying the size. Quite so: δs depend on the size. They can
be deﬁned for a speciﬁc size or for a range of sizes. For example, we can take action only
where there is truly a problem and correct it without aﬀecting anything at other sizes.
To apply a δ to a point of the outline, we ﬁrst click on the button
(for a medial δ:
it represents a capital delta indexed by a letter ‘M’) or on the button
(for a ﬁnal δ:
it represents ΔF). Then we click on the point in question and drag in the direction of
the movement. The δs are the only visual hints for which there is no diﬀerence between
horizontal and vertical mode, as FontLab will systematically create two δs: a horizontal
one and a vertical one, corresponding to the projections of the movement obtained by
dragging the mouse. Warning: movement is done in eighths of a pixel and cannot exceed
one pixel. We can edit the values of a δ and the sizes at which it is applied in the lower
part of the TrueType Program window, separately for the horizontal and vertical parts.
Here is an example of applying a ﬁnal δ in order to move a pixel (encircled on the left
side of the image) that had the nerve to put itself in the wrong place:

<!-- Page 549 (Book page 529) -->
δ
As can be seen on the right side of the image, inserting a ﬁnal δ half a pixel to the left
and half a pixel upwards was enough to correct4 the wayward pixel.
Generating or importing bitmaps
There are branches of computer science in which fonts are very seldom changed. For
instance, since 1987, when the author bought his ﬁrst Macintosh, he has used only one
font, and at only one size, to prepare his documents: 9-point Monaco. If this font had been
a TrueType vector font, then for all these years, every time the font was displayed on the
screen, the rasterizing engine would have had to execute the same instructions only to
obtain the same rasterization over and over again. That is a waste of memory and of CPU
cycles.
We are far removed from the graphical applications in which thousands of fonts are used
at virtually all possible and imaginable sizes, for which real-time rasterization is crucial.
The reason that we are driven to rasterize our fonts in real time is that we cannot store
4 The astute reader will surely have noticed that there is a paradox here. By applying a δ to the upper
curve, we naturally blackened a new pixel, since its center appeared inside the outline. But since we have not
modiﬁed the lower curve, why did the “wayward” pixel disappear? If its center lay inside the outline before, it
still does!
By way of answering this question, let us take a closer look at the situation before and after the δ:
We see that the pixel is black although it should not be, since its center lies slightly outside the outline. The
explanation is as follows: we slightly underestimated the rasterizing engine by saying that it uses pixels alone
to decide whether to blacken a given pixel. Here the engine noticed that there would be a white pixel here if
only the centers of the pixels were used, whereas the outline itself does not have a discontinuity at this point.
Probably by applying criteria such as the continuity of the surface or the distance between the curve and the
center of the pixel, the rasterizing engine, in its inﬁnite wisdom, decided to break the rules and give us a black
pixel at that location.
When we took action by adding a pixel through the use of the δ, the exception no longer existed, and the
“hidden” pixel disappeared.

<!-- Page 550 (Book page 530) -->
all the rasterizations on the disk. But if there is a small number of sizes that we use very
frequently, the storage of a bitmap rasterization becomes an attractive option.
It is for these reasons that TrueType fonts can indeed contain bitmap fonts (the EBLC
and EBDT tables; see §D.7). FontLab allows for the generation of such bitmaps, which are
identical to the rasterization displayed in “visual hints” mode.
To generate a bitmap for the current glyph and at the current size, we switch to “bitmap”
mode by clicking on the button
of the TrueType Tools bar. Next, we select the option
Generate bitmap in the window’s pop-up menu. Once generated, the bitmap can be
modiﬁed by simply clicking on its pixels.
Through this same pop-up menu, we can import a bitmap from another font. Finally,
we can also ask FontLab to show us the diﬀerences between the imported (or generated)
bitmap and the bitmap produced by rasterizing the glyph. For that purpose, we enable
the option Highlight differences on the pop-up menu and leave “bitmap” mode: the
pixels whose values diﬀer in the two versions are displayed on a red background. FontLab
even recommends the following common strategy: take a good bitmap, display it as a
background task, and create visual hints until the two bitmaps coincide. A funny way
to work!
Behind the scenes
The reader who has read Appendix E and mastered the concepts and syntax of TrueType instruc-
tions may be curious to know how FontLab’s “visual hints” are turned into genuine instructions.
It is surprising to observe how easily this conversion is made:
• An “alignment” is nothing but MDAP (move direct absolute point) instruction, i.e., a rounding
according to the active rounding method.
• A “single link” is an MDAP of the ﬁrst point followed by an MIRP, i.e., an indirect relative move;
since the ﬁrst point has become a point of reference because of the previous instruction, we
simply take a value from the CVT and apply to the second point a movement equal (in pixels)
to the CVT.
• “Double links” are more complex: FontLab uses a function (deﬁned in the fpgm table) that
will put things in place for this rather special visual hint. The last lines of the function take
the MDAP and the MIRP from the single link.
• “Interpolation” is nothing but an IP interpolation instruction.
• Similarly, a “δ” is merely a DELTAP1. The restriction on the size of a “δ” comes from the fact
that we can change neither delta_base nor delta_shift.
Thus we see that “visual hints” are simply a small subset of TrueType instructions. But thanks to
FontLab’s enjoyable interface, this subset enables us to perform very eﬀective optimizations.
Managing Instructions under VTT
The history of VTT goes back to the earliest days of TrueType. The author of TrueType,
Sampo Kaasila, also wrote a tool for instructing fonts. This tool, called Typeman, it seems,
was sold at exorbitant prices on the order of thousands of dollars (!). Later the product

<!-- Page 551 (Book page 531) -->
was called TTED (= TrueType Editor), and for the past several years it has gone by the name
of VTT (= Visual TrueType).
VTT is distributed free of charge by Microsoft. But be warned! “Free of charge” does not
mean “freely”. To obtain a copy of VTT, one must print out a copy of the license [261]
and fax it to Microsoft. Usually within a few days one will be given access to the VTT dis-
cussion forum, from which the software can be downloaded (for Mac OS 9 or Windows).
Nevertheless, the documentation and all the ancillary resources are available freely on
Microsoft’s site [262].
How does VTT compare to FontLab? Both oﬀer graphical interfaces for instructing True-
Type glyphs. VTT’s interface is less pleasant to use, less aesthetically appealing, and less
ergonomic than that of FontLab, but VTT is closer to the real TrueType instructions and,
therefore, gives access to features that are inconceivable under FontLab. Yet VTT has this
in common with FontLab: the user is not required to learn the assembly language for
instructions, as everything is done in a graphical manner. VTT oﬀers a graphical adapta-
tion of instructions that is more powerful than that of FontLab, and therefore necessarily
more complex.
How do the approaches of VTT and FontLab diﬀer? First of all, VTT oﬀers a completely
diﬀerent vision of the management of relevant dimensions (relevant heights, stroke
widths, etc.).
Control values
We have seen that FontLab allows us to store relevant dimensions in a table, give them
names, and indicate when their rasterization changes from 1 to 2 pixels, from 2 to 3, and
so on. When a TrueType font is generated, this table internal to FontLab feeds the table
CVT (“control values table”), which is contained in every TrueType font.
VTT, for its part, allows us to operate directly on the control values table. Indeed, unlike
the TrueType speciﬁcation, VTT attaches precise semantics to the entries in the CVT table, or
at least to its ﬁrst 120 values. For instance, we have shown in Figure 13-8 the meanings
of the entries 0 to 20, 22, and 24.
On the other hand, VTT classiﬁes glyphs into four groups: “uppercase”, “lowercase”, “ﬁg-
ure”, and “other”. (The group of a glyph can be redeﬁned, and new groups can be deﬁned
at any time.) The glyphs in Figure 13-8 belong to these four groups.
Finally, the CVT entries are classiﬁed according to their color, direction, and property. The
“color” depends on the color traversed by the link, which we shall deﬁne as follows:
• Black only: we say that the CVT entry in question is “black”, as, for example, the
horizontal width of the ‘I’.
• White only: we say that the entry is “white”, as, for example, the counter of the ‘n’.
• Or both black and white: the entry is “gray”, as, for example, the one that connects
the upper and lower strokes of the ‘8’, which thus traverses the two counters and the
juncture of the strokes.

<!-- Page 552 (Book page 532) -->
14
14+15
4+5
4
12
12+13
2+3
2
6+7
6+7
6+7
6
6
6
10+11
10+11
10+11
10
10
10
16
16+17
18
18+19
0
0+1
8+9
8
20
24
22
Figure 13-8: The meaning of CVT entries 0–19. These are diﬀerent relevant heights. For each
height n, entry n+1 contains the corresponding overshoot. The notation 2+3 indicates that the
height in question is the sum of entries 2 and 3. Finally, 20, 22, and 24 are the slopes of the
capitals, the lowercase letters, and the numerals.
68
69
Str.
70
71
Round
72
73
Str.
74
75
Round
80
SH
76
77
Str.
78
79
SW
81
82
Str.
83
84
Round
94
(66)
Dist.
85
86
Str.
87
88
Round
93
SH
95
Dist.
89
90
Str.
91
92
SW
96
Dist.
97
98
Str.
99
100
Round
101
102
Str.
103
104
Round
109
SH
105
106
Str.
107
108
SW
110
111
Str.
112
113
Round
114
115
Str.
116
117
Round
118
119
Str.
Horiz.
Vertical
Diag.
Horiz.
Horiz.
Horiz.
Vertical
Diag.
Horiz.
Horiz. Horiz.
Vertical
Vertical
Vertical
Diag.
Diag.
Black
Black
Black
Black
White
White
White
Uppercase
Lowercase
Figures
Other
(67)
(67)
(67)
(67)
(66)
(66)
(66)
Figure 13-9: The meaning of CVT entries 68–119. The abbreviations “SH” and “SW” mean
“serif height” and “serif width”. The broken arrows indicate inheritance.

::: tip Figure 13-8: The meaning of CVT entries 0–19. These are different relevant heights
![Figure 13-8: The meaning of CVT entries 0–19](/images/fonts-encodings/fig13-8.png)
*Figure 13-8: The meaning of CVT entries 0–19. These are different relevant heights.*
:::

::: tip Figure 13-9: The meaning of CVT entries 68–119. The abbreviations 'SH' and 'SW' mean 'serif height' and 'serif width'
![Figure 13-9: The meaning of CVT entries 68–119](/images/fonts-encodings/fig13-9.png)
*Figure 13-9: The meaning of CVT entries 68–119. The abbreviations 'SH' and 'SW' mean 'serif height' and 'serif width'.*
:::


<!-- Page 553 (Book page 533) -->
The “direction” may be horizontal, vertical, or diagonal. Finally, the “property” is also
a predeﬁned string, selected from “thickness of a straight stroke” (StraightStroke),
“thickness of a curve” (RoundStroke), “serif height” (SerifHeight), “serif breadth”
(SerifExtension), “another distance” (Distance). Figure 13-9 shows the classiﬁcation of
CVT entries 68 to 119 according to these four criteria: group, color, direction, property.
In Figure 13-9, we have also shown—with a broken arrow—another important property
of CVT entries under VTT: inheritance. We say that a “daughter” entry inherits from a
“mother” entry if they are rendered with the same number of pixels, up to a certain
size—the size at which the daughter breaks free of the mother and can be rendered by
a diﬀerent number of pixels. The sire of all the entries of a relevant dimension is en-
try 65 (which is both horizontal and vertical). Entries 66 (horizontal) and 67 (vertical)
inherit from it and are therefore, in a sense, the most relevant dimensions of the font. We
see in Figure 13-9 that entries 68, 81, 97, and 110 inherit from 66 and that entries 72,
85, 101, and 114 inherit from 67: that ensures a certain uniformity in the font, one that
will no longer be maintained beyond a certain size, when there will be enough pixels
for the diﬀerence of stroke thicknesses in these groups of glyphs to be felt. Finally, within
each group (uppercase, lowercase, etc.), the thicknesses of round strokes inherit the thick-
nesses of straight strokes.
Note that this classiﬁcation of strokes recapitulates, in a sense, the principle of the pa-
rameters of METAFONT (see Appendix F), if only with regard to rasterization. Of course,
METAFONT goes much further by parameterizing the relevant dimensions themselves,
not only their bitmap rasterization. But let us not forget that METAFONT works quietly
up the line, whereas the TrueType rasterizing engine must fulﬁll the user’s requests in
real time.
Let us return to the classiﬁcation of the CVT entries. Their interest lies not only in the
fact that they force us to organize the rasterization of the font. It lies mostly in the fact
that VTT, like FontLab, will automatically select the CVT entry to which a link will be
connected. But unlike FontLab, where relevant dimensions are classiﬁed only by their
names and their directions, VTT is aware of the group to which the current glyph belongs
and also knows the link’s color: “black”, “white”, or “gray”; thus it will automatically
choose a CVT entry with the correct group, direction, and color. Thus there are much
better chances that the automatically selected entry will be the correct one in VTT than
in FontLab.
Opening/saving a ﬁle
VTT knows how to open TrueType ﬁles under Windows and Mac OS 9 (or Mac OS X, in
the Classic environment).
But there is a small problem under Mac OS 9: the font must not be contained in a Macintosh “suit-
case”. Thus, under Mac OS 9, one must double-click on the font suitcase to open it and then extract
the TrueType font (warning: this operation is not possible under Mac OS X, which fact seriously
compromises the functionality of VTT under that system). Next, so that the ﬁle in question will
be recognized by VTT, it must be of Macintosh ﬁle type sfnt. To that end, a utility for converting
ﬁle types (such as File Buddy) is necessary. After that manipulation is complete, everything works
correctly, and VTT will open the font with no problems.

<!-- Page 554 (Book page 534) -->
Let us now skip the steps and suppose that we have ﬁnished optimizing a TrueType font.
Before distributing it, we must strip out all “private” data, i.e., those that have been
added through VTT. Speciﬁcally, VTT adds a number of tables to the font’s TrueType
structure, and if the font is not free, it might not be prudent to distribute these tables—
which, after all, contain the entire strategy for instructing the font—to the end user. But
beware! Unlike FontLab or FontForge, each of which has its own ﬁle format, VTT uses
the TrueType format as both a “working” ﬁle format and a format for the generated
fonts. Fonts are generated through the menu option Tools>Ship Font, and it is therefore
necessary to take care to select a diﬀerent font name, or a diﬀerent target location, or
else the original font will be overwritten by the ﬁle generated and the internal data will
therefore be irretrievably lost.
The glyph window
Figure 13-10: The glyph window of VTT.
VTT’s interface consists of a glyph window, a font-table window (where we can choose the
glyph to manipulate), and a number of text windows, the most important of which are
the control-program window, which represents an uncompiled version of the CVT table,

::: tip Figure 13-10: The glyph window of VTT
![Figure 13-10: The glyph window of Visual TrueType (VTT)](/images/fonts-encodings/fig13-10.png)
*Figure 13-10: The glyph window of VTT.*
:::


<!-- Page 555 (Book page 535) -->
and the glyph-program window, which displays, in real time, the TrueType instructions
generated from the VTT visual hints.
Unfortunately, the glyph window does not display both the original outline and the cus-
tomized outline at the same time, as FontLab does. We have to switch from one to the
other by enabling or disabling the option Display>General Options>Grid fit (shortcut:
ctrl-G).
In Figure 13-10, we see the glyph window in “customized outline” mode. Here we have
chosen to view the pixels in gray-level mode; in fact, we have the choice of several ras-
terizing engines, including diﬀerent versions of ClearType’s technology. At the top are
a number of buttons, which we can slide back and forth through the use of the small
triangles. At the bottom, we can preview the glyph at its actual size; by clicking on one
of the sizes at the bottom, we change the grid of the glyph displayed in the middle of the
window.
The window of the control program
We obtain this window by selecting View>Control program. It represents, at the begin-
ning, the contents of the ﬁle CvtTmpl.txt: the value of the primary CVT entries and a
large number of comments. Its syntax is as follows:
66: 200
means that we are assigning the value 200 to entry 66. This value represents 200 abstract
TrueType units. The rasterizing engine will obtain the number of pixels corresponding
to this dimension by using the resolution and the number of units per em.
Inheritance is expressed in the following manner:
68: 200 = 66 @27
which means: entry 68 (the “daughter”) takes the value 200 and must be rendered with
the same number of pixels as entry 66 (the “mother”), up to 27 points. Beyond that size,
the number of pixels will be calculated by a simple rule of three from the abstract value
of the dimension (here, 200).
By writing:
70: 10 ~ 68 @100
we specify that entry 70, whose abstract value is equal to that of entry 68 plus 10 units,
will be rendered with the same number of pixels as 68 up to size 100. Beyond that size,
the entry breaks free of entry 68 and is rendered as usual by converting its value into
pixels.
Finally, we can have δ instructions applied to certain CVT entries. By writing:
3: 30 ~ 2 @18 Delta (1 @18, - @32-)

<!-- Page 556 (Book page 536) -->
we ask the rasterizing engine to add a pixel at 18 points and to remove one at sizes be-
tween 32 and 100. For those who have read Appendix E, let us note that these are DELTAC
instructions that appear in the prep table. These are global instructions that must not be
confused with DELTAP instructions, which aﬀect only one glyph.
We have already mentioned that other CVT entries are classiﬁed by group, color, direc-
tion, and property. We can write:
UpperCase
Black
X
StraightStroke
68: 200 = 66 @27
to indicate the classiﬁcation of the entry (indentation is optional). In this notation, the
groups (Uppercase, Lowercase, Figure, Other), the colors (Black, White, Grey5), the di-
rections (X, Y, Diag), and the properties of strings (StraightStroke, RoundStroke, Ser-
ifHeight, SerifExt, etc.) are predeﬁned.
We can deﬁne new groups by writing, for example:
GROUP Kanji
Then we must declare the glyphs in the ﬁle CharGrp.txt and associate the appropriate
glyphs with the new group.
To enter the correct values of CVT entries in the control-program window, we must
measure a number of heights, widths, and stroke thicknesses. VTT oﬀers us a tool for
this purpose that can be invoked by clicking on the Measure button. Before taking mea-
surements, we are required to hide the pixels and switch to “original outline” mode by
disabling Display>General Options>Grid fit and Display>General Options>Pixels. To
choose the correct glyphs and the correct dimensions to measure, we can draw inspira-
tion from Figures 13-8 and 13-9.
Warning: After every modiﬁcation to the control-program window, it is necessary to re-
compile the CVT through the use of Tools>Compile>Control values.
Modifying a glyph’s trace
VTT’s operations depend a great deal on the correct positioning of the outline’s nodes. It is quite
probable that we will notice, while in VTT, that a node is poorly placed or that it is superﬂuous,
or that one is missing at a certain location. VTT gives us the tools to correct the problem:
• Move will move a node.
• Swap will transform a point oﬀthe curve (i.e., a control point) into a point on the curve (i.e.,
into a starting/ending point of the Bézier curve), and vice versa.
5 The word “grey” is spelled in the British manner, not the American one (“gray”).

<!-- Page 557 (Book page 537) -->
• Delete will delete a node without breaking the outline.
• Insert will insert a node at a given point on the outline.
To be able to use these tools, we must be in “original outline” mode (disable Display>General
Options>Grid fit). On the other hand, the Swap operation makes sense only if the points oﬀthe
curve are visible: that can be achieved by disabling Display>General Options>Show fewer points.
Those used to the trace mode for Bézier curves in FontLab or FontForge will need to break their
habits. When Insert is selected, VTT will insert a point oﬀthe curve if Show fewer points is
disabled or a point or the curve otherwise. Whether the point lies on or oﬀthe curve determines
the curve’s behavior: we need only consider that the fact that a Bézier curve between two points
on the curve and with no points oﬀthe curve is necessarily straight. The points oﬀthe curve are
responsible for its curvature.
To make an inserted point the starting point of a new trace, it is necessary to right-click (under Win-
dows; °-click on the Macintosh). But since VTT is not glyph-design software, it is recommended
to switch to other, more appropriate, software (FontForge or FontLab) for this purpose.
Anchors
An anchor is a rounded control point that is not the target of a link or an interpolation.
An anchor may be horizontal, vertical, or both at once. To obtain an anchor, we select
XLink (for a horizontal anchor) or YLink (for a vertical anchor) and right-click (under
Windows; °-click on the Macintosh) on the control point that we want to convert into
an anchor. Then one of the two windows below appears, depending on whether we are
in horizontal or vertical mode:
We slide the mouse onto one of the boxes. These boxes represent the 18 (!) ways of
rounding a control point. Here is how to interpret the symbols. The three rows of boxes
correspond to:
1. The usual situation of an upright glyph.
2. The situation of an italic glyph whose slant has been speciﬁed with the Angle tool.
In order for this rounding to be useful, the stroke in question must have this slant
(in which case we use YLink) or be perpendicular to the slant (XLink).
3. Like the previous case, but the slant is not an abstract slant but rather a slant calcu-
lated from pixels (whose angle is thus slightly diﬀerent and depends on the resolu-
tion).
On every line there are six boxes, containing six symbols:
1. The ﬁrst corresponds to the absence of rounding.

<!-- Page 558 (Book page 538) -->
2. The second is classical rounding (the left/bottom or right/top edge of the pixel, ac-
cording to the position of the point with respect to the center of the pixel).
3. The third is the rounding of the center of the pixel in which the point is found.
4. The fourth is rounding according to a subgrid of half-pixels. In other words, the point
will be placed on the edge of a pixel or over the center of a pixel, whichever is closer.
5. The ﬁfth is rounding down (towards the left or the bottom).
6. Finally, the last is rounding up (towards the right or the top).
Thus we have the same rounding methods as in FontLab, except that special attention is
paid to slanted strokes, according to the angle of their slope.
Vertical anchors (produced by Ylink) may be connected to a
relevant height. To this end, one enables the option Display>
Visual TrueType Options>Anchors. All the vertical anchors
are then represented by an icon shaped like the U.S. interstate
highway shield:
.
In addition, when the option Display>Visual TrueType Op-
tions>Cvt numbers is enabled, these highway shields are dis-
played larger and contain numbers (see opposite). These num-
bers are the CVT entries connected to the anchors. Ordinarily,
according to the available data, VTT has already selected the
appropriate CVT entry for each vertical anchor. To change it, one merely right-clicks
(under Windows; °-click on the Macintosh) on the highway shield and selects the new
CVT entry on the pull-down menu that appears.
After verifying or modifying the CVT entries of the anchors, one must once again disable
the display of the highway shields, which are a bit too cumbersome.
Links, distances, shifts
VTT’s links work like those of FontLab: we select either XLink (for horizontal links) or
YLink (for vertical links), click on the link’s starting point (its “parent”), and drag it to its
ending point (its “child”). The starting point is then automatically transformed into an
anchor. So far there has been nothing unusual with regard to FontLab.
The ﬁrst novelty: the CVT entries to which the links are connected are selected not only
according to the width of the link but also according to the group of the glyph, the color
of the link (“black”, “white”, or “gray”), and the link’s direction.
On the other hand, links can be of various types, according to the nature of the stroke and
our choices of minimum distances. After drawing a link, we right-click (under Windows;
°-click on the Macintosh) on the head of the arrow, and one of the two pull-down menus
shown below appears:

<!-- Page 559 (Book page 539) -->
depending on whether the link is horizontal or vertical. Then we slide the mouse to a
box to indicate the type of the link.
The four columns of these pop-up menus have the following meanings:
1. The link is not connected to any CVT entry. We say that the link represents a distance.
2. The link is connected to a CVT entry that is neither “straight” (the StraightStroke
property) nor “round” (the RoundStroke property). We will use it, for example, for
the breadths of serifs and other dimensions that cannot be classiﬁed into these two
cases.
3. The link is connected to a “straight” CVT entry (the StraightStroke property); thus
it represents the thickness of a straight stroke or the breadth of a straight counter.
4. The link is connected to a “round” CVT entry (the RoundStroke property); thus it
represents the thickness of a curvilinear stroke or the breadth of a round cavity.
As for the rows of boxes:
1. The icons in the ﬁrst row represent links without a minimum distance. The thickness
in question can therefore be rendered with 0 pixels.
2. Those in the second row (with the symbol of an “opening elevator door”
) repre-
sent links with a minimum distance. The minimum distance may be from 0 to 8 (!!)
pixels, in units of one-eighth of a pixel. By default, its value is 1 pixel. To change
the minimum distance for a given link, we ﬁrst enable the option Display>Visual
TrueType Options>Minimum distance, which has the eﬀect of displaying an icon of
an “opening elevator door” over the link. Right-clicking (under Windows; °-click on
the Macintosh) on this icon displays a ruler bar. By sliding from right to left—feel
free to slide oﬀthe end of the ruler, only a small part of which is visible—we can
indicate, with a precision of an eighth of a pixel, the exact value of the minimum
distance, between 0 and 8 pixels.
3. Those in the third row (with the symbol of a “closing elevator door”
) are there
for legacy reasons: Typeman, the predecessor of VTT, took the initiative to force min-
imum distances into existence, even where they were not desired. By selecting a link
of this type, we can abandon Typeman’s choice and obtain all the same a link with
no minimum distance.
Opposite, by way of example, is shown a letter ‘m’ in which the side bearings, the stems,
and the outlines have been connected.

<!-- Page 560 (Book page 540) -->
We have used “distances” (i.e., links not connected to CVT entries) for the side bearings,
since they do not have a uniform (abstract) breadth anywhere in the font. On the other
hand, we have requested a minimum distance of 1 pixel for the side bearings. For the
stems we have used “straight” links, and VTT has automatically decided to connect them
to CVT entry 81, which, according to Figure 13-9, is indeed the entry “lowercase, black,
horizontal, straight”. To connect the internal outlines, we have been forced to add a new
entry to the control-program window, like this:
Lowercase
White
X
StraightStroke
120: 430
Thus we have used entry 120, which is “lowercase, white, horizontal, straight”. It was
automatically selected by VTT.
A shift is another type of link. The idea is to connect two points (the “parent” and the
“child”) so that the “child” will follow all of the “parent’s” moves caused by instructions.
A shift does not use a CVT entry; it has no rounding a priori, nor any minimum distance.
We insert a shift by choosing the tool X Shift (or Y Shift for a vertical shift) and proceed-
ing as for a link.
Interpolations and alignments
Interpolations work as in FontLab. We select points that will be the reference points for
the interpolation. Then we select one or more points that will be interpolated relative
to the ﬁrst two. There are no constraints: since we are doing interpolation rather than
extrapolation, the projections (horizontal or vertical) of the points to be interpolated
must lie between those of the reference points.
To perform interpolation, we select the tool X Inter (or Y Inter for vertical interpolation).
We click on the ﬁrst reference point and drag the mouse to the second. A black line is
thus drawn between the two points. Next, we click on this line and slide to the point to be
interpolated. If there are points to interpolate, we repeat the procedure as many times
as necessary. VTT will represent the interpolation by a series of white arrows chained
together that will run through all the points, the ﬁrst one starting from the ﬁrst reference
point, the last one ending on the last reference point.
Alignments (not to be confused twith FontLab’s “alignments”, which are roundings of
an individual point relative to the grid) are a stronger form of interpolations in which
we request that points be mutually aligned with one another at all costs. That is really
of interest only for points that fall on the same slanted straight line, since for points
aligned horizontally or vertically an alignment can be obtained much more easily by
rounding them.

<!-- Page 561 (Book page 541) -->
A typical example of alignment is the slanted and discontinuous stroke of the ‘A’ (see
opposite), for which the rasterizing engine has no way, in the absence of an instruction,
to guess that the pieces above and below the cross stroke absolutely must be aligned.
We insert an alignment by selecting the Align tool and joining (by drag-
ging the mouse) the two extreme points of the points to be aligned. VTT
will produce as many blue arrows as there are points between these ex-
tremes. By playing with the heads of these arrows, we can exclude some
or add others. The extreme points automatically become anchors.
Strokes
Strokes are a very interesting feature of VTT. The question that arises is: if links, distances,
and shifts allow for the management of the thicknesses of horizontal and vertical strokes,
what is done for slanted ones? That is where the “stroke” tool comes to the rescue. It
allows us to cover the surface with a slanted stroke and to associate with it a thickness
that is merely an entry in the CVT table. This entry must be stored in the table under the
“black” and “diagonal” attributes. The rasterizing engine will then optimize the slanted
stroke.
Here is how we insert a stroke. First, we select the Stroke tool on the button bar. Next,
we select four points that cover a large part of the slanted stroke to be optimized; for
example, in the ﬁgure below, points 2, 5, 4, and 3 constitute two pairs, (2, 5) and (3, 4).
We click on one of the four (for example, 2) and drag to the matching point (here, 5);
then we click on the point that is on the same side as the ﬁrst, at the other end of the
stroke (here, 3), and drag to the remaining point.
As we drag the mouse the second time, the area of the stroke turns black. When we have
ﬁnished, the area is shown hatched on a yellow background, with a “highway shield” in
the middle that indicates the number of the CVT entry selected by VTT:
We can change the CVT entry as usual by making a contextual click on the highway-
shield icon and selecting the appropriate entry.
The starting points for the two links (here, 2 and 3) are automatically made into anchors.
δ instructions
These δs are shifts of the nodes to the customized outline. They are our last hope for
correcting minor imperfections that the other instructions have left behind. They must

<!-- Page 562 (Book page 542) -->
be used in moderation: they do allow us to add a pixel here or delete one there, but we
must be careful not to overuse them, since they increase the bulk of the font. One or
more rasterized sizes can be aﬀected by a δ.
We can classify δs according to their direction (horizontal or vertical), their amplitude
(between 1
64 and 8 pixels), the sizes of rasterization to which they apply, or the moment
of their execution in the assembly code for TrueType instructions: “inline” (inline), “just
before global interpolation” (pre-IUP), or “after global interpolation” (post-IUP).
To insert δs, we must enable the option Display>General Options>Grid fit and possibly
also the option Pixels.
The tools XMove and YMove are used for horizontal and vertical δs that apply to all sizes
of glyphs; the tools XDelta and YDelta are used for those that apply only to the active
size. The sizes are independent with respect to δs; thus we can apply several diﬀerent δs
to the same point, each corresponding to a diﬀerent size.
Once we have selected the tool, we click on the point to which we wish to apply a δ. A
ruler then appears:
We can select the amplitude of the δ, between −8 and 8 pixels, in subdivisions of one
eighth of a pixel (feel free to slide outside the little window: only a small part of the
ruler is visible). When the Ctrl key is pressed while the ruler is visible, the subdivisions
become larger; conversely, when Alt is pressed, the subdivisions become smaller, down
to 1
64 of a pixel.
By holding down the Shift key while the ruler is visible, we change the moment at which
the δ is executed, which is indicated by the keywords inline, preIUP, and postIUP in
the upper right part of the window containing the ruler. Nevertheless, be forewarned:
“inline” δs and “pre-IUP” δs can be applied only to “touched” points, i.e., to points that
have been rounded by an anchor or a link.
Finally, when we right-click (under Windows; °-click on the Macintosh) on the point
to which we are applying the δ, the ruler’s window displays a third piece of information,
the keywords b/w only and grey only:
If “gray scale” mode has been selected (Tools>General Options>Gray scale), a right-
click/°-click will limit the δ’s scope to gray-scale rasterizations. Conversely, if “black-and-
white” mode is selected, the δ will apply only to rasterizations of that type. This feature
allows us to restrict δ instructions to a certain kind of rasterization.

<!-- Page 563 (Book page 543) -->
A few examples
We shall examine three typical examples (the letters ‘O’, ‘H’, and ‘A’) drawn from the font
Trebuchet in a VTT tutorial [260].
The letter ‘O’ from this font is shown opposite. In the im-
age, we have enabled the option Show fewer points; thus
we see only the points on the curve (the others do not
have an eﬀect on visual hints).
We shall ﬁrst place an anchor at point 3—an anchor
connected to the CVT entry for the upper overshoot of
a capital letter, which is entry 3. Likewise, we shall place
an anchor at point 9 that will be linked to CVT entry 9
(the lower overshoot of a capital letter). We thus ensure
the alignment of our glyph relative to the other glyphs in
the font.
Next, we shall place two horizontal links: one from 0 to 12 and one from 6 to 18. VTT
will automatically associate these links with entry 70 (“capitals, black, horizontal, round
stroke”). Likewise, we shall place vertical links from 3 to 20 and from 9 to 15; VTT will
automatically select CVT entry 74 (“capitals, black, vertical, round stroke”). We shall
always use “round” links with a minimum distance of one pixel. The minimum distance
ensures that we shall always have a visible stroke, even if the thinness and arrangement
would ordinarily cause some pixels not to be black (which would leave holes in the out-
line of the ‘O’ when rendered with pixels). Thus we can be sure of obtaining good stroke
thicknesses.
Finally, we shall deal with the side bearings. We shall connect the origin (point 23) and
point 0 with a “distance”, i.e., a link not connected to a CVT entry. We shall do the same
on the other side: we connect the glyph’s set-width (point 24) and point 6 with a “dis-
tance”. But this time we specify a true minimum distance, of one pixel. Thus the glyph
may have a zero approach on the left, but it will always have an approach of at least one
pixel on the right.
Here, then, is the result of our instructions, as shown in VTT:

<!-- Page 564 (Book page 544) -->
Note that all the links go from the outside inward. That allows us to direct any changes
to the outline towards the inside of the glyph, where they will be less damaging to the
glyph’s overall appearance.
Let us continue with this font’s letter ‘H’.
We shall start by placing anchors in order to ensure align-
ment with the other glyphs: points 6 and 9 will be con-
nected by CVT entry 2 (the height of a capital letter), and
points 3 and 0 will be connected by entry 8 (the baseline
of a capital).
Next, we shall concern ourselves with the thicknesses of
the strokes: we shall connect points 5 and 7, then 10 and 8,
with horizontal links. VTT will automatically select CVT
entry 68 (“capitals, black, horizontal, straight stroke”). We
shall request a minimum distance of one pixel so that the
stroke will not disappear under any circumstances.
Here there is a trap. For us humans, it is obvious that point 2, for example, must have
the same abscissa as point 7. But from looking at the outline, it is not at all obvious to
the rasterizing engine that that must be so. Therefore, to prevent stroke thicknesses that
diﬀer for the upper and lower parts of the glyph, we shall also set links from 5 to 3 and
from 10 to 0, with the same width and type as the previous links.
After that, we shall ensure the correct thickness of the cross stroke. To that end, we shall
create a vertical link between 2 and 8. This link is automatically connected to CVT en-
try 72 (“capitals, black, vertical, straight stroke”), and we request a minimum distance of
one pixel, so that the cross stroke will always be visible.
But what about the position of the cross stroke? Rather than deﬁning a special CVT entry
for the height of the cross stroke of the ‘H’, we can make use of an interpolation: after all,
the position of this cross stroke is not of critical importance. Let us take points 0 and 6 as
the extreme points for our interpolation. But which point shall we interpolate: the one
on the top of the cross stroke, or the one on the bottom?
To answer that question, let us consider another: if the height of the glyph is an even
number of pixels, we shall have to decide to place the cross stroke either above or below
the imaginary line that runs between the two pixels in the middle. What would be the
more appropriate choice? From the aesthetic point of view, we would prefer for the cross
stroke of the ‘H’ to err on the high side. Moreover, we can see right away in the original
outline that the cross stroke appears slightly higher than the middle of the glyph. Thus
we must interpolate, and round, a point below the cross stroke (for example, point 2).
Then the pixels resulting from any possible rounding error will be propagated towards
the top of the glyph.
Finally, to include the instruction of the glyph, we resolve the problem of the side bear-
ings by adding “distances”, just as with the letter ‘O’. Here is VTT’s representation of our
instructions:

<!-- Page 565 (Book page 545) -->
We shall conclude this series of examples with the letter ‘A’.
Note that, in the image opposite, the lower left point of the
letter (point 4) is mistaken for the origin (11) and that the
lower right point (7) is mistaken for the set-width (12).
We shall begin by placing anchors at the relevant heights: at
points 5 and 6 (CVT entry 3: “height of a capital letter with
overshoot”) and at points 4, 3, 0, and 7 (CVT entry 8: “base-
line of a capital letter, without overhang”).
We shall also set an anchor at point 8. It will not be linked to
a CVT entry, but it will use a very special rounding method—
rounding towards the center of the pixel—to ensure that the point will be rendered by
one and only one pixel.
How shall we handle this letter horizontally? If the extreme points are close enough to
the edges of its abstract box, then the side bearings are completely insigniﬁcant, and we
shall not worry about them (as we did with the ‘O’ and the ‘H’). On the other hand, we
know that we have the stroke tool to handle the thickness and rasterization of slanted
strokes. What we need is a mechanism to ensure that the letter will not lean to one side—
in other words, a mechanism to preserve the letter’s vertical symmetry.
We shall bring out the big guns in order to obtain this symmetry. For example, we shall
deﬁne a new CVT entry, representing half the distance between 3 and 0, i.e., half of the
letter’s internal width. That entry will be classiﬁed as “capitals, gray, horizontal, distance”.
Next, we shall create horizontal links between points 8 and 3, and then between 8 and 0.
VTT will associate them automatically with the new CVT entry. We shall request that
they be given a minimum distance of one pixel, so that the slanted strokes will not run
the risk of becoming vertical. The fact that the two links run from the outside inward
ensures that the letter can be drawn a bit wider so that its design will be correct.
To avoid any risks, we shall also deal with the letter’s external width by creating an in-
terpolation: point 8 will be interpolated horizontally relative to points 4 and 7. Nothing
remains but to use the stroke tool on the two slanted strokes; VTT will automatically
select CVT entry 77 (“capitals, black, diagonal, straight stroke”).

<!-- Page 566 (Book page 546) -->
One ﬁnal precautionary measure: will the two slanted strokes be aligned on both sides
of the cross stroke? To ensure their alignment, we shall use the alignment tool, twice:
between 8 and 3, and between 8 and 0.
Thus we have solved the problem of the slanted strokes. Here is what we have obtained
so far:
Now we have to solve the problem of the cross stroke. For its thickness, we need only
create a vertical link between 9 and 2. VTT will automatically select CVT entry 72 (just
as it did for the ‘H’). We shall specify for the link a minimum distance of one pixel so as to
avoid ending up with a ‘Λ’ instead of an ‘A’. Now that the cross stroke’s thickness has been
corrected, we must deal with its height. We shall proceed as with the letter ‘H’: that is, we
shall use an interpolation. Just one annoying detail: we would not want the cross stroke
to run too close to the apex, but still less would we want it to drift to the bottom; else
the ‘A’ might become a ‘Δ’. Thus we have to preserve the letter’s vertical integrity and
interpolate points 2 and 8 simultaneously towards the letter’s extremities, 3 and 5.
Finally, to ensure that the cross stroke will remain horizontal, we shall perform “align-
ments” (YShift) between the pairs of points (9, 10) and (2, 1).
Here are the new instructions that we have just added:
(Here we have represented only the instructions not shown in the previous ﬁgure.)

<!-- Page 567 (Book page 547) -->
Managing Instructions under FontForge
While FontLab and VTT oﬀer us interactive interfaces for creating instructions, Font-
Forge follows a diﬀerent approach, that of the integrated development environment
(IDE). For instance, it oﬀers us a debugger for TrueType instructions that allows us to
follow, step by step, the evolution of the original outline to the outline customized for
the grid. Other windows (see Figure 13-11) display the contents of the registers, the stor-
age area, and the stack, as well as the coordinates of the points of the glyph, in real time.
There is, however, a catch. As is described on the project’s web page FreeType [330], the library of
subroutines used by FontForge’s debugger is subject to certain patents held by Apple. To use it,
one must therefore request a license from Apple or be located in a country where the patents in
question are not valid. And since the FreeType project does not wish to subject honest people to
temptation, the code required by the debugger is not compiled in the default version of FreeType.
To be able to work with FontForge’s debugger, therefore, one must ﬁrst recompile FreeType after
having slightly modiﬁed the code. Here is how to do so:
1. Obtain the latest version of the sources for freetype from
http://sourceforge.net/project/showfiles.php?group_id=3157
2. Decompress them and open the ﬁle
include/freetype/config/ftoption.h
3. Replace
/* #define TT_CONFIG_OPTION_BYTECODE_INTERPRETER */
with
#define TT_CONFIG_OPTION_BYTECODE_INTERPRETER
i.e., uncomment the deﬁnition of the C preprocessor directive.
4. Compile FreeType and install it by following the instructions in docs/INSTALL.
Only after this maneuver will the debugger for TrueType instructions work in FontForge.
The debugger’s interface
Let us open a glyph for editing in FontForge. When we select Hints>Debug, a small
window asks us for the size of the rasterization that we wish to debug and the resolution
of the device. Once this window is closed, the glyph’s window splits into two. On the left:
the original outline of the glyph, shown in black on a grid of pixels (whose centers are
marked by small crosses), an approximation by straight strokes of the modiﬁed outline,
and the positions and numbers of all the nodes. On the right: a series of seven buttons
and, below it, a numbered list of all the instructions in the glyph.
The buttons have the following functions:
• The
button causes the following instruction to be executed. If it is a procedure
call, we will go into the procedure and execute its ﬁrst instruction.
• The second button,
, also proceeds step by step with the execution of the program
but does not go into procedure calls. This is the button that we shall use the most
often.

<!-- Page 568 (Book page 548) -->
Figure 13-11: The interface for debugging instructions in FontForge.
• The third button,
, takes us out of a procedure. If we are in the glyph’s code (not
in a procedure), clicking on this button will take us to the end of the code.
• The fourth button,
, is for “speed-reading”: it executes all the instructions up to
the end of the glyph’s code.
The execution of an instruction launched with the buttons
and
can also halt if the
debugger encounters a breakpoint or the shifting of a watchpoint.
We set a breakpoint,
, by simply clicking on a line. A second click disables the break-
point.
The principle of a watchpoint is diﬀerent, and especially interesting: we select a point
on the outline and click on the button
. The point is then “watched”. We can launch
the rapid execution of the instructions: as soon as an instruction modiﬁes this point,
execution will halt. In this way, we can ﬁnd the instructions that will modify a given
point and, by so doing, achieve a better understanding of the operation of instructions.
When we reach the end of the code, we need only click twice on a button that initiates
execution (such as
), and the code will be executed again from the beginning.
It is impossible to understand the operation of instructions without constantly moni-
toring the instruction stack, the graphics state, and possibly the storage area, registers
and CVT. That can all be done through the use of auxiliary windows obtained by means
of the button
. There is also a “glossary” window providing explanation on TrueType
instructions.

::: tip Figure 13-11: The interface for debugging instructions in FontForge
![Figure 13-11: The interface for debugging instructions in FontForge](/images/fonts-encodings/fig13-11.png)
*Figure 13-11: The interface for debugging instructions in FontForge.*
:::


<!-- Page 569 (Book page 549) -->
Figure 13-12: Seven auxiliary windows: Registers, Cvt, Storage, Points, Stack, Raster, and
Glossary.
It is also possible to edit instructions. We do so with another window, which is obtained
with Hints>Edit instructions.
Figure 13-13: The FontForge window for editing TrueType instructions.
This window—which, unlike the debugger, is not constrained by patents and is therefore
always available—displays a numbered list of instructions. By clicking on the Edit but-
ton, we can modify the instructions. Note that the modiﬁcations are not immediately
conveyed to the debugger: we must halt the execution of the code and start it again.

::: tip Figure 13-12: Seven auxiliary windows: Registers, Cvt, Storage, Points, Stack, Raster, and Glossary
![Figure 13-12: Seven auxiliary windows in FontForge](/images/fonts-encodings/fig13-12.png)
*Figure 13-12: Seven auxiliary windows: Registers, Cvt, Storage, Points, Stack, Raster, and Glossary.*
:::

::: tip Figure 13-13: The FontForge window for editing TrueType instructions
![Figure 13-13: The FontForge window for editing TrueType instructions](/images/fonts-encodings/fig13-13.png)
*Figure 13-13: The FontForge window for editing TrueType instructions.*
:::
