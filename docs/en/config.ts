import type { DefaultTheme } from 'vitepress'
import { defineConfig } from 'vitepress'

export default defineConfig({
  lang: 'en-US',
  description: 'Voile Magic Library - Forbidden knowledge with the scent of books, all within this library.',

  themeConfig: {
    nav: nav(),

    sidebar: {
      '/en/rocket-pioneers/': [
        {
          text: 'Pioneers of Rocket Technology: Selected Works',
          items: [
            { text: 'Overview & Table of Contents', link: '/en/rocket-pioneers/' },
            { text: 'Editorial Foreword: Soviet Astronautics', link: '/en/rocket-pioneers/preface' },
            { text: 'Part 1: Project for an Aeronautical Machine (Kibal\'chich)', link: '/en/rocket-pioneers/kibalchich' },
          ],
        },
        {
          text: 'Part 2: To Whoever Will Read to Build (Kondratyuk 1918–1919)',
          collapsed: false,
          items: [
            { text: 'Manuscript Overview & Reading Guide', link: '/en/rocket-pioneers/kondratyuk-build/' },
            { text: 'Section 1: Propulsion Principles & Velocity Equations', link: '/en/rocket-pioneers/kondratyuk-build/section-1' },
            { text: 'Section 2: Trajectory Ascent & Active Propellants', link: '/en/rocket-pioneers/kondratyuk-build/section-2' },
            { text: 'Section 3: Spacecraft Hull & Gyroscopic Orientation', link: '/en/rocket-pioneers/kondratyuk-build/section-3' },
            { text: 'Section 4: Nozzle Design & Retro-Braking Discoveries', link: '/en/rocket-pioneers/kondratyuk-build/section-4' },
            { text: 'Section 5: Gliding Reentry & Atmospheric Thermal Protection', link: '/en/rocket-pioneers/kondratyuk-build/section-5' },
            { text: 'Section 6: Solar Concentrators & Gravitational Slingshot', link: '/en/rocket-pioneers/kondratyuk-build/section-6' },
            { text: 'Editorial Historical Notes & Commentary', link: '/en/rocket-pioneers/kondratyuk-build/commentary' },
          ],
        },
        {
          text: 'Part 3: Conquest of Interplanetary Space (Kondratyuk 1929)',
          collapsed: false,
          items: [
            { text: 'Author\'s Preface & Guide to the Work', link: '/en/rocket-pioneers/kondratyuk-space/' },
            { text: 'Chapter 1: Flight Prerequisites & Laws of Motion', link: '/en/rocket-pioneers/kondratyuk-space/chapter-1' },
            { text: 'Chapter 2: Boost Phase Trajectory & Propellant Mass', link: '/en/rocket-pioneers/kondratyuk-space/chapter-2' },
            { text: 'Chapter 3: Exhaust Velocity & Chemical Energy', link: '/en/rocket-pioneers/kondratyuk-space/chapter-3' },
            { text: 'Chapter 4: Rocket Construction & Lightweight Design', link: '/en/rocket-pioneers/kondratyuk-space/chapter-4' },
            { text: 'Chapter 5: Structural Deadweight & Staging Optimization', link: '/en/rocket-pioneers/kondratyuk-space/chapter-5' },
            { text: 'Chapter 6: Passive Trajectories & Orbital Maneuvers', link: '/en/rocket-pioneers/kondratyuk-space/chapter-6' },
            { text: 'Chapter 7: Lunar Landing & Lunar Orbit Rendezvous (LOR)', link: '/en/rocket-pioneers/kondratyuk-space/chapter-7' },
            { text: 'Chapter 8: Atmospheric Effects on Boost Ascent', link: '/en/rocket-pioneers/kondratyuk-space/chapter-8' },
            { text: 'Chapter 9: Atmospheric Reentry & Hypersonic Thermal Shielding', link: '/en/rocket-pioneers/kondratyuk-space/chapter-9' },
            { text: 'Chapter 10: Space Relay Stations & Interplanetary Bases', link: '/en/rocket-pioneers/kondratyuk-space/chapter-10' },
            { text: 'Chapter 11: Solar Mirrors & Orbital Energy Systems', link: '/en/rocket-pioneers/kondratyuk-space/chapter-11' },
            { text: 'Chapter 12: Priority Claims & Historical Notes', link: '/en/rocket-pioneers/kondratyuk-space/chapter-12' },
            { text: 'Chapter 13: Urgent Fundamental Experiments', link: '/en/rocket-pioneers/kondratyuk-space/chapter-13' },
            { text: 'Editorial Mathematical Commentary & Derivations', link: '/en/rocket-pioneers/kondratyuk-space/commentary' },
          ],
        },
        {
          text: 'Part 4: Historical Outline of Rocket Pioneers',
          collapsed: false,
          items: [
            { text: 'Introduction & Early 19th Century Pioneers', link: '/en/rocket-pioneers/historical-outline/' },
            { text: 'Section 1: Tsiolkovskiy & Meshcherskiy', link: '/en/rocket-pioneers/historical-outline/section-1' },
            { text: 'Section 2: Tsander & Early Liquid-Propellant Engines', link: '/en/rocket-pioneers/historical-outline/section-2' },
            { text: 'Section 3: Kondratyuk\'s Theoretical Contributions', link: '/en/rocket-pioneers/historical-outline/section-3' },
            { text: 'Section 4: Summary of Research Groups (GDL/GIRD/RNII)', link: '/en/rocket-pioneers/historical-outline/section-4' },
          ],
        },
        {
          text: 'Appendix & Bibliography',
          items: [
            { text: 'Comprehensive Archival Index & Bibliography', link: '/en/rocket-pioneers/bibliography' },
          ],
        },
      ],
      '/en/fonts-encodings/': [
        {
          text: 'Front Matter',
          items: [
            { text: 'Overview & Table of Contents', link: '/en/fonts-encodings/' },
            { text: 'Introduction: Explorations', link: '/en/fonts-encodings/introduction' },
          ],
        },
        {
          text: 'Part I: Encodings & Unicode',
          collapsed: false,
          items: [
            { text: 'Chapter 1: Before Unicode', link: '/en/fonts-encodings/chapter-1' },
            { text: 'Chapter 2: Characters, Glyphs, Bytes', link: '/en/fonts-encodings/chapter-2' },
            { text: 'Chapter 3: Properties of Unicode Characters', link: '/en/fonts-encodings/chapter-3' },
            { text: 'Chapter 4: Normalization, Bidi & East Asian', link: '/en/fonts-encodings/chapter-4' },
            { text: 'Chapter 5: Using Unicode', link: '/en/fonts-encodings/chapter-5' },
          ],
        },
        {
          text: 'Part II: Font Management',
          collapsed: false,
          items: [
            { text: 'Chapter 6: Management on Macintosh', link: '/en/fonts-encodings/chapter-6' },
            { text: 'Chapter 7: Management under Windows', link: '/en/fonts-encodings/chapter-7' },
            { text: 'Chapter 8: Management under X Window', link: '/en/fonts-encodings/chapter-8' },
          ],
        },
        {
          text: 'Part III: Typographic Software & Web',
          collapsed: false,
          items: [
            { text: 'Chapter 9: Fonts in TeX and Omega', link: '/en/fonts-encodings/chapter-9' },
            { text: 'Chapter 10: Fonts and Web Pages', link: '/en/fonts-encodings/chapter-10' },
          ],
        },
        {
          text: 'Part IV: Typeface Art, Design & Typography',
          collapsed: false,
          items: [
            { text: 'Chapter 11: History and Classifications', link: '/en/fonts-encodings/chapter-11' },
            { text: 'Chapter 12: Creating and Modifying Fonts', link: '/en/fonts-encodings/chapter-12' },
            { text: 'Chapter 13: Optimizing a Rasterization', link: '/en/fonts-encodings/chapter-13' },
            { text: 'Chapter 14: Enriching Fonts: Advanced Typography', link: '/en/fonts-encodings/chapter-14' },
          ],
        },
        {
          text: 'Part V: Technical Reference',
          collapsed: false,
          items: [
            { text: 'Appendices A–G: Technical Reference Manual', link: '/en/fonts-encodings/appendices' },
          ],
        },
      ],
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
            { text: 'Vol. 02 Pioneers of Rocket Technology', link: '/en/rocket-pioneers/' },
            { text: 'Vol. 03 Fonts & Encodings: Complete Guide', link: '/en/fonts-encodings/' },
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
      pattern: 'https://github.com/AmayaLab2026/voile-magic-library/edit/main/docs/:path',
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
        { text: 'Vol. 02 Pioneers of Rocket Technology', link: '/en/rocket-pioneers/' },
        { text: 'Vol. 03 Fonts & Encodings: Complete Guide', link: '/en/fonts-encodings/' },
      ],
    },
    {
      text: 'Acknowledgements',
      link: '/en/acknowledgements',
      activeMatch: '/en/acknowledgements',
    },
  ]
}
