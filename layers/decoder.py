import numpy as np


class Decoder:

    """
    D(Y_t) = O_hat_t

    Reconstruct full market observation
    from latent predicted state.
    """

    def __init__(self,
                 input_dim=32,
                 output_dim=7):

        self.input_dim = input_dim

        self.output_dim = output_dim

        self.W = np.random.randn(
            output_dim,
            input_dim
        ) * 0.01


    def forward(self,
                latent_state):

        """
        latent_state = Y_t

        Output:

        reconstructed_observation
        """

        output = np.dot(
            self.W,
            latent_state
        )

        return output