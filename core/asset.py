# model-eur-aggressive/core/asset.py
"""
Asset Class
"""
from dataclasses import dataclass
from typing import Optional
import pandas as pd
import numpy as np

TRADING_DAYS = 252

@dataclass
class Asset:
    isin: str
    name: str
    ticker: str
    allocation_w: float  # portfolio weights (0-1)
    asset_class: Optional[str] = None  # to add later
    sector: Optional[str] = None
    region: Optional[str] = None
    
    # time-series (set later)
    prices: Optional[pd.Series] = None
    returns: Optional[pd.Series] = None
    
    def attach_prices(self, prices: pd.Series) -> None:
        "For prices and performance calculations"
        self.prices
        