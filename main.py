from utils.loader import load_json
from utils.future_return import build_future_return
from utils.labels import build_labels

from utils.config import DATA_PATH

from features.registry import FEATURES

from research.evaluator import evaluate

from research.analysis.registry import (
    TABLE_ANALYSIS
)

import pandas as pd



records = load_json(DATA_PATH)

future = build_future_return(

    records,

    horizon=10

)

labels = build_labels(future)



metric_results = []

analysis_results = {}



for feature_name, feature_function in FEATURES.items():

    feature = feature_function(records)

    # `future` at index i is the return from record i to record i + horizon,
    # so values without a corresponding future return must be excluded.
    feature = feature[:len(future)]

    result = evaluate(

        feature_name,

        feature,

        future

    )

    metric_results.append(result)

    analysis_results[feature_name] = {}

    for analysis_name, analysis_function in TABLE_ANALYSIS.items():

        if analysis_name in [

            "Probability",

            "Decile"

        ]:

            analysis_results[feature_name][analysis_name] = analysis_function(

                feature,

                labels

            )

        else:

            analysis_results[feature_name][analysis_name] = analysis_function(

                feature,

                future

            )



metrics_df = pd.DataFrame(

    metric_results

)



print(metrics_df)
print(
analysis_results["Imbalance"]["Threshold"]
)

print(TABLE_ANALYSIS.keys())