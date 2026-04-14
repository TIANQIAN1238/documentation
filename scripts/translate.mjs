#!/usr/bin/env node

/**
 * Temporal 文档批量翻译脚本 - Claude API 版
 *
 * 用法:
 *   node scripts/translate.mjs                    # 翻译所有未翻译的文件
 *   node scripts/translate.mjs --dry-run          # 预览
 *   node scripts/translate.mjs --file <path>      # 翻译单个文件
 *   node scripts/translate.mjs --dir develop      # 翻译指定目录
 *   node scripts/translate.mjs --concurrency 10   # 并发数 (默认 10)
 */

import { readFileSync, writeFileSync, mkdirSync, readdirSync, statSync } from 'fs';
import { join, dirname, relative, extname } from 'path';
import https from 'https';
import http from 'http';

const DOCS_DIR = join(process.cwd(), 'docs');
const I18N_DIR = join(process.cwd(), 'i18n/zh-Hans/docusaurus-plugin-content-docs/current');
const PROGRESS_FILE = join(process.cwd(), 'scripts/.translate-progress.json');

// Claude API 配置 - 从环境变量或硬编码
const API_KEY = process.env.ANTHROPIC_AUTH_TOKEN || 'sk-P8JJxg27JFXUC6by499cA4298eA74766AdEb31Bc45E6D5F9';
const BASE_URL = process.env.ANTHROPIC_BASE_URL || 'https://api.openai-next.com';

// CLI args
const args = process.argv.slice(2);
const DRY_RUN = args.includes('--dry-run');
const SINGLE_FILE = args.includes('--file') ? args[args.indexOf('--file') + 1] : null;
const TARGET_DIR = args.includes('--dir') ? args[args.indexOf('--dir') + 1] : null;
const CONCURRENCY = args.includes('--concurrency')
  ? parseInt(args[args.indexOf('--concurrency') + 1], 10)
  : 10;

function findFiles(dir) {
  const results = [];
  const exts = ['.md', '.mdx'];
  function walk(d) {
    for (const entry of readdirSync(d)) {
      const full = join(d, entry);
      const stat = statSync(full);
      if (stat.isDirectory()) walk(full);
      else if (exts.includes(extname(full))) results.push(full);
    }
  }
  walk(dir);
  return results;
}

function loadProgress() {
  try { return JSON.parse(readFileSync(PROGRESS_FILE, 'utf-8')); }
  catch { return { translated: [], failed: [] }; }
}

function saveProgress(progress) {
  mkdirSync(dirname(PROGRESS_FILE), { recursive: true });
  writeFileSync(PROGRESS_FILE, JSON.stringify(progress, null, 2));
}

// --- Claude API 调用 ---
async function callClaude(content) {
  const url = new URL('/v1/chat/completions', BASE_URL);

  const body = JSON.stringify({
    model: 'claude-sonnet-4-20250514',
    max_tokens: 16000,
    messages: [
      {
        role: 'system',
        content: `你是一个技术文档翻译器。将英文 Markdown/MDX 文档翻译成中文。

规则：
1. 只输出翻译后的完整文档内容，不要加任何解释
2. 保留所有 frontmatter (--- 之间的内容)，只翻译 title、description、sidebar_label 的值
3. 保留所有 import/export 语句不变
4. 保留所有代码块 (\`\`\`) 内容不变
5. 保留所有 JSX 组件标签不变 (如 <SdkLogos />)
6. 保留所有链接 URL 不变，翻译链接文字
7. 保留所有 HTML 标签属性不变
8. 以下专有名词不翻译，保持英文原文：Temporal, Workflow, Activity, Worker, Namespace, Task Queue, Signal, Query, Update, Schedule, Retry Policy, Search Attribute, Visibility, Codec Server, Data Converter, Child Workflow, Continue-As-New, Timer, Event History, Workflow Task, Side Effect, Nexus, tctl, tcld, gRPC, Protobuf, mTLS, SDK
9. 保留 Markdown 格式 (标题、列表、粗体、斜体等)
10. 保留 admonition 语法 (:::note, :::tip 等) 不变`
      },
      {
        role: 'user',
        content: `翻译以下文档为中文：\n\n${content}`
      }
    ]
  });

  return new Promise((resolve, reject) => {
    const protocol = url.protocol === 'https:' ? https : http;
    const req = protocol.request(url, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Authorization': `Bearer ${API_KEY}`,
      },
      timeout: 120000,
    }, (res) => {
      let data = '';
      res.on('data', chunk => data += chunk);
      res.on('end', () => {
        try {
          const json = JSON.parse(data);
          if (json.choices && json.choices[0]) {
            resolve(json.choices[0].message.content);
          } else if (json.error) {
            reject(new Error(json.error.message || JSON.stringify(json.error)));
          } else {
            reject(new Error('Unexpected response: ' + data.slice(0, 200)));
          }
        } catch (e) {
          reject(new Error('Parse error: ' + data.slice(0, 200)));
        }
      });
    });

    req.on('error', reject);
    req.on('timeout', () => { req.destroy(); reject(new Error('Request timeout')); });
    req.write(body);
    req.end();
  });
}

function sleep(ms) { return new Promise(r => setTimeout(r, ms)); }

