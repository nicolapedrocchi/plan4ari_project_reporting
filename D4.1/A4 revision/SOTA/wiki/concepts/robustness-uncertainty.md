---
title: Robustness to disturbances and model uncertainty
type: concept
updated: 2026-10-01
---

# Robustness to disturbances and model uncertainty

| Variant | Idea | Source |
|---|---|---|
| Tube-MPPI | MPPI nominal + iLQG ancillary tracker | [[sources/williams2018tubemppi]] |
| RMPPI | augmented nominal state, free-energy growth bound (performance guarantee) | [[sources/gandhi2021rmppi]] |
| Ensemble MPPI | sample physical parameters, adapt online | [[sources/abraham2020emppi]] |
| U-MPPI | unscented propagation of mean+covariance, risk-sensitive cost | [[sources/mohamed2025umppi]] |
| Covariance steering | control the trajectory-distribution covariance | [[sources/yin2022covsteering]] |
| BSS-MPPI | belief-space chance constraints | [[sources/yin2024ccmppi]] |
| Online domain randomisation | randomise contact parameters inside MPC budget; global physics params too weak a signal | [[sources/dierking2026parallelsbmpc]] |

**Plan4ARI relevance.** Unknown payloads, friction and human motion → ensemble/unscented ideas; layered nominal + tracker architecture (Tube/RMPPI) maps to MPPI + Core-IPC. See [[comparisons/plan4ari-gap-analysis]].
