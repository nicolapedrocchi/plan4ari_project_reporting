---
key: dharmawan2018functional
title: "Maximizing Robot Manipulator's Functional Redundancy via Sequential Informed Optimization"
authors: "Dharmawan, Audelia G.; Padmanathan, Suhasini; Xiong, Yi; Ituarte, Inigo F.; Foong, Shaohui; Soh, Gim Song"
year: 2018
venue: "2018 3rd International Conference on Advanced Robotics and Mechatronics (ICARM), pp. 334-339"
arxiv: 
doi: 10.1109/icarm.2018.8610834
pdf: raw/papers/dharmawan2018functional.pdf
text: raw/text/dharmawan2018functional.txt
tags: [redundancy-resolution, path-planning, manipulators, industrial, welding]
status: read
---

# Maximizing Robot Manipulator's Functional Redundancy via Sequential Informed Optimization

*Dharmawan, Audelia G.; Padmanathan, Suhasini; Xiong, Yi; Ituarte, Inigo F.; Foong, Shaohui; Soh, Gim Song* (2018). 2018 3rd International Conference on Advanced Robotics and Mechatronics (ICARM), pp. 334-339.

## TL;DR
For a 6-axis arm whose task leaves the rotation about the torch approach axis free (functional redundancy, wire-arc additive manufacturing with a welding torch), a constrained nonlinear optimisation over joint angles plus the free roll γ is solved per path point, **warm-started with the optimum of the previous point** ("Sequential Informed Optimization", SIO). Only the first point needs a global (exhaustive) search. Costs: manipulability or joint velocity (successive joint differences).

## Method
- Path discretised into task poses T_i; per point minimise f(x) subject to 7 kinematic equality constraints (Eq. 1, 9–10), with x = six joints, an auxiliary variable μ and roll γ.
- Torch approach direction fixed along gravity, γ free (Eq. 7); base and tool frames enter via Eq. 8.
- Costs: negative squared closed-form manipulability of the ABB IRB1660ID (Eq. 2–5) or sum of squared joint differences to the previous point (Eq. 6).
- **Global initialisation** of the first point by exhaustive search; then SQP at each next point seeded with the previous optimum (§II, Fig. 2). Global optimality is argued from continuity of the optimum along the path.

## Evidence
- Numerical simulation only; ABB IRB1660ID welding robot, no extra axes (§III, Fig. 3).
- Two WAAM layers (§IV): 50 × 50 cm square and 1.6 × 0.9 m rectangle (near reach limit), discretised at 5 cm; SQP solver; ground truth by exhaustive search.
- SIO matches the exhaustive-search optimum; the ground truth alternates between elbow-left/right solutions with similar manipulability, while SIO stays on one and gives a smoother sequence (Fig. 4–5).
- About 20 ms per new path point, presented as compatible with a 50 Hz loop (§IV).
- Joint-velocity cost reduces mean joint velocity, acceleration and jerk versus fixed γ, although single joints (e.g. joint 6) can be higher at some points (Fig. 6–7, qualitative).

## Relevance for Plan4ARI
- Same **functional redundancy** as our seam task (free roll on a 6-axis arm); confirms that exploiting the roll improves manipulability and joint smoothness over a fixed tool orientation.
- Warm-starting from the previous optimum is the deterministic analogue of MPPI's shifted nominal sequence; ~20 ms per point shows per-point optimisation over (q, roll) is cheap once a seed per IK branch exists, consistent with the per-branch seeds of our multi-goal design ([[comparisons/welding-mppi-design-review]]).
- No external axis; a rail would add one variable to the same formulation.

## Critical assessment (our view)
- "Globally optimal" is not shown in general: the sequential warm start is greedy along the path and cannot anticipate a needed **branch switch** or a dead end later on the seam (the myopia that DP or a look-ahead addresses).
- The elbow switching of the pointwise ground truth shows that pointwise optimality is not path feasibility; SIO's smoothness comes from staying near the seed, not from an explicit continuity constraint.
- No joint limits, collisions, orientation cone, travel-speed constraint or timing; manipulability formula is robot-specific; 5 cm discretisation is coarse for welding.
- The 7-equation kinematic formulation with auxiliary μ is less general than analytic IK plus a 1-D search over γ.

## Links
- [[concepts/path-wise-redundancy-resolution]]
- [[comparisons/welding-mppi-design-review]]
- [[applications/industrial-manipulators]]
- Related: [[sources/razjigaev2025functional]] (fast functional-redundant IK), [[sources/sun2020externalaxis]], [[sources/yin2024dpbreakpoints]]
- BibTeX key: `dharmawan2018functional` in `latex/references.bib`
