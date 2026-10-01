---
key: elias2025cuspidal
title: "Path Planning and Optimization for Cuspidal 6R Manipulators"
authors: "Elias, Alexander J.; Wen, John T."
year: 2025
venue: "Journal of Mechanisms and Robotics, vol. 17, no. 12, pp. 121008"
arxiv: 2501.18505
doi: 10.1115/1.4069599
pdf: raw/papers/elias2025cuspidal.pdf
text: raw/text/elias2025cuspidal.txt
tags: [inverse-kinematics, path-planning, manipulators, industrial, welding, cuspidal-robots]
status: read
---

# Path Planning and Optimization for Cuspidal 6R Manipulators

*Elias, Alexander J.; Wen, John T.* (2025). Journal of Mechanisms and Robotics, vol. 17, no. 12, pp. 121008.

## TL;DR
**Cuspidal** robots can move between IK solutions without crossing a singularity, so IK "branch" labels (elbow up/down, etc.) lose meaning, and a Cartesian path can be feasible only from some initial solutions — or not at all — even if every point is reachable. The paper (i) gives a cheap randomised test for cuspidality using the complete IK solver IK-Geo, showing for the first time that the **ABB GoFa** and some robots with three parallel axes are cuspidal; (ii) plans joint paths along a fixed 6-DoF task path with a **layered DAG over all IK solutions** (Descartes-like, but with all solutions, ±π wrapping, optional singularity/regularity constraints and robustness to missed IK); (iii) wraps the planner in a derivative-free optimisation of the **toolpath placement** in the robot frame (base/workpiece pose).

## Method
- Definitions (§2.1): aspect (max singularity-free connected region in joint space), cuspidal = several IK solutions in one aspect, feasible path (continuous joint path, possibly through singularities), repeatable/regular closed paths.
- **Key structural fact** (§2.3.1): robots whose IK reduces to quadratics are non-cuspidal; typical cases are a **spherical wrist**, or three parallel axes plus two other intersecting/parallel axes. A 6R arm with spherical wrist is cuspidal iff its first-three-link 3R arm is cuspidal.
- **Identification** (§3.2): random pose → all IK solutions (IK-Geo) → pairs with equal sign(det J) → check whether a linear joint-space move between them keeps det J ≠ 0; if yes the robot is cuspidal.
- **Graph path planning** (§4): discretise the path in K+1 points; vertices = all IK solutions per point; edges between consecutive layers if the wrapped squared joint step / Δλ is below a threshold ε (≈ max joint speed); start/finish super-nodes; shortest path = optimal feasible joint path (cost ≈ ∫‖dq/dλ‖²). Options: forbid edges across sign(det J) changes (non-singular paths), joint limits with turn counting, cycles for repeatable closed paths, skip-one-layer edges for missed IK solutions, continuous approximate (least-squares) IK at boundary singularities.
- **Path optimisation** (§5): optimise workpiece pose (quaternion + offset, one DoF removed by symmetry about axis 1) with MATLAB fminsearch, running the graph planner at each iteration; random restarts for feasibility and global search.

## Evidence
- Cuspidality shown for all three GoFa variants (Fig. 6) and for a constructed robot with three parallel axes (Fig. 7). RobotStudio returns at most 8 IK solutions for the GoFa although it has up to 16; ROBOGUIDE likewise returns up to 8 for the FANUC CRX, which has up to 16 (§1, §2.2).
- MoveL examples (graph method, 200 samples): GoFa — 8 initial and 10 final IK solutions but only **6 feasible paths** (Fig. 3); CRX-10iA/L — 8 initial/final, up to 12 intermediate solutions, only **2 feasible paths** (Fig. 4).
- Non-cuspidal ABB IRB 6640 (spherical wrist): a path fully inside the workspace that is infeasible for every configuration class (Fig. 5); the authors note joint limits prevent this in practice.
- IK-Geo: under 1 ms per pose for robots with at least one intersecting/parallel axis pair, vs ~10 ms (Husty-Pfurner) and 8.52 s for the multiple-shooting identification of prior work (§3.2).
- Path optimisation on 500-point helical paths (§5.3): canonical 3R RMS joint velocity 0.8209 → 0.3874 rad/m and 0.5690 → 0.3149 rad/m (two seeds); CRX-10iA/L 13.9328 → 10.0447 rad/m and 13.1054 → 9.9929 rad/m; multiple local minima.
- **No computation times for the graph planner or the optimisation loop are reported.** Collision avoidance is not included (future work).

