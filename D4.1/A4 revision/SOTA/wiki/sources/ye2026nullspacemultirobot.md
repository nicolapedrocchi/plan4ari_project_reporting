---
key: ye2026nullspacemultirobot
title: "Path-constrained trajectory planning for multi-robot manufacturing systems using null-space descent optimization with reduced Hessian"
authors: "Ye, Xin; Grobbel, Max; Schurmann, Tobias; Schwab, Stefan; Hohmann, Soren"
year: 2026
venue: "The International Journal of Robotics Research, vol. 45, no. 11, pp. 1648-1681"
arxiv: 
doi: 10.1177/02783649251400381
pdf: raw/papers/ye2026nullspacemultirobot.pdf
text: raw/text/ye2026nullspacemultirobot.txt
tags: [multi-robot, redundancy-resolution, path-planning, trajectory-optimization, null-space, manipulators, industrial]
status: read
---

# Path-constrained trajectory planning for multi-robot manufacturing systems using null-space descent optimization with reduced Hessian

*Ye, Xin; Grobbel, Max; Schurmann, Tobias; Schwab, Stefan; Hohmann, Soren* (2026). The International Journal of Robotics Research, vol. 45, no. 11, pp. 1648-1681.

## TL;DR
Offline, single-stage optimisation that plans **robot/work-piece placement and B-spline joint trajectories at the same time** for several robots that are **physically coupled** (closed kinematic loop through a common tool/coupler) and must follow a given Cartesian path exactly. Each SQP iteration is split into a *vertical* step that removes path and coupling errors (minimum-norm Gauss–Newton) and a *horizontal* step that lowers the cost (TCP stiffness, conditioning, smoothness) only inside a **kinematically interpretable null-space basis** of the constraints, with a BFGS **reduced Hessian**. The authors prove two-step superlinear local convergence including joint bounds, use multi-start from analytic-IK seeds (up to 8 per robot) and split long paths into segments coordinated by (fast) ADMM. Validated with two coupled KUKA LBR iiwa 14 (7-DoF) in a spring-pulling benchmark (478 starts: 78.87% success, 8.08 s mean, Table 4) and in real three-segment milling (stiffness gains ≥20.8% / ≥35.1% vs. non-optimised, Tables 12–13).

## Method
- **Problem (§Preliminaries, Problems 1–4).** Configuration trajectory θ(u) = [q(u); y] with path parameter u ∈ [0,1] (not time); y = static placement of robot bases and work-piece. Equality constraints e_pose = [e_cp; e_path] = 0: path error of one robot TCP w.r.t. the path (dimension n_path ≤ 6) plus loop-closure errors between the TCPs of all robots (Eq. 1, 33). Bounds on joints and placement (Eq. 3–4). Multi-segment version: same placement for all segments and C⁰/C¹ joint continuity at segment joints (Eq. 5–6, 18–19).
- **Parametrisation.** Each joint is a B-spline (order κ, l control points, uniform knots, Eq. 10–13); the decision vector z stacks control points and placement. Path constraints are enforced at l discrete points (Eq. 14); the path itself is re-approximated by a Cartesian B-spline of the same order/size so that s(u) and q(u) progress in sync (Fig. 6). Joint position limits via the convex-hull property of B-splines (conservative, Eq. 15).
- **Cost (Eq. 16–21).** Directional compliance index along the known process wrench (Eq. 20) using additive coupled stiffness K_tcp = Σ_r (J_r K_q⁻¹ J_rᵀ)⁻¹ (rigid coupler, Eq. 9), a kinetostatic-conditioning term against singularities (Eq. 16) and a control-point fluctuation term scaled by q̇_max (Eq. 17). **Velocity/acceleration limits are not constraints**: the time law is unknown at planning time and is fixed afterwards; only penalties keep joint speeds reasonable (§Constraints). **Collision avoidance is not modelled**; Remark 1 states it could be added as a penalty.
- **Reduced-Hessian null-space descent (§Solving optimization problem, Eq. 24–31).** Step d = v + α·Z_z·d̄: v = minimum-norm solution of the linearised constraints (Eq. 37, with Tikhonov regularisation for ill-conditioning, Eq. 38); Z_z is a null-space basis of the constraint Jacobian whose columns are "move one redundant joint at one waypoint" or "move one placement variable", each projected so the pose error is unchanged (Eq. 39–43, Lemmas 1–2). Unlike SVD/QR bases, this basis is continuous in z, which is what makes BFGS on the reduced Hessian Z_zᵀBZ_z convergent. Bounds are kept in a small QP solved by an active-set method (Eq. 31b, 48–51). Cost gradients via CasADi automatic differentiation (Eq. 44–47).
- **Convergence (Lemma 3–5, Theorem 6, Corollary 7).** Two-step linear, then two-step superlinear local convergence, assuming the active set has settled, full step α = 1 and an accurate reduced Hessian; extends Kupfer (1996) with bounds and line search.
- **Global search (Algorithm 2).** Redundant joint values and placement are sampled randomly; analytic IK at the first path point gives up to 8 solutions per robot → up to 8^n_rob seed combinations, optimised in parallel and pruned (Algorithm 1). Infeasible seeds are accepted (even constant trajectories), because placement can move until the path becomes reachable.
- **Multi-segment (§Inter-segment coordinated descend).** Long paths are split into segments solved in parallel; continuity constraints are relaxed with ADMM (augmented Lagrangian, Eq. 23) and a Nesterov-accelerated fast ADMM; the small residual is removed at the end by averaging and a pseudo-inverse correction.

