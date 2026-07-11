from pathlib import Path

import typer

from ...config import load_app_config
from ...data.loader import load_prices
from ...data.preprocessing import compute_log_returns
from ...logging_utils import setup_logging
from ...risk.var_variance_covariance import VarianceCovarianceVaR
from ...risk.var_historical import HistoricalVaR
from ...risk.var_monte_carlo import MonteCarloVaR


def run_var_cmd(
    base_cfg: Path = typer.Option(...),
    data_cfg: Path = typer.Option(...),
    var_cfg: Path = typer.Option(...),
) -> None:
    cfg = load_app_config(base_cfg, data_cfg, Path(), var_cfg, Path())
    setup_logging(cfg.base.log_dir)

    prices_ng = load_prices(cfg.data.raw_path, "nymex_ng")
    returns_ng = compute_log_returns(prices_ng)

    estimators = {
        "variance_covariance": VarianceCovarianceVaR(cfg.var.distribution),
        "historical": HistoricalVaR(),
        "monte_carlo": MonteCarloVaR(),
    }

    # Example: compute one series per method & save
    for name, est in estimators.items():
        var_series = est.estimate_var_series(
            returns_ng,
            alpha=cfg.var.confidence_levels[0],
            horizon=cfg.var.horizon_days,
            window=cfg.var.rolling_window_days,
        )
        out_path = Path("data/processed") / f"var_{name}.csv"
        out_path.parent.mkdir(parents=True, exist_ok=True)
        var_series.to_csv(out_path)
