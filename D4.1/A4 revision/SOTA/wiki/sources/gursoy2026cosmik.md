---
key: gursoy2026cosmik
title: "COSMIK-MPPI: Scaling Constrained Model Predictive Control to Collision Avoidance in Close-Proximity Dynamic Human Environments"
authors: "Gursoy, Ege; Sabbah, Maxime; Haffemayer, Arthur; Cavalcanti Santos, Joao; Crestaz, Pietro Noah; Petrik, Vladimir; Mansard, Nicolas; Bonnet, Vincent"
year: 2026
venue: "arXiv preprint arXiv:2604.10358"
arxiv: 2604.10358
doi: 
pdf: raw/papers/gursoy2026cosmik.pdf
text: raw/text/gursoy2026cosmik.txt
tags: [manipulators, hri, safety]
status: summarised
---

# COSMIK-MPPI: Scaling Constrained Model Predictive Control to Collision Avoidance in Close-Proximity Dynamic Human Environments

*Gursoy, Ege; Sabbah, Maxime; Haffemayer, Arthur; Cavalcanti Santos, Joao; Crestaz, Pietro Noah; Petrik, Vladimir; Mansard, Nicolas; Bonnet, Vincent* (2026). arXiv preprint arXiv:2604.10358.

## TL;DR
COSMIK-MPPI: MPPI + RT-COSMIK markerless human pose + constraints-as-terminations; 100% success at constant 22 ms, outperforming gradient-based MPC.

## Method
Constraint violation terminates rollout; no human motion prediction needed.

## Evidence
Sim (incl. infeasible scenarios) and real HRI on torque-controlled arm.

## Relevance for Plan4ARI
Most direct precedent for ISO/TS 15066-aware MPPI.

## Abstract (verbatim, arXiv)
> Ensuring safe physical interaction between torque-controlled manipulators and humans is essential for deploying robots in everyday environments. Model Predictive Control (MPC) has emerged as a suitable framework thanks to its capacity to handle hard constraints, provide strong guarantees and zero-shot adaptability through predictive reasoning. However, Gradient-Based MPC (GB-MPC) solvers have demonstrated limited performance for collision avoidance in complex environments. Sampling-based approaches such as Model Predictive Path Integral (MPPI) control offer an alternative via stochastic rollouts, but enforcing safety via additive penalties is inherently fragile, as it provides no formal constraint satisfaction guarantees. We propose a collision avoidance framework called COSMIK-MPPI combining MPPI with the toolbox for human motion estimation RT-COSMIK and the Constraints-as-Terminations transcription, which enforces safety by treating constraint violations as terminal events, without relying on large penalty terms or explicit human motion prediction. The proposed approach is evaluated against state-of-the-art GB-MPC and vanilla MPPI in simulation and on a real manipulator arm. Results show that COSMIK-MPPI achieves a 100% task success rate with a constant computation time (22 ms), largely outperforming GB-MPC. In simulated infeasible scenarios, COSMIK-MPPI consistently generates collision-free trajectories, contrary to vanilla MPPI. These properties enabled safe execution of complex real-world human-robot interaction tasks in shared workspaces using an affordable markerless human motion estimator, demonstrating a robust, compliant, and practical solution for predictive collision avoidance (cf. results showcased at https://exquisite-parfait-ffa925.netlify.app)

## Links
- [[concepts/constraints-and-safety]]
- [[applications/human-robot-shared-spaces]]
- [[applications/industrial-manipulators]]
- BibTeX key: `gursoy2026cosmik` in `latex/references.bib`
