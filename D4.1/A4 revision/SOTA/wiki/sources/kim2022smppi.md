---
key: kim2022smppi
title: "Smooth Model Predictive Path Integral Control without Smoothing"
authors: "Kim, Taekyung; Park, Gyuhyun; Kwak, Kiho; Bae, Jihwan; Lee, Wonsuk"
year: 2022
venue: "IEEE Robotics and Automation Letters, vol. 7, no. 4, pp. 10406-10413"
arxiv: 2112.09988
doi: 10.1109/LRA.2022.3192800
pdf: raw/papers/kim2022smppi.pdf
text: raw/text/kim2022smppi.txt
tags: [smoothness]
status: summarised
---

# Smooth Model Predictive Path Integral Control without Smoothing

*Kim, Taekyung; Park, Gyuhyun; Kwak, Kiho; Bae, Jihwan; Lee, Wonsuk* (2022). IEEE Robotics and Automation Letters, vol. 7, no. 4, pp. 10406-10413.

## TL;DR
Smooth-MPPI: samples in the derivative-action space (input lifting) to obtain smooth commands without post-hoc smoothing.

## Method
Action-derivative sampling with smoothness cost.

## Evidence
Pendulum, autonomous driving with NN dynamics.

## Relevance for Plan4ARI
Smooth references are mandatory for industrial axes.

## Abstract (verbatim, arXiv)
> We present a sampling-based control approach that can generate smooth actions for general nonlinear systems without external smoothing algorithms. Model Predictive Path Integral (MPPI) control has been utilized in numerous robotic applications due to its appealing characteristics to solve non-convex optimization problems. However, the stochastic nature of sampling-based methods can cause significant chattering in the resulting commands. Chattering becomes more prominent in cases where the environment changes rapidly, possibly even causing the MPPI to diverge. To address this issue, we propose a method that seamlessly combines MPPI with an input-lifting strategy. In addition, we introduce a new action cost to smooth control sequence during trajectory rollouts while preserving the information theoretic interpretation of MPPI, which was derived from non-affine dynamics. We validate our method in two nonlinear control tasks with neural network dynamics: a pendulum swing-up task and a challenging autonomous driving task. The experimental results demonstrate that our method outperforms the MPPI baselines with additionally applied smoothing algorithms.

## Links
- [[concepts/smoothness-action-parametrization]]
- BibTeX key: `kim2022smppi` in `latex/references.bib`
