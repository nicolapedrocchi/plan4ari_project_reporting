---
name: wiki-query
description: Answer questions about MPPI, sampling-based MPC, industrial manipulators, AMRs or the Plan4ARI framework using the SOTA LLM wiki as primary source, with [[links]] to supporting pages, and file valuable answers back into the wiki. Use for any question on the content of the knowledge base ("quali lavori...", "confronta...", "che rate raggiunge...").
---

# wiki-query — answer from the knowledge base

Run from the SOTA root. Read `CLAUDE.md` first.

## Steps
1. Read `wiki/index.md`, then `wiki/overview.md`, then the relevant concept/application/comparison pages, then the source pages they link. For questions about Plan4ARI requirements, scope, KPIs or architecture, read the project pages `wiki/project/prj-*.md` (requirements come from there, evidence from `sources/`). Use Grep over `wiki/` for keywords (variant names, robot names, numbers).
2. If the wiki is insufficient, read `raw/text/<key>.txt` of the relevant sources (and the PDF pages for tables/figures). If the corpus itself is insufficient, say so and offer `wiki-search`.
3. Answer in the user's language with:
   - a direct answer first;
   - supporting facts with the source page links (`[[sources/<key>]]`) and, for numbers, the table/section of the paper;
   - a clear separation between *what the papers say* and *our assessment*.
   Choose the format that fits: short prose, comparison table, bullet list, or a LaTeX snippet if the user is writing the deliverable.
4. **File back** answers with lasting value (a new comparison, a synthesis, a design decision): create or update a page in `wiki/comparisons/` or `wiki/concepts/` with frontmatter (`title, type, updated`) and links; rebuild the index (`python tools/build_index.py`). Ask the user if unsure whether it is worth keeping.
5. Log: `## [YYYY-MM-DD] query | <question in ≤10 words>` with the pages consulted and any page filed back.

## Rules
- Never cite a paper that has no page in `wiki/sources/`; never invent numbers.
- If two sources disagree, report both.
