---
key: lambert2020svmpc
title: "Stein Variational Model Predictive Control"
authors: "Lambert, Alexander; Fishman, Adam; Fox, Dieter; Boots, Byron; Ramos, Fabio"
year: 2020
venue: "Proc. Conf. Robot Learning (CoRL), PMLR vol. 155"
arxiv: 2011.07641
doi: 
pdf: raw/papers/lambert2020svmpc.pdf
text: raw/text/lambert2020svmpc.txt
tags: [multimodal, variational]
status: summarised
---

# Stein Variational Model Predictive Control

*Lambert, Alexander; Fishman, Adam; Fox, Dieter; Boots, Byron; Ramos, Fabio* (2020). Proc. Conf. Robot Learning (CoRL), PMLR vol. 155.

## TL;DR
Stein Variational MPC: non-parametric particle approximation of the posterior over control sequences via SVGD, capturing multiple modes.

## Method
SVGD on a mixture of Gaussians over control sequences.

## Evidence
Simulated navigation, manipulation, real car.

## Relevance for Plan4ARI
Principled multimodality; heavier than MPPI.

## Abstract (verbatim, arXiv)
> Decision making under uncertainty is critical to real-world, autonomous systems. Model Predictive Control (MPC) methods have demonstrated favorable performance in practice, but remain limited when dealing with complex probability distributions. In this paper, we propose a generalization of MPC that represents a multitude of solutions as posterior distributions. By casting MPC as a Bayesian inference problem, we employ variational methods for posterior computation, naturally encoding the complexity and multi-modality of the decision making problem. We present a Stein variational gradient descent method to estimate the posterior directly over control parameters, given a cost function and observed state trajectories. We show that this framework leads to successful planning in challenging, non-convex optimal control problems.

## Links
- [[concepts/multimodality]]
- [[concepts/sampling-distributions]]
- BibTeX key: `lambert2020svmpc` in `latex/references.bib`
