---
key: sun2024nullspacempc
title: "Online Predictive Motion Control of Redundant Robots via Model Predictive Control and Full Null Space Parameterization"
authors: "Sun, Haoxiang; Song, Hanwen"
year: 2024
venue: "2024 IEEE International Conference on Robotics and Biomimetics (ROBIO), pp. 1501-1506"
arxiv: 
doi: 10.1109/robio64047.2024.10907580
pdf: raw/papers/sun2024nullspacempc.pdf
text: raw/text/sun2024nullspacempc.txt
tags: [mpc, redundancy-resolution, manipulators, look-ahead]
status: read
---

# Online Predictive Motion Control of Redundant Robots via Model Predictive Control and Full Null Space Parameterization

*Sun, Haoxiang; Song, Hanwen* (2024). 2024 IEEE International Conference on Robotics and Biomimetics (ROBIO), pp. 1501-1506.

## TL;DR
"Predictive Motion Control" (PMC) is a nonlinear MPC whose decision variables are only the **null-space coordinates** u ∈ R^(n−m). The joint velocity is q̇ = J†ẋ + G(q)u, where G is an orthonormal null-space basis from the SVD of J (full null-space parametrisation, FNSP). The end-effector task is therefore tracked exactly by construction, and the MPC uses foresight to choose the self-motion that avoids future violations of secondary objectives (joint limits, collisions). Two devices make it fast enough to run online:
- **Analytical gradients**, obtained by direct shooting with sensitivity recursion.
- A **"retained rolling" scheme**: at each cycle only the first and last controls of the horizon are re-optimised, and the middle of the sequence is reused from the previous solution.

## Method
- **FNSP** (§II, Eq. 2–4). It replaces the gradient projection method (GPM). The secondary motion is a linear combination of all null-space basis vectors, rather than a projected gradient.
- **MPC problem** (§III-A, Eq. 5). The cost Σ L_k is minimised over u_1…u_np, with Euler integration of q.
  - Constraints: bounds on u, and position, velocity and acceleration limits.
  - Running cost: a secondary objective h(q) plus an exponential penalty on predicted bound violation (Eq. 6), so that a breach predicted later in the horizon can change the current configuration.
- **Shaped velocity constraints** (§III-C, Eq. 7–9). Joint position and acceleration limits are turned into velocity bounds, including a viability term that keeps stopping within acceleration limits.
- **Analytical gradients** (§IV-A, Eq. 10–13). Sensitivity recursion through f(q,u), with derivatives of J† and of the null-space basis G with respect to q.
- **Retained rolling** (§IV-B, Eq. 14–15, Fig. 1). The stored sequence is shifted, only u_{n+1,1} and u_{n+1,np} are optimised, and the early steps are warm-started offline.

## Evidence
- **Test 1: 4-DOF planar arm, joint-limit avoidance along a straight line** (§V-A, Figs. 2–5). The task is 2-D position, so 2 redundant DoF. MATLAB R2020a interior point on a Ryzen 7 6800H, horizon np = 20 with t_ps = 0.1 s.
  - Pseudo-inverse control and GPM both violate a joint limit; PMC moves away from it in advance.
  - Table I: total time for 236 path nodes, 10 runs. NMPC with finite differences: 588.39 ± 10.01 s. With analytical gradients: 20.43 ± 1.05 s. PMC: 8.95 ± 0.58 s.
  - The authors report this as a 98.48% reduction. Our arithmetic: about 38 ms per node for PMC in MATLAB.
- **Test 2: 7-DOF Franka Panda, collision avoidance** (§V-B, Figs. 6–7). NLopt in C++ with ROS/FCI, validated in **Gazebo (simulation)**, where libfranka requires a 1 ms cycle.
  - Task: a spiral, position only, so 4 redundant DoF; same horizon (np = 20, 0.1 s steps). The cost is the clearance of joint 4 from a table.
  - GPM and pseudo-inverse control violate the clearance during [1, 1.5] s; PMC reacts before 1 s.
- **Achievable rate** (§V-B). Up to **100 Hz** with 4 redundant DoF and up to **300 Hz** with 2. When a solve is late, a null joint command is sent.

## Relevance for Plan4ARI
- **The closest deterministic counterpart** to "MPPI over null-space coordinates". It has the same decomposition: the task part is exact, and only the self-motion coordinates are optimised over a horizon with secondary costs. It is therefore a natural **deterministic baseline** for the MPPI look-ahead in [[comparisons/welding-mppi-design-review]] (flaw #24). The secondary costs used here (joint-limit margin, clearance) are among the welding costs.
- **Rates for redundancy size.** It gives realistic gradient-based NMPC rates for 2–4 redundant DoF: 100–300 Hz in C++, well below 1 kHz. This supports keeping MPPI or NMPC as an outer look-ahead layer, with a light speed layer at the Core-IPC rate.
- **Continuity with our group's work.** It extends the predictive-IK line ([[sources/faroni2019pik]], also cited by the authors) with null-space parametrisation instead of a full joint-space QP.

## Critical assessment (our view)
- **Time horizon, not path horizon.** The horizon is in time with a fixed task velocity (2 s), so there is no path–velocity decomposition. With a welding travel speed of a few mm/s, 2 s covers only a few mm of seam, far below our ~10 cm look-ahead. A path-parametrised horizon would be needed.
- **Local, differentiable, single branch.** The method uses an interior-point solver with smooth costs, and the exponential penalty is a soft constraint. It cannot switch IK branches or handle non-smooth costs such as torch-hose wrap or discrete collision checks. This is exactly where MPPI is argued to help ([[concepts/mppi-vs-mpc]]).
- **Retained rolling is an approximation.** Only 2 of the np control vectors are re-optimised each cycle, so the middle of the plan is never re-optimised against new information. This trades optimality for speed, and its effect is not quantified.
- **Weak validation.** Everything is in simulation (MATLAB, Gazebo), and the rates are reported without hardware, solve-time distributions or failure statistics. Orientation is not tracked in the Panda test, whereas welding needs a 5-D task with a cone tolerance, which the method's equality-only task model does not represent.

## Links
- [[comparisons/welding-mppi-design-review]]
- [[concepts/path-wise-redundancy-resolution]]
- [[concepts/mppi-vs-mpc]]
- [[applications/industrial-manipulators]]
- Related: [[sources/faroni2019pik]], [[sources/gao2022taskredundancy]], [[sources/razjigaev2025functional]], [[sources/yin2024dprealtime]]
- BibTeX key: `sun2024nullspacempc` in `latex/references.bib`
