---
key: yin2024dpbreakpoints
title: "Dynamic Programming-Based Redundancy Resolution for Path Planning of Redundant Manipulators Considering Breakpoints"
authors: "Yin, Zhihang; Wu, Fa; Bian, Ruofan; Wang, Ziqian; Yang, Jianmin; Tan, Jiyong; Kong, Dexing"
year: 2024
venue: "arXiv preprint arXiv:2411.17034"
arxiv: 2411.17034
doi: 
pdf: raw/papers/yin2024dpbreakpoints.pdf
text: raw/text/yin2024dpbreakpoints.txt
tags: [redundancy-resolution, dynamic-programming, path-planning, manipulators, breakpoints]
status: read
---

# Dynamic Programming-Based Redundancy Resolution for Path Planning of Redundant Manipulators Considering Breakpoints

*Yin, Zhihang; Wu, Fa; Bian, Ruofan; Wang, Ziqian; Yang, Jianmin; Tan, Jiyong; Kong, Dexing* (2024). arXiv preprint arXiv:2411.17034.

## TL;DR
Offline, path-wise redundancy resolution for a 7-DoF Franka arm following a time-stamped Cartesian path (robotic ultrasound). The redundancy is parameterised by q7 (closed-form IK for the remaining 6 joints), q7 is discretised into m values per path point, and a dynamic programme over pairs of consecutive grid nodes finds the globally optimal joint path (for that grid) under joint position, velocity **and acceleration** limits. When no continuous path exists, a large penalty M per interruption makes the same DP return the **minimum number of breakpoints** and their optimal placement; for closed (circular) paths a variant also picks the start point that removes one breakpoint. A real-time interpolation/compensation layer brings sparse DP waypoints to the 1 kHz controller under jerk limits.

## Method
- **Problem (§2)**: path sampled at fixed t0 (pose and time prescribed, i.e. fixed Cartesian speed); constraints Eq. 4 on q, q̇, q̈ via finite differences (Eq. 3). Cost Eq. 5: sum of squared joint increments for continuous steps plus a constant M for each interrupted step, with M > n‖q_max − q_min‖², so that L/M (integer part) = number of breakpoints — lexicographic "fewest breakpoints first, then smoothness".
- **IK parameterisation (§3.1)**: q7 as redundancy parameter (He & Liu analytic IK). Of the up to 8 IK solutions for a given q7, the multiplicity is **removed by restricting joint ranges** so that the map (T_EE, q7) → q is bijective, i.e. a single IK branch is kept. The q7 range is split into m values → grid of m(n+1) candidate configurations; infeasible nodes appear as holes in a (t, q7) feasibility map (Fig. 2, 3).
- **DP (§3.2, Alg. 1)**: state = (current node j, previous node k) so that acceleration can be checked; value L̃(i,j,k) built from L̂(i,j,k,p) (Eq. 13–19). Velocity violation → infinite cost; if velocity/acceleration over the triple fails, the path is "broken" between i−2 and i−1, adding M to the best predecessor value (Eq. 16–18). Backtracking gives the globally optimal sequence for the given discretisation (the authors refer to a proof in an Appendix B that is not in the arXiv text).
- **Breakpoint semantics**: a breakpoint is a step where the arm stops at q̄_{i−2,p} and then re-orients to q̄_{i,j} before restarting ("interruption and re-orientation", §1). The transfer motion itself is **not** planned or costed beyond M; the DP chooses *where* to break so that the global cost is minimal, rather than breaking only when stuck.
- **Start-point modification (§3.3, Alg. 2)**: for closed paths the path is duplicated (2n points) and the penalty is re-coded (Eq. 20) so the DP also returns the earliest start index after the first interruption; the authors show that changing the start can reduce the breakpoint count by at most one.
- **Interpolation / motion compensation (§3.4, Alg. 3)**: DP run on a coarse set of points; between them an online law computes desired q̇, q̈ and jerk from the measured state and clips jerk → acceleration → velocity, with a "cautionary" velocity and shrunk joint limits as braking margin, plus stopping constraints (Eq. 22).

