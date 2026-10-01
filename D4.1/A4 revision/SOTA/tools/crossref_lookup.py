"""Look up the published version (venue, volume, pages, DOI) of a paper on Crossref.

Usage
  python tools/crossref_lookup.py "Title of the paper" ["Another title" ...]
  python tools/crossref_lookup.py --doi 10.1109/LRA.2024.3426183

Use it to upgrade an arXiv @misc entry in latex/references.bib to @article/@inproceedings.
Always check that the returned title really matches (score >= 0.9) before editing the bib.
"""
import difflib
import json
import sys
import urllib.parse
import urllib.request

API = 'https://api.crossref.org/works'


def show(it, score=None):
    au = ', '.join((a.get('given', '') + ' ' + a.get('family', '')).strip() for a in it.get('author', []))
    print('%s| %s | %s | %s | vol %s no %s pp %s | %s | %s' % (
        '' if score is None else '[%.2f] ' % score, it.get('DOI'), (it.get('title') or [''])[0],
        (it.get('container-title') or [''])[0], it.get('volume', ''), it.get('issue', ''), it.get('page', ''),
        it.get('issued', {}).get('date-parts', [[None]])[0], au))


def by_title(t):
    url = API + '?rows=5&query.bibliographic=' + urllib.parse.quote(t)
    for it in json.load(urllib.request.urlopen(url, timeout=30))['message']['items']:
        if '/mm' in it.get('DOI', '') or it.get('type') == 'component':  # skip supplementary material
            continue
        s = difflib.SequenceMatcher(None, (it.get('title') or [''])[0].lower(), t.lower()).ratio()
        show(it, s)


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['--doi']:
        for d in a[1:]:
            show(json.load(urllib.request.urlopen(API + '/' + d, timeout=30))['message'])
    else:
        for t in a:
            print('##', t)
            by_title(t)
