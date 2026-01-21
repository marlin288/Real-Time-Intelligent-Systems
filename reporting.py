# reporting.py
import matplotlib.pyplot as plt


def plot_scaling(results, title, ylabel, filename):
    sizes = sorted(results.keys())
    values = [results[n] for n in sizes]

    plt.figure()
    plt.plot(sizes, values, marker="o")
    plt.xlabel("Number of Ticks")
    plt.ylabel(ylabel)
    plt.title(title)
    plt.grid(True)
    plt.savefig(filename)
    plt.close()
