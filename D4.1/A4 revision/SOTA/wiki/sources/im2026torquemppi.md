---
key: im2026torquemppi
title: "Real-Time Dynamics-Based Torque-Sampling MPPI for Compliant and Force Aware Manipulation"
authors: "Im, Euncheol; Kim, Taehyun; Oh, Yonghwan; Lim, Myotaeg; Lee, Yisoo"
year: 2026
venue: "arXiv preprint arXiv:2609.02020"
arxiv: 2609.02020
doi: 
pdf: raw/papers/im2026torquemppi.pdf
text: raw/text/im2026torquemppi.txt
tags: [manipulators, torque, hri]
status: summarised
---

# Real-Time Dynamics-Based Torque-Sampling MPPI for Compliant and Force Aware Manipulation

*Im, Euncheol; Kim, Taehyun; Oh, Yonghwan; Lim, Myotaeg; Lee, Yisoo* (2026). arXiv preprint arXiv:2609.02020.

## TL;DR
Torque-sampling MPPI task-space control with full rigid-body dynamics and safety constraints; compliant, force-aware behaviour at >166 Hz, 0.18 s horizon.

## Method
Torque sampling on GPU, task-space costs, safety constraints.

## Evidence
Real 7-DoF manipulator.

## Relevance for Plan4ARI
MPPI at torque level for physical HRI.

## Abstract (verbatim, arXiv)
> This study proposes a novel Model Predictive Path Integral (MPPI)-based task-space control framework. The proposed framework explicitly solves rigid-body dynamics within a real-time MPC formulation and enforces safety constraints, enabling accurate motion and force control that yields compliant behaviors for safe and effective physical interaction of robotic manipulators in unstructured environments. By leveraging MPPI, the proposed framework efficiently handles nonlinear dynamics that are difficult to solve with conventional MPC approaches in real-time. Furthermore, we develop a torque-sampling-based control architecture that enables efficient exploitation of GPU-based parallelization, resulting in effective compliant and force-aware behaviors. As a result, the proposed framework achieves a solver update rate of over 166 Hz with a 0.18 s prediction horizon, and its performance is validated through real-world experiments on a 7-DoF manipulator.

## Links
- [[applications/industrial-manipulators]]
- [[applications/human-robot-shared-spaces]]
- BibTeX key: `im2026torquemppi` in `latex/references.bib`
