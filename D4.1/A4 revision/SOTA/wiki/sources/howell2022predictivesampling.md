---
key: howell2022predictivesampling
title: "Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo"
authors: "Howell, Taylor; Gileadi, Nimrod; Tunyasuvunakool, Saran; Zakka, Kevin; Erez, Tom; Tassa, Yuval"
year: 2022
venue: "arXiv preprint arXiv:2212.00541"
arxiv: 2212.00541
doi: 
pdf: raw/papers/howell2022predictivesampling.pdf
text: raw/text/howell2022predictivesampling.txt
tags: [sampling, software, simulator]
status: summarised
---

# Predictive Sampling: Real-time Behaviour Synthesis with MuJoCo

*Howell, Taylor; Gileadi, Nimrod; Tunyasuvunakool, Saran; Zakka, Kevin; Erez, Tom; Tassa, Yuval* (2022). arXiv preprint arXiv:2212.00541.

## TL;DR
Predictive Sampling in MuJoCo MPC (MJPC): very simple best-sample sampling MPC is competitive with iLQG when using the physics engine as model.

## Method
Spline-parametrised sampling, keep best rollout.

## Evidence
Many MuJoCo tasks in real time.

## Relevance for Plan4ARI
Shows simulator-in-the-loop sampling MPC is viable; MJPC is a ready tool.

## Abstract (verbatim, arXiv)
> We introduce MuJoCo MPC (MJPC), an open-source, interactive application and software framework for real-time predictive control, based on MuJoCo physics. MJPC allows the user to easily author and solve complex robotics tasks, and currently supports three shooting-based planners: derivative-based iLQG and Gradient Descent, and a simple derivative-free method we call Predictive Sampling. Predictive Sampling was designed as an elementary baseline, mostly for its pedagogical value, but turned out to be surprisingly competitive with the more established algorithms. This work does not present algorithmic advances, and instead, prioritises performant algorithms, simple code, and accessibility of model-based methods via intuitive and interactive software. MJPC is available at: github.com/deepmind/mujoco_mpc, a video summary can be viewed at: dpmd.ai/mjpc.

## Links
- [[concepts/physics-simulator-rollouts]]
- [[tools/software-ecosystem]]
- [[concepts/mppi-vs-mpc]]
- BibTeX key: `howell2022predictivesampling` in `latex/references.bib`
