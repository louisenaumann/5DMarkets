import numpy as np


class MarketManifold:

    """
    M(Z_t) = S_t

    Project reconstructed latent state
    onto continuous market state manifold.
    """

    def __init__(self,
                 input_dim=128,
                 manifold_dim=32):

        self.input_dim = input_dim

        self.manifold_dim = manifold_dim

        # projection matrix
        self.W = np.random.randn(
            manifold_dim,
            input_dim
        ) * 0.01


    def forward(self, latent_state):

        """
        latent_state = Z_t

        Output:

        manifold_state = S_t
        """

        manifold_state = np.dot(
            self.W,
            latent_state
        )

        manifold_state = np.tanh(
            manifold_state
        )

        return manifold_state