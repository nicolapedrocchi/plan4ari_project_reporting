---
key: jankowski2023vpsto
title: "VP-STO: Via-point-based Stochastic Trajectory Optimization for Reactive Robot Behavior"
authors: "Jankowski, Julius; Brudermuller, Lara; Hawes, Nick; Calinon, Sylvain"
year: 2023
venue: "Proc. IEEE Int. Conf. Robotics and Automation (ICRA), pp. 10125-10131"
arxiv: 2210.04067
doi: 10.1109/ICRA48891.2023.10160214
pdf: raw/papers/jankowski2023vpsto.pdf
text: raw/text/jankowski2023vpsto.txt
tags: [manipulators, trajopt]
status: summarised
---

# VP-STO: Via-point-based Stochastic Trajectory Optimization for Reactive Robot Behavior

*Jankowski, Julius; Brudermuller, Lara; Hawes, Nick; Calinon, Sylvain* (2023). Proc. IEEE Int. Conf. Robotics and Automation (ICRA), pp. 10125-10131.

## TL;DR
VP-STO: stochastic (CMA-ES) optimisation over via-points with time-optimal smooth trajectories, used in MPC for reactive behaviour.

## Method
Via-point parametrisation, CMA-ES.

## Evidence
Franka reactive tasks.

## Relevance for Plan4ARI
Industrial-friendly trajectory representation for sampling MPC.

## Abstract (verbatim, arXiv)
> Achieving reactive robot behavior in complex dynamic environments is still challenging as it relies on being able to solve trajectory optimization problems quickly enough, such that we can replan the future motion at frequencies which are sufficiently high for the task at hand. We argue that current limitations in Model Predictive Control (MPC) for robot manipulators arise from inefficient, high-dimensional trajectory representations and the negligence of time-optimality in the trajectory optimization process. Therefore, we propose a motion optimization framework that optimizes jointly over space and time, generating smooth and timing-optimal robot trajectories in joint-space. While being task-agnostic, our formulation can incorporate additional task-specific requirements, such as collision avoidance, and yet maintain real-time control rates, demonstrated in simulation and real-world robot experiments on closed-loop manipulation. For additional material, please visit https://sites.google.com/oxfordrobotics.institute/vp-sto.

## Links
- [[concepts/smoothness-action-parametrization]]
- [[applications/industrial-manipulators]]
- BibTeX key: `jankowski2023vpsto` in `latex/references.bib`
