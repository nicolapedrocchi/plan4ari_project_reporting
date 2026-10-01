---
key: pan2024mbd
title: "Model-Based Diffusion for Trajectory Optimization"
authors: "Pan, Chaoyi; Yi, Zeji; Shi, Guanya; Qu, Guannan"
year: 2024
venue: "Advances in Neural Information Processing Systems (NeurIPS), vol. 37, pp. 57914-57943"
arxiv: 2407.01573
doi: 
pdf: raw/papers/pan2024mbd.pdf
text: raw/text/pan2024mbd.txt
tags: [diffusion]
status: summarised
---

# Model-Based Diffusion for Trajectory Optimization

*Pan, Chaoyi; Yi, Zeji; Shi, Guanya; Qu, Guannan* (2024). Advances in Neural Information Processing Systems (NeurIPS), vol. 37, pp. 57914-57943.

## TL;DR
Model-based diffusion: trajectory optimisation as score-based denoising using the model, no data needed.

## Method
Monte-Carlo score estimation.

## Evidence
Simulated tasks.

## Relevance for Plan4ARI
Theoretical link MPPI <-> diffusion.

## Abstract (verbatim, arXiv)
> Recent advances in diffusion models have demonstrated their strong capabilities in generating high-fidelity samples from complex distributions through an iterative refinement process. Despite the empirical success of diffusion models in motion planning and control, the model-free nature of these methods does not leverage readily available model information and limits their generalization to new scenarios beyond the training data (e.g., new robots with different dynamics). In this work, we introduce Model-Based Diffusion (MBD), an optimization approach using the diffusion process to solve trajectory optimization (TO) problems without data. The key idea is to explicitly compute the score function by leveraging the model information in TO problems, which is why we refer to our approach as model-based diffusion. Moreover, although MBD does not require external data, it can be naturally integrated with data of diverse qualities to steer the diffusion process. We also reveal that MBD has interesting connections to sampling-based optimization. Empirical evaluations show that MBD outperforms state-of-the-art reinforcement learning and sampling-based TO methods in challenging contact-rich tasks. Additionally, MBD's ability to integrate with data enhances its versatility and practical applicability, even with imperfect and infeasible data (e.g., partial-state demonstrations for high-dimensional humanoids), beyond the scope of standard diffusion models.

## Links
- [[concepts/sampling-distributions]]
- BibTeX key: `pan2024mbd` in `latex/references.bib`
