# 附录 C：PostScript 体系字体格式深度参考（Type 1, Type 2/CFF, MM, Type 0, CIDFont）

*译者：[Lycoris \<lycorismisaka@gmail.com\>](mailto:lycorismisaka@gmail.com)*

1984 年，约翰·沃诺克（John Warnock）与查尔斯·格施克（Charles Geschke）创立的 Adobe 公司发布了 **PostScript 页面描述语言**。PostScript 不仅是一套绘图指令，更是一门图灵完备的逆波兰栈式编程语言。随之诞生的 **PostScript Type 1 字体格式**，首次将三次贝塞尔曲线（Cubic Bézier Splines）与高度机密的字体微观渲染提示（Hinting）机制引入数字印刷，彻底催生了人类的桌面出版革命（DTP Revolution）。

在长达十余年的时间里，Adobe 将 Type 1 的核心字节码解释器与加密算法视为最顶级的商业机密，直到 1990 年面对苹果与微软联手推出 TrueType 的巨大竞争压力，才被迫公开出版了著名的黑皮书《Adobe Type 1 Font Format》。本附录基于 PostScript 官方规范，对 Type 1、Type 2（CFF）、Multiple Master、Type 0 复合字体以及当今东亚巨型字库的基石 CID-keyed 字体进行底层的全面技术解密。

---

## C.1 PostScript Type 1 字体的内存拓扑与解密引擎

一个物理上的 Type 1 字体在不同操作系统下有不同的打包载体：
1. **`.PFA`（PostScript Font ASCII）**：纯文本封装格式，常用于 Unix 工作站与通信信道。`eexec` 加密段被编码为两位的十六进制 ASCII 字符串（Hexadecimal-encoded），每行 64 字符；
2. **`.PFB`（PostScript Font Binary）**：二进制封装格式，常用于 IBM PC 与 Windows 系统。文件由若干个带 6 字节二进制头部的记录块（Records）拼接而成；
3. **Mac OS `POST` 资源**：在经典 Mac 操作系统中存储于资源分支（Resource Fork）中的 `POST` 资源段中。

```
+-------------------------------------------------------+
|  .PFB 记录块结构 (Record Header: 6 Bytes)              |
+-------------------------------------------------------+
|  Byte 0:     0x80 (魔数标识符)                          |
|  Byte 1:     记录类型 (0x01: ASCII, 0x02: Binary, 0x03: EOF)
|  Bytes 2-5:  记录长度 (32-bit Little-Endian uint32)    |
|  Bytes 6..N: 载荷数据 (Payload Data)                  |
+-------------------------------------------------------+
```

整个 Type 1 字体由三大逻辑段构成：
1. **ASCII 明文头部段**：包含字体家族声明、版权信息与全局元数据字典；
2. **`eexec` 二进制加密段**：受到伪随机数发生器加密保护的私有核心，包含字体全局微调参数字典 `Private` 与字形轮廓字典 `CharStrings`；
3. **512 字节全零尾部与 `cleartomark` 闭合段**：用于刷新 IBM PC 通信端口与早期激光打印机串口缓冲区。

::: tip PostScript Type 1 字体整体拓扑与 eexec 解密结构（Figure C-1, C-2）
![Type 1 字体整体拓扑（Figure C-1）](/images/fonts-encodings/fig-app-c1.png)
*Type 1 字体整体拓扑（Figure C-1）*
:::

*图 C-1：PostScript Type 1 字体顶层数据字典组织拓扑。从根目录 FontDirectory 到 FontInfo、Encoding、Private 与 CharStrings。*

::: tip Type 1 字体 ASCII 头部与 eexec 加密段（Figure C-2）
![Type 1 字体 eexec 段解构（Figure C-2）](/images/fonts-encodings/fig-app-c2.png)
*Type 1 字体 eexec 段解构（Figure C-2）*
:::

*图 C-2：Type 1 字体物理文件剖分。明文段通过 `currentfile eexec` 关键字瞬间切换为二进制密码流。*

### 1. `eexec` 线性同余解密引擎

进入 `eexec` 关键字后，PostScript 解释器启动一套 16 位线性同余伪随机数发生器（Linear Congruential Generator, LCG）进行实时流式异或解密：

$$R_{n+1} = (R_n \times c_1 + c_2) \bmod M$$

$$P_n = C_n \oplus (R_n \gg 8)$$

* 模数 $M = 65536 = 2^{16}$；
* 乘数 $c_1 = 52845$；
* 增量常数 $c_2 = 22719$；
* **初始密钥 $R_0 = 52845$**（十六进制 `0xCE6D`）；
* $C_n$ 为当前读入的密文字节，$P_n$ 为解密输出的明文字节。

**前 4 个随机字节的丢弃原则**：在 `eexec` 密文的开头，Adobe 强制填充了 4 个完全随机生成的无意义字节。解密引擎在完成前 4 轮循环后，必须将这 4 字节明文直接抛弃，从第 5 个字节开始才是真正的 PostScript 代码。这一设计的目的在于使相同内容的字库在每次导出时呈现完全不同的密文散列，破坏早期密码学者的差分分析！

#### Python 工业级 eexec 解密与加密实现：
```python
def decrypt_type1_cipher(ciphertext: bytes, key: int = 52845, discard: int = 4) -> bytes:
    # PostScript Type 1 线性同余解密算法
    # key = 52845 (eexec) 或 4330 (CharStrings)
    c1 = 52845
    c2 = 22719
    r = key
    plaintext = bytearray()
    for cipher_byte in ciphertext:
        plain_byte = cipher_byte ^ (r >> 8)
        plaintext.append(plain_byte)
        r = ((cipher_byte + r) * c1 + c2) & 0xFFFF
    return bytes(plaintext[discard:])

def encrypt_type1_cipher(plaintext: bytes, key: int = 52845, random_header: bytes = b'\x00\x00\x00\x00') -> bytes:
    # PostScript Type 1 线性同余加密算法
    c1 = 52845
    c2 = 22719
    r = key
    ciphertext = bytearray()
    full_data = random_header + plaintext
    for plain_byte in full_data:
        cipher_byte = plain_byte ^ (r >> 8)
        ciphertext.append(cipher_byte)
        r = ((cipher_byte + r) * c1 + c2) & 0xFFFF
    return bytes(ciphertext)
```