## Evidence
- **Platform.** Two physically coupled KUKA LBR iiwa 14 R820 (7-DoF each, 14 joints) sharing a coupler; computations on an AMD Ryzen 7 PRO 6850U laptop CPU (§Results).
- **Spring pulling (§Pulling a spring).** 14 joints + 5 placement variables, 6 coupling + 6 path constraints → 7 DoF of redundancy; 30 control points per joint, κ = 3. 5000 random seeds → 478 seeds where the first point is reachable by both robots; trajectories initialised as constant (infeasible). Success = rotational error < 0.01 rad and translational error < 10 mm everywhere (also between sample points) and cost decreased (Table 4):
  - Matlab fmincon active set: −51.14% cost, 33.26% success, 9.46 s (large errors between sample points, Fig. 12).
  - Multi-stage successive constraint refinement ([Kabir et al. 2021]): −1.76% cost, 53.97% success, 71.3 s (≈7.2× slower).
  - Proposed reduced Hessian: −39.94% cost, **78.87% success, 8.08 s** mean; previous version (Ye et al. 2022): −36.82%, 65.89 s.
- **Ablation (Table 5).** Full finite differences instead of AD: 17.46 s; reduced finite differences: 13.53 s; without parallelism: 33.45 s (AD) and 50.26 s (reduced FD) — still 23.7% faster than the old method under its original conditions; parallelism gives about a factor 4.
- **Spline sensitivity (Tables 6–8).** For l₁ = 20–85 and κ = 2–10, TCP position error stays below 2 mm except with l₁ = 20; cost reduction weakens for many control points/high order, one failure (lowest l₁, highest κ) attributed to line search; efficient for l₁ ≤ 40, κ ≤ 8. The authors defer sub-mm accuracy to an online tracking MPC (Ye et al. 2024).
- **Multi-segment milling (§Multi-segment milling).** 3-D path with 11 lines and 10 corners, 75 control points, three segments, arbitrary infeasible start. After 30 iterations (Table 9): single segment κ = 3 fails (12.68 mm error, 138.2 s); κ = 4 feasible but −12.89% cost (173.1 s); 3-segment ADMM −19.47% cost, 0.085–0.088 mm max error, 204–209 s. Fast ADMM (Table 10): 19 iterations, ~102 s, −19.5% cost, 0.087–0.117 mm. ADMM did not speed up versus single-segment because of coordination overhead.
- **Real milling (Tables 12–15, Fig. 16–19).** Joint impedance control (Table 11 joint stiffness 1.31–1.91 kN·m/rad). Optimised vs. non-optimised coupled robots: stiffness higher by ≥20.8% (x, feed) and ≥35.1% (z, depth). Coupled vs. single robot with same coupler: ≥9.8% (x), ≥136% (z); coupled also always stiffer than single robot with a shorter adapter. Measured z-stiffness lower than predicted (e.g. Kzz1 predicted 38.9 vs measured 31.9 N/mm) due to unmodelled coupler elasticity (Remark 6).
- **Limits stated by the authors.** Offline planning separated from real-time control (computing times "acceptable" only in that split); velocity limits only via penalties, time law decided afterwards; convergence is local and requires α = 1 / settled active set; rigid-coupler assumption; ADMM brings no speed-up yet; improvements suggested in initial guesses, update ratio and ADMM tuning.

