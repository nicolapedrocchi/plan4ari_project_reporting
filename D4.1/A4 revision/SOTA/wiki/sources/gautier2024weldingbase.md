---
key: gautier2024weldingbase
title: "Comparison of Robot Morphologies and Base Positioning for Welding Applications"
authors: "Gautier, Nicolas; Guillermit, Yves; Sebsadji, Yazid; Porez, Mathieu; Chablat, Damien"
year: 2024
venue: "Proc. ASME Int. Design Engineering Technical Conf. (IDETC), 48th Mechanisms and Robotics Conference, vol. 7"
arxiv: 2407.05720
doi: 10.1115/DETC2024-143459
pdf: raw/papers/gautier2024weldingbase.pdf
text: raw/text/gautier2024weldingbase.txt
tags: [welding, base-placement, manipulators, industrial, reachability]
status: read
---

# Comparison of Robot Morphologies and Base Positioning for Welding Applications

*Gautier, Nicolas; Guillermit, Yves; Sebsadji, Yazid; Porez, Mathieu; Chablat, Damien* (2024). Proc. ASME Int. Design Engineering Technical Conf. (IDETC), 48th Mechanisms and Robotics Conference, vol. 7.

## TL;DR
Simulation study (Weez-U Welding + LS2N) comparing two 6-axis arm morphologies for teleoperated arc welding: a PUMA-like anthropomorphic arm and a UR-like arm (three parallel axes), each tested on five industrial weld scenarios and on a few hand-picked base poses per scenario. A trajectory is declared feasible if, in ROS2/MoveIt, it is free of collisions (environment and self) and singularities and keeps joint speeds and static torques within actuator limits; all analytical IK branches (postures) are enumerated. The UR-like arm wins 4 of 5 cases (Table 5) but only in few postures; the PUMA-like arm is more posture-robust. Base placement is evaluated, **not optimised** (optimisation is announced as future work).

## Method
- **Weld task definition (§2.1–2.2)**: fixed torch tilt 45°, drag +7° (transition allowed over max 20 cm at corners), stick-out 15 mm; linear and circular seams only; all runs at the most critical manual-welding speed 90 cm/min. Torch-mounted camera adds an orientation constraint (camera aligned with the weld axis, ideally in front of the pool) — i.e. the rotation about the torch axis is **not** free in their setting.
- **Morphologies (§3, Table 1, Fig. 3–4)**: PUMA-like (wrist offset on joint 5, L_arm = 793 mm) vs UR-like (L_arm = 735 mm); segment lengths from an internal reach/torque study; no joint limits; torch mounted at 45° to the last axis.
- **Base poses (§4, Table 2)**: 1–4 candidate base poses per scenario (ground, wall, on pipe, beam), chosen the way an operator would, from space constraints, attachment points, min TCP–base distance and reach; explicitly not optimised.
- **Feasibility pipeline (§5, Fig. 11)**: weld rules → Cartesian path → all analytical IK solutions (8 for PUMA, 2/4/6/8 for UR) → execution in ROS2 + MoveIt (collision margin 0.01 m, singularity margin 6°) → numerically differentiated joint speeds (limits 5 rpm joints 1–3, 10 rpm joints 4–6) and static Newton-Euler torques (limits 65 Nm / 20 Nm; 2 kg hose mass on actuator 3; Table 3). Dynamics neglected (low speed, reduction ~100).
- **Scenario-specific criteria**: max weldable height h/L_arm (Eq. 1), max weldable horizontal length d/(2 L_arm) (Eq. 2), max Cartesian speed keeping all joints below 80% of their limit (Eq. 3), number of feasible sub-trajectories without base relocation (cases 4–5).

## Evidence
- Five scenarios (§4, Fig. 5–9): (1) vertical seam, base on ground; (2) horizontal seam, base on wall; (3) fillet weld around a plate end (4 base poses); (4) pipe-on-plate, 0.3 m diameter tube, 4 arcs, no base change (2 poses); (5) beam T-connection with stiffener, 3 seams (3 poses). Simulation only (ROS2/RViz), no hardware.
- Case 1 (§6.1): UR-like reaches 720 mm (h = 0.98, single posture) vs PUMA-like 560 mm (h = 0.71, four postures); both limited by singularity; PUMA joint 3 peaks at 51.93% of speed limit.
- Case 2 (§6.2): UR-like 1500 mm (d = 1.02, two postures) vs PUMA-like 560 mm (d = 0.76, four postures); torque on motor 1 up to 68.66% (UR) / 57.36% (PUMA) at full extension.
- Case 3 (§6.3): base poses A, B, D infeasible (self-collision or link–workpiece collision, or singularity depending on camera side); in pose C at 90 cm/min UR exceeds joint-2 speed limit by 26.8% (feasible v_max = 57 cm/min), PUMA exceeds joint-1 limit by 106.8% (v_max = 35 cm/min).
- Case 4 (§6.4): pose A — PUMA performs all four arcs with camera kept, one posture each; UR only arcs 1.2/1.4 (arcs 1.1/1.3 collide with the tube). Pose B infeasible for both; raising the base by about 30 cm would make 1.2/1.4 feasible.
- Case 5 (§6.5, Table 4): UR-like does all three seams from pose A; PUMA-like needs a base change (A for seams 1 and 3, B or C for seam 2). Seam 2 needs drag angle ≥ 12° to avoid joint-6 collision with the T-structure. Speeds/torques far from limits.
- Summary (Table 5): UR-like relative performance vs PUMA-like +38, +34, +63, −50, +50% for cases 1–5. No significant difference in average/peak torques and speeds otherwise (§7).
- No computation times reported.

