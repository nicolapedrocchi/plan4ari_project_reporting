---
title: Sampling distributions, proposals and guidance
type: concept
updated: 2026-10-01
---

# Sampling distributions, proposals and guidance

MPPI quality depends on *where* samples are drawn. Vanilla MPPI samples a Gaussian around the shifted previous solution → local minima and wasted samples.

## Families of fixes
- **Importance sampling with arbitrary proposals**: Biased-MPPI mixes samples from ancillary controllers (classical controllers, learned policies, braking) — [[sources/trevisan2024biasedmppi]]. Origin: covariance-variable IS [[sources/williams2015covariance]].
- **Heavy-tailed / non-Gaussian noise**: log-MPPI (normal–log-normal) [[sources/mohamed2022logmppi]].
- **Adaptive / iterated IS**: MPOPI [[sources/asmar2023mpopi]]; annealing [[sources/xue2025dialmpc]], [[sources/pan2024mbd]].
- **Distribution shaping**: covariance steering [[sources/yin2022covsteering]]; unscented transform [[sources/mohamed2025umppi]].
- **Global guidance**: subgoals from a GP perception model [[sources/mohamed2023gpmppi]]; global planner paths as proposals (Biased-MPPI).
- **Learned proposals**: normalising flows [[sources/sacks2023learningsampling]]; environment-conditioned flow reusable across MPPI/iCEM, with OOD projection for unseen scenes, tested on a 7-DoF arm [[sources/power2024generalizable]].
- **Generalised weights**: Tsallis [[sources/wang2021tsallis]].
- **Multimodal proposals**: see [[concepts/multimodality]].

## Plan4ARI takeaway
Biased-MPPI is the mechanism to inject Open-IPC paths (informed RRT*/PRM, reused multi-paths) into the local planner → [[comparisons/plan4ari-gap-analysis]].
