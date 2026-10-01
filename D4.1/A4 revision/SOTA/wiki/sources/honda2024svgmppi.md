---
key: honda2024svgmppi
title: "Stein Variational Guided Model Predictive Path Integral Control: Proposal and Experiments with Fast Maneuvering Vehicles"
authors: "Honda, Kohei; Akai, Naoki; Suzuki, Kosuke; Aoki, Mizuho; Hosogaya, Hirotaka; Okuda, Hiroyuki; Suzuki, Tatsuya"
year: 2024
venue: "Proc. IEEE Int. Conf. Robotics and Automation (ICRA), pp. 7020-7026"
arxiv: 2309.11040
doi: 10.1109/ICRA57147.2024.10611021
pdf: raw/papers/honda2024svgmppi.pdf
text: raw/text/honda2024svgmppi.txt
tags: [multimodal, mobile]
status: summarised
---

# Stein Variational Guided Model Predictive Path Integral Control: Proposal and Experiments with Fast Maneuvering Vehicles

*Honda, Kohei; Akai, Naoki; Suzuki, Kosuke; Aoki, Mizuho; Hosogaya, Hirotaka; Okuda, Hiroyuki; Suzuki, Tatsuya* (2024). Proc. IEEE Int. Conf. Robotics and Automation (ICRA), pp. 7020-7026.

## TL;DR
SVG-MPPI: SVGD identifies a target mode, MPPI then converges on that mode only (mode-seeking).

## Method
SVGD-guided proposal + MPPI.

## Evidence
Fast vehicle sim and real.

## Relevance for Plan4ARI
Avoids mode averaging while keeping MPPI speed.

## Abstract (verbatim, arXiv)
> This paper presents a novel Stochastic Optimal Control (SOC) method based on Model Predictive Path Integral control (MPPI), named Stein Variational Guided MPPI (SVG-MPPI), designed to handle rapidly shifting multimodal optimal action distributions. While MPPI can find a Gaussian-approximated optimal action distribution in closed form, i.e., without iterative solution updates, it struggles with the multimodality of the optimal distributions. This is due to the less representative nature of the Gaussian. To overcome this limitation, our method aims to identify a target mode of the optimal distribution and guide the solution to converge to fit it. In the proposed method, the target mode is roughly estimated using a modified Stein Variational Gradient Descent (SVGD) method and embedded into the MPPI algorithm to find a closed-form "mode-seeking" solution that covers only the target mode, thus preserving the fast convergence property of MPPI. Our simulation and real-world experimental results demonstrate that SVG-MPPI outperforms both the original MPPI and other state-of-the-art sampling-based SOC algorithms in terms of path-tracking and obstacle-avoidance capabilities. Source code: https://github.com/kohonda/proj-svg_mppi

## Links
- [[concepts/multimodality]]
- BibTeX key: `honda2024svgmppi` in `latex/references.bib`
