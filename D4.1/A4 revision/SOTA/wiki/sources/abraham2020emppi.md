---
key: abraham2020emppi
title: "Model-Based Generalization Under Parameter Uncertainty Using Path Integral Control"
authors: "Abraham, Ian; Handa, Ankur; Ratliff, Nathan; Lowrey, Kendall; Murphey, Todd D.; Fox, Dieter"
year: 2020
venue: "IEEE Robotics and Automation Letters, vol. 5, no. 2, pp. 2864-2871"
arxiv: 2006.03106
doi: 10.1109/LRA.2020.2972836
pdf: raw/papers/abraham2020emppi.pdf
text: raw/text/abraham2020emppi.txt
tags: [robustness, learning]
status: summarised
---

# Model-Based Generalization Under Parameter Uncertainty Using Path Integral Control

*Abraham, Ian; Handa, Ankur; Ratliff, Nathan; Lowrey, Kendall; Murphey, Todd D.; Fox, Dieter* (2020). IEEE Robotics and Automation Letters, vol. 5, no. 2, pp. 2864-2871.

## TL;DR
Ensemble MPPI: samples model parameters (domain randomisation) and adapts their distribution online for generalisation under parameter uncertainty.

## Method
Ensemble rollouts over parameters, risk-sensitive aggregation, online adaptation.

## Evidence
Simulated manipulation and locomotion.

## Relevance for Plan4ARI
Handles unknown payloads/friction in industrial tasks.

## Abstract (verbatim, arXiv)
> This work addresses the problem of robot interaction in complex environments where online control and adaptation is necessary. By expanding the sample space in the free energy formulation of path integral control, we derive a natural extension to the path integral control that embeds uncertainty into action and provides robustness for model-based robot planning. Our algorithm is applied to a diverse set of tasks using different robots and validate our results in simulation and real-world experiments. We further show that our method is capable of running in real-time without loss of performance. Videos of the experiments as well as additional implementation details can be found at https://sites.google.com/view/emppi.

## Links
- [[concepts/robustness-uncertainty]]
- BibTeX key: `abraham2020emppi` in `latex/references.bib`
