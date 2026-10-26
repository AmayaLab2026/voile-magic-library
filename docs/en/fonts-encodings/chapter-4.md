---
title: "Chapter 4: Normalization, bidirectionality, and East Asian characters"
description: "Unabridged English text: Canonical and compatibility equivalence, NFC/NFD/NFKC/NFKD, Unicode Bidirectional Algorithm (UAX #9), CJK Unihan ideographs, CDL, and Hangul Jamo arithmetic."
---

# Chapter 4: Normalization, bidirectionality, and East Asian characters
**By Yannis Haralambous, Ph.D.**
*From Fonts & Encodings, pp. 127–158*

---


In this chapter we shall examine three aspects of Unicode that have nothing in common
other than requiring a certain amount of technical background and being of interest
more to the specialist than to the average Unicode user. They are the procedures for
decomposition and normalization (of interest to those who develop Unicode applica-
tions for the Web), the bidirectional algorithm (of interest to users of the Arabic, Syriac,
and Hebrew scripts), and the handling of ideographs and hangul syllables (of interest to
readers of Chinese, Japanese, or Korean).
### Combining Characters
We have already discussed the block of combining characters, as well as the category of
“marks” and, in particular, the nonspacing marks. But how do these characters work?
The glyph of a combining character interacts with the glyph of a base character. This in-
teraction may take a variety of forms: an acute accent goes over a letter, the cedilla goes
underneath, the Hebrew dagesh goes inside the letter, etc.
Some of these diacritical marks are independent of each other: placing a cedilla under-
neath a letter in no way prevents a circumﬂex accent from being added as well. Other
marks are placed in the same location and thus must appear in a speciﬁc order. For ex-
ample, the Vietnamese language has an ‘Ë’ with a circumﬂex accent and a tilde, in that
order; it would be incorrect to place them the other way around.
127


128
All of that suggests two things: ﬁrst, diacritical marks can be classiﬁed in “orthogonal”
categories; second, the order of application within a single category is important. Uni-
code has formalized this approach by deﬁning combining classes.
There are 352 combining characters in Unicode, and they are distributed among 53 com-
bining classes. Among these classes are, ﬁrst of all, those for signs that are speciﬁc to a
single writing system (an Arabic vowel over a Thai consonant would have little chance
of being recognized as such):
• Class 7: the sign nukta, used in Indian languages. It is a dot centered below the letter,
and it is used to create new letters.
• Class 8: the kana phonetic modiﬁers dakuten and handakuten.
• Class 9: the sign virama, used in Indian languages. It is a small slanted stroke that
indicates the absence of the inherent vowel.
• Classes 10–26: the Hebrew vowels, semivowels, sign for the absence of a vowel, pho-
netic modiﬁer dagesh, and other diacritical marks.
• Classes 27–35: the Arabic vowels with and without nunation, the sign for gemination
of a consonant, the sign for the absence of a vowel, and the superscript alif.
• Classes 36: The superscript alif of Syriac.
• Classes 84 and 91: the two Telugu length marks.
• Class 103: the two subscript vowels of Thai.
• Class 107: the four Thai tone marks, placed above the letter and right-aligned.
• Class 118: the two subscript vowels of Lao.
• Class 122: the four Lao tone marks, placed above the letter and right-aligned.
• Class 129: the Tibetan subscript vowel ‘%’.
• Class 130: the six Tibetan superscript vowels.
• Class 132: the Tibetan subscript vowel ‘u’.
• Class 240: the Greek iota subscript, Unicode’s enfant terrible.
We shall see that Unicode did not exactly put itself out when classifying the signs of He-
brew and Arabic. Rather than determining precisely which of these signs can combine
with which others, it assigns each of them to a distinct class; thus, in theory, they can
be combined without regard for their order and with no typographical interplay among
them. This approach is obviously incorrect: when we combine a shadda (sign of conso-
nant gemination) and the vowel damma over a letter, as in ‘È’, the latter must appear
over the former. But let us move on.
In addition to these speciﬁc classes, there are also 12 general combining classes, whose
members can be used in more than one writing system:


129
• Class 202: attached beneath a letter, as is the case with the cedilla (ç) and the
ogonek (J)
• Class 216: attached above and to the right of a letter, as with the Vietnamese horn (q)
• Class 218: attached beneath and to the left of a letter, as with a small circle that indi-
cates the ﬁrst tone of a Chinese ideograph
• Class 220: centered beneath a letter and detached from it, as with the underdot (),
the underbar (R), and 79 other signs of this type
• Class 222: to the right of a letter, beneath it, and detached from it, as with two Ma-
soretic signs, yetiv (Í) and dehi (Î), among other signs
• Class 224: centered vertically and to the left, as with the Korean tone marks
• Class 226: centered vertically and to the right, as with dotted notes in music (Ì)
• Class 228: above and to the left of the letter, and detached from it, as with one Ma-
soretic sign, zinor (Ï), among others
• Class 230, the largest class: centered above the letter, as with 147 characters ranging
from the grave accent (à) to the musical pizzicato sign
• Class 232: above and to the right of the letter, and detached from it, as with the háˇcek
shaped like an apostrophe that appears with the Czech and Slovak letters ‘d’ ’, ‘t’ ’, ‘l’ ’,
etc.
• Class 233: an accent extending beneath two letters, such as (Ô)
• Class 234: an accent extending above two letters, such as (Ó)
To encode diacritical marks, we proceed in any order for those that are not in the same
combining class and from the inside outward1 for those that are. Thus, to obtain ‘’, we can
use the sequence “a, circumﬂex, tilde, underdot, under-háˇcek” or “a, underdot, under-
háˇcek, circumﬂex, tilde”. Unicode deﬁnes a canonical approach: diacritical marks of dif-
ferent classes are handled in the increasing order of their class numbers. In our example,
the accents that appear above the letter are of class 230 and those beneath the letter are
of class 220; therefore, we ﬁrst write the accents beneath the letter, then the ones above.
We thus obtain a unique string yielding ‘’:
1 Unicode’s approach is almost perfect, but one case raises some doubts: how to handle combinations of
a breathing mark and an accent in Greek? As we can see in the letter ‘V’, there can be a breathing (rough, in
this case) and an accent (grave) on the same letter. Since these two diacritical marks are of the same combining
class, number 230, arranging them in canonical order requires that one be the inner and the other the outer
mark. But since they appear at the same height, we ﬁnd it hard to make a decision. The solution to this problem
appears in the Unicode book. We have seen that it contains the ﬁrst canonical decomposition for every decom-
posable character. In the present example, the breathing comes ﬁrst; this choice is in any case natural, because
the script itself reads from left to right. Another problem of the same type: iota with a diaeresis and an acute
accent (G). Here Unicode stipulates that the diaeresis comes ﬁrst, doubtless because there is also a diaeresis/tilde
combination ‘I’, in which the tilde clearly lies outside the diaeresis. But perhaps we are nitpicking here?


130
0x0061 latin small letter a
0x0323 combining dot below
0x032C combining caron below
0x0302 combining circumﬂex accent
0x0303 combining tilde
Composition and Decomposition
We have seen that there is a canonical way to represent a base character followed by one
or more combining characters. But for historical reasons, or merely so as not to overtax
our software, Unicode contains a large number of decomposable characters—those whose
glyph consists of a base glyph and a certain number of diacritical marks. In order for a
glyph to be decomposable, its constituents must also be Unicode characters. Example: we
could say that ‘’ is the precomposed form of a character ‘’ and a trio of Arabic dots,
but that would be of no validity, as Unicode does not separate the Arabic characters from
their dots, much as we do not say that ‘W’ is made up of two instances of the letter ‘V’.
Thus these two characters are not decomposable.
Practically all Unicode characters with diacritical marks are decomposable. Their canon-
ical decomposition is given in the Unicode book by lines beginning with the equivalence
sign (≡), and also in the following ﬁle:
http://www.unicode.org/Public/UNIDATA/UnicodeData.txt
We are concerned with the ﬁfth ﬁeld, counting from zero, of each line of this ﬁle. This
ﬁeld may contain, as appropriate, either the canonical decomposition or the compatibil-
ity decomposition. In the latter case, it always begins with a tag (see page 124).
A canonical decomposition is, by deﬁnition, unique and always consists of one or two
characters. Canonical decompositions containing only one character usually represent
characters created for reasons of compatibility with other encodings, for which we in-
dicate the canonical equivalence to other characters. For example, the Greek question
mark (;), which is the spitting image of the Latin semicolon, is canonically equivalent
to it.
When a canonical decomposition consists of two characters, the ﬁrst is a base character
and the second is a combining character.
There is a reason for calling this decomposition “canonical”, as in the previous section
we also identiﬁed as “canonical” the standard way to combine base characters with com-
bining characters. By applying canonical decomposition recursively to a character, we
obtain a base character and a canonical sequence of combining characters.
Example: The Vietnamese character ‘©’ is decomposed into “ê, acute accent”. If we de-
compose the new base character, we obtain “e, circumﬂex accent, acute accent”, which is
indeed the canonical order, because it arranges the diacritical marks from the inside out.
The other type of decomposition is compatibility decomposition. Its purpose may be to
help software to generate a glyph for a character that it does not recognize or to facilitate


