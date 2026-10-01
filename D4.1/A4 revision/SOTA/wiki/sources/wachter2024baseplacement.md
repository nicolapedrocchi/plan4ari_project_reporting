---
key: wachter2024baseplacement
title: "Robot Base Placement Optimization for Pick-and-Place Sequences in Industrial Environments"
authors: "Wachter, Alexander; Hartl-Nesic, Christian; Kugi, Andreas"
year: 2024
venue: "IFAC-PapersOnLine, vol. 58, no. 19, pp. 19-24"
arxiv: 
doi: 10.1016/j.ifacol.2024.09.080
pdf: raw/papers/wachter2024baseplacement.pdf
text: raw/text/wachter2024baseplacement.txt
tags: [base-placement, path-planning, manipulators, industrial]
status: read
---

# Robot Base Placement Optimization for Pick-and-Place Sequences in Industrial Environments

*Wachter, Alexander; Hartl-Nesic, Christian; Kugi, Andreas* (2024). IFAC-PapersOnLine, vol. 58, no. 19, pp. 19-24.

## TL;DR
Base placement for a cyclic pick-and-place sequence in which every candidate base is scored by **actually planning the free-space trajectories** (VP-STO, MuJoCo MJX collision checks) through a graph over all IK solutions of every pose (Dijkstra with cyclic constraint). An asynchronous Bayesian black-box optimiser dispatches candidate bases to parallel workers. Objectives: cycle time, time + energy, or a "throughput-adaptive" cost (time-optimal motions that are time-scaled to minimise energy at a longer cycle time).

## Method
- **Problem** (§3): base b = (x, y, z, rotation about z); task = N poses visited by point-to-point (P2P) motions, cyclic (first = last configuration); constraints: collisions, kinodynamic limits.
- **P2P planner** (§4.1, Alg. 1): VP-STO via-point stochastic trajectory optimisation (low-dimensional, limit-respecting by construction), modified with a 100× larger population for the first 10 generations and then only the 10 best; warm start from a database of trajectories planned for similar bases/configurations; collision checks in MuJoCo MJX.
- **Cyclic planner** (§4.2, Alg. 2, Fig. 2): layered graph with all IK solutions per pose as nodes and P2P costs as edges (computed independently and in parallel); Dijkstra with the cyclic constraint.
- **Outer loop** (§4.3, Fig. 1): OpenBox black-box (Bayesian) optimisation with W asynchronous workers.
- **Costs** (§4.4–4.6): cycle time T; C = T + wE with E the integral of τᵀq̇ (Eq. 1–3); throughput-adaptive: time-optimal segments scaled by factors c_i ≥ 1 to minimise energy subject to Σ c_i T_i ≤ T_max (Eq. 4).

## Evidence
- Simulation only: SCARA, N = 14 poses between 7 stations, up to 6 IK solutions per pose (last joint ±2π); z fixed (no effect for a SCARA); dynamics approximated by an average mass matrix (§5).
- Two scenes, sparse and complex (with a fence). Tab. 1 (each column normalised to its minimum): in the sparse scene the worst feasible base has 1.78× the optimal cycle time (−44%) and 2.11× the time-energy cost (−53%); human expert 1.21×; manipulability-based placement 1.17×; joint-distance placement (no collisions) 1.11×; Cartesian-distance placement invalid. In the complex scene the gains vs the worst base are 17% (time) and 23% (time-energy), and all three baseline heuristics give **invalid** placements (§5.2–5.3).
- Throughput-adaptive placement: 4% slower than the cycle-time-optimal one at high throughput but 14% less energy at T_max = 2.5 T_min; the time-energy-optimal placement needs 9% more energy than it at low throughput (§5.2).
- Runtime ≈ **80 min on a 90-core machine** per placement; index-based methods take a few minutes on the same hardware (§5.4).

## Relevance for Plan4ARI
- Shows the "plan the real motions inside the placement loop" paradigm and quantifies why proxies (manipulability, joint/Cartesian distance) fail in cluttered cells — relevant for stations close to a large steel structure.
- The layered IK graph with a cyclic constraint is a template for including **transfer motions between seam segments** in station evaluation (our transfers are planned with a sampling planner, cf. VAMP in [[comparisons/welding-mppi-design-review]]).
- Asynchronous Bayesian optimisation with parallel workers and a trajectory warm-start database is a practical pattern for an expensive per-station feasibility check.

## Critical assessment (our view)
- **Point-to-point only**: no continuous process path; seam following, orientation cones and constant speed are out of scope. For our problem it covers only the transfer/approach part.
- Single base, single station; no minimisation of the number of stations, no robustness to positioning error.
- SCARA in simulation with an approximated dynamic model; a 6-axis arm (8+ IK branches, richer collision geometry) will raise an already heavy cost (80 min on 90 cores).
- Bayesian optimisation gives no guarantee of global optimality, despite the authors' wording.

## Links
- [[concepts/base-placement]] · [[comparisons/welding-mppi-design-review]]
- Same group: [[sources/weingartshofer2021tcpbase]], [[sources/weingartshofer2023pathframework]]; inner planner: [[sources/jankowski2023vpsto]]; related: [[sources/zhao2025bstar]], [[sources/makhal2018reuleaux]]
- BibTeX key: `wachter2024baseplacement` in `latex/references.bib`
