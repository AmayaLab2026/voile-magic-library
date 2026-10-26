---
title: "Chapter 3: Properties of Unicode characters"
description: "Unabridged English text: Character names, blocks, general category, case properties, rendering properties, Arabic and Syriac, grapheme clusters, UCD."
---

# Chapter 3: Properties of Unicode characters
**By Yannis Haralambous, Ph.D.**
*From Fonts & Encodings, pp. 95–126*

---

```text
allow the user to correct errors that may arise from the generalized application of character properties.
What are these properties, and where are they found? We shall answer both questions
in the remainder of this chapter.
Basic properties
Name
The name of a character is what we have called its description. The official list of the English names of characters according to their positions within the encoding appears in the
following file:
http://www.unicode.org/Public/UNIDATA/UnicodeData.txt
This file contains a large amount of data in a format that is hard for humans to read but
easy for computers: fifteen text fields separated by semicolons. Here are a few lines from
this file:
0020;SPACE;Zs;0;WS;;;;;N;;;;;
0021;EXCLAMATION MARK;Po;0;ON;;;;;N;;;;;
0022;QUOTATION MARK;Po;0;ON;;;;;N;;;;;
0023;NUMBER SIGN;Po;0;ET;;;;;N;;;;;
0024;DOLLAR SIGN;Sc;0;ET;;;;;N;;;;;
The first two fields are the character’s position (also called its “code point”) and name
(which we called its “description” in the previous chapter). These are fields number 0
and 1. (Counting begins at 0.) We shall see the other fields later.
Character names are not there solely for the benefit of humans; programming languages
also understand them. In Perl, for example, to obtain the character that represents the
letter ‘D’ of the Cherokee script, we can write \N{CHEROKEE LETTER A}, which is strictly
equivalent to \x{13a0}, a reference to the character’s code point.
Block and script
These properties refer to the distribution of the full set of characters according to the
script to which they belong or to their functional similarity. Thus we have a block of
Armenian characters (Armenian), but also a block of pictograms (Dingbats), a block of
special codes (Specials), etc.
The names of the blocks, in the form of running heads, can be found in the Unicode
book but also in the file Blocks.txt (in the same directory as UnicodeData.txt). Here
is a snippet of this file:
0000..007F; Basic Latin
0080..00FF; Latin- Supplement
```

```text
Basic properties
0100..017F; Latin Extended-A
0180..024F; Latin Extended-B
0250..02AF; IPA Extensions
Block names are used by Unicode-compatible programming languages in the syntax for
testing whether a character belongs to a specified block. In Perl, for example, we can
determine whether a character is in the Shavian block by writing:
/\p{InShavian}/
The problem with the blocks is the fact that they are not always contiguous: Latin is
spread over five blocks separated by 7,553 code points; Greek is split into two blocks separated by 6,913 code points; the Chinese ideographs are in four blocks on two planes....
To know whether a character is a Latin letter, therefore, we have to perform five separate
tests.
One piece of data, the script, attempts to solve this problem. The file Scripts.txt
presents a breakdown of Unicode into 60 scripts: Latin, Greek, Cyrillic, Armenian, Hebrew, Arabic, Syriac, Thaana, Devanagari, Bengali, Gurmukhi, Gujarati, Oriya, Tamil,
Telugu, Kannara, Malayalam, Sinhala, Thai, Lao, Tibetan, Myanmar, Georgian, Hangul,
Ethiopic, Cherokee, Canadian_aboriginal, Ogham, Runic, Khmer, Mongolian, Hiragana,
Katakana, Bopomofo, Han, Yi, Old_italic, Gothic, Deseret, Inherited, Tagalog, Hanunoo, Buhid, Tagbanwa, Limbu, Tai_le, Linear_b, Ugaritic, Shavian, Osmanya, Cypriot,
Braille, Buginese, Coptic, New_Tai_Lue, Glagolitic, Tifinagh, Syloti_Nagri, Old_Persian, Kharoshthi. And a 61st, which is the default value: Common.
Among these values, there is one that should be handled with care: inherited. This value
applies to diacritical marks and other symbols that take on the value of the script of the
surrounding characters.
It is very interesting to observe that the author of the report that describes this property [108] emphasized its usefulness for detecting spoofing, or the confusion of characters
whose glyphs are identical or similar. The reader who has worked with Greek or Russian
documents will certainly have had the experience of seeing words that print poorly or
that cannot be found during a search simply because an ‘O’, a ‘T’, an ‘A’, a ‘P’, etc., has
been entered in the wrong script. Experience shows that a user who types the two words
“DEARОЛЬГА” will often change scripts not just before the word “ОЛЬГА” but after
the letter ‘О’, because of the need to type the ‘Л’; consequently, the word will contain
both Latin and Cyrillic letters. We also refer the reader back to the photo on page 57,
where we see glorious spoofing between the words “ΠΑΡΚΙΝΓΚ” and “PARKING”.
Age
This is nothing but the number of the Unicode version in which the character first appeared in the encoding. Let us take this opportunity to observe that Unicode characters
have one thing in common with our academics: they are immortal, in the sense that a
Unicode character, once defined, can never be removed from the encoding. The worst
```

thing that can happen to a character is to be “deprecated”, which in Unicode leads to
hilarious situations à la “the character is here, but act as if it were not, and for heaven’s
sake don’t use it!”
The age of characters is indicated in the file DerivedAge.txt.
General category
This is perhaps a character’s most important property, the one that will determine its
behavior in most text-processing systems (both linguistic and typographic). As it should
be, the category is structured in a hierarchical fashion, with the concepts of primary category (letters, diacritical marks, numbers, punctuation, symbols, separators, other) and
subcategories, which specify the classification more precisely.
These give us 30 possibilities in all, each of them represented by a two-letter code.
Letters
• Lu (letter, uppercase). The name of the primary category of “letter” should be construed in a very broad sense, as it can apply equally to a letter of an alphabet, a sign
belonging to a syllabary, or an ideograph.
This particular subcategory refers to an “uppercase” letter; therefore, we can tell that
the category applies to scripts that distinguish uppercase from lowercase letters. Very
few scripts have this property: Latin, Greek, Coptic, Cyrillic, Armenian, liturgical
Georgian, and Deseret.
• Ll (letter, lowercase). This category is the mirror image of the previous one. Here we
are dealing with a letter from one of the multicameral alphabets (i.e., those that have
more than one case) listed above, and that letter will be lowercase.
• Lt (letter, titlecase). There are two very different types of characters that have been
classified Lt: the Croatian digraphs ‘Dž’, ‘Lj’, ‘Nj’ and the capital Greek vowels with
iota adscript.
In the first instance, we see a compromise that was made to facilitate transcription
between the Cyrillic and Latin alphabets: it was necessary to transcribe the Cyrillic
letters ‘r’, ‘y’, and ‘z’, and no better solution was found than the use of digraphs. But
unlike ligatures such as ‘œ’, ‘ij’, and ‘æ’, whose two elements both change case (‘Œ’,
‘IJ’, ‘Æ’), here we may just as easily have ‘DŽ’ (in a word in which all the letters are
uppercase) as ‘Dž’ (in a word in which only the first letter is supposed to be uppercase). This is so for all digraphs: the Spanish and German ‘ch’, the Breton ‘c’h’, etc.
Unicode is not in the habit of encoding digraphs, but in this instance compatibility
with old encodings forced Unicode to turn these digraphs into characters. Thus we
consider ‘dž’ to be the lowercase version, ‘DŽ’ the uppercase version, and ‘Dž’ the
“titlecase” version of the character.
The second instance is the result of a typographical misunderstanding. In Greek
there is a diacritical mark, “iota subscript”, that is written beneath the vowels alpha,
eta, and omega: “?, @, A”. Typographers have found various ways to represent these

Basic properties
characters in uppercase. The most common practice, in Greece, is to place the same
diacritical mark underneath the uppercase letter: “B, C, D”. In the English-speaking
countries another solution is used, which involves placing a capital or small-capital
iota after the letter. The latter is called iota adscript. Unicode incorrectly considers
adscript the only possibly way to write this mark and thus has applied the category Lt
to uppercase letters with iota adscript.
• Lm (letter, modifier). This is a rather small category for letters that are never used alone
and that serve only to modify the sound of the letter that comes before them. Most
of these characters appear in the block of “modifier letters” (0x02B0-0x02FF). There
are a few rare examples of characters in other blocks: the iota subscript that we just
mentioned is one; the stroke kashida that joins Arabic letters is another. Intuitively
we could say that a modifier letter is something that plays the same rôle as a diacritical mark but that does not have the same graphical behavior, since its glyph will not
combine with the one of the previous character but will rather follow it.
• Lo (letter, other). There is no denying it: Unicode is Eurocentric. Proof: Usually,
when we create a classification, we begin with the most important cases and add
a “catchall” case at the very end to cover any exceptions and omissions. Here the
subcategory named letter, other covers all the scripts in the world that have no notion
of case, which is to say practically the entire world! The Semitic, Indian, Southeast
Asian, and ideographic scripts—all are lumped together indiscriminately as Lo....
Diacritical marks
• Mn (mark, non-spacing). These are diacritical marks: accents, cedillas, and other signs
that are independent Unicode characters but that do not have the right to show
themselves in isolation. Fate inexorably binds this sort of Unicode character to the
one that comes before it, and their glyphs merge to form only a single glyph. The
term “non-spacing” is a bit awkward, for an accent can, in some cases, change the
width of its base letter: imagine a wide circumflex accent over a narrow sans-serif ‘i’.
• Mc (mark, spacing combining). If the “modifier letters” are letters that behave somewhat like diacritical marks, the “spacing combining marks” are diacritical marks that
behave somewhat like letters. For example, the languages of India and Southeast
Asia have vowels, markers of nasalization, glottal stops, etc., which graphically resemble letters but which, by their very nature, are always logically attached to letters.
By way of illustration, in Cambodian the letter ‘S’ is pronounced nyo. To turn it into
nye, we add a modifying symbol, the one for the vowel e, whose glyph comes before
the consonant: ‘MS’. We never see this glyph standing alone, just as we never see a
cedilla standing alone—and that is what led Unicode to classify this vowel 0x17C1
khmer vowel sign e among the diacritical marks.
• Me (mark, enclosing). These are diacritical marks whose glyphs completely enclose the
glyph of the character that precedes them. There are very few of them in Unicode:
the Cyrillic signs for hundreds of thousands and millions that encircle a letter taken

