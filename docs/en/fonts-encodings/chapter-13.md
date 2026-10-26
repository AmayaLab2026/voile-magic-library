---
title: "Chapter 13: Optimizing a rasterization"
description: "Unabridged English text: Rasterization dilemmas, PostScript declarative hints (BlueValues, stem hints), TrueType virtual machine instructions and deltas."
---

# Chapter 13: Optimizing a rasterization
**By Yannis Haralambous, Ph.D.**
*From Fonts & Encodings, pp. 507–550*

---

The first two have problems with different thicknesses of strokes. In addition, the crossbar changes from 1 pixel to 2, and then, in the last two letters, back to 1 pixel again.
Conclusion: Even if the outline is perfect, the rasterization can ruin everything and cause
completely unpredictable behavior. We cannot just sit idly by and hope that some poorly
rendered glyphs will pass unnoticed. It is well known that as soon as something goes
wrong in typography, it will be noticed right away. Besides, it is, after all, unworthy of
our fonts: if we have spent hours creating impeccable outlines, we cannot accept poor
rasterizations. We have to take action—aggressive action!
Each of the three main font formats (PostScript Type 1, TrueType, METAFONT) offers a
different approach to this problem:
• In the case of METAFONT, rasterization—and everything else, for that matter—is
controlled through programming. The situation is quite unusual, as the bitmaps
are created by METAFONT before they are used. Provided that the characteristics of
a screen or a printer are known, METAFONT will generate bitmap fonts that are
adapted to it in advance. The rasterization will therefore be perfect, but the price
to pay for that perfect rasterization is total dependence on a certain kind of display
or printing hardware—the kind for which the bitmap fonts were generated. In the
day when METAFONT was developed, that constraint posed no problem at all: one
would prepare fonts specifically for one’s screen and printer. When one switched to
a new printer, one would figure out its characteristics somehow and generate new
fonts adapted appropriately.
But this balance fell apart with the advent of the Web: an “electronic document”
must be immediately and universally legible and printable. It cannot be restricted
to a particular type of output device. METAFONT is therefore incompatible with the
Web. We shall describe METAFONT’s approach in Appendix F.
• In the case of PostScript Type 1 or OpenType/CFF fonts, the rasterization is optimized
through the use of hints. Adobe’s strategy has been to refrain from stating exactly how
rasterization works and to give users nothing more than the possibility of vaguely
indicating some of the font’s characteristics, in the hope that the rendering engine
will see fit to use them. This approach is often decried by programmers but was actually welcomed by font designers, since, in a certain way, it relieved them of the
responsability to optimize the rasterization of their fonts. For them it is enough to
give a few indications to the black box that is the rendering engine in order to make

PostScript Hints
it “work”. And when “it doesn’t work”, Adobe will say that the designers are to blame
for not having supplied the correct hints, the designers will point a finger at Adobe,
and, if no other information surfaces, the matter will go no further. But none of that
is a serious problem, since PostScript fonts are used mainly in phototypesetting, and
hints are quite useless for that purpose because differences of one pixel in the thickness of a stroke are too small for the human eye to detect. We shall give a technical
description of hints in Appendix C.
• TrueType fonts use TrueType instructions, a programming language akin to assembly
language, to define the behavior of rasterization relative to the grid. There is no
“black box”; everything is disclosed, explained, exposed. For that reason, TrueType
instructions are much more complex than hints. Predictably, TrueType instructions
have been ill received by font designers, since their manipulation calls for a great
deal of effort and a way of organizing work that differs greatly from the designers’
own habits. With the exception of some fonts from big foundries such as Monotype, which were instructed by engineers specialized in instructing fonts, most of
the TrueType fonts that we find today are automatically instructed by font-design
software—which is a real pity, since much of the potential of instructions remains
unexploited. We have devoted all of Appendix E to the technical description of TrueType instructions.
Since the technical descriptions appear in the appendices, we shall focus here on the
practical question “How do we place hints, or how do we instruct a font?” And, more
precisely, how to do so with tools such as FontLab, FontForge, and Visual TrueType (or
VTT, a program for instructing TrueType fonts that is distributed free of charge by Microsoft).
PostScript Hints
In this section we shall examine hinting, which is the placement of hints in PostScript
Type 1 or CFF fonts. In Figure 13-1, the reader can compare the same text in various rasterizations, three of them optimized with hints in different ways and one not optimized
at all.
There are two types of PostScript hints: global hints, which affect the entire font, and
individual hints, which affect only a single glyph.
Global PostScript Hints
Of the global hints, two are very important: the alignment zones (i.e., the relevant heights
and the overshoots that go with them) and the relevant stroke thicknesses (see §C.3.4.1–
C.3.4.3). Some examples are shown in Figure 13-2. Thus it is necessary to “take inventory” of the alignment zones and the stroke thicknesses that seem relevant: for a Latin
font, these are more or less classic; for another font, these must be determined by taking
measurements and trying to observe similarities and analogies. We shall see how FontLab and FontForge can help us to identify the most relevant values.

::: tip Typographical Specimen Plate (Figure 13-1)
![Figure 13-1: Comparison of rasterization optimizations](/images/fonts-encodings/fig13-1-rasterization-hinting-comparison.png)
*Figure 13-1: Comparison of rasterization optimizations.*
:::

![Figure 13-1: Comparison of rasterization optimizations](/images/fonts-encodings/fig13-1-rasterization-hinting-comparison.png)
*Figure 13-1: Comparison of rasterization optimizations.*

    Figure 13-1: A comparison of various optimizations of the rasterization of a PostScript Type 1 font. The font is Monotype Old Style. Left: as rasterized by freetype with gray levels. Right: without gray levels.  The font’s original hints.  The font without hints.  The hints generated by FontForge.  The hints generated by FontLab. The text is from Goethe: “Ye wavering shapes, again ye do enfold me / As erst upon my troubled sight ye stole,” etc.

PostScript Hints
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
thicknesses: V1, the thickness of the vertical strokes and the curves (at the point where the tangents are vertical) of the capital letters; V2, the same, for the lowercase letters; H1, the thickness
of the horizontal strokes of the capitals; H2, the thickness of the ‘E’ and the ‘H’, but also of the
curves of the ‘o’; H3, the thickness of the curves of the ‘O’ where the tangents are horizontal;
H4, the thickness of the top part of the ‘z’. The font shown here is Computer Modern Sans Serif.
Let us get a bit more technical: alignment zones are pairs of values: a “relevant height” and
an “overshoot”. They are stored in a PostScript font parameter called BlueValues. When
these zones lie completely below the baseline, they are instead stored in another parameter, called OtherBlues. Beyond these parameters, three others of lesser importance also
appear in PostScript fonts: BlueScale, BlueShift, and BlueFuzz. We shall describe them
in §C.3.4.1. Finally, there is one other boolean parameter, which has the advantage of
being easily to understand, even for those who do not know much about how the rasterizing engine goes about using it: ForceBold. This parameter indicates to the rasterizing
engine that the font is bold and that the rasterization should be made “heavy” (so that
the difference between the font and any possible light version will be immediately evident).
The relevant stroke thicknesses are stored in the following manner: the “most relevant”
horizontal stroke thickness is stored in a parameter called StdHW, and its vertical counterpart is stored in StdVW; all other horizontal and vertical stroke thicknesses are stored in
two other parameters, StemSnapH and StemSnapV. Note that there can be no more than
twelve stroke thicknesses in each direction.
Now, here is how FontLab and FontForge manage global hints.
FontLab and global hints
In FontLab, we enter the following three types of data about global hints under three
tabs of the font-information window (File>Font Info):
• Hinting: alignment zones (see Figure 13-3 [a]): the two lists Primary zones and Secondary
zones contain the alignment zones for BlueValues and OtherBlues (the latter lie

(a) (b) (c) Figure 13-3: The tabs “Hinting Settings”, “Hinting Settings: Standard stems”, and “Additional hinting parameters”.

PostScript Hints
completely below the baseline). Clicking on the button Auto zones causes FontLab
to take the measurements and fill in the two lists for us.
• Hints: standard stems (see Figure 13-3 [b]): we enter in V Stems relevant thicknesses
of the vertical stems (the first goes in StdVW, the rest go in StemSnapV) and, likewise, the thicknesses of the horizontal strokes in H Stems. The ForceBold checkbox
enables this property. Clicking on the button Auto stems causes FontLab to take the
measurements for us and fill in the two lists as it sees fit.
• Additional hinting parameters (see Figure 13-3 [c]): we supply values for the parameters
ForceBoldThreshold, BlueScale, BlueShift, BlueFuzz.
FontForge and global hints
In FontForge, the management of global hints
is, as one might expect, both less pleasant and
more powerful than in FontLab. The data are
entered under a single tab of the font-information
window (Element>Font Info>PS Private Dictionary), shown opposite.
In the top part of the window, we choose the
parameter that we wish to modify: BlueValues
(alignment zones), OtherBlues (alignment zones
beneath the baseline), BlueScale, BlueShift,
BlueFuzz, StdHW (the most relevant horizontal stroke thickness), StdVW (ditto, but vertical),
ForceBold (whose value must be either false or
true). Other than ForceBold, the values that we
supply to FontForge must be written in PostScript’s tabular syntax, i.e., in the form of
numbers separated by spaces, with brackets around the whole entry.
The reader must be wondering what happened to the other relevant stroke thicknesses
(StemSnapV, StemSnapH). Clicking on the Add button reveals other parameters, including these two, from the “private” part of the PostScript Type 1 or CFF font. There
are even parameters specific to the ideographic scripts, such as ExpansionFactor and
LanguageGroup (see §C.3.4.3) and all the rest.
The functionality for the parameters for alignment zones and relevant stroke thicknesses
is the same as in FontLab: there is a Guess button, which will take the measurements for
us and supply values for these parameters. But FontForge goes further! For each of these
parameters there is a Hist (histogram) button; when we click on this button, FontForge
shows us an interactive histogram:

