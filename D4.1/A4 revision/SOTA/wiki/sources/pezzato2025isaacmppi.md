---
key: pezzato2025isaacmppi
title: "Sampling-based Model Predictive Control Leveraging Parallelizable Physics Simulations"
authors: "Pezzato, Corrado; Salmi, Chadi; Trevisan, Elia; Spahn, Max; Alonso-Mora, Javier; Hernandez Corbato, Carlos"
year: 2025
venue: "IEEE Robotics and Automation Letters, vol. 10, no. 3, pp. 2750-2757"
arxiv: 2307.09105
doi: 10.1109/LRA.2025.3535185
pdf: raw/papers/pezzato2025isaacmppi.pdf
text: raw/text/pezzato2025isaacmppi.txt
tags: [manipulators, mobile-manipulation, simulator]
status: summarised
---

# Sampling-based Model Predictive Control Leveraging Parallelizable Physics Simulations

*Pezzato, Corrado; Salmi, Chadi; Trevisan, Elia; Spahn, Max; Alonso-Mora, Javier; Hernandez Corbato, Carlos* (2025). IEEE Robotics and Automation Letters, vol. 10, no. 3, pp. 2750-2757.

## TL;DR
MPPI with IsaacGym as dynamics model: no explicit dynamics/contact modelling; navigation, pushing and whole-body control at 25 Hz with 750 parallel envs.

## Method
GPU physics simulator rollouts, Halton splines, open-source m3p2i-aip code base.

## Evidence
Sim and real: omnidirectional and differential-drive bases, fixed and mobile manipulators (Panda).

## Relevance for Plan4ARI
Basis of M3P2I; simulator-in-the-loop for contact tasks.

## Abstract (verbatim, arXiv)
> We present a method for sampling-based model predictive control that makes use of a generic physics simulator as the dynamical model. In particular, we propose a Model Predictive Path Integral controller (MPPI), that uses the GPU-parallelizable IsaacGym simulator to compute the forward dynamics of a problem. By doing so, we eliminate the need for explicit encoding of robot dynamics and contacts with objects for MPPI. Since no explicit dynamic modeling is required, our method is easily extendable to different objects and robots and allows one to solve complex navigation and contact-rich tasks. We demonstrate the effectiveness of this method in several simulated and real-world settings, among which mobile navigation with collision avoidance, non-prehensile manipulation, and whole-body control for high-dimensional configuration spaces. This method is a powerful and accessible open-source tool to solve a large variety of contact-rich motion planning tasks.

## Links
- [[concepts/physics-simulator-rollouts]]
- [[applications/mobile-manipulation-tamp]]
- [[applications/industrial-manipulators]]
- BibTeX key: `pezzato2025isaacmppi` in `latex/references.bib`
