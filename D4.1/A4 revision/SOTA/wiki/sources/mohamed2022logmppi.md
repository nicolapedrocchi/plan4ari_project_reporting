---
key: mohamed2022logmppi
title: "Autonomous Navigation of AGVs in Unknown Cluttered Environments: log-MPPI Control Strategy"
authors: "Mohamed, Ihab S.; Yin, Kai; Liu, Lantao"
year: 2022
venue: "IEEE Robotics and Automation Letters, vol. 7, no. 4, pp. 10240-10247"
arxiv: 2203.16599
doi: 10.1109/LRA.2022.3192772
pdf: raw/papers/mohamed2022logmppi.pdf
text: raw/text/mohamed2022logmppi.txt
tags: [sampling, mobile]
status: summarised
---

# Autonomous Navigation of AGVs in Unknown Cluttered Environments: log-MPPI Control Strategy

*Mohamed, Ihab S.; Yin, Kai; Liu, Lantao* (2022). IEEE Robotics and Automation Letters, vol. 7, no. 4, pp. 10240-10247.

## TL;DR
log-MPPI: normal-log-normal mixture noise for better exploration; navigation of AGVs in unknown cluttered environments with local costmaps.

## Method
NLN sampling distribution.

## Evidence
2D navigation sims, real AGV.

## Relevance for Plan4ARI
Directly targets AGVs with costmaps.

## Abstract (verbatim, arXiv)
> Sampling-based model predictive control (MPC) optimization methods, such as Model Predictive Path Integral (MPPI), have recently shown promising results in various robotic tasks. However, it might produce an infeasible trajectory when the distributions of all sampled trajectories are concentrated within high-cost even infeasible regions. In this study, we propose a new method called log-MPPI equipped with a more effective trajectory sampling distribution policy which significantly improves the trajectory feasibility in terms of satisfying system constraints. The key point is to draw the trajectory samples from the normal log-normal (NLN) mixture distribution, rather than from Gaussian distribution. Furthermore, this work presents a method for collision-free navigation in unknown cluttered environments by incorporating the 2D occupancy grid map into the optimization problem of the sampling-based MPC algorithm. We first validate the efficiency and robustness of our proposed control strategy through extensive simulations of 2D autonomous navigation in different types of cluttered environments as well as the cartpole swing-up task. We further demonstrate, through real-world experiments, the applicability of log-MPPI for performing a 2D grid-based collision-free navigation in an unknown cluttered environment, showing its superiority to be utilized with the local costmap without adding additional complexity to the optimization problem. A video demonstrating the real-world and simulation results is available at https://youtu.be/_uGWQEFJSN0.

## Links
- [[concepts/sampling-distributions]]
- [[applications/mobile-robots-amr]]
- BibTeX key: `mohamed2022logmppi` in `latex/references.bib`
