---
key: faroni2022safetyaware
title: "Safety-Aware Time-Optimal Motion Planning with Uncertain Human State Estimation"
authors: "Faroni, Marco; Beschi, Manuel; Pedrocchi, Nicola"
year: 2022
venue: "IEEE Robotics and Automation Letters, vol. 7, no. 4, pp. 12219-12226"
arxiv: 2210.11655
doi: 10.1109/LRA.2022.3211493
pdf: raw/papers/faroni2022safetyaware.pdf
text: raw/text/faroni2022safetyaware.txt
tags: [hri, safety, iso-ts-15066, manipulators, industrial, path-planning]
status: read
---

# Safety-Aware Time-Optimal Motion Planning with Uncertain Human State Estimation

*Faroni, Marco; Beschi, Manuel; Pedrocchi, Nicola* (2022). IEEE Robotics and Automation Letters, vol. 7, no. 4, pp. 12219-12226.

## TL;DR
Human-aware path planner (HAMP) whose cost is the **expected execution time including ISO/TS 15066 safety slowdowns**, instead of an arbitrary trade-off of distance/comfort terms. SSM/PFL speed limits are converted into a configuration-space *time-dilation* costmap λ(q, H) ≥ 1; deterministic and probabilistic (voxel occupancy) human states are supported; independent of the prediction model and usable in any C-space planner (Informed-RRT* in the paper).

## Method
- SSM protective distance (Eq. 1–3) gives a maximum robot–human relative speed v_max; PFL gives an analogous limit (§II-B).
- Path cost c = Σ_l t_nom,l · λ(midpoint_l, H) (Eq. 7–8), with t_nom from the assumption that one joint always moves at full speed (decouples cost from velocities); Tikhonov term on length (Eq. 9).
- Deterministic human (points h_j): λ = max(1, max_j v_rh,j / v_max) using Jacobians of robot points (Eq. 10–13); human velocity set to 0 in experiments.
- Probabilistic human (voxel occupancy π_j): expected λ from worst-case-first ordering of voxels (Eq. 15–16).
- Multi-goal approximation: path length + terminal human-aware cost b·λ(q_goal) (Eq. 17), much cheaper.
- Execution: speed override s_ovr = min(v_max / v_rh,max, 1) (Eq. 18) as runtime safety module.

## Evidence
- Simulation, 3-DoF arm, 100 queries × 6 runs (Table I): Exp. A, C = 0.2 m: path +30%, execution time −19%, safety delay −17%, success 0.985 vs 0.901; C = 0.5 m: execution −11%, success 0.829 vs 0.675. Exp. B (probabilistic update): HAMP-Probabilistic success 0.93 vs HAMP 0.86. Exp. C (20 equivalent goals): execution −50% (HAMP), −45% (approximated).
- Real cell (Sharework project): UR10e, two RealSense D435 @ 30 Hz, 16 pick&place with an operator, 10 participants (Table II): robot time 135 s vs 166 s (−19%), speed scaling 91.2% vs 78.8%, human–robot distance 1.07 vs 0.96 m; operators' time not significantly different.
- Limits stated by the authors: real-world gain smaller than in simulation because of the simple human prediction; λ computation is the bottleneck; future work: neural approximation of λ and integration into online re-planners.

## Relevance for Plan4ARI
- It is the ISO/TS 15066 cost explicitly named in the Project Description §A.4.2.2 ([[project/prj-plan4ari-proposal]]).
- **Direct fit with MPPI**: λ(q, H) is a per-configuration, non-smooth, gradient-free cost — exactly what MPPI evaluates on each rollout state. Summing λ-weighted time over a rollout gives an MPPI running cost that targets the KPI "−30% interaction-task execution time" directly.
- The paper's own future work (cheaper λ, integration in online re-planning, parallel evaluation over many human/robot points) is what a GPU MPPI provides; probabilistic voxel occupancy matches Monte-Carlo risk in [[sources/trevisan2025drampi]].

## Critical assessment (our view)
- Path-level planner (no time/velocity in the state): inside MPPI the velocity is available, so the full v_rh (including human velocity, set to 0 in the paper) can be used.
- The cost minimises *expected* slowdown, it does not certify safety: the runtime speed override (Eq. 18) or a Core-IPC filter must remain ([[concepts/constraints-and-safety]]).

## Abstract (verbatim, arXiv)
> Human awareness in robot motion planning is crucial for seamless interaction with humans. Many existing techniques slow down, stop, or change the robot's trajectory locally to avoid collisions with humans. Although using the information on the human's state in the path planning phase could reduce future interference with the human's movements and make safety stops less frequent, such an approach is less widespread. This paper proposes a novel approach to embedding a human model in the robot's path planner. The method explicitly addresses the problem of minimizing the path execution time, including slowdowns and stops owed to the proximity of humans. For this purpose, it converts safety speed limits into configuration-space cost functions that drive the path's optimization. The costmap can be updated based on the observed or predicted state of the human. The method can handle deterministic and probabilistic representations of the human state and is independent of the prediction algorithm. Numerical and experimental results on an industrial collaborative cell demonstrate that the proposed approach consistently reduces the robot's execution time and avoids unnecessary safety speed reductions.

## Links
- [[applications/human-robot-shared-spaces]]
- [[concepts/constraints-and-safety]]
- [[comparisons/plan4ari-gap-analysis]]
- [[project/prj-plan4ari-proposal]]
- Related: [[sources/gursoy2026cosmik]], [[sources/trevisan2025drampi]]
- BibTeX key: `faroni2022safetyaware` in `latex/references.bib`
