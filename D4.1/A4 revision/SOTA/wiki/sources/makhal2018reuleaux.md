---
key: makhal2018reuleaux
title: "Reuleaux: Robot Base Placement by Reachability Analysis"
authors: "Makhal, Abhijit; Goins, Alex K."
year: 2018
venue: "Proc. IEEE Int. Conf. Robotic Computing (IRC), pp. 137-142"
arxiv: 1710.01328
doi: 10.1109/IRC.2018.00028
pdf: raw/papers/makhal2018reuleaux.pdf
text: raw/text/makhal2018reuleaux.txt
tags: [base-placement, reachability, software, mobile-manipulation, manipulators]
status: read
---

# Reuleaux: Robot Base Placement by Reachability Analysis

*Makhal, Abhijit; Goins, Alex K.* (2018). Proc. IEEE Int. Conf. Robotic Computing (IRC), pp. 137-142.

## TL;DR
**Reuleaux** is an open-source ROS/C++ library (ROS-Industrial, Google Summer of Code) that (i) builds a voxel/sphere **reachability map** of any URDF arm with a reachability index D = share of sampled poses per sphere that are reachable, (ii) inverts it into an **inverse reachability map (IRM)**, and (iii) transforms the IRM by a set of user task poses into a **union map** scored by a "placebase index", from which n candidate base poses are extracted, either *floating* (6-D, arm only) or *on the ground* (planar x, y, yaw for a mobile robot). Validated on several arms, a simulated PR2 and a real Fetch; once the map exists (offline), base poses for a handful of point tasks are found in seconds.

## Method
- **Reachability map** (§III, Alg. 1): octree voxelisation of the workspace from the URDF; sphere centres colliding with the robot body are filtered *before* IK (FCL), which is the main source of speed-up; each sphere surface is sampled uniformly with frames whose z-axis points to the centre (Fig. 2); IK via IKFast (KDL fallback); self-collision checked per pose. Reachability index D = (R/N)·100 (Eq. 1).
- **Inverse reachability map** (§IV): invert every reachable TCP pose (Eq. 2–3) and re-cluster the inverted poses into spheres by nearest neighbour; score by a normalised placebase index (Eq. 5).
- **Union map** (Alg. 2, Eq. 4): each task pose transforms the IRM into candidate base poses B_ij = task_i · T_j⁻¹; spheres accumulate candidates from all tasks.
- **Floating base** (§V-A): among the m best spheres, candidates are built by (a) PCA of the poses in a sphere (orientation kept parallel to the floor, z-rotation only), (b) *GraspReachabilityScore* (number of task poses reached), or (c) *IkSolutionScore* (total number of IK solutions, up to 8 per pose); the top n are kept.
- **Base on the ground** (§V-B, Alg. 3, Eq. 6): add the arm-base→robot-base transform, slice the union map at floor level (6-D → planar x, y, yaw), sample yaw uniformly per sphere, discard bases that do not reach all task poses, keep the n best.
- Several base locations can be requested (Fig. 5: 2 bases for 3 poses, Husky + UR5), but selection is top-n scoring, not a coverage/cardinality optimisation.

