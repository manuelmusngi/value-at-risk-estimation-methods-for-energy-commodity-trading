import numpy as np
import pandas as pd
from scipy.stats import norm

from .var_base import VaREstimator


class VarianceCovarianceVaR(VaREstimator):
    """
    Parametric VaR using mean-variance and normal distribution.
    """

    def __init__(self, distribution: str = "normal") -> None:
        self.distribution = distribution

    def estimate_var(
        self,
        returns: pd.Series,
        alpha: float,
        horizon: int,
    ) -> float:
        mu = returns.mean()
        sigma = returns.std(ddof=1)

        z = norm.ppf(1 - alpha)
        var_1d = -(mu + z * sigma)
        return float(var_1d * np.sqrt(horizon))