to be a number; the rub el-hizb, which appears in the Koran at the beginnings of the
subdivisions; a few technical signs, such as the triangle on European road signs that
indicates danger; etc.
Numbers
• Nd (number, decimal digit). After the letters and the diacritical marks come the numbers. Various writing systems have their own systems of decimal digits: we in the West
have our “Arabic numberals”; the Arab countries of the Mashreq have their “Indian
numerals”; each of the languages of India and Southeast Asia has its own set of digits
between 0 and 9; etc. These are the digits that we find in category Nd. But beware: if
one of these scripts should have the poor taste to continue the series of numerals
by introducing, for example, a symbol for the number 10 (as is the case in Tamil
and Amharic) or a sign for one half (as in Tibetan), these new characters would not
be admissible to the Nd category; they would be too far removed from our Western
practices! They would instead go into the catchall No, which we shall see in just a
moment.
• Nl (number, letter). An especially nasty problem: in many writing systems, letters are
used to count (in which case we call them “numerals”). In Greek, for instance, 2006
is written κ . But if the letters employed are also used in running text, they cannot
belong to two categories at the same time. And Unicode cannot double the size of
the blocks for these scripts simply because someone might wish to use their letters as
numerals. What, then, is a “number-letter”, if not a letter that appears in text? There
are very few such characters: the Roman numerals that were encoded separately in
Unicode, the “Suzhou numerals” that are special characters used by Chinese merchants, a Gothic letter here, a runic letter there. Note that the Greek letters koppa ‘E’
and ‘sampi F’, which represent the numbers 90 and 900, do not count as “numberletters” although they should, since their only use is to represent numbers....
• No (number, other). The catchall into which we place the various characters inherited from other encodings: superscript and subscript numerals, fractions, encircled
numbers. Also in this category are the numbers from various systems of numeration
whose numerical value is not an integer between 0 and 9: the 10, 100, and 1,000
of Tamil; the numbers between 10 and 10,000 of Amharic; etc. Note: although we
cannot classify the ideographs 一‘one’, 二‘two’, 三‘three’, 四‘four’, etc., as “letters”
and “numbers” at the same time, we can so classify ideographs in parentheses: ㈠,
㈡, ㈢, ㈣, etc., are Unicode characters in their own right and are classified as No.
Punctuation
• Pc (punctuation, connector). A very little-used category for punctuation marks—those
that connect two parts of a word to form a single word. The hyphen plays this rôle
in English (“merry-go-round”, “two-year-old”), but the character 0x002D hyphenminus belongs to a separate category, the “dashes”. The most commonly used character in category Pc is the midpoint of the katakana block. Katakana is used mainly to

Basic properties
represent foreign words. When these are connected or contain a hyphen in the original language, it is not possible to do the same in Japanese because there is already a
symbol shaped like a hyphen, whose purpose is to prolong the vowel that precedes
it. An example that shows both characters: by combining ウォーター(wHtE) and ポ
ロ(poro), we obtain ウォーター・ポロ(= “water polo”), in which the midpoint is
character 0x30FB katakana middle dot, which is of category Pc. Another example
of a character in category Pc: the “underscore”, which programmers use to write variable names that consist of more than one word, such as “\$who_am_i”.
• Pd (punctuation, dash). All sorts of dashes: figure, en, em, the hyphen, the minus sign,
the Armenian hyphen, the Mongolian hyphen, etc.
• Ps (punctuation, open). Some of the punctuation marks come in pairs: the parentheses, the brackets, the braces, etc. Here we include the “opening” symbol of each of
these pairs. Recall that Unicode encodes characters in their logical order. When we
write a word in parentheses, we begin with the opening parenthesis, then we write
the word, and finally we finish with the closing parenthesis. What we have just said is
blindingly obvious, except for the fact that the glyph for the character that we call the
“opening parenthesis” may, according to the direction of the script, be ‘(’ (in English)
or ‘)’ (in Hebrew or Arabic) or even ‘Œ’ (in Chinese or Japanese). We have the same
Unicode character in all three cases; only the glyph differs. Later we shall see another
property, mirroring, which affects characters such as these. Note that the quotation
marks are not categorized as Ps, since they have a category to themselves.
• Pe (punctuation, close). The closing counterpart of Ps.
• Pi (punctuation, initial quote). A special case of binary punctuation marks, as quotation marks generally come in pairs. Thus the American double opening quotation
mark “, the French opening quotation mark «, the second-level Greek opening quotation mark Õ, etc., are all of category Pi. But take note: these quotation marks can
be used in peculiar ways that defy any attempt to establish universal rules. For example, « and “ are closing quotation marks in German, ” is an opening and a closing
quotation mark in Dutch, etc. Saying that « and “ are “initial” quotation marks is no
more accurate than saying that the men wear trousers and the women wear skirts in
every country in the world.
• Pf (punctuation, final quote) for ‘”’, ‘ »’, etc. As mentioned in the previous paragraph,
these are no more “final” than Pi is “initial”.
• Po (punctuation, other). The catchall that turns out to contain the most important
punctuation marks: the period, the comma, the colon, the semicolon, the exclamation point, the question mark, etc.
Symbols
• Sm (symbol, math). This category is for signs that are used only in mathematics. Thus
in “sin(π) = 0”, only the equals sign is in category Sm, for all the other signs are either
letters, numbers, or punctuation marks.

• Sc (symbol, currency). Example: the dollar sign ‘\$’, whose glyph is sometimes also used
for the character ‘s’, as in “Micro\$oft” or “U\$A”.
• Sk (symbol, modifier). These are phonetic symbols that modify the letters around
them but that never appear by themselves—much like the modifier letters, except
that here we have not letters but punctuation marks or symbols. For example, there
are the phonetic symbols ‘œ – — “ ”’, which denote the five tones of certain Chinese
dialects. A tone mark necessarily goes with a letter, which it modifies; yet it is a graphical symbol, not a letter, so it is a good example of a “modifier symbol”.
Unfortunately, some symbols that do not modify anything have been included in
this category. These are the unnatural characters known as the spacing diacritical
marks, i.e., the non-combining diacritical marks that have been included in the encoding for reasons of compatibility with earlier standards.
• So (symbol, other). The catchall category for symbols that are not mathematical symbols, currency signs, or modifiers. In a set containing i, h, and g, there is something
for every taste—within the limits of political correctness, of course, and a certain
technocratic ethical standard. Unicode has not yet created a category for ostentatious
religious symbols, but one should not be long in the coming....
Separators
• Zs (separator, space). These are spaces: zero-width, thin, medium, wide, 1-em, 1-en,
3-to-an-em, 4-to-an-em, and many more. Some of them allow a line break and some
do not. And there is one typographical curiosity: in the ogham script, there is a space
that is not a space! This script is written along a baseline; but unlike the line in Devanagari, this line is not broken between words. Accordingly, the space (in the sense
of “word separator”) is a segment of baseline with no letter on it.
• Zl (separator, line) and Zp (separator, paragraph). These categories contain only one
character each: 0x2028 line separator and 0x2029 paragraph separator. These
characters attempt to solve the problem of breaking text into lines and paragraphs
in an unambiguous way. Recall that, when a document is read by a word processor
such as Word, the lines are automatically divided without any changes to the underlying text, and a newline character in the document will visually mark the start
of a new paragraph. The conventions are different in TEX: a newline in the source
document is equivalent to a blank space in the output. It takes two consecutive newlines in the source to produce a new paragraph in the output. XHTML follows yet
another convention: any number of newlines in the source will yield a single blank
when rendered; to start a new line or a new paragraph in the output, one must use
the appropriate tags (&lt;br/&gt; and &lt;p&gt; or &lt;div&gt;). In this paragraph we have used the
term “newline”. The character corresponding to this operation varies from system to
system: under MacOS, the character is cr; under Unix, it is nl; and under Windows,
it is a pair of bytes, cr nl. To avoid having to adopt one of these conventions, Unicode decided to punt: there are two new characters to indicate a change of line (if
necessary) and a change of paragraph. Now all that remains is to persuade people to
use them....

Basic properties
The remaining categories
• Cc (other, control). This category covers code points 0x0000-0x001F and 0x00800x009F, i.e., tables C0 and C1 in ISO 2022–compatible encodings. Unicode does
not assign any semantic value to these characters; their names are invariably “&lt;control&gt;”. No other Unicode character is in this category.
• Cf (other, format). These characters are all used to insert metadata into a document.
They are important enough to be listed here:
– 0x00AD soft hyphen marks a potential spot for dividing a word across lines.
We can imagine a human or a program that inserted such characters at every
permitted break-point; the rendering software would then not have to apply the
hyphenation algorithm.1
– 0x0600 arabic number sign and the three characters that follow behave in a
very unusual way: they occur at the beginning of a number, and their effect lasts
as long as digits are added. Thus they are combining characters, in a sense, the
only differences being that they precede the base character and that they act on an
unlimited number of following characters. This character indicates that a number is being written. Its graphical shape is that of a letter ayn with a stroke that
extends for the length of the number. This practice occurs in languages such as
Urdu and Baluchi.
– 0x0601 arabic sign sanah: In Arabic sanah means ‘year’. This character is the
word sanah written beneath a number for its entire width to indicate that the
number represents a date.
– 0x0602 arabic footnote marker is written beneath the index of a footnote.
– 0x0603 arabic sign safha is likewise written beneath a page number.
– 0x06DD arabic end of ayah is a very different symbol: it is a circle, often highly
embellished, that is used in the Koran to enclose the number of the ayah that
has just ended. This character is in category Cf because it behaves like those
that we have just described: it encircles the number before which it appears,
irrespective—at least in theory—of the number’s size.
– 0x070F syriac abbreviation mark is a means of drawing a horizontal line above
a string of Syriac glyphs to indicate that they form an abbreviation. This character is placed at the beginning of the abbreviation, which continues until the end
of the string, namely, until the first character of type “punctuation”, “symbol”,
or “separator”.
– 0x17B4 khmer vowel inherent aq and 0x17B5 khmer vowel inherent aa are
mistakes [335, p. 390], and their use is discouraged by the Consortium.
1 In certain languages we may be able to make good use of multiple characters of this kind, corresponding to different degrees of precedence. In German, for instance, we distinguish four levels of precedence for
the hyphenation of a word such as Wahr2schein4lich4keits1theo3rie, depending on whether the breaks occur in
front of the last component, between the other components, between syllables of the last component, between
syllables of other components.

