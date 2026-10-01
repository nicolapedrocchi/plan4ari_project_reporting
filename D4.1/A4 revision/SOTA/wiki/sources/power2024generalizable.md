---
key: power2024generalizable
title: "Learning a Generalizable Trajectory Sampling Distribution for Model Predictive Control"
authors: "Power, Thomas; Berenson, Dmitry"
year: 2024
venue: "IEEE Transactions on Robotics, vol. 40, pp. 2111-2127"
arxiv: 
doi: 10.1109/TRO.2024.3370026
pdf: raw/papers/power2024generalizable.pdf
text: raw/text/power2024generalizable.txt
tags: [learning, sampling, multimodal, manipulators, variational]
status: read
---

# Learning a Generalizable Trajectory Sampling Distribution for Model Predictive Control

*Power, Thomas; Berenson, Dmitry* (2024). IEEE Transactions on Robotics, vol. 40, pp. 2111-2127.

## TL;DR
Learns a **conditional normalising flow** q(U | start, goal, environment SDF, cost parameters) over whole control sequences and uses it as the proposal distribution of sampling-based MPC (FlowMPPI, FlowiCEM). For out-of-distribution (OOD) environments it **projects the environment embedding** towards the training distribution while keeping trajectory cost low in the true environment ("hallucinating" a familiar scene). Extended journal version of the authors' RSS 2022 paper.

## Method
- Control-as-inference / VI formulation; flow trained end-to-end with a VAE encoding of the SDF (§IV–V).
- FlowMPPI: half of the K samples are Gaussian perturbations of the shifted nominal (as MPPI), half come from the flow; all weighted as in MPPI (§V-D, Alg. 1). Running MPPI only in the flow latent space does not work (Fig. 3: no local improvement).
- The same flow works with MPPI and iCEM without retraining; the flow is conditioned on cost parameters ρ (control magnitude, smoothness, velocity).
- OOD projection: one gradient step per timestep on the environment embedding (§V-E).

## Evidence
- Systems (simulation): 2-D double integrator, 12-DoF quadrotor, 7-DoF kinematic manipulator; one real 7-DoF arm demonstration (Fig. 8). Budget 512 samples for all methods; training on 10k–20k random environments.
- Quadrotor, narrow-passage OOD environment: FlowMPPIProject 90% success vs iCEM 14% and MPPI 6% (§VI-F).
- Real-world-derived environments (stairway): FlowMPPIProject 58% vs iCEM 44%.
- 7-DoF manipulator, "fridge" environment from real data (Table V): FlowiCEMProject 97% vs iCEM 89% and SVMPC 44%.
- Flow-based methods are less smooth than iCEM (e.g. smoothness 4.26 vs 1.20, planar in-distribution) but reach lower cost.
- Limits stated by the authors (§VII): navigation-to-configuration tasks only; generalisation limits unknown; static environments; **projection too slow for real time in their Python implementation**; system-dependent hyper-parameters; needs an accurate dynamics model.

## Relevance for Plan4ARI
- Cited as ref. 10 in the Project Description ([[project/prj-plan4ari-proposal]]). **Citation check:** the proposal sentence describes MPC for aerial robots with learned penalties for coverage missions; the paper is instead about learned sampling distributions for collision-free navigation (double integrator, quadrotor, 7-DoF arm). The citation should be re-worded or replaced in D4.1.
- Technically it is the most mature example of a **learned, environment-conditioned, multimodal proposal for MPPI**, directly applicable to repetitive industrial cells (many similar scenes → training data). Fits the "learned proposals" branch of [[concepts/sampling-distributions]] and complements Biased-MPPI ([[sources/trevisan2024biasedmppi]]).

## Critical assessment (our view)
- The OOD projection is the key idea for industrial deployment (cells change), but its cost is incompatible with Core-IPC timing; for Plan4ARI it could run at Open-IPC rate.
- Training data could come from the Open-IPC sampling-based planner (paths in many cell variants), linking T4.2 and an MPPI layer.

## Links
- [[concepts/sampling-distributions]]
- [[concepts/learning-augmented-mppi]]
- [[concepts/multimodality]]
- [[comparisons/mppi-variants-matrix]]
- [[project/prj-plan4ari-proposal]]
- [[sources/sacks2023learningsampling]]
- [[sources/okada2020vimpc]]
- BibTeX key: `power2024generalizable` in `latex/references.bib`
