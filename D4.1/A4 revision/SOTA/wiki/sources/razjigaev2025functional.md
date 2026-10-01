---
key: razjigaev2025functional
title: "Fast Functionally Redundant Inverse Kinematics for Robotic Toolpath Optimisation in Manufacturing Tasks"
authors: "Razjigaev, Andrew; Lohr, Hans; Vargas-Uscategui, Alejandro; King, Peter; Bandyopadhyay, Tirthankar"
year: 2025
venue: "arXiv preprint arXiv:2512.10116"
arxiv: 2512.10116
doi: 
pdf: raw/papers/razjigaev2025functional.pdf
text: raw/text/razjigaev2025functional.txt
tags: [inverse-kinematics, redundancy-resolution, manipulators, industrial, welding]
status: read
---

# Fast Functionally Redundant Inverse Kinematics for Robotic Toolpath Optimisation in Manufacturing Tasks

*Razjigaev, Andrew; Lohr, Hans; Vargas-Uscategui, Alejandro; King, Peter; Bandyopadhyay, Tirthankar* (2025). arXiv preprint arXiv:2512.10116.

## TL;DR
FRIK: a local, iterative IK solver for **functionally redundant** tasks (symmetric tool, 5-DoF task on a 6-axis arm). The pose error and Jacobian are expressed in the target frame and the tool-axis roll row is masked out (task-space decomposition), then each iteration does a damped Newton-Raphson step followed by a damped **Halley** (second-order, kinematic Hessian) step. Rotation about the tool axis is never prescribed; it falls out of the minimum-norm damped update, which gives small joint motion. Tested in simulation (Continuous3D, ABB IRB4600, conical spiral cold-spray toolpath) and replayed on the real robot: ~0.2 ms per target pose, +92% reachable workpiece placements and -16.66% joint travel compared with a hand-picked fixed roll.

