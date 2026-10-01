---
key: lange2016pathaccurate
title: "Path-Accurate Online Trajectory Generation for Jerk-Limited Industrial Robots"
authors: "Lange, Friedrich; Albu-Schaffer, Alin"
year: 2016
venue: "IEEE Robotics and Automation Letters, vol. 1, no. 1, pp. 82-89"
arxiv: 
doi: 10.1109/lra.2015.2506899
pdf: raw/papers/lange2016pathaccurate.pdf
text: raw/text/lange2016pathaccurate.txt
tags: [trajectory-generation, look-ahead, path-following, industrial, manipulators]
status: read
---

# Path-Accurate Online Trajectory Generation for Jerk-Limited Industrial Robots

*Lange, Friedrich; Albu-Schaffer, Alin* (2016). IEEE Robotics and Automation Letters, vol. 1, no. 1, pp. 82-89.

## TL;DR
An online trajectory generator from DLR. It sits between a robot program, which a sensor may modify, and the position interface of a standard industrial controller. The desired motion is a sequence of sampled 6-axis joint positions. At every control step the generator looks ahead over the next κ̄ samples and checks them against per-axis **velocity, acceleration and jerk limits** (the limits that make a commercial controller abort). It fixes violations in two ways: **forward scaling** (slowing down along the path) and **backtracking** (starting to decelerate earlier). The new contribution is **arc-length interpolation (ALI)**. All scaling acts on a scalar path parameter s, so the commanded samples always stay on the original joint-space polyline (no corner cutting). After a temporary slowdown the trajectory re-synchronises with the original program timing. If everything else fails, a "direct scaling" fallback always returns a feasible command, but that command leaves the path.

## Method
- Problem (§II): given desired joint samples q_d(k), produce commanded samples q_c(k) that (1) satisfy symmetric per-axis bounds on velocity, acceleration and jerk, computed as backward differences (Eq. 1–3); (2) are **path-accurate**, i.e. lie on the straight segments between consecutive q_d samples (Eq. 4); (3) eventually **re-synchronise** with q_d in time (Eq. 5). The path does not need to be differentiable or continuous.
- Forward scaling (§III-A): if a sample violates a limit, one common factor α ∈ (0,1) scales the step of all axes (Eq. 6–11). This is iterated because scaling one axis can make another axis violate its limit (at most as many iterations as axes).
- Direct scaling (§III-B): a last-resort scaling of acceleration or jerk. It is feasible but leaves the path (Fig. 1).
- Backtracking (§III-C): when the look-ahead finds an infeasible sample at k+κ, earlier samples are changed (Eq. 16–20) so the robot decelerates in time instead of overshooting.
- Iterative procedure (§III-D): check κ = 0…κ̄ ahead, then forward-scale or backtrack. The loop ends with success, or with failure if it reaches the current step or runs out of computing time. On failure, direct scaling is applied. κ̄ should cover at least the stopping distance.
- ALI (§IV): prior work [19] interpolated positions directly (direct position interpolation, DPI). ALI instead interpolates a scalar s(k) and maps it back to q through the sampled path (Eq. 26–32, flow chart Fig. 3). It keeps the smallest s over all axes and constraint types. Backtracking with ALI is repeated with a shrinking factor until it is feasible, and a fallback is guaranteed (§IV-B).

## Evidence
- Robot: KUKA KR16, position-controlled at **250 Hz via RSI Ethernet** from an external PC (§V). The abstract states the algorithm can run in every sampling step, e.g. every 4 ms. The per-axis limits are given in Table I, in rad per sampling step (and its powers).
- Experiment 1 (Figs. 6–7): a force sensor detects contact at step 3184, earlier than expected, and the desired trajectory is recomputed.
  - All methods stay feasible. Steps 3184–3186 are not path-accurate because axes 2, 3 and 5 cannot accelerate fast enough.
  - DPI with forward scaling only overshoots and oscillates around the path; the authors judge this "classical" approach unsuitable. DPI with backtracking avoids the overshoot.
  - The logged look-ahead reaches step 3208 = 3187 + κ̄ (§V).
  - Reflexxes (RMLPosition, used outside its intended mode) behaves similarly but ignores path accuracy between samples (§V, footnote 2).
  - ALI decelerates more. It re-joins the desired trajectory later in time but at an earlier point of the path.
- Experiment 2 (Fig. 8): a predictive distance sensor is simulated and the motion is 5× faster.
  - DPI with backtracking blends the vertex (up to 30 iterations).
  - **ALI reproduces the desired path exactly.** The price is a delay k − s(k) of **up to 9.5 sampling steps**, with **at most 56 iterations** per trajectory.
- No CPU times are reported; the real-time claim rests on the 4 ms RSI cycle. Compensating for the robot dynamics is left to future work (§I).

## Relevance for Plan4ARI
- **Template for the speed layer.** This is a concrete, industrial-grade template for the downstream speed layer in [[comparisons/welding-mppi-design-review]].
  - Its input is exactly what MPPI would hand over: a sampled joint path on one IK branch.
  - Its output respects the per-axis v/a/j bounds that a commercial controller enforces.
  - The look-ahead κ̄ (at least the stopping distance) and the per-cycle budget map onto Core-IPC timing (4 ms here, 1 ms in our target).
- **Path–velocity split.** ALI is a discrete, sample-based form of path–velocity decomposition. Only s(t) changes; the geometric path, and with it the seam accuracy in joint space, is untouched. This matches our split: MPPI gives q(s), the speed layer gives s(t).
- **What industrial look-ahead means.** It is a deterministic repair of a nominal timing with a bounded number of iterations, not an optimisation. If MPPI is "a better look-ahead", it must at least match this on guaranteed feasibility and determinism.

## Critical assessment (our view)
- **Synchronisation conflicts with welding.** After a slowdown the method catches up with the original program timing, which means a temporary speed-up. In welding the travel speed must stay within ±10%, so catch-up must be disabled or bounded (for example by re-anchoring the time law instead).
- **The slowdown is unbounded.** Path accuracy is kept by decelerating as much as needed (a delay of up to 9.5 steps in Experiment 2). Nothing keeps the speed inside a band. That information has to come from MPPI upstream, by choosing a null-space path that does not need large slowdowns.
- **Joint-space accuracy only.** Path accuracy is defined in joint space between samples. Cartesian accuracy between samples depends on how dense the samples are, so the MPPI joint path must be sampled densely enough.
- **Limited validation.** The method is purely kinematic (no torque limits, no dynamics) and heuristic (convergence is sped up with empirical factors). It is tested on one contact scenario, with no timing statistics. It is a good baseline, not a certified component.
- **Versus convex scaling.** Compared with convex or predictive scaling ([[sources/faroni2020scaling]], [[sources/palleschi2021fastsafe]]), it handles non-smooth sampled paths without needing path derivatives. That is attractive if MPPI outputs discrete knots.

## Links
- [[comparisons/welding-mppi-design-review]]
- [[applications/industrial-manipulators]]
- [[concepts/smoothness-action-parametrization]]
- [[concepts/mppi-vs-mpc]]
- Related: [[sources/faroni2020scaling]], [[sources/palleschi2021fastsafe]], [[sources/faulwasser2017pathfollowing]], [[sources/ma2025lookahead]]
- BibTeX key: `lange2016pathaccurate` in `latex/references.bib`
