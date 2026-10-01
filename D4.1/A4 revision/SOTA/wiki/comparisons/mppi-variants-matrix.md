---
title: MPPI variants vs issue addressed
type: comparison
updated: 2026-10-01
---

# MPPI variants vs issue addressed

Legend: ● main contribution, ○ partial. Columns: R = robustness, C = constraints/safety, M = multimodality, S = sampling efficiency, Sm = smoothness, H = humans, A = arm, B = mobile base.

| Variant | R | C | M | S | Sm | H | A | B | Source |
|---|---|---|---|---|---|---|---|---|---|
| Tube-MPPI | ● | | | | | | | ● | [[sources/williams2018tubemppi]] |
| RMPPI | ● | ○ | | | | | | ● | [[sources/gandhi2021rmppi]] |
| Ensemble MPPI | ● | | | | | | ● | | [[sources/abraham2020emppi]] |
| U-MPPI | ● | ○ | | ● | | | | ● | [[sources/mohamed2025umppi]] |
| Covariance steering | ○ | | | ● | | | | ● | [[sources/yin2022covsteering]] |
| Shield-MPPI | | ● | | | | | | ● | [[sources/yin2023shieldmppi]] |
| SC-MPPI | | ● | | ● | | | | ● | [[sources/gandhi2023safeis]] |
| GS-MPPI | | ● | | ● | | | | ● | [[sources/rabiee2025gsmppi]] |
| BR-MPPI | | ● | | | | | | ● | [[sources/parwana2025brmppi]] |
| BSS-MPPI | ● | ● | | | | | | ● | [[sources/yin2024ccmppi]] |
| PR-MPPI | | ● | | | | | ● | | [[sources/lee2026prmppi]] |
| COSMIK-MPPI | | ● | | | | ● | ● | | [[sources/gursoy2026cosmik]] |
| DRA-MPPI | ○ | ● | | | | ● | | ● | [[sources/trevisan2025drampi]] |
| Contingency-MPPI | | ● | | ● | | | | ● | [[sources/jung2024contingency]] |
| Smooth-MPPI | | | | | ● | | | ● | [[sources/kim2022smppi]] |
| log-MPPI | | | | ● | | | | ● | [[sources/mohamed2022logmppi]] |
| Biased-MPPI | | | ○ | ● | | | | ● | [[sources/trevisan2024biasedmppi]] |
| MPOPI | | | | ● | | | | | [[sources/asmar2023mpopi]] |
| SVMPC | | | ● | ○ | | | ○ | ● | [[sources/lambert2020svmpc]] |
| SVG-MPPI | | | ● | | | | | ● | [[sources/honda2024svgmppi]] |
| CE-MPPI | | | ● | | | | ● | ○ | [[sources/liu2026clusteringmppi]] |
| M3P2I | | | ● | | ○ | | ● | ● | [[sources/zhang2024m3p2i]] |
| STORM | | ○ | | | ● | | ● | | [[sources/bhardwaj2021storm]] |
| Torque-sampling MPPI | | ○ | | | | ● | ● | | [[sources/im2026torquemppi]] |
| FlowMPPI (learned flow proposal) | | | ○ | ● | | | ○ | ○ | [[sources/power2024generalizable]] |
| PMPPI (parallel planners + Judge, blended) | | | ● | ○ | | ● | ● | | [[sources/zhou2025parallelmppi]] |
| Input-constrained NMPPI (saturated integrator) | | ● | | | ○ | | | | [[sources/homburger2023nmppi]] |
| MPPI-Tan (tangential subspace sampling) | | | ○ | ● | | | ● | | [[sources/zhao2025tangentialmpc]] |
| CSMPC (null-space projected samples, preprint) | | ● | | | ○ | ○ | ● | | [[sources/wang2024constrainedpi]] |
| RRT-guided MPPI | | | | ● | | | | ● | [[sources/tao2023rrtmppi]] |
| Feedback-MPPI (gains from rollouts) | ● | | | | ○ | | | | [[sources/belvedere2026feedbackmppi]] |
| Generalised MPPI as EM (mixtures) | | | ● | ○ | | | | | [[sources/wang2026mppiem]] |
| DIAL-MPC | | | | ● | | | | | [[sources/xue2025dialmpc]] |

Reading: no row covers C + M + H + A + B together → that intersection is the Plan4ARI opportunity ([[comparisons/plan4ari-gap-analysis]]).
