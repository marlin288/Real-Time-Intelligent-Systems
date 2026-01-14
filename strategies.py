from collections import deque
from typing import List
from models import Strategy, MarketDataPoint

class NaiveMovingAverageStrategy(Strategy):
    def __init__(self):
        self.prices: List[float] = []

    def generate_signals(self, tick: MarketDataPoint) -> List[str]:
        self.prices.append(tick.price)

        average_price = sum(self.prices) / len(self.prices)

        if tick.price > average_price:
            return ["BUY"]
        elif tick.price < average_price:
            return ["SELL"]
        else:
            return []


class WindowedMovingAverageStrategy(Strategy):
    def __init__(self, window_size: int):
        self.window_size = window_size
        self.window = deque()
        self.running_sum = 0.0

    def generate_signals(self, tick: MarketDataPoint) -> List[str]:
        self.window.append(tick.price)
        self.running_sum += tick.price

        if len(self.window) > self.window_size:
            removed_price = self.window.popleft()
            self.running_sum -= removed_price

        average_price = self.running_sum / len(self.window)

        if tick.price > average_price:
            return ["BUY"]
        elif tick.price < average_price:
            return ["SELL"]
        else:
            return []
