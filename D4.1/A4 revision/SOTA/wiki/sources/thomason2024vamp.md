---
key: thomason2024vamp
title: "Motions in Microseconds via Vectorized Sampling-Based Planning"
authors: "Thomason, Wil; Kingston, Zachary; Kavraki, Lydia E."
year: 2024
venue: "Proc. IEEE Int. Conf. Robotics and Automation (ICRA), pp. 8749-8756"
arxiv: 2309.14545
doi: 10.1109/ICRA57147.2024.10611190
pdf: raw/papers/thomason2024vamp.pdf
text: raw/text/thomason2024vamp.txt
tags: [path-planning, software, hardware, manipulators]
status: summarised
---

# Motions in Microseconds via Vectorized Sampling-Based Planning

*Thomason, Wil; Kingston, Zachary; Kavraki, Lydia E.* (2024). Proc. IEEE Int. Conf. Robotics and Automation (ICRA), pp. 8749-8756.

## TL;DR
VAMP (Vector-Accelerated Motion Planning): sampling-based planners (e.g. RRT-Connect) made 500×+ faster by vectorising forward kinematics and collision checking with CPU SIMD instructions (AVX2, ARM Neon), reaching planning times of tens of microseconds on one CPU core, without a GPU. Open source: https://github.com/KavrakiLab/vamp (link provided by the user, 2026-10-01).

## Method
- Struct-of-Arrays memory layout so that a batch of configurations is processed in one SIMD vector (Fig. 1).
- **Tracing compiler**: from a URDF it generates branch-free, unrolled FK code specialised for the robot (§IV).
- Collision geometry approximated by sphere hierarchies generated from meshes; obstacles as primitives; "raked" edge validation checks evenly spaced configurations in parallel and stops at the first collision (Fig. 2).
- Assumes a Euclidean configuration space (linear interpolation, ℓ2 distances).

## Evidence
- Median 40 µs for the 7-DoF Panda over the MotionBenchMaker problems (≈ 25 kHz), single CPU core (§I, Table I); robots from 7 to 14 DoF (Panda, Fetch, Baxter); also evaluated on a low-power single-board computer (ARM).
- AVX-512 gave lower throughput than AVX2 in the authors' tests.

## Relevance for Plan4ARI
- Proposed by the user as the planner for the **connection motion q_state → q_start** (detach / reconfigure / approach) in the welding design ([[comparisons/welding-mppi-design-review]]). At these speeds the *actual* transfer path for each of the 8 IK-branch goals can be computed every cycle, instead of an estimate.
- Its vectorised FK + sphere collision primitives are also exactly what a **CPU-based MPPI rollout** needs: a route to MPPI without GPU, consistent with the proposal KPI that excludes GPU planners ([[project/prj-plan4ari-proposal]]).
- CPU-only, low power: compatible with industrial PCs (Open IPC).

## Critical assessment (our view)
- Output is a geometric path: it needs time parametrisation (e.g. time-optimal / jerk-limited) before execution, and its time is the real transition cost.
- Sphere approximations of torch, hose package and a very large welded structure: accuracy vs number of spheres must be checked near the seam (tight clearances).
- A new robot (e.g. COMAU) needs code generated from its URDF by the tracing compiler — feasible but to verify in practice.

## Abstract (verbatim, arXiv)
> Modern sampling-based motion planning algorithms typically take between hundreds of milliseconds to dozens of seconds to find collision-free motions for high degree-of-freedom problems. This paper presents performance improvements of more than 500x over the state-of-the-art, bringing planning times into the range of microseconds and solution rates into the range of kilohertz, without specialized hardware. Our key insight is how to exploit fine-grained parallelism within sampling-based planners, providing generality-preserving algorithmic improvements to any such planner and significantly accelerating critical subroutines, such as forward kinematics and collision checking. We demonstrate our approach over a diverse set of challenging, realistic problems for complex robots ranging from 7 to 14 degrees-of-freedom. Moreover, we show that our approach does not require high-power hardware by also evaluating on a low-power single-board computer. The planning speeds demonstrated are fast enough to reside in the range of control frequencies and open up new avenues of motion planning research.

## Links
- [[comparisons/welding-mppi-design-review]]
- [[tools/software-ecosystem]]
- [[project/prj-plan4ari-proposal]]
- Related: [[sources/sundaralingam2023curobo]], [[sources/desai2026fpgampi]]
- BibTeX key: `thomason2024vamp` in `latex/references.bib`
