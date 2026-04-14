#!/usr/bin/env python3
"""
Temporal 文档批量翻译 - 就地覆盖 docs/
用法:
  python3 scripts/translate_fast.py --reset
  python3 scripts/translate_fast.py --workers 12
  python3 scripts/translate_fast.py --dir develop
  python3 scripts/translate_fast.py --file index.mdx
"""

import json
import re
import time
import urllib.parse

import requests
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

DOCS_DIR = Path('docs')
PROGRESS_FILE = Path('scripts/.translate-progress.json')

PROTECTED = [
    'Temporal Cloud', 'Temporal Server', 'Temporal CLI',
    'Workflow Execution', 'Workflow Definition', 'Activity Definition',
    'Retry Policy', 'Search Attribute', 'Codec Server', 'Data Converter',
    'Child Workflow', 'Continue-As-New', 'Event History', 'Side Effect',
    'Task Queue', 'Visibility',
    'Go SDK', 'Java SDK', 'Python SDK', 'TypeScript SDK', 'PHP SDK', '.NET SDK', 'Ruby SDK',
    'Workflow', 'Activity', 'Worker', 'Namespace', 'Signal', 'Query', 'Update', 'Schedule', 'Timer',
    'Nexus', 'Temporal', 'gRPC', 'Protobuf', 'mTLS', 'tctl', 'tcld',
]
PROTECTED.sort(key=len, reverse=True)
CHUNK_LIMIT = 4200


def load_progress():
    try:
        return json.loads(PROGRESS_FILE.read_text('utf-8'))
    except Exception:
        return {'translated': [], 'failed': []}


def save_progress(progress):
    PROGRESS_FILE.write_text(json.dumps(progress, ensure_ascii=False, indent=2), 'utf-8')


def safe_translate(text: str) -> str:
    if not text.strip():
        return text
    url = 'https://translate.googleapis.com/translate_a/single'
    params = {
        'client': 'gtx',
        'sl': 'en',
        'tl': 'zh-CN',
        'dt': 't',
        'q': text,
    }
    headers = {'User-Agent': 'Mozilla/5.0'}
    for attempt in range(3):
        try:
            resp = requests.get(url, params=params, headers=headers, timeout=20)
            resp.raise_for_status()
            data = resp.json()
            parts = []
            for item in data[0]:
                if item and item[0]:
                    parts.append(item[0])
            result = ''.join(parts)
            return result if result else text
        except Exception:
            if attempt == 2:
                return text
            time.sleep(attempt + 1)
    return text


def protect_terms(text: str):
    mapping = {}
    for i, term in enumerate(PROTECTED):
        key = f'ZZTERM{i:03d}ZZ'
        pat = re.compile(re.escape(term), re.IGNORECASE)
        if pat.search(text):
            text = pat.sub(key, text)
            mapping[key] = term
    return text, mapping


def restore(text: str, mapping: dict) -> str:
    for k, v in mapping.items():
        text = text.replace(k, v)
    return text


def split_chunks(text: str):
    if len(text) <= CHUNK_LIMIT:
        return [text]
    chunks = []
    current = ''
    for line in text.split('\n'):
        add = (line + '\n')
        if current and len(current) + len(add) > CHUNK_LIMIT:
            chunks.append(current.rstrip('\n'))
            current = add
        else:
            current += add
    if current:
        chunks.append(current.rstrip('\n'))
    return chunks


def replace_special(text: str):
    mapping = {}
    idx = 0

    def put(val: str):
        nonlocal idx
        key = f'ZZPH{idx:03d}ZZ'
        idx += 1
        mapping[key] = val
        return key

    def repl_img(m):
        alt = translate_text(m.group(1)) if m.group(1) else ''
        return put(f'![{alt}]({m.group(2)})')

    def repl_link(m):
        label = translate_text(m.group(1)) if m.group(1) else ''
        return put(f'[{label}]({m.group(2)})')

    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', repl_img, text)
    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', repl_link, text)
    text = re.sub(r'`[^`]+`', lambda m: put(m.group(0)), text)
    text = re.sub(r'<[^>]+>', lambda m: put(m.group(0)), text)
    text = re.sub(r'https?://[^\s)>]+', lambda m: put(m.group(0)), text)
    text = re.sub(r'(?<!\w)/(?:[A-Za-z0-9_.-]+/?)+(?:#[A-Za-z0-9_-]+)?', lambda m: put(m.group(0)), text)
    return text, mapping


def translate_text(text: str) -> str:
    if not text.strip():
        return text
    text, term_map = protect_terms(text)
    text, ph_map = replace_special(text)
    translated_parts = [safe_translate(chunk) for chunk in split_chunks(text)]
    translated = '\n'.join(translated_parts)
    translated = restore(translated, ph_map)
    translated = restore(translated, term_map)
    return translated


