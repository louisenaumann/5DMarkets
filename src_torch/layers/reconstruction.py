import torch
import torch.nn as nn


class ReconstructionOperator(nn.Module):

    """
    R(O_t) = Z_t

    Reconstruct latent market state
    from sparse observations.
    """

    def __init__(self,
                 input_dim=7,
                 latent_dim=128):

        super().__init__()

        self.linear = nn.Linear(
            input_dim,
            latent_dim
        )


    def forward(self,
                observations):

        latent_state = torch.tanh(
            self.linear(
                observations
            )
        )

        return latent_state