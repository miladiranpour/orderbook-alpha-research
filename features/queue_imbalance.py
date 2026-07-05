def calculate(records):

    values = []

    for row in records:

        bid = row["bid_volumes"][0]

        ask = row["ask_volumes"][0]

        values.append(

            (bid - ask) /
            (bid + ask)

        )

    return values