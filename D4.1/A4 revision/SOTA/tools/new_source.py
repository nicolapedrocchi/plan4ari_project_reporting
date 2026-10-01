"""Scaffold wiki/sources/<key>.md pages from arXiv metadata, references.bib and source_notes.py.

Usage
  python tools/new_source.py <key> [<key> ...]     create pages for the given keys
  python tools/new_source.py --all                 create pages for every key in references.bib
  add --force to overwrite existing pages (normally NEVER do this: pages are hand-curated).

A scaffold is only a starting point: after creation, read raw/text/<key>.txt and complete
"Key contributions", "Evidence" and "Relevance for Plan4ARI" (see the wiki-ingest skill).
"""
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wikilib import PAPERS, TEXT, WIKI, detex, load_meta, parse_bib  # noqa: E402

try:
    from source_notes import NOTES
except ImportError:
    NOTES = {}


def venue(b):
    v = b.get('journal') or b.get('booktitle') or b.get('howpublished') or b.get('publisher') or ''
    extra = ', '.join(x for x in [('vol. ' + b['volume']) if 'volume' in b else '',
                                  ('no. ' + b['number']) if 'number' in b else '',
                                  ('pp. ' + b['pages']) if 'pages' in b else ''] if x)
    return detex(v + (', ' + extra if extra else ''))


def page(key, meta, bib):
    m = meta.get(key) or meta.get(key + '_arxiv') or {}
    b = bib.get(key, {})
    n = NOTES.get(key, {})
    title = detex(b.get('title', m.get('title', key)))
    authors = detex(b.get('author', ' and '.join(m.get('authors', [])))).replace(' and ', '; ')
    year = b.get('year', m.get('published', '')[:4])
    arxiv = m.get('arxiv', '')
    doi = b.get('doi', m.get('doi', ''))
    pdf = os.path.exists(os.path.join(PAPERS, key + '.pdf'))
    txt = os.path.exists(os.path.join(TEXT, key + '.txt'))
    tags = n.get('tags', [])
    links = n.get('concepts', [])
    L = ['---',
         'key: ' + key,
         'title: "' + title.replace('"', "'") + '"',
         'authors: "' + authors.replace('"', "'") + '"',
         'year: ' + str(year),
         'venue: "' + venue(b).replace('"', "'") + '"',
         'arxiv: ' + arxiv,
         'doi: ' + doi,
         'pdf: ' + ('raw/papers/%s.pdf' % key if pdf else 'none'),
         'text: ' + ('raw/text/%s.txt' % key if txt else 'none'),
         'tags: [' + ', '.join(tags) + ']',
         'status: ' + ('summarised' if n else 'stub'),
         '---', '',
         '# ' + title, '',
         '*' + authors + '* (' + str(year) + '). ' + venue(b) + '.', '',
         '## TL;DR', n.get('tldr', '_TODO: one-paragraph summary._'), '',
         '## Method', n.get('method', '_TODO_'), '',
         '## Evidence', n.get('evidence', '_TODO: platforms, rates, key numbers._'), '',
         '## Relevance for Plan4ARI', n.get('relevance', '_TODO_'), '']
    if m.get('abstract'):
        L += ['## Abstract (verbatim, arXiv)', '> ' + m['abstract'], '']
    L += ['## Links']
    L += ['- [[%s]]' % c for c in links] or ['- _TODO: link to concept/application pages_']
    L += ['- BibTeX key: `%s` in `latex/references.bib`' % key, '']
    return '\n'.join(L)


def main(argv):
    force = '--force' in argv
    argv = [a for a in argv if a != '--force']
    meta, bib = load_meta(), parse_bib()
    keys = sorted(bib) if argv == ['--all'] else argv
    os.makedirs(os.path.join(WIKI, 'sources'), exist_ok=True)
    for k in keys:
        p = os.path.join(WIKI, 'sources', k + '.md')
        if os.path.exists(p) and not force:
            print('exists, skipped:', k)
            continue
        open(p, 'w', encoding='utf8').write(page(k, meta, bib))
        print('written:', p)


if __name__ == '__main__':
    main(sys.argv[1:])
