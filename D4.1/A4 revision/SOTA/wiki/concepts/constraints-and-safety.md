---
title: Constraints and safety in MPPI
type: concept
updated: 2026-10-01
---

# Constraints and safety in MPPI

Vanilla MPPI handles constraints as **penalties** in the cost → no certified satisfaction; large penalties degrade weights (few effective samples). This is the main obstacle to industrial certification (joint/jerk/torque limits, ISO/TS 15066 separation distance).

## Taxonomy
| Mechanism | Idea | Sources |
|---|---|---|
| CBF in cost + repair | barrier cost, local gradient repair of the solution | [[sources/yin2023shieldmppi]] |
| Safety controller inside rollouts | barrier states / safe control law in forward sampling → all samples safe | [[sources/gandhi2023safeis]], [[sources/rabiee2025gsmppi]] |
| Barrier-rate as input + projection | extra input, samples projected on constraint manifold | [[sources/parwana2025brmppi]] |
| Projection–retraction | joint velocities projected on equality/inequality constraints, retracted to manifold | [[sources/lee2026prmppi]] |
| Saturated integrator on inputs | sample input rate, saturate -> box constraint by construction | [[sources/homburger2023nmppi]] |
| Null-space projection of samples | path/attitude equalities exact for every sample (preprint) | [[sources/wang2024constrainedpi]] |
| Constraints-as-terminations | violating rollouts terminated | [[sources/gursoy2026cosmik]] |
| Chance constraints | belief-space MC + CBF heuristic | [[sources/yin2024ccmppi]] |
| Safety-aware cost (not a constraint) | ISO/TS 15066 slowdown as expected time dilation in the cost; runtime speed override keeps safety | [[sources/faroni2022safetyaware]] |
| Collision probability | MC joint CP vs non-Gaussian predictions, rejection or cost | [[sources/trevisan2025drampi]] |
| Contingency | nested MPPI keeps a fallback plan | [[sources/jung2024contingency]] |
| Downstream certified layer | gradient MPC / scaling after MPPI; convex jerk-limited safe re-timing (PFL) | [[sources/faroni2020scaling]], [[sources/williams2018tubemppi]], [[sources/palleschi2021fastsafe]] |
| Safety-aware planning cost (non-MPPI) | time with biomechanically safe speed as graph edge cost | [[sources/laha2023sstar]] |

## Assessment
- For manipulators: PR-MPPI (exact kinematic constraints) + COSMIK (human separation) are the most directly reusable.
- For AMRs: GS-MPPI (provable) and DRA-MPPI (probabilistic, humans).
- None is yet combined with an industrial, safety-rated reference interface → gap #1 in [[comparisons/plan4ari-gap-analysis]].
- Related: [[applications/human-robot-shared-spaces]], [[concepts/robustness-uncertainty]].
