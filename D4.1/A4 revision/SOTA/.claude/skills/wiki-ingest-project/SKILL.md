---
name: wiki-ingest-project
description: Ingest an internal Plan4ARI project document (.docx or .pdf - proposal, grant agreement, deliverable outline or draft, minutes, specification, slides exported to PDF) into the SOTA LLM wiki as a project page (wiki/project/prj-*.md), extract requirements and decisions, and link them to the literature pages. Use when the user asks to add/ingest a project document, outline, deliverable, Word file or internal PDF (not a scientific paper).
---

# wiki-ingest-project — add an internal project document

Run from the SOTA root. Read `CLAUDE.md` first (§ *Project documents*).

**Paper or project document?** A peer-reviewed paper / preprint / thesis with a citable reference → use `wiki-ingest`. Anything internal to Plan4ARI (no bibliographic reference, not citable in the deliverable) → this skill.

## 1. Key and metadata
- Key: `prj-<short-kebab>`, e.g. `prj-d41-outline`, `prj-plan4ari-proposal`, `prj-d71-outline`. Check `wiki/project/` for collisions.
- A new version of an already-ingested document gets a new key with suffix (`prj-d41-outline-v2`): raw files are immutable. Link the two pages ("supersedes / superseded by").
- Choose `--doctype`: proposal, grant-agreement, outline, deliverable, report, minutes, specification, presentation, other.

## 2. Raw file + text + scaffold
```bash
python tools/add_project_doc.py "<path to file.docx|pdf>" prj-<name> --doctype <type> [--title "..."] [--date YYYY-MM-DD] [--version 0.1] [--confidentiality consortium]
```
- The file is **copied** (never moved) to `raw/project/<key>.<ext>`; text extracted to `raw/text/<key>.txt` (docx: headings marked `#`, tables as `| ... |` rows; pdf: `pdftotext -layout`).
- `.doc`, `.pptx`, `.xlsx` are not supported directly: ask the user to export to `.docx`/`.pdf` (or read them with the matching skill and save a PDF export).
- Scanned PDFs give empty text: tell the user (OCR needed, see the `pdf` skill).

## 3. Read and summarise
Read `raw/text/<key>.txt` fully (in chunks if long). Fill the page `wiki/project/<key>.md`:
- **Purpose** — what the document is, author/partner, version, status (draft/approved).
- **Key content** — structured summary: objectives, scenarios, architecture, KPIs/targets, timeline, WP/task mapping.
- **Requirements / constraints for the motion-planning framework** — one bullet per requirement, with the document section (e.g. "§6 MPC: jerk and torque constraints"). These are the most valuable lines: they drive the gap analysis.
- **Relation to the literature** — link each requirement to `[[concepts/...]]`, `[[applications/...]]`, `[[sources/...]]` that address it, or mark it as an open gap.
- **Open points / decisions to take**.
- Set `status: summarised`; adjust `title`, `date`, `version` in the frontmatter if the scaffold guessed wrong.
- Quote sparingly; summarise in English. Do not copy confidential numbers (budgets, person-months, personal data) unless they are needed for the technical analysis.

## 4. Propagate
- Update `wiki/comparisons/plan4ari-gap-analysis.md` (requirements ↔ gaps) and, if relevant, `wiki/overview.md` and application pages. Link back with `[[project/<key>]]`.
- If a requirement contradicts what the wiki/deliverable assumes, flag it with `> **Contradiction:**` and tell the user.

## 5. Rebuild, lint, log
```bash
python tools/build_index.py
python tools/lint_wiki.py
```
Append to `wiki/log.md`: `## [YYYY-MM-DD] ingest-project | <key> — <title>` with pages updated.

## Rules
- Project documents are **never** added to `latex/references.bib` nor `\cite`d (the linter enforces it). The deliverable may describe their content in prose ("according to the Plan4ARI Project Description, ...").
- Confidentiality: default `consortium`. Never copy project documents outside the consortium SharePoint, never upload them to external services.
