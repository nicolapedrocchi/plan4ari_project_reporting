---
key: lowrey2019polo
title: "Plan Online, Learn Offline: Efficient Learning and Exploration via Model-Based Control"
authors: "Lowrey, Kendall; Rajeswaran, Aravind; Kakade, Sham; Todorov, Emanuel; Mordatch, Igor"
year: 2019
venue: "Proc. Int. Conf. Learning Representations (ICLR)"
arxiv: 1811.01848
doi: 
pdf: raw/papers/lowrey2019polo.pdf
text: raw/text/lowrey2019polo.txt
tags: [learning]
status: summarised
---

# Plan Online, Learn Offline: Efficient Learning and Exploration via Model-Based Control

*Lowrey, Kendall; Rajeswaran, Aravind; Kakade, Sham; Todorov, Emanuel; Mordatch, Igor* (2019). Proc. Int. Conf. Learning Representations (ICLR).

## TL;DR
POLO: MPPI planning with learned value function as terminal cost and optimistic exploration.

## Method
MPPI + value ensemble.

## Evidence
Humanoid, hand manipulation sims.

## Relevance for Plan4ARI
Terminal value extends short horizons.

## Abstract (verbatim, arXiv)
> We propose a plan online and learn offline (POLO) framework for the setting where an agent, with an internal model, needs to continually act and learn in the world. Our work builds on the synergistic relationship between local model-based control, global value function learning, and exploration. We study how local trajectory optimization can cope with approximation errors in the value function, and can stabilize and accelerate value function learning. Conversely, we also study how approximate value functions can help reduce the planning horizon and allow for better policies beyond local solutions. Finally, we also demonstrate how trajectory optimization can be used to perform temporally coordinated exploration in conjunction with estimating uncertainty in value function approximation. This exploration is critical for fast and stable learning of the value function. Combining these components enable solutions to complex simulated control tasks, like humanoid locomotion and dexterous in-hand manipulation, in the equivalent of a few minutes of experience in the real world.

## Links
- [[concepts/learning-augmented-mppi]]
- BibTeX key: `lowrey2019polo` in `latex/references.bib`
