# portfolio_engine/core/risk_metrics.py
import numpy as np
import pandas as pd

TRADING_DAYS = 252

def annualized_return(rets: pd.Series) -> float:
    return rets.mean() * TRADING_DAYS

def annualized_volatility(rets: pd.Series) -> float:
    return rets.std() * np.sqrt(TRADING_DAYS)

def sharpe_ratio(rets: pd.Series, rf: float = 0.0) -> float:
    excess = rets - rf / TRADING_DAYS
    return annualized_return(excess) / annualized_volatility(excess)

def sortino_ratio(rets: pd.Series, rf: float = 0.0) -> float:
    excess = rets - rf / TRADING_DAYS
    downside = excess[excess < 0]
    downside_vol = downside.std() * np.sqrt(TRADING_DAYS)
    return annualized_return(excess) / downside_vol

def max_drawdown(rets: pd.Series) -> float:
    cum = (1 + rets).cumprod()
    peak = cum.cummax()
    dd = cum / peak - 1
    return dd.min()

def historical_var(rets: pd.Series, alpha: float = 0.95) -> float:
    return np.quantile(rets, 1 - alpha)

def beta_alpha(port: pd.Series, bench: pd.Series) -> tuple[float, float]:
    aligned = pd.concat([port, bench], axis=1).dropna()
    cov = np.cov(aligned.iloc[:,0], aligned.iloc[:,1])
    beta = cov[0,1] / cov[1,1]
    # CAPM alpha su base annua
    rp = annualized_return(aligned.iloc[:,0])
    rb = annualized_return(aligned.iloc[:,1])
    rf = 0.0
    alpha = rp - (rf + beta * (rb - rf))
    return beta, alpha
