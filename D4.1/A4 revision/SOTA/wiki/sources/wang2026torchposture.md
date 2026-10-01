---
key: wang2026torchposture
title: "Innovation in robot welding trajectory control: Online synchronous planning of welding paths and torch postures for structures with unknown spatial geometries"
authors: "Wang, Hao; Wang, Xiujun; Liu, Chunguo; Chen, Chao; Zhao, Xiaohui"
year: 2026
venue: "Robotics and Computer-Integrated Manufacturing, vol. 101, pp. 103315"
arxiv: 
doi: 10.1016/j.rcim.2026.103315
pdf: raw/papers/wang2026torchposture.pdf
text: raw/text/wang2026torchposture.txt
tags: [welding, orientation-tolerance, manipulators, industrial, perception]
status: read
---

# Innovation in robot welding trajectory control: Online synchronous planning of welding paths and torch postures for structures with unknown spatial geometries

*Wang, Hao; Wang, Xiujun; Liu, Chunguo; Chen, Chao; Zhao, Xiaohui* (2026). Robotics and Computer-Integrated Manufacturing, vol. 101, pp. 103315.

## TL;DR
Sensor-driven generation of the **full 6-DoF welding trajectory** (seam points + torch orientation) for grooved butt and fillet joints of unknown geometry, from a line-laser scan, without CAD or teaching. Most of the paper is perception (camera/light-plane/hand-eye calibration, YOLOv11 ROI detection, laser-centreline extraction, B-spline fitting). The planning part is geometric: on a sliding window of three consecutive laser profiles, tangent planes of base metal and groove faces are fitted; their intersections give groove feature points; the weld point of each layer/pass follows an equal-height/equal-area layout, and the **torch axis is set on the bisector of the groove angle within the groove cross-section plane**, with the tool x-axis in that plane (so roll is fixed by the geometry). On a Yaskawa AR1440 GMAW cell, path RMSE is ≈0.15–0.28 mm (3-D) and orientation RMSE ≈0.5–1.1° per Euler angle; multi-layer multi-pass welds were executed. "Online" means scan-then-plan per joint, not replanning during the weld; no reachability, IK, collision or joint-limit reasoning is involved.

## Method
- **System (§2)**: self-built line-laser sensor (CMOS camera, red laser, narrow-band filter) on a Yaskawa AR1440 with YRC1000 controller, RD350S welder, industrial PC over TCP/IP; C++/Qt software on the Yaskawa SDK. Q235 steel, 80% Ar + 20% CO₂, 1.2 mm wire.
- **Calibration (§3)**: camera calibration with a circular tangential-gradient sub-pixel corner detector (CTGOM) and adaptive PSO refinement; light-plane calibration from back-projected point clouds; sphere-based hand-eye calibration.
- **Joint reconstruction (§4.1)**: YOLOv11 locates and classifies joint ROIs in laser images; iterative context-based centreline extraction (CIICEA); outlier removal with the Pauta (3σ) criterion; K-means-based quasi-uniform cubic B-spline fitting; profiles transformed to base frame and stacked into a point cloud.
- **Trajectory planning by point-cloud geometric differentiation (§4.2)**:
  - sliding window of three consecutive stripes → fitted planes (left/right base metal, left/right groove faces) → groove cross-section plane and feature points (left edge, root, right edge);
  - weld points for each layer/pass obtained by translating the feature points in the cross-section according to groove angle/depth (equal height, equal area);
  - torch axis = bisector of the groove angle at the root; tool x-axis in the cross-section plane and orthogonal to the axis; y completes the frame; converted to roll–pitch–yaw (Eqs. 31–37).

