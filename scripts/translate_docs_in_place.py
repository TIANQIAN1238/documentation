#!/usr/bin/env python3
import argparse
import json
import re
import time
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

from deep_translator import GoogleTranslator

DOCS_DIR = Path('docs')
PROGRESS_FILE = Path('scripts/.translate-in-place-progress.json')

PROTECTED_TERMS = [
    'Temporal Cloud', 'Temporal Server', 'Temporal CLI',
    'Workflow Execution', 'Workflow Definition', 'Activity Definition',
    'Retry Policy', 'Search Attribute', 'Codec Server', 'Data Converter',
    'Child Workflow', 'Continue-As-New', 'Event History', 'Side Effect',
    'Task Queue', 'Workflow', 'Activity', 'Worker', 'Namespace', 'Signal',
    'Query', 'Update', 'Schedule', 'Timer', 'Visibility', 'Nexus',
    'Go SDK', 'Java SDK', 'Python SDK', 'TypeScript SDK', 'PHP SDK',
    '.NET SDK', 'Ruby SDK', 'Temporal', 'gRPC', 'Protobuf', 'mTLS', 'tctl', 'tcld',
]
PROTECTED_TERMS.sort(key=len, reverse=True)

translator = GoogleTranslator(source='en', target='zh-CN')


def load_progress():
    try:
        return json.loads(PROGRESS_FILE.read_text('utf-8'))
    except Exception:
        return {'translated': [], 'failed': []}


def save_progress(progress):
    PROGRESS_FILE.write_text(json.dumps(progress, ensure_ascii=False, indent=2), 'utf-8')


def safe_translate(text: str) -> str:
    if not text or not text.strip():
        return text
    for attempt in range(3):
        try:
            result = translator.translate(text)
            return result if isinstance(result, str) else text
        except Exception:
            if attempt == 2:
                return text
            time.sleep(attempt + 1)
    return text


def protect_terms(text: str):
    mapping = {}
    for i, term in enumerate(PROTECTED_TERMS):
        pat = re.compile(re.escape(term), re.IGNORECASE)
        key = f'@@TERM{i}@@'
        if pat.search(text):
            text = pat.sub(key, text)
            mapping[key] = term
    return text, mapping


def restore_mapping(text: str, mapping: dict):
    for k, v in mapping.items():
        text = text.replace(k, v)
    return text


def split_frontmatter_value(raw: str):
    raw = raw.rstrip()
    if not raw:
        return '', '', ''
    if (raw[0] == raw[-1]) and raw[0] in ('"', "'"):
        return raw[0], raw[1:-1], raw[-1]
    return '', raw, ''


def translate_frontmatter_line(line: str) -> str:
    m = re.match(r'^(\s*)(title|description|sidebar_label)(\s*:\s*)(.*)$', line)
    if not m:
        return line
    indent, key, sep, value = m.groups()
    q1, core, q2 = split_frontmatter_value(value)
    if not core.strip():
        return line
    translated = translate_inline(core)
    return f'{indent}{key}{sep}{q1}{translated}{q2}'


def replace_with_placeholders(text: str):
    mapping = {}
    idx = 0

    def put(val: str):
        nonlocal idx
        key = f'@@PH{idx}@@'
        idx += 1
        mapping[key] = val
        return key

    def repl_image(m):
        alt = translate_inline(m.group(1)) if m.group(1) else ''
        return put(f'![{alt}]({m.group(2)})')

    text = re.sub(r'!\[([^\]]*)\]\(([^)]+)\)', repl_image, text)

    def repl_link(m):
        label = translate_inline(m.group(1)) if m.group(1) else ''
        return put(f'[{label}]({m.group(2)})')

    text = re.sub(r'\[([^\]]+)\]\(([^)]+)\)', repl_link, text)

    text = re.sub(r'`[^`]+`', lambda m: put(m.group(0)), text)
    text = re.sub(r'https?://[^\s)>]+', lambda m: put(m.group(0)), text)
    text = re.sub(r'<[^>]+>', lambda m: put(m.group(0)), text)
    text = re.sub(r'(?<!\w)/(?:[A-Za-z0-9_.-]+/?)+(?:#[A-Za-z0-9_-]+)?', lambda m: put(m.group(0)), text)
    return text, mapping


def translate_inline(text: str) -> str:
    if not text.strip():
        return text
    text, term_map = protect_terms(text)
    text, ph_map = replace_with_placeholders(text)
    translated = safe_translate(text)
    if not isinstance(translated, str):
        translated = text
    translated = restore_mapping(translated, ph_map)
    translated = restore_mapping(translated, term_map)
    translated = translated.replace('：', ': ') if re.fullmatch(r'[A-Za-z0-9 _.-]+：\s*.*', translated) else translated
    return translated


