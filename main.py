from layers.reconstruction import ReconstructionOperator
from layers.market_manifold import MarketManifold
from layers.hysteresis_memory import HysteresisMemory
from layers.deformation_graph import DeformationGraph
from layers.future_transition import FutureTransition
from layers.capital_allocator import CapitalAllocator


# --------------------------------------------------
# INITIALIZE OPERATORS
# --------------------------------------------------

R = ReconstructionOperator()

M = MarketManifold()

H = HysteresisMemory()

G = DeformationGraph()

Phi = FutureTransition()

Pi = CapitalAllocator()


# --------------------------------------------------
# OBSERVED MARKET DATA
# example input vector
# --------------------------------------------------

O_t = [

    0.03,      # price return

    1.2,       # volume change

    0.25,      # implied volatility

    0.18,      # options skew

    0.72,      # sentiment

    0.55,      # sector strength

    0.42       # yield curve state
]


# --------------------------------------------------
# FULL PIPELINE
# --------------------------------------------------

Z_t = R.forward(O_t)

S_t = M.forward(Z_t)

S_memory = H.forward(S_t)

D_t = G.forward(S_memory)

Y_future = Phi.forward(D_t)

allocation = Pi.forward(Y_future)


# --------------------------------------------------
# OUTPUT
# --------------------------------------------------

print("Portfolio Allocation")

print(allocation)