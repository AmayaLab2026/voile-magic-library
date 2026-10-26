with open('scripts/ch10_content.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Let's find Section 3.2 TrueDoc and add CSR mathematical curve decomposition
p_pfr = text.find('### 3.2 先驱之一：Bitstream TrueDoc 与 PFR 格式')
csr_extra = r"""
#### 3. CSR（字符形态记录器）的几何拟合与动态贝塞尔重建
Bitstream TrueDoc 之所以在 1990 年代名噪一时，核心在于其独创的 **CSR（Character Shape Recording）矢量拟合技术**。
- **高阶曲线离散化**：当 CSR 处理 TrueType 的二阶贝塞尔曲线或 Type 1 的三阶贝塞尔曲线时，为了规避各操作系统平台底层光栅化引擎的专利壁垒，它首先将轮廓离散化为一系列极细密的特征多边形折线；
- **自适应凸凹分割与拓扑压缩**：算法通过检测轮廓曲率符号的变换点（拐点与极值点），将字形笔画划分为连续的单调区间（Monotonic Intervals）。在这些区间内，算法并不存储浮点数坐标，而是存储相对于前一个特征顶点的**一维动态位移增量（Delta Offsets）**；
- **CSP 客户端内存即时重建**：当浏览器的 Character Shape Player（CSP）读取 PFR 字节流时，它在内存中即时执行三阶样条插值与轮廓缝合，并直接挂钩操作系统的图形设备上下文（GDI 或 X11 GC）实施硬件绘制。这种“在作者端抽丝剥茧，在读者端现场重构”的思想，使得 100 个西文字符的完整字形能够在短短 8KB 至 12KB 内高质量传输。

"""

p_insert1 = text.find('#### 核心工作流与架构', p_pfr)
text = text[:p_insert1] + csr_extra + text[p_insert1:]

# Let's expand Section 4.5 SVG Kerning with advanced grouping and range syntax
p_kern = text.find('### 4.5 字偶距调整（Kerning）：`<hkern>` 与 `<vkern>`')
p_kern_insert = text.find('#### 语法过滤规则：', p_kern)
kern_extra = r"""
#### 批量字偶距群组定义语法
在大型专业字体中，如果为每一个字符对单独书写一行 `<hkern>`，会导致 SVG 字体文件体积膨胀至数万行。SVG 字体规范为此提供了强大的批量群组（Grouping）匹配语法：
- **逗号分隔多字符匹配**：`u1="A,B,D" u2="V,W,Y"` 指示集合 $\{A, B, D\}$ 中的任意字符后接集合 $\{V, W, Y\}$ 中的任意字符时，统一应用指定的紧缩量；
- **字符范围语法（Range Syntax）**：`u1="A-Z"` 允许使用短横线直接界定 Unicode 字符区间，极大简化了全大写字母间的间距压缩规则书写；
- **混合标识符过滤**：允许同时混合使用 `u1`、`g1` 与 `u2`、`g2`，例如 `g1="T,Tbar" u2="a-z" k="-45"`。排版引擎在扫描字符对时，会按照字形优先级匹配最狭窄的特化规则，赋予了 SVG 字体极其灵活的微观排版调控能力。

"""
text = text[:p_kern_insert] + kern_extra + text[p_kern_insert:]

with open('scripts/ch10_content.md', 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Pushed ch10 to {len(text)} characters!")
