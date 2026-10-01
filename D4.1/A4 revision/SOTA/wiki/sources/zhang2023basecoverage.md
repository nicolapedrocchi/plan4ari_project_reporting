---
key: zhang2023basecoverage
title: "Base Placement Optimization for Coverage Mobile Manipulation Tasks"
authors: "Zhang, Huiwen; Mi, Kai; Zhang, Zhijun"
year: 2023
venue: "arXiv preprint arXiv:2304.08246"
arxiv: 2304.08246
doi: 
pdf: raw/papers/zhang2023basecoverage.pdf
text: raw/text/zhang2023basecoverage.txt
tags: [base-placement, coverage, mobile-manipulation, reachability]
status: read
---

# Base Placement Optimization for Coverage Mobile Manipulation Tasks

*Zhang, Huiwen; Mi, Kai; Zhang, Zhijun* (2023). arXiv preprint arXiv:2304.08246.

## TL;DR
Base placement optimisation (BPO) for a mobile manipulator that must **cover a surface from several stops**. The target surface is discretised into Scale-Like Discs (SLDs: centre, normal, radius), which decouples the task (a soft, non-deterministic family of trajectories) from the base pose. An offline voxel-hashed reachability map (RM) returns, for each SLD, the collision-free configuration with best manipulability within the approach-direction cluster closest to the disc normal. The set of base placements (number and poses) is optimised with NSGA-II over three objectives: coverage, total time (per-stop TSP over reachable SLDs + navigation time) and manipulability. Validated on a public-toilet washbasin cleaning task (simulation + real differential-drive base with lift and 6-DoF cobot).

## Method
- **Problem (§III-A)**: find base poses z_i = (x, y, θ) whose workspaces cover the task set; metrics: coverage, minimal time (number and sequence of stops), manipulability, collision safety.
- **SLD representation (§III-B, Fig. 2)**: surface approximated by discs (r, p, n); reachability is evaluated per disc, independently of the specific coverage path.
- **Offline RM (§III-C)**: workspace voxelised (resolution δ); joint space uniformly discretised; for each configuration store end-effector position, approach vector, manipulability and occupied voxels in a hash map keyed by voxel index. Query for an SLD: transform to base frame → voxel lookup → K-means clustering of stored configurations by angular distance to the disc normal → pick the cluster closest to the normal → choose the max-manipulability collision-free configuration (collision check via stored occupied voxels).
- **Objectives**: f1 coverage = fraction of SLDs reachable from at least one stop (Eq. 1); f2 time = Σ TSP length over reachable SLDs / end-effector speed + (m−1)·navigation time (Eq. 2, TSP by dynamic programming); f3 = summed Yoshikawa-type manipulability (based on det(J Jᵀ)) of the selected configurations (Eq. 3).
- **Optimisation (§III-D, Eq. 4)**: NSGA-II, chromosome = list of candidate-BP indices with 0 = "no stop", so the number of stops m is optimised too; candidate set pre-filtered to favoured base placements (FBPs) by reach range and 2D polygon collision check; duplicates and too-close stops avoided. Final optional local base-placement search (fine-tuning) around the BPO solution for the concrete paths.

## Evidence
- Setup (Table I, §IV-A): reconstructed toilet; 3.3 m × 1.5 m candidate area at (0.05 m, 0.05 m, 90°) → 3213 candidate BPs, 1840 FBPs after filtering; washbasin approximated by 200 SLDs of radius 0.04 m; RM voxel 0.03 m, 20 samples per joint → 172063 valid poses; NSGA-II population 40, 80 generations, mutation probability 0.6, 2/3/4 genes; arm Cartesian speed 0.1 m/s, base speed 0.2 m/s.
- Simulation (Fig. 3): with 3 stops, ≈90% coverage after 10 generations, final mean coverage > 95%, best 98.5%. More stops → higher coverage and manipulability but longer time; 3 vs 4 stops give very similar coverage, so > 3 stops brings little benefit. Some 2-stop Pareto solutions reach 95% coverage in less time; a 2-stop solution with 97.5% coverage is chosen (Fig. 4).
- Real robot (§IV-B, Fig. 5–6): differential-drive base + lift + 6-DoF collaborative arm, Nvidia Xavier; after each stop the base pose is re-estimated from RGB-D and the 12 cleaning paths (6 per side) are updated. Path coverage 87% (left) and 93% (right); with local fine-tuning of the base pose, 100% on both sides.
- No computation times are reported (neither RM construction nor NSGA-II runtime).

