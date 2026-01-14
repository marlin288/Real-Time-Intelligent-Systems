from dataclasses import dataclass
from datetime import datetime
from abc import ABC, abstractmethod
from typing import List


@dataclass(frozen=True)
class MarketDataPoint:
    """
    Immutable market data record.

    Space Complexity:
    - O(1) per MarketDataPoint
    - O(n) total for n data points stored in memory
    """
    timestamp: datetime
    symbol: str
    price: float


class Strategy(ABC):
    """
    Abstract base class for trading strategies.
    """

    @abstractmethod
    def generate_signals(self, tick: MarketDataPoint) -> List[str]:
        """
        Generate trading signals based on a single market data tick.

        Time Complexity:
        - Depends on concrete strategy implementation

        Space Complexity:
        - Depends on internal state maintained by the strategy
        """
        pass
