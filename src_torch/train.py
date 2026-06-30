import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from model import FiveDMarketsModel
from dataset import MarketSequenceDataset


# -----------------------------------------
# DATA
# -----------------------------------------

dataset = MarketSequenceDataset()

loader = DataLoader(
    dataset,
    batch_size=32,
    shuffle=True
)


# -----------------------------------------
# MODEL
# -----------------------------------------

model = FiveDMarketsModel()


optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)


loss_fn = nn.MSELoss()
loss_history = []

# -----------------------------------------
# TRAINING LOOP
# -----------------------------------------

NUM_EPOCHS = 50

NUM_EPOCHS = 50

loss_history = []

for epoch in range(NUM_EPOCHS):

    total_loss = 0

    for current_obs, future_obs in loader:

        previous_delta = torch.zeros(
            current_obs.shape[0],
            32
        )

        optimizer.zero_grad()

        predicted_future, delta = model(
            current_obs,
            previous_delta
        )

        target = model.P(
            future_obs
        )

        loss = loss_fn(
            predicted_future,
            target
        )

        loss.backward()

        optimizer.step()

        total_loss += loss.item()

    loss_history.append(
        total_loss
    )

    print(
        "Epoch:",
        epoch,
        "Loss:",
        total_loss
    )

print(loss_history)
