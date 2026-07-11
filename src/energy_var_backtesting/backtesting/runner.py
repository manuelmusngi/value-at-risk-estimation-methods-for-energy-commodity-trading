from typing import Dict

import pandas as pd

from ..risk.var_base import VaREstimator
from .qps import compute_qps
from .exceptions import count_exceptions, kupiec_test


def run_backtest(
    returns: pd.Series,
    estimators: Dict[str, VaREstimator],
    alpha: float,
    horizon: int,
    window: int,
) -> pd.DataFrame:
    records = []
    for name, est in estimators.items():
        var_series = est.estimate_var_series(
            returns, alpha, horizon, window
        )
        qps = compute_qps(returns, var_series, alpha)
        n_exc = count_exceptions(returns, var_series)
        kupiec_p = kupiec_test(returns, var_series, alpha)

        records.append(
            {
                "method": name,
                "alpha": alpha,
                "horizon": horizon,
                "qps": qps,
                "exceptions": n_exc,
                "kupiec_p": kupiec_p,
            }
        )
    return pd.DataFrame(records)


def compare_methods(results: pd.DataFrame) -> pd.DataFrame:
    """
    Rank methods by QPS (lower is better).
    """
    return results.sort_values("qps")
