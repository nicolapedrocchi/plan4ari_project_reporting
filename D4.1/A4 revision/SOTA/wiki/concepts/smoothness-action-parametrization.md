---
title: Smoothness and action parametrisation
type: concept
updated: 2026-10-01
---

# Smoothness and action parametrisation

White Gaussian noise on each time step produces chattering commands — unacceptable for industrial axes (jerk limits, wear) and for AMR comfort.

| Technique | Source |
|---|---|
| Post-filter (Savitzky–Golay) of the update | common practice ([[sources/williams2018tro]]) |
| Halton-spline (low-discrepancy, smooth) noise | [[sources/bhardwaj2021storm]], [[sources/pezzato2025isaacmppi]], [[sources/zhang2024m3p2i]] |
| Coloured (time-correlated) noise | [[sources/pinneri2020icem]] |
| Sampling in derivative-action space | [[sources/kim2022smppi]] |
| Spline parametrisation of sequences | [[sources/howell2022predictivesampling]] |
| Via-point, time-optimal trajectory parametrisation | [[sources/jankowski2023vpsto]] |
| Downstream jerk-bounded interpolation/scaling | [[sources/faroni2020scaling]] |

**Takeaway.** Use a spline / via-point action space in MPPI and leave certified jerk/torque bounds to the Core-IPC layer ([[comparisons/plan4ari-gap-analysis]]).
