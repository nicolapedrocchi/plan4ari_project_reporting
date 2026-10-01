---
key: trevisan2025drampi
title: "Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations"
authors: "Trevisan, Elia; Mustafa, Khaled A.; Notten, Godert; Wang, Xinwei; Alonso-Mora, Javier"
year: 2025
venue: "Proc. IEEE/RSJ Int. Conf. Intelligent Robots and Systems (IROS), pp. 313-320"
arxiv: 2506.21205
doi: 10.1109/IROS60139.2025.11246822
pdf: raw/papers/trevisan2025drampi.pdf
text: raw/text/trevisan2025drampi.txt
tags: [mobile, hri, safety]
status: summarised
---

# Dynamic Risk-Aware MPPI for Mobile Robots in Crowds via Efficient Monte Carlo Approximations

*Trevisan, Elia; Mustafa, Khaled A.; Notten, Godert; Wang, Xinwei; Alonso-Mora, Javier* (2025). Proc. IEEE/RSJ Int. Conf. Intelligent Robots and Systems (IROS), pp. 313-320.

## TL;DR
DRA-MPPI: Monte-Carlo joint collision probability against non-Gaussian human predictions for hundreds of rollouts in real time; sample rejection or CP cost.

## Method
MC collision probability per rollout.

## Evidence
Real and simulated crowds.

## Relevance for Plan4ARI
Human-aware AMR navigation, mitigates freezing robot.

## Abstract (verbatim, arXiv)
> Deploying mobile robots safely among humans requires the motion planner to account for the uncertainty in the other agents' predicted trajectories. This remains challenging in traditional approaches, especially with arbitrarily shaped predictions and real-time constraints. To address these challenges, we propose a Dynamic Risk-Aware Model Predictive Path Integral control (DRA-MPPI), a motion planner that incorporates uncertain future motions modelled with potentially non-Gaussian stochastic predictions. By leveraging MPPI's gradient-free nature, we propose a method that efficiently approximates the joint Collision Probability (CP) among multiple dynamic obstacles for several hundred sampled trajectories in real-time via a Monte Carlo (MC) approach. This enables the rejection of samples exceeding a predefined CP threshold or the integration of CP as a weighted objective within the navigation cost function. Consequently, DRA-MPPI mitigates the freezing robot problem while enhancing safety. Real-world and simulated experiments with multiple dynamic obstacles demonstrate DRA-MPPI's superior performance compared to state-of-the-art approaches, including Scenario-based Model Predictive Control (S-MPC), Frenet planner, and vanilla MPPI.

## Links
- [[applications/human-robot-shared-spaces]]
- [[applications/mobile-robots-amr]]
- [[concepts/constraints-and-safety]]
- BibTeX key: `trevisan2025drampi` in `latex/references.bib`
