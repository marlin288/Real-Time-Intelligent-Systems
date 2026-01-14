import csv
from datetime import datetime
from typing import List
from datetime import timedelta
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
    
def generate_synthetic_market_data(
    base_data: list,
    target_size: int
) -> list:
    if not base_data:
        raise ValueError("Base market data is empty")

    synthetic_data = []
    current_time = base_data[0].timestamp

    for i in range(target_size):
        base_point = base_data[i % len(base_data)]

        price = base_point.price * (1 + random.uniform(-0.001, 0.001))

        synthetic_data.append(
            MarketDataPoint(
                timestamp=current_time,
                symbol=base_point.symbol,
                price=round(price, 2)
            )
        )

        # simulate streaming ticks (1-second intervals)
        current_time += timedelta(seconds=1)

    return synthetic_data
