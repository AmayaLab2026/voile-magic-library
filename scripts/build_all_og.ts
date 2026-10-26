import fs from 'node:fs'
import path from 'node:path'
import process from 'node:process'
import { fileURLToPath } from 'node:url'
import matter from 'gray-matter'
import { renderOGImage } from './og_generator'

const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)
const docsDir = path.resolve(__dirname, '../docs')
const publicOgDir = path.resolve(__dirname, '../public/og')
const docsPublicOgDir = path.resolve(__dirname, '../docs/public/og')

interface PageMeta {
  filePath: string
  urlPath: string
  slug: string
  title: string
  category: string
  callNo?: string
  author?: string
  lang: string
}

function getAllMarkdownFiles(dir: string, base = ''): string[] {
  const entries = fs.readdirSync(dir, { withFileTypes: true })
  let files: string[] = []
  for (const entry of entries) {
    if (entry.name === 'public' || entry.name === 'node_modules' || entry.name.startsWith('.'))
      continue
    const fullPath = path.join(dir, entry.name)
    const relPath = path.join(base, entry.name)
    if (entry.isDirectory()) {
      files = files.concat(getAllMarkdownFiles(fullPath, relPath))
    }
    else if (entry.isFile() && entry.name.endsWith('.md')) {
      files.push(relPath)
    }
  }
  return files
}

