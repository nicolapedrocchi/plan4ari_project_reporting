---
title: Physics simulators as MPPI dynamics models
type: concept
updated: 2026-10-01
---

# Physics simulators as MPPI dynamics models

Because MPPI only needs forward simulation, a GPU physics engine can replace hand-written dynamics and contact models.

| Engine / stack | Use | Source |
|---|---|---|
| Isaac Gym | 750 parallel envs at 25 Hz: navigation, pushing, whole-body mobile manipulation | [[sources/pezzato2025isaacmppi]], [[sources/makoviychuk2021isaacgym]] |
| Isaac Gym (multi-modal) | N×K rollouts for alternative plans | [[sources/zhang2024m3p2i]] |
| Isaac Gym (UR5e) | CE-MPPI rollouts | [[sources/liu2026clusteringmppi]] |
| MuJoCo (MJPC) | predictive sampling | [[sources/howell2022predictivesampling]] |
| MuJoCo-MJX + JAX | contact-rich Push-T on Franka FR3, 8–10 Hz on RTX 5090 | [[sources/dierking2026parallelsbmpc]] |

**Pros.** Contacts, articulated objects, mobile bases "for free"; easy to switch robot.
**Cons.** Compute cost per rollout; sim-to-real gap of contact parameters; non-determinism of GPU physics; difficult to certify. Domain randomisation helps only for contact-initiation parameters ([[sources/dierking2026parallelsbmpc]]).
