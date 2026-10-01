# Shared latexmk configuration for all Project Reporting documents.
#
# Each document includes it from a small latexmkrc next to its main .tex:
#
#   $root   = '../../..';    # relative path from the document to Project Reporting
#   $engine = 'lualatex';    # optional: xelatex (default), lualatex, pdflatex
#   do "$root/latexmkrc";
#
# Settings placed after the `do` line override the ones below.

$root   //= '.';
$engine //= 'xelatex';

my %engine_modes = (pdflatex => 1, lualatex => 4, xelatex => 5);
die "latexmkrc: unknown engine '$engine' (use xelatex, lualatex or pdflatex)\n"
  unless exists $engine_modes{$engine};
$pdf_mode = $engine_modes{$engine};

# Keep auxiliary files (.aux, .log, .bbl, .toc, .xdv, ...) out of the source folder.
$aux_dir = 'build';

# Shared class and style files (plan4ari.cls, ...).
ensure_path('TEXINPUTS', "$root/latex-style//");
