---
key: zhou2022weldavoidance
title: "Online obstacle avoidance path planning and application for arc welding robot"
authors: "Zhou, Xin; Wang, Xuewu; Xie, Zuhong; Li, Fang; Gu, Xingsheng"
year: 2022
venue: "Robotics and Computer-Integrated Manufacturing, vol. 78, pp. 102413"
arxiv: 
doi: 10.1016/j.rcim.2022.102413
pdf: raw/papers/zhou2022weldavoidance.pdf
text: raw/text/zhou2022weldavoidance.txt
tags: [welding, path-planning, manipulators, industrial]
status: read
---

# Online obstacle avoidance path planning and application for arc welding robot

*Zhou, Xin; Wang, Xuewu; Xie, Zuhong; Li, Fang; Gu, Xingsheng* (2022). Robotics and Computer-Integrated Manufacturing, vol. 78, pp. 102413.

## TL;DR
Collision-free planning of the **transition motions between welds** for a 7-DOF arc welding robot (FANUC M20iD/25 on a linear external axis) welding shipbuilding stiffened plates whose placement on the table varies. The workpiece pose is measured by an overhead laser scanner and the precomputed environment/roadmap is rigidly transformed; an improved **lazy-PRM** then searches TCP-space roadmaps with an A* cost augmented by a grid-based **repulsive field** (safety distance), collision-checks the candidate path a posteriori on a 10 mm voxel grid, and, if only the torch collides, nudges the torch pose away from the overlap (≤ 20 steps). Weld seams themselves are fixed and assumed collision-free; seam order, direction and torch angles at the seam ends are given. In MATLAB simulations it beats lazy-PRM, RRT* and AB-RRT* on a time/length composite cost; on three real workpieces it plans the full job in 10–26 s on average. "Online" here means per-workpiece replanning in seconds to tens of seconds, not reactive control.

## Method
- **Setting (§2)**: FANUC M20iD/25 + prismatic external axis (0 to −3 m) as a 7-DOF kinematic chain (DH in Table 1); torch carries a seam-tracking sensor that constrains the torch direction (sensor must lead), torch perpendicular to the seam and at 45° to both plates. Requirements: known static workpiece geometry, user-defined weld sequence/direction, predefined torch poses at seam terminals.
- **Offline preparation (§3.1)**: robot (7 link segments incl. torch) and workpiece voxelised from STL at 10 mm; rule-based approach points lifting the torch above the seam (Fig. 5) because voxel inflation buries corner seams; low-dispersion random sampling near obstacles (minimum inter-sample radius from a Lebesgue-volume argument, Eq. 6) plus uniform sampling elsewhere; samples include random torch orientation (w, p, r); connectivity matrix of collision-free TCP segments.
- **Online adjustment (§3.2)**: laser scan gives rotation about z and x/y offsets; workpiece model and roadmap are transformed (Eq. 7) instead of rebuilt.
- **Query (§3.3)**: A* with cost = path length + μ × sum of repulsive-field levels crossed (Eq. 9); field levels are integers decreasing away from obstacles; max level × grid size = safety distance.
- **Lazy collision checking (§3.4)**: candidate path interpolated in Q points; IK (analytic, up to 8 solutions) per point; branch selection minimising motion of joints 1–3 first, then weighted joint change (weights 0.3/0.3/0.3/0.1/0.1/0.1, Eq. 13); robot voxels intersected with obstacle voxels; colliding nodes/edges removed and A* repeated.
- **Posture adjustment (§3.5)**: when only the torch collides, the TCP is shifted along the resultant vector from the torch centre to the overlapping voxels, step = grid size, up to 20 times (Eqs. 14–15); otherwise the edge is discarded.

## Evidence
- **Simulation (§4, MATLAB, 20 runs, four box obstacles, Table 2)**, composite cost = 0.5 (T_roadmap + T_search) + 0.5 · length/10 (Eq. 16):
  - Scenario 1: improved lazy-PRM roadmap 2.76 s, search 39.6 s, mean length 2417 mm, cost 284.1; lazy-PRM 11.5 s / 121 s / 2658 mm / 398.2; RRT* search 1480 s, cost 1767.1; AB-RRT* search 2022 s, cost 1160.7.
  - Scenario 2: improved 3.90 s / 99.3 s / 1826 mm / 142.9; lazy-PRM 4.04 s / 66.2 s / 2158 mm / 143.0; AB-RRT* found the shortest minimum path (1728 mm) but with long search time (1236 s) and high variance.
  - Parameter studies (Tables 3–5): 600 samples, repulsion level 13, μ = 1 best in scenario 1; without repulsion (μ = 0) feasible paths are hard to find in limited time.
- **Real application (§5)**: three stiffened-plate workpieces (4, 2 and 4 seams, Fig. 12), 500 + 500 samples, repulsion level 2, μ = 5, torch lift 50 mm or 200 mm; mean planning time 10.5 s, 18.6 s and 26.1 s over 10 runs (Table 6), "less than one minute" per workpiece; workpiece 2 used the measured (non-ideal) pose; transition points incl. external-axis positions in Table 7; verified in FANUC ROBOGUIDE and in a real welding run (Figs. 14–15), MoveL for seams/lifts, MoveJ for transitions.
- Future work stated: algorithmic weld sequencing; multiple workpieces; **multi-robot cooperation** when one robot cannot reach the whole table.

## Relevance for Plan4ARI
- Same functional block as our **transfer planner** (VAMP, [[sources/thomason2024vamp]]): transitions between seams, approach/retract, with the seam itself treated as fixed. The workflow "scan → rigidly update the known model → replan transfers" matches our station-level use; its numbers (seconds to tens of seconds in MATLAB) set a weak baseline that a vectorised CPU planner should beat by orders of magnitude.
- Useful design elements: torch-only posture nudging (a cheap local repair analogous to sampling the cone/roll in MPPI), inflated-obstacle safety margin as a cost, IK branch selection that penalises proximal-joint motion, and a 7-DOF chain with a **linear external axis** like our optional rail.
- It confirms the problem split of our design: seam following and transitions are separate sub-problems with different planners ([[sources/demaeyer2021weldbenchmark]]).
- Not covered and needed by us: obstacle avoidance *during* the weld under tolerance (our MPPI look-ahead), travel-speed constraints, reconfiguration with restart overlap.

## Critical assessment (our view)
- Despite the title, avoidance is not online/reactive: obstacles are static, the workpiece pose is measured once, and planning takes 10–100+ s in MATLAB; no dynamic obstacles or humans.
- Planning in TCP space with random orientations then IK per interpolated point leaves joint-space continuity to heuristics (branch selection rule); posture adjustment explicitly may change torch poses, and the seam's own feasibility (reachability, singularities, joint limits along the weld) is assumed rather than checked.
- 10 mm voxels and integer repulsion levels are coarse for torch-in-corner clearances; the composite cost mixes seconds and millimetres with arbitrary weights, so rankings depend on the weighting.
- Statistics are 20 (sim) or 10 (real) runs on few scenarios; the RRT* baselines appear poorly tuned (search times of 10³ s), which inflates the reported advantage.

## Links
- [[comparisons/welding-mppi-design-review]]
- [[applications/industrial-manipulators]]
- [[concepts/constraints-and-safety]]
- Related: [[sources/thomason2024vamp]], [[sources/demaeyer2021weldbenchmark]], [[sources/demaeyer2017descartes]], [[sources/tang2023dualrobotweld]] (dual-robot welding allocation; cites this work), [[sources/wang2026torchposture]], [[sources/peng2026ringwelding]]
- BibTeX key: `zhou2022weldavoidance` in `latex/references.bib`
