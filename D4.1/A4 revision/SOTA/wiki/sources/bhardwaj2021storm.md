---
key: bhardwaj2021storm
title: "STORM: An Integrated Framework for Fast Joint-Space Model-Predictive Control for Reactive Manipulation"
authors: "Bhardwaj, Mohak; Sundaralingam, Balakumar; Mousavian, Arsalan; Ratliff, Nathan; Fox, Dieter; Ramos, Fabio; Boots, Byron"
year: 2022
venue: "Proc. Conf. Robot Learning (CoRL), PMLR vol. 164, pp. 750-759"
arxiv: 2104.13542
doi: 
pdf: raw/papers/bhardwaj2021storm.pdf
text: raw/text/bhardwaj2021storm.txt
tags: [manipulators, gpu, software]
status: summarised
---

# STORM: An Integrated Framework for Fast Joint-Space Model-Predictive Control for Reactive Manipulation

*Bhardwaj, Mohak; Sundaralingam, Balakumar; Mousavian, Arsalan; Ratliff, Nathan; Fox, Dieter; Ramos, Fabio; Boots, Byron* (2022). Proc. Conf. Robot Learning (CoRL), PMLR vol. 164, pp. 750-759.

## TL;DR
STORM: GPU joint-space MPPI for 7-DoF arms with learned self-collision and SDF costs, Halton-spline sampling; 125 Hz with task and joint constraints.

## Method
Batched kinematics on GPU, MPPI with Halton splines, cost terms for limits/collisions.

## Evidence
Franka real-world reactive reaching, pose tracking, obstacle avoidance.

## Relevance for Plan4ARI
Reference architecture for MPPI on industrial arms.

## Abstract (verbatim, arXiv)
> Sampling-based model-predictive control (MPC) is a promising tool for feedback control of robots with complex, non-smooth dynamics, and cost functions. However, the computationally demanding nature of sampling-based MPC algorithms has been a key bottleneck in their application to high-dimensional robotic manipulation problems in the real world. Previous methods have addressed this issue by running MPC in the task space while relying on a low-level operational space controller for joint control. However, by not using the joint space of the robot in the MPC formulation, existing methods cannot directly account for non-task space related constraints such as avoiding joint limits, singular configurations, and link collisions. In this paper, we develop a system for fast, joint space sampling-based MPC for manipulators that is efficiently parallelized using GPUs. Our approach can handle task and joint space constraints while taking less than 8ms~(125Hz) to compute the next control command. Further, our method can tightly integrate perception into the control problem by utilizing learned cost functions from raw sensor data. We validate our approach by deploying it on a Franka Panda robot for a variety of dynamic manipulation tasks. We study the effect of different cost formulations and MPC parameters on the synthesized behavior and provide key insights that pave the way for the application of sampling-based MPC for manipulators in a principled manner. We also provide highly optimized, open-source code to be used by the wider robot learning and control community. Videos of experiments can be found at: https://sites.google.com/view/manipulation-mpc

## Links
- [[applications/industrial-manipulators]]
- [[tools/software-ecosystem]]
- [[concepts/smoothness-action-parametrization]]
- BibTeX key: `bhardwaj2021storm` in `latex/references.bib`