## Method
- Toolpath = N target poses T_d(k); only the tool z-axis direction and the position matter (5-DoF task, §II).
- Baseline: resolved-rate IK with saturated twist error e = log(T_e T_d^-1) (Eq. 5-6) and damped least-squares pseudo-inverse (Eq. 8-9).
- **Task-space decomposition** (§IV, following Zlajpah & Müller's TSD): rotate J and dx into the target frame with R~_t = blkdiag(R_d, R_d) (Eq. 12), then apply a selection mask T_t (Eq. 13-14). T_{r=5} = [I_5 0] removes the rotation about the target z-axis (Eq. 15); T_{r=3} keeps position only (Eq. 16). DLS on the reduced r x n Jacobian (Eq. 17).
- **Halley's method** (§V, after Lloyd et al. 2022): uses the kinematic Hessian H (6 x n x n). Damped NR step dq_dnr (Eq. 25), augmented matrix A = J + 1/2 H dq_dnr, projected the same way (Eq. 24), and a damped Halley step dq = Â^T(ÂÂ^T + λ²I)^-1 dx̂ (Eq. 26).
- Algorithm 1: iterate until ||dx̂|| < ε or max iterations; the trajectory starts from a given q0 (Eq. 27), and successive targets are solved from the previous solution (implied by the q0-dependence discussed in §VII). Implemented in C++/Eigen. The values of λ, ε and the iteration cap are not reported.
- No secondary objectives (joint limits, collisions, manipulability) and no cone/tolerance constraints. The redundancy is used only through the minimum-norm damped update.

## Evidence
- Robot: ABB IRB4600 (6 DoF, DH parameters in Table I) carrying an Impact Innovations 5/11 cold-spray gun. Toolpath: spiral on a cone of 100 mm diameter and 50 mm height (§VI). Fig. 1 uses a Fanuc LRmate200ic weld-torch line only as an illustration.
- **Workpiece placement** (§VI-A, Table II, Figs. 3-4): 100 mm voxel grid on the wall plane. Reachable voxels: 75 with the ad hoc roll vs 144 with FRIK (+92%). Joint-limit-weighted manipulability: max 77,040 -> 63,309 (-17.8%), mean 34,934 -> 25,304 (-27.6%). FRIK failed at a few voxels near the base where the ad hoc roll succeeded; the authors attribute this to local (non-global) optimality.
- **Joint travel** (§VI-B, Table III, Figs. 5 and 8, workpiece at y = -1.1 m, z = 0.9 m): overall 6D joint-space distance 685.5° -> 571.3° (-16.66%). J4 -72.6% and J6 -51.8%, but J5 +168% and J2 +23.8%: motion is redistributed, not reduced on every joint.
- **Computation** (Table IV): 717 linear move commands, 81,746 simulation steps, **196.0 µs average per step**, 3.69 s total, on a 13th-gen Intel i7 laptop with 32 GB RAM (§VI-C).
- **Hardware** (§VI-C, Figs. 6-7 and 9): the program was exported to ABB RobotStudio and run in CSIRO Lab22. Joints 4-6 deviated from simulation because the toolpath location was miscalibrated.
- Limitations stated by the authors (§VII): greedy local optimiser that depends on q0; no secondary objectives (obstacles, joint limits, torque, energy); sensitive to the sim-to-real gap; **no tolerance cones** for admissible orientations. Future work: flexible constraints, combination with sampling-based global planning, search for the best q0.

## Relevance for Plan4ARI
- It addresses exactly our 5-axis case: torch-axis roll is free and handled by masking one row of the target-frame Jacobian. Its cost (~0.2 ms per pose on a laptop CPU) suits two roles in our design: (i) an **inner IK** inside MPPI rollouts, where each rollout sample perturbs the target (cone tilt) and FRIK resolves the roll by minimum joint motion; (ii) a **deterministic baseline**, i.e. warm-started FRIK along the seam starting from each of the up-to-8 IK branches at the first seam point, to compare against the MPPI look-ahead [[comparisons/welding-mppi-design-review]].
- The masking idea extends naturally: masking two rotational rows would free the whole tool direction (cone), but then the cone limit (~10°, possibly anisotropic) has to be enforced somewhere else, for example by clamping or by an MPPI cost.
- Its reported failure mode (greedy, depends on q0, locally optimal over long paths) is the argument for keeping a look-ahead or global layer on top: MPPI horizon, DP-based path-wise resolution ([[sources/yin2024dpbreakpoints]]) or GRR roadmaps ([[sources/zhong2024expansiongrr]]).

## Critical assessment (our view)
- It is an IK step, not a planner: it does not handle joint limits, collisions, singularity avoidance (only damping), manipulability or configuration changes. In the paper, travel and manipulability move in opposite directions (Table II vs III).
- The orientation constraint is either exact or fully free about one axis. There are no cone or tolerance bounds, which is what our ±10° torch cone needs. Bounds like these, together with joint limits, are what a constrained, horizon-based IK such as [[sources/faroni2019pik]] (QP with task scaling) or an MPPI cost would provide.
- The evidence is thin: one toolpath, one robot, one placement for the travel analysis, no comparison against Descartes, TSD-only or other planners, and no convergence statistics (iterations, failure rate). λ, ε and the iteration limit are not given.
- Timing is per simulation step on a CPU and covers a whole toolpath offline. For MPPI we would need a batched or GPU version. This is plausible because the method is fixed-iteration and matrix-only, but the paper does not show it.
- Arc welding is named as a motivating application but not tested; velocity and travel speed are not addressed.

## Abstract (verbatim, arXiv)
> Industrial automation with six-axis robotic arms is critical for many manufacturing tasks, including welding and additive manufacturing applications; however, many of these operations are functionally redundant due to the symmetrical tool axis, which effectively makes the operation a five-axis task. Exploiting this redundancy is crucial for achieving the desired workspace and dexterity required for the feasibility and optimisation of toolpath planning. Inverse kinematics algorithms can solve this in a fast, reactive framework, but these techniques are underutilised over the more computationally expensive offline planning methods. We propose a novel algorithm to solve functionally redundant inverse kinematics for robotic manipulation utilising a task space decomposition approach, the damped least-squares method and Halley's method to achieve fast and robust solutions with reduced joint motion. We evaluate our methodology in the case of toolpath optimisation in a cold spray coating application on a non-planar surface. The functionally redundant inverse kinematics algorithm can quickly solve motion plans that minimise joint motion, expanding the feasible operating space of the complex toolpath. We validate our approach on an industrial ABB manipulator and cold-spray gun executing the computed toolpath.

## Links
- [[concepts/path-wise-redundancy-resolution]]
- [[comparisons/welding-mppi-design-review]]
- [[applications/industrial-manipulators]]
- [[concepts/mppi-vs-mpc]]
- Related: [[sources/zhong2024expansiongrr]], [[sources/faroni2019pik]], [[sources/yin2024dpbreakpoints]], [[sources/yin2024dprealtime]]
- BibTeX key: `razjigaev2025functional` in `latex/references.bib`
