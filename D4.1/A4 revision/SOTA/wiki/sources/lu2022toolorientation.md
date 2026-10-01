---
key: lu2022toolorientation
title: "High-order joint-smooth trajectory planning method considering tool-orientation constraints and singularity avoidance for robot surface machining"
authors: "Lu, Lei; Zhang, Lei; Fan, Cheng; Wang, Hao"
year: 2022
venue: "Journal of Manufacturing Processes, vol. 80, pp. 789-804"
arxiv: 
doi: 10.1016/j.jmapro.2022.06.041
pdf: raw/papers/lu2022toolorientation.pdf
text: raw/text/lu2022toolorientation.txt
tags: [redundancy-resolution, orientation-tolerance, machining, manipulators, industrial, singularity-avoidance]
status: read
---

# High-order joint-smooth trajectory planning method considering tool-orientation constraints and singularity avoidance for robot surface machining

*Lu, Lei; Zhang, Lei; Fan, Cheng; Wang, Hao* (2022). Journal of Manufacturing Processes, vol. 80, pp. 789-804.

## TL;DR
Greedy, step-by-step **differential (local) redundancy resolution** for ball-end surface machining with a 6R robot: the tool tip follows the path exactly, while all **three rotational DoFs** of the tool (two tilt angles bounded by cutting-angle and collision limits, plus free roll) are chosen at each integration step by optimising a small differential rotation. The weighted objective combines minimal joint step, distance from singularity (Jacobian condition number) and distance from the tilt-angle bounds, with adaptive weights that grow sharply near limits. Second-order smoothness is obtained by **rate-limiting the differential rotation**, and the lack of foresight is compensated by **pre-smoothing the orientation bounds** along the path. Validated on a UR5 (simulation + aluminium carving).

## Method
- Integration scheme (§2): tool pose T_{i+1} = R(D)·T_i, with D = [tangent·Δu (fixed), δx, δy, δz (free)]; joints by IK of each new pose. Initial pose: tilt angles at the centre of the feasible region; roll chosen by discretisation for minimal condition number.
- Objectives (§3): (1) minimal joint differential ‖J⁻¹D‖; (2) minimal predicted condition number κ(J) at the next step; (3) tilt angles α (azimuth in local frame) and γ (inclination from local normal) driven towards the centre of their bounds [α_min, α_max], [γ_min, γ_max] (Eq. 8–13).
- Combined normalised objective (Eq. 14) with **adaptive weights** (Eq. 15–16): λ2 = (κ/κ_threshold)^a with κ_threshold = 100, a = 4; λ3, λ4 grow steeply as α, γ approach their bounds (a1 = a2 = 3, b1 = b2 = 8).
- Bounds on δ/ds (C¹ continuity) and on its change rate between steps (Algorithm 1) → limited second-order derivative ("high-order" smoothness).
- **Look-ahead surrogate** (§4–5): abrupt changes of the feasible region (obstacles) or of the local frame (sharp corners) are pre-smoothed backwards along the path (Algorithm 2 + simple moving average), so that the centring term starts moving the tool before the constraint changes.

## Evidence
- Robot: UR5 with ROS controller (§6); no computation times are reported.
- **Case A** (square path, 200 mm side, three right-angle corners, four obstacle blocks; 90° ≤ α ≤ 270°, 5° ≤ γ ≤ 45°): ablations NSC (no pre-smoothing), FDL (no rate limit), NSO (no singularity term). NSC violates the tilt bounds at corners and at obstacle onsets (Fig. 12–13); NSO shows joint jumps and high condition number (Fig. 10–11); proposed method satisfies all bounds and avoids the blocks (Fig. 14).
- **Case B** (butterfly curve on inclined aluminium surface; 90° ≤ α ≤ 270°, 5° ≤ γ ≤ 15°): total joint travel (Table 1) 11.09 rad (proposed) vs 36.89 rad for SCA (fixed tilt at bound centre, only roll optimised by a graph method + smoothing), 10.82 rad (FDL), 9.57 rad (NSC, which violates the bounds). Feedrate-scheduled machining time (Fig. 19, read from plot axes): about 800 s for the proposed method vs about 2,500 s for SCA; FDL longer than proposed despite shorter joint path, attributed to unlimited higher-order derivatives.
- Physical carving of the butterfly curve completed (Fig. 20, qualitative).

## Relevance for Plan4ARI
- Same task structure as our welding seam: exact tip path, tool axis inside a **(possibly asymmetric) cone** — here two independent angle bounds, analogous to separate **work and travel angle** tolerances — and free roll. Table 1 is quantitative evidence that **exploiting the cone (3 rotational DoFs) instead of roll only** cuts joint travel by ~3× and machining time strongly — supporting the decision to sample the cone in MPPI rather than fix the torch at the nominal angle ([[comparisons/welding-mppi-design-review]]).
- Adaptive "barrier-like" weights near the cone boundary and near singularity are a ready template for MPPI running costs (flaw #12: orientation-rate limits → their δ/ds rate limit).
- The authors needed a hand-made **look-ahead (pre-smoothed bounds)** to fix the myopia of step-wise integration: this is evidence for our horizon-based approach (flaw #1) — MPPI over ~10 cm achieves the anticipation natively.

## Critical assessment (our view)
- Purely local/greedy and deterministic: no branch choice, no recovery if the path becomes infeasible, no reconfiguration; the singularity term is a soft weight, not a guarantee.
- Pre-smoothing of bounds is heuristic and tuned per path; parameters (κ_threshold, exponents) are arbitrary.
- Demonstrated on a light UR5 with very low joint speeds (Fig. 19); the SCA comparison is against a baseline that fixes tilt at the centre, so part of the gain is simply the larger search space.
- Useful as the "differential IK with cone" deterministic baseline next to [[sources/razjigaev2025functional]], and as the cheapest per-step projection inside rollouts.

## Links
- [[concepts/path-wise-redundancy-resolution]]
- [[concepts/smoothness-action-parametrization]]
- [[comparisons/welding-mppi-design-review]]
- [[applications/industrial-manipulators]]
- Related: [[sources/chen2025cooptimization]], [[sources/wang2023rangedik]], [[sources/razjigaev2025functional]], [[sources/faroni2019pik]], [[sources/elias2025cuspidal]]
- BibTeX key: `lu2022toolorientation` in `latex/references.bib`