– 0x200C zero width non-joiner, or “ZWNJ”, is a character that prevents the
formation of a link or a ligature between the glyphs of the two surrounding
characters. We can use it in scripts such as Arabic when two consecutive letters
should not be connected, or in those cases in which we want to avoid a ligature
at all costs, as in the German word Auflage, in which the letters ‘f’ and ‘l’ belong
to different components of the compound word.
– 0x200D zero width joiner, or “ZWJ”, is the opposite of ZWNJ. It is very useful
when we need to obtain a specific contextual form. For example, the abbreviation “” is found in Arabic dictionaries. It is the initial form of the letter hah.
Since this letter is preceded and followed by non-letters, the rendering engine
will automatically select the glyph  for the isolated form. To obtain the initial
form, we follow the letter with the character ZWJ, which leads the rendering
engine to think that the letter is followed by another Arabic letter, to which it
must be connected.
– 0x200E left-to-right mark, 0x200F right-to-left mark, 0x202A left-to-right
embedding, 0x202B right-to-left embedding, 0x202C pop directional formatting, 0x202D left-to-right override, and 0x202E right-to-left override
are used by the bidirectional algorithm, which we shall describe in detail in
Chapter 4.
– 0x2060 word joiner can be inserted between two words to prevent a line break
at that location. Software systems have their own line-breaking algorithms, of
course, but these algorithms take only letters into account. Often the author has
typed an em dash followed by a comma only to shudder in horror when he saw
the comma moved down to the next line. Of course, we can always develop more
refined software that will avoid this sort of typographical error, but until then
it will not be a bad idea to insert a character that will effectively prevent the
separation of two glyphs.
– 0x2061 function application is a character that does not affect rendering at all.
Its rôle is strictly semantic. It indicates that two mathematical symbols stand
in relation to each other as a function and its argument. When we write f(x),
it is clear that we are referring to the function f of x; likewise, when we write
a(b + c), it is clear that we are referring to the product of the variable a and
the sum of the variables b + c. But what is f(g + h)? Is it f : g + h →f(g + h) or
f ·g+ f ·h? To eliminate the ambiguity, we have an invisible “function” character
that indicates, when placed between f and (g + h), that the notation refers to
the application of a function. This invisible character can also be used for other
purposes than mathematical notation: symbolic calculation, voice synthesis, or
simply the transmission or storage of a formula with its contents represented
unambiguously.
– 0x2062 invisible times is the other option for interpreting the expression f(g+
h): the product of f and g + h. In algebra we have the habit of not explicitly
writing a symbol for multiplication and, more generally, the laws of algebraic
structures. Unicode speaks of multiplication, but all indications suggest that this
operator may be used for any law of an algebraic structure.

Other general properties
– 0x2063 invisible separator handles a third case in which ambiguity may arise,
that of indices. When we write ai j within a matrix, it is clear from context that
we are referring to the i th row and the j th column of that matrix. Thus we are
speaking of two indices, not the product of i and j. To make our intention clear,
we may insert the invisible separator between the two indices.
– 0x206A inhibit symmetric swapping and 0x206B activate symmetric swapping are deprecated [335, p. 543].
– 0x206C inhibit arabic form shaping and 0x206D activate arabic form shaping are also deprecated.
– 0x206E national digit shapes and 0x206F nominal digit shapes are deprecated as well.
– 0xFEFF zero width non-breaking space, or “BOM”, is the character that enables us to determine whether a Unicode document in UTF-16 is encoded in
little-endian or big-endian order. This technique works because the character’s
alter ego, 0xFFFE, is not a Unicode character. Therefore, if we find an 0xFFFE in
a file, there is only one possible conclusion: it is an 0xFEFF that we are reading
backwards, in the wrong mode. This character has no other rôle than indicating
endianness.
– 0xFFF9 interlinear annotation anchor, 0xFFFA interlinear annotation
separator, and 0xFFFB interlinear annotation terminator are used to encode interlinear annotations, which are pieces of information that are presented
in a special way, such as by placing them between two lines of text. They may
be used for a word-for-word translation or, in the case of the ideographic languages, to indicate an ideograph’s pronunciation by making reference to a phonetic writing system such as the Japanese kana, the Korean hangul, or the Chinese
bopomofo.
– There are also characters in category Cf for encoding the basic units of musical
notation.
– And all the language tags in Plane 14 that are used as markup for languages are
also in category Cf.
• Cs (other, surrogate). The characters in the high and low surrogate zones (0xD8000xDBFF and 0xDC00-0xDFFF); see page 64.
• Co (other, private use). The characters of the private use areas.
• Cn (other, not assigned). By extending the notion of category to all of the code points in
the Unicode chart, we can say that a code point that is not assigned to any character
is of category Cn. Corollary: No character in the file UnicodeData.txt can ever be of
category Cn.
Other general properties
By scanning over the categories and subcategories described in the previous section, we
can quickly notice that many properties are omitted from the categorization. Another

```text
file at the Unicode site, by the name of PropList.txt, makes up for this deficiency by
introducing a certain number of properties that are orthogonal to the notion of category.
Here is a snippet of the file, showing the characters that have the property of being
“spaces”:
0009..000D
; White_Space # Cc
[5] &lt;control-&gt;..&lt;control-D&gt;
; White_Space # Zs
SPACE
; White_Space # Cc
&lt;control-&gt;
00A0
; White_Space # Zs
NO-BREAK SPACE
; White_Space # Zs
OGHAM SPACE MARK
180E
; White_Space # Zs
MONGOLIAN VOWEL SEPARATOR
2000..200A
; White_Space # Zs
[11] EN QUAD..HAIR SPACE
; White_Space # Zl
LINE SEPARATOR
; White_Space # Zp
PARAGRAPH SEPARATOR
202F
; White_Space # Zs
NARROW NO-BREAK SPACE
205F
; White_Space # Zs
MEDIUM MATHEMATICAL SPACE
; White_Space # Zs
IDEOGRAPHIC SPACE
At the start of each line, we see the code points or ranges concerned. The name of the
property appears after the semicolon. Everything after the pound sign is a comment;
this section contains the character’s category and its name or, when there are multiple
characters, the names of the endpoints of the range.
Of these properties, which number 28 in all, here are the general-purpose ones. We shall
see the others later when we discuss case, the bidirectional algorithm, etc.
Spaces
This property applies to 26 Unicode characters, of which some are genuine spaces (category Zs) and others are control characters (category Cc). The line separator and the
paragraph separator, which are respectively in categories Zl and Zp, also have this property.
Alphabetic characters
These are characters of category “letter” (Lu, Ll, Lt, Lm, Lo) or “ alphabetic numbers” (Nl).
There are 90,989 of them in all. Note that characters have the alphabetic property simply by virtue of belonging to one of these categories; thus extracting the corresponding
characters from the file UnicodeData.txt yields a complete list of alphabetic characters.
For that reason, this property is called a “derived” property, and its characters are listed
not in PropList.txt but in DerivedCoreProperties.txt.
Noncharacters
These characters are the forbidden fruit of Unicode: their code points may not be used.
The Consortium even created a special term for them: noncharacters (written solid). They
```

```text
Other general properties
cover 32 code points in the block of Arabic presentation forms 0xFDD0-0xFDEF and the
last two positions in each plane, 0x??FFE and 0x??FFF. This is why: Code point 0xFFFE
must be ruled out as a character so that the pair of bytes 0xFF 0xFE, when read by software, can be interpreted as the character BOM 0xFEFF read in the wrong direction. Only
if one code point (0xFFFE) is sacrificed can the test for endiannism work. The non-use
of the character 0xFFFF is intended to simplify the programmer’s life. It happens that
some programming languages use a special character to terminate a string; we call that
character a sentinel (in C, for example, it is the character 0x00). This approach has the
drawback that the sentinel cannot be used within a string. If 0xFFFF is selected as the
sentinel, this problem will never arise, as 0xFFFF is not a character and therefore cannot
appear within a string.
Why was this decision extended to the other planes? Out of compassion, or perhaps because it was expected that programmers would take algorithms intended for the BMP
and apply them to the other planes by simply adding an offset. Since these restrictions
were applied to all the planes, the algorithms remain valid.
Ignorable characters
The full name is default ignorable code points. If we take this property’s name at face value
and examine the list of its members, which is a veritable country club of exotic characters
(the combining grapheme joiner, the Korean syllable fillers, the variation selectors, the
zero-width space, the various control characters... ), we may scratch our heads for a long
time before understanding what it means. Yet it is very simple: when software does not
have a glyph to represent a character, it is supposed to display a symbol for “missing
glyph”. But in certain cases we would prefer not to display anything. A character is ignorable if it should not be represented by a generic glyph when the software is unable to
carry out the behavior that it implies. For example, the combining grapheme joiner is
a character that calls for very special behavior: that of construing two glyphs as one and
applying a diacritical mark to the combination. If the software is not equipped for this
functionality, it is expected not to display anything in this character’s place.
To obtain a complete list of the ignorable characters, take the “other, control” characters
Cc, the “other, format” characters Cf, and the “other, surrogate” characters, blend in certain characters listed under property Other_Default_Ignorable_Code_Point in the file
PropList.txt, shake well, and serve immediately.
Deprecated characters
Old lawyers never die; they just lose their appeal. The same goes for characters: the worst
thing that can happen to them is to be deprecated. There are ten such characters (as of this
writing), and they are listed in PropList.txt.
Logical-order exceptions
These are characters that are not rendered in their logical order. They represent a blemish
in Unicode that is due, once again, to the principle of backward compatibility with ex-
```

