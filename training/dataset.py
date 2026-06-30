import numpy as np


class MarketDataset:

    """
    Generate synthetic market observations
    for reconstruction training.
    """

    def __init__(self,
                 num_samples=10000):

        self.num_samples = num_samples


    def generate_sample(self):

        """
        Create one synthetic observation vector.

        [return,
         volume,
         volatility,
         options,
         sentiment,
         sector,
         yield_curve]
        """

        sample = np.array([

            np.random.normal(0, 0.03),

            np.random.uniform(0.5, 2.0),

            np.random.uniform(0.1, 0.8),

            np.random.uniform(0.05, 0.4),

            np.random.uniform(0, 1),

            np.random.uniform(0, 1),

            np.random.uniform(0, 1)

        ])

        return sample


    def corrupt(self, sample):

        """
        Hide random variables.
        """

        corrupted = sample.copy()

        # randomly hide volatility
        corrupted[2] = 0.0

        # randomly hide options skew
        corrupted[3] = 0.0

        return corrupted