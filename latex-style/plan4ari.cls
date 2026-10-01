% =====================================================================
%  plan4ari.cls -- LaTeX class reproducing the Plan4ARI deliverable layout
%  Derived from Plan4ARI_D1.1_Project_Management_Report.docx (Word styles,
%  theme colours, page setup, cover page and table styles).
%
%  Engine: XeLaTeX or LuaLaTeX (Cambria/Calibri system fonts via fontspec).
%          pdfLaTeX also works with metric-compatible Caladea/Carlito.
%  Options: pagenumbers (default) | nopagenumbers, draft (adds DRAFT watermark
%           line on cover), any article option (e.g. 11pt is NOT recommended).
% =====================================================================
\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{plan4ari}[2026/10/01 v0.1 Plan4ARI deliverable class]

\newif\ifplan@pagenumbers \plan@pagenumberstrue
\DeclareOption{pagenumbers}{\plan@pagenumberstrue}
\DeclareOption{nopagenumbers}{\plan@pagenumbersfalse}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{article}}
\ProcessOptions\relax
\LoadClass[10pt,a4paper]{article}

% ---------------------------------------------------------------- page
% Word: A4, top/bottom 1020 twips (1.8 cm), left/right 1134 twips (2.0 cm)
\RequirePackage[a4paper,top=1.8cm,bottom=1.8cm,left=2cm,right=2cm,
  headsep=0.4cm,footskip=0.7cm,includefoot]{geometry}

% ---------------------------------------------------------------- colours
% Word styles / theme1.xml
\RequirePackage[dvipsnames,table]{xcolor}
\definecolor{p4aText}{HTML}{243746}      % Normal
\definecolor{p4aHeading}{HTML}{1F4E78}   % Title, Heading 1/3, doc-control header
\definecolor{p4aAccent}{HTML}{4F81BD}    % accent1: Heading 4, captions, title rule
\definecolor{p4aTableHead}{HTML}{17365D} % data-table header rows
\definecolor{p4aKeyCell}{HTML}{D9EAF7}   % cover info table, key column
\definecolor{p4aRowAlt}{HTML}{F2F4F6}    % alternate rows
\definecolor{p4aNote}{HTML}{DBE5F1}      % boxed note
\definecolor{p4aProject}{HTML}{709FDB}   % "Plan4ARI" project-name character style

% ---------------------------------------------------------------- fonts
\RequirePackage{iftex}
\ifPDFTeX
  \RequirePackage[T1]{fontenc}
  \RequirePackage{caladea}                 % Cambria-compatible (body)
  \RequirePackage[sfdefault=false]{carlito}% Calibri-compatible (headings)
  \newcommand{\plan@headfont}{\fontfamily{Carlito}\selectfont}
\else
  \RequirePackage{fontspec}
  \setmainfont{Cambria}[Ligatures=TeX]
  \setsansfont{Calibri}[Ligatures=TeX]
  \newfontfamily\plan@calibri{Calibri}[Ligatures=TeX]
  \newcommand{\plan@headfont}{\plan@calibri}
\fi
\RequirePackage{microtype}
\AtBeginDocument{\color{p4aText}}

% Normal: 10 pt, line 252/240 = 1.05, after 40 twips (2 pt), justified
\linespread{1.05}
\setlength{\parindent}{0pt}
\setlength{\parskip}{6pt plus 2pt minus 1pt}