```text
isting encodings. This property applies to 10 Thai and Lao characters, all of them vowels
placed to the left of the consonant. One example is the consonant ’ 0x0E99 lao letter no. To obtain the sound “nF”, we add the vowel ‘ 0x0EC0 lao vowel sign e after the
consonant. But graphically this vowel appears before the consonant: ‘’. Its graphical
order is therefore the opposite of its logical order; thus it is a “logical-order exception”.
The reader with an inquisitive bent will easily discover that this phenomenon of vowels
placed before consonants occurs in Khmer, Sinhala, Malayalam, Tamil, Oriya, Gujarati,
Gurmukhi, Bengali, Devanagari, and doubtless other writing systems as well. Why are
the characters in question “logical” in these scripts but “illogical” in Thai and Lao? For
no better reason than a difference of status. In all of the scripts mentioned, the vowels in
question are combining characters; therefore, their graphical position is managed by the
class of combining characters, which we shall discuss below. In particular, this position,
whatever it be, is in no way illogical. In the case of Thai and Lao, however, the same vowels were encoded as ordinary characters; thus it was necessary to make some adjustments
by adding this property.
Soft-dotted letters
These are characters whose glyphs have a dot: ‘i’, ‘j’, and all their derivatives. In exchange
for the privilege of bearing an accent, these letters must forfeit their dot: thus we have
‘î’, not ‘◊’2. The only exception: Lithuanian, which preserves the dot beneath the accent.
By way of contrast, we can say that the dot on the Lithuanian ‘i’ is a “hard dot”.
How to “harden” the dot on an ‘i’? The method recommended by Unicode is to add a
dot, i.e., to put the character 0x0307 combining dot above after the ‘i’. The glyph will
remain the same—because the original dot on the ‘i’ is soft—but its behavior will differ:
a subsequent diacritical mark added to this glyph will not suppress the dot. Thus, if for
some reason we should wish to obtain ‘◊’, we would have to write three characters in a
row: “i, combining dot above, circumflex accent”.
Mathematical characters
Or, to be more precise, the Unicode characters with the property “other math”. These
are the characters in the category Sm (“symbol, math”) plus 1,069 characters listed in
the file PropList.txt under the property Other_Math. All the punctuation marks that
can appear in a mathematical formula (parentheses, brackets, braces, the vertical bar,
etc.) and all the letters in the various styles that appear in the block of mathematical
alphanumeric symbols 0x1D400-0x0x1D7FF are assembled under this heading.
If assignment to category Sm guarantees that a character is a mathematical symbol, then
“mathematical character” can assist software in identifying the extent of a formula. But
note that—alas!—the ordinary Latin and Greek letters are neither in category Sm nor
of property “mathematical characters”, even though they are essential to mathematical
formulae.
2 For many years a classic mistake of the user who was new to LATEX was to write \^i instead of \^{\i}.
The advent of the T1 fonts, whose macros provide for the “soft dot”, eliminated this error.
```

```text
Other general properties
Quotation marks
This property covers all the characters that can be used as quotation marks. They are of
categories Po, Pi, Pf, Ps, and Pe. There are 29 of them, and they are listed in PropList.txt
under the property Quotation_Mark.
Dashes
Everything that looks more or less like a dash and is used as such. There are 20 characters
that have this property; they are of categories Pd (punctuation, dash) and Sm (mathematical symbol). They are listed in PropList.txt under the property Dash.
Hyphens
The existence of this property shows that the Consortium wished to distinguish clearly
between “hyphens” and “dashes”: the former are placed within words and play a morphological rôle (“merry-go-round”, “two-year-old”); the latter are placed between words
and play a syntactic rôle (“I’m leaving—do I have to repeat myself?”). Usage varies
widely among the typographic conventions of the different countries; for that reason,
some characters have both properties: “dash” and “hyphen”.
There are 10 characters that have the “hyphen” property; they are in categories Pd
(punctuation, dash), Pc (punctuation, connector; for the midpoint used in katakana,
see page 101), and Cf (character, format; for a potential line break). They are listed in
PropList.txt under the property Hyphen.
Terminal punctuation
Folk wisdom says that “birds of a feather flock together”. Well, the characters with this
property have flocked together from various and sundry blocks, yet they are of quite
different feathers indeed. What they have in common is that they play the rôle of “terminal” punctuation. This term is rather ill chosen, as these characters also include the
slash, which does not necessarily end a sentence. For want of a better definition, we can
say intuitively that these are characters that play the same rôle as our various stops (the
period, exclamation point, semicolon, colon), and also the slash.
There are 78 characters with the “hyphen” property; they are all of category Po (punctuation, other). They are listed in PropList.txt under the property Terminal_Punctuation.
Diacritics
When we described the category of “marks”, we called them “diacritical marks”. That
might sow confusion, as Unicode also defines a property called diacritics. It covers both
the “real” (non-spacing) diacritical marks and the “inert” (spacing) diacritical marks of
ASCII, as well as a host of other signs. For example, the katakana prolonged sound mark,
graphically speaking, is not a diacritical mark at all but nonetheless effectively plays
this rôle.
```

```text
There are 482 characters with the “diacritic” property. They are listed in PropList.txt
under the property Diacritic.
Extenders
These are characters whose rôle is to extend or repeat the preceding character. Thus,
for example, we have ‘ゝ’ 0x309D hiragana iteration mark, which works as follows:
Suppose that we have two identical hiragana syllables in a row, such as “きき” (kiki). It is
faster to write the iteration mark: “きゝ”; the result is the same. In addition, if the second
syllable is voiced, as in “きぎ” (kigi), we can use the iteration mark with a phonetic modifier: “きゞ”. We find this most often in vertical text, especially in Japanese calligraphy.
There is the same type of iteration mark for katakana and for ideographs.
There are 19 characters with the “extender” property. They are listed in PropList.txt
under the property Extender.
Join control
There are two characters that manage joining and non-joining between glyphs: zero
width joiner 0x200D, or ZWJ, and its opposite: zero width non-joiner 0x200C, or
ZWNJ. We have discussed these on page 104.
These are the only two characters with the Join_Control property. They are listed in the
file PropList.txt.
The Unicode 1 name and ISO’s comments
Recall that Unicode 1 dates from the antediluvian era before it was merged with
ISO 10646, i.e., the era when each of them did pretty much what it pleased (whereas
today Unicode and ISO do what they please together). In UnicodeData.txt there is a
vestige of that era: the name of the character as it was in Unicode 1.
Glancing over these names, we notice that some of them were better than the current
ones. For example, the pseudo-accents of ASCII had the word spacing in their names:
spacing grave, spacing diaeresis, etc. The parentheses were called opening parenthesis and closing parenthesis, not left parenthesis and right parenthesis, as they
are called today, when we know perfectly well that their glyphs can be reversed or even
turned 90 degrees for vertical typesetting.
Finally, there are also monstrous errors. The Coptic letters, for instance, were called
“Greek”: we have unbelievable names such as greek capital letter shei and greek
capital letter fei. The other monumental error of Unicode 1 was to refer to the
modern Georgian letters as “small” letters (georgian small letter an, etc.), when
there is no case in Georgian. But all of that belongs to the past, and we are not going
to dig into these almost 15-year-old documents if the information does not appear in
UnicodeData.txt.
In this file we also find a piece of potentially useful information: the comment, associated with certain characters, that appears in ISO 10646. We have already mentioned the
```

Properties that pertain to case
fact that ISO 10646-1 and Unicode bring themselves into alignment on a regular basis.
This alignment involves the names and the code points of characters, but nothing prevents ISO 10646 from adding comments to the characters, and Unicode is not obligated
to adopt those comments. These are the comments that we find in this file.
Properties that pertain to case
Case is a typographical phenomenon that, fortunately, affects only a few scripts, the socalled bicameral ones: Latin, Greek, Coptic, Cyrillic, Armenian, liturgical Georgian, and
Deseret. We say “fortunately” because there is a complex problem that makes the processing of textual data more difficult.
Unicode distinguishes three cases: lower case (the “small letters”), upper case (the “capital letters”), and title case (the case of characters that are capitals at the beginning of a
word). The name “title case” is very ill chosen, as this concept has nothing to do with
titles, at least as they are typeset in most languages. This name comes from the Englishspeaking countries’ custom of capitalizing all the important words (including the first
and the last) in titles: what is “La vie est un long fleuve tranquille” in French becomes
“Life Is a Long and Quiet River” in English.
Before describing the properties that pertain to case, let us note, by way of information, that four
cases still are not handled by Unicode:
• Obligatory lower case. These are letters that remain in the lower case irrespective of the context.
Example: German has the abbreviation GmbH (Gesellschaft mit beschränkter Haftung = ‘limited
liability company’). In this abbreviation, the letters ‘m’ and ‘b’ must always be written as lowercase letters, even in the context of full capitals. Another example: if “mV” stands for millivolt
and “MV” for megavolt, we had better treat the ‘m’ of “milli” as an obligatory lowercase letter;
else we will run the risk of seriously damaging our electrical equipment.
• Obligatory capitals. In the name of the country Turkey, the ‘T’ is an obligatory capital: we can
write the word as “Turkey” or “TURKEY” but never “turkey” (which refers instead to the bird).
• Alternating capitals. These are another German invention. To designate students of both sexes
in a politically correct fashion, we can write StudentInnen: Studentinnen means ‘female students’, but by using a capital ‘I’ we show that it refers to male students (Studenten) as well.
We call this ‘I’ an alternating capital because it assumes the case opposite to that of the surrounding characters. It is the equivalent of our politically correct “steward(ess)” or “s/he”.
• Alternating lowercase letters. This occurs when we write STUDENTiNNEN in capitals. The ‘i’
must be written as a lowercase letter under the circumstances.
Here are the properties of Unicode characters that apply to the concept of case.
Uppercase letters
These are the “uppercase letters” (category Lu) as well as the uppercase Roman numerals (category “number, letter” Nl) and the encircled uppercase letters (“symbol,
other” So). The characters other than Lu are listed in PropList.txt under the property
Other_Uppercase.

