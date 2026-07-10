from research.metrics import (
    correlation,
    sharpe,
    win_rate,
    average_return
)


def evaluate(

    name,

    feature,

    future

):

    return {

        "Feature": name,

        "Correlation":
            correlation(
                feature,
                future
            ),

        "WinRate":
            win_rate(
                feature,
                future
            ),

        "AverageReturn":
            average_return(
                feature,
                future
            ),

        "Sharpe":
            sharpe(
                feature,
                future
            )

    }