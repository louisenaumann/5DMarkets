import torch
import torch.nn as nn


class FutureTransition(nn.Module):

    """
    Φ(D_t) = Y_t

    Predict next plausible
    latent state transition.
    """

    def __init__(self,
                 state_dim=32):

        super().__init__()

        self.linear = nn.Linear(
            state_dim,
            state_dim
        )


    def forward(self,
                deformation_state):

        future_state = torch.tanh(
            self.linear(
                deformation_state
            )
        )

        return future_state