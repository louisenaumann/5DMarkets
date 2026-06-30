import torch
import torch.nn as nn


class DivergenceOperator(nn.Module):

    """
    Ω(S_eq,S_obs) = Δ_t

    Measure divergence between
    equilibrium market state and
    observed market state.
    """

    def __init__(self):

        super().__init__()


    def forward(self,
                equilibrium_state,
                observed_state):

        divergence = (

            equilibrium_state

            -

            observed_state

        )

        return divergence