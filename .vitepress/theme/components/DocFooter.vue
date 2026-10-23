<script setup lang="ts">
import { useData, useRoute } from 'vitepress'
import { computed } from 'vue'

const route = useRoute()
const { frontmatter, lang } = useData()

const isAcknowledgements = computed(() => {
  if (frontmatter.value?.hideReprintNotice)
    return true
  return route.path.includes('acknowledgements')
})

const isControlledSubstances = computed(() => {
  return route.path.includes('controlled-substances')
})

const isRocketPioneers = computed(() => {
  return route.path.includes('rocket-pioneers')
})

const isZh = computed(() => {
  if (lang.value)
    return lang.value.startsWith('zh')
  return !route.path.startsWith('/en') && !route.path.startsWith('/ja')
})

const rocketPioneersAuthors = computed(() => {
  return isZh.value
    ? 'N. I. 基巴利契奇、K. E. 齐奥尔科夫斯基、F. A. 灿德尔、Yu. V. 孔德拉秋克 等 / 编撰：V. N. 索科利斯基 博士'
    : 'N. I. Kibal\'chich, K. E. Tsiolkovskiy, F. A. Tsander, Yu. V. Kondratyuk / Ed. Dr. V. N. Sokol\'skiy'
})
</script>

<template>
  <div v-if="!isAcknowledgements" class="book-attribution-card mt-12 rounded-2xl p-5 transition-all">
    <!-- 管制物质：联邦药物法的化学与法律指南 专属索书号与著者卡片 -->
    <div v-if="isControlledSubstances">
      <div flex="~ items-center gap-2" text-sm font-semibold class="text-$vp-c-brand">
        <span class="i-carbon:book-reference" />
        <span>{{ isZh ? '馆藏典籍索引 · 索书与著者信息' : 'Library Catalog & Book Call Card' }}</span>
      </div>

      <div class="grid mt-3 gap-2 text-xs text-$vp-c-text-2">
        <div flex="~ wrap items-center gap-x-6 gap-y-1.5">
          <div>
            <span font-medium class="text-$vp-c-text-1">{{ isZh ? '著者' : 'Author' }}：</span>
            <span font-medium class="text-$vp-c-text-1">Alexander T. Shulgin, Ph.D.（亚历山大·T·舒尔金 博士）</span>
          </div>
          <div>
            <span font-medium class="text-$vp-c-text-1">{{ isZh ? '馆藏索书号' : 'Call No.' }}：</span>
            <code class="rounded bg-$vp-c-brand-soft px-2 py-0.5 text-$vp-c-brand font-bold font-mono">VML-KF3890.S58-1992</code>
          </div>
          <div>
            <span font-medium class="text-$vp-c-text-1">ISBN：</span>
            <span class="font-semibold font-mono">0-914171-50-X</span>
          </div>
        </div>

        <div flex="~ wrap items-center gap-x-6 gap-y-1" class="mt-1 text-xs opacity-90">
          <div>
            <span font-medium class="text-$vp-c-text-1">{{ isZh ? '典籍原名' : 'Original Work' }}：</span>
            <span italic>Controlled Substances: A Chemical and Legal Guide to the Federal Drug Laws (2nd Edition, 1992)</span>
          </div>
          <div>
            <span font-medium class="text-$vp-c-text-1">{{ isZh ? '出版机构' : 'Publisher' }}：</span>
            <span>Ronin Publishing, Inc. (Berkeley, CA)</span>
          </div>
          <div>
            <span font-medium class="text-$vp-c-text-1">{{ isZh ? '馆藏库位' : 'Archive' }}：</span>
            <span>ヴワル魔法図書館 · 特藏文献室</span>
          </div>
        </div>
      </div>
    </div>

    <!-- 俄罗斯火箭技术先驱：选集（1881–1933）专属索书号与著者卡片 -->
    <div v-else-if="isRocketPioneers">
      <div flex="~ items-center gap-2" text-sm font-semibold class="text-$vp-c-brand">
        <span class="i-carbon:book-reference" />
        <span>{{ isZh ? '馆藏典籍索引 · 索书与著者信息' : 'Library Catalog & Book Call Card' }}</span>
      </div>

      <div class="grid mt-3 gap-2 text-xs text-$vp-c-text-2">
        <div flex="~ wrap items-center gap-x-6 gap-y-1.5">
          <div>
            <span font-medium class="text-$vp-c-text-1">{{ isZh ? '著者' : 'Authors' }}：</span>
            <span font-medium class="text-$vp-c-text-1">{{ rocketPioneersAuthors }}</span>
          </div>
          <div>
            <span font-medium class="text-$vp-c-text-1">{{ isZh ? '馆藏索书号' : 'Call No.' }}：</span>
            <code class="rounded bg-$vp-c-brand-soft px-2 py-0.5 text-$vp-c-brand font-bold font-mono">VML-TL781.P56-1965</code>
          </div>
          <div>
            <span font-medium class="text-$vp-c-text-1">{{ isZh ? '文献编号' : 'Report No.' }}：</span>
            <span class="font-semibold font-mono">NASA TT F-9285 / TT 65-50114</span>
          </div>
        </div>

        <div flex="~ wrap items-center gap-x-6 gap-y-1" class="mt-1 text-xs opacity-90">
          <div>
            <span font-medium class="text-$vp-c-text-1">{{ isZh ? '典籍原名' : 'Original Work' }}：</span>
            <span italic>Pioneers of Rocket Technology: Selected Works (Пионеры ракетной техники: Избранные труды)</span>
          </div>
          <div>
            <span font-medium class="text-$vp-c-text-1">{{ isZh ? '出版机构' : 'Publisher' }}：</span>
            <span>NASA (Washington, D.C.) / Nauka (Moscow) / IPST (Jerusalem)</span>
          </div>
          <div>
            <span font-medium class="text-$vp-c-text-1">{{ isZh ? '馆藏库位' : 'Archive' }}：</span>
            <span>ヴワル魔法図書館 · 特藏文献室</span>
          </div>
        </div>
      </div>
    </div>

    <!-- 其他通用页面 -->
    <div v-else>
      <div flex="~ items-center gap-2" text-sm font-semibold class="text-$vp-c-brand">
        <span class="i-carbon:library" />
        <span>{{ isZh ? '馆藏文献阅览说明' : 'Voile Magic Library Notice' }}</span>
      </div>
      <p class="mt-2 text-xs text-$vp-c-text-2 leading-relaxed">
        {{ isZh ? '本站所有数字化文献与学术译本归档于 ヴワル魔法図書館，供学术研讨、法庭科学与知识传播查阅。更多开源与技术致谢请参阅' : 'Archived at Voile Magic Library for academic, forensic, and educational purposes. See ' }}
        <a :href="isZh ? '/zh/acknowledgements' : '/acknowledgements'" class="text-$vp-c-brand font-medium hover:underline">
          {{ isZh ? '项目致谢独立页面 →' : 'Acknowledgements →' }}
        </a>
      </p>
    </div>
  </div>
</template>

<style scoped>
.book-attribution-card {
  border: 1px solid var(--vp-c-border);
  background-color: var(--vp-c-bg-elv);
  box-shadow: 0 4px 18px -2px rgba(0, 0, 0, 0.03);
}
</style>
