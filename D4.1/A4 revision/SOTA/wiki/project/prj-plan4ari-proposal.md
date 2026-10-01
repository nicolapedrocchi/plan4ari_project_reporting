---
key: prj-plan4ari-proposal
title: "Plan4ARI Project Description (FISA 2024-00099, Allegato A)"
doctype: proposal
version: ""
date: 2025-11-12
author: "NICOLA PEDROCCHI"
confidentiality: consortium
file: raw/project/prj-plan4ari-proposal.pdf
text: raw/text/prj-plan4ari-proposal.txt
original_name: "FISA_2024_00099_Allegato A.pdf"
tags: [project, proposal, requirements, kpi, architecture]
status: summarised
---

# Plan4ARI Project Description (FISA 2024-00099, Allegato A)

*Project document (proposal), PDF dated 2025-11-12, 46 pages. MUR – Fondo Italiano per le Scienze Applicate (FISA). Internal — not citable in the deliverable bibliography.*

## Purpose
Technical annex of the Plan4ARI proposal ("Planning for Artificial Robotic Intelligence and Beyond", 48 months, area Advanced Manufacturing). PI Nicola Pedrocchi (CNR, research organisation), host institution COMAU SpA. It is the **primary source of requirements and KPIs** for Activity 4; the D4.1 outline ([[project/prj-d41-outline]]) is derived from it (§E.3 and §A.4).

## Key content
- **Architecture (§A.2.2, Fig. 1)** — two computing units:
  - *Open IPC*: COMAU MI.RA/Dexter low-code platform (dispatcher + execution monitor), ROS 2, sensing, the offline/online motion planner; "firewall" between non-real-time and real-time worlds.
  - *Core IPC*: hard-real-time motion controller, micro-interpolation ("high-rate real-time motion planner"), all safety rules; an MPC micro-interpolator for external references (Cartesian and joint), direct link to high-rate sensors (visual servoing).
  - Motion references are streamed continuously between the two IPCs.
