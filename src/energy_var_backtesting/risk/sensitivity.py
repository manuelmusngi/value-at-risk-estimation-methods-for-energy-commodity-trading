from typing import Dict, List

import pandas as pd

from .var_base import VaREstimator


def run_sensitivity(
    returns: pd.Series,
    estimators: Dict[str, VaREstimator],
    confidence_levels: List[float],
    horizons: List[int],
    window: int,
) -> pd.DataFrame:
    records = []
    for name, est in estimators.items():
        for alpha in confidence_levels:
            for h in horizons:
                var_series = est.estimate_var_series(
                    returns, alpha, h, window
                )
                records.append(
                    {
                        "method": name,
                        "alpha": alpha,
                        "horizon": h,
                        "mean_var": var_series.mean(),
                        "max_var": var_series.max(),
                    }
                )
    return pd.DataFrame(records)
