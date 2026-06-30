import numpy as np


class HysteresisMemory:

    """
    H(S_t) = S_t_tilde

    Incorporates path dependence and
    historical trajectory memory.

    Current state alone is insufficient.
    """

    def __init__(self,
                 state_dim=32,
                 alpha=0.2):

        self.state_dim = state_dim

        self.alpha = alpha

        # initialize historical memory
        self.previous_state = np.zeros(
            state_dim
        )


    def forward(self, current_state):

        """
        current_state = S_t

        Output:

        memory_adjusted_state = S_t_tilde
        """

        updated_state = (

            self.alpha * current_state

            +

            (1 - self.alpha)
            * self.previous_state

        )

        self.previous_state = updated_state

        return updated_state