import type { DefaultTheme } from 'vitepress'
import { defineConfig } from 'vitepress'

export default defineConfig({
  lang: 'en-US',
  description: 'Voile Magic Library - Forbidden knowledge with the scent of books, all within this library.',

  themeConfig: {
    nav: nav(),

    sidebar: {
      '/en/controlled-substances/': [
        {
          text: 'Controlled Substances: Guide',
          items: [
            { text: 'Overview & Table of Contents', link: '/en/controlled-substances/' },
            { text: 'Forewords & Introduction', link: '/en/controlled-substances/forewords' },
            { text: 'Chapter 1: Legal Details & Definitions', link: '/en/controlled-substances/chapter-1' },
            { text: 'Chapter 2: Scheduled Drugs & Synonyms', link: '/en/controlled-substances/chapter-2' },
            { text: 'Chapter 3: History of Drug Laws', link: '/en/controlled-substances/chapter-3' },
            { text: 'Chapter 4: Molecular Structures', link: '/en/controlled-substances/chapter-4' },
            { text: 'Chapter 5: DEA Code Numbers', link: '/en/controlled-substances/chapter-5' },
            { text: 'Chapter 6: Federal Register Citations', link: '/en/controlled-substances/chapter-6' },
            { text: 'Chapter 7: Empirical Formulas Index', link: '/en/controlled-substances/chapter-7' },
            { text: 'Appendices: Regulations & Precursors', link: '/en/controlled-substances/appendices' },
          ],
        },
      ],
      '/en/': [
        {
          text: 'Library Guide',
          items: [
            { text: 'About: Voile Magic Library', link: '/en/about' },
            { text: 'Library Catalogue', link: '/en/catalogue' },
          ],
        },
        {
          text: 'Collections',
          items: [
            { text: 'Vol. 01 Controlled Substances Guide', link: '/en/controlled-substances/' },
            { text: 'Vol. 02 Pioneers of Rocket Technology', link: '/rocket-pioneers/' },
          ],
        },
        {
          text: 'About',
          items: [
            { text: 'Acknowledgements', link: '/en/acknowledgements' },
          ],
        },
      ],
    },

    editLink: {
      pattern: 'https://github.com/vuejs/vitepress/edit/main/docs/:path',
      text: 'Edit this page on GitHub',
    },

    footer: {
      message: 'Released under the MIT License.',
      copyright: `Copyright © 2023-${new Date().getFullYear()} AmayaLab`,
    },

    docFooter: {
      prev: 'Previous page',
      next: 'Next page',
    },

    outline: {
      level: [2, 3],
      label: 'On this page',
    },

    lastUpdated: {
      text: 'Last updated',
    },

    notFound: {
      title: 'PAGE NOT FOUND',
      quote:
        'But if you don\'t change your direction, and if you keep looking, you may end up where you are heading.',
      linkLabel: 'go to home',
      linkText: 'Take me home',
    },

    langMenuLabel: 'Change language',
    returnToTopLabel: 'Return to top',
    sidebarMenuLabel: 'Menu',
    darkModeSwitchLabel: 'Appearance',
    lightModeSwitchTitle: 'Switch to light theme',
    darkModeSwitchTitle: 'Switch to dark theme',
    skipToContentLabel: 'Skip to content',
  },
})

function nav(): DefaultTheme.NavItem[] {
  return [
    {
      text: 'About',
      link: '/en/about',
      activeMatch: '/en/about',
    },
    {
      text: 'Catalogue',
      link: '/en/catalogue',
      activeMatch: '/en/catalogue',
    },
    {
      text: 'Collections',
      items: [
        { text: 'Vol. 01 Controlled Substances Guide', link: '/en/controlled-substances/' },
        { text: 'Vol. 02 Pioneers of Rocket Technology', link: '/rocket-pioneers/' },
      ],
    },
    {
      text: 'Acknowledgements',
      link: '/en/acknowledgements',
      activeMatch: '/en/acknowledgements',
    },
  ]
}
