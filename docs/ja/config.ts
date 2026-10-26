import type { DefaultTheme } from 'vitepress'
import { defineConfig } from 'vitepress'

export default defineConfig({
  lang: 'ja-JP',
  description: 'ヴワル魔法図書館 - 本の香りに満ちた禁忌の知識、すべてはこの館に。',

  themeConfig: {
    nav: nav(),

    sidebar: {
      '/ja/rocket-pioneers/': [
        {
          text: 'ロケット技術の先駆者たち：選集',
          items: [
            { text: '概要と全巻目次', link: '/ja/rocket-pioneers/' },
            { text: '主編序言：ソ連宇宙開発の歩みと先駆者評伝', link: '/ja/rocket-pioneers/preface' },
            { text: '第一編：航空機械の構想（キバリチッチ 1881）', link: '/ja/rocket-pioneers/kibalchich' },
          ],
        },
        {
          text: '第二編：建造を期して本書を読む者へ（コンドラチュク 1918–1919）',
          collapsed: false,
          items: [
            { text: '手稿全貌と工学的礎石の解題', link: '/ja/rocket-pioneers/kondratyuk-build/' },
            { text: '第1章：噴射推進の基本原理と理想速度方程式', link: '/ja/rocket-pioneers/kondratyuk-build/section-1' },
            { text: '第2章：軌道上昇計画、抗過重と活性推進剤', link: '/ja/rocket-pioneers/kondratyuk-build/section-2' },
            { text: '第3章：宇宙船構造、多段分離とジャイロ姿勢制御', link: '/ja/rocket-pioneers/kondratyuk-build/section-3' },
            { text: '第4章：ノズル設計、天体指向と帰還制動の発見', link: '/ja/rocket-pioneers/kondratyuk-build/section-4' },
            { text: '第5章：滑空再突入、大気減速と熱防護', link: '/ja/rocket-pioneers/kondratyuk-build/section-5' },
            { text: '第6章：太陽光集光鏡、重力スイングバイと軌道基地', link: '/ja/rocket-pioneers/kondratyuk-build/section-6' },
            { text: '編集委員会による文献考証と技術注記', link: '/ja/rocket-pioneers/kondratyuk-build/commentary' },
          ],
        },
        {
          text: '第三編：惑星間空間の征服（コンドラチュク 1929）',
          collapsed: false,
          items: [
            { text: '著者自序と全編解題', link: '/ja/rocket-pioneers/kondratyuk-space/' },
            { text: '第1章：惑星間飛行の前提条件とロケット運行法則', link: '/ja/rocket-pioneers/kondratyuk-space/chapter-1' },
            { text: '第2章：能動加速段軌道と多段推進剤積載公式', link: '/ja/rocket-pioneers/kondratyuk-space/chapter-2' },
            { text: '第3章：排気速度と推進剤の化学反応発熱量', link: '/ja/rocket-pioneers/kondratyuk-space/chapter-3' },
            { text: '第4章：ロケット構造と軽量化設計工学', link: '/ja/rocket-pioneers/kondratyuk-space/chapter-4' },
            { text: '第5章：構造自重比と最適多段化理論', link: '/ja/rocket-pioneers/kondratyuk-space/chapter-5' },
            { text: '第6章：慣性飛行軌道と軌道遷移', link: '/ja/rocket-pioneers/kondratyuk-space/chapter-6' },
            { text: '第7章：月面着陸と月軌道ランデブー（LOR）', link: '/ja/rocket-pioneers/kondratyuk-space/chapter-7' },
            { text: '第8章：大気層が能動上昇段に及ぼす影響', link: '/ja/rocket-pioneers/kondratyuk-space/chapter-8' },
            { text: '第9章：大気減速再突入と極超音速熱防護', link: '/ja/rocket-pioneers/kondratyuk-space/chapter-9' },
            { text: '第10章：宇宙中継基地と惑星間拠点', link: '/ja/rocket-pioneers/kondratyuk-space/chapter-10' },
            { text: '第11章：太陽光集光鏡と宇宙エネルギー利用', link: '/ja/rocket-pioneers/kondratyuk-space/chapter-11' },
            { text: '第12章：研究の優先権と歴史的経緯の覚書', link: '/ja/rocket-pioneers/kondratyuk-space/chapter-12' },
            { text: '第13章：緊急に実施すべき基礎実験一覧', link: '/ja/rocket-pioneers/kondratyuk-space/chapter-13' },
            { text: '編集注記と理論力学導出付録', link: '/ja/rocket-pioneers/kondratyuk-space/commentary' },
          ],
        },
        {
          text: '第四編：ロシアおよびソ連におけるロケット先駆者の歴史的概説',
          collapsed: false,
          items: [
            { text: '歴史概説 序言と19世紀初期の先駆者たち', link: '/ja/rocket-pioneers/historical-outline/' },
            { text: '第1章：ツィオルコフスキーとメシチェルスキー', link: '/ja/rocket-pioneers/historical-outline/section-1' },
            { text: '第2章：ツァンダーと初期液体ロケットエンジンの開発', link: '/ja/rocket-pioneers/historical-outline/section-2' },
            { text: '第3章：コンドラチュクの宇宙航行理論への貢献', link: '/ja/rocket-pioneers/historical-outline/section-3' },
            { text: '第4章：初期研究機関（GDL/GIRD/RNII）の総括', link: '/ja/rocket-pioneers/historical-outline/section-4' },
          ],
        },
        {
          text: '付録・文献索引',
          items: [
            { text: '先駆者の著作および歴史文献全景索引', link: '/ja/rocket-pioneers/bibliography' },
          ],
        },
      ],
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
            { text: '蔵書目録索引', link: '/ja/catalogue' },
          ],
        },
        {
          text: '所蔵文献',
          items: [
            { text: 'Vol. 01 規制物質：化学と法律のガイド', link: '/ja/controlled-substances/' },
            { text: 'Vol. 02 ロケット技術の先駆者たち：選集', link: '/ja/rocket-pioneers/' },
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
      pattern: 'https://github.com/AmayaLab2026/voile-magic-library/edit/main/docs/:path',
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
      text: '蔵書目録',
      link: '/ja/catalogue',
      activeMatch: '/ja/catalogue',
    },
    {
      text: '蔵書庫',
      items: [
        { text: 'Vol. 01 規制物質：化学と法律のガイド', link: '/ja/controlled-substances/' },
        { text: 'Vol. 02 ロケット技術の先駆者たち：選集', link: '/ja/rocket-pioneers/' },
      ],
    },
    {
      text: '謝辞',
      link: '/ja/acknowledgements',
      activeMatch: '/ja/acknowledgements',
    },
  ]
}
