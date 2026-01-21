# Runtime and Space Complexity in Financial Signal Processing

## Overview
This project investigates how algorithmic design choices affect **runtime performance** and **memory usage** in financial signal processing systems. A Python-based framework is implemented to ingest market data from a CSV file, apply multiple trading strategies with differing computational complexities, and empirically evaluate their performance using profiling tools.

The project focuses on moving average–based trading strategies implemented in both naive and optimized forms. By comparing theoretical Big-O analysis with empirical profiling results, the project demonstrates why efficient algorithmic design is critical for scalable trading infrastructure.

---

## Project Structure and Modules

### `data_loader.py`
Handles data ingestion and preparation. This module reads simulated market data from a CSV file and parses each row into immutable `MarketDataPoint` objects. It also supports the generation of simulated CSV market data used for testing and benchmarking.

### `models.py`
Defines the core data structures and interfaces used throughout the project. This includes the immutable `MarketDataPoint` dataclass and the abstract `Strategy` base class, which enforces a consistent interface across all trading strategies.

### `strategies.py`
Contains concrete trading strategy implementations:
- **NaiveMovingAverageStrategy** recomputes the moving average at each tick using historical prices.
- **WindowedMovingAverageStrategy** maintains a fixed-size sliding window and updates the moving average incrementally to improve efficiency.

### `profiler.py`
Provides utilities for measuring execution time and peak memory usage for each strategy. Profiling is performed using high-resolution timing and Python memory tracing tools.

### `reporting.py`
Generates visualizations such as runtime versus input size and memory usage versus input size. These plots are used to compare strategy scalability and support conclusions drawn in the analysis.

### `main.py`
Serves as the orchestration layer. This script coordinates data loading, strategy execution, profiling, and plot generation. Running this file executes the full experimental pipeline.

### `tests/`
Contains unit tests that validate the correctness and consistency of strategy implementations. Tests ensure that optimized strategies produce the same trading signals as naive strategies under identical conditions.

### `complexity_report.md`
Provides a detailed discussion of theoretical and empirical complexity results, including tables, plots, and interpretive analysis.

---

## Setup Instructions

1. Ensure **Python 3.9 or later** is installed.
2. (Recommended) Create and activate a virtual environment.
3. Install required dependencies:

bash
pip install matplotlib pytest
### `Running the Project`
To execute the full pipeline, including data ingestion, strategy evaluation, and profiling:

###`python main.py`


This will generate runtime measurements and performance plots for different input sizes.

###`Running Tests`

To validate correctness and ensure strategy consistency:

### `pytest`


All tests should pass without errors.