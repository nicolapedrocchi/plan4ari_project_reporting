---
key: parwana2025brmppi
title: "BR-MPPI: Barrier-Rate Guided MPPI for Enforcing Multiple Inequality Constraints with Learned Signed Distance Fields"
authors: "Parwana, Hardik; Kim, Taekyung; Long, Kehan; Hoxha, Bardh; Okamoto, Hideki; Fainekos, Georgios; Panagou, Dimitra"
year: 2025
venue: "arXiv preprint arXiv:2506.07325"
arxiv: 2506.07325
doi: 
pdf: raw/papers/parwana2025brmppi.pdf
text: raw/text/parwana2025brmppi.txt
tags: [safety, cbf]
status: summarised
---

# BR-MPPI: Barrier-Rate Guided MPPI for Enforcing Multiple Inequality Constraints with Learned Signed Distance Fields

*Parwana, Hardik; Kim, Taekyung; Long, Kehan; Hoxha, Bardh; Okamoto, Hideki; Fainekos, Georgios; Panagou, Dimitra* (2025). arXiv preprint arXiv:2506.07325.

## TL;DR
BR-MPPI: CBF condition as equality with learnable class-K parameter treated as extra input; samples projected onto constraint manifold.

## Method
Barrier-rate augmentation, projection of sampled controls.

## Evidence
Simulations with learned SDFs, hardware.

## Relevance for Plan4ARI
Multiple constraints with learned distance fields.

## Abstract (verbatim, arXiv)
> Model Predictive Path Integral (MPPI) control provides a sampling-based framework for optimal control, while Control Barrier Functions (CBFs) provide a principled means of enforcing safety constraints. We introduce BR-MPPI, which integrates CBF-like conditions into MPPI's control sampling procedure. CBFs impose inequality constraints that bound the rate of change of barrier functions using a class-K function of the barrier value. We instead impose the CBF condition as an equality constraint using a parametric linear class-K function and augment the system state with its parameter. The parameter's time derivative serves as an additional control input optimized by MPPI. We further design a cost function that promotes parameter values consistent with Nagumo's condition at the safe-set boundary, thereby encouraging safety. The resulting multiple state- and control-dependent equality constraints pose a challenge for random control sampling. We address this through state transformations and control projections inspired by manifold path planning that map sampled controls onto the constraint manifold. We also incorporate learned signed distance fields to represent robot geometry and reduce computation time. Simulations demonstrate improved sample efficiency over vanilla MPPI and higher navigation success rates across five robot models compared with safety-oriented MPPI variants. Hardware experiments on a quadrotor further demonstrate the method's ability to navigate constrained environments near safe-set boundaries.

## Links
- [[concepts/constraints-and-safety]]
- BibTeX key: `parwana2025brmppi` in `latex/references.bib`
