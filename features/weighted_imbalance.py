def calculate(records, levels=20):

    values = []

    for row in records:

        bid = 0
        ask = 0

        for i in range(levels):

            weight = 1 / (i + 1)

            bid += row["bid_volumes"][i] * weight
            ask += row["ask_volumes"][i] * weight

        values.append(

            (bid - ask) /
            (bid + ask)

        )

    return values