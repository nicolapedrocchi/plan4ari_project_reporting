---
key: gandhi2023safeis
title: "Safe Importance Sampling in Model Predictive Path Integral Control"
authors: "Gandhi, Manan; Almubarak, Hassan; Theodorou, Evangelos"
year: 2023
venue: "arXiv preprint arXiv:2303.03441"
arxiv: 2303.03441
doi: 
pdf: raw/papers/gandhi2023safeis.pdf
text: raw/text/gandhi2023safeis.txt
tags: [safety, cbf]
status: summarised
---

# Safe Importance Sampling in Model Predictive Path Integral Control

*Gandhi, Manan; Almubarak, Hassan; Theodorou, Evangelos* (2023). arXiv preprint arXiv:2303.03441.

## TL;DR
SC-MPPI: embeds a barrier-state safety controller in forward sampling so rollouts stay safe, increasing sample efficiency.

## Method
Barrier states inside rollouts; information-theoretic derivation.

## Evidence
Simulated navigation.

## Relevance for Plan4ARI
Safety inside sampling rather than after.

## Abstract (verbatim, arXiv)
> We introduce the notion of importance sampling under embedded barrier state control, titled Safety Controlled Model Predictive Path Integral Control (SC-MPPI). For robotic systems operating in an environment with multiple constraints, hard constraints are often encoded utilizing penalty functions when performing optimization. Alternative schemes utilizing optimization-based techniques, such as Control Barrier Functions, can be used as a safety filter to ensure the system does not violate the given hard constraints. In contrast, this work leverages the principle of a safety filter but applies it during forward sampling for Model Predictive Path Integral Control. The resulting set of forward samples can remain safe within the domain of the safety controller, increasing sample efficiency and allowing for improved exploration of the state space. We derive this controller through information theoretic principles analogous to Information Theoretic MPPI. We empirically demonstrate both superior sample efficiency, exploration, and system performance of SC-MPPI when compared to Model-Predictive Path Integral Control (MPPI) and Differential Dynamic Programming (DDP) optimizing the barrier state.

## Links
- [[concepts/constraints-and-safety]]
- BibTeX key: `gandhi2023safeis` in `latex/references.bib`
