from pathlib import Path

import pandas as pd


def generate_method_summary(results: pd.DataFrame) -> pd.DataFrame:
    return results.set_index("method")


def export_report(path: Path, results: pd.DataFrame) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    results.to_csv(path, index=False)
