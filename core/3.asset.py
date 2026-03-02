# portfolio_engine/core/asset.py
from dataclasses import dataclass
from typing import Optional
import pandas as pd

@dataclass
class Asset:
    isin: str
    name: str
    ticker: str
    weight: float              # peso nel portafoglio
    asset_class: str
    sector: Optional[str] = None
    region: Optional[str] = None
    country: Optional[str] = None
    currency: Optional[str] = None
    market_type: Optional[str] = None

    # time-series set later
    prices: Optional[pd.Series] = None
    returns: Optional[pd.Series] = None

    def attach_prices(self, prices: pd.Series) -> None:
        self.prices = prices.dropna()
        self.returns = self.prices.pct_change().dropna()
