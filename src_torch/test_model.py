import torch

from model import FiveDMarketsModel


model = FiveDMarketsModel()


observation = torch.randn(
    1,
    7
)

previous_delta = torch.zeros(
    1,
    32
)


allocation, delta = model(
    observation,
    previous_delta
)


print("Allocation shape:",
      allocation.shape)

print("Delta shape:",
      delta.shape)