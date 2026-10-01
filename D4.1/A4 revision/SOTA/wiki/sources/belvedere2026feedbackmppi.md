---
key: belvedere2026feedbackmppi
title: "Feedback-MPPI: Fast Sampling-Based MPC via Rollout Differentiation - Adios Low-Level Controllers"
authors: "Belvedere, Tommaso; Ziegltrum, Michael; Turrisi, Giulio; Modugno, Valerio"
year: 2026
venue: "IEEE Robotics and Automation Letters, vol. 11, no. 1, pp. 1-8"
arxiv: 2506.14855
doi: 10.1109/lra.2025.3630871
pdf: raw/papers/belvedere2026feedbackmppi.pdf
text: raw/text/belvedere2026feedbackmppi.txt
tags: [mppi-core, hybrid, mpc, gpu]
status: read
---

# Feedback-MPPI: Fast Sampling-Based MPC via Rollout Differentiation - Adios Low-Level Controllers

*Belvedere, Tommaso; Ziegltrum, Michael; Turrisi, Giulio; Modugno, Valerio* (2026). IEEE Robotics and Automation Letters, vol. 11, no. 1, pp. 1-8.

## TL;DR
F-MPPI differentiates the MPPI weighted-average update with respect to the initial state, obtaining a **local linear feedback gain F = ∂u*/∂x₀** (the sampling-based analogue of Riccati/DDP gains). MPPI runs at low rate (50 Hz) and an inner loop applies u = u* + F(x̂ − x_sp) at 200–500 Hz, removing the need for a separately tuned tracking controller. Cost gradients of each rollout are computed by JAX autodiff in parallel with the rollouts; the overhead is roughly 40–70% of MPPI runtime. Shown on a simulated quadruped, a real quadrotor (onboard Jetson Orin NX), a hybrid 1-D hopper and quadrotor obstacle navigation.

## Method
- **Base MPPI** (§II-A, Eqs. 1–5): parameters θ (direct inputs or splines) sampled from N(θ̄, Σ); weights with min-cost baseline; θ* = θ̄ + Σ ω_k Δθ_k; inputs clipped inside the parametrisation.
- **Gain derivation** (§II-B, Eqs. 6–13): chain rule through the weights gives ∂ω_k/∂x₀ = (ω_k/λ)(Σ_j ω_j ∂J_j/∂x₀ − ∂J_k/∂x₀); F is the weighted covariance between parameter perturbations and rollout-cost gradients, mapped through the policy parametrisation. Setpoint x_sp is linearly interpolated between x₀ and x₁ (footnote 1).
- **Requirements** (Remarks 1–2): dynamics and costs must be locally differentiable along rollouts; indicator (constant) constraint penalties contribute nothing to F, so constraints are invisible to the feedback unless written as smooth barriers; clipped inputs give ∂π/∂θ = 0, so gains correctly vanish when saturated.
- **Implementation** (§II-C): open-source JAX library, JIT on CUDA GPUs, per-rollout cost gradients by autodiff together with the rollouts.
- **Sanity check** (§II-D, Fig. 2): on an inverted pendulum, MPPI gains approach the infinite-horizon LQR gains as K grows from 10³ to 10⁶ (linear and nonlinear rollouts); with input saturation they go to zero.

## Evidence
- **Quadruped (sim, MuJoCo, Aliengo SRBD model)** (§III-A, Tab. I, Fig. 3): N = 10, δt = 0.02 s, K = 5000, linear-spline GRF parametrisation; i7-13700H + RTX 4050 laptop. F-MPPI ≈ 3 ms per run vs MPPI ≈ 2 ms. F-MPPI at 50 Hz with gains applied at 500 Hz; velocity tracking MAE over 50 trials competitive with MPPI at 100 Hz and better than MPPI at 80 Hz (similar compute budget).
- **Quadrotor (real, MikroKopter, Jetson Orin NX 16 GB onboard)** (§III-B, Tab. II, Fig. 4): N = 15, δt = 0.05 s, K = 800, cubic splines with 5 knots. MPPI at its maximum feasible 66.7 Hz vs F-MPPI at 50 Hz + 200 Hz gain loop. Post-transient RMSE x/z: 0.017/0.027 m (F-MPPI) vs 0.048/0.038 m (MPPI), i.e. −64.6% / −28.9%; visibly smoother rotor commands.
- **Computation** (Fig. 5): Jetson Orin NX (1024 CUDA cores), K ∈ {400, 800, 1200}, horizon 10–25 steps: gain computation adds roughly 40–70% to runtime, upper end when K = 1200 exceeds the GPU cores.
- **Discontinuous problems** (§III-C, Figs. 6–7): 1-D hopper (MuJoCo MJX, hybrid contact) at 50 Hz + 500 Hz gains keeps bouncing under noise where plain MPPI gets stuck; quadrotor obstacle navigation with indicator penalties reaches the goal in about 4 s.

