import type { DefaultTheme } from 'vitepress'
import { defineConfig } from 'vitepress'

export default defineConfig({
  lang: 'zh-Hans',
  description: 'ヴワル魔法図書館 - 散发着书香的禁忌之识，尽在本馆',

  themeConfig: {
    nav: nav(),

    sidebar: {
      '/rocket-pioneers/': [
        {
          text: '火箭技术先驱：选集',
          items: [
            { text: '典籍概述与全书目录', link: '/rocket-pioneers/' },
            { text: '主编序言：苏联航天历程与先驱评述', link: '/rocket-pioneers/preface' },
            { text: '第一编：航空机器设想（基巴利契奇）', link: '/rocket-pioneers/kibalchich' },
          ],
        },
        {
          text: '第二编：致读此书以建造者（孔德拉秋克 1918–1919）',
          collapsed: false,
          items: [
            { text: '手稿全貌与工程奠基导读', link: '/rocket-pioneers/kondratyuk-build/' },
            { text: '第一章：喷气推进原理与速度方程', link: '/rocket-pioneers/kondratyuk-build/section-1' },
            { text: '第二章：轨道爬升方案与活性推进剂', link: '/rocket-pioneers/kondratyuk-build/section-2' },
            { text: '第三章：飞船结构与陀螺仪定向', link: '/rocket-pioneers/kondratyuk-build/section-3' },
            { text: '第四章：喷管设计与返回制动发现', link: '/rocket-pioneers/kondratyuk-build/section-4' },
            { text: '第五章：滑翔再入与大气减速防热', link: '/rocket-pioneers/kondratyuk-build/section-5' },
            { text: '第六章：太阳能聚能镜与引力弹弓', link: '/rocket-pioneers/kondratyuk-build/section-6' },
            { text: '编委会文献考证与技术评注', link: '/rocket-pioneers/kondratyuk-build/commentary' },
          ],
        },
        {
          text: '第三编：征服星际空间（孔德拉秋克 1929）',
          collapsed: false,
          items: [
            { text: '作者自序与全书导览', link: '/rocket-pioneers/kondratyuk-space/' },
            { text: '第 1 章：星际飞行前提与运行规律', link: '/rocket-pioneers/kondratyuk-space/chapter-1' },
            { text: '第 2 章：主动段加速与多级载荷公式', link: '/rocket-pioneers/kondratyuk-space/chapter-2' },
            { text: '第 3 章：排气速度与推进剂化学热值', link: '/rocket-pioneers/kondratyuk-space/chapter-3' },
            { text: '第 4 章：火箭结构与轻量化工程设计', link: '/rocket-pioneers/kondratyuk-space/chapter-4' },
            { text: '第 5 章：结构死重占比与级数优化', link: '/rocket-pioneers/kondratyuk-space/chapter-5' },
            { text: '第 6 章：空间惯性飞行轨道与变轨', link: '/rocket-pioneers/kondratyuk-space/chapter-6' },
            { text: '第 7 章：登月与月球轨道交会（LOR）', link: '/rocket-pioneers/kondratyuk-space/chapter-7' },
            { text: '第 8 章：大气层对主动段爬升的影响', link: '/rocket-pioneers/kondratyuk-space/chapter-8' },
            { text: '第 9 章：再入大气减速与超高速防热', link: '/rocket-pioneers/kondratyuk-space/chapter-9' },
            { text: '第 10 章：空间中继站与行星际基地', link: '/rocket-pioneers/kondratyuk-space/chapter-10' },
            { text: '第 11 章：太阳能聚能镜与能源利用', link: '/rocket-pioneers/kondratyuk-space/chapter-11' },
            { text: '第 12 章：研究优先权与历史说明', link: '/rocket-pioneers/kondratyuk-space/chapter-12' },
            { text: '第 13 章：亟待开展的基础实验清单', link: '/rocket-pioneers/kondratyuk-space/chapter-13' },
            { text: '编注与理论数学推导附录', link: '/rocket-pioneers/kondratyuk-space/commentary' },
          ],
        },
        {
          text: '第四编：俄罗斯与苏联火箭先驱历史纲要',
          collapsed: false,
          items: [
            { text: '历史纲要引言与 19 世纪早期先驱', link: '/rocket-pioneers/historical-outline/' },
            { text: '第一章：齐奥尔科夫斯基与梅谢尔斯基', link: '/rocket-pioneers/historical-outline/section-1' },
            { text: '第二章：灿德尔与早期火箭发动机研发', link: '/rocket-pioneers/historical-outline/section-2' },
            { text: '第三章：孔德拉秋克对航天理论的贡献', link: '/rocket-pioneers/historical-outline/section-3' },
            { text: '第四章：早期机构（GDL/GIRD/RNII）总结', link: '/rocket-pioneers/historical-outline/section-4' },
          ],
        },
        {
          text: '附录与文献索引',
          items: [
            { text: '先驱著作与历史文献全景索引', link: '/rocket-pioneers/bibliography' },
          ],
        },
      ],
      '/controlled-substances/': [
        {
          text: '管制物质：化学与法律指南',
          items: [
            { text: '本书概述与全书目录', link: '/controlled-substances/' },
            { text: '引言与专家序言', link: '/controlled-substances/forewords' },
            { text: '第一章：法规细节与定义', link: '/controlled-substances/chapter-1' },
            { text: '第二章：受管制药物与同义词', link: '/controlled-substances/chapter-2' },
            { text: '第三章：联邦药物法历史沿革', link: '/controlled-substances/chapter-3' },
            { text: '第四章：分子结构式图解（全）', link: '/controlled-substances/chapter-4' },
            { text: '第五章：DEA 管制代码编号全表', link: '/controlled-substances/chapter-5' },
            { text: '第六章：联邦公报法令与行政依据', link: '/controlled-substances/chapter-6' },
            { text: '第七章：经验实验式化学索引库', link: '/controlled-substances/chapter-7' },
            { text: '附录：联邦法规与前体清单', link: '/controlled-substances/appendices' },
          ],
        },
      ],
      '/fonts-encodings/': [
        {
          text: '卷首与总论',
          items: [
            { text: '典籍概述与全书目录', link: '/fonts-encodings/' },
            { text: '导言 · 探索篇：字母部件与排版', link: '/fonts-encodings/introduction' },
          ],
        },
        {
          text: '第一编：编码与字符集（Part I）',
          collapsed: false,
          items: [
            { text: '第一章：前 Unicode 时代编码体系', link: '/fonts-encodings/chapter-1' },
            { text: '第二章：字符字形与字节（Unicode 导论）', link: '/fonts-encodings/chapter-2' },
            { text: '第三章：Unicode 字符核心属性体系', link: '/fonts-encodings/chapter-3' },
            { text: '第四章：规范化、双向算法与东亚文字', link: '/fonts-encodings/chapter-4' },
            { text: '第五章：Unicode 实践与字符录入工具', link: '/fonts-encodings/chapter-5' },
          ],
        },
        {
          text: '第二编：操作系统字体管理（Part II）',
          collapsed: false,
          items: [
            { text: '第六章：Macintosh 操作系统的字体管理', link: '/fonts-encodings/chapter-6' },
            { text: '第七章：Windows 操作系统的字体管理', link: '/fonts-encodings/chapter-7' },
            { text: '第八章：X Window 与 Unix 字体管理', link: '/fonts-encodings/chapter-8' },
          ],
        },
        {
          text: '第三编：排版引擎与技术生态（Part III）',
          collapsed: false,
          items: [
            { text: '第九章：TeX 与 Omega 系统的字体技术', link: '/fonts-encodings/chapter-9' },
            { text: '第十章：Web 网页字体与排版技术', link: '/fonts-encodings/chapter-10' },
          ],
        },
        {
          text: '第四编：字体艺术、设计与高级排版（Part IV）',
          collapsed: false,
          items: [
            { text: '第十一章：拉丁字体的历史演进与分类学', link: '/fonts-encodings/chapter-11' },
            { text: '第十二章：字体设计与编辑实操', link: '/fonts-encodings/chapter-12' },
            { text: '第十三章：栅格化渲染优化与字形微调', link: '/fonts-encodings/chapter-13' },
            { text: '第十四章：丰富字体表达：高级排版特性', link: '/fonts-encodings/chapter-14' },
          ],
        },
        {
          text: '第五编：技术附录（Part V）',
          collapsed: false,
          items: [
            { text: '附录全编：底层格式与数学原理手册', link: '/fonts-encodings/appendices' },
          ],
        },
      ],
      '/': [
        {
          text: '本馆导览',
          items: [
            { text: '关于本馆：ヴワル魔法図書館', link: '/about' },
            { text: '馆藏典籍索引 · 索书与著者信息', link: '/catalogue' },
          ],
        },
        {
          text: '馆藏典籍',
          items: [
            { text: '《管制物质：联邦药物法的化学与法律指南》', link: '/controlled-substances/' },
            { text: '《火箭技术先驱：苏联宇航先驱选集》', link: '/rocket-pioneers/' },
            { text: '《字体与编码：Unicode 与高级排版全解》', link: '/fonts-encodings/' },
          ],
        },
        {
          text: '关于',
          items: [
            { text: '项目致谢', link: '/acknowledgements' },
          ],
        },
      ],
    },

    editLink: {
      pattern: 'https://github.com/AmayaLab2026/voile-magic-library/edit/main/docs/:path',
      text: '在 GitHub 上编辑此页面',
    },

    footer: {
      message: '基于 MIT 许可发布',
      copyright: `版权所有 © 2023-${new Date().getFullYear()} AmayaLab`,
    },

    docFooter: {
      prev: '上一页',
      next: '下一页',
    },

    outline: {
      level: [2, 3],
      label: '页面导航',
    },

    lastUpdated: {
      text: '最后更新于',
    },

    notFound: {
      title: '页面未找到',
      quote:
        '但如果你不改变方向，并且继续寻找，你可能最终会到达你所前往的地方。',
      linkLabel: '前往首页',
      linkText: '带我回首页',
    },

    langMenuLabel: '多语言',
    returnToTopLabel: '回到顶部',
    sidebarMenuLabel: '菜单',
    darkModeSwitchLabel: '主题',
    lightModeSwitchTitle: '切换到浅色模式',
    darkModeSwitchTitle: '切换到深色模式',
    skipToContentLabel: '跳转到内容',
  },
})

function nav(): DefaultTheme.NavItem[] {
  return [
    { text: '本馆介绍', link: '/about', activeMatch: '/about' },
    { text: '典籍索引', link: '/catalogue', activeMatch: '/catalogue' },
    {
      text: '馆藏书库',
      items: [
        { text: '《管制物质：联邦药物法的化学与法律指南》', link: '/controlled-substances/' },
        { text: '《火箭技术先驱：苏联宇航先驱选集》', link: '/rocket-pioneers/' },
        { text: '《字体与编码：Unicode 与高级排版全解》', link: '/fonts-encodings/' },
      ],
    },
    {
      text: '项目致谢',
      link: '/acknowledgements',
      activeMatch: '/acknowledgements',
    },
  ]
}