## Evidence
- **Map generation** (Table I; 0.08 m voxels, 1 m maximum radius, IKFast): Reuleaux 124.31 / 160.41 / 143.27 min for PR2 / LWR / UR5, versus 490.07 / 427.11 / 371.38 min and 405.47 / 542.18 / 413.23 min for the two re-implemented prior approaches (Diankov/OpenRAVE and Zacharias et al.). Poses processed (×10^5): 20.938 / 13.718 / 7.636 for Reuleaux. Without collision checking, average generation time is about 156 s (§VI).
- **Floating-base placement**, table task (Table II): with 2 / 4 task poses, PCA reaches 10/10 and 20/20 solutions, score 97.28 / 93.45, time 1.45 / 2.11 s; GraspReachability 9/10, 17/20 (score 89.7 / 85.1, 1.77 / 2.64 s); IKsolution 10/10, 19/20 (96.52 / 96.27, 1.82 / 2.79 s).
- **Comparison with Vahrenkamp et al. and human users** (Table IV, scores by IkSolutionScore): Reuleaux 97.28 / 93.45 vs Vahrenkamp et al. 89.7 / 81.17 and users between 79.23 and 97.4, all within about 1.5–3.2 s. Reporting caveat: the Reuleaux row coincides with the PCA row of Table II, the three user rows are all labelled "User1", and the reference numbers of the two baselines in Table I are swapped relative to the bibliography.
- **Mobile robots** (Table III, 4 runs each): simulated PR2 in the Fraunhofer IPA kitchen reached 4/6, 6/6, 6/6, 5/6 task poses, base calculation 18.2–21.8 s; real Fetch reached 3/3, 2/3, 1/3, 3/3, base calculation 8.23–9.23 s. Failures attributed to motion-planning collisions (obstacles not considered in placement) and depth-sensor noise in task-pose definition (§VI).
- Robots shown: KUKA KR6/KR10, UR5, Motoman MH5, LWR, JACO, PR2, Husky + UR5, Fetch.
- **Open source**: self-contained C++ ROS library, http://wiki.ros.org/reuleaux (ROS 1 era).
- **Authors' stated limitations** (§VII): task-pose input from noisy depth sensors; no collision with workpiece/environment in base placement; reachability alone ignores energy and joint-motion cost.

## Relevance for Plan4ARI
- Canonical reference and tooling for **reachability / inverse reachability maps** in base placement ([[concepts/base-placement]], [[tools/software-ecosystem]]): for the AGV-mounted welding arm, the IRM transformed by sampled weld poses and sliced at floor level directly yields a planar (x, y, yaw) candidate map per seam segment for raw AGV positioning.
- The union map can provide the "which station reaches which seam samples" relation that a set-cover station selector such as [[sources/nguyen2023taskclustering]] needs; Reuleaux itself only ranks bases and does not minimise the number of stations.
- A 7th linear axis could be handled by building the map for the rail + arm chain, or by extending the floor slice to an (x, y, yaw, rail position) grid.

## Critical assessment (our view)
- **Point tasks only**: trajectories must be sampled into poses by the user (declared out of scope, §VI); no guarantee of continuity, of a single IK branch or of absence of reconfiguration along a seam, which is key for welding.
- **Orientation tolerance not modelled**: task poses are exact 6-D frames; our torch-in-cone / roll-free task would need several frames per weld point (or a 5-D map), multiplying the union-map size.
- No collisions with workpiece/environment at placement time, no localisation-error margin, no manipulability or joint-limit distance in the score (only reach/IK counts); top-n selection does not optimise the number of stations or the coverage.
- Small-scale evaluation (2–6 task poses, table/kitchen), weak reporting (duplicated rows, mislabelled users) and ROS 1 code base that may need porting. Good building block and baseline, not a complete station-planning method for large steel structures.

## Abstract (verbatim, arXiv)
> Before beginning any robot task, users must position the robot's base, a task that now depends entirely on user intuition. While slight perturbation is tolerable for robots with moveable bases, correcting the problem is imperative for fixed-base robots if some essential task sections are out of reach. For mobile manipulation robots, it is necessary to decide on a specific base position before beginning manipulation tasks. This paper presents Reuleaux, an open source library for robot reachability analyses and base placement. It reduces the amount of extra repositioning and removes the manual work of identifying potential base locations. Based on the reachability map, base placement locations of a whole robot or only the arm can be efficiently determined. This can be applied to both statically mounted robots, where position of the robot and work piece ensure the maximum amount of work performed, and to mobile robots, where the maximum amount of workable area can be reached. Solutions are not limited only to vertically constrained placement, since complicated robotics tasks require the base to be placed at unique poses based on task demand. All Reuleaux library methods were tested on different robots of different specifications and evaluated for tasks in simulation and real world environment. Evaluation results indicate that Reuleaux had significantly improved performance than prior existing methods in terms of time-efficiency and range of applicability.

## Links
- [[concepts/base-placement]]
- [[tools/software-ecosystem]]
- [[applications/mobile-robots-amr]]
- [[applications/industrial-manipulators]]
- [[comparisons/welding-mppi-design-review]]
- Related: [[sources/nguyen2023taskclustering]] (set-cover station selection), [[sources/gautier2024weldingbase]], [[sources/zhang2023basecoverage]]
- BibTeX key: `makhal2018reuleaux` in `latex/references.bib`
