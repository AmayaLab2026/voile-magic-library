# -*- coding: utf-8 -*-
"""
Expander for Appendix C: PostScript Font Formats
Appends comprehensive binary structs for CFF, Type 2 CharStrings, MM, and CIDFont/CMap
Target: ~28,000 characters
"""

extra_c = r"""
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
"""

# Let's read app_c.md, append extra_c and write it back
with open('scripts/app_builders/app_c.md', 'r', encoding='utf-8') as f:
    text_c = f.read()

full_c = text_c.strip() + '\n' + extra_c.strip() + '\n'

with open('scripts/app_builders/app_c.md', 'w', encoding='utf-8') as f:
    f.write(full_c)

print("Successfully expanded scripts/app_builders/app_c.md, total length:", len(full_c))

# Update build_app_c.py
py_c = """# -*- coding: utf-8 -*-
import os

def get_appendix_c():
    p = os.path.join(os.path.dirname(__file__), 'app_c.md')
    with open(p, 'r', encoding='utf-8') as f:
        return f.read()
"""
with open('scripts/app_builders/build_app_c.py', 'w', encoding='utf-8') as f:
    f.write(py_c)
print("Updated build_app_c.py")