In the figure above, we see the histogram for the vertical stroke thickness parameter. In the Bar Width input area, we can specify the width of the histogram’s bars. That might seem pointless: why should we want to change the width of the bars in the histogram? Well, as with everything else in FontForge, there is a reason: the bars of the histogram are, in fact, interactive. When we slide over a bar, a small text box appears with a great deal of information: what is the exact value of the bar? How many glyphs have this same value? Even better: which glyphs have this value? Then, when we click on the bar, its value becomes the primary value (here StdVW). Clicking with the shift key depressed adds the value to the secondary values (here StemSnapV). Finally, the parameter Sum Around is also very interesting: it “blows up” the histogram and thus allows for a better understanding of the clustering of data by eliminating isolated extreme values. Individual PostScript Hints As their name shows, individual hints are defined at the level of each glyph. The basic idea is very simple: we tell the rasterizing engine which are the relevant horizontal and vertical strokes. The rasterizing engine detects strokes that appear at the indicated coordinates and arranges for them to have the same thickness in pixels, irrespective of the location of the centers of the adjacent pixels. The reason for the name “hint” is now clear: we hint to the rasterizing engine which strokes should have the same thickness, either within a single glyph or over all the glyphs in the font. Then the rendering engine will manage to perform its task correctly, respecting at all costs the directions that we have given. Unfortunately, that does not work as well as one might wish: there are complications and special cases to handle. The complications result from the way in which hints are defined: rather than connecting them to precise nodes on the glyph, Adobe preferred to consider

```text
PostScript Hints
hints as vertical or horizontal zones in such a way that all the strokes that coincide with
these zones are optimized. The intention was noble, but the approach works only if the
zones defined by the individual hints do not touch. For example, in the letter ‘H’, the
zones that will optimize the two stems do not touch, and so everything works perfectly.
But there are cases in which zones will inevitably touch. Take the letter ‘B’ below:
There are three vertical zones. By the very nature of the letter ‘B’, zones 2 and 3 will
inevitably overlap. What should we do in this case? To solve this specific problem in
Type 1 fonts, Adobe invented a horribly complicated method called “hint replacement”.
This method involves enabling and disabling, while the glyph is being traced, the hints
that overlap. That is one of the major difficulties in placing hints. We shall describe hint
replacement in §C.3.6.1 of this book. The situation is better for Type 2 (OpenType/CFF)
fonts: we must still do “hint replacement”, but the relevant structure and syntax are much
more rational (see §C.8.2.1).
The special cases that arise with hints come from a visual characteristic of the glyphs:
the fact that the symmetry between stems also extends to the white counters between
them. Take the example of the letter ‘m’: the stems of this letter must, of course, have the
same width, but that also applies to the two white spaces that separate them. It is just as
important to ensure that the two “crotches” of the ‘m’ have exactly the same width, in
pixels. But hints operate only on strokes, not on counters.
Adobe tried to solve this problem in two steps. The first measure taken affects only configurations of three parallel stems, as in ‘m’, the Greek ‘Ξ’, the Cyrillic letters ‘Ш’, ‘ш’, ‘Щ’,
‘щ’, the symbol ≡, ideographs such as 三, 且, 山, 彐, 日, 王, 田, etc. It involved an operator
(by the name of hstem3 or vstem3; see §C.3.6) to which we would supply three hint zones,
and the blank spaces between these zones would be equalized.
But Adobe quickly realized that handling configurations of three strokes was not
enough! One need only consider ideographs such as 皿, 目(4 strokes), 冒(7 strokes),
etc., to convince oneself that more powerful operators are needed. Moreover, when the
number of strokes runs that high, we realize that the danger is not so much that we
may have unequal white spaces but rather that there may not be any white spaces at all.
Indeed, the rasterization at a low resolution of a glyph such as 癴is a real challenge,
one that rasterizing engines in East Asia must face every day. Accordingly, Adobe’s
second attempt involved developing a system—once again inordinately complicated—
to manage situations of this kind (§C.3.6.2). This system was named “counter control”
```

```text
Figure 13-4: Displaying individual hints in FontLab.
and was used only in East Asian fonts. Only with the advent of Type 2 (OpenType/CFF)
fonts did Adobe finally provide a stable and robust operator to perform operations of
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
```

```text
PostScript Hints
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
But beware: automatic conversions cannot perform miracles! A link is, by definition, a
pair of nodes traversed by two lines for a hint’s zone. When we ask FontLab to convert
a hint to a link, it will first check whether there are indeed nodes on the two lines for
the hint. If there are not, as sometimes happens in poorly optimized fonts, the hint will
remain a hint, and FontLab will not issue an error message or otherwise complain. Thus
we should supervise this operation carefully.
The Tools>Hints
&
Guides menu
also allows us to initiate autohinting. But beware: before using this
command, it would behoove you to
check its configuration panel File>
Font
Info>Hinting
Settings>T1
Autohinting.
The numeric values in this configuration panel are of little importance, except perhaps in
extreme cases: for example, if the font has very thin strokes, Min width must be reduced;
if it has very thick strokes, increase Max width; if you want more hints globally, reduce
Min length. What is also really important is to select Tools>Hints & Guides>Remove
Hints>Both, since FontLab will otherwise add new hints to the old ones, thus making
the situation catastrophic. In Figure 13-1, the reader can compare the results of FontLab
autohinting to the lack of hints and to the analogous operation in FontForge.
Finally, a few words on hint replacement, a problem due to a poor definition of the concept of hints. We have seen that “hint zones”, i.e., the pairs of horizontal or vertical lines
that indicate the relevant strokes in a glyph, are defined for the entire working area of the
glyph. In Figure 516, we see at the left the hint zone that corresponds to the lower bowl
of the ‘B’ and, at the right, the zone that corresponds to the upper bowl. Obviously these
two hint zones do touch, thus running counter to the definition of hints. What can we
do so that when rasterizing the lower part of the glyph the rasterizing engine will ignore
the upper part, and vice versa?
The solution is as follows: first we divide up the outline of the letter, then we “attach”
hints to the various segments. When there is a hint within a given group of segments, we
```

```text
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
displayed in yellow. Then we select the first node of a segment of the outline and choose
on its pop-up menu Add replace point here. FontLab segments the outline and automatically attaches to this segment of the outline the hints that it considers relevant.
In Figure 13-5, we see the glyph window for the letter ‘B’ with four manually inserted
replacement points. At the left we see the first segment of the outline (in black, whereas
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
```

