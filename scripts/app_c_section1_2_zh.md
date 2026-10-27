## C.1 PostScript 页面描述语言技术导论（Introduction to the PostScript Language）

自 1985 年首款激光打印机（Apple LaserWriter）面世以来，PostScript 语言迅速风靡了整个计算机世界——从印刷工业级的出版物制作，到企业办公与个人文档打印，它无处不在。在本附录中，我们将详细剖析 PostScript 体系的各类字体格式：首当其冲的自然是 Type 1，此外还包括 Type 3、Type 42、Type 0、CID 架构、多重母版（Multiple Master）以及紧凑字体格式 CFF/Type 2。

在剖析具体的字体二进制容器与轮廓格式之前，我们必须首先对 PostScript 语言进行精要而严谨的技术导引。这门导引对于理解字体内部所使用的语法结构、算子操作模型以及字形对象的操纵本质至关重要。需要说明的是，本节并不企图面面俱到地替代厚达 912 页的官方《PostScript 语言参考手册》（*PostScript Language Reference*, 俗称红皮书）[24]；我们的核心宗旨在于直击要害，为排印工程师建立扎实的语言心智模型。

### C.1.1 语法范式与逆波兰栈式机（Syntax）

PostScript 是一门纯粹的**解释型、栈式、后缀表达式（Postfix / Reverse Polish Notation, RPN）**编程语言。其基本语法规则由空白字符（空格、制表符、换行符）分隔的**词元（Tokens）**构成，以 `%` 开头的行视为注释。

当解释器扫描到一个词元时：
- 若词元代表一个字面常量（如整数、实数、字符串），解释器将其直接压入**操作数栈（Operand Stack）**；
- 若词元代表一个可执行算子（Operator）或命名过程，解释器将立即执行它，该算子会从操作数栈顶弹出所需数量的操作数，执行计算后将结果重新压回栈顶。

例如，简单的数学加法 $3 + 4$ 在 PostScript 中书写为：

```postscript
3 4 add
```

计算完毕后，操作数栈顶只留下唯一的整数结果 `7`。

PostScript 支持丰富的数据类型：
1. **数值型（Numbers）**：整数（`123`）、八进制数（`8#177`）、十六进制数（`16#FF`）与实数（`3.14159`、`-1.2e-4`）；
2. **布尔型（Booleans）**：`true` 与 `false`；
3. **字符串（Strings）**：定界在圆括号中的普通字符串（如 `(Hello World)`），或定界在尖括号中的十六进制字符串（如 `<48656C6C6F>`）；
4. **名称（Names）**：
   - **字面名称（Literal Name）**：以斜杠开头的符号（如 `/Helvetica`、`/width`），自身不被立即求值，直接作为符号键名压入栈中；
   - **可执行名称（Executable Name）**：不带斜杠的标识符（如 `add`、`moveto`），被解释器在当前活动字典层级中查找并立即执行；
5. **数组（Arrays）**：由方括号定界的对象序列（如 `[ 1 2 (three) /four ]`）；
6. **过程（Procedures）**：由花括号定界的可执行代码块（如 `{ add 2 div }`），在被调用前作为整体对象保存在栈或字典中；
7. **字典（Dictionaries）**：键值对集合，驱动着 PostScript 的全局变量表与字体定义模型。

### C.1.2 物理坐标系与用户空间（The System of Coordinates）

在 PostScript 中，所有几何绘图操作均发生在一个抽象的**用户空间（User Space）**中，解释器在光栅化输出时会将其自动映射到物理设备的**设备空间（Device Space）**。

- **默认度量单位**：用户坐标系采用经典的排印**大号点（PostScript Point）**，严格定义为：
  $$1 \text{ pt} = \frac{1}{72} \text{ inch} = \frac{25.4}{72} \text{ mm} \approx 0.352778 \text{ mm}$$
- **默认原点与轴向**：默认原点 $(0, 0)$ 坐落于物理页面的**左下角**；$x$ 轴水平向右延伸，$y$ 轴垂直向上延伸。这与大多数计算机屏幕坐标系（原点在左上角、$y$ 轴向下）形成了鲜明对立。