### 2. `FontInfo` 与顶层字典字段全景

在明文段中，`FontDirectory` 注册的顶层字典包含以下核心键值对：
* `FontName`（常字字名符号，如 `/Times-Roman`）；
* `PaintType`（整型：0 为填充笔画，2 为轮廓空心线框）；
* `FontType`（整型：恒为 1）；
* `FontMatrix`（仿射变换矩阵，通常为 `[0.001 0 0 0.001 0 0]`，将 1000 栅格单位归一化为 1 磅）；
* `FontBBox`（四元实数数组：`[llx lly urx ury]`，全字体的左下角与右上角极限包围盒）；
* `UniqueID`（24 位整数，用于激光打印机显存全局光栅缓存索引）；
* `Encoding`（256 元素符号数组，如 `StandardEncoding` 或 `ISOLatin1Encoding`）。

`FontInfo` 子字典则进一步记录了排版与法律元数据：
* `version`：版本号字符串；
* `Notice`：版权所有声明；
* `FullName`：人机可读的完整全名（如 `"Times Roman"`）；
* `FamilyName`：字体家族名（如 `"Times"`）；
* `Weight`：字重描述（`"Regular"`, `"Bold"`, `"Black"` 等）；
* `ItalicAngle`：倾斜角度（正体为 0.0，西文斜体通常为 $-12.0$ 度，负号表示顺时针右倾）；
* `isFixedPitch`：布尔值（等宽字体为 `true`，比例变宽字体为 `false`）；
* `UnderlinePosition`：下划线中心基准线相对于文本基线的垂直偏移（负值）；
* `UnderlineThickness`：下划线的推荐物理宽度。

### 3. `Private` 字典与底层渲染微调中枢

解密后的 `eexec` 内部定义了字体的神经中枢——`Private` 字典。它控制着光栅化渲染器在低分辨率下的所有几何对齐行为：
* **`BlueValues` 与 `OtherBlues`**：基准蓝色对齐带。定义了基线、x 字高、大写字高、升部与降部的平顶吸附区间；
* **`FamilyBlues` 与 `FamilyOtherBlues`**：字体家族全局共享的对齐带，确保同一家族的不同字重在混排时视觉平齐；
* **`BlueScale`, `BlueShift`, `BlueFuzz`**：控制对齐带随显示字号（Point Size）放大时何时解除强行平顶吸附的微调浮点常数；
* **`StdHW` 与 `StdVW`**：全字体的标准主导水平与垂直笔画宽度；
* **`StemSnapH` 与 `StemSnapV`**：允许吸附对齐的多级候选笔画宽度数组；
* **`ForceBold`**：布尔值，在小字号极低分辨率下强行将细笔画加粗一个像素，防止文字笔画断裂消失；
* **`LanguageGroup`**：语言组代码（0 代表拉丁、希腊、西里尔等西文字系；1 代表中日韩繁复汉字字系）；
* **`lenIV`**：指示字形轮廓数据 `CharStrings` 开头包含的随机校验字节数（默认恒为 4；若设为 -1 则表示不加密）。

::: tip Type 1 字体 Private 字典与蓝色对齐带空间分布（Figure C-3, C-4, C-5）
![Private 字典蓝色对齐带（Figure C-3）](/images/fonts-encodings/fig-app-c3.png)
*Private 字典蓝色对齐带（Figure C-3）*
:::

*图 C-3：BlueValues 与 OtherBlues 在基线、x 字高与大写字高周围构筑的垂直吸附禁飞区。*

::: tip StdHW 与 StemSnapH 笔画网格吸附（Figure C-4）
![StdHW 笔画宽度归一化（Figure C-4）](/images/fonts-encodings/fig-app-c4.png)
*StdHW 笔画宽度归一化（Figure C-4）*
:::

*图 C-4：水平主干与垂直主干宽度通过 StemSnap 阵列强行聚类，消除小字号下笔画粗细不均的视觉杂讯。*

::: tip Subrs 子程序池与宏指令复用（Figure C-5）
![Subrs 子程序池（Figure C-5）](/images/fonts-encodings/fig-app-c5.png)
*Subrs 子程序池（Figure C-5）*
:::

*图 C-5：`Subrs` 数组存储了全字体通用的衬线轮廓、弯角弧线与提示替换宏，供所有字形频繁调用。*

---

## C.2 Type 1 CharStrings 虚拟机解释器深度剖析

`CharStrings` 字典内部，每一个字符外观对应一段经过二次加密的二进制字节流。其解密算法与 `eexec` 完全相同，但**初始密钥被替换为 $R_0 = 4330$**。

解密后的字节码在一个深度为 24 的微型数值操作数栈上执行。Type 1 CharStrings 拥有极其精简的操作码体系，划分为单字节基础指令与 `12` 开头的双字节转义指令：

::: tip Type 1 曲线绘制指令与端点切线控制（Figure C-6, C-7, C-8）
![Type 1 曲线绘制指令（Figure C-6）](/images/fonts-encodings/fig-app-c6.png)
*Type 1 曲线绘制指令（Figure C-6）*
:::

*图 C-6：`rrcurveto`、`vhcurveto` 与 `hvcurveto` 指令通过 6 个相对坐标增量定义一段三次贝塞尔曲线。*

::: tip Type 1 闭合路径与内部轮廓填充规则（Figure C-7）
![Type 1 闭合路径（Figure C-7）](/images/fonts-encodings/fig-app-c7.png)
*Type 1 闭合路径（Figure C-7）*
:::

