---
title: "Chapter 5: Using Unicode"
description: "Unabridged English text: Interactive character palette tools across Mac OS X, Windows, and Linux; keyboard layout tools (MSKLC, Keyman Developer)."
---

# Chapter 5: Using Unicode
**By Yannis Haralambous, Ph.D.**
*From Fonts & Encodings, pp. 159–188*

---

Using Unicode
Unicode is found everywhere that text occurs. It would be pointless to describe here all
the software that processes text in one or another of Unicode’s forms. Let us consider
instead the chain of data transmission: the author enters his data, which pass through
his CPU and through the network to reach the CPU of his reader/interlocutor. This computer displays the information or prints it out in a way that enables the person who
received the information to read it.
Let us take these steps one by one. First, there is data entry: how do we go about entering
Unicode data? Data can also be converted from other encodings. How do we convert data
to Unicode? Next, once the data is in the computer, we must display it. For that purpose
we use fonts that must themselves be Unicode-compatible. (We shall discuss fonts in the
entire second half of this book, Chapters 6 through 14 and Appendices A through F).
Once the data has been revised and corrected, it is transmitted over the network. We have
already mentioned MIME and the various encoding forms of Unicode in Chapter 2. At
this level, it matters not to HTTP, TCP/IP, and other protocols that the data is encoded
in Unicode rather than in some other encoding. Finally, the data reach the recipient.
There it must be displayed, and so adequate fonts must be available. The recipient of the
message replies, and the entire process begins all over again, in the opposite direction.
What we shall examine in this chapter are the three ways to obtain text in Unicode:
• Interactively, by selecting characters from a table.
• Through the use of a virtual keyboard.
• By converting data that exist in other encodings.

Figure 5-1: The Character Palette of Mac OS X. Interactive Tools for Entering Unicode Characters Under Mac OS X Character Palette On the menu of keyboards, denoted by a little flag corresponding to the system’s active language, we find the entry Show Character Palette. This entry will open a separate window, independent of all other software, that will remain in the foreground. In Figure 5-1 we have a screenshot of the Character Palette. When we select Code Tables in the little menu on the top, the middle section of the window is divided into two parts. On the top is a list of all the blocks in Unicode v.4. When a block is selected, the corresponding characters are displayed underneath. When the user selects a character, its glyph is displayed in the area which opens through the little triangle next to Character Info. Clicking on the button Insert will insert it into the current document in the active application (which is why the Character Palette does not affect the operation of the other windows in any way). Once we have selected a Unicode character, we can read its number and its description. In certain cases, the Character Palette gives us “related characters”, which are the various canonical equivalents and compatibility equivalents that may exist. The result is astounding: out of love for the fair sex, we have selected the character for the ideographic

::: tip Typographical Specimen Plate (Figure 5-1)
![Figure 5-1: The Mac OS X Character Palette](/images/fonts-encodings/fig5-1-mac-character-palette.png)
*Figure 5-1: The Mac OS X Character Palette.*
:::

![Figure 5-1: The Mac OS X Character Palette](/images/fonts-encodings/fig5-1-mac-character-palette.png)
*Figure 5-1: The Mac OS X Character Palette.*

```text
Interactive Tools for Entering Unicode Characters
radical “woman” 0x2F25 女. This radical has a compatibility equivalent with the actual
ideographic character 0x5973 女, which, in turn, has its own compatibility equivalent
with the characters “compatibility ideographs 0xF981” and “circled female” 0x329B ㊛
. Thus the Palette has followed this chain of compatibility equivalents to the very end
in order to produce a complete list for us. In addition, it also shows us the character
0x2640 female sign, which is the symbol for femininity, even though Unicode does not
provide any metadata connecting this character to the others.
By opening the Font Variation area one can see the glyphs of the selected character in
all fonts that contain it—a feature that is very useful for finding out which fonts contain
a specified character or block.
The Character Palette has been part of the Mac OS X operating system since version 10.2,
the version we show is from system 10.4.7.
UniDict
Here is a clever little program of the same type that is designed especially for Japanese
ideographic characters: UniDict [104], which unfortunately was released for Mac OS 8
but has never been upgraded for Mac OS X. It is a multipurpose dictionary, but what is
of interest to us here is the possibility of selecting an ideograph through a combination
of radicals. In Figure 5-2 we see UniDict’s Kanji Constructor window, with a series of buttons at the left that represent the radicals and the shapes that the radicals assume when
they are used in characters. When a button is pressed, all the characters that use it are
displayed at the right. When a second button is pressed, only the characters that contain
both radicals are displayed, and so forth. Double-clicking an ideograph opens another
window (Figure 5-2), which supplies a broad range of supplementary information. The
data that UniDict employs come primarily from the academic project for the Japanese–
English dictionary EDICT [90]; thus they are updated regularly.
Under Windows XP
Character Map
The Windows operating system offers an analogue to the Character Palette of Mac OS X.
It is the Character Map (Figure 5-3), and it can be run from the Start menu: All Programs>
Accessories>System Tools. This tool allows us to select a Unicode character from a table
(by scrolling with the scroll bar), copy it onto the clipboard, and then copy it from the
clipboard into a document.
BabelMap
BabelMap, by Andrew West [346], is a very sophisticated free software package for entering Unicode text with a mouse. The user chooses the Unicode block that contains the
characters that he wants, the buttons in the middle area of BabelMap display the characters in that block, and the user may click characters to enter them into the Edit Buffer
at the bottom of the window. While text is being composed in the Edit Buffer, BabelMap
applies the relevant contextual rules appropriately. Thus, as shown in Figure 5-4, Arabic
```

::: tip Typographical Specimen Plate (Figure 5-3)
![Figure 5-3: The Windows Character Map](/images/fonts-encodings/fig5-3-windows-character-map.png)
*Figure 5-3: The Windows Character Map.*
:::

::: tip Typographical Specimen Plate (Figure 5-4)
![Figure 5-4: BabelMap main window](/images/fonts-encodings/fig5-4-babelmap-main-window.png)
*Figure 5-4: BabelMap main window.*
:::

![Figure 5-4: BabelMap main window](/images/fonts-encodings/fig5-4-babelmap-main-window.png)
*Figure 5-4: BabelMap main window.*

![Figure 5-3: The Windows Character Map](/images/fonts-encodings/fig5-3-windows-character-map.png)
*Figure 5-3: The Windows Character Map.*

