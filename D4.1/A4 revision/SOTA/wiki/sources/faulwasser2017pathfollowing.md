---
key: faulwasser2017pathfollowing
title: "Implementation of Nonlinear Model Predictive Path-Following Control for an Industrial Robot"
authors: "Faulwasser, Timm; Weber, Tobias; Zometa, Pablo; Findeisen, Rolf"
year: 2017
venue: "IEEE Transactions on Control Systems Technology, vol. 25, no. 4, pp. 1505-1511"
arxiv: 1506.09084
doi: 10.1109/tcst.2016.2601624
pdf: raw/papers/faulwasser2017pathfollowing.pdf
text: raw/text/faulwasser2017pathfollowing.txt
tags: [mpc, path-following, manipulators, industrial, background]
status: read
---

# Implementation of Nonlinear Model Predictive Path-Following Control for an Industrial Robot

*Faulwasser, Timm; Weber, Tobias; Zometa, Pablo; Findeisen, Rolf* (2017). IEEE Transactions on Control Systems Technology, vol. 25, no. 4, pp. 1505-1511.

## TL;DR
Model predictive path-following control (MPFC): the path parameter θ is made a **virtual state** driven by a virtual input through an integrator chain (timing law), and one NMPC simultaneously chooses joint torques and the progress θ(t) along a Cartesian path, under state/input constraints. Speed assignment (track a reference θ̇_ref) or stop-at-end are selected by changing two weights. Implemented with ACADO code generation and real-time iteration (one SQP step), it runs at **1 kHz** on a KUKA LWR IV with 3 active joints: max OCP solve 0.48 ms, total latency < 0.92 ms; Cartesian error below 1 mm after convergence; the controller slows down or stops along the path under external disturbances.

## Method
- **Problems** (§II-A): Problem 1 — constrained output path following (converge to the path, move forward, θ̇ ≥ 0, satisfy constraints); Problem 2 — speed-assigned path following (θ̇ → θ̇_ref). Remark 1: speed assignment is not trajectory tracking, because timing can be re-adjusted after disturbances.
- **Augmented system** (Eq. 4): robot dynamics + timing law θ^(r+1) = v (here a double integrator); output = path error e = h(x) − p(θ) and virtual state z.
- **OCP** (Eq. 6–7): quadratic cost on (e, θ − θ₁, θ̇ − θ̇_ref) and (u, v); box constraints on joint angles/velocities, torques, z and v. Problem 1: w_θ > 0, w_θ̇ = 0; Problem 2: w_θ̇ > 0, w_θ = 0 (Table I). z is an internal controller state propagated from the previous solution (dynamic feedback).
- **Model** (§III-A, Eq. 8): rigid-body dynamics of joints 1, 2, 4 (others locked); Coulomb friction smoothed by arctan; gravity compensated by the robot controller and dropped from the OCP; path = C¹ polynomial splines in Cartesian space.
- **Solver** (§III-B): ACADO Toolkit 1.2.1beta, direct single shooting, real-time iteration (one SQP iteration per sample), implicit Gauss–Legendre integrator order 2 with 10 steps; horizon T = 100 ms, sampling δ = 1 ms, inputs piecewise constant on 10 intervals of 10 ms → Hessian 40 × 40. Torques superposed via the KUKA Fast Research Interface in joint impedance mode; velocities from filtered finite differences.
- Remark 3: stability/path convergence need terminal penalty + terminal constraint (from earlier theory), not used in the experiments.