*图 C-7：`closepath` 指令将绘制点连接回当前轮廓的起点，形成封闭区域，并依据非零环绕数规则（Non-zero Winding Rule）进行光栅化填充。*

::: tip Type 1 复合字形 seac 指令构造重音字符（Figure C-8）
![Type 1 seac 指令（Figure C-8）](/images/fonts-encodings/fig-app-c8.png)
*Type 1 seac 指令（Figure C-8）*
:::

*图 C-8：`seac`（Standard Encoding Accented Character）指令通过基字码点与重音码点，瞬间在二维空间将两字合成，大幅节省字体体积。*

### 1. 操作数编码规则（Operand Encoding）
CharStrings 中的每个字节若处于 `32..255` 之间，则被解释为操作数（数值），被直接压入操作数栈：
* `32 <= b0 <= 246`：直接表示整数 $v = b_0 - 139$（范围：$-107 \dots +107$）；
* `247 <= b0 <= 250`：双字节正整数 $v = (b_0 - 247) \times 256 + b_1 + 108$（范围：$+108 \dots +1131$）；
* `251 <= b0 <= 254`：双字节负整数 $v = -(b_0 - 251) \times 256 - b_1 - 108$（范围：$-1131 \dots -108$）；
* `b0 == 255`：随后跟随 4 字节的大端序 32 位有符号整数。

### 2. 核心操作码字典全集

| 操作码（Hex/Dec） | 指令名称 | 参数栈形态 | 几何绘制与虚拟机执行行为 |
| :--- | :--- | :--- | :--- |
| `0x01 (1)` | `hstem` | $y \quad dy$ | 声明一条水平笔画提示（从绝对坐标 $y$ 起，垂直宽度为 $dy$） |
| `0x03 (3)` | `vstem` | $x \quad dx$ | 声明一条垂直笔画提示（从绝对坐标 $x$ 起，水平宽度为 $dx$） |
| `0x04 (4)` | `vmoveto` | $dy$ | 沿垂直轴相对移动当前画笔 $dy$ 距离（水平不移动） |
| `0x05 (5)` | `rlineto` | $dx \quad dy$ | 从当前画笔绘制一条直线至相对坐标 $(dx, dy)$ |
| `0x06 (6)` | `hlineto` | $dx$ | 绘制一条水平直线，距离为 $dx$ |
| `0x07 (7)` | `vlineto` | $dy$ | 绘制一条垂直直线，距离为 $dy$ |
| `0x08 (8)` | `rrcurveto` | $dx_1 dy_1 dx_2 dy_2 dx_3 dy_3$ | 绘制一段三次贝塞尔曲线，三对增量分别为第一控制点、第二控制点与曲线终点 |
| `0x09 (9)` | `closepath` | $\emptyset$ | 闭合当前子路径轮廓 |
| `0x0A (10)` | `callsubr` | $subr\_index$ | 调用 `Subrs` 数组中索引为 $subr\_index$ 的子程序 |
| `0x0B (11)` | `return` | $\emptyset$ | 从当前子程序返回主调用流程 |
| `0x0D (13)` | `hsbw` | $sb_x \quad wx$ | **字形初始化首指令**：设置水平左侧轴承 $sb_x$ 与字符总前进字宽 $wx$ |
| `0x0E (14)` | `endchar` | $\emptyset$ | **字形终结指令**：终结当前字符的绘制，将光栅缓存提交至输出器 |
| `0x15 (21)` | `rmoveto` | $dx \quad dy$ | 二维平面相对移动当前画笔 |
| `0x16 (22)` | `hmoveto` | $dx$ | 沿水平轴相对移动当前画笔 |
| `0x1E (30)` | `vhcurveto` | $dy_1 dx_2 dy_2 dx_3$ | 垂直起刀、水平落刀的简写贝塞尔曲线（首控制点水平位移为 0，终控制点垂直位移为 0） |
| `0x1F (31)` | `hvcurveto` | $dx_1 dx_2 dy_2 dy_3$ | 水平起刀、垂直落刀的简写贝塞尔曲线 |
| `0x0C 0x00` | `dotsection` | $\emptyset$ | 声明进入或退出字符上的点状微小特征（如字母 'i', 'j' 上的圆点） |
| `0x0C 0x01` | `vstem3` | $x_1 dx_1 x_2 dx_2 x_3 dx_3$ | 同时声明三条等距的垂直笔画提示（如字母 'm' 的三根立柱） |
| `0x0C 0x02` | `hstem3` | $y_1 dy_1 y_2 dy_2 y_3 dy_3$ | 同时声明三条等距的水平笔画提示（如字母 'E' 的三根横线） |
| `0x0C 0x06` | `seac` | $asb \quad adx \quad ady \quad bchar \quad achar$ | 标准重音合成：将基字 $bchar$ 与重音 $achar$ 在位移 $(adx, ady)$ 处瞬间拼接 |
| `0x0C 0x07` | `sbw` | $sb_x \quad sb_y \quad wx \quad wy$ | 完整四维轴承设置（包含垂直排版时的垂直轴承与前进高） |
| `0x0C 0x0C` | `div` | $num_1 \quad num_2$ | 整数除法：将栈顶两数弹出并压入商 $num_1 / num_2$ |
| `0x0C 0x10` | `callothersubr` | $arg_1 \dots arg_n \quad n \quad proc$ | 调用解释器底层的驱动级扩展程序（用于 Flex 弧线与动态提示替换） |
| `0x0C 0x11` | `pop` | $\emptyset$ | 将 `callothersubr` 返回的结果从专用暂存器弹出至操作数栈 |

### 3. Flex 弹性微弧算子（Flex Operator）

当字母轮廓中包含极其平缓的浅弧线（例如字母大写 'O' 或加长破折号的微凸弧度）时，在低分辨率屏幕上如果强行光栅化为曲线，往往会因像素阶梯效应产生一个极其丑陋刺眼的孤立凸起像素；而在高分辨率激光照排机上，排版师又必须忠实呈现该优美的弧度。

