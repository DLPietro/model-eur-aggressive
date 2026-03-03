# model-eur-aggressive/core/risk_metrics.py
"""
Risk Metrics
"""
import numpy as np
import pandas as pd
from typing import Optional

TRADING_DAYS = 252
DEFAULT_RF = 0.02  # 2% risk-free annuo

def annualized_return(rets: pd.Series) -> float:
    """Annual Return"""
    return rets.mean() * TRADING_DAYS

def annualized_volatility(rets: pd.Series) -> float:
    """Annual Volatility"""
    return rets.std() * np.sqrt(TRADING_DAYS)

def sharpe_ratio(rets: pd.Series, rf: float = DEFAULT_RF) -> float:
    """Sharpe ratio (annuo)"""
    excess = rets - rf / TRADING_DAYS
    return annualized_return(excess) / annualized_volatility(rets)

def sortino_ratio(rets: pd.Series, rf: float = DEFAULT_RF) -> float:
    """Sortino ratio (annuo, downside vol)"""
    excess = rets - rf / TRADING_DAYS
    downside = excess[excess < 0]
    downside_vol = downside.std() * np.sqrt(TRADING_DAYS)
    return annualized_return(excess) / downside_vol

def max_drawdown(rets: pd.Series) -> float:
    """Max drawdown (%)"""
    cum = (1 + rets).cumprod()
    peak = cum.cummax()
    dd = (cum / peak) - 1
    return dd.min()

def historical_var(rets: pd.Series, alpha: float = 0.95) -> float:
    """VaR daily"""
    return np.quantile(rets, 1 - alpha)

def calmar_ratio(rets: pd.Series) -> float:
    """Calmar = ann_ret / |max_dd|"""
    ann_ret = annualized_return(rets)
    mdd = max_drawdown(rets)
    return ann_ret / abs(mdd)

def beta(port_rets: pd.Series, bench_rets: pd.Series) -> float:
    """Beta vs benchmark"""
    aligned
