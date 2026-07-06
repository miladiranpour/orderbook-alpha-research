from utils import snapshot


def calculate(records):

    values = [0]

    for i in range(1, len(records)):

        prev = records[i - 1]

        cur = records[i]

        bid_change = (

            snapshot.best_bid_volume(cur)

            -

            snapshot.best_bid_volume(prev)

        )

        ask_change = (

            snapshot.best_ask_volume(cur)

            -

            snapshot.best_ask_volume(prev)

        )

        values.append(

            bid_change - ask_change

        )

    return values