# portfolio_engine/osint/sentiment.py
from typing import List
import pandas as pd

def fetch_news_for_ticker(ticker: str, limit: int = 20) -> List[str]:
    """
    Placeholder: usa API news (NewsAPI, Finnhub, ecc.) per headline.
    """
    raise NotImplementedError

def score_finbert(texts: List[str]) -> pd.DataFrame:
    """
    Usa FinBERT per calcolare sentiment su lista di testi.
    """
    raise NotImplementedError
