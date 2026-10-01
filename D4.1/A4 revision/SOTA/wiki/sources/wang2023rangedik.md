---
key: wang2023rangedik
title: "RangedIK: An Optimization-based Robot Motion Generation Method for Ranged-Goal Tasks"
authors: "Wang, Yeping; Praveena, Pragathi; Rakita, Daniel; Gleicher, Michael"
year: 2023
venue: "2023 IEEE International Conference on Robotics and Automation (ICRA), pp. 9700-9706"
arxiv: 2302.13935
doi: 10.1109/icra48891.2023.10161311
pdf: raw/papers/wang2023rangedik.pdf
text: raw/text/wang2023rangedik.txt
tags: [inverse-kinematics, orientation-tolerance, redundancy-resolution, manipulators]
status: read
---

# RangedIK: An Optimization-based Robot Motion Generation Method for Ranged-Goal Tasks

*Wang, Yeping; Praveena, Pragathi; Rakita, Daniel; Gleicher, Michael* (2023). 2023 IEEE International Conference on Robotics and Automation (ICRA), pp. 9700-9706.

## TL;DR
Per-instant (one configuration per control update) optimisation-based IK, extending RelaxedIK, in which every kinematic requirement is a **task** with either a specific goal, a **range of equally valid goals**, or a **range with a preferred goal**. Ranges (e.g. Cartesian tolerances on tool tilt or position) are encoded by smooth relaxed-barrier loss functions ("Swamp", "Swamp Groove") inside a weighted-sum objective, so the solver uses the tolerance to improve smoothness, manipulability and feasibility of other tasks. Compared with RelaxedIK and Trac-IK on UR5 and Sawyer benchmarks with tolerances; open-source (built on the CollisionIK library).

## Method
- Problem (§III): q* = argmin Σ_j w_j f_j(χ_j(q)) subject to joint bounds (Eq. 4–5); future goals unknown (purely reactive).
- **Basic losses** (§IV-A): negative Gaussian (normalisation), Wall (flat inside [l,u], steep at boundaries, Eq. 7), polynomial (gradients far from goal).
- **Parametric losses** (§IV-B): Groove for specific goals (Eq. 9); **Swamp** = Wall surrounded by polynomial funnel for equally-valid ranges (Eq. 10); **Swamp Groove** for a range with preferred goal, preferred value need not be centred (Eq. 11). All smooth and defined outside the feasible set (relaxed barrier, unlike strict log barriers).
- **Tasks** (§IV-C): per-axis end-effector position/rotation error in the goal frame (Eq. 12–13, can be ranged); joint velocity/acceleration as ranged-with-preference (limits, prefer zero), jerk as specific goal zero; self-collision as ranged distances ≥ 0.02 m between capsules; Yoshikawa manipulability maximisation.
- Solver: PANOC (proximal averaged Newton-type method); Trac-IK baseline is seeded with the previous configuration.

## Evidence
- Setup (§V): Intel i7-11800H; simulated UR5 (6-DoF) and Sawyer (7-DoF); four benchmarks with Cartesian tolerances (Table I): writing (tip exact, tilt ±π/6 about x,y, free z-rotation), spraying (±0.05 m in plane), wiping (free z-rotation), filling water. Each path 2,000 goal poses at 30 Hz, 10 repetitions; 480,000 solutions in total.
- Results (Table II), UR5: mean joint acceleration 0.0269 (RangedIK) vs 0.0299 (RelaxedIK) vs 1.9333 rad/s² (Trac-IK); mean jerk 0.224 vs 0.336 vs 115.536 rad/s³; manipulability 0.0544 vs 0.0533 vs 0.0487; joint movement 16.747 vs 20.097 vs 24.195 rad. Sawyer shows the same ordering (jerk 0.290 vs 0.328 vs 88.930). Zero tolerance violations for all three methods; Trac-IK has the smallest position/rotation error (order 1e-6) but choppy motion, because its tolerance mapping is discontinuous (Eq. 16).
- Physical demo (§VI): camera-in-hand robot using a ranged "look-at" task for smoother video (qualitative).
- **No per-solve computation time is reported** in the paper.
- Limits stated by the authors (§VII-A): no foresight (only the current instant), local minima of nonlinear optimisation, weights/parameters need scenario-specific tuning.

## Relevance for Plan4ARI
- Gives a ready-made, smooth **cost shape for tolerance cones**: the torch-axis ~10° cone (possibly anisotropic → separate per-axis ranges for work and travel angle), free roll (infinite range), and the ±10% speed band (ranged-with-preference around nominal speed) can all be expressed as Swamp/Swamp-Groove terms. These are directly reusable as MPPI running costs in [[comparisons/welding-mppi-design-review]], avoiding the hard-threshold chattering we flagged.
- Usable as the **inner per-point IK / projection** in rollouts or as the greedy baseline: it is what [[sources/wang2025anytimetracking]] uses as IK sampler for tolerance-constrained (welding) tracking.
- Its stated limitation — no look-ahead — is precisely what a horizon-based method (MPPI, DP, graph search) adds.

## Critical assessment (our view)
- Single-instant method: cannot anticipate joint limits or branch infeasibility along the seam; as a welding baseline it represents the "myopic" end of the spectrum (cf. functional IK [[sources/razjigaev2025functional]]).
- Tolerances are soft (penalties): zero violations were observed in the benchmarks, but there is no guarantee; for the exact seam point we still need exact IK or projection (design-review flaw #10).
- Per-axis Euler-like rotation errors in the goal frame (Eq. 13) approximate a cone as a box in tilt angles; a true circular/elliptical cone needs a custom task function (easy to add in this framework).
- No timing figures, so real-time claims cannot be compared with our budget without re-benchmarking.

## Abstract (verbatim, arXiv)
> Generating feasible robot motions in real-time requires achieving multiple tasks (i.e., kinematic requirements) simultaneously. These tasks can have a specific goal, a range of equally valid goals, or a range of acceptable goals with a preference toward a specific goal. To satisfy multiple and potentially competing tasks simultaneously, it is important to exploit the flexibility afforded by tasks with a range of goals. In this paper, we propose a real-time motion generation method that accommodates all three categories of tasks within a single, unified framework and leverages the flexibility of tasks with a range of goals to accommodate other tasks. Our method incorporates tasks in a weighted-sum multiple-objective optimization structure and uses barrier methods with novel loss functions to encode the valid range of a task. We demonstrate the effectiveness of our method through a simulation experiment that compares it to state-of-the-art alternative approaches, and by demonstrating it on a physical camera-in-hand robot that shows that our method enables the robot to achieve smooth and feasible camera motions.

## Links
- [[concepts/path-wise-redundancy-resolution]]
- [[concepts/constraints-and-safety]]
- [[comparisons/welding-mppi-design-review]]
- [[applications/industrial-manipulators]]
- Related: [[sources/wang2025anytimetracking]], [[sources/razjigaev2025functional]], [[sources/demaeyer2017descartes]], [[sources/chen2025cooptimization]], [[sources/lu2022toolorientation]]
- BibTeX key: `wang2023rangedik` in `latex/references.bib`
