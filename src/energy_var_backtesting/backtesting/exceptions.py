 import numpy as np
import pandas as pd
from scipy.stats import chi2


def count_exceptions(
    realized_losses: pd.Series,
    var_series: pd.Series,
) -> int:
    aligned = pd.concat(
        [realized_losses, var_series], axis=1, join="inner"
    ).dropna()
    losses = aligned.iloc[:, 0]
    var = aligned.iloc[:, 1]
    exceedances = (losses < -var).astype(int)
    return int(exceedances.sum())


def kupiec_test(
    realized_losses: pd.Series,
    var_series: pd.Series,
    alpha: float,
) -> float:
    """
    Kupiec proportion of failures test p-value.
    """
    aligned = pd.concat(
        [realized_losses, var_series], axis=1, join="inner"
    ).dropna()
    losses = aligned.iloc[:, 0]
    var = aligned.iloc[:, 1]
    exceedances = (losses < -var).astype(int)

    n = len(exceedances)
    x = exceedances.sum()
    p = alpha

    lr = -2 * (
        np.log(((1 - p) ** (n - x) * p**x))
        - np.log(((1 - x / n) ** (n - x) * (x / n) ** x))
    )
    p_value = 1 - chi2.cdf(lr, df=1)
    return float(p_value)