```text
Figure 5-2: The UniDict software under the Classic environment
is displayed correctly, the Indian ligatures (included in the font specified for display) are
correctly produced, the jamo are combined into hangul syllables, and so on.
We can search for a character by its name or by its code point. We can select a font for
display in a very sophisticated manner: a special window shows the Unicode blocks covered by the font and, conversely, the fonts that cover a specified block.
Like UniDict, BabelMap also provides a window for selecting ideographs. Its advantage:
it applies not only to Japanese ideographs but to the entire range of Unicode characters
(provided, as always, that a font containing the required glyphs is available1). Its disadvantage: the method is not so elegant as that of UniDict. In fact, as shown in Figure 5-5,
we select a radical from a complete list (only their standard forms are displayed; a cer1 The reader will find at http://www.alanwood.net/unicode/fontsbyrange.html a list of freely distributed Unicode-compatible fonts.
```

```text
Interactive Tools for Entering Unicode Characters
Figure 5-3: The Character Map of Windows XP.
tain amount of training is required to recognize a radical in a nonstandard form), then
we select the number of strokes needed to write the character, omitting the strokes in the
radical. The corresponding characters are displayed at the lower left. This method is close
to what one does to look up a character in an ideographic dictionary.
There is also a way to search for an ideograph by its pinyin representation (a Latin transcription of the ideographs used in the Chinese language). Finally, BabelMap also offers
a means of searching for Yi ideographs according to the radicals of this writing system;
see Figure 5-6.
Under X Window
gucharmap
gucharmap [237] is a program in the spirit of the Character Palette under Mac OS X
and BabelMap under Windows. It is a SourceForge project whose administrator is Noah
Levitt. It runs under X Window with GTK+ 2 or a later version. The project’s web site
bears the subtitle “resisting the worldwide hegemony of english!”, but the site itself is in English only. The software, however, is localizable, and translations into several
other languages exist.
As shown in Figure 5-7, the main window of gucharmap presents a list of the Unicode
blocks on the left and the contents of each block in tabular form on the right. When we
click on a glyph in the table, it is inserted into the Edit Buffer at the lower left. A second
tab provides information on the selected character that is drawn directly from the online
files of the Unicode Consortium.
```

::: tip Typographical Specimen Plate (Figure 5-7)
![Figure 5-7: Gucharmap on Linux](/images/fonts-encodings/fig5-7-gucharmap-linux.png)
*Figure 5-7: Gucharmap on Linux.*
:::

![Figure 5-7: Gucharmap on Linux](/images/fonts-encodings/fig5-7-gucharmap-linux.png)
*Figure 5-7: Gucharmap on Linux.*

```text
Figure 5-4: The main window of the program BabelMap.
Virtual Keyboards
The interactive tools of the previous section enable us to enter a handful of Unicode
characters, but we would hardly want to input a long document in this manner. People
were using keyboards to type up documents even before the advent of computer science,
and the keyboard will remain—until a direct connection between brain and computer
becomes a reality—the most natural means of carrying out this operation.
But keyboards are physical, or hard, objects. If we often write in English, Arabic, Hindi,
and Japanese, must we buy a keyboard for each of these languages and play a game
of musical keyboards every time we switch languages? Absolutely not. We can simply
change the virtual keyboard, which is the table of correspondences between (physical)
keys and the (virtual) characters that they generate.
Operating systems have offered such virtual keyboards from the beginning; they have
been part of the process of localization for each language. Thus a user of the English version of Mac OS X or Windows XP can switch to the Greek, Arabic, or Chinese keyboard
at any time.
But there are at least two problems. First, these virtual keyboards do not necessarily cover
all writing systems (although Windows provides a rich set of virtual keyboards); in par-
```

```text
Virtual Keyboards
Figure 5-5: The BabelMap for selecting a Chinese ideograph through the use of radicals.
ticular, they do not cover ancient languages. To be sure, we can always find a supplier
of rare virtual keyboards. But there is a second problem, of a more subtle nature: we
would like for the virtual keyboard to be adapted to our habits, with its keys arranged in
a certain way.
One example: suppose that an American user, who therefore is a QWERTY typist, wishes
to type a document in Russian. He has a basic idea of Russian phonetics; after all, it is not
necessary to study this language for years in order to learn that the Russian ‘A’ is like an
English ‘A’ (as in “father”), that the Russian ‘З’ is like the English ‘Z’, that the Russian ‘O’
is like the English ‘O’, and so on. Accordingly, he selects the Russian keyboard on his
Macintosh or Windows/Linux PC and expects to find the letters in the same locations.
But they are not there: the layout of the Russian keyboard is completely different. Instead
of an ‘A’ key, he will find a ‘Ф’; instead of a ‘Z’ key, a ‘Я’; and instead of an ‘O’, a ‘Ш’. That
is to be expected, since the keyboard layouts derive from typewriter keyboards; but we
might have preferred for the common letters, at a minimum, to be in the same locations.
Thus we have to learn everything from the beginning, with the constant risk of expecting
to find the Russian ‘A’ where the English ‘A’ would be and vice versa.
It can be even worse: for almost 20 years, the author has been using “Greeklish,” an
ASCII transliteration of Greek that is very useful for writing in Greek where the protocol
does not support the script (email on a non-Unicode machine, filenames, etc.). There
```

```text
Figure 5-6: The BabelMap window for selecting an Yi ideograph through the use of radicals.
is nothing unusual about that: transliteration is a habit for everyone who works in an
environment with a non-Latin script. In this Greek transliteration, which happens to be
that of TEX, alpha is ‘a’, beta is ‘b’, and so forth. Using this transliteration has become so
habitual for the author that he is thoroughly at a loss when faced with a “real” Greek
keyboard, i.e., a keyboard used in Greece. Moreover, aside from the layout of the letters,
the Greek keyboard is, like most other keyboards in the world, based on the QWERTY
layout; thus the digits appear on the lowercase position of the keys, the ‘A’ is on the home
row, etc. But the author, living in France, is an AZERTY2 typist. Can the reader imagine
the double difficulty of using a Greek virtual keyboard with the Greek letters arranged
as in QWERTY although the physical keyboard is AZERTY?
In all these cases, there is only one solution: generating one’s own virtual keyboards. In
this section, we shall discuss a handful of tools that enable us to do so in a simple and
efficient manner.
2 AZERTY is a keyboard layout used in France, Belgium, and certain francophone African countries (but
not in French-speaking Canada or Switzerland) that differs slightly from the keyboards of most other countries
in its arrangement of the basic letters of the Latin alphabet and also the 10 Arabic numerals. The top row of
keys contains some punctuation marks and a few accented letters; the digits have to be typed with the shift key.
Furthermore, the second row begins with ‘A’ and ‘Z’ rather than with ‘Q’ and ‘W’, which explains the name
“AZERTY” (the QWERTY, QWERTZ, and AZERTY keyboards have only 20 keys in common). Many other
small differences conspire to irritate those who travel and find themselves using various types of keyboards:
the letter ‘M’ is at the end of the home row; the brackets and braces—punctuation marks that programmers
frequently use—require combinations of keystrokes that can only be typed with both hands at a time (unless
one has the hands of Sergey Rachmaninoffor Clara Haskil); etc.
```

