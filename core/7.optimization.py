# portfolio_engine/core/optimization.py
import numpy as np
import pandas as pd
from typing import Dict

def mean_variance_opt(
    rets: pd.DataFrame,
    cov: pd.DataFrame | None = None,
    rf: float = 0.0,
    target: str = "max_sharpe",
    long_only: bool = True,
    bounds: Dict[str, tuple[float,float]] | None = None,
) -> pd.Series:
    """
    Piccolo wrapper per ottimizzazione Markowitz.
    In seguito puoi sostituirlo con skfolio o toolkit più evoluti.
    """
    # placeholder: qui userai cvxpy / scipy.optimize
    raise NotImplementedError
