---
title: Overview — MPPI for industrial manipulators and AMRs
type: synthesis
updated: 2026-10-01
---

# Overview — MPPI for industrial manipulators and AMRs

*Living synthesis of the knowledge base. Keep it short (≤ 1 page); details live in concept and source pages. The LaTeX deliverable (`latex/main.tex`) is the "frozen" view of this page.*

## Thesis
MPPI is a credible basis for the reactive local planner of Plan4ARI: sound theory ([[concepts/path-integral-control]], [[concepts/information-theoretic-mppi]]), GPU implementations ([[tools/software-ecosystem]]), industrial adoption for AMRs (Nav2, [[sources/macenski2023nav2survey]]) and recent demonstrations on 7-DoF/dual-arm manipulators, contact-rich and human-shared tasks ([[applications/industrial-manipulators]], [[applications/human-robot-shared-spaces]]).

## What MPPI is good at
Non-smooth costs, contacts via simulator ([[concepts/physics-simulator-rollouts]]), exploration within the horizon, parallel hardware, easy reformulation of objectives (task alternatives as costs, [[sources/zhang2024m3p2i]]).

## What it lacks (and who fixes it)
- hard constraints → [[concepts/constraints-and-safety]]
- mode averaging → [[concepts/multimodality]]
- chattering → [[concepts/smoothness-action-parametrization]]
- sample efficiency → [[concepts/sampling-distributions]], [[concepts/learning-augmented-mppi]]
- robustness/guarantees → [[concepts/robustness-uncertainty]], [[concepts/mppi-vs-mpc]]

## Position vs MPC
Complementary: sample-based exploration + gradient-based certification ([[concepts/hybrid-gradient-sampling]]).

## Plan4ARI opportunity
No existing work combines constraints + multimodality + humans + arm + mobile base ([[comparisons/mppi-variants-matrix]]). Candidate framework and open questions: [[comparisons/plan4ari-gap-analysis]].

## Reference application (2026-10-01)
AGV-mounted welding of large structures: multi-goal MPPI look-ahead over the null space, DP / station planning upstream, VAMP transfers, MPC speed control downstream → [[comparisons/welding-mppi-design-review]], [[concepts/path-wise-redundancy-resolution]], [[concepts/base-placement]], [[applications/robotic-welding]].

## Key papers to read first
1. [[sources/williams2018tro]] — the algorithm
2. [[sources/zhang2024m3p2i]] — multimodal reactive TAMP (key paper)
3. [[sources/bhardwaj2021storm]] — MPPI on 7-DoF arms
4. [[sources/trevisan2024biasedmppi]] — arbitrary proposals / global guidance
5. [[sources/gursoy2026cosmik]] and [[sources/lee2026prmppi]] — safety and exact constraints on arms
6. [[sources/trevisan2025drampi]] — human-aware AMR navigation
7. [[sources/kazim2024survey]] — survey
