import numpy as np


class CapitalAllocator:

    """
    Π(Y_(t+1)) = A_t

    Convert predicted future market state
    into portfolio allocation decision.
    """

    def __init__(self):

        pass


    def softmax(self, x):

        exp_x = np.exp(
            x - np.max(x)
        )

        return exp_x / np.sum(
            exp_x
        )


    def forward(self,
                future_state):

        """
        future_state = Y_(t+1)

        Output:

        allocation_weights
        """

        allocation = self.softmax(
            future_state
        )

        return allocation