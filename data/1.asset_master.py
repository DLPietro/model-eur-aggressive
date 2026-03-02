# portfolio_engine/data/asset_master.py
from dataclasses import dataclass
from typing import Optional
import pandas as pd

@dataclass
class AssetMeta:
    isin: str
    name: str
    ticker: str
    asset_class: str          # Equity, Bond, Cash, Crypto, Commodity, REIT…
    sector: Optional[str]     # GICS/ICB sector
    region: Optional[str]     # Europe, North America, EM Asia…
    country: Optional[str]
    currency: Optional[str]
    market_type: Optional[str]  # DM, EM, Frontier

class AssetMaster:
    def __init__(self, df_master: pd.DataFrame):
        self.df = df_master.copy()

    @classmethod
    def from_csv(cls, path: str) -> "AssetMaster":
        df = pd.read_csv(path)
        # normalizza colonne ecc.
        return cls(df)

    def lookup(self, isin: str) -> Optional[AssetMeta]:
        row = self.df.loc[self.df["isin"] == isin].squeeze()
        if row.empty:
            return None
        return AssetMeta(
            isin=row["isin"],
            name=row["name"],
            ticker=row["ticker"],
            asset_class=row["asset_class"],
            sector=row.get("sector"),
            region=row.get("region"),
            country=row.get("country"),
            currency=row.get("currency"),
            market_type=row.get("market_type"),
        )