Lowercase letters
Again, these are the “lowercase letters” (category Ll) as well as a certain number of
characters listed in PropList.txt under the property Other_Lowercase: certain modifier letters, the Greek iota subscript, the lowercase Roman numerals, and the encircled
lowercase letters. Note that the iota subscript is available in two flavors: combining and
non-combining. Both of them have the property “lowercase”.
Simple lowercase/uppercase/titlecase mappings
These mappings are said to be “simple” when the result is a single character whose mapping is independent of the language. This information appears in UnicodeData.txt in
fields 12 (uppercase), 13 (lowercase), and 14 (titlecase). When the mapping maps the
character to itself, the field is left empty. Thus uppercase letters will typically have no
value in fields 12 and 14, and lowercase letters will have no value in field 13.
When a character calls for special treatment, the value that appears in UnicodeData.txt
represents its default behavior (thus the uppercase form of ‘i’ is specified as ‘I’ in this
file); if there is no default behavior, the field is left blank (all three fields for the German
letter ‘ß’ are empty!).
Special lowercase/uppercase/titlecase mappings
Eight sets of characters pose problems for case assignment. They are described in the file
SpecialCasing.txt, whose structure resembles that of UnicodeData.txt. Its lines are of
a fixed format: five fields, of which the first four contain the initial code point and, in
order, the lowercase, titlecase, and uppercase mappings. The fifth field (which can be repeated if necessary) describes the context of the rule. This description is either the name
of one or more languages or a keyword for the context. Here are the special cases:
• The German ‘ß’ 0x00DF latin small letter sharp s, whose uppercase version is said
by Unicode to be ‘SS’. Unicode even gives a titlecase version ‘Ss’ that is purely fictitious, since no German word begins with ‘ß’ or with a double ‘s’. Note that Unicode
has omitted an important possibility: in some instances [123, p. 75], ‘ß’ is capitalized as ‘SZ’, as in the word MASZE (Maße = ‘measures’), to distinguish it from MASSE
(Masse = ‘mass’).
• The Turkish and Azeri ‘i’, whose uppercase form is ‘˙I’. These languages also have an ‘ı’,
whose uppercase form is ‘I’.
• The Latin ligatures ‘ff’, ‘fi’, ‘fl’, ‘ffi’, ‘ffl’, ‘÷’, and ‘s’ (but not the ‘c’ ligature, which is
just as important as ‘s’) from the block of presentation forms. Their uppercase forms
are ‘FF’, ‘FI’, ‘FL’, ‘FFI’, ‘FFL’, ‘ST’, and again ‘ST’. Their titlecase forms are ‘Ff’, ‘Fi’, ‘Fl’,
‘Ffi’, ‘Ffl’, ‘St’, and ‘St’.
• The grammatical Armenian ligature ‘ú’ and the presentation forms ‘ç’, ‘é’, ‘ù’,
‘å’, and ‘ü’, Their respective uppercase forms are ‘EU’, ‘MN’, ‘ME’, ‘MI’, ‘EN’,
and ‘MQ’, and in title case they appear as ‘Eu’, ‘Mn’, ‘Me’, ‘Mi’, ‘En’, and ‘Mq’.

Properties that pertain to case
• Various letters for which no uppercase form has been provided: the Afrikaans ‘ ’n’,
whose uppercase form is ‘ ’N’; the Greek ‘G’, ‘H’, and ‘I’, which all become ‘J’ (or ‘K’ in
some fonts); ‘L’, ‘M’, and ‘N’, which become ‘O’, etc.
• The Greek letters with iota subscript. Unicode claims that ‘?’ is written ‘B’ in title
case and ‘ΑΙ’ in upper case. The author considers the form ‘B’ more natural under
all circumstances, but at the end of the day this is merely a question of taste.
• The Greek sigma. (The Greek language does indeed present lots of problems!) There
are two characters: ‘σ’ 03C3 greek small letter sigma, which is used at the beginning and in the middle of words, and ‘P’ 03C2 greek small letter final sigma,
which appears at the end of words. When converting from uppercase to lowercase letters, one must take into account the position of the letter within the word and select
the appropriate character. Unfortunately, reality is more complex: in an abbreviated
word, sigma retains its form even when it is the last letter of the abbreviation. The
sentence “Ο ΦΙΛΟΣ. ΙΩΑΝΝΗΣ ΕΙΝΑΙ ΦΙΛΟΣ.” (= ‘The philos(opher) Ioannis
is a friend’) becomes “S φιλTσ. ’Ιω!ννηP εUναι φλοP.” in lower case because the
first “ΦΙΛΟΣ.” is the abbreviation for “ΦΙΛΟΣΟΦΟΣ”, while the second one is the
word “ΦΙΛΟΣ” followed by a period to end the sentence. The computer cannot distinguish the two instances without advanced linguistic processing. Not to mention
the use of medial sigma as a number (σ = 200) and the similar use of a letter that is
not a final sigma but that looks like one: stigma ‘’, whose numeric value is 6.
• Although everyone likes to “dot his ‘i’s”, the Lithuanians do so even when the ‘i’
also bears other accents. Thus the lowercase versions of ‘Ì’, ‘Í’, and ‘˜I’ in Lithuanian
are not ‘ì’, ‘í’, and ‘˜ı’ as in most other languages but ‘ÿ’, ‘Ÿ’, and ‘⁄’. We say that the
Lithuanian dot is “hard”, as opposed to the soft dot that is replaced by accents.
Case folding
By case folding we mean a standard transformation of all letters into a single case so as to
facilitate alphabetical sorting. This information is given in the file CaseFolding.txt, a
sample of which appears here:
00DB; C; 00FB; # LATIN CAPITAL LETTER U WITH CIRCUMFLEX
00DC; C; 00FC; # LATIN CAPITAL LETTER U WITH DIAERESIS
00DD; C; 00FD; # LATIN CAPITAL LETTER Y WITH ACUTE
00DE; C; 00FE; # LATIN CAPITAL LETTER THORN
00DF; F; 0073 0073; # LATIN SMALL LETTER SHARP S
The three fields contain the original character, a description of its case, and the characters
that result from case folding. Four possibilities exist:
• C, or “common case folding”: the usual instance, in which we have only a single character in the output, which is not dependent on the active language.

• F, or “full case folding”: the special eventuality in which the output has more characters than the input, as is the case for the German ‘ß’, the ‘f’-ligatures, etc.
• S, or “simple case folding” is like C, but it is used when the same original character
has another folding instruction of type F. Example: ‘D’ becomes ‘ωι’ under full case
folding and ‘A’ under simple case folding.
• T, or “Turkic case folding”:3 ‘I’ becomes ‘i’ under simple case folding and ‘ı’ under
Turkic case folding; ‘˙I’ becomes ‘i’ under Turkic case folding and ‘i’ under ordinary
case folding (in fact, this glyph is the pair of characters ‘i’ and ‘combining dot above’).
Take note of this subtlety: the latter glyph has a “hard” dot, a dot that will not be
removed by any following accents. By adding a circumflex accent after this ‘i’, we
obtain ‘◊’, and by adding a second dot accent we can even obtain ‘€’....
Rendering properties
The Arabic and Syriac scripts
The characters of these scripts have two additional properties: joining type and joining
group. To understand what these terms mean, let us recall the properties of these two
scripts.
The scripts include three types of letters:
• those that have four contextual forms: initial, medial, final, and isolated, the isolated
form being both initial and final;
• those that have two contextual forms: final and isolated;
• those that have only one contextual form.
Let B be a letter with four forms and R a letter with two forms. Let us use 0, 1, 2, and 3 to
represent the isolated, initial, medial, and final forms, respectively. Thus we have at our
disposal the forms B0, B1, B2, B3, and also R0 and R3.
Contrary to what one might expect, contextual forms do not refer to words but to contiguous strings of letters. An initial letter may very well appear in the middle of a word;
that will occur if the preceding letter is a final form. Thus we shall concern ourselves here
with strings of letters.
Here are the three rules to follow in order to build up strings:
1. start the string with an initial letter;
2. within the string, continue with a medial letter, or, if the required letter has no medial form, use its final form, which will end the string;
3 “Turkic” rather than “Turkish” because the phenomenon occurs in Azeri as well as in Turkish.

