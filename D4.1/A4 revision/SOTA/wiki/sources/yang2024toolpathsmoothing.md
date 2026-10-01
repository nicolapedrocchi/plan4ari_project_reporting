---
key: yang2024toolpathsmoothing
title: "An analytical tool path smoothing algorithm for robotic machining with the consideration of redundant kinematics"
authors: "Yang, Jixiang; Qi, Qi; Adili, Abulikemu; Ding, Han"
year: 2024
venue: "Robotics and Computer-Integrated Manufacturing, vol. 89, pp. 102768"
arxiv: 
doi: 10.1016/j.rcim.2024.102768
pdf: raw/papers/yang2024toolpathsmoothing.pdf
text: raw/text/yang2024toolpathsmoothing.txt
tags: [machining, redundancy-resolution, path-planning, industrial]
status: read
---

# An analytical tool path smoothing algorithm for robotic machining with the consideration of redundant kinematics

*Yang, Jixiang; Qi, Qi; Adili, Abulikemu; Ding, Han* (2024). Robotics and Computer-Integrated Manufacturing, vol. 89, pp. 102768.

## TL;DR
Offline smoothing of 5-axis CAM tool paths (position + tool axis) for a 6-DoF arm, treating the rotation about the tool axis (z-y-z Euler angle γ) as functional redundancy. Position and tool axis are fitted with C2 quintic Pythagorean-Hodograph (PH) splines (analytic arc length); γ is fitted as a quintic polynomial spline in the tool-tip arc length s minimising ∫(d²γ/ds²)² (a QP); all three are synchronised to s; a minimum-time feed planner under joint velocity/acceleration/jerk limits produces the timing. On a UR10 the cycle time drops by 33.97% and the peak joint acceleration by up to 65.05% versus a C2 γ-spline without the acceleration objective, with unchanged end-effector error.

## Method
- Kinematics (§2): CL data [P, O] from CAM; tool orientation via z-y-z Euler angles (α, β) computed from O (Eq. 5–6); γ does not change O but changes the joint configuration → 1-D functional redundancy.
- Initial γ_i at each CL point from a tangential frame (y axis = O × path direction), following the authors' earlier work (§2, Ref. [37]). **The γ values at the points are fixed; only the interpolation between them is optimised.**
- Position: C2 quintic PH spline, quaternion coefficients from a Newton-like method (Eq. 7–16); analytic arc length s(u), inverted by Newton–Raphson.
- Orientation: planar PH spline in (α, β) Euler space (Eq. 17–22); ω(s) by polynomial fitting.
- Redundant angle: piecewise quintic γ(s) through the γ_i, with C2 continuity and zero end derivatives as linear equality constraints and minimum integrated squared second derivative (Eq. 23–36), solved with MATLAB fmincon.
- Feed planning (§3.5, Eq. 40–41): minimum-time s(t) under joint position/velocity/acceleration/jerk limits, solved with SQP; joint commands by IK of [P(u(s)), Θ(ω(s)), γ(s)].

## Evidence
- Platform (§4, Fig. 9, Table 1): UR10 with 3 kg load; MATLAB 2020 on Windows 11; interpolation period 0.008 s; Cartesian limits 25 mm/s, 2000 mm/s², 10000 mm/s³; joint limits 120/180 °/s, 2000 °/s², 10000 °/s³.
- Test path (Fig. 10–11): a small free-form path (~300 mm arc length, Fig. 17b) with strongly oscillating tool orientation and γ.
- Computation: spline construction + arc length 74.8 ms vs 240.1 ms for a B-spline method (§4).
- Efficiency (Fig. 12): mean feed 14.337 vs 9.467 mm/s; cycle time 17.648 s vs 26.728 s (−33.97%); baseline = C2 γ-spline without the acceleration objective.
- Smoothness (Fig. 14): peak joint acceleration reduced on joints 1–3 and 6 (e.g. joint 2: 196.3 → 68.6 °/s², the reported −65.05%); joint 4 unchanged (104.0 → 105.3 °/s²); joint 5 increases (271.2 → 313.8 °/s²).
- Accuracy (Fig. 15–17): joint tracking-error peaks similar or lower (joint 6: 0.403° → 0.366°); end-effector tracking and contour errors of the same order for both methods (below ~0.5 mm, read from Fig. 17).

## Relevance for Plan4ARI
- Direct analogue of our welding task: a 5-D task (point + tool axis) on a 6-axis arm, with the free roll about the torch axis as the redundancy to be smoothed ([[concepts/path-wise-redundancy-resolution]], [[comparisons/welding-mppi-design-review]]).
- Two take-aways for the MPPI design: (i) parametrise the null-space coordinate (roll) as a **smooth function of the path abscissa s** and penalise d²γ/ds², which is exactly the "parametrise on s with few spline knots" mitigation of the design review ([[concepts/smoothness-action-parametrization]]); (ii) keep the geometric path q(s) separate from the timing s(t) (path–velocity decomposition), consistent with our downstream speed layer ([[sources/faroni2020scaling]], [[sources/palleschi2021fastsafe]]).
- Can serve as a cheap deterministic baseline or warm start for a null-space MPPI on a fixed IK branch.

## Critical assessment (our view)
- The redundancy is not really optimised: the γ_i are fixed by a geometric rule and only interpolated; joint limits, singularities, collisions and IK-branch changes are not considered. On long seams this cannot prevent the reconfigurations that drive our design.
- Only the 1-D roll redundancy; tolerance cones on the tool axis are not exploited.
- The feed is **minimum-time, not constant** (Fig. 12 shows the feed dropping almost to zero repeatedly). For welding at constant travel speed ±10% the objective must become "feasible at nominal speed", where the smoothness of γ(s) directly decides whether the speed band is reachable.
- Single short test path, one baseline (the same method without the objective), no repetitions; 74.8 ms is for the whole path in MATLAB, not per control cycle.

## Links
- [[concepts/path-wise-redundancy-resolution]] · [[concepts/smoothness-action-parametrization]] · [[comparisons/welding-mppi-design-review]] · [[applications/industrial-manipulators]]
- Related: [[sources/razjigaev2025functional]], [[sources/yin2024dpbreakpoints]], [[sources/faroni2020scaling]], [[sources/palleschi2021fastsafe]]
- Same group: [[sources/zhao2021mobilemachining]], [[sources/peng2026ringwelding]]
- BibTeX key: `yang2024toolpathsmoothing` in `latex/references.bib`
