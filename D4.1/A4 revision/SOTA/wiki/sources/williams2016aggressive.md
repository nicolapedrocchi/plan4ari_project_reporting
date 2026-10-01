---
key: williams2016aggressive
title: "Aggressive Driving with Model Predictive Path Integral Control"
authors: "Williams, Grady; Drews, Paul; Goldfain, Brian; Rehg, James M.; Theodorou, Evangelos A."
year: 2016
venue: "Proc. IEEE Int. Conf. Robotics and Automation (ICRA), pp. 1433-1440"
arxiv: 
doi: 10.1109/ICRA.2016.7487277
pdf: none
text: none
tags: [foundations, mppi-core, mobile]
status: summarised
---

# Aggressive Driving with Model Predictive Path Integral Control

*Williams, Grady; Drews, Paul; Goldfain, Brian; Rehg, James M.; Theodorou, Evangelos A.* (2016). Proc. IEEE Int. Conf. Robotics and Automation (ICRA), pp. 1433-1440.

## TL;DR
Real-time MPPI on the AutoRally 1:5 rally car at the limits of handling, using GPU rollouts of a learned/physics model.

## Method
Continuous-time path-integral MPPI, thousands of samples on GPU, costmap-based track cost.

## Evidence
Real aggressive driving on dirt track.

## Relevance for Plan4ARI
Proof that sampling-based MPC can run in real time on non-smooth costs; seed of MPPI in mobile robotics.

## Links
- [[concepts/information-theoretic-mppi]]
- [[applications/mobile-robots-amr]]
- BibTeX key: `williams2016aggressive` in `latex/references.bib`
