# Log

Append-only, newest at the bottom. One entry per operation: `## [YYYY-MM-DD] <op> | <subject>` followed by 1–5 bullets.
Ops: `ingest`, `query`, `lint`, `synthesis`, `latex`.

## [2026-10-01] ingest | initial corpus (52 PDFs, 69 bib entries)
- Seeded from Zhang et al. 2024 (M3P2I, IEEE RA-L version supplied by the user) and an arXiv/Crossref search on MPPI for manipulators, AMRs, safety, multimodality (searches run on 2026-10-01, sorted by date to include 2025–2026 work).
- Downloaded 50 arXiv PDFs + JMLR (PI²) + RSS 2018 (Tube-MPPI); text extracted with pdftotext to `raw/text/`.
- Metadata in `raw/meta/arxiv_metadata.json`; published venues verified on Crossref (`raw/meta/crossref_matches.json`).
- Created 69 source pages (`tools/new_source.py --all`, notes from `tools/source_notes.py`), 11 concept pages, 4 application pages, 1 tool page, 2 comparison pages, overview.

## [2026-10-01] latex | SOTA note v0.1
- `latex/main.tex` + `latex/references.bib` written from the wiki; 5 pages + references; compiled with latexmk (MiKTeX), no undefined citations.

## [2026-10-01] lint | first pass
- See output of `python tools/lint_wiki.py` (0 errors expected; warnings for classical refs without PDF are accepted).

## [2026-10-01] schema | project documents (.docx/.pdf)
- New page type `wiki/project/prj-*.md`, raw folder `raw/project/`, tool `tools/add_project_doc.py`, skill `wiki-ingest-project`; lint and index extended (project docs never in bib nor `\cite`d).

## [2026-10-01] ingest-project | prj-d41-outline — D4.1 outline v0.1
- 14 requirements (R1–R14) mapped to wiki pages; gap analysis updated.
- Tension flagged: outline §10 wants OMPL baseline and GPU planners reported separately vs GPU-centric MPPI layer.

## [2026-10-01] ingest-project | prj-plan4ari-proposal — Plan4ARI Project Description (FISA Allegato A)
- Found in raw/papers (dropped by the user), copied to raw/project/; read §A.2.2, §A.4, §E.3 Activity 4.
- 13 requirements/KPIs (P1–P13) mapped; gap analysis updated.
- Tension confirmed at source: KPI §A.4.4.1 excludes GPU planners from the OMPL comparison.
- 4 cited papers proposed for ingestion (Faroni 2022 RA-L, Power & Berenson 2024 T-RO, Palleschi 2021 RA-L, Laha 2023 ICRA).

## [2026-10-01] cleanup | removed misplaced raw/papers/FISA_2024_00099_Allegato A.pdf
- Deleted on user request; identical copy kept as raw/project/prj-plan4ari-proposal.pdf (verified byte-for-byte).

## [2026-10-01] ingest | faroni2022safetyaware — Safety-aware time-optimal motion planning (RA-L 2022)
- arXiv 2210.11655; bib verified on Crossref (10.1109/LRA.2022.3211493); status: read.
- Updated: applications/human-robot-shared-spaces, concepts/constraints-and-safety, comparisons/plan4ari-gap-analysis, project/prj-plan4ari-proposal.
- Key point: the ISO/TS 15066 time-dilation cost λ(q,H) is a natural MPPI rollout cost.
- Pending (not on arXiv, user to download from IEEE Xplore): power2024generalizable (10.1109/TRO.2024.3370026), palleschi2021fastsafe (10.1109/LRA.2021.3076968), laha2023sstar (10.1109/ICRA48891.2023.10161248).

## [2026-10-01] ingest | power2024generalizable — Learned generalizable trajectory sampling distribution for MPC (T-RO 2024)
- IEEE PDF provided by the user (renamed from the Xplore file name); status: read.
- Updated: concepts/sampling-distributions, concepts/learning-augmented-mppi, concepts/multimodality, comparisons/mppi-variants-matrix, project/prj-plan4ari-proposal.
- Confirmed citation mismatch of proposal ref. 10 (paper is about learned sampling for collision-free navigation, not aerial coverage).

