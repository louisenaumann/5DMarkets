# Simulation 1 Design

Objective:

Test whether 5DMarkets produces coherent market evolution behavior in a minimal artificial market.

------------------------------------------------------------
SIMULATION WORLD
------------------------------------------------------------

Five assets:

A1 = Pharma

A2 = Energy

A3 = Technology

A4 = Consumer Goods

A5 = Treasury

Total capital:

K_global = 1000

Capital conserved:

Σ C_i(t) = 1000

------------------------------------------------------------
WORLD STATE
------------------------------------------------------------

Define objective attractiveness state:

W(t)

Example:

W(0) = [0.8,0.4,0.6,0.5,0.2]

------------------------------------------------------------
IDEAL COMPUTATION
------------------------------------------------------------

Perfect rational allocation:

C*(t)

=

1000 × W_i / ΣW_i

Example:

C*(0)

=

[320,160,240,200,80]

------------------------------------------------------------
OBSERVED COMPUTATION
------------------------------------------------------------

Agents compute imperfectly.

Observed world state:

Ŵ(t)

Example:

Ŵ(0)

=

[0.7,0.6,0.4,0.5,0.3]

Target allocation:

Ĉ(t)

------------------------------------------------------------
CAPITAL MOVEMENT
------------------------------------------------------------

Capital moves gradually toward perceived target.

dC_i/dt

=

α(Ĉ_i(t) - C_i(t))

------------------------------------------------------------
PRICE EMERGENCE
------------------------------------------------------------

Price depends on capital concentration and liquidity.

P_i(t)

=

C_i(t)/L_i

where

L_i = asset liquidity

------------------------------------------------------------
OBSERVATIONS
------------------------------------------------------------

Measure divergence:

Δ(t)

=

Σ|C*_i(t) - C_i(t)|

Measure price lag.

Measure impact of observer error.

Measure convergence toward ideal allocation state.