::: tip Flex 算子几何判据与双轨渲染切换（Figure C-9, C-10）
![Flex 算子几何判据（Figure C-9）](/images/fonts-encodings/fig-app-c9.png)
*Flex 算子几何判据（Figure C-9）*
:::

*图 C-9：Flex 算子的几何控制骨架。包含起点、两个控制点、中途鞍点、以及终点共 7 组二维坐标。*

::: tip Flex 在低分辨率与高分辨率下的不同输出（Figure C-10）
![Flex 双轨渲染（Figure C-10）](/images/fonts-encodings/fig-app-c10.png)
*Flex 双轨渲染（Figure C-10）*
:::

*图 C-10：Flex 动态决策：若该弧度矢高在当前显示设备上折合像素小于等于 0.5 像素（由 `BlueShift` 阈值控制），解释器强制将其退化为一条笔直的水平直线（`rlineto`）；一旦设备分辨率提升使弧度达到 1 像素以上，解释器自动无缝切换为两条平滑拼接的三次贝塞尔曲线！*

### 4. 动态提示替换（Hint Substitution）

在复杂汉字或包含密集笔画的西文符号（如货币符号 '$'、数字 '8'、字母 'B'）中，一个字符从左至右或从上到下存在数十条笔画。由于 Type 1 虚拟机的提示寄存器容量有限，若在字符开头一次性激活所有提示，会导致空间重叠与逻辑死锁。

::: tip 动态提示替换在西文与汉字中的应用（Figure C-11, C-12）
![动态提示替换机制（Figure C-11）](/images/fonts-encodings/fig-app-c11.png)
*动态提示替换机制（Figure C-11）*
:::

*图 C-11：Hint Substitution 通过调用 `callothersubr 3`，在绘制完字符上半部分后，瞬间抹除旧提示并重新声明一套全新的笔画提示集合。*

::: tip 汉字复杂笔画 Hinting 拆解（Figure C-12）
![汉字 Hinting 拆解（Figure C-12）](/images/fonts-encodings/fig-app-c12.png)
*汉字 Hinting 拆解（Figure C-12）*
:::

*图 C-12：在巨型中文字符排版中，Hint Substitution 沿书写笔顺逐笔激活局部提示，彻底消除了笔画粘连。*

---

## C.3 CFF 容器与 Type 2 CharStrings 规范

1996 年，Adobe 在推出 OpenType 架构时，对 Type 1 进行了全方位的现代化重构，推出了 **CFF（Compact Font Format）** 与 **Type 2 CharStrings**：

### 1. CFF 内部索引表（INDEX Table）二进制布局

CFF 彻底废除了 PostScript 文本解释器，采用纯二进制数据布局。其核心是通用的 **INDEX 结构**：
* `uint16 count`：对象总数；
* `uint8 offSize`：偏移数组每个指针占用的字节宽度（1 到 4 字节）；
* `uint<offSize> offset[count + 1]`：累加字节偏移数组；
* `uint8 data[...]`：连续对象二进制载荷。

### 2. CFF 顶层段落拓扑

一个合法的 CFF 表严格按序包含：
1. `Header`：魔数与版本号（通常为 `1.0`，四个字节：`0x01, 0x00, 0x04, 0x04`）；
2. `Name INDEX`：包含的字体家族名称字符串；
3. `Top DICT INDEX`：顶层键值对字典（记录 CharStrings 偏移、编码表偏移、私有字典偏移）；
4. `String INDEX`：全字体共享的字符串池（索引 391 之后自定义字符串）；
5. `Global Subr INDEX`：全局通用子程序池；
6. `Encodings` / `Charsets`：字符编码与字形名称映射；
7. `FDSelect` / `Font DICT INDEX`（针对 CIDFont）：多子字族分类选择表；
8. `CharStrings INDEX`：所有字形的 Type 2 轮廓字节码；
9. `Private DICT`：各字族的局部私有微调字典；
10. `Local Subr INDEX`：局部子程序池。

### 3. Type 2 CharStrings 的颠覆性算子

* **`hintmask` 与 `cntrmask`**：在字形轮廓指令流中间，直接紧随一个根据已声明提示总数决定的位掩码字节数组（例如 24 条提示占用 3 字节）。解释器在 1 字节开销内瞬间激活指定的笔画提示集合，彻底淘汰了 Type 1 繁琐的 `callothersubr 3`！
* **`blend` 算子**：用于支持可变字体（Variable Fonts）与多重母版，在单次计算中完成多个设计母版坐标的线性组合；
* **暂存数组与算术指令**：支持 `put`（将栈顶数存入暂存槽）、`get`（提取暂存数）、`add`, `sub`, `mul`, `div`, `sqrt`, `neg`, `abs`, `random` 等高阶代数运算。

---

## C.4 多重母版字体（Multiple Master Fonts）与连续设计轴

1991 年，Adobe 研发了代表模拟排印巅峰的 **Multiple Master（MM）技术**。MM 允许字体设计师在多维几何空间中建立连续变形轴线：

::: tip Multiple Master 二维与三维设计空间拓扑（Figure C-13, C-14）
![MM 设计空间拓扑（Figure C-13）](/images/fonts-encodings/fig-app-c13.png)
*MM 设计空间拓扑（Figure C-13）*
:::

*图 C-13：由字重轴（Weight: Light to Black）与字宽轴（Width: Condensed to Expanded）构成的二维笛卡尔设计空间。*

::: tip MM 母版轮廓拓扑同构与控制点对应（Figure C-14）
![MM 轮廓拓扑同构（Figure C-14）](/images/fonts-encodings/fig-app-c14.png)
*MM 轮廓拓扑同构（Figure C-14）*
:::

*图 C-14：多重母版插值铁律：参与混配的所有母版字形，其贝塞尔轮廓必须保持**严格绝对的拓扑同构**！即控制点总数、起刀点编号、线段与曲线段的顺序必须逐一精确对应。*

