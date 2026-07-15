from datetime import datetime, timezone

import pandas as pd

from features.registry import FEATURES
from research.analysis.registry import PLOT_ANALYSIS, TABLE_ANALYSIS
from research.evaluator import evaluate
from research.ranking import build as build_ranking
from research.result import ResearchResult
from utils.alignment import align


class ResearchEngine:
    """Run the registered order-book features through the research pipeline."""

    def __init__(self, records, future_returns, labels, config=None):
        self.records = records
        self.future_returns = future_returns
        self.labels = labels
        self.config = config or {}

    def run(self):
        metric_rows = []
        analysis_results = {}
        plot_results = {}

        for feature_name, feature_function in FEATURES.items():
            feature_values = feature_function(self.records)
            feature_values, future_returns = align(
                feature_values, self.future_returns
            )
            feature_values, labels = align(feature_values, self.labels)

            metric_rows.append(
                evaluate(feature_name, feature_values, future_returns)
            )

            feature_analysis = {}
            for analysis_name, analysis_function in TABLE_ANALYSIS.items():
                if analysis_name in {"Probability", "Decile"}:
                    feature_analysis[analysis_name] = analysis_function(
                        feature_values, labels
                    )
                else:
                    feature_analysis[analysis_name] = analysis_function(
                        feature_values, future_returns
                    )
            analysis_results[feature_name] = feature_analysis

            feature_plots = {}
            for plot_name, plot_function in PLOT_ANALYSIS.items():
                if plot_name == "Histogram":
                    feature_plots[plot_name] = plot_function(
                        feature_values, feature_name
                    )
                else:
                    feature_plots[plot_name] = plot_function(
                        feature_values, future_returns, feature_name
                    )
            plot_results[feature_name] = feature_plots

        metrics = pd.DataFrame(metric_rows)
        ranking = build_ranking(metrics.copy()) if not metrics.empty else metrics

        return ResearchResult(
            metrics=metrics,
            analysis=analysis_results,
            ranking=ranking,
            plots=plot_results,
            metadata={
                "created_at": datetime.now(timezone.utc).isoformat(),
                "horizon": self.config.get("horizon"),
                "records": len(self.records),
            },
        )
