---
key: bai2024toolpath7dof
title: "Tool Path Optimization for 7-DOF Robot Machining Based on Sampling Motion Planning Algorithm"
authors: "Bai, Haijun; Bi, Guangde; Zhang, Zhentao; Lei, Guoqin; Lu, Lei; Sun, Lining"
year: 2024
venue: "2024 6th International Symposium on Robotics &amp;amp; Intelligent Manufacturing Technology (ISRIMT), pp. 124-127"
arxiv: 
doi: 10.1109/isrimt63979.2024.10875295
pdf: raw/papers/bai2024toolpath7dof.pdf
text: raw/text/bai2024toolpath7dof.txt
tags: [path-planning, redundancy-resolution, external-axis, machining, manipulators, industrial]
status: read
---

# Tool Path Optimization for 7-DOF Robot Machining Based on Sampling Motion Planning Algorithm

*Bai, Haijun; Bi, Guangde; Zhang, Zhentao; Lei, Guoqin; Lu, Lei; Sun, Lining* (2024). 2024 6th International Symposium on Robotics &amp;amp; Intelligent Manufacturing Technology (ISRIMT), pp. 124-127.

## TL;DR
A 6-axis robot plus a rotary worktable (7 DoF) machines a spiral path: tool tip constrained to the curve (equality), tool-axis angles (b, c) bounded to intervals (inequality); the joint path minimising the total travel of all 7 axes is found with **PRM\*** from OMPL. Optimised tool orientation plus the turntable reduces total joint travel by 12.4% versus a fixed-orientation 7-DoF baseline.

## Method
- Kinematics (§II-A, Eq. 1–2): turntable rotation r composed with the robot chain; IK obtained by fixing r and solving the 6-axis IK.
- Constraints (§III, Eq. 4–8): tool tip on curve C(k); tool-axis angles b, c bounded so that the cutting force stays in the spindle's high-stiffness region (Fig. 2).
- Objective (Eq. 3): sum of the total travel of each joint including r, as a proxy for machining time.
- Planner: PRM\* (OMPL) producing "hundreds" of discrete joint-space path states (§IV); a final variant adds weights on start/end joint angles.

## Evidence
- Simulation; robot model not named; spiral of radius 50 mm, k from 0 to 4π (Eq. 9, Table I); b in [0.2618, 1.047] rad, c in [0, 1.571] rad (Eq. 10–11).
- Table III, total joint travel: fixed-attitude 7-DoF 7.141 rad; variable-attitude 6-DoF 7.6789 rad; variable-attitude 7-DoF 6.7675 rad; weighted variable-attitude 7-DoF 6.25525 rad (−12.4% vs fixed attitude, §V).
- No computation times, no collision-scene details, no hardware experiment.

## Relevance for Plan4ARI
- Same problem structure as our seam: tool point exact + tool axis inside an admissible region + one extra axis (here a turntable, for us a rail), solved with an off-the-shelf sampling planner.
- Supports optimising the extra axis jointly with the arm rather than on a fixed schedule: for the linear 7th axis, rail motion should be planned together with the arm within a station.

## Critical assessment (our view)
- Very short paper; how PRM\* handles an equality-constrained path (sampling, connection rule, monotone path progress) is not described, so the method is not reproducible.
- Joint travel is a weak proxy for time; no velocity/acceleration limits, no constant feed, no IK branch handling.
- One spiral, one 12.4% figure, no runtime: weak evidence; useful mainly as an example formulation.

## Links
- [[concepts/path-wise-redundancy-resolution]]
- [[applications/industrial-manipulators]]
- [[comparisons/welding-mppi-design-review]]
- Related: [[sources/sun2020externalaxis]] (external axes, graph search), [[sources/weingartshofer2023pathframework]], [[sources/lu2022toolorientation]]
- BibTeX key: `bai2024toolpath7dof` in `latex/references.bib`
