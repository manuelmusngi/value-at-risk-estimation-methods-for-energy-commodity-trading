from abc import ABC, abstractmethod

import pandas as pd


class VaREstimator(ABC):
    """
    Base interface for VaR estimators.
    """

    @abstractmethod
    def estimate_var(
        self,
        returns: pd.Series,
        alpha: float,
        horizon: int,
    ) -> float:
        ...

    def estimate_var_series(
        self,
        returns: pd.Series,
        alpha: float,
        horizon: int,
        window: int,
    ) -> pd.Series:
        vars = []
        idx = []
        for i in range(window, len(returns)):
            window_ret = returns.iloc[i - window : i]
            vars.append(self.estimate_var(window_ret, alpha, horizon))
            idx.append(returns.index[i])
        return pd.Series(vars, index=idx, name=f"VaR_{alpha}_{horizon}")
