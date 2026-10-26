# -*- coding: utf-8 -*-
"""
Rich OpenType Layout Section (GSUB & GPOS in TTX XML & Binary Structs)
"""

rich_sec3 = r"""---

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
          <FeatureIndex index="2" value="2"/> <!-- 指向 'cpsp' -->
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
    <FeatureRecord index="1">
      <FeatureTag value="smcp"/>
      <Feature>
        <LookupListIndex value="1"/>
      </Feature>
    </FeatureRecord>
  </FeatureList>
  <LookupList>
    <Lookup index="0">
      <LookupType value="4"/> <!-- Ligature Substitution -->
      <LookupFlag value="0"/>
      <!-- 具体子表 -->
    </Lookup>
    <Lookup index="1">
      <LookupType value="1"/> <!-- Single Substitution -->
      <LookupFlag value="0"/>
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

### 2. `GSUB` 表内部 8 大查找子表规范与 TTX 源码全景

#### Type 1：单字替换（Single Substitution）
* **Format 1（固定增量）**：将输入字形的 GID 加上固定标量 `DeltaGlyphID`；
* **Format 2（一一映射查找表）**：
  ```xml
  <Lookup index="1">
    <LookupType value="1"/>
    <LookupFlag value="0"/>
    <SingleSubst index="0" Format="2">
      <Substitution in="a" out="a.sc"/>
      <Substitution in="b" out="b.sc"/>
      <Substitution in="c" out="c.sc"/>
      <Substitution in="d" out="d.sc"/>
    </SingleSubst>
  </LookupList>
  ```

#### Type 2：多字分解（Multiple Substitution）
将单个输入字形在排版流中原地解构为一个连续的字形序列：
```xml
<Lookup index="2">
  <LookupType value="2"/>
  <LookupFlag value="0"/>
  <MultipleSubst index="0" Format="1">
    <!-- 将连字符 'ffi' 还原分解为独立的三个字形 -->
    <Sequence glyph="f_f_i">
      <Substitute value="f"/>
      <Substitute value="f"/>
      <Substitute value="i"/>
    </Sequence>
  </MultipleSubst>
</Lookup>
```

#### Type 3：备选替换（Alternate Substitution）
为单个字符提供一组等价的美学候选变体，供排版师在交互式菜单中按需挑选：
```xml
<Lookup index="3">
  <LookupType value="3"/>
  <LookupFlag value="0"/>
  <AlternateSubst index="0" Format="1">
    <AlternateSet glyph="ampersand">
      <Alternate glyph="ampersand.italic"/>
      <Alternate glyph="ampersand.swash1"/>
      <Alternate glyph="ampersand.swash2"/>
    </AlternateSet>
  </AlternateSubst>
</Lookup>
```

#### Type 4：合字替换（Ligature Substitution）
包含按首字母聚合的 `LigatureSet` 数组，内部包含各连字组件与生成的目标合字：
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

#### Type 5 与 Type 6：上下文与链式上下文替换（Contextual & Chained Contextual）
Type 6 是 OpenType 文法重写的顶峰。它维护 Backtrack、Input、Lookahead 三重滑动窗口：
```xml
<Lookup index="6">
  <LookupType value="6"/>
  <LookupFlag value="0"/>
  <ChainContextSubst index="0" Format="3">
    <!-- 回溯序列：前面必须有大写字母 -->
    <BacktrackCoverage index="0" Format="1">
      <Glyph value="A"/>
      <Glyph value="E"/>
    </BacktrackCoverage>
    <!-- 输入序列：当前字符小写 'e' -->
    <InputCoverage index="0" Format="1">
      <Glyph value="e"/>
    </InputCoverage>
    <!-- 前瞻序列：后面必须跟随字母 'r' -->
    <LookaheadCoverage index="0" Format="1">
      <Glyph value="r"/>
    </LookaheadCoverage>
    <!-- 动作：在当前输入位置 0 处，调用 Lookup 1 (小型大写替换) -->
    <SubstLookupRecord index="0">
      <SequenceIndex value="0"/>
      <LookupListIndex value="1"/>
    </SubstLookupRecord>
  </ChainContextSubst>
</Lookup>
```

#### Type 7 与 Type 8：
* **Type 7（Extension Substitution）**：打破 16 位 64KB 内部相对偏移限制的 32 位跳转包装器；
* **Type 8（Reverse Chaining Contextual Single）**：专为乌尔都文纳斯塔里克体（Nastaliq）量身定制，排版引擎从后向前逆序求值，确保向下倾斜的级联词尾字符能够正确变形。

---

### 3. `GPOS` 表内部 9 大几何定位子表与 TTX 源码全景

`GPOS` 不修改字形代码，而是通过对字形施加二维矢量偏移与前进宽度修正，完成毫秒级空间装配：

#### Type 1：单字定位调整（Single Adjustment）
```xml
<Lookup index="7">
  <LookupType value="1"/>
  <LookupFlag value="0"/>
  <SinglePos index="0" Format="1">
    <Coverage Format="1">
      <Glyph value="hyphen"/>
      <Glyph value="endash"/>
    </Coverage>
    <!-- 将连字符向上抬高 120 栅格单位以匹配大写字母中心 -->
    <Value YPlacement="120"/>
  </SinglePos>
</Lookup>
```

#### Type 2：基于类的字偶距微调（Class-based PairPos）
```xml
<Lookup index="8">
  <LookupType value="2"/>
  <LookupFlag value="8"/> <!-- 忽略结合音标 -->
  <PairPos index="0" Format="2">
    <Coverage Format="1">
      <Glyph value="T"/>
      <Glyph value="V"/>
      <Glyph value="W"/>
    </Coverage>
    <ClassDef1 Format="1">
      <ClassDefinition glyph="T" class="1"/>
      <ClassDefinition glyph="V" class="2"/>
      <ClassDefinition glyph="W" class="2"/>
    </ClassDef1>
    <ClassDef2 Format="1">
      <ClassDefinition glyph="o" class="1"/>
      <ClassDefinition glyph="c" class="1"/>
      <ClassDefinition glyph="e" class="1"/>
      <ClassDefinition glyph="a" class="2"/>
    </ClassDef2>
    <!-- 类别 1 (T) 与 类别 1 (o, c, e) 相遇时的字距调整 -->
    <Class1Record index="1">
      <Class2Record index="1">
        <Value1 XAdvance="-180"/>
      </Class2Record>
      <!-- 类别 1 (T) 与 类别 2 (a) 相遇时微调 -150 -->
      <Class2Record index="2">
        <Value1 XAdvance="-150"/>
      </Class2Record>
    </Class1Record>
  </PairPos>
</Lookup>
```

#### Type 3：草书连贯吸附（Cursive Attachment）
```xml
<Lookup index="9">
  <LookupType value="3"/>
  <LookupFlag value="1"/> <!-- 从右向左排版 -->
  <CursivePos index="0" Format="1">
    <Coverage Format="1">
      <Glyph value="ar_baa.init"/>
      <Glyph value="ar_noon.medi"/>
    </Coverage>
    <EntryExitRecord index="0">
      <EntryAnchor Format="1">
        <XCoordinate value="0"/>
        <YCoordinate value="150"/>
      </EntryAnchor>
      <ExitAnchor Format="1">
        <XCoordinate value="600"/>
        <YCoordinate value="100"/>
      </ExitAnchor>
    </EntryExitRecord>
  </CursivePos>
</Lookup>
```

#### Type 4：基字标音吸附（MarkToBase Attachment）
定义字母主干上的固定锚点与音标符号上的对齐锚点：
```xml
<Lookup index="10">
  <LookupType value="4"/>
  <LookupFlag value="0"/>
  <MarkBasePos index="0" Format="1">
    <MarkCoverage Format="1">
      <Glyph value="acute"/>
      <Glyph value="grave"/>
    </MarkCoverage>
    <BaseCoverage Format="1">
      <Glyph value="a"/>
      <Glyph value="e"/>
      <Glyph value="o"/>
    </BaseCoverage>
    <BaseArray>
      <BaseRecord index="0">
        <!-- 字母 'a' 顶部的对齐中心锚点 -->
        <BaseAnchor index="0" Format="1">
          <XCoordinate value="260"/>
          <YCoordinate value="680"/>
        </BaseAnchor>
      </BaseRecord>
    </BaseArray>
    <MarkArray>
      <MarkRecord index="0">
        <Class value="0"/>
        <MarkAnchor Format="1">
          <XCoordinate value="0"/>
          <YCoordinate value="0"/>
        </MarkAnchor>
      </MarkRecord>
    </MarkArray>
  </MarkBasePos>
</Lookup>
```

---

### 4. `GDEF`、`BASE` 与 `JSTF` 表深度解构

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
    f.write(rich_sec3.strip() + '\n')
print("Successfully written rich app_d_sec3.md, length:", len(rich_sec3))