- **Modules (§A.2.3)**: A3 low-code & natural communication · **A4 intelligent sensing and safe motion planning for mobile manipulators and multi-agent interaction** · A5 neural motion control · A6 trustworthiness.
- **A.4 objectives**: library for offline planning + online continuous replanning; *multi-path replanning* (connect to pre-existing paths to the same goal, with completeness/optimality guarantees); safety-aware cost function for humans/movable objects; fast replanning with dynamics and runtime velocity modulation, because "lookahead micro-interpolator fails in challenging operative scenes"; motion planning split between Open IPC (asynchronous) and Core IPC (synchronous, e.g. visual servoing); deep-learning registration/segmentation; radar + 3D camera fusion for human tracking.
- **A.4.2.2 methodology** (building on the PI's FOSS OpenMORE): RRT-like planners with *admissible informed + local sampling* and adaptive exploration/exploitation; ISO/TS 15066 safety-aware cost in a fast replanner (from Faroni, Beschi, Pedrocchi, RA-L 2022); an **MPC for path planning running alongside the sampling-based planner**, with online speed adaptation and use of residual DoF (e.g. free rotation about the tool axis) to reduce torque/jerk.
- **Work plan (§E.3, Activity 4, M1–M36)**: T4.1 SOTA update (M1–M6) · T4.2 informed sampling-based optimal planning for teams of mobile manipulators (M4–M24; mixed global/local informed sampling, anytime, graph of paths) · T4.3 MPC for optimal adaptive micro-interpolation (M4–M24; joint/velocity/acceleration/workspace constraints, visual servoing, COMAU virtualisation tools) · T4.4 integration in MI.RA/Dexter as dockerised actions (M25–M30) · T4.5 MPC integration in the COMAU Core IPC (M31–M36; async channel outwards, hard-real-time channel to the robot, synchronous sensor input; MPC "mainly designed to safely change the speed override") · T4.6 continuous integration · T4.7 benchmarking (M1–M6).

## Requirements / constraints for the motion-planning framework
| # | Requirement (proposal §) | Wiki coverage |
|---|---|---|
| P1 | Teams of mobile manipulators and arms, humans with or without fences, multi-agent interaction (§A.4.1, §E.3 Act. 4) | [[applications/mobile-manipulation-tamp]], [[sources/streichenberg2023mapi]] — partial |
| P2 | Offline planning + online continuous replanning under one architecture supervising execution and scene updates (§A.4.1) | [[comparisons/plan4ari-gap-analysis]] |
| P3 | Multi-path replanning: reuse pre-computed paths to the same goal, formal completeness/optimality (§A.4.1, T4.2) | not MPPI; Biased-MPPI could consume the path graph as proposals ([[sources/trevisan2024biasedmppi]]) |
| P4 | ISO/TS 15066 (SSM, PFL) safety-aware cost; minimise safety-induced slowdowns rather than only avoid collisions (§A.4.2.1–2) | [[applications/human-robot-shared-spaces]], [[concepts/constraints-and-safety]] |
| P5 | Blend proactive and reactive human-aware planning (§A.4.2.1) | [[sources/trevisan2025drampi]], [[sources/gursoy2026cosmik]] |
| P6 | MPC as trajectory generator ("active filter") with velocity/acceleration/workspace constraints, smooth feasible output (§A.4.2.1, T4.3) | [[concepts/mppi-vs-mpc]], [[sources/faroni2020scaling]] |
| P7 | Runtime velocity modulation / speed override, exploit residual DoF to reduce torque and jerk (§A.4.2.2, T4.5) | [[sources/faroni2019pik]], [[sources/faroni2020scaling]] |
| P8 | Core IPC: hard real-time, synchronous sensor input (visual servoing), joint and Cartesian interfaces (§A.2.2, T4.3, T4.5) | [[tools/software-ecosystem]] — gap for MPPI |
| P9 | Integration as dockerised MI.RA/Dexter actions; reuse/re-engineer research code to industrial requirements (T4.4) | [[tools/software-ecosystem]] |
| P10 | KPI computation time: ≥50 scenarios, mean over >100 contexts, benchmark vs OMPL; **"planners running on GPU will not be compared"** (§A.4.4.1) | see tension below |
| P11 | KPI execution time of interaction tasks −30% vs SOTA planners; safe velocity adaptation (§A.4.4) | [[applications/human-robot-shared-spaces]] |
| P12 | KPI trajectory adaptation: tracking performance +~50% over ≥50 scenarios (§A.4.4.3) | Core-IPC MPC |
| P13 | Compliance with the EU AI Act (§A.2.2) | not covered by the MPPI literature |

## Relation to the literature
- The proposal's baseline is **informed sampling-based path planning (RRT*/PRM) + MPC micro-interpolation**. MPPI is not mentioned: it would be an *update* of the scientific plan, which is exactly the purpose of T4.1/D4.1.
- MPPI fits between the two baseline blocks: it is a sampling-based method (in line with the "sampling-based approach to overcome computational complexity" of §A.4.2.2), but in control space with a receding horizon, and it naturally carries the ISO/TS 15066 safety-aware cost as a rollout cost ([[concepts/information-theoretic-mppi]]). The proposal's "MPC for path planning running alongside the sampling-based planner" is the slot an MPPI layer could take, with the Core-IPC MPC kept for certified micro-interpolation ([[comparisons/plan4ari-gap-analysis]]).
- Ref. 10 of the proposal (Power & Berenson, T-RO 2024, learned trajectory sampling distribution for MPC) is an MPPI-family work and is not yet in the wiki; the sentence citing it in §A.4.2.1 describes MPC for aerial coverage, which does not match the paper. **Confirmed after reading** [[sources/power2024generalizable]]: it learns a sampling distribution for collision-free navigation (double integrator, quadrotor, 7-DoF arm), not aerial coverage with learned penalties. Re-word or replace this citation in D4.1.

> **Contradiction / tension:** KPI §A.4.4.1 states that GPU planners will not be compared with the OMPL benchmark. A GPU MPPI layer therefore (a) does not count towards the computation-time KPI and needs its own evaluation track, or (b) must run on CPU (as the Nav2 MPPI controller does, [[sources/macenski2023nav2survey]]) or on embedded hardware ([[sources/desai2026fpgampi]]) to stay comparable. Decision needed in D4.1 §9–10. Same tension in [[project/prj-d41-outline]] §10.

## Open points / decisions to take
- Position MPPI explicitly as an *update* of the plan (T4.1 mandate) and decide whether it replaces or complements the "MPC alongside the sampling-based planner" of §A.4.2.2.
- KPI treatment of GPU-based methods (P10).
- Whether the ISO/TS 15066 cost of Faroni et al. 2022 can be used verbatim as MPPI rollout cost.
- Hardware placement of an MPPI layer in the Open-IPC / Core-IPC split and its timing budget.

## Sources cited by the proposal (ingested 2026-10-01)
- ✔ ingested: [[sources/faroni2022safetyaware]] — basis of the ISO/TS 15066 cost.
- ✔ ingested: [[sources/power2024generalizable]] — citation mismatch confirmed (see below).
- ✔ ingested: [[sources/palleschi2021fastsafe]]
- ✔ ingested: [[sources/laha2023sstar]]

## Links
- [[project/prj-d41-outline]]
- [[comparisons/plan4ari-gap-analysis]]
- [[applications/human-robot-shared-spaces]]
- [[overview]]
