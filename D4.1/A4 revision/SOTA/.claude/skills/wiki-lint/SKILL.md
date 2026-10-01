---
name: wiki-lint
description: Health-check the MPPI SOTA LLM wiki - structural lint (tools/lint_wiki.py), bibliography freshness (arXiv preprints that got published), semantic checks for contradictions, stale claims, stubs, missing concept pages and weak cross-links; then fix or report. Use when the user asks for a lint/check/cleanup of the wiki or periodically after several ingests.
---

# wiki-lint — keep the wiki healthy

Run from the SOTA root. Read `CLAUDE.md` first.

## 1. Structural lint
```bash
python tools/build_index.py
python tools/lint_wiki.py
```
Fix every ERROR (missing source page → `python tools/new_source.py <key>` and complete it; unknown `\cite` → add bib entry or fix the key; broken `[[link]]` → fix or create the page). Review WARNs.

## 2. Bibliography freshness
- For each `@misc` (arXiv-only) entry in `latex/references.bib`, run `python tools/crossref_lookup.py "<title>"`; if a published version exists (score ≥ 0.9), upgrade the entry (type, venue, volume, pages, DOI) and the `venue:` field of the source page. Keep the key unchanged unless the year changes the key convention — if you rename a key, rename raw files, page, bib and every `[[link]]`/`\cite` consistently.

## 3. Semantic checks (read pages, do not just grep)
- **Stubs**: pages with `status: stub` → summarise from `raw/text/`.
- **Unsupported claims**: statements in concept/application/comparison pages without a `[[sources/...]]` link.
- **Numbers**: spot-check 3–5 numbers against the source text.
- **Contradictions / stale claims**: newer sources that supersede statements (e.g. "no method does X" when a newly ingested paper does X). Update the page and the gap analysis.
- **Missing pages**: ideas mentioned in ≥2 pages without their own concept page; frequent tags without a concept page.
- **Weak linking**: source pages with < 2 links; concept pages not linked from overview.
- **Deliverable drift**: compare `latex/main.tex` claims with the wiki; list sentences that are no longer accurate.

## 4. Report and log
- Present a short table `issue | page | action taken / proposed`. Apply safe fixes directly; ask before large rewrites or LaTeX changes.
- Rebuild index, re-run the linter, append to `wiki/log.md`: `## [YYYY-MM-DD] lint | <n> errors fixed, <m> issues open`.
