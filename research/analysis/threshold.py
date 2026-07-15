import numpy as np
import pandas as pd


def calculate(

    feature,

    future,

    start=0.50,

    end=0.95,

    step=0.05

):

    feature = np.asarray(feature)
    future = np.asarray(future)

    rows = []

    thresholds = np.arange(

        start,

        end + step,

        step

    )

    for threshold in thresholds:

        mask = feature > threshold

        trades = mask.sum()

        if trades == 0:

            continue

        returns = future[mask]

        average_return = returns.mean()

        win_rate = (returns > 0).mean()

        sharpe = (

            average_return

            /

            returns.std()

            if returns.std() != 0

            else 0

        )

        rows.append({

            "Threshold": round(threshold,2),

            "Trades": trades,

            "WinRate": round(win_rate,4),

            "AverageReturn": average_return,

            "Sharpe": sharpe

        })

    return pd.DataFrame(rows)