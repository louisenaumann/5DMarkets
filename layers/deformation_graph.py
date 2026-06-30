import numpy as np


class DeformationGraph:

    """
    G(S_t_tilde) = D_t

    Propagates state changes across
    economically coupled assets.

    Analogous to deformation vector field
    propagation in 5DCT.
    """

    def __init__(self,
                 state_dim=32):

        self.state_dim = state_dim

        # adjacency matrix
        self.A = np.random.randn(
            state_dim,
            state_dim
        ) * 0.05


    def forward(self,
                memory_state):

        """
        memory_state = S_t_tilde

        Output:

        deformation_state = D_t
        """

        deformation_state = np.dot(
            self.A,
            memory_state
        )

        deformation_state = np.tanh(
            deformation_state
        )

        return deformation_state