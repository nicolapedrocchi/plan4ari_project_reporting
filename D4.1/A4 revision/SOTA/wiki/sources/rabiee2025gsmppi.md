---
key: rabiee2025gsmppi
title: "Guaranteed-Safe MPPI Through Composite Control Barrier Functions for Efficient Sampling in Multi-Constrained Robotic Systems"
authors: "Rabiee, Pedram; Hoagg, Jesse B."
year: 2025
venue: "Proc. IEEE Conf. Decision and Control (CDC), pp. 5515-5520"
arxiv: 2410.02154
doi: 10.1109/CDC57313.2025.11312129
pdf: raw/papers/rabiee2025gsmppi.pdf
text: raw/text/rabiee2025gsmppi.txt
tags: [safety, cbf]
status: summarised
---

# Guaranteed-Safe MPPI Through Composite Control Barrier Functions for Efficient Sampling in Multi-Constrained Robotic Systems

*Rabiee, Pedram; Hoagg, Jesse B.* (2025). Proc. IEEE Conf. Decision and Control (CDC), pp. 5515-5520.

## TL;DR
GS-MPPI: composite CBF builds a single safe closed-form controller integrated into dynamics so all sampled trajectories are provably safe.

## Method
Composite CBF, safe control law inside rollouts.

## Evidence
Nonholonomic ground robot simulation.

## Relevance for Plan4ARI
Provable safety for AMRs under multiple constraints.

## Abstract (verbatim, arXiv)
> We present a new guaranteed-safe model predictive path integral (GS-MPPI) control algorithm that enhances sample efficiency in nonlinear systems with multiple safety constraints. The approach use a composite control barrier function (CBF) along with MPPI to ensure all sampled trajectories are provably safe. We first construct a single CBF constraint from multiple safety constraints with potentially differing relative degrees, using it to create a safe closed-form control law. This safe control is then integrated into the system dynamics, allowing MPPI to optimize over exclusively safe trajectories. The method not only improves computational efficiency but also addresses the myopic behavior often associated with CBFs by incorporating long-term performance considerations. We demonstrate the algorithm's effectiveness through simulations of a nonholonomic ground robot subject to position and speed constraints, showcasing safety and performance.

## Links
- [[concepts/constraints-and-safety]]
- [[applications/mobile-robots-amr]]
- BibTeX key: `rabiee2025gsmppi` in `latex/references.bib`
