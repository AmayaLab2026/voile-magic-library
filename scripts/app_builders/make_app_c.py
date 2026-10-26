# -*- coding: utf-8 -*-
"""
Generator for Expanded Appendix C (build_app_c.py)
Target: ~30,000 characters
"""

content = r'''# -*- coding: utf-8 -*-
"""
Appendix C: PostScript Font Formats
Unabridged 1:1 Reference Manual
Comprehensive expansion covering all PostScript, CFF, MM, Type 0, CIDFont architectures
Target: ~30,000 characters
All 17 figures embedded.
"""

def get_appendix_c():
    return r"""# 附录 C：PostScript 体系字体格式深度参考（Type 1, Type 2/CFF, MM, Type 0, CIDFont）

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
    """
    PostScript Type 1 线性同余解密算法
    key = 52845 (eexec) 或 4330 (CharStrings)
    """
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
    """
    PostScript Type 1 线性同余加密算法
    """
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
"""
'''

with open('scripts/app_builders/build_app_c.py', 'w', encoding='utf-8') as f:
    f.write(content)
print("Successfully written scripts/app_builders/build_app_c.py")