Virtual Keyboards
Figure 5-7: The main window of gucharmap under Linux
Useful Concepts Related to Virtual Keyboards
A keyboard contains four types of keys:
• Ordinary keys, for typing text and symbols (‘A’, ‘B’, etc.).
• Dead keys. For example, on a French keyboard, the circumflex accent and grave accent are dead keys. These keys are said to be dead because nothing happens at the very
moment when they are pressed. The key’s effect does not appear until another key, a
“live” one, is pressed. We can compare dead keys to Unicode’s combining characters,
except that a dead key comes before the base key and a combining character comes
after the base character.
A few scripts require multiple dead keys: for example, to obtain an ‘X’, we could use
the sequence of dead keys “smooth breathing”, “circumflex accent”, “iota subscript”,
followed by the ordinary key ‘ω’. Unfortunately, few systems for generating virtual
keyboards allow multiple dead keys.

• Function keys (F1, F2, etc.) and all other keys that do not lead to the insertion of a
character when pressed. (The space bar is not a function key, as it inserts a space,
although this character is invisible.)
• And modifier keys, which are keys pressed together with ordinary or dead keys and
that modify the mapping of those keys’ characters. On the Macintosh, the following modifier keys exist: shift, control, ° or command or apple, alt, function. On
a PC, there are also the shift, control, alt, and function keys, but there is no command
key. On the other hand, there are two keys that do not appear on the Macintosh: right
alt, or AltGr (at the right side of the keyboard), and the -, or windows, key.
The role of the virtual keyboard is, therefore, to map characters to combinations of keys
and modifiers, or perhaps to assign dead keys for them.
Under Mac OS X
Under Mac OS 9 we used ResEdit to create virtual keyboards, and those keyboards can
still be used under Mac OS X; we simply place them in:
• ~/Library/Keyboard Layouts to make them available to the current user only
• /Library/Keyboard Layouts to make them available to all local users
• /Network/Library/Keyboard Layouts to make them available to all users on the
network
But these virtual keyboards are based on the old WorldScript system, not on Unicode.
To obtain Unicode keyboards, we have to create them in a different way.
XML description of virtual keyboard
To produce Unicode keyboards, Mac OS X adopted a system that is simply brilliant: one
merely creates an XML file according to a certain Document Type Definition and places
it in the area in which the binary resources for virtual keyboards are stored (see below).
The system will compile this XML file into a binary resource the first time it is loaded.
But the most brilliant aspect is the fact that we use finite automata to define multiple
dead keys. Apple has already surprised us by using finite automata in the advanced typographic features of the AAT fonts (see Chapter 14, page 589 and following, and also
Appendix §D.13.1, where we give an introduction to the concept of finite automaton);
now this method is also applied to virtual keyboards.
But let us first describe the structure of a virtual-keyboard file, according to specification [57].
This file must have the extension .keylayout and must be placed in with the keyboard resources. It may have an icon, whose file must be present in the same directory, must be of
Macintosh format icns, and must have the same filename but with the extension .icns.
Like every self-respecting XML document, our virtual-keyboard file must begin with an
XML declaration and a reference to a DTD:

Virtual Keyboards
&lt;?xml version="1.0" encoding="UTF-"?&gt;
<!DOCTYPE keyboard SYSTEM
"file://localhost/System/Library/DTDs/KeyboardLayout.dtd">
The top-level element in the document is called keyboard. It takes four attributes:
• group is the number of the script, according to Apple’s earlier system. For Unicode
keyboards, it is always 126.
• id is the identification number of the virtual keyboard. It must be unique, but the
system takes care of that. There is only one constraint: we initially assign it a negative
value to indicate that we are defining a Unicode keyboard.
• name is the keyboard’s name as it will appear on the menu of keyboards. It is a UTF-8
string (if we have declared that the document is prepared in this natural form).
• maxout is the maximum number of Unicode characters that can be generated by a
single keystroke. For an ordinary keyboard it is 1, but sometimes a key will produce
multiple characters, as, for example, with the accented characters produced through
the use of combining characters, in which two characters are produced: the base character and the combining character.
Next come two mandatory elements: layouts and modifierMap. The contents of these
elements are very technical (the former is a code for the physical keyboard; the latter
identifies the various kinds of modifiers that we may use), and they are practically the
same for all virtual keyboards. We can therefore copy them from one file to another
without many qualms.
Here are the first two elements of a typical virtual keyboard, in their entirety:
&lt;keyboard group="126" id="-" name="Find the keycodes" maxout="4"&gt;
&lt;layouts&gt;
&lt;layout first="0" last="17"
modifiers="commonModifiers" mapSet="ANSI"/>
&lt;/layouts&gt;
&lt;modifierMap id="commonModifiers" defaultIndex="7"&gt;
&lt;keyMapSelect mapIndex="0"&gt;
&lt;modifier keys=""/&gt;
&lt;modifier keys="command anyShift? caps?"/&gt;
&lt;/keyMapSelect&gt;
&lt;keyMapSelect mapIndex="1"&gt;
&lt;modifier keys="anyShift caps?"/&gt;
&lt;/keyMapSelect&gt;
&lt;keyMapSelect mapIndex="2"&gt;
&lt;modifier keys="caps"/&gt;
&lt;/keyMapSelect&gt;
&lt;keyMapSelect mapIndex="3"&gt;

&lt;modifier keys="anyOption"/&gt;
&lt;/keyMapSelect&gt;
&lt;keyMapSelect mapIndex="4"&gt;
&lt;modifier keys="anyShift anyOption command? caps?"/&gt;
&lt;/keyMapSelect&gt;
&lt;keyMapSelect mapIndex="5"&gt;
&lt;modifier keys="anyOption caps"/&gt;
&lt;/keyMapSelect&gt;
&lt;keyMapSelect mapIndex="6"&gt;
&lt;modifier keys="command anyOption caps?"/&gt;
&lt;/keyMapSelect&gt;
&lt;keyMapSelect mapIndex="7"&gt;
&lt;modifier keys="control command? shift? caps? option?"/&gt;
&lt;modifier keys="control command? shift? caps?
option? rightShift"/>
&lt;modifier keys="control command? shift? caps?
option? rightOption"/>
&lt;/keyMapSelect&gt;
&lt;/modifierMap&gt;
A few words of explanation are in order. In layouts we define physical keyboards. Here
there is only one: ANSI.3 For each physical keyboard, we define virtual tables: keyMap
elements.
When no modifier key is used, the active table will be keyMap with index 0. The other
tables will be activated when we press one or more modifier keys.
The keyMapSelect elements describe the relationship between modifiers and activated
tables (because the same table can be activated by multiple combinations of different
modifiers). The keywords used are:
• shift: the left shift key
• rightShift: the right shift key
• anyshift: either of the shift keys
• option: the left option key
• rightOption: the right option key
• anyOption: either of the option keys
• control: the left control key
3 Just one little detail: in addition to ANSI, there are also the Japanese JIS keyboards. In any event,
there is at least one noncompiled keylayout file in each installation of Mac OS X, that of the Unicode hex input keyboard: /System/Library/KeyboardLayouts/Unicode.bundle/Contents/Resources/UnicodeHexInput.
keylayout. We can always start with the first two elements of this file.

