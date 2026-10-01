---
key: desai2026fpgampi
title: "Real-Time, Energy-Efficient, Sampling-Based Optimal Control via FPGA Acceleration"
authors: "Desai, Tanmay; Plancher, Brian; Bahar, R. Iris"
year: 2026
venue: "arXiv preprint arXiv:2601.17231"
arxiv: 2601.17231
doi: 
pdf: raw/papers/desai2026fpgampi.pdf
text: raw/text/desai2026fpgampi.txt
tags: [mobile, hardware]
status: summarised
---

# Real-Time, Energy-Efficient, Sampling-Based Optimal Control via FPGA Acceleration

*Desai, Tanmay; Plancher, Brian; Bahar, R. Iris* (2026). arXiv preprint arXiv:2601.17231.

## TL;DR
FPGA-optimised MPPI: deep pipelining; 3.1-7.5x faster and 2.5-5.4x less energy than embedded GPU/CPU.

## Method
FPGA architecture.

## Evidence
AMR benchmarks.

## Relevance for Plan4ARI
Deterministic, low-power MPPI for embedded industrial controllers.

## Abstract (verbatim, arXiv)
> Autonomous mobile robots (AMRs), used for search-and-rescue and remote exploration, require fast and robust planning and control schemes. Sampling-based approaches for Model Predictive Control, especially approaches based on the Model Predictive Path Integral Control (MPPI) algorithm, have recently proven both to be highly effective for such applications and to map naturally to GPUs for hardware acceleration. However, both GPU and CPU implementations of such algorithms can struggle to meet tight energy and latency budgets on battery-constrained AMR platforms that leverage embedded compute. To address this issue, we present an FPGA-optimized MPPI design that exposes fine-grained parallelism and eliminates synchronization bottlenecks via deep pipelining and parallelism across algorithmic stages. This results in an average 3.1x to 7.5x speedup over optimized implementations on an embedded GPU and CPU, respectively, while simultaneously achieving a 2.5x to 5.4x reduction in energy usage. These results demonstrate that FPGA architectures are a promising direction for energy-efficient and high-performance edge robotics.

## Links
- [[tools/software-ecosystem]]
- [[applications/mobile-robots-amr]]
- BibTeX key: `desai2026fpgampi` in `latex/references.bib`
