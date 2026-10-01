---
key: demaeyer2017descartes
title: "Cartesian path planning for arc welding robots: Evaluation of the descartes algorithm"
authors: "De Maeyer, Jeroen; Moyaers, Bart; Demeester, Eric"
year: 2017
venue: "2017 22nd IEEE International Conference on Emerging Technologies and Factory Automation (ETFA), pp. 1-8"
arxiv: 
doi: 10.1109/etfa.2017.8247616
pdf: raw/papers/demaeyer2017descartes.pdf
text: raw/text/demaeyer2017descartes.txt
tags: [welding, path-planning, redundancy-resolution, orientation-tolerance, manipulators, industrial]
status: read
---

# Cartesian path planning for arc welding robots: Evaluation of the descartes algorithm

*De Maeyer, Jeroen; Moyaers, Bart; Demeester, Eric* (2017). 2017 22nd IEEE International Conference on Emerging Technologies and Factory Automation (ETFA), pp. 1-8.

## TL;DR
First written description and independent evaluation of **ROS-Industrial Descartes**, the de-facto open-source planner for semi-constrained Cartesian paths (welding, painting, grinding). Descartes samples each path point inside a per-axis pose tolerance, solves all IK branches, builds a layered graph (nodes = joint solutions, edges between consecutive points) and runs Dijkstra on an L1 joint-motion edge cost. On a KUKA KR5 arc welding model the paper shows that it is **globally optimal only for the discretised problem**, but scales badly in memory, ignores acceleration limits, does not check collisions between consecutive points, treats every pose inside the tolerance as equally good, and handles wrist singularities only implicitly. A node cost penalising deviation from the nominal torch tilt angles (weighted, so one tilt angle can be preferred over the other) is proposed and keeps the torch at nominal orientation unless deviation is needed.

## Method
- **Problem (§II)**: N Cartesian points; find joint vectors satisfying FK at each point. Redundancy comes from free torch roll, tolerances on tilt angles and multiple IK branches (arm up/down). Evaluation criteria: computation time, memory, correctness (collisions, joint limits), behaviour near singularities. Dynamics not considered.
- **Descartes pipeline (§III, Fig. 2)**, reconstructed from ROS-I slides and source code because no formal publication existed:
  1. *Phase 1*: every trajectory point (Cartesian or joint) can carry a tolerance on each pose parameter (position or xyz Euler angle **in the base frame**); the tolerance range is sampled uniformly at a user resolution and each sample goes through IK (all branches). An "axial-symmetric point" type gives free rotation about one axis. Points carry no speed, only an upper bound on the travel time between points (TimingConstraint).
  2. *Phase 2*: collision-free joint solutions become nodes; edges connect **all** node pairs of consecutive points, pruned only if the joint displacement exceeds velocity limit × allowed time; edge cost = L1 norm of the joint difference (Eq. 4).
  3. *Phase 3*: Dijkstra (Boost) on the layered graph.
  - A *sparse* variant plans on a subset of points, interpolates joints in between, checks the Cartesian error with FK and adds points / replans when the error is too large.
- **Improved cost (§V)**: node cost η|α − α_ee| + |β_p − β_ee| on the two tilt Euler angles, roll ignored, η prioritising one tilt over the other (Eq. 9); implemented by adding it to all incoming edges so that standard Dijkstra still applies.

