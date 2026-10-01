---
key: wang2021tsallis
title: "Variational Inference MPC using Tsallis Divergence"
authors: "Wang, Ziyi; So, Oswin; Gibson, Jason; Vlahov, Bogdan; Gandhi, Manan S.; Liu, Guan-Horng; Theodorou, Evangelos A."
year: 2021
venue: "Proc. Robotics: Science and Systems (RSS) XVII"
arxiv: 2104.00241
doi: 10.15607/RSS.2021.XVII.073
pdf: raw/papers/wang2021tsallis.pdf
text: raw/text/wang2021tsallis.txt
tags: [variational]
status: summarised
---

# Variational Inference MPC using Tsallis Divergence

*Wang, Ziyi; So, Oswin; Gibson, Jason; Vlahov, Bogdan; Gandhi, Manan S.; Liu, Guan-Horng; Theodorou, Evangelos A.* (2021). Proc. Robotics: Science and Systems (RSS) XVII.

## TL;DR
Generalises MPPI weighting with Tsallis divergence; yields a family including CEM-like thresholding and MPPI exponential weights.

## Method
Tsallis VI-MPC.

## Evidence
Simulated tasks.

## Relevance for Plan4ARI
Weighting function is a tunable design choice.

## Abstract (verbatim, arXiv)
> In this paper, we provide a generalized framework for Variational Inference-Stochastic Optimal Control by using thenon-extensive Tsallis divergence. By incorporating the deformed exponential function into the optimality likelihood function, a novel Tsallis Variational Inference-Model Predictive Control algorithm is derived, which includes prior works such as Variational Inference-Model Predictive Control, Model Predictive PathIntegral Control, Cross Entropy Method, and Stein VariationalInference Model Predictive Control as special cases. The proposed algorithm allows for effective control of the cost/reward transform and is characterized by superior performance in terms of mean and variance reduction of the associated cost. The aforementioned features are supported by a theoretical and numerical analysis on the level of risk sensitivity of the proposed algorithm as well as simulation experiments on 5 different robotic systems with 3 different policy parameterizations.

## Links
- [[concepts/information-theoretic-mppi]]
- [[concepts/sampling-distributions]]
- BibTeX key: `wang2021tsallis` in `latex/references.bib`
