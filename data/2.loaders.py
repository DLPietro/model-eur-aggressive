# portfolio_engine/data/loaders.py
from typing import List, Dict
import pandas as pd
import yfinance as yf

def load_portfolio_xlsx(path: str, sheet: str = None) -> pd.DataFrame:
    """
    Legge un portafoglio da Excel e restituisce df con:
    ['isin','weight','name', ...]
    """
    df = pd.read_excel(path, sheet_name=sheet or 0)
    # normalizza nomi, pesi in 0-1
    return df

def download_price_history(
    tickers: List[str], start: str, end: str = None, freq: str = "1d"
) -> pd.DataFrame:
    """
    Restituisce prices[date, ticker] (Adj Close)
    """
    data = yf.download(tickers, start=start, end=end, interval=freq)["Adj Close"]
    return data

def load_benchmark(ticker: str, start: str, end: str = None) -> pd.Series:
    return yf.download(ticker, start=start, end=end)["Adj Close"].rename("benchmark")