def translate_table_line(line: str) -> str:
    if re.match(r'^\s*\|?[\s:-]+\|[\s|:-]*$', line):
        return line
    left = '|' if line.startswith('|') else ''
    right = '|' if line.endswith('|') else ''
    body = line[1:-1] if left and right else line.strip('|')
    cells = body.split('|')
    out = []
    for cell in cells:
        stripped = cell.strip()
        if not stripped:
            out.append(cell)
            continue
        pad_left = len(cell) - len(cell.lstrip(' '))
        pad_right = len(cell) - len(cell.rstrip(' '))
        translated = translate_inline(stripped)
        out.append(' ' * pad_left + translated + ' ' * pad_right)
    return left + '|'.join(out) + right


def translate_markdown_line(line: str) -> str:
    if not line.strip():
        return line
    if re.match(r'^\s*:::', line):
        return line
    if re.match(r'^\s*(import|export)\s', line):
        return line
    if re.match(r'^\s*<[/A-Za-z]', line):
        return line
    if re.match(r'^\s*\{[/A-Za-z<]', line):
        return line
    if re.match(r'^\s*[-*_]{3,}\s*$', line):
        return line
    if '|' in line and line.count('|') >= 2:
        return translate_table_line(line)

    m = re.match(r'^(\s*(?:>\s*)*)(#{1,6}\s+|[-*+]\s+|\d+\.\s+)?(.*)$', line)
    if not m:
        return translate_inline(line)
    prefix1, prefix2, rest = m.groups()
    prefix = (prefix1 or '') + (prefix2 or '')
    return prefix + translate_inline(rest)


def translate_content(content: str) -> str:
    lines = content.split('\n')
    out = []
    i = 0
    in_code = False
    if lines and lines[0] == '---':
        out.append(lines[0])
        i = 1
        while i < len(lines):
            out.append(lines[i] if lines[i] == '---' else translate_frontmatter_line(lines[i]))
            if lines[i] == '---':
                i += 1
                break
            i += 1

    while i < len(lines):
        line = lines[i]
        if line.strip().startswith('```'):
            out.append(line)
            in_code = not in_code
            i += 1
            continue
        if in_code:
            out.append(line)
        else:
            out.append(translate_markdown_line(line))
        i += 1
    return '\n'.join(out)


def translate_file(rel_path: str):
    path = DOCS_DIR / rel_path
    original = path.read_text('utf-8')
    translated = translate_content(original)
    path.write_text(translated, 'utf-8')
    return rel_path, True, ''


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--dir')
    parser.add_argument('--file')
    parser.add_argument('--workers', type=int, default=8)
    parser.add_argument('--reset', action='store_true')
    parser.add_argument('--dry-run', action='store_true')
    args = parser.parse_args()

    if args.reset:
        PROGRESS_FILE.unlink(missing_ok=True)

    if args.file:
        files = [args.file]
    else:
        search_dir = DOCS_DIR / args.dir if args.dir else DOCS_DIR
        files = sorted(str(p.relative_to(DOCS_DIR)) for p in search_dir.rglob('*') if p.suffix in ('.md', '.mdx'))

    progress = load_progress()
    pending = [f for f in files if f not in progress['translated']]
    print(f'total={len(files)} translated={len(progress["translated"])} pending={len(pending)} workers={args.workers}')
    if args.dry_run:
        print('\n'.join(pending))
        return
    if not pending:
        print('no pending files')
        return

    ok = fail = 0
    with ThreadPoolExecutor(max_workers=args.workers) as pool:
        futures = {pool.submit(translate_file, f): f for f in pending}
        for future in as_completed(futures):
            rel_path = futures[future]
            try:
                _, success, err = future.result()
                if success:
                    progress['translated'].append(rel_path)
                    ok += 1
                    print(f'✓ {rel_path} [{ok+fail}/{len(pending)}]')
                else:
                    progress['failed'].append(rel_path)
                    fail += 1
                    print(f'✗ {rel_path}: {err}')
            except Exception as e:
                progress['failed'].append(rel_path)
                fail += 1
                print(f'✗ {rel_path}: {e}')
            if (ok + fail) % 10 == 0:
                save_progress(progress)
    save_progress(progress)
    print(f'done ok={ok} fail={fail}')


if __name__ == '__main__':
    main()