Virtual Keyboards
• rightControl: the right control key
• anyControl: either of the control keys
• command: the ° key
• caps: the caps-lock key
The presence of any of these keywords in the value of the keys attribute indicates that
the corresponding key is pressed. The question mark indicates that it does not matter
whether the key is pressed or not.
Thus, according to the code shown above, virtual table 0 is activated in two cases: when
no modifier is being used, and (command anyShift? caps?) when the ° key is depressed.
In the latter case, the shift or caps-lock keys may also be depressed; they make no difference. Table 1 is activated when the shift key is depressed. (Pressing the caps-lock key
makes no difference.) Table 2 is activated when the caps-lock key is depressed and caps
lock is active. And so on. Thus we can describe in great detail the exact moment when
one or another table will be active.
Here is the remainder of the file, up to the end:
&lt;keyMapSet id="ANSI"&gt;
&lt;keyMap index="0"&gt;
<!-- No modifiers -->
&lt;key code="12" output="q" /&gt;
&lt;key code="13" output="w" /&gt;
&lt;key code="14" output="e" /&gt;
...
&lt;/keyMap&gt;
&lt;keyMap index="1"&gt;
<!-- anyShift -->
...
&lt;/keyMap&gt;
...
&lt;/keyMapSet&gt;
&lt;actions&gt;
...
&lt;/action&gt;
&lt;terminators&gt;
...
&lt;/terminator&gt;
&lt;/keyboard&gt;
There is a keyMapSet for each physical keyboard. In the example, there is only one. Next,
there is a keyMap for each virtual table; the index attribute furnishes its number.
Within the keyMap are key definitions. These are key elements, with three possible attributes:

• code takes the number of a key as its value. How can we know which number corresponds to a given key? That is a very good question that the specification carefully
avoids. Searching through Apple’s technical documentation also yields nothing, and
in any event there would be no guarantee that any tables that we did find would be
valid for a given machine and a given version of the operating system. The author,
however, has discovered a foolproof trick for finding the numbers of keys. All that
we have to do is to create a keyboard that generates as its output the number N for
key number N. The code is extremely simple:
&lt;keyboard group="126" id="-" name="Find the keycodes" maxout="4"&gt;
&lt;layouts&gt;
... as usual ...
&lt;/modifierMap&gt;
&lt;keyMapSet id="ANSI"&gt;
&lt;keyMap index="0"&gt;
<!-- No modifiers -->
&lt;key code="0" output="0 " /&gt;
&lt;key code="1" output="1 " /&gt;
&lt;key code="2" output="2 " /&gt;
...
&lt;key code="256" output="256 " /&gt;
&lt;/keyMap&gt;
&lt;/keyMapSet&gt;
&lt;/keyboard&gt;
That keyboard may also serve as a test of installation. We place this file in one of
the directories mentioned above and then close out the session. Later, we choose
Open International... on the keyboard menu, we click on Input Menu and then we
select this keyboard from the list that appears (it should be at the bottom of the list).
If the keyboard is not present, compilation must have failed. In that case, we open
the Console (a utility found in Applications>Utilities); it will certainly contain an
error message from the XML compilation.
Do not forget the spaces in the values of the output attribute, or the numbers produced will all be run together.
Using this keyboard, we can discover that, for example, the ‘e’ key has the number 14,
the carriage-return key is number 36, and the escape key is number 53, at least on the
author’s computer (a PowerBook G4 running the French version of Mac OS X 10.4.7,
with an AZERTY keyboard).
• output takes as its value the string of characters to be generated. As in every XML
document, we can write the code in UTF-8 or by using character entities of the type
&#x1234;. Be careful not to write more characters than the value of the maxout attribute of keyboard allows.
• Instead of writing a string of characters, we can specify an action by writing the action
attribute (instead of output), whose value is the name of an action.

Virtual Keyboards
The actions are described in the element actions. This element contains action subelements whose names (id attribute) are those used in the key elements.
What is an action? It is simply a series of when elements that will do different things according to context. The context is defined by a global variable, the “current state”, which
by default has the value none. According to the value of the current state, a different
when will be executed. The state can be changed by a when. Similarly, a when can produce
characters of output.
This element thus takes the following attributes:
• state: the state under which the when is executed. The value of this attribute may be
a string of characters or a whole number.
• next: the new current state following execution of the when.
• output: any Unicode characters to be produced.
There are two other attributes that we shall not describe: they are useful primarily for
hangul. They allow a when to be applied to more than one state and to calculate the value
of a character in the output according to the number of the state and the position of the
character entered.
Let us take a concrete example. We wish to make a dead key for the “circumflex accent”
and produce an ‘ê’ when this key is followed by an ‘e’. The numbers of these two keys
are 33 and 14, respectively. Thus we shall write the following in keyMapSet:
&lt;key code="33" action="circumflex" /&gt;
&lt;key code="14" action="e" /&gt;
and we shall define two new actions in actions:
&lt;action id="circumflex"&gt;
&lt;when state="none" next="circumflex"/&gt;
&lt;/action&gt;
&lt;action id="e"&gt;
&lt;when state="none" output="e"/&gt;
&lt;when state="circumflex" output="ê"/&gt;
&lt;/action&gt;
Thus, when we press the “circumflex” key, no character is produced, but we move into
the circumflex state. Next, when we press ‘e’, the when tests the value of the state and
produces an ‘ê’.
The default value of next is none, which means that we automatically return to the initial
state when no state is explicitly specified.
But what will happen if we change our minds after pressing the circumflex key and press
a key other than ‘e’? Nothing. The new character is produced, and no trace of the circumflex accent remains. That is one solution, but it is not the best. Ordinarily the system