```text
PostScript Hints
FontLab does what is needed to make the glyphs with overlapping hints easy to detect:
the disputed area is painted yellow.
FontForge and individual hints
Figure 13-6: The management of individual hints in FontForge.
The management of individual hints in FontForge is a little less powerful than in FontLab. It is true that FontForge has a very efficient autohinting feature (Hints>AutoHint),
but, on the other hand, there are few possibilities for manual intervention. The hint
zones are marked with dotted lines and colored sky blue. The intersection of a hint zone
with a vertical or horizontal stroke is colored purple (for a vertical hint) or green (for a
horizontal hint).
Using Hints>Review Hints, one can modify the coordinates of the hint zones or add
or subtract hint zones. But those actions are done with coordinates, not with the mouse;
we are thus far from the pleasant interface of FontLab, where we can create hints and set
their positions in a few seconds, by simply moving the mouse.
When two hint zones overlap, the word “Overlap” appears in the Review Hints dialog box. FontForge will automatically divide the outline into segments and place the
replacement points for the hints—but there is no visible evidence of this operation, nor
any possibility of manual intervention.
```

TrueType Instructions
TrueType instructions are the means that we have for optimizing the rasterization of
glyphs in a TrueType font. Unlike PostScript hints, they are not values of parameters or
graphical zones but a genuine programming language. Furthermore, the view that font
designers have of TrueType instructions is not very different from Freud’s opinion of the
unconscious: “a cave where repressed desires move around in the dark”. Indeed, the sight
of hundreds of lines of code of this type:
MIRP[00100]
MIRP[10100]
MIRP[01110]
SRP1[ ]
SRP2[ ]
SLOOP[ ]
is enough to make anyone, not just a technophobe, break out in a cold sweat.
But is this cold sweat justified?
It is true that, unlike Adobe, Apple—which sparked the development of the TrueType
instructions—has always been partial to “hard” notation in computer science, perhaps to
highlight the contrast between the roles of Macintosh “user” (who communicates with
his machine through menus and dialog boxes) and “programmer” (who stumbled into
assembly language as a child).
We might have envisioned a high-level language that, when compiled, would produce
the assembly code for the instructions of today; after all, that is precisely what Knuth
did with METAFONT (see Appendix F). This high-level language does not yet exist and,
no doubt, never will. Nonetheless, various tools have been created to make up for this
deficiency: FontLab offers a simplified version of instructions with a graphical interface;
Visual TrueType, by Microsoft, offers a graphical interface that is a veritable factory for
instructions; and FontForge offers a built-in programming environment with an interactive debugger.
Not to mention that both FontLab and FontForge pride themselves on automatically
generating instructions for our fonts. As often happens in life, we have the choice of
• A quick solution (just a click on the button for automatically generating instructions), without troubling ourselves much over the details
• Or a method that gives us more room for maneuver, with a concomitantly greater
investment required on our part
• Or, finally, a difficult method that gives us 100 percent control over the rasterization
of our glyphs and also 100 percent of the responsibility for the result but that requires
extensive study of a nontrivial technique

TrueType Instructions
In this section, we shall adopt the second solution: a small dose of technical learning
through which we will gain control over the situation. For those who dare to pursue the
third course, we have written a very thorough description of instructions, illustrated by
real-world examples: it is Appendix E of this book.
The principle of instructions is as follows: to optimize the rasterization of a glyph, we
change the shape of its vector outline. The change involves modifying the underlying grid of
pixels. Then we will obtain a new outline, more or less different from the original one, for
each grid, and thus for each size of glyph. We call this new outline the grid-fitted outline.
It must be understood that the grid-fitted outline will not necessarily be as beautiful as
the original outline. After all, no one will ever see it, since it exists only to yield a good
rasterization. Once the grid-fitted outline has been obtained, the rasterization engine
need only apply the rule about the centers of the pixels (blacken the pixel if its center
lies within the outline, else leave it white) in a strict, even stupid, manner, and the job
is done.
Why should one bother to obtain an outline customized for each size when it would
be enough to activate or disactivate pixels? Because the customized outline, unlike the
original outline, is not designed specifically by the font’s designer; on the contrary, it is
produced automatically by means of a number of rules. By stating these rules, we obtain
all the customized outlines for every size. In fact, this rule is not absolute, as there is
indeed a way (we call it a δ instruction) to modify the individual outlines customized
for certain sizes. But it is the exception, and in most cases a few rules for customizing the
outline are enough to render all glyph sizes correctly.
The goal of instructions is to express these rules (and their exceptions).
How should we go about altering an outline? For the TrueType language, an outline is
nothing more than a series of points, some of which (the nodes) lie on the curve and others (the control points) offthe curve. An outline can be modified only by manipulating
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
• Other points will be set at an appropriate distance from a touched point. The appropriate distances in a list of values called CVT (for “Control Value Table”), which is
found in the TrueType table cvt. When we move two points so that they are set at an
appropriate distance, this distance is always at least one pixel; thus we have a property
for the minimum distance.

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
been moved; finally, we interpolate all the other points.
Now that we have explained the general principle, let us move on without delay to the
management of instructions by the chief software systems. We shall see how each of them
manages instructions in a different way, with its own advantages and disadvantages.
Managing Instructions in FontLab
It is clear that FontLab has undertaken an enormous effort in the area of the design
of instructions and of their human interface, even though it provides only a simplified
version of instructions. FontLab has succeeded in reducing the essence of the instructions
to six visual operations called visual hints:1alignments, links, double links, interpolations,
and two types of δ instructions: medial δs and final δs. With these six operations, the user
can instruct her font and view the rasterization in real time. When a TrueType font is
generated, the visual hints are converted into genuine TrueType instructions.
What is striking about visual hints is the blend between the concepts of instructions
(alignments, interpolations, δ instructions) and those of PostScript hints: links, introduced by FontLab as an improvement to the concept of a hint zone. Indeed, FontLab
considers hints as a sort of preliminary step to instructions. For instance, global hints
(relevant heights, relevant stroke thicknesses, etc.) are used in PostScript and TrueType
alike. Moreover, FontLab has no direct function for automatically optimizing a rasterization through the use of instructions; instead, we find, on the one hand, optimization
through the addition of hints and, on the other, an operation for converting hints into
visual hints.
The user interface
The interface for managing instructions in FontLab deserves some discussion. At first
blush it may give the impression of being a “juggernaut”; but when we become familiar
with its tools, we find that they are all useful and that the various methods for representing information are actually complementary and globally effective. Because we should
not deceive ourselves: a user interface that claims to present to the user all the information about the instructions of a given glyph (at a given size) should be able to display,
1 Not to be confused with Microsoft’s Visual TrueType operations, which are also called visual hints and
which we shall study in the section dedicated to this software.

TrueType Instructions
Figure 13-7: Managing visual hints in FontLab.
all at the same time, the original outline, the customized outline, the resulting rasterization, the grid of pixels (with their centers, the baseline, and the alignment zones clearly
displayed), the six types of visual hints represented by different symbols, and, finally, the
rasterization of the glyph at its actual size, since what seems horrible at a large size is
often impeccable at the actual size. Representing all this information simultaneously is
a real challenge, and we can say that FontLab is well up to the task.
In Figure 13-7, we see FontLab’s basic working environment for visual hints. To switch to
“instruction” mode, we need only select Tools>Hints & Guides>TrueType Hinting.
Then the TrueType Tools, shown above and to the left, appears, together with the
TrueType Options dialog box, which is shown immediately below.
To see the different layers of information and the two other windows that appear to
the right of the glyph, we use the last button at the right end of the bar, the button
.
Clicking on this button opens a pull-down menu with the following options:
• Hinted outline: show the glyph’s customized outline. To see it, pay close attention
to Figure 13-7: the hinted outline is the gray one shown inside the black outline,
marked with node numbers. The hinted outline depends on instructions and is updated whenever the instructions are modified.
• Grid lines: show the grid. The first option in the TrueType Options box (Current
PPM, or “current pixels per em”) shows us the size of the glyph. In the figure, the
glyph is of size2 15, with a set-width of 11 pixels.
2 Recall that we speak of “size” when we measure the height of a glyph in pixels and of “actual size” when
we measure it in points.

• Pixel centers: mark the center of each pixel on the grid with a dot. This feature is
not offered for ornamental purposes. As we know, a pixel in the final outline will be
black if its center lies inside the modified outline. Thus it is quite important to know
where the centers of the pixels lie with respect to the modified outline so that we can
insert a δ instruction that will make a pixel black or white by slightly modifying the
outline. In addition, we see in the image that the pixels (2,3) and (4,3) came within
a hair’s breadth of being made black, which would have made the curve’s descent
too dark.
• Resulting image: show the pixels of our rasterization—an indispensable option.
• Point numbers: show the point numbers. This option is useful only when combined with the TrueType Program window, which we shall discuss just below.
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
Of the buttons in TrueType Tools, there are two whose effect is global: the button
displays vertical visual hints (i.e., those that apply to horizontal strokes), and
displays
horizontal visual hints (applied to vertical strokes). The effect of these buttons is not
confined to display: we can even switch outright from a “vertical mode” to a “horizontal
mode”. According to the active mode, the buttons that we shall discuss below will produce horizontal or vertical visual hints.
Now let us take another look at the different types of visual hints and their manipulation.
Alignments
Alignments are made with the button
. They are horizontal or vertical, according to the
active mode. The term “alignment” is a bit unfortunate: here it refers not to aligning two

