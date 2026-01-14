import matplotlib.pyplot as plt
from typing import List, Tuple


def plot_runtime(
    input_sizes: List[int],
    naive_times: List[float],
    windowed_times: List[float],
    output_path: str = "runtime_comparison.png"
) -> None:
    plt.figure(figsize=(8, 5))
    plt.plot(input_sizes, naive_times, label="Naive Moving Average", marker="o")
    plt.plot(input_sizes, windowed_times, label="Windowed Moving Average", marker="o")

    plt.xlabel("Number of Ticks")
    plt.ylabel("Execution Time (seconds)")
    plt.title("Runtime vs Input Size")
    plt.legend()
    plt.grid(True)

    plt.savefig(output_path)
    plt.close()


def plot_memory(
    input_sizes: List[int],
    naive_memory: List[float],
    windowed_memory: List[float],
    output_path: str = "memory_comparison.png"
) -> None:
    plt.figure(figsize=(8, 5))
    plt.plot(input_sizes, naive_memory, label="Naive Moving Average", marker="o")
    plt.plot(input_sizes, windowed_memory, label="Windowed Moving Average", marker="o")

    plt.xlabel("Number of Ticks")
    plt.ylabel("Peak Memory Usage (MB)")
    plt.title("Memory Usage vs Input Size")
    plt.legend()
    plt.grid(True)

    plt.savefig(output_path)
    plt.close()


def generate_runtime_table(
    input_sizes: List[int],
    naive_times: List[float],
    windowed_times: List[float]
) -> List[Tuple[int, float, float]]:
    table = []
    for i in range(len(input_sizes)):
        table.append((input_sizes[i], naive_times[i], windowed_times[i]))
    return table
