import numpy as np

from utils import snapshot


def calculate(records, levels=20):

    values = []

    for row in records:

        bid = np.sum(

            snapshot.bid_volumes(row)[:levels]

        )

        ask = np.sum(

            snapshot.ask_volumes(row)[:levels]

        )

        values.append(

            np.log(

                bid / ask

            )

        )

    return values