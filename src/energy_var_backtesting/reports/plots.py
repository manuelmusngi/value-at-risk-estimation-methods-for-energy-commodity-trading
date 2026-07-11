from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd


def plot_var_vs_pnl(
    pnl: pd.Series,
    var_series: pd.Series,
    out_path: Path,
) -> None:
    aligned = pd.concat([pnl, var_series], axis=1, join="inner").dropna()
    plt.figure(figsize=(10, 5))
    plt.plot(aligned.index, aligned.iloc[:, 0], label="P&L")
    plt.plot(aligned.index, -aligned.iloc[:, 1], label="VaR", color="red")
    plt.legend()
    plt.tight_layout()
    out_path.parent.mkdir(parents=True, exist_ok=True)
    plt.savefig(out_path)
    plt.close()
