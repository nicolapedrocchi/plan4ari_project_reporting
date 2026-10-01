---
title: MPPI for mobile robots and AMRs
type: application
updated: 2026-10-01
---

# MPPI for mobile robots and AMRs

## Timeline
- 2016–2018: AutoRally aggressive driving ([[sources/williams2016aggressive]], [[sources/williams2018tro]], [[sources/williams2018tubemppi]]).
- 2022–2025: AGV/AMR navigation in unknown clutter: log-MPPI, GP-MPPI, U-MPPI ([[sources/mohamed2022logmppi]], [[sources/mohamed2023gpmppi]], [[sources/mohamed2025umppi]]); Biased-MPPI ([[sources/trevisan2024biasedmppi]]).
- 2023: Nav2 MPPI controller, planned default replacing DWB ([[sources/macenski2023nav2survey]]).
- 2023–2025: human-/interaction-aware: [[sources/jansma2023interaction]], [[sources/streichenberg2023mapi]], DRA-MPPI [[sources/trevisan2025drampi]].
- 2024–2026: safety: GS-MPPI [[sources/rabiee2025gsmppi]], Contingency-MPPI [[sources/jung2024contingency]]; embedded FPGA [[sources/desai2026fpgampi]].

## Station / base placement (AGV-mounted manipulators)
Reachability maps, set-cover station selection, coverage BPO: [[concepts/base-placement]].

## Incumbents compared
DWA [[sources/fox1997dwa]], TEB [[sources/rosmann2017teb]] → see [[concepts/mppi-vs-mpc]].

## Relevance for Plan4ARI AMRs
- Nav2-MPPI is a deployable baseline today (ROS 2).
- Missing: coupling with mobile-manipulator arm planning, certified human separation, fleet coordination. → [[applications/mobile-manipulation-tamp]], [[comparisons/plan4ari-gap-analysis]].
