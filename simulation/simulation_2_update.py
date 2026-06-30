import numpy as np
import matplotlib.pyplot as plt


# --------------------------------------------------
# CONFIGURATION
# --------------------------------------------------

NUM_ASSETS = 5
NUM_AGENTS = 100
CAPITAL_PER_AGENT = 10
TIMESTEPS = 50

INFO_ERROR_STD = 0.12
HUMAN_ERROR_STD = 0.04

# memory persistence
BETA = 0.75


# --------------------------------------------------
# EXTERNAL WORLD EVOLUTION
# independent of market
# --------------------------------------------------

def world_state(t):

    if t < 10:
        return np.array([0.8, 0.4, 0.6, 0.5, 0.2])

    elif t < 20:
        return np.array([0.5, 0.9, 0.5, 0.4, 0.2])

    elif t < 30:
        return np.array([0.4, 0.4, 0.5, 0.3, 0.9])

    elif t < 40:
        return np.array([0.3, 0.4, 1.0, 0.5, 0.2])

    else:
        return np.array([0.5, 0.3, 0.4, 0.9, 0.3])


# --------------------------------------------------
# IDEAL ALLOCATION
# perfect rational observer
# --------------------------------------------------

def ideal_allocation(world):

    total_capital = NUM_AGENTS * CAPITAL_PER_AGENT

    weights = world / np.sum(world)

    return total_capital * weights


# --------------------------------------------------
# AGENT UPDATE
# memory + imperfect observation
# --------------------------------------------------

def update_agent_belief(previous_belief, true_world):

    info_error = np.random.normal(
        0,
        INFO_ERROR_STD,
        NUM_ASSETS
    )

    human_error = np.random.normal(
        0,
        HUMAN_ERROR_STD,
        NUM_ASSETS
    )

    observed_world = true_world + info_error + human_error

    observed_world = np.clip(
        observed_world,
        0.01,
        None
    )

    new_belief = (
        BETA * previous_belief
        +
        (1 - BETA) * observed_world
    )

    return new_belief


# --------------------------------------------------
# CAPITAL ALLOCATION
# --------------------------------------------------

def allocate_capital(belief):

    weights = belief / np.sum(belief)

    return CAPITAL_PER_AGENT * weights


# --------------------------------------------------
# INITIALIZE AGENTS
# --------------------------------------------------

agent_beliefs = []

initial_world = world_state(0)

for _ in range(NUM_AGENTS):
    agent_beliefs.append(initial_world.copy())


# --------------------------------------------------
# RUN SIMULATION
# --------------------------------------------------

divergence_history = []

for t in range(TIMESTEPS):

    true_world = world_state(t)

    market_allocation = np.zeros(NUM_ASSETS)

    for i in range(NUM_AGENTS):

        updated_belief = update_agent_belief(
            agent_beliefs[i],
            true_world
        )

        agent_beliefs[i] = updated_belief

        allocation = allocate_capital(
            updated_belief
        )

        market_allocation += allocation

    ideal = ideal_allocation(true_world)

    divergence = np.sum(
        np.abs(
            ideal - market_allocation
        )
    )

    divergence_history.append(divergence)


# --------------------------------------------------
# PLOT RESULTS
# --------------------------------------------------

plt.plot(divergence_history)

plt.xlabel("Time")

plt.ylabel("Divergence")

plt.title("Simulation 1: Delayed Adaptation")

plt.show()