---
key: gandhi2021rmppi
title: "Robust Model Predictive Path Integral Control: Analysis and Performance Guarantees"
authors: "Gandhi, Manan; Vlahov, Bogdan; Gibson, Jason; Williams, Grady; Theodorou, Evangelos A."
year: 2021
venue: "IEEE Robotics and Automation Letters, vol. 6, no. 2, pp. 1423-1430"
arxiv: 2102.09027
doi: 10.1109/LRA.2021.3057563
pdf: raw/papers/gandhi2021rmppi.pdf
text: raw/text/gandhi2021rmppi.txt
tags: [robustness, guarantees]
status: summarised
---

# Robust Model Predictive Path Integral Control: Analysis and Performance Guarantees

*Gandhi, Manan; Vlahov, Bogdan; Gibson, Jason; Williams, Grady; Theodorou, Evangelos A.* (2021). IEEE Robotics and Automation Letters, vol. 6, no. 2, pp. 1423-1430.

## TL;DR
Robust MPPI: augmented nominal/real state with iterative feedback, bound on free-energy growth giving performance guarantees.

## Method
Nominal state selection, ancillary feedback, theoretical bound.

## Evidence
AutoRally sim/real.

## Relevance for Plan4ARI
Only MPPI variant with explicit performance bounds; template for certified layering.

## Abstract (verbatim, arXiv)
> In this paper we propose a novel decision making architecture for Robust Model Predictive Path Integral control (RMPPI) and investigate its performance guarantees and applicability to off-road navigation. Key building blocks of the proposed architecture are an augmented state space representation of the system consisting of nominal and actual dynamics, a placeholder for different types of tracking controllers, a safety logic for nominal state propagation, and an importance sampling scheme that takes into account the capabilities of the underlying tracking control. Using these ingredients, we derive a bound on the free energy growth of the dynamical system which is a function of task constraint satisfaction level, the performance of the underlying tracking controller, and the sampling error of the stochastic optimization used within RMPPI. To validate the bound on free energy growth, we perform experiments in simulation using two types of tracking controllers, namely the iterative Linear Quadratic Gaussian and Contraction-Metric based control. We further demonstrate the applicability of RMPPI in real hardware using the GT AutoRally vehicle. Our experiments demonstrate that RMPPI outperforms MPPI and Tube-MPPI by alleviating issues of the aforementioned model predictive controllers related to either lack of robustness or excessive conservatism. RMPPI provides the best of the two worlds in terms of agility and robustness to disturbances.

## Links
- [[concepts/robustness-uncertainty]]
- BibTeX key: `gandhi2021rmppi` in `latex/references.bib`