## Evidence
- Platform: Franka Emika 7-DoF, 1 kHz host communication; joint limits in Table 1. Test paths: circle of radius 0.1 m with the tool axis vertical, duration 10 s (Eq. 8: accelerate–decelerate profile; Eq. 9: constant angular rate).
- §4.1, Fig. 4–6: DP with **100 path points per second and m = 4000** completes the full circle in simulation and on the real robot; the Franka built-in Cartesian pose generator (local IK) drives q7 to its lower limit and stops mid-path.
- §4.2, Fig. 7–8: interpolated joint trajectories respect normalised position, velocity, acceleration and jerk limits; mean end-effector position error 2.5101e-6 m (DP at 100 points/s) vs 6.7442e-6 m (10 points/s); error accumulation is observed at some points at 100 points/s.
- §4.3, Fig. 9–11: on the constant-rate circle, Alg. 1 yields a discontinuity (large detour of the arm), whereas Alg. 2 finds a new start point that gives a breakpoint-free joint path.
- **No computation times, memory figures or complexity statement are reported.** Our reading of Alg. 1: the (j, k, p) loops imply on the order of n·m³ transition evaluations before velocity pruning, which with m = 4000 explains the authors' concern about "computational and memory requirements" (§1.1) and their use of sparse points plus interpolation.

## Relevance for Plan4ARI
- **Breakpoints = our reconfigurations.** The M-penalty trick (cost = M·#breaks + smoothness) is exactly the lexicographic objective we want for welding: first minimise the number of stop–retract–reconfigure–approach cycles, then optimise quality. It is a ready-made deterministic baseline for (c) and a reference to check whether the MPPI look-ahead takes reconfiguration decisions at the right places.
- **Segmentation / cost-to-go (b)**: the DP value table over (seam index, redundancy grid) gives, for any node, the minimal remaining number of breaks; it can serve as terminal cost or goal-set selection for the ~10 cm MPPI window, and its breakpoints give the segment boundaries where VAMP transfer motions are inserted.
- The fixed-time sampling with q̇/q̈ limits corresponds to our constant travel speed (±10 %); the speed band could be an extra DP dimension or be left to the downstream MPC.
- The start-point modification for closed paths applies directly to closed weld seams (e.g. around stiffeners or pipes).

## Critical assessment (our view)
- **Single IK branch**: branch multiplicity is suppressed by joint-range restriction, so switching between the up to 8 IK solutions (our "configuration change") is not represented. For us each branch must be a separate layer of the grid, with breakpoints allowed between layers (cost = retract/approach time instead of a constant M).
- **One-dimensional redundancy (q7)** of an intrinsically redundant 7-DoF arm. Our redundancy is task-space (free roll, torch axis in a ~10° possibly anisotropic cone) on a 6-DoF arm, possibly plus a linear 7th axis: 3–4 grid dimensions, so the m³-type transition cost explodes; coarser grids, pruning or cascaded/hierarchical DP would be needed.
- The breakpoint model is crude: constant M, no transfer-motion cost, no collision checking, no restart overlap (our ~1 cm back-off), and the stop happens at an existing path point.
- No collision avoidance or workpiece/environment model, no base placement (AGV), no explicit singularity treatment.
- Thin experimental evidence: two synthetic circles on one robot, no timing, no comparison with other DP redundancy-resolution methods (e.g. Ferrentino et al., cited by the authors); the referenced Appendix B is missing from the arXiv version and §4 cites equation numbers inconsistently.
- Authors' framing: the cost is chosen for simplicity and can be replaced; global optimality holds only for the given discretisation m.

## Abstract (verbatim, arXiv)
> This paper proposes a redundancy resolution algorithm for a redundant manipulator based on dynamic programming. This algorithm can compute the desired joint angles at each point on a pre-planned discrete path in Cartesian space, while ensuring that the angles, velocities, and accelerations of each joint do not exceed the manipulator's constraints. We obtain the analytical solution to the inverse kinematics problem of the manipulator using a parameterization method, transforming the redundancy resolution problem into an optimization problem of determining the parameters at each path point. The constraints on joint velocity and acceleration serve as constraints for the optimization problem. Then all feasible inverse kinematic solutions for each pose under the joint angle constraints of the manipulator are obtained through parameterization methods, and the globally optimal solution to this problem is obtained through the dynamic programming algorithm. On the other hand, if a feasible joint-space path satisfying the constraints does not exist, the proposed algorithm can compute the minimum number of breakpoints required for the path and partition the path with as few breakpoints as possible to facilitate the manipulator's operation along the path. The algorithm can also determine the optimal selection of breakpoints to minimize the global cost function, rather than simply interrupting when the manipulator is unable to continue operating. The proposed algorithm is tested using a manipulator produced by a certain manufacturer, demonstrating the effectiveness of the algorithm.

## Links
- [[concepts/path-wise-redundancy-resolution]]
- [[comparisons/welding-mppi-design-review]]
- [[applications/industrial-manipulators]]
- Companion paper (same group, real-time adjustment): [[sources/yin2024dprealtime]]
- Related: [[sources/faroni2019pik]], [[sources/zhong2024expansiongrr]], [[sources/razjigaev2025functional]]
- BibTeX key: `yin2024dpbreakpoints` in `latex/references.bib`
