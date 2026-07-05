import numpy as np

import research.analysis as analysis
import research.plots as plots

def run(
        feature_name,
        feature_values,
        future_returns,
        labels
):

    print("=" * 60)

    print(f"Feature Report : {feature_name}")

    print("=" * 60)

    corr = analysis.correlation(
        feature_values,
        future_returns
    )

    print(f"Correlation : {corr:.4f}")

    print()

    avg = analysis.average_return(
        feature_values,
        future_returns
    )

    prob = analysis.up_probability(
        feature_values,
        labels
    )

    table = analysis.threshold_analysis(

        feature_values,

        future_returns,

        np.arange(-1, 1.05, 0.05)

    )

    print(table)

    plots.histogram(feature_values)

    plots.scatter(
        feature_values,
        future_returns
    )

    plots.average_return_plot(avg)

    plots.probability_plot(prob)