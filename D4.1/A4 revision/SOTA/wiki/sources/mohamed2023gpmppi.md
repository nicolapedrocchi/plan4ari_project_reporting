---
key: mohamed2023gpmppi
title: "GP-guided MPPI for Efficient Navigation in Complex Unknown Cluttered Environments"
authors: "Mohamed, Ihab S.; Ali, Mahmoud; Liu, Lantao"
year: 2023
venue: "Proc. IEEE/RSJ Int. Conf. Intelligent Robots and Systems (IROS), pp. 7463-7470"
arxiv: 2307.04019
doi: 10.1109/IROS55552.2023.10341382
pdf: raw/papers/mohamed2023gpmppi.pdf
text: raw/text/mohamed2023gpmppi.txt
tags: [mobile, guidance]
status: summarised
---

# GP-guided MPPI for Efficient Navigation in Complex Unknown Cluttered Environments

*Mohamed, Ihab S.; Ali, Mahmoud; Liu, Lantao* (2023). Proc. IEEE/RSJ Int. Conf. Intelligent Robots and Systems (IROS), pp. 7463-7470.

## TL;DR
GP-MPPI: sparse Gaussian process perception model proposes subgoals to MPPI beyond its horizon.

## Method
SGP variance surface, subgoal selection.

## Evidence
Simulated and real navigation.

## Relevance for Plan4ARI
Local-global coupling for AMRs without a global map.

## Abstract (verbatim, arXiv)
> Robotic navigation in unknown, cluttered environments with limited sensing capabilities poses significant challenges in robotics. Local trajectory optimization methods, such as Model Predictive Path Intergal (MPPI), are a promising solution to this challenge. However, global guidance is required to ensure effective navigation, especially when encountering challenging environmental conditions or navigating beyond the planning horizon. This study presents the GP-MPPI, an online learning-based control strategy that integrates MPPI with a local perception model based on Sparse Gaussian Process (SGP). The key idea is to leverage the learning capability of SGP to construct a variance (uncertainty) surface, which enables the robot to learn about the navigable space surrounding it, identify a set of suggested subgoals, and ultimately recommend the optimal subgoal that minimizes a predefined cost function to the local MPPI planner. Afterward, MPPI computes the optimal control sequence that satisfies the robot and collision avoidance constraints. Such an approach eliminates the necessity of a global map of the environment or an offline training process. We validate the efficiency and robustness of our proposed control strategy through both simulated and real-world experiments of 2D autonomous navigation tasks in complex unknown environments, demonstrating its superiority in guiding the robot safely towards its desired goal while avoiding obstacles and escaping entrapment in local minima. The GPU implementation of GP-MPPI, including the supplementary video, is available at https://github.com/IhabMohamed/GP-MPPI.

## Links
- [[applications/mobile-robots-amr]]
- [[concepts/sampling-distributions]]
- BibTeX key: `mohamed2023gpmppi` in `latex/references.bib`
