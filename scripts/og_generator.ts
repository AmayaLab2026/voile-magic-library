import { Buffer } from 'node:buffer'
import fs from 'node:fs'
import { createRequire } from 'node:module'
import path from 'node:path'
import { fileURLToPath } from 'node:url'
import { initWasm, Resvg } from '@resvg/resvg-wasm'

const require = createRequire(import.meta.url)
const __filename = fileURLToPath(import.meta.url)
const __dirname = path.dirname(__filename)

let wasmInitialized = false
let fontBuffer: Buffer | null = null

export async function ensureInit() {
  if (!wasmInitialized) {
    const wasmPath = require.resolve('@resvg/resvg-wasm/index_bg.wasm')
    const wasm = fs.readFileSync(wasmPath)
    await initWasm(wasm)
    wasmInitialized = true
  }
  if (!fontBuffer) {
    const fontPath = path.resolve(__dirname, '../public/source-han-sans.ttf')
    fontBuffer = fs.readFileSync(fontPath)
  }
}

export interface OGCardOptions {
  title: string
  category?: string
  subtitle?: string
  callNo?: string
  author?: string
  lang?: string
}

function escapeXml(unsafe: string): string {
  return unsafe
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&apos;')
}

/**
 * Intelligent line breaker supporting English word boundaries and CJK natural breaks.
 * Directly mirrors the English Nolebase typesetting standard.
 */
function splitLines(text: string, maxCharactersPerLine = 22): string[] {
  const raw = text.replace(/[\r\n]+/g, ' ').trim()
  if (!raw)
    return ['']

  // If text contains mostly Latin words (English)
  const isLatin = /^[a-z0-9\s.,'":;()\-·]+$/i.test(raw)
  if (isLatin) {
    const words = raw.split(/\s+/)
    const lines: string[] = []
    let current = ''

    for (const word of words) {
      if (!current) {
        current = word
      }
      else if (`${current} ${word}`.length <= maxCharactersPerLine) {
        current += ` ${word}`
      }
      else {
        lines.push(current)
        current = word
      }
    }
    if (current)
      lines.push(current)

    if (lines.length > 3) {
      lines[2] = `${lines[2]}...`
      return lines.slice(0, 3)
    }
    return lines
  }

  // CJK & Mixed text breaking
  const lines: string[] = []
  let current = ''
  for (let i = 0; i < raw.length; i++) {
    const char = raw[i]
    current += char
    const visualLen = Array.from(current).reduce((acc, c) => acc + (c.charCodeAt(0) > 255 ? 1 : 0.55), 0)
    if (visualLen >= maxCharactersPerLine && i < raw.length - 1) {
      lines.push(current.trim())
      current = ''
    }
  }
  if (current.trim())
    lines.push(current.trim())

  if (lines.length > 3) {
    lines[2] = `${lines[2]}...`
    return lines.slice(0, 3)
  }
  return lines
}

export function generateOGSvg(options: OGCardOptions): string {
  const {
    title,
    category = '特藏文献 · ヴワル魔法図書館',
    callNo,
    author,
    lang = 'zh',
  } = options

  const isEn = lang === 'en'
  const isJa = lang === 'ja'

  // Dynamic max characters & font size based on language and title length
  const maxChars = isEn ? 28 : 20
  const lines = splitLines(title, maxChars)

  // Typesetting parameters aligned with the English standard layout
  let titleFontSize = 62
  let lineHeight = 78
  let startY = 280

  if (lines.length >= 3 || (isEn && title.length > 50)) {
    titleFontSize = 52
    lineHeight = 68
    startY = 265
  }

  const titleSvgLines = lines.map((line, idx) => {
    const y = startY + idx * lineHeight
    return `<text x="60" y="${y}" font-family="Source Han Sans SC, sans-serif" font-size="${titleFontSize}" font-weight="bold" fill="#1f1e1d">${escapeXml(line)}</text>`
  }).join('\n')

  const callNoSvg = callNo
    ? `
      <g transform="translate(930, 68)">
        <rect x="0" y="0" width="210" height="36" rx="6" fill="#f5efe8" stroke="#d97757" stroke-width="1.2" />
        <text x="105" y="23" text-anchor="middle" font-family="Source Han Sans SC, monospace" font-size="13" font-weight="bold" fill="#a3482b" letter-spacing="0.5">
          ${escapeXml(callNo)}
        </text>
      </g>
    `
    : ''

  const authorY = startY + lines.length * lineHeight + (lines.length === 1 ? 25 : 15)
  const authorSvg = author
    ? `
      <text x="60" y="${authorY}" font-family="Source Han Sans SC, sans-serif" font-size="22" font-weight="500" fill="#635f59">
        ${isEn ? 'Author' : isJa ? '著者' : '著者'} · ${escapeXml(author)}
      </text>
    `
    : ''

  const siteTitle = 'ヴワル魔法図書館'
  const siteDesc = isEn
    ? 'Voile Magic Library'
    : isJa
      ? '書香漂う禁断の知識、すべてここに'
      : '散发着书香的禁忌之识，尽在本馆'

  return `
    <svg width="1200" height="630" viewBox="0 0 1200 630" xmlns="http://www.w3.org/2000/svg">
      <!-- Claude Signature Warm Paper Background (#fbfaf7) -->
      <rect width="1200" height="630" fill="#fbfaf7" />

      <!-- Clean Outer Claude Border (#e6e1d8) -->
      <rect x="2" y="2" width="1196" height="626" rx="12" fill="none" stroke="#e6e1d8" stroke-width="2" />

      <!-- Top Header Brand Area -->
      <text x="60" y="92" font-family="Source Han Sans SC, sans-serif" font-size="20" font-weight="bold" fill="#1f1e1d" letter-spacing="0.5">
        ${siteTitle}
      </text>

      <!-- Call No Badge (Top Right) -->
      ${callNoSvg}

      <!-- Category Label (Pure Typography Aligned with x=60) -->
      <text x="60" y="210" font-family="Source Han Sans SC, sans-serif" font-size="28" font-weight="600" fill="#c15f3e" letter-spacing="0.5">
        ${escapeXml(category)}
      </text>

      <!-- Main Title (Aliged with English Nolebase font-size:62-64, y:280) -->
      ${titleSvgLines}

      <!-- Author Attribution (if present) -->
      ${authorSvg}

      <!-- Bottom Line Separator Aligned to Claude Border -->
      <line x1="60" y1="520" x2="1140" y2="520" stroke="#e6e1d8" stroke-width="1.2" />

      <!-- Bottom Footer: Site & Domain Aligned with English Template (y=560) -->
      <text x="60" y="565" font-family="Source Han Sans SC, sans-serif" font-size="24" font-weight="500" fill="#78716c">
        ${escapeXml(siteDesc)}
      </text>
      <text x="1140" y="565" text-anchor="end" font-family="Source Han Sans SC, monospace" font-size="20" fill="#a39e97">
        amayalab2026.github.io/voile-magic-library
      </text>
    </svg>
  `
}

export async function renderOGImage(options: OGCardOptions): Promise<Buffer> {
  await ensureInit()
  const svg = generateOGSvg(options)
  const resvg = new Resvg(svg, {
    font: {
      fontBuffers: [fontBuffer!],
      loadSystemFonts: false,
      defaultFontFamily: 'Source Han Sans SC',
    },
    fitTo: {
      mode: 'width',
      value: 1200,
    },
  })
  return Buffer.from(resvg.render().asPng())
}
