---
key: fazlyab2026mppigd
title: "Model Predictive Path Integral Control as Preconditioned Gradient Descent"
authors: "Fazlyab, Mahyar; Sharifi, Sina; Wang, Jiarui"
year: 2026
venue: "IEEE Control Systems Letters, vol. 10, pp. 2089-2094"
arxiv: 
doi: 10.1109/lcsys.2026.3708745
pdf: raw/papers/fazlyab2026mppigd.pdf
text: raw/text/fazlyab2026mppigd.txt
tags: [theory, mppi-core, hybrid, convergence]
status: read
---

# Model Predictive Path Integral Control as Preconditioned Gradient Descent

*Fazlyab, Mahyar; Sharifi, Sina; Wang, Jiarui* (2026). IEEE Control Systems Letters, vol. 10, pp. 2089-2094.

## TL;DR
Theory letter: constrained trajectory optimisation is lifted to a KL-regularised problem over distributions; eliminating the decision distribution leaves a **free-energy objective F(θ) = −τ log Z(θ)** over the sampling-distribution parameters. Preconditioned gradient descent on F with a fixed-covariance Gaussian, preconditioner P = Σ/τ and unit step **is exactly the classical MPPI update**. Under a bounded-Hessian (smoothness) assumption the exact (infinite-sample) iteration is a descent method with O(1/K) ergodic stationarity; for the Gaussian case a sufficient condition for unit-step descent is that the **sampling covariance is not too small w.r.t. the feasible-set diameter** (λ_min(Σ) ≥ D²/12). It also motivates step sizes ≠ 1, multiple inner iterations per control step ("M-MPPI") and a gradient-norm stopping rule.

## Method
- §II: problem min f₀(u) over a compact feasible set C (obstacles, state bounds, input limits). Lifted problem: min_ρ E_ρ[f₀] + τ KL(ρ‖π) with supp(ρ) ⊆ C (Eq. 2). Optimal ρ is the **truncated Gibbs tilt** of π: weights exp(−f₀/τ)·1_C (Eq. 4) — infeasible samples get zero weight. Optimising π over a family Π gives the free energy (Eq. 7).
- §III: gradient and Hessian of F for any parametric family (Lemma 1, Eqs. 10–13); self-normalised importance-sampling estimator of the gradient (Eqs. 15–16). Theorem 1: with L_P-smoothness in the P-metric and 0 < η < 2/L_P → monotone descent, summable gradients, min-gradient bound O(1/K) (Eqs. 19–21). Algorithm 1 = multi-step MPPI with stopping on ‖∇F‖_P.
- §IV: fixed-covariance Gaussian; with P = Σ/τ, η = 1 the update becomes the weighted sample mean (Eqs. 26–27) = MPPI. Preconditioned Hessian = I − Σ^(−1/2) Cov_ρ(u) Σ^(−1/2) (Eq. 28), independent of τ. Theorem 2: L_Σ ≤ max{1, D²_Σ⁻¹/4 − 1} (Eq. 31) → unit-step MPPI descends if D²_Σ⁻¹ < 12.
- Remark 1: the sampled (biased, self-normalised) update keeps the descent inequality up to bias and variance terms; a non-asymptotic finite-sample analysis is left open.

## Evidence
- Only numerical illustrations; no robot hardware, no computation platform specified.
- LQR (§V-A, Fig. 1): double integrator, T = 10 (u ∈ R¹⁰), |u| ≤ 1 and box state constraints, N = 1000 samples/iteration. Ablations over Σ and τ comparing η = 1 with η = 1/L_Σ; when L_Σ is small (e.g. 0.1) η = 1 is conservative and a larger step converges faster. Multi-step MPPI converges further than finite differences (Fig. 1 right).
- Dubins car in clutter (§V-B, Fig. 2, Table I): T = 20, N = 1024, 3 seeds. Average cost of chosen trajectory: MPPI (K = 1) 26.14, Log-MPPI 24.3, M-MPPI K = 5 23.98, K = 10 23.85; runtime column 16.8 s, 17.1 s, 34.4 s, 47.8 s respectively (units as printed, setup details in the "longer version"); sample acceptance 0.75–0.80 %. Single-iteration MPPI selects a suboptimal path (Fig. 2).

## Relevance for Plan4ARI
- Gives the formal answer to "MPPI vs gradient methods" needed in D4.1: MPPI is a **preconditioned gradient step on a smoothed (free-energy) objective**, so hybrid gradient-sampling schemes ([[concepts/hybrid-gradient-sampling]]) and multiple MPPI iterations per cycle are principled, with step size and stopping rule as tunable knobs. Complements the mirror-descent view in [[sources/wagener2019dmd]] and [[concepts/information-theoretic-mppi]].
- Design rule for our welding look-ahead ([[comparisons/welding-mppi-design-review]]): the null-space domain (roll + cone ≤ ~10° + rail) is **bounded and small**, so the condition "covariance large w.r.t. feasible-set diameter" is easy to meet → unit-step MPPI is in its guaranteed-descent regime; an over-tight Σ (to get smooth motion) is what breaks the guarantee.
- Since the welding cycle has time budget (slow travel), several inner MPPI iterations per cycle (M-MPPI) with a ‖∇F‖ stop are justified, warm-started each cycle.
- Hard feasibility via 1_C (zero weight for infeasible samples) matches "select feasible rollouts only" — relevant to exact-IK / joint-limit rejection in our design ([[concepts/constraints-and-safety]]).

## Critical assessment (our view)
- Guarantees hold for the **exact expectation** iteration of the open-loop problem at a fixed x₀; finite-sample bias, receding-horizon shifting and closed-loop behaviour are explicitly not covered.
- Convergence is to a **stationary point of the smoothed free energy**, not to a global/feasible optimum of f₀; multimodality (IK branches) is untouched — select-never-blend remains necessary ([[concepts/multimodality]]).
- With 1_C in the weights, if no sample is feasible the update is undefined; in practice soft penalties are still needed.
- Experiments are toy-sized; the Table I runtimes cannot be used as robot timing references.
- "First convergence analysis for general nonlinear systems" is the authors' claim; related analyses (CoVO-MPC, MPPI optimality studies) are cited as complementary.

## Links
- [[concepts/hybrid-gradient-sampling]] · [[concepts/information-theoretic-mppi]] · [[concepts/path-integral-control]] · [[concepts/sampling-distributions]]
- [[comparisons/mppi-variants-matrix]] · [[comparisons/welding-mppi-design-review]]
- Related: [[sources/wagener2019dmd]] (dynamic mirror descent), [[sources/okada2020vimpc]] (variational inference MPC), [[sources/mohamed2022logmppi]] (Log-MPPI baseline), [[sources/pan2024mbd]], [[sources/xue2025dialmpc]] (diffusion view), [[sources/homburger2023nmppi]]
- BibTeX key: `fazlyab2026mppigd` in `latex/references.bib`