### C.1.3 当前变换矩阵（The Current Transformation Matrix, CTM）

用户空间到物理设备空间的几何映射由一个 $3 \times 3$ 的仿射变换矩阵掌控，称为**当前变换矩阵（CTM）**。任何用户坐标 $(x, y)$ 变换为设备坐标 $(x', y')$ 的矩阵代数方程为：

$$\begin{bmatrix} x' & y' & 1 \end{bmatrix} = \begin{bmatrix} x & y & 1 \end{bmatrix} \begin{bmatrix} a & b & 0 \\ c & d & 0 \\ t_x & t_y & 1 \end{bmatrix} = \begin{bmatrix} a x + c y + t_x & b x + d y + t_y & 1 \end{bmatrix}$$

在 PostScript 中，该矩阵在内存中紧凑地表示为一个六元数组 `[a b c d tx ty]`。PostScript 提供了完整的坐标系操纵算子：
- `translate`：将原点平移 $(t_x, t_y)$，即 `tx ty translate`；
- `scale`：按比例因子 $(s_x, s_y)$ 缩放坐标系，即 `sx sy scale`；
- `rotate`：逆时针旋转 $\theta$ 角度，即 `theta rotate`；
- `concat`：将栈顶的自定义变换矩阵复合累加到当前 CTM 中；
- `matrix`：在内存中分配一个恒等变换矩阵 `[1 0 0 1 0 0]`；
- `currentmatrix` 与 `setmatrix`：获取与恢复底层 CTM。

### C.1.4 矢量路径系统（Paths）

在 PostScript 中，绘制任意几何轮廓的核心是**路径（Path）**。路径由一系列连续或离散的线段和三次贝塞尔曲线段构成。构建路径的关键算子包括：
- `newpath`：清空当前路径缓存，初始化一条全新路径；
- `moveto`（与相对位移 `rmoveto`）：抬起虚拟画笔，移动至绝对坐标 $(x, y)$，确立新的**当前点（Current Point）**；
- `lineto`（与相对位移 `rlineto`）：从当前点向目标点 $(x, y)$ 连接一条直线段；
- `curveto`（与相对位移 `rcurveto`）：从当前点 $(x_0, y_0)$ 出发，以 $(x_1, y_1)$ 与 $(x_2, y_2)$ 作为两个离线贝塞尔控制手柄，绘制平滑到达 $(x_3, y_3)$ 的**三次贝塞尔曲线段（Cubic Bézier Curve）**：
  $$B(t) = (1-t)^3 P_0 + 3(1-t)^2 t P_1 + 3(1-t) t^2 P_2 + t^3 P_3, \quad t \in [0, 1]$$
- `closepath`：从当前点向当前子路径的起始点绘制一条闭合直线，封口形成闭合轮廓；
- `pathbbox`：计算并返回当前路径的严格轴对齐外包围盒 `llx lly urx ury`；
- `clip`：将当前闭合路径设为**裁剪区域（Clipping Path）**，后续的所有绘制操作将被限制在闭合多边形内部。

### C.1.5 轮廓着色与两大填色拓扑准则（Shapes & Filling Rules）

路径构建完毕后，本身仅是一条无形数学边界；要将其固化为可见图元，需调用着色算子：
- `stroke`：使用当前描边宽度与画笔属性，沿路径轨迹绘制有宽度的墨迹；
- `fill`：按照**非零环绕数规则（Non-zero Winding Number Rule）**对闭合多边形内部进行实体填充；
- `eofill`：按照**奇偶规则（Even-Odd Rule）**对闭合多边形内部进行填充。

