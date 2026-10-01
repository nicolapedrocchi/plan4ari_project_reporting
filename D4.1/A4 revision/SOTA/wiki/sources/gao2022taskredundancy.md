---
key: gao2022taskredundancy
title: "Optimal Motion Planning Considering Task Redundancy in Trajectory Tracking Applications for Industrial Robot"
authors: "Gao, Wenxiang; Tang, Qing; Yao, Jin"
year: 2022
venue: "2022 IEEE International Conference on Robotics and Biomimetics (ROBIO), pp. 1580-1585"
arxiv: 
doi: 10.1109/robio55434.2022.10011791
pdf: raw/papers/gao2022taskredundancy.pdf
text: raw/text/gao2022taskredundancy.txt
tags: [redundancy-resolution, path-following, industrial, manipulators, welding]
status: read
---

# Optimal Motion Planning Considering Task Redundancy in Trajectory Tracking Applications for Industrial Robot

*Gao, Wenxiang; Tang, Qing; Yao, Jin* (2022). 2022 IEEE International Conference on Robotics and Biomimetics (ROBIO), pp. 1580-1585.

## TL;DR
An offline, path-wise redundancy-resolution planner for a 6-axis industrial robot following a welding seam. The search space is a grid over (seam position × task-redundant angles): rotation about the torch axis, plus the work/swing angle in 2-D cases. A modified A* searches this grid. Each expanded node is mapped to joints by numerical IK seeded from the parent configuration, which keeps the joint path continuous on one branch, and is then collision-checked. The cost adds the travelled translation and rotation, a heuristic to the end of the seam, and a "guiding" term: the running maximum along the path of sigmoid-shaped joint-limit and singularity penalties. The authors argue that grid search gives resolution completeness, which they consider more appropriate for industry than probabilistic completeness.

## Method
- **A\* framework** (§II-A, Alg. 1): an open priority queue and a closed set; the path is recovered by backtracking.
- **Cost** (§II-B, Eq. 1–8): f = ω_g g + ω_h h + ω_e e.
  - g accumulates the translational length along the seam and the rotation angle between end-effector frames (Eq. 2, 4, 5).
  - h is the same metric evaluated to the goal (Eq. 3).
  - e is the maximum of the per-node penalties along the whole path (Eq. 6). The joint-limit penalty is a sigmoid in normalised margin (Eq. 7); the singularity penalty is a sigmoid in Yoshikawa manipulability with a threshold (Eq. 8).
- **Expansion** (§II-C, Alg. 2): FK of the current node, then the neighbours on the task-redundant grid. Numerical IK [21] is seeded with the current joints, followed by a collision check of the motion between nodes and the usual A* relaxation.

## Evidence
- Robot and environment: a self-developed simulation platform with a welding torch on a 6-axis industrial robot (model not named). There are no hardware experiments.
- No computation time, grid resolution, node count or comparison with another planner is reported.
- **Singularity test** (Fig. 1): a horizontal seam crossing a singularity. Without the singularity term, joints 4 and 6 jump and joint 5 turns back at zero; with it, the joint motions are gentle and joint 5 stays near zero without reaching it.
- **Joint-limit test** (Fig. 2): without the limit term, joint 3 exceeds its limit; with it, the joint stays inside its bounds.
- **1-D redundancy** (Figs. 3–4): torch perpendicular to a plate, free roll only, cylinder obstacle. The planner rolls the robot to the other side of the obstacle. The task-redundant map (position × roll angle) shows free, unreachable, collision and joint-limit zones together with the optimal path.
- **2-D redundancy** (Figs. 5–6): intersecting-pipe welding, roll plus swing angle in a cluttered scene. A collision-free path is shown, with redundant-angle profiles over about 300 steps.

## Relevance for Plan4ARI
- **The deterministic baseline, by design.** It plans in the task-redundant coordinates of welding (free roll, plus a bounded tilt within a cone), which are exactly the coordinates MPPI samples in [[comparisons/welding-mppi-design-review]]. It is a plain example of "graph search over a discretised null space along the seam", the baseline that flaw #24 requires ([[concepts/path-wise-redundancy-resolution]]).
- **Costs we can reuse.** The sigmoid joint-limit and singularity penalties and the max-along-path aggregation are reusable as MPPI running and terminal costs. The zone map (Fig. 4) is a useful visualisation for checking the feasibility of IK branches along a seam.

## Critical assessment (our view)
- **Missing numbers.** There are no timing or resolution figures, so whether it can run online over a 10 cm look-ahead cannot be judged. Grid A* in 2-D or more of redundancy times seam length grows quickly. The paper is better read as an offline seam planner.
- **Single IK branch.** IK is seeded from the parent, so the search follows one branch. Reconfigurations (detach and restart) and multi-branch goals are not modelled, so the planner cannot express the "fewest interruptions" objective of [[sources/yin2024dpbreakpoints]].
- **No timing.** Speed, joint-rate limits and the constant travel speed are ignored, as are smoothness of the redundant angles (beyond the rotation-distance cost), anisotropic cone limits and torch-hose constraints.
- **The max-type guiding term.** It is not additive, so A* optimality with it is questionable. The authors' optimality argument rests on the g/h part.

## Links
- [[comparisons/welding-mppi-design-review]]
- [[concepts/path-wise-redundancy-resolution]]
- [[applications/industrial-manipulators]]
- Related: [[sources/yin2024dpbreakpoints]], [[sources/yin2024dprealtime]], [[sources/zhong2024expansiongrr]], [[sources/demaeyer2017descartes]], [[sources/sun2024nullspacempc]]
- BibTeX key: `gao2022taskredundancy` in `latex/references.bib`
