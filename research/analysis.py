import numpy as np
import pandas as pd

def correlation(feature, future):

    n = min(len(feature), len(future))

    x = np.array(feature[:n])

    y = np.array(future[:n])

    return np.corrcoef(x, y)[0, 1]


def average_return(feature, future, bins=10):

    n = min(len(feature), len(future))

    df = pd.DataFrame({

        "feature": feature[:n],

        "future": future[:n]

    })

    df["bin"] = pd.cut(df["feature"], bins)

    result = (
        df.groupby("bin", observed=False)["future"]
        .mean()
    )

    return result


def up_probability(feature, labels, bins=10):

    n = min(len(feature), len(labels))

    df = pd.DataFrame({

        "feature": feature[:n],

        "label": labels[:n]

    })

    df["bin"] = pd.cut(df["feature"], bins)

    result = (
        df.groupby("bin", observed=False)["label"]
        .mean()
    )

    return result


def threshold_analysis(
        feature,
        future,
        thresholds
):

    n = min(len(feature), len(future))

    feature = np.array(feature[:n])

    future = np.array(future[:n])

    rows = []

    for th in thresholds:

        mask = feature >= th

        ret = future[mask]

        if len(ret) == 0:
            continue

        rows.append({

            "Threshold": th,

            "Trades": len(ret),

            "Win Rate": np.mean(ret > 0),

            "Average Return": np.mean(ret),

            "Sharpe": np.mean(ret) / np.std(ret)

        })

    return pd.DataFrame(rows)


