# Plan4ARI LaTeX style

`plan4ari.cls` reproduces the layout of the Plan4ARI Word deliverables (derived from
`D1.1/Plan4ARI_D1.1_Project_Management_Report.docx`, 2026-10-01).

| Element | Word source | LaTeX |
|---|---|---|
| Page | A4, margins 2.0 cm left/right, 1.8 cm top/bottom | `geometry` |
| Body | Cambria 10 pt, colour #243746, justified | `fontspec` (XeLaTeX) or Caladea (pdfLaTeX) |
| Heading 1 | Calibri bold 15 pt #1F4E78, new page | `\section` |
| Heading 2 | Calibri bold 12 pt | `\subsection` |
| Heading 3 | Calibri bold 10.5 pt #1F4E78 | `\subsubsection` |
| Heading 4 | Calibri bold italic #4F81BD, numbered | `\paragraph` |
| Title / cover | Calibri bold 25 pt #1F4E78, rule #4F81BD, info table (#D9EAF7 key column, #F2F4F6 alternate rows) | `\makecover`, `\inforow{key}{value}` |
| Document control | header #1F4E78, white text | `documentcontrol` env + `\docversion{v}{date}{author}{change}` |
| Data tables | header #17365D, white bold, grid | `plangrid` env, `\planheadrow`, `\thead{}` |
| Boxed note | fill #DBE5F1, black frame | `planbox` env |
| Caption | bold #4F81BD 9 pt, "Figure 1 Text" | `caption` setup |
| Project name | Calibri bold #709FDB | `\PlanARI` |

## Usage
```latex
\documentclass{plan4ari}          % option: nopagenumbers
\deliverable{D4.1}
\deliverabletitle{Updated Scientific Plan ...}
\docstatusline{Draft -- Version 0.1}
\inforow{Project acronym}{Plan4ARI}
...
\begin{document}
\makecover
\begin{documentcontrol}
\docversion{0.1}{1 October 2026}{N. Pedrocchi}{Initial draft}
\end{documentcontrol}
\sectionsonsamepage \tableofcontents \sectionsonnewpage
\section{Executive summary}
\begin{planbox} Key message \end{planbox}
\begin{plangrid}{|L{3cm}|Y|}
\planheadrow \thead{Column A} & \thead{Column B}\\ \hline
a & b \\ \hline
\end{plangrid}
\end{document}
```
Build with **XeLaTeX** (`latexmk -xelatex`, or a `latexmkrc` with `$pdf_mode = 5;`). Put this folder on `TEXINPUTS`
(see `D4.1/A4 revision/D4.1-latex/latexmkrc`). pdfLaTeX also works (metric-compatible fonts Caladea/Carlito).

Not reproduced: Word fields (automatic TOC update), highlight colours used for TBC items (use `\colorbox{yellow}{...}` if needed).
