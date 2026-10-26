import { createMarkdownRenderer } from 'vitepress';
import fs from 'fs';

async function test() {
  const content = fs.readFileSync('docs/zh/fonts-encodings/appendices.md', 'utf-8');
  
  // Let's test section by section: A, B, C, D, E, F, G
  const sections = content.split(/^## 附录/m);
  console.log(`Found ${sections.length} sections`);

  // Let's test importing the mathjax markdown-it plugin or running vitepress render
}
test();
