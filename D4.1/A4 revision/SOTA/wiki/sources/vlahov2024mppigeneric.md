---
key: vlahov2024mppigeneric
title: "MPPI-Generic: A CUDA Library for Stochastic Trajectory Optimization"
authors: "Vlahov, Bogdan; Gibson, Jason; Gandhi, Manan; Theodorou, Evangelos A."
year: 2024
venue: "arXiv preprint arXiv:2409.07563"
arxiv: 2409.07563
doi: 
pdf: raw/papers/vlahov2024mppigeneric.pdf
text: raw/text/vlahov2024mppigeneric.txt
tags: [software, gpu]
status: summarised
---

# MPPI-Generic: A CUDA Library for Stochastic Trajectory Optimization

*Vlahov, Bogdan; Gibson, Jason; Gandhi, Manan; Theodorou, Evangelos A.* (2024). arXiv preprint arXiv:2409.07563.

## TL;DR
MPPI-Generic: header-only CUDA C++ library for MPPI, Tube-MPPI, RMPPI with plug-in dynamics and costs.

## Method
Software library.

## Evidence
Timing benchmarks vs other implementations.

## Relevance for Plan4ARI
Candidate production-grade backend.

## Abstract (verbatim, arXiv)
> This paper introduces a new C++/CUDA library for GPU-accelerated stochastic optimization called MPPI-Generic. It provides implementations of Model Predictive Path Integral control, Tube-Model Predictive Path Integral Control, and Robust Model Predictive Path Integral Control, and allows for these algorithms to be used across many pre-existing dynamics models and cost functions. Furthermore, researchers can create their own dynamics models or cost functions following our API definitions without needing to change the actual Model Predictive Path Integral Control code. Finally, we compare computational performance to other popular implementations of Model Predictive Path Integral Control over a variety of GPUs to show the real-time capabilities our library can allow for. Library code can be found at: https://acdslab.github.io/mppi-generic-website/ .

## Links
- [[tools/software-ecosystem]]
- BibTeX key: `vlahov2024mppigeneric` in `latex/references.bib`
