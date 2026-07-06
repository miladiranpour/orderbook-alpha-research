from utils import snapshot


def calculate(records):

    values = []

    for row in records:

        bid = snapshot.best_bid_volume(row)

        ask = snapshot.best_ask_volume(row)

        values.append(

            (bid - ask)

            /

            (bid + ask)

        )

    return values