::: tip 深入理解两大填充法则的拓扑对立
* **非零环绕数规则（`fill`）**：从待判定的测试点向无穷远处引一条射线。初始化计数器为 0；凡是从射线左侧穿向右侧的轮廓线，计数器加 1；凡是从右侧穿向左侧的轮廓线，计数器减 1。若最终计数器的代数和不等于 0，则判定该点位于图形内部，执行着色；若等于 0，则判定为外部镂空（Counter）。**这正是 Type 1 与 TrueType 字体规范中要求外轮廓与内镂空轮廓必须严格逆向旋转的拓扑根源！**
* **奇偶规则（`eofill`）**：从测试点向无穷远引一条射线，统计与路径的所有交点总数。若交点总数为奇数，则判定在内部填充；若为偶数，则判定在外部。该规则无需关心轮廓绘制的顺时针或逆时针方向。
:::

### C.1.6 光栅位图渲染（Bitmap Images）

除了矢量路径，PostScript 还支持点阵光栅位图的精准印制：
- `imagemask`：专门用于渲染 1 位黑白单色掩码，常用于位图点阵字体的快速印制。它将单色像素阵列作为不透明与全透明的蒙版，仅在位为 1 的区域泼洒当前选定的前景色；
- `image`：用于渲染 8 位或 24 位的多级灰度与全彩照片级图像，通过传入宽度、高度、位深与矩阵解码数据流。

### C.1.7 虚拟机堆栈、数组与字典管理（Managing Stack & Dictionaries）

PostScript 解释器内部常驻三大核心堆栈：
1. **操作数栈（Operand Stack）**：暂存全部数据与算子参数；
2. **执行栈（Execution Stack）**：跟踪当前正在调用的嵌套过程与控制流；
3. **字典栈（Dictionary Stack）**：管理名称与对象绑定的作用域。

#### (1) 操作数栈操纵经典算子
- `dup`：复制栈顶元素（`x -> x x`）；
- `pop`：丢弃栈顶元素（`x -> `）；
- `exch`：交换栈顶前两个元素的位置（`x y -> y x`）；
- `copy`：复制栈顶前 $n$ 个元素；
- `index`：将栈深第 $n$ 处的元素复制一份置于栈顶（`xn ... x0 n -> xn ... x0 xn`）；
- `roll`：对栈顶 $n$ 个元素执行深度为 $j$ 的循环滚动置换；
- `clear`：清空整个操作数栈。

#### (2) 字典管理与命名空间
字典是键值对哈希表。字典栈顶部的字典称为**当前字典（Current Dictionary）**。
- `dict`：在堆内存中分配指定容量的新字典（例如 `10 dict` 创建一个容量为 10 的字典）；
- `begin`：将指定的字典压入字典栈顶，使其成为当前查找名称的第一优先作用域；
- `end`：弹出字典栈顶的字典；
- `def`：在当前字典中创建键值绑定（如 `/pi 3.14159 def`）；
- `load`：在字典栈中沿着作用域层级由顶向下搜索指定的键名并返回其绑定的对象。

### C.1.8 字体调度与排版核心指令（Font Management and Typesetting）

PostScript 将字体本身设计为一种特殊的顶层字典。排版文本的基本工作流由以下核心指令驱动：
1. `findfont`：在全局字库目录（`FontDirectory`）中按名称检索字体字典指针（如 `/Helvetica findfont`）；
2. `scalefont`：将字体的基准设计空间（通常为 1000 单位正方形）按指定字号缩放（如 `12 scalefont`，在底层自动将其 `FontMatrix` 与缩放矩阵相乘）；
3. `setfont`：将缩放后的字体安装到当前图形状态中；
4. `show`：从当前点出发，将栈顶字符串逐字渲染输出，并自动按照各字符的进深（Advance Width）步进当前点；
5. `stringwidth`：计算指定字符串在当前字体下的总体排版宽度与位移量 `(wx wy)`，但不执行任何实际墨迹绘制；
6. `charpath`：提取字符串中每一个字符的纯矢量轮廓，将其转化为当前路径，以便设计师后续调用 `stroke` 描边、`clip` 镂空或填充渐变特效！

### C.1.9 图形状态堆栈与色彩模型（The Graphics State）

