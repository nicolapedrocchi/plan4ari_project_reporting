---
key: peng2026ringwelding
title: "Research on Welding-obstacle Avoidance Collaborative Path Planning Method for Ring-welding Robot of Main Arch Segment of Large-Span Arch Bridge"
authors: "Peng, Shuangqian; Cui, Xiaolu; Zhou, Jianting; Zhang, Hong; Huang, Bo"
year: 2026
venue: "SSRN preprint (not peer reviewed)"
arxiv: 
doi: 10.2139/ssrn.6636646
pdf: raw/papers/peng2026ringwelding.pdf
text: raw/text/peng2026ringwelding.txt
tags: [welding, path-planning, large-structures, industrial]
status: read
---

# Research on Welding-obstacle Avoidance Collaborative Path Planning Method for Ring-welding Robot of Main Arch Segment of Large-Span Arch Bridge

*Peng, Shuangqian; Cui, Xiaolu; Zhou, Jianting; Zhang, Hong; Huang, Bo* (2026). SSRN preprint (not peer reviewed).

## TL;DR
**SSRN preprint, not peer reviewed.** Path planning for a dedicated rail-guided "ring-welding" robot that welds the circumferential joint between tubular main-arch segments of long-span arch bridges. A circumferential carriage on a flexible rail fixed next to the seam is joint 1, followed by four arm joints and a torch-rotation joint (6 DoF in total). A nominal ring path with prescribed torch angles is adapted to the arch-axis geometry by an offset model, then locally corrected near temporary connecting rib plates by geometric rules (torch tilt in the cross-section plane; fixture link lengths from a planar 3-link model in the axial plane), and the crossings of the plates are bridged by CHOMP. "Collaborative" here means **coordinating the welding objective with the obstacle-avoidance objective**, not multi-robot cooperation. Validation is on a scaled rig with a coating device that simulates welding.

## Method
- Modelling (§2.1–2.3): arch segment and rib plates as non-uniform-density sphere point clouds (denser at the seam); robot decomposed with V-HACD into convex parts, enveloped by capsules and discretised into spheres (Fig. 4–5). Kinematics: standard DH with a diameter-dependent first link (D_a + 117 mm, Table 1); IK by Levenberg–Marquardt plus a fixed torch-fixture transform. Offset model between rail centre and weld path for parabolic arch axes (Eq. 6–7).
- Nominal ring path (§3.1, Fig. 9): weld-progress angle α from 0 to π on both sides; torch angles β (along the arch axis) and θ (in the cross-section, gravity-related); discrete control points.
- Cross-section ("horizontal") plane (§3.2.1, Fig. 11–13): rule-based six-phase sequence near each rib plate: approach at nominal θ, increase θ by a tangent-circle construction around the obstacle corner, stop welding and cross the obstacle, reverse tangency, wall-guided sliding back to nominal θ, resume. Thresholds L_sd and L_sc define the safety distances (Eq. 8).
- Axial ("vertical") plane (§3.2.2, Fig. 14): robot projected to a planar 3-link chain (joints 2, 3, 5); closed-form joint angles clearing three rectangular plates, from which the two fixture link lengths are derived, i.e. partly a **fixture design** step.
- Obstacle crossing (§3.3, Fig. 15): CHOMP in joint space with SDF/EDT distances on the sphere model, smoothness + weighted collision cost; the resulting segments are inserted between weld segments.

## Evidence
- Case study (§4.1): arch segment of 1200 mm diameter, three rectangular rib plates; β fixed at 0°, 10° tilt against gravity; first-link length 717 mm.
- Simulation results (§4.1, Fig. 17–19): torch inclination kept between −7.156° and 28.075° (within the ±30° GMAW range cited); torch–plate distance held at the preset 20 mm; fixture links 255.48 mm and 230.00 mm; maximum joint step between control points 2.516° (joint 1) and 2.032° (joint 2).
- Experiment (§4.2, Fig. 20–21): scaled test rig, laser displacement sensor and a coating device instead of a real arc; simulated travel speed 5 mm/s; maximum joint jerk 3.0392 rad/s³; maximum end-effector deviation 0.835 mm radial and 0.360 mm axial, reported as meeting Class E of GB/T 19804-2005; uniform coating bead; obstacle crossing executed as stop → tilt → lift → reset → restart.
- Inconsistency: the abstract and conclusion (3) report a 35 mm minimum clearance, §4 reports 20 mm.
- No computation times, no comparison with other planners, a single geometry.

## Relevance for Plan4ARI
- The only work in our set on robotic welding of **bridge-scale** steel structures with in-process obstacle avoidance. It documents the same pattern as our design review: the weld is **interrupted at an obstacle, the torch is retracted, a transfer motion is planned and welding restarts** ([[comparisons/welding-mppi-design-review]], flaws 4, 14, 16).
- Their split "rule-based torch-angle adjustment within a tolerance band + optimisation-based planner (CHOMP) for transfers" mirrors our "null-space MPPI inside the cone + VAMP for transfers" ([[sources/thomason2024vamp]], [[sources/zucker2013chomp]]). The reported inclination band (~35° span) supports treating torch orientation as a tolerance set rather than a fixed pose.
- The robot is clamped to a rail fixed on the workpiece, so localisation is mechanical; the sub-mm deviation is a **rail-on-workpiece** figure and does not transfer to an AGV-mounted arm (contrast [[sources/zhao2021mobilemachining]]).

## Critical assessment (our view)
- Preprint quality: inconsistent clearance numbers, imprecise notation; the "sub-millimetre accuracy" comes from a scaled rig with a coating device, not real arc welding.
- Planning is geometric and hand-crafted for one obstacle type (rectangular plates) on a near-cylindrical segment; no general redundancy resolution, no IK-branch handling, no travel-speed constraint beyond a jerk check, no re-planning.
- The "6-DoF" count includes the rail carriage, so the arm itself has limited redundancy; the axial-plane step fixes fixture geometry offline rather than exploiting the null space online.
- Useful as an application reference and as evidence that restart-around-obstacle is accepted practice in bridge welding; not as a reusable algorithm.

## Links
- [[comparisons/welding-mppi-design-review]] · [[applications/industrial-manipulators]] · [[concepts/path-wise-redundancy-resolution]]
- Related: [[sources/zucker2013chomp]], [[sources/thomason2024vamp]], [[sources/gautier2024weldingbase]]
- Same group: [[sources/zhao2021mobilemachining]], [[sources/yang2024toolpathsmoothing]]
- BibTeX key: `peng2026ringwelding` in `latex/references.bib`
