import torch

from model import FiveDMarketsModel


model = FiveDMarketsModel()


# batch size = 1
observation = torch.randn(
    1,
    7
)

previous_state = torch.zeros(
    1,
    32
)


output, state = model(
    observation,
    previous_state
)


print("Output shape:", output.shape)

print("State shape:", state.shape)