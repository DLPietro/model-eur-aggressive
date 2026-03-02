# portfolio_engine/core/backtesting.py
import pandas as pd
from typing import Literal
from .portfolio import Portfolio

def backtest_static_weights(
    portfolio: Portfolio,
    prices: pd.DataFrame,
    rebalance: Literal["none","monthly","annual"] = "annual",
) -> pd.Series:
    """
    Ritorno cumulativo del portafoglio con ribilanciamento periodico.
    """
    rets = prices.pct_change().dropna()
    w = portfolio.weights_vector(prices.columns)
    if rebalance == "none":
        return (1 + (rets * w).sum(axis=1)).cumprod()

    values = []
    value = 1.0
    units = (value * w) / prices.iloc[0]
    for date, row in prices.iterrows():
        value = (row * units).sum()
        # condizione di ribilanciamento grezza
        if rebalance == "annual" and date.month == 1 and date.day <= 3:
            units = (value * w) / row
        if rebalance == "monthly" and date.day <= 3:
            units = (value * w) / row
        values.append(value)
    equity = pd.Series(values, index=prices.index)
    return equity / equity.iloc[0]
