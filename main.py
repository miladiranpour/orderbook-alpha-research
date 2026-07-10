from utils.loader import load_json
from utils.future_return import build_future_return
from utils.alignment import align
from utils.config import DATA_PATH

from features.registry import FEATURES

from research.evaluator import evaluate

import pandas as pd

records = load_json(DATA_PATH)

future = build_future_return(records, 10)

results = []

for name, func in FEATURES.items():

    feature = func(records)

    feature, future_aligned = align(
        feature,
        future
    )

    result = evaluate(
        name,
        feature,
        future_aligned
    )

    results.append(result)

df = pd.DataFrame(results)

print(df)