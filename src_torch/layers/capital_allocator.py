import torch
import torch.nn as nn


class CapitalAllocator(nn.Module):

    """
    Π(Y_(t+1)) = A_t

    Convert future state into
    portfolio allocation.
    """

    def __init__(self):

        super().__init__()

        self.softmax = nn.Softmax(
            dim=1
        )


    def forward(self,
                future_state):

        allocation = self.softmax(
            future_state
        )

        return allocation