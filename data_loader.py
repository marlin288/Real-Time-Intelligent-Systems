# data_loader.py

import csv
from datetime import datetime
from typing import List

import csv
import random
from datetime import datetime, timedelta
from collections import deque
from statistics import mean
import time
import tracemalloc
import pandas as pd

from models import MarketDataPoint

csv_path = "market_data.csv"
n_rows = 10000

start_time = datetime(2020, 1, 1)
price = 100.0

with open(csv_path, "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["timestamp", "symbol", "price"])
    for i in range(n_rows):
        price += random.uniform(-1, 1)
        writer.writerow([
            (start_time + timedelta(minutes=i)).isoformat(),
            "SIM",
            round(price, 2)
        ])

# ---------- Load data ----------
class MarketDataPoint:
    def __init__(self, timestamp, symbol, price):
        self.timestamp = timestamp
        self.symbol = symbol
        self.price = price

data = []
with open(csv_path, newline="") as f:
    reader = csv.DictReader(f)
    for row in reader:
        data.append(
            MarketDataPoint(
                datetime.fromisoformat(row["timestamp"]),
                row["symbol"],
                float(row["price"])
            )
        )



def load_market_data(csv_path: str) -> List[MarketDataPoint]:
    """
    Loads market data from CSV into immutable MarketDataPoint objects.

    Time Complexity:
        O(n)

    Space Complexity:
        O(n)
    """
    data: List[MarketDataPoint] = []

    with open(csv_path, mode="r", newline="") as file:
        reader = csv.DictReader(file)

        for row in reader:
            data.append(
                MarketDataPoint(
                    timestamp=datetime.fromisoformat(row["timestamp"]),
                    symbol=row["symbol"],
                    price=float(row["price"])
                )
            )

    return data
