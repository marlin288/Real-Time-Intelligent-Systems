# strategies.py
from collections import deque
from typing import List
from statistics import mean

from models import MarketDataPoint, Strategy


class NaiveMovingAverageStrategy(Strategy):
    """
    Recomputes moving average from full price history.

    Time Complexity:
        Per tick: O(n)
        Total: O(n²)

    Space Complexity:
        O(n) — stores all historical prices
    """

    def __init__(self, window: int = 10):
        self.window = window
        self.prices: List[float] = []

    def generate_signals(self, tick: MarketDataPoint) -> List[str]:
        self.prices.append(tick.price)

        if len(self.prices) < self.window:
            return []

        avg = mean(self.prices[-self.window:])  # O(k) slice
        return ["BUY"] if tick.price > avg else ["SELL"]


class WindowedMovingAverageStrategy(Strategy):
    """
    Optimized moving average using a fixed-size buffer.

    Time Complexity:
        Per tick: O(1)
        Total: O(n)

    Space Complexity:
        O(k) — fixed window size
    """

    def __init__(self, window: int = 10):
        self.window = window
        self.buffer = deque(maxlen=window)
        self.running_sum = 0.0

    def generate_signals(self, tick: MarketDataPoint) -> List[str]:
        if len(self.buffer) == self.window:
            self.running_sum -= self.buffer[0]

        self.buffer.append(tick.price)
        self.running_sum += tick.price

        if len(self.buffer) < self.window:
            return []

        avg = self.running_sum / self.window
        return ["BUY"] if tick.price > avg else ["SELL"]
