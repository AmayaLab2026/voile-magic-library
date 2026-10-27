
---

### 传奇转码利器：François Pinard 的 `recode` 实用程序

在 Unix 自由软件历史长河中，有一款拥有数十载深厚渊源的传奇转码工具——由加拿大魁北克杰出程序员弗朗索瓦·皮纳尔（François Pinard）主导开发的 **`recode`** [293]。其历史雏形（当时冠以其他名称）甚至可一路追溯至 20 世纪 70 年代，而其现代版本则在底层依托于 GNU `libiconv` 运行时架构。

#### 1. 极简优雅的管道语法

在命令行中，转换文件 `foo.txt` 的基本语法极其直观：只需在 `recode` 庞大的支持列表里找到源编码 $A$ 与目标编码 $B$，即可直接执行原位覆写转换：

```bash
recode A..B foo.txt
```

若希望保留原始文件并重定向输出至新文件，可使用标准流重定向：

```bash
recode A..B < foo.txt > foo-converted.txt
```

更为惊艳的是，`recode` 允许在单一命令调用中串联任意多级转换跳板：

```bash
recode A..B..C..D..E foo.txt
```

#### 2. “表面”（Surface）序列化机制

`recode` 最具突破性的设计之一，在于引入了名为“表面”（Surface）的概念——这在本质上正是 Unicode 序列化机制（Serialization Mechanisms）的对应物：**在不改变字符抽象编码的前提下，对其物理存储与传输载体形态进行变换**。

若 $S$ 为某种表面序列化机制，用户可通过斜杠语法将其直接附加于目标编码之后：

```bash
recode A..B/S foo.txt
```

在执行编码 $A \to B$ 转换的同时，工具会自动叠加上特定的序列化表示。`recode` 提供的核心表面机制包括：
* **`b64`**：标准的 Base64 编码；
* **`d1, d2, d4`**：以十进制纯数字形式转储字符（分别对应单字节 byte-by-byte、双字节 wyde-by-wyde、四字节 tetrabyte-by-tetrabyte）；
* **`h1, x2, x4`**（以及八进制形式 `o1`）：以十六进制或八进制格式输出字节序列；
* **`QP`**：电子邮件中广泛采用的 Quoted-Printable 可打印字符编码；
* **`CR` 与 `CR-LF`**：行尾终止符标准化转换（将 Unix 换行符 LF 转换为经典 Mac 的回车符 CR，或 Windows/DOS 的 CR-LF 序列）。

#### 3. 全景式 Unicode 与 ISO 10646 编码形式支持

对于面向现代 Unicode 体系的转换，`recode` 提供了细致入微的编码形式别名：
* **`u7`**：UTF-7 编码（其优势在于完全由纯 ASCII 字符表示，对欧洲语言具备高度的人类可读性）；
* **`u8`**：通用的标准 UTF-8；
* **`u6`**：通用 UTF-16（字节序自适应当前主机平台的本地硬件架构）；
* **`UTF-16BE` 与 `UTF-16LE`**：显式钦定的大端序（Big-Endian）与小端序（Little-Endian）UTF-16；
* **ISO 10646 家族别名**：
  - `UCS-2-INTERNAL`：采用本地字节序的 16 位编码；
  - `UCS-2-SWAPPED`：采用与本地主机完全相反字节序的 16 位编码；
  - `UCS-2LE`：纯小端序 16 位编码（在此重温：UCS-2 绝大多数规则与 UTF-16 一致，唯独不支持超出 `0x10FFFF` 的辅助平面代理对）；
  - `UCS-4-INTERNAL`、`UCS-4-SWAPPED`、`UCS-4BE`、`UCS-4LE`：32 位全宽编码的完整字节序矩阵。

在转换过程中，若文档包含某些无法直接映射的目标字符，`recode` 默认会终止处理以确保数据安全；用户可通过附加 **`-f`（Force）参数** 强制工具完成转码（未识别字符将被特定标记替换，但在工程中须谨慎校验结果）。

#### 4. 277 种编码体系与独特的“伪编码”（Pseudo-Encodings）生态

截至 3.6 版本，`recode` 官方支持的编码库高达 277 种，完整横跨了半个多世纪的计算史遗产：
* **`us`**：美国本地化 ASCII（即后来的 ISO 646.1991-IRV），带音符的字母会自动拆解为反斜杠形式（如 `voil\a`）；
* **Macintosh 体系**：`MacArabic`、`MacCentralEurope`、`MacCroatian`、`MacCyrillic`、`MacGreek`、`MacHebrew`、`MacIceland`、`MacRoman`、`MacRomania`、`MacThai`、`MacTurkish`、`MacUkraine` 等全套经典资源分叉编码；
* **中文传统编码**：`BIG5`、`cn`（GB 1988）、`CHINESE`（GB 2312）、`ISO-2022-CN`、`ISO-2022-CN-EXT`、`EUC-CN`、`EUC-TW`；
* **日文传统编码**：`JIS_C6220-1969`、`JIS_C6229-1984`、`JIS_X0201`、`JIS_X0208`、`JIS_X0212`、`SJIS`、`ISO-2022-JP`、`EUC-JP` 等；
* **韩文传统编码**：`KSC5636`、`KSC_5601`、`JOHAB`（组合型编码）、`ISO-2022-KR`、`EUC-KR`；
* **ISO 8859 全家桶**：`l1` 至 `l9`（Latin-1 至 Latin-9）、`cyrillic`（8859-5）、`arabic`（8859-6）、`greek`（8859-7）、`hebrew`（8859-8）；
* **微软代码页**：`CP866`、`CP874`、`CP932`、`CP949`、`CP950`、`CP1258`、`ms-ee`（Windows-1250）、`ms-cyrl`（Windows-1251）、`ms-ansi`（Windows-1252）、`ms-greek`、`ms-turk`、`ms-hebr`、`ms-arab` 等；
* **大型机 EBCDIC**：覆盖各主要国家语言本地化变体的 EBCDIC 系列。

尤为令人拍案叫绝的是 `recode` 原创的一系列**“伪编码”（Pseudo-Encodings）**，它们为文档排版与逆向工程提供了不可替代的魔术般捷径：
* **`TeX`**：自动将文档中的带音符字符转换为纯正的 $\mathrm{\TeX}$ 控制宏（例如将 `é` 转为 `\'{e}`，将 `à` 转为 `\`{a}`）；
* **`h1, ..., h4`**：自动将特殊字符转义为对应 HTML 版本标准的命名实体（如 `&eacute;`、`&ccedil;`）；
* **`flat`**：将所有带音符的字母粗暴剥离其附加符号，退化为其基础拉丁字母骨架（如将 `ë`、`ê`、`é` 统一拍平为 `e`）；
* **`dump-with-names`**：将文档中的每一个字符逐一展开，打印出其所属的 Unicode 官方标准全称（例如将字符 `A` 展开为 `0x0041 LATIN CAPITAL LETTER A`），为字符属性研判与疑难乱码排查提供了终极调试利器！
