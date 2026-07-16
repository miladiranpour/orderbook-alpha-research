from .correlation import calculate as correlation
from .average_return import calculate as average_return
from .win_rate import calculate as win_rate
from .sharpe import calculate as sharpe


METRICS = {

    "Correlation": {

        "function": correlation,

        "maximize": True,

        "precision": 6,

        "weight": 1.0,

        "description": "Pearson Correlation"

    },

    "Average Return": {

        "function": average_return,

        "maximize": True,

        "precision": 8,

        "weight": 1.0,

        "description": "Average Future Return"

    },

    "Win Rate": {

        "function": win_rate,

        "maximize": True,

        "precision": 4,

        "weight": 1.0,

        "description": "Winning Percentage"

    },

    "Sharpe": {

        "function": sharpe,

        "maximize": True,

        "precision": 4,

        "weight": 2.0,

        "description": "Sharpe Ratio"

    }

}