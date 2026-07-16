import pandas as pd


def normalize(metrics_df, metric_info):

    normalized = metrics_df.copy()

    for metric_name, info in metric_info.items():

        values = normalized[metric_name]

        minimum = values.min()

        maximum = values.max()

        if maximum == minimum:

            normalized[metric_name] = 1.0

            continue

        normalized[metric_name] = (

            values - minimum

        ) / (

            maximum - minimum

        )

    return normalized