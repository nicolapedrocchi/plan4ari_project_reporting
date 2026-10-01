---
key: wachter2024tcpbase
title: "Time-Optimal TCP and Robot Base Placement for Pick-and-Place Tasks in Highly Constrained Environments"
authors: "Wachter, Alexander; Kugi, Andreas; Hartl-Nesic, Christian"
year: 2024
venue: "2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 2251-2257"
arxiv: 
doi: 10.1109/iros58592.2024.10801373
pdf: raw/papers/wachter2024tcpbase.pdf
text: raw/text/wachter2024tcpbase.txt
tags: [base-placement, path-planning, manipulators, industrial]
status: read
---

# Time-Optimal TCP and Robot Base Placement for Pick-and-Place Tasks in Highly Constrained Environments

*Wachter, Alexander; Kugi, Andreas; Hartl-Nesic, Christian* (2024). 2024 IEEE/RSJ International Conference on Intelligent Robots and Systems (IROS), pp. 2251-2257.

## TL;DR
Simultaneous optimisation of robot base position (2-D) and TCP geometry (7 parameters) for a cyclic pick-and-place sequence, with the **actual minimum cycle time** as objective: an asynchronous parallel Bayesian optimiser proposes {base, TCP}; each worker builds a graph over all IK solutions and grasp alternatives, plans every edge with a time-optimal stochastic trajectory optimiser (modified VP-STO, collision checking in MuJoCo MJX) and runs Dijkstra with a cyclic constraint. 41% lower cycle time than a manipulability-based placement.

## Method
- Decision variables (§III–IV): base offset b = [bx, by]; TCP t = points c, d and rotation r defining a cubic B-spline tool shape and a tube collision mesh (Fig. 3).
- Outer loop (§V, Fig. 4): asynchronous Bayesian optimisation (OpenBox) dispatching candidates to W parallel workers.
- Inner loop (Alg. 2, Fig. 2): enumerate IK solutions for every pick/place pose and grasp alternative; plan each P2P edge with VP-STO (Alg. 1; population ×100 for the first 20 iterations, then the 20 best kept); warm start from a database of trajectories with similar start/goal and placement; Dijkstra on the layered graph with cyclic constraint q1 = qL.
- TCP realised by topology optimisation (Fusion 360) under the force profile computed from the optimal trajectory (§V-C).

## Evidence
- KUKA LBR iiwa 14 R820 (7 DoF, analytic IK with elbow/wrist branches, elbow angle sampled at 12 values); no extra axes; packaging scenario with L = 8 poses and two-fold grasp redundancy (§VI-A).
- Table I, minimum cycle time: base+TCP 17.58 s; base only with trivial TCP 25.64 s (+46%, §VI-C); manipulability-based 29.61 s (proposed 41% lower, §VI-D); joint-space distance 22.98 s; Cartesian distance infeasible.
- SHAP feature importance (Fig. 7): base placement 2.01, TCP parameters 0.18–0.51.
- Runtime (§VI-E): about 360 min on 90 cores; one P2P plan about 6 s cold, 1.21 s with database warm start, 4.1 ms when an endpoint is in collision; index-based methods take a few minutes but give worse or infeasible placements.
- Experiment (§VII): printed PLA TCP (topology optimisation with safety factor 2 gives 78% mass reduction for PLA, 88% for AlSi10Mg); measured IMU accelerations agree with simulation (Fig. 8–9).

## Relevance for Plan4ARI
- Strong evidence for our station-planning principle: **score placements by the actual motion (feasibility/time), not by reachability or manipulability proxies**, which here gave 41% worse or infeasible results ([[concepts/base-placement]]).
- Architecture transferable to AGV station planning: outer black-box optimiser over (station x, y, yaw, rail interval), inner evaluation = path-wise feasibility of the seam segment over all IK branches (graph over branches as in Alg. 2), with a warm-start database shared across nearby candidates.
- Base placement dominates (SHAP 2.01 vs ≤ 0.51), supporting priority on AGV/rail placement over tool geometry; torch-neck geometry could still be treated like the TCP parameters.

## Critical assessment (our view)
- Free-space P2P tasks, not continuous constrained paths; welding needs path-wise evaluation at constant speed (continuous-path counterpart: [[sources/weingartshofer2021tcpbase]]).
- About 6 h on 90 cores for 8 poses and a 2-D base is far beyond an online budget; with many stations on a large structure, much cheaper inner evaluations (coarse DP, reachability pre-filter) are needed.
- Base restricted to 2-D translation (no yaw), no positioning uncertainty, static cell; AGV docking errors would require robustness margins.
- Single scenario; optimality of the Bayesian optimiser is empirical.

## Links
- [[concepts/base-placement]]
- [[comparisons/welding-mppi-design-review]]
- [[applications/industrial-manipulators]]
- Related: [[sources/weingartshofer2021tcpbase]] (TCP/base for continuous paths), [[sources/wachter2024baseplacement]], [[sources/jankowski2023vpsto]] (VP-STO), [[sources/makhal2018reuleaux]], [[sources/gautier2024weldingbase]]
- BibTeX key: `wachter2024tcpbase` in `latex/references.bib`
