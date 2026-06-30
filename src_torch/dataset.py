import torch
import numpy as np


class MarketDataset:

    """
    Structured synthetic market data.

    Variables are correlated.

    This simulates realistic market structure.
    """

    def __init__(self):

        pass


    def generate_sample(self):

        # base market stress variable
        stress = np.random.normal(0, 1)

        # correlations built in

        price_return = -0.03 * stress \
                       + np.random.normal(0, 0.01)

        volume = 1.0 \
                 + 0.4 * abs(stress) \
                 + np.random.normal(0, 0.05)

        volatility = 0.2 \
                     + 0.15 * abs(stress) \
                     + np.random.normal(0, 0.02)

        options_skew = 0.15 \
                       + 0.10 * stress \
                       + np.random.normal(0, 0.02)

        sentiment = 0.7 \
                    - 0.25 * stress \
                    + np.random.normal(0, 0.03)

        sector_strength = 0.6 \
                          - 0.2 * stress \
                          + np.random.normal(0, 0.03)

        yield_curve = 0.4 \
                      + 0.1 * stress \
                      + np.random.normal(0, 0.02)

        sample = np.array([

            price_return,

            volume,

            volatility,

            options_skew,

            sentiment,

            sector_strength,

            yield_curve

        ])

        return torch.tensor(
            sample,
            dtype=torch.float32
        )


    def corrupt(self,
                sample):

        corrupted = sample.clone()

        # hide volatility
        corrupted[2] = 0.0

        # hide options skew
        corrupted[3] = 0.0

        return corrupted