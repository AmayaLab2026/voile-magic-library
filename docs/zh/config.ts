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
            { text: '第二编：致读此书以建造者（孔德拉秋克第一手稿）', link: '/rocket-pioneers/kondratyuk-build' },
            { text: '第三编：征服星际空间（孔德拉秋克代表作）', link: '/rocket-pioneers/kondratyuk-space' },
            { text: '第四编：俄罗斯与苏联火箭技术先驱历史纲要', link: '/rocket-pioneers/historical-outline' },
            { text: '附录：先驱著作与历史文献全景索引', link: '/rocket-pioneers/bibliography' },
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
      '/': [
        {
          text: '本馆导览',
          items: [
            { text: '关于本馆：ヴワル魔法図書館', link: '/about' },
          ],
        },
        {
          text: '馆藏典籍',
          items: [
            { text: 'Vol. 01 管制物质：化学与法律指南', link: '/controlled-substances/' },
            { text: 'Vol. 02 火箭技术先驱：选集', link: '/rocket-pioneers/' },
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
      pattern: 'https://github.com/vuejs/vitepress/edit/main/docs/:path',
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
    {
      text: '本馆介绍',
      link: '/about',
      activeMatch: '/about',
    },
    {
      text: '馆藏书库',
      items: [
        { text: 'Vol. 01 管制物质：化学与法律指南', link: '/controlled-substances/' },
        { text: 'Vol. 02 火箭技术先驱：选集', link: '/rocket-pioneers/' },
      ],
    },
    {
      text: '项目致谢',
      link: '/acknowledgements',
      activeMatch: '/acknowledgements',
    },
  ]
}

function searchOptions(): any {
  return {
    miniSearch: {
      searchOptions: {
        fuzzy: 0.2,
        prefix: true,
        boost: {
          title: 4,
          text: 2,
          titles: 1,
        },
      },
    },
  }
}
