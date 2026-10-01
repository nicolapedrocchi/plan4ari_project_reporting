"""Generate BibTeX entries from Crossref metadata.

Usage
  python tools/bib_from_doi.py <key>=<doi>[@<arxiv_id>] [...]  >> latex/references.bib

- Journal articles -> @article, proceedings -> @inproceedings, posted content (SSRN, TechRxiv) -> @misc.
- Non-ASCII characters are escaped for 8-bit BibTeX; check the output before appending.
"""
import json
import re
import sys
import unicodedata
import urllib.parse
import urllib.request

ACC = {'́': "\\'", '̀': '\\`', '̈': '\\"', '̂': '\\^', '̃': '\\~', '̧': '\\c', '̌': '\\v'}


def tex(s):
    out = []
    for ch in s:
        if ord(ch) < 128:
            out.append({'&': '\\&', '%': '\\%', '#': '\\#'}.get(ch, ch))
            continue
        d = unicodedata.normalize('NFD', ch)
        if len(d) == 2 and d[1] in ACC:
            out.append('{%s%s}' % (ACC[d[1]], d[0]) if ACC[d[1]] not in ('\\c', '\\v') else '{%s{%s}}' % (ACC[d[1]], d[0]))
        else:
            out.append({'–': '--', '—': '---', '’': "'", '‘': '`', '“': '``', '”': "''", 'ß': '{\\ss}', 'ø': '{\\o}', 'ł': '{\\l}'}.get(ch, ''))
    return ''.join(out)


def protect(t):
    words = []
    for w in t.split(' '):
        core = re.sub(r'[^A-Za-z0-9\-*]', '', w)
        if any(sum(c.isupper() for c in p) >= 2 for p in core.split('-')) or re.search(r'[A-Z].*\d|\d.*[A-Z]', core):
            w = '{' + w + '}' if not w.endswith(':') else '{' + w[:-1] + '}:'
        words.append(w)
    return ' '.join(words)


def entry(key, doi, arxiv=None):
    m = json.load(urllib.request.urlopen('https://api.crossref.org/works/' + urllib.parse.quote(doi), timeout=60))['message']
    typ = {'journal-article': 'article', 'proceedings-article': 'inproceedings', 'posted-content': 'misc'}.get(m.get('type'), 'misc')
    title = re.sub(r'<[^>]+>', '', m['title'][0]).replace('$', '').replace('^{*}', '*')
    authors = ' and '.join(tex('%s, %s' % (a.get('family', ''), a.get('given', ''))).strip(', ') for a in m.get('author', []))
    f = [('author', authors), ('title', protect(tex(' '.join(title.split()))))]
    venue = tex((m.get('container-title') or [''])[0])
    if typ == 'article':
        f.append(('journal', venue))
    elif typ == 'inproceedings':
        f.append(('booktitle', venue))
    else:
        f.append(('howpublished', 'Preprint, %s' % (m.get('institution', [{}])[0].get('name') if m.get('institution') else 'posted content')))
    f.append(('year', str(m['issued']['date-parts'][0][0])))
    for a, b in (('volume', 'volume'), ('number', 'issue'), ('pages', 'page')):
        if m.get(b):
            f.append((a, m[b].replace('-', '--') if a == 'pages' else m[b]))
    if not m.get('page') and m.get('article-number'):
        f.append(('pages', m['article-number']))
    f.append(('doi', m['DOI']))
    if arxiv:
        f.append(('note', 'arXiv:' + arxiv))
    return '@%s{%s,\n' % (typ, key) + ',\n'.join('  %-12s= {%s}' % (a, b) for a, b in f) + '\n}\n'


if __name__ == '__main__':
    for arg in sys.argv[1:]:
        key, rest = arg.split('=', 1)
        doi, _, ax = rest.partition('@')
        print(entry(key, doi, ax or None))
