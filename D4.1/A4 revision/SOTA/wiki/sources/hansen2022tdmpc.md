---
key: hansen2022tdmpc
title: "Temporal Difference Learning for Model Predictive Control"
authors: "Hansen, Nicklas; Wang, Xiaolong; Su, Hao"
year: 2022
venue: "Proc. Int. Conf. Machine Learning (ICML), PMLR vol. 162"
arxiv: 2203.04955
doi: 
pdf: raw/papers/hansen2022tdmpc.pdf
text: raw/text/hansen2022tdmpc.txt
tags: [learning]
status: summarised
---

# Temporal Difference Learning for Model Predictive Control

*Hansen, Nicklas; Wang, Xiaolong; Su, Hao* (2022). Proc. Int. Conf. Machine Learning (ICML), PMLR vol. 162.

## TL;DR
TD-MPC: latent world model + TD-learned value; plans with MPPI in latent space.

## Method
Latent MPPI with learned terminal value.

## Evidence
DMControl, Meta-World.

## Relevance for Plan4ARI
Learning-based MPPI for long-horizon tasks.

## Abstract (verbatim, arXiv)
> Data-driven model predictive control has two key advantages over model-free methods: a potential for improved sample efficiency through model learning, and better performance as computational budget for planning increases. However, it is both costly to plan over long horizons and challenging to obtain an accurate model of the environment. In this work, we combine the strengths of model-free and model-based methods. We use a learned task-oriented latent dynamics model for local trajectory optimization over a short horizon, and use a learned terminal value function to estimate long-term return, both of which are learned jointly by temporal difference learning. Our method, TD-MPC, achieves superior sample efficiency and asymptotic performance over prior work on both state and image-based continuous control tasks from DMControl and Meta-World. Code and video results are available at https://nicklashansen.github.io/td-mpc.

## Links
- [[concepts/learning-augmented-mppi]]
- BibTeX key: `hansen2022tdmpc` in `latex/references.bib`
