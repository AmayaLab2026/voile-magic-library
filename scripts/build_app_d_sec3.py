# -*- coding: utf-8 -*-
"""
Builder for Appendix D Section 3: OpenType Layout Tables (GSUB, GPOS, GDEF, BASE, JSTF)
Target: ~15,000 characters
"""

sec3 = r"""---

## D.6 OpenType 布局与形态表（GSUB, GPOS, GDEF, BASE, JSTF）

OpenType 彻底超越传统点阵与静态矢量的核心，在于其将排印学提升为一门**上下文敏感的文法重写系统**。排版引擎在加载字库后，首先构建起全局布局查找拓扑：

$$\text{ScriptList} \longrightarrow \text{LangSysRecord} \longrightarrow \text{FeatureList} \longrightarrow \text{LookupList} \longrightarrow \text{SubTables}$$

```xml
<!-- OpenType 顶层布局结构拓扑 (TTX 范例) -->
<GSUB>
  <Version value="0x00010000"/>
  <ScriptList>
    <ScriptRecord index="0">
      <ScriptTag value="latn"/>
      <Script>
        <DefaultLangSys>
          <ReqFeatureIndex value="65535"/>
          <FeatureIndex index="0" value="0"/> <!-- 指向 'liga' -->
          <FeatureIndex index="1" value="1"/> <!-- 指向 'smcp' -->
        </DefaultLangSys>
      </Script>
    </ScriptRecord>
  </ScriptList>
  <FeatureList>
    <FeatureRecord index="0">
      <FeatureTag value="liga"/>
      <Feature>
        <LookupListIndex value="0"/>
      </Feature>
    </FeatureRecord>
  </FeatureList>
  <LookupList>
    <Lookup index="0">
      <LookupType value="4"/> <!-- Ligature Substitution -->
      <LookupFlag value="0"/>
      <!-- 具体子表 -->
    </Lookup>
  </LookupList>
</GSUB>
```

---

### 1. 基础构件：Coverage 表与 ClassDef 表
在所有 GSUB 与 GPOS 子表中，两个最基础的筛选构件是 **Coverage 表** 与 **ClassDef 表**：

#### Coverage 表（覆盖字形集合）：
用于快速裁决当前字形是否属于本子表的受控目标，并将 GID 转换为致密的从 0 开始的覆盖索引（Coverage Index）：
* **Format 1（离散字形数组）**：
  ```c
  struct CoverageFormat1 {
      uint16 coverageFormat; /* 恒为 1 */
      uint16 glyphCount;     /* 受控字形总数 */
      uint16 glyphArray[glyphCount]; /* 严格按 GID 字典序升序排列 */
  };
  ```
* **Format 2（连续区间数组）**：
  ```c
  struct CoverageRangeRecord {
      uint16 startGlyphID;   /* 连续区间起始 GID */
      uint16 endGlyphID;     /* 连续区间结束 GID */
      uint16 startCoverageIndex; /* 该区间首个字符分配的连续覆盖索引 */
  };
  struct CoverageFormat2 {
      uint16 coverageFormat; /* 恒为 2 */
      uint16 rangeCount;     /* 区间总数 */
      struct CoverageRangeRecord rangeRecords[rangeCount];
  };
  ```

#### ClassDef 表（字形分类定义表）：
将成百上千个字形划分为若干个等价类（Class ID: 0 到 65535），极大地压缩上下文匹配规则矩阵：
* **Format 1**：指定 `startGlyphID` 与连续数组 `classValueArray`；
* **Format 2**：通过 `ClassRangeRecord` 将连续区间指定为特定的类编号。

---

### 2. `GSUB` 表内部 8 大查找子表规范全解

| 查找类型 (LookupType) | 英文名称 | 语法与物理排版行为 | 典型排版特性 |
| :--- | :--- | :--- | :--- |
| **Type 1** | Single Substitution | 单字替换：将 1 个字形替换为另 1 个指定字形 | `smcp` (小型大写), `swsh` (花体) |
| **Type 2** | Multiple Substitution | 多字分解：将 1 个字形拆解展开为多个连续字形序列 | 连字还原、梵文构件分解 |
| **Type 3** | Alternate Substitution | 备选替换：为单个字符提供一组等价的美学候选变体 | `aalt` (所有备选), `salt` (样式变体) |
| **Type 4** | Ligature Substitution | 合字替换：将多个连续字形整体熔铸为单一合字 | `liga` (标准连字 'fi', 'fl'), `dlig` |
| **Type 5** | Contextual Substitution | 上下文替换：当满足特定前后文模式时触发替换 | 阿拉伯文词首、词中、词尾形 |
| **Type 6** | Chaining Contextual | 链式上下文替换：支持回溯（Backtrack）、当前输入（Input）与前瞻（Lookahead）三重序列约束 | 现代高级排版核心、乌尔都文 |
| **Type 7** | Extension Substitution | 32 位扩展跳转：打破 16 位 64KB 内部偏移限制 | 超大字库全局寻址 |
| **Type 8** | Reverse Chaining Single | 逆向链式单字替换：从右向左逆序扫描文本流执行单字替换 | 乌尔都文悬挂波浪折体排版 |

#### GSUB Type 4 合字替换二进制与 TTX 解构：
```xml
<Lookup index="0">
  <LookupType value="4"/>
  <LookupFlag value="0"/>
  <LigatureSubst index="0" Format="1">
    <LigatureSet glyph="f">
      <!-- 遇到 'f' + 'i' 触发替换为 'fi' (GID 280) -->
      <Ligature components="i" glyph="f_i"/>
      <!-- 遇到 'f' + 'l' 触发替换为 'fl' (GID 281) -->
      <Ligature components="l" glyph="f_l"/>
      <!-- 遇到 'f' + 'f' + 'i' 触发替换为 'ffi' -->
      <Ligature components="f,i" glyph="f_f_i"/>
    </LigatureSet>
  </LigatureSubst>
</Lookup>
```

#### GSUB Type 6 链式上下文（Chaining Contextual）的三重拓扑匹配：
在排版引擎扫描文本时，Type 6 构筑了一个三维滑动窗口：
1. **Backtrack Sequence**：当前字符前必须依次匹配的字形序列；
2. **Input Sequence**：当前正待发生替换的字形序列（核心目标）；
3. **Lookahead Sequence**：紧随当前字符后必须出现的字形序列。
当且仅当三重序列的 Coverage 条件同时满足时，引擎在 Input 序列的指定相对位置激活下游的 Lookup 子查找表，实现了图灵完备的语法树重写！

---

### 3. `GPOS` 表内部 9 大几何定位子表规范全解

`GPOS` 不改变字形代码，而是通过 **ValueRecord 结构体** 动态微调字形在二维空间中的物理绘制原点与前进宽度：

```c
struct ValueRecord {
    int16 xPlacement;   /* 水平绘制原点位移偏移 */
    int16 yPlacement;   /* 垂直绘制原点位移偏移 */
    int16 xAdvance;     /* 水平前进字宽增量微调（Kern 负值使下一字符左移） */
    int16 yAdvance;     /* 垂直前进高度增量微调 */
    Offset xPlaDevice;  /* 亚像素设备微调表偏移（Device Table） */
    Offset yPlaDevice;
    Offset xAdvDevice;
    Offset yAdvDevice;
};
```

#### GPOS 9 大子表类型全览：
1. **Type 1（Single Adjustment）**：为单个字形调整坐标或字宽（例如句尾标点或全角标点悬挂）；
2. **Type 2（Pair Adjustment / 字偶距调整 Kerning）**：
   * Format 1：基于离散字偶对（PairSet 数组，针对特异孤立字符对）；
   * Format 2：基于类的矩阵微调（Class-based Kerning，将数千字形划分为大写类、小写圆弧类，以极小矩阵覆盖全字库）；
3. **Type 3（Cursive Attachment / 草书连贯吸附）**：为连续草书（如阿拉伯文、乌尔都文）定义 `EntryAnchor`（进入锚点）与 `ExitAnchor`（退出锚点）。排版引擎通过平移字形，强制使当前字符的 Entry 锚点与前一字符的 Exit 锚点在二维空间严格重叠，确保流体书法天衣无缝；
4. **Type 4（MarkToBase Attachment / 基字标音吸附）**：将变音符、声调（Mark）吸附到字母主干（Base）的特定几何位置（如重音字母、泰文元音）；
5. **Type 5（MarkToLigature Attachment / 合字标音吸附）**：在合字内部各个逻辑分字符构件上独立定义标音锚点；
6. **Type 6（MarkToMark Attachment / 标音叠标音吸附）**：在阿拉伯文多重修饰音符中，将上方音符叠加在另一个音符之上；
7. **Type 7 / 8 / 9**：上下文定位、链式上下文定位与 32 位扩展定位跳转。

---

### 4. `GDEF`、`BASE` 与 `JSTF` 表

* **`GDEF`（字形全局属性定义表）**：
  * `GlyphClassDef`：将全字库字形划分为四种神圣类型：
    1. **Base Glyph（单字基字）**：常规文本字符；
    2. **Ligature Glyph（合字字符）**：由多字拼接而成的连字；
    3. **Mark Glyph（结合附着符号）**：无前进宽度的变音符或声调符号；
    4. **Component Glyph（组件字符）**：不可单独显示的内部拼装部件。
  * `AttachList`：在轮廓上显式标明可用于几何组装的锚点编号；
  * `LigCaretList`：定义多字符合字（如 'ffi'）内部的文本光标闪烁分界线（Caret Positions）；
* **`BASE`（跨文字基准线对齐表）**：
  * 在同一段落中混合排版西文拉丁字母、汉字方块字、藏文与印度天城体时，各种文字的历史基准参考线完全不同。`BASE` 表统一定义了 `romn`（罗马基线）、`ideo`（汉字底部基线）、`idcm`（汉字正中轴线）以及 `math`（数学公式中轴），排版引擎依据各文字的基线偏差矩阵自动平移字身，实现跨语系视觉平齐；
* **`JSTF`（两端对齐与段落调整表）**：
  * 专为阿拉伯文等复杂书写系统设计。当需要对段落执行两端对齐（Justification）时，`JSTF` 定义了多级优先级的微调动作：第一级拉长笔画横梁（Kashida 填充）；第二级调用更宽的备选字形；第三级微调字距；第四级允许空格适度拉伸，再现了传统手抄本时代的极致排印美感。
"""

with open('scripts/app_builders/app_d_sec3.md', 'w', encoding='utf-8') as f:
    f.write(sec3.strip() + '\n')
print("Section 3 written, length:", len(sec3))
