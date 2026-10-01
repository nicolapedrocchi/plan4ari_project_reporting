---
key: okada2020vimpc
title: "Variational Inference MPC for Bayesian Model-based Reinforcement Learning"
authors: "Okada, Masashi; Taniguchi, Tadahiro"
year: 2020
venue: "Proc. Conf. Robot Learning (CoRL), PMLR vol. 100"
arxiv: 1907.04202
doi: 
pdf: raw/papers/okada2020vimpc.pdf
text: raw/text/okada2020vimpc.txt
tags: [variational, learning]
status: summarised
---

# Variational Inference MPC for Bayesian Model-based Reinforcement Learning

*Okada, Masashi; Taniguchi, Tadahiro* (2020). Proc. Conf. Robot Learning (CoRL), PMLR vol. 100.

## TL;DR
Variational-inference MPC: MPPI/CEM as inference; mixture proposal for multimodality with Bayesian learned models.

## Method
VI-MPC with Gaussian mixtures.

## Evidence
Simulated tasks.

## Relevance for Plan4ARI
Inference view of MPPI; mixture proposals.

## Abstract (verbatim, arXiv)
> In recent studies on model-based reinforcement learning (MBRL), incorporating uncertainty in forward dynamics is a state-of-the-art strategy to enhance learning performance, making MBRLs competitive to cutting-edge model free methods, especially in simulated robotics tasks. Probabilistic ensembles with trajectory sampling (PETS) is a leading type of MBRL, which employs Bayesian inference to dynamics modeling and model predictive control (MPC) with stochastic optimization via the cross entropy method (CEM). In this paper, we propose a novel extension to the uncertainty-aware MBRL. Our main contributions are twofold: Firstly, we introduce a variational inference MPC, which reformulates various stochastic methods, including CEM, in a Bayesian fashion. Secondly, we propose a novel instance of the framework, called probabilistic action ensembles with trajectory sampling (PaETS). As a result, our Bayesian MBRL can involve multimodal uncertainties both in dynamics and optimal trajectories. In comparison to PETS, our method consistently improves asymptotic performance on several challenging locomotion tasks.

## Links
- [[concepts/multimodality]]
- [[concepts/learning-augmented-mppi]]
- BibTeX key: `okada2020vimpc` in `latex/references.bib`
