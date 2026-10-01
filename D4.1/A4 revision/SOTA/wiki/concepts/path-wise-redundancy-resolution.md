---
title: Path-wise redundancy resolution (prescribed Cartesian paths)
type: concept
updated: 2026-10-01
---

# Path-wise redundancy resolution (prescribed Cartesian paths)

**Problem.** The end-effector must follow a prescribed Cartesian path (welding seam, toolpath); the robot has residual freedom — functional redundancy (free roll of a symmetric tool on a 6-axis arm, i.e. a 5-axis task), kinematic redundancy (7th joint or linear axis), orientation tolerances (cone), and discrete IK branches. Choose the joint path that respects joint limits, velocity/acceleration (at the prescribed speed), collisions, and minimises interruptions ("breakpoints" = stop, re-orient, restart).

## Families
| Family | Idea | Horizon | Sources |
|---|---|---|---|
| Global dynamic programming over a discretised null space | layered graph (path index × redundancy grid), DP with joint limits; large constant cost per breakpoint → minimises the number of breakpoints first, then smoothness | whole path, offline | [[sources/yin2024dpbreakpoints]] |
| DP offline + bounded online adjustment | backward DP computes, per node, the largest online deviation still executable to the end; online policy table | whole path offline, online adjustment | [[sources/yin2024dprealtime]] |
| Global redundancy resolution roadmaps | one configuration per task-space point, smooth and repeatable mapping | whole task space, offline | [[sources/zhong2024expansiongrr]] |
| Fast local functionally-redundant IK | 5-DoF task on 6-axis arm, damped Newton + Halley steps, ~0.2 ms per step | local, greedy | [[sources/razjigaev2025functional]] |
| Predictive IK with task scaling | QP over a short horizon, task scaling when infeasible | receding horizon | [[sources/faroni2019pik]] |
| Projection inside sampling | MPPI samples projected on equality/inequality constraint manifold | receding horizon | [[sources/lee2026prmppi]] |
| Layered graph over sampled tolerances + all IK branches (Descartes) | per-point sampling of tolerance, Dijkstra on joint motion; memory ~ (N-1)(2M)^2 edges, no speed, no inter-point collision check | whole path, offline | [[sources/demaeyer2017descartes]] |
| Descartes + external axes | rail/rotary value sampled per point, ladder graph DP | offline (minutes for ~60 points) | [[sources/sun2020externalaxis]] |
| Anytime layered graph | sparse guide path first, then refine around it; minimises reconfigurations first | anytime, offline | [[sources/wang2025anytimetracking]] |
| Global NLP co-optimisation | tool orientation in cones + roll/positioner + waypoint timing, fixed configuration among 8, windowed SQP | offline (<10 min for ~8k waypoints) | [[sources/chen2025cooptimization]] |
| Point-by-point warm-started optimisation with tolerance windows | exact / window / band / free per process DoF, multiple IK seeds in parallel | offline, 1-point look-ahead | [[sources/weingartshofer2023pathframework]] |
| Greedy SQP over roll | warm start from previous point, exhaustive only at first point | greedy | [[sources/dharmawan2018functional]] |
| Grid A* over torch angles | seam position x roll/swing, sigmoid penalties | offline, single branch | [[sources/gao2022taskredundancy]] |
| Greedy cone+roll integration | rate-limited, pre-smoothed bounds | greedy | [[sources/lu2022toolorientation]] |
| Roll as smooth spline in s | QP on roll second derivative + separate minimum-time feed | offline | [[sources/yang2024toolpathsmoothing]] |
| Null-space NMPC | decision variables = null-space coordinates, task exact by construction; 100-300 Hz on Panda (sim) | receding (time) | [[sources/sun2024nullspacempc]] |
| Ranged-goal IK | flat-inside-range losses for tolerances | per configuration | [[sources/wang2023rangedik]] |
| Null-space projected MPPI | samples projected on path/attitude constraints (preprint) | receding | [[sources/wang2024constrainedpi]] |
| Robot + extra axis, sampling planner | tool tip on curve, bounded tool axis, PRM* on joint travel | offline | [[sources/bai2024toolpath7dof]] |
| Multi-robot null-space descent (reduced Hessian) | exact path/coupling correction then descent along a null-space basis; placement + B-spline joint paths jointly; ADMM over segments; IK seeds up to 8 per robot | offline (~100-200 s for a 3-segment milling path) | [[sources/ye2026nullspacemultirobot]] |
| Smoothing of tool axis + extra axis in arc length | G3 B-spline corners, constant jerk-continuous feed; redundancy values given, not optimised | offline | [[sources/li2024weldredundant]] |
| (Our proposal) multi-goal MPPI look-ahead | MPPI over null-space coordinates on each IK branch, modes = branches, transfer by VAMP | ~10 cm receding | [[comparisons/welding-mppi-design-review]] |

## Facts worth remembering (from the sources)
- The breakpoint-minimising DP keeps a single IK branch (joint ranges restricted) and one redundancy dimension (q7 of a Franka); transfer motions are not planned; no computation times are reported ([[sources/yin2024dpbreakpoints]]).
- The real-time-adjustment DP yields a "viability margin" table usable online, but handles one disturbance dimension and no breakpoints ([[sources/yin2024dprealtime]]).
- GRR roadmaps give repeatability but consume the redundancy (no freedom left for secondary objectives); tested only in simulation, not on 5-D pose tasks ([[sources/zhong2024expansiongrr]]).
- Fast functional IK is greedy and depends on the start configuration; no joint limits, cones or collisions in the formulation ([[sources/razjigaev2025functional]]).

- **IK branches.** Typical industrial 6R arms with spherical wrist are non-cuspidal: up to 8 solutions separated by singularities, so a branch change needs a reconfiguration. Offset-wrist cobots (FANUC CRX, ABB GoFa) are cuspidal (up to 16 solutions, branch change without singularity); joint ranges beyond +-pi on axes 4/6 multiply the solutions ([[sources/elias2025cuspidal]]).
- The documented limits of Descartes (memory blow-up, no speed, torch jumps inside the tolerance, implicit singularity handling) are exactly what a null-space MPPI with rate costs and speed feasibility addresses ([[sources/demaeyer2017descartes]]).

## Plan4ARI takeaway
- DP over (path index × IK branch × roll × cone tilt × rail position) with a breakpoint cost = **deterministic baseline and cost-to-go provider** for the MPPI look-ahead; its value table can act as MPPI terminal cost and its breakpoints as the segment boundaries / transfer points.
- None of the sources handles **IK-branch switches with planned transfer motions**, **orientation cones**, **constant travel speed** and **online scene changes** together: that combination is the novelty space of the welding design.
- See [[comparisons/welding-mppi-design-review]], [[concepts/hybrid-gradient-sampling]], [[concepts/base-placement]].
