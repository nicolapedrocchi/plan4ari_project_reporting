"""arXiv helper for the SOTA wiki (stdlib only).

Usage
  python tools/arxiv_tool.py search "abs:MPPI AND abs:manipulator" [-n 10] [--sort date|relevance]
  python tools/arxiv_tool.py add <bibkey> <arxiv_id> [<bibkey> <arxiv_id> ...]
        -> appends metadata to raw/meta/arxiv_metadata.json, downloads raw/papers/<bibkey>.pdf,
           extracts raw/text/<bibkey>.txt (needs pdftotext from MiKTeX/poppler on PATH)

Bibkey convention: <firstauthorlastname><year><shortname>, lowercase, e.g. zhang2024m3p2i.
Be polite with arXiv: the tool waits 3 s between requests.
"""
import argparse
import os
import subprocess
import sys
import time
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wikilib import PAPERS, TEXT, load_meta, save_meta  # noqa: E402

NS = {'a': 'http://www.w3.org/2005/Atom', 'x': 'http://arxiv.org/schemas/atom'}
API = 'http://export.arxiv.org/api/query?'
UA = {'User-Agent': 'Mozilla/5.0 (CNR-STIIMA SOTA wiki)'}


def _entries(url):
    x = ET.fromstring(urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=90).read())
    for e in x.findall('a:entry', NS):
        g = lambda t: (e.find(t, NS).text if e.find(t, NS) is not None else '') or ''
        yield dict(arxiv=g('a:id').split('abs/')[-1].rsplit('v', 1)[0],
                   title=' '.join(g('a:title').split()),
                   authors=[a.find('a:name', NS).text for a in e.findall('a:author', NS)],
                   published=g('a:published')[:10], journal_ref=g('x:journal_ref'), doi=g('x:doi'),
                   abstract=' '.join(g('a:summary').split()))


def search(q, n, sort):
    s = 'submittedDate' if sort == 'date' else 'relevance'
    url = API + 'sortBy=%s&max_results=%d&search_query=%s' % (s, n, urllib.parse.quote(q))
    for e in _entries(url):
        print('%s | %s | %s | %s' % (e['arxiv'], e['title'], ', '.join(e['authors'][:4]), e['published']))


def add(pairs):
    meta = load_meta()
    ids = [i for _, i in pairs]
    found = {e['arxiv']: e for e in _entries(API + 'max_results=100&id_list=' + ','.join(ids))}
    os.makedirs(PAPERS, exist_ok=True)
    os.makedirs(TEXT, exist_ok=True)
    for key, i in pairs:
        if i not in found:
            print('NOT FOUND', key, i)
            continue
        meta[key] = found[i]
        pdf = os.path.join(PAPERS, key + '.pdf')
        if not os.path.exists(pdf):
            data = urllib.request.urlopen(urllib.request.Request('https://arxiv.org/pdf/' + i, headers=UA), timeout=120).read()
            open(pdf, 'wb').write(data)
            time.sleep(3)
        txt = os.path.join(TEXT, key + '.txt')
        try:
            subprocess.run(['pdftotext', '-enc', 'UTF-8', pdf, txt], check=True)
        except Exception as ex:  # pdftotext missing
            print('pdftotext failed for', key, ex)
        print('added', key, '|', found[i]['title'])
    save_meta(meta)


if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    sub = ap.add_subparsers(dest='cmd', required=True)
    s = sub.add_parser('search')
    s.add_argument('query')
    s.add_argument('-n', type=int, default=10)
    s.add_argument('--sort', choices=['date', 'relevance'], default='relevance')
    a = sub.add_parser('add')
    a.add_argument('pairs', nargs='+')
    args = ap.parse_args()
    if args.cmd == 'search':
        search(args.query, args.n, args.sort)
    else:
        p = args.pairs
        if len(p) % 2:
            sys.exit('add expects <bibkey> <arxiv_id> pairs')
        add(list(zip(p[::2], p[1::2])))
