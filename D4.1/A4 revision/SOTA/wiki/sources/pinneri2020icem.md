---
key: pinneri2020icem
title: "Sample-efficient Cross-Entropy Method for Real-time Planning"
authors: "Pinneri, Cristina; Sawant, Shambhuraj; Blaes, Sebastian; Achterhold, Jan; Stueckler, Joerg; Rolinek, Michal; Martius, Georg"
year: 2020
venue: "Proc. Conf. Robot Learning (CoRL), PMLR vol. 155"
arxiv: 2008.06389
doi: 
pdf: raw/papers/pinneri2020icem.pdf
text: raw/text/pinneri2020icem.txt
tags: [sampling, cem]
status: summarised
---

# Sample-efficient Cross-Entropy Method for Real-time Planning

*Pinneri, Cristina; Sawant, Shambhuraj; Blaes, Sebastian; Achterhold, Jan; Stueckler, Joerg; Rolinek, Michal; Martius, Georg* (2020). Proc. Conf. Robot Learning (CoRL), PMLR vol. 155.

## TL;DR
iCEM: improved CEM for real-time planning with coloured noise, elite memory and shifting.

## Method
CEM with time-correlated (coloured) noise.

## Evidence
Simulated locomotion and manipulation.

## Relevance for Plan4ARI
Coloured noise is a cheap smoothness fix also applicable to MPPI.

## Abstract (verbatim, arXiv)
> Trajectory optimizers for model-based reinforcement learning, such as the Cross-Entropy Method (CEM), can yield compelling results even in high-dimensional control tasks and sparse-reward environments. However, their sampling inefficiency prevents them from being used for real-time planning and control. We propose an improved version of the CEM algorithm for fast planning, with novel additions including temporally-correlated actions and memory, requiring 2.7-22x less samples and yielding a performance increase of 1.2-10x in high-dimensional control problems.

## Links
- [[concepts/mppi-vs-mpc]]
- [[concepts/smoothness-action-parametrization]]
- BibTeX key: `pinneri2020icem` in `latex/references.bib`
