# Order Book Alpha Research

Research project investigating whether
BTCUSDT order book information can predict
future short-term returns.

## Dataset

Exchange: Binance

Market: BTCUSDT

Sampling Frequency:
~1 snapshot per second

Duration:
~5 hours

Snapshots:
~18,000

## Features

- Order Book Imbalance
- Weighted Imbalance
- Order Flow Imbalance (OFI)

## Results

| Horizon | Imbalance | Weighted | OFI |
|----------|----------:|----------:|----------:|
| 10s | 0.183 | 0.184 | 0.093 |
| 30s | 0.120 | 0.120 | 0.050 |
| 60s | 0.072 | 0.072 | 0.039 |
| 120s | 0.025 | 0.025 | 0.027 |
| 300s | -0.020 | -0.020 | 0.019 |

## Key Findings

- Most predictive information exists within the first 5 order book levels.
- Signal decays rapidly after 30-60 seconds.
- Imbalance outperformed OFI in this dataset.

## Next Steps

- Label Engineering
- Classification Models
- Logistic Regression
- Backtesting
