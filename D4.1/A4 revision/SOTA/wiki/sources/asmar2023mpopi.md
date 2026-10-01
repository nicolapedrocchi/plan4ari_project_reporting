---
key: asmar2023mpopi
title: "Model Predictive Optimized Path Integral Strategies"
authors: "Asmar, Dylan M.; Senanayake, Ransalu; Manuel, Shawn; Kochenderfer, Mykel J."
year: 2023
venue: "Proc. IEEE Int. Conf. Robotics and Automation (ICRA), pp. 3182-3188"
arxiv: 2203.16633
doi: 10.1109/ICRA48891.2023.10160929
pdf: raw/papers/asmar2023mpopi.pdf
text: raw/text/asmar2023mpopi.txt
tags: [sampling]
status: summarised
---

# Model Predictive Optimized Path Integral Strategies

*Asmar, Dylan M.; Senanayake, Ransalu; Manuel, Shawn; Kochenderfer, Mykel J.* (2023). Proc. IEEE Int. Conf. Robotics and Automation (ICRA), pp. 3182-3188.

## TL;DR
MPOPI: adaptive importance sampling iterations within MPPI for better proposal.

## Method
Adaptive importance sampling / PMC iterations.

## Evidence
Simulated tasks.

## Relevance for Plan4ARI
Sample efficiency.

## Abstract (verbatim, arXiv)
> We generalize the derivation of model predictive path integral control (MPPI) to allow for a single joint distribution across controls in the control sequence. This reformation allows for the implementation of adaptive importance sampling (AIS) algorithms into the original importance sampling step while still maintaining the benefits of MPPI such as working with arbitrary system dynamics and cost functions. The benefit of optimizing the proposal distribution by integrating AIS at each control step is demonstrated in simulated environments including controlling multiple cars around a track. The new algorithm is more sample efficient than MPPI, achieving better performance with fewer samples. This performance disparity grows as the dimension of the action space increases. Results from simulations suggest the new algorithm can be used as an anytime algorithm, increasing the value of control at each iteration versus relying on a large set of samples.

## Links
- [[concepts/sampling-distributions]]
- BibTeX key: `asmar2023mpopi` in `latex/references.bib`