131
searches in a document. The typical example of compatibility decomposition is that of
the Japanese character ‘㎦’, which is decomposed into a ‘k’, an ‘m’, and a ‘3’. This ‘3’ in turn
has a compatibility decomposition into a regular ‘3’ with the &lt;sup&gt; tag, which indicates
that it is an exponent. By carrying out all the decompositions, a program can know that
‘㎦’ corresponds approximately to the string km3; thus the user can search for this string
without bothering to enter the original Unicode character.
Compatibility decomposition also entails loss of information: we lose, at a minimum,
the precise semantics of the original character, and we may also lose precision with re-
spect to the glyph. Thus the decomposition of the character ‘W’ 0x03D1 greek theta
symbol is ‘θ’ 0x03B8 greek small letter theta, whose glyph is not the same. That loss
may be relatively unimportant (in a Greek document, for example), but it may be critical
in a mathematical document in which both forms of theta have been used as diﬀerent
symbols. Be careful!
The compatibility decomposition of a character is found in the character’s description
in the Unicode book and also in the ﬁle UnicodeData.txt, where it occupies the ﬁfth
ﬁeld. This is the same ﬁeld used for the canonical decomposition, but there is no con-
ﬂict because the two may not occur with the same character. We use tags to indicate
that the decomposition is one of compatibility. These tags may also serve to provide a
better description of the desired glyph. In this way, we can indicate that a special font
is recommended, that the glyph is superscript or subscript, that it is full-width or half-
width, etc. We described these tags in detail in the previous chapter on page 124.
Normalization Forms
We have seen that the canonical decomposition, when applied recursively for a ﬁnite and
even relatively small number of steps, will yield a base character followed by a canonical
sequence of combining characters. Why not carry out this operation systematically? That
strategy would have the advantage of encoding each character in a unique manner: there
would be no more precomposed characters, no more noncanonical ways to decompose
a character—just a canonical method, nothing else.
This operation is called Normalization Form D (‘D’ as in “decomposition”), or NFD. This
normalization form requires each decomposable character, including the hangul sylla-
bles (see page 4), to be decomposed canonically.
Since we are going to that extent, why not carry out all compatibility decompositions
as well? That strategy is called Normalization Form KD (‘K’ to suggest “compatibility”),
or NFKD. In the previous section, we urged the reader to be careful with compatibility
decomposition, and here we are suggesting that it be applied blindly to an entire docu-
ment! That is a risky approach. But it may also facilitate the task of software that wishes
to perform searches or sorting and that relegates the precise semantics of characters to
secondary importance.
When we decompose all characters, the size of the document goes up. A Vietnamese
document, for example, will almost double in size. Decomposition is also a burden to


132
software because it must not only look up a glyph corresponding to a character but ac-
tually place an accent over a glyph or look up in a table the information that shows that
a given sequence of characters corresponds to a certain precomposed glyph. Thus it is
quite natural to go in the other direction and perform massive compositions.
It is interesting to take the data in Unicode, produce their NFD (normalization based on
canonical decomposition), and then recompose the composite characters. By so doing,
we obtain a document encoded in a way that is unique (because NFD makes it unique)
and eﬃcient (because the number of characters is minimized). We call that Normalization
Form C (‘C’ as in “composition”), or NFC.
One may well ask how to go about composing characters. If, for example, I have a canon-
ical string “X accent1 accent2”, in which the two accents are not in the same combining
class, and if no precomposed character “X accent1” exists, may I try to combine ‘X’ with
“accent2”? And what happens if the accents are in the same combining class?
Fortunately, NFC’s rules have been clearly stated in a technical report by the consortium
[109]. A few deﬁnitions: if B is a base character and C a combining character, we say that
C is isolated from B if there is another combining character C ′ of the same class as C that
appears between B and C. We say that a character is a primary precomposed character if
it has a canonical decomposition in the ﬁle UnicodeData.txt and if it is not listed in
CompositionExclusions.txt.
What is the meaning of the latter condition? Some precomposed characters should be
ruled out. In other words, when we systematically compose everything that can be com-
posed, there are certain characters that we are better oﬀnot obtaining by composition.
These characters are of four types:
• 67 characters speciﬁc to single scripts, most of them characters that are in Unicode for
reasons of compatibility with other encodings. Very important in this list are the He-
brew presentation characters, i.e., the precomposed Hebrew letters with the dagesh or
vowels. Since they are only presentation forms, they should not have had canonical
decompositions; after all, the Arabic ligatures that are presentation forms have only
compatibility decompositions, and so this problem does not arise. The consortium
attempted to correct the error by placing the Hebrew presentation forms on this
blacklist of precomposed characters that are excluded from canonical composition.
• 14 characters that were added to Unicode after the report was published.
• 924 characters that are canonically decomposed to a single character.
• 4 crazy characters that are both precomposed and combining. The typical example is
the Greek diaeresis with accent (Û). It is a precomposed character because it combines
a diaeresis with an acute accent, but it is also a combining character.
The third deﬁnition: a character B can be primary combined with a character C if there is
a primary precomposed character whose canonical decomposition is BC.
This is how we shall carry out NFC on the basis of these three deﬁnitions. We start with a
string S and apply NFD to it. Next, we take each characterC in the document in the order


133
in which it appears. IfC is a combining character and B is the last base character beforeC,
then: (a) if C is not isolated from B and (b) if B can be primary combined with C, we
replace B by the composition of B and C and we delete C. Once we have carried out this
process for all the characters, we will obtain a new string S ′, which is the NFC-normalized
version of S.
Example: take the string “a Ù ı ˜”, i.e., an ‘a’ followed by a cedilla (class 202), an underdot
accent (class 220), and a ring accent (class 230). The glyph obtained in the end is ‘ˆ’. The
NFD of this string will be the same because the string is already canonical (the classes
are in increasing order). On the other hand, the NFC is “å Ù ı”, i.e., ‘å’ followed by the
cedilla and the underdot. The rules of NFC enabled us to incorporate the ring accent,
despite its distance from the base character.
NFC has become very popular because it is part of a recommendation by the W3C.
Speciﬁcally, the W3C considers that all data on the network—be it in XML or XHTML
documents, URLs, or anything else—should be normalized according to NFC. There
is only one little detail: this conversion must be performed at the source, as early as
possible. The W3C’s report [126] calls that early uniform normalization (EUN). Text must
therefore be normalized as soon as possible. Why? Because the creator of the text is in the
best position to normalize it, and furthermore because she will perform the normaliza-
tion only once. By assuming that text is already NFC-normalized when it is published on
the Web, browsers and other software that receives web data do not have to check that the
text has been normalized and can eﬃciently conduct their searches, string comparisons,
indexing, and so on.
We can also perform a “compatibility composition”, i.e., a compatibility decomposition
followed by a canonical composition, as we did for NFC. This procedure is known as
Normalization Form KC (NFKC). It can also be useful for facilitating certain tasks, such as
searches for strings.
Before ﬁnishing this section on normalization, let us note that the consortium makes
available a “torture test” that can be used to evaluate the quality of a normalization
performed by software. It is the ﬁle NormalizationTest.txt. This 2 MB ﬁle enables us
to test the four normalization forms: NFD, NFKD, NFC, and NFKC.
Nowadays we often speak of “culture shock”. This shock has been troubling typographers
for centuries because one of its most trivial aspects (and, alas, one of the easiest to resolve)
is the diﬀerence in the direction in which scripts read. Suppose that we are writing a line
of text in English and suddenly decide to switch to Arabic when we reach the middle of
the line. Arabic is written from right to left; thus we cannot simply stay where we are and
start writing in the opposite direction, since the space is already occupied. Thus we have
to move, but where should we go? The less daring among us will change paragraphs at
this point: that is a way to start from scratch. In the new paragraph, we start at the right,
with the usual indention, and everything is perfect.