```text
TrueType Instructions
points with each other but rather to aligning a point with respect to the boundary or
center of a pixel. It would be more correct to speak of “rounding relative to the grid”. In
any event, alignment is often the first operation that we perform (moreover, it is always
executed first, as the reader will notice on the list in the TrueType Program window).
It consists of the “correct” placement of an initial point, from which we will then place
other points.
To “align” a point, we click on the button
and then choose the appropriate method of rounding in the group of buttons that appears
in the middle of the TrueType Option window, shown opposite.
The first three buttons mean, respectively, “place the point on the
nearest pixel boundary” (for vertical alignment, that would mean
moving the point up if it appeared above the center of the pixel and down if it appeared
below the center), “place the point at the bottom of the pixel” (the left side, in horizontal
mode), and “place the point at the top of the pixel” (the right). The two buttons below
are used for more sophisticated alignment: Center means that the point will be identified with the center of the pixel that contains it. We thus obtain a pixel surrounding the
point, whatever the circumstances of the rasterization may be; that may prove useful, for
example, for the point of the letter ‘v’, which should be “as pointed as possible”. Finally,
Double means that we will round according to a grid twice as fine as the current grid:
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
in the direction of the relevant height. We can prevent this automatic behavior by holding down the shift key while we click.
One last comment: aside from the points of the outline (the nodes and the control
points), two other types of points can be manipulated—the glyph’s origin and its setwidth. The origin is always “aligned”, but there is no reason that the set-width should
also be so aligned. If our glyph is symmetrical (like the ‘O’ in Figure 13-7), we should
reflect on the left side of the glyph the behavior of the right side. To this end, the least
that we can ask is for the point representing the glyph’s set-width to be “aligned” as well.
```

```text
Single and double links
Links follow the same principle as PostScript hints: they “link” two points in such a way
that their distance is handled in a certain manner, whatever the size of the glyph may be.
What exactly is this treatment? It depends on the link’s type. We have already said that
there are “single” and “double” links. A single link is a link whose starting point must be
a touched point, whereas its ending point must not be one. The most interesting single
links are those that are connected to a relevant distance. Let us explain. While discussing
PostScript hints, we mentioned relevant stroke thicknesses. We can generalize this concept and say that in a font there are some distances that are used in multiple glyphs
and that guarantee the font’s aesthetic uniformity. For instance, it may happen that the
counter of an ‘n’ in a given font is equal to those of the ‘m’ or that the breadth of the ‘O’
is the same as that of the ‘Q’.
We can store dimensions of this kind and use them to create interesting links. To do so, we click on the ellipsis in the top part of the
TrueType Options window, shown opposite.
The window below then appears:
Each line on the list corresponds to a relevant dimension. The lines on a clear background correspond to vertical dimensions; those on a yellow background, to horizontal
ones. The name of the relevant dimension is also shown in the glyph’s window each time
a link makes use of the dimension. The second column contains the dimension’s value.
The other columns contain the size of the glyph, in pixels, at which the dimension in
question changes from 1 to 2 pixels, then from 2 to 3 pixels, and so on, up to 6 pixels.
(The difference in stroke width is assumed to be insignificant from 6 pixels onwards.)
By clicking on a line, we can edit it—in the bottom of the window. For example, we can
specify precisely the moment at which a new pixel will be added to the dimension, and
our specification will apply to the entire font.
To establish a single link, we click on the button
(a yellow circle) on the bar TrueType Tools. Then we determine, in the window TrueType Options, how this link will
be connected to a relevant dimension: should FontLab automatically find the nearest
relevant dimension (Automatic)? Is there no relevant dimension that is connected to
```

```text
TrueType Instructions
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
point at the start, nontouched point
at the end”, we must sometimes define
the links in a certain order. Take the
example of the letter ‘m’ shown opposite. We start with the five links , ,
, , and , which must be defined in
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
too far away if the outline were significantly modified. We have prepared two examples, drawn from the optimization of this same letter, ‘m’. We use a heavy vertical stroke
to represent the set-width of the optimized glyph and a broken stroke to represent the
glyph’s original set-width. The image on the left is that of the glyph without link ; the
image on the right includes this link.
At 9 points, without link  the customized outline is much wider, which causes the optimized set-width (which is nothing but a rounded version of the original set-width) to
be too narrow and the right-hand side bearing to be missing altogether:
```

Conversely, at 12 points, the customized outline is much narrower (because the stroke widths are always one pixel and the counters always two pixels) and the set-width is too wide,3 giving a right-hand side bearing of 3 (!) pixels: In these two examples, the addition of link  restores the situation and shows the utility of a link that is not connected to any relevant dimension. In addition to single links, we also have double links. Their peculiarity lies in the fact that they are placed between two non-touched points—which, consequently, become touched. Establishing a relationship between a double link and a relevant dimension works just as with a single link. What does it mean to say that the two points of the double link must not have been touched? It means that the double link is, in a sense, “independent” of everything else—that it is not its position that matters but its dimension. For example, we shall place double links on the two sides of the letter ‘O’— links connected to the dimension “thick stroke of the ‘O’ ”, shown opposite. What matters here is not the width of the ‘O’ but the fact that its two sides have exactly the same width, and that is what the two double links ensure. To establish a double link, we click on the button (a blue circle) on the TrueType Tools bar and then proceed as with a single link. Should we use single or double links? Both are useful, but often we achieve a good result with less effort by using double links. Interpolations This operation allows us to interpolate the movement of a point relative to those of two other points. We have already mentioned that all the nontouched points are interpolated relative to the touched points anyway at the end of the optimization process. The difference here is that, first, this interpolation is done before the execution of the links and, 3 We could have requested, through the control table for the relevant dimensions, that the counters of the ‘m’ increase to 3 pixels starting at 12 points (in the example in question, that happens only at 14 points). That would have produced a wider glyph. It is up to the designer to choose the less unattractive solution. Note that a decision of that sort would also have had repercussions on a plethora of other glyphs (the ‘n’, the ‘h’, etc.) that use the same relevant dimension.

```text
TrueType Instructions
second, rather than relying on automatic interpolation, which is based on the nearest
points, we can perform interpolation here relative to carefully chosen points—points
that may be arbitrarily far away.
To interpolate a point c relative to two points a and b, we first click on the button
(a
green circle) on the TrueType Tools bar. Then we click on a, drag it to c, and click on b.
δ instructions
FontLab adopted unchanged the technique of δ instructions as it is defined in the TrueType specification. The intention is noble, but one small problem remains: TrueType’s
δ instructions are inserted into a program; thus they appear at a given moment and
operate on the position of the points at that very moment. Here the time at which the
δ instructions are instantiated is less clear: all that we know is that alignments come first,
then interpolations, and finally links, in the order in which they were created by the user.
If we add a visual δ hint, when will it be executed?
Not to worry. FontLab has taken a wise decision by defining two types of visual δ hints:
medial δs and final δs. Medial δs are executed along with the links, while final δs are executed at the end of the optimization process, after global interpolation. Thus medial δs
are modifications to the optimized outline that take part in the work done by the links,
whereas final δs are last-minute solutions employed to eliminate an annoying pixel or
creating a pixel where its absence is most cruelly felt.
Certainly the reader is beginning to wonder: is it not dangerous to play with pixels? After all, at every size the configuration of the pixels is so different that we cannot sensibly
talk about pixels without also specifying the size. Quite so: δs depend on the size. They can
be defined for a specific size or for a range of sizes. For example, we can take action only
where there is truly a problem and correct it without affecting anything at other sizes.
To apply a δ to a point of the outline, we first click on the button
(for a medial δ:
it represents a capital delta indexed by a letter ‘M’) or on the button
(for a final δ:
it represents ΔF). Then we click on the point in question and drag in the direction of
the movement. The δs are the only visual hints for which there is no difference between
horizontal and vertical mode, as FontLab will systematically create two δs: a horizontal
one and a vertical one, corresponding to the projections of the movement obtained by
dragging the mouse. Warning: movement is done in eighths of a pixel and cannot exceed
one pixel. We can edit the values of a δ and the sizes at which it is applied in the lower
part of the TrueType Program window, separately for the horizontal and vertical parts.
Here is an example of applying a final δ in order to move a pixel (encircled on the left
side of the image) that had the nerve to put itself in the wrong place:
```

