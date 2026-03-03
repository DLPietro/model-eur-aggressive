# model-eur-aggressive/core/analytics.py
"""
Diversification, Correlation, Concentration Analysis
"""
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

def breakdown(portfolio_df: pd.DataFrame, by: str = "asset_class") -> pd.Series:
    """
    Breakdown per category (asset_class, sector, region...)
    """
    if by not in portfolio_df.columns:
        raise ValueError(f"Column '{by}' not found in portfolio")
    
    return portfolio_df.groupby(by)["allocation_w"].sum().sort_values(ascending=False)

def herfindahl_index(weights: pd.Series) -> float:
    """
    Herfindahl-Hirschman Index (concentration)
    0 = perfect diversification, 1 = total concentration
    """
    w = weights.values
    return np.sum(w ** 2)

def effective_number_diversifiers(weights: pd.Series) -> float:
    """
    Diversificators (1/HHI)
    """
    hhi = herfindahl_index(weights)
    return 1 / hhi

def top_n_concentration(portfolio_df: pd.DataFrame, n: int = 10) -> float:
    """top-N asset Weights"""
    return portfolio_df.nlargest(n, "allocation_w")["allocation_w"].sum()

def correlation_matrix(returns_df: pd.DataFrame) -> pd.DataFrame:
    """Correlation Matrix"""
    return returns_df.corr()

def plot_correlation_heatmap(corr: pd.DataFrame, title: str = "Correlation Matrix"):
    """Heatmap correlation"""
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap="RdBu_r", center=0, 
                fmt='.2f', square=True)
    plt.title(title)
    plt.tight_layout()
    plt.show()

def plot_allocation_pie(breakdown: pd.Series, title: str = "Allocation"):
    """Pie chart breakdown"""
    plt.figure(figsize=(8, 6))
    breakdown.plot(kind="pie", autopct="%1.1f%%")
    plt.ylabel("")
    plt.title(title)
    plt.tight_layout()
    plt.show()

def diversification_score(portfolio_df: pd.DataFrame) -> dict:
    """
    Diversification Score
    """
    # HHI per asset class
    hhi_ac = herfindahl_index(breakdown(portfolio_df, "asset_class"))
    
    # Top 10 concentration
    top10 = top_n_concentration(portfolio_df, 10)
    
    # Numero asset
    n_assets = len(portfolio_df)
    
    return {
        "n_assets": n_assets,
        "hhi_asset_class": hhi_ac,
        "effective_diversifiers_ac": effective_number_diversifiers(
            breakdown(portfolio_df, "asset_class")
        ),
        "top_10_concentration": top10,
        "hhi_interpretation": "Low" if hhi_ac < 0.15 else "Medium" if hhi_ac < 0.25 else "High"
    }