134
But suppose that the nature of the text does not permit a change of paragraph. Ideally
we would set aside the space needed to write the few words of Arabic and begin at that
point. But what happens if the Arabic text runs for several lines? And how can we go
back to writing in English?
Fortunately, we are not the ﬁrst to raise these questions; they have been tormenting ty-
pographers, and subsequently computer scientists, for some time now. In this chapter,
we shall discuss the solution that Unicode oﬀers for these problems, which are as old as
the hills (or, at a minimum, as old as our cultures).
So as not to favor one of the scripts that are written from right to left (Arabic, Hebrew,
Syriac, Thaana, and sometimes Tiﬁnagh, Egyptian hieroglyphs, epigraphic Greek, etc.),
we shall illustrate our points with examples in English, but by using a special font, eL
erviL ednoM. The reader will have to put forth a little extra eﬀort to get used to read-
ing backwards, but we consider this eﬀort minuscule compared with the learning of a
new alphabet. Besides, in an era when mirrors were not so common as they are now,
Leonardo da Vinci used this sort of writing for his notes, so there is a precedent for it!
And that is not the only precedent. Another great man, Donald Knuth, used this trick in
his famous article Mixing Right-to-Left Texts with Left-to-Right Texts of 1987 [222] to demon-
strate bidirectionality in digital typography.
Before taking up the technical details of Unicode’s bidirectional algorithm, we shall de-
scribe the situation from the point of view of the typesetter, which will help us to under-
stand the Consortium’s approach.
Typography in both directions
We shall deﬁne two concepts that are crucial for describing the typographical behavior
of a document that uses scripts that read in opposite directions.
The ﬁrst concept is that of embedding. When we quote a sentence, we increase the level of
embedding. For example, in the sentence “ABC said that ‘CBS said that “NBC said that
‘PBS said that “So-and-so is going to step down” ’ ” ’ ”, we have embedding to level 3 (or 4
if we consider the entire sentence to be embedded, as it is in this book).
Conversely, if we wrote “So-and-so is going to step down. That was announced by PBS.
NBC picked up the story. CBS got it from NBC. ABC quoted NBC.”, we would remain at
embedding level 0. In this case, we would say that the sentences are sequential.
Language is not a mathematical structure; therefore there will inevitably be situations in
which we cannot tell whether there is embedding or not. In any event, we must decide
whether to interpret a given passage as being embedded or not; the formatting of the
passage will be radically diﬀerent in the two cases.
The second important concept is that of the global or local aspect of a script. The global
aspect pertains to the occupation of space, irrespective of the order in which the words
are arranged. Thus a passage in an English book might look like this:


135
![Figure 4-1: Paragraph flow and line indentation in a global left-to-right context](/images/fonts-encodings/fig4-1.png)

There will be (perhaps) an indention, and the last line does not run to the full measure.
We read the lines in the order indicated, but we disregard the contents of each line. We
say that we are in a (global) left-to-right context.
In a Hebrew or Arabic book, the situation will be reversed:
![Figure 4-2: Paragraph flow and line indentation in a global right-to-left context](/images/fonts-encodings/fig4-2.png)

The indention is at the right; the club line ends at the left. We say that we are in a right-
to-left context. Once again, as long as we remain at the global level, we see nothing but
“gray”.
The local aspect concerns the order of the words within a line. Since English is written
from left to right, the local aspect will be:
And in a language written from right to left, it is:
Up to now, what we have been discussing has been perfectly obvious. Things get more
interesting when we put the two aspects together.
Fundamental principle of bidirectional typesetting: When a passage in one
script is embedded within a passage in a diﬀerent script, the context remains the same.
Conversely, when the passages are sequential, the context changes according to the di-
rection of the script.
Example: Suppose that within our left-to-right text we have a passage written from right
to left. The principle that we have just stated tells us that, when embedding occurs, ev-
erything remains the same on the global level, as if we remained in the initial context,
namely, the left-to-right context:
![Figure 4-3: Short embedded right-to-left quotation within left-to-right text](/images/fonts-encodings/fig4-3.png)


136
What is astonishing about the ﬁgure shown above is that nothing shows that blocks
 and  are set in a diﬀerent direction. The ﬁgure would have been exactly the same
for a passage set entirely from left to right.
The situation is quite diﬀerent when the passages are sequential. For, once  has been
typeset, the context has changed, and so  will begin not at the left but at the right
(as required by the right-to-left global aspect). Likewise, when we have ﬁnished , the
context is no longer the same, and therefore  will begin at the left. Here is the result:
![Figure 4-5: Reading order across line breaks in bidirectional text](/images/fonts-encodings/fig4-5.png)
We can also reason in terms of mode. We change modes when the passages are sequential.
When we write , we are in the (global) right-to-left mode; therefore, the following line
will behave like a line in a left-to-right work. In particular, it will begin at the right. When
we write , we have changed modes again, and the next line will begin at the left because
it is in left-to-right mode. If, however, the passage is embeddded, we remain in the same
(global) mode. If this mode is left-to-right, then right-to-left blocks of text will always
begin where left-to-right blocks begin, which is to say at the left.
What, then, happens at the local level? Well, the words had better watch out. The global
level imposes its will on the local. Indeed, the local level is not even concerned with the
arrangement of the blocks. It has only one task to complete: arranging the words within
the available blocks in the required order, according to the space available. Here is how
the text looks to the eye of the reader:
![Figure 4-5: Reading order across line breaks in bidirectional text](/images/fonts-encodings/fig4-5.png)
A ﬁne exercise for eye movements! It is a bit easier in the case of sequential passages
because at least the paths traced by the eyes do not cross:
![Figure 4-5: Reading order across line breaks in bidirectional text](/images/fonts-encodings/fig4-5.png)
Let us exercise our eyes, then. Here is a paragraph containing just the ordinal numbers
from 1 to 17, with those from 5 to 13 set from right to left:


137
First second third fourth hthgie htneves htxis htfﬁ
htneetriht htflewt htnevele htnet htnin fourteenth
ﬁfteenth sixteenth seventeenth.
We can see that embedding has occurred, since the end of the right-to-left passage in the
third line appears at the left.
Let us take the same example with sequential (not embedded) text:
First second third fourth hthgie htneves htxis htfﬁ
fourteenth htneetriht htflewt htnevele htnet htnin
ﬁfteenth sixteenth seventeenth.
And here, by way of illustration, are the same examples in Arabic script. First, the em-
bedded passage:
First second third fourth  

  ! 
 "# 
 \$ %! \$

 &'! fourteenth ﬁfteenth sixteenth
seventeenth.
And then the sequential passages:
First second third fourth  

  ! 
 "# 
 \$ %! \$
fourteenth ﬁfteenth sixteenth 
 &'!
seventeenth.
Another problem compounds the diﬃculties of mixing scripts: the use of numbers. In
Arabic, Hebrew, Syriac, and Thaana alike, numbers are written from left to right.
Thus the author’s birthday is written 1962 ,16 yraurbeF ,yadirF, which in Arabic looks
like this: ()*+ 
,-
. (* /012'- 34, (or 565 78 55, meaning 11 Ramadan 1381 ah
[337]). That means that each number is treated as an embedded “left-to-right” block.
And we must not forget the characters that appear within numbers: the decimal point,
for example, which is a period in the United States but a comma in France and a small
damma in the Arab countries of the Mashreq.
Now that we have seen the methods that typography uses to solve the problems of bidi-
rectionality, let us move on to the heart of this section: the description of the algorithm
that the Consortium recommends for implementing these methods.


138
### Unicode and Bidirectionality
Here is the problem: we have a string of Unicode characters of which some belong to left-
to-right scripts, others to right-to-left scripts, and still others to all scripts (the space, the
period, etc.). This string will eventually be displayed or printed. And if it is long enough,
it will be broken into lines when it is rendered. Thus we face the same problem that ty-
pographers face: how to distribute the glyphs among lines so as to represent the structure
of the document as faithfully as possible while respecting the typographic conventions?
The reader may be surprised: why is Unicode suddenly concerned with the presentation
of the text? We are told over and over again that characters are superior to glyphs and
that Unicode, being interested only in abstract concepts, would never dirty its hands with
printer’s ink, even if that ink is virtual.
There is a kernel of truth to that. But at the same time, Unicode always strives to give
as much information as possible about its characters. We have seen, for example, that it
describes the contextual behavior of the Arabic characters so that software can perform a
contextual analysis on the sole basis of the information that Unicode has supplied. Thus
Unicode aims to provide software with the necessary information, even though it is not
going to talk typography or serve as a handbook for multilingual typesetting.
But there is an important reason for which Unicode concerns itself with presentation in
this way. In the previous section, we saw that presentation depends on the structure of the
document. But as long as there is no direct connection (wireless or otherwise) between
the computer and the human brain, no software will be able to detect the structure of
a document automatically and without error. We need a way to indicate this structure.
And that is why Unicode’s involvement is necessary: to give the user a way to specify
whether the text contains embedding or sequential blocks.
Unicode could have included one or two special characters to indicate embedding (with
sequential as the default choice) and leave it at that. But it preferred to address the prob-
lem fully—and that is a good thing, because otherwise what guarantee would there be
that a text rendered by this or that commercial or public-domain software package would
have the same structure?
Let us therefore explore this algorithm, which consists of six steps, each of them with
substeps:
1. Determine the default direction of the paragraph.
2. Process the Unicode characters that explicitly mark direction.
3. Process numbers and the surrounding characters.
4. Process neutral characters (spaces, quotation marks, etc.).
5. Make use of the inherent directionality of characters.
6. Reverse substrings as necessary.