δ As can be seen on the right side of the image, inserting a final δ half a pixel to the left and half a pixel upwards was enough to correct4 the wayward pixel. Generating or importing bitmaps There are branches of computer science in which fonts are very seldom changed. For instance, since 1987, when the author bought his first Macintosh, he has used only one font, and at only one size, to prepare his documents: 9-point Monaco. If this font had been a TrueType vector font, then for all these years, every time the font was displayed on the screen, the rasterizing engine would have had to execute the same instructions only to obtain the same rasterization over and over again. That is a waste of memory and of CPU cycles. We are far removed from the graphical applications in which thousands of fonts are used at virtually all possible and imaginable sizes, for which real-time rasterization is crucial. The reason that we are driven to rasterize our fonts in real time is that we cannot store 4 The astute reader will surely have noticed that there is a paradox here. By applying a δ to the upper curve, we naturally blackened a new pixel, since its center appeared inside the outline. But since we have not modified the lower curve, why did the “wayward” pixel disappear? If its center lay inside the outline before, it still does! By way of answering this question, let us take a closer look at the situation before and after the δ: We see that the pixel is black although it should not be, since its center lies slightly outside the outline. The explanation is as follows: we slightly underestimated the rasterizing engine by saying that it uses pixels alone to decide whether to blacken a given pixel. Here the engine noticed that there would be a white pixel here if only the centers of the pixels were used, whereas the outline itself does not have a discontinuity at this point. Probably by applying criteria such as the continuity of the surface or the distance between the curve and the center of the pixel, the rasterizing engine, in its infinite wisdom, decided to break the rules and give us a black pixel at that location. When we took action by adding a pixel through the use of the δ, the exception no longer existed, and the “hidden” pixel disappeared.

TrueType Instructions
all the rasterizations on the disk. But if there is a small number of sizes that we use very
frequently, the storage of a bitmap rasterization becomes an attractive option.
It is for these reasons that TrueType fonts can indeed contain bitmap fonts (the EBLC
and EBDT tables; see §D.7). FontLab allows for the generation of such bitmaps, which are
identical to the rasterization displayed in “visual hints” mode.
To generate a bitmap for the current glyph and at the current size, we switch to “bitmap”
mode by clicking on the button
of the TrueType Tools bar. Next, we select the option
Generate bitmap in the window’s pop-up menu. Once generated, the bitmap can be
modified by simply clicking on its pixels.
Through this same pop-up menu, we can import a bitmap from another font. Finally,
we can also ask FontLab to show us the differences between the imported (or generated)
bitmap and the bitmap produced by rasterizing the glyph. For that purpose, we enable
the option Highlight differences on the pop-up menu and leave “bitmap” mode: the
pixels whose values differ in the two versions are displayed on a red background. FontLab
even recommends the following common strategy: take a good bitmap, display it as a
background task, and create visual hints until the two bitmaps coincide. A funny way
to work!
Behind the scenes
The reader who has read Appendix E and mastered the concepts and syntax of TrueType instructions may be curious to know how FontLab’s “visual hints” are turned into genuine instructions.
It is surprising to observe how easily this conversion is made:
• An “alignment” is nothing but MDAP (move direct absolute point) instruction, i.e., a rounding
according to the active rounding method.
• A “single link” is an MDAP of the first point followed by an MIRP, i.e., an indirect relative move;
since the first point has become a point of reference because of the previous instruction, we
simply take a value from the CVT and apply to the second point a movement equal (in pixels)
to the CVT.
• “Double links” are more complex: FontLab uses a function (defined in the fpgm table) that
will put things in place for this rather special visual hint. The last lines of the function take
the MDAP and the MIRP from the single link.
• “Interpolation” is nothing but an IP interpolation instruction.
• Similarly, a “δ” is merely a DELTAP1. The restriction on the size of a “δ” comes from the fact
that we can change neither delta_base nor delta_shift.
Thus we see that “visual hints” are simply a small subset of TrueType instructions. But thanks to
FontLab’s enjoyable interface, this subset enables us to perform very effective optimizations.
Managing Instructions under VTT
The history of VTT goes back to the earliest days of TrueType. The author of TrueType,
Sampo Kaasila, also wrote a tool for instructing fonts. This tool, called Typeman, it seems,
was sold at exorbitant prices on the order of thousands of dollars (!). Later the product

was called TTED (= TrueType Editor), and for the past several years it has gone by the name
of VTT (= Visual TrueType).
VTT is distributed free of charge by Microsoft. But be warned! “Free of charge” does not
mean “freely”. To obtain a copy of VTT, one must print out a copy of the license [261]
and fax it to Microsoft. Usually within a few days one will be given access to the VTT discussion forum, from which the software can be downloaded (for Mac OS 9 or Windows).
Nevertheless, the documentation and all the ancillary resources are available freely on
Microsoft’s site [262].
How does VTT compare to FontLab? Both offer graphical interfaces for instructing TrueType glyphs. VTT’s interface is less pleasant to use, less aesthetically appealing, and less
ergonomic than that of FontLab, but VTT is closer to the real TrueType instructions and,
therefore, gives access to features that are inconceivable under FontLab. Yet VTT has this
in common with FontLab: the user is not required to learn the assembly language for
instructions, as everything is done in a graphical manner. VTT offers a graphical adaptation of instructions that is more powerful than that of FontLab, and therefore necessarily
more complex.
How do the approaches of VTT and FontLab differ? First of all, VTT offers a completely
different vision of the management of relevant dimensions (relevant heights, stroke
widths, etc.).
Control values
We have seen that FontLab allows us to store relevant dimensions in a table, give them
names, and indicate when their rasterization changes from 1 to 2 pixels, from 2 to 3, and
so on. When a TrueType font is generated, this table internal to FontLab feeds the table
CVT (“control values table”), which is contained in every TrueType font.
VTT, for its part, allows us to operate directly on the control values table. Indeed, unlike
the TrueType specification, VTT attaches precise semantics to the entries in the CVT table, or
at least to its first 120 values. For instance, we have shown in Figure 13-8 the meanings
of the entries 0 to 20, 22, and 24.
On the other hand, VTT classifies glyphs into four groups: “uppercase”, “lowercase”, “figure”, and “other”. (The group of a glyph can be redefined, and new groups can be defined
at any time.) The glyphs in Figure 13-8 belong to these four groups.
Finally, the CVT entries are classified according to their color, direction, and property. The
“color” depends on the color traversed by the link, which we shall define as follows:
• Black only: we say that the CVT entry in question is “black”, as, for example, the
horizontal width of the ‘I’.
• White only: we say that the entry is “white”, as, for example, the counter of the ‘n’.
• Or both black and white: the entry is “gray”, as, for example, the one that connects
the upper and lower strokes of the ‘8’, which thus traverses the two counters and the
juncture of the strokes.

TrueType Instructions 14+15 4+5 12+13 2+3 6+7 6+7 6+7 10+11 10+11 10+11 16+17 18+19 0+1 8+9 Figure 13-8: The meaning of CVT entries 0–19. These are different relevant heights. For each height n, entry n+1 contains the corresponding overshoot. The notation 2+3 indicates that the height in question is the sum of entries 2 and 3. Finally, 20, 22, and 24 are the slopes of the capitals, the lowercase letters, and the numerals. Str. Round Str. Round SH Str. SW Str. Round (66) Dist. Str. Round SH Dist. Str. SW Dist. Str. Round Str. Round SH Str. SW Str. Round Str. Round Str. Horiz. Vertical Diag. Horiz. Horiz. Horiz. Vertical Diag. Horiz. Horiz. Horiz. Vertical Vertical Vertical Diag. Diag. Black Black Black Black White White White Uppercase Lowercase Figures Other (67) (67) (67) (67) (66) (66) (66) Figure 13-9: The meaning of CVT entries 68–119. The abbreviations “SH” and “SW” mean “serif height” and “serif width”. The broken arrows indicate inheritance.

