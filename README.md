# 5DMarkets
A path-dependent market state reconstruction framework inspired by UCLA 5DCT respiratory motion modeling.
5DMarkets is a physics-inspired framework for identifying when collective market computation diverges sufficiently from world-consistent capital allocation to allow strategic capital deployment that outperforms consensus.
Can a 5DCT-inspired latent state reconstruction framework outperform traditional time-series models by modeling path dependence and cross-asset state deformation?

## Abstract

Financial markets are traditionally modeled as point-in-time systems where future behavior is assumed to depend primarily on present observations. This assumption ignores path dependency, hysteresis, latent structural dynamics, and cross-asset deformation under systemic stress.

We propose a new computational framework inspired by five-dimensional computed tomography (5DCT), originally developed for respiratory motion modeling in radiation oncology.

In 5DCT, anatomical state is reconstructed continuously from sparse observations by modeling motion as a function of spatial position, breathing amplitude, and respiratory velocity.

We hypothesize that financial markets exhibit analogous behavior.

Specifically:

- identical present prices may correspond to distinct future probabilities depending on historical trajectory
- cross-asset relationships deform dynamically under macroeconomic stress
- hidden latent market states must be reconstructed from sparse noisy observations
- future market evolution depends on path-dependent state transition dynamics

We define a market evolution operator:

A_t = Π(Φ(G(H(M(R(O_t))))))

where:

R = latent state reconstruction  
M = market state manifold  
H = hysteresis memory operator  
G = cross-asset deformation field  
Φ = future state transition operator  
Π = portfolio optimization operator

This repository explores the mathematical foundations, implementation, and empirical validation of this framework.

---

Inspired by research by Dr. Low et al in medical physics, dynamical systems, and quantitative finance.

----
Update 6/30/26

# 5DMarkets

A physics-inspired machine learning architecture for modeling financial markets as dynamic state-transition systems under incomplete observation.

Inspired by the UCLA 5DCT respiratory motion reconstruction framework used in radiation oncology.

---

## Core Idea

Traditional quantitative finance models attempt to predict future prices directly.

5DMarkets proposes a different approach.

Instead of forecasting price, financial markets are modeled as partially observed dynamic systems whose future behavior depends on divergence between:

- The market's **current observed state**
- The market's **estimated equilibrium state**

Future market movement is assumed to be partially driven by correction toward equilibrium.

---

## Inspiration from UCLA 5DCT

This project is directly inspired by the UCLA 5DCT framework developed for respiratory motion modeling in medical physics.

In 5DCT:

- Sparse observations of respiratory motion are collected
- A deformation vector field models voxel-level anatomical motion
- Prior temporal trajectory constrains future motion reconstruction
- A motion model predicts plausible anatomical state transitions

5DMarkets transfers this architecture into financial systems.

Analogy:

| 5DCT (Medical Physics) | 5DMarkets (Finance) |
|------------------------|---------------------|
| CT observations | Market observations |
| Respiratory surrogate | Financial indicators |
| Deformation vector field | Cross-asset state propagation |
| Respiratory motion manifold | Market state manifold |
| Temporal respiratory hysteresis | Market path dependence |
| Anatomical state reconstruction | Market equilibrium reconstruction |

---

## Mathematical Framework

We define two market states.

Observed market state:

S_obs(t)

Current realized market configuration.

Estimated equilibrium state:

S_eq(t)

Estimated present equilibrium state representing where market should currently be if available information were fully reflected.

Market divergence:

Δ(t) = S_eq(t) - S_obs(t)

Future state transition depends partially on present disequilibrium:

S_future(t+1) = Φ(Δ(t), H_t, G_t)

where future market evolution is influenced by:

- Disequilibrium
- Historical path dependence
- Cross-asset propagation

---

## Architecture V2

The current architecture consists of the following operators.

O_t = observed market data

↓

R = Reconstruction Operator

Infer latent market representation from sparse observations.

↓

M = Market Manifold Operator

Project latent representation onto constrained market state manifold.

↓

P = Observed Projection Operator

Represent current observed market state directly.

↓

Ω = Divergence Operator

Compute divergence between equilibrium state and observed state.

Δ(t) = S_eq(t) - S_obs(t)

↓

H = Hysteresis Memory Operator

Incorporate temporal path dependence.

↓

G = Deformation Graph Operator

Propagate state deformation across coupled assets.

↓

Φ = Future Transition Operator

Predict next latent state transition.

↓

Π = Capital Allocation Operator

Convert predicted future state into portfolio allocation.

(Currently bypassed during training)

---

## Repository Structure

```text
5DMarkets/

research/
    architecture_v2.md

layers/
    (original NumPy architecture)

src_torch/

    layers/

        reconstruction.py

        market_manifold.py

        observed_projection.py

        divergence.py

        hysteresis_memory.py

        deformation_graph.py

        future_transition.py

        capital_allocator.py

    model.py

    test_model.py
```

---

## Current Development Status

Phase I — Architecture Design  
Completed

- Mathematical architecture defined
- Core operators implemented in NumPy

Phase II — PyTorch Rewrite  
Completed

- Full architecture rewritten in PyTorch
- Differentiable end-to-end model built
- Architecture successfully compiles

Phase III — Learning System  
In Progress

Current work:

- Define training objective
- Generate structured synthetic market data
- Train model on disequilibrium → future state prediction

Upcoming work:

- Sequence-based training pipeline
- Historical market data integration
- Contrastive manifold learning
- Asset-level allocation mapping
- Backtesting framework

---

## Current Research Question

Can future market movement be predicted by modeling divergence between:

- Current observed market state

and

- Estimated present equilibrium market state

while accounting for:

- temporal path dependence
- cross-asset propagation dynamics
- incomplete observation structure

---

## Why This Project Exists

Most quantitative finance models directly predict future price movement.

This project explores a different hypothesis.

Financial markets may be better understood as dynamic state-transition systems evolving under partial observation and disequilibrium correction.

The objective is not conventional forecasting.

The objective is to learn latent market structure.

---

## Technical Stack

Python

PyTorch

NumPy

Google Colab

GitHub

---

## Author

Louise Naumann

PhD Physics and Biology in Medicine  
UCLA

Research interests:

- Machine learning
- Dynamic systems modeling
- Quantitative finance
- Cross-disciplinary computational architectures
- Scientific machine learning

---

## Current Status

Architecture compiles successfully.

Training system under active development.

Research project in progress.