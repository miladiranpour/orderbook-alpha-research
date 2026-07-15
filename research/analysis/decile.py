import numpy as np
import pandas as pd


def calculate(

    feature,

    labels

):

    feature = np.asarray(feature)

    labels = np.asarray(labels)

    q = np.quantile(

        feature,

        np.linspace(

            0,

            1,

            11

        )

    )

    rows=[]

    for i in range(10):

        left=q[i]

        right=q[i+1]

        mask=(

            feature>=left

        )&(

            feature<=right

        )

        rows.append({

            "Decile":i+1,

            "Count":mask.sum(),

            "UP":labels[mask].mean()

        })

    return pd.DataFrame(rows)