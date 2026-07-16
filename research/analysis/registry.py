from .probability import calculate as probability
from .decile import calculate as decile
from .threshold import calculate as threshold
from .stability import calculate as stability


TABLE_ANALYSIS = {

    "Probability": {

        "function": probability,

        "input": "labels",

        "output": "table",

        "description": "Probability Table"

    },

    "Decile": {

        "function": decile,

        "input": "labels",

        "output": "table",

        "description": "Decile Analysis"

    },

    "Threshold": {

        "function": threshold,

        "input": "future",

        "output": "table",

        "description": "Threshold Analysis"

    },

    "Stability": {

        "function": stability,

        "input": "future",

        "output": "table",

        "description": "Stability Analysis"

    }

}