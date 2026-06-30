import torch
from torch.utils.data import Dataset
import numpy as np


class DisequilibriumDataset(Dataset):

    """
    Synthetic market world.

    Hidden equilibrium exists.

    Observed market deviates from equilibrium.

    Future partially corrects toward equilibrium.
    """

    def __init__(self,
                 num_samples=5000):

        self.samples = []

        for _ in range(num_samples):

            #
            # hidden equilibrium
            #

            equilibrium = np.random.normal(
                0,
                1
            )

            #
            # observed market displaced
            #

            displacement = np.random.normal(
                0,
                0.8
            )

            observed_state = (
                equilibrium
                +
                displacement
            )

            #
            # future moves toward equilibrium
            #

            correction_strength = 0.4

            future_state = (

                observed_state

                +

                correction_strength *

                (

                    equilibrium

                    -

                    observed_state

                )

                +

                np.random.normal(
                    0,
                    0.05
                )

            )

            current = self.generate_features(
                observed_state
            )

            future = self.generate_features(
                future_state
            )

            self.samples.append(
                (current, future)
            )


    def generate_features(self,
                          latent):

        price_return = -0.04 * latent \
                       + np.random.normal(0, 0.02)

        volume = 1.0 \
                 + 0.5 * abs(latent)

        volatility = 0.3 \
                     + 0.25 * abs(latent)

        options_skew = 0.2 \
                       + 0.15 * latent

        sentiment = 0.8 \
                    - 0.30 * latent

        sector_strength = 0.7 \
                          - 0.2 * latent

        yield_curve = 0.5 \
                      + 0.12 * latent

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
