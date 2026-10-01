---
key: makoviychuk2021isaacgym
title: "Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning"
authors: "Makoviychuk, Viktor; Wawrzyniak, Lukasz; Guo, Yunrong; Lu, Michelle; Storey, Kier; Macklin, Miles; Hoeller, David; Rudin, Nikita; Allshire, Arthur; Handa, Ankur; State, Gavriel"
year: 2021
venue: "arXiv preprint arXiv:2108.10470"
arxiv: 2108.10470
doi: 
pdf: raw/papers/makoviychuk2021isaacgym.pdf
text: raw/text/makoviychuk2021isaacgym.txt
tags: [simulator, software]
status: summarised
---

# Isaac Gym: High Performance GPU-Based Physics Simulation For Robot Learning

*Makoviychuk, Viktor; Wawrzyniak, Lukasz; Guo, Yunrong; Lu, Michelle; Storey, Kier; Macklin, Miles; Hoeller, David; Rudin, Nikita; Allshire, Arthur; Handa, Ankur; State, Gavriel* (2021). arXiv preprint arXiv:2108.10470.

## TL;DR
Isaac Gym: GPU physics simulation with tensor API for thousands of parallel environments.

## Method
Software.

## Evidence
RL benchmarks.

## Relevance for Plan4ARI
Rollout engine for Pezzato et al. / M3P2I.

## Abstract (verbatim, arXiv)
> Isaac Gym offers a high performance learning platform to train policies for wide variety of robotics tasks directly on GPU. Both physics simulation and the neural network policy training reside on GPU and communicate by directly passing data from physics buffers to PyTorch tensors without ever going through any CPU bottlenecks. This leads to blazing fast training times for complex robotics tasks on a single GPU with 2-3 orders of magnitude improvements compared to conventional RL training that uses a CPU based simulator and GPU for neural networks. We host the results and videos at \url{https://sites.google.com/view/isaacgym-nvidia} and isaac gym can be downloaded at \url{https://developer.nvidia.com/isaac-gym}.

## Links
- [[concepts/physics-simulator-rollouts]]
- [[tools/software-ecosystem]]
- BibTeX key: `makoviychuk2021isaacgym` in `latex/references.bib`
