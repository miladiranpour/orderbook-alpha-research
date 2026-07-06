import features.imbalance as imbalance
import features.weighted_imbalance as weighted_imbalance
import features.queue_imbalance as queue_imbalance
import features.microprice as microprice
import features.book_pressure as book_pressure
import features.ofi as ofi


FEATURES = {

    "Imbalance": imbalance.calculate,

    "Weighted Imbalance": weighted_imbalance.calculate,

    "Queue Imbalance": queue_imbalance.calculate,

    "Microprice": microprice.calculate,

    "Book Pressure": book_pressure.calculate,

    "OFI": ofi.calculate

}