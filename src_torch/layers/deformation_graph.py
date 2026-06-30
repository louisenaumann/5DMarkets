import torch
import torch.nn as nn


class DeformationGraph(nn.Module):

    """
    G(S_t_tilde) = D_t

    Propagate state deformation
    through connected assets.
    """

    def __init__(self,
                 state_dim=32):

        super().__init__()

        self.linear = nn.Linear(
            state_dim,
            state_dim
        )


    def forward(self,
                memory_state):

        deformation = torch.tanh(
            self.linear(
                memory_state
            )
        )

        return deformation