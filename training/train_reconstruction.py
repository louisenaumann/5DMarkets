import numpy as np

from training.dataset import MarketDataset

from layers.reconstruction import ReconstructionOperator
from layers.market_manifold import MarketManifold
from layers.hysteresis_memory import HysteresisMemory
from layers.deformation_graph import DeformationGraph
from layers.future_transition import FutureTransition
from layers.decoder import Decoder


# --------------------------------------------------
# INITIALIZE DATASET
# --------------------------------------------------

dataset = MarketDataset()


# --------------------------------------------------
# INITIALIZE MODEL
# --------------------------------------------------

R = ReconstructionOperator()

M = MarketManifold()

H = HysteresisMemory()

G = DeformationGraph()

Phi = FutureTransition()

D = Decoder()


# --------------------------------------------------
# LOSS FUNCTION
# --------------------------------------------------

def mse_loss(true, pred):

    return np.mean(
        (true - pred) ** 2
    )


# --------------------------------------------------
# TRAINING LOOP
# --------------------------------------------------

NUM_EPOCHS = 1000

loss_history = []

for epoch in range(NUM_EPOCHS):

    sample = dataset.generate_sample()

    corrupted = dataset.corrupt(sample)

    # forward pass

    z = R.forward(corrupted)

    s = M.forward(z)

    h = H.forward(s)

    d = G.forward(h)

    y = Phi.forward(d)

    reconstructed = D.forward(y)

    loss = mse_loss(
        sample,
        reconstructed
    )

    loss_history.append(loss)

    if epoch % 100 == 0:

        print(
            "Epoch:",
            epoch,
            "Loss:",
            loss
        )


print("Training Complete")