139
Before attacking the ﬁrst step, we should see how Unicode categorizes characters accord-
ing to their bidirectional behavior.
Each Unicode character has a property called the bidirectional character type. This infor-
mation is found in the fourth ﬁeld (starting the count from zero) of the lines of the
ﬁle UnicodeData.txt. There are 19 character types of this kind, which fall into three
large groups: “strong”, “weak”, and “neutral”. “Strong” characters are those whose di-
rectionality is obvious and independent of context; “weak” characters are the numbers
and characters with similar behavior; “neutral” characters are those with no inherent
directionality, such as spaces and certain punctuation marks that are shared by many
scripts (e.g., the exclamation point).
Here are the 19 categories:
• Category L (“left-to-right”, strong): characters of the “strong” left-to-right type.
“Strength” refers to their determination: these characters are always set from left
to right, irrespective of context. They make up the absolute majority: 9,712 charac-
ters in the ﬁle UnicodeData.txt have this property, and the ideographs of planes
BMP and SIP are not taken into account.
• Category R (“right-to-left”, strong): the opposite of L, this category contains the char-
acters of the “strong” right-to-left type, except for the Arabic, Syriac, and Thaana
letters. Numbering 135, these characters are the Hebrew letters and the Cypriot sym-
bols.
• Category AL (“Arabic letter”, strong): the continuation of Category R; namely, the
Arabic, Syriac, and Thaana characters of the “strong” right-to-left type. There are 981
of them—a large number, because all the Arabic presentation ligatures are included.
• Category EN (“European number”, weak): the digits and “European-style” numerals.
A surprising fact is that the “Eastern Arabic-Indic digits” 95:;&lt;=&gt;6?, used in
Iran and India, are also included in this category. There are 161 numerals of this type.
• Category AN (“Arabic number”, weak): the “Arabic-style” numerals. There are
12 characters of this type: the 10 “Hindu-Arabic” digits 95:@AB>6?, the decimal
separator (C), and the thousands separator ( ’ ).
• Category ES (“European number separator”, weak): number separators—or, more
precisely, a separator, the slash. There are two characters in this category: the second
is again the slash, but its full-width version.
• Category ET (“European number terminator”, weak): a selection of characters that
are in no way extraterrestrial. These characters may follow a number and may be
considered to be part of it. Among them are the dollar sign, the percent sign, the
currency signs, the prime and its repeated forms, the plus and minus signs, etc. On
the other hand, neither the units of measure nor the numeric constants are in this
category. There are 63 ET characters.


140
• Category CS (“common number separator”, weak): the period, the comma, the
colon, and the no-break space, together with all their variants; that makes 11 char-
acters in all.
• Category BN (“boundary-neutral”, weak): the ASCII and ISO 1022 control charac-
ters, ZWJ and ZWNJ, the interlinear annotation marks, the language tags, etc. These
characters number 178.
• Category NSM (“nonspacing mark”, weak): the combining characters and the varia-
tion selectors, for a total of 803 characters.
• Category ON (“other neutral”, neutral): the universal punctuation marks, the proof-
reading symbols, the mathematical symbols, the pictograms, the box-drawing ele-
ments, the braille cells, the ideographic radicals—every character that has no inher-
ent directionality (although that is debatable for certain symbols). These are alto-
gether 3,007 characters.
• Category B (“paragraph separator”, neutral): every character that can separate para-
graphs, namely, the ASCII control characters 0x000A (line feed), 0x000D (carriage re-
turn), 0x001C, 0x001D, 0x001E, 0x0085, and the paragraph separator.
• Category S (“segment separator”, neutral): the tab characters (0x0009, 0x000B,
0x001F);
• Category WS (“whitespace”, neutral): the whitespace. Every character that is consid-
ered a space of nonzero width. There are 19 characters of this type.
The ﬁve remaining categories are actually ﬁve Unicode control characters that appear in
the block of general punctuation:
• 0x202A left-to-right embedding (LRE), marks the beginning of the embedding of
left-to-right text.
• 0x202B right-to-left embedding (RLE), marks the beginning of the embedding of
right-to-left text.
• 0x202C pop directional formatting, or “PDF” (not to be confused with the PDF
ﬁle format of Adobe’s Acrobat software). States form a stack, and each of the charac-
ters LRE, RLE, LRO, and RLO adds to the stack a new state, whether for embedding
or for explicit direction. The character PDF pops the top state oﬀthe stack.
• 0x202D left-to-right override (LRO), forces the direction to be left-to-right.
• 0x202E right-to-left override (RLO), forces the direction to be right-to-left.
The bidirectional algorithm automatically manages embedding, but the characters LRE
and RLE allow us to switch to “manual control” when errors occur. Manual control en-
ables us to do even more, since with the characters LRO and RLO we enjoy low-level


141
control over the behavior of the glyphs representing the characters with respect to the
direction of the script. Thus we can torture Unicode characters at will by forcing a Latin
text to run from right to left or an Arabic text to run from left to right. But these charac-
ters should be used only when absolutely necessary. Let us not forget that the interactive
use of software and the transmission of data are ill suited to “modes”, and modes are
indeed what these characters represent. Suppose that we have placed the character LRE
at the beginning of a paragraph and that we copy a few words to another document. The
eﬀect of the LRE will disappear, since the character will not be copied with our string.
Use your judgment, and be careful!
Let us also point out that the scope of all these characters is limited to a single paragraph
(a paragraph being a block of data that ends at the end of the ﬁle or at a character of
category B). At the end of the paragraph, however many states may have accumulated
on the stack, they are all swallowed up by the dreaded cyber-sinkhole that lies within
every computer (the place where ﬁles that we have accidentally deleted without keeping
a backup end up).
The characters that we have just described are also listed in the ﬁle PropList.txt under
the property Bidi_Control.
This ﬁle also mentions characters that we have not yet discussed, the implicit directional
marks:
• 0x200E left-to-right mark (LRM): an invisible character of zero width whose only
raison d’être is its category, L.
• 0x200F right-to-left mark (RLM): as above, but of category R.
What good are these invisible, zero-width characters? They can be used, for example,
to lead the rendering engine to believe that the text begins with a character of a given
direction—in other words, to cheat!
Finally, one other important property of characters is the possibility of mirroring. The
ninth ﬁeld (counting from zero) in the lines of the ﬁle UnicodeData.txt contains a ‘Y’
when the glyph should be mirrored in a right-to-left context. Thus an “opening” paren-
thesis will remain an opening parenthesis in a left-to-right context; it will be a “right”
parenthesis in absolute terms, but we do “open” a right-to-left passage at the right.
Mirroring is ordinarily managed by the rendering engine. But Unicode, through its in-
ﬁnite mercy, has also given us a list of characters whose glyphs can serve as mirrored
glyphs. These data are included in the ﬁle BidiMirroring.txt, a sample of which appears
below:
0028; 0029 # LEFT PARENTHESIS
0029; 0028 # RIGHT PARENTHESIS
003C; 003E # LESS-THAN SIGN
003E; 003C # GREATER-THAN SIGN
005B; 005D # LEFT SQUARE BRACKET
005D; 005B # RIGHT SQUARE BRACKET


142
As we can see, for each original character at the left, Unicode provides a character whose
glyph is the mirror image of the original. There are 320 pairs of characters of this kind in
the ﬁle, some of which are marked [BEST FIT], which means that merely ﬂipping them
horizontally does not yield the best result. Most of these characters are mathematical
symbols, and we can indeed wonder what the ideal mirrored version of ‘¯’, for example,
would be. Should it be ‘˘’ or ‘˙’? The former is exactly what we would write in a left-
to-right document. In Western mathematics, the negating stroke is always slanted to the
right.
Is ‘˙’, then, the ideal form for right-to-left mathematics? Azzeddine Lazrek [229, 230]
seems to prefer ‘˘’, which we could accuse of left-to-right bias. Arabian mathematics uses
an unusual system of notation that yields formulae such as the following:
The Algorithm, Step by Step
We start with a string C = c1c2 ...cn, and the object of the game is to obtain, for each
character ci, the value ˚i of its “embedding level”, a value that we shall use at the end to
rearrange the glyphs.
1. Determine the implicit direction of the paragraph
We shall ﬁrst break the document into paragraphs. Each paragraph will have an implicit
direction. If this direction is not given by any higher-level protocol (XML, XSL-FO, etc.),
the algorithm will look for the ﬁrst character of category L, AL, or R. If this character is
of category L, the implicit direction of the paragraph is from left to right; otherwise, the
implicit direction is from right to left.
Now suppose that we are in a left-to-right document (such as this book) and that, un-
fortunately, a paragraph begins with a word in Hebrew. According to the algorithm, this
paragraph will begin at the right, and the last line will run short at the left. How can we
avoid that situation? That is where the implicit directional marks come in. All that we
have to do is to place the character LRM at the beginning of the paragraph. This character
will lead the algorithm to believe that the ﬁrst letter of the paragraph is of category L,
and the formatting will be correct.
To calculate the values of ˚, we need an initial value. This will be the “paragraph em-
bedding level”, ¸. If the paragraph’s direction is from right to left, then ¸ = 1; otherwise,
¸ = 0.
2. Process the control characters for bidirectionality
In this step, we shall collect and use the data provided by the various characters LRE, RLE,
LRO, RLO, and PDF that may be found in the document. We shall examine characters
one by one and calculate for each character the embedding-level value ˚ and the explicit
direction.


