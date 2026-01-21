# tests/test_strategies.py

from financial_signal_processing.strategies import NaiveMovingAverageStrategy, WindowedMovingAverageStrategy
from models import MarketDataPoint
from datetime import datetime


def test_strategies_consistency():
    ticks = [
        MarketDataPoint(datetime.now(), "TEST", p)
        for p in range(1, 21)
    ]

    naive = NaiveMovingAverageStrategy(window=5)
    opt = WindowedMovingAverageStrategy(window=5)

    naive_signals = []
    opt_signals = []

    for t in ticks:
        naive_signals.append(naive.generate_signals(t))
        opt_signals.append(opt.generate_signals(t))

    assert naive_signals == opt_signals
