from .probability import calculate as probability
from .decile import calculate as decile
from .threshold import calculate as threshold
from .stability import calculate as stability

from .histogram import plot as histogram
from .scatter import plot as scatter


TABLE_ANALYSIS = {

    "Probability": probability,

    "Decile": decile,

    "Threshold": threshold,

    "Stability": stability

}


PLOT_ANALYSIS = {

    "Histogram": histogram,

    "Scatter": scatter

}