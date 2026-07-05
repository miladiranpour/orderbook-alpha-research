from utils.loader import load_json
from utils.future_return import build_future_return
from utils.config import DATA_PATH
from utils.labels import build_labels
from features.imbalance import calculate
from research.report import run

records = load_json(DATA_PATH)
future = build_future_return(records, 10)
labels = build_labels(future)
imbalance = calculate(records)


import features.imbalance as imbalance

import research.report as report
imbalance_values = imbalance.calculate(records)

report.run(

    feature_name="Imbalance",

    feature_values=imbalance_values,

    future_returns=future,

    labels=labels

)