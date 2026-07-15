from .correlation import calculate as correlation
from .average_return import calculate as average_return
from .win_rate import calculate as win_rate
from .sharpe import calculate as sharpe
from .test_metric import calculate as test_metric

METRICS = {

    "Correlation": correlation,

    "Average Return": average_return,

    "Win Rate": win_rate,

    "Sharpe": sharpe,
    
    "Test_metric": test_metric

}

