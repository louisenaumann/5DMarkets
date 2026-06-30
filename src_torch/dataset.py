import torch
from torch.utils.data import Dataset
import numpy as np


class MarketSequenceDataset(Dataset):

    """
    Generate synthetic sequential market data.

    Each sample:

    O_t  -> current observation

    O_t+1 -> future observation
    """

    def __init__(self,
                 num_samples=5000):

        self.samples = []

        for _ in range(num_samples):

            # latent market stress
            stress_t = np.random.normal(0, 1)

            # next step partially persistent
            stress_next = (
                0.8 * stress_t
                +
                np.random.normal(0, 0.2)
            )

            current = self.generate_state(
                stress_t
            )

            future = self.generate_state(
                stress_next
            )

            self.samples.append(
                (current, future)
            )


    def generate_state(self,
                       stress):

        price_return = -0.03 * stress \
                       + np.random.normal(0, 0.01)

        volume = 1.0 \
                 + 0.4 * abs(stress)

        volatility = 0.2 \
                     + 0.15 * abs(stress)

        options_skew = 0.15 \
                       + 0.10 * stress

        sentiment = 0.7 \
                    - 0.25 * stress

        sector_strength = 0.6 \
                          - 0.2 * stress

        yield_curve = 0.4 \
                      + 0.1 * stress

        vec = np.array([

            price_return,

            volume,

            volatility,

            options_skew,

            sentiment,

            sector_strength,

            yield_curve

        ])

        return torch.tensor(
            vec,
            dtype=torch.float32
        )


    def __len__(self):

        return len(
            self.samples
        )


    def __getitem__(self,
                    idx):

        return self.samples[idx]