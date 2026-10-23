import { presetMarkdownIt } from '@nolebase/integrations/vitepress/markdown-it'
import { presetVite } from '@nolebase/integrations/vitepress/vite'
import { transformHeadMeta } from '@nolebase/vitepress-plugin-meta'
import MarkdownItFootnote from 'markdown-it-footnote'
import UnoCSS from 'unocss/vite'
import Components from 'unplugin-vue-components/vite'
import { defineConfig } from 'vitepress'
import Inspect from 'vite-plugin-inspect'

import enConfig from '../docs/en/config'
import jaConfig from '../docs/ja/config'
import { githubRepoLink, siteDescription, siteName } from '../metadata/index'
import zhConfig from '../docs/zh/config'
import zhHantConfig from '../docs/zh-hant/config'
import head from './head'

const nolebase = presetMarkdownIt()
const nolebaseVite = presetVite({
  // Match the client preset: changelog rendering is disabled in the theme.
  // The collector also writes Git config, which restricted deploys disallow.
  gitChangelog: false,
})

export default defineConfig({
  base: process.env.VITEPRESS_BASE || '/',
  srcDir: 'docs',
  vue: {
    template: {
      transformAssetUrls: {
        video: ['src', 'poster'],
        source: ['src'],
        img: ['src'],
        image: ['xlink:href', 'href'],
        use: ['xlink:href', 'href'],
        NolebaseUnlazyImg: ['src'],
      },
    },
  },
  vite: {
    assetsInclude: ['**/*.mov'],
    optimizeDeps: {
      exclude: ['vitepress'],
    },
    ssr: {
      noExternal: [
        /@nolebase\/.*/,
        /@unlazy\/.*/,
      ],
    },
    plugins: [
      // The client preset's optional dynamic imports are resolved even when
      // changelog rendering is disabled. Supply its unused data module without
      // enabling the Git collector (which writes repository configuration).
      {
        name: 'disabled-git-changelog-data',
        resolveId(id) {
          if (id === 'virtual:nolebase-git-changelog')
            return '\0virtual:nolebase-git-changelog'
        },
        load(id) {
          if (id === '\0virtual:nolebase-git-changelog')
            return 'export default { commits: [], authors: [] }'
        },
      },
      Inspect(),
      Components({
        include: [/\.vue$/, /\.md$/],
        dirs: '.vitepress/theme/components',
        dts: '.vitepress/components.d.ts',
      }),
      UnoCSS(),
      nolebaseVite,
      ...nolebaseVite.plugins(),
    ],
  },
  title: siteName,
  description: siteDescription,
  ignoreDeadLinks: true,
  head,
  rewrites: {
    'zh/:rest*': ':rest*',
  },
  themeConfig: {
    logo: { src: '/naruto.svg', width: 24, height: 24, alt: 'Voile' },
    outline: {
      level: [2, 3],
      label: '本页导览',
    },
    socialLinks: [
      { icon: 'github', link: githubRepoLink },
    ],
    footer: {
      message: 'Released under the MIT License.',
      copyright: `Copyright © 2023-${new Date().getFullYear()} AmayaLab`,
    },
    search: {
      provider: 'local',
      options: {
        locales: {
          zh: {
            translations: {
              button: {
                buttonText: '搜索文档',
                buttonAriaLabel: '搜索文档',
              },
              modal: {
                noResultsText: '无法找到相关结果',
                resetButtonTitle: '清除查询条件',
                footer: {
                  selectText: '选择',
                  navigateText: '切换',
                },
              },
            },
          },
          'zh-hant': {
            translations: {
              button: {
                buttonText: '搜尋文檔',
                buttonAriaLabel: '搜尋文檔',
              },
              modal: {
                noResultsText: '無法找到相關結果',
                resetButtonTitle: '清除查詢條件',
                footer: {
                  selectText: '選擇',
                  navigateText: '切換',
                },
              },
            },
          },
          ja: {
            translations: {
              button: {
                buttonText: 'ドキュメントを検索',
                buttonAriaLabel: 'ドキュメントを検索',
              },
              modal: {
                noResultsText: '検索結果が見つかりません',
                resetButtonTitle: '検索条件をクリア',
                footer: {
                  selectText: '選択',
                  navigateText: '切り替え',
                },
              },
            },
          },
        },
      },
    },
  },
  locales: {
    root: {
      label: '简体中文',
      lang: 'zh-Hans',
      ...zhConfig,
    },
    en: {
      label: 'English',
      lang: 'en-US',
      link: '/en/',
      ...enConfig,
    },
    'zh-hant': {
      label: '繁體中文',
      lang: 'zh-Hant',
      link: '/zh-hant/',
      ...zhHantConfig,
    },
    ja: {
      label: '日本語',
      lang: 'ja-JP',
      link: '/ja/',
      ...jaConfig,
    },
  },
  markdown: {
    theme: {
      light: 'github-light',
      dark: 'one-dark-pro',
    },
    math: true,
    preConfig: async (md) => {
      await nolebase.install(md)
    },
    config: (md) => {
      md.use(MarkdownItFootnote as any)

      // Strip MathJax styles; VitePress already adds v-pre and block tabindex.
      const origMathInline = md.renderer.rules.math_inline
      if (origMathInline) {
        md.renderer.rules.math_inline = function (...args) {
          const res = origMathInline.apply(this, args)
          return res.replace(/<style[\s\S]*?<\/style>/gi, '')
        }
      }

      const origMathBlock = md.renderer.rules.math_block
      if (origMathBlock) {
        md.renderer.rules.math_block = function (...args) {
          const res = origMathBlock.apply(this, args)
          return res.replace(/<style[\s\S]*?<\/style>/gi, '')
        }
      }
    },
  },
  async transformHead(context) {
    let head = [...context.head]

    const returnedHead = await transformHeadMeta()(head, context)
    if (typeof returnedHead !== 'undefined')
      head = returnedHead

    return head
  },
})
