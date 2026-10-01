---
key: jansma2023interaction
title: "Interaction-Aware Sampling-Based MPC with Learned Local Goal Predictions"
authors: "Jansma, Walter; Trevisan, Elia; Serra-Gomez, Alvaro; Alonso-Mora, Javier"
year: 2023
venue: "Proc. Int. Symp. Multi-Robot and Multi-Agent Systems (MRS), pp. 15-21"
arxiv: 2309.14931
doi: 10.1109/MRS60187.2023.10416788
pdf: raw/papers/jansma2023interaction.pdf
text: raw/text/jansma2023interaction.txt
tags: [mobile, multi-agent]
status: summarised
---

# Interaction-Aware Sampling-Based MPC with Learned Local Goal Predictions

*Jansma, Walter; Trevisan, Elia; Serra-Gomez, Alvaro; Alonso-Mora, Javier* (2023). Proc. Int. Symp. Multi-Robot and Multi-Agent Systems (MRS), pp. 15-21.

## TL;DR
Interaction-aware sampling-based MPC with learned local-goal predictions of other agents.

## Method
MPPI + learned goal prediction.

## Evidence
Simulated multi-agent navigation scenarios.

## Relevance for Plan4ARI
Fleet / human interaction for AMRs.

## Abstract (verbatim, arXiv)
> Motion planning for autonomous robots in tight, interaction-rich, and mixed human-robot environments is challenging. State-of-the-art methods typically separate prediction and planning, predicting other agents' trajectories first and then planning the ego agent's motion in the remaining free space. However, agents' lack of awareness of their influence on others can lead to the freezing robot problem. We build upon Interaction-Aware Model Predictive Path Integral (IA-MPPI) control and combine it with learning-based trajectory predictions, thereby relaxing its reliance on communicated short-term goals for other agents. We apply this framework to Autonomous Surface Vessels (ASVs) navigating urban canals. By generating an artificial dataset in real sections of Amsterdam's canals, adapting and training a prediction model for our domain, and proposing heuristics to extract local goals, we enable effective cooperation in planning. Our approach improves autonomous robot navigation in complex, crowded environments, with potential implications for multi-agent systems and human-robot interaction.

## Links
- [[applications/mobile-robots-amr]]
- [[applications/human-robot-shared-spaces]]
- BibTeX key: `jansma2023interaction` in `latex/references.bib`