```text
produces the circumflex accent (as an isolated character) and then the new character. To
achieve this sort of behavior, we have another subelement of keyboard, the terminators
element.
This element also contains when entries. But this time they cannot invoke new actions;
they can only generate strings of characters. These when are executed when the last key
pressed had no provision for the current state. In our example, we shall write:
&lt;terminators&gt;
&lt;when state="circumflex" output="^"/&gt;
&lt;/terminators&gt;
Thus if we followed the circumflex accent with something other than an ‘e’, we would
obtain the ASCII character for the circumflex accent.
We have covered the syntax of this method of describing a keyboard.
Here is one other example, this time with a triple dead key: the Vietnamese letter ‘,’.
To obtain it, we shall use the following characters in the order specified: the circumflex
accent, the acute accent, the dot. We shall take advantage of this approach to produce
the intermediate characters ‘ó’, ‘ô’, ‘’, ‘’, ‘×’, and ‘p’ as well. Here are the definitions of
the keys:
&lt;keyMap index="0"&gt;
<!-- no modifiers -->
&lt;key code="33" action="circumflex"/&gt;
&lt;key code="21" action="acute"/&gt;
&lt;key code="31" action="o"/&gt;
&lt;/keyMap&gt;
&lt;keyMap index="1"&gt;
<!-- shift -->
&lt;key code="43" action="dot"/&gt;
&lt;/keyMap&gt;
in which we have separated the “dot” from the other keys because, at least on an AZERTY
keyboard, it is typed with the shift key depressed.
Now we must define the following four actions:
&lt;action id="circumflex"&gt;
&lt;when state="none" next="c"/&gt;
&lt;/action&gt;
&lt;action id="acute"&gt;
&lt;when state="none" next="a"/&gt;
&lt;when state="c" next="ca"/&gt;
&lt;/action&gt;
&lt;action id="dot"&gt;
&lt;when state="none" next="d"/&gt;
&lt;when state="c" next="cd"/&gt;
```

```text
Virtual Keyboards
&lt;when state="ca" next="cad"/&gt;
&lt;when state="a" next="ad"/&gt;
&lt;/action&gt;
&lt;action id="o"&gt;
&lt;when state="none" output="o"/&gt;
&lt;when state="a" output="ó"/&gt;
&lt;when state="c" output="ô"/&gt;
&lt;when state="d" output="!"/&gt;
&lt;when state="ad" output="""/&gt;
&lt;when state="ca" output="#"/&gt;
&lt;when state="cd" output="−"/&gt;
&lt;when state="cad" output="\$"/&gt;
&lt;/action&gt;
We name states according to the keys already pressed: c (circumflex), a (acute), d (dot),
ad, ca, cd, cad. We accept sequences of keystrokes in only one fixed order: first a possible
circumflex, then a possible acute accent, and finally a possible dot. Thus the circumflex
action necessarily occurs in the initial state, whereas the acute action may occur in the
initial state or in state c, and so on.
Now all that remains is to add the terminators. There will be as many of them as there
are possible states (the initial state being excluded):
&lt;terminators&gt;
&lt;when state="a" output="'"/&gt;
&lt;when state="c" output="^"/&gt;
&lt;when state="d" output="."/&gt;
&lt;when state="ad" output="'."/&gt;
&lt;when state="ca" output="^'"/&gt;
&lt;when state="cd" output="^."/&gt;
&lt;when state="cad" output="^'."/&gt;
&lt;/terminators&gt;
Thus, if we have typed the circumflex, the acute, and the dot and then change our minds
and press something other than ‘o’, we will obtain the characters for all three keys.
Note that the example is realistic in all but one aspect: converting the apostrophe and
the period into dead keys may be disturbing to the user. And the period is often the last
character in a file. If it is on a dead key, it will not be entered into the file unless we type
another character after it—and we are not accustomed to “typing one extra character
so that the period will appear”. Thus we are well advised to choose other keys for the
“combining dot” and the “combining acute accent”.
Under Windows
Microsoft recently released a program for creating virtual keyboards, the Microsoft Keyboard Layout Creator (MSKLC). This software is certainly robust and easy to use, but
```

```text
Figure 5-8: The main window of the Microsoft Keyboard Layout Creator. The keyboard displayed is the one for “polytonic Greek”.
certain functionality, such as multiple dead keys, is missing. We shall describe it all the
same because it is free of charge and because some users may not need advanced functionality.
Microsoft Keyboard Layout Creator
MSKLC is a Microsoft product issued in 2002 that today is up to version 1.3. It is freely
distributed [268], but it works only on Win32 systems, namely Windows NT4, 2000, and
XP4. It allows the user to open existing keyboards or to create new ones from scratch, to
test the operation of a keyboard without installing it, and even to create a Windows installation package for distribution. This package allows other users who are not Windows
experts to install the new keyboard in a user-friendly fashion.
The easiest way to obtain a new virtual keyboard is often to open an existing keyboard
and modify it. In Figure 5-8 we see the main window of MSKLC. Dead keys are shown
in light gray; modifiers, in dark gray. Using the checkboxes at the left, we can activate or
deactivate the modifiers and see their different keyboard tables.
To associate a key with a Unicode character, we click on the key. A little dialog box opens,
with an area for entering text. We can type a Unicode character directly or use the hexadecimal notation \xXXXX or U+XXXX (or U+XXXXXX for characters outside the BMP). This
dialog box contains a button All that expands the dialog box to show the mappings of
the key when combined with modifiers (Shift, Control+Alt, Shift+Control+Alt). That is
4 Please be aware of the fact that this software needs .Net framework 1.1 to be installed (it will not work
with .Net version 2).
```

::: tip Typographical Specimen Plate (Figure 5-8)
![Figure 5-8: Microsoft Keyboard Layout Creator](/images/fonts-encodings/fig5-8-microsoft-keyboard-layout-creator.png)
*Figure 5-8: Microsoft Keyboard Layout Creator.*
:::

![Figure 5-8: Microsoft Keyboard Layout Creator](/images/fonts-encodings/fig5-8-microsoft-keyboard-layout-creator.png)
*Figure 5-8: Microsoft Keyboard Layout Creator.*

```text
Virtual Keyboards
Figure 5-9: The main window of Tavultesoft Keyman Developer, with the debugger and the
character map.
also how we convert a key into a dead key. A third little window provides us with a list
of the results of combinations of the current dead key with other characters.5
When we have finished defining a keyboard, we can test it in a miniature text editor
supplied under Project>Test Keyboard Layout. Then we can try to validate it (Project>
Validate Layout); the program will search for any errors and all the minor imperfections
of the keyboard. Finally, when we are happy with our work, we give the keyboard a
name, associate it with a language in the system (which will also determine the little
icon that will appear on the task bar), and create a Windows installer (of type MSI) using
Project>Build DLL and Setup Package. This installer can be distributed freely.
Tavultesoft Keyman Developer
Tavultesoft Keyman Developer dates from 1993. It was developed by Marc Durdin, whose
company, Tavulte, is based in Tasmania. This program adopts an approach totally different from that of MSKLC, with its own advantages and disadvantages.
5 Here we are indeed speaking of Unicode characters, not of keys. But before we can enter Unicode characters, we have to have defined keys that generate the characters in question; otherwise, the software would be
unable to make the (reverse) connection between characters and keys.
```

