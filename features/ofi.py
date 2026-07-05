def calculate(records):

    values = [0]

    for i in range(1, len(records)):

        prev = records[i - 1]

        cur = records[i]

        bid_change = (

            cur["bid_volumes"][0]

            -

            prev["bid_volumes"][0]

        )

        ask_change = (

            cur["ask_volumes"][0]

            -

            prev["ask_volumes"][0]

        )

        values.append(

            bid_change - ask_change

        )

    return values