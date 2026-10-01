---
name: sota-latex
description: Update, extend or compile the LaTeX state-of-the-art note (latex/main.tex + latex/references.bib) from the MPPI SOTA LLM wiki, keeping citations consistent with wiki source pages and the 4-5 page budget. Use when the user asks to update/rewrite/compile the SOTA document, add a paper to the document, or export a section for D4.1.
---

# sota-latex — the deliverable view of the wiki

Run from the SOTA root. Read `CLAUDE.md` first. The LaTeX document is a *frozen, curated* view of the wiki: the wiki is the source of truth for facts, the LaTeX for wording.

## Document structure (keep it)
1. Scope and motivation (Plan4ARI context)
2. Theoretical framework (path integral control, information-theoretic MPPI, Algorithm 1, properties/limitations)
3. MPPI vs MPC and other horizon-based planners (Table 1)
4. Analysis of the literature: algorithmic advances · industrial/collaborative manipulators · mobile robots and AMRs · in-depth M3P2I (Zhang et al. 2024) · software ecosystem
5. Gap analysis and implications for the proposed framework (Fig. 1)
6. Conclusions

Budget: **~5 pages of body** (A4, 10 pt, 2.1 cm margins) + references. If adding content, compress elsewhere.

## Shared files (important)
- The SOTA body lives in `latex/sota_body.tex` (macros in `latex/sota_macros.tex`); `latex/main.tex` is only a wrapper.
- The D4.1 deliverable (`../D4.1-latex/main.tex`, class `Project Reporting/latex-style/plan4ari.cls`, XeLaTeX) **inputs the same `sota_body.tex`** in its Section 6 (with `\sotafullfalse`, i.e. without Scope / Gap analysis / Conclusions, headings demoted one level) and uses the same `references.bib`.
- After editing `sota_body.tex` or the bib, rebuild **both**: `cd latex && latexmk -pdf main.tex` and `cd ../D4.1-latex && latexmk main.tex`.
- Use the Write/Edit tools for TeX content: shell heredocs mangle backslash sequences such as `\n` and `\f` (they become control characters).

## Procedure
1. Identify the wiki pages behind the change (`wiki/index.md`, concept/application/comparison pages, source pages).
2. Edit `latex/main.tex`:
   - cite with `\cite{<key>}`; every key must exist in `latex/references.bib` **and** have `wiki/sources/<key>.md`;
   - numbers only if present in the source page *Evidence* section (or verified in `raw/text/`);
   - keep the style: British English, concise, "we" for the consortium view, facts vs assessment explicit.
3. If new references are needed and not in the wiki, run the `wiki-ingest` skill first.
4. Compile and check:
   ```bash
   cd latex
   latexmk -pdf -interaction=nonstopmode main.tex
   grep -E "^!|undefined|Overfull" main.log
   ```
   Fix errors and undefined citations; check the page count (`Output written on main.pdf (N pages`)` and view the PDF pages (Read tool on `latex/main.pdf`) to verify figures/tables layout.
5. Run `python tools/lint_wiki.py` (it checks `\cite` keys against the bib).
6. Log: `## [YYYY-MM-DD] latex | <what changed>` in `wiki/log.md`.

## Export tips
- For integration into the D4.1 master document: sections can be `\input` as they are; the bib uses `IEEEtran` style and plain `cite` package.
- For Word: `pandoc main.tex --citeproc --bibliography=references.bib -o main.docx` (check equations/figures by hand).
