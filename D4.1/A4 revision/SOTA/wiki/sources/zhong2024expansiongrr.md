---
key: zhong2024expansiongrr
title: "Expansion-GRR: Efficient Generation of Smooth Global Redundancy Resolution Roadmaps"
authors: "Zhong, Zhuoyun; Li, Zhi; Chamzas, Constantinos"
year: 2024
venue: "Proc. IEEE/RSJ Int. Conf. Intelligent Robots and Systems (IROS), pp. 8854-8860"
arxiv: 2405.13770
doi: 10.1109/IROS58592.2024.10801917
pdf: raw/papers/zhong2024expansiongrr.pdf
text: raw/text/zhong2024expansiongrr.txt
tags: [redundancy-resolution, roadmap, repeatability, inverse-kinematics, manipulators, path-planning]
status: read
---

# Expansion-GRR: Efficient Generation of Smooth Global Redundancy Resolution Roadmaps

*Zhong, Zhuoyun; Li, Zhi; Chamzas, Constantinos* (2024). Proc. IEEE/RSJ Int. Conf. Intelligent Robots and Systems (IROS), pp. 8854-8860.

## TL;DR
Expansion-GRR builds a **global redundancy resolution (GRR) roadmap**. It discretises the task space (T-space) into a grid graph and assigns exactly one configuration to each task point. Neighbouring configurations must be continuous (checked by recursive bisection with projection), so every task-space path, cyclic paths included, maps to the same joint path. This gives repeatable, predictable motion. The roadmap is grown breadth-first from a few seeds taken on one cyclic path: each new point is the IK projection of a distance-weighted average of its already-assigned neighbours. Compared with the earlier Random-GRR of Hauser & Emmons (2018), it builds the roadmap up to 2 orders of magnitude faster and the result is smoother. In emulated teleoperation it reached 100% success, where Newton IK and RelaxedIK got stuck in local minima or singularities.

## Method
- Problem (§III): T-space graph G_p (grid). Find a C-space graph G_q that is (1) **injective**, with one q per self-motion manifold; (2) **continuous** on every T-edge; (3) **smooth**, meaning a small mean ratio of C-space to T-space edge length (Eq. 3). All this at minimum build time.
- **Projection** = Newton-Raphson (Jacobian pseudo-inverse) IK from a guess, followed by a self-collision check (§IV-A).
- **Continuity check** (Alg. 1, after Taylor 1979): bisect the T-edge and the C-edge, project the C-midpoint onto the self-motion manifold of the T-midpoint, reject if the deviation exceeds c·D_q(q_i, q_j), and recurse down to resolution ε. Defaults scale with dim(C): c = 0.5·dim(C), ε = 0.05·dim(C).
- **Projection from multiple neighbours** (Alg. 2): take the k nearest T-neighbours that already have configurations, weight them by inverse squared distance, average in C-space, then project. T-distance (Eq. 1) is the Euclidean translation distance plus 1-|quaternion dot product|, with w_t = 1, w_o = 0.3. The value of k is not reported.
- **Multi-seed strategy** (§IV-C, Fig. 6): one seed can grow two incompatible branches (elbow-up and elbow-down) that clash where they meet. Seeding from the configurations of one continuous cyclic path avoids this. That path was created **manually** for each robot.
- **Global expansion** (Alg. 3): breadth-first search over G_p. Unassigned points get ProjectNeighbors, then edges are added to G_q when IsContinuous passes.
- **Use** (§IV-E): (i) as an IK solver or warm-start generator for any p, using neighbours in the largest connected component; (ii) T-space path planning: search G_p, interpolate along its edges, ProjectNeighbors at each waypoint, so the C-path is continuous by construction; (iii) teleoperation: if the step to the commanded target fails IsContinuous, track the nearest valid roadmap node, then re-plan on the roadmap once the command becomes feasible again.

## Evidence
- Hardware: Intel i5-10400, 16 GB RAM, simulation only (§V). Robots: 5-link planar arm (5 DoF, continuous joints without limits, self-intersection allowed) with T = R² and T = SE(2) with fixed rotation; Kinova Gen3 (7 DoF) with Robotiq-85, T = R³ and SE(3) with fixed downward orientation (§V-B).
- **Roadmap quality** (Table I; Random-GRR uses 100 random samples per T-point): both methods reach 100% connectivity in all four settings.
  - Smoothness, Random vs Expansion: 16.853 vs 5.675 (planar, position), 24.528 vs 8.992 (planar, fixed rotation), 9.223 vs 2.563 (Kinova, position), 11.205 vs 4.299 (Kinova, fixed rotation).
  - **Build time**: 2.023 vs 0.095 min, 1.862 vs 0.150 min, 22.971 vs 0.201 min, 72.013 vs 0.196 min.
  - Grid sizes: 1,013 vertices (planar) and 3,299 vertices (Kinova).
