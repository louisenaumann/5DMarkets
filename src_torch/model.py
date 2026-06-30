import torch
import torch.nn as nn

from layers.reconstruction import ReconstructionOperator
from layers.market_manifold import MarketManifold
from layers.hysteresis_memory import HysteresisMemory
from layers.deformation_graph import DeformationGraph
from layers.future_transition import FutureTransition
from layers.decoder import Decoder


class FiveDMarketsModel(nn.Module):

    """
    Full 5DMarkets architecture

    O_t → R → M → H → G → Φ → D → O_hat
    """

    def __init__(self):

        super().__init__()

        self.R = ReconstructionOperator()

        self.M = MarketManifold()

        self.H = HysteresisMemory()

        self.G = DeformationGraph()

        self.Phi = FutureTransition()

        self.D = Decoder()


    def forward(self,
                observation,
                previous_state):

        z = self.R(
            observation
        )

        s = self.M(
            z
        )

        h = self.H(
            s,
            previous_state
        )

        d = self.G(
            h
        )

        y = self.Phi(
            d
        )

        reconstructed = self.D(
            y
        )

        return reconstructed, s