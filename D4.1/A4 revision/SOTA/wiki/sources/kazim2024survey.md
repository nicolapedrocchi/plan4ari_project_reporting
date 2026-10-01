---
key: kazim2024survey
title: "Recent Advances in Path Integral Control for Trajectory Optimization: An Overview in Theoretical and Algorithmic Perspectives"
authors: "Kazim, Muhammad; Hong, JunGee; Kim, Min-Gyeom; Kim, Kwang-Ki K."
year: 2024
venue: "Annual Reviews in Control, vol. 57, pp. 100931"
arxiv: 2309.12566
doi: 10.1016/j.arcontrol.2023.100931
pdf: raw/papers/kazim2024survey.pdf
text: raw/text/kazim2024survey.txt
tags: [survey]
status: summarised
---

# Recent Advances in Path Integral Control for Trajectory Optimization: An Overview in Theoretical and Algorithmic Perspectives

*Kazim, Muhammad; Hong, JunGee; Kim, Min-Gyeom; Kim, Kwang-Ki K.* (2024). Annual Reviews in Control, vol. 57, pp. 100931.

## TL;DR
Survey of path-integral control for trajectory optimisation: theory (KL, free energy, variational inference), algorithmic variants and applications.

## Method
Review.

## Evidence
Benchmark simulations of several variants.

## Relevance for Plan4ARI
Used to cross-check coverage of the SOTA. Good entry point for new team members.

## Abstract (verbatim, arXiv)
> This paper presents a tutorial overview of path integral (PI) control approaches for stochastic optimal control and trajectory optimization. We concisely summarize the theoretical development of path integral control to compute a solution for stochastic optimal control and provide algorithmic descriptions of the cross-entropy (CE) method, an open-loop controller using the receding horizon scheme known as the model predictive path integral (MPPI), and a parameterized state feedback controller based on the path integral control theory. We discuss policy search methods based on path integral control, efficient and stable sampling strategies, extensions to multi-agent decision-making, and MPPI for the trajectory optimization on manifolds. For tutorial demonstrations, some PI-based controllers are implemented in Python, MATLAB and ROS2/Gazebo simulations for trajectory optimization. The simulation frameworks and source codes are publicly available at https://github.com/INHA-Autonomous-Systems-Laboratory-ASL/An-Overview-on-Recent-Advances-in-Path-Integral-Control.

## Links
- [[concepts/path-integral-control]]
- [[concepts/information-theoretic-mppi]]
- [[comparisons/mppi-variants-matrix]]
- BibTeX key: `kazim2024survey` in `latex/references.bib`
