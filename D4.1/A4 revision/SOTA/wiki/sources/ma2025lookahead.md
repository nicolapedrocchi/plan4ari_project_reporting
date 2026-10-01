---
key: ma2025lookahead
title: "Real-Time Look-Ahead Trajectory Planning Algorithm Based on Small Line Segment Pose Synchronization"
authors: "Ma, Jianing; Tang, Hao; Guo, Rong; Wu, Chengqian; Bhatti, Uzair Aslam; Tong, Chong Wen"
year: 2025
venue: "2025 10th Asia-Pacific Conference on Intelligent Robot Systems (ACIRS), pp. 312-318"
arxiv: 
doi: 10.1109/acirs66343.2025.11360954
pdf: raw/papers/ma2025lookahead.pdf
text: raw/text/ma2025lookahead.txt
tags: [look-ahead, trajectory-generation, industrial, path-following]
status: read
---

# Real-Time Look-Ahead Trajectory Planning Algorithm Based on Small Line Segment Pose Synchronization

*Ma, Jianing; Tang, Hao; Guo, Rong; Wu, Chengqian; Bhatti, Uzair Aslam; Tong, Chong Wen* (2025). 2025 10th Asia-Pacific Conference on Intelligent Robot Systems (ACIRS), pp. 312-318.

## TL;DR
A CNC-style look-ahead interpolator for 6-D tool paths made of many short linear segments, as in G-code. It has four parts:
- **Corner blending:** each corner is smoothed with a G2 quintic Bézier curve that stays within a corner tolerance.
- **Orientation blending:** orientation is handled the same way. Quaternions are mapped to 3-D points with the logarithm, blended, and **synchronised with position** through auxiliary 1-D "virtual synchronisation" curves.
- **Feed profile:** a seven-segment, jerk-continuous quintic acceleration law.
- **Look-ahead:** a **bidirectional (forward/backward) scan** of curvature-based speed limits, so the tool does not stop at every segment junction.

Validation is simulation only.

## Method
- Corner smoothing (§II-A): a quintic Bézier with six control points is inserted at each junction. G2 continuity holds by construction (Eq. 4). The control-point distances follow from the maximum corner error ε, half the segment length, and a power-law fit that minimises the maximum curvature (Eq. 5–6).
- Interpolation on the curve (§II-B): the Bézier parameter u is advanced with a second-order Taylor step. A quadratic correction of the truncation error makes the step match the commanded length (Eq. 8–18).
- Pose synchronisation (§III): the orientation logarithm is treated as a 3-D point path and blended with a Bézier. Start and end orientation speeds come from length ratios (Eq. 19–20). Two 1-D Bézier synchronisation curves, F(u) and G(u), map position arc length to orientation arc length (Eq. 21–25).
- Feed planning (§IV-A): a seven-segment quintic polynomial profile (Eq. 26), with closed-form phase times from v_max, a_max and j_max.
- Look-ahead (§IV-B): each point gets a speed limit from normal acceleration, jerk and curvature (Eq. 27). A forward scan starts from zero velocity and propagates limits backward when needed. A reverse scan then starts from zero end velocity.

## Evidence
- Test bed: §V describes a "three-axis motion platform" with simulated velocity, acceleration and jerk profiles. There is no robot, no hardware run and no computation time.
- Feed look-ahead test (§V, Figs. 4–5):
  - Path: a five-pointed star plus a semicircle, discretised into **75 linear segments with an average length of 1 mm**.
  - Limits: v = 2.0×10³ mm/s, a = 4.0×10⁴ mm/s², j = 1.8×10⁷ mm/s³.
  - With look-ahead, the velocity drops significantly at only three points. Acceleration and jerk stay continuous (Fig. 5).
- Pose synchronisation versus SLERP:
  - Setup: 6 waypoints (Table I), and an extreme case with more than 60° of orientation change over 0.15 mm (Figs. 6–7).
  - Table II, proposed vs SLERP (units not stated): maximum angular variation 0.6698 vs 1.4791; RMS 0.2644 vs 0.8781; smoothness index 0.7670 vs 0.5050; peak angular acceleration 2.0270 vs 23.2343.
  - The text summarises this as about 55% and 70% lower errors and more than 90% lower peak angular acceleration.

## Relevance for Plan4ARI
- **The industrial baseline.** This paper is representative of **industrial/CNC look-ahead**: geometric corner blending within a tolerance, a bidirectional scan of curvature-limited feed, and a jerk-limited profile. It is a deterministic Cartesian look-ahead with a single solution, and it has **no redundancy, no IK and no joint limits**. "MPPI as a better look-ahead" improves on this baseline by exploring the null space.
- **A cheap speed layer.** The bidirectional scan is the cheapest possible speed layer and a useful reference for the ±10% band. Speed limits induced by curvature and joint rates can be computed along the MPPI path, and the band checked before execution.
- **Pacing the torch orientation.** Synchronising position and orientation along arc length matters for the torch. Orientation changes inside the cone must be paced with travel, not interpolated by SLERP segment by segment.

## Critical assessment (our view)
- **Path deviation.** Corner blending **deviates from the programmed path** by up to ε. When the seam point must be exact, this is only acceptable if ε is within the weld tolerance. It is the opposite philosophy to [[sources/lange2016pathaccurate]], which keeps the path exact and scales time.
- **Weak evidence.** The validation is simulation on a 3-axis platform, the metrics have no units, there are no timings despite the "real-time" claim, and there is no comparison with established look-ahead interpolators. The paper is useful as a description of the standard pipeline, not as a quantitative benchmark.
- **Maximum feed, not constant speed.** The feed is maximised for time efficiency rather than held constant. For welding, the scan must target a constant travel speed with a lower bound (0.9 v_nom), not only an upper limit.

## Links
- [[comparisons/welding-mppi-design-review]]
- [[applications/industrial-manipulators]]
- [[concepts/smoothness-action-parametrization]]
- Related: [[sources/lange2016pathaccurate]], [[sources/yang2024toolpathsmoothing]], [[sources/palleschi2021fastsafe]]
- BibTeX key: `ma2025lookahead` in `latex/references.bib`
