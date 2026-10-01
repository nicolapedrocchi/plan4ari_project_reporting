---
key: williams2018tubemppi
title: "Robust Sampling Based Model Predictive Control with Sparse Objective Information"
authors: "Williams, Grady; Goldfain, Brian; Drews, Paul; Saigol, Kamil; Rehg, James M.; Theodorou, Evangelos A."
year: 2018
venue: "Proc. Robotics: Science and Systems (RSS) XIV"
arxiv: 
doi: 10.15607/RSS.2018.XIV.042
pdf: raw/papers/williams2018tubemppi.pdf
text: raw/text/williams2018tubemppi.txt
tags: [robustness]
status: summarised
---

# Robust Sampling Based Model Predictive Control with Sparse Objective Information

*Williams, Grady; Goldfain, Brian; Drews, Paul; Saigol, Kamil; Rehg, James M.; Theodorou, Evangelos A.* (2018). Proc. Robotics: Science and Systems (RSS) XIV.

## TL;DR
Tube-MPPI: MPPI plans a nominal trajectory while an iLQG ancillary controller tracks it, robustifying against disturbances when the cost is sparse.

## Method
Nominal/actual state split; augmented importance sampling; iLQG tracking.

## Evidence
AutoRally real-world, sparse costs.

## Relevance for Plan4ARI
First "MPPI + classical controller" layering, analogous to MPPI + Core-IPC MPC in Plan4ARI.

## Links
- [[concepts/robustness-uncertainty]]
- [[concepts/hybrid-gradient-sampling]]
- BibTeX key: `williams2018tubemppi` in `latex/references.bib`