## Relevance for Plan4ARI
- Methodological template for our **station (raw-positioning) planning**: replace SLDs by seam samples (point + torch-axis cone), the RM query by a welding-feasibility query (point exact, axis within ~10°, roll free), and keep the multi-objective set-cover formulation where the number of stations is a decision variable — directly matching "minimise reconfigurations".
- The "flexible / non-deterministic task constraints" motivation (soft orientation, many valid IK solutions) is the same situation as our tolerance cone + free roll; clustering stored configurations by angle to a nominal direction is a cheap way to exploit the cone.
- The time objective (in-station work + inter-station travel) and the explicit fine-tuning step after AGV relocalisation correspond to our raw-positioning error followed by local correction, and to the 7th-axis option (which would enlarge each station's reachable set).

## Critical assessment (our view)
- **Point-wise reachability, not path feasibility**: a disc counts as covered if one configuration reaches it; continuity of a seam, constant speed (±10%), joint-speed limits and configuration changes along the path are not evaluated — the main gap for welding, where a seam must be executed continuously from one station (cf. the corner speed violations in [[sources/gautier2024weldingbase]]).
- Base pose is planar (x, y, θ) with 90° yaw resolution; the lift height and any extra axis are not optimised; no robustness to base-positioning error in the optimisation (it is recovered a posteriori by fine-tuning).
- Single small task (one washbasin, 200 discs, ≤ 4 stops); scalability to very large structures with thousands of seam samples and many stations is not shown; NSGA-II gives no optimality guarantee beyond the discretisation, and runtimes are missing.
- Assignment of paths to stops is manual (authors' stated limitation; automatic partitioning and learning-based online reachability are future work).
- arXiv preprint only (not peer reviewed at time of reading); the real-robot evaluation reports a single execution, without repetitions or statistics.

## Abstract (verbatim, arXiv)
> Base placement optimization (BPO) is a fundamental capability for mobile manipulation and has been researched for decades. However, it is still very challenging for some reasons. First, compared with humans, current robots are extremely inflexible, and therefore have higher requirements on the accuracy of base placements (BPs). Second, the BP and task constraints are coupled with each other. The optimal BP depends on the task constraints, and in BP will affect task constraints in turn. More tricky is that some task constraints are flexible and non-deterministic. Third, except for fulfilling tasks, some other performance metrics such as optimal energy consumption and minimal execution time need to be considered, which makes the BPO problem even more complicated. In this paper, a Scale-like disc (SLD) representation of the workspace is used to decouple task constraints and BPs. To evaluate reachability and return optimal working pose over SLDs, a reachability map (RM) is constructed offline. In order to optimize the objectives of coverage, manipulability, and time cost simultaneously, this paper formulates the BPO as a multi-objective optimization problem (MOOP). Among them, the time optimal objective is modeled as a traveling salesman problem (TSP), which is more in line with the actual situation. The evolutionary method is used to solve the MOOP. Besides, to ensure the validity and optimality of the solution, collision detection is performed on the candidate BPs, and solutions from BPO are further fine-tuned according to the specific given task. Finally, the proposed method is used to solve a real-world toilet coverage cleaning task. Experiments show that the optimized BPs can significantly improve the coverage and efficiency of the task.

## Links
- [[concepts/base-placement]]
- [[applications/mobile-robots-amr]]
- [[comparisons/welding-mppi-design-review]]
- Related: [[sources/gautier2024weldingbase]], [[sources/makhal2018reuleaux]], [[sources/nguyen2023taskclustering]]
- BibTeX key: `zhang2023basecoverage` in `latex/references.bib`
