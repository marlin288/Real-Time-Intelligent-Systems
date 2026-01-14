from datetime import datetime
from models import MarketDataPoint
from strategies import NaiveMovingAverageStrategy, WindowedMovingAverageStrategy

def test_naive_strategy_basic():
    strategy = NaiveMovingAverageStrategy()

    tick1 = MarketDataPoint(datetime.now(), "AAPL", 10.0)
    tick2 = MarketDataPoint(datetime.now(), "AAPL", 20.0)
    tick3 = MarketDataPoint(datetime.now(), "AAPL", 15.0)

    assert strategy.generate_signals(tick1) == []
    assert strategy.generate_signals(tick2) == ["BUY"]
    assert strategy.generate_signals(tick3) == ["SELL"]


def test_windowed_strategy_basic():
    strategy = WindowedMovingAverageStrategy(window_size=2)

    tick1 = MarketDataPoint(datetime.now(), "AAPL", 10.0)
    tick2 = MarketDataPoint(datetime.now(), "AAPL", 20.0)
    tick3 = MarketDataPoint(datetime.now(), "AAPL", 15.0)

    assert strategy.generate_signals(tick1) == []
    assert strategy.generate_signals(tick2) == ["BUY"]
    assert strategy.generate_signals(tick3) == ["SELL"]


def test_window_size_limit():
    strategy = WindowedMovingAverageStrategy(window_size=2)

    tick1 = MarketDataPoint(datetime.now(), "AAPL", 10.0)
    tick2 = MarketDataPoint(datetime.now(), "AAPL", 20.0)
    tick3 = MarketDataPoint(datetime.now(), "AAPL", 30.0)

    strategy.generate_signals(tick1)
    strategy.generate_signals(tick2)
    strategy.generate_signals(tick3)

    assert len(strategy.window) == 2

