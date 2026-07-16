import pickle
from pathlib import Path


class ResearchResult:


    def __init__(

        self,

        metrics=None,

        analysis=None,

        ranking=None,

        plots=None,

        metadata=None

    ):


        self.metrics = metrics

        self.analysis = analysis

        self.ranking = ranking

        self.plots = plots

        self.metadata = metadata



    def summary(self):

        print(
            "===== Research Summary ====="
        )


        print(
            f"Features evaluated: {len(self.metrics)}"
        )


        print(
            f"Analysis modules: {len(self.analysis)}"
        )


        print(
            f"Created: {self.metadata.get('created_at')}"
        )

    def save(self, path):
        destination = Path(path)
        destination.parent.mkdir(parents=True, exist_ok=True)

        with destination.open("wb") as file:
            pickle.dump(self, file)
