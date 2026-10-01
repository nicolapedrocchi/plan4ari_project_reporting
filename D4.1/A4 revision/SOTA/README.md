# SOTA — MPPI for industrial manipulators and AMRs (Plan4ARI D4.1, A4 revision)

Contents of this folder:

```
SOTA/
├── latex/                  ← deliverable: SOTA note (main.tex, references.bib, main.pdf)
├── wiki/                   ← LLM-maintained knowledge base (open in Obsidian or any md viewer)
│   ├── index.md            ← generated catalogue of all pages (start here)
│   ├── overview.md         ← 1-page living synthesis
│   ├── log.md              ← append-only history of ingests/queries/lints
│   ├── sources/            ← one page per paper (= one BibTeX key)
│   ├── concepts/           ← theory and cross-cutting ideas
│   ├── applications/       ← arms, AMRs, mobile manipulation, human-shared spaces
│   ├── tools/              ← software ecosystem
│   ├── comparisons/        ← variant matrix, Plan4ARI gap analysis
│   └── project/            ← internal Plan4ARI documents (prj-*), requirements and context
├── raw/                    ← immutable sources
│   ├── papers/<key>.pdf    ← 52 PDFs (arXiv open access + JMLR + RSS + 1 IEEE licensed copy)
│   ├── project/prj-*.docx|pdf ← internal project documents (copies, consortium-only)
│   ├── text/<key>.txt      ← pdftotext extraction (what the LLM reads)
│   └── meta/               ← arXiv metadata and Crossref matches
├── tools/                  ← stdlib Python helpers (search, add, scaffold, index, lint)
├── .claude/skills/         ← SKILL.md procedures: wiki-search, wiki-ingest, wiki-ingest-project, wiki-query, wiki-lint, sota-latex
├── CLAUDE.md               ← wiki schema (rules for the LLM)
└── AGENTS.md               ← pointer for non-Claude agents
```

## How to use
- Read the deliverable: `latex/main.pdf` (rebuild: `cd latex && latexmk -pdf main.tex`).
- Browse the knowledge: open `wiki/` as an Obsidian vault (wikilinks `[[...]]` work), start from `index.md`.
- Grow it with Claude Code opened **in this SOTA folder** (so `CLAUDE.md` and the skills are loaded):
  - "cerca nuovi paper su MPPI per mobile manipulator" → `wiki-search`
  - "ingerisci questo PDF / arXiv 2xxx.xxxxx" → `wiki-ingest`
  - "aggiungi questo documento di progetto (docx/pdf)" → `wiki-ingest-project`
  - "quali varianti MPPI garantiscono vincoli hard sui giunti?" → `wiki-query`
  - "fai un lint del wiki" → `wiki-lint`
  - "aggiorna il documento LaTeX con le nuove fonti" → `sota-latex`

## Notes
- `raw/papers/zhang2024m3p2i.pdf` is the IEEE Xplore copy downloaded under the Università di Brescia licence: internal use only.
- Bibliographic data were verified on arXiv and Crossref on 2026-10-01; 2026 preprints may get published versions later (re-run `wiki-lint`).
