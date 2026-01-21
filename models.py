# models.py
from dataclasses import dataclass
from datetime import datetime
from abc import ABC, abstractmethod
from typing import List


@dataclass(frozen=True)
class MarketDataPoint:
    """
    Immutable market tick.
    Space Complexity: O(1) per instance
    """
    timestamp: datetime
    symbol: str
    price: float


class Strategy(ABC):
    """
    Abstract base class for all trading strategies.
    """

    @abstractmethod
    def generate_signals(self, tick: MarketDataPoint) -> List[str]:
        """
        Processes one tick and emits trading signals.
        """
        pass
