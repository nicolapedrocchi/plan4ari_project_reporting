---
title: Multimodality and mode averaging
type: concept
updated: 2026-10-01
---

# Multimodality and mode averaging

**Problem.** The optimal control distribution `q*` is often multimodal (go left/right of an obstacle, push vs pull, top vs side grasp). MPPI's Gaussian projection averages rollouts of different modes → the mean can be infeasible ("averaging-induced failure", hesitation in front of obstacles). Theoretical root: symmetry breaking in path-integral control ([[sources/kappen2005pathintegrals]]).

## Approaches
| Approach | How | Source |
|---|---|---|
| Particle/Stein posterior | SVGD over control sequences | [[sources/lambert2020svmpc]] |
| Mode-seeking guidance | SVGD finds target mode, MPPI converges on it | [[sources/honda2024svgmppi]] |
| Mixture VI | Gaussian mixtures | [[sources/okada2020vimpc]] |
| Rollout clustering | DBSCAN + direction feature, select one cluster | [[sources/liu2026clusteringmppi]] |
| Task-level alternatives | N cost functions from symbolic planner, per-mode weights, blending | [[sources/zhang2024m3p2i]] |
| Learned multimodal proposal | conditional normalising flow mixed with Gaussian samples (FlowMPPI) | [[sources/power2024generalizable]] |
| Structured global sampling | MTP sampler for mode switching in contact-rich tasks | [[sources/dierking2026parallelsbmpc]] |
| Explicit topologies (gradient) | TEB parallel homotopies | [[sources/rosmann2017teb]] |
| Multimodal ME-DDP / Stein DDP | hybrid | [[sources/aoyama2026hybrid]] |

## Insight for Plan4ARI
M3P2I *selects among strategies by sampling* (good) but *blends* them in the final update (risky). Combining M3P2I-style task modes with CE-MPPI-style mode separation is an open gap → [[comparisons/plan4ari-gap-analysis]].
