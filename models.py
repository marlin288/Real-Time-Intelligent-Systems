from dataclasses import dataclass
from datetime import datetime
from abc import ABC, abstractmethod
from typing import List


@dataclass(frozen=True)
class MarketDataPoint:
    timestamp: datetime
    symbol: str
    price: float


class Strategy(ABC):
    """
    Abstract base class for trading strategies.
    """

    @abstractmethod
    def generate_signals(self, tick: MarketDataPoint) -> List[str]:
        pass
