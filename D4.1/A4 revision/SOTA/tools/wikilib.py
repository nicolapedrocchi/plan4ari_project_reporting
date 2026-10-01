"""Shared helpers for the SOTA LLM-wiki tools (stdlib only)."""
import json
import os
import re

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW = os.path.join(ROOT, 'raw')
PAPERS = os.path.join(RAW, 'papers')
TEXT = os.path.join(RAW, 'text')
PROJECT = os.path.join(RAW, 'project')  # internal project documents (.docx/.pdf), keys prj-*
META = os.path.join(RAW, 'meta', 'arxiv_metadata.json')
WIKI = os.path.join(ROOT, 'wiki')
LATEX = os.path.join(ROOT, 'latex')
BIB = os.path.join(LATEX, 'references.bib')


def load_meta():
    if not os.path.exists(META):
        return {}
    with open(META, encoding='utf8') as f:
        return json.load(f)


def save_meta(m):
    with open(META, 'w', encoding='utf8') as f:
        json.dump(m, f, indent=1, ensure_ascii=False)


def parse_bib(path=BIB):
    """Minimal BibTeX parser: returns {key: {'type':..., field: value}}."""
    if not os.path.exists(path):
        return {}
    s = open(path, encoding='utf8').read()
    out = {}
    for mt in re.finditer(r'@(\w+)\s*\{\s*([^,\s]+)\s*,', s):
        typ, key = mt.group(1).lower(), mt.group(2)
        i, depth = mt.end(), 1
        while i < len(s) and depth:
            depth += {'{': 1, '}': -1}.get(s[i], 0)
            i += 1
        body = s[mt.end():i - 1]
        fields = {'type': typ}
        for fm in re.finditer(r'(\w+)\s*=\s*\{((?:[^{}]|\{[^{}]*\}|\{[^{}]*\{[^{}]*\}[^{}]*\})*)\}', body):
            fields[fm.group(1).lower()] = ' '.join(fm.group(2).split())
        out[key] = fields
    return out


def detex(t):
    t = re.sub(r"\\['\"`^~]\{?(\w)\}?", r'\1', t)
    return t.replace('{', '').replace('}', '').replace('\\&', '&').replace('--', '-')


def wiki_pages():
    pages = {}
    for d, _, files in os.walk(WIKI):
        for f in files:
            if f.endswith('.md'):
                p = os.path.join(d, f)
                slug = os.path.relpath(p, WIKI).replace(os.sep, '/')[:-3]
                pages[slug] = p
    return pages


def frontmatter(path):
    s = open(path, encoding='utf8').read()
    if not s.startswith('---'):
        return {}, s
    end = s.find('\n---', 3)
    fm = {}
    for line in s[3:end].strip().splitlines():
        if ':' in line:
            k, v = line.split(':', 1)
            fm[k.strip()] = v.strip()
    return fm, s[end + 4:]


WIKILINK = re.compile(r'\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]')
