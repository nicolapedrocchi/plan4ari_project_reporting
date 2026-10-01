---
key: weingartshofer2021tcpbase
title: "Optimal TCP and Robot Base Placement for a Set of Complex Continuous Paths"
authors: "Weingartshofer, Thomas; Hartl-Nesic, Christian; Kugi, Andreas"
year: 2021
venue: "2021 IEEE International Conference on Robotics and Automation (ICRA), pp. 9659-9665"
arxiv: 
doi: 10.1109/icra48506.2021.9561900
pdf: raw/papers/weingartshofer2021tcpbase.pdf
text: raw/text/weingartshofer2021tcpbase.txt
tags: [base-placement, path-planning, continuous-path, manipulators, industrial]
status: read
---

# Optimal TCP and Robot Base Placement for a Set of Complex Continuous Paths

*Weingartshofer, Thomas; Hartl-Nesic, Christian; Kugi, Andreas* (2021). 2021 IEEE International Conference on Robotics and Automation (ICRA), pp. 9659-9665.

## TL;DR
Placement of the **TCP** (tool adapter) and, with the same machinery, of the **robot base** so that a whole *set* of complex continuous tool paths (44 shoe-sole trim paths) is executable without reconfiguration. The inner tool is a fast joint-space path planner that enumerates **all continuous IK-branch sequences** along a densely sampled 6-D path (including ±2π copies of wide-range joints and passages through singularities); the outer loop is a derivative-free surrogate optimisation (MATLAB `surrogateopt`) of a weighted score built from those paths. It is one of the few placement works that is path-level rather than point-level.

## Method
- **Robot model** (§II): 6-DoF spherical-wrist arm; analytic IK set Q_i per pose; joints with range beyond ±π add solutions by ±2π shifts, so more than the usual 8 branches exist.
- **Joint-space path planner** (§III, Alg. 1, Fig. 1): IK for every pose of the path → keep feasible solutions (joint limits). Start one candidate path per feasible IK at the first pose; at each next pose append the nearest feasible IK (Euclidean joint distance); if the jump exceeds a user threshold T the candidate is discarded. Output: all continuous joint paths P_c for the tool path. Because every IK index is tracked, passages through singularities inside one continuous path are possible. Redundant output spaces (fewer than 6 task DoF) would require sampling of the IK sets (pointer to Descartes), not done here.
- **Objective** (§IV-B, Eq. 5–10, maximised, manually weighted): f1 = mean fraction of feasible IK solutions per path point (gives a gradient where no path is yet feasible); f2 = number of continuous solutions per path (main feasibility term, creates plateaus); f3 = inverse of mean joint motion between consecutive points; f4 = margin to joint limits along the paths.
- **Optimisation** (§IV-C/D): TCP pose in R⁶ within box bounds (Eq. 11), or base position (x, y) at fixed height (Eq. 12–13); objective non-differentiable and expensive → parallel surrogate (RBF) optimisation.

## Evidence
- Robot: KUKA KR8 R1620 (Cybertech), DH and joint limits in Tab. I (q6 ±350°, q3 additionally constrained by floor and energy chain). Task: 44 trim paths (22 per shoe), e.g. n = 638 poses for one path (§V).
- Planner speed: all feasible joint paths for one trim path (n = 638) in **< 100 ms** on a Core i7-8700K, 16 GB (§V).
- Base placement (§V-A): Monte-Carlo map of the objective (Fig. 4) shows three plateaus (all / some / no paths feasible). Optimum (0.902 m, 0.003 m) (Eq. 14) found with about **25 objective evaluations**; all 44 paths executable. Fig. 5: a sub-optimal but feasible base (0.8, −0.4) m leaves much less margin on q3; the wide range of q6 is needed for continuity.
- TCP placement (§V-B): with a mis-placed base (0.6, −0.4) m only a subset of paths is feasible with the existing tool; the optimised TCP (Eq. 15) makes all 44 paths executable (Fig. 6); Fig. 7–8 show the feasible TCP position/orientation regions.
- No total wall-clock time of the placement optimisation is reported; no collisions, no dynamics/speed limits (listed as future work, §VI).

## Relevance for Plan4ARI
- Direct precedent for **path-level station feasibility**: a station (base pose) is scored by whether each seam segment has at least one continuous IK-branch path, exactly the coverage test proposed in [[concepts/base-placement]]. The planner is cheap (< 100 ms for ~600 poses) and therefore usable inside a set-cover over stations × segments.
- The objective decomposition (fraction of reachable points → number of continuous branches → joint motion → joint-limit margin) is a reusable recipe for a station score with a useful gradient even when no segment is yet feasible.
- Tracking all IK branches including ±2π copies matches our 8-goal branch set in [[comparisons/welding-mppi-design-review]].

## Critical assessment (our view)
- Exact 6-D poses only: our torch has free roll and a ~10° cone; adding them means sampling the IK sets (paper's own remark), which multiplies the candidate set — the follow-up [[sources/weingartshofer2023pathframework]] handles tolerances by optimisation instead.
- Greedy nearest-neighbour continuation per start branch, no cross-connections between branches; a jump threshold T is the only continuity check. No joint-velocity check at a given Cartesian speed, so constant-speed (±10%) feasibility is not verified; near singularities a "continuous" path may demand very high joint speeds.
- No collision checking, no robustness to base positioning error, single station (no minimisation of the number of stations). Placement is a 2-D (x, y) search at fixed yaw in the example.
- Still, it is the closest path-level analogue to our station problem found so far in the industrial literature.

## Links
- [[concepts/base-placement]] · [[concepts/path-wise-redundancy-resolution]] · [[comparisons/welding-mppi-design-review]]
- Same group / follow-ups: [[sources/weingartshofer2023pathframework]], [[sources/wachter2024baseplacement]]; related placement: [[sources/zhao2025bstar]], [[sources/farzanehkaloorazi2018pathplacement]]
- Point-based placement for contrast: [[sources/makhal2018reuleaux]], [[sources/nguyen2023taskclustering]], [[sources/gautier2024weldingbase]], [[sources/zhang2023basecoverage]]; Descartes: [[sources/demaeyer2017descartes]]
- BibTeX key: `weingartshofer2021tcpbase` in `latex/references.bib`