```text
The “direction” may be horizontal, vertical, or diagonal. Finally, the “property” is also
a predefined string, selected from “thickness of a straight stroke” (StraightStroke),
“thickness of a curve” (RoundStroke), “serif height” (SerifHeight), “serif breadth”
(SerifExtension), “another distance” (Distance). Figure 13-9 shows the classification of
CVT entries 68 to 119 according to these four criteria: group, color, direction, property.
In Figure 13-9, we have also shown—with a broken arrow—another important property
of CVT entries under VTT: inheritance. We say that a “daughter” entry inherits from a
“mother” entry if they are rendered with the same number of pixels, up to a certain
size—the size at which the daughter breaks free of the mother and can be rendered by
a different number of pixels. The sire of all the entries of a relevant dimension is entry 65 (which is both horizontal and vertical). Entries 66 (horizontal) and 67 (vertical)
inherit from it and are therefore, in a sense, the most relevant dimensions of the font. We
see in Figure 13-9 that entries 68, 81, 97, and 110 inherit from 66 and that entries 72,
85, 101, and 114 inherit from 67: that ensures a certain uniformity in the font, one that
will no longer be maintained beyond a certain size, when there will be enough pixels
for the difference of stroke thicknesses in these groups of glyphs to be felt. Finally, within
each group (uppercase, lowercase, etc.), the thicknesses of round strokes inherit the thicknesses of straight strokes.
Note that this classification of strokes recapitulates, in a sense, the principle of the parameters of METAFONT (see Appendix F), if only with regard to rasterization. Of course,
METAFONT goes much further by parameterizing the relevant dimensions themselves,
not only their bitmap rasterization. But let us not forget that METAFONT works quietly
up the line, whereas the TrueType rasterizing engine must fulfill the user’s requests in
real time.
Let us return to the classification of the CVT entries. Their interest lies not only in the
fact that they force us to organize the rasterization of the font. It lies mostly in the fact
that VTT, like FontLab, will automatically select the CVT entry to which a link will be
connected. But unlike FontLab, where relevant dimensions are classified only by their
names and their directions, VTT is aware of the group to which the current glyph belongs
and also knows the link’s color: “black”, “white”, or “gray”; thus it will automatically
choose a CVT entry with the correct group, direction, and color. Thus there are much
better chances that the automatically selected entry will be the correct one in VTT than
in FontLab.
Opening/saving a file
VTT knows how to open TrueType files under Windows and Mac OS 9 (or Mac OS X, in
the Classic environment).
But there is a small problem under Mac OS 9: the font must not be contained in a Macintosh “suitcase”. Thus, under Mac OS 9, one must double-click on the font suitcase to open it and then extract
the TrueType font (warning: this operation is not possible under Mac OS X, which fact seriously
compromises the functionality of VTT under that system). Next, so that the file in question will
be recognized by VTT, it must be of Macintosh file type sfnt. To that end, a utility for converting
file types (such as File Buddy) is necessary. After that manipulation is complete, everything works
correctly, and VTT will open the font with no problems.
```

TrueType Instructions Let us now skip the steps and suppose that we have finished optimizing a TrueType font. Before distributing it, we must strip out all “private” data, i.e., those that have been added through VTT. Specifically, VTT adds a number of tables to the font’s TrueType structure, and if the font is not free, it might not be prudent to distribute these tables— which, after all, contain the entire strategy for instructing the font—to the end user. But beware! Unlike FontLab or FontForge, each of which has its own file format, VTT uses the TrueType format as both a “working” file format and a format for the generated fonts. Fonts are generated through the menu option Tools>Ship Font, and it is therefore necessary to take care to select a different font name, or a different target location, or else the original font will be overwritten by the file generated and the internal data will therefore be irretrievably lost. The glyph window Figure 13-10: The glyph window of VTT. VTT’s interface consists of a glyph window, a font-table window (where we can choose the glyph to manipulate), and a number of text windows, the most important of which are the control-program window, which represents an uncompiled version of the CVT table,

```text
and the glyph-program window, which displays, in real time, the TrueType instructions
generated from the VTT visual hints.
Unfortunately, the glyph window does not display both the original outline and the customized outline at the same time, as FontLab does. We have to switch from one to the
other by enabling or disabling the option Display>General Options>Grid fit (shortcut:
ctrl-G).
In Figure 13-10, we see the glyph window in “customized outline” mode. Here we have
chosen to view the pixels in gray-level mode; in fact, we have the choice of several rasterizing engines, including different versions of ClearType’s technology. At the top are
a number of buttons, which we can slide back and forth through the use of the small
triangles. At the bottom, we can preview the glyph at its actual size; by clicking on one
of the sizes at the bottom, we change the grid of the glyph displayed in the middle of the
window.
The window of the control program
We obtain this window by selecting View>Control program. It represents, at the beginning, the contents of the file CvtTmpl.txt: the value of the primary CVT entries and a
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
```

TrueType Instructions
we ask the rasterizing engine to add a pixel at 18 points and to remove one at sizes between 32 and 100. For those who have read Appendix E, let us note that these are DELTAC
instructions that appear in the prep table. These are global instructions that must not be
confused with DELTAP instructions, which affect only one glyph.
We have already mentioned that other CVT entries are classified by group, color, direction, and property. We can write:
UpperCase
Black
X
StraightStroke
68: 200 = 66 @27
to indicate the classification of the entry (indentation is optional). In this notation, the
groups (Uppercase, Lowercase, Figure, Other), the colors (Black, White, Grey5), the directions (X, Y, Diag), and the properties of strings (StraightStroke, RoundStroke, SerifHeight, SerifExt, etc.) are predefined.
We can define new groups by writing, for example:
GROUP Kanji
Then we must declare the glyphs in the file CharGrp.txt and associate the appropriate
glyphs with the new group.
To enter the correct values of CVT entries in the control-program window, we must
measure a number of heights, widths, and stroke thicknesses. VTT offers us a tool for
this purpose that can be invoked by clicking on the Measure button. Before taking measurements, we are required to hide the pixels and switch to “original outline” mode by
disabling Display>General Options>Grid fit and Display>General Options>Pixels. To
choose the correct glyphs and the correct dimensions to measure, we can draw inspiration from Figures 13-8 and 13-9.
Warning: After every modification to the control-program window, it is necessary to recompile the CVT through the use of Tools>Compile>Control values.
Modifying a glyph’s trace
VTT’s operations depend a great deal on the correct positioning of the outline’s nodes. It is quite
probable that we will notice, while in VTT, that a node is poorly placed or that it is superfluous,
or that one is missing at a certain location. VTT gives us the tools to correct the problem:
• Move will move a node.
• Swap will transform a point offthe curve (i.e., a control point) into a point on the curve (i.e.,
into a starting/ending point of the Bézier curve), and vice versa.
5 The word “grey” is spelled in the British manner, not the American one (“gray”).

• Delete will delete a node without breaking the outline.
• Insert will insert a node at a given point on the outline.
To be able to use these tools, we must be in “original outline” mode (disable Display>General
Options>Grid fit). On the other hand, the Swap operation makes sense only if the points offthe
curve are visible: that can be achieved by disabling Display>General Options>Show fewer points.
Those used to the trace mode for Bézier curves in FontLab or FontForge will need to break their
habits. When Insert is selected, VTT will insert a point offthe curve if Show fewer points is
disabled or a point or the curve otherwise. Whether the point lies on or offthe curve determines
the curve’s behavior: we need only consider that the fact that a Bézier curve between two points
on the curve and with no points offthe curve is necessarily straight. The points offthe curve are
responsible for its curvature.
To make an inserted point the starting point of a new trace, it is necessary to right-click (under Windows; °-click on the Macintosh). But since VTT is not glyph-design software, it is recommended
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
2. The situation of an italic glyph whose slant has been specified with the Angle tool.
In order for this rounding to be useful, the stroke in question must have this slant
(in which case we use YLink) or be perpendicular to the slant (XLink).
3. Like the previous case, but the slant is not an abstract slant but rather a slant calculated from pixels (whose angle is thus slightly different and depends on the resolution).
On every line there are six boxes, containing six symbols:
1. The first corresponds to the absence of rounding.