- **Teleoperation** (Table II): Kinova, fixed-rotation task. 4 task types × 100 random paths, each streamed as 200 waypoints at 50 Hz over 4 s. Success rates for Newton IK / RelaxedIK / Random-GRR / Expansion-GRR:
  - Random Line: 90 / 78 / 49 / **100**
  - Self-crossing Line: 30 / 54 / 34 / **100**
  - Random Circle: 98 / 98 / 77 / **100**
  - Partially Reachable Circle: 99 / 95 / 78 / **100**
  - Deviation equals Newton IK on the random line and circle (0.011, 0.022). It is higher on self-crossing (0.461 vs RelaxedIK 0.184) and partially reachable paths (0.166 vs Newton IK 0.085), because these need detours (§V-C).
  - Path smoothness is worse than the IK solvers (e.g. 5.071 vs 4.395 for Newton IK on the random line) but better than Random-GRR. The authors note this is expected, because the method puts global consistency before smoothness.
- Limitations stated by the authors (§VI): it uses **all** the redundancy to satisfy the T-space constraint, so it leaves no room for secondary objectives. Seed selection is manual. Full connectivity is not guaranteed, e.g. with obstacles. Code is open source (github.com/elpis-lab/Expansion-GRR).

## Relevance for Plan4ARI
- This is the "global" end of [[concepts/path-wise-redundancy-resolution]]: a fixed, consistent map from seam pose to joint configuration. The same seam point then always gets the same configuration, across retries, restarts after a stop/retract/reconfigure 1 cm back, and repeated parts. This is the repeatability property our MPPI look-ahead does not give by itself [[comparisons/welding-mppi-design-review]].
- Possible roles: (i) a **warm start or prior** for the MPPI nominal trajectory, or a cost term pulling rollouts toward the roadmap configuration; (ii) a lookup for which IK branch to use at the first seam point; (iii) detecting where in the workspace a continuous mapping breaks, which is where configuration changes are unavoidable.
- The fast build (well under a minute for 7 DoF with about 3.3k task points, Table I) makes per-cell or per-AGV-pose roadmaps conceivable. Our redundancy dimension is small (roll plus cone, and possibly a 7th linear axis).
- Complementary to [[sources/razjigaev2025functional]]. FRIK is a fast but greedy local IK for the free roll; GRR fixes the global branch and consistency choice that FRIK leaves to q0.

## Critical assessment (our view)
- The task spaces tested are position, or position plus a **fixed** orientation, on coarse grids. Our weld task is a 5-D pose (point plus axis direction), with the redundancy in roll and cone tilt. A grid over all reachable torch poses along large steel structures is much bigger. A roadmap restricted to the seam's tube neighbourhood would be more realistic, but the paper does not test that.
- With one configuration per task point, GRR **removes** the null-space freedom MPPI is meant to explore. The authors' own limitation (no secondary objectives) means collisions with the workpiece, joint-limit margins and process quality cannot be traded off once the roadmap exists. Obstacles beyond self-collision are not considered.
- The roadmap is kinematic only: no velocities and no constant travel speed (±10%). The downstream MPC would still have to time-parametrise.
- The seeds come from a hand-made cyclic path per robot. Connectivity is 100% only in obstacle-free tests; for a mobile base that moves along the structure, the roadmap would have to be rebuilt or re-anchored for each base pose.
- Online query cost (ProjectNeighbors plus the continuity check per teleop step) is not reported; only build time is.
- Evidence is simulation only, on non-industrial arms (planar, Kinova). There are no welding or 6-axis industrial results.

## Abstract (verbatim, arXiv)
> Global redundancy resolution (GRR) roadmaps is a novel concept in robotics that facilitates the mapping from task space paths to configuration space paths in a legible, predictable, and repeatable way. Such roadmaps could find widespread utility in applications such as safe teleoperation, consistent path planning, and motion primitives generation. However, previous methods to compute GRR roadmaps often necessitate a lengthy computation time and produce non-smooth paths, limiting their practical efficacy. To address this challenge, we introduce a novel method Expansion-GRR that leverages efficient configuration space projections and enables rapid generation of smooth roadmaps that satisfy the task constraints. Additionally, we propose a simple multi-seed strategy that further enhances the final quality. We conducted experiments in simulation with a 5-link planar manipulator and a Kinova arm. We were able to generate the Expansion-GRR roadmaps up to 2 orders of magnitude faster while achieving higher smoothness. We also demonstrate the utility of the GRR roadmaps in teleoperation tasks where our method outperformed prior methods and reactive IK solvers in terms of success rate and solution quality.

## Links
- [[concepts/path-wise-redundancy-resolution]]
- [[comparisons/welding-mppi-design-review]]
- [[applications/industrial-manipulators]]
- [[concepts/mppi-vs-mpc]]
- Related: [[sources/razjigaev2025functional]], [[sources/yin2024dpbreakpoints]], [[sources/yin2024dprealtime]], [[sources/lee2026prmppi]]
- BibTeX key: `zhong2024expansiongrr` in `latex/references.bib`
