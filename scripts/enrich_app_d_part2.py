# -*- coding: utf-8 -*-
"""
Enriches app_d.md with advanced GSUB Type 5, 7, 8 and GPOS MarkToMark & Ligature Caret XML.
Target: ~43,000 characters
"""

extra_d_2 = r"""
---

## D.8 复杂书写系统（Complex Scripts）排版布局实战案例

为了彻底展示 OpenType 与 AAT 处理阿拉伯文、南亚印度系文字（Indic Scripts）以及东亚纵排文字的工业级能力，以下剖析三大高级排版实战结构：

### 1. 阿拉伯文四态上下文替换（Contextual Substitution GSUB Type 5）
在阿拉伯文字体中，每个字母具有四种截然不同的书写形态：
* **孤立态（Isolated）**：字符前后均未连笔；
* **词首态（Initial）**：仅与后一字符连笔；
* **词中态（Medial）**：前后均连笔；
* **词尾态（Final）**：仅与前一字符连笔。

OpenType 引擎首先通过 `init`、`medi`、`fina`、`isol` 四个排版特性，使用 GSUB Type 5（基于类的上下文替换）进行状态匹配：

```xml
<Lookup index="15">
  <LookupType value="5"/> <!-- Contextual Substitution -->
  <LookupFlag value="1"/> <!-- RightToLeft -->
  <ContextSubst index="0" Format="2">
    <!-- 覆盖所有具有连笔能力的阿拉伯文字母 -->
    <Coverage Format="1">
      <Glyph value="ar_baa"/>
      <Glyph value="ar_jeem"/>
      <Glyph value="ar_seen"/>
    </Coverage>
    <ClassDef Format="1">
      <ClassDefinition glyph="ar_baa" class="1"/>
      <ClassDefinition glyph="ar_jeem" class="1"/>
      <ClassDefinition glyph="space" class="2"/>
    </ClassDef>
    <!-- 当 Class 1 (字母) 后紧随 Class 1 (字母) 时，触发替换为词首态 -->
    <SubClassSet index="1">
      <SubClassRule index="0">
        <ClassSequence>
          <Class value="1"/>
        </ClassSequence>
        <SubstLookupRecord index="0">
          <SequenceIndex value="0"/>
          <LookupListIndex value="20"/> <!-- 词首态替换子表 -->
        </SubstLookupRecord>
      </SubClassRule>
    </SubClassSet>
  </ContextSubst>
</Lookup>
```

---

### 2. 多重音标堆叠与碰撞规避（Mark-to-Mark GPOS Type 6）
在阿拉伯文《古兰经》诵读记号或希伯来文圣经多重变音符中，字母上方往往需要垂直堆叠两到三个独立的读音与声调符号。若机械放置，符号必然重叠。

GPOS Type 6 构筑了音标之间的递归相对几何锚点：
```xml
<Lookup index="16">
  <LookupType value="6"/> <!-- MarkToMark Attachment -->
  <LookupFlag value="0"/>
  <MarkMarkPos index="0" Format="1">
    <!-- 顶层音标：开音符 (Fathah) -->
    <Mark1Coverage Format="1">
      <Glyph value="ar_fathah"/>
    </Mark1Coverage>
    <!-- 底层音标：鼻音化轻读符 (Tanwin) -->
    <Mark2Coverage Format="1">
      <Glyph value="ar_tanwin"/>
    </Mark2Coverage>
    <Mark2Array>
      <Mark2Record index="0">
        <!-- 在底层音标顶端定义向上的对接锚点 -->
        <Mark2Anchor index="0" Format="1">
          <XCoordinate value="0"/>
          <YCoordinate value="220"/>
        </Mark2Anchor>
      </Mark2Record>
    </Mark2Array>
    <Mark1Array>
      <Mark1Record index="0">
        <Class value="0"/>
        <Mark1Anchor Format="1">
          <XCoordinate value="0"/>
          <YCoordinate value="0"/>
        </Mark1Anchor>
      </Mark1Record>
    </Mark1Array>
  </MarkMarkPos>
</Lookup>
```

无论下层音标的位置因基字高度发生何种位移，上层音标通过实时锚点对齐，永远浮动在下层音标正上方 220 栅格单位处，彻底消除了文字重叠！

---

### 3. 合字光标分割线（`GDEF` Ligature Caret List）
当用户使用光标键在一个连字合字（如 'ffi'）内部穿行时，文字处理软件查询 `GDEF` 表的 `LigCaretList`：

```xml
<GDEF>
  <Version value="0x00010002"/>
  <LigCaretList>
    <Coverage Format="1">
      <Glyph value="f_f_i"/>
    </Coverage>
    <LigGlyph index="0">
      <!-- 'f' 与第二个 'f' 之间的光标闪烁 X 坐标 -->
      <CaretValue index="0" Format="1">
        <Coordinate value="320"/>
      </CaretValue>
      <!-- 第二个 'f' 与 'i' 之间的光标闪烁 X 坐标 -->
      <CaretValue index="1" Format="1">
        <Coordinate value="650"/>
      </CaretValue>
    </LigGlyph>
  </LigCaretList>
</GDEF>
```

软件依据这些坐标，在屏幕上绘制闪烁的垂直光标，并在用户按下退格键（Backspace）时，精准将合字拆解还原，提供毫无破绽的原生多字符编辑体验。
"""

with open('scripts/app_builders/app_d.md', 'r', encoding='utf-8') as f:
    text_d = f.read()

full_d = text_d.strip() + '\n' + extra_d_2.strip() + '\n'

with open('scripts/app_builders/app_d.md', 'w', encoding='utf-8') as f:
    f.write(full_d)

print("Successfully expanded scripts/app_builders/app_d.md, total length:", len(full_d))
