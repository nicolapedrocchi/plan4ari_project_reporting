---
key: demaeyer2021weldbenchmark
title: "Benchmarking framework for robotic arc welding motion planning"
authors: "De Maeyer, Jeroen; Demeester, Eric"
year: 2021
venue: "Procedia CIRP, vol. 97, pp. 247-252"
arxiv: 
doi: 10.1016/j.procir.2020.05.233
pdf: raw/papers/demaeyer2021weldbenchmark.pdf
text: raw/text/demaeyer2021weldbenchmark.txt
tags: [welding, benchmark, path-planning, manipulators, industrial, orientation-tolerance]
status: read
---

# Benchmarking framework for robotic arc welding motion planning

*De Maeyer, Jeroen; Demeester, Eric* (2021). Procedia CIRP, vol. 97, pp. 247-252.

## TL;DR
ROS-based framework to benchmark **portfolios of planners** on complete arc welding tasks rather than single point-to-point queries. A task is written in an industrial-robot-like specification language (MOVEJ / MOVEP / MOVEL with named poses and constraints such as free torch roll); a simple high-level planner splits it into segments (weld lines = task-space path following, transitions = C-space point-to-point) and dispatches each to a low-level planner through a planner-agnostic ROS service interface; problem, planner settings and results are logged in MongoDB for reproducibility. Metrics: success rate, planning time, C-space path length (L1). Validation on two welding cases (simplified truck part; hard-to-reach seam in a gantry/positioner cell) with OMPL RRTConnect for transitions and the authors' grid-search planner for the welds. It is a framework paper: the results are a demonstration, not a planner comparison.

## Method
- **Motivation (§1–2)**: existing manipulator benchmarks (MoveIt/OMPL benchmarking infrastructure, TrajOpt's PR2 suite, bin-picking studies) target single, short point-to-point queries solved by one planner; no single planner solves a whole welding job (TrajOpt "comes close" but lacks welding-specific end-effector constraints). Weld sequence is assumed fixed (not a TAMP problem); dynamics and time-optimality are out of scope.
- **Architecture (§4, Fig. 1)**: URDF robot + workpiece, MoveIt configuration, task file, planner configuration file → high-level planner → low-level planner services → MongoDB log.
- **Low-level interface (§4.1, App. A)**, three ROS services with no planner-specific settings in the request:
  - free-space point-to-point from a start configuration to a C-space or T-space goal, optionally with goal tolerance (Fig. A.6);
  - T-space path following between start and goal poses of a weld line with optional position/orientation tolerances, assumed valid along the whole segment (Fig. A.7);
  - sampling of valid C-space configurations for a T-space pose (IK + redundant-joint sampling), for planners that do not accept T-space goals (Fig. A.8).
  - Non-ROS planners connect through rosbridge (JSON over WebSocket).
- **High-level planner (§4.2)**: maps commands one-to-one to low-level services; it does not choose the C-space configuration at segment junctions (left to future work, e.g. MoveIt Task Constructor).
- **Task specification (§4.3, Fig. 3)**: variables (CONFIG, POSE, SET-REFERENCE), constraints (e.g. RPY tolerance with 0–360° about the torch axis), commands (MOVEJ home → MOVEP approach → MOVEL weld P1→P2 → MOVEL retract → MOVEJ home).
- **Performance criteria (§4.5)**: success rate (percentage over runs for probabilistic planners); planning time (whole portfolio and per sub-problem); path length = Σ‖q_{i+1} − q_i‖₁ (Eq. 1). Planner-internal statistics (e.g. sampled states) can be logged but are low priority.

## Evidence
- **Benchmark problems (§6)**: Case 1 – simplified model of a small part of a truck rebuilt from primitive shapes (Fig. 4), floor-mounted industrial arm with torch; Case 2 – weld line that is difficult to reach, robot hanging from a gantry above a workpiece on a positioner (Fig. 5). The robot model is not named in the text.
- Planners: OMPL RRTConnect for transitions; a custom grid-search planner (extension of the authors' 2018 sampling-based tube-following work) for weld paths, reported with 100% success.
- **Table 1** (RRTConnect for the in-between motions, 20 runs): Case 1 success 100%, mean planning time 0.21 s, path length 3.79 rad; Case 2 success 80%, 0.92 s, 11.49 rad.
- No hardware specification, no weld-path planning times, no comparison between planners are reported.
- Stated limitations (§7): framework limited by the integrated planners; no way yet to specify the objective function in the task language; better high-level planner needed.

## Relevance for Plan4ARI
- Directly usable as a template for the **D4.1 §10 benchmarking plan** ([[project/prj-d41-outline]], requirements R12–R13): it decomposes a welding job into the same two problem types as our design – seam following under tolerance (multi-goal MPPI) and transfers (VAMP, [[sources/thomason2024vamp]]) – and evaluates the *portfolio*, which is exactly how our MPPI + VAMP + time-scaling stack must be evaluated ([[comparisons/welding-mppi-design-review]]).
- Benchmark elements we can reuse: segment-level service interfaces (point-to-point to C/T-space goal, path following with tolerance, IK sampling); task language with approach/weld/retract structure (maps onto our detach → retract → reconfigure → approach → restart cycle); OMPL RRTConnect as transfer baseline (consistent with the OMPL-baseline requirement of §10); reproducibility logging of planner settings.
- Metrics to **add** for our scenario, absent in the paper: number of detach/reconfigure events per seam, travel-speed deviation vs the ±10% band (time-dilation λ), torch-angle deviation from nominal (work/travel separately), joint-limit and singularity margins, replanning latency per cycle, and total cycle time (planning + execution).
- The custom grid-search weld planner and Descartes ([[sources/demaeyer2017descartes]]) are the natural deterministic baselines for the seam-following track; DP with breakpoints ([[sources/yin2024dpbreakpoints]]) adds the restart-count objective.

## Critical assessment (our view)
- The validation is minimal (two cases, one transfer planner, 20 runs); it shows the framework runs, not which planners work. The truck-part and gantry cases are nonetheless good *shapes* of problems for our benchmark (cluttered, hard-to-reach seams), and a large-structure, AGV-station variant would have to be built by us.
- Fixed weld sequence and fixed robot base: base/station placement ([[sources/gautier2024weldingbase]], [[concepts/base-placement]]) and multi-robot allocation ([[sources/tang2023dualrobotweld]]) are outside its scope.
- Kinematic only: no travel speed, no time-parametrisation – the dimension most critical for our design is missing and must be added as a metric.
- We have not checked whether the code (ROS 1, MongoDB) is still maintained.

## Links
- [[comparisons/welding-mppi-design-review]]
- [[project/prj-d41-outline]]
- [[applications/industrial-manipulators]]
- [[concepts/path-wise-redundancy-resolution]]
- Related: [[sources/demaeyer2017descartes]], [[sources/thomason2024vamp]], [[sources/schulman2014trajopt]], [[sources/zhou2022weldavoidance]], [[sources/tang2023dualrobotweld]], [[sources/wang2026torchposture]]
- BibTeX key: `demaeyer2021weldbenchmark` in `latex/references.bib`
