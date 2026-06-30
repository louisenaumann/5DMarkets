import sys
import os

# add repo root to python path
sys.path.append(
    os.path.abspath(
        os.path.join(
            os.path.dirname(__file__),
            "../../../"
        )
    )
)

import torch
import torch.nn as nn

from src_torch.layers.observed_projection import ObservedProjection
from src_torch.layers.hysteresis_memory import HysteresisMemory
from src_torch.layers.deformation_graph import DeformationGraph
from src_torch.layers.future_transition import FutureTransition


class NoDivergenceModel(nn.Module):

    """
    Ablation model.

    Removes equilibrium branch and
    removes divergence operator Ω.
    """

    def __init__(self):

        super().__init__()

        self.P = ObservedProjection()

        self.H = HysteresisMemory()

        self.G = DeformationGraph()

        self.Phi = FutureTransition()


    def forward(self,
                observation,
                previous_state):

        observed = self.P(
            observation
        )

        memory = self.H(
            observed,
            previous_state
        )

        deformation = self.G(
            memory
        )

        future = self.Phi(
            deformation
        )

        return future
