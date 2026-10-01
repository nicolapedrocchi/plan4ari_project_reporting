---
key: weingartshofer2023pathframework
title: "Optimization-based path planning framework for industrial manufacturing processes with complex continuous paths"
authors: "Weingartshofer, Thomas; Bischof, Bernhard; Meiringer, Martin; Hartl-Nesic, Christian; Kugi, Andreas"
year: 2023
venue: "Robotics and Computer-Integrated Manufacturing, vol. 82, pp. 102516"
arxiv: 
doi: 10.1016/j.rcim.2022.102516
pdf: raw/papers/weingartshofer2023pathframework.pdf
text: raw/text/weingartshofer2023pathframework.txt
tags: [path-planning, redundancy-resolution, continuous-path, manipulators, industrial]
status: read
---

# Optimization-based path planning framework for industrial manufacturing processes with complex continuous paths

*Weingartshofer, Thomas; Bischof, Bernhard; Meiringer, Martin; Hartl-Nesic, Christian; Kugi, Andreas* (2023). Robotics and Computer-Integrated Manufacturing, vol. 82, pp. 102516.

## TL;DR
Deterministic, optimisation-based planner that maps a Cartesian manufacturing path to a continuous joint path while exploiting **process DoF**: exact constraints, **tolerance bands**, **process windows** (e.g. an orientation cone) and **redundant process DoF** (e.g. free rotation of a symmetric tool), with collision avoidance (V-Clip signed distances) and passages through singularities. The path is solved point by point as a sequence of small NLPs (interior point, analytic gradients), warm-started from the previous point and launched in parallel from several IK seeds of the first pose; the best complete path is selected afterwards.

## Method
- **Process properties** (§4.3, Eq. 6–7, Fig. 2–3): per-axis min/max displacement and roll–pitch–yaw deviation of the tool frame w.r.t. the path frame. Each component can be a hard equality (exact), an inequality (window), a soft cost (tolerance) or cost + inequality (tolerance band); zero weight and no constraint gives a free (redundant) DoF.
- **Start configurations** (§5.1, Eq. 8–12): grid sampling of the windows at the first path pose only, IK (analytic or TRAC-IK) for each sample, de-duplication with a minimum joint distance → e_g seeds.
- **Sequential NLP** (§5.2, Eq. 13–15): for each seed u and path pose i, minimise f(q) subject to joint limits, c_eq, c_ineq, warm-started at the solution of pose i−1; MATLAB `fmincon` interior point with analytic gradients; seeds solved in parallel on CPU cores. A seed whose sequence becomes infeasible is discarded (Fig. 5).
- **Terms** (§5.3): position error (Eq. 18–24); quaternion orientation error, isotropic (Eq. 26) or per-axis weighted (Eq. 27), and as constraints (Eq. 28–30); collision soft penalty + hard signed-distance inequality (Eq. 36–39; using both improves convergence); joint-step continuity cost (Eq. 40) and joint-limit centring (Eq. 42–44). IK is implicit in the optimisation, so kinematically redundant arms need no analytic IK.
- **Selection and timing** (§5.4–5.5): sum of a chosen subset of cost terms along the path (Eq. 45) picks the best path (e.g. by process quality only); time stamps from Cartesian distance / desired path speed (Eq. 46) + cubic Hermite interpolation.
- No cross-connections between seed paths (Remark 2): each candidate path stays on the branch it started from (branch changes only via continuous passage through singularities).

## Evidence
- Path: meander on a rabbit-shaped workpiece, ~2.5 m, 1024 poses (§6, Fig. 6).
- **Drawing, real robot** (§6.1): KUKA LBR iiwa 14 R820 (7-DoF), marker with rectangular nib; position exact (equality), orientation window ±40° about x, y and ±20° about z (Eq. 47), extra collision box; weights in Tab. 1. More than **15%** of the path poses are reachable only by using the tolerances (Fig. 8). Used tolerances stay below 30° (x, y) and 10° (z) (Fig. 11); the robot passes three times through a singular configuration (Fig. 9). Mean time per NLP ≈ **70 ms** single-core, ≈ **18 ms** with all cores (i7-8700K); total ≈ **90 s** with e_g = 6 seeds; without collision checks the per-step time drops by a factor 3. Executed without absolute calibration (passively compliant tool).
- **Spraying, simulation** (§6.2): KUKA KR8 R1620 (6-DoF) holding the workpiece, stationary nozzle; x, y exact, z band +45/−55 mm, x/y rotation fixed, rotation about the nozzle axis free (Eq. 48, Tab. 2). Constant path speed; one singular passage (q5 = 0); ≈ **36 ms** / **9 ms** per NLP (single/all cores), total ≈ **60 s** with 6 seeds; the free rotation is used extensively, the z band only slightly (Fig. 14).
- The relative workpiece/base placement in both cases was precomputed with the authors' earlier method [[sources/weingartshofer2021tcpbase]] (§6.1.2, §6.2.2).

## Relevance for Plan4ARI
- The process-property formalism maps one-to-one onto our welding spec: seam position exact, torch axis in a ~10° cone (anisotropic via per-axis bounds), free roll = redundant process DoF, plus collision with the structure. It is a ready **deterministic baseline** for the MPPI look-ahead (item 24 of [[comparisons/welding-mppi-design-review]]).
- Multi-seed sequential optimisation = our "IK branch + null-space seed" goal set; per-seed feasibility over a whole segment is the path-wise test needed by the station planner ([[concepts/base-placement]]).
- Timing (tens of ms per pose, ~1 min per 1000-pose path) is fine for offline station evaluation but too slow to embed brute force in a large set-cover without pruning.

## Critical assessment (our view)
- **Greedy and local**: each pose is optimised from the previous one; no look-ahead, no cost-to-go, no branch switching — the same myopia we expect from a short MPPI horizon, here with a horizon of one point. Graph-based/predictive variants are named as future work.
- **Speed not verified**: timing is derived from Cartesian distance only; joint velocity/acceleration limits at the commanded speed are not checked, so the ±10% constant-speed requirement and singular passages (which can demand large joint rates) remain unverified.
- Tolerance use is driven by heuristic weights that strongly affect convergence (§5.4); hard bounds guarantee the windows but the result depends on tuning.
- No reconfiguration/restart logic: a failing seed is discarded; there is no "detach, reconfigure, resume" planning.
- MATLAB implementation; compiled code and other solvers are future work.

## Links
- [[concepts/path-wise-redundancy-resolution]] · [[concepts/base-placement]] · [[comparisons/welding-mppi-design-review]]
- Same group: [[sources/weingartshofer2021tcpbase]], [[sources/wachter2024baseplacement]]; related: [[sources/zhao2025bstar]], [[sources/farzanehkaloorazi2018pathplacement]]
- Alternatives cited/compared: [[sources/demaeyer2017descartes]], [[sources/schulman2014trajopt]], [[sources/zucker2013chomp]], [[sources/kalakrishnan2011stomp]]; DP baselines [[sources/yin2024dpbreakpoints]], [[sources/yin2024dprealtime]]
- BibTeX key: `weingartshofer2023pathframework` in `latex/references.bib`