::: tip Typographical Specimen Plate (Figure 5-9)
![Figure 5-9: Tavultesoft Keyman Developer](/images/fonts-encodings/fig5-9-tavultesoft-keyman-developer.png)
*Figure 5-9: Tavultesoft Keyman Developer.*
:::

![Figure 5-9: Tavultesoft Keyman Developer](/images/fonts-encodings/fig5-9-tavultesoft-keyman-developer.png)
*Figure 5-9: Tavultesoft Keyman Developer.*

The virtual keyboard is created not through a user interface (that possibility does exist,
but the result is simplistic) but by a little program written by the programmer in an
ad hoc language. Once compiled, this program produces the virtual keyboard.
A keyboard produced with Keyman Developer cannot be used directly by Windows. It is
necessary first to install a runtime program called Keyman (nothing more). This program
is free for personal use and relatively inexpensive for professional use. With the runtime
program, we can manually select Keyman virtual keyboards or use them instead of Windows keyboards; all these possibilities can be configured in great detail.
In terms of architecture, Keyman comes after the Windows keyboard; we can also associate Keyman with a specific Windows keyboard. That approach keeps us from having to
start from scratch when we define a Keyman keyboard and also ensures that the Keyman
keyboard will be compatible with all hardware: the Keyman keyboard receives not key
numbers but Unicode characters as its input.
Owing to its relative independence from Windows, Keyman is capable of going much
further. To explore its functionality, we shall begin by describing the syntax of the source
code from which Keyman Developer compiles the virtual keyboard.
A Keyman code file is a text file with the extension .kmn. It has two parts: a header and
a body. The body of the file contains rules.
Here is the header of a typical KMN file:
c Some comments
c
VERSION 6.0
c The version of Keyman that is needed
c in order to use this file
NAME "Grolandese ***** keyboard"
BITMAP "groland.bmp"
store(&MnemonicLayout) "1"
begin Unicode > use(Main)
group(Main) using keys
A few words of explanation:
• The field BITMAP refers to the BMP file for the keyboard’s icon on the taskbar.
• The line store(&MnemonicLayout) "1" indicates that the code that follows should be
executed in “mnemonic” mode. That means that the keys are interpreted as characters and then processed by Keyman. If we omit this line, we proceed in “positional”
mode, as in other systems.
• The body of the document begins after begin Unicode. The instruction > use(Main)
indicates that the first “group” of rules is the one named Main.
• And the group Main begins with group(Main). The keywords using keys specify that
we shall use the current character. The absence of these keywords would mean that
this group of rules performed contextual analysis only. Later we shall see an example.

```text
Virtual Keyboards
As with Apple’s XML files, this header will usually remain the same; we can therefore
copy it from one file to another.
Now let us move on to the rules. We shall write one rule on each line. A rule consists
of a left-hand part (the input) and a right-hand part (the output), separated by a ‘>’. The
left-hand part consists of a context and a current character, separated by a ‘+’. The context
may be empty, in which case the line begins with the plus sign.
A rule with no context could be used to produce a euro sign every time we typed a dollar
sign:
+ '\$' > U+20AC
The character at the beginning of this rule indicates that there is no context and that
the rule will therefore always be applied. There are two ways to describe a character:
writing it in UTF-8 between single or double quotation marks, and writing its Unicode
code point.
A rule to cause the apostrophe followed by an ‘e’ to produce an ‘é’:
"'" + 'e' > "é"
Before delving more deeply into the syntax, let us see how to use Keyman’s interface to
write the program, compile it, and debug it. By opening Keyman and selecting File>New,
we are given the main window, which can be seen in Figure 5-9. We can write the header
by hand or let Keyman do it (Keyboard>Insert standard header).
We write our two rules under the line group(Main)..., and we save the file under some
name. To enter the euro sign, we can make use of the character map (View>Character
map). If it does not contain the characters that we need, the reason is doubtless that the
required font is not available. We can change the font by right-clicking on the character
map and selecting Other font on the contextual menu that appears. On this same contextual menu, there is also a function Goto for rapidly searching for a character whose
name or Unicode code point we know.
Then we will compile the program (Keyboard>Compile keyboard). If errors occur during compilation, they will be reported at the bottom of the window, which shows messages from Keyman. Once we have compiled the program successfully, we can debug it
(Debug>Show debugger). The debugger’s window opens, and Keyman is ready to accept
our keystrokes.
We can select rapid mode (all instructions are executed immediately) or step-by-step
mode (in which we can follow the flow of the program after every keystroke). By typing
in the Debug input area, we can see the dollar sign change to a euro sign (a fine European
dream) and the apostrophe followed by an ‘e’ turn into an ‘é’.
We can experiment a little to gain a better understanding of how Keyman works. For
example, if we type xxx'xxx and then insert an ‘e’ after the apostrophe, it will indeed be
replaced by an ‘é’. On the other hand, if we type an apostrophe followed by a space and
an ‘e’, then delete the space, the replacement will not occur.
```

Let us return now to KMN’s syntax. We may use any number of characters in the rules, both for the context and for the result. Thus we can imagine three Unicode characters (the context) followed by a fourth (the current character) that yield seven other characters (the result). Now suppose that we wish to write a rule that will change the case of the 20 consonants of the Latin alphabet. Must we write 20 rules? Not at all. Three keywords—store, any, and index—allow us to define lists of characters and perform iterative operations on them. Thus we begin by defining two lists of characters, called uppercase and lowercase: store(uppercase) "BCDFGHJKLMNPQRSTVWXZ" store(lowercase) "bcdfghjklmnpqrstvwxz" Next we write a rule in which we consider the 20 elements of the uppercase list one by one and convert them to elements of the lowercase list in the same position: + any(uppercase) > index(lowercase, 1) The 1 indicates that the any to which we have referred is character number 1 of the expression at the left. We can imagine another rule that would reverse the order of two letters: any(lowercase) + any(lowercase) > index(lowercase, 2) index(lowercase, 1) (all on one line). Up to now we have not used any dead keys, yet we have modified an ‘e’ preceded by an apostrophe. We have less need for dead keys, since combinations can easily be built up without them. But in case we should like to use them, here is how to do so. A rule can produce an invisible “character” written in the form deadkey(foo), in which foo is a keyword. Nothing will be displayed for the time being. Next, we shall write other rules that will serve as a context or a portion of a context for deadkey(foo). Other interesting keywords: context, nul, and beep. The first of these, context, is used as a right-hand component. It will be replaced by the context of the left-hand part. It can be followed by the index of the character that we wish to produce: "raou" + "l" > context(4) will produce a ‘u’. The keyword nul is also used on the right-hand side. It indicates that there will be no output. Finally, with the keyword beep, the machine generates a beep. This device can be used to punish the typist for trying to enter a bad combination of characters.