## Evidence
- **Perception**: system 3-D measurement error within ±0.17 mm, mean absolute 0.1111 mm on a calibration block (Table 4). YOLOv11: precision and recall 1.0, mAP@0.5 0.995, 4.7 ms per inference (213 Hz) (Table 5, §4.1.1). CIICEA ≈55.88 ms per frame (≈18 Hz) (§4.1.2).
- **Planning accuracy on known specimens (§4.2.3)**: butt joint (60° groove, 6 mm deep) and fillet joint (40° groove). Per-axis path errors within ±0.35 mm (butt) and ±0.78 mm (fillet); 3-D deviation within ±0.38 / ±0.79 mm (Figs. 29–30). Table 6: 3-D path RMSE 0.1474 mm (butt), 0.2777 mm (fillet). Torch errors within ±2° (butt) and ±2.1° (fillet) (Figs. 32, 34); Table 7: RMSE R_X/R_Y/R_Z 0.9226/0.6226/0.8194° (butt), 1.0771/0.5198/0.8222° (fillet).
- **Welding experiments (§5.1)**: butt (specimen A) and fillet (specimen B) of unknown geometry placed randomly; 4 layers each, travel speed 30 cm/min for all passes, currents ≈120–171 A (Table 8); 20 online-planned paths reported smooth and continuous (Figs. 39–42), sound multi-pass fill (Figs. 43–45).
- **Comparison (§5.2, Tables 10–11)**: against three line-laser pose-estimation works, mean errors reported lower (e.g. R_Y mean 0.5428°, 55–61% below the baselines); the baselines were evaluated on simpler seams in their own papers.
- **Stated limitations (§5.3)**: needs a distinct groove (not applicable to non-grooved joints without modification); stripe extraction degrades under strong ambient light/reflective surfaces; latency grows with point-cloud density and joint complexity (GPU acceleration suggested); no thermal-distortion-aware real-time control.
- Note: the RMSE values quoted in the abstract and conclusion (e.g. 0.0829 mm and 0.1334 mm) do not match the per-axis/3-D values in Table 6; we cite Table 6.

## Relevance for Plan4ARI
- Provides the **upstream reference** for our seam frame: a sensor-derived nominal torch axis (groove bisector) and seam point with sub-millimetre / ~1° accuracy. In our design this is the *centre of the cone* around which the multi-goal MPPI explores roll and tilt ([[comparisons/welding-mppi-design-review]]); the reported ~2° worst-case orientation error is small compared with the ~10° cone, so a perception error budget fits inside the tolerance.
- The bisector rule fixes the work angle; the travel (push/drag) angle and roll are not optimised – precisely the freedoms our planner exploits. The paper therefore motivates the **anisotropic cone**: work angle tied to groove geometry, travel angle and roll free for kinematic reasons.
- Scan-then-plan with sliding windows of three profiles is compatible with receding-horizon planning on the path abscissa s: the scanned look-ahead must cover at least the ~10 cm MPPI horizon.
- Travel speed of 30 cm/min (5 mm/s) in their GMAW experiments is a data point for our horizon-time estimate (flaw #1 of the design review).

## Critical assessment (our view)
- This is a **perception + geometric pose-assignment** paper, not motion planning: the torch pose is uniquely determined per point, with no check of IK feasibility, joint limits, singularities, torch/robot collisions or travel-speed feasibility; failure of reachability on large structures is not addressed.
- Small specimens on a fixed cell; nothing on large structures, mobile bases or reconfiguration.
- Fixed roll from the groove plane could drive the wrist into joint limits on long curved seams – where null-space optimisation such as ours is needed. Pose output as RPY with ±180° wraps (noted by the authors) also shows that downstream planners should work on rotation matrices or quaternions, not Euler angles.
- Timing of the planning step itself is not reported (only perception per-frame times).

## Links
- [[comparisons/welding-mppi-design-review]]
- [[applications/industrial-manipulators]]
- [[concepts/path-wise-redundancy-resolution]]
- Related: [[sources/demaeyer2017descartes]] (tolerance-based torch orientation), [[sources/lu2022toolorientation]], [[sources/zhou2022weldavoidance]], [[sources/demaeyer2021weldbenchmark]], [[sources/tang2023dualrobotweld]]
- BibTeX key: `wang2026torchposture` in `latex/references.bib`
