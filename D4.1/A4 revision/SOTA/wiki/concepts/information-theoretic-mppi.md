---
title: Information-theoretic MPPI (the core algorithm)
type: concept
updated: 2026-10-01
---

# Information-theoretic MPPI

**Definition.** Discrete-time MPPI derived from a free-energy / relative-entropy bound; it does not require control-affine dynamics ([[sources/williams2017itmpc]], [[sources/williams2018tro]]).

## Derivation in 4 lines
1. Free energy `F = -λ log E_p[exp(-S(V)/λ)] ≤ E_q[S] + λ KL(q‖p)` (Jensen).
2. Equality for `q*(V) ∝ exp(-S(V)/λ) p(V)` (optimal, intractable).
3. Choose Gaussian `q_U` (mean U, covariance Σ) minimising `KL(q*‖q_U)` → moment matching: `U* = E_{q*}[V]`.
4. Importance sampling from `q_U` with K rollouts → closed-form update.

## Update rule (as used in latex/main.tex, Eq. 3)
```
u_t ← u_t + Σ_k w_k ε_t^k
w_k = exp(-(S̃_k - ρ)/λ) / η,   ρ = min_k S̃_k,  η = Σ_k exp(-(S̃_k - ρ)/λ)
S̃_k = S(V_k) + γ Σ_t u_tᵀ Σ⁻¹ v_t^k,   γ = λ(1-α)
```
- λ (temperature): λ→∞ plain average, λ→0 best sample. Many works auto-tune it to keep the effective sample size η in a band (e.g. 5–10% of K in [[sources/zhang2024m3p2i]]).
- α: trade-off between sampling around the nominal sequence and around zero.
- Warm start: shift U by one step each cycle → anytime / real-time-iteration behaviour.
- Smoothing: Savitzky–Golay filter, splines, or sampling in derivative space ([[concepts/smoothness-action-parametrization]]).

## Interpretations
- Online learning / mirror descent: [[sources/wagener2019dmd]].
- Variational inference: [[sources/okada2020vimpc]], Tsallis generalisation [[sources/wang2021tsallis]].
- Covariance variable importance sampling (first MPPI): [[sources/williams2015covariance]].
- Diffusion / annealing view: [[sources/xue2025dialmpc]], [[sources/pan2024mbd]].

## Known weaknesses → where addressed
| Weakness | Pages |
|---|---|
| soft constraints only | [[concepts/constraints-and-safety]] |
| unimodal proposal, mode averaging | [[concepts/multimodality]] |
| chattering | [[concepts/smoothness-action-parametrization]] |
| sample inefficiency / local minima | [[concepts/sampling-distributions]] |
| disturbances, model error | [[concepts/robustness-uncertainty]] |
| no stability guarantees | [[concepts/mppi-vs-mpc]], [[sources/gandhi2021rmppi]] |