## Relevance for Plan4ARI
- Closest welding-specific reference for **arm morphology and base-pose feasibility** on large structural parts (beams, stiffeners, pipes, plates), i.e. our domain. Its feasibility checklist (collision incl. self-collision, singularity margin, joint-speed and torque limits along the whole seam at constant welding speed) is a directly reusable *station-acceptance test* for each candidate AGV station.
- Case 3 shows that at constant Cartesian speed, corner/contouring segments are where joint-speed limits break: this maps onto our ±10% speed-tolerance requirement and supports segmenting seams upstream at corners or allowing local speed modulation.
- Case 5 quantifies the morphology/base-relocation trade-off (UR-like: one station; PUMA-like: two) — exactly the "minimise reconfigurations" objective of our station planning, and an argument to evaluate morphology together with base placement (and the 7th linear axis) rather than separately.
- The drag-angle result (≥ 12° needed in case 5) is evidence that exploiting orientation tolerance (our ~10° cone) can turn infeasible seams into feasible ones.

## Critical assessment (our view)
- **No optimisation**: base poses are a handful of operator-style guesses (Table 2); the paper is a feasibility comparison, not a base-placement method. Optimisation and robustness/sensitivity of placement are stated as future work (§7).
- **Rigid task**: fixed tilt/drag and camera-aligned roll; the tolerance cone and free roll that we have are not exploited systematically (only the drag-angle remark in case 5). Coverage-style formulations such as [[sources/zhang2023basecoverage]] or reachability maps ([[sources/makhal2018reuleaux]]) are needed to turn this into a search.
- Lightweight cobot-class arms (L_arm < 0.8 m, 65/20 Nm) with custom morphologies, manually mounted; no mobile base, no external axis, no positioning error of the base — all central for an AGV-mounted welder on large steel structures.
- Static torques only; joint speeds by numerical differentiation; single speed (90 cm/min); only linear and circular seams; simulation only, no weld quality.
- Results reported for the best posture only; the per-scenario relative scores of Table 5 mix heterogeneous criteria, so the "4 of 5" headline should not be over-generalised.

## Abstract (verbatim, arXiv)
> This article undertakes a comprehensive examination of two distinct robot morphologies: the PUMA-type arm (Programmable Universal Machine for Assembly) and the UR-type robot (Universal Robots). The primary aim of this comparative analysis is to assess their respective performances within the specialized domain of welding, focusing on predefined industrial application scenarios. These scenarios encompass a range of geometrical components earmarked for welding, along with specified welding paths, spatial constraints, and welding methodologies reflective of real-world scenarios encountered by manual welders. The case studies presented in this research serve as illustrative examples of Weez-U Welding practices, providing insights into the practical implications of employing different robot morphologies. Moreover, this study distinguishes between various base positions for the robot, thereby aiding welders in selecting the optimal base placement aligned with their specific welding objectives. By offering such insights, this research facilitates the selection of the most suitable architecture for this particular range of trajectories, thus optimizing welding efficiency and effectiveness. A departure from conventional methodologies, this study goes beyond merely considering singularities and also delves into the analysis of collisions between the robot and its environment, contingent upon the robot's posture. This holistic approach offers a more nuanced understanding of the challenges and considerations inherent in deploying robotic welding systems, providing valuable insights for practitioners and researchers alike in the field of robotic welding technology.

## Links
- [[concepts/base-placement]]
- [[comparisons/welding-mppi-design-review]]
- [[applications/industrial-manipulators]]
- Related: [[sources/zhang2023basecoverage]], [[sources/makhal2018reuleaux]], [[sources/nguyen2023taskclustering]]
- BibTeX key: `gautier2024weldingbase` in `latex/references.bib`
