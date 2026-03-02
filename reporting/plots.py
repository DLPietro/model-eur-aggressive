# portfolio_engine/reporting/plots.py
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd

def plot_allocation_pie(breakdown: pd.Series, title: str):
    breakdown.plot(kind="pie", autopct="%1.1f%%", figsize=(5,5))
    plt.ylabel("")
    plt.title(title)
    plt.tight_layout()
    plt.show()

def plot_correlation_heatmap(corr: pd.DataFrame, title: str):
    plt.figure(figsize=(8,6))
    sns.heatmap(corr, cmap="RdBu_r", center=0)
    plt.title(title)
    plt.tight_layout()
    plt.show()

def plot_equity_curves(df: pd.DataFrame, title: str):
    df.plot(figsize=(8,4))
    plt.title(title)
    plt.tight_layout()
    plt.show()