Rendering properties
3. the last letter of the string must necessarily be a final form.
Let us take a few typical examples of words of three letters: BBB, BBR, BRB, RBB, BRR,
RBR, RRB, RRR.
In the first of these words, the first letter is initial (rule 1), the second is medial (rule 2),
and the third begins as a medial letter (rule 2) but becomes final because we are at the
end of the word, and therefore also at the end of the string (rule 3). Thus we have B1B2B3.
The second word is similar, but the third letter immediately becomes final, as it does not
have a medial form: B1B2R3.
The third word is more interesting. We begin with an initial letter (rule 1). Next we
should have a medial letter in the second position; but since R does not have a medial
form, we have a final form in the second position instead. Our string is now complete,
and we begin a new string with an initial form of B. But since this letter is the last one in
the word, it is also final. Being both initial and final, it assumes its isolated form. Thus
we have B1R3B0.
In the fourth word, we begin with an initial form (rule 1), but the letter R does not have
one, unless we take its isolated form (which is both initial and final at the same time).
Thus we take an isolated R, which means that our first string is already finished. The B
that follows thus appears at the beginning of a new string and is therefore in its initial
form. Finally, the second B is medial and becomes final because we are at the end of the
word. Thus we have R0B1B3.
The reader may work out the remaining words in the same manner: B1R3R0, R0B1R3,
R0R0B0, R0R0R0. To illustrate this mechanism, let us take two genuine Arabic letters: beh
in its four forms, “   	”, and reh in its two forms, “
”. Here are our eight hypothetical
words in the Arabic alphabet: BBB , BBR
, BRB
, RBB , BRR
, RBR
,
RRB 	, RRR .
Letters with only a single form have the same behavior as letters that are not Arabic or
Syriac: they form a string in themselves and therefore cause the preceding string to end
and a new string to begin.
Let us now return to Unicode properties. The joining type is one that precisely describes
the behavior of a letter with respect to its context. There are five kinds:
• Letters with four forms are of type D;
• Those with two forms are of type R;
• Letters with one form, including the character ZWNJ (zero-width non-joiner), and
all non-Arabic and non-Syriac letters are of type U;
• The “marks”—namely, the diacritical marks and other characters of this type—do
not affect joining; they are therefore “transparent” to contextual analysis, and therefore we shall say that they are of type T;

• One type remains: there are two artificial characters that are not letters but that behave like letters with four forms. These are the character ZWJ (zero-width joiner) and
the character 0x0640 arabic tatweel, which is an extended connecting stroke, also
called kashida. We shall say that these two characters are of type C.
In the file ArabicShaping.txt, the types of all of the affected characters (those that are
not listed are automatically of type T if they are of category Mn or Cf; otherwise, they are
of type U) are provided. Here is an extract of this file:
0627; ALEF; R; ALEF
0628; BEH; D; BEH
0629; TEH MARBUTA; R; TEH MARBUTA
062A; TEH; D; BEH
062B; THEH; D; BEH
The first field contains the character’s code point; the second, a part of the name (the
ever-present arabic letter or syriac letter is omitted); the third, the type of the letter.
By respecting the above-listed rules and the types of letters, software can perform basic
contextual analysis for Arabic and Syriac—provided, of course, that an adequate font is
available.
The sample of code shown above contains a fourth field, the joining group.4 It is a visual
classification of the letters. To understand how it works, we need to review the rôle of
dots in the Arabic script.
In its earliest form, the Arabic script suffered from acute polysemy of its glyphs. The
sounds b, t, th (as in the word think), n, and y (the last of these in its initial and medial forms only) were written with the same symbol. How, then, to distinguish
 bayt
(house) and
 tayb (well)? To alleviate this difficulty, a system of dots was invented:
one dot below beh, two dots below yeh, one dot above noon, two dots above teh, three dots
above theh. Thus the words ‘house’ and ‘well’ can finally be distinguished:  and .
Systems of dots used to disambiguate words were further developed by the other languages that use the Arabic script, other signs were added, and today we find ourselves
with several hundred signs, all derived from the same few undotted Arabic letters. Thus
we can classify letters according to their ancestry: if they are derived from the same ancestor (free of dots and diacritical marks), we shall say that they are in the same joining
group. The complete list of joining groups for Arabic appears in [335, p. 279].
Managing grapheme clusters
The idea is that a script or a system of notation is sometimes too finely divided into
characters. And when we have cut constructs up into characters, there is no way to put
4 A very poor choice of name, as this information has absolutely nothing to do with the way that this
letter will be joined to other letters.

```text
Rendering properties
them back together again to rebuild larger characters. For example, Catalan has the ligature ‘l·l’. This ligature is encoded as two Unicode characters: an ‘l·’ 0x0140 latin small
letter l with middle dot and an ordinary ‘l’. But this division may not always be what
we want. Suppose that we wish to place a circumflex accent over this ligature, as we might
well wish to do with the ligatures ‘œ’ and ‘æ’. How can this be done in Unicode?
To allow users to build up characters in constructs that play the rôle of new characters,
Unicode introduced three new properties (grapheme base, grapheme extension, grapheme
link) and one new character: 0x034F combining grapheme joiner.
First, a bit of jargon: a grapheme cluster is a generalization of the notion of combining
characters. A character is in itself a grapheme cluster. When we apply non-spacing
or enclosing combining characters to it, we extend the cluster. In certain cases, a
grapheme cluster can also be extended with spacing combining characters. There are
16 instances of this type, and they are listed in the file PropList.txt under the property
Other_Grapheme_Extend.
To obtain all the grapheme extenders, we take the characters of Other_Grapheme_Extend
type together with all the Unicode characters of category Mn (mark, non-spacing) or Me
(mark, enclosing).
Up till now there has been nothing especially spectacular. The 16 spacing characters in
Other_Grapheme_Extend have very special behavior because they merge with the original consonant and produce only one image with it. Take the Bengali letter ‹ and the
character › 0x09D7 bengali au length mark, which is a member of the very exclusive
club of spacing grapheme extenders. Together, these characters form the new grapheme
cluster ‹›.
Spectacular things start to happen when we add two other concepts: grapheme links and
the grapheme joiner. To understand grapheme links, we will need to review some properties of the languages of India and Southeast Asia. The consonants in these languages have
an inherent vowel, most often a short ‘a’. Thus, whereas in the West the sequence “kt”
is actually pronounced “kt” (as in the word “act”), in Bengali the concatenation of these
two letters of the alphabet, fi‡, yields “kata”. To get rid of the inherent vowel of fi, we use
a special sign, called virama. The sequence fifl‡ is pronounced “kta”. Here the opposite of
Mies van der Rohe’s principle “less is more” applies: we write more to represent fewer
sounds.
But have we not forgotten the Kama Sutra and the erotic sculptures of Khajuraho? Indian
scripts would have no charm at all if things stopped at that point. In fact, under the effect
of the virama, the two letters intertwine themselves to form the pretty ligature ·, which
is—obviously—just a single grapheme. And since it is the virama that played the rôle of
go-between and brought these letters together, we assign it a special Unicode property,
that of grapheme joiner. There are only 14 characters of this type; they are listed in PropList.txt under the property Grapheme_Link.
All Unicode characters that are not grapheme extenders or grapheme joiners and that
are not in any of the categories Cc, Cf, Cs, Co, Cn, Zl, and Zp have the property of
grapheme base.
```

```text
The reader must be wondering: if all the grapheme joiners are from the Indian and
Southeast Asian scripts, is there nothing left for the West? Did we carry out sexual liberation for naught? Of course not. Unicode provides us with a special character, 0x034F
combining grapheme joiner, or CGJ. By placing this character between any two Unicode characters, the latter merge into a single grapheme. Of course this union is rather
platonic: there will be neither intermingling nor necessarily the formation of a ligature.
There are two reasons: first, glyphs can form a ligature on their own, quite without the
assistance of a CGJ; second, a ligature such as ‘fi’ may well be a single glyph, but it is still a
string of two characters. If a ligature incidentally happens to form, the essence of joining
graphemes is not present; it appears at an abstract, institutional level.
We use the grapheme joiner, for example, to apply a combining character to two glyphs
at once. Thus, if the digit ‘5’ followed by 0x20DD combining enclosing circle yields ,
then to obtain ~ we can use the following string of characters: “five” CGJ “zero” “enclosing circle”. Our digits “five” and “zero” in ~ are quite puritanical: even when enclosed in
this cocoon they do not touch each other!
What will happen if we apply the CGJ to the letters ‘f’ and ‘i’? We will still have an ‘fi’
ligature. The difference will become visible when we apply a combining character: ‘f’ ‘i’
followed by the combining circumflex accent will yield ‘fî’; however, ‘f’ CGJ ‘i’ followed
by the same accent will yield ‘‚’, which illustrates that “f CGJ i” is henceforth considered
to be connected by grapheme links in the eyes of Unicode.
Numeric properties
Some characters may be used as digits, a trivial example being ‘3’ 0x0033 digit three,
which is part of the curriculum about halfway through nursery school. For a young
reader of Tamil, this digit is written ‘„’ 0x0BE9 tamil digit three, but the semantics
are the same. The fact that we all have ten fingers must certainly have favored base-ten
arithmetic, without regard for language, religion, or skin color.
It is interesting to know that „ is the number three, even if we are not readers of Tamil.
For that reason, Unicode set aside three fields in UnicodeData.txt: value of decimal digit
(field 6), value of digit or value of numeral (field 7), and numeric value or value of alphanumeric numeral (field 8). Once again we are baffled by the subtleties of the jargon being
used: what exactly distinguishes these three fields?
Value of decimal digit is the strictest of the fields. The only characters that are “decimal
digits” are those that act as—decimal digits. Thus ‘1’ is a decimal digit, ‘’ is a decimal
digit (in Arabic), ‘‰’ is a decimal digit (in Amharic), etc. These characters combine with
their associates to form numbers in a system of decimal numeration.
By contrast, ‘’ is not a “decimal digit” (the teacher would be rather unhappy if we wrote
+ = ), ‘3’ is not a “decimal digit” (it is a superscript), ‘III’ is not a “decimal digit” (the
Roman numeral system is not decimal, in the sense that a1a2a3 cannot be interpreted as
“a1 hundreds plus a2 tens plus a1 units”), etc.
The difference between “digit” and “number” is clearer: if the numeric value of the symbol is in the set {0,1,2,3,4,5,6,7,8,9}, then the symbol is a “digit”; otherwise, it is a
```

