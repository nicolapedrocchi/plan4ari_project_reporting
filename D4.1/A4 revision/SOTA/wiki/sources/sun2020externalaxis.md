---
key: sun2020externalaxis
title: "Semi-constrained Path Planning for Industrial Robot with External Axis"
authors: "Sun, Yu; Meng, Xiangqun; Yu, Miaocheng; Tang, Houjun"
year: 2020
venue: "2020 Chinese Automation Congress (CAC), pp. 6180-6185"
arxiv: 
doi: 10.1109/cac51589.2020.9327766
pdf: raw/papers/sun2020externalaxis.pdf
text: raw/text/sun2020externalaxis.txt
tags: [path-planning, external-axis, redundancy-resolution, manipulators, industrial, welding]
status: read
---

# Semi-constrained Path Planning for Industrial Robot with External Axis

*Sun, Yu; Meng, Xiangqun; Yu, Miaocheng; Tang, Houjun* (2020). 2020 Chinese Automation Congress (CAC), pp. 6180-6185.

*Note: the extracted text in `raw/text/` is garbled (font encoding); this page was written from the PDF.*

## TL;DR
Sampling-plus-graph-search planner for a 6-axis industrial robot with external axes (linear gantry or rotary axis) following a Cartesian curve with **tolerances** ("semi-constrained" path, e.g. free rotation about the tool z-axis). The configuration space is decoupled into an external-axis space and a task space: external-axis values and tolerance-admissible tool poses are sampled on grids, analytic IK (IKFast, up to 8 branches) maps each sample to arm joints, and a shortest path over the layered C-space graph minimises weighted joint motion. In practice a Descartes-like ladder graph extended with external-axis samples.

## Method
- **Semi-constrained task space** (§III-A, Eq. 1): each path point is a pose (x, y, z, Rx, Ry, Rz) with per-component tolerance intervals; the experiments only use free rotation about the tool Z axis. **External-axis space** (Eq. 2): box of external-axis values e1…en.
- **Sampling space** S_a = T × E_x (Eq. 3, §III-B): for each path point the external axes are sampled at equal intervals within their range (fixing the robot base pose), then the pose tolerance interval is sampled at equal intervals.
- **IK** (§III-C): analytic IK of the 6-axis arm only (IKFast), up to 8 solutions per sample; colliding or out-of-limit solutions discarded (MoveIt!, FCL, KDL, §IV-B).
- **Graph and search** (§III-D, Alg. 1–2, Fig. 3): one layer per path point; edges between consecutive layers only if a kinematic validity check (e.g. velocity limits) passes; edge cost (Eq. 4) = weighted squared joint differences plus an application-specific loss term; DAG shortest path by dynamic programming in O(V+E).

## Evidence
- Simulation only, MoveIt!/ROS on a laptop (i5-7300HQ, 6 GB RAM, §IV-B).
- Task 1 (§IV-A): ABB IRB120 on a **2-DoF linear gantry**, cylinder-intersection curve, orientation fixed except tool-Z rotation (Fig. 4–5, qualitative only).
- Task 2: ABB IRB1200 with a **1-DoF rotary external axis**, circular curve on a rotating tube (Fig. 6–7).
- Table I (Task 2, 60 path points): 5 / 30 / 180 samples per point → IK time 0.7 / 3.3 / 19.2 s, graph search 0.08 / 2.31 / 60.81 s, total joint rotation 11.6 / 10.2 / 8.9 rad.
- Table II (180 samples): 30 / 60 / 90 path points → IK 7.5 / 19.2 / 27.3 s, search 22.89 / 60.81 / 86.10 s, total rotation 8.6 / 8.9 / 9.0 rad.
- No hardware test, no comparison with other planners, no time parametrisation (velocity limits only as an edge validity test).

## Relevance for Plan4ARI
- Closest match to the **"6-axis arm + interpolated linear 7th axis"** option on a semi-constrained (free-roll) seam: rail position as an extra sampled dimension of a ladder graph is a simple deterministic offline baseline for one seam segment at one station.
- The decoupling "fix external axis → base pose known → analytic IK" keeps IK cheap with a rail; the same trick applies to MPPI rollouts (sample rail + roll + cone, analytic arm IK per branch).
- Tables I–II show the cost of brute-force grids: with one extra DoF and fine sampling, ~60 points already take minutes on a laptop. Long seams plus a 2-D cone would explode the grid, which argues for coarse DP for station feasibility checks and receding-horizon sampling for execution.

## Critical assessment (our view)
- Minimises joint travel only; no explicit **constant travel speed**, branch-switch/reconfiguration handling, singularity or joint-limit margins (the "no singularity" claim is qualitative, Fig. 5/7).
- External axis sampled independently at each path point; smooth rail motion is only encouraged by the edge cost, and rail weighting in Eq. 4 is not studied.
- Only a single free rotation tested; an orientation **cone** fits Eq. 1 but is not evaluated.
- Small evaluation (two curves, simulation, conference paper): numbers indicate scaling only.

## Links
- [[concepts/path-wise-redundancy-resolution]]
- [[concepts/base-placement]]
- [[comparisons/welding-mppi-design-review]]
- [[applications/industrial-manipulators]]
- Related: [[sources/demaeyer2017descartes]] (ladder-graph Cartesian planning), [[sources/yin2024dpbreakpoints]], [[sources/bai2024toolpath7dof]] (rotary table as 7th axis), [[sources/dharmawan2018functional]]
- BibTeX key: `sun2020externalaxis` in `latex/references.bib`
