# Agent Computation Model

The market consists of heterogeneous agents computing capital allocation independently.

Each agent possesses imperfect information and internal decision variability.

------------------------------------------------------------
AGENT WORLD ESTIMATION
------------------------------------------------------------

Each agent k estimates world state.

Define:

Ŵ_k(t)

=

W(t)

+

ε_I(k,t)

+

ε_H(k,t)

where

ε_I(k,t)

=

information visibility error

ε_H(k,t)

=

internal human decision variability

------------------------------------------------------------
INFORMATION ERROR
------------------------------------------------------------

Agents possess incomplete information.

Different agents observe different subsets of world state.

Examples:

Retail investors observe public news.

Institutions possess proprietary research.

Algorithms observe price and options flow only.

------------------------------------------------------------
HUMAN DECISION ERROR
------------------------------------------------------------

Agents with identical information may compute differently.

Sources include:

Temporary risk tolerance changes

Emotional overreaction

Behavioral bias

Overconfidence

Defensive positioning after prior losses

------------------------------------------------------------
CAPITAL ALLOCATION DECISION
------------------------------------------------------------

Each agent computes allocation independently.

Define:

Ĉ_k(t)

=

F(Ŵ_k(t))

Aggregate market allocation emerges from all agent decisions.

------------------------------------------------------------
CORE PRINCIPLE
------------------------------------------------------------

The overall market behaves deterministically at system scale.

Individual agents behave imperfectly at local scale.

Global market behavior emerges from aggregation of imperfect local computation.