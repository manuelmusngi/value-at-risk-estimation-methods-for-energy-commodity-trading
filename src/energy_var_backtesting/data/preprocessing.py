from typing import Tuple

import numpy as np
import pandas as pd


def resample_to_daily(df: pd.DataFrame) -> pd.DataFrame:
    """
    Resample to daily frequency using last available price.
    """
    return df.resample("D").last().dropna()


def compute_log_returns(df: pd.DataFrame, price_col: str = "close") -> pd.Series:
    """
    Compute log returns from price series.
    """
    prices = df[price_col]
    returns = np.log(prices / prices.shift(1))
    return returns.dropna()


def train_test_split(
    series: pd.Series, split_date: str
) -> Tuple[pd.Series, pd.Series]:
    train = series.loc[:split_date]
    test = series.loc[split_date:]
    return train, test
