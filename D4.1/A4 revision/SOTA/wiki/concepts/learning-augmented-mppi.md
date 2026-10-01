---
title: Learning-augmented MPPI
type: concept
updated: 2026-10-01
---

# Learning-augmented MPPI

| Role of learning | Source |
|---|---|
| Learned dynamics (NN) inside MPPI | [[sources/williams2017itmpc]], [[sources/kim2022smppi]] |
| Learned terminal value → longer effective horizon | [[sources/lowrey2019polo]], [[sources/bhardwaj2020mpq]], [[sources/hansen2022tdmpc]] |
| Learned proposal distribution | [[sources/sacks2023learningsampling]], [[sources/power2024generalizable]] (conditioned on start/goal/SDF, OOD projection) |
| Learned ancillary policy as proposal | [[sources/trevisan2024biasedmppi]] |
| Bayesian / VI models | [[sources/okada2020vimpc]] |
| Learned collision / SDF costs | [[sources/bhardwaj2021storm]], [[sources/parwana2025brmppi]] |

**Plan4ARI relevance.** Repetitive industrial cells generate data: learned terminal values and proposals can cut the sample budget; links to Activity 5 (neural control).
