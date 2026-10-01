---
key: yin2024dprealtime
title: "Dynamic Programming-Based Offline Redundancy Resolution of Redundant Manipulators Along Prescribed Paths with Real-Time Adjustment"
authors: "Yin, Zhihang; Wu, Fa; Wang, Ziqian; Yang, Jianmin; Tan, Jiyong; Kong, Dexing"
year: 2024
venue: "arXiv preprint arXiv:2411.17052"
arxiv: 2411.17052
doi: 
pdf: raw/papers/yin2024dprealtime.pdf
text: raw/text/yin2024dprealtime.txt
tags: [redundancy-resolution, dynamic-programming, path-planning, manipulators]
status: read
---

# Dynamic Programming-Based Offline Redundancy Resolution of Redundant Manipulators Along Prescribed Paths with Real-Time Adjustment

*Yin, Zhihang; Wu, Fa; Wang, Ziqian; Yang, Jianmin; Tan, Jiyong; Kong, Dexing* (2024). arXiv preprint arXiv:2411.17052.

## TL;DR
Offline DP redundancy resolution that leaves room for **online path correction**. The prescribed Cartesian path of a 7-DoF Franka may be shifted at run time along the tool z-axis by a bounded parameter y (contact-force regulation in ultrasound scanning). Offline, a backward DP over (path index, q7 grid value, discretised y) computes for every node the largest per-step change of y that can be tolerated from there to the end of the path without violating joint position/velocity limits, plus a lookup policy giving the next joint configuration from the current one. Online, any y sequence whose step changes stay below that global bound is guaranteed to be executable: offline look-ahead combined with sensor-driven online correction.

## Method
- **Problem (§2)**: path {T_EE,i} with n+1 samples; online offset T̂_EE,i(y_i) = original translation + y_i·Z_i (Eq. 2), with y discretised into 2o+1 values b_−o … b_o (index c_i). Goal: the maximum integer d and an IK map q_i = f⁻¹(T̂_EE,i(b_ci), q_{i−1}) such that **every** index sequence with c_0 = 0 and |c_i − c_{i−1}| ≤ d yields joint paths within position and velocity limits (Eq. 3–5). Acceleration and jerk are handled later by motion compensation.
- **IK (§3.1)**: as in [[sources/yin2024dpbreakpoints]], q7 is the parameter of an analytic IK with a single branch (multiplicity removed by joint-range restriction); configurations with a singular Jacobian are discarded; q7 grid of m values. Feasibility is shown as a 3-D (t, y, q7) map (Fig. 4).
- **DP (§3.2, Alg. 1)**: L(i,j,k) = largest tolerated per-step index change for the sub-path starting at configuration q̄_{i,j,k}. Backward recursion from i = n−1: L(i,j,k) ≥ s iff for every admissible offset change e with |e| ≤ s there is a velocity-feasible successor q̄_{i+1,j_e,k+e} with L(i+1, j_e, k+e) ≥ s (inductive argument in §3.2). The successor with maximal L is stored as the policy (Eq. 14). The global bound d_max = max_j L(0, j, 0) also selects the start configuration. Stated complexity: O(m²·n·o²).
- **Online (end of §3.2, §3.3, Alg. 2)**: at each sampling point the adjustment index c_i is read from the sensor and the stored successor is looked up; a jerk/acceleration/velocity-clipping compensation law (same as in the companion paper) interpolates at 1 kHz. To allow recovery from tracking deviations, the DP is run with a reduced velocity limit q̇_max2; Eq. 17 gives the worst-case joint error and return time as functions of q̇_max and q̇_max2.

