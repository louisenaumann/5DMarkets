import numpy as np


class ReconstructionOperator:

    """
    R(O_t) = Z_t

    Reconstruct latent market state
    from sparse observed market data.
    """

    def __init__(self, latent_dim=128):

        self.latent_dim = latent_dim

        # placeholder weight matrix
        self.W = np.random.randn(
            latent_dim,
            7
        ) * 0.01


    def forward(self, observations):

        """
        observations:

        [price,
         volume,
         volatility,
         options,
         sentiment,
         sector_strength,
         yield_curve]
        """

        observations = np.array(
            observations
        )

        latent_state = np.dot(
            self.W,
            observations
        )

        latent_state = np.tanh(
            latent_state
        )

        return latent_state