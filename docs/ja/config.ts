import type { DefaultTheme } from 'vitepress'
import { defineConfig } from 'vitepress'

export default defineConfig({
  lang: 'ja-JP',
  description: 'ヴワル魔法図書館 - 本の香りに満ちた禁忌の知識、すべてはこの館に。',

  themeConfig: {
    nav: nav(),

    sidebar: {
      '/ja/controlled-substances/': [
        {
          text: '規制物質：化学と法律のガイド',
          items: [
            { text: '概要と目次', link: '/ja/controlled-substances/' },
            { text: 'まえがきと専門家序文', link: '/ja/controlled-substances/forewords' },
            { text: '第1章：法的詳細と定義', link: '/ja/controlled-substances/chapter-1' },
            { text: '第2章：規制薬物とシノニム', link: '/ja/controlled-substances/chapter-2' },
            { text: '第3章：連邦薬物法の歴史', link: '/ja/controlled-substances/chapter-3' },
            { text: '第4章：分子構造式（全図版）', link: '/ja/controlled-substances/chapter-4' },
            { text: '第5章：DEA規制コード番号表', link: '/ja/controlled-substances/chapter-5' },
            { text: '第6章：官報判令・行政根拠', link: '/ja/controlled-substances/chapter-6' },
            { text: '第7章：実験式・化学索引', link: '/ja/controlled-substances/chapter-7' },
            { text: '付録：連邦規則と前駆物質', link: '/ja/controlled-substances/appendices' },
          ],
        },
      ],
      '/ja/': [
        {
          text: '図書館案内',
          items: [
            { text: '当館について：ヴワル魔法図書館', link: '/ja/about' },
          ],
        },
        {
          text: '所蔵文献',
          items: [
            { text: '規制物質：化学と法律のガイド', link: '/ja/controlled-substances/' },
          ],
        },
        {
          text: '概要',
          items: [
            { text: '謝辞', link: '/ja/acknowledgements' },
          ],
        },
      ],
    },

    editLink: {
      pattern: 'https://github.com/vuejs/vitepress/edit/main/docs/:path',
      text: 'GitHub でこのページを編集',
    },

    footer: {
      message: 'MIT ライセンスに基づき公開されています。',
      copyright: `Copyright © 2023-${new Date().getFullYear()} AmayaLab`,
    },

    docFooter: {
      prev: '前のページ',
      next: '次のページ',
    },

    outline: {
      level: [2, 3],
      label: '目次',
    },

    lastUpdated: {
      text: '最終更新日',
    },

    notFound: {
      title: 'ページが見つかりません',
      quote:
        '方向を変えずに探し続ければ、最終的には目的地にたどり着くことができるでしょう。',
      linkLabel: 'トップページへ',
      linkText: 'ホームへ戻る',
    },

    langMenuLabel: '言語切り替え',
    returnToTopLabel: 'ページ先頭へ',
    sidebarMenuLabel: 'メニュー',
    darkModeSwitchLabel: 'テーマ',
    lightModeSwitchTitle: 'ライトモードに切り替え',
    darkModeSwitchTitle: 'ダークモードに切り替え',
    skipToContentLabel: '本文へスキップ',
  },
})

function nav(): DefaultTheme.NavItem[] {
  return [
    {
      text: '当館について',
      link: '/ja/about',
      activeMatch: '/ja/about',
    },
    {
      text: '謝辞',
      link: '/ja/acknowledgements',
      activeMatch: '/ja/acknowledgements',
    },
  ]
}