## Evidence
- **Platform**: KUKA LWR IV, 3 actuated joints, pen writing on a whiteboard; external PC Intel Xeon X5675 3.07 GHz, Linux, C/C++ (§III-B).
- **Timing** (§III-B): OCP solve max 0.48 ms (mean 0.24 ms, median 0.18 ms); overall latency incl. estimation and communication < 0.92 ms (mean 0.42 ms, median 0.42 ms) → 1 kHz, the interface maximum.
- **Clover path, speed assignment** (§IV, Fig. 2): errors drop below 1 mm after the controller is switched on and stay there; path speed varies periodically with curvature; θ̇ does not reach θ̇_ref = 250 s⁻¹ because joint-4 velocity bound is active — the controller trades speed for feasibility instead of violating constraints.
- **"Hello" path with disturbances** (§IV, Fig. 3): during five intervals of manual pushing the robot is dragged off the path; MPFC slows/stops θ and returns to the path when released, then stops at the path end.
- **Table I**: weights w_e = 10⁷, r_u = 0.5, r_v = 10⁻⁷; torque bound 60 Nm; joint-speed bound 0.5 or 0.6 rad/s depending on the experiment; 1800 / 2700 spline segments.

## Relevance for Plan4ARI
- This is the canonical form of our **downstream speed layer** ([[comparisons/welding-mppi-design-review]], "Downstream MPC"): MPPI provides the geometric path (joint path q(s) on the chosen IK branch, or the Cartesian seam + null-space profile), and an MPFC chooses the timing s(t) with joint limits as hard constraints. Speed assignment (Problem 2) with θ̇_ref = nominal travel speed and box constraints [0.9, 1.1]·θ̇_ref on the virtual state directly encodes the ±10% welding tolerance.
- **Computation-time evidence**: a 3-DoF torque-level NMPC with 100 ms horizon solves in < 0.5 ms with RTI on a 2010-era Xeon. For a 6/7-DoF arm the Hessian grows; but for welding speeds a kinematic (velocity/acceleration-level) model and a 10–100 Hz downstream rate would suffice, so a path-following NMPC with acados ([[sources/verschueren2022acados]]) is plausibly affordable on an IPC — still to benchmark.
- Disturbance behaviour (slow down/stop and recover on the path) is what we want when MPPI's look-ahead is late or a seam correction arrives; but for welding, *stopping* means an arc defect — the ±10% bound must be a hard constraint and a violation must trigger the planned detach logic upstream.
- Lighter alternatives with the same path–velocity split: [[sources/faroni2020scaling]], [[sources/faroni2019pik]], [[sources/palleschi2021fastsafe]]; MPPI-native feedback alternative: [[sources/belvedere2026feedbackmppi]].

## Critical assessment (our view)
- Proof of concept only: 3 joints, planar writing task, no orientation path, no redundancy, no collision constraints, gravity handled by the vendor controller. Torque-level interface (FRI) is not available on typical industrial welding controllers, which accept position/velocity setpoints.
- No terminal ingredients in experiments, so no formal convergence/recursive-feasibility guarantee in the tested setup (Remark 3); RTI returns a sub-optimal iterate.
- Speed assignment is soft (weight on θ̇ − θ̇_ref); constant-speed welding needs either hard bounds on θ̇ or a high weight plus feasibility check — the clover experiment shows the speed reference is simply abandoned when joint limits bind.
- No comparison with decoupled time-scaling or trajectory-tracking MPC (authors refer to other work).

## Abstract (verbatim, arXiv)
> Many robotic applications, such as milling, gluing, or high precision measurements, require the exact following of a pre-defined geometric path. In this paper, we investigate the real-time feasible implementation of model predictive path-following control for an industrial robot. We consider constrained output path following with and without reference speed assignment. We present results from an implementation of the proposed model predictive path-following controller on a KUKA LWR IV robot.

## Links
- [[concepts/mppi-vs-mpc]] · [[concepts/path-wise-redundancy-resolution]] · [[applications/industrial-manipulators]]
- [[comparisons/welding-mppi-design-review]]
- Related: [[sources/verschueren2022acados]], [[sources/faroni2020scaling]], [[sources/faroni2019pik]], [[sources/palleschi2021fastsafe]], [[sources/belvedere2026feedbackmppi]], [[sources/rawlings2017mpc]]
- BibTeX key: `faulwasser2017pathfollowing` in `latex/references.bib`
