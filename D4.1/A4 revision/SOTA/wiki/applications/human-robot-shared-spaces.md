---
title: MPPI in human-shared spaces
type: application
updated: 2026-10-01
---

# MPPI in human-shared spaces

| Setting | Approach | Source |
|---|---|---|
| Arm, path planning (CNR-STIIMA) | ISO/TS 15066 SSM/PFL speed limits → time-dilation costmap; minimises expected execution time; −19% robot time on real UR10e cell | [[sources/faroni2022safetyaware]] |
| Arm, time-law replanning on fixed path (non-MPPI) | PFL / Safe Motion Unit limits, convex jerk-limited minimum-time re-timing at 25–40 Hz | [[sources/palleschi2021fastsafe]] |
| Arm, graph search (non-MPPI) | edge cost = max(joint-limit time, biomechanically safe time) | [[sources/laha2023sstar]] |
| Arm, close-proximity humans | constraints-as-terminations + markerless pose (RT-COSMIK), 22 ms | [[sources/gursoy2026cosmik]] |
| Arm, physical interaction | torque-sampling MPPI, compliant/force-aware | [[sources/im2026torquemppi]] |
| AMR in crowds | MC collision probability vs non-Gaussian predictions | [[sources/trevisan2025drampi]] |
| AMR interaction-aware | learned local-goal predictions | [[sources/jansma2023interaction]] |
| Multi-agent | joint path-integral planning | [[sources/streichenberg2023mapi]] |
| Chance constraints | belief-space MPPI | [[sources/yin2024ccmppi]] |

## Link to standards (Plan4ARI D4.1 Sect. 5)
- [[sources/faroni2022safetyaware]] already converts SSM/PFL limits into a per-configuration cost λ(q,H): the most direct candidate MPPI running cost.
- Non-MPPI baselines sharing the "minimise time *including* safety limits" principle: SSM-based [[sources/faroni2022safetyaware]], PFL/biomechanics-based [[sources/laha2023sstar]] (planning) and [[sources/palleschi2021fastsafe]] (re-timing). Both SSM and PFL limits can be evaluated per rollout state in MPPI.
- ISO/TS 15066 speed-and-separation monitoring (SSM) maps naturally to a rollout-level separation cost or termination; power-and-force limiting maps to torque-level MPPI.
- Objective in Plan4ARI: reduce safety-induced idle time (~30% interaction-task time reduction target) → MPPI can *anticipate* the safety system by penalising predicted SSM interventions rather than reacting to them.
- Open gap: no work certifies MPPI outputs w.r.t. ISO 10218 / ISO/TS 15066 → [[comparisons/plan4ari-gap-analysis]], [[concepts/constraints-and-safety]].
