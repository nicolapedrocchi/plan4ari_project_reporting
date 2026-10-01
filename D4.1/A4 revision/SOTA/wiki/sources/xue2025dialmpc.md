---
key: xue2025dialmpc
title: "Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing"
authors: "Xue, Haoru; Pan, Chaoyi; Yi, Zeji; Qu, Guannan; Shi, Guanya"
year: 2025
venue: "Proc. IEEE Int. Conf. Robotics and Automation (ICRA), pp. 4974-4981"
arxiv: 2409.15610
doi: 10.1109/ICRA55743.2025.11127320
pdf: raw/papers/xue2025dialmpc.pdf
text: raw/text/xue2025dialmpc.txt
tags: [diffusion, locomotion]
status: summarised
---

# Full-Order Sampling-Based MPC for Torque-Level Locomotion Control via Diffusion-Style Annealing

*Xue, Haoru; Pan, Chaoyi; Yi, Zeji; Qu, Guannan; Shi, Guanya* (2025). Proc. IEEE Int. Conf. Robotics and Automation (ICRA), pp. 4974-4981.

## TL;DR
DIAL-MPC: diffusion-style annealing of MPPI noise for full-order torque-level sampling MPC.

## Method
Annealed multi-iteration MPPI.

## Evidence
Quadruped hardware.

## Relevance for Plan4ARI
Annealing for high-dimensional systems (whole-body).

## Abstract (verbatim, arXiv)
> Due to high dimensionality and non-convexity, real-time optimal control using full-order dynamics models for legged robots is challenging. Therefore, Nonlinear Model Predictive Control (NMPC) approaches are often limited to reduced-order models. Sampling-based MPC has shown potential in nonconvex even discontinuous problems, but often yields suboptimal solutions with high variance, which limits its applications in high-dimensional locomotion. This work introduces DIAL-MPC (Diffusion-Inspired Annealing for Legged MPC), a sampling-based MPC framework with a novel diffusion-style annealing process. Such an annealing process is supported by the theoretical landscape analysis of Model Predictive Path Integral Control (MPPI) and the connection between MPPI and single-step diffusion. Algorithmically, DIAL-MPC iteratively refines solutions online and achieves both global coverage and local convergence. In quadrupedal torque-level control tasks, DIAL-MPC reduces the tracking error of standard MPPI by $13.4$ times and outperforms reinforcement learning (RL) policies by $50\%$ in challenging climbing tasks without any training. In particular, DIAL-MPC enables precise real-world quadrupedal jumping with payload. To the best of our knowledge, DIAL-MPC is the first training-free method that optimizes over full-order quadruped dynamics in real-time.

## Links
- [[concepts/sampling-distributions]]
- [[concepts/hybrid-gradient-sampling]]
- BibTeX key: `xue2025dialmpc` in `latex/references.bib`