## Relevance for Plan4ARI
- Directly answers whether MPPI feedback can **replace or complement the downstream MPC** in our path–velocity decomposition ([[comparisons/welding-mppi-design-review]], "Downstream MPC"). F-MPPI gives a cheap high-rate local policy around the MPPI solution, so the look-ahead MPPI could run at tens of Hz while a kHz-ish loop corrects small tracking deviations — without a second optimiser.
- **But** it does not replace the hard-constraint role we assigned to the downstream layer: the gains ignore inequality constraints written as indicators (Remark 2), and there is no guarantee on joint velocity/acceleration limits or on the ±10% travel-speed band. Our view: F-MPPI is a candidate for the inner tracking of the null-space/roll coordinates, while speed scaling along s stays a convex 1-DoF layer ([[sources/faroni2020scaling]], [[sources/palleschi2021fastsafe]]) or a path-following NMPC ([[sources/faulwasser2017pathfollowing]]).
- Requires differentiable rollout costs: analytic IK + FK are differentiable on a branch, but collision and branch selection are not — gains would only capture the smooth part (λ time-dilation cost, cone/roll penalties), which is acceptable for local correction.
- Overhead figure (+40–70%) is a useful planning number for our compute budget if we adopt it.
- Fits [[concepts/hybrid-gradient-sampling]] (gradients used *after* sampling, not to steer samples) and [[concepts/mppi-vs-mpc]] (Riccati-like feedback brought to sampling MPC).

## Critical assessment (our view)
- Platforms are floating-base robots with low-dimensional reduced models (SRBD, rigid-body quadrotor); no manipulator and no task with sub-mm path accuracy. Benefit is shown against plain MPPI, not against MPPI + a tuned low-level tracker (the usual industrial setup), so the "adios low-level controllers" claim is only partially tested.
- The quadrotor result is a single goal-reaching manoeuvre; RMSE from one trial. Quadruped evidence is simulation only.
- The gain is a local first-order approximation that is noisy at low K (Fig. 2 variance) and blind to active-set changes; the authors note it is heavier than Riccati/NLP-sensitivity approaches and list constraint-aware gains and cheaper backpropagation as future work.
- GPU + autodiff (JAX) is assumed; on our CPU-oriented design the per-rollout gradient cost must be re-evaluated (analytic Jacobians would be cheaper than autodiff).

## Abstract (verbatim, arXiv)
> Model Predictive Path Integral control is a powerful sampling-based approach suitable for complex robotic tasks due to its flexibility in handling nonlinear dynamics and non-convex costs. However, its applicability in real-time, highfrequency robotic control scenarios is limited by computational demands. This paper introduces Feedback-MPPI (F-MPPI), a novel framework that augments standard MPPI by computing local linear feedback gains derived from sensitivity analysis inspired by Riccati-based feedback used in gradient-based MPC. These gains allow for rapid closed-loop corrections around the current state without requiring full re-optimization at each timestep. We demonstrate the effectiveness of F-MPPI through simulations and real-world experiments on two robotic platforms: a quadrupedal robot performing dynamic locomotion on uneven terrain and a quadrotor executing aggressive maneuvers with onboard computation. Results illustrate that incorporating local feedback significantly improves control performance and stability, enabling robust, high-frequency operation suitable for complex robotic systems.

## Links
- [[concepts/hybrid-gradient-sampling]] · [[concepts/mppi-vs-mpc]] · [[concepts/smoothness-action-parametrization]]
- [[comparisons/welding-mppi-design-review]]
- Related: [[sources/faulwasser2017pathfollowing]], [[sources/faroni2020scaling]], [[sources/palleschi2021fastsafe]], [[sources/verschueren2022acados]], [[sources/tao2023rrtmppi]], [[sources/wang2026mppiem]]
- BibTeX key: `belvedere2026feedbackmppi` in `latex/references.bib`
