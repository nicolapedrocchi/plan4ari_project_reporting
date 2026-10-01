---
key: palleschi2021fastsafe
title: "Fast and Safe Trajectory Planning: Solving the Cobot Performance/Safety Trade-Off in Human-Robot Shared Environments"
authors: "Palleschi, Alessandro; Hamad, Mazin; Abdolshah, Saeed; Garabini, Manolo; Haddadin, Sami; Pallottino, Lucia"
year: 2021
venue: "IEEE Robotics and Automation Letters, vol. 6, no. 3, pp. 5445-5452"
arxiv: 
doi: 10.1109/LRA.2021.3076968
pdf: raw/papers/palleschi2021fastsafe.pdf
text: raw/text/palleschi2021fastsafe.txt
tags: [hri, safety, iso-ts-15066, manipulators, mpc, trajectory-scaling]
status: read
---

# Fast and Safe Trajectory Planning: Solving the Cobot Performance/Safety Trade-Off in Human-Robot Shared Environments

*Palleschi, Alessandro; Hamad, Mazin; Abdolshah, Saeed; Garabini, Manolo; Haddadin, Sami; Pallottino, Lucia* (2021). IEEE Robotics and Automation Letters, vol. 6, no. 3, pp. 5445-5452.

## TL;DR
Online replanning of the **time law along a fixed path** for cobots: a convex, jerk-limited, minimum-time path-tracking problem is re-solved at 25–40 Hz whenever a biomechanics-based safety module (Safe Motion Unit, PFL-type speed limits from reflected mass and injury data) detects that the planned motion would exceed safe speeds over a short horizon; a *performance recovery* step restores the time-optimal profile as soon as possible.

## Method
- Time-optimal path tracking in the (a = s̈, b = ṡ²) variables with velocity, acceleration, torque **and jerk as hard constraints**, kept convex by a worst-case jerk upper bound (§II-A, Eq. 4–5); the convex approximation is ~93% faster to solve than the non-convex one (Appendix).
- Safety evaluation over a receding monitoring horizon at points of interest (POIs): reflected mass → maximum safe speed from injury curves (Eq. 6, Alg. 2).
- Safe replanning: same convex problem with POI speed limits mapped to upper bounds on b (Eq. 7–8) → feasible, safe trajectory respecting actuation limits.
- Path is never modified (path consistency, predictability).
- Implementation: C++, CasADi + IPOPT (MA57).

## Evidence
- Simulation (Panda + SoftHand, circular path, moving human): conservative offline scaling needs ~6× lower velocity limits to be safe; performance recovery reduces task time by ~18% with respect to replanning without recovery (§III).
- Experiments: Panda unwrapping station (25 Hz, 0.12 s horizon); comparison with plain velocity scaling on Panda and UR10e, 80 tests, planner at 40 Hz with 25 ms horizon, OpenPose perception at 15 Hz: the proposed method completed all trajectories, velocity scaling failed in some tests because of infeasible decelerations (§IV).

## Relevance for Plan4ARI
- Cited in the Project Description ([[project/prj-plan4ari-proposal]]) for the cobot performance/safety trade-off.
- It is a concrete instance of the **certified downstream layer** we propose under an MPPI planner: convex, jerk-limited, actuator-feasible re-timing that enforces PFL limits — the same role as the Core-IPC MPC / trajectory scaling ([[sources/faroni2020scaling]]) in [[comparisons/plan4ari-gap-analysis]].
- Shows why naive speed override is insufficient: scaling can command infeasible decelerations.

## Critical assessment (our view)
- Reactive and path-preserving: it cannot avoid slowdowns by changing the path; this is exactly what a path-level (MPPI or [[sources/faroni2022safetyaware]]) planner adds on top.
- Single POI and chest injury data in experiments; multi-POI is future work.

## Links
- [[applications/human-robot-shared-spaces]]
- [[concepts/constraints-and-safety]]
- [[concepts/hybrid-gradient-sampling]]
- [[comparisons/plan4ari-gap-analysis]]
- [[project/prj-plan4ari-proposal]]
- [[sources/faroni2020scaling]]
- [[sources/laha2023sstar]]
- BibTeX key: `palleschi2021fastsafe` in `latex/references.bib`
