from pathlib import Path
from typing import Any, Dict

import yaml
from pydantic import BaseModel


class BaseConfig(BaseModel):
    log_dir: Path = Path("logs")
    random_seed: int = 42


class DataConfig(BaseModel):
    raw_path: Path
    interim_path: Path
    processed_path: Path
    instruments: Dict[str, Dict[str, Any]]


class LSTMConfig(BaseModel):
    input_window: int
    forecast_horizon: int
    hidden_size: int
    num_layers: int
    dropout: float
    batch_size: int
    epochs: int
    learning_rate: float


class VaRConfig(BaseModel):
    methods: list[str]
    confidence_levels: list[float]
    horizon_days: int
    rolling_window_days: int
    distribution: str


class BacktestConfig(BaseModel):
    start_date: str
    end_date: str
    evaluation_metrics: list[str]
    output_dir: Path


class AppConfig(BaseModel):
    base: BaseConfig
    data: DataConfig
    lstm: LSTMConfig
    var: VaRConfig
    backtest: BacktestConfig


def _load_yaml(path: Path) -> Dict[str, Any]:
    with path.open("r") as f:
        return yaml.safe_load(f)


def load_app_config(
    base_cfg: Path,
    data_cfg: Path,
    lstm_cfg: Path,
    var_cfg: Path,
    backtest_cfg: Path,
) -> AppConfig:
    base = BaseConfig(**_load_yaml(base_cfg))
    data = DataConfig(**_load_yaml(data_cfg))
    lstm = LSTMConfig(**_load_yaml(lstm_cfg))
    var = VaRConfig(**_load_yaml(var_cfg))
    backtest = BacktestConfig(**_load_yaml(backtest_cfg))

    return AppConfig(
        base=base,
        data=data,
        lstm=lstm,
        var=var,
        backtest=backtest,
    )
