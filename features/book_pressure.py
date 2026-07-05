import numpy as np

def calculate(records, levels=10):

    values = []

    for row in records:

        bid = np.sum(

            row["bid_volumes"][:levels]

        )

        ask = np.sum(

            row["ask_volumes"][:levels]

        )

        values.append(

            np.log(

                bid / ask

            )

        )

    return values