### 多重母版数学插值模型：

设设计空间包含 $k$ 个轴线，空间顶点由 $2^k$ 个极端母版字形 $M_1, M_2, \dots, M_{2^k}$ 锚定。对于用户给定的任意归一化设计坐标 $(w_1, w_2, \dots, w_k) \in [0, 1]^k$，排版引擎通过多线性基函数计算各母版的加权权重 $W_i$：

$$P = \sum_{i=1}^{2^k} W_i M_i, \quad \text{其中 } \sum W_i = 1$$

生成的衍生字形继承了所有母版的优秀基因，在 Adobe Acrobat SuperATM 中实现了对任意未知版面字体的无损克隆！

---

## C.5 Type 0 复合字体（Composite Fonts）

在处理中日韩（CJK）等包含数万汉字的庞大书写系统时，传统 PostScript 字典 256 个字符的上限彻底失效。Adobe 由此设计了 **Type 0 复合字体架构**：

::: tip Type 0 复合字体树状寻址分发体系（Figure C-15）
![Type 0 复合字体分发（Figure C-15）](/images/fonts-encodings/fig-app-c15.png)
*Type 0 复合字体分发（Figure C-15）*
:::

*图 C-15：Type 0 字体的树状解析管线。顶层 Type 0 字体不包含任何轮廓，而是一个路由交换机：通过 `FMapType` 算法将输入的双字节字符编码拆分为高字节与低字节，将高字节作为索引在 `FDepVector`（子字体依赖向量）中查得对应的底层 Type 1 子字库，再用低字节在子字库中提取具体轮廓。*

---

## C.6 CID-keyed 字体体系与 CMap 映射映射学

Type 0 架构虽然解决了字符数量限制，但存在严重的性能缺陷：将汉字硬生生割裂进数十个小字库导致字间距、度量表极度碎片化，且强行绑定了特定的本地化编码（如 Shift-JIS 或 Big5）。

1993 年，Adobe 推出了现代泛东亚字型的终极标准——**CID-keyed 字体（CIDFontType 0 与 CIDFontType 2）**：

::: tip CID-keyed 字符标识符与 CMap 分离架构（Figure C-16, C-17）
![CID 架构图解（Figure C-16）](/images/fonts-encodings/fig-app-c16.png)
*CID 架构图解（Figure C-16）*
:::

*图 C-16：字符集与字形集的彻底解耦。字库内部所有字形按 0 到 65535 的纯数字 CID（Character Identifier）无序线性排列，所有外部编码映射完全交由外挂的 CMap 文件裁决。*

::: tip CMap 文件在多编码环境下的动态映射（Figure C-17）
![CMap 映射机制（Figure C-17）](/images/fonts-encodings/fig-app-c17.png)
*CMap 映射机制（Figure C-17）*
:::

*图 C-17：同一款 CID 字体（如 Adobe-Japan1-6），挂载 `UniJIS-UTF16-H` 即可作为 Unicode 字体使用，挂载 `90ms-RKSJ-H` 即可原生支持日文 Windows Shift-JIS 编码，挂载垂直排版 CMap 即可瞬间激活竖排字形，实现了数字字型史上最伟大的一次架构大一统！*

### 1. CMap 语法规范与映射条目

一个典型的 CMap 文件由以下核心段构成：
```postscript
/CIDInit /ProcSet findresource begin
12 dict begin
begincmap
/CIDSystemInfo 3 dict dup begin
  /Registry (Adobe) def
  /Ordering (Japan1) def
  /Supplement 6 def
end def
/CMapName /UniJIS-UTF16-H def
/CMapVersion 1.018 def
/CMapType 1 def
/UIDOffset 0 def
/XUID [1 10 25330] def
/WMode 0 def % 0 = Horizontal, 1 = Vertical

% 声明编码空间范围 (1 到 4 字节)
1 begincodespacerange
  <0000> <FFFF>
endcodespacerange

% 单字符映射 (Character to CID)
10 beginbfchar
  <0020> 1
  <0021> 2
endbfchar

% 范围连续映射 (Range to CID)
25 begincidrange
  <0022> <005F> 3
  <0060> <007E> 65
endcidrange

endcmap
CMapName currentdict /CMap defineresource pop
end
end
```

通过将字符与字形完全解耦，CMap 文件不仅支持一对一的直接寻址，更通过垂直变体（`V` 系列 CMap）与竖排度量表实现了无缝的纵向书写切换。
---

## C.7 CFF 字典键值与二进制操作码权威词典

在 CFF 容器中，所有的属性字典（Top DICT 与 Private DICT）均采用极其紧凑的**逆波兰键值字节码**存储：操作数（数值）在前，操作符（Operator）在后。单字节操作符占用 `0..21`（除 12 外），双字节操作符以 `12` 开头。

### 1. Top DICT 核心操作符全集：

