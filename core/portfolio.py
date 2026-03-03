# model-eur-aggressive/core/portfolio.py
"""
Portfolio Class: Collecting assets + analysis method
"""
from typing import Dict, List, Optional
from dataclasses import dataclass
import pandas as pd
import numpy as np
from .asset import Asset

@dataclass
class Portfolio:
    assets: Dict[str, Asset] = None  # key: isin
    
    def __post_init__(self):
        if self.assets is None:
            self.assets = {}

    def add_asset(self, asset: Asset) -> None:
        "Adding asset at the portfolio"
        self.assets[asset.isin] = asset

    @classmethod
    def from_dataframe(cls, df: pd.DataFrame) -> "Portfolio":
        """Creating portfolio from DataFrame (isin, name, allocation_w, ticker)"""
        port = cls()
        for _, row in df.iterrows():
            asset = Asset(
                isin=row["isin"],
                name=row["name"],
                ticker=row.get("ticker", ""),
                allocation_w=row["allocation_w"]
            )
            port.add_asset(asset)
        return port

    def attach_prices_to_all(self, prices: pd.DataFrame) -> None:
        "Addoing asset prices"
        for isin, asset in self.assets.items():
            ticker = asset.ticker
            if ticker in prices.columns:
                asset.attach_prices(prices[ticker])
                print(f"✓ {asset.name}: prices loaded ({len(asset.prices)} obs)")
            else:
                print(f"✗ {asset.name}: ticker {ticker} not found")

    def portfolio_returns(self) -> pd.Series:
        """Calculating portfolio returns (weightered)"""
        # allinea tutte le serie returns
        all_rets = []
        for asset in self.assets.values():
            if asset.returns is not None:
                all_rets.append(asset.returns * asset.allocation_w)
        
        if not all_rets:
            raise ValueError("No returns data available")
        
        # concat + sum
        df_rets = pd.concat(all_rets, axis=1, join="inner")
        port_rets = df_rets.sum(axis=1)
        return port_rets

    def to_dataframe(self) -> pd.DataFrame:
        """Esporting portfolio as DataFrame"""
        rows