## [2026-10-01] ingest | palleschi2021fastsafe — Fast and safe trajectory planning, cobot performance/safety trade-off (RA-L 2021)
- IEEE PDF provided by the user; status: read.
- Updated: applications/human-robot-shared-spaces, concepts/constraints-and-safety, concepts/hybrid-gradient-sampling, comparisons/plan4ari-gap-analysis.
- Template for a certified downstream layer: convex jerk-limited PFL-aware re-timing at 25–40 Hz.

## [2026-10-01] ingest | laha2023sstar — S*: safe and time-efficient motion planning (ICRA 2023)
- IEEE PDF provided by the user; status: read.
- Updated: applications/human-robot-shared-spaces, concepts/constraints-and-safety.
- Same "minimise time including safety limits" principle as faroni2022safetyaware, PFL instead of SSM; offline, static human.

## [2026-10-01] ingest | thomason2024vamp — VAMP, vectorized sampling-based planning (ICRA 2024)
- arXiv 2309.14545; Crossref verified; status: summarised. Updated tools/software-ecosystem.

## [2026-10-01] synthesis | welding-mppi-design-review
- Filed back the critical review of the multi-goal MPPI look-ahead for AGV-mounted welding, with the PI's refinements (8 IK-branch goals, 10 cm horizon, ±10% speed, VAMP for transfers, optional downstream MPC).
- Linked from comparisons/plan4ari-gap-analysis.

## [2026-10-01] query | literature search redundancy resolution along welding paths, base placement, mobile welding
- Queries (arXiv): welding+redundancy; Cartesian path+tolerances; redundancy resolution+path+global; orientation tolerance; tool path+kinematic redundancy; base placement (+welding/mobile manipulator/coverage); welding+mobile manipulator; functional redundancy+manufacturing; reconfiguration+prescribed path; MPPI+path following+manipulator; seam welding planning.
- ~30 hits, 8 proposed to the PI (awaiting confirmation). No MPPI work for path-constrained redundancy resolution found on arXiv.
- Design page updated with PI answers (6-axis + optional linear 7th axis, ±10% constant, VAMP two-pass scheme).

## [2026-10-01] ingest | 8 sources on path-wise redundancy resolution and base placement
- yin2024dpbreakpoints, yin2024dprealtime, razjigaev2025functional, zhong2024expansiongrr (IROS 2024), gautier2024weldingbase (ASME IDETC 2024), zhang2023basecoverage, nguyen2023taskclustering (ICRA 2023), makhal2018reuleaux (IRC 2018; key renamed from makhal2017reuleaux to match the published year).
- Pages read and written by 4 parallel sub-agents (2 papers each); numbers spot-checked against raw text by the coordinator.
- New concept pages: concepts/path-wise-redundancy-resolution, concepts/base-placement.
- Updated: comparisons/welding-mppi-design-review (literature check + novelty assessment), applications/industrial-manipulators, applications/mobile-robots-amr, overview.
- Key finding: closest prior art = breakpoint-minimising DP (single IK branch, no transfer planning, no timings); station-placement works are point-based, none checks seam continuity at constant speed.

## [2026-10-01] query | literature search Elsevier + Descartes (welding redundancy, mobile welding, base placement, multi-robot welding)
- Crossref restricted to Elsevier (member 78), 9 queries; web search for Descartes (ROS-Industrial) and its evaluation papers.
- Descartes: no journal paper; ROS-Industrial package (Apache-2.0, ROS Melodic branch) + ROSCon 2015 slides; evaluation by De Maeyer et al. (ETFA 2017) and follow-up benchmark (Procedia CIRP).
- 15 non-downloadable candidates listed for manual download by the PI (Elsevier blocks automated download even for CC-licensed articles); 3 arXiv candidates proposed (Cuspidal 6R path planning, RangedIK, anytime EE trajectory tracking).

