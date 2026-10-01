# SOTA knowledge base — schema (LLM Wiki)

This folder is an **LLM Wiki**: a persistent, LLM-maintained markdown knowledge base on
**MPPI (Model Predictive Path Integral) control for industrial manipulators and AMRs**, built for
Plan4ARI D4.1 (Activity 4, Task 4.1, A4 revision). The LLM writes and maintains the wiki; humans
curate sources, ask questions and review. This file is the schema: read it before any operation.

## Layers
| Layer | Path | Owner | Rule |
|---|---|---|---|
| Raw sources | `raw/papers/<key>.pdf`, `raw/text/<key>.txt`, `raw/meta/*.json` | human + tools | **Immutable**. Never edit or delete; only add. |
| Raw project docs | `raw/project/prj-*.docx|pdf` (+ `raw/text/prj-*.txt`) | human + tools | **Immutable**, internal Plan4ARI material, not citable. |
| Wiki | `wiki/**.md` | LLM | Edited by the LLM following this schema. |
| Deliverable | `latex/main.tex`, `latex/references.bib` | LLM + human | "Frozen" view of the wiki for the report. |
| Tools | `tools/*.py` | LLM | Stdlib-only Python helpers (Python 3.11, pdftotext from MiKTeX). |
| Skills | `.claude/skills/*/SKILL.md` | LLM | Procedures for each operation. |

## Keys and naming
- One **bibkey** per source: `<firstauthorlastname><year><shortname>`, lowercase ASCII, e.g. `zhang2024m3p2i`.
  Year = year of the version cited in the bib (published version if any).
- The same key names `raw/papers/<key>.pdf`, `raw/text/<key>.txt`, `wiki/sources/<key>.md` and the BibTeX entry.
- Other pages: kebab-case slugs in `concepts/`, `applications/`, `tools/`, `comparisons/`.

## Page types
- `wiki/sources/<key>.md` — one per bib entry. YAML frontmatter: `key, title, authors, year, venue, arxiv, doi, pdf, text, tags, status (stub|summarised|read)`.
  Sections: TL;DR · Method · Evidence (platform, rates, numbers) · Relevance for Plan4ARI · (Detailed notes) · Abstract · Links.
- `wiki/project/prj-*.md` — one per internal project document (see § *Project documents*).
- `wiki/concepts/*.md` — one idea per page (definition, taxonomy table, sources, takeaway).
- `wiki/applications/*.md` — application domain (arms, AMR, mobile manipulation, human-shared spaces).
- `wiki/tools/*.md` — software, simulators, hardware.
- `wiki/comparisons/*.md` — cross-cutting tables and the Plan4ARI gap analysis.
- `wiki/overview.md` — ≤1 page living synthesis. `wiki/index.md` — **generated** (`python tools/build_index.py`). `wiki/log.md` — append-only.

## Conventions
- Links: Obsidian-style `[[folder/slug]]` relative to `wiki/` (e.g. `[[sources/zhang2024m3p2i]]`, `[[concepts/multimodality]]`). Every page must be reachable from `index`.
- Every factual claim in concept/application/comparison pages must link the supporting source page. Numbers (rates, errors, speed-ups) must come from the source text — quote the section/table when adding them.
- Distinguish **facts from the paper** from **our assessment** (use a heading "Critical assessment (our view)" or "Plan4ARI takeaway").
- Verbatim text: only the arXiv abstract and short (<15 words) quotes. Summarise, do not copy.
- Language: English (the deliverable is in English). Chat with the user in Italian if they write in Italian.
- Dates absolute (YYYY-MM-DD). Today's knowledge cut is recorded in `log.md`.
- Bibliography: venues/DOIs verified with `tools/crossref_lookup.py`; arXiv-only entries stay `@misc` with `howpublished = {arXiv preprint arXiv:XXXX}` until published. Escape non-ASCII in the bib (`{\"u}`, `{\'a}`), bibtex is 8-bit.
- Licensed PDFs (e.g. IEEE Xplore copies such as `zhang2024m3p2i.pdf`) are for internal project use only; do not redistribute outside the consortium SharePoint.

## Project documents
Internal Plan4ARI material (Project Description, Grant Agreement, deliverable outlines/drafts, minutes,
specifications, slides exported to PDF), formats `.docx` and `.pdf`.
- Key `prj-<short-kebab>` (e.g. `prj-d41-outline`); file `raw/project/<key>.<ext>`; text `raw/text/<key>.txt`; page `wiki/project/<key>.md`.
- Frontmatter: `key, title, doctype (proposal|grant-agreement|outline|deliverable|report|minutes|specification|presentation|other), version, date, author, confidentiality (public|consortium|internal), file, text, original_name, tags, status`.
- Sections: Purpose · Key content · Requirements / constraints for the motion-planning framework (with document section) · Relation to the literature · Open points · Document outline · Links.
- **Not bibliographic**: never in `references.bib`, never `\cite`d (lint enforces). They provide *requirements and context*; papers provide *evidence*. Link them as `[[project/<key>]]`.
- New version of a document → new key with `-v2` suffix; raw files are never overwritten.

## Operations (see skills)
| Operation | Skill | Summary |
|---|---|---|
| Find new papers | `wiki-search` | arXiv/Crossref search with inclusion criteria; proposes keys; user confirms. |
| Ingest paper | `wiki-ingest` | add raw files → source page → update concept/application/comparison pages → index → log. |
| Ingest project doc | `wiki-ingest-project` | copy .docx/.pdf → extract text → project page with requirements → link to gap analysis → index → log. |
| Query | `wiki-query` | answer from the wiki with `[[links]]`; file valuable answers back as pages. |
| Lint | `wiki-lint` | `tools/lint_wiki.py` + semantic checks (contradictions, stale claims, missing pages). |
| Deliverable | `sota-latex` | sync `latex/main.tex` + `references.bib` with the wiki and compile. |

## Scope and inclusion criteria
- In scope: MPPI and path-integral control; sampling-based MPC siblings (CEM, predictive sampling, SVMPC) when compared to MPPI; applications to industrial/collaborative arms, mobile manipulators, AMR/AGV, human-shared spaces; safety/constraints; GPU/embedded implementations.
- Background (short pages, no PDF needed): classical MPC, DDP, trajectory optimisation, DWA/TEB.
- Out of scope unless asked: aerial/legged-only works, pure RL without MPPI.

## Quick commands
```bash
python tools/arxiv_tool.py search "abs:MPPI AND abs:manipulator" -n 15 --sort date
python tools/arxiv_tool.py add <key> <arxiv_id>
python tools/crossref_lookup.py "<title>"
python tools/new_source.py <key>
python tools/add_project_doc.py "<file.docx|pdf>" prj-<name> --doctype outline
python tools/build_index.py
python tools/lint_wiki.py
cd latex && latexmk -pdf main.tex
```
