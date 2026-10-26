---
title: "Chapter 1: Before Unicode"
description: "Unabridged English text from Yannis Haralambous, Fonts & Encodings: FIELDATA, ASCII, EBCDIC, ISO 2022, ISO 8859 families, East Asian multi-byte encodings, Microsoft and Apple code pages, email and Web encodings."
---

# Chapter 1: Before Unicode
**By Yannis Haralambous, Ph.D. (Translated and Expanded by P. Scott Horne, Ph.D.)**  
*From Fonts & Encodings (O'Reilly Media, 2007), pp. 27–52*

---

When we need precise definitions of computer-related concepts that seem a little fuzzy to us, nothing is more refreshing and beneficial than consulting old documents. For example, in C.E. MacKenzie’s Coded Character Sets, History and Development (1980) [242], we find the following definitions (slightly condensed here):

• a bit is a binary digit, either 0 or 1;

• a bit pattern is an ordered set of bits, usually of fixed length;

• a byte is a bit pattern of fixed length; thus we speak of 8-bit bytes, 6-bit bytes, and so on;

• a graphic is a particular shape, printed, typed, or displayed, that represents an alphabetic, numeric or special symbol;

• a character is a specific bit pattern and a meaning assigned to it: a graphic character has an assigned graphic meaning, and a control character has an assigned control meaning;

• a bit code is a specific set of bit patterns to which either graphic or control meanings have been asigned;

• a code table is a compact matrix form of rows and columns for exhibiting the bit patterns and assigned meanings of a code;

• a shifted code is a code in which the meaning of a bit pattern depends not only on the bit pattern itself, but also on the fact that it has been preceded in the data stream by some other particular bit pattern, which is called a shift character.

All this makes sense; only the terminology has slightly changed. Nowadays a byte is always considered to be of fixed length 8; what MacKenzie calls a “graphic” is now called a glyph; a “bit code” is called an encoding; and a “code table” is simply a way of graphically representing the encoding. In the old days, the position of a character in the encoding was given by a double number: “x/y”, where x is the column number and y the row number. Nowadays we simply give its number in decimal or hexadecimal form. “Shifted” encodings tend to become extinct because they are incompatible with human–user interaction such as copying and pasting, but at that time GUIs were still well-protected experiments in the Palo Alto Xerox Lab.

Let us go even further back in time. It seems that the first people to invent a code-based system for long-distance transmission of information were the Greeks: around 350 bc, as related by the historian Polybius [183], the general Aeneas employed a two-by-five system of torches placed on two walls to encode the Greek alphabet, an alphabet of 24 letters that could be adequately encoded by the 25 = 32 combinations of five lighted or extinguished torches. At the end of the 18th century, the French engineer Claude Chappe established the first telegraphic link between Paris and Lille by using semaphores visible at distances of 10 to 15 kilometers. In 1837, Samuel Morse invented “Morse code” for the electric telegraph, a code that was more complex because it used a variable number of long and short pulses (dahs and dits) for each letter, with the letters being obligatorily separated by pauses. Thus there were two basic units: dahs and dits. It was the first internationally recognized system of encoding.

In 1874, Émile Baudot took up a code invented by Sir Francis Bacon in 1605 and adapted it to the telegraph. Unlike Morse’s code, the Baudot code used codes of five symbols that were typed on a device bearing five keys like those of a piano. Each key was connected to a cable that transmitted signals. The reader will find a detailed description of Baudot’s code and keyboard in [201].

The first important encoding of the twentieth century was CCITT #2, a 58-character shifted 5-bit code, standardized as an international telegraph code in 1931 by CCITT (“Comité Consultatif International Télégraphique et Téléphonique”). Being shifted, it used two “modes”, also called “cases”. The first is the letter case:

00 T 01 cr 02 O 03 sp 04 H 05 N 06 M 07 lf 08 L 09 R 0A G 0B I 0C P 0D C 0E V 0F E

10 Z

11 D

12 B

13 S

14 Y

15 F

16 X

17 A

18 W

19 J

1B U

1C Q

1D K

1A fs

1E ls

1F

Here “lf” is the carriage return, “sp” is the blank space, “lf” is the line feed, and “ls” (letter shift) and “fs” (figure shift) are two escape codes. “fs” shifts to figure case:

00 5 01 cr 02 9 03 sp 04 ***05 , 06 . 07 lf 08 ) 09 4 0A ***0B 8 0C 0 0D : 0E ; 0F 3 10 + 11 ab 12 ? 13 ’ 14 6 15 ***16 / 17 - 18 2 19 bel1A fs 1B 7 1C 1 1D ( 1E ls 1F

Here “***” is intended for national use (#, \$, and & in the US; Ä Ö Ü in Germany, Sweden and Finland; Æ Ø Å in Denmark and Norway), “ab” is used for answering back, and “bel” rings a bell. With “ls” we return to the first version of the encoding. This use of two

states seems awkward to us today; after all, why not just use a sixth bit? One consequence of this approach is that the interpretation of a position within the encoding depends on context—whether we are in “letter” or “figure” case.

In the prehistoric era of computers (the 1930s to the 1960s), only a few brilliant visionaries, such as Alan Turing and Vannevar Bush, imagined that the computer would one day come to use letters. To everyone else, it was just a calculating machine and therefore was good only for processing numbers.

FIELDATA was a 7-bit encoding developed by the US Army for use on military data communication lines. It became a US military standard in 1960:

::: tip Typographical Specimen: FIELDATA Character Matrix (Plate 1-1)
![Plate 1-1: FIELDATA Character Matrix](/images/fonts-encodings/plate1-1-fieldata-table.png)
*Plate 1-1: FIELDATA 6-bit / 7-bit character matrix representation (from original book p. 29).*
:::



ms 40 uc 41 lc 42 lf 43 cr 44 sp 45 A 46 B 47 C 48 D 49 E 4A F 4B G 4C H 4D I 4E J 4F K

50 L

51 M

52 N

53 O

54 P

55 Q

56 R

57 S

58 T

59 U

5A V

5B W

5C X

5D Y

5E Z

5F ) 60 - 61 + 62 < 63 = 64 > 65 _ 66 \$ 67 * 68 ( 69 " 6A : 6B ? 6C ! 6D , 6E stop6F 0 70 1 71 2 72 3 73 4 74 5 75 6 76 7 77 8 78 9 79 ’

7A ;

7B /

7C .

7D spec 7E idle 7F

“ms” stands for “master space”; “uc/lc” are shift codes for uppercase and lowercase letters; “stop”, “spec”, and “idle” stand for “stop”, “special”, and “idle”. In this encoding we already find most of the characters used a few years later in ASCII. FIELDATA survives even today as the internal encoding of certain COBOL software.

Towards the end of the 1950s, the telecommunications industry redoubled its efforts to develop a standard encoding. IBM and AT&T were among the large corporations that drove the ASA (American Standards Association) to define an encoding. Thus ASCII- 1963, a preliminary version of ASCII with no lower-case letters, was born on June 17, 1963, a few months after the assassination of President Kennedy.

ASCII was updated in 1967. From that time on, it would include lower-case letters. Here is ASCII-1967:

::: tip Typographical Specimen: ASCII-1963 / 1967 Matrix (Plate 1-2)
![Plate 1-2: ASCII-1963 / 1967 Character Matrix](/images/fonts-encodings/plate1-2-ascii-table.png)
*Plate 1-2: ASCII-1963 and 1967 code matrix showing control codes, uppercase and lowercase letters.*
:::



nul00 soh01 stx02 etx03 eot04 enq05 ack06 bel07 bs 08 ht 09 lf 0A vt 0B ff 0C cr 0D so 0E si 0F

dle10 dc111 dc212 dc313 dc414 nak15 syn16 etb17 can18 em19 sub1A esc1B fs 1C gs 1D rs 1E us 1F

sp 20 ! 21 " 22 # 23 \$ 24 % 25 & 26 ' 27 ( 28 ) 29 * 2A + 2B , 2C - 2D . 2E / 2F 0 30 1 31 2 32 3 33 4 34 5 35 6 36 7 37 8 38 9 39 : 3A ; 3B < 3C = 3D > 3E ? 3F @ 40 A 41 B 42 C 43 D 44 E 45 F 46 G 47 H 48 I 49 J 4A K 4B L 4C M 4D N 4E O 4F P 50 Q 51 R 52 S 53 T 54 U 55 V 56 W57 X 58 Y 59 Z 5A [ 5B \ 5C ] 5D ^ 5E _ 5F

70 q

71 r

72 s

73 t

74 u

75 v

76 w

77 x

78 y

79 z

7A {

7B |

7C }

7D ˜

7E del

7F

The first thirty-two positions in this encoding are occupied by control codes:

• formatting control codes: cr (carriage return), lf (line feed), bs (backspace), ht (horizontal tab), vt (vertical tab), sp (blank space), ff (form feed);

• extension codes: esc (escape is a shift but modifies only the following character), so (shift out), si (shift in);

• controls for communications: soh (start of heading), stx (start of text), etx (end of text), eot (end of transmission), etb (end of transmission block), ack (acknowledge), nak (negative acknowledge), syn (synchronous idle), nul (null), dle (data link escape);

• device control functions dc1, ... , dc4;

• functions for error management: can (cancel), sub (substitute), del (delete), bel (bell).

Of the characters that do not represent controls, a few call for some explanation:

• The backslash ‘\’, used by DOS as a delimiter for directory paths and by TEX as the escape character for commands, was introduced into encodings in September 1961 and subsequently accepted into ASCII-1963 at the suggestion of Bob Bemer [72]. A great fan of the ALGOL language, Bemer wanted to obtain the logical operators and (∧) and or (∨). Since the forward slash was already present in the encoding, he was able to obtain these two operators by simply concatenating a forward slash and a backslash (‘/\’) and vice versa (‘\/’).

• The apostrophe is represented by a vertical stroke, ‘'’, not by a raised comma, ‘”, as printers have represented it for centuries. Today we call this type of apostrophe a “non-oriented apostrophe”. Although it has a peculiar shape, it is perfectly suitable for those programming languages that use it as the opening and closing delimiter for strings.

• The same goes for the “double quote” or “non-oriented quotation marks”, ‘"’: they served as the opening and closing American-style quotation marks, and even as the diæresis; thus this symbol, too, had to be symmetrical.

• The grave accent ‘`’ also serves as an American-style opening quotation mark.

• The vertical bar ‘|’ was introduced to represent the or operator in the language PL/I [226].

It may seem unbelievable today, but a not insignificant number of ASCII characters could vary according to local needs: the number sign ‘#’, the dollar sign ‘\$’, the at sign ‘@’, the square brackets ‘[’ and ‘]’, the backslash ‘\’, the caret ‘^’, the grave accent ‘`’, the curly braces ‘{’ and ‘}’, the vertical bar ‘|’, and the tilde ‘˜’.

Thus, at one time, France used the NF Z62010 standard and the United Kingdom used the BS 4730 standard, both of which replaced the number sign by the symbol for pounds sterling ‘£’; Japan used the JIS C-6220 standard, which employed a yen sign ‘¥’ in the place of the backslash; the Soviet Union used the GOST 13052 standard, which substituted a universal currency sign ‘´’ for the dollar sign, etc. The reader will find a complete list of these “localized ASCII encodings” in [248, p. 243]. To distinguish it from the localized versions, the original version of ASCII was called IRV (International Reference Version).

Another problem with the ASCII encoding is that it offered a rather naïve and æstheti- cally unacceptable method for placing accents on letters: to obtain an ‘é’, one was asked to type the sequence ‘e bs '’, that is: ‘letter e’, ‘backspace’, ‘apostrophe’. That is why the grave and circumflex accents and the tilde, represented as spacing characters, are found in the encoding. To obtain a diæresis, one used the backspace followed by a double quote; and underscoring words was accomplished with backspaces followed by underscores.

The ASCII-1967 encoding became the ISO 646 standard in 1983. Its latest revision, published by ECMA [192], dates to 1991.

While the computer giant IBM had taken part in the development of ASCII-1963, it released in 1964 a new and highly appreciated line of computers, IBM System/360, whose low-end model came equipped with 24 kb (!) of memory. The development of these machines was the second most expensive industrial project of the 1960s, after NASA’s Apollo program....

The System/360 computers use the EBCDIC encoding (Extended Binary Coded Decimal Interchange Code, pronounced “eb-cee-dic”), an 8-bit encoding in which many positions are left empty and in which the letters of the alphabet are not always contiguous:

::: tip Typographical Specimen: EBCDIC Character Matrix (Plate 1-3)
![Plate 1-3: EBCDIC Character Matrix](/images/fonts-encodings/plate1-3-ebcdic-table.png)
*Plate 1-3: EBCDIC 8-bit character matrix showing discontinuous alphabet blocks (A–I, J–R, S–Z).*
:::



nul00 soh01 stx02 etx03 pf 04 ht 05 lc 06 del07 ge 08 rlf09 smm0A vt 0B ff 0C cr 0D so 0E si 0F

dle10 dc111 dc212 tm13 res14 nl 15 bs 16 il 17 can18 em19 cc 1A cui1B ifs1C igs1D irs1E ius1F

ds 20 sos21 fs 22 23 byp24 lf 25 etb26 esc27 28 29 sm 2A cu22B 2C enq2D ack2E bel2F

30 31 syn32 33 pn 34 rs 35 uc 36 eot37 38 39 3A cu33B dc43C nak3D 3E sub3F

sp 40 41 42 43 44 45 46 47 48 49 ¢ 4A . 4B < 4C ( 4D + 4E | 4F & 50 51 52 53 54 55 56 57 58 59 ! 5A \$ 5B * 5C ) 5D ; 5E ¬ 5F - 60 / 61 62 63 64 65 66 67 68 69 ¦ 6A , 6B % 6C _ 6D > 6E ? 6F

90 j

91 k

92 l

93 m

94 n

95 o

96 p

97 q

98 r

C9 CA CB π

CC CD ∫

C0 A

C1 B

C2 C

C3 D

C4 E

C5 F

C6 G

C7 H

C8 I

E9 EA EB ª

E0 E1 S

E2 T

E3 U

E4 V

E5 W

E6 X

E7 Y

E8 Z

EC ED EE EF 0 F0 1 F1 2 F2 3 F3 4 F4 5 F5 6 F6 7 F7 8 F8 9 F9 | FA FB FC FD FE eo FF

We may well ask: why are the letters of the alphabet distributed in so bizarre a manner in this encoding? Why did IBM insist so firmly on its EBCDIC encoding? To understand what happened, we need a bit of historical background.

In 1801 the Parisian weaver Joseph-Marie Jacquard used strings of punched cards to operate his looms, thus perfecting an invention by Basile Bouchon that dated to 1725. Seventy-nine years later, on the other side of the Atlantic, a census conducted in the United States was ruined. The failure resulted from the fact that it took 7 years (!) to process the data on the country’s 31.8 million residents—so much time that the data were no longer up to date. Faced with this situation, the Census Bureau organized a contest to find an invention that could solve the problem. A certain Herman Hollerith won the contest with a system inspired by that of Jacquard: the census-takers would carry cards that they would punch according to the profile of the person being surveyed. Later a machine, the ancestor of the computer, would read the cards and compile the results.

In 1890 a new census was taken. While the previous census collected only six pieces of information for each person, this time plans were made for 245! The Bureau sent 50,000 employees all over America to conduct the census. And, as had been expected, the results were spectacular: the data were completely processed in less than six weeks. Hollerith had thus succeeded in processing 40 times as much information in 1/56 of the time....

Encouraged by this astounding success, Hollerith founded a company named TMC (Tabulating Machine Company). In 1924 it became International Business Machines, or IBM.

But what relationship is there between Hollerith and EBCDIC? In Figure 1-1, the reader can see a remnant of the past: an ISO 1681 card punched by the author at the University of Lille (France) in September 1983, a few months before this medium disappeared from that university. Punch cards were the user’s means of interacting with the computer before the advent of terminals with screens and keyboards. Note that punch cards have twelve rows, of which two are “unlabeled” (we call them “X” and “Y”) and the remaining ten bear the digits from “0” to “9”. Since there are twelve potential holes, can we therefore encode numbers with 212 = 4,096 bits in a single column on the card? Alas, no.

::: tip Archival Engineering Plate: Punch Card (Figure 1-1)
![Figure 1-1: A punch card (ISO 1681 standard)](/images/fonts-encodings/fig1-1-punch-card-iso-1681.png)
*Figure 1-1: An ISO 1681 80-column punch card showing zone punches (12, 11, 0) and digit punches (1–9).*
:::



In fact, Hollerith quickly noticed that punch cards could not be punched excessively, lest they be torn. Therefore he invented a system by which one could encode letters and numbers without ever using more than two holes per column. The system is called the Hollerith code:

Figure 1-1: A punch card (ISO 1681 standard).

Holes 0 1 2 3 4 5 6 7 8 9

with X punched A B C D E F G H I

with Y punched J K L M N O P Q R

with 0 punched S T U V W X Y Z

neither X nor Y punched 0 1 2 3 4 5 6 7 8 9

In other words, to obtain an ‘A’, one punches row “X” and row “1”; to obtain a ‘Z’, one punches row “0” and row “9”; to obtain a digit, one punches only one hole—the one corresponding to that digit.

The reader will readily recognize the last four lines of the EBCDIC encoding. How could IBM have ever abandoned the code created by its legendary founder?

Despite the awkwardness of this encoding, IBM spread it to the four corners of the earth. The company created 57 national versions of EBCDIC. All of them suffer from the same problem: they lack certain ASCII characters, such as the square brackets, that are indispensable for computer programming.

Extremely rare today, the EBCDIC encoding is nonetheless very much alive. As recently as 1997, an article appeared in Perl Journal on the use of Perl 5 in an EBCDIC environment under IBM System/390 [298].

In the early 1970s, the industry was well aware of the fact that the “localized” versions of ASCII were an impediment. People had to use multiple encodings that were really quite different, and sooner or later they had to switch from one encoding to another in the middle of a document or a transmission. But how to indicate this change of encoding?

C0 C1 GL GR

Figure 1-2: The manner in which ISO 2022 subdivides the 8-bit table.

::: tip Architecture Diagram: ISO 2022 Subdivisions (Figure 1-2)
![Figure 1-2: Subdivisions of an 8-bit space in ISO 2022](/images/fonts-encodings/fig1-2-iso-2022-subdivisions.png)
*Figure 1-2: Subdivisions of an 8-bit space into C0, GL, C1, and GR zones in ISO 2022.*
:::



It was for this reason that the ISO 2022 standard emerged, in 1973. Its latest revision dates to 1994 [193]. It is not an encoding but a definition of a certain number of escape sequences that make it possible to use as many as four distinct encodings within the same set of data.

ISO 2022 starts from the principle that the 256 squares in a table of 8 bits are distributed among four zones, which can be seen in Figure 1-2. Zones C0 and C1 are reserved for control characters, and zones GL (“L” for “left”) and GR (“R” for “right”) are reserved for what today are known as alphanumeric characters (and what at the time bore the oxymoronic name “graphic characters”, whence the ‘G’).

Thus we have up to four distinct encodings at our disposal. Let us call them G0, G1, G2, G3. These encodings may be of any of four types:

• Encodings with 94 positions: 6 columns with 16 positions each, minus the two excluded positions, namely the first and the last.

• Encodings with 96 positions: 6 columns with 16 positions each.

• Encodings with 94n positions, if we use n bytes to encode a single character. Thus for ideographic languages we will take n = 2, and we will therefore have encodings of 942 = 8,836 positions.

• Encodings with 96n positions, if we use n bytes to encode a single character. By taking n = 2, we will obtain encodings with 962 = 9,216 positions.

There is only one small constraint: encoding G0 must necessarily be of type 94 or 94n.

A first series of escape sequences allows us to specify encodings G0, G1, G2, G3. These sequences depend on the type of the encoding. Thus, for example, the sequences ‘esc 0x2D

F’, ‘esc 0x2E F’, ‘esc 0x2F F’, in which ‘F’ is an identifier for an encoding with 96 positions, declares that the encoding designated by ‘F’ is assigned to G1, G2, or G3, respectively.

To identify the encoding, we use identifiers defined by the “competent authority”, which today is the Information Processing Society of Japan [196]. The IPSJ’s Web site provides a list of encodings.1 There we can discover, for example, that the ISO 8859-1 encoding that we shall discuss below is registered under the number 100 and has the identifier “4/1”, an old-fashioned way to represent the hexademical number 0x41. It is an encoding with 96 positions; therefore, it cannot be assigned to G0. The escape sequences ‘esc 0x2D 0x41’, ‘esc 0x2E 0x41’, and ‘esc 0x2F 0x41’ will therefore serve to declare ISO 8859-1 as encoding G1, G2, or G3.

Once the Gn have been defined, we can use them. There are escape sequences that switch the active encoding until further notice. To do so, they must implement a finite automaton. These sequences consist either of ASCII control characters (so and si assign G0 and G1 to zone GL) or of pairs of bytes beginning with esc: thus ‘esc 0x7E’ will select G1 for zone GR, ‘esc 0x6F’ will select G3 for zone GL, etc.

There are also control characters for zone C1 that affect only the following character: ss2 (0x8E) and ss3 (0x8F) specify that only the following character should be interpreted as being in encoding G2 or G3, respectively. The idea is that G2 and G3 may be rare encodings from which we draw only isolated characters now and then; it therefore makes more sense to “flag” them individually.

ISO 2022 is based on the principle of total freedom to define new encodings. Indeed, all that it takes to make an encoding an integral part of ISO 2022 is to register it with the competent authority. And there are so many registered encodings today that it is practically impossible for a computer developer to support all of them. The only viable alternative is to limit oneself to a small number of recognized and widely used encodings—the ISO 2022-* instances that Ken Lunde has described [240, p. 147].

Thus we have, for example, ISO 2022-JP (defined in RFC 1468), which is a combination of ASCII, JIS-Roman (JIS X 0201-1976), JIS X 0208-1978, and JIS X 0208-1983 (taken, respectively, as encodings G0, G1, G2, G3). This is how we resolve the problem of rare ideographic characters: we put ASCII and the most common ideographic characters in G0 and G1, and we reserve G2 and G3 for the rare cases, in which we select the required characters individually.

As soon as the ISO 2022 standard allowed multiple encodings to be combined in a single data flow, ISO started to define encodings with 96 positions that would supplement ASCII. This became the ISO 8859 family of encodings, a family characterized by its longevity—and its awkwardness.

1 This Web site is a gold mine for historians of computer science, as it offers a PDF version of the description of each registered encoding!

The new standard’s flagship, ISO 8859-1, was launched in 1987. By 1990, Bernard Marti had written [248, p. 257]: “Unfortunately, the haste with which this standard was established [... ] and its penetration into stand-alone systems have led to incoherence in the definition of character sets.”

This flagship is dedicated to the languages of Western Europe. Here is part GR of the standard (parts C0 and GL are identical to those of ASCII, and part C1 was not included in the new standard):

::: tip Typographical Specimen: ISO 8859-1 (Latin-1) High-Order Table (Plate 1-4)
![Plate 1-4: ISO 8859-1 (Latin-1) Table](/images/fonts-encodings/plate1-4-iso8859-1-table.png)
*Plate 1-4: ISO 8859-1 (Latin-1) upper GR region (0xA0–0xFF) showing accented letters and symbols.*
:::



B0 ±

B4 μ

B6 · B7 ¸

B1 ²

B2 ³

B3 ´

B5 ¶

B8 ¹

B9 º

BA »

BB ¼

BC ½

BD ¾

BE ¿

D6 ×

D0 Ñ

D1 Ò

D2 Ó

D3 Ô

D4 Õ

D5 Ö

D7 Ø

D8 Ù

D9 Ú

DA Û

DB Ü

DC Ý

DD Þ

DE ß

F6 ÷

F0 ñ

F1 ò

F2 ó

F3 ô

F4 õ

F5 ö

F7 ø

F8 ù

F9 ú

FA û

FB ü

FC ý

FD þ

FE ÿ

FF

Certain symbols deserve a few words of explanation:

• nbsp is the non-breaking space.

• ‘¡’ and ‘¿’ are the Spanish exclamation point and question mark used at the beginning of a sentence. Thanks to these characters, we avoid in Spanish the rather annoying experience of coming to the end of a sentence only to discover that it was a question or an exclamation—and that we shall have to read the whole sentence over again in order to give it the proper intonation.

• ‘¢’, ‘£’, and ‘¥’ are currency symbols: the cent sign, the British pound, and the Japanese yen.

• ‘´’ is the “universal currency sign”. The Italians were the ones to propose this symbol as a replacement for the dollar sign in certain localized and “politically correct” versions of ASCII. The author has never seen this symbol used in text and cannot even imagine any use for it.

• ‘ª’ and ‘º’ are used in Spanish, Italian, and Portuguese for numerals (the first being feminine and the second masculine): ‘1ª, ‘2º’, etc.

• shy, the “soft hyphen”, may be the least coherent character in the encoding. In ISO 8859-1 it is described as a “hyphen resulting from a line break”, while in Unicode, which ordinarily follows ISO 8859-1 to the letter, it is described as “an invisible character whose purpose is to indicate potential line breaks”. The reader will find a full discussion in [225].

• Unless we use a font such as Futura in which the letter ‘o’ is a perfect circle, we must not confuse the “degree sign °” (position 0xB0) with the “superscript o º” (position 0xBA). The first is a perfect circle, whereas the latter is a letter ‘o’ written small. Thus we write “nº” but “37,2°C”.

• The “midpoint” ‘·’ is used to form the Catalan ligature ‘l·l’ [135];

• the German eszett ‘ß’ must not be mistaken for a beta. Historically, it comes from the ligature “long s–round s”. Its upper-case version is ordinarily ‘SS’ but can also be ‘SZ’ to distinguish certain words. Thus, in German, MASSE is the uppercase version of Masse (= mass), whereas MASZE is the one of Maße (= measures);

• the “y with diæresis” is used in Welsh and in Old French. We find it in Modern French in place names such as “l’Haÿe-les-Roses”, surnames such as “de Croÿ” and “Louÿ”, or expressions such as “kir à l’aÿ” [36]. This letter is extremely rare, and its inclusion in ISO 8859-1 is peculiar at best.

But the biggest deficiency in ISO 8859-1 is the lack of certain characters:

• While ‘ÿ’ is extremely rare in French, the ligature ‘œ’ is not. It appears in many very common French words (“cœur” ‘heart’, “œil” ‘eye’, etc.); in some other words—less common ones, to be sure, but that is neither here nor there—it is not used: “moelle” ‘marrow’, “coefficient”, “coexistence”, “foehn”, etc. According to an urban legend, the French delegate was out sick the day when the standard came up for a vote and had to have his Belgian counterpart act as his proxy. In fact [36], the French delegate was an engineer who was convinced that this ligature was useless, and the Swiss and German representatives pressed hard to have the mathematical symbols ‘×’ and ‘÷’ included at the positions where Œ and œ would logically appear.

• French is not the only language neglected by ISO 8859-1. Dutch has another ligature, ‘ij’ (which, in italics, looks dangerously close to a ‘ÿ’, a fact that has led to numerous misunderstandings [161, note 4]). This ligature is just as important as the French ‘œ’—perhaps even more important, as it has acquired the status of a letter in certain situations. Thus, in some Dutch encyclopædias, the entries are sorted according to an order in which ‘ij’ appears between ‘w’ and ‘y’. The upper-case version of ‘ij’ is ‘IJ’, as in the name of the city “IJmegen”.

• Finally, if only for reasons of consistency, there should also be a ‘Ÿ’, the upper-case version of ‘ÿ’.

• it has become the standard encoding for Unix;

• Unicode is an extension of it;

• at least in Western Europe, most Web browsers and electronic-mail software have long used it as the default encoding when no encoding was specified.

The languages covered by ISO 8859-1 are Afrikaans, Albanian, Basque, Catalan (using the midpoint to form the ligature ‘l·l’), Dutch (without the ligature ‘ij’), English, Faeroese, Finnish, French (without the ligature ‘œ’ and without ‘Ÿ’), German, Icelandic, Italian, Norwegian, Portuguese, Rhaeto-Romance, Scottish Gaelic, Spanish, and Swedish.

In March 1999, when the euro sign was added, ISO took advantage of the opportunity to correct two other strategic errors: first, the free-standing accent marks were eliminated; second, the ligatures ‘Œ’ and ‘œ’ and the letter ‘Ÿ’, needed for French but missing from the encoding, were finally introduced; third, the letters “Ž ž Š š”, which are used in most Central European languages and which can be useful in personal and place names, were also added. After the fall of the Soviet Union, the euro sign took the place of the universal monetary symbol.

The new standard was called ISO 8859-15 (or “Latin-9”). It differs from ISO 8859-1 in only eight positions (shown in black in the following diagram):

AB ¬

A0 ¡

A1 ¢

A2 £

A3 ¤

A4 ¥

A5 Š

A6 §

A7 š

A8 ©

A9 ª

AA «

AD ®

AE ¯

nbsp

AC shy

AF ° B0 ± B1 ² B2 ³ B3 Ž B4 μ B5 ¶ B6 · B7 ž B8 ¹ B9 º BA » BB ŒBC œ BD Ÿ BE ¿ BF

After ISO 8859-1, which is also known as ISO Latin-1, three other encodings for the Latin alphabet came out: one each for the countries of Eastern Europe (ISO 8859-2), Southern Europe (ISO 8859-3), and Northern Europe (ISO 8859-4).

Thus ISO 8859-2 (or “Latin-2”) includes the characters needed for certain languages of Central Europe: Bosnian, Croatian, Czech, Hungarian, Polish, Romanian (but with a cedilla instead of a comma under the letters ‘¨’ and ‘≠’), Slovak, Slovenian, and Sorbian. It also contains the characters needed for German (commercial influence at work) and some of the characters needed for French (some accented capitals are missing):

AA ˇT

AE ˙Z

A3 ´

A5 0 A6 §

AB 3 AC shy

A0 ˛ A

A1 ˘

A2 Ł

A4 L’

A7 ¨

A8 Š

A9 ¸S

AD Ž

nbsp

AF ° B0 ˛a B1 . B2 ł B3 ´ B4 l’ B5 6 B6 ˇ B7 ¸ B8 š B9 ¸s BA t’ BB 9 BC ˝ BD ž BE ˙z BF 2 C0 Á

C2 ˘A

C7 ˇC

CB ˇE

CE ˇD

C4 4 C5 /

C1 Â

C3 Ä

C6 Ç

C8 É

C9 ˛E

CA Ë

CC Í

CD Î

CF Ð D0 1 D1 ˇN D2 Ó D3 Ô D4 ˝O D5 Ö D6 × D7 ˇR D8 ˚U D9 Ú DA < DB Ü DC Ý DD ¸T DE ß DF 8 E0 á

E4 :

E5 5 E6 ç

EB ˇe

E2 ˘a

E7 ˇc

E1 â

E3 ä

E8 é

E9 ˛e

EA ë

EC í

ED î

EE d’

EF Æ F0 7 F1 ˇn F2 ó F3 ô F4 = F5 ö F6 ÷ F7 ˇr F8 ˚u F9 ú FA > FB ü FC ý FD ¸t FE ˙ FF

A few characters may need some explanation:

• Do not confuse the breve ‘˘’ and the háˇcek ‘ˇ’: the former is round, the latter pointed.

• Do not confuse the cedilla ‘¸’ (which opens to the left) and the ogonek ‘.’, especially because the cedilla was often written like an ogonek in Old French, where we find the letter ‘˛e’.

• Turkish uses the letter ‘s’ with a cedilla, but in Romanian the same letter, as well as letter ‘t’, are written with a diacritical mark shaped like a comma: ‘¨’, ‘≠’. The ISO 8859- 2 standard was not intended to cover Turkish, yet we can see in the description of the characters that these letters are anomalously written with a cedilla rather than a comma.

In 2001, after the release of ISO 8859-15, which added the euro sign to ISO 8859-1 and corrected a number of other deficiencies in that encoding, ISO did the same for ISO 8859- 2: ISO 8859-16 (or “Latin-10”), the latest encoding in the 8859 saga, covers the languages of Central Europe (Polish, Czech, Slovenian, Slovak, Hungarian, Albanian, Romanian), but also French (with the ‘œ’ ligature!), German, and Italian. The coverage of this encoding stopped at the French border and did not extend to Spanish (‘ñ’ is missing) or Portuguese (there are no vowels with a tilde). It has the distinction of being the first (better late than never!) to include the Romanian letters ‘¨’ and ‘≠’.

B1 ˇC

B9 ¨

B0 ±

B6 · B7 ž

B8 ˇc

B2 ł

B3 Ž

B4 ”

B5 ¶

BA »

BB Œ

BC œ

BD Ÿ

BE ˙z

BF À C0 Á C1 Â C2 ˘A C3 Ä C4 / C5 ÆC6 Ç C7 È C8 É C9 Ê CA Ë CB Ì CC Í CD Î CE Ï CF Ð

DD ∏

D0 1 D1 Ò

D4 ;

D6 0 D7 <

D2 Ó

D3 Ô

D5 Ö

D8 Ù

D9 Ú

DA Û

DB Ü

DC ˛E

DE ß

DF à E0 á E1 â E2 ˘a E3 ä E4 5 E5 æ E6 ç E7 è E8 é E9 ê EA ë EB ì EC í ED î EE ï EF Æ

FD ≠

F0 7 F1 ò

F4 =

F6 6 F7 >

F2 ó

F3 ô

F5 ö

F8 ù

F9 ú

FA û

FB ü

FC ˛e

FE ÿ

FF

The third (ISO 8859-3, or ‘Latin-3’) in the series is dedicated to the languages of “the South”: Turkish, Maltese, and Esperanto (the last of these not being particularly Southern). In it we find certain characters from ISO 8859-1 and ISO 8859-2 and also— surprise!—a few empty blocks:

::: tip Typographical Specimen: ISO 8859-3 (Latin-3) Table (Plate 1-6)
![Plate 1-6: ISO 8859-3 (Latin-3) Table](/images/fonts-encodings/plate1-6-iso8859-3-table.png)
*Plate 1-6: ISO 8859-3 (Latin-3) upper GR region for Esperanto, Maltese, and Turkish.*
:::



B0 Ø

B5 h

BB ˆj

B4 μ

B6 · B7 ¸

BA ˘g

B1 ²

B2 ³

B3 ´

B8 ı

B9 ¸s

BC ½

BD BE ˙z

BF À C0 Á C1 Â C2 C3 Ä C4 ˙C C5 ˆC C6 Ç C7 È C8 É C9 Ê CA Ë CB Ì CC Í CD Î CE Ï CF

D4 ˙G

D7 ˆG

DC ˘U

DD ˆS

D6 ×

D0 Ñ

D1 Ò

D2 Ó

D3 Ô

D5 Ö

D8 Ù

D9 Ú

DA Û

DB Ü

DE ß

DF à E0 á E1 â E2 E3 ä E4 ˙c E5 ˆc E6 ç E7 è E8 é E9 ê EA ë EB ì EC í ED î EE ï EF

F6 ÷

F4 ˙g

F7 ˆg

FC ˘u

FD ˆs

F0 ñ

F1 ò

F2 ó

F3 ô

F5 ö

F8 ù

F9 ú

FA û

FB ü

FE ˙

FF

In 1989 the Turks, dissatisfied with ISO 8859-3, asked for a slightly modified version of ISO 8859-1 with the Turkish characters in place of the Icelandic ones. The result was

ISO 8859-9 (or “Latin-5”), which differs from ISO 8859-1 in only six positions (shown in black below):

˘G D0 Ñ D1 Ò D2 Ó D3 Ô D4 Õ D5 Ö D6 × D7 Ø D8 Ù D9 Ú DA Û DB Ü DC ˙I DD ¸S DE ß DF ˘g F0 ñ F1 ò F2 ó F3 ô F4 õ F5 ö F6 ÷ F7 ø F8 ù F9 ú FA û FB ü FC ı FD ¸s FE ÿ FF

ISO 8859-4 (Latin-4), ISO 8859-10 (Latin-6), and ISO 8859-13 (Latin-7)

Encoding number 4 in the series (ISO 8859-4, or “Latin-4”) is dedicated to the languages of “the North”. Since Danish, Swedish, Norwegian, Finnish, and Icelandic are already covered by ISO 8859-1, “languages of the North” here refers to those of the Baltic countries: Lithuanian, Latvian, Estonian, and Lapp. Here is the encoding:

A4 ˜I

A1 ±

A3 ´

AA ≤

AB ¥

A9 !

A0 ˛ A

A2 R¸

A5 L¸

A6 §

A7 ¨

A8 Š

AD Ž

AE ¯

nbsp

AC shy

AF ° B0 ˛a B1 . B2 r¸ B3 ´ B4 ˜ı B5 l¸ B6 ˇ B7 ¸ B8 š B9 & BA ≥BB μ BC ∂BD ž BE n BF

C6 * C7 ˇC

CB ˙E

CE "

C0 Á

C1 Â

C2 Ã

C3 Ä

C4 Å

C5 Æ

C8 É

C9 ˛E

CA Ë

CC Í

CD Î

CF Ð D0 N¸ D1 # D2 K¸ D3 Ô D4 Õ D5 Ö D6 × D7 Ø D8 + D9 Ú DA Û DB Ü DC ˜U DD \$ DE ß DF %

E6 ,

EE '

EB ˙e

E7 ˇc

E0 á

E1 â

E2 ã

E3 ä

E4 å

E5 æ

E8 é

E9 ˛e

EA ë

EC í

ED î

EF Æ F0 n¸ F1 ( F2 k¸ F3 ô F4 õ F5 ö F6 ÷ F7 ø F8 - F9 ú FA û FB ü FC ˜u FD ) FE ˙ FF

In 1992, a new encoding (ISO 8859-10, or “Latin-6”), much more rational than the previous one, was created for the Nordic languages. It also includes all of the characters required to write Icelandic. One special feature: certain “customs” of the ISO 8859 encodings were abandoned; for example, the universal currency symbol, the free-standing accent marks, and the mathematical signs are not included.

::: tip Typographical Specimen: ISO 8859-10 (Latin-6) Table (Plate 1-7)
![Plate 1-7: ISO 8859-10 (Latin-6) Table](/images/fonts-encodings/plate1-7-iso8859-10-table.png)
*Plate 1-7: ISO 8859-10 (Latin-6) upper GR region for Nordic, Sami, and Inuit languages.*
:::



FE ±

F1 (

F8 -

F6 ˜u

F0 n¸

F2 ó

F3 ô

F4 õ

F5 ö

F7 ø

F9 ú

FA û

FB ü

FC ý

FD þ

FF

A few comments:

• Clearly this ISO 8859 encoding is much more mature than the previous ones. Not only have all the useless characters been done away with, but also there is a companion to the isolated ‘ß’: the Greenlandic letter ‘±’, whose upper-case version is identical to ‘K’.

• The glyph ‘Ð’ appears twice: in position 0xA9 it represents the Croatian dje, whose lower-case form is ‘Æ’; in position 0xD0, on the other hand, it represents the Icelandic eth, whose lower-case form is ‘ð’.

In 1998 a third encoding dedicated to the Baltic languages came out: ISO 8859-13 (or “Latin-7”), which has the peculiarity of combining these languages with Polish and including the appropriate types of quotation marks.

ISO 8859-5, or “ISO Cyrillic”, stems from a Soviet standard of 1987, GOST 19768/87, and is meant for the languages that use the Cyrillic alphabet. As there are many such languages, all of them rich in characters, the encoding is limited to Russian as spelled after the revolution (without the characters “fita …, yat , izhitsa ‡, i dessyatirichnoye i” that Lenin eliminated) and to the languages spoken in European countries: Ukrainian (without the character ‘‰ ’, which the Soviet government did not recognize), Byelorussian, Moldavian, Bulgarian, Serbian, and Macedonian. This encoding also includes the ‘№’ ligature, a number sign (like the North American English ‘#’), which appears in practically every Russian font. The ‘N’ in this character is a foreign letter; it does not appear in the Cyrillic alphabet.

ISO 8859-6, or “ISO Arabic”, covers the Arabic alphabet. We are astonished by the minimalist appearance of this encoding: there are numerous empty blocks, yet many languages that use the Arabic script have extra characters that are not provided. ISO 8859-6 includes only the basic letters required to write Arabic and also the short vowels and some of the diacritical marks (the wasla and the vertical fatha are missing). The punctuation marks that differ in appearance from their Latin counterparts (the comma, semicolon, question mark) are also included.

Describing the ISO 8859-7, or “ISO Greek”, encoding is a very painful experience for the author, for he still bears the scars of that massacre of the Greek language that is known as the “monotonic reform”. This reform of 1981 cut the Greek language offfrom its accents and breathing marks for the sake of facilitating the work of the daily press and the computerization of the language. Which other country in the world could bear to perpetrate so grave an injury on a 2,000-year-old language in order to accommodate it better to the limitations of the computer? (See [169, 166].) The survivors of the massacre are collected in this encoding: letters without accents and vowels with an acute accent. There are also the vowels iota and upsilon with a diæresis, as well as with both an accent and a diæresis, but their upper-case versions with the diæresis are absent.

The ISO 8859-8, or “ISO Hebrew”, encoding covers Modern Hebrew (or Ivrit). Once again, a minimalist approach was taken: the Hebrew consonants and long vowels are all there, but not the short vowels or any other diacritical marks. Yiddish is not provided for.

Finally, ISO 8859-11, or “ISO Thai”, which stems from Thai standard TIS 620 of 1986, covers Thai, a Southeast Asian script that is a simplified version of the Khmer script. The encoding is rather thorough: it contains practically all of the consonants, initial vowels, diacritical marks, and special punctuation marks, as well as the numerals.

ISO 8859-14 (or “Latin-8”) is dedicated to the Celtic languages: Irish Gaelic (which is ordinarily written in its own alphabet), Scottish, and Welsh. Only Breton, with its famous ‘c’h’ ligature, is absent. It is a variant of ISO 8859-1 with 31 modified characters that we have shown here in black:

The first telegraph systems in the Far East were imported from the West and therefore used the Latin alphabet. How could the thousands, even tens of thousands, of ideographic characters of the Chinese writing system have been encoded, with either Morse code or anything similar? Transliteration into the Latin alphabet was not an option either, as the phonetics of the Chinese language are very ill suited to that approach. Japanese is simpler phonetically, but another problem impeded transliteration: the enormous number of homophones that are distinguished only in writing.

Only computer science could enable the countries of the Far East to communicate conveniently over large distances. The country the best equipped for this task was, of course, Japan. In 1976, three years after the release of ISO 2022, the Japanese prepared the first GR-type encoding—that is, a 94-character supplement to ASCII: JIS C 6220 (which was rechristened as JIS X 0201-1976 in 1987). The ASCII used in Japan was already localized: a yen sign ‘¥’ replaced the backslash2 and the tilde was replaced by an overbar (for writing the Japanese long vowels in Latin script). JIS C 6220, based on the JISCII released in 1969, contains only katakana and a few ideographic punctuation marks (the period, the quotation marks, the comma, the raised dot), all in half-width characters:

A0 ｡

A1 ｢

A2 ｣

A3 ､

A4 ･

A5 ｦ

A6 ｧ

A7 ｨ

A8 ｩ

A9 ｪ

AA ｫ

AB ｬ

AC ｭ

AD ｮ

AE ｯ

nbsp

C0 ﾁ

C1 ﾂ

C2 ﾃ

C3 ﾄ

C4 ﾅ

C5 ﾆ

C6 ﾇ

C7 ﾈ

C8 ﾉ

C9 ﾊ

CA ﾋ

CB ﾌ

CC ﾍ

CD ﾎ

CE ﾏ

The phonetic modifiers were supplied as independent characters even though there was enough space to encode all of their combinations with letters. The syllable ‘ペ’ was thus obtained from the character ‘ヘ’ followed by a modifier character ‘°’.

2 As a result of which right up to this day, thirty years later, TEX commands in Japanese handbooks always start with a yen sign rather than a backslash.. . .

On January 1, 1978, after nine years of hard effort, the first true Japanese encoding, JIS C 6226-1978, known today as “old JIS”, officially came into effect. It contains 6,694 characters: the Latin, Greek, and Cyrillic alphabets, the kana, and 6,349 kanji ideographic characters, distributed over two levels. It was revised three times, finally to become JIS X 0208-1997 in January 1997. This last encoding is perhaps the most important Japanese encoding of all. Its structure complies with ISO 2022: there are 94 GR tables of 94 characters each.

In 1990 a second Japanese encoding was released: JIS X 0212-1990. It supplements the first with 5,801 ideographic characters and 266 other characters. A third encoding, JIS X 0213-2000, was released in January 2000. It adds another two levels of kanji to those of JIS X 0208-1997: the third level contains 1,249 kanji; the fourth, 2,436.

China did not lag far behind Japan: in 1981, on the symbolic date of May 1, it issued the first Chinese encoding, GB 2312-80. This encoding, which contains 7,445 characters, is compatible with the ISO 2022 standard. It is suspiciously similar to the Japanese encodings, at least in its choice of non-ideographic characters: it includes the Latin, Greek, and Cyrillic letters, and even the Japanese kana.

Over time there were numerous extensions to GB 2312-80. By 1992, the number of characters totaled 8,443. After Mao’s Cultural Revolution, the People’s Republic of China adopted a simplified writing system of ideographic characters, and the encodings respect it. But, contrary to what one might have expected, China also issued encodings in traditional characters. Thus in 1990 the GB/T 12345-90 encoding was released. The letter ‘T’ in its name comes from the character 推and means “optional”—after all, in a country that has simplified its writing system, the traditional form could only be regarded as optional.

An encoding was also released in Taiwan on a May 1, but this time in 1984 (three years after the People’s Republic of China released its own encoding). It is called, in English, “Big Five”, and its name refers to the five big Taiwanese corporations that collaborated on its development. It seems that Taiwan went all out to surpass its bigger cousin: Big Five contains no fewer than 13,494 characters, 13,053 of which are ideographic, arranged on two levels. Finally, 1992 saw the release of the CNS 11643-1992 encoding, which broke all the records for number of characters: a total of 48,711, including 48,027 ideographic characters, organized into seven planes with approximately 6 to 8 thousand characters each. The first two planes correspond roughly to the two levels of Big Five.

As for the other Chinese-speaking countries, Singapore uses mainly the GB encodings of mainland China, and Hong Kong, despite its recent annexation into China, uses mainly Big Five.

The encoding frenzy began in South Korea in 1992 with the KS X 1001-1992 encoding, which contains 4,888 ideographic characters, 2,350 hangul phonetic characters, and 986 other characters, once again including Latin, Greek, Cyrillic, and the Japanese kana, strictly in imitation of the Japanese encoding JIS X 0208-1997.

North Korea is said to have abolished the ideographic characters, yet the first North Korean encoding, KPS 9566-97 of 1997, contained 4,653 ideographic characters as well as 2,679 hangul characters and 927 other characters. This encoding was inspired by

the South Korean one but presents certain incompatibilities. In addition, positions 0x0448 to 0x044D fulfill an important state purpose: they contain the names of honorable party president Kim Il-sung and his son and successor Kim Jong-il ... a funny way to achieve immortality.

Using ISO 2022 to gain access to the characters in these encodings is not always very practical because at any given time one must be aware of the current mode, that is, which of G0, G1, G2, and G3 is the active encoding. In Japan there have been two attempts to overcome this problem and make use of the characters of the JIS encodings without employing escape sequences:

1. Shift-JIS is an initiative of Microsoft. The idea is very simple: the JIS encodings are made up of tables of 94×94 characters, and, if we count in ranges of 16 characters, that makes 6×6 = 36 ranges. But 36 can also be written as 3×12; thus we can obtain any character by using two bytes, of which the first covers three different ranges and the second covers twelve different ranges. We select the ranges 0x81-0x9F and 0xE0- 0xEF for the first byte and 0x40-0x7E and 0x80-0xFC for the second. Why have we chosen those particular ranges for the first byte? Because they leave section 0x20- 0x7F free for ASCII and section 0xA0-0xDF free for the katakana. Thus, upon reading a byte, the computer knows if it is a single-byte character or if a second byte will follow, and a simple calculation is sufficient to find the table and the position of the desired character.

Shift-JIS was widely used under Windows and MacOS. Its flagrant drawback is that the technique of 3 × 12 severely limits the number of characters accessible through this method. Thus there is no hope at all of adding any extra characters. And we cannot automatically change encodings because we do not have access to the ISO 2022 escape sequences.

2. EUC (Extended Unix Coding) is a variant of ISO 2022 without escape sequences. There is not just one EUC but an assortment of localized versions: EUC-JP, EUC-CN, etc. In each of them, one chooses from one to four encodings. The first two are obtained from suitable choices of ranges of characters. The third and fourth encodings are ultimately formed through the use of two control characters: ss2 (0x8E) and ss3 (0x8F), followed by one or two other characters.

Thus, for example, EUC-JP includes ASCII, JIS X 0208-1997, the katakana, and JIS X 0212-1990. Among these four, ASCII is obtained directly, JIS X 0208-1997 is obtained from the characters 0xA1-0xFE×0xA1-0xFE, the katakana are obtained with ss2 followed by 0xA1-0xDF, and JIS X 0212-1990 is obtained with ss3 followed by 0xA1-0xFE×0xA1-0xFE.

While Shift-JIS is peculiar to Japan, EUC has also been used in other countries: there are the encodings EUC-CN (mainland China), EUC-TW (Taiwan), EUC-KR (South Korea).

The interested reader will find a very detailed description of these encodings and a host of other information in Ken Lunde’s book CJKV Information Processing [240].

Microsoft’s code pages 45

Microsoft’s code pages

The term codepage for “encoding” was oined by Microsoft. As the DOS system, for example, was console-based, we find in the DOS code pages a set of graphical symbols used to draw user interfaces through the simple arrangement of straight segments, corners, crosses, etc. There are even lattices of pixels that simulate various shades of gray.

In the US, the most commonly used DOS code pages were 437 (“United States”) and 850 (“Multilingual”). In both cases, 128-position extensions to ASCII were made (the entire upper half of the table). Here is the part of the table beyond ASCII for code page 437, entitled “MS-DOS Latin US”:

::: tip Typographical Specimen: MS-DOS Code Page 437 Graphic & Box Characters (Plate 1-8)
![Plate 1-8: MS-DOS Code Page 437 Table](/images/fonts-encodings/plate1-8-cp437-table.png)
*Plate 1-8: MS-DOS Code Page 437 upper 128 characters featuring line-drawing and block elements.*
:::



√

n

FC ² FD a FE nbspFF

FB

This code page is a real mixed bag: a few accented letters (there is an ‘É’ but no ‘È’... ), a handful of currency symbols, some punctuation marks, three rows of building blocks for drawing user interfaces, and a number of mathematical symbols, including a small range of Greek letters. One startling fact: the author does not know whether the character in position xE1 is a Greek beta ‘β’ or a German eszett ‘ß’. Its location between alpha and gamma suggests that it is a beta, but at the same time the presence of the German letters ‘ä’, ‘ö’, and ‘ü’ implies that this encoding should logically include an ‘ß’. Could it be that the same character was supposed to serve for both? If so, depending on the font, we would have had aberrations such as “ßιßλον” or “Gieβgefäβ”...

Code page 850 (MS-DOS Latin 1) is a variant of the preceding. It contains fewer graphical characters and more characters for the languages of Western Europe. Note that the German eszett ‘ß’ appears in the same position as the ‘β / ß’ of code page 437:

::: tip Typographical Specimen: MS-DOS Code Page 850 Multilingual (Plate 1-9)
![Plate 1-9: MS-DOS Code Page 850 Table](/images/fonts-encodings/plate1-9-cp850-table.png)
*Plate 1-9: MS-DOS Code Page 850 replacing box characters with Western European accented letters.*
:::



D8 6 D9 3 DA [[

DB ZZ

DE YY

D0 Ð

D1 Ê

D2 Ë

D3 È

D4 ı

D5 Í

D6 Î

D7 Ï

DC ¦

DD Ì

F0 ±

F5 ÷

F9 · FA ¹

FD a

F1 < F2 ¾

F3 ¶

F4 §

F6 ¸

F7 °

F8 ¨

FB ³

FC ²

shy

FE nbsp

FF

There were numerous other MS-DOS code pages [204]: 708–710, 720, and 864 (Arabic); 737 and 869 (“monotonic” Greek); 775 (Baltic countries); 852 (countries of Central Europe); 855 and 866 (Cyrillic, with 866 being for Russian only); 857 (Turkish); 860 (Portuguese); 861 (Icelandic); 862 (Hebrew, without the short vowels); 863 (“Canadian French”, a pastiche of 437 and 850); 865 (Nordic countries); 874 (Thai); 932 (Japanese); 936 (simplified Chinese); 949 (Korean); 950 (traditional Chinese).

When Windows came out, there was no longer any need for “graphical characters”, and a change of encodings was called for (even though it caused big problems for users who were porting their documents from MS-DOS to Windows). In the meantime, the first ISO 8859 encodings were released, and Microsoft decided to adopt them—but avoided their major shortcoming: the characters 0x80-0x9F were not control characters in Microsoft’s implementation.

Thus code page 1252 Windows Latin 1, also known as “ANSI”, is an ISO 8859-1 encoding to which the following two lines have been added:

::: tip Typographical Specimen: Windows Code Page 1252 (ANSI 0x80–0x9F) (Plate 1-10)
![Plate 1-10: Windows Code Page 1252 (ANSI) Table](/images/fonts-encodings/plate1-10-cp1252-table.png)
*Plate 1-10: Windows Code Page 1252 populating the C1 control zone (0x80–0x9F) with typographic characters.*
:::



84 ...

¤

80 81 ,

82 f

83 „

85 †

86 ‡

87 ˆ

88 ‰ 89 Š

8A ‹

8B Œ 8C 8D Ž

90 ‘ 91 ’ 92 “ 93 ” 94 • 95 – 96 —97 ˜ 98 ™99 š 9A › 9B œ 9C 9D ž 9E Ÿ 9F

We can only rejoice at the fact that the letters ‘Œ’, ‘œ’, and ‘Ÿ’ are found in this encoding. There are also the single guillemets ‘‹ ›’ and the two most common Central European letters, ‘Š š’ and ‘Ž ž’. A few details: ‘,’ and ‘„’ are the German single and double opening quotation marks, also called Gänsefüßchen (= ‘[little] goose feet’).

Code page 1250 Windows Latin 2 both extends and modifies ISO 8859-2. Positions 0x80- 0xBF are the ones that have undergone modification:

90 ‘ 91 ’ 92 “ 93 ” 94 • 95 – 96 —97 98 ™99 š 9A › 9B 6 9C t’ 9D ž 9E 9 9F

There has never been a Windows Latin 3 or a Windows Latin 4, but there is a 1254 Windows Latin 5 for Turkish, which differs from 1252 Windows Latin 1 in only six positions:

˘G D0 Ñ D1 Ò D2 Ó D3 Ô D4 Õ D5 Ö D6 × D7 Ø D8 Ù D9 Ú DA Û DB Ü DC ˙I DD ¸S DE ß DF ˘g F0 ñ F1 ò F2 ó F3 ô F4 õ F5 ö F6 ÷ F7 ø F8 ù F9 ú FA û FB ü FC ı FD ¸s FE ÿ FF

Apple’s encodings 47

These are the same differences that we find between ISO 8859-1 and ISO 8859-9.

Other Windows code pages are 1251 Windows Cyrillic, 1253 Windows Greek (“monotonic Greek” is implied3), 1255 Windows Hebrew, 1256 Windows Arabic, and 1257 Windows Baltic.

Apple’s encodings

From the beginning, the Macintosh used its own encoding, an extension of ASCII that was still incomplete on the first Macintosh (released in 1984) but was gradually fleshed out. The unusual aspect of the Macintosh encodings is that they, like the MSDOS code pages, include mathematical symbols. Since most fonts do not contain these symbols, MacOS had a special substitution procedure. Whichever font one used, the mathematical symbols almost always came from the same system fonts. Other special features of the Macintosh encodings: they include the ‘fi’ and ‘fl’ ligatures as well as the famous bitten apple ‘z’ that Apple uses as its logo.

::: tip Typographical Specimen: Classic Mac OS MacRoman Table (Plate 1-11)
![Plate 1-11: Classic Mac OS MacRoman Table](/images/fonts-encodings/plate1-11-macroman-table.png)
*Plate 1-11: Classic Mac OS MacRoman 8-bit table featuring mathematical and typographic glyphs.*
:::



Here is the encoding used on the Macintoshes sold in the US and in Western Europe, which is called Standard Roman [53] (a rather poorly chosen name, since the term “roman” refers to a font style rather than to a writing system):

B0 ±

B1 ≤

B2 ≥

B4 μ

B5 ∂

B6 ∑B7 ∏B8 π

BC Ω

B3 ¥

BA ª

BB º

BD æ

BE ø



BF ¿ C0 ¡ C1 ¬ C2

B9

√

C3 f C4 ≈C5 Δ C6 « C7 » C8 ... C9 nbspCA À CB Ã CC Õ CD ŒCE œ CF –

DA ´

D5 ÷

D6 ♦ D7 ÿ

D0 —

D1 “

D2 ”

D3 ‘

D4 ’

D8 Ÿ

D9 /

DB ‹

DC ›

DD fi

DE fl

DF ‡ E0 · E1 , E2 „ E3 ‰E4 Â E5 Ê E6 Á E7 Ë E8 È E9 Í EA Î EB Ï EC Ì ED Ó EE Ô EF z

FD .

F0 Ò

F1 Ú

F2 Û

F3 Ù

F4 ı

F5 ˆ

F6 ˜

F7 ¯

F8 ˘

F9 ˙

FA ˚

FB ¸

FC ˝

FE ˇ

FF

A few details: we have already seen the German quotation marks ‘,’ and ‘„’ in the 1252 Windows Latin 1 encoding. The character 0xDA ‘/ ’ is a fraction bar. Do not mistake the characters ‘∑’ and ‘∏’ for the Greek letters ‘Σ’ and ‘Π’: the former, the mathematical symbols for sum and product, are larger than the ordinary Greek letters, which are of regular size. In addition, both may appear in one formula: ∑∞

i=0 Σi = ∏∞

j=0 Π j. The two glyphs look very much alike, but in position xA1 we have the degree sign (a perfect circle) while in position xBC there is a superscript letter ‘o’, used in Spanish, French, and other languages. The letter ‘ı’ in position F5 is not intended for Turkish but to be combined with accents.

3 This encoding long irritated the Greeks because it differs only slightly from ISO 8859-7: the accented capital letter alpha occurs in position 0xA2 on the Windows code page and in position 0xB6 in the ISO encoding; thus the letter tends to disappear when a document is transferred from Windows to Unix or the opposite.. . .

There is an Icelandic version of this encoding that differs from Standard Roman in six positions: ‘Ý’ (0xA0), ‘Ð’ (0xDC), ‘ð’ (0xDD), ‘Þ’ (0xDE), ‘þ’ (0xDF), ‘ý’ (0xE0).

There is a Turkish version as well, that differs from Standard Roman in six consecutive positions: ‘˘G’ (0xDA), ‘˘g’ (0xDB), ‘˙I’ (0xDC), ‘ı’ (0xDD), ‘¸S’ (0xDE), ‘¸s’ (0xDF). Position 0xF5 of this encoding has been left empty so that the letter ‘ı’ would not appear twice.

In addition, there is a Romanian version of the encoding, Romanian, that again differs from Standard Roman in six positions: ‘˘A’ (0xAE), ‘∑’ (0xAF), ‘˘a (0xBE), ‘¨’ (0xBF), ‘∏’ (0xDE), ‘≠’ (0xDF).

For the languages of Central Europe and the Baltic countries, Apple offers the Central European encoding, shown below:

95 ˙E

9C ˇE

93 !

94 &

97 ˙e

9D ˇe

91 í

92 d’

96 ó

98 ô

99 ö

9A õ

9B ú

9E ü

9F † A0 ° A1 ˛E A2 £ A3 § A4 • A5 ¶ A6 ß A7 ® A8 © A9 ™AA ˛e AB ¨ AC̸ = AD ≥AE * AF ,

B0 "

B1 ≤

B2 ≥

B3 '

B5 ∂

B6 Σ

BC 4 BD :

B4 K¸

B7 ł

B8 L¸

B9 l¸

BA L’

BB l’

BE N¸

BF n¸ C0 1 C1 ¬ C2

√

C3 7 C4 ˇN C5 Δ C6 « C7 » C8 ... C9 nbspCA ˇn CB ˝O CC Õ CD = CE # CF –

D5 ÷

D6 ♦ D7 (

DD ˇr

D0 —

D1 “

D2 ”

D3 ‘

D4 ’

DB ‹

DC ›

DE R¸

DF r¸ E0 Š E1 , E2 „ E3 š E4 0 E5 6 E6 Á E7 ˇT E8 t’ E9 Í EA Ž EB ž EC \$ ED Ó EE Ô EF )

F0 ˚U

FA ˙Z

FD ≤

F3 <

F4 >

F5 +

F6 -

F2 ˚u

F1 Ú

F7 Ý

F8 ý

F9 k¸

FB Ł

FC ˙z

FE ˇ

FF

Notice that, for an unknown reason, the ‘Σ’ has resumed its customary size and that there is no ‘Π’. This encoding covers Polish, Czech, Slovak, Slovenian, Hungarian, Lithuanian, Latvian, and Estonian. It does not cover Croatian because it lacks the letter ‘Ð Æ’. For this reason, Apple issued a special encoding (Croatian) for the Croatian language.

Other Apple encodings: Arabic (Arabic, Persian, Urdu, still without wasla but with vertical fatha), Chinese Traditional, Cyrillic (for the European languages that use the Cyrillic alphabet, with the exception of Ukrainian, for which the letter ‘‰’ is missing), Greek (“monotonic” Greek), Hebrew (Hebrew with vowels, semivowels, and schwa), Japanese, Korean, Devanagari, Gujarati, Gurmukhi, and Thai.

The protocol for electronic mail that is still in use today was published in 1982: it is RFC 822 (in which RFC stands for “Request for Comments”, a way to demonstrate the democratic nature of the Web’s standards). This RFC stipulates that electronic messages are to be encoded in ASCII.

To mitigate that drawback, a new RFC published in 1996 (RFC 2045) introduced a technique that has since become an integral part of electronic mail: the MIME protocol (= “Multipurpose Internet Mail Extensions”). MIME allows for the attachment of files to e-mail messages and for dividing a message into multiple segments, each one potentially

of a different type, or, if it is of type text, potentially in a different encoding. To specify the encoding of a message or a part of a message, we use two operators:

• charset is the encoding of the content. Its value must appear on a list [186] established and regularly updated by IANA (= “Internet Assigned Numbers Authority”). In February 2004 there were 250 registered encodings, such as US-ASCII, ISO-2022- JP, EBCDIC-INT, ISO-8859-1, IBM437 (code page 437), windows-1252 (Windows code page 1252), etc.

The encoding affects only those segments of MIME type text (the subtype being plain, which indicates that the text is not enriched). The syntax is as follows:

• Content-Transfer-Encoding specifies how to translate the coming binary (beyond 0x7f) bytes into ASCII data. This is necessary because MIME did not change the nature of electronic mail—which remains based on ASCII just as much as it was twenty years ago. In fact, MIME offers only makeshift methods for converting binary bytes to ASCII and vice versa. Two methods are available: “quoted-printable” text and text in “base 64”.

Quoted-printable involves using the equals sign as an escape character. Three possibilities exist:

1. The character to convert is a “printable” ASCII character—that is, in the range of 0x20 to 0x7e—other than the equals sign (ASCII 0x3d). In this case it passes through unchanged.

2. The character is a control character (0x00-0x1f), a binary character (0x80-0xff), or an equals sign. In this case we write the equals sign followed by the position of the character in the table, in the form of a two-digit hexadecimal number. Thus, if we have specified that we are using ISO 8859-1, the word “voilà” is written voil=E0.

3. Since the length of the lines in the message is limited, we will divide any excessively long line by adding an equals sign followed by a newline. A line break of this kind will ordinarily be disregarded by the application that decodes the “quoted-printable” text.

A message encoded in “quoted-printable” format must include the following line in its header:

Content-Transfer-Encoding: quoted-printable

The other method, “base 64”, involves taking three consecutive bytes of text and regarding them as four groups of six bits (3 × 8 = 4 × 6). Each group of six bits is represented by one ASCII character, as follows:

– the letters A to Z represent the numbers between 0 and 25;

– the letters a to z represent the numbers between 26 and 51;

– the digits 0 to 9 represent the numbers between 52 and 61; – + and / represent respectively the numbers 62 and 63.

The remaining possibility is that one or two bytes will be left over after translation of all of the three-byte sequences. Suppose that one byte, notated xxxxxxxx, is left over. Then we will use the two six-bit groups xxxxxx and xx0000, and we will append two equals signs to the converted string. If two bytes, xxxxxxxx and yyyyyyyy, are left over, we will use the three six-bit groups xxxxxx, xxyyyy, and yyyy00, and we will append a single equals sign to the converted string.

Example: to encode the word “voilà” (01110110 01101111 01101001 01101100 11100000), we start by taking the first four letters and dividing them into groups of six bits (011101 100110 111101 101001 011011 000000), namely the numbers 29, 38, 61, 41, 27, and 0, which give us the alphanumerics dm9pbA. The remaining letter ‘à’ (11100000) gives us two groups of six bits (111000 000000), namely the numbers 56 and 0, and therefore the codes 4A. We will append an equal signs to indicate that one letter is missing to complete the triplet. Thus the result is dm9pbA4A=.

A message encoded in “base 64” must include the following line in its header:

Content-Transfer-Encoding: base64

What are the advantages and disadvantages of the conversions to “quoted-printable” or “base 64”? When the encoding and decoding are performed transparently by the e-mail software, the difference is of little importance, apart from the fact that a message in ASCII with few binary characters will take up less space in “quoted-printable” than in “base 64”, while for a message entirely in binary characters the opposite is true. Nevertheless, if the message could be read with software that is not compatible with MIME, “quotedprintable” text will be legible in languages such as French or German that do not use accented or special lettetrs with great frequency, whereas text in “base 64” will have to be processed by computer.

While RFC 2045 specified the encoding of text segments, no provision was made for the subject line of the message or the other lines in the header that would contain text. The solution was provided by RFC 2047, which defined a way to change encodings at any time, either within a string in the header or within the body of the message. It is nothing revolutionary: we once again use the equals sign (which plays a special rôle in both forms of conversion to ASCII) as an escape character:

=?name?*?converted_string?=

where name is the IANA name of the encoding, * is either Q (= quoted-printable) or B (= base 64), and converted_string is the converted string. Thus the word “voilà” encoded in ISO 8859-1 can be written in the following two ways:

=?iso--?Q?voil=E0?= =?iso--?B?dm9pbA4A=?=

Alas, neither of them is really legible...

The Web is the exchange of HTML data under the protocol HTTP (“Hypertext Transfer Protocol”). Version 1.1 of this protocol is described in RFC 2616 of 1999. Browsers and servers communicate through this protocol by sending each other messages that may or may not contain HTML data. Thus, when one types a URL followed by a carriage return in the appropriate area in the browser, the browser sends an HTTP request to the server in question. The server replies by sending the HTML data corresponding to the URL, or with an error message. In all three cases (request, transmission of HTML data, error message), the parties to the communication send each other messages through HTTP.

HTTP is based on three concepts: the encoding (called charset), which by default is ISO 8859-1 (and not ASCII); the type of compression to be applied (called contentcoding, whose values may be gzip, compress, zlib, or identity); and the “transfer coding” to be used. The transfer coding corresponds to the “quoted-printable” and “base 64” of MIME, except that here data transfer is binary and thus does not require conversion to ASCII. The “transfer coding” that we use is chunk, which means that the data will be divided into blocks of a fixed length.

Here is an example of an HTTP header for a message in ISO 8859-1 with gzip compression:

Content-Type: text/html; charset=iso--

Content-Encoding: gzip Transfer-coding: chunked

where the first line specifies that the MIME type of the following document is text, with html as its subtype.

HTTP headers can also be included in the value of the content attribute of the meta element of HTML and XHTML. Each occurrence of this element contains a line of the HTTP header.

The first two parameters (encoding and compression) can also be used in the HTTP request sent to the server, to express the browser’s possibilities. In this way the browser can request a certain encoding that it knows how to use or even multiple encodings arranged in order of preference, one or more types of compression, etc. By writing

Accept-Charset: iso--, iso--;q=0.8

the client specifies that it can read, in order of preference, text in ISO 8859-15 and ISO 8859-1. The parameter q=0.8 (‘q’ as in “quality” and a number between 0 and 1) that follows the second encoding applies to it alone and indicates that the use of this encoding will give a result with 80% quality. Using this list of requested encodings and their weights with respect to quality, the server will decide which encoding to use to send data. If none of the requested encodings is available, the server will reply with an error message: “406: not acceptable”.

The same is true for compression:

Accept-Encoding: gzip;q=1.0, identity;q=0.5, *;q=0

where the asterisk is the “wildcard”. The line shown above should be interpreted as follows: the document may be compressed with gzip (top quality) or not compressed at all (50% quality), and every other type of compression is of “0% quality”, which means unacceptable.

One details that may lend itself to confusion: here “charset” is used to designate the character encoding and “coding”, or even “encoding” in the “accept” commands, is used for compression.