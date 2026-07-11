from pathlib import Path
from typing import Tuple

import numpy as np
import pandas as pd
import torch
from torch import nn, optim
from torch.utils.data import DataLoader, TensorDataset

from .lstm_model import PriceLSTM


def make_sequences(
    series: pd.Series, window: int, horizon: int
) -> Tuple[np.ndarray, np.ndarray]:
    values = series.values
    X, y = [], []
    for i in range(len(values) - window - horizon + 1):
        X.append(values[i : i + window])
        y.append(values[i + window : i + window + horizon])
    return np.array(X), np.array(y)


def train_lstm(cfg, train_series: pd.Series) -> PriceLSTM:
    X, y = make_sequences(train_series, cfg.input_window, cfg.forecast_horizon)
    X_t = torch.tensor(X, dtype=torch.float32).unsqueeze(-1)
    y_t = torch.tensor(y, dtype=torch.float32)

    ds = TensorDataset(X_t, y_t)
    dl = DataLoader(ds, batch_size=cfg.batch_size, shuffle=True)

    model = PriceLSTM(
        input_size=1,
        hidden_size=cfg.hidden_size,
        num_layers=cfg.num_layers,
        dropout=cfg.dropout,
    )
    criterion = nn.MSELoss()
    optimizer = optim.Adam(model.parameters(), lr=cfg.learning_rate)

    model.train()
    for epoch in range(cfg.epochs):
        for xb, yb in dl:
            optimizer.zero_grad()
            preds = model(xb)
            loss = criterion(preds, yb[:, -1].unsqueeze(-1))
            loss.backward()
            optimizer.step()
    return model


def forecast_forward_prices(
    model: PriceLSTM,
    test_series: pd.Series,
    cfg,
) -> pd.Series:
    X, _ = make_sequences(test_series, cfg.input_window, cfg.forecast_horizon)
    X_t = torch.tensor(X, dtype=torch.float32).unsqueeze(-1)
    model.eval()
    with torch.no_grad():
        preds = model(X_t).squeeze(-1).numpy()
    idx = test_series.index[cfg.input_window : cfg.input_window + len(preds)]
    return pd.Series(preds, index=idx, name="forecast_price")


def save_model(model: PriceLSTM, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    torch.save(model.state_dict(), path)


def load_model(path: Path, cfg) -> PriceLSTM:
    model = PriceLSTM(
        input_size=1,
        hidden_size=cfg.hidden_size,
        num_layers=cfg.num_layers,
        dropout=cfg.dropout,
    )
    state = torch.load(path, map_location="cpu")
    model.load_state_dict(state)
    return model