| 操作符字节（Hex） | 键名（Key Name） | 参数类型 | 默认值 | 语义与排印功能 |
| :--- | :--- | :--- | :--- | :--- |
| `0x00 (0)` | `version` | SID (String ID) | 无 | 字体版本字符串索引 |
| `0x01 (1)` | `Notice` | SID | 无 | 版权声明字符串索引 |
| `0x02 (2)` | `FullName` | SID | 无 | 人机可读全名字串索引 |
| `0x03 (3)` | `FamilyName` | SID | 无 | 字体家族名称索引 |
| `0x04 (4)` | `Weight` | SID | 无 | 字重描述（如 "Bold"） |
| `0x05 (5)` | `FontBBox` | 4 个数值 | `0 0 0 0` | 全字体极限全局包围盒 `[llx lly urx ury]` |
| `0x0D (13)` | `UniqueID` | 整数 | 无 | PostScript 全局缓存唯一 ID |
| `0x0E (14)` | `XUID` | 数组 | 无 | 扩展唯一 ID 序列（用于 PDF 嵌入缓存） |
| `0x0F (15)` | `charset` | 偏移量 (offset) | 0 (ISO-Adobe) | 字形字符集映射表相对于 CFF 表首的字节偏移 |
| `0x10 (16)` | `Encoding` | 偏移量 (offset) | 0 (StandardEncoding) | 字符编码表相对于 CFF 表首的字节偏移 |
| `0x11 (17)` | `CharStrings` | 偏移量 (offset) | 无 | **核心指针**：字形 Type 2 轮廓索引表的字节偏移 |
| `0x12 (18)` | `Private` | 长度与偏移量 | 无 | **神经中枢**：私有微调字典的字节长度与其起始偏移 |
| `0x0C 0x01` | `isFixedPitch` | 布尔值 | `false (0)` | 是否为等宽字体 |
| `0x0C 0x02` | `ItalicAngle` | 数值 | `0.0` | 斜体倾斜角度 |
| `0x0C 0x03` | `UnderlinePosition` | 数值 | `-100` | 下划线垂直基准线位置 |
| `0x0C 0x04` | `UnderlineThickness` | 数值 | `50` | 下划线推荐物理厚度 |
| `0x0C 0x07` | `FontMatrix` | 6 元素数组 | `[0.001 0 0 0.001 0 0]` | 归一化仿射变换矩阵 |
| `0x0C 0x1E` | `ROS` | 3 个 SID | 无 | **CIDFont 专属**：Registry、Ordering 与 Supplement 三元组 |
| `0x0C 0x1F` | `CIDFontVersion` | 数值 | `0` | CID 字体版本号 |
| `0x0C 0x24` | `FDArray` | 偏移量 | 无 | **CIDFont 专属**：子字体字典索引表（Font DICT INDEX）偏移 |
| `0x0C 0x25` | `FDSelect` | 偏移量 | 无 | **CIDFont 专属**：字形到子字体分类映射表偏移 |

---

### 2. Private DICT 核心操作符全集：

| 操作符字节（Hex） | 键名（Key Name） | 参数类型 | 默认值 | 语义与光栅化控制功能 |
| :--- | :--- | :--- | :--- | :--- |
| `0x06 (6)` | `BlueValues` | 偶数个增量数组 | 无 | 主对齐带（包含基线下沉与上冲对齐区间） |
| `0x07 (7)` | `OtherBlues` | 偶数个增量数组 | 无 | 辅助对齐带（包含降部底部对齐区间） |
| `0x08 (8)` | `FamilyBlues` | 偶数个增量数组 | 无 | 家族共享主对齐带 |
| `0x09 (9)` | `FamilyOtherBlues`| 偶数个增量数组 | 无 | 家族共享辅助对齐带 |
| `0x0A (10)` | `StdHW` | 数值 | 无 | 标准水平主笔画宽度 |
| `0x0B (11)` | `StdVW` | 数值 | 无 | 标准垂直主笔画宽度 |
| `0x0C 0x09` | `BlueScale` | 浮点数 | `0.039625` | 对齐带随字号放大时解除吸附的阈值系数 |
| `0x0C 0x0A` | `BlueShift` | 数值 | `7` | 超出对齐带多少单位后强制取消对齐的突变阈值 |
| `0x0C 0x0B` | `BlueFuzz` | 数值 | `1` | 对齐带边界容错扩展像素 |
| `0x0C 0x0C` | `StemSnapH` | 递增数组 | 无 | 允许吸附对齐的多级水平笔画宽度候选表 |
| `0x0C 0x0D` | `StemSnapV` | 递增数组 | 无 | 允许吸附对齐的多级垂直笔画宽度候选表 |
| `0x0C 0x0E` | `ForceBold` | 布尔值 | `false` | 小字号极小分辨率下是否强行加粗细笔画 |
| `0x0C 0x11` | `LanguageGroup` | 整数 | `0` | 语言群组代码（0: 拉丁系; 1: 中日韩繁复汉字系） |
| `0x0C 0x13` | `Subrs` | 偏移量 | 无 | 本私有字典专属的局部子程序池偏移（Local Subrs） |
| `0x14 (20)` | `defaultWidthX` | 数值 | `0` | 全字库大多数字符共享的默认水平字宽 |
| `0x15 (21)` | `nominalWidthX` | 数值 | `0` | 字宽差分基数（实际字宽 = 存储增量 + nominalWidthX） |

---

### 3. Type 2 CharStrings 颠覆性指令全集权威字典

Type 2 彻底优化了 Type 1 指令流的冗余。其操作码体系更加高效紧凑：

#### 堆栈算术与逻辑运算指令：
* `0x0C 0x03 (and)`：逻辑与；
* `0x0C 0x04 (or)`：逻辑或；
* `0x0C 0x05 (not)`：逻辑非；
* `0x0C 0x09 (abs)`：绝对值；
* `0x0C 0x0A (add)`：加法；
* `0x0C 0x0B (sub)`：减法；
* `0x0C 0x0C (div)`：除法；
* `0x0C 0x0E (neg)`：求负数；
* `0x0C 0x0F (eq)`：相等判定；
* `0x0C 0x1A (sqrt)`：开平方；
* `0x0C 0x18 (drop)`：丢弃栈顶元素；
* `0x0C 0x1B (dup)`：复制栈顶；
* `0x0C 0x1C (exch)`：交换栈顶两元素；
* `0x0C 0x1D (index)`：提取指定深度操作数；
* `0x0C 0x1E (roll)`：操作数栈循环滚动；
* `0x0C 0x14 (put)`：将数值存入暂存数组槽位 $i$；
* `0x0C 0x15 (get)`：从暂存数组槽位 $i$ 提取数值压栈；
* `0x0C 0x16 (ifelse)`：条件三目选择运算。

