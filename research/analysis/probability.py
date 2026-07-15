import numpy as np
import pandas as pd


def calculate(

    feature,

    labels,

    bins=10

):

    feature = np.asarray(feature)

    labels = np.asarray(labels)

    edges = np.linspace(

        -1,

        1,

        bins + 1

    )

    rows = []

    for i in range(bins):

        left = edges[i]

        right = edges[i+1]

        mask = (

            (feature >= left)

            &

            (feature < right)

        )

        count = mask.sum()

        if count == 0:

            up = np.nan

        else:

            up = labels[mask].mean()

        rows.append({

            "Bin":

            f"[{left:.1f},{right:.1f})",

            "Count":

            count,

            "UP":

            up

        })

    return pd.DataFrame(rows)