---
key: laha2023sstar
title: "S*: On Safe and Time Efficient Robot Motion Planning"
authors: "Laha, Riddhiman; Wu, Wenxi; Sun, Ruiai; Mansfeld, Nico; Figueredo, Luis F. C.; Haddadin, Sami"
year: 2023
venue: "Proc. IEEE Int. Conf. Robotics and Automation (ICRA), pp. 12758-12764"
arxiv: 
doi: 10.1109/ICRA48891.2023.10161248
pdf: raw/papers/laha2023sstar.pdf
text: raw/text/laha2023sstar.txt
tags: [hri, safety, iso-ts-15066, manipulators, path-planning]
status: read
---

# S*: On Safe and Time Efficient Robot Motion Planning

*Laha, Riddhiman; Wu, Wenxi; Sun, Ruiai; Mansfeld, Nico; Figueredo, Luis F. C.; Haddadin, Sami* (2023). Proc. IEEE Int. Conf. Robotics and Automation (ICRA), pp. 12758-12764.

## TL;DR
S* / Lazy-S*: a task-space, lazy weighted-A* planner whose edge cost is the traversal time max(t_lim, t_SMU), i.e. the slower of the joint-limit time-optimal transfer (Ruckig) and the time allowed by the biomechanically safe velocity (reflected mass → safety curve). The search therefore prefers routes with low reflected mass where higher safe speeds are allowed.

## Method
- Voxelised task space (4-D: position + interpolated orientation), IKFast feasibility per node, redundancy resolved by weighted minimum joint motion (§IV-A).
- Edge evaluation: time-optimal joint transfer with Ruckig (TOJO) + safe velocity from the Safe Motion Unit / safety map (reflected mass, Eq. 4) → w = max(t_lim, t_SMU) (Eq. 5).
- Lazy edge evaluation to reduce cost; resolution-complete only on the task-space grid (§IV-B).
- Collisions assumed only at the end-effector; human (quasi-)static.

## Evidence
- 100 obstacle-free scenarios, UR5 in CoppeliaSim (Table I): S* time-to-goal 3.60 s, Lazy-S* 3.42 s, vs RRT*+SJBO 5.35 s, Lazy-A*+SJBO 6.33 s, A*+SJBO 6.79 s (decoupled plan-then-scale baselines); the unsafe time-optimal Lazy-A*+TOJO (2.32 s) spends 70.5% of the trajectory outside the safety bounds.
- Real Franka pick&place near a human (Fig. 3): plain velocity scaling takes about twice as long for the same path; Lazy-S* stays within the safe velocity bound.
- Non-optimised code used offline; online use with dynamic obstacles is future work.

## Relevance for Plan4ARI
- Cited in the Project Description ([[project/prj-plan4ari-proposal]]) as an example of planners that consider human influence only offline.
- Same principle as [[sources/faroni2022safetyaware]] (make the planner minimise *time including safety limits*), but with PFL/biomechanics limits instead of SSM and a graph search instead of RRT*.
- For an MPPI layer: t_SMU per state is another non-smooth, per-configuration cost that MPPI can evaluate in parallel on rollouts; the reflected mass along the motion direction is cheap to compute on GPU.

## Critical assessment (our view)
- Offline, static human, end-effector-only contact and obstacle-free benchmarks: far from the dynamic multi-agent setting of Plan4ARI; useful mainly as a cost-function design reference and as a baseline for D4.1 §5.

## Links
- [[applications/human-robot-shared-spaces]]
- [[concepts/constraints-and-safety]]
- [[project/prj-plan4ari-proposal]]
- [[sources/faroni2022safetyaware]]
- [[sources/palleschi2021fastsafe]]
- BibTeX key: `laha2023sstar` in `latex/references.bib`
