import ccxt
import json
import time
from datetime import datetime

exchange = ccxt.binance()

for _ in range(1800):

    ob = exchange.fetch_order_book("BTC/USDT")

    best_bid = ob["bids"][0][0]
    best_ask = ob["asks"][0][0]

    mid_price = (best_bid + best_ask) / 2
    spread = best_ask - best_bid
    
    bid_volume = sum(v for p, v in ob["bids"][:20])
    ask_volume = sum(v for p, v in ob["asks"][:20])

    imbalance = (
                    (bid_volume - ask_volume)
                    / (bid_volume + ask_volume)
                )

    snapshot = {
        "timestamp": datetime.utcnow().isoformat(),
        "unix_time": time.time(),

        "best_bid": best_bid,
        "best_ask": best_ask,

        "mid_price": mid_price,
        "spread": spread,

        "bids": ob["bids"][:20],
        "asks": ob["asks"][:20],
        
        "bid_volume_20": bid_volume,
        "ask_volume_20": ask_volume,
        "imbalance_20": imbalance
    }

    with open("orderbook.jsonl", "a") as f:
        f.write(json.dumps(snapshot) + "\n")

    time.sleep(1)
