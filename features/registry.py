from .imbalance import calculate as imbalance
from .weighted_imbalance import calculate as weighted_imbalance
from .queue_imbalance import calculate as queue_imbalance
from .microprice import calculate as microprice
from .book_pressure import calculate as book_pressure
from .ofi import calculate as ofi


FEATURES = {

    "Imbalance": {

        "function": imbalance,

        "group": "Volume",

        "description": "Order Book Imbalance",

        "version": "1.0"

    },

    "Weighted Imbalance": {

        "function": weighted_imbalance,

        "group": "Volume",

        "description": "Distance Weighted Imbalance",

        "version": "1.0"

    },

    "Queue Imbalance": {

        "function": queue_imbalance,

        "group": "Queue",

        "description": "Best Queue Imbalance",

        "version": "1.0"

    },

    "Microprice": {

        "function": microprice,

        "group": "Price",

        "description": "Microprice",

        "version": "1.0"

    },

    "Book Pressure": {

        "function": book_pressure,

        "group": "Pressure",

        "description": "Book Pressure",

        "version": "1.0"

    },

    "OFI": {

        "function": ofi,

        "group": "Flow",

        "description": "Order Flow Imbalance",

        "version": "1.0"

    }

}