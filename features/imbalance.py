def calculate(records):

    values = []

    for row in records:

        bid = row["bid_volume_20"]

        ask = row["ask_volume_20"]

        imbalance = (
            bid - ask
        ) / (
            bid + ask
        )

        values.append(imbalance)

    return values