---
key: wang2026mppiem
title: "Generalized Model Predictive Path Integral Control as Expectation-Maximization"
authors: "Wang, Jiarui; Sharifi, Sina; Fazlyab, Mahyar"
year: 2026
venue: "IEEE Control Systems Letters, vol. 10, pp. 2119-2124"
arxiv: 2606.00317
doi: 10.1109/lcsys.2026.3709158
pdf: raw/papers/wang2026mppiem.pdf
text: raw/text/wang2026mppiem.txt
tags: [mppi-core, theory, variational, multimodal]
status: read
---

# Generalized Model Predictive Path Integral Control as Expectation-Maximization

*Wang, Jiarui; Sharifi, Sina; Fazlyab, Mahyar* (2026). IEEE Control Systems Letters, vol. 10, pp. 2119-2124.

## TL;DR
Treating the control sequence as a latent variable and "optimality" as a Bernoulli observation with likelihood exp(−(J − J*)/τ), one MPPI update is exactly one **EM iteration**: the E-step is Boltzmann reweighting of the current proposal, the M-step a weighted maximum-likelihood fit of the next proposal. This gives (i) a recipe for MPPI with any sampling family that admits a weighted-MLE update (e.g. Gaussian mixtures), (ii) monotone likelihood ascent and convergence to stationary points from classical EM theory, (iii) a local linear rate set by Cov_q[u]·Σ⁻¹ for Gaussian MPPI, and (iv) a sufficient-increase bound with constant λ_min(Σ). Only Dubins-car toy experiments.

## Method
- **Inference model** (§IV, Eqs. 3–5): log-likelihood ℓ(θ) = log E_{p(u;θ)}[exp(−J(u)/τ)] + const; ELBO = −E_q[J]/τ − KL(q‖p_θ).
- **E-step** (Eq. 6): q(u;θ) ∝ p(u;θ) exp(−J(u)/τ) — the usual MPPI posterior, never formed explicitly.
- **M-step** (Eqs. 7–10): maximise Σ w_i log p(u_i; θ⁺) with self-normalised weights; Gaussian with fixed Σ gives μ⁺ = Σ w_i u_i, i.e. standard MPPI (Eq. 15). Algorithm 1 = "Generalized MPPI".
- **Convergence** (§IV-C): Theorem 1 — under regularity of the sampling density and coercive J (no differentiability of dynamics or cost needed), ℓ increases strictly at non-stationary points, converges, and limit points are stationary. Theorem 2 — local linear rate ρ(∂M(θ*)) < 1 with ∂M = −(∇²₁₁Q)⁻¹∇²₁₂Q.
- **Exponential family** (§V, Theorem 3): M-step = moment matching; if the log-partition A(η) is α-strongly convex, ℓ(η⁺) − ℓ(η) ≥ (α/2)‖η⁺ − η‖². Remark 2: with N samples the bound holds up to an O(N^-1/2) moment-estimation error.
- **Special cases** (§VI): Gaussian MPPI — local rate governed by Cov_q[u] Σ⁻¹, global increase with α = λ_min(Σ) (Eq. 16); Mixture-of-Gaussians MPPI — M-step solved by an inner EM over component responsibilities.

## Evidence
- **Platform**: simulation only, Dubins car (3 states, angular-velocity input bounded in ±3π/2, constant forward speed), at least 1024 feasible trajectories per update (§VII).
- **Sufficient increase** (§VII-A, Fig. 1): 20 iterations on an obstacle-free goal-reaching problem; the Monte-Carlo log-likelihood estimate stays above the lower bound of Eq. 16.
- **Cluttered navigation** (§VII-B, Fig. 2, Table I): Gaussian vs 2-component MoG, 1 or 5 EM iterations per control step. Total samples / rejected fraction: Gaussian-1 268 288 / 56.11%; Gaussian-5 1 083 392 / 45.65%; MoG-1 239 616 / 50.85%; MoG-5 1 092 608 / 46.11%. Gaussian averages left/right modes and heads into the obstacle.
- **Mode switching** (App. D, Fig. 3): when an obstacle grows, MoG keeps a minority left-turn component and switches to it at iteration 16; Gaussian, collapsed onto the right mode by iteration 10, does not recover.
- No computation times, no robot hardware.

## Relevance for Plan4ARI
- Gives the **theoretical justification** for two choices in our welding design ([[comparisons/welding-mppi-design-review]]): (a) running a few MPPI iterations per cycle is likelihood ascent with monotone improvement (in the large-sample limit), useful when arguing convergence of the null-space optimisation in D4.1; (b) the local rate Cov_q[u]Σ⁻¹ says that a sampling covariance much wider than the posterior speeds convergence only if enough samples resolve it — consistent with keeping the null space low-dimensional.
- The MoG case and the mode-switching experiment support our **multi-goal scheme**: keep one component per IK branch / goal rather than a single Gaussian that would blend branches (our flaw #7, "select, never blend"). EM-MPPI frames this as a mixture whose weights π_l are re-estimated each cycle — a principled form of branch selection with hysteresis (flaw #8) if π_l are smoothed over time. Caveat: across IK branches we must forbid the averaging that a single shared mean would do; a mixture keeps per-component means, which is what we need.
- Complements [[concepts/information-theoretic-mppi]] and [[concepts/sampling-distributions]]; related variational views: [[sources/okada2020vimpc]], [[sources/wang2021tsallis]], [[sources/lambert2020svmpc]].

## Critical assessment (our view)
- Analysis is for the **exact** expectation (population) update; finite-sample effects only via Remark 2, and receding-horizon closed-loop behaviour is explicitly left as future work by the authors. Covariance adaptation is not analysed (Σ fixed).
- Guarantees are to stationary points of a likelihood surrogate of J (temperature-dependent), not to minimisers of J; for small τ the surrogate approaches min J but weights degenerate.
- Experiments are minimal (2-D car, no timings, no statistics over seeds); Table I shows MoG and Gaussian with similar rejection rates, so the practical benefit is mostly the qualitative mode preservation of Fig. 3.
- Some proofs are deferred to a "longer version" (Theorems 1–2 detail).

## Abstract (verbatim, arXiv)
> Model Predictive Path Integral (MPPI) control is a powerful sampling-based method for solving stochastic optimal control problems and has enabled real-time control in complex robotic systems. Despite its empirical success, its theoretical understanding remains limited. In this work, we show that MPPI can be interpreted as a special case of the Expectation-Maximization (EM) algorithm applied to a probabilistic inference formulation of optimal control. This perspective leads to a generalized EM-MPPI framework that extends MPPI beyond the commonly used Gaussian parameterization. We analyze the convergence behavior of this algorithm and characterize the local convergence rate in terms of the covariance of the posterior trajectory distribution and the exploration distribution. For exponential-family distributions, we establish a sufficient increase property of the log-likelihood when the log-partition function is strongly convex. Specializing the analysis to Gaussian MPPI yields explicit global and local convergence characterizations. The code for the experiments will be available upon acceptance.

## Links
- [[concepts/information-theoretic-mppi]] · [[concepts/sampling-distributions]] · [[concepts/multimodality]] · [[concepts/path-integral-control]]
- [[comparisons/welding-mppi-design-review]]
- Related: [[sources/okada2020vimpc]], [[sources/wang2021tsallis]], [[sources/lambert2020svmpc]], [[sources/liu2026clusteringmppi]], [[sources/zhang2024m3p2i]], [[sources/tao2023rrtmppi]], [[sources/belvedere2026feedbackmppi]]
- BibTeX key: `wang2026mppiem` in `latex/references.bib`
