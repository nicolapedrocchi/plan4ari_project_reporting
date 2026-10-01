---
title: Design review — multi-goal MPPI look-ahead for AGV-mounted welding
type: comparison
updated: 2026-10-01
---

# Design review — multi-goal MPPI look-ahead for AGV-mounted welding

*Working note from the discussion of 2026-10-01 (PI + Claude). Status: idea under evaluation for the update of the Plan4ARI scientific plan (D4.1 §8–9). Facts from papers are linked; everything else is design reasoning.*

## Reference application (from the PI, 2026-10-01)
- Welding of very large metal structures; industrial arm mounted on an AGV, positioned at a station, then welds a portion of the structure. Base motion interpolated with the arm during welding is possible but remote (theoretically interesting).
- Under-constrained task: reach the seam point; torch axis within a **cone of ~10°** around the surface normal (possibly **anisotropic**: work vs travel angle); rotation about the torch axis almost always free.
- Travel speed along the seam **almost constant: ±10% tolerance**.
- Because of the size, configuration changes may be needed: stop → retract → reconfigure → approach → restart, with the restart **~1 cm before** the detach point.
- Upstream (industrial standard, to be made explicit in the plan): **seam segmentation** and **raw positioning of the manipulator/AGV** chosen to minimise reconfiguration risk.

## Proposed scheme (PI, refined)
1. **Goal set** = up to 8 tuples (IK solution of a different branch at the first point, Cartesian segment). The first configuration is a *soft* target ("approximately"); orientation constraints are cones, possibly anisotropic.
2. **MPPI look-ahead** over ~**10 cm** of seam per goal: it interpolates from the robot state to the first IK, then follows the Cartesian segment exploring the null space (tool roll + cone).
3. **Transition cost** (detach/reconfigure/approach/restart 1 cm back) becomes relevant when the current branch **cannot keep the speed within ±10%** or **approaches joint limits**.
4. **Connection motion** q_state → q_start computed by a fast sampling-based planner, e.g. VAMP ([[sources/thomason2024vamp]]), not by MPPI.
5. Optional **downstream MPC** for speed control (computational load to be assessed).

## What works
- Null space is low-dimensional (6-axis arm: 5 task constraints → 1 free roll + 2-D cone tolerance, plus discrete IK branches): MPPI samples efficiently there.
- Non-smooth costs (collisions with structure, torch-hose wrap, singularities, joint limits) suit MPPI ([[concepts/information-theoretic-mppi]]).
- Receding horizon tracks seam deviations (registration, seam tracking).
- Welding is slow → large time budget per replanning cycle → CPU MPPI plausible, avoiding the GPU-KPI conflict ([[project/prj-plan4ari-proposal]] §A.4.4.1).
- VAMP-style vectorised FK and sphere collision checking on CPU ([[sources/thomason2024vamp]]) can serve both the transfer planner and MPPI rollouts.

## Flaws found (first review) and status after the PI's refinements
| # | Flaw | Status 2026-10-01 |
|---|---|---|
| 1 | Myopia: 2 s ≈ 1–2 cm at 3–10 mm/s (typical MAG range, to verify); infeasibility may appear far ahead | Partly mitigated: horizon defined on path coordinate s (~10 cm) + upstream segmentation/positioning. Residual risk to quantify experimentally. A breakpoint-minimising DP ([[sources/yin2024dpbreakpoints]]) can supply cost-to-go and segment boundaries |
| 2 | Long time horizons blow up sampling variance | Mitigated: parametrise on s with few spline knots |
| 3 | No cost-to-go → modes not comparable | Open: compare modes at the **same end abscissa s_end**; optional terminal value from upstream feasibility check |
| 4 | Detach point s* is a decision variable, missing from the tuple | Open: rule "detach at the last point with margin before predicted violation", restart at s* − 1 cm |
| 5 | One q₀ per branch discards the null space | Solved by design: q₀ is a soft seed, MPPI optimises roll/cone within the branch |
| 6 | Combinatorial growth of mode sequences | Mitigated: ≤ 8 goals per cycle; sequences decided upstream |
| 7 | Blending across IK branches (M3P2I-style, [[sources/zhang2024m3p2i]]) yields non-existent configurations | Must hold: **select, never blend** across branches ([[sources/liu2026clusteringmppi]]) |
| 8 | Mode chattering from noisy cost estimates | Open: hysteresis + commitment (branch changes only through a planned detach) |
| 9 | Commensurable costs (time vs restart defect) | Partly: time as common unit (time-dilation as in [[sources/faroni2022safetyaware]]); restart quality penalty needs a process weight |
| 10 | Sub-mm path accuracy cannot be a soft cost | Must hold: sample only null-space coordinates, exact analytic IK on the branch, or projection ([[sources/lee2026prmppi]]) |
| 11 | Constant speed is a hard process constraint | Partly: ±10% tolerance; speed scaling coupled to welding parameters; downstream time-scaling layer ([[sources/faroni2019pik]], [[sources/faroni2020scaling]], [[sources/palleschi2021fastsafe]]) |
| 12 | Anisotropic cone, orientation-rate limits | Acknowledged by PI (anisotropic); add rate cost |
| 13 | Torch-hose / axis-6 wrap limits roll | Open: model explicitly |
| 14 | Transfer motions are a planning problem | Solved by design: sampling-based planner (VAMP) |
| 15 | Transfer cost inside every rollout is unaffordable | Mitigated: VAMP fast enough to plan the real transfer per goal per cycle; circular dependency with MPPI-chosen start (see below) |
| 16 | Restart overlap is process-dependent (crater, arc start) | Open: parametric overlap |
| 17–18 | AGV motion during welding; station placement is the real lever | Accepted: base static per station; placement upstream |
| 19–21 | Multi-robot: allocation/sequencing (distortion), scalability, communication | Open: allocation in task planner (Activity 2); per-robot MPPI with others as dynamic obstacles ([[sources/streichenberg2023mapi]], [[sources/jansma2023interaction]]); joint sampling only for tightly coupled pairs |
| 22 | Repeatability / weld qualification | Open: deterministic sampling (fixed-seed Halton), logging, approved variation limits |
| 23 | Certification, determinism | Open: certified downstream layer |
| 24 | Deterministic baseline (DP over discretised null space, gradient predictive IK) mandatory | Literature found: DP with breakpoints [[sources/yin2024dpbreakpoints]], DP + online adjustment [[sources/yin2024dprealtime]], fast functional IK [[sources/razjigaev2025functional]], GRR roadmaps [[sources/zhong2024expansiongrr]]; see [[concepts/path-wise-redundancy-resolution]]. Benchmark plan still open |

