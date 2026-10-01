---
key: trevisan2024biasedmppi
title: "Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers"
authors: "Trevisan, Elia; Alonso-Mora, Javier"
year: 2024
venue: "IEEE Robotics and Automation Letters, vol. 9, no. 6, pp. 5871-5878"
arxiv: 2401.09241
doi: 10.1109/LRA.2024.3397083
pdf: raw/papers/trevisan2024biasedmppi.pdf
text: raw/text/trevisan2024biasedmppi.txt
tags: [sampling, mobile, guidance]
status: summarised
---

# Biased-MPPI: Informing Sampling-Based Model Predictive Control by Fusing Ancillary Controllers

*Trevisan, Elia; Alonso-Mora, Javier* (2024). IEEE Robotics and Automation Letters, vol. 9, no. 6, pp. 5871-5878.

## TL;DR
Biased-MPPI: derivation of MPPI for arbitrary sampling distributions; mixes samples from ancillary controllers (classical, learned) for informative sampling.

## Method
Importance sampling with arbitrary proposals, control fusion.

## Evidence
Simulated and real (mobile robots, driving).

## Relevance for Plan4ARI
Mechanism to inject Open-IPC global paths as proposals.

## Abstract (verbatim, arXiv)
> Motion planning for autonomous robots in dynamic environments poses numerous challenges due to uncertainties in the robot's dynamics and interaction with other agents. Sampling-based MPC approaches, such as Model Predictive Path Integral (MPPI) control, have shown promise in addressing these complex motion planning problems. However, the performance of MPPI relies heavily on the choice of sampling distribution. Existing literature often uses the previously computed input sequence as the mean of a Gaussian distribution for sampling, leading to potential failures and local minima. In this paper, we propose a novel derivation of MPPI that allows for arbitrary sampling distributions to enhance efficiency, robustness, and convergence while alleviating the problem of local minima. We present an efficient importance sampling scheme that combines classical and learning-based ancillary controllers simultaneously, resulting in more informative sampling and control fusion. Several simulated and real-world demonstrate the validity of our approach.

## Links
- [[concepts/sampling-distributions]]
- [[concepts/hybrid-gradient-sampling]]
- [[comparisons/plan4ari-gap-analysis]]
- BibTeX key: `trevisan2024biasedmppi` in `latex/references.bib`
