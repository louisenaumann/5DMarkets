import numpy as np
import matplotlib.pyplot as plt


# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

NUM_ASSETS = 5
NUM_AGENTS = 100
CAPITAL_PER_AGENT = 10
TIMESTEPS = 50

INFO_ERROR_STD = 0.15
HUMAN_ERROR_STD = 0.05


# --------------------------------------------------
# WORLD STATE
# --------------------------------------------------

# Objective world attractiveness
W = np.array([0.8, 0.4, 0.6, 0.5, 0.2])


# --------------------------------------------------
# IDEAL ALLOCATION
# --------------------------------------------------

def ideal_allocation(world_state):

    total_capital = NUM_AGENTS * CAPITAL_PER_AGENT

    weights = world_state / np.sum(world_state)

    return total_capital * weights


# --------------------------------------------------
# AGENT COMPUTATION
# --------------------------------------------------

def agent_estimate(world_state):

    # Information visibility error
    info_error = np.random.normal(
        0,
        INFO_ERROR_STD,
        NUM_ASSETS
    )

    # Human decision error
    human_error = np.random.normal(
        0,
        HUMAN_ERROR_STD,
        NUM_ASSETS
    )

    estimate = world_state + info_error + human_error

    estimate = np.clip(estimate, 0.01, None)

    return estimate


# --------------------------------------------------
# AGENT CAPITAL ALLOCATION
# --------------------------------------------------

def agent_allocate(estimated_world):

    weights = estimated_world / np.sum(estimated_world)

    allocation = CAPITAL_PER_AGENT * weights

    return allocation


# --------------------------------------------------
# MARKET SIMULATION
# --------------------------------------------------

divergence_history = []

for t in range(TIMESTEPS):

    market_allocation = np.zeros(NUM_ASSETS)

    # Each agent computes independently
    for agent in range(NUM_AGENTS):

        estimated_world = agent_estimate(W)

        allocation = agent_allocate(
            estimated_world
        )

        market_allocation += allocation

    ideal = ideal_allocation(W)

    divergence = np.sum(
        np.abs(
            ideal - market_allocation
        )
    )

    divergence_history.append(divergence)


# --------------------------------------------------
# PLOT
# --------------------------------------------------

plt.plot(divergence_history)

plt.xlabel("Time")

plt.ylabel("Market Divergence")

plt.title("5DMarkets Simulation 1")

plt.show()