export function resolvePageMeta(relPath: string): PageMeta {
  const fullPath = path.join(docsDir, relPath)
  const content = fs.readFileSync(fullPath, 'utf-8')
  let data: Record<string, any> = {}
  let body = content

  try {
    const parsed = matter(content)
    data = parsed.data || {}
    body = parsed.content || content
  }
  catch {
    // Fallback: extract title/description manually if YAML contains unquoted colons
    for (const line of content.split('\n')) {
      const trimmed = line.trim()
      if (trimmed.startsWith('title:')) {
        data.title = trimmed.slice(6).trim().replace(/^["']|["']$/g, '')
        break
      }
    }
    const cleanBody = content.replace(/^---[\s\S]*?---/, '')
    body = cleanBody || content
  }

  // Determine language
  const normalized = relPath.replace(/\\/g, '/')
  let lang = 'zh'
  if (normalized.startsWith('en/')) {
    lang = 'en'
  }
  else if (normalized.startsWith('ja/')) {
    lang = 'ja'
  }
  else if (normalized.startsWith('zh-hant/')) {
    lang = 'zh-hant'
  }

  // URL Path
  // rewrites: 'zh/:rest*' -> ':rest*'
  let urlPath = `/${normalized.replace(/\.md$/, '')}`
  if (normalized.startsWith('zh/')) {
    urlPath = `/${normalized.slice(3).replace(/\.md$/, '')}`
  }
  if (urlPath.endsWith('/index'))
    urlPath = urlPath.slice(0, -5) || '/'

  // Slug for OG Image
  let slug = urlPath.replace(/^\//, '').replace(/\/$/, '').replace(/\//g, '--')
  if (!slug)
    slug = 'index'
  if (lang !== 'zh' && slug === 'index')
    slug = `${lang}-index`

  // Title extraction
  let title = data.title
  if (!title) {
    for (const line of body.split('\n')) {
      const trimmed = line.trim()
      if (trimmed.startsWith('# ')) {
        title = trimmed.slice(2).replace(/\{#[^}]+\}/, '').trim()
        break
      }
    }
  }
  if (!title) {
    title = slug
  }

  // Book Category, Call No, and Author extraction
  let category = 'ヴワル魔法図書館 · 藏书'
  let callNo: string | undefined
  let author: string | undefined

  const isHome = urlPath === '/' || urlPath === '/en/' || urlPath === '/ja/' || urlPath === '/zh-hant/'
  if (isHome) {
    if (lang === 'en') {
      title = 'Voile Magic Library · Digital Archives'
      category = 'Digital Special Collections'
    }
    else if (lang === 'ja') {
      title = 'ヴワル魔法図書館 · 書香漂う禁断の知識'
      category = '館蔵典籍総覧'
    }
    else if (lang === 'zh-hant') {
      title = 'ヴワル魔法図書館 · 散發著書香的禁忌之識'
      category = '館藏典籍總覽'
    }
    else {
      title = 'ヴワル魔法図書館 · 散发着书香的禁忌之识'
      category = '馆藏典籍总览'
    }
  }
  else if (normalized.includes('rocket-pioneers')) {
    callNo = 'VML-TL781.P56-1965'
    if (lang === 'en') {
      category = 'Pioneers of Rocket Technology (NASA TT F-9285)'
      author = 'N. I. Kibal\'chich, K. E. Tsiolkovskiy, F. A. Tsander, Yu. V. Kondratyuk'
    }
    else if (lang === 'ja') {
      category = 'ロシア・ソ連 ロケット技術の先駆者：選集 (1881–1933)'
      author = 'キバリチッチ、ツィオルコフスキー、ツァンダー、コンドラチュク 等'
    }
    else if (lang === 'zh-hant') {
      category = '俄羅斯火箭技術先驅：選集（1881–1933）'
      author = 'N. I. 基巴利契奇、K. E. 齊奧爾科夫斯基、F. A. 燦德爾、Yu. V. 孔德拉秋克 等'
    }
    else {
      category = '俄罗斯火箭技术先驱：选集（1881–1933）'
      author = 'N. I. 基巴利契奇、K. E. 齐奥尔科夫斯基、F. A. 灿德尔、Yu. V. 孔德拉秋克 等'
    }
  }
  else if (normalized.includes('controlled-substances')) {
    callNo = 'VML-KF3890.S58-1992'
    if (lang === 'en') {
      category = 'Controlled Substances: Chemical & Legal Guide (2nd Ed)'
      author = 'Alexander T. Shulgin, Ph.D.'
    }
    else if (lang === 'ja') {
      category = '規制物質：連邦薬物法の化学と法律ガイド (第2版)'
      author = 'アレクサンダー・T・シュルギン 博士'
    }
    else if (lang === 'zh-hant') {
      category = '管制物質：聯邦藥物法的化學與法律指南 (第2版)'
      author = 'Alexander T. Shulgin, Ph.D.（亞歷山大·T·舒爾金 博士）'
    }
    else {
      category = '管制物质：联邦药物法的化学与法律指南 (第2版)'
      author = 'Alexander T. Shulgin, Ph.D.（亚历山大·T·舒尔金 博士）'
    }
  }
  else if (normalized.includes('catalogue')) {
    category = lang === 'en' ? 'Library Catalog & Archive' : lang === 'ja' ? '館蔵典籍目録' : '馆藏典籍索引'
  }
  else if (normalized.includes('about') || normalized.includes('acknowledgements')) {
    category = lang === 'en' ? 'About Voile Magic Library' : lang === 'ja' ? '図書館について' : '关于本馆'
  }

  return {
    filePath: relPath,
    urlPath,
    slug,
    title,
    category,
    callNo,
    author,
    lang,
  }
}

export async function buildAllOGImages(options: { force?: boolean } = {}) {
  const { force = false } = options
  fs.mkdirSync(publicOgDir, { recursive: true })
  fs.mkdirSync(docsPublicOgDir, { recursive: true })

  const files = getAllMarkdownFiles(docsDir)
  console.log(`[OG-Generator] Found ${files.length} markdown documents in docs/`)

  const mapping: Record<string, string> = {}
  let generatedCount = 0
  let skippedCount = 0

  const startTime = Date.now()

  for (const file of files) {
    const meta = resolvePageMeta(file)
    const outFilename = `${meta.slug}.png`
    mapping[meta.urlPath] = `/og/${outFilename}`

    const destPath = path.join(publicOgDir, outFilename)
    const docsDestPath = path.join(docsPublicOgDir, outFilename)

    if (!force && fs.existsSync(destPath) && fs.existsSync(docsDestPath)) {
      skippedCount++
      continue
    }

    try {
      const pngBuffer = await renderOGImage({
        title: meta.title,
        category: meta.category,
        callNo: meta.callNo,
        author: meta.author,
        lang: meta.lang,
      })
      fs.writeFileSync(destPath, pngBuffer)
      fs.writeFileSync(docsDestPath, pngBuffer)
      generatedCount++
    }
    catch (err) {
      console.error(`[OG-Generator] Error generating OG for ${meta.urlPath}:`, err)
    }
  }

  // Also write the mapping JSON for VitePress transformHead or SSR runtime
  const mapPath = path.resolve(__dirname, '../metadata/og-mapping.json')
  fs.writeFileSync(mapPath, `${JSON.stringify(mapping, null, 2)}\n`, 'utf-8')

  const elapsed = ((Date.now() - startTime) / 1000).toFixed(2)
  console.log(`[OG-Generator] Complete in ${elapsed}s! Generated: ${generatedCount}, Cached/Skipped: ${skippedCount}`)
}

// If executed directly
if (process.argv[1] && process.argv[1].endsWith('build_all_og.ts')) {
  buildAllOGImages({ force: true }).catch(console.error)
}
