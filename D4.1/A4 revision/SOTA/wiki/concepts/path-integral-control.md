---
title: Path integral control
type: concept
updated: 2026-10-01
---

# Path integral control

**Definition.** A class of stochastic optimal control problems whose Hamilton–Jacobi–Bellman (HJB) equation becomes *linear* after the exponential transformation `V = -λ log Ψ`, so that the optimal control can be written as an expectation over *uncontrolled* trajectories and estimated by Monte-Carlo sampling.

## Setting
- Dynamics: `dx = f(x) dt + G(x) (u dt + dw)`, `E[dw dwᵀ] = Σ dt` (control-affine, noise enters through the same channel as control).
- Cost: `φ(x_T) + ∫ q(x) + ½ uᵀ R u dt`.
- Key assumption: `λ R⁻¹ = Σ` → cheap control directions must be noisy directions. This couples exploration (noise) and control penalty, and is the origin of the "control cost" term in MPPI weights.

## Result (Feynman–Kac)
- `Ψ(x,t) = E_p[exp(-S(τ)/λ)]`, `S` = state cost of the trajectory.
- `u* dt = E_p[exp(-S/λ) dw] / E_p[exp(-S/λ)]` → optimal control = **cost-weighted average of the noise**.
- Consequences: no gradients of dynamics or cost; arbitrary (non-smooth) state costs; parallelisable.
- Low noise / temperature can induce *symmetry breaking*: several optimal solutions (modes) — the theoretical root of the [[concepts/multimodality]] issue. ([[sources/kappen2005pathintegrals]])

## Lineage
- Theory: [[sources/kappen2005pathintegrals]]
- PI² policy improvement: [[sources/theodorou2010pi2]]
- STOMP offline trajectory optimisation: [[sources/kalakrishnan2011stomp]]
- MPPI receding horizon: [[sources/williams2016aggressive]], [[sources/williams2017jgcd]] → [[concepts/information-theoretic-mppi]]
- Survey: [[sources/kazim2024survey]]

## Open questions
- How restrictive is `λR⁻¹ = Σ` for torque-controlled arms with very different joint inertias? The information-theoretic derivation removes it ([[concepts/information-theoretic-mppi]]) but the tuning coupling remains in practice.
