import pandas as pd


def score(

    normalized_df,

    metrics_info

):

    df = normalized_df.copy()

    score = []

    metric_columns = []

    for metric_name in metrics_info.keys():

        metric_columns.append(

            metric_name

        )

    for _, row in df.iterrows():

        total = 0.0

        weight_sum = 0.0

        for metric_name, info in metrics_info.items():

            weight = info["weight"]

            total += (

                row[metric_name]

                *

                weight

            )

            weight_sum += weight

        score.append(

            total / weight_sum

        )

    df["Score"] = score

    return df