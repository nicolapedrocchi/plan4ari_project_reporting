---
key: wagener2019dmd
title: "An Online Learning Approach to Model Predictive Control"
authors: "Wagener, Nolan; Cheng, Ching-An; Sacks, Jacob; Boots, Byron"
year: 2019
venue: "Proc. Robotics: Science and Systems (RSS) XV"
arxiv: 1902.08967
doi: 
pdf: raw/papers/wagener2019dmd.pdf
text: raw/text/wagener2019dmd.txt
tags: [theory]
status: summarised
---

# An Online Learning Approach to Model Predictive Control

*Wagener, Nolan; Cheng, Ching-An; Sacks, Jacob; Boots, Byron* (2019). Proc. Robotics: Science and Systems (RSS) XV.

## TL;DR
Casts MPC as online learning; shows MPPI and CEM are instances of dynamic mirror descent (DMD-MPC) and derives new variants.

## Method
Online learning / mirror descent framework for sampling-based MPC.

## Evidence
Simulated cart-pole and AutoRally.

## Relevance for Plan4ARI
Theoretical link between MPPI, CEM and gradient-like updates; useful to justify step-size (alpha_u) choices.

## Abstract (verbatim, arXiv)
> Model predictive control (MPC) is a powerful technique for solving dynamic control tasks. In this paper, we show that there exists a close connection between MPC and online learning, an abstract theoretical framework for analyzing online decision making in the optimization literature. This new perspective provides a foundation for leveraging powerful online learning algorithms to design MPC algorithms. Specifically, we propose a new algorithm based on dynamic mirror descent (DMD), an online learning algorithm that is designed for non-stationary setups. Our algorithm, Dynamic Mirror Descent Model Predictive Control (DMD-MPC), represents a general family of MPC algorithms that includes many existing techniques as special instances. DMD-MPC also provides a fresh perspective on previous heuristics used in MPC and suggests a principled way to design new MPC algorithms. In the experimental section of this paper, we demonstrate the flexibility of DMD-MPC, presenting a set of new MPC algorithms on a simple simulated cartpole and a simulated and real-world aggressive driving task. Videos of the real-world experiments can be found at https://youtu.be/vZST3v0_S9w and https://youtu.be/MhuqiHo2t98.

## Links
- [[concepts/mppi-vs-mpc]]
- [[concepts/information-theoretic-mppi]]
- BibTeX key: `wagener2019dmd` in `latex/references.bib`