```text
TrueType Instructions
2. The second is classical rounding (the left/bottom or right/top edge of the pixel, according to the position of the point with respect to the center of the pixel).
3. The third is the rounding of the center of the pixel in which the point is found.
4. The fourth is rounding according to a subgrid of half-pixels. In other words, the point
will be placed on the edge of a pixel or over the center of a pixel, whichever is closer.
5. The fifth is rounding down (towards the left or the bottom).
6. Finally, the last is rounding up (towards the right or the top).
Thus we have the same rounding methods as in FontLab, except that special attention is
paid to slanted strokes, according to the angle of their slope.
Vertical anchors (produced by Ylink) may be connected to a
relevant height. To this end, one enables the option Display>
Visual TrueType Options>Anchors. All the vertical anchors
are then represented by an icon shaped like the U.S. interstate
highway shield:
.
In addition, when the option Display>Visual TrueType Options>Cvt numbers is enabled, these highway shields are displayed larger and contain numbers (see opposite). These numbers are the CVT entries connected to the anchors. Ordinarily,
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
The first novelty: the CVT entries to which the links are connected are selected not only
according to the width of the link but also according to the group of the glyph, the color
of the link (“black”, “white”, or “gray”), and the link’s direction.
On the other hand, links can be of various types, according to the nature of the stroke and
our choices of minimum distances. After drawing a link, we right-click (under Windows;
°-click on the Macintosh) on the head of the arrow, and one of the two pull-down menus
shown below appears:
```

```text
depending on whether the link is horizontal or vertical. Then we slide the mouse to a
box to indicate the type of the link.
The four columns of these pop-up menus have the following meanings:
1. The link is not connected to any CVT entry. We say that the link represents a distance.
2. The link is connected to a CVT entry that is neither “straight” (the StraightStroke
property) nor “round” (the RoundStroke property). We will use it, for example, for
the breadths of serifs and other dimensions that cannot be classified into these two
cases.
3. The link is connected to a “straight” CVT entry (the StraightStroke property); thus
it represents the thickness of a straight stroke or the breadth of a straight counter.
4. The link is connected to a “round” CVT entry (the RoundStroke property); thus it
represents the thickness of a curvilinear stroke or the breadth of a round cavity.
As for the rows of boxes:
1. The icons in the first row represent links without a minimum distance. The thickness
in question can therefore be rendered with 0 pixels.
2. Those in the second row (with the symbol of an “opening elevator door”
) represent links with a minimum distance. The minimum distance may be from 0 to 8 (!!)
pixels, in units of one-eighth of a pixel. By default, its value is 1 pixel. To change
the minimum distance for a given link, we first enable the option Display>Visual
TrueType Options>Minimum distance, which has the effect of displaying an icon of
an “opening elevator door” over the link. Right-clicking (under Windows; °-click on
the Macintosh) on this icon displays a ruler bar. By sliding from right to left—feel
free to slide offthe end of the ruler, only a small part of which is visible—we can
indicate, with a precision of an eighth of a pixel, the exact value of the minimum
distance, between 0 and 8 pixels.
3. Those in the third row (with the symbol of a “closing elevator door”
) are there
for legacy reasons: Typeman, the predecessor of VTT, took the initiative to force minimum distances into existence, even where they were not desired. By selecting a link
of this type, we can abandon Typeman’s choice and obtain all the same a link with
no minimum distance.
Opposite, by way of example, is shown a letter ‘m’ in which the side bearings, the stems,
and the outlines have been connected.
```

```text
TrueType Instructions
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
We insert a shift by choosing the tool X Shift (or Y Shift for a vertical shift) and proceeding as for a link.
Interpolations and alignments
Interpolations work as in FontLab. We select points that will be the reference points for
the interpolation. Then we select one or more points that will be interpolated relative
to the first two. There are no constraints: since we are doing interpolation rather than
extrapolation, the projections (horizontal or vertical) of the points to be interpolated
must lie between those of the reference points.
To perform interpolation, we select the tool X Inter (or Y Inter for vertical interpolation).
We click on the first reference point and drag the mouse to the second. A black line is
thus drawn between the two points. Next, we click on this line and slide to the point to be
interpolated. If there are points to interpolate, we repeat the procedure as many times
as necessary. VTT will represent the interpolation by a series of white arrows chained
together that will run through all the points, the first one starting from the first reference
point, the last one ending on the last reference point.
Alignments (not to be confused twith FontLab’s “alignments”, which are roundings of
an individual point relative to the grid) are a stronger form of interpolations in which
we request that points be mutually aligned with one another at all costs. That is really
of interest only for points that fall on the same slanted straight line, since for points
aligned horizontally or vertically an alignment can be obtained much more easily by
rounding them.
```

```text
A typical example of alignment is the slanted and discontinuous stroke of the ‘A’ (see
opposite), for which the rasterizing engine has no way, in the absence of an instruction,
to guess that the pieces above and below the cross stroke absolutely must be aligned.
We insert an alignment by selecting the Align tool and joining (by dragging the mouse) the two extreme points of the points to be aligned. VTT
will produce as many blue arrows as there are points between these extremes. By playing with the heads of these arrows, we can exclude some
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
example, in the figure below, points 2, 5, 4, and 3 constitute two pairs, (2, 5) and (3, 4).
We click on one of the four (for example, 2) and drag to the matching point (here, 5);
then we click on the point that is on the same side as the first, at the other end of the
stroke (here, 3), and drag to the remaining point.
As we drag the mouse the second time, the area of the stroke turns black. When we have
finished, the area is shown hatched on a yellow background, with a “highway shield” in
the middle that indicates the number of the CVT entry selected by VTT:
We can change the CVT entry as usual by making a contextual click on the highwayshield icon and selecting the appropriate entry.
The starting points for the two links (here, 2 and 3) are automatically made into anchors.
δ instructions
These δs are shifts of the nodes to the customized outline. They are our last hope for
correcting minor imperfections that the other instructions have left behind. They must
```

```text
TrueType Instructions
be used in moderation: they do allow us to add a pixel here or delete one there, but we
must be careful not to overuse them, since they increase the bulk of the font. One or
more rasterized sizes can be affected by a δ.
We can classify δs according to their direction (horizontal or vertical), their amplitude
(between 1
64 and 8 pixels), the sizes of rasterization to which they apply, or the moment
of their execution in the assembly code for TrueType instructions: “inline” (inline), “just
before global interpolation” (pre-IUP), or “after global interpolation” (post-IUP).
To insert δs, we must enable the option Display>General Options>Grid fit and possibly
also the option Pixels.
The tools XMove and YMove are used for horizontal and vertical δs that apply to all sizes
of glyphs; the tools XDelta and YDelta are used for those that apply only to the active
size. The sizes are independent with respect to δs; thus we can apply several different δs
to the same point, each corresponding to a different size.
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
If “gray scale” mode has been selected (Tools>General Options>Gray scale), a rightclick/°-click will limit the δ’s scope to gray-scale rasterizations. Conversely, if “black-andwhite” mode is selected, the δ will apply only to rasterizations of that type. This feature
allows us to restrict δ instructions to a certain kind of rasterization.
```

```text
A few examples
We shall examine three typical examples (the letters ‘O’, ‘H’, and ‘A’) drawn from the font
Trebuchet in a VTT tutorial [260].
The letter ‘O’ from this font is shown opposite. In the image, we have enabled the option Show fewer points; thus
we see only the points on the curve (the others do not
have an effect on visual hints).
We shall first place an anchor at point 3—an anchor
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
would ordinarily cause some pixels not to be black (which would leave holes in the outline of the ‘O’ when rendered with pixels). Thus we can be sure of obtaining good stroke
thicknesses.
Finally, we shall deal with the side bearings. We shall connect the origin (point 23) and
point 0 with a “distance”, i.e., a link not connected to a CVT entry. We shall do the same
on the other side: we connect the glyph’s set-width (point 24) and point 6 with a “distance”. But this time we specify a true minimum distance, of one pixel. Thus the glyph
may have a zero approach on the left, but it will always have an approach of at least one
pixel on the right.
Here, then, is the result of our instructions, as shown in VTT:
```

