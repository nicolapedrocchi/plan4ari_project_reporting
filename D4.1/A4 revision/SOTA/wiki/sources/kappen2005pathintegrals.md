---
key: kappen2005pathintegrals
title: "Path integrals and symmetry breaking for optimal control theory"
authors: "Kappen, H. J."
year: 2005
venue: "Journal of Statistical Mechanics: Theory and Experiment, vol. 2005, no. 11, pp. P11011"
arxiv: physics/0505066
doi: 10.1088/1742-5468/2005/11/P11011
pdf: raw/papers/kappen2005pathintegrals.pdf
text: raw/text/kappen2005pathintegrals.txt
tags: [foundations, theory]
status: summarised
---

# Path integrals and symmetry breaking for optimal control theory

*Kappen, H. J.* (2005). Journal of Statistical Mechanics: Theory and Experiment, vol. 2005, no. 11, pp. P11011.

## TL;DR
Shows that, for control-affine dynamics and quadratic control cost with lambda*R^-1 = Sigma, the HJB equation becomes linear via V = -lambda log Psi; the solution is a path integral (Feynman-Kac) over uncontrolled trajectories.

## Method
Exponential transformation of the value function; Feynman-Kac representation; Monte-Carlo estimate of the optimal control as cost-weighted noise. Discusses symmetry breaking (multiple optimal solutions) as a function of noise level.

## Evidence
Analytical examples (delayed choice, symmetry breaking).

## Relevance for Plan4ARI
Theoretical root of every MPPI variant. The noise/cost coupling assumption explains why MPPI exploration and control penalty are tied together.

## Abstract (verbatim, arXiv)
> This paper considers linear-quadratic control of a non-linear dynamical system subject to arbitrary cost. I show that for this class of stochastic control problems the non-linear Hamilton-Jacobi-Bellman equation can be transformed into a linear equation. The transformation is similar to the transformation used to relate the classical Hamilton-Jacobi equation to the Schrödinger equation. As a result of the linearity, the usual backward computation can be replaced by a forward diffusion process, that can be computed by stochastic integration or by the evaluation of a path integral. It is shown, how in the deterministic limit the PMP formalism is recovered. The significance of the path integral approach is that it forms the basis for a number of efficient computational methods, such as MC sampling, the Laplace approximation and the variational approximation. We show the effectiveness of the first two methods in number of examples. Examples are given that show the qualitative difference between stochastic and deterministic control and the occurrence of symmetry breaking as a function of the noise.

## Links
- [[concepts/path-integral-control]]
- BibTeX key: `kappen2005pathintegrals` in `latex/references.bib`