143
We begin with the ﬁrst character by taking ˚1 = ¸ as the initial value and not specify-
ing any explicit direction. If we come upon the character RLE, then the value ˚ for the
following characters will be increased by one or two units so as to yield an odd number.
Likewise, if we come upon LRE, the value ˚ for the following characters will be increased
by one or two so as to yield an even number.
If we ﬁnd RLO or LRO, our behavior is similar, but in addition the explicit direction of
the following characters will be right-to-left or left-to-right, respectively. In other words,
the characters aﬀected by RLO are considered to be of category R, and those aﬀected by
LRO are of category L.
LRE, RLE, LRO, and RLO are placed onto a stack. Each new operator of this type will
push the previous one further down the stack, where it waits to be popped oﬀ. When
we come upon a PDF, we pop the most recent LRE, RLE, LRO, or RLO. Note that this
stack has a height of 61: when the 62d successive operator is reached, the algorithm stops
keeping track of the oldest characters.
At the start of this procedure, we have a value ˚ for each character in the string. Thus we
can restrict the remaining operations to substrings of characters having the same value
of ˚. We call that type of substring a run. A run is thus a substring of characters with the
same value of ˚.
For each run S, we shall deﬁne two variables, Ss and Se, which correspond to the condi-
tions at its endpoints. These variables can assume the values ‘L’ for left-to-right and ‘R’
for right-to-left; these are also the names of the categories L and R.
Here is how we deﬁne these variables. Let S′,S,S′′ be three consecutive runs and
˚′,˚,˚′′ their embedding levels. Then Ss has the value R if max(˚′,˚) is odd and
the value L otherwise. Similarly, Se is R if max(˚,˚′′) is odd, otherwise L.
If S appears at the beginning or the end of the paragraph—and thus there is no S′
(or S′′)—we take ¸ instead of ˚′ (or ˚′′).
The ﬁnal operation: delete all occurrences of RLE, LRE, RLO, LRO, and PDF.
Let us review the process. We break our paragraph into runs S, the elements of a run all
having the same value ˚. For each run, we have the variables Ss and Se, whose values
may be L or R.
3. Process the numbers and the surrounding characters
Steps 3, 4, and 5 are, in a sense, intermediate steps. We process three special types of
characters and change their categories, and possibly their ˚ values, according to context.
In this section, we shall process numbers. There are two categories of numbers: EN (“Eu-
ropean numbers”) and AN (“Arabic numbers”). The names of these categories should
not be taken literally, as the categories serve only to indicate a certain type of behavior.
Suppose we ﬁnd ourselves in a run S with embedding level ˚. We shall begin a ballet of
changing categories.


144
First of all, every NSM character (combining character) assumes the category of its base
character; if there is none (so that the character is necessarily at the beginning of the run),
it assumes the value of Ss as its category.
Next, we shall consider the EN characters (European numbers) in the run. For each of
them, we shall check whether the ﬁrst strong character as we read leftward is of type AL.
If it is, the EN becomes an AN.
Now the distinction between right-to-left Arabic characters (AL) and Hebrew characters
(R) is no longer needed; therefore, we convert the AL characters to type R.
Now we shall address the characters of type ET (ﬁnal punctuation), ES (slash), or CS
(period, comma, etc.). An ES between two ENs becomes an EN. A CS between two ENs
becomes an EN. A CS between two ANs becomes an AN. A series of ETs before or after
an EN becomes a series of ENs.
After these transformations, if any ETs, ESs, or CSs remain, we convert them all to ONs
(harmless neutral characters).
Finally, in the last transformation of this step, we search backwards from each EN for the
ﬁrst strong character. If it is an L, we convert the EN to an L.
By the end of this step, we have separated the EN and AN numbers, and we have elimi-
nated the categories ET, ES, and CS.
4. Process the neutral characters
And, in particular, process the spaces. This step is necessary because Unicode decided not
to “directionalize” its spaces, as Apple did in its Arabic system, in which one copy of the
ASCII table worked from right to left. Thus Mac OS had a left-to-right space and a right-
to-left space.
Here it is the algorithm that determines the direction of the spaces. The goal of this sec-
tion is therefore to assign a category, either L or R, to each neutral character. Two very
simple rules suﬃce.
1. If the neutral character is surrounded by strong characters of a single category, it also
is of that category; if it appears at the beginning or at the end of run S, we treat it as if
there were a strong character of category Ss at its left or a strong character of category Se
at its right, respectively.
2. All other neutral characters are of category ¸.
5. Make use of the inherent directionality of the characters
Up to now, we have dealt only with speciﬁc cases (numbers, neutral characters) and some
special characters (RLE and company). But the reader must certainly have noticed that
we have not yet raised the issue of the category of each character cn. Yet we shall have to
use this category (L or R) as the basis of our decision to set the text from right to left or
from left to right. Now is the time to take the category of the characters into account.
But nor should we forget what has been done in the preceding procedures, even if they
are less common and deal primarily with exceptional cases. Here is where we see the


145
strength of the algorithm: all that we have to do is increment ˚ in a certain way, and we
obtain values that take both the preceding calculations and the inherent directionality
of the characters into account.
Here are the procedures to carry out:
• For each character of category L: if its ˚ is odd, increment it by 1;
• For each R: if its ˚ is even, increment it by 1;
• For each AN: if its ˚ is odd, increment it by 2; else increment it by 1;
• For each EN: if its ˚ is even, increment it by 2; else increment it by 1.
At the end of this step, we have a deﬁnitive value of ˚ for each character in the string.
6. Reverse substrings
This section is the most fun. We have weighted the characters in our string with whole
numbers (the values of ˚). Beginning with the largest number, we shall reverse all the
runs that have this value of ˚. Then we shall do the same for the number immediately
below, until we reach an embedding level of 0. If the largest level ˚ is n, then some
substrings (those for which ˚ is equal to n) will be reversed.
Here are a few examples to shed light on the procedure. Let us take three speakers:
R and R′ are speakers of right-to-left languages, and L is a speaker of a left-to-right lan-
guage.
First example: L says that “−−−−−−−−−−→
Yes means ←−
yes.” (“Yes means D0 .”). We have a single right-
to-left word in a left-to-right context.
After running the string through the bidirectional algorithm, we obtain the following
embedding levels ˚:
[0Yes means [1yes]1.]0
The inherent directionality of the letters is enough to yield the desired result. We have
only one reversal to perform, that of level 1:
[0Yes means [1sey]1.]0
Second example: R says “←−−−−−−−−−
−→
yes means yes”.
Then L quotes him by saying “
−−−−−−−−−−−−−−−−−−−→
R said that ‘←−−−−−−−−−
−→
yes means yes’.” (“He said that ‘D0E DF

yes’.”). Thus we have right-to-left embedding in a left-to-right passage.
But if we leave the algorithm to do its work unassisted, it will yield undesired results. By
merely reading “He said that ‘yes ... ”, the algorithm cannot know that the word “yes”
is part of a right-to-left quotation. Thus we shall use a pair of characters, ˝ and ˇ, to
indicate the quotation’s boundaries:


146
[0He said that “˝[1[2yes]2 means yes]1ˇ”.]0
The ﬁrst reversal to carry out is at level 2:
[0He said that “˝[1[2sey]2 means yes]1ˇ”.]0
The second reversal will be at level 1 (thus we remove ˝ and ˇ):
[0He said that “[1sey snaem [2yes]2]1”.]0
Third example: R′ hears L quote R and asks him:
“
←−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−−
Did you say that ‘
−−−−−−−−−−−−−−−−−−−→
R said that “←−−−−−−−−−
−→
yes means yes” ’?” (“G“He said that ‘D0EDF
 yes’ ”HI”).
