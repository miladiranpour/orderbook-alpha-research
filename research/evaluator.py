from research.metrics import METRICS


def evaluate(

    feature_name,

    feature,

    future

):

    result = {

        "Feature": feature_name

    }

    for metric_name, metric_function in METRICS.items():

        value = metric_function(

            feature,

            future

        )

        result[metric_name] = value

    return result