Virtual Keyboards All the code that we have written has been “mnemonic” because we have used Unicode characters, not the identifiers of keys. To use the latter, we can write [NAME], in which NAME is the name of a key. To obtain the name of a given key, we can use the feature Tools>Virtual Key Identifier. The window that appears will display the name of any key that we press. Finally, the best aspect of KMN’s syntax: groups. These play the role of states in finite automata: a rule can invoke a group (i.e., activate a state), and each group contains rules that are specific to it. Let us take an example. Suppose that we want a keyboard that will prevent a Cyrillic letter from immediately following a Latin letter (to prevent the problems that result from mixing scripts): begin Unicode > use(prelim) store(latin) "ABCDEFGHIJKLMNOPQRSTUVWXYZ" store(cyrillic) "АБЦДЕФГХИЙКЛМНОПЯРСТУЖВЬЫЗШЭЩЧЪЮ" group(prelim) any(latin) > context use(latinstate) nomatch > use(nostate) group(latinstate) using keys + any(cyrillic) > beep nomatch > use(nostate) group(nostate) using keys Explanation: At the beginning (as soon as we have typed a character), we ask Keyman to go into the prelim group. There we ask: is the letter that has just been entered a Latin letter? If so, we store this letter as a context for the following rule and switch to the group latinstate. In this group there is only one rule: if the following character is Cyrillic, we sound a beep and stop the process. In both groups, if the letter that is entered does not comply with the rule, we switch to the group nostate, which does not have any rules.6 Under X Window Under X Window, we have two fundamental concepts [299, p. 401]: the keycode (which is the number of each physical key) and the keysym (the symbolic name associated with each key). To configure a virtual keyboard is to write a table of mappings between the two. 6 A word of warning to the reader who may be trying to play around with the code above under his copy of Keyman Developer: there is a bug in the debugger’s input area that requires the user to release the shift key and press it again for each capital letter. There is also a separate testing window (validate it first with Tools> Options>Debugger, then press F9 to open it), which does not suffer from this flaw.

```text
xmodmap
The basic tool for manipulating virtual keyboards is xmodmap, a utility as old as X itself.
By entering xmodmap -pke, we obtain a list of mappings between keycode and keysym that
looks like this:
keycode
8 = q Q doubledagger
keycode
9 = s S Ograve
keycode
10 = d D
keycode
11 = f F NoSymbol periodcentered
keycode
12 = h H Igrave Icircumflex
keycode
13 = g G
keycode
14 = w W leftanglebracket rightanglebracket
The four different entries indicate the keysym when there is no modifier; when the Shift
key is pressed; when a key called Mode_switch, which is therefore a modifier, is pressed;
when Mode_switch and Shift are pressed together. What is this Mode_switch key? That
is also specified in the code, along with the identity of the modifier key for Shift and all
the other modifiers:
keycode
63 = Meta_L
keycode
64 = Shift_L
keycode
65 = Caps_Lock
keycode
66 = Mode_switch
keycode
67 = Control_L
keycode
68 = Shift_R
keycode
69 = Alt_R
keycode
70 = Control_R
If we save the output of xmodmap -pke, we obtain a configuration file for a virtual keyboard. Then we have only to run
xmodmap ./mykeyboard
(in which mykeyboard is a file using the same syntax as the code above), and the new
keyboard is loaded.
To test both the keycode associated with each key and the keysym that is associated with
the current configuration, we can launch xev, a very special application that opens a little
window and captures every event that occurs while the cursor is positioned over that
window. Thus when we press the ‘a’ key under these conditions, we see:
KeyPress event, serial 24, synthetic NO, window 0x1000001,
root 0x38, subw 0x0, time 1568428051, (129,44), root:(244,364),
state 0x0, keycode 20 (keysym 0x61, a), same_screen YES,
XLookupString gives 1 bytes:
"a"
```

Conversion of Text from One Encoding to Another KeyRelease event, serial 24, synthetic NO, window 0x1000001, root 0x38, subw 0x0, time 1568428130, (129,44), root:(244,364), state 0x0, keycode 20 (keysym 0x61, a), same_screen YES, XLookupString gives 1 bytes: "a" Thus there are two events: the pressing of the key and its release. The keycode of this key is 20, and the keysym is a. If we press ‘é’ on a French keyboard, we obtain: KeyPress event, serial 24, synthetic NO, window 0x1000001, root 0x38, subw 0x0, time 1568533302, (110,40), root:(225,360), state 0x0, keycode 27 (keysym 0xe9, eacute), same_screen YES, XLookupString gives 1 bytes: "é" KeyRelease event, serial 24, synthetic NO, window 0x1000001, root 0x38, subw 0x0, time 1568533382, (110,40), root:(225,360), state 0x0, keycode 27 (keysym 0xe9, eacute), same_screen YES, XLookupString gives 1 bytes: "é" in which we see the keycode (27), the keysym (eacute), and even an interpretation of the keysym as a Unicode character: ‘é’. Another interesting feature of xmodmap: instead of defining the behavior of the keys, we can reallocate the characters. Thus, if we write: keysym bracketleft = 0x005b 0x007b 0272 0260 keysym bracketright = 0x005d 0x007d 0305 comma keysym a = a A 0277 0304 keysym s = s S 0313 0246 keysym d = d D 0241 0257 it is the keysym values that will change, according to the modifiers that are activated. This style of writing is independent of the physical keyboard. There is also XKeyCaps (see Figure 5-10), a graphical interface for xmodmap that was developed by Jamie Zawinski. This interface allows us to select the keysym for each keycode from a list of available keysym values. Unfortunately, the development of this program was halted in 1999. Conversion of Text from One Encoding to Another There are few tools for converting text, no doubt because text editors (such as BBEdit and Ultra-Edit) and word-processing packages (such as MS Word and Corel WordPerfect) handle this process internally. There is a free library of subroutines devoted to converting between encodings: libiconv, developed by Bruno Haible. The GNU software provided with this library that performs conversions is called iconv.