We have surrounded the entire previous sentence with the question “Did you say that”
and a question mark ‘?’. And since R′ is right-to-left, we are in that context from the very
beginning; i.e., the embedding level ˚ of the ﬁrst character already has the value of 1.
Once again the algorithm cannot know that “He said ... ” is embedded; therefore, we
shall mark the fact with the pair ˛, ˇ. Here is the situation:
[1Did you say that “˛[2He said that ‘˝[3[4yes]4 means yes]3ˇ’]2ˇ”?]1
Thus we have reached embedding level 4! Let us carry out the reversal at level 4:
[1Did you say that “˛[2He said that ‘˝[3[4sey]4 means yes]3ˇ’]2ˇ”?]1
Next, we shall reverse level 3:
[1Did you say that “˛[2He said that ‘[3sey snaem [4yes]4]3’]2ˇ”?]1
And level 2:
[1Did you say that “[2‘[4sey]4 [3means yes]3’ taht dias eH]2”?]1
Finally, we reverse level 1, the global level:
[1?“[2He said that ‘[3sey snaem [4yes]4]3’]2” taht yas uoy diDE]1
The three great nations of East Asia (China, Japan, Korea) have writing systems that pose
challenges to computer science. In this section, we shall discuss two of these writing sys-
tems: the ideographs of Chinese origin that were also adopted by the Japanese and the
Koreans, and the Korean syllabic hangul script.


147
### Ideographs of Chinese Origin
Westerners must put forth an enormous eﬀort to learn Chinese ideographs: there are
thousands of them, and they all look similar—at least that is the impression that we have
at ﬁrst. We can easily be discouraged by the thought that even if we managed to learn
3,000, 4,000, or 5,000 ideographs there would still be more than 60,000 others that we
had not even touched upon, and life is so short. But do we know all the words in our own
language? Certainly not! Are we discouraged by that fact? The author is not ashamed of
his ignorance of the words “gallimaufry”, “jecorary”, “frondescent”2, and many others.
The same goes for the East Asian who comes across an ideograph that he does not recog-
nize. The only diﬀerence is that we can usually pronounce words that we do not know,
whereas the East Asian cannot do so with an unknown character. On the other hand, he is
better equipped to understand its meaning. We require a solid knowledge of etymology
in order to interpret a word; he, however, has a better chance of correctly interpreting
an ideograph if he can recognize the radicals from which it is constructed.
Etymology for us, radicals for the East Asians. Two ways of investigating the possible
meaning of a word/ideograph. They are similar, from a human perspective. But what
is a computer to make of them?
When we operate on a phonetic basis, we lose the pictorial representation of mean-
ing, but we gain the possibility of segmenting: sounds can be separated, and all that we
have to do is invent signs to represent them. That is what the alphabetic and syllabic
writing systems do. Gutenberg used segmenting into symbols to good advantage in his
invention, and computer science inherited it from him. Result: a few dozen symbols are
enough to write the hundreds of thousands of English words. Most important of all,
these symbols will suﬃce for all future words as well: neologisms, loan words, etc.
That is not the case for the ideographs. Generating them from radicals in real time is not
a solution: sometimes we do not know which radicals are needed, or else they transform
themselves to yield new shapes. This is not a process that lends itself to automation; at
least no one has yet succeeded at automating it.
There have been attempts to “rationalize” the ideographs: graphical syntaxes by them-
selves [125] or accompanied by tools for generating ideographs [356], or highly parame-
terized METAFONT code [178]. One of these attempts is Character Description Language,
an approach based on XML that we shall describe on page 151.
In the absence of “intelligent” systems that oﬀer a functional solution for all data ex-
changed in China, Japan, and Korea, the Chinese ideographs have been “hardcoded”;
i.e., one code point is assigned to each ideograph. We have discussed various East Asian
encodings (pages 1 and following) that reached the record number of 48,027 ideographs.
These encodings were adequate as long as data remained within each country. But when
we began to exchange information across borders, if only by creating web pages, a new
sort of problem arose: compatibility among Chinese, Japanese, and Korean ideographs.
2 In order: “a hotchpotch”, “relating to the liver”, “covered with leaves”.


148
The Greeks borrowed the writing system of the Phoenicians; then the Romans borrowed
theirs from the Greeks. The writing system changed each time, although the similar-
ities are astonishing. The same phenomenon appeared among the Chinese, Japanese,
and Koreans—in the third century C.E. for the Japanese, in the ﬁfth century C.E. for
the Koreans. The Chinese script was exported and adapted to the needs of each nation.
New ideographs were created, others changed their meaning; some even changed their
forms slightly. Often the diﬀerences are minimal, even imperceptible to the Western eye,
which may recognize that a text is in Japanese or Korean solely by the presence of kana
or hangul.
Indeed, these scripts (kana in Japan, hangul in Korea) were attempts to rationalize the
Chinese writing system. But the goal was never to replace it, only to supplement it with
a phonetic adjunct. Which means that these countries have two scripts (as well as the
Latin script) in parallel.
Unicode and ideographs
While ISO 10646 originally intended to use separate planes for the ideographs of these
three languages, Unicode took up the challenge of unifying the ideographs.
Three principles were adopted as a basis of this uniﬁcation:
1. The principle of source separation: if two ideographs occupy distinct positions in a
single encoding, they are not uniﬁed within Unicode.
2. The noncognate rule: if two ideographs are etymologically diﬀerent—i.e., if they are
historically derived from diﬀerent ideographs, they are not uniﬁed within Unicode.
3. If two ideographs that do not satisfy the two previous conditions have the same ab-
stract shape, they are uniﬁed.
The ﬁrst of these principles was highly controversial, but it is consistent with Unicode’s
general principle of convertibility (see page 61), which provides that all data encoded
in a recognized encoding can be converted to Unicode without loss of information. The
typical example of ideographs that have not been uniﬁed for this reason is the series of six
ideographs 剣劍剱劔劒釼, all of which mean “sword” and are clearly graphical variants
of one another. Since they are distinct in JIS X 0208, they are distinct in Unicode as well.
The second principle leaves the door wide open to polemics among historians of the
ideographs; nonetheless, it is indispensable. The most commonly cited example is doubt-
less that of the radicals ‘土’ and ‘士’: the former means “ground, earth, soil”; the latter
means “samurai, gentleman, scholar”. There are even characters that contain both of
these radicals, such as 擡(“pick up, raise”).
The third principle is where things really go wrong. The concept of an abstract shape is,
unfortunately, not clear in the slightest and depends primarily on the individual’s intu-
ition.
The Unicode book gives a certain number of examples of uniﬁed and nonuniﬁed
ideographs. In these examples, the pairs of nonuniﬁed ideographs clearly consist of


149
two diﬀerent characters, but the pairs of uniﬁed ideographs are very interesting because
they show us how much tolerance uniﬁcation exhibits towards diﬀerences that may seem
signiﬁcant at ﬁrst glance.
The examples range from the almost identical to the discernibly diﬀerent. The diﬀerence
between · and ‚ is the order in which the strokes are written; in the bottom part of
„ (vs. ‰), the middle stroke protrudes slightly; likewise, in the bottom part of Â, the
stroke in the middle extends for the whole width of the rectangle, which is not the case
in Ê; the contents of the rectangle in È and Í are quite diﬀerent; the vertical stroke
in Î and Ï has a diﬀerent ending; the stroke at the left of Ì has a lead-in element,
unlike that of Ó; the right-hand stroke is smooth in Ô and angular in ; the upper
right-hand parts of Ò and Ú are quite diﬀerent. Yet all these pairs of ideographs were
uniﬁed and yield only a single character each.
Be that as it may, the ideographs of 38 national or industrial encodings were collected,
compared, analyzed, and sorted according to four large dictionaries (two of them Chi-
nese, one Japanese, and one Korean)—a large-scale project. And that was only the be-
ginning, as other blocks of ideographic characters were added in the following versions
of Unicode. Today there are 71,233 uniﬁed characters.
The Unihan database
As always, Unicode does not stop with the already abundant information found in the
Unicode book. The consortium also provides a database of the ideographs, which is con-
tained in the following ﬁle:
ftp://ftp.unicode.org/Public/UNIDATA/Unihan.zip
as well as a web interface for searches (in which we may enter a character’s hexadecimal
code point, or even the character itself in UTF-8):
http://www.unicode.org/charts/unihan.html
Nine types of data are provided:
• numeric value: if the character is used as a number, including the special use of cer-
tain characters for accounting purposes.
• variants: whether there are other characters that are semantic variants (characters
with more or less the same meaning that can be used in the place of the character in
question); whether there is a simpliﬁed Chinese version of the character; whether
there are semantic variants in specialized contexts; whether there is a traditional
Chinese version; whether there are presentation variants (for example, two of the
“swords” shown above, namely 剑and 劍, are presentation variants).
• the number of strokes, calculated according to six diﬀerent methods: Unicode’s
method, the traditional Japanese method, the method of Morohashi’s dictionary,
the method of the prestigious Kangxi dictionary of the Chinese language, the Korean
method, and the total number of strokes, including those of the radical.