为了支持模块化的绘图逻辑，PostScript 维护了**图形状态（Graphics State）**栈：
- `gsave`：将当前的全部图形属性（CTM、当前点、画笔线宽、线帽样式、裁剪路径、色彩等）打包克隆并压入图形栈顶；
- `grestore`：弹出并完全恢复上一次保存的图形上下文状态，确保子程序的局部坐标变换绝不污染全局页面。

线条与色彩控制指令包括：
- `setlinewidth`：设定描边线宽；
- `setlinecap`：设定线端端点形状（0 为平头断开，1 为圆头，2 为方形延伸方头）；
- `setlinejoin`：设定折角连接样式（0 为尖角拼接，1 为圆弧拼接，2 为斜角平切）；
- `setmiterlimit`：设定斜接限制比率，防止尖角过度延长；
- `setdash`：配置虚线模式（如 `[3 2] 0 setdash`）；
- `setgray`、`setrgbcolor`、`setcmykcolor`：分别在单通道灰度、三原色 RGB 以及四色印刷 CMYK 色彩空间中配置当前绘制墨色。

### C.1.10 文档结构规范化注释（Structured Comments / DSC）

为了让外部预检软件、排版排版解释器与打印机后台打印管理程序（Spooler）能够在不完全执行整个 PostScript 程序的情况下提取页面元数据，Adobe 制定了**文档结构规范（Document Structuring Conventions, DSC）**。这些结构化信息均以形如 `%%` 的特殊注释格式书写：
- `%!PS-Adobe-3.0`：指明该文件遵循 DSC 3.0 工业标准；
- `%%BoundingBox: llx lly urx ury`：声明整个文档所有页面的全局闭包矩形；
- `%%Pages: n`：声明文档的总页数；
- `%%Page: label ordinal`：明确标识某一特定页面的起始点（例如 `%%Page: 1 1`）；
- `%%Trailer`：进入文档的尾声收尾段落；
- `%%EOF`：文档正式终止标记。

---

## C.2 纯 PostScript 可编程字型：Type 3 字体架构（Type 3 Fonts）

在所有 PostScript 字体格式中，**Type 3** 是最为自由、最为开放、但也最缺乏光栅微调约束的一种特殊格式。与底层采用高度压缩加密字节码（CharStrings）的 Type 1 不同，Type 3 字体**直接使用正规的 PostScript 高级源码过程来定义字形**！

### C.2.1 Type 3 字体的工业优势与技术局限

- **核心优势**：
  * **完全图灵完备的自由表达**：字形描述过程可以使用几乎所有合法的 PostScript 算子！这意味着字形可以拥有全彩色渐变（Shading）、可以内嵌光栅照片（`image`）、可以动态计算随机纹理、甚至可以绘制带有可调线宽的灰度描边图元；
  * **零授权成本**：在 Type 1 加密算法被 Adobe 严密封锁的岁月里，Type 3 成为所有第三方开源编译器与 DTP 软件生成矢量字型的唯一合法途径。
- **技术局限**：
  * **无微观提示机制（No Hinting）**：Type 3 规范不具备 Type 1 专属的干预像素栅格对齐的提示算子。因此在低分辨率显示器或激光打印机的小字号排印下，字形边缘容易模糊或笔画断裂；
  * **无法享受专用硬件光栅加速器**：多数 PostScript RIP 硬件针对 Type 1 内置了极其快速的专用解密与光栅化 ASIC 芯片，而 Type 3 只能作为普通通用 PostScript 过程在解释器主循环中慢速解析。

### C.2.2 Type 3 字体字典的内部字段架构

一个标准的 Type 3 字体字典必须向解释器注册以下关键条目：

| 字典键名 | 类型 | 规范说明 |
| :--- | :---: | :--- |
| `FontType` | 整数 | **固定必须为 3**，向解释器声明此乃 Type 3 字体字典。 |
| `FontMatrix` | 数组 | 将字形设计空间转换为用户空间的仿射变换矩阵（常用 `[0.001 0 0 0.001 0 0]`，将 1000 单位的设计网格折算为 1 点）。 |
| `FontBBox` | 数组 | 容纳字库中全体字形的绝对外包围盒 `[llx lly urx ury]`。 |
| `Encoding` | 数组 | 容量固定为 256 的名称数组，将 `0-255` 编码映射为字形符号名称。 |
| `BuildGlyph` | 过程 | 现代 PostScript Level 2/3 标准驱动程序：从栈顶接收字体字典与字形名称，负责动态绘制该字形。 |
| `BuildChar` | 过程 | 早期 PostScript Level 1 兼容程序：从栈顶接收字体字典与字符编码，负责执行字形绘制。 |