## Evidence
- Platform: Franka Emika 7-DoF, 1 kHz; joint limits including jerk in Table 1.
- §4.1, Fig. 6–10: circle of radius 0.1 m over 10 s (Eq. 9); the proposed method completes the circle in simulation and on the real robot with all normalised joint quantities within limits (Fig. 7). The Franka Cartesian pose generator first halts because of velocity/acceleration limits and, with a softened speed profile, stops just after mid-path when q7 reaches its lower limit (Fig. 8–9). The authors note that q7 must sweep from its maximum to its minimum along the circle, so start and end configurations differ although the pose is the same.
- §4.2, Fig. 11–13: practical test with a spring-mounted model probe and a distance sensor; path of **101 sampling points**, **0.1 s** between samples, **maximum adjustment b_o = 0.05 m**; the arm follows vertical hand motions in real time. Tracking error with respect to the DP-desired path is of the order of **1e-3 m**, larger at start/end (acceleration from / deceleration to rest) and larger on hardware than in simulation.
- **Not reported**: the grid sizes m and o used, the d_max obtained, the value of q̇_max2, and any offline computation time or memory.
- Authors' stated limitations (§5): the path cannot be smoothed beforehand because it is not known in advance; frequent accelerations/direction changes produce errors and vibrations, so performance degrades on complex paths.

## Relevance for Plan4ARI
- **Offline guarantee + online freedom** is the same structure as our design: a deterministic DP over the seam provides a feasibility "funnel", and the online layer (MPPI over the ~10 cm look-ahead) may deviate within it. L(i,j,k) is effectively a **robustness margin / viability cost-to-go** that an MPPI rollout could use as terminal cost or constraint: stay in nodes from which the remaining seam is still traversable under bounded disturbances.
- The disturbance axis here (offset along the tool axis) maps naturally to our seam-tracking corrections (sensor-measured offsets of the seam point) and to the ±10 % travel-speed band; a DP margin over these would show where the plan is fragile and where a reconfiguration should be scheduled early.
- The policy table (next configuration as a function of current configuration and measured offset) is a cheap deterministic fallback when MPPI fails to find a feasible rollout.

## Critical assessment (our view)
- Only one disturbance dimension (y along Z), one redundancy parameter (q7), a single IK branch, and no breakpoints: if no feasible successor exists the node is simply stuck (L = 0). Combining this with the breakpoint DP of the companion paper is not attempted.
- The max-min objective (largest uniform tolerance) ignores quality costs (smoothness, manipulability, torch angle); a single global d is conservative, a per-index tolerance would be more useful for welding.
- Only position and velocity limits in the DP; acceleration/jerk are enforced only by online clipping, which causes tracking errors (order 1e-3 m here, probably too large for welding without a seam-tracking loop).
- No collision checking, no mobile base, no timing data; evaluation on one circular path plus a qualitative hand-following demo, no comparison with other robust or online redundancy-resolution methods.
- Scaling to our case (task-space redundancy in a cone, 8 IK branches, optional linear axis) multiplies the grid, and the O(m²·n·o²) complexity grows accordingly.

## Abstract (verbatim, arXiv)
> Traditional offline redundancy resolution of trajectories for redundant manipulators involves computing inverse kinematic solutions for Cartesian space paths, constraining the manipulator to a fixed path without real-time adjustments. Online redundancy resolution can achieve real-time adjustment of paths, but it cannot consider subsequent path points, leading to the possibility of the manipulator being forced to stop mid-motion due to joint constraints. To address this, this paper introduces a dynamic programming-based offline redundancy resolution for redundant manipulators along prescribed paths with real-time adjustment. The proposed method allows the manipulator to move along a prescribed path while implementing real-time adjustment along the normal to the path. Using Dynamic Programming, the proposed approach computes a global maximum for the variation of adjustment coefficients. As long as the coefficient variation between adjacent sampling path points does not exceed this limit, the algorithm provides the next path point's joint angles based on the current joint angles, enabling the end-effector to achieve the adjusted Cartesian pose. The main innovation of this paper lies in augmenting traditional offline optimal planning with real-time adjustment capabilities, achieving a fusion of offline planning and online planning.

## Links
- [[concepts/path-wise-redundancy-resolution]]
- [[comparisons/welding-mppi-design-review]]
- [[concepts/mppi-vs-mpc]]
- [[applications/industrial-manipulators]]
- Companion paper (breakpoints): [[sources/yin2024dpbreakpoints]]
- Related: [[sources/faroni2019pik]], [[sources/zhong2024expansiongrr]], [[sources/razjigaev2025functional]]
- BibTeX key: `yin2024dprealtime` in `latex/references.bib`
