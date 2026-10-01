---
key: williams2015covariance
title: "Model Predictive Path Integral Control using Covariance Variable Importance Sampling"
authors: "Williams, Grady; Aldrich, Andrew; Theodorou, Evangelos"
year: 2015
venue: "arXiv preprint arXiv:1509.01149"
arxiv: 1509.01149
doi: 
pdf: raw/papers/williams2015covariance.pdf
text: raw/text/williams2015covariance.txt
tags: [foundations, mppi-core]
status: summarised
---

# Model Predictive Path Integral Control using Covariance Variable Importance Sampling

*Williams, Grady; Aldrich, Andrew; Theodorou, Evangelos* (2015). arXiv preprint arXiv:1509.01149.

## TL;DR
First MPPI formulation with covariance variable importance sampling: allows changing the sampling covariance independently of the control cost.

## Method
Importance sampling with a modified covariance in the path-integral expectation; GPU implementation.

## Evidence
Simulated cart-pole, quadrotor, race car.

## Relevance for Plan4ARI
Introduces the importance-sampling view that every later variant (Biased-MPPI, MPOPI) builds on.

## Abstract (verbatim, arXiv)
> In this paper we develop a Model Predictive Path Integral (MPPI) control algorithm based on a generalized importance sampling scheme and perform parallel optimization via sampling using a Graphics Processing Unit (GPU). The proposed generalized importance sampling scheme allows for changes in the drift and diffusion terms of stochastic diffusion processes and plays a significant role in the performance of the model predictive control algorithm. We compare the proposed algorithm in simulation with a model predictive control version of differential dynamic programming.

## Links
- [[concepts/information-theoretic-mppi]]
- [[concepts/sampling-distributions]]
- BibTeX key: `williams2015covariance` in `latex/references.bib`