150
• pronunciations: in Cantonese Chinese, in Mandarin Chinese, in the ancient Chinese
of the Tang dynasty, in Japanese (both kun pronunciations, of Japanese origin, and
on pronunciations, borrowed from Chinese together with the character), in Korean,
in Vietnamese.
• the deﬁnition.
• the frequency of use in Chinese discussion groups.
• the level of diﬃculty, according to the school system in Hong Kong.
• indexes in 22 diﬀerent dictionaries.
• code points in 32 diﬀerent encodings.
Web access to this database is connected to searches in the Japanese EDICT dictionaries
[90]. In this way, we also obtain for character its meanings in Japanese as well as a list
of all the compound words (indivisible groups of ideographs) that contain it, with their
pronunciations.
This enormous mass of data is collected in a 25 MB ﬁle that is available for downloading
as a ZIP archive.
What shall we do when 71,233 ideographs are not enough?
Unlike our ﬁne old Latin letters, which have not changed much since Julius Caesar, the
Chinese ideographs display an almost biological behavior: they live and die, merge, re-
produce, form societies—societies similar to human societies, as an ideograph is often
created for use in a child’s name, and the popularity of the ideograph will thus be related
to that of its human bearer. Be that as it may, one thing is certain: they present problems
for computer science. How to manage a writing system that changes every day?
First of all, let us mention two methods that do not really oﬀer a solution to the problem
of missing characters. The ﬁrst is the method of throwing up our hands: the glyph—or
even the character—that we need is not available, so we decide to replace it with a symbol
provided for this purpose, the character 0x3013 geta mark 〓. It has the special quality
of having a glyph that stands out in text. In traditional printing, the geta mark was a sort
of substitute, used in ﬁrst and second proofs, that was not supposed to appear in the ﬁnal
printing. It was used until the punch-cutter had the time to design and cut the missing
glyph. Its glyph was made deliberately conspicuous so that it would be easy to ﬁnd and
correct—and, most of all, so that it would not be overlooked during proofreading.
Another possibility: 0x303E ideographic variation indicator .. The idea is that the
following character is an approximation of the character that was intended. Thus, if we
ﬁnd a character that resembles the missing one, we can substitute that character without
running the risk of being a laughing stock. The ideographic variation indicator bears all
the following meanings at the same time: “don’t be surprised if what you are reading
doesn’t make any sense”, “I know that this is not the right character, but I haven’t found


151
anything better”, “this is what the missing character looks like; unless you are extremely
stupid, context should enable you to ﬁgure it out”.
These two solutions are not solutions at all. If we have enough time and energy, we can
design the missing glyphs. Chapter 12 of this book is devoted to that very subject. But
designing the glyph is not enough: we also have to insert it into fonts, install those fonts
on the computer, make sure that they are displayed and printed correctly, send them to
all our associates, or even distribute them on the Internet with instructions for installa-
tion. It is a ﬁery ordeal that we might not wish to endure just for one or two characters.
Below, we shall see two solutions that fall between these extremes. They are attempts to
describe the ideographs by combining other ideographs or elemental strokes—attempts
whose aim is to provide the user with a rapid and eﬃcient way to obtain and use the new
ideographs that are being created just as the reader is reading these lines, or, conversely,
old ideographs that the most ancient of the ancient sages forgot many centuries ago.
Ideographic description characters
The ﬁrst attempt is simplistic but nonetheless powerful. And it lies at the very heart of
Unicode. It is a set of a dozen characters (0x2FF0-0x2FFB) called ideographic description
characters.
The goal is to describe ideographic characters without actually displaying them. That is
one of the many paradoxes of Unicode: all the combinations of ideographs that we shall
see in this section are in fact created in the mind of the reader, just as the reader who sees
the characters :-) in an email message immediately recognizes them as the smiley (²).
Let us also note that these characters “operate” on the two or three characters that follow
them (whereas combining characters operate on the preceding characters).
Here are the graphical representations of these control characters. In themselves, they
give a good idea of the possibilities for combining characters that are available to us:
‘ ’ ÷ ◊ÿ Ÿ ⁄ € ‹ › ﬁﬂ
When we begin to combine the operators themselves,3 we acquire an impressive power
to describe characters. Thus we can write several operators in a row: each of them will
wait until the following ones have performed their tasks before beginning to perform
its own.
A few simple examples:
‘女壬(woman + ninth month) yields妊(pregnancy)
’宀女(roof + woman) yields安(tranquillity)
3 There is only one restriction: the entire string of ideographs and description characters must not exceed
16 Unicode characters and must not contain more than six consecutive ideographs.


152
ÿ囗大(box + large) yields因(cause)
ﬁ辶巛(walking + river) yields 巡(patrol)
And a few examples with compounding:
‘女’女女(woman + woman + woman) yields姦(noise)
‹广’‘木木手(cliﬀ+ large + large + hand) yields摩(polish)
But one must be very careful, as a radical can change its shape in combination. For exam-
ple, the radical for “water” (水) assumes the shape 氵when it is combined horizontally
with other radicals. We can thus have combinations of this kind:
‘水中(sea + center) yields沖(in the open sea)
’隹火(old bird + ﬁre) yields焦(impatience)
In fact, we can freely combine ideographs, radicals (0x2F00-0x2FD5), and characters from
the block of supplementary radicals (0x2E80-0x2EF3). The supplementary radicals are
characters that represent the diﬀerent shapes that a radical can assume when it is com-
bined with other ideographs. Normally neither the radicals nor the supplementary rad-
icals should be used as ordinary characters in a document; they should be reserved for
cases in which we are referring speciﬁcally to the ideographic radical, not to the character.
Example: 0x706B 火is an ideographic character that means “ﬁre” but also “Tuesday”,
“March”, “ﬂame”, “heat”; 0x2F55 kangxi radical ﬁre 火(same glyph) is radical num-
ber 86, “ﬁre”; 0x2EA3 cjk radical ﬁre 灬is the shape that this radical assumes when
it is combined with other ideographs. We would use the ﬁrst of these characters in a
document that mentioned ﬁre; the second, in a dictionary that listed the radicals or in
a document that referred to the radical for ﬁre (to explain another ideograph, for exam-
ple); the third, in a textbook on writing in which it is explained that the radical for ﬁre
assumes a special shape under certain conditions.
Before concluding this section, let us note that, although Unicode’s method of ideo-
graphic description seems ﬁne on paper, the challenge that software faces to combine the
glyphs correctly is not negligible. That is why Unicode decided not to require Unicode-
compatible software to combine the glyphs in reality, which is a great shame.
If we wish to avoid the ideographic description characters and produce glyphs of high
quality, we may as well put a shoulder to the grindstone and combine the glyphs of a
speciﬁc font by using font-design software such as FontLab or FontForge, which we shall
describe in Chapter 12—provided, of course, that our license to use the font allows us to
do so.
But let us move on to the second attempt to describe ideographs, the CDL markup
system.


153
### CDL, or How to Describe Ideographs in XML
In the 1980s, Tom Bishop, a Chinese-speaking American, developed some software for
learning the Chinese language that had a very interesting property: a window that
showed how a Chinese character was written, stroke by stroke, in slow motion. To
describe the characters, Tom developed an internal language. Later, in view of the
astounding success of XML, he took up the principles of this language again and created
an XML-based method for describing ideographs.
It is Character Description Language (CDL) [79, 80], which has been submitted to the
Unicode Technical Committee and the Ideographic Rapporteur Group (IRG) for ratiﬁ-
cation.
The approach is twofold: we can build up an ideograph from other ideographs. For that
purpose, we need only the ideographs’ Unicode code points and the coordinates of their
graphical frames. For example, to obtain L (which is a radical, but that fact is of no
consequence here), it is suﬃcient to combine K and E, both of which are in Unicode.
Thus we write:
&lt;cdl char="L"&gt;
&lt;comp char="K" points="0,0 40,128"/&gt;
&lt;comp char="E" points="60,12 128,128"/&gt;
&lt;/cdl&gt;
The values of the arguments to char are Unicode characters in UTF-8.
We can also construct an ideograph from strokes. Here is how to obtain the ideograph K:
&lt;cdl char="K"&gt;
&lt;stroke type="p" points="107,0 10,46"/&gt;
&lt;stroke type="p" points="128,38 0,83"/&gt;
&lt;stroke type="s" points="86,70 86,128"/&gt;
&lt;/cdl&gt;
Finally, we can combine the two methods. To obtain ”, we can write:
&lt;cdl char="”"&gt;
&lt;comp char="P" points="0,0 40,128"/&gt;
&lt;stroke type="d" points="45,104 66,128"/&gt;
&lt;/cdl&gt;
The possibility of directly using the glyphs of Unicode characters is nothing but a façade:
in fact, 56,000 characters have already been described in this way, and the value of a char
attribute refers the rendering engine to this sort of description, which in turn may refer
it to other descriptions, and so on, until nothing but basic strokes remain.
The basic strokes number 39. Here is the full list. (The abbreviations are the codes used
as values of the type attribute of element stroke.)



