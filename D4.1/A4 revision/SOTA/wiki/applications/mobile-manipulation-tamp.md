---
title: Mobile manipulation and reactive TAMP with MPPI
type: application
updated: 2026-10-01
---

# Mobile manipulation and reactive TAMP with MPPI

- **Whole-body MPPI with physics simulator**: [[sources/pezzato2025isaacmppi]] (omni/diff-drive bases, mobile manipulators, pushing/pulling).
- **Reactive TAMP**: Active Inference + BT [[sources/pezzato2023aip]] → multi-modal MPPI [[sources/zhang2024m3p2i]] (key paper; detailed notes in its page).
- **Contact-rich manipulation with mode switching**: [[sources/dierking2026parallelsbmpc]].
- **Multimodal selection without blending**: [[sources/liu2026clusteringmppi]], [[sources/honda2024svgmppi]].

## Pattern worth reusing
Task layer proposes *alternatives* → each becomes a cost function → motion layer samples all of them in parallel and lets the geometry decide. In Plan4ARI the alternatives can be: grasp types, approach sides, base placements, homotopy classes from the Open-IPC planner, or which robot of a team executes a sub-task.

## Gaps
Human safety, hard constraints, and certification are not addressed by these works → [[concepts/constraints-and-safety]], [[comparisons/plan4ari-gap-analysis]].
