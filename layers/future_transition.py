import numpy as np


class FutureTransition:

    """
    Φ(D_t) = Y_(t+1)

    Predict next plausible market state
    transition from deformation state.

    Predict state transition,
    not future price.
    """

    def __init__(self,
                 state_dim=32):

        self.state_dim = state_dim

        # transition matrix
        self.W = np.random.randn(
            state_dim,
            state_dim
        ) * 0.02

        self.b = np.zeros(
            state_dim
        )


    def forward(self,
                deformation_state):

        """
        deformation_state = D_t

        Output:

        future_state = Y_(t+1)
        """

        future_state = np.dot(
            self.W,
            deformation_state
        ) + self.b

        future_state = np.tanh(
            future_state
        )

        return future_state