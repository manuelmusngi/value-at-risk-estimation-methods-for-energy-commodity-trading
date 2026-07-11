import numpy as np
import pandas as pd

from .var_base import VaREstimator


class MonteCarloVaR(VaREstimator):
    """
    Monte Carlo VaR using simulated return paths.
    """

    def __init__(
        self,
        n_scenarios: int = 10_000,
        seed: int | None = 42,
    ) -> None:
        self.n_scenarios = n_scenarios
        self.rng = np.random.default_rng(seed)

    def estimate_var(
        self,
        returns: pd.Series,
        alpha: float,
        horizon: int,
    ) -> float:
        mu = returns.mean()
        sigma = returns.std(ddof=1)

        sims = self.rng.normal(mu, sigma, size=(self.n_scenarios, horizon))
        pnl_paths = sims.sum(axis=1)
        var = -np.quantile(pnl_paths, 1 - alpha)
        return float(var)