#### 提示掩码指令（`hintmask` 与 `cntrmask`）：
* **操作码 `0x13 (19)` (`hintmask`)**：
  在一条字形轮廓中，若首先声明了 $H$ 条水平提示与 $V$ 条垂直提示，则提示总数为 $N = H + V$。
  紧随 `hintmask` 操作码之后，直接内嵌 $\lceil N / 8 \rceil$ 个字节的二进制位掩码！
  每一个位（Bit）对应一条提示：若第 $k$ 位为 1，则指示当前轮廓从此时此刻起，瞬间激活第 $k$ 号提示；若为 0 则静默禁用该提示。
  这使得包含数十条复杂笔画的汉字（如“囊”、“龘”）能够在单个字符内部自由切分局部微观几何，且额外字节开销极其微小！
* **操作码 `0x14 (20)` (`cntrmask`)**：
  专门用于声明笔画中轴线与内部对称留白（Counter）的排他性约束，保证在超低分辨率下小写字母 'm' 的两个拱门或汉字“三”的三条间隙均匀等距。

---

### 4. 工业级 CFF INDEX 解析器 Python 实现

```python
import struct

class CFFIndex:
    def __init__(self, data: bytes, offset: int = 0):
        self.count, = struct.unpack(">H", data[offset:offset+2])
        self.items = []
        if self.count == 0:
            self.total_size = 2
            return
            
        self.off_size = data[offset+2]
        offsets_start = offset + 3
        offsets_count = self.count + 1
        
        # 动态解析 1 到 4 字节的变宽偏移量
        raw_offsets = []
        for i in range(offsets_count):
            pos = offsets_start + i * self.off_size
            chunk = b'\x00' * (4 - self.off_size) + data[pos:pos+self.off_size]
            val, = struct.unpack(">I", chunk)
            raw_offsets.append(val)
            
        data_base = offsets_start + offsets_count * self.off_size - 1
        for i in range(self.count):
            item_start = data_base + raw_offsets[i]
            item_end = data_base + raw_offsets[i+1]
            self.items.append(data[item_start:item_end])
            
        self.total_size = (offsets_start + offsets_count * self.off_size + raw_offsets[-1] - 1) - offset

    def __len__(self):
        return self.count

    def __getitem__(self, idx):
        return self.items[idx]
```

通过这一套高度浓缩、架构统一的现代矢量二进制规范，PostScript CFF 体系在维持了 Type 1 极致平滑的三次贝塞尔曲线与高级提示的同时，将全字库体积削减了 40% 以上，成为了当今印刷出版工业无可争议的矢量基石。
---

## C.8 多重母版字体（Multiple Master）动态实例生成实战

在 PostScript 解释器内部，用户可以通过动态混合（Blend）直接派生出全新的物理字体实例：

```postscript
% 查找基础多重母版字体
/MinionMM findfont

% 在二维设计空间中定义归一化插值坐标：
% 字重轴权重 0.45 (Light到Black之间)，字宽轴权重 0.80 (紧缩到宽体之间)
[0.45 0.80] makeblendedfont

% 将生成的派生字体注册为全局字体
/Minion-Custom findfont
12 scalefont
setfont

% 在页面上排版输出
100 700 moveto
(Voile Magic Library: Multiple Master Dynamic Instance) show
showpage
```

### 线性与非线性空间插值微积分：
在实际工程中，字体设计师往往要求插值不是简单的线性渐变，而是遵循视觉平衡曲线。Adobe MM 引入了 `NormalizeDesignVector` 映射函数：
对于设计轴输入坐标 $d_j \in [D_{j, \min}, D_{j, \max}]$，通过分段线性查找表将其非线性映射为归一化混合标量 $w_j \in [0, 1]$，再通过 Kronecker 积计算最终的 $2^k$ 个极端母版加权矩阵：

$$\mathbf{W} = \bigotimes_{j=1}^k \begin{pmatrix} 1 - w_j \\ w_j \end{pmatrix}$$

这一数学框架，成为了二十五年后现代 OpenType 1.8 矢量可变字体（Variable Fonts / Variations `fvar`, `gvar`, `HVAR`, `MVAR`）的理论祖先！

---

## C.9 东亚巨型字符集 ROS（Registry-Ordering-Supplement）全景谱系

在 CID-keyed 字体体系中，字符集的版本与规模由 **ROS 三元组** 严格定义：

| 字符集集合名称 | 适用的文字与国家/地区 | 字符总数 (Supplement) | 核心涵盖范围与标准 |
| :--- | :--- | :--- | :--- |
| **Adobe-Japan1-6** | 日文（汉字 Kanji、平假名、片假名） | 23,058 字形 (Supp 6) | JIS X 0208, JIS X 0213, JIS X 0212, 印刷用人名汉字变体、纵排变体 |
| **Adobe-GB1-5** | 中国大陆简体中文 | 30,284 字形 (Supp 5) | GB 2312, GB 13000.1, GBK, GB 18030-2000, 繁体字及少数民族拼音 |
| **Adobe-CNS1-7** | 中国台湾/香港繁体中文 | 19,088 字形 (Supp 7) | Big5, Big-5E, CNS 11643 第 1-15 字母字面、香港增补字符集 (HKSCS) |
| **Adobe-Korea1-2** | 韩国与朝鲜谚文（Hangul）及汉字 | 18,352 字形 (Supp 2) | KS X 1001, KS X 1002, 常用谚文音节块及韩国古汉字 |

每一个 Supplement 保持绝对的**向后单调递增兼容性**：新版本仅在数组末尾追加全新的 CID 编号，绝不修改或删除既有的历史 CID，彻底杜绝了跨版本文档重新排版时的文字跑位风险！
---

## C.10 CFF 规范前 391 个预定义标准字符串（Standard Strings）架构

在 CFF 容器中，为了极致压缩字体体积，Adobe 在标准规范（Adobe Technical Note #5176）中硬编码固化了 **391 个最常用的全语言字形名称字符串**。在 `Top DICT`、`Private DICT` 或字形名称寻址中：
* 任何 String ID（SID）若落在 `0 <= SID <= 390` 之间，**完全不需要在字体文件的 `String INDEX` 中占用任何字节**！解码引擎直接在静态标准字符串数组中查表；
* 自定义字形名称（如汉字 GID、私有合字）的 SID 从 391 开始分配，实际存储在 `String INDEX` 中的物理索引为 $\text{CustomSID} = \text{SID} - 391$。

