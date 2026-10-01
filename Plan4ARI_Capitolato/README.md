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
latexmk plan4ari_capitolato.tex
```

Or simply:

```bash
make
```

## Structure

- `plan4ari_capitolato.tex` - entry point
- `../latex-style/plan4ari_capitolato.sty` - shared document style, found through `latexmkrc`
- `sections/` - converted document body
- `assets/` - LaTeX-ready embedded images, including PDF conversions of the original EMF graphics
- `assets/original/` - exact copies of all eight media files embedded in the DOCX

The package does not require the original DOCX in order to compile.

## Validation

The included `main.pdf` was compiled twice with XeLaTeX and visually checked page by page. The PDF contains 33 pages and 20 unique external hyperlink targets. Pagination differs from Word because LaTeX reflows text and tables natively.