def translate_frontmatter_line(line: str) -> str:
    m = re.match(r'^(\s*)(title|description|sidebar_label)(\s*:\s*)(.*)$', line)
    if not m:
        return line
    indent, key, sep, value = m.groups()
    value = value.rstrip()
    quote = ''
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
        quote, core = value[0], value[1:-1]
    else:
        core = value
    if not core.strip():
        return line
    return f'{indent}{key}{sep}{quote}{translate_text(core)}{quote}'


def translate_table_line(line: str) -> str:
    if re.match(r'^\s*\|?[\s:-]+\|[\s|:-]*$', line):
        return line
    leading = '|' if line.startswith('|') else ''
    trailing = '|' if line.endswith('|') else ''
    raw = line[1:-1] if leading and trailing else line.strip('|')
    cells = raw.split('|')
    out = []
    for cell in cells:
        stripped = cell.strip()
        if not stripped:
            out.append(cell)
            continue
        left = len(cell) - len(cell.lstrip(' '))
        right = len(cell) - len(cell.rstrip(' '))
        out.append(' ' * left + translate_text(stripped) + ' ' * right)
    return leading + '|'.join(out) + trailing


def translate_mdx(content: str) -> str:
    lines = content.split('\n')
    result = []
    i = 0
    in_code = False
    in_prop_code = False
    if lines and lines[0] == '---':
        result.append('---')
        i = 1
        while i < len(lines):
            if lines[i] == '---':
                result.append('---')
                i += 1
                break
            result.append(translate_frontmatter_line(lines[i]))
            i += 1

    buffer = []

    def flush_buffer():
        if not buffer:
            return
        joined = '\n'.join(buffer)
        result.append(translate_text(joined))
        buffer.clear()

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        if stripped.startswith('```'):
            flush_buffer()
            result.append(line)
            in_code = not in_code
            i += 1
            continue

        if in_code:
            result.append(line)
            i += 1
            continue

        if in_prop_code:
            result.append(line)
            if stripped == '}> ':
                pass
            if stripped == '}>' or stripped.endswith('}>'):
                in_prop_code = False
            i += 1
            continue

        if not stripped:
            flush_buffer()
            result.append('')
            i += 1
            continue

        if re.match(r'^\s*(import|export)\s', line) or stripped.startswith(':::'):
            flush_buffer()
            result.append(line)
            i += 1
            continue

        if 'code={' in line:
            flush_buffer()
            result.append(line)
            in_prop_code = True
            i += 1
            continue

        if re.match(r'^\s*</?>\s*$', line) or re.match(r'^\s*<[/A-Za-z]', line) or re.match(r'^\s*\{[/<A-Za-z]', line):
            flush_buffer()
            result.append(line)
            i += 1
            continue

        if '|' in line and line.count('|') >= 2:
            flush_buffer()
            result.append(translate_table_line(line))
            i += 1
            continue

        buffer.append(line)
        i += 1

    flush_buffer()
    return '\n'.join(result)


def translate_file(rel_path: str):
    path = DOCS_DIR / rel_path
    content = path.read_text('utf-8')
    translated = translate_mdx(content)
    path.write_text(translated, 'utf-8')
    return rel_path, True, ''


def main():
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--workers', type=int, default=10)
    parser.add_argument('--dir', type=str, default=None)
    parser.add_argument('--file', type=str, default=None)
    parser.add_argument('--dry-run', action='store_true')
    parser.add_argument('--reset', action='store_true')
    args = parser.parse_args()

    if args.reset:
        PROGRESS_FILE.unlink(missing_ok=True)
        print('progress reset')

    if args.file:
        files = [args.file]
    else:
        search_dir = DOCS_DIR / args.dir if args.dir else DOCS_DIR
        files = sorted(str(p.relative_to(DOCS_DIR)) for p in search_dir.rglob('*') if p.suffix in ('.md', '.mdx'))

    progress = load_progress()
    pending = [f for f in files if f not in progress['translated']]
    print(f'total={len(files)} done={len(progress["translated"])} pending={len(pending)} workers={args.workers}')
    if args.dry_run:
        print('\n'.join(pending))
        return
    if not pending:
        print('all translated')
        return

    ok = fail = 0
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(translate_file, f): f for f in pending}
        for future in as_completed(futures):
            rel = futures[future]
            try:
                _, success, err = future.result()
                if success:
                    progress['translated'].append(rel)
                    ok += 1
                    print(f'✓ {rel} [{ok+fail}/{len(pending)}]')
                else:
                    progress['failed'].append(rel)
                    fail += 1
                    print(f'✗ {rel}: {err}')
            except Exception as e:
                progress['failed'].append(rel)
                fail += 1
                print(f'✗ {rel}: {e}')
            if (ok + fail) % 10 == 0:
                save_progress(progress)
    save_progress(progress)
    print(f'done ok={ok} fail={fail}')


if __name__ == '__main__':
    main()
