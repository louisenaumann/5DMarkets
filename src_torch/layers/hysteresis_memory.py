import torch
import torch.nn as nn


class HysteresisMemory(nn.Module):

    """
    H(S_t,S_(t-1))
    """

    def __init__(self,
                 alpha=0.2):

        super().__init__()

        self.alpha = alpha


    def forward(self,
                current_state,
                previous_state):

        output = (

            self.alpha
            * current_state

            +

            (1 - self.alpha)
            * previous_state

        )

        return output