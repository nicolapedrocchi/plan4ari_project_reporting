
# Plan4ARI Professional Beamer Package

Files included:
- `Plan4ARI_main.tex` — main presentation source.
- `plan4ari_theme.sty` — custom Beamer colors, footline, and helper commands.
- `Plan4ARI_refs.bib` — selected bibliography entries from the proposal.
- `README.md` — this file.

## Compile
A standard `pdflatex` workflow should work:

```bash
pdflatex Plan4ARI_main.tex
pdflatex Plan4ARI_main.tex
```

If your TeX distribution is missing packages, install at least:
- `beamer`
- `pgfgantt`
- `tikz/pgf`
- `booktabs`
- `tabularx`
- `lmodern`

## Notes
- The deck is authored directly from the uploaded Plan4ARI proposal.
- Architecture and workflow figures are recreated in TikZ rather than copied as embedded images.
- The deliverables/milestones slides keep the proposal content and note explicit numbering inconsistencies where relevant.
