# Plan4ARI - LaTeX package

This package is a structured LaTeX conversion of the supplied DOCX file. It preserves:

- all embedded figures and logos;
- external hyperlinks and PDF bookmarks;
- heading hierarchy and alphanumeric section numbering;
- footnotes, lists, bold/underlined emphasis, long tables and captions;
- the page header with the FISA and MUR logos, the blue visual accent, and right-aligned page numbers.

The layout is intentionally close to the original Word document, but it is implemented with native LaTeX flow rather than fixed page positioning. Small pagination differences are therefore expected.

## Build

Recommended engine: XeLaTeX.

```bash
latexmk plan4ari_capitolato_A2_revision.tex
```

Or simply:

```bash
make
```

## Structure

- `plan4ari_capitolato_A2_revision.tex` - entry point
- `sections/changelog.tex` - revision history and A2 change summary (first pages)
- `styles/macros.tex` - A2 change-tracking colour `RevAii` and `evAii{}` macro
- `../latex-style/plan4ari_capitolato.sty` - shared document style, found through `latexmkrc`
- `sections/` - converted document body
- `assets/` - LaTeX-ready embedded images, including PDF conversions of the original EMF graphics
- `assets/original/` - exact copies of all eight media files embedded in the DOCX

The package does not require the original DOCX in order to compile.

## Validation

The included `main.pdf` was compiled twice with XeLaTeX and visually checked page by page. The PDF contains 33 pages and 20 unique external hyperlink targets. Pagination differs from Word because LaTeX reflows text and tables natively.

## Revision A2 (23 September 2026)

Baseline: `../2026-02-01-approved`. Source: `../../D2.1/Plan4ARI_Capitolato_A2_Revised.docx`.
Only the Activity 2 table (objectives, T2.1-T2.8) and the A2 references in Milestones 2 and 4 change;
this text is typeset in colour `RevAii` (#B4237A) and summarised in `sections/changelog.tex`.
Wrap any further A2 change in `evAii{...}` and add a row to the changelog.
