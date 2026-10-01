---
key: zhang2024m3p2i
title: "Multi-Modal MPPI and Active Inference for Reactive Task and Motion Planning"
authors: "Zhang, Yuezhe; Pezzato, Corrado; Trevisan, Elia; Salmi, Chadi; Hernandez Corbato, Carlos; Alonso-Mora, Javier"
year: 2024
venue: "IEEE Robotics and Automation Letters, vol. 9, no. 9, pp. 7461-7468"
arxiv: 2312.02328
doi: 10.1109/LRA.2024.3426183
pdf: raw/papers/zhang2024m3p2i.pdf
text: raw/text/zhang2024m3p2i.txt
tags: [tamp, multimodal, mobile-manipulation, key-paper]
status: summarised
---

# Multi-Modal MPPI and Active Inference for Reactive Task and Motion Planning

*Zhang, Yuezhe; Pezzato, Corrado; Trevisan, Elia; Salmi, Chadi; Hernandez Corbato, Carlos; Alonso-Mora, Javier* (2024). IEEE Robotics and Automation Letters, vol. 9, no. 9, pp. 7461-7468.

## TL;DR
M3P2I: Active Inference planner returns N alternative symbolic plans -> N cost functions; multi-modal MPPI samples N*K rollouts in IsaacGym, per-mode weights with auto-tuned temperature, blended into one command. Reactive push/pull and pick-place.

## Method
AIP + BT (1 Hz), plan interface (action->cost), M3P2I (25 Hz) with Halton splines, per-mode beta_i so eta_i in 5-10% of K, joint re-weighting.

## Evidence
Push-pull omni base: multimodal 0.1052 pos err, 0.0041 ori err, 3.8 s vs push 6.2 s / pull 25.1 s; corner case push times out. Pick-place reactive: 0.0117 vs RL 0.0246. Real Franka experiments with disturbances.

## Relevance for Plan4ARI
Key paper for Plan4ARI: alternative strategies sampled at motion level. Limits: blending may average modes, soft constraints, N*K physics cost, no human safety.

## Detailed notes (from full text)
- **Problem**: reactive TAMP under run-time geometric uncertainty and disturbances (moved/stolen objects, dynamic obstacles, corner configurations where a single skill fails).
- **Architecture** (Fig. 1 of the paper): symbolic observer -> Active Inference planner (AIP) + Behaviour Tree -> *N* alternative symbolic plans -> plan interface (database action -> cost function) -> M3P2I -> robot. AIP at ~1 Hz, M3P2I at 25 Hz.
- **AIP change**: instead of stopping at the first executable action, the search is repeated removing the found action, so all alternative first actions are returned (Alg. 2).
- **M3P2I** (Alg. 4):
  - *N* alternatives x *K* samples; noise = Halton splines (from STORM [[sources/bhardwaj2021storm]]); rollouts in IsaacGym [[sources/makoviychuk2021isaacgym]] as in [[sources/pezzato2025isaacmppi]].
  - Per-alternative cost S_i(V_k) = sum_t gamma^t C_i(x_t,k, v_t,k); weights omega_i = exp(-(S_i - rho_i)/beta_i)/eta_i.
  - Inverse temperature beta_i auto-tuned *within a rollout* so that eta_i (effective samples) stays in [5%,10%] of K (Alg. 3: beta*0.9 if eta too large, beta*1.2 if too small).
  - Per-mode means mu_i, then joint weights over the concatenated costs and update u_t = (1-alpha_u) u_{t-1} + alpha_u sum_k w_k v_t,k (alpha_u = step size).
- **Costs**: push / pull with distance, orientation (axis alignment, symmetric objects), alignment h(cos theta), pull-only suction-like constraint, dynamic-obstacle cost with constant-velocity prediction; pick-place with reach (tilt parameter psi for top vs side grasp), gripper and placement costs.
- **Results**: Table I (push-pull, 20 trials per case): middle->corner multimodal pos 0.1052, ori 0.0041, time 3.78 s vs push 6.21 s and pull 25.10 s; corner->corner push time-out, multimodal 9.95 s. Table II: vanilla pick-place ours 0.0075 vs RL 0.0042 (RL trained 1500 epochs); reactive with disturbances ours 0.0117 vs RL 0.0246. Real Franka: dynamic obstacle, displaced target, stolen cube, top/side grasp blending.
- **Authors' discussion**: sampling alternatives slightly biases the distribution towards less effective strategies (cf. [[sources/trevisan2024biasedmppi]]); cost weights need tuning (auto-tuning suggested); symbolic templates are manual; online system identification could help with model uncertainty ([[sources/abraham2020emppi]]).

## Critical assessment (our view)
1. Blending of modes after weighting can average incompatible strategies -> see [[sources/liu2026clusteringmppi]], [[sources/honda2024svgmppi]], [[concepts/multimodality]].
2. Obstacle avoidance and limits are soft costs -> see [[concepts/constraints-and-safety]].
3. Compute grows as N*K physics rollouts; real-time only with few alternatives and a GPU.
4. No human model or safety-standard compliance -> see [[applications/human-robot-shared-spaces]].
5. Reusable idea for Plan4ARI: alternatives (grasps, approach sides, base poses, homotopy classes from the Open-IPC planner) as parallel modes of one MPPI. See [[comparisons/plan4ari-gap-analysis]].

## Abstract (verbatim, arXiv)
> Task and Motion Planning (TAMP) has made strides in complex manipulation tasks, yet the execution robustness of the planned solutions remains overlooked. In this work, we propose a method for reactive TAMP to cope with runtime uncertainties and disturbances. We combine an Active Inference planner (AIP) for adaptive high-level action selection and a novel Multi-Modal Model Predictive Path Integral controller (M3P2I) for low-level control. This results in a scheme that simultaneously adapts both high-level actions and low-level motions. The AIP generates alternative symbolic plans, each linked to a cost function for M3P2I. The latter employs a physics simulator for diverse trajectory rollouts, deriving optimal control by weighing the different samples according to their cost. This idea enables blending different robot skills for fluid and reactive plan execution, accommodating plan adjustments at both the high and low levels to cope, for instance, with dynamic obstacles or disturbances that invalidate the current plan. We have tested our approach in simulations and real-world scenarios.

## Links
- [[concepts/multimodality]]
- [[applications/mobile-manipulation-tamp]]
- [[concepts/physics-simulator-rollouts]]
- BibTeX key: `zhang2024m3p2i` in `latex/references.bib`
