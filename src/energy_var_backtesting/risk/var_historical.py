import numpy as np
import pandas as pd

from .var_base import VaREstimator


class HistoricalVaR(VaREstimator):
    """
    Historical simulation VaR using empirical distribution of returns.
    """

    def estimate_var(
        self,
        returns: pd.Series,
        alpha: float,
        horizon: int,
    ) -> float:
        sorted_ret = returns.sort_values()
        idx = int((1 - alpha) * len(sorted_ret))
        var_1d = -sorted_ret.iloc[idx]
        return float(var_1d * np.sqrt(horizon))
