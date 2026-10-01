---
key: yin2023shieldmppi
title: "Shield Model Predictive Path Integral: A Computationally Efficient Robust MPC Approach Using Control Barrier Functions"
authors: "Yin, Ji; Dawson, Charles; Fan, Chuchu; Tsiotras, Panagiotis"
year: 2023
venue: "IEEE Robotics and Automation Letters, vol. 8, no. 11, pp. 7106-7113"
arxiv: 2302.11719
doi: 10.1109/LRA.2023.3315211
pdf: raw/papers/yin2023shieldmppi.pdf
text: raw/text/yin2023shieldmppi.txt
tags: [safety, cbf]
status: summarised
---

# Shield Model Predictive Path Integral: A Computationally Efficient Robust MPC Approach Using Control Barrier Functions

*Yin, Ji; Dawson, Charles; Fan, Chuchu; Tsiotras, Panagiotis* (2023). IEEE Robotics and Automation Letters, vol. 8, no. 11, pp. 7106-7113.

## TL;DR
Shield-MPPI: CBF cost terms plus a local repair (shield) of the MPPI solution to reduce constraint violations cheaply.

## Method
CBF-based cost and gradient-based local repair.

## Evidence
Aggressive racing sim and hardware.

## Relevance for Plan4ARI
Shows a cheap safety layer after MPPI.

## Abstract (verbatim, arXiv)
> Model Predictive Path Integral (MPPI) control is a type of sampling-based model predictive control that simulates thousands of trajectories and uses these trajectories to synthesize optimal controls on-the-fly. In practice, however, MPPI encounters problems limiting its application. For instance, it has been observed that MPPI tends to make poor decisions if unmodeled dynamics or environmental disturbances exist, preventing its use in safety-critical applications. Moreover, the multi-threaded simulations used by MPPI require significant onboard computational resources, making the algorithm inaccessible to robots without modern GPUs. To alleviate these issues, we propose a novel (Shield-MPPI) algorithm that provides robustness against unpredicted disturbances and achieves real-time planning using a much smaller number of parallel simulations on regular CPUs. The novel Shield-MPPI algorithm is tested on an aggressive autonomous racing platform both in simulation and using experiments. The results show that the proposed controller greatly reduces the number of constraint violations compared to state-of-the-art robust MPPI variants and stochastic MPC methods.

## Links
- [[concepts/constraints-and-safety]]
- BibTeX key: `yin2023shieldmppi` in `latex/references.bib`