### 核心标准字符串索引分布表（节选）：

| SID 范围 | 代表性字形符号名称 | 用途与排印归属 |
| :--- | :--- | :--- |
| `0` | `.notdef` | 缺失字符默认外观 |
| `1..10` | `space`, `exclam`, `quotedbl`, `numbersign`, `dollar`, `percent`, `ampersand`, `quoteright`, `parenleft`, `parenright` | 基础 ASCII 标点符号 |
| `11..26` | `asterisk`, `plus`, `comma`, `hyphen`, `period`, `slash`, `zero`..`nine` | 运算符与阿拉伯数字 |
| `27..52` | `A` 至 `Z` | 大写拉丁英文字母 |
| `53..78` | `a` 至 `z` | 小写拉丁英文字母 |
| `96..145` | `Agrave`, `Aacute`, `Acircumflex`, `Atilde`, `Adieresis`, `Aring`, `Ccedilla`, `Egrave`, `Eacute`, `Igrave`, `Ntilde`, `Oacute`, `Uacute` | 西欧重音大写字母 |
| `146..195` | `agrave`, `aacute`, `acircumflex`, `atilde`, `adieresis`, `aring`, `ccedilla`, `egrave`, `eacute`, `igrave`, `ntilde`, `oacute`, `uacute` | 西欧重音小写字母 |
| `196..250` | `fi`, `fl`, `dotlessi`, `grave`, `acute`, `circumflex`, `tilde`, `macron`, `breve`, `dotaccent`, `dieresis`, `ring`, `cedilla`, `hungarumlaut`, `ogonek` | 经典拉丁连字与独立变音符 |
| `251..390` | `Euro`, `trademark`, `perthousand`, `bullet`, `copyright`, `registered`, `ellipsis`, `dagger`, `daggerdbl`, `guillemotleft`, `guillemotright` | 国际通用货币符号与出版商印刷符号 |

通过这一天才设计，全套包含西欧 200 多个拉丁字符的 CFF 字体，其 `String INDEX` 内部往往**仅需存储家族名称与字型版本两个短字串**，字符串表体积被压缩至令人惊叹的 20 字节以内！

---

## C.11 复杂符号 Type 1 CharStrings 真实字节码反汇编跟踪（以字符 '$' 为例）

货币美元符号 `$` 是字体设计中几何复杂度最高的符号之一：它由一个平滑双重弯曲的 'S' 形曲线躯干与一到两条垂直贯穿的主干立柱构成，在有限的铅字空间中存在多达 4 条水平提示与 4 条垂直提示。

以下为一段真实的 Type 1 解密字节码指令序列及其物理执行过程：

```postscript
% 1. 设置水平左侧轴承为 50，前进字宽为 500
50 500 hsbw

% 2. 声明字符上半部分的初始水平与垂直提示
% 顶部横弧 (y=650, dy=40) 与 中部横梁 (y=360, dy=35)
650 40 360 35 hstem
% 左右垂直干提示 (x=230, dx=40)
230 40 vstem

% 3. 绘制顶部衬线与第一段曲线
230 650 rmoveto
40 hlineto
-15 -30 -40 -35 -80 -40 rrcurveto

% 4. 触发动态提示替换 (Hint Substitution)
% 抹除上半部提示，激活中腰与下半部的全新笔画提示集合！
1 3 callothersubr pop
150 40 hstem % 底部横弧提示
210 40 vstem % 下干提示

% 5. 继续绘制穿越中腰的平滑反向曲线
-30 -20 -40 -30 -30 -60 rrcurveto
0 -50 vlineto
closepath

% 6. 终结绘制，提交光栅缓冲区
endchar
```

在执行 `callothersubr 3` 的瞬间，光栅化引擎重置几何对齐网格，使美元符号上下两个封闭线圈在低分辨率下互不干涉，完美维持了对称饱满的印刷轮廓。
---

## C.12 Type 0 复合字体 FMapType 寻址算法与映射模式全集

在 Type 0 复合字体中，顶层字体维护一个 `FDepVector`（子字体依赖向量）数组，并通过 `FMapType` 整数代码指示解释器如何对多字节文本流进行分词与寻址：

| FMapType 代码 | 映射模式名称 | 输入字节流分词机制 | 子字体索引与内部字符映射算法 |
| :--- | :--- | :--- | :--- |
| **`2`** | 8/8 映射（两字节对称） | 严格按 2 字节（双字节）切分 | 高字节作为 `FDepVector` 索引选择子字体，低字节在该子字体中提取字符 |
| **`3`** | 8/16 映射（单双字节混合） | 首字节若为 `EscChar` 则消耗两字节 | 用于西文 ASCII 与日文半角/全角混合排版，动态切换单字节与双字节子字库 |
| **`4`** | 16/16 映射（四字节大字符集）| 严格按 4 字节切分 | 前双字节选择子字体，后双字节在子字体内部寻址（用于超早期 CNS 繁体大字库） |
| **`8`** | Shift-JIS 专用硬件映射 | 依据 Shift-JIS 编码范围智能分词 | 首字节若落在 `0x81..0x9F` 或 `0xE0..0xFC`，自动判定为双字节并执行高低字节解包 |
| **`9`** | Big5 繁体中文专用映射 | 依据 Big5 高字节范围智能分词 | 首字节若落在 `0xA1..0xFE`，自动抓取次字节并映射至对应的繁体字形子字库 |

尽管 Type 0 架构在 1990 年代初有效支撑了东亚桌面出版的起步，但其复杂的树状解析与割裂的子字库度量，最终促使 Adobe 在 1993 年推出了架构更加扁平、纯粹且强大的 CID-keyed 字体体系。
