# -*- coding: utf-8 -*-
"""
Script to expand docs/zh/fonts-encodings/appendices.md to unabridged 1:1 reference manual,
incorporating figures fig-app-a*, fig-app-c*, fig-app-d*, fig-app-e*, fig-app-f*,
and preserving all 10 math blocks.
"""
import sys, re
import opencc

sys.stdout.reconfigure(encoding='utf-8')

# Read current zh appendices
with open('docs/zh/fonts-encodings/appendices.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect where to insert the figures in appendices
# Appendix A:
# fig-app-a1: Chicago font global image
# fig-app-a2: BDF bitmap and vector versions of ideographic character
# fig-app-a3: gftodvi Computer Modern Roman 10 at 5203 DPI

fig_a1 = '''
::: tip 麦金塔操作系统经典 Chicago 字体的全局条带图像（Figure A-1）
![麦金塔操作系统经典 Chicago 字体的全局条带图像（Figure A-1）](/images/fonts-encodings/fig-app-a1.png)
*麦金塔操作系统经典 Chicago 字体的全局条带图像（Figure A-1）*
:::

*图 A-1：在苹果 Macintosh 视窗菜单中服役超过 15 年的经典 Chicago 字体全局点阵条带位图（Strike Bitmap）。图中展示了包含了欧元符号（€）的现代维护版本。*
'''

fig_a2 = '''
::: tip BDF 规范中表意汉字点阵与度量属性的定义模型（Figure A-2）
![BDF 规范中表意汉字点阵与度量属性的定义模型（Figure A-2）](/images/fonts-encodings/fig-app-a2.png)
*BDF 规范中表意汉字点阵与度量属性的定义模型（Figure A-2）*
:::

*图 A-2：Adobe BDF 规范对单个汉字表意文字点阵像素阵列与外包围盒、基线偏移、字距步进向量的完整定义模型。*
'''

fig_a3 = '''
::: tip gftodvi 在 5,203 DPI 超高分辨率下渲染的 Computer Modern 字母排印图（Figure A-3）
![gftodvi 在 5,203 DPI 超高分辨率下渲染的 Computer Modern 字母排印图（Figure A-3）](/images/fonts-encodings/fig-app-a3.png)
*gftodvi 在 5,203 DPI 超高分辨率下渲染的 Computer Modern 字母排印图（Figure A-3）*
:::

*图 A-3：高德纳开发的大师级公用程序 `gftodvi` 将 GF 点阵字库逆向转化为 DVI 文件的排印样张（Computer Modern Roman 10 磅在 5,203 DPI 下的精细点阵剖析）。*
'''

fig_c1 = '''
::: tip PostScript 路径构建与填充代码（Figure C-1）
![PostScript 路径构建与填充代码（Figure C-1）](/images/fonts-encodings/fig-app-c1.png)
*PostScript 路径构建与填充代码（Figure C-1）*
:::

*图 C-1：PostScript 语言底层路径构建与填充执行指令。*
'''

fig_c2 = '''
::: tip 非零缠绕数规则与奇偶环绕规则的物理填充对比（Figure C-2）
![非零缠绕数规则与奇偶环绕规则的物理填充对比（Figure C-2）](/images/fonts-encodings/fig-app-c2.png)
*非零缠绕数规则与奇偶环绕规则的物理填充对比（Figure C-2）*
:::

*图 C-2：左侧三图展示非零环绕数规则（Nonzero Winding Number Rule），右侧三图展示奇偶填充规则（Even-Odd Rule）对自相交复杂路径的填充判定。*
'''

fig_c7 = '''
::: tip 跨文种字符度量高度与超逸（Overshoot）全景（Figure C-7）
![跨文种字符度量高度与超逸（Overshoot）全景（Figure C-7）](/images/fonts-encodings/fig-app-c7.png)
*跨文种字符度量高度与超逸（Overshoot）全景（Figure C-7）*
:::

*图 C-7：Omega Serif 字体中拉丁文、阿拉伯文、希伯来文与亚美尼亚文多种复杂文字的基准高度与光学超逸量分布。*
'''

fig_c9 = '''
::: tip 字母 ‘H’、‘O’、‘m’ 的对齐区与微调主干（Figure C-9）
![字母 ‘H’、‘O’、‘m’ 的对齐区与微调主干（Figure C-9）](/images/fonts-encodings/fig-app-c9.png)
*字母 ‘H’、‘O’、‘m’ 的对齐区与微调主干（Figure C-9）*
:::

*图 C-9：PostScript Type 1 字形中的水平与垂直微调主干（灰色阴影带代表 `BlueValues` 与 `OtherBlues` 对齐区）。*
'''

fig_c10 = '''
::: tip 字母 ‘B’ 中四重提示替换的执行过程（Figure C-10）
![字母 ‘B’ 中四重提示替换的执行过程（Figure C-10）](/images/fonts-encodings/fig-app-c10.png)
*字母 ‘B’ 中四重提示替换的执行过程（Figure C-10）*
:::

*图 C-10：字母 ‘B’ 内部四个局部垂直微调的动态提示替换（Hint Substitution）连续阶段。*
'''

fig_c11 = '''
::: tip PostScript Type 1 双三次贝塞尔 Flex 机制（Figure C-11）
![PostScript Type 1 双三次贝塞尔 Flex 机制（Figure C-11）](/images/fonts-encodings/fig-app-c11.png)
*PostScript Type 1 双三次贝塞尔 Flex 机制（Figure C-11）*
:::

*图 C-11：由两段三次贝塞尔曲线 $abcd$ 与 $defg$ 构成的 Flex 弹性微调结构。*
'''

fig_c12 = '''
::: tip 汉字 “講” 与 “皿” 内部的白空主干计数控制（Figure C-12）
![汉字 “講” 与 “皿” 内部的白空主干计数控制（Figure C-12）](/images/fonts-encodings/fig-app-c12.png)
*汉字 “講” 与 “皿” 内部的白空主干计数控制（Figure C-12）*
:::

*图 C-12：PostScript Type 1 与 Type 2 面向东亚复杂表意文字的白空主干计数控制（Counter Control）。*
'''

fig_c16 = '''
::: tip CIDFont（Type 0）整体解引用架构（Figure C-16）
![CIDFont（Type 0）整体解引用架构（Figure C-16）](/images/fonts-encodings/fig-app-c16.png)
*CIDFont（Type 0）整体解引用架构（Figure C-16）*
:::

*图 C-16：CIDFont 文件基于字符集身份码（CID）从全局二进制流解引用字形数据的完整管线。*
'''

fig_d1 = '''
::: tip EBLC 点阵表中字形的水平与垂直度量（Figure D-1）
![EBLC 点阵表中字形的水平与垂直度量（Figure D-1）](/images/fonts-encodings/fig-app-d1.png)
*EBLC 点阵表中字形的水平与垂直度量（Figure D-1）*
:::

*图 D-1：TrueType EBLC 表中内嵌点阵字形的水平与垂直排版度量定义。*
'''

fig_d3 = '''
::: tip Verdana 字体 letter ‘A’ 在 gasp 表控制下的栅格尺寸分布（Figure D-3）
![Verdana 字体 letter ‘A’ 在 gasp 表控制下的栅格尺寸分布（Figure D-3）](/images/fonts-encodings/fig-app-d3.png)
*Verdana 字体 letter ‘A’ 在 gasp 表控制下的栅格尺寸分布（Figure D-3）*
:::

*图 D-3：微软经典屏幕字体 Verdana 在 `gasp` 表控制下，平滑抗锯齿与网格微调随 ppem 尺寸的动态阶梯切换。*
'''

fig_d6 = '''
::: tip CastleType 的 202 个花体 Ampersand 字符全景（Figure D-6）
![CastleType 的 202 个花体 Ampersand 字符全景（Figure D-6）](/images/fonts-encodings/fig-app-d6.png)
*CastleType 的 202 个花体 Ampersand 字符全景（Figure D-6）*
:::

*图 D-6：CastleType 字体工坊制作的 202 个极具书法美感的 Ampersand（&）连字变体。*
'''

fig_d8 = '''
::: tip Apple Skia 字体在 wght 轴上的连续变形全景（Figure D-8）
![Apple Skia 字体在 wght 轴上的连续变形全景（Figure D-8）](/images/fonts-encodings/fig-app-d8.png)
*Apple Skia 字体在 wght 轴上的连续变形全景（Figure D-8）*
:::

*图 D-8：苹果 AAT 经典可变字体 Skia 在字重（`wght`）轴上的平滑连续渐变插值。*
'''

fig_e1 = '''
::: tip Courier 字体在 TrueType 虚拟机下的指令控制点阵（Figure E-1）
![Courier 字体在 TrueType 虚拟机下的指令控制点阵（Figure E-1）](/images/fonts-encodings/fig-app-e1.png)
*Courier 字体在 TrueType 虚拟机下的指令控制点阵（Figure E-1）*
:::

*图 E-1：苹果/Bitstream Courier 字体大写字母 ‘T’ 在 TrueType 指令系统控制下的网格微调与对齐点。*
'''

fig_e2 = '''
::: tip Verdana 字母 ‘O’ 在 MIRP 指令控制下的轮廓拟合（Figure E-2）
![Verdana 字母 ‘O’ 在 MIRP 指令控制下的轮廓拟合（Figure E-2）](/images/fonts-encodings/fig-app-e2.png)
*Verdana 字母 ‘O’ 在 MIRP 指令控制下的轮廓拟合（Figure E-2）*
:::

*图 E-2：微软 Verdana 字体大写 ‘O’ 在指令 `MIRP[10110]` 控制下对 CVT 参考值与轮廓点距的锁定。*
'''

fig_f1 = '''
::: tip METAFONT 原始 Computer Modern 字体家族谱系（1/2）（Figure F-1）
![METAFONT 原始 Computer Modern 字体家族谱系（1/2）（Figure F-1）](/images/fonts-encodings/fig-app-f1.png)
*METAFONT 原始 Computer Modern 字体家族谱系（1/2）（Figure F-1）*
:::

*图 F-1：高德纳原始 Computer Modern 字体家族全集谱系（前半部）。*
'''

# Now let's carefully insert these figures into zh text
# Replace or insert into sections:
text = text.replace('### 1. `FONT` 与 `NFNT` 资源头结构', fig_a1 + '\n### 1. `FONT` 与 `NFNT` 资源头结构')
text = text.replace('### 3. Unix 与 X11 体系：Adobe BDF 与 PCF 格式', fig_a2 + '\n### 3. Unix 与 X11 体系：Adobe BDF 与 PCF 格式')
text = text.replace('### 1. GF（Generic Font）格式', fig_a3 + '\n### 1. GF（Generic Font）格式')

text = text.replace('## C.1 PostScript 语言执行机与图形状态', '## C.1 PostScript 语言执行机与图形状态\n' + fig_c1 + '\n' + fig_c2)
text = text.replace('### Type 1 CharString 核心操作码全集', fig_c7 + '\n' + fig_c9 + '\n' + fig_c10 + '\n' + fig_c11 + '\n### Type 1 CharString 核心操作码全集')
text = text.replace('## C.3 CFF（Compact Font Format）与 Type 2 CharStrings', '## C.3 CFF（Compact Font Format）与 Type 2 CharStrings\n' + fig_c12 + '\n' + fig_c16)

text = text.replace('## D.2 核心基础数据表详解', '## D.2 核心基础数据表详解\n' + fig_d1 + '\n' + fig_d3)
text = text.replace('### 2. 覆盖表（Coverage Table）与类定义表（ClassDef Table）', '### 2. 覆盖表（Coverage Table）与类定义表（ClassDef Table）\n' + fig_d6 + '\n' + fig_d8)

text = text.replace('## E.2 画笔（Pens）与包络线理论', '## E.2 画笔（Pens）与包络线理论\n' + fig_f1)
text = text.replace('## F.2 核心指令全集分类字典', '## F.2 核心指令全集分类字典\n' + fig_e1 + '\n' + fig_e2)

# Ensure translator line
text = re.sub(r'\*?译者：.*?\n', '*译者：[Lycoris \\<lycorismisaka@gmail.com\\>](mailto:lycorismisaka@gmail.com)*\n\n', text)

with open('docs/zh/fonts-encodings/appendices.md', 'w', encoding='utf-8') as f:
    f.write(text)

print(f"docs/zh/fonts-encodings/appendices.md updated: {len(text)} chars")

# Mirror to zh-hant
converter = opencc.OpenCC('s2twp')

def convert_preserving(t):
    code_blocks = []
    def code_repl(m):
        code_blocks.append(m.group(0))
        return f"__CODE_BLOCK_{len(code_blocks)-1}__"
    t = re.sub(r'```[\s\S]*?```', code_repl, t)

    math_blocks = []
    def math_repl(m):
        math_blocks.append(m.group(0))
        return f"__MATH_BLOCK_{len(math_blocks)-1}__"
    t = re.sub(r'\$\$[\s\S]*?\$\$', math_repl, t)

    inline_math = []
    def inline_repl(m):
        inline_math.append(m.group(0))
        return f"__INLINE_MATH_{len(inline_math)-1}__"
    t = re.sub(r'\$[^\$\n]+?\$', inline_repl, t)

    converted = converter.convert(t)

    for i, im in enumerate(inline_math):
        converted = converted.replace(f"__INLINE_MATH_{i}__", im)
    for i, mb in enumerate(math_blocks):
        converted = converted.replace(f"__MATH_BLOCK_{i}__", mb)
    for i, cb in enumerate(code_blocks):
        converted = converted.replace(f"__CODE_BLOCK_{i}__", cb)

    return converted

zh_hant = convert_preserving(text)
zh_hant = zh_hant.replace('*譯者：[Lycoris <lycorismisaka@gmail.com>]', '*譯者：[Lycoris \\<lycorismisaka@gmail.com\\>]')

with open('docs/zh-hant/fonts-encodings/appendices.md', 'w', encoding='utf-8') as f:
    f.write(zh_hant)

print(f"docs/zh-hant/fonts-encodings/appendices.md updated: {len(zh_hant)} chars")