```text
Identifiers
“number”. There are many examples of “numbers” in the various writing systems: “Â”
is the number 1,000 in Tamil, ‘ÁD’ is 1,000 in Roman numerals, ‘Ê’ is 10,000 in Amharic.
There are also Unicode characters that represent fractions: “4, 2” are also “numbers”,
and their numeric values appear in field 8 of UnicodeData.txt.
Programmers might well wish that they had sixteen fingers, not so that they could type
more quickly but because their system of numeration is hexadecimal, whose digits are 0–
9 and A–F. Unicode provides a property called “hexadecimal digit” for characters that
can be used in this system of numeration. There are 44 of them, and they are listed in
PropList.txt under the property Hex_Digit. And for purists who live on a strict diet of
pure, organic, fat-free ASCII, there is a subset of these: the “ASCII hexadecimal digits”.
There are 22 (0–9, A–F, a–f), and they are listed under the property ASCII_Hex_Digit.
Identifiers
In Chapter 10, which discusses fonts and the Web, we shall give a quick introduction
to XML (pages 345–349), and we shall discuss tags for elements and entities. The reader
will notice that we have carefully refrained from defining the way in which this markup
is constructed—a subject that is not necessarily of interest to the XML novice.
A priori, we can regard XML tags as being written with ASCII letters and digits; at least
that is what we shall see in all the examples. That is true for good old SGML but not for
young, dynamic XML, which proudly proclaims itself “Unicode compatible”. We are free
to use <книга>, <βιβλον>, <	>, &lt;girw&gt;, <読本>, and other exotic tags!
But does that really mean that we can use just any Unicode character in the names of
our tags? No. By this point, the reader will certainly be aware that the various scripts of
the world have largely the same structures as ours: letters (or similar), diacritical marks,
punctuation marks, etc. Therefore we shall do in other scripts as we do in our own: letters
will be allowed in tag names; diacritical marks will also be allowed but may not come
first; punctuation marks will not be allowed (with a few exceptions).
But XML is not the only markup system in the world—to say nothing of all the various
programming languages, which have not tags but identifiers. Should every markup system and every programming language be allowed to choose the Unicode characters that
it prefers for its tags/identifiers? We would have no end of confusion.
Fortunately, the Unicode Consortium took control of the situation and defined two character properties: identifier start (property ID_Start) and identifier continue (ID_Continue).
That means that we can begin an identifier with any character that has the former property and continue the identifier with any character having the latter property. Of course,
the latter set of characters is a superset of the former.
There are 90,604 ID_Start characters and 91,815 ID_Continue characters in Unicode.
They are listed in DerivedCoreProperties.txt.
We shall see in the section on normalization that there are two other properties:
XID_Start and XID_Continue, which correspond to sets identical to those just mentioned, with the exception of about thirty characters. The advantage of these two
```

properties is that they are compatible with Unicode’s various normalization formats.
Thus we will not be in danger of ending up with non-compliant tags after normalization
of an XML document.
Reading a Unicode block
On pages 121 and 122, we have reproduced (with the kind permission of the Unicode
Consortium given to us by Lisa Moore) two pages of the Unicode book [335]. They are
for the “Latin Extended-A” block, which contains Latin characters too exotic to be included in ISO 8859-1 but not bizarre enough to be in “Latin Extended-B”.
The page that illustrates the block’s layout needs no explanation: under each representative glyph, there is the hexadecimal code for the corresponding Unicode character. The
representative glyphs are set in the same Times-style font as the body text. In this table,
we find four characters that are familiar to us for having been omitted from ISO 8859-1:
‘Œ and ‘œ’ (0x0152 and 0x0153), ‘Ÿ’ (0x0178), and ‘f ’ (0x017F) (the long “s”).
Let us now examine the list of character descriptions, page 122. The title “European
Latin” in bold Helvetica is a subdivision of the table according to the characters’ purpose;
in this case, it is the only subdivision.
For each character, we have information listed in three columns: the first column contains the character’s code point in hexadecimal, the second shows the representative
glyph, and the third contains the name and a certain number of other details.
The character name is written in capitals: “LATIN CAPITAL LETTER A WITH MACRON”. This name is definitive and may not be changed for all of eternity. If it contains
errors, they will remain in place to plague future generations for as long as Unicode
is used.
On the other hand, the Consortium retains the right to annotate character names. An
annotation begins with a bullet • and is considered an informative note, with no prescriptive significance, intended to assist with the use of the character. In the illustration,
we see annotations to the effect that ‘%’ is a letter in Latvian and Latin, that ‘5’ is a letter in
Polish and Croatian, that ‘d’ ’ with an apostrophe is the preferred form of “d with háˇcek”
(we are not told which other forms exist), that we must not confuse the Croatian ‘Æ’ with
the ‘Ò’ (not shown in the text) of Americanist orthographies, etc.
Besides the annotations, we also have alternative names. An alternative name is an additional name given to a character, with no prescriptive significance. It always begins with
the equals sign. There are no alternative names in the example presented here, but two
pages later in the Unicode book we find:
setlength
extrarowheight0dd
œ
LATIN SMALL LIGATURE OE
= ethel (from Old English eðel)
• French, IPA, Old Icelandic, Old English, ...
→00E6 æ latin small letter ae
→0276 œ latin letter small capital oe

