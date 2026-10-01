---
key: farzanehkaloorazi2018pathplacement
title: "Simultaneous path placement and trajectory planning optimization for a redundant coordinated robotic workcell"
authors: "FarzanehKaloorazi, MohammadHadi; Bonev, Ilian A.; Birglen, Lionel"
year: 2018
venue: "Mechanism and Machine Theory, vol. 130, pp. 346-362"
arxiv: 
doi: 10.1016/j.mechmachtheory.2018.08.022
pdf: raw/papers/farzanehkaloorazi2018pathplacement.pdf
text: raw/text/farzanehkaloorazi2018pathplacement.txt
tags: [base-placement, redundancy-resolution, continuous-path, manipulators, industrial]
status: read
---

# Simultaneous path placement and trajectory planning optimization for a redundant coordinated robotic workcell

*FarzanehKaloorazi, MohammadHadi; Bonev, Ilian A.; Birglen, Lionel* (2018). Mechanism and Machine Theory, vol. 130, pp. 346-362.

## TL;DR
Path placement and redundancy resolution for a 13-DoF automated fibre placement cell (6-DoF serial robot + hexapod + rotary table on the hexapod). A PSO searches the placement of the path/rotary table (hexapod pose, used as a tilt-and-torsion table) and, nested inside each particle, a 1-D Newton search per path point chooses the rotary-table angle that maximises the serial robot's distance from singularity (|det J|). The hexapod is static while one branch of the part is wrapped and moves only in a transition phase between branches.

## Method
- **Kinematics** (§2): Fanuc serial robot (DH in Tab. 1, analytic IK); 6-RSS hexapod with analytic IK and numerical FK; its translational workspace is about 1% of the robot's, so it is used for tilt/torsion only, maximum tilt about 12° (Fig. 5–6).
- **Objective** (§4, Eq. 10): maximise Σ_p |det J_p| along the path subject to the serial robot's joint limits; tool always normal to the surface (6-D path given as frames).
- **Nested optimisation** (§5, Alg. 1): outer PSO (Eq. 9, reflection at the workspace limits) over the placement; inner 1-D Newton–Raphson per point for the rotary-table angle, warm-started at the previous point's angle; particles whose det J changes sign between consecutive points (i.e. would cross a singularity / change working mode) get infinite cost; rotary-table speed and direction reversals are limited (fibre breakage).
- **Branch strategy**: one hexapod placement per branch of the Y-shaped part; between branches the hexapod moves while the robot tool stays attached to the transition point.

## Evidence
- Planar 3-point illustration (§4.1): 30 particles, ≤ 20 iterations, ≈ 0.71 s (600 calls); with a stagnation stop ≈ 0.35 s (300 calls) on a 3.5 GHz CPU (Fig. 10).
- Case study (§5.2): helix path of 2795 points on a Y-shaped workpiece (points 1–1399 main branch, junction at 1400; Fig. 11). 20 particles × 10 iterations took about **21 min** (2.3 GHz, 8 GB). Result: near-linear robot trajectory on the main branch, expanding helix on the second branch, transition at point 1617, joint 5 kept in [78°, 128°], away from its singular values (Fig. 14–16); final hexapod at x = 1549 mm from the robot base, with a spacer to mount the rotary table (Fig. 17).
- No collisions modelled (§1.3), no timing law, simulation only.

## Relevance for Plan4ARI
- Structurally close to our setting with an extra axis: a slowly reconfigured placement (hexapod ↔ AGV station) held fixed per path segment (branch ↔ seam segment), plus a continuously interpolated redundant axis (rotary table ↔ our optional linear 7th axis) resolved along the path.
- The "no sign change of det J along the segment" rule is a cheap proxy for "no reconfiguration within a segment" that a station evaluator can reuse.

## Critical assessment (our view)
- Point-wise greedy redundancy resolution (1-D Newton warm-started from the previous point): no look-ahead, no global path optimisation; |det J| as singularity distance is unit- and scale-dependent.
- Orientation is exact (tool normal): no tolerance cone, no free roll exploited; no joint-speed or constant-speed verification; no collisions.
- Metaheuristic (PSO) placement, not repeatable across runs, 21 min for one path; a feasibility demonstration on one part, not a benchmark.
- Still useful as an early example of placement + redundancy co-optimisation per segment, with an explicit transition between segments.

## Links
- [[concepts/base-placement]] · [[concepts/path-wise-redundancy-resolution]] · [[comparisons/welding-mppi-design-review]]
- Related: [[sources/weingartshofer2021tcpbase]], [[sources/weingartshofer2023pathframework]], [[sources/zhao2025bstar]], [[sources/wachter2024baseplacement]], [[sources/yin2024dpbreakpoints]]
- BibTeX key: `farzanehkaloorazi2018pathplacement` in `latex/references.bib`
