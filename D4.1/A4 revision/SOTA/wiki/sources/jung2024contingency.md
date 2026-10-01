---
key: jung2024contingency
title: "Contingency Constrained Planning with MPPI within MPPI"
authors: "Jung, Leonard; Estornell, Alexander; Everett, Michael"
year: 2024
venue: "arXiv preprint arXiv:2412.09777"
arxiv: 2412.09777
doi: 
pdf: raw/papers/jung2024contingency.pdf
text: raw/text/jung2024contingency.txt
tags: [mobile, safety]
status: summarised
---

# Contingency Constrained Planning with MPPI within MPPI

*Jung, Leonard; Estornell, Alexander; Everett, Michael* (2024). arXiv preprint arXiv:2412.09777.

## TL;DR
Contingency-MPPI: nested MPPI ensures a contingency (fallback) plan always exists; adaptive importance sampling and warm-start from a light planner.

## Method
MPPI within MPPI.

## Evidence
Sim and hardware mobile robot.

## Relevance for Plan4ARI
Fallback strategies required by D4.1 Sect. 5.

## Abstract (verbatim, arXiv)
> For safety, autonomous systems must be able to consider sudden changes and enact contingency plans appropriately. State-of-the-art methods currently find trajectories that balance between nominal and contingency behavior, or plan for a singular contingency plan; however, this does not guarantee that the resulting plan is safe for all time. To address this research gap, this paper presents Contingency-MPPI, a data-driven optimization-based strategy that embeds contingency planning inside a nominal planner. By learning to approximate the optimal contingency-constrained control sequence with adaptive importance sampling, the proposed method's sampling efficiency is further improved with initializations from a lightweight path planner and trajectory optimizer. Finally, we present simulated and hardware experiments demonstrating our algorithm generating nominal and contingency plans in real time on a mobile robot.

## Links
- [[concepts/constraints-and-safety]]
- [[applications/mobile-robots-amr]]
- BibTeX key: `jung2024contingency` in `latex/references.bib`