The Unicode Standard 5.0, Copyright © 1991-2006 Unicode, Inc. All rights reserved. 017F Latin Extended-A Ā ā Ă ă Ą ą Ć ć Ĉ ĉ Ċ ċ Č č Ď ď   Ē ē Ĕ ĕ Ė ė Ę ę Ě ě Ĝ ĝ Ğ ğ Ġ ġ Ģ ģ Ĥ ĥ ( ) Ĩ ĩ Ī ī Ĭ ĭ Į į İ ı Ĳ ĳ Ĵ ĵ Ķ ķ Ĺ ĺ Ļ ļ Ľ ľ   Ł ł Ń ń Ņ ņ Ň ň ŉ Ŋ ŋ Ō ō Ŏ ŏ Ő ő Œ œ Ŕ ŕ Ŗ ŗ Ř ř Ś ś Ŝ ŝ Ş ş Š š Ţ ţ Ť ť _ ` Ũ ũ Ū ū Ŭ ŭ Ů ů Ű ű Ų ų Ŵ ŵ Ŷ ŷ Ÿ Ź ź Ż ż Ž ž ſ 010A 010B 010C 010D 010E 010F 011A 011B 011C 011D 011E 011F 012A 012B 012C 012D 012E 012F 013A 013B 013C 013D 013E 013F 014A 014B 014C 014D 014E 014F 015A 015B 015C 015D 015E 015F 016A 016B 016C 016D 016E 016F 017A 017B 017C 017D 017E 017F A B C D E F

The Unicode Standard 5.0, Copyright © 1991-2006 Unicode, Inc. All rights reserved.
012D
Latin Extended-A
ĕ
LATIN SMALL LETTER E WITH BREVE
• Malay, Latin, ...
≡ 0065 e  0306 
Ė
LATIN CAPITAL LETTER E WITH DOT ABOVE
≡ 0045 E  0307 
ė
LATIN SMALL LETTER E WITH DOT ABOVE
• Lithuanian
≡ 0065 e  0307 
Ę
LATIN CAPITAL LETTER E WITH OGONEK
≡ 0045 E  0328 
ę
LATIN SMALL LETTER E WITH OGONEK
• Polish, Lithuanian, ...
≡ 0065 e  0328 
011A
Ě
LATIN CAPITAL LETTER E WITH CARON
≡ 0045 E  030C 
011B
ě
LATIN SMALL LETTER E WITH CARON
• Czech, ...
≡ 0065 e  030C 
011C
Ĝ
LATIN CAPITAL LETTER G WITH CIRCUMFLEX
≡ 0047 G  0302 
011D
ĝ
LATIN SMALL LETTER G WITH CIRCUMFLEX
• Esperanto
≡ 0067 g  0302 
011E
Ğ
LATIN CAPITAL LETTER G WITH BREVE
≡ 0047 G  0306 
011F
ğ
LATIN SMALL LETTER G WITH BREVE
• Turkish, Azerbaijani
→ 01E7 ǧ  latin small letter g with caron
≡ 0067 g  0306 
Ġ
LATIN CAPITAL LETTER G WITH DOT ABOVE
≡ 0047 G  0307 
ġ
LATIN SMALL LETTER G WITH DOT ABOVE
• Maltese, Irish Gaelic (old orthography)
≡ 0067 g  0307 
Ģ
LATIN CAPITAL LETTER G WITH CEDILLA
≡ 0047 G  0327 
ģ
LATIN SMALL LETTER G WITH CEDILLA
• Latvian
• there are three major glyph variants
≡ 0067 g  0327 
Ĥ
LATIN CAPITAL LETTER H WITH CIRCUMFLEX
≡ 0048 H  0302 
ĥ
LATIN SMALL LETTER H WITH CIRCUMFLEX
• Esperanto
≡ 0068 h  0302 
LATIN CAPITAL LETTER H WITH STROKE
LATIN SMALL LETTER H WITH STROKE
• Maltese, IPA, ...
→ 045B ћ  cyrillic small letter tshe
→ 210F   planck constant over two pi
Ĩ
LATIN CAPITAL LETTER I WITH TILDE
≡ 0049 I  0303 !
ĩ
LATIN SMALL LETTER I WITH TILDE
• Greenlandic (old orthography)
≡ 0069 i  0303 !
012A
Ī
LATIN CAPITAL LETTER I WITH MACRON
≡ 0049 I  0304 \$
012B
ī
LATIN SMALL LETTER I WITH MACRON
• Latvian, Latin, ...
≡ 0069 i  0304 \$
012C
Ĭ
LATIN CAPITAL LETTER I WITH BREVE
≡ 0049 I  0306 
012D
ĭ
LATIN SMALL LETTER I WITH BREVE
• Latin, ...
≡ 0069 i  0306 
European Latin
Ā
LATIN CAPITAL LETTER A WITH MACRON
≡ 0041 A  0304 \$
ā
LATIN SMALL LETTER A WITH MACRON
• Latvian, Latin, ...
≡ 0061 a  0304 \$
Ă
LATIN CAPITAL LETTER A WITH BREVE
≡ 0041 A  0306 
ă
LATIN SMALL LETTER A WITH BREVE
• Romanian, Vietnamese, Latin, ...
≡ 0061 a  0306 
Ą
LATIN CAPITAL LETTER A WITH OGONEK
≡ 0041 A  0328 
ą
LATIN SMALL LETTER A WITH OGONEK
• Polish, Lithuanian, ...
≡ 0061 a  0328 
Ć
LATIN CAPITAL LETTER C WITH ACUTE
≡ 0043 C  0301 /
ć
LATIN SMALL LETTER C WITH ACUTE
• Polish, Croatian, ...
→ 045B ћ  cyrillic small letter tshe
≡ 0063 c  0301 /
Ĉ
LATIN CAPITAL LETTER C WITH CIRCUMFLEX
≡ 0043 C  0302 
ĉ
LATIN SMALL LETTER C WITH CIRCUMFLEX
• Esperanto
≡ 0063 c  0302 
010A
Ċ
LATIN CAPITAL LETTER C WITH DOT ABOVE
≡ 0043 C  0307 
010B
ċ
LATIN SMALL LETTER C WITH DOT ABOVE
• Maltese, Irish Gaelic (old orthography)
≡ 0063 c  0307 
010C
Č
LATIN CAPITAL LETTER C WITH CARON
≡ 0043 C  030C 
010D
č
LATIN SMALL LETTER C WITH CARON
• Czech, Slovak, Slovenian, and many other
languages
≡ 0063 c  030C 
010E
Ď
LATIN CAPITAL LETTER D WITH CARON
• the form using caron/hacek is preferred in all
contexts
≡ 0044 D  030C 
010F
ď
LATIN SMALL LETTER D WITH CARON
• Czech, Slovak
• the form using apostrophe is preferred in
typesetting
≡ 0064 d  030C 
LATIN CAPITAL LETTER D WITH STROKE
→ 00D0 Ð  latin capital letter eth
→ 0111 :  latin small letter d with stroke
→ 0189 Đ  latin capital letter african d
:
LATIN SMALL LETTER D WITH STROKE
• Croatian, Vietnamese, Sami
• an alternate glyph with the stroke through the
bowl is used in Americanist orthographies
→ 0110 9  latin capital letter d with stroke
→ 0452 ђ  cyrillic small letter dje
Ē
LATIN CAPITAL LETTER E WITH MACRON
≡ 0045 E  0304 \$
ē
LATIN SMALL LETTER E WITH MACRON
• Latvian, Latin, ...
≡ 0065 e  0304 \$
Ĕ
LATIN CAPITAL LETTER E WITH BREVE
≡ 0045 E  0306 

Reading a Unicode block in which we learn that the ‘œ’ ligature is used not only in French but also in Old English, where it had the pretty name eðel, and in Old Icelandic. But let us return to our example, which still has plenty of things to teach us. The lines that begin with an arrow →are either “explicit inequalities” (which indicate likely sources of confusion with other characters whose glyphs are similar) or “linguistic relationships” (transliterations or phonetic similarities). In reality, these lines have to be understood as comments that show how the character is related to other characters in Unicode. Thus we can find the following under the name of the character 0x0110 latin capital letter d with stroke: →00D0 Ð latin capital letter edh →0111 Æ latin small letter d with stroke →0189 Ð latin capital letter african d Of these three lines, the first and the third are “inequalities”: they warn us not to mistake this character for the Icelandic eth or the African “barred D” used in the Ewe language. The second line simply refers us to the corresponding lowercase letter, which incidentally is the next one in the table. And this is what we find under 0x0111 latin small letter d with stroke: →0110 Ð latin capital letter d with stroke →0452 r cyrillic small letter dje The first line is a cross-reference back to the uppercase version. The second line is a “linguistic relationship”: we learn that this letter, as used in Croatian, has a Serbian counterpart, the letter ‘r’. This information can be useful when transliterating between the two alphabets. When a line begins with an “identical to” sign ≡, the character can be decomposed into others, and this line shows its canonical decomposition. This decomposition is, by definition, unique and always consists of either one or two characters. When there are two characters, the first is a base character and the second is a combining character. Thus we see that the canonical decomposition of ‘ ’ is the letter ‘A’ followed by the macron. We shall discuss compositions and decompositions in the next chapter. Another type of decomposition, which is not illustrated on this page, is the compatibility decomposition. This represents a compromise that can be made when the software’s configuration does not allow us to use the original character. Thus, two pages later, we see the description of the character 0x0149, which, as shown by its representative glyph, is an apostrophe followed by an ‘n’. This letter is used in Afrikaans, the language of the colonists of Dutch origin in South Africa. Here is the full description of this letter:

’n
LATIN SMALL LETTER N PRECEDED BY
APOSTROPHE
= LATIN SMALL LETTER APOSTROPHE N
• Afrikaans
• this is not actually a single letter
≈02BC ’ 006E n
The line that begins with ≈is a compatibility decomposition. Visually, the result is
the same.
When we make a compatibility decomposition, we always lose information. If the author
of a document has used an Afrikaans ‘ ’n’, he must have had a good reason to do so. On
the other hand, if our Stone Age software cannot correctly display, sort, and search for
this character, it is better for it to use an apostrophe followed by an ‘n’ than nothing at all.
As always, there is a trade-offbetween rigor and efficiency.
And since we are talking about “display”, why not also add display attributes to the
compatibility decomposition? After all, in some cases a little assistance in the area of
rendering may lead to a better simulation of the missing character. Unicode provides
16 formatting “tags”,5 which we can find in the descriptions of compatibility decompositions:
• &lt;font&gt;: a judicious choice of font will make the greatest improvement to the little
trick that we are perpetrating. This tag is used no fewer than 1,038 times in Unicode.
For example, the character ‘R’ 0x211C black-letter capital r, used in mathematics for the real part of a complex number, has the compatibility decomposition “≈
&lt;font&gt; 0052 R latin capital letter r”. In other words, if the software does not know
how to display the symbol for the real part of a complex number, take a [Fraktur]
font and set the ‘R’ in that font, and the representation will be adequate. Unicode
does not go so far as to specify which font to use, but reading Chapter 11 of the
present book will certainly help the reader to make a good choice.
• &lt;noBreak&gt;: the non-breaking version of what follows. Example: the character ‘-’
0x2011 non-breaking hyphen is a hyphen at a point where a line break may not
occur. Its compatibility decomposition is “≈&lt;noBreak&gt; 2010 - hyphen”. Here we
go further to ensure correct rendering: we tell the software how the character in
question behaves.
• &lt;initial&gt;: an initial form of a letter in a contextual script. Used in presentation
forms.
• &lt;medial&gt;: a medial form of a letter in a contextual script. Used in presentation forms.
• &lt;final&gt;: a final form of a letter in a contextual script. Used in presentation forms.
5 Note that these are not XML tags. They have no closing counterpart, and their effect is limited to the
single character immediately following.

Reading a Unicode block
• &lt;isolated&gt;: an isolated form of a letter in a contextual script. Used in presentation
forms.
• &lt;circle&gt;: an encircled symbol, such as ‘	’, ‘©’, etc.
• &lt;super&gt;: a superscript, such as ‘1’, ‘a’, etc.
• &lt;sub&gt;: a subscript, such as ‘1’, ‘n’, etc.
• &lt;vertical&gt;: a vertical version of the glyph. That may mean “act as if we were setting
type vertically” or “this character is used only in vertical mode”. Thus the character ‘Œ’ 0xFE35 presentation form for vertical left parenthesis has as its compatibility decomposition “≈&lt;vertical&gt;
0028 (”. We know that the parenthesis
ordinarily assumes the appropriate form for the direction of the current script. Here
we have a presentation form; thus we secure the glyph’s vertical orientation.
• &lt;wide&gt;: the full-width versions of certain ASCII characters (like
this).
• &lt;narrow&gt;: the half-width katakana syllables and ideographic punctuation marks ｢ｺﾒ
･ｾｼ｣.
• &lt;small&gt;: small forms. Used only in the mysterious CNS-compatibility block 0xFE500xFE6B.
• &lt;square&gt;: placed within an ideographic square. Thus the compatibility decomposition of ‘㎦’ is “≈&lt;square&gt; 006B k 006D m 00B3 3”.
• &lt;fraction&gt;: fractions. For example, the compatibility decomposition of ‘4’ is “≈
&lt;fraction&gt; 0031 1 2044 / 0032 2”, in which the character 0x2044 is the “fraction
slash”, not to be confused with the ASCII slash.
• &lt;compat&gt;: all other cases. We use this tag in UnicodeData.txt to distinguish compatibility decompositions from canonical decompositions.

```text
Normalization, Bidirectionality,
and East Asian Characters
In this chapter we shall examine three aspects of Unicode that have nothing in common
other than requiring a certain amount of technical background and being of interest
more to the specialist than to the average Unicode user. They are the procedures for
decomposition and normalization (of interest to those who develop Unicode applications for the Web), the bidirectional algorithm (of interest to users of the Arabic, Syriac,
and Hebrew scripts), and the handling of ideographs and hangul syllables (of interest to
readers of Chinese, Japanese, or Korean).
Decompositions and Normalizations
Combining Characters
We have already discussed the block of combining characters, as well as the category of
“marks” and, in particular, the nonspacing marks. But how do these characters work?
The glyph of a combining character interacts with the glyph of a base character. This interaction may take a variety of forms: an acute accent goes over a letter, the cedilla goes
underneath, the Hebrew dagesh goes inside the letter, etc.
Some of these diacritical marks are independent of each other: placing a cedilla underneath a letter in no way prevents a circumflex accent from being added as well. Other
marks are placed in the same location and thus must appear in a specific order. For example, the Vietnamese language has an ‘Ë’ with a circumflex accent and a tilde, in that
order; it would be incorrect to place them the other way around.
```
