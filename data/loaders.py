# model-eur-aggressive/data/loaders.py

import pandas as pd
import yfinance as yf
from typing import List, Optional
import numpy as np

def load_portfolio_csv(path: str) -> pd.DataFrame:
    
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip().str.lower()
    
    # Columns
    isin_col = next(c for c in df.columns if "isin" in c)
    name_col = next(c for c in df.columns if any(x in c for x in ["name", "nome"]))
    weight_col = next(c for c in df.columns if "alloc" in c or "peso" in c or "weight" in c)
    
    df = df[[isin_col, name_col, weight_col]].copy()
    df.columns = ["isin", "name", "allocation_pct"]
    
    # Calculating Percentage
    df["allocation_pct"] = pd.to_numeric(df["allocation_pct"], errors="coerce") / 100
    
    # Filter assets with weight > 0 and valid ISIN
    df = df[df["allocation_pct"] > 0].copy()
    df["isin"] = df["isin"].astype(str).str.strip()
    df = df[df["isin"].str.len() > 5]  # ISIN minimo 12 char, ma 5 per sicurezza
    
    # Add liquidity 5% if sum < 1
    total_weight = df["allocation_pct"].sum()
    if total_weight < 0.95:
        liquidity = pd.DataFrame({
            "isin": ["CASH-LIQ"], 
            "name": ["Liquidità / Cash"], 
            "allocation_pct": [0.05]
        })
        df = pd.concat([df, liquidity], ignore_index=True)
    
    # Normalize at 100%
    df["allocation_w"] = df["allocation_pct"] / df["allocation_pct"].sum()
    
    return df[["isin", "name", "allocation_w"]]

def download_price_history(
    tickers: List[str], 
    start: str = "2020-01-01", 
    end: Optional[str] = None,
    freq: str = "1d"
)