## New points raised by the refinement
- **Hard vs soft first point.** The *configuration* at the first point is soft; the *Cartesian* start point of the weld (arc start) must stay exact.
- **Circular dependency MPPI ↔ VAMP.** VAMP needs a goal configuration, MPPI optimises it. Options: (a) VAMP to the nominal IK of each branch, then a short MPPI-controlled approach adjusts it; (b) MPPI with an estimated transfer cost, then VAMP validates only the selected mode. (b) is cheaper.
- **Transition as cost comparison, not hard trigger.** Use the time-dilation factor along each rollout, λ = max_j |q̇_j,req| / q̇_j,max, where q̇_req is the joint speed needed for the nominal travel speed. "Speed kept within tolerance" ⇔ λ ≤ 1/0.9 ≈ 1.11. Add a smooth barrier on joint-limit margins. A mode switch happens when C_alt + C_transfer + hysteresis < C_continue. Hard thresholds would make the cost discontinuous and cause chattering.
- **Equal-progress comparison.** All modes evaluated up to the same s_end; alternatives start at s_detach − 1 cm.
- **Pruning of the 8 goals.** At segment planning time, check along the whole segment with analytic IK which branches are feasible; offer MPPI only those, with nominal null-space seeds.
- **Research question.** How many restarts does a 10 cm local look-ahead produce vs a global DP optimum over the segment? This is a clean experiment for D4.1 §10, also as a function of horizon length (5/10/20 cm).

## PI answers and decisions (2026-10-01, second round)
- **Robot**: 6-axis arm on AGV, potentially on an **interpolated 7th linear axis** (rail). With the rail the null space gains one continuous DoF (rail position): goals become "IK branch + rail seed", IK is no longer a finite set per point, and reconfigurations can often be avoided by moving the rail. Rail limits and (slower) dynamics enter as constraints.
- **Speed tolerance**: ±10%, constant along the whole path → the λ threshold (≤ 1/0.9) is fixed.
- **VAMP two-pass scheme (PI)**: (1) VAMP plans the connection to the *nominal* start configuration of each goal → transfer cost used by MPPI; (2) after MPPI optimisation, VAMP re-plans the *real* connection to the optimised start; (3) if the cost changed a lot, something is wrong → more rollouts, or discard that solution.
  - Assessment: sound "predict-then-validate" loop (it is option (b) above with an explicit consistency check). Caveats: RRT-Connect is randomised, so two VAMP calls to the same goal give different path costs → use best-of-N or shortcutting before comparing; compare *time-parametrised* costs computed the same way in both passes; set the tolerance relative to the transfer cost; nominal transfer costs can be cached per segment and recomputed only on scene change; on discard, fall back to the next-best mode.

