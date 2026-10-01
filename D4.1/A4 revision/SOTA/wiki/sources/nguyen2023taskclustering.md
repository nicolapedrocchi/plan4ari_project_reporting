---
key: nguyen2023taskclustering
title: "Task-Space Clustering for Mobile Manipulator Task Sequencing"
authors: "Nguyen, Quang-Nam; Adrian, Nicholas; Pham, Quang-Cuong"
year: 2023
venue: "Proc. IEEE Int. Conf. Robotics and Automation (ICRA), pp. 3693-3699"
arxiv: 2305.17345
doi: 10.1109/ICRA48891.2023.10161293
pdf: raw/papers/nguyen2023taskclustering.pdf
text: raw/text/nguyen2023taskclustering.txt
tags: [base-placement, mobile-manipulation, set-cover, reachability, manipulators, industrial]
status: read
---

# Task-Space Clustering for Mobile Manipulator Task Sequencing

*Nguyen, Quang-Nam; Adrian, Nicholas; Pham, Quang-Cuong* (2023). Proc. IEEE Int. Conf. Robotics and Automation (ICRA), pp. 3693-3699.

## TL;DR
Two-step solution of the mobile-manipulator Robotic Task Sequencing Problem (RTSP): (1) **task-space clustering**, which partitions hundreds of 5-D targets (position + tool axis, roll free) into the *minimum* number of clusters, each reachable from one base pose, by casting it as a **uniform-cost Set Cover Problem (SCP)** on a bipartite graph targets ↔ discretised floor points built from an offline reachability analysis; (2) **sequencing** with a modified RoboTSP (TSP on base poses, TSP on targets, graph search over IK solutions). Minimising the number of base placements is given priority over arm motion because base relocation brings larger localisation error. Demonstrated on a 336-hole mobile drilling task (4 base poses, 100 s planning).

## Method
- **Targets** t_i = (x, y, z, θ, φ): position plus polar/azimuthal angles of the tool axis; rotation about the tool axis is treated as irrelevant (set as a tuning parameter) (§III-A, Eq. 1). **Floor** discretised into a grid F of candidate base positions, base yaw free (Eq. 2).
- **Offline reachability database** (§IV-A): voxelise the space around the robot and keep voxels where IK exists for *all* sampled polar angles (N_sam = 10 values in [110°, 150°] in the test case; azimuth sampled at 0). Joint 1 is restricted to [−90°, 90°] for the database (hardware ±170°); the residual joint-1 range gives a reachable azimuth width per base pose Δφ_max = 2(j1_lim − j1_res) (Eq. 5), i.e. the arm, not the base, rotates the reachable region.
- **Geometric reachable region** (Eq. 6–7): a simple conservative shape fitted inside the valid-voxel cloud, made of two horizontal planes (Z_min, Z_max), one vertical safety plane (x′ ≥ X_min) and two concentric spheres (R_min, R_max) centred near the second joint (Fig. 3). Test-case values are listed in §IV-A.
- **Bigraph by inversion** (§IV-B, Eq. 8): for each target, the set of floor points from which it is reachable is an analytic 2-D region (annulus ∩ half-plane after rotating by φ_i), so the bigraph is built in n fast iterations instead of n × m IK calls or per-target inverse-reachability voxel matching.
- **Cluster assignment** (§IV-C): solve the uniform-cost SCP (NP-complete) with near-optimal heuristics; chosen sets whose azimuth span (Eq. 9) exceeds Δφ_max are split; base yaw is set to the middle of the cluster's azimuth range (Fig. 4).
- **Sequencing** (§V): 2-Opt TSP over base poses; TSP over all targets with clusters virtually separated by a distance h (Eq. 11) to respect the base order; layered IK graph search for the shortest configuration path (RoboTSP); RRT-Connect + post-processing for collision-free trajectories.

