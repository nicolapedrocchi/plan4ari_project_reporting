---
name: wiki-ingest
description: Ingest one or more new sources (arXiv id, PDF dropped in raw/papers, or DOI) into the MPPI SOTA LLM wiki - store raw files, add BibTeX, write the source page, propagate the knowledge to concept/application/comparison pages, rebuild the index and log the operation. Use when the user says "ingest/aggiungi/integra questo paper", gives an arXiv link or drops a PDF.
---

# wiki-ingest — add a source and integrate it

Run from the SOTA root. Read `CLAUDE.md` first. This skill is for **citable scientific sources** (papers, preprints, theses, books). Internal Plan4ARI documents (.docx/.pdf proposals, outlines, minutes) → use `wiki-ingest-project`. One source at a time; for batches repeat steps 2–7 per source and do steps 8–10 once.

## 1. Identify and key
- Decide the bibkey `<lastname><year><shortname>` (year of the version you will cite). Check it does not exist: `ls wiki/sources/<key>.md`.

## 2. Raw files (immutable layer)
- **arXiv**: `python tools/arxiv_tool.py add <key> <arxiv_id>` → `raw/papers/<key>.pdf`, `raw/text/<key>.txt`, metadata in `raw/meta/arxiv_metadata.json`.
- **PDF provided by the user**: copy/rename it to `raw/papers/<key>.pdf` (do not modify it), then `pdftotext -enc UTF-8 raw/papers/<key>.pdf raw/text/<key>.txt`.
- Never overwrite or delete existing raw files.

## 3. Bibliography
- Look up the published version: `python tools/crossref_lookup.py "<exact title>"` (accept only matches with score ≥ 0.9 and same authors).
- Append the entry to `latex/references.bib` using the key. Journal → `@article`, conference → `@inproceedings` (booktitle in the style `Proc. IEEE Int. Conf. Robotics and Automation (ICRA)`), preprint → `@misc` with `howpublished = {arXiv preprint arXiv:<id>}` and `url`. Add `doi` when known and `note = {arXiv:<id>}` for published papers with an arXiv version.
- Escape non-ASCII characters (`{\"u}`, `{\'a}`) and protect acronyms in titles with braces (`{MPPI}`).

## 4. Read the source
- Read `raw/text/<key>.txt` (start with abstract, intro, method, experiments, conclusions; for long texts read in chunks). If figures/tables matter, read the PDF pages with the Read tool.
- Extract: problem, method (what changes w.r.t. vanilla MPPI), platform (arm/AMR/sim), rates/horizon/samples, key quantitative results, limitations stated by the authors, code availability.

## 5. Source page
- Scaffold: `python tools/new_source.py <key>` (fills frontmatter from bib + metadata). Then **edit** the page:
  - `TL;DR`, `Method`, `Evidence` (numbers with table/section reference), `Relevance for Plan4ARI`, optional `Detailed notes` and `Critical assessment (our view)`.
  - `tags:` from the existing tag vocabulary in `wiki/index.md` (add new tags sparingly).
  - `status: summarised` (or `read` after a full careful reading).
  - `## Links` with `[[concepts/...]]`, `[[applications/...]]`, related `[[sources/...]]`.
- Optionally add a seed entry to `tools/source_notes.py` (not required).

## 6. Propagate (this is the important part)
- Update **every** concept/application/tool/comparison page the source touches (typically 2–6): add a table row or bullet with a `[[sources/<key>]]` link.
- Update `wiki/comparisons/mppi-variants-matrix.md` if it is an MPPI variant.
- If the source contradicts or supersedes an existing claim, do not silently overwrite: write both, mark `> **Contradiction:**` with links, and mention it to the user.
- If a new cross-cutting idea emerges with ≥2 sources, create a new concept page.
- Update `wiki/overview.md` only if the big picture changes; update `comparisons/plan4ari-gap-analysis.md` if a gap is closed or a new one appears.

## 7. Check the deliverable impact
- If the source changes something stated in `latex/main.tex`, tell the user and offer the `sota-latex` skill (do not edit the LaTeX silently).

## 8. Rebuild and lint
```bash
python tools/build_index.py
python tools/lint_wiki.py
```
Fix all ERRORs.

## 9. Log
Append to `wiki/log.md`:
```
## [YYYY-MM-DD] ingest | <key> — <short title>
- pages created/updated: ...
- notable facts / contradictions: ...
```

## 10. Report
Tell the user in 3–6 lines: what the paper adds, which pages changed, any contradiction or impact on the deliverable.
