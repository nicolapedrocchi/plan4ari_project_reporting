---
key: williams2017itmpc
title: "Information Theoretic MPC for Model-Based Reinforcement Learning"
authors: "Williams, Grady; Wagener, Nolan; Goldfain, Brian; Drews, Paul; Rehg, James M.; Boots, Byron; Theodorou, Evangelos A."
year: 2017
venue: "Proc. IEEE Int. Conf. Robotics and Automation (ICRA), pp. 1714-1721"
arxiv: 
doi: 10.1109/ICRA.2017.7989202
pdf: none
text: none
tags: [foundations, mppi-core, learning]
status: summarised
---

# Information Theoretic MPC for Model-Based Reinforcement Learning

*Williams, Grady; Wagener, Nolan; Goldfain, Brian; Drews, Paul; Rehg, James M.; Boots, Byron; Theodorou, Evangelos A.* (2017). Proc. IEEE Int. Conf. Robotics and Automation (ICRA), pp. 1714-1721.

## TL;DR
Information-theoretic derivation of MPPI in discrete time, removing control-affine assumption; used with learned neural-network dynamics (model-based RL).

## Method
Free-energy / KL bound, optimal distribution q*, KL projection onto Gaussian family; NN dynamics.

## Evidence
AutoRally real-world with learned dynamics.

## Relevance for Plan4ARI
The discrete-time form used in almost all modern implementations.

## Links
- [[concepts/information-theoretic-mppi]]
- [[concepts/learning-augmented-mppi]]
- BibTeX key: `williams2017itmpc` in `latex/references.bib`
