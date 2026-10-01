---
title: Gap analysis and implications for the Plan4ARI MPPI framework
type: comparison
updated: 2026-10-01
---

# Gap analysis and implications for the Plan4ARI framework

Mirrors Section 5 / Fig. 1 of `latex/main.tex`. Plan4ARI context: teams of mobile manipulators and industrial arms in human-shared spaces; Open IPC (global, informed sampling-based planning) + Core IPC (MPC reference generation, micro-interpolation); targets: autonomous plan generation, ~30% reduction of interaction-task time, safe velocity adaptation (from the D4.1 outline, [[project/prj-d41-outline]] — requirements R1–R14 mapped to the literature there).

Requirements and KPIs originate in the Project Description, [[project/prj-plan4ari-proposal]] (P1–P13): its baseline is informed sampling-based path planning + MPC micro-interpolation; MPPI is not mentioned there, so it must be presented as an *update* of the scientific plan (T4.1 mandate).

> **Tension with the proposal KPI (§A.4.4.1) and the D4.1 outline (§10):** OMPL planners are the computation-time baseline and "planners running on GPU will not be compared". A GPU MPPI layer needs a separate evaluation track, or a CPU / embedded implementation to stay comparable. See [[project/prj-plan4ari-proposal]], [[project/prj-d41-outline]].

## Gaps
1. **Certified constraint satisfaction** — penalties in vanilla MPPI; promising: [[sources/lee2026prmppi]], [[sources/gursoy2026cosmik]], [[sources/rabiee2025gsmppi]]. Not combined with industrial reference interfaces.
2. **Multimodality across task and motion** — [[sources/zhang2024m3p2i]] samples alternatives but blends; [[sources/liu2026clusteringmppi]] separates modes but has no task layer.
3. **Unified arm/AMR whole-body planning in human spaces** — only sim-heavy demos ([[sources/pezzato2025isaacmppi]]); human-risk models exist for AMRs ([[sources/trevisan2025drampi]]) not for mobile manipulators.
4. **Global–local coupling** — Biased-MPPI ([[sources/trevisan2024biasedmppi]]) enables global paths as proposals; not yet exploited with informed planners / multi-path reuse.
5. **Real-time determinism** — GPU MPPI 20–170 Hz vs 1 kHz industrial axes → certified downstream layer ([[sources/faroni2019pik]], [[sources/faroni2020scaling]]); embedded FPGA option ([[sources/desai2026fpgampi]]).

## Proposed direction (candidate framework)
- MPPI layer (GPU, 20–100 Hz):
  - (a) modes = task alternatives / homotopies / grasps (M3P2I idea) **kept separate** before the update (CE-MPPI / SVG-MPPI idea);
  - (b) part of proposals from Open-IPC paths and ancillary controllers (Biased-MPPI);
  - (c) kinematic constraints by projection (PR-MPPI), human separation by termination / risk (COSMIK, DRA-MPPI), ISO/TS 15066 time-dilation cost of [[sources/faroni2022safetyaware]] as rollout cost;
  - (d) smooth spline / via-point action space ([[concepts/smoothness-action-parametrization]]).
- Core-IPC layer (1 kHz): gradient MPC / predictive IK / trajectory scaling as certified safety filter ([[concepts/hybrid-gradient-sampling]]); a convex, jerk-limited, PFL-aware re-timing as in [[sources/palleschi2021fastsafe]] is a proven template (25–40 Hz there).

## Open research questions (to refine in D4.1)
- How to choose the number of modes N and samples K under a fixed GPU budget for a mobile manipulator (~9–10 DoF)?
- Can mode selection be stabilised (hysteresis) to avoid switching chatter between strategies?
- Which certification argument covers the MPPI + MPC-filter chain (filter-based safety vs planner-based)?
- Benchmarks: reuse D4.1 Sect. 3 metrics (success, replan latency, path cost, smoothness, constraint satisfaction, idle time due to safety stops).

Application-specific design (AGV-mounted welding, multi-goal MPPI look-ahead): [[comparisons/welding-mppi-design-review]].

See also [[comparisons/mppi-variants-matrix]], [[overview]].
