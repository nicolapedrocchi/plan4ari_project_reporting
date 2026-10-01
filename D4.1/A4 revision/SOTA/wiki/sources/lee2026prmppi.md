---
key: lee2026prmppi
title: "Projection-Retraction MPPI: Exact Constraint-Manifold Control for Manipulators"
authors: "Lee, Seulchan; Park, Leesai; Kang, Minhyeong; Kim, Sanghyun"
year: 2026
venue: "arXiv preprint arXiv:2608.07573"
arxiv: 2608.07573
doi: 
pdf: raw/papers/lee2026prmppi.pdf
text: raw/text/lee2026prmppi.txt
tags: [manipulators, constraints]
status: summarised
---

# Projection-Retraction MPPI: Exact Constraint-Manifold Control for Manipulators

*Lee, Seulchan; Park, Leesai; Kang, Minhyeong; Kim, Sanghyun* (2026). arXiv preprint arXiv:2608.07573.

## TL;DR
PR-MPPI: projects sampled velocities onto equality (closed chain) and inequality (limits, clearance) constraints, then retracts onto the manifold: exact constraint satisfaction.

## Method
Projection-retraction inside rollouts.

## Evidence
14-DoF dual-arm sims; Unitree H1-2 arms real.

## Relevance for Plan4ARI
Hard joint/workspace constraints in MPPI without penalties.

## Abstract (verbatim, arXiv)
> Model Predictive Path Integral (MPPI) control is widely used in manipulation for its gradient-free, parallel handling of non-convex costs. Manipulation tasks, however, often impose constraints that hold throughout the motion: a closed kinematic chain that two grasping arms keep exactly, or joint limits and obstacle clearances that are never crossed. MPPI handles such constraints only through the cost, as soft penalties that hold approximately and fail under a strong task cost. To address this, we propose Projection-Retraction MPPI (PR-MPPI), which enforces the constraints inside the sampled dynamics. At every rollout step, the sampled velocity is projected to satisfy both constraint types: the equality restricts it to a subspace, and each inequality to a half-space within that subspace, so inequality handling never breaks the equality. This projection, however, satisfies the constraints only to first order, and a finite step leaves a small drift off the equality. Therefore, we retract the returned command back onto the constraint to numerical tolerance and independent of task weighting. We validate PR-MPPI on 14-DoF dual-arm systems. In simulation, the returned commands satisfy the closed-chain equality to numerical tolerance through a joint-limit stress test and randomized obstacle avoidance. On real hardware, the arms of a Unitree H1-2 humanoid reactively avoid a moving obstacle. Code and experiment videos are available at https://rcilab.github.io/prmppi.

## Links
- [[concepts/constraints-and-safety]]
- [[applications/industrial-manipulators]]
- BibTeX key: `lee2026prmppi` in `latex/references.bib`
