from utils.loader import load_json
from utils.future_return import build_future_return
from utils.labels import build_labels
from utils.config import DATA_PATH

from research.engine import ResearchEngine


records = load_json(DATA_PATH)

future = build_future_return(

    records,

    horizon=10

)

labels = build_labels(future)

engine = ResearchEngine(

    records,

    future,

    labels,

    config={

        "horizon":10

    }

)

results = engine.run()
results.save("results/latest.pkl")

print()

print("===== Metrics =====")
print(results.metrics)

print(
    "\n===== Ranking ====="
)
print(results.ranking)
