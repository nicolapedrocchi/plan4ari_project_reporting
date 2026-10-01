---
key: chen2025cooptimization
title: "Co-Optimization of Tool Orientations, Kinematic Redundancy, and Waypoint Timing for Robot-Assisted Manufacturing"
authors: "Chen, Yongxue; Zhang, Tianyu; Huang, Yuming; Liu, Tao; Wang, Charlie C. L."
year: 2025
venue: "IEEE Transactions on Automation Science and Engineering, vol. 22, pp. 12102-12117"
arxiv: 2409.13448
doi: 10.1109/tase.2025.3542218
pdf: raw/papers/chen2025cooptimization.pdf
text: raw/text/chen2025cooptimization.txt
tags: [redundancy-resolution, orientation-tolerance, path-planning, manipulators, industrial, trajectory-optimization]
status: read
---

# Co-Optimization of Tool Orientations, Kinematic Redundancy, and Waypoint Timing for Robot-Assisted Manufacturing

*Chen, Yongxue; Zhang, Tianyu; Huang, Yuming; Liu, Tao; Wang, Charlie C. L.* (2025). IEEE Transactions on Automation Science and Engineering, vol. 22, pp. 12102-12117.

## TL;DR
Offline, deterministic trajectory optimiser that treats **tool orientation (within cones), kinematic redundancy (roll + positioner joints) and per-waypoint timing** as one nonlinear program over the whole toolpath, minimising a joint velocity/acceleration/jerk smoothness integral under joint, orientation-cone, tool-tip speed/acceleration and total-time constraints. Toolpaths of up to ~8k waypoints are handled by an **overlapping block decomposition** (two staggered sets of independent 100-waypoint sub-problems solved in parallel by SQP/OSQP), initialised by a graph search over roll angle and IK configuration. Demonstrated on an ABB IRB-2600 + 2-axis positioner for multi-axis additive manufacturing; code is public.

## Method
- **Kinematic model** (§II-A): tool-tip position fixed at waypoint p_i; free variables per waypoint θ_i = [ω_i (exponential coords of tool orientation, 3), q_B (positioner, 2)] ∈ R⁵; robot joints from analytic IK of one of the **eight configurations μ**, fixed for the whole path (Eq. 13). Single-robot (6-DoF) variant in §IV-C.
- **Time as variable** (§II-B): segment durations t_i are optimised; velocity/acceleration/jerk by unevenly-spaced finite differences (Eq. 5, App. A).
- **Objective** (Eq. 6–7): Σ (k_v‖v‖² + k_a‖a‖² + k_j‖j‖²)·Δs, normalised by initial-solution range (Eq. 56; k_v=0.1, k_a=0.5, k_j=1).
- **Constraints** (Eq. 13–22): joint position/velocity/acceleration/jerk limits; learned collision proxy Γ(q) (Fastron); **orientation cones** as dot-product inequalities (tool axis vs gravity ≤ α, layer normal vs gravity ≤ β, tool vs layer normal ≤ γ); tool-tip speed, tangential and normal acceleration bounds; extrusion-rate lower bound on t_i; total time ≤ t_u.
- **Initialisation** (§III-A): nominal orientations, then **graph-based optimisation over roll angle η and configuration μ** (from their earlier work), FCL collision repair, timing from joint-speed bounds (Eq. 23).
- **Decomposition** (§III-B, Alg. 1): sub-problems DS(a,b) over ζ=100 waypoints with 2-waypoint coupling margins; two staggered sets S1/S2 solved alternately (block-coordinate-descent-like), each set in parallel; τ=0.001, k_max=5.
- **Sub-problem solver** (§III-C): SQP with analytic linearisation (Jacobian-based ∂q/∂ω, Eq. 30–36), sparse QP via OSQP.
- **Result correction** (§III-D): exact collision check; bisection between optimised and initial θ_i if a collision remains.
- Generalisation (§IV-C): time can be fixed (prescribed speed) or replaced by arc length (geometric smoothness only).

