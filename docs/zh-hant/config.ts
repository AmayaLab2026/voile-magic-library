import type { DefaultTheme } from 'vitepress'
import { defineConfig } from 'vitepress'

export default defineConfig({
  lang: 'zh-Hant',
  description: 'ヴワル魔法図書館 - 散發著書香的禁忌之識，盡在本館',

  themeConfig: {
    nav: nav(),

    sidebar: {
      '/zh-hant/rocket-pioneers/': [
        {
          text: '火箭技術先驅：選集',
          items: [
            { text: '典籍概述與全書目錄', link: '/zh-hant/rocket-pioneers/' },
            { text: '主編序言：蘇聯航太歷程與先驅評述', link: '/zh-hant/rocket-pioneers/preface' },
            { text: '第一編：航空機器設想（基巴利契奇）', link: '/zh-hant/rocket-pioneers/kibalchich' },
          ],
        },
        {
          text: '第二編：致讀此書以建造者（孔德拉秋克 1918–1919）',
          collapsed: false,
          items: [
            { text: '手稿全貌與工程奠基導讀', link: '/zh-hant/rocket-pioneers/kondratyuk-build/' },
            { text: '第一章：噴氣推進原理與速度方程', link: '/zh-hant/rocket-pioneers/kondratyuk-build/section-1' },
            { text: '第二章：軌道爬升方案與活性推進劑', link: '/zh-hant/rocket-pioneers/kondratyuk-build/section-2' },
            { text: '第三章：飛船結構與陀螺儀定向', link: '/zh-hant/rocket-pioneers/kondratyuk-build/section-3' },
            { text: '第四章：噴管設計與返回制動發現', link: '/zh-hant/rocket-pioneers/kondratyuk-build/section-4' },
            { text: '第五章：滑翔再入與大氣減速防熱', link: '/zh-hant/rocket-pioneers/kondratyuk-build/section-5' },
            { text: '第六章：太陽能聚能鏡與引力彈弓', link: '/zh-hant/rocket-pioneers/kondratyuk-build/section-6' },
            { text: '編委會文獻考證與技術評注', link: '/zh-hant/rocket-pioneers/kondratyuk-build/commentary' },
          ],
        },
        {
          text: '第三編：征服星際空間（孔德拉秋克 1929）',
          collapsed: false,
          items: [
            { text: '作者自序與全書導覽', link: '/zh-hant/rocket-pioneers/kondratyuk-space/' },
            { text: '第 1 章：星際飛行前提與運行規律', link: '/zh-hant/rocket-pioneers/kondratyuk-space/chapter-1' },
            { text: '第 2 章：主動段加速與多級載荷公式', link: '/zh-hant/rocket-pioneers/kondratyuk-space/chapter-2' },
            { text: '第 3 章：排氣速度與推進劑化學熱值', link: '/zh-hant/rocket-pioneers/kondratyuk-space/chapter-3' },
            { text: '第 4 章：火箭結構與輕量化工程設計', link: '/zh-hant/rocket-pioneers/kondratyuk-space/chapter-4' },
            { text: '第 5 章：結構死重佔比與級數優化', link: '/zh-hant/rocket-pioneers/kondratyuk-space/chapter-5' },
            { text: '第 6 章：空間慣性飛行軌道與變軌', link: '/zh-hant/rocket-pioneers/kondratyuk-space/chapter-6' },
            { text: '第 7 章：登月與月球軌道交會（LOR）', link: '/zh-hant/rocket-pioneers/kondratyuk-space/chapter-7' },
            { text: '第 8 章：大氣層對主動段爬升的影響', link: '/zh-hant/rocket-pioneers/kondratyuk-space/chapter-8' },
            { text: '第 9 章：再入大氣減速與超高速防熱', link: '/zh-hant/rocket-pioneers/kondratyuk-space/chapter-9' },
            { text: '第 10 章：空間中繼站與行星際基地', link: '/zh-hant/rocket-pioneers/kondratyuk-space/chapter-10' },
            { text: '第 11 章：太陽能聚能鏡與能源利用', link: '/zh-hant/rocket-pioneers/kondratyuk-space/chapter-11' },
            { text: '第 12 章：研究優先權與歷史說明', link: '/zh-hant/rocket-pioneers/kondratyuk-space/chapter-12' },
            { text: '第 13 章：亟待開展的基礎實驗清單', link: '/zh-hant/rocket-pioneers/kondratyuk-space/chapter-13' },
            { text: '編注與理論數學推導附錄', link: '/zh-hant/rocket-pioneers/kondratyuk-space/commentary' },
          ],
        },
        {
          text: '第四編：俄羅斯與蘇聯火箭先驅歷史綱要',
          collapsed: false,
          items: [
            { text: '歷史綱要引言與 19 世紀早期先驅', link: '/zh-hant/rocket-pioneers/historical-outline/' },
            { text: '第一章：齊奧爾科夫斯基與梅謝爾斯基', link: '/zh-hant/rocket-pioneers/historical-outline/section-1' },
            { text: '第二章：燦德爾與早期火箭發動機研發', link: '/zh-hant/rocket-pioneers/historical-outline/section-2' },
            { text: '第三章：孔德拉秋克對航太理論的貢獻', link: '/zh-hant/rocket-pioneers/historical-outline/section-3' },
            { text: '第四章：早期機構（GDL/GIRD/RNII）總結', link: '/zh-hant/rocket-pioneers/historical-outline/section-4' },
          ],
        },
        {
          text: '附錄與文獻索引',
          items: [
            { text: '先驅著作與歷史文獻全景索引', link: '/zh-hant/rocket-pioneers/bibliography' },
          ],
        },
      ],
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
            { text: 'Vol. 02 火箭技術先驅：選集', link: '/zh-hant/rocket-pioneers/' },
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
      pattern: 'https://github.com/AmayaLab2026/voile-magic-library/edit/main/docs/:path',
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
        { text: 'Vol. 02 火箭技術先驅：選集', link: '/zh-hant/rocket-pioneers/' },
      ],
    },
    {
      text: '項目致謝',
      link: '/zh-hant/acknowledgements',
      activeMatch: '/zh-hant/acknowledgements',
    },
  ]
}
