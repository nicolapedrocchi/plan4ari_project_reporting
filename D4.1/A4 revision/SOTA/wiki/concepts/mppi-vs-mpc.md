---
title: MPPI vs MPC and other horizon-based planners
type: concept
updated: 2026-10-01
---

# MPPI vs MPC and other horizon-based planners

Mirrors Section 3 and Table 1 of `latex/main.tex`.

## Gradient-based NMPC
- Deterministic NLP per step (SQP / interior point, real-time iterations), e.g. [[sources/verschueren2022acados]].
- Hard constraints, local optimality, stability & recursive feasibility with terminal ingredients ([[sources/rawlings2017mpc]], [[sources/mayne2014mpc]]).
- Needs smooth models/costs; trapped in the homotopy class of the initial guess; contacts/logic awkward.
- In-house industrial examples: predictive IK & trajectory scaling ([[sources/faroni2019pik]], [[sources/faroni2020scaling]]) → natural **Core-IPC** layer.

## DDP / iLQR
- Riccati backward pass + feedback gains ([[sources/tassa2012ilqg]]). Same smoothness requirements. Used as ancillary controller in Tube-MPPI ([[sources/williams2018tubemppi]]).

## Sampling-based MPC family
| Method | Update | Page |
|---|---|---|
| CEM / iCEM | refit Gaussian on elites | [[sources/rubinstein1999cem]], [[sources/pinneri2020icem]] |
| Predictive sampling | keep best sample | [[sources/howell2022predictivesampling]] |
| MPPI | soft exponential weights | [[concepts/information-theoretic-mppi]] |
| SVMPC | particle (SVGD) posterior | [[sources/lambert2020svmpc]] |
| Unifying view | dynamic mirror descent | [[sources/wagener2019dmd]] |

## Trajectory optimisation for motion planning (offline)
CHOMP [[sources/zucker2013chomp]], STOMP [[sources/kalakrishnan2011stomp]], TrajOpt [[sources/schulman2014trajopt]].

## Mobile-robot local planners (incumbents)
DWA [[sources/fox1997dwa]], TEB [[sources/rosmann2017teb]]; Nav2 moving to MPPI as default ([[sources/macenski2023nav2survey]]).

## Synthesis
- Complementary, not competing: MPPI explores within the horizon and handles non-smooth objectives; gradient MPC refines and certifies.
- Hybrids: cuRobo particle seeding + L-BFGS ([[sources/sundaralingam2023curobo]]), ME-DDP ([[sources/aoyama2026hybrid]]), Tube-MPPI. See [[concepts/hybrid-gradient-sampling]].

## Industrial look-ahead and path-following references
- Online trajectory generation on sampled joint paths with jerk limits, path-exact, 250 Hz on KUKA KR16 ([[sources/lange2016pathaccurate]]).
- CNC-style Cartesian look-ahead with corner blending and bidirectional speed scan ([[sources/ma2025lookahead]]).
- Path-following NMPC on an industrial robot: path parameter as virtual state, OCP solve max 0.48 ms, 1 kHz ([[sources/faulwasser2017pathfollowing]]).
- Null-space NMPC, 100-300 Hz on a 7-DoF arm in simulation ([[sources/sun2024nullspacempc]]).

## Rates reported (for Table 1)
- STORM 125 Hz (7-DoF, GPU); PMPPI 32 ms/iteration on RTX 3060, 27.8 Hz on real Franka ([[sources/zhou2025parallelmppi]]); MPPI-Tan 14-95 Hz depending on horizon ([[sources/zhao2025tangentialmpc]]); CSMPC ~13 ms/step ([[sources/wang2024constrainedpi]]); torque-MPPI 166 Hz, 0.18 s horizon; COSMIK 22 ms/cycle (50 Hz); Pezzato/M3P2I 25 Hz; MJX contact-rich 8–10 Hz; Biased-MPPI 10–50 Hz. Gradient NMPC on small models typically 100–1000 Hz (generic figure, not from a single source).