## Evidence
- Platform: ABB IRB-2600 (6-DoF) + ABB IRBP-A positioner (2-DoF), C++, Intel i9 3 GHz, 32 GB RAM (§V). Single 6-DoF robot with fixed nozzle in Example IV.
- **Example I** (7,497 waypoints; α=20°, β=8°, γ=12°), ablation (Table I, Fig. 7): smoothness objective 4.48 → 0.28 (−93.75%) with R+O+T; max joint vel/acc/jerk 0.55 / 2.82 / 43.12 vs limits 0.60 / 5.00 / 50.00. Partial variants (R only, R+O, R+T) end at 0.39–0.42 and violate acceleration and/or jerk limits.
- Decomposition (Fig. 8, first 1,000 waypoints): 1,780.15 s without vs 111.95 s with decomposition (>93% faster); full path without decomposition ran out of memory.
- Sensitivity (Fig. 9, 500 waypoints): convergence robust near the graph-search initial guess; fixed roll η = 90° or 270° fails to reach the optimum.
- Physical vibrations (Table II): average measured end-effector acceleration reduced by 12.12% (robot) and 19.95% (positioner).
- **Example II** (1,987 waypoints, fixed timing, vs local jerk filtering of their prior work): computation 225.36 s → 81.10 s (−64.01%); positioner average acceleration −30.96% (§V-B); the baseline still violated the 60 rad/s³ jerk limit on joint 7 after 120 iterations.
- **Example III** (8,832 waypoints, geometric smoothing on arc length): avoids positioner shaking near its singularity (Fig. 22); printing time 587 s → 534 s with the controller's own speed planning (§V-C).
- Limits stated by the authors (§VI): collision proxy needs up to 5 min of learning and re-learning when the scene changes; optimisation itself < 10 min for ~8k waypoints; final collision correction may lose optimality.

## Relevance for Plan4ARI
- Closest **deterministic, offline baseline** for the welding design ([[comparisons/welding-mppi-design-review]], flaw #24): it co-optimises exactly our three free quantities — orientation inside cones (our ~10° torch cone, also anisotropic via separate inequalities), roll about the tool axis, and timing (our ±10% speed band maps to bounds on t_i or on tool-tip speed, Eq. 20) — over a whole seam.
- The fixed **configuration index μ among eight analytic IK solutions** is the same "IK branch" abstraction we use; branch choice is made once by a graph search in the initialisation, not during optimisation. Branch switches/reconfigurations are not modelled.
- Overlapping-window decomposition is structurally a receding-horizon idea: 100-waypoint windows with coupling margins ≈ our ~10 cm MPPI look-ahead; can be used to produce a global reference / warm start that MPPI tracks online ([[concepts/path-wise-redundancy-resolution]]).
- The 2-axis positioner as extra redundancy is analogous to our optional 7th linear axis.

## Critical assessment (our view)
- Offline: minutes for long toolpaths; not a replanning tool. Use as benchmark ("global optimum on a segment") against MPPI restarts/smoothness, as already planned in the design review's research question.
- Local SQP from a graph-search seed: the result inherits the branch and homotopy of the initial guess (Fig. 9 shows failure from poor seeds). No handling of infeasibility along the path (no detach/reconfigure), whereas our design needs exactly that decision.
- Collision handled via a learned proxy that must be retrained per scene — incompatible with large, changing welding structures unless replaced by sphere/SDF checks.
- Process constraints are AM-specific (gravity, extrusion); for welding they must be replaced by work/travel-angle cones and speed band — the formulation allows it (§II-E).

## Abstract (verbatim, arXiv)
> In this paper, we present a concurrent and scalable trajectory optimization method to improve the quality of robot-assisted manufacturing. Our method simultaneously optimizes tool orientations, kinematic redundancy, and waypoint timing on input toolpaths with large numbers of waypoints to improve kinematic smoothness while incorporating manufacturing constraints. Differently, existing methods always determine them in a decoupled manner. To deal with the large number of waypoints on a toolpath, we propose a decomposition-based numerical scheme to optimize the trajectory in an out-of-core manner, which can also run in parallel to improve the efficiency. Simulations and physical experiments have been conducted to demonstrate the performance of our method in examples of robot-assisted additive manufacturing.

## Links
- [[concepts/path-wise-redundancy-resolution]]
- [[comparisons/welding-mppi-design-review]]
- [[applications/industrial-manipulators]]
- Related: [[sources/lu2022toolorientation]] (cone + singularity, integration-based), [[sources/wang2025anytimetracking]] (graph-based anytime), [[sources/yin2024dpbreakpoints]], [[sources/razjigaev2025functional]], [[sources/elias2025cuspidal]]
- BibTeX key: `chen2025cooptimization` in `latex/references.bib`
