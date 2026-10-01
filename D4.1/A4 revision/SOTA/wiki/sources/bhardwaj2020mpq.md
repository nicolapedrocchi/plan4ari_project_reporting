---
key: bhardwaj2020mpq
title: "Information Theoretic Model Predictive Q-Learning"
authors: "Bhardwaj, Mohak; Handa, Ankur; Fox, Dieter; Boots, Byron"
year: 2020
venue: "Proc. Learning for Dynamics and Control (L4DC), PMLR vol. 120"
arxiv: 2001.02153
doi: 
pdf: raw/papers/bhardwaj2020mpq.pdf
text: raw/text/bhardwaj2020mpq.txt
tags: [learning]
status: summarised
---

# Information Theoretic Model Predictive Q-Learning

*Bhardwaj, Mohak; Handa, Ankur; Fox, Dieter; Boots, Byron* (2020). Proc. Learning for Dynamics and Control (L4DC), PMLR vol. 120.

## TL;DR
MPQ: information-theoretic MPC combined with soft Q-learning; MPPI with learned terminal Q.

## Method
Soft Q terminal cost.

## Evidence
Simulated manipulation and control.

## Relevance for Plan4ARI
Theory of MPC + RL combination.

## Abstract (verbatim, arXiv)
> Model-free Reinforcement Learning (RL) works well when experience can be collected cheaply and model-based RL is effective when system dynamics can be modeled accurately. However, both assumptions can be violated in real world problems such as robotics, where querying the system can be expensive and real-world dynamics can be difficult to model. In contrast to RL, Model Predictive Control (MPC) algorithms use a simulator to optimize a simple policy class online, constructing a closed-loop controller that can effectively contend with real-world dynamics. MPC performance is usually limited by factors such as model bias and the limited horizon of optimization. In this work, we present a novel theoretical connection between information theoretic MPC and entropy regularized RL and develop a Q-learning algorithm that can leverage biased models. We validate the proposed algorithm on sim-to-sim control tasks to demonstrate the improvements over optimal control and reinforcement learning from scratch. Our approach paves the way for deploying reinforcement learning algorithms on real systems in a systematic manner.

## Links
- [[concepts/learning-augmented-mppi]]
- BibTeX key: `bhardwaj2020mpq` in `latex/references.bib`
