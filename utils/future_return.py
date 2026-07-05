def build_future_return(records, horizon):

    future_returns = []

    for i in range(len(records) - horizon):

        current = records[i]["mid_price"]

        future = records[i + horizon]["mid_price"]

        ret = (future - current) / current

        future_returns.append(ret)

    return future_returns