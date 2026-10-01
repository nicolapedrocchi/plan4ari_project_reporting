---
key: homburger2023nmppi
title: "Efficient Nonlinear Model Predictive Path Integral Control for Stochastic Systems considering Input Constraints"
authors: "Homburger, Hannes; Wirtensohn, Stefan; Reuter, Johannes"
year: 2023
venue: "2023 European Control Conference (ECC), pp. 1-6"
arxiv: 
doi: 10.23919/ecc57647.2023.10178349
pdf: raw/papers/homburger2023nmppi.pdf
text: raw/text/homburger2023nmppi.txt
tags: [mppi-core, constraints, input-constraints, smoothness]
status: read
---

# Efficient Nonlinear Model Predictive Path Integral Control for Stochastic Systems considering Input Constraints

*Homburger, Hannes; Wirtensohn, Stefan; Reuter, Johannes* (2023). 2023 European Control Conference (ECC), pp. 1-6.

## TL;DR
Short ECC paper on how to impose **hard box constraints on the control input** in MPPI without breaking the path-integral assumption (quadratic input cost, unconstrained noise). Both proposals augment the state with an **integrator on the input** (MPPI samples the input *rate*, the applied input becomes a state). Variant **PT** adds an L1 penalty on the integrator state leaving the box; variant **SI** (saturated integrator) clips the integrator state inside the dynamics. SI satisfies the bounds by construction, needs no tuning of a penalty weight and performed better on a self-balancing vehicle in simulation and full scale with M = 2000 samples on a Jetson Nano.

## Method
- Standard MPPI / path-integral optimizer recalled (§II, Alg. 1): Lagrange term must be state cost + quadratic input cost with R = λΣ⁻¹; any other input cost or a constrained feasible set violates the derivation.
- Key idea (§III): extend the state with integrator states w_k ∈ R^nu, so the sampled variable v_k is the input derivative and the actual input w_k is a state. Two properties of MPPI are then exploited: state costs may be arbitrary, and dynamics may be discontinuous.
- **PT – penalty term** (§III-A, Eq. 8): add σ·dist₁(w_k, [u⁻, u⁺]) to the state cost; the penalty vanishes iff the box is satisfied. Constraint can be violated.
- **SI – saturated integrator** (§III-B, Eq. 9): element-wise saturation of w_k + h·v_k to [u⁻, u⁺] inside the (artificial) integrator dynamics; constraint satisfied for every sample and for the applied input. The SI structure is credited to the integrator idea of SMPPI ([[sources/kim2022smppi]]).
- Both variants have negligible extra cost; the integrator also low-pass filters the input sequence (smoother commands, §VI).

## Evidence
- Platform: self-balancing vehicle MonoChair2 (5-state model: planar pose, heading, two internal states of the inner velocity loop; inputs desired velocity and desired heading), positioning task to (10 m, 5 m) with desired velocity box [0, 0.5] m/s (Table I, §IV).
- Parameters (Table II): MPPI step h = 0.5 s, horizon T = 10 s (N = 20 steps), RK4 with 0.1 s, λ = 1, penalty σ = 50000, L1 position costs.
- Simulation (§V-A, Figs. 2–3): benchmark with M = 10⁶ samples and real-time setting M = 2000. SI reaches the goal and brakes with both sample counts and respects the bound at all times; PT reaches the goal only with 10⁶ samples, with M = 2000 it under-steers, overshoots the bound at some instants and oscillates below the upper bound instead of using it.
- Full scale (§V-B, Figs. 4–5): controller on an **NVIDIA Jetson Nano**, only M = 2000 feasible; PT brakes spuriously at t = 11.5 s due to model mismatch, SI behaves as in simulation.
- Accumulated Lagrange cost over 30 s (§V-B): PT 478 vs SI 418.7 in simulation; PT 522.8 vs SI 425.3 full scale.
- No computation time per iteration and no control rate beyond h = 0.5 s are reported.

## Relevance for Plan4ARI
- Directly answers "how to keep **joint velocity/acceleration limits as hard constraints** in MPPI": sample joint accelerations (or jerks), integrate, and saturate the integrated velocity in the rollout dynamics. This is the natural way to keep q̇ inside limits in our welding null-space MPPI and to make the time-dilation λ cost meaningful (λ ≤ 1/0.9 means requested joint speeds stay below saturated limits) — see [[comparisons/welding-mppi-design-review]].
- The paper shows penalty-only treatment (PT) degrades with realistic sample counts (2000) — an argument against relying on soft joint-limit costs alone in a CPU-budget MPPI. See [[concepts/constraints-and-safety]].
- Saturation only handles **input/rate box constraints**; joint *position* limits and collisions remain costs (or need projection, [[sources/lee2026prmppi]]).

## Critical assessment (our view)
- Very small evidence base: one 2-input vehicle, single scenario, single run per setting, no statistics, no timing. The 10⁶-sample benchmark is a useful sanity check but not a real-time result.
- Saturating inside the dynamics makes the map V → trajectory non-injective (many samples collapse to the bound); the authors do not discuss the resulting loss of exploration near the bounds nor a stability proof (stated as future work).
- The integrator trick changes the decision variable (input rate), so it also changes smoothness and responsiveness; for welding this is desirable (smooth q̇), but the horizon grows in effective order.
- Nothing about state constraints; for manipulators the joint-position box needs a second integrator stage (acceleration → velocity → position), where clipping position would create non-physical trajectories.

## Links
- [[concepts/constraints-and-safety]] · [[concepts/smoothness-action-parametrization]] · [[concepts/information-theoretic-mppi]]
- [[comparisons/mppi-variants-matrix]] · [[comparisons/welding-mppi-design-review]]
- Related: [[sources/kim2022smppi]] (integrator / input-lifting), [[sources/williams2018tro]] (base MPPI used), [[sources/wang2024constrainedpi]] (equality constraints by projection), [[sources/fazlyab2026mppigd]] (theory with bounded feasible set)
- BibTeX key: `homburger2023nmppi` in `latex/references.bib`