% ---------------------------------------------------------------- headings
\RequirePackage{titlesec}
\setcounter{secnumdepth}{4}
\setcounter{tocdepth}{2}
% Heading 1: Calibri bold 15 pt, 1F4E78, page break before, 24 pt before / 12 pt after
\titleformat{\section}{\plan@headfont\fontsize{15}{18}\selectfont\bfseries\color{p4aHeading}}{\thesection}{0.8em}{}
\titlespacing*{\section}{0pt}{0pt}{12pt}
\newif\ifplan@newpagesections \plan@newpagesectionstrue
\newcommand{\sectionsonsamepage}{\plan@newpagesectionsfalse}
\newcommand{\sectionsonnewpage}{\plan@newpagesectionstrue}
\let\plan@origsection\section
\renewcommand{\section}{\ifplan@newpagesections\clearpage\fi\plan@origsection}
% Heading 2: Calibri bold 12 pt, text colour, 7 pt before / 4 pt after
\titleformat{\subsection}{\plan@headfont\fontsize{12}{14.5}\selectfont\bfseries\color{p4aText}}{\thesubsection}{0.8em}{}
\titlespacing*{\subsection}{0pt}{10pt}{4pt}
% Heading 3: Calibri bold 10.5 pt, 1F4E78
\titleformat{\subsubsection}{\plan@headfont\fontsize{10.5}{13}\selectfont\bfseries\color{p4aHeading}}{\thesubsubsection}{1.2em}{}
\titlespacing*{\subsubsection}{0pt}{8pt}{3pt}
% Heading 4: Calibri bold italic, accent1, numbered (4.2.1.1)
\titleformat{\paragraph}[block]{\plan@headfont\normalsize\bfseries\itshape\color{p4aAccent}}{\theparagraph}{1.6em}{}
\titlespacing*{\paragraph}{0pt}{8pt}{1pt}
% unnumbered run-in label used in running text
\newcommand{\runin}[1]{\textbf{#1}\enspace}

% ---------------------------------------------------------------- captions
% Caption: bold, accent1, 9 pt, "Figure 1 Text" (no colon), centred
\RequirePackage{caption}
\DeclareCaptionLabelSeparator{p4aspace}{\enspace}
\captionsetup{font={small,bf,color=p4aAccent},labelsep=p4aspace,justification=centering,skip=4pt}
\captionsetup[table]{position=top}

% ---------------------------------------------------------------- lists
\RequirePackage{enumitem}
\setlist{itemsep=1pt,topsep=3pt,parsep=0pt}
\setlist[itemize,1]{label={\small\textbullet},leftmargin=2.2em}
\setlist[itemize,2]{label={\color{p4aAccent}\rule[0.25ex]{0.45em}{0.45em}},leftmargin=1.8em}

% ---------------------------------------------------------------- tables
\RequirePackage{array,tabularx,longtable,booktabs,multirow}
\newcolumntype{L}[1]{>{\raggedright\arraybackslash}p{#1}}
\newcolumntype{Y}{>{\raggedright\arraybackslash}X}
\setlength{\arrayrulewidth}{0.4pt}
\renewcommand{\arraystretch}{1.35}
% header cell for data tables (17365D, white, Calibri bold)
\newcommand{\thead}[1]{\leavevmode{\plan@headfont\bfseries\color{white}#1}}
\newcommand{\planheadrow}{\rowcolor{p4aTableHead}}
\newcommand{\planaltrow}{\rowcolor{p4aRowAlt}}
% Grid-style data table like the RACI matrix:
%   \begin{plangrid}{|L{3cm}|Y|Y|} \planheadrow \thead{A} & \thead{B} & \thead{C}\\ \hline ... \end{plangrid}
\newenvironment{plangrid}[1]{\par\noindent\arrayrulecolor{black}\tabularx{\linewidth}{#1}\hline}{\endtabularx\par}

% ---------------------------------------------------------------- note box
\RequirePackage[most]{tcolorbox}
\newtcolorbox{planbox}[1][]{enhanced,sharp corners,colback=p4aNote,colframe=black,
  boxrule=0.5pt,left=3pt,right=3pt,top=2pt,bottom=2pt,fontupper=\color{p4aText},#1}

% ---------------------------------------------------------------- project name
\newcommand{\PlanARI}{{\plan@headfont\bfseries\color{p4aProject}Plan4ARI}\xspace}
\RequirePackage{xspace}

% ---------------------------------------------------------------- links
\RequirePackage{graphicx}
\RequirePackage{flafter}% floats never appear before their reference point (e.g. above a section title)
\RequirePackage[hidelinks]{hyperref}
\hypersetup{colorlinks=true,linkcolor=p4aHeading,citecolor=p4aHeading,urlcolor=p4aAccent}

% ---------------------------------------------------------------- footer
\RequirePackage{fancyhdr}
\fancypagestyle{plain}{\fancyhf{}\renewcommand{\headrulewidth}{0pt}%
  \ifplan@pagenumbers\fancyfoot[R]{\plan@headfont\footnotesize\color{p4aAccent}\@planfootleft\quad\thepage}\fi}
\pagestyle{plain}
\newcommand{\@planfootleft}{\PlanARI\ \plan@deliverable}

% ---------------------------------------------------------------- metadata
\newcommand{\plan@deliverable}{D?.?}
\newcommand{\plan@doctitle}{Title}
\newcommand{\plan@status}{DRAFT}
\newcommand{\plan@subtitle}{Planning for Artificial Robotic Intelligence and Beyond}
\newcommand{\deliverable}[1]{\renewcommand{\plan@deliverable}{#1}}
\newcommand{\deliverabletitle}[1]{\renewcommand{\plan@doctitle}{#1}}
\newcommand{\docstatusline}[1]{\renewcommand{\plan@status}{#1}}
\newcommand{\projectsubtitle}[1]{\renewcommand{\plan@subtitle}{#1}}
% info table rows: \inforow{Project acronym}{Plan4ARI}
\newcommand{\plan@inforows}{}
\newcommand{\inforow}[2]{\g@addto@macro\plan@inforows{\cellcolor{p4aKeyCell}#1 & #2\\}}

% ---------------------------------------------------------------- cover
\newcommand{\makecover}{%
  \thispagestyle{empty}%
  \begin{center}
    {\plan@headfont\normalsize PLAN4ARI}\par\vspace{2pt}
    {\plan@headfont\fontsize{25}{30}\selectfont\bfseries\color{p4aHeading}%
      Deliverable \plan@deliverable\\[2pt]\plan@doctitle\par}%
    \vspace{4pt}{\color{p4aAccent}\rule{\linewidth}{0.8pt}}\par\vspace{2pt}
    {\small \MakeUppercase{\plan@status}\\ \plan@subtitle\par}
  \end{center}
  \vspace{8pt}
  \begingroup\small\renewcommand{\arraystretch}{1.7}\arrayrulecolor{white}%
  \rowcolors{1}{white}{p4aRowAlt}%
  \noindent\hspace*{0.03\linewidth}%
  \begin{tabularx}{0.94\linewidth}{@{\hspace{6pt}}>{\raggedright\arraybackslash}p{0.27\linewidth}@{\hspace{12pt}}Y@{\hspace{6pt}}}
    \plan@inforows
  \end{tabularx}\par\endgroup
  \clearpage}

% ---------------------------------------------------------------- document control
% \begin{documentcontrol} \docversion{0.1}{4 April 2026}{N. Pedrocchi}{Initial draft} \end{documentcontrol}
\newcommand{\docversion}[4]{#1 & #2 & #3 & #4\\}
\newenvironment{documentcontrol}{%
  \plan@origsection*{Document control}%
  \begingroup\small\arrayrulecolor{white}\rowcolors{2}{white}{p4aRowAlt}%
  \noindent\tabularx{\linewidth}{@{\hspace{6pt}}L{0.12\linewidth}L{0.18\linewidth}L{0.25\linewidth}Y}
  \rowcolor{p4aHeading}\thead{Version} & \thead{Date} & \thead{Author/reviewer} & \thead{Change description}\\}%
  {\endtabularx\endgroup\clearpage}

\endinput
