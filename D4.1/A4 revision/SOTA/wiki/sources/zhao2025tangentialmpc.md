---
key: zhao2025tangentialmpc
title: "Online Motion Generation via Tangential Sampling-Based MPC Around Nonconvex Obstacles"
authors: "Zhao, Guangbao; Jin, Ninglong; Wu, Jianhua; Xiong, Zhenhua"
year: 2025
venue: "IEEE Robotics and Automation Letters, vol. 10, no. 6, pp. 5537-5544"
arxiv: 
doi: 10.1109/lra.2025.3560885
pdf: raw/papers/zhao2025tangentialmpc.pdf
text: raw/text/zhao2025tangentialmpc.txt
tags: [mppi-core, manipulators, sampling, local-minima]
status: read
---

# Online Motion Generation via Tangential Sampling-Based MPC Around Nonconvex Obstacles

*Zhao, Guangbao; Jin, Ninglong; Wu, Jianhua; Xiong, Zhenhua* (2025). IEEE Robotics and Automation Letters, vol. 10, no. 6, pp. 5537-5544.

## TL;DR
**MPPI-Tan**: online joint-space motion generation that escapes local minima behind concave obstacles. The joint velocity is a blend of a **nominal** velocity (linear DS or modulated DS towards q*) and a **tangential** velocity lying in the hyperplane orthogonal to the gradient of the robot–obstacle distance. MPPI samples only the **(n−1) coordinates along an orthonormal tangent basis E(q)**, not the full velocity; a warm-start operator maps the distribution between tangent spaces of successive configurations; a sigmoid weight raises the tangential share near obstacles and near "facing" local minima. Higher success than ModDS, QP, MPPI-ModDS on MotionBenchMaker scenes with a Franka, at 14–95 Hz depending on horizon (CPU/GPU laptop, Python).

## Method
- Distance model (§III-A): learned regressor gives per-link minimum distance and direction to point/sphere obstacles; gradient ∇_qΓ = Jᵀ n (Eq. 1); learned self-distance network.
- MPPI with per-step Gaussian means and covariances and step-size updates (Eq. 3, STORM-style).
- Decision variable (§IV, Eq. 5): u ∈ R^(n−1); q̇_tan = E(q) u, where E(q) is a QR-based orthonormal basis of the tangent space of n(q) = ∇_qΓ (Eq. 4); q̇ = ω_vel q̇_tan + (1−ω_vel) q̇_nom; q integrated with step dt.
- Costs (§IV-A): terminal-only goal distance (Eq. 6, allows temporary detours); consistency cost on successive velocity directions over the first T = 5 steps, decay 0.99 (Eq. 7); path-exploration cost penalising short rollouts (Eq. 8); **binary** collision indicator for environment and self-collision (Eq. 9).
- Warm start across tangent spaces (§IV-B, Eq. 10): μ̂₂ = E(q₂)†E(q₁)μ₁, covariance transformed likewise, plus time shift.
- Dynamic weight (§IV-C, Eqs. 11–12): product of sigmoids of ⟨n(q), q̇_nom⟩ and of obstacle distance relative to a safe distance; forced to 0 within radius δ of the goal to keep the DS convergence; tends to mitigate penetration as the normal component vanishes.

## Evidence
- Implementation (§V): Python, AMD Ryzen R4600H 2.8 GHz CPU, 16 GB RAM, GTX/RTX 1650 GPU; **N = 50 rollouts, H = 15, dt = 0.2 s**; safety distance 0.1 m (reaching) / 0.05 m (benchmark); success = final joint error < 0.02 rad.
- 2-DoF planar arm (§V-A, Fig. 4): illustrates tangential vs nominal components and the weight map.
- Franka reaching task of Koptev et al., 100 trials per obstacle (Table I): Cross-5 ModDS 62 / QP 66 / MPPI-ModDS 100 / MPPI-Tan 100 %; Cross-7 51/53/100/99 %; I-shaped –/–/93/90 %.
- MotionBenchMaker, 400 problems, 300–1000 spheres (Table II): success MPPI-Tan vs best baseline — Thin Bookshelf 97 vs 68 %, Tall Bookshelf 81 vs 67 %, Box 65 vs 40 %, Table Pick 80 vs 58 %. STORM excluded from Table II because its termination error did not meet the tolerance (Fig. 7); occasional STORM collisions reported.
- Rates (Table III): ModDS 472.1 Hz, QP 149.3 Hz, STORM 84.2 Hz, MPPI-ModDS 408.3 (DS) / 7.2 Hz (optimisation); MPPI-Tan **95.3 Hz (H = 2), 41.3 (H = 5), 20.9 (H = 10), 14.2 Hz (H = 15)** — cost linear in H, the distance network ≈ 70 % of time, links evaluated sequentially (§V-D).
- Real robot (§V-E, Fig. 8): 6-DoF JAKA Zu7, bottle transport through a concave obstacle and a shelf; qualitative only; several iterations needed to find the right tangential direction in narrow passages.

## Relevance for Plan4ARI
- Shows that **reparametrising the MPPI decision variable onto a geometry-adapted low-dimensional subspace** (here tangent to obstacles) outperformed joint-velocity sampling (STORM, by termination error, Fig. 7) on cluttered, nonconvex scenes — the same principle as our sampling over **null-space coordinates** (roll, cone, rail) instead of joints ([[comparisons/welding-mppi-design-review]]). The tangent-space warm-start operator (Eq. 10) is a template for warm-starting when the null-space basis changes along the seam.
- Relevant for the large welded structures (concave pockets, stiffeners): local-minimum escape near nonconvex obstacles is a known weakness of joint-space MPPI ([[sources/bhardwaj2021storm]] used as baseline here).
- Timing confirms that **few rollouts (N = 50)** can suffice when the sampled subspace is well chosen, which is encouraging for a CPU budget — but rates drop to 14 Hz at H = 15 in Python with a neural distance model.

## Critical assessment (our view)
- Point-to-point reaching in joint space with a goal configuration; no task-space/path constraint — it cannot be used as-is for seam following, only the parametrisation idea transfers.
- Collision handled by a binary cost; no guarantee of collision-freedom (the DS impenetrability argument is only for the continuous case).
- Baselines use default hyperparameters; STORM's goal cost was modified to joint space and then excluded on a tolerance criterion, which weakens the comparison.
- Sequential (non-batched) tangential computation is the stated bottleneck; the authors limit applicability to static/quasi-static scenes.
- Hardware labelled "RTX1650" in the paper (likely GTX 1650); GPU use is not detailed.

## Links
- [[concepts/multimodality]] · [[concepts/sampling-distributions]] · [[concepts/constraints-and-safety]]
- [[applications/industrial-manipulators]] · [[comparisons/mppi-variants-matrix]] · [[comparisons/welding-mppi-design-review]]
- Related: [[sources/bhardwaj2021storm]] (baseline), [[sources/zhou2025parallelmppi]] (another local-minima escape for manipulator MPPI), [[sources/wang2024constrainedpi]] (null-space projection of samples), [[sources/sun2024nullspacempc]]
- BibTeX key: `zhao2025tangentialmpc` in `latex/references.bib`
