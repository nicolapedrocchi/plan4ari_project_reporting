---
key: williams2018tro
title: "Information-Theoretic Model Predictive Control: Theory and Applications to Autonomous Driving"
authors: "Williams, Grady; Drews, Paul; Goldfain, Brian; Rehg, James M.; Theodorou, Evangelos A."
year: 2018
venue: "IEEE Transactions on Robotics, vol. 34, no. 6, pp. 1603-1622"
arxiv: 1707.02342
doi: 10.1109/TRO.2018.2865891
pdf: none
text: none
tags: [foundations, mppi-core, mobile]
status: summarised
---

# Information-Theoretic Model Predictive Control: Theory and Applications to Autonomous Driving

*Williams, Grady; Drews, Paul; Goldfain, Brian; Rehg, James M.; Theodorou, Evangelos A.* (2018). IEEE Transactions on Robotics, vol. 34, no. 6, pp. 1603-1622.

## TL;DR
T-RO consolidation of information-theoretic MPC: theory, the gamma = lambda(1-alpha) control-cost trade-off and extensive autonomous driving results.

## Method
Free energy and relative entropy duality; importance sampling update; learned dynamics; costmap.

## Evidence
AutoRally at high speed, simulations.

## Relevance for Plan4ARI
Primary citation for the MPPI update equation in the SOTA (Eq. 3).

## Abstract (verbatim, arXiv)
> We present an information theoretic approach to stochastic optimal control problems that can be used to derive general sampling based optimization schemes. This new mathematical method is used to develop a sampling based model predictive control algorithm. We apply this information theoretic model predictive control (IT-MPC) scheme to the task of aggressive autonomous driving around a dirt test track, and compare its performance to a model predictive control version of the cross-entropy method.

## Links
- [[concepts/information-theoretic-mppi]]
- [[applications/mobile-robots-amr]]
- BibTeX key: `williams2018tro` in `latex/references.bib`
