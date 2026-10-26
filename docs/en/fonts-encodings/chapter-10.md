---
title: "Chapter 10: Fonts and Web Pages"
description: "Unabridged English text: HTML and CSS font specifications, font-size-adjust and x-height, web font embedding (TrueDoc, WEFT/EOT), SVG fonts."
---

# Chapter 10: Fonts and Web Pages
**By Yannis Haralambous, Ph.D.**
*From Fonts & Encodings, pp. 315–366*

---

```text
Fonts and Web Pages
When Tim Berners-Lee defined the HTTP protocol and the HTML markup system, he
could hardly have expected that the whole world would be talking “.com” 20 years later.
The explosion of the Web is without a doubt one of the highlights of the end of the
twentieth century.
HTML is a markup system—a set of rules for the structure and the semantics of tags.
It is based on SGML, the Standard Generalized Markup Language—“generalized” in the
sense that it has no semantics, only rules for writing. An SGML document is composed
of elements. An element is represented by a pair of tags: the opening tag (written &lt;name&gt;)
and the closing tag (written &lt;/name&gt;). Between these tags is the element’s “content”,
which can contain other tags and/or textual content. An element can have any number
of metadata called attributes. Attributes take the form of “key–value” pairs written within
the opening tag. Their number and their order are arbitrary.
An SGML document may be accompanied by a Document Type Definition (DTD), included in the file or stored in an external file. This DTD is a set of data of two types: first,
a list of all the elements allowed in the SGML document, together with their attributes
and the types of data that may have these attributes; second, a list of rules for the behavior
of the elements with one another. We can specify, for example, that a given element may
contain another given element a certain number of times, or that it must be empty, or
that it may contain anything, and so on.
HTML is an SGML DTD, and, at the same time, a markup syntax. That means that the
tags that may be used in an HTML document are well defined once and for all, that their
interaction with one another is also defined, and that we have a sort of “user’s manual”
that shows us the meaning and applicability of each tag.
```

But unlike LATEX, in which the meaning of each tag is as clear as can be,1HTML assigns only an approximate meaning, and each browser may interpret that meaning as it chooses. HTML has suffered greatly from the artistic fuzziness that surrounds its tags. For example, each browser has felt itself obliged to add its own tags to the basic system, which has led to frequent updates of HTML, many of them based on the initiatives of some of the browsers with the largest market share. Despite that fact, however, it must be understood that during the era when the Macintosh, the Windows PC, and Unix stations had a terrible time communicating with each other, HTML was (together with TEX and, a little later, Acrobat) the first “document format” common to all operating systems. To solve a number of problems without completely tearing the HTML standard apart, two new layers of information were added: JavaScript, a programming language developed by Netscape (and later to become an ECMA standard under the name of ECMAScript), whose purpose is to manage the interactivity of HTML pages, and Cascading Style Sheets (CSS, a W3C standard), a language for describing the appearance of HTML pages. These three layers of information (HTML, JavaScript, CSS) live together in harmony within a single document. Furthermore, JavaScript has access to the information in all three levels, thanks to a syntax called Document Object Model (DOM, also a W3C standard). But let us leave history aside and move on to the situation that exists today. Several years ago, a successor to SGML arrived on the scene and literally conquered the market: XML (Extensible Markup Language, a W3C standard). XML, which we shall discuss in greater detail on page 345, is a stricter version of SGML—and “stricter (for the human)” means “easier to manage (by machine)”. Indeed, whereas there were only one or two very specialized tools for processing SGML that were quite inaccessible to the ordinary mortal, today we have an enormous number of tools—industrial, mass-market, or free—for working with XML. By slightly constraining the freedom of markup that SGML affords (the differences between SGML and XML can be summed up with five simple rules), XML has succeeded in wiping out the unfavorable impression that the public had of SGML (“labyrinth”, “juggernaut”, etc.) and in establishing a genuine format for data exchange that can be used in all areas of computer science. Between the fantastically expanding XML and the aging HTML, we eventually find ourselves faced with a sharp contradiction. The World Wide Web Consortium (W3C) has suggested a solution: an XML-ized version of HTML, known as XHTML. In addition, XML inherits technologies from the HTML era: JavaScript, CSS, and a technique specific to XML that is called namespaces. Namespaces are a means of combining several DTDs, i.e., of creating documents with tags coming from various and sundry sources, with predefined semantics in different contexts. Since XHTML has been defined and codified, we know that it does not have any tags that support the creation of mathematical formulae. But a standard exists that does make it possible to create them: MathML. By 1 This is true because LATEX is a programming language and we can follow the execution of a LATEX command right down into the bowels of TEX. A LATEX command is therefore a “tag” whose semantics are defined a posteriori by its effects when we compile a document using that tag with TEX or Ω.

using a namespace for “XHTML” and another for “MathML”, we can simultaneously use
tags belonging to both standards without causing any conflicts. In this way, every new
standard can be used immediately within XHTML documents, provided, of course, that
tools for processing it are available.
In this chapter, our concern shall be font management as performed using the technologies of the Web.
We can see that fonts are one of the Web’s major problems, for the very simple reason
that fonts, unlike text and illustrations, are the only resources in a document that do not
belong to the document’s author. If they do not belong to the document’s author, that is
because they are under license, and he does not have the right to distribute them freely.
To display a web page, one can limit oneself to using only the fonts that are available
on the client’s system; but then one needs either to know their names or to use generic
names. If one absolutely insists on using a specific font (for example, if one must display
text in a script that is not supported by all operating systems), it is necessary to communicate with the client, and that is where the technical problems and questions of rights
begin.
We can observe that the subject of fonts has been approached from three different angles,
which will form the three main divisions of this chapter:
• HTML offers a certain number of tags for font selection; for its part, CSS offers a
certain number of instructions for describing the fonts used in (X)HTML pages, be
they local fonts (present on the client’s sytem) or fonts downloaded from the Web
(provided that the browser is capable of downloading fonts from the Web).
• Two companies have developed plug-ins that enable browsers to obtain through the
network the fonts that are needed to display an HTML page. These are Bitstream
(TrueDoc technology) and Microsoft (Font Embedding technology). Bitstream has apparently had only limited success with the browsers that are compatible with its
technology: Netscape 4.x (but not version 6 or 7), Explorer under Windows only,
and iCab. Microsoft’s technology for incorporating fonts is compatible only with its
own browser (Explorer) and only under Windows; its benefit is that one can freely
create downloadable fonts.
On the other hand, a Swedish company by the name of em2 Solutions markets the ne
plus ultra for fonts on the Web: a server plug-in named GlyphGate. This software uses
many different techniques for displaying a document with precisely defined fonts
by adapting itself to the technical capabilities of the client browser. According to the
browser being used, GlyphGate may send totally different information to different
clients, either by taking advantage of downloadable file formats for some browsers
or, in the worst case, by generating GIF images for the words in the document. GlyphGate is Unicode-compatible and is able to display any script on any browser. There
is even a software development kit (SDK) for adapting GlyphGate to special fonts or
scripts.
• A new standard, by the name of SVG, was developed by the W3C. It is based on XML,
and its purpose is to describe a page’s geography, through the use of glyphs, bitmap or

vector images, and interactive or dynamic elements. Naysayers will maintain that it
is an XMLization of the PostScript language, which is not altogether wrong, as Adobe
was the originator of this standard. In any event, font management under SVG is
very rich, to the point that there is even an ad hoc font format, which makes it possible to include within a document the vector description of the glyphs to be displayed
while at the same time treating them as characters (selection with the mouse, copying and pasting, searching for strings, etc.). SVG is a very promising technology, and
it deserves a detailed study, even though, to date, not all browsers natively support
it.2
(X)HTML, CSS, and Fonts
The Standard HTML Tags
Since the beginning, HTML has offered a number of tags for enhancing text: &lt;address&gt;
(the “address” mode, which both Netscape and Explorer have chosen to represent with
italics), &lt;b&gt; (bold), &lt;cite&gt; (the “citation” mode, represented with italics), &lt;em&gt; (the emphasized mode à la LATEX, represented with italics), &lt;i&gt; (italics), &lt;code&gt;, &lt;kbd&gt;, &lt;pre&gt;,
&lt;samp&gt;, &lt;tt&gt;, (typewriter type), &lt;strong&gt; (the “strong” mode, represented with italics
or bold type), &lt;var&gt; (the “variable” mode, in the sense of variables in a programming
language).
Versions 1 to 3.2 of HTML include an element called &lt;font&gt; for specifying the active
font. This element was dropped from version 4 of HTML in favor of CSS and, of course,
is also absent from XHTML. Here are the different attributes that this element could take,
during its short life:
Name
Netscape
Explorer
Example of usage
color
≥2
≥3
color="#660099"
face
≥3
≥3
face="Helvetica, Arial, sans-serif"
point-size
-
point-size="12"
size
all
all
size="-2"
weight
-
weight="300"
In the case of the face attribute, one can use any number of “font family names”, separated by commas. These names are the names by which fonts are identified by the system;
in other words, Quickdraw names on the Macintosh, Windows names under that operating system, and part of the XLFD name under Unix.3 Since these names are quite
variable, it follows that the approach used here is far from infallible. To compensate for
2 See http://www.svgi.org on SVG compatibility with browsers. This URL also provides a comprehensive list of resources, tools and documentation.
3 In Mozilla’s dialog box for selecting the default fonts, for example, one may choose fonts whose names
are made up from the foundry’s name, the family name, and the primary and secondary indicators of the encoding
(in the sense of XLFD; see page 222):

```text
(X)HTML, CSS, and Fonts
these problems, the standard provides five “generic” font-family names, to be added to
the end of the list: serif, sans-serif, cursive, fantasy, monospace. Each browser is free
to choose a font for each of these generic names, and all recent browsers allow the user
to select a representative font for each of these “categories”.
The size attribute is perhaps the HTML attribute that is the most poorly understood by
users. This is how it works: one may choose an absolute value (between 1 and 7, the
default value being 3) or a relative value (between +1 and +7 or between -1 and -7).
Contrary to the mathematical notation that we all learned in school, here +3 and 3 do
not have the same meaning: the former increases the active size by three units; the latter
calls for the size named “3”, thus a medium size.
There is a variant of &lt;font&gt; by the name of &lt;basefont&gt;. It takes the attributes color,
face, and size. It was also abandoned in version 4 of HTML. The difference between
&lt;basefont&gt; and &lt;font&gt; is not clear.
CSS (version 3)
CSS is a W3C standard that manages the display of elements in an (X)HTML document.
The idea is as follows: one writes rules for display, with each rule containing a selector,
which determines the elements that will be displayed in a certain manner, and a set
of declarations, which determine the way in which elements selected in advance will be
displayed. The word “cascading” refers to the method for managing selectors and declarations. Take the following CSS code as an example:
&lt;style type="text/css"&gt;
em { color:pink; text-decoration: underline; }
.important { color:green; text-transform: uppercase; }
p em { color:blue; font-family: "Helvetica"; }
p > em { color:red; font-size: 24pt; }
&lt;/style&gt;
Here we have four CSS rules. The first deals with em elements and requests that these
elements be typeset in underlined pink type (thus there are two declarations: one for
the color pink and one for underlining). The second applies to any element with a class
attribute whose value is “important”, and it requests that these elements be set in green
type and in full capitals. The third applies once again to em elements, but this time only to
those that “have a p ancestor”, i.e, those that are contained with a p element, at any depth
whatsoever: it requests that they be set in blue and in Helvetica. Finally, the fourth again
applies to em elements, but this time only to those that are direct children of a p element;
they must be set in red and at 24 points.
We can see here that Mozilla chooses to omit all the other fields of the XLFD name so as to make the choice
easier and to retain better control over the properties of the selected fonts.
```

This example may seem absurd at first glance, but what it is intended to illustrate is that
when an element appears in all these categories, the rules of the CSS standard specify
the priority of one or another property, while preserving all properties that do not cause
a conflict. In the example, we always have two declarations: the color, different in each
case, and another property, which is unique. Let us consider the following HTML code:
&lt;em class="important"&gt;A few words;
how will they be displayed?&lt;/em&gt;
The em element that we see here is “selected” by all the rules in the style sheet. How will it
be displayed? Well, it is clear that it will be displayed in capitals, in Helvetica, underlined,
and at 24 points, because these properties do not come into conflict. On the other hand,
what will its color be? CSS clearly defines the rules of the game: in this example, the
class="important" constraint is the most important; thus the block of text will be set
in green. And that will be true in every CSS-compatible browser. This last point is very
important, as it guarantees that a page will be displayed in the same way everywhere.
Note that CSS allows us to short-circuit the hierarchy of priorities by adding among the
declarations for one rule the keyword “!important”.
In the following material, we shall not go into the details of the syntax and features of
CSS. For those subjects, there is a plethora of books, as instructive as they are comprehensive, that the reader may consult; for example, [151] (O’Reilly), [254], and, last but
not least, the CSS specification, published by the Web consortium [88]. For our part, we
shall instead make a detailed study of the use of fonts under CSS (version 3).
CSS declarations for specifying the active font
Recall that a CSS rule consists of a selector (one or more (X)HTML tag names, or the name
of a class, or an identifier, or a combination of the three), which indicates the parts of the
document that are affected by this presentation rule, and a set of declarations (name–value
pairs), which indicate the visual properties of the material to be displayed. The general
syntax is as follows:
selector { name: value; name: value; name: value; etc. }
What are the declarations that manage fonts? They are of two kinds: there are seven for
selecting the active font and five others that manage “decorations”. Here are the seven
most important declarations:4
• font-family (NN4, IE4), which takes as its value a number of font names (Quickdraw names on the Macintosh, Windows names under that operating system, a part
of the XLFD name under Unix [see note 3]) placed within single or double quotation marks and separated by commas. The order of these font names is the order of
4 To indicate the compatibility of these declarations with the Netscape Navigator and Internet Explorer
browsers, we shall use the following abbreviations: ‘NN’ followed by a number indicates the version of
Netscape since which the declaration has been supported; ‘IE’ indicates the version of Explorer; ‘W’ indicates
Windows; ‘M’ indicates Macintosh.

