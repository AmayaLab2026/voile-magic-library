import type { DefaultTheme } from 'vitepress'
import { defineConfig } from 'vitepress'

export default defineConfig({
  lang: 'zh-Hant',
  description: 'ヴワル魔法図書館 - 散發著書香的禁忌之識，盡在本館',

  themeConfig: {
    nav: nav(),

    sidebar: {
      '/zh-hant/controlled-substances/': [
        {
          text: '管制物質：化學與法律指南',
          items: [
            { text: '本書概述與全書目錄', link: '/zh-hant/controlled-substances/' },
            { text: '引言與專家序言', link: '/zh-hant/controlled-substances/forewords' },
            { text: '第一章：法規細節與定義', link: '/zh-hant/controlled-substances/chapter-1' },
            { text: '第二章：受管制藥物與同義詞', link: '/zh-hant/controlled-substances/chapter-2' },
            { text: '第三章：聯邦藥物法歷史沿革', link: '/zh-hant/controlled-substances/chapter-3' },
            { text: '第四章：分子結構式圖解（全）', link: '/zh-hant/controlled-substances/chapter-4' },
            { text: '第五章：DEA 管制代碼編號全表', link: '/zh-hant/controlled-substances/chapter-5' },
            { text: '第六章：聯邦公報法令與行政依據', link: '/zh-hant/controlled-substances/chapter-6' },
            { text: '第七章：經驗實驗式化學索引庫', link: '/zh-hant/controlled-substances/chapter-7' },
            { text: '附錄：聯邦法規與前體清單', link: '/zh-hant/controlled-substances/appendices' },
          ],
        },
      ],
      '/zh-hant/': [
        {
          text: '本館導覽',
          items: [
            { text: '關於本館：ヴワル魔法図書館', link: '/zh-hant/about' },
            { text: '館藏典籍索引 · 索書與著者信息', link: '/zh-hant/catalogue' },
          ],
        },
        {
          text: '館藏典籍',
          items: [
            { text: 'Vol. 01 管制物質：化學與法律指南', link: '/zh-hant/controlled-substances/' },
            { text: 'Vol. 02 火箭技術先驅：選集', link: '/rocket-pioneers/' },
          ],
        },
        {
          text: '關於',
          items: [
            { text: '項目致謝', link: '/zh-hant/acknowledgements' },
          ],
        },
      ],
    },

    editLink: {
      pattern: 'https://github.com/vuejs/vitepress/edit/main/docs/:path',
      text: '在 GitHub 上編輯此頁面',
    },

    footer: {
      message: '基於 MIT 許可發布',
      copyright: `版權所有 © 2023-${new Date().getFullYear()} AmayaLab`,
    },

    docFooter: {
      prev: '上一頁',
      next: '下一頁',
    },

    outline: {
      level: [2, 3],
      label: '頁面導航',
    },

    lastUpdated: {
      text: '最後更新於',
    },

    notFound: {
      title: '頁面未找到',
      quote:
        '但如果你不改變方向，並且繼續尋找，你可能最終會到達你所前往的地方。',
      linkLabel: '前往首頁',
      linkText: '帶我回首頁',
    },

    langMenuLabel: '多語言',
    returnToTopLabel: '回到頂部',
    sidebarMenuLabel: '菜單',
    darkModeSwitchLabel: '主題',
    lightModeSwitchTitle: '切換到淺色模式',
    darkModeSwitchTitle: '切換到深色模式',
    skipToContentLabel: '跳轉到內容',
  },
})

function nav(): DefaultTheme.NavItem[] {
  return [
    { text: '本館介紹', link: '/zh-hant/about', activeMatch: '/zh-hant/about' },
    { text: '典籍索引', link: '/zh-hant/catalogue', activeMatch: '/zh-hant/catalogue' },
    {
      text: '館藏書庫',
      items: [
        { text: 'Vol. 01 管制物質：化學與法律指南', link: '/zh-hant/controlled-substances/' },
        { text: 'Vol. 02 火箭技術先驅：選集', link: '/rocket-pioneers/' },
      ],
    },
    {
      text: '項目致謝',
      link: '/zh-hant/acknowledgements',
      activeMatch: '/zh-hant/acknowledgements',
    },
  ]
}
