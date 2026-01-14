import csv
from datetime import datetime
from typing import List

from models import MarketDataPoint


def load_market_data(csv_path: str) -> List[MarketDataPoint]:
    data: List[MarketDataPoint] = []

    with open(csv_path, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            datapoint = MarketDataPoint(
                timestamp=datetime.fromisoformat(row["timestamp"]),
                symbol=row["symbol"],
                price=float(row["price"])
            )
            data.append(datapoint)

    return data
