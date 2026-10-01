---
key: yin2022covsteering
title: "Trajectory Distribution Control for Model Predictive Path Integral Control using Covariance Steering"
authors: "Yin, Ji; Zhang, Zhiyuan; Theodorou, Evangelos; Tsiotras, Panagiotis"
year: 2022
venue: "Proc. IEEE Int. Conf. Robotics and Automation (ICRA), pp. 1478-1484"
arxiv: 2109.12147
doi: 10.1109/ICRA46639.2022.9811615
pdf: raw/papers/yin2022covsteering.pdf
text: raw/text/yin2022covsteering.txt
tags: [robustness, sampling]
status: summarised
---

# Trajectory Distribution Control for Model Predictive Path Integral Control using Covariance Steering

*Yin, Ji; Zhang, Zhiyuan; Theodorou, Evangelos; Tsiotras, Panagiotis* (2022). Proc. IEEE Int. Conf. Robotics and Automation (ICRA), pp. 1478-1484.

## TL;DR
Covariance-steering MPPI: shapes the distribution of sampled trajectories (terminal covariance) for better sample efficiency.

## Method
Covariance steering of the sampling distribution.

## Evidence
Simulated race car.

## Relevance for Plan4ARI
Better use of sample budget.

## Abstract (verbatim, arXiv)
> This paper presents a novel control approach for autonomous systems operating under uncertainty. We combine Model Predictive Path Integral (MPPI) control with Covariance Steering (CS) theory to obtain a robust controller for general nonlinear systems. The proposed Covariance-Controlled Model Predictive Path Integral (CC-MPPI) controller addresses the performance degradation observed in some MPPI implementations owing to unexpected disturbances and uncertainties. Namely, in cases where the environment changes too fast or the simulated dynamics during the MPPI rollouts do not capture the noise and uncertainty in the actual dynamics, the baseline MPPI implementation may lead to divergence. The proposed CC-MPPI controller avoids divergence by controlling the dispersion of the rollout trajectories at the end of the prediction horizon. Furthermore, the CC-MPPI has adjustable trajectory sampling distributions that can be changed according to the environment to achieve efficient sampling. Numerical examples using a ground vehicle navigating in challenging environments demonstrate the proposed approach.

## Links
- [[concepts/sampling-distributions]]
- [[concepts/robustness-uncertainty]]
- BibTeX key: `yin2022covsteering` in `latex/references.bib`
