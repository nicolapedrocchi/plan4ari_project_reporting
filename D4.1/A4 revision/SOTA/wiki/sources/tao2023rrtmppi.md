---
key: tao2023rrtmppi
title: "RRT Guided Model Predictive Path Integral Method"
authors: "Tao, Chuyuan; Kim, Hunmin; Hovakimyan, Naira"
year: 2023
venue: "2023 American Control Conference (ACC), pp. 776-781"
arxiv: 2301.13143
doi: 10.23919/acc55779.2023.10155837
pdf: raw/papers/tao2023rrtmppi.pdf
text: raw/text/tao2023rrtmppi.txt
tags: [mppi-core, sampling, hybrid, path-planning, guidance]
status: read
---

# RRT Guided Model Predictive Path Integral Method

*Tao, Chuyuan; Kim, Hunmin; Hovakimyan, Naira* (2023). 2023 American Control Conference (ACC), pp. 776-781.

## TL;DR
An RRT path, computed offline and repaired online by a local "replanning RRT", is turned into a **nominal control** (Lyapunov/PD tracking law) that is used as the **time-varying mean** of the MPPI sampling distribution. MPPI still explores around it and penalises obstacles, so the RRT path only has to be roughly right. A sample-complexity argument (Hoeffding + Chebyshev bounds) shows that the number of samples MPPI needs grows with the magnitude of the sampling mean, which motivates a mean that is "just large enough" and supplied by a planner rather than hand-tuned. Validated only on a simulated 2-D unicycle.

## Method
- **Guide** (§III-A, Alg. 1): standard RRT from start to goal (projection radius γ), run once offline → nominal path p_n.
- **Nominal control** (§III-C, Eq. 19): the nearest point of p_n is tracked by a Lyapunov law for linear velocity and a P law for heading; u_n = L(s, x) becomes the mean of N(u_n, Σ).
- **MPPI** (§III-B, Eqs. 3–6): K rollouts with quadratic goal cost plus a large indicator penalty on obstacle states; exponential weights with min-cost baseline subtraction.
- **Replanning trigger** (§III-C, Alg. 2): if the robot drifts farther than a radius R from p_n, a replanning RRT grows from the current state until it reconnects to the old path or reaches the goal; no tree trimming because obstacle avoidance is left to MPPI's cost.
- **Sample-size analysis** (§IV, Theorem 1, Eqs. 12–18): with quadratic costs (Assumption 1), the sample size K₁ for the weight normaliser is independent of the mean, while K₂ for the weighted control average scales with Γ = 2(Var[δu] + E[δu]²); hence a larger sampling mean requires more samples. Small means instead under-explore (Fig. 1).

## Evidence
- **Platform**: simulation only, kinematic unicycle with steering state (4 states, 2 inputs), Δt = 0.05 s (§V-A). MacBook Air M1 laptop (§V-C).
- **Settings** (§V-B): RRT up to 20 000 samples, γ = 0.5; MPPI K = 10 000 rollouts, horizon 20 steps, λ = 1.0; obstacle penalty 1000·indicator.
- **Motivation** (Fig. 1–2): fixed means μ = [0,0], [1,0], [1,1] respectively fail to reach the goal, succeed, or violate safety; μ = [1,0] fails when obstacle radii grow by 4 at t = 0.5 s.
- **Results** (Fig. 3–4): RRT-MPPI solves static and two dynamic scenes (obstacle radii +2 and +4); over 10 repetitions with R ∈ [2, 8], R = 6 gives the shortest task time; the offline RRT alone takes around 0.2 s, which the authors consider too slow for real-time use.
- **Table I** (sample-size bound at T·Δt = 2.5 s, ε₁ = 0.02, ε₂ = 0.1, ρ₁ = 0.05, ρ₂ = 0.1): K₁ = 9222 for both; K₂ = 11 413 (fixed-mean MPPI) vs 6122 (RRT-MPPI); running time 21.81 s vs 14.56 s.
- No per-cycle MPPI computation time is reported; no hardware experiment.

## Relevance for Plan4ARI
- It is the simplest template of **"sampling-based planner provides the MPPI mean"**, which is our VAMP → MPPI interface ([[comparisons/welding-mppi-design-review]], [[sources/thomason2024vamp]]). In our design the analogous guide is (i) the VAMP transfer path for approach/retract motions and (ii) the nominal analytic-IK path of each branch along the seam, used as the mean around which MPPI samples the null-space coordinates.
- The replanning trigger "distance from the guide > R" is a cheap rule we can reuse to decide when to re-call VAMP (e.g. after a large seam-registration correction).
- Theorem 1 is a qualitative argument for **centring samples on a good nominal** (warm start from the previous cycle or the IK seed) rather than on zero perturbation: it lowers the sample count needed for a given accuracy — relevant for a CPU budget of ~128 rollouts per goal.
- Same family as biased/ancillary-controller sampling ([[sources/trevisan2024biasedmppi]]) and planner-informed distributions ([[concepts/sampling-distributions]]).

## Critical assessment (our view)
- Toy setting: 2-D unicycle, quadratic distance-to-goal cost, single guide path. No manipulator, no multimodality (one RRT path = one homotopy class), no comparison with other informed-mean MPPI variants.
- The guide is used only through a tracking controller; the planner's cost is not fed to MPPI as cost-to-go, so the myopia issue of our flaw #1/#3 is not addressed.
- The sample-size result rests on quadratic costs (Assumption 1) and a 1-D input; it bounds Monte-Carlo error of the update, not closed-loop performance. The indicator obstacle cost used in the experiments is not quadratic, so the theorem does not formally cover them.
- Minor inconsistencies: horizon 20 steps in §V-B vs T = 50 steps used for Table I; "running time" in Table I appears to be total task time, not computation time.
- The RRT is randomised: different guides yield different MPPI behaviour, which the paper does not quantify — the same caveat we raised for the two-pass VAMP scheme.

## Abstract (verbatim, arXiv)
> This work presents an optimal sampling-based method to solve the real-time motion planning problem in static and dynamic environments, exploiting the Rapid-exploring Random Trees (RRT) algorithm and the Model Predictive Path Integral (MPPI) algorithm. The RRT algorithm provides a nominal mean value of the random control distribution in the MPPI algorithm, resulting in satisfactory control performance in static and dynamic environments without a need for fine parameter tuning. We also discuss the importance of choosing the right mean of the MPPI algorithm, which balances exploration and optimality gap, given a fixed sample size. In particular, a sufficiently large mean is required to explore the state space enough, and a sufficiently small mean is required to guarantee that the samples reconstruct the optimal controls. The proposed methodology automates the procedure of choosing the right mean by incorporating the RRT algorithm. The simulations demonstrate that the proposed algorithm can solve the motion planning problem in real-time for static or dynamic environments.

## Links
- [[concepts/sampling-distributions]] · [[concepts/hybrid-gradient-sampling]] · [[concepts/information-theoretic-mppi]]
- [[comparisons/welding-mppi-design-review]]
- Related: [[sources/thomason2024vamp]], [[sources/trevisan2024biasedmppi]], [[sources/wang2026mppiem]], [[sources/belvedere2026feedbackmppi]]
- BibTeX key: `tao2023rrtmppi` in `latex/references.bib`