(X)HTML, CSS, and Fonts
precedence for font selection, provided that the font exists on the client’s system. For
example, we may write:
body { font-family: "PMN Caecilia", "Helvetica", "Arial MS",
sans-serif; }
where PMN Caecilia is the name of a very specific font that perhaps does not exist
on all platforms (unless it is downloaded together with the page, which we shall see
later), Helvetica is the name of a Macintosh font that is one of the default fonts, Arial
is the name of the same font but under Windows, and sans-serif is a generic keyword (the same keywords as those used with the &lt;font&gt; attribute are available here:
serif, sans-serif, cursive, fantasy, monospace, or none [when we wish to disable
font substitution]). Thus we move from the specific to the general, hoping that the
browser will find the corresponding font as soon as possible.
But the Web is an international facility, and the specificity of the font also entails
the specificity of the script, and more specifically the Unicode zones covered by each
font, i.e., the set of Unicode characters that can be represented by the font. The fontfamily declaration allows us to take glyphs from multiple fonts, according to what
they have available. Thus, by writing:
body { font-family: "PMN Caecilia", "Heisei Gothic W3",
"Arial Unicode MS", sans-serif; }
we take the glyphs for the Latin characters from PMN Caecilia, the glyphs for the ideographic characters (more specifically, the Japanese characters) from Heisei Gothic W3,
the glyphs for Cyrillic or Greek characters from Arial Unicode MS, and everything else
from sans-serif, provided, of course, that the font selected by the client’s browser
is sufficiently rich.
In other words, the browser will check not only the existence of a given font but also
the existence of each glyph in each font, one by one, and will choose for each glyph
the first font that contains it.
Finally, note that among the among the CSS selectors we also find the language of
the block of text. We can thus connect the selection of a font to that of the active
language. That possibility is particularly attractive when several languages share the
same Unicode characters but are written with different glyphs. Here is an example
in which we use the selector :lang(), which indicates the language of the XML or
XHTML element, specified through the xml:lang attribute:
*:lang(de) { font-family: "DS-Normal-Fraktur", serif; }
*:lang(fr) { font-family: "Fournier MT", serif; }
*:lang(ja) { font-family: "Heisei Mincho W3", serif; }
*:lang(zh) { font-family: "Li Sung", serif; }
In this example, we have decided to write German in the Gothic script (using the
“standardized Gothic” of Delbanco Schriften), as it was still written just a bit more
than 60 years ago. For French we are using a typically French font (the magnificent

Fournier, by Monotype); for Japanese, we use a Japanese font, and we use a Chinese
font for Chinese.5
• font-style (NN4, IE4), which can take three values: normal, italic, oblique. Note
that CSS does not provide for switching to upright type in the event of “double italics”, i.e., a fragment in italics that appears in a block that is already in italics. But we
can simulate this behavior by writing, for example:
em { font-style: italic; }
em em { font-style: normal; }
em em em { font-style: italic; }
which means: the contents of &lt;em&gt; are to be set in italics unless this &lt;em&gt; appears
within another &lt;em&gt;, at any depth whatsoever. And if this second &lt;em&gt; is itself contained within another &lt;em&gt;, we shift back to upright type. But be forewarned: there
are other elements that are also set in italics; thus one must handle them all, one
by one, through the use of selectors.
Note that the value italic will result in oblique if no italic font is available but a
slanted font is available.
• font-variant (NN6, IE4), which takes only two values—normal and small-caps—
and thus is used only for small capitals. Note that since capital letters are being used
(since small capitals are in fact capitals, even though they are of smaller size), in order
to complete this operation successfully the browser must both have access to Unicode’s case-mapping tables (page 112) and be able to recognize the active language,
as capitalization often depends on the language: for example, the same word “liter” is
written “LITER” in capitals within an English context and “L˙ITER” within a Turkish
context.
• font-weight (NN4, IE4), which indicates the weight of the font. To this end, three
types of values are available: numerical values, absolute keywords, and relative keywords. The numerical values must be even hundreds between 100 and 900.6 The
possible absolute keywords are normal (which is equal to 400) and bold (700). The
relative keywords are bolder and lighter. Each of these raises or lowers the weight
by 100 units.
5 A word of explanation, to help the reader to understand these examples better. (a) Just over 60 years
ago, German was written in the Gothic script—which was not a choice of font, as it is today, but another script
altogether, with a full spectrum of quite varied fonts, comparable to the range of roman fonts that we enjoy
today. (b) Japanese, Chinese, and Korean are all written with ideographs and use the same Unicode characters,
but the fact remains that they often need slightly different glyphs for the same characters. We must therefore
use separate fonts, which, incidentally, creates big problems for printers in the corresponding countries: what
should be done when a Chinese word using a character specific to Chinese pops up right in the middle of a
Japanese document? or a character that is common to the two languages but that has slightly different glyphs
in each? Some will substitute a similar glyph; others will change fonts by using a makeshift font, which runs
the risk of destroying the visual unity of the text.
6 Why hundreds rather than simply integer values between 1 and 9? In the hope, no doubt, that the
browsers of the future will also be able to accept intermediate numeric values, somewhat like the Multiple
Master fonts.

(X)HTML, CSS, and Fonts
• font-stretch (no browser), which indicates the font’s set-width. Once again we have
absolute and relative keywords. The absolute keywords are ultra-condensed, extracondensed, condensed, semi-condensed, normal, semi-expanded, expanded, extraexpanded, ultra-expanded. As one might expect, the relative keywords are wider and
narrower; they enable us to move up or down one level in the series.
• font-size (NN4, IE4), which indicates the font’s actual size. To represent this size,
we may choose:
– A dimension, expressed in em (the em of the current font, i.e., its actual size), ex
(the height of the lowercase letter ‘x’), px (pixels), pt (American printer’s points),
mm, cm, or in (inches).
– A percentage of the actual size of the active font.
– Absolute keywords (inspired by the sizes of T-shirts): xx-small, x-small, small,
medium, large, x-large, xx-large. The CSS specification recommends the
following correspondences between keywords, scaling/shrinking factors, and
XHTML heading levels:
Keyword
xx-small x-small small medium large x-large xx-large
Factor
60%
75%
89%
100% 120%
150%
200%
Heading
h6
h5
h4
h3
h2
h1
– Relative keywords: larger and smaller, which enable us to move up or down
one level in the series of absolute keywords. If, however, the size is defined by a
dimension, the browser is free to apply a scaling factor based on that size or to
round it offfirst so that its value will match that of an absolute keyword.
• font-size-adjust (no browser), followed by a rational number between 0 and 1.
To understand the usefulness of this declaration, which applies only to those scripts
that distinguish uppercase and lowercase letters, i.e., the Latin, Gothic, Gaelic, Greek,
Cyrillic, Armenian, and liturgical Georgian scripts and, by extension, the modern
Georgian7 and Arabic8 scripts (see Figure 10-1), let us conduct a little experiment.
The text that the reader is currently reading is set in Le Monde Livre, which has a rather
large x-height: the ratio between the height of the letter ‘x’ and the body size of the
font is 0.482. Now let us switch to Centaur, a font designed in 1915 by Bruce Rogers [228, p.
62] that many people consider to be one of the most beautiful fonts of the previous century.
Does the reader not have the impression that the text has suddenly become less legible? That
change results from the significant difference between the x-heights of the two fonts: that of
Centaur is only 0.366, or 25 percent less than that of Le Monde Livre. Here we are again in
7 Modern Georgian has no notion of uppercase and lowercase letters, but the Georgian letters do have
ascenders and descenders in certain styles. We can consider the x-height of this script to be the ratio between
the short letters and those with an ascender.
8 In Arabic, if one disregards the dots above and below the letters, there are two basic heights for glyphs:
the “tall” glyphs (alef, lam, etc.) and the “short” glyphs (beh, seen, sad, etc.). Here again, we can consider the
x-height to be the ratio between the tall letters and the short letters.

::: tip Typographical Specimen Plate (Figure 10-1)
![Figure 10-1: Web x-heights comparison](/images/fonts-encodings/fig10-1-web-x-heights.png)
*Figure 10-1: Web x-heights comparison.*
:::

![Figure 10-1: Web x-heights comparison](/images/fonts-encodings/fig10-1-web-x-heights.png)
*Figure 10-1: Web x-heights comparison.*

```text









Figure 10-1: The x-heights (ratios of the height of the short letters to the body size) of several typical fonts for different scripts: (1) the Latin script, Linotype Didot font, 0.42; (2) the Gaelic script,
Morley Bun˙cló font, 0.50; (3) the Gothic script, Delbanco Normal-Fraktur font, 0.52; (4) the
Cyrillic script, Monotype Garamond Cyrillic font, 0.45; (5) the Armenian script, MacCampus
Mesrop font, 0.30; (6) the Greek script, Monotype Greek 91 font, 0.41; and (7) the Georgian liturgical script, MacCampus Parnavaz font, 0.38. Next, two scripts with no uppercase/lowercase
letters: (8) the Arabic script, Monotype Naskh font, 0.22; and (9) the modern Georgian script,
ParaGraph Deda Ena font, 0.40.
Le Monde Livre, to continue our experiment. And what if we increase the actual size
of Centaur so that its lowercase letters have the same size as those of Le Monde Livre?
Here is the result! The text is certainly more legible now. We can see that
the uppercase letters are a little larger, but that is the price to pay if we
wish to keep the font intact. Later (page 441) we shall see the tools that
enable us to modify the font by changing only the size of the lowercase
letters, but let us not forget that that constitutes a major departure from
the font’s design.
As the reader will have guessed, the role of font-size-adjust is to effect this correction of the actual size of a font that is substituted for another. How does it work? The
information, known as the x-height, that is specified in this declaration is the ratio
between the height of the short letters (those that have neither an ascender nor a
descender: ‘a’, ‘c’, ‘e’, etc.) and the body size of the selected font. To return to CSS, if
```

(X)HTML, CSS, and Fonts
we wish to request Centaur in the stylesheet as the font to use for some text, we can
write:
body { font-family: "Centaur", serif; font-size: 16pt;
font-size-adjust: .366; }
In this case, if Centaur is not available and cannot be downloaded, and will thus be
replaced by the default font—for example, Times, which has an x-height of 0.46—
the actual size of this Times font will be not 16 points, as specified, but 14 × (0.366 /
0.46) = 12.73 points, which is more acceptable, as Times quickly becomes intolerable
at large sizes.
• baseline, centerline, mathline, topline: the height, expressed in the font’s internal units, of four “baselines”: the baseline of running text; the “central line” (without
going into too much detail, this line can be halfway between the height of the ascenders and the depth of the descenders); the horizontal axis for centering mathematical
symbols such as +, −, ×, etc.; and, finally, the top line (which can be useful for scripts
whose baseline is at the top, such as Devanagari).
Note that a “synthetic” declaration is available: font, which can take all the values of the
preceding declarations at once, along with a few ancillary values. Thus:
body { font: 500 italic 12pt/14.4pt "Palatino Linotype", serif; }
is the same as:
body { font-style: italic; font-weight: 500;
font-size: 12pt; line-height: 14.4pt;
font-family: "Palatino Linotype", serif;
font-stretch: normal; font-variant: normal; }
We can notice two things in this example: first, the fact that the declarations that are not
given an explicit value in font are initialized to their default values; second, that a new
declaration appears here: line-height, which determines the leading. Let us note that
font-size-adjust is not covered by font.
One last bit of information on the font declaration: it can also take as values the following keywords, but in that case there can be no other indication of size, weight, etc.:
• caption: the font used by the system for buttons
• icon: the font used by the system for the legends of icons
• menu: the font used for menus
• message-box: the font used in dialog boxes
• small-caption: the font used for “small buttons”

• status-bar: the font used for the status bar
Thus by writing font:
menu;, we obtain the font that the operating system uses for
menus, whatever that operating system may be. That is not possible with the separate
declarations font-size, font-stretch, etc.
And now here are the four declarations that manage “decorations” applied to fonts:
• font-effect (no browser), which takes the following values: emboss (set in relief),
engrave, outline, none. For lovers of effects meant for the screen rather than for
good old-fashioned paper.
• font-smooth (no browser), which specifies the smoothing, if any, to be applied to the
font: auto (use the browser’s rules), never (never smooth the font), always (always
apply smoothing). Or a keyword or a dimension chosen from those of font-size:
large, 14pt, 20px, etc. This possibility allows us to smooth text from a certain size
and up, as it is widely recognized that the smoothing of small glyphs tends to hamper
the legibility of text.
• font-emphasize-style (no browser), which applies to the ideographic languages
(Japanese, Chinese, Korean). In these languages, there is ordinarily no italic style,
and bold is not used within text in the way that we use italics in Western typography.
To “emphasize” a fragment of text, through the use of the &lt;em&gt; tag, one uses various
devices, the most common being small symbols (dots, commas, etc.) written above
or below the glyphs. This declaration specifies the type of emphasis mark to place
above (or below) the ideographs: accent (a brush stroke shaped like a droplet, which
is nothing but the ideographic comma), dot (a dot), disc (a heavier dot), circle (a
small circle), none (no symbol).
• font-emphasize-position (no browser), in the same vein as the previous declaration, specifies the position of the ideographic emphasis mark. The possible values
of this declaration may initially come as a surprise: before or after. It must not be
forgotten that the ideographic languages can be written both horizontally (from left
to right) and vertically (the lines are arranged from right to left). In the first case, the
values of this declaration must be interpreted as “above” and “below”; in the second
case, as “at the right” and “at the left”. Note that Japanese and Korean printers, and
Chinese printers from Taiwan, place these signs “before” (example: 微軟
◦
企
◦
業
◦
領
◦
航專
區), whereas printers from the People’s Republic of China place them “after” (微軟
◦企
◦業
◦領
◦航專區).
Creating a CSS “database” of fonts
In the previous section, we reviewed all the CSS declarations (of version 3) that make it
possible to specify the font desired for any element of an (X)HTML or XML document.
Now it is time to ask a question: how will the browser choose the font the best adapted
to our desiderata?

