---
key: zhao2021mobilemachining
title: "Accuracy analysis in mobile robot machining of large-scale workpiece"
authors: "Zhao, Xingwei; Tao, Bo; Han, Shibo; Ding, Han"
year: 2021
venue: "Robotics and Computer-Integrated Manufacturing, vol. 71, pp. 102153"
arxiv: 
doi: 10.1016/j.rcim.2021.102153
pdf: raw/papers/zhao2021mobilemachining.pdf
text: raw/text/zhao2021mobilemachining.txt
tags: [mobile-manipulation, machining, accuracy, industrial, large-structures]
status: read
---

# Accuracy analysis in mobile robot machining of large-scale workpiece

*Zhao, Xingwei; Tao, Bo; Han, Shibo; Ding, Han* (2021). Robotics and Computer-Integrated Manufacturing, vol. 71, pp. 102153.

## TL;DR
System-level accuracy analysis of a mobile manipulator (arm on a mobile platform) grinding a wind-turbine blade at successive stations. A scalar **TCP error index** (distance between TCP and the nominal machining point in the global frame) is decomposed into four calibration terms: workpiece registration from measured points (e1), CAD matching error on free-form surfaces (ed), platform localisation (e2) and arm kinematic/joint error (e3). A 30-camera OptiTrack system localises workpiece and platform once per station; the arm then executes an open-loop trajectory transformed into its base frame. The measured TCP error stays **below 40 mm**, dominated by workpiece registration; it is absorbed by a force-controlled grinding head (force fluctuation within ±2 N), not by the motion planner.

## Method
- Frame chain global → workpiece and global → platform → arm base → tool (Eq. 2); TCP error index e = ‖gl P_tool − gl P_cha‖ (Eq. 3–4), linearised in the transform deviations (Eq. 5–6).
- Error budget E_c = e1 + e2 + e3 + ed (Eq. 13): least-squares registration of the workpiece from feature points (Eq. 7) or ICP against CAD when features are not identifiable (Eq. 8, adds the matching error ed); least-squares platform pose (Eq. 9), optionally constrained to planar motion (Eq. 15); arm error from DH and joint-angle errors via the Jacobian (Eq. 11–12).
- Sensitivity study (§3): Gaussian noise on measured points, 30 measurement groups per noise level.
- Work strategy (Table 1, Fig. 9): offline CAD path → workpiece calibration → drive to station → measure platform/base pose (arm base found by rotating joint 1, Eq. 17) → transform path to base frame (Eq. 18) → machine → next station. The base is static during machining.

## Evidence
- Setup (§2.1, Fig. 1–2): 30-camera OptiTrack covering 7.5 m × 12 m; workpiece = part of a wind-turbine blade (the CAD model in Fig. 4 spans roughly 15 m); arm and platform models are not specified in the text; force-controlled grinding head.
- Simulation (§3): with measurement noise up to 0.02 m, the TCP error grows to roughly 0.04–0.05 m (Fig. 5, read from plot). Platform localisation is the most sensitive term because the marker baseline on the platform is small: without the planar constraint the TCP error reaches ~0.13 m at 0.02 m noise vs ~0.04 m with it (Fig. 6, read from plot).
- Arm error assumptions (§3): link error 3.33% of length and 0.1° joint error, planar simplification; resulting TCP error up to ~0.025 m, increasing towards the workspace boundary (Fig. 7, read from plot).
- Combined budget (Fig. 8): at small noise ed and e3 dominate; at larger noise the measurement error dominates.
- Experiment (§4, Fig. 10–13): three stations, one "S" trajectory per station. The TCP error (grinding-head stroke) grows from station 1 to 3, varies within 10 mm inside stations 2–3 and correlates with arm posture; maximum within 40 mm; directional bias attributed to workpiece calibration. Grinding force within ±2 N.
- No computation times, no repeated trials, no independent ground truth (e.g. laser tracker), no local sensing.

## Relevance for Plan4ARI
- A rare end-to-end accuracy budget for a station-based mobile manipulator on a very large workpiece, i.e. our AGV-welding scenario ([[comparisons/welding-mppi-design-review]], [[applications/mobile-robots-amr]]).
- **Implication for welding without seam tracking:** with global optical localisation and CAD registration only, centimetre-level TCP errors (here up to 40 mm) are reported, and the process survived only thanks to a compliant force-controlled tool. Arc welding has no such mechanical compliance (the admissible seam offset is of the order of the wire/bevel size), so a per-station **local registration of the seam** (touch sensing, laser scan or seam tracking) is a prerequisite. The null-space MPPI must take the corrected seam as input; it cannot absorb a centimetre-level bias.
- The error depends on arm posture and grows near the workspace boundary (Fig. 7, Fig. 13): a posture-dependent accuracy term is a candidate cost for MPPI and for station placement, alongside reachability ([[concepts/base-placement]]).
- The station workflow (Table 1) matches our assumption "AGV to station, base static, weld a portion".

## Critical assessment (our view)
- The error budget is additive and largely qualitative; numbers in §3 come from synthetic noise with assumed magnitudes (e.g. a 3.33% link error is unrealistically large for a calibrated industrial arm), so they do not transfer as a quantitative budget.
- The 40 mm figure mixes workpiece registration error with arm/platform errors and is measured indirectly through the grinding-head stroke.
- The planner is open-loop per station: no redundancy, no path optimisation, no re-registration within a station. Useful as a pessimistic baseline and as motivation for local sensing, not as a reusable method.

## Links
- [[comparisons/welding-mppi-design-review]] · [[concepts/base-placement]] · [[applications/mobile-robots-amr]] · [[applications/industrial-manipulators]]
- Same group: [[sources/yang2024toolpathsmoothing]], [[sources/peng2026ringwelding]]
- BibTeX key: `zhao2021mobilemachining` in `latex/references.bib`
