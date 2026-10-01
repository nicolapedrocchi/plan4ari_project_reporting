---
key: zhou2025parallelmppi
title: "Parallel MPPI With Gradient-Velocity Modulated SDF Cost for High-Performance Real-Time Dynamic Obstacle Avoidance by Robot Manipulators"
authors: "Zhou, Lelai; Li, Zhengmao; Li, Yibin; Bai, Shaoping"
year: 2025
venue: "IEEE Transactions on Robotics, vol. 41, pp. 5149-5168"
arxiv: 
doi: 10.1109/tro.2025.3600125
pdf: raw/papers/zhou2025parallelmppi.pdf
text: raw/text/zhou2025parallelmppi.txt
tags: [mppi-core, manipulators, safety, hri, multimodality, gpu]
status: read
---

# Parallel MPPI With Gradient-Velocity Modulated SDF Cost for High-Performance Real-Time Dynamic Obstacle Avoidance by Robot Manipulators

*Zhou, Lelai; Li, Zhengmao; Li, Yibin; Bai, Shaoping* (2025). IEEE Transactions on Robotics, vol. 41, pp. 5149-5168.

## TL;DR
**PMPPI** runs several MPPI planners with different cost "strategies" (greedy goal-seeking vs obstacle-sensitive) in one shared sampling pass, scores each planner's top-K rollouts with a common **Judge cost**, converts these scores into MPQ-style soft values and **blends the planners' Gaussian means/covariances** with softmax weights (GMR-like collapse to one Gaussian). It adds a **gradient-velocity modulated SDF cost** (GVM-SDF) that lowers the collision cost when a key point moves along the SDF gradient (away from obstacles) and raises it when moving towards them, plus a TRAC-IK joint-goal cost and a sparse-reward term. On a Franka with point-cloud SDF, GPU/PyTorch, ~32 ms per iteration; real control at 27.8 Hz, EE speed 0.523 m/s mean, 1.225 m/s max.

## Method
- Base MPPI with per-step means/covariances and smoothing step sizes (Eqs. 1–4), samples **joint accelerations**, integrated to q, q̇ commands sent to a PD torque loop (§III).
- PMPPI (§IV, Alg. 1): each planner n samples M rollouts from its own Gaussian, plus samples from the global mixed Gaussian; all rollouts evaluated with S sub-costs in parallel; each planner updates its own distribution; selects top-K rollouts with planner-internal softmax weights (β, Eq. 15); Judge strategy computes value V⁽ⁿ⁾ (log-sum-exp, Eq. 16); planner weights w⁽ⁿ⁾ = softmax(−V/α) (Eq. 11); mixed mean/covariance updated as weighted combination (Eq. 10); first mean sent to actuators. Theoretical motivation from MME-DDP, MPQ and GMR in Appendix A.
- GVM-SDF (§V-A, Eq. 25): SDF from voxelised point cloud, inflation-layer potential Φ (Eq. 21), finite-difference gradient (Eq. 22), robot as spheres; cost Σ_links Φ + Φ·‖v‖·(1 − ρ cos θ), θ angle between key-point velocity and SDF gradient. Compared with Coll_p (RAMP: potential only → rushes through) and Coll_pv (STOMP: potential × speed → stalls near obstacles).
- TRAC-IK in a separate process gives a joint-space target q_des for joint-goal cost (Eq. 26), Cartesian fallback (Eq. 27); sparse reward 1 − exp(−d²/2ξ²) (Eq. 28); STORM-style joint-limit, stop and self-collision costs.