(X)HTML, CSS, and Fonts
To this end, we shall develop for the browser a “database” of fonts. Each of this database’s
entries will be a combination of “family name”, “Unicode coverage”, “set-width”, “weight”,
“style”, “variant”, and “actual size”, which can only take absolute values. For each entry,
one must specify:
• Either a way to download the font in question
• Or a way to make a judicious substitution
• Or a way to generate the font artificially from a generic font
Provided, of course, that the browser supports these possibilities—which is far from being the case at this time.
Let us take a few examples:
@font-face { font-family: "Charcoal";
panose-: 2 0 5 3 0 0 0 2 0 4;
units-per-em: 2048;
stemv: 340; stemh: 233; slope: 0;
cap-height: 1509; x-height: 1151; ascent: 1509; descent: -;
}
@font-face { font-family: "Omega Serif";
font-style: italic;
unicode-range: U+0020-, U+0300-E, U+1E??, U+2000-F;
src: url("http://omega.enstb.org/fonts/omsela.otf")
format("opentype");
}
@font-face { font-family: "Heisei Mincho W3";
unicode-range: U+3000-FA2D, U+FF00-FFEE;
units-per-em: 2048;
widths: U+3000-FA2D 2048, U+FF00-FF5F 2048, U+FF60-FFEE 1024;
bbox: -, -, 2048, 1755;
}
Here we have three entries in the font “database”. The first will be used when we request,
in an (X)HTML/XML document, Omega Serif italic in a very specific Unicode zone (which
corresponds, in fact, to the Latin alphabet and its punctuation); the second, when we
request Charcoal; and the third, when we request Heisei Mincho W3 in a specific Unicode
zone (that of the ideographic characters). What is interesting is that in the three examples
above, if the font in question is missing, we ask the browser to carry out three different
operations:
• In the first case, we ask it to find another font that is as similar as possible to the original font. To assist the browser in making this choice, we furnish a certain amount

