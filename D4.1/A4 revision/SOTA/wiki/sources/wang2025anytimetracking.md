---
key: wang2025anytimetracking
title: "Anytime Planning for End-Effector Trajectory Tracking"
authors: "Wang, Yeping; Gleicher, Michael"
year: 2025
venue: "IEEE Robotics and Automation Letters, vol. 10, no. 4, pp. 3246-3253"
arxiv: 2502.03676
doi: 10.1109/lra.2025.3540633
pdf: raw/papers/wang2025anytimetracking.pdf
text: raw/text/wang2025anytimetracking.txt
tags: [redundancy-resolution, path-planning, orientation-tolerance, inverse-kinematics, welding, manipulators]
status: read
---

# Anytime Planning for End-Effector Trajectory Tracking

*Wang, Yeping; Gleicher, Michael* (2025). IEEE Robotics and Automation Letters, vol. 10, no. 4, pp. 3246-3253.

## TL;DR
Turns **Descartes-style layered-graph trajectory tracking** (IK samples per waypoint as vertices, feasible joint moves as edges, shortest path) into an **anytime** algorithm. Instead of sampling hundreds of IK solutions per waypoint up front, it samples sparsely every s waypoints, connects them with "sparse edges" to get a cheap **guide path**, then densifies the graph by sampling IK solutions around the guide path (plus an equal number of uniform samples) and searches dense edges for a real solution; repeat. Applied to Stampede (min joint movement) and IKLink (min **number of reconfigurations**, then joint movement), including a **welding task with free torch roll** via RangedIK. Same or better quality in less time than the conventional and naïve-anytime variants; open-source (Rust, IKLink).

## Method
- Problem (§III-A): track a time-stamped pose sequence; edges valid if the joint move fits velocity limits in the time step; **reconfiguration** = deliberate joint discontinuity where the robot pauses, relocates and resumes (counted as a primary cost in IKLink).
- Baselines: conventional sequential framework (sample m IK per waypoint — e.g. m=250 Stampede, 300 IKLink — build graph, search); naïve anytime (incremental random sampling).
- **Guided anytime framework** (§III-D, §IV, Alg. 1–4):
  1. sparse vertex sampling (m0 IK solutions every s waypoints);
  2. sparse edges between layers s apart (linear joint motion within velocity limits);
  3. guide path = shortest path over sparse + dense edges;
  4. additional sampling: interpolate along each sparse edge, perturb (δ), solve IK seeded there; plus the same number of uniform random IK samples (softmax favouring under-sampled waypoints) to retain worst-case convergence to the conventional framework;
  5. dense edges between adjacent layers; sparse edges pruned when a dense path of similar cost (factor η) exists (lazy-planning flavour);
  6. solution = shortest path on dense edges only; monotone improvement over iterations.
- Framework is agnostic to IK sampler, edge cost and graph-search algorithm (value iteration, DP, Dijkstra).

## Evidence
- Implementation: Rust (IKLink library); md=5, δ=0.2, η=1.1; m0=50 (Exp. A, B), m0=500 (Exp. C); Intel i7-11800H laptop (§V).
- **Exp. A** (Stampede, KUKA iiwa 7-DoF, 10 random curves of ~379 waypoints + "hello" writing; Table I): time to match baseline quality 1.8 s (s=5) vs 20.5 s conventional and 7.1 s naïve; initial solutions about 2× faster (Fig. 3).
- **Exp. B** (IKLink, Franka Panda 7-DoF, random curves ~678 waypoints + 3D scanning; Table I): 13.6 s vs 58.2 s (conventional) / 58.9 s (naïve) on testbed 1; reconfigurations within baseline time 1.3 vs 1.8.
- **Exp. C — tolerances** (IKLink + RangedIK, free rotation about the tool axis; Table I): testbed 1 = 10 random **welding trajectories** on a Panda, torch axis at 45° from the last joint axis, ~647 waypoints, 1.29 m: reconfigurations 0.4 (s=5) vs 0.9 for both baselines within baseline time; time to match baseline 14.6–28.7 s (s=10 / s=3) vs 38.3 s. Testbed 2 = sanding spiral on a 7-DoF Sawyer (tool axis 90° from last axis): 0.8 vs 2.6 (conventional) / 2.9 (naïve) reconfigurations; 24.6 s vs 41.6 s.
- Step size s trades initial-solution delay vs guide-path accuracy; sweet spot s=5 (§V summary).
- Limits stated by the authors (§VI): no quality-based stopping rule; heuristic may mislead (can be slower than naïve); only joint-velocity constraints, no acceleration/dynamics; demonstrated on two algorithms only.

## Relevance for Plan4ARI
- This is the **graph-based ("Descartes-like") anytime baseline** requested for the welding design ([[comparisons/welding-mppi-design-review]], flaw #24; [[sources/demaeyer2017descartes]]). Its objective in IKLink — fewest reconfigurations first, then joint motion — is the same lexicographic objective as our "fewest detach/reconfigure cycles", and Exp. C is literally torch-roll-free welding tracking.
- The **guide path** idea maps onto our design: a coarse sparse-layer search over the whole seam segment can provide (i) cost-to-go/terminal values for the MPPI modes (open flaw #3) and (ii) nominal null-space seeds and branch pruning for the ≤8 goals.
- Anytime property fits a station-level pre-computation (seconds to tens of seconds per seam) followed by online MPPI refinement.

## Critical assessment (our view)
- Times of 10–40 s per trajectory on a laptop CPU are fine for offline/station planning, not for a 10–100 Hz loop; MPPI remains the online layer.
- Only velocity-feasibility edges; our ±10% travel-speed band, accelerations and torch-hose wrap would need additional edge costs/constraints.
- Tested on 7-DoF arms (redundant) or with a single free roll; a 2-D tilt cone on a 6-DoF industrial arm (our case) enlarges the IK sample space and was not tested — though RangedIK supports it.
- Reconfigurations are counted but their execution (retract, transfer, approach, overlap 1 cm back) is not planned or costed; we still need VAMP-style transfers ([[sources/thomason2024vamp]]).
- Sampling IK via local optimisation (RelaxedIK/RangedIK) does not guarantee covering all branches; for a 6R arm with analytic IK, enumerating all branches per sample is cheaper and complete (see [[sources/elias2025cuspidal]]).

## Abstract (verbatim, arXiv)
> End-effector trajectory tracking algorithms find joint motions that drive robot manipulators to track reference trajectories. In practical scenarios, anytime algorithms are preferred for their ability to quickly generate initial motions and continuously refine them over time. In this paper, we present an algorithmic framework that adapts common graph-based trajectory tracking algorithms to be anytime and enhances their efficiency and effectiveness. Our key insight is to identify guide paths that approximately track the reference trajectory and strategically bias sampling toward the guide paths. We demonstrate the effectiveness of the proposed framework by restructuring two existing graph-based trajectory tracking algorithms and evaluating the updated algorithms in three experiments.

## Links
- [[concepts/path-wise-redundancy-resolution]]
- [[comparisons/welding-mppi-design-review]]
- [[applications/industrial-manipulators]]
- Related: [[sources/demaeyer2017descartes]], [[sources/wang2023rangedik]], [[sources/yin2024dpbreakpoints]], [[sources/zhong2024expansiongrr]], [[sources/elias2025cuspidal]], [[sources/chen2025cooptimization]]
- BibTeX key: `wang2025anytimetracking` in `latex/references.bib`