## [2026-10-01] query | literature search IEEE (Crossref member 263) — methodology
- 13 queries: MPPI+MPC hierarchical/cascade, sampling-based MPC path following with null space, MPPI redundancy, look-ahead/online trajectory generation, reconfiguration/IK switching, base placement for continuous paths, functional redundancy/tool axis, contouring control, external axis, posture change in welding, MPPI collision avoidance for arms, path-velocity decomposition.
- 20 candidates screened: 6 with arXiv version (ingestable), 14 for manual download (IEEE/TechRxiv). Awaiting PI confirmation.

## [2026-10-01] ingest | 35 sources: Elsevier/IEEE/TechRxiv/SSRN (PDFs from the PI's academic account) + 9 arXiv
- Elsevier/IEEE PDFs renamed from publisher file names to bibkeys; text extracted (sun2020externalaxis text garbled -> page written from PDF images).
- BibTeX generated from Crossref with new tool `tools/bib_from_doi.py`.
- Pages written by 8 parallel sub-agents (4-5 papers each); coordinator spot-checked numbers.
- New page: applications/robotic-welding. Updated: concepts/path-wise-redundancy-resolution, concepts/base-placement, concepts/hybrid-gradient-sampling, concepts/mppi-vs-mpc, concepts/constraints-and-safety, applications/industrial-manipulators, comparisons/mppi-variants-matrix, comparisons/welding-mppi-design-review (literature check round 2 + updated novelty), overview.
- Key findings: cuspidal offset-wrist cobots break the "8 branches = reconfiguration" assumption; null-space projected MPPI exists as preprint (wang2024constrainedpi) -> claim the combination, not null-space MPPI alone; mobile-platform accuracy (~40 mm) makes seam registration mandatory.
- Not ingested (no access): Li 2024 Precision Eng., Lee & Han 2025 ASCE, Ye 2026 IJRR. Two .tmp partial downloads left in raw/papers.

## [2026-10-01] ingest | li2024weldredundant (Precision Eng. 2024), ye2026nullspacemultirobot (IJRR 2026)
- PDFs supplied by the PI (Elsevier, SAGE); renamed, text extracted, bib from Crossref; pages by 2 sub-agents (first run interrupted by usage limit, re-run).
- Li 2024: offline FSW path smoothing with fixed tool axis + 1-DoF table; weak redundancy baseline.
- Ye 2026: offline exact-path null-space descent for coupled multi-robot systems with joint placement; deterministic baseline for tightly coupled pairs.
- Updated: applications/robotic-welding, concepts/path-wise-redundancy-resolution, comparisons/welding-mppi-design-review (novelty unchanged).
- Duplicate of zhang2024m3p2i.pdf found in raw/papers (publisher file name); left in place pending PI decision.

## [2026-10-01] cleanup | removed duplicate publisher-named copy of zhang2024m3p2i.pdf (PI request, verified identical)

## [2026-10-01] latex | updated scientific plan draft v0.1 (../scientific-plan/plan_update.tex)
- PI decisions: robot-agnostic framework; keep sampling-based planning and ADD MPPI look-ahead; explicit pipeline starting from optimal task localisation after segmentation; Open IPC / Core IPC allocation; T4.7 application catalogue (welding on hardware, all others in simulation); GitHub benchmark repository deferred to a later step.
- 8 pages, cites 42 wiki sources via the shared bib (../SOTA/latex/references.bib); compiled without undefined citations.

## [2026-10-01] latex | Plan4ARI LaTeX class + D4.1 deliverable v0.2
- New class `Project Reporting/latex-style/plan4ari.cls` reproducing the D1.1 Word layout (Cambria/Calibri, colours, cover, document control, grid tables, note box, captions); README with mapping.
- SOTA note refactored: body in `latex/sota_body.tex`, macros in `latex/sota_macros.tex` (standalone note unchanged, 9 pages).
- D4.1 assembled in `../D4.1-latex/` (12 sections per the outline, 29 pages, XeLaTeX): sections 2, 8-11 from the plan draft, section 6 inputs the SOTA body, bibliography shared. `../scientific-plan/plan_update.tex` is superseded by the D4.1.
- sota-latex skill updated with the shared-file rule.