of information: the font’s Panose-1 classification (see Chapter 11) and some fontmetric information, such as the thickness of the horizontal and vertical strokes, the
slope, etc.
• In the second case, we ask it to download the font in question from a given URL,
with the specification that the font is of OpenType format.
• In the third case, we ask it to use a default font, but scaled so that its dimensions
correspond to those of the original font. Thus we specify the bounding box of the
original font and the set-widths of all of its glyphs.
Note that we can include within a declaration some instructions for intelligent substitution, downloading, and synthesis, as in the following (hypothetical) example:
@font-face { font-family: "Heisei Mincho W3";
unicode-range: U+3000-FA2D, U+FF00-FFEE;
src: url("http://not.found.anywhere/heiseiw3.otf")
format("opentype");
units-per-em: 2048;
panose-: 2 0 5 3 0 0 0 2 0 4;
widths: U+3000-FA2D 2048, U+FF00-FF5F 2048, U+FF60-FFEE 1024;
bbox: -, -, 2048, 1755;
ascent: 1653; descent: -;
}
In this case, the browser will first try to make an intelligent substitution for the font (and
the Panose-1 classification is of crucial importance to that attempt); then it will try to
download the font, and if it fails, it will attempt a substitution through “synthesis” using
a generic font—provided, yet again, that the browser is capable of carrying out all these
operations, which is not yet the case today.
Now let us examine in more detail the various declarations at our disposal. First and
foremost, the syntax @font-face, which is that of an “at-rule”, which applies not to one
or more elements in particular but to the entire document. Unlike ordinary selectors,
which may not be repeated, the @font-face rule frequently appears multiple times, once
for each entry in the font “database”.
Within each @font-face rule, two types of declarations occur:
• Those that make connections to the fonts requested by the user
• Those that tell the browser what to do—make a substitution, download a font, generate a font, etc.
The first of these are nothing more or less than the rules of the previous section: they
include the “family name”—but with no alternatives provided; here we are concerned
with only a single family name—the Unicode zone covered, the “style” (upright, italic,

(X)HTML, CSS, and Fonts
oblique), the “variant” (small capitals), the “weight”, the “set-width”, and finally the actual size. In the last four of these, only absolute values are permitted; therefore, do not
use larger, narrower, 110%, 1.2em, etc.
The declarations that will be of interest to us below are the second: those that tell the
browser what course to take when the font with the requested family name is not available on the system.9
Let us start with the simplest case: downloading. For downloading a font, the following
keywords are available:
• url("a URL"), which enables us to specify a URL (HTTP protocol or a local file).
• format("font
format"), to indicate the font format. We may choose from the
following: truedoc-pfr, embedded-opentype, type-1 (PostScript Type 1), truetype,
opentype, truetype-gx, speedo, intellifont, svg.10 Note that, as always, the fact
that these names of font formats are part of the CSS specification does not in any
way guarantee that there is at least one browser in the world that can download and
use fonts of this kind.
• local("a
font
name"), to indicate the name of a font that is present on the local system. Recall that the font-family declaration uses the “family name”; here,
however, it is the name of the font itself that is used, and therefore a name that also
contains the style, the weight, the set-width, etc., and that is a member of the font
family. Example: “ITC Franklin Gothic” is the name of a font family that includes
“FranklinGothic-Demi”, and we shall therefore write:
body { font-family: "ITC Franklin Gothic";
font-weight: 600;
src: local("FranklinGothic-Demi");
}
We may use any number of local(...) and url(...) keywords, separated by commas:
the browser will attempt, in the given order, to use a local font or download a remote
font and will continue to the next entry on the list if the attempt fails.
Now let us proceed to intelligent substitution. To find what CSS considers to be a “good
substitute” for a font that is not available, it is necessary to be able to describe certain
characteristics of this font, and the browser will compare them to the characteristics of
the fonts that it has available. Then it will choose the font that is the most similar. Thus
everything comes down to selecting relevant characteristics, i.e., those that are both precise and readily computable. Here are the characteristics available to us:
9 In fact, at startup, the browser builds its own internal font database containing all the fonts on the
system. The declarations in this database are read before those of the document’s stylesheet. If a font is already
present on the system, the browser will not even read the declaration in the stylesheet and will thus not attempt
to replace, download, or generate the font.
10 The svg format is not mentioned in the CSS specification [88], but it is used in an example in the specification of SVG [134]. Surely its omission was an oversight.

• panose-1: the 10 whole numbers that make up the Panose-1 classification of the font.
In Chapter 11, we shall present the complete description of this system of font classification. The problem is still that only few font developers take the trouble of classifying their fonts according to Panose-1, which makes the substitution mechanism
uneffective. Another problem is that this classification is more suited to Western
scripts than to Eastern ones.11 But let’s not ask for too much! After all, is it possible to
classify all the scripts of the world according to a single schema? Certainly not; but
most non-Latin fonts also include a Latin component, and we can compare those
components through the use of Panose, which is already a good start.
• units-per-em: the number of units per em. This is the number of subdivisions of
an em used to describe the font: frequently 1,024 or 2,048, but it may run as high as
tens of thousands, according to the foundry. The larger this number goes, the more
precision we have; but the more precision we have, the more memory the rendering
engine needs to perform the various calculations. Thus there is a trade-offbetween
the precision of the design and the consumption of RAM.
• stemv and stemh: the main thickness of vertical or horizontal strokes. Unfortunately,
the standard provides no further explanations of this subject. But we can agree, in
the case of a Latin, Cyrillic, or Greek font, that these two parameters indicate the
thickness of the downstrokes of the letter ‘H’ (“aitch” in Latin, “en” in Cyrillic, “eta”
in Greek).
• slope: the slope of the font, measured in degrees in the trigonometric sense (and
therefore a negative number in our customary italics). Once again, the standard is
not specific enough: what to do in the case of a font such as the sublime Lanston
Garamont Italic, in which the letters ‘L’, ‘K’, and ‘M’ have slopes equal to 9, 12.4, and
18 degrees, respectively? Is the slope of the lowercase letters more significant for the
“look” of the font, given that these letters are more common than the capitals? These
questions will remain open as long as the CSS standard does not provide more precise instructions for calculating this parameter.
• cap-height and x-height: the height of the uppercase and lowercase letters; for example, the height of the letters ‘H’ and ‘x’.
• ascent and descent: the height of the letters with ascenders (for example, ‘d’) and
the depth of those with descenders (for example, ‘g’).
Finally, font synthesis (a term used in the CSS specification). The term is ill chosen, as the
focus is entirely on the metrics of the font to “synthesize”; thus the procedure involves
replacing the glyphs of the original font with other glyphs, but with the same dimensions. Why this insistence on preserving the same dimensions? The reason proffered in
the standard is progressive rendering. Suppose that our browser is able to download the
11 The aim of Panose-2 [113], an extension of Panose-1, was precisely to fill this void and offer a system of
classification based on measurements that are independent of the script. Although a white paper describing
this system was published as early as 1993, no software seems to support it yet.

(X)HTML, CSS, and Fonts
marvelous fonts of the site that we have just visited. But there are many of them, and
they contain large numbers of glyphs; thus downloading may take a long time. What do
we do when we must render a text but do not yet have the glyphs to use? We render
them with another font, preferably a system font that is readily available. But rendering
an (X)HTML+CSS page also implies global layout, and this layout cannot change when
the correct glyphs become available to replace the temporary ones. Thus, from the beginning, we must place the glyphs so that the replacement of the temporary font with
the downloaded font can be performed entirely within the box of each glyph, without
any repercussions for the arrangement of the page’s visual elements.
Here are the available declarations:
• units-per-em, already seen above, which is indispensable when we use declarations
that refer to the font’s metrics.
• bbox, followed by four numbers: the bounding box, or container, of the font. These
are the coordinates of the lower left point and the upper right point of the smallest
rectangle that can contain every glyph in the font.
• widths, followed by any number of “Unicode coverage” pairs (with the same syntax
as unicode-range) and “set-widths” (whole numbers representing the set-widths of
the glyphs corresponding to the Unicode characters that precede them), separated by
commas. If there are fewer set-widths than characters, the last set-width is repeated
as often as necessary. For example, in the case of the font Le Monde Livre, which is
used for the text that the reader is currently reading:
units-per-em: 1000;
widths: U+002F- 255 510, U+003A-B 255;
which means: the glyph of the character12 U+002F (the slash) has a set-width of 255,
and the glyphs of the characters from U+0030 to U+0039 (the Arabic digits ‘0’ to ‘9’)
all have the same set-width: 510. Similarly, the glyphs U+003A (the colon) and U+003B
(the semicolon) have a set-width of 255.
This technique is not new: it has been part of the PDF format from the beginning. In fact,
it is possible to refrain from including fonts in a PDF file. In that case, the two Multiple
Master fonts provided with Acrobat will be used: Adobe Serif and Adobe Sans. But in order
for these fonts to fit into the “body” of the original font, they require scaling that is performed by Acrobat, using the set-widths of the glyphs of the original font. Fortunately,
the set-widths are not subject to copyright, and one may quite legally include within a
PDF file the set-widths of all the fonts employed.
That is roughly the same method that CSS sought to implement, except that in PDF the
set-widths are in an optimized and compressed binary format, whereas in CSS they appear in plain text and could potentially take up a great deal of space and cause significant
12 And here we run into a glaring inconsistency of this approach: what will happen if we use a font that
contains multiple glyphs for a single Unicode character, such as, for instance, even the humblest Arabic font?

```text
delays in the downloading and rendering of a page.13 We can get around this problem by
only including in the stylesheet the set-widths of the glyphs that are actually used in the
XML/(X)HTML document, but that also means that we cannot separate the stylesheet
from the document. We shall have to see how the industry will implement this type of
approach, which certainly appears very awkward.
Conclusion: is CSS effective?
In the previous two sections, we studied CSS’s approach to font management in web
documents ((X)HTML) and XML documents in general. We have seen that CSS separates two points of view: that of the author of a web page, who wishes to use a certain
number of fonts without worrying too much about technical issues, and that of the “web
technician”, who does her utmost to ensure that the fonts requested by the author will
reach the browser or, as a last resort, be replaced by intelligently chosen fonts.
Is this method effective? When we compare the fine concepts described in the CSS specification with reality, we can see that everything depends, at the end of the day, on the
willingness of browsers to comply with the specifications and that, in the case of fonts,
that is not yet the case. Next we shall see the real possibilities that exist for downloading
fonts. We shall also see that the tools that make downloading possible also manage the
“web technician’s” part and enable the author of a web page to give free rein to his creativity without worrying about such crudely material details as the management of the
CSS font database.
Tools for Downloading Fonts from the Web
In the previous section, we described the CSS declaration src: url("...");, which requests the downloading of a font from the Web. We even furnished a list of font formats
provided in the CSS specification. But what does this declaration actually do?
Well, the situation is not golden. Several factors are responsible: first, and we shall never
say it enough in this book, fonts are usually subject to copyright and cannot be made
available to the public. Thus (a) the format in which the font is downloaded must be an
encrypted and secure format so that extraction of its data will be impossible, and (b) the
file downloaded must serve no purpose other than the rendering of the web page in
question. That is all quite possible, through the use of unpublished font formats (unlike
OpenType, PostScript Type 1, etc.) and by locking the downloaded file to a given URL:
even if the file is recovered and moved to another location, it will be useless.
But the technical difficulties do not stop there. A browser usually resorts to graphical
routines in the operating system to render the contents of its windows. That means that
13 That is why, in the example of a stylesheet with set-widths that we presented above, we “cheated” by
considering an ideographic font. A huge yet wonderful paradox of the Japanese, Chinese, and Korean scripts:
they contain tens of thousands of signs, but these signs are all extremely disciplined and take up exactly the
same space: a square, symbol of balance and harmony. Thus giving the set-widths of the ideographic glyphs
presents no problem; after all, they all have the same set-width (with a single exception: the few dozen halfwidth Japanese kana, a twentieth-century invention whose inclusion in Unicode led to the spilling of a great
deal of ink).
```

Tools for Downloading Fonts from the Web
the fonts used for rendering text also come from the operating system. But here we are
proposing to obtain a file from the Web—a file that only the browser will know how to
decrypt—and use its contents as a font, just like the fonts on the system. That approach
amounts to short-circuiting the operating system. At the same time, the glyphs rendered
must support searches, copying and pasting, etc. And that support presupposes a close
collaboration with the operating system—which is being short-circuited, with all the
risks of conflict that that entails.
And we have not even mentioned the problems of internationalization: how to render
Arabic on a client station that is not configured for the language? If we can download
an Arabic font, should we not also be able to render text with it, even if that assumes
contextual analysis that may be complex? And what about the link between characters
and glyphs? When we select an Arabic word whose glyphs we see and then copy the
selection to the clipboard, is it not reasonable to wish to obtain the Unicode characters
rather than the positions of the glyphs in a given font?
We can tell that the technical problems involved are not minor ones, and that may explain, at least in part, the weakness and the obscurity of the existing tools. At the same
time, these problems emphasize all the more the great accomplishment represented by
the development of a product such as GlyphGate, which we shall see below.
We shall present, in a chronological order, the three tools for downloading fonts that
are currently available: the TrueDoc technology of Bitstream, the WEFT software of Microsoft, and GlyphGate, by em2 Solutions.
TrueDoc, by Bitstream
Bitstream is a large American foundry; its fonts are neither the most magnificent nor
the most extravagant nor yet the most authentic, but they maintain a generally high
level of quality. Bitstream is known for having launched technologies that failed when
confronted with the commercial supremacy of giant multinationals such as Microsoft or
Adobe, the most famous examples being Speedo and TrueDoc, of which the latter is our
focus here. TrueDoc technology [81] is based on the PFR (for ‘Portable Font Resource’)
file format [99]. PFR has the following technical characteristics:
• It is binary, and its architecture is recognizably different from that of TrueType and
PostScript Type 1. In particular, it has its own techniques for hinting, and any font
converted to PFR loses its original hints and is given new ones at the time of rendering,
which, according to Bitstream, enables the rendering to be optimized by creating
hints customized for each platform.
• It can theoretically contain up to 65,536 glyphs, but they are not connected to characters, because there is no indication of the encoding being used. Moreover, these
glyphs have no name, only a position.
• Part of the PFR specification is freely accessible on Bitstream’s web site. But—and
this is hardly surprising—the locking of a font to one or more URLs is not docu-

Figure 10-2: Screenshots from WebFont Wizard.
mented. Furthermore, no information on hinting is provided, other than a technique for the replacement, at a low resolution, of certain curves with straight lines;
this technique is related to the flex of PostScript Type 1 fonts.
Just a few years ago, two products for generating PFR fonts were available on the market:
• Typograph, by HexWeb, a Macintosh software package in two versions—an independent version and a plug-in version for the BBEdit text editor
• WebFont Wizard, by Bitstream, for the Macintosh and Windows
The first of these was triply unsuccessful, since the software is not distributed anymore,
the company HexWeb disappeared from the map and from the Web, and, finally, the
Typograph plug-in is incompatible with the latest versions of BBEdit and is therefore unusable. As for WebFont Wizard, the situation is less severe: the company still exists, and the
product is still usable today; it is simply no longer being distributed. Just in case Bitstream
ever decides to launch it again on the market, here is how it works:

Tools for Downloading Fonts from the Web
• First, one selects (Figure 10-2 [a]) the font to convert, from among the fonts installed
on the system. At the same time, one selects the style (regular, italic, bold, bold italic)
and the “script”. In fact, what is called “script” here is nothing but a subset of the
WGL4 set of glyphs, which was introduced by Windows NT. WGL4 corresponds to
a small part of Unicode that covers the languages of Western Europe (except Maltese), Central Europe, the Baltic states, Eastern Europe, and the Balkans, as well as
Greek (only “monotonic”, thus a poor subset of true Greek (see [169, 166])) and
Turkish. One may select “Western”, “Greek”, “Turkish”, “Baltic languages”, “Central
Europe”, or “Cyrillic”, provided, of course, that the corresponding glyphs are available in the font.
• Next, one selects (Figure 10-2 [b]) the set of glyphs to include in the font: “alphanumeric characters (without accents) and punctuation”, the “complete” set, or a “custom” range. This window also affords us the possibility (Figure 10-2 [c]) of inspecting
the set of glyphs to ensure that we have made the correct choice and of preserving
only those that are needed for the web page.
• Finally (Figure 10-2 [d]), we choose the URL(s) of the web pages with which the font
may be used, and we save the font under a filename with the extension .pfr.
Thus we obtain a PFR file for which the set of glyphs and the authorized URLs are customized. How can we use this font on a web page?
Unfortunately, TrueDoc does not comply with the recommendations of CSS; instead, it
uses an (X)HTML tag to supply the URL of the file containing the font. Here it is:
&lt;link rel="fontdef" src="http://omega.enstb.org/fonts/palatino.pfr"/&gt;
On the other hand, within the web page we use the font’s internal name (not its filename); thus we must have carefully made note of it somewhere. To facilitate that task,
WebFont Wizard produces, at the time of each conversion, an HTML file bearing the font’s
filename and containing a range of useful information: the font’s internal name, the
glyphs that are available, the authorized URLs, the code needed to download the font,
and some JavaScript code that will test the browser and install, in some cases, a plug-in
from Bitstream’s web site.
TrueDoc technology is compatible with the following browsers:
Browser
Mac OS
Windows
Unix
Netscape Navigator 4.x
yes
yes
yes
Netscape Navigator 6, 7
no
no
no
Internet Explorer 4–6
no
yes*
—
iCab
yes
—
—
where the asterisk denotes the need to download a plug-in.

Figure 10-3: WEFT’s font database. In the absence of a product to generate PFR files and with no support from Netscape Navigator beyond version 6 or from Internet Explorer for the Macintosh, the survival of TrueDoc technology is in jeopardy, to say the least. In discussions with employees at Bitstream, the author has noticed a certain bitterness resulting from the abandonment of this technology, especially with regard to Netscape, which supported it very well from the beginning. It is typical that Bitstream has launched a call for help on its web site to Internet citizens who care about beautiful fonts: “Bitstream suggests you contact Microsoft and AOL and encourage them to support dynamic fonts in the new releases of their browsers.” Let us hope that this distress call will be answered! Font Embedding, by Microsoft Microsoft launched the first version of its WEFT (for “Web Embedding Fonts Tools”) software [269] in 1997, at the same time as version 4 of Internet Explorer. This software works only under Windows, and the technology in question is called Font Embedding (a name that—let’s face it—is not very imaginative). The font format used by this technology is Embeddable OpenType (EOT). Once again, this format is undocumented, and Microsoft is not inclined to provide its specifications, even under cover of a nondisclosure agreement. Our contacts at Microsoft have told us that it is an OpenType format compressed with an Agfa technology called Microtype Express that contains only a subset of the glyphs and that is inextricably linked to one or more URLs. Since we cannot say anything more about EOT, let us move on to WEFT. How does it work? First of all, it is important to know that WEFT maintains a database of all the fonts installed on the system. By selecting View>Available Fonts, one obtains a table with a list of all the fonts (Figure 10-3), showing for each one its Windows name, its “family” (in the Windows sense), its font format, an indication of whether it is installed on the system or not, its location on the disk, and, most important of all, the right to include this font in

Tools for Downloading Fonts from the Web
a web page. Thus a font can be Editable or Installable (or downloadable, even for pages
in which the Internet user can write), Previewable (or downloadable, but exclusively for
pages that can only be read), 'No embedding' font, Windows core font (thus downloading
it is unnecessary), or Font may be broken!.
Before writing stylesheets for web pages, one must check, in this database, whether the
fonts that one wishes to use can be downloaded. Next, one writes the CSS stylesheets,
using the declarations font-family, font-style, etc., but not declarations for downloading the fonts, since WEFT will add them to the page.
Next (Figure 10-4 [a]), one has WEFT read one’s pages, using Tools>Add Web Pages. The
software will read them and generate a list of all the requested fonts, specifying whether
they are downloadable and how many characters are required from each: this information will appear in the Fonts to Embed window (Figure 10-4 [b]).
This window is very interesting, as it offers us seven ways, arranged in increasing order,
to select the glyphs to include in a font to be downloaded.
• Per page subsetting: WEFT will analyze each (X)HTML file separately and will
create EOT files for each, which can be used by this file only. This procedure entails
the largest number of EOT files but also the greatest degree of independence of the
various files—the addition of a few glyphs to one file will not force the recompilation
of the full set of web pages on the site.
• Per site subsetting: a global analysis is performed on the entire site. The EOT files
generated will have enough glyphs for all the web pages on the site. The same fonts
will be used for all the pages.
• Family based subsetting: the analysis is global and, in addition, the fonts of the same
family (in the Windows sense) contain the same glyphs. For example, if an upright
font contains the glyphs ‘a’, ‘b’, and ‘c’ and the italic version of the same font contains
only a ‘c’ and a ‘d’, the EOT fonts generated will each contain the same set of glyphs:
‘a’, ‘b’, ‘c’, and ‘d’. The reason is as follows: Suppose that on your web page a JavaScript
script changes the style of your font from upright to italic, or from light to bold. It
would be a shame if some glyphs were missing simply because the JavaScript script
was not activated when the EOT files were produced. Thus all the glyphs are supplied
in all the styles in use. This is the default choice.
• Union subsetting: the same principle operates here as with selection by family, but
here it extends beyond font families. WEFT will make note of all the characters used
on all the pages and will generate EOT fonts, each of which contains enough glyphs
for all the characters. This method even covers pages on which JavaScript scripts may
change the fonts that are used.
• Raw subsetting: this approach goes even beyond selection by union because here
even the text that is not part of the visible contents of the (X)HTML elements is
included—XML comments, the text that appears within scripts, tags, etc. The fact

Figure 10-4: Steps for creating EOT fonts in WEFT.

Tools for Downloading Fonts from the Web
that the document is an (X)HTML page is disregarded; the file in question is considered to be a text file, and all the glyphs whose characters are found therein are
incorporated.
• Language subsetting: the glyphs of a Unicode block are included in the EOT files.
This choice is discouraged because it is possible to include only a single block, and
rare are the pages that use only one: a mere space character on the page makes the
ASCII block necessary; an em dash or a proper quotation mark will force us to use
the block of general punctuation; an accented letter, and the Latin Extended block is
required. One would not expect it, but the sentence “—Darling, don’t be naïve! said
she” requires no fewer than three Unicode blocks!
• No subsetting: the inclusion of the entire font—not recommended for large fonts,
especially ideographic ones.
Did the reader not find what she wanted among these methods for selecting glyphs? She
may also select her glyphs by hand. Clicking on the Subset button brings up a dialog
window (Figure 10-4 [c]) showing all the glyphs in the font, arranged by Unicode table,
and the glyphs that are not used on the page are masked in gray. Merely clicking on a
glyph will cause it to be included in the font; one more click will deselect it. The full set
of glyphs selected is displayed at the bottom. One can even save a selection of glyphs to
a file and use it later for another font.
Now that we have finished selecting the glyphs to be included, we shall move on to the
creation of the EOT fonts (Figure 10-4 (d)). In the window Create Font Objects, we
simply indicate the location where the generated fonts are to be stored and the URLs
under which the fonts may be used. The location where the fonts are to be stored is used
both by the WEFT software (for saving the fonts) and by the CSS code generated by this
software: it is the argument to the src: url(...) declaration. We may use files on the
disk (file) or those accessible through the http, https, and ftp protocols.
As for the URLs under which a font may be used, we may supply any number at all, and
the authorized protocols are file (a file on the disk), http (an [X]HTML page), https (an
[X]HTML page with a secure connection), ftp (file transfer), mhtml (an [X]HTML page
included in an email message).
The next two windows (Figures 10-4 (e), (f)) complete the process by asking us to update
the pages and to give confirmation.
This procedure was conceived by Microsoft for graphic artists and other authors of web
pages who wanted to write (X)HTML/CSS code first and then have the fonts generated
semi-automatically from their code. Those who feel more at ease with the technical nature of EOT font generation may do it directly, without going through an analysis of web
pages. Selecting Tools>Expert Create Fonts will do the job. The window that appears
(Figure 10-5, left) offers a direct choice of fonts to generate, the possibility of choosing
glyphs to include (a manual choice, with the option of saving and reusing a set of glyphs),
the authorized URLs, and a location for the generated fonts. In short, all the functionality outlined above—except, of course, the intelligent selection of glyphs to include from

Figure 10-5: The window for generating EOT fonts in WEFT. an analysis of the characters used on web pages, since there are no web pages to analyze this time. And since there are no web pages yet, the CSS declarations are written in a window (Figure 10-5, right) from which one can copy and paste them into (X)HTML or CSS files. In conclusion, WEFT seems, at first blush, to be the solution for downloading fonts from the Web: it is efficient, Unicode-compatible, and completely free. It would indeed be the ideal solution if all of humanity used Windows and surfed the Web with Internet Explorer. But that is (un)fortunately not so, and with the exception of Internet Explorer under Windows, no browser is compatible with EOT fonts (Internet Explorer under Macintosh was compatible at one time, but it no longer is). GlyphGate, by em2 Solutions One thing that we have noticed about the two tools for downloading fonts that were described above: however wonderful the technologies are, their success depends on their compatibility with browsers, and neither of the two technologies has managed to prevail in this area. We can amuse ourselves by creating PFR or EOT fonts and including them in our web pages, but we have no guarantee that the Internet user who visits those pages will be using a compatible browser. And we all know how annoying it is to read on a web page: “This page can be displayed only with X version Y.” But is there a way to know which browser the cybernaut who connects to our server is using? We all know that the Web is anonymous: when we connect to a server, the server knows very little about our identity. That is part of the Web’s code of ethics. But, at the same time, this principle has its limits. It is quite helpful, for example, for the server to know the type of browser that we are using, so that it can improve the configuration of the pages that it sends us. That is indeed done, using information transmitted through the HTTP protocol [152]: the User-Agent declaration, which is an integral part of every HTTP request that the client sends to the server.

Tools for Downloading Fonts from the Web
But there turns out to be a problem of diversity. First of all, each browser is free to
identify itself with a string of its choice; no standards prevail. Next, there are oodles of
browsers, running on many platforms, and new versions of these browsers come out every day. Thus it is a herculean task to preserve a record of every version of every browser
for every platform. And we would also need to prepare for each of these, according to
its features, a different version of the web page, with or without downloaded fonts, and
with the appropriate syntax.
That is exactly the idea that occurred to the company em2 Solutions—which, incidentally, was Microsoft’s contractor for the development of WEFT. Rather than focusing on
having the author of the web pages generate downloadable fonts, em2 Solutions tackles the web server itself and furnishes a web server plug-in by the name of GlyphGate
(formerly called Fairy) [130]. This plug-in is compatible with Apache, servers compatible
with the Netscape API, and Microsoft IIS.
The principle behind its operation is similar to that of WEFT: one prepares web pages by
indicating the desired fonts, and GlyphGate does the rest. In fact, it is not even necessary
to generate the fonts; GlyphGate does so, in real time, and according to the nature of the
client that connects to the server. em2 Solutions does not claim to cover all browsers,
but actually it does. Indeed, it covers even the oldest ones, by sending GIF images of the
words in the document, if nothing else can be done.
But GlyphGate goes much further:
• If the web page requires contextual analysis—for example, if it contains text in
Arabic—and the browser cannot handle this functionality, GlyphGate will take care
of it and render the Arabic text correctly.
• If the font being used is an OpenType font with advanced typographic features, then
GlyphGate will offer special CSS declarations for enabling or disabling any of these
properties in any part of the document. For instance, one can enable ligatures, oldstyle figures, stylistic variants, etc., on the fly.
• Unbelievable but true, GlyphGate even offers to perform kerning, something that
browsers ordinarily are not equipped to do. How does it perform kerning? Suppose
that the browser must render the pair of glyphs ‘AT’ and that it is necessary to move
the ‘T’ closer to the ‘A’. GlyphGate will generate a new font in which the glyph ‘A’
will have a smaller set-width, so that when ‘AT’ is rendered one gets the impression
that kerning has occurred. Farfetched, yes, but darned effective!
• A key use of GlyphGate is to support less common languages on the Internet. This
is done through Web fonts in common browsers on personal computers, by graphics on less common platforms and browsers, and through romanization on text only
browsers. There is as such support for any browser on any platform that support at
least HTML 2.0, even on platforms without a graphical user interface.
• Last but not least, GlyphGate offers a development kit containing modules for the
rearrangement, replacement, and repositioning of glyphs. One can thus construct

Figure 10-6: Extract from the browser’s window: a list of fonts available on the server that was generated by GlyphGate. one’s own rules for contextual analysis, replacement of certain strings with glyphs for ligatures, placement of diacritical marks, etc. Now let us see how to use GlyphGate. Suppose that GlyphGate has been installed on the server. The fonts to be used have to be installed somewhere on the server. Under http://our_web_site:8024/gg-fonts, GlyphGate shows us a list of all the fonts available for web pages (Figure 10-6). By clicking on a font, we gain access to a series of pages displaying all the font’s glyphs, including the glyphs generated by GlyphGate, such as, for example, the accented letters that do not exist in the original font but whose components (the base letter and the accent) are present. These glyphs are arranged by Unicode table (Figure 10-7), and only the tables that contain at least one glyph are displayed. Note that these are not imported images but true Unicode characters that we can copy and paste, print out, or search for if the operating system allows. What comes close to being a miracle is that these characters are represented by glyphs in the font in question, though that font is not installed on the client system.

Tools for Downloading Fonts from the Web Figure 10-7: Extract from the browser’s window: glyphs from the font Palatino Linotype in the Unicode table Latin Extended-1, displayed by GlyphGate.

Once we have checked that the fonts that we want are correctly recognized and displayed
by GlyphGate, we may go ahead and use them in our pages. No surprise: we can use
standard CSS declarations. From this point on, GlyphGate takes charge of rendering.
And it works!
Some browsers may take advantage of a plug-in called FontEnabler,14 which takes just a
minute to download and even less time to install. One must simply make sure that the
browser detected by the plug-in’s installation program is indeed the browser that one is
using.
To conclude this section, here are two CSS declarations defined by GlyphGate:
• text-otl is used to enable OpenType’s advanced typographic features (see Appendix D.9). It is followed by any number of labels for such properties. These labels
are always strings of four characters. For example, if in an OpenType font we define
a property onum that replaces the ordinary digits with old-style digits and a property
stct that replaces the strings ‘st’ and ‘ct’ with the ligatures ‘s’ and ‘c’, then by writing
.oldstyle { text-otl: onum,stct; }
in a stylesheet, and
&lt;span class="oldstyle" lang="en"&gt;Acts of Justice of 1770.&lt;/span&gt;
in the document, we do indeed obtain text with old-style figures and ligatures: “Acs
of Jusice of 1770”. It is also important to specify the language (with the lang attribute), since the advanced typographic features of OpenType are always connected
to a language. We shall see that in detail when we discuss the editing and creation of
OpenType fonts (see Chapter 14).
• glyphgate enables or disables analysis by GlyphGate. It can take three values: skip
(GlyphGate completely disregards this part of the document), nofonts (partial processing: CSS and contextual analysis are performed, and only the fonts are not downloaded), process (regular processing, which is the default value).
Thus GlyphGate is indeed the miracle solution, for those who have control over their
web server. Let us hope that the use of this system will become more and more common,
as it will improve the “look” of the Web and will democratize the use of even rare nonLatin languages.
14 Internet Explorer will default to using web fonts without the plug-in. Browsers without native Web font
support, such as Safari and Mozilla, will default to using graphics for text in prominent places on a Web page.
By default, Web pages will thus “look right” in browsers without the use of a plug-in. The administrator of a
Web site may chose to offer the FontEnabler plug-in to browser users in order to enable the use of Web pages
that can be searched and printed more easily. This can be highly customized; for example, you can choose
the exact circumstances under which to make the plug-in available). In that case, it is up to the user to either
use the plug-in, with its benefits, or settle for the default behavior (which is probably good enough). For a
page with Arabic and Brahmi text, the use of the plug-in would be recommended, although still not required.
For example, you would be able to render Urdu text correctly in Mozilla without using either the plug-in or
graphics: GlyphGate would produce Arabic text with presentation forms to ensure that the text was legible,
albeit not with the intended font.

The SVG Format
The SVG Format
SVG is the acronym of Scalable Vector Graphics, a name that is quite ill chosen, being as
it is redundant. Specifically, scalable and vector mean exactly the same thing: that the
images can be scaled because they are mathematically abstract objects such as straight
lines, curves, circles, rectangles, polygons, etc.
The notion of a “vector image” has existed for a long time in the world of industrial design; it is thanks to software such as Adobe Illustrator and Corel Draw that “vector design”
is, and has been for a good decade, within the reach of the public.
Apart from the redundancy of its name, SVG holds nothing but pleasant surprises in
store for us. The most important of these: it is a W3C standard based entirely on XML.
That is an enormous advantage:
• First, because SVG’s vector images become human-readable and human-editable
documents. There are no more secrets, no more mysterious proprietary file formats,
no more “black boxes”. Which also means that an SVG image placed on the Web
can be indexed like any web page.
• Next, because all XML tools and technologies can also process SVG vector images.
For instance, if one wishes to generate or transform SVG images, there is no more
need to reinvent the wheel and write tools to do the job; tools already exist, and one
need only tell them what to do.
• Images become hierarchical objects; in particular, they can be composed of several
parts and/or layers, each of which is an SVG image in itself. Moreover, SVG manages
interactions and certain dynamic operations, and the reader can thus interact with
the different parts of the image.
• Finally, an SVG image and its different parts can be resources accessible on the Web
through the use of semantic metadata (web semantics) [107, 331]: each portion of
the image can carry metadata that is associated with one or more ontologies. For example, if one is searching for resources indexed by the concepts “seed” and “corn” in
an “Agriculture” ontology, one may find a part of the SVG image showing different
types of seeds, one of which shows a seed of corn, because the creator of the image
took the trouble to index each part of the image separately, through the use of the
correct ontology.
Before tackling the use of fonts under SVG and its impact on the Web, a brief introduction to the concepts and terminology of XML is in order. (The reader may also profitably
consult the works [300, 252].)
Fundamental Concepts of XML
In the exact sciences, and mathematics in particular, there are two possible pedagogical
approaches: the one that goes from the general to the specific and from the abstract to

```text
the concrete—which is the “Bourbakist” approach, named after the prestigious French
association of mathematicians—and the one that goes from the specific to the general,
from a set of concrete cases to an abstraction—which is the “American” approach. To
discuss XML, we shall take a Bourbakist approach, which may not actually be one, since
from the beginning of this chapter we have discussed the Web—and HTML, and more
specifically XHTML, is nothing but a special case of XML. Is XML then an extended
XHTML? A generalized XHTML?
It is all a matter of perspective. Some would say that XML is like XHTML, only that we
choose the names of the tags ourselves. There is a kernel of truth in that position, but
XML goes much further than that. Let us therefore wipe the slate clean and start again
from the beginning.
Our starting point is the document. Our goal is to give it a structure. What do we mean
by that? Well, that means that we are going to subdivide it into parts, each of which will
have a meaning, or at least a “description”. These parts will be embedded; in other words,
each of them will be included in one, and only one, immediately larger part, and so forth,
until we obtain the entire document, which contains all of the parts. We can represent
that with a “shoebox” diagram like the one shown below:
book
chapter
chapter
chapter
section
section
section
section
where we have called the parts “book”, “chapter”, and “section” to give an example of a
structured document that has been known for millennia: the book. We acknowledge the
customary form of embedding: the book contains chapters, which contain sections. But
these objects, unlike the unorganized elements of set theory, also have an order, which is
the order in which the book is read, and it is the logical order of our document. We can
therefore revise the figure shown above by adding the order of the subparts of each part:
book
chapter 1
chapter 2
chapter 3
section 1
section 2
section 1
section 2
And here is the first trick: using the figure above, we can draw a diagram in which the
nodes are the parts of the document, the edges represent the relationships for their incorporation, and the parts are arranged from left to right in the order of their occurrence,
thus eliminating the need to number them:15
15 The sentence, “It was a dark and stormy night; the rain fell in torrents—except at occasional intervals,
when it was checked by a violent gust of wind which swept up the streets (for it is in London that our scene
lies), rattling along the house-tops, and fiercely agitating the scanty flame of the lamps that struggled against
the darkness”, from Bulwer-Lytton’s Paul Clifford (1830), is widely held to be the worst opening sentence in any
English novel. The author would like to thank Scott Horne for suggesting it.
```

```text
The SVG Format
book
chapter
section
chapter
section
chapter
section
section
It was a dark and stormy night...
Surprising though this may be, the approach leads to a very important mathematical
concept, that of the tree. The parts of an XML document, symbolised by boxes in the
figure shown above, are called elements. The terminology used is in part botanical and
in part genealogical. Let us deal with the botanical aspect first: the element at the top
of the tree is called the tree’s “root”, the part of the tree that appears beneath a given
element is called a “branch”, and the elements that appear at the end and that have no
subelements are called “leaves”. Now for the genealogical aspect: an element has “ancestors” and “descendants”, “parents”, “children”, and “siblings”.
Here, then, is what an XML structure really is: a breakdown of a document into parts
that are embedded so as to form a tree. Having thus defined the XML structure, we can
immediately see its limitations: in the real world, not everything can be structured in
this manner. Consider a document that we arrange first according to the languages used
in it and then according to the styles (roman, italic, etc.); there is no reason that the
elements obtained in the first structure will be embeddable within those of the second or
vice versa. Thus structuring a document in tree form is a compromise—but an attractive
compromise, as it allows us to profit from existing techniques and tools for processing
trees.
And now our excursion through the world of concepts is complete: it is time to come
back down to earth and see how we represent an XML document in the form of computer data. This is where we return to tags: since an element is part of a document, we
insert an opening tag at its beginning and an ending tag at its end:
&lt;book&gt;
&lt;chapter&gt;
&lt;section&gt;It was a dark and stormy night ...&lt;/section&gt;
&lt;section&gt;...&lt;/section&gt;
&lt;/chapter&gt;
&lt;chapter&gt;
&lt;section&gt;...&lt;/section&gt;
&lt;section&gt;...&lt;/section&gt;
&lt;/chapter&gt;
&lt;/book&gt;
And if we have a page with no textual content, we will write an empty tag, with a slash at
the end. For example: &lt;img/&gt;.
Another fundamental notion: attributes. Suppose that we would like to attach certain
information to certain elements without incorporating this information into the text;
for example, the identification number of a section, the language of a paragraph, a short
```

```text
text describing an image for the benefit of visually impaired web users. This sort of information is placed within attributes, which are key–value pairs that are placed inside
opening tags or empty tags in the following manner:
&lt;p xml:lang="en-us" id="p137"&gt;It was a dark and stormy night ...
In this example, we say that the paragraph tagged by &lt;p&gt; is identified by the string p137,
and that it is written in American English.
We may have as many attributes as we wish, and their order is not significant. We must be
careful, however, not to include any tags in the values of the attributes; they are supposed
to be strings with no tags in them.
Another interesting notion: entities. An entity is a block of text or a branch of a document
to which one has assigned a name. In the document, one uses the entity reference, which
is the name of the entity, preceded by an ampersand and followed by a semicolon. For
example: &foo;. We ask the software processing our XML to replace all entity references
with the corresponding text or branches at the start of processing. Thus there is nothing
profound about the notion of an entity: it is just a “shortcut” that masks text or even an
entire branch of a document—a branch, incidentally, that could even be contained in
another file.
One last important notion in this quick overview of XML: namespaces. Consider the
following problem: how to associate an element’s tag or an attribute with precise semantics? Example: when we write &lt;img/&gt;, how can we indicate that it is indeed the img tag
of the XHTML standard of the W3C and that it must be interpreted as such, not as an
HTML tag or as any other sort of tag unknown to anyone but the person who wrote it?
Answer: by specifying that this tag belongs to the XHTML namespace. This namespace
is uniquely represented by the string:
http://www.w3.org/1999/xhtml
The technique is as follows: We declare a namespace in a branch of the XML document
(a branch that may very well be the entire document), and the elements and attributes
of this branch may, in turn, belong to this namespace or not. Here is what to write, for
example, to declare the XHTML namespace in a &lt;section&gt; branch of the document:
&lt;section xmlns:xhtml="http://www.w3.org/1999/xhtml"&gt;
&lt;xhtml:div&gt;
&lt;xhtml:p&gt;
Blah-blah.... &lt;foo/&gt;...
&lt;/xhtml:p&gt;
&lt;/xhtml:div&gt;
&lt;/section&gt;
The string xhtml is the alias associated with the namespace. In this example, only the tags
preceded by the alias belong to the namespace in question. Thus div and p are indeed
```

```text
The SVG Format
the XHTML tags that we know and love; however, foo does not belong to this namespace
(simply because no foo tag appears in the XHTML standard). It is also possible to have
a namespace without an alias; in this case, we say that we declare a default namespace:
&lt;body xmlns="http://www.w3.org/1999/xhtml"&gt;
&lt;div&gt;
... nothing but XHTML code, unless otherwise specified ...
&lt;/div&gt;
&lt;/body&gt;
Here all the tags that are not preceded by an alias belong to this namespace by default.
Note that the tag that declares the default namespace (the body tag, in the example
above) also belongs to this namespace, unless, of course, it is preceded by an explicit alias.
The namespace (and the corresponding alias, if any) is defined only in the branch of the
element that contains its definition. The choice of string for the alias is of no importance;
however, it is essential to write the string for the namespace itself correctly: with the
slightest error, it is no longer the same namespace!
The reader may be surprised by the resemblance of this string to a URL. It did not happen
by chance. Suppose that Mr. George Everyman has defined a set of tags that are very
useful for documents on the subject of oyster-farming. Which string will he choose as
the namespace for his tags in order to ensure that no one else will adopt the same name?
Choosing George-Everyman would be the height of self-centeredness; in any event, there
are plenty of other “George Everymans” in the world. A more eccentric choice, along
the lines of GeoEveryman-oyster-PodunkbytheSea, might have better chances of being
unique, but could we ever be sure? The W3C’s idea is much more natural. On the Web,
there is a syntax for strings that identify resources—a well-defined syntax, known around
the world and, in addition, many web users have already taken one of its strings: as the
reader has no doubt guessed, this syntax is the URL [74]. For example, the URL:
http://omega.enstb.org
is that of the author’s machine. If each person uses his own URLs or those with which
he is associated in one way or another, there will be no risk of duplicates. In addition,
by following the URL, the user of the namespace could possibly find information on the
set of tags in question. But the author is not required to publish such information at
the URL.
Namespaces exist for all major applications of XML: XHTML, XSLT, XSL-FO, XForms,
XLink, XOL, XQL, MathML, RDF, SMIL, XML Schema, VoiceML, WML, MML, etc. What
is interesting is that one can, thanks to these namespaces, mix several kinds of tags in
the same document, with no risk of conflict or confusion. Thus, right in the middle
of an XHTML document, one can insert an SVG figure without surprising anyone: it
is sufficient to specify the namespace of each tag used. The tools that process the XML
document will then know, unambiguously, whether or not they are able to process the
standards used therein.
```

And what about SVG?
It is said that a picture is worth a thousand words. Well, to describe the picture below:
only four tags and 15 attributes were needed:
&lt;svg xmlns="http://www.w3.org/2000/svg" width="233.503" height="113"
viewBox="0 0 233.503 113" overflow="visible"
enable-background="new 0 0 233.503 113">
&lt;path fill="#CCCCCC" stroke="#000000"
d="M76.5,94.5h-v-h76V94.5z"/>
&lt;path fill="#E6E6E6" stroke="#000000"
d="M188.5,56.5c0,30.928-.311,56-,56s--.072
--s27.311-,61-S188.5,25.572,188.5,56.5z"/>
&lt;path fill="#999999" stroke="#000000"
d="M186.265,12.596L200.53,41.5l31.898,4.635l-.082,
22.499l5.449,31.77l-.531-l-.53,15l5.449
-.77l-.083-.499l31.898-.635L186.265,12.596z"/>
&lt;/svg&gt;
The four elements and their attributes are:
• An svg element, which contains all the other elements and is labeled with the SVG
namespace (in the example above, this is the default namespace). Through the attributes of this element, the overall size of the image is also determined.
• Three path elements, which correspond to closed contours: a square, a circle, and
a star, each filled in with a different shade of gray. The fill and stroke attributes
indicate the color to be used for filling and drawing the contours, respectively. The
d attribute takes rather cryptic values: but don’t panic; it is just an “optimized” way
to represent sequences of straight lines and Bézier curves in order to form contours.
We have written the word “optimized” in quotation marks because the optimization
is done more for the sake of the machine than for the sake of the human reader. In
any event, there is nothing mysterious about it; it consists merely of the coordinates
of a path to draw.
The reader is invited to compare the code above with that of the same image under
Illustrator or Corel Draw: no vector format is so simple and logical. Each contour has

```text
The SVG Format
its own path element, and the order of these elements is important, since it is the order
in which the figure will be drawn. Proof: the images slightly overlap, and each younger
sibling consistently encroaches upon his elders.
On the other hand, SVG allows the optimization of code through macros: the first part
of an SVG document is for definitions. A definition is a defs element that contains shapes
or colors or blocks of text that are used multiple times in a document. By defining them
within defs, we can later use them by merely referring to them with a special referencing
element. Fonts are also placed within defs, since, after all, they are global data that are
used throughout the document.
We shall not describe SVG in any more detail. The curious reader will find more information in the book of the same title published by O’Reilly [129] and in an increasing
number of other books on this subject, including, of course, the specifications of this
standard [134].
In the following section, we shall concern ourselves with font management under SVG.
We shall first see how to select a font when writing text under SVG, and then how to
define a font in order to use it in the same document or in other documents. What is
interesting is the fact that SVG defines XML elements to describe the glyphs and all the
other metric properties that make up a font: thus it is in fact a font format—not a binary
one like OpenType or PostScript Type 1, but one written in a human-readable format
and, what is more, in XML. The result is vaguely reminiscent of the TTX fonts (see §D.1),
but here we are not rewriting OpenType fonts in XML but rather describing them in
an original way; and, unlike TTX (which is the personal creation of an individual), this
format is an integral part of SVG, which is a W3C standard.
Font Selection under SVG
In XHTML and in XML documents in general, each element has its own attributes; some
attributes may be shared, but that is the exception rather than the rule. In the case of
SVG, the situation is quite different: so as not to torture the writer of SVG code with the
eternal question “does element X take attribute Y or not?”, the designers of SVG opted for
complete libertinism: any element can be combined with any attribute. These attributes
are called properties. What happens if a property has no meaning for a given element?
If, for example, we define the size of a font when we are inside an element that draws
a circle, and thus has no font? Well, then, the property is ignored—with no grumbling
from the viewing software about the fact that “such-and-such has no meaning!” But if
the property in question has no meaning for the element itself, it may perhaps have a
meaning for some of the element’s descendants, and, indeed, most properties are automatically inherited by the descendants.
What is attractive about properties, at least from the pedagogical point of view, is the
fact that one can describe elements and properties separately. The user will combine the
elements and properties that strike her as being compatible, and the viewing software
will decide whether the combinations in question are meaningful or not; in the worst
case, they will be ignored, as they are expected to be, since software of the kind must be
tolerant, as web browsers are.
```

```text
The element that makes it possible to include text in an SVG image is text. This element
can contain text directly or tref elements (which are links to blocks of text defined in
advance) or tspan elements (which, like the span elements of XHTML, have no meaning
in their own right but act as bearers of properties) or even textpath elements, which are
blocks of text set along a path.
The properties that manage the choice of font are the following: font-family, fontstyle, font-variant, font-weight, font-stretch, font-size, font-size-adjust, font.
The reader who has read the section on CSS will have noticed that these are the same
names as those of the CSS font-selection declarations. Not for nothing is that so: indeed,
the SVG specification defers to CSS for an explanation of these properties and a description of the values that they can have. Here the CSS declarations, which, under XHTML,
should be described in a stylesheet or in the value of a class attribute, become true
attributes. Here is an example:
&lt;svg xmlns="http://www.w3.org/2000/svg"
width="233.503" height="113" viewBox="0 0 233.503 113">
&lt;text x="100" y="50" font-family="Historical-EnglishTextura"&gt;
&lt;tspan fill="black" font-size="24pt"&gt;Hilfe!&lt;/tspan&gt;
&lt;/text&gt;
&lt;/svg&gt;
which produces:
In this example, we see the font-family property as an attribute of the text tag, and the
font-size property as an attribute of tspan.
Are all the properties that manage fonts merely CSS declarations in disguise? No, there is
an exception that proves the rule. It is kerning: an attribute, absent from CSS, that takes
the values auto, inherit (its default value), or a length. The effect of this property is to
enable (with the auto value) the kerning of glyphs as defined in the font. The code:
&lt;svg xmlns="http://www.w3.org/2000/svg"
width="233.503" height="113" viewBox="0 0 233.503 113"
overflow="visible" enable-background="new 0 0 233.503 113"
xml:space="preserve" font-family="Times" font-size="24pt">
&lt;text x="100" y="50" kerning="0pt"&gt;AVATAR&lt;/text&gt;
&lt;text x="100" y="30" kerning="auto"&gt;AVATAR&lt;/text&gt;
&lt;/svg&gt;
produces the following image:
```

```text
The SVG Format
AVATAR
AVATAR
Why would we want to disable kerning? No reason comes to mind;16 but the property
does exist, and it already works in the latest Adobe viewer.
Alternate Glyphs
The previous section did not introduce any new concepts, since everything was drawn
straight from the CSS specification, with the CSS declarations becoming SVG properties.
Here we shall address a new concept: that of alternate glyphs. This concept shatters the
barriers between the textual content of a document and its fonts. Indeed, it affords us the
possibility of selecting an arbitrary glyph in any font and inserting it into our document.
And if this font, or this glyph, is not available, we can act as if nothing were wrong and
display the corresponding characters with their default representative glyphs. For example, suppose that we wish to display an ‘fi’ ligature and that we know that this glyph exists
in the active font, with the identifier “g-f_i”. We shall write:
&lt;altGlyph xlink:href="#g-f_i" dx="238"&gt;fi&lt;/altGlyph&gt;
In this case, if the glyph exists, it will be set, and the current location will be moved ahead
by 238 units.17 If, however, the glyph does not exist, the contents of altGlyph—in this
case the string ‘fi’ with no ligature—will be set.
The number sign in the value of the xlink:href attribute shows that the string is in fact
a URL. If this glyph, with the same identifier, were contained in an SVG font, itself contained in an XML document with the URL:
http://omega.enstb.org/fontes/svg/omsela.svg
then the element altGlyph would be written:
&lt;altGlyph
xlink:href="http://omega.enstb.org/fontes/svg/omsela.svg#g-f_i"
dx="238">fi&lt;/altGlyph&gt;
16 There is, in fact, a reason, but it seems quite unlikely to the author that that reason has ever occurred to
the inventors of SVG: one traditionally does not kern letters that represent variables in mathematical formulae.
17 These are SVG’s current units of length, a concept borrowed from the PostScript language, where there
is a basic unit of length—1/72 of an inch—but where the current transformation matrix can alter the size of the
units at any time.
```

```text
Which means, perhaps surprisingly, that we can use glyphs whose descriptions are found
anywhere on the Web. Unlike the methods for downloading fonts that we saw above,
here it is the glyph in question, and only that glyph, that will be obtained from the
Web. And if it cannot be obtained, the contents of the altGlyph element will be used
for display.
The dx attribute is used to indicate the offset of the current location once the glyph has
been typeset: it keeps the rendering engine from having to search for this information
in the font.
One may combine several alternate glyphs in a sequence of glyphs. To do so, one uses
a definition of alternate glyphs. Like all SVG definitions, this one is placed in the &lt;def&gt;
... &lt;/def&gt; section of the SVG document. To indicate the glyphs that will make up the
desired sequence, we use another element, named glyphRef. This element is a variant
of altGlyph: it takes the same attributes and has the same role, i.e., to be a link between
a glyph named glyph in an SVG font; the difference between altGlyph and glyphRef is
that the latter does not supply a string of Unicode characters for the case in which the
glyph in question is not available. For example, by writing in the definitions area:
&lt;altGlyphDef id="TeX"&gt;
&lt;glyphRef xlink:href="#g-T"/&gt;
&lt;glyphRef xlink:href="#g-E" dx="-" dy="100"/&gt;
&lt;glyphRef xlink:href="#g-X" dx="-" dy="-"/&gt;
&lt;/altGlyphDef&gt;
we should then be able to write the following within the body of the document:
&lt;altGlyph xlink:href="#TeX"&gt;TeX&lt;/altGlyph&gt;
to obtain either the “TEX” logo or the string “TeX”. Note that when this book was being
prepared, and also under Adobe SVGViewer version 3, altGlyphDef could not yet contain
more than one glyphRef, and the relative displacement attributes dx and dy were not yet
recognized.18
We can go even further. Suppose that the string of glyphs that we wish to obtain can
be represented in several ways, depending on the availability of one or another glyph.
Suppose further that a company called “FOO” has placed the SVG font containing the
‘F’ and ‘O’ glyphs of its logo on its company web site, http://www.foo.com/logo.svg.
The first option would be to download these glyphs. In case the site is ever unavailable,
the company has provided a second site: http://foo.free.fr/just-in-case/logo.svg.
And if there is no connection to the Web, then the glyphs can be taken from an SVG font
included in the document. What should be done so that the SVG reader will choose the
best solution according to the available glyphs?
18 It is unfortunate to observe that, unlike the situation with web browsers, in which the fierce competition
between Netscape and Explorer forces the two companies to continue to improve their products, the near
monopoly that Adobe has on SVG products results in a lack of verification of the compatibility of SVGViewer
with the SVG standard and no guarantee that this compatibility will ever be achieved.
```

```text
The SVG Format
For this purpose, there is the element altGlyphItem. This element, placed within an
altGlyphDef, informs the reader that its contents are only one possible choice among
others. The reader checks its feasibility and, if it fails, moves on to the following option.
And, of course, if all the choices of this kind fail, it may always fall back on the string in
altGlyph, which does not refer to any glyph and therefore has no reason to fail. Here is
an example of the use of altGlyphItem:
&lt;altGlyphDef id="FOO-logo"&gt;
&lt;altGlyphItem&gt;
&lt;glyphref xlink:href="http://foo.com/logo.svg#g-T"/&gt;
&lt;glyphref xlink:href="http://foo.com/logo.svg#g-"/&gt;
&lt;glyphref xlink:href="http://foo.com/logo.svg#g-T"/&gt;
&lt;glyphref xlink:href="http://foo.com/logo.svg#g-"/&gt;
&lt;/altGlyphItem&gt;
&lt;altGlyphItem&gt;
&lt;glyphref xlink:href="http://foo.org/just-in-case/logo.svg#g-T"/&gt;
&lt;glyphref xlink:href="http://foo.org/just-in-case/logo.svg#g-O"/&gt;
...
&lt;/altGlyphItem&gt;
&lt;altGlyphItem&gt;
&lt;glyphref xlink:href="#g-T"/&gt;
&lt;glyphref xlink:href="#g-O"/&gt;
...
&lt;/altGlyphItem&gt;
&lt;/altGlyphDef&gt;
Thus we see that, since the fonts being used are SVG fonts, we can directly obtain the
glyphs without the slightest hesitation—even if they are kept at the very depths of the
Web—and use them in the document. And if, for whatever reason, these glyphs are inaccessible, we can always fall back on a string represented by their default glyphs.
The standard also gives access to fonts other than SVG fonts but leaves the details of implementing this access to the developers. For instance, a glyphRef attribute is provided,
both for the altGlyph element and for the glyphRef element. This attribute takes as its
value “the glyph’s identifier, whose format depends on the font format”. In other words,
the SVG standard washes its hands of the details: let others struggle to define a syntax
for gaining access to a given glyph in an OpenType or PostScript Type 1 font! And how
can we begin to discuss implementation if we do not even have a syntax? In this area,
without a doubt, the future holds surprises in store.
SVG Fonts
We have already said, in the previous section, that the SVG standard allows for the complete description of a font within an SVG document, so as to make totally independent
documents possible. What a pleasant surprise, when on the Web we are always obliged
to download fonts—in formats locked three times over so as not to infringe copyright!
```

```text
But what about copyright, exactly? An SVG font, like everything else prepared in SVG, is
written in plain text, with no encryption whatsoever. This is a veritable revolution, on a
par with that of October: free distribution of fonts to the proletarians of the world! And
how are the foundries reacting?
Well, they are not reacting at all. The W3C is encouraging developers not to write tools
for converting SVG fonts to a standard font format. The idea—and this idea is explicitly
stated in the SVG specification—is that the graphic artist who receives an SVG document
with the font embedded within it should only be able to view the document: to edit it, she
must first purchase the corresponding font. Thus we are returning to the classic model
of licenses for the use of fonts.
What is actually happening? We do not know yet; it is still too early to say. In any event,
today there are at least two tools for converting TrueType fonts to SVG: FontForge and
batik-ttf2svg (a tool in the Batik distribution [329], written in Java), but neither of them
reads SVG fonts in order to convert them to another format.
But let us return to the description of SVG fonts. An SVG font is completely contained
within a font element. This element applies to the entire SVG document and must therefore be placed among the document’s definitions. What usually appears in a font?
A preamble with general information, a certain number of glyphs, and a certain number of instructions about the behavior of the glyphs relative to each other: ligatures and
kerning pairs. The same is true here: font contains, first of all, a subelement font-face,
which contairs the global information for the font. Most of this information is provided
in the form of attributes and is the spitting image of the CSS declarations.
Next comes something new: an element named missing-glyph, which contains the description of the “missing glyph”, i.e., the glyph that is displayed in the place of another
that cannot be found. It is interesting to note that missing-glyph is mandatory and comes
before all the other glyphs.
Next follow, in no particular order, any number of glyph (descriptions of glyphs), hkern
(horizontal kerning), and vkern (vertical kerning) elements. Ligatures are defined, as we
shall see below, by an attribute of the glyph element.
Here, then, in schematic form, is the structure of an SVG font:
&lt;font ... various attributes ...&gt;
&lt;font-face
... attributes taken from CSS ...>
&lt;font-face-src&gt;
&lt;font-face-name name="... name of the font ..."/&gt;
&lt;/font-face-src&gt;
&lt;/font-face&gt;
&lt;glyph unicode="... Unicode code ..."
glyph-name="... name of the glyph ..."
lang="... language ..."
... font-metric attributes ...
d="... description of the glyph's contours ..."/>
```

The SVG Format
&lt;glyph .../&gt;
&lt;glyph .../&gt;
...
&lt;hkern ... various attributes .../&gt;
&lt;hkern .../&gt;
...
&lt;vkern ... various attributes .../&gt;
&lt;vkern .../&gt;
...
&lt;/font&gt;
Let us return now to a more detailed description of the elements font, font-face, glyph,
hkern, and vkern; after all, they deserve it, and they even hold a few pleasant surprises
in store for us.
The font element and its attributes
There is nothing much to say: the font element contains an SVG font. There are only six
characteristic properties that affect the set-width and the default spacing of the glyphs:
• horiz-adv-x and vert-adv-y: the default horizontal and vertical set-widths, used
when the glyph itself has no indication of its set-width. That makes no sense for
an ordinary Latin font, but for monospaced fonts it can come in handy, and it is
very useful indeed for ideographic fonts, for which there may be 30,000 glyphs, all
with the same set-width. No default value is specified for the horizontal set-width;
if the reader does not use this attribute, no problem will arise until the day that
he attempts to set type vertically. Specifically, as we shall see, SVG takes half of the
value of horiz-adv-x to define the baseline for vertical typesetting. The default value
for the vertical set-width is an em; thus the set-width is correct for the ideographic
fonts, which are, after all, the ones most often used in vertical typesetting; and for
the others—for example, in the unusual case of English typeset vertically, the em
corresponds to the standard leading, and is thus the most natural choice.
• horiz-origin-x and horiz-origin-y: the offset of the origin of each glyph when
type is set horizontally; their values are zero by default.
• vert-origin-x and vert-origin-y: the offset of the origin of each glyph when type
is set vertically. The default values are quite interesting: horizontally the value is half
of horiz-adv-x, and vertically it is the value of the ascent attribute of font-face—
an attribute that we already know, since it is part of the CSS declarations and gives the
height of the letters with ascenders. Once again, these choices are oriented towards
the ideographic languages: indeed, in this case, ascent and horiz-adv-x are both
equal to an em. Thus the default spacing amounts to starting above the glyph and
on its axis of vertical symmetry, which is the usual method for vertical typesetting.

Characterizing a font
The first node under the font element is font-face, whose name is inspired by the “atrule” @font-face of CSS; the role of this element is to characterize the font being used.
If it is an SVG font whose glyphs are explicitly described by glyph elements, certain properties (such as the set-widths of all the glyphs) may be useless; but it may also be a font
to be downloaded, and in that case it is necessary to provide for the possibility that the
font may be inaccessible, and, therefore, to have enough informations to “synthesize” it
or make a judicious replacement. Thus we find ourselves in the same dilemma as in CSS,
and that is why font-face takes practically all of the CSS declarations that apply to fonts.
This element is therefore a catchall that contains no fewer than 33 properties specific to
it. We can classify these properties into four categories:
• An essential property: units-per-em, which determines the number of internal
units per em. The most common values are 1,000 (PostScript Type 1), 2,048 (TrueType), 250 (Intellifont). Default value: 1,000.
• Those that we already know, having seen them and described them in detail in the
section on CSS (see page 320): font-family (the name of the “font family”), fontstyle (roman, italic, slanted), font-variant (small capitals or not), font-weight
(weight), font-stretch (expansion or contraction of the set-width), font-size (actual size), unicode-range (Unicode range covered), panose-1 (a classification of the
font through the use of 10 numbers, described in Chapter 11), stemv (the thickness
of the main vertical downstroke), stemh (the thickness of the main horizontal downstroke), slope (slope), cap-height (height of the capitals), x-height (height of the
short letters), accent-height (height of the accents), ascent (height of the letters
with ascenders), descent (depth of the letters with descenders), widths (set-widths of
the glyphs—warning: only one glyph per Unicode character!), bbox (the bounding
box for all the glyphs in the font).
• Alignment properties: these are a certain number of baselines and axes for horizontal and vertical alignment (Figure 10-8): alphabetic (our good old baseline), ideographic (the same, but for the ideographic characters, which are set slightly lower
than Latin and other letters), mathematical (the axis for aligning mathematical symbols such as the minus sign, the plus sign, the equal sign, etc.), hanging (the “baseline” for the scripts that “hang down”, such as Devanagari). Next come the vertical
counterparts of these properties: v-ideographic (the vertical axis of the ideographs),
v-alphabetical (the vertical axis of the alphabetic scripts set in this direction), vmathematical (the same for mathematical symbols), v-hanging (the same for “hanging” scripts); note that these last four are added to the value of vert-origin-x, an
attribute of font.
• Finally, properties for underlining: underline-position (depth of the underline),
underline-thickness (thickness of the underline), strikethrough-position, strikethrough-thickness, overline-position, overline-thickness (height and thickness of the bar used for striking through text or overlining) (Figure 10-8).

The SVG Format












Figure 10-8: Different SVG metric properties, specific to the font-face element. Left: (1) ascent, (2) cap-height, (3) x-height, (4) alphabetical, (5) descent. Right: (1) overlineposition, (2) strikethrough-position, (3) underline-position, (4) hanging, (5) mathematical, (6) alphabetical again, (7) ideographic.
We mentioned above the fact that font-face can use CSS’s strategies for the downloading, intelligent replacement, or synthesis of fonts. These tasks are achieved through the
subelements of font-face, with names that evoke the corresponding CSS declarations:
• font-face-src: the equivalent of the src: declaration. Its role is to indicate that no
font is explicitly described here but rather that downloading, replacement, or synthesis of a font is desired.
• font-face-uri, with the xlink:href attribute: the equivalent of the url() keyword
of CSS. Its role is to give the location of the file containing the font on the Web or
on the disk. Note that “URI” is more accurate than “URL”, since URIs include both
URLs and local files.
• font-face-name, with the name attribute: the equivalent of the local() keyword of
CSS. Its role is to specify the name of the font in question as used in the operating
system. Note that the choice of the term “name” in SVG is more appropriate than
that of “local” in CSS, since, first, it is indeed an internal name, which justifies “name”,
and, second, url() can also point to a “local” file, and so the difference between it
and local() is not clear.
• font-face-format, with the string attribute: the equivalent of the format() keyword of CSS; in addition to the values of the latter keyword, there is also svg. Note
that font-face-format is a subelement of font-face-uri—which is quite logical: if
there are multiple URIs, they may not all be of the same format.
Thus our CSS example:
@font-face { font-family: "Omega Serif";
font-style: italic;
unicode-range: U+0020-, U+0300-E, U+1E??, U+2000-F;

```text
src: url("http://omega.enstb.org/fonts/omsela.otf")
format("opentype");
local("Omega Serif Italic");
}
is written as follows in SVG:
&lt;font-face font-family="Omega Serif" font-style="italic"
unicode-range="U+0020-, U+0300-E, U+1E??, U+2000-F">
&lt;font-face-src&gt;
&lt;font-face-uri xlink:href="http://omega.enstb.org/fonts/omsela.otf"&gt;
&lt;font-face-format string="opentype"/&gt;
&lt;/font-face-uri&gt;
&lt;font-face-name name="Omega Serif Italic"/&gt;
&lt;/font-face-src&gt;
&lt;/font-face&gt;
The reader may decide which of these forms is clearer.
Describing a glyph
After all this discussion à la CSS, we have finally reached the innovative part of SVG:
the description of glyphs. If glyphs are “atoms” in the presentation of a document, we
can say that SVG has managed to become the first XML standard that can operate at the
atomic level. But beware: in real life, when we descend to this level, we discover that
nature hides obscure and destructive forces that are quite capable of annihilating us. The
same is true here, but the role of Mother Nature is played by the foundries: if the reader
has fun including glyphs from fonts produced by the large foundries in his document, it
does not take an Einstein to anticipate what is likely to happen.
Now that we have issued this figurative warning, which, we hope, will be more effective
than the ubiquitous “small print” in licenses that no one ever bothers to read, let us
present a question: what is a glyph, and how can we describe it?
According to the straight and narrow road of PostScript Type 1 and True/OpenType, a
glyph is a set of contours enclosed in an abstract box that is used in typesetting. But
then why should we choose one glyph instead of another? Recall how typesetting is
done: the typesetting software receives Unicode characters and is supposed to supply
the glyphs. Thus it must first know which glyphs correspond to which given Unicode
characters (or to a set of Unicode characters, if these represent a ligature), then which
glyphs are available, and, finally, under which conditions it should choose a given glyph
from among them.
In the case in which the glyphs that correspond to the same Unicode character are only
graphical variants pure and simple, these glyphs must have identifiers so that they can
be selected through the use of altGlyph.
Let us continue. The description of a glyph is completely contained in a glyph element—
or perhaps in a missing-glyph element, which indicates the glyph to be used when the
```

The SVG Format


Figure 10-9: Examples of horizontal and vertical typesetting: (1) the arrows start from the “horizontal” origin (coordinates (0, 0)) of the glyph and have a length of horiz-adv-x; (2) the arrows
start from the “vertical” origin (coordinates (vert-origin-x, vert-origin-y)) of the glyph
and have a length of vert-adv-y.
requested glyph is missing. The attributes of glyph describe its abstract box, relate it to
Unicode, and allow it to be distinguished from other glyphs belonging to the same character:
• horiz-adv-x: the displacement of the current location for this glyph during the process of (horizontal) typesetting.
• vert-adv-y: the same, but for vertical typesetting.
• vert-origin-x and vert-origin-y: the origin of the glyph in vertical typesetting
(see Figure 10-9).
• unicode: the Unicode character corresponding to the glyph. The usual XML techniques for designating this character are available: either one uses the active encoding (UTF-8, for example) or one uses a character entity (such as &#xABCD; or
&#12345;).
Here is where any ligatures are indicated: if the ligature is of the classic type, i.e., the
replacement of several glyphs by only one, we write here the corresponding Unicode
characters. Thus, by writing unicode="st", SVG will replace the glyphs for the characters ‘s’ and ‘t’ with the glyph for the ligature ‘s’.
• id: a unique identifier (at the level of the entire XML document) that, in addition,
must begin with a letter (not, for example, with a digit or a punctuation mark). This
attribute is not specific to glyph and can be used with any SVG element. We mention this here because it is the link that we have to the world outside the font. The
altGlyph element can directly invoke a glyph in the font by using the URI of the
XML document containing the font and this identifier.

• glyph-name: one or more internal names for the glyph. If several are used, they are
separated by commas. These are also unique identifiers, but those used internally by
the font: they are used to describe kerning pairs.
• orientation: is this glyph used only for horizontal or vertical composition? Possible
values: h and v.
• lang: is this glyph specific to a certain language? That is the case, for example, for
the “Chinese” and “Japanese” variants of many ideographs, or even the letters ‘ä’,
‘ë’, ‘ö’, and ‘ü’, whose accent (“diaeresis” or “umlaut”) is not set at the same height in
English and German typography. Possible values [103]: a series of language codes (as
recommended by RFC 3066; in other words, a two-letter ISO 639 code for the name
of the language, possibly followed by an ISO 3166 country code and other auxiliary
codes), separated by commas. Example: lang="fr, en, es".
• arabic-form: the Arabic or Syriac contextual form of the glyph. Possible values:
initial, medial, terminal, isolated. Note that these forms also apply to ligatures.
Thus, for example, if we form a ligature by beginning with an initial (or medial)
glyph and ending with a medial (or final) glyph, the result is an initial glyph. (Likewise for medial, final, and isolated glyphs.)
• d: the contours. We have left the most important item for last: the value of this attribute is a sequence of contours. Each contour is a closed path, i.e., a sequence of
concatenated Bézier curves and/or straight lines for which the terminal point of the
last is identical to the initial point of the first.
The syntax for the SVG paths used in the value of the d attribute remains to be seen. This
syntax is not specific to fonts but is also used for graphic design in SVG: drawing shapes,
setting text along curves. In it, we find quadratic Bézier curves, just as in TrueType fonts,
but also cubic ones, as in PostScript and OpenType/CFF fonts. There is even another type
of curve, never before used in fonts: elliptical arcs.
Another characteristic: the format looks like PostScript (or PDF) at first glance. For example, we use operators with a single letter and coordinates. But we quickly learn that
there are fundamental differences. First of all, the notation is not reverse Polish: the
parameters follow the operator instead of preceding it. Next, there is no stack: it is impossible to push one value in order to pop it 10 lines below, as we can enjoy doing in
languages such as PostScript. Another peculiarity: we can separate operators and parameters from each other through the use of “separators” (spaces or commas), but we can
also delete all the separators, except for spaces that separate numbers. This compacting
of the code gives the value of d its terribly cryptic appearance.
Rather than describing the syntax of SVG paths in detail (the reader will find a detailed description
in [134, section 8.3]), we shall take apart a concrete example: the description of the glyph ‘R’ of the
font that we are currently using, Le Monde Livre, by Jean François Porchez (see Figure 10-10). Note
that the two programs (batik-ttf2svg and FontForge) produced exactly the same code, shown here:

```text
The SVG Format
&lt;glyph unicode="R" glyph-name="R" horiz-adv-x="689"
d="M 520 -,
Q 496 29 459 76, T 382 173, T 305 270, T 244 350,
H 275,
Q 307 350 337 357, T 390 380, T 428 424, T 443 492,
Q 443 537 431 565, T 395 610, T 341 633, T 272 640,
H 226, V 129,
Q 226 97 227 79, T 234 50, T 248 35, T 273 26,
L 317 14, V 0, H 33, V 14, L 77 26,
Q 92 30 101 34, T 116 49, T 122 78, T 124 129,
V 546,
Q 124 578 123 596, T 116 625, T 102 640, T 77 649,
L 33 661, V 675, H 309,
Q 352 675 395 670, T 474 647, T 532 597, T 554 510,
Q 554 473 539 445, T 499 395, T 442 359, T 375 336,
Q 395 311 416 284, T 460 230, T 503 178, T 544 129,
Q 587 80 610 56, T 654 25,
L 687 14, V 0, L 520 -, Z" />
We have added spaces and commas to make the code more legible. Does it still appear cryptic?
Here are the rules of the game: M is a motion without drawing; it is used only once to set the starting
point at the base of the leg of the ‘R’; Q and T are quadratic Bézier curves (as in TrueType), their
difference being that in Q both the control point and the end point are indicated, whereas in T
it is assumed that the control point is the reflection of the control point of the preceding curve
(which is why a T must always follow a Q); L is a straight line; H and V are straight lines, the former
horizontal and the latter vertical.
Let us examine the code, following the diagram in Figure 10-10. We begin with an M at the base of
the leg. Next come a series of Q commands and three Ts, to bring us to the top of the leg. Then we
move to the right with an H, which produces a short horizontal line, and then two 1-3 sequences
(i.e., a Q and three Ts) to form the inside curve. A horizontal line (H) follows, and then we move
straight down with a V. Now we prepare to draw the bottom serif. We begin with a 1-3 series, and
before reaching the flat part of the serif we have another short straight segment (L). We draw the
base (V, H, V) and proceed symmetrically with an L and a 1-3. The bottom serif is finished. We move
up with a V and then draw, as with the lower serif, the half-serif at the top: a 1-3, an L, then a V. We
have reached the top line. We go to the right (H) and draw the large curve with two 1-3 sequences.
Having again reached the leg, but this time on its upper part, we slide down with a 1-3. At the point
544,129, we follow the logic of the half-serif; we had expected a 1-3, but it is easier this time: a Q
followed by a single T, and then another L and the base: a V and an L to take us back to the starting
point. We finish with a Z, which closes the path and makes it into a contour.
After this excursion around the periphery of the ‘R’, and before concluding this section
on the glyph element, one more important point: up to now, we have assumed that a
glyph was merely a set of contours drawn with the d attribute, the glyph element being
left empty. SVG also affords us the possibility of including graphical elements in the
glyph. Indeed, we can include any graphical operator within glyph: an entire SVG image
can become a single glyph! Up to now that was possible only for PostScript Type 3 fonts
(whose death knell was sounded the day that Acrobat was released) and the virtual fonts
of TEX, in which both DVI commands and PostScript code can be included. The power
gained in this way boggles the imagination: a glyph can be colored in, contain a bitmap,
```

```text
520,-1
459,76
382,173
305,270
244,350
h=275 337,357
390,380
428,424
443,492
431,565
395,610
341,633
272,640
h=226
v=129
227,79
234,50
248,35
273,25
317,44
v=0
h=33
v=1477,26
101,34
116,49
122,78
124,129
v=546
123,596
116,625
102,640
77,649
33,661
v=675
h=309
395,670
474,647
532,597
554,510
539,445
499,395
442,359
375,336
416,284
460,230
503,178
544,129
610,56
654,25
687,14
v=0
Q
Q
Q
Q
Q
Q
Q
Q
Q
Q
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
T
L
L
L
L
V
V
V
V
V
V
H
H
H
H
H
Point de départ
Figure 10-10: The glyph ‘R’ from the font Le Monde Livre, converted to SVG.
be transparent, be animated, even interact with the user. It goes without saying that that
ground remains unexplored, but the fact that the SVG standard provides for it is in itself
a minor revolution!
Kerning and kerns
To conclude our journey through SVG fonts, only kerning remains to be discussed. Here
again, the developers of SVG drew their inspiration from very highly developed formats
such as OpenType, and they introduced a very flexible system for determining kerning
paires. The idea is that there are often families of glyphs that are kerned in the same way;
“A, À, Â, Á, Å, Ã, ... ” is one example. On the other hand, while it is very practical to indicate these glyphs through their Unicode characters—after all, for most of the characters
in the world, there is a one-to-one correspondence between character and glyph—that
is not always possible. If necessary, we can always use the internal names of the glyphs
(those of the glyph-name attribute of glyph).
Thus we can write:
```

```text
Conclusion
&lt;hkern u1="A,À,Â,Á,Å,Ã,&#x100;,&#x104;" g1="A.pretty,A.bizarre"
u2="T,&#x162;,&#x164;,&#x166;" g2="T.shirt"
k="35"/>
where hkern is a kerning pair for horizontal typesetting; u1 and g1 describe the family
of glyphs that appear at the left (u1 contains characters or zones of Unicode coverage,
separated by commas, and g1 contains internal glyph names, also separated by commas);
u2 and g2 describe the family of glyphs that appear at the right; k gives the kerning value
(positive equals closer spacing of the glyphs). Although the reader may not have expected
it, hkern has defined 10 × 5 = 50 kerning pairs.
One small detail, to avoid surprises if the reader is preparing to kern a Hebrew, Arabic,
or Syriac font: kerning is performed after the left-to-right rearrangement of the glyphs. In
other words, if the reader wishes to kern a reh followed by a beh (the beh thus being to
the left of the reh), she must write a pair with beh as g1, even though logically it comes
second, and reh as g2, even though logically it comes first. Thus kerning occurs in the
left-to-right visual order, not in the logical order. Could this be a flagrant lack of political
correctness on the part of the authors of SVG?
Finally, SVG provides vertical kerning pairs, which are very useful for certain typographic practices in the ideographic languages.19 The syntax is the same, except that the
element is called vkern and the adjustment of spacing is towards the top.
Conclusion
Here we are at the end of this chapter devoted to the management and use of fonts on the
Web. We can see that the Web is the victim of its own success: faced with the explosion in
the number of users (and the size of the market that they represent), organizations and
companies have produced in record time a vast range of tools and standards. But there is
always something amiss: the tools are compatible with so few browsers that incompatibility is more the rule than the exception. The standards, as beautiful and powerful as they
may be, exist on paper only, in the vast majority of cases. Even worse, the multinational
corporations control the lion’s share: it is Microsoft that reigns supreme in the downloading of fonts, at least until GlyphGate comes to be more widely used—as it deserves
to be; and Adobe has a near monopoly on tools for SVG.
Let us not deceive ourselves: the true problem is neither technology nor the complexity
of the world’s writing systems. The problem is copyright. The fact that a font belongs to
the foundry that distributes it and that that foundry grants to only one person at a time
the right to use it stands in flagrant contradiction to the principles of the Web, where all
resources (text, images, sound, animations) are freely available to everyone. That is why
Bitstream, Microsoft, and em2 Solutions are bending over backwards to provide fonts
19 Ordinarily the ideographic languages are written vertically. But tradition demands that each glyph occupy a perfect square (the ideographic square) and that typesetting consist of the juxtaposition of these squares,
which is why kerning is denied. Some Japanese typographers, however, violate this tradition by recommending
kerning between ideographs whose shape calls for it. [208, p. 七五(75)], [240, p. 364]
```

to web users—without actually providing them. That is the reason for which the best intentions of CSS and SVG may go unheeded. Let us hope that in the future we shall emerge from this tunnel, either by a miracle solution to the problem of rights or by a decision from the large foundries to offer even part of their fonts to the users of the Web so as to bring a little beauty to this virtual space that is nothing less than the first space for communication on a planetary scale in human history.
