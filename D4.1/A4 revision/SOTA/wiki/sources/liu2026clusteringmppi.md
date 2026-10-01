---
key: liu2026clusteringmppi
title: "Clustering-Embedded Model Predictive Path Integral Control: Avoiding Averaging-Induced Failure and Enabling Efficient Cluster Selection for Dynamic Obstacles"
authors: "Liu, Zidong; Chang, Kaixin; Chen, Xu"
year: 2026
venue: "arXiv preprint arXiv:2607.06499"
arxiv: 2607.06499
doi: 
pdf: raw/papers/liu2026clusteringmppi.pdf
text: raw/text/liu2026clusteringmppi.txt
tags: [multimodal, manipulators]
status: summarised
---

# Clustering-Embedded Model Predictive Path Integral Control: Avoiding Averaging-Induced Failure and Enabling Efficient Cluster Selection for Dynamic Obstacles

*Liu, Zidong; Chang, Kaixin; Chen, Xu* (2026). arXiv preprint arXiv:2607.06499.

## TL;DR
CE-MPPI: DBSCAN clustering of rollouts with a geometric direction feature isolates feasible modes and avoids averaging-induced failure.

## Method
Prune and cluster rollouts, choose mode by cost/obstacle flux.

## Evidence
2D JAX sims; real UR5e with Isaac Gym rollouts (-48% time-to-goal, -12% path).

## Relevance for Plan4ARI
Fixes the main weakness of M3P2I blending.

## Abstract (verbatim, arXiv)
> With the widespread availability of parallel computing hardware, sampling-based motion planning methods such as Model Predictive Path Integral (MPPI) control have become increasingly powerful for complex nonlinear systems in non-smooth task spaces. However, the sampling and forward-simulation pipeline in MPPI suffers from averaging-induced failure in cluttered environments, where the importance-weighted update averages incompatible rollouts and leads to hesitation or even collision when an obstacle lies directly ahead. This paper proposes Clustering-Embedded MPPI (CE-MPPI), a framework that architecturally resolves the averaging-induced failures inherent in standard MPPI within non-convex environments. Rather than simply mitigating interference, CE-MPPI redefines the control law by integrating a high-fidelity pruning and clustering stage. By leveraging density-based spatial clustering of applications with noise (DBSCAN) alongside a novel geometric direction feature that is extracted from collision-derived reference points, the system isolates feasible trajectory modes from the noise of infeasible rollouts. This is paired with an intelligent selection logic that optimizes for minimum cost in static scenes while actively steering opposite to obstacle flux in dynamic environments. Experiments in 2-D JAX-accelerated simulations show that CE-MPPI alleviates obstacle-front hesitation and avoids persistent coupling with moving obstacles in dynamic scenes. In particular, real-world tests on a 6-DoF UR5e manipulator with CUDA-parallel rollouts in Isaac Gym achieve a 48\% reduction in time-to-goal and a 12\% shorter end-effector path.

## Links
- [[concepts/multimodality]]
- [[applications/industrial-manipulators]]
- BibTeX key: `liu2026clusteringmppi` in `latex/references.bib`