## Evidence
- **Robot**: DENSO VS-087 6-DOF arm on a Clearpath Ridgeback 3-DOF omnidirectional base; planning in OpenRAVE; CPU AMD Ryzen 9, Ubuntu 18.04 (§VI).
- **Real drilling experiment** (§VI-A, Fig. 1, 5): 336 targets on both sides of a 1 m workpiece (polar 110–150°, azimuth −37…37° front / 168…192° back); LRg solver, 0.10 m floor grid, 0.05 m voxels → **4 clusters / 4 base poses**, sequence and collision-free trajectories in **100 s**; total motion time 414 s.
- **SCP solvers benchmarked** (§VI-B, Fig. 6, wider azimuth range): Greedy, LP relaxation + rounding (LPr), Lagrangian relaxation + greedy (LRg, SetCoverPy). LRg found the best solution (fewest clusters) in most cases, with longer but acceptable time; finer floor grids give fewer clusters at higher clustering time. Fig. 7: trajectory planning dominates the total planning time and clustering is a small fraction (read from the plot only).
- **Offline database cost** (Table I): voxel size 0.04 / 0.05 / 0.07 / 0.10 m → 74004 / 40204 / 15902 / 6332 voxels, 1765.2 / 943.5 / 366.6 / 126.1 s.
- **Comparison** (Table II, 264 one-sided targets, φ = 0): base poses 2 vs 8 (RoboTSP + sphere clustering) vs 70 (Cluster-RTSP); planning time 49.7 vs 51.8 vs 368.1 s; motion time 225.4 vs 265.0 vs 323.5 s.
- **Code**: no repository given in the paper (only a video link); the SCP solver reuses the existing SetCoverPy algorithm.
- **Authors' future work**: base moving in 3-D (gantry systems) and clustering for **continuous tasks** such as 3-D printing (§VII).

## Relevance for Plan4ARI
- Closest formal match to our "minimise the number of AGV stations" requirement: stations = chosen floor points of an SCP whose universe is the set of weld targets. Replacing drilling holes with weld-seam samples gives an immediate baseline formulation for [[concepts/base-placement]].
- The 5-D target model with free roll and a polar-angle range matches our task (torch axis within a ~10° cone, roll free): the cone can be folded into the "IK for all sampled orientations" condition of the reachability database (conservative, stricter test).
- The joint-1 trick (restricting the database range so that the arm, not the base, rotates the region) is a cheap way to make station placement yaw-free; analogously, an interpolated 7th linear axis could be used to enlarge each station's reachable region before solving the SCP.
- The two-step decomposition (stations first, sequencing after) fits a pipeline where seams are segmented upstream and the motion planner executes per station ([[comparisons/welding-mppi-design-review]]).

## Critical assessment (our view)
- **Point targets, not continuous seams**: covering a point does not imply that a whole seam segment is executable from the same station *without reconfiguration* and at constant speed. For welding, the SCP elements should be seam segments with a feasibility test along the segment (same IK branch, joint-limit/velocity margins); the paper does not address this and lists continuous tasks as future work.
- The geometric reachable region is a conservative, partly hand-tuned inner approximation (limit planes chosen manually, Step 1 in §IV-A); it ignores arm–workpiece and base–workpiece collisions at the chosen floor points, and base localisation error is used as motivation but not modelled as a reachability margin.
- Flat 2-D floor grid only; reaching high/deep zones of large steel structures may require a vertical or linear extra axis, which changes the reachable shape (3-D base motion is future work).
- Uniform cost (cardinality only): no weighting of station quality (manipulability, distance to joint limits, cycle time) or AGV travel; a weighted SCP would be a natural extension.
- Small comparison (one task family, two baselines adapted by the authors) and no released code.

## Abstract (verbatim, arXiv)
> Mobile manipulators have gained attention for the potential in performing large-scale tasks which are beyond the reach of fixed-base manipulators. The Robotic Task Sequencing Problem for mobile manipulators often requires optimizing the motion sequence of the robot to visit multiple targets while reducing the number of base placements. A two-step approach to this problem is clustering the task-space into clusters of targets before sequencing the robot motion. In this paper, we propose a task-space clustering method which formulates the clustering step as a Set Cover Problem using bipartite graph and reachability analysis, then solves it to obtain the minimum number of target clusters with corresponding base placements. We demonstrated the practical usage of our method in a mobile drilling experiment containing hundreds of targets. Multiple simulations were conducted to benchmark the algorithm and also showed that our proposed method found, in practical time, better solutions than the existing state-of-the-art methods.

## Links
- [[concepts/base-placement]]
- [[applications/mobile-robots-amr]]
- [[applications/industrial-manipulators]]
- [[comparisons/welding-mppi-design-review]]
- Related: [[sources/makhal2018reuleaux]] (reachability / inverse reachability maps), [[sources/gautier2024weldingbase]], [[sources/zhang2023basecoverage]]
- BibTeX key: `nguyen2023taskclustering` in `latex/references.bib`
