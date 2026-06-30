import torch
import torch.nn as nn


class Decoder(nn.Module):

    """
    D(Y_t) = O_hat_t

    Reconstruct full market
    observation vector.
    """

    def __init__(self,
                 input_dim=32,
                 output_dim=7):

        super().__init__()

        self.linear = nn.Linear(
            input_dim,
            output_dim
        )


    def forward(self,
                latent_state):

        output = self.linear(
            latent_state
        )

        return output