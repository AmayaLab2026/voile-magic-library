---
title: "Chapter 2: Characters, glyphs, bytes: An introduction to Unicode"
description: "Unabridged English text from Yannis Haralambous, Fonts & Encodings: Philosophical issues, first principles of Unicode, character encoding forms (UTF-8, UTF-16, UTF-32, CESU-8, SCSU), BMP and higher planes roadmap with authentic script specimen plates."
---

# Chapter 2: Characters, glyphs, bytes: An introduction to Unicode
**By Yannis Haralambous, Ph.D. (Translated and Expanded by P. Scott Horne, Ph.D.)**  
*From Fonts & Encodings (O'Reilly Media, 2007), pp. 53–94*

---

In the previous chapter, we saw the long journey that encodings took on their way to covering as many languages and writing systems as possible. In Orwell’s year, 1984, an ISO committee was formed with the goal of developing a universal multi-byte encoding. In its first (experimental) version, this encoding, known as ISO 10646 (to show that it was an extension of ISO 646, i.e., ASCII), sought to remain compatible with the ISO 2022 standard and offered room for approximately 644 million characters (!), divided into 94 groups (G0) of 190 planes (G0 + G1) of 190 rows (G0 + G1) of 190 cells (G0 + G1). The ideographic characters were distributed over four planes: traditional Chinese, simplified Chinese, Japanese, and Korean. When this encoding came up for a vote, it was not adopted.

At the same time, engineers from Apple and Xerox were working on the development of Unicode, starting with an encoding called XCCS that Xerox had developed. The Unicode Consortium was established, and discussions between the ISO 10646 committee and Unicode began. Unicode’s fundamental idea was to break free of the methods of ISO 2022, with its mixture of one- and two-byte encodings, by systematically using two bytes throughout. To that end, it was necessary to save space by unifying the ideographic characters.

Instead of becoming fierce competitors, Unicode and ISO 10646 influenced each other, to the point that ISO 10646 systematically aligned itself with Unicode after 1993.

Unicode was released in 1993 and has not stopped growing and evolving since. Its latest version, as of the writing of the book, bears the number 5 and was released in 2006. Most operating systems (Windows XP, MacOS X, Linux) are currently based on Unicode, although not all software is yet compatible with it. The Web is also moving more and

54 Chapter 2 : Characters, glyphs, bytes: An introduction to Unicode

more towards adopting Unicode, especially in regard to East Asian languages and writing systems.

But there is a price to pay for being open to the writing systems, and therefore also the cultures, of other peoples: computers and their operating systems must be more powerful, software must be more advanced, fonts must be much larger (and necessarily more cumbersome). And we have not even spoken of the different rendering techniques needed to display East Asian languages correctly—techniques employed in part by the operating system and in part by OpenType or AAT fonts.

In this chapter, which aims to be an introduction to Unicode, we shall discuss its overall structure and a number of technical and philosophical questions: what is the difference between characters and glyphs? how do we move from abstract characters to the very concrete bytes used in the computer?

In the following chapters, we shall examine the individuals that populate Unicode: characters and their properties. We shall discuss a few special situations that call for advanced techniques (normalization, bidirectionality, East Asian characters). Finally, we shall see how Unicode is used in operating systems and, more specifically, how we can enter Unicode characters into a document, whether by using special software or by designing virtual keyboards ad hoc.

What we shall not do in this book—so as not to double its already considerable size— is describe one by one the different writing systems covered by Unicode. Our approach will be to describe only those cases that present problems and that are worth discussing in detail. We shall refer the reader to other works that discuss the world’s writing systems very thoroughly, from either the linguistic ([106, 309, 345, 136, 96]) or the typographic () point of view.

Unicode is an encoding of characters, and it is the first encoding that really takes the trouble of defining what a character is.

Let’s be frank: computer specialists are not in the habit of worrying about philosophical issues (“who am I?”, “what comes after death?”, “what is a character?”). But that issue arose quite naturally in Unicode when the Asian languages were touched upon. Unicode purports to be an encoding based on principles, and one of these principles is precisely the fact that it contains characters exclusively. This fact forces us to give serious consideration to the question of what constitutes a character and what does not.

We can compare the relationship between characters and glyphs to the relationship between signifier and signified in linguistics. After all, Ferdinand de Saussure, the founder of linguistics, said himself: “Whether I write in black or white, in incised characters or in relief, with a pen or a chisel—none of that is of any importance for the meaning” . What he called “meaning” corresponds very well to what we intend to call “character”, namely, the meaning that the author of the document wished to impart by means of the glyph that he used.

But things are a bit more complicated than that: there are characters with no glyphs, glyphs that can correspond to a number of different characters according to context, glyphs that correspond to multiple characters at the same time (with weightings assigned to each), and even more possibilities.

The problem of glyphs and characters is so complex that it has gone beyond the realm of computer specialists and has come to be of interest even to philosophers. For example, the Japanese philosopher Shigeki Moro, who has worked with ideographic characters in Buddhist documents, goes so far in his article Surface or Essence: Beyond Character Model Set [274] as to say that Unicode’s approach is Aristotelian essentialist and to recommend supplanting it by an approach inspired by Jacques Derrida’s theory of writing . The reader interested in the philosophical aspects of the issue is invited to consult , in addition to the works cited above.

Let’s be pragmatic! In this book we shall adopt a practical definition of the character, starting with the definition of the glyph as a point of departure:

• A glyph is the image of a symbol used in a writing system (in an alphabet, a syllabary, a set of ideographs, etc.) or in a notational system (like music, mathematics, cartography, etc.).

• A character is the simple description, primarily linguistic or logical, of an equivalence class of glyphs.

Let us take a concrete illustration by way of example: the letter ‘W’. It is clear that there are thousands of ways to write this letter—to convince oneself of that fact, one need only thumb through Chapter 11, on the history of typographic characters. We could describe it as “the capital Latin letter double-you”. All the various ways to write the letter (‘W’, ‘W’, ‘W’, ‘W’, ‘W’,... ) have in common the fact that they match this description. The description is simple because it does not contain any unnecessary or irrelevant terms. It is linguistic because it falls within the realm of English grammar. We can therefore say, if the fact of corresponding to a description of this type is an equivalence relation, that the equivalence class in question is the character “capital Latin letter double-you”.

Let us take another example: the symbol ‘×’. We could give it the description “the mathematical multiplication sign”. This description is simple—we could even omit the word “mathematical”, as Unicode has indeed done. But it is not linguistic at all. It is a logical description because it falls within the realm of a well-defined, universally accepted system of notation, that used by mathematics. Thus the glyphs that could be described in this manner form an equivalence class that is the character in question.

But are the names of characters always as clear and precise as these?

Unfortunately not. For example, we have a character that is described as the “double high-reversed-9 quotation mark”. The “high-reversed-9” part of the description is neither linguistic nor logical but rather crudely graphical, even awkward. To describe this character, whose glyph is ‘ ’, it would have been easier to call it the “second-level Greek opening quotation mark”, because that is its most common use.

56 Chapter 2 : Characters, glyphs, bytes: An introduction to Unicode

Fortunately the Unicode book and the PDF files that can be found at the Consortium’s Web site (http://www.unicode.org/charts/) always supply with the description of each character a glyph that is called the representative glyph. It is not prescriptive, but its presence is extremely useful because it enables non-speakers of a language to identify the symbols described by their names. In the absence of representative glyphs, one would have to speak Tibetan in order to know that dzud rtags bzhi mig can is a cross made of four dots, and one would have to be a specialist in runes to know that the letter ingwaz is shaped like a diamond.

The representative glyph is not always sufficient when one is not familiar with a given writing system. Indeed, the glyphs that correspond to a given character may sometimes assume forms far removed from one another. That variation may be due to stylistic effects or historical reasons (the difference between ‘W’ and ‘W’ is considerable), or even to reasons of grammar. The latter is true in the case of Arabic, whose grammar provides that the letters assume different forms according to context and, more specifically, according to their position in the word. Thus the representative glyph for the character arabic letter kaf is ‘’, but within a word the same letter is rendered by a glyph similar to ‘’, a shape that is not a priori trivial for the reader unfamiliar with the Arabic script to recognize.

The representative glyph is the only way to find an ideographic character, as those characters have no description. We might have imagined, for example, that the character 門 could be described as “character meaning ‘gate’ ”; but since it also means “entrance”, “section”, “field”, “disciple”, “school”, and “clan”—and all that in Japanese alone—, we can see that an attempt to represent the encoding’s 70,027 ideographic characters in that manner would be a task as monumental as it would be futile. We shall see in Chapter 4 the specific problems that ideographs present.

Other characters do not have a glyph at all. That should come as no surprise to the reader, since even before ASCII there were encodings with control characters that had very precise semantics but did not need to be visually represented. Unicode goes even further: it is no longer restricted to sending messages to the central processing unit (such as “bell”) or to peripheral devices (such as “carriage return”) but extends even to the rendering of characters. Thus we have combining characters that affect the rendering of the preceding character(s). Often this modification involves adding an accent or a diacritical mark. In some cases, it involves graphically combining the preceding characters. There are many other applications of this possibility.

A string of Unicode characters can thus sometimes be more than a mere concatenation of symbols. It may be a sort of miniature program that tells the rendering engine how to proceed.

Another factor that distinguishes Unicode from other encodings is that its characters are more than mere descriptions and positions in a table. They have a certain number of properties thanks to which Unicode-compatible software is better equipped to render strings of characters visually or to process them. Let us take an example: in a document written in French and Khmer, the year 2006 may appear as “2006” or “æºº¬”. To keep us from having to search for two different strings, an intelligent text editor would only

Figure 2-1: When scripts are mixed.... [Photo taken in Athens by the author.]

::: tip Visual Linguistic Plate: Mixed Scripts (Figure 2-1)
![Figure 2-1: Mixed scripts on an Athens street sign](/images/fonts-encodings/fig2-1-mixed-scripts-athens.png)
*Figure 2-1: When scripts are mixed: A street sign photographed in Athens by the author showing Greek and Latin scripts with contrasting baseline metrics.*
:::



have to look up the properties of the characters ‘æ’, ‘º’, and ‘¬’ to learn that they are digits whose numeric values are precisely 2, 0, and 6—and voilà!

Of course, that does not work for numeration systems such as those of the Romans (in which 2006 is written “MMVI”), the Greeks (“κ”), and the Chinese (“二〇〇六”), but it hardly matters: using Unicode properties, software can process Unicode data in an intelligent way without having to reinvent the wheel. Chapter 3 is dedicated to Unicode character properties.

Another characteristic of the relationships between characters and glyphs: for reasons that are usually historical, the same glyph can represent multiple characters. Only context enables one to identify the character visually. Thus when we write ‘H’ in an Englishlanguage context such as this book, it is clear that we are using the eighth letter of the Latin alphabet. But the same glyph in the word “ΓΙΑΝΝΗΣ” (which is the author’s first name) or in the word “Ηρεμα” (Aremia = ‘tranquillity’) represents the Greek letter eta. Yet mixtures of writing systems are not always impossible, as shown by the photo taken in Athens that appears in Fig. 2-1. In it we see the word “PARKING” that starts off in Greek letters and ends with Latin ones, passing through the letters ‘K’, ‘I’, and ‘N’, which are common, both graphically and phonetically, to the two scripts. Finally, the same glyph in a word such as “РЕСТОРАН” (= ‘restaurant’) or “Наташа” (= ‘Natasha’) is ordinarily recognized right away as the Cyrillic letter ‘N’ (except by the various Western tourists who believe that restaurants in Russian are called pektopah... ). In the case of the glyph ‘H’, the lower-case versions enable us to identify the character unambiguously: ‘h’, ‘η’, ‘н’. There are also Unicode characters that have the same glyph yet belong to the same writing system: ‘Ð’ can be the Icelandic letter eth (lower-case ‘ð’) or the Croatian letter djé (lower-case ‘Æ’). The glyph ‘!’ may represent either greek small letter alpha with tonos or greek small letter alpha with acute: in the first instance, the acute accent is regarded as the single accent of the “monotonic” system; in the second instance, it is an ordinary acute accent. Even worse, there are Unicode characters belonging to the

58 Chapter 2 : Characters, glyphs, bytes: An introduction to Unicode

same writing system that have the same glyphs and the same semantics: the ideographic characters in the “CJK compatibility” block. These are characters that the Koreans encoded twice because those characters have two distinct pronunciations in their language. If the Japanese had done the same, we would have twenty or even thirty identical copies of certain ideographic characters...

Which brings us to a fact that justifies to a large degree the inconsistency of certain parts of Unicode: among the principles of Unicode, there is one that often comes into conflict with the others, the principle of convertibility. This principle stipulates that all data encoded in an official or industrial encoding that is in sufficiently wide use must be convertible to Unicode without loss of information. In other words, and with a little less tact: every wacky, exotic, vaguely defined, arcane, and often completely useless character that exists today in any of the designated encodings is elevated to the rank of Unicode character. Let’s just consider a few examples that arose in Chapter 1: the “universal currency sign”? It is in Unicode. The graphical symbols in the DOS code pages that were used to draw user interfaces? They are in Unicode. The self-standing accent marks that we used to add to letters by backspacing? They are present as well. The Koreans encode certain ideographs twice? Unicode follows their lead.

What is to be gained by having certain characters appear in the encoding twice? Nothing. Only the principle of convertibility has forced us to spurn all the other noble principles and accept as characters certain symbols that are not. When a Korean document containing two characters with the same glyph but with different pronunciations is converted to Unicode, those two characters are mapped to different code points in Unicode, which makes it possible to convert back to the original Korean encoding.

When we launch a project of Unicode’s size, it is essential to define a certain number of first principles on which we can subsequently fall back when decisions, often delicate ones, must be made. Even if leaning on our principles too much causes them to bend, in the words of Italian author Leo Longanesi. Unicode is based on ten principles—a highly symbolic number—which we shall describe in this section. The Unicode book, however, warns us that the ten principles cannot be satisfied simultaneously: there will always be trade-offs and compromises to be made. Our task is to figure out which compromises those are.

Here, then, are the ten principles.

Principle #1: universality

Unicode concerns itself with all living writing systems and with most historic ones. That aim, expressed in those terms, sounds inordinately ambitious; but if we weight writing systems by the number of documents actually available in electronic format, then Unicode is not far from achieving its goal.

Principle #2: efficiency

It sounds like a slogan out of an advertisement from the 1950s. But it contains a kernel of truth. From the technical point of view, Unicode has enabled us to rid ourselves of escape characters, the states of ISO 2022, and so on. And it is undeniable that the documentation that comes with Unicode (the book, the Web site, the technical reports, the proceedings of the Unicode conferences) is more efficient than the dry, sterile commentary of the ISO standards, when that commentary exists at all. Functions, special characters, algorithms—all are described in minute detail, annotated, explained, and made accessible and ready for implementation.

Principle #3: the difference between characters and glyphs

As we have just discussed in the previous section, characters and glyphs are two totally different concepts, and Unicode is concerned only with the former. Even though it has not yet managed to provide a satisfactory definition of what a character is, Unicode at least deserves credit for having raised the issue and for having led people to understand the confusion that used to reign in this regard.

Principle #4: the well-defined semantics of characters

This principle harks back to what we were said about principle #2: Unicode has undertaken the formidable task of investigating writing systems and documenting its standard. As much as possible, characters are well defined, and their definitions clearly show what they are and what they are not. Knowing the meaning of each of the characters in our documents is important, for this knowledge is the very basis for the storage of textual data.

Principle #5: plain text

Who has never said to a colleague or a friend: “Send me that document in ASCII”? Yet a document in French, Swedish, or Spanish1 can hardly be encoded in ASCII, since it will necessarily contain accented characters. What we mean by this expression is that we want a document in “plain text” format, which means a file containing nothing but miles and miles of text without the slightest bit of markup and without a single binary character that would turn it into a word-processing file. Unicode encodes nothing but text; it has no need for markup or—within practical limits—formatting characters. All information is borne by the characters themselves.

In fact, there is a rather ambiguous relationship between Unicode and, for example, XML. They complement each other perfectly and desperately need each other:

• The basic units of an XML document are, by definition, Unicode characters; therefore, without Unicode, there would be no XML.

1 We have not added German to this list because, theoretically, the German umlauts ‘ä’ ‘ö’ and ‘ü’ can be written as the digraphs ‘ae’, ‘oe’, ‘ue’, and the es-zet ‘ß’ can be written as ‘ss’. Nevertheless, these rules have exceptions: no one will ever write ‘Goethe’ as ‘Göthe’, and the words ‘Maße’ and ‘Masse’ are not the same.. . .

60 Chapter 2 : Characters, glyphs, bytes: An introduction to Unicode

• On the other hand, a certain type of information, such as the direction in which a paragraph is laid out, is best expressed by a high-level protocol such as XML rather than by examining the first letter of the paragraph to check whether it reads from left to right or from right to left (see Chapter 4). In addition, the language of a paragraph can be better indicated with XML’s markup attribute xml:lang than by the completely artificial linguistic labels of Unicode (see p. 88).

Nonetheless, Unicode continues to disregard XML. Under the pretext that all of Unicode’s functionality must be accessible even under the most restrictive protocol (such as URLs, for example), Unicode attempts to mark up a certain number of things itself, without relying on any other markup system. That is without a doubt the true meaning of principle #5.

Principle #6: logical order

How should the bytes be stored inside the computer: from right to left or from left to right? This question is meaningless because bits have no material substance. But we cannot keep from thinking of bytes as little boxes or rectangles that are arranged in a certain direction. This false notion stems, no doubt, from the fact that we confuse the interface of the low-level editor that we use with the actual functioning of the computer. This same false notion leads us to suppose that the natural order of our language is the order used by the computer and that languages written from right to left should be encoded backwards.

Unicode sets things straight. The reading of a document is an action situated in time that, like any other such action, has a certain inherent logical order. Unicode data are encoded in that order, and there is nothing material about the arrangement; therefore, there is no indication of direction. The issue of the direction in which text reads does not arise until the very moment when we begin to present the data visually. The way to render a document containing scripts that run in different directions may be very complex, even if the order in which the text is encoded is strictly logical. To convince ourselves of this fact, we need only read a text of this sort aloud: we will see that we follow the arrangement of Unicode-encoded data very precisely.

Principle #7: unification

To save space and to accommodate all the ideographic characters within fewer than 65,536 code points, Unicode decided to identify the ideographs of Chinese origin that are used in mainland China (the simplified Chinese script), in Taiwan and Hong Kong (traditional Chinese), in Japan, and in Korea. This unification was praised by some, criticized by others. We shall explain its ins and outs in Chapter 4, starting on page 148.

Principle #8: dynamic composition

Some Unicode characters possess special powers: when placed after another character, they modify its glyph. This modification usually involves placing an accent or a diacritical mark somewhere around the glyph of the base character. We call these characters

combining characters. The most interesting feature of these characters is that they can combine with each other and form glyphs with multiple accents, with no limit to the number or the position of the accents and diacritical marks. Their drawback is that they have no respect for the principle of efficiency: if, within a Unicode string, we select a substring that begins with a combining character, this new string will not be a valid string in Unicode. Such an outcome never occurs in a string in ASCII or ISO 8859, and that fact gives Unicode a bit of a bad reputation. It is the price to pay in order to enjoy the power of dynamic composition. We shall describe the combining characters in detail in Chapter 4.

Principle #9: equivalent sequences

For reasons that arise from the tenth principle, Unicode contains a large number of “precomposed” characters—characters whose glyphs are already constructed from a base character and one or more diacritical marks. Principle #9 guarantees that every precomposed character can be decomposed, which means that it can be expressed as a string in which the first character is a base character and the following characters are all combining characters. We shall discuss this matter in detail in Chapter 4.

Principle #10: convertibility

This is the principle that has done the greatest harm to Unicode. It was nonetheless necessary so that the encoding would be accepted by the computer industry. The principle stipulates that conversion of data to Unicode from any recognized official or industrial encoding that existed before May 1993 could be done with no loss of information. This decision is fraught with consequences, as it implies that Unicode must inherit all the errors, imperfections, weaknesses, inconsistencies, and incompatibilities of the existing encodings. We have the almost Messianic image of a Unicode that “taketh away the sin of the world” for our redemption. Perhaps we are getting a bit carried away here, but the fact remains that 99.9% of Unicode’s inconsistencies are due to principle #10 alone. We are told in the documentation that this or that thing exists “for historical reasons”.

But there is a good side as well: there is no risk of losing the slightest bit of information when converting our data to Unicode. That is reassuring, especially for those of us who in the past have had to contend with the results of incorrect conversions.

Unwritten principle #11: permanent stability

We have taken the liberty of adding an eleventh principle to the list of official Unicode principles, one that is important and laden with consequences: as soon as a character has been added to the encoding, that character cannot be removed or altered. The idea is that a document encoded in Unicode today should not become unusable a few years hence, as is often the case with word-processing software documents (such as those produced with MS Word, not to name any names). Unlike the ten official principles, this one is so scrupulously respected that Unicode has come to contain a large number of characters whose use is deprecated by Unicode itself. Even more shocking is that the name of character 0x1D0C5 contains an obvious typo (fhtora instead of fthora = φθορ!); rather

62 Chapter 2 : Characters, glyphs, bytes: An introduction to Unicode

than correcting it, the Consortium has decided to let it stand and to insert a little note along the lines of “yes, we know that there’s an error here; don’t bother to tell us”. We can only hope that the Consortium will allow for minor corrections in the future when they would have little effect on data encoded in Unicode.

Even the philosophers say it: philosophy is not the only thing in life. And in the life of a Unicode user there are also issues of a strictly technical nature, such as the following: how are Unicode characters represented internally in memory? how are they stored on disk? how are they transmitted over the Internet? These are very important questions, for without memory, storage, and transmission there would be no information....

Those who have dealt with networks know that the transmission of information can be described by several layers of protocols, ranging from the lowest layer (the physical layer) to the highest (the application layer: HTTP, FTP, etc.). The same is true of Unicode: officially [347] five levels of representation of characters are distinguished. Here they are:

1. An abstract character repertoire (or “ACR”) is a set of characters—that is, a set of “descriptions of characters” in the sense used in the previous section—with no explicit indication of the position of each character in the Unicode table.

2. A coded character set (or “CCS”) is an abstract character repertoire to which we have added the “positions” or “code points” of the characters in the table. These are whole numbers between 0 and 0x10FFFF (= 1,114,111). We have not yet raised the issue of representing these code points in computers.

3. A character encoding form (or “CEF”) is a possible way to represent the code points of characters on computers. For example, to encode characters on Unicode we usually need 21 bits; but the manner in which operating systems use internal memory makes it more efficient to encode these 21 bits over 32 bits (by leaving the first 11 bits unset) or as a series of wydes (16 bits) or of bytes. An encoding form may be of fixed length (like UTF-32) or variable length (like UTF-16 or UTF-8).

4. A character encoding scheme2 for “CES”) is a representation of characters in bytes. Allow us to explain: when we say, for example, that we encode Unicode characters with 21 bits within 32-bit numbers, that occurs at the level of internal memory, precisely because the internal memory of many computers today uses 32-bit units. But when we store these same data on disk, we write not 32-bit (or 16-bit) numbers but series of four (or two) bytes. And according to the type of processor (Intel or RISC), the most significant byte will be written either first (the “little-endian” system) or last (the “big-endian” system). Therefore, we have both a UTF-32BE and a UTF-32LE, a UTF-16BE and a UTF16LE. Only the encoding form UTF-8 avoids this problem: since it represents the characters in byte format from the outset, there is no need to encode

2 We beg the reader’s forbearance for the proliferation of jargon in this section. The terms used here are official terms taken directly from a Unicode technical report.

the data as a sequence of bytes. Also note that steps (1) to (4) taken collectively are called a “character map”. The names of character maps are registered with IANA [186] so that they can be used within protocols such as MIME and HTTP. There are the following registered character maps for Unicode:

• UTF-8, a very efficient encoding form in which Unicode characters are represented over 1 to 4 bytes (see page 65).

• UTF-7, an unofficial encoding scheme that is quite similar to “base 64”, described in RFC 2152;

• UTF-32, the encoding form in which we use the lowest 21 bits of a 32-bit number.

• UTF-32LE, the encoding scheme for UTF-32 in which a 32-bit number is encoded over four bytes in little-endian order, which means that the least significant byte comes first. This counterintuitive order is used by the Intel processors.

• UTF-32BE is similar to UTF-32LE but uses the big-endian order of the PowerPC, Sparc, and other processors.

• UTF-16, an encoding form in which Unicode characters are represented over one or two wydes (see page 64).

• UTF-16LE, the encoding scheme for UTF-16 in which a 16-bit number is encoded over two bytes in little-endian order.

• UTF-16BE, which is similar to UTF-16LE but uses big-endian order.

• UNICODE-1-1, version 1.1 of Unicode (described in RFC 1641).

• UNICODE-1-1-UTF-7, the former version of UTF-7 (described in RFC 1642).

• CESU-8 is a variant of UTF-8 that handles surrogates differently (see page 65).

• SCSU is a transfer encoding syntax and also a compression method for Unicode (see page 66).

• BOCU-1 is another compression method for Unicode, one that is more efficient than SCSU (see page 66).

The reader will certainly have noticed that UTF-16 and UTF-32, with no indication of endianness, cannot be encoded character maps. The idea is as follows: if we specify one of these, either we are in memory, in which case the issue of representation as a sequence of bytes does not arise, or we are using a method that enables us to detect the endianness of the document. We shall discuss the latter on page 64.

5. Finally, a transfer encoding syntax (or “TES”) is a “transcription” that can occur at the very end to adapt data to certain transmission environments. We can imagine a conversion of the bytes from the encoding scheme into hexadecimal, “quoted-printable” (page 49), or “base 64” (page 49) so that they can be transmitted through a medium that does not accept binary-coded data, such as electronic mail.

In a conventional 8-bit encoding, steps (2) and (3) do not arise: there is no need to fill out our units of storage or to worry about big-endian or little-endian systems because we are

64 Chapter 2 : Characters, glyphs, bytes: An introduction to Unicode

already at the byte level. Things are not so trivial for the East Asian encodings that we have seen on page 48. In the case of Japanese, JIS X 0201-1976 is both an abstract character repertoire and a coded character set. It becomes an encoding form when we use 16 bits to represent its 94 × 94 tables. Finally, ISO 2022-JP, Shift-JIS, and EUC-JP are encoding schemes. And when we use them for electronic mail, we employ a transfer encoding syntax such as “quoted-printable” or “base 64”.

Now a bit of history. In the beginning, Unicode was encoded with 16 bits, with little concern about endianness. At an early date, UTF-8 was put forward (under different names) to resolve a certain number of problems, such as the issue of endianness. At the same time, Unicode’s bigger cousin, ISO 10646, proposed two encoding forms: UCS-4, which used 31 bits of a 32-bit number (thus avoiding the issue of how to know whether the number was signed or not), and UCS-2, which took the first wyde of this number and ignored the rest.

UTF-16 and surrogates

When the Consortium realized that 16 bits were insufficient, a trick was suggested: instead of extending Unicode by adding bits, we could reserve two areas for surrogates: the high and low surrogate areas. We would then take a surrogate pair consisting of two wydes: the first from the high area, the second from the low area. This approach would enable us to encode far more characters.

These areas are 0xD800-0xDBFF (the high surrogate area) and 0xDC00-0xDFFF (the low surrogate area). They give us 1,0242 = 1,048,576 supplementary characters encoded with two wydes. Thanks to surrogate pairs, we can obtain any character between 0x10000 and 0x10FFFF (Unicode’s current limits). This is how we proceed: Let A be the code point of a character. We subtract 0x10000 from A to obtain a number between 0x00 and 0xFFFFF, which is therefore a 20-bit number. We divide these 20 bits into two groups:

xxxxxxxxxxyyyyyyyyyy

and we use these groups to form the first and the second wydes of the surrogate pair, as follows:

110110xxxxxxxxxx 110111yyyyyyyyyy

Detection of endianness

Consider a 16-bit number whose numerical value is 1. If this number is encoded in bigendian order, we will write to the disk 0x00 0x01, which corresponds to our intuition. On the other hand, if it is encoded in little-endian order, we will write 0x01 0x00. Unicode devised a very clever way to indicate the endianness of a block of text. The approach uses a character called the byte order mark, or “BOM”. This character is 0xFEFF. This method works because the “inverse” of this character, namely 0xFFFE, is an invalid character. If at

the beginning of a document the software encounters 0xFFFE, it will know that it must be reading the bytes in the wrong order.

We may well ask what happens to these parasitic BOMs. After all, if we cut and paste Unicode strings that contain BOMs, we may end up with a flurry of BOMs throughout our document. Not to worry: this character is completely harmless and should be ignored3

by the rendering engine as well as by routines for searching, sorting, etc.

In the case of UTF-32, the BOM is the character 0x0000FEFF. There as well, its inverse, 0xFFFE0000, is not a character, as it greatly exceeds the limit of 0x10FFFF.

UTF-8 and CESU-8

UTF-8 is the most commonly used encoding form because it is the default character set for XML. It incorporates both an encoding form and an encoding scheme, as it consists of bytes. The idea is very simple: the 21 bits of a Unicode code point are distributed over 1, 2, 3, or 4 bytes that have characteristic high bits. From these bits, we can recognize whether a byte is the beginning of a sequence of 1, 2, 3, or 4 bytes or whether it occurs in the middle of one such sequence.

Here is how the bits are distributed:

Code point Byte 1 Byte 2 Byte 3 Byte 4

00000 00000000 0xxxxxxx 0xxxxxxx

00000 00000yyy yyxxxxxx 110yyyyy 10xxxxxx

00000 zzzzyyyy yyxxxxxx 1110zzzz 10yyyyyy 10xxxxxx

uuuuu zzzzyyyy yyxxxxxx 11110uuu 10uuzzzz 10yyyyyy 10xxxxxx

We can see that the first byte of a sequence begins with two, three, or four set bits, according to the length of the sequence. If a byte begins with a single set bit, then it occurs in the middle of a sequence. Finally, if a byte begins with a cleared bit, it is an ASCII character, and such characters are not affected by UTF-8. Thus we can see the key to the success of this encoding form: all documents written in ASCII—which means the great majority of documents in the English language—are already encoded in UTF-8.

The drawback of UTF-8 is that it is necessary to divide a string of bytes at the right place in order to obtain a string of characters. If we break a string of UTF-8 bytes just before an intermediate byte, we obtain an invalid string; therefore, the software may either reject it or ignore the intermediate bytes and start from the first byte that begins a sequence. It is therefore recommended, when manipulating strings of UTF-8 bytes, always to examine the three preceding bytes to find the byte that begins the nearest sequence.

3 That has not always been the case. Indeed, the name of this character is zero-width no-break space. The problem with this name is the “no-break” property. Before Unicode 3.2, this name was taken literally, and if BOM happened to fall between two syllables of a word, the word could not be broken at that point. But later another character was defined for that purpose, character 0x2060 word joiner; and now the BOM is used only to detect byte order.

66 Chapter 2 : Characters, glyphs, bytes: An introduction to Unicode

CESU-8 (Compatibility Encoding Scheme for UTF-16: 8-bit, [292]) is a curious blend of UTF- 16 and UTF-8. In CESU-8, we start by converting our document into UTF-16, using surrogate pairs; then we convert each wyde into UTF-8. A document encoded in CESU-8 may take up more space than one encoded in UTF-8. Each wyde may thus need as many as three bytes for its representation; each pair of wydes, as many as six.

SCSU and BOCU

SCSU (Standard Compression Scheme for Unicode [353]) is a compression scheme for text encoded in Unicode. It was defined in a technical report by the Unicode Consortium. The principle is simple: we have a sort of “window” onto the Unicode table, a window 128 characters wide, whose exact location can therefore vary. Eight such “dynamically positioned” windows are available, which we can redefine at any time, and also eight “static” windows, whose locations are fixed.

In the initial state, we are in window 0. When we specify a shift to window n, the characters in the window become accessible through numerical values of only one byte each. More precisely, if the active window is window n, then a byte B between 0x00 and 0x7F is interpreted as being within the static window at an offset of B from the window’s origin; and if B is a byte between 0x80 and 0xFF, then we go to dynamic window n and select the character located at an offset of B−128 from that window’s origin.

SCSU operates in two modes: the “compression” mode, in which bytes are interpreted as Unicode characters within a static or dynamically positioned window, and the “Unicode” mode, in which wydes are interpreted as UTF-16 sequences.

When we begin to (de)compress data, we are in the initial mode: “compression” mode, window 0 as the active window, all dynamically positioned windows in their default positions. Here are the fixed positions of the static windows and the default positions for the dynamically positioned windows:

# static window dynamically positioned window, by default

0 0x0000 (ASCII) 0x0080 (Latin 1)

1 0x0080 (Latin 1) 0x00C0 (Latin 1++)

2 0x0100 (Latin Extended-A) 0x0400 (Cyrillic)

3 0x0300 (Diacritical marks) 0x0600 (Arabic)

4 0x2000 (General punctuation) 0x0900 (Devanagari)

5 0x2080 (Currency symbols) 0x3040 (Hiragana)

6 0x2100 (Letterlike symbols) 0x30A0 (Katakana)

7 0x3000 (CJK symbols and punctuation) 0xFF00 (full-width ASCII)

There are six escape characters:

• SQU 0x0E (Quote Unicode), followed by a big-endian wyde: directly select the Unicode character specified by the wyde, irrespective of the windows. This is a temporary change of mode.

• SCU 0x0F (Change to Unicode): change to UTF-16 mode, irrespective of the windows. This is a permanent change of mode, in effect until another change is made.

• SQn 0x01-0x08 (Quote from Window n, followed by byte B: if B is in the interval 0x00-0x7F, we use static window n; otherwise, we use dynamic window n. This is a temporary change of mode.

• SCn 0x10-0x17 (Change to Window n), followed by byte B: use dynamically positioned window n for all of the following characters in the range 0x80-0xFF and window 0 (ASCII) for the characters 0x09, 0x0A, 0x0D, and those in the range 0x20-0x7F. This is a permanent change of mode, in effect until another change is made.

• SDn 0x18-0x1F (Define Window n), followed by byte B: redefine dynamically positioned window n as the window whose index is B. How do we specify windows using an index? The reader who is expecting an elegant and universally applicable calculation will be disappointed. In fact, we use the following table:

Index B Origin of the window Comments

0x00 value reserved

0x01-0x67 B×80 the half-blocks from 0x0080 to 0x3380

0x68-0xA7 B×80+0xAC00 the half-blocks from 0xE000 to 0xFF80

0xA8-0xF8 values reserved

0xF9 0x00C0 Latin letters

0xFA 0x0250 Phonetic alphabet

0xFB 0x0370 Mutilated (“monotonic”) Greek

0xFC 0x0530 Armenian

0xFD 0x3040 Hiragana

0xFE 0x30A0 Katakana

0xFF 0xFF60 Half-width katakana

• SDX 0x0B (Define Extended) followed by wyde W. Let W ′ be the first three bits of W and W ′′ the remaining bits (W = 213 ·W ′ +W ′′). We redefine the dynamically positioned window whose index is W ′ as being at origin 0x10000+80·W ′′.

We can notice a certain asymmetry between SQn and SCn: the first allows us to use static windows 0 to 7, the second can only use static window 0. Only one question remains: when we are in Unicode mode, how do we switch back to “windows” mode?

The problem is that in Unicode mode the decompression algorithm is reading wydes. The solution is to provide it with wydes that it does not expect to see: those whose first byte is in the range 0xE0-0xF1. These wydes are in Unicode’s private use area; to use them in Unicode mode, we have the escape character UQU (see below). When the decompression algorithm encounters such a wyde, it immediately switches to “windows” mode and interprets the wyde as a pair of bytes whose first character is an escape character from the following list:

68 Chapter 2 : Characters, glyphs, bytes: An introduction to Unicode

• UQU 0xF0 (Quote Unicode), followed by a big-endian wyde: directly select the Unicode character specified by the wyde, without interpreting it as an escape character. This is a temporary change of mode.

• UCn 0xE0-0xE7 (Change to Window n), followed by byte B: same behavior as SCn.

• UDn 0xE8-0xEF (Define Window n), followed by byte B: same behavior as SDn.

• UDX 0xF1 (Define Extended), followed by wyde W: same behavior as UDn.

We can see that, as with most self-respecting compression schemes, there are more ways than one to compress data and the rates of compression obtained depend upon the skill of the compression algorithm: the judicious selection of dynamically positioned windows, switching to locking shift or the use of temporary escape sequences, etc. Thus we can use more or less sophisticated tools for compression by making several passes and compiling statistics and the like. But there is only a single approach to decompression, and it is quite simple to implement.

BOCU-1 (Binary Ordered Compression for Unicode, [313]) is another compression scheme; its performance is equal to that of SCSU, but it has some benefits of its own: it is MIMEcompatible, and code point order is preserved. This final property implies that if we take a set of Unicode strings compressed in BOCU-1 and sort them, they will be arranged in the same order as the original strings. That could be convenient for a database: the fields would be compressed, yet they could still be sorted without first undergoing decompression.

Another major benefit of BOCU-1: it is “deterministic”, in the sense that there is only one way to compress a string. That fact implies that we can compare compressed files: if they are different, then the decompressed originals will be different as well.

We shall not describe BOCU’s compression algorithm in detail. The reader will find the description and some accompanying C code in [110], a document that starts with a fine French quotation from Montesquieu: “il faut avoir beaucoup étudié pour savoir peu” (you have to study a great deal to know a little). The idea behind this compression scheme is to encode the difference between two consecutive characters. Thus as long as we remain within the same script, we can encode our document with single bytes— provided that the script be “small”. Writers will notice that this idea is not very efficient, as we often make “leaps” within the encoding to insert spaces or punctuation marks (which are shared by a large number of writing systems). Accordingly, the difference is determined not from the last character, but from the last three characters—an approach that reduces the differences.

The technique of using differences, which is also employed in compression algorithms such as MPEG, is of great interest because it starts from the notion that a document written in Unicode will reflect a certain consistency with regard to writing systems. A user may know N languages, which use M writing systems altogether (often M < N). There is a good chance that the user’s documents are distributed across these writing systems,

0x100000

Plane 16 Allocated Codepoints

0xF0000

Surrogate pairs

Plane 15

Private zone

0xE0000

(11 non-occupied planes)

Plane 14 (SSP)

0x20000

Plane 2 (SIP)

0x10000

Plane 1 (SMP)

0x0000

0x10FFFD Plane 0 (BMP)

0xFFFFD

0xEFFFD

0x2FFFD

0x1FFFD

0xFFFD

Figure 2-2: The six currently “populated” planes of Unicode (version 4).

::: tip Architecture Diagram: Populated Planes of Unicode (Figure 2-2)
![Figure 2-2: Populated planes of Unicode](/images/fonts-encodings/fig2-2-populated-planes-unicode.png)
*Figure 2-2: The populated planes of the 21-bit Unicode codespace: BMP (Plane 0), SMP (Plane 1), SIP (Plane 2), SSP (Plane 14), and Private Use Planes (Planes 15 & 16).*
:::



which greatly reduces the range of characters used and ensures the success of a means of compression that is based on the proximity of characters.

We hope to see BOCU-1 compression used more and more in the years to come.

70 Chapter 2 : Characters, glyphs, bytes: An introduction to Unicode

Code points may range from 0 to 0x10FFFF (= 1 114 111). We divide this range into 17 planes, which we number from 0 to 16. Of these 17 planes, only 6 are currently “populated” (see Fig. 2-2):

• Plane 0, or the BMP (Basic Multilingual Plane), corresponds to the first 16 bits of Unicode. It covers most modern writing systems.

• Plane 1, or the SMP (Supplementary Multilingual Plane), covers certain historic writing systems as well as various systems of notation, such as Western and Byzantine musical notation, mathematical symbols, etc.

• Plane 2, or the SIP (Supplementary Ideographic Plane), is the catchall for the new ideographs that are added every year. We can predict that when this plane is filled up we will proceed to Plane 3 and beyond. We shall discuss the special characteristics of ideographic writing systems in Chapter 4.

• Plane 14, or the SSP (Supplementary Special-Purpose Plane), is in some senses a quarantine area. In it are placed all the questionable characters that are meant to be isolated as much as possible from the “sound” characters in the hope that users will not notice them. Among those are the “language tag” characters, a Unicode device for indicating the current language that has come under heavy criticism by those, the author among them, who believe that markup is the province of higher-level languages such as XML.

• Planes 15 and 16 are Unicode’s gift to the industry: they are private use areas, and everyone is free to use their codepoints in applications, with any desired meaning.

This plane—which for many years made up all of Unicode—is organized as follows:

 The first block of 8 columns (0x0000-0x007F) is identical to ASCII

(ISO 646).

 The second block of 8 columns (0x0080-0x00FF) is identical to

ISO 8859-1. The character 0x00AD soft hyphen represents a potential place to divide a word and therefore should not have a glyph (unless the word is divided at that point, in which case its glyph depends on the language and writing system). Do not confuse it with 0x2027 hyphenation point, which is the midpoint used in dictionaries to show where word division is permitted.

[ %˘a ˛a5ˆc˙cˇcd’Æ& ] Still in the Latin alphabet, the Latin Extended-A block (0x0100-

0x017F) which contains the characters of Central Europe, the Baltic countries, Maltese, Esperanto, etc.

x0 x1 x2 x3 x4 x5 x6 x7 x8 x9 xA xB xC xD xE xF

       Indic Scripts . /



0x









!

#

  

1x





 

 

  

"

\$

2x



x

z y

3x

CJK Unified Ideographs Extension A

{

4x

5x

6x

CJK Unified Ideographs

7x

8x

9x

} | ~

Yi Syllables

Ax

Bx

Hangul Syllables

Cx

³ Á

Dx

Ex

Private Zone

Ç ´ µÈ ¶

Fx

Figure 2-3: The roadmap of Unicode’s Basic Multilingual Plane (BMP):  ASCII and Latin 1,  Latin Extended-A and -B,  phonetic alphabet and modifiers,  diacritical marks,  Greek (crippled by the monotonic reform) and Coptic,  Cyrillic,  Armenian,  Hebrew,  Arabic,  Syriac, Thaana and N’ko, . Thai and Lao, / Tibetan,  Myanmar and Georgian,  elements for forming hangul syllables, 	 Amharic,  Cherokee,  Canadian aboriginal scripts,  runes, 0 scripts of the Philippines, 1 Khmer,  Mongolian,  Limbu, Tai Le, etc.,  Balinese,  phonetic extensions, ! Latin Extended Additional, # Greek with accents and breathings (as it should be),  general punctuation, superscripts and subscripts, currency symbols, diacritical marks for symbols,  letterlike symbols, Roman numerals   arrows, mathematical and technical symbols,  graphic pictures for control codes, OCR,  enclosed alphanumerics,  geometric shapes,  miscellaneous symbols,  “Zapf dingbats”,  braille,  supplemental arrows and mathematical symbols,  Glagolitic and Latin Extended-C,  Coptic disunified from Greek,  Khutsuri, Tifinagh and Ethiopic Extended,  Supplemental Punctuation, " ideographic radicals, \$ ideographic description characters,  ideographic punctuation, x kana, e bopomofo, hangul supplement, kanbun and CJK strokes, z enclosed ideographs and abbreviations used in ideographic writing systems, { Yijing hexagrams, | modified tone letters and Latin Extended-D, } Syloti Nagri, ~ Phags-pa, ³ highhalf zone for surrogates, Á low zone, ´ compatibility ideographs, Ç presentation forms A (Latin, Armenian, Hebrew, Arabic), µ variation selectors and other oddities, È presentation forms B (Arabic), ¶ full-width Latin letters and halfwidth katakana, specials.

::: tip Global Roadmap: The Basic Multilingual Plane (Figure 2-3)
![Figure 2-3: The BMP roadmap](/images/fonts-encodings/fig2-3-bmp-roadmap.png)
*Figure 2-3: Complete roadmap of Unicode's Basic Multilingual Plane (BMP, Plane 0).*
:::



72 Chapter 2 : Characters, glyphs, bytes: An introduction to Unicode

 Wrapping up the series of Latin characters, the Latin Extended-

B block (0x0180-0x024F), home to numerous rare and strange characters as well as some that Western linguists cobbled together for the African languages. Also in this block are the Romanian characters ‘¨’ and ‘≠’, which previously were conflated with the characters ‘¸s’ and ‘¸t’ (which have a cedilla instead of the comma). Finally, there are three digraphs—‘dž’, ‘lj’, and ‘nj’—which are the Latin versions of the Cyrillic letters ‘’, ‘y’, and ‘z’. The original idea behind these was to establish a one-to-one correspondence between the Serbian alphabet and the Croatian alphabet. But there is a problem: the upper-case version of the digraph will differ according to whether it appears as the first letter of a capitalized word (‘Dž’, ‘Lj’, ‘Nj’) or as a letter in a word written in full capitals (‘DŽ’, ‘LJ’, ‘NJ’). It was therefore necessary to include both forms in Unicode.  There are 6 columns (0x0250-0x02AF) for the special letters of

the International Phonetic Alphabet. This alphabet is typically unicameral (i.e., written only in lower case), except for those letters within it that are also used as ordinary letters in African languages. The upper-case versions of those letters appear in the “Latin Extended-B” block.

 Five columns (0x02B0-0x02FF) are allocated to the phonetic modifiers.

These are small spacing characters that are used to indicate or modify the pronunciation of the preceding or following letter. For example, the five tones of transcribed Chinese are found in this block.  The block for diacritical marks (7 columns, 0x0300-0x036F),

which contains the accents and other diacritical marks of most languages. This block also contains 0x034F combining grapheme joiner, whose function is to allow a combining character to be applied to more than one glyph at once (see page 116).

[ αβγδεζηθικ ] Now we come to the block shared by Greek and Coptic (9 columns,

0x0374-0x03FC). Greek is only partly covered because the letters with breathings, accents, and iota subscripts are found in the “Greek Extended” block, which we shall see later. This block suffers from the dual use of the Greek alphabet for text in the Greek language and for mathematical formulae. Thus we find in it the two contextual forms of beta, ‘β’ and ‘%’ (the former being used—in Greece and France—at the beginning of a word and the latter in the middle or at the end of a word), listed as separate characters. In addition, we find two versions each of theta, phi, rho, and kappa, which ordinarily are nothing but glyphs from different fonts, included here simply because they are used as distinct symbols in mathematics. Finally, there are some characters used as numerals (sampi, koppa, stigma) and some that are archaic or used in transcriptions.

[ абвгдежзий ] Next comes the block for the Cyrillic alphabet (17 columns,

0x0400-0x0513), which covers three categories of symbols: the letters used for Russian and the other European languages written in the Cyrillic alphabet (Serbian, Macedonian, Bulgarian, Byelorussian, Ukrainian, etc.); the letters, diacritical marks,

and numeric symbols of Old Cyrillic (an ancient script still used for liturgical documents); and finally the letters of the Asian languages written in the Cyrillic alphabet (Abkhaz, Azerbaijani, Bashkir, Uzbek, Tajik, etc.). The special Asian letters are no less contrived or strange than those of Latin Extended-B; once again, it was necessary to devise new letters on the basis of an existing alphabet to represent sounds in these languages that do not occur in Russian, and the results are sometimes startling. [ abgdezôœïì ] Between East and West, the Armenian alphabet (6 columns,

0x0530-0x058A), in which the ‘ú’ ligature is considered a character because it is used almost exclusively to represent the word “and” in Armenian.  And now for the Semitic languages. First, Hebrew (7 columns,

0x0591-0x05F4), in which there are four types of symbols: the Masoretic cantillation signs (musical notation for the chanting of the Bible), the short vowels and semivowels, the Hebrew letters (with the final forms of the letters separately encoded), and finally the three ligatures used in Yiddish. Of these four categories, the first two are almost completely made up of combining characters.

 Next comes Arabic (16 columns, 0x0600-0x06FF, and a supplement of

3 columns 0x0750-0x076D), where we find the letters, short vowels, and diacritical marks of Standard Arabic, the letters used by other languages written in the Arabic script (Persian, Urdu, Pashtu, Sindhi, etc.), and a certain number of signs used to guide recitation of the Koran and indicate its structure. Unlike those of Hebrew, the contextual forms of Arabic are not encoded as separate characters. Nevertheless, contextual forms and even ligatures of an æsthetic nature are encoded in the section for “presentation forms”, near the end of the BMP. There is nothing inherently Arabic about the character ‘⋆’ 0x066D arabic five pointed star; it was provided only to ensure that a five-pointed asterisk would be available, as the ordinary asterisk ‘*’, with its six lobes, might be mistaken for a Star of David in print of poor quality. Finally, there are two series of digits (0x0660-0x0669 and 0x06F0-0x06F9): the first matches the glyphs used in Arabic; the second, those used in the languages of Iran, Pakistan, and India.  Syriac (5 columns, 0x0700-0x074F) is the writing system of the

Christian Arabs. Not being the national script of any country, it took a long time to be standardized and added to Unicode. The alphabet bears a vague resemblance to Arabic. There is a profusion of short vowels because two systems of vowel pointing are in use: a set of dots and a set of signs derived from the Greek vowels.  The last writing system of this group is Thaana (4 columns,

0x0780-0x07B1). This script, inspired by Arabic, is used to write the Dhivehi language, spoken in the Maldives. A distinctive feature of Thaana is that the vowels must be written.  Between the Semitic and the Indic languages, Unicode v. 5 has

managed to squeeze the very exotic script N’Ko (4 columns, 0x07C0-0x07FA). This

74 Chapter 2 : Characters, glyphs, bytes: An introduction to Unicode

is another artificial script, created by an African leader, Sulemana Kante, in 1948. It is used in Guinea, Côte d’Ivoire, and southern Mali.

 Now we come to the long list of writing systems of India.

These have all been encoded according to a single phonetic principle. Accordingly, characters of the same pronunciation appear in the same location in the tables for the respective scripts. In addition, the writing systems are encoded in geographic order, from north to south. Thus the first script is Devanagari (8 columns, 0x0901- 0x097F), which is still used for Hindi but also for Sanskrit. Since Sanskrit has a rich variety of phonemes, it comes as no surprise that the table for Devanagari is almost full whereas those for the languages of southern India become sparser as we go. We can also see that the letters’ strokes are pointed in the north but rounder and rounder as we move southward, where most writing was done on palm leaves.

::: tip Authentic Typographical Specimen: South Asian Indic Scripts (Plate 2-1)
![Plate 2-1: South Asian Indic Scripts](/images/fonts-encodings/plate2-1-south-asian-scripts.png)
*Plate 2-1: Authentic script specimens from Devanagari, Bengali, Gurmukhi, Gujarati, Oriya, Tamil, Telugu, Kannada, Malayalam, and Sinhala (from original book p. 75).*
:::



 Second is Bengali (8 columns, 0x0981-0x09FA), used principally

in Bangladesh.

 Next comes Gurmukhi (8 columns, 0x0A01-0x0A74), which is

used to write the Punjabi language, spoken in northern India.

 Gujarati (8 columns, 0x0A81-0x0AF1), which looks like De-

vanagari without the characteristic horizontal bar.

 Oriya (8 columns, 0x0B01-0x0B71), a script noticeably

rounder than the previous ones.

[ †°¢£§•¶ß®© ] Tamil (8 columns, 0x0B82-0x0BFA), without a doubt

the best-known script in southern India. It is simpler than the scripts of the north, as can be seen at a glance from the Unicode table for Tamil, which contains only 69 characters, whereas the table for Devanagari contains 105.

[ ™´¨≠ÆØ∞±≤≥] Telugu (8 columns, 0x0C01-0x0C6F), a script rounder

than that of Tamil that is used in the state of Andhra Pradesh.

[ ¥μ∂∑∏π∫ªºΩ ] Kannada, or Kanarese (8 columns, 0x0C82-0x0CF2),

a script very similar to the previous one, used in the state of Karnataka.

[ æø¿¡¬√ƒ≈Δ« ] Malayalam (8 columns, 0x0D02-

0x0D6F), a script used in the state of Kerala.

[ »… ÀÃÕŒœ–— ] Finally, because south of the island of Sri Lanka

there is nothing but the Indian Ocean, we have Sinhala, or Sin(g)halese (8 columns, 0x0D82-0x0DF4), a script composed almost entirely of curves, with a strong contrast between downstrokes and upstrokes.

[ “”‘’÷◊ÿŸ⁄€ ] Having finished the languages of India, we continue to those

of Southeast Asia. We shall begin with the Thai script (8 columns, 0x0E01-0x0E5B), which was doubtless encoded first because of its flourishing computer market. Thai has diacritics for vowels and tone marks. [ ‹›fifl‡·‚„‰Â ] Geographically and graphically close to Thai is Lao (8 col-

::: tip Authentic Typographical Specimen: Southeast Asian & Central Scripts (Plate 2-2)
![Plate 2-2: Southeast Asian & Central Scripts](/images/fonts-encodings/plate2-2-southeast-asian-scripts.png)
*Plate 2-2: Authentic script specimens from Thai, Lao, Tibetan, Myanmar, Georgian, and Ethiopic (Amharic) (from original book p. 76).*
:::



umns, 0x0E81-0x0EDD). This script is simpler and rounder than Thai and also contains fewer characters.  We might have expected to find Khmer here, but that is

not the case. We shall take a geographic leap and move from the tropical heat of the Mekong River to the cold peaks of the Himalaya, where Tibetan (16 columns, 0x0F00-0x0FD1) is spoken and written. This angular script operates according to the same principle as Khmer: when a consonant with no vowel is followed by a second consonant, the latter is written beneath the former. Unlike Khmer, Tibetan has codes for the subjoined consonants in its block.

[ ÒÚÛÙıˆ˜¯˘˙ ] Next comes Burmese (or Myanmar) (10 columns,

0x1000-0x1059), the script of Burma, similar to the scripts of India as well as those of Southeast Asia.

 Another geographic leap: we head offto the Caucasus to encode

the Georgian script (6 columns, 0x10A0-0x10FC), which ordinarily should have been placed near Armenian. There have been several misunderstandings with regard to Georgian. The Unicode table speaks of “capital” Georgian letters (for example, georgian capital letter an) and of caseless letters (georgian letter an). In fact, the modern Georgian script is unicameral. Two issues gave rise to the confusion. First, the fact that there are two types of Georgian fonts: those for running text and those for titles. The former have glyphs with ascenders and descenders (see the sample above), whereas in the latter the glyphs are all of the same height and no depth: fifl‡·‚„‰ÂÊÁ. Second, in the ancient Georgian script, khutsuri, there were indeed two cases. Thus we find in the Unicode table the capitals of khutsuri (*+,-./0123) and the caseless letters of modern Georgian.

 After Georgian comes a block of 16 columns

(0x1100-0x11F9) containing the basic elements of the Korean syllabic script hangul. As we shall see later (page 155), these elements combine graphically within an ideographic square to form hangul syllables. Unicode also has a rather large area for precomposed hangul syllables.

 We continue to leap about. From Korea we leave for

Ethiopia, since the following block is dedicated to the Amharic (or Ethiopic) script. This block is rather large (24 columns, 0x1200-0x137C with a supplement of another 2 columns 0x1380-0x1399) because the script is syllabic and all of the possible syllables (combinations of a consonant and a vowel) have been encoded. The block

76 Chapter 2 : Characters, glyphs, bytes: An introduction to Unicode

also contains punctuation, digits, and some signs used in numeration. Amharic is the only Semitic script written from left to right.  Next is a rather picturesque script, that of the Cherokee Indi-

::: tip Authentic Typographical Specimen: Indigenous & Historic Scripts (Plate 2-3)
![Plate 2-3: Indigenous & Historic Scripts](/images/fonts-encodings/plate2-3-indigenous-historic-scripts.png)
*Plate 2-3: Authentic specimens of Cherokee syllabary, Canadian Aboriginal, Ogham, Runes, Philippine scripts (Tagalog, Hanunoo, Buhid, Tagbanwa), Khmer, and Mongolian (p. 77).*
:::



ans, which is still used today by some 20,000 people. When this language had no writing system, a tribal chief devised one for it that was later adapted to printing. To facilitate the adaptation, capital Latin letters were selected—but in a way not compatible with their original phonetics—and sometimes slightly modified for use in writing Cherokee. An example: the Cherokee phonemes ‘a’, ‘e’, and ‘i’ are respectively written with the letters ‘D’, ‘R’, and ‘T’. The Cherokee block occupies 6 columns (0x13A0-0x13F4).

 The Native Canadians also have a syllabary that was in-

vented from scratch in 1830. This time, all sorts of geometric shapes were employed. Unicode has collected symbols for some of Canada’s indigenous languages in a 40- column block (0x1401-0x1676).  The next script is Ogham (2 columns, 0x1680-0x169C),

a very ancient Irish script (5th century CE). It is made up of strokes written above or below a baseline. Note that the “blank space” (i.e., the word separator) of this script is not a blank but a horizontal stroke.  Similar is the runic script (6 columns, 0x16A0-0x16F0), used by

the Germanic, Anglo-Saxon, and Scandinavian peoples (the Vikings in particular) before the spread of the Latin script.  Next come four blocks (2 columns each, 0x1700-

0x1714, etc.) that cover four writing systems of the Philippines: Tagalog (see the sample above), Hanunóo (ÑÖÜáàâäãåç), Buhid (éèêëíìîïñó), and Tagbanwa (ËÈÍÎÏÌÓÔÒ). These scripts have the same structure, and their glyphs are so similar that they sometimes look like glyphs from the same script in different fonts. [ òôöõúùûü†° ] Only now do we come to the block for Khmer (8 columns,

0x1780-0x17F9), the main script used in Cambodia. The script appears at this late point because it took a long time to be standardized.4

[ ¢£§•¶ß®©™´ ] After Khmer comes Mongolian (11 columns, 0x1800-0x18A9). This

script is derived from Syriac (as it was taken to Mongolia by Syriac missionaries)

4 Worse yet, its standardization provoked a major diplomatic incident. The method used to encode this language is the same as for Thai; yet the Cambodians, including the Cambodian government, feel that their writing system should have been encoded according to the Tibetan model, i.e., by setting aside Unicode code points for the subscript consonants. Not even the presence of a Cambodian government minister at a Unicode conference succeeded in getting the Khmer block in Unicode modified—a lamentable situation for an encoding that exists to serve the speakers of a language, not the blind pride of a consortium. Let us hope that this incident will be resolved by the next version of Unicode, before the Cambodian government turns to the United Nations or the International Court of Justice in The Hague.. . .

but, unlike Syriac, it is written from top to bottom. Contextuality in Mongolian is so complex that Unicode has provided four characters whose purpose is to modify glyphs: three variation selectors (0x180B-0x180D) and a vowel separator (0x180E).

[ ¨≠ÆØ∞±≤≥¥μ ] Limbu (5 columns, 0x1900-0x194F) is a minority language

in Nepal and northern India that is spoken by approximately 200,000 people.

[ ÚÛÙıˆ˜¯˘˙˚ ] Tai Le (3 columns, 0x1950-0x1974) is another Southeast Asian writ-

ing system.

 The so called New Tai Le or Xishuang Banna Dai script

(6 columns, 0x1980-0x19DF) which is also used by minorities in Southeast Asia.

[ ∂∑∏π∫ªºΩæø ] The two columns 0x19E0-0x19FF contain combinations of Cambo-

dian letters and numbers that are used in lunar dates. [ ¿¡¬√ƒ≈Δ«»… ] Next comes Buginese (2 columns, 0x1A00-0x1A1F), a

writing system used on the Indonesian island of Sulawesi (Celebes).

 Balinese (8 columns, 0x1B00-0x1B7C), the script of Bali, a

province of Indonesia, used by nearly 3 million people. (Actually, the Balinese language is also written in the Latin script.)

[ ¿¡¬√ƒ≈Δ«»… ] Then there is a block of phonetic letters (8 columns, 0x1D00-0x1D7F,

followed by a supplement of an additional 4 columns 0x1D80-0x1DBF) that extends the block of the International Phonetic Alphabet. It consists of Latin letters turned in various ways, some ligatures that are not very kosher, some small capitals, some Greek and Cyrillic letters, etc.

—— A small supplement to the block of diacritical marks (4 columns, 0x1DC0-0x1DFF).

[  ÀÃÕŒœ–—“” ] The Latin Extended Additional block (16 columns, 0x1E00-0x1EF9)

contains characters that are useful for the transcription of Indian languages as well as for Vietnamese and Welsh.  After this tour of the world of characters, and in last place be-

fore the non-alphabetic characters, finally comes regular Greek (16 columns, 0x1F00- 0x1FFE), which Unicode calls “Greek Extended”. This block contains the Greek letters with accents, breathings, and the iota subscript, which uneducated Greek engineers had the nerve to separate from the unaccented Greek letters. The acute accent, sole survivor of the massacre known as the “monotonic” reform (see ), appears over letters in the first block and the second block alike: in the first block, Unicode calls it tonos (= ‘accent’); in the second block, oxia. [ –—‘’‚Ã“”„Õ ] We have reached a turning point in the BMP: the block for general

punctuation (7 columns, 0x2000-0x206F). This table contains punctuation marks that were not included in ASCII and ISO 8859-1 (the true apostrophe ‘ ’ ’, the English

78 Chapter 2 : Characters, glyphs, bytes: An introduction to Unicode

double quotation marks ‘ “” ’, the German quotation marks ‘„’, the dagger and double dagger ‘†’ ‘‡’, the en dash ‘–’, the em dash ‘—’, etc.), some proofreading symbols, and other similar characters. There is also a set of typographic spaces: the em quad, en quad, three-per-em space, four-per-em space, six-per-em space, thin space, hair space, zero-width space (a space that ordinarily has no width but may result in increased spacing during justification). There are also a certain number of control characters: zero-width joiners and non-joiners, together with indicators of the direction of the text, which we shall see on page 142. Finally, for use in entering mathematical formulae, an invisible character placed between a function and its argument, another that indicates multiplication, and a third that acts as a comma in a list of symbols.

 The digits and parentheses as superscripts and subscripts (3 columns,

0x2070-0x2094.

[ ‘’÷◊ÿŸ⁄€‹› ] The currency symbols (3 columns, 0x20A0-0x20B5), where we

find the euro sign and also a number of symbols that have never been used, such as those for the ecu ‘«’, the drachma ‘»’, and even the French franc ‘Δ’.

[ ËÈÍÎÏÌÓÔÒ ] Diacritical marks for symbols (3 columns, 0x20D0-

0x20EF). These include various ways to modify a symbol: striking through it, encircling it, enclosing it in a triangle in the manner of European road signs, etc.

[ ÚÛÙıˆ˜¯˘˙˚ ] The letterlike symbols (5 columns, 0x2100-0x214E). These

are letters of the alphabet, sometimes rendered in a specific font, alone or in groups, that acquire a special meaning in a given context. Thus we have the signs for degrees Celsius ‘°C’, the rational numbers ‘Q’, the real part of a complex number ‘R’, the first transfinite cardinal number ‘ℵ’, and many other symbols of this kind, which become more exotic and eccentric as one proceeds down the chart.

 Fractions and Roman numerals (4 columns, 0x2153-

0x2184). A slight Eurocentric faux pas in Unicode: of all the numeration systems based on letters (the Greek, the Hebrew, the Arabic, etc.), only Roman numerals are provided in Unicode.

 All kinds of arrows (7 columns, 0x2190-0x21FF), point-

ing in every direction.

[ ∀∁∂∃∄/0Δ∇∈] Mathematical symbols (16 columns, 0x2200-0x22FF).

 Technical symbols (16 columns, 0x2300-0x23E7), which

is a catchall for the symbols of numerous disciplines: drafting, industrial design, keys on the keyboard, chemistry, the APL programming language, electrical engineering, dentistry, etc.

 Some graphic pictures for control codes, the space, the car-

riage return, etc. (4 columns, 0x2400-0x2426).

 Characters specially designed for the optical recognition of

check numbers, etc. (2 columns, 0x2440-0x244A).

 Letters and numbers in circles, in parentheses, fol-

lowed by a period, etc. (10 columns, 0x2460-0x24FF).

 The graphical elements inherited from the DOS code

pages (10 columns, 0x2500-0x259F).

 All kinds of geometric shapes: squares, circles, triangles,

diamonds, etc. (6 columns, 0x25A0-0x25FF).

 A hodgepodge of miscellanous symbols (16 columns,

0x2600-0x26B2): weather symbols, astrological symbols, telephones, cups of coffee, fleurons, the skull and crossbones, the sign for radioactive material, various religious symbols, symbols for various political ideologies, the peace sign and the yin–yang sign, the trigrams of the Yijing, some smilies, the planets, the constellations, chess symbols, playing-card symbols, some musical notes, the symbols for different types of recyclable materials, the faces of dice, the sign for high voltage, etc.

 In honor of a great typeface designer who shall re-

main nameless, this block contains the glyphs from the font Zapf Dingbats, made into Unicode characters (12 columns, 0x2701-0x27BE).

—— Some more mathematical and technical symbols (4 columns, 0x27C0-0x27FF).

 The 256 braille patterns (16 columns, 0x2800-0x28FF).

—— More arrows (8 columns, 0x2900-0x297F).

—— And still more mathematical symbols, each rarer and more eccentric than the one

before it (25 columns, 0x2980-0x2B23).

[  ÀÃÕŒœ–—“” ] Before moving to the Far East, a bit of history: Glagolitic

(6 columns, 0x2C00-0x2C5E), was used in Russia and probably invented by Saint Cyril in ad 862 for the translation of the Scriptures into Old Church Slavonic. It was later replaced by the Cyrillic script, but the order and the names of the letters were retained.

—— And, as if weird versions of Latin letters never end, another small supplement

called Latin Extended-C (2 columns, 0x2C60-0x2C77).

[ ‘’÷◊ÿŸ⁄€‹› ] Coptic, which is finally completely disunified from Greek

(8 columns, 0x2C80-0x2CFF).

80 Chapter 2 : Characters, glyphs, bytes: An introduction to Unicode

 Followed by Nuskhuri (3 columns, 0x2D00-0x2D25), the

lower-case version of the Georgian liturgical khutshuri letters, the upper-case ones being included in the Georgian block. This block corrects Unicode’s mistake of mixing the modern Georgian alphabet with the ancient liturgical alphabet.

 Tifinagh (5 columns, 0x2D30-0x2D6F), the writing system

of the Berbers, still widely used in Algeria in the province of Tizi-Ouzou and also taught in the public schools of Morocco.

—— A supplement to the Amharic script: 6 columns, 0x2D80-0x2DDE.

—— And, to prove the fact that any block can be supplemented, a supplement to...

punctuation: 8 columns, 0x2E00-0x2E1D.

 Now we have reached another turning point in

the BMP: this is where the scripts of the Far East begin. The ideographs can be described by their radicals, which are encoded here in the first two blocks. But there are two ways to represent the radicals: in isolation, or in the form that they assume when they are combined with other radicals. The first block (8 columns, 0x2E80-0x2EF3) contains radicals represented according to the latter approach.

 The next block (14 columns, 0x2F00-0x2FD5) con-

tains all of the ideographic radicals as they are represented in isolation.

—— The ideographic description characters (1 column, 0x2FF0-0x2FFB) are characters

whose purpose is to suggest ways to form new ideographs from existing Unicode ideographic characters. It is as if we were to take the glyphs of two or three of the characters in the preceding blocks and combine them to form the glyph of a character not available in Unicode. This is one way to obtain millions of new ideographs, but its direct implementation in software would likely yield rather poor results, as ideographs are seldom just simple graphical combinations of other ideographs. We shall discuss the creation of new ideographs on page 153.

[ ùûü†°¢£§•¶ ] Now we have come to ideographic punctuation and

ideographic symbols (4 columns, 0x3000-0x303F). We also find here the ideographic space, quotation marks, different types of brackets, the Japanese postal symbol, etc. A rather special character is 0x303E ideographic variation indicator, which indicates that the following ideograph is not exactly what is intended and that it should be construed as one of its variant forms (cf. p. 150).

[ ß®©™´¨≠ÆØ∞] Hiragana (6 columns, 0x3041-0x309F), a Japanese

syllabary. Two hiragana used before World War II are also listed here.

[ ±≤≥¥μ∂∑∏π∫] Katakana (6 columns, 0x30A0-0x30FF), another

Japanese syllabary, used for foreign words. Two katakana used before World War II and a number of dialectal signs also appear in this block.

[ ªºΩæø¿¡¬√ƒ ] Bopomofo (3 columns, 0x3105-0x312C) is an at-

tempt at an alphabetic script for Chinese that is used to represent ideographs phonetically. The influence of the Japanese kana is obvious.

—— Next is a “compatibility” block, i.e., a table of useless characters added only for the

sake of compatibility with an existing encoding. This particular block contains the basic elements Korean syllabic hangul script (6 columns, 0x3131-0x318E). Whereas the basic elements of block 0x1100-0x11F9 combine to form syllables, those in this block do not (see p. 155 for more explanation).

[ ≈Δ«»… ÀÃÕŒ ] A small block of ideographs written as superscripts, the

kanbun (1 column, 0x3190-0x319F). These characters are very interesting because they show how the cultures of East Asia are connected through the ideographic writing system. A Chinese poem is automatically a poem in Japanese as well, with one difference: the order of the ideographs may not be correct. The kanbun serve to indicate a reading order appropriate to the Japanese reader to understand the poem.

—— A supplementary set of phonetic bopomofo, CJK strokes and katakana (4 columns,

0x31A0-0x31FF).

[ œ–—“”‘’÷◊ÿ ] Next comes a block of encircled ideographs, of

katakana and hangul in circles or parentheses, of numbers (either Chinese or Arabic) in circles or parentheses, and of symbols for months (16 columns, 0x3200-0x32FE).

[ ’÷◊ÿŸ⁄€‹›fi] And a block of ideographic abbreviations (16 col-

umns, 0x3300-0x33FF). These are groups of 4 to 6 katakana within an ideographic square or Latin abbreviations for such things as units of measure, also within that type of square.

—— After the abbreviations, we step right into the vast pool of ideographic characters.

Before starting on the basic characters, we have the CJK Unified Ideographs Extension A: 432 columns, 0x3400-0x4DB5 (6,582 ideographs).

[ „‰ÂÊÁËÈÍÎÏ ] A short interlude before the big section of ideo-

graphic characters: the hexagrams from the Yijing (4 columns, 0x4DC0-0x4DFF), a Chinese book of divination. [ ÌÓÔÒÚÛÙıˆ ] Then come the unified ideographs: 1306 col-

umns, 0x4E00-0x9FBB (20,924 ideographs).

 After the ideographs and before the hangul syllables come the

syllables of Yi, a writing system from southern China. Yi, a rather young writing system (only five centuries old), is in fact ideographic. There are between 8 and 10 thousand Yi ideographs, but they are not yet encoded in Unicode. On the other hand, a syllabary was invented in the 1970s to facilitate the learning of this language, and it is this syllabary that Unicode includes (84 columns, 0xA000-0xA4C6).

82 Chapter 2 : Characters, glyphs, bytes: An introduction to Unicode

—— A block with modifier tone marks for Chinese: 2 columns, 0xA700-0xA71A.

—— Did you think that there were enough Latin letters in this encoding? Well, the Uni-

code Consortium did not agree with you. Here comes another supplemental block for Latin letters, called “Latin Extended-D”. For the moment it contains only two characters (0xA720 and 0xA721), but there is room for many more, since 14 columns have been reserved for this block.

[ ËÈÍÎÏÌÓÔÒ ] Another previously forgotten script: Syloti Nagri (3 columns,

0xA800-0xA82B), the alphabet of the Sylheti language, spoken by ten million Indians in Bangladesh. The script, which closely resembles that of Bengali, dates from the fourteenth century, and works written in it were still being printed up to the 1970s.

[ fifl‡·‚„‰ÂÊÁ ] Another relic of history: Phags-pa (4 columns,

0xA840-0xA877), invented by a Tibetan lama in 1269 under commission from Mongolian leader Khubilai Khan to serve as the new Mongolian alphabet. The most recent text in this script is from 1352.

 Next comes the list of the most common hangul

syllables: 698 columns, 0xAC00-0xD7A3 (11,172 syllabes).

—— Zones 0xD800-0xDBFF and 0xDC00-0xDFFF are used to encode the characters be-

yond the BMP in UTF-16. These two zones are called the high-half and low-half surrogate zones.

—— Between 0xE000 and 0xF8FF is the private use area, where we are free to place any

characters that we wish.

—— Then follows a block of compatibility ideographs (included twice in a Korean encod-

ing, in Big-5, in an IBM encoding, and in JIS X 0213) (32 columns, 0xF900-0xFAD9).

—— From 0xFB00 to 0xFDFD and from 0xFE70 to 0xFEFF are characters called presentation

forms. These are glyphs that have, for one or another reason, been given the status of characters. More precisely, these characters include a handful of Latin ligatures (including the “f-ligatures”), five Armenian ligatures, some widened Hebrew letters (to facilitate justification), some Hebrew letters with vowel points and Yiddish letters with vowels, one Hebrew ligature, the contextual forms of the Arabic letters, and a large number of æsthetic Arabic ligatures. There is even a single character ‘…’ for the phrase “In the name of Allah, the Beneficent, the Merciful” (actually made of ** characters), which appears at the beginning of every sura in the Koran. The Unicode Consortium discourages the use of these presentation forms.

—— A small block (1 column, 0xFE00-0xFE0F) contains control characters that indicate

a glyphic variant of the preceding character. There are 16 characters of this kind; thus 16 different variants of the same glyph can be used in a single document. Another 240 characters of the same kind are found in Plane 14.

—— A one-column block with variants of Latin and CJK punctuation for vertical type-

setting: 0xFE10-0xFE19.

—— The two halves of a horizontal parenthesis and a horizontal tilde (1 column,

0xFE20-0xFE23).

—— Various ideographic punctuation marks whose glyphs are adapted for vertical type-

setting (2 columns, 0xFE30-0xFE4F).

—— Smaller glyphs for certain ideographic punctuation marks (1 column, 0xFE50-

0xFE6B).

—— Code point 0xFEFF is the byte order mark (BOM), a character that we are free to

place at the beginning of a document. It makes it possible to determine whether the file was saved in little-endian or big-endian format. The system works because the inverse of this character (code point OxFFFE) is not a Unicode character.

[ 456789:;<=, >?@ABCDEFG ] To wrap up the BMP with a

flourish, this block contains full-width ASCII characters (the size of ideographs) as well as half-width katakana and hangul elements (15 columns, 0xFF01-0xFFEE).

—— Finally, in the last block of the BMP, we have special characters: first, three char-

acters for interlinear annotations, a means of presentation of which one possible interpretation involves adding small characters above the characters of the main text, which could be used for a translation into another language or to indicate the pronunciation of the main text. They are very frequently used in Japan, where the kanji ideographs are annotated with kana so that they can be read by schoolchildren and teenagers who do not yet have a sufficient command of the ideographs. If A is the annotation of T, then Unicode offers a character 0xFFF9 to place before T, a character 0xFFFA to place between T and A, and a character 0xFFFB to place after A.

Another special character, 0xFFFC object replacement character, is used as a placeholder for an unspecified object.

Last of all, the final character of the BMP, 0xFFFD replacement character, is the recommended character for representing a character that does not exist in Unicode during conversion from an encoding not recognized by the Consortium.

Code points 0xFFFE and 0xFFFF do not contain Unicode characters.

Now that we have finished the BMP, which is worthy of Jules Verne’s Around the World in Eighty Days, let us continue with Unicode’s other planes, which are not yet heavily populated, at least for the time being.

Plane 1 is called the SMP (Supplementary Multilingual Plane). It consists of historic or unusual scripts:

84 Chapter 2 : Characters, glyphs, bytes: An introduction to Unicode

x0 x1 x2 x3 x4 x5 x6 x7 x8 x9 xA xB xC xD xE xF



       

10x

11x

. /

12x

  	 



1Dx

1Ex

Figure 2-4: The roadmap of Unicode’s Supplementary Multilingual Plane:  Linear B,  Aegean and ancient Greek numbers,  Old Italic and Gothic,  Ugaritic and Persian cuneiform,  Deseret,  Shavian,  Osmanya,  the Cypriot syllabary,  Phœnician,  Kharoshthi, . cuneiform, / cuneiform numbers and punctuation,  Byzantine musical notation,  Western musical notation, 	 ancient Greek musical notation,  monograms, digrams, and tetragrams of the Yijing,  counting rod numerals,  Latin, Fraktur, and Greek letters used in mathematical formulae.

::: tip Supplementary Roadmap: SMP, SIP, and SSP (Figures 2-4, 2-5, 2-6)
![Figure 2-4: The SMP roadmap](/images/fonts-encodings/fig2-4-smp-roadmap.png)
*Figure 2-4: The Supplementary Multilingual Plane (SMP, Plane 1) roadmap.*

![Figure 2-5: The SIP roadmap](/images/fonts-encodings/fig2-5-sip-roadmap.png)
*Figure 2-5: The Supplementary Ideographic Plane (SIP, Plane 2) roadmap.*

![Figure 2-6: The SSP roadmap](/images/fonts-encodings/fig2-6-ssp-roadmap.png)
*Figure 2-6: The Supplementary Special-Purpose Plane (SSP, Plane 14) roadmap.*
:::



x0 x1 x2 x3 x4 x5 x6 x7 x8 x9 xA xB xC xD xE xF

20x

CJK Unified Ideographs Extension B

21x

2Ax

2Bx



2Fx

Figure 2-5: The roadmap of Unicode’s Supplementary Ideographic Plane (SIP):  supplementary compatibility ideographs.

x0 x1 x2 x3 x4 x5 x6 x7 x8 x9 xA xB xC xD xE xF

À

E0x

E1x

Á

E2x

Figure 2-6: The roadmap of Unicode’s Supplementary Special-Purpose Plane (SSP):  language tags,  supplementary variation selectors.

 Linear B (16 columns, 0x10000-0x100FA), a Cretan writing sys-

::: tip Authentic Typographical Specimen: Ancient Scripts of the SMP (Plate 2-4)
![Plate 2-4: Supplementary Multilingual Plane Ancient Scripts](/images/fonts-encodings/plate2-4-supplementary-ancient-scripts.png)
*Plate 2-4: Authentic specimens of Cretan Linear B, Aegean numbers, Old Italic (Etruscan), Gothic, Ugaritic, and Old Persian cuneiform (p. 86).*
:::



tem from the time of King Minos and his labyrinth for containing the Minotaur (2000 bc), which was deciphered by architect and amateur archæologist Michael Ventris in 1952. It is called “B” because there is a script known as “Linear A” that has not yet been deciphered. Linear A is not yet encoded in Unicode, doubtless because the Consortium is waiting for its decipherment so that sensible descriptions can be given to the signs.

 The Aegean numbers (4 columns, 0x10100-0x1013F) are sym-

bols derived from Linear A and identified as being numbers or units of measure. [  ÀÃÕŒœ–—“” ] They are followed by the Greek numbers (5 columns, 0x10140-

0x1018A), which have been used over the centuries in quite a few systems of numeration. The numbers in the first two columns are called acrophonic because they are the first letters (akron = ‘tip’) of the names of the numbers. For example, ‘Õ’ = pi is the first letter of π0ντε = ‘five’.  The Old Italic block (3 columns, 0x10300-0x10323) contains the let-

ters used by a certain number of ancient languages of the Italian peninsula, such as Etruscan, Oscan, Umbrian, etc. We can clearly discern the influence of Greek, but the nascent Latin alphabet is also recognizable.

 Gothic5 (2 columns, 0x10330-0x1034A) is the writing system of

the Goths, Vandals, Burgundians, and Lombards used by the archbishop Wulfila in his Bible in ad 350. It greatly resembles the uncial script but also contains a number of Greek letters: psi, lambda, pi, theta, etc.

 Ugaritic (2 columns, 0x10380-0x1039F) is one of the lan-

guages written in cuneiform. The cuneiform characters that it uses are letters of an alphabet. Incidentally, their names seem familiar to us: alpa, beta, gamla, delta, etc.

[ ÚÛÙıˆ˜¯˘˙˚ ] They are followed directly by another cuneiform

writing system, Old Persian (4 columns, 0x103A0-0x103D5). The cuneiform scripts of Akkadian and Elamite have yet to be encoded in Unicode.  The following two blocks are controversial: they contain two

artificial alphabets from the nineteenth century and the beginning of the twentieth century. The first is Deseret (5 columns, 0x10400-0x1044F), or the “Mormon alphabet”, which was used for English-language texts (altogether four books and one tombstone!) between 1847 and 1869 and can be regarded as an attempt to isolate

::: tip Authentic Typographical Specimen: Constructed & Mediterranean Scripts (Plate 2-5)
![Plate 2-5: Deseret, Shavian, Osmanya, Cypriot, Kharoshthi](/images/fonts-encodings/plate2-5-deseret-shavian-cypriot.png)
*Plate 2-5: Authentic specimens of the Mormon Deseret alphabet, George Bernard Shaw's Shavian alphabet, Somali Osmanya, Cypriot syllabary, and Gandharan Kharoshthi (p. 87).*
:::



5 There seem to be multiple uses of the term “Gothic” in various languages. In US English it is used for the script of Wulfila, but also, more commonly, for sans-serif fonts. In French, Wulfila’s script is called “gotique” (without the ‘h’), and “gothique” is used for German broken scripts. Germans call the latter “German scripts” (“Deutsche Schrift”). The result of this linguistic imbroglio is that in the well-known comics “Asterix and the Goths”, the words spoken by the Goths are written in a ... broken script, which allows the author, Réné Goscinny, to compare the Goths with the pre-WWI Germans.

86 Chapter 2 : Characters, glyphs, bytes: An introduction to Unicode

the Mormons culturally from the rest of the United States. Let us hope that other religions will not create their own new scripts, lest Unicode end up full of useless, unwanted alphabets.  The next alphabet, the Shavian alphabet (3 columns, 0x10450-

0x1047F), contains an element of humor that is certainly due to the person responsible for its development, the great British humorist George Bernard Shaw (whence “Shavian”, the adjectival form of “Shaw”). In his will, he provided for a contest to be held for the design of a new alphabet adapted to the phonetics of English. He died in 1950, the contest was held in 1958, and the alphabet encoded in Unicode was the winner. The letters have funny names: ha-ha, church, thigh, gag, peep, etc.  Osmanya (3 columns, 0x10480-0x104A9) was invented in 1922

by a certain Cismaan Yuusuf Keenadiid, a high-ranking figure in Somalia. It was destined to become the country’s official script, but in 1969 a coup d’état decided otherwise. Although letters look nothing like those of Arabic, their names (alif, ba, ta, dja, ... ) betray Arabian cultural influence. [ òôöõúùûü†° ] We return to ancient times with the Cypriot syllabary

(4 columns, 0x10800-0x1083F), a script influenced by Linear B and used on the native island of the goddess Venus between 800 and 200 bc.  Phœnician (2 columns, 0x10900-0x1091F) is the ancestor of

the Greek alphabet and those of the Semitic languages. It was used between the 20th

and the 2nd centuries bce. [ fifl‡·‚„‰ÂÊÁ ] Let us now leave the Mediterranean and take a trip to the Far

East with Kharoshthi (6 columns, 0x10A00-0x10A58), a historical writing system of northeastern India. Just like the Brahmi script, it has been used to write the Sanskrit language.

 One of the big novelties of Unicode v. 5 is the beautiful cuneiform script. It occupies no fewer than 64 columns (positions 0x12000-0x1236E), and another 8 columns (0x12400- 0x12473) for numbers and punctuation. Some of the glyphs are quite complex. [ ¢£§•¶ß®©™´ ] After the big cuneiform block, we find two blocks

devoted to music. We begin with the notational system used for Byzantine music6

6 This block demonstrates that Unicode’s inviolable principle of not changing a character’s description once the character has been adopted leads to the most ridiculous results. The English description of the character 0x1D0C5 contains the word fhtora, which is obviously a typo (the correct term, fthora from the Greek φθορ!, appears in the names of many of the neighboring characters). [Fortunately, the French translation corrected this error. Thanks, Patrick!] Rather than correcting this innocent typo, Unicode decided to add the following hilarious comment after the character’s description: “misspelling of ‘fhtora’ in character name is a known defect”.. . . The author knows of one other case of this sort of behavior: errors in the Hebrew Bible are also preserved, to the point that today there is a list of broken letters, upside-down letters, etc., that have been “institutionalized” to prevent the copyist from “correcting” the sacred text. Will Unicode be the new Bible?

(16 columns, 0x1D000-0x1D0F5), a system still widely used in Greece and in other Eastern Orthodox countries.

[ ¨≠ÆØ∞±≤≥¥μ ] The next block is for the Western system of musical notation

(16 columns, 0x1D100-0x1D1DD, which includes both the modern notation (written on the five-line staff) and the notation used for Gregorian chant (written on the four-line staff). Everything is present: notes, clefs, measure lines, dynamics, ties and slurs, crescendo and decrescendo hairpins, glissandi, fermatas, etc. All that we need is the creativity of Stockhausen, Berio, Crumb, and Boulez of the twenty-first century to make this block explode with a profusion of new symbols. [ ‘’÷◊ÿŸ⁄€‹› ] And since we are right in the midst of all this musical nota-

tion, why not encode the symbols used to notate music in antiquity? No sooner said than done: here is the block for ancient Greek musical notation (6 columns, 0x1D200- 0x1D245). [ ∂∑∏π∫ªºΩæø ] We have already mentioned the block of Yijing hexa-

grams, which is located on the BMP, squeezed between two blocks of ideographs. Here we have monograms, digrams, and tetragrams from this book (6 columns, 0x1D300-0x1D356).  Next comes a small block for counting rods (2

columns, 0x1D360-Ox1D371). “Counting rods” are small sticks, several centimeters long, used in East Asia for counting. These characters contain the basic patterns of this numbering system.  Finally, a block that was also controversial but that is more likely

to be useful to the reader than many other Unicode blocks: the mathematical alphanumeric symbols (48 columns, 0x1D400-0x0x1D7FF). The idea behind these is very simple. It is well known that “mathematicians are like Frenchmen: whenever you say something to them, they translate it into their own language, and at once it is something entirely different” (in the words of Goethe). Well, in this case it is the notion of a Unicode character that has been “translated”: the bold, italic, and bold italic forms of a letter are regarded here as distinct Unicode characters because they take on different meanings in mathematical formulae. Thus this block contains the styles mentioned above and also script, blackletter, blackboard-bold, sans-serif, and typewriter type—all of it for both Latin and Greek.

Plane 2 is called the “Supplementary Ideographic Plane” (SIP). Its structure is extremely simple. Between 0x20000 and 0x2A6D6 there is a contiguous block of 42,711 ideographs called “Ideographs Extension B”. The ideographic character with the greatest number of strokes is found there: it is 0x2A6A5 À, which is written with 64 (!) strokes. Its structure is quite simple: it contains four copies of the radical   ‘dragon’. As for the meaning of À, the reader will have guessed it: ‘four dragons’ (or ‘several dragons’). Perhaps the ease with which today’s font-design software can be used will soon give rise to characters with n2 dragons, for a total of 24n2 strokes....

88 Chapter 2 : Characters, glyphs, bytes: An introduction to Unicode

At the end of the plane, there is a relatively small block (34 columns, 0x2F800-0x2FA1D) of compatibility ideographs, all of them from the encoding CNS 11643-1992.

Unicode’s last “inhabited” plane is Plane 14. Here we find two blocks, the first of which was highly controversial. It is a set of language tags. The idea is as follows: to indicate the language of a block of text, we ordinarily use “high-level protocols” (otherwise known as markup systems) such as XML, which provides the attribute xml:lang for this purpose. But suppose that we absolutely insist on doing it at the level of Unicode. It would be both naïve and futile to try to define control characters corresponding to the various languages of the world: there would be far too many, and we would need a sub-Consortium to manage them all. Unicode’s idea, therefore, was as follows: on the basis of XML’s syntax, we will write the value of the xml:lang attribute using special characters that cannot possibly be mistaken for characters in running text. Thus Plane 14 contains a carbon copy of ASCII (8 columns, 0xE0001-0xE007F) whose characters fulfill this rôle.

According to the XML standard, the value of xml:lang is a combination of abbreviations of the name of a language (ISO 639 standard [191]) and the name of a country (ISO 3166 standard [190]), the latter being unnecessary if the name of the language is precise enough. The code for English is en, and this is what we would write in a document to indicate that it is in English: 0xE0001 language tag, 0xE0065 tag latin small letter e, 0xE006E tag latin small letter n. If we use letters in boxes for the tags (and Ä for 0xE0001, which marks the beginning of a sequence), the immortal verses of Goethe and their translations into various languages would look somewhat like this:

ÄdeÜber allen Gipfeln ist Ruh. In allen Wipfeln spürest Du kaum einen Hauch. ÄelΕπ2 π!ντων τ4ν 5ρ0ων 6συχα βασιλε9ει. Επ2 τ4ν κλαδσκων πλ0ον ο;τε φ9λλον δ<ν σαλε9ει. ÄfrAu dessus de tous les sommets est le repos. Écoute dans toutes les cimes, à peine si tu surprends un souffle. Äen Hush’d on the hill is the breeze. Scarce by the zephyr the trees softly are press’d.

The purpose of Ä is to indicate the version of markup. It is quite possible to envision a different use of the same tags, with a character other than 0xE0001 to mark the beginning of the sequence.

As we shall see when we discuss the bidirectional algorithm, it is important to make a logical distinction between sequential and embedded blocks of text when marking up a multilingual document. Ordinarily the sentences that we write are sequential, but when we write “I am telling you: ‘It is time to do this’ ”, we embed one sentence in another. The distinction is crucial when the sentences that we embed are written in scripts that read in opposite directions. Markup must therefore express this property of text, and XML lends itself admirably to this task because sequential blocks are “sibling nodes”, whereas embedded blocks are new branches of the tree. Unlike XML’s markup, Unicode’s language tags are unable to “structure” a document.

The Unicode Consortium admits that it committed a blunder by adopting these characters. It now strongly encourages users not to use these characters, at least when another means of indicating the language is available....

The last block of the last inhabited plane is for variation selectors. In the BMP there are already 16 selectors of this type that enable us to indicate as many variants of a single character. In the event that more than 16 variants occur, have no fear: Plane 14 contains 240 more (15 columns, 0xE0100-0xE01EF), bringing the total to 256.

When going from the BMP to the higher planes, we have the impression of moving from the overpopulated Gangetic Plain to the empty steppes of Siberia. The vast majority of these planes’ code points are still unassigned, and, unless in the near future we come upon an extraterrestrial civilization with a writing system that uses a million characters, that situation is likely to persist for some time.

Which scripts are planned for addition to Unicode in the near future?

There are at least three stages for a script to be included in Unicode. In the following we describe the pipeline of scripts submitted for inclusion, as of August 2006.

Approved proposals in balloting

These scripts have been approved by the Unicode Technical Committee and the WG2. They are in the process of being approved by ISO for inclusion in 10646.

 Kayah Li, used to write Eastern and Western Kayah Li lan-

guages, spoken by about half a million people in Myanmar and Thailand.

 Lepcha is the script of Sikkim, a formerly independent

country that since 1975 has been a state of India, located between Nepal and Bhutan.

 Ol Chiki, invented by Pandit Raghunath Murmu in the first half

of the 20th century to write the southern dialect of Santali, a language of India, as spoken in the Orissan Mayurbhañi district.

 Vai, an African script used in Liberia and Sierra Leone.

 Rejang, the script of the language by the same name, spoken by

about 200,000 people in Indonesia, on the island of Sumatra.

 Sauvashtra, the script of an Indian language related to Gu-

jarati and spoken by about 300,000 people in southern India (actually a IndoEuropean language in the midst of several Dravidian languages).

 Sundanese, one of the scripts of the language Sundanese,

spoken by about 27 million people on the island of Java in Indonesia.

[ ‘’÷◊ÿŸ⁄€‹› ] Carian, as well as

 Lycian, and

90 Chapter 2 : Characters, glyphs, bytes: An introduction to Unicode

 Lydian: the three ancient Greek “Anatolian” scripts, used in Asia

Minor until the 3rd century bce.

Proposals in early committee review

These scripts have complete formal proposals and are waiting for approval or rejection by the UTC.

 Avestan is a pre-Islamic Persian script invented to

record Zoroastrian texts in the 3d century ce.

[ fifl‡·‚„‰ÂÊÁ ] Batak.

—— Manipuri, a recently extinct script for writing the Meithei language of Manipur

State in India.

 Hieroglyphic Egyptian, whose (future) Unicode

block is based on the font of the Centre for Computer-Aided Egyptological Research in Utrecht, in the Netherlands. The proposal distributes the hieroglyphs over two blocks: the basic block (761 characters) and the extended block (4,548 characters that come primarily from the inscriptions in the temple of Edfu). To place hieroglyphs inside cartouches, one uses the control characters egyptian hieroglyphic begin cartouche, etc. [ òôöõúùûü†° ] Brahmi, the ancient pan-Indian script, ancestral to the scripts of

India and Southeast Asia. [ òôöõúùûü†° ] Manichaean, the script of the texts of Manichaeism, a re-

ligion founded by Mani (216–274 ce). The Manichaean script was inspired by the Syriac Estrangelo.

 Tengwar, a script invented by Tolkien for The Lord of the

Rings.

Proposals in the initial and exploratory stages [ ËÈÍÎÏÌÓÔÒ ] Chakma is the script of Chakmas, the largest eth-

nic group in Bangladesh. Nowadays the Chakma language is mostly written in the Bengali script.

 Cham, a Southeast Asian script used by minorities

in Cambodia and Vietnam, which bears a vague resemblance to Khmer.

 Javanese, another Southeast Asian script, an In-

donesian derivative of Brahmi.

—— Lanna. [ ¢£§•¶ß®©™´ ] Mandaic is another Semitic alphabet, derived from the Aramaic script.

It is used for Mandaic, the liturgical language of the Mandaean religion.

[ ÚÛÙıˆ˜¯˘˙˚ ] Newari.

 Old Hungarian, a runic script used in Hungary before the Latin al-

phabet was adopted. In Hungarian it is called rovásírás.

 Pahawh Hmong, a script revealed in 1959 to a messianic figure

among the Hmong people of Laos, Shong Lue Yang, by two supernatural messengers who appeared to him over a period of months.

[ ¨≠ÆØ∞±≤≥¥μ ] Samaritan is the script of the Samaritans, a Mesopotamian

people that migrated and settled down in Palestine circa 500 bce. It is also known as Old Hebrew, in contrast with the script we nowadays call Hebrew, which is of Aramaic origin.

 Siddham: this very beautiful script, a descendent of Brahmi,

is used by Shingon Buddhists in Japan to write mantras and sutras in Sanskrit. It was introduced to Japan by Kukai in 806 ce after he studied Sanskrit and Mantrayana Buddhism in China. In Japan it is known as 梵字(bonji).

 Sorang Sompeng, the script used to write the Sora language, spoken by

populations living between the Oriya- and Telugu-speaking peoples in India. It was devised by Mangei Gomango, son of the charismatic leader Malia Gomango.

—— Tai Lü, a script for writing various Tai dialects in northern Thailand, Yunnan, and

parts of Myanmar.

 Varang Kshiti, the script used to write the Ho language of In-

dia, devised by another charismatic leader, Lako Bodra.

 Viet Thai is a script for the Thai languages used by Thai people

in Vietnam.  Ahom is the script of an extinct Tai language spoken by the Ahom

people, who ruled the Brahmaputra Valley in the Indian state of Assam between the 13th and the 18th centuries.

—— Early Aramaic, an alphabet descending from Phœnician. It is an ancestor of Syriac,

Arabic, and other scripts.

—— Balti, the script of the language of Baltistan, in northern Kashmir. This script was

apparently introduced around the 15th century ce, when the people converted to Islam. It is related to Arabic.

92 Chapter 2 : Characters, glyphs, bytes: An introduction to Unicode

[ ∂∑∏π∫ªºΩæø ] Bassa Vah is a script used by the Bassa people on the central

coast of Liberia and Sierra Leone. In the 1900s, a chemist, Flo Darvin Lewis, discovered that descendants of slaves in Brazil and the West Indies were still using it. He then tried to revive this alphabet in Liberia.

 Blissymbolics is an ideographic writing system used primarily by

people with physical and cognitive handicaps. It was developed by Charles Bliss in the 1950s as a “universal language” that could cut across national boundaries and facilitate international communication and peace. It contains 2384 characters in 149 columns.  Cirth, another script invented by Tolkien for The Lord of the Rings.

[ ¿¡¬√ƒ≈Δ«»… ] Hittite is the language of the Hitties, a people living

in north-central Anatolia. It was spoken between 1600 and 1100 bc. It was written in cuneiform characters with syllabic and logographic meanings.

 The Indus Valley script is still undeciphered. It

was used between 2500 and 1700 bce. The proposal includes 386 characters.

—— Kaithi, a script used widely throughout northern India, primarily in the former

North-West Provinces (present-day Uttar Pradesh) and Bihar. It was used to write legal, administrative, and private records.

 Khamti, or Lik-Tai, used to write the Khamti language in

India and Myanmar.

—— The Kirat, or Limbu, script, used among the Limbu of Sikkim and Darjeeling (the

place with the delicious tea).

—— Linear-A, an undeciphered script—unlike Linear B, which was deciphered by

Michael Ventris—used in ancient Crete around 1400 bce.

 Meroitic is a very interesting case of the alternative use of

a writing system. The Meroites lived in the Sudan during the time of the pharaohs. To write their language, they used 23 Egyptian hieroglyphs (or demotic characters), each with a very precise phonetic value.

[  ÀÃÕŒœ–—“” ] Naxi-Geba: Geba is one of the three scripts of the Naxi

language (together with Dongba and the Latin alphabet). The language is spoken by about 300,000 people in Yunnan, Sichuan, Tibet, and Myanmar.

[ ¢£§•¶ß®©™´ ] Old Permic is the script invented by the missionary Étienne

de Perme in the 14th century to write the Komi and Permyak languages, which are spoken in the Ural Mountains in Russia.

—— Palmyrene.

[ ∂∑∏π∫ªºΩæø ] The Pollard script. Samuel Pollard was a British missionary who

lived in China at the beginning of the 20th century. He invented a writing system for the A-Hmao language of the Miao minority. His system is structurally related to hangul in that he defined basic elements that are combined to form syllables. The language is much more complex phonetically than Chinese.

 Rongorongo, the yet undeciphered symbols of Easter Is-

land, carved on wooden boards. It is written in reverse boustrophedon style (from bottom to top). There are two other scripts to write the Rapa Nui language: Ta’u and Mama.

[ ¨≠ÆØ∞±≤≥¥μ ] South Arabian is an ancient Semitic script, the ancestor of

Amharic. It was used from the 5th century bce to the 7th century ce.

[ ¿¡¬√ƒ≈Δ«»… ] Soyombo is another writing system for the Mongolian lan-

guage that was created in 1686 by the illustrious Mongolian monk Zanabazar. It can be used to write Mongolian as well as Tibetan and Sanskrit. One of the Soyombo letters became the national symbol of the Mongolian state in 1992; its proportions are even defined in the country’s constitution.

The Web site http://www.ethnologue.com gives a list of 6,800 languages of the world, but it is estimated that only about 100 scripts have existed. Unicode already includes about 60 scripts, and another 50 are waiting in the pipeline for inclusion. Does this mean that Unicode has managed to encompass most of the world’s scripts? One thing is certain: both the Consortium and the designers of “Unicode-compatible” fonts will have their hands full for some decades to come.