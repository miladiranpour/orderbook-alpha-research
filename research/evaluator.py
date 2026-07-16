from research.metrics import METRICS


def evaluate(

    feature_name,

    feature,

    future

):

    result = {

        "Feature": feature_name

    }

    for metric_name, metric_info in METRICS.items():

        metric_function = metric_info["function"]

        value = metric_function(

            feature,

            future

        )

        result[metric_name] = round(

            value,

            metric_info["precision"]

        )

    return result