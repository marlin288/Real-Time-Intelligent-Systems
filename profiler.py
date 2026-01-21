# profiler.py
import time
import tracemalloc
from typing import List, Dict

from models import MarketDataPoint, Strategy


def profile_strategy(
    strategy: Strategy,
    data: List[MarketDataPoint]
) -> Dict[str, float]:
    """
    Measures execution time and peak memory usage.
    """
    tracemalloc.start()
    start = time.perf_counter()

    for tick in data:
        strategy.generate_signals(tick)

    elapsed = time.perf_counter() - start
    _, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    return {
        "time_seconds": elapsed,
        "peak_memory_mb": peak / (1024 ** 2),
    }
