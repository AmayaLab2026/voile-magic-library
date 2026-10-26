import fs from 'fs';
import path from 'path';
import { TeX } from 'mathjax-full/js/input/tex.js';
import { AllPackages } from 'mathjax-full/js/input/tex/AllPackages.js';
import { mathjax } from 'mathjax-full/js/mathjax.js';
import { liteAdaptor } from 'mathjax-full/js/adaptors/liteAdaptor.js';
import { RegisterHTMLHandler } from 'mathjax-full/js/handlers/html.js';

const adaptor = liteAdaptor();
RegisterHTMLHandler(adaptor);

const content = fs.readFileSync('docs/zh/fonts-encodings/appendices.md', 'utf-8');

// Find all $$ ... $$ blocks
const regex = /\$\$([\s\S]*?)\$\$/g;
let match;
let count = 0;

const tex = new TeX({ packages: AllPackages });

while ((match = regex.exec(content)) !== null) {
  count++;
  const math = match[1].trim();
  try {
    const doc = mathjax.document('', { InputJax: tex });
    doc.convert(math, { display: true });
    // console.log(`Block ${count}: OK`);
  } catch (err) {
    console.error(`ERROR in block ${count}:`, err.message);
    console.error(`Math snippet:\n${math}\n------------------`);
  }
}

// Also check inline math $...$
const inlineRegex = /(?<!\$)\$(?!\$)(.*?)(?<!\$)\$(?!\$)/g;
let inlineCount = 0;
while ((match = inlineRegex.exec(content)) !== null) {
  inlineCount++;
  const math = match[1].trim();
  try {
    const doc = mathjax.document('', { InputJax: tex });
    doc.convert(math, { display: false });
  } catch (err) {
    console.error(`ERROR in inline math ${inlineCount}:`, err.message);
    console.error(`Math snippet:\n${math}\n------------------`);
  }
}

console.log(`Tested ${count} display blocks and ${inlineCount} inline math snippets.`);
