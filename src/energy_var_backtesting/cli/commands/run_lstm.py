from pathlib import Path

import typer

from ...config import load_app_config
from ...data.loader import load_prices
from ...data.preprocessing import compute_log_returns
from ...logging_utils import setup_logging
from ...models.lstm_pipeline import train_lstm, save_model


def run_lstm_cmd(
    base_cfg: Path = typer.Option(...),
    data_cfg: Path = typer.Option(...),
    lstm_cfg: Path = typer.Option(...),
) -> None:
    cfg = load_app_config(
        base_cfg, data_cfg, lstm_cfg, Path(), Path()
    )
    setup_logging(cfg.base.log_dir)

    prices_ng = load_prices(cfg.data.raw_path, "nymex_ng")
    returns_ng = compute_log_returns(prices_ng)

    model = train_lstm(cfg.lstm, returns_ng)
    save_model(model, Path("models/lstm_nymex_ng.pt"))
