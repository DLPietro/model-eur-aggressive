Portfolio Structure
```
model-eur-aggressive/
├─ __init__.py
├─ config.py
├─ data/
│  ├─ __init__.py
│  ├─ loaders.py          # ISIN and prices
│  ├─ asset_master.py     # mapping ISIN → ticker, asset_class, sector, region…
├─ core/
│  ├─ __init__.py
│  ├─ asset.py            # class Asset
│  ├─ portfolio.py        # class Portfolio
│  ├─ risk_metrics.py     # Sharpe, Sortino, VaR, drawdown…
│  ├─ analytics.py        # breakdown, diversificazione, correlation
│  ├─ optimization.py     # mean-variance, HRP, ecc.
│  ├─ backtesting.py      # backtest
├─ osint/
│  ├─ __init__.py
│  ├─ sentiment.py        # FinBERT / news sentiment
│  ├─ macro.py            # API open (ongoing)
├─ reporting/
│  ├─ __init__.py
│  ├─ plots.py            # matplotlib/plotly plots
│  ├─ reports.py          # report
└─ notebooks/
   ├─ 01_single_portfolio_demo.ipynb
   └─ 02_optimization_demo.ipynb

```

