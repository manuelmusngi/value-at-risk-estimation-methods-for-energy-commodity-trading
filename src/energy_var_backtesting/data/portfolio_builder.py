from typing import Dict

import pandas as pd


def build_portfolio(
    prices_map: Dict[str, pd.DataFrame],
    weights: Dict[str, float],
    price_col: str = "close",
) -> pd.Series:
    """
    Build a portfolio price series from instrument prices and weights.
    """
    idx = None
    for df in prices_map.values():
        idx = df.index if idx is None else idx.union(df.index)

    combined = pd.DataFrame(index=idx)
    for name, df in prices_map.items():
        combined[name] = df[price_col].reindex(idx).ffill()

    w = pd.Series(weights)
    portfolio_price = (combined[w.index] * w).sum(axis=1)
    return portfolio_price


def mark_to_market(portfolio_price: pd.Series) -> pd.Series:
    """
    Compute daily P&L from portfolio prices.
    """
    return portfolio_price.diff().dropna()
