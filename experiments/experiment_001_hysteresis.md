# Experiment 001 — Market Hysteresis Validation

Objective

Test whether identical present asset prices correspond to distinct future probability distributions depending on the historical trajectory through which the price was reached.

------------------------------------------------------------

Hypothesis

Future return distribution depends not only on present market state but also on the historical path through which that state was reached.

Formally:

Traditional assumption:

Future = f(Current State)

5DMarkets assumption:

Future = f(Current State, Historical Path)

------------------------------------------------------------

Theoretical Motivation

In 5DCT respiratory motion modeling, anatomical structures frequently occupy identical spatial coordinates during inhalation and exhalation.

Despite identical present position, future movement differs because system trajectory differs.

This effect is known as hysteresis.

We hypothesize the same phenomenon exists in financial markets.

------------------------------------------------------------

Experimental Design

Select a financial asset.

Example assets:

NVDA
SPY
TSLA
QQQ
XBI

Collect historical price data.

For all instances where asset reaches approximately identical price levels:

Separate observations into two trajectory groups.

Group A

Asset reached price through positive trend.

Example:

150 → 160 → 170 → 180

Group B

Asset reached identical price through negative trend recovery.

Example:

230 → 210 → 190 → 180

Present state:

Both groups end at identical price.

------------------------------------------------------------

Test Variable

Measure future return distribution over:

1 day forward return

5 day forward return

10 day forward return

20 day forward return

------------------------------------------------------------

Statistical Question

Does future return distribution differ significantly between path groups?

Test methods:

Two sample t test

Kolmogorov Smirnov distribution test

Bootstrap distribution comparison

Bayesian posterior estimation

------------------------------------------------------------

Possible Outcomes

Outcome 1

No statistical difference.

Conclusion:

Weak evidence for market hysteresis.

Outcome 2

Significant difference exists.

Conclusion:

Path dependency influences future state.

Evidence supports 5DMarkets framework.

------------------------------------------------------------

Expected Implication

If hysteresis exists, market state cannot be fully described by instantaneous observation.

Historical path becomes a necessary component of future prediction models.

------------------------------------------------------------

Future Extension

Train hysteresis operator H(S_t) using path dependent sequence learning models.

Possible models:

LSTM

Transformer attention

Temporal convolution network