import torch
import torch.nn as nn

from layers.reconstruction import ReconstructionOperator
from layers.market_manifold import MarketManifold
from layers.observed_projection import ObservedProjection
from layers.divergence import DivergenceOperator
from layers.hysteresis_memory import HysteresisMemory
from layers.deformation_graph import DeformationGraph
from layers.future_transition import FutureTransition
from layers.capital_allocator import CapitalAllocator


class FiveDMarketsModel(nn.Module):

    """
    Architecture V2

    O_t → [Equilibrium Branch + Observed Branch]

    Δ = S_eq - S_obs

    Δ → H → G → Φ → Π
    """

    def __init__(self):

        super().__init__()

        # equilibrium branch
        self.R = ReconstructionOperator()

        self.M = MarketManifold()

        # observed branch
        self.P = ObservedProjection()

        # divergence
        self.Omega = DivergenceOperator()

        # temporal + propagation
        self.H = HysteresisMemory()

        self.G = DeformationGraph()

        self.Phi = FutureTransition()

        # allocation
        self.Pi = CapitalAllocator()


    def forward(self,
                observation,
                previous_delta):

        # equilibrium estimate
        z = self.R(
            observation
        )

        s_eq = self.M(
            z
        )

        # observed state
        s_obs = self.P(
            observation
        )

        # divergence
        delta = self.Omega(
            s_eq,
            s_obs
        )

        # memory
        memory = self.H(
            delta,
            previous_delta
        )

        # deformation propagation
        deformation = self.G(
            memory
        )

        # future transition
        future = self.Phi(
            deformation
        )

        # allocation
        allocation = self.Phi(
            future
        )

        return allocation, delta