---
key: wang2024constrainedpi
title: "Constrained Sampling-Based MPC using Path Integral for Collision-Free Robot Manipulation"
authors: "Wang, Xingfang; Li, Hui; Wang, Dong; Huang, Xiao; Jiang, Zhihong"
year: 2024
venue: "TechRxiv preprint (not peer reviewed)"
arxiv: 
doi: 10.36227/techrxiv.173398154.46056666/v1
pdf: raw/papers/wang2024constrainedpi.pdf
text: raw/text/wang2024constrainedpi.txt
tags: [mppi-core, constraints, manipulators, hri, equality-constraints]
status: read
---

# Constrained Sampling-Based MPC using Path Integral for Collision-Free Robot Manipulation

*Wang, Xingfang; Li, Hui; Wang, Dong; Huang, Xiao; Jiang, Zhihong* (2024). TechRxiv preprint (not peer reviewed).

> **Status:** TechRxiv preprint posted 2024-12-12, CC-BY 4.0, **not peer reviewed**; numbers below are the authors' and may be preliminary.

## TL;DR
**CSMPC**: MPPI for a 7-DoF arm that enforces **equality hard constraints** (e.g. end-effector moving along a prescribed path with fixed attitude, tool tip fixed while joint 6 circles) by projecting every sampled input/state onto the constraint manifold with a weighted least-norm (Lagrange-multiplier) correction — a null-space projection of the samples. Because the projection is affine and the weights sum to one, the weighted average remains on the constraint. Collision avoidance (skeleton-based distance to point-cloud obstacles) and smoothness (triple exponential smoothing prediction) are soft costs; a time-scheduled **adaptive noise** amplitude increases exploration mid-task and reduces it at start/end. Reported tracking errors ~10⁻⁵ m in simulation and < 0.5 mm on a real Diana7, at ~13 ms per step.

## Method
- Problem (§III, Eq. 14): control-affine robot (x = joint angles, v = joint velocities), linearised state-only equality c₁ + B₁x = 0, state-input equality c₂ + B₂(x)v = 0, inequality h(x) ≥ 0; input bounds by clamping in the dynamics as in standard MPPI.
- Upper level (§III-A): closest point to each sample on the constraint (weighted LS, Eqs. 15–18): x̄ = (I − B₁†B₁)F(x, v) − B₁†c₁ and v̄ = (I − B₂†B₂)v − B₂†c₂ (Eq. 24), with weighted pseudo-inverse. Since Σω = 1 the updated control satisfies the same constraint (Eqs. 25–27).
- Lower level: inequality constraints as costs. Collision (§III-B, Eqs. 29–33): Diana7 reduced to a 3-link skeleton with sphere/cylinder envelopes; point-to-segment distances to depth-camera obstacle points; penalty active below safety distance γ.
- Smoothness (§III-C, Eqs. 34–39): triple exponential smoothing of past states predicts a smooth future sequence; quadratic cost when a rollout deviates beyond threshold μ.
- Adaptive noise (§III-D, Eq. 40): sigmoid ramp of Σ between Σ_min and Σ_max at task start and end (time- or progress-based).
- Weights use the usual baseline subtraction (minimum cost β, Eqs. 11–12).

## Evidence
- Planar 3-link (§IV-A): Δt = 0.02 s, **K = 200 samples, T = 5 steps**; EE constrained to a straight line (Eq. 43), safety distance 0.125 m, goal tolerance 0.5 mm.
- 7-DoF simulation (§IV-B, Fig. 8, Table I; "setup similar" to the planar case): four tasks — reaching with static obstacle; "∞" path with vertical attitude and moving obstacles (Eq. 45); fixed tip with joint-6 circle, polishing-like (Eq. 46); discrete grid-map cost.
- Table I (AMD Ryzen 5 3600X, GTX 1660): time per control step **OCS2 14.83 ms, STORM 12.54 ms, CSMPC 13.12 ms**; max EE error Sim 1: 4.73·10⁻⁵ / 8.18·10⁻⁴ / 3.25·10⁻⁵ m; Sim 2: 1.61·10⁻⁵ / 1.12·10⁻² / 1.56·10⁻⁵ m; Sim 3: OCS2 2.44·10⁻⁵, STORM collides/fails, CSMPC 1.45·10⁻⁵ m; Sim 4: OCS2 not applicable (discrete cost).
- Real Diana7 (§V, Figs. 9–10): Kinect V2 point clouds, servoJ joint streaming; Fig. 9 annotates pipeline rates of 30/40/50/100 Hz. "∞" tracking with human interference: max position error < 4.31·10⁻⁴ m, orientation < 1.29·10⁻⁴ rad; hole polishing: < 2.31·10⁻⁴ m (EE) and < 2.86·10⁻⁴ m (joint 6); contact scanning on a human body: < 2.57·10⁻⁴ m, contact force < 0.45 N.

## Relevance for Plan4ARI
- Closest match in the MPPI literature to our requirement **"seam point exact, null space sampled"**: equality constraints (path + orientation) enforced on *every* sample by projection, MPPI explores only the null space. Directly addresses flaw #10 of [[comparisons/welding-mppi-design-review]] (sub-mm accuracy cannot be a soft cost) and is an alternative/complement to projection MPPI ([[sources/lee2026prmppi]]) and to our exact analytic IK.
- The hole-polishing task (tip fixed, tool axis rotating) is structurally analogous to welding with a free roll / cone, and the ∞-path with fixed attitude is analogous to seam following.
- Timing (~13 ms/step on a consumer GPU for a 7-DoF arm) suggests the projection adds only modest overhead vs STORM (12.54 ms).

## Critical assessment (our view)
- **Not peer reviewed**; experiments are single demonstrations without repetitions or statistics; 7-DoF sample count/horizon not stated explicitly.
- The projection is **first-order (velocity-level, linearised)**: constraint satisfaction is exact only for the linearised constraint per step; drift on curved paths is handled implicitly by the receding horizon. For welding we prefer exact IK on the seam with null-space coordinates as decision variables (no drift by construction).
- Equality projection ignores inequality limits: a projected sample can exceed joint limits or velocity bounds; clamping afterwards would break the equality — interaction not analysed (see [[sources/homburger2023nmppi]] for input saturation).
- Requires a redundant arm (7-DoF) and full-rank B; near singularities the weighted pseudo-inverse is ill-conditioned — no damping discussed.
- STORM was used with equality constraints converted to costs, which is an expected failure mode rather than a tuned baseline; OCS2 timing depends heavily on its collision model.

## Links
- [[concepts/constraints-and-safety]] · [[concepts/path-wise-redundancy-resolution]] · [[concepts/smoothness-action-parametrization]] · [[concepts/sampling-distributions]]
- [[applications/industrial-manipulators]] · [[applications/human-robot-shared-spaces]] · [[comparisons/mppi-variants-matrix]] · [[comparisons/welding-mppi-design-review]]
- Related: [[sources/lee2026prmppi]] (projection MPPI), [[sources/bhardwaj2021storm]] (baseline), [[sources/homburger2023nmppi]] (input constraints), [[sources/zhao2025tangentialmpc]] (subspace sampling), [[sources/sun2024nullspacempc]]
- BibTeX key: `wang2024constrainedpi` in `latex/references.bib`
