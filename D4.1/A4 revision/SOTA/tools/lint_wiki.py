"""Health check of the SOTA LLM wiki. Prints problems; exit code 1 if any ERROR.

Checks
  ERROR  bib key without wiki/sources/<key>.md          (every reference must have a page)
  ERROR  source page whose key is not in references.bib
  ERROR  \\cite{key} in latex/*.tex not in references.bib
  ERROR  broken [[wikilink]]
  WARN   source page with status: stub (still to be summarised)
  WARN   source page pointing to a missing pdf/text file
  WARN   page not reachable from wiki/index.md (orphan)
  WARN   PDF in raw/papers without a source page
  ERROR  project page (wiki/project/prj-*.md) with missing file/text, bad key, or key in the bib
  ERROR  \\cite of a prj-* key (internal documents are never cited in the deliverable)
  WARN   file in raw/project without a page; project page with status: stub
Usage: python tools/lint_wiki.py
"""
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wikilib import LATEX, PAPERS, PROJECT, ROOT, WIKI, WIKILINK, frontmatter, parse_bib, wiki_pages  # noqa: E402


def main():
    errors, warns = [], []
    bib = parse_bib()
    pages = wiki_pages()
    sources = {s.split('/', 1)[1]: p for s, p in pages.items() if s.startswith('sources/')}

    for k in bib:
        if k not in sources:
            errors.append('bib key without source page: ' + k)
    for k, p in sources.items():
        fm, _ = frontmatter(p)
        if k not in bib:
            errors.append('source page not in bib: ' + k)
        if fm.get('status') == 'stub':
            warns.append('stub page: sources/' + k)
        for fld in ('pdf', 'text'):
            v = fm.get(fld, 'none')
            if v != 'none' and not os.path.exists(os.path.join(ROOT, v)):
                warns.append('%s missing for %s: %s' % (fld, k, v))

    projects = {s.split('/', 1)[1]: p for s, p in pages.items() if s.startswith('project/')}
    for k, p in projects.items():
        fm, _ = frontmatter(p)
        if not re.fullmatch(r'prj-[a-z0-9\-]+', k):
            errors.append('project key must be prj-<kebab>: ' + k)
        if k in bib:
            errors.append('project document must not be in references.bib: ' + k)
        for fld in ('file', 'text'):
            v = fm.get(fld, 'none')
            if v == 'none' or not os.path.exists(os.path.join(ROOT, v)):
                errors.append('%s missing for project/%s: %s' % (fld, k, v))
        if fm.get('status') == 'stub':
            warns.append('stub page: project/' + k)
    for f in glob.glob(os.path.join(PROJECT, '*')):
        k = os.path.splitext(os.path.basename(f))[0]
        if k not in projects:
            warns.append('project file without page: ' + os.path.basename(f))

    for tex in glob.glob(os.path.join(LATEX, '*.tex')):
        for c in re.findall(r'\\cite[tp]?\*?(?:\[[^\]]*\])?\{([^}]*)\}', open(tex, encoding='utf8').read()):
            for k in c.split(','):
                if k.strip().startswith('prj-'):
                    errors.append('%s cites internal project document %s' % (os.path.basename(tex), k.strip()))
                elif k.strip() not in bib:
                    errors.append('%s cites unknown key %s' % (os.path.basename(tex), k.strip()))

    linked = set()
    for slug, p in pages.items():
        _, body = frontmatter(p)
        for t in WIKILINK.findall(body):
            t = t.strip()
            if t not in pages:
                errors.append('broken link [[%s]] in %s' % (t, slug))
            linked.add(t)
    # reachability from index
    seen, todo = {'index'}, ['index']
    while todo:
        s = todo.pop()
        if s not in pages:
            continue
        for t in WIKILINK.findall(frontmatter(pages[s])[1]):
            t = t.strip()
            if t in pages and t not in seen:
                seen.add(t)
                todo.append(t)
    for s in pages:
        if s not in seen and s not in ('log',):
            warns.append('orphan (not reachable from index): ' + s)
    for pdf in glob.glob(os.path.join(PAPERS, '*.pdf')):
        k = os.path.basename(pdf)[:-4]
        if k not in sources:
            warns.append('pdf without source page: ' + k)

    for e in errors:
        print('ERROR', e)
    for w in warns:
        print('WARN ', w)
    print('\n%d pages, %d sources, %d bib entries -> %d errors, %d warnings' % (
        len(pages), len(sources), len(bib), len(errors), len(warns)))
    return 1 if errors else 0


if __name__ == '__main__':
    sys.exit(main())
