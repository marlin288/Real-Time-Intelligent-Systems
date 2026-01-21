# main.py
import csv
import random
from datetime import datetime, timedelta
from collections import deque
from statistics import mean
import time
import tracemalloc
from data_loader import load_market_data
from strategies import (
    NaiveMovingAverageStrategy,
    WindowedMovingAverageStrategy
)
from profiler import profile_strategy
from reporting import plot_scaling

SIZES = [1_000, 10_000, 100_000]


def main():
   
    data = load_market_data("market_data.csv")

    runtime_naive = {}
    runtime_opt = {}

    for n in SIZES:
        subset = data[:n]

        runtime_naive[n] = profile_strategy(
            NaiveMovingAverageStrategy(), subset
        )["time_seconds"]

        runtime_opt[n] = profile_strategy(
            WindowedMovingAverageStrategy(), subset
        )["time_seconds"]

    plot_scaling(runtime_naive, "Naive MA Runtime", "Seconds", "naive_runtime.png")
    plot_scaling(runtime_opt, "Optimized MA Runtime", "Seconds", "opt_runtime.png")
    

    print(runtime_naive, runtime_opt )



if __name__ == "__main__":
    main()
