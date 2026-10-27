import opencc

s2t = opencc.OpenCC('s2t')

with open('scripts/ch3_enrichment.md', 'r', encoding='utf-8') as f:
    enrich_zh = f.read()

enrich_hant = s2t.convert(enrich_zh)

enrich_ja = """### ソフトドット文字（Soft-Dotted Letters）

ラテン文字の小文字 ‘i’ および ‘j’ は、そのグリフ頂部に固有の点（Tittle / Dot）を備えている。アクセント記号やダイアクリティカルマークを冠する「特権」を得る代償として、これらの文字は本来の点を放棄しなければならない：例えば ‘î’ と記述し、点とサーカムフレックスが重複した奇妙なグリフにはならない。[^ch3_note_latex]

唯一の例外はリトアニア語（Lithuanian）である：同言語の正書法では、アクセント記号の下に元の点を厳格に維持することが要求される！これと対比して、リトアニア語の ‘i’ の点は「ハードドット」（Hard Dot）と呼ばれる。

では符号化において、通常の ‘i’ の点を「硬化」させるにはどうすればよいか？Unicode が推奨する標準手法は、‘i’ の直後に結合文字 `0x0307 COMBINING DOT ABOVE` を付加することである。画面上の表示は同一であるが（‘i’ が本来ソフトドットを持つため）、その挙動は根本的に変化する：これ以降に追加されるいかなるダイアクリティカルマークも、元の点を抹消・抑制しなくなる。したがって点とサーカムフレックスの共存を望む場合、「i + combining dot above + circumflex accent」の3文字連続として表現することになる。

[^ch3_note_latex]: 長年にわたり、$\\mathrm{\\LaTeX}$ の初心者が犯す最も典型的な誤りの一つが、ドットなし小文字 `\\i` を用いた `\\^{\\i}` ではなく直に `\\^i` と書くことであった。T1 フォントエンコーディングとマクロによるソフトドットのネイティブサポートによって、この歴史的課題は解消された。

### 数学文字（Mathematical Characters）

より厳密には、Unicode において「その他の数学」（Other Math）プロパティを持つ文字を指す。これは一般カテゴリ `Sm`（数学記号）の全文字、および `PropList.txt` の `Other_Math` プロパティにリストアップされた 1,069 文字から構成される。数式内に登場し得るあらゆる約物（括弧、角括弧、波括弧、縦線など）、および数学用英数字記号ブロック（`0x1D400-0x1D7FF`）に配置された様々な書体スタイル（黒板太字、スクリプト体、フラクトゥール等）の全文字がここに集結している。

カテゴリ `Sm` への割り当てが数学演算子であることを保証するとすれば、「数学文字」プロパティは組版ソフトウェアが数式の適用範囲を正確に同定するのを支援する。しかし悲しいことに——日常の一般的なラテン文字およびギリシャ文字は、数式に不可欠な存在であるにもかかわらず、`Sm` にも「数学文字」プロパティにも属していない！

### 引用符（Quotation Marks）

このプロパティは、世界中の諸文字において引用の境界を示すために用いられるあらゆる約物を網羅しており、カテゴリ `Po`、`Pi`、`Pf`、`Ps`、`Pe` にまたがる。計 29 文字が定義されており、`PropList.txt` の `Quotation_Mark` のもとに一元管理されている。

### ダッシュ（Dashes）とハイフン（Hyphens）の精緻な対比

組版学において、ダッシュとハイフンは明確に異なる言語的役割を担っている：
- **ダッシュ（Dashes）**：視覚的に横線状であり、ダッシュとして機能する記号全般。計 20 文字がこのプロパティを持ち、カテゴリ `Pd`（ダッシュ約物）および `Sm`（数学マイナス等）に属し、`PropList.txt` の `Dash` にリストされている。
- **ハイフン（Hyphens）**：この独立プロパティの存在は、Unicode コンソーシアムが「ハイフン」と「ダッシュ」を明確に弁別しようとした意志を象徴している：
  * **ハイフン**は**語の内部**に配置され、**形態論的役割**を果たす（例：“merry-go-round”、“two-year-old”）；
  * **ダッシュ**は**語と語の間**に配置され、**統語論的役割**を果たす（例：“I’m leaving—do I have to repeat myself?”）。

ただし、各国における組版慣行の多様性から、一部の文字は「ダッシュ」と「ハイフン」の双方のプロパティを併せ持っている。現在 10 文字が `Hyphen` プロパティを持ち、`Pd`、`Pc`（接続約物、カタカナの中黒など）、`Cf`（フォーマット文字、ソフトハイフンなど）に分布している。

### 終結約物（Terminal Punctuation）、ダイアクリティカルマーク、伸長子

- **終結約物（Terminal Punctuation）**：文末の終止符（ピリオド、疑問符、感嘆符、アラビア語節区切り等）を標識し、自然言語処理の文境界検出や段落フロー分割に用いられる。
- **ダイアクリティカルマーク（Diacritics）**：文字体系においてアクセントや声調等を修飾する独立・結合記号を特定する。
- **伸長子（Extenders）**：先行文字を水平書字方向に物理的に引き伸ばす記号（アラビア語のカシーダ / タトウィール `0x0640`、日本語カタカナの長音符 `U+30FC` 等）。

### Unicode 1.0 旧名称と ISO 10646 の歴史的逸話

Unicode 1.0 が国際標準化機構 ISO 10646 と統合される以前の時代、双方はそれぞれ独立して策定を進めていた。`UnicodeData.txt` の第 10 フィールドには、その時代の化石である Unicode 1.0 当時の文字名称が今なお記録されている。

これらの旧名称を振り返ると、現在の規格名よりも優れていた例が散見される：
- 例えば、ASCII の独立アクセント記号の旧名には明確に **`spacing`**（スペーシング）の語冠が付されていた（`spacing grave`、`spacing diaeresis` 等）。これにより、送り幅を持つ独立文字であることが一目瞭然であった；
- 括弧記号は現在のように機械的な `left parenthesis`（左括弧）/ `right parenthesis`（右括弧）ではなく、優雅に `opening parenthesis`（開始括弧）/ `closing parenthesis`（終了括弧）と命名されていた——アラビア語等の右横書き環境では括弧が鏡像反転し、縦組では時計回りに90度回転するため、「左括弧」という呼称は極めて不適切だからである！

一方で、初期 Unicode には信じがたい誤謬も存在した：
- コプト文字（Coptic）の数々を誤ってギリシャ文字と混同し、`GREEK CAPITAL LETTER SHEI` や `GREEK CAPITAL LETTER FEI` といった奇妙な名称を与えていた；
- 現代ジョージア文字に大文字・小文字の区別が一切存在しないにもかかわらず、小文字として `GEORGIAN SMALL LETTER AN` と命名するなどの記念碑的失策を犯していた。

第 11 フィールドには ISO 10646 側の公式注記が格納されている。両規格は定期的に同期されるが、ISO が独自に追加したコメントを Unicode がそのまま受容する義務は負っていない。

---

## 大文字・小文字プロパティ（Properties That Pertain to Case）

大文字・小文字（Case）の二元制は、幸いにも**「二院制文字体系」（Bicameral Scripts）**と呼ばれるごく一部の言語（ラテン、ギリシャ、コプト、キリル、アルメニア、典礼用ジョージア、デゼレット文字等）のみに限定される組版現象である。テキスト処理系に複雑怪奇な計算コストをもたらすからこそ、これが限定的であることは「幸い」と言える。

Unicode は3つの基本ケースを区別する：
1. **小文字（Lower Case）**：通常のテキスト本文；
2. **大文字（Upper Case）**：文頭や強調の全大文字；
3. **タイトルケース（Title Case）**：単語先頭の大文字合成文字（合字 `Ǆ` に対応するタイトルケース `ǅ` など）。

なお「Title Case」という術語は極めて不適切であり、英語圏以外のタイポグラフィ規範とは乖離している。これは英語圏の書籍題名において主要単語の頭文字を機械的に大文字化する風習（フランス語原題 “*La vie est un long fleuve tranquille*” が英題で “*Life Is a Long and Quiet River*” となる現象）に由来する。

### 現代の Unicode が依然として扱えない4つの未解決ケース

具体的なプロパティ詳解に入る前に、著者の Haralambous 氏は、現代の Unicode 規格が依然としてエレガントに処理できない4つの現実的な大文字・小文字の奇観を提示している：

1. **強制的低ケース（Obligatory Lower Case）**：全大文字の文脈であっても、絶対に小文字にとどまらなければならない文字。例えばドイツ語の会社形態略称 **`GmbH`**（*Gesellschaft mit beschränkter Haftung*：有限会社）における ‘m’ と ‘b’ は常に小文字でなければならない！また電気工学においてミリボルト **`mV`** とメガボルト **`MV`** は9桁の致命的差異を有しており、大文字変換アルゴリズムが ‘m’ を無差別に大文字化すれば機器の破滅的損傷を招く；
2. **強制的キャピタル（Obligatory Capitals）**：国名 **`Turkey`**（トルコ）における ‘T’ は常に大文字であり、小文字の `turkey` は鳥のシチメンチョウを指してしまう；
3. **交互大文字（Alternating Capitals）**：近年のドイツ語で男女平等を包括する表現 **`StudentInnen`**（男子学生 Studenten と女子学生 Studentinnen の統合表記）。小文字文脈の中で単語内部の ‘I’ のみが大文字化する；
4. **交互小文字（Alternating Lowercase Letters）**：上記表記を全大文字見出しで組む場合、**`STUDENTiNNEN`** となり、内部の ‘i’ のみが頑健に小文字を維持しなければならない！
"""

