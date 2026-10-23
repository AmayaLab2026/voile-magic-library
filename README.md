<div align="center">

# ヴワル魔法図書館
### *Voile Magic Library*

<p align="center">
  <strong>散发着书香的禁忌之识，尽在本馆</strong>
</p>

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![VitePress](https://img.shields.io/badge/VitePress-2.x-8a63d2.svg)](https://vitepress.dev/)
[![pnpm](https://img.shields.io/badge/pnpm-10.x-f69220.svg)](https://pnpm.io/)
[![Organization](https://img.shields.io/badge/AmayaLab-2026-c2785c.svg)](https://github.com/AmayaLab2026)

</div>

---

> *“书页微黄，散发着沉香与墨彩的芬芳；世俗不可窥探的理性微光，皆在此处静默安歇。”*

## 关于本馆

**ヴワル魔法図書館**（Voile Magic Library / 伏瓦鲁魔法图书馆）由 **[AmayaLab](https://github.com/AmayaLab2026)** 创设并由馆长 **翎奈猫（YuukiReina2023）** 主持维护，是一座**致力于沉淀跨学科“硬核学术与禁忌前沿知识”的开源数字典籍馆**。

我们不随波逐流于浅尝辄止的快餐资讯，而是将目光投向那些横跨在**高级有机化学、精神药理学（Psychopharmacology）、法庭毒理物证学、理论天体动力学与火箭工程史、开源情报学（OSINT）以及人类社会法律规制边界**上的深度文献与经典巨著。

### 核心特色

- **严谨化学与工程图解**：收录舒尔金 33 幅化学母核骨架图、基巴利契奇 1881 年死牢火箭草图、孔德拉秋克 42 幅轨道力学与航天器总体构型原理图版。
- **法律与科学交汇**：深度剖析美国《受控物质法案》（CSA）五级分类架构、DEA 药物管制代码、紧急列管特权与 1986 年《类似物法案》（Federal Analogue Act）实质相似判定难题。
- **跨学科权威典籍全译**：拒绝断章取义与概括总结，严格依照原著段落与数学力学公式进行全文深度学术汉译。
- **典雅拟纸排版**：基于 VitePress 与 Claude 温润拟纸设计规范，全胶囊化交互与优雅衬线排版，带来纯粹静谧的阅读享受。
- **多语言支持**：原生支持简体中文（默认）、English、日本語、繁體中文。

---

## 现有馆藏书库

| 馆藏号 | 书名 | 原作者 | 说明 |
| :---: | :--- | :--- | :--- |
| **Vol. 01** | [《管制物质：联邦药物法的化学与法律指南》](/controlled-substances/) (*Controlled Substances: A Chemical and Legal Guide to the Federal Drug Laws*) | Alexander T. Shulgin, Ph.D.（第二版） | 436 页经典巨著全书编译整理，完整收录 7 大核心章节、引言序言、33 幅母核图版与附录。 |
| **Vol. 02** | [《火箭技术先驱：选集》](/rocket-pioneers/) (*Pioneers of Rocket Technology: Selected Works*) | 苏联科学院自然科学与技术史研究所 编纂，NASA TT F-9285 | 完整收录基巴利契奇 1881 死囚牢手稿、孔德拉秋克《致读此书以建造者》（1918–1919）与《征服星际空间》（1929）、索科尔斯基历史纲要全译，配齐全部 42 幅高清工程原理图版。 |

---

## 技术栈与架构

- **核心驱动**：[VitePress](https://vitepress.dev/) 2.x
- **插件生态**：[Nólëbase](https://nolebase.ayaka.moe/) 系列增强套件（双向链接、图片懒加载、代码高亮、行内预览、阅读进度、Git 变更记录）
- **原子化样式**：[UnoCSS](https://unocss.dev/)
- **公式渲染**：Markdown-it-mathjax3（KaTeX / MathJax）
- **排版主题**：定制温润拟纸色调（Warm Paper Tone）与 Claude 风格圆角胶囊组件

---

## 本地研读与开发指南

本项目采用 [pnpm](https://pnpm.io/)（v10+）进行依赖管理。

### 1. 安装依赖

```bash
pnpm install
```

### 2. 启动本地开发服务

```bash
pnpm dev
```
启动后在浏览器中打开控制台输出的本地地址（通常为 `http://localhost:5173`）即可预览本馆。

### 3. 构建生产静态页面

```bash
pnpm build
```
编译产物将生成至 `.vitepress/dist` 目录。

### 4. 预览生产构建

```bash
pnpm serve
```

---

## 目录结构

```text
.
├── docs/                # 馆藏典籍多语言文档源文件
│   ├── zh/              # 简体中文馆藏（默认语言）
│   │   ├── controlled-substances/  # 馆藏第一号：受控物质全书译文
│   │   ├── rocket-pioneers/        # 馆藏第二号：火箭技术先驱全书译文
│   │   ├── about.md     # 馆藏导览与本馆介绍
│   │   └── acknowledgements.md     # 致谢
│   ├── en/              # English Documentation
│   ├── ja/              # 日本語文献
│   ├── zh-hant/         # 繁體中文文獻
│   └── public/          # 静态资源、化学母核图解与航天原理图版
├── .vitepress/          # 站点配置、Claude 拟纸主题、组件与样式
├── metadata/            # 站点元信息、创作者列表与导航配置
├── scripts/             # 构建辅助脚本与图解抽取工具
├── package.json         # 项目配置与脚本定义
├── pnpm-lock.yaml       # pnpm 依赖锁文件
├── uno.config.ts        # UnoCSS 配置文件
└── README.md            # 本说明文档
```

---

## 馆务与致谢

- **创设与主办**：[AmayaLab](https://github.com/AmayaLab2026)
- **馆长与维护**：[翎奈猫 (YuukiReina2023)](https://github.com/YuukiReina2023)
- **特别致敬**：
  - 亚历山大·“萨沙”·舒尔金 博士（Alexander "Sasha" Shulgin, 1925–2014）及其对药物化学与学术自由的无私奉献。
  - 尼古拉·基巴利契奇、尤里·孔德拉秋克、康斯坦丁·齐奥尔科夫斯基、弗里德里希·灿德尔等人类航天先驱。
  - [Nólëbase](https://github.com/nolebase) 社区提供的杰出 VitePress 知识库套件。

---

## 学术免责声明

本馆收录与整理之所有内容仅用于**法庭科学、化学科普、药物法制史、宇航动力学研读与学术研究交流**，坚决反对并不鼓励任何违反当地法律法规滥用、制造或流通受控物质之行为。

---

## 许可证

本项目基于 [MIT 许可证](LICENSE) 开源。
