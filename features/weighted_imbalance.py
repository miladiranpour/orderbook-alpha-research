from utils import snapshot


def calculate(records, levels=20):

    values = []

    for row in records:

        bids = snapshot.bid_volumes(row)

        asks = snapshot.ask_volumes(row)

        bid = 0
        ask = 0

        for i in range(levels):

            weight = 1 / (i + 1)

            bid += bids[i] * weight

            ask += asks[i] * weight

        values.append(

            (bid - ask)

            /

            (bid + ask)

        )

    return values