Figure 5-10: The main window of XKeyCaps The recode Utility In this section we shall describe a program with a long history (its origins, under a different name, go back to the 1970s) that today is based on libiconv: recode, by the Québécois François Pinard [293]. To convert a file foo.txt, all that we need is to find the source encoding A and the target encoding B on the list of encodings supported by recode and write: recode A..B foo.txt The file foo.txt will be overwritten. We can also write: recode A..B < foo.txt > foo-converted.txt In fact, we can go through multiple steps: recode A..B..C..D..E foo.txt What is even more interesting is that recode refers to surface, which is roughly the equivalent of Unicode’s serialization mechanisms (see page 62)—a technique for transmitting data without changing the encoding. If S is a serialization mechanism, we can write: recode A..B/S foo.txt and, in addition to the conversion, this mechanism will also be applied. For example, we can convert data to hexadecimal, or base 64, or quoted-printable (page 48). Here are the serialization mechanisms provided by recode:

Conversion of Text from One Encoding to Another
• b64:7 base 64.
• d1, d2, d4: write the characters as decimal numbers, byte by byte, wyde by wyde, or
tetrabyte by tetrabyte.
• h1, x2, x4: write the characters as hexadecimal numbers, byte by byte, wyde by wyde,
or tetrabyte by tetrabyte.
• o1, x2, x4: write the characters as hexadecimal numbers, byte by byte, wyde by wyde,
or tetrabyte by tetrabyte.
• QP: quoted-printable.
• CR and CR-LF: convert Unix’s line feeds to carriage returns or carriage returns followed by line feeds.
What concerns us here is the conversion of data to Unicode. Here are the Unicode encoding forms that are recognized by recode:
• u7: UTF-7, which has the advantage of being expressible in ASCII and of being generally legible, at least for the European languages
• u8: our beloved UTF-8
• u6: generic UTF-16, either big-endian or little-endian, according to the platform being used
• UTF-16BE and UTF-16LE: big-endian or little-endian UTF-16, respectively
And those of ISO 10646:
• UCS-2-INTERNAL: the 16-bit encoding, with the endianness of the local platform.
• UCS-2-SWAPPED: the 16-bit encoding, with endianness opposite to that of the local
platform.
• UCS-2LE: the 16-bit encoding in little-endian mode. Recall that UCS-2 is like UTF-16,
with the exception that the code points beyond 0x10FFFF, while not disallowed, are
simply not allocated.
• UCS-4-INTERNAL, UCS-4-SWAPPED, UCS-4BE, UCS-4LE: the 32-bit encoding, with the
endianness of the platform, with the opposite endianness, in big-endian mode, and
in little-endian mode, respectively.
Sometimes recode refuses to convert a document, no doubt because there is a character
that cannot be converted. In this case, we can force it to complete the conversion by using
the -f option. The results, of course, must be used with care.
Among the encodings supported by recode (there are 277 in all, as of version 3.6), these
are the most important:
7 There are many aliases for each name. We have provided only one, typically the shortest.

• us, which is simply the version of ASCII localized for the United States, which was
to become ISO 646.1991-IRV. Accented letters are decomposed into an accent and a
letter: voil`a.
• The Mac’s encodings: MacArabic, MacCentralEurope, MacCroatian, MacCyrillic,
MacGreek, MacHebrew, MacIceland, MacRoman, MacRomania, MacThai, MacTurkish,
MacUkraine.
• The Chinese encodings: BIG5, cn (le codage GB 1988), CHINESE (le codage GB 2312),
ISO-2022-CN, ISO-2022-CN-EXT, EUC-CN, EUC-TW.
• The Japanese encodings: JIS_C6220-1969, JIS_C6229-1984, JIS_X0201, JIS_X0208,
JIS_X0212, SJIS, ISO-2022-JP, ISO-2022-JP-1, ISO-2022-JP-2, EUC-JP.
• The Korean encodings: KSC5636, KSC_5601, KS_C_5601, JOHAB, ISO-2022-KR, EUC-KR.
• The ISO 8859 family of encodings: l1, l2, ... l9 (ISO Latin-1 to -9), cyrillic (ISO
8859-5), arabic (ISO 8859-6), greek (ISO 8859-7), hebrew (ISO 8859-8).
• The Microsoft code pages: CP866, CP874, CP932, CP949, CP950, CP1133, CP1258, ms-ee
(Windows 1250), ms-cyrl (Windows Cyrillic), ms-ansi (Windows Latin 1), ms-greek,
ms-turk, ms-hebr, ms-arab, WinBaltRim.
• EBCDIC and all of its localized forms: EBCDIC, EBCDIC-FR, etc.
• Some pseudo-encodings:
– TeX: the accents in \'{e}, \`{a}, etc.
– h1, ... , h4: HTML entities &eacute;, &ccedil;, etc., in which the digit denotes
the HTML version.
– flat: all accented letters lose their accents.
– dump-with-names gives us a list of all the characters in the document, one character per line, containing for each character its numeric value, its representation,
and its Unicode description.
– Texte [in French!], a decomposition of the accented letters into “letter + accent”,
created specially for French (e'le'ment, apre`s, de'ja`).
The reader may consult the list of all the encodings that recode supports by typing
recode -l.

```text
Font Management on the
Macintosh
Our concern in this chapter will be the installation and management of fonts under
Mac OS 9 and Mac OS X. The Mac OS 9 operating system is the fruit of a long development process that began in 1984 with System 1.0, which came with the very first
Macintosh. It is not astonishing that practically all extant types of fonts are found under
Mac OS 9. We shall begin by describing these types of fonts and giving a little glimpse at
font management à la Macintosh.
But Mac OS 9 will soon be nothing but a fleeting memory, since Mac OS X, the new
Unix-based operating system, now comes standard on Macintoshes. At the beginning of
the twenty-first century, Mac OS X aimed to simplify font management while also adding
new functionality. We shall discuss the new features in the second part of this chapter.
Nevertheless, one thing has remained unchanged throughout the long course of development that led to Mac OS X: the ease of installing fonts. All that was necessary, dixit
Apple, was to place them in the system folder (under Mac OS 9 and earlier systems) or in one
of the designated folders (under Mac OS X). What more, then, need we say about installing
fonts on the Macintosh?
In fact, a number of factors combine to make font management on the Macintosh more
complex than Apple claims. First of all, fonts placed in the system folder are loaded into
memory; thus they take up RAM and slow down both booting and the launching of
applications (which systematically analyze the fonts contained in the system folder). Second, fonts are files that remain permanently open and that can be corrupted upon the
slightest system crash. A corrupted font loaded by the system will cause a fatal system
crash. Such crashes are often fraught with consequences, and this type of corrupt file is
also difficult to detect.
```
