# -*- coding: utf-8 -*-
"""
Enriches app_a.md with DOS CPI complete binary structures and PCF chunk directory.
Target: ~20,000 characters
"""

extra_a_2 = r"""
---

## A.6 DOS 代码页信息文件（`.CPI`）的段落拓扑与显卡固件注入

在微软 MS-DOS 与 IBM PC-DOS 时代，操作系统为了在 EGA 与 VGA 图形显示适配器上切换不同的国家/地区字符集（如代码页 437 美国英语、850 西欧多语言、936 简体中文），采用了专有的 **`.CPI`（Code Page Information）** 点阵字体封装容器。

### 1. CPI 文件的四级二进制树状拓扑：
一个标准的 `.CPI` 文件在物理上由四大层级构成：
1. **Font File Header（字体文件头）**：
   * `0x19` 字节魔数：`\xFF\x46\x4F\x4E\x54\x20\x20`（"FONT  "）；
   * 预留字段与版本号；
   * `pCodePageEntry`：指向首个代码页条目的文件绝对字节偏移。
2. **Code Page Entry Header（代码页条目头）**：
   * `next`：指向下一个代码页条目的指针（为 0 表示链表末尾）；
   * `device_type`：目标硬件设备代码（1: 屏幕显示适配器 Screen; 2: 针式/激光打印机 PRN）；
   * `device_name`：8 字节 ASCII 设备名称（如 `"EGA     "` 或 `"4201    "`）；
   * `codepage_id`：DOS 代码页整数编号（如 437, 850, 852）；
   * `pFontInfo`：指向具体字体信息的偏移量。
3. **Font Info Header（点阵字体信息头）**：
   * `version`：字体格式版本号；
   * `num_fonts`：该代码页下封装的不同像素规格点阵字体总数（通常为 3 种：$8 \times 8$, $8 \times 14$, $8 \times 16$）。
4. **Screen Font Data（屏幕点阵原始字节矩阵）**：
   * 存储每个字符的点阵位图。例如对于标准的 $8 \times 16$ VGA 字体，每个字符占用 16 个连续字节（每行 8 像素占用 1 字节）。256 个字符恰好占用：
     $$256 \times 16 \text{ 字节} = 4096 \text{ 字节} = 4 \text{ KB}$$
   DOS 的 `MODE CON: SELECT=...` 命令正是将这 4KB 数据通过显卡 BIOS 中断（`INT 10h, AX=1100h`）直接写入 VGA 显卡的字符发生器内存平面 2（Plane 2），实现了纯硬件级的即时字符渲染！

---

## A.7 X11 PCF 二进制结构与快速加载优化

在 X Window System 诞生初期，虽然 BDF 纯文本格式极其易读，但每次 X 终端启动或切换字号时，解析数十万行 ASCII 文本并将其转换为二进制点阵极为耗时。

DEC、MIT 与 X 联盟推出了 **PCF（Portable Compiled Format）** 格式：
* PCF 预先在磁盘上完成了大小端字节序重排、4 字节内存页对齐、以及各字符包围盒的微积分计算；
* 操作系统启动 X Server 时，只需发起一次底层的 `mmap` 系统调用，即可将全字体瞬间映射至 X11 核心显存，比 BDF 文本解析提速了整整两百倍！
"""

with open('scripts/app_builders/app_a.md', 'r', encoding='utf-8') as f:
    text_a = f.read()

full_a = text_a.strip() + '\n' + extra_a_2.strip() + '\n'

with open('scripts/app_builders/app_a.md', 'w', encoding='utf-8') as f:
    f.write(full_a)

print("Successfully expanded scripts/app_builders/app_a.md, total length:", len(full_a))
