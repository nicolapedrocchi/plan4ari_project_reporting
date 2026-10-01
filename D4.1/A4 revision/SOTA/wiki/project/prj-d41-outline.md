---
key: prj-d41-outline
title: "D4.1 Outline - Updated Scientific Plan for Local and Global Autonomous Motion Planning"
doctype: outline
version: "0.1"
date: 2026-07-20
author: ""
confidentiality: consortium
file: raw/project/prj-d41-outline.docx
text: raw/text/prj-d41-outline.txt
original_name: "Plan4ARI_D4.1_Outline_Updated_Scientific_Plan_Motion_Planning.docx"
tags: [project, d4.1, requirements]
status: summarised
---

# D4.1 Outline — Updated Scientific Plan for Local and Global Autonomous Motion Planning

*Project document (outline), v0.1, 2026-07-20. Internal — not citable in the deliverable bibliography.*

## Purpose
Writing blueprint for Plan4ARI deliverable D4.1 (Activity 4, Task 4.1 "Update of the Scientific Plan with the latest State-of-the-Art Methodologies and Tools for Motion Planning", M1–M6, suggested delivery M6). Inferred from the Plan4ARI Project Description (§E.3 pp. 38–48; technical baseline §A.3–A.6). Title, due date, lead beneficiary and dissemination level still to be confirmed against the Grant Agreement.

## Key content
- **12 sections**: executive summary · objectives/scenarios/baseline architecture · review methodology · sampling-based optimal planning SOTA · dynamic replanning & human-aware safety · MPC for trajectory generation & micro-interpolation · software & industrial toolchain · gap analysis & revised architecture · selected methods & fallbacks · benchmarking plan · integration roadmap/risks/compliance · conclusions.
- **Baseline architecture** (§2): *Open IPC* (sample-based informed planning, offline + online replanning) and *Core IPC* (hard-real-time, high-rate MPC reference generation / micro-interpolation).
- **Scenario** (§2): teams of mobile manipulators and industrial arms in dynamic, human-shared environments; joint and Cartesian interfaces, residual DoF, visual servoing.
- **Targets** (§2): autonomous plan generation, ~30% reduction of interaction-task execution time, safe velocity adaptation.
- **Annexes** (suggested): A framework matrix · B benchmark catalogue · C safety-aware cost assumptions · D Open/Core IPC interface & timing budgets · E search protocol · F roadmap.
- **Boundary** (§Source mapping): D4.1 updates the research and benchmark plan; algorithms, MPC implementation and MI.RA/Dexter/Core-IPC integration belong to Tasks 4.2–4.7.

