---
key: aoyama2026hybrid
title: "Beyond Pure Sampling: Hybrid Optimization Mechanisms for Non-Convex Model Predictive Control"
authors: "Aoyama, Yuichiro; Jung, Minchan; Ratheesh, Akash; Theodorou, Evangelos A."
year: 2026
venue: "arXiv preprint arXiv:2606.00737"
arxiv: 2606.00737
doi: 
pdf: raw/papers/aoyama2026hybrid.pdf
text: raw/text/aoyama2026hybrid.txt
tags: [hybrid, ddp]
status: summarised
---

# Beyond Pure Sampling: Hybrid Optimization Mechanisms for Non-Convex Model Predictive Control

*Aoyama, Yuichiro; Jung, Minchan; Ratheesh, Akash; Theodorou, Evangelos A.* (2026). arXiv preprint arXiv:2606.00737.

## TL;DR
ME-DDP: alternates DDP gradient steps with sampling from inverse-Hessian policies (unimodal, multimodal, Stein) to escape local minima; benchmarked against MPPI.

## Method
Maximum-entropy DDP variants.

## Evidence
Navigation of four robotic systems in clutter.

## Relevance for Plan4ARI
Evidence for gradient+sampling hybrids.

## Abstract (verbatim, arXiv)
> This paper investigates the optimization mechanisms of non-convex Model Predictive Control (MPC) using the Maximum Entropy Differential Dynamic Programming (ME-DDP) framework. Navigating non-convex cost landscapes induced by nonlinear dynamics, multiple obstacles, etc. remains a fundamental challenge in robotics, where gradient-based methods frequently converge to suboptimal local minima. We demonstrate a dual-step optimization mechanism designed to overcome these traps. (1) an initial phase of using DDP to exploit the gradient of the cost landscape, followed by (2) disruption of the optimization via sampling from policies characterized by the inverse Hessian of the action-value function. We provide a rigorous analysis of this sampling mechanism of three ME-DDP variants: Unimodal Gaussian ME-DDP, Multimodal Gaussian ME-DDP, and Stein Variational DDP. Furthermore, with navigation tasks of four robotic systems under cluttered environments, we conduct extensive benchmarking of three variants of the ME-DDP, against deterministic DDP, and one of the most successful sampling-based schemes, Model Predictive Path Integral (MPPI) control with three policy parameterizations and update laws that correspond to those of ME-DDPs. The results show that in low-dimensional systems where the cost landscapes are relatively simple and local information is sufficiently representative, our framework consistently outperforms MPPIs. In high-dimensional systems, MPPI can occasionally discover aggressive maneuvers that enable it to steer the systems faster than DDP-based methods, whereas our method maintains a higher, more stable success rate. Finally, we validate the practical efficacy of the framework through hardware experiments with a quadrotor navigating a dense, non-convex obstacle field, confirming the robustness of the proposed framework for real-world deployment.

## Links
- [[concepts/hybrid-gradient-sampling]]
- [[concepts/mppi-vs-mpc]]
- BibTeX key: `aoyama2026hybrid` in `latex/references.bib`
