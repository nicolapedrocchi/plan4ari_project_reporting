---
key: tang2023dualrobotweld
title: "A Dual-Robot Cooperative Arc Welding Path Planning Algorithm based on Multi-Objective Optimization"
authors: "Tang, Qichao; Ma, Lei; Zhao, Duo; Sun, Yongkui; Wang, Qingyi"
year: 2023
venue: "IFAC-PapersOnLine, vol. 56, no. 2, pp. 3048-3053"
arxiv: 
doi: 10.1016/j.ifacol.2023.10.1433
pdf: raw/papers/tang2023dualrobotweld.pdf
text: raw/text/tang2023dualrobotweld.txt
tags: [welding, multi-robot, industrial, task-allocation]
status: read
---

# A Dual-Robot Cooperative Arc Welding Path Planning Algorithm based on Multi-Objective Optimization

*Tang, Qichao; Ma, Lei; Zhao, Duo; Sun, Yongkui; Wang, Qingyi* (2023). IFAC-PapersOnLine, vol. 56, no. 2, pp. 3048-3053.

## TL;DR
Seam-level **task allocation and sequencing** for two arc welding robots on a large complex component, posed as a bi-objective problem: minimise total no-load (air-move) distance and total waiting time, subject to synchronous-welding pairs (seams welded simultaneously against distortion), fixed welding directions, asynchronous pairs and an inter-robot collision constraint. Seams are pre-classified as exclusive to robot 1, exclusive to robot 2, or competitive (reachable by both). A permutation-coded NSGA-II variant (R-NSGA-II) replaces mutation with a "recombination" operator that swaps half of the genes within an individual. On 27 seams in MATLAB its Pareto front dominates NSGA-II and OMOPSO; at a selected point it reports 42.39% less waiting time and 10.50% less no-load distance than NSGA-II. Despite the title, it is a combinatorial sequencing problem: there is no robot kinematics, joint-space path or motion planning.

## Method
- **Model (§2)**: seam set W with start/end points and lengths; two robots with welding speed v₁ and no-load speed v₂. Decision variables: assignment of competitive seams and the visiting order of each robot. Objectives: no-load distance D_nd = Σ Euclidean distances from the end of one seam to the start of the next (Eq. 6); waiting time T_w = Σ (actual − unconstrained) completion time of each robot (Eq. 7). Constraints: synchronous seams must share start and end times (Eq. 8); fixed welding direction (Eq. 9); robots' occupied volumes must not intersect (Eq. 10).
- **R-NSGA-II (§3)**: individual = permutation of seam IDs (exclusive seams of each robot + randomly assigned competitive seams, Eq. 12); fast non-dominated sorting + crowding distance (Alg. 2); one-point crossover with duplicate removal (Alg. 3); recombination swapping two random halves of gene positions within an individual (Alg. 4); elitist merge of parents and offspring; termination on generations/evaluations.

## Evidence
- **Scenario (§4, Fig. 1, Table 1)**: 27 typical seams of a large complex component; exclusive seams 1–6, 14–19, 26 (robot 1) and 7–12, 20–25, 27 (robot 2); synchronous pair 3 & 7; asynchronous pair 26 & 27; competitive seam 13.
- **Parameters (Table 2)**: population 100, welding speed 10 mm/s, no-load speed 20 mm/s, crossover probability 0.7, recombination probability 0.3, recombination ratio 0.5. MATLAB 2021b, Intel i9 2.3 GHz, 32 GB.
- **Results (§4.2–4.3, Figs. 4–5)**: R-NSGA-II front dominates NSGA-II and OMOPSO; chosen solution waiting time 7.23 s and no-load distance 5.37·10³ mm vs NSGA-II 12.55 s and 6.00·10³ mm (−42.39%, −10.50%). Seam 13 assigned to robot 1; robot 2 waits 7.23 s at seam 7 before the synchronous pair 3/7.
- Not reported: computation time, number of generations, number of independent runs/statistics, how the collision constraint is evaluated.
- Stated future work (§5): more objectives (e.g. balance of welding time), parameter tuning, more complex problems.

## Relevance for Plan4ARI
- Covers the **allocation/sequencing layer** for possible multi-robot cooperation in our design (flaws #19–21 in [[comparisons/welding-mppi-design-review]]): synchronous seams against distortion, competitive seams in overlapping workspaces, and waiting-time minimisation are exactly the decisions the design assigns to the task planner (Activity 2), above the per-robot MPPI.
- Its constraint types (synchronous / asynchronous / direction) are a compact vocabulary for the interface between task planner and motion layer: a synchronous pair imposes a time-coupling that our per-robot MPPI with others as dynamic obstacles ([[sources/streichenberg2023mapi]], [[sources/jansma2023interaction]]) must respect, e.g. through a shared start time and matched travel speeds.
- For AGV-mounted robots the cost terms must change: no-load distance becomes AGV/station transfer time, and seam allocation is coupled with station placement ([[sources/gautier2024weldingbase]], [[concepts/base-placement]]).

## Critical assessment (our view)
- Kinematics-free abstraction: no-load distance is Euclidean between seam endpoints, robot reachability and orientation constraints are absent, so assignments may be infeasible or need reconfigurations not counted in the cost.
- The collision constraint is stated but its evaluation is not described; synchronous welding is only a timing constraint, not a coordinated motion problem.
- Evidence is a single instance with one selected Pareto point and no statistics or run-time; the 42.39% / 10.50% gains come from that point comparison only.
- Useful as a problem formulation reference, not as an algorithmic baseline for D4.1 motion planning.

## Links
- [[comparisons/welding-mppi-design-review]]
- [[applications/industrial-manipulators]]
- [[concepts/base-placement]]
- Related: [[sources/streichenberg2023mapi]], [[sources/jansma2023interaction]], [[sources/gautier2024weldingbase]], [[sources/zhou2022weldavoidance]] (cited by the authors; names multi-robot cooperation as future work), [[sources/demaeyer2021weldbenchmark]], [[sources/demaeyer2017descartes]], [[sources/wang2026torchposture]]
- BibTeX key: `tang2023dualrobotweld` in `latex/references.bib`
