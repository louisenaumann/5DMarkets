import torch
import torch.nn as nn


class MarketManifold(nn.Module):

    """
    M(Z_t) = S_t
    """

    def __init__(self,
                 input_dim=128,
                 manifold_dim=32):

        super().__init__()

        self.linear = nn.Linear(
            input_dim,
            manifold_dim
        )


    def forward(self,
                latent_state):

        state = torch.tanh(
            self.linear(
                latent_state
            )
        )

        return state