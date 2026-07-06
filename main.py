from utils.loader import load_json
from utils.future_return import build_future_return
from utils.config import DATA_PATH
from utils.labels import build_labels
from research.report import run
from features.registry import FEATURES
import research.report as report

records = load_json(DATA_PATH)
future = build_future_return(records, 10)
labels = build_labels(future)

for name, func in FEATURES.items():

    feature = func(records)

    report.run(

        feature_name=name,

        feature_values=feature,

        future_returns=future,

        labels=labels

    )

