class ResearchPresenter:
    """Prepare persisted research results for dashboard components."""

    def __init__(self, result):
        self.result = result

    def overview(self):
        metadata = self.result.metadata or {}

        return {
            "market": metadata.get("market", "BTC/USDT"),
            "horizon": metadata.get("horizon"),
            "records": metadata.get("records"),
        }

    def ranking(self):
        return self.result.ranking

    def metrics(self):
        return self.result.metrics

    def analyses(self):
        return self.result.analysis or {}

    def analysis(self, feature_name):
        return (self.result.analysis or {}).get(feature_name, {})
