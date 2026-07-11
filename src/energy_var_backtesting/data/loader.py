from pathlib import Path
from typing import Literal

import pandas as pd


Instrument = Literal["nymex_ng", "ttf_ng"]


def load_prices(data_root: Path, instrument: Instrument) -> pd.DataFrame:
    """
    Load raw price data for a given instrument.

    Expects CSV with at least: date, close.
    """
    file_map = {
        "nymex_ng": data_root / "raw" / "nymex_ng.csv",
        "ttf_ng": data_root / "raw" / "ttf_ng.csv",
    }
    path = file_map[instrument]
    df = pd.read_csv(path, parse_dates=["date"])
    df = df.sort_values("date").set_index("date")
    return df


def save_processed(df: pd.DataFrame, path: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_csv(path)
