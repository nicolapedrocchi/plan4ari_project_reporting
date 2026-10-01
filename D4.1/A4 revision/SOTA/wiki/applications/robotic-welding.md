---
title: Robotic arc welding — planning literature
type: application
updated: 2026-10-01
---

# Robotic arc welding — planning literature

Reference application of Plan4ARI (AGV-mounted welding of large structures): [[comparisons/welding-mppi-design-review]].

## By sub-problem
| Sub-problem | Sources | What they give us |
|---|---|---|
| Smoothing of welding paths with an extra axis (friction stir welding) | [[sources/li2024weldredundant]] | G3 corner smoothing, tool axis + 1-DoF table synchronised in arc length, constant jerk-continuous feed; no redundancy decision |
| Seam path with tolerances (5-DoF, free roll, cones) | [[sources/demaeyer2017descartes]], [[sources/sun2020externalaxis]], [[sources/wang2025anytimetracking]], [[sources/chen2025cooptimization]], [[sources/gao2022taskredundancy]], [[sources/razjigaev2025functional]] | Deterministic baselines (layered graph / DP / NLP); Descartes limits (memory, no speed, jumps inside tolerance) |
| Torch posture from sensing | [[sources/wang2026torchposture]] | Line-laser scan → groove geometry → cone centre; orientation error budget ~2° (Table 7) |
| Transfer motions between seams | [[sources/zhou2022weldavoidance]] | Lazy-PRM in TCP space with external axis; 10–26 s on real cell (slow vs VAMP) |
| Welding of very large structures | [[sources/peng2026ringwelding]] (preprint), [[sources/zhao2021mobilemachining]] | Stop–transfer–restart accepted practice; centimetre-level error of mobile platforms without local registration |
| Robot morphology and base position | [[sources/gautier2024weldingbase]], [[concepts/base-placement]] | Constant-speed corners break joint-speed limits; morphology changes number of base positions |
| Multi-robot welding | [[sources/tang2023dualrobotweld]], [[sources/ye2026nullspacemultirobot]] | Seam allocation/sequencing with synchronous pairs (distortion), direction constraints |
| Benchmarking | [[sources/demaeyer2021weldbenchmark]] | Planner-portfolio benchmark (weld segments + transitions), metrics: success, planning time, joint path length |

## Plan4ARI takeaway
- The welding literature is almost entirely **offline and deterministic**; online elements are perception-driven (seam scan) or transfer-only. An online null-space look-ahead with planned reconfigurations is not covered.
- Benchmark metrics to add for D4.1 §10 (beyond [[sources/demaeyer2021weldbenchmark]]): number of restarts/reconfigurations, deviation from the ±10% speed band, work/travel angle deviation, joint-limit and singularity margins, replan latency, total cycle time.
