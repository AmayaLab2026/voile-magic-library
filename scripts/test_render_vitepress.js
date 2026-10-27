import fs from 'node:fs'
import process from 'node:process'
import { createMarkdownRenderer } from 'vitepress'

async function main() {
  const md = await createMarkdownRenderer(process.cwd(), {
    math: true,
  })

  const content = fs.readFileSync('docs/zh/fonts-encodings/appendices.md', 'utf-8')

  // Let's test line by line or section by section
  const lines = content.split('\n')
  console.log(`Total lines: ${lines.length}`)

  // Test blocks of 100 lines to isolate the exact line
  const chunkSize = 200
  for (let i = 0; i < lines.length; i += chunkSize) {
    const chunk = lines.slice(i, i + chunkSize).join('\n')
    try {
      await md.renderAsync(chunk, {})
    }
    catch (err) {
      console.error(`Error in lines ${i + 1} to ${Math.min(i + chunkSize, lines.length)}:`, err.message)
      // Now narrow down line by line
      for (let j = i; j < Math.min(i + chunkSize, lines.length); j++) {
        try {
          await md.renderAsync(lines[j], {})
        }
        catch (lineErr) {
          console.error(`Exact failing line ${j + 1}:`, lines[j])
          console.error(lineErr)
        }
      }
      return
    }
  }
  console.log('All chunks rendered successfully!')
}

main().catch(console.error)
