import time
import cProfile
import pstats
from typing import List, Tuple

from models import MarketDataPoint
from strategies import NaiveMovingAverageStrategy, WindowedMovingAverageStrategy


def run_strategy(strategy, data: List[MarketDataPoint]) -> None:
    for tick in data:
        strategy.generate_signals(tick)


def time_execution(strategy, data: List[MarketDataPoint]) -> float:
    start = time.time()
    run_strategy(strategy, data)
    end = time.time()
    return end - start


def profile_with_cprofile(strategy, data: List[MarketDataPoint], output_file: str) -> None:
    profiler = cProfile.Profile()
    profiler.enable()
    run_strategy(strategy, data)
    profiler.disable()

    with open(output_file, "w") as f:
        stats = pstats.Stats(profiler, stream=f)
        stats.sort_stats("cumulative")
        stats.print_stats()


def benchmark_strategies(
    data: List[MarketDataPoint],
    window_size: int
) -> List[Tuple[str, float]]:
    results = []

    naive = NaiveMovingAverageStrategy()
    naive_time = time_execution(naive, data)
    results.append(("NaiveMovingAverageStrategy", naive_time))

    windowed = WindowedMovingAverageStrategy(window_size)
    windowed_time = time_execution(windowed, data)
    results.append(("WindowedMovingAverageStrategy", windowed_time))

    return results
