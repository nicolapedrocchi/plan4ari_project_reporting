---
title: MPPI for industrial and collaborative manipulators
type: application
updated: 2026-10-01
---

# MPPI for industrial and collaborative manipulators

| Work | Level | Platform | Rate | Notes | Source |
|---|---|---|---|---|---|
| STORM | joint-space kinematics, GPU | Franka 7-DoF | 125 Hz | learned self-collision, SDF costs, Halton splines | [[sources/bhardwaj2021storm]] |
| cuRobo | global motion generation | various arms | 30–50 ms/plan | particle seeding + L-BFGS | [[sources/sundaralingam2023curobo]] |
| IsaacGym-MPPI | simulator in the loop | Panda, mobile manipulators | 25 Hz | pushing, whole-body | [[sources/pezzato2025isaacmppi]] |
| M3P2I | multi-modal TAMP | Franka | 25 Hz (+1 Hz AIP) | alternative grasps/skills | [[sources/zhang2024m3p2i]] |
| Torque-sampling MPPI | torque, full RBD | 7-DoF | >166 Hz, 0.18 s | compliant, force-aware | [[sources/im2026torquemppi]] |
| PR-MPPI | velocity + projection | 14-DoF dual arm, H1-2 | — | exact equality/inequality constraints | [[sources/lee2026prmppi]] |
| COSMIK-MPPI | HRC collision avoidance | torque-controlled arm | 22 ms constant | constraints-as-terminations + markerless human pose | [[sources/gursoy2026cosmik]] |
| CE-MPPI | multimodal | UR5e | — | −48% time-to-goal | [[sources/liu2026clusteringmppi]] |
| MJX sampling MPC | contact-rich | Franka FR3 | 8–10 Hz | MoveIt Servo 1 kHz downstream | [[sources/dierking2026parallelsbmpc]] |
| VP-STO | via-point stochastic opt. | Franka | — | time-optimal smooth | [[sources/jankowski2023vpsto]] |
| PMPPI | parallel MPPI planners + SDF cost | Franka | 27.8 Hz real | blends planners; crash rates 0-8.75% sim | [[sources/zhou2025parallelmppi]] |
| MPPI-Tan | tangential subspace sampling | Franka sim, JAKA real | 14-95 Hz | few rollouts (N=50) | [[sources/zhao2025tangentialmpc]] |
| CSMPC (preprint) | null-space projected MPPI | Diana7 | ~13 ms/step | path error <0.43 mm real | [[sources/wang2024constrainedpi]] |
| STOMP (offline ancestor) | trajectory | PR2 | offline | MoveIt plugin | [[sources/kalakrishnan2011stomp]] |

## Path-constrained (welding / toolpath) — non-MPPI references
- Breakpoint-minimising DP ([[sources/yin2024dpbreakpoints]]), DP with online adjustment ([[sources/yin2024dprealtime]]), functionally-redundant IK for 5-axis tasks ([[sources/razjigaev2025functional]]), GRR roadmaps ([[sources/zhong2024expansiongrr]]), welding morphology/base positioning ([[sources/gautier2024weldingbase]]). See [[concepts/path-wise-redundancy-resolution]].

## Observations
- Industrial interfaces need smooth, bounded references at 1 kHz → MPPI rates (20–170 Hz) require a downstream certified layer ([[sources/faroni2019pik]], [[sources/faroni2020scaling]]); [[sources/dierking2026parallelsbmpc]] does this with MoveIt Servo.
- Exact kinematic constraints now possible (PR-MPPI); human separation via COSMIK → [[applications/human-robot-shared-spaces]].
- See also [[concepts/constraints-and-safety]], [[concepts/smoothness-action-parametrization]], [[tools/software-ecosystem]].
