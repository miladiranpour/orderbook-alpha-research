def calculate(records):

    values = []

    for row in records:

        bid_price = row["bid_prices"][0]

        ask_price = row["ask_prices"][0]

        bid_volume = row["bid_volumes"][0]

        ask_volume = row["ask_volumes"][0]

        micro = (

            ask_price * bid_volume +

            bid_price * ask_volume

        ) / (

            bid_volume + ask_volume

        )

        mid = (

            bid_price + ask_price

        ) / 2

        values.append(

            (micro - mid) / mid

        )

    return values