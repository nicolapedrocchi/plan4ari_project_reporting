---
key: testouri2023mppiad
title: "Towards a Safe Real-Time Motion Planning Framework for Autonomous Driving Systems: An MPPI Approach"
authors: "Testouri, Mehdi; Elghazaly, Gamal; Frank, Raphael"
year: 2023
venue: "Proc. Int. Conf. Robotics, Automation and Artificial Intelligence (RAAI)"
arxiv: 2308.01654
doi: 10.1109/RAAI59955.2023.10601272
pdf: raw/papers/testouri2023mppiad.pdf
text: raw/text/testouri2023mppiad.txt
tags: [mobile, driving]
status: summarised
---

# Towards a Safe Real-Time Motion Planning Framework for Autonomous Driving Systems: An MPPI Approach

*Testouri, Mehdi; Elghazaly, Gamal; Frank, Raphael* (2023). Proc. Int. Conf. Robotics, Automation and Artificial Intelligence (RAAI).

## TL;DR
MPPI-based real-time safe motion planning framework for autonomous driving (Frenet/road constraints).

## Method
MPPI with driving-specific costs and safety layer.

## Evidence
Simulation.

## Relevance for Plan4ARI
Structured-environment MPPI design patterns.

## Abstract (verbatim, arXiv)
> Planning safe trajectories in Autonomous Driving Systems (ADS) is a complex problem to solve in real-time. The main challenge to solve this problem arises from the various conditions and constraints imposed by road geometry, semantics and traffic rules, as well as the presence of dynamic agents. Recently, Model Predictive Path Integral (MPPI) has shown to be an effective framework for optimal motion planning and control in robot navigation in unstructured and highly uncertain environments. In this paper, we formulate the motion planning problem in ADS as a nonlinear stochastic dynamic optimization problem that can be solved using an MPPI strategy. The main technical contribution of this work is a method to handle obstacles within the MPPI formulation safely. In this method, obstacles are approximated by circles that can be easily integrated into the MPPI cost formulation while considering safety margins. The proposed MPPI framework has been efficiently implemented in our autonomous vehicle and experimentally validated using three different primitive scenarios. Experimental results show that generated trajectories are safe, feasible and perfectly achieve the planning objective. The video results as well as the open-source implementation are available at: https://gitlab.uni.lu/360lab-public/mppi

## Links
- [[applications/mobile-robots-amr]]
- BibTeX key: `testouri2023mppiad` in `latex/references.bib`