## Evidence
- Simulation (§VI): 2-D point mass (360 rollouts, H = 20, top-K = 20, α = λ = 1, β = 0.8) and 7-DoF Franka in Isaac Gym (**580 rollouts, H = 30**, 80 per planner), moving cylinder obstacles at 0.269 m/s.
- Table II (Franka Task 3): PMPPI 0 collisions, 0 % crash rate, avg EE speed 0.416 m/s vs greedy MPPI 108 collisions / 87.5 %; GVM-SDF MPPI 4.75 / 3.333 %; Coll_pv MPPI fails (local minima). Task 4: PMPPI 3.5 collisions, 8.75 % crash.
- vs STORM with voxel collision (Table III): STORM 168.5 / 80 % crash (Task 3), 251.25 / 93.75 % (Task 4) vs PMPPI 0 / 0 % and 3.5 / 8.75 %.
- vs NEO (QP reactive, Table V, §VI-D): at 0.269 m/s obstacle speed crash rate 45 % (NEO) vs 3.75 % (PMPPI); at 0.359 m/s 50 % vs 10 %.
- Compute (Table VI, RTX 3060 + 8-core Ryzen 7 5800H): planning time **32.25 ± 0.12 ms/iter** (PMPPI) vs 31.852 ms (MPPI-Coll_ppvθ) vs 31.82 ms (STORM); GPU usage ~67–71 %.
- Real Franka (§VII, Table VII): Azure Kinect point cloud filtered at 30 Hz; planning 0.041 s/iter (PMPPI) vs 0.038 s (MPPI); dynamic obstacle scene crash rate 10 % vs 30 % (MPPI-Coll_ppvθ), lap time 7.381 s vs 8.397 s; MoveIt RRT-Connect/CHOMP with 1 Hz Octomap as offline-style baselines. Sudden-obstacle test: 27.8 Hz control, peak joint speed 1.77 rad/s, EE speed 0.523 m/s mean / 1.225 m/s max, 3 collisions in 20 laps (Fig. 14). Pick-and-place with GraspNet and human interference: 5/5 objects.
- Stated limits (§VIII-B): single-camera occlusion, jagged sampling trajectories (EE path +8.3 % vs RRT-Connect in the static free scene), no obstacle motion prediction.

## Relevance for Plan4ARI
- Recent T-RO reference point for **manipulator MPPI rates on GPU**: ~30–40 ms per iteration with 580 rollouts × 30 steps for a 7-DoF arm incl. SDF lookup; useful to size our budget ([[applications/industrial-manipulators]]).
- **Multi-strategy MPPI** is close to our multi-goal scheme, but PMPPI **blends** the planners' means; this is acceptable when all planners live in the same joint-space mode, and is exactly what we must *not* do across IK branches (select-never-blend, [[comparisons/welding-mppi-design-review]], [[concepts/multimodality]]). The **Judge cost** idea — one common evaluation for candidates generated with different internal costs — is directly reusable to compare our ≤ 8 goal modes at equal progress s_end.
- The IK-guided joint goal (TRAC-IK in a parallel process) parallels our exact IK seeding per branch.
- GVM-SDF is a cheap, direction-aware clearance cost that could replace a pure distance penalty for the torch/arm vs structure, and for humans in shared cells ([[applications/human-robot-shared-spaces]]).

## Critical assessment (our view)
- Crash rates of 5–10 % in real dynamic tests are far from an industrial safety argument; collision avoidance is only a cost. A certified layer (speed and separation monitoring) would still be required ([[concepts/constraints-and-safety]]).
- Blending means of planners with different strategies can produce a mean that none of the planners would choose; the paper does not analyse this beyond the GMR approximation.
- Many hand-tuned weights (Table I) and three temperatures (α, λ, β); the grid search (Table IV) covers only two weights.
- GPU-only results; no CPU timing. Comparison with MoveIt at 1 Hz Octomap is not a like-for-like reactive baseline.
- No task-space/path constraint: point-to-point reaching only.

## Links
- [[applications/industrial-manipulators]] · [[applications/human-robot-shared-spaces]] · [[concepts/multimodality]] · [[concepts/constraints-and-safety]]
- [[comparisons/mppi-variants-matrix]] · [[comparisons/welding-mppi-design-review]]
- Related: [[sources/bhardwaj2021storm]] (baseline and base implementation), [[sources/bhardwaj2020mpq]] (value function used for weights), [[sources/zhang2024m3p2i]] and [[sources/liu2026clusteringmppi]] (multimodal MPPI: blend vs select), [[sources/zhao2025tangentialmpc]], [[sources/kalakrishnan2011stomp]], [[sources/makoviychuk2021isaacgym]]
- BibTeX key: `zhou2025parallelmppi` in `latex/references.bib`