## Literature check (2026-10-01)
- Path-wise redundancy resolution: closest work is DP with a large constant cost per breakpoint, minimising the number of interruptions first ([[sources/yin2024dpbreakpoints]]) — same objective as our "fewest detach/reconfigure cycles". But it keeps a single IK branch, one redundancy dimension, does not plan transfer motions and reports no computation times. DP with online viability margins ([[sources/yin2024dprealtime]]) is the closest match to "offline funnel + online adjustment". See [[concepts/path-wise-redundancy-resolution]].
- Inner IK for rollouts / deterministic baseline: functionally-redundant IK for 5-axis tasks on 6-axis arms, ~0.2 ms per step ([[sources/razjigaev2025functional]]).
- Station placement: set-cover over targets with 5-D reachability ([[sources/nguyen2023taskclustering]]), inverse reachability maps ([[sources/makhal2018reuleaux]]), coverage BPO ([[sources/zhang2023basecoverage]]), welding feasibility checklist per base pose ([[sources/gautier2024weldingbase]]). All point-based: none checks seam-level continuity at constant speed. See [[concepts/base-placement]].
- **Novelty assessment (arXiv only):** no MPPI work on path-constrained redundancy resolution with IK-branch modes and planned transfers was found. IEEE/Elsevier-only literature and ROS-Industrial Descartes still to be checked.

## Literature check, round 2 (IEEE, Elsevier, Descartes — 2026-10-01, 35 sources)
**Impact on the design, by flaw / decision:**
- **8 IK branches (decision).** Holds for non-cuspidal industrial arms (spherical wrist): branches separated by singularities, so a branch change = reconfiguration. It **fails for offset-wrist "welding cobots"** (FANUC CRX, ABB GoFa: up to 16 solutions, branch change without singularity), and axes 4/6 with range > ±π multiply the goals (branch × turn) ([[sources/elias2025cuspidal]]). → Fix the target robot kinematics before freezing the goal model.
- **#7 select-never-blend.** Confirmed as a real risk: PMPPI blends the means of parallel planners ([[sources/zhou2025parallelmppi]]). A principled alternative: MPPI as EM with a Gaussian mixture, one component per branch, mixture weights as branch-selection signal with hysteresis ([[sources/wang2026mppiem]]).
- **#10 exact path.** Null-space projected MPPI already exists as a preprint (<0.43 mm path error on a real 7-DoF arm, [[sources/wang2024constrainedpi]]); deterministic counterpart: null-space NMPC at 100–300 Hz in simulation ([[sources/sun2024nullspacempc]]). Sampling a low-dimensional subspace works with few rollouts ([[sources/zhao2025tangentialmpc]], N=50).
- **#11 speed layer.** Industrial template: path-exact jerk-limited online trajectory generation that only modifies s(t), 250 Hz on KUKA ([[sources/lange2016pathaccurate]]) — its catch-up must be disabled and its slowdown bounded to ±10%. Path-following NMPC solves in ≤0.48 ms at 1 kHz on a 3-DoF arm ([[sources/faulwasser2017pathfollowing]]) → the downstream MPC is affordable; a band violation must trigger the planned detach upstream, not a stop. Hard joint-velocity limits inside MPPI: sample accelerations, saturate velocities ([[sources/homburger2023nmppi]]). Feedback-MPPI gains could stabilise null-space tracking between MPPI updates ([[sources/belvedere2026feedbackmppi]]).
- **#12 anisotropic cone.** Ranged-goal losses (flat inside the range) are ready-made cost shapes ([[sources/wang2023rangedik]]); Descartes extended with a weighted tilt-deviation cost for the same reason ([[sources/demaeyer2017descartes]]). Groove-based torch posture gives the cone centre with ~2° error ([[sources/wang2026torchposture]]).
- **Seam registration (new requirement).** Global localisation + CAD registration of a mobile platform left up to ~40 mm TCP error on a large workpiece ([[sources/zhao2021mobilemachining]]) → per-station local seam registration / tracking is mandatory; MPPI plans on the corrected seam.
- **#14 transfers.** Welding-specific transfer planning (lazy-PRM in TCP space with external axis) takes 10–26 s on a real cell ([[sources/zhou2022weldavoidance]]) vs tens of µs for VAMP queries ([[sources/thomason2024vamp]]): strong argument for VAMP. RRT-guided MPPI ([[sources/tao2023rrtmppi]]) supports "planner provides the MPPI mean" and gives a rule (distance from guide > R) for when to re-call the planner.
- **#17–18 stations.** Placement for continuous paths exists ([[sources/weingartshofer2021tcpbase]], <100 ms per path for branch enumeration) and placement scored by true cycle time ([[sources/wachter2024tcpbase]]); joint base+path optimisation ([[sources/zhao2025bstar]]). None checks constant speed or cones, none minimises the number of stations for continuous seams → our station planner = set-cover over segments with a Weingartshofer-like continuous-branch test + λ speed check. See [[concepts/base-placement]].
- **#19–21 multi-robot.** Seam allocation with synchronous pairs (distortion) and direction constraints, NSGA-II ([[sources/tang2023dualrobotweld]]) → task-layer vocabulary for the interface to per-robot MPPI. For tightly coupled pairs, the deterministic offline baseline is null-space descent with exact path/coupling correction and joint placement optimisation ([[sources/ye2026nullspacemultirobot]]: 78.87% success in ~8 s on two 7-DoF arms vs 33% for fmincon, Table 4); it has no cones, no reconfiguration, no inter-robot collision model and timing only as penalty. Its "correct onto the path, then descend in the null space" step is reusable after MPPI sampling.
- **#24 deterministic baselines (now well covered).** Descartes ([[sources/demaeyer2017descartes]]; memory ~ (N−1)(2M)² edges, no speed, torch jumps inside tolerance), Descartes with external axes ([[sources/sun2020externalaxis]]), anytime layered graph minimising reconfigurations ([[sources/wang2025anytimetracking]]: 0.4 vs 0.9 reconfigurations in a welding test), global co-optimisation of cones, redundancy and timing ([[sources/chen2025cooptimization]], <10 min for ~8k waypoints), warm-started optimisation with tolerance windows ([[sources/weingartshofer2023pathframework]]). Benchmark framework and metrics: [[sources/demaeyer2021weldbenchmark]]. See [[applications/robotic-welding]].
- **7th linear axis.** Descartes-style DP with rail sampled per point works but scales badly (minutes for ~60 points; [[sources/sun2020externalaxis]]); fixing the rail value inside a rollout keeps analytic IK cheap.

