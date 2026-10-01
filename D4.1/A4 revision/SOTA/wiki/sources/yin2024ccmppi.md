---
key: yin2024ccmppi
title: "Chance-Constrained Information-Theoretic Stochastic Model Predictive Control with Safety Shielding"
authors: "Yin, Ji; Tsiotras, Panagiotis; Berntorp, Karl"
year: 2024
venue: "Proc. IEEE Conf. Decision and Control (CDC), pp. 653-658"
arxiv: 2408.00494
doi: 10.1109/CDC56724.2024.10885840
pdf: raw/papers/yin2024ccmppi.pdf
text: raw/text/yin2024ccmppi.txt
tags: [safety, chance-constraints]
status: summarised
---

# Chance-Constrained Information-Theoretic Stochastic Model Predictive Control with Safety Shielding

*Yin, Ji; Tsiotras, Panagiotis; Berntorp, Karl* (2024). Proc. IEEE Conf. Decision and Control (CDC), pp. 653-658.

## TL;DR
BSS-MPPI: belief-space stochastic MPPI enforcing chance constraints with a CBF-inspired heuristic, no linearisation.

## Method
Monte-Carlo belief propagation, chance constraints.

## Evidence
Race-car simulation.

## Relevance for Plan4ARI
Probabilistic safety, relevant for uncertain human predictions.

## Abstract (verbatim, arXiv)
> This paper introduces a novel nonlinear stochastic model predictive control path integral (MPPI) method, which considers chance constraints on system states. The proposed belief-space stochastic MPPI (BSS-MPPI) applies Monte-Carlo sampling to evaluate state distributions resulting from underlying systematic disturbances, and utilizes a Control Barrier Function (CBF) inspired heuristic in belief space to fulfill the specified chance constraints. Compared to several previous stochastic predictive control methods, our approach applies to general nonlinear dynamics without requiring the computationally expensive system linearization step. Moreover, the BSS-MPPI controller can solve optimization problems without limiting the form of the objective function and chance constraints. By multi-threading the sampling process using a GPU, we can achieve fast real-time planning for time- and safety-critical tasks such as autonomous racing. Our results on a realistic race-car simulation study show significant reductions in constraint violation compared to some of the prior MPPI approaches, while being comparable in computation times.

## Links
- [[concepts/constraints-and-safety]]
- [[concepts/robustness-uncertainty]]
- BibTeX key: `yin2024ccmppi` in `latex/references.bib`