## Relevance for Plan4ARI
- **"≤ 8 IK branches" assumption** in [[comparisons/welding-mppi-design-review]]: for the typical industrial welding arm (6R, two parallel axes, spherical wrist — e.g. ABB IRB 6640, Yaskawa MA2010 cited in §1) the paper confirms **non-cuspidal, up to 8 IK solutions, separated by singularities**, so a branch label is a valid, invariant mode identifier and a branch change necessarily requires crossing a singularity → our "detach/reconfigure" is the right model. The assumption **does not hold** for offset-wrist cobots increasingly sold for welding (FANUC CRX, Kinova Link 6, ABB GoFa): up to 16 solutions, branches can change smoothly during the weld (and a re-run of the same closed weld may get stuck), and vendor software may report only 8.
- Even for non-cuspidal arms the paper stresses that feasibility depends on the initial branch (Fig. 5) — exactly why we evaluate all branches per segment and prune upfront.
- Joint ranges beyond ±π (common on axes 4 and 6 of welding robots; also torch-hose wrap) multiply the distinct joint-space solutions; the turn-counting remark (§4.2) applies to our goal set, which should be "branch × turn" where limits allow.
- The DAG planner is a clean **global feasibility/cost-to-go check** for a seam segment and its §5 placement optimisation is a path-level version of station placement ([[concepts/base-placement]]).

## Critical assessment (our view)
- Fully constrained 6-DoF task path only: the torch-roll/cone null space is not explored (would need a sampled tolerance dimension as in [[sources/wang2025anytimetracking]] or DP over roll as in [[sources/yin2024dpbreakpoints]]).
- No timing, no collision, no speed limits beyond an edge threshold; derivative-free outer optimisation with random restarts is slow and local.
- Practical rule for us: **check the kinematic class of the target arm**; if it is a spherical-wrist industrial arm keep 8 discrete modes (× turns), if it is an offset-wrist cobot replace branch labels with connectivity computed by a graph over all IK solutions (as here) and do not rely on vendor configuration flags.

## Abstract (verbatim, arXiv)
> A cuspidal robot can move from one inverse kinematics (IK) solution to another without crossing a singularity. Multiple industrial robots are cuspidal. They tend to have a beautiful mechanical design, but they pose path planning challenges. A task-space path may have a valid IK solution for each point along the path, but a continuous joint-space path may depend on the choice of the IK solution or even be infeasible. This paper presents new analysis, path planning, and optimization methods to enhance the utility of cuspidal robots. We first demonstrate an efficient method to identify cuspidal robots and show, for the first time, that the ABB GoFa and certain robots with three parallel joint axes are cuspidal. We then propose a new path planning method for cuspidal robots by finding all IK solutions for each point along a task-space path and constructing a graph to connect each vertex corresponding to an IK solution. Graph edges have a weight based on the optimization metric, such as minimizing joint velocity. The optimal feasible path is the shortest path in the graph. This method can find non-singular paths as well as smooth paths which pass through singularities. Finally, we incorporate this path planning method into a path optimization algorithm. Given a fixed workspace toolpath, we optimize the offset of the toolpath in the robot base frame while ensuring continuous joint motion. Code examples are available in a publicly accessible repository.

## Links
- [[concepts/path-wise-redundancy-resolution]]
- [[concepts/base-placement]]
- [[comparisons/welding-mppi-design-review]]
- [[applications/industrial-manipulators]]
- Related: [[sources/demaeyer2017descartes]], [[sources/wang2025anytimetracking]], [[sources/chen2025cooptimization]], [[sources/lu2022toolorientation]]
- BibTeX key: `elias2025cuspidal` in `latex/references.bib`
