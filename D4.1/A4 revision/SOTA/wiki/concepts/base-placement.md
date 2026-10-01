---
title: Base / station placement for mobile manipulators
type: concept
updated: 2026-10-01
---

# Base / station placement for mobile manipulators

**Problem.** Choose where (and how many times) to park the mobile base / AGV so that the arm can execute all task segments, minimising the number of stations, total time and reconfiguration risk. For Plan4ARI welding: the "raw positioning" upstream of the MPPI look-ahead ([[comparisons/welding-mppi-design-review]]).

## Building blocks
| Block | Idea | Sources |
|---|---|---|
| Reachability / inverse reachability maps | offline voxel map of reachable poses; inverted and transformed by task poses → scored candidate bases (ground slice x, y, yaw) | [[sources/makhal2018reuleaux]] (open source, ROS 1) |
| Minimum number of stations | set-cover over targets × floor grid using reachability; then sequencing (TSP + IK graph search) | [[sources/nguyen2023taskclustering]] |
| Coverage with flexible constraints | surface split into discs (centre, normal, radius); NSGA-II over number and poses of stops (coverage, time, manipulability) | [[sources/zhang2023basecoverage]] |
| Base/TCP placement for **continuous paths** | enumerate continuous IK-branch sequences per path (<100 ms per 638-pose path), surrogate optimiser over placement | [[sources/weingartshofer2021tcpbase]] |
| Placement scored by real cycle time | Bayesian optimisation over base (+TCP), inner time-optimal planning over IK branches; hours on 90 cores | [[sources/wachter2024tcpbase]], [[sources/wachter2024baseplacement]] |
| Joint base + path optimisation | base mobile per waypoint, frozen by growing l1 penalty; ~2.8 s for 64 poses | [[sources/zhao2025bstar]] |
| Placement of a positioner in a redundant cell | PSO over hexapod pose, rotary table as interpolated axis, det J sign test against working-mode changes | [[sources/farzanehkaloorazi2018pathplacement]] |
| Welding-specific feasibility | per base pose and seam: collisions, singularity margin, joint speed and static torque along the whole seam at constant speed; morphology comparison | [[sources/gautier2024weldingbase]] |

## Facts worth remembering (from the sources)
- Set-cover station selection reduced base poses to 2 vs 8 and 70 for baselines on 264 drilling targets, with 5-D targets (position + tool axis, free roll) ([[sources/nguyen2023taskclustering]], Table II).
- Constant-speed welding around a corner broke joint-speed limits (feasible speed dropped to 57 and 35 cm/min for the two arms), and morphology changed the number of base positions needed ([[sources/gautier2024weldingbase]]).
- All sources treat targets as points or discs: **no path-level, no-reconfiguration, constant-speed feasibility** and no robustness to AGV positioning error.

- **Accuracy budget.** Mobile machining of a large workpiece with global localisation + CAD registration left TCP errors up to ~40 mm; platform localisation dominates ([[sources/zhao2021mobilemachining]]) -> per-station local seam registration / seam tracking is a prerequisite for welding.
- Still missing in all sources: constant-speed feasibility, orientation cones at station level, minimum number of stations for continuous seams.

## Plan4ARI takeaway
- Station planning = set-cover over **seam segments** (not points), where a segment is "covered" by a station only if a path-wise feasibility check succeeds on at least one IK branch (DP of [[concepts/path-wise-redundancy-resolution]] or a Gautier-like checklist), with margins for AGV positioning error and the ~10° cone.
- Linear 7th axis: stations become intervals along the rail, reducing the number of stations.
- Links: [[applications/mobile-robots-amr]], [[applications/industrial-manipulators]].
