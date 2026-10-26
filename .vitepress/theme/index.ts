import type { Theme } from 'vitepress'

import { presetClient } from '@nolebase/integrations/vitepress/client'
import DefaultTheme from 'vitepress/theme'
import { h } from 'vue'

import AppContainer from './components/AppContainer.vue'
import AppearanceToggleTransition from './components/AppearanceToggleTransition.vue'
import ComponentInHeader from './components/ComponentInHeader.vue'
import DocFooter from './components/DocFooter.vue'
import ModalDemo from './components/ModalDemo.vue'
import Share from './components/Share.vue'

import 'virtual:uno.css'
import '../styles/main.css'
import '../styles/vars.css'

const nolebase = presetClient<{
  tags: string[]
  progress: number
}>({
  gitChangelog: false,
  pageProperties: false,
  enhancedReadabilities: {
    options: {
      layoutSwitch: {
        defaultMode: 4,
      },
      spotlight: {
        defaultToggle: false,
        hoverBlockColor: 'rgb(240 197 52 / 7%)',
      },
    },
  },
})

const ExtendedTheme: Theme = {
  extends: DefaultTheme,
  Layout: () => {
    const slots = nolebase!.enhanceLayout?.() ?? {}

    return h(DefaultTheme.Layout, null, {
      // https://vitepress.dev/guide/extending-default-theme#layout-slots
      'doc-top': () => [
        ...(slots['doc-top']?.map(slot => slot()) ?? []),
      ],
      'doc-footer-before': () => [
        h(DocFooter),
      ],
      'nav-bar-content-after': () => [
        h(Share),
        ...(slots['nav-bar-content-after']?.map(slot => slot()) ?? []),
      ],
      'nav-screen-content-after': () => [
        ...(slots['nav-screen-content-after']?.map(slot => slot()) ?? []),
      ],
    })
  },
  async enhanceApp(ctx) {
    const { app, siteData } = ctx

    await nolebase?.enhanceApp?.(ctx)

    if (typeof window !== 'undefined' && siteData?.value) {
      const year = new Date().getFullYear()
      const syncCopyright = (config: any) => {
        if (config?.footer?.copyright && typeof config.footer.copyright === 'string') {
          config.footer.copyright = config.footer.copyright.replace(/2023(-\d*)?/, () => {
            return year > 2023 ? `2023-${year}` : '2023'
          })
        }
      }
      syncCopyright(siteData.value.themeConfig)
      if (siteData.value.locales) {
        Object.values(siteData.value.locales).forEach((locale: any) => {
          syncCopyright(locale?.themeConfig)
        })
      }
    }

    app.component('DocFooter', DocFooter)
    app.component('Share', Share)
    app.component('AppContainer', AppContainer)
    app.component('ModalDemo', ModalDemo)
    app.component('ComponentInHeader', ComponentInHeader)
    app.component('AppearanceToggleTransition', AppearanceToggleTransition)
  },
}

export default ExtendedTheme
