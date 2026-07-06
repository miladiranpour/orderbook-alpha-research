from utils import snapshot


def calculate(records):

    values = []

    for row in records:

        bid_price = snapshot.best_bid_price(row)
        ask_price = snapshot.best_ask_price(row)

        bid_volume = snapshot.best_bid_volume(row)
        ask_volume = snapshot.best_ask_volume(row)

        micro = (

            ask_price * bid_volume +

            bid_price * ask_volume

        ) / (

            bid_volume + ask_volume

        )

        mid = snapshot.mid_price(row)

        values.append(

            (micro - mid)

            / mid

        )

    return values