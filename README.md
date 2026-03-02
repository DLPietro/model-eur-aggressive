Portfolio Structure
```
model-eur-aggressive/
├─ __init__.py
├─ config.py
├─ data/
│  ├─ __init__.py
│  ├─ loaders.py          # ISIN, prezzi, benchmark, macro
│  ├─ asset_master.py     # mapping ISIN → ticker, asset_class, sector, region…
├─ core/
│  ├─ __init__.py
│  ├─ asset.py            # class Asset
│  ├─ portfolio.py        # class Portfolio
│  ├─ risk_metrics.py     # Sharpe, Sortino, VaR, drawdown…
│  ├─ analytics.py        # breakdown, diversificazione, correlazioni
│  ├─ optimization.py     # mean-variance, HRP, ecc.
│  ├─ backtesting.py      # backtest & simulazioni
├─ osint/
│  ├─ __init__.py
│  ├─ sentiment.py        # FinBERT / news sentiment
│  ├─ macro.py            # dati macro da API open
├─ reporting/
│  ├─ __init__.py
│  ├─ plots.py            # grafici matplotlib/plotly
│  ├─ reports.py          # generazione report HTML/markdown/notebook
└─ notebooks/
   ├─ 01_single_portfolio_demo.ipynb
   └─ 02_optimization_demo.ipynb

```
