---
key: sundaralingam2023curobo
title: "cuRobo: Parallelized Collision-Free Robot Motion Generation"
authors: "Sundaralingam, Balakumar; Hari, Siva Kumar Sastry; Fishman, Adam; Garrett, Caelan; Wyk, Karl Van; Blukis, Valts; Millane, Alexander; Oleynikova, Helen; Handa, Ankur; Ramos, Fabio; Ratliff, Nathan; Fox, Dieter"
year: 2023
venue: "Proc. IEEE Int. Conf. Robotics and Automation (ICRA), pp. 8112-8119"
arxiv: 2310.17274
doi: 10.1109/ICRA48891.2023.10160765
pdf: raw/papers/sundaralingam2023curobo.pdf
text: raw/text/sundaralingam2023curobo.txt
tags: [manipulators, gpu, software, hybrid]
status: summarised
---

# cuRobo: Parallelized Collision-Free Robot Motion Generation

*Sundaralingam, Balakumar; Hari, Siva Kumar Sastry; Fishman, Adam; Garrett, Caelan; Wyk, Karl Van; Blukis, Valts; Millane, Alexander; Oleynikova, Helen; Handa, Ankur; Ramos, Fabio; Ratliff, Nathan; Fox, Dieter* (2023). Proc. IEEE Int. Conf. Robotics and Automation (ICRA), pp. 8112-8119.

## TL;DR
cuRobo: GPU-parallel collision-free motion generation: parallel IK, geometric planner, particle-based (MPPI-like) seeding + L-BFGS; ~30-50 ms per plan.

## Method
Batched particle optimisation + L-BFGS with parallel line search.

## Evidence
Benchmarks vs SOTA planners; real robots.

## Relevance for Plan4ARI
Industrial-grade GPU motion generation; hybrid sampling+gradient.

## Abstract (verbatim, arXiv)
> This paper explores the problem of collision-free motion generation for manipulators by formulating it as a global motion optimization problem. We develop a parallel optimization technique to solve this problem and demonstrate its effectiveness on massively parallel GPUs. We show that combining simple optimization techniques with many parallel seeds leads to solving difficult motion generation problems within 50ms on average, 60x faster than state-of-the-art (SOTA) trajectory optimization methods. We achieve SOTA performance by combining L-BFGS step direction estimation with a novel parallel noisy line search scheme and a particle-based optimization solver. To further aid trajectory optimization, we develop a parallel geometric planner that plans within 20ms and also introduce a collision-free IK solver that can solve over 7000 queries/s. We package our contributions into a state of the art GPU accelerated motion generation library, cuRobo and release it to enrich the robotics community. Additional details are available at https://curobo.org

## Links
- [[applications/industrial-manipulators]]
- [[concepts/hybrid-gradient-sampling]]
- [[tools/software-ecosystem]]
- BibTeX key: `sundaralingam2023curobo` in `latex/references.bib`
