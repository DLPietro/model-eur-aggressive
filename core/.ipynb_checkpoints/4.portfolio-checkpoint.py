# portfolio_engine/core/portfolio.py
from dataclasses import dataclass, field
from typing import Dict, List
import pandas as pd
import numpy as np
from .asset import Asset

@dataclass
class Portfolio:
    assets: Dict[str, Asset] = field(default_factory=dict)  # key: isin

    def weights_vector(self, tickers: List[str]) -> np.ndarray:
        return np.array([self.assets_by_ticker[t].weight for t in tickers])

    @property
    def assets_by_ticker(self) -> Dict[str, Asset]:
        return {a.ticker: a for a in self.assets.values()}

    def to_dataframe(self) -> pd.DataFrame:
        rows = []
        for a in self.assets.values():
            rows.append({
                "isin": a.isin,
                "ticker": a.ticker,
                "name": a.name,
                "weight": a.weight,
                "asset_class": a.asset_class,
                "sector": a.sector,
                "region": a.region,
                "country": a.country,
                "market_type": a.market_type,
            })
        return pd.DataFrame(rows)

    def portfolio_returns(self, prices: pd.DataFrame) -> pd.Series:
        rets = prices.pct_change().dropna()
        w = self.weights_vector(prices.columns)
        return (rets * w).sum(axis=1)
