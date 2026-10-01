---
key: streichenberg2023mapi
title: "Multi-Agent Path Integral Control for Interaction-Aware Motion Planning in Urban Canals"
authors: "Streichenberg, Lucas; Trevisan, Elia; Chung, Jen Jen; Siegwart, Roland; Alonso-Mora, Javier"
year: 2023
venue: "Proc. IEEE Int. Conf. Robotics and Automation (ICRA), pp. 1379-1385"
arxiv: 2302.06547
doi: 10.1109/ICRA48891.2023.10161511
pdf: raw/papers/streichenberg2023mapi.pdf
text: raw/text/streichenberg2023mapi.txt
tags: [mobile, multi-agent]
status: summarised
---

# Multi-Agent Path Integral Control for Interaction-Aware Motion Planning in Urban Canals

*Streichenberg, Lucas; Trevisan, Elia; Chung, Jen Jen; Siegwart, Roland; Alonso-Mora, Javier* (2023). Proc. IEEE Int. Conf. Robotics and Automation (ICRA), pp. 1379-1385.

## TL;DR
Multi-agent path-integral control for interaction-aware planning of autonomous vessels in urban canals.

## Method
Joint sampling over agents, cooperative cost.

## Evidence
Simulation.

## Relevance for Plan4ARI
Multi-agent MPPI template for AMR fleets.

## Abstract (verbatim, arXiv)
> Autonomous vehicles that operate in urban environments shall comply with existing rules and reason about the interactions with other decision-making agents. In this paper, we introduce a decentralized and communication-free interaction-aware motion planner and apply it to Autonomous Surface Vessels (ASVs) in urban canals. We build upon a sampling-based method, namely Model Predictive Path Integral control (MPPI), and employ it to, in each time instance, compute both a collision-free trajectory for the vehicle and a prediction of other agents' trajectories, thus modeling interactions. To improve the method's efficiency in multi-agent scenarios, we introduce a two-stage sample evaluation strategy and define an appropriate cost function to achieve rule compliance. We evaluate this decentralized approach in simulations with multiple vessels in real scenarios extracted from Amsterdam's canals, showing superior performance than a state-of-the-art trajectory optimization framework and robustness when encountering different types of agents.

## Links
- [[applications/mobile-robots-amr]]
- BibTeX key: `streichenberg2023mapi` in `latex/references.bib`
