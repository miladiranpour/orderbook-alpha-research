def best_bid_price(row):
    return row["bids"][0][0]


def best_bid_volume(row):
    return row["bids"][0][1]


def best_ask_price(row):
    return row["asks"][0][0]


def best_ask_volume(row):
    return row["asks"][0][1]


def bid_prices(row):
    return [price for price, volume in row["bids"]]


def ask_prices(row):
    return [price for price, volume in row["asks"]]


def bid_volumes(row):
    return [volume for price, volume in row["bids"]]


def ask_volumes(row):
    return [volume for price, volume in row["asks"]]


def bid_volume_20(row):
    return row["bid_volume_20"]


def ask_volume_20(row):
    return row["ask_volume_20"]


def mid_price(row):
    return row["mid_price"]


def spread(row):
    return row["spread"]

def bids(row):
    return row["bids"]


def asks(row):
    return row["asks"]