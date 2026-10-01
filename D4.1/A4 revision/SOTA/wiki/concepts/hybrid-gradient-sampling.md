---
title: Hybrid gradient + sampling schemes
type: concept
updated: 2026-10-01
---

# Hybrid gradient + sampling schemes

| Scheme | Sampling part | Gradient part | Source |
|---|---|---|---|
| Tube-MPPI | MPPI nominal | iLQG tracking | [[sources/williams2018tubemppi]] |
| RMPPI | MPPI | feedback on augmented state | [[sources/gandhi2021rmppi]] |
| cuRobo | particle-based seeding | batched L-BFGS + parallel line search | [[sources/sundaralingam2023curobo]] |
| Shield-MPPI | MPPI | local CBF repair | [[sources/yin2023shieldmppi]] |
| ME-DDP | Hessian-shaped sampling | DDP steps | [[sources/aoyama2026hybrid]] |
| Biased-MPPI | MPPI | ancillary (e.g. gradient MPC) controllers as proposals | [[sources/trevisan2024biasedmppi]] |
| RRT-guided MPPI | MPPI around RRT-tracking nominal control | (planner) | [[sources/tao2023rrtmppi]] |
| Feedback-MPPI | MPPI at 50 Hz | gains by differentiating the MPPI update, inner loop 200-500 Hz | [[sources/belvedere2026feedbackmppi]] |
| DIAL-MPC | annealed sampling | — (diffusion view) | [[sources/xue2025dialmpc]] |

Theory: one MPPI update = one preconditioned gradient step on a free-energy objective ([[sources/fazlyab2026mppigd]]) = one EM iteration ([[sources/wang2026mppiem]]); both justify several MPPI iterations per cycle and step sizes other than 1.

Downstream example of the gradient/convex layer for safety: convex jerk-limited safe re-timing along a fixed path, [[sources/palleschi2021fastsafe]].

**Plan4ARI design principle**: MPPI for exploration and non-smooth objectives, gradient MPC (Core IPC; [[sources/faroni2019pik]], [[sources/faroni2020scaling]], [[sources/verschueren2022acados]]) for certification. See [[comparisons/plan4ari-gap-analysis]].