# Apply to zh
with open('docs/zh/fonts-encodings/chapter-3.md', 'r', encoding='utf-8') as f:
    zh_content = f.read()

start_zh = '### 软点字母（Soft-Dotted Letters）'
end_zh = '## 大小写相关属性（Properties That Pertain to Case）'
p1 = zh_content.find(start_zh)
p2 = zh_content.find(end_zh)
zh_content = zh_content[:p1] + enrich_zh + '\n\n' + zh_content[p2 + len(end_zh):]
with open('docs/zh/fonts-encodings/chapter-3.md', 'w', encoding='utf-8') as f:
    f.write(zh_content)
print('Applied to zh/chapter-3.md')

# Apply to zh-hant
with open('docs/zh-hant/fonts-encodings/chapter-3.md', 'r', encoding='utf-8') as f:
    hant_content = f.read()

start_hant = s2t.convert(start_zh)
end_hant = s2t.convert(end_zh)
p1 = hant_content.find(start_hant)
p2 = hant_content.find(end_hant)
hant_content = hant_content[:p1] + enrich_hant + '\n\n' + hant_content[p2 + len(end_hant):]
with open('docs/zh-hant/fonts-encodings/chapter-3.md', 'w', encoding='utf-8') as f:
    f.write(hant_content)
print('Applied to zh-hant/chapter-3.md')

# Apply to ja
with open('docs/ja/fonts-encodings/chapter-3.md', 'r', encoding='utf-8') as f:
    ja_content = f.read()

start_ja = '### ソフトドット文字（Soft-Dotted Letters）'
end_ja = '## 大文字・小文字に関する属性（Properties That Pertain to Case）'
p1 = ja_content.find(start_ja)
p2 = ja_content.find(end_ja)
if p1 != -1 and p2 != -1:
    ja_content = ja_content[:p1] + enrich_ja + '\n\n' + ja_content[p2 + len(end_ja):]
    with open('docs/ja/fonts-encodings/chapter-3.md', 'w', encoding='utf-8') as f:
        f.write(ja_content)
    print('Applied cleanly to ja/chapter-3.md')
else:
    print(f'JA find failed: p1={p1}, p2={p2}')
    for l in ja_content.splitlines():
        if 'ソフトドット' in l or '二院制' in l or 'Pertain to Case' in l:
            print('Line:', l)