## Requirements / constraints for the motion-planning framework
| # | Requirement (outline §) | Addressed in the wiki by | Status |
|---|---|---|---|
| R1 | Reactive replanning in dynamic, human-shared scenes; reduce safety-induced idle time (§5) | [[applications/human-robot-shared-spaces]], [[sources/trevisan2025drampi]], [[sources/gursoy2026cosmik]] | covered by literature, gap for mobile manipulators |
| R2 | Safety-aware cost functions informed by ISO/TS 15066; minimise safety-system interventions (§5, Annex C) | [[concepts/constraints-and-safety]] | open gap: no MPPI work certified vs ISO/TS 15066 |
| R3 | Prediction uncertainty of humans and movable objects (§5) | [[sources/trevisan2025drampi]], [[sources/yin2024ccmppi]], [[concepts/robustness-uncertainty]] | covered (AMR) |
| R4 | Path switching, repair and emergency fallback (§5, §9) | [[sources/jung2024contingency]], [[concepts/multimodality]] | partially covered |
| R5 | MPC for constrained trajectory generation: joint, velocity, acceleration, jerk, torque, workspace limits (§6) | [[concepts/mppi-vs-mpc]], [[sources/faroni2019pik]], [[sources/faroni2020scaling]], [[sources/lee2026prmppi]] | Core-IPC gradient MPC; MPPI only with projection |
| R6 | Online speed adaptation, redundant DoF exploitation (§6) | [[sources/faroni2019pik]], [[sources/faroni2020scaling]] | covered by Core-IPC layer |
| R7 | Real-time feasibility, determinism, fallback (§6, §9) | [[tools/software-ecosystem]], [[sources/desai2026fpgampi]] | open gap for GPU MPPI |
| R8 | Mixed global–local sampling, path repository / reuse (§4, §8) | [[sources/trevisan2024biasedmppi]], [[concepts/sampling-distributions]] | open gap (not yet exploited) |
| R9 | Multi-robot and mobile-manipulator configuration spaces (§4) | [[applications/mobile-manipulation-tamp]], [[sources/streichenberg2023mapi]] | partially covered |
| R10 | Solver libraries for C++ and hard real-time; ROS 2/MoveIt; COMAU digital twin; MI.RA/Dexter containerisation (§7) | [[tools/software-ecosystem]] | MPPI-Generic / acados candidates; COMAU/MI.RA integration not in literature |
| R11 | Interfaces to Activity 3 (tracking) and Activity 2 (task replanning) (§5, §11) | [[sources/zhang2024m3p2i]], [[sources/pezzato2023aip]] | M3P2I-style task→cost interface |
| R12 | Metrics: success, initial-solution time, convergence, path cost, replan latency, memory, CPU load, scalability, smoothness, constraint satisfaction (§3, §10) | [[comparisons/plan4ari-gap-analysis]] | to be applied in benchmarking |
| R13 | ≥50 application scenarios, >100 contexts for computation-time evaluation; OMPL planners as baseline (§10) | — | benchmark design pending |
| R14 | Proof/verification obligations: completeness, optimality, stability or constraint satisfaction (§9) | [[sources/gandhi2021rmppi]], [[concepts/constraints-and-safety]] | weak for MPPI → certify via Core-IPC |

## Relation to the literature
- The MPPI SOTA (`latex/main.tex`) mainly feeds outline **§5, §6, §8** and Annex C/D; it does not cover §4 (RRT*/PRM, informed sets, path reuse), which needs its own review.
- The candidate architecture in [[comparisons/plan4ari-gap-analysis]] is consistent with the Open/Core IPC split: MPPI sits between them as reactive local planner.

> **Contradiction / tension:** §10 asks for OMPL planners as baseline and an "explicit rationale for excluding or separately reporting GPU planners". An MPPI-based local planner is GPU-centric ([[tools/software-ecosystem]]). The deliverable must therefore (a) report GPU methods in a separate benchmark track, and (b) justify the hardware assumption (embedded GPU / FPGA, [[sources/desai2026fpgampi]]) for MI.RA/Dexter integration.

## Open points / decisions to take
- Where MPPI runs physically (Open IPC host vs dedicated GPU/FPGA) and its timing budget towards Core IPC (Annex D).
- Whether ISO/TS 15066 SSM is enforced as MPPI cost, rollout termination, or only in the Core-IPC safety filter (Annex C).
- Benchmark track for GPU planners vs OMPL baseline (§10).
- Scope of D4.1 vs Tasks 4.2–4.7: the MPPI framework is a *selected methodology* (§9), its implementation belongs to later tasks.

## Document outline (headings)
- Executive summary · Objectives, scenarios and baseline architecture · Review methodology and comparison criteria · Sampling-based optimal planning SOTA · Dynamic replanning and human-aware safety · MPC for trajectory generation and micro-interpolation · Software frameworks and industrial toolchain · Gap analysis and revised architecture · Selected methodologies and fallback options · Benchmarking and evaluation plan · Integration roadmap, risks and compliance · Conclusions · Completion checklist · Annexes · Source mapping

## Links
- Derived from [[project/prj-plan4ari-proposal]] (§E.3, §A.4)
- [[comparisons/plan4ari-gap-analysis]]
- [[overview]]
