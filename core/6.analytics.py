# portfolio_engine/core/analytics.py
import pandas as pd
import numpy as np

def breakdown(portfolio_df: pd.DataFrame, by: str) -> pd.Series:
    """
    Somma i pesi per asset_class/sector/region/market_type ecc.
    """
    return portfolio_df.groupby(by)["weight"].sum().sort_values(ascending=False)

def herfindahl_index(weights: pd.Series) -> float:
    """
    HHI per misurare concentrazione (somma pesi^2).
    """
    w = weights.values
    return np.sum(w ** 2)

def correlation_matrix(returns_df: pd.DataFrame) -> pd.DataFrame:
    return returns_df.corr()