## Evidence
- Robot: KUKA KR5 arc model (Figs. 4–5); wire feeder and cables not modelled; collision checking added from the ROS-I Godel project. Laptop i7-6820HQ, 16 GB RAM.
- Tasks: A "cylinder on a plane" (±π about the torch axis, Fig. 6); B "L-profile with obstacle" (±10° about the path axis to avoid a small plate, Fig. 7); C L-profile in another placement that drives the wrist through a singularity (Fig. 12).
- **Computation time (§IV, task B, 50 points)**, KDL numerical IK (20 seeds per point) vs IKFast analytic IK: phase 1 731.1 s vs 1.4 s; phase 2 8.6 s vs 0.8 s; phase 3 1.6 s vs 0.2 s. KDL returns more, partly near-duplicate, solutions and inflates the graph; IKFast is limited to ≤ 6 DOF (a rail-mounted robot would need an adapted solver).
- **Memory**: nodes ≈ 2NM, edges ≈ (N−1)(2M)² (Eqs. 5–6; factor 2 from robot configurations). With only torch-axis tolerance (360° at 1°) and 30 points: 2.16·10⁴ nodes, 1.50·10⁷ edges, about 1 GB of RAM. Tolerances on further axes quickly become unmanageable. Sparse planner on task B (50 points, π/4 about the path, π/20 about the torch axis): 9 points planned, 41 interpolated; it started from 6 points and had to add one three times (memory in Fig. 9).
- **Correctness**: with tolerance only about the path x-axis in task B the obstacle cannot be avoided, yet Descartes still returns a plan in which the torch **jumps from one end of the tolerance range to the other** across the obstacle, because nothing is checked between consecutive points (Figs. 10–11). Acceleration limits are not considered.
- **Singularities**: the L1 cost implicitly avoids them in general, but in task C joint 5 approaches zero and joints 4 and 6 grow large in opposite directions (Fig. 13, around 22 s).
- **Improved cost**: the default planner keeps a constant 0.4 rad deviation about the path y-axis in task B; with Eq. 9 the deviation is zero except where collision avoidance requires it (Fig. 14); joints 4/6 still show brisk changes (Fig. 15).
- Authors' future work (§VI): tighter coupling of graph search, IK and tolerances; tolerances in the local path frame; dynamics in the cost.

## Relevance for Plan4ARI
- Descartes is the **industrial open-source baseline** for our exact problem class (exact seam point, tilt tolerance, free roll, IK branches). It should appear as a baseline in D4.1 §10 ([[project/prj-d41-outline]]) next to DP with breakpoints ([[sources/yin2024dpbreakpoints]]); see [[concepts/path-wise-redundancy-resolution]] and flaw #24 in [[comparisons/welding-mppi-design-review]].
- Its documented failures map onto requirements for the multi-goal MPPI look-ahead:
  - *Memory blow-up* with multi-axis tolerances: our null space (roll + 2-D cone, plus the rail if present) is 3–4-D, so a dense Descartes graph over long seams is not affordable; sampling only the null space in MPPI avoids enumerating it.
  - *Jumps inside the tolerance and no inter-point collision check*: rollouts need an orientation-rate cost and interpolated collision checking (flaw #12).
  - *No acceleration limits, no travel speed*: the ±10% speed constraint and the downstream time-scaling layer have no counterpart in Descartes; speed feasibility (time-dilation λ) must be evaluated on each rollout.
  - *Indifference within the tolerance*: our cost should prefer the nominal work/travel angles; the weighted tilt cost of Eq. 9 is a direct template for the **anisotropic cone**.
  - *Base-frame Euler tolerances*: the cone should be defined in the local seam frame, as the authors themselves suggest.
- Descartes keeps all IK branches in one graph (a branch switch is "free" if the joint step passes the velocity check), whereas our design treats a branch change as an explicit detach/reconfigure/restart event; this must be made explicit when comparing.

## Critical assessment (our view)
- The evaluation is qualitative: three tasks, one robot, results mostly as figures, no success-rate statistics. Timings are for the 2017 Descartes with KDL/IKFast and say nothing about later ROS-I tools (Descartes Light, Tesseract), which we have not checked.
- As a global graph search on a discretised segment, Descartes (or an equivalent layered-graph DP) is a useful **offline oracle** to measure how far a 10 cm receding-horizon MPPI is from the segment optimum (the "restarts vs horizon" experiment in the design review).
- Not addressed: reconfiguration/restart events, constant travel speed, online replanning, AGV/rail coupling (beyond a remark on IKFast for rails).

## Links
- [[comparisons/welding-mppi-design-review]]
- [[concepts/path-wise-redundancy-resolution]]
- [[applications/industrial-manipulators]]
- [[project/prj-d41-outline]]
- Related: [[sources/demaeyer2021weldbenchmark]] (same group, benchmark framework), [[sources/yin2024dpbreakpoints]], [[sources/wang2026torchposture]], [[sources/zhou2022weldavoidance]], [[sources/tang2023dualrobotweld]]
- BibTeX key: `demaeyer2017descartes` in `latex/references.bib`
