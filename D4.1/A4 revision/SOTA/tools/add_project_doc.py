"""Add a project document (.docx or .pdf) to the raw layer and scaffold its wiki page.

Project documents are internal Plan4ARI material (proposal, deliverable outlines, minutes,
specifications...). They are NOT bibliographic sources: no BibTeX entry, never cited in
latex/main.tex, referenced in the wiki as [[project/<key>]].

Usage
  python tools/add_project_doc.py <path/to/file.docx|pdf> <key> [--doctype outline] [--title "..."]
         [--date YYYY-MM-DD] [--version 0.1] [--confidentiality consortium]
  python tools/add_project_doc.py --reextract <key>      re-extract text of an existing file

Key convention: prj-<short-kebab-name>, e.g. prj-d41-outline, prj-plan4ari-proposal.
The original file is copied (never moved) to raw/project/<key>.<ext>; text goes to raw/text/<key>.txt.
"""
import argparse
import os
import re
import shutil
import subprocess
import sys
import zipfile
import xml.etree.ElementTree as ET
from datetime import date

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wikilib import PROJECT, TEXT, WIKI  # noqa: E402

W = '{http://schemas.openxmlformats.org/wordprocessingml/2006/main}'
DOCTYPES = ['proposal', 'grant-agreement', 'outline', 'deliverable', 'report', 'minutes', 'specification',
            'presentation', 'other']


def _ptext(p):
    return ''.join(t.text or '' for t in p.iter(W + 't')).strip()


def docx_text(path):
    """Paragraphs in order; headings prefixed with '#'; tables as ' | '-separated rows."""
    root = ET.fromstring(zipfile.ZipFile(path).read('word/document.xml'))
    body = root.find(W + 'body')
    out = []
    for el in body:
        if el.tag == W + 'p':
            t = _ptext(el)
            if not t:
                continue
            style = el.find(f'{W}pPr/{W}pStyle')
            sv = style.get(W + 'val', '') if style is not None else ''
            m = re.match(r'(?i)heading\s*(\d)|titolo\s*(\d)|title', sv)
            if m:
                lvl = int(m.group(1) or m.group(2) or 1)
                t = '#' * lvl + ' ' + t
            out.append(t)
        elif el.tag == W + 'tbl':
            for tr in el.iter(W + 'tr'):
                cells = [' '.join(_ptext(p) for p in tc.iter(W + 'p')).strip() for tc in tr.iter(W + 'tc')]
                if any(cells):
                    out.append('| ' + ' | '.join(cells) + ' |')
            out.append('')
    return '\n'.join(out)


def docx_props(path):
    props = {}
    try:
        x = ET.fromstring(zipfile.ZipFile(path).read('docProps/core.xml'))
        for el in x:
            tag = el.tag.split('}')[-1]
            if el.text and tag in ('title', 'creator', 'modified', 'created'):
                props[tag] = el.text.strip()
    except KeyError:
        pass
    return props


def extract(src, key):
    os.makedirs(TEXT, exist_ok=True)
    txt = os.path.join(TEXT, key + '.txt')
    if src.lower().endswith('.docx'):
        open(txt, 'w', encoding='utf8').write(docx_text(src))
    elif src.lower().endswith('.pdf'):
        subprocess.run(['pdftotext', '-layout', '-enc', 'UTF-8', src, txt], check=True)
    else:
        sys.exit('unsupported format (use .docx or .pdf): ' + src)
    return txt


def page(key, a, rel_file, props, txt):
    title = a.title or props.get('title') or os.path.splitext(os.path.basename(a.file))[0].replace('_', ' ')
    d = a.date or (props.get('modified') or props.get('created') or '')[:10]
    words = len(open(txt, encoding='utf8').read().split())
    heads = [l for l in open(txt, encoding='utf8').read().splitlines() if l.startswith('#')][:25]
    L = ['---',
         'key: ' + key,
         'title: "' + title.replace('"', "'") + '"',
         'doctype: ' + a.doctype,
         'version: "' + (a.version or '') + '"',
         'date: ' + d,
         'author: "' + (props.get('creator', '') or '').replace('"', "'") + '"',
         'confidentiality: ' + a.confidentiality,
         'file: ' + rel_file,
         'text: raw/text/%s.txt' % key,
         'original_name: "' + os.path.basename(a.file).replace('"', "'") + '"',
         'tags: [project]',
         'status: stub',
         '---', '',
         '# ' + title, '',
         '*Project document (%s), %s. Internal — not citable in the deliverable bibliography.* ' % (a.doctype, d or 'undated'),
         'Extracted text: %d words.' % words, '',
         '## Purpose', '_TODO: what this document is for and who wrote it._', '',
         '## Key content', '_TODO: structured summary (objectives, requirements, decisions, numbers)._', '',
         '## Requirements / constraints for the motion-planning framework',
         '_TODO: list each requirement with the section of the document it comes from._', '',
         '## Relation to the literature', '_TODO: links to [[concepts/...]], [[comparisons/...]], [[sources/...]]._', '',
         '## Open points / decisions to take', '_TODO_', '']
    if heads:
        L += ['## Document outline (headings)', ''] + ['- ' + h.lstrip('#').strip() for h in heads] + ['']
    L += ['## Links', '- [[comparisons/plan4ari-gap-analysis]]', '']
    return '\n'.join(L)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('file', nargs='?')
    ap.add_argument('key', nargs='?')
    ap.add_argument('--doctype', choices=DOCTYPES, default='other')
    ap.add_argument('--title')
    ap.add_argument('--date')
    ap.add_argument('--version')
    ap.add_argument('--confidentiality', default='consortium', choices=['public', 'consortium', 'internal'])
    ap.add_argument('--reextract')
    a = ap.parse_args()
    if a.reextract:
        k = a.reextract
        src = [f for f in os.listdir(PROJECT) if os.path.splitext(f)[0] == k]
        if not src:
            sys.exit('no raw/project file for ' + k)
        print('re-extracted', extract(os.path.join(PROJECT, src[0]), k))
        return
    if not (a.file and a.key):
        ap.error('file and key are required')
    if not re.fullmatch(r'prj-[a-z0-9\-]+', a.key):
        sys.exit('key must match prj-<lowercase-kebab>, e.g. prj-d41-outline')
    ext = os.path.splitext(a.file)[1].lower()
    os.makedirs(PROJECT, exist_ok=True)
    dst = os.path.join(PROJECT, a.key + ext)
    if os.path.exists(dst):
        sys.exit('raw/project/%s%s already exists: raw files are immutable (choose a new key, e.g. -v2)' % (a.key, ext))
    shutil.copy2(a.file, dst)
    txt = extract(dst, a.key)
    props = docx_props(dst) if ext == '.docx' else {}
    os.makedirs(os.path.join(WIKI, 'project'), exist_ok=True)
    p = os.path.join(WIKI, 'project', a.key + '.md')
    if os.path.exists(p):
        print('page exists, not overwritten:', p)
    else:
        open(p, 'w', encoding='utf8').write(page(a.key, a, 'raw/project/' + a.key + ext, props, txt))
        print('page written:', p)
    print('raw file:', dst, '\ntext:', txt, '\ntoday:', date.today().isoformat())


if __name__ == '__main__':
    main()
