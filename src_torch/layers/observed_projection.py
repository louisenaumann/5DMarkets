import torch
import torch.nn as nn


class ObservedProjection(nn.Module):

    """
    Project raw observation directly
    into observed market state space.

    S_obs(t)
    """

    def __init__(self,
                 input_dim=7,
                 state_dim=32):

        super().__init__()

        self.linear = nn.Linear(
            input_dim,
            state_dim
        )


    def forward(self,
                observation):

        state = torch.tanh(

            self.linear(
                observation
            )

        )

        return state