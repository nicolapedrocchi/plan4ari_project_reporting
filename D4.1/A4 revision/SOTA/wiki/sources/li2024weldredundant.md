---
key: li2024weldredundant
title: "An effective path planning approach for robot welding considering redundant kinematics"
authors: "Li, Guangxi; Ren, Zhizhen; Yue, Wei; Liu, Haitao"
year: 2024
venue: "Precision Engineering, vol. 91, pp. 462-475"
arxiv: 
doi: 10.1016/j.precisioneng.2024.10.008
pdf: raw/papers/li2024weldredundant.pdf
text: raw/text/li2024weldredundant.txt
tags: [welding, redundancy-resolution, path-planning, industrial, machining]
status: read
---

# An effective path planning approach for robot welding considering redundant kinematics

*Li, Guangxi; Ren, Zhizhen; Yue, Wei; Liu, Haitao* (2024). Precision Engineering, vol. 91, pp. 462-475.

## TL;DR
Offline, CNC-style path planner for a **friction stir welding (FSW)** cell: a 5-DoF hybrid robot (TriMule: 3-DoF parallel mechanism plus A/C swing head) combined with a **1-DoF movable worktable**, which is the "redundant axis". The five-axis toolpath (tool-tip position plus tool axis) is smoothed at the corners to G3 continuity with quintic B-splines whose control points are built in closed form, under explicit position and orientation error bounds. The orientation arc length and the redundant-axis value are then written as C3-continuous functions of the position arc length, so a jerk-continuous feedrate can drive all axes in sync. **This paper does not optimise the redundant-axis values.** They come from the authors' earlier posture optimisation based on stiffness and singularity (their Ref. [32]); here they are only smoothed and synchronised.

## Method
- **Redundancy used**: one continuous external axis, the worktable translation x_r (Eq. 2: q = invk(p − x_r, o)). The tool pose is fully prescribed as a five-axis path (position plus axis vector).
  - There is **no orientation tolerance** (no tilt cone) and no tool roll: the FSW spindle is axisymmetric and the robot has 5 DoF.
  - No IK branches are considered: for a given x_r, the IK of the hybrid robot is treated as unique.
- **Choice of x_r**: one discrete value per cutter-location (CL) point, taken from prior work and chosen for stiffness and singularity avoidance (§2, §4.4 Step 3, Fig. 18). The stated motivation is that higher stiffness reduces the loss of plunge depth under welding forces.
- **Toolpath preprocessing** (§3.1, Eq. 12; §3.2, Eq. 21): before smoothing, CL points are shifted within the error tolerance to lower the curvature peaks of the inserted corner splines.
- **Corner smoothing** (§3): a quintic B-spline at each corner, with control points in closed form from the G3 conditions.
  - Position spline in Cartesian space: fixed ratio c_p = 7/16 and a segment-length rule (Eq. 11).
  - Orientation spline built in R³ and normalised onto the unit sphere: c_o = 0.16, with a 1-D search on the smoothing angle to meet the orientation error bound (Eq. 20).
- **Synchronisation, orientation path (TOP) to position path (TPP)** (§4.2): the orientation arc length s_o(s) is a piecewise quintic B-spline through the arc-length pairs at the junctions.
  - Monotonicity and C0–C3 continuity are linear constraints (Eqs. 25–27).
  - The objective is the integral of the squared third derivative (Eq. 28).
  - It is solved with MATLAB fmincon, starting from a constructed feasible initial guess (Eq. 29).
- **Synchronisation, x_r to TPP** (§4.3): piecewise 5th-degree polynomials x_r(s) through the given x_r values, with C0–C3 continuity constraints (Eq. 33) and minimum squared jerk in s (Eq. 32). It is solved with the MATLAB Optimization Toolbox.
- **Timing**: a jerk-continuous feedrate profile is scheduled afterwards, with S-shaped acc/dec at start and end and the velocity, acceleration and jerk of the redundant axis (Eq. 34) as constraints (§4.4 Step 6).
  - Execution uses PVT commands with a 10 ms interpolation period (§5.3).
  - Speed is constant along the path apart from the start and stop ramps. The authors leave time-optimal feedrate scheduling to future work (§5.3).

## Evidence
- **Platform**: TriMule-800 FSW hybrid robotised equipment, mounted vertically on a frame, with the 1-DoF worktable, an NC system and a hydraulic station (§2, Fig. 1). Simulations were run in MATLAB (§5).
- **§5.1, S-shaped path** (tolerances 0.02 mm and 0.004°), with vs without preprocessing:
  - Average position smoothing error 0.017 mm, 11.3× the value without preprocessing, i.e. better use of the allowed tolerance.
  - Curvature peak 0.135 mm⁻¹, 43% lower (Fig. 11).
- **§5.2, five-axis test path** from Tulsyan & Altintas (tolerances 0.1 mm and 0.01°, robot configuration ignored), compared with Liu's C3 method:
  - TPP curvature peak lower, e.g. 0.531 → 0.366 mm⁻¹ at P1 (−31%). TOP curvature maximum 228 → 134 (−41%) (Fig. 14).
  - At a constant 20 mm/s feedrate: peak tool-axis angular acceleration 2.43 → 0.38 and peak jerk 235.7 → 8.15. Units are as printed in the paper (Fig. 15); §6 reports these as −84% and more than −95%.
- **§5.3, spatial weld path** (51 CL points, tolerances 0.1 mm and 0.001°, feedrate 40 mm/min). Results are qualitative only:
  - Smoothing errors stay within tolerance (Fig. 16).
  - s_o(s) is monotone and C3 (Fig. 17).
  - x_r(s) is smooth up to the third derivative (Figs. 18–19).
  - Joint and worktable trajectories are smooth (Fig. 20).
- **§5.4, experiment**:
  - Setup: AA2024-T4 plate 5.5 mm thick, H13 tapered pin tool with a 15 mm shoulder, 1000 rpm, 0.3 mm plunge, 40 mm/min; a weld takes about 750 s.
  - Comparison on the same workpiece: worktable fixed at zero vs worktable moving along the planned x_r path.
  - Result: the weld with the moving axis shows moderate flash, the one with the fixed axis almost none. The authors read this as less loss of plunge depth thanks to higher stiffness (Fig. 21b).
  - The comparison is visual only: no measurement of force, plunge depth or weld quality.
- **No computation times** are reported for any step, and there is no comparison with other redundancy-resolution methods.

## Relevance for Plan4ARI
- **External axis as redundancy.** The paper is a welding-specific example of this case in [[comparisons/welding-mppi-design-review]] (our interpolated 7th linear axis). It shows the industrial CNC practice: fix the external-axis profile offline and make it C3 in path arc length, so the feedrate stays smooth and constant.
- **Reference for downstream smoothing and synchronisation.** Any null-space profile chosen by MPPI (roll, cone offsets, rail position) must become a smooth function of s before time-scaling. The paper gives a ready recipe: arc-length synchronisation with jerk-minimising splines and monotonicity constraints. Its redundant-axis derivative constraints in the feedrate scheduler play the role of our downstream speed MPC.
- **Parametrisation on s.** It supports our choice of parametrising on the path coordinate s rather than on time ([[concepts/path-wise-redundancy-resolution]]).
- **Not a baseline for the redundancy decision.** x_r is supplied by another method, and the paper searches over no branches, tolerances or reconfigurations. For that decision, [[sources/yin2024dpbreakpoints]], [[sources/gao2022taskredundancy]], [[sources/chen2025cooptimization]] and [[sources/demaeyer2017descartes]] are closer.

## Critical assessment (our view)
- **Scope mismatch.** The paper covers FSW with a stiff hybrid robot at 40 mm/min, not arc welding of large steel structures with a serial 6-axis arm. Its machining-style formulation (exact tool axis, tolerances of hundredths of a mm and thousandths of a degree) has no equivalent for our ~10° cone and free roll.
- **Fully offline and open-loop.** Planning runs in MATLAB with no reported run times, and there is no seam tracking, replanning or reaction to deviations. In our design the same smoothing would have to run incrementally on the receding horizon.
- **Redundancy is smoothed, not resolved.** The objective is pure smoothness (jerk in s); stiffness and singularity enter only through the precomputed x_r points. Joint limits, collisions, IK branches and the feasibility of constant speed are not addressed, so reconfigurations (detach, reconfigure, restart) never arise in the paper.
- **Constant speed.** It is assumed by construction: constant feedrate with start and stop ramps. Nothing checks or holds a ±10% band when the redundant axis or the joints saturate, and the authors themselves leave time-optimal feedrate scheduling to future work.
- **Weak evidence.** The experimental benefit rests on one visual comparison (flash appearance) against a fixed worktable, with no quantitative weld-quality metric. The smoothing gains are shown against a single prior method (Liu, from the same group).
- **Closest prior work.** For robot machining with a redundant axis this is [[sources/yang2024toolpathsmoothing]] (their Ref. [31]); the authors extend it with G3 continuity and B-spline orientation synchronisation.

## Links
- [[applications/robotic-welding]]
- [[concepts/path-wise-redundancy-resolution]]
- [[comparisons/welding-mppi-design-review]]
- Related: [[sources/yang2024toolpathsmoothing]], [[sources/yin2024dpbreakpoints]], [[sources/gao2022taskredundancy]], [[sources/chen2025cooptimization]], [[sources/demaeyer2017descartes]]
- BibTeX key: `li2024weldredundant` in `latex/references.bib`