**Novelty assessment (updated).** Closest prior work per ingredient: null-space projected MPPI ([[sources/wang2024constrainedpi]], preprint, single branch, no reconfiguration, no speed band); reconfiguration-minimising offline planners ([[sources/yin2024dpbreakpoints]], [[sources/wang2025anytimetracking]], [[sources/chen2025cooptimization]]); MPPI guided by sampling planners ([[sources/tao2023rrtmppi]]). Still **no work combines** an online null-space look-ahead with IK-branch modes, planned transfers + restart overlap, constant-speed band and seam-registered replanning. Claim the combination, not "null-space MPPI" alone. Li et al. 2024 turned out to be offline smoothing with fixed tool axis (weak baseline, [[sources/li2024weldredundant]]); Ye et al. 2026 is offline, exact-path, coupled multi-robot ([[sources/ye2026nullspacemultirobot]]) — neither changes the novelty assessment. Still not read: Lee & Han 2025 (ASCE, mobile welding navigation).

## Downstream MPC (speed control)
- Natural split = path–velocity decomposition: MPPI outputs a smooth joint path q(s) on the chosen branch; the downstream layer computes s(t) within ±10% under hard joint velocity/acceleration/jerk limits and feeds the actual s(t) back to MPPI.
- Light option: 1-DoF path-parametrised scaling (convex, as [[sources/palleschi2021fastsafe]]; predictive scaling as [[sources/faroni2020scaling]]). Heavy option: full joint-space NMPC ([[sources/verschueren2022acados]]). Compute load must be benchmarked on Core-IPC hardware (no numbers assumed here).

## Compute budget (estimate to verify)
- Order of magnitude per MPPI cycle: 8 goals × ~128 rollouts × ~50 states over 10 cm ≈ 5·10⁴ state evaluations (analytic IK + FK + sphere collision). With CPU vectorised primitives this is plausibly within a few-ms to tens-of-ms budget; **first task: micro-benchmark** on the target IPC.

## Next steps
1. Micro-benchmark of rollout evaluation (IK + FK + collision) on CPU (VAMP primitives) and GPU.
2. Prototype on one segment: single-branch null-space MPPI vs DP baseline vs gradient predictive IK.
3. Add multi-goal selection + VAMP transfer; measure restarts vs horizon.
4. ~~Literature search on arXiv~~ done 2026-10-01 (8 sources); ~~IEEE / Elsevier / Descartes~~ done 2026-10-01 (35 sources). Li 2024 and Ye 2026 ingested; remaining: Lee & Han 2025 (no access).
6. Decide the target robot kinematic class (non-cuspidal vs offset-wrist cobot; axes 4/6 range) — it changes the goal model.
5. Station planner: set-cover over seam segments with path-wise feasibility ([[concepts/base-placement]]).

## Links
- Deliverable draft built on this review: `../scientific-plan/plan_update.tex` (updated scientific plan, 2026-10-01)
- [[comparisons/plan4ari-gap-analysis]] · [[project/prj-plan4ari-proposal]] · [[project/prj-d41-outline]]
- [[concepts/multimodality]] · [[concepts/constraints-and-safety]] · [[concepts/hybrid-gradient-sampling]] · [[applications/industrial-manipulators]]
