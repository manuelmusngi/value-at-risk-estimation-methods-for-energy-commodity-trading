import typer
from pathlib import Path

from .commands.run_lstm import run_lstm_cmd
from .commands.run_var import run_var_cmd
from .commands.run_backtest import run_backtest_cmd
from .commands.run_sensitivity import run_sensitivity_cmd

app = typer.Typer(help="Energy VaR backtesting CLI")

app.command("run-lstm")(run_lstm_cmd)
app.command("run-var")(run_var_cmd)
app.command("run-backtest")(run_backtest_cmd)
app.command("run-sensitivity")(run_sensitivity_cmd)


def main() -> None:
    app()


if __name__ == "__main__":
    main()
