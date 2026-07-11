import pandas as pd


def compute_qps(
    realized_losses: pd.Series,
    var_series: pd.Series,
    alpha: float,
) -> float:
    """
    Quadratic Probability Score for VaR exceedances.
    """
    aligned = pd.concat(
        [realized_losses, var_series], axis=1, join="inner"
    ).dropna()
    losses = aligned.iloc[:, 0]
    var = aligned.iloc[:, 1]

    exceedances = (losses < -var).astype(int)
    p_hat = exceedances.mean()
    return float((p_hat - alpha) ** 2)