### Table of CDL Basic Strokes

In Character Description Language (CDL), ideographs are decomposed into basic calligraphic strokes. The complete inventory of 42 basic strokes, their stroke names in Pinyin, abbreviations, and sample occurrences are presented in the following plates:

![Plate 4-1: CDL Stroke Classification Table — Strokes 1 to 29 (p. 154)](/images/fonts-encodings/plate4-1.png)



![Plate 4-2: CDL Stroke Classification Table — Strokes 30 to 42 (p. 155)](/images/fonts-encodings/plate4-2.png)

The reader will notice that certain words are repeated in the Chinese names of these strokes. They are basic stroke types: *héng* (horizontal), *shù* (vertical), *piě* (slash/fall left), *nà* (press down/fall right), *diǎn* (dot), *tí* (rise), *zhé* (fold/bend), *gōu* (hook), *wān* (curve), and *quān* (circle).


156
After four years of work, the commission presented to the king a writing system made up
of 11 vowels and 17 consonants that was perfectly suited to the needs of the Korean lan-
guage. It was oﬃcially ratiﬁed in 1446. In the beginning, it was called “vulgar script”,
“the script that can be learned in one morning”, and “women’s writing”. Only in the
nineteenth century did it receive the name hangul (“large script”). In other words, the
upper classes in Korean society looked down upon this script for centuries.
While Gutenberg was getting ready to print his Bibles, the ﬁrst book in hangul appeared:
Songs of the Dragons Flying to Heaven, by Jeong Inji (1447), typeset on wooden boards. It
was followed by Songs of the Moon Shining on a Thousand Rivers, which was written by the
king himself, and then by a Buddhist sutra in 1449. Thus begins the story of the script
that many linguists consider to be the most perfectly conceived script in the history of
the world.4
The shapes of the hangul consonants were established according to the positions of the
vocal organs. They are distributed among ﬁve phonetic categories built up by adding one
or more strokes to indicate phonetic features:
![Figure 4-7: Hangul Consonants — Articulatory Geometric Design](/images/fonts-encodings/fig4-7.png)
Among the consonants, ‘ᄋ’ plays the role of a placeholder for an independent vowel, or
produces an ‘ng’ sound at the end of a syllable.
The vowels are based on the four elements of East Asian philosophy: heaven (a short
stroke), earth (a horizontal stroke), man (a vertical line), and the yin–yang circle (in
evidence from the cyclical pattern that the forms of the vowels follow):
![Figure 4-8: Hangul Vowels — Trinitarian Philosophical Design (Heaven, Earth, Man)](/images/fonts-encodings/fig4-8.png)
The reader will note that we have chosen to entitle this section “The Syllabic Korean
Hangul Script”, whereas here we can see nothing but letters (consonants and vowels). In-
deed, the signs that we have just described, which are called jamo, are merely the building
blocks of the hangul system. By combining jamo within an ideographic square, we obtain
the hangul syllables.
A hangul syllable consists of one or more initial consonants (choseong), one or more
vowels (jungseong), and possibly one or more ﬁnal consonants (jongseong). There are
19 possible initial consonants, 21 possible vowels or combinations of vowels, and 26 pos-
sible ﬁnal consonants or combinations of ﬁnal consonants.
4 For more information on its history, please consult [287].


157
If we use I for initial consonants, V for vowels, and F for ﬁnal consonants, we have as the
general form of a hangul syllable the expression I+V +F∗(in which we employ the nota-
tion for regular expressions: + for “one or more times” and ∗for “zero or more times”).
To encode a syllable of this kind, Unicode oﬀers us two possibilities: we can look up the
corresponding character in the block of precomposed hangul syllables (0xAC00-0xD7A3),
or we can enter the corresponding jamo, which the rendering engine will combine into
a hangul syllable.
These two methods are equivalent, and the choice of one or the other is analogous to
the choice in the Latin script between precomposed accented letters and those obtained
using combining characters. The jamo of Unicode (0x1100-0x11F9) do not have the status
of combining characters, for the simple reason that their logic is diﬀerent: rather than
combining with a base character, they combine with one another.
But let us return to the general expression of a hangul syllable, H = I+V +F∗, and suppose
that we have two hangul syllables H and H′, the latter coming immediately after the
former. Their decomposition is therefore HH′ = I+V +F∗I′+V ′+F′∗. The sharp reader is
bound to ask one burning question: F and I being both consonants, how do we distin-
guish the ﬁnal consonants of H from the initial ones of H′?
Sophisticated linguistic processing could certainly do the job, but here we need to enter
characters in real time and see them transformed into syllables. Therefore a cumbersome
or ambiguous approach is out of the question.
What, then, shall we do? There is only one solution, which may seem awkward at ﬁrst
because it entails redundant code points in Unicode: we double the Unicode consonants
and thus create an artiﬁcial distinction between initial and ﬁnal forms. It is as if we had
two copies of each of the consonants of English and wrote “afﬁrmation” (with the “ﬁnal”
consonants in bold) to show that the word breaks down into syllables as “af-ﬁr-ma-tion”.
In addition, this is the technique that the encoding Johab (which allows only one letter
from each category) already used: ﬁve bits for the initial consonant, ﬁve for the vowel,
ﬁve for the ﬁnal consonant, plus one disabled bit, which gives 16 bits in all and is a very
practical approach.
Thus the table of jamo contains ﬁrst the initial consonants 0x1100-1159, then the vowels
0x1160-0x11A2, and at last the ﬁnal consonants 0x11A8-0x11F9, whose glyphs are identi-
cal to those of the initial consonants. The character 0x115F hangul choseong ﬁller is a
control character that marks the absence of an initial consonant, which may be needed in
irregularly constructed syllables; likewise, there is a 0x1160 hangul jungseong ﬁller,
used when the vowel is missing.
There are six ways to combine jamo in order to form hangul syllables. To describe them,
we shall distinguish the horizontal vowels (Ih) from the vertical ones (Iv):
IVv &, IVh ', IVhVv (, IVvF ), IVhF *, IVhVvF +.
Here is an example: the jamo sequence 한is of the shape IVvF; therefore, we take
the combination ) and get 한. Similarly, the sequence 글is of the shape IVhF;


158
therefore, we take the combination * and get 글. We have here the form of the word
“hangul”: 한글.
Syllables are constructed with unprecedented mathematical rigor. The same is true of
their encoding. To obtain 한, we used the Unicode jamo characters 0x1112, 0x1161,
0x11AB. Where, then, does the syllable 한appear in the encoding? The computer can
answer the question in a few microseconds, as it has only to carry out the following
computation:

(I −0x1100)×21

+(V −0x1161)

×28+(F −0x11A7)+0xAC00
(where I, V, F are the Unicode code points of the jamo).
When a syllable has no ﬁnal consonant F, the formula is simpler:

(I −0x1100)×21

+(V −0x1161)

×28+0xAC00
Unlike the ideographs, the Unicode characters for syllables that are constructed in this
manner do have names. These names are formed from the letters associated with the
jamo in the tables on page 156. The letters associated with 한글are “han” and “geur”;
thus the names of the Unicode characters are 0xD55C hangul syllable han and 0xAE00
hangul syllable geur. The names of the jamo can be found in the ﬁle Jamo.txt.
Another interesting ﬁle is HangulSyllableType.txt: it gives the type of each hangul syl-
lable (IV or IVF).
When the initial consonant or the vowel is missing, or when we have more than one
initial consonant and/or more than two vowels and/or more than one ﬁnal consonant,
no precomposed syllable is available, and we must resort to the automatic combination
of jamo. Here is an example of a historical hangul syllable [267] dating from that heroic
era when people were still capable of pronouncing “bstwyaermh!” without choking: we
take three initial consonants ᄇᄉᄐ, two vowels ᅩᅤ, and three ﬁnal consonants ᆯᆷ
ᇂ. And here is the result of their composition: à.
What shall we do if we simply wish to combine jamo without forcing them to form sylla-
bles? There are two methods, only one of which is recommended by Unicode. The better
method involves using the character ZWNJ between the jamo. The inferior method uses
“compatibility jamo”. These have the same glyphs as the regular jamo, but their libido
is nonexistent: they have no desire whatsoever to mate with their neighbors. As always,
characters ﬂagged as “compatibility” are the skeletons in Unicode’s closet: we are discour-
aged from using them, and Unicode goes to great lengths to lead us to forget that they
even exist.