### C.2.3 `setcachedevice` 与 `setcharwidth` 缓存决策

在 `BuildGlyph`（或 `BuildChar`）过程内部，字形绘制的第一步必须明确通知底层图形引擎该字形是否应当被存入 RIP 的高速字形点阵缓存（Font Cache）：

1. **`setcachedevice`（启用字形高速缓存）**：
   语法：`wx wy llx lly urx ury setcachedevice`
   通知解释器：该字形的前进量为 $(w_x, w_y)$，外包围盒为 $[ll_x, ll_y, ur_x, ur_y]$。解释器会为该字形在内存中分配一块点阵缓冲区；当相同字符再次出现时，直接拷贝光栅位图，极大提升排版吞吐率。**注意：使用 `setcachedevice` 的字形内部严禁调用任何色彩算子（如 `setrgbcolor`），所有描边与填充强制继承外部文本前景色。**
2. **`setcharwidth`（禁用缓存，允许全彩与复杂动态特性）**：
   语法：`wx wy setcharwidth`
   仅向系统声明字形水平与垂直位移 $(w_x, w_y)$。系统不会缓存渲染结果，每次排版均重新执行绘制代码。**该算子专为全彩色字形、多色套印图章、以及带有随机动态算法的特殊字型量身定制！**

### C.2.4 极简 Type 3 字体纯 PostScript 源码实战范例

以下是一份完全符合工业标准的 Type 3 字体可执行 PostScript 源代码范本，它定义了一个名为 `/MinimalType3` 的字体，并在内部通过纯矢量指令手工绘制了字母 `'A'` 与 `'B'`：

```postscript
%!PS-Adobe-3.0 Resource-Font
8 dict begin
  /FontType 3 def
  /FontMatrix [0.001 0 0 0.001 0 0] def
  /FontBBox [0 0 1000 1000] def

  % 256 位编码向量初始化：默认填入 /.notdef
  /Encoding 256 array def
  0 1 255 { Encoding exch /.notdef put } for
  Encoding 65 /A put
  Encoding 66 /B put

  % 字形轮廓描述子字典
  /CharProcs 3 dict def
  CharProcs begin
    /.notdef {
      0 0 0 0 0 0 setcachedevice
    } def

    /A {
      % 进深 600，包围盒 [50 0 550 800]
      600 0 50 0 550 800 setcachedevice
      newpath
      50 0 moveto
      300 800 lineto
      550 0 lineto
      450 0 lineto
      375 250 lineto
      225 250 lineto
      150 0 lineto
      closepath
      % 内部镂空三角（逆时针绘制以实现非零环绕数镂空）
      300 600 moveto
      250 400 lineto
      350 400 lineto
      closepath
      fill
    } def

    /B {
      % 进深 650，包围盒 [50 0 600 800]
      650 0 50 0 600 800 setcachedevice
      newpath
      50 0 moveto 50 800 lineto 400 800 lineto
      550 800 600 700 600 550 curveto
      600 450 520 400 450 400 curveto
      550 400 600 350 600 200 curveto
      600 50 500 0 350 0 curveto
      closepath
      fill
    } def
  end

  % BuildGlyph 分发器
  /BuildGlyph {
    exch begin
      % 栈：glyphname
      dup CharProcs exch known {
        CharProcs exch get exec
      } {
        pop CharProcs /.notdef get exec
      } ifelse
    end
  } def

  /BuildChar {
    1 index /Encoding get exch get
    1 index /BuildGlyph get exec
  } def
currentdict end
/MinimalType3 exch definefont pop
```