TrueType Instructions Note that all the links go from the outside inward. That allows us to direct any changes to the outline towards the inside of the glyph, where they will be less damaging to the glyph’s overall appearance. Let us continue with this font’s letter ‘H’. We shall start by placing anchors in order to ensure alignment with the other glyphs: points 6 and 9 will be connected by CVT entry 2 (the height of a capital letter), and points 3 and 0 will be connected by entry 8 (the baseline of a capital). Next, we shall concern ourselves with the thicknesses of the strokes: we shall connect points 5 and 7, then 10 and 8, with horizontal links. VTT will automatically select CVT entry 68 (“capitals, black, horizontal, straight stroke”). We shall request a minimum distance of one pixel so that the stroke will not disappear under any circumstances. Here there is a trap. For us humans, it is obvious that point 2, for example, must have the same abscissa as point 7. But from looking at the outline, it is not at all obvious to the rasterizing engine that that must be so. Therefore, to prevent stroke thicknesses that differ for the upper and lower parts of the glyph, we shall also set links from 5 to 3 and from 10 to 0, with the same width and type as the previous links. After that, we shall ensure the correct thickness of the cross stroke. To that end, we shall create a vertical link between 2 and 8. This link is automatically connected to CVT entry 72 (“capitals, black, vertical, straight stroke”), and we request a minimum distance of one pixel, so that the cross stroke will always be visible. But what about the position of the cross stroke? Rather than defining a special CVT entry for the height of the cross stroke of the ‘H’, we can make use of an interpolation: after all, the position of this cross stroke is not of critical importance. Let us take points 0 and 6 as the extreme points for our interpolation. But which point shall we interpolate: the one on the top of the cross stroke, or the one on the bottom? To answer that question, let us consider another: if the height of the glyph is an even number of pixels, we shall have to decide to place the cross stroke either above or below the imaginary line that runs between the two pixels in the middle. What would be the more appropriate choice? From the aesthetic point of view, we would prefer for the cross stroke of the ‘H’ to err on the high side. Moreover, we can see right away in the original outline that the cross stroke appears slightly higher than the middle of the glyph. Thus we must interpolate, and round, a point below the cross stroke (for example, point 2). Then the pixels resulting from any possible rounding error will be propagated towards the top of the glyph. Finally, to include the instruction of the glyph, we resolve the problem of the side bearings by adding “distances”, just as with the letter ‘O’. Here is VTT’s representation of our instructions:

```text
We shall conclude this series of examples with the letter ‘A’.
Note that, in the image opposite, the lower left point of the
letter (point 4) is mistaken for the origin (11) and that the
lower right point (7) is mistaken for the set-width (12).
We shall begin by placing anchors at the relevant heights: at
points 5 and 6 (CVT entry 3: “height of a capital letter with
overshoot”) and at points 4, 3, 0, and 7 (CVT entry 8: “baseline of a capital letter, without overhang”).
We shall also set an anchor at point 8. It will not be linked to
a CVT entry, but it will use a very special rounding method—
rounding towards the center of the pixel—to ensure that the point will be rendered by
one and only one pixel.
How shall we handle this letter horizontally? If the extreme points are close enough to
the edges of its abstract box, then the side bearings are completely insignificant, and we
shall not worry about them (as we did with the ‘O’ and the ‘H’). On the other hand, we
know that we have the stroke tool to handle the thickness and rasterization of slanted
strokes. What we need is a mechanism to ensure that the letter will not lean to one side—
in other words, a mechanism to preserve the letter’s vertical symmetry.
We shall bring out the big guns in order to obtain this symmetry. For example, we shall
define a new CVT entry, representing half the distance between 3 and 0, i.e., half of the
letter’s internal width. That entry will be classified as “capitals, gray, horizontal, distance”.
Next, we shall create horizontal links between points 8 and 3, and then between 8 and 0.
VTT will associate them automatically with the new CVT entry. We shall request that
they be given a minimum distance of one pixel, so that the slanted strokes will not run
the risk of becoming vertical. The fact that the two links run from the outside inward
ensures that the letter can be drawn a bit wider so that its design will be correct.
To avoid any risks, we shall also deal with the letter’s external width by creating an interpolation: point 8 will be interpolated horizontally relative to points 4 and 7. Nothing
remains but to use the stroke tool on the two slanted strokes; VTT will automatically
select CVT entry 77 (“capitals, black, diagonal, straight stroke”).
```

```text
TrueType Instructions
One final precautionary measure: will the two slanted strokes be aligned on both sides
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
Finally, to ensure that the cross stroke will remain horizontal, we shall perform “alignments” (YShift) between the pairs of points (9, 10) and (2, 1).
Here are the new instructions that we have just added:
(Here we have represented only the instructions not shown in the previous figure.)
```

Managing Instructions under FontForge
While FontLab and VTT offer us interactive interfaces for creating instructions, FontForge follows a different approach, that of the integrated development environment
(IDE). For instance, it offers us a debugger for TrueType instructions that allows us to
follow, step by step, the evolution of the original outline to the outline customized for
the grid. Other windows (see Figure 13-11) display the contents of the registers, the storage area, and the stack, as well as the coordinates of the points of the glyph, in real time.
There is, however, a catch. As is described on the project’s web page FreeType [330], the library of
subroutines used by FontForge’s debugger is subject to certain patents held by Apple. To use it,
one must therefore request a license from Apple or be located in a country where the patents in
question are not valid. And since the FreeType project does not wish to subject honest people to
temptation, the code required by the debugger is not compiled in the default version of FreeType.
To be able to work with FontForge’s debugger, therefore, one must first recompile FreeType after
having slightly modified the code. Here is how to do so:
1. Obtain the latest version of the sources for freetype from
http://sourceforge.net/project/showfiles.php?group_id=3157
2. Decompress them and open the file
include/freetype/config/ftoption.h
3. Replace
/* #define TT_CONFIG_OPTION_BYTECODE_INTERPRETER */
with
#define TT_CONFIG_OPTION_BYTECODE_INTERPRETER
i.e., uncomment the definition of the C preprocessor directive.
4. Compile FreeType and install it by following the instructions in docs/INSTALL.
Only after this maneuver will the debugger for TrueType instructions work in FontForge.
The debugger’s interface
Let us open a glyph for editing in FontForge. When we select Hints>Debug, a small
window asks us for the size of the rasterization that we wish to debug and the resolution
of the device. Once this window is closed, the glyph’s window splits into two. On the left:
the original outline of the glyph, shown in black on a grid of pixels (whose centers are
marked by small crosses), an approximation by straight strokes of the modified outline,
and the positions and numbers of all the nodes. On the right: a series of seven buttons
and, below it, a numbered list of all the instructions in the glyph.
The buttons have the following functions:
• The
button causes the following instruction to be executed. If it is a procedure
call, we will go into the procedure and execute its first instruction.
• The second button,
, also proceeds step by step with the execution of the program
but does not go into procedure calls. This is the button that we shall use the most
often.

TrueType Instructions
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
, by simply clicking on a line. A second click disables the breakpoint.
The principle of a watchpoint is different, and especially interesting: we select a point
on the outline and click on the button
. The point is then “watched”. We can launch
the rapid execution of the instructions: as soon as an instruction modifies this point,
execution will halt. In this way, we can find the instructions that will modify a given
point and, by so doing, achieve a better understanding of the operation of instructions.
When we reach the end of the code, we need only click twice on a button that initiates
execution (such as
), and the code will be executed again from the beginning.
It is impossible to understand the operation of instructions without constantly monitoring the instruction stack, the graphics state, and possibly the storage area, registers
and CVT. That can all be done through the use of auxiliary windows obtained by means
of the button
. There is also a “glossary” window providing explanation on TrueType
instructions.

Figure 13-12: Seven auxiliary windows: Registers, Cvt, Storage, Points, Stack, Raster, and Glossary. It is also possible to edit instructions. We do so with another window, which is obtained with Hints>Edit instructions. Figure 13-13: The FontForge window for editing TrueType instructions. This window—which, unlike the debugger, is not constrained by patents and is therefore always available—displays a numbered list of instructions. By clicking on the Edit button, we can modify the instructions. Note that the modifications are not immediately conveyed to the debugger: we must halt the execution of the code and start it again.

Enriching Fonts: Advanced Typography Introduction The title of this chapter refers to the “advanced typographic features” of OpenType and AAT fonts, which are tables added to the basic TrueType fonts by Microsoft, Adobe, and Apple. We have witnessed the emergence of two new font formats: OpenType (defined by Adobe and Microsoft, formerly called “TrueType Open”) and AAT (for “Apple advanced typography”, formerly called “TrueType GX”). Thanks to these tables, we can better meet the needs of the non-Latin scripts, in particular the Asian scripts, but also some of the requirements of traditional typography, well beyond the possibilities of the original TrueType format. Here, then, is the dialog box for OpenType in Adobe Illustrator CS2 (under Mac OS X), where the different OpenType features (default ligatures, calligraphic letters, etc.) are shown in the form of buttons that are enabled only when the feature in question is present in the font: Whether for setting type in Sanskrit, in Urdu or Arabic with aesthetic ligatures, in Hebrew with vowel points, in Elzevirian Greek with ligatures, in calligraphic Latin, or simply in a text font with capitals and old-style figures, OpenType and AAT tables are well