## Relevance for Plan4ARI
- **Deterministic offline baseline for the multi-robot case.** It is the closest work found for *path-constrained, multi-robot, null-space optimisation*, but for **tightly coupled** robots (closed chain, one shared path), i.e. exactly the "joint sampling only for tightly coupled pairs" corner of our design ([[comparisons/welding-mppi-design-review]] flaws 19–21). It does not cover the loosely coupled case (independent seams, others as moving obstacles) of [[sources/streichenberg2023mapi]]-style per-robot MPPI.
- **Building blocks to reuse.** (i) Joint optimisation of **placement + trajectory** with infeasible seeds — directly relevant to our station/AGV placement upstream ([[concepts/base-placement]]); (ii) the interpretable, continuous null-space basis (one column per redundant joint/placement variable per waypoint) is a natural **parametrisation of the MPPI sampling space** (sample d̄ instead of joint noise, then vertical correction), cf. [[sources/wang2024constrainedpi]]; (iii) vertical-step projection as the "exact path" repair after sampling ([[concepts/hybrid-gradient-sampling]]); (iv) seed enumeration "8 AIK branches × sampled redundancy" is the same goal model as our IK-branch modes, here multiplied as 8^n_rob for coupled robots.
- **Speed layer.** Confirms the path–velocity decomposition we assume: geometry q(u) is planned first, s(t) is decided afterwards, and online accuracy is delegated to a downstream MPC (Ye et al. 2024). For welding this means our downstream speed MPC must handle the ±10% band itself, because nothing in this planner guarantees joint-speed feasibility at a given travel speed ([[sources/lange2016pathaccurate]], [[sources/faroni2020scaling]]).
- **Benchmark use.** For a two-robot synchronous welding pair (e.g. distortion-driven simultaneous seams, [[sources/tang2023dualrobotweld]]) this method, together with [[sources/chen2025cooptimization]] and [[sources/weingartshofer2023pathframework]], is the offline optimum against which a receding-horizon MPPI can be compared (cost, restarts, computation).

## Critical assessment (our view)
- **Offline only.** Seconds to minutes per plan (8.08 s on a 7-DoF pair for a short closed path; ~100–200 s for a 3-segment milling path) on a laptop CPU; no receding-horizon variant. It cannot react to seam registration updates, so in our scheme it fits the upstream planning stage (station + nominal null-space seed per segment), not the online look-ahead.
- **Exact equality path only.** Path constraints are equalities of dimension n_path ≤ 6 plus box bounds; free roll could be handled by reducing n_path, but a **10° (anisotropic) cone is an inequality** the method does not support except as penalty — the experiments use full 6-D pose constraints.
- **IK branches as seeds, not modes.** Branches enter only through multi-start; there are no reconfigurations, detach/restart or transfer motions within a path, and the continuous null-space descent cannot change branch. Our reconfiguration logic has no counterpart here.
- **No collisions, no inter-robot avoidance.** Collision avoidance is only mentioned as a possible penalty (Remark 1) and not evaluated; for coupled robots self/inter-robot collision is partly implicit, but for independently welding robots on large structures it is the core problem.
- **Time law missing.** Velocity limits are penalised, not constrained, and the time profile is unknown during planning, so a constant travel speed is not guaranteed — a gap for welding that our λ-based speed check and downstream MPC must fill.
- **Convergence is local** (assumptions on active set, α = 1, BFGS accuracy); global behaviour rests on many seeds (5000 sampled → 478 used) and pruning, i.e. on sampling — which supports the view that sampling (MPPI or multi-start) and gradient null-space steps are complementary.
- Strong points: rigorous constraint handling (sub-0.1 mm path error in milling planning), honest comparison with fmincon and Kabir et al., ablations of AD and parallelism. Only one robot pair/model and one real task; stiffness, not process speed, is the objective.

## Links
- [[concepts/path-wise-redundancy-resolution]]
- [[concepts/hybrid-gradient-sampling]]
- [[concepts/base-placement]]
- [[applications/robotic-welding]]
- [[applications/industrial-manipulators]]
- [[comparisons/welding-mppi-design-review]]
- Related: [[sources/tang2023dualrobotweld]], [[sources/chen2025cooptimization]], [[sources/weingartshofer2023pathframework]], [[sources/demaeyer2017descartes]], [[sources/sun2024nullspacempc]], [[sources/wang2024constrainedpi]], [[sources/streichenberg2023mapi]], [[sources/lange2016pathaccurate]], [[sources/faroni2020scaling]]
- BibTeX key: `ye2026nullspacemultirobot` in `latex/references.bib`
