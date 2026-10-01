---
key: dierking2026parallelsbmpc
title: "Real-World Deployment of Massively Parallel Sampling-Based MPC for Contact-Rich Manipulation"
authors: "Dierking, Magnus; Carvalho, Joao; Le, An Thai; Chalvatzaki, Georgia; Peters, Jan"
year: 2026
venue: "arXiv preprint arXiv:2606.20712"
arxiv: 2606.20712
doi: 
pdf: raw/papers/dierking2026parallelsbmpc.pdf
text: raw/text/dierking2026parallelsbmpc.txt
tags: [manipulators, contact, simulator]
status: summarised
---

# Real-World Deployment of Massively Parallel Sampling-Based MPC for Contact-Rich Manipulation

*Dierking, Magnus; Carvalho, Joao; Le, An Thai; Chalvatzaki, Georgia; Peters, Jan* (2026). arXiv preprint arXiv:2606.20712.

## TL;DR
Real-world JAX + MuJoCo-MJX sampling MPC on Franka FR3 for Push-T; structured multimodal sampling (MTP) beats CEM/MPPI/PS; online domain randomisation analysed.

## Method
Massively parallel MJX rollouts, real-to-sim-to-real pipeline, MoveIt Servo at 1 kHz.

## Evidence
Sim and hardware; planning at 8-10 Hz on RTX 5090.

## Relevance for Plan4ARI
Honest assessment of compute and contact-model limits.

## Abstract (verbatim, arXiv)
> Sampling-based Model Predictive Control (SMPC) is a promising strategy for contact-rich robotic manipulation, combining gradient-free optimization with massively parallel GPU simulation. Yet, most prior work relies on simplified dynamics or remains confined to simulation. We present an MPC framework that leverages JAX for large-scale parallelization and efficient computation, coupled with the high-fidelity MuJoCo MJX simulator, and deploy it on a Franka Research 3 executing the Push-T manipulation task through a complete real-to-sim-to-real pipeline. The MTP variant with structured global sampling outperforms unimodal baselines such as CEM, MPPI, and PS across tasks that require mode switching, both in simulation and on hardware. Furthermore, we evaluate online domain randomization within the MPC sample budget, showing that contact-initiation parameters yield interpretable adaptation signals, whereas global physics parameters provide feedback that is too weak for reliable exploitation at typical replanning frequencies. These findings highlight key challenges for sampling-based MPC in contact-rich manipulation-contact sensitivity, tight compute budgets, and the difficulty of obtaining informative domain-randomization signals in real time.

## Links
- [[concepts/physics-simulator-rollouts]]
- [[concepts/multimodality]]
- [[applications/industrial-manipulators]]
- BibTeX key: `dierking2026parallelsbmpc` in `latex/references.bib`
