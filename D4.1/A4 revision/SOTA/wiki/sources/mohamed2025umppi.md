---
key: mohamed2025umppi
title: "Towards Efficient MPPI Trajectory Generation with Unscented Guidance: U-MPPI Control Strategy"
authors: "Mohamed, Ihab S.; Xu, Junhong; Sukhatme, Gaurav S; Liu, Lantao"
year: 2025
venue: "IEEE Transactions on Robotics, vol. 41, pp. 1172-1192"
arxiv: 2306.12369
doi: 10.1109/TRO.2025.3526078
pdf: raw/papers/mohamed2025umppi.pdf
text: raw/text/mohamed2025umppi.txt
tags: [robustness, mobile, safety]
status: summarised
---

# Towards Efficient MPPI Trajectory Generation with Unscented Guidance: U-MPPI Control Strategy

*Mohamed, Ihab S.; Xu, Junhong; Sukhatme, Gaurav S; Liu, Lantao* (2025). IEEE Transactions on Robotics, vol. 41, pp. 1172-1192.

## TL;DR
U-MPPI: propagates mean and covariance with the unscented transform; risk-sensitive cost and better exploration.

## Method
Unscented transform sampling, risk-sensitive cost.

## Evidence
Simulated and real autonomous navigation.

## Relevance for Plan4ARI
Uncertainty-aware AMR navigation.

## Abstract (verbatim, arXiv)
> The classical Model Predictive Path Integral (MPPI) control framework, while effective in many applications, lacks reliable safety features due to its reliance on a risk-neutral trajectory evaluation technique, which can present challenges for safety-critical applications such as autonomous driving. Furthermore, when the majority of MPPI sampled trajectories concentrate in high-cost regions, it may generate an infeasible control sequence. To address this challenge, we propose the U-MPPI control strategy, a novel methodology that can effectively manage system uncertainties while integrating a more efficient trajectory sampling strategy. The core concept is to leverage the Unscented Transform (UT) to propagate not only the mean but also the covariance of the system dynamics, going beyond the traditional MPPI method. As a result, it introduces a novel and more efficient trajectory sampling strategy, significantly enhancing state-space exploration and ultimately reducing the risk of being trapped in local minima. Furthermore, by leveraging the uncertainty information provided by UT, we incorporate a risk-sensitive cost function that explicitly accounts for risk or uncertainty throughout the trajectory evaluation process, resulting in a more resilient control system capable of handling uncertain conditions. By conducting extensive simulations of 2D aggressive autonomous navigation in both known and unknown cluttered environments, we verify the efficiency and robustness of our proposed U-MPPI control strategy compared to the baseline MPPI. We further validate the practicality of U-MPPI through real-world demonstrations in unknown cluttered environments, showcasing its superior ability to incorporate both the UT and local costmap into the optimization problem without introducing additional complexity.

## Links
- [[concepts/robustness-uncertainty]]
- [[applications/mobile-robots-amr]]
- BibTeX key: `mohamed2025umppi` in `latex/references.bib`
