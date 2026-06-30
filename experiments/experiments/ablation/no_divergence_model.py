import torch
import torch.nn as nn
from torch.utils.data import DataLoader

from 5DMarkets.src_torch.dataset import MarketSequenceDataset
from no_divergence_model import NoDivergenceModel


dataset = MarketSequenceDataset()

loader = DataLoader(
    dataset,
    batch_size=32,
    shuffle=True
)


model = NoDivergenceModel()


optimizer = torch.optim.Adam(
    model.parameters(),
    lr=0.001
)


loss_fn = nn.MSELoss()


NUM_EPOCHS = 50

loss_history = []


for epoch in range(NUM_EPOCHS):

    total_loss = 0

    for current_obs, future_obs in loader:

        previous_state = torch.zeros(
            current_obs.shape[0],
            32
        )

        optimizer.zero_grad()

        prediction = model(
            current_obs,
            previous_state
        )

        #
        # SAME TARGET
        #

        target = model.P(
            future_obs
        )

        loss = loss_fn(
            prediction,
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