const MAX_CHUNK_SIZE = 4000; // 每段最大字符数

/**
 * 将文件内容按段落边界拆分成多个 chunk
 */
function splitIntoChunks(content) {
  if (content.length <= MAX_CHUNK_SIZE) return [content];

  const chunks = [];
  const lines = content.split('\n');
  let current = '';
  let inFrontmatter = false;
  let frontmatterDone = false;

  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];

    // 处理 frontmatter - 作为一个完整的 chunk
    if (i === 0 && line === '---') {
      inFrontmatter = true;
      current = line + '\n';
      continue;
    }
    if (inFrontmatter) {
      current += line + '\n';
      if (line === '---') {
        inFrontmatter = false;
        frontmatterDone = true;
        chunks.push(current.trimEnd());
        current = '';
      }
      continue;
    }

    // 正常内容：在段落边界处切分
    const candidate = current + line + '\n';
    if (candidate.length > MAX_CHUNK_SIZE && current.length > 0) {
      chunks.push(current.trimEnd());
      current = line + '\n';
    } else {
      current = candidate;
    }
  }

  if (current.trim()) chunks.push(current.trimEnd());
  return chunks;
}

// --- 翻译单个文件 (带重试和分段) ---
async function translateFile(relPath, retries = 3) {
  const srcPath = join(DOCS_DIR, relPath);
  const destPath = join(I18N_DIR, relPath);

  const content = readFileSync(srcPath, 'utf-8');

  // 跳过太短的文件
  if (content.trim().length < 20) {
    mkdirSync(dirname(destPath), { recursive: true });
    writeFileSync(destPath, content, 'utf-8');
    return true;
  }

  const chunks = splitIntoChunks(content);
  const translatedChunks = [];

  for (let ci = 0; ci < chunks.length; ci++) {
    const chunk = chunks[ci];
    let success = false;

    for (let attempt = 0; attempt < retries; attempt++) {
      try {
        const translated = await callClaude(chunk);

        // 清理可能的 markdown 代码块包裹
        let cleaned = translated;
        if (cleaned.startsWith('```mdx\n') || cleaned.startsWith('```markdown\n') || cleaned.startsWith('```md\n')) {
          cleaned = cleaned.replace(/^```(?:mdx|markdown|md)\n/, '').replace(/\n```$/, '');
        }
        if (cleaned.startsWith('```\n')) {
          cleaned = cleaned.replace(/^```\n/, '').replace(/\n```$/, '');
        }
        translatedChunks.push(cleaned);
        success = true;
        break;
      } catch (err) {
        if (attempt < retries - 1) {
          const delay = (attempt + 1) * 5000;
          console.log(`  ⟳ ${relPath} [chunk ${ci+1}/${chunks.length}] 重试 ${attempt + 1}/${retries}...`);
          await sleep(delay);
        } else {
          console.error(`  ✗ ${relPath} [chunk ${ci+1}]: ${err.message}`);
          return false;
        }
      }
    }

    if (!success) return false;
  }

  mkdirSync(dirname(destPath), { recursive: true });
  writeFileSync(destPath, translatedChunks.join('\n\n'), 'utf-8');
  const chunkInfo = chunks.length > 1 ? ` (${chunks.length} 段)` : '';
  console.log(`  ✓ ${relPath}${chunkInfo}`);
  return true;
}

// --- 主流程 ---
async function main() {
  let files;
  if (SINGLE_FILE) {
    files = [SINGLE_FILE];
  } else {
    const searchDir = TARGET_DIR ? join(DOCS_DIR, TARGET_DIR) : DOCS_DIR;
    files = findFiles(searchDir).map(p => relative(DOCS_DIR, p));
  }

  const progress = loadProgress();
  const pending = files.filter(f => !progress.translated.includes(f));

  console.log(`\n========== Temporal 文档翻译 (Claude API) ==========`);
  console.log(`总文件: ${files.length} | 已完成: ${progress.translated.length} | 待翻译: ${pending.length} | 并发: ${CONCURRENCY}`);
  console.log(`====================================================\n`);

  if (DRY_RUN) {
    pending.forEach((f, i) => console.log(`  ${i + 1}. ${f}`));
    return;
  }

  if (!pending.length) { console.log('全部翻译完成！'); return; }

  let ok = 0, fail = 0;

  // 并发控制
  for (let i = 0; i < pending.length; i += CONCURRENCY) {
    const batch = pending.slice(i, i + CONCURRENCY);
    const results = await Promise.allSettled(batch.map(f => translateFile(f)));

    for (let j = 0; j < results.length; j++) {
      if (results[j].status === 'fulfilled' && results[j].value) {
        progress.translated.push(batch[j]);
        ok++;
      } else {
        progress.failed.push(batch[j]);
        fail++;
      }
    }
    saveProgress(progress);
    console.log(`  --- 进度: ${ok + fail}/${pending.length} (成功 ${ok}, 失败 ${fail}) ---`);
  }

  console.log(`\n========== 完成! 成功: ${ok}, 失败: ${fail}, 总进度: ${progress.translated.length}/${files.length} ==========`);
}

main().catch(err => { console.error('致命错误:', err); process.exit(1); });
