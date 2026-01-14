from typing import List

from data_loader import load_market_data
from profiler import benchmark_strategies, profile_with_cprofile
from reporting import plot_runtime
from strategies import NaiveMovingAverageStrategy, WindowedMovingAverageStrategy



def run_experiment(
    csv_path: str,
    window_size: int,
    input_sizes: List[int]
) -> None:
    naive_times = []
    windowed_times = []

    full_data = load_market_data(csv_path)

    for size in input_sizes:
        data = full_data[:size]

        results = benchmark_strategies(data, window_size)

        for name, exec_time in results:
            if name == "NaiveMovingAverageStrategy":
                naive_times.append(exec_time)
            elif name == "WindowedMovingAverageStrategy":
                windowed_times.append(exec_time)

        # Optional detailed profiling (only once for largest input)
        if size == input_sizes[-1]:
            profile_with_cprofile(
                NaiveMovingAverageStrategy(),
                data,
                "naive_cprofile.txt"
            )
            profile_with_cprofile(
                WindowedMovingAverageStrategy(window_size),
                data,
                "windowed_cprofile.txt"
            )

    plot_runtime(
        input_sizes=input_sizes,
        naive_times=naive_times,
        windowed_times=windowed_times
    )


if __name__ == "__main__":
    CSV_PATH = "market_data.csv"
    WINDOW_SIZE = 10
    INPUT_SIZES = [1000, 10000, 100000]

    run_experiment(
        csv_path=CSV_PATH,
        window_size=WINDOW_SIZE,
        input_sizes=INPUT_